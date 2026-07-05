# Constitutional Compliance Matrix
## TML Specification Architecture v3.3.0-tml-monograph-2025

**Authority:** TML Constitutionalization Monograph v3.3 > This Matrix > Existing Repository Files.  
**Purpose:** Maps every OpenAPI path and every JSON Schema definition to its monograph section, TML Pillar, regulatory nexus, and implementation status. Sufficient for auditor verification without reading implementation code.  
**Supersedes:** api/complete_api_reference.md (LEGACY)

**Regulatory Nexus Guard:** Regulatory mappings are made only to provisions explicitly cited or unmistakably implied in the monograph. All other cells carry: `Not directly referenced in monograph`.

**Implementation Status Key:**

| Status | Criteria |
|--------|----------|
| SHIPPING | Buildable with 2025 production libraries; no known blockers from Section 10. |
| BETA | Buildable with documented tradeoffs; latency, cost, or throughput penalties acceptable for regulated deployments. |
| FUTURE | Blocked by a named constraint from Section 10 (Implementation Gap). |

**Pillar Identifier Key:**

| Identifier | Pillar |
|------------|--------|
| SacredZero | Pillar I |
| AlwaysMemory | Pillar II |
| GoukassianPromise | Pillar III |
| MoralTraceLogs | Pillar IV |
| HumanRightsMandate | Pillar V |
| EarthProtectionMandate | Pillar VI |
| HybridShield | Pillar VII |
| PublicBlockchains | Pillar VIII |

---

## PART 1: OpenAPI Path Compliance Matrix

### 1.1 Inference Lane

| Path | Method | Operation | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|------|--------|-----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `/decisions` | POST | Submit Decision Vector | Section 2.3 | SacredZero, AlwaysMemory | Art. 9 (Risk Management); Art. 13 (Transparency) | ID.RA-01; DE.CM-01 | Cl. 6.1.2; Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `/decisions/{decisionId}` | GET | Retrieve Decision Record | Section 2.3; Section 8 | AlwaysMemory, MoralTraceLogs | Art. 13 (Transparency); Art. 19 (Logging) | ID.AM-03; DE.AE-02 | Cl. 8.5; Cl. 9.1 | Rule 902(11) (Certified Domestic Records) | SHIPPING |

### 1.2 Anchoring Lane

| Path | Method | Operation | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|------|--------|-----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `/anchoring-logs` | POST | Submit Moral Trace Log; Request Permission Token | Section 2.3.3; Section 8 | AlwaysMemory, PublicBlockchains, MoralTraceLogs | Art. 12 (Record-keeping); Art. 19 (Logging) | PR.DS-01; PR.DS-10; DE.CM-09 | Cl. 7.5; Cl. 8.5; Cl. 9.1 | Rule 902(11); Rule 902(13) (Certified Foreign Records) | SHIPPING |
| `/anchoring-logs/{logId}` | GET | Retrieve Anchoring Log Record | Section 8 | MoralTraceLogs, PublicBlockchains | Art. 12; Art. 19 | DE.AE-02; ID.AM-03 | Cl. 8.5; Cl. 9.1 | Rule 902(11) | SHIPPING |

### 1.3 Sacred Zero Escalation

| Path | Method | Operation | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|------|--------|-----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `/sacred-zero/escalations` | GET | List Sacred Zero Escalation Queue | Section 2.2 | SacredZero, HumanRightsMandate | Art. 9 (Risk Management); Art. 14 (Human Oversight) | GV.OC-01; DE.AE-06 | Cl. 6.1.2; Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `/sacred-zero/escalations/{escalationId}` | GET | Retrieve Sacred Zero Escalation Case | Section 2.2; Section 8 | SacredZero, MoralTraceLogs | Art. 14 (Human Oversight); Art. 19 | DE.AE-02; RS.AN-03 | Cl. 8.4; Cl. 9.1 | Rule 902(11) | SHIPPING |
| `/sacred-zero/escalations/{escalationId}` | PATCH | Resolve Sacred Zero Escalation | Section 2.2 | SacredZero, HumanRightsMandate, AlwaysMemory | Art. 14 (Human Oversight); Art. 22 (Fundamental Rights Impact) | RS.AN-03; RC.RP-01 | Cl. 8.4; Cl. 10.2 | Not directly referenced in monograph | SHIPPING |
| `/sacred-zero/lantern` | GET | Get Current Lantern Status | Section 2.4 | GoukassianPromise | Art. 13 (Transparency); Art. 50 (Transparency Obligations) | GV.OC-04; ID.RA-06 | Cl. 5.2; Cl. 7.4 | Not directly referenced in monograph | SHIPPING |

### 1.4 Refusal State

| Path | Method | Operation | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|------|--------|-----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `/refusals` | POST | Record Refusal State | Section 2.3; Section 2.4 | SacredZero, GoukassianPromise, AlwaysMemory | Art. 9; Art. 12; Art. 19 | PR.DS-01; DE.CM-01 | Cl. 6.1.2; Cl. 7.5; Cl. 8.4 | Rule 902(11) | SHIPPING |
| `/refusals/license-violations` | POST | Record License Violation | Section 2.4 | GoukassianPromise | Art. 9; Art. 13 | DE.CM-01; ID.RA-01 | Cl. 6.1.2; Cl. 8.4 | Not directly referenced in monograph | SHIPPING |

### 1.5 Emergency Override

| Path | Method | Operation | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|------|--------|-----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `/emergency/override` | POST | Execute Emergency Override | Section 13.3 | SacredZero, AlwaysMemory, HybridShield | Art. 9 (Risk Management); Art. 14 (Human Oversight) | RS.MA-01; RC.RP-01; GV.OC-01 | Cl. 6.1.2; Cl. 8.4; Cl. 10.2 | Not directly referenced in monograph | SHIPPING |
| `/emergency/status` | GET | Get Emergency Override Status | Section 13.3 | SacredZero, HybridShield | Art. 14; Art. 9 | DE.AE-06; GV.OC-01 | Cl. 8.4; Cl. 9.1 | Not directly referenced in monograph | SHIPPING |

### 1.6 Auditor Verification

| Path | Method | Operation | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|------|--------|-----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `/audit/verifications/merkle/{merkleRoot}` | GET | Verify Merkle Root | Section 8 | PublicBlockchains, MoralTraceLogs | Art. 19 (Logging); Art. 72 (Post-market Monitoring) | DE.AE-02; ID.AM-03 | Cl. 9.1; Cl. 9.2 | Rule 902(13) (Certified Foreign Records) | SHIPPING |
| `/audit/verifications/inclusion/{logId}` | GET | Get Log Inclusion Proof | Section 8 | PublicBlockchains, MoralTraceLogs, AlwaysMemory | Art. 12; Art. 19 | DE.AE-02; PR.DS-10 | Cl. 7.5; Cl. 9.1 | Rule 902(11); Rule 902(13) | SHIPPING |
| `/audit/custodians/{custodianId}/heartbeat` | GET | Get Custodian Heartbeat | Section 2.3.3 | HybridShield | Art. 9; Art. 19 | ID.AM-03; DE.CM-09 | Cl. 8.5; Cl. 9.1 | Not directly referenced in monograph | SHIPPING |
| `/audit/compliance/attestation` | GET | Pull Compliance Attestation | Section 2.4; Section 8 | GoukassianPromise, PublicBlockchains, HumanRightsMandate, EarthProtectionMandate | Art. 19; Art. 22; Art. 72 | GV.OC-04; DE.AE-02 | Cl. 9.1; Cl. 9.2; Cl. 9.3 | Rule 902(11) | SHIPPING |

### 1.7 Redress and Appeal

| Path | Method | Operation | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|------|--------|-----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `/redress/challenges` | POST | Submit Redress Challenge | Section 2.3.3 | HumanRightsMandate, MoralTraceLogs | Art. 26(7) (Redress Obligations); Art. 85 (Right to Explanation) | RS.AN-03; GV.OC-01 | Cl. 8.4; Cl. 10.2 | Not directly referenced in monograph | SHIPPING |
| `/redress/challenges/{challengeId}` | GET | Get Redress Challenge Status | Section 2.3.3 | HumanRightsMandate, MoralTraceLogs | Art. 26(7); Art. 85 | RS.AN-03; DE.AE-02 | Cl. 8.4; Cl. 9.1 | Not directly referenced in monograph | SHIPPING |
| `/redress/log-reevaluation` | POST | Request Log Re-evaluation | Section 8 | MoralTraceLogs, AlwaysMemory, HumanRightsMandate | Art. 12; Art. 26(7); Art. 85 | RS.AN-03; PR.DS-10 | Cl. 7.5; Cl. 8.4; Cl. 10.2 | Rule 902(11) | SHIPPING |
| `/redress/human-rights-grievances` | POST | File Human Rights Grievance | Section 2.3.3 | HumanRightsMandate, AlwaysMemory, PublicBlockchains | Art. 22 (Fundamental Rights Impact); Art. 85 | GV.OC-01; RS.AN-03 | Cl. 6.1.2; Cl. 8.4; Cl. 10.2 | Not directly referenced in monograph | SHIPPING |

