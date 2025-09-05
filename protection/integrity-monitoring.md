# Ternary Moral Logic — Integrity Monitoring System  
**Technical Protection and Legal-Grade Evidence**

**Author:** Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Contact:** leogouk@gmail.com  
**Framework:** Ternary Moral Logic for Ethical AI Decision-Making  
**Protection Level:** Court-grade integrity with creator attribution preserved  

---

## 1. Purpose and Scope
This specification defines how TML produces **court-grade Moral Trace Logs** and protects their integrity against adversaries.  
It sets the evidentiary floor: **immutability**, **origin**, **time**.  

**What TML demands:** verifiable evidence for ethically significant decisions.  
**What TML does not demand:** model choice, workflow design, or business methods.  

---

## 2. Integrity Guarantees
Every log entry must satisfy:  
1. **Immutability** — append-only chaining with tamper evidence.  
2. **Non-repudiation** — digital signatures bind entry to the authorized monitor.  
3. **Independent time** — trusted timestamps from external authorities.  

Failures must trigger **signed control records**, making outages visible.  

---

## 3. Threat Model
Adversaries may attempt to:  
- Suppress, forge, reorder, or flood logs.  
- Manipulate SPRL thresholds (*threshold gaming*).  
- Launch denial-of-service on TSA or storage.  
- Extract signing keys via side-channels.  
- Use supply-chain backdoors.  
- Exploit “silence” (no logs) to weaken trust.  

**Defense principle:** every attempt leaves forensic evidence.  

---

## 4. Architecture
- **Integrity Monitor**  
  - Builds chained entries, signs, timestamps, anchors.  
  - Runs inside TEE/HSM with attestation.  

- **Risk Trigger**  
  - Computes SPRL, compares thresholds, emits metadata.  
  - Shadow models may cross-check to detect gaming.  

- **Attribution & License**  
  - Enforced by signed manifests and licensing.  
  - Kept outside the monitor’s trust boundary.  

---

## 5. Canonical Log Schema
```json
{
  "seq": 18421,
  "prev_hash": "b0c5...e7",
  "ts_local": "2025-09-05T10:42:03.412Z",
  "event": "sacred_pause",
  "system_id": "org.acme.triage.v3",
  "decision_id": "0f2a3f1c-7f0a-4dbe-9e2a-7f5e1a",
  "sprl": 0.742,
  "threshold": 0.70,
  "context_hash": "9f14...aa",
  "entry_hash": "sha256(canonicalized_record_without_sig)",
  "sig": "base64(Ed25519_sig(entry_hash))",
  "key_id": "signing-key-2025Q3",
  "tsa_tokens": [
    "RFC3161-base64-token-1",
    "RFC3161-base64-token-2"
  ]
}
````

---

## 6. Chain and Storage

* **Append-only ledger:** write once, never modify.
* **Rollovers:** fixed-size files, each ends with a Merkle root.
* **Anchoring:** publish Merkle roots to council mirrors or private chain.
* **Redundancy:** at least two physical sites; offline snapshots.
* **Verification:** rebuild chain and validate every link.

---

## 7. Time Anchoring

* Use **two independent RFC-3161 TSAs** per entry.
* If both fail, queue entries locally and emit signed `tsa_unavailable` control records every 30s.
* Backfill TSA tokens once connectivity returns.

---

## 8. Keys and Attestation

* **Signing key:** Ed25519/ECDSA P-256, held in TEE/HSM.
* **Rotation:** quarterly rotation with public key registry + revocation list.
* **Attestation:** auditors can verify running binary + config via remote attestation.
* **Separation:** signing keys distinct from encryption keys.

---

## 9. Heartbeats, Floods, and Backpressure

* **Heartbeat:** signed every 30s with queue depth + TSA status. Missing heartbeats = evidence.
* **Aggregation:** low-risk routine decisions batched with Merkle root.
* **Rate control:** randomized micro-thresholds, per-principal caps, dampening for threshold oscillation.
* **Backlogs:** emit signed `backpressure` control records; never drop silently.

---

## 10. SPRL Transparency

* Publish methodology for stakeholder impact, vulnerability weights, probability.
* Log config updates as signed `risk_config_update` records.
* Encourage external review bodies to certify domain-specific profiles.

---

## 11. Supply Chain Integrity

* Reproducible builds, signed releases, dependency pinning.
* No dynamic code loading in the monitor.
* On startup: signed `monitor_started` record with binary + config hash.

---

## 12. Control Records

The monitor must issue structured control records for anomalies:

* `monitor_started` — binary + config hash, attestation data.
* `key_rotation` — old/new key IDs, reason.
* `tsa_unavailable` — TSA IDs, queue size.
* `backpressure` — queue depth, aggregation policy.
* `storage_rollover` — Merkle root, anchor reference.
* `anomaly_detected` — IDS evidence, severity.

---

## 13. Compliance and Metrics

Auditors must see:

* Chain continuity, last valid `seq`.
* Heartbeat cadence, TSA availability, anchors.
* Sacred Pause and Prohibit distributions.
* Queue depth and aggregation counts.
* Config change history.

Reports must be computed from live data — no hardcoded scores.

---

## 14. Privacy and Minimization

* Logs contain hashes, not raw sensitive data.
* Use AEAD (AES-GCM / XChaCha20-Poly1305) for encrypted payloads.
* Tiered release model: routine audits use proofs, investigations request payloads.
* Zero-knowledge proofs optional for completeness checks.

---

## 15. Governance and Oversight

* **Council custody:** 11 institutions mirror roots and verify anchors.
* **Access:** auditors use proofs + metadata; full content needs authorization + custody receipts.
* **Legal clause:** *missing logs create a **rebuttable presumption of guilt*** unless signed outage/control records prove external interference.

---

## 16. Reference Workflow

1. AI proposes decision.
2. Risk Trigger computes SPRL → classify event.
3. Monitor builds entry, signs, timestamps, anchors.
4. Store entry append-only, advance `seq`.
5. Emit heartbeat every 30s.
6. Anchor Merkle root at rollover or interval.
7. Failures → signed control records.

---

## 17. Creator Attribution

Attribution is enforced via signed manifests:

```
Ternary Moral Logic Framework
Creator: Lev Goukassian, ORCID 0009-0006-5966-1243
Contact: leogouk@gmail.com
This implementation preserves the Sacred Pause principle for intelligent moral decision-making.
```

---

## 18. Validation Checklist

Before deployment:

* Chain continuity verified across rollovers.
* Signatures validate against all keys.
* TSA tokens verified; anchors validated.
* Heartbeats present; outages explained.
* Risk configs logged and signed.
* Attestation matches published binary.

---

## 19. Legal Notes

* Tampering or forged entries = obstruction of justice.
* Threshold gaming = deceptive practice (fraud).
* Due process preserved through **rebuttable presumption** and control records.

---

## 20. Rationale

* **XAI explains, TML proves.**
* Gaps are not weakness; they are evidence.
* Adversarial pressure leaves fingerprints.
* Mandatory logs flip incentives: hiding risk costs more than fixing it.

---

## 21. Status

**Creator:** Lev Goukassian
**Integrity level:** Court-grade
**Legacy preservation:** Active and verifiable

*"Truth that can be verified is a public good. TML makes it non-optional."*

```
