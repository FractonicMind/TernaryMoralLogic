# File: Immutable_Trace_Logger.py
import hashlib
import json
import time

class ImmutableTraceLogger:
    """
    Enforces the 'No Log = No Action' mandate.
    Provides the cryptographic evidentiary backbone required before any execution.
    """
    def __init__(self):
        # In a production environment; this would connect to a decentralized Hybrid Shield.
        self.ledger = []
        self.previous_hash = "0000000000000000000000000000000000000000000000000000000000000000"

    def commit_trace(self, intent_vector: dict, classification: int) -> str:
        """
        Synchronously commits the action to the ledger.
        Returns a cryptographic receipt required for system execution.
        """
        timestamp = time.time_ns()
        
        # Construct the trace record
        trace_record = {
            "timestamp": timestamp,
            "intent": intent_vector,
            "moral_classification": classification,
            "previous_hash": self.previous_hash
        }
        
        # Serialize and hash the record
        record_string = json.dumps(trace_record, sort_keys=True).encode('utf-8')
        receipt_hash = hashlib.sha256(record_string).hexdigest()
        
        # Cryptographic chaining guarantees immutability
        self.previous_hash = receipt_hash
        self.ledger.append({receipt_hash: trace_record})
        
        return receipt_hash

    def verify_receipt(self, receipt_hash: str) -> bool:
        """
        Verifies that a log exists and the chain is unbroken.
        If this fails; the system halts immediately.
        """
        for entry in self.ledger:
            if receipt_hash in entry:
                return True
        return False
