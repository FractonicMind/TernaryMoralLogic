# README_Transition_To_Dual_Layer_SPRL.md

**Path:** `legacy/README_Transition_To_Dual_Layer_SPRL.md`

## Purpose
This file is a transitional README for developers, researchers, or regulators who previously engaged with the static-threshold SPRL architecture. It explains how and why the TML project has transitioned to the Dual-Layer SPRL model.

---

## What Changed

| Element | Legacy SPRL | Dual-Layer SPRL |
|--------|--------------|------------------|
| Logging Trigger | Manual threshold (e.g. 0.4) | Automatic Static Anchor (SA) |
| Early Detection | No | Dynamic Stream (DS) from token 1 |
| Developer Control | Full | Read-only ethical zone |
| Forensic Trace | Only if threshold crossed | Full journey from prompt |
| Calibration | Hardcoded | Real-time risk model + metalogging |

---

## Why We Changed

Legacy SPRL served as a working prototype. However, TML is now positioned as a forensic compliance architecture — one that must:

- Prevent both **silence** (under-logging) and **noise** (over-logging)
- Be immune to silent suppression by developers
- Show proportional response to moral complexity
- Provide **glass box** transparency to regulators

The Dual-Layer system meets all of these, while improving UX for both AI systems and governance bodies.

---

## What to Do If You're Using Static Thresholds

If your project still uses legacy SPRL via something like:
```python
spm = SPRL(sacred_pause_threshold=0.3)
```

You should:
1. Remove manual thresholding
2. Import from the new API:
```python
from sprl.dynamic import SPRL_RiskEngine
```
3. Integrate the new `AnchorTrigger` system:
```python
risk_engine = SPRL_RiskEngine()
response = model.generate(prompt, observer=risk_engine)
```
4. Display real-time stream via Dev Console (`ui/SPRL_Dev_Console.md`)

---

## Legacy Compatibility
To support transition:
- Legacy threshold-based logging is still available via `sprl/legacy/static_threshold.py`
- All legacy docs are moved to `/legacy/`
- Devs are encouraged to label their logs clearly as `LEGACY` if they continue using them

---

## Compliance Note
> ❗ Legacy SPRL logs are not considered **compliant** under the Goukassian Standard unless accompanied by Dynamic Stream output and anchored logs.

For certification purposes, refer to `docs/SPRL_Conformance_Testing.md`.

---

## In Summary
Static SPRL walked. Dual-Layer SPRL flies.

The Sacred Pause now comes with its own wings — one to stream, one to anchor.

Welcome to the new ethical backbone of machine reasoning.

— TML Ethics Directorate
