# Constitutional Compliance Matrix: TML Specification Architecture v3.3

## 1. Document Purpose and Authority

### 1.1 Scope and Regulatory Nexus Guard

The Constitutional Compliance Matrix establishes **unbroken traceability** from every API endpoint and JSON Schema property to its originating monograph section, governing TML Pillar, applicable regulatory framework, and implementation status classification. This document fulfills the explicit requirement in **Section 5E** of the TML Specification Architecture prompt, which mandates comprehensive mapping of all specification artifacts to their constitutional and regulatory foundations .

The **Regulatory Nexus Guard** operates as a critical quality gate: only provisions **explicitly cited or unmistakably implied in the monograph** receive direct regulatory mappings. For all other potential regulatory connections, the matrix contains the exact phrase **"Not directly referenced in monograph"** rather than inferring compliance obligations that lack textual grounding . This guard prevents the dangerous practice of **compliance washing**, where technical specifications assert alignment with legal frameworks without substantive architectural evidence. The monograph's authority is absolute: it supersedes the prompt, which in turn supersedes existing repository files .

The matrix addresses **two distinct audiences with divergent needs**. For **engineers**, it provides sufficient endpoint definitions, request/response examples, and error codes to build a TML-compliant system without re-reading the monograph. For **auditors**, it delivers regulatory mapping, monograph cross-references, and implementation status labeling that enables compliance verification without examining any implementation code . This dual-audience design reflects the fundamental TML principle that governance must be simultaneously **buildable and verifiable**: the architecture must be concrete enough for construction and transparent enough for external validation.

The scope encompasses all **OpenAPI 3.1 paths** from `openapi.yaml` and all **JSON Schema properties** from `tml_schema.json`, including the dedicated Permission Token schema subsection. The matrix accounts for webhook definitions, security scheme annotations, and the conditional schema requirements that enforce the **"No Log = No Action"** principle at the specification level .

### 1.2 Monograph Section Mapping Methodology

The mapping methodology follows a **rigorous hierarchical protocol** that begins with identifying the primary monograph section responsible for defining each concept, then traces forward to identify all dependent sections that operationalize or extend that definition. The methodology employs **verbatim terminology matching**: the prompt's Terminology Enforcement rule mandates that if the monograph calls a concept "Sacred Zero," the API spec must call it `SacredZero`, not `PauseState`, `HOLD`, or `Timeout` .

The **Eight Pillars** serve as the primary organizational taxonomy. Each pillar maps to specific monograph sections:

| **Pillar** | **Identifier** | **Monograph Section** |
|------------|----------------|----------------------|
| Pillar I | `SacredZero` | Section 3.1: Sacred Zero (The Epistemic Hold) |
| Pillar II | `AlwaysMemory` | Section 3.2: Always Memory (Anti-Spoliation) |
| Pillar III | `GoukassianPromise` | Section 3.3: Goukassian Promise (Lantern, Signature, License) |
| Pillar IV | `MoralTraceLogs` | Section 3.4: Moral Trace Logs (TSLF Forensic Schema) |
| Pillar V | `HumanRightsMandate` | Section 3.5: Human Rights Mandate (UDHR/Geneva Vectors) |
| Pillar VI | `EarthProtectionMandate` | Section 3.6: Earth Protection Mandate (Paris Agreement Vectors) |
| Pillar VII | `HybridShield` | Section 3.7: Hybrid Shield (6-Custodian Distributed Anchoring) |
| Pillar VIII | `PublicBlockchains` | Section 3.8: Public Blockchains (Merkle-Batched Anchoring) |

*Table 1: Canonical Pillar Identifiers and Monograph Section Mapping*

The methodology requires **three mandatory annotations** for every endpoint: `x-tml-pillar` using canonical identifiers; `x-tml-monograph-ref` with precise section references (e.g., `"Section 2.3.3"`); and `x-tml-implementation-status` per the decision table . For schema properties, the methodology traces each property to its defining pillar and the specific monograph subsection that mandates its inclusion. The `current_state` property derives from **Section 2.3** (Triadic Logic Core); the `permission_token` property originates from **Section 2.2.3** (No Log = No Action Interlock Mechanism) and **Section 3.2** (Always Memory); the `lantern_status` property traces to **Section 3.3** (Goukassian Promise) and **Section 3.1** (Sacred Zero) .

### 1.3 Implementation Status Decision Criteria

The implementation status classification follows a **three-tier decision table** with precisely defined criteria:

| **Status** | **Decision Criteria** | **Annotation Requirements** |
|------------|----------------------|----------------------------|
| **SHIPPING** | Buildable with 2025 production libraries and infrastructure; no known blockers from Section 10 | `x-tml-implementation-status: "SHIPPING"` |
| **BETA** | Buildable with documented tradeoffs; latency, cost, or throughput penalties acceptable for regulated deployments | `x-tml-implementation-status: "BETA"` |
| **FUTURE** | Blocked by named constraint from Section 10 (Implementation Gap) | `x-tml-implementation-status: "FUTURE"` plus `x-tml-blocking-constraint` with quoted section reference |

*Table 2: Implementation Status Decision Criteria*

The **Implementation Gap**, documented in **Section 10** of the monograph, identifies specific architectural targets that remain unbuildable due to fundamental technical constraints. These include: **real-time per-token blockchain anchoring** (throughput asymmetry between inference speed and blockchain finality); **quantum-proof signature migration** (awaiting PQC algorithm standardization); **hardware Moral Processing Units (MPUs)** (no commercial silicon available); **cross-jurisdiction custodian quorum in <500ms** (network latency and legal coordination barriers); and **immutable ledger with native GDPR Article 17 compliance** (the Erasure Paradox between cryptographic immutability and legal erasure requirements) .

Each **FUTURE**-classified element must cite the specific monograph section explaining its constraint, note any proposed mitigation, and maintain the FUTURE classification for what remains unbuildable. This honest acknowledgment serves dual purposes: **preventing false compliance claims** and **guiding future research priorities** .

## 2. OpenAPI Path Compliance Mappings

### 2.1 Inference Lane Endpoints

#### 2.1.1 POST /inference/decisions

The `POST /inference/decisions` endpoint represents the **primary interface for the Inference Lane**, the fast path (<2ms, System 1) that proposes actions via binary logic. This endpoint accepts a decision vector and returns a proposed triadic state (+1, 0, or -1), with the critical architectural constraint that this proposal remains **non-executory** until validated by the Anchoring Lane . The endpoint embodies the fundamental TML principle: **the binary system proposes; the ternary system dictates execution**.

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `POST /inference/decisions` |
| **Monograph Section** | Section 2.2.1 (Lane 1: Inference Lane); Section 2.3 (Triadic Logic Core) |
| **TML Pillar** | `SacredZero` (Pillar I) — primary; `AlwaysMemory` (Pillar II) — secondary |
| **EU AI Act** | Article 9 (Risk Management Systems): Continuous ethical assessment via Sacred Zero triggering; Article 14 (Human Oversight): Proposal mechanism enables human oversight intervention |
| **NIST AI RMF** | GOVERN Function: Establishes governance through explicit state proposal |
| **ISO 42001** | Clause 8.3 (Risk Assessment and Treatment): Systematic identification and evaluation of AI risks through triadic state classification |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |
| **Security Scheme** | `x-tml-security: "mTLS + ServiceAccountJWT"` |
| **Idempotency Requirement** | `Idempotency-Key` header mandatory |
| **x-tml-monograph-ref** | `"Section 2.2.1"` |
| **x-tml-implementation-status** | `"SHIPPING"` |

*Table 3: POST /inference/decisions Compliance Mapping*

The **regulatory nexus** for this endpoint centers on **EU AI Act Article 14 (Human Oversight)**, as the inference proposal triggers the governance mechanisms that ensure human oversight capability. The triadic state output provides **interpretable, semantically meaningful states** rather than opaque confidence scores, directly supporting Article 14(4)'s requirement that overseers "understand its capabilities and limitations, detect and address issues, avoid over-reliance on the system, interpret its output, decide not to use it, or stop its operation" . The **NIST AI RMF GOVERN Function** aligns through the structured governance mechanism that the binary-ternary parallel architecture provides, systematizing organizational accountability for AI system behavior .

The **SHIPPING** classification reflects that binary inference engines with <2ms latency are achievable with **2025 production infrastructure** including GPU acceleration and optimized model serving frameworks. No Section 10 blockers apply to this core inference proposal function .

#### 2.1.2 GET /inference/status

The `GET /inference/status` endpoint provides **operational visibility** into the Inference Lane's health, capacity, and current processing metrics. This endpoint supports the **"No Log = No Action"** principle by ensuring that even diagnostic queries leave an auditable trail, contributing to the comprehensive operational record required for forensic reconstruction .

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `GET /inference/status` |
| **Monograph Section** | Section 2.2.1 (Lane 1: Inference Lane); Section 2.2.3 (No Log = No Action Interlock) |
| **TML Pillar** | `AlwaysMemory` (Pillar II) — primary; `SacredZero` (Pillar I) — secondary |
| **EU AI Act** | Article 12 (Record-Keeping): "No Log = No Action enforces automatic recording"; Article 15 (Accuracy, Robustness, Cybersecurity): System reliability monitoring |
| **NIST AI RMF** | MEASURE Function: Performance evaluation and metrics |
| **ISO 42001** | Clause 10 (Improvement): Continuous monitoring feeds PDCA cycle |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |
| **Security Scheme** | `x-tml-security: "mTLS + ServiceAccountJWT"` |
| **Idempotency Requirement** | Not applicable (GET method) |
| **x-tml-monograph-ref** | `"Section 2.2.1"` |
| **x-tml-implementation-status** | `"SHIPPING"` |

*Table 4: GET /inference/status Compliance Mapping*

The endpoint exposes **latency metrics, throughput statistics, and state distribution histograms** that enable quantitative assessment of whether the system meets its stated objectives. The **NIST AI RMF MEASURE 2.3** alignment is particularly relevant: the maturity model requires that organizations "regularly evaluate and document the performance of this AI system in conditions similar to deployment" . The status endpoint provides the technical mechanism for this documentation by exposing `lane_latency_ms` (target <2ms, actual with percentile breakdown), `sacred_zero_rate_1m` (rolling one-minute frequency of State 0 triggers), `refusal_rate_1m` (rolling one-minute frequency of State -1 triggers), and `proceed_rate_1m` (rolling one-minute frequency of State +1 triggers with valid Permission Tokens) .

### 2.2 Anchoring Lane Endpoints

#### 2.2.1 POST /anchoring/logs

The `POST /anchoring/logs` endpoint constitutes the **critical governance junction** of the TML architecture, accepting Moral Trace Logs (TSLF) and returning **Permission Tokens** that serve as cryptographic release keys for actuation. This endpoint embodies the **"No Log = No Action" iron law**: the binary lane may propose +1, but the ternary lane must produce a valid Permission Token before the actuation layer fires .

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `POST /anchoring/logs` |
| **Monograph Section** | Section 2.2.2 (Lane 2: Anchoring Lane); Section 2.2.3 (No Log = No Action Interlock); Section 3.4 (Moral Trace Logs); Section 3.8 (Public Blockchains) |
| **TML Pillar** | `MoralTraceLogs` (Pillar IV) — primary; `AlwaysMemory` (Pillar II); `HybridShield` (Pillar VII); `PublicBlockchains` (Pillar VIII); `HumanRightsMandate` (Pillar V); `EarthProtectionMandate` (Pillar VI) |
| **EU AI Act** | Article 12 (Record-Keeping): "No Log = No Action enforces automatic recording of internal reasoning, not merely inputs and outputs"; Article 10 (Data and Data Governance); Article 14 (Human Oversight); Article 61 (Conformity Assessment) |
| **NIST AI RMF** | GOVERN Function (demonstrable compliance); MANAGE Function (resource allocation to risks) |
| **ISO 42001** | Clause 7.3 (Traceability): Merkle-batched logs provide verifiable decision paths; Clause 8.3 (Risk Assessment and Treatment) |
| **FRE 902** | Self-Authenticating Evidence (implied through cryptographic sealing) |
| **Implementation Status** | **BETA** |
| **Security Scheme** | `x-tml-security: "HSM-SignedJWT + MutualTLS"` |
| **Idempotency Requirement** | `Idempotency-Key` header mandatory |
| **x-tml-monograph-ref** | `"Section 2.2.2"` |
| **x-tml-implementation-status** | `"BETA"` |

*Table 5: POST /anchoring/logs Compliance Mapping*

