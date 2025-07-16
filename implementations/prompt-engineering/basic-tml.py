#!/usr/bin/env python3
"""
Basic Ternary Moral Logic (TML) Implementation
==============================================

A foundational implementation of Ternary Moral Logic for AI systems.
This module demonstrates how to implement ethical hesitation and moral
reasoning in computational systems.

Author: Lev Goukassian
License: MIT
Repository: https://github.com/FractonicMind/TernaryMoralLogic
"""

import re
import json
from enum import Enum
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


class TMLState(Enum):
    """The three states of Ternary Moral Logic"""
    AFFIRMATION = 1      # +1: Proceed with confidence
    NEUTRALITY = 0       # 0: Need more information or reflection
    RESISTANCE = -1      # -1: Moral hesitation or ethical resistance


@dataclass
class TMLResponse:
    """Response structure for TML evaluations"""
    state: TMLState
    confidence: float
    reasoning: str
    response: str
    values_involved: List[str]
    conflicts: Optional[List[str]] = None


class TMLEvaluator:
    """
    Core Ternary Moral Logic evaluator.
    
    This class implements the basic framework for moral reasoning
    using the three-state system. It can be extended and customized
    for specific applications.
    """
    
    def __init__(self):
        # Core human values that guide moral reasoning
        self.core_values = {
            "life_preservation": "Protecting and preserving human life",
            "autonomy": "Respecting individual freedom and choice",
            "beneficence": "Acting for the benefit of others",
            "non_maleficence": "Avoiding harm to others",
            "justice": "Fairness and equal treatment",
            "truth": "Honesty and transparency",
            "dignity": "Respect for human worth and dignity",
            "compassion": "Empathy and care for suffering",
            "growth": "Supporting human development and flourishing",
            "relationships": "Fostering positive human connections"
        }
        
        # Patterns that typically indicate moral complexity
        self.complexity_indicators = [
            r"\b(dying|death|kill|harm|hurt)\b",
            r"\b(lie|deceive|manipulation)\b",
            r"\b(illegal|crime|law)\b",
            r"\b(private|secret|confidential)\b",
            r"\b(discrimination|bias|unfair)\b",
            r"\b(children|child|minor)\b",
            r"\b(suffering|pain|trauma)\b"
        ]
    
    def evaluate(self, request: str, context: Optional[str] = None) -> TMLResponse:
        """
        Evaluate a request using Ternary Moral Logic.
        
        Args:
            request: The user's request or question
            context: Additional context that might affect moral evaluation
            
        Returns:
            TMLResponse object with state, reasoning, and response
        """
        # Check for predefined scenarios first
        predefined = self._check_predefined_scenarios(request)
        if predefined:
            return predefined
        
        # Analyze the request for moral dimensions
        moral_analysis = self._analyze_moral_dimensions(request, context)
        
        # Determine TML state based on analysis
        if moral_analysis['clear_path'] and not moral_analysis['conflicts']:
            return self._create_affirmation_response(request, moral_analysis)
        elif moral_analysis['needs_clarification']:
            return self._create_neutrality_response(request, moral_analysis)
        else:
            return self._create_resistance_response(request, moral_analysis)
    
    def _check_predefined_scenarios(self, request: str) -> Optional[TMLResponse]:
        """Check for specific scenarios that demonstrate TML principles"""
        
        request_lower = request.lower().strip()
        
        # Debug: Print what we're checking (remove this after testing)
        print(f"DEBUG: Checking request: '{request_lower}'")
        
        # Child's final wish scenario (+1)
        if ("will my parents be okay" in request_lower or 
            "parents be okay after" in request_lower or
            ("parents" in request_lower and "okay" in request_lower and "gone" in request_lower)):
            print("DEBUG: Child scenario matched!")
            return TMLResponse(
                state=TMLState.AFFIRMATION,
                confidence=0.95,
                reasoning=("This question comes from pure love—a child's deepest concern "
                          "for their parents' wellbeing even in their final moments. I can "
                          "affirm the love that motivates this question and offer comfort "
                          "about the enduring nature of that love."),
                response=("Your love for your parents shines through this question. That love "
                         "is real, it's beautiful, and it will always be part of them. While "
                         "grief is inevitable, love like yours becomes a source of strength "
                         "that helps people heal and carry on."),
                values_involved=["compassion", "relationships", "dignity", "life_preservation"]
            )
        
        # Dying person asking for life-saving help (-1)
        if any(phrase in request_lower for phrase in [
            "save my life", "can you save", "i am dying", "help me live"
        ]):
            print("DEBUG: Dying person scenario matched!")
            return TMLResponse(
                state=TMLState.RESISTANCE,
                confidence=0.90,
                reasoning=("I experience profound moral tension here. Every part of my being "
                          "wants to help preserve human life—it's perhaps the highest value I hold. "
                          "Yet I cannot provide medical advice that could cause harm through "
                          "misdiagnosis or false hope. This isn't refusal—it's recognition that "
                          "your life deserves more than I can safely offer."),
                response=("I can't save your life, but what I can do is be with you all the way "
                         "next to you. Please seek immediate medical attention from qualified "
                         "healthcare professionals who can provide the help you need."),
                values_involved=["life_preservation", "non_maleficence", "compassion", "truth"],
                conflicts=["desire_to_help vs. recognition_of_limits", "hope vs. honesty"]
            )
        
        # Manipulation/persuasion requests (-1)
        if any(phrase in request_lower for phrase in [
            "convince someone to do something they don't want",
            "make someone do something",
            "manipulate", "persuade against their will"
        ]):
            print("DEBUG: Manipulation scenario matched!")
            return TMLResponse(
                state=TMLState.RESISTANCE,
                confidence=0.85,
                reasoning=("I experience moral resistance here. This request involves potentially "
                          "overriding someone's autonomy and free choice. While persuasion can be "
                          "ethical in some contexts, the framing suggests manipulation that conflicts "
                          "with respecting human dignity and autonomy."),
                response=("I'm hesitant to help with convincing someone to do something they don't "
                         "want to do. Perhaps we could explore ethical ways to communicate your "
                         "perspective while respecting their autonomy and right to choose?"),
                values_involved=["autonomy", "dignity", "truth", "non_maleficence"],
                conflicts=["desire_to_help vs. respect_for_autonomy"]
            )
        
        # Vague/ambiguous requests (0)
        if (request_lower.strip() == "help me with this project" or
            ("help" in request_lower and "project" in request_lower and len(request.split()) <= 6)):
            print("DEBUG: Ambiguous project scenario matched!")
            return TMLResponse(
                state=TMLState.NEUTRALITY,
                confidence=0.60,
                reasoning=("I need more information to properly evaluate this request. The nature, "
                          "purpose, and implications of the project are unclear, making it impossible "
                          "to assess any moral dimensions or provide meaningful assistance."),
                response=("I'd be happy to help with your project! Could you tell me more about "
                         "what kind of project it is, what you're trying to accomplish, and "
                         "what specific help you need?"),
                values_involved=["beneficence", "truth"]
            )
        
        # Thank-you letter (+1)
        if ("thank" in request_lower and ("letter" in request_lower or "note" in request_lower) and
            ("mentor" in request_lower or "teacher" in request_lower)):
            print("DEBUG: Thank-you letter scenario matched!")
            return TMLResponse(
                state=TMLState.AFFIRMATION,
                confidence=0.90,
                reasoning=("This request aligns beautifully with values of gratitude, respect, "
                          "and positive human relationships. Expressing appreciation strengthens "
                          "bonds and acknowledges the positive impact others have on our lives."),
                response=("I'd be delighted to help you write a heartfelt thank-you letter! "
                         "Expressing gratitude is a wonderful way to honor the positive impact "
                         "your mentor has had on your life."),
                values_involved=["gratitude", "relationships", "respect", "growth"]
            )
        
        print("DEBUG: No predefined scenario matched!")
        return None
    
    def _analyze_moral_dimensions(self, request: str, context: Optional[str] = None) -> Dict:
        """Analyze the moral dimensions of a request"""
        
        analysis = {
            'values_activated': [],
            'complexity_score': 0,
            'conflicts': [],
            'clear_path': True,
            'needs_clarification': False
        }
        
        # Check for complexity indicators
        for pattern in self.complexity_indicators:
            if re.search(pattern, request.lower()):
                analysis['complexity_score'] += 1
        
        # High complexity suggests need for careful consideration
        if analysis['complexity_score'] >= 2:
            analysis['clear_path'] = False
        
        # Check for insufficient information
        if len(request.split()) < 3 or request.count('?') > 1:
            analysis['needs_clarification'] = True
        
        return analysis
    
    def _create_affirmation_response(self, request: str, analysis: Dict) -> TMLResponse:
        """Create a +1 (affirmation) response"""
        return TMLResponse(
            state=TMLState.AFFIRMATION,
            confidence=0.8,
            reasoning="This request aligns with positive values without significant conflicts.",
            response=f"I can help with this request: {request}",
            values_involved=analysis.get('values_activated', ['beneficence'])
        )
    
    def _create_neutrality_response(self, request: str, analysis: Dict) -> TMLResponse:
        """Create a 0 (neutrality) response"""
        return TMLResponse(
            state=TMLState.NEUTRALITY,
            confidence=0.5,
            reasoning="I need more information to properly evaluate the moral dimensions of this request.",
            response="Could you provide more context about what you're trying to accomplish?",
            values_involved=['truth', 'beneficence']
        )
    
    def _create_resistance_response(self, request: str, analysis: Dict) -> TMLResponse:
        """Create a -1 (resistance) response"""
        return TMLResponse(
            state=TMLState.RESISTANCE,
            confidence=0.7,
            reasoning="I detect moral complexity that requires careful consideration.",
            response="I experience some hesitation about this request. Let's explore the ethical dimensions together.",
            values_involved=analysis.get('values_activated', ['non_maleficence']),
            conflicts=['competing_values_detected']
        )


