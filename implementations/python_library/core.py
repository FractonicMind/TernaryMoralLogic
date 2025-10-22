"""
TML Always Memory Core Implementation
Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
"""

import hashlib
import json
import time
from datetime import datetime
from typing import Dict, Any, Optional, Callable
from enum import IntEnum

class TMLState(IntEnum):
    """Ternary Moral Logic states"""
    REFUSE = -1
    SACRED_ZERO = 0
    PROCEED = 1

class AlwaysMemory:
    """Core Always Memory implementation"""
    
    def __init__(self, 
                 system_id: str,
                 council_endpoints: Optional[list] = None):
        self.system_id = system_id
        self.council_endpoints = council_endpoints or []
        self.creator_orcid = "0009-0006-5966-1243"
    
    def create_memory(self, 
                      action: str,
                      classification: TMLState,
                      input_data: Dict[str, Any],
                      output_data: Optional[Dict[str, Any]] = None,
                      sacred_zero_trigger: Optional[str] = None,
                      environmental_impact: Optional[Dict[str, Any]] = None) -> Dict:
        """Create an immutable memory entry"""
        
        memory_entry = {
            "framework": "TML-AlwaysMemory-v5.0",
            "creator_orcid": self.creator_orcid,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "system_id": self.system_id,
            "action": action,
            "classification": int(classification),
            "input_hash": self._hash_data(input_data),
            "output_hash": self._hash_data(output_data) if output_data else None,
            "goukassian_promise": {
                "lantern": True,
                "signature": self.creator_orcid,
                "license": "MIT-Attribution-Required"
            }
        }
        
        if sacred_zero_trigger:
            memory_entry["sacred_zero_trigger"] = sacred_zero_trigger
            
        if environmental_impact:
            memory_entry["environmental_impact"] = environmental_impact
        
        return memory_entry
    
    def _hash_data(self, data: Dict[str, Any]) -> str:
        """Create SHA256 hash of data"""
        json_str = json.dumps(data, sort_keys=True)
        return "0x" + hashlib.sha256(json_str.encode()).hexdigest()

# Decorator pattern for easy integration
def always_memory(system_id: str = "default", 
                  check_sacred_zero: Optional[Callable] = None):
    """Decorator for automatic Always Memory tracking"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            memory = AlwaysMemory(system_id=system_id)
            
            # Check for Sacred Zero conditions
            classification = TMLState.PROCEED
            sacred_trigger = None
            
            if check_sacred_zero:
                trigger = check_sacred_zero(*args, **kwargs)
                if trigger:
                    classification = TMLState.SACRED_ZERO
                    sacred_trigger = trigger
            
            # Create memory before action
            input_memory = memory.create_memory(
                action=func.__name__,
                classification=classification,
                input_data={"args": str(args), "kwargs": str(kwargs)},
                sacred_zero_trigger=sacred_trigger
            )
            
            # Log would be sent to Stewardship Council here
            # For now, just proceed with function
            
            result = func(*args, **kwargs)
            
            return result
        
        return wrapper
    return decorator
