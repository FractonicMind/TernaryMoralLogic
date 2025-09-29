# Installation Guide - 10 Minute Deployment

## Ternary Moral Logic (TML) - Blockchain-First Framework

**Deploy in 10 minutes. Protect humans and Earth immediately. No committees required.**

---

## Quick Start (Really 10 Minutes)

### Step 1: Pull Docker Image (2 minutes)
```bash
docker pull tml/always-memory:latest
```

### Step 2: Configure Blockchain (3 minutes)
```bash
# Create configuration
cat > tml-config.env << EOF
# MANDATORY - Blockchain Anchoring
BLOCKCHAIN_ANCHORING=true
BITCOIN_RPC=https://btc.yournode.com
POLYGON_RPC=https://polygon-rpc.com
ETHEREUM_RPC=https://eth.yournode.com

# MANDATORY - Protection Frameworks
HUMAN_RIGHTS_FRAMEWORK=true  # 26 documents
EARTH_PROTECTION=true         # 20+ treaties
FUTURE_GENERATIONS=true       # 7-generation impact

# OPTIONAL - Guardian Network (leave false)
GUARDIAN_NETWORK=false        # Not required for operation
EOF
```

### Step 3: Deploy TML (5 minutes)
```bash
docker run -d \
  --name tml-production \
  --env-file tml-config.env \
  -p 8080:8080 \
  tml/always-memory:latest

# Verify deployment
curl http://localhost:8080/health
```

**Done!** TML is now protecting humans and Earth. No institutional coordination needed.

---

## System Requirements

### Minimum (Works Fine)
- **Docker**: 20.10+
- **Memory**: 2GB RAM
- **Storage**: 10GB (for blockchain proofs)
- **Network**: Internet for blockchain anchoring

### Recommended (Better Performance)
- **Docker**: Latest version
- **Memory**: 8GB RAM
- **Storage**: 100GB SSD
- **CPU**: 4 cores

---

## Core Configuration

### Blockchain Anchoring (MANDATORY)
```yaml
blockchain:
  bitcoin:
    enabled: true
    confirmation_blocks: 6
    cost_per_batch: "$2.00"
    
  polygon:
    enabled: true
    confirmation_blocks: 128
    cost_per_batch: "$0.005"
    
  ethereum:
    enabled: true
    confirmation_blocks: 12
    cost_per_batch: "$20.00"
    
  minimum_chains: 2  # At least 2 for redundancy
```

### Protection Frameworks (MANDATORY)
```yaml
human_rights:
  documents: 26
  includes:
    - Universal Declaration of Human Rights
    - International Covenants (ICCPR, ICESCR)
    - Convention Against Torture (zero tolerance)
    - Geneva Conventions
    - Child Rights Convention
    - Disability Rights Convention
  
earth_protection:
  treaties: 20+
  includes:
    - Paris Agreement
    - Convention on Biological Diversity
    - IPCC thresholds
    - Indigenous FPIC protocols
    - Planetary boundaries
```

### Guardian Network (OPTIONAL - Skip This)
```yaml
guardians:
  enabled: false  # Not required for deployment
  note: "Optional enhancement for 1% of companies years later"
```

---

## Smart Contract Deployment

### Automatic Penalties
```solidity
// Deploy to Ethereum/Polygon
contract TMLEnforcement {
    uint constant HUMAN_RIGHTS_MULTIPLIER = 2;
    uint constant EARTH_HARM_MULTIPLIER = 3;
    uint constant FUTURE_GEN_MULTIPLIER = 7;
    
    function enforcePenalties(bytes32 violationProof) public {
        uint penalty = calculateBasePenalty(violationProof);
        
        if (isHumanRightsViolation(violationProof)) {
            penalty *= HUMAN_RIGHTS_MULTIPLIER;
        }
        if (isEnvironmentalHarm(violationProof)) {
            penalty *= EARTH_HARM_MULTIPLIER;
        }
        if (affectsFutureGenerations(violationProof)) {
            penalty *= FUTURE_GEN_MULTIPLIER;
        }
        
        executePenalty(penalty);
        compensateVictims(penalty);
    }
}
```

Deploy with:
```bash
docker run tml/always-memory deploy-contracts \
  --network ethereum \
  --network polygon
```

---

## Verification

### Check Blockchain Anchoring
```bash
curl http://localhost:8080/verify/blockchain
# Should return: {"bitcoin": "active", "polygon": "active", "ethereum": "active"}
```

