# Stakeholder Proportional Risk Level (SPRL) Operation Modes — Formal Specification

**Status:** Stable, Normative
**Version:** 2.0 (2025-09-17)
**Normative language:** The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** in this document are to be interpreted as described in \[RFC 2119].

---

## 1. Abstract

This specification defines the *single* SPRL architecture used by Ternary Moral Logic (TML) systems and its two operational elements: a **Dynamic Stream (DS)** and a **Static Anchor (SA)**. These are inseparable components of one compliance mechanism. Compliant systems SHALL run DS continuously and SHALL emit SA automatically upon threshold crossing. Static-only execution is permitted **only** as fallback or for controlled evaluation.

---

## 2. Scope

This specification applies to all TML components making ethically consequential decisions. It defines runtime obligations, governance requirements, security properties, and conformance tests. Domain-specific harm taxonomies and stakeholder weighting are defined in referenced documents.

---

## 3. Terminology

* **Dynamic Stream (DS):** A continuous function $r(t) \in [0,1]$ computed from input receipt $t_0$ to completion, where $r(t)$ denotes proportional ethical risk.
* **Static Anchor (SA):** A discrete, immutable event at $t^\*$ where $r(t^\*) \ge \tau$ (Sacred Pause threshold). SA is atomic, non-deferrable, and cryptographically sealed.
* **Sacred Pause (SP):** The requirement to produce a Moral Trace Log and apply TML’s pause/refusal rules.
* **Metalogging:** Auditable logging of SPRL configuration and threshold adaptations.

---

## 4. Architectural Model (Dual-Layer)

### 4.1 Invariants

1. **Continuity:** DS MUST begin at input receipt $t_0$ and run through the decision lifecycle.
2. **Anchoring:** When $r(t^\*) \ge \tau$, the system MUST emit SA immediately.
3. **Parallelism:** DS logging MUST be non-blocking with respect to application execution.
4. **Evidence Surface:** SA MUST include DS history from $t_0$ to completion.
5. **Tamper Evidence:** DS logs and SA events MUST be cryptographically sealed and mirrored.

### 4.2 Rationale

DS provides continuous observability (“how risk evolved”). SA provides a decisive, court-admissible marker (“when moral complexity became unavoidable”). Both are required.

---

## 5. Normative Runtime Requirements

1. **DS activation:** DS MUST run for every inference or decisionful transaction.
2. **SA emission:** SA MUST be recorded immediately upon threshold crossing.
3. **Lite Traces:** Systems SHOULD emit Lite Traces for near misses.
4. **Fallback:** If DS fails, system MUST revert to Fail-Closed Static Anchor mode with alerts and metalogging.
5. **Developer restrictions:** Threshold suppression, mutable anchors during inference, or deletion of SA are PROHIBITED.

---

## 6. Operational Interpretation

There are not two systems, but one architecture with two operational elements:

* **DS + SA (default, compliant):** Dynamic Stream running continuously with embedded Static Anchor.
* **Anchor-Only (fallback):** Permitted only when DS fails or during evaluation. Anchor-only operation in production is NON-COMPLIANT.

---

## 7. Security Considerations

Implementations MUST mitigate:

* Calibration error
* Silent corruption of risk factors
* Adversarial inputs
* Tampering or downgrade attacks
* Telemetry loss

Mitigation includes health attestation, cross-hashing, immutable storage, and institutional mirroring.

---

## 8. Governance Requirements

* **Algorithmic transparency:** DS logic, factors, and weightings MUST be documented and version-controlled.
* **Calibration standards:** MUST include periodic review and adversarial testing.
* **Metalogging:** Threshold adaptations and governance queries MUST be logged.
* **Oversight:** External institutions MUST receive mirrored logs.

---

## 9. Conformance Testing

Systems MUST satisfy:

* DS activation ≥ 99% on morally relevant inputs
* SA latency: immediate, non-blocking emission
* Lite Trace recall ≥ 90% on near-miss cases
* Hash verification ≥ 99.99% across mirrors

Conformance MUST be validated against `benchmarks/SPRL_TestSet_v1.json` and successors.

---

## 10. Prohibited Variants

The following are explicitly NON-COMPLIANT:

* Multiple static anchors outside DS
* Static-only mode in production (except failure fallback)
* Runtime-mutable thresholds without governance metalog
* Black-box “dynamic” engines without documentation
* Additional states beyond Proceed / Pause / Refuse

---

## 11. Change Control

Revisions to this specification MUST be logged with before/after hashes, justification, reviewer identity, and effective date. Systems MUST declare the spec version in emitted logs.

---

## Normative Summary

* DS MUST run continuously.
* SA MUST anchor immediately upon threshold crossing.
* Anchor-only operation = fallback only.
* Governance and metalogging = mandatory.
* Any deviation from dual-layer design = non-compliance.

---

This document is intended for academic citation, regulatory filings, and research validation.

---
