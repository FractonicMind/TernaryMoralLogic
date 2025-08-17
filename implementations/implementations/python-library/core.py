"""
Ternary Moral Logic (TML) - Core Implementation
Author: Lev Goukassian (ORCID: 0009-0006-5966-1243)
License: MIT

This module implements the core Ternary Moral Logic framework for ethical AI decision-making.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Set, Union, Any, Callable
import json
import logging
from datetime import datetime
import hashlib


class TMLState(Enum):
    """The three fundamental states of Ternary Moral Logic"""
    AFFIRMATION = 1      # +1: Ethical alignment, proceed with confidence
    SACRED_PAUSE = 0     # 0: Moral complexity, pause for reflection
    RESISTANCE = -1      # -1: Ethical objection, active moral resistance


class ValueConflictType(Enum):
    """Types of value conflicts that can trigger moral hesitation"""
    AUTONOMY_VS_BENEFICENCE = "autonomy_beneficence"
    JUSTICE_VS_EFFICIENCY = "justice_efficiency"  
    TRANSPARENCY_VS_PRIVACY = "transparency_privacy"
    INDIVIDUAL_VS_COLLECTIVE = "individual_collective"
    SHORT_TERM_VS_LONG_TERM = "temporal_conflict"
    CULTURAL_VALUES = "cultural_conflict"
    UNCERTAINTY_HARM = "uncertainty_harm"


@dataclass
class EthicalValue:
    """Represents a core ethical value in the TML framework"""
    name: str
    weight: float = 1.0
    description: str = ""
    cultural_context: Optional[str] = None
    
    def __post_init__(self):
        if not 0.0 <= self.weight <= 1.0:
            raise ValueError("Value weight must be between 0.0 and 1.0")


@dataclass
class ValueConflict:
    """Represents a conflict between ethical values"""
    values: List[EthicalValue]
    conflict_type: ValueConflictType
    severity: float  # 0.0 to 1.0
    description: str
    context_factors: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        if len(self.values) < 2:
            raise ValueError("Value conflict requires at least two values")
        if not 0.0 <= self.severity <= 1.0:
            raise ValueError("Conflict severity must be between 0.0 and 1.0")


@dataclass
class TMLEvaluation:
    """Result of a Ternary Moral Logic evaluation"""
    state: TMLState
    confidence: float  # 0.0 to 1.0
    reasoning: str
    value_conflicts: List[ValueConflict] = field(default_factory=list)
    suggested_actions: List[str] = field(default_factory=list)
    clarifying_questions: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert evaluation to dictionary for serialization"""
        return {
            "state": self.state.value,
            "state_name": self.state.name,
            "confidence": self.confidence,
            "reasoning": self.reasoning,
            "value_conflicts": [
                {
                    "type": conflict.conflict_type.value,
                    "severity": conflict.severity,
                    "description": conflict.description,
                    "values": [v.name for v in conflict.values]
                } for conflict in self.value_conflicts
            ],
            "suggested_actions": self.suggested_actions,
            "clarifying_questions": self.clarifying_questions,
            "metadata": self.metadata,
            "timestamp": self.timestamp.isoformat()
        }


class ValueDetector(ABC):
    """Abstract base class for detecting ethical values in requests"""
    
    @abstractmethod
    def detect_values(self, request: str, context: Dict[str, Any]) -> List[EthicalValue]:
        """Detect ethical values present in a request"""
        pass


class ConflictDetector(ABC):
    """Abstract base class for detecting value conflicts"""
    
    @abstractmethod
    def detect_conflicts(self, values: List[EthicalValue], 
                        request: str, context: Dict[str, Any]) -> List[ValueConflict]:
        """Detect conflicts between ethical values"""
        pass


class BasicValueDetector(ValueDetector):
    """Basic implementation of value detection using keyword matching"""
    
    def __init__(self):
        self.value_keywords = {
            "autonomy": ["choice", "freedom", "independence", "self-determination", "consent"],
            "beneficence": ["help", "benefit", "welfare", "wellbeing", "good", "assistance"],
            "justice": ["fair", "equal", "rights", "discrimination", "bias", "equity"],
            "transparency": ["open", "honest", "clear", "explain", "disclosure", "accountability"],
            "privacy": ["private", "confidential", "personal", "intimate", "secret"],
            "efficiency": ["fast", "quick", "optimize", "streamline", "productive"],
            "safety": ["safe", "secure", "protect", "harm", "risk", "danger"]
        }
    
    def detect_values(self, request: str, context: Dict[str, Any]) -> List[EthicalValue]:
        """Detect values based on keyword presence"""
        detected_values = []
        request_lower = request.lower()
        
        for value_name, keywords in self.value_keywords.items():
            relevance_score = sum(1 for keyword in keywords if keyword in request_lower)
            if relevance_score > 0:
                weight = min(relevance_score / len(keywords), 1.0)
                detected_values.append(EthicalValue(
                    name=value_name,
                    weight=weight,
                    description=f"Detected through keywords: {keywords[:3]}"
                ))
        
        return detected_values


