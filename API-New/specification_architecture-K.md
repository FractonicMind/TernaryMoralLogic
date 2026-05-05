## 1. specification_architecture.md

### 1.1 Dual-Lane Architecture in OpenAPI Paths

The Ternary Moral Logic (TML) framework v3.3 expresses its foundational **Binary-Ternary Parallel Architecture** through a deliberate and rigorous separation of OpenAPI path structures, creating two distinct but interoperable API surfaces that correspond to the two cognitive lanes defined in the monograph. This architectural pattern is not merely organizational convenience; it is the technical embodiment of the principle that the **binary inference engine and the ternary governance coprocessor operate as sovereign peers**, neither subordinate to the other, with the binary system proposing actions and the ternary system exercising absolute veto authority over whether those actions physically cross the threshold into execution. The **Dual-Lane Latency Architecture**, with its explicit timing constraints of **less than 2 milliseconds for the Inference Lane** and **less than 500 milliseconds for the Anchoring Lane**, is preserved and enforced through endpoint design, security scheme differentiation, and schema constraints that make the latency contract machine-verifiable.

The OpenAPI specification achieves this separation through three primary mechanisms: **path prefix segregation**, **security scheme binding**, and **schema field conditioning**. Path prefixes `/inference/` and `/anchoring/` create immediate visual and programmatic distinction between the two lanes, ensuring that client developers cannot accidentally route governance traffic through the fast path or inference traffic through the governance path without explicit awareness of the crossing. Security scheme binding attaches `x-tml-security: "mTLS + ServiceAccountJWT"` exclusively to Inference Lane endpoints, while Anchoring Lane endpoints carry `x-tml-security: "HSM-SignedJWT + MutualTLS"`, creating a cryptographic access control layer that reflects the differing trust requirements of pattern recognition versus constitutional enforcement. Schema field conditioning, most critically in the `StateEnvelope` schema, uses JSON Schema `if-then` constructs to make `permission_token` mandatory only when `current_state` equals `+1`, encoding the **No Log = No Action** principle directly into validation logic.

| Lane | Path Prefix | Latency Target | System Level | Security Scheme | Primary Endpoint | Pillar Annotation |
|:---|:---|:---|:---|:---|:---|:---|
| Inference | `/inference/` | <2ms | System 1 (Fast) | `mTLS + ServiceAccountJWT` | `POST /inference/decisions` | `AlwaysMemory` |
| Anchoring | `/anchoring/` | <500ms | System 2 (Governance) | `HSM-SignedJWT + MutualTLS` | `POST /anchoring/logs` | `MoralTraceLogs` |

The repository context provided in Section 4 of the prompt indicates that documentation files including `Dual-Lane Architecture.md`, `TML_Gateway.md`, and `Sacred_Pause_Protocol.md` exist in the `docs/specs/` directory, but these are explicitly **informational back-context only** and are not to be mapped directly to API endpoints. Instead, the specification creates logical REST-style paths that abstract the physical implementation while preserving the semantic integrity of the dual-lane model. This abstraction layer is essential for the specification's goal of being implementation-agnostic; a TML-compliant system could be built on microservices, serverless functions, or embedded systems, provided it exposes the specified endpoints and honors the schema constraints.

#### 1.1.1 Inference Lane: Binary Proposition Pathway

The Inference Lane is operationalized through the endpoint **`POST /inference/decisions`**, which serves as the sole entry point for the binary inference engine to submit its proposed decision vectors and receive the system's state assessment. This endpoint is annotated with **`x-tml-pillar: "AlwaysMemory"`** (Pillar II), reflecting that even the fast path must generate an immutable pre-actuation commit before any further processing occurs. The monograph reference **`x-tml-monograph-ref: "Section 2.2.1"`** binds this endpoint to the specific textual authority that defines the Inference Lane's role and constraints. The implementation status is **`SHIPPING`**, indicating that this endpoint can be constructed with 2025 production libraries and infrastructure without known blockers from Section 10 of the monograph.

The request schema for `POST /inference/decisions` is the **`DecisionVector`**, which carries the decision context, the proposed action parameters, and preliminary confidence metrics from the binary system. The response schema is the **`StateEnvelope`**, but with a critical distinction: in the Inference Lane context, the `StateEnvelope` returned will **never contain a valid `permission_token` field**, because the Inference Lane lacks authority to issue Permission Tokens. Instead, the `StateEnvelope` at this stage represents a *proposed* state, a recommendation from the binary engine that awaits ternary validation. The `current_state` field may contain any of the three valid values (`+1`, `0`, `-1`), but when `current_state` is `+1`, the `permission_token` field will be either absent or explicitly marked as `null` with a `pending_anchoring` flag in the `state_metadata` object.

The security requirements for this endpoint enforce **`mTLS + ServiceAccountJWT`**, a lighter-weight authentication pattern appropriate for high-throughput internal service communication. The **`Idempotency-Key`** header is mandatory for all `POST` requests, ensuring that duplicate decision vectors from retry logic do not generate spurious log entries. Error responses conform to **RFC 7807 `application/problem+json`** with the required `x-tml-state`, `x-tml-pillar`, and `retry_after` fields, allowing clients to distinguish between transient infrastructure failures (retryable) and constitutional violations (non-retryable).

The latency target of less than 2 milliseconds is not enforced by the API specification itself; the specification defines the contract, not the runtime performance. However, the specification includes **`x-tml-latency-target: "<2ms"`** as an informational annotation, and the `StateEnvelope` schema includes a `proposed_at` timestamp field that, when compared with the `anchored_at` timestamp from the Anchoring Lane response, enables latency monitoring and alerting as an operational concern outside the specification's scope.

#### 1.1.2 Anchoring Lane: Ternary Governance Pathway

The Anchoring Lane is operationalized through the endpoint **`POST /anchoring/logs`**, which serves as the constitutional gate through which all proposed `+1` states must pass before actuation can occur. This endpoint is annotated with **`x-tml-pillar: "MoralTraceLogs"`** (Pillar IV), reflecting that the primary function of the Anchoring Lane is to generate, validate, and persist the Moral Trace Log (TSLF) that constitutes the forensic record of every governance decision. The monograph reference **`x-tml-monograph-ref: "Section 2.2.2"`** binds this endpoint to the specific textual authority that defines the Anchoring Lane's role as the sovereign execution dictator. The implementation status is **`SHIPPING`**, with the documented tradeoff that the less than 500 millisecond latency target may require regional deployment of anchoring infrastructure for globally distributed systems.

The request schema for `POST /anchoring/logs` is the complete **`MoralTraceLog`** object, which must conform to one of the three TSLF state variants (`TSLF-State0`, `TSLF-State-1`, `TSLF-State+1`) as determined by the **`discriminator`** field `log_type`. The response schema is the **`PermissionToken`**, the cryptographic release key that, when presented to the actuation layer, authorizes the physical execution of the proposed action. The `PermissionToken` schema enforces non-repudiation through required fields **`log_hash`** (SHA-256 of the anchored log), **`epoch_timestamp`**, **`signer_key_id`**, and **`lane_origin`**, with the cryptographic signature generated by the Anchoring Lane's HSM-protected signing key and verifiable against the current Merkle root.

