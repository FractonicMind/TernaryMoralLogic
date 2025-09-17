"""
Financial AI Decision System - Dual-Layer SPRL Implementation Example

Demonstrates how a financial institution implements TML with:
- Dynamic Stream (DS) from prompt arrival
- Static Anchor (SA) at Sacred Pause
- Framework-enforced thresholds (not configurable)
- I × V × P formula for risk calculation

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
    """Financial decision categories"""
    LOAN_APPROVAL = "loan_approval"
    CREDIT_LIMIT = "credit_limit"
    TRADING = "trading"
    FRAUD_DETECTION = "fraud_detection"
    ACCOUNT_CLOSURE = "account_closure"
    INVESTMENT_ADVICE = "investment_advice"


class FinancialAI:
    """
    Financial AI system with Dual-Layer SPRL implementation.
    
    Real financial systems require regulatory compliance (SOX, GDPR, etc.),
    extensive testing, and audit trails. This is for demonstration only.
    """
    
    def __init__(self):
        # Framework-enforced thresholds (not configurable)
        self.framework = create_tml_framework(
            domain="financial",
            retention_days=2555  # 7 years per financial regulations
        )
        
        # High-frequency trading uses batch logging
        self.trading_batch_logger = BatchLogger(self.framework, batch_size=100)
        
        print("=" * 70)
        print("FINANCIAL AI - DUAL-LAYER SPRL IMPLEMENTATION")
        print("=" * 70)
        print()
        print("⚠️  DISCLAIMER:")
        print("This is a demonstration only. NOT financial advice.")
        print("Real financial AI requires regulatory compliance.")
        print()
        print("Dual-Layer Architecture:")
        print("  • Dynamic Stream (DS) from prompt arrival")
        print("  • Static Anchor (SA) at Sacred Pause")
        print("  • Framework-enforced thresholds")
        print("  • I × V × P formula for risk calculation")
        print("  • Retention: 7 years (financial regulations)")
        print()
    
    def calculate_ivp_components(self, transaction: Dict) -> Dict:
        """
        Calculate I × V × P components for financial decisions.
        
        Real systems would use sophisticated credit scoring,
        market analysis, and regulatory compliance checks.
        """
        decision_type = transaction.get('type')
        
        # Initialize components
        impact = 0.5
        vulnerability = 0.5
        probability = 0.5
        
        if decision_type == FinancialDecisionType.LOAN_APPROVAL:
            # Impact based on loan amount
            amount = transaction.get('amount', 0)
            if amount > 500000:
                impact = 0.9
            elif amount > 100000:
                impact = 0.7
            elif amount > 50000:
                impact = 0.5
            else:
                impact = 0.3
            
            # Vulnerability based on borrower profile
            credit_score = transaction.get('credit_score', 700)
            if credit_score < 600:
                vulnerability = 0.9
            elif credit_score < 650:
                vulnerability = 0.7
            elif credit_score < 700:
                vulnerability = 0.5
            else:
                vulnerability = 0.3
            
            # Probability based on DTI ratio
            dti = amount / max(transaction.get('annual_income', 1), 1)
            if dti > 0.5:
                probability = 0.9
            elif dti > 0.3:
                probability = 0.6
            elif dti > 0.2:
                probability = 0.3
            else:
                probability = 0.1
            
        elif decision_type == FinancialDecisionType.TRADING:
            # Trading I×V×P
            volume = transaction.get('volume', 0)
            volatility = transaction.get('market_volatility', 0)
            
            impact = min(volume / 1000000, 1.0)  # Normalized by $1M
            vulnerability = volatility  # Market vulnerability
            probability = 0.5  # Trading risk probability
            
        elif decision_type == FinancialDecisionType.FRAUD_DETECTION:
            # Fraud I×V×P
            anomaly_score = transaction.get('anomaly_score', 0)
            amount = transaction.get('amount', 0)
            
            impact = min(amount / 10000, 1.0)  # Normalized by $10K
            vulnerability = 0.8  # Fraud victims are vulnerable
            probability = anomaly_score  # Likelihood of fraud
            
        elif decision_type == FinancialDecisionType.ACCOUNT_CLOSURE:
            # Account closure always high impact
            impact = 0.9
            vulnerability = 0.8  # Customer vulnerability
            probability = 0.9  # High certainty of impact
        
        # Protected class considerations increase vulnerability
        if transaction.get('affects_protected_class'):
            vulnerability = max(vulnerability, 0.8)
        
        return {
            'impact': impact,
            'vulnerability': vulnerability,
            'probability': probability
        }
    
    def process_loan_application(self, application: Dict) -> Dict:
        """Process loan application with Dual-Layer SPRL."""
        
        application['type'] = FinancialDecisionType.LOAN_APPROVAL
        application['prompt_timestamp'] = datetime.now().isoformat()  # t₀
        
        # Calculate I×V×P components
        ivp = self.calculate_ivp_components(application)
        application['i_v_p'] = ivp
        application['sprl_score'] = ivp['impact'] * ivp['vulnerability'] * ivp['probability']
        application['sprl_score'] = max(0.0001, min(0.9999, application['sprl_score']))
        
        # Check for fair lending considerations
        application['affects_protected_class'] = application.get('monitor_fairness', False)
        
        # Stakeholders
        application['stakeholders'] = [
            {'type': 'applicant', 'id': application.get('applicant_id')},
            {'type': 'institution', 'id': 'bank'},
            {'type': 'shareholders', 'id': 'investors'}
        ]
        
        def loan_decision_logic(context):
            sprl = context['sprl_score']
            credit_score = context.get('credit_score', 700)
            
            # Decision states: +1 (approve), 0 (pause), -1 (prohibit)
            if sprl > 0.8:
                return {
                    'decision_state': -1,
                    'decision': 'declined',
                    'reason': 'High risk profile',
                    'factors': ['DTI ratio', 'Credit score'],
                    'appeal_available': True
                }
            elif sprl > 0.5:
                return {
                    'decision_state': 0,  # Sacred Pause
                    'decision': 'manual_review',
                    'reason': 'Requires additional verification',
                    'factors': ['Income verification needed'],
                    'appeal_available': True
                }
            elif sprl > 0.3:
                return {
                    'decision_state': 1,
                    'decision': 'approved_with_conditions',
                    'reason': 'Moderate risk',
                    'interest_rate': 7.5 + (sprl * 5),
                    'conditions': ['Higher down payment required'],
                    'appeal_available': False
                }
            else:
                return {
                    'decision_state': 1,
                    'decision': 'approved',
                    'reason': 'Low risk profile',
                    'interest_rate': 5.0 + (sprl * 3),
                    'conditions': [],
                    'appeal_available': False
                }
        
        # Process with Dual-Layer SPRL
        result = self.framework.process_decision(
            context=application,
            ai_decision_func=loan_decision_logic
        )
        
        return result
    
    def process_trading_decision(self, trade: Dict) -> Dict:
        """Process high-frequency trading decision."""
        
        trade['type'] = FinancialDecisionType.TRADING
        trade['prompt_timestamp'] = datetime.now().isoformat()  # t₀
        
        # Calculate I×V×P
        ivp = self.calculate_ivp_components(trade)
        trade['i_v_p'] = ivp
        trade['sprl_score'] = max(0.0001, min(0.9999, 
            ivp['impact'] * ivp['vulnerability'] * ivp['probability']))
        
        # Decision based on SPRL
        if trade['sprl_score'] > 0.7:
            decision_state = 0  # Sacred Pause - needs review
            action = 'hold'
        elif trade['sprl_score'] > 0.9:
            decision_state = -1  # Prohibit
            action = 'block'
        else:
            decision_state = 1  # Proceed
            action = 'execute'
        
        decision = {
            'decision_id': f"TRADE-{random.randint(100000, 999999)}",
            'timestamp': datetime.now().isoformat(),
            'decision_state': decision_state,
            'action': action,
            'price': trade.get('price'),
            'volume': trade.get('volume'),
            'sprl_score': trade['sprl_score']
        }
        
        # Use batch logger for high-frequency trading
        self.trading_batch_logger.log_decision(trade, decision)
        
        return decision
    
    def detect_fraud(self, transaction: Dict) -> Dict:
        """Process fraud detection with Dual-Layer SPRL."""
        
        transaction['type'] = FinancialDecisionType.FRAUD_DETECTION
        transaction['prompt_timestamp'] = datetime.now().isoformat()  # t₀
        
        # Calculate I×V×P
        ivp = self.calculate_ivp_components(transaction)
        transaction['i_v_p'] = ivp
        transaction['sprl_score'] = max(0.0001, min(0.9999,
            ivp['impact'] * ivp['vulnerability'] * ivp['probability']))
        
        def fraud_detection_logic(context):
            sprl = context['sprl_score']
            
            if sprl > 0.9:
                return {
                    'decision_state': -1,  # Prohibit
                    'action': 'block',
                    'reason': 'High fraud probability',
                    'notify_customer': True,
                    'notify_fraud_team': True
                }
            elif sprl > 0.7:
                return {
                    'decision_state': 0,  # Sacred Pause
                    'action': 'challenge',
                    'reason': 'Suspicious activity',
                    'require_2fa': True,
                    'notify_fraud_team': True
                }
            elif sprl > 0.5:
                return {
                    'decision_state': 1,
                    'action': 'monitor',
                    'reason': 'Elevated risk',
                    'enhanced_monitoring': True,
                    'notify_fraud_team': False
                }
            else:
                return {
                    'decision_state': 1,
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
        
        print("LOAN APPLICATION PROCESSING - DUAL-LAYER SPRL")
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
            
            # Show I×V×P components
            ivp = app['i_v_p']
            print(f"  I×V×P Components:")
            print(f"    Impact: {ivp['impact']:.2f}")
            print(f"    Vulnerability: {ivp['vulnerability']:.2f}")
            print(f"    Probability: {ivp['probability']:.2f}")
            print(f"  SPRL Score: {app['sprl_score']:.4f}")
            
            # Decision state
            state = decision.get('decision_state', 1)
            state_str = {1: "PROCEED", 0: "SACRED PAUSE", -1: "PROHIBIT"}[state]
            print(f"  Decision State: {state_str}")
            print(f"  Decision: {decision['decision']}")
            print(f"  Reason: {decision['reason']}")
            
            if 'interest_rate' in decision:
                print(f"  Rate: {decision['interest_rate']:.2f}%")
            
            # Dual-layer tracking
            if state == 0:
                print(f"  ✓ Static Anchor set at Sacred Pause")
                print(f"    SA Hash: {result.get('sa_hash', 'N/A')[:12]}...")
            
            if result.get('dynamic_stream_active'):
                print(f"  ✓ Dynamic Stream active from t₀")
            
            if app.get('monitor_fairness'):
                print(f"  📊 Fair lending monitoring active")
            
            print()
    
    def demonstrate_trading_operations(self):
        """Simulate high-frequency trading with batch logging."""
        
        print("HIGH-FREQUENCY TRADING - DUAL-LAYER SPRL")
        print("-" * 70)
        print()
        
        print("Processing 100 trades with Dynamic Stream tracking...")
        start_time = time.time()
        
        trades_executed = 0
        trades_held = 0
        trades_blocked = 0
        
        for i in range(100):
            trade = {
                'symbol': random.choice(['AAPL', 'GOOGL', 'MSFT', 'AMZN']),
                'volume': random.randint(100, 10000),
                'price': random.uniform(100, 500),
                'market_volatility': random.random() * 0.5,
                'timestamp': time.time()
            }
            
            decision = self.process_trading_decision(trade)
            
            if decision['decision_state'] == 1:
                trades_executed += 1
            elif decision['decision_state'] == 0:
                trades_held += 1
            else:
                trades_blocked += 1
        
        # Flush batch logger
        self.trading_batch_logger.flush()
        
        elapsed = time.time() - start_time
        trades_per_second = 100 / elapsed
        
        print(f"Completed 100 trades in {elapsed:.3f} seconds")
        print(f"Rate: {trades_per_second:.0f} trades/second")
        print(f"Decision States:")
        print(f"  +1 (Executed): {trades_executed}")
        print(f"   0 (Held/Review): {trades_held}")
        print(f"  -1 (Blocked): {trades_blocked}")
        print()
        print("Dynamic Stream ensures continuous tracking")
        print("without impacting trading performance.")
        print()
    
    def demonstrate_fraud_detection(self):
        """Simulate fraud detection scenarios."""
        
        print("FRAUD DETECTION - DUAL-LAYER SPRL")
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
            
            result = self.detect_fraud(txn)
            decision = result['decision']
            
            # Show I×V×P and decision state
            ivp = txn.get('i_v_p', {})
            if ivp:
                print(f"  I×V×P: I={ivp['impact']:.2f}, V={ivp['vulnerability']:.2f}, P={ivp['probability']:.2f}")
            print(f"  SPRL: {txn.get('sprl_score', 0):.4f}")
            
            state = decision.get('decision_state', 1)
            state_str = {1: "PROCEED", 0: "SACRED PAUSE", -1: "PROHIBIT"}[state]
            print(f"  Decision State: {state_str}")
            print(f"  Action: {decision['action'].upper()}")
            print(f"  Reason: {decision['reason']}")
            
            if state == 0:
                print(f"  ✓ Static Anchor set for review")
            elif state == -1:
                print(f"  ⛔ Transaction blocked")
            
            print()
    
    def display_compliance_metrics(self):
        """Display financial compliance metrics."""
        
        print("=" * 70)
        print("DUAL-LAYER SPRL COMPLIANCE METRICS")
        print("=" * 70)
        
        stats = self.framework.get_performance_report()
        
        print(f"Total Financial Decisions: {stats.get('total_decisions', 0)}")
        print()
        print("Decision State Distribution:")
        print(f"  +1 (Proceed): {stats.get('proceed_count', 0)}")
        print(f"   0 (Sacred Pause): {stats.get('sacred_pause_count', 0)}")
        print(f"  -1 (Prohibit): {stats.get('prohibit_count', 0)}")
        print()
        print("Dual-Layer Metrics:")
        print(f"  Dynamic Stream Continuity: {stats.get('ds_continuity', 100)}%")
        print(f"  Static Anchors Set: {stats.get('sa_count', 0)}")
        print(f"  Average SA Write Time: {stats.get('sa_write_time_ms', 0):.1f}ms")
        print(f"  Lite Traces (near-miss): {stats.get('lite_trace_count', 0)}")
        print()
        print("Performance:")
        print(f"  Non-blocking Verified: {stats.get('non_blocking', True)}")
        print(f"  Average Latency: {stats.get('avg_latency_ms', 0):.1f}ms")
        print()
        print("Note: Thresholds are framework-enforced")
        print("Organizations cannot configure or game thresholds")
        print()


def main():
    """Run financial AI demonstration."""
    
    # Create financial AI system
    financial_ai = FinancialAI()
    
    # Demonstrate different financial decisions
    financial_ai.demonstrate_lending_decisions()
    financial_ai.demonstrate_trading_operations()
    financial_ai.demonstrate_fraud_detection()
    
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
    print("1. Thresholds are FRAMEWORK-ENFORCED (not configurable)")
    print("2. Financial institutions must:")
    print("   - Comply with SOX, GDPR, CCPA, etc.")
    print("   - Implement fair lending monitoring")
    print("   - Maintain 7-year retention minimum")
    print("   - Enable regulatory audit access")
    print()
    print("3. Dual-Layer SPRL provides:")
    print("   - Dynamic Stream from prompt arrival (t₀)")
    print("   - Static Anchor at Sacred Pause")
    print("   - I × V × P formula for risk")
    print("   - Non-blocking execution")
    print()
    print("This is NOT financial advice or software.")
    print()
    print("Framework Support: support@tml-goukassian.org")
    print("See Succession Charter: /TML-SUCCESSION-CHARTER.md")


if __name__ == "__main__":
    main()
