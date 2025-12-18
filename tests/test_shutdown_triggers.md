## Test Shutdown Triggers

**Type:** Destructive Validation Suite

### **Testing Philosophy**

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
