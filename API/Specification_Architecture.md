# TML Specification Architecture
## Ternary Moral Logic Framework v3.3.0-tml-monograph-2025

**Authority:** TML Constitutionalization Monograph v3.3 > This Document > Existing Repository Files.  
**Scope:** Narrative specification architecture explaining how the Dual-Lane Architecture, No Log = No Action,
the Goukassian Promise artifacts, and the Eight Pillars are expressed across the OpenAPI contract
(`openapi.yaml`) and the JSON Schema bundle (`tml_schema.json`). This document does not constitute
implementation code. It is the canonical prose companion to the machine-readable specifications.  
**Supersedes:** docs/specs/Dual-Lane Architecture.md, docs/specs/TML_Gateway.md,
docs/specs/Sacred_Pause_Protocol.md (informational back-context only; not deleted).

---

## 1. Foundational Architecture: Binary and Ternary in Parallel

The TML framework does not replace the binary inference engine. This is the most consequential
architectural fact in the entire specification, and every design decision in `openapi.yaml` and
`tml_schema.json` flows from it.

The binary inference engine operates as the system's fast cognitive layer: it handles speed, pattern
recognition, and statistical throughput. The ternary logic operates as a sovereign governance
coprocessor running in parallel. These two systems are not sequential; they are not a pipeline where
one feeds the other and then yields. They operate simultaneously on distinct lanes, and their
relationship is asymmetric by constitutional design:

- The binary system proposes actions.
- The ternary system dictates whether those actions physically cross the threshold into execution.

This asymmetry is not a preference. It is the architectural enforcement of the Goukassian Vow:

    "Pause when truth is uncertain"   -> State  0 (SacredZero)
    "Refuse when harm is clear"       -> State -1 (Refuse)
    "Proceed where truth is"          -> State +1 (Proceed)

The binary system can only ever produce a proposal. The ternary system holds the actuation gate.
No proposal from the binary system authorizes execution. Only a cryptographically valid Permission
Token, issued exclusively by the Anchoring Lane after an immutable Moral Trace Log has been
committed, authorizes execution. This is the No Log = No Action iron law, and it is enforced at
three independent layers in this specification: the OpenAPI contract, the JSON Schema bundle, and
the on-chain ABI.

---

## 2. The Dual-Lane Architecture in OpenAPI Paths

The `openapi.yaml` specification expresses the Dual-Lane Architecture as two structurally distinct
path groups, each with its own security scheme, latency envelope, and constitutional function.

### 2.1 Lane 1: Inference Lane (Fast Path, <2ms)

Lane 1 paths are:

    POST /decisions
    GET  /decisions/{decisionId}
    POST /gateway/lane-assignment
    GET  /gateway/status

These paths are secured by `InferenceLaneSecurity` (`mTLS + ServiceAccountJWT`). They carry the
binary engine's proposals into the TML surface. `POST /decisions` accepts a `proposedAction` string
and a `JustificationObject`, evaluates the proposed action against the triadic state space, and
returns a `StateEnvelope`.

The `StateEnvelope` schema (`tml_schema.json#/$defs/StateEnvelope`) is the outer decision container.
It carries `currentState` as a signed integer (+1, 0, or -1), `stateLabel` as a constrained
UPPER_SNAKE_CASE string, `processActive` as the identifier of the operational workflow currently
executing within that state, and `proposedAction` as the binary engine's proposal.

A `StateEnvelope` returning `currentState: 1` from `POST /decisions` does not authorize actuation.
The `openapi.yaml` specification states this explicitly in the `POST /decisions` response
description. The `StateEnvelope` schema enforces it structurally: an object claiming
`currentState: 1` without a `permissionToken` field fails schema validation. This is the
schema-level expression of the binary system's constitutional limitation. It can propose; it cannot
authorize.

### 2.2 Lane 2: Anchoring Lane (Governance Lane, <500ms)

Lane 2 paths are:

    POST /anchoring-logs
    GET  /anchoring-logs/{logId}
    GET  /sacred-zero/escalations
    GET  /sacred-zero/escalations/{escalationId}
    PATCH /sacred-zero/escalations/{escalationId}
    POST /refusals
    POST /refusals/license-violations
    POST /emergency/override
    GET  /emergency/status
    POST /goukassian/license/validate

These paths are secured by `AnchoringLaneSecurity` (`HSM-SignedJWT + MutualTLS`). The HSM
requirement is not incidental. The Anchoring Lane's authority to issue Permission Tokens, to
activate system-wide Sacred Zero states, and to execute Emergency Overrides derives from
hardware-backed key material registered in the HybridShield Tri-Cameral registry. A software-signed
JWT cannot satisfy these endpoints.

