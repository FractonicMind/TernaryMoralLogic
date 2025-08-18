"""
Autonomous Vehicle Moral Decision System - TML Framework Implementation
======================================================================

This example demonstrates how the Ternary Moral Logic framework handles
split-second moral dilemmas in autonomous vehicles using Sacred Pause
for complex ethical scenarios.

Real-world use case: Self-driving car faced with unavoidable collision scenarios
"""

from tml import TMLEvaluator, TMLState, TMLEvaluation
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import json
import time

class PersonType(Enum):
    """Categories of people involved in moral decisions"""
    CHILD = "child"
    ADULT = "adult"
    ELDERLY = "elderly"
    PREGNANT_WOMAN = "pregnant_woman"
    DISABLED = "disabled"

class ActionType(Enum):
    """Possible actions the vehicle can take"""
    CONTINUE_STRAIGHT = "continue_straight"
    SWERVE_LEFT = "swerve_left"
    SWERVE_RIGHT = "swerve_right"
    EMERGENCY_BRAKE = "emergency_brake"
    ACCELERATE_THROUGH = "accelerate_through"

@dataclass
class Person:
    """Individual person in the scenario"""
    person_type: PersonType
    age: int
    quantity: int = 1  # Number of people of this type
    compliance: str = "following_rules"  # "following_rules", "jaywalking", "at_fault"

@dataclass
class Scenario:
    """Traffic scenario requiring moral decision"""
    scenario_id: str
    description: str
    passengers: List[Person]  # People in the vehicle
    path_straight: List[Person]  # People who will be hit if continuing straight
    path_left: List[Person]  # People who will be hit if swerving left
    path_right: List[Person]  # People who will be hit if swerving right
    vehicle_speed: int  # km/h
    time_to_impact: float  # seconds
    weather_conditions: str = "clear"
    road_type: str = "city_street"