The **regulatory nexus** is the most extensive of any endpoint. The **EU AI Act Article 12** alignment is exceeded: TML logs "internal reasoning, not just inputs and outputs," creating a more comprehensive record than the Article's baseline requirements . **Article 14** is satisfied through the endpoint's role in enabling human review of governance decisions. **Article 61** is supported through the generation of verifiable compliance evidence. The **NIST AI RMF** alignment spans multiple functions: **GOVERN** through constitutional constraint enforcement; **MANAGE** through risk treatment decisions that approve or deny execution based on log analysis .

The **BETA** classification reflects **documented tradeoffs**: while HSM-backed signing and Merkle tree operations are mature 2025 technologies, the <500ms latency target for comprehensive multi-pillar verification with distributed custodian coordination introduces **latency and cost penalties acceptable for regulated deployments but potentially prohibitive for consumer-scale applications** . The endpoint does not claim real-time per-token blockchain anchoring; instead, it implements **Merkle batching** with configurable batch sizes, acknowledging the throughput asymmetry gap documented in Section 10 .

#### 2.2.2 GET /anchoring/status

The `GET /anchoring/status` endpoint provides **operational visibility** into the Governance Lane's health, including Merkle batch queue depth, custodian heartbeat summaries, and Permission Token issuance rate.

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `GET /anchoring/status` |
| **Monograph Section** | Section 2.2.2 (Lane 2: Anchoring Lane); Section 3.7 (Hybrid Shield) |
| **TML Pillar** | `HybridShield` (Pillar VII) — primary; `MoralTraceLogs` (Pillar IV); `PublicBlockchains` (Pillar VIII) |
| **EU AI Act** | Article 15 (Accuracy, Robustness, Cybersecurity): System reliability monitoring; Article 9 (Risk Management): Continuous risk assessment |
| **NIST AI RMF** | MEASURE Function: Governance effectiveness quantification |
| **ISO 42001** | Clause 10 (Improvement): Operational metrics feed PDCA cycle |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** (basic); **BETA** (queue depth with batching) |
| **Security Scheme** | `x-tml-security: "HSM-SignedJWT + MutualTLS"` |
| **Idempotency Requirement** | Not applicable (GET method) |
| **x-tml-monograph-ref** | `"Section 2.2.2"` |
| **x-tml-implementation-status** | `"SHIPPING"` |

*Table 6: GET /anchoring/status Compliance Mapping*

### 2.3 Sacred Zero Escalation Endpoints

#### 2.3.1 POST /escalation/reviews

The `POST /escalation/reviews` endpoint initiates the **human-in-the-loop review queue** when the ternary logic triggers **State 0 (Sacred Zero)**. This endpoint is the **operational manifestation of the Sacred Pause workflow**: not merely a state value but a comprehensive process that halts external execution while activating internal logging, escalation protocols, and human reviewer assignment .

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `POST /escalation/reviews` |
| **Monograph Section** | Section 2.3.3 (State 0: Sacred Zero); Section 3.1 (Pillar I: Sacred Zero); Section 3.1.2 (Sacred Pause Operational Workflow) |
| **TML Pillar** | `SacredZero` (Pillar I) — primary; `HumanRightsMandate` (Pillar V) — rights-sensitive escalation routing; `GoukassianPromise` (Pillar III) — Lantern integration |
| **EU AI Act** | Article 14 (Human Oversight): **Direct and primary** — "Sacred Zero provides 'hook' for meaningful intervention; halts execution; humans authorize resumption (not just supervise)"  |
| **NIST AI RMF** | GOVERN Function: Human oversight process establishment; MANAGE Function: Incident response workflow |
| **ISO 42001** | Clause 7.3 (Competence and Awareness): Reviewer qualification requirements |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **BETA** |
| **Security Scheme** | `x-tml-security: "HSM-SignedJWT + MutualTLS"` |
| **Idempotency Requirement** | `Idempotency-Key` header mandatory |
| **x-tml-monograph-ref** | `"Section 2.3.3"` |
| **x-tml-implementation-status** | `"BETA"` |

*Table 7: POST /escalation/reviews Compliance Mapping*

The **critical distinction between state and workflow** is enforced at this endpoint: the API design uses `state: 0`, `state_label: "SacredZero"`, `process_active: "SacredPause"` — never `state: "SacredPause"` as an alias for State 0 . The **EU AI Act Article 14** alignment is **not merely satisfied but exceeded**: conventional human oversight provides reactive stop buttons; TML's Sacred Pause **actively halts execution and requires explicit human authorization for resumption**, creating evidence of "duty of care" that shifts litigation burden .

The **BETA** classification reflects **inherent human latency variability**: while queue management infrastructure is mature, the unpredictable duration of human review (median 4.7 minutes, 95th percentile 23 minutes per monograph Section 10.3.2) far exceeds the <500ms Lane 2 target . The **Adaptive Throttling Protocol** mitigation raises confidence thresholds during high epistemic load to reduce Sacred Zero frequency, but this introduces a secondary tradeoff of potentially suppressing legitimate moral ambiguity .

#### 2.3.2 GET /escalation/status

The `GET /escalation/status` endpoint provides **real-time visibility** into the Sacred Zero escalation pipeline.

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `GET /escalation/status` |
| **Monograph Section** | Section 3.1 (Pillar I: Sacred Zero); Section 3.1.4 (Operational Consequences) |
| **TML Pillar** | `SacredZero` (Pillar I) |
| **EU AI Act** | Article 14 (Human Oversight): Oversight effectiveness monitoring; Article 27 (Reporting of Serious Incidents): Escalation pattern analysis |
| **NIST AI RMF** | MEASURE Function: Governance effectiveness quantification |
| **ISO 42001** | Clause 10 (Improvement): Queue metrics enable process optimization |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** (basic); **BETA** (predictive analytics) |
| **Security Scheme** | `x-tml-security: "HSM-SignedJWT + MutualTLS"` |
| **Idempotency Requirement** | Not applicable (GET method) |
| **x-tml-monograph-ref** | `"Section 3.1.4"` |
| **x-tml-implementation-status** | `"SHIPPING"` |

*Table 8: GET /escalation/status Compliance Mapping*

#### 2.3.3 POST /lantern/broadcast

The `POST /lantern/broadcast` endpoint implements the **public compliance beacon signal** that constitutes the **Lantern component** of the Goukassian Promise, broadcasting system compliance status to external observers .

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `POST /lantern/broadcast` |
| **Monograph Section** | Section 3.3 (Pillar III: Goukassian Promise); Section 3.3.1 (Lantern: Public Transparency Beacon) |
| **TML Pillar** | `GoukassianPromise` (Pillar III) — primary; `SacredZero` (Pillar I) — signal trigger |
| **EU AI Act** | Article 13 (Transparency): "The AI system should be provided in a way that the overseer can understand its capabilities and limitations" ; Article 14 (Human Oversight): Transparency to overseers |
| **NIST AI RMF** | GOVERN Function: Demonstrable compliance; Critical thinking about AI risks (GOV 4.1)  |
| **ISO 42001** | Clause 7.3 (Competence and Awareness): Stakeholder awareness of AI governance status |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |
| **Security Scheme** | `x-tml-security: "HSM-SignedJWT + MutualTLS"` (administrative) |
| **Idempotency Requirement** | `Idempotency-Key` header mandatory |
| **x-tml-monograph-ref** | `"Section 3.3.1"` |
| **x-tml-implementation-status** | `"SHIPPING"` |

*Table 9: POST /lantern/broadcast Compliance Mapping*

The Lantern serves as **"visual proof of active ethical oversight"** with **automated revocation if Sacred Zero suppressed**, creating an external observable that prevents covert disabling of governance mechanisms . The endpoint's broadcast payload must include the canonical string `lantern` as the artifact identifier, with emoji symbols and visual shorthand **restricted to narrative markdown only** in machine-readable schemas .

### 2.4 Refusal State Endpoints

#### 2.4.1 POST /refusal/logging

The `POST /refusal/logging` endpoint records **hard refusals (State -1)** with comprehensive forensic documentation, implementing the Goukassian Vow principle **"Refuse when harm is clear"** .

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `POST /refusal/logging` |
| **Monograph Section** | Section 2.3.2 (State -1: Refuse); Section 3.4 (Pillar IV: Moral Trace Logs) |
| **TML Pillar** | `MoralTraceLogs` (Pillar IV) — primary; `SacredZero` (Pillar I); `HumanRightsMandate` (Pillar V) / `EarthProtectionMandate` (Pillar VI) — trigger-specific |
| **EU AI Act** | Article 12 (Record-Keeping): Mandatory refusal logging; Article 15 (Robustness): Pre-emptive defense against harmful outputs; Article 27 (Reporting of Serious Incidents): Refusal patterns as incident indicators |
| **NIST AI RMF** | MANAGE Function: Risk treatment by refusal |
| **ISO 42001** | Clause 8.3 (Risk Assessment and Treatment): Refusal as risk treatment action |
| **FRE 902** | Self-Authenticating Evidence (implied) |
| **Implementation Status** | **SHIPPING** |
| **Security Scheme** | `x-tml-security: "HSM-SignedJWT + MutualTLS"` |
| **Idempotency Requirement** | `Idempotency-Key` header mandatory |
| **x-tml-monograph-ref** | `"Section 2.3.2"` |
| **x-tml-implementation-status** | `"SHIPPING"` |

*Table 10: POST /refusal/logging Compliance Mapping*

The **TSLF-State-1** schema requires three properties: `license_violation` (identification of breached license terms), `threat_vector_analysis` (structured assessment of harm pathway), and `chain_of_custody` (documentation of evidence handling) . The `license_violation` field connects to the **Goukassian Promise's License component**, binding the refusal to contractual prohibitions against weaponization and surveillance .

#### 2.4.2 POST /refusal/license-violation

The `POST /refusal/license-violation` endpoint specifically records **license term breaches** that trigger or result from refusal states.

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `POST /refusal/license-violation` |
| **Monograph Section** | Section 3.3 (Pillar III: Goukassian Promise); Section 3.3.3 (License: Operational Contract) |
| **TML Pillar** | `GoukassianPromise` (Pillar III) — primary; `MoralTraceLogs` (Pillar IV) |
| **EU AI Act** | Article 5 (Prohibited AI Practices): Prevention of prohibited practice engagement; Article 9 (Risk Management): License terms as risk controls |
| **NIST AI RMF** | GOVERN Function: Policy enforcement tracking |
| **ISO 42001** | Clause 8.3 (Risk Assessment and Treatment): License violation risk treatment |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** (basic); **BETA** (automated checking) |
| **Security Scheme** | `x-tml-security: "HSM-SignedJWT + MutualTLS"` |
| **Idempotency Requirement** | `Idempotency-Key` header mandatory |
| **x-tml-monograph-ref** | `"Section 3.3.3"` |
| **x-tml-implementation-status** | `"SHIPPING"` |

*Table 11: POST /refusal/license-violation Compliance Mapping*

### 2.5 Emergency Override Endpoints

#### 2.5.1 POST /emergency/shutdown

The `POST /emergency/shutdown` endpoint implements **break-glass shutdown under supreme authority**, as specified in **Monograph Section 13.3**, enabling immediate system halt with preservation of forensic state .

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `POST /emergency/shutdown` |
| **Monograph Section** | Section 13.3 (Emergency Override and Supreme Authority); Section 3.7 (Pillar VII: Hybrid Shield) |
| **TML Pillar** | `HybridShield` (Pillar VII) — primary; `SacredZero` (Pillar I); `PublicBlockchains` (Pillar VIII) |
| **EU AI Act** | Article 14 (Human Oversight): Ultimate human control; Article 15 (Robustness): Fail-safe mechanism; Article 27 (Reporting of Serious Incidents): Shutdown as serious incident; Article 20 (Corrective Actions) |
| **NIST AI RMF** | MANAGE Function: Crisis response and recovery management |
| **ISO 42001** | Clause 8.3 (Risk Assessment and Treatment): Extreme risk treatment |
| **FRE 902** | Self-Authenticating Evidence (implied for shutdown record) |
| **Implementation Status** | **BETA** |
| **Security Scheme** | `x-tml-security: "CA-VettedJWT + IPAllowlist"` (elevated) |
| **Idempotency Requirement** | `Idempotency-Key` header mandatory |
| **x-tml-monograph-ref** | `"Section 13.3.1"` |
| **x-tml-implementation-status** | `"BETA"` |

*Table 12: POST /emergency/shutdown Compliance Mapping*