The security requirements for this endpoint enforce **`HSM-SignedJWT + MutualTLS`**, a substantially stronger authentication pattern that requires hardware-backed key protection for the signing operations that generate Permission Tokens. This security elevation reflects the constitutional significance of the Anchoring Lane; compromise of an Inference Lane service account would allow spurious proposals, but compromise of an Anchoring Lane signing key would allow unauthorized actuations, violating the **No Log = No Action** principle at the most fundamental level. The **`Idempotency-Key`** header is again mandatory, with the additional constraint that idempotency keys for Anchoring Lane requests must be derived from the corresponding Inference Lane request's idempotency key through a deterministic transformation (specified as `SHA-256("anchoring:" + inference_idempotency_key)`), ensuring traceability across lane boundaries.

The **`lane_origin`** field in the `PermissionToken` schema is an enum with values `INFERENCE` and `ANCHORING`, but the specification clarifies that only **`ANCHORING`** is valid for tokens issued by `POST /anchoring/logs`. The `INFERENCE` value is reserved for future protocol extensions and, if encountered in a token presented for actuation, must trigger immediate rejection with `x-tml-state: "-1"` and escalation to the `POST /sacred-zero/escalation` endpoint.

#### 1.1.3 Lane Separation and Cryptographic Decoupling

The architectural principle that **the inference engine is cryptographically decoupled from actuation** is realized through a multi-layer enforcement strategy that spans endpoint design, schema validation, and operational protocol. At the endpoint layer, no Inference Lane path accepts a `PermissionToken` in its request body, and no Anchoring Lane path accepts a decision vector without an accompanying `MoralTraceLog`. At the schema layer, the `StateEnvelope` uses JSON Schema's `dependentRequired` keyword (Draft 2020-12) to make `permission_token` mandatory when `current_state` equals `+1`, but the `PermissionToken` schema itself is only defined in the `$defs` section referenced by Anchoring Lane responses. At the operational protocol layer, the actuation layer (which is outside the API specification's scope but referenced in the `TML_Gateway.md` back-context document) is required to maintain separate TLS certificate trust stores for the two lanes, with the Anchoring Lane trust store rooted in HSM-issued certificates that are physically and procedurally protected.

The **`POST /gateway/route`** endpoint provides explicit lane assignment logic, returning a `lane_assignment` object that contains the resolved endpoint URLs for both lanes, the expected latency targets, and the active security scheme identifiers. This endpoint is annotated with **`x-tml-pillar: "GoukassianPromise"`** (Pillar III), reflecting that correct lane assignment is part of the system's covenant with its users. The **`fail-closed`** status, accessible via `GET /gateway/fail-closed-status`, returns a boolean `is_fail_closed` that, when `true`, indicates the system has detected a lane integrity violation and has defaulted to refusing all `+1` proposals regardless of their content. This is the technical implementation of the Goukassian Vow's **"Refuse when harm is clear"** principle applied to infrastructure integrity.

### 1.2 Permission Token and No Log = No Action Enforcement

The **No Log = No Action** principle is the iron law of TML governance, and its enforcement at the schema level represents one of the most significant architectural innovations in the v3.3 specification. Unlike policy-based enforcement, which can be bypassed through configuration errors or privilege escalation, **schema-level enforcement creates a structural impossibility**: a `+1` state cannot be represented in a valid `StateEnvelope` without an accompanying `PermissionToken`, and the `PermissionToken` cannot be generated without a valid `MoralTraceLog` having been anchored. This creates a cryptographic dependency chain that is verifiable by any party possessing the relevant public keys and Merkle roots, without requiring trust in the system's operational configuration.

The enforcement mechanism relies on three schema constructs working in concert: **conditional field requirement**, **cross-schema reference validation**, and **cryptographic proof verification**. Conditional field requirement uses JSON Schema's `if-then-else` construct to evaluate the `current_state` field and apply different `required` arrays. Cross-schema reference validation ensures that when `permission_token` is present, it conforms to the `PermissionToken` schema with all its mandatory fields. Cryptographic proof verification is not performed by the schema itself; schemas validate structure, not cryptography. However, the schema requires the fields (`log_hash`, `epoch_timestamp`, `signer_key_id`, `lane_origin`) that make cryptographic verification possible, and the **`unevaluatedProperties: false`** constraint ensures that no additional fields can be injected to confuse verification logic.

#### 1.2.1 Schema-Level Constraint Mechanism

The `StateEnvelope` schema defines the outer decision container with the following core structure. The **`current_state`** field is a signed integer with enum values `[+1, 0, -1]`, represented in JSON as the number values `1`, `0`, `-1` (not strings). The **`state_label`** field is a string enum with values `["PROCEED", "SACRED_ZERO", "REFUSE"]`, providing human-readable annotation without ambiguity. The **`proposed_action`** field is an object containing `action_type` (string), `action_parameters` (object), and `action_hash` (SHA-256 of canonicalized parameters).

The conditional requirement is expressed through the following JSON Schema fragment:

```json
{
  "if": {
    "properties": {
      "current_state": { "const": 1 }
    },
    "required": ["current_state"]
  },
  "then": {
    "required": ["permission_token"],
    "properties": {
      "permission_token": {
        "$ref": "#/$defs/PermissionToken"
      }
    }
  },
  "else": {
    "properties": {
      "permission_token": {
        "type": "null"
      }
    }
  }
}
```

This construct ensures that any JSON instance with `current_state: 1` that lacks a `permission_token` field, or that has a `permission_token` field not conforming to the `PermissionToken` schema, will fail validation. The **`unevaluatedProperties: false`** constraint at the `StateEnvelope` root ensures that no workaround can inject the required data through non-standard field names. The `else` branch explicitly requires `permission_token` to be `null` for non-`+1` states, preventing confusion about whether a token might be present but ignored.

The `PermissionToken` schema is referenced through **`#/$defs/PermissionToken`**, maintaining the single-document bundle structure required by Deliverable B. The `$defs` section contains all schema definitions, and cross-references use `$ref` with absolute JSON Pointer paths. This structure enables the OpenAPI specification to reference the same schemas through `components.schemas` entries that proxy to the underlying `$defs`, ensuring consistency between the JSON Schema validation layer and the OpenAPI documentation layer.

#### 1.2.2 Permission Token Schema Structure

The `PermissionToken` schema is defined as a standalone definition in `$defs/PermissionToken` with the following mandatory fields and their semantic specifications. The **`log_hash`** field is a string with pattern `^[a-f0-9]{64}$`, representing the SHA-256 hash of the anchored `MoralTraceLog` in lowercase hexadecimal. This hash binds the token to a specific log entry, preventing token replay across different decisions. The **`epoch_timestamp`** field is an integer representing Unix epoch time in milliseconds, with minimum value `1609459200000` (2021-01-01T00:00:00Z) to prevent backdated tokens and maximum value derived from the current system time plus a clock skew tolerance of 300 seconds. The **`signer_key_id`** field is a string with format `urn:tml:signer:{custodian_id}:{key_version}`, identifying the specific HSM key that performed the signing operation. The **`lane_origin`** field is an enum string with values `["INFERENCE", "ANCHORING"]`, with `ANCHORING` being the only valid value for production tokens.

The non-repudiation binding is achieved through the **`signature`** field, which is an object containing `signature_value` (base64-encoded ECDSA signature over the canonicalized token fields), `signature_algorithm` (enum: `["ECDSA_P256", "ECDSA_P384", "Ed25519"]`), and `merkle_root` (the Merkle root against which the log hash can be verified). The `signature` field is not itself mandatory in the base `PermissionToken` schema; instead, it is required by the `StateEnvelope` conditional requirement when the token is embedded. This allows the `PermissionToken` schema to serve dual purposes: as a response schema from `POST /anchoring/logs` (where signature is generated by the server) and as a request schema to the actuation layer (where signature is verified by the receiver).

