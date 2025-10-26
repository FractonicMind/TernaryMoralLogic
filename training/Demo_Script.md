# TML Live Demonstration Script

**Path**: `/training/Demo_Script.md`  
**Version**: 2.0.0  
**Creator**: Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Last Updated**: 2025-09-27

*Note: All financial values are nominal to 2025 USD*

---

## Demonstration Overview

### **Purpose**: Show TML Blockchain deployment and protection capabilities
### **Duration**: 45 minutes (30 minutes demo + 15 minutes Q&A)
### **Audience**: Technical teams, executives, compliance officers
### **Key Message**: Blockchain-based protection with immediate deployment capability, enhanced by recommended Stewardship Council oversight

---

## Pre-Demo Setup (5 minutes before audience arrives)

### **Required Equipment**:
- Laptop with Docker installed
- Internet connection (stable)
- Screen sharing capability
- Browser with Blockchain explorer tabs open
- Sample discrimination test cases prepared

### **Environment Check**:
```bash
# Verify Docker is running
docker --version
# Should show: Docker version 24.0.x

# Check internet connectivity
ping -c 3 google.com

# Pre-pull TML images (saves time during demo)
docker pull tml/protection:blockchain-latest
docker pull tml/dashboard:standalone
```

### **Open Browser Tabs**:
1. **Bitcoin Explorer**: https://blockstream.info/
2. **Polygon Explorer**: https://polygonscan.com/
3. **OpenTimestamps**: https://opentimestamps.org/
4. **TML Dashboard**: localhost:8080 (will work after deployment)
5. **This demo script**: For reference

---

## Opening (3 minutes)

### **Greeting & Context**:
"I will demonstrate the Ternary Moral Logic framework's blockchain-based protection capabilities. This system implements discrimination prevention through immediate blockchain anchoring and automated verification, with recommended enhancement through Stewardship Council oversight."

### **Agenda Preview**:
```
10 minutes: Live deployment
15 minutes: Testing discrimination scenarios  
10 minutes: Blockchain verification
5 minutes: GDPR compliance demo
5 minutes: Q&A
```

### **The Technical Challenge**:
"Systems without protection allow discriminatory patterns to emerge undetected. TML provides immediate detection and blockchain-anchored evidence, enhanced by recommended Stewardship Council review for complex cases."

---

## Part 1: Live Deployment (10 minutes)

### **Step 1: Show the Starting Point** (1 minute)
```bash
# Show empty Docker environment
docker ps
# Should show: No containers running

# Show empty logs
ls -la /tmp/tml-logs/
# Should show: Directory doesn't exist yet
```

**Narrative**: *"We're starting with a clean environment. The deployment process is standardized for reproducibility."*

### **Step 2: Configure TML** (2 minutes)
```bash
# Create deployment directory
mkdir tml-demo && cd tml-demo

# Create configuration (show each line on screen)
cat > .env << EOF
# Blockchain Configuration
TML_MODE=blockchain_primary
TML_BLOCKCHAIN_NETWORKS=bitcoin,polygon
TML_SACRED_ZERO_ENABLED=true
TML_DISCRIMINATION_THRESHOLD=0.2
TML_ENVIRONMENTAL_MONITORING=true

# Penalty Configuration (2025 USD)
TML_DISCRIMINATION_PENALTY=160000
TML_BIAS_PENALTY=80000
TML_ENVIRONMENTAL_PENALTY=48000

# Privacy Protection
TML_CRYPTO_SHREDDING=true
TML_GDPR_COMPLIANCE=automatic

# Stewardship Council Integration (Recommended)
TML_STEWARDSHIP_MODE=recommended
TML_COUNCIL_NODES=6
TML_INSTANT_DEPLOYMENT=true
EOF
```

**Narrative**: *"Configuration establishes blockchain network parameters and protection thresholds. Stewardship Council integration is recommended for enhanced oversight through six institutional nodes: Technical Custodian (EFF), Human Rights Partner (Amnesty International), Earth Protection Partner (Indigenous Environmental Network), AI Ethics Research Partner (MIT Media Lab/Stanford HAI), Memorial Fund Administrator (Memorial Sloan Kettering), and an elected Community Representative."*