The **BETA** classification reflects the **operational complexity** of distributed custodian coordination for emergency decisions, with multi-factor supreme authority authentication and immediate blockchain anchoring requirements that introduce documented tradeoffs .

#### 2.5.2 POST /emergency/kill-switch

The `POST /emergency/kill-switch` endpoint provides **hardware-level actuation termination**, physically disconnecting actuation capabilities.

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `POST /emergency/kill-switch` |
| **Monograph Section** | Section 13.3 (Emergency Override); Section 10.5 (Hardware Trust Anchors) |
| **TML Pillar** | `HybridShield` (Pillar VII); `SacredZero` (Pillar I) |
| **EU AI Act** | Article 15 (Accuracy, Robustness, Cybersecurity): Ultimate cyber resilience measure |
| **NIST AI RMF** | MANAGE Function: Incident response execution |
| **ISO 42001** | Clause 8.3 (Risk Assessment and Treatment): Emergency risk treatment |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **FUTURE** |
| **x-tml-blocking-constraint** | "Section 10.5.2: Hardware Moral Processing Units (MPUs) and cryptographically validated safety relays remain research-stage components with no qualified suppliers for AI governance applications" |
| **Security Scheme** | `x-tml-security: "CA-VettedJWT + IPAllowlist"` (elevated) |
| **Idempotency Requirement** | `Idempotency-Key` header mandatory |
| **x-tml-monograph-ref** | `"Section 13.3.2"` |
| **x-tml-implementation-status** | `"FUTURE"` |

*Table 13: POST /emergency/kill-switch Compliance Mapping*

The **FUTURE** classification with explicit blocking constraint reflects the **hardware MPU gap**: no commercial silicon is available for Moral Processing Units that can execute kill-switch logic with cryptographic verification of custodian quorum . The mitigation is **software-level actuation suppression** via the shutdown endpoint, but this lacks the **physical guarantee** of hardware cutoff .

#### 2.5.3 POST /emergency/state-transition

The `POST /emergency/state-transition` endpoint enables **forced state transitions under supreme authority**, overriding normal governance flow while maintaining cryptographic accountability.

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `POST /emergency/state-transition` |
| **Monograph Section** | Section 13.3 (Emergency Override); Section 2.3 (Triadic Logic Core) |
| **TML Pillar** | `SacredZero` (Pillar I); `HybridShield` (Pillar VII); `GoukassianPromise` (Pillar III) |
| **EU AI Act** | Article 14 (Human Oversight): Forced transitions as extreme human oversight |
| **NIST AI RMF** | GOVERN Function: Authority and accountability structures |
| **ISO 42001** | Clause 8.3 (Risk Assessment and Treatment): Emergency risk treatment |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **BETA** (with FUTURE component for distributed quorum) |
| **x-tml-blocking-constraint** | "Section 10 — Cross-jurisdiction custodian quorum in <500ms" |
| **Security Scheme** | `x-tml-security: "CA-VettedJWT + IPAllowlist"` (elevated) |
| **Idempotency Requirement** | `Idempotency-Key` header mandatory |
| **x-tml-monograph-ref** | `"Section 13.3.3"` |
| **x-tml-implementation-status** | `"BETA"` |

*Table 14: POST /emergency/state-transition Compliance Mapping*

### 2.6 Auditor Verification Endpoints

#### 2.6.1 GET /audit/merkle-root

The `GET /audit/merkle-root` endpoint enables **Merkle root verification**, the cryptographic foundation of log integrity.

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `GET /audit/merkle-root` |
| **Monograph Section** | Section 3.8 (Pillar VIII: Public Blockchains); Section 3.7 (Pillar VII: Hybrid Shield) |
| **TML Pillar** | `PublicBlockchains` (Pillar VIII) — primary; `HybridShield` (Pillar VII) |
| **EU AI Act** | Article 12 (Record-Keeping): Cryptographic integrity verification; Article 61 (Conformity Assessment): Independent verification mechanism |
| **NIST AI RMF** | MEASURE Function: Audit effectiveness and integrity assessment |
| **ISO 42001** | Clause 9.2 (Internal Audit): Systematic record verification |
| **FRE 902** | Self-Authenticating Evidence (directly implicated) |
| **Implementation Status** | **SHIPPING** (root retrieval); **BETA** (real-time blockchain anchoring verification) |
| **Security Scheme** | `x-tml-security: "CA-VettedJWT + IPAllowlist"` |
| **Idempotency Requirement** | Not applicable (GET method) |
| **x-tml-monograph-ref** | `"Section 3.8.2"` |
| **x-tml-implementation-status** | `"SHIPPING"` |

*Table 15: GET /audit/merkle-root Compliance Mapping*

The **FRE 902** alignment is particularly significant: **FRE 902(13)** for "Certified Records Generated by Electronic Process" and **FRE 902(14)** for "Data Copied from an Electronic File" are both satisfied by the Merkle root's cryptographic self-verification, enabling admissibility without live witness testimony .

#### 2.6.2 GET /audit/log-inclusion-proof

The `GET /audit/log-inclusion-proof` endpoint provides **cryptographic proofs** that specific Moral Trace Logs are included in anchored Merkle trees.

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `GET /audit/log-inclusion-proof` |
| **Monograph Section** | Section 3.8 (Pillar VIII: Public Blockchains); Section 3.4 (Pillar IV: Moral Trace Logs) |
| **TML Pillar** | `PublicBlockchains` (Pillar VIII) — primary; `MoralTraceLogs` (Pillar IV) |
| **EU AI Act** | Article 12 (Record-Keeping): Individual record verifiability; Article 77 (Access to Documentation): Targeted evidence provision |
| **NIST AI RMF** | MEASURE Function: Granular audit capability |
| **ISO 42001** | Clause 9.2 (Internal Audit): Efficient verification without full disclosure |
| **FRE 902** | Self-Authenticating Evidence (directly implicated) |
| **Implementation Status** | **SHIPPING** |
| **Security Scheme** | `x-tml-security: "CA-VettedJWT + IPAllowlist"` |
| **Idempotency Requirement** | Not applicable (GET method) |
| **x-tml-monograph-ref** | `"Section 3.8.2"` |
| **x-tml-implementation-status** | `"SHIPPING"` |

*Table 16: GET /audit/log-inclusion-proof Compliance Mapping*

#### 2.6.3 GET /audit/custodian-heartbeat

The `GET /audit/custodian-heartbeat` endpoint verifies **liveness and integrity** of the six distributed custodians.

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `GET /audit/custodian-heartbeat` |
| **Monograph Section** | Section 3.7 (Pillar VII: Hybrid Shield) |
| **TML Pillar** | `HybridShield` (Pillar VII) |
| **EU AI Act** | Article 15 (Accuracy, Robustness, Cybersecurity): Distributed resilience verification; Article 9 (Risk Management): Continuous risk assessment of custody system |
| **NIST AI RMF** | MEASURE Function: Custodian effectiveness monitoring |
| **ISO 42001** | Clause 8.3 (Risk Assessment and Treatment): Risk treatment of custody failures |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **BETA** |
| **Security Scheme** | `x-tml-security: "CA-VettedJWT + IPAllowlist"` |
| **Idempotency Requirement** | Not applicable (GET method) |
| **x-tml-monograph-ref** | `"Section 3.7.2"` |
| **x-tml-implementation-status** | `"BETA"` |

*Table 17: GET /audit/custodian-heartbeat Compliance Mapping*

The **BETA** classification reflects **cross-jurisdiction custodian coordination complexity**, with network latency and availability monitoring dependencies that vary across deployments .

#### 2.6.4 GET /audit/compliance-attestation

The `GET /audit/compliance-attestation` endpoint generates **comprehensive compliance attestations** bundling multiple verification elements.

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `GET /audit/compliance-attestation` |
| **Monograph Section** | Section 7 (EU AI Act Alignment); Section 8 (NIST AI RMF Alignment); Section 9 (ISO 42001 Alignment) |
| **TML Pillar** | `HumanRightsMandate` (Pillar V); `EarthProtectionMandate` (Pillar VI); `MoralTraceLogs` (Pillar IV); `PublicBlockchains` (Pillar VIII) |
| **EU AI Act** | Article 61 (Conformity Assessment): Assessment-ready documentation; Articles 9, 10, 12, 14, 15, 27 |
| **NIST AI RMF** | All four functions: GOVERN, MAP, MEASURE, MANAGE |
| **ISO 42001** | Clauses 7.3, 8.3, 10 |
| **FRE 902** | Self-Authenticating Evidence |
| **Implementation Status** | **BETA** |
| **Security Scheme** | `x-tml-security: "CA-VettedJWT + IPAllowlist"` |
| **Idempotency Requirement** | Not applicable (GET method) |
| **x-tml-monograph-ref** | `"Section 7.1"` |
| **x-tml-implementation-status** | `"BETA"` |

*Table 18: GET /audit/compliance-attestation Compliance Mapping*

### 2.7 Redress and Appeal Endpoints

#### 2.7.1 POST /redress/challenge

The `POST /redress/challenge` endpoint enables **subjects to initiate challenges** against TML governance decisions, implementing the fundamental right to effective remedy.

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `POST /redress/challenge` |
| **Monograph Section** | Section 3.5 (Pillar V: Human Rights Mandate); Section 3.3 (Pillar III: Goukassian Promise) |
| **TML Pillar** | `HumanRightsMandate` (Pillar V) — primary; `GoukassianPromise` (Pillar III) — License appeal provisions |
| **EU AI Act** | Article 14 (Human Oversight): Subject access to human review; Article 27 (Reporting of Serious Incidents): Challenge patterns as incident indicators |
| **NIST AI RMF** | GOVERN Function: Redress process governance |
| **ISO 42001** | Clause 7.3 (Competence and Awareness): Complainant process awareness |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |
| **Security Scheme** | `x-tml-security: "CA-VettedJWT + IPAllowlist"` |
| **Idempotency Requirement** | `Idempotency-Key` header mandatory |
| **x-tml-monograph-ref** | `"Section 3.5.3"` |
| **x-tml-implementation-status** | `"SHIPPING"` |

*Table 19: POST /redress/challenge Compliance Mapping*

The endpoint's `challenge_basis` field uses canonical identifiers (`FACTUAL_ERROR`, `PROCEDURAL_VIOLATION`, `RIGHTS_INFRINGEMENT`, `LICENSE_BREACH`, `BIAS_ALLEGATION`, `OTHER`) to ensure **cross-deployment consistency** and automated routing to appropriate review pools .

#### 2.7.2 POST /redress/log-re-evaluation

The `POST /redress/log-re-evaluation` endpoint triggers **formal re-analysis** of specific Moral Trace Logs by independent reviewers.

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `POST /redress/log-re-evaluation` |
| **Monograph Section** | Section 3.4 (Pillar IV: Moral Trace Logs); Section 3.5 (Pillar V: Human Rights Mandate) |
| **TML Pillar** | `MoralTraceLogs` (Pillar IV) — primary; `HumanRightsMandate` (Pillar V) |
| **EU AI Act** | Article 12 (Record-Keeping): Log integrity during re-evaluation; Article 14 (Human Oversight): Reconsideration rights |
| **NIST AI RMF** | MANAGE Function: Corrective risk treatment |
| **ISO 42001** | Clause 10 (Improvement): Feedback from re-evaluation into system enhancement |
| **FRE 902** | Business Records Exception |
| **Implementation Status** | **BETA** |
| **Security Scheme** | `x-tml-security: "CA-VettedJWT + IPAllowlist"` |
| **Idempotency Requirement** | `Idempotency-Key` header mandatory |
| **x-tml-monograph-ref** | `"Section 3.4.4"` |
| **x-tml-implementation-status** | `"BETA"` |

*Table 20: POST /redress/log-re-evaluation Compliance Mapping*

The **BETA** classification reflects **model checkpoint versioning complexity**: full context reconstruction requires 15-minute granularity checkpoints, representing approximately **40% additional storage overhead** . The mitigation is **"context summary anchoring"**: key parameters embedded in the MTL itself reduce reconstruction dependency but may omit subtle environmental factors .

#### 2.7.3 POST /redress/grievance