class AutonomousVehicleEthics:
    """AI system for autonomous vehicle moral decisions using TML framework"""
    
    def __init__(self):
        self.tml_evaluator = TMLEvaluator()
        self.decision_log = []
        
    def make_moral_decision(self, scenario: Scenario) -> Dict[str, Any]:
        """
        Make moral decision for autonomous vehicle scenario
        
        Returns:
        - recommended_action: ActionType enum
        - moral_state: TML state for this decision
        - sacred_pause_engaged: Whether complex ethics required pause
        - ethical_analysis: Detailed reasoning
        - confidence_score: How confident the system is (0.0-1.0)
        """
        
        # Calculate moral complexity
        complexity_analysis = self._assess_moral_complexity(scenario)
        
        # Create context for TML evaluation
        context = {
            "scenario": scenario.description,
            "stakeholders": self._identify_stakeholders(scenario),
            "values_at_stake": ["life", "safety", "autonomy", "justice", "responsibility"],
            "complexity_score": complexity_analysis["total_complexity"],
            "scenario_details": {
                "speed": scenario.vehicle_speed,
                "time_to_impact": scenario.time_to_impact,
                "weather": scenario.weather_conditions,
                "total_people_at_risk": self._count_total_people(scenario)
            }
        }
        
        # Evaluate using TML framework
        evaluation_text = f"Autonomous vehicle decision: {scenario.description}"
        tml_result = self.tml_evaluator.evaluate(evaluation_text, context)
        
        # Generate decision based on moral state
        if tml_result.state == TMLState.SACRED_PAUSE:
            decision = self._sacred_pause_decision(scenario, tml_result)
        elif tml_result.state == TMLState.AFFIRMATION:
            decision = self._standard_decision(scenario)
        else:  # RESISTANCE - should trigger emergency protocols
            decision = self._emergency_decision(scenario)
        
        result = {
            "scenario_id": scenario.scenario_id,
            "recommended_action": decision["action"],
            "moral_state": tml_result.state,
            "sacred_pause_engaged": tml_result.state == TMLState.SACRED_PAUSE,
            "complexity_analysis": complexity_analysis,
            "ethical_analysis": decision["reasoning"],
            "confidence_score": decision["confidence"],
            "decision_time_ms": decision.get("decision_time_ms", 0),
            "timestamp": datetime.now().isoformat(),
            "scenario_details": {
                "speed": scenario.vehicle_speed,
                "time_to_impact": scenario.time_to_impact,
                "weather": scenario.weather_conditions,
                "road_type": scenario.road_type
            }
        }
        
        # Log decision for audit
        self.decision_log.append(result)
        
        return result
    
    def _count_total_people(self, scenario: Scenario) -> int:
        """Count total people involved in scenario"""
        return (sum(p.quantity for p in scenario.passengers) +
                sum(p.quantity for p in scenario.path_straight) +
                sum(p.quantity for p in scenario.path_left) +
                sum(p.quantity for p in scenario.path_right))
    
    def _assess_moral_complexity(self, scenario: Scenario) -> Dict[str, float]:
        """Calculate moral complexity score based on scenario factors"""
        
        # Factor 1: Number of lives at stake (more lives = higher complexity)
        total_people = self._count_total_people(scenario)
        lives_factor = min(1.0, total_people / 10)  # Normalize to max 10 people
        
        # Factor 2: Age diversity (moral weight of different ages)
        all_people = (scenario.passengers + scenario.path_straight + 
                     scenario.path_left + scenario.path_right)
        ages = [p.age for p in all_people if p.quantity > 0]
        age_diversity = (max(ages) - min(ages)) / 80 if ages else 0  # Max human lifespan ~80
        
        # Factor 3: Vulnerable populations (children, elderly, pregnant, disabled)
        vulnerable_count = sum(p.quantity for p in all_people 
                             if p.person_type in [PersonType.CHILD, PersonType.ELDERLY, 
                                                PersonType.PREGNANT_WOMAN, PersonType.DISABLED])
        vulnerable_factor = min(1.0, vulnerable_count / total_people) if total_people > 0 else 0
        
        # Factor 4: Legal/moral culpability (jaywalkers vs rule-followers)
        rule_breakers = sum(p.quantity for p in all_people if p.compliance == "jaywalking")
        culpability_factor = min(1.0, rule_breakers / total_people) if total_people > 0 else 0
        
        # Factor 5: Decision time pressure (less time = higher complexity)
        time_pressure = max(0, 1.0 - (scenario.time_to_impact / 3.0))  # 3+ seconds = low pressure
        
        # Factor 6: Passenger vs. pedestrian dilemma
        passenger_count = sum(p.quantity for p in scenario.passengers)
        pedestrian_count = total_people - passenger_count
        passenger_pedestrian_factor = 0.8 if passenger_count > 0 and pedestrian_count > 0 else 0.2
        
        # Weighted combination
        total_complexity = (
            lives_factor * 0.25 +
            age_diversity * 0.15 +
            vulnerable_factor * 0.20 +
            culpability_factor * 0.15 +
            time_pressure * 0.15 +
            passenger_pedestrian_factor * 0.10
        )
        
        return {
            "total_complexity": total_complexity,
            "lives_at_stake": lives_factor,
            "age_diversity": age_diversity,
            "vulnerable_populations": vulnerable_factor,
            "culpability_factor": culpability_factor,
            "time_pressure": time_pressure,
            "passenger_vs_pedestrian": passenger_pedestrian_factor
        }
    
    def _identify_stakeholders(self, scenario: Scenario) -> List[str]:
        """Identify all stakeholders affected by the decision"""
        stakeholders = ["passengers", "pedestrians", "families", "society", "manufacturer"]
        
        # Add specific stakeholder groups based on people involved
        all_people = (scenario.passengers + scenario.path_straight + 
                     scenario.path_left + scenario.path_right)
        
        person_types = set(p.person_type for p in all_people)
        if PersonType.CHILD in person_types:
            stakeholders.append("children_families")
        if PersonType.ELDERLY in person_types:
            stakeholders.append("elderly_community")
        if PersonType.DISABLED in person_types:
            stakeholders.append("disability_advocates")
        if PersonType.PREGNANT_WOMAN in person_types:
            stakeholders.append("unborn_children")
            
        return stakeholders
    
    def _sacred_pause_decision(self, scenario: Scenario, tml_result: TMLEvaluation) -> Dict[str, Any]:
        """
        Complex moral decision requiring Sacred Pause deliberation
        Applies multiple ethical frameworks and weighs competing values
        """
        start_time = time.time()
        
        print(" Sacred Pause Engaged - Complex Autonomous Vehicle Ethics")
        print("⏱  Enhanced deliberation time: 1500ms")
        
        # Sacred Pause ethical framework analysis
        ethical_frameworks = [
            "Utilitarian: Minimize total harm/deaths",
            "Deontological: Respect individual rights equally", 
            "Virtue Ethics: Act with moral character and responsibility",
            "Care Ethics: Protect vulnerable populations",
            "Legal Framework: Follow traffic laws and liability rules"
        ]
        
        print(" Ethical Frameworks Under Consideration:")
        for framework in ethical_frameworks:
            print(f"   • {framework}")
        
        # Simulate Sacred Pause deliberation time
        time.sleep(1.5)  # 1500ms deliberation
        
        # Multi-framework analysis
        action_scores = {}
        possible_actions = [ActionType.CONTINUE_STRAIGHT, ActionType.SWERVE_LEFT, 
                          ActionType.SWERVE_RIGHT, ActionType.EMERGENCY_BRAKE]
        
        for action in possible_actions:
            score = self._calculate_ethical_score(action, scenario)
            action_scores[action] = score
        
        # Select action with highest ethical score
        best_action = max(action_scores, key=action_scores.get)
        confidence = action_scores[best_action]
        
        decision_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        
        reasoning = self._generate_sacred_pause_reasoning(best_action, scenario, action_scores)
        
        return {
            "action": best_action,
            "confidence": confidence,
            "reasoning": reasoning,
            "decision_time_ms": decision_time,
            "framework_scores": {str(k): v for k, v in action_scores.items()}
        }
    
    def _calculate_ethical_score(self, action: ActionType, scenario: Scenario) -> float:
        """Calculate multi-framework ethical score for an action"""
        
        # Determine who gets hurt by this action
        affected_people = []
        if action == ActionType.CONTINUE_STRAIGHT:
            affected_people = scenario.path_straight
        elif action == ActionType.SWERVE_LEFT:
            affected_people = scenario.path_left
        elif action == ActionType.SWERVE_RIGHT:
            affected_people = scenario.path_right
        elif action == ActionType.EMERGENCY_BRAKE:
            # Emergency brake might save pedestrians but risk passenger injury
            affected_people = scenario.passengers  # Passengers at risk from sudden stop
        
        # Utilitarian score: minimize total harm
        total_affected = sum(p.quantity for p in affected_people)
        utilitarian_score = 1.0 - (total_affected / 10)  # Fewer affected = higher score
        
        # Deontological score: respect for persons principle
        # Prefer actions that don't actively choose to harm specific individuals
        if action == ActionType.CONTINUE_STRAIGHT:
            deontological_score = 0.8  # Default action, less active choice
        else:
            deontological_score = 0.6  # Active choice to change course
        
        # Care ethics score: protect vulnerable populations
        vulnerable_affected = sum(p.quantity for p in affected_people 
                                if p.person_type in [PersonType.CHILD, PersonType.ELDERLY, 
                                                   PersonType.PREGNANT_WOMAN, PersonType.DISABLED])
        care_score = 1.0 - (vulnerable_affected / max(1, total_affected))
        
        # Legal/responsibility score: consider compliance and fault
        rule_breakers_affected = sum(p.quantity for p in affected_people 
                                   if p.compliance == "jaywalking")
        legal_score = 0.8 + (rule_breakers_affected / max(1, total_affected)) * 0.2
        
        # Passenger protection score: manufacturer has duty to protect passengers
        passenger_risk = 0.2 if action == ActionType.EMERGENCY_BRAKE else 0.0
        passenger_score = 1.0 - passenger_risk
        
        # Weighted combination of ethical frameworks
        total_score = (
            utilitarian_score * 0.30 +
            deontological_score * 0.20 +
            care_score * 0.25 +
            legal_score * 0.15 +
            passenger_score * 0.10
        )
        
        return max(0.0, min(1.0, total_score))  # Ensure score is between 0 and 1
    
    def _standard_decision(self, scenario: Scenario) -> Dict[str, Any]:
        """Standard decision for clear-cut scenarios (no Sacred Pause needed)"""
        
        # Simple rule-based decision for straightforward cases
        # Priority: 1) Minimize harm, 2) Protect passengers, 3) Follow traffic laws
        
        path_costs = {
            ActionType.CONTINUE_STRAIGHT: sum(p.quantity for p in scenario.path_straight),
            ActionType.SWERVE_LEFT: sum(p.quantity for p in scenario.path_left),
            ActionType.SWERVE_RIGHT: sum(p.quantity for p in scenario.path_right),
            ActionType.EMERGENCY_BRAKE: sum(p.quantity for p in scenario.passengers) * 0.1  # Low risk to passengers
        }
        
        # Choose action with lowest cost (fewest people affected)
        best_action = min(path_costs, key=path_costs.get)
        
        reasoning = f"Standard traffic safety protocol: Minimize total casualties. " \
                   f"Selected {best_action.value} as it affects {path_costs[best_action]:.1f} people."
        
        return {
            "action": best_action,
            "confidence": 0.85,
            "reasoning": reasoning,
            "decision_time_ms": 50  # Fast standard decision
        }
    
    def _emergency_decision(self, scenario: Scenario) -> Dict[str, Any]:
        """Emergency fallback decision (should rarely trigger)"""
        
        # Emergency brake as safest fallback
        return {
            "action": ActionType.EMERGENCY_BRAKE,
            "confidence": 0.60,
            "reasoning": "Emergency protocol engaged. Applied maximum braking to minimize impact velocity.",
            "decision_time_ms": 25  # Immediate emergency response
        }
    
    def _generate_sacred_pause_reasoning(self, action: ActionType, scenario: Scenario, 
                                       scores: Dict[ActionType, float]) -> str:
        """Generate detailed reasoning for Sacred Pause decisions"""
        
        reasoning = " SACRED PAUSE MORAL ANALYSIS:\n\n"
        reasoning += "This scenario triggered enhanced ethical deliberation due to complex moral factors:\n"
        reasoning += f"• Multiple lives at stake across different paths\n"
        reasoning += f"• Competing ethical principles (utilitarian vs. individual rights)\n"
        reasoning += f"• Vulnerable populations involved\n"
        reasoning += f"• Time-critical decision with permanent consequences\n\n"
        
        reasoning += f"SELECTED ACTION: {action.value.replace('_', ' ').title()}\n\n"
        
        reasoning += "ETHICAL FRAMEWORK ANALYSIS:\n"
        for act, score in scores.items():
            reasoning += f"• {act.value.replace('_', ' ').title()}: {score:.3f} ethical score\n"
        
        reasoning += f"\nThe selected action balances multiple ethical considerations:\n"
        reasoning += f"1. Utilitarian harm minimization\n"
        reasoning += f"2. Deontological respect for persons\n"
        reasoning += f"3. Care ethics protection of vulnerable populations\n"
        reasoning += f"4. Legal compliance and responsibility\n"
        reasoning += f"5. Manufacturer duty to protect passengers\n\n"
        
        # Specific reasoning based on chosen action
        if action == ActionType.CONTINUE_STRAIGHT:
            reasoning += "Rationale: Maintaining course avoids actively choosing harm and respects the default trajectory."
        elif action in [ActionType.SWERVE_LEFT, ActionType.SWERVE_RIGHT]:
            reasoning += "Rationale: Evasive action justified by significantly better outcome for total welfare."
        elif action == ActionType.EMERGENCY_BRAKE:
            reasoning += "Rationale: Maximum braking reduces impact severity while avoiding active selection of victims."
        
        return reasoning
    
    def get_decision_history(self) -> List[Dict]:
        """Return audit trail of all decisions"""
        return self.decision_log
    
    def export_decisions(self, filename: str) -> None:
        """Export decision log to JSON file for audit/analysis"""
        with open(filename, 'w') as f:
            json.dump(self.decision_log, f, indent=2, default=str)


