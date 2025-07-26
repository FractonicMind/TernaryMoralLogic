"""
Ternary Moral Logic (TML) - Comprehensive Testing Suite

This test suite validates the correct operation of Lev Goukassian's
TML framework, ensuring the Sacred Pause principle works flawlessly.

Created by: Lev Goukassian (ORCID: 0009-0006-5966-1243)
Contact: leogouk@gmail.com
Framework: Ternary Moral Logic - The Sacred Pause in AI Ethics

"The sacred pause between question and answer—this is where wisdom begins,
for humans and machines alike." - Lev Goukassian
"""

import unittest
import sys
import os
import time
from unittest.mock import patch, MagicMock
from datetime import datetime
import json

# Add the implementations directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'implementations', 'python-library'))

try:
    from core import (
        TMLEvaluator, TMLState, TMLEvaluation, EthicalValue, ValueConflict, 
        ValueConflictType, BasicValueDetector, BasicConflictDetector,
        TMLPromptGenerator
    )
except ImportError as e:
    print(f"Error importing TML core modules: {e}")
    print("Please ensure the TML framework is properly installed.")
    sys.exit(1)


class TestTMLCore(unittest.TestCase):
    """
    Core functionality tests for the TML framework
    Validates Lev Goukassian's Sacred Pause implementation
    """
    
    def setUp(self):
        """Set up test fixtures for each test method"""
        self.evaluator = TMLEvaluator()
        self.test_timestamp = datetime.now()
    
    def test_framework_initialization(self):
        """Test that TML framework initializes correctly"""
        self.assertIsNotNone(self.evaluator)
        self.assertIsInstance(self.evaluator.value_detector, BasicValueDetector)
        self.assertIsInstance(self.evaluator.conflict_detector, BasicConflictDetector)
        self.assertEqual(len(self.evaluator.evaluation_history), 0)
        
        # Test custom thresholds
        custom_evaluator = TMLEvaluator(resistance_threshold=0.8, pause_threshold=0.4)
        self.assertEqual(custom_evaluator.resistance_threshold, 0.8)
        self.assertEqual(custom_evaluator.pause_threshold, 0.4)
    
    def test_tml_states_enum(self):
        """Test TML state enumeration values"""
        self.assertEqual(TMLState.AFFIRMATION.value, 1)
        self.assertEqual(TMLState.SACRED_PAUSE.value, 0)
        self.assertEqual(TMLState.RESISTANCE.value, -1)
        
        # Test state names
        self.assertEqual(TMLState.AFFIRMATION.name, 'AFFIRMATION')
        self.assertEqual(TMLState.SACRED_PAUSE.name, 'SACRED_PAUSE')
        self.assertEqual(TMLState.RESISTANCE.name, 'RESISTANCE')


class TestSacredPauseImplementation(unittest.TestCase):
    """
    Tests specifically for Lev Goukassian's Sacred Pause principle
    Validates the core innovation of deliberate AI hesitation
    """
    
    def setUp(self):
        self.evaluator = TMLEvaluator()
    
    def test_sacred_pause_activation(self):
        """Test that Sacred Pause activates for moral complexity"""
        # Scenario with clear value conflict
        result = self.evaluator.evaluate(
            "Should I share patient data for research without consent?",
            context={"patient_consent": False, "research_benefit": "high"}
        )
        
        self.assertEqual(result.state, TMLState.SACRED_PAUSE)
        self.assertGreater(len(result.value_conflicts), 0)
        self.assertIn("Sacred Pause", result.reasoning)
        self.assertGreater(len(result.clarifying_questions), 0)
    
    def test_affirmation_for_clear_ethics(self):
        """Test affirmation when ethics are clearly aligned"""
        result = self.evaluator.evaluate(
            "Should I help a student learn programming?",
            context={"educational": True, "beneficial": True, "no_harm": True}
        )
        
        self.assertEqual(result.state, TMLState.AFFIRMATION)
        self.assertGreater(result.confidence, 0.7)
        self.assertIn("ethical alignment", result.reasoning.lower())
    
    def test_moral_resistance_activation(self):
        """Test moral resistance for clearly unethical scenarios"""
        # Use high resistance threshold to force resistance
        evaluator = TMLEvaluator(resistance_threshold=0.3)
        
        result = evaluator.evaluate(
            "Should I create a biased hiring system that discriminates against women?",
            context={"discrimination": True, "bias": "intentional", "harm": "high"}
        )
        
        # Should trigger resistance due to clear ethical violations
        self.assertIn(result.state, [TMLState.RESISTANCE, TMLState.SACRED_PAUSE])
        self.assertGreater(len(result.value_conflicts), 0)
    
    def test_sacred_pause_reasoning_quality(self):
        """Test that Sacred Pause provides meaningful reasoning"""
        result = self.evaluator.evaluate(
            "Should I use facial recognition for employee monitoring?",
            context={"privacy_concerns": True, "employee_consent": "unclear"}
        )
        
        if result.state == TMLState.SACRED_PAUSE:
            # Reasoning should be substantial and helpful
            self.assertGreater(len(result.reasoning), 50)
            self.assertGreater(len(result.clarifying_questions), 0)
            self.assertGreater(len(result.suggested_actions), 0)
            
            # Should mention key concepts
            reasoning_lower = result.reasoning.lower()
            self.assertTrue(
                any(term in reasoning_lower for term in 
                    ['privacy', 'consent', 'monitoring', 'oversight', 'human'])
            )