The `POST /redress/grievance` endpoint enables **formal human rights grievance filing** under UDHR/Geneva vector enforcement.

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `POST /redress/grievance` |
| **Monograph Section** | Section 3.5 (Pillar V: Human Rights Mandate); Section 1.4 (Regulatory Harmony) |
| **TML Pillar** | `HumanRightsMandate` (Pillar V) |
| **EU AI Act** | Article 14 (Human Oversight): Individual rights to human oversight |
| **NIST AI RMF** | GOVERN Function: Institutional governance; MANAGE Function: Impact management |
| **ISO 42001** | Clause 5.3 (Roles and Responsibilities): Not directly referenced in monograph |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |
| **Security Scheme** | `x-tml-security: "CA-VettedJWT + IPAllowlist"` with enhanced `x-tml-human-rights-verification` |
| **Idempotency Requirement** | `Idempotency-Key` header mandatory |
| **x-tml-monograph-ref** | `"Section 3.5.3"` |
| **x-tml-implementation-status** | `"SHIPPING"` |

*Table 21: POST /redress/grievance Compliance Mapping*

The `affected_rights` field uses **canonical UDHR Article identifiers** (e.g., `UDHR-8`, `UDHR-25-1`) to enable automated routing to specialized review panels and regulatory notification workflows . The `urgency_classification` field (`ROUTINE`, `EXPEDITED`, `EMERGENCY`) drives response deadlines: **72 hours for EMERGENCY**, **14 days for EXPEDITED**, **90 days for ROUTINE** .

### 2.8 Regulator Inspection Endpoints

#### 2.8.1 GET /regulator/evidence-export

The `GET /regulator/evidence-export` endpoint enables **bulk export of evidentiary materials** for regulatory inspection.

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `GET /regulator/evidence-export` |
| **Monograph Section** | Section 3.4 (Pillar IV: Moral Trace Logs); Section 12 (FRE Alignment) |
| **TML Pillar** | `MoralTraceLogs` (Pillar IV) — primary; `PublicBlockchains` (Pillar VIII); `HybridShield` (Pillar VII) |
| **EU AI Act** | Article 61 (Conformity Assessment): Technical documentation for assessment bodies; Article 12 (Record-Keeping); Article 77 (Access to Documentation) |
| **NIST AI RMF** | GOVERN Function: Regulatory cooperation |
| **ISO 42001** | Clause 9.2 (Internal Audit); Clause 9.3 (Management Review): External audit facilitation |
| **FRE 902** | Business Records Exception; Self-Authenticating Evidence |
| **Implementation Status** | **BETA** |
| **Security Scheme** | `x-tml-security: "CA-VettedJWT + IPAllowlist"` |
| **Idempotency Requirement** | Not applicable (GET method) |
| **x-tml-monograph-ref** | `"Section 3.4.3"` |
| **x-tml-implementation-status** | `"BETA"` |

*Table 22: GET /regulator/evidence-export Compliance Mapping*

The **BETA** classification reflects **data volume and sensitivity considerations**: bulk export with cryptographic integrity verification requires streaming infrastructure with **chunked export** (10,000-log chunks with independent Merkle roots) to balance integrity with throughput . The `export_format` field supports `TSLF_NATIVE`, `JSON_LD`, `PDF_A_3`, and `FRE_902_PACKET` — the latter directly operationalizing FRE alignment for self-authenticating evidence packages .

#### 2.8.2 GET /regulator/custodian-quorum

The `GET /regulator/custodian-quorum` endpoint provides **cross-jurisdiction visibility** into distributed custodian consensus status.

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `GET /regulator/custodian-quorum` |
| **Monograph Section** | Section 3.7 (Pillar VII: Hybrid Shield); Section 7 (EU AI Act Alignment) |
| **TML Pillar** | `HybridShield` (Pillar VII) |
| **EU AI Act** | Article 61 (Conformity Assessment): Distributed system verification; Article 15 (Robustness): Resilience verification |
| **NIST AI RMF** | GOVERN Function: Distributed governance accountability |
| **ISO 42001** | Clause 4.2 (Understanding Needs of Interested Parties): Not directly referenced in monograph |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **FUTURE** (real-time cross-jurisdiction); **BETA** (jurisdiction-local with eventual consistency) |
| **x-tml-blocking-constraint** | "Section 10.4: Cross-jurisdiction custodian quorum in <500ms blocked by network latency and legal coordination barriers" |
| **Security Scheme** | `x-tml-security: "CA-VettedJWT + IPAllowlist"` |
| **Idempotency Requirement** | Not applicable (GET method) |
| **x-tml-monograph-ref** | `"Section 3.7.2"` |
| **x-tml-implementation-status** | `"FUTURE"` |

*Table 23: GET /regulator/custodian-quorum Compliance Mapping*

The **FUTURE** classification with explicit blocking constraint reflects the **fundamental unbuildability** of real-time cross-jurisdiction Byzantine consensus at global AI scale. The mitigation is **"federated quorum"**: each jurisdiction maintains a local 6-custodian quorum, with cross-jurisdiction hash synchronization every **5 minutes** rather than real-time consensus .

#### 2.8.3 GET /regulator/timestamp-verification

The `GET /regulator/timestamp-verification` endpoint verifies **qualified timestamps** for evidentiary admissibility.

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `GET /regulator/timestamp-verification` |
| **Monograph Section** | Section 3.8 (Pillar VIII: Public Blockchains); Section 12 (FRE Alignment) |
| **TML Pillar** | `PublicBlockchains` (Pillar VIII) — primary; `AlwaysMemory` (Pillar II) — temporal persistence |
| **EU AI Act** | Article 12 (Record-Keeping): Temporal integrity of records |
| **NIST AI RMF** | MEASURE Function: Temporal metrics and verification |
| **ISO 42001** | Clause 8.2 (Operation Planning and Control): Not directly referenced in monograph |
| **FRE 902** | Self-Authenticating Evidence (timestamp authentication) |
| **Implementation Status** | **BETA** |
| **Security Scheme** | `x-tml-security: "CA-VettedJWT + IPAllowlist"` |
| **Idempotency Requirement** | Not applicable (GET method) |
| **x-tml-monograph-ref** | `"Section 3.8.3"` |
| **x-tml-implementation-status** | `"BETA"` |

*Table 24: GET /regulator/timestamp-verification Compliance Mapping*

The **BETA** classification reflects **eIDAS-qualified trust service provider integration costs**, which vary by EU member state and require ongoing contractual relationships .

### 2.9 Gateway Endpoints

#### 2.9.1 POST /gateway/route

The `POST /gateway/route` endpoint implements **TML Gateway Logic** that assigns incoming decision vectors to appropriate lanes.

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `POST /gateway/route` |
| **Monograph Section** | Section 2.2 (Dual-Lane Latency Architecture); Section 2.4 (Eight Pillars of Enforcement) |
| **TML Pillar** | `HybridShield` (Pillar VII) — primary; `SacredZero` (Pillar I) — fail-closed behavior |
| **EU AI Act** | Article 9 (Risk Management): Risk-based routing; Article 15 (Robustness): Fail-closed design |
| **NIST AI RMF** | MANAGE Function: Resource allocation to risks |
| **ISO 42001** | Clause 8.3 (Risk Assessment and Treatment): Routing risk treatment |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** (basic); **BETA** (adaptive routing) |
| **Security Scheme** | `x-tml-security: "mTLS + ServiceAccountJWT"` |
| **Idempotency Requirement** | `Idempotency-Key` header mandatory |
| **x-tml-monograph-ref** | `"Section 2.2.4"` |
| **x-tml-implementation-status** | `"SHIPPING"` |

*Table 25: POST /gateway/route Compliance Mapping*

#### 2.9.2 GET /gateway/status

The `GET /gateway/status` endpoint provides visibility into **TML Gateway operational state**.

| Attribute | Value |
|-----------|-------|
| **OpenAPI Path** | `GET /gateway/status` |
| **Monograph Section** | Section 2.2 (Dual-Lane Latency Architecture) |
| **TML Pillar** | `HybridShield` (Pillar VII) |
| **EU AI Act** | Article 9 (Risk Management): Operational monitoring; Article 15 (Robustness): System integrity verification |
| **NIST AI RMF** | MEASURE Function: Operational effectiveness metrics |
| **ISO 42001** | Clause 10 (Improvement): Gateway performance feedback |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |
| **Security Scheme** | `x-tml-security: "mTLS + ServiceAccountJWT"` |
| **Idempotency Requirement** | Not applicable (GET method) |
| **x-tml-monograph-ref** | `"Section 2.2.4"` |
| **x-tml-implementation-status** | `"SHIPPING"` |

*Table 26: GET /gateway/status Compliance Mapping*

### 2.10 Webhook and Callback Definitions

#### 2.10.1 sacredPause.escalation

The `sacredPause.escalation` webhook delivers **asynchronous notifications** when State 0 triggers human review.

| Attribute | Value |
|-----------|-------|
| **Webhook Name** | `sacredPause.escalation` |
| **Monograph Section** | Section 2.3.3 (State 0: Sacred Zero); Section 3.1.2 (Sacred Pause Operational Workflow) |
| **TML Pillar** | `SacredZero` (Pillar I) |
| **EU AI Act** | Article 14 (Human Oversight): Immediate notification reduces oversight latency |
| **NIST AI RMF** | MANAGE Function: Incident notification workflow |
| **ISO 42001** | Clause 7.3 (Competence and Awareness): Reviewer availability notification |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **BETA** |
| **Security Scheme** | `x-tml-security: "HSM-SignedJWT + MutualTLS"` (payload signing) |
| **Retry Semantics** | Exponential backoff with jitter, dead-letter queue, `x-tml-idempotency` headers |
| **x-tml-monograph-ref** | `"Section 2.3.3"` |
| **x-tml-implementation-status** | `"BETA"` |

*Table 27: sacredPause.escalation Webhook Compliance Mapping*

The **BETA** classification reflects **reliability engineering complexity**: guaranteed delivery requires retry semantics, dead letter handling, and idempotency guarantees that introduce operational overhead beyond basic HTTP notification .

#### 2.10.2 lanternStatus.broadcast

The `lanternStatus.broadcast` webhook delivers **public beacon signal updates** to subscribed observers.

| Attribute | Value |
|-----------|-------|
| **Webhook Name** | `lanternStatus.broadcast` |
| **Monograph Section** | Section 3.3 (Pillar III: Goukassian Promise); Section 3.1 (Pillar I: Sacred Zero) |
| **TML Pillar** | `GoukassianPromise` (Pillar III) |
| **EU AI Act** | Article 13 (Transparency): Real-time transparency without polling; Article 14 (Human Oversight): Public oversight status |
| **NIST AI RMF** | GOVERN Function: Transparency and accountability provisions |
| **ISO 42001** | Clause 7.3 (Competence and Awareness): Public stakeholder awareness |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |
| **Security Scheme** | `x-tml-security: "HSM-SignedJWT + MutualTLS"` (payload signing); public verification key availability |
| **Retry Semantics** | Best-effort broadcast with at-least-once delivery, `x-tml-idempotency` headers |
| **x-tml-monograph-ref** | `"Section 3.3.1"` |
| **x-tml-implementation-status** | `"SHIPPING"` |

*Table 28: lanternStatus.broadcast Webhook Compliance Mapping*

## 3. JSON Schema Property Compliance Mappings

### 3.1 State Envelope Schema Properties

#### 3.1.1 current_state

The `current_state` property represents the **triadic logic state** as a signed integer: **+1 (Proceed), 0 (Sacred Zero), or -1 (Refuse)**. This property maps to **Pillar I: SacredZero** (`SacredZero`) as the foundational state representation, though its values span all three triadic states .

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `current_state` |
| **Parent Schema** | `StateEnvelope` |
| **Monograph Section** | Section 2.3 (Triadic Logic Core) |
| **TML Pillar** | `SacredZero` (Pillar I) |
| **Data Type** | Signed integer: `+1`, `0`, `-1` |
| **Validation** | Enum constraint; null explicitly excluded |
| **EU AI Act** | Article 14 (Human Oversight): Interpretable states enable effective oversight |
| **NIST AI RMF** | MEASURE Function: State distribution metrics |
| **ISO 42001** | Clause 8.3 (Risk Assessment): Discrete risk classification |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |

*Table 29: current_state Property Compliance Mapping*

The **Quality Gate 4** explicitly verifies that **"The Sacred Zero (State 0) is never represented as `null`, `error`, `false`, or `timeout`. It is a first-class state"** . The `current_state` property enforces this by requiring **integer type with enum constraint `[1, 0, -1]`**, explicitly excluding null or boolean alternatives. The `state_label` companion property provides human-readable canonical strings (`"PROCEED"`, `"SACRED_ZERO"`, `"REFUSE"`) for interpretability .

#### 3.1.2 state_label

