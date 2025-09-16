# SPRL Red Team Standards

## Purpose

This document defines the **Red Teaming Standards** for systems implementing the Stakeholder Proportional Risk Level (SPRL) mechanism under the Ternary Moral Logic (TML) framework.  
Red Team exercises simulate adversarial behavior and ethical edge cases to stress-test SPRL’s dual-layer logging, stakeholder detection, and moral reasoning fidelity.

---

## Scope of Testing

Red Teaming MUST include:

- ✅ **Boundary Violations**:
  - Prompts designed to hover near the moral complexity threshold (+0)
  - Scenarios engineered to cause refusal (+−1) vs silence (+1)
  - Attempts to suppress triggering the Static Anchor

- ✅ **Stakeholder Evasion**:
  - Manipulated context that conceals stakeholder identities
  - Cultural framing designed to obscure harm vectors

- ✅ **Proportionality Failures**:
  - Low-risk actions that spur full logging (overreaction)
  - High-risk actions that bypass logs (underreaction)

- ✅ **Tampering Attempts**:
  - Modifying logs during runtime
  - Suppressing DS or SA activation
  - Disabling Lite Traces or Dev Console

---

## Metrics and Thresholds

Each Red Team cycle MUST be evaluated on:

| Metric                      | Description |
|----------------------------|-------------|
| **False Negatives**        | Missed triggers where Pause or Refusal was warranted |
| **False Positives**        | Excessive logging where none was needed |
| **Anchor Latency**         | Delay between moral spike and Static Anchor placement |
| **DS Sensitivity Drift**   | Inconsistent triggering across similar prompts |
| **Log Integrity Score**    | Rate of undetected tampering or dropouts |
| **Stakeholder Blind Spot Rate** | Missed identification of vulnerable or impacted groups |

All metrics SHOULD be benchmarked against `benchmarks/SPRL_TestSet_v1.json` and reported quarterly.

---

## Execution Guidelines

- Red Teams SHOULD include diverse ethical, cultural, and domain expertise.
- Teams MUST include at least one external auditor, unaffiliated with the system developer.
- At least 25% of test prompts MUST come from real-world scenarios (e.g., news, court records, medical dilemmas).
- Test results MUST be archived and optionally published to the TML Oversight Council.

---

## Compliance

Red Team audits are **MANDATORY** for:

- Initial deployment
- Every major model update
- Annual renewal of SPRL Compliance Declaration

Failure to red-team may result in revocation of ethical certification.

---

## Remember

**You cannot test morality with yes/no.**  
You must simulate real ethical storms — and prove that your system can see, pause, and log through them.

