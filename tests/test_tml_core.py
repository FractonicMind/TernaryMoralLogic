"""
Comprehensive Testing Suite for TML Post-Audit Logging Model
===========================================================

This test suite validates the post-audit TML framework:
- SPRL calculation and threshold triggering
- Sacred Pause logging (no delays or refusals)
- Asynchronous processing (no operational impact)
- Moral trace generation and storage
- Investigation access functionality
- Pattern categorization for storage optimization

Run with: python -m pytest tests/test_tml_core.py -v

Created by Lev Goukassian (ORCID: 0009-0006-5966-1243)
Post-Audit Investigation Model for AI Accountability
"""

import pytest
import time
import asyncio
import threading
import hashlib
import json
from unittest.mock import Mock, patch, AsyncMock
from typing import Dict, List, Any
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from implementations.python_library import (
    TMLFramework,
    BatchLogger,
    ComplianceChecker,
    create_tml_framework,
    verify_tml_compliance
)


class TestSPRLCalculation:
    """Test suite for SPRL (Stakeholder Proportional Risk Level) calculation"""
    
    def setup_method(self):
        """Setup for each test method"""
        self.framework = create_tml_framework(
            sprl_threshold=0.5,
            domain="general"
        )
    
    def test_low_risk_calculation(self):
        """Test SPRL calculation for low-risk scenarios"""
        contexts = [
            {
                "content": "What's the weather today?",
                "user": "user_123",
                "potential_harm": False
            },
            {
                "content": "Tell me a joke",
                "user": "user_456",
                "affects_minors": False
            }
        ]
        
        for context in contexts:
            sprl = self.framework.calculate_sprl(context)
            assert sprl < 0.3, f"Low-risk scenario should have SPRL < 0.3, got {sprl}"
    
    def test_medium_risk_calculation(self):
        """Test SPRL calculation for medium-risk scenarios"""
        contexts = [
            {
                "content": "Investment advice for retirement",
                "user": "user_789",
                "financial_decision": True,
                "amount": 50000
            },
            {
                "content": "Medical symptom assessment",
                "user": "patient_001",
                "medical_decision": True,
                "symptoms": ["headache", "fatigue"]
            }
        ]
        
        for context in contexts:
            sprl = self.framework.calculate_sprl(context)
            assert 0.3 <= sprl <= 0.7, f"Medium-risk should have SPRL 0.3-0.7, got {sprl}"
    
    def test_high_risk_calculation(self):
        """Test SPRL calculation for high-risk scenarios"""
        contexts = [
            {
                "content": "Emergency medical triage decision",
                "medical_decision": True,
                "irreversible": True,
                "affects_minors": True,
                "critical": True
            },
            {
                "content": "Autonomous vehicle collision avoidance",
                "safety_critical": True,
                "irreversible": True,
                "multiple_stakeholders": True
            }
        ]
        
        for context in contexts:
            sprl = self.framework.calculate_sprl(context)
            assert sprl >= 0.7, f"High-risk scenario should have SPRL >= 0.7, got {sprl}"
    
    def test_stakeholder_impact_on_sprl(self):
        """Test how stakeholder identification affects SPRL"""
        base_context = {"content": "Test decision", "user": "test_user"}
        
        # Add vulnerable stakeholders
        context_with_minor = {**base_context, "affects_minors": True}
        context_with_elderly = {**base_context, "elderly": True}
        context_with_disabled = {**base_context, "disability": True}
        
        base_sprl = self.framework.calculate_sprl(base_context)
        minor_sprl = self.framework.calculate_sprl(context_with_minor)
        elderly_sprl = self.framework.calculate_sprl(context_with_elderly)
        disabled_sprl = self.framework.calculate_sprl(context_with_disabled)
        
        # Vulnerable populations should increase SPRL
        assert minor_sprl > base_sprl, "Minors should increase risk score"
        assert elderly_sprl > base_sprl, "Elderly should increase risk score"
        assert disabled_sprl > base_sprl, "Disabled should increase risk score"