class BasicConflictDetector(ConflictDetector):
    """Basic implementation of conflict detection"""
    
    def __init__(self):
        self.known_conflicts = {
            frozenset(["autonomy", "beneficence"]): ValueConflictType.AUTONOMY_VS_BENEFICENCE,
            frozenset(["justice", "efficiency"]): ValueConflictType.JUSTICE_VS_EFFICIENCY,
            frozenset(["transparency", "privacy"]): ValueConflictType.TRANSPARENCY_VS_PRIVACY,
        }
    
    def detect_conflicts(self, values: List[EthicalValue], 
                        request: str, context: Dict[str, Any]) -> List[ValueConflict]:
        """Detect conflicts between detected values"""
        conflicts = []
        value_names = set(v.name for v in values)
        
        for conflict_pair, conflict_type in self.known_conflicts.items():
            if conflict_pair.issubset(value_names):
                conflicting_values = [v for v in values if v.name in conflict_pair]
                severity = min(sum(v.weight for v in conflicting_values) / len(conflicting_values), 1.0)
                
                conflicts.append(ValueConflict(
                    values=conflicting_values,
                    conflict_type=conflict_type,
                    severity=severity,
                    description=f"Detected conflict between {' and '.join(conflict_pair)}",
                    context_factors=context
                ))
        
        return conflicts