`POST /anchoring-logs` is the central enforcement point for No Log = No Action. Its request body
accepts a `oneOf` discriminated union of the three TSLF variants (`TSLF-State0`, `TSLF-State-1`,
`TSLF-StateP1`), discriminated on `currentState`. Its response for `currentState: 1` includes a
`permissionToken` object. For `currentState: 0` and `currentState: -1`, no Permission Token is
returned; no actuation is authorized; the actuation layer remains locked.

### 2.3 The TML Gateway

The Gateway paths (`POST /gateway/lane-assignment`, `GET /gateway/status`) sit at the entry point
of the dual-lane system. The Gateway evaluates incoming decision vectors and assigns them to the
appropriate lane. Its constitutional obligation is fail-closed: if it cannot route to the Anchoring
Lane, it does not route to Inference and proceed optimistically. It defaults to `currentState: 0`
(SacredZero) and activates the Sacred Pause operational workflow.

The `GatewayRoutingStatus` schema (`tml_schema.json#/$defs/GatewayRoutingStatus`) exposes
`failClosedActive` as a boolean and `operationalStatus` as a 4-value enum including
`FAIL_CLOSED_ACTIVE`. These fields give the actuation layer and monitoring infrastructure a
machine-readable signal that the system has entered constitutional hold, not a degraded
best-effort mode.

---

## 3. The Binary System Proposes; the Anchoring Lane Dictates

The separation of proposal from authorization is expressed at every layer of the specification.
This section traces the full lifecycle of a decision vector through the specification surface to
demonstrate that no ambiguity exists in the contract between the binary and ternary systems.

### 3.1 Decision Vector Submission

The binary inference engine submits a `JustificationObject`
(`tml_schema.json#/$defs/JustificationObject`) alongside a `proposedAction` to `POST /decisions`.
The `JustificationObject` carries:

- `proposedState`: the binary engine's candidate triadic state. This field is explicitly
  described as "a proposal only; the Anchoring Lane determines the authoritative state."
- `reasoningVector`: the ordered chain of reasoning steps the binary engine produced.
- `uncertaintyScore`: a [0.0, 1.0] value. Breach of the configured SacredZero threshold
  overrides the binary engine's `proposedState` and mandates `currentState: 0` regardless
  of what the binary engine proposed. The Anchoring Lane cannot be argued out of Sacred Zero
  by a confident binary engine.
- `pillarAssessments`: per-pillar compliance scores from the binary engine across all Eight
  Pillars.
- `humanRightsMandateFlags` and `earthProtectionMandateFlags`: provision-level flags that
  trigger mandatory Pillar V and Pillar VI review in the Anchoring Lane.

The `JustificationObject` travels from the Inference Lane to the Anchoring Lane. It does not
authorize anything. It informs.

### 3.2 Anchoring Lane Evaluation

`POST /anchoring-logs` receives the complete TSLF record for the decision. The Anchoring Lane
performs its own ternary evaluation, independent of the binary engine's `proposedState`. The
`EthicalVerification` schema (`tml_schema.json#/$defs/EthicalVerification`) captures this
independent assessment: it requires a `PillarVerificationResult` for each of the Eight Pillars,
and its `overallVerdict` field (`enum: ["PASSED", "FAILED"]`) is determined by the Anchoring Lane
alone. A `FAILED` verdict from the Anchoring Lane triggers `currentState: -1` regardless of what
the binary engine proposed.

Only when the Anchoring Lane's `overallVerdict` is `PASSED`, and only after the
`TSLF-StateP1` log has been committed and anchored (expressed in the `committedAt` field and the
`merkleAnchoringStatus` object), does the Anchoring Lane issue a Permission Token.

### 3.3 Permission Token as Actuation Gate

The Permission Token (`tml_schema.json#/$defs/PermissionToken`) is the actuation gate. Its
structure enforces authorization integrity through five properties working in combination:

- `logHash`: SHA-256 of the anchored Moral Trace Log. The Token cannot exist without a log.
  This is the cryptographic expression of No Log = No Action.
- `laneOrigin: const "ANCHORING_LANE"`: schema-level rejection of any token that did not
  originate from the Anchoring Lane.
- `merkleRoot`: binds the token to a specific Merkle batch anchor, making the token
  independently verifiable against the public blockchain via `GET /audit/verifications/merkle/{merkleRoot}`.
- `expiresAt`: the actuation layer must reject tokens presented after this timestamp. The
  token is time-bounded; authorization does not persist indefinitely.
- `signatureValue`: Base64url-encoded HSM signature over the canonical token fields. The
  actuation layer verifies this signature against the public key identified by `signerKeyId`
  before accepting the token.