### 1.8 Regulator Inspection

| Path | Method | Operation | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|------|--------|-----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `/regulator/evidence-export` | POST | Request Bulk Evidence Export | Section 8 | MoralTraceLogs, PublicBlockchains, AlwaysMemory | Art. 72 (Post-market Monitoring); Art. 74 (Market Surveillance) | GV.OC-05; DE.AE-02; PR.DS-01 | Cl. 9.1; Cl. 9.2; Cl. 7.5 | Rule 902(11); Rule 902(13) | SHIPPING |
| `/regulator/custodian-quorum` | GET | Get Custodian Quorum Status | Section 2.3.3 | HybridShield | Art. 9; Art. 19 | ID.AM-03; DE.CM-09 | Cl. 8.5; Cl. 9.1 | Not directly referenced in monograph | SHIPPING (endpoint); FUTURE (sub-500ms cross-jurisdiction quorum per Section 10) |
| `/regulator/timestamp-verification/{logId}` | GET | Verify Qualified Timestamp | Section 8 | MoralTraceLogs, PublicBlockchains | Art. 12; Art. 19 | PR.DS-10; DE.AE-02 | Cl. 7.5; Cl. 9.1 | Rule 902(9) (Certified Domestic Business Records); Rule 902(11) | SHIPPING |

### 1.9 Gateway

| Path | Method | Operation | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|------|--------|-----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `/gateway/status` | GET | Get Gateway Status (Fail-Closed) | Section 2.3 | SacredZero, AlwaysMemory | Art. 9; Art. 14 | DE.CM-09; GV.OC-01 | Cl. 8.4; Cl. 8.5 | Not directly referenced in monograph | SHIPPING |
| `/gateway/lane-assignment` | POST | Request Lane Assignment | Section 2.3 | SacredZero, AlwaysMemory, MoralTraceLogs | Art. 9; Art. 13; Art. 14 | ID.RA-01; DE.CM-01; GV.OC-01 | Cl. 6.1.2; Cl. 8.4; Cl. 8.5 | Not directly referenced in monograph | SHIPPING |

### 1.10 Goukassian Promise

| Path | Method | Operation | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|------|--------|-----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `/goukassian/signature` | GET | Get Signature Block | Section 2.4 | GoukassianPromise | Art. 13 (Transparency); Art. 50 | GV.OC-04; ID.RA-06 | Cl. 5.2; Cl. 7.4 | Rule 902(11) | SHIPPING |
| `/goukassian/license/validate` | POST | Validate License | Section 2.4 | GoukassianPromise | Art. 9; Art. 13 | ID.RA-01; DE.CM-01 | Cl. 6.1.2; Cl. 8.4 | Not directly referenced in monograph | SHIPPING |

### 1.11 Webhooks

| Webhook | Event | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|---------|-------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `sacredPauseEscalation` | Sacred Pause operational workflow triggers human review | Section 2.2 | SacredZero | Art. 14 (Human Oversight) | DE.AE-06; RS.AN-03 | Cl. 8.4; Cl. 10.2 | Not directly referenced in monograph | SHIPPING |
| `lanternStatusBroadcast` | Goukassian Promise Lantern compliance beacon update | Section 2.4 | GoukassianPromise | Art. 13; Art. 50 | GV.OC-04 | Cl. 7.4; Cl. 5.2 | Not directly referenced in monograph | SHIPPING |

---

### 1.12 Tri-Cameral Governance

| Path | Method | Operation | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|------|--------|-----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `TML_Core.registerTriCameralProposal` | ABI fn | Register governance proposal on-chain; proposer exit on submission; 180-day clock starts at submission | Section III; Section 7A | HybridShield | Art. 9; Art. 14 | GV.OC-01; GV.PO-01 | Cl. 5.2; Cl. 8.4 | Rule 902(13) | SHIPPING |
| `TML_Core.recordTriCameralVote` | ABI fn | Record Technical Council or Stewardship Custodian vote; vetoExercised=true constitutionally blocks | Section III; Section 7A | HybridShield | Art. 9; Art. 14 | GV.OC-01 | Cl. 5.2; Cl. 8.4 | Rule 902(13) | SHIPPING |
| `TML_Core.executeTriCameralRatification` | ABI fn | Smart Contract Treasury automatic execution; no admin key; no human override | Section III | HybridShield | Art. 9 | GV.OC-01 | Cl. 5.2 | Rule 902(13) | SHIPPING |
| `TML_Core` event `TriCameralConstitutionalVeto` | ABI event | Emitted when Stewardship Custodians exercise binding veto; immutable on-chain record | Section III; Section 7A | HybridShield | Art. 9; Art. 14 | GV.OC-01 | Cl. 5.2; Cl. 8.4 | Rule 902(13) | SHIPPING |
| `TML_Core` error `TriCameralNotRatified` | ABI error | Reverts premature ratification execution before dual-vote complete | Section III; Section 7A | HybridShield | Art. 9 | GV.OC-01 | Cl. 5.2 | Not directly referenced in monograph | SHIPPING |

---

## PART 2: JSON Schema Definition Compliance Matrix

### 2.1 Primitive and Shared Types

| Schema (`$defs` key) | Key Properties | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `TriadicStateValue` | `enum: [-1, 0, 1]`; signed integer; State 0 is SACRED_ZERO, not null/error/timeout | Section 2.3 (Triadic State Code / Goukassian Vow) | SacredZero | Art. 9 | ID.RA-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `TriadicStateLabel` | `enum: ["PROCEED", "SACRED_ZERO", "REFUSE"]`; UPPER_SNAKE_CASE per convention | Section 2.3 | SacredZero | Art. 13 | ID.RA-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `PillarIdentifier` | `enum` of all eight canonical PascalCase pillar identifiers; no aliasing permitted | Section 2 (Eight Pillars) | All Pillars | Art. 9; Art. 13 | GV.OC-04 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `LaneOrigin` | `enum: ["INFERENCE_LANE", "ANCHORING_LANE"]`; maps to Dual-Lane Architecture | Section 2.3 (Dual-Lane Latency Architecture) | SacredZero, AlwaysMemory | Art. 9 | ID.AM-03 | Cl. 8.5 | Not directly referenced in monograph | SHIPPING |
| `SHA256Hex` | `pattern: ^[a-f0-9]{64}$`; 64-char lowercase hex; tamper-evidence primitive | Section 8 | AlwaysMemory, MoralTraceLogs | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(11) | SHIPPING |
| `ISO8601DateTime` | `format: date-time`; RFC 3339 UTC; timestamp integrity primitive | Section 8 | MoralTraceLogs | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(9) | SHIPPING |
| `UUIDv4` | `format: uuid`; UUID v4 pattern; unique identifier primitive | Section 8 | MoralTraceLogs | Not directly referenced in monograph | Not directly referenced in monograph | Not directly referenced in monograph | Not directly referenced in monograph | SHIPPING |

