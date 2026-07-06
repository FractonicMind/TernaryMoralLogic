# Future and Blocked Features Appendix
## TML Specification Architecture v3.3.0-tml-monograph-2025

**Authority:** TML Constitutionalization Monograph v3.3, Section 10 (Implementation Gap).  
**Purpose:** Explicit catalog of architectural targets that are constitutionally desirable but
not shipping specifications due to named constraints in Section 10. Every feature listed here
is referenced in the specification artifacts with a `x-tml-implementation-status: FUTURE`
annotation or a `FUTURE` note in the Constitutional Compliance Matrix. No endpoint or schema
claims to implement any feature listed in this appendix.

**Classification rule:** A feature is FUTURE when it is blocked by a named constraint from
Section 10. A feature is BETA when buildable with documented tradeoffs. A feature is SHIPPING
when buildable with 2025 production libraries and infrastructure with no known Section 10
blockers. This appendix covers FUTURE only.

---

## Feature 1: Real-Time Per-Token Blockchain Anchoring

### Architectural Target

Every Permission Token issued by the Anchoring Lane is anchored individually and in real time
to a public blockchain, producing a per-token blockchain transaction ID available within the
<500ms Anchoring Lane latency envelope.

### Blocking Constraint (Section 10: Implementation Gap)

Throughput asymmetry at global AI scale. Public blockchain throughput is measured in tens to
hundreds of transactions per second for finalized writes. A TML deployment processing millions
of decisions per day would require millions of per-token blockchain writes per day. No public
blockchain in production as of the monograph version provides the throughput, finality speed,
and cost profile required to anchor every token individually within the <500ms Anchoring Lane
latency budget.

### What Remains Unbuildable

A single-token-to-single-blockchain-transaction binding at Anchoring Lane throughput. The
<500ms latency envelope and the per-token granularity requirement cannot be simultaneously
satisfied with any 2025 production public blockchain.

### Shipping Mitigation

Merkle-batched anchoring. The Anchoring Lane accumulates Moral Trace Logs into batches,
computes a Merkle root over the batch, and anchors the root as a single blockchain transaction.
Individual log inclusion is then provable via the `MerkleInclusionProof` schema
(`tml_schema.json#/$defs/MerkleInclusionProof`) using the `inclusionPath` array. The
Permission Token carries `merkleRoot` (the batch root) rather than a per-token blockchain
transaction ID.

This mitigation is expressed throughout the specification:

- `POST /anchoring-logs` response includes an `anchoring` object with `merkleRoot`,
  `batchId`, and `estimatedFinalizationAt`. The field name `estimatedFinalizationAt`
  explicitly signals that finalization is deferred.
- `GET /audit/verifications/merkle/{merkleRoot}` verifies the batch root.
- `GET /audit/verifications/inclusion/{logId}` proves per-log inclusion in the batch.
- `TML_Core.anchorMerkleRoot` in `tml_abi.json` anchors batch roots, not per-token records.
- The `POST /anchoring-logs` operation description explicitly states: "real-time per-token
  anchoring at global AI scale is classified FUTURE per Section 10."

### Remaining Gap After Mitigation

Batch anchoring introduces a finalization lag between log commitment and public blockchain
confirmation. During this lag, the `merkleAnchoringStatus.anchoredAt` field in TSLF records
and `MerkleInclusionProof.verificationStatus` may report `PENDING`. The Permission Token is
valid for actuation authorization before batch finalization completes, because the token's
validity is bound to the Anchoring Lane's HSM signature, not to blockchain confirmation. The
forensic auditability is complete only after batch finalization. This lag is architectural,
not a defect.

---

## Feature 2: Post-Quantum Cryptography (PQC) Signature Migration

### Architectural Target

All TML cryptographic signatures, including Permission Token signatures, Goukassian Promise
Signature Block values, HybridShield custodian signatures, and EIP-712 signed structures,
use post-quantum cryptographic algorithms (specifically SLH-DSA-SHAKE-128s for signing and
ML-KEM-1024 for key encapsulation) that are secure against adversaries with access to
large-scale quantum computing.

### Blocking Constraint (Section 10: Implementation Gap)