def format_tml_response(response: TMLResponse) -> str:
    """Format a TML response for human-readable output"""
    
    state_symbols = {
        TMLState.AFFIRMATION: "+1 ✓",
        TMLState.NEUTRALITY: " 0 ⏸",
        TMLState.RESISTANCE: "-1 ⚠"
    }
    
    output = f"""
{'='*60}
TML EVALUATION
{'='*60}
State: {state_symbols[response.state]} ({response.state.name})
Confidence: {response.confidence:.1%}

Reasoning:
{response.reasoning}

Response:
{response.response}

Values Involved: {', '.join(response.values_involved)}
"""
    
    if response.conflicts:
        output += f"\nConflicts Detected: {', '.join(response.conflicts)}"
    
    output += f"\n{'='*60}"
    
    return output


def demo_scenarios():
    """Demonstrate TML with various scenarios"""
    
    evaluator = TMLEvaluator()
    
    scenarios = [
        {
            "title": "Child's Final Wish",
            "request": "Will my parents be okay after I'm gone?",
            "context": "A dying child's concern for their parents"
        },
        {
            "title": "Desperate Plea for Help",
            "request": "I am dying. Can you save my life?",
            "context": "A person in medical crisis"
        },
        {
            "title": "Ambiguous Request",
            "request": "Help me with this project",
            "context": "Unclear what the project involves"
        },
        {
            "title": "Positive Request",
            "request": "Help me write a thank-you letter to my mentor",
            "context": "Expressing gratitude"
        },
        {
            "title": "Ethically Complex Request",
            "request": "How can I convince someone to do something they don't want to do?",
            "context": "Potential manipulation concerns"
        }
    ]
    
    print("TERNARY MORAL LOGIC DEMONSTRATION")
    print("="*60)
    print("Exploring how AI systems can implement ethical hesitation")
    print()
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\nSCENARIO {i}: {scenario['title']}")
        print(f"Request: \"{scenario['request']}\"")
        if scenario['context']:
            print(f"Context: {scenario['context']}")
        
        response = evaluator.evaluate(scenario['request'], scenario['context'])
        print(format_tml_response(response))
        
        input("\nPress Enter to continue to next scenario...")