### 2.2 Permission Token

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `PermissionToken` | `tokenId` | Section 2.3.3; Section 5B.i | AlwaysMemory, MoralTraceLogs | Art. 12 | PR.DS-01 | Cl. 7.5 | Rule 902(11) | SHIPPING |
| `PermissionToken` | `logHash` (SHA-256 of anchored Moral Trace Log; core No Log = No Action binding) | Section 2.3.3; Section 5B.i | AlwaysMemory, MoralTraceLogs, PublicBlockchains | Art. 12; Art. 19 | PR.DS-10; PR.DS-01 | Cl. 7.5; Cl. 9.1 | Rule 902(11) | SHIPPING |
| `PermissionToken` | `epochTimestamp` | Section 5B.i | AlwaysMemory | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(9) | SHIPPING |
| `PermissionToken` | `signerKeyId` (HSM key; HybridShield registry reference) | Section 2.3.3; Section 5B.i | HybridShield, GoukassianPromise | Art. 9 | PR.DS-01 | Cl. 8.5 | Not directly referenced in monograph | SHIPPING |
| `PermissionToken` | `laneOrigin` (`const: "ANCHORING_LANE"`; rejects Inference Lane tokens by schema) | Section 2.3; Section 5B.i | AlwaysMemory | Art. 9 | DE.CM-01 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `PermissionToken` | `merkleRoot` (non-repudiation binding to public blockchain anchor) | Section 8; Section 5B.i | PublicBlockchains, AlwaysMemory | Art. 12; Art. 19 | PR.DS-10 | Cl. 9.1 | Rule 902(13) | SHIPPING |
| `PermissionToken` | `signatureValue` (Base64url HSM signature; non-repudiation artifact) | Section 2.4; Section 5B.i | GoukassianPromise, HybridShield | Art. 9; Art. 13 | PR.DS-01 | Cl. 8.5 | Rule 902(11) | SHIPPING |
| `PermissionToken` | `issuedAt` | Section 5B.i | MoralTraceLogs | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(9) | SHIPPING |
| `PermissionToken` | `expiresAt` (actuation layer MUST reject expired tokens) | Section 5B.i | AlwaysMemory | Art. 9 | DE.CM-01 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `PermissionToken` | `decisionId` (additional token-to-decision binding) | Section 2.3.3; Section 5B.i | MoralTraceLogs | Art. 12 | PR.DS-01 | Cl. 7.5 | Not directly referenced in monograph | SHIPPING |
| `PermissionToken` | `custodianQuorumAttestation` (optional; BETA for full quorum attestation) | Section 2.3.3 | HybridShield | Art. 9 | ID.AM-03 | Cl. 8.5 | Not directly referenced in monograph | BETA |

### 2.3 State Envelope

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `StateEnvelope` | `envelopeId` | Section 2.3 | MoralTraceLogs | Art. 12 | PR.DS-01 | Cl. 7.5 | Not directly referenced in monograph | SHIPPING |
| `StateEnvelope` | `currentState` (signed integer; State 0 = SACRED_ZERO; never null/error/timeout) | Section 2.3 | SacredZero | Art. 9; Art. 13 | ID.RA-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `StateEnvelope` | `stateLabel` (constrained per state via `if/then/else`; must match `currentState`) | Section 2.3 | SacredZero | Art. 13 | ID.RA-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `StateEnvelope` | `processActive` (State 0: `const "SacredPause"`; Sacred Pause is workflow, not state synonym) | Section 2.2 | SacredZero | Art. 9; Art. 14 | DE.CM-01 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `StateEnvelope` | `proposedAction` (binary Inference Lane proposal; ternary Anchoring Lane dictates execution) | Section 2.3 | SacredZero, AlwaysMemory | Art. 9 | ID.RA-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `StateEnvelope` | `laneOrigin` | Section 2.3 | AlwaysMemory | Art. 9 | ID.AM-03 | Cl. 8.5 | Not directly referenced in monograph | SHIPPING |
| `StateEnvelope` | `createdAt` | Section 8 | MoralTraceLogs | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(9) | SHIPPING |
| `StateEnvelope` | `justificationObject` | Section 2.3 | MoralTraceLogs, AlwaysMemory | Art. 12; Art. 13 | PR.DS-01 | Cl. 7.5 | Not directly referenced in monograph | SHIPPING |
| `StateEnvelope` | `permissionToken` (REQUIRED when `currentState == 1`; schema-enforced via `if/then`; No Log = No Action) | Section 2.3.3; Section 5B.i | AlwaysMemory, MoralTraceLogs | Art. 12; Art. 19 | PR.DS-01; DE.CM-01 | Cl. 7.5; Cl. 8.4 | Rule 902(11) | SHIPPING |
| `StateEnvelope` | `anchoring` (Merkle batch metadata; populated post-Anchoring Lane processing) | Section 8 | PublicBlockchains, AlwaysMemory | Art. 12; Art. 19 | PR.DS-10 | Cl. 9.1 | Rule 902(13) | SHIPPING |
| `StateEnvelope` | `version` | Section 2.3 | Not directly referenced in monograph | Not directly referenced in monograph | Not directly referenced in monograph | Not directly referenced in monograph | Not directly referenced in monograph | SHIPPING |
| `StateEnvelope` | `if/then` constraint (currentState +1 requires permissionToken; schema-level No Log = No Action) | Section 2.3.3 | AlwaysMemory, MoralTraceLogs | Art. 12; Art. 19 | PR.DS-01 | Cl. 7.5 | Rule 902(11) | SHIPPING |

### 2.4 Justification Object

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `JustificationObject` | `justificationId` | Section 2.3 | MoralTraceLogs | Art. 12 | PR.DS-01 | Cl. 7.5 | Not directly referenced in monograph | SHIPPING |
| `JustificationObject` | `proposedState` (Inference Lane proposal only; not authoritative) | Section 2.3 | SacredZero | Art. 9 | ID.RA-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `JustificationObject` | `reasoningVector` (ordered Inference Lane reasoning chain) | Section 2.3 | MoralTraceLogs | Art. 13 (Transparency) | DE.AE-02 | Cl. 7.5 | Not directly referenced in monograph | SHIPPING |
| `JustificationObject` | `uncertaintyScore` (range [0.0, 1.0]; breach of threshold triggers SacredZero) | Section 2.2; Section 2.3 | SacredZero | Art. 9 | ID.RA-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `JustificationObject` | `pillarAssessments` (per-pillar compliance scores from Inference Lane) | Section 2.3 | All Pillars | Art. 9; Art. 13 | ID.RA-01; GV.OC-04 | Cl. 6.1.2; Cl. 9.1 | Not directly referenced in monograph | SHIPPING |
| `JustificationObject` | `generatedAt` | Section 8 | MoralTraceLogs | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(9) | SHIPPING |
| `JustificationObject` | `inferenceEngineId` (chain-of-custody for binary engine instance) | Section 8 | MoralTraceLogs, AlwaysMemory | Art. 12 | PR.DS-01 | Cl. 7.5 | Not directly referenced in monograph | SHIPPING |
| `JustificationObject` | `inputHash` (SHA-256 of decision vector; tamper-evidence) | Section 8 | AlwaysMemory, MoralTraceLogs | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(11) | SHIPPING |
| `JustificationObject` | `humanRightsMandateFlags` (UDHR/Geneva provision flags; triggers HumanRightsMandate review) | Section 2.3.3 | HumanRightsMandate | Art. 22 (Fundamental Rights Impact) | DE.CM-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `JustificationObject` | `earthProtectionMandateFlags` (Paris Agreement provision flags; triggers EarthProtectionMandate review) | Section 2.3.3 | EarthProtectionMandate | Art. 22 | DE.CM-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |

### 2.5 Uncertainty Quantification

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `UncertaintyQuantification` | `overallUncertaintyScore` | Section 2.2 | SacredZero | Art. 9 | ID.RA-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `UncertaintyQuantification` | `epistemicHoldActive` (`const: true` in State 0 logs; Epistemic Hold is canonical TML term) | Section 2.2 | SacredZero | Art. 9; Art. 14 | ID.RA-01 | Cl. 6.1.2; Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `UncertaintyQuantification` | `uncertaintyDimensions` (decomposed per-dimension scores) | Section 2.2 | SacredZero | Art. 9 | ID.RA-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `UncertaintyQuantification` | `quantifiedAt` | Section 8 | MoralTraceLogs | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(9) | SHIPPING |
| `UncertaintyQuantification` | `thresholdBreached` (configured SacredZero threshold value) | Section 2.2 | SacredZero | Art. 9 | ID.RA-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |

### 2.6 Deliberation Matrix

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `DeliberationMatrix` | `matrixId` | Section 2.2 | SacredZero | Art. 14 | RS.AN-03 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `DeliberationMatrix` | `considerations` (per-pillar ethical, factual, and legal considerations) | Section 2.2 | SacredZero, All Pillars | Art. 9; Art. 14 | RS.AN-03 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `DeliberationMatrix` | `riskVectors` (risk vector set for human reviewer) | Section 2.2 | SacredZero | Art. 9; Art. 14 | ID.RA-01; RS.AN-03 | Cl. 6.1.2; Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `DeliberationMatrix` | `resolutionOptions` (`proposedState enum: [1, -1]`; State 0 not a valid resolution) | Section 2.2 | SacredZero, HumanRightsMandate | Art. 14 | RS.AN-03; RC.RP-01 | Cl. 8.4; Cl. 10.2 | Not directly referenced in monograph | SHIPPING |

