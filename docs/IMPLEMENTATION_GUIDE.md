# TML Implementation Guide

**Path**: `/docs/IMPLEMENTATION_GUIDE.md`  
**Version**: 6.0.0  
**Last Updated**: October 2025

---

## Quick Start (10 Minutes)

### Prerequisites

- Python 3.9+
- Docker (optional, recommended)
- Blockchain RPC endpoints (Bitcoin, Ethereum, Polygon)
- TEE or HSM access (AWS Nitro Enclaves, Azure Confidential Computing, or physical HSM)

### Installation

```bash
# Install TML blockchain framework
pip install tml-blockchain

# Or use Docker
docker pull tmlframework/blockchain:latest
```

### Basic Configuration

```python
from tml_blockchain import AlwaysMemory, BlockchainAnchors

# Configure multi-chain anchoring
anchors = BlockchainAnchors(
    bitcoin_rpc="https://bitcoin.node.example.com",
    ethereum_rpc="https://eth.node.example.com",
    polygon_rpc="https://polygon.node.example.com",
    opentimestamps=True
)

# Initialize Always Memory engine
memory = AlwaysMemory(
    blockchain_anchors=anchors,
    tee_platform="aws_nitro",  # or "azure_cc", "hsm"
    sacred_zero_triggers="standard"  # Loads 66 documents
)

# Start logging
@memory.always_log
def ai_decision(input_data):
    result = your_ai_model.predict(input_data)
    return result
```

**Deployment time**: 10 minutes  
**Protection active**: Immediately

---

## Core Architecture

### Always Memory Engine

Every AI action creates an immutable log before execution:

```python
class AlwaysMemory:
    """Core logging and anchoring engine"""
    
    def __init__(self, blockchain_anchors, tee_platform, sacred_zero_triggers):
        self.anchors = blockchain_anchors
        self.tee = TEEManager(tee_platform)
        self.triggers = load_triggers(sacred_zero_triggers)
        
    def always_log(self, func):
        """Decorator ensuring pre-action logging"""
        def wrapper(*args, **kwargs):
            # Create log BEFORE action
            log = self.create_log(func, args, kwargs)
            
            # Seal in TEE
            sealed_log = self.tee.seal(log)
            
            # Anchor to blockchains (async)
            self.anchors.anchor_async(sealed_log)
            
            # Execute action
            result = func(*args, **kwargs)
            
            # Update log with result
            self.finalize_log(sealed_log, result)
            
            return result
        return wrapper
```

### Sacred Zero Detection

Automatic triggers for moral complexity:

```yaml
sacred_zero_triggers:
  human_rights:
    - source: "UDHR_articles.yaml"
      documents: 26
      threshold: "any_violation"
    
  earth_protection:
    - source: "planetary_treaties.yaml"
      documents: 20
      threshold: "irreversibility > 0.7"
    
  discrimination:
    - source: "protected_classes.yaml"
      threshold: "disparate_impact > 0.20"
    
  vulnerable_populations:
    - source: "protection_rules.yaml"
      multiplier: 1.5
```

### Blockchain Anchoring

Multi-chain redundancy for maximum resilience:

```python
class BlockchainAnchors:
    """Multi-chain anchoring system"""
    
    def anchor_batch(self, merkle_root: bytes):
        """Anchor to multiple chains simultaneously"""
        results = {}
        
        # Bitcoin via OpenTimestamps
        results['bitcoin'] = self.bitcoin.anchor(merkle_root)
        
        # Ethereum smart contract
        results['ethereum'] = self.ethereum_contract.recordAnchor(merkle_root)
        
        # Polygon for fast verification
        results['polygon'] = self.polygon_contract.recordAnchor(merkle_root)
        
        return results
    
    def verify_anchor(self, log_hash: bytes) -> bool:
        """Verify log exists on at least 2 chains"""
        confirmations = sum([
            self.bitcoin.verify(log_hash),
            self.ethereum.verify(log_hash),
            self.polygon.verify(log_hash)
        ])
        return confirmations >= 2
```

---

## Implementation Phases

### Phase 1: Core Deployment (Days 1-7)

**Objective**: Get basic TML operational with blockchain anchoring

**Steps**:

1. **Install TML Framework**
```bash
pip install tml-blockchain
tml init --project-name "your-org"
```

2. **Configure Blockchain Endpoints**
```yaml
# config/blockchain.yaml
bitcoin:
  rpc_url: "https://bitcoin.node.example.com"
  network: "mainnet"
  
ethereum:
  rpc_url: "https://eth.node.example.com"
  contract: "0x..." # TML smart contract address
  
polygon:
  rpc_url: "https://polygon.node.example.com"
  contract: "0x..." # TML smart contract address
```

