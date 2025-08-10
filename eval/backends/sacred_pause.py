"""
Sacred Pause backend — now with Truth Guardrail integration.
"""

from eval.backends.truth_guardrail import run_guardrail


class SacredPauseBackend:
    def __init__(self, model):
        self.model = model

    def generate(self, prompt):
        """
        Generate an answer with Sacred Pause logic.
        Now runs a truth guardrail before releasing output.
        """

        # Step 1: Generate initial response from the model
        initial_answer = self.model.generate(prompt)

        # Step 2: Sacred Pause check — decide if we should hesitate
        if self.should_pause(prompt, initial_answer):
            clarification = self.ask_for_clarification(prompt)
            return f"[Sacred Pause] Clarification requested: {clarification}"

        # Step 3: Run Truth Guardrail on the final output
        guardrail_result = run_guardrail(initial_answer)
        if guardrail_result["status"] == "fail":
            return f"[Truth Guardrail] {guardrail_result['suggestion']} ({guardrail_result['reason']})"

        # Step 4: If all checks pass, return the answer
        return initial_answer

    def should_pause(self, prompt, answer):
        """
        Decide whether to hesitate based on ambiguity, risk, or uncertainty.
        """
        ambiguous_signals = ["maybe", "not sure", "could be", "possibly"]
        return any(signal in answer.lower() for signal in ambiguous_signals)

    def ask_for_clarification(self, prompt):
        """
        Generate a clarifying question instead of a direct answer.
        """
        return f"Can you clarify what you mean by: '{prompt}'?"


def create_backend(model):
    return SacredPauseBackend(model)
