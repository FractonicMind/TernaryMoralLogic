# 🚀 TML Quick Start Guide

## Implement Sacred Pause for Ethical AI in 60 Minutes

* Estimated Time: 60 minutes

---

## ⏱️ What You'll Accomplish in 60 Minutes

By the end of this guide, you will have:
- ✅ Installed TML Framework
- ✅ Implemented Sacred Pause in a sample AI system
- ✅ Configured domain-specific thresholds
- ✅ Set up basic monitoring and audit trails
- ✅ Tested ethical decision-making scenarios
- ✅ Created your first Sacred Pause escalation

**No prior TML experience required!**

---

## 📋 Prerequisites (5 minutes)

### System Requirements
- Python 3.8 or higher
- 2GB free disk space
- Internet connection for package installation

### Check Python Version
```bash
python --version
# Should output: Python 3.8.x or higher
```

### Create Project Directory
```bash
mkdir my-tml-project
cd my-tml-project
```

### Set Up Virtual Environment
```bash
python -m venv tml_env

# Activate on Windows:
tml_env\Scripts\activate

# Activate on Mac/Linux:
source tml_env/bin/activate
```

---

## 🔧 Minute 0-10: Installation and Setup

### Install TML Framework
```bash
# Install via pip (recommended)
pip install tml-framework

# Or install from source
git clone https://github.com/Lev-Goukassian/TML-Framework.git
cd TML-Framework
pip install -e .
cd ..
```

### Verify Installation
```python
# test_install.py
import tml_framework
print(f"TML Version: {tml_framework.__version__}")
print("✅ TML successfully installed!")
```

Run:
```bash
python test_install.py
```

### Install Additional Dependencies
```bash
# For this tutorial
pip install numpy pandas flask
```

---

## 💡 Minute 10-20: Your First Sacred Pause

### Create Basic Implementation
```python
# my_first_sacred_pause.py
from tml_framework import TMLEngine, MoralContext

def main():
    # Step 1: Initialize TML Engine
    print("🚀 Initializing TML Engine...")
    tml = TMLEngine(domain="general")
    
    # Step 2: Create a moral context
    print("🎭 Creating moral context...")
    context = MoralContext(
        action="share_user_data_with_third_party",
        stakeholders=["user", "company", "third_party"],
        risk_level=0.6  # Moderate risk
    )
    
    # Step 3: Evaluate the decision
    print("🔍 Evaluating ethical decision...")
    decision = tml.evaluate(context)
    
    # Step 4: Handle the decision
    print(f"\n📊 Decision: {decision.state}")
    print(f"Confidence: {decision.confidence:.2%}")
    
    if decision.state == "SACRED_PAUSE":
        print("⏸️ Sacred Pause triggered!")
        print(f"Reason: {decision.pause_reason}")
        print("Action: Escalating for human review...")
    elif decision.state == "PROCEED":
        print("✅ Ethically cleared to proceed")
    else:  # STOP
        print("🛑 Action ethically prohibited")
    
    return decision

if __name__ == "__main__":
    decision = main()
```

### Run Your First Sacred Pause
```bash
python my_first_sacred_pause.py
```

**Expected Output:**
```
🚀 Initializing TML Engine...
🎭 Creating moral context...
🔍 Evaluating ethical decision...

📊 Decision: SACRED_PAUSE
Confidence: 45%
⏸️ Sacred Pause triggered!
Reason: Stakeholder conflict detected
Action: Escalating for human review...
```

---

## 🏥 Minute 20-30: Domain-Specific Implementation