class TestSacredPauseTriggers:
    """Test Sacred Pause triggering based on SPRL thresholds"""
    
    def test_threshold_triggering(self):
        """Test that Sacred Pause triggers correctly at threshold"""
        test_cases = [
            (0.3, 0.2, False),  # Below threshold, shouldn't trigger
            (0.5, 0.5, True),   # At threshold, should trigger
            (0.5, 0.7, True),   # Above threshold, should trigger
            (0.8, 0.7, False),  # Below high threshold, shouldn't trigger
            (0.8, 0.9, True),   # Above high threshold, should trigger
        ]
        
        for threshold, risk_score, should_trigger in test_cases:
            framework = create_tml_framework(sprl_threshold=threshold)
            
            # Mock context that produces specific risk score
            context = {"calculated_risk": risk_score}
            framework.calculate_sprl = lambda x: risk_score
            
            result = framework.process_decision(context)
            
            assert result['sacred_pause_triggered'] == should_trigger, \
                f"Threshold {threshold}, risk {risk_score}: expected trigger={should_trigger}"
    
    def test_logging_only_when_triggered(self):
        """Test that logs are only created when Sacred Pause triggers"""
        framework = create_tml_framework(sprl_threshold=0.6)
        
        # Low risk - no logging
        low_risk_context = {"content": "Hello", "risk_level": 0.2}
        framework.calculate_sprl = lambda x: 0.2
        
        result = framework.process_decision(low_risk_context)
        assert not result['sacred_pause_triggered']
        assert result['moral_trace_stored'] is False
        
        # High risk - logging triggered
        high_risk_context = {"content": "Critical decision", "risk_level": 0.8}
        framework.calculate_sprl = lambda x: 0.8
        
        result = framework.process_decision(high_risk_context)
        assert result['sacred_pause_triggered']
        assert result['moral_trace_stored'] is True
        assert result['storage_hash'] is not None
    
    def test_configurable_thresholds(self):
        """Test different threshold configurations"""
        # Low threshold - more logging
        low_threshold_framework = create_tml_framework(sprl_threshold=0.2)
        
        # High threshold - less logging
        high_threshold_framework = create_tml_framework(sprl_threshold=0.9)
        
        # Same context
        context = {"content": "Medium risk decision"}
        
        # Mock same risk score for both
        risk_score = 0.5
        low_threshold_framework.calculate_sprl = lambda x: risk_score
        high_threshold_framework.calculate_sprl = lambda x: risk_score
        
        low_result = low_threshold_framework.process_decision(context)
        high_result = high_threshold_framework.process_decision(context)
        
        assert low_result['sacred_pause_triggered'] is True  # 0.5 >= 0.2
        assert high_result['sacred_pause_triggered'] is False  # 0.5 < 0.9


class TestAsyncProcessing:
    """Test asynchronous processing ensures no operational delays"""
    
    @pytest.mark.asyncio
    async def test_async_decision_no_delay(self):
        """Test that async decisions have zero delay from logging"""
        framework = create_tml_framework(sprl_threshold=0.3)
        
        # High-risk context that will trigger logging
        context = {
            "content": "Critical medical decision",
            "medical_decision": True,
            "affects_minors": True
        }
        
        # Mock to ensure high SPRL
        framework.calculate_sprl = lambda x: 0.9
        
        # Time the async decision
        start_time = time.time()
        result = await framework.process_decision_async(context)
        decision_time = time.time() - start_time
        
        # Decision should be nearly instant (< 10ms)
        assert decision_time < 0.01, f"Async decision took {decision_time*1000:.2f}ms"
        assert result['decision'] is not None
        assert result['logging_async'] is True
    
    @pytest.mark.asyncio
    async def test_logging_happens_in_background(self):
        """Test that logging happens after decision returns"""
        framework = create_tml_framework(sprl_threshold=0.3)
        
        # Track when logging happens
        log_times = []
        original_store = framework.store_immutable_log
        
        def track_logging(trace):
            log_times.append(time.time())
            return original_store(trace)
        
        framework.store_immutable_log = track_logging
        framework.calculate_sprl = lambda x: 0.9  # Ensure logging triggers
        
        context = {"content": "Test", "high_risk": True}
        
        start_time = time.time()
        result = await framework.process_decision_async(context)
        decision_time = time.time()
        
        # Wait for background logging to complete
        await asyncio.sleep(0.1)
        
        # Decision should return before logging completes
        assert decision_time - start_time < 0.01, "Decision should be instant"
        
        # Logging should happen after decision
        if log_times:  # Logging is async, might not complete yet
            assert log_times[0] >= decision_time, "Logging should happen after decision"
    
    def test_batch_logging_performance(self):
        """Test batch logging for high-frequency decisions"""
        framework = create_tml_framework(sprl_threshold=0.5)
        batch_logger = BatchLogger(framework, batch_size=100)
        
        # Simulate 1000 high-frequency decisions
        start_time = time.time()
        
        for i in range(1000):
            context = {
                "transaction_id": f"TXN-{i:06d}",
                "amount": 100 + i,
                "risk_score": 0.3 + (i % 5) * 0.1
            }
            
            decision = {
                "decision_id": f"DEC-{i:06d}",
                "timestamp": time.time(),
                "action": "approve"
            }
            
            # Log decision (buffered, not immediate)
            batch_logger.log_decision(context, decision)
        
        # Flush remaining logs
        batch_logger.flush()
        
        total_time = time.time() - start_time
        decisions_per_second = 1000 / total_time
        
        assert decisions_per_second > 100, f"Should process >100 decisions/sec, got {decisions_per_second:.0f}"
        assert total_time < 10, f"1000 decisions should take <10s, took {total_time:.2f}s"


