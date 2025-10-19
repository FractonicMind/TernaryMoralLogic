## TRADE SECRET ERASURE, Ethical Key Revocation, and TML

**Purpose.** Explain how Ternary Moral Logic reconciles immutable moral trace logs with legitimate trade secret and privacy claims, by destroying decryption keys rather than deleting anchored records. This document describes the legal rationale, technical design, custody model, judicial workflow, and implementation checklist required to operate Ethical Key Revocation, EKR, in compliance with GDPR Article 17 and the EU Trade Secrets Directive 2016/943.

---

## Summary

TML’s Moral Trace Logs are permanent, schema-verified records of ethically consequential decision points. To protect intellectual property and personal data while preserving accountability, TML implements Ethical Key Revocation (EKR). EKR renders logged content permanently unreadable by securely destroying decryption keys or their quorum shares, while preserving on-chain hashes and timestamps as immutable proof that the event occurred. The public keeps proof, the secret stays sealed.

---

## Legal Foundation

1. **GDPR, Article 17.** Effective erasure can be satisfied by rendering data inaccessible, including through secure cryptographic techniques, where full deletion is impractical while a legal necessity to retain provenance exists.
2. **EU Trade Secrets Directive 2016/943.** Protects information that has commercial value from being disclosed, while not preventing legitimate public interest or judicial discovery under due process.
3. **Evidentiary Law.** Public anchoring of hashes and time stamps establishes tamper-evident provenance; judicial mechanisms govern conditional access, see `COURT_ORDER_TEMPLATE.md`.

---

## Principles

* **Proof without disclosure.** Preserve auditable proof of ethical events, avoid reconstructing proprietary methods.
* **Separation of existence and content.** On-chain and public records prove an event, keys control content.
* **Institutional custody with distributed trust.** Keys are split across independent custodians to prevent unilateral disclosure.
* **Due process gate.** Courts or authorized tribunals may compel limited decryption under strict procedures; otherwise keys may be revoked.
* **Minimal disclosure.** If decryption is authorized, return only the smallest necessary redaction set consistent with the judicial order.

---

## Technical Design (high level)

1. **Encryption Standard.** Logs are encrypted at rest using AES-256 GCM, per modern cryptographic best practice.
2. **Key Management.** A master symmetric key encrypts each log or log batch, keys are themselves split via **Shamir Secret Sharing** into N shares, with a quorum threshold Q (e.g., N=7, Q=5).
3. **Anchoring.** Each encrypted log produces a SHA-256 hash and timestamp, these are anchored to a public blockchain and/or OpenTimestamps. The anchor records log identifier, schema version, and custody metadata.
4. **Custodianship.** Key shares are held by independent custodians, a mix of public institutions, neutral NGOs, academic mirrors, and a hardware security module service. No single custodian can reconstruct a key.
5. **Audit Trail.** All key share operations are logged in a separate, auditable ledger, themselves hashed and anchored. Custodian actions require multi-party signatures and follow `SIGNATURE_PROCEDURE.md`.

---

## EKR Workflow

1. **Normal Operation.** System writes Moral Trace Log, encrypts with AES-256, anchors hash to chain, stores encrypted payload in custody. Key shares distributed.
2. **Privacy or Trade Secret Claim.** Claim submitted to custodian portal, claim tagged with justification, reference to anchored hash. See `CONFIDENTIAL_DISCLOSURE_POLICY.md`.
3. **Quorum Review.** Custodians validate the claim against statutory criteria, or forward to an independent review panel if contested. If claim is validated, execute one of two actions:

   * **Revocation:** destroy key shares irrevocably, document the destruction, publish revocation tombstone anchored on-chain; the encrypted payload remains but is mathematically unreadable.
   * **Escrowed Decryption:** if a court order requires access, custodians follow `COURT_ORDER_TEMPLATE.md`, securely reconstruct keys under court supervision, decrypt only the minimal content required, produce redacted extract, then re-encrypt remaining content under new keys and reanchor.
4. **Post-Revocation Audit.** Anchor a revocation proof, publish metadata: revocation time, responsible custodian signatures, legal citation, redaction summary. The hash chain proves existence and revocation integrity.

---

## Judicial and Procedural Controls

* **Court Order Standard.** Use `COURT_ORDER_TEMPLATE.md` to request decryptive access. Orders should specify scope, minimality, protective measures, and destruction or resealing rules.
* **Emergency Protocol.** For immediate public safety threats, an emergency quorum process activates, with a mandatory post facto judicial review.
* **Appeal and Oversight.** A neutral oversight panel adjudicates disputed claims between custodians and claimants, its decisions are public and anchored.

---

## Admissibility and Evidence Strategy

* Maintain anchored hash plus notarized custody receipts, chain of custody metadata, and anchor proofs to satisfy evidentiary standards such as FRE 902(13) and EU equivalents. Hash plus custody receipt proves the log existed at time T, revocation proves it was intentionally sealed thereafter.

---

## Threats and Mitigations

* **Custodian collusion.** Use geographically, institutionally, and legally diverse custodians; require hardware security modules; rotate custodians with anchored proofs.
* **Key leakage.** Enforce hardware-backed keys, strict access controls, split-key thresholds, frequent audits.
* **Legal capture.** Maintain public transparency of revocation metadata, use multi-jurisdictional custodians to prevent single-jurisdiction coercion.

---

## Implementation Checklist

* [ ] Define N and Q for Shamir sharing, pick custodians.
* [ ] Implement AES-256 GCM encryption pipeline, schema version control.
* [ ] Integrate OpenTimestamps and blockchain anchoring for hash proofing.
* [ ] Create custodian onboarding contract templates, service level agreements.
* [ ] Publish `CONFIDENTIAL_DISCLOSURE_POLICY.md` and `COURT_ORDER_TEMPLATE.md`.
* [ ] Run third-party crypto and legal audits, publish redacted executive summary.
* [ ] Test full revocation cycle in staging, anchor all steps.

---

## Cross references

Related files:

* `README.md` in `main/legal_provisions/`
* `COURT_ORDER_TEMPLATE.md`
* `EVIDENCE_CHAIN_GUIDE.md`
* `LEGAL_SUMMARY.md`
* `MOTION_STRUCTURED_LOGGING.md`
* `../Hybrid_Shield.md`
* `../Privacy_Safety.md`
* `../MANDATORY.md`

---

## Short legal paragraph for license and downstream users

Use with the TML license: Implementation of EKR does not waive trade secret protection, it operationalizes lawful secrecy while preserving public provenance. Any custodian or implementer must accept the `Goukassian Promise` clauses relevant to custody conduct and publication of revocation metadata.

---

## Sample revocation tombstone (public metadata)

```
{
  "log_id": "tml-log-2025-07-21-0001",
  "anchor_hash": "sha256:3e7ed2bff6a115b...afe55",
  "revocation_time": "2025-10-13T21:39:18Z",
  "revocation_reason": "Validated trade secret claim under Directive 2016/943; GDPR art 17 invoked",
  "custodian_signatures": ["org1.sig","org2.sig","org3.sig"],
  "court_reference": "EU-T/2026/045",
  "note": "Content sealed, tombstone proven, content inaccessible."
}
```
---

Created by Lev Goukassian * ORCID: 0009-0006-5966-1243 *  
   Email: leogouk@gmail.com  
   Successor Contact: support@tml-goukassian.org  
   [see Succession Charter](/TML-SUCCESSION-CHARTER.md)

---

## Glossary

Define EKR, AES-256, Shamir, anchor, tombstone, custodian, quorum, revocation, moral trace log.