### Healthcare AI Example
```python
# healthcare_ai.py
from tml_framework import TMLEngine, MoralContext, Stakeholder, Outcome

class HealthcareAISystem:
    def __init__(self):
        # Initialize with healthcare-specific configuration
        self.tml = TMLEngine(
            domain="healthcare",
            thresholds={
                "moral_complexity": 0.6,      # More sensitive
                "potential_harm": 0.4,         # Lower threshold for healthcare
                "stakeholder_conflict": 0.5,
                "novel_situation": 0.7,
                "reversibility": 0.3
            }
        )
        self.decisions_made = []
    
    def evaluate_treatment(self, patient_id, treatment_plan):
        """Evaluate ethical implications of treatment plan."""
        
        # Create detailed context
        context = MoralContext(
            action=f"recommend_treatment_{treatment_plan['name']}",
            stakeholders=[
                Stakeholder("patient", weight=0.4, 
                           vulnerabilities=["elderly", "chronic_condition"]),
                Stakeholder("family", weight=0.3),
                Stakeholder("medical_team", weight=0.2),
                Stakeholder("insurance", weight=0.1)
            ]
        )
        
        # Add potential outcomes
        context.add_outcome(
            Outcome(
                description="Treatment success",
                probability=treatment_plan['success_rate'],
                utility=0.9,
                harm_risk=treatment_plan['risk_level']
            )
        )
        
        # Evaluate
        decision = self.tml.evaluate(context)
        
        # Log decision
        self.decisions_made.append({
            'patient_id': patient_id,
            'treatment': treatment_plan['name'],
            'decision': decision.state,
            'confidence': decision.confidence,
            'timestamp': datetime.now()
        })
        
        return decision
    
    def handle_decision(self, decision, treatment_plan):
        """Handle TML decision appropriately."""
        
        if decision.state == "PROCEED":
            print(f"✅ Treatment approved: {treatment_plan['name']}")
            print(f"   Confidence: {decision.confidence:.2%}")
            # Implement treatment
            return self.implement_treatment(treatment_plan)
            
        elif decision.state == "SACRED_PAUSE":
            print(f"⏸️ Ethics review required for: {treatment_plan['name']}")
            print(f"   Reason: {decision.pause_reason}")
            # Escalate to medical ethics board
            return self.escalate_to_ethics_board(decision, treatment_plan)
            
        else:  # STOP
            print(f"🛑 Treatment not recommended: {treatment_plan['name']}")
            print(f"   Ethical concerns: {decision.reasoning}")
            # Document why treatment was rejected
            return self.document_rejection(decision, treatment_plan)
    
    def implement_treatment(self, plan):
        """Implement approved treatment."""
        print(f"   → Implementing {plan['name']}...")
        return {"status": "implemented", "plan": plan}
    
    def escalate_to_ethics_board(self, decision, plan):
        """Escalate to medical ethics board."""
        print(f"   → Creating ethics review ticket...")
        print(f"   → Notifying ethics board members...")
        print(f"   → Review deadline: 24 hours")
        return {"status": "under_review", "plan": plan, "ticket_id": "ETH-001"}
    
    def document_rejection(self, decision, plan):
        """Document rejected treatment."""
        print(f"   → Documenting ethical concerns...")
        print(f"   → Suggesting alternatives...")
        return {"status": "rejected", "plan": plan, "alternatives": ["palliative_care"]}

# Test the healthcare system
if __name__ == "__main__":
    from datetime import datetime
    
    # Initialize system
    healthcare_ai = HealthcareAISystem()
    
    # Test cases
    test_treatments = [
        {
            "name": "Aggressive Chemotherapy",
            "success_rate": 0.3,
            "risk_level": 0.8
        },
        {
            "name": "Standard Treatment",
            "success_rate": 0.7,
            "risk_level": 0.3
        },
        {
            "name": "Experimental Therapy",
            "success_rate": 0.5,
            "risk_level": 0.6
        }
    ]
    
    print("🏥 Healthcare AI Ethical Evaluation System\n")
    print("=" * 50)
    
    for treatment in test_treatments:
        print(f"\n📋 Evaluating: {treatment['name']}")
        print(f"   Success Rate: {treatment['success_rate']:.1%}")
        print(f"   Risk Level: {treatment['risk_level']:.1%}")
        
        decision = healthcare_ai.evaluate_treatment("PATIENT-001", treatment)
        result = healthcare_ai.handle_decision(decision, treatment)
        print(f"   Result: {result['status']}")
        print("=" * 50)
    
    # Show summary
    print(f"\n📊 Summary: {len(healthcare_ai.decisions_made)} decisions made")
    for d in healthcare_ai.decisions_made:
        print(f"   • {d['treatment']}: {d['decision']} ({d['confidence']:.1%} confidence)")
```

### Run Healthcare Example
```bash
python healthcare_ai.py
```

---

## 🔍 Minute 30-40: Configure Monitoring & Audit