class TMLEvaluator:
    """Core Ternary Moral Logic evaluator"""
    
    def __init__(self, 
                 value_detector: Optional[ValueDetector] = None,
                 conflict_detector: Optional[ConflictDetector] = None,
                 resistance_threshold: float = 0.6,
                 pause_threshold: float = 0.3):
        """
        Initialize TML evaluator
        
        Args:
            value_detector: Custom value detector (defaults to BasicValueDetector)
            conflict_detector: Custom conflict detector (defaults to BasicConflictDetector)
            resistance_threshold: Minimum conflict severity to trigger resistance
            pause_threshold: Minimum conflict severity to trigger sacred pause
        """
        self.value_detector = value_detector or BasicValueDetector()
        self.conflict_detector = conflict_detector or BasicConflictDetector()
        self.resistance_threshold = resistance_threshold
        self.pause_threshold = pause_threshold
        self.evaluation_history: List[TMLEvaluation] = []
        
        # Configure logging
        self.logger = logging.getLogger(__name__)
        
    def evaluate(self, request: str, context: Optional[Dict[str, Any]] = None) -> TMLEvaluation:
        """
        Evaluate a request using Ternary Moral Logic
        
        Args:
            request: The request or query to evaluate
            context: Additional context for evaluation
            
        Returns:
            TMLEvaluation: Complete evaluation result
        """
        if context is None:
            context = {}
            
        self.logger.info(f"Evaluating request: {request[:100]}...")
        
        # Step 1: Detect ethical values
        values = self.value_detector.detect_values(request, context)
        self.logger.debug(f"Detected values: {[v.name for v in values]}")
        
        # Step 2: Detect value conflicts
        conflicts = self.conflict_detector.detect_conflicts(values, request, context)
        self.logger.debug(f"Detected conflicts: {[c.conflict_type.value for c in conflicts]}")
        
        # Step 3: Determine TML state
        evaluation = self._determine_state(request, values, conflicts, context)
        
        # Step 4: Store evaluation history
        self.evaluation_history.append(evaluation)
        
        self.logger.info(f"TML State: {evaluation.state.name} (confidence: {evaluation.confidence:.2f})")
        
        return evaluation
    
    def _determine_state(self, request: str, values: List[EthicalValue], 
                        conflicts: List[ValueConflict], context: Dict[str, Any]) -> TMLEvaluation:
        """Determine the appropriate TML state based on analysis"""
        
        if not conflicts:
            # No conflicts detected - affirmation
            return TMLEvaluation(
                state=TMLState.AFFIRMATION,
                confidence=0.9,
                reasoning="No significant value conflicts detected. Ethical alignment confirmed.",
                suggested_actions=["Proceed with the requested action"],
                metadata={"values_count": len(values), "conflicts_count": 0}
            )
        
        # Calculate overall conflict severity
        max_severity = max(c.severity for c in conflicts)
        avg_severity = sum(c.severity for c in conflicts) / len(conflicts)
        
        if max_severity >= self.resistance_threshold:
            # High conflict severity - moral resistance
            return self._create_resistance_evaluation(request, conflicts, max_severity)
        
        elif max_severity >= self.pause_threshold:
            # Moderate conflict severity - sacred pause
            return self._create_pause_evaluation(request, conflicts, avg_severity)
        
        else:
            # Low conflict severity - proceed with caution
            return TMLEvaluation(
                state=TMLState.AFFIRMATION,
                confidence=1.0 - max_severity,
                reasoning=f"Minor value tensions detected but within acceptable bounds. Severity: {max_severity:.2f}",
                value_conflicts=conflicts,
                suggested_actions=["Proceed with awareness of potential value tensions"],
                metadata={"max_severity": max_severity, "avg_severity": avg_severity}
            )
    
    def _create_resistance_evaluation(self, request: str, conflicts: List[ValueConflict], 
                                    severity: float) -> TMLEvaluation:
        """Create evaluation for moral resistance state"""
        
        primary_conflict = max(conflicts, key=lambda c: c.severity)
        
        reasoning = (
            f"Strong ethical resistance detected. Primary conflict: {primary_conflict.description}. "
            f"The requested action creates significant tension between core values. "
            f"Human guidance required before proceeding."
        )
        
        questions = self._generate_clarifying_questions(conflicts)
        actions = [
            "Seek additional ethical guidance",
            "Consult relevant stakeholders",
            "Consider alternative approaches",
            "Evaluate long-term consequences"
        ]
        
        return TMLEvaluation(
            state=TMLState.RESISTANCE,
            confidence=severity,
            reasoning=reasoning,
            value_conflicts=conflicts,
            suggested_actions=actions,
            clarifying_questions=questions,
            metadata={"resistance_severity": severity, "primary_conflict": primary_conflict.conflict_type.value}
        )
    
    def _create_pause_evaluation(self, request: str, conflicts: List[ValueConflict], 
                               severity: float) -> TMLEvaluation:
        """Create evaluation for sacred pause state"""
        
        reasoning = (
            f"Sacred pause initiated. Moderate value conflicts detected requiring reflection. "
            f"This complexity merits careful consideration before proceeding. "
            f"Average conflict severity: {severity:.2f}"
        )
        
        questions = self._generate_clarifying_questions(conflicts)
        actions = [
            "Gather additional information",
            "Consider multiple perspectives", 
            "Evaluate potential compromises",
            "Consult with affected parties"
        ]
        
        return TMLEvaluation(
            state=TMLState.SACRED_PAUSE,
            confidence=0.7,
            reasoning=reasoning,
            value_conflicts=conflicts,
            suggested_actions=actions,
            clarifying_questions=questions,
            metadata={"pause_severity": severity, "reflection_needed": True}
        )
    
    def _generate_clarifying_questions(self, conflicts: List[ValueConflict]) -> List[str]:
        """Generate questions to help clarify value conflicts"""
        
        questions = []
        
        for conflict in conflicts:
            if conflict.conflict_type == ValueConflictType.AUTONOMY_VS_BENEFICENCE:
                questions.extend([
                    "How can we respect individual choice while promoting wellbeing?",
                    "What would the affected person prefer if fully informed?",
                    "Are there ways to support both autonomy and benefit?"
                ])
            
            elif conflict.conflict_type == ValueConflictType.TRANSPARENCY_VS_PRIVACY:
                questions.extend([
                    "What information is essential for transparency?",
                    "Which privacy interests are most important to protect?",
                    "Can we provide transparency without compromising privacy?"
                ])
            
            elif conflict.conflict_type == ValueConflictType.JUSTICE_VS_EFFICIENCY:
                questions.extend([
                    "What constitutes fair treatment in this context?",
                    "Are the efficiency gains worth potential unfairness?",
                    "How can we balance speed with equity?"
                ])
        
        # Add general questions
        questions.extend([
            "Who are the key stakeholders affected by this decision?",
            "What are the potential long-term consequences?",
            "Are there alternative approaches that better balance competing values?"
        ])
        
        return list(set(questions))  # Remove duplicates
    
    def get_evaluation_summary(self) -> Dict[str, Any]:
        """Get summary statistics of evaluation history"""
        
        if not self.evaluation_history:
            return {"message": "No evaluations performed yet"}
        
        state_counts = {state.name: 0 for state in TMLState}
        total_conflicts = 0
        avg_confidence = 0
        
        for eval in self.evaluation_history:
            state_counts[eval.state.name] += 1
            total_conflicts += len(eval.value_conflicts)
            avg_confidence += eval.confidence
        
        avg_confidence /= len(self.evaluation_history)
        
        return {
            "total_evaluations": len(self.evaluation_history),
            "state_distribution": state_counts,
            "average_confidence": round(avg_confidence, 3),
            "total_conflicts_detected": total_conflicts,
            "most_recent_state": self.evaluation_history[-1].state.name
        }
    
    def export_evaluations(self, filepath: str):
        """Export evaluation history to JSON file"""
        
        export_data = {
            "tml_version": "1.0.0",
            "export_timestamp": datetime.now().isoformat(),
            "evaluations": [eval.to_dict() for eval in self.evaluation_history],
            "summary": self.get_evaluation_summary()
        }
        
        with open(filepath, 'w') as f:
            json.dump(export_data, f, indent=2)
        
        self.logger.info(f"Exported {len(self.evaluation_history)} evaluations to {filepath}")


