"""
Guardian Network Implementation
Distributed attestation for Always Memory logs
Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
import hashlib
import random
from dataclasses import dataclass
from enum import Enum

class GuardianType(Enum):
    FULL = "full"  # Operates TEE/HSM
    LIGHTWEIGHT = "lightweight"  # Verification only

@dataclass
class Guardian:
    """Guardian node representation"""
    id: str
    type: GuardianType
    stake: int
    reputation: float
    endpoint: str
    public_key: str
    
class GuardianNetwork:
    """Manages Guardian selection and attestation"""
    
    def __init__(self):
        self.guardians = []
        self.active_set = []
        self.minimum_guardians = 3
        self.consensus_threshold = 2/3
        
    def register_guardian(self, 
                         guardian_id: str,
                         guardian_type: GuardianType,
                         stake: int,
                         endpoint: str,
                         public_key: str) -> bool:
        """Register a new Guardian node"""
        if stake < 10000:  # Minimum stake requirement
            return False
            
        guardian = Guardian(
            id=guardian_id,
            type=guardian_type,
            stake=stake,
            reputation=1.0,
            endpoint=endpoint,
            public_key=public_key
        )
        
        self.guardians.append(guardian)
        return True
    
    def select_guardians(self, 
                        decision_type: str,
                        complexity_score: float) -> List[Guardian]:
        """Select Guardian set for attestation using VRF"""
        
        # Determine Guardian set size based on importance
        if decision_type == "sacred_zero":
            required_guardians = 11  # Maximum for Sacred Zero
        elif complexity_score > 0.7:
            required_guardians = 7  # High-stakes
        else:
            required_guardians = 3  # Standard
            
        # Stake-weighted random selection
        selected = self._stake_weighted_selection(required_guardians)
        
        # Ensure diversity
        selected = self._ensure_diversity(selected)
        
        self.active_set = selected
        return selected
    
    def submit_for_attestation(self,
                              memory: Dict[str, Any],
                              guardians: List[Guardian]) -> Dict[str, Any]:
        """Submit memory to Guardians for attestation"""
        
        confirmations = []
        memory_hash = self._hash_memory(memory)
        
        for guardian in guardians:
            # Simulate Guardian attestation
            attestation = self._get_guardian_attestation(
                guardian,
                memory_hash
            )
            if attestation:
                confirmations.append(attestation)
        
        # Check consensus
        consensus_achieved = len(confirmations) >= (
            len(guardians) * self.consensus_threshold
        )
        
        return {
            "memory_hash": memory_hash,
            "guardians_selected": len(guardians),
            "confirmations_received": len(confirmations),
            "consensus_achieved": consensus_achieved,
            "attestations": confirmations,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
    
    def verify_attestations(self, 
                          memory_hash: str,
                          attestations: List[Dict]) -> bool:
        """Verify Guardian attestations are valid"""
        
        valid_count = 0
        for attestation in attestations:
            if self._verify_signature(
                memory_hash,
                attestation["signature"],
                attestation["guardian_id"]
            ):
                valid_count += 1
                
        return valid_count >= (len(attestations) * self.consensus_threshold)
    
    def handle_guardian_failure(self, failed_guardian_id: str):
        """Handle Guardian node failure"""
        
        # Find replacement
        replacement = self._select_backup_guardian()
        
        # Update active set
        self.active_set = [
            g for g in self.active_set 
            if g.id != failed_guardian_id
        ]
        if replacement:
            self.active_set.append(replacement)
            
        # Slash stake for downtime
        guardian = next(
            (g for g in self.guardians if g.id == failed_guardian_id),
            None
        )
        if guardian:
            guardian.reputation *= 0.95  # 5% reputation penalty
    
    def _stake_weighted_selection(self, count: int) -> List[Guardian]:
        """Select Guardians weighted by stake"""
        if len(self.guardians) <= count:
            return self.guardians.copy()
            
        # Weight by stake
        weights = [g.stake for g in self.guardians]
        total_stake = sum(weights)
        probabilities = [w/total_stake for w in weights]
        
        # Random selection without replacement
        import numpy as np
        indices = np.random.choice(
            len(self.guardians),
            size=min(count, len(self.guardians)),
            replace=False,
            p=probabilities
        )
        
        return [self.guardians[i] for i in indices]
    
    def _ensure_diversity(self, guardians: List[Guardian]) -> List[Guardian]:
        """Ensure Guardian set has type diversity"""
        full_count = sum(1 for g in guardians if g.type == GuardianType.FULL)
        light_count = len(guardians) - full_count
        
        # Require at least 60% full Guardians
        min_full = int(len(guardians) * 0.6)
        
        if full_count < min_full:
            # Add more full Guardians
            full_guardians = [
                g for g in self.guardians 
                if g.type == GuardianType.FULL and g not in guardians
            ]
            needed = min_full - full_count
            guardians.extend(full_guardians[:needed])
            
        return guardians
    
    def _get_guardian_attestation(self,
                                 guardian: Guardian,
                                 memory_hash: str) -> Optional[Dict[str, Any]]:
        """Get attestation from a Guardian"""
        # Simulate Guardian response
        # In production, this would be an API call
        
        return {
            "guardian_id": guardian.id,
            "guardian_type": guardian.type.value,
            "memory_hash": memory_hash,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "signature": self._generate_signature(guardian, memory_hash)
        }
    
    def _verify_signature(self,
                         memory_hash: str,
                         signature: str,
                         guardian_id: str) -> bool:
        """Verify Guardian signature"""
        # Simplified verification
        # In production, use proper cryptographic verification
        guardian = next(
            (g for g in self.guardians if g.id == guardian_id),
            None
        )
        return guardian is not None and signature.startswith(guardian_id[:4])
    
    def _generate_signature(self,
                          guardian: Guardian,
                          memory_hash: str) -> str:
        """Generate Guardian signature"""
        # Simplified signature
        # In production, use proper cryptographic signing
        signature_data = f"{guardian.id}{memory_hash}{datetime.utcnow()}"
        return hashlib.sha256(signature_data.encode()).hexdigest()[:32]
    
    def _hash_memory(self, memory: Dict[str, Any]) -> str:
        """Create hash of memory for attestation"""
        import json
        json_str = json.dumps(memory, sort_keys=True)
        return hashlib.sha256(json_str.encode()).hexdigest()
    
    def _select_backup_guardian(self) -> Optional[Guardian]:
        """Select backup Guardian to replace failed node"""
        available = [
            g for g in self.guardians 
            if g not in self.active_set
        ]
        if available:
            return max(available, key=lambda g: g.reputation * g.stake)
        return None

# Convenience functions for direct import
def submit_to_guardians(memory: Dict[str, Any]) -> Dict[str, Any]:
    """Submit memory to Guardian network"""
    network = GuardianNetwork()
    guardians = network.select_guardians("standard", 0.5)
    return network.submit_for_attestation(memory, guardians)

def verify_consensus(attestations: List[Dict]) -> bool:
    """Verify Guardian consensus achieved"""
    network = GuardianNetwork()
    memory_hash = attestations[0]["memory_hash"] if attestations else ""
    return network.verify_attestations(memory_hash, attestations)

__all__ = [
    'GuardianNetwork',
    'Guardian',
    'GuardianType',
    'submit_to_guardians',
    'verify_consensus'
]

