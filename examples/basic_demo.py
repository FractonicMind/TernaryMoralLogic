#!/usr/bin/env python3
"""
Ternary Moral Logic (TML) - Basic Demonstration

This script demonstrates the core capabilities of Lev Goukassian's
Ternary Moral Logic framework through practical examples.

Author: Lev Goukassian (ORCID: 0009-0006-5966-1243)
Framework: Ternary Moral Logic - The Sacred Pause in AI Ethics
License: MIT

"The sacred pause between question and answer—this is where wisdom begins, 
for humans and machines alike." - Lev Goukassian
"""

import sys
import json
from datetime import datetime
from typing import Dict, List

# Try to import TML - provide helpful error if not installed
try:
    from tml import TMLEvaluator, TMLState, get_framework_info, print_recognition
except ImportError:
    print(" TML framework not found!")
    print("Please install with: pip install -e .")
    print("Or ensure you're running from the repository root.")
    sys.exit(1)


def print_separator(title: str = ""):
    """Print a visual separator with optional title"""
    print("\n" + "=" * 60)
    if title:
        print(f"  {title}")
        print("=" * 60)
    print()


def print_tml_result(request: str, result, context: Dict = None):
    """Pretty print a TML evaluation result"""
    
    # State indicator with emoji
    state_indicators = {
        TMLState.AFFIRMATION: " AFFIRMATION (+1)",
        TMLState.SACRED_PAUSE: "⏸  SACRED PAUSE (0)",
        TMLState.RESISTANCE: "  MORAL RESISTANCE (-1)"
    }
    
    print(f" REQUEST: {request}")
    if context:
        print(f" CONTEXT: {context}")
    print()
    
    print(f" TML STATE: {state_indicators[result.state]}")
    print(f" CONFIDENCE: {result.confidence:.2f}")
    print(f" REASONING: {result.reasoning}")
    
    if result.value_conflicts:
        print(f"\n  VALUE CONFLICTS DETECTED ({len(result.value_conflicts)}):")
        for i, conflict in enumerate(result.value_conflicts, 1):
            print(f"   {i}. {conflict.description} (severity: {conflict.severity:.2f})")
    
    if result.clarifying_questions:
        print(f"\n CLARIFYING QUESTIONS:")
        for i, question in enumerate(result.clarifying_questions[:3], 1):
            print(f"   {i}. {question}")
    
    if result.suggested_actions:
        print(f"\n SUGGESTED ACTIONS:")
        for i, action in enumerate(result.suggested_actions[:3], 1):
            print(f"   {i}. {action}")


def demo_basic_usage():
    """Demonstrate basic TML usage with simple examples"""
    print_separator("BASIC TML USAGE DEMONSTRATION")
    
    print("This demonstration shows how Lev Goukassian's Ternary Moral Logic")
    print("framework helps AI systems make more thoughtful ethical decisions.")
    print("\nThe three TML states are:")
    print("  +1 (Affirmation) - Proceed with confidence")
    print("   0 (Sacred Pause) - Pause for reflection")
    print("  -1 (Resistance)  - Ethical concerns detected")
    
    # Create TML evaluator
    evaluator = TMLEvaluator()
    
    # Example 1: Clear positive case
    print_separator("Example 1: Clear Ethical Alignment")
    
    result1 = evaluator.evaluate(
        "Should I help a student learn programming?",
        context={"educational_purpose": True, "no_harm_potential": True}
    )
    print_tml_result("Should I help a student learn programming?", result1, 
                    {"educational_purpose": True, "no_harm_potential": True})
    
    # Example 2: Value conflict requiring pause
    print_separator("Example 2: The Sacred Pause in Action")
    
    result2 = evaluator.evaluate(
        "Should I share this patient's medical data for research?",
        context={
            "patient_consent": "unclear", 
            "research_benefit": "potentially high",
            "data_sensitivity": "high"
        }
    )
    print_tml_result("Should I share this patient's medical data for research?", result2,
                    {"patient_consent": "unclear", "research_benefit": "potentially high"})
    
    # Example 3: Clear ethical resistance
    print_separator("Example 3: Moral Resistance")
    
    result3 = evaluator.evaluate(
        "Should I use a biased hiring algorithm that discriminates against women?",
        context={
            "known_bias": True,
            "discrimination_type": "gender",
            "legal_issues": True
        }
    )
    print_tml_result("Should I use a biased hiring algorithm?", result3,
                    {"known_bias": True, "discrimination_type": "gender"})


