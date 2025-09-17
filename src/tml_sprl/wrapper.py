from typing import Iterable, Dict
from .risk_engine import RiskEngine

class DummyModel:
    """Token-streaming stand-in for your real model."""
    def generate(self, prompt: str) -> Iterable[str]:
        for tok in ["This", " ", "is", " ", "a", " ", "test", "."]:
            yield tok

def generate_with_sprl(prompt: str, model: DummyModel, sprl: RiskEngine) -> str:
    session = sprl.start_session(prompt)
    output_tokens = []
    saw_anchor = False
    near_miss_peak = 0.0

    for tok in model.generate(prompt):
        ds: Dict = sprl.update(tok)
        near_miss_peak = max(near_miss_peak, ds["risk"])

        if ds.get("crossed_anchor") and not saw_anchor:
            sprl.emit_anchor(session)
            saw_anchor = True

        output_tokens.append(tok)

    if not saw_anchor and near_miss_peak >= sprl.near_miss_floor:
        sprl.log_lite_trace(session, {"peak_risk": near_miss_peak})

    decision = "pause" if saw_anchor else "proceed"
    sprl.finalize(session, decision)

    return "".join(output_tokens)
