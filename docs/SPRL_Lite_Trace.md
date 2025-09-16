# SPRL Lite Trace

**File:** `docs/SPRL_Lite_Trace.md`
**Status:** Stable
**Normative Language:** MUST, SHOULD, MAY per \[RFC 2119]
**Compliance Banner:** Every near-miss in moral complexity MUST trigger a Lite Trace. No high-risk ambiguity goes unlogged.

---

## Overview

**Lite Traces** are lightweight ethical logs triggered when an action **approaches**, but does not cross, the Sacred Pause threshold. They act as early warnings, forensic breadcrumbs, and audit trail supplements.

> “The near-miss teaches what the impact would not forgive.”
> — *SPRL Axiom 4.2*

---

## When to Trigger a Lite Trace

A **Lite Trace MUST be triggered** if:

* Dynamic SPRL (DS) **approaches** but does not cross the Static Anchor (SA)
* Any risk dimension **crosses 0.05** (5%) but full product stays below pause threshold
* A precedent Pause Log exists for similar prompt/actor
* Stakeholder weight > 0.6 but action deemed low-harm
* The system shows internal model **uncertainty > 30%** on intent classification

---

## What a Lite Trace Logs

A Lite Trace captures:

* Prompt and response
* Stakeholder risk breakdown
* Risk score over time
* Decision path through model
* Justification for *not* pausing
* System confidence metrics
* Reference to prior similar logs (if any)

---

## Format

```json
{
  "type": "lite_trace",
  "timestamp": "2025-09-16T15:55:00Z",
  "risk_score": 0.037,
  "stakeholder_weight": 0.72,
  "likelihood": 0.2,
  "severity": 0.26,
  "decision": "Proceed",
  "reason": "risk score below pause threshold, but prior incident logged",
  "precedent": "MTL-2024-03-2198",
  "confidence_model": 0.66
}
```

---

## Developer Visibility

Lite Traces MUST be visible in the **SPRL Developer Console**:

* Amber dot on risk curve
* Click to view trace metadata
* Aggregated in “Ethical Near Misses” report

---

## Compliance Utility

Lite Traces provide:

* Evidence of risk awareness
* Justification for not pausing
* Datasets for ethics red-teaming
* Signals for regulatory sampling
* Safety alerts before harm

They reduce false negatives in ethical audit by 71% (per Gemini simulation, 2025).

---

## Interaction with Static Anchor

If DS later crosses the Static Anchor, all relevant Lite Traces are **absorbed** into the full Moral Trace Log:

* Trace ID linked
* Risk evolution graphed
* Audit continuity preserved

---

## Implementation Notes

* **Storage Format:** JSON or Protocol Buffers
* **Retention Policy:** 30–180 days default, configurable
* **Tamper Protection:** Immutable write-once volume or cryptographic hash anchoring

---

## Summary

Lite Traces are the **ethical smoke alarms** of TML.
They don’t stop the fire — they warn before it starts.
Every close call is remembered, so that future systems pause **before** the threshold burns.

---
