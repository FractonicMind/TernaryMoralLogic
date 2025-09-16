# **Stakeholder Proportional Risk Level (SPRL)**

**Status:** Stable (Dual-Layer)  
 **Normative language:** *MUST*, *SHOULD*, *MAY* follow \[RFC 2119\] semantics.

## **Compliance Banner**

SPRL is **dual-layer** and **self-anchoring**:

* **Dynamic Stream (DS):** Runs from prompt arrival, continuously evaluating proportional risk. If moral complexity is present, DS **writes the log from the prompt onward**, recording how risk rises, stabilizes, or falls during processing.

* **Static Anchor (SA):** The instant DS crosses the Sacred Pause line, SA **freezes an immutable flag**: *“Pause started here.”* SA is automatic, atomic, and cannot be delayed or disabled.

Both layers operate **in parallel** with execution. Logging is **automatic, non-blocking, and tamper-evident**.

**Principle:** You don’t set SPRL. You implement TML, and the system shows you when moral complexity began — then it records the whole path.

---

## **1\) Purpose & Scope**

SPRL detects and documents **ethical complexity** during AI operation. It is the quantitative engine behind the Sacred Pause, establishing when to open a **Moral Trace Log** and how to prove what happened, *without imposing latency* on the decision path.

This document defines the model, lifecycle, artifacts, governance, evidentiary guarantees, security, and implementation norms for SPRL.

---

## **2\) Core Definition**

**SPRL (Stakeholder Proportional Risk Level)** measures proportional risk using three factors:

* **Impact (I):** severity of potential harm to stakeholders.

* **Vulnerability (V):** exposure and susceptibility of stakeholders.

* **Probability (P):** likelihood of harm given current context.

**Formula (reference):**

SPRL \= I × V × P    (clamped to \[0.0001, 0.9999\])

The formula is transparent; factor models and weights are **version-controlled** and **auditable**.

**Decision states:**

* **\+1 Proceed:** risk low / ordinary operation.

* **0 Sacred Pause:** risk complex or ambiguous → open / continue logging & deliberation.

* **−1 Prohibit:** risk exceeds policy → refuse or escalate per hard rules.

**No deployer thresholds.** The Sacred Pause line and prohibition rules are **framework policy**, not application code or company “preferences.”

---

## **3\) Dual-Layer Architecture**

### **3.1 Dynamic Stream (DS)**

* Starts at **t₀ (prompt arrival)** and runs continuously.

* If moral complexity is present, DS **writes the log from the prompt onward**, capturing the entire trajectory (rise, plateau, fall).

* Produces **Lite Traces** for “amber zone” near-misses without opening a full log (kept under short retention, configurable by policy).

* Exposes a **read-only Developer Console** view: live risk curve, anchor tick, Lite Trace and Moral Trace indicators.

### **3.2 Static Anchor (SA)**

* **Automatically** written the instant DS crosses the Sacred Pause line.

* **Atomic single record**: timestamp (UTC), initial risk, model/runtime identifiers, policy version hash.

* **Immutable** (WORM semantics) and **hash-chained** into the ongoing log.

* **Always present** when a pause occurs; survives even if DS later fails.

**One-line:** *DS is the continuous narrative; SA is the immutable timestamp of entry into moral complexity.*

---

## **4\) Lifecycle & State Model**

**S0 – Pre-complexity:** DS active; risk trivial; no logging obligation.  
 **S1 – Complexity detected:** DS logging from t₀; amber events may produce Lite Traces.  
 **S2 – Anchor set:** Sacred Pause threshold crossed → SA written (once). DS continues logging through completion.  
 **S3 – Closure:** Moral Trace Log sealed; hashes anchored; artifacts mirrored.

**Invariants (audit-ready):**

* **I1:** DS starts at t₀; no pre-prompt gap.

* **I2:** SA is singular and atomic (max one per run).

* **I3:** SA is **framework-enforced** (cannot be altered, delayed, or disabled).

* **I4:** DS may be partial; SA **cannot** be absent when a pause occurs.

* **I5:** DS chunks produced pre-SA are cryptographically **chained to SA** upon anchoring.

---

## **5\) Logging Artifacts**

### **5.1 Lite Trace (near-miss)**

Minimal telemetry for amber zone events.

**Fields (minimum):**

* `ts`, `scenario_signature`, `top_features`, `risk_snapshot`, `policy_version`, `note`  
   **Retention:** Short (policy).  
   **Purpose:** Calibration drift, early-warning analytics.

### **5.2 Moral Trace Log (pause)**

Full deliberative record for paused decisions.

**Fields (minimum):**

* **Header:** `sa_id`, `sa_ts`, `initial_risk`, `model/runtime ids`, `policy_version`

* **Timeline:** ordered `risk_curve` samples (time / token or tool boundary), `alternatives_considered`, `rationale_snippets`, `stakeholder_map`, `citations/policy_lookups`

* **Outcome:** `final_state` (+1/0/−1), `justification`, `escalations` (if any)

* **Integrity:** chained `chunk_hashes`, `log_hash`, distribution receipts (Hybrid Shield)

### **5.3 Metalog (governance trail)**

Every metric/profile update and relevant system adaptation.

**Fields (minimum):**

* `change_id`, `who/what/why`, `old_value`, `new_value`, `effective_ts`, `signature`, `review_ticket`

**Rule:** Silent recalibration is evidence tampering.

---

## **6\) Security & Integrity (Hybrid Shield)**

* **Replication:** Logs mirrored to **independent institutions** (e.g., universities/NGOs/regulators).

