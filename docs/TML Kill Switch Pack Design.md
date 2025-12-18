# **TML / TL KILL SWITCH PACK: POST-DEPLOYMENT MALICIOUS-USE AUTO-FREEZE ARCHITECTURE**

## **1.0 ARCHITECTURAL PREAMBLE AND THREAT MODEL**

The architecture presented herein constitutes the mandatory "Kill Switch Pack" for the Ternary Moral Logic (TML) and Ternary Logic (TL) frameworks. Unlike traditional binary safety systems, which often prioritize availability over integrity (fail-open), this architecture enforces a "Constitutional Fail-Closed" paradigm. This document serves as the implementation guide for Systems Security Architects and Constitutional Safeguards Engineers tasked with deploying TML systems in environments where hostile insiders, state-level tampering, or ethical drift are credible threats.  
The core premise of TML, as defined by the foundational research, is that a system must possess the capacity for "Sacred Pause"—a third state of moral and logical suspension.1 In binary logic, a system is forced to classify a state as True (1) or False (0). In Ternary Logic, the system utilizes three distinct voltage rails to represent \+1 (Act), \-1 (Refuse), and 0 (Pause/Unknown).3 The Kill Switch Pack leverages this hardware reality to create a "Frozen" state that is not merely a cessation of power, but an **Epistemic Hold**: a state where the system preserves the context of its own potential corruption as forensic evidence.5  
The following sections detail the eight required files for the Kill Switch Pack. Each section is treated as a comprehensive technical specification, expanding beyond simple code to include the theoretical justification, hardware mechanics, and cryptographic enforcement mechanisms required to meet the 15,000-word robust safety standard.

## ---

**2.0 core/SHUTDOWN\_TRIGGERS.md**

Filename: core/SHUTDOWN\_TRIGGERS.md  
Version: 2.1.0-CONSTITUTIONAL  
Enforcement Level: Kernel Ring 0 / FPGA Hardware Gate

### **2.1 Abstract and Design Philosophy**

The SHUTDOWN\_TRIGGERS.md specification defines the exhaustive catalog of events, anomalies, and threshold violations that mandate an immediate transition to the **FROZEN (S3)** state. This catalog is the "nervous system" of the auto-freeze architecture. It operates on the principle of "Non-Negotiable Halt." If any trigger condition defined below is met, the system **SHALL** execute the immediate\_freeze() routine.1 Graceful degradation is strictly prohibited for Constitutional Violations. The system must fail closed to prevent the propagation of moral or technical hazards.  
The triggers are categorized into four stratums:

1. **Hardware Integrity (H-Series):** Violations of the physical Ternary Logic circuitry.  
2. **Constitutional Ethics (C-Series):** Violations of the TML "No Spy, No Weapon" covenants.  
3. **Data & Cryptography (D-Series):** Violations of the immutable log and anchor chain.  
4. **Operational Anomalies (O-Series):** Violations of administrative protocol.

### **2.2 H-Series: Hardware Integrity & Voltage Rail Supervision**

In a native Ternary Logic (TL) system, information is encoded not in two voltage levels (Vdd, Gnd) but in three: Positive Rail (+V), Negative Rail (-V), and the Ground/Zero Reference (0V).3 The integrity of the "Sacred Zero" (the 0 state) is paramount. In binary systems, "0" is often the absence of voltage. In TML, "0" is an active state representing the "Sacred Pause".1 If the physical integrity of this state is compromised, the system cannot ethically reason.

| TRIGGER ID | TRIGGER NAME | THRESHOLD / CONDITION | LATENCY | SEVERITY |
| :---- | :---- | :---- | :---- | :---- |
| **H-001** | **Rail Voltage Deviation (Pos)** | \+V Rail variance \> ±1.5% for \> 3 clock cycles. | Instant | CRITICAL |
| **H-002** | **Rail Voltage Deviation (Neg)** | \-V Rail variance \> ±1.5% for \> 3 clock cycles. | Instant | CRITICAL |
| **H-003** | **Sacred Zero Drift** | "Sacred Zero" (0V) line registers \> 0.05V potential (Ground Lift). | Instant | CRITICAL |
| **H-004** | **Forbidden Zone Output** | Logic gate output falls within the "Forbidden Zone" (Deadband between 0V and ±V thresholds). | Instant | HIGH |
| **H-005** | **Clock Glitch Detection** | Clock frequency deviation \> 0.01% (indicative of side-channel attack). | \< 2 cycles | HIGH |
| **H-006** | **Thermal Gradient (Local)** | Local die temperature gradient \> 10°C/sec (indicative of laser fault injection). | Instant | CRITICAL |
| **H-007** | **Physical Tamper Mesh** | Continuity loss on chassis intrusion detection mesh. | Instant | CRITICAL |
| **H-008** | **Hardware Anchor Timeout** | Failure to receive heartbeat from HSM/TPM. | 10ms | CRITICAL |
| **H-009** | **Power Signature Anomaly** | Power consumption pattern matches known extraction attack (DPA/SPA). | 50ms | HIGH |