### Verify Protection Frameworks
```bash
curl http://localhost:8080/verify/frameworks
# Should return: {"human_rights": 26, "earth_protection": 20+}
```

### Test Sacred Zero
```bash
curl -X POST http://localhost:8080/test/sacred-zero \
  -d '{"scenario": "human_rights_violation"}'
# Should trigger immediate logging
```

---

## Production Deployment

### Docker Compose (Recommended)
```yaml
version: '3.8'
services:
  tml:
    image: tml/always-memory:latest
    environment:
      - BLOCKCHAIN_ANCHORING=true
      - HUMAN_RIGHTS_FRAMEWORK=true
      - EARTH_PROTECTION=true
      - GUARDIAN_NETWORK=false
    volumes:
      - tml-data:/data
      - tml-logs:/logs
    ports:
      - "8080:8080"
    restart: always
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3

volumes:
  tml-data:
  tml-logs:
```

### Kubernetes (Enterprise)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tml-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: tml
  template:
    metadata:
      labels:
        app: tml
    spec:
      containers:
      - name: tml
        image: tml/always-memory:latest
        env:
        - name: BLOCKCHAIN_ANCHORING
          value: "true"
        - name: HUMAN_RIGHTS_FRAMEWORK
          value: "true"
        - name: EARTH_PROTECTION
          value: "true"
        - name: GUARDIAN_NETWORK
          value: "false"
```

---

## Cost Analysis

### Operational Costs (Per Month)
```
Blockchain Anchoring:
- Bitcoin: ~$100 (50 batches)
- Polygon: ~$10 (2000 batches)
- Ethereum: ~$40 (2 batches)
Total: $150/month

