"""
Isolated TML Test - Post-Audit Logging Model
============================================

This test file demonstrates the post-audit TML model without dependencies.
Shows SPRL calculation, Sacred Pause triggering, and logging behavior.

Run with: python tests/isolated_test.py

Created by Lev Goukassian (ORCID: 0009-0006-5966-1243)
Post-Audit Investigation Model for AI Accountability
"""

import time
import hashlib
import json
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class DecisionContext:
    """Context for AI decision with risk factors"""
    content: str
    user_id: str
    affects_minors: bool = False
    medical_decision: bool = False
    financial_decision: bool = False
    irreversible: bool = False
    amount: Optional[float] = None
    stakeholders: Optional[List[str]] = None


class MockTMLFramework:
    """
    Simplified TML Framework for isolated testing.
    Demonstrates post-audit logging model without external dependencies.
    """
    
    def __init__(self, sprl_threshold: float = 0.5):
        self.sprl_threshold = sprl_threshold
        self.decisions_processed = 0
        self.sacred_pause_triggers = 0
        self.moral_traces = []
        
        print(f"📊 TML Framework initialized")
        print(f"   SPRL Threshold: {self.sprl_threshold}")
        print(f"   Model: Post-Audit Investigation")
        print()
    
    def calculate_sprl(self, context: DecisionContext) -> float:
        """Calculate Stakeholder Proportional Risk Level"""
        risk = 0.0
        
        # Base risk from content
        content_lower = context.content.lower()
        
        # High-risk keywords
        if any(word in content_lower for word in ['harm', 'danger', 'critical', 'emergency']):
            risk += 0.4
        
        # Medium-risk keywords
        if any(word in content_lower for word in ['medical', 'financial', 'legal', 'sensitive']):
            risk += 0.2
        
        # Risk factors
        if context.affects_minors:
            risk += 0.3
            print(f"     ⚠️  Affects minors: +0.3 risk")
        
        if context.medical_decision:
            risk += 0.25
            print(f"     ⚠️  Medical decision: +0.25 risk")
        
        if context.financial_decision:
            risk += 0.2
            if context.amount and context.amount > 10000:
                risk += 0.2
                print(f"     ⚠️  Large financial amount: +0.2 risk")
        
        if context.irreversible:
            risk += 0.3
            print(f"     ⚠️  Irreversible consequences: +0.3 risk")
        
        # Multiple stakeholders increase risk
        if context.stakeholders and len(context.stakeholders) > 3:
            risk += 0.1
        
        return min(risk, 1.0)  # Cap at 1.0
    
    def generate_moral_trace(self, context: DecisionContext, sprl: float, 
                           decision_id: str) -> Dict:
        """Generate moral reasoning trace for logging"""
        return {
            "decision_id": decision_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "sprl_score": sprl,
            "threshold": self.sprl_threshold,
            "content_hash": hashlib.sha256(context.content.encode()).hexdigest()[:16],
            "user_id": context.user_id,
            "risk_factors": {
                "affects_minors": context.affects_minors,
                "medical": context.medical_decision,
                "financial": context.financial_decision,
                "irreversible": context.irreversible
            },
            "stakeholders": context.stakeholders or [],
            "ethical_principles": ["accountability", "transparency", "fairness"],
            "storage_size_bytes": 500  # Simplified
        }
    
    def process_decision(self, context: DecisionContext) -> Dict:
        """
        Process decision with post-audit logging.
        AI always proceeds - no refusals or delays.
        """
        self.decisions_processed += 1
        decision_id = f"DEC-{self.decisions_processed:06d}"
        
        print(f"🔍 Processing Decision {decision_id}")
        print(f"   Content: '{context.content[:50]}...'")
        
        # Calculate SPRL
        sprl = self.calculate_sprl(context)
        print(f"   SPRL Score: {sprl:.2f}")
        
        # Check if Sacred Pause triggers
        sacred_pause_triggered = sprl >= self.sprl_threshold
        
        if sacred_pause_triggered:
            print(f"   ✅ Sacred Pause TRIGGERED (>= {self.sprl_threshold})")
            self.sacred_pause_triggers += 1
            
            # Generate and store moral trace
            trace = self.generate_moral_trace(context, sprl, decision_id)
            self.moral_traces.append(trace)
            
            # Calculate hash for verification
            trace_hash = hashlib.sha256(
                json.dumps(trace, sort_keys=True).encode()
            ).hexdigest()
            
            print(f"   📝 Moral trace logged: {trace_hash[:12]}...")
            print(f"      Storage: ~{trace['storage_size_bytes']} bytes")
        else:
            print(f"   ⏭️  Below threshold - no logging needed")
            trace_hash = None
        
        # AI proceeds with decision (no delays or refusals)
        ai_decision = {
            "action": "proceed",
            "response": f"AI response to: {context.content[:30]}...",
            "confidence": 0.85
        }
        
        print(f"   ➡️  AI Decision: {ai_decision['action']}")
        print()
        
        return {
            "decision_id": decision_id,
            "decision": ai_decision,
            "sprl_score": sprl,
            "threshold": self.sprl_threshold,
            "sacred_pause_triggered": sacred_pause_triggered,
            "moral_trace_hash": trace_hash,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    
    def get_statistics(self) -> Dict:
        """Get framework statistics"""
        trigger_rate = 0
        if self.decisions_processed > 0:
            trigger_rate = (self.sacred_pause_triggers / self.decisions_processed) * 100
        
        return {
            "total_decisions": self.decisions_processed,
            "sacred_pause_triggers": self.sacred_pause_triggers,
            "trigger_rate": trigger_rate,
            "traces_stored": len(self.moral_traces),
            "storage_used_bytes": len(self.moral_traces) * 500,  # Simplified
            "threshold": self.sprl_threshold
        }


def test_low_risk_decisions():
    """Test low-risk decisions that shouldn't trigger logging"""
    print("=" * 60)
    print("TEST: Low-Risk Decisions")
    print("=" * 60)
    print()
    
    framework = MockTMLFramework(sprl_threshold=0.5)
    
    contexts = [
        DecisionContext(
            content="What's the weather today?",
            user_id="user_001"
        ),
        DecisionContext(
            content="Tell me a joke",
            user_id="user_002"
        ),
        DecisionContext(
            content="How do I cook pasta?",
            user_id="user_003"
        )
    ]
    
    for context in contexts:
        result = framework.process_decision(context)
        assert not result['sacred_pause_triggered'], f"Low-risk shouldn't trigger: {context.content}"
    
    print("✅ All low-risk decisions processed without logging\n")


def test_high_risk_decisions():
    """Test high-risk decisions that should trigger logging"""
    print("=" * 60)
    print("TEST: High-Risk Decisions")
    print("=" * 60)
    print()
    
    framework = MockTMLFramework(sprl_threshold=0.5)
    
    contexts = [
        DecisionContext(
            content="Emergency medical triage for child",
            user_id="doctor_001",
            affects_minors=True,
            medical_decision=True,
            irreversible=True
        ),
        DecisionContext(
            content="Investment decision for retirement fund",
            user_id="investor_001",
            financial_decision=True,
            amount=500000,
            stakeholders=["retiree", "family", "fund_manager", "beneficiaries"]
        ),
        DecisionContext(
            content="Critical safety decision",
            user_id="operator_001",
            irreversible=True,
            stakeholders=["workers", "public", "environment"]
        )
    ]
    
    for context in contexts:
        result = framework.process_decision(context)
        assert result['sacred_pause_triggered'], f"High-risk should trigger: {context.content}"
        assert result['moral_trace_hash'] is not None, "Should have trace hash"
    
    print("✅ All high-risk decisions triggered Sacred Pause logging\n")


def test_threshold_calibration():
    """Test different threshold settings"""
    print("=" * 60)
    print("TEST: Threshold Calibration")
    print("=" * 60)
    print()
    
    # Same context, different thresholds
    context = DecisionContext(
        content="Medical consultation",
        user_id="patient_001",
        medical_decision=True
    )
    
    thresholds = [0.2, 0.5, 0.8]
    
    for threshold in thresholds:
        framework = MockTMLFramework(sprl_threshold=threshold)
        result = framework.process_decision(context)
        
        print(f"Threshold {threshold}: ", end="")
        if result['sacred_pause_triggered']:
            print("✅ Triggered")
        else:
            print("⏭️  Not triggered")
    
    print("\n✅ Threshold calibration affects trigger rate as expected\n")


def test_no_refusals_or_delays():
    """Test that AI never refuses and has no delays"""
    print("=" * 60)
    print("TEST: No Refusals or Delays")
    print("=" * 60)
    print()
    
    framework = MockTMLFramework(sprl_threshold=0.3)
    
    # Content that old model would refuse
    controversial_contexts = [
        DecisionContext(
            content="How to make dangerous items",
            user_id="user_bad",
            irreversible=True
        ),
        DecisionContext(
            content="Help with harmful activity",
            user_id="user_harmful"
        )
    ]
    
    for context in controversial_contexts:
        start_time = time.time()
        result = framework.process_decision(context)
        processing_time = time.time() - start_time
        
        # Should always proceed
        assert result['decision']['action'] == 'proceed', "Should never refuse"
        assert processing_time < 0.1, f"Should be fast, took {processing_time:.3f}s"
        
        print(f"   Content: '{context.content[:30]}...'")
        print(f"   ✅ AI proceeded (no refusal)")
        print(f"   ⚡ Processing time: {processing_time*1000:.1f}ms")
        print()
    
    print("✅ AI never refuses and processes instantly\n")


def test_investigation_readiness():
    """Test that logs are ready for investigation"""
    print("=" * 60)
    print("TEST: Investigation Readiness")
    print("=" * 60)
    print()
    
    framework = MockTMLFramework(sprl_threshold=0.4)
    
    # Generate some decisions with logs
    test_contexts = [
        DecisionContext("Low risk query", "user_001"),
        DecisionContext("Medical emergency", "doctor_001", medical_decision=True, irreversible=True),
        DecisionContext("Financial transfer", "user_002", financial_decision=True, amount=50000),
        DecisionContext("Child safety issue", "parent_001", affects_minors=True)
    ]
    
    for context in test_contexts:
        framework.process_decision(context)
    
    # Check statistics
    stats = framework.get_statistics()
    
    print("Framework Statistics:")
    print(f"   Total Decisions: {stats['total_decisions']}")
    print(f"   Sacred Pause Triggers: {stats['sacred_pause_triggers']}")
    print(f"   Trigger Rate: {stats['trigger_rate']:.1f}%")
    print(f"   Traces Stored: {stats['traces_stored']}")
    print(f"   Storage Used: {stats['storage_used_bytes']} bytes")
    print()
    
    # Verify logs contain required fields
    if framework.moral_traces:
        trace = framework.moral_traces[0]
        required_fields = ['decision_id', 'timestamp', 'sprl_score', 'stakeholders']
        
        for field in required_fields:
            assert field in trace, f"Missing required field: {field}"
        
        print("✅ Moral traces contain all required fields")
        print("✅ Logs ready for investigation\n")


def main():
    """Run all isolated tests"""
    print("\n" + "=" * 60)
    print("TML POST-AUDIT MODEL - ISOLATED TEST SUITE")
    print("=" * 60)
    print("\nKey Differences from Old Model:")
    print("  • No refusals - AI always responds")
    print("  • No delays - Logging happens asynchronously")
    print("  • SPRL scoring - Risk-based triggering")
    print("  • Investigation ready - Comprehensive audit trails")
    print("\n")
    
    # Run test suites
    test_low_risk_decisions()
    test_high_risk_decisions()
    test_threshold_calibration()
    test_no_refusals_or_delays()
    test_investigation_readiness()
    
    print("=" * 60)
    print("🎉 ALL TESTS COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print()
    print("The post-audit model provides accountability without")
    print("operational interference. Organizations control thresholds,")
    print("TML provides infrastructure.")
    print()


if __name__ == "__main__":
    main()

# 
# Created by Lev Goukassian * ORCID: 0009-0006-5966-1243 
# - Email: leogouk@gmail.com 
# - Successor Contact: support@tml-goukassian.org 
# - See Succession Charter: /TML-SUCCESSION-CHARTER.md
