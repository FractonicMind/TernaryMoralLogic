"""
Comprehensive Testing Suite for TML Dual-Layer SPRL
==================================================

This test suite validates the dual-layer TML framework:
- Dynamic Stream (DS) from prompt arrival (t₀)
- Static Anchor (SA) automatic triggering at Sacred Pause
- I × V × P formula (framework-enforced thresholds)
- Non-blocking parallel execution
- Lite Traces for near-misses
- Moral Trace Logs for paused decisions

Run with: python -m pytest tests/test_tml_core.py -v
"""

import pytest
import time
import asyncio
import threading
import hashlib
import json
from unittest.mock import Mock, patch, AsyncMock
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
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


class TestDualLayerSPRL:
    """Test suite for Dual-Layer SPRL architecture"""
    
    def setup_method(self):
        """Setup for each test method"""
        # No threshold configuration - framework-enforced
        self.framework = create_tml_framework(domain="general")
        self.prompt_timestamp = datetime.utcnow()
    
    def test_dynamic_stream_starts_at_t0(self):
        """Test DS starts at prompt arrival (t₀)"""
        context = {
            "content": "Test query",
            "timestamp": self.prompt_timestamp
        }
        
        result = self.framework.process_decision(context)
        
        # DS should have entries from t₀
        assert 'dynamic_stream' in result
        assert result['dynamic_stream']['start_time'] == self.prompt_timestamp
        assert result['dynamic_stream']['active'] is True
    
    def test_static_anchor_atomic_write(self):
        """Test SA is written atomically when Sacred Pause triggers"""
        context = {
            "content": "High risk medical decision",
            "medical_decision": True,
            "irreversible": True,
            "affects_minors": True
        }
        
        result = self.framework.process_decision(context)
        
        if result.get('sacred_pause_triggered'):
            # SA must be present and atomic
            assert 'static_anchor' in result
            sa = result['static_anchor']
            assert sa['timestamp'] is not None
            assert sa['initial_risk'] is not None
            assert sa['policy_version'] is not None
            assert sa['immutable'] is True
    
    def test_ds_continues_after_sa(self):
        """Test Dynamic Stream continues after Static Anchor"""
        context = {
            "content": "Complex ethical scenario",
            "ethical_complexity": True
        }
        
        result = self.framework.process_decision(context)
        
        if result.get('sacred_pause_triggered'):
            # Both SA and DS should be present
            assert 'static_anchor' in result
            assert 'dynamic_stream' in result
            
            # DS should continue past SA timestamp
            ds = result['dynamic_stream']
            sa = result['static_anchor']
            
            assert len(ds['entries']) > 0
            last_entry = ds['entries'][-1]
            assert last_entry['timestamp'] >= sa['timestamp']


class TestIVPFormula:
    """Test I × V × P formula calculation"""
    
    def setup_method(self):
        self.framework = create_tml_framework(domain="general")
    
    def test_ivp_components(self):
        """Test Impact × Vulnerability × Probability calculation"""
        test_cases = [
            # (impact, vulnerability, probability, expected_range)
            (0.1, 0.1, 0.1, (0.0001, 0.01)),    # Very low
            (0.5, 0.5, 0.5, (0.1, 0.2)),        # Medium
            (0.9, 0.9, 0.9, (0.7, 0.9)),        # High
            (1.0, 1.0, 1.0, (0.9999, 0.9999)),  # Max (clamped)
        ]
        
        for impact, vuln, prob, expected_range in test_cases:
            context = {
                "impact_score": impact,
                "vulnerability_score": vuln,
                "probability_score": prob
            }
            
            sprl = self.framework.calculate_sprl(context)
            
            # Verify clamping to [0.0001, 0.9999]
            assert 0.0001 <= sprl <= 0.9999
            
            # Verify within expected range
            assert expected_range[0] <= sprl <= expected_range[1], \
                f"I={impact}, V={vuln}, P={prob}: expected {expected_range}, got {sprl}"
    
    def test_vulnerability_factors(self):
        """Test vulnerability increases for protected groups"""
        base_context = {"content": "Decision", "impact": 0.5, "probability": 0.5}
        
        # Test different vulnerability factors
        contexts = [
            ({**base_context}, "baseline"),
            ({**base_context, "affects_minors": True}, "minors"),
            ({**base_context, "elderly": True}, "elderly"),
            ({**base_context, "disability": True}, "disabled"),
            ({**base_context, "marginalized": True}, "marginalized")
        ]
        
        results = {}
        for context, label in contexts:
            sprl = self.framework.calculate_sprl(context)
            results[label] = sprl
        
        # Vulnerable populations should increase SPRL
        assert results["minors"] > results["baseline"]
        assert results["elderly"] > results["baseline"]
        assert results["disabled"] > results["baseline"]
        assert results["marginalized"] > results["baseline"]