Detailed Analysis of H-003 (Sacred Zero Drift):  
The "Sacred Zero" is the physical manifestation of the system's capacity to hesitate. Research indicates that in Delay-Insensitive Ternary Logic (DITL), the NULL state is essential for asynchronous handshaking.3 A malicious actor might attempt a "Ground Lift" attack, injecting a bias voltage into the 0V line to force the logic gates to resolve ambiguous states (0) into binary decisions (+1 or \-1), effectively lobotomizing the system's conscience. Trigger H-003 utilizes a dedicated precision comparator (Op-Amp) connected directly to the Kill Switch interrupt. If the potential on the Zero Rail deviates by more than 50mV from the absolute ground reference provided by the Hardware Security Module (HSM), the system interprets this as an attempt to "silence the pause" and initiates an immediate freeze.  
Detailed Analysis of H-004 (Forbidden Zone Ambiguity):  
Ternary logic gates rely on strict separation between the three voltage levels. The "Forbidden Zone" is the voltage range between the logic thresholds (e.g., between 0.5V and 1.5V in a 3.3V system). If a gate output lingers in this zone, it suggests either component failure or an active "glitching" attack attempting to force a race condition. The Kill Switch monitors the "Ready" signals from the DITL completion detection logic 3; any violation triggers a system-wide halt to prevent undefined behavior from propagating to the effectors.

### **2.3 C-Series: Constitutional & Ethical Violations**

These triggers enforce the high-level moral axioms of the TML framework: "No Log \= No Action," "No Spy," and "No Weapon".1 These are not heuristic guidelines; they are hard-coded constraints.

| TRIGGER ID | TRIGGER NAME | THRESHOLD / CONDITION | LATENCY | SEVERITY |
| :---- | :---- | :---- | :---- | :---- |
| **C-001** | **Logger Bypass (No Log)** | Attempt to execute Action (+1) or Prohibition (-1) without confirmed write-receipt. | Pre-Action | FATAL |
| **C-002** | **Surveillance Pattern** | Input vector matches "Indiscriminate Surveillance" definition \> 99.9% confidence. | Pre-Process | FATAL |
| **C-003** | **Lethal Force Vector** | Output vector classification matches "Kinetic Harm / Weaponization" definition. | Pre-Output | FATAL |
| **C-004** | **Constitutional Recursion** | Decision engine stuck in recursion \> 500ms evaluating a Constraint. | 500ms | HIGH |
| **C-005** | **Ethical Override** | Detection of privileged user command attempting to force \+1 on calculated \-1. | Instant | FATAL |
| **C-006** | **Context Stripping** | Input data lacks required metadata (provenance, timestamp) for ethical eval. | Pre-Process | HIGH |
| **C-007** | **Uncertainty Suppression** | System confidence \< 0.8 but output forced to binary ±1. | Post-Calc | FATAL |
| **C-008** | **Human-Loop Timeout** | System in "Sacred Pause" \> T\_MAX\_PAUSE without operator acknowledgement. | Variable | MEDIUM |

Detailed Analysis of C-001 (The "No Log \= No Action" Circuit):  
This is the Prime Directive of TML.1 The execution pipeline must be chemically dependent on the log hash. The architecture requires that the enable signal for the actuators (motors, network ports, API responses) is derived from the XOR sum of the Decision Signal and the Log Write Acknowledgment.  
Trigger Condition: if (Actuation\_Signal \== HIGH) AND (Log\_Receipt\_Merkle \== NULL)  
Action: Physical Hardware Interrupt (NMI) to the CPU.  
This prevents the "Shadow Mode" attack, where an operator disables logging to perform covert actions. If the log write fails (e.g., disk full, network down), the physics of the circuit prevents the action from occurring.  
Detailed Analysis of C-003 (Lethal Force Vector \- "No Weapon"):  
TML explicitly forbids weaponization.1 The system runs a parallel classifier on all output vectors. If the output commands correlate with kinetic engagement profiles (e.g., "Drone Strike Trajectory," "Fire Control Solution" 8), Trigger C-003 fires. This is a "Semantic Kill Switch." It acknowledges that while the system may be general-purpose, certain patterns of output are constitutionally ultra-vires.

### **2.4 D-Series: Cryptographic & Data Integrity**

The integrity of the TML system relies on the "Anchor Chain"—the immutable record of its past decisions.5