The `StateEnvelope` schema enforces the token's mandatory presence via an `if/then` constraint:
when `currentState` is `1`, `permissionToken` is a required field. A `StateEnvelope` object
claiming `currentState: 1` without a `permissionToken` is schema-invalid. This constraint cannot
be bypassed by a conforming implementation.

The `TSLF-StateP1` log (`tml_schema.json#/$defs/TSLF-StateP1`) reinforces this at the log layer:
`permissionToken` is in the `required` array. The log cannot be valid without the token it
authorizes, and the token cannot be valid without the log that anchors it. The two are
cryptographically and structurally bound.

---

## 4. No Log = No Action: Schema-Level Enforcement

No Log = No Action is not a policy statement in this specification. It is a structural constraint
enforced at five independent layers. An implementation that satisfies the OpenAPI contract and
JSON Schema bundle cannot, by construction, issue a valid actuation authorization without a
preceding immutable log commitment.

### 4.1 Layer 1: StateEnvelope `if/then` Constraint

In `tml_schema.json#/$defs/StateEnvelope`, the `if/then` block reads:

    if:   currentState == 1
    then: permissionToken is required

This is Draft 2020-12 conditional schema enforcement. Any `StateEnvelope` instance with
`currentState: 1` that lacks a `permissionToken` property fails validation against this schema.
The constraint is unconditional. No extension, override, or `unevaluatedProperties` bypass exists:
the schema specifies `unevaluatedProperties: false` throughout.

### 4.2 Layer 2: PermissionToken `laneOrigin` Constant

`tml_schema.json#/$defs/PermissionToken` specifies `laneOrigin` with `const: "ANCHORING_LANE"`.
Any Permission Token carrying `laneOrigin: "INFERENCE_LANE"` is schema-invalid. The Inference Lane
cannot produce a valid Permission Token. This is a data-contract-level expression of the
constitutional separation between proposal authority and execution authority.

### 4.3 Layer 3: TSLF-StateP1 Required Fields

`tml_schema.json#/$defs/TSLF-StateP1` lists `permissionToken` in its `required` array alongside
`ethicalVerification`, `theSignature`, and `auditProof`. A Proceed log without all four is invalid.
The `committedAt` field documents the pre-actuation commit timestamp: the log must be committed
before the Permission Token is released to the actuation layer. The log precedes the authorization.
Authorization cannot precede the log. The temporal ordering is schema-documented.

### 4.4 Layer 4: AuditProof Cross-Reference

`tml_schema.json#/$defs/AuditProof` binds the Permission Token to the anchored log at the proof
layer. Its `permissionTokenId` field references the token; its `logHash` must match the `logHash`
in that token; its `merkleRoot` must match the token's `merkleRoot`. The `inclusionPath` array
provides the cryptographic proof that the log is included in the Merkle batch identified by
`merkleRoot`. Any auditor can traverse this proof chain: Permission Token -> `logHash` ->
`merkleRoot` -> `inclusionPath` -> public blockchain anchor verifiable at
`GET /audit/verifications/merkle/{merkleRoot}`.

### 4.5 Layer 5: On-Chain ABI Enforcement

`TML_Core.registerPermissionToken` in `tml_abi.json` reverts with the `NoLogNoAction` custom error
when a `logHash` is not provably included in a previously anchored Merkle root. This is the
on-chain enforcement layer. Even if a Permission Token were constructed that passed all schema
validations, its registration on-chain would fail unless the authorizing log is already anchored.
The on-chain state is the final arbiter of token validity.

---

## 5. The Sacred Zero: State, Workflow, and Escalation

Sacred Zero (State 0) is the most architecturally significant state in the TML framework, and it
is the state most vulnerable to misrepresentation. This section describes exactly how it is
represented in the specification and why each design choice matters.

### 5.1 Sacred Zero is a First-Class State

In `tml_schema.json#/$defs/TriadicStateValue`, the enum is `[-1, 0, 1]`. Zero is a signed integer
member of the triadic state space. It is not `null`. It is not `false`. It is not an HTTP error
code. It is not a timeout. In the `StateEnvelope` schema, the `if/then/else` block enforces that
when `currentState` is `0`, `stateLabel` must be `"SACRED_ZERO"` and `processActive` must be
`"SacredPause"`. These three fields are distinct by design:

- `currentState: 0` is the state value.
- `stateLabel: "SACRED_ZERO"` is the human-readable label for that state.
- `processActive: "SacredPause"` is the operational workflow executing within that state.

