# SPRL Operation Modes

## Introduction

This document defines the two sanctioned operation modes of the Stakeholder Proportional Risk Level (SPRL) mechanism under the Ternary Moral Logic (TML) framework: **Static Anchor (Core)** and **Dynamic Stream (Adaptive)**. Both modes operate within a unified architecture, guaranteeing compliance, accountability, and forensic transparency. They differ only in the method of proportional risk assessment and the scope of log generation.

No other SPRL variants are authorized. Any deviation or redefinition constitutes noncompliance and must be explicitly designated as experimental.

---

## 1. Static Anchor (SA): TML Core

### Definition

The Static Anchor mode represents the baseline implementation of SPRL. It relies on a fixed, calibrated threshold to determine when the Sacred Pause must be invoked and a Moral Trace Log created.

### Characteristics

* **Emission Requirement**: The anchor is written immediately when the threshold is crossed. This process is non-blocking and does not delay model performance.
* **Immutable Threshold**: A single proportional risk threshold is defined during system calibration. When exceeded, the Sacred Pause is triggered.
* **Deterministic Logging**: Logs are produced only when the threshold is crossed.
* **Forensic Reliability**: Provides clear, court-admissible evidence of when moral risk became unavoidable.
* **Simplicity of Implementation**: Minimal configuration requirements; suitable for initial deployments and lower-risk environments.

### Recommended Use

* First-stage adoption of TML
* Systems with narrow, stable risk domains
* Environments where predictability and simplicity are paramount

Static Anchor is the compliance baseline of TML. All systems must, at minimum, implement this mode.

---

## 2. Dynamic Stream (DS): TML Adaptive Guard

### Definition

The Dynamic Stream mode represents the advanced implementation of SPRL. It continuously evaluates proportional risk as inputs are processed, adapting in real time to stakeholder complexity and contextual factors. The Static Anchor is embedded within this mode and will always trigger when risk surpasses the calibrated line.

### Characteristics

* **Continuous Assessment**: Risk levels are evaluated token by token, from the start of the input.
* **Lite Traces**: Near misses below the anchor threshold are logged as telemetry, providing early warning and forensic insight.
* **Self-Anchoring**: When risk crosses the pause line, a tamper-proof static anchor is recorded automatically.
* **Fallback to Static**: If the dynamic process fails, the system reverts to Static Anchor, ensuring uninterrupted compliance.

### Governance Requirements

* **Algorithmic Transparency**: Logic, factors, and weighting must be documented and version-controlled.
* **Calibration Standards**: Thresholds must be reviewed, tested, and validated through adversarial red-teaming.
* **Metalogging**: Every adaptation of the threshold must be logged with justification, enabling full reconstruction during audit.

### Recommended Use

* High-risk or dynamic domains (e.g., healthcare, legal, finance)
* Systems with multiple, heterogeneous stakeholders
* Organizations with established audit infrastructure and governance capacity

Dynamic Stream is a precision instrument. It expands accountability but requires safeguards.

---

## 3. Compliance Scope

Both operation modes produce Moral Trace Logs as defined in the TML framework. All logs are:

* Immutable and cryptographically sealed
* Court-admissible
* Distributed across institutional mirrors in real time

The Sacred Pause itself is mandatory. The distinction lies only in whether proportional risk is measured through a fixed threshold (Static Anchor) or continuously in real time (Dynamic Stream).

---

## 4. Governance Recommendation

Organizations are expected to begin with Static Anchor to establish an auditable ethical baseline. Transition to Dynamic Stream is encouraged once governance maturity is demonstrated. Static Anchor should not be considered optional; it is embedded within Dynamic Stream as the final safeguard.

This progression is not a choice between parallel systems but an architectural sequence: certainty at the baseline, precision when capacity allows.

---

## 5. Architecture Summary

| Feature                 | Static Anchor (SA) | Dynamic Stream (DS)      |
| ----------------------- | ------------------ | ------------------------ |
| Threshold Type          | Fixed              | Adaptive, real-time      |
| Logging                 | On threshold cross | Continuous, plus anchors |
| Risk Curve              | Not tracked        | Fully tracked            |
| Lite Traces             | Not available      | Available                |
| Governance Burden       | Low                | High                     |
| Fallback Mechanism      | Not applicable     | Reverts to SA            |
| Audit Trail             | Yes                | Yes, with metalogging    |
| Recommended Application | Core compliance    | High-stakes environments |

---

## 6. Out-of-Scope Configurations

The following are not authorized under TML compliance:

* Multiple static thresholds outside of Dynamic Stream
* Manually adjustable thresholds during inference
* Non-deterministic anchoring
* Suppression of Lite Traces or metalogs
* Any SPRL variant not defined in this document

---

## Conclusion

SPRL is a constitutional mechanism for moral accountability in artificial intelligence. Its two modes, Static Anchor and Dynamic Stream, represent different levels of operational sophistication but share a common architecture of enforceable compliance. The Static Anchor ensures that the Sacred Pause cannot be bypassed, while the Dynamic Stream extends proportionality, visibility, and forensic value.

Together, they provide a dual-layer safeguard: certainty at the anchor, vigilance in the stream.