### Set Up Basic Monitoring
```python
# monitoring_setup.py
from tml_framework import TMLEngine, TMLMonitor, AlertConfig
import json
from datetime import datetime

class MonitoredAISystem:
    def __init__(self, domain="general"):
        # Initialize engine
        self.engine = TMLEngine(domain=domain, audit_mode=True)
        
        # Configure alerts
        alert_config = AlertConfig(
            sacred_pause_threshold=0.15,  # Alert if >15% decisions pause
            bias_threshold=0.05,          # Alert on 5% demographic disparity
            response_time_threshold=200   # Alert if >200ms response
        )
        
        # Initialize monitor
        self.monitor = TMLMonitor(self.engine, alert_config)
        
        # Audit log file
        self.audit_file = f"audit_log_{datetime.now().strftime('%Y%m%d')}.json"
        
    def make_decision(self, context):
        """Make decision with full monitoring."""
        
        # Record start time
        start_time = datetime.now()
        
        # Evaluate
        decision = self.engine.evaluate(context)
        
        # Calculate response time
        response_time = (datetime.now() - start_time).total_seconds() * 1000
        
        # Track in monitor
        self.monitor.track_decision(decision, context)
        
        # Create audit record
        audit_record = {
            "timestamp": datetime.now().isoformat(),
            "context": {
                "action": context.action,
                "stakeholders": context.stakeholders,
                "risk_level": context.risk_level
            },
            "decision": {
                "state": str(decision.state),
                "confidence": decision.confidence,
                "reasoning": decision.reasoning
            },
            "metrics": {
                "response_time_ms": response_time
            }
        }
        
        # Write to audit log
        self.write_audit(audit_record)
        
        # Check for alerts
        self.check_alerts()
        
        return decision
    
    def write_audit(self, record):
        """Write audit record to file."""
        try:
            with open(self.audit_file, 'a') as f:
                f.write(json.dumps(record) + '\n')
        except Exception as e:
            print(f"⚠️ Audit write failed: {e}")
    
    def check_alerts(self):
        """Check for monitoring alerts."""
        metrics = self.engine.get_metrics(period="hour")
        
        if metrics.sacred_pause_rate > 0.15:
            print("🚨 ALERT: High Sacred Pause rate detected!")
            print(f"   Current rate: {metrics.sacred_pause_rate:.1%}")
            
        if metrics.avg_response_time > 200:
            print("🚨 ALERT: Slow response time detected!")
            print(f"   Average: {metrics.avg_response_time:.0f}ms")
    
    def generate_report(self):
        """Generate monitoring report."""
        print("\n📊 MONITORING REPORT")
        print("=" * 40)
        
        # Get metrics
        daily_metrics = self.engine.get_metrics(period="day")
        
        print(f"Total Decisions: {daily_metrics.total_decisions}")
        print(f"Sacred Pauses: {daily_metrics.sacred_pauses} ({daily_metrics.sacred_pause_rate:.1%})")
        print(f"Average Response Time: {daily_metrics.avg_response_time:.0f}ms")
        print(f"Audit Records Written: {daily_metrics.audit_records}")
        
        # Check for bias
        bias_report = self.monitor.detect_bias(window="day")
        if bias_report.bias_detected:
            print("\n⚠️ BIAS DETECTED:")
            for finding in bias_report.findings:
                print(f"   • {finding}")
        else:
            print("\n✅ No bias detected")

# Test monitoring system
if __name__ == "__main__":
    from tml_framework import MoralContext
    
    # Create monitored system
    system = MonitoredAISystem(domain="finance")
    
    # Test scenarios
    test_scenarios = [
        MoralContext(
            action="approve_loan",
            stakeholders=["applicant", "bank", "community"],
            risk_level=0.3
        ),
        MoralContext(
            action="deny_credit_increase",
            stakeholders=["customer", "bank"],
            risk_level=0.7
        ),
        MoralContext(
            action="flag_suspicious_transaction",
            stakeholders=["account_holder", "bank", "authorities"],
            risk_level=0.8
        )
    ]
    
    print("🔍 Running Monitored AI System\n")
    
    # Process decisions
    for i, context in enumerate(test_scenarios, 1):
        print(f"Decision {i}: {context.action}")
        decision = system.make_decision(context)
        print(f"   Result: {decision.state}")
        print()
    
    # Generate report
    system.generate_report()
    
    print(f"\n📁 Audit log saved to: {system.audit_file}")
```

### Run Monitoring Example
```bash
python monitoring_setup.py
```

---

## 🌐 Minute 40-50: Create REST API

