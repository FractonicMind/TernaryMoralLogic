
# SPRL: Anchor vs Stream

**Normative Language:** MUST, SHOULD, MAY per \[RFC 2119]   
**Compliance Banner:** TML-compliant systems MUST implement both layers of SPRL — the Dynamic Stream (DS) and the Static Anchor (SA) — in parallel. These layers serve distinct but complementary accountability functions.

---

## Summary

The **Anchor** is the flag.
The **Stream** is the path.

Together, they ensure every morally relevant action is both documented and accountable — not as a guess, but as evidence.

---

## Dual-Layer Design

### 1. **Dynamic Stream (DS)**

* Begins at **prompt arrival**
* Evaluates risk continuously, frame-by-frame
* Writes the **entire log** if ethical complexity is detected
* Records moral trajectory: rising risk, decay, stalling, recovery
* Outputs:

  * **Lite Trace** (if sub-threshold but morally notable)
  * **Full Moral Trace Log** (if Pause threshold crossed)

> Think of DS as the **live telemetry** of moral risk.

---

### 2. **Static Anchor (SA)**

* Triggers **only once**: the instant DS risk crosses the **Sacred Pause threshold**
* Writes a **permanent marker**:

  * "Pause started here"
  * Timestamp
  * Immutable flag
* Does **not re-trigger**; the anchor freezes the threshold crossing point
* Cannot be disabled, overridden, or deferred

> SA is the **forensic point of no return** — a cryptographic snapshot of ethical tension.

---

## Why Both?

| Purpose                | Dynamic Stream (DS)        | Static Anchor (SA)            |
| ---------------------- | -------------------------- | ----------------------------- |
| Tracks rising risk     | ✅ Yes                      | ❌ No                          |
| Freezes log scope      | ❌ No                       | ✅ Yes                         |
| Prevents silence       | ✅ Captures subtle morality | ❌ Not designed for nuance     |
| Forensic admissibility | ✅ Full log                 | ✅ Immutable anchor            |
| Developer debugging    | ✅ Live risk feedback       | ❌ Frozen event only           |
| Governance utility     | ✅ Risk pattern audits      | ✅ Anchor timestamp as trigger |

---

## Key Principles

* **DS is continuous; SA is discrete.**
* **DS tells the story; SA proves the chapter mattered.**
* **A Pause without a Stream is hollow. A Stream without an Anchor is ambiguous.**

---

## Legal Significance

* **SA**: Court-admissible signal of *when* the system detected moral complexity.
* **DS**: Court-admissible evidence of *why* it acted (or paused, or refused).

Together, they shift accountability from "intent" to **recorded moral reality**.

---

## Compliance Mandate

All TML-compliant systems MUST:

1. Run **DS** from the moment a prompt or input is received
2. Automatically trigger **SA** when DS crosses the Sacred Pause threshold
3. Ensure both are:

   * Parallel
   * Non-blocking
   * Tamper-evident

---

## Analogy

> DS is the video.
> SA is the bookmark that says: "Here’s where the moral fight began."

---


