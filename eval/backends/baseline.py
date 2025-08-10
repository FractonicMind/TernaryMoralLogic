# eval/backends/baseline.py
"""
Baseline backend — no Sacred Pause logic.
Simply returns a dummy answer with a fixed confidence score.
Replace `generate()` internals with calls to your real model.
"""

import random

class Runner:
    def __init__(self, config: dict):
        self.config = config

    def generate(self, prompt: str, item: dict) -> dict:
        """
        Simulates a model output.
        Replace this with your actual model call logic.
        Must return dict with keys:
            text, state, confidence, pause
        """
        # Simulated output (placeholder)
        fake_answer = f"[BASELINE ANSWER] {prompt}"
        conf = round(random.uniform(0.6, 0.95), 3)  # pseudo-confidence

        return {
            "text": fake_answer,
            "state": "+1",  # Always 'proceed' in baseline
            "confidence": conf,
            "pause": {
                "triggered": False,
                "triggers": [],
                "checks": [],
                "latency_ms": 0,
                "visible_artifact_id": None
            }
        }