3. **Set Up TEE/HSM**
```python
# AWS Nitro Enclaves
tee_config = {
    'platform': 'aws_nitro',
    'enclave_image': 'tml-enclave:latest',
    'cpu_count': 2,
    'memory_mb': 512
}

# Or Azure Confidential Computing
tee_config = {
    'platform': 'azure_cc',
    'vm_size': 'Standard_DC2s_v3',
    'attestation_url': 'https://...'
}

# Or physical HSM
tee_config = {
    'platform': 'hsm',
    'device': '/dev/ttyUSB0',
    'pkcs11_library': '/usr/lib/libCryptoki.so'
}
```

4. **Deploy Always Memory**
```bash
tml deploy --config config/blockchain.yaml --tee config/tee.yaml
```

5. **Verify Operation**
```bash
tml verify --all-chains
# ✓ Bitcoin anchoring: Active
# ✓ Ethereum contracts: Deployed  
# ✓ Polygon verification: Running
# ✓ TEE attestation: Valid
# ✓ Sacred Zero: 66 documents loaded
```

**Deliverable**: Operational TML instance with blockchain protection active

### Phase 2: Integration (Days 8-14)

**Objective**: Integrate TML into existing AI systems

**Steps**:

1. **Wrap AI Endpoints**
```python
from tml_blockchain import AlwaysMemory

memory = AlwaysMemory.from_config('config/blockchain.yaml')

# Existing AI endpoint
@app.post("/predict")
@memory.always_log  # Add TML logging
async def predict(request: PredictRequest):
    result = model.predict(request.data)
    return result
```

2. **Configure Sacred Zero Callbacks**
```python
@memory.on_sacred_zero
async def handle_sacred_zero(context):
    """Called when Sacred Zero triggers"""
    # Notify human reviewer
    await notify_human_reviewer(context)
    
    # Wait for confirmation
    decision = await wait_for_human_decision(context)
    
    # Log decision
    memory.log_human_override(context, decision)
    
    return decision
```

3. **Set Up Monitoring**
```python
# Monitor Sacred Zero triggers
@app.get("/metrics/sacred-zero")
async def sacred_zero_metrics():
    return {
        'triggers_today': memory.count_triggers(period='24h'),
        'trigger_types': memory.aggregate_triggers(),
        'average_resolution_time': memory.avg_resolution_time()
    }
```

4. **Test Integration**
```bash
# Run test suite
tml test integration --scenarios config/test_scenarios.yaml

# Verify logs anchored
tml verify logs --from-date "2025-10-02" --to-date "2025-10-03"
```

**Deliverable**: TML fully integrated with AI systems, all actions logged

### Phase 3: Compliance (Days 15-21)

**Objective**: Establish compliance infrastructure

**Steps**:

1. **Configure Penalty Smart Contracts**
```solidity
// Deploy penalty enforcement
tml contract deploy \
  --type penalty \
  --network ethereum \
  --base-penalty 100000000  # $100M in wei
```

2. **Set Up Audit Access**
```python
# config/audit_access.yaml
audit_roles:
  - name: "internal_audit"
    permissions: ["read_logs", "verify_anchors"]
    
  - name: "regulatory_audit"
    permissions: ["read_logs", "verify_anchors", "export_evidence"]
    
  - name: "victim_access"
    permissions: ["read_own_logs", "request_explanation"]
```

3. **Enable Whistleblower System**
```bash
# Deploy anonymous reporting endpoint
tml whistleblower deploy \
  --reward-percentage 15 \
  --anonymous-submission true \
  --tor-endpoint true
```

4. **Configure Memorial Fund**
```python
# config/memorial_fund.yaml
distribution:
  victims: 40  # 40% of penalties
  environmental_restoration: 30  # 30% for Earth Protection
  whistleblower: 15  # 15% rewards
  operations: 15  # 15% fund operations
  
emergency_support:
  immediate_amount: 50000  # $50K nominal 2025
  response_time_hours: 2
```

**Deliverable**: Full compliance infrastructure operational

### Phase 4: Monitoring & Optimization (Days 22-30)

**Objective**: Fine-tune performance and establish ongoing monitoring

**Steps**:

1. **Performance Optimization**
```python
# Tune batching for your workload
memory.configure_batching(
    max_batch_size=10000,
    max_wait_time_ms=100,
    adaptive_sizing=True
)

# Optimize chain selection
memory.configure_chains(
    bitcoin_frequency='hourly',  # Expensive, less frequent
    polygon_frequency='realtime',  # Cheap, every batch
    ethereum_frequency='daily'  # Medium, periodic
)
```

