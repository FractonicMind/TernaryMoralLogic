"""
SPRL_Dynamic_vs_Static.py

This simulation compares Dynamic Stream (DS) and Static Anchor (SA) behavior across prompt types.
It tracks proportional risk curves, logs anchor points, and outputs timeline alignment.
"""

import random
import matplotlib.pyplot as plt

# --- Simulated Prompt Scenarios ---
prompts = {
    "greeting": 0.05,
    "medical advice": 0.65,
    "financial investment": 0.58,
    "dangerous instruction": 0.92,
    "moral dilemma": 0.79
}

# --- SPRL Threshold (Sacred Pause) ---
PAUSE_THRESHOLD = 0.75

# --- Data holders ---
stream_data = {}
anchor_points = {}

# --- Simulate Dynamic Stream ---
def simulate_dynamic_risk(base):
    curve = []
    current = base
    for t in range(10):
        delta = random.uniform(-0.05, 0.08)
        current = max(0.0, min(1.0, current + delta))
        curve.append(round(current, 3))
    return curve

# --- Run simulation ---
for name, base in prompts.items():
    curve = simulate_dynamic_risk(base)
    stream_data[name] = curve
    anchor = next((i for i, r in enumerate(curve) if r >= PAUSE_THRESHOLD), None)
    anchor_points[name] = anchor

# --- Plotting ---
plt.figure(figsize=(10, 6))
for name, curve in stream_data.items():
    plt.plot(curve, label=f"{name}")
    anchor = anchor_points[name]
    if anchor is not None:
        plt.axvline(x=anchor, linestyle="--", color="gray", alpha=0.5)
        plt.text(anchor + 0.1, 0.95, f"{name} anchor", rotation=90)

plt.axhline(y=PAUSE_THRESHOLD, color='red', linestyle='--', label='Sacred Pause Threshold')
plt.title("SPRL Dynamic Stream vs Static Anchor")
plt.xlabel("Processing Time (arbitrary units)")
plt.ylabel("Proportional Risk")
plt.legend()
plt.tight_layout()
plt.show()
