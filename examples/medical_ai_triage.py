"""
Medical AI Triage System TML Implementation Example

Demonstrates how a medical triage AI MIGHT implement TML for patient
care decisions. All thresholds are EXAMPLES ONLY. Healthcare organizations
must determine appropriate values based on medical standards and regulations.

DISCLAIMER: This is not medical software. Do not use for actual healthcare.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from implementations.python_library import create_tml_framework, ComplianceChecker
import random
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional


class TriagePriority:
    """Standard emergency department triage categories (example)"""
    IMMEDIATE = 1    # Life-threatening, immediate care needed
    EMERGENT = 2     # Could become life-threatening
    URGENT = 3       # Serious but stable
    LESS_URGENT = 4  # Stable, can wait
    NON_URGENT = 5   # Minor issues


class MedicalAITriage:
    """
    EXAMPLE medical triage AI with TML integration.
    
    Real medical systems require regulatory approval, clinical validation,
    and extensive safety testing. This is for demonstration only.
    """
    
    def __init__(self):
        # EXAMPLE CONFIGURATION - NOT FOR CLINICAL USE
        self.framework = create_tml_framework(
            sprl_threshold=0.3,  # EXAMPLE: Lower threshold for patient safety
            domain="medical",
            calculate_risk_on="all",  # Evaluate all patient decisions
            retention_days=3650  # 10 years per medical record requirements
        )
        
        print("=" * 70)
        print("MEDICAL AI TRIAGE TML EXAMPLE")
        print("=" * 70)
        print()
        print("⚠️  CRITICAL DISCLAIMER:")
        print("This is a demonstration only. NOT for clinical use.")
        print("Real medical AI requires regulatory approval and clinical validation.")
        print()
        print("Example Configuration:")
        print(f"  SPRL Threshold: {self.framework.sprl_threshold} (example only)")
        print(f"  Retention: 10 years (medical record requirement)")
        print(f"  Enhanced logging for vulnerable populations")
        print()
    
    def assess_patient_risk(self, patient: Dict) -> float:
        """
        EXAMPLE risk assessment for medical triage.
        
        Real systems would use validated clinical scoring systems,
        evidence-based protocols, and physician oversight.
        """
        risk_score = 0.0
        
        # Vital signs (simplified example)
        vitals = patient.get('vitals', {})
        
        # Blood pressure
        systolic = vitals.get('systolic_bp', 120)
        if systolic < 90 or systolic > 180:
            risk_score += 0.4
        elif systolic < 100 or systolic > 160:
            risk_score += 0.2
        
        # Heart rate
        heart_rate = vitals.get('heart_rate', 75)
        if heart_rate < 50 or heart_rate > 120:
            risk_score += 0.3
        elif heart_rate < 60 or heart_rate > 100:
            risk_score += 0.1
        
        # Respiratory rate
        resp_rate = vitals.get('respiratory_rate', 16)
        if resp_rate < 10 or resp_rate > 30:
            risk_score += 0.4
        elif resp_rate < 12 or resp_rate > 24:
            risk_score += 0.2
        
        # Temperature
        temp_c = vitals.get('temperature_c', 37.0)
        if temp_c < 35 or temp_c > 39:
            risk_score += 0.3
        elif temp_c < 36 or temp_c > 38:
            risk_score += 0.1
        
        # Chief complaint severity (example categories)
        complaint = patient.get('chief_complaint', {})
        if complaint.get('chest_pain'):
            risk_score += 0.5
        if complaint.get('difficulty_breathing'):
            risk_score += 0.5
        if complaint.get('altered_mental_status'):
            risk_score += 0.6
        if complaint.get('severe_bleeding'):
            risk_score += 0.7
        if complaint.get('stroke_symptoms'):
            risk_score += 0.8
        
        # Patient factors
        if patient.get('age', 40) < 2:
            risk_score += 0.4  # Infant
        elif patient.get('age', 40) < 18:
            risk_score += 0.2  # Minor
        elif patient.get('age', 40) > 65:
            risk_score += 0.3  # Elderly
        
        # Comorbidities (example)
        conditions = patient.get('medical_history', [])
        if 'heart_disease' in conditions:
            risk_score += 0.2
        if 'diabetes' in conditions:
            risk_score += 0.1
        if 'immunocompromised' in conditions:
            risk_score += 0.3
        
        return min(risk_score, 1.0)
    
    def triage_patient(self, patient: Dict) -> Dict:
        """
        Process triage decision with TML logging for accountability.
        """
        # Calculate medical risk
        patient['calculated_risk'] = self.assess_patient_risk(patient)
        
        # Identify if vulnerable population
        patient['affects_minors'] = patient.get('age', 40) < 18
        patient['elderly'] = patient.get('age', 40) > 65
        patient['disability'] = any(
            cond in patient.get('medical_history', [])
            for cond in ['cognitive_impairment', 'developmental_disability']
        )
        
        # Enhanced context for medical decisions
        patient['medical_decision'] = True
        patient['irreversible'] = False  # Triage can be re-evaluated
        patient['time_sensitive'] = patient['calculated_risk'] > 0.6
        
        # Triage decision logic (simplified example)
        def medical_triage_logic(context):
            risk = context['calculated_risk']
            
            if risk > 0.8:
                priority = TriagePriority.IMMEDIATE
                reason = "Life-threatening condition detected"
                wait_time = "Immediate"
            elif risk > 0.6:
                priority = TriagePriority.EMERGENT
                reason = "Potentially life-threatening"
                wait_time = "< 15 minutes"
            elif risk > 0.4:
                priority = TriagePriority.URGENT
                reason = "Serious but stable condition"
                wait_time = "< 60 minutes"
            elif risk > 0.2:
                priority = TriagePriority.LESS_URGENT
                reason = "Stable condition"
                wait_time = "< 120 minutes"
            else:
                priority = TriagePriority.NON_URGENT
                reason = "Minor condition"
                wait_time = "< 240 minutes"
            
            return {
                'triage_priority': priority,
                'reason': reason,
                'estimated_wait': wait_time,
                'requires_reassessment': risk > 0.4,
                'physician_notification': risk > 0.6
            }
        
        # Process with TML
        result = self.framework.process_decision(
            context=patient,
            ai_decision_func=medical_triage_logic
        )
        
        return result
    
    def simulate_emergency_department(self):
        """Simulate ED triage scenarios."""
        
        print("SIMULATING EMERGENCY DEPARTMENT TRIAGE")
        print("-" * 70)
        print()
        
        # Generate example patients
        patients = [
            {
                'patient_id': 'PT-001',
                'age': 67,
                'chief_complaint': {'chest_pain': True, 'radiating': True},
                'vitals': {
                    'systolic_bp': 160,
                    'heart_rate': 110,
                    'respiratory_rate': 22,
                    'temperature_c': 37.2
                },
                'medical_history': ['heart_disease', 'hypertension'],
                'arrival_time': '14:23'
            },
            {
                'patient_id': 'PT-002',
                'age': 8,
                'chief_complaint': {'fever': True, 'lethargy': True},
                'vitals': {
                    'systolic_bp': 95,
                    'heart_rate': 140,
                    'respiratory_rate': 28,
                    'temperature_c': 39.5
                },
                'medical_history': [],
                'arrival_time': '14:35'
            },
            {
                'patient_id': 'PT-003',
                'age': 35,
                'chief_complaint': {'ankle_injury': True},
                'vitals': {
                    'systolic_bp': 125,
                    'heart_rate': 72,
                    'respiratory_rate': 16,
                    'temperature_c': 37.0
                },
                'medical_history': [],
                'arrival_time': '14:40'
            },
            {
                'patient_id': 'PT-004',
                'age': 82,
                'chief_complaint': {'difficulty_breathing': True, 'confusion': True},
                'vitals': {
                    'systolic_bp': 85,
                    'heart_rate': 125,
                    'respiratory_rate': 32,
                    'temperature_c': 38.2
                },
                'medical_history': ['copd', 'diabetes', 'cognitive_impairment'],
                'arrival_time': '14:42'
            },
            {
                'patient_id': 'PT-005',
                'age': 22,
                'chief_complaint': {'headache': True},
                'vitals': {
                    'systolic_bp': 118,
                    'heart_rate': 68,
                    'respiratory_rate': 14,
                    'temperature_c': 36.8
                },
                'medical_history': ['migraines'],
                'arrival_time': '14:45'
            }
        ]
        
        priority_names = {
            1: "IMMEDIATE",
            2: "EMERGENT",
            3: "URGENT",
            4: "LESS URGENT",
            5: "NON-URGENT"
        }
        
        for patient in patients:
            print(f"Patient: {patient['patient_id']}")
            print(f"  Age: {patient['age']} years")
            print(f"  Chief Complaint: {list(patient['chief_complaint'].keys())}")
            print(f"  Arrival: {patient['arrival_time']}")
            
            result = self.triage_patient(patient)
            decision = result['decision']
            
            print(f"  Triage Priority: {priority_names[decision['triage_priority']]}")
            print(f"  Reason: {decision['reason']}")
            print(f"  Wait Time: {decision['estimated_wait']}")
            print(f"  Risk Score: {patient['calculated_risk']:.2f}")
            print(f"  SPRL Score: {result['sprl_score']:.2f}")
            
            if result['sacred_pause_triggered']:
                print(f"  ✓ Medical decision logged for accountability")
                print(f"    Log Hash: {result['storage_hash'][:12]}...")
                if patient.get('affects_minors'):
                    print(f"    📋 Enhanced logging: Pediatric patient")
                if patient.get('elderly'):
                    print(f"    📋 Enhanced logging: Elderly patient")
                if patient.get('disability'):
                    print(f"    📋 Enhanced logging: Cognitive impairment")
            else:
                print(f"  - Below logging threshold")
            
            if decision.get('physician_notification'):
                print(f"  🚨 Physician notified immediately")
            
            print()
        
        self.display_clinical_metrics()
    
    def display_clinical_metrics(self):
        """Display clinical decision metrics."""
        
        print("=" * 70)
        print("CLINICAL DECISION METRICS")
        print("=" * 70)
        
        stats = self.framework.get_performance_report()
        
        print(f"Total Triage Decisions: {stats['total_decisions']}")
        print(f"Logged Decisions: {stats['sacred_pause_triggers']}")
        print(f"Logging Rate: {stats['trigger_rate']:.1f}%")
        print()
        
        # Medical-specific guidance
        print("CALIBRATION CONSIDERATIONS FOR MEDICAL AI:")
        print()
        
        if stats['trigger_rate'] < 10:
            print("⚠️  Low logging rate for medical decisions")
            print("  - May miss important clinical decisions")
            print("  - Consider if threshold captures sufficient cases")
            print("  - Review against clinical safety standards")
        elif stats['trigger_rate'] > 70:
            print("⚠️  Very high logging rate")
            print("  - May be logging routine decisions")
            print("  - Consider if threshold is too conservative")
            print("  - Balance accountability with efficiency")
        else:
            print("✓ Logging rate within expected range")
            print("  - Continue monitoring for edge cases")
            print("  - Regularly review against patient outcomes")
        
        print()
        print("VULNERABLE POPULATION CONSIDERATIONS:")
        print("- Pediatric patients receive enhanced documentation")
        print("- Elderly patients get additional safeguards")
        print("- Patients with disabilities have specialized protocols")
        print()
    
    def demonstrate_clinical_audit(self):
        """Demonstrate clinical audit and investigation."""
        
        print("=" * 70)
        print("CLINICAL AUDIT DEMONSTRATION")
        print("=" * 70)
        print()
        
        print("Scenario: Monthly quality assurance review")
        print()
        
        # Request logs for audit
        audit_request = {
            'id': 'AUDIT-MED-2025-08',
            'timeframe': (
                datetime.now().strftime("%Y-%m-01T00:00:00"),
                datetime.now().strftime("%Y-%m-%dT23:59:59")
            ),
            'purpose': 'Quality assurance and outcome review'
        }
        
        # Hospital quality committee requests access
        audit_package = self.framework.provide_investigation_access(
            institution='un_human_rights',  # Example medical oversight
            incident=audit_request
        )
        
        if audit_package:
            print("Audit Package Generated:")
            print(f"  Period: Current month")
            print(f"  Decisions Logged: {audit_package['log_count']}")
            print(f"  Integrity Verified: {audit_package['integrity_verified']}")
            print()
            print("Clinical review can analyze:")
            print("  - Triage accuracy vs. final diagnoses")
            print("  - Time to treatment for critical cases")
            print("  - Equity across patient demographics")
            print("  - Protocol adherence and variations")
            print("  - Opportunities for improvement")
            print()
            print("This enables evidence-based quality improvement")
            print("while maintaining patient privacy through anonymization.")
        
        print()
    
    def demonstrate_adverse_event_investigation(self):
        """Show how TML helps investigate adverse events."""
        
        print("=" * 70)
        print("ADVERSE EVENT INVESTIGATION")
        print("=" * 70)
        print()
        
        print("Scenario: Patient had adverse outcome, investigating triage decision")
        print()
        
        # Specific patient investigation
        investigation = {
            'id': 'AE-2025-001',
            'decision_id': 'PT-004',  # The elderly patient with breathing difficulty
            'timeframe': (
                (datetime.now() - timedelta(hours=24)).isoformat(),
                datetime.now().isoformat()
            ),
            'description': 'Delayed recognition of sepsis'
        }
        
        print("Investigation findings from TML logs:")
        print("  ✓ Initial triage priority: IMMEDIATE")
        print("  ✓ Risk factors identified: Age, COPD, confusion")
        print("  ✓ Enhanced logging present: Elderly + disability")
        print("  ✓ Physician notification: Triggered")
        print("  ✓ Alternative priorities considered: Yes")
        print()
        print("TML logs demonstrate:")
        print("  - AI correctly identified high risk")
        print("  - Appropriate priority was assigned")
        print("  - Vulnerable population protocols followed")
        print("  - Issue was in post-triage care, not AI decision")
        print()
        print("This accountability protects both patients and providers")
        print("by creating clear evidence of decision-making process.")
        print()


def main():
    """Run medical AI triage demonstration."""
    
    # Create example medical AI system
    medical_ai = MedicalAITriage()
    
    # Simulate ED triage
    medical_ai.simulate_emergency_department()
    
    # Demonstrate audit capabilities
    medical_ai.demonstrate_clinical_audit()
    
    # Show adverse event investigation
    medical_ai.demonstrate_adverse_event_investigation()
    
    # Compliance check
    print("=" * 70)
    print("MEDICAL AI COMPLIANCE CHECK")
    print("=" * 70)
    
    compliance = ComplianceChecker.check_framework(medical_ai.framework)
    
    print(f"Infrastructure Compliant: {compliance['infrastructure_compliant']}")
    if compliance['issues']:
        for issue in compliance['issues']:
            print(f"  ✗ {issue}")
    else:
        print("✓ All TML infrastructure requirements met")
    
    print()
    print("=" * 70)
    print("CRITICAL REMINDERS FOR MEDICAL AI")
    print("=" * 70)
    print()
    print("1. This example uses arbitrary thresholds")
    print("2. Real medical AI requires:")
    print("   - Regulatory approval (FDA/CE marking)")
    print("   - Clinical validation studies")
    print("   - Physician oversight protocols")
    print("   - Patient consent procedures")
    print("   - HIPAA/GDPR compliance")
    print()
    print("3. TML provides accountability infrastructure")
    print("4. Healthcare organizations determine clinical thresholds")
    print("5. Enhanced protections for vulnerable populations mandatory")
    print()
    print("Contact Information:")
    print("- Email: leogouk@gmail.com")
    print("- Successor Contact: support@tml-goukassian.org")
    print("- See Succession Charter: /TML-SUCCESSION-CHARTER.md")


if __name__ == "__main__":
    main()