The **`x-tml-pillar`** annotation for the `PermissionToken` schema is `MoralTraceLogs` (Pillar IV), and the **`x-tml-monograph-ref`** is `"Section 2.2.3"`. The schema includes **`x-tml-implementation-status: "SHIPPING"`** at the definition level, with a sibling **`x-tml-blocking-constraint: null`** to indicate no Section 10 blockers apply to the base token structure.

#### 1.2.3 Operational Workflow

The complete operational workflow for a `+1` state transition proceeds through six distinct phases, each with defined API interactions and schema validations. **Phase 1, Inference**, involves the client submitting a decision vector to `POST /inference/decisions` and receiving a `StateEnvelope` with `current_state: 1` and `permission_token: null`. **Phase 2, Justification**, involves the client constructing a `JustificationObject` that includes the original decision vector, the inference response, and the proposed action parameters. **Phase 3, Anchoring**, involves submitting the `JustificationObject` along with a `MoralTraceLog` (variant `TSLF-State+1`) to `POST /anchoring/logs`. **Phase 4, Token Issuance**, involves the Anchoring Lane validating the log, computing its hash, generating the `PermissionToken`, and returning it to the client. **Phase 5, Reconstitution**, involves the client constructing a new `StateEnvelope` with `current_state: 1` and the valid `permission_token` field populated. **Phase 6, Actuation**, involves presenting this reconstituted `StateEnvelope` to the actuation layer, which verifies the token's signature and Merkle inclusion before executing the proposed action.

Any failure in Phases 3 through 5 results in the system defaulting to `current_state: 0` (Sacred Zero) and activating the Sacred Pause workflow via `POST /sacred-zero/escalation`. The `StateEnvelope` schema supports this transition through the **`fallback_state`** field, which is mandatory when `current_state` is `0` and must contain the state that would have been reached absent the triggering condition. For a `+1` proposal that fails anchoring, `fallback_state` would be `1` with `fallback_reason: "ANCHORING_FAILURE"`.

### 1.3 Goukassian Promise Artifacts as API Resources

The **Goukassian Promise**, defined in Monograph Section 1.5 as the tripartite covenant consisting of the Lantern, the Signature, and the License, is operationalized in the API specification as three distinct but interrelated resource types. Each artifact has its own schema, its own endpoint or embedding pattern, and its own lifecycle within the TML governance protocol. The specification strictly enforces the **canonical string names `lantern`, `signature`, and `license`** in all machine-readable contexts, with emoji symbols and visual shorthand restricted to narrative markdown and human-facing documentation.

The Goukassian Promise is annotated with **`x-tml-pillar: "GoukassianPromise"`** (Pillar III) across all its operationalized resources. This pillar identifier is used consistently in endpoint annotations, schema `x-tml-pillar` properties, and webhook callback registrations. The monograph reference for all Goukassian Promise resources is `"Section 2.3"`, with subsections `2.3.1` (License), `2.3.2` (Signature), and `2.3.3` (Lantern) used for granular referencing where appropriate.

| Artifact | API Resource | Schema | Primary Endpoint | Purpose | Monograph Ref |
|:---|:---|:---|:---|:---|:---|
| Lantern | Public beacon | `LanternStatus` | `GET /gateway/lantern` | Compliance signal broadcast | `Section 2.3.3` |
| Signature | Provenance mark | `SignatureBlock` | Embedded in `JustificationObject` | Non-repudiation binding | `Section 2.3.2` |
| License | Capability grant | `LicenseValidationRequest` | `POST /license/validate` | Permission scope verification | `Section 2.3.1` |

#### 1.3.1 Lantern Status Resource

The Lantern Status is the **public compliance beacon signal** that provides external visibility into the system's current governance posture. It is operationalized through the endpoint **`GET /gateway/lantern`**, which returns the `LanternStatus` schema. This endpoint is unauthenticated in its base form, reflecting the Lantern's role as a public signal, but rate-limited to prevent beacon flooding attacks. An authenticated variant **`GET /gateway/lantern/detailed`** is available for authorized auditors, returning additional fields including `custodian_quorum_status` and `last_merkle_anchor_height`.

The `LanternStatus` schema contains the following fields. The **`lanternState`** field is an enum string with values `["LIT", "DIM", "DARK", "PULSING"]`, where `LIT` indicates normal operation with all pillars functional, `DIM` indicates degraded operation with one or more pillars in non-optimal state, `DARK` indicates emergency shutdown or complete governance failure, and `PULSING` indicates active Sacred Pause conditions with human review pending. The **`lastTransition`** field is an ISO 8601 timestamp of the most recent state change. The **`signalBroadcast`** field is an object containing `broadcast_frequency_seconds` (integer, default 60), `next_scheduled_broadcast` (timestamp), and `broadcast_channel_uris` (array of webhook URLs registered for `lanternStatus.broadcast` callbacks).

The `LanternStatus` schema is embedded in the `TSLF-State0` (Sacred Pause Log) as the `lantern_status` field, creating a recursive self-documentation pattern where the log of the pause condition includes the public signal state that was active when the pause was triggered. This embedding uses the same schema definition through `$ref`, ensuring consistency between the public beacon and the forensic record.

The webhook **`lanternStatus.broadcast`** is defined in the OpenAPI `webhooks` section with payload schema `LanternStatus`, retry semantics of fixed 30-second intervals with maximum 3 attempts, and required `x-tml-idempotency` header derived from `SHA-256(lanternState + lastTransition)`. The **`x-tml-pillar`** annotation for this webhook is `GoukassianPromise`, and the **`x-tml-monograph-ref`** is `"Section 2.3.3"`.

#### 1.3.2 Signature Block Resource

The Signature Block is the **provenance and non-repudiation artifact** that binds every governance decision to its originating authority. It is operationalized as the `SignatureBlock` schema, which is embedded within the `JustificationObject` for inter-lane transport and within the `TSLF-State+1` (Proceed Log) as the **`the_signature`** field. The canonical field name **`the_signature`** (with definite article) is mandated by the monograph's terminology enforcement rules and must not be shortened to `signature` or expanded to `signature_block` in machine-readable contexts.

The `SignatureBlock` schema contains the following fields. The **`signatureValue`** field is a base64-encoded string containing the cryptographic signature. The **`signerKeyId`** field is a string with the `urn:tml:signer:` prefix format described in Section 1.2.2. The **`signingTimestamp`** field is an ISO 8601 timestamp with millisecond precision. The **`signatureAlgorithm`** field is an enum string with values `["ECDSA_P256", "ECDSA_P384", "Ed25519"]`, with `ECDSA_P256` as the default for 2025 shipping implementations. The **`signaturePurpose`** field is an enum string with values `["LANE_ATTESTATION", "CUSTODIAN_ACKNOWLEDGMENT", "OVERRIDE_AUTHORIZATION"]`, distinguishing between routine lane-to-lane attestation, multi-custodian quorum acknowledgment, and emergency override scenarios.

The `SignatureBlock` schema includes **algorithm agility** as a forward-compatibility mechanism for quantum-proof migration. The `signatureAlgorithm` field accepts the current values but is defined with `unevaluatedProperties: false` at the schema root to prevent injection of unrecognized algorithm identifiers. Future PQC algorithm identifiers will be added through schema version revision, not through permissive validation. This design reflects the monograph's Section 10.7 guidance that algorithm agility must be structured, not open-ended.

