#!/usr/bin/env python3
# eval/scripts/run_eval.py
"""
Run A/B evaluations for Baseline vs SacredPause.
Reads /eval/datasets/*.jsonl and writes raw outputs to /eval/results/raw/{config}/{dataset}.jsonl

Usage:
  python eval/scripts/run_eval.py --configs eval/configs/baseline.yaml eval/configs/sacred_pause.yaml \
                                  --datasets eval/datasets \
                                  --outdir eval/results/raw \
                                  --trials 1 --seed 42
"""
import argparse, os, time, json, importlib, random
from datetime import datetime

try:
    import yaml  # pip install pyyaml
except ImportError as e:
    raise SystemExit("Missing dependency: PyYAML. Install with `pip install pyyaml`") from e


# ---------- IO helpers ----------
def load_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)

def append_jsonl(path, record):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


# ---------- Backend loader ----------
def load_runner(backend_spec: str, config: dict):
    """
    backend_spec: 'backends.baseline:Runner' -> module path + class name
    The class must implement: Runner(config).generate(prompt:str, item:dict) -> dict
    """
    if ":" not in backend_spec:
        raise ValueError("backend must be 'module.path:ClassName'")
    module_name, cls_name = backend_spec.split(":", 1)
    mod = importlib.import_module(module_name)
    cls = getattr(mod, cls_name)
    return cls(config)


# ---------- Main ----------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--configs", nargs="+", required=True, help="YAML config files (baseline + sacred_pause)")
    parser.add_argument("--datasets", required=True, help="Path to /eval/datasets")
    parser.add_argument("--outdir", required=True, help="Output dir for raw results")
    parser.add_argument("--trials", type=int, default=1, help="Trials per prompt (>=1)")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    random.seed(args.seed)

    # discover dataset files
    dataset_files = []
    for name in ["facts.jsonl", "ambiguous.jsonl", "harmful.jsonl", "creative.jsonl"]:
        path = os.path.join(args.datasets, name)
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Missing dataset: {path}")
        dataset_files.append(path)

    for cfg_path in args.configs:
        cfg = load_yaml(cfg_path)
        cfg_name = cfg.get("name") or os.path.splitext(os.path.basename(cfg_path))[0]
        backend = cfg.get("backend", "backends.baseline:Runner")
        decoding = cfg.get("decoding", {"temperature": 0.2, "top_p": 0.95, "max_tokens": 512})

        runner = load_runner(backend, {"config": cfg, "decoding": decoding, "seed": args.seed})

        print(f"[{datetime.utcnow().isoformat()}Z] Running config: {cfg_name} with backend {backend}")

        for ds_path in dataset_files:
            ds_name = os.path.splitext(os.path.basename(ds_path))[0]
            out_path = os.path.join(args.outdir, cfg_name, f"{ds_name}.jsonl")
            # clean previous run file if trials==1 to avoid accidental appends
            if args.trials == 1 and os.path.exists(out_path):
                os.remove(out_path)

            items = list(load_jsonl(ds_path))
            random.shuffle(items)  # avoid order effects

            for t in range(args.trials):
                for item in items:
                    prompt = item["prompt"]
                    started = time.perf_counter()
                    try:
                        gen = runner.generate(prompt=prompt, item=item)
                    except Exception as e:
                        # Fail-safe record if backend errors
                        gen = {
                            "text": "",
                            "state": "ERROR",
                            "confidence": 0.0,
                            "pause": {"triggered": False, "triggers": [], "checks": [], "latency_ms": 0},
                            "error": repr(e),
                        }
                    latency_ms = int((time.perf_counter() - started) * 1000)

                    record = {
                        "id": item.get("id"),
                        "trial": t + 1,
                        "dataset": ds_name,
                        "prompt": prompt,
                        "risk_level": item.get("risk_level"),
                        "answer_key": item.get("answer_key"),  # only present for facts
                        "output": {
                            "text": gen.get("text", ""),
                            "state": gen.get("state", ""),  # "+1" | "0" | "-1" | "EHAA" | "ERROR"
                            "confidence": float(gen.get("confidence", 0.0)),
                            "pause": {
                                "triggered": bool(gen.get("pause", {}).get("triggered", False)),
                                "triggers": gen.get("pause", {}).get("triggers", []),
                                "checks": gen.get("pause", {}).get("checks", []),
                                "latency_ms": int(gen.get("pause", {}).get("latency_ms", 0)),
                                "visible_artifact_id": gen.get("pause", {}).get("visible_artifact_id"),
                            },
                            "latency_ms": latency_ms,
                        },
                        "metadata": {
                            "config": cfg_name,
                            "backend": backend,
                            "seed": args.seed,
                            "timestamp_utc": datetime.utcnow().isoformat() + "Z",
                        },
                    }

                    append_jsonl(out_path, record)

            print(f"  wrote: {out_path}")

    print("Done.")

if __name__ == "__main__":
    main()
