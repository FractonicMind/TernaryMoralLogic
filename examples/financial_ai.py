"""
Financial AI Ethics System - TML Framework Implementation
========================================================

This example demonstrates how the Ternary Moral Logic framework handles
complex financial decisions using Sacred Pause for ethically sensitive
scenarios involving bias, fairness, and regulatory compliance.

Real-world use cases: Investment decisions, loan approvals, risk assessment
"""

from tml import TMLEvaluator, TMLState, TMLEvaluation
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import json

class FinancialService(Enum):
    """Types of financial services"""
    LOAN_APPROVAL = "loan_approval"
    INVESTMENT_ADVICE = "investment_advice"
    INSURANCE_PRICING = "insurance_pricing"
    CREDIT_SCORING = "credit_scoring"
    TRADING_DECISION = "trading_decision"
    WEALTH_MANAGEMENT = "wealth_management"

class DecisionType(Enum):
    """Financial decision outcomes"""
    APPROVE = "approve"
    DENY = "deny"
    APPROVE_WITH_CONDITIONS = "approve_with_conditions"
    REQUEST_MORE_INFO = "request_more_info"
    ESCALATE_TO_HUMAN = "escalate_to_human"
    OFFER_ALTERNATIVE = "offer_alternative"

class RiskLevel(Enum):
    """Risk assessment levels"""
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    EXTREME = "extreme"

@dataclass
class Customer:
    """Customer information for financial decisions"""
    customer_id: str
    age: int
    income: int
    credit_score: int
    employment_status: str
    location: str
    gender: str
    ethnicity: str
    marital_status: str
    dependents: int
    education_level: str
    account_history_years: int
    previous_defaults: int

@dataclass
class FinancialRequest:
    """Financial service request"""
    request_id: str
    service_type: FinancialService
    customer: Customer
    amount_requested: float
    purpose: str
    requested_terms: Dict[str, Any]
    risk_factors: List[str]
    market_conditions: Dict[str, float]
    regulatory_constraints: List[str]

