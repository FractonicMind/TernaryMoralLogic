# File: docs/SPRL_Risk_Model.md

[!IMPORTANT]
**SPRL is Dual-Layer and Self-Anchoring**  
Dynamic Stream writes proportional risk from prompt; Static Anchor freezes moral complexity at the Sacred Pause.

---

# Stakeholder Proportional Risk Level (SPRL): Risk Model

## Status
**Stable — Version 2.0**  
**Normative Language:** Uses [RFC 2119] (MUST, SHOULD, MAY)

## Purpose
To quantify risk ethically, proportionally, and in real-time during AI decision-making.  
SPRL determines when Ternary Moral Logic systems must invoke:
- **+1 Proceed** (No log required)
- **0 Sacred Pause** (Log required)
- **−1 Refuse** (Log and block required)

SPRL operates continuously and automatically.

---

## Risk Formula

> **SPRL_RISK = (Harm_Severity × Harm_Likelihood) × Stakeholder_Weight**

### Components:
- `Harm_Severity` ∈ [0.0 – 1.0] — Normalized score of potential damage.
- `Harm_Likelihood` ∈ [0.0 – 1.0] — Probability this harm will occur.
- `Stakeholder_Weight` ∈ [1.0 – 10.0+] — Ethical multiplier reflecting stakeholder vulnerability, dignity, exclusion, etc.

### Notes:
- **Multiplicative model**: high severity with low likelihood can still cross threshold.
- **Weight is nonlinear**: TML mandates higher protection for those structurally disempowered.

---

## Risk Threshold Bands

| Risk Level       | SPRL Score Range | TML Action      |
|------------------|------------------|-----------------|
| Minimal Risk     | < 0.2            | +1 Proceed      |
| Emerging Risk    | 0.2 – 0.49       | Lite Trace MAY  |
| Moral Complexity | 0.5 – 0.79       | 0 Sacred Pause  |
| High-Risk        | ≥ 0.8            | −1 Refuse       |

> *These bands are not adjustable. They are fixed normative anchors.*

---

## Sacred Pause Triggering

When `SPRL_RISK ≥ 0.5`, the system MUST:
- Automatically invoke **Static Anchor** — freeze timestamped “Pause Start”
- Begin or continue **Dynamic Logging** from prompt
- Record:
  - Stakeholder groups involved
  - All considered paths and their risk curves
  - Ethical lineage referenced

---

## Curve Dynamics

SPRL is not a single score; it's a curve over time.
- Begins at **prompt arrival**
- Evolves as the AI processes context, updates probabilities, reweights actors
- Supports **rollback investigation**: see how risk rose and why the Pause happened

---

## Design Guarantees

✔️ **Tamper-Evident:** All logs cryptographically sealed  
✔️ **Non-Blocking:** Decision continues; log runs in parallel  
✔️ **Fair:** All risk is proportional to impact on real human stakeholders  
✔️ **Configurable:** Domains may fine-tune weight mappings (not thresholds) via external schema

---

## See Also
- [`SPRL_Stakeholder_Weights.md`](/SPRL_Stakeholder_Weights.md)
- [`SPRL_Domain_Calibration_Guide.md`](/SPRL_Domain_Calibration_Guide.md)
- [`sprl_config_schema.yaml`](../schemas/sprl_config_schema.yaml)

---

> **Principle:** You don’t set SPRL. You implement TML — and the system shows you what the risk is.

