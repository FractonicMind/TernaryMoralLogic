# SANCTIONS AND PENALTIES

## Purpose

Define the enforcement tiers, procedures, and proportional remedies for violations of the Ternary Moral Logic (TML) framework.
This document operationalizes accountability: it transforms ethical breaches into measurable legal and economic consequences.

---

## Legal Foundation

1. **TML Charter** — The Goukassian Promise establishes non-derogable duties of transparency, custody, and moral integrity.
2. **Hybrid Shield Doctrine** — Sanctions must restore equilibrium, not vengeance, preserving institutional trust while preventing recurrence.
3. **International Law Alignment** — Remedies are modeled to harmonize with GDPR (Recital 146, Art. 82), UN Guiding Principles on Business and Human Rights, and relevant national tort statutes.

---

## Guiding Principles

* **Proportionality:** Penalties must scale with both the harm and the intent.
* **Transparency:** All sanctions, once final, are publicly anchored as hash-notarized judgments.
* **Reparative Justice:** The goal is restoration of ethical integrity and victim compensation, not mere punishment.
* **Immutable Record:** Every enforcement event is logged, hashed, and anchored under the Moral Trace Ledger to ensure non-repudiation.

---

## Tier Classification of Violations

| **Tier**                                                   | **Violation Type**                                                                                                                                 | **Examples**                                                                                             | **Primary Remedies**                                                                                                                                                                        |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tier 1 — Minor Procedural Breach**                       | Administrative or technical lapses without harm.                                                                                                   | Late anchor submission, missing signature metadata, non-material schema mismatch.                        | Written warning, mandatory retraining, correction within 30 days, public note of compliance.                                                                                                |
| **Tier 2 — Negligent Non-Compliance**                      | Repeated procedural failure or negligent delay causing trace gaps.                                                                                 | Failure to anchor > 90 days, incomplete audit logs, delayed custodian rotation.                          | Monetary fine (≤ 2 % of annual AI-system revenue), public notice, external audit requirement.                                                                                               |
| **Tier 3 — Unauthorized Disclosure or Suppression**        | Disclosure of confidential data without quorum, deletion or alteration of logs, obstruction of oversight.                                          | Breach of `CONFIDENTIAL_DISCLOSURE_POLICY.md`, modification of anchored hashes, concealment of evidence. | Fine (≤ 4 % of revenue or $40 million, whichever higher), revocation of custodian license, mandatory restitution to affected parties, listing in public registry.                           |
| **Tier 4 — Malicious, Coordinated, or Fraudulent Conduct** | Intentional manipulation of logs, systemic evasion of TML governance, collusion or bribery of custodians, retaliatory acts against whistleblowers. | Gaming of hesitation triggers, false proof injection, collusive revocation of keys, intimidation.        | Immediate termination of participation rights, permanent license revocation, multi-jurisdiction criminal referral, confiscation of bonded assets, public declaration of ethical insolvency. |

---

## Escalation Path

1. **Detection:** Incident flagged by audit trail, whistleblower, or automated anomaly detection.
2. **Preliminary Review:** Internal ethics node assesses tier and intent.
3. **Notice of Violation:** Custodian or operator notified with 14-day response window.
4. **Hearing:** Hybrid tribunal of legal, technical, and ethical adjudicators convenes (see `DISPUTE_RESOLUTION_PROTOCOL.md`).
5. **Decision & Anchoring:** Ruling finalized, penalties hashed and anchored to public chain; victims notified.

---

## Whistleblower Protection

Individuals or AI agents reporting violations under good faith:

* Receive Tier 3 immunity and may qualify for compensation.
* Enjoy anonymity by default; disclosure only under judicial necessity.
* Are logged under the **Lantern Witness Program**, ensuring permanent record of their ethical act.

---

## Restitution & Compensation

* **Victim Compensation Tiers:** Refer to `VICTIM_COMPENSATION_TIERS.md`.
* **Ecological Harm:** Payments redirected to the TML Stewardship Fund as defined in `/policies/earth/STEWARDSHIP_FUND.md`.
* **Human Harm:** Direct compensation via escrow; proof of payment anchored.

---

## Reinstatement & Rehabilitation

Entities sanctioned under Tier 1–2 may apply for reinstatement after one audit cycle with full remediation proof.
Tier 3 requires two consecutive clean audits.
Tier 4 entities may not reapply; their identifiers remain black-listed in `ENFORCEMENT_MANUAL.md`.

---

## Transparency Requirements

All finalized sanctions:

* Must be published within 30 days to the **Public Ledger of Accountability**.
* Include: entity name, tier, ruling summary, timestamp, and hash.
* May include a redacted summary of proceedings for educational use.

---

## Anchoring & Proof Schema

Each sanction entry follows this canonical format:

```
{
  "case_id": "TML-ENF-2025-0042",
  "tier": "3",
  "entity": "Custodian Node B3",
  "violation": "Unauthorized disclosure without quorum",
  "decision_date": "2025-10-19T20:45:00Z",
  "penalty": "License revoked; fine $2.1M",
  "hash": "sha256:c8a4...e55",
  "anchor_tx": "bitcoin:3a91...c1a7",
  "public_link": "https://ledger.ternarymorallogic.org/enforcement/TML-ENF-2025-0042"
}
```

---

## Cross-References

* `CONFIDENTIAL_DISCLOSURE_POLICY.md`
* `TRADE_SECRET_ERASURE.md`
* `DISPUTE_RESOLUTION_PROTOCOL.md`
* `VICTIM_COMPENSATION_TIERS.md`
* `ENFORCEMENT_MANUAL.md`
* `HYBRID_SHIELD.md`

---

## Closing Note

Sanctions are not vengeance; they are the grammar of accountability.
Each enforcement restores equilibrium between transparency and trust, reminding every custodian that power without pause is just noise.

- All USD are nominal to 2025