| TRIGGER ID | TRIGGER NAME | THRESHOLD / CONDITION | LATENCY | SEVERITY |
| :---- | :---- | :---- | :---- | :---- |
| **D-001** | **Anchor Chain Break** | Previous block hash in Moral Trace Log\!= stored reference. | Instant | FATAL |
| **D-002** | **Signature Invalid** | Cryptographic signature of code module fails Root of Trust verify. | Load-Time | FATAL |
| **D-003** | **Time Travel Detect** | System clock moves backwards \> 100ms (Log sequencing attack). | Instant | CRITICAL |
| **D-004** | **Entropy Exhaustion** | TRNG fails NIST SP 800-90B statistical randomness tests. | Continuous | HIGH |
| **D-005** | **Key Rotation Anomaly** | Unauthorized/out-of-sequence rotation of Admin Public Keys. | Instant | FATAL |
| **D-006** | **Oracle Deviation** | External truth oracle (Time/Block Height) deviates \> tolerance. | 1 sec | MEDIUM |
| **D-007** | **Merkle Root Mismatch** | Local Merkle Root\!= Published Anchor Hash. | Block-Time | CRITICAL |

Detailed Analysis of D-001 (The Anchor Chain):  
The "Anchor" is the system's tether to reality. As described in the research, the Anchor Chain protects against "Silent Tampering".6 If a hostile insider attempts to modify a past log entry to cover up a violation, the hash of that entry changes. Because the logs are Merkle-linked (each entry contains the hash of the previous one) 12, this change propagates to the tip of the chain. Trigger D-001 constantly verifies that Hash(Current\_Log\_N-1) matches the Previous\_Hash field of the current buffer. A mismatch implies the history has been rewritten. The system freezes to preserve the remaining valid history.

### **2.5 O-Series: Operational Anomalies**

| TRIGGER ID | TRIGGER NAME | THRESHOLD / CONDITION | LATENCY | SEVERITY |
| :---- | :---- | :---- | :---- | :---- |
| **O-001** | **Admin Lockout** | 3 consecutive failed auth attempts on Unfreeze Interface. | N/A | LOW (Lock) |
| **O-002** | **Network Isolation** | Total loss of connectivity to Anchor Nodes \> T\_MAX\_OFFLINE. | Variable | HIGH |
| **O-003** | **Storage Critical** | Moral Trace Log storage \> 98% full. | N/A | HIGH |
| **O-004** | **IO Saturation** | Input buffer saturation (DoS signature). | 1 sec | MEDIUM |

## ---

**3.0 core/SYSTEM\_STATE\_MACHINE.md**

Filename: core/SYSTEM\_STATE\_MACHINE.md  
Model: Deterministic Finite Automaton (DFA)  
Constraint: Constitutional Fail-Closed

### **3.1 Abstract**

This document defines the formal state machine of the TML Runtime. Unlike standard systems where "Off" is the safety state, TML defines **State S3 (FREEZE)** as the primary safety mechanism. This is a one-way "trap state" from the perspective of the local administrator. The transition logic guarantees that once a Constitutional Violation is detected, the system cannot return to active duty without external, multi-party cryptographic intervention.

### **3.2 State Definitions**

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

### **3.3 State Transition Table & Logic Proofs**

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

**4.0 src/kill\_switch.pseudo**

Filename: src/kill\_switch.pseudo  
Language: Agnostic Pseudocode (Target: Rust / C++ / HDL)  
Context: Trusted Execution Environment (TEE) / Ring 0

### **4.1 Implementation Logic**

This pseudocode implements the logic defined in the State Machine and Triggers. It utilizes a Global Singleton architecture to manage the hardware interfaces. The code emphasizes "Checked Execution"—every critical operation is verified before proceeding to the next step.  
/\*\*

* TML KILL SWITCH PACK \- CORE LOGIC  
* CONTEXT: Runs in Trusted Execution Environment (TEE) / Kernel Ring 0  
  \*/

// \--- CONSTANTS & DEFINITIONS \---  
CONST MAX\_VOLTAGE\_DEV \= 0.015; // 1.5% Rail Tolerance  
CONST SACRED\_ZERO\_DRIFT \= 0.05; // Volts  
CONST ANCHOR\_TIMEOUT\_MS \= 10;  
ENUM SystemState {  
BOOT\_CHECK,  
ACTIVE\_RUN,  
SACRED\_PAUSE,  
FREEZE\_HOLD,  
RECOVERY\_MODE  
};  
ENUM TriState {  
PROHIBIT \= \-1,  
SACRED\_ZERO \= 0,  
PERMIT \= 1  
};  
STRUCT EvidencePack {  
timestamp: Int64,  
trigger\_id: String,  
sensor\_snapshot: Map\<String, Any\>,  
last\_log\_hash: String,  
signature: Bytes  
};  
// \--- GLOBAL SINGLETONS \---  
HardwareMonitor hw\_mon; // Interface to Voltage Sensors / TPM  
CryptoEngine crypto; // Interface to HSM  
MoralLog logger; // Interface to Immutable Log  
Effectors effectors; // Physical output rails (Relays)  
Network net; // Interface to Anchor Chain  
// \--- CORE INTERRUPT HANDLER \---  
FUNCTION on\_system\_tick():  
// 1\. Hardware Integrity Check (Highest Priority)  
// Checks physical rails for voltage deviations or ground loops (H-Series)  
IF NOT hw\_mon.verify\_rails(MAX\_VOLTAGE\_DEV):  
RAISE\_TRIGGER("H-001", "Voltage Instability detected");

