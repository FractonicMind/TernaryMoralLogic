"""
TML Always Memory Framework
Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)

Core implementation with Sacred Zero enforcement and Earth protection
"""

from .core import (
    AlwaysMemory,
    TMLState,
    always_memory,
    MemoryLogger
)

from .earth import (
    EarthProtection,
    CommunityRegistry,
    check_environmental_harm,
    validate_community_directive
)

from .guardians import (
    GuardianNetwork,
    submit_to_guardians,
    verify_consensus
)

__version__ = "5.0.0"
__author__ = "Lev Goukassian"
__orcid__ = "0009-0006-5966-1243"

__all__ = [
    # Core Always Memory
    'AlwaysMemory',
    'TMLState',
    'always_memory',
    'MemoryLogger',
    
    # Earth Protection
    'EarthProtection',
    'CommunityRegistry',
    'check_environmental_harm',
    'validate_community_directive',
    
    # Guardian Network
    'GuardianNetwork',
    'submit_to_guardians',
    'verify_consensus'
]

def get_framework_info():
    """Return framework information including Earth protection status"""
    return {
        "framework": "TML-AlwaysMemory",
        "version": __version__,
        "creator": __author__,
        "orcid": __orcid__,
        "earth_protection": True,
        "principle": "No memory = No action",
        "planetary_principle": "Earth cannot testify; Always Memory speaks for it"
    }

# Decorator pattern for easy integration
from .core import always_memory

# Earth protection decorator
from .earth import with_earth_protection

