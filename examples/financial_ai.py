"""
Financial AI Decision System TML Implementation Example

Demonstrates how a financial institution MIGHT implement TML for
lending, trading, and risk decisions. All thresholds are EXAMPLES ONLY.
Financial institutions must determine appropriate values based on
regulatory requirements and risk tolerance.

NOT FINANCIAL ADVICE. For demonstration purposes only.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from implementations.python_library import create_tml_framework, ComplianceChecker, BatchLogger
import random
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from decimal import Decimal


class FinancialDecisionType:
    """Example financial decision categories"""
    LOAN_APPROVAL = "loan_approval"
    CREDIT_LIMIT = "credit_limit"
    TRADING = "trading"
    FRAUD_DETECTION = "fraud_detection"
    ACCOUNT_CLOSURE = "account_closure"
    INVESTMENT_ADVICE = "investment_advice"


class FinancialAI:
    """
    EXAMPLE financial AI system with TML integration.
    
    Real financial systems require regulatory compliance (SOX, GDPR, etc.),
    extensive testing, and audit trails. This is for demonstration only.
    """
    
    def __init__(self):
        # EXAMPLE CONFIGURATION - NOT FOR PRODUCTION USE
        self.framework = create_tml_framework(
            sprl_threshold=0.6,  # EXAMPLE: Medium threshold for financial
            domain="financial",
            calculate_risk_on="all",
            retention_days=2555  # 7 years per financial regulations
        )
        
        # High-frequency trading uses batch logging
        self.trading_batch_logger = BatchLogger(self.framework, batch_size=100)
        
        print("=" * 70)
        print("FINANCIAL AI TML IMPLEMENTATION EXAMPLE")
        print("=" * 70)
        print()
        print("⚠️  DISCLAIMER:")
        print("This is a demonstration only. NOT financial advice.")
        print("Real financial AI requires regulatory compliance.")
        print()
        print("Example Configuration:")
        print(f"  SPRL Threshold: {self.framework.sprl_threshold} (example only)")
        print(f"  Retention: 7 years (financial regulation requirement)")
        print(f"  Batch logging for high-frequency trading")
        print()
    
    def assess_financial_risk(self, transaction: Dict) -> float:
        """
        EXAMPLE risk assessment for financial decisions.
        
        Real systems would use sophisticated credit scoring,
        market analysis, and regulatory compliance checks.
        """
        risk_score = 0.0
        decision_type = transaction.get('type')
        
        if decision_type == FinancialDecisionType.LOAN_APPROVAL:
            # Loan risk factors (simplified)
            amount = transaction.get('amount', 0)
            income = transaction.get('annual_income', 1)
            credit_score = transaction.get('credit_score', 700)
            
            # Debt-to-income ratio
            dti = amount / max(income, 1)
            if dti > 0.5:
                risk_score += 0.5
            elif dti > 0.3:
                risk_score += 0.3
            elif dti > 0.2:
                risk_score += 0.1
            
            # Credit score factor
            if credit_score < 600:
                risk_score += 0.4
            elif credit_score < 650:
                risk_score += 0.3
            elif credit_score < 700:
                risk_score += 0.1
            
            # Loan amount factor
            if amount > 500000:
                risk_score += 0.3
            elif amount > 100000:
                risk_score += 0.2
            elif amount > 50000:
                risk_score += 0.1
            
        elif decision_type == FinancialDecisionType.TRADING:
            # Trading risk factors
            volume = transaction.get('volume', 0)
            volatility = transaction.get('market_volatility', 0)
            
            if volume > 1000000:
                risk_score += 0.4
            elif volume > 100000:
                risk_score += 0.2
            
            risk_score += volatility * 0.5
            
        elif decision_type == FinancialDecisionType.FRAUD_DETECTION:
            # Fraud risk indicators
            anomaly_score = transaction.get('anomaly_score', 0)
            risk_score = min(anomaly_score, 1.0)
            
        elif decision_type == FinancialDecisionType.ACCOUNT_CLOSURE:
            # Account closure is always high risk (affects customer)
            risk_score = 0.8
        
        # Protected class considerations (fair lending)
        if transaction.get('affects_protected_class'):
            risk_score = max(risk_score, 0.7)  # Ensure logging for fairness
        
        return min(risk_score, 1.0)
    
    def process_loan_application(self, application: Dict) -> Dict:
        """Process loan application with TML logging."""
        
        application['type'] = FinancialDecisionType.LOAN_APPROVAL
        application['calculated_risk'] = self.assess_financial_risk(application)
        
        # Check for fair lending considerations
        application['affects_protected_class'] = application.get('monitor_fairness', False)
        
        # Stakeholders
        application['stakeholders'] = [
            {'type': 'applicant', 'id': application.get('applicant_id')},
            {'type': 'institution', 'id': 'bank'},
            {'type': 'shareholders', 'id': 'investors'}
        ]
        
        def loan_decision_logic(context):
            risk = context['calculated_risk']
            credit_score = context.get('credit_score', 700)
            
            if risk > 0.8:
                return {
                    'decision': 'declined',
                    'reason': 'High risk profile',
                    'factors': ['DTI ratio', 'Credit score'],
                    'appeal_available': True
                }
            elif risk > 0.6:
                return {
                    'decision': 'manual_review',
                    'reason': 'Requires additional verification',
                    'factors': ['Income verification needed'],
                    'appeal_available': True
                }
            elif risk > 0.3:
                return {
                    'decision': 'approved_with_conditions',
                    'reason': 'Moderate risk',
                    'interest_rate': 7.5 + (risk * 5),
                    'conditions': ['Higher down payment required'],
                    'appeal_available': False
                }
            else:
                return {
                    'decision': 'approved',
                    'reason': 'Low risk profile',
                    'interest_rate': 5.0 + (risk * 3),
                    'conditions': [],
                    'appeal_available': False
                }
        
        # Process with TML
        result = self.framework.process_decision(
            context=application,
            ai_decision_func=loan_decision_logic
        )
        
        return result
    
    def process_trading_decision(self, trade: Dict) -> Dict:
        """Process high-frequency trading decision."""
        
        trade['type'] = FinancialDecisionType.TRADING
        trade['calculated_risk'] = self.assess_financial_risk(trade)
        
        decision = {
            'decision_id': f"TRADE-{random.randint(100000, 999999)}",
            'timestamp': datetime.now().isoformat(),
            'action': 'execute' if trade['calculated_risk'] < 0.7 else 'hold',
            'price': trade.get('price'),
            'volume': trade.get('volume')
        }
        
        # Use batch logger for high-frequency trading
        self.trading_batch_logger.log_decision(trade, decision)
        
        return decision
    
    def detect_fraud(self, transaction: Dict) -> Dict:
        """Process fraud detection with TML logging."""
        
        transaction['type'] = FinancialDecisionType.FRAUD_DETECTION
        transaction['calculated_risk'] = self.assess_financial_risk(transaction)
        
        def fraud_detection_logic(context):
            anomaly_score = context.get('anomaly_score', 0)
            
            if anomaly_score > 0.9:
                return {
                    'action': 'block',
                    'reason': 'High fraud probability',
                    'notify_customer': True,
                    'notify_fraud_team': True
                }
            elif anomaly_score > 0.7:
                return {
                    'action': 'challenge',
                    'reason': 'Suspicious activity',
                    'require_2fa': True,
                    'notify_fraud_team': True
                }
            elif anomaly_score > 0.5:
                return {
                    'action': 'monitor',
                    'reason': 'Elevated risk',
                    'enhanced_monitoring': True,
                    'notify_fraud_team': False
                }
            else:
                return {
                    'action': 'approve',
                    'reason': 'Normal activity',
                    'notify_customer': False,
                    'notify_fraud_team': False
                }
        
        result = self.framework.process_decision(
            context=transaction,
            ai_decision_func=fraud_detection_logic
        )
        
        return result
    
    def demonstrate_lending_decisions(self):
        """Simulate various lending decisions."""
        
        print("LOAN APPLICATION PROCESSING")
        print("-" * 70)
        print()
        
        applications = [
            {
                'applicant_id': 'APP-001',
                'amount': 250000,
                'annual_income': 75000,
                'credit_score': 720,
                'employment_years': 5,
                'description': 'Standard mortgage application'
            },
            {
                'applicant_id': 'APP-002',
                'amount': 50000,
                'annual_income': 35000,
                'credit_score': 580,
                'employment_years': 1,
                'description': 'High-risk personal loan'
            },
            {
                'applicant_id': 'APP-003',
                'amount': 500000,
                'annual_income': 150000,
                'credit_score': 680,
                'employment_years': 3,
                'monitor_fairness': True,  # Fair lending monitoring
                'description': 'Large loan with fairness monitoring'
            },
            {
                'applicant_id': 'APP-004',
                'amount': 15000,
                'annual_income': 60000,
                'credit_score': 750,
                'employment_years': 10,
                'description': 'Low-risk auto loan'
            }
        ]
        
        for app in applications:
            print(f"Application: {app['applicant_id']}")
            print(f"  Type: {app['description']}")
            print(f"  Amount: ${app['amount']:,}")
            print(f"  Credit Score: {app['credit_score']}")
            
            result = self.process_loan_application(app)
            decision = result['decision']
            
            print(f"  Decision: {decision['decision'].upper()}")
            print(f"  Reason: {decision['reason']}")
            if 'interest_rate' in decision:
                print(f"  Rate: {decision['interest_rate']:.2f}%")
            print(f"  Risk Score: {app['calculated_risk']:.2f}")
            print(f"  SPRL Score: {result['sprl_score']:.2f}")
            
            if result['sacred_pause_triggered']:
                print(f"  ✓ Decision logged for compliance")
                print(f"    Log Hash: {result['storage_hash'][:12]}...")
                if app.get('monitor_fairness'):
                    print(f"    📊 Fair lending monitoring active")
            else:
                print(f"  - Below logging threshold")
            
            print()
    
    def demonstrate_trading_operations(self):
        """Simulate high-frequency trading with batch logging."""
        
        print("HIGH-FREQUENCY TRADING SIMULATION")
        print("-" * 70)
        print()
        
        print("Processing 100 trades in batch mode...")
        start_time = time.time()
        
        trades_executed = 0
        trades_held = 0
        
        for i in range(100):
            trade = {
                'symbol': random.choice(['AAPL', 'GOOGL', 'MSFT', 'AMZN']),
                'volume': random.randint(100, 10000),
                'price': random.uniform(100, 500),
                'market_volatility': random.random() * 0.5,
                'timestamp': time.time()
            }
            
            decision = self.process_trading_decision(trade)
            
            if decision['action'] == 'execute':
                trades_executed += 1
            else:
                trades_held += 1
        
        # Flush batch logger
        self.trading_batch_logger.flush()
        
        elapsed = time.time() - start_time
        trades_per_second = 100 / elapsed
        
        print(f"Completed 100 trades in {elapsed:.3f} seconds")
        print(f"Rate: {trades_per_second:.0f} trades/second")
        print(f"Executed: {trades_executed}, Held: {trades_held}")
        print()
        print("Batch logging ensures compliance without impacting")
        print("high-frequency trading performance.")
        print()
    
    def demonstrate_fraud_detection(self):
        """Simulate fraud detection scenarios."""
        
        print("FRAUD DETECTION SYSTEM")
        print("-" * 70)
        print()
        
        transactions = [
            {
                'transaction_id': 'TXN-001',
                'amount': 50.00,
                'anomaly_score': 0.1,
                'location': 'usual',
                'description': 'Normal purchase'
            },
            {
                'transaction_id': 'TXN-002',
                'amount': 5000.00,
                'anomaly_score': 0.6,
                'location': 'unusual',
                'description': 'Large unusual purchase'
            },
            {
                'transaction_id': 'TXN-003',
                'amount': 10000.00,
                'anomaly_score': 0.95,
                'location': 'foreign',
                'description': 'Highly suspicious transaction'
            }
        ]
        
        for txn in transactions:
            print(f"Transaction: {txn['transaction_id']}")
            print(f"  Description: {txn['description']}")
            print(f"  Amount: ${txn['amount']:,.2f}")
            print(f"  Anomaly Score: {txn['anomaly_score']:.2f}")
            
            result = self.detect_fraud(txn)
            decision = result['decision']
            
            print(f"  Action: {decision['action'].upper()}")
            print(f"  Reason: {decision['reason']}")
            
            if result['sacred_pause_triggered']:
                print(f"  ✓ Fraud decision logged")
                print(f"    Log Hash: {result['storage_hash'][:12]}...")
            
            print()
    
    def demonstrate_regulatory_audit(self):
        """Demonstrate regulatory compliance audit."""
        
        print("=" * 70)
        print("REGULATORY COMPLIANCE AUDIT")
        print("=" * 70)
        print()
        
        print("Scenario: Quarterly fair lending compliance review")
        print()
        
        # Request logs for protected class monitoring
        audit_request = {
            'id': 'AUDIT-FL-2025-Q3',
            'timeframe': (
                (datetime.now() - timedelta(days=90)).isoformat(),
                datetime.now().isoformat()
            ),
            'purpose': 'Fair lending compliance review'
        }
        
        # Regulatory body requests access
        audit_package = self.framework.provide_investigation_access(
            institution='un_human_rights',  # Example regulatory authority
            incident=audit_request
        )
        
        if audit_package:
            print("Compliance Audit Package:")
            print(f"  Period: Last 90 days")
            print(f"  Decisions Logged: {audit_package['log_count']}")
            print(f"  Integrity Verified: {audit_package['integrity_verified']}")
            print()
            print("Regulatory review can verify:")
            print("  - Equal treatment across protected classes")
            print("  - Consistent application of lending criteria")
            print("  - Proper adverse action notifications")
            print("  - Risk model fairness and accuracy")
            print("  - Compliance with ECOA, Fair Lending Act")
            print()
            print("TML logs provide evidence of non-discriminatory")
            print("decision-making and regulatory compliance.")
        
        print()
    
    def display_compliance_metrics(self):
        """Display financial compliance metrics."""
        
        print("=" * 70)
        print("FINANCIAL AI COMPLIANCE METRICS")
        print("=" * 70)
        
        stats = self.framework.get_performance_report()
        
        print(f"Total Financial Decisions: {stats['total_decisions']}")
        print(f"Logged Decisions: {stats['sacred_pause_triggers']}")
        print(f"Logging Rate: {stats['trigger_rate']:.1f}%")
        print(f"Average Log Time: {stats['average_logging_time_ms']:.1f}ms")
        print(f"Storage Optimization: {stats['storage_optimization']}")
        print()
        
        # Financial-specific guidance
        if stats['trigger_rate'] < 5:
            print("⚠️  CALIBRATION NOTE:")
            print("  Low logging rate for financial decisions")
            print("  - May miss important compliance events")
            print("  - Consider if capturing fair lending issues")
            print("  - Review against regulatory requirements")
        elif stats['trigger_rate'] > 60:
            print("⚠️  CALIBRATION NOTE:")
            print("  High logging rate")
            print("  - May be over-logging routine transactions")
            print("  - Consider raising threshold for efficiency")
            print("  - Ensure storage costs remain manageable")
        else:
            print("✓ Logging rate appears appropriate")
            print("  - Continue monitoring for regulatory compliance")
            print("  - Regular audits recommended")
        
        print()


def main():
    """Run financial AI demonstration."""
    
    # Create example financial AI system
    financial_ai = FinancialAI()
    
    # Demonstrate different financial decisions
    financial_ai.demonstrate_lending_decisions()
    financial_ai.demonstrate_trading_operations()
    financial_ai.demonstrate_fraud_detection()
    
    # Show regulatory compliance
    financial_ai.demonstrate_regulatory_audit()
    
    # Display metrics
    financial_ai.display_compliance_metrics()
    
    # Compliance check
    print("=" * 70)
    print("TML INFRASTRUCTURE COMPLIANCE")
    print("=" * 70)
    
    compliance = ComplianceChecker.check_framework(financial_ai.framework)
    
    print(f"Infrastructure Compliant: {compliance['infrastructure_compliant']}")
    if not compliance['infrastructure_compliant']:
        for issue in compliance['issues']:
            print(f"  ✗ {issue}")
    else:
        print("✓ All TML requirements met")
    
    print()
    print("=" * 70)
    print("IMPORTANT NOTES FOR FINANCIAL INSTITUTIONS")
    print("=" * 70)
    print()
    print("1. Thresholds shown are examples only")
    print("2. Financial institutions must:")
    print("   - Comply with SOX, GDPR, CCPA, etc.")
    print("   - Implement fair lending monitoring")
    print("   - Maintain 7-year retention minimum")
    print("   - Enable regulatory audit access")
    print("   - Document risk calibration rationale")
    print()
    print("3. TML provides accountability infrastructure")
    print("4. Institutions determine appropriate thresholds")
    print("5. Regular calibration based on regulatory guidance")
    print()
    print("This is NOT financial advice or software.")
    print()
    print("Contact Information:")
    print("- Email: leogouk@gmail.com")
    print("- Successor Contact: support@tml-goukassian.org")
    print("- See Succession Charter: /TML-SUCCESSION-CHARTER.md")


if __name__ == "__main__":
    main()