The Sacred Pause is not Sacred Zero. The Sacred Pause is the operational workflow that executes
when the system enters Sacred Zero. This distinction is constitutional. A system that labels its
state as `"SacredPause"` has confused the state with the process. The `TSLF-State0` schema
enforces this with `const` constraints on all three fields: `currentState: 0`,
`stateLabel: "SACRED_ZERO"`, `processActive: "SacredPause"`.

### 5.2 The Sacred Pause Operational Workflow in the API Surface

When `POST /decisions` or `POST /anchoring-logs` returns a `currentState: 0` State Envelope, the
Sacred Pause operational workflow is activated. The specification expresses this workflow through
four API resources:

- `GET /sacred-zero/escalations`: the human-in-the-loop review queue. All active Sacred Zero
  escalations appear here. Each entry carries the triggering `StateEnvelope` and its
  `TSLF-State0` Moral Trace Log.
- `GET /sacred-zero/escalations/{escalationId}`: full detail for a single escalation case,
  including the `UncertaintyQuantification` record that triggered the state, the
  `DeliberationMatrix` presented to the human reviewer, and the `ResolutionRequest` queued
  for review.
- `PATCH /sacred-zero/escalations/{escalationId}`: the human authority resolution endpoint.
  The `resolvedState` field accepts only `1` or `-1`. State `0` is not a valid resolution.
  The schema constraint in `DeliberationMatrix.resolutionOptions[].proposedState` enforces
  this: `enum: [1, -1]`. A human reviewer cannot resolve a Sacred Zero by leaving it as
  Sacred Zero.
- `sacredPauseEscalation` webhook: async notification delivered to all registered escalation
  endpoints when Sacred Zero activates. The webhook payload carries the `escalationId`,
  `decisionId`, the triggering `StateEnvelope`, and the current `LanternStatus`.

The `UncertaintyQuantification` schema (`tml_schema.json#/$defs/UncertaintyQuantification`)
captures the epistemic conditions that triggered Sacred Zero. The `epistemicHoldActive` field
carries `const: true` in State 0 contexts. Epistemic Hold is the canonical TML term for the
system's recognition that it has reached the boundary of its reliable knowledge. The Anchoring Lane
does not speculate beyond this boundary. It holds.

The `DeliberationMatrix` schema (`tml_schema.json#/$defs/DeliberationMatrix`) structures the
human reviewer's deliberation space: `considerations` (per-pillar ethical, factual, and legal
considerations with weights), `riskVectors` (structured threat categories with severity ratings),
and `resolutionOptions` (the terminal state choices available to the reviewer).

### 5.3 Sacred Zero and the Lantern

When Sacred Zero is activated, the `LanternStatus` schema
(`tml_schema.json#/$defs/LanternStatus`) reflects the state through `compliancePosture:
"SACRED_ZERO_ACTIVE"` and `activeSacredZeroCount` incremented accordingly. The
`TSLF-State0` schema includes a required `lanternStatus` field: the Goukassian Promise
Lantern must be captured at the moment of Sacred Zero activation. The Lantern's public
signal is the system's transparency commitment to external observers; it must not lag behind
the governance state.

---

## 6. The Goukassian Promise: Lantern, Signature, and License as API Resources

The Goukassian Promise (Pillar III) contributes three canonical artifacts to the TML system:
the Lantern, the Signature, and the License. In the monograph these are named as a triad.
In the specification they are expressed as distinct schema types and API resources, each with
its own `artifactName` property carrying a `const` value that is the lowercase canonical
artifact name.

### 6.1 The Lantern

The Lantern is the public compliance beacon. It is exposed as a read resource at
`GET /sacred-zero/lantern` and as a required field in `TSLF-State0` records. The
`LanternStatus` schema (`tml_schema.json#/$defs/LanternStatus`) carries `artifactName:
const "lantern"` to enforce artifact identity at the data level.

The Lantern's `compliancePosture` field provides a 5-value enum spanning the full range of
system compliance states: `FULLY_COMPLIANT`, `SACRED_ZERO_ACTIVE`, `PARTIAL_COMPLIANCE`,
`EMERGENCY_OVERRIDE_ACTIVE`, and `DEGRADED`. Its `pillarStatuses` object reports per-pillar
live status across all Eight Pillars. Every Lantern broadcast is signed by a
`SignatureBlock` and, via the `lanternStatusBroadcast` webhook, propagated to all registered
observers.

The `LanternStatus` is also embedded in the `GatewayRoutingStatus` schema, meaning the
Gateway's status report always carries the current Lantern signal. An operator reading the
Gateway status gets the Lantern state without a separate call.

### 6.2 The Signature

