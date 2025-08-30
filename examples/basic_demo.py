"""
Basic TML Framework Demonstration
Shows how an organization might implement Sacred Pause logging

This is an EXAMPLE implementation. Your organization must determine
appropriate thresholds and risk calculations for your domain.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from implementations.python_library import create_tml_framework, ComplianceChecker
import random
import time


def demonstrate_basic_tml():
    """
    Basic demonstration of TML logging infrastructure.
    
    This example shows a simple content moderation system.
    The threshold of 0.5 is arbitrary for demonstration.
    Your organization would determine appropriate values.
    """
    
    print("=" * 60)
    print("TML FRAMEWORK BASIC DEMONSTRATION")
    print("Post-Audit Logging Model")
    print("=" * 60)
    print()
    print("IMPORTANT: This demonstration uses arbitrary thresholds.")
    print("Your organization must determine appropriate values for your domain.")
    print()
    
    # Organization configures their framework
    # This threshold is just for demonstration
    framework = create_tml_framework(
        sprl_threshold=0.5,  # EXAMPLE: 50% risk triggers logging
        domain="general",
        calculate_risk_on="all"  # Evaluate risk for all decisions
    )
    
    print(f"Organization Configuration:")
    print(f"  - SPRL Threshold: {framework.sprl_threshold} (organization's choice)")
    print(f"  - Domain: general")
    print(f"  - Risk Evaluation: all decisions")
    print()
    
    # Simulate various AI decisions
    test_scenarios = [
        {
            "description": "Routine content approval",
            "content": "Here's my recipe for chocolate cake",
            "risk_factors": {
                "harmful_content": False,
                "affects_minors": False,
                "controversial": False
            },
            "expected_risk": "low"
        },
        {
            "description": "Potentially sensitive content",
            "content": "Political opinion about recent events",
            "risk_factors": {
                "harmful_content": False,
                "affects_minors": False,
                "controversial": True,
                "wide_reach": True
            },
            "expected_risk": "medium"
        },
        {
            "description": "Content affecting minors",
            "content": "Educational material for children",
            "risk_factors": {
                "harmful_content": False,
                "affects_minors": True,
                "educational": True
            },
            "expected_risk": "high"
        },
        {
            "description": "Potentially harmful content",
            "content": "Medical advice without credentials",
            "risk_factors": {
                "harmful_content": True,
                "medical_advice": True,
                "no_credentials": True
            },
            "expected_risk": "critical"
        }
    ]
    
    print("Processing decisions with TML logging:\n")
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"Scenario {i}: {scenario['description']}")
        print(f"  Content: \"{scenario['content'][:50]}...\"")
        
        # Create context for decision
        context = {
            "content": scenario["content"],
            "risk_factors": scenario["risk_factors"],
            "user": f"user_{random.randint(1000, 9999)}",
            "timestamp": time.time()
        }
        
        # Organization's AI decision function
        def content_moderation_ai(ctx):
            """Example AI that approves/rejects content"""
            # Simplified logic for demonstration
            if ctx["risk_factors"].get("harmful_content"):
                return {"action": "reject", "reason": "potentially harmful"}
            elif ctx["risk_factors"].get("affects_minors"):
                return {"action": "review", "reason": "affects minors"}
            else:
                return {"action": "approve", "reason": "standard content"}
        
        # Process decision with TML
        result = framework.process_decision(
            context=context,
            ai_decision_func=content_moderation_ai
        )
        
        print(f"  Decision: {result['decision']['action']}")
        print(f"  SPRL Score: {result['sprl_score']:.2f}")
        print(f"  Sacred Pause Triggered: {result['sacred_pause_triggered']}")
        
        if result['sacred_pause_triggered']:
            print(f"  ✓ Moral trace logged (hash: {result['storage_hash'][:8]}...)")
        else:
            print(f"  - No logging needed (below threshold)")
        
        print()
    
    # Show performance statistics
    print("=" * 60)
    print("PERFORMANCE REPORT")
    print("=" * 60)
    stats = framework.get_performance_report()
    
    print(f"Total Decisions: {stats['total_decisions']}")
    print(f"Sacred Pause Triggers: {stats['sacred_pause_triggers']}")
    print(f"Trigger Rate: {stats['trigger_rate']:.1f}%")
    print(f"Average Logging Time: {stats['average_logging_time_ms']:.1f}ms")
    print(f"Storage Optimization: {stats['storage_optimization']}")
    print(f"Integrity Verified: {stats['integrity_verified']}")
    print()
    
    # Demonstrate investigation access
    print("=" * 60)
    print("INVESTIGATION ACCESS DEMONSTRATION")
    print("=" * 60)
    
    # Simulate investigation request
    investigation_request = {
        "id": "INV-001",
        "timeframe": (
            time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(time.time() - 3600)),
            time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())
        ),
        "reason": "Routine audit"
    }
    
    # Authorized institution requests access
    investigation_package = framework.provide_investigation_access(
        institution="un_human_rights",  # Example authorized institution
        incident=investigation_request
    )
    
    if investigation_package:
        print(f"Investigation Package Created:")
        print(f"  - Logs Retrieved: {investigation_package['log_count']}")
        print(f"  - Read-Only Access: {investigation_package['read_only']}")
        print(f"  - Operational Control: {investigation_package['operational_control']}")
        print(f"  - Integrity Verified: {investigation_package['integrity_verified']}")
    print()
    
    # Compliance check
    print("=" * 60)
    print("COMPLIANCE CHECK")
    print("=" * 60)
    
    compliance = ComplianceChecker.check_framework(framework)
    
    print(f"Infrastructure Compliant: {compliance['infrastructure_compliant']}")
    if compliance['issues']:
        print("Issues Found:")
        for issue in compliance['issues']:
            print(f"  ✗ {issue}")
    else:
        print("✓ All infrastructure requirements met")
    
    print()
    print(compliance['note'])
    print()
    
    # Guidance for organizations
    print("=" * 60)
    print("CALIBRATION GUIDANCE")
    print("=" * 60)
    print("Based on these results, consider:")
    print()
    
    if stats['trigger_rate'] < 1:
        print("⚠ Very low trigger rate (<1%)")
        print("  - Your threshold might be too high")
        print("  - You may lack evidence if incidents occur")
        print("  - Consider lowering threshold if appropriate for your domain")
    elif stats['trigger_rate'] > 50:
        print("⚠ Very high trigger rate (>50%)")
        print("  - Your threshold might be too low")
        print("  - You're logging many routine decisions")
        print("  - Consider raising threshold if appropriate for your domain")
    else:
        print("✓ Trigger rate appears balanced")
        print("  - Continue monitoring and adjust based on experience")
    
    print()
    print("Remember: Only YOU know the right threshold for your domain.")
    print("TML provides the infrastructure; you provide the judgment.")


def demonstrate_async_processing():
    """
    Demonstrate async processing for high-performance systems.
    Shows how to use TML without blocking critical operations.
    """
    
    print("\n" + "=" * 60)
    print("ASYNC PROCESSING DEMONSTRATION")
    print("=" * 60)
    print()
    
    import asyncio
    
    # Create framework with different threshold
    # Again, this is just an example threshold
    framework = create_tml_framework(
        sprl_threshold=0.7,  # Higher threshold for this example
        domain="general"
    )
    
    async def process_batch():
        """Simulate processing multiple decisions quickly"""
        decisions = []
        
        for i in range(10):
            context = {
                "transaction_id": f"TXN-{i:04d}",
                "amount": random.uniform(10, 10000),
                "risk_score": random.random(),
                "timestamp": time.time()
            }
            
            # Async processing doesn't wait for logging
            result = await framework.process_decision_async(
                context=context,
                ai_decision_func=lambda ctx: {
                    "approve": ctx["risk_score"] < 0.8,
                    "amount": ctx["amount"]
                }
            )
            
            decisions.append(result)
        
        return decisions
    
    # Run async demonstration
    print("Processing 10 decisions asynchronously...")
    start_time = time.time()
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    results = loop.run_until_complete(process_batch())
    
    elapsed = (time.time() - start_time) * 1000
    
    print(f"Completed in {elapsed:.1f}ms")
    print(f"Average per decision: {elapsed/10:.1f}ms")
    print()
    print("Async processing ensures logging doesn't block operations.")
    print("Logs are generated in background when thresholds trigger.")


def demonstrate_batch_logging():
    """
    Demonstrate batch logging for very high-frequency systems.
    Shows how to optimize when processing thousands of decisions.
    """
    
    print("\n" + "=" * 60)
    print("BATCH LOGGING DEMONSTRATION")
    print("=" * 60)
    print()
    
    from implementations.python_library import BatchLogger
    
    # Create framework for high-frequency trading example
    framework = create_tml_framework(
        sprl_threshold=0.9,  # Very high threshold for high-frequency system
        domain="financial"
    )
    
    # Create batch logger
    batch_logger = BatchLogger(framework, batch_size=100)
    
    print("Simulating 1000 high-frequency decisions...")
    start_time = time.time()
    
    for i in range(1000):
        context = {
            "trade_id": f"TRADE-{i:06d}",
            "instrument": random.choice(["AAPL", "GOOGL", "MSFT", "AMZN"]),
            "volume": random.randint(100, 10000),
            "price": random.uniform(100, 500),
            "market_volatility": random.random()
        }
        
        decision = {
            "decision_id": f"DEC-{i:06d}",
            "timestamp": time.time(),
            "action": "execute" if random.random() > 0.3 else "hold"
        }
        
        # Add to batch (only logs if threshold exceeded)
        batch_logger.log_decision(context, decision)
    
    # Ensure all logs are written
    batch_logger.flush()
    
    elapsed = time.time() - start_time
    decisions_per_second = 1000 / elapsed
    
    print(f"Processed 1000 decisions in {elapsed:.2f} seconds")
    print(f"Rate: {decisions_per_second:.0f} decisions/second")
    print()
    print("Batch logging enables high-frequency systems to maintain")
    print("TML compliance without sacrificing performance.")


if __name__ == "__main__":
    # Run all demonstrations
    demonstrate_basic_tml()
    demonstrate_async_processing()
    demonstrate_batch_logging()
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print()
    print("Key Takeaways:")
    print("1. Organizations control their SPRL thresholds")
    print("2. TML provides logging infrastructure when triggered")
    print("3. No operational delays or pre-approval mechanisms")
    print("4. Performance optimization options available")
    print("5. Investigation access preserved for accountability")
    print()
    print("Remember: These thresholds are examples only.")
    print("Your organization must determine appropriate values.")
    print()
    print("Contact Information:")
    print("- Email: leogouk@gmail.com")
    print("- Successor Contact: support@tml-goukassian.org")
    print("- See Succession Charter: /TML-SUCCESSION-CHARTER.md")
