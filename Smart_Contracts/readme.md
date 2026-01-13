# TML Smart Contracts: Constitutional Code for Sovereign AI

## Overview

This directory contains the definitive technical specifications for the **Ternary Moral Logic (TML)** enforcement layer. Unlike traditional governance frameworks that rely on "soft law" (policy), these documents detail the implementation of "Hard Code"—a deterministic, immutable state machine deployed on EVM-compatible blockchains.

The architecture replaces the binary boolean (`true`/`false`) with a strict **Tri-State Logic** (`+1`, `0`, `-1`), ensuring that ethical ambiguity triggers a mathematical **Epistemic Hold** (The Sacred Zero) rather than an algorithmic error or reckless execution.

---

## Documentation Index

### Core Specifications

### [01_TML_System_Architecture_and_Ecosystem.md](01_TML_System_Architecture_and_Ecosystem.md)
*(Available formats: .md, .pdf)*
**The Blueprint.**
This document outlines the high-level philosophy converted into engineering constraints. It details:
* **The "No Log = No Action" primitive:** Binding execution to cryptographic proof.
* **The Hybrid Shield:** A dual-layer defense system using multi-chain anchoring.
* **The Goukassian Promise:** The licensing covenant (No Spy / No Weapon) enforced via Soulbound Tokens (SBTs).

### [02_TML_Technical_Specification_and_FSM.md](02_TML_Technical_Specification_and_FSM.md)
*(Available formats: .md, .pdf, .html)*
**The Code Logic.**
The rigorous engineering specification for the TML State Machine. It includes:
* **Finite State Machine (FSM):** Transitions between `STATE_ACTIVE`, `STATE_REVIEW_HOLD`, and `STATE_INTEGRITY_FROZEN`.
* **Solidity Interfaces:** Definitions for `ITMLEnforcer` and the `int8` Tri-State return values.
* **Gas Analysis:** Cost estimates for ethical verification vs. standard execution.

### [03_TML_Security_Audit_and_Adversarial_Analysis.md](03_TML_Security_Audit_and_Adversarial_Analysis.md)
*(Available formats: .md, .pdf)*
**The Defense.**
A "No God Mode" proof and adversarial stress test. It demonstrates:
* **Irreversibility:** Mathematical proof that `STATE_INTEGRITY_FROZEN` has no exit transitions.
* **Always Memory:** The hybrid on-chain/off-chain storage architecture for auditability.
* **Attack Vectors:** Mitigation strategies for Oracle Fraud and Sybil Pausing.

### [04_TML_Governance_Whitepaper.md](04_TML_Governance_Whitepaper.md)
*(Available formats: .md, .pdf, .html)*
**The Human Interface.**
Details the "Human in the Loop" protocols for resolving the Sacred Zero. It covers:
* **The Stewardship Council:** A multi-sig software role constrained to resolving ambiguity.
* **Automated Penalties:** Smart contracts for immediate fine execution and license revocation.
* **The Memorial Fund:** Perpetual, code-governed distribution of funds to victims and research.

---

### Infrastructure & Evidence Layers

### [05_Ethereum_as_Constitutional_Infrastructure.md](05_Ethereum_as_Constitutional_Infrastructure.md)
**The Muscle (Compute).**
Defines why the Ethereum Virtual Machine (EVM) is the designated execution layer for TML.
* **State Enforcement:** Using the global computer to block non-compliant state transitions.
* **Smart Contract Sovereignty:** Ensuring the logic runs without centralized interference.

### [06_Bitcoin_as_Immutable_Evidence.md](06_Bitcoin_as_Immutable_Evidence.md)
**The Memory (Truth).**
Explains the use of Bitcoin's thermodynamic finality as the ultimate anchor for moral facts.
* **Deep Storage:** Anchoring hash headers to the most secure ledger on Earth.
* **Fact vs. Opinion:** Separating the execution of logic (ETH) from the proof of history (BTC).

### [07_Polygon_as_Throughput_Anchor.md](07_Polygon_as_Throughput_Anchor.md)
**The Nervous System (Speed).**
Details the high-frequency logging layer for rapid decision-making.
* **O(1) Scalability:** Handling thousands of moral micro-decisions per second.
* **Cost Efficiency:** preventing "ethics tax" from making safety economically unviable.

### [08_OpenTimestamps_as_the_Immutable_Witness_Layer_for_TML.md](08_OpenTimestamps_as_the_Immutable_Witness_Layer_for_TML.md)
*(Available formats: .md, .html)*
**The Witness (Proof).**
The technical specification for the hash anchoring protocol that binds TML to thermodynamic time.
* **The Sacred Zero Receipt:** How to generate a portable `.ots` file proving the AI hesitated.
* **Merkle Aggregation:** The cryptographic mechanics of batching evidence without gas fees.
* **Self-Sovereign Evidence:** Proofs that survive the collapse of the issuing institution.

---

## Source Code & Implementation

### [`/src`](src)
**The Engine Room.**
This directory contains the live implementation of the TML protocols, separating logic, storage, and interfaces.

| File | Type | Description |
| :--- | :--- | :--- |
| **`TML_Core.sol`** | Solidity | **The Kernel.** The primary logic contract that enforces the Finite State Machine (FSM) and validates Tri-State transitions. |
| **`TML_Storage.sol`** | Solidity | **The Vault.** Handles the immutable storage of moral logs, ensuring separation of data from logic (Upgradeability pattern). |
| **`ITMLEnforcer.sol`** | Solidity | **The Standard.** The strict interface definition ensuring all TML-compliant agents adhere to the same external API. |
| **`AI_Bridge.py`** | Python | **The Synapse.** The middleware script that translates off-chain AI reasoning (Python/PyTorch) into on-chain transactions. |
| **`Deploy_TML.js`** | JavaScript | **The Genesis.** Deployment scripts for spinning up the TML ecosystem on Ethereum/Polygon testnets or mainnets. |
| **`TML_Config.json`** | JSON | **The Parameters.** Configuration file defining system constants, gas limits, and initial governance addresses. |

### [TML_Smart_Contract_Architecture_Executive_Summary.pdf](TML_Smart_Contract_Architecture_Executive_Summary.pdf)
**Executive Brief.**
A concise, high-level summary of the entire architecture suitable for stakeholders, legal review, and non-technical auditing.

---

## Core Primitives

| Component | Function | State Representation |
| :--- | :--- | :--- |
| **Enforcement Primitive** | Deterministic gatekeeper for all actions. | `evaluateTransaction() -> int8` |
| **Sacred Zero** | Mandated pause for ethical ambiguity. | `STATE_REVIEW_HOLD` |
| **Always Memory** | Immutable, Merkle-batched audit logs. | `bytes32 merkleRootV1` |
| **No God Mode** | Prevention of administrative override. | `STATE_INTEGRITY_FROZEN` |
| **The Witness** | Thermodynamic proof of hesitation. | `.ots` (OpenTimestamps) |

## License

**TML-Constitutional-Code License** ***Code is Law, but Logic is Constitution.***

```