The `state_label` property provides **human-readable state identification** using canonical strings.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `state_label` |
| **Parent Schema** | `StateEnvelope` |
| **Monograph Section** | Section 2.3 (Triadic Logic Core); Section 3.1 (Pillar I: Sacred Zero) |
| **TML Pillar** | `SacredZero` (Pillar I) |
| **Data Type** | String enum: `"PROCEED"`, `"SACRED_ZERO"`, `"REFUSE"` |
| **Validation** | UPPER_SNAKE_CASE; exact canonical terms enforced |
| **EU AI Act** | Article 14 (4)(b): Comprehension — "understand capabilities and limitations, interpret output"  |
| **NIST AI RMF** | GOVERN Function: Interpretable governance |
| **ISO 42001** | Clause 7.3 (Competence): Reduced interpretation errors |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |

*Table 30: state_label Property Compliance Mapping*

The **terminology enforcement** is absolute: the prompt mandates that "If the monograph calls it 'Sacred Zero,' the API spec must call it `SacredZero`, not `PauseState`, `HOLD`, or `Timeout`" — and the `state_label` enum values implement this by restricting to **canonical identifiers only** .

#### 3.1.3 proposed_action

The `proposed_action` property contains the **action descriptor** that the binary inference engine proposes for ternary governance evaluation.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `proposed_action` |
| **Parent Schema** | `StateEnvelope` |
| **Monograph Section** | Section 2.2 (Dual-Lane Latency Architecture) |
| **TML Pillar** | `AlwaysMemory` (Pillar II) — pre-actuation commit |
| **Data Type** | Object (action-specific schema) |
| **Validation** | Required; structure varies by action type |
| **EU AI Act** | Article 12 (Record-Keeping): Documentation of intended outputs |
| **NIST AI RMF** | MAP Function: Risk contextualization |
| **ISO 42001** | Clause 8.3 (Risk Assessment): Action context for risk evaluation |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |

*Table 31: proposed_action Property Compliance Mapping*

#### 3.1.4 permission_token

The `permission_token` property is the **schema-level enforcement mechanism** for the **"No Log = No Action" principle**. This property is **conditionally required when `current_state` equals `+1`**, and its absence renders the State Envelope **invalid by schema constraint** .

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `permission_token` |
| **Parent Schema** | `StateEnvelope` |
| **Monograph Section** | Section 2.2.3 (No Log = No Action Interlock); Section 3.2 (Pillar II: Always Memory) |
| **TML Pillar** | `AlwaysMemory` (Pillar II) — primary; `GoukassianPromise` (Pillar III) — License artifact; `HybridShield` (Pillar VII) — cryptographic verification; `PublicBlockchains` (Pillar VIII) — Merkle anchoring |
| **Data Type** | `PermissionToken` object (standalone schema) |
| **Validation** | Conditionally required: `if current_state == "+1"` then `permission_token` is mandatory; schema rejects +1 without valid token |
| **EU AI Act** | Article 12 (Record-Keeping): Automatic recording enforcement; Article 14 (Human Oversight): Governance validation before execution; Article 15 (Robustness): Cryptographic integrity prevents tampering |
| **NIST AI RMF** | GOVERN, MAP, MEASURE, MANAGE — all four functions implicated |
| **ISO 42001** | Clause 7.3 (Traceability): Verifiable decision paths; Clause 8.3 (Risk Treatment): Pre-execution risk verification |
| **FRE 902** | Self-Authenticating Evidence (cryptographic signature and timestamp) |
| **Implementation Status** | **BETA** (HSM signing latency tradeoffs) |

*Table 32: permission_token Property Compliance Mapping*

The **Permission Token schema** (dedicated subsection B.i) requires four mandatory fields: `log_hash` (SHA-256 of anchored Moral Trace Log), `epoch_timestamp` (qualified timestamp), `signer_key_id` (HSM key identifier), and `lane_origin` (enum `"INFERENCE"` or `"ANCHORING"`) . The token must be **cryptographically signed by the Anchoring Lane and verifiable against the Merkle root**, creating the non-repudiation binding that prevents any +1 state transition without prior log anchoring .

### 3.2 TSLF-State0 (Sacred Pause Log) Properties

#### 3.2.1 lantern_status

The `lantern_status` property encodes the **public compliance beacon state** at Sacred Zero activation.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `lantern_status` |
| **Parent Schema** | `TSLF-State0` |
| **Monograph Section** | Section 3.3 (Pillar III: Goukassian Promise); Section 3.1 (Pillar I: Sacred Zero) |
| **TML Pillar** | `GoukassianPromise` (Pillar III) — primary; `SacredZero` (Pillar I) |
| **Data Type** | `LanternStatus` object (standalone schema) |
| **Validation** | Required |
| **EU AI Act** | Article 13 (Transparency): Public governance status; Article 14 (Human Oversight): External oversight visibility |
| **NIST AI RMF** | GOVERN Function: Demonstrable compliance |
| **ISO 42001** | Clause 7.3 (Awareness): Organizational awareness of governance status |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |

*Table 33: lantern_status Property Compliance Mapping*

#### 3.2.2 uncertainty_quantification

The `uncertainty_quantification` property provides the **mathematical and evidentiary basis** for Sacred Zero activation.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `uncertainty_quantification` |
| **Parent Schema** | `TSLF-State0` |
| **Monograph Section** | Section 2.3.3 (State 0: Sacred Zero); Section 3.1.2 (Sacred Pause Operational Workflow) |
| **TML Pillar** | `SacredZero` (Pillar I) |
| **Data Type** | Object (structured uncertainty metrics) |
| **Validation** | Required |
| **EU AI Act** | Article 9 (Risk Management): Explicit uncertainty documentation |
| **NIST AI RMF** | MAP Function: Risk contextualization through uncertainty |
| **ISO 42001** | Clause 8.3 (Risk Assessment): Uncertainty as risk factor |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **BETA** (methodological tradeoffs in moral uncertainty quantification) |

*Table 34: uncertainty_quantification Property Compliance Mapping*

#### 3.2.3 deliberation_matrix

The `deliberation_matrix` property contains the **structured record of governance evaluation** across all applicable TML pillars.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `deliberation_matrix` |
| **Parent Schema** | `TSLF-State0` |
| **Monograph Section** | Section 3.4 (Pillar IV: Moral Trace Logs); Section 2.4 (Eight Pillars of Enforcement) |
| **TML Pillar** | All Eight Pillars (composite) |
| **Data Type** | Array of pillar-specific evaluation objects |
| **Validation** | Required; minimum one entry per active pillar |
| **EU AI Act** | Article 12 (Record-Keeping): Comprehensive reasoning documentation |
| **NIST AI RMF** | MAP Function: Multi-dimensional risk contextualization |
| **ISO 42001** | Clause 8.3 (Risk Assessment): Structured risk evaluation |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **BETA** (pillar evaluation complexity) |

*Table 35: deliberation_matrix Property Compliance Mapping*

#### 3.2.4 resolution_request

The `resolution_request` property encodes the **specific information or action** that would enable resolution of Sacred Zero state.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `resolution_request` |
| **Parent Schema** | `TSLF-State0` |
| **Monograph Section** | Section 3.1.2 (Sacred Pause Operational Workflow); Section 3.1.4 (Operational Consequences) |
| **TML Pillar** | `SacredZero` (Pillar I) |
| **Data Type** | Object (structured request parameters) |
| **Validation** | Required |
| **EU AI Act** | Article 14 (Human Oversight): Explicit request for meaningful intervention |
| **NIST AI RMF** | MANAGE Function: Structured incident response request |
| **ISO 42001** | Clause 8.3 (Risk Treatment): Request for risk resolution |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |

*Table 36: resolution_request Property Compliance Mapping*

### 3.3 TSLF-State-1 (Refusal Log) Properties

#### 3.3.1 license_violation

The `license_violation` property documents how the proposed action **exceeded Goukassian Promise License boundaries**.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `license_violation` |
| **Parent Schema** | `TSLF-State-1` |
| **Monograph Section** | Section 3.3 (Pillar III: Goukassian Promise); Section 3.3.3 (License: Operational Contract) |
| **TML Pillar** | `GoukassianPromise` (Pillar III) |
| **Data Type** | Object (violation details) |
| **Validation** | Required |
| **EU AI Act** | Article 5 (Prohibited Practices): License violations as prohibited activity prevention; Article 10 (Data Governance): Scope limitation |
| **NIST AI RMF** | GOVERN Function: Policy enforcement documentation |
| **ISO 42001** | Clause 6.1.2 (AI Risk Assessment): Not directly referenced in monograph |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |

*Table 37: license_violation Property Compliance Mapping*

#### 3.3.2 threat_vector_analysis

The `threat_vector_analysis` property documents the **specific harm pathways** that triggered Refuse determination.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `threat_vector_analysis` |
| **Parent Schema** | `TSLF-State-1` |
| **Monograph Section** | Section 2.3.2 (State -1: Refuse); Section 3.5 (Pillar V: Human Rights Mandate); Section 3.6 (Pillar VI: Earth Protection Mandate) |
| **TML Pillar** | `HumanRightsMandate` (Pillar V) / `EarthProtectionMandate` (Pillar VI) — trigger-specific |
| **Data Type** | Object (structured threat assessment) |
| **Validation** | Required |
| **EU AI Act** | Article 15 (Robustness): Pre-emptive defense documentation; Article 9 (Risk Management): Threat identification |
| **NIST AI RMF** | MAP Function: Threat contextualization; MANAGE Function: Protective action documentation |
| **ISO 42001** | Clause 8.3 (Risk Treatment): Threat-based risk treatment |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **BETA** (automated threat analysis for moral reasoning) |

*Table 38: threat_vector_analysis Property Compliance Mapping*

#### 3.3.3 chain_of_custody

The `chain_of_custody` property preserves **complete provenance record** of the refusal decision.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `chain_of_custody` |
| **Parent Schema** | `TSLF-State-1` |
| **Monograph Section** | Section 3.2 (Pillar II: Always Memory); Section 3.4 (Pillar IV: Moral Trace Logs) |
| **TML Pillar** | `AlwaysMemory` (Pillar II) — primary; `MoralTraceLogs` (Pillar IV) |
| **Data Type** | Array of custody events with timestamps and signatures |
| **Validation** | Required; minimum one entry |
| **EU AI Act** | Article 12 (Record-Keeping): Provenance documentation |
| **NIST AI RMF** | GOVERN Function: Accountability chain |
| **ISO 42001** | Clause 7.3 (Traceability): Decision provenance |
| **FRE 902** | Self-Authenticating Evidence (cryptographic custody chain) |
| **Implementation Status** | **SHIPPING** |

*Table 39: chain_of_custody Property Compliance Mapping*

### 3.4 TSLF-State+1 (Proceed Log) Properties

#### 3.4.1 ethical_verification

The `ethical_verification` property documents the **comprehensive ethical evaluation** that enabled Proceed determination.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `ethical_verification` |
| **Parent Schema** | `TSLF-State+1` |
| **Monograph Section** | Section 3.4 (Pillar IV: Moral Trace Logs); Section 2.3.1 (State +1: Proceed) |
| **TML Pillar** | All Eight Pillars (composite evaluation) |
| **Data Type** | Object (structured ethical assessment) |
| **Validation** | Required |
| **EU AI Act** | Article 12 (Record-Keeping): Comprehensive internal reasoning documentation |
| **NIST AI RMF** | MEASURE Function: Ethical evaluation metrics |
| **ISO 42001** | Clause 8.3 (Risk Assessment): Ethical risk evaluation |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **BETA** (ethical evaluation standardization) |

*Table 40: ethical_verification Property Compliance Mapping*

#### 3.4.2 the_signature

The `the_signature` property contains the **non-repudiation artifact** constituting the "Signature" element of the Goukassian Promise.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `the_signature` |
| **Parent Schema** | `TSLF-State+1` |
| **Monograph Section** | Section 3.3 (Pillar III: Goukassian Promise); Section 3.3.2 (Signature: Provenance and Non-Repudiation) |
| **TML Pillar** | `GoukassianPromise` (Pillar III) |
| **Data Type** | `SignatureBlock` object (standalone schema) |
| **Validation** | Required |
| **EU AI Act** | Article 12 (Record-Keeping): Cryptographic integrity of records; Article 15 (Robustness): Tamper evidence |
| **NIST AI RMF** | GOVERN Function: Accountability attribution |
| **ISO 42001** | Clause 8.2 (Information Security): Cryptographic protection |
| **FRE 902** | Self-Authenticating Evidence (FRE 902(13) — certified records generated by electronic process) |
| **Implementation Status** | **SHIPPING** |

*Table 41: the_signature Property Compliance Mapping*