Guardian Network: $0 (not needed)
Committees: $0 (don't exist)
Coordination: $0 (unnecessary)

ROI: 300-800% from risk mitigation
```

---

## Python Integration

### Basic Usage
```python
from tml import TMLClient

# Connect to local deployment
client = TMLClient("http://localhost:8080")

# Check configuration
config = client.get_config()
assert config['blockchain_anchoring'] == True
assert config['human_rights_documents'] == 26
assert config['guardian_network'] == False  # Not needed

# Log decision
result = client.log_decision({
    'action': 'resource_allocation',
    'impact': 'affects_vulnerable_population',
    'stakeholders': ['patients', 'hospitals']
})

# Verify blockchain proof
proof = client.verify_on_blockchain(result['log_id'])
assert proof['bitcoin_tx'] is not None
assert proof['polygon_tx'] is not None
```

---

## Troubleshooting

### Issue: "Cannot connect to blockchain"
```bash
# Solution: Check RPC endpoints
docker logs tml-production | grep blockchain

# Use public endpoints if needed
POLYGON_RPC=https://polygon-rpc.com
ETHEREUM_RPC=https://cloudflare-eth.com
```

### Issue: "Guardian Network required?"
```bash
# Solution: NO! Set to false always
GUARDIAN_NETWORK=false
# TML works perfectly without any Guardian Network
```

### Issue: "Waiting for institutional approval?"
```bash
# Solution: There is no waiting!
# Deploy immediately with blockchain
# No committees exist
# No approval needed
```

---

## Migration from Old TML

### If Using Pre-Blockchain Version
```bash
# Stop waiting for committees
docker stop old-tml

# Deploy blockchain version NOW
docker run tml/always-memory:latest

# Migration complete in 10 minutes
```

---

## Academic Citation

```bibtex
@software{goukassian2025tml,
  title={Ternary Moral Logic: Blockchain-First Framework},
  author={Goukassian, Lev},
  year={2025},
  note={Protects Humans + Earth + Future Generations},
  url={https://github.com/FractonicMind/TernaryMoralLogic}
}
```

---

## Support

**Blockchain Deployment**: support@tml-goukassian.org  
**Emergency**: emergency@tml-goukassian.org  
**Guardian Questions**: Don't bother - you don't need them

---

## Key Innovation

> "# Installation Guide - 10 Minute Deployment

## Ternary Moral Logic (TML) - Blockchain-First Framework

**Deploy in 10 minutes. Protect humans and Earth immediately. No committees required.**

---

## Quick Start (Really 10 Minutes)

### Step 1: Pull Docker Image (2 minutes)
```bash
docker pull tml/always-memory:latest
```

### Step 2: Configure Blockchain (3 minutes)
```bash
# Create configuration
cat > tml-config.env << EOF
# MANDATORY - Blockchain Anchoring
BLOCKCHAIN_ANCHORING=true
BITCOIN_RPC=https://btc.yournode.com
POLYGON_RPC=https://polygon-rpc.com
ETHEREUM_RPC=https://eth.yournode.com

# MANDATORY - Protection Frameworks
HUMAN_RIGHTS_FRAMEWORK=true  # 26 documents
EARTH_PROTECTION=true         # 20+ treaties
FUTURE_GENERATIONS=true       # 7-generation impact

# OPTIONAL - Guardian Network (leave false)
GUARDIAN_NETWORK=false        # Not required for operation
EOF
```

### Step 3: Deploy TML (5 minutes)
```bash
docker run -d \
  --name tml-production \
  --env-file tml-config.env \
  -p 8080:8080 \
  tml/always-memory:latest

# Verify deployment
curl http://localhost:8080/health
```

**Done!** TML is now protecting humans and Earth. No institutional coordination needed.

---

## System Requirements

### Minimum (Works Fine)
- **Docker**: 20.10+
- **Memory**: 2GB RAM
- **Storage**: 10GB (for blockchain proofs)
- **Network**: Internet for blockchain anchoring

### Recommended (Better Performance)
- **Docker**: Latest version
- **Memory**: 8GB RAM
- **Storage**: 100GB SSD
- **CPU**: 4 cores

---

## Core Configuration

### Blockchain Anchoring (MANDATORY)
```yaml
blockchain:
  bitcoin:
    enabled: true
    confirmation_blocks: 6
    cost_per_batch: "$2.00"
    
  polygon:
    enabled: true
    confirmation_blocks: 128
    cost_per_batch: "$0.005"
    
  ethereum:
    enabled: true
    confirmation_blocks: 12
    cost_per_batch: "$20.00"
    
  minimum_chains: 2  # At least 2 for redundancy
```

### Protection Frameworks (MANDATORY)
```yaml
human_rights:
  documents: 26
  includes:
    - Universal Declaration of Human Rights
    - International Covenants (ICCPR, ICESCR)
    - Convention Against Torture (zero tolerance)
    - Geneva Conventions
    - Child Rights Convention
    - Disability Rights Convention
  
earth_protection:
  treaties: 20+
  includes:
    - Paris Agreement
    - Convention on Biological Diversity
    - IPCC thresholds
    - Indigenous FPIC protocols
    - Planetary boundaries
```

### Guardian Network (OPTIONAL - Skip This)
```yaml
guardians:
  enabled: false  # Not required for deployment
  note: "Optional enhancement for 1% of companies years later"
```

---

## Smart Contract Deployment

### Automatic Penalties
```solidity
// Deploy to Ethereum/Polygon
contract TMLEnforcement {
    uint constant HUMAN_RIGHTS_MULTIPLIER = 2;
    uint constant EARTH_HARM_MULTIPLIER = 3;
    uint constant FUTURE_GEN_MULTIPLIER = 7;
    
    function enforcePenalties(bytes32 violationProof) public {
        uint penalty = calculateBasePenalty(violationProof);
        
        if (isHumanRightsViolation(violationProof)) {
            penalty *= HUMAN_RIGHTS_MULTIPLIER;
        }
        if (isEnvironmentalHarm(violationProof)) {
            penalty *= EARTH_HARM_MULTIPLIER;
        }
        if (affectsFutureGenerations(violationProof)) {
            penalty *= FUTURE_GEN_MULTIPLIER;
        }
        
        executePenalty(penalty);
        compensateVictims(penalty);
    }
}
```

Deploy with:
```bash
docker run tml/always-memory deploy-contracts \
  --network ethereum \
  --network polygon
```

---

## Verification

### Check Blockchain Anchoring
```bash
curl http://localhost:8080/verify/blockchain
# Should return: {"bitcoin": "active", "polygon": "active", "ethereum": "active"}
```

### Verify Protection Frameworks
```bash
curl http://localhost:8080/verify/frameworks
# Should return: {"human_rights": 26, "earth_protection": 20+}
```

### Test Sacred Zero
```bash
curl -X POST http://localhost:8080/test/sacred-zero \
  -d '{"scenario": "human_rights_violation"}'
# Should trigger immediate logging
```

---

## Production Deployment

### Docker Compose (Recommended)
```yaml
version: '3.8'
services:
  tml:
    image: tml/always-memory:latest
    environment:
      - BLOCKCHAIN_ANCHORING=true
      - HUMAN_RIGHTS_FRAMEWORK=true
      - EARTH_PROTECTION=true
      - GUARDIAN_NETWORK=false
    volumes:
      - tml-data:/data
      - tml-logs:/logs
    ports:
      - "8080:8080"
    restart: always
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3

volumes:
  tml-data:
  tml-logs:
```

### Kubernetes (Enterprise)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tml-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: tml
  template:
    metadata:
      labels:
        app: tml
    spec:
      containers:
      - name: tml
        image: tml/always-memory:latest
        env:
        - name: BLOCKCHAIN_ANCHORING
          value: "true"
        - name: HUMAN_RIGHTS_FRAMEWORK
          value: "true"
        - name: EARTH_PROTECTION
          value: "true"
        - name: GUARDIAN_NETWORK
          value: "false"
```

---

## Cost Analysis

### Operational Costs (Per Month)
```
Blockchain Anchoring:
- Bitcoin: ~$100 (50 batches)
- Polygon: ~$10 (2000 batches)
- Ethereum: ~$40 (2 batches)
Total: $150/month

Guardian Network: $0 (not needed)
Committees: $0 (don't exist)
Coordination: $0 (unnecessary)

ROI: 300-800% from risk mitigation
```

---

## Python Integration

### Basic Usage
```python
from tml import TMLClient

# Connect to local deployment
client = TMLClient("http://localhost:8080")

# Check configuration
config = client.get_config()
assert config['blockchain_anchoring'] == True
assert config['human_rights_documents'] == 26
assert config['guardian_network'] == False  # Not needed

# Log decision
result = client.log_decision({
    'action': 'resource_allocation',
    'impact': 'affects_vulnerable_population',
    'stakeholders': ['patients', 'hospitals']
})

# Verify blockchain proof
proof = client.verify_on_blockchain(result['log_id'])
assert proof['bitcoin_tx'] is not None
assert proof['polygon_tx'] is not None
```

---

## Troubleshooting

### Issue: "Cannot connect to blockchain"
```bash
# Solution: Check RPC endpoints
docker logs tml-production | grep blockchain

# Use public endpoints if needed
POLYGON_RPC=https://polygon-rpc.com
ETHEREUM_RPC=https://cloudflare-eth.com
```

### Issue: "Guardian Network required?"
```bash
# Solution: NO! Set to false always
GUARDIAN_NETWORK=false
# TML works perfectly without any Guardian Network
```

### Issue: "Waiting for institutional approval?"
```bash
# Solution: There is no waiting!
# Deploy immediately with blockchain
# No committees exist
# No approval needed
```

---

## Migration from Old TML

### If Using Pre-Blockchain Version
```bash
# Stop waiting for committees
docker stop old-tml

# Deploy blockchain version NOW
docker run tml/always-memory:latest

# Migration complete in 10 minutes
```

---

## Academic Citation

```bibtex
@software{goukassian2025tml,
  title={Ternary Moral Logic: Blockchain-First Framework},
  author={Goukassian, Lev},
  year={2025},
  note={Protects Humans + Earth + Future Generations},
  url={https://github.com/FractonicMind/TernaryMoralLogic}
}
```

---

## Support

**Blockchain Deployment**: support@tml-goukassian.org  
**Emergency**: emergency@tml-goukassian.org  
**Guardian Questions**: Don't bother - you don't need them

---

## Key Innovation

#### **"Miss one byte, pay twice for the human; thrice for the reef; sevenfold for the child not yet born—math that makes greed think twice."**

**Deploy today. Protect immediately. No permission required.**

---

**Creator**: Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Email**: leogouk@gmail.com  
**Repository**: https://github.com/FractonicMind/TernaryMoralLogic  
**Architecture**: Blockchain-First, Guardian-Never-Needed

*All USD amounts are nominal to 2025*"

**Deploy today. Protect immediately. No permission required.**

---

**Creator**: Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Email**: leogouk@gmail.com  
**Repository**: https://github.com/FractonicMind/TernaryMoralLogic  
**Architecture**: Blockchain-First, Guardian-Never-Needed

*All USD amounts are nominal to 2025*