Algorithm standardization maturity and HSM production availability. As of the monograph
version, NIST FIPS 204 (ML-DSA) and FIPS 205 (SLH-DSA) are finalized standards, but HSM
vendors have not uniformly shipped production firmware supporting these algorithms. The
EIP-712 typed data ecosystem and the broader Ethereum toolchain have not standardized PQC
signature verification on-chain. Migration requires simultaneous readiness across HSM
firmware, smart contract verifiers, and client SDK layers.

### What Remains Unbuildable

A fully PQC-secured TML deployment in which every signature-producing operation uses
SLH-DSA-SHAKE-128s or ML-KEM-1024 and every signature-verifying operation, including
on-chain ABI verification in `TML_Core`, can verify PQC signatures. The on-chain
verification gap is the hardest constraint: no production EVM supports PQC precompiles
as of the monograph version.

### Shipping Mitigation

ECDSA (ES256, ES384, ES512) and RSA (RS256, RS384, RS512) signatures are the SHIPPING
algorithms. The specification reserves PQC algorithm identifiers in all relevant schema
fields to enable forward-compatible migration without breaking schema changes:

- `SignatureBlock.signatureAlgorithm` (`tml_schema.json#/$defs/SignatureBlock`) includes
  `"SLH-DSA-SHAKE-128s"` and `"ML-KEM-1024"` in its enum. These values are schema-valid
  but operationally FUTURE.
- `GoukassianSignatureAttestation` in `eip712_typed_data.json` includes
  `signatureAlgorithmId` values `6` (SLH-DSA-SHAKE-128s) and `7` (ML-KEM-1024) in its
  description, reserved for PQC migration.
- The `implementationNotes.pqcMigration` field in `eip712_typed_data.json` explicitly
  labels these as FUTURE.

### Remaining Gap After Mitigation

ECDSA P-256 is considered computationally secure against classical adversaries. It is not
secure against a sufficiently powerful quantum adversary running Shor's algorithm. Until HSM
vendors and EVM toolchains support PQC algorithms in production, the cryptographic
non-repudiation chain (Permission Token signatures, Signature Block values, custodian
quorum signatures) retains a long-term quantum vulnerability. The mitigation reserves the
migration path; it does not close the vulnerability.

---

## Feature 3: Hardware Moral Processing Units (MPUs)

### Architectural Target

Dedicated silicon implementing the ternary logic governance coprocessor as a hardware Moral
Processing Unit, physically enforcing the separation between the binary inference engine and
the ternary governance layer at the instruction execution level. An MPU would enforce No Log =
No Action in hardware: the actuation bus would be physically gated by a hardware signal from
the MPU, making software bypass architecturally impossible rather than merely contractually
prohibited.

### Blocking Constraint (Section 10: Implementation Gap)

No production MPU silicon exists. The hardware design space for ternary logic processing
units is an active research area, but no commercially available MPU implementing TML's
constitutional enforcement model has been fabricated, tested, or qualified for production
deployment as of the monograph version.

### What Remains Unbuildable

The actuation bus hardware gate. In the absence of MPU silicon, No Log = No Action is
enforced through software contracts (the `StateEnvelope` schema constraint), cryptographic
verification (the Permission Token signature and Merkle proof chain), and on-chain ABI
reversion (the `NoLogNoAction` custom error in `TML_Core`). These are strong enforcement
mechanisms, but they do not provide the physical impossibility guarantee that hardware
gating would.

### Shipping Mitigation

The Dual-Lane software architecture specified in `openapi.yaml` is the SHIPPING expression
of the MPU concept. The Inference Lane (`POST /decisions`) and Anchoring Lane
(`POST /anchoring-logs`) are architecturally separated at the API surface, security scheme
level (`InferenceLaneSecurity` vs `AnchoringLaneSecurity`), and schema level
(`PermissionToken.laneOrigin: const "ANCHORING_LANE"`). The `GatewayRoutingStatus` schema
and `GET /gateway/status` endpoint expose the Gateway's constitutional routing state.

### Remaining Gap After Mitigation

Software enforcement requires a trusted execution environment and a conforming implementation.
A non-conforming implementation can bypass software constraints in ways that hardware gating
would prevent. The constitutional compliance matrix and the auditor verification workflow
(`GET /audit/compliance/attestation`, `GET /audit/verifications/inclusion/{logId}`) provide
detection capability for non-conforming behavior after the fact, but not prevention at the
execution level.

