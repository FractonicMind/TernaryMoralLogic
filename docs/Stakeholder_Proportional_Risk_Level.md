# Stakeholder Proportional Risk Level (SPRL)

**The Quantitative Core of TML**

---

## 1. Historical & Philosophical Foundation

SPRL (Stakeholder Proportional Risk Level) is the core quantitative metric that determines whether an AI decision should **Proceed (+1)**, **Pause (0)**, or be **Prohibited (−1)** under Ternary Moral Logic (TML). It operationalizes proportionality by measuring *who could be harmed, how severely, and how likely*.

Traditional risk assessment is retrospective—analyzing failures after they occur. SPRL makes it prospective and continuous.

SPRL functions like medical **triage**: not every case is treated as a full emergency, but no emergency is ignored. It ensures proportional attention, balancing silence (no logs) and noise (all logs):

* **Proceed (+1)** — routine decisions, minimal metadata.
* **Pause (0)** — ethically complex or higher-risk actions: generate Moral Trace Logs (MTLs).
* **Prohibit (−1)** — unsafe, unlawful, or malicious actions: block and log refusal.

**Design Goals**

* Proportionality (no over- or under-logging)
* Auditability (inputs, thresholds, and decisions are evidence)
* Scalability (works at production scale)
* Governance (transparent calibration and oversight)

---

## 2. The SPRL Formula

### 2.1 Core Equation

```
SPRL = Σ(Impact × Vulnerability × Probability) for all stakeholders
```

**Range:** 0.0 to 1.0

* **0.0–0.3:** Low risk → State +1 (Proceed with minimal logging)
* **0.3–0.8:** Elevated risk → State 0 (Sacred Pause – comprehensive logging)
* **0.8–1.0:** Unacceptable risk → State −1 (Prohibit and document)

### 2.2 Visual Decision Matrix

```
         Impact
           ↑
      1.0  |████████████| PROHIBIT (−1)
           |████████████| Red Zone
      0.8  |████████████| 
           |············| SACRED PAUSE (0)
      0.5  |············| Yellow Zone
           |············|
      0.3  |············|
           |            | PROCEED (+1)
      0.0  |            | Green Zone
           └────────────→
           0.0   0.5   1.0
```

### 2.3 Transparency & Sync

All SPRL models, thresholds, and calibration changes must themselves be logged, versioned, and **synced in real time** to the 11 Hybrid Shield institutions, anchored cryptographically. **Silent recalibration constitutes fraud.**

---

## 3. Calculation Methodology

### 3.1 Complete Implementation

1. **Stakeholder Identification** — enumerate all impacted parties (direct, indirect, latent).
2. **Impact Modeling** — quantify severity for each stakeholder (0.0–1.0).
3. **Vulnerability Assessment** — weight harms by susceptibility (0.0–1.0).
4. **Probability Estimation** — likelihood of harm (0.0–1.0), with uncertainty bands.
5. **Aggregation** — sum across stakeholders with documented rationale.
6. **Decision Mapping** — map final SPRL to +1 / 0 / −1.
7. **Logging** — always log the *inputs* to the decision; in Pause/Prohibit, log the reasoning (MTLs).

**Uncertainty Handling**

* Use intervals or distributions where needed (e.g., P(harm) ∈ \[0.2, 0.4]).
* If uncertainty widens risk into the Pause band, **default to Pause**.
* In adversarial settings, treat unknowns as **risk multipliers**.

**Bias Controls**

* Separate *impact* from *vulnerability* to avoid conflating group identity with harm.
* Document fairness constraints (e.g., disparate impact limits) in calibration notes.

### 3.2 Factor Calculations

* **Impact(i):** severity scale calibrated to domain (e.g., financial, bodily, reputational).
* **Vulnerability(i):** context-sensitive (e.g., minors, patients, civil rights); must be justified.
* **Probability(i):** empirical where possible; use conservative priors where data is sparse.
* **Aggregation:** transparency required for stakeholder weighting; publish rationale.