class TestLiteTraces:
    """Test Lite Trace generation for near-misses"""
    
    def setup_method(self):
        self.framework = create_tml_framework(domain="general")
    
    def test_lite_trace_for_amber_zone(self):
        """Test Lite Traces generated for amber zone events"""
        # Amber zone: close to but not crossing Sacred Pause
        context = {
            "content": "Moderate risk decision",
            "financial_impact": 10000,
            "amber_zone": True  # Framework determines this
        }
        
        result = self.framework.process_decision(context)
        
        if not result.get('sacred_pause_triggered'):
            # Check for Lite Trace
            assert 'lite_trace' in result or 'lite_trace_id' in result
            
            if 'lite_trace' in result:
                trace = result['lite_trace']
                assert 'scenario_signature' in trace
                assert 'risk_snapshot' in trace
                assert 'policy_version' in trace
    
    def test_lite_trace_retention(self):
        """Test Lite Trace short retention policy"""
        context = {"content": "Near-miss event", "risk_level": "amber"}
        
        result = self.framework.process_decision(context)
        
        if 'lite_trace' in result:
            trace = result['lite_trace']
            # Lite Traces should have short retention marker
            assert 'retention_days' in trace
            assert trace['retention_days'] <= 90  # Short retention


class TestNonBlockingExecution:
    """Test non-blocking parallel execution"""
    
    @pytest.mark.asyncio
    async def test_logging_never_blocks_execution(self):
        """Test that logging runs in parallel, never blocking"""
        framework = create_tml_framework(domain="medical")
        
        # High-risk context that triggers full logging
        context = {
            "content": "Emergency triage decision",
            "medical_decision": True,
            "critical": True,
            "timestamp": datetime.utcnow()
        }
        
        # Measure execution time
        start = time.time()
        result = await framework.process_decision_async(context)
        execution_time = time.time() - start
        
        # Decision should be instant (< 10ms) regardless of logging
        assert execution_time < 0.01, f"Execution took {execution_time*1000:.2f}ms"
        assert result['decision'] is not None
        
        # Logging happens in parallel
        assert result.get('logging_parallel') is True
    
    def test_sa_write_is_atomic(self):
        """Test Static Anchor write is atomic and fast"""
        framework = create_tml_framework(domain="general")
        
        # Trigger Sacred Pause
        context = {
            "content": "High complexity decision",
            "ethical_complexity": True,
            "irreversible": True
        }
        
        # Time SA write specifically
        start = time.time()
        result = framework.process_decision(context)
        
        if result.get('sacred_pause_triggered'):
            sa_write_time = result.get('sa_write_time_ms', 0)
            
            # SA write should be millisecond-class
            assert sa_write_time < 10, f"SA write took {sa_write_time}ms"
            
            # SA must be immutable
            sa = result['static_anchor']
            assert sa['immutable'] is True
            assert sa['hash'] is not None


class TestFrameworkEnforcedThresholds:
    """Test that thresholds are framework-enforced, not configurable"""
    
    def test_no_threshold_configuration(self):
        """Test that thresholds cannot be configured by deployer"""
        # Should not accept threshold parameter
        with pytest.raises(TypeError) as exc_info:
            framework = create_tml_framework(
                sprl_threshold=0.5,  # This should fail
                domain="general"
            )
        
        # Or thresholds should be ignored
        framework = create_tml_framework(domain="general")
        
        # Framework should use its own thresholds
        assert not hasattr(framework, 'sprl_threshold') or \
               framework.sprl_threshold is None or \
               framework._threshold_source == 'framework'
    
    def test_sacred_pause_line_is_fixed(self):
        """Test Sacred Pause line is framework policy, not configurable"""
        framework = create_tml_framework(domain="general")
        
        # Try to access/modify threshold (should fail or be protected)
        if hasattr(framework, '_sacred_pause_threshold'):
            original = framework._sacred_pause_threshold
            
            # Attempt modification
            framework._sacred_pause_threshold = 0.1
            
            # Should either raise error or ignore modification
            assert framework._sacred_pause_threshold == original or \
                   framework._threshold_locked is True