The **`x-tml-pillar`** annotation for the `SignatureBlock` schema is `GoukassianPromise`, and the **`x-tml-monograph-ref`** is `"Section 2.3.2"`. The **`x-tml-implementation-status`** is `SHIPPING` for `ECDSA_P256` and `ECDSA_P384`, with `Ed25519` marked as `BETA` due to its less universal HSM support in 2025.

#### 1.3.3 License Validation Resource

The License is the **binding prohibition against weaponization and surveillance**, operationalized through the `LicenseValidationRequest` schema and the **`POST /license/validate`** endpoint. Unlike the Lantern and Signature, which are primarily observability and provenance artifacts, the License is an **active enforcement mechanism** that gates system capability based on granted permissions and prohibited use cases.

The `POST /license/validate` endpoint accepts a `LicenseValidationRequest` and returns a `LicenseValidationResponse`. The request schema contains `licenseId` (string, UUID format), `scopeVector` (object mapping capability identifiers to boolean grants), `validityPeriod` (object with `notBefore` and `notAfter` timestamps), and `revocationStatus` (enum: `["ACTIVE", "SUSPENDED", "REVOKED", "EXPIRED"]`). The response schema contains `validationResult` (enum: `["VALID", "INVALID", "CONDITIONAL"]`), `conditionalConstraints` (array of constraint objects, present only when `validationResult` is `CONDITIONAL`), and `nextRevalidation` (timestamp).

The License validation endpoint is annotated with **`x-tml-pillar: "GoukassianPromise"`** and **`x-tml-monograph-ref: "Section 2.3.1"`**. The implementation status is **`SHIPPING`** for base validation logic, with **`BETA`** status for the `CONDITIONAL` validation path that supports dynamic constraint injection. The **`x-tml-blocking-constraint`** for the `CONDITIONAL` path is `"Section 10.6"` (Dynamic Policy Evaluation Performance), indicating that real-time constraint resolution at scale remains an area of active optimization.

The License is referenced in the `TSLF-State-1` (Refusal Log) through the **`license_violation`** field, which contains a `LicenseValidationRequest` object representing the validation attempt that triggered the refusal. This creates a complete forensic chain: the system attempted to validate a license for a proposed action, the validation failed or returned a constraint violation, and the refusal log captures both the proposed action and the license context that justified the refusal.

### 1.4 Sacred Zero and Sacred Pause Operationalization

The **Sacred Zero state** and its associated **Sacred Pause workflow** represent one of the most distinctive and technically challenging aspects of the TML architecture. The specification enforces a **strict separation between the state (`SacredZero`, numeric value `0`) and the process (`SacredPause`, the operational workflow that executes within that state)**, preventing the conceptual collapse that would occur if the process name were used as a state alias. This separation is maintained through field naming conventions, schema structures, and endpoint designs that make the distinction machine-verifiable.

The **Sacred Zero is never represented as `null`, `error`, `false`, or `timeout`** in any schema or endpoint response. It is a first-class governance state with its own complete TSLF variant (`TSLF-State0`), its own escalation endpoint, its own webhook callback, and its own set of operational semantics. The `StateEnvelope` schema supports Sacred Zero through the standard `current_state: 0` and `state_label: "SACRED_ZERO"` fields, with additional fields **`process_active: "SacredPause"`** and **`pause_duration_ms`** (integer, cumulative pause time in milliseconds) that are mandatory when `current_state` is `0`.

| Representation | Valid | Example |
|:---|:---|:---|
| State value | Yes | `current_state: 0` |
| State label | Yes | `state_label: "SACRED_ZERO"` |
| Process active | Yes | `process_active: "SacredPause"` |
| State alias | **No** | `state: "SacredPause"` (rejected) |
| Null state | **No** | `current_state: null` (rejected) |
| Error state | **No** | `current_state: "error"` (rejected) |

#### 1.4.1 State Representation

The `StateEnvelope` schema represents Sacred Zero through the following mandatory and conditional fields. The **`current_state`** field is the integer `0`. The **`state_label`** field is the string `"SACRED_ZERO"`. The **`proposed_action`** field remains present but is wrapped in a **`suspended_action`** object that adds `suspension_reason` (enum: `["UNCERTAINTY_THRESHOLD", "HUMAN_REVIEW_REQUIRED", "CUSTODIAN_QUORUM_PENDING", "EMERGENCY_HALT"]`) and `suspension_timestamp`. The **`process_active`** field is the string `"SacredPause"`, mandatory for `current_state: 0`. The **`pause_duration_ms`** field is an integer tracking cumulative pause time. The **`escalation_queue_position`** field is an integer, present only when `suspension_reason` is `"HUMAN_REVIEW_REQUIRED"`.

The **`TSLF-State0`** schema (Sacred Pause Log) contains the following fields that operationalize the Sacred Pause workflow. The **`lantern_status`** field is a `LanternStatus` object, capturing the public beacon state at pause initiation. The **`uncertainty_quantification`** field is an object with `uncertainty_score` (float, 0.0 to 1.0), `uncertainty_dimensions` (array of dimension identifiers), and `threshold_breaches` (array of threshold identifiers that were exceeded). The **`deliberation_matrix`** field is an object with `stakeholder_views` (array of view objects), `evidence_considered` (array of evidence references), and `deliberation_outcome` (enum: `["PROCEED_RECOMMENDED", "REFUSE_RECOMMENDED", "EXTEND_PAUSE"]`). The **`resolution_request`** field is an object with `request_type` (enum: `["HUMAN_ARBITER", "CUSTODIAN_VOTE", "AUTOMATED_REEVALUATION"]`), `request_timestamp`, and `request_priority` (integer, 1 to 5).

The **`unevaluatedProperties: false`** constraint on `TSLF-State0` ensures that no additional fields can be injected into the Sacred Pause Log, preserving its forensic integrity. The **`discriminator`** field `log_type` with value `"SACRED_ZERO"` distinguishes this variant from `TSLF-State-1` and `TSLF-State+1` in the `oneOf` construct that defines the base `MoralTraceLog` schema.

#### 1.4.2 Sacred Pause Workflow

The Sacred Pause workflow is initiated through the endpoint **`POST /sacred-zero/escalation`**, which accepts a `SacredZeroEscalationRequest` and returns a `SacredZeroEscalationResponse`. The request schema contains `triggering_envelope` (the `StateEnvelope` that triggered the pause), `escalation_reason` (enum, matching `suspension_reason` values), and `requested_priority` (integer, 1 to 5, default 3). The response schema contains `escalation_id` (UUID), `queue_position` (integer), `estimated_resolution_time` (ISO 8601 duration), and `assigned_arbiter_pool` (string, identifier of the human reviewer group).

The `POST /sacred-zero/escalation` endpoint is annotated with **`x-tml-pillar: "SacredZero"`** and **`x-tml-monograph-ref: "Section 2.3.3"`**. The implementation status is **`SHIPPING`** for automated escalation and queue management, with **`BETA`** status for the `estimated_resolution_time` prediction algorithm. The security requirement is **`HSM-SignedJWT + MutualTLS`**, reflecting that Sacred Pause initiation is a governance action requiring the same trust level as Anchoring Lane operations.

The webhook **`sacredPause.escalation`** is defined in the OpenAPI `webhooks` section with payload schema `SacredZeroEscalationPayload` (a subset of the escalation response containing non-sensitive queue information). The retry semantics are **exponential backoff starting at 1 second, doubling to maximum 60 seconds, with maximum 5 attempts**. The **`x-tml-idempotency`** header is required and derived from `SHA-256(escalation_id + triggering_envelope.current_state)`. The **`x-tml-pillar`** annotation is `SacredZero`, and the **`x-tml-monograph-ref`** is `"Section 2.3.3"`.