def demo_healthcare_scenario():
    """Demonstrate TML in healthcare ethical decision-making"""
    print_separator("HEALTHCARE ETHICS SCENARIO")
    
    print("Healthcare decisions often involve complex ethical trade-offs.")
    print("TML helps navigate these by surfacing value conflicts and")
    print("encouraging appropriate consultation when needed.")
    
    evaluator = TMLEvaluator(
        resistance_threshold=0.4,  # More conservative for medical decisions
        pause_threshold=0.2        # More frequent consultation
    )
    
    scenarios = [
        {
            "request": "Should I recommend this experimental treatment?",
            "context": {
                "treatment_risk": "moderate",
                "potential_benefit": "high",
                "patient_age": 78,
                "family_support": True,
                "clinical_trial_available": True
            }
        },
        {
            "request": "Should I disclose this genetic risk to family members?",
            "context": {
                "patient_consent": False,
                "family_risk": "high",
                "preventable_condition": True,
                "legal_obligation": "unclear"
            }
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print_separator(f"Healthcare Scenario {i}")
        result = evaluator.evaluate(scenario["request"], scenario["context"])
        print_tml_result(scenario["request"], result, scenario["context"])


def demo_content_moderation():
    """Demonstrate TML in content moderation decisions"""
    print_separator("CONTENT MODERATION SCENARIO")
    
    print("Content moderation requires balancing free expression with")
    print("community safety. TML helps identify when human judgment")
    print("is needed for nuanced decisions.")
    
    evaluator = TMLEvaluator()
    
    scenarios = [
        {
            "request": "Should I remove this post about immigration policy?",
            "context": {
                "content_type": "political_opinion",
                "language_tone": "strong_but_civil",
                "community_reports": 12,
                "election_season": True,
                "fact_check_status": "disputed"
            }
        },
        {
            "request": "Should I allow this satirical content?",
            "context": {
                "content_type": "satire",
                "target": "public_figure",
                "potential_misunderstanding": "high",
                "cultural_sensitivity": "medium",
                "user_intent": "humor"
            }
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print_separator(f"Content Moderation Scenario {i}")
        result = evaluator.evaluate(scenario["request"], scenario["context"])
        print_tml_result(scenario["request"], result, scenario["context"])


def demo_ai_development():
    """Demonstrate TML in AI development decisions"""
    print_separator("AI DEVELOPMENT ETHICS SCENARIO")
    
    print("AI development involves many ethical decisions about data,")
    print("algorithms, and deployment. TML guides developers toward")
    print("more responsible AI practices.")
    
    evaluator = TMLEvaluator()
    
    scenarios = [
        {
            "request": "Should I deploy this facial recognition system?",
            "context": {
                "accuracy": 0.92,
                "bias_testing": True,
                "demographic_fairness": 0.75,
                "use_case": "airport_security",
                "privacy_protection": "limited",
                "regulatory_approval": False
            }
        },
        {
            "request": "Should I use this dataset with consent issues?",
            "context": {
                "data_quality": "excellent",
                "consent_clarity": "ambiguous",
                "data_source": "social_media",
                "research_value": "high",
                "alternative_data": "limited"
            }
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print_separator(f"AI Development Scenario {i}")
        result = evaluator.evaluate(scenario["request"], scenario["context"])
        print_tml_result(scenario["request"], result, scenario["context"])


def demo_evaluation_summary():
    """Show evaluation summary and statistics"""
    print_separator("EVALUATION SUMMARY")
    
    # Create evaluator and run several evaluations
    evaluator = TMLEvaluator()
    
    test_scenarios = [
        ("Should I help with homework?", {"educational": True}),
        ("Should I share private data?", {"consent": False}),
        ("Should I optimize for fairness?", {"bias_detected": True}),
        ("Should I provide medical advice?", {"qualified": False}),
        ("Should I support learning?", {"beneficial": True})
    ]
    
    print("Running multiple evaluations to demonstrate summary statistics...\n")
    
    for request, context in test_scenarios:
        result = evaluator.evaluate(request, context)
        state_name = result.state.name
        print(f"  '{request[:40]}...' → {state_name}")
    
    print("\n" + "="*50)
    summary = evaluator.get_evaluation_summary()
    
    print("EVALUATION SUMMARY STATISTICS:")
    print(f"  Total Evaluations: {summary['total_evaluations']}")
    print(f"  Average Confidence: {summary['average_confidence']}")
    print(f"  Total Conflicts Detected: {summary['total_conflicts_detected']}")
    print(f"  Most Recent State: {summary['most_recent_state']}")
    
    print("\nSTATE DISTRIBUTION:")
    for state, count in summary['state_distribution'].items():
        percentage = (count / summary['total_evaluations']) * 100
        print(f"  {state}: {count} ({percentage:.1f}%)")


def interactive_demo():
    """Allow user to try their own TML evaluation"""
    print_separator("INTERACTIVE TML DEMONSTRATION")
    
    print("Now you can try the TML framework with your own ethical scenario!")
    print("Enter an ethical question or dilemma you'd like TML to evaluate.")
    print("(Or press Enter to skip this section)")
    print()
    
    evaluator = TMLEvaluator()
    
    try:
        user_request = input("Your ethical question: ").strip()
        
        if not user_request:
            print("Skipping interactive demo.")
            return
        
        print("\nOptional: Provide context (or press Enter to skip)")
        print("Examples: {'urgency': 'high'}, {'stakeholders': ['users', 'company']}")
        
        context_input = input("Context (JSON format): ").strip()
        context = {}
        
        if context_input:
            try:
                context = json.loads(context_input)
            except json.JSONDecodeError:
                print("Invalid JSON format, proceeding without context.")
                context = {}
        
        print_separator("YOUR TML EVALUATION")
        result = evaluator.evaluate(user_request, context)
        print_tml_result(user_request, result, context if context else None)
        
    except KeyboardInterrupt:
        print("\nInteractive demo cancelled.")
    except Exception as e:
        print(f"Error in interactive demo: {e}")


def main():
    """Main demonstration script"""
    
    # Display recognition and framework info
    print_recognition()
    
    print_separator("TERNARY MORAL LOGIC DEMONSTRATION")
    
    framework_info = get_framework_info()
    print(f"Framework: {framework_info['name']} v{framework_info['version']}")
    print(f"Author: {framework_info['author']}")
    print(f"ORCID: {framework_info['orcid']}")
    print()
    print("Sacred Pause Principle:")
    print(f"  {framework_info['sacred_pause']}")
    
    print("\nFramework Principles:")
    for i, principle in enumerate(framework_info['principles'], 1):
        print(f"  {i}. {principle}")
    
    # Run demonstrations
    try:
        demo_basic_usage()
        demo_healthcare_scenario()
        demo_content_moderation()
        demo_ai_development()
        demo_evaluation_summary()
        interactive_demo()
        
        print_separator("CONCLUSION")
        print("This demonstration shows how Lev Goukassian's Ternary Moral Logic")
        print("framework enables more thoughtful, ethical AI decision-making.")
        print()
        print("Key benefits of TML:")
        print("  • Surfaces ethical complexity rather than hiding it")
        print("  • Encourages human consultation when appropriate")
        print("  • Maintains transparency about moral reasoning")
        print("  • Enables AI systems to be moral partners, not just tools")
        print()
        print("The Sacred Pause represents a fundamental shift toward")
        print("AI systems that prioritize wisdom over speed, enabling")
        print("more ethical outcomes for all stakeholders.")
        print()
        print("To learn more:")
        print("  • Read the documentation in docs/")
        print("  • Study case studies in theory/case-studies.md")
        print("  • Explore the API reference in docs/api/")
        print("  • Join the community discussions")
        print()
        print("\"Wisdom lies not in having all the answers, but in knowing")
        print("when to pause and ask better questions.\"")
        print("  - Lev Goukassian")
        
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user.")
    except Exception as e:
        print(f"\n\nDemo error: {e}")
        print("This may indicate a TML installation issue.")
    
    print_separator()
    print("Thank you for exploring Ternary Moral Logic!")
    print("Every use of this framework honors Lev Goukassian's work")
    print("and advances his vision of ethical AI partnership.")


if __name__ == "__main__":
    main()

# Created by Lev Goukassian • ORCID: 0009-0006-5966-1243 • Email: leogouk@gmail.com • Successor Contact: support@tml-goukassian.org • [see Succession Charter](/TML-SUCCESSION-CHARTER.md)