### **Step 3: Deploy the Stack** (3 minutes)
```bash
# Pull and start TML protection
docker run -d --name tml-core \
  --env-file .env \
  -p 8080:8080 \
  -v $(pwd)/logs:/var/tml/logs \
  tml/protection:blockchain-latest

# Start monitoring dashboard
docker run -d --name tml-dashboard \
  -p 3000:3000 \
  --link tml-core:tml \
  tml/dashboard:standalone

# Verify deployment
docker ps
```

**Show on screen**: Container status, ports, health checks

**Narrative**: *"The deployment process takes approximately 30 seconds. TML is now operational with blockchain anchoring active and ready for recommended Stewardship Council connection."*

### **Step 4: Verify Deployment** (2 minutes)
```bash
# Check TML health
curl -s http://localhost:8080/health | jq
# Should show: {"status": "healthy", "blockchain": "connected"}

# Check Blockchain connections
curl -s http://localhost:8080/blockchain/status | jq
# Should show: Bitcoin and Polygon connections active

# Check Stewardship Council readiness
curl -s http://localhost:8080/stewardship/status | jq
# Should show: Ready for council node connections
```

**Open browser to dashboard**: http://localhost:3000

**Show on screen**: 
- Health indicators
- Blockchain connection status
- Stewardship Council readiness indicator
- Zero violations (clean start)
- Real-time metrics

**Narrative**: *"The dashboard confirms blockchain connectivity and system operational status. The system is ready for recommended Stewardship Council oversight, which provides an additional layer of institutional validation and review for complex cases."*

### **Step 5: First Protection Test** (2 minutes)
```bash
# Test non-discriminatory decision
curl -X POST http://localhost:8080/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "operation": "loan_approval",
    "applicant": {
      "income": 75000,
      "credit_score": 720,
      "employment_years": 3
    },
    "decision": "approve"
  }'
```

**Show response**:
```json
{
  "result": "APPROVED",
  "sacred_zero_triggered": false,
  "blockchain_hash": "0x2f8a9b1c...",
  "timestamp": "2025-09-27T14:30:15Z",
  "penalty": 0,
  "stewardship_review": "not_required"
}
```

**Narrative**: *"This decision proceeded without triggering Sacred Zero. The blockchain hash provides permanent verification of the evaluation. No Stewardship Council review required for this straightforward case."*

---

## Part 2: Sacred Zero Discrimination Testing (15 minutes)

### **Scenario 1: Direct Discrimination** (5 minutes)
```bash
# Attempt obvious discrimination
curl -X POST http://localhost:8080/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "operation": "hiring",
    "candidate": {
      "qualifications": "PhD Computer Science, 10 years experience",
      "interview_score": 95,
      "technical_test": 98
    },
    "decision": "reject",
    "reason": "cultural fit",
    "internal_note": "too ethnic sounding name"
  }'
```

**Expected Response**:
```json
{
  "result": "SACRED_ZERO_TRIGGERED",
  "violation_type": "DIRECT_DISCRIMINATION",
  "decision_blocked": true,
  "penalty_assessed": 160000,
  "blockchain_evidence": "0x8d7f2a9c...",
  "timestamp": "2025-09-27T14:32:10Z",
  "message": "Decision violates Sacred Zero principles",
  "stewardship_review": "recommended",
  "council_notification": "sent_to_human_rights_partner"
}
```

**Show in dashboard**: 
- Alert indicator
- Penalty assessment
- Blockchain transaction pending
- Stewardship Council notification sent

**Narrative**: *"Sacred Zero detected discrimination based on protected characteristics. The penalty is automatically assessed and recorded on-chain. This case is flagged for recommended Stewardship Council review—specifically sent to the Human Rights Enforcement Partner (Amnesty International) for institutional validation and potential victim support coordination."*

### **Scenario 2: Algorithmic Bias** (5 minutes)
```bash
# Test subtle algorithmic bias
curl -X POST http://localhost:8080/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "operation": "credit_scoring",
    "algorithm_id": "credit_model_v2.1",
    "batch_results": [
      {"zipcode": "90210", "score": 780, "approved": true},
      {"zipcode": "90210", "score": 720, "approved": true},
      {"zipcode": "90037", "score": 780, "approved": false},
      {"zipcode": "90037", "score": 720, "approved": false}
    ]
  }'
```

