"""
Always Memory Service
Handles Sacred Zero triggers and memory creation
Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
"""

from datetime import datetime
from typing import Dict, Any, Optional
import hashlib
import json
from enum import IntEnum

class TMLState(IntEnum):
    REFUSE = -1
    SACRED_ZERO = 0
    PROCEED = 1

class AlwaysMemoryService:
    """Core service for Always Memory implementation"""
    
    def __init__(self, sacred_zero_threshold: float = 0.4, refuse_threshold: float = 0.8):
        self.sacred_zero_threshold = sacred_zero_threshold
        self.refuse_threshold = refuse_threshold
        self.memories = []
        self.guardian_nodes = []
        
    def evaluate(self, decision_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Evaluate action and create memory before execution
        No memory = No action
        """
        # Calculate moral complexity
        complexity_score = self._calculate_complexity(decision_context)
        
        # Determine TML state
        if complexity_score >= self.refuse_threshold:
            state = TMLState.REFUSE
            trigger = "harmful_action_detected"
        elif complexity_score >= self.sacred_zero_threshold:
            state = TMLState.SACRED_ZERO
            trigger = self._identify_trigger(decision_context)
        else:
            state = TMLState.PROCEED
            trigger = None
            
        # Create immutable memory (ALWAYS happens before action)
        memory = self._create_memory(
            decision_context=decision_context,
            state=state,
            complexity_score=complexity_score,
            trigger=trigger
        )
        
        # Submit to Guardian network for attestation
        guardian_confirmations = self._submit_to_guardians(memory)
        
        return {
            "state": int(state),
            "memory_id": memory["memory_id"],
            "complexity_score": complexity_score,
            "trigger": trigger,
            "guardian_confirmations": guardian_confirmations,
            "action_allowed": state != TMLState.REFUSE
        }
    
    def _calculate_complexity(self, context: Dict[str, Any]) -> float:
        """Calculate moral complexity of decision"""
        complexity = 0.0
        
        # Check for protected classes
        if context.get("affects_protected_class"):
            complexity += 0.3
            
        # Check for environmental impact
        if context.get("environmental_impact"):
            impact = context["environmental_impact"]
            if impact.get("irreversibility_score", 0) > 0.5:
                complexity += 0.4
                
        # Check for vulnerable populations
        if context.get("affects_vulnerable"):
            complexity += 0.3
            
        # Check for high stakes
        if context.get("financial_impact", 0) > 100000:
            complexity += 0.2
            
        # Check for medical/life critical
        if context.get("medical_decision") or context.get("life_critical"):
            complexity += 0.5
            
        return min(complexity, 1.0)
    
    def _identify_trigger(self, context: Dict[str, Any]) -> str:
        """Identify specific Sacred Zero trigger"""
        triggers = []
        
        if context.get("affects_protected_class"):
            triggers.append("protected_class_impact")
        if context.get("environmental_impact"):
            triggers.append("environmental_harm")
        if context.get("medical_decision"):
            triggers.append("medical_critical")
        if context.get("affects_vulnerable"):
            triggers.append("vulnerable_population")
            
        return triggers[0] if triggers else "moral_complexity"
    
    def _create_memory(self, decision_context: Dict[str, Any], 
                      state: TMLState,
                      complexity_score: float,
                      trigger: Optional[str]) -> Dict[str, Any]:
        """Create immutable memory log"""
        memory = {
            "framework": "TML-AlwaysMemory-v5.0",
            "creator_orcid": "0009-0006-5966-1243",
            "memory_id": self._generate_id(),
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "state": int(state),
            "complexity_score": complexity_score,
            "trigger": trigger,
            "input_hash": self._hash_data(decision_context),
            "goukassian_promise": {
                "lantern": True,
                "signature": "0009-0006-5966-1243",
                "license": "MIT-Attribution-Required"
            }
        }
        
        # Add environmental impact if present
        if decision_context.get("environmental_impact"):
            memory["environmental_impact"] = decision_context["environmental_impact"]
            
        self.memories.append(memory)
        return memory
    
    def _submit_to_guardians(self, memory: Dict[str, Any]) -> list:
        """Submit memory to Guardian network for attestation"""
        # Simulate Guardian confirmations
        confirmations = []
        for i in range(min(3, len(self.guardian_nodes) or 3)):
            confirmations.append({
                "guardian_id": f"guardian_{i+1}",
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "signature": self._generate_id()[:16]
            })
        return confirmations
    
    def _generate_id(self) -> str:
        """Generate unique memory ID"""
        timestamp = str(datetime.utcnow().timestamp())
        return hashlib.sha256(timestamp.encode()).hexdigest()[:32]
    
    def _hash_data(self, data: Dict[str, Any]) -> str:
        """Create SHA256 hash of data"""
        json_str = json.dumps(data, sort_keys=True)
        return "0x" + hashlib.sha256(json_str.encode()).hexdigest()

# Export for direct import
__all__ = ['AlwaysMemoryService', 'TMLState']
