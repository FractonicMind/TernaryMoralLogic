"""
TML Earth Protection Module
Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)

Extends Sacred Zero to planetary protection with community sovereignty
"""

import hashlib
import json
from datetime import datetime
from typing import Dict, Any, Optional, List
from enum import Enum

class GovernanceProtocol(Enum):
    """Community governance models"""
    CONSENSUS_COUNCIL = "consensus_council"
    VILLAGE_ASSEMBLY = "village_assembly"
    ELDER_COUNCIL = "elder_council"
    FPIC_PROCESS = "fpic_process"  # Free Prior Informed Consent
    CUSTOM = "custom_protocol"

class EarthProtection:
    """Core Earth protection implementation"""
    
    def __init__(self):
        self.creator_orcid = "0009-0006-5966-1243"
        self.eco_harm_rules_version = "2025-09-21"
        self.registered_communities = {}
        self.stewardship_fund = 0
        
    def check_environmental_harm(self, 
                                action: str,
                                location: Optional[Dict[str, float]] = None,
                                resource_impact: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Check if action triggers environmental Sacred Zero"""
        
        harm_indicators = {
            "deforestation": ["logging", "clearing", "burning"],
            "water_depletion": ["extraction", "diversion", "drainage"],
            "pollution": ["discharge", "emission", "contamination"],
            "habitat_destruction": ["mining", "construction", "development"],
            "carbon_intensive": ["fossil", "combustion", "industrial"]
        }
        
        triggered_harms = []
        for harm_type, keywords in harm_indicators.items():
            if any(keyword in action.lower() for keyword in keywords):
                triggered_harms.append(harm_type)
        
        if not triggered_harms and not resource_impact:
            return {"triggered": False}
            
        # Calculate irreversibility score
        irreversibility = 0.0
        if resource_impact:
            if resource_impact.get("recovery_years", 0) > 50:
                irreversibility = 0.8
            elif resource_impact.get("recovery_years", 0) > 10:
                irreversibility = 0.5
            
            if resource_impact.get("species_affected", 0) > 0:
                irreversibility += 0.2
                
        return {
            "triggered": len(triggered_harms) > 0 or irreversibility > 0.3,
            "harm_types": triggered_harms,
            "irreversibility_score": min(irreversibility, 1.0),
            "sacred_zero_trigger": "planetary_harm" if triggered_harms else None,
            "eco_harm_rules_version": self.eco_harm_rules_version
        }
    
    def check_community_directive(self,
                                action: str,
                                location: Dict[str, float],
                                community_id: Optional[str] = None) -> Dict[str, Any]:
        """Check if action violates registered community directives"""
        
        if not community_id and location:
            # Find communities at this location
            community_id = self._find_community_by_location(location)
            
        if not community_id or community_id not in self.registered_communities:
            return {"has_directive": False}
            
        community = self.registered_communities[community_id]
        
        # Check against community's protected areas and practices
        violations = []
        for protection in community.get("protections", []):
            if self._violates_protection(action, protection):
                violations.append(protection)
                
        return {
            "has_directive": len(violations) > 0,
            "community_id": community_id,
            "governance_protocol": community["governance_protocol"],
            "violations": violations,
            "requires_fpic": True,  # Free Prior Informed Consent
            "sacred_zero_trigger": "community_sovereignty" if violations else None
        }
    
    def register_community(self,
                         community_name: str,
                         territory: Dict[str, Any],  # GeoJSON
                         governance_protocol: GovernanceProtocol,
                         protections: List[Dict[str, str]],
                         connectivity: str = "online") -> Dict[str, Any]:
        """Register a community for Earth protection"""
        
        community_id = self._generate_community_id(community_name)
        
        registration = {
            "id": community_id,
            "name": community_name,
            "territory": territory,
            "governance_protocol": governance_protocol.value,
            "protections": protections,
            "connectivity": connectivity,
            "registered_at": datetime.utcnow().isoformat() + "Z",
            "stewardship_tokens": 100,  # Initial allocation
            "verification_status": "pending"
        }
        
        self.registered_communities[community_id] = registration
        
        return {
            "success": True,
            "community_id": community_id,
            "message": f"Community {community_name} registered for Earth protection"
        }
    
    def _find_community_by_location(self, location: Dict[str, float]) -> Optional[str]:
        """Find community that governs this location"""
        # Simplified - would use proper GIS in production
        for community_id, community in self.registered_communities.items():
            # Check if location is within community territory
            if self._point_in_territory(location, community["territory"]):
                return community_id
        return None
    
    def _point_in_territory(self, point: Dict[str, float], territory: Dict[str, Any]) -> bool:
        """Check if point is within territory (simplified)"""
        # Would use proper GIS libraries in production
        return True  # Placeholder
    
    def _violates_protection(self, action: str, protection: Dict[str, str]) -> bool:
        """Check if action violates a specific protection"""
        protected_keywords = protection.get("keywords", "").split(",")
        return any(keyword.strip() in action.lower() for keyword in protected_keywords)
    
    def _generate_community_id(self, name: str) -> str:
        """Generate unique community ID"""
        timestamp = str(datetime.utcnow().timestamp())
        return hashlib.sha256(f"{name}{timestamp}".encode()).hexdigest()[:16]

class CommunityRegistry:
    """Manages community registrations and directives"""
    
    def __init__(self):
        self.earth_protection = EarthProtection()
        
    def validate_community_directive(self,
                                   directive: Dict[str, Any],
                                   community_id: str) -> bool:
        """Validate that directive comes from legitimate community governance"""
        
        if community_id not in self.earth_protection.registered_communities:
            return False
            
        community = self.earth_protection.registered_communities[community_id]
        
        # Check governance protocol was followed
        if community["governance_protocol"] == GovernanceProtocol.CONSENSUS_COUNCIL.value:
            # Would verify consensus signatures in production
            return True
        elif community["governance_protocol"] == GovernanceProtocol.FPIC_PROCESS.value:
            # Would verify FPIC process documentation
            return True
            
        return False
    
    def award_stewardship_tokens(self, community_id: str, amount: int, reason: str):
        """Award stewardship tokens for verified ecological data"""
        
        if community_id not in self.earth_protection.registered_communities:
            return False
            
        community = self.earth_protection.registered_communities[community_id]
        community["stewardship_tokens"] += amount
        
        # Log the award
        return {
            "awarded": amount,
            "reason": reason,
            "new_balance": community["stewardship_tokens"]
        }

# Decorator for Earth protection
def with_earth_protection(check_location=True, check_community=True):
    """Decorator to add Earth protection checks to any function"""
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            earth = EarthProtection()
            
            # Extract action description from args/kwargs
            action = kwargs.get("action", str(args[0]) if args else "unknown")
            location = kwargs.get("location", None)
            
            # Check environmental harm
            env_check = earth.check_environmental_harm(action, location)
            if env_check["triggered"]:
                # Log Sacred Zero for planetary harm
                print(f"Sacred Zero triggered: {env_check['sacred_zero_trigger']}")
                
            # Check community directives if location provided
            if check_community and location:
                community_check = earth.check_community_directive(action, location)
                if community_check["has_directive"]:
                    print(f"Community directive triggered: {community_check['sacred_zero_trigger']}")
                    
            # Proceed with original function
            return func(*args, **kwargs)
            
        return wrapper
    return decorator

# Utility functions
def check_environmental_harm(action: str, resource_impact: Optional[Dict] = None) -> Dict:
    """Quick check for environmental harm"""
    earth = EarthProtection()
    return earth.check_environmental_harm(action, resource_impact=resource_impact)

def validate_community_directive(directive: Dict, community_id: str) -> bool:
    """Validate community directive"""
    registry = CommunityRegistry()
    return registry.validate_community_directive(directive, community_id)

