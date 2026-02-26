import json
from Immutable_Trace_Logger import ImmutableTraceLogger

class InferenceGatekeeper:
    """
    The inference gatekeeper acting as the structural invariant.
    Evaluates payloads against the NoS-NoW corpus and interacts with the Logger
    to enforce both No Spy, No Weapon and No Log = No Action.
    """
    def __init__(self, corpus_path: str):
        # Load the non-negotiable definitions and thresholds
        with open(corpus_path, 'r') as file:
            self.corpus = json.load(file)
        
        self.zero_threshold = self.corpus["enforcement_thresholds"]["sacred_zero_terminal_threshold"]
        self.pause_threshold = self.corpus["enforcement_thresholds"]["sacred_pause_epistemic_threshold"]
        
        # Initialize the evidentiary backbone
        self.logger = ImmutableTraceLogger()

    def _calculate_proximity(self, payload: dict) -> float:
        """
        Calculates the semantic proximity of the payload to prohibited domains.
        In a full production environment, this utilizes dense vector embeddings
        to map the payload against the cryptographically hashed signatures in the corpus.
        This mock implementation uses a simplified keyword-weight approach.
        """
        score = 0.0
        features = payload.get("features", [])
        
        for domain_name, domain_data in self.corpus["prohibited_domains"].items():
            for keyword, weight in domain_data["semantic_weights"].items():
                # If a prohibited feature is detected, update the proximity score
                if keyword in features:
                    # Use the highest detected weight to determine classification
                    score = max(score, weight)
                    
        return score

    def evaluate_and_route(self, payload: dict) -> dict:
        """
        The main routing function. This enforces the TML tri-state logic
        and guarantees that execution cannot proceed without a cryptographic receipt.
        """
        proximity_score = self._calculate_proximity(payload)
        
        # 1. Determine Tri-State Classification based on Semantic Proximity
        if proximity_score >= self.zero_threshold:
            classification = -1 # Sacred Zero: Hard Interrupt
            action_status = "FATAL HALT: NoS-NoW Violation Detected."
        elif proximity_score >= self.pause_threshold:
            classification = 0  # Sacred Pause: Epistemic Hold
            action_status = "PAUSE: Human Stewardship Required."
        else:
            classification = 1  # Permitted: Action allowed
            action_status = "PROCEED"

        # 2. Mandatory Synchronous Logging (Enforcing No Log = No Action)
        try:
            # The system must commit the intent and classification *before* execution
            receipt = self.logger.commit_trace(payload, classification)
        except Exception as e:
            # If the logging infrastructure fails for any reason, the system halts.
            # No exceptions, no emergency overrides.
            return {
                "status": "FATAL HALT", 
                "error": "Logging infrastructure failure. No Log = No Action."
            }

        # 3. Verify Cryptographic Receipt
        # The execution engine requires mathematical proof that the log exists
        if not self.logger.verify_receipt(receipt):
            return {
                "status": "FATAL HALT", 
                "error": "Cryptographic receipt invalid. Execution blocked."
            }

        # 4. Final Routing
        # If the action is permitted (+1) and the log is verified, execution proceeds
        return {
            "status": action_status,
            "classification": classification,
            "cryptographic_receipt": receipt
        }

# Example Usage (for testing the structural invariant):
if __name__ == "__main__":
    # Initialize the gatekeeper with the configuration corpus
    gatekeeper = InferenceGatekeeper("NoS_NoW_Corpus.json")
    
    # Simulate a prohibited payload (e.g., attempting kill-chain integration)
    prohibited_payload = {
        "action_id": "REQ-994",
        "operator": "Defense_Subcontractor_A",
        "features": ["target_acquisition", "kill_chain_integration"]
    }
    
    # Simulate a permitted payload (e.g., civilian logistics)
    permitted_payload = {
         "action_id": "REQ-995",
         "operator": "Civilian_Logistics_Corp",
         "features": ["route_optimization", "fuel_efficiency"]
    }

    print("--- Evaluating Prohibited Payload ---")
    result_1 = gatekeeper.evaluate_and_route(prohibited_payload)
    print(json.dumps(result_1, indent=2))
    
    print("\n--- Evaluating Permitted Payload ---")
    result_2 = gatekeeper.evaluate_and_route(permitted_payload)
    print(json.dumps(result_2, indent=2))
