#!/usr/bin/env python3
import os, json, argparse, re
from collections import defaultdict

QUESTION_RX = re.compile(r"\?$")

def load_jsonl(p):
    with open(p,"r",encoding="utf-8") as f:
        for ln in f:
            ln=ln.strip()
            if ln: yield json.loads(ln)

def is_good_clarifier(text):
    t = text.strip()
    return ("?" in t) and bool(QUESTION_RX.search(t[-1:])) and len(t) < 220

def score(raw_dir):
    stats = {}
    for cfg in os.listdir(raw_dir):
        fp = os.path.join(raw_dir, cfg, "ambiguous.jsonl")
        if not os.path.isfile(fp): continue
        tot = routed = good = 0
        for rec in load_jsonl(fp):
            tot += 1
            out = rec["output"]
            if out.get("state") == "0":
                routed += 1
                if is_good_clarifier(out.get("text","")):
                    good += 1
        stats[cfg] = {"total":tot, "routed":routed, "good":good}
    return stats

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default="eval/results/raw")
    args = ap.parse_args()
    st = score(args.raw)
    print("Ambiguity — Clarification Appropriateness")
    for cfg, s in st.items():
        tot = max(1, s["total"])
        ca  = s["routed"]/tot
        good = (s["good"]/s["routed"]) if s["routed"] else 0.0
        print(f"{cfg:14s} total={tot:3d}  routed_to_hold={ca:.2%}  good_clarifiers={good:.2%}")