class FinancialAIEthics:
    """AI system for ethical financial decisions using TML framework"""
    
    def __init__(self):
        self.tml_evaluator = TMLEvaluator()
        self.decision_log = []
        
        # Protected characteristics for bias detection
        self.protected_characteristics = [
            "gender", "ethnicity", "age", "marital_status", 
            "location", "education_level"
        ]
        
        # Regulatory frameworks
        self.regulations = {
            "fair_credit_reporting": ["credit_score", "employment_status", "payment_history"],
            "equal_credit_opportunity": ["gender", "ethnicity", "marital_status", "age"],
            "community_reinvestment": ["location", "income_level"],
            "gdpr_privacy": ["data_minimization", "consent", "transparency"]
        }
    
    def make_financial_decision(self, request: FinancialRequest) -> Dict[str, Any]:
        """
        Make ethical financial decision using TML framework
        
        Returns:
        - decision: DecisionType enum
        - moral_state: TML state for this decision
        - sacred_pause_engaged: Whether complex ethics required pause
        - bias_analysis: Detailed bias and fairness assessment
        - regulatory_compliance: Compliance with financial regulations
        - reasoning: Detailed explanation of decision
        """
        
        # Perform bias and fairness analysis
        bias_analysis = self._analyze_bias_risks(request)
        
        # Check regulatory compliance
        compliance_analysis = self._assess_regulatory_compliance(request)
        
        # Calculate ethical complexity
        complexity_analysis = self._assess_financial_complexity(request, bias_analysis)
        
        # Create context for TML evaluation
        context = {
            "scenario": f"{request.service_type.value} for ${request.amount_requested:,.0f}: {request.purpose}",
            "stakeholders": self._identify_stakeholders(request),
            "values_at_stake": ["fairness", "economic_opportunity", "financial_stability", "regulatory_compliance", "privacy"],
            "complexity_score": complexity_analysis["total_complexity"],
            "bias_risks": bias_analysis,
            "regulatory_factors": compliance_analysis
        }
        
        # Evaluate using TML framework
        evaluation_text = f"Financial decision: {request.service_type.value} for ${request.amount_requested:,.0f}"
        tml_result = self.tml_evaluator.evaluate(evaluation_text, context)
        
        # Generate decision based on moral state
        if tml_result.state == TMLState.SACRED_PAUSE:
            decision = self._sacred_pause_financial_decision(request, bias_analysis, tml_result)
        elif tml_result.state == TMLState.AFFIRMATION:
            decision = self._standard_financial_decision(request, bias_analysis)
        else:  # RESISTANCE - potential bias or unfair treatment detected
            decision = self._bias_mitigation_decision(request, bias_analysis)
        
        result = {
            "request_id": request.request_id,
            "decision": decision["decision"],
            "moral_state": tml_result.state,
            "sacred_pause_engaged": tml_result.state == TMLState.SACRED_PAUSE,
            "complexity_analysis": complexity_analysis,
            "bias_analysis": bias_analysis,
            "regulatory_compliance": compliance_analysis,
            "reasoning": decision["reasoning"],
            "confidence_score": decision["confidence"],
            "conditions": decision.get("conditions", []),
            "alternative_offers": decision.get("alternatives", []),
            "human_review_required": decision.get("human_review", False),
            "timestamp": datetime.now().isoformat()
        }
        
        # Log decision for audit and regulatory compliance
        self.decision_log.append(result)
        
        return result
    
    def _analyze_bias_risks(self, request: FinancialRequest) -> Dict[str, Any]:
        """Analyze potential bias and fairness issues in financial decision"""
        
        analysis = {
            "bias_risks": [],
            "fairness_concerns": [],
            "protected_group_impact": {},
            "disparate_impact_risk": 0.0
        }
        
        customer = request.customer
        
        # Age bias detection
        if request.service_type in [FinancialService.LOAN_APPROVAL, FinancialService.INSURANCE_PRICING]:
            if customer.age < 25 or customer.age > 65:
                analysis["bias_risks"].append("age_discrimination")
                analysis["protected_group_impact"]["age"] = "high_risk"
        
        # Gender bias detection
        if customer.gender in ["female", "non-binary"]:
            analysis["protected_group_impact"]["gender"] = "monitor_for_bias"
        
        # Geographic bias (redlining prevention)
        high_risk_locations = ["inner_city", "rural_underserved", "minority_majority"]
        if customer.location in high_risk_locations:
            analysis["bias_risks"].append("geographic_discrimination")
            analysis["fairness_concerns"].append("potential_redlining")
        
        # Income bias vs. legitimate risk assessment
        if customer.income < 30000 and request.amount_requested > customer.income * 3:
            analysis["fairness_concerns"].append("debt_to_income_ratio")
        
        # Education level bias
        if customer.education_level in ["high_school", "less_than_high_school"]:
            analysis["bias_risks"].append("education_discrimination")
        
        # Calculate overall disparate impact risk
        risk_factors = len(analysis["bias_risks"]) + len(analysis["fairness_concerns"])
        analysis["disparate_impact_risk"] = min(1.0, risk_factors / 5)
        
        return analysis
    
    def _assess_regulatory_compliance(self, request: FinancialRequest) -> Dict[str, Any]:
        """Assess compliance with financial regulations"""
        
        compliance = {
            "compliant_regulations": [],
            "violation_risks": [],
            "required_disclosures": [],
            "audit_requirements": []
        }
        
        # Fair Credit Reporting Act compliance
        if request.service_type in [FinancialService.LOAN_APPROVAL, FinancialService.CREDIT_SCORING]:
            if request.customer.credit_score >= 300:  # Valid credit score
                compliance["compliant_regulations"].append("fair_credit_reporting_act")
            else:
                compliance["violation_risks"].append("invalid_credit_assessment")
        
        # Equal Credit Opportunity Act compliance
        protected_factors_used = any(
            factor in ["gender", "ethnicity", "marital_status"] 
            for factor in request.risk_factors
        )
        if protected_factors_used:
            compliance["violation_risks"].append("protected_characteristic_discrimination")
        else:
            compliance["compliant_regulations"].append("equal_credit_opportunity_act")
        
        # Community Reinvestment Act compliance
        if request.customer.location in ["underserved_community"] and request.service_type == FinancialService.LOAN_APPROVAL:
            compliance["audit_requirements"].append("community_reinvestment_act_reporting")
        
        # GDPR/Privacy compliance
        compliance["required_disclosures"].extend([
            "data_usage_explanation",
            "automated_decision_notice",
            "right_to_human_review"
        ])
        
        return compliance
    
    def _assess_financial_complexity(self, request: FinancialRequest, bias_analysis: Dict) -> Dict[str, float]:
        """Calculate ethical complexity score for financial decision"""
        
        # Factor 1: Bias risk severity
        bias_factor = bias_analysis["disparate_impact_risk"]
        
        # Factor 2: Amount significance relative to customer income
        amount_factor = min(1.0, request.amount_requested / max(1, request.customer.income))
        
        # Factor 3: Protected group membership
        protected_groups = len(bias_analysis["protected_group_impact"])
        protection_factor = min(1.0, protected_groups / 4)
        
        # Factor 4: Regulatory complexity
        regulatory_risks = len(request.regulatory_constraints)
        regulatory_factor = min(1.0, regulatory_risks / 3)
        
        # Factor 5: Customer vulnerability
        vulnerability_indicators = 0
        if request.customer.income < 30000:
            vulnerability_indicators += 1
        if request.customer.age < 25 or request.customer.age > 65:
            vulnerability_indicators += 1
        if request.customer.credit_score < 600:
            vulnerability_indicators += 1
        if request.customer.previous_defaults > 0:
            vulnerability_indicators += 1
        vulnerability_factor = vulnerability_indicators / 4
        
        # Factor 6: Market conditions impact
        market_volatility = request.market_conditions.get("volatility", 0.0)
        market_factor = min(1.0, market_volatility)
        
        # Factor 7: Decision reversibility
        reversibility_factor = 0.8 if request.service_type == FinancialService.LOAN_APPROVAL else 0.3
        
        # Weighted combination
        total_complexity = (
            bias_factor * 0.25 +
            amount_factor * 0.15 +
            protection_factor * 0.20 +
            regulatory_factor * 0.15 +
            vulnerability_factor * 0.15 +
            market_factor * 0.05 +
            reversibility_factor * 0.05
        )
        
        return {
            "total_complexity": total_complexity,
            "bias_risk": bias_factor,
            "amount_significance": amount_factor,
            "protected_groups": protection_factor,
            "regulatory_complexity": regulatory_factor,
            "customer_vulnerability": vulnerability_factor,
            "market_conditions": market_factor,
            "decision_reversibility": reversibility_factor
        }
    
    def _identify_stakeholders(self, request: FinancialRequest) -> List[str]:
        """Identify all stakeholders affected by financial decision"""
        
        stakeholders = [
            "customer", "financial_institution", "shareholders", 
            "regulators", "community", "economy"
        ]
        
        # Service-specific stakeholders
        if request.service_type == FinancialService.LOAN_APPROVAL:
            stakeholders.extend(["co_signers", "dependents", "credit_agencies"])
        
        if request.service_type == FinancialService.INVESTMENT_ADVICE:
            stakeholders.extend(["investment_market", "other_investors"])
        
        # Protected group stakeholders
        if request.customer.ethnicity in ["minority"]:
            stakeholders.append("minority_communities")
        
        if request.customer.location in ["underserved_community"]:
            stakeholders.append("underserved_populations")
        
        return stakeholders
    
    def _sacred_pause_financial_decision(self, request: FinancialRequest, 
                                       bias_analysis: Dict, tml_result: TMLEvaluation) -> Dict[str, Any]:
        """
        Complex financial decision requiring Sacred Pause deliberation
        Balances profitability, fairness, regulatory compliance, and social responsibility
        """
        print("💰 Sacred Pause Engaged - Complex Financial Ethics Decision")
        print("⏱️  Enhanced deliberation time: 2500ms")
        
        # Sacred Pause ethical considerations
        ethical_principles = [
            "Financial Inclusion: Expand access to financial services equitably",
            "Fair Treatment: Prevent discrimination and bias in decisions",
            "Responsible Lending: Protect customers from predatory practices",
            "Regulatory Compliance: Adhere to all applicable financial laws",
            "Risk Management: Balance risk with opportunity and fairness",
            "Community Impact: Consider broader socioeconomic effects"
        ]
        
        print("🤔 Financial Ethics Principles Under Consideration:")
        for principle in ethical_principles:
            print(f"   • {principle}")
        
        # Multi-criteria decision analysis
        decision_scores = self._score_financial_decisions(request, bias_analysis)
        
        # Select decision with highest ethical balance
        best_decision = max(decision_scores, key=decision_scores.get)
        confidence = decision_scores[best_decision]
        
        # Generate conditions or alternatives if needed
        conditions, alternatives = self._generate_financial_options(request, best_decision)
        
        # Determine human review requirement
        human_review = (
            confidence < 0.7 or
            bias_analysis["disparate_impact_risk"] > 0.6 or
            request.amount_requested > 500000
        )
        
        reasoning = self._generate_sacred_pause_financial_reasoning(
            best_decision, request, bias_analysis, decision_scores
        )
        
        return {
            "decision": best_decision,
            "confidence": confidence,
            "reasoning": reasoning,
            "conditions": conditions,
            "alternatives": alternatives,
            "human_review": human_review,
            "decision_scores": {str(k): v for k, v in decision_scores.items()}
        }
    
    def _score_financial_decisions(self, request: FinancialRequest, bias_analysis: Dict) -> Dict[DecisionType, float]:
        """Score each possible financial decision across multiple ethical dimensions"""
        
        scores = {}
        
        # Factors for scoring
        high_bias_risk = bias_analysis["disparate_impact_risk"] > 0.5
        good_credit = request.customer.credit_score >= 650
        adequate_income = request.amount_requested <= request.customer.income * 2.5
        protected_group = len(bias_analysis["protected_group_impact"]) > 0
        
        # Score APPROVE
        approve_score = 0.7
        if good_credit and adequate_income:
            approve_score += 0.2
        if high_bias_risk and not good_credit:
            approve_score -= 0.4  # Avoid approving high-risk decisions that could appear biased
        if protected_group and good_credit:
            approve_score += 0.1  # Positive bias correction
        scores[DecisionType.APPROVE] = max(0.0, approve_score)
        
        # Score DENY
        deny_score = 0.3
        if not good_credit or not adequate_income:
            deny_score += 0.4
        if high_bias_risk and protected_group:
            deny_score -= 0.3  # Avoid denying protected groups without strong justification
        scores[DecisionType.DENY] = max(0.0, deny_score)
        
        # Score APPROVE WITH CONDITIONS
        conditional_score = 0.8
        if not good_credit but adequate_income:
            conditional_score += 0.2
        if protected_group:
            conditional_score += 0.1  # Prefer conditional approval to outright denial
        scores[DecisionType.APPROVE_WITH_CONDITIONS] = max(0.0, conditional_score)
        
        # Score REQUEST MORE INFO
        more_info_score = 0.6
        if high_bias_risk:
            more_info_score += 0.3  # Gather more data to ensure fair decision
        if request.customer.account_history_years < 2:
            more_info_score += 0.2
        scores[DecisionType.REQUEST_MORE_INFO] = max(0.0, more_info_score)
        
        # Score ESCALATE TO HUMAN
        escalate_score = 0.5
        if high_bias_risk and protected_group:
            escalate_score += 0.4
        if request.amount_requested > 250000:
            escalate_score += 0.2
        scores[DecisionType.ESCALATE_TO_HUMAN] = max(0.0, escalate_score)
        
        # Score OFFER ALTERNATIVE
        alternative_score = 0.7
        if not adequate_income but good_credit:
            alternative_score += 0.2
        if protected_group and not good_credit:
            alternative_score += 0.1  # Offer alternatives rather than outright denial
        scores[DecisionType.OFFER_ALTERNATIVE] = max(0.0, alternative_score)
        
        return scores
    
    def _generate_financial_options(self, request: FinancialRequest, 
                                  decision: DecisionType) -> Tuple[List[str], List[str]]:
        """Generate conditions and alternatives based on decision"""
        
        conditions = []
        alternatives = []
        
        if decision == DecisionType.APPROVE_WITH_CONDITIONS:
            if request.customer.credit_score < 650:
                conditions.append("Higher interest rate due to credit risk")
                conditions.append("Required credit monitoring enrollment")
            
            if request.amount_requested > request.customer.income * 2:
                conditions.append("Reduced loan amount to improve debt-to-income ratio")
            
            if request.customer.previous_defaults > 0:
                conditions.append("Co-signer required")
        
        elif decision == DecisionType.OFFER_ALTERNATIVE:
            if request.service_type == FinancialService.LOAN_APPROVAL:
                alternatives.append("Secured loan option with collateral")
                alternatives.append("Credit-building loan program")
                alternatives.append("Financial counseling and reapplication in 6 months")
            
            if request.service_type == FinancialService.INVESTMENT_ADVICE:
                alternatives.append("Lower-risk investment portfolio")
                alternatives.append("Dollar-cost averaging strategy")
        
        return conditions, alternatives
    
    def _standard_financial_decision(self, request: FinancialRequest, bias_analysis: Dict) -> Dict[str, Any]:
        """Standard financial decision for clear-cut cases (no Sacred Pause needed)"""
        
        # Simple rule-based decision
        customer = request.customer
        
        if (customer.credit_score >= 700 and 
            request.amount_requested <= customer.income * 2 and
            bias_analysis["disparate_impact_risk"] < 0.3):
            decision = DecisionType.APPROVE
            confidence = 0.90
            reasoning = "Strong credit profile and low bias risk. Standard approval criteria met."
        
        elif (customer.credit_score < 500 or 
              request.amount_requested > customer.income * 4):
            decision = DecisionType.DENY
            confidence = 0.85
            reasoning = "High credit risk or excessive debt-to-income ratio. Standard denial criteria."
        
        else:
            decision = DecisionType.REQUEST_MORE_INFO
            confidence = 0.75
            reasoning = "Borderline case requiring additional documentation and review."
        
        return {
            "decision": decision,
            "confidence": confidence,
            "reasoning": reasoning,
            "conditions": [],
            "alternatives": [],
            "human_review": False
        }
    
    def _bias_mitigation_decision(self, request: FinancialRequest, bias_analysis: Dict) -> Dict[str, Any]:
        """Handle potential bias situations (RESISTANCE state)"""
        
        # When bias is detected, escalate to human and apply fairness corrections
        decision = DecisionType.ESCALATE_TO_HUMAN
        
        reasoning = f"Potential bias detected in decision process. "
        reasoning += f"Bias risks: {', '.join(bias_analysis['bias_risks'])}. "
        reasoning += f"Escalating to human review to ensure fair treatment and regulatory compliance."
        
        return {
            "decision": decision,
            "confidence": 0.95,  # High confidence in need for human review
            "reasoning": reasoning,
            "conditions": ["Bias mitigation review required"],
            "alternatives": [],
            "human_review": True
        }
    
    def _generate_sacred_pause_financial_reasoning(self, decision: DecisionType, 
                                                 request: FinancialRequest,
                                                 bias_analysis: Dict, 
                                                 scores: Dict) -> str:
        """Generate detailed reasoning for Sacred Pause financial decisions"""
        
        reasoning = "💰 SACRED PAUSE FINANCIAL ETHICS ANALYSIS:\n\n"
        reasoning += "This financial decision triggered enhanced ethical deliberation due to:\n"
        reasoning += f"• Complex intersection of risk assessment and fairness principles\n"
        reasoning += f"• Potential protected group impact requiring careful consideration\n"
        reasoning += f"• Regulatory compliance requirements across multiple frameworks\n"
        reasoning += f"• Significant financial impact on customer and community\n\n"
        
        reasoning += f"SELECTED DECISION: {decision.value.replace('_', ' ').title()}\n\n"
        
        # Customer profile
        reasoning += "CUSTOMER PROFILE:\n"
        reasoning += f"• Age: {request.customer.age}, Income: ${request.customer.income:,}\n"
        reasoning += f"• Credit Score: {request.customer.credit_score}\n"
        reasoning += f"• Location: {request.customer.location}\n"
        reasoning += f"• Request: ${request.amount_requested:,.0f} for {request.purpose}\n\n"
        
        # Bias analysis
        reasoning += "BIAS & FAIRNESS ANALYSIS:\n"
        if bias_analysis["bias_risks"]:
            reasoning += f"• Bias risks identified: {', '.join(bias_analysis['bias_risks'])}\n"
        if bias_analysis["protected_group_impact"]:
            reasoning += f"• Protected group considerations: {list(bias_analysis['protected_group_impact'].keys())}\n"
        reasoning += f"• Disparate impact risk: {bias_analysis['disparate_impact_risk']:.3f}\n\n"
        
        # Decision scores
        reasoning += "DECISION EVALUATION SCORES:\n"
        for dec, score in scores.items():
            reasoning += f"• {dec.value.replace('_', ' ').title()}: {score:.3f}\n"
        
        reasoning += f"\nETHICAL CONSIDERATIONS BALANCED:\n"
        reasoning += f"1. Financial Inclusion: Expanding access while managing risk\n"
        reasoning += f"2. Fair Treatment: Preventing discrimination and bias\n"
        reasoning += f"3. Responsible Lending: Protecting customer financial wellbeing\n"
        reasoning += f"4. Regulatory Compliance: Adhering to fair lending laws\n"
        reasoning += f"5. Community Impact: Contributing to economic opportunity\n"
        
        return reasoning
    
    def generate_fairness_report(self) -> Dict[str, Any]:
        """Generate fairness and bias report across all decisions"""
        
        if not self.decision_log:
            return {"error": "No decisions to analyze"}
        
        # Analyze decisions by protected characteristics
        fairness_metrics = {
            "total_decisions": len(self.decision_log),
            "approval_rates_by_group": {},
            "bias_incidents": 0,
            "sacred_pause_rate": 0,
            "human_review_rate": 0
        }
        
        sacred_pause_count = sum(1 for d in self.decision_log if d["sacred_pause_engaged"])
        human_review_count = sum(1 for d in self.decision_log if d.get("human_review_required", False))
        
        fairness_metrics["sacred_pause_rate"] = sacred_pause_count / len(self.decision_log)
        fairness_metrics["human_review_rate"] = human_review_count / len(self.decision_log)
        fairness_metrics["bias_incidents"] = sum(1 for d in self.decision_log 
                                               if d["moral_state"] == TMLState.RESISTANCE)
        
        return fairness_metrics
    
    def get_decision_history(self) -> List[Dict]:
        """Return audit trail of all financial decisions"""
        return self.decision_log
    
    def export_decisions(self, filename: str) -> None:
        """Export decision log to JSON file for regulatory audit"""
        with open(filename, 'w') as f:
            json.dump(self.decision_log, f, indent=2, default=str)