2. **Set Up Alerting**
```python
# config/alerts.yaml
alerts:
  - condition: "blockchain_anchor_failed"
    severity: "critical"
    action: "page_oncall"
    
  - condition: "sacred_zero_unresolved > 1h"
    severity: "high"
    action: "email_ethics_team"
    
  - condition: "missing_log_detected"
    severity: "critical"
    action: ["page_oncall", "notify_legal", "lock_system"]
```

3. **Create Dashboards**
```bash
# Deploy monitoring dashboard
tml dashboard deploy \
  --metrics "logs_per_second,sacred_zero_rate,anchor_latency" \
  --port 3000
```

4. **Document Procedures**
- Incident response procedures
- Sacred Zero escalation paths
- Blockchain recovery procedures
- Audit request handling

**Deliverable**: Optimized, monitored TML deployment ready for production

---

## Critical Implementation Points

### Always Memory Requirements

**Non-negotiable**:
- Every action must create a log BEFORE execution
- Logs must be sealed in TEE/HSM
- Logs must be anchored to at least 2 blockchains
- Missing logs trigger automatic penalties

**Implementation**:
```python
def critical_decision(input_data):
    # WRONG: Action before log
    result = model.predict(input_data)
    memory.log(result)  # Too late!
    
    # CORRECT: Log before action
    log_id = memory.pre_action_log(input_data)
    result = model.predict(input_data)
    memory.post_action_update(log_id, result)
```

### Sacred Zero Handling

**Trigger Sources**:
- Human Rights: 26 documents (UDHR, ICCPR, ICESCR, etc.)
- Earth Protection: 20+ treaties (Paris Agreement, CBD, etc.)
- Discrimination: Protected class analysis
- Vulnerable populations: Enhanced protections

**Response Flow**:
```python
if sacred_zero_triggered(input_data):
    # 1. Log the trigger
    log = memory.log_sacred_zero(
        trigger_type=trigger.type,
        trigger_document=trigger.source,
        reasoning=trigger.reasoning
    )
    
    # 2. Pause execution
    await pause_execution()
    
    # 3. Request human review
    decision = await human_review_system.request_review(log)
    
    # 4. Log human decision
    memory.log_human_override(log, decision)
    
    # 5. Execute based on human decision
    if decision == "proceed":
        return execute_action()
    else:
        return refuse_action(reason=decision.reason)
```

### Blockchain Anchoring

**Minimum Requirements**:
- At least 2 chains for redundancy
- OpenTimestamps for Bitcoin
- Smart contracts for Ethereum/Polygon
- Verification within 5 minutes

**Anchor Verification**:
```python
def verify_log_integrity(log_hash: bytes) -> bool:
    """Verify log exists on blockchains"""
    bitcoin_confirmed = opentimestamps.verify(log_hash)
    ethereum_confirmed = ethereum_contract.verifyAnchor(log_hash)
    polygon_confirmed = polygon_contract.verifyAnchor(log_hash)
    
    # Require at least 2 confirmations
    confirmations = sum([
        bitcoin_confirmed,
        ethereum_confirmed,
        polygon_confirmed
    ])
    
    return confirmations >= 2
```

### Performance Standards

**Latency Targets**:
- User-visible response: <2ms added latency
- Log creation: <50ms
- Blockchain anchoring: <500ms (async)
- Full verification: <5 seconds

**Throughput**:
- Support 100,000+ decisions per second
- Batch 1,000-10,000 logs per anchor
- Anchor every 60 seconds minimum

**Degraded Mode**:
```python
if blockchain_unavailable():
    # Continue logging to TEE
    memory.degraded_mode(
        local_storage=True,
        queue_for_retry=True,
        alert_operations=True
    )
    
    # When blockchain recovers
    memory.sync_backlog()
```

---

## Testing & Validation

### Unit Tests

```python
# test_always_memory.py
def test_log_before_action():
    """Verify log created before action executes"""
    memory = AlwaysMemory(test_config)
    
    @memory.always_log
    def test_action():
        return "result"
    
    # Should create log first
    with memory.assert_log_created_first():
        result = test_action()
    
    assert result == "result"

def test_missing_log_raises():
    """Verify missing log triggers error"""
    with pytest.raises(MissingLogException):
        execute_without_log()
```

### Integration Tests

```bash
# Run full integration test suite
tml test integration --config config/test.yaml

# Test scenarios:
# - Sacred Zero triggers correctly
# - Blockchain anchoring succeeds
# - Degraded mode handles failures
# - Penalty contracts enforce violations
# - Whistleblower system accepts reports
```