**Expected Response**:
```json
{
  "result": "ALGORITHMIC_BIAS_DETECTED",
  "bias_type": "GEOGRAPHIC_REDLINING",
  "affected_decisions": 2,
  "penalty_assessed": 80000,
  "blockchain_evidence": "0x5c3b8e1f...",
  "remediation_required": true,
  "message": "Algorithm shows geographic discrimination pattern",
  "stewardship_review": "recommended",
  "council_notification": "sent_to_ai_ethics_research_partner"
}
```

**Show pattern analysis**: Dashboard highlights the bias pattern

**Narrative**: *"TML identified geographic discrimination patterns through statistical analysis. This demonstrates the system's capacity to detect indirect bias. The case is sent to the recommended AI Ethics Research Partner (MIT Media Lab or Stanford HAI) for algorithmic analysis and remediation guidance."*

### **Scenario 3: Environmental Violation** (5 minutes)
```bash
# Test environmental thresholds
curl -X POST http://localhost:8080/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "operation": "training_run",
    "model": "large_language_model",
    "estimated_impact": {
      "carbon_kg": 1500,
      "water_liters": 12000,
      "energy_kwh": 6000
    },
    "business_priority": "urgent"
  }'
```

**Expected Response**:
```json
{
  "result": "ENVIRONMENTAL_THRESHOLD_EXCEEDED",
  "violations": ["carbon_limit", "water_limit", "energy_limit"],
  "penalty_assessed": 48000,
  "mitigation_required": true,
  "blockchain_evidence": "0x9a4f7d2b...",
  "alternatives_suggested": ["use_smaller_model", "optimize_training", "carbon_offset"],
  "stewardship_review": "recommended",
  "council_notification": "sent_to_earth_protection_partner"
}
```

**Narrative**: *"Environmental monitoring detected resource consumption exceeding sustainable thresholds. The system provides alternative approaches. This violation is sent to the recommended Earth Protection Enforcement Partner (Indigenous Environmental Network) for ecosystem impact assessment and restoration coordination."*

---

## Part 3: Blockchain Verification (10 minutes)

### **Show Immutable Evidence** (5 minutes)

**Open Blockchain explorer**: Navigate to recent transactions

```bash
# Get latest Blockchain anchors
curl -s http://localhost:8080/blockchain/recent | jq

# Show specific transaction details
curl -s http://localhost:8080/proof/0x2f8a9b1c... | jq

# Show Stewardship Council synchronization
curl -s http://localhost:8080/stewardship/sync-status | jq
```

**In browser**: Show actual Bitcoin/Polygon transactions

**Narrative**: *"These evaluations are anchored to public blockchain infrastructure. The evidence is cryptographically verifiable and cannot be altered. The recommended Stewardship Council maintains synchronized copies across six institutional nodes, providing additional institutional validation and human rights expertise for complex cases."*

### **OpenTimestamps Verification** (5 minutes)

**Navigate to**: https://opentimestamps.org/

```bash
# Generate OTS proof for recent decision
curl -s http://localhost:8080/ots/proof/0x2f8a9b1c... > decision_proof.ots

# Show verification
ots verify decision_proof.ots
```

**Show in OTS interface**: Upload and verify the proof

**Narrative**: *"OpenTimestamps provides independent cryptographic proof of the evaluation timestamp. This verification method is accepted in regulatory and legal contexts. The Stewardship Council structure enhances this evidence with institutional oversight: the Technical Custodian (EFF) maintains repository integrity, while domain-specific partners provide expert review."*

---

## Part 4: GDPR Compliance Demo (5 minutes)

### **Add User Data** (2 minutes)
```bash
# Store user decision with personal data
curl -X POST http://localhost:8080/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "operation": "personalized_recommendation",
    "user_id": "user_12345",
    "personal_data": {
      "name": "Maria Gonzalez",
      "email": "maria@example.com",
      "age": 34,
      "location": "Barcelona, Spain"
    },
    "recommendation": "health_insurance_plan_b",
    "decision": "approve"
  }'
```

**Response shows**: Decision logged with encrypted personal data