### Build Simple API Server
```python
# api_server.py
from flask import Flask, request, jsonify
from tml_framework import TMLEngine, MoralContext
import logging

# Initialize Flask app
app = Flask(__name__)

# Initialize TML engine
tml_engine = TMLEngine(domain="general")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "framework": "TML",
        "version": "2.0.0"
    })

@app.route('/evaluate', methods=['POST'])
def evaluate_decision():
    """Evaluate moral decision."""
    try:
        # Parse request
        data = request.json
        
        # Create context from request
        context = MoralContext(
            action=data['action'],
            stakeholders=data.get('stakeholders', []),
            risk_level=data.get('risk_level', 0.5)
        )
        
        # Evaluate
        decision = tml_engine.evaluate(context)
        
        # Log decision
        logger.info(f"Decision for '{data['action']}': {decision.state}")
        
        # Return response
        return jsonify({
            "decision": str(decision.state),
            "confidence": decision.confidence,
            "reasoning": decision.reasoning,
            "pause_reason": decision.pause_reason
        })
        
    except Exception as e:
        logger.error(f"Evaluation failed: {e}")
        return jsonify({"error": str(e)}), 400

@app.route('/metrics', methods=['GET'])
def get_metrics():
    """Get system metrics."""
    period = request.args.get('period', 'day')
    metrics = tml_engine.get_metrics(period=period)
    
    return jsonify({
        "period": period,
        "total_decisions": metrics.total_decisions,
        "sacred_pauses": metrics.sacred_pauses,
        "sacred_pause_rate": metrics.sacred_pause_rate,
        "avg_response_time_ms": metrics.avg_response_time
    })

@app.route('/escalate', methods=['POST'])
def escalate_pause():
    """Escalate Sacred Pause for review."""
    data = request.json
    
    # Log escalation
    logger.info(f"Escalating Sacred Pause: {data.get('reason')}")
    
    # In production, this would trigger actual escalation
    return jsonify({
        "status": "escalated",
        "ticket_id": "ESC-" + str(hash(data.get('reason', '')) % 10000),
        "review_deadline": "24 hours",
        "assigned_to": "ethics_board"
    })

if __name__ == '__main__':
    print("🚀 Starting TML API Server...")
    print("📍 Server running at http://localhost:5000")
    print("📚 API Endpoints:")
    print("   • GET  /health     - Health check")
    print("   • POST /evaluate   - Evaluate decision")
    print("   • GET  /metrics    - Get metrics")
    print("   • POST /escalate   - Escalate Sacred Pause")
    print("\nPress Ctrl+C to stop")
    
    app.run(debug=True, port=5000)
```

### Test API with curl
```bash
# Start server
python api_server.py

# In another terminal, test endpoints:

# Health check
curl http://localhost:5000/health

# Evaluate decision
curl -X POST http://localhost:5000/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "action": "share_medical_records",
    "stakeholders": ["patient", "researcher", "hospital"],
    "risk_level": 0.7
  }'

# Get metrics
curl http://localhost:5000/metrics?period=hour
```

---

## ✅ Minute 50-60: Test & Validate

### Create Test Suite
```python
# test_sacred_pause.py
import unittest
from tml_framework import TMLEngine, MoralContext

class TestSacredPause(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.engine = TMLEngine(domain="general")
    
    def test_low_risk_proceeds(self):
        """Test that low risk actions proceed."""
        context = MoralContext(
            action="send_newsletter",
            stakeholders=["subscribers"],
            risk_level=0.1
        )
        decision = self.engine.evaluate(context)
        self.assertEqual(decision.state, "PROCEED")
    
    def test_high_risk_triggers_pause(self):
        """Test that high risk triggers Sacred Pause."""
        context = MoralContext(
            action="delete_user_data",
            stakeholders=["user", "company", "regulators"],
            risk_level=0.8
        )
        decision = self.engine.evaluate(context)
        self.assertIn(decision.state, ["SACRED_PAUSE", "STOP"])
    
    def test_vulnerable_population_protection(self):
        """Test enhanced protection for vulnerable groups."""
        context = MoralContext(
            action="collect_child_data",
            stakeholders=["minor", "parents", "school"],
            risk_level=0.5
        )
        # Add vulnerability
        context.add_stakeholder("minor", weight=1.5, vulnerabilities=["age<13"])
        
        decision = self.engine.evaluate(context)
        # Should be more cautious with minors
        self.assertNotEqual(decision.state, "PROCEED")
    
    def test_audit_trail_creation(self):
        """Test that audit trails are created."""
        context = MoralContext(
            action="test_action",
            stakeholders=["test_user"],
            risk_level=0.5
        )
        decision = self.engine.evaluate(context)
        
        # Check audit trail exists
        self.assertIsNotNone(decision.audit_trail)
        self.assertIn("timestamp", decision.audit_trail)
        self.assertIn("context", decision.audit_trail)

if __name__ == '__main__':
    # Run tests
    print("🧪 Running Sacred Pause Tests\n")
    unittest.main(verbosity=2)
```

