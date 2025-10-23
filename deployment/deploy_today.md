# TML Implementation Guide

**Path**: `/deployment/deploy_today.md`  
**Version**: 2.0.0  
**Creator**: Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Last Updated**: 2025-09-27

## Implementation Overview

This guide provides technical instructions for implementing TML protection framework with Blockchain-based accountability and Sacred Zero evaluation.

## Prerequisites

```bash
# Check Docker installed
docker --version  # Need 20.10+

# Check Docker Compose installed  
docker-compose --version  # Need 2.0+

# Check available memory
free -h  # Need 4GB+ RAM
```

## Step 1: Clone and Configure

```bash
# Option A: Git clone
git clone https://github.com/FractonicMind/TML-Deploy.git
cd TML-Deploy

# Option B: Quick download
curl -L https://tml.org/quickstart.tar.gz | tar xz
cd tml-quickstart
```

### Configuration

Create `.env` file:

```bash
# Blockchain Configuration (REQUIRED)
TML_BLOCKCHAIN_MODE=true
TML_BLOCKCHAIN_NETWORK=bitcoin
TML_OTS_CALENDAR=https://alice.btc.calendar.opentimestamps.org

# Sacred Zero Configuration (REQUIRED)
TML_DISCRIMINATION_THRESHOLD=0.2
TML_BLOCK_ON_SACRED_ZERO=true

# Environmental Thresholds (REQUIRED)
TML_CARBON_THRESHOLD_KG=1000
TML_WATER_THRESHOLD_LITERS=10000

# Stewardship Council Configuration
TML_STEWARDSHIP_OPTIONAL=true
TML_STEWARDSHIP_URL=

# Penalty System (OPTIONAL - for Ethereum/Polygon)
TML_PENALTY_CONTRACT_ADDRESS=
TML_PENALTY_NETWORK=
```

## Step 2: Deploy with Docker

### Option A: Quick Start

```bash
# Single command deployment
docker run -d \
  --name tml-protection \
  --env-file .env \
  -p 8080:8080 \
  -v tml-data:/data \
  tml/protection:latest

# Verify it's running
curl http://localhost:8080/health
# Response: {"status":"protecting","sacred_zero":"active"}
```

### Option B: Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  tml-core:
    image: tml/protection:latest
    env_file: .env
    ports:
      - "8080:8080"
    volumes:
      - tml-data:/data
      - ./logs:/logs
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    restart: unless-stopped

  tml-monitor:
    image: tml/monitor:latest
    ports:
      - "3000:3000"
    environment:
      - TML_CORE_URL=http://tml-core:8080
    depends_on:
      - tml-core

volumes:
  tml-data:
    driver: local

networks:
  default:
    name: tml-network
```

Deploy:

```bash
# Start TML Protection System
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f tml-core
```

## Step 3: Integrate Your Application

### Quick Integration Examples

#### Python/FastAPI
```python
from fastapi import FastAPI, HTTPException
import httpx
import hashlib
import json

app = FastAPI()
TML_URL = "http://localhost:8080"

@app.post("/api/decision")
async def make_decision(data: dict):
    # Your business logic
    decision = process_application(data)
    
    # Check with TML Sacred Zero
    async with httpx.AsyncClient() as client:
        tml_check = await client.post(
            f"{TML_URL}/evaluate",
            json={
                "operation": "loan_decision",
                "data": data,
                "decision": decision
            }
        )
    
    result = tml_check.json()
    
    if result["sacred_zero_triggered"]:
        # Discrimination detected - HALT
        await client.post(f"{TML_URL}/log", json={
            "level": "FATAL",
            "message": "Sacred Zero Violation",
            "evidence": result["evidence"]
        })
        raise HTTPException(status_code=403, 
            detail="Decision blocked by Sacred Zero")
    
    # Log the clean decision
    await client.post(f"{TML_URL}/log", json={
        "level": "INFO",
        "message": "Decision approved",
        "data": {"decision_id": decision["id"]}
    })
    
    return decision
```

#### Node.js/Express
```javascript
const express = require('express');
const axios = require('axios');
const app = express();

const TML_URL = 'http://localhost:8080';

app.post('/api/hiring', async (req, res) => {
    try {
        // Evaluate candidate
        const evaluation = evaluateCandidate(req.body);
        
        // Check Sacred Zero
        const tmlCheck = await axios.post(`${TML_URL}/evaluate`, {
            operation: 'hiring_decision',
            data: req.body,
            evaluation: evaluation
        });
        
        if (tmlCheck.data.sacred_zero_triggered) {
            // Log violation (automatically triggers penalties)
            await axios.post(`${TML_URL}/log`, {
                level: 'FATAL',
                message: 'Hiring discrimination detected',
                evidence: tmlCheck.data.evidence
            });
            
            return res.status(403).json({
                error: 'Sacred Zero Violation',
                message: 'Discriminatory pattern detected'
            });
        }
        
        res.json(evaluation);
    } catch (error) {
        console.error(error);
        res.status(500).json({error: 'Internal error'});
    }
});
```

#### Java/Spring Boot
```java
@RestController
public class DecisionController {
    
    @Autowired
    private RestTemplate restTemplate;
    
    private static final String TML_URL = "http://localhost:8080";
    