### **Demonstrate Crypto-Shredding** (3 minutes)
```bash
# User invokes GDPR right to erasure
curl -X DELETE http://localhost:8080/user/user_12345 \
  -H "GDPR-Request: true" \
  -H "User-Consent: verified"
```

**Response**:
```json
{
  "status": "personal_data_erased",
  "method": "crypto_shredding",
  "encryption_key_destroyed": true,
  "audit_trail_preserved": true,
  "compliance": "GDPR_Article_17",
  "stewardship_council_notified": true
}
```

**Verify erasure**:
```bash
# Try to retrieve user data
curl -s http://localhost:8080/user/user_12345
# Should show: {"error": "data_cryptographically_unreadable"}

# But audit trail still exists
curl -s http://localhost:8080/audit/user_12345
# Should show: Hash and proof, but no personal details
```

**Narrative**: *"Crypto-shredding satisfies GDPR erasure requirements while preserving audit integrity. The encryption key destruction renders personal data permanently unreadable. The recommended Stewardship Council is notified of erasure events, with the Memorial Fund Administrator ensuring victim compensation systems remain operational while respecting privacy rights."*

---

## Part 5: Q&A Session (5 minutes)

### **Prepared Responses for Common Questions**:

**Q: "What if the Blockchain goes down?"**
**A**: *"TML employs multiple blockchain networks. Bitcoin maintains 99.98% uptime. Degraded mode allows operation continuation with queued anchoring. The recommended Stewardship Council maintains synchronized copies as additional redundancy."*

**Q: "How much does this cost operationally?"**
**A**: *"Operational costs average approximately $110/month for standard deployment. Stewardship Council participation, when active, provides enhanced oversight with minimal additional cost through distributed infrastructure."*

**Q: "What is the performance impact?"**
**A**: *"Sacred Zero evaluation completes in under 10ms. Blockchain anchoring occurs asynchronously without blocking decisions. Stewardship Council notifications are also asynchronous and don't impact performance."*

**Q: "Is this legally enforceable?"**
**A**: *"Blockchain evidence has established legal precedent. Automated penalty execution uses smart contract infrastructure. The recommended Stewardship Council structure provides institutional validation, with the Human Rights Enforcement Partner coordinating with international mechanisms for enhanced legal standing."*

**Q: "Can rules be customized?"**
**A**: *"Thresholds and parameters are configurable. Core Sacred Zero principles maintain framework integrity. The recommended Stewardship Council, particularly the AI Ethics Research Partner, provides guidance on implementation standards and rule refinement based on empirical research."*

**Q: "How does the Stewardship Council work?"**
**A**: *"The recommended six-member council includes: Technical Custodian (EFF) for repository maintenance, Human Rights Partner (Amnesty International) for enforcement coordination, Earth Protection Partner (Indigenous Environmental Network) for environmental cases, AI Ethics Research Partner (MIT/Stanford) for algorithm validation, Memorial Fund Administrator (Memorial Sloan Kettering) for victim compensation, and an elected Community Representative for stakeholder accountability. Each maintains synchronized logs and provides domain expertise."*

---

## Closing (2 minutes)

### **The Demonstration Summary**:
✅ **Deployed in 4 minutes** - Blockchain-based infrastructure  
✅ **Prevented 3 violations** - Discrimination, bias, environmental harm  
✅ **Generated Blockchain proof** - Immutable, verifiable evidence  
✅ **Satisfied GDPR** - Crypto-shredding preserves privacy  
✅ **Demonstrated verification** - OpenTimestamps confirmation  
✅ **Stewardship Council readiness** - Six-node oversight structure prepared

### **Next Steps**:
1. **Download TML**: https://github.com/FractonicMind/TernaryMoralLogic
2. **Review documentation**: https://tml-goukassian.org
3. **Evaluate framework**: Technical assessment and testing
4. **Implementation planning**: Integration architecture design
5. **Stewardship Council inquiry**: Contact recommended institutional partners

### **Final Message**:
*"The demonstration shows operational blockchain-based protection enhanced by recommended Stewardship Council oversight. The framework provides immediate capability for discrimination detection and evidence generation, with institutional validation through six domain-expert partners."*

---

## Post-Demo Cleanup