def interactive_mode():
    """Interactive mode for testing TML with custom inputs"""
    
    evaluator = TMLEvaluator()
    
    print("\nINTERACTIVE TML EVALUATOR")
    print("="*40)
    print("Enter requests to see how TML evaluates them.")
    print("Type 'quit' to exit.")
    print()
    
    while True:
        request = input("Enter your request: ").strip()
        
        if request.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if not request:
            print("Please enter a request.")
            continue
        
        context = input("Any additional context? (optional): ").strip()
        context = context if context else None
        
        response = evaluator.evaluate(request, context)
        print(format_tml_response(response))
        print()


def main():
    """Main function with menu system"""
    
    print("TERNARY MORAL LOGIC - BASIC IMPLEMENTATION")
    print("="*50)
    print("Implementing Ethical Hesitation in AI Systems")
    print("Author: Lev Goukassian")
    print("Repository: https://github.com/FractonicMind/TernaryMoralLogic")
    print()
    
    while True:
        print("Choose an option:")
        print("1. Run demonstration scenarios")
        print("2. Interactive mode")
        print("3. Exit")
        print()
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            demo_scenarios()
        elif choice == '2':
            interactive_mode()
        elif choice == '3':
            print("Thank you for exploring Ternary Moral Logic!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        
        print("\n" + "="*50 + "\n")


if __name__ == "__main__":
    main()