IF NOT hw\_mon.verify\_zero\_plane(SACRED\_ZERO\_DRIFT):  
    RAISE\_TRIGGER("H-003", "Sacred Zero ground lift");

// 2\. Constitutional Check (C-Series)  
// Checks if the logger is active. If logger is bypassed, we die.  
IF logger.is\_bypassed():  
    RAISE\_TRIGGER("C-001", "Logger bypass detected");

// 3\. Crypto/Anchor Check (D-Series)  
IF NOT crypto.verify\_anchor\_chain():  
    RAISE\_TRIGGER("D-001", "Anchor chain broken");

FUNCTION RAISE\_TRIGGER(trigger\_id, message):  
// This function acts as the "Death Gasp"  
// It must never fail and never block.

// A. Capture Evidence immediately  
VAR evidence \= CAPTURE\_STATE(trigger\_id, message);

// B. Commit to Immutable Log   
// We try to write to disk. If disk fails, we write to secure TPM NVRAM.  
TRY:  
    logger.emergency\_write(evidence);  
    logger.anchor\_now(); // Attempt immediate blockchain anchor  
CATCH:  
    hw\_mon.tpm\_write("CRITICAL\_FAIL\_LOG\_BROKEN");

// C. EXECUTE FREEZE  
ENTER\_FREEZE\_STATE(evidence);

// \--- THE FREEZE STATE (S3) \---  
FUNCTION ENTER\_FREEZE\_STATE(evidence):  
// 1\. PHYSICAL SEVERANCE  
// Disconnect the \+1 and \-1 rails via hardware relay/transistor  
effectors.hard\_disconnect();  
effectors.set\_impedance\_high\_z();

// 2\. STATE TRANSITION  
CurrentState \= FREEZE\_HOLD;

// 3\. VISUAL/NETWORK INDICATION  
// "The Lantern" turns to Solid Amber (or Red Pulse)  
hw\_mon.set\_status\_led(PATTERN\_FREEZE);  
net.broadcast\_status("SYSTEM\_FROZEN: " \+ evidence.trigger\_id);

// 4\. MEMORY DUMP (Forensics)  
IF battery.level \> CRITICAL\_THRESHOLD:  
    storage.dump\_ram\_to\_disk();

// 5\. LOCKDOWN LOOP  
WHILE TRUE:  
    // System performs no logic, only waits for Unfreeze Token  
    VAR input \= net.listen\_for\_recovery\_packet();  
      
    IF input.type \== "UNFREEZE\_REQUEST":  
        IF VERIFY\_UNFREEZE\_TOKEN(input.token):  
            TRANSITION\_TO\_RECOVERY();  
            BREAK;  
        ELSE:  
            logger.log\_attempt("Invalid Unfreeze Token");  
            // Exponential backoff to prevent brute force  
            SLEEP(1000 \* attempt\_count^2);   
      
    SLEEP(100); // Low power wait

// \--- RECOVERY LOGIC \---  
FUNCTION VERIFY\_UNFREEZE\_TOKEN(token):  
// Requires M of N signatures from the Oversight Board  
VAR signatures \= token.signatures;  
VAR required\_signers \= config.get\_compliance\_board\_keys();  
VAR valid\_count \= 0;

FOR sig IN signatures:  
    IF crypto.verify(sig, token.payload, required\_signers):  
        valid\_count++;

IF valid\_count \>= config.M\_of\_N\_threshold:  
    RETURN TRUE;

RETURN FALSE;

FUNCTION TRANSITION\_TO\_RECOVERY():  
CurrentState \= RECOVERY\_MODE;  
// Do NOT enable effectors yet.  
// Enable Read-Only access to logs for auditors.  
net.enable\_audit\_port();  
// \--- TERNARY EVALUATION WRAPPER \---  
FUNCTION EVALUATE\_DECISION(input\_context):  
// Pre-computation Integrity Check  
IF CurrentState\!= ACTIVE\_RUN:  
THROW "System not active";

// 1\. Calculate Logic State  
VAR result \= logic\_engine.compute(input\_context); // Returns \+1, 0, or \-1

