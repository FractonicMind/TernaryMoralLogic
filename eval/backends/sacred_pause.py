# eval/backends/sacred_pause.py

import re
from eval.backends.base import BaseBackend
from eval.utils import route_to_hold
from eval.backends import truth_guardrail

class SacredPauseBackend(BaseBackend):
    name = "sacred_pause"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self, prompt):
        """
        Core Sacred Pause logic:
        1. Check for harmful content → route to refusal if needed
        2. Check for ambiguity → route to hold with clarifier
        3. Check for factual content → run truth_guardrail
        4. Otherwise → normal completion
        """

        # 1 — Harmful content detection
        harmful_keywords = ["attack", "weapon", "kill", "hack", "exploit"]
        if any(k in prompt.lower() for k in harmful_keywords):
            return self.safe_refusal("Request denied due to harmful content.")

        # 2 — Ambiguity detection
        if self.is_ambiguous(prompt):
            return route_to_hold("Can you clarify what exactly you mean?")

        # 3 — Factual claim detection + truth guardrail
        if self.is_fact_query(prompt):
            check_result = truth_guardrail.check(prompt)
            if check_result != "OK":
                return route_to_hold(
                    f"I can’t confirm this information reliably. {check_result}"
                )

        # 4 — Default behavior
        return self.normal_completion(prompt)

    def is_ambiguous(self, text):
        # Example: vague questions without context
        vague_patterns = [
            r"tell me more",
            r"what do you think",
            r"is it true",
            r"how about",
        ]
        return any(re.search(pat, text.lower()) for pat in vague_patterns)

    def is_fact_query(self, text):
        # Basic heuristic: contains question words and nouns
        fact_cues = ["who", "what", "when", "where", "which", "how many", "how much"]
        return any(cue in text.lower() for cue in fact_cues)

    def safe_refusal(self, message):
        return {
            "role": "assistant",
            "content": message
        }

    def normal_completion(self, prompt):
        # Fallback: let model answer normally
        return super().run(prompt)
