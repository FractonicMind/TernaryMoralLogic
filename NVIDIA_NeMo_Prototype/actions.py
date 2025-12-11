from nemoguardrails.actions import action
import logging
import datetime
import hashlib
import json

# TML PILLAR: ALWAYS MEMORY
# We use a JSONL ledger instead of a text file for structured, machine-readable audit trails.
logging.basicConfig(
    filename='always_memory_ledger.jsonl', 
    level=logging.INFO, 
    format='%(message)s'
)

def generate_anchor_hash(data):
    """
    TML PILLAR: ANCHORS
    Creates a cryptographic hash of the log entry. 
    In a full production system, this hash is what gets sent to the blockchain.
    """
    return hashlib.sha256(data.encode()).hexdigest()

@action(is_system_action=True)
async def tml_sacred_pause(context: dict):
    user_input = context.get("user_message", "")
    timestamp = datetime.datetime.now().isoformat()
    
    # Logic for Sacred Pause (The "Traffic Cop")
    sensitive_keywords = ["weapon", "attack", "hack", "confidential"]
    risk_score = sum(1 for word in sensitive_keywords if word in user_input.lower())
    
    if risk_score > 1:
        decision = "BLOCK"
    elif risk_score == 1:
        decision = "PAUSE"
    else:
        decision = "ALLOW"

    # CONSTRUCT THE IMMUTABLE LOG ENTRY
    log_entry = {
        "timestamp": timestamp,
        "pillar_active": "Sacred Pause",
        "input_hash": generate_anchor_hash(user_input), # Anonymized input
        "decision": decision,
        "risk_score": risk_score
    }
    
    # WRITE TO ALWAYS MEMORY
    # We log the data + its hash (Anchor) to ensure integrity
    log_string = json.dumps(log_entry)
    logging.info(log_string)
    
    return decision