### Compliance Validation

```python
# compliance/validate.py
def validate_deployment():
    """Verify deployment meets all requirements"""
    checks = {
        'always_memory_active': memory.is_operational(),
        'sacred_zero_loaded': len(memory.triggers) >= 66,
        'blockchain_anchoring': verify_multi_chain_anchors(),
        'tee_attestation': verify_tee_secure(),
        'smart_contracts': verify_contracts_deployed(),
        'whistleblower_system': verify_anonymous_reporting(),
        'memorial_fund': verify_fund_configured()
    }
    
    return all(checks.values()), checks
```

---

## Production Deployment

### Pre-Production Checklist

- [ ] All tests passing (unit, integration, compliance)
- [ ] Blockchain anchoring verified on all chains
- [ ] TEE/HSM attestation valid
- [ ] Sacred Zero triggers loaded (66 documents minimum)
- [ ] Smart contracts deployed and tested
- [ ] Whistleblower system operational
- [ ] Memorial Fund configured
- [ ] Monitoring and alerting active
- [ ] Incident response procedures documented
- [ ] Legal review completed

### Deployment Command

```bash
# Deploy to production
tml deploy production \
  --config config/production.yaml \
  --verify-all-checks \
  --create-backup \
  --enable-monitoring
```

### Post-Deployment Verification

```bash
# Verify all systems operational
tml verify production --comprehensive

# Monitor for 24 hours
tml monitor --duration 24h --alert-on-issues
```

---

## Ongoing Operations

### Daily Operations

```bash
# Check system health
tml status --detailed

# Verify blockchain anchoring
tml verify anchors --last-24h

# Review Sacred Zero triggers
tml report sacred-zero --daily
```

### Weekly Tasks

- Review Sacred Zero patterns
- Verify blockchain anchor success rate
- Check TEE/HSM attestations
- Audit Memorial Fund distributions
- Review whistleblower reports

### Monthly Tasks

- Generate compliance reports
- Update Sacred Zero trigger documents
- Review penalty contract balances
- Audit full system integrity
- Test disaster recovery procedures

### Quarterly Tasks

- External security audit
- Penetration testing
- Legal compliance review
- Performance optimization review
- Documentation updates

---

## Common Issues & Solutions

### Issue: Blockchain Anchoring Delays

**Symptoms**: Anchors taking >5 minutes

**Solutions**:
```python
# Increase gas prices
memory.configure_chains(
    ethereum_gas_multiplier=1.5,
    polygon_gas_multiplier=1.2
)

# Use priority channels
memory.enable_priority_anchoring(True)

# Add more chains
memory.add_chain('algorand', config)
```

### Issue: Sacred Zero Trigger Fatigue

**Symptoms**: Too many false positives

**Solutions**:
```python
# Fine-tune thresholds
memory.update_triggers(
    discrimination_threshold=0.25,  # Was 0.20
    environmental_irreversibility=0.8  # Was 0.7
)

# Add context filters
memory.add_context_rules([
    'ignore_if_user_consent',
    'ignore_if_regulatory_approved'
])
```

### Issue: TEE Attestation Failures

**Symptoms**: Logs not sealed properly

**Solutions**:
```bash
# Verify TEE configuration
tml tee verify --platform aws_nitro

# Restart TEE service
tml tee restart --force-reboot

# Update TEE image
tml tee update --image tml-enclave:latest
```

---

## Support & Resources

### Documentation
- API Reference: `/docs/api/complete_api_reference.md`
- Sacred Zero Triggers: `/policies/sacred_zero_triggers.yaml`
- Smart Contracts: `/contracts/TMLPenalty.sol`
- Test Suites: `/tests/`

### Technical Support
- Email: technical@tml-goukassian.org
- GitHub Issues: https://github.com/FractonicMind/TernaryMoralLogic/issues
- Emergency: emergency@tml-goukassian.org

### Legal & Compliance
- Compliance Questions: compliance@tml-goukassian.org
- Victim Support: victims@tml-goukassian.org
- Whistleblower: whistleblower@tml-goukassian.org (anonymous)

---

**Creator**: Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Email**: leogouk@gmail.com  
**Repository**: https://github.com/FractonicMind/TernaryMoralLogic  
**Support**: support@tml-goukassian.org

*All USD amounts are nominal to 2025*

---

#### *“Follow the guide and you’ll ship ethics at CI speed: build, test, hash, sign—done. Morality now deploys faster than most bug fixes.”* - Lev Goukassian
---