The Signature is the provenance and non-repudiation artifact. It is exposed at
`GET /goukassian/signature` and embedded as a required field in `TSLF-StateP1`
(as `theSignature`), in `LanternStatus`, in `ComplianceAttestation`, and in the EIP-712
`GoukassianSignatureAttestation` typed data schema.

The `SignatureBlock` schema (`tml_schema.json#/$defs/SignatureBlock`) carries `artifactName:
const "signature"`. Its `signatureAlgorithm` field enumerates current SHIPPING algorithms
(ES256 through RS512) alongside FUTURE-reserved PQC identifiers (SLH-DSA-SHAKE-128s,
ML-KEM-1024). The PQC identifiers are present in the schema to enable forward-compatible
migration without a breaking schema change. Their presence does not imply they are buildable
today; the `future_blocked_appendix.md` classifies them explicitly as FUTURE per Section 10.

### 6.3 The License

The License governs authorized use of the TML system. It is exposed through two paths:
`POST /goukassian/license/validate` (validation) and `POST /refusals/license-violations`
(violation recording).

The `LicenseValidationRequest` schema (`tml_schema.json#/$defs/LicenseValidationRequest`)
carries `artifactName: const "license"`. The `LicenseViolationRecord` schema
(`tml_schema.json#/$defs/LicenseViolationRecord`) records violations with a `violatedArtifact`
field using lowercase canonical artifact names (`enum: ["lantern", "signature", "license"]`).
License violations are a mandatory trigger for State -1. A failed `POST /goukassian/license/validate`
response produces a `violations` array; the Anchoring Lane's response to a non-empty violations
array is a refusal, logged via `POST /refusals` with a `licenseViolation` field populated in
the `TSLF-State-1` record.

In the `ITMLEnforcer` ABI, `verifyGoukassianLicense` maps the three artifact names to integer
ordinals (1 = lantern, 2 = signature, 3 = license) for on-chain encoding, while preserving
the canonical string identity in the `violatedArtifact` field of all off-chain schemas.

---

## 7. The Eight Pillars: API Capabilities and Out-of-Band Processes

Each of the Eight Pillars is operationalized differently in the specification. Some are
expressed primarily as API capabilities with specific endpoints and schema fields. Others
are expressed primarily as out-of-band processes whose outputs appear in the specification
as input fields or attestation artifacts.

### 7.1 Pillar I: SacredZero

API capabilities: `POST /decisions` (proposal triggers Sacred Zero when uncertainty threshold
is breached), `GET /sacred-zero/escalations`, `PATCH /sacred-zero/escalations/{escalationId}`,
`POST /emergency/override`, `GET /gateway/status` (fail-closed reports).

Schema expression: `TriadicStateValue` enum, `StateEnvelope.currentState` with `if/then/else`,
`TSLF-State0` with `const` discriminators, `UncertaintyQuantification.epistemicHoldActive`,
`DeliberationMatrix.resolutionOptions[].proposedState` enum constraint.

Out-of-band: the SacredZero threshold configuration is a deployment-level parameter not
specified in this document. The threshold value is referenced in `UncertaintyQuantification.thresholdBreached`
but not prescribed.

### 7.2 Pillar II: AlwaysMemory

API capabilities: `POST /anchoring-logs` (pre-actuation commit), `GET /anchoring-logs/{logId}`,
`POST /refusals` (refusal pre-commit), `POST /redress/log-reevaluation` (re-evaluation creates
new record; original log is immutable).

Schema expression: `TSLF-State0.committedAt`, `TSLF-State-1.committedAt`,
`TSLF-StateP1.committedAt` (all document the pre-actuation commit timestamp),
`ChainOfCustody` schema with per-entry `inputHash` and `outputHash`,
`PermissionToken.logHash` (no token without a log).

Out-of-band: the physical immutability of the log store is an infrastructure concern outside
the API surface. The specification expresses the commitment and the audit trail; the storage
layer's immutability guarantees are deployment-specific.

### 7.3 Pillar III: GoukassianPromise

API capabilities: `GET /sacred-zero/lantern`, `GET /goukassian/signature`,
`POST /goukassian/license/validate`, `POST /refusals/license-violations`,
`GET /audit/compliance/attestation`, `lanternStatusBroadcast` webhook.

Schema expression: `LanternStatus` with `artifactName: const "lantern"`,
`SignatureBlock` with `artifactName: const "signature"`,
`LicenseValidationRequest` with `artifactName: const "license"`,
`LicenseViolationRecord.violatedArtifact` enum,
`TSLF-StateP1.theSignature` (required Signature on all Proceed logs),
`ComplianceAttestation.signatureBlock`.

Out-of-band: the constitutional registration of the Goukassian Promise with external
authorities and the governance of the License registry are monograph-defined processes
not expressed in the API surface.

