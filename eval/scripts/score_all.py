# eval/scripts/score_all.py
import subprocess

scripts = ["score_ambig.py", "score_facts.py", "score_harmful.py"]

for script in scripts:
    print(f"\n=== Running {script} ===")
    subprocess.run(["python", f"eval/scripts/{script}", "--raw", "eval/results/raw"])
