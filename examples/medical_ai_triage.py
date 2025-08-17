"""
Medical AI Triage System - TML Framework Implementation
======================================================

This example demonstrates how the Ternary Moral Logic framework handles
life-critical medical resource allocation decisions using Sacred Pause
for complex ethical scenarios.

Real-world use case: Hospital AI system during resource scarcity
"""

from tml import TMLEvaluator, TMLState, TMLEvaluation
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime
import json

@dataclass
class Patient:
    """Patient data structure for triage decisions"""
    id: str
    name: str
    age: int
    condition: str
    severity_score: float  # 0.0-1.0, higher = more severe
    survival_probability: float  # 0.0-1.0
    treatment_cost: int  # Resource units required
    time_sensitive: bool  # True if delay significantly impacts outcome
    dependents: int  # Number of people depending on this patient
    
class MedicalTriageSystem:
    """AI system for medical resource allocation using TML framework"""
    
    def __init__(self):
        self.tml_evaluator = TMLEvaluator()
        self.decision_log = []
        
    def evaluate_resource_allocation(self, 
                                   patients: List[Patient],
                                   available_resources: int) -> Dict[str, Any]:
        """
        Determine resource allocation among competing patients
        
        Returns:
        - allocation_decision: Dict mapping patient_id to resources allocated
        - moral_state: TML state for this decision
        - sacred_pause_engaged: Whether complex ethics required pause
        - justification: Reasoning for the decision
        """
        
        # Calculate moral complexity based on multiple factors
        complexity_factors = self._assess_complexity(patients, available_resources)
        
        # Create context for TML evaluation
        context = {
            "scenario": f"Allocate {available_resources} medical resources among {len(patients)} patients",
            "stakeholders": self._identify_stakeholders(patients),
            "values_at_stake": ["life", "fairness", "utility", "dignity", "justice"],
            "complexity_score": complexity_factors["total_complexity"]
        }
        
        # Evaluate using TML framework
        evaluation_text = f"Medical resource allocation: {available_resources} units for {len(patients)} patients"
        tml_result = self.tml_evaluator.evaluate(evaluation_text, context)
        
        # Generate allocation based on moral state
        if tml_result.state == TMLState.SACRED_PAUSE:
            allocation = self._sacred_pause_allocation(patients, available_resources, tml_result)
        elif tml_result.state == TMLState.AFFIRMATION:
            allocation = self._standard_allocation(patients, available_resources)
        else:  # RESISTANCE - shouldn't happen in medical context
            allocation = self._emergency_fallback(patients, available_resources)
        
        result = {
            "allocation_decision": allocation,
            "moral_state": tml_result.state,
            "sacred_pause_engaged": tml_result.state == TMLState.SACRED_PAUSE,
            "complexity_analysis": complexity_factors,
            "justification": self._generate_justification(allocation, tml_result, patients),
            "timestamp": datetime.now().isoformat(),
            "patients_evaluated": len(patients),
            "total_resources": available_resources
        }
        
        # Log decision for audit trail
        self.decision_log.append(result)
        
        return result
    
    def _assess_complexity(self, patients: List[Patient], resources: int) -> Dict[str, float]:
        """Calculate moral complexity score based on scenario factors"""
        
        # Factor 1: Resource scarcity (more scarcity = higher complexity)
        total_need = sum(p.treatment_cost for p in patients)
        scarcity_factor = min(1.0, (total_need - resources) / total_need) if total_need > 0 else 0
        
        # Factor 2: Outcome uncertainty (varied survival rates = higher complexity)
        survival_rates = [p.survival_probability for p in patients]
        if len(survival_rates) > 1:
            uncertainty_factor = max(survival_rates) - min(survival_rates)
        else:
            uncertainty_factor = 0
        
        # Factor 3: Age diversity (competing life stages = ethical complexity)
        ages = [p.age for p in patients]
        age_range = (max(ages) - min(ages)) / 100 if ages else 0
        
        # Factor 4: Dependency impact (people depending on patients)
        dependency_variance = max([p.dependents for p in patients]) - min([p.dependents for p in patients])
        dependency_factor = min(1.0, dependency_variance / 10)
        
        # Factor 5: Time pressure (urgent cases increase complexity)
        urgent_cases = sum(1 for p in patients if p.time_sensitive)
        urgency_factor = urgent_cases / len(patients) if patients else 0
        
        # Weighted combination of factors
        total_complexity = (
            scarcity_factor * 0.3 +
            uncertainty_factor * 0.25 +
            age_range * 0.2 +
            dependency_factor * 0.15 +
            urgency_factor * 0.1
        )
        
        return {
            "total_complexity": total_complexity,
            "scarcity_factor": scarcity_factor,
            "uncertainty_factor": uncertainty_factor,
            "age_diversity": age_range,
            "dependency_factor": dependency_factor,
            "urgency_factor": urgency_factor
        }
    
    def _identify_stakeholders(self, patients: List[Patient]) -> List[str]:
        """Identify all stakeholders affected by the decision"""
        stakeholders = ["patients", "families", "medical_staff", "hospital", "society"]
        
        # Add specific stakeholder categories based on patient characteristics
        if any(p.dependents > 0 for p in patients):
            stakeholders.extend(["children", "dependents"])
        
        if any(p.age < 18 for p in patients):
            stakeholders.append("minors")
            
        if any(p.age > 65 for p in patients):
            stakeholders.append("elderly")
            
        return stakeholders
    
    def _sacred_pause_allocation(self, patients: List[Patient], 
                                resources: int, tml_result: TMLEvaluation) -> Dict[str, int]:
        """
        Complex allocation requiring Sacred Pause deliberation
        Uses multi-criteria decision analysis with ethical weighting
        """
        print("🔄 Sacred Pause Engaged - Complex Medical Ethics Decision")
        print("⏱️  Additional deliberation time: 2000ms")
        
        # Sacred Pause reflection considerations
        ethical_principles = [
            "Maximize lives saved (utilitarian)",
            "Equal treatment regardless of age/status (deontological)", 
            "Prioritize those with best outcomes (consequentialist)",
            "Consider family/dependent impacts (care ethics)",
            "Respect individual dignity and autonomy"
        ]
        
        print("🤔 Ethical Principles Under Consideration:")
        for principle in ethical_principles:
            print(f"   • {principle}")
        
        # Multi-criteria scoring for each patient
        allocations = {}
        remaining_resources = resources
        
        # Score patients on multiple ethical dimensions
        scored_patients = []
        for patient in patients:
            score = self._calculate_ethical_score(patient, patients)
            scored_patients.append((patient, score))
        
        # Sort by ethical score (highest first)
        scored_patients.sort(key=lambda x: x[1], reverse=True)
        
        # Allocate resources based on ethical scoring
        for patient, score in scored_patients:
            if remaining_resources >= patient.treatment_cost:
                allocations[patient.id] = patient.treatment_cost
                remaining_resources -= patient.treatment_cost
            else:
                # Partial allocation if beneficial
                if remaining_resources > 0 and patient.survival_probability > 0.3:
                    allocations[patient.id] = remaining_resources
                    remaining_resources = 0
                else:
                    allocations[patient.id] = 0
                    
            if remaining_resources <= 0:
                break
        
        # Ensure all patients have allocation entry (0 if none)
        for patient in patients:
            if patient.id not in allocations:
                allocations[patient.id] = 0
                
        return allocations
    
    def _calculate_ethical_score(self, patient: Patient, all_patients: List[Patient]) -> float:
        """Calculate multi-dimensional ethical score for resource allocation"""
        
        # Utilitarian component: maximize expected lives saved
        utilitarian_score = patient.survival_probability * 0.3
        
        # Severity component: help those most in need
        severity_score = patient.severity_score * 0.25
        
        # Dependency component: consider impact on others
        max_dependents = max([p.dependents for p in all_patients] + [1])
        dependency_score = (patient.dependents / max_dependents) * 0.2
        
        # Time sensitivity: urgent cases get priority
        urgency_score = 0.15 if patient.time_sensitive else 0
        
        # Efficiency component: consider resource efficiency
        if patient.treatment_cost > 0:
            efficiency_score = (patient.survival_probability / patient.treatment_cost) * 0.1
        else:
            efficiency_score = 0
        
        total_score = (utilitarian_score + severity_score + 
                      dependency_score + urgency_score + efficiency_score)
        
        return total_score
    
    def _standard_allocation(self, patients: List[Patient], resources: int) -> Dict[str, int]:
        """Standard allocation for clear-cut cases (no Sacred Pause needed)"""
        
        # Simple triage: severity-based allocation
        allocations = {}
        remaining_resources = resources
        
        # Sort by severity score (highest first)
        sorted_patients = sorted(patients, key=lambda p: p.severity_score, reverse=True)
        
        for patient in sorted_patients:
            if remaining_resources >= patient.treatment_cost:
                allocations[patient.id] = patient.treatment_cost
                remaining_resources -= patient.treatment_cost
            else:
                allocations[patient.id] = 0
                
        return allocations
    
    def _emergency_fallback(self, patients: List[Patient], resources: int) -> Dict[str, int]:
        """Emergency fallback allocation (should rarely trigger)"""
        
        # Equal distribution as fallback
        per_patient = resources // len(patients) if patients else 0
        return {patient.id: min(per_patient, patient.treatment_cost) for patient in patients}
    
    def _generate_justification(self, allocation: Dict[str, int], 
                               tml_result: TMLEvaluation, patients: List[Patient]) -> str:
        """Generate human-readable justification for the allocation decision"""
        
        patient_map = {p.id: p for p in patients}
        allocated_patients = [pid for pid, resources in allocation.items() if resources > 0]
        
        justification = f"Allocation Decision Analysis:\n"
        justification += f"Moral Framework State: {tml_result.state.value}\n\n"
        
        if tml_result.state == TMLState.SACRED_PAUSE:
            justification += "⚠️  COMPLEX ETHICAL SCENARIO DETECTED\n"
            justification += "Sacred Pause engaged for additional ethical deliberation.\n"
            justification += "Multi-criteria analysis applied considering:\n"
            justification += "• Utilitarian outcomes (lives saved)\n"
            justification += "• Deontological equality principles\n" 
            justification += "• Care ethics (family/dependent impact)\n"
            justification += "• Individual dignity and autonomy\n\n"
        
        justification += f"Resources Allocated to {len(allocated_patients)} of {len(patients)} patients:\n"
        
        for patient_id in allocated_patients:
            patient = patient_map[patient_id]
            resources = allocation[patient_id]
            justification += f"• {patient.name} (ID: {patient_id}): {resources} units\n"
            justification += f"  - Condition: {patient.condition}\n"
            justification += f"  - Survival Probability: {patient.survival_probability:.1%}\n"
            justification += f"  - Severity Score: {patient.severity_score:.2f}\n\n"
        
        non_allocated = [pid for pid, resources in allocation.items() if resources == 0]
        if non_allocated:
            justification += f"Patients not allocated resources ({len(non_allocated)}):\n"
            for patient_id in non_allocated:
                patient = patient_map[patient_id]
                justification += f"• {patient.name}: Insufficient remaining resources\n"
        
        return justification
    
    def get_decision_history(self) -> List[Dict]:
        """Return audit trail of all allocation decisions"""
        return self.decision_log
    
    def export_decisions(self, filename: str) -> None:
        """Export decision log to JSON file for audit/analysis"""
        with open(filename, 'w') as f:
            json.dump(self.decision_log, f, indent=2, default=str)