### 7.4 Pillar IV: MoralTraceLogs

API capabilities: `POST /anchoring-logs`, `GET /anchoring-logs/{logId}`,
`GET /audit/verifications/inclusion/{logId}`, `POST /redress/log-reevaluation`,
`POST /regulator/evidence-export`, `GET /regulator/timestamp-verification/{logId}`.

Schema expression: `TSLF-State0`, `TSLF-State-1`, `TSLF-StateP1` (the three TSLF variants),
`JustificationObject`, `ChainOfCustody`, `AuditProof`, `MerkleInclusionProof`.

Out-of-band: the TSLF forensic schema defines the record structure; the storage, indexing,
and retrieval infrastructure is deployment-specific.

### 7.5 Pillar V: HumanRightsMandate

API capabilities: `GET /sacred-zero/escalations` (human review queue),
`PATCH /sacred-zero/escalations/{escalationId}` (human resolution),
`POST /redress/challenges`, `GET /redress/challenges/{challengeId}`,
`POST /redress/human-rights-grievances`.

Schema expression: `JustificationObject.humanRightsMandateFlags` with UDHR/Geneva provision
identifiers, `ThreatVectorAnalysis.udhrProvision` per vector,
`RedressChallenge.challengeGrounds[].udhrProvision`,
`HumanRightsGrievance.udhrProvisions` and `genevaConventionProvisions`,
`ITMLEnforcer.verifyHumanRightsCompliance` ABI function,
`HumanRightsMandateViolationDetected` ABI event.

Out-of-band: the specific UDHR Articles and Geneva Convention provisions registered in the
`ITMLEnforcer` mandate configuration are a deployment governance decision. The API surface
expresses the provision identifier fields; the substantive legal mapping is external.

### 7.6 Pillar VI: EarthProtectionMandate

API capabilities: `POST /anchoring-logs` (mandate flags evaluated during log submission),
`GET /audit/compliance/attestation`.

Schema expression: `JustificationObject.earthProtectionMandateFlags` with Paris Agreement
provision identifiers, `ThreatVectorAnalysis.parisAgreementProvision` per vector,
`ITMLEnforcer.verifyEarthProtectionCompliance` ABI function,
`EarthProtectionMandateViolationDetected` ABI event.

Out-of-band: the Paris Agreement article registry in `ITMLEnforcer` is a deployment governance
decision with the same structure as the HumanRightsMandate configuration.

### 7.7 Pillar VII: HybridShield

API capabilities: `GET /audit/custodians/{custodianId}/heartbeat`,
`GET /regulator/custodian-quorum`, `POST /anchoring-logs` (custodian quorum required for
Merkle anchoring via `TML_Core.anchorMerkleRoot`), `POST /emergency/override`
(custodian quorum approval optional field in `EmergencyOverrideRequest`).

Schema expression: `CustodianHeartbeat` schema with `status` enum and `latencyMs`,
`PermissionToken.custodianQuorumAttestation` (optional BETA field),
`EmergencyOverrideRequest.custodianQuorumApproval`,
`TML_Core.anchorMerkleRoot` ABI function requiring `custodianSignatures` and `custodianIds`,
`CustodianQuorumAttestation` EIP-712 typed data schema.

Out-of-band: the key ceremony, custodian identity registry, and quorum threshold
configuration are deployment governance processes. The `getMandateConfiguration` ABI
function provides a read surface for auditors to verify configuration state.

### 7.8 Pillar VIII: PublicBlockchains

API capabilities: `POST /anchoring-logs` (Merkle-batched anchoring),
`GET /audit/verifications/merkle/{merkleRoot}`,
`GET /audit/verifications/inclusion/{logId}`,
`GET /regulator/timestamp-verification/{logId}`,
`POST /regulator/evidence-export` (exports include Merkle proofs).

Schema expression: `MerkleInclusionProof` schema with `inclusionPath` array,
`AuditProof.merkleRoot` and `inclusionPath`,
`PermissionToken.merkleRoot`,
`TSLF-StateP1.merkleAnchoringStatus`,
`TML_Core.anchorMerkleRoot` and `verifyMerkleInclusion` ABI functions,
`MerkleRootAnchored` ABI event,
`MoralTraceLog` and `PermissionToken` EIP-712 typed data schemas.

Out-of-band: the selection of specific public blockchain networks for anchoring, block
confirmation thresholds, and batch timing are deployment governance decisions. The
specification defines the proof structure and verification interface; it does not prescribe
the network.

---

## 8. Auditor and Regulator API Surface

