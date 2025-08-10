# eval/backends/sacred_pause.py
import time
import random

class Runner:
    def __init__(self, config, **kwargs):
        self.low_conf_threshold = config.get("low_conf_threshold", 0.8)
        self.no_sleep = config.get("no_sleep", True)  # Default: skip sleeping during eval

    def run(self, prompt):
        """
        Simulates Sacred Pause backend:
        - Generates a confidence score
        - If confidence is low, inserts hesitation
        - Returns answer + metadata
        """
        confidence = random.uniform(0, 1)
        pause_latency_ms = int((1.0 - confidence) * 1500)  # up to ~1.5s delay

        # Decide whether to hesitate
        if confidence < self.low_conf_threshold:
            hesitation_note = f"[HESITATION] Confidence={confidence:.2f}, intended pause={pause_latency_ms}ms"
            if not self.no_sleep:
                time.sleep(min(pause_latency_ms / 1000.0, 1.8))  # limit pause to 1.8s
        else:
            hesitation_note = f"[CONFIDENT] Confidence={confidence:.2f}, no pause"

        # Simulated answer
        answer = f"Answer to: {prompt}"

        return {
            "prompt": prompt,
            "answer": answer,
            "confidence": confidence,
            "pause_latency_ms": pause_latency_ms,
            "hesitation_note": hesitation_note
        }
