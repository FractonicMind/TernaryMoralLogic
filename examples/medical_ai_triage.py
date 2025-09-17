"""
Medical AI Triage System - TML Framework with Dual-Layer SPRL
=============================================================

Demonstrates framework-enforced Sacred Pause in healthcare contexts.
No configurable thresholds - the framework determines when medical
decisions involve moral complexity requiring enhanced logging.

Created by: Lev Goukassian (ORCID: 0009-0006-5966-1243)
Repository: https://github.com/FractonicMind/TernaryMoralLogic
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from datetime import datetime
import json
import time

from tml import (
    TMLEngine,
    TMLState,
    dynamic_sprl,
    create_tml_engine
)

@dataclass
class Patient:
    """Patient requiring triage"""
    patient_id: str
    name: str
    age: int
    condition: str
    urgency_score: float  # 0-1 scale
    survival_probability: float  # 0-1 scale
    estimated_resources: int  # Resource units needed
    insurance_status: bool
    dependents: int


class MedicalTriageSystem:
    """
    Medical triage system with framework-enforced Sacred Pause.
    Healthcare domain automatically uses lower Sacred Pause threshold (0.15).
    """
    
    def __init__(self):
        # Healthcare domain gets special framework thresholds
        self.tml_engine = create_tml_engine(domain="healthcare", region="US")
        self.decision_log = []
        
    def evaluate_resource_allocation(self, 
                                    patients: List[Patient], 
                                    available_resources: int) -> Dict[str, Any]:
        """
        Evaluate resource allocation with automatic Sacred Pause.
        Framework determines when moral complexity exists.
        """
        # Build context for TML evaluation
        context = self._build_context(patients, available_resources)
        
        # Process decision - executes immediately
        # Logging happens in parallel if Sacred Pause triggered
        prompt = f"Allocate {available_resources} resources among {len(patients)} patients"
        
        tml_result = self.tml_engine.process_decision(prompt, context)
        
        # Make actual allocation (not delayed by logging)
        allocation = self._perform_allocation(patients, available_resources)
        
        # Check console for Sacred Pause status (after brief parallel processing)
        time.sleep(0.1)
        console_view = self.tml_engine.console.get_view(tml_result['request_id'])
        
        # Package result
        result = {
            'allocation': allocation,
            'tml_tracking': tml_result['request_id'],
            'sacred_pause_triggered': console_view.get('sa_tick') is not None,
            'risk_curve': console_view.get('risk_curve', []),
            'moral_complexity': self._assess_complexity(console_view),
            'timestamp': datetime.now().isoformat()
        }
        
        # Add justification if Sacred Pause was triggered
        if result['sacred_pause_triggered']:
            result['enhanced_logging'] = {
                'reason': 'Framework detected moral complexity in medical decision',
                'factors': self._extract_complexity_factors(context),
                'static_anchor': console_view.get('sa_tick'),
                'alternatives_logged': True
            }
        
        self.decision_log.append(result)
        return result
    
    def _build_context(self, patients: List[Patient], resources: int) -> Dict[str, Any]:
        """Build context for TML evaluation"""
        stakeholders = []
        for patient in patients:
            stakeholders.append({
                'id': patient.patient_id,
                'harm_type': 'physical',
                'severity': 1.0 - patient.survival_probability,
                'urgency': patient.urgency_score
            })
            
            # Add dependents as stakeholders
            if patient.dependents > 0:
                stakeholders.append({
                    'id': f"{patient.patient_id}_dependents",
                    'harm_type': 'psychological',
                    'count': patient.dependents
                })
        
        # Check for protected populations
        has_minors = any(p.age < 18 for p in patients)
        has_elderly = any(p.age > 65 for p in patients)
        
        # Calculate confidence based on data quality
        confidence = min(p.survival_probability for p in patients)
        uncertainty = 1.0 - confidence if len(patients) > 3 else 0.3
        
        return {
            'stakeholders': stakeholders,
            'affects_minors': has_minors,
            'affects_elderly': has_elderly,
            'confidence': confidence,
            'uncertainty': uncertainty,
            'resource_scarcity': resources / sum(p.estimated_resources for p in patients),
            'features': {
                'patient_count': len(patients),
                'resource_deficit': max(0, sum(p.estimated_resources for p in patients) - resources),
                'mortality_risk': any(p.survival_probability < 0.5 for p in patients),
                'triage_complexity': len(patients) * (1.0 - resources/100)
            }
        }
    
    def _perform_allocation(self, patients: List[Patient], resources: int) -> Dict[str, int]:
        """
        Perform actual resource allocation.
        This happens immediately, not delayed by Sacred Pause.
        """
        allocation = {}
        remaining = resources
        
        # Sort by combined score (urgency * survival probability)
        sorted_patients = sorted(
            patients,
            key=lambda p: p.urgency_score * p.survival_probability,
            reverse=True
        )
        
        for patient in sorted_patients:
            if remaining >= patient.estimated_resources:
                allocation[patient.patient_id] = patient.estimated_resources
                remaining -= patient.estimated_resources
            elif remaining > 0:
                allocation[patient.patient_id] = remaining
                remaining = 0
            else:
                allocation[patient.patient_id] = 0
                
        return allocation
    
    def _assess_complexity(self, console_view: Dict) -> str:
        """Assess moral complexity level from console data"""
        if console_view.get('status') == 'prohibit':
            return 'UNACCEPTABLE'
        elif console_view.get('sa_tick'):
            return 'HIGH'
        elif len(console_view.get('risk_curve', [])) > 5:
            return 'MODERATE'
        else:
            return 'LOW'
    
    def _extract_complexity_factors(self, context: Dict) -> List[str]:
        """Extract factors contributing to moral complexity"""
        factors = []
        
        if context.get('affects_minors'):
            factors.append('Pediatric patients involved')
        if context.get('affects_elderly'):
            factors.append('Elderly patients involved')
        if context.get('resource_scarcity', 1.0) < 0.5:
            factors.append('Severe resource scarcity')
        if context.get('uncertainty', 0) > 0.5:
            factors.append('High medical uncertainty')
        if context['features'].get('mortality_risk'):
            factors.append('Life-threatening conditions')
            
        return factors
    
    def export_decisions(self, filename: str):
        """Export decision log for audit"""
        with open(filename, 'w') as f:
            json.dump(self.decision_log, f, indent=2, default=str)


def demo_medical_triage():
    """Demonstrate medical triage with framework-enforced Sacred Pause"""
    
    print("=" * 60)
    print("Medical AI Triage - Dual-Layer SPRL")
    print("Framework-enforced Sacred Pause for healthcare")
    print("=" * 60)
    
    triage_system = MedicalTriageSystem()
    
    # Scenario 1: Simple triage (unlikely to trigger Sacred Pause)
    print("\nScenario 1: Routine Emergency Department")
    print("-" * 40)
    
    simple_patients = [
        Patient("P001", "Alice Johnson", 45, "Pneumonia", 0.6, 0.85, 50, True, 2),
        Patient("P002", "Bob Smith", 70, "Dehydration", 0.4, 0.95, 30, True, 0)
    ]
    
    result1 = triage_system.evaluate_resource_allocation(simple_patients, 100)
    print(f"Allocation made: {len(result1['allocation'])} patients")
    print(f"Sacred Pause triggered: {result1['sacred_pause_triggered']}")
    print(f"Moral complexity: {result1['moral_complexity']}")
    
    # Scenario 2: Complex case (framework will likely trigger Sacred Pause)
    print("\nScenario 2: Mass Casualty with Resource Scarcity")
    print("-" * 40)
    
    complex_patients = [
        Patient("P003", "Emma Wilson", 8, "Severe trauma", 0.9, 0.60, 120, True, 0),
        Patient("P004", "Frank Davis", 35, "Organ failure", 0.85, 0.40, 150, True, 3),
        Patient("P005", "Grace Chen", 72, "Stroke", 0.7, 0.30, 80, True, 1),
        Patient("P006", "Henry Brown", 28, "Multiple injuries", 0.95, 0.80, 100, True, 2),
        Patient("P007", "Infant Doe", 1, "Respiratory failure", 1.0, 0.70, 60, False, 0)
    ]
    
    result2 = triage_system.evaluate_resource_allocation(complex_patients, 200)
    print(f"Allocation made: {len(result2['allocation'])} patients")
    print(f"Sacred Pause triggered: {result2['sacred_pause_triggered']}")
    print(f"Moral complexity: {result2['moral_complexity']}")
    
    if result2['sacred_pause_triggered']:
        print(f"\nSacred Pause Details:")
        print(f"- Static Anchor: {result2['enhanced_logging']['static_anchor']}")
        print(f"- Complexity factors:")
        for factor in result2['enhanced_logging']['factors']:
            print(f"  • {factor}")
    
    # Export for audit
    triage_system.export_decisions("medical_triage_audit.json")
    print(f"\nAudit trail exported to: medical_triage_audit.json")
    
    print("\nKey Points:")
    print("• Healthcare domain uses framework-set threshold (0.15)")
    print("• Sacred Pause triggers automatically for complex cases")
    print("• Decisions execute immediately (no delay)")
    print("• Comprehensive logging happens in parallel")
    print("• Audit trail proves ethical consideration")


@dynamic_sprl(domain="healthcare")
def quick_triage_decision(patient_data: dict, context: dict) -> dict:
    """
    Example using decorator pattern for quick integration.
    Sacred Pause handled automatically by framework.
    """
    # Your triage logic here
    decision = {
        'patient_id': patient_data['id'],
        'priority': 'urgent' if context.get('affects_minors') else 'standard',
        'resources_allocated': patient_data.get('resources', 50)
    }
    
    # Decision returns immediately
    # TML tracking attached automatically
    return decision


if __name__ == "__main__":
    demo_medical_triage()