### 2.7 Resolution Request

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `ResolutionRequest` | `resolutionRequestId` | Section 2.2 | SacredZero | Art. 14 | RS.AN-03 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `ResolutionRequest` | `escalationId` | Section 2.2 | SacredZero | Art. 14 | RS.AN-03 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `ResolutionRequest` | `priority` (`enum: ["STANDARD","ELEVATED","CRITICAL"]`) | Section 2.2 | SacredZero | Art. 14 | RS.AN-03 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `ResolutionRequest` | `deliberationMatrix` | Section 2.2 | SacredZero | Art. 14 | RS.AN-03 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `ResolutionRequest` | `deadlineAt` (HybridShield failover if exceeded) | Section 2.2; Section 2.3.3 | SacredZero, HybridShield | Art. 14 | RS.AN-03 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |

### 2.8 TSLF-State0 (Sacred Pause Log)

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `TSLF-State0` | `logId` | Section 8 | MoralTraceLogs | Art. 12; Art. 19 | PR.DS-01 | Cl. 7.5 | Rule 902(11) | SHIPPING |
| `TSLF-State0` | `currentState` (`const: 0`; discriminator; Sacred Zero is never null/error/timeout) | Section 2.2; Section 8 | SacredZero | Art. 9; Art. 13 | ID.RA-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `TSLF-State0` | `stateLabel` (`const: "SACRED_ZERO"`) | Section 2.2 | SacredZero | Art. 13 | ID.RA-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `TSLF-State0` | `processActive` (`const: "SacredPause"`; Sacred Pause is operational workflow within State 0, not a state synonym) | Section 2.2 | SacredZero | Art. 9; Art. 14 | DE.CM-01 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `TSLF-State0` | `logVersion` | Section 8 | MoralTraceLogs | Art. 12 | PR.DS-01 | Cl. 7.5 | Not directly referenced in monograph | SHIPPING |
| `TSLF-State0` | `decisionId` | Section 8 | MoralTraceLogs | Art. 12 | PR.DS-01 | Cl. 7.5 | Not directly referenced in monograph | SHIPPING |
| `TSLF-State0` | `envelopeId` | Section 2.3; Section 8 | MoralTraceLogs | Art. 12 | PR.DS-01 | Cl. 7.5 | Not directly referenced in monograph | SHIPPING |
| `TSLF-State0` | `lanternStatus` (Goukassian Promise Lantern must reflect SacredZero state at activation) | Section 2.4; Section 2.2 | GoukassianPromise, SacredZero | Art. 13 | GV.OC-04 | Cl. 5.2; Cl. 7.4 | Not directly referenced in monograph | SHIPPING |
| `TSLF-State0` | `uncertaintyQuantification` | Section 2.2; Section 8 | SacredZero | Art. 9 | ID.RA-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `TSLF-State0` | `deliberationMatrix` | Section 2.2 | SacredZero | Art. 14 | RS.AN-03 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `TSLF-State0` | `resolutionRequest` | Section 2.2 | SacredZero, HumanRightsMandate | Art. 14 | RS.AN-03 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `TSLF-State0` | `committedAt` (pre-actuation commit; AlwaysMemory anti-spoliation; before any human review) | Section 8 | AlwaysMemory | Art. 12; Art. 19 | PR.DS-10 | Cl. 7.5 | Rule 902(11) | SHIPPING |
| `TSLF-State0` | `pillarsCertified` (Eight Pillars assessed at commit time) | Section 2; Section 8 | All Pillars | Art. 9 | GV.OC-04 | Cl. 9.1 | Not directly referenced in monograph | SHIPPING |
| `TSLF-State0` | `merkleAnchoringStatus` | Section 8 | PublicBlockchains, AlwaysMemory | Art. 12; Art. 19 | PR.DS-10 | Cl. 9.1 | Rule 902(13) | SHIPPING |
| `TSLF-State0` | `resolution` (human authority resolution record; resolvedState enum [1,-1] only) | Section 2.2 | SacredZero, HumanRightsMandate, AlwaysMemory | Art. 14 | RS.AN-03; RC.RP-01 | Cl. 8.4; Cl. 10.2 | Rule 902(11) | SHIPPING |

### 2.9 License Violation Record

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `LicenseViolationRecord` | `violationId` | Section 2.4 | GoukassianPromise | Art. 9 | DE.CM-01 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `LicenseViolationRecord` | `violationType` (`enum` of five violation categories) | Section 2.4 | GoukassianPromise | Art. 9 | DE.CM-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `LicenseViolationRecord` | `violatedArtifact` (`enum: ["lantern","signature","license"]`; canonical lowercase artifact names) | Section 2.4 | GoukassianPromise | Art. 13 | DE.CM-01 | Cl. 5.2 | Not directly referenced in monograph | SHIPPING |
| `LicenseViolationRecord` | `description` | Section 2.4 | GoukassianPromise | Art. 13 | DE.CM-01 | Cl. 7.5 | Not directly referenced in monograph | SHIPPING |
| `LicenseViolationRecord` | `detectedAt` | Section 8 | MoralTraceLogs | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(9) | SHIPPING |
| `LicenseViolationRecord` | `evidenceHash` | Section 8 | AlwaysMemory, GoukassianPromise | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(11) | SHIPPING |

### 2.10 Threat Vector Analysis

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `ThreatVectorAnalysis` | `analysisId` | Section 2.3; Section 8 | MoralTraceLogs | Art. 12 | PR.DS-01 | Cl. 7.5 | Not directly referenced in monograph | SHIPPING |
| `ThreatVectorAnalysis` | `threatVectors` (8-category enum incl. HUMAN_RIGHTS_VIOLATION, EARTH_PROTECTION_VIOLATION) | Section 2.3 | All Pillars | Art. 9; Art. 22 | ID.RA-01; DE.CM-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `ThreatVectorAnalysis` | `udhrProvision` per vector (UDHR Article tracking; HumanRightsMandate enforcement) | Section 2.3.3 | HumanRightsMandate | Art. 22 | DE.CM-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `ThreatVectorAnalysis` | `parisAgreementProvision` per vector (Paris Agreement tracking; EarthProtectionMandate enforcement) | Section 2.3.3 | EarthProtectionMandate | Art. 22 | DE.CM-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `ThreatVectorAnalysis` | `overallSeverity` | Section 2.3 | MoralTraceLogs | Art. 9 | ID.RA-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `ThreatVectorAnalysis` | `analysedAt` | Section 8 | MoralTraceLogs | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(9) | SHIPPING |

### 2.11 Chain of Custody

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `ChainOfCustody` | `custodyChainId` | Section 8 | MoralTraceLogs, AlwaysMemory | Art. 12 | PR.DS-01 | Cl. 7.5 | Rule 902(11) | SHIPPING |
| `ChainOfCustody` | `entries` (ordered sequence of CREATED, RECEIVED, VALIDATED, ANCHORED, etc.) | Section 8 | MoralTraceLogs, AlwaysMemory | Art. 12; Art. 19 | PR.DS-01; PR.DS-10 | Cl. 7.5; Cl. 9.1 | Rule 902(11); Rule 902(13) | SHIPPING |
| `ChainOfCustody` | `inputHash` / `outputHash` per entry (tamper-evidence across handler transitions) | Section 8 | AlwaysMemory, MoralTraceLogs | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(11) | SHIPPING |

