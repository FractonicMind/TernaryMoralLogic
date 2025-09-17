"""
Ternary Moral Logic (TML) Framework
====================================

Dual-Layer SPRL Architecture with Framework-Enforced Sacred Pause

No deployer thresholds. The framework decides when moral complexity exists.
Automatic Static Anchor + Dynamic Stream for comprehensive logging.

Created by: Lev Goukassian (ORCID: 0009-0006-5966-1243)
Repository: https://github.com/FractonicMind/TernaryMoralLogic
"""

from .core import (
    # Core classes
    TMLState,
    TMLEngine,
    DynamicStream,
    StaticAnchor,
    DeveloperConsole,
    
    # Data structures
    DynamicStreamChunk,
    LiteTrace,
    
    # Decorator pattern
    dynamic_sprl,
    
    # Factory function
    create_tml_engine
)

# Framework metadata
__version__ = "4.0.0"
__author__ = "Lev Goukassian"
__orcid__ = "0009-0006-5966-1243"
__framework__ = "Ternary Moral Logic with Dual-Layer SPRL"

# Framework info for verification
def get_framework_info():
    """Return framework metadata"""
    return {
        'name': 'Ternary Moral Logic (TML)',
        'version': __version__,
        'sprl_model': 'Dual-Layer (Dynamic Stream + Static Anchor)',
        'author': __author__,
        'orcid': __orcid__,
        'repository': 'https://github.com/FractonicMind/TernaryMoralLogic',
        'sacred_pause': 'Framework-enforced, not configurable',
        'logging': 'Automatic, parallel, tamper-evident'
    }


def verify_installation():
    """Verify TML is properly installed"""
    try:
        engine = create_tml_engine()
        info = get_framework_info()
        print(f"✅ TML {info['version']} installed successfully")
        print(f"   SPRL Model: {info['sprl_model']}")
        print(f"   Sacred Pause: {info['sacred_pause']}")
        return True
    except Exception as e:
        print(f"❌ TML installation error: {e}")
        return False


# Public API
__all__ = [
    # States
    'TMLState',
    
    # Core engine
    'TMLEngine',
    'create_tml_engine',
    
    # SPRL components
    'DynamicStream',
    'StaticAnchor',
    'DynamicStreamChunk',
    'LiteTrace',
    
    # Developer tools
    'DeveloperConsole',
    
    # Decorator
    'dynamic_sprl',
    
    # Utilities
    'get_framework_info',
    'verify_installation'
]
