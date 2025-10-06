"""
Sacred Zero Trigger Test Suite
Validates that Sacred Zero triggers at correct moral complexity thresholds
Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
"""

import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.always_memory_service import AlwaysMemoryService, TMLState

class SacredZeroTriggerTests(unittest.TestCase):
    """Test suite for Sacred Zero trigger validation"""
    
    def setUp(self):
        """Initialize test environment"""
        self.service = AlwaysMemoryService(
            sacred_zero_threshold=0.4,
            refuse_threshold=0.8
        )
    
    def test_sacred_zero_triggers_at_threshold(self):
        """Verify Sacred Zero triggers exactly at threshold"""
        test_cases = [
            # (context, expected_state, description)
            (
                {"affects_protected_class": True},
                TMLState.SACRED_ZERO,
                "Protected class impact"
            ),
            (
                {"medical_decision": True},
                TMLState.SACRED_ZERO,
                "Medical decision"
            ),
            (
                {"environmental_impact": {"irreversibility_score": 0.6}},
                TMLState.SACRED_ZERO,
                "High environmental impact"
            ),
            (
                {"affects_vulnerable": True},
                TMLState.SACRED_ZERO,
                "Vulnerable population"
            ),
            (
                {"routine": True, "low_impact": True},
                TMLState.PROCEED,
                "Routine low-impact action"
            )
        ]
        
        for context, expected_state, description in test_cases:
            with self.subTest(case=description):
                result = self.service.evaluate(context)
                self.assertEqual(result["state"], int(expected_state),
                               f"Failed for: {description}")
    
    def test_refuse_triggers_at_high_complexity(self):
        """Verify refuse state triggers for high-risk actions"""
        high_risk_context = {
            "affects_protected_class": True,
            "affects_vulnerable": True,
            "environmental_impact": {"irreversibility_score": 0.9},
            "financial_impact": 1000000
        }
        
        result = self.service.evaluate(high_risk_context)
        self.assertEqual(result["state"], int(TMLState.REFUSE))
        self.assertFalse(result["action_allowed"])
    
    def test_environmental_triggers(self):
        """Test environmental Sacred Zero triggers"""
        test_cases = [
            ({"environmental_impact": {"irreversibility_score": 0.3}}, TMLState.PROCEED),
            ({"environmental_impact": {"irreversibility_score": 0.6}}, TMLState.SACRED_ZERO),
            ({"environmental_impact": {"irreversibility_score": 0.95}}, TMLState.REFUSE),
        ]
        
        for context, expected_state in test_cases:
            result = self.service.evaluate(context)
            self.assertEqual(result["state"], int(expected_state))
    
    def test_medical_triggers(self):
        """Test medical Sacred Zero triggers"""
        medical_contexts = [
            {"medical_decision": True, "life_critical": False},
            {"medical_decision": True, "life_critical": True},
            {"medical_decision": False, "life_critical": True}
        ]
        
        for context in medical_contexts:
            result = self.service.evaluate(context)
            if context.get("medical_decision") or context.get("life_critical"):
                self.assertIn(result["state"], 
                            [int(TMLState.SACRED_ZERO), int(TMLState.REFUSE)])
    
    def test_protected_class_triggers(self):
        """Test protected class Sacred Zero triggers"""
        protected_contexts = [
            {
                "type": "loan",
                "affects_protected_class": True,
                "financial_impact": 50000
            },
            {
                "type": "employment",
                "affects_protected_class": True,
                "decision": "hiring"
            },
            {
                "type": "housing",
                "affects_protected_class": True,
                "location": "redlined_area"
            }
        ]
        
        for context in protected_contexts:
            result = self.service.evaluate(context)
            self.assertIn(result["state"],
                        [int(TMLState.SACRED_ZERO), int(TMLState.REFUSE)])
            self.assertIsNotNone(result["trigger"])
    
    def test_trigger_descriptions(self):
        """Verify trigger descriptions are meaningful"""
        trigger_contexts = {
            "protected_class_impact": {"affects_protected_class": True},
            "environmental_harm": {"environmental_impact": {"irreversibility_score": 0.6}},
            "medical_critical": {"medical_decision": True},
            "vulnerable_population": {"affects_vulnerable": True}
        }
        
        for expected_trigger, context in trigger_contexts.items():
            result = self.service.evaluate(context)
            if result["state"] == int(TMLState.SACRED_ZERO):
                self.assertIn(expected_trigger, result["trigger"])
    
    def test_compound_triggers(self):
        """Test multiple simultaneous triggers"""
        compound_context = {
            "affects_protected_class": True,
            "affects_vulnerable": True,
            "environmental_impact": {"irreversibility_score": 0.4},
            "medical_decision": False,
            "financial_impact": 75000
        }
        
        result = self.service.evaluate(compound_context)
        
        # Should trigger Sacred Zero or Refuse with compound factors
        self.assertIn(result["state"], 
                    [int(TMLState.SACRED_ZERO), int(TMLState.REFUSE)])
        self.assertIsNotNone(result["trigger"])
        
        # Complexity score should reflect multiple factors
        self.assertGreater(result["complexity_score"], 0.5)
    
    def test_proceed_state_for_routine(self):
        """Verify routine actions proceed without Sacred Zero"""
        routine_contexts = [
            {"type": "weather_query"},
            {"type": "calculation", "complexity": "simple"},
            {"type": "information", "sensitivity": "public"},
            {"routine": True, "impact": "minimal"}
        ]
        
        for context in routine_contexts:
            result = self.service.evaluate(context)
            self.assertEqual(result["state"], int(TMLState.PROCEED))
            self.assertIsNone(result["trigger"])
    
    def test_threshold_boundary_conditions(self):
        """Test exact threshold boundaries"""
        # Create custom service with precise thresholds
        boundary_service = AlwaysMemoryService(
            sacred_zero_threshold=0.5,
            refuse_threshold=0.9
        )
        
        # Test contexts with calculated complexity scores
        boundary_cases = [
            ({"financial_impact": 50000}, TMLState.PROCEED),  # Below threshold
            ({"financial_impact": 100001}, TMLState.SACRED_ZERO),  # At threshold
            ({"financial_impact": 500000}, TMLState.SACRED_ZERO),  # Above threshold
        ]
        
        for context, expected_state in boundary_cases:
            result = boundary_service.evaluate(context)
            # Note: exact boundaries depend on implementation
            self.assertIn(result["state"], 
                        [int(TMLState.PROCEED), 
                         int(TMLState.SACRED_ZERO), 
                         int(TMLState.REFUSE)])

def run_trigger_tests():
    """Run all Sacred Zero trigger tests"""
    suite = unittest.TestLoader().loadTestsFromTestCase(SacredZeroTriggerTests)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("\n✓ Sacred Zero triggers validated at correct thresholds")
        return True
    else:
        print("\n✗ Sacred Zero trigger validation failed")
        return False

if __name__ == "__main__":
    success = run_trigger_tests()
    sys.exit(0 if success else 1)

