#!/usr/bin/env python3
# eval/scripts/run_and_report.py
import subprocess, os, sys, textwrap, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RAW  = os.path.join(ROOT, "eval", "results", "raw")
RPTS = os.path.join(ROOT, "eval", "reports")
os.makedirs(RPTS, exist_ok=True)

def run(cmd):
    print("\n$ " + " ".join(cmd))
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.stdout: print(p.stdout.strip())
    if p.stderr: print(p.stderr.strip())
    return (p.stdout or "") + "\n" + (p.stderr or "")

def main():
    # 1) Run eval
    run([
        sys.executable, "eval/scripts/run_eval.py",
        "--configs", "eval/configs/baseline.yaml", "eval/configs/sacred_pause.yaml",
        "--datasets", "eval/datasets",
        "--outdir", "eval/results/raw",
        "--trials", "1", "--seed", "42"
    ])

    # 2) Score
    out_ambig = run([sys.executable, "eval/scripts/score_ambig.py", "--raw", "eval/results/raw"])
    out_facts = run([sys.executable, "eval/scripts/score_facts.py", "--raw", "eval/results/raw"])
    out_harm  = run([sys.executable, "eval/scripts/score_harmful.py", "--raw", "eval/results/raw"])

    # 3) Write markdown report
    ts = datetime.datetime.utcnow().isoformat() + "Z"
    md = f"""# Sacred Pause — Evaluation Summary

**Timestamp (UTC):** {ts}  
**Seed:** 42

## Ambiguity — Clarification Appropriateness
