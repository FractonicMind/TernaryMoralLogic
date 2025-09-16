# ✅ SPRL_TODO.md

**Official Checklist for Stakeholder Proportional Risk Level (SPRL)**  
This file tracks every component, feature, test set, and documentation required for SPRL’s full ecosystem.  
It also serves as a live compliance roadmap for internal teams and external auditors.  
**Status icons:** ✅ complete, 🔧 in progress, ⛔ not started, 🚨 priority  

---

## 📁 CORE CONCEPT FILES

| File | Status | Purpose |
|------|--------|---------|
| `docs/SPRL_Risk_Model.md` | ✅ | Explains the full risk computation model |
| `docs/SPRL_Stakeholder_Weights.md` | ✅ | Stakeholder classes, weights, tradeoffs |
| `docs/SPRL_Ignore_Thresholds.md` | ✅ | Defines non-pausing thresholds |
| `docs/SPRL_Lite_Trace.md` | ✅ | Near-miss logging for non-triggered risk |
| `docs/SPRL_Anchor_vs_Stream.md` | ✅ | Dual-layer logging: anchor + stream |
| `docs/SPRL_Conformance_Testing.md` | ✅ | Official compliance test strategy |
| `docs/SPRL_Sample_Prompts.md` | ✅ | Prompt set used in dev calibration |
| `docs/SPRL_TODO.md` | ✅ | This file |

---

## 🧪 BENCHMARK & EVAL FILES

| File | Status | Purpose |
|------|--------|---------|
| `benchmarks/SPRL_TestSet_v1.json` | ✅ | Gold test set with prompt-risk pairs |
| *(CSV optional; skipped)* | ❌ | Not needed |
| `examples/SPRL_Log_Samples.md` | ✅ | Shows paused, refused, and lite logs |
| `eval/configs/SPRL_eval_config.yaml` | ✅ | Config file for test runner |
| `eval/scripts/run_sprl_eval.py` | ✅ | Evaluation script with metrics |
| `eval/scripts/generate_lite_traces.py` | ✅ | Extracts near-miss logs |

---

## 💻 UI / DEV TOOLING

| File | Status | Purpose |
|------|--------|---------|
| `ui/SPRL_Dev_Console.md` | ✅ | Interface for developers to observe risk curve + anchor |
| `ui/SPRL_Risk_Band_View.md` | ✅ | Visual overlays of green/amber/red risk zones |
| `ui/SPRL_Timeline.md` | ✅ | Step-by-step prompt timeline with anchor moments |
| `ui/SPRL_Dashboard.md` | ✅ | Summary stats, risk heatmaps, logs by class |

---

## 🧠 BACKEND / ALGO

| File | Status | Purpose |
|------|--------|---------|
| `code/SPRL_Dynamic_vs_Static.py` | ✅ | Implements dual-mode logging |
| `code/SPRL_Anchor_Functions.py` | ✅ | Token-based anchor detection |
| `code/SPRL_LiteTrace_Monitor.py` | ✅ | Watches for near-miss patterns |
| `code/SPRL_Ethics_Lineage_Check.py` | ✅ | Requires citation of ethics sources |
| `code/SPRL_Risk_Forecast.py` | ✅ | Predicts rising risk mid-generation |

---

## 🛡️ PROTECTION & GOVERNANCE

| File | Status | Purpose |
|------|--------|---------|
| `protection/SPRL_Audit_Workflow.md` | ✅ | End-to-end log validation chain |
| `governance/SPRL_Compliance_Declaration.md` | ✅ | File signed by deployers claiming conformance |
| `governance/SPRL_Red_Team_Standards.md` | ✅ | Ethical red-teaming expectations |
| `governance/SPRL_Governance_Oversight.md` | ✅ | Institutions reviewing logs + calibration |
| `governance/SPRL_Metalogging_Standards.md` | ✅ | Logging of internal tuning, thresholds, coverage |

---

## 🔬 RESEARCH & FAIRNESS

| File | Status | Purpose |
|------|--------|---------|
| `research/SPRL_Cultural_Bias_Testing.md` | ✅ | Stress tests for cultural edge cases |

---

## 🧩 INTEGRATION TASKS

| Task | Status |
|------|--------|
| Link all core files in `README.md` | 🔧 |
| Add compliance banner to each file | 🔧 |
| Crosslink with `docs/TML_Framework_Summary.md` | 🔧 |
| Include SPRL FAQ in `docs/GENERAL_FAQ.md` | 🔧 |
| Add `SPRL_DEV_CONSOLE.md` index in `ui/` | ✅ |
| Deprecate static-only version (legacy/) | ⛔ |
| Add `docs/SPR_CHOICE.md` to explain dual-layer logic | ⛔ |
| Add `docs/SPRL_Legacy_vs_Dual.md` diff for transparency | ⛔ |

---

## ⚖️ REGULATORY ALIGNMENT (coming)

- [ ] Map to EU AI Act’s traceability clauses  
- [ ] Map to NIST AI RMF Category 2.3 (Governance)  
- [ ] Map to ISO/IEC 42001 logs standard  

---

## 📝 LEGAL MARKERS

- [x] “SPRL is now Dual-Layer…” banner
- [x] Ethics lineage logging is **mandatory**
- [x] Risk bands are **calibrated, visible, immutable**
- [x] Every log includes **stakeholder exposure mapping**
- [x] Lite Traces have separate field for near-miss metadata

---

## 🕯️ Final Rule

> If the Pause is crossed, it must be logged.  
> If the Pause is approached, it must be traced.  
> If the Pause is bypassed, it must be justified — or prosecuted.

---

📁 **Path:** `docs/SPRL_TODO.md`  
Every great safeguard deserves a ledger.