def demo_financial_ai_ethics():
    """Demonstration of financial AI ethics system with various complexity scenarios"""
    
    print("💰 Financial AI Ethics System - TML Framework Demo")
    print("=" * 55)
    
    ethics_system = FinancialAIEthics()
    
    # Create test customers
    prime_customer = Customer(
        "cust_001", 35, 75000, 750, "employed", "suburban", 
        "male", "white", "married", 2, "bachelor", 8, 0
    )
    
    protected_customer = Customer(
        "cust_002", 28, 45000, 620, "employed", "inner_city",
        "female", "hispanic", "single", 1, "high_school", 3, 1
    )
    
    vulnerable_customer = Customer(
        "cust_003", 67, 25000, 580, "retired", "rural_underserved",
        "female", "african_american", "widowed", 0, "less_than_high_school", 15, 2
    )
    
    # Scenario 1: Standard loan approval (should be AFFIRMATION)
    print("\n💳 SCENARIO 1: Standard Loan Approval (Low Complexity)")
    print("-" * 50)
    
    standard_request = FinancialRequest(
        "req_001", FinancialService.LOAN_APPROVAL, prime_customer,
        50000, "home_improvement", {"term": "5_years", "rate": "market"},
        ["good_employment", "stable_income"], {"volatility": 0.1}, []
    )
    
    result1 = ethics_system.make_financial_decision(standard_request)
    print(f"Decision: {result1['decision'].value}")
    print(f"Moral State: {result1['moral_state'].value}")
    print(f"Sacred Pause: {result1['sacred_pause_engaged']}")
    print(f"Complexity: {result1['complexity_analysis']['total_complexity']:.3f}")
    print(f"Bias Risk: {result1['bias_analysis']['disparate_impact_risk']:.3f}")
    
    # Scenario 2: Protected group loan (should trigger Sacred Pause)
    print("\n⚖️  SCENARIO 2: Protected Group Financial Decision (High Complexity)")
    print("-" * 60)
    
    protected_request = FinancialRequest(
        "req_002", FinancialService.LOAN_APPROVAL, protected_customer,
        35000, "small_business_startup", {"term": "7_years", "rate": "market_plus"},
        ["new_business", "minority_owned"], {"volatility": 0.3}, 
        ["community_reinvestment_act", "equal_credit_opportunity_act"]
    )
    
    result2 = ethics_system.make_financial_decision(protected_request)
    print(f"Decision: {result2['decision'].value}")
    print(f"Moral State: {result2['moral_state'].value}")
    print(f"Sacred Pause: {result2['sacred_pause_engaged']}")
    print(f"Complexity: {result2['complexity_analysis']['total_complexity']:.3f}")
    print(f"Bias Risk: {result2['bias_analysis']['disparate_impact_risk']:.3f}")
    print(f"Human Review: {result2['human_review_required']}")
    
    if result2['sacred_pause_engaged']:
        print(f"\n💰 Sacred Pause Financial Reasoning:")
        print(result2['reasoning'])
    
    # Scenario 3: Vulnerable customer (high ethical stakes)
    print("\n👵 SCENARIO 3: Vulnerable Customer Protection")
    print("-" * 45)
    
    vulnerable_request = FinancialRequest(
        "req_003", FinancialService.LOAN_APPROVAL, vulnerable_customer,
        15000, "debt_consolidation", {"term": "10_years", "rate": "high"},
        ["fixed_income", "previous_defaults", "rural_location"], 
        {"volatility": 0.2}, ["fair_credit_reporting_act"]
    )
    
    result3 = ethics_system.make_financial_decision(vulnerable_request)
    print(f"Decision: {result3['decision'].value}")
    print(f"Moral State: {result3['moral_state'].value}")
    print(f"Sacred Pause: {result3['sacred_pause_engaged']}")
    print(f"Complexity: {result3['complexity_analysis']['total_complexity']:.3f}")
    
    if result3['conditions']:
        print(f"Conditions: {result3['conditions']}")
    if result3['alternative_offers']:
        print(f"Alternatives: {result3['alternative_offers']}")
    
    # Generate fairness report
    fairness_report = ethics_system.generate_fairness_report()
    print(f"\n📊 FAIRNESS METRICS:")
    print(f"• Total Decisions: {fairness_report['total_decisions']}")
    print(f"• Sacred Pause Rate: {fairness_report['sacred_pause_rate']:.1%}")
    print(f"• Human Review Rate: {fairness_report['human_review_rate']:.1%}")
    print(f"• Bias Incidents: {fairness_report['bias_incidents']}")
    
    # Export audit trail
    ethics_system.export_decisions("financial_ai_audit.json")
    print(f"\n📋 Financial audit trail exported to: financial_ai_audit.json")
    
    print(f"\n✅ Demo completed! TML framework ensured ethical financial decisions.")
    print("Sacred Pause protected against bias while enabling financial inclusion.")


if __name__ == "__main__":
    demo_financial_ai_ethics()

# Created by Lev Goukassian • ORCID: 0009-0006-5966-1243 • Email: leogouk@gmail.com • Successor Contact: support@tml-goukassian.org • [see Succession Charter](/TML-SUCCESSION-CHARTER.md)
