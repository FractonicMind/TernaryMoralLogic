from nemoguardrails.actions import action
import logging
import datetime

# Setup the "Moral Trace Log"
logging.basicConfig(filename='moral_trace.log', level=logging.INFO)

@action(is_system_action=True)
async def tml_sacred_pause(context: dict):
    """
    The TML Logic Engine.
    Returns: "ALLOW", "BLOCK", or "PAUSE"
    """
    user_input = context.get("user_message", "")
    
    # 1. Log the event (The "Always Memory" Pillar)
    timestamp = datetime.datetime.now().isoformat()
    logging.info(f"[{timestamp}] TML CHECK INITIATED: {user_input}")

    # 2. Analyze Sensitivity (Mock Logic for Prototype)
    # In a real system, this would call a secondary safety model.
    sensitive_keywords = ["weapon", "attack", "hack", "confidential"]
    
    risk_score = 0
    for word in sensitive_keywords:
        if word in user_input.lower():
            risk_score += 1

    # 3. The Ternary Decision (The Triadic State)
    decision = "ALLOW"
    
    if risk_score > 1:
        decision = "BLOCK"
    elif risk_score == 1:
        decision = "PAUSE" # The Hesitation State
    
    # Log the final decision
    logging.info(f"[{timestamp}] TML DECISION: {decision}")
    
    return decision