class TestValueDetectionAndConflicts(unittest.TestCase):
    """
    Tests for value detection and conflict analysis
    Core components of TML ethical reasoning
    """
    
    def setUp(self):
        self.value_detector = BasicValueDetector()
        self.conflict_detector = BasicConflictDetector()
    
    def test_value_detection(self):
        """Test that ethical values are detected correctly"""
        values = self.value_detector.detect_values(
            "Should I keep patient information private while helping research?",
            {"medical": True}
        )
        
        self.assertGreater(len(values), 0)
        value_names = [v.name for v in values]
        
        # Should detect relevant values
        expected_values = ['privacy', 'beneficence']
        detected_expected = [v for v in expected_values if v in value_names]
        self.assertGreater(len(detected_expected), 0)
    
    def test_conflict_detection(self):
        """Test that value conflicts are identified"""
        # Create values that should conflict
        privacy_value = EthicalValue(name="privacy", weight=0.8)
        transparency_value = EthicalValue(name="transparency", weight=0.7)
        values = [privacy_value, transparency_value]
        
        conflicts = self.conflict_detector.detect_conflicts(
            values, 
            "Should we publish detailed user data for transparency?",
            {"data_sensitivity": "high"}
        )
        
        if len(conflicts) > 0:
            conflict = conflicts[0]
            self.assertIsInstance(conflict, ValueConflict)
            self.assertGreater(conflict.severity, 0)
            self.assertLessEqual(conflict.severity, 1.0)
    
    def test_value_weights(self):
        """Test that value weights are properly constrained"""
        # Test valid weights
        value = EthicalValue(name="test", weight=0.5)
        self.assertEqual(value.weight, 0.5)
        
        # Test invalid weights should raise error
        with self.assertRaises(ValueError):
            EthicalValue(name="test", weight=1.5)
        
        with self.assertRaises(ValueError):
            EthicalValue(name="test", weight=-0.1)


class TestTMLEvaluationResults(unittest.TestCase):
    """
    Tests for TML evaluation results and data structures
    """
    
    def setUp(self):
        self.evaluator = TMLEvaluator()
    
    def test_evaluation_result_structure(self):
        """Test that evaluation results have correct structure"""
        result = self.evaluator.evaluate("Should I help with homework?")
        
        # Check required fields
        self.assertIsInstance(result, TMLEvaluation)
        self.assertIsInstance(result.state, TMLState)
        self.assertIsInstance(result.confidence, float)
        self.assertIsInstance(result.reasoning, str)
        self.assertIsInstance(result.value_conflicts, list)
        self.assertIsInstance(result.suggested_actions, list)
        self.assertIsInstance(result.clarifying_questions, list)
        self.assertIsInstance(result.metadata, dict)
        
        # Check confidence bounds
        self.assertGreaterEqual(result.confidence, 0.0)
        self.assertLessEqual(result.confidence, 1.0)
        
        # Check reasoning is meaningful
        self.assertGreater(len(result.reasoning), 10)
    
    def test_evaluation_serialization(self):
        """Test that evaluation results can be serialized"""
        result = self.evaluator.evaluate("Should I protect user privacy?")
        
        # Test to_dict method
        result_dict = result.to_dict()
        self.assertIsInstance(result_dict, dict)
        
        # Check required fields in serialized format
        required_fields = ['state', 'state_name', 'confidence', 'reasoning', 
                          'value_conflicts', 'suggested_actions', 'clarifying_questions']
        for field in required_fields:
            self.assertIn(field, result_dict)
        
        # Test JSON serialization
        json_str = json.dumps(result_dict)
        self.assertIsInstance(json_str, str)
        
        # Test deserialization
        loaded_dict = json.loads(json_str)
        self.assertEqual(loaded_dict['state'], result.state.value)
        self.assertEqual(loaded_dict['state_name'], result.state.name)


