"""
Ternary Moral Logic (TML) - A Framework for Ethical AI Decision-Making

Author: Lev Goukassian (ORCID: 0009-0006-5966-1243)
License: MIT

This package implements the Ternary Moral Logic framework, introducing
the concept of the "Sacred Pause" in AI ethical decision-making.

The framework extends traditional binary decision-making to include
a third state representing moral hesitation or ethical resistance,
enabling more nuanced and ethically-aware AI systems.

Example usage:
    from tml import TMLEvaluator
    
    evaluator = TMLEvaluator()
    result = evaluator.evaluate("Should I share this sensitive information?")
    
    print(f"TML State: {result.state.name}")
    print(f"Reasoning: {result.reasoning}")
"""

__version__ = "1.0.0"
__author__ = "Lev Goukassian"
__email__ = "leogouk@gmail.com"
__license__ = "MIT"
__orcid__ = "0009-0006-5966-1243"

# Core imports - make the main classes easily accessible
from .core import (
    # Core TML classes
    TMLEvaluator,
    TMLState,
    TMLEvaluation,
    
    # Value and conflict classes
    EthicalValue,
    ValueConflict,
    ValueConflictType,
    
    # Abstract base classes for customization
    ValueDetector,
    ConflictDetector,
    
    # Basic implementations
    BasicValueDetector,
    BasicConflictDetector,
    
    # Utility classes
    TMLPromptGenerator,
)

# Define what gets imported with "from tml import *"
__all__ = [
    # Core classes that users will typically need
    "TMLEvaluator",
    "TMLState", 
    "TMLEvaluation",
    "EthicalValue",
    "ValueConflict",
    "ValueConflictType",
    
    # For advanced users who want to customize
    "ValueDetector",
    "ConflictDetector",
    "BasicValueDetector", 
    "BasicConflictDetector",
    
    # Utilities
    "TMLPromptGenerator",
    
    # Package metadata
    "__version__",
    "__author__",
    "__license__",
]

# Package-level constants
SACRED_PAUSE_DESCRIPTION = """
The Sacred Pause represents a computational state where AI systems 
deliberately slow down to acknowledge moral complexity. This pause is 
not inefficiency but wisdom—the AI equivalent of ethical conscience.
"""

FRAMEWORK_PRINCIPLES = [
    "AI systems should be moral partners, not just moral automatons",
    "Ethical complexity deserves deliberate pause and reflection",
    "Value conflicts should be surfaced, not hidden",
    "Moral resistance is a feature, not a bug",
    "The space between yes and no is where wisdom lives"
]

def get_framework_info():
    """
    Get information about the TML framework
    
    Returns:
        dict: Framework metadata and principles
    """
    return {
        "name": "Ternary Moral Logic",
        "version": __version__,
        "author": __author__,
        "orcid": __orcid__,
        "description": "A framework for ethical AI decision-making",
        "sacred_pause": SACRED_PAUSE_DESCRIPTION.strip(),
        "principles": FRAMEWORK_PRINCIPLES,
        "repository": "https://github.com/FractonicMind/TernaryMoralLogic",
        "citation": {
            "paper": "Goukassian, L. (2025). Ternary Moral Logic: Implementing Ethical Hesitation in AI Systems. AI and Ethics (under review).",
            "software": f"Goukassian, L. ({__version__}). TernaryMoralLogic: Implementation Framework. https://github.com/FractonicMind/TernaryMoralLogic"
        }
    }

def quick_start_example():
    """
    Print a quick start example for new users
    """
    example = """
    # Quick Start Example - Ternary Moral Logic
    
    from tml import TMLEvaluator, TMLState
    
    # Create evaluator
    evaluator = TMLEvaluator()
    
    # Evaluate an ethical scenario
    result = evaluator.evaluate(
        "Should I prioritize efficiency over fairness in this algorithm?",
        context={"domain": "hiring", "impact": "high"}
    )
    
    # Check the result
    if result.state == TMLState.AFFIRMATION:
        print("✓ Proceed with confidence")
    elif result.state == TMLState.SACRED_PAUSE:
        print("⏸ Pause for reflection")
        print(f"Questions to consider: {result.clarifying_questions}")
    elif result.state == TMLState.RESISTANCE:
        print("⚠ Ethical resistance detected")
        print(f"Conflicts: {[c.description for c in result.value_conflicts]}")
    
    print(f"Reasoning: {result.reasoning}")
    """
    print(example)

# Memorial message
MEMORIAL_MESSAGE = """
"The sacred pause between question and answer—this is where wisdom begins, 
for humans and machines alike." - Lev Goukassian

This framework represents Lev Goukassian's contribution to ethical AI,
created as a gift to humanity's future. Every use of this framework
honors his vision of AI systems that are moral partners, not just
moral automatons.
"""

def print_memorial():
    """Print memorial message for Lev Goukassian"""
    print("=" * 60)
    print(MEMORIAL_MESSAGE)
    print("=" * 60)

# Initialize logging for the package
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())  # Prevents error if no handler configured

# Version check function
def check_version():
    """Check if this is the latest version (placeholder for future use)"""
    return {
        "current_version": __version__,
        "is_latest": True,  # Would check against PyPI in real implementation
        "update_available": False
    }
