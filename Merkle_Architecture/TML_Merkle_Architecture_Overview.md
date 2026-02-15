# **Structural, Adversarial, and Availability-Hardened Merkle Architecture for Ternary Moral Logic (TML)**


**Lev Goukassian**  
Architect of Ternary Moral Logic  
Santa Monica, California

**ORCID: [0009-0006-5966-1243](https://orcid.org/0009-0006-5966-1243)**

February 14, 2026

[**Interactive Version:**](https://fractonicmind.github.io/TernaryMoralLogic/Merkle_Architecture/TML_Merkle_Architecture_Overview.html) *This document is available as a live web artifact containing Structural, Adversarial, and Availability-Hardened Architecture formatting.*



## **Merkle as a Core Structural Component of TML**

The fundamental architecture of Ternary Moral Logic (TML) establishes a paradigm shift in AI governance by moving from post-hoc auditing to real-time, architectural enforcement. At the center of this transition is the Merkle tree, which functions as the primary structural component ensuring that every autonomous action is preceded by a verifiable and immutable record.1 In TML, the Merkle tree is not an optional logging enhancement; it is the mathematical backbone that operationalizes ethical constraints. Without this structure, the system’s core logical states—Permissible (+1), Impermissible (-1), and the Sacred Zero (0)—would lack the evidentiary weight required for legal and intergenerational review.4   
Merkle structures are intrinsic to TML's ethical guarantees because they provide a mechanism for constant state-transition validation. In traditional AI systems, a decision log is a separate artifact that can be deleted, truncated, or modified by a malicious insider or a system failure. In TML, the execution of an action is cryptographically coupled to the commitment of its corresponding Moral Trace Log within a Merkle tree.7 If the Merkle structure is removed, several critical TML properties collapse: the "No Log \= No Action" mandate becomes unenforceable, causal ordering of events is lost, and the ability to detect silent bypasses of the Sacred Zero state is eliminated.6   
The "Sacred Zero" represents a state of epistemic hold or recognized complexity.7 Merkle trees freeze these outcomes as immutable moral states by requiring that the hash of the log—which includes the reasoning and context for the pause—be included in the current Merkle batch before the system can finalize its next operational state.7 This ensures that even "hesitation" is captured as a permanent data point, preventing the AI or its operators from retroactively reinterpreting a moment of uncertainty as a definitive approval.8   
Contextual integrity is further enforced through the Active Axiom Set Hash. Every leaf in the TML Merkle tree includes a cryptographic commitment to the exact set of ethical rules and regulatory parameters active at the moment of the decision.7 This commitment ensures that the system is operating under a specific "Constitution of Code" and that any modification to these rules produces a new, distinct Axiom Hash. This prevents "moral drift" where system updates might silently relax ethical constraints or ignore specific legal mandates, such as the 26+ international human rights documents integrated into the TML framework.4  
The TML architecture utilizes hierarchical Merkle subtrees to reflect distinct ethical domains: Human Rights, Earth Protection, and Governance.6 This partitioning allows for specialized retention policies and verification protocols tailored to the requirements of each domain. For instance, the Earth Protection subtree may be optimized for long-term environmental auditability, while the Human Rights subtree might utilize ephemeral encryption and crypto-shredding to protect individual privacy while maintaining the hash continuity of the overall record.8   
Proof compression, a characteristic of Merkle architectures, enables scalable governance. Regulators do not need to replicate the entire dataset to verify compliance; instead, they can verify specific high-risk events using compact Merkle inclusion proofs.7 This scalability is essential for TML, which is designed to handle throughputs exceeding 10,000 decisions per second with sub-2ms visible inference latency.8   
Consider a scenario where an autonomous financial agent decides to execute a high-frequency trade in a volatile market. The TML engine detects that the market conditions exceed the "Ethical Uncertainty Score" (EUS) threshold, triggering a Sacred Zero.3 A Moral Trace Log is generated, hashed, and included in the Merkle batch. The resulting Merkle root is anchored to a public blockchain.7 Months later, during a forensic reconstruction of a market flash crash, the regulator requests proof of the agent's behavior. The Merkle structure prevents the financial institution from retroactively claiming the trade was a "Permit" decision; the inclusion proof for that sequence ID uniquely points to the Sacred Zero log, providing irrefutable evidence of the system's recognized complexity at the time of the event.8

## **Canonical Leaf Node Specification**

For the TML Merkle tree to function as a deterministic enforcement layer, the input data (the leaf nodes) must adhere to a strict canonical schema. This ensures that any change in the event data, no matter how minor, results in a completely different hash, thereby invalidating any associated proofs.7 The schema is designed to enforce contextual integrity by embedding versioned commitments directly into the event payload.

### **Mandatory Field Definitions**

The TML moral event schema requires the following fields to be present and serialized in a specific order:

| Field Name | Type | Security/Governance Purpose |
| :---- | :---- | :---- |
| Event ID | UUID v4 | Globally unique identifier to prevent collisions across different TML instances.7 |
| Monotonic Sequence ID | uint64 | Strictly increasing counter to enforce causal ordering and detect truncation.7 |
| Trusted Timestamp | uint64 | eIDAS-qualified timestamp to prevent backdating of moral decisions.8 |
| Sacred Zero Trigger | float | The specific EUS or semantic proximity trigger that initiated the state transition.4 |
| Pillar Reference | enum | Identifies which moral domain (Human Rights, Earth, Governance) governed the event.14 |
| Risk Classification | uint8 | Categorization based on frameworks like the EU AI Act (e.g., Unacceptable, High).4 |
| Reflection Outcome | int8 | The final TML voice outcome (+1, 0, \-1) representing the system's "conscience".6 |
| Integrity Flags | bits | Hardware attestation status (e.g., TPM/TEE signatures) confirming enclave integrity.11 |
| Schema Version ID | uint16 | Incremental version to ensure log consumers can parse the data correctly.7 |
| Schema Hash Commitment | bytes32 | Keccak256 hash of the full schema definition to prevent silent field injection.7 |
| Active Axiom Set Hash | bytes32 | Cryptographic commitment to the rule-set active at event time.7 |
| Hash Algorithm Version | uint8 | Identifier for the cryptographic primitive used to hash this leaf.8 |

### **Active Axiom Set Hash Requirements**

The Active Axiom Set Hash is a critical field that represents the "constitutional state" of the system. It is generated by hashing the entire TML configuration, including the weightings of moral voices, the specific human rights instruments referenced (e.g., UDHR, Geneva Conventions), and the operational thresholds for the Sacred Zero.4 Any change to these rules, whether by a legitimate governance vote or a malicious developer modification, requires a version increment and the generation of a new Axiom Hash. Because this hash is embedded in every leaf node, it is impossible for an agent to claim it was following an older rule-set to justify an action that is prohibited under a newer one.7

### **Determinism and Privacy Requirements**

To ensure that the Merkle root is reproducible across different verification environments, TML mandates a canonical serialization format (e.g., Canonical JSON per RFC 8785 or a strict Protobuf definition). This includes:

* Strict field ordering (typically alphabetical or by field index).7  
* Rejection of non-deterministic values (such as unformatted floating-point numbers or local-dependent date strings).7  
* Explicit UTF-8 encoding for all text fields.  
* Locale independence in all numerical representations.

Privacy is preserved through a strict redaction-before-hashing protocol. TML explicitly prohibits the hashing of raw personal data. Instead, irreversible pseudonymization or zero-knowledge commitments are applied to sensitive fields before they are included in the leaf node.8 An audit trace of the redaction process itself—detailing what was redacted and by which authority—is stored in a separate, highly restricted log, while the public leaf contains only the redacted, hash-safe version of the event.8 Any mutation to the leaf data after the fact, even a change to a redacted field, invalidates the Merkle proof, ensuring that the integrity of the record is maintained even when the data is partially obscured for privacy.7

## **Merkle Tree Construction Model**

The TML Merkle tree construction model is optimized for high-throughput, real-time AI inference environments. While binary Merkle trees are the industry standard for blockchain and ledger systems, TML introduces a ternary geometry to better align the data structure with its triadic logical states (+1, 0, \-1).7

### **Hashing and Collision Resistance**

TML primarily utilizes SHA-256 for its leaf and internal node hashing due to its widespread hardware acceleration and proven collision resistance.8 However, to address the threat of long-term cryptographic degradation, the leaf schema includes a "Hash Algorithm Version ID," enabling a migration path to post-quantum resistant algorithms like SHA-3 (Keccak) or BLAKE3 without requiring a full system reset.8 The system relies on the assumption that the probability of a second-preimage attack—where an adversary finds a different Moral Trace Log that produces the same hash—is effectively zero ($\\approx 2^{-256}$), which is sufficient for legal evidence standards under FRE 901/902.8

### **Ternary Geometry and Mathematical Modeling**

The TML ternary Merkle tree uses a branching factor of $k=3$. This geometry is selected because it provides a more natural semantic mapping to the TML states: the first child branch corresponds to Permissible events (+1), the second to Indeterminate/Sacred Zero events (0), and the third to Impermissible events (-1).10  
**Mathematical Depth and Proof Size Comparison:**  
For a tree with $N$ leaves, the depth $D$ and proof size $P$ are calculated as follows:

| Feature | Binary Tree (k=2) | Ternary Tree (k=3) |
| :---- | :---- | :---- |
| Depth ($D$) | $\\lceil \\log\_2 N \\rceil$ | $\\lceil \\log\_3 N \\rceil$ |
| Proof Nodes per Level | $1$ | $2$ |
| Total Proof Size | $D \\times 32 \\text{ bytes}$ | $2D \\times 32 \\text{ bytes}$ |
| Example ($N=10^6$) | $D \\approx 20, P \\approx 640 \\text{ bytes}$ | $D \\approx 13, P \\approx 832 \\text{ bytes}$ |

While ternary trees result in slightly larger proofs, the reduction in tree depth reduces the number of hashing operations required to verify a path during high-frequency resolution events in the "Slow Lane".7 The CPU and memory overhead for constructing a ternary tree is approximately 1.5x higher than a binary tree, but this is mitigated by the asynchronous "Anchoring Lane" and the use of dedicated Audit Processing Units (APUs) or FPGA offload for cryptographic operations.8

### **Construction Requirements**

TML construction is strictly asynchronous to ensure it does not block the "Inference Lane," which must maintain $\\le 2$ ms latency.10 A rolling buffer with an integrity checksum collects leaf hashes. Once the buffer reaches a pre-defined batch size (e.g., 1,000 to 10,000 events) or a time-out occurs (e.g., 500 ms), the tree is built.7  
The construction process must follow these rules:

* **Deterministic Leaf Placement:** Leaves are placed based on their Monotonic Sequence ID. This ensures that any attempt by an attacker to reorder events to change their causal relationship is immediately detectable.7  
* **Odd-Leaf Handling:** In cases where the number of leaves is not a power of 3, TML utilizes node duplication or a specific null-hash padding (e.g., $H(0)$) to maintain a balanced tree structure.  
* **Balanced Tree Enforcement:** The system ensures that the tree remains balanced to provide consistent logarithmic proof sizes, preventing performance degradation for older events.7

Replay protection is enforced by checking the globally unique Event ID and the Monotonic Sequence ID against the "Always Memory" registry. Any attempt to re-anchor a previously committed log is rejected, and an anomaly signal is emitted to the governance monitors.7

## **Hierarchical Integrity Model**

To support the modular governance of complex AI systems, TML employs a hierarchical integrity model. Instead of a single flat Merkle tree for all events, the system maintains separate subtrees for Human Rights, Earth Protection, and Governance.6

### **Master Root and Aggregation**

The roots of the individual subtrees are themselves hashed together to form a higher-order Master Root. This Master Root is what is eventually anchored to public blockchains.6 This "Root-of-Roots" versioning allows the system to guarantee the integrity of multiple ethical domains simultaneously while providing subtree continuity. For example, a regulator interested only in Human Rights violations can download only the Human Rights subtree and verify it against the Master Root without needing to process the high-volume Governance data.7

### **Forward Integrity Safeguards**

To prevent an attacker with log write access from retroactively modifying historical roots, TML establishes a forward hash chain. Each new Master Root ($R\_t$) must include a cryptographic reference to the previous Master Root ($R\_{t-1}$):

$$R\_t \= H(AggregatedSubtreeRoots\_t \\parallel R\_{t-1} \\parallel Timestamp\_t \\parallel MaxSequenceID\_t)$$  
This creates an unbroken chain of moral history. Any attempt to delete an intermediate root or truncate the log would break the chain, alerting any verifier who has a copy of the most recent anchored root.7

## **Anchoring Strategy**

The TML anchoring strategy, known as the "Hybrid Shield," ensures that the integrity of the Merkle tree is bound to multiple external, high-security ledgers. This protects the system against an infrastructure operator who might attempt to delay or suppress the anchoring of an incriminating log.3

### **Time-Bound Enforcement**

TML enforces an explicit maximum anchoring delay (MaxAnchorDelay) of 500 ms (P95) for the anchoring process to complete once a batch is finalized.8 An automatic anchoring trigger is activated by:

* Reaching the batch capacity.7  
* The occurrence of a Sacred Zero event that requires immediate external verification.7  
* A periodic heart-beat timer (e.g., every 10 seconds).8

The multi-chain anchoring strategy involves publishing the Master Root to Bitcoin (via OpenTimestamps), Ethereum, and Polygon.6 This redundancy ensures that even if one network is compromised or suffers a partition, the TML record remains verifiable on others.9

### **Time Integrity and Reconciliation**

Time integrity is maintained by binding the root hash to the block height and timestamp of the host blockchain. This prevents backdating attacks, as the blockchain acts as a decentralized trusted timestamping authority. The TML reconciliation protocol continuously monitors the anchoring history. If it detects a missing root interval or a discrepancy between the local log and the anchored root, it initiates a mandatory anomaly logging event and halts all high-risk actions.9

## **Causal Integrity Enforcement (Sacred Zero Protection)**

The most critical function of the TML Merkle architecture is the protection of the Sacred Zero state. The system must provide a formal guarantee that a Sacred Zero log commitment occurs before or atomically with the inference output.7

### **Atomic Snapshot Boundary**

When a moral conflict is detected, the TML enforcer contract defines an atomic snapshot boundary. This boundary includes the current input context, the reasoning logic path, and the hash of the preceding committed log.7 The system creates a "Pause Record" in the "Always Memory" registry, which acts as a cryptographic interlock.

### **Execution Interlock**

The TML "No Log \= No Action" interlock dictates that:

* An inference output (the decision) must include a reference to the committed log hash.7  
* Any output produced without a corresponding, verifiable log hash in the Always Memory registry is considered invalid and will be rejected by the governed system's hardware or execution environment.7  
* This prevents a malicious actor or a "God Mode" administrator from silently bypassing the Sacred Zero to execute an unethical action without a forensic trail.7

## **Proof Generation and Verification**

To fulfill its role as a "Constitution of Code," TML must enable independent third-party verification of its moral history without requiring the verifier to download the entire system state.7

### **Light Client and SPV Specification**

TML specifies a Simple Payment Verification (SPV) model allowing a regulator or user to verify a single event on a standard laptop or mobile device.7  
**Verification Protocol Workflow:**

1. **Input:** The verifier receives the Event Payload ($P$), the Merkle Inclusion Proof (a set of sibling hashes $S\_1, S\_2,... S\_D$), and a reference to the anchored Master Root ($R\_{anchor}$).7  
2. **Step 1:** The verifier computes the leaf hash $H \= \\text{Hash}(P)$ following the canonical serialization rules.7  
3. **Step 2:** The verifier iteratively hashes $H$ with the sibling hashes $S\_i$ to calculate the expected root $R\_{calc}$.7  
4. **Step 3:** The verifier queries a public blockchain node (e.g., Infura for Ethereum or a Bitcoin block explorer) to retrieve the value of $R\_{anchor}$.8  
5. **Step 4:** The verifier asserts $R\_{calc} \== R\_{anchor}$. If true, the event is verified as authentic and unaltered.7

Verification failure handling requires that if Step 4 fails, the client must automatically log a "Compliance Violation" and request a full forensic reconstruction of the affected batch.11

### **Key Security and Crypto-Shredding**

To balance immutability with privacy and the "right to be forgotten," TML utilizes ephemeral encryption keys stored in hardware-backed storage (HSMs).8

* **Key Rotation:** Encryption keys for Moral Trace Logs are rotated every 24 hours to limit the blast radius of a potential key compromise.  
* **Crypto-Shredding:** When a data retention period expires or a deletion request is granted, the decryption key for the specific event is destroyed.8  
* **Hash Continuity:** Because the Merkle tree only stores the *hash* of the encrypted data, the destruction of the key does not invalidate the Merkle root. The proof of the event's occurrence and its logic remains part of the immutable record, but the sensitive context is rendered permanently unreadable, fulfilling the requirements for intergenerational review without violating individual privacy.8

## **Data Availability (DA) Strategy**

A Merkle root that refers to data that can no longer be retrieved is a failure of TML's governance guarantees.3 Therefore, TML defines a redundant and resilient Data Availability (DA) strategy.

### **Redundant Storage Model**

Encrypted pre-hash event data is stored using a tiered approach to ensure both performance and long-term durability.6

| Storage Tier | Technology | Purpose | Geographic Distribution |
| :---- | :---- | :---- | :---- |
| Tier 1: Cache | NVMe SSD Clusters | Fast retrieval for real-time human oversight.7 | Local to AI Engine |
| Tier 2: Institutional | Private Hyperledger Fabric | High-availability record keeping for the operator.18 | Multi-region Cloud |
| Tier 3: Decentralized | Arweave or IPFS | Long-term, permanent storage resilient to operator failure.8 | Global P2P Network |
| Tier 4: Regulatory | Secure Escrow | Legal preservation for "intergenerational review".3 | Multi-institutional |

TML requires a "Proof-of-Storage" or availability attestation mechanism where the decentralized storage provider must periodically prove that they still hold the data associated with a specific Merkle root.8 If the primary operator's storage fails, the data rehydration workflow allows a regulator to use the anchored Merkle root and the inclusion proofs to pull and verify the original logs from the decentralized or regulatory tiers.3

## **Log Truncation and Tamper Resistance**

TML is designed to be resistant to both external attackers and malicious insiders who might attempt to truncate the log to hide historical errors.

### **Append-Only Storage Enforcement**

The "Always Memory" component is an append-only registry where once a hash is written, it cannot be modified or deleted without invalidating the Master Root.6 The system performs periodic integrity checks to detect missing Monotonic Sequence IDs. Any gap in the sequence triggers an automatic anomaly signaling event to the Stewardship Council.7

### **Schema Governance**

The schema of the TML logs is itself a governed entity. A signed schema registry tracks all valid versions. Dual control is required for schema updates: any change must be approved by both a Technical Council and a Stewardship Council.7 The hash of the active schema is independently anchored to ensure that even the *rules for recording the truth* cannot be silently changed.7

## **Latency and Throughput Modeling**

One of the most significant challenges for TML is ensuring that its rigorous cryptographic guarantees do not degrade the performance of real-time AI systems.8

### **Quantified Computational Overhead**

The "Dual-Lane" architecture separates the synchronous inference logic (the Fast Lane) from the asynchronous cryptographic anchoring (the Slow Lane).7  
**Numerical Scenario: 10,000 Events Per Second**

* **Inference Latency:** The visible overhead for a user is $\\le 2$ ms. This is achieved by performing only the leaf hashing and signature verification in the synchronous path.8  
* **Batching and Hashing:** For a batch of 10,000 events, the system must perform $\\sim 10,000$ leaf hashes and $\\sim 15,000$ internal node hashes (for a ternary tree). Using an FPGA-accelerated APU, this total batch hashing can be completed in $\< 100$ ms.10  
* **Anchoring Latency:** The "full sealing" of the batch (building the tree and submitting the root to Ethereum/Polygon) is targeted at $\\le 500$ ms (P95).8

Sustainable event rates are maintained by a parallel construction strategy, where multiple threads build subtrees in parallel before they are aggregated into the Master Root.8

## **Formal Integrity Guarantees**

The TML Merkle architecture provides the following formal guarantees under its specified threat model:

* **Collision Resistance:** Based on the SHA-256 assumption, it is computationally infeasible to find two different moral events that produce the same leaf hash.8  
* **Forward Integrity:** The use of forward hash chaining in the Master Root ensures that once a root is anchored, all prior moral history is locked against retroactive modification.7  
* **Survivability:** The multi-chain anchoring strategy ensures that the TML record survives even the collapse of a single blockchain network or the disappearance of the system operator.8

These guarantees degrade only under conditions of catastrophic cryptographic failure (e.g., a practical break of SHA-256) or the complete loss of all four storage tiers and all public blockchains, a scenario that TML considers outside its design-time risk threshold.3

## **Comparative Analysis of Merkle Architectures**

The TML Merkle architecture represents a synthesis of existing technologies adapted for the unique requirements of AI governance.7

| Feature | Bitcoin | Ethereum State Trie | Certificate Transparency | TML Architecture |
| :---- | :---- | :---- | :---- | :---- |
| **Branching** | Binary | Hexary Patricia | Binary | Ternary |
| **Logic** | Transactions | Account Balances | SSL Certificates | Triadic Moral Logic |
| **Latency** | 10 min | 12 sec | Seconds | $\\le 2$ ms |
| **Privacy** | Pseudonymous | Public | Public | ZK-Redacted |
| **Governance** | Miner Consensus | Staker Consensus | Domain Authorities | Tri-State Enforcers |

Unlike the Ethereum state trie, which is optimized for rapid account balance lookups, TML is optimized for the audit clarity and governance robustness required by legal systems. TML's use of ternary geometry provides a unique "semantic audit" capability where the structure of the tree itself reflects the ethical balance of the system.7

## **Failure Mode Disclosure**

TML acknowledges specific residual risks and conditions under which its guarantees fail:

1. **Malicious Insider with Key Access:** If an insider obtains both a partial encryption key and log write access, they could theoretically redact sensitive data *before* it is hashed, though they cannot change the logic or outcome without invalidating the Merkle proof.8  
2. **Delayed Anchoring:** A malicious infrastructure operator could delay anchoring to suppress a log. TML mitigates this with a numerical delay bound (500 ms) and a "Lantern Signal" that alerts external monitors if anchoring fails to occur.8  
3. **Data Loss Event:** A catastrophic failure of all storage tiers would leave the system with an anchored root but no retrievable data, which constitutes a total failure of the governance guarantee.3  
4. **Long-term Cryptographic Degradation:** Over a 50-year horizon, the security of SHA-256 may diminish. TML's migration path and periodic re-rooting are required to maintain intergenerational integrity.8

By embedding these architectural choices, TML transforms AI ethics from a design-time aspiration into a runtime, evidentiary substrate that is both resilient to adversarial attack and open to independent verification.5

---
## Document Control
| Attribute | Detail |
| :--- | :--- |
| **Document ID** | TML-STRAT-001 |
| **Version** | 1.0.0 |
| **Status** | **RELEASED** |
| **Classification** | **Strategic Framework** |
| **Author** | Lev Goukassian |
| **Date** | 2026-02-14 |

---

#### **Works cited**

1. Auditable AI: tracing the ethical history of a model \- ResearchGate, accessed February 14, 2026, [https://www.researchgate.net/publication/399129971\_Auditable\_AI\_tracing\_the\_ethical\_history\_of\_a\_model](https://www.researchgate.net/publication/399129971_Auditable_AI_tracing_the_ethical_history_of_a_model)  
2. Auditable AI: Tracing the Ethical History of a Model, accessed February 14, 2026, [https://papers.ssrn.com/sol3/Delivery.cfm/SSRN\_ID5655110\_code8713860.pdf?abstractid=5655110\&mirid=1\&type=2](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID5655110_code8713860.pdf?abstractid=5655110&mirid=1&type=2)  
3. Ternary Logic (TL): Evidentiary Framework for Economic Systems by ..., accessed February 14, 2026, [https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=5695042](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5695042)  
4. Ternary Moral Logic (TML) and the EU AI Act \- SSRN, accessed February 14, 2026, [https://papers.ssrn.com/sol3/Delivery.cfm/SSRN\_ID5655090\_code8713860.pdf?abstractid=5655090\&mirid=1](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID5655090_code8713860.pdf?abstractid=5655090&mirid=1)  
5. Ternary Moral Logic (TML) and the EU AI Act: A Technical Backbone ..., accessed February 14, 2026, [https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=5655090](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5655090)  
6. FractonicMind/TernaryMoralLogic: I've always believed that the hardest problems in AI aren't technical; they're architectural. We keep building systems that can't explain themselves, can't prove their own integrity, can't handle uncertainty without either freezing or lying. And then we act surprised when \- GitHub, accessed February 14, 2026, [https://github.com/FractonicMind/TernaryMoralLogic](https://github.com/FractonicMind/TernaryMoralLogic)  
7. Technical Architecture & Governance of TML Smart Contracts: A Deterministic Enforcement Layer for Ternary Moral Logic : r/solidity \- Reddit, accessed February 14, 2026, [https://www.reddit.com/r/solidity/comments/1qjil7f/technical\_architecture\_governance\_of\_tml\_smart/](https://www.reddit.com/r/solidity/comments/1qjil7f/technical_architecture_governance_of_tml_smart/)  
8. Ternary Moral Logic (TML) Quantitative Governance Analysis | by ..., accessed February 14, 2026, [https://medium.com/@leogouk/ternary-moral-logic-tml-quantitative-governance-analysis-d874812eb158](https://medium.com/@leogouk/ternary-moral-logic-tml-quantitative-governance-analysis-d874812eb158)  
9. TML Smart Contracts: Automating Ethics and Accountability on the Blockchain \- SSRN, accessed February 14, 2026, [https://papers.ssrn.com/sol3/Delivery.cfm/5990974.pdf?abstractid=5990974\&mirid=1](https://papers.ssrn.com/sol3/Delivery.cfm/5990974.pdf?abstractid=5990974&mirid=1)  
10. The Oracle of the Sacred Zero. Pause when truth is uncertain ..., accessed February 14, 2026, [https://medium.com/@leogouk/the-oracle-of-the-sacred-zero-083b014a03d7](https://medium.com/@leogouk/the-oracle-of-the-sacred-zero-083b014a03d7)  
11. Constitutional Logic in the Ethereum Virtual Machine: A Technical Implementation Report on Ternary Moral Logic : r/solidity \- Reddit, accessed February 14, 2026, [https://www.reddit.com/r/solidity/comments/1qm4hku/constitutional\_logic\_in\_the\_ethereum\_virtual/](https://www.reddit.com/r/solidity/comments/1qm4hku/constitutional_logic_in_the_ethereum_virtual/)  
12. Adversarial Audit & IP Fortress for Ternary Moral Logic (TML) | by Lev Goukassian \- Medium, accessed February 14, 2026, [https://medium.com/@leogouk/adversarial-audit-ip-fortress-for-ternary-moral-logic-tml-b4dac4139f2e](https://medium.com/@leogouk/adversarial-audit-ip-fortress-for-ternary-moral-logic-tml-b4dac4139f2e)  
13. Six People, One Binder, and No Way Back. | by Lev Goukassian \- Medium, accessed February 14, 2026, [https://medium.com/@leogouk/six-people-one-binder-and-no-way-back-f812fabd00f1](https://medium.com/@leogouk/six-people-one-binder-and-no-way-back-f812fabd00f1)  
14. My Algorithmic Will: Creating AI Ethics That No One Can Own | by Lev Goukassian \- Medium, accessed February 14, 2026, [https://medium.com/@leogouk/my-algorithmic-will-creating-ai-ethics-that-no-one-can-own-25e905d56a4a](https://medium.com/@leogouk/my-algorithmic-will-creating-ai-ethics-that-no-one-can-own-25e905d56a4a)  
15. blockchain-foundations.pdf, accessed February 14, 2026, [https://www.marabu.dev/blockchain-foundations.pdf](https://www.marabu.dev/blockchain-foundations.pdf)  
16. Technical Architecture & Governance of TML Smart Contracts \- SSRN, accessed February 14, 2026, [https://papers.ssrn.com/sol3/Delivery.cfm/5985954.pdf?abstractid=5985954\&mirid=1](https://papers.ssrn.com/sol3/Delivery.cfm/5985954.pdf?abstractid=5985954&mirid=1)  
17. TernaryMoralLogic/docs/Public\_Blockchain\_FAQ.md at main \- GitHub, accessed February 14, 2026, [https://github.com/FractonicMind/TernaryMoralLogic/blob/main/docs/Public\_Blockchain\_FAQ.md](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/docs/Public_Blockchain_FAQ.md)  
18. Auditable AI by Design: How TML Turns Governance into Operational Fact \- Medium, accessed February 14, 2026, [https://medium.com/@leogouk/auditable-ai-by-design-how-tml-turns-governance-into-operational-fact-37fd73e7b77e](https://medium.com/@leogouk/auditable-ai-by-design-how-tml-turns-governance-into-operational-fact-37fd73e7b77e)  
19. VESPo: Verified Evaluation of Secret Polynomials (with application to dynamic proofs of retrievability) \- Privacy Enhancing Technologies Symposium, accessed February 14, 2026, [https://petsymposium.org/popets/2023/popets-2023-0085.pdf](https://petsymposium.org/popets/2023/popets-2023-0085.pdf)
