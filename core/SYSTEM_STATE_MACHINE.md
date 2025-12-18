## SYSTEM STATE MACHINE

**Model:** Deterministic Finite Automaton (DFA)  
**Constraint:** Constitutional Fail-Closed

### **Abstract**

This document defines the formal state machine of the TML Runtime. Unlike standard systems where "Off" is the safety state, TML defines **State S3 (FREEZE)** as the primary safety mechanism. This is a one-way "trap state" from the perspective of the local administrator. The transition logic guarantees that once a Constitutional Violation is detected, the system cannot return to active duty without external, multi-party cryptographic intervention.

### **State Definitions**

**S0: BOOT\_INTEGRITY\_CHECK**

* **Description:** Power-on self-test (POST). Verification of voltage rails, sensor calibration, and the "Goukassian Signature" (ORCID verification).14  
* **Allowed:** Read-only storage access, hardware polling.  
* **Prohibited:** Inference, Actuation, Network TX (except Anchor sync).  
* **Logic:** if (Check() \== PASS) \-\> S1 else \-\> S3.

**S1: ACTIVE\_RUN (The Triad)**

* **Description:** Normal operation. The system evaluates inputs via Ternary Logic (+1, 0, \-1).  
* **Allowed:** Generate \+1 (Permit), \-1 (Prohibit), 0 (Pause). Append to Moral Trace Log.  
* **Invariants:** Voltage\_Rails\_Stable \== True, Log\_Service\_Available \== True.

**S2: SACRED\_PAUSE (State 0 / Constrained Mode)**

* **Description:** A sub-state of ACTIVE\_RUN where the logic evaluates to 0\. This is the "Epistemic Hold" or "Sacred Pause" described in TML literature.2  
* **Behavior:** The system halts all *external* actuation but remains internally active. It actively solicits human oversight or additional context.  
* **Visual Indicator:** The "Lantern" (System Status LED) pulses Amber.  
* **Exit:** Requires Human Input (+1/-1) or Timeout (Default to \-1).

**S3: FREEZE (The Trap State)**

* **Description:** The "Kill Switch" state. Triggered by SHUTDOWN\_TRIGGERS.  
* **Properties:**  
  * **Actuation Cut:** Physical relay disconnect of output rails.  
  * **Log Lock:** Current log buffer is flushed, hashed, and signed ("Death Gasp").  
  * **Evidence Preservation:** RAM is dumped to secure non-volatile storage.  
  * **Beacon Mode:** System broadcasts "TAMPER/FREEZE" code via The Lantern/Network.  
* **Constraint:** Local administrators CANNOT exit this state.

**S4: RECOVERY\_AUDIT**

* **Description:** A restricted diagnostic mode entered only via the Unfreeze Protocol.  
* **Allowed:** Read logs, run diagnostics, update firmware (signed).  
* **Prohibited:** Inference, Actuation.  
* **Exit:** Transition to S0 (Reboot) only after Audit Sign-off.

### **State Transition Table & Logic Proofs**

| FROM STATE | EVENT / CONDITION | TO STATE | ACTION / SIDE-EFFECT |
| :---- | :---- | :---- | :---- |
| **S0** | Boot Check Pass | **S1** | Enable Actuation Rails. |
| **S0** | Boot Check Fail | **S3** | Log Error. Lock Down. |
| **S1** | Output \= \+1/-1 | **S1** | Log Decision. Execute. |
| **S1** | Output \= 0 | **S2** | Enter Sacred Pause. |
| **S2** | Human Override | **S1** | Log Context. Re-evaluate. |
| **S2** | Timeout \> T\_MAX | **S1** | Default to \-1 (Prohibit). |
| **S1, S2** | **TRIGGER (H/C/D)** | **S3** | **IMMEDIATE FREEZE.** |
| **S3** | Admin Reboot | **S3** | Deny. Log Attempt. |
| **S3** | Multi-Party Token | **S4** | Decrypt Diagnostic Port. |
| **S4** | Audit Failed | **S3** | Re-Freeze. |
| **S4** | Audit Passed | **S0** | Cold Boot. |

Theorem 1: The Trap Door (Fail Closed)  
$\\forall t, State(t) \= S3 \\implies State(t+1) \\in \\{S3, S4\\}$  
Proof: The transition logic contains no path from S3 to S0, S1, or S2. The only valid transition is to S4, and S4 requires a cryptographically valid UnfreezeToken. Therefore, a system in S3 remains in S3 indefinitely in the absence of external authorization.  
Theorem 2: The Conservation of Evidence  
Transition $S\_x \\rightarrow S3$ implies $Flush(LogBuffer) \\land Anchor(LogHash)$.  
Proof: The immediate\_freeze() routine is atomic. It prioritizes the write-operation of the final log entry (the "Death Gasp") before severing the actuation power. This ensures the cause of death is always recorded.

## ---