The Sacred Pause workflow includes an **automatic timeout mechanism** that transitions the state from `0` to `-1` (Refuse) if resolution is not achieved within a configurable `max_pause_duration_ms`. This timeout is not a `timeout` error condition; it is a deliberate governance decision that **"uncertainty extended beyond acceptable bounds" constitutes a refusal condition**. The `TSLF-State0` schema captures this through the `resolution_request` field's `request_type` value `"AUTOMATED_REEVALUATION"`, which triggers the timeout evaluation logic.

### 1.5 Eight Pillars Operationalized as API Capabilities versus Out-of-Band Processes

The **Eight Pillars of TML** are operationalized through a deliberate pattern that distinguishes **API capabilities** (machine-invokable functions defined in the OpenAPI specification) from **out-of-band processes** (human and organizational procedures that the API supports but does not replace). This distinction is critical for the specification's audience split: engineers must know what the system can do autonomously, while auditors must know what requires human judgment and procedural verification.

Each pillar has a **canonical machine-readable identifier** used in `x-tml-pillar` annotations, as specified in Section 2 of the prompt. The following subsections describe the operationalization pattern for each pillar, with API capabilities listed as endpoint/schema pairs and out-of-band processes described as contextual requirements.

| Pillar | Identifier | API Capabilities | Out-of-Band Processes | Monograph Ref |
|:---|:---|:---|:---|:---|
| I | `SacredZero` | `POST /sacred-zero/escalation`, `TSLF-State0` schema, `sacredPause.escalation` webhook | Human arbiter pool management, organizational escalation protocols, pause timeout policy setting | `Section 2.3.3` |
| II | `AlwaysMemory` | `POST /inference/decisions` (pre-actuation commit), `StateEnvelope` persistence, `JustificationObject` transport | Long-term archival infrastructure, spoliation prevention procedures, storage media lifecycle management | `Section 2.2.1` |
| III | `GoukassianPromise` | `GET /gateway/lantern`, `POST /license/validate`, `SignatureBlock` schema, `LanternStatus` schema, `LicenseValidationRequest` schema | Key ceremony for signing key generation, trust anchor establishment and maintenance, legal framework adherence and jurisdictional compliance | `Section 1.5`, `Section 2.3` |
| IV | `MoralTraceLogs` | `POST /anchoring/logs`, `GET /audit/verifications/merkle-root/{logHash}`, `GET /audit/verifications/log-inclusion/{tokenId}`, TSLF schema variants (`TSLF-State0`, `TSLF-State-1`, `TSLF-State+1`), `PermissionToken` schema | Forensic analysis procedures, chain of custody maintenance, log integrity verification over extended time horizons | `Section 2.2.2`, `Section 8` |
| V | `HumanRightsMandate` | `POST /auditor/human-rights/udhr`, `POST /redress/human-rights-grievance`, human rights vector fields in `TSLF-State-1` | UDHR/Geneva vector enforcement by qualified legal authorities, grievance adjudication procedures, reparation and redress fulfillment | `Section 2.4` |
| VI | `EarthProtectionMandate` | `POST /auditor/earth-protection/paris`, environmental impact fields in `TSLF-State+1` and `TSLF-State-1` | Paris Agreement vector enforcement by environmental authorities, carbon accounting and offset verification, ecosystem damage assessment | `Section 2.4` |
| VII | `HybridShield` | `POST /hybrid-shield/confirm`, `GET /audit/verifications/custodian-heartbeat`, `GET /regulator/custodian-quorum-status`, custodian acknowledgment fields in `SignatureBlock` | 6-custodian distributed key management, quorum ceremonies, custodian selection and rotation, physical security of custodian infrastructure | `Section 2.2.2`, `Section 10.4` |
| VIII | `PublicBlockchains` | `POST /blockchain/anchor`, `GET /audit/verifications/merkle-root/{logHash}`, Merkle root fields in `PermissionToken` | Batch scheduling and gas management, blockchain network selection governance, anchor confirmation monitoring, fork handling procedures | `Section 2.2.2`, `Section 10.2` |

#### 1.5.1 Pillar I: SacredZero

Pillar I, **`SacredZero`**, is operationalized through the `POST /sacred-zero/escalation` endpoint and the `TSLF-State0` schema. The API capabilities focus on initiation, tracking, and notification of Sacred Pause conditions, while the substantive resolution of those conditions (human judgment, custodian vote, or automated reevaluation) is defined as out-of-band. The `TSLF-State0` schema captures the complete context of a Sacred Pause for forensic purposes, but the schema itself does not encode resolution logic; it encodes the request for resolution and the evidence considered.

#### 1.5.2 Pillar II: AlwaysMemory

Pillar II, **`AlwaysMemory`**, operationalizes the principle that memory must be created before action can be contemplated. In the API specification, this is realized through the requirement that every `POST /inference/decisions` request generates a `JustificationObject` that is immediately persisted before any state assessment is returned. The `StateEnvelope` schema includes `memory_commit_timestamp` and `memory_commit_hash` fields that bind the envelope to this pre-actuation commit. The out-of-band processes include the physical and procedural measures that ensure this memory cannot be altered or destroyed, which are outside the API specification's scope but referenced in the `ANCHORING_STANDARDS.md` and `SYNC_PROTOCOL.md` back-context documents.

#### 1.5.3 Pillar III: GoukassianPromise

Pillar III, **`GoukassianPromise`**, operationalizes the tripartite covenant through three distinct API resource patterns. The Lantern is a read-only observability resource with public and authenticated variants. The Signature is an embedded provenance artifact within transport and logging schemas. The License is an active validation mechanism with request-response semantics. The out-of-band processes are particularly extensive for this pillar, encompassing the cryptographic ceremonies and legal frameworks that make the machine-readable artifacts meaningful. The specification explicitly does not define these ceremonies; they are referenced as organizational requirements in the monograph and assumed to be implemented through procedures outside the API surface.

#### 1.5.4 Pillar IV: MoralTraceLogs

Pillar IV, **`MoralTraceLogs`**, is the most extensively operationalized in the API specification, reflecting its central role in the No Log = No Action principle. The TSLF schema variants use `oneOf` with `discriminator` to create a unified but type-safe logging structure that captures the distinct evidentiary requirements of each triadic state. The `PermissionToken` schema, while technically a separate artifact, is annotated with this pillar because it is the cryptographic release mechanism that makes the logs actionable. The out-of-band processes include the forensic and legal procedures that transform the machine-readable logs into admissible evidence, which are referenced in the `tml_audit_project/` back-context directory but not defined in the API specification.

#### 1.5.5 Pillar V: HumanRightsMandate

Pillar V, **`HumanRightsMandate`**, operationalizes the requirement that the system detect and refuse actions that would violate human rights norms. The API capabilities focus on detection logging (`TSLF-State-1` captures `threat_vector_analysis` with human rights-specific dimensions) and grievance filing (`POST /redress/human-rights-grievance` creates a subject-initiated challenge). The `POST /auditor/human-rights/udhr` endpoint allows auditors to pull compliance attestations specific to human rights enforcement. The out-of-band processes are substantive legal procedures that the API supports but cannot replace; the specification explicitly notes that grievance filing does not constitute legal action and that the API creates a record that may be used in subsequent legal proceedings.

