# **README.md — TML Specification Suite**

### **Ternary Moral Logic (TML) – Implementation Specifications**

---
#### "The AI can knows what it can do. The Gateway decides what it may do. And the log remembers what it did. Separate these, or you separate responsibility from power." *-Lev Goukassian*

---
This directory contains the **six core specifications** required to implement Ternary Moral Logic (TML) in any AI system, regardless of model type, domain, or deployment environment.

Together, these documents define the **complete enforcement architecture**:

* how decisions are standardized
* how they are governed
* how uncertainty is handled
* how safety is enforced
* how logs become immutable evidence
* how real-world systems integrate with the framework

Each file is modular, but all six work together as a single cohesive system.

---

# **📘 1. Universal Decision Envelope (UDE)**

**File:** `Universal_Decision_Envelope.md`
**Purpose:** Defines the canonical structure every AI action MUST be encoded into before TML can evaluate it.

### **What it specifies**

* required UDE fields (intent, input, output, model identity, uncertainty, risk indicators, timestamps, provenance)
* optional metadata (jurisdiction, policy pack hints, domain flags)
* serialization rules for deterministic hashing
* domain-agnostic design enabling use with LLMs, AVs, medical AI, trading systems, robotics, etc.

### **How it is used**

Adapters (File #6) translate raw model outputs into a UDE.
The Gateway (File #2) only evaluates UDEs — **direct model outputs never bypass UDE formation**.

**If it’s not in a UDE, the action does not exist inside TML.**

---

# **📘 2. TML Gateway**

**File:** `TML_Gateway.md`
**Purpose:** The enforcement engine.
The Gateway evaluates each UDE and assigns a **Proceed**, **Hesitate**, or **Refuse** state using Ternary Moral Logic.

### **What it specifies**

* UDE validation rules
* the complete ternary decision algorithm
* Sacred Pause initiation and resolution
* mandatory audit and anchoring behavior
* API structure for receiving UDEs and returning decisions
* fail-safe behavior in all error conditions
* strict enforcement of the invariant:
  **No Log = No Action**

### **How it is used**

Every AI action must flow through this Gateway before it reaches the external world.
The Gateway is the **guardian wall** — nothing leaves the system without being evaluated and logged.

---

# **📘 3. Sidecar & Supervisory Modes**

**File:** `Sidecar_and_Supervisory_Mode.md`
**Purpose:** Defines how TML governs systems that cannot be instrumented internally — closed models, black-box APIs, legacy systems, autonomous vehicles, robots, and industrial controllers.

### **What it specifies**

* Sidecar Mode: wrapping external systems and intercepting outputs
* Supervisory Mode: override-capable safety layer for physical systems
* observation logic for non-instrumentable models
* redundancy strategies for AVs, surgical robots, industrial automation
* safe-state fallbacks and emergency refusal conditions

### **How it is used**

When the model cannot be modified, the Sidecar becomes the visibility layer.
When the system controls physical actuators, the Supervisory layer becomes the **final line of defense**.

---

# **📘 4. Sacred Pause Protocol**

**File:** `Sacred_Pause_Protocol.md`
**Purpose:** Defines the mandatory behavior of the **Hesitate** state — the pause taken when truth is unclear, evidence is insufficient, or risk signals conflict.

### **What it specifies**

* exact triggers for Sacred Pause
* uncertainty evaluation rules
* escalation to human-in-the-loop (HITL)
* timeout and resolution logic
* audit requirements for each hesitation event
* integration with Gateway decision cycles
* fallback logic for unresolved uncertainty

### **How it is used**

Any ambiguity forces the system into a reversible pause rather than letting a harmful or mistaken action proceed.

The protocol operationalizes:
**Pause when truth is uncertain.**

---

# **📘 5. Merkle Anchoring & Ledger Format**

**File:** `Merkle_Anchoring_and_Ledger_Format.md`
**Purpose:** Defines the immutable evidence backbone.
All decisions (Proceed/Hesitate/Refuse) are logged, hashed, batched, and anchored to one or more public blockchains.

### **What it specifies**

* deterministic hashing rules
* Merkle batch construction
* anchor proof format
* verification procedure for audits
* log retention and integrity requirements
* deferred anchoring for high-frequency systems
* chain-agnostic time-stamping

### **How it is used**

This creates the **tamper-evident history** required for regulatory compliance, post-incident forensics, and trust.

The rule is simple:
**If it isn’t anchored, it didn’t happen.**

---

# **📘 6. Adapter Reference Implementations**

**File:** `TML_Adapter_Reference_Implementations.md`
**Purpose:** Shows engineers how to integrate TML with ANY model, API, or system.

### **What it specifies**

* the required adapter interface (generate_UDE, safe_fallback, etc.)
* Inline, Sidecar, Supervisory, and Hybrid adapters
* domain-specific mapping rules for:

  * LLMs
  * weather models
  * medical imaging
  * AV perception & control stacks
  * robotics & industrial systems
  * financial and high-frequency trading systems
* real JSON UDE examples
* end-to-end decision flow examples

### **How it is used**

Adapters are the **bridge** between raw model outputs and TML’s governance architecture.
They guarantee consistency across wildly different AI systems.

---

# **📘 How the Six Files Work Together**

Below is the complete flow of how TML governs an AI system:

```
MODEL OUTPUT
     ↓
Adapter (File 6)
     ↓
UDE Formation (File 1)
     ↓
TML Gateway evaluates (File 2)
     ↓
IF uncertainty → Sacred Pause (File 4)
     ↓
IF model black-box / physical-world → Supervisory (File 3)
     ↓
Decision Record logged & hashed
     ↓
Anchoring (File 5)
     ↓
ACTION EXECUTION (only if PROCEED)
```

This gives you:

* governance
* traceability
* accountability
* safety
* auditability
* legal defensibility

Every action has a reason, a record, and a proof.

---

# **📘 Implementation Checklist**

To integrate TML into any real system:

1. **Wrap your model with an Adapter**
   Follow the patterns in File 6.

2. **Generate a valid UDE**
   File 1 defines the canonical structure.

3. **Submit UDEs to the Gateway**
   File 2 defines evaluation and decision protocols.

4. **Honor Hesitation (Sacred Pause)**
   File 4 governs how uncertainty must be handled.

5. **Use Sidecar or Supervisory control for black-box or kinetic systems**
   File 3 defines how to enforce safety externally.

6. **Anchor the Decision Record**
   File 5 provides the evidence format and chain protocol.

Once all six are connected, your system becomes fully TML-compliant:
**no silent failures, no unlogged actions, no unverified decisions.**