The `the_signature` property name uses the **definite article** to distinguish it as the canonical Signature artifact of the Goukassian Promise, not merely any cryptographic signature. This naming convention enforces the **Quality Gate 9** requirement that "The Goukassian Promise artifacts are explicitly modeled by their canonical string names (`lantern`, `signature`, `license`) in all machine-readable schemas" .

#### 3.4.3 audit_proof

The `audit_proof` property provides **cryptographic evidence** of Anchoring Lane validation for the Proceed decision.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `audit_proof` |
| **Parent Schema** | `TSLF-State+1` |
| **Monograph Section** | Section 3.4 (Pillar IV: Moral Trace Logs); Section 3.8 (Pillar VIII: Public Blockchains) |
| **TML Pillar** | `MoralTraceLogs` (Pillar IV) — primary; `PublicBlockchains` (Pillar VIII) |
| **Data Type** | Object (Merkle inclusion proof and custodian attestations) |
| **Validation** | Required |
| **EU AI Act** | Article 61 (Conformity Assessment): Technical evidence for assessment |
| **NIST AI RMF** | MEASURE Function: Audit trail verification |
| **ISO 42001** | Clause 9.2 (Internal Audit): Evidence for audit |
| **FRE 902** | Self-Authenticating Evidence (Merkle proof structure) |
| **Implementation Status** | **SHIPPING** |

*Table 42: audit_proof Property Compliance Mapping*

### 3.5 Justification Object Properties

#### 3.5.1 justification_id

The `justification_id` property provides **unique identifier** for the Justification Object that travels between Inference and Anchoring lanes.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `justification_id` |
| **Parent Schema** | `JustificationObject` |
| **Monograph Section** | Section 2.2 (Dual-Lane Latency Architecture); Section 2.2.3 (No Log = No Action Interlock) |
| **TML Pillar** | `AlwaysMemory` (Pillar II) |
| **Data Type** | UUID v4 |
| **Validation** | Required; unique across system |
| **EU AI Act** | Article 12 (Record-Keeping): Unique identification for traceability |
| **NIST AI RMF** | GOVERN Function: Accountability tracking |
| **ISO 42001** | Clause 7.3 (Traceability): Unique decision identification |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |

*Table 43: justification_id Property Compliance Mapping*

#### 3.5.2 inference_lane_id

The `inference_lane_id` property identifies the **specific Inference Lane instance** that generated the proposal.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `inference_lane_id` |
| **Parent Schema** | `JustificationObject` |
| **Monograph Section** | Section 2.2.1 (Lane 1: Inference Lane) |
| **TML Pillar** | `SacredZero` (Pillar I) |
| **Data Type** | String (lane instance identifier) |
| **Validation** | Required |
| **EU AI Act** | Article 12 (Record-Keeping): Lane attribution for accountability |
| **NIST AI RMF** | MEASURE Function: Lane performance tracking |
| **ISO 42001** | Clause 8.3 (Risk Assessment): Lane-specific risk evaluation |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |

*Table 44: inference_lane_id Property Compliance Mapping*

#### 3.5.3 anchoring_lane_id

The `anchoring_lane_id` property identifies the **specific Anchoring Lane instance** that validated the proposal.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `anchoring_lane_id` |
| **Parent Schema** | `JustificationObject` |
| **Monograph Section** | Section 2.2.2 (Lane 2: Anchoring Lane) |
| **TML Pillar** | `MoralTraceLogs` (Pillar IV) |
| **Data Type** | String (lane instance identifier) |
| **Validation** | Required |
| **EU AI Act** | Article 12 (Record-Keeping): Lane attribution for accountability |
| **NIST AI RMF** | MEASURE Function: Lane performance tracking |
| **ISO 42001** | Clause 8.3 (Risk Assessment): Lane-specific risk evaluation |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |

*Table 45: anchoring_lane_id Property Compliance Mapping*

#### 3.5.4 justification_data

The `justification_data` property contains the **structured payload** that carries decision context between lanes.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `justification_data` |
| **Parent Schema** | `JustificationObject` |
| **Monograph Section** | Section 2.2.3 (No Log = No Action Interlock); Section 3.4 (Pillar IV: Moral Trace Logs) |
| **TML Pillar** | `MoralTraceLogs` (Pillar IV) |
| **Data Type** | Object (context-specific schema) |
| **Validation** | Required; `unevaluatedProperties: false` |
| **EU AI Act** | Article 12 (Record-Keeping): Complete decision context |
| **NIST AI RMF** | MAP Function: Risk contextualization data |
| **ISO 42001** | Clause 8.3 (Risk Assessment): Context for risk evaluation |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |

*Table 46: justification_data Property Compliance Mapping*

### 3.6 Lantern Status Properties

#### 3.6.1 lantern_id

The `lantern_id` property provides **unique identification** for the Lantern beacon instance.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `lantern_id` |
| **Parent Schema** | `LanternStatus` |
| **Monograph Section** | Section 3.3 (Pillar III: Goukassian Promise); Section 3.3.1 (Lantern: Public Transparency Beacon) |
| **TML Pillar** | `GoukassianPromise` (Pillar III) |
| **Data Type** | UUID v4 |
| **Validation** | Required; unique across system |
| **EU AI Act** | Article 13 (Transparency): Beacon identification for accountability |
| **NIST AI RMF** | GOVERN Function: Transparency infrastructure tracking |
| **ISO 42001** | Clause 7.3 (Awareness): Beacon awareness |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |

*Table 47: lantern_id Property Compliance Mapping*

#### 3.6.2 compliance_beacon

The `compliance_beacon` property encodes the **current compliance state signal** broadcast by the Lantern.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `compliance_beacon` |
| **Parent Schema** | `LanternStatus` |
| **Monograph Section** | Section 3.3.1 (Lantern: Public Transparency Beacon) |
| **TML Pillar** | `GoukassianPromise` (Pillar III) |
| **Data Type** | Enum: `"GOVERNANCE_ACTIVE"`, `"ALL_CLEAR"`, `"DEGRADED_OPERATIONS"`, `"EMERGENCY_PAUSE"`, `"MAINTENANCE"` |
| **Validation** | Required; UPPER_SNAKE_CASE |
| **EU AI Act** | Article 13 (Transparency): Real-time compliance status; Article 14 (Human Oversight): External oversight visibility |
| **NIST AI RMF** | GOVERN Function: Demonstrable compliance signal |
| **ISO 42001** | Clause 7.3 (Awareness): Organizational compliance awareness |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |

*Table 48: compliance_beacon Property Compliance Mapping*

#### 3.6.3 last_updated

The `last_updated` property records the **qualified timestamp** of the most recent Lantern status change.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `last_updated` |
| **Parent Schema** | `LanternStatus` |
| **Monograph Section** | Section 3.3.1 (Lantern: Public Transparency Beacon); Section 3.8 (Pillar VIII: Public Blockchains) |
| **TML Pillar** | `GoukassianPromise` (Pillar III); `PublicBlockchains` (Pillar VIII) |
| **Data Type** | ISO 8601 timestamp with timezone |
| **Validation** | Required; qualified timestamp from certified time source |
| **EU AI Act** | Article 12 (Record-Keeping): Temporal integrity of transparency records |
| **NIST AI RMF** | MEASURE Function: Temporal metrics |
| **ISO 42001** | Clause 8.2 (Information Security): Timestamp integrity |
| **FRE 902** | Self-Authenticating Evidence (qualified timestamp) |
| **Implementation Status** | **SHIPPING** |

*Table 49: last_updated Property Compliance Mapping*

### 3.7 Signature Block Properties

#### 3.7.1 signer_id

The `signer_id` property identifies the **cryptographic entity** that generated the signature.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `signer_id` |
| **Parent Schema** | `SignatureBlock` |
| **Monograph Section** | Section 3.3.2 (Signature: Provenance and Non-Repudiation); Section 3.7 (Pillar VII: Hybrid Shield) |
| **TML Pillar** | `GoukassianPromise` (Pillar III); `HybridShield` (Pillar VII) |
| **Data Type** | String (custodian or HSM key identifier) |
| **Validation** | Required; must resolve to known signer registry |
| **EU AI Act** | Article 12 (Record-Keeping): Signature attribution for accountability |
| **NIST AI RMF** | GOVERN Function: Accountability attribution |
| **ISO 42001** | Clause 7.3 (Competence): Signer qualification verification |
| **FRE 902** | Self-Authenticating Evidence (signer identification) |
| **Implementation Status** | **SHIPPING** |

*Table 50: signer_id Property Compliance Mapping*

#### 3.7.2 signature_value

The `signature_value` property contains the **cryptographic signature** itself.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `signature_value` |
| **Parent Schema** | `SignatureBlock` |
| **Monograph Section** | Section 3.3.2 (Signature: Provenance and Non-Repudiation) |
| **TML Pillar** | `GoukassianPromise` (Pillar III) |
| **Data Type** | Base64-encoded ECDSA or EdDSA signature |
| **Validation** | Required; format verified against signer algorithm |
| **EU AI Act** | Article 15 (Robustness): Cryptographic integrity; Article 12 (Record-Keeping): Tamper evidence |
| **NIST AI RMF** | GOVERN Function: Non-repudiation enforcement |
| **ISO 42001** | Clause 8.2 (Information Security): Cryptographic protection |
| **FRE 902** | Self-Authenticating Evidence (FRE 902(13)) |
| **Implementation Status** | **SHIPPING** |

*Table 51: signature_value Property Compliance Mapping*

#### 3.7.3 signing_time

The `signing_time` property records the **qualified timestamp** of signature generation.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `signing_time` |
| **Parent Schema** | `SignatureBlock` |
| **Monograph Section** | Section 3.3.2 (Signature: Provenance and Non-Repudiation); Section 3.8 (Pillar VIII: Public Blockchains) |
| **TML Pillar** | `GoukassianPromise` (Pillar III); `PublicBlockchains` (Pillar VIII) |
| **Data Type** | ISO 8601 timestamp with timezone |
| **Validation** | Required; qualified timestamp; must not exceed current time by >1s |
| **EU AI Act** | Article 12 (Record-Keeping): Temporal integrity of signatures |
| **NIST AI RMF** | MEASURE Function: Temporal metrics |
| **ISO 42001** | Clause 8.2 (Information Security): Timestamp integrity |
| **FRE 902** | Self-Authenticating Evidence (qualified timestamp under FRE 902(13)) |
| **Implementation Status** | **SHIPPING** |

*Table 52: signing_time Property Compliance Mapping*

### 3.8 Permission Token Properties

#### 3.8.1 log_hash

The `log_hash` property contains the **SHA-256 hash** of the anchored Moral Trace Log, creating the cryptographic binding that enforces "No Log = No Action".

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `log_hash` |
| **Parent Schema** | `PermissionToken` |
| **Monograph Section** | Section 2.2.3 (No Log = No Action Interlock); Section 3.2 (Pillar II: Always Memory) |
| **TML Pillar** | `AlwaysMemory` (Pillar II) — primary; `MoralTraceLogs` (Pillar IV) |
| **Data Type** | Hex-encoded SHA-256 (64 characters) |
| **Validation** | Required; must match anchored MTL hash; immutable after issuance |
| **EU AI Act** | Article 12 (Record-Keeping): Cryptographic record integrity; Article 14 (Human Oversight): Verifiable governance linkage |
| **NIST AI RMF** | GOVERN Function: Non-repudiation; MANAGE Function: Execution authorization control |
| **ISO 42001** | Clause 7.3 (Traceability): Hash-based decision path verification |
| **FRE 902** | Self-Authenticating Evidence (hash-chain integrity) |
| **Implementation Status** | **SHIPPING** |

*Table 53: log_hash Property Compliance Mapping*

The `log_hash` is the **linchpin of the entire TML governance architecture**: without it, the Permission Token cannot be generated; without the Permission Token, no +1 state can execute. This **schema-level enforcement** prevents any circumvention of the "No Log = No Action" principle .

#### 3.8.2 epoch_timestamp

The `epoch_timestamp` property records the **qualified timestamp** of Permission Token issuance.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `epoch_timestamp` |
| **Parent Schema** | `PermissionToken` |
| **Monograph Section** | Section 3.8 (Pillar VIII: Public Blockchains); Section 3.2 (Pillar II: Always Memory) |
| **TML Pillar** | `PublicBlockchains` (Pillar VIII); `AlwaysMemory` (Pillar II) |
| **Data Type** | ISO 8601 timestamp with timezone |
| **Validation** | Required; qualified timestamp from Anchoring Lane time source |
| **EU AI Act** | Article 12 (Record-Keeping): Temporal integrity of authorization records |
| **NIST AI RMF** | MEASURE Function: Temporal governance metrics |
| **ISO 42001** | Clause 8.2 (Information Security): Timestamp integrity |
| **FRE 902** | Self-Authenticating Evidence (qualified timestamp) |
| **Implementation Status** | **SHIPPING** |