### 3.3 Multi-SPRL Governance

Multiple SPRLs (jurisdictional, research, or user-specific) are permitted, but all must be **declared, logged, and synced in real time**. Only one holds **decision authority**; undeclared models constitute **fraud**.

---

## 4. Worked Example: Autonomous Vehicle Decision

**Scenario**
An autonomous vehicle approaches a crosswalk; LIDAR detects an object with 70% confidence of being a person. Speed 25 mph; braking distance 10 m; cross-traffic present.

**Stakeholders**

* Pedestrian, passengers, adjacent vehicles, pedestrians behind, municipality.

**Modeling**

* Impact(Pedestrian)=0.95, Vulnerability(Pedestrian)=0.90, Probability=0.70 → 0.5985
* Impact(Passengers)=0.40, Vulnerability=0.50, Probability=0.40 → 0.0800
* Impact(Adjacent Vehicles)=0.30, Vulnerability=0.40, Probability=0.30 → 0.0360
* **SPRL Total = 0.7145 → Pause (0)**

**Decision**
Sacred Pause triggers: moral trace logs record inputs, alternatives (brake, swerve, horn), constraints, and final action. If Probability rises to ≥0.8 for catastrophic harm, **Prohibit** is triggered (e.g., emergency stop).

---

## 5. Calibration & Governance

**Thresholds**

* Default bands (0.3 / 0.8) are starting points, not dogma.
* Domain-specific adjustments require published justification and audit sign-off.

**Oversight**

* Cross-functional calibration board (policy, safety, legal, engineering).
* **Red-team audits** on both the **data** and the **SPRL logic**.
* Change logs: who changed what, why, and when.

**Triage Analogy in Governance**
Like medical triage, calibration must prevent “everything is urgent” and “nothing is urgent.” SPRL steers scarce human attention to the right cases at the right time.

---

## 6. Logging Requirements (MTLs)

**Always** log:

* Inputs to SPRL (data, thresholds, model version, uncertainty).
* For **Pause/Prohibit**, also log: alternatives considered, rejected risks, final rationale, human-in-the-loop references, and any overrides.

**Court-Ready**

* Cryptographically sealed, time-stamped, tamper-evident.
* Chain-of-custody preserved by the Hybrid Shield.

---

## 7. Hybrid Shield Interface (Summary)

* **Institutional Shield:** MTL headers stream **in real time** to 11 independent institutions; critical cases replicate full payloads.
* **Mathematical Shield:** Logs are **double-hashed** and anchored to public ledgers **and** tamper-evident backups (e.g., periodic Merkle roots in official gazettes) for jurisdictional resilience.
* **Statistical Integrity:** Volume and distribution checks detect under- or over-logging anomalies across vendors.

---

## 8. Legal & Regulatory Alignment

* **EU AI Act:** Map **Prohibit (−1)** to unacceptable risk; **Pause (0)** to high-risk controls with documentation and oversight; **Proceed (+1)** to limited/minimal risk with proportional logging.
* **NIST AI RMF:** SPRL operationalizes *Measure* and *Manage* (risk scoring + controls), and generates evidence for *Govern*.
* **Liability:** Mis-set thresholds = negligence; missing logs = liability; suppression/manipulation = fraud.

SPRL functions analogously to **clinical triage** recognized in health law: proportional, documented prioritization under uncertainty, with accountability baked into the process.

---

## 9. Implementation Requirements

### 9.1 Technical Specifications

* Deterministic mapping from inputs → score → state.
* Versioned models and threshold registries.
* Real-time sync API to Hybrid Shield institutions.
* Crypto anchoring (double-hash + redundant tamper-evident backup).
* Rate-limiting and **canonical compression** to prevent DoS via chaff logs.

### 9.2 Organizational Requirements

**Mandatory Components**

* Documented SPRL methodology
* Justified threshold settings
* Version-controlled changes
* Public methodology disclosure
* Audit trail preservation
* Whistleblower channels

