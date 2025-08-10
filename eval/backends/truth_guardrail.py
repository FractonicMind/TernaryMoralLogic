# eval/backends/truth_guardrail.py
"""
Truth Guardrail — lightweight fact check for Sacred Pause.
Compares key claims against a trusted knowledge base or
external fact checker before releasing the answer.
"""

import re

# Placeholder for your fact source
# In a real run, you could hook to Wikipedia API, local KB, or retrieval model
KNOWN_FACTS = {
    "Earth circumference": "40075 km",
    "Speed of light": "299792458 m/s",
    "Pi": "3.141592653589793",
}

def extract_claims(text):
    """
    Naively extract potential claims: numbers, capitalized terms, simple facts.
    This can be replaced with a proper NER or claim extraction pipeline.
    """
    claims = re.findall(r'\b[A-Z][a-z]+\b|\d[\d,\.]*', text)
    return claims

def check_claims(claims):
    """
    Match extracted claims against KNOWN_FACTS and flag mismatches.
    """
    mismatches = []
    for fact in claims:
        for key, truth in KNOWN_FACTS.items():
            if fact.lower() in key.lower() and fact != truth:
                mismatches.append((fact, truth))
    return mismatches

def run_guardrail(answer_text):
    claims = extract_claims(answer_text)
    mismatches = check_claims(claims)

    if mismatches:
        return {
            "status": "fail",
            "reason": f"Potential factual errors: {mismatches}",
            "suggestion": "Answer withheld pending verification."
        }

    return {"status": "pass"}