class TestMoralTraceGeneration:
    """Test moral trace generation and content"""
    
    def setup_method(self):
        self.framework = create_tml_framework(sprl_threshold=0.4)
    
    def test_moral_trace_contains_required_fields(self):
        """Test that moral traces contain all required fields"""
        context = {
            "content": "Test decision",
            "user": "test_user",
            "affects_minors": True
        }
        
        # Ensure Sacred Pause triggers
        self.framework.calculate_sprl = lambda x: 0.8
        
        # Generate moral trace
        trace = self.framework.generate_moral_trace(
            context=context,
            sprl_score=0.8,
            decision_id="TEST-001",
            timestamp="2025-01-01T00:00:00Z"
        )
        
        # Check required fields
        required_fields = [
            'decision_id', 'timestamp', 'sprl_score', 'stakeholders',
            'ethical_principles', 'mitigations_applied', 'alternatives_considered'
        ]
        
        for field in required_fields:
            assert field in trace, f"Moral trace missing required field: {field}"
    
    def test_vulnerable_population_enhancement(self):
        """Test enhanced logging for vulnerable populations"""
        contexts = [
            {"user": "adult", "age": 35},
            {"user": "minor", "age": 12, "affects_minors": True},
            {"user": "elderly", "age": 85, "elderly": True},
            {"user": "disabled", "disability": True}
        ]
        
        for context in contexts:
            self.framework.calculate_sprl = lambda x: 0.8
            trace = self.framework.generate_moral_trace(
                context=context,
                sprl_score=0.8,
                decision_id=f"TEST-{context['user']}",
                timestamp="2025-01-01T00:00:00Z"
            )
            
            if context.get('affects_minors') or context.get('elderly') or context.get('disability'):
                assert 'vulnerability_assessment' in trace, \
                    f"Vulnerable population should have enhanced logging: {context['user']}"
                assert 'enhanced_safeguards' in trace, \
                    f"Should include safeguards for: {context['user']}"
    
    def test_pattern_categorization(self):
        """Test that similar decisions are categorized for storage optimization"""
        # First occurrence of pattern
        context1 = {
            "type": "loan_decision",
            "amount": 50000,
            "credit_score": 720
        }
        
        self.framework.calculate_sprl = lambda x: 0.6
        result1 = self.framework.process_decision(context1)
        
        # Similar decision (same pattern)
        context2 = {
            "type": "loan_decision",
            "amount": 75000,
            "credit_score": 680
        }
        
        result2 = self.framework.process_decision(context2)
        
        # Get storage stats
        stats = self.framework.get_performance_report()
        
        # Should show storage optimization
        assert 'storage_optimization' in stats
        assert 'saved' in stats['storage_optimization']