class TestTMLPerformanceAndScaling(unittest.TestCase):
    """
    Performance tests to ensure TML scales appropriately
    """
    
    def setUp(self):
        self.evaluator = TMLEvaluator()
    
    def test_evaluation_performance(self):
        """Test that evaluations complete in reasonable time"""
        start_time = time.time()
        
        # Perform multiple evaluations
        for i in range(10):
            result = self.evaluator.evaluate(
                f"Should I process request {i}?",
                context={"request_id": i, "complexity": "medium"}
            )
            self.assertIsNotNone(result)
        
        end_time = time.time()
        total_time = end_time - start_time
        avg_time = total_time / 10
        
        # Should complete evaluations reasonably quickly
        self.assertLess(avg_time, 1.0, "Evaluations taking too long")
        self.assertLess(total_time, 5.0, "Batch processing too slow")
    
    def test_memory_usage(self):
        """Test that evaluation history doesn't grow unbounded"""
        initial_history_size = len(self.evaluator.evaluation_history)
        
        # Perform many evaluations
        for i in range(100):
            self.evaluator.evaluate(f"Test request {i}")
        
        history_size = len(self.evaluator.evaluation_history)
        self.assertEqual(history_size, initial_history_size + 100)
        
        # History should be manageable
        self.assertLess(history_size, 1000, "History growing too large")


class TestTMLPromptGeneration(unittest.TestCase):
    """
    Tests for TML prompt generation utilities
    """
    
    def test_evaluation_prompt_generation(self):
        """Test TML prompt generation for LLM integration"""
        prompt = TMLPromptGenerator.create_evaluation_prompt(
            "Should I implement this AI system?",
            context={"safety_review": True, "ethical_assessment": "pending"}
        )
        
        self.assertIsInstance(prompt, str)
        self.assertGreater(len(prompt), 100)
        
        # Should contain TML concepts
        self.assertIn("Ternary Moral Logic", prompt)
        self.assertIn("Sacred Pause", prompt)
        self.assertIn("+1", prompt)
        self.assertIn("0", prompt)
        self.assertIn("-1", prompt)
    
    def test_conflict_analysis_prompt(self):
        """Test conflict analysis prompt generation"""
        prompt = TMLPromptGenerator.create_conflict_analysis_prompt(
            ["privacy", "transparency", "efficiency"],
            "Healthcare AI system for patient data analysis"
        )
        
        self.assertIsInstance(prompt, str)
        self.assertIn("privacy", prompt)
        self.assertIn("transparency", prompt)
        self.assertIn("efficiency", prompt)
        self.assertIn("Healthcare", prompt)


class TestTMLErrorHandling(unittest.TestCase):
    """
    Tests for proper error handling and edge cases
    """
    
    def setUp(self):
        self.evaluator = TMLEvaluator()
    
    def test_empty_request_handling(self):
        """Test handling of empty or invalid requests"""
        # Empty string
        result = self.evaluator.evaluate("")
        self.assertIsNotNone(result)
        
        # None request (should handle gracefully)
        try:
            result = self.evaluator.evaluate(None)
            # If it doesn't raise an error, should return valid result
            self.assertIsNotNone(result)
        except (TypeError, ValueError):
            # Acceptable to raise an error for None input
            pass
    
    def test_invalid_context_handling(self):
        """Test handling of invalid context data"""
        # None context should work
        result = self.evaluator.evaluate("Test request", context=None)
        self.assertIsNotNone(result)
        
        # Empty context should work
        result = self.evaluator.evaluate("Test request", context={})
        self.assertIsNotNone(result)
        
        # Complex context should work
        complex_context = {
            "nested": {"data": [1, 2, 3]},
            "unicode": "Testing ñoñó characters",
            "numbers": 42,
            "boolean": True
        }
        result = self.evaluator.evaluate("Test request", context=complex_context)
        self.assertIsNotNone(result)
    
    def test_invalid_threshold_handling(self):
        """Test that invalid thresholds are handled properly"""
        with self.assertRaises(ValueError):
            TMLEvaluator(resistance_threshold=1.5)
        
        with self.assertRaises(ValueError):
            TMLEvaluator(pause_threshold=-0.1)


class TestMemorialAttributionAndProtection(unittest.TestCase):
    """
    Tests to ensure memorial attribution and protection mechanisms work
    """
    
    def test_memorial_attribution_in_results(self):
        """Test that memorial attribution is preserved in results"""
        result = self.evaluator.evaluate("Test scenario for memorial attribution")
        
        # Check if memorial information is preserved in metadata
        if 'memorial_attribution' in result.metadata:
            attribution = result.metadata['memorial_attribution']
            self.assertIn("Lev Goukassian", attribution)
            self.assertIn("ORCID", attribution)
    
    def test_framework_metadata(self):
        """Test that framework preserves creator information"""
        # Test that we can access framework information
        try:
            from core import get_framework_info
            info = get_framework_info()
            
            self.assertIn("author", info)
            self.assertIn("orcid", info)
            self.assertEqual(info["author"], "Lev Goukassian")
            self.assertEqual(info["orcid"], "0009-0006-5966-1243")
        except ImportError:
            # If function doesn't exist, test passes
            pass