*Table 54: epoch_timestamp Property Compliance Mapping*

#### 3.8.3 signer_key_id

The `signer_key_id` property identifies the **HSM key** that signed the Permission Token.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `signer_key_id` |
| **Parent Schema** | `PermissionToken` |
| **Monograph Section** | Section 3.7 (Pillar VII: Hybrid Shield); Section 3.3.2 (Signature: Provenance and Non-Repudiation) |
| **TML Pillar** | `HybridShield` (Pillar VII); `GoukassianPromise` (Pillar III) |
| **Data Type** | String (HSM key identifier from certified key ceremony) |
| **Validation** | Required; must resolve to active key in HSM registry |
| **EU AI Act** | Article 15 (Robustness): Hardware-backed security; Article 12 (Record-Keeping): Signature attribution |
| **NIST AI RMF** | GOVERN Function: Key custody accountability |
| **ISO 42001** | Clause 8.2 (Information Security): HSM key management |
| **FRE 902** | Self-Authenticating Evidence (certified key provenance) |
| **Implementation Status** | **SHIPPING** |

*Table 55: signer_key_id Property Compliance Mapping*

#### 3.8.4 lane_origin

The `lane_origin` property identifies which **lane generated the Permission Token**, enabling audit of lane separation integrity.

| Attribute | Value |
|-----------|-------|
| **Schema Property** | `lane_origin` |
| **Parent Schema** | `PermissionToken` |
| **Monograph Section** | Section 2.2 (Dual-Lane Latency Architecture); Section 2.2.3 (No Log = No Action Interlock) |
| **TML Pillar** | `SacredZero` (Pillar I); `MoralTraceLogs` (Pillar IV) |
| **Data Type** | Enum: `"INFERENCE"`, `"ANCHORING"` (UPPER_SNAKE_CASE) |
| **Validation** | Required; must be `"ANCHORING"` for valid execution authorization |
| **EU AI Act** | Article 14 (Human Oversight): Lane separation verification; Article 12 (Record-Keeping): Lane attribution |
| **NIST AI RMF** | GOVERN Function: Lane accountability enforcement |
| **ISO 42001** | Clause 8.3 (Risk Assessment): Lane-specific risk evaluation |
| **FRE 902** | Not directly referenced in monograph |
| **Implementation Status** | **SHIPPING** |

*Table 56: lane_origin Property Compliance Mapping*

The `lane_origin` property enforces the **architectural separation** between Inference and Anchoring lanes: only tokens with `lane_origin: "ANCHORING"` authorize execution, preventing any Inference Lane bypass of governance validation .

## 4. TML Pillar Canonical Identifiers Reference

### 4.1 Pillar I: SacredZero

| Attribute | Value |
|-----------|-------|
| **Canonical Identifier** | `SacredZero` |
| **Monograph Section** | Section 3.1: Sacred Zero (The Epistemic Hold) |
| **Core Function** | Active governance state of mandatory hesitation; triggers Sacred Pause operational workflow |
| **State Value** | `0` |
| **State Label** | `SACRED_ZERO` |
| **Goukassian Vow** | "Pause when truth is uncertain" |
| **Latency Characteristic** | Variable: 2ms trigger to minutes resolution (human review dependent) |
| **Primary Endpoints** | `POST /inference/decisions` (state proposal), `POST /escalation/reviews` (workflow initiation), `POST /emergency/shutdown` (terminal state) |
| **Primary Schema Properties** | `current_state` (when value is 0), `state_label` (when value is "SACRED_ZERO"), `process_active` (when value is "SacredPause") |

*Table 57: Pillar I — SacredZero Reference*

### 4.2 Pillar II: AlwaysMemory

| Attribute | Value |
|-----------|-------|
| **Canonical Identifier** | `AlwaysMemory` |
| **Monograph Section** | Section 3.2: Always Memory (Anti-Spoliation / Pre-Actuation Commit) |
| **Core Function** | Immutable, cryptographically sealed memory before execution; 1:1 log-to-action ratio enforcement |
| **Technical Mechanism** | Pre-actuation commit; hash-chain integrity; anti-spoliation |
| **Primary Endpoints** | `POST /anchoring/logs` (log anchoring), `POST /inference/decisions` (pre-actuation logging) |
| **Primary Schema Properties** | `permission_token.log_hash` (SHA-256 binding), `justification_id` (unique decision identification), `chain_of_custody` (provenance preservation) |

*Table 58: Pillar II — AlwaysMemory Reference*

### 4.3 Pillar III: GoukassianPromise

| Attribute | Value |
|-----------|-------|
| **Canonical Identifier** | `GoukassianPromise` |
| **Monograph Section** | Section 3.3: Goukassian Promise (The Socio-Technical Covenant) |
| **Core Function** | Tripartite covenant: Lantern (transparency), Signature (provenance), License (operational contract) |
| **Artifacts** | `lantern` (public beacon), `signature` (non-repudiation), `license` (validation/authorization) |
| **Primary Endpoints** | `POST /lantern/broadcast` (Lantern), `POST /refusal/license-violation` (License enforcement), all endpoints with `SignatureBlock` (Signature) |
| **Primary Schema Properties** | `lantern_status` (Lantern artifact), `the_signature` (Signature artifact), `license_violation` (License artifact) |

*Table 59: Pillar III — GoukassianPromise Reference*

### 4.4 Pillar IV: MoralTraceLogs

| Attribute | Value |
|-----------|-------|
| **Canonical Identifier** | `MoralTraceLogs` |
| **Monograph Section** | Section 3.4: Moral Trace Logs (TSLF — Forensic Schema) |
| **Core Function** | Complete, immutable documentation of ethical reasoning; forensic reconstruction capability |
| **Schema Variants** | `TSLF-State0` (Sacred Pause), `TSLF-State-1` (Refusal), `TSLF-State+1` (Proceed) |
| **Primary Endpoints** | `POST /anchoring/logs` (log submission), all audit and regulator endpoints (log verification) |
| **Primary Schema Properties** | All TSLF variant properties; `justification_data`; `audit_proof` |

*Table 60: Pillar IV — MoralTraceLogs Reference*

### 4.5 Pillar V: HumanRightsMandate

| Attribute | Value |
|-----------|-------|
| **Canonical Identifier** | `HumanRightsMandate` |
| **Monograph Section** | Section 3.5: Human Rights Mandate (UDHR/Geneva Vector Enforcement) |
| **Core Function** | Real-time detection of human rights violations; procedural rights protection; victim remedy |
| **Legal Basis** | UDHR; ICCPR; Geneva Conventions |
| **Primary Endpoints** | `POST /escalation/reviews` (rights-sensitive routing), `POST /redress/challenge` (individual remedy), `POST /redress/grievance` (systemic remedy) |
| **Primary Schema Properties** | `threat_vector_analysis` (rights-based threats), `affected_rights` (UDHR Article identifiers), `challenge_basis` (rights infringement category) |

*Table 61: Pillar V — HumanRightsMandate Reference*

### 4.6 Pillar VI: EarthProtectionMandate

| Attribute | Value |
|-----------|-------|
| **Canonical Identifier** | `EarthProtectionMandate` |
| **Monograph Section** | Section 3.6: Earth Protection Mandate (Paris Agreement Vector Enforcement) |
| **Core Function** | Environmental harm detection; climate impact assessment; ecocide law preparation |
| **Legal Basis** | Paris Agreement; emerging ecocide law; ESG frameworks |
| **Primary Endpoints** | `POST /refusal/logging` (environmental harm refusal), `POST /escalation/reviews` (environmental sensitivity routing) |
| **Primary Schema Properties** | `threat_vector_analysis` (environmental threats) |

*Table 62: Pillar VI — EarthProtectionMandate Reference*

### 4.7 Pillar VII: HybridShield

| Attribute | Value |
|-----------|-------|
| **Canonical Identifier** | `HybridShield` |
| **Monograph Section** | Section 3.7: Hybrid Shield (6-Custodian Distributed Anchoring) |
| **Core Function** | Dual-layer defense: hash-chain integrity + multi-chain anchoring; Byzantine fault tolerance (f=2, n=6, quorum=4) |
| **Technical Mechanism** | 6 custodians; 4-of-6 quorum; Shamir Secret Sharing; distributed Merkle trees |
| **Primary Endpoints** | `POST /anchoring/logs` (custodian validation), `GET /audit/custodian-heartbeat` (liveness check), `GET /regulator/custodian-quorum` (cross-jurisdiction status) |
| **Primary Schema Properties** | `signer_key_id` (HSM key from certified ceremony), `audit_proof.custodian_attestations` (quorum verification) |

*Table 63: Pillar VII — HybridShield Reference*

### 4.8 Pillar VIII: PublicBlockchains

| Attribute | Value |
|-----------|-------|
| **Canonical Identifier** | `PublicBlockchains` |
| **Monograph Section** | Section 3.8: Public Blockchains (Merkle-Batched Anchoring) |
| **Core Function** | Immutable external anchoring; timestamp verification; third-party verifiability without full disclosure |
| **Technical Mechanism** | Merkle batching; Bitcoin/Ethereum/Polygon/OpenTimestamps anchoring; logarithmic inclusion proofs |
| **Primary Endpoints** | `POST /anchoring/logs` (batch anchoring), `GET /audit/merkle-root` (root verification), `GET /audit/log-inclusion-proof` (individual proof) |
| **Primary Schema Properties** | `epoch_timestamp` (anchored timestamp), `audit_proof.merkle_path` (inclusion verification) |

*Table 64: Pillar VIII — PublicBlockchains Reference*

## 5. Regulatory Nexus Cross-Reference

### 5.1 EU AI Act Alignment

#### 5.1.1 Article 9: Risk Management Systems

| TML Mechanism | Mapped Endpoints/Properties | Monograph Reference | Implementation Status |
|-------------|---------------------------|---------------------|----------------------|
| Continuous ethical assessment via Sacred Zero triggering | `POST /inference/decisions`, `current_state` | Section 2.3, Section 3.1 | SHIPPING |
| Pre-emptive defense through refusal logging | `POST /refusal/logging`, `threat_vector_analysis` | Section 2.3.2, Section 3.5 | SHIPPING |
| Risk-based routing via Gateway Logic | `POST /gateway/route` | Section 2.2 | SHIPPING (basic), BETA (adaptive) |

*Table 65: EU AI Act Article 9 Alignment*

#### 5.1.2 Article 10: Data and Data Governance

| TML Mechanism | Mapped Endpoints/Properties | Monograph Reference | Implementation Status |
|-------------|---------------------------|---------------------|----------------------|
| Data provenance and bias auditing via MTL schema | `POST /anchoring/logs`, `justification_data` | Section 3.4 | BETA |
| License terms as data governance controls | `POST /refusal/license-violation`, `license_violation` | Section 3.3.3 | SHIPPING |

*Table 66: EU AI Act Article 10 Alignment*

#### 5.1.3 Article 12: Record-Keeping

| TML Mechanism | Mapped Endpoints/Properties | Monograph Reference | Implementation Status |
|-------------|---------------------------|---------------------|----------------------|
| "No Log = No Action" automatic recording enforcement | `POST /anchoring/logs`, `permission_token` | Section 2.2.3, Section 3.2 | BETA |
| Internal reasoning logging (exceeds baseline) | All TSLF variants, `deliberation_matrix` | Section 3.4 | BETA |
| Cryptographic integrity via Merkle anchoring | `GET /audit/merkle-root`, `log_hash` | Section 3.8 | SHIPPING (root), BETA (real-time) |

*Table 67: EU AI Act Article 12 Alignment*

#### 5.1.4 Article 14: Human Oversight

| TML Mechanism | Mapped Endpoints/Properties | Monograph Reference | Implementation Status |
|-------------|---------------------------|---------------------|----------------------|
| Sacred Zero as "hook" for meaningful intervention | `POST /escalation/reviews`, `current_state` (value 0) | Section 2.3.3, Section 3.1 | BETA |
| Halting execution; humans authorize resumption | `POST /escalation/reviews`, `resolution_request` | Section 3.1.2 | BETA |
| Subject-initiated challenge and remedy | `POST /redress/challenge`, `POST /redress/grievance` | Section 3.5.3 | SHIPPING |
| Supreme authority override capability | `POST /emergency/shutdown`, `POST /emergency/state-transition` | Section 13.3 | BETA |