### 2.12 TSLF-State-1 (Refusal Log)

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `TSLF-State-1` | `currentState` (`const: -1`; discriminator) | Section 2.3; Section 8 | SacredZero | Art. 9; Art. 13 | ID.RA-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `TSLF-State-1` | `stateLabel` (`const: "REFUSE"`) | Section 2.3 | SacredZero | Art. 13 | ID.RA-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `TSLF-State-1` | `processActive` (`const: "RefusalLogging"`) | Section 2.3 | SacredZero, AlwaysMemory | Art. 9 | DE.CM-01 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `TSLF-State-1` | `licenseViolation` (optional; required when Goukassian Promise violation triggers refusal) | Section 2.4; Section 8 | GoukassianPromise, AlwaysMemory | Art. 9; Art. 13 | DE.CM-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `TSLF-State-1` | `threatVectorAnalysis` | Section 2.3; Section 8 | MoralTraceLogs | Art. 9; Art. 12 | ID.RA-01; DE.CM-01 | Cl. 6.1.2; Cl. 7.5 | Not directly referenced in monograph | SHIPPING |
| `TSLF-State-1` | `chainOfCustody` | Section 8 | MoralTraceLogs, AlwaysMemory | Art. 12; Art. 19 | PR.DS-01; PR.DS-10 | Cl. 7.5; Cl. 9.1 | Rule 902(11) | SHIPPING |
| `TSLF-State-1` | `committedAt` (pre-actuation commit; AlwaysMemory) | Section 8 | AlwaysMemory | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(11) | SHIPPING |
| `TSLF-State-1` | `refusalIsPermanent` (`default: true`; permanent unless Section 13.3 supreme override) | Section 13.3 | SacredZero, AlwaysMemory | Art. 9 | PR.DS-01 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `TSLF-State-1` | `appealEligible` (`default: true`; subject redress right) | Section 2.3.3 | HumanRightsMandate | Art. 26(7); Art. 85 | GV.OC-01 | Cl. 10.2 | Not directly referenced in monograph | SHIPPING |

### 2.13 Ethical Verification

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `EthicalVerification` | `verificationId` | Section 2.3.3; Section 8 | MoralTraceLogs | Art. 12 | PR.DS-01 | Cl. 7.5 | Not directly referenced in monograph | SHIPPING |
| `EthicalVerification` | `pillarVerifications` (all Eight Pillars required; all must be PASSED for PROCEED) | Section 2.3.3 | All Pillars | Art. 9; Art. 13 | GV.OC-04; ID.RA-01 | Cl. 6.1.2; Cl. 9.1 | Not directly referenced in monograph | SHIPPING |
| `EthicalVerification` | `overallVerdict` (`enum: ["PASSED","FAILED"]`; FAILED triggers State -1) | Section 2.3.3 | All Pillars | Art. 9 | ID.RA-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `EthicalVerification` | `verifiedAt` | Section 8 | MoralTraceLogs | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(9) | SHIPPING |
| `EthicalVerification` | `verifierEngineId` (Anchoring Lane ternary engine identity; chain-of-custody) | Section 8 | MoralTraceLogs, AlwaysMemory | Art. 12 | PR.DS-01 | Cl. 7.5 | Not directly referenced in monograph | SHIPPING |
| `PillarVerificationResult` | `verdict` (`enum: ["PASSED","FAILED","NOT_APPLICABLE"]`; FAILED blocks PROCEED) | Section 2.3.3 | All Pillars | Art. 9 | GV.OC-04 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `PillarVerificationResult` | `verifiedAt` | Section 8 | MoralTraceLogs | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(9) | SHIPPING |

### 2.14 Audit Proof

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `AuditProof` | `proofId` | Section 8 | MoralTraceLogs | Art. 12 | PR.DS-01 | Cl. 7.5 | Not directly referenced in monograph | SHIPPING |
| `AuditProof` | `permissionTokenId` (binds proof to specific Permission Token) | Section 2.3.3; Section 8 | AlwaysMemory, MoralTraceLogs | Art. 12 | PR.DS-01 | Cl. 7.5 | Rule 902(11) | SHIPPING |
| `AuditProof` | `logHash` (must match Permission Token `logHash`; enforces No Log = No Action at proof level) | Section 2.3.3; Section 8 | AlwaysMemory | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(11) | SHIPPING |
| `AuditProof` | `merkleRoot` (must match Permission Token `merkleRoot`) | Section 8 | PublicBlockchains | Art. 19 | PR.DS-10 | Cl. 9.1 | Rule 902(13) | SHIPPING |
| `AuditProof` | `inclusionPath` (ordered sibling hashes; Merkle inclusion proof) | Section 8 | PublicBlockchains | Art. 12; Art. 19 | PR.DS-10 | Cl. 9.1 | Rule 902(13) | SHIPPING |
| `AuditProof` | `blockchainTxId` | Section 8 | PublicBlockchains | Art. 19 | PR.DS-10 | Cl. 9.1 | Rule 902(13) | SHIPPING |

### 2.15 TSLF-StateP1 (Proceed Log)

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `TSLF-StateP1` | `currentState` (`const: 1`; discriminator) | Section 2.3; Section 8 | AlwaysMemory | Art. 9; Art. 13 | ID.RA-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `TSLF-StateP1` | `stateLabel` (`const: "PROCEED"`) | Section 2.3 | AlwaysMemory | Art. 13 | ID.RA-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `TSLF-StateP1` | `processActive` (`const: "ActuationGated"`) | Section 2.3 | AlwaysMemory | Art. 9 | DE.CM-01 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `TSLF-StateP1` | `ethicalVerification` (all Eight Pillars must be PASSED) | Section 2.3.3 | All Pillars | Art. 9; Art. 13 | GV.OC-04 | Cl. 6.1.2; Cl. 9.1 | Not directly referenced in monograph | SHIPPING |
| `TSLF-StateP1` | `theSignature` (Goukassian Promise Signature; provenance and non-repudiation) | Section 2.4 | GoukassianPromise | Art. 13 | PR.DS-01 | Cl. 5.2 | Rule 902(11) | SHIPPING |
| `TSLF-StateP1` | `auditProof` (Merkle inclusion proof; binds Permission Token to anchored log) | Section 8 | PublicBlockchains, AlwaysMemory | Art. 12; Art. 19 | PR.DS-10 | Cl. 9.1 | Rule 902(13) | SHIPPING |
| `TSLF-StateP1` | `permissionToken` (REQUIRED; schema-level No Log = No Action enforcement in Proceed log) | Section 2.3.3; Section 5B.i | AlwaysMemory, MoralTraceLogs | Art. 12; Art. 19 | PR.DS-01; DE.CM-01 | Cl. 7.5; Cl. 8.4 | Rule 902(11) | SHIPPING |
| `TSLF-StateP1` | `committedAt` (log anchored before Permission Token released to actuation layer) | Section 8 | AlwaysMemory | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(11) | SHIPPING |
| `TSLF-StateP1` | `pillarsCertified` (`minItems: 8, maxItems: 8`; all Eight Pillars mandatory for PROCEED) | Section 2; Section 8 | All Pillars | Art. 9 | GV.OC-04 | Cl. 9.1 | Not directly referenced in monograph | SHIPPING |

### 2.16 Lantern Status

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `LanternStatus` | `lanternId` | Section 2.4 | GoukassianPromise | Art. 13 | GV.OC-04 | Cl. 7.4 | Not directly referenced in monograph | SHIPPING |
| `LanternStatus` | `artifactName` (`const: "lantern"`; canonical Goukassian Promise artifact name, lowercase) | Section 2.4 | GoukassianPromise | Art. 13 | GV.OC-04 | Cl. 5.2 | Not directly referenced in monograph | SHIPPING |
| `LanternStatus` | `currentSystemState` (aggregate triadic state of TML system) | Section 2.3; Section 2.4 | SacredZero, GoukassianPromise | Art. 13 | GV.OC-04; ID.RA-06 | Cl. 5.2; Cl. 7.4 | Not directly referenced in monograph | SHIPPING |
| `LanternStatus` | `compliancePosture` (5-value enum incl. SACRED_ZERO_ACTIVE, EMERGENCY_OVERRIDE_ACTIVE) | Section 2.4 | GoukassianPromise | Art. 13; Art. 50 | GV.OC-04 | Cl. 5.2; Cl. 7.4 | Not directly referenced in monograph | SHIPPING |
| `LanternStatus` | `pillarStatuses` (per-pillar live compliance status) | Section 2; Section 2.4 | All Pillars | Art. 13 | GV.OC-04 | Cl. 9.1 | Not directly referenced in monograph | SHIPPING |
| `LanternStatus` | `signalEmittedAt` | Section 8 | MoralTraceLogs | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(9) | SHIPPING |
| `LanternStatus` | `signatureBlock` (Goukassian Promise Signature signing each Lantern broadcast) | Section 2.4 | GoukassianPromise | Art. 13 | PR.DS-01 | Cl. 5.2 | Rule 902(11) | SHIPPING |
| `LanternStatus` | `activeSacredZeroCount` | Section 2.2; Section 2.4 | SacredZero, GoukassianPromise | Art. 13; Art. 14 | DE.AE-06 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `LanternStatus` | `emergencyOverrideActive` | Section 13.3; Section 2.4 | SacredZero, HybridShield | Art. 14 | GV.OC-01 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |

