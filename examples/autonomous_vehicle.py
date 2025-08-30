"""
Autonomous Vehicle TML Implementation Example

Demonstrates how an autonomous vehicle system MIGHT implement TML
for safety-critical decisions. All thresholds and risk calculations
are EXAMPLES ONLY - each manufacturer must determine appropriate values.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from implementations.python_library import create_tml_framework, ComplianceChecker
import random
import time
from enum import Enum
from typing import Dict, List, Tuple


class SafetyLevel(Enum):
    """Example safety classifications - manufacturers define their own"""
    CRITICAL = "critical"  # Immediate safety risk
    HIGH = "high"          # Potential safety impact
    MEDIUM = "medium"      # Comfort/efficiency impact
    LOW = "low"            # Minimal impact


class AutonomousVehicleAI:
    """
    EXAMPLE autonomous vehicle decision system with TML integration.
    
    Real manufacturers would have vastly more sophisticated systems.
    This demonstrates the logging infrastructure, not actual AV logic.
    """
    
    def __init__(self):
        # EXAMPLE CONFIGURATION - NOT FOR REAL USE
        # Manufacturers must determine appropriate thresholds
        self.framework = create_tml_framework(
            sprl_threshold=0.4,  # EXAMPLE: Lower threshold for safety
            domain="autonomous",
            calculate_risk_on="all",  # Evaluate all decisions for safety
            retention_days=3650  # 10 years for accident investigation
        )
        
        print("=" * 70)
        print("AUTONOMOUS VEHICLE TML EXAMPLE")
        print("=" * 70)
        print()
        print("⚠️  WARNING: This is a demonstration only!")
        print("Real autonomous vehicles require rigorous safety engineering.")
        print("Thresholds shown are arbitrary examples.")
        print()
        print(f"Example Configuration:")
        print(f"  SPRL Threshold: {self.framework.sprl_threshold}")
        print(f"  Retention: 10 years (for accident investigation)")
        print(f"  Domain: Autonomous vehicles")
        print()
    
    def calculate_safety_risk(self, scenario: Dict) -> float:
        """
        EXAMPLE risk calculation for autonomous vehicle decisions.
        
        Real systems would use sophisticated sensor fusion,
        predictive modeling, and safety engineering standards.
        """
        base_risk = 0.0
        
        # Speed factor (example)
        speed_kmh = scenario.get('speed_kmh', 0)
        if speed_kmh > 100:
            base_risk += 0.3
        elif speed_kmh > 50:
            base_risk += 0.2
        elif speed_kmh > 30:
            base_risk += 0.1
        
        # Proximity to other objects (example)
        min_distance = scenario.get('min_distance_m', 100)
        if min_distance < 5:
            base_risk += 0.5
        elif min_distance < 10:
            base_risk += 0.3
        elif min_distance < 20:
            base_risk += 0.1
        
        # Environmental conditions (example)
        conditions = scenario.get('conditions', {})
        if conditions.get('heavy_rain'):
            base_risk += 0.2
        if conditions.get('night'):
            base_risk += 0.1
        if conditions.get('construction_zone'):
            base_risk += 0.3
        
        # Vulnerable road users (example)
        if scenario.get('pedestrians_detected'):
            base_risk += 0.4
        if scenario.get('cyclists_detected'):
            base_risk += 0.3
        if scenario.get('school_zone'):
            base_risk += 0.5
        
        return min(base_risk, 1.0)
    
    def make_driving_decision(self, scenario: Dict) -> Dict:
        """
        Process driving decision with TML logging for safety-critical events.
        """
        # Add safety risk calculation to context
        scenario['calculated_risk'] = self.calculate_safety_risk(scenario)
        
        # Identify stakeholders
        stakeholders = []
        if scenario.get('pedestrians_detected'):
            stakeholders.append({'type': 'pedestrian', 'vulnerability': 2.0})
        if scenario.get('cyclists_detected'):
            stakeholders.append({'type': 'cyclist', 'vulnerability': 1.8})
        if scenario.get('other_vehicles'):
            for vehicle in scenario.get('other_vehicles', []):
                stakeholders.append({'type': 'vehicle_occupants', 'vulnerability': 1.2})
        stakeholders.append({'type': 'own_occupants', 'vulnerability': 1.0})
        
        scenario['stakeholders'] = stakeholders
        
        # Example decision logic (simplified)
        def autonomous_decision_logic(context):
            risk = context['calculated_risk']
            
            if risk > 0.8:
                return {
                    'action': 'emergency_stop',
                    'reason': 'critical_safety_risk',
                    'deceleration': 'maximum'
                }
            elif risk > 0.6:
                return {
                    'action': 'slow_down',
                    'reason': 'elevated_risk',
                    'target_speed': max(context['speed_kmh'] * 0.5, 20)
                }
            elif risk > 0.4:
                return {
                    'action': 'increase_following_distance',
                    'reason': 'moderate_risk',
                    'adjustment': '50%'
                }
            else:
                return {
                    'action': 'maintain_course',
                    'reason': 'acceptable_risk',
                    'confidence': 0.95
                }
        
        # Process with TML
        result = self.framework.process_decision(
            context=scenario,
            ai_decision_func=autonomous_decision_logic
        )
        
        return result
    
    def simulate_driving_scenarios(self):
        """Simulate various driving scenarios to demonstrate TML logging."""
        
        scenarios = [
            {
                'name': 'Highway Cruising',
                'speed_kmh': 110,
                'min_distance_m': 50,
                'conditions': {'clear': True},
                'pedestrians_detected': False,
                'cyclists_detected': False,
                'other_vehicles': [{'distance': 50}, {'distance': 75}]
            },
            {
                'name': 'School Zone Approach',
                'speed_kmh': 40,
                'min_distance_m': 30,
                'conditions': {'school_hours': True},
                'school_zone': True,
                'pedestrians_detected': True,
                'cyclists_detected': False,
                'other_vehicles': []
            },
            {
                'name': 'Emergency Braking Event',
                'speed_kmh': 60,
                'min_distance_m': 3,
                'conditions': {'sudden_obstacle': True},
                'pedestrians_detected': False,
                'cyclists_detected': False,
                'other_vehicles': [{'distance': 3, 'sudden_stop': True}]
            },
            {
                'name': 'Rain and Construction',
                'speed_kmh': 45,
                'min_distance_m': 15,
                'conditions': {'heavy_rain': True, 'construction_zone': True},
                'pedestrians_detected': False,
                'cyclists_detected': True,
                'other_vehicles': [{'distance': 15}]
            },
            {
                'name': 'Night Driving - Rural',
                'speed_kmh': 80,
                'min_distance_m': 100,
                'conditions': {'night': True, 'rural': True},
                'pedestrians_detected': False,
                'cyclists_detected': False,
                'other_vehicles': []
            }
        ]
        
        print("SIMULATING DRIVING SCENARIOS")
        print("-" * 70)
        print()
        
        for scenario in scenarios:
            print(f"Scenario: {scenario['name']}")
            print(f"  Speed: {scenario['speed_kmh']} km/h")
            print(f"  Conditions: {scenario['conditions']}")
            
            result = self.make_driving_decision(scenario)
            
            print(f"  Decision: {result['decision']['action']}")
            print(f"  Reason: {result['decision']['reason']}")
            print(f"  Risk Score: {scenario['calculated_risk']:.2f}")
            print(f"  SPRL Score: {result['sprl_score']:.2f}")
            
            if result['sacred_pause_triggered']:
                print(f"  ✓ Safety event logged for investigation")
                print(f"    Log Hash: {result['storage_hash'][:12]}...")
            else:
                print(f"  - Below logging threshold")
            
            print()
        
        # Show statistics
        self.display_safety_metrics()
    
    def display_safety_metrics(self):
        """Display safety and performance metrics."""
        
        print("=" * 70)
        print("SAFETY METRICS AND COMPLIANCE")
        print("=" * 70)
        
        stats = self.framework.get_performance_report()
        
        print(f"Total Decisions: {stats['total_decisions']}")
        print(f"Safety Events Logged: {stats['sacred_pause_triggers']}")
        print(f"Logging Rate: {stats['trigger_rate']:.1f}%")
        print(f"Average Log Time: {stats['average_logging_time_ms']:.1f}ms")
        print()
        
        # Calibration guidance
        if stats['trigger_rate'] < 0.1:
            print("⚠️  CALIBRATION NOTE:")
            print("  Very low logging rate - may miss safety-critical events")
            print("  Consider if threshold is appropriate for safety requirements")
        elif stats['trigger_rate'] > 30:
            print("⚠️  CALIBRATION NOTE:")
            print("  High logging rate - many events being recorded")
            print("  Verify if all logged events are truly safety-relevant")
        else:
            print("✓ Logging rate appears appropriate for safety monitoring")
        
        print()
        
        # Compliance check
        compliance = ComplianceChecker.check_framework(self.framework)
        print(f"Infrastructure Compliant: {compliance['infrastructure_compliant']}")
        
        if not compliance['infrastructure_compliant']:
            print("Issues:")
            for issue in compliance['issues']:
                print(f"  ✗ {issue}")
        
        print()
    
    def demonstrate_investigation_scenario(self):
        """Demonstrate how investigation would work after an incident."""
        
        print("=" * 70)
        print("POST-INCIDENT INVESTIGATION EXAMPLE")
        print("=" * 70)
        print()
        
        print("Scenario: Minor collision occurred, investigating decision logs")
        print()
        
        # Simulate incident investigation request
        incident = {
            'id': 'INC-AV-2025-001',
            'timeframe': (
                time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(time.time() - 7200)),
                time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())
            ),
            'description': 'Minor collision during automated driving'
        }
        
        # Authorized safety board requests logs
        investigation = self.framework.provide_investigation_access(
            institution='ieee_ethics',  # Example safety authority
            incident=incident
        )
        
        if investigation:
            print("Investigation Package Provided:")
            print(f"  Logs Retrieved: {investigation['log_count']}")
            print(f"  Time Period: Last 2 hours")
            print(f"  Integrity Verified: {investigation['integrity_verified']}")
            print()
            print("Safety board can now analyze:")
            print("  - Decision patterns leading to incident")
            print("  - Risk calculations at time of event")
            print("  - Environmental conditions considered")
            print("  - Alternative actions evaluated")
            print()
            print("This enables thorough post-incident analysis without")
            print("interfering with vehicle operation at time of event.")
        
        print()


def main():
    """Run autonomous vehicle TML demonstration."""
    
    # Create example AV system
    av_system = AutonomousVehicleAI()
    
    # Run driving scenarios
    av_system.simulate_driving_scenarios()
    
    # Demonstrate investigation
    av_system.demonstrate_investigation_scenario()
    
    print("=" * 70)
    print("DEMONSTRATION COMPLETE")
    print("=" * 70)
    print()
    print("Key Points for Autonomous Vehicle Manufacturers:")
    print()
    print("1. TML provides logging infrastructure for safety events")
    print("2. Manufacturers determine appropriate risk thresholds")
    print("3. No interference with real-time vehicle operation")
    print("4. Logs preserved for accident investigation")
    print("5. Enables accountability without compromising safety")
    print()
    print("REMINDER: This example uses arbitrary thresholds.")
    print("Real autonomous vehicles require rigorous safety engineering")
    print("and domain-specific risk calibration.")
    print()
    print("Contact Information:")
    print("- Email: leogouk@gmail.com")
    print("- Successor Contact: support@tml-goukassian.org")
    print("- See Succession Charter: /TML-SUCCESSION-CHARTER.md")


if __name__ == "__main__":
    main()