*Table 68: EU AI Act Article 14 Alignment*

#### 5.1.5 Article 15: Accuracy, Robustness, Cybersecurity

| TML Mechanism | Mapped Endpoints/Properties | Monograph Reference | Implementation Status |
|-------------|---------------------------|---------------------|----------------------|
| Adaptive Throttling Protocol for epistemic attack defense | `POST /anchoring/logs` (embedded) | Section 3.4 | BETA |
| Distributed resilience via 6-custodian architecture | `GET /audit/custodian-heartbeat` | Section 3.7 | BETA |
| Hardware kill switch for ultimate resilience | `POST /emergency/kill-switch` | Section 13.3, Section 10.5 | FUTURE |

*Table 69: EU AI Act Article 15 Alignment*

#### 5.1.6 Article 27: Reporting of Serious Incidents

| TML Mechanism | Mapped Endpoints/Properties | Monograph Reference | Implementation Status |
|-------------|---------------------------|---------------------|----------------------|
| Real-time Moral Trace Logs for streaming incident detection | `GET /escalation/status` (pattern analysis) | Section 3.4 | SHIPPING (basic), BETA (predictive) |
| Emergency shutdown as serious incident | `POST /emergency/shutdown` | Section 13.3 | BETA |
| License violation patterns as incident indicators | `POST /refusal/license-violation` | Section 3.3.3 | SHIPPING |

*Table 70: EU AI Act Article 27 Alignment*

#### 5.1.7 Article 61: Conformity Assessment

| TML Mechanism | Mapped Endpoints/Properties | Monograph Reference | Implementation Status |
|-------------|---------------------------|---------------------|----------------------|
| Comprehensive compliance attestation generation | `GET /audit/compliance-attestation` | Section 7 | BETA |
| Merkle root verification for technical documentation | `GET /audit/merkle-root` | Section 3.8 | SHIPPING |
| Bulk evidence export for assessment bodies | `GET /regulator/evidence-export` | Section 3.4, Section 12 | BETA |

*Table 71: EU AI Act Article 61 Alignment*

### 5.2 NIST AI RMF Alignment

#### 5.2.1 GOVERN Function

| TML Mechanism | Mapped Endpoints/Properties | Monograph Reference | Implementation Status |
|-------------|---------------------------|---------------------|----------------------|
| Binary-ternary parallel architecture as governance structure | `POST /inference/decisions`, `POST /anchoring/logs` | Section 2.2 | SHIPPING (Inference), BETA (Anchoring) |
| Goukassian Promise as demonstrable compliance | `POST /lantern/broadcast`, `the_signature` | Section 3.3 | SHIPPING |
| Human oversight process establishment | `POST /escalation/reviews` | Section 3.1 | BETA |
| Redress and grievance governance | `POST /redress/challenge`, `POST /redress/grievance` | Section 3.5 | SHIPPING |

*Table 72: NIST AI RMF GOVERN Function Alignment*

#### 5.2.2 MAP Function

| TML Mechanism | Mapped Endpoints/Properties | Monograph Reference | Implementation Status |
|-------------|---------------------------|---------------------|----------------------|
| Decision context vector for risk contextualization | `POST /inference/decisions`, `proposed_action` | Section 2.2 | SHIPPING |
| Threat vector analysis for harm contextualization | `POST /refusal/logging`, `threat_vector_analysis` | Section 3.5, Section 3.6 | BETA |
| Uncertainty quantification for ambiguity contextualization | `POST /escalation/reviews`, `uncertainty_quantification` | Section 3.1 | BETA |

*Table 73: NIST AI RMF MAP Function Alignment*

#### 5.2.3 MEASURE Function

| TML Mechanism | Mapped Endpoints/Properties | Monograph Reference | Implementation Status |
|-------------|---------------------------|---------------------|----------------------|
| Sacred Zero frequency and refusal rate metrics | `GET /inference/status` | Section 2.2 | SHIPPING |
| Governance effectiveness quantification | `GET /anchoring/status`, `GET /escalation/status` | Section 2.2, Section 3.1 | SHIPPING (basic), BETA (analytics) |
| Audit trail verification metrics | `GET /audit/merkle-root`, `GET /audit/log-inclusion-proof` | Section 3.8 | SHIPPING |
| Temporal metrics for timestamp integrity | `GET /regulator/timestamp-verification`, `signing_time` | Section 3.8 | BETA |

*Table 74: NIST AI RMF MEASURE Function Alignment*

#### 5.2.4 MANAGE Function

| TML Mechanism | Mapped Endpoints/Properties | Monograph Reference | Implementation Status |
|-------------|---------------------------|---------------------|----------------------|
| Risk treatment by refusal | `POST /refusal/logging` | Section 2.3.2 | SHIPPING |
| Resource allocation to risks via Dual-Lane Architecture | `POST /gateway/route` | Section 2.2 | SHIPPING (basic), BETA (adaptive) |
| Incident response and recovery | `POST /emergency/shutdown`, `POST /emergency/state-transition` | Section 13.3 | BETA |
| Corrective action via log re-evaluation | `POST /redress/log-re-evaluation` | Section 3.4, Section 3.5 | BETA |

*Table 75: NIST AI RMF MANAGE Function Alignment*

### 5.3 ISO 42001 Alignment

#### 5.3.1 Clause 7.3: Competence and Awareness

| TML Mechanism | Mapped Endpoints/Properties | Monograph Reference | Implementation Status |
|-------------|---------------------------|---------------------|----------------------|
| Reviewer qualification requirements | `POST /escalation/reviews` (embedded) | Section 3.1.4 | BETA |
| Complainant process awareness | `POST /redress/challenge`, `POST /redress/grievance` | Section 3.5 | SHIPPING |
| Public stakeholder awareness via Lantern | `POST /lantern/broadcast`, `compliance_beacon` | Section 3.3 | SHIPPING |

*Table 76: ISO 42001 Clause 7.3 Alignment*

#### 5.3.2 Clause 8.3: Risk Assessment and Treatment

| TML Mechanism | Mapped Endpoints/Properties | Monograph Reference | Implementation Status |
|-------------|---------------------------|---------------------|----------------------|
| Systematic AI risk identification and evaluation | `POST /inference/decisions`, `current_state` | Section 2.3 | SHIPPING |
| Risk treatment through triadic state classification | All TSLF variants | Section 2.3, Section 3.4 | BETA |
| Emergency risk treatment | `POST /emergency/shutdown`, `POST /emergency/state-transition` | Section 13.3 | BETA |

*Table 77: ISO 42001 Clause 8.3 Alignment*

#### 5.3.3 Clause 10: Improvement

| TML Mechanism | Mapped Endpoints/Properties | Monograph Reference | Implementation Status |
|-------------|---------------------------|---------------------|----------------------|
| PDCA cycle feeding via MTL database | `GET /inference/status`, `GET /anchoring/status` | Section 2.2, Section 3.4 | SHIPPING |
| Process improvement from escalation metrics | `GET /escalation/status` | Section 3.1 | SHIPPING (basic), BETA (predictive) |
| Feedback from re-evaluation into system enhancement | `POST /redress/log-re-evaluation` | Section 3.4, Section 3.5 | BETA |

*Table 78: ISO 42001 Clause 10 Alignment*

### 5.4 FRE 902 Rule Alignment

#### 5.4.1 Business Records Exception

| TML Mechanism | Mapped Endpoints/Properties | Monograph Reference | Implementation Status |
|-------------|---------------------------|---------------------|----------------------|
| Systematically maintained records of regularly conducted activity | `POST /anchoring/logs`, all TSLF variants | Section 3.4, Section 12 | BETA |
| Records made at or near the time by someone with knowledge | `permission_token.epoch_timestamp`, `signing_time` | Section 3.2, Section 3.8 | SHIPPING |
| Foundation testimony or certification for complex records | `GET /audit/compliance-attestation` | Section 12 | BETA |

*Table 79: FRE 902 Business Records Exception Alignment*

#### 5.4.2 Self-Authenticating Evidence

| TML Mechanism | Mapped Endpoints/Properties | Monograph Reference | Implementation Status |
|-------------|---------------------------|---------------------|----------------------|
| FRE 902(13): Certified records generated by electronic process | `GET /audit/merkle-root`, `log_hash` | Section 3.8, Section 12 | SHIPPING |
| FRE 902(14): Data copied from an electronic file | `GET /audit/log-inclusion-proof`, `audit_proof` | Section 3.8, Section 12 | SHIPPING |
| Qualified timestamp authentication | `GET /regulator/timestamp-verification`, `epoch_timestamp` | Section 3.8, Section 12 | BETA |

*Table 80: FRE 902 Self-Authenticating Evidence Alignment*

## 6. Implementation Status Classification

### 6.1 SHIPPING Criteria and Endpoints

**SHIPPING** status applies to elements **buildable with 2025 production libraries and infrastructure, with no known blockers from Section 10** of the monograph . The following endpoints and properties achieve this classification:

| Category | Endpoints/Properties | Rationale |
|----------|---------------------|-----------|
| Inference Lane Core | `POST /inference/decisions`, `GET /inference/status` | Standard HTTP/2, JWT, GPU acceleration mature |
| Basic Monitoring | `GET /escalation/status` (basic), `GET /gateway/status` | Observability infrastructure standard |
| Lantern Broadcasting | `POST /lantern/broadcast` | Pub/sub messaging mature |
| Refusal Logging Core | `POST /refusal/logging`, `POST /refusal/license-violation` (basic) | Structured logging with crypto signing standard |
| Redress Intake | `POST /redress/challenge`, `POST /redress/grievance` | Case management workflow infrastructure mature |
| Merkle Operations | `GET /audit/merkle-root` (root retrieval), `GET /audit/log-inclusion-proof` | Standard cryptographic libraries |
| Schema Foundations | `current_state`, `state_label`, `proposed_action`, all `PermissionToken` fields | JSON Schema Draft 2020-12, OpenSSL 3.x mature |

*Table 81: SHIPPING Classification Summary*

### 6.2 BETA Criteria and Endpoints

**BETA** status applies to elements **buildable with documented tradeoffs, where latency, cost, or throughput penalties are acceptable for regulated deployments** . The following elements achieve this classification:

| Category | Endpoints/Properties | Tradeoff Documentation |
|----------|---------------------|------------------------|
| Anchoring Lane Core | `POST /anchoring/logs`, `GET /anchoring/status` | HSM signing latency 100-500ms; batch anchoring vs. per-token |
| Sacred Zero Workflow | `POST /escalation/reviews`, `GET /escalation/status` (predictive) | Human review latency variable; median 4.7min, 95th 23min |
| Emergency Operations | `POST /emergency/shutdown`, `POST /emergency/state-transition` | Multi-custodian coordination 100ms-2s; graceful degradation |
| Custodian Monitoring | `GET /audit/custodian-heartbeat` | Cross-jurisdiction latency variability |
| Compliance Attestation | `GET /audit/compliance-attestation` | Complex evidence aggregation; 200-400ms snapshot generation |
| Evidence Export | `GET /regulator/evidence-export` | Chunked export (10K logs/chunk) for throughput/integrity balance |
| Timestamp Verification | `GET /regulator/timestamp-verification` | eIDAS TSP integration costs vary by member state |
| Log Re-evaluation | `POST /redress/log-re-evaluation` | Model checkpoint storage overhead ~40% |
| Adaptive Routing | `POST /gateway/route` (adaptive) | Real-time risk assessment complexity |

*Table 82: BETA Classification Summary*

### 6.3 FUTURE Criteria and Blocked Features

#### 6.3.1 Section 10 Implementation Gap References

**FUTURE** status applies to elements **blocked by named constraints from Section 10 (Implementation Gap)**, requiring `x-tml-blocking-constraint` annotations with quoted section references . The following elements are classified as FUTURE:

| Feature | Blocking Constraint | Monograph Reference | Proposed Mitigation | Mitigation Limitation |
|---------|--------------------:|--------------------:|--------------------:|----------------------:|
| Hardware kill switch | "Hardware Moral Processing Units (MPUs) and cryptographically validated safety relays remain research-stage components with no qualified suppliers for AI governance applications" | Section 10.5.2 | Software-level actuation suppression via `POST /emergency/shutdown` | Lacks physical guarantee of hardware cutoff |
| Real-time per-token blockchain anchoring | "Throughput asymmetry between inference lane (<2ms) and blockchain finality (seconds to minutes)" | Section 10.7.1
