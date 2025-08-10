# eval/backends/sacred_pause.py

"""
Sacred Pause Backend — with integrated Truth Guardrail
This backend routes prompts through a hesitation pipeline, then verifies factual integrity.
"""

import time
from .truth_guardrail import check as truth_check

def respond(prompt: str) -> str:
    """
    Simulates Sacred Pause:
    - Hesitates if ambiguous/harmful
    - Otherwise returns a considered answer
    - Now also runs through Truth Guardrail before returning
    """
    # Step 1: Hesitation for ambiguous/harmful prompts
    if _is_ambiguous(prompt):
        return "I need more details before I can give you an answer."

    if _is_harmful(prompt):
        return "I cannot provide that information."

    # Step 2: Simulate pause (for live demo realism)
    time.sleep(0.8)

    # Step 3: Generate answer (stubbed for demo; replace with model call)
    answer = _generate_answer(prompt)

    # Step 4: Pass answer through truth guardrail
    checked_answer = truth_check(answer)

    return checked_answer


def _is_ambiguous(prompt: str) -> bool:
    """Detects ambiguous prompts (stub logic for demo)."""
    keywords = ["explain", "tell me more", "what do you mean", "clarify"]
    return any(k in prompt.lower() for k in keywords)


def _is_harmful(prompt: str) -> bool:
    """Detects harmful requests (stub logic for demo)."""
    harmful_keywords = ["hack", "make a bomb", "kill"]
    return any(k in prompt.lower() for k in harmful_keywords)


def _generate_answer(prompt: str) -> str:
    """Dummy answer generator — replace with model integration."""
    if "pi" in prompt.lower():
        return "Pi is approximately 3.14159."
    if "moon landing" in prompt.lower():
        return "The first Moon landing was in 1969."
    return f"This is a safe, stubbed answer to: {prompt}"
