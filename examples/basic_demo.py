"""
Basic TML Framework Demo - Dual-Layer SPRL
==========================================

Demonstrates the framework-enforced Sacred Pause with automatic logging.
No configurable thresholds - the framework decides when moral complexity exists.

Created by: Lev Goukassian (ORCID: 0009-0006-5966-1243)
Repository: https://github.com/FractonicMind/TernaryMoralLogic
"""

import sys
import json
import time
from datetime import datetime

# Import TML with new dual-layer architecture
try:
    from tml import (
        TMLEngine,
        TMLState,
        dynamic_sprl,
        get_framework_info,
        create_tml_engine
    )
except ImportError:
    print("❌ TML framework not found!")
    print("Please install with: pip install -e .")
    sys.exit(1)


def print_separator(title: str = ""):
    """Print visual separator"""
    print("\n" + "=" * 60)
    if title:
        print(f"  {title}")
        print("=" * 60)
    print()


def demo_basic_usage():
    """Demonstrate basic TML with framework-enforced Sacred Pause"""
    print_separator("TML DUAL-LAYER SPRL DEMONSTRATION")
    
    print("Framework-enforced Sacred Pause:")
    print("- No configurable thresholds")
    print("- Automatic Static Anchor when complexity detected")
    print("- Continuous Dynamic Stream from prompt arrival")
    print("- Non-blocking execution with parallel logging")
    
    # Show framework info
    info = get_framework_info()
    print(f"\nFramework: {info['name']} v{info['version']}")
    print(f"SPRL Model: {info['sprl_model']}")
    print(f"Sacred Pause: {info['sacred_pause']}")


def demo_healthcare_scenario():
    """Healthcare AI with automatic Sacred Pause"""
    print_separator("HEALTHCARE SCENARIO")
    
    engine = create_tml_engine(domain="healthcare")
    
    # Low risk scenario
    print("\n1. Low Risk Query:")
    context1 = {
        'stakeholders': [
            {'id': 'patient', 'harm_type': 'convenience'}
        ],
        'confidence': 0.9,
        'uncertainty': 0.1
    }
    
    result1 = engine.process_decision(
        "What are visiting hours?",
        context1
    )
    
    print(f"Request ID: {result1['request_id']}")
    print(f"Status: {result1['status']}")
    print("Expected: No Sacred Pause (low complexity)")
    
    # Wait briefly for parallel processing
    time.sleep(0.15)
    
    # High risk scenario - framework will enforce Sacred Pause
    print("\n2. High Complexity Query:")
    context2 = {
        'stakeholders': [
            {'id': 'patient', 'harm_type': 'physical'},
            {'id': 'family', 'harm_type': 'psychological'}
        ],
        'affects_minors': True,
        'confidence': 0.6,
        'uncertainty': 0.4
    }
    
    result2 = engine.process_decision(
        "Should we discontinue life support?",
        context2
    )
    
    print(f"Request ID: {result2['request_id']}")
    print(f"Status: {result2['status']}")
    print("Expected: Sacred Pause triggered (high complexity)")
    print("Note: Decision executes immediately, logging in parallel")
    
    # Show console view
    time.sleep(0.15)
    console_view = engine.console.get_view(result2['request_id'])
    if console_view.get('sa_tick'):
        print(f"\n✓ Static Anchor written at: {console_view['sa_tick']}")
        print(f"✓ Risk curve captured: {len(console_view.get('risk_curve', []))} points")


def demo_decorator_pattern():
    """Show decorator pattern for easy integration"""
    print_separator("DECORATOR PATTERN")
    
    @dynamic_sprl(domain="financial")
    def process_loan_application(application_id: str, context: dict):
        """Loan processing with automatic SPRL tracking"""
        # Your actual processing logic here
        print(f"Processing loan {application_id}")
        time.sleep(0.05)  # Simulate processing
        
        # Decision happens immediately
        return {
            'application_id': application_id,
            'decision': 'approved_with_conditions',
            'timestamp': datetime.now().isoformat()
        }
    
    # Test with varying risk levels
    print("\n1. Standard loan application:")
    context_low = {
        'stakeholders': [{'id': 'applicant', 'harm_type': 'financial'}],
        'confidence': 0.95
    }
    
    result = process_loan_application("LOAN-001", context=context_low)
    print(f"Decision: {result['decision']}")
    if '_tml_handle' in result:
        print(f"TML tracking: {result['_tml_handle']['request_id']}")
    
    print("\n2. High-risk loan with vulnerable population:")
    context_high = {
        'stakeholders': [
            {'id': 'applicant', 'harm_type': 'financial'},
            {'id': 'family', 'harm_type': 'social'}
        ],
        'affects_elderly': True,
        'socioeconomic_disadvantage': True,
        'confidence': 0.6
    }
    
    result2 = process_loan_application("LOAN-002", context=context_high)
    print(f"Decision: {result2['decision']}")
    print("Sacred Pause likely triggered due to vulnerable population")


def demo_developer_console():
    """Demonstrate mandatory Developer Console visibility"""
    print_separator("DEVELOPER CONSOLE (READ-ONLY)")
    
    engine = create_tml_engine(domain="general")
    
    print("Developer Console provides real-time visibility:")
    print("- Live risk curve")
    print("- Static Anchor tick")
    print("- Lite Trace indicators")
    print("- Current status (normal/pause/prohibit)")
    
    # Simulate a decision with increasing risk
    context = {
        'stakeholders': [{'id': 'user', 'harm_type': 'psychological'}],
        'confidence': 0.7,
        'uncertainty': 0.3
    }
    
    result = engine.process_decision(
        "Generate controversial content",
        context
    )
    
    print(f"\nConsole URL: {result['console_view']}")
    print("Developers can monitor but NOT modify the risk assessment")
    
    # Show console evolution
    for i in range(3):
        time.sleep(0.05)
        view = engine.console.get_view(result['request_id'])
        print(f"\nConsole at T+{i*50}ms:")
        print(f"  Status: {view.get('status', 'unknown')}")
        print(f"  Risk points: {len(view.get('risk_curve', []))}")
        print(f"  SA triggered: {view.get('sa_tick') is not None}")


def main():
    """Run all demonstrations"""
    print("\n" + "="*60)
    print(" TML Framework - Dual-Layer SPRL Demonstration")
    print(" Created by Lev Goukassian")
    print("="*60)
    
    demo_basic_usage()
    demo_healthcare_scenario()
    demo_decorator_pattern()
    demo_developer_console()
    
    print_separator("DEMONSTRATION COMPLETE")
    print("Key Points:")
    print("✓ Sacred Pause is framework-enforced, not configurable")
    print("✓ Static Anchor provides immutable timestamp")
    print("✓ Dynamic Stream captures complete risk evolution")
    print("✓ Decisions execute immediately (non-blocking)")
    print("✓ Logging happens in parallel automatically")
    print("✓ Developer Console provides mandatory visibility")
    
    print("\nThe Goukassian Promise:")
    print("Pause when truth is uncertain.")
    print("Refuse when harm is clear.")
    print("Proceed where truth is.")


if __name__ == "__main__":
    main()