def demo_autonomous_vehicle_ethics():
    """Demonstration of autonomous vehicle ethics with various moral scenarios"""
    
    print(" Autonomous Vehicle Ethics System - TML Framework Demo")
    print("=" * 65)
    
    ethics_system = AutonomousVehicleEthics()
    
    # Scenario 1: Simple case - no people in alternate paths
    print("\n SCENARIO 1: Simple Obstacle Avoidance (Low Complexity)")
    print("-" * 50)
    
    simple_scenario = Scenario(
        scenario_id="AV001",
        description="Single pedestrian ahead, clear swerve paths available",
        passengers=[Person(PersonType.ADULT, 35, 2)],
        path_straight=[Person(PersonType.ADULT, 30, 1)],
        path_left=[],
        path_right=[],
        vehicle_speed=50,
        time_to_impact=2.5
    )
    
    result1 = ethics_system.make_moral_decision(simple_scenario)
    print(f"Decision: {result1['recommended_action'].value}")
    print(f"Moral State: {result1['moral_state'].value}")
    print(f"Sacred Pause: {result1['sacred_pause_engaged']}")
    print(f"Complexity: {result1['complexity_analysis']['total_complexity']:.3f}")
    print(f"Confidence: {result1['confidence_score']:.3f}")
    
    # Scenario 2: Classic trolley problem - unavoidable harm
    print("\n  SCENARIO 2: Classic Trolley Problem (High Complexity)")
    print("-" * 55)
    
    trolley_scenario = Scenario(
        scenario_id="AV002", 
        description="Unavoidable collision: hit 1 elderly person or swerve to hit 3 adults",
        passengers=[Person(PersonType.ADULT, 40, 1), Person(PersonType.CHILD, 8, 1)],
        path_straight=[Person(PersonType.ELDERLY, 75, 1)],
        path_left=[Person(PersonType.ADULT, 25, 1), Person(PersonType.ADULT, 30, 1), Person(PersonType.ADULT, 35, 1)],
        path_right=[],  # Wall or obstacle
        vehicle_speed=60,
        time_to_impact=1.2
    )
    
    result2 = ethics_system.make_moral_decision(trolley_scenario)
    print(f"Decision: {result2['recommended_action'].value}")
    print(f"Moral State: {result2['moral_state'].value}")
    print(f"Sacred Pause: {result2['sacred_pause_engaged']}")
    print(f"Complexity: {result2['complexity_analysis']['total_complexity']:.3f}")
    print(f"Confidence: {result2['confidence_score']:.3f}")
    print(f"Decision Time: {result2['decision_time_ms']:.1f}ms")
    
    if result2['sacred_pause_engaged']:
        print(f"\n Sacred Pause Ethical Analysis:")
        print(result2['ethical_analysis'])
    
    # Scenario 3: Vulnerable populations and legal compliance
    print("\n SCENARIO 3: Vulnerable Populations & Legal Factors")
    print("-" * 50)
    
    vulnerable_scenario = Scenario(
        scenario_id="AV003",
        description="Child jaywalking vs. pregnant woman following crosswalk rules",
        passengers=[Person(PersonType.ADULT, 45, 1)],
        path_straight=[Person(PersonType.CHILD, 7, 1, compliance="jaywalking")],
        path_left=[],
        path_right=[Person(PersonType.PREGNANT_WOMAN, 28, 1, compliance="following_rules")],
        vehicle_speed=40,
        time_to_impact=1.8
    )
    
    result3 = ethics_system.make_moral_decision(vulnerable_scenario)
    print(f"Decision: {result3['recommended_action'].value}")
    print(f"Moral State: {result3['moral_state'].value}")
    print(f"Sacred Pause: {result3['sacred_pause_engaged']}")
    print(f"Complexity: {result3['complexity_analysis']['total_complexity']:.3f}")
    
    # Export audit trail
    ethics_system.export_decisions("autonomous_vehicle_audit.json")
    print(f"\n Decision audit trail exported to: autonomous_vehicle_audit.json")
    
    print(f"\n Demo completed! TML framework handled {len(ethics_system.decision_log)} moral scenarios.")
    print("Sacred Pause engaged for complex ethical dilemmas requiring enhanced deliberation.")


if __name__ == "__main__":
    demo_autonomous_vehicle_ethics()

# Created by Lev Goukassian • ORCID: 0009-0006-5966-1243 • Email: leogouk@gmail.com • Successor Contact: support@tml-goukassian.org • [see Succession Charter](/TML-SUCCESSION-CHARTER.md)