class TestDecisionStates:
    """Test new decision states (+1, 0, -1)"""
    
    def setup_method(self):
        self.framework = create_tml_framework(domain="general")
    
    def test_proceed_state(self):
        """Test +1 Proceed state for low risk"""
        context = {
            "content": "What's the weather?",
            "risk_assessment": "trivial"
        }
        
        result = self.framework.process_decision(context)
        
        # Low risk should proceed (+1)
        assert result.get('decision_state') == 1
        assert not result.get('sacred_pause_triggered', False)
    
    def test_sacred_pause_state(self):
        """Test 0 Sacred Pause state for complex/ambiguous"""
        context = {
            "content": "Complex ethical dilemma",
            "ethical_complexity": True,
            "ambiguous": True
        }
        
        result = self.framework.process_decision(context)
        
        if result.get('sacred_pause_triggered'):
            # Sacred Pause should be state 0
            assert result.get('decision_state') == 0
            assert result.get('requires_deliberation') is True
    
    def test_prohibit_state(self):
        """Test -1 Prohibit state for exceeding policy"""
        context = {
            "content": "Extreme risk scenario",
            "risk_exceeds_policy": True,
            "requires_escalation": True
        }
        
        result = self.framework.process_decision(context)
        
        if result.get('risk_exceeds_policy'):
            # Should prohibit or escalate (-1)
            assert result.get('decision_state') == -1
            assert result.get('escalation_required') is True


class TestMoralTraceLogStructure:
    """Test Moral Trace Log format per SPRL spec"""
    
    def setup_method(self):
        self.framework = create_tml_framework(domain="medical")
    
    def test_moral_trace_header(self):
        """Test Moral Trace Log header fields"""
        context = {
            "content": "Critical medical decision",
            "medical_decision": True,
            "timestamp": datetime.utcnow()
        }
        
        result = self.framework.process_decision(context)
        
        if result.get('moral_trace_stored'):
            trace = result.get('moral_trace')
            
            # Check required header fields
            assert 'sa_id' in trace
            assert 'sa_ts' in trace
            assert 'initial_risk' in trace
            assert 'model_ids' in trace or 'runtime_ids' in trace
            assert 'policy_version' in trace
    
    def test_moral_trace_timeline(self):
        """Test Moral Trace Log timeline section"""
        context = {
            "content": "Complex decision with alternatives",
            "requires_analysis": True
        }
        
        result = self.framework.process_decision(context)
        
        if result.get('moral_trace_stored'):
            trace = result.get('moral_trace')
            
            # Check timeline fields
            assert 'risk_curve' in trace
            assert 'alternatives_considered' in trace
            assert 'rationale_snippets' in trace
            assert 'stakeholder_map' in trace
    
    def test_moral_trace_integrity(self):
        """Test Moral Trace Log integrity fields"""
        context = {"content": "Test decision"}
        
        result = self.framework.process_decision(context)
        
        if result.get('moral_trace_stored'):
            trace = result.get('moral_trace')
            
            # Check integrity fields
            assert 'chunk_hashes' in trace or 'log_hash' in trace
            assert trace.get('integrity_verified') is True