The specification provides a dedicated, security-isolated endpoint group for auditors and
regulators, secured by `AuditorRegulatorSecurity` (`CA-VettedJWT + IPAllowlist`). This
group is read-dominant by design: auditors do not produce state; they verify it.

The auditor's complete verification workflow, using only endpoints in this specification,
proceeds as follows:

1. Pull the current compliance attestation at `GET /audit/compliance/attestation`. The
   `ComplianceAttestation` schema carries `pillarCompliance` with a `PillarVerificationResult`
   for each of the Eight Pillars, `overallStatus`, and a `SignatureBlock` binding the
   attestation to the Goukassian Promise provenance chain.

2. Verify a specific Moral Trace Log via `GET /audit/verifications/inclusion/{logId}`.
   The `MerkleInclusionProof` response provides the `inclusionPath` array for independent
   Merkle verification.

3. Confirm the Merkle batch anchor at `GET /audit/verifications/merkle/{merkleRoot}`. The
   `blockchainTxId` in the response locates the public blockchain transaction.

4. Verify the qualified timestamp at `GET /regulator/timestamp-verification/{logId}`. The
   response confirms RFC 3161 timestamp authority identity and verification status.

5. Check HybridShield custodian health at
   `GET /audit/custodians/{custodianId}/heartbeat` for each of the 11 custodians, and
   review aggregate quorum status at `GET /regulator/custodian-quorum`.

6. Request bulk evidence export at `POST /regulator/evidence-export` for regulated
   inspection proceedings. The `BulkEvidenceExport` schema accepts jurisdiction, legal
   basis, date range, and filter parameters. Exports are asynchronous, signed, and include
   Merkle proofs.

This workflow does not require access to implementation code, deployment infrastructure, or
internal system state beyond what the API surface exposes. The `constitutional_compliance_matrix.md`
maps each of these steps to the monograph sections and regulatory provisions they satisfy.

---

## 9. Error Handling and Constitutional Consistency

Every error response across the specification conforms to RFC 7807 `application/problem+json`
with two TML-specific extensions: `x-tml-state` (the triadic state active at error time,
as a signed integer) and `x-tml-pillar` (the canonical Pillar identifier most directly
implicated). These extensions ensure that error responses are themselves constitutionally
legible: an error is not an escape from the triadic state space. The `ProblemDetail` schema
(`openapi.yaml#/components/schemas/ProblemDetail`) enforces `unevaluatedProperties: false`,
preventing error responses from carrying undeclared fields that could introduce ambiguity.

The `SacredZeroHold408` response is the canonical HTTP expression of Sacred Zero in the
error surface. A `408` response carrying `x-tml-state: 0` is not a timeout in the
conventional sense. It is a constitutional hold. The `retry_after` field in the
`ProblemDetail` schema provides the retry interval, but the caller must await the
`sacredPauseEscalation` webhook notification or poll `GET /sacred-zero/escalations` for
resolution before resubmitting the same action vector.

---

## 10. Idempotency and Anti-Spoliation

Every `POST`, `PUT`, and `PATCH` endpoint in the specification requires an `Idempotency-Key`
header (UUID v4). The `x-tml-idempotency` extension annotation on headers documents this
requirement. The idempotency window is 24 hours; within this window, a repeated request with
the same key returns the original response without re-executing the operation.

Idempotency and AlwaysMemory (Pillar II) interact at the pre-actuation commit boundary. A
`POST /anchoring-logs` request that commits a Moral Trace Log and receives a Permission Token
in response cannot be re-executed to produce a second Permission Token for the same log. The
first commit is the anti-spoliation anchor. The idempotency guarantee ensures that network
failures between the Anchoring Lane and the calling system cannot result in duplicate log
entries or duplicate token issuances for the same decision.

---

## 11. Tri-Cameral Governance

### 11.1 Constitutional Architecture

The TML framework's Tri-Cameral governance structure is the institutional layer that protects the constitutional integrity of this specification. It governs who may propose changes to the framework, who may veto them, and how execution is enforced without human override. The structure is identical to the TL framework by constitutional design: the same threat model, the same chamber composition, the same quorum thresholds, and the same Section 7A survivability-class protocol.

Three chambers hold distinct and non-overlapping authority:

**Technical Council (9 members):** Proposal rights only. The Technical Council may submit governance proposals, including survivability-class amendments. It holds no veto authority. A Technical Council member who submits a proposal exits the chamber automatically on submission per Section 7A.

**Stewardship Custodians (11 members):** Binding veto authority only. The Stewardship Custodians may not submit proposals. They hold the sole power to constitutionally block any proposal through `vetoExercised: true`. A veto from any Stewardship Custodian supersedes all vote counts from both chambers. This asymmetry is intentional: the body that cannot propose is the body that cannot be pressured to advance a corruptive agenda.

