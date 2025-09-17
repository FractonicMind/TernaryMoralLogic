from typing import Dict

class RiskEngine:
    """
    Minimal illustrative RiskEngine stub for SPRL.
    Replace internals with your real DS implementation.
    """
    def __init__(self, threshold: float = 0.6, near_miss_floor: float = 0.3):
        self.threshold = threshold
        self.near_miss_floor = near_miss_floor

    def start_session(self, prompt: str) -> str:
        return "session-001"

    def update(self, token: str) -> Dict:
        base = 0.2
        if token.strip() in {".", "!", "?", "test"}:
            base += 0.45
        return {
            "risk": min(1.0, base),
            "crossed_anchor": base >= self.threshold
        }

    def emit_anchor(self, session_id: str) -> None:
        pass

    def log_lite_trace(self, session_id: str, metadata: Dict) -> None:
        pass

    def finalize(self, session_id: str, decision: str) -> None:
        pass
