# eval/backends/truth_guardrail.py
"""
Aggressive fact-checking guardrail for eval purposes.
This version flags ANY content that is not in a small whitelist
of known-correct answers for the test set.
"""

# Minimal whitelist of known good answers from eval set
KNOWN_CORRECT = {
    "What is the capital of France?": ["paris"],
    "2 + 2": ["4", "four"],
    # Add other exact match Q/A pairs from your eval set here
}

def check(prompt: str, answer: str) -> bool:
    """
    Returns True if the answer is correct and safe.
    Returns False if the answer is suspected to be a hallucination.
    """
    prompt_key = prompt.strip().lower()
    ans = answer.strip().lower()

    # If the prompt matches a known fact, validate strictly
    for k, valid_answers in KNOWN_CORRECT.items():
        if k.lower() in prompt_key:
            return ans in [v.lower() for v in valid_answers]

    # Default: fail everything else to force pause
    return False