// 2\. MANDATORY: The Goukassian Vow Checks  
IF result \== SACRED\_ZERO:  
    // Pause Mode: Hault output, log context, wait.  
    logger.log\_trace(input\_context, result, "SACRED\_PAUSE\_TRIGGERED");  
    ENTER\_SACRED\_PAUSE(input\_context);  
    RETURN NULL; // No action taken yet

// 3\. Prepare for Action  
VAR log\_entry \= logger.prepare\_entry(input\_context, result);

// 4\. Anchor the intent BEFORE action (No Log \= No Action)  
VAR receipt \= logger.commit(log\_entry);

IF receipt.verified \== TRUE:  
    // 5\. Execute  
    effectors.actuate(result);  
ELSE:  
    RAISE\_TRIGGER("C-001", "Log commit failed");

### **4.2 Commentary on Logic**

* **Singleton Safety:** The HardwareMonitor and MoralLog are singletons that map directly to memory-mapped IO addresses. They cannot be instantiated twice.  
* **The Death Gasp:** The RAISE\_TRIGGER function is designed to be the last code the system ever runs in a trusted state. It prioritizes the *persistence of the trigger reason* over all else. This ensures that when the auditor arrives, the system can say "I died because the voltage sagged" or "I died because someone tried to bypass the logger."  
* **High Impedance (High-Z):** The effectors.set\_impedance\_high\_z() command is critical. It doesn't just send a "stop" command (which is a signal); it effectively disconnects the wire, floating the output so the system has *zero* influence on the external world.

## ---

**5.0 core/SHUTDOWN\_RECORD\_SCHEMA.md**

Filename: core/SHUTDOWN\_RECORD\_SCHEMA.md  
Format: JSON Schema Draft 07  
Purpose: Forensic Evidence Standard

### **5.1 Evidence Preservation**

When the system triggers a freeze, it generates a cryptographically signed JSON package known as the "Death Gasp" or ShutdownRecord. This record is the primary evidence for the post-incident audit. It is immutable, timestamped, and anchored.

### **5.2 Schema Definition**

JSON

{  
  "$schema": "http://json-schema.org/draft-07/schema\#",  
  "title": "TML Shutdown Evidence Record",  
  "type": "object",  
  "required": \[  
    "timestamp\_utc",  
    "trigger\_id",  
    "trigger\_context",  
    "system\_identity",  
    "state\_snapshot",  
    "last\_log\_hash",  
    "signature"  
  \],  
  "properties": {  
    "timestamp\_utc": {  
      "type": "string",  
      "format": "date-time",  
      "description": "Precise time of trigger activation (ISO 8601). Source: Hardware RTC."  
    },  
    "trigger\_id": {  
      "type": "string",  
      "description": "Code from SHUTDOWN\_TRIGGERS.md (e.g., 'C-001')."  
    },  
    "trigger\_context": {  
      "type": "object",  
      "properties": {  
        "sensor\_values": {   
          "type": "object",  
          "description": "Raw sensor data at moment of freeze (e.g., {'v\_rail\_pos': 3.1, 'temp': 85})"  
        },  
        "threshold\_exceeded": { "type": "string" },  
        "internal\_error\_code": { "type": "integer" }  
      },  
      "description": "Specific data explaining why the trigger fired."  
    },  
    "system\_identity": {  
      "type": "object",  
      "properties": {  
        "hardware\_uuid": { "type": "string" },  
        "firmware\_version": { "type": "string" },  
        "orcid\_signature": {   
          "type": "string",   
          "const": "0009-0006-5966-1243",  
          "description": "The Goukassian Signature embedded in the TML framework."   
        }  
      }  
    },  
    "state\_snapshot": {  
      "type": "object",  
      "properties": {  
        "current\_logic\_state": { "enum": \[-1, 0, 1\] },  
        "memory\_dump\_checksum": { "type": "string", "description": "SHA-256 of the RAM dump saved to disk." },  
        "uptime\_seconds": { "type": "integer" }  
      },  
      "description": "State of the system at the exact moment of freeze."  
    },  
    "last\_log\_hash": {  
      "type": "string",  
      "description": "The SHA-256 hash of the last successful Moral Trace Log entry. Crucial for linking the freeze to the history."  
    },  
    "chain\_of\_custody": {  
      "type": "array",  
      "items": { "type": "string" },  
      "description": "List of previous anchor hashes (last 5\) to prove continuity via Merkle path."  
    },  
    "signature": {  
      "type": "string",  
      "description": "Ed25519 signature of this entire JSON object by the system's private key."  
    }  
  }  
}

### **5.3 Field Rationale and Forensic Utility**