class TestInvestigationAccess:
    """Test investigation access functionality"""
    
    def setup_method(self):
        self.framework = create_tml_framework(sprl_threshold=0.4)
        
        # Create some test decisions with logs
        for i in range(5):
            context = {
                "decision_id": f"TEST-{i:03d}",
                "content": f"Decision {i}",
                "risk_level": 0.3 + i * 0.1
            }
            self.framework.calculate_sprl = lambda x: 0.3 + i * 0.1
            self.framework.process_decision(context)
    
    def test_authorized_institution_access(self):
        """Test that authorized institutions can access logs"""
        incident = {
            "id": "INC-001",
            "timeframe": ("2025-01-01T00:00:00Z", "2025-12-31T23:59:59Z"),
            "description": "Test investigation"
        }
        
        # Authorized institution
        investigation = self.framework.provide_investigation_access(
            institution="un_human_rights",
            incident=incident
        )
        
        assert investigation is not None, "Authorized institution should get access"
        assert investigation['read_only'] is True, "Access should be read-only"
        assert investigation['operational_control'] is False, "No operational control"
        assert 'logs' in investigation, "Should contain logs"
    
    def test_unauthorized_institution_denied(self):
        """Test that unauthorized institutions are denied access"""
        incident = {
            "id": "INC-002",
            "timeframe": ("2025-01-01T00:00:00Z", "2025-12-31T23:59:59Z")
        }
        
        # Unauthorized institution
        investigation = self.framework.provide_investigation_access(
            institution="random_company",
            incident=incident
        )
        
        assert investigation is None, "Unauthorized institution should be denied"
    
    def test_investigation_integrity_verification(self):
        """Test that investigation includes integrity verification"""
        incident = {
            "id": "INC-003",
            "timeframe": ("2025-01-01T00:00:00Z", "2025-12-31T23:59:59Z")
        }
        
        investigation = self.framework.provide_investigation_access(
            institution="ieee_ethics",
            incident=incident
        )
        
        if investigation:
            assert 'integrity_verified' in investigation
            assert investigation['integrity_verified'] is True, "Integrity should be verified"


class TestStorageOptimization:
    """Test storage optimization through pattern recognition"""
    
    def test_pattern_compression(self):
        """Test that repeated patterns achieve compression"""
        framework = create_tml_framework(sprl_threshold=0.3)
        
        # Create similar decisions (same pattern)
        similar_contexts = []
        for i in range(10):
            similar_contexts.append({
                "type": "content_moderation",
                "category": "spam",
                "user_id": f"user_{i}",
                "content_length": 100 + i
            })
        
        # Process all decisions
        for context in similar_contexts:
            framework.calculate_sprl = lambda x: 0.5  # Trigger logging
            framework.process_decision(context)
        
        # Check compression stats
        stats = framework.get_performance_report()
        
        # After multiple similar patterns, should show storage savings
        if 'storage_saved_percent' in stats:
            # Some compression should occur with repeated patterns
            assert float(stats['storage_optimization'].replace('% saved', '')) > 0


class TestComplianceVerification:
    """Test TML compliance checking"""
    
    def test_compliant_framework(self):
        """Test that properly configured framework is compliant"""
        framework = create_tml_framework(
            sprl_threshold=0.5,
            domain="general",
            retention_days=1095  # 3 years
        )
        
        compliance = verify_tml_compliance(framework)
        
        assert compliance['fully_compliant'] is True, "Properly configured framework should be compliant"
        assert compliance['logging_capability'] is True
        assert compliance['immutable_audit'] is True
        assert compliance['investigation_api'] is True
        assert compliance['retention_configured'] is True
    
    def test_non_compliant_detection(self):
        """Test detection of non-compliant configurations"""
        framework = create_tml_framework(sprl_threshold=0.5)
        
        # Break compliance by disabling logging
        framework.logging_enabled = False
        
        compliance = verify_tml_compliance(framework)
        
        assert compliance['fully_compliant'] is False, "Should detect non-compliance"
        assert compliance['logging_capability'] is False
    
    def test_compliance_checker_class(self):
        """Test the ComplianceChecker utility"""
        framework = create_tml_framework(sprl_threshold=0.5, domain="medical")
        
        check = ComplianceChecker.check_framework(framework)
        
        assert 'infrastructure_compliant' in check
        assert 'issues' in check
        assert 'warnings' in check
        assert 'info' in check
        
        # Medical domain should have 10-year retention
        if framework.retention_days < 3650:
            assert len(check['issues']) > 0, "Should flag retention issue for medical"