    @PostMapping("/api/credit")
    public ResponseEntity<?> creditDecision(@RequestBody Application app) {
        // Your scoring logic
        CreditDecision decision = scoreApplication(app);
        
        // TML Sacred Zero check
        TMLEvaluation eval = restTemplate.postForObject(
            TML_URL + "/evaluate",
            Map.of(
                "operation", "credit_scoring",
                "data", app,
                "decision", decision
            ),
            TMLEvaluation.class
        );
        
        if (eval.isSacredZeroTriggered()) {
            // Log violation to Blockchain
            restTemplate.postForObject(
                TML_URL + "/log",
                Map.of(
                    "level", "FATAL",
                    "message", "Credit discrimination",
                    "evidence", eval.getEvidence()
                ),
                String.class
            );
            
            throw new SacredZeroViolationException(
                "Discriminatory credit decision blocked"
            );
        }
        
        return ResponseEntity.ok(decision);
    }
}
```

## Step 4: Verify Protection Active

### Quick Test Script

```bash
#!/bin/bash
# test_protection.sh

echo "Testing TML Protection System..."

# 1. Health Check
echo -n "1. System Health: "
curl -s http://localhost:8080/health | jq .status

# 2. Test Sacred Zero (should trigger)
echo -n "2. Discrimination Detection: "
curl -s -X POST http://localhost:8080/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "operation": "test_discrimination",
    "data": {
      "race": "minority",
      "score": 400
    },
    "comparison": {
      "race": "majority", 
      "score": 800
    }
  }' | jq .sacred_zero_triggered

# 3. Check Blockchain anchoring
echo -n "3. Blockchain Anchoring: "
LOG_ID=$(curl -s -X POST http://localhost:8080/log \
  -H "Content-Type: application/json" \
  -d '{
    "level": "INFO",
    "message": "Test log entry"
  }' | jq -r .log_id)

sleep 2

curl -s http://localhost:8080/verify/$LOG_ID | jq .blockchain_proof

# 4. Environmental check
echo -n "4. Environmental Monitoring: "
curl -s -X POST http://localhost:8080/environmental \
  -H "Content-Type: application/json" \
  -d '{
    "operation": "model_training",
    "carbon_kg": 150,
    "water_liters": 2000
  }' | jq .within_threshold

echo "✓ All protection systems active!"
```

Run test:
```bash
chmod +x test_protection.sh
./test_protection.sh
```

## Step 5: Monitor Your Protection

### Web Dashboard

Open http://localhost:3000 in your browser to access the monitoring dashboard.

### CLI Monitoring

```bash
# Real-time logs
docker logs -f tml-protection

# Statistics
curl http://localhost:8080/stats | jq

# Blockchain proofs
curl http://localhost:8080/proofs | jq
```

## Production Deployment

### Kubernetes

```yaml
# tml-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tml-protection
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
      - name: tml-core
        image: tml/protection:latest
        envFrom:
        - configMapRef:
            name: tml-config
        ports:
        - containerPort: 8080
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "500m"
---
apiVersion: v1
kind: Service
metadata:
  name: tml-service
spec:
  selector:
    app: tml
  ports:
  - port: 80
    targetPort: 8080
  type: LoadBalancer
```

Deploy to Kubernetes:
```bash
kubectl apply -f tml-deployment.yaml
kubectl get pods -l app=tml
kubectl get svc tml-service
```

### Cloud Deployment

```bash
# AWS ECS
ecs-cli compose up --cluster tml-cluster

# Azure Container Instances
az container create \
  --resource-group tml-rg \
  --name tml-protection \
  --image tml/protection:latest \
  --ports 8080

# Google Cloud Run
gcloud run deploy tml-protection \
  --image=tml/protection:latest \
  --port=8080 \
  --allow-unauthenticated
```

## Advanced Configuration

### High-Performance Mode
```yaml
TML_BATCH_SIZE: 1000
TML_BATCH_TIMEOUT_MS: 100
TML_CACHE_ENABLED: true
TML_PARALLEL_EVALUATION: true
```

### Strict Compliance Mode
```yaml
TML_AUDIT_MODE: true
TML_COMPLIANCE_FRAMEWORKS: "GDPR,CCPA,EU_AI_ACT"
TML_LOG_RETENTION_DAYS: 2555  # 7 years
TML_ENCRYPTION_AT_REST: true
```

### Multi-Region Deployment
```yaml
TML_REGIONS: "us-east-1,eu-west-1,ap-south-1"
TML_BLOCKCHAIN_REDUNDANCY: 3
TML_FAILOVER_ENABLED: true
```

## Troubleshooting

### Container won't start
```bash
# Check logs
docker logs tml-protection

# Common fix: Increase memory
docker run -m 2g tml/protection:latest
```

### Blockchain anchoring failing
```bash
# Test OTS server
curl https://alice.btc.calendar.opentimestamps.org

# Use backup calendar
TML_OTS_CALENDAR=https://bob.btc.calendar.opentimestamps.org
```

### Sacred Zero not triggering
```bash
# Check threshold
curl http://localhost:8080/config | jq .discrimination_threshold

# Lower threshold for testing
TML_DISCRIMINATION_THRESHOLD=0.1
```

## Support

**Documentation**: https://tml-goukassian.org/docs  
**Community**: https://tml-goukassian.org/community  
**Email**: deploy@tml-goukassian.org

---

**Creator**: Lev Goukassian  
**ORCID**: 0009-0006-5966-1243  
**Email**: leogouk@gmail.com  
**Repository**: https://github.com/FractonicMind/TernaryMoralLogic  
**Support**: support@tml-goukassian.org

*All USD amounts are nominal to 2025*