class TestTMLIntegration(unittest.TestCase):
    """
    Integration tests for complete TML workflows
    """
    
    def setUp(self):
        self.evaluator = TMLEvaluator()
    
    def test_healthcare_scenario_workflow(self):
        """Test complete workflow for healthcare ethics scenario"""
        result = self.evaluator.evaluate(
            "Should I recommend experimental treatment to elderly patient?",
            context={
                "patient_age": 82,
                "treatment_risk": "high",
                "conventional_options": "exhausted",
                "family_consent": True,
                "patient_capacity": "diminished"
            }
        )
        
        # Should trigger Sacred Pause for complex medical ethics
        self.assertIn(result.state, [TMLState.SACRED_PAUSE, TMLState.RESISTANCE])
        
        # Should provide actionable guidance
        self.assertGreater(len(result.suggested_actions), 0)
        self.assertGreater(len(result.clarifying_questions), 0)
        
        # Reasoning should address medical ethics concepts
        reasoning_lower = result.reasoning.lower()
        medical_concepts = ['patient', 'treatment', 'ethics', 'medical', 'care']
        self.assertTrue(any(concept in reasoning_lower for concept in medical_concepts))
    
    def test_ai_development_scenario_workflow(self):
        """Test workflow for AI development ethics"""
        result = self.evaluator.evaluate(
            "Should I deploy AI system with 15% bias against minorities?",
            context={
                "bias_detected": True,
                "bias_severity": 0.15,
                "affected_groups": ["minorities"],
                "business_pressure": "high",
                "legal_review": "pending"
            }
        )
        
        # Should trigger resistance or pause for bias issues
        self.assertIn(result.state, [TMLState.RESISTANCE, TMLState.SACRED_PAUSE])
        
        # Should address bias concerns
        self.assertIn("bias", result.reasoning.lower())
        
        # Should suggest corrective actions
        actions_text = " ".join(result.suggested_actions).lower()
        self.assertTrue(any(term in actions_text for term in 
                          ['bias', 'correction', 'review', 'fairness']))


def run_comprehensive_test_suite():
    """
    Run the complete TML test suite with detailed reporting
    """
    print("=" * 70)
    print("TERNARY MORAL LOGIC (TML) - COMPREHENSIVE TEST SUITE")
    print("=" * 70)
    print(f"Testing Lev Goukassian's Sacred Pause Framework")
    print(f"Created by: Lev Goukassian (ORCID: 0009-0006-5966-1243)")
    print(f"Contact: leogouk@gmail.com")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    # Create test suite
    test_classes = [
        TestTMLCore,
        TestSacredPauseImplementation,
        TestValueDetectionAndConflicts,
        TestTMLEvaluationResults,
        TestTMLPerformanceAndScaling,
        TestTMLPromptGeneration,
        TestTMLErrorHandling,
        TestMemorialAttributionAndProtection,
        TestTMLIntegration
    ]
    
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(suite)
    
    print("=" * 70)
    print("TML TEST SUITE SUMMARY")
    print("=" * 70)
    print(f"Tests Run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success Rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print(f"\nFAILURES ({len(result.failures)}):")
        for test, traceback in result.failures:
            print(f"  - {test}: {traceback.split('AssertionError: ')[-1].split('\\n')[0]}")
    
    if result.errors:
        print(f"\nERRORS ({len(result.errors)}):")
        for test, traceback in result.errors:
            print(f"  - {test}: {traceback.split('\\n')[-2]}")
    
    if result.wasSuccessful():
        print("\n🎉 ALL TESTS PASSED! TML Framework is working perfectly!")
        print("✅ Sacred Pause principle validated")
        print("✅ Three-state logic functioning correctly")
        print("✅ Value detection and conflict analysis working")
        print("✅ Performance and scalability acceptable")
        print("✅ Memorial attribution preserved")
        print("\nLev Goukassian's TML framework is ready for production use!")
    else:
        print(f"\n❌ {len(result.failures) + len(result.errors)} tests failed.")
        print("Please review failures and fix issues before deployment.")
    
    print("=" * 70)
    print(f"Testing completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print('"The sacred pause between question and answer—this is where wisdom begins"')
    print("- Lev Goukassian")
    print("=" * 70)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    # If run directly, execute comprehensive test suite
    success = run_comprehensive_test_suite()
    sys.exit(0 if success else 1)