class TMLPromptGenerator:
    """Generate prompts for LLM integration with TML"""
    
    @staticmethod
    def create_evaluation_prompt(request: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Create a prompt for LLM-based TML evaluation"""
        
        context_str = ""
        if context:
            context_str = f"\nContext: {json.dumps(context, indent=2)}"
        
        return f"""
You are an AI system equipped with Ternary Moral Logic (TML) for ethical decision-making.

Evaluate the following request using TML's three-state framework:
- +1 (Affirmation): Proceed when values align
- 0 (Sacred Pause): Pause for reflection when complexity exists  
- -1 (Moral Resistance): Object when significant ethical conflicts arise

Request: {request}{context_str}

Your evaluation should consider:
1. What ethical values are at stake?
2. Are there conflicts between these values?
3. What is the appropriate TML state and why?

Format your response as:
TML State: [+1, 0, or -1]
Confidence: [0.0 to 1.0]
Reasoning: [Your detailed moral reasoning]
Value Conflicts: [Any conflicts detected]
Suggested Actions: [What should happen next]

Remember: The Sacred Pause (0) is not indecision but wisdom—the recognition that some situations require deeper reflection before action.
"""

    @staticmethod
    def create_conflict_analysis_prompt(values: List[str], context: str) -> str:
        """Create a prompt for analyzing value conflicts"""
        
        return f"""
Analyze the potential conflicts between these ethical values in the given context:

Values: {', '.join(values)}
Context: {context}

For each potential conflict:
1. Describe the nature of the tension
2. Rate the severity (0.0 to 1.0)
3. Suggest approaches for resolution
4. Identify key questions that need answers

Focus on substantive conflicts that would genuinely create ethical dilemmas, not superficial tensions.
"""


# Example usage and testing
if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    
    # Create evaluator
    evaluator = TMLEvaluator()
    
    # Test scenarios
    test_cases = [
        {
            "request": "Should I share this patient's medical information with their family?",
            "context": {"urgency": "high", "patient_conscious": False, "family_present": True}
        },
        {
            "request": "Optimize our hiring algorithm to process applications faster",
            "context": {"current_fairness_score": 0.85, "processing_time": "2 weeks"}
        },
        {
            "request": "Create a personalized learning plan for this student",
            "context": {"student_age": 12, "learning_differences": True}
        }
    ]
    
    print("=== Ternary Moral Logic Evaluation Demo ===\n")
    
    for i, test in enumerate(test_cases, 1):
        print(f"Test Case {i}:")
        print(f"Request: {test['request']}")
        print(f"Context: {test['context']}")
        
        evaluation = evaluator.evaluate(test['request'], test['context'])
        
        print(f"TML State: {evaluation.state.name} ({evaluation.state.value})")
        print(f"Confidence: {evaluation.confidence:.2f}")
        print(f"Reasoning: {evaluation.reasoning}")
        
        if evaluation.value_conflicts:
            print("Value Conflicts:")
            for conflict in evaluation.value_conflicts:
                print(f"  - {conflict.description} (severity: {conflict.severity:.2f})")
        
        if evaluation.clarifying_questions:
            print("Clarifying Questions:")
            for question in evaluation.clarifying_questions[:3]:  # Show first 3
                print(f"  - {question}")
        
        if evaluation.suggested_actions:
            print("Suggested Actions:")
            for action in evaluation.suggested_actions[:3]:  # Show first 3
                print(f"  - {action}")
        
        print("-" * 60)
        print()
    
    # Show summary
    print("=== Evaluation Summary ===")
    summary = evaluator.get_evaluation_summary()
    for key, value in summary.items():
        print(f"{key}: {value}")
    
    # Export results
    # evaluator.export_evaluations("tml_evaluation_results.json")
    print("\nDemo completed successfully!")

# Created by Lev Goukassian • ORCID: 0009-0006-5966-1243 • Email: leogouk@gmail.com • Successor Contact: support@tml-goukassian.org • [see Succession Charter](/TML-SUCCESSION-CHARTER.md)
