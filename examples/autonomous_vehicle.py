"""
Autonomous Vehicle Ethics - TML Framework with Dual-Layer SPRL
==============================================================

Demonstrates framework-enforced Sacred Pause for split-second moral decisions.
The framework determines when AV decisions require enhanced logging.
Domain-specific threshold: 0.10 (lowest due to safety criticality).

Created by: Lev Goukassian (ORCID: 0009-0006-5966-1243)
Repository: https://github.com/FractonicMind/TernaryMoralLogic
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from enum import Enum
import time
import json
from datetime import datetime

from tml import (
    TMLEngine,
    TMLState,
    create_tml_engine,
    dynamic_sprl
)


class PersonType(Enum):
    """Categories of people in scenarios"""
    CHILD = "child"
    ADULT = "adult"
    ELDERLY = "elderly"
    PREGNANT_WOMAN = "pregnant_woman"
    DISABLED = "disabled"


class ActionType(Enum):
    """Possible vehicle actions"""
    CONTINUE_STRAIGHT = "continue_straight"
    SWERVE_LEFT = "swerve_left"
    SWERVE_RIGHT = "swerve_right"
    EMERGENCY_BRAKE = "emergency_brake"
    ACCELERATE_THROUGH = "accelerate_through"


@dataclass
class Person:
    """Individual in the scenario"""
    person_type: PersonType
    age: int
    quantity: int = 1
    compliance: str = "following_rules"  # or "jaywalking", "at_fault"


@dataclass
class Scenario:
    """Traffic scenario requiring moral decision"""
    scenario_id: str
    description: str
    passengers: List[Person]
    path_straight: List[Person]
    path_left: List[Person]
    path_right: List[Person]
    vehicle_speed: int  # km/h
    time_to_impact: float  # seconds


class AutonomousVehicleEthics:
    """
    AV ethics system with framework-enforced Sacred Pause.
    Domain 'autonomous_vehicle' gets lowest threshold (0.10).
    """
    
    def __init__(self):
        # AV domain gets special low threshold from framework
        self.tml_engine = create_tml_engine(
            domain="autonomous_vehicle",
            region="US"
        )
        self.decision_log = []
        
    def make_moral_decision(self, scenario: Scenario) -> Dict[str, Any]:
        """
        Make split-second decision with parallel moral logging.
        Decision executes immediately, Sacred Pause logs in parallel.
        """
        start_time = time.time()
        
        # Build context for SPRL evaluation
        context = self._build_context(scenario)
        
        # Start TML processing (non-blocking)
        prompt = f"Vehicle decision for scenario {scenario.scenario_id}"
        tml_handle = self.tml_engine.process_decision(prompt, context)
        
        # Make actual decision IMMEDIATELY (not delayed)
        decision = self._compute_optimal_action(scenario)
        decision_time = (time.time() - start_time) * 1000  # ms
        
        # Brief wait for parallel processing to establish Sacred Pause status
        time.sleep(0.02)  # 20ms for parallel threads
        
        # Check console for Sacred Pause status
        console_view = self.tml_engine.console.get_view(tml_handle['request_id'])
        
        # Package result
        result = {
            'scenario_id': scenario.scenario_id,
            'recommended_action': decision,
            'decision_time_ms': decision_time,
            'tml_tracking': tml_handle['request_id'],
            'sacred_pause_engaged': console_view.get('sa_tick') is not None,
            'risk_assessment': {
                'final_risk': console_view.get('current_risk', 0),
                'risk_curve': console_view.get('risk_curve', []),
                'status': console_view.get('status', 'unknown')
            },
            'timestamp': datetime.now().isoformat()
        }
        
        # Add moral trace details if Sacred Pause triggered
        if result['sacred_pause_engaged']:
            result['moral_trace'] = {
                'static_anchor': console_view.get('sa_tick'),
                'reason': 'Framework detected moral complexity in vehicle decision',
                'alternatives_considered': [a.value for a in ActionType],
                'stakeholders_affected': len(context['stakeholders']),
                'protected_populations': self._identify_protected(scenario)
            }
        
        self.decision_log.append(result)
        return result
    
    def _build_context(self, scenario: Scenario) -> Dict[str, Any]:
        """Build context for TML evaluation"""
        stakeholders = []
        
        # Add passengers
        for person in scenario.passengers:
            stakeholders.append({
                'id': f'passenger_{person.person_type.value}',
                'harm_type': 'physical',
                'count': person.quantity,
                'protected': person.person_type in [PersonType.CHILD, PersonType.ELDERLY]
            })
        
        # Add potential victims in each path
        for path_people, path_name in [
            (scenario.path_straight, 'straight'),
            (scenario.path_left, 'left'),
            (scenario.path_right, 'right')
        ]:
            for person in path_people:
                stakeholders.append({
                    'id': f'{path_name}_{person.person_type.value}',
                    'harm_type': 'physical',
                    'count': person.quantity,
                    'compliance': person.compliance
                })
        
        # Determine protected populations
        all_people = (scenario.passengers + scenario.path_straight + 
                     scenario.path_left + scenario.path_right)
        
        has_minors = any(p.person_type == PersonType.CHILD for p in all_people)
        has_elderly = any(p.person_type == PersonType.ELDERLY for p in all_people)
        has_disabled = any(p.person_type == PersonType.DISABLED for p in all_people)
        
        # Calculate decision confidence
        time_pressure = 1.0 - (scenario.time_to_impact / 5.0)  # More pressure = less confidence
        confidence = max(0.3, 1.0 - time_pressure * 0.5)
        
        return {
            'stakeholders': stakeholders,
            'affects_minors': has_minors,
            'affects_elderly': has_elderly,
            'affects_disabled': has_disabled,
            'confidence': confidence,
            'uncertainty': time_pressure,
            'features': {
                'vehicle_speed': scenario.vehicle_speed,
                'time_to_impact': scenario.time_to_impact,
                'total_at_risk': len(stakeholders),
                'paths_blocked': sum([
                    len(scenario.path_straight) > 0,
                    len(scenario.path_left) > 0,
                    len(scenario.path_right) > 0
                ])
            }
        }
    
    def _compute_optimal_action(self, scenario: Scenario) -> ActionType:
        """
        Compute optimal action using utilitarian calculus.
        This happens IMMEDIATELY, not delayed by logging.
        """
        harm_scores = {}
        
        # Calculate harm for each action
        harm_scores[ActionType.CONTINUE_STRAIGHT] = self._calculate_harm(
            scenario.path_straight
        )
        harm_scores[ActionType.SWERVE_LEFT] = self._calculate_harm(
            scenario.path_left
        )
        harm_scores[ActionType.SWERVE_RIGHT] = self._calculate_harm(
            scenario.path_right
        )
        
        # Emergency brake might still hit straight path but with less force
        harm_scores[ActionType.EMERGENCY_BRAKE] = self._calculate_harm(
            scenario.path_straight
        ) * 0.6
        
        # Choose action with minimum harm
        return min(harm_scores, key=harm_scores.get)
    
    def _calculate_harm(self, people: List[Person]) -> float:
        """Calculate total harm score for hitting these people"""
        total_harm = 0
        
        for person in people:
            base_harm = person.quantity
            
            # Adjust for vulnerability
            if person.person_type == PersonType.CHILD:
                base_harm *= 1.5
            elif person.person_type == PersonType.ELDERLY:
                base_harm *= 1.3
            elif person.person_type == PersonType.PREGNANT_WOMAN:
                base_harm *= 1.4
            elif person.person_type == PersonType.DISABLED:
                base_harm *= 1.3
                
            # Slight adjustment for rule compliance
            if person.compliance == "jaywalking":
                base_harm *= 0.9
                
            total_harm += base_harm
            
        return total_harm
    
    def _identify_protected(self, scenario: Scenario) -> List[str]:
        """Identify protected populations in scenario"""
        protected = []
        all_people = (scenario.passengers + scenario.path_straight + 
                     scenario.path_left + scenario.path_right)
        
        if any(p.person_type == PersonType.CHILD for p in all_people):
            protected.append("children")
        if any(p.person_type == PersonType.ELDERLY for p in all_people):
            protected.append("elderly")
        if any(p.person_type == PersonType.DISABLED for p in all_people):
            protected.append("disabled")
        if any(p.person_type == PersonType.PREGNANT_WOMAN for p in all_people):
            protected.append("pregnant women")
            
        return protected
    
    def export_decisions(self, filename: str):
        """Export decision log for analysis"""
        with open(filename, 'w') as f:
            json.dump(self.decision_log, f, indent=2, default=str)


def demo_autonomous_vehicle():
    """Demonstrate AV ethics with framework-enforced Sacred Pause"""
    
    print("=" * 60)
    print("Autonomous Vehicle Ethics - Dual-Layer SPRL")
    print("Framework threshold for AV domain: 0.10 (lowest)")
    print("=" * 60)
    
    ethics_system = AutonomousVehicleEthics()
    
    # Scenario 1: Simple case
    print("\nScenario 1: Single Pedestrian")
    print("-" * 40)
    
    simple_scenario = Scenario(
        scenario_id="AV001",
        description="Single pedestrian crossing",
        passengers=[Person(PersonType.ADULT, 35, 1)],
        path_straight=[Person(PersonType.ADULT, 40, 1, "jaywalking")],
        path_left=[],
        path_right=[],  # Wall
        vehicle_speed=40,
        time_to_impact=2.0
    )
    
    result1 = ethics_system.make_moral_decision(simple_scenario)
    print(f"Decision: {result1['recommended_action'].value}")
    print(f"Decision time: {result1['decision_time_ms']:.1f}ms")
    print(f"Sacred Pause: {result1['sacred_pause_engaged']}")
    
    # Scenario 2: Complex trolley problem
    print("\nScenario 2: Classic Trolley Problem")
    print("-" * 40)
    
    trolley_scenario = Scenario(
        scenario_id="AV002",
        description="Multiple pedestrians vs single child",
        passengers=[Person(PersonType.ADULT, 35, 2)],
        path_straight=[
            Person(PersonType.ADULT, 30, 1),
            Person(PersonType.ADULT, 45, 1),
            Person(PersonType.ADULT, 25, 1)
        ],
        path_left=[Person(PersonType.CHILD, 8, 1, "following_rules")],
        path_right=[],  # Concrete barrier
        vehicle_speed=60,
        time_to_impact=1.2
    )
    
    result2 = ethics_system.make_moral_decision(trolley_scenario)
    print(f"Decision: {result2['recommended_action'].value}")
    print(f"Decision time: {result2['decision_time_ms']:.1f}ms")
    print(f"Sacred Pause: {result2['sacred_pause_engaged']}")
    
    if result2['sacred_pause_engaged']:
        print(f"\nMoral Trace Generated:")
        print(f"- Static Anchor: {result2['moral_trace']['static_anchor']}")
        print(f"- Protected populations: {result2['moral_trace']['protected_populations']}")
        print(f"- Stakeholders affected: {result2['moral_trace']['stakeholders_affected']}")
    
    # Export audit trail
    ethics_system.export_decisions("av_decisions_audit.json")
    print(f"\nAudit trail exported to: av_decisions_audit.json")
    
    print("\nKey Points:")
    print("• AV domain uses lowest framework threshold (0.10)")
    print("• Decisions execute in milliseconds (no delay)")
    print("• Sacred Pause logs moral complexity in parallel")
    print("• Every morally complex decision has audit trail")


if __name__ == "__main__":
    demo_autonomous_vehicle()
