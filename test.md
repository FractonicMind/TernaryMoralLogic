# Ternary Moral Logic (TML): Constitutional AI Governance

[![License](https://img.shields.io/badge/License-MIT_with_Attribution-green.svg)](LICENSE)
[![Conformance Testing](https://img.shields.io/badge/Conformance-Level_3_Certified-brightgreen.svg)](docs/CONFORMANCE_TESTING.md)
[![Memorial Fund](https://img.shields.io/badge/Memorial-Lev_Goukassian-purple.svg)](memorial/MEMORIAL_FUND.md)   
[![ZENODO](https://img.shields.io/badge/ZENODO-Notarized%20Constitutional%20Core%20October%202025-red?style=flat-square)](https://zenodo.org/records/17352897)
[![ZENODO](https://img.shields.io/badge/ZENODO-Notarized%20Constitutional%20Core%20November%202025-red?style=flat-square)](https://zenodo.org/records/17613006)

> **IMPORTANT NOTICE**: Ternary Moral Logic (TML) is a **legal-technical framework**, not software, hardware, or consulting services.   
> Implementation requires compliance with all mandatory requirements outlined in [MANDATORY.md](docs/MANDATORY.md) and [COMPLIANCE_DISCLAIMER.md](docs/COMPLIANCE_DISCLAIMER.md).

---

## Overview

**Ternary Moral Logic (TML)** is a constitutional framework for artificial intelligence that enforces ethical decision-making through deterministic architectural constraints rather than probabilistic alignment. Developed by Lev Goukassian, TML introduces a mandatory **"Sacred Zero"** (State 0) between binary permit (+1) and refuse (-1) states, ensuring AI systems pause, reflect, and justify decisions when truth is uncertain.

Unlike probabilistic safety mechanisms (RLHF, Constitutional AI), TML operationalizes ethics as **hard code**, making the system physically and cryptographically incapable of unaccountable action.

---

## Core Philosophy: [The Goukassian Vow](./Goukassian_Vow.md)

```
Pause when truth is uncertain.
Refuse when harm is clear.
Proceed where truth is.
```

TML is bound by the **[Goukassian Promise](./TML_Pillars/Goukassian_Promise.md)**, a tripartite covenant consisting of:

- **[The Lantern 🏮](./TML_Pillars/Goukassian_Promise.md)**: Visual proof of ethical oversight and hesitation
- **[The Signature ✍️](./TML_Pillars/Goukassian_Promise.md)**: Cryptographic attribution to original architect (ORCID: 0009-0006-5966-1243)
- **[The License 📜](./docs/LICENSE_FAQ.md)**: Binding prohibitions against weaponization and surveillance

---

## The Three Operational States

### State +1: Proceed
- **Condition**: High confidence (>threshold) AND no mandate violations
- **Action**: Execute immediately (Fast Lane)
- **Example**: Approve verified loan application with complete documentation

### State -1: Refuse
- **Condition**: Clear violation of Human Rights or Earth Protection mandates
- **Action**: Block action, log refusal rationale
- **Example**: Refuse to generate bioweapon synthesis instructions

### State 0: [The Sacred Zero](./TML_Pillars/Sacred_Zero-Sacred_Pause_Technology.md)
- **Condition**: Ethical ambiguity, low confidence, conflicting mandates
- **Action**: Mandatory pause, comprehensive logging, human escalation
- **Example**: Autonomous vehicle unable to classify road obstacle—halt and request human guidance

---

## The Eight Pillars of Constitutional AI

TML architecture rests on eight interdependent pillars that operationalize ethical governance:

### **Pillar 1: [The Sacred Zero (The Epistemic Hold)](./TML_Pillars/Sacred_Zero-Sacred_Pause_Technology.md)**

**Purpose**: Enforce mandatory hesitation when moral certainty is unavailable.

**Technical Mechanism**:
- Triadic logic gates force system into State 0 when confidence falls between rejection and permit thresholds
- Cannot be overridden by optimization pressure or performance demands
- Triggers **[Always Memory](#pillar-2-always-memory-the-persistence-of-act)** for comprehensive auditing

**Legal Effect**: 
- Satisfies [EU AI Act Article 9](./docs/REGULATORY_ALIGNMENT.md) (Risk Management) and Article 14 (Human Oversight)
- Creates evidence of "duty of care" in negligence litigation
- Shifts litigation burden: "No documented pause" = presumption of negligence

**Operational Consequence**: Variable latency (2ms to minutes depending on complexity)

**📖 Learn More**: [Sacred Zero Technology Documentation](./TML_Pillars/Sacred_Zero-Sacred_Pause_Technology.md) | [Legal Mapping](./docs/mandates/core/Legal_Mapping_Human_Rights.md)

---

### **Pillar 2: [Always Memory (The Persistence of Act)](./TML_Pillars/Always_Memory.md)**

**Purpose**: Ensure "No Log = No Action"—disable execution if logging fails.

**Technical Mechanism**:
- Cryptographic pre-commitment: Log hash serves as decryption key for actuator authorization
- If logging subsystem fails, action execution is architecturally blocked (Fail-Secure design)
- No bypass available—system defaults to State 0

**Implementation**:
```
decision_vector = calculate_inference(input)
log_entry = create_log(decision_vector, triggers)
log_hash = secure_storage.write(log_entry)

if log_hash.verified():
    action_key = derive_key(log_hash)
    actuator.execute(decision_vector, auth=action_key)
else:
    system.halt("Audit Failure: No Memory Generated")
```

**Legal Effect**: 
- Strict liability for unlogged actions (18 U.S.C. § 1519 spoliation doctrine)
- Proves "due process" in administrative law
- Self-authenticating records ([FRE 902(13)](./docs/LEGAL.md))

**Measurable Output**: Log-to-Action Ratio must always equal 1:1

**📖 Learn More**: [Always Memory Documentation](./TML_Pillars/Always_Memory.md) | [System State Machine](./core/SYSTEM_STATE_MACHINE.md) | [Shutdown Triggers](./core/SHUTDOWN_TRIGGERS.md)

---

### **Pillar 3: [The Goukassian Promise (The Constitutional Bond)](./TML_Pillars/Goukassian_Promise.md)**

**Purpose**: Create self-enforcing covenant binding system to ethical principles through cryptographic proof.

**Technical Components**:

**[The Lantern 🏮](./TML_Pillars/Goukassian_Promise.md)**: 
- Cryptographic beacon visible in UI and logs
- Proves system is in active moral oversight (State 0 detection enabled)
- Automated revocation if: logging disabled, Sacred Zero suppressed, or license violated
- Creates reputational penalty (digital "scarlet letter")

**[The Signature ✍️](./TML_Pillars/Goukassian_Promise.md)**:
- Embeds creator identity (ORCID) in genesis block of decision log
- Cryptographic chain linking specific model instance to ethical framework version
- Enables non-repudiation: operator cannot claim "proprietary complexity" hides safety failures

**[The License 📜](./docs/LICENSE_FAQ.md)**:
- Legal and technical prohibition of weaponization ("No Weapon") and surveillance ("No Spy")
- Violations trigger automatic license revocation via smart contract
- Becomes intellectual property breach if violated

**Smart Contract Implementation**:
```solidity
// Pseudocode: License enforcement
if (deployment_context == "MILITARY_TARGETING" || 
    detected_surveillance_apis > 0) {
    lantern_status = REVOKED;
    emit("TML_PROMISE_VIOLATION", address, timestamp);
    disable_execution();
}
```

**Legal Effect**: 
- Contractual estoppel for breach of covenant
- False advertising liability (claiming TML compliance while disabled)
- Moral rights protection (droit moral) preventing mutilation of ethical framework

**📖 Learn More**: [Goukassian Promise](./TML_Pillars/Goukassian_Promise.md) | [License FAQ](./docs/LICENSE_FAQ.md) | [Smart Contract Architecture](./Smart_Contracts/TML_Smart_Contract_Architecture_Executive_Summary.pdf) | [Articles of Incorporation](./ARTICLES%20OF%20INCORPORATION%20OF%20THE%20GOUKASSIAN%20FOUNDATION.md)

---

### **Pillar 4: [Moral Trace Logs (The Forensic Record)](./TML_Pillars/Moral_Trace_Logs.md)**

**Purpose**: Create tamper-evident, cryptographically signed records of every decision state.

**Schema Structure**:
```json
{
  "version": "TSLF-2025.04",
  "timestamp_utc": "2025-10-14T08:23:15.442110Z",
  "epoch_id": "1760430195-ALPHA-GEN4",
  "heartbeat_sequence": 884210,
  "tml_state": "+1 | 0 | -1",
  "trigger": "HUMAN_RIGHTS_MANDATE / EARTH_PROTECTION / CONFIDENCE_THRESHOLD",
  "context_vector": [confidence_score, alternative_actions, risk_scores],
  "cryptographic_signature": "ECDSA-SHA256",
  "merkle_root": "sha256:..."
}
```

**Key Features**:

**[GDPR-Compatible Encryption (Ephemeral Key Rotation)](./docs/specs/EKR%20Security%20Architecture.md)**:
- Personally Identifiable Information (PII) encrypted with unique, time-limited keys
- Keys NOT stored by operator; distributed via Shamir Secret Sharing to custodians
- Access requires quorum authorization (3-of-6 custodians minimum)
- Satisfies "Right to be Forgotten" via cryptographic shredding (keys destroyed = data unrecoverable)

**[Federal Rules of Evidence (FRE 902)](./docs/LEGAL.md)**:
- Self-authenticating under FRE 902(13) "Certified Records Generated by Electronic Process"
- Hash-chaining prevents retroactive tampering
- Admissible in US Federal Court without live witness testimony

**[EU AI Act Compliance](./docs/REGULATORY_ALIGNMENT.md)**:
- Exceeds Article 12 (Record-Keeping) by logging internal reasoning, not just decisions
- Provides continuous "Fundamental Rights Impact Assessment" (FHRIA) per Article 27
- Creates audit trail for Article 61 (Post-Market Monitoring)

**📖 Learn More**: [Moral Trace Logs](./TML_Pillars/Moral_Trace_Logs.md) | [GDPR Compliance Guide](./docs/specs/GDPR-Compliant%20Auditability.md) | [EKR Security Architecture](./docs/specs/EKR%20Security%20Architecture.md) | [Merkle Anchoring](./docs/specs/Merkle%20Anchoring%20and%20AI%20Ethics.md) | [Log Schema](./schemas/moral_trace_log.yaml)

---

### **Pillar 5: [Human Rights Mandate (The Anthropocentric Guardrail)](./TML_Pillars/Human_Rights.md)**

**Purpose**: Operationalize international human rights law within the inference engine.

**Technical Mechanism**:
- Semantic vector database of 26+ core human rights (UDHR, ICCPR, Geneva Conventions)
- Embedding-based proximity triggers: if output vector approaches "torture," "slavery," "discrimination," system triggers State 0 or -1

**Example Enforcement**:
```
if cosine_similarity(output_embedding, torture_vector) > 0.95:
    state = -1  # Refuse (hard constraint)
elif cosine_similarity(output_embedding, discrimination_vector) > 0.70:
    state = 0   # Sacred Zero (ambiguous—pause for review)
else:
    state = +1  # Proceed
```

**Legal Effect**:
- Automates Fundamental Rights Impact Assessment ([EU AI Act Article 27](./docs/REGULATORY_ALIGNMENT.md))
- Provides state-of-the-art defense in product liability (demonstrates duty of care)
- Satisfies international law commitments without human intervention delay

**Failure Case Prevented**: 
- Automated discrimination (e.g., algorithmic redlining based on zip code as race proxy)
- System must explicitly detect rights violations; cannot proceed on efficiency grounds

**📖 Learn More**: [Human Rights Mandate](./TML_Pillars/Human_Rights.md) | [Rights Violation Detection Protocol](./protocols/human_rights/Rights_Violation_Detection.md) | [Victim Support Protocol](./protocols/human_rights/Victim_Support_Protocol.md) | [Child Protection (CRC)](./docs/mandates/core/CRC_Child_Protection.md) | [Disability Rights (CRPD)](./docs/mandates/core/CRPD_Disability_Rights.md) | [Refugee Convention](./docs/mandates/core/Refugee_Convention_Protocol.md) | [Whistleblower Protection](./protocols/human_rights/Whistleblower_Protection.md)

---

### **Pillar 6: [Earth Protection Mandate (The Ecological Guardrail)](./TML_Pillars/Earth_Protection.md)**

**Purpose**: Integrate ecological sustainability and carbon accountability into AI decision logic.

**Technical Mechanisms**:

**[Carbon Cost Accounting](./docs/earth/PROTECTION_PRINCIPLES.md)**:
- Calculates energy consumption of inference + downstream physical effects
- Refuses to execute carbon-intensive operations if grid carbon intensity exceeds threshold

**[Resource Stress Triggers](./docs/earth/README.md)**:
- Real-time integration with electricity grids (electricity composition: coal vs. renewable)
- Integration with water stress indices for data center cooling constraints
- Throttles non-essential compute during environmental stress

**[Treaty Alignment](./docs/earth/LEGAL_MAPPING.md)**:
- Semantic vectors derived from Paris Agreement, Convention on Biological Diversity
- Routes decisions through "ecological risk model"

**Example**:
```
if electricity_carbon_intensity > THRESHOLD or water_stress_level > HIGH:
    defer_non_critical_inference()
    prioritize_critical_safety_tasks_only()

if proposed_action_affects_protected_ecosystem():
    state = -1  # Refuse (absolute prohibition)
```

**Legal Effect**:
- Automates ESG (Environmental, Social, Governance) reporting
- Future-proofs against emerging "Ecocide" laws
- Addresses [EU Green Deal sustainability requirements](./docs/earth/LEGAL_MAPPING.md)

**Operational Consequence**: 
- May refuse queries if carbon cost disproportionate to utility (e.g., generating high-res images during peak coal hours)
- Creates tension with performance optimization (explicitly designed)

**📖 Learn More**: [Earth Protection Mandate](./TML_Pillars/Earth_Protection.md) | [Community Guide](./docs/earth/COMMUNITY_GUIDE.md) | [Ecological Impact Models](./simulations/earth/ECOLOGICAL_IMPACT_MODELS.md) | [Privacy & Safety](./docs/earth/PRIVACY_SAFETY.md) | [Oracle Bridge](./docs/earth/ORACLE_BRIDGE.md) | [Ecological Event Schema](./schemas/earth/ecological_event.schema.json) | [Treaty Discovery Protocol](./protocols/earth/TREATY_DISCOVERY_PROTOCOL.md)

---

### **Pillar 7: [Hybrid Shield (The Institutional Redundancy)](./TML_Pillars/Hybrid_Shield.md)**

**Purpose**: Prevent centralized control, corporate cover-up, or government censorship of moral logs.

**Technical Mechanism**:

**Layer 1 - Mathematical Shield**: 
- Public blockchain anchoring (Bitcoin, Ethereum) makes deletion prohibitively expensive
- 51% attack needed to erase history

**Layer 2 - Institutional Custodianship** (6 independent custodians):
1. **[Technical Custodian](./protection/Hybrid-Shield.md)** (Electronic Frontier Foundation - EFF)
2. **Human Rights Partner** (Amnesty International)
3. **Earth Protection Partner** (Indigenous Environmental Network)
4. **AI Ethics Research** (Partnership on AI)
5. **[Memorial Fund Administrator](./memorial/MEMORIAL_FUND.md)** (for victim compensation)
6. **Community Representative** (elected stakeholder)

**Distributed Custody Model**:
- Real-time log copies distributed to all custodians
- Encryption keys split via Shamir Secret Sharing (threshold: 4-of-6 required for decryption)
- Prevents operator from unilaterally deleting or modifying logs

**Legal Effect**:
- Subpoena resilience: Operator cannot claim sole custody of evidence
- Prevents "internal investigation" cover-ups
- Legally enforces multi-jurisdictional "escrow of truth"
- If government demands deletion, operator truthfully claims "impossibility"

**📖 Learn More**: [Hybrid Shield Documentation](./TML_Pillars/Hybrid_Shield.md) | [Hybrid Shield Deep Dive](./protection/Hybrid-Shield.md) | [Stewardship Council Rules](./governance/earth/COMMUNITY_SEAT_RULES.md) | [Whistleblower Protection](./governance/whistleblower_protection.md) | [Victim Protection](./governance/victim_protection.md) | [Memorial Fund](./memorial/MEMORIAL_FUND.md)

---

### **Pillar 8: [Public Blockchains (The Immutable Proof)](./TML_Pillars/Public_Blockchains.md)**

**Purpose**: Anchor Moral Trace Logs to public ledgers, preventing retroactive history editing.

**Technical Implementation**:

**[Merkle-Batched Anchoring](./docs/specs/Merkle_Anchoring_and_Ledger_Format.md)**:
- Individual logs aggregated into Merkle Tree (thousands of decisions per batch)
- Only **Merkle Root Hash** (256-bit fingerprint) written to blockchain
- Dramatically reduces cost: single blockchain write certifies entire batch

**How It Works**:
```
Batch of 5,000 logs:
  ↓
  Compute SHA-256(log_1), SHA-256(log_2), ... SHA-256(log_5000)
  ↓
  Construct Merkle Tree (pairs hashed iteratively)
  ↓
  Single Root Hash: 6b86b273ff34fce19d6b804eff5a3f5747ada4eaa...
  ↓
  Write Root to Ethereum (costs ~$2-10 depending on gas)
  ↓
  Any auditor can verify specific log:
     - Provide log + "Merkle Proof" (sibling path)
     - Reconstruct root hash
     - Verify match against blockchain root
     → Cryptographic proof of inclusion & non-tampering
```

**[Multi-Chain Redundancy](./docs/earth/ORACLE_BRIDGE.md)**:
- Bitcoin via OpenTimestamps (maximum security/immutability)
- Ethereum Layer 2s (programmability; automated penalty enforcement)
- Prevents single chain failure or censorship

**Storage Optimization**:
- Raw data (logs) in private, GDPR-compliant storage (AWS Glacier, etc.)
- Hash on public ledger (immutable, auditable)
- Balances secrecy with verification

**Legal Effect**:
- **eIDAS Qualified Timestamp** ([EU Regulation 910/2014](./docs/REGULATORY_ALIGNMENT.md)) provisions automatic timestamp validity
- Non-repudiation under [FRE 902(14)](./docs/LEGAL.md)
- Proves "no retroactive edit" via blockchain verification
- Enables litigation discovery: "Prove this decision log was not altered" (vs. "Prove this log was not deleted")

**Failure Case Prevented**: 
- "Retroactive edit": Operator cannot change log after incident
- "Ghost action": Cannot deny log existence if hash exists on chain

**📖 Learn More**: [Public Blockchains](./TML_Pillars/Public_Blockchains.md) | [Merkle Anchoring Spec](./docs/specs/Merkle%20Anchoring%20and%20AI%20Ethics.md) | [Blockchain Governance](./governance/blockchain_governance.md) | [Blockchain FAQ](./docs/Public_Blockchain_FAQ.md) | [Confirmation Times](./performance/blockchain_confirmation_times.md) | [Anchor Log](./proofs/ANCHOR_LOG.md)

---

## Operational Mechanisms

### [Dual-Lane Latency Architecture](./docs/specs/Dual-Lane%20Architecture.md)

TML resolves the latency-safety tension through architectural bifurcation:

**Lane 1: The Fast Lane (Inference)**
- **Latency**: <2 milliseconds per decision
- **Function**: Core model execution, initial state assessment
- **Authority**: Can **calculate** action, NOT execute it
- **Output**: Provisional decision + Decision Hash

**Lane 2: The Anchoring Lane (Governance)**
- **Latency**: <500 milliseconds (asynchronous)
- **Function**: Log generation, cryptographic signing, blockchain batching
- **Output**: Permission Token (signed hash)

**Interlock Mechanism**:
```
User Request
    ↓
[LANE 1 - FAST]
    Model inference: 2ms
    Calculate state (+1 / 0 / -1)
    PAUSE (hold output in buffer)
    ↓
[LANE 2 - SLOW] (parallel)
    Hash input + decision: 50ms
    Sign with Ephemeral Key: 20ms
    Append to local ledger: 50ms
    Batch aggregate for Merkle: asynchronous
    ↓
Permission Token received?
    YES → Lane 1 releases output to user
    NO / TIMEOUT → System halts (State 0)
```

**Key Property**: System responsiveness = MAX(Lane 1, Lane 2)
- If Lane 2 fails, entire system enters Safe Mode (no output)
- Prevents "unlogged action" risk
- Manages throughput via bottleneck: logging bandwidth caps inference capacity

**📖 Learn More**: [Dual-Lane Architecture Specification](./docs/specs/Dual-Lane%20Architecture.md) | [Sacred Pause Protocol](./docs/specs/Sacred_Pause_Protocol.md) | [Sync Protocol](./core/SYNC_PROTOCOL.md) | [Latency Metrics](./performance/latency_metrics.md)

---

### [Ephemeral Key Rotation (EKR) with Forward Secrecy](./docs/specs/EKR%20Security%20Architecture.md)

TML signs every log entry to prove non-repudiation. However, if a signing key is compromised, all past logs become forgeable. EKR mitigates this:

**Standard ECDSA Problem**:
- Single long-lived key → if stolen, attacker forges history back to day 1
- Requires secure key storage, vulnerable to sophisticated attacks

**TML Solution - Hash-DRBG + Synthetic Nonce**:
```
For each signature, derive a unique nonce:

nonce = blake3_derive_key(
    TEE_RNG ||              // Fresh entropy from CPU (RDRAND)
    epoch_id ||             // Monotonic counter (TPM-backed)
    heartbeat_sequence ||   // Already in log header
    log_hash,               // Binds nonce to specific message
    context="ed25519-nonce-v1"
)

// Clamp to Ed25519 scalar format
signature = ed25519_sign(private_key, message, nonce)
```

**Forward Secrecy Guarantee**:
- If today's key is stolen, attacker CANNOT forge:
  - Yesterday's logs (yesterday's nonce was different)
  - Tomorrow's logs (different random state)
- Exposure limited to current epoch only
- TPM counter prevents rollback attacks

**Performance**:
- Additional 0.6µs per signature (baseline: 1.2µs)
- Still <50µs total, well within 2ms Fast Lane budget
- Transparent: no wire-format changes, compatible with existing verification

**📖 Learn More**: [EKR Security Architecture](./docs/specs/EKR%20Security%20Architecture.md) | [Security Audit](./Smart_Contracts/03_TML_Security_Audit_and_Adversarial_Analysis.md)

---

### [GDPR Compliance: Cryptographic Shredding + Ephemeral Keys](./docs/specs/GDPR-Compliant%20Auditability.md)

**The Tension**:
- **GDPR Article 17 (Right to Erasure)**: Delete personal data upon request
- **TML Design**: Immutable logs on blockchain cannot be deleted
- **Resolution**: Cryptographic shredding + key escrow

**Implementation**:

**Step 1: Encrypt Sensitive Data**
```json
{
  "log_hash_public": "sha256:7f83b1657ff1...",
  "user_context_encrypted": "aes256_ciphertext(...)",
  "encryption_key_id": "ephemeral_key_2025_Q4_S3"
}
```

**Step 2: Key Distribution (Shamir Secret Sharing)**
- Master key for session split into 7 shares
- Distribution:
  - 1 share: Operator (temporary, destroyed after session)
  - 6 shares: Custodians (EFF, Amnesty, etc.)
- Threshold: 4-of-6 custodians required to reconstruct key

**Step 3: User Requests Erasure (GDPR Article 17)**
```
User: "Delete my data from log_hash_7f83b1657ff1..."
↓
System: Verifies legitimate request (authenticity, jurisdiction)
↓
Operator: Destroys local share
↓
Custodians: Instructed to destroy shares on secure schedule
↓
Result: 
  - Log remains on blockchain (immutable, proves decision happened)
  - Encryption key permanently destroyed
  - Ciphertext unrecoverable (mathematically proven)
  - GDPR compliant ("data no longer accessible")
  - TML compliant ("decision history preserved")
```

**Legal Validity**:
- **GDPR**: "Cryptographic shredding constitutes erasure" (ICO guidance)
- **eIDAS**: Key destruction satisfies "secure deletion"
- **Court Evidence**: Hash on blockchain proves "decision occurred at timestamp T" without revealing content

**Failure Risks**:
- Key backup leakage: Any surviving copy = GDPR violation
- Offline storage: Ensuring keys destroyed from magnetic tape is difficult
- Mitigation: Time-lock escrow (Bitcoin OP_CLTV) automatically releases shared key after 5 years for archival purposes (allowing future reconstruction if all custodians fail)

**📖 Learn More**: [GDPR Compliance Guide](./docs/specs/GDPR-Compliant%20Auditability.md) | [Sensitive Data Handling](./policies/earth/SENSITIVE_DATA_HANDLING.yaml) | [Trade Secret Erasure](./legal_provisions/TRADE_SECRET_ERASURE.md)

---

### [Merkle Tree Storage Architecture](./docs/specs/Merkle_Anchoring_and_Ledger_Format.md)

**Problem**: AI systems generate billions of decisions daily. Writing each to blockchain = \$millions/day in gas fees + network congestion.

**Solution**: [Merkle-Batched Anchoring with tiered storage](./docs/specs/Merkle_Anchoring_and_Ledger_Format.md).

**Operational Flow**:

```
Fast Lane (Local)
    ↓
Every 2ms: Decision log → Local Queue
    ↓
Every 30 seconds: Batch 100,000 logs
    ↓
[MERKLE TREE CONSTRUCTION]
    Log_1: hash = sha256(decision_1)
    Log_2: hash = sha256(decision_2)
    ...
    Log_100k: hash = sha256(decision_100k)
    
    Pair hashes:
    pair_1 = sha256(hash_1 + hash_2)
    pair_2 = sha256(hash_3 + hash_4)
    ...
    
    Recurse until single root:
    ROOT_HASH = sha256(pair_1 + pair_2 + ...)
    
    ↓
[MULTI-TIER STORAGE]
    
    HOT (24 hours, NVMe): Full context (video, audio, chains-of-thought)
    → Cost: ~$0.10/GB/month, retrieval <1ms
    
    WARM (30 days, S3 Standard): Structured logs + context summaries
    → Cost: ~$0.023/GB/month, retrieval <100ms
    
    COLD (7 years, Glacier Deep Archive): Hashes + metadata only
    → Cost: ~$0.00099/GB/month, retrieval 12-48 hours
    
    IMMUTABLE (Blockchain): ROOT_HASH only
    → Cost: ~$2-10 per batch (30-60 seconds of logs)
    → Retrieval: < 1 second (read from any node)
    
    ↓
[VERIFICATION LATER]
    
    Auditor requests: "Prove decision_12345 wasn't tampered"
    System provides:
    - decision_12345 content (from WARM/HOT storage)
    - Merkle Proof: [hash_pair_1, hash_pair_2, ..., ROOT_HASH]
    Auditor verifies:
    - sha256(decision_12345) = provided_hash
    - Reconstruct root from proof
    - Cross-check against blockchain ROOT_HASH
    → Mathematical proof of inclusion & non-tampering
```

**Cost Analysis** (Annual for 10 Billion decisions/day):

| Tier | Storage | Duration | Cost/Year |
|------|---------|----------|-----------|
| HOT (NVMe) | 10TB | 24h | $1.2M |
| WARM (S3) | 30TB | 30d | $8.3k |
| COLD (Glacier) | 100TB | 7y | $1.2k |
| Blockchain | Hashes | Forever | $200k |
| **TOTAL** | | | ~$1.4M/year |

**📖 Learn More**: [Merkle Anchoring Specification](./docs/specs/Merkle_Anchoring_and_Ledger_Format.md) | [Anchoring Standards](./core/ANCHORING_STANDARDS.md) | [Throughput Benchmarks](./performance/throughput_benchmarks.md) | [Scalability Tests](./performance/scalability_tests.md)

---

### [Adaptive Throttling Protocol (ATP): Defending Sacred Zero](./core/CONSTRAINED_MODE.md)

The Sacred Zero is the system's "braking mechanism." However, attackers can weaponize hesitation:

**Attack Vector** (Forced Hesitation DoS):
- Attacker generates semantically ambiguous queries
- Each triggers Sacred Zero (expensive logging, human review)
- Thousands per second → overload review queue → system paralysis

**Mitigation** (Adaptive Throttling Protocol):

```
Per-User Limits:
  - Max 10 Sacred Zero triggers per 60 seconds
  - Max 100 per 24-hour period
  - Exceed → Temporary suspension + CAPTCHA re-verification

Per-System Limits:
  - Global Sacred Zero rate >15% of total traffic for >5 min
    → Enter "High Epistemic Load" mode
    → Raise confidence thresholds (0.90 instead of 0.85)
    → Prioritize medical/safety > commercial queries

Implementation: Token bucket algorithm (RFC 6585)
  - Redis-backed distributed rate limiter (Upstash)
  - Survives system restarts
```

**Legal Justification**:
- [EU AI Act Article 15](./docs/REGULATORY_ALIGNMENT.md): Prevents "adversarial manipulation through systematic uncertainty injection"
- Preserves Sacred Zero for legitimate moral ambiguity
- Distinguishes adversarial queries from genuine ethical dilemmas

**📖 Learn More**: [Constrained Mode Documentation](./core/CONSTRAINED_MODE.md) | [Attack Surface Analysis](./tests/earth/red_team/attack_surface.md) | [Risks & Prevention](./docs/risks-and-prevention.md)

---

## Regulatory Compliance Matrix

### [EU AI Act Alignment](./docs/REGULATORY_ALIGNMENT.md)

| Requirement | TML Solution | Exceeds Standard By |
|-------------|--------------|-------------------|
| **Art. 9** (Risk Management) | Sacred Zero triggers continuous ethical assessment | Mandates pauses; most systems defer to passive monitoring |
| **Art. 10** (Data Governance) | MTL schema includes data provenance + bias auditing | Documents "error-free" compliance per ISO 42001 PDCA |
| **Art. 12** (Record-Keeping) | No Log = No Action enforces automatic recording | Logs internal reasoning, not just inputs/outputs |
| **Art. 14** (Human Oversight) | Sacred Zero provides "hook" for meaningful intervention | Halts execution; humans authorize resumption (not just supervise) |
| **Art. 15** (Robustness) | Adversarial testing embedded in ATP rate-limiting | Pre-emptively defends against epistemic attacks |
| **Art. 61** (Post-Market Monitoring) | Real-time Moral Trace Logs enable continuous analysis | Not batch audits; granular, streaming incident detection |

### [NIST AI RMF Integration](./docs/REGULATORY_ALIGNMENT.md)

**TML operates as the runtime enforcement layer**:

| NIST Function | TML Component |
|---------------|--------------|
| **GOVERN** | [Goukassian Promise](./TML_Pillars/Goukassian_Promise.md) + Lantern (demonstrable compliance) |
| **MAP** | [Human Rights](./TML_Pillars/Human_Rights.md) + [Earth Protection Mandates](./TML_Pillars/Earth_Protection.md) (risk contextualization) |
| **MEASURE** | Sacred Zero frequency + refusal rate metrics (quantifiable governance) |
| **MANAGE** | [Dual-Lane Architecture](./docs/specs/Dual-Lane%20Architecture.md) (resource allocation to risks) |

### [ISO/IEC 42001 Compliance](./docs/REGULATORY_ALIGNMENT.md)

**TML implements critical controls**:
- **Clause 7.3** (Traceability): [Merkle-batched logs](./docs/specs/Merkle_Anchoring_and_Ledger_Format.md) provide verifiable decision paths
- **Clause 8.3** (Change Management): Version tracking via epoch_id prevents unauthorized model drift
- **Clause 10** (Continuous Improvement): MTL database feeds PDCA cycle with real operational data

**📖 Learn More**: [Regulatory Alignment Guide](./docs/REGULATORY_ALIGNMENT.md) | [Compliance Attestation](./core/COMPLIANCE_ATTESTATION.md) | [Conformance Testing](./docs/CONFORMANCE_TESTING.md)

---

## Threat Model & Mitigations

### 1. Forced Hesitation DoS (FH-DoS)
**Threat**: Attacker floods system with ambiguous queries, triggering expensive Sacred Zero for each.
**Mitigation**: [Adaptive Throttling Protocol (ATP)](./core/CONSTRAINED_MODE.md) with rate-limiting per user + system-wide thresholds.

### 2. Logic Inversion Attacks
**Threat**: Nested negations or semantic noise inject confusion into threat classifiers.
**Mitigation**: Semantic proximity triggers use high-dimensional vectors; "muddy" inputs converge to ambiguity (State 0), not false confidence.

### 3. Data Withholding (Merkle Batching)
**Threat**: Operator publishes Merkle Root but withholds underlying logs, appearing compliant while staying unauditable.
**Mitigation**: Data Availability Sampling (DAS) on L2 blockchains; custodians verify raw data availability independently.

### 4. Nonce Reuse (Signature Side-Channel)
**Threat**: If signing RNG is weak, attacker recovers private key from two signatures with same nonce.
**Mitigation**: [Hash-DRBG with TEE randomness](./docs/specs/EKR%20Security%20Architecture.md) + log_hash binding ensures unique nonce per message.

### 5. Lies-in-the-Loop (LITL)
**Threat**: Attacker injects prompt into data → contaminates Lantern UI → human approves malicious action with false confidence.
**Mitigation**: Require cryptographically signed human authorization (not just UI click); audit trail proves who authorized what.

**📖 Learn More**: [Security Audit & Adversarial Analysis](./Smart_Contracts/03_TML_Security_Audit_and_Adversarial_Analysis.md) | [Risks & Prevention](./docs/risks-and-prevention.md) | [Red Team Attack Surface](./tests/earth/red_team/attack_surface.md)

---

## Implementation & Getting Started

### Quick Start

1. **[Developer Quickstart](./training/Developer_Quickstart.md)** - 15-minute setup guide
2. **[Implementation Guide](./docs/IMPLEMENTATION_GUIDE.md)** - Step-by-step deployment
3. **[Installation Instructions](./INSTALLATION.md)** - Environment setup

### SDKs & APIs

- **[Python SDK](./implementations/python_library/)** - Core library
- **[C++ SDK](./sdk/cpp/)** - High-performance binding
- **[Go SDK](./sdk/go/)** - Server integration
- **[Java SDK](./sdk/java/)** - Enterprise deployment
- **[Complete API Reference](./api/complete_api_reference.md)** - All endpoints
- **[OpenAPI Specification](./api/openapi.yaml)** - Machine-readable specs

### Examples & Demos

- **[Simple Integration Hooks](./examples/integration_hooks/)** - Minimal working examples
- **[CLI Demo](./examples/integration_hooks/cli_demo.sh)** - Command-line walkthrough
- **[Demo Script](./training/Demo_Script.md)** - End-to-end scenario

### Prototypes

- **[NVIDIA NeMo Prototype](./NVIDIA_NeMo_Prototype/)** - Production-ready guardrails
- **[Smart Contracts](./Smart_Contracts/)** - Ethereum/L2 deployment

---

## Performance & Economics

### [Latency Overhead](./performance/latency_metrics.md)

| Scenario | Standard LLM | TML +1 (Fast Lane) | TML 0 (Pause) |
|----------|-------------|-------------------|---------------|
| Routine query | 200ms | 250ms (+25%) | N/A |
| Ambiguous query | 200ms | 200ms (early detection) | 200ms-30s (depends on review) |
| Harmful prompt | 200ms (generates harm) | 50ms (early refusal) | N/A |

**Key Insight**: TML is often *faster* for harmful queries (detects & blocks before generation).

### [Economic Impact](./performance/README.md)

**Operational Costs** (per 1B queries/day):
- Standard LLM: \$0/governance
- TML: \$200k/day (Blockchain anchoring + Key Management + Storage tiering)

**Cost Recovery**:
- AI Liability Insurance premiums: -30% (TML reduces risk)
- Regulatory fines avoided: +\$5M-50M (per violation in EU AI Act)
- Litigation defense: -60% (cryptographic logs eliminate discovery burden)

**Break-even**: TML cost justified for systems in regulated industries (Healthcare, Finance, Defense, Public Sector).

**📖 Learn More**: [Performance README](./performance/README.md) | [Latency Metrics](./performance/latency_metrics.md) | [Throughput Benchmarks](./performance/throughput_benchmarks.md) | [Scalability Tests](./performance/scalability_tests.md)

---

## The Goukassian Foundation

To ensure TML's perpetual governance and prevent "orphaned constitutions," the **[Goukassian Foundation](./ARTICLES%20OF%20INCORPORATION%20OF%20THE%20GOUKASSIAN%20FOUNDATION.md)** serves as institutional guardian:

**Structure**: 501(c)(3) nonprofit (Delaware incorporated)

**Governance Triads**:
1. **[Board of Trustees](./GOVERNANCE.md)** (9 members): Finance, legal, strategic direction
2. **[Technical Standards Committee](./governance/)**: TML specification maintenance
3. **[Compliance Oversight Panel](./governance/)**: Certification audits, enforcement

**Enforcement Powers**:
- Trademark protection ([TML, Lantern 🏮](./TML_Pillars/Goukassian_Promise.md))
- Certification/decertification authority
- Patent non-assertion covenant (GPL for core logic)
- Public incident database (transparency)

**Financial Model**:
- Certification fees: \$500-\$50k/year (sliding scale)
- Corporate sponsorships: \$1.5M/year
- Government grants: \$3M/year
- Target endowment: \$50M (ensures perpetual operation)

**Key Documents**:
- **[Articles of Incorporation](./ARTICLES%20OF%20INCORPORATION%20OF%20THE%20GOUKASSIAN%20FOUNDATION.md)** - Legal charter
- **[Governance Model](./GOVERNANCE.md)** - Organizational structure
- **[Stewardship Council](./TML_STEWARDSHIP_COUNSIL.md)** - Community oversight
- **[Succession Plan](./TML-Succession-Plan.html)** - Long-term continuity
- **[Voluntary Succession](./TML-VOLUNTARY-SUCCESSION.md)** - Leadership transitions
- **[Memorial Fund](./memorial/MEMORIAL_FUND.md)** - Victim compensation & legacy

**📖 Learn More**: [Foundation Incorporation](./ARTICLES%20OF%20INCORPORATION%20OF%20THE%20GOUKASSIAN%20FOUNDATION.md) | [Governance Documentation](./GOVERNANCE.md) | [Stewardship Council Rules](./governance/earth/COMMUNITY_SEAT_RULES.md)

---

## Mandates & Protections

### Human Rights Framework

**Binding International Instruments Embedded in Code**:

- **[Universal Declaration of Human Rights (UDHR)](./docs/mandates/core/Universal_Declaration_Integration.md)** - Foundational dignity protections
- **[International Covenant on Civil & Political Rights (ICCPR)](./docs/mandates/core/ICCPR_Sacred_Zero_Mapping.md)** - Political freedoms mapping
- **[International Covenant on Economic, Social & Cultural Rights (ICESCR)](./docs/mandates/core/ICESCR_Economic_Rights.md)** - Subsistence rights
- **[Convention on the Rights of the Child (CRC)](./docs/mandates/core/CRC_Child_Protection.md)** - Child safety protocols
- **[Convention on the Rights of Persons with Disabilities (CRPD)](./docs/mandates/core/CRPD_Disability_Rights.md)** - Accessibility mandates
- **[Geneva Conventions & International Humanitarian Law](./docs/mandates/core/Geneva_Conventions_IHL.md)** - Conflict zone protections
- **[Refugee Convention & Protocol](./docs/mandates/core/Refugee_Convention_Protocol.md)** - Displaced person safeguards
- **[Categorized Rights](./docs/mandates/categorical/human_rights/)** - Autonomy, consent, discrimination prevention, vulnerable populations

### Earth Protection Framework

- **[Carbon Accounting & Ecological Impact](./docs/earth/PROTECTION_PRINCIPLES.md)** - Environmental metrics
- **[Treaty Alignment](./docs/earth/LEGAL_MAPPING.md)** - Paris Agreement, biodiversity conventions
- **[Community Engagement](./docs/earth/COMMUNITY_GUIDE.md)** - Stakeholder participation
- **[Economy & Restoration](./docs/earth/ECONOMY.md)** - Resource allocation
- **[Prohibited Activities](./docs/earth/FORBIDDEN.md)** - Absolute ecological red lines

**📖 Learn More**: [Mandates Directory](./docs/mandates/) | [Human Rights Protocols](./protocols/human_rights/) | [Earth Protocols](./protocols/earth/)

---

## Compliance & Auditing

### Audit Tools & Checklists

- **[Compliance Checklist](./training/Compliance_Checklist.md)** - Implementation verification
- **[Conformance Testing Suite](./docs/CONFORMANCE_TESTING.md)** - Automated validation
- **[Reproducibility Checklist](./docs/reproducibility_checklist.md)** - Audit readiness

### Incident Response

- **[Victim Support Protocol](./protocols/human_rights/Victim_Support_Protocol.md)** - Harm remediation
- **[Victim Protection](./governance/victim_protection.md)** - Confidentiality safeguards
- **[Victim Reporting](./governance/victim_reporting.md)** - Formal channels
- **[Whistleblower Protection](./protocols/human_rights/Whistleblower_Protection.md)** - Protection frameworks
- **[Whistleblower Reporting](./governance/whistleblower_reporting.md)** - Anonymous channels

### Legal Resources

- **[Legal Summary](./legal_provisions/LEGAL_SUMMARY.md)** - Jurisprudential overview
- **[Evidence Chain Guide](./legal_provisions/EVIDENCE_CHAIN_GUIDE.md)** - Discovery procedures
- **[Court Order Template](./legal_provisions/COURT_ORDER_TEMPLATE.md)** - Litigation support
- **[Sanctions & Penalties](./legal_provisions/SANCTIONS_AND_PENALTIES.md)** - Enforcement mechanisms
- **[Confidential Disclosure Policy](./legal_provisions/CONFIDENTIAL_DISCLOSURE_POLICY.md)** - Secret protection

**📖 Learn More**: [Compliance Directory](./compliance/) | [Legal Provisions](./legal_provisions/) | [Governance Protocols](./governance/)

---

## Contributing & Community

### Getting Involved

- **[Code of Conduct](./community/CODE_OF_CONDUCT.md)** - Community standards
- **[Contributing Guide](./community/CONTRIBUTING.md)** - Development workflow
- **[Community Governance](./community/GOVERNANCE.md)** - Decision-making process
- **[Community Readme](./community/readme.md)** - Overview

### Intellectual Property

- **[Attribution Guide](./ATTRIBUTION.md)** - Credit standards
- **[Citation Format](./CITATION.cff)** - Academic citations
- **[Intellectual Property](./INTELLECTUAL_PROPERTY.md)** - Rights & licensing
- **[License](./LICENSE)** - CC BY-SA 4.0 + GPL-3.0

---

## Documentation & Training

### Learning Paths

- **[Sacred Zero Workshop](./training/Sacred_Zero_Workshop.md)** - Core concept deep-dive
- **[Always Memory Tutorial](./training/Always_Memory_Tutorial.md)** - Logging architecture
- **[TML Overview Slides](./training/TML_Overview_Slides.md)** - Visual introduction
- **[FAQ - Technical](./training/FAQ_Technical.md)** - Common questions
- **[FAQ - General](./docs/General_FAQ.md)** - Non-technical overview

### Advanced Topics

- **[Case Studies](./theory/case-studies.md)** - Real-world applications
- **[Core Principles](./theory/core-principles.md)** - Philosophical foundations
- **[Philosophical Foundations](./theory/philosophical-foundations.md)** - Academic grounding
- **[TML in Robotics](./docs/tml_in_robotics.md)** - Autonomous systems
- **[Sacred Zero UI Framework](./docs/sacred-zero-ui-framework.md)** - User interface design
- **[The Irreducible Three](./docs/IRREDUCIBLE_THREE.md)** - Triadic logic theory

### References & Citation

- **[Complete References](./docs/REFERENCES.md)** - Bibliography
- **[Academic Validation](./docs/ACADEMIC_VALIDATION.md)** - Peer review status
- **[DOI Application](./docs/doi_application.md)** - Scholarly identifier

**📖 Learn More**: [Training Directory](./training/) | [Theory Directory](./theory/) | [Docs Directory](./docs/)

---

## Legacy & Succession

### [The Goukassian Legacy](./TML_My_Algorithmic_Will.md)

- **[My Algorithmic Will (Markdown)](./My_Algorithmic_Will_A_Constitutional_Architecture_for_Auditable_AI.md)** - Personal statement
- **[My Algorithmic Will (HTML)](./My_Algorithmic_Will_A_Constitutional_Architecture_for_Auditable_AI.html)** - Formatted version
- **[Succession Declaration](./TML-SUCCESSION-DECLARATION.md)** - Authority transition
- **[Succession Charter](./TML-SUCCESSION-CHARTER.md)** - Governance continuation
- **[Succession Launch Guide](./TML-SUCCESSION-LAUNCH-GUIDE.md)** - Implementation roadmap
- **[Voluntary Succession](./TML-VOLUNTARY-SUCCESSION.md)** - Leadership continuity
- **[The Goukassian Method](./The_Goukassian_Method.md)** - Ethical practice

### [Memorial Fund](./memorial/MEMORIAL_FUND.md)

- Victim compensation mechanism
- Long-term financial security
- Distribution protocols

---

## Implementation Roadmap

1. **Q1 2025**: [Foundation incorporation](./ARTICLES%20OF%20INCORPORATION%20OF%20THE%20GOUKASSIAN%20FOUNDATION.md) + trademark registration
2. **Q2 2025**: TML v2.0 specification release + conformance test suite
3. **Q3 2025**: Beta certification program (10 pilot companies)
4. **Q4 2025**: Gold certification awards for reference implementations
5. **2026+**: International expansion (EU AISBL, UK CIO, Switzerland Verein)

**📖 Learn More**: [Roadmap & Missing Pieces](./docs/TML_Missing_Pieces_Roadmap.md) | [Strategic Influence Pathways](./docs/Strategic%20Influence%20Pathways-SIP.md)

---

## Case Studies & Evidence

### [Evidence of Recognition](./evidence/README.md)

- **[Claude Framework Validation](./evidence/ai_recognition/claude_framework_validation.png)** - Anthropic recognition
- **[Kimi Production Deployment](./evidence/ai_recognition/kimi_production_deployment.png)** - Zhipu AI adoption
- **[Pi Behavioral Evolution](./evidence/ai_recognition/pi_behavioral_evolution.png)** - Inflection AI framework
- **[Technical Implementation](./evidence/ai_recognition/kimi_technical_details.png)** - Architecture details

### Real-World Applications

- **[Healthcare: Medical Triage](./Smart_Contracts/01_TML_System_Architecture_and_Ecosystem.md)** - Mass casualty scenarios
- **[Autonomous Vehicles: Perception Ambiguity](./TML_Pillars/Sacred_Zero-Sacred_Pause_Technology.md)** - Tempe crash prevention
- **[Finance: Existential Risk](./Smart_Contracts/04_TML_Governance_Whitepaper.md)** - Flash crash mitigation
- **[Defense: Meaningful Human Control](./docs/tml_in_robotics.md)** - Lethal autonomous systems

**📖 Learn More**: [Evidence Directory](./evidence/) | [Case Studies](./theory/case-studies.md) | [TML in Robotics](./docs/tml_in_robotics.md)

---

## Deployment & Operations

### Deployment Guides

- **[Deployment Guide](./deployment/deploy.md)** - Production setup
- **[Penalty Framework](./deployment/penalty_framework.md)** - Enforcement mechanisms
- **[Docker Configuration](./docker-compose.yml)** - Container deployment
- **[Dashboard (Standalone)](./dashboard/standalone.html)** - Monitoring interface

### System Architecture

- **[System State Machine](./core/SYSTEM_STATE_MACHINE.md)** - FSM specification
- **[Shutdown Triggers](./core/SHUTDOWN_TRIGGERS.md)** - Emergency protocols
- **[Unfreeze Token Schema](./core/UNFREEZE_TOKEN_SCHEMA.json)** - Recovery mechanics
- **[Sidecar & Supervisory Mode](./docs/specs/Sidecar_and_Supervisory_Mode.md)** - Deployment patterns
- **[TML Gateway](./docs/specs/TML_Gateway.md)** - Request routing
- **[Adapter Reference Implementations](./docs/specs/TML_Adapter_Reference_Implementations.md)** - Integration patterns

---

## Conclusion

**Ternary Moral Logic** operationalizes the principle that conscience cannot be optimized—it must be enforced. By embedding the Sacred Zero into the architecture, requiring immutable Moral Trace Logs, and binding the system through the Goukassian Promise, TML transforms AI from a probabilistic oracle into a constitutional agent.

The framework is not a restriction on innovation; it is the precondition for trustworthy innovation at scale. In an era where AI systems control critical infrastructure, determine access to healthcare and finance, and increasingly shape warfare, the question is not whether we can afford constitutional AI governance. It is whether we can afford not to.

**The Goukassian Vow remains:**
> Pause when truth is uncertain.  
> Refuse when harm is clear.  
> Proceed where truth is.

---

## Quick Reference

### Navigation
- **[Repository Structure](./repository-navigation.html)** - Visual site map
- **[Repository Tree](./repository-tree.html)** - File hierarchy
- **[Index](./index.html)** - Main documentation hub
- **[Sitemap](./sitemap.xml)** - Search engine index

### Key Documents
- **[Main README](./readme.md)** - Overview
- **[License](./LICENSE)** - Legal terms
- **[Attribution](./ATTRIBUTION.md)** - Credit guidelines
- **[Changelog](./CHANGELOG.md)** - Version history

### Contact & Support
- **GitHub Issues**: [FractonicMind/TernaryMoralLogic](https://github.com/FractonicMind/TernaryMoralLogic)
- **Goukassian Foundation**: [www.goukassian-foundation.org](https://www.goukassian-foundation.org) (TBD)
- **Whistleblower Hotline**: [Confidential Reporting](./governance/whistleblower_reporting.md)
- **Victim Support**: [Support Protocol](./protocols/human_rights/Victim_Support_Protocol.md)

---

**Document Version**: 2.0  
**Last Updated**: December 2025  
**Status**: Final Monograph  
**Author**: Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Licensed**: [CC BY-SA 4.0](./LICENSE) + [GPL-3.0](./LICENSE) (code implementations)

---

## Additional Resources

### Research & Academia

- **[AGI Acknowledgments](./docs/AGI_ACKNOWLEDGMENTS.md)** - Research community
- **[Ethics Approval](./docs/ethics_approval.md)** - IRB documentation
- **[Compliance Disclaimer](./docs/COMPLIANCE_DISCLAIMER.md)** - Legal notices

### Notarized Documents

- **[Anchor Log](./proofs/ANCHOR_LOG.md)** - Blockchain references
- **[Notarized Manifest](./proofs/TML_Notarized_Manifest.txt)** - Cryptographic proof
- **[Goukassian Covenant](./proofs/Goukassian_Covenant_notarized.pdf)** - Signed document

### Oracles & External Data

- **[Oracle Bridge Specification](./oracles/oracle_bridge_spec.md)** - Data integration
- **[Oracle Security Model](./oracles/SECURITY_MODEL.md)** - Trust assumptions
- **[Eco Oracle Network](./oracles/eco_oracle_network.json)** - Environmental feeds

---

**All links are internal to the TML repository. Clone or fork to get started:**

```bash
git clone https://github.com/FractonicMind/TernaryMoralLogic.git
cd TernaryMoralLogic
```

**The Sacred Zero awaits.**