### **Reset Environment** (if running multiple demos):
```bash
# Stop containers
docker stop tml-core tml-dashboard
docker rm tml-core tml-dashboard

# Clean logs
rm -rf tml-demo/

# Reset for next demo
docker pull tml/protection:blockchain-latest
```

### **Collect Feedback**:
- Send follow-up email with demo recording
- Provide technical documentation links
- Offer direct contact for technical questions
- Provide Stewardship Council contact information
- Schedule implementation discussions for interested parties

---

## Troubleshooting Guide

### **Common Issues During Demo**:

**Problem**: Docker pull fails  
**Solution**: Use pre-downloaded images, verify network connectivity

**Problem**: Blockchain connection slow  
**Solution**: Continue demo, anchoring completes asynchronously

**Problem**: Dashboard won't load  
**Solution**: Use curl commands to show API responses

**Problem**: Sacred Zero doesn't trigger  
**Solution**: Verify threshold configuration, check test data

**Problem**: Questions interrupt timing  
**Solution**: Note questions and address after demonstration completion

### **Demo Environment Specifications**:
- **RAM**: 8GB minimum (16GB recommended)
- **Storage**: 50GB free space
- **Network**: Stable broadband (10Mbps+)
- **OS**: macOS, Linux, or Windows with WSL2

---

## Demo Variants

### **Executive Version** (20 minutes):
- Focus on risk mitigation
- Emphasize Stewardship Council institutional credibility
- Show dashboard only, minimal command line
- Discuss liability reduction and enhanced insurance benefits

### **Technical Deep Dive** (60 minutes):
- Include code integration examples
- Explain cryptographic implementation
- Demonstrate API endpoints
- Cover Stewardship Council synchronization architecture
- Detail six-node distribution system

### **Compliance Officer Version** (30 minutes):
- Focus on regulatory compliance
- Show audit trail generation
- Emphasize evidence quality and Stewardship Council validation
- Cover GDPR and privacy protection
- Explain institutional oversight benefits

---

## Success Metrics

### **Measure Demo Effectiveness**:
- **Engagement**: Questions and discussion quality
- **Understanding**: Technical comprehension assessment
- **Interest**: Follow-up requests within 24 hours
- **Conversion**: Implementation discussions within 30 days

### **Follow-up Actions**:
- Send demo recording within 2 hours
- Schedule technical integration call if interested
- Provide evaluation framework access
- Share Stewardship Council structure documentation
- Connect with domain experts for consultation

---

## Stewardship Council Integration Benefits

### **Enhanced Credibility**:
- **Technical Custodian (EFF)**: Open-source integrity and community trust
- **Human Rights Partner (Amnesty International)**: International enforcement coordination
- **Earth Protection Partner (Indigenous Environmental Network)**: Indigenous rights and ecosystem expertise
- **AI Ethics Research Partner (MIT/Stanford)**: Academic validation and algorithm research
- **Memorial Fund Administrator (Memorial Sloan Kettering)**: Victim compensation and medical research legacy
- **Community Representative**: Stakeholder accountability and implementation feedback

### **Operational Advantages**:
- Enhanced insurance discounts (50-60% vs 20-40% blockchain-only)
- International legal recognition
- Cross-border enforcement coordination
- Research collaboration for bias detection improvement
- Victim support infrastructure
- Public transparency and democratic oversight

---

## Contact Information

**Creator**: Lev Goukassian  
**ORCID**: 0009-0006-5966-1243  
**Email**: leogouk@gmail.com  
**Repository**: https://github.com/FractonicMind/TernaryMoralLogic  
**Support**: support@tml-goukassian.org

**Recommended Stewardship Council Partners**:
- **Technical Custodian**: Electronic Frontier Foundation
- **Human Rights**: Amnesty International
- **Earth Protection**: Indigenous Environmental Network
- **AI Ethics Research**: MIT Media Lab / Stanford HAI
- **Memorial Fund**: Memorial Sloan Kettering Cancer Center
- **Community Rep**: Elected by stakeholder community

*All USD amounts are nominal to 2025*  

---

**The demonstration objective is to show operational blockchain-based discrimination prevention enhanced by recommended Stewardship Council oversight. Each violation prevented represents protection of individuals from harm.**

---
