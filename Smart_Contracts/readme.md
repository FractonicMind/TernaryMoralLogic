# TML Smart Contracts: Constitutional Code for Sovereign AI

## Overview

This directory contains the definitive technical specifications for the **Ternary Moral Logic (TML)** enforcement layer. Unlike traditional governance frameworks that rely on "soft law" (policy), these documents detail the implementation of "Hard Code"—a deterministic, immutable state machine deployed on EVM-compatible blockchains.

The architecture replaces the binary boolean (`true`/`false`) with a strict **Tri-State Logic** (`+1`, `0`, `-1`), ensuring that ethical ambiguity triggers a mathematical **Epistemic Hold** (The Sacred Zero) rather than an algorithmic error or reckless execution.

---

## Documentation Index

### [01_TML_System_Architecture_and_Ecosystem.md](/Smart_Contracts/01_TML_System_Architecture_and_Ecosystem.md)

**The Blueprint.**
This document outlines the high-level philosophy converted into engineering constraints. It details:

* **The "No Log = No Action" primitive:** Binding execution to cryptographic proof.


* **The Hybrid Shield:** A dual-layer defense system using multi-chain anchoring (Ethereum + Bitcoin).


* **The Goukassian Promise:** The licensing covenant (No Spy / No Weapon) enforced via Soulbound Tokens (SBTs).



### [02_TML_Technical_Specification_and_FSM.md](/Smart_Contracts/02_TML_Technical_Specification_and_FSM.md)

**The Code Logic.**
The rigorous engineering specification for the TML State Machine. It includes:

* **Finite State Machine (FSM):** Transitions between `STATE_ACTIVE`, `STATE_REVIEW_HOLD`, and `STATE_INTEGRITY_FROZEN`.


* **Solidity Interfaces:** Definitions for `ITMLEnforcer` and the `int8` Tri-State return values.


* **Gas Analysis:** Cost estimates for ethical verification vs. standard execution.



### [03_TML_Security_Audit_and_Adversarial_Analysis.md](/Smart_Contracts/03_TML_Security_Audit_and_Adversarial_Analysis.md)

**The Defense.**
A "No God Mode" proof and adversarial stress test. It demonstrates:

* **Irreversibility:** Mathematical proof that `STATE_INTEGRITY_FROZEN` has no exit transitions, preventing admin "rug pulls".


* **Always Memory:** The hybrid on-chain/off-chain storage architecture for auditability.


* **Attack Vectors:** Mitigation strategies for Oracle Fraud and Sybil Pausing.



### [04_TML_Governance_Whitepaper.md](/Smart_Contracts/04_TML_Governance_Whitepaper.md)

**The Human Interface.**
Details the "Human in the Loop" protocols for resolving the Sacred Zero. It covers:

* **The Stewardship Council:** A multi-sig software role constrained to resolving ambiguity, not overriding refusals.


* **Automated Penalties:** Smart contracts for immediate fine execution and license revocation.


* **The Memorial Fund:** Perpetual, code-governed distribution of funds to victims and research.



---

## Core Primitives

| Component | Function | State Representation |
| --- | --- | --- |
| **Enforcement Primitive** | Deterministic gatekeeper for all actions. | <br>`evaluateTransaction() -> int8` 

 |
| **Sacred Zero** | Mandated pause for ethical ambiguity. | <br>`STATE_REVIEW_HOLD` 

 |
| **Always Memory** | Immutable, Merkle-batched audit logs. | <br>`bytes32 merkleRootV1` 

 |
| **No God Mode** | Prevention of administrative override. | <br>`STATE_INTEGRITY_FROZEN` 

 |

## License

**TML-Constitutional-Code License**
*Code is Law, but Logic is Constitution.*