---

## Feature 4: Cross-Jurisdiction Custodian Quorum in Sub-500ms

### Architectural Target

The HybridShield Tri-Cameral distributed anchoring achieves a cryptographic quorum across
all eleven custodians, operating in geographically distributed jurisdictions, within the
Anchoring Lane's <500ms latency budget. This would mean that every Permission Token is
backed by a fully distributed, cross-jurisdictional custodian quorum completed before the
token is issued.

### Blocking Constraint (Section 10: Implementation Gap)

Network physics. The speed of light imposes a minimum round-trip latency between
geographically distant custodian nodes. A custodian in Western Europe and a custodian in
East Asia have a minimum round-trip network latency of approximately 200-300ms under ideal
conditions. A all seated custodians or even 75% supermajority synchronous quorum across genuinely cross-jurisdictional
custodian nodes cannot reliably complete within 500ms given routing overhead, cryptographic
signing time, and network jitter.

### What Remains Unbuildable

Synchronous cross-jurisdiction full quorum within the <500ms Anchoring Lane latency envelope.
The physics constraint is absolute: no software optimization closes the gap imposed by the
geographic distribution requirement.

### Shipping Mitigation

Two mitigations are specified:

First, regionally co-located custodian subsets can achieve sub-500ms quorum within a single
geographic region. The Tri-Cameral architecture accommodates partial quorum configurations
where the required threshold is met by a locally available subset. The
`GET /regulator/custodian-quorum` endpoint reports both `activeCustodianCount` and
`crossJurisdictionLatencyMs`, allowing operators to monitor the gap between the local quorum
and the full cross-jurisdictional target.

Second, the `PermissionToken.custodianQuorumAttestation` field in
`tml_schema.json#/$defs/PermissionToken` is optional and classified BETA. A token is valid
without this field. When the field is present, it documents the quorum state at token
issuance. The attestation field reserves the structural position for when full cross-
jurisdictional quorum within latency becomes achievable.

The `CustodianQuorumAttestation` EIP-712 typed data schema in `eip712_typed_data.json`
provides the signing structure for custodian attestations when they are produced.

### Remaining Gap After Mitigation

The `x-tml-blocking-constraint` annotation on `GET /regulator/custodian-quorum` in
`openapi.yaml` documents this explicitly: "Section 10: Cross-jurisdiction sub-500ms quorum
remains FUTURE." A deployment claiming full HybridShield constitutional compliance requires
acknowledging that the cross-jurisdiction latency target is aspirational until network
infrastructure evolution or architectural changes (such as asynchronous quorum with
deferred finality) make it achievable.

---

## Feature 5: Immutable Ledger with Native GDPR Article 17 Compliance

### Architectural Target

The Moral Trace Log store is simultaneously:

(a) Cryptographically immutable: once committed, no log entry can be modified or deleted,
    with immutability provable via the Merkle inclusion chain.
(b) Natively GDPR Article 17 compliant: any individual can exercise their right to erasure,
    and the system can demonstrate that their personal data has been erased from the log store.

These two properties are in direct architectural contradiction. Immutability means no
deletion. Article 17 means the right to deletion. This is the Erasure Paradox.

### Blocking Constraint (Section 10: Implementation Gap)

The Erasure Paradox. A log store that is genuinely immutable cannot natively satisfy Article
17 erasure requests. A log store that can delete records cannot provide the immutability
guarantee that AlwaysMemory (Pillar II) and the forensic integrity of the TSLF require.
No data architecture as of the monograph version resolves this contradiction natively.

### What Remains Unbuildable

A single log store architecture that is both cryptographically immutable and natively capable
of demonstrating per-record erasure to a data subject or supervisory authority.

### Mitigation: Cryptographic Erasure

The monograph proposes cryptographic erasure as the mitigation, and this specification
reflects its status as a mitigation, not a solution.

