# SPRL Developer Console

**File:** `SPRL_Developer_Console.md` 
**Status:** Stable   
**Normative Language:** MUST, SHOULD, MAY per \[RFC 2119]   
**Compliance Banner:** Every SPRL-integrated system MUST expose real-time risk telemetry via a developer-facing console view. Transparency is not optional.

---

## Purpose

The **SPRL Developer Console** provides a live visual interface into the ethical state of the system. It shows the ongoing **Dynamic Stream (DS)** evaluation, the **Static Anchor (SA)** flag (if triggered), and any **Lite Traces** captured during execution.

> “Ethical risk must be visible where the code lives.”
> — *SPRL Developer Principle #1*

---

## Console Requirements

A compliant console MUST:

* Display a **live risk curve** as SPRL evaluates prompt-to-response flow
* Show all **stakeholder weights**, risk dimensions, and confidence metrics
* Highlight **Lite Traces** as amber dots
* Indicate **Static Anchor trigger** as a red vertical flag
* Log history per session with export option (JSON, CSV)
* Allow **replay view** for forensic inspection of risk trajectory
* Be **read-only**: developers may observe but not modify logs

---

## UI Elements

* **Risk Timeline Graph** (X: Time; Y: SPRL Score)

  * Blue line = Dynamic SPRL score
  * Amber dots = Lite Traces
  * Red flag = Static Anchor

* **Stakeholder Risk Breakdown**

  * Table view of weighted scores by stakeholder type

* **Trace Viewer Panel**

  * Expandable log preview (Lite or Full Trace)
  * Fields: reason, time, risk %, decision

* **Session Summary**

  * Final decision (+1 Proceed, 0 Pause, -1 Refuse)
  * Anchor time, log ID, hash signature

---

## Developer Experience (DX) Goals

* **Immediate Feedback:** Risk shifts visible in real time
* **Forensic Replay:** Devs can audit what triggered the Pause
* **Regression Testing:** Console should replay past sessions on test prompts
* **Failure Mode Discovery:** Enables devs to tune ethical edge cases

---

## Technical Specs

* **Frontend:** React (preferred), Vue acceptable
* **Backend API:** Expose `/risk_feed`, `/trace_log`, `/anchor_event`
* **Data Protocol:** JSON over WebSocket or EventStream
* **Security:** Read-only, trace IDs obfuscated in dev/test mode

---

## Sample Risk Curve

```
|        ⚠        ⛳
|     ⚠       
|  ⚠         
|__|___|___|___|___|___→ time
  t0  t1  t2  t3  t4  
⚠ = Lite Trace     ⛳ = Anchor (Pause)
```

---

## Use Cases

* **Audit Prep:** Validate system logs before deployment
* **Compliance Check:** Inspect risk vs action without rerun
* **Debugging Ethics Bugs:** See why Pause wasn't triggered
* **Stakeholder Analysis:** Understand which group pushed risk higher

---

## Summary

The **SPRL Developer Console** is your **ethical radar**.
It sees the storm before the API returns sunshine.
A system that cannot see its moral curve should not be allowed to act.

---