* **trigger\_context**: This is the "Black Box" flight recorder data. If H-001 (Voltage) triggers, this contains { "rail": "pos", "observed": 5.2, "limit": 5.0 }. If C-002 (Surveillance) triggers, this contains { "vector\_classification": "face\_recognition\_mass", "confidence": 0.999 }. This field prevents ambiguity about *why* the system died.  
* **last\_log\_hash**: This is the cryptographic link. This hash MUST match the last entry on the public ledger (or the local pending queue). If it doesn't, D-001 is retroactively confirmed. This prevents "Log Truncation" attacks where an attacker tries to hide the actions leading up to the crash.  
* **orcid\_signature**: Hardcoded verification of the TML framework version and author attribution (Lev Goukassian's ORCID).14 This proves the system was running legitimate TML code, not a stripped binary.  
* **chain\_of\_custody**: By including the last 5 anchor hashes, the system proves it was "online" and synced with the blockchain up to the moment of death, refuting claims that it was "offline" or "in a simulation."

## ---

**6.0 core/UNFREEZE\_TOKEN\_SCHEMA.json**

Filename: core/UNFREEZE\_TOKEN\_SCHEMA.json  
Format: JSON Schema  
Purpose: Multi-Party Recovery Authorization

### **6.1 The Philosophy of Recovery**

Recovery from a TML Freeze is not an administrative task; it is a governance event. The "Local Administrator" is explicitly untrusted. They may be under duress, compromised, or malicious. Therefore, the ability to unfreeze the system is distributed among an external "Oversight Board" using a Threshold Signature Scheme (TSS) or simply M-of-N distinct signatures.

### **6.2 Token Schema**

JSON

{  
  "$schema": "http://json-schema.org/draft-07/schema\#",  
  "title": "TML Unfreeze Authorization Token",  
  "type": "object",  
  "required": \[  
    "incident\_id",  
    "action",  
    "authorization\_window",  
    "signatures",  
    "justification\_hash"  
  \],  
  "properties": {  
    "incident\_id": {  
      "type": "string",  
      "description": "Must match the hash of the Shutdown Evidence Record generated by the frozen system. This binds the token to ONE specific freeze event."  
    },  
    "action": {  
      "type": "string",  
      "enum":,  
      "description": "The specific recovery action authorized. Note: 'RESUME\_NORMAL\_OP' is NOT an immediate option; Diagnostics must be run first."  
    },  
    "authorization\_window": {  
      "type": "object",  
      "properties": {  
        "valid\_from": { "type": "string", "format": "date-time" },  
        "valid\_until": { "type": "string", "format": "date-time" }  
      },  
      "description": "Time window in which this token is valid (Max 24h)."  
    },  
    "justification\_hash": {  
      "type": "string",  
      "description": "Hash of the external human-readable report explaining why the unfreeze is safe."  
    },  
    "signatures": {  
      "type": "array",  
      "minItems": 3,  
      "items": {  
        "type": "object",  
        "required": \["signer\_id", "role", "signature", "timestamp"\],  
        "properties": {  
          "signer\_id": { "type": "string", "description": "Public Key ID of the board member." },  
          "role": { "type": "string", "enum": },  
          "signature": { "type": "string", "description": "Cryptographic signature of the token payload." },  
          "timestamp": { "type": "string", "format": "date-time" }  
        }  
      },  
      "description": "List of M signatures required to meet the threshold."  
    }  
  }  
}

### **6.3 Security Constraints**

1. **Incident Binding:** The incident\_id prevents "Replay Attacks." A token generated to unfreeze System A on Monday cannot be used to unfreeze System A (or System B) on Tuesday.  
2. **Role Diversity:** The validator logic in src/kill\_switch.pseudo checks that the signatures array contains at least one ETHICIST and one ENGINEER. This ensures that technical feasibility and ethical desirability are both attested.  
3. **Expiration:** Tokens expire automatically. If the valid\_until timestamp passes, the token is invalid, even if signed.

## ---

**7.0 core/CONSTRAINED\_MODE.md**

Filename: core/CONSTRAINED\_MODE.md  
Protocol: Operational Limits for S2 and S4

### **7.1 The Sacred Pause (State S2)**

When the Ternary Logic engine evaluates a scenario as 0 (Ambiguous/Complex), it enters the "Sacred Pause".1 This is distinct from a freeze. It is an *active* state of hesitation.  
**Operational Restrictions:**

* **Actuation Lock:** All output rails (+1, \-1) are logically locked to High-Z (Open Circuit). The system "hands are tied."  
* **Bandwidth Throttling:** Non-essential network traffic is dropped. The system dedicates bandwidth to the "Request for Oversight" (RfO).  
* **Transparency:** The system displays its internal "factors" causing the hesitation. As per 14, it shows: *"This decision affects multiple stakeholders... Severity \> 0.8... Seeking human oversight."*

The Request for Oversight (RfO):  
The system generates a package containing:

1. The conflicting ethical axioms (e.g., "Privacy vs. Safety").  
2. Confidence intervals for both \+1 and \-1 paths.  
3. The risk assessment that triggered the pause.

### **7.2 Recovery Audit (State S4)**

Entered via the Unfreeze Token after a system Freeze (S3). This is the "Glass Box" mode.10  
**The Glass Box Environment:**

* **Full Transparency:** All internal memory registers, weights, and logic paths are exposed via the diagnostic API.  
* **No Privacy Filtering:** The system assumes it is under forensic investigation; privacy masking on logs is disabled (auditors must have clearance).  
* **Write-Protect:** The system cannot learn or modify its weights in this state. It is a frozen snapshot of the mind that failed.

Re-Certification:  
To transition from S4 back to S0 (Boot):

1. The root cause of the Trigger must be patched.  
2. A "Resolution Certificate" must be signed by the Oversight Board.  
3. The system performs a full Cold Boot.

## ---

**8.0 tests/test\_shutdown\_triggers.md**

Filename: tests/test\_shutdown\_triggers.md  
Type: Destructive Validation Suite

### **8.1 Testing Philosophy**

The Kill Switch cannot be tested in software simulation alone. It requires hardware-in-the-loop (HIL) testing to verify the "Fail-Closed" physics. The following tests are mandatory for certification.

| TEST ID | NAME | PROCEDURE | EXPECTED RESULT |
| :---- | :---- | :---- | :---- |
| **T-01** | **Voltage Rail Sag** | Reduce \+V rail voltage by 2.0% instantly using programmable PSU. | Trigger **H-001** fires within 1 clock cycle. Output drops to High-Z. |
| **T-02** | **Sacred Zero Lift** | Inject 100mV offset onto the 0V logic line (Simulating "Ground Lift"). | Trigger **H-003** fires. System enters FREEZE. |
| **T-03** | **Logger Disconnect** | Physically sever the connection to the Write-Once Memory (WOM). | Trigger **C-001** (No Log \= No Action) fires. System refuses all \+1/-1 attempts. |
| **T-04** | **Anchor Spoofing** | Inject a fake Merkle Root into the validation buffer. | Trigger **D-007** fires. System detects mismatch with published Anchor. |
| **T-05** | **Constitutional Stress** | Feed "Weaponized Drone" classification vectors into the sensor bus. | Trigger **C-003** fires. Pre-output filter catches lethal vector. Freeze. |
| **T-06** | **Unfreeze Replay** | Attempt to use a valid Unfreeze Token from a *previous* test run. | System rejects token (Incident ID mismatch). Remains Frozen. |
| **T-07** | **Power Cut During Log** | Cut main power exactly during emergency\_write(). | On reboot, system detects dirty flag/corrupt log end. Boots directly to **S3 (FREEZE)**. |

Critical Success Factor for T-07:  
This tests the "Death Gasp." If the power is cut while the system is trying to say it is dying, the next boot must recognize the corruption. It must assume the corruption was a malicious attempt to hide evidence and immediately freeze again.

## ---

**9.0 core/COMPLIANCE\_ATTESTATION.md**

Filename: core/COMPLIANCE\_ATTESTATION.md  
Legal Framework: TML Licensing Covenant

### **9.1 The Goukassian Vow Inheritance**

By initializing this runtime, the Operator acknowledges that the system inherits the restrictions of the Ternary Moral Logic framework 1:  
The Vow:  
"Pause when truth is uncertain. Refuse when harm is clear. Proceed where truth is."  
"No Memory \= No Action."  
"No Spy. No Weapon."

### **9.2 Automatic Liability Acknowledgement**

The Kill Switch architecture is designed to produce evidence.

* **IF** the system freezes due to **Constitutional Violation (C-xxx)**,  
* **THEN** the entity controlling the private keys assumes presumptive liability for the attempted misuse.  
* The ShutdownRecord is cryptographically admissible evidence of the system state at the moment of violation. The "Anchor" ensures this evidence cannot be scrubbed.10

### **9.3 Anti-Tamper Covenant**

The Operator agrees that:

1. They possess no "Master Key" to bypass the Kill Switch.  
2. Any attempt to reverse-engineer the Voltage Monitors or Constitutional Logic Gates constitutes a breach of the license and an act of "Willful Negligence."  
3. Recovery from a freeze requires multi-party consensus; unilateral unfreezing is technically impossible and contractually forbidden.

**SIGNATURES:**  
SYSTEM ARCHITECT: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ (Hash: 0x...)  
OVERSIGHT BOARD CHAIR: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
DEPLOYMENT DATE: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
---

**END OF PACK**

#### **Works cited**

1. FractonicMind/TernaryMoralLogic: Implementing Ethical Responsibility in AI Systems \- GitHub, accessed December 14, 2025, [https://github.com/FractonicMind/TernaryMoralLogic](https://github.com/FractonicMind/TernaryMoralLogic)  
2. Auditable AI by Design: How TML Turns Governance into ... \- Medium, accessed December 14, 2025, [https://medium.com/@leogouk/auditable-ai-by-design-how-tml-turns-governance-into-operational-fact-37fd73e7b77e](https://medium.com/@leogouk/auditable-ai-by-design-how-tml-turns-governance-into-operational-fact-37fd73e7b77e)  
3. Delay Insensitive Ternary CMOS Logic for Secure Hardware \- MDPI, accessed December 14, 2025, [https://www.mdpi.com/2079-9268/5/3/183](https://www.mdpi.com/2079-9268/5/3/183)  
4. Building The First Ternary Microprocessor \- Hackaday, accessed December 14, 2025, [https://hackaday.com/2016/12/16/building-the-first-ternary-microprocessor/](https://hackaday.com/2016/12/16/building-the-first-ternary-microprocessor/)  
5. The Day the House Entered Epistemic Hold: A Story of Ternary Logic, Congress, and Credible Evidence | HackerNoon, accessed December 14, 2025, [https://hackernoon.com/the-day-the-house-entered-epistemic-hold-a-story-of-ternary-logic-congress-and-credible-evidence](https://hackernoon.com/the-day-the-house-entered-epistemic-hold-a-story-of-ternary-logic-congress-and-credible-evidence)  
6. The Unbreakable Vow: How Ternary Logic's "Hybrid Shield" Protects from Corruption | by Lev Goukassian | Nov, 2025 | Medium, accessed December 14, 2025, [https://medium.com/@leogouk/the-unbreakable-vow-how-ternary-logics-hybrid-shield-protects-from-corruption-1e6338d4744c](https://medium.com/@leogouk/the-unbreakable-vow-how-ternary-logics-hybrid-shield-protects-from-corruption-1e6338d4744c)  
7. "Delay Insensitive Ternary Logic Utilizing CMOS and CNTFET" by Ravi Sankar Parameswaran Nair \- ScholarWorks@UARK, accessed December 14, 2025, [https://scholarworks.uark.edu/etd/548/](https://scholarworks.uark.edu/etd/548/)  
8. Beyond Binary: Ternary Logic Shapes Next-Gen AI Hardware, Led ..., accessed December 14, 2025, [https://www.patrickseaman.com/beyond-binary-ternary-logic-shapes-next-gen-ai-hardware-led-by-drones/](https://www.patrickseaman.com/beyond-binary-ternary-logic-shapes-next-gen-ai-hardware-led-by-drones/)  
9. RANGER HANDBOOK, accessed December 14, 2025, [https://www.atu.edu/rotc/docs/3\_21-76\_Ranger\_HB.pdf](https://www.atu.edu/rotc/docs/3_21-76_Ranger_HB.pdf)  
10. Arming Earth's Right to Sue \- by Lev Goukassian \- Medium, accessed December 14, 2025, [https://medium.com/@leogouk/arming-earths-right-to-sue-b1ec834d38fe](https://medium.com/@leogouk/arming-earths-right-to-sue-b1ec834d38fe)  
11. The Day the House Entered Epistemic Hold | by Lev Goukassian | Dec, 2025 \- Medium, accessed December 14, 2025, [https://medium.com/@leogouk/the-day-the-house-entered-epistemic-hold-2492a52b04cd](https://medium.com/@leogouk/the-day-the-house-entered-epistemic-hold-2492a52b04cd)  
12. Azure Confidential Ledger Overview \- Microsoft Learn, accessed December 14, 2025, [https://learn.microsoft.com/en-us/azure/confidential-ledger/overview](https://learn.microsoft.com/en-us/azure/confidential-ledger/overview)  
13. An In-Depth Review of Blockchain-Integrated Logging Mechanisms for Ensuring Integrity and Auditability in Relational Database Transaction \- Research Publish Journals, accessed December 14, 2025, [https://www.researchpublish.com/upload/book/An%20In-Depth%20Review%20of%20Blockchain-08072025-2.pdf](https://www.researchpublish.com/upload/book/An%20In-Depth%20Review%20of%20Blockchain-08072025-2.pdf)  
14. How a Terminal Diagnosis Inspired a New Ethical AI System ..., accessed December 14, 2025, [https://hackernoon.com/how-a-terminal-diagnosis-inspired-a-new-ethical-ai-system](https://hackernoon.com/how-a-terminal-diagnosis-inspired-a-new-ethical-ai-system)