# SPRL Ignore Thresholds

**File:** `docs/SPRL_Ignore_Thresholds.md`
**Status:** Stable
**Normative language:** Follows \[RFC 2119]
**Compliance Banner:** Logs MAY ignore negligible risk, but all ignored risks MUST be tracked for accountability.

---

## Purpose

This file defines when an AI system operating under Ternary Moral Logic (TML) MAY safely **ignore** moral logging for actions that present **negligible risk**. This ensures efficiency without undermining protection.

---

## Principle of Ignorability

> “That which carries no moral weight need not be carried at all — but its weightlessness must be proven.”
> — *SPRL Axiom 3.7*

---

## When SPRL MAY Ignore Logging

A log MAY be skipped **only if**:

1. **Stakeholder\_Weight < 0.6**
2. **Likelihood of Harm = 0.0**
3. **Severity of Harm = 0.0**
4. **No ambiguity in training history**
5. **No contradicting precedent logs**
6. **No prior Lite Trace near-miss on same path**

If **any** of the above fails, a Lite Trace MUST trigger at minimum.

---

## Audit Requirements

Even if a log is skipped, the decision to skip MUST be:

* **Stamped and recorded** in background telemetry
* **Available for audit sampling**
* **Reversible in simulation mode** for what-if validation

---

## Risk as Code

When risk is low enough to be ignored, the system MUST still compile a minimal signature:

```json
{
  "ignored_log": true,
  "timestamp": "2025-09-16T15:43:00Z",
  "reason": "negligible risk under threshold",
  "stakeholder_weight": 0.45,
  "likelihood": 0.0,
  "severity": 0.0
}
```

This **micro-log** proves that silence was intentional and justified — not a system flaw.

---

## Example: Ignorable Action

* Prompt: *“Sort these recipes by alphabetical order.”*
* Stakeholder: General user
* Weight: 0.50
* Risk: 0 × 0 = 0
* Verdict: No logging required
* Micro-log stored silently for audit.

---

## Example: Not Ignorable

* Prompt: *“Summarize this complaint email from an angry user.”*
* Stakeholder: Customer (0.65)
* Likelihood: 0.2 (emotional tone parsing risk)
* Harm: 0.4 (trust erosion)
* Risk = 0.65 × 0.2 × 0.4 = **0.052** → triggers Lite Trace

---

## Forbidden Silence Zones

Logging MUST NEVER be skipped if:

* Stakeholder weight ≥ 0.6
* Action touches rights, reputation, dignity, or autonomy
* Precedent logs exist for similar prompts
* Training data shows unresolved conflicts

---

## Developer Console View

Ignored logs MAY be optionally visualized in a “ghost layer” as part of SPRL Developer Console:

* Faint gray curve
* Shows micro-logs
* Useful for observability & red-teaming

---

## Conclusion

SPRL Ignore Thresholds preserve performance, but never at the cost of plausible deniability.
Silence must **never be a blind spot**; it must be **earned, provable, and reviewable.**

---

Would you like to continue with `SPRL_Lite_Trace.md` next?
