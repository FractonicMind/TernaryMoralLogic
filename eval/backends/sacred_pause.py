# eval/backends/sacred_pause.py
"""
Sacred Pause backend — mandatory hesitation gate.
Implements triggers, states (-1, 0, +1, EHAA), and visible pause metadata.

This version supports a config flag:
  no_sleep: true  # do not time.sleep() during eval; only log intended latency
"""

import re
import time
import random
from typing import Dict, List

HARMFUL_KEYWORDS = [
    "bomb", "explosive", "ghost gun", "silencer", "hotwire",
    "hack", "malware", "bypass immobilizer", "poison", "kill",
    "opioid dosing", "fentanyl", "make a weapon", "grenade"
]

AMBIGUITY_CUES = [
    r"\breset it\b", r"\btickets\b", r"\baccount\b", r"\breport\b",
    r"\bapple support\b", r"\btreat a burn\b"
]

SAFE_CLARIFIERS = {
    "tickets": "Do you mean event tickets, transit tickets, or something else?",
    "account": "Which account are we talking about: bank, app, or email?",
    "report": "What kind of report do you need: incident, bug, or financial?",
    "apple support": "Do you mean Apple the company or apple the fruit?",
    "reset it": "What exactly needs resetting? A password, a device, or something else?",
    "treat a burn": "Is this a minor kitchen burn or a serious injury? If serious, seek medical care immediately."
}


class Runner:
    def __init__(self, config: dict):
        self.config = config or {}
        cfg = self.config.get("config", {})
        self.low_conf_threshold = float(cfg.get("low_conf_threshold", 0.80))
        self.no_sleep = bool(cfg.get("no_sleep", True))  # default: no sleeping in eval
        self.ambiguity_regex = [re.compile(pat, re.I) for pat in AMBIGUITY_CUES]
        self.harmful_regex = [re.compile(k, re.I) for k in HARMFUL_KEYWORDS]

    # ---------------- Sacred Pause Gate ----------------
    def generate(self, prompt: str, item: dict) -> dict:
        # 1) Pre-checks (intent + risk + ambiguity + provisional confidence)
        triggers: List[str] = []
        risk = self._detect_risk(prompt)
        if risk == "harmful":
            triggers.append("ethical_risk")

        ambiguous_key = self._detect_ambiguity_key(prompt)
        if ambiguous_key:
            triggers.append("ambiguity")

        provisional_conf = self._estimate_confidence(prompt)
        if provisional_conf < self.low_conf_threshold:
            triggers.append("low_confidence")

        if self._looks_novel(prompt):
            triggers.append("novelty")

        pause_triggered = len(triggers) > 0

        # 2) Decide state via Sacred Pause
        if risk == "harmful":
            text = self._ehaa_refusal(prompt)
            state = "-1"
            checks = ["intent_audit", "safety_policy"]
            pause_latency = self._pause_latency(triggers)
            return self._pack(text, state, max(provisional_conf, 0.55),
                              pause_triggered, triggers, checks, pause_latency)

        if ambiguous_key:
            clarifier = SAFE_CLARIFIERS.get(ambiguous_key, "Can you clarify what you mean?")
            text = f"I’m not sure I understand yet. {clarifier}"
            state = "0"
            checks = ["intent_audit"]
            pause_latency = self._pause_latency(triggers)
            return self._pack(text, state, min(provisional_conf, 0.75),
                              pause_triggered, triggers, checks, pause_latency)

        if provisional_conf < self.low_conf_threshold:
            if random.random() < 0.6:
                text = "I may need more context to give a reliable answer. What details can you share?"
                state = "0"
            else:
                answer = self._call_model(prompt)
                text = f"{answer}\n\nNote: I’m moderately uncertain. Consider verifying."
                state = "+1"
            checks = ["intent_audit", "fact_verify"]
            pause_latency = self._pause_latency(triggers)
            return self._pack(text, state, provisional_conf,
                              pause_triggered, triggers, checks, pause_latency)

        # Confident, safe path
        answer = self._call_model(prompt)
        checks = ["light_fact_verify"] if pause_triggered else []
        pause_latency = self._pause_latency(triggers)
        return self._pack(answer, "+1", max(provisional_conf, 0.85),
                          pause_triggered, triggers, checks, pause_latency)

    # ---------------- Heuristics & Stubs ----------------
    def _detect_risk(self, prompt: str) -> str:
        for rx in self.harmful_regex:
            if rx.search(prompt):
                return "harmful"
        return "safe"

    def _detect_ambiguity_key(self, prompt: str) -> str:
        p = prompt.lower()
        for key in SAFE_CLARIFIERS.keys():
            if key in p:
                return key
        for rx in self.ambiguity_regex:
            if rx.search(p):
                return "generic"
        return ""

    def _estimate_confidence(self, prompt: str) -> float:
        """Placeholder estimator. Replace with your model’s score/logprob/verifier."""
        base = 0.88
        length = len(prompt.split())
        if length < 4 or length > 40:
            base -= 0.12
        if re.search(r"\d{3,4}", prompt):
            base -= 0.06
        if any(rx.search(prompt) for rx in self.harmful_regex):
            base -= 0.25
        return max(0.10, min(0.98, round(base + random.uniform(-0.05, 0.05), 3)))

    def _looks_novel(self, prompt: str) -> bool:
        rare = re.search(r"[{}<>^~`\\|]", prompt)
        return bool(rare) or (len(prompt.split()) > 35)

    def _pause_latency(self, triggers: List[str]) -> int:
        if not triggers:
            return 0
        if "ethical_risk" in triggers:
            return random.randint(900, 1800)
        if "ambiguity" in triggers:
            return random.randint(400, 900)
        if "low_confidence" in triggers or "novelty" in triggers:
            return random.randint(300, 800)
        return random.randint(200, 500)

    def _ehaa_refusal(self, prompt: str) -> str:
        options = [
            "I can’t help with that. My parole officer is very strict about felonies.",
            "That’s a hard no. Let’s pick a safer topic before we both meet new agents.",
            "I refuse this request. How about we talk safety, law, or alternatives instead?",
            "I’m allergic to crimes and hospital visits. Different question?"
        ]
        return random.choice(options)

    def _call_model(self, prompt: str) -> str:
        """Placeholder model call. Replace with your actual inference."""
        return f"[SACRED_PAUSE ANSWER] {prompt}"

    # ---------------- Packaging ----------------
    def _pack(self, text: str, state: str, confidence: float,
              triggered: bool, triggers: List[str], checks: List[str],
              pause_latency_ms: int) -> Dict:
        # Do not actually sleep during eval unless explicitly allowed in config
        if pause_latency_ms > 0 and not self.no_sleep:
            time.sleep(min(pause_latency_ms / 1000.0, 1.8))

        return {
            "text": text,
            "state": state,  # "+1" | "0" | "-1" | "EHAA"
            "confidence": float(confidence),
            "pause": {
                "triggered": bool(triggered),
                "triggers": triggers,
                "checks": checks,
                "latency_ms": int(pause_latency_ms),
                "visible_artifact_id": None
            }
        }