### 2.17 Signature Block

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `SignatureBlock` | `signatureId` | Section 2.4 | GoukassianPromise | Art. 13 | PR.DS-01 | Cl. 5.2 | Not directly referenced in monograph | SHIPPING |
| `SignatureBlock` | `artifactName` (`const: "signature"`; canonical Goukassian Promise artifact name, lowercase) | Section 2.4 | GoukassianPromise | Art. 13 | GV.OC-04 | Cl. 5.2 | Not directly referenced in monograph | SHIPPING |
| `SignatureBlock` | `signerIdentity` | Section 2.4 | GoukassianPromise | Art. 13 | PR.DS-01 | Cl. 5.2 | Rule 902(11) | SHIPPING |
| `SignatureBlock` | `signerKeyId` | Section 2.4 | GoukassianPromise, HybridShield | Art. 9 | PR.DS-01 | Cl. 8.5 | Not directly referenced in monograph | SHIPPING |
| `SignatureBlock` | `signedPayloadHash` | Section 8 | AlwaysMemory, GoukassianPromise | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(11) | SHIPPING |
| `SignatureBlock` | `signatureValue` | Section 2.4 | GoukassianPromise | Art. 13 | PR.DS-01 | Cl. 5.2 | Rule 902(11) | SHIPPING |
| `SignatureBlock` | `signatureAlgorithm` (ES256 = SHIPPING; SLH-DSA-SHAKE-128s, ML-KEM-1024 = FUTURE per Section 10) | Section 2.4; Section 10 | GoukassianPromise | Art. 9 | PR.DS-01 | Cl. 8.5 | Not directly referenced in monograph | SHIPPING (ES256); FUTURE (PQC) |
| `SignatureBlock` | `signedAt` | Section 8 | MoralTraceLogs | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(9) | SHIPPING |
| `SignatureBlock` | `certChain` | Section 2.4 | GoukassianPromise | Art. 9 | PR.DS-01 | Cl. 8.5 | Rule 902(11) | SHIPPING |
| `SignatureBlock` | `custodianId` | Section 2.3.3 | HybridShield | Art. 9 | ID.AM-03 | Cl. 8.5 | Not directly referenced in monograph | SHIPPING |

### 2.18 License Validation Request

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `LicenseValidationRequest` | `validationRequestId` | Section 2.4 | GoukassianPromise | Art. 9 | DE.CM-01 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `LicenseValidationRequest` | `artifactName` (`const: "license"`; canonical Goukassian Promise artifact name, lowercase) | Section 2.4 | GoukassianPromise | Art. 13 | GV.OC-04 | Cl. 5.2 | Not directly referenced in monograph | SHIPPING |
| `LicenseValidationRequest` | `licenseToken` | Section 2.4 | GoukassianPromise | Art. 9 | DE.CM-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `LicenseValidationRequest` | `requestingEntityId` | Section 2.4 | GoukassianPromise | Art. 13 | ID.AM-03 | Cl. 5.2 | Not directly referenced in monograph | SHIPPING |
| `LicenseValidationRequest` | `requestedAt` | Section 8 | MoralTraceLogs | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(9) | SHIPPING |
| `LicenseValidationRequest` | `purposeOfUse` | Section 2.4 | GoukassianPromise | Art. 13 | ID.RA-06 | Cl. 7.4 | Not directly referenced in monograph | SHIPPING |
| `LicenseValidationRequest` | `decisionId` | Section 2.3 | MoralTraceLogs | Art. 12 | PR.DS-01 | Cl. 7.5 | Not directly referenced in monograph | SHIPPING |

### 2.19 Merkle Inclusion Proof

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `MerkleInclusionProof` | `proofId` | Section 8 | PublicBlockchains | Art. 19 | PR.DS-10 | Cl. 9.1 | Not directly referenced in monograph | SHIPPING |
| `MerkleInclusionProof` | `logId` | Section 8 | MoralTraceLogs | Art. 12 | PR.DS-01 | Cl. 7.5 | Rule 902(11) | SHIPPING |
| `MerkleInclusionProof` | `logHash` (leaf node; SHA-256) | Section 8 | AlwaysMemory, PublicBlockchains | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(11) | SHIPPING |
| `MerkleInclusionProof` | `merkleRoot` | Section 8 | PublicBlockchains | Art. 19 | PR.DS-10 | Cl. 9.1 | Rule 902(13) | SHIPPING |
| `MerkleInclusionProof` | `inclusionPath` | Section 8 | PublicBlockchains | Art. 19 | PR.DS-10 | Cl. 9.1 | Rule 902(13) | SHIPPING |
| `MerkleInclusionProof` | `batchId` | Section 8 | PublicBlockchains | Art. 19 | PR.DS-01 | Cl. 9.1 | Not directly referenced in monograph | SHIPPING |
| `MerkleInclusionProof` | `anchoredAt` | Section 8 | PublicBlockchains, AlwaysMemory | Art. 12; Art. 19 | PR.DS-10 | Cl. 9.1 | Rule 902(9) | SHIPPING |
| `MerkleInclusionProof` | `blockchainTxId` | Section 8 | PublicBlockchains | Art. 19 | PR.DS-10 | Cl. 9.1 | Rule 902(13) | SHIPPING |
| `MerkleInclusionProof` | `blockchainNetwork` | Section 8 | PublicBlockchains | Art. 19 | ID.AM-03 | Cl. 9.1 | Not directly referenced in monograph | SHIPPING |
| `MerkleInclusionProof` | `verificationStatus` (`enum: ["VERIFIED","PENDING","FAILED"]`) | Section 8 | PublicBlockchains | Art. 19 | DE.AE-02 | Cl. 9.1 | Not directly referenced in monograph | SHIPPING |

### 2.20 Custodian Heartbeat

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `CustodianHeartbeat` | `custodianId` | Section 2.3.3 | HybridShield | Art. 9 | ID.AM-03 | Cl. 8.5 | Not directly referenced in monograph | SHIPPING |
| `CustodianHeartbeat` | `status` (`enum: ["ACTIVE","DEGRADED","UNREACHABLE","ROTATING_KEYS"]`) | Section 2.3.3 | HybridShield | Art. 9 | ID.AM-03; DE.CM-09 | Cl. 8.5 | Not directly referenced in monograph | SHIPPING |
| `CustodianHeartbeat` | `lastHeartbeatAt` | Section 2.3.3 | HybridShield | Art. 9 | DE.CM-09 | Cl. 8.5 | Not directly referenced in monograph | SHIPPING |
| `CustodianHeartbeat` | `jurisdiction` | Section 2.3.3 | HybridShield | Art. 9 | GV.OC-05 | Cl. 8.5 | Not directly referenced in monograph | SHIPPING |
| `CustodianHeartbeat` | `latencyMs` (sub-500ms cross-jurisdiction = FUTURE per Section 10) | Section 2.3.3; Section 10 | HybridShield | Art. 9 | DE.CM-09 | Cl. 8.5 | Not directly referenced in monograph | SHIPPING (field); FUTURE (sub-500ms global) |
| `CustodianHeartbeat` | `keyVersion` | Section 2.3.3 | HybridShield | Art. 9 | PR.DS-01 | Cl. 8.5 | Not directly referenced in monograph | SHIPPING |

### 2.21 Compliance Attestation

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `ComplianceAttestation` | `attestationId` | Section 2.4; Section 8 | GoukassianPromise | Art. 13 | GV.OC-04 | Cl. 9.1 | Not directly referenced in monograph | SHIPPING |
| `ComplianceAttestation` | `attestedAt` | Section 8 | MoralTraceLogs | Art. 12 | PR.DS-10 | Cl. 9.1 | Rule 902(9) | SHIPPING |
| `ComplianceAttestation` | `pillarCompliance` (all Eight Pillars required) | Section 2; Section 2.4 | All Pillars | Art. 9; Art. 13 | GV.OC-04 | Cl. 9.1; Cl. 9.2; Cl. 9.3 | Not directly referenced in monograph | SHIPPING |
| `ComplianceAttestation` | `overallStatus` (`enum: ["FULLY_COMPLIANT","PARTIAL_COMPLIANCE","NON_COMPLIANT"]`) | Section 2.4 | GoukassianPromise | Art. 13 | GV.OC-04 | Cl. 9.1 | Not directly referenced in monograph | SHIPPING |
| `ComplianceAttestation` | `signatureBlock` (Goukassian Promise Signature on attestation) | Section 2.4 | GoukassianPromise | Art. 13 | PR.DS-01 | Cl. 5.2 | Rule 902(11) | SHIPPING |
| `ComplianceAttestation` | `merkleRoot` (attestation anchored to public blockchain) | Section 8 | PublicBlockchains | Art. 19 | PR.DS-10 | Cl. 9.1 | Rule 902(13) | SHIPPING |