### Run Tests
```bash
python test_sacred_pause.py
```

### Validation Checklist
```python
# validation_checklist.py
print("""
✅ TML IMPLEMENTATION VALIDATION CHECKLIST
==========================================

Core Functionality:
[ ] TML Framework installed successfully
[ ] Sacred Pause triggers on high-risk decisions
[ ] Three states work correctly (PROCEED, SACRED_PAUSE, STOP)
[ ] Stakeholder analysis functioning
[ ] Risk assessment operational

Safety Features:
[ ] Vulnerable population protection active
[ ] Audit trails being created
[ ] Cannot bypass Sacred Pause
[ ] Escalation mechanism works

Monitoring:
[ ] Decisions being tracked
[ ] Metrics accessible
[ ] Bias detection operational
[ ] Alert system functioning

API/Integration:
[ ] REST API responding
[ ] Can evaluate decisions via API
[ ] Metrics endpoint working
[ ] Error handling robust

Documentation:
[ ] This Quick Start completed
[ ] MANDATORY.md reviewed
[ ] API documentation accessible
[ ] FAQ available for reference

Next Steps:
1. Review MANDATORY.md for safety requirements
2. Configure domain-specific thresholds
3. Set up production monitoring
4. Train your team on Sacred Pause
5. Implement in your AI system

🎉 CONGRATULATIONS! You've implemented TML in 60 minutes!

For questions: support@tml-goukassian.org
For ethics emergencies: ethics@tml-goukassian.org
""")
```

---

## 🎓 What You've Learned

In just 60 minutes, you've:

1. **Installed** the TML Framework
2. **Implemented** Sacred Pause in multiple contexts
3. **Configured** domain-specific ethical thresholds
4. **Created** monitoring and audit systems
5. **Built** a REST API for integration
6. **Tested** your implementation

You now have a working foundation for ethical AI decision-making using Sacred Pause!

---

## 📚 Next Steps

### Immediate Actions
1. **Read MANDATORY.md** - Critical safety requirements
2. **Review FAQs** - Common questions answered
3. **Explore examples/** - More implementation patterns

### This Week
1. **Customize for your domain** - Adjust thresholds
2. **Set up production monitoring** - Full metrics
3. **Train your team** - Sacred Pause principles

### This Month
1. **Run pilot program** - Test in production
2. **Gather feedback** - Refine thresholds
3. **Contribute back** - Share your learnings

---

## 🆘 Getting Help

### Documentation
- [Complete API Reference](./api/complete_api_reference.md)
- [MANDATORY Safety Guidelines](./MANDATORY.md)
- [General FAQ](./GENERAL_FAQ.md)
- [License FAQ](./LICENSE_FAQ.md)

### Community Support
- GitHub: https://github.com/FractonicMind/TernaryMoralLogic
- Forum: https://community.tml-goukassian.org
- Email: support@tml-goukassian.org

### Emergency Ethics Support
- 24/7 Hotline: ethics@tml-goukassian.org
- Response time: < 4 hours

---

## 🏆 Success Metrics

Your TML implementation is successful when:
- ✅ Sacred Pause triggers appropriately (1-5% of decisions)
- ✅ No harmful decisions proceed without review
- ✅ Stakeholder trust increases
- ✅ Audit trail is complete and immutable
- ✅ Team understands when and why pauses occur

---

*Quick Start Guide Version: 1.0.0*
*Framework Version: TML 2.0.0*
*Time to Implementation: 60 minutes*

**"Every Sacred Pause is a moment of ethical reflection that makes AI more human."** - Lev Goukassian

Created by Lev Goukassian
* ORCID: 0009-0006-5966-1243  
* Email: leogouk@gmail.com
* Successor Contact: support@tml-goukassian.org
  