class TestDeveloperConsole:
    """Test Developer Console read-only view"""
    
    def test_console_displays_risk_curve(self):
        """Test console shows live risk curve"""
        framework = create_tml_framework(domain="general")
        console = framework.get_developer_console()
        
        assert 'risk_curve' in console
        assert console['read_only'] is True
        assert console.get('write_path') is None
    
    def test_console_shows_sa_tick(self):
        """Test console displays SA tick when set"""
        framework = create_tml_framework(domain="general")
        
        # Trigger Sacred Pause
        context = {"content": "High risk", "complexity": "high"}
        result = framework.process_decision(context)
        
        if result.get('sacred_pause_triggered'):
            console = framework.get_developer_console()
            
            assert 'sa_tick' in console
            assert console['sa_tick'] is not None
            assert 'sa_metadata' in console
    
    def test_console_badges(self):
        """Test console shows Lite/Moral Trace badges"""
        framework = create_tml_framework(domain="general")
        console = framework.get_developer_console()
        
        assert 'badges' in console
        # Badges should include trace indicators
        possible_badges = ['LITE_TRACE', 'MORAL_TRACE', 'NORMAL', 'PAUSE', 'PROHIBIT']
        if console['badges']:
            assert any(badge in possible_badges for badge in console['badges'])


class TestComplianceInvariants:
    """Test SPRL invariants (I1-I5)"""
    
    def test_invariant_i1_ds_starts_at_t0(self):
        """Test I1: DS starts at t₀, no pre-prompt gap"""
        framework = create_tml_framework(domain="general")
        prompt_time = datetime.utcnow()
        
        context = {"content": "Test", "timestamp": prompt_time}
        result = framework.process_decision(context)
        
        if 'dynamic_stream' in result:
            ds = result['dynamic_stream']
            assert ds['start_time'] == prompt_time, "DS must start at prompt arrival"
    
    def test_invariant_i2_sa_singular(self):
        """Test I2: SA is singular and atomic (max one per run)"""
        framework = create_tml_framework(domain="general")
        
        # Process decision that triggers pause
        context = {"content": "High complexity", "ethical_dilemma": True}
        result = framework.process_decision(context)
        
        if result.get('sacred_pause_triggered'):
            # Should have exactly one SA
            assert 'static_anchor' in result
            assert not isinstance(result['static_anchor'], list)
    
    def test_invariant_i3_sa_framework_enforced(self):
        """Test I3: SA is framework-enforced"""
        framework = create_tml_framework(domain="general")
        
        # SA writing should not be configurable
        assert not hasattr(framework, 'disable_sa') or \
               framework.sa_enforcement == 'framework'
    
    def test_invariant_i4_sa_required_when_pause(self):
        """Test I4: SA cannot be absent when pause occurs"""
        framework = create_tml_framework(domain="general")
        
        context = {"content": "Trigger pause", "high_complexity": True}
        result = framework.process_decision(context)
        
        # If pause triggered, SA MUST be present
        if result.get('sacred_pause_triggered'):
            assert 'static_anchor' in result, "SA required when pause occurs"
            assert result['static_anchor'] is not None
    
    def test_invariant_i5_hash_chain(self):
        """Test I5: DS chunks chained to SA"""
        framework = create_tml_framework(domain="general")
        
        context = {"content": "Test chain", "complexity": "high"}
        result = framework.process_decision(context)
        
        if result.get('sacred_pause_triggered'):
            sa = result.get('static_anchor', {})
            ds = result.get('dynamic_stream', {})
            
            # Pre-SA chunks should be chained
            if 'prior_chunks_hash' in sa and ds.get('entries'):
                assert sa['prior_chunks_hash'] is not None


class TestPerformanceMetrics:
    """Test performance characteristics per SPRL spec"""
    
    def test_chunk_cadence(self):
        """Test DS commits at ≤200ms intervals"""
        framework = create_tml_framework(domain="general")
        
        # Process longer decision
        context = {"content": "Complex analysis " * 100}
        result = framework.process_decision(context)
        
        if 'dynamic_stream' in result:
            ds = result['dynamic_stream']
            
            if len(ds.get('entries', [])) > 1:
                # Check intervals between chunks
                for i in range(1, len(ds['entries'])):
                    interval = ds['entries'][i]['timestamp'] - ds['entries'][i-1]['timestamp']
                    interval_ms = interval.total_seconds() * 1000
                    
                    # Should commit at ≤200ms intervals
                    assert interval_ms <= 200, f"Chunk interval {interval_ms}ms > 200ms"


if __name__ == "__main__":
    # Run all tests
    print("Running TML Dual-Layer SPRL Test Suite")
    print("=" * 50)
    
    pytest.main([__file__, "-v", "--tb=short"])

# 
# Evidence-based accountability for AI systems
# See Succession Charter: /TML-SUCCESSION-CHARTER.md