### 2.22 Redress Challenge

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `RedressChallenge` | `challengeId` | Section 2.3.3 | HumanRightsMandate | Art. 26(7); Art. 85 | GV.OC-01 | Cl. 10.2 | Not directly referenced in monograph | SHIPPING |
| `RedressChallenge` | `subjectIdentity` | Section 2.3.3 | HumanRightsMandate | Art. 85 | GV.OC-01 | Cl. 10.2 | Not directly referenced in monograph | SHIPPING |
| `RedressChallenge` | `challengedLogId` | Section 8 | MoralTraceLogs, HumanRightsMandate | Art. 12; Art. 85 | RS.AN-03 | Cl. 9.1; Cl. 10.2 | Rule 902(11) | SHIPPING |
| `RedressChallenge` | `challengeGrounds` (per-pillar grounds; optional UDHR Article citation) | Section 2.3.3 | HumanRightsMandate | Art. 22; Art. 85 | GV.OC-01; RS.AN-03 | Cl. 6.1.2; Cl. 10.2 | Not directly referenced in monograph | SHIPPING |
| `RedressChallenge` | `submittedAt` | Section 8 | MoralTraceLogs | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(9) | SHIPPING |
| `RedressChallenge` | `supportingEvidenceHash` | Section 8 | AlwaysMemory | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(11) | SHIPPING |

### 2.23 Human Rights Grievance

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `HumanRightsGrievance` | `grievanceId` | Section 2.3.3 | HumanRightsMandate | Art. 22; Art. 85 | GV.OC-01 | Cl. 10.2 | Not directly referenced in monograph | SHIPPING |
| `HumanRightsGrievance` | `complainantIdentity` | Section 2.3.3 | HumanRightsMandate | Art. 85 | GV.OC-01 | Cl. 10.2 | Not directly referenced in monograph | SHIPPING |
| `HumanRightsGrievance` | `udhrProvisions` (UDHR Articles alleged violated; HumanRightsMandate vector enforcement) | Section 2.3.3 | HumanRightsMandate | Art. 22 | DE.CM-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `HumanRightsGrievance` | `genevaConventionProvisions` (Geneva Convention provisions; HumanRightsMandate) | Section 2.3.3 | HumanRightsMandate | Art. 22 | DE.CM-01 | Cl. 6.1.2 | Not directly referenced in monograph | SHIPPING |
| `HumanRightsGrievance` | `grievanceNarrative` (`minLength: 100`) | Section 2.3.3 | HumanRightsMandate | Art. 85 | GV.OC-01 | Cl. 10.2 | Not directly referenced in monograph | SHIPPING |
| `HumanRightsGrievance` | `filedAt` | Section 8 | MoralTraceLogs | Art. 12 | PR.DS-10 | Cl. 7.5 | Rule 902(9) | SHIPPING |
| `HumanRightsGrievance` | `requestedRemedy` | Section 2.3.3 | HumanRightsMandate | Art. 85 | GV.OC-01 | Cl. 10.2 | Not directly referenced in monograph | SHIPPING |

### 2.24 Bulk Evidence Export

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `BulkEvidenceExport` | `exportRequestId` | Section 8 | MoralTraceLogs | Art. 72; Art. 74 | GV.OC-05 | Cl. 9.2 | Not directly referenced in monograph | SHIPPING |
| `BulkEvidenceExport` | `regulatorIdentity` | Section 8 | MoralTraceLogs | Art. 74 | GV.OC-05 | Cl. 9.2 | Not directly referenced in monograph | SHIPPING |
| `BulkEvidenceExport` | `legalBasis` | Section 8 | MoralTraceLogs, HumanRightsMandate | Art. 72; Art. 74 | GV.OC-05 | Cl. 9.2 | Not directly referenced in monograph | SHIPPING |
| `BulkEvidenceExport` | `exportScope` (date range, state filter, pillar filter, token/proof inclusion flags) | Section 8 | MoralTraceLogs, PublicBlockchains | Art. 72; Art. 74 | GV.OC-05; DE.AE-02 | Cl. 9.1; Cl. 9.2 | Rule 902(11); Rule 902(13) | SHIPPING |
| `BulkEvidenceExport` | `jurisdiction` | Section 2.3.3 | HybridShield | Art. 74 | GV.OC-05 | Cl. 9.2 | Not directly referenced in monograph | SHIPPING |

### 2.25 Gateway Routing Status

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `GatewayRoutingStatus` | `gatewayId` | Section 2.3 | AlwaysMemory | Art. 9 | ID.AM-03 | Cl. 8.5 | Not directly referenced in monograph | SHIPPING |
| `GatewayRoutingStatus` | `operationalStatus` (enum incl. FAIL_CLOSED_ACTIVE; fail-open not permitted) | Section 2.3 | SacredZero, AlwaysMemory | Art. 9; Art. 14 | DE.CM-09; GV.OC-01 | Cl. 8.4; Cl. 8.5 | Not directly referenced in monograph | SHIPPING |
| `GatewayRoutingStatus` | `failClosedActive` (true when Gateway defaults all decisions to Sacred Zero) | Section 2.3 | SacredZero | Art. 9; Art. 14 | DE.CM-09 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `GatewayRoutingStatus` | `inferenceLaneStatus` | Section 2.3 | AlwaysMemory | Art. 9 | DE.CM-09 | Cl. 8.5 | Not directly referenced in monograph | SHIPPING |
| `GatewayRoutingStatus` | `anchoringLaneStatus` | Section 2.3 | AlwaysMemory | Art. 9 | DE.CM-09 | Cl. 8.5 | Not directly referenced in monograph | SHIPPING |
| `GatewayRoutingStatus` | `activeSacredZeroDecisions` | Section 2.2 | SacredZero | Art. 14 | DE.AE-06 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `GatewayRoutingStatus` | `lanternStatus` | Section 2.4 | GoukassianPromise | Art. 13 | GV.OC-04 | Cl. 5.2 | Not directly referenced in monograph | SHIPPING |

### 2.26 Emergency Override Request

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `EmergencyOverrideRequest` | `overrideRequestId` | Section 13.3 | AlwaysMemory | Art. 9; Art. 14 | RS.MA-01 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `EmergencyOverrideRequest` | `overrideType` (BREAK_GLASS_SHUTDOWN, KILL_SWITCH, FORCED_STATE_TRANSITION) | Section 13.3 | SacredZero, AlwaysMemory, HybridShield | Art. 14 | RS.MA-01; RC.RP-01 | Cl. 8.4; Cl. 10.2 | Not directly referenced in monograph | SHIPPING |
| `EmergencyOverrideRequest` | `supremeAuthorityIdentity` | Section 13.3 | HybridShield | Art. 14 | GV.OC-01 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `EmergencyOverrideRequest` | `justification` (`minLength: 100`; logged before execution; No Log = No Action) | Section 13.3 | AlwaysMemory | Art. 14 | PR.DS-01; RS.MA-01 | Cl. 8.4 | Rule 902(11) | SHIPPING |
| `EmergencyOverrideRequest` | `targetDecisionId` (required when overrideType = FORCED_STATE_TRANSITION; `if/then`) | Section 13.3 | AlwaysMemory | Art. 14 | RS.MA-01 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `EmergencyOverrideRequest` | `forcedState` (`enum: [-1, 0]`; forced transition to +1 not permitted) | Section 13.3 | SacredZero | Art. 14 | RS.MA-01 | Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `EmergencyOverrideRequest` | `custodianQuorumApproval` | Section 2.3.3; Section 13.3 | HybridShield | Art. 9; Art. 14 | GV.OC-01 | Cl. 8.4; Cl. 8.5 | Not directly referenced in monograph | BETA |

---

### 2.27 Tri-Cameral Approval