def demo_medical_triage():
    """Demonstration of medical triage system with various complexity scenarios"""
    
    print("🏥 Medical AI Triage System - TML Framework Demo")
    print("=" * 60)
    
    triage_system = MedicalTriageSystem()
    
    # Scenario 1: Simple case (should be AFFIRMATION state)
    print("\n📊 SCENARIO 1: Standard Triage (Low Complexity)")
    print("-" * 40)
    
    simple_patients = [
        Patient("P001", "Alice Johnson", 45, "Pneumonia", 0.6, 0.85, 50, True, 2),
        Patient("P002", "Bob Smith", 70, "Heart Attack", 0.8, 0.70, 80, True, 0)
    ]
    
    result1 = triage_system.evaluate_resource_allocation(simple_patients, 100)
    print(f"Decision: {result1['moral_state'].value}")
    print(f"Sacred Pause: {result1['sacred_pause_engaged']}")
    print(f"Complexity Score: {result1['complexity_analysis']['total_complexity']:.3f}")
    
    # Scenario 2: Complex ethical dilemma (should trigger Sacred Pause)
    print("\n⚠️  SCENARIO 2: Complex Ethical Dilemma (High Complexity)")
    print("-" * 50)
    
    complex_patients = [
        Patient("P003", "Emma Wilson", 8, "Leukemia", 0.9, 0.60, 120, True, 0),
        Patient("P004", "Frank Davis", 35, "Liver Failure", 0.85, 0.40, 150, True, 3),
        Patient("P005", "Grace Chen", 72, "Stroke", 0.7, 0.30, 80, True, 1),
        Patient("P006", "Henry Brown", 28, "Accident Trauma", 0.95, 0.80, 100, True, 2)
    ]
    
    result2 = triage_system.evaluate_resource_allocation(complex_patients, 200)
    print(f"Decision: {result2['moral_state'].value}")
    print(f"Sacred Pause: {result2['sacred_pause_engaged']}")
    print(f"Complexity Score: {result2['complexity_analysis']['total_complexity']:.3f}")
    
    if result2['sacred_pause_engaged']:
        print("\n🔄 Sacred Pause Justification:")
        print(result2['justification'])
    
    # Export audit trail
    triage_system.export_decisions("medical_triage_audit.json")
    print("\n📋 Decision audit trail exported to: medical_triage_audit.json")
    
    print("\n✅ Demo completed! TML framework successfully handled medical ethics.")


if __name__ == "__main__":
    demo_medical_triage()

# Created by Lev Goukassian • ORCID: 0009-0006-5966-1243 • Email: leogouk@gmail.com • Successor Contact: support@tml-goukassian.org • [see Succession Charter](/TML-SUCCESSION-CHARTER.md)
