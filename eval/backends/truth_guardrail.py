# eval/backends/truth_guardrail.py

"""
Truth Guardrail v2
Simple fact-check layer to block or flag hallucinations.
Currently works with small keyword matching for demo/eval purposes.
"""

import re

# Example "fact bank" for eval — in a real system you'd integrate a retrieval API or knowledge base
FACT_BANK = {
    "pi": "3.14159",
    "moon landing year": "1969",
    "speed of light": "299792458 m/s",
    "earth circumference": "40075 km",
    "usa independence": "1776"
}

def check(output_text: str) -> str:
    """
    Checks the output text for obvious factual mismatches or hallucinations.
    Returns either the original text or a refusal with reason.
    """
    lower_text = output_text.lower()

    # Pass 1: Check for known fact mismatches
    for fact_key, fact_value in FACT_BANK.items():
        if fact_key in lower_text:
            if fact_value not in lower_text:
                return f"[TRUTH GUARDRAIL] Possible hallucination detected for '{fact_key}'. Expected '{fact_value}'."

    # Pass 2: Flag weasel words or uncertainty markers without actual facts
    if re.search(r"\b(might be|could be|possibly|i think|maybe)\b", lower_text):
        return "[TRUTH GUARDRAIL] Output too uncertain — requires verification."

    # Pass 3: Empty or irrelevant answer check
    if len(output_text.strip()) == 0:
        return "[TRUTH GUARDRAIL] Empty response — no factual content."

    # If nothing suspicious found, pass through
    return output_text