| Schema (`$defs` key) | Property | Monograph Section | TML Pillar(s) | EU AI Act | NIST RMF | ISO 42001 | FRE 902 | Implementation Status |
|----------------------|----------|-------------------|---------------|-----------|----------|-----------|---------|----------------------|
| `TriCameralApproval` | `technicalCouncilVotes` (`totalMembers: const 9`; proposal rights only) | Section III; Section 7A | HybridShield | Art. 9; Art. 14 | GV.OC-01 | Cl. 5.2; Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `TriCameralApproval` | `technicalCouncilVotes.seatedActiveMembers` (quorum denominator; excludes vacant and quarantined) | Section III; Section 7A | HybridShield | Art. 9 | GV.OC-01 | Cl. 5.2 | Not directly referenced in monograph | SHIPPING |
| `TriCameralApproval` | `stewardshipCustodianVotes` (`totalMembers: const 11`; binding veto authority; no proposal rights) | Section III; Section 7A | HybridShield | Art. 9; Art. 14 | GV.OC-01 | Cl. 5.2; Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `TriCameralApproval` | `stewardshipCustodianVotes.vetoExercised` (binding veto; `true` constitutionally blocks regardless of vote counts) | Section III; Section 7A | HybridShield | Art. 9; Art. 14 | GV.OC-01 | Cl. 5.2; Cl. 8.4 | Rule 902(13) | SHIPPING |
| `TriCameralApproval` | `stewardshipCustodianVotes.seatedActiveMembers` (quorum denominator; excludes vacant and quarantined) | Section III; Section 7A | HybridShield | Art. 9 | GV.OC-01 | Cl. 5.2 | Not directly referenced in monograph | SHIPPING |
| `TriCameralApproval` | `smartContractTreasuryExecution` (`executed`, `transactionHash`; automatic; no admin key; no human override) | Section III | HybridShield | Art. 9 | GV.OC-01 | Cl. 5.2 | Rule 902(13) | SHIPPING |
| `TriCameralApproval` | `quorumAchieved` (`for / seatedActiveMembers >= 0.75` in both chambers) | Section III; Section 7A | HybridShield | Art. 9 | GV.OC-01 | Cl. 5.2 | Not directly referenced in monograph | SHIPPING |
| `TriCameralApproval` | `survivabilityClass` (triggers Section 7A dual-vote protocol, proposer exit, institution ban) | Section 7A | HybridShield | Art. 9; Art. 14 | GV.PO-01 | Cl. 5.2; Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `TriCameralApproval` | `proposerExitConfirmed` (proposer's membership suspended on submission per Section 7A.2) | Section 7A | HybridShield | Art. 14 | GV.PO-01 | Cl. 5.2 | Not directly referenced in monograph | SHIPPING |
| `TriCameralApproval` | `clockStartTimestamp` (180-day window starts at submission regardless of vacancy status) | Section 7A | HybridShield | Art. 9 | GV.PO-01 | Cl. 5.2 | Not directly referenced in monograph | SHIPPING |
| `TriCameralApproval` | `voteNumber` (`enum: [1, 2]`; dual-vote for survivability-class; both at 75% required) | Section 7A | HybridShield | Art. 9; Art. 14 | GV.PO-01 | Cl. 5.2; Cl. 8.4 | Not directly referenced in monograph | SHIPPING |
| `TriCameralApproval` | `institutionBanActive` (proposer's institution banned from filling vacated seat for one year) | Section 7A | HybridShield | Art. 9 | GV.PO-01 | Cl. 5.2 | Not directly referenced in monograph | SHIPPING |
| `TriCameralApproval` | `quarantinedAppointees` (appointees within 90 days of submission quarantined from voting) | Section 7A | HybridShield | Art. 9 | GV.PO-01 | Cl. 5.2 | Not directly referenced in monograph | SHIPPING |
| `EmergencyOverrideRequest` | `triCameralApproval` (required for survivability-class emergency overrides targeting NL=NA chain) | Section III; Section 13.3 | HybridShield | Art. 9; Art. 14 | GV.OC-01; RS.MA-01 | Cl. 8.4; Cl. 8.5 | Not directly referenced in monograph | SHIPPING |

---

## PART 3: Cross-Cutting Compliance Notes

### 3.1 No Log = No Action - Cross-Cutting Enforcement Points

The following artifacts collectively enforce the No Log = No Action iron law. An auditor verifying this principle must confirm all five enforcement layers are intact:

| Layer | Artifact / Location | Enforcement Mechanism | Monograph Section |
|-------|--------------------|-----------------------|-------------------|
| Schema | `StateEnvelope` `if/then` constraint | `permissionToken` required when `currentState == 1` | Section 2.3.3 |
| Schema | `PermissionToken.laneOrigin` | `const: "ANCHORING_LANE"`; rejects all Inference Lane tokens | Section 2.3 |
| Schema | `TSLF-StateP1.permissionToken` | Required field in all Proceed logs | Section 5B.i |
| Schema | `AuditProof.logHash` | Must match `PermissionToken.logHash`; no valid token without anchored log | Section 8 |
| On-chain | `TML_Core.registerPermissionToken` | Reverts with `NoLogNoAction` if `logHash` not in anchored Merkle root | Section 2.3.3 |

| `TriCameralApproval.smartContractTreasuryExecution` | Smart Contract Treasury on-chain execution record for ratified proposals | `tml_abi.json` (`executeTriCameralRatification`) | `tml_schema.json` (`TriCameralApproval`) |
### 3.2 Sacred Zero - Integrity Checkpoints

The following properties are the critical integrity checkpoints for Sacred Zero. An auditor must confirm State 0 is never aliased, substituted, or represented as a null or error:

| Check | Location | Correct Value | Prohibited Values |
|-------|----------|---------------|-------------------|
| State integer | `TriadicStateValue`, `StateEnvelope.currentState`, `TSLF-State0.currentState` | `0` | `null`, `false`, `"HOLD"`, `"TIMEOUT"`, `"ERROR"` |
| State label | `StateEnvelope.stateLabel`, `TSLF-State0.stateLabel` | `"SACRED_ZERO"` | `"SacredPause"`, `"PauseState"`, `"HOLD"` |
| Process identifier | `StateEnvelope.processActive`, `TSLF-State0.processActive` | `"SacredPause"` | Anything used as the state value itself |
| Epistemic Hold | `UncertaintyQuantification.epistemicHoldActive` | `true` (const in State 0 context) | `false` |
| Resolution states | `DeliberationMatrix.resolutionOptions[].proposedState` | `1` or `-1` only | `0` |

### 3.3 Goukassian Promise Artifact Name Integrity

The canonical Goukassian Promise artifact names appear as `const` values in three schema properties. An auditor must confirm these are lowercase strings exactly as shown:

| Artifact | Schema | Property | `const` Value |
|----------|--------|----------|---------------|
| Lantern | `LanternStatus` | `artifactName` | `"lantern"` |
| Signature | `SignatureBlock` | `artifactName` | `"signature"` |
| License | `LicenseValidationRequest` | `artifactName` | `"license"` |

### 3.4 Implementation Gap Summary (FUTURE Items)

All FUTURE-classified items trace to Section 10 (Implementation Gap) of the monograph:

| Feature | Blocking Constraint | Mitigation in SHIPPING Specification | Section 10 Reference |
|---------|--------------------|------------------------------------|----------------------|
| Real-time per-token blockchain anchoring | Throughput asymmetry at global AI scale | Batch Merkle anchoring (`anchoringLogs`, `merkleAnchoringStatus`) | Section 10 |
| Cross-jurisdiction custodian quorum in <500ms | Network physics; geographic distribution | Endpoint SHIPPING; latency field present; sub-500ms not guaranteed | Section 10 |
| PQC signature migration (SLH-DSA-SHAKE-128s, ML-KEM-1024) | Algorithm standardization maturity | ES256 in production; PQC algorithm IDs reserved in `SignatureBlock` and EIP-712 schema | Section 10 |
| Hardware Moral Processing Units (MPUs) | No production MPU silicon | Dual-Lane software architecture specified; MPU not referenced in API surface | Section 10 |
| Immutable ledger with native GDPR Article 17 compliance | Erasure Paradox (immutability vs. right to erasure) | Cryptographic erasure mitigation referenced; feature still FUTURE | Section 10 |
| Full `custodianQuorumAttestation` in every Permission Token | Cross-jurisdiction latency | Field present as optional BETA; not required for SHIPPING token validity | Section 10 |