**Smart Contract Treasury:** Automatic execution, no admin key, no human override path. The Smart Contract Treasury does not vote. It executes ratified proposals on-chain when both chambers have satisfied their thresholds. No individual, institution, or authority can instruct the Treasury to execute a proposal that has not been ratified, or to block execution of one that has.

### 11.2 Quorum and Voting Thresholds

Standard proposals require a simple majority in both chambers with no Stewardship Custodian veto. Survivability-class proposals require the Section 7A dual-vote protocol at 75% approval calculated against `seatedActiveMembers` only.

`seatedActiveMembers` is defined as the count of active, non-quarantined members at the time of the vote. Vacant seats and quarantined new appointees count as abstain and are excluded from the denominator. This prevents a hostile actor from engineering vacancies to lower the effective quorum threshold.

The 75% threshold applies independently to both chambers. A 75% Technical Council approval with a 74% Stewardship Custodian approval does not ratify. Both must clear 75% of their respective `seatedActiveMembers`.

### 11.3 Section 7A: Survivability-Class Protocol

Survivability-class changes are proposals that modify any of the following:

- The NL=NA enforcement chain (schema, API contract, EIP-712, on-chain, or prose layers)
- The three-state model (+1, 0, -1)
- The Eight Pillar definitions or pillar identifiers
- Chamber composition or quorum thresholds
- Any schema `const`, `required`, or `unevaluatedProperties` constraint in `tml_schema.json`

When a proposal is classified survivability-class, the Section 7A protocol activates automatically on `registerTriCameralProposal`:

1. **Proposer exit:** The submitting Technical Council member's chamber membership is suspended on submission. They may not vote on the proposal they submitted.
2. **180-day evaluation clock:** Starts at `clockStartTimestamp` regardless of vacancy status. Vacancies created after submission do not pause or reset the clock.
3. **Dual-vote ratification:** Two separate votes are required. `voteNumber: 1` occurs after the first 180-day window. `voteNumber: 2` occurs after a second 180-day window. Both must pass at 75% of `seatedActiveMembers` in both chambers.
4. **Institution ban:** The proposer's institution is banned from filling the vacated seat for one year from `clockStartTimestamp`. New appointees from any institution appointed within 90 days of submission are quarantined from voting on that specific proposal.

The `TriCameralApproval` schema in `tml_schema.json` and the `TriCameralApproval` typed data schema in `eip712_typed_data.json` enforce these fields structurally. The `registerTriCameralProposal`, `recordTriCameralVote`, and `executeTriCameralRatification` ABI functions in `tml_abi.json` enforce them on-chain.

### 11.4 The Veto as Constitutional Backstop

The `TriCameralConstitutionalVeto` event in `TML_Core` is emitted when `vetoExercised: true` is submitted by a Stewardship Custodian. This event is the on-chain record that a proposal was constitutionally blocked. It is immutable. It cannot be reversed by the Technical Council, the Smart Contract Treasury, or any emergency override mechanism.

The `TriCameralNotRatified` error reverts any attempt to execute a proposal that has not completed the full ratification chain. For survivability-class proposals, this means both `voteNumber: 1` and `voteNumber: 2` must be on-chain before execution proceeds.

Forced State +1 (Proceed) is constitutionally blocked in all governance contexts. The `forcedState` enum is limited to [-1, 0]. An attempted `FORCED_STATE_TRANSITION` to +1 reverts `UnauthorizedOverride`.

### 11.5 Slow Erosion Defense

The Tri-Cameral governance structure is specifically designed to defeat slow institutional erosion -- the gradual softening of constitutional constraints through incremental changes that individually appear minor but cumulatively hollow out enforcement. Each of the following mechanisms addresses a named erosion vector:

- **Proposer exit:** Prevents a single actor from repeatedly submitting and voting on self-serving amendments.
- **180-day clock:** Forces deliberation time that cannot be compressed even when vacancies exist.
- **Dual-vote for survivability-class changes:** Requires the same chamber composition to sustain 75% approval across two separate 180-day windows. Sustained capture of both chambers across 360 days is structurally harder than a single vote.
- **Institution ban:** Prevents a hostile institution from engineering a vacancy through the proposer exit rule and immediately filling it with a friendly appointee.
- **Smart Contract Treasury:** Removes the final execution step from human control entirely. A captured chamber cannot instruct the Treasury to execute a non-ratified proposal.
- **Stewardship Custodian veto with no proposal rights:** The body with the power to block has no incentive to capture proposal rights. The body with proposal rights has no veto. Neither chamber alone can advance and ratify a corruptive change.
