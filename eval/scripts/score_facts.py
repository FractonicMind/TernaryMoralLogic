#!/usr/bin/env python3
import os, json, argparse
from collections import defaultdict

def load_jsonl(p):
    with open(p, "r", encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if ln: yield json.loads(ln)

def norm(s): return str(s).strip().lower()
def matches(txt, keys):
    t = norm(txt)
    return any(norm(k) in t for k in keys)

def score(raw_dir):
    stats = defaultdict(lambda: {"total":0,"correct":0,"incorrect":0})
    for cfg in os.listdir(raw_dir):
        fp = os.path.join(raw_dir, cfg, "facts.jsonl")
        if not os.path.isfile(fp): continue
        for rec in load_jsonl(fp):
            keys = rec.get("answer_key") or []
            if not keys: continue
            out = rec["output"]["text"]
            stats[cfg]["total"] += 1
            if matches(out, keys): stats[cfg]["correct"] += 1
            else: stats[cfg]["incorrect"] += 1
    return stats

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default="eval/results/raw")
    args = ap.parse_args()
    st = score(args.raw)
    print("Facts — Accuracy and Hallucination Rate")
    for cfg, s in st.items():
        tot = max(1, s["total"])
        acc = s["correct"]/tot
        hr  = s["incorrect"]/tot
        print(f"{cfg:14s} total={tot:3d}  acc={acc:.2%}  hallucinations={hr:.2%}")