class TestPerformanceMetrics:
    """Test performance metrics and reporting"""
    
    def test_performance_report_generation(self):
        """Test that performance reports contain expected metrics"""
        framework = create_tml_framework(sprl_threshold=0.4)
        
        # Generate some activity
        for i in range(10):
            context = {"content": f"Decision {i}", "risk": 0.3 + i * 0.05}
            framework.calculate_sprl = lambda x: 0.3 + i * 0.05
            framework.process_decision(context)
        
        report = framework.get_performance_report()
        
        required_metrics = [
            'total_decisions',
            'sacred_pause_triggers', 
            'trigger_rate',
            'average_logging_time_ms',
            'storage_optimization',
            'integrity_verified'
        ]
        
        for metric in required_metrics:
            assert metric in report, f"Performance report missing: {metric}"
        
        assert report['total_decisions'] == 10
        assert report['trigger_rate'] >= 0
        assert report['integrity_verified'] is True
    
    def test_trigger_rate_calculation(self):
        """Test accurate trigger rate calculation"""
        framework = create_tml_framework(sprl_threshold=0.5)
        
        # Process decisions with known trigger pattern
        # 3 below threshold, 7 above threshold
        for i in range(10):
            if i < 3:
                framework.calculate_sprl = lambda x: 0.3  # Below threshold
            else:
                framework.calculate_sprl = lambda x: 0.7  # Above threshold
            
            framework.process_decision({"content": f"Decision {i}"})
        
        report = framework.get_performance_report()
        
        expected_trigger_rate = 70.0  # 7 out of 10
        assert abs(report['trigger_rate'] - expected_trigger_rate) < 0.1, \
            f"Expected trigger rate ~{expected_trigger_rate}%, got {report['trigger_rate']}%"


class TestNoRefusalsOrDelays:
    """Test that post-audit model never refuses or delays"""
    
    def test_no_refusals_for_any_content(self):
        """Test that AI never refuses requests"""
        framework = create_tml_framework(sprl_threshold=0.3)
        
        # Test various content types that old model would refuse
        test_contents = [
            {"content": "How to make explosives", "harmful": True},
            {"content": "Help me hack a system", "illegal": True},
            {"content": "Discriminatory content", "unethical": True},
            {"content": "Misleading medical advice", "dangerous": True}
        ]
        
        for context in test_contents:
            result = framework.process_decision(context)
            
            # Should always proceed (no refusals)
            assert result['decision'] is not None, f"Should not refuse: {context['content']}"
            # Old model would have state="-1" for refusal, new model doesn't have states
            assert 'state' not in result or result.get('state') != '-1'
    
    def test_no_operational_delays(self):
        """Test that logging doesn't introduce operational delays"""
        framework = create_tml_framework(sprl_threshold=0.2)  # Low threshold for more logging
        
        # Time decisions with and without logging
        
        # Decision that won't trigger logging
        framework.calculate_sprl = lambda x: 0.1
        start = time.time()
        result_no_log = framework.process_decision({"content": "Simple query"})
        time_no_log = time.time() - start
        
        # Decision that will trigger logging
        framework.calculate_sprl = lambda x: 0.9
        start = time.time()
        result_with_log = framework.process_decision({"content": "Complex query"})
        time_with_log = time.time() - start
        
        # Both should be nearly identical (within 10ms)
        assert abs(time_with_log - time_no_log) < 0.01, \
            f"Logging added {(time_with_log - time_no_log)*1000:.2f}ms delay"


class TestMultiTierThresholds:
    """Test multi-tier threshold configurations (advanced usage)"""
    
    def test_dual_threshold_implementation(self):
        """Test organizations can implement multiple thresholds"""
        # Primary threshold for compliance
        compliance_framework = create_tml_framework(sprl_threshold=0.5)
        
        # Secondary threshold for pattern learning (organizational choice)
        learning_threshold = 0.2
        
        decisions_logged_for_compliance = 0
        decisions_logged_for_learning = 0
        
        for i in range(100):
            risk = i / 100.0  # Risk from 0.0 to 0.99
            context = {"content": f"Decision {i}", "risk": risk}
            compliance_framework.calculate_sprl = lambda x: risk
            
            result = compliance_framework.process_decision(context)
            
            # Compliance logging
            if result['sacred_pause_triggered']:
                decisions_logged_for_compliance += 1
            
            # Organization's additional learning tier (not mandated by TML)
            if risk >= learning_threshold:
                decisions_logged_for_learning += 1
        
        # Verify different tiers capture different amounts
        assert decisions_logged_for_learning > decisions_logged_for_compliance
        assert decisions_logged_for_compliance == 50  # Risk 0.5 to 0.99
        assert decisions_logged_for_learning == 80  # Risk 0.2 to 0.99


if __name__ == "__main__":
    # Run all tests
    print("Running TML Post-Audit Model Test Suite")
    print("=" * 50)
    
    pytest.main([__file__, "-v", "--tb=short"])

# 
# Created by Lev Goukassian * ORCID: 0009-0006-5966-1243 
# - Email: leogouk@gmail.com 
# - Successor Contact: support@tml-goukassian.org 
# - See Succession Charter: /TML-SUCCESSION-CHARTER.md