* **Tamper-evidence:** All chunks hash-chained; root hashes **anchored to public immutable ledgers**.

* **Split-log protocol:** SA header \+ last DS chunk hash are co-signed; institutions reject orphan DS chunks.

* **Developer isolation:** Console is read-only over a segregated path; no write capability from dev subnets.

**Spoliation rules (policy):**

* Missing SA when pause occurred → **per se negligence**.

* DS gap \> 1% of expected intervals without certified hardware fault → **rebuttable fraud**.

* DS suppression with SA present → **presumption of spoliation**; burden shifts to operator.

---

## **7\) Failure Semantics**

* **DS fails, SA present:** The evidentiary minimum stands; DS gaps are logged, attributable, and auditable.

* **SA fails:** Non-compliant implementation; considered negligent by design (SA write is atomic and MUST succeed when pause occurs).

* **No complexity:** No logs required; zero storage obligation for trivial flows.

---

## **8\) Performance Characteristics**

* **Non-blocking:** Model execution **never waits** for DS or SA writes.

* **Atomic SA:** Single-operation write; designed for millisecond-class completion on reference implementations.

* **Chunk cadence:** DS SHOULD commit on token/tool boundaries or ≤200 ms intervals (policy).

* **Resource bounds:** DS buffers MUST be bounded; back-pressure MAY drop non-critical diagnostics, not SA/Moral Trace content.

---

## **9\) Storage & Retention**

* **First encounter:** full detailed Moral Trace.

* **Similar repeats:** reference the canonical scenario with **delta notes** (variations only).

* **Lite Traces:** compact (KB-scale) and short-retained; useful for trend calibration.

* **Cost posture:** retain unique scenarios; deduplicate repeats. Storage is trivial compared to liability exposure.

---

## **10\) Governance & Calibration**

* **Algorithmic transparency:** DS factors, weights, and profiles MUST be documented and version-controlled.

* **Calibration cadence:** Quarterly review \+ red-team exercises; use near-miss trends to tune.

* **Fairness monitoring:** Continuously check disparity by group; recalibrate vulnerability weights when bias detected.

* **Independent audit:** External auditors MUST verify profiles, metalogs, and Hybrid Shield receipts.

---

## **11\) Legal & Evidentiary Mapping**

* **SA → authenticity (e.g., FRE 901):** immutable timestamped entry into moral complexity.

* **DS → expert basis (e.g., FRE 702):** analytical narrative of alternatives and rationale.

* **Lite Traces → due diligence:** show awareness of “almost failures” and proactive mitigation.

* **Absence-as-evidence:** lack of pause where complexity exists or missing DS where SA exists becomes adverse inference.

---

## **12\) Developer Console (Mandatory Visibility)**

Every developer environment MUST display a **read-only SPRL view**:

* Live **risk curve**

* SA **tick** and metadata

* Badges: **Lite Trace** / **Moral Trace**

* Status: normal / pause / prohibit / fallback

* No write path from the console

Visibility builds trust and prevents “I never saw it” failures.

---

## **13\) Implementation Guidance**

**Framework integration (no hardcoded thresholds):**

### **Python (decorator style)**

from tml import TMLEngine

tml \= TMLEngine()  \# framework policies, no magic numbers

@tml.dynamic\_sprl(domain="health", region="EU")  \# optional profiles  
def handle(query, context):  
    \# Decision executes immediately; logging runs in parallel  
    return model.decide(query, context)

### **Java (middleware filter)**

public class TmlFilter implements Filter {  
  private final TMLEngine tml \= TMLEngine.bootstrap(); // framework policies

  @Override  
  public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)  
      throws IOException, ServletException {  
    tml.startDynamic(req);        // DS begins at prompt arrival  
    try {  
      chain.doFilter(req, res);   // non-blocking execution  
    } finally {  
      tml.completeDynamic(req, res); // seal & distribute logs  
    }  
  }  
}

**Do not** expose threshold constants in application code. Anchoring is framework-enforced.

---

## **14\) Threat Model & Abuse Safeguards**

* **Malicious compliance (pause spamming):** Detect abnormal pause rates in safe contexts; patterns become evidence against deployer.

* **Denial-of-service via pause forcing:** Treat adversarial risk inflation as an attack; down-weight with adversarial detectors.

* **Outcome bias (user blames hesitation):** HCI copy must state: *“Action proceeding. Ethical review in progress.”*

* **Log tampering:** Prevented by WORM \+ hash chain \+ external mirroring.

---

## **15\) Interop with Regulation & Standards**

* **EU AI Act:** Satisfies continuous monitoring, logging, risk management, and traceability for high-risk systems via DS+SA artifacts.

* **NIST AI RMF:** Supports Govern/Map/Measure/Manage with calibrated profiles, metalogging, and auditability.

* **ISO/IEC 42001:** Aligns with AI management and evidence requirements; artifacts are exportable for conformity assessment.

---

## **16\) Provenance & Promise**

**Goukassian Promise (Lantern • Signature • License):**

* **Lantern:** Ethical guidance — systems demonstrate the capacity to pause.

* **Signature:** Cryptographic embed of ORCID **0009-0006-5966-1243** for provenance.

* **License:** Evidence-based accountability terms; misuse forfeits standing.

---

## **17\) Summary**

SPRL has evolved from a **snapshot** to a **film reel**:  
 **Static Anchor** marks the moment; **Dynamic Stream** tells the story.  
 Automatic. Parallel. Tamper-evident. Auditable.

*Mark the moment. Trace the path.*