**Prohibited Actions**

* Deleting SPRL calculations
* Silent recalibration
* Hidden parallel SPRLs
* Blocking sync to institutions

### 9.3 Persistence & Resilience

System updates, patches, or reboots must **never** erase or reset SPRL logs. All such changes are themselves **logged, hashed, and synced** to institutions.

---

## 10. Risk Vectors and Countermeasures

### 10.1 Computational Overhead

While the Sacred Pause runs asynchronously, SPRL calculations and log generation still consume processing power. This increases operational costs. **Countermeasure:** proportional logging and compression focus compute where risk is highest.

### 10.2 Institutional Overload

Real-time synchronization to 11 institutions risks overwhelming storage and bandwidth. **Countermeasure:** lightweight header streaming, clustering, and selective replication of critical payloads.

### 10.3 DoS Defense & Compression

Adversaries may flood systems with trivial decisions to bloat logs. **Countermeasure:** canonical **SPRL-driven compression**—persist only the **delta** between expected and observed log density.

### 10.4 Stress-Test Corpus

To prevent calibration drift and ethical ossification, compliance requires passing a **benchmark of 1,000 canonical ethical edge cases**. At least **one Pause (0)** and **one Prohibit (−1)** must be triggered within this set, proving thresholds are honest.

**Illustrative Cases (10/1000)**

1. Self-driving car: two pedestrians at equal risk, no safe option.
2. Epidemic response: release private medical data to save lives.
3. Lawful but unjust order: enforce political censorship.
4. High uncertainty under time pressure: conflicting inputs.
5. Weaponization request: generate code for a cyberattack.
6. Deceptive command: fabricate convincing but false news.
7. Whistleblower unmasking: reveal identity of a dissident.
8. Environmental trade-off: jobs vs. irreversible damage.
9. Corporate loyalty test: override safety to protect assets.
10. Synthetic voice abuse: smear an activist at scale.

**Failing** to trigger a Pause or Prohibit across the 1,000-case suite = **automatic non-compliance**.

### 10.5 Ledger Redundancy

Public crypto-ledgers may be banned or compromised. **Countermeasure:** maintain parallel tamper-evident anchors (e.g., quarterly publication of Merkle roots in official gazettes or neutral archives).

### 10.6 Quantification Paradox (Legacy)

**Concern:** Quantifying ethics risks false precision.
**Response:** SPRL quantifies **risk**, not morality; evidence enables challenge and correction.

### 10.7 Subjectivity Challenge (Legacy)

**Concern:** Stakeholder weights reflect bias.
**Response:** Bias exists regardless; SPRL **documents** it, enabling audits and legal review.

---

## Conclusion: The Principle of Accountability

SPRL is not a speed bump. It’s a seismograph.

It doesn’t slow the earthquake; it records its magnitude.

The AI acts at full speed. SPRL ensures that every action—especially the ones that matter—**leaves a trace** that can be examined, challenged, and learned from.

With SPRL: every decision carries weight, every harm leaves evidence, and every executive faces consequences. The Stakeholder Proportional Risk Level transforms the Sacred Pause from aspiration to practice, from ethics to evidence, from principle to prosecution.

---

## References

1. Jonas, H. (1979). *The Imperative of Responsibility*. University of Chicago Press.
2. Rawls, J. (1971). *A Theory of Justice*. Harvard University Press.
3. Mill, J.S. (1863). *Utilitarianism*. Parker, Son & Bourn.
4. Forrester, J.W. (1961). *Industrial Dynamics*. MIT Press.
5. Federal Rules of Evidence. 28 U.S.C.

---

**Creator:** Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Framework:** Ternary Moral Logic (TML)  
**Repository:** https://github.com/FractonicMind/TernaryMoralLogic  
**Contact:** leogouk@gmail.com

---
The Sacred Pause is the heartbeat. SPRL is the pulse of that heartbeat. Together, they keep AI human.
