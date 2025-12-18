## SHUTDOWN TRIGGERS

**Version:** 2.1.0-CONSTITUTIONAL  
**Enforcement Level:** Kernel Ring 0 / FPGA Hardware Gate

### **2.1 Abstract and Design Philosophy**

The SHUTDOWN TRIGGERS specification defines the exhaustive catalog of events, anomalies, and threshold violations that mandate an immediate transition to the **FROZEN (S3)** state. This catalog is the "nervous system" of the auto-freeze architecture. It operates on the principle of "Non-Negotiable Halt." If any trigger condition defined below is met, the system **SHALL** execute the immediate\_freeze() routine.1 Graceful degradation is strictly prohibited for Constitutional Violations. The system must fail closed to prevent the propagation of moral or technical hazards.  
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