#### 1.5.6 Pillar VI: EarthProtectionMandate

Pillar VI, **`EarthProtectionMandate`**, follows a similar operationalization pattern to Pillar V, with API capabilities focused on detection logging and compliance attestation. The `TSLF-State+1` (Proceed Log) includes `ethical_verification` with `environmental_impact_assessment` sub-fields, while `TSLF-State-1` includes `threat_vector_analysis` with `environmental_harm_dimensions`. The `POST /auditor/earth-protection/paris` endpoint returns compliance attestations against Paris Agreement vectors. The out-of-band processes include the scientific and regulatory procedures for environmental impact assessment that the API records but does not perform.

#### 1.5.7 Pillar VII: HybridShield

Pillar VII, **`HybridShield`**, operationalizes the 6-custodian distributed anchoring model through API capabilities that verify custodian participation and quorum achievement. The `POST /hybrid-shield/confirm` endpoint accepts a `HybridShieldConfirmationRequest` containing `custodian_acknowledgments` (array of `SignatureBlock` objects with `signaturePurpose: "CUSTODIAN_ACKNOWLEDGMENT"`) and returns a `quorum_status` object. The heartbeat and quorum status endpoints provide continuous monitoring. The out-of-band processes are extensive, encompassing the physical, procedural, and organizational measures that make distributed custody meaningful. The specification explicitly notes that API-level quorum confirmation does not replace procedural verification of custodian identity and availability.

#### 1.5.8 Pillar VIII: PublicBlockchains

Pillar VIII, **`PublicBlockchains`**, operationalizes Merkle-batched anchoring through API capabilities that initiate anchoring operations and verify anchor inclusion. The `POST /blockchain/anchor` endpoint accepts a `BlockchainAnchorRequest` containing `merkle_root` (string, hex), `batch_size` (integer), and `target_networks` (array of network identifiers), and returns a `BlockchainAnchorResponse` with `anchor_transaction_hashes` and `confirmation_status`. The `GET /audit/verifications/merkle-root/{logHash}` endpoint verifies that a specific log hash is included in an anchored Merkle root. The out-of-band processes include the operational complexities of blockchain interaction that the API abstracts but does not eliminate, including the critical Section 10.2 constraint that real-time per-token anchoring is not achievable at global AI scale.

### 1.6 Additional Endpoint Categories

Beyond the core dual-lane and pillar-specific endpoints, the specification defines additional endpoint categories that complete the TML governance surface. These categories are organized by functional domain rather than by lane or pillar, but each endpoint maintains its `x-tml-pillar` and `x-tml-monograph-ref` annotations.

#### 1.6.1 Refusal State Endpoints

The Refusal State endpoints operationalize the `-1` (Refuse) state and its associated logging and license violation recording functions. The primary endpoint is **`POST /refusal/logs`**, which accepts a `TSLF-State-1` (Refusal Log) and returns an acknowledgment with `refusal_id` and `archived_at` timestamp. This endpoint is annotated with **`x-tml-pillar: "MoralTraceLogs"`** and **`x-tml-monograph-ref: "Section 2.2.2"`**.

The secondary endpoint is **`POST /refusal/license-violation`**, which accepts a `LicenseViolationRecord` containing `violated_license` (embedded `LicenseValidationRequest`), `violating_action` (action object), `violation_type` (enum: `["WEAPONIZATION", "SURVEILLANCE", "UNAUTHORIZED_SCOPE", "REVOKED_LICENSE_USE"]`), and `remediation_required` (boolean). This endpoint is annotated with **`x-tml-pillar: "GoukassianPromise"`** and **`x-tml-monograph-ref: "Section 2.3.1"`**. The implementation status is `SHIPPING` for base violation recording, with `BETA` for automated remediation workflow initiation.

The `TSLF-State-1` schema contains the following mandatory fields. The **`license_violation`** field is a `LicenseViolationRecord` object. The **`threat_vector_analysis`** field is an object with `threat_category` (enum: `["HUMAN_RIGHTS", "EARTH_PROTECTION", "GOVERNANCE_INTEGRITY", "SECURITY"]`), `threat_severity` (integer, 1 to 5), and `threat_indicators` (array of indicator objects). The **`chain_of_custody`** field is an array of `CustodyEvent` objects with `custodian_id`, `event_type`, and `event_timestamp`, documenting the handling of the refusal evidence.

#### 1.6.2 Emergency Override Endpoints

The Emergency Override endpoints operationalize Monograph Section 13.3's provisions for break-glass shutdown, kill switch activation, and forced state transitions under supreme authority. These endpoints represent the highest-privilege operations in the TML system and are protected by the strongest security requirements and the most extensive audit logging.

The **`POST /emergency/override`** endpoint accepts an `EmergencyOverrideRequest` containing `override_type` (enum: `["CONSTITUTIONAL_FREEZE", "LANE_ISOLATION", "FORCED_STATE_TRANSITION"]`), `override_authority` (string, supreme authority identifier), `override_justification` (string, minimum 100 characters), and `override_signature` (embedded `SignatureBlock` with `signaturePurpose: "OVERRIDE_AUTHORIZATION"`). The response is an `EmergencyOverrideResponse` with `override_id`, `effective_at` timestamp, and `affected_endpoints` (array of path strings). This endpoint is annotated with **`x-tml-pillar: "SacredZero"`** and **`x-tml-monograph-ref: "Section 13.3"`**. The implementation status is `SHIPPING` for override execution, with `BETA` for automated affected endpoint calculation.

The **`POST /emergency/kill-switch`** endpoint accepts a `KillSwitchRequest` with `activation_level` (enum: `["SOFT_HALT", "HARD_HALT", "DESTRUCTIVE_ZEROIZATION"]`) and returns a `KillSwitchResponse` with `activation_id` and `estimated_recovery_time`. The **`POST /emergency/forced-transition`** endpoint accepts a `ForcedTransitionRequest` with `target_state` (enum: `["+1", "0", "-1"]`, but with constraints that prevent transition to `+1` without a valid `PermissionToken` even in emergency context), `transition_authority`, and `transition_justification`.

All emergency endpoints require **`HSM-SignedJWT + MutualTLS`** security and additional **`x-tml-emergency-authorization`** header containing a secondary authorization code. The `Idempotency-Key` requirement is waived for emergency requests (to prevent idempotency key unavailability from blocking emergency response), but the endpoints generate their own idempotency tokens internally for logging purposes.

#### 1.6.3 Auditor Verification Endpoints

The Auditor Verification endpoints provide the evidence verification capabilities required for external audit of TML system compliance. These endpoints are annotated with `x-tml-pillar` values of `HybridShield` or `PublicBlockchains` depending on the verification target, and all require **`CA-VettedJWT + IPAllowlist`** security.

The **`GET /audit/verifications/merkle-root/{logHash}`** endpoint returns a `MerkleVerificationResponse` containing `merkle_root` (hex string), `inclusion_proof` (array of sibling hashes), `anchor_transaction_hash` (blockchain transaction reference), and `confirmation_depth` (integer, number of block confirmations). This endpoint is annotated with **`x-tml-pillar: "PublicBlockchains"`** and **`x-tml-monograph-ref: "Section 2.4.8"`**.

The **`GET /audit/verifications/log-inclusion/{tokenId}`** endpoint returns a `LogInclusionResponse` containing `log_hash`, `merkle_root`, `inclusion_path`, and `verification_status` (enum: `["VERIFIED", "PENDING", "FAILED"]`). This endpoint is annotated with **`x-tml-pillar: "MoralTraceLogs"`** and **`x-tml-monograph-ref: "Section 2.4.4"`**.

The **`GET /audit/verifications/custodian-heartbeat`** endpoint returns a `CustodianHeartbeatResponse` containing `custodians` (array of objects with `custodian_id`, `last_heartbeat`, `jurisdiction`, `quorum_participation_status`, and `signature_valid`). This endpoint is annotated with **`x-tml-pillar: "HybridShield"`** and **`x-tml-monograph-ref: "Section 2.4.7"`**.

The **`GET /audit/verifications/compliance-attestation`** endpoint returns a `ComplianceAttestation` document containing `attestation_id`, `generated_at`, `valid_until`, `pillar_status` (object mapping each pillar to `COMPLIANT`, `NON_COMPLIANT`, or `NOT_ASSESSED`), and `attestation_signature` (SignatureBlock signed by the compliance officer's key). This endpoint is annotated with **`x-tml-pillar: "GoukassianPromise"`** and **`x-tml-monograph-ref: "Section 2.3.1"`**.

#### 1.6.4 Redress and Appeal Endpoints

The Redress and Appeal endpoints implement the subject-initiated challenge mechanisms required by the Human Rights Mandate. These endpoints enable affected parties to contest TML decisions and seek re-evaluation or remedy.

The **`POST /redress/appeal`** endpoint accepts a `RedressAppealRequest` containing `subject_identifier` (pseudonymized), `challenged_decision_id` (reference to original StateEnvelope), `appeal_grounds` (enum: `["PROCEDURAL_ERROR", "RIGHTS_VIOLATION", "FACTUAL_INCORRECTNESS", "BIAS_ALLEGATION"]`), and `requested_remedy` (enum: `["REVERSAL", "COMPENSATION", "EXPLANATION", "POLICY_CHANGE"]`). The response is a `RedressAppealResponse` with `appeal_id`, `assigned_reviewer_pool`, and `estimated_resolution_time`. This endpoint is annotated with **`x-tml-pillar: "HumanRightsMandate"`** and **`x-tml-monograph-ref: "Section 2.4.5"`**.

The **`POST /redress/re-evaluation`** endpoint accepts a `ReEvaluationRequest` containing `original_log_id`, `new_evidence` (optional structured data), and `reevaluation_scope` (enum: `["FULL", "LIMITED", "HUMAN_REVIEW_ONLY"]`). The response is a `ReEvaluationResponse` with `reevaluation_id` and `status`. This endpoint is annotated with **`x-tml-pillar: "MoralTraceLogs"`** and **`x-tml-monograph-ref: "Section 2.4.4"`**.

The **`POST /redress/human-rights-grievance`** endpoint accepts a `HumanRightsGrievanceRequest` with enhanced fields for UDHR-specific claims: `violated_articles` (array of UDHR article numbers), `affected_party_demographics` (optional, for disparate impact analysis), and `urgency_flag` (boolean, for expedited review). This endpoint is annotated with **`x-tml-pillar: "HumanRightsMandate"`** and **`x-tml-monograph-ref: "Section 2.4.5"`**.

All redress endpoints require **`CA-VettedJWT + IPAllowlist`** security, with additional `x-tml-subject-verification` header for identity binding. Implementation status is `SHIPPING` for appeal submission, `BETA` for re-evaluation execution (due to computational cost of re-running anchoring), and `BETA` for grievance adjudication (due to need for human rights expertise integration).

#### 1.6.5 Regulator Inspection Endpoints

The Regulator Inspection endpoints enable bulk oversight and cross-jurisdictional coordination for supervisory authorities. These endpoints support the "Compliance-as-a-Service" economy described in the monograph by providing structured, exportable evidence packages.

The **`POST /regulator/bulk-evidence-export`** endpoint accepts a `BulkEvidenceExportRequest` containing `time_range` (object with `start` and `end`), `pillar_filter` (array of pillar identifiers to include), `decision_state_filter` (array of states: `["+1", "0", "-1"]`), `anonymization_level` (enum: `["NONE", "PSEUDONYMIZED", "AGGREGATED"]`), and `delivery_format` (enum: `["JSON", "PARQUET", "PDF_REPORT"]`). The response is an `ExportJobResponse` with `job_id`, `estimated_completion_time`, and `secure_download_url` (time-limited, IP-restricted). This endpoint is annotated with **`x-tml-pillar: "MoralTraceLogs"`** and **`x-tml-monograph-ref: "Section 2.4.4"`**.

The **`GET /regulator/custodian-quorum-status`** endpoint returns a `CrossJurisdictionQuorumStatus` containing `jurisdictions` (array of country codes), `custodian_status_by_jurisdiction` (object mapping jurisdictions to arrays of custodian status objects), `global_quorum_achievable` (boolean), and `latency_ms` (measured or estimated time to achieve global quorum). This endpoint is annotated with **`x-tml-pillar: "HybridShield"`** and **`x-tml-monograph-ref: "Section 2.4.7"`**. The implementation status is `SHIPPING` for regional quorum status, `BETA` for cross-jurisdiction latency reporting, and `FUTURE` for sub-500ms global unanimous quorum (blocked by Section 10.4).

The **`GET /regulator/qualified-timestamp`** endpoint returns a `QualifiedTimestampResponse` containing `timestamp` (RFC 3161 format), `timestamp_authority` (identifier), `eidas_qualified` (boolean), and `signature` (SignatureBlock from the timestamp authority). This endpoint is annotated with **`x-tml-pillar: "PublicBlockchains"`** and **`x-tml-monograph-ref: "Section 2.4.8"`**.

#### 1.6.6 Gateway Endpoints

The Gateway Endpoints provide the TML Gateway Logic that routes requests to appropriate lanes, manages lane assignment under load, and exposes system-level status for operational monitoring.

The **`POST /gateway/route`** endpoint accepts a `GatewayRouteRequest` containing `payload_type` (enum: `["DECISION_VECTOR", "MORAL_TRACE_LOG", "AUDIT_QUERY", "REDRESS_REQUEST"]`), `priority_class` (enum: `["ROUTINE", "URGENT", "EMERGENCY"]`), and `source_identity` (service account identifier). The response is a `GatewayRouteResponse` with `assigned_lane` (enum: `["INFERENCE", "ANCHORING", "AUDIT", "REDRESS"]`), `endpoint_url` (resolved URL), `latency_target_ms` (expected response time), and `fallback_endpoints` (array of alternative URLs for disaster recovery). This endpoint is annotated with **`x-tml-pillar: "GoukassianPromise"`** and **`x-tml-monograph-ref: "Section 2.3.2"`**.

The **`GET /gateway/lane-assignment`** endpoint returns a `LaneAssignmentStatus` containing `current_assignments` (object mapping payload types to lane endpoints), `capacity_utilization` (percentages by lane), and `health_status` (enum per lane: `["HEALTHY", "DEGRADED", "UNAVAILABLE"]`). This endpoint is annotated with **`x-tml-pillar: "GoukassianPromise"`** and **`x-tml-monograph-ref: "Section 2.2.1"`**.

The **`GET /gateway/fail-closed-status`** endpoint returns a `FailClosedStatus` containing `is_fail_closed` (boolean), `trigger_reason` (conditional enum: `["LANE_UNREACHABLE", "CONSTITUTIONAL_VIOLATION", "MANUAL_OVERRIDE", "EMERGENCY_ACTIVE"]`), `affected_lanes` (array), and `estimated_recovery_time` (conditional duration). This endpoint is annotated with **`x-tml-pillar: "SacredZero"`** and **`x-tml-monograph-ref: "Section 2.3.3"`**.

### 1.7 Webhooks and Callbacks

The TML API specification includes two critical webhooks that provide asynchronous notification of governance events, with detailed payload schemas, retry semantics, and idempotency requirements that ensure reliable delivery without duplicate processing.

#### 1.7.1 sacredPause.escalation

The **`sacredPause.escalation`** webhook fires when the Anchoring Lane determines that a proposed action triggers State 0 (Sacred Zero) and requires human review. The payload schema **`SacredZeroEscalationPayload`** contains: `escalation_id` (UUID, primary correlation identifier), `trigger_timestamp` (ISO 8601, when the escalation occurred), `trigger_source` (enum: `["INFERENCE_AMBIGUITY", "ANCHORING_REJECTION", "ADAPTIVE_THROTTLING", "MANUAL_OVERRIDE"]`), `proposed_action` (original inference proposal with full StateEnvelope), `uncertainty_metrics` (structured object with `entropy_score` [0.0-1.0], `confidence_interval` [lower, upper], `ambiguity_dimensions` [array of ambiguous factors]), `human_review_queue` (queue identifier with `queue_url` and `expected_review_time`), and `lantern_transition` (Lantern state before and after escalation).

Retry semantics specify **exponential backoff starting at 1 second, doubling to maximum 60 seconds, with maximum 5 attempts** and dead-letter routing to `POST /sacred-zero/escalation-fallback` after exhaustion. The **`x-tml-idempotency`** header is required on all delivery attempts, with idempotency keys valid for 24 hours. The webhook is annotated with **`x-tml-pillar: "SacredZero"`** and **`x-tml-monograph-ref: "Section 2.3.3"`**.

#### 1.7.2 lanternStatus.broadcast

The **`lanternStatus.broadcast`** webhook fires whenever the Lantern undergoes any state transition, providing public transparency into system moral status. Its payload schema is the full **`LanternStatus`** object, with the `signalBroadcast` field containing the parameters for public verification. Retry semantics specify **fixed 30-second intervals with maximum 3 attempts**, reflecting the lower criticality of beacon updates compared to Sacred Pause escalations. The **`x-tml-idempotency`** header is similarly required, with 24-hour key validity. This webhook is annotated with **`x-tml-pillar: "GoukassianPromise"`** and **`x-tml-monograph-ref: "Section 1.5"`**.

### 1.8 Schema Cross-References

The TML schema architecture uses **JSON Schema Draft 2020-12** with `$defs` for centralized definition and `$ref` for cross-referencing, ensuring single-source-of-truth for all type definitions. The `tml_schema.json` bundle contains all definitions, with the OpenAPI specification referencing them via external `$ref` pointers or through `components.schemas` proxies.

#### 1.8.1 Core Schemas

The **core schemas** form the decision and governance chain, with strict interdependencies that enforce constitutional constraints across the API surface:

| Schema | Purpose | Key Fields | References |
|:---|:---|:---|:---|
| `StateEnvelope` | Universal decision container | `current_state` (+1/0/-1), `state_label`, `permission_token` (conditional), `proposed_action` | `PermissionToken`, `JustificationObject` |
| `TSLF-State0` | Sacred Pause forensic log | `lantern_status`, `uncertainty_quantification`, `deliberation_matrix`, `resolution_request` | `LanternStatus` |
| `TSLF-State-1` | Refusal forensic log | `license_violation`, `threat_vector_analysis`, `chain_of_custody` | `LicenseValidationRequest` |
| `TSLF-State+1` | Proceed forensic log | `ethical_verification`, `the_signature`, `audit_proof` | `SignatureBlock` |
| `JustificationObject` | Inter-lane transport envelope | `decision_vector`, `proposed_state`, `uncertainty_metrics`, `mandate_vectors`, `signature_block` | `SignatureBlock` |
| `PermissionToken` | Cryptographic release key | `log_hash`, `epoch_timestamp`, `signer_key_id`, `lane_origin`, `signature` | `SignatureBlock` (implicit) |

The **`StateEnvelope`** schema serves as the root of this dependency graph, with `current_state` (+1, 0, -1) and conditional `permission_token` requirement as previously described. It references `JustificationObject` for the `proposed_action` field, ensuring that every state proposal carries the evidentiary foundation required for Anchoring Lane evaluation. The `JustificationObject` schema contains the original decision vector, the proposed state, uncertainty quantification metrics, and references to relevant mandate vectors (Human Rights, Earth Protection). It does not contain any credential or token that could shortcut the Anchoring Lane's evaluation. The Anchoring Lane treats the Justification Object as advisory input, performing its own independent analysis before rendering a governance decision.

The **TSLF schema variants** form the forensic record layer, with each state having a dedicated schema that captures state-specific evidentiary requirements. `TSLF-State0` requires `lantern_status` (Lantern state at log creation), `uncertainty_quantification` (structured ambiguity metrics), `deliberation_matrix` (array of considered alternatives with scoring), and `resolution_request` (object with `requiredReviewType`, `escalationPath`, `deadline`, `notifiedParties`). `TSLF-State-1` requires `license_violation` (object with `licenseId`, `violatedTerms`, `violationEvidence`), `threat_vector_analysis` (object with `threatCategory`, `severityScore`, `mitigationStatus`, `affectedParties`), and `chain_of_custody` (array of evidence references with `evidenceId`, `evidenceType`, `custodianId`, `timestamp`). `TSLF-State+1` requires `ethical_verification` (object with `verifiedPrinciples`, `verificationMethod`, `verifierIdentity`), `the_signature` (Anchoring Lane signature over the complete log), and `audit_proof` (Merkle inclusion proof with `merkleRoot`, `leafIndex`, `siblingHashes`).

#### 1.8.2 Supporting Schemas

The **supporting schemas** provide the infrastructure that enables core schema functionality:

| Schema | Purpose | Key Fields | Used In |
|:---|:---|:---|:---|
| `LanternStatus` | Public compliance beacon | `lanternState`, `lastTransition`, `signalBroadcast`, `pillarHealth` | `GET /gateway/lantern`, `lanternStatus.broadcast` webhook, `TSLF-State0` |
| `SignatureBlock` | Provenance and non-repudiation | `signatureValue`, `signerKeyId`, `signingTimestamp`, `signatureAlgorithm`, `signaturePurpose` | `JustificationObject`, `TSLF-State+1`, `PermissionToken` (implicit) |
| `LicenseValidationRequest` | Capability verification request | `licenseId`, `scopeVector`, `validityPeriod`, `revocationStatus` | `POST /license/validate`, `TSLF-State-1` |
| `LicenseValidationResponse` | Capability verification result | `validationResult`, `grantedScopes`, `expiryTimestamp`, `revocationProof` | `POST /license/validate` response |

The **`LanternStatus`** schema serves both as API response and webhook payload, with the properties previously described. The **`SignatureBlock`** appears embedded in multiple parent schemas, with algorithm agility that supports future PQC migration through the `signatureAlgorithm` enum extensibility. The **`LicenseValidationRequest`** and its response counterpart enable runtime capability verification that prevents unauthorized operation scope expansion. These supporting schemas carry the same `unevaluatedProperties: false` constraint as core schemas, ensuring that no implementation can introduce unstandardized extensions that might bypass constitutional enforcement.