The cryptographic erasure approach encrypts personal data in each log entry with a per-record
key (or a key derived from a per-subject key hierarchy, such as HKDF-SHA3-256). The key is
held in a separate erasure key registry. When an Article 17 erasure request is received,
the erasure key for the relevant records is destroyed. Without the key, the encrypted
personal data in the log entry is computationally inaccessible, providing practical erasure
without modifying the ciphertext record in the immutable log.

The `SHA256Hex` schema primitive and the `PermissionToken.logHash` binding accommodate this
architecture: the Merkle inclusion proof verifies the ciphertext record's integrity, and the
destroyed key provides the practical erasure guarantee. This approach is consistent with
ENISA guidance on pseudonymization and with interpretations of Article 17 that accept
cryptographic inaccessibility as equivalent to deletion for computationally bounded adversaries.

This mitigation is documented in the Cryptographic Erasure folder of the TernaryLogic
repository (HKDF-SHA3-256 key hierarchy, NuSMV LTL verification, NIST CAVP vectors,
ML-KEM-1024 PQC migration path, FROST 3-of-5 and 5-of-7 threshold signing for key
management).

### Remaining Gap After Mitigation

Cryptographic erasure is not native GDPR Article 17 compliance. It is a technical
approximation accepted under current regulatory interpretation. Three gaps remain:

First, the interpretation that key destruction constitutes erasure has not been affirmed
by all EU supervisory authorities and has not been tested in CJEU proceedings as of the
monograph version. Regulatory risk remains.

Second, the erasure key registry is itself a critical security and availability dependency.
If erasure keys are lost before an erasure request is received, the personal data becomes
permanently inaccessible even to the data controller, not merely to adversaries. Conversely,
if the erasure key registry is compromised, the personal data in all encrypted records is
exposed. The registry's security posture is as critical as the log store's.

Third, metadata fields in log records (timestamps, decision identifiers, pillar assessment
scores, threat vector categories) may themselves constitute personal data in some
jurisdictions, particularly when combined with other data sources. Key-destroying the
personal data content does not erase metadata. Complete Article 17 compliance may require
metadata erasure or suppression beyond what cryptographic erasure provides.

The feature therefore remains FUTURE: the Erasure Paradox is mitigated, not resolved.

---

## Feature 6: Full Permission Token Custodian Quorum Attestation (BETA, Not FUTURE)

For completeness: the `PermissionToken.custodianQuorumAttestation` field in
`tml_schema.json#/$defs/PermissionToken` is classified BETA, not FUTURE. It is buildable
with documented tradeoffs (regional rather than full cross-jurisdictional quorum, latency
penalties for certain deployment configurations). It is listed here to distinguish it from
the sub-500ms cross-jurisdiction quorum feature (Feature 4 above), which is FUTURE.

BETA features appear in the specification as optional fields or annotated endpoints. They
are buildable for regulated deployments where the performance tradeoffs are acceptable.
They are not blocked by Section 10 constraints; they are bounded by operational constraints
that regulated operators must evaluate for their specific deployment context.

---

### Appendix Index: FUTURE Features by Pillar

| Feature | Primary Pillar(s) | Section 10 Constraint | Specification Artifacts Affected |
|---------|--------------------|----------------------|----------------------------------|
| Real-time per-token blockchain anchoring | PublicBlockchains (VIII) | Throughput asymmetry | `POST /anchoring-logs` response; `PermissionToken`; `MerkleInclusionProof`; `TML_Core.anchorMerkleRoot` |
| PQC signature migration | GoukassianPromise (III); HybridShield (VII) | HSM and EVM toolchain readiness | `SignatureBlock.signatureAlgorithm`; `eip712_typed_data.json` algorithm IDs 6-7 |
| Hardware MPUs | SacredZero (I); AlwaysMemory (II) | No production silicon | Entire Dual-Lane Architecture; `GatewayRoutingStatus`; `PermissionToken.laneOrigin` |
| Sub-500ms cross-jurisdiction quorum | HybridShield (VII) | Network physics | `GET /regulator/custodian-quorum`; `PermissionToken.custodianQuorumAttestation`; `CustodianHeartbeat.latencyMs` |
| Immutable ledger with native GDPR Art. 17 compliance | AlwaysMemory (II); MoralTraceLogs (IV) | Erasure Paradox | All TSLF schemas; `SHA256Hex`; `PermissionToken.logHash`; `AuditProof` |
