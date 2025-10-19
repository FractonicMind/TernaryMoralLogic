# CONFIDENTIAL DISCLOSURE POLICY

## Purpose

Define the lawful, auditable process for disclosing encrypted Moral Trace Logs or their metadata to authorized parties under Ternary Moral Logic (TML).
This policy ensures transparency without unauthorized exposure, balancing privacy, trade-secret law, and public accountability.

---

## Scope

Applies to:

* All custodians and operators holding encrypted Moral Trace Logs.
* Any institution requesting access to such logs under court order, regulatory audit, or verified public-interest claim.
* All disclosure events executed through the Ethical Key Revocation (EKR) framework.

---

## Legal Foundation

1. **GDPR, Articles 6, 9, 17, 23** – Disclosure may occur only when mandated by law or overriding public interest; erasure obligations satisfied by key destruction after access window closes.
2. **EU Trade Secrets Directive 2016/943** – Permits disclosure of protected information when necessary for legitimate whistleblowing, judicial proceedings, or protection of public welfare.
3. **Evidentiary Rules (FRE 902(13), EU eIDAS)** – Hash and timestamp proofs maintain evidentiary validity even when content is redacted.

---

## Disclosure Principles

* **Necessity:** Only disclose when required by statutory authority or to prevent demonstrable harm.
* **Proportionality:** Reveal the minimal segment of data sufficient for the lawful purpose.
* **Custodial Consensus:** At least the quorum Q of custodians must co-sign the disclosure event.
* **Temporal Sealing:** All disclosed material must be re-encrypted or key-revoked after the legal purpose is fulfilled.
* **Auditability:** Every disclosure, reason, custodian signature, and hash must be anchored publicly.

---

## Standard Workflow

1. **Request Submission** – Authorized requester (court, regulator, certified investigator) submits signed digital request citing legal basis, targeted log ID, and justification.
2. **Verification Phase** – Custodians verify credentials and jurisdictional authority; ambiguous cases escalated to the Oversight Panel.
3. **Controlled Decryption** – If approved, quorum reconstructs decryption key within an isolated hardware enclave; only necessary fragments are read.
4. **Delivery Phase** – Decrypted content or analytical excerpt transmitted via encrypted channel; chain-of-custody signed and logged.
5. **Resealing Phase** – After statutory window expires, content re-encrypted under new key or key shares destroyed; tombstone metadata anchored on-chain.
6. **Publication of Disclosure Metadata** – A public record lists: log ID, requester type, legal citation, date/time, and confirmation that proportionality and resealing were performed.

---

## Emergency Procedure

In life-threatening or large-scale ecological harm scenarios:

* Two custodians plus one judicial authority may authorize immediate access.
* Disclosure must be retroactively validated within 72 hours.
* All actions logged and anchored with the “Emergency” flag in `EVIDENCE_CHAIN_GUIDE.md`.

---

## Custodian Obligations

* Maintain tamper-proof audit logs of every disclosure event.
* Conduct quarterly compliance audits with independent cryptographic attestation.
* Report aggregate disclosure statistics publicly at least once per year.

---

## Violations & Sanctions

* Unauthorized disclosure → Tier 3 penalty under `SANCTIONS_AND_PENALTIES.md`.
* Failure to reseal or destroy keys after disclosure → Tier 4 penalty, immediate custodian suspension.
* Knowingly false or malicious disclosure request → referral to criminal authorities.

---

## Cross-References

* `TRADE_SECRET_ERASURE.md` – Key-revocation process
* `COURT_ORDER_TEMPLATE.md` – Judicial authorization form
* `EVIDENCE_CHAIN_GUIDE.md` – Logging and anchoring format
* `LEGAL_SUMMARY.md` – High-level policy index
* `MANDATORY.md` – Compliance requirements

---

## Closing Clause

This policy ensures that secrecy and accountability coexist within measurable bounds.
Proof remains public; content remains protected; conscience remains visible.

Even when words are hidden, the light behind them must still be provable.
