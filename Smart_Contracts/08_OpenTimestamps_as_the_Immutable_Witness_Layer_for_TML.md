# **OpenTimestamps (OTS) as the Immutable Witness Layer for Ternary Moral Logic (TML)**

## **1\. What OpenTimestamps Is — and Is Not**

### **1.1 The Definition of a Hash Anchoring Protocol**

OpenTimestamps (OTS) represents a fundamental shift in the architecture of digital provenance, moving away from institutional attestation toward cryptographic proof. To understand its role within the Ternary Moral Logic (TML) ecosystem, one must first rigorously define the protocol by what it is, and perhaps more importantly, by what it is not. OTS is a hash anchoring protocol, designed to generate independent, verifiable proofs of existence for arbitrary data sets without reliance on a centralized issuer. Unlike complex state machines or smart contract platforms that seek to automate logic, OTS performs a singular, atomic function: it binds a specific cryptographic digest (hash) to a specific point in thermodynamic time.1

It is imperative to clarify that OpenTimestamps is not a blockchain. It possesses no native ledger, no consensus algorithm of its own, no validators, and no native currency or token. It acts as a parasitic—or more accurately, symbiotic—protocol that leverages the existing security budget of the Bitcoin network. It does not seek to create a new definition of truth but rather to anchor data to the most secure "clock" humanity has yet devised: the Bitcoin block header chain. OTS is a proof-of-existence mechanism, distinct from settlement systems. Settlement systems are concerned with the transfer of value and the reconciliation of balances; OTS is concerned solely with the temporal ordering of events.3

In the context of TML, this distinction is architectural, not merely semantic. TML requires a "Witness Layer" that is incapable of moral judgment or executive interference. OTS fits this requirement because it decouples timestamping from execution. It testifies to *when* a decision was made, never to *why* it was made or *what* the decision contains. This neutrality is the feature, not a bug, ensuring that the evidence layer remains uncorrupted by the very logic it is meant to audit.

### **1.2 The Limits of the Protocol: What OTS Does Not Do**

To trust OTS as a witness, one must understand its limitations. A common error in system design is attributing agency to the timestamping layer. OpenTimestamps explicitly does *not* perform the following functions:

* **No Execution:** OTS cannot execute code. It provides no environment for Turing-complete scripts, no loops, and no conditional logic that could alter the state of the TML agent. It cannot enforce the "Sacred Zero" or prevent a "Proceed" action; it can only record that the action occurred. This prevents the "logic coupling" vulnerabilities seen in smart contract platforms where the evidence of a failure is often lost if the contract itself fails.4, 5  
* **No Governance:** There are no administrative keys, no voting mechanisms, and no decentralized autonomous organizations (DAOs) governing the validity of a timestamp. A timestamp is mathematically valid if the Merkle path connects to a Bitcoin block header; no committee can vote to invalidate a mathematical fact. This absence of governance protects TML from "political" interference or retroactive censorship.5  
* **No Identity Verification:** OTS proves the existence of data, not the identity of the author. While a TML log may contain a digital signature identifying the AI agent (e.g., an RSA or ECDSA signature), OTS validates only the existence of that signature at time $T$. It does not validate the public key infrastructure (PKI) behind the signature. This separation ensures that OTS remains a pure timestamping utility, unburdened by the complexities and liabilities of identity management.6  
* **No Moral Reasoning:** The protocol is agnostic to the semantic content of the hashed data. It will timestamp a declaration of war with the same indifference as a recipe for tea. For TML, this means the witness is unbiased. It does not filter logs based on "appropriateness," ensuring that evidence of errors or unethical behavior is preserved just as robustly as evidence of compliance.

### **1.3 Decoupling Timestamping from Financial Transactions**

A critical architectural decision in OTS is the decoupling of the timestamping operation from financial transfers. In early blockchain experiments (e.g., "Satoshi Dice" style transactions or OP\_RETURN bloating), timestamping was often achieved by sending small amounts of Bitcoin to specific addresses. This method is economically inefficient and pollutes the host blockchain's Unspent Transaction Output (UTXO) set.7

OTS utilizes Merkle Aggregation to separate the user's intent (timestamping) from the network's cost (transaction fees). By aggregating millions of hashes into a single root, OTS allows the financial cost of the Bitcoin transaction to be amortized across all users, driving the marginal cost of a proof effectively to zero. This decoupling is essential for TML, which may generate thousands of "Moral Trace Logs" per hour. If every log required a distinct on-chain transaction, the cost would be prohibitive. OTS allows for forensic-grade logging at a scale impossible with direct on-chain writes.6

### **1.4 The Logic Being Witnessed: From Binary Certainty to Triadic Accountability**

*(Note: This section is integrated from the TML-GF document context.)*

The philosophical and technical foundation of modern AI is built upon the binary axiom, a framework where every input must ultimately be reduced to a one or a zero.13 While efficient for data processing, this logic is epistemologically violent when applied to human rights and moral agency. A binary system cannot hesitate; it can only execute or refuse. Ternary Moral Logic (TML) represents a fundamental correction to this paradigm by embedding a third, constitutional state directly into the execution path of the AI system.34

The triadic model of TML operates on the principle that if a system cannot prove its moral reasoning, it should not be permitted to act. This transition from "Code is Law" to "Logic is Constitution" requires a granular understanding of the three states that define TML-compliant cognition, which OTS is responsible for anchoring:

| Logical State | Symbolic Designation | Operational Trigger | Systemic Consequence |
| :---- | :---- | :---- | :---- |
| $+1$ | Proceed / Permit | Clear ethical alignment; rule-satisfaction and principle-adherence metrics are met. | The programmed action is executed immediately. |
| $-1$ | Refuse / Prohibit | Clear harm detection; violation of human rights or predefined ethical prohibitions. | Action is blocked; a refusal log is generated for auditing. |
| $0$ | **Sacred Zero / Pause** | Genuine moral ambiguity; conflicting rules, data deficiency, or high-stakes uncertainty. | Mandatory pause; the **Always Memory** component is triggered to document the impasse. |

The "Sacred Zero" is not merely a technical error state or a "null" value. It is a mandated moment of reflection where the AI recognizes the limits of its training data.22 This is the specific operational moment that OTS must capture to ensure accountability.

---

## **2\. The .ots Artifact — Self-Sovereign Evidence**

### **2.1 The Portable, Bearer-Based Cryptographic Receipt**

The output of the OpenTimestamps process is the .ots file—a binary artifact that serves as a self-contained cryptographic receipt. This file is not a pointer to a database entry or a URL to a cloud server; it *is* the proof. It contains the complete series of operations (hashing, appending, prepending) required to traverse from the document's hash to the Merkle Root anchored in the Bitcoin blockchain.2

For TML, this artifact represents "Self-Sovereign Evidence." The AI agent "owns" the proof of its own behavior. The evidence is not "on the blockchain"; the blockchain only contains the root hash (the anchor). The detailed evidence (the Merkle path) is held by the subject itself. This inversion of the data model enhances privacy—since the logs are not public—while maximizing accountability, since the logs cannot be forged.10

### **2.2 Freedom from Institutional Permission**

The .ots file requires no live servers for verification. Once the timestamp has been "upgraded" (i.e., the path to the Bitcoin header is complete), the calendar server that facilitated the aggregation can cease to exist. The verification logic is entirely self-contained within the .ots file and the public Bitcoin blockchain.2

This property is vital for the long-term archival of TML decisions. An AI agent deployed today may operate for twenty years. The startup that built the agent, or the OTS calendar server it used, may go bankrupt. However, as long as the Bitcoin blockchain (or even a saved copy of its headers) exists, the .ots files generated today will remain verifiable decades from now. This "institutional survivability" ensures that TML's moral history is not contingent on the lifespan of corporate entities.11, 14

### **2.3 Technical Structure of the Artifact**

The .ots file is a binary sequence of opcodes and data. It is designed to be compact, typically ranging from a few hundred bytes to a few kilobytes, regardless of the size of the original file. This compactness is critical for TML agents, which may act on embedded systems with limited storage.

The file structure typically follows this sequence:

1. **Header/Magic Bytes:** Identifying the file type.  
2. **Operations:** A sequence of hashing (SHA256) and concatenation (APPEND, PREPEND) instructions that reconstruct the local branch of the Merkle tree.  
3. **Attestation:** A specialized opcode (0x00) that links the final hash of the local branch to a known public anchor, such as a Bitcoin block header.6

This structure is extensible. While currently focused on Bitcoin, the .ots format supports multiple attestations. A single file can contain proofs from Bitcoin, Litecoin, and even centralized notaries, providing redundancy. This redundancy is a core component of the "Hybrid Shield" defense strategy in TML.13

---

## **3\. Cryptographic Mechanics — The Aggregation Tree**

### **3.1 Step-by-Step Technical Walkthrough**

The efficacy of OTS lies in its use of Merkle Trees to bridge the gap between individual user data and the global blockchain. The process transforms a local intent into a global fact through four distinct stages:

Phase 1: Client-Side Hashing

The process begins entirely locally within the TML agent. The agent takes the "Lantern Signal" (the JSON object representing the Sacred Zero state) and applies a SHA-256 hash function.

$$H\_{local} \= \\text{SHA256}(\\text{Lantern\\\_JSON})$$  
Crucially, the raw data never leaves the agent. Only this 32-byte digest ($H\_{local}$) is transmitted. This preserves the privacy of the AI's internal reasoning while committing to its content.2, 9

Phase 2: Aggregation (The Calendar Server)

The agent transmits $H\_{local}$ to an OTS Calendar Server (e.g., alice.btc.calendar.opentimestamps.org). The server acts as a high-throughput funnel. It accepts hashes from thousands of users and organizes them into a binary tree structure.

The server pairs the hashes ($H\_A, H\_B$) and concatenates them to form a parent node:

$$H\_{parent} \= \\text{SHA256}(H\_A || H\_B)$$  
This process is repeated recursively. A tree with a height of 20 can aggregate over a million ($2^{20}$) unique timestamps into a single root hash.6, 10

Phase 3: Anchoring (The Bitcoin Transaction)

Once the aggregation window closes (typically once per second or minute), the server takes the final Merkle Root and embeds it into a Bitcoin transaction.

The standard method uses the OP\_RETURN script opcode. This opcode allows the transaction to carry up to 80 bytes of arbitrary data. The server creates a transaction that spends a small amount of dust (to pay the miner fee) and includes the Merkle Root in the OP\_RETURN output.

$$\\text{Tx}\_{anchor} \\rightarrow \\text{OP\\\_RETURN} \\langle \\text{Merkle Root} \\rangle$$  
Once this transaction is mined into a block, the Merkle Root is immutable.8, 15

Phase 4: Proof Generation and Upgrading

Initially, the server provides the client with a "pending" .ots file. This file contains the path from $H\_{local}$ to the Merkle Root. The client must verify that this root is indeed the one the server plans to anchor.

Once the Bitcoin transaction is confirmed (mined), the client "upgrades" the .ots file. The server provides the final link: the path from the Merkle Root to the Bitcoin Block Header. The .ots file now forms a complete chain from the Lantern Signal to the thermodynamic energy of the Bitcoin network.10

### **3.2 The Economics of Forensic-Grade Logging**

The "Aggregation Tree" architecture is what makes OTS economically feasible for TML. Bitcoin transactions are scarce and expensive. If a TML agent required a separate transaction for every decision, the cost would be unsustainable. By aggregating millions of hashes into a single transaction, the cost per proof becomes:

$$\\text{Cost}\_{proof} \= \\frac{\\text{Bitcoin Tx Fee}}{\\text{Number of Aggregated Hashes}}$$  
As the number of hashes approaches infinity, the marginal cost approaches zero. This economic reality allows TML agents to log every micro-decision, every hesitation, and every sensor reading without concern for budget constraints.7

---

## **4\. Relationship to Bitcoin — The Global Clock**

### **4.1 Bitcoin as a Thermodynamic Clock**

To understand why TML relies on Bitcoin, one must discard the notion of Bitcoin as a currency and view it as a clock. Conventional clocks (NTP servers, atomic clocks) measure time based on oscillation. They are precise but mutable; a system administrator can change the time on a server, effectively rewriting history for that system.18

Bitcoin measures time based on energy (work). The "tick" of the Bitcoin clock is the finding of a block. This event is probabilistic but thermodynamically constrained. The difficulty adjustment algorithm ensures that the network produces a block roughly every 10 minutes, requiring a massive expenditure of electricity (hashing power). This creates a property known as Thermodynamic Finality. To rewrite the timestamp of a block $N$, an attacker cannot simply edit a database field. They must re-expend the energy required to mine block $N$, plus the energy for every block mined since ($N+1, N+2,...$). This creates a "wall of energy" protecting the past.16, 17

### **4.2 Verification Model: Trustless Validation**

Validating an OTS proof is a deterministic process that requires no trust in the original timestamping server. The verification model involves three inputs:

1. **The Evidence:** The TML log file (Lantern Signal).  
2. **The Map:** The .ots receipt file.  
3. **The Anchor:** The Bitcoin blockchain (specifically, the header chain).

The verifier calculates the hash of the evidence, applies the operations listed in the map, and checks if the result matches the Merkle Root stored in the anchor.

$$\\text{Result} \= \\text{ApplyOps}(\\text{Evidence}, \\text{.ots})$$  
$$\\text{Assert}(\\text{Result} \== \\text{BitcoinHeader}\[N\].\\text{MerkleRoot})$$  
Because Bitcoin block headers are widely replicated (stored by thousands of nodes globally), the anchor is universally accessible. The verifier does not need to ask the OTS server "Is this valid?" They simply check the math against the public ledger.10

---

## **5\. OTS vs Smart Contracts — Separation of Concerns**

### **5.1 The Smart Contract Fallacy**

A common question in blockchain architecture is: "Why use OpenTimestamps on Bitcoin when we could use a Smart Contract on Ethereum or Polygon?" Smart contracts allow for logic and state to be stored together, which seems intuitive for TML. However, this coupling introduces severe risks and inefficiencies.

| Feature | OpenTimestamps (OTS) | Smart Contracts (EVM) |
| :---- | :---- | :---- |
| **Primary Function** | Witness (Timestamping) | Execution (Logic \+ State) |
| **Cost Model** | Aggregated (Near Zero) | Per-Operation (Gas Fees) |
| **Trust Boundary** | Physics (PoW) | Validator Consensus (PoS) |
| **Attack Surface** | Minimal (Hashing only) | High (Reentrancy, Logic Bugs) |
| **Data Privacy** | Absolute (Off-chain data) | Variable (Often on-chain) |
| **Scalability** | $O(log N)$ Merkle Path | Linear State Growth |

Why Logic Weakens Timestamping:

In a smart contract, the timestamping logic is often intertwined with the business logic. If the contract has a bug (e.g., a reentrancy vulnerability), the integrity of the logs stored within it can be compromised. This is known as "Timestamp Dependence," where miners can manipulate block times.19 OTS separates the two. The evidence is not stored in a contract; it is anchored to a block. Even if the TML agent's internal code is completely compromised, the attacker cannot alter the cryptographic relationship between the past .ots files and the Bitcoin blockchain.3

### **5.2 Exclusive Use Cases for OTS in TML**

TML utilizes OTS exclusively for "Constitution and Memory," while relegating execution to other layers (if used at all).

* **Constitutions:** The foundational ethical axioms of the AI (the "Goukassian Promise") are timestamped via OTS. This proves that the AI was initialized with a specific moral code at birth.  
* **Licenses:** The usage rights and constraints are timestamped.  
* **Critical Immutable Logs:** The "Sacred Zero" events (Lantern Signals) are timestamped via OTS.

Smart contracts may be used for *payment* or *access tokens*, but the *evidence of moral intent* must reside in the neutral, static, and immutable layer of OTS. Smart contracts are "Law"; OTS is "History." TML recognizes that Law can change, but History cannot.13

---

## **6\. OTS in TML Architecture — Anchoring Intent**

### **6.1 The Role of Anchoring**

In TML, the "intent" of an AI agent is formalized through the transition between states (Proceed \+1, Pause 0, Refuse \-1). OTS anchors these intent states to the physical world.

* **Proving Authorship and Prior Art:** OTS allows the creator of a TML model to prove that a specific neural network architecture or set of weights existed at time $T$.20  
* **Preventing Retroactive Reinterpretation:** In the event of an AI accident, there is a temptation to reinterpret the logs. OTS locks the "Lantern Signal"—which contains the specific "Epistemic Uncertainty" score—in time. This forces the post-mortem analysis to rely on the data as it existed *then*, not as it is interpreted *now*.21

### **6.2 The Goukassian Promise: Continuity Beyond Founders**

The "Goukassian Promise" is the ethical covenant binding the TML system. It consists of The Lantern (transparency), The Signature (provenance), and The License (terms). OTS provides the "Signature" layer.23 By timestamping the release of the TML kernel, the architect creates a genesis point. Any subsequent update to the kernel must also be timestamped.

This creates a Chain of Continuity. If a corporation acquires the rights to the TML agent and silently removes the "Sacred Zero" safeguard to increase efficiency, the chain is broken. Auditors can detect this "Ghost Update" by verifying the OTS proofs of the running software against the genesis chain.22, 24

### **6.3 The Lantern Signal Integration**

The integration of OTS with the TML "Lantern Signal" is the operational core of the system.

The Lantern Signal is defined as a JSON object:

JSON  
{  
  "system\_status": "PULSING",  
  "epistemic\_uncertainty": 0.85,  
  "state\_id": 0,  
  "trace\_id": "uuid-v4-...",  
  "compliance\_hash": "blake3:f47ac10b..."  
}

When the AI enters State 0, it serializes this object, hashes it, and immediately submits the hash to the OTS layer. The resulting .ots file is the "receipt of hesitation." This mechanism transforms the subjective experience of the AI (uncertainty) into an objective historical artifact.13

---

## **7\. Legal and Evidentiary Standing**

### **7.1 OTS Proofs as Self-Authenticating Evidence**

The ultimate utility of TML's witness layer is its admissibility in legal proceedings. In the United States, the Federal Rules of Evidence (FRE) govern the admissibility of digital records.

FRE 902(13) and 902(14):

These rules allow for "Certified Records Generated by an Electronic Process or System" to be self-authenticating, meaning they do not require a live witness to lay a foundation for their authenticity in court, provided they are accompanied by a certification.25, 26

* **The Certification:** An OTS proof acts as this certification. It mathematically demonstrates that the file has not been altered since the timestamp (Integrity) and that it existed at that time (Authenticity).28  
* **The Process:** A qualified expert (or even a scripted verification tool) can generate an affidavit stating that the SHA256 hash of the evidence matches the value anchored in Bitcoin Block \#X.27

### **7.2 Comparison to Traditional Attestation**

| Method | Trust Source | Vulnerability | Cost |
| :---- | :---- | :---- | :---- |
| **Notary Public** | Human Officer | Bribery, Error, Backdating | High (per doc) |
| **RFC 3161 TSA** | Centralized Server (PKI) | Key Compromise, Insider Threat | Medium |
| **OpenTimestamps** | Thermodynamic Physics | 51% Attack (Global) | Negligible |

OTS minimizes trust while maximizing verifiability. A traditional notary can be coerced into signing a document today and dating it "last week." OTS cannot be coerced because the "notary" is the aggregate work of the entire Bitcoin mining network.6, 29

### **7.3 Cryptographic Chain of Custody**

Legal cases often turn on the "Chain of Custody." OTS creates a Cryptographic Chain of Custody. The .ots file proves that the content of the log has not changed. The physical storage of the drive becomes less critical because any alteration to the data would invalidate the Merkle proof. This relieves the TML operator of the burden of proving "secure storage" in the traditional sense; they only need to prove "mathematical integrity."30, 31

### **7.4 Compliance with the EU AI Act**

(Note: Integrated from the TML-GF document context.)

The emerging EU AI Act mandates high levels of transparency, traceability, and human oversight for "high-risk" AI systems.34 TML provides the technical substrate to meet these requirements through:

* **System-Enforced Traceability:** Every morally consequential action is logged and signed by default.22  
* **Human-in-the-Loop Verification:** The Sacred Pause records exactly which human reviewed an escalation, what they decided, and why, providing a clear chain of custody for accountability.22  
* **Immutable Record-Keeping:** The use of OTS ensures that these logs meet the "qualified timestamp" provisions of the eIDAS regulation, establishing a "sure date" for digital documents that is legally recognized across the EU.24

---

## **8\. Adversarial Analysis**

### **8.1 The Fake Calendar Attack**

Scenario: An adversary sets up a malicious OTS calendar server. The TML agent submits a hash, and the server returns a "pending" .ots file but never actually anchors it to Bitcoin.

Mitigation:

* **Redundancy:** TML agents must be configured to use multiple, independent calendar servers (e.g., alice, bob, finney) simultaneously. The OTS client handles this natively, creating a "commitment operation tree" that splits. If *any* one of the servers behaves honestly, the timestamp is valid.  
* **Verification Loops:** The agent must periodically check for the Bitcoin confirmation. If a server fails to anchor within a specific window (e.g., 24 hours), the agent flags a "Witness Availability Error".11

### **8.2 Backdating Impossibility**

Scenario: An AI causes an accident. The operator wants to retroactively insert a log entry showing the AI tried to stop (State \-1) but failed.

Analysis: To forge this log, the operator would need to generate an .ots file that links the new log's hash to an old Bitcoin block.

Constraint: The 0x00 Attestation opcode requires the Merkle path to resolve to the Merkle Root stored in that old block. Since cryptographic hash functions (SHA256) are pre-image resistant, the operator cannot find a new input that resolves to the already-fixed root. They would have to 51% attack Bitcoin to rewrite the block header itself.

Result: Backdating is thermodynamically impossible.5

### **8.3 OTS Server Disappearance**

Scenario: The calendar server that issued the timestamp goes offline permanently.

Resilience: Once the timestamp is upgraded (anchored), the server is irrelevant. The .ots file contains the full path. The verification depends only on the file and the Bitcoin blockchain.32

---

## **9\. Operational Case Studies: The Witness Layer in Practice**

*(Note: This section is integrated from the TML-GF document context.)*

The implementation of OTS as a witness layer is not a theoretical exercise; it is currently being deployed in some of the world's most demanding information environments.

### **9.1 The Internet Archive and "Carbon Dating" the Web**

The OpenTimestamps team, led by Peter Todd, has timestamped every item in the Internet Archive—approximately 750 million files—using a single Bitcoin transaction.35 This provides a permanent, cryptographically verifiable "Carbon Date" for the historical record of the internet. If a malicious sysadmin were to alter a snapshot of a political website, the OTS proof would immediately reveal that the modified file does not match the hash anchored to the blockchain in the past.35

### **9.2 El Salvador and Government Transparency**

The government of El Salvador has partnered with Simple Proof to timestamp official records from the Ministry of Foreign Affairs and the Ministry of Environment on the Bitcoin blockchain.36 Using the OTS protocol, the government can protect millions of documents without congesting the network or incurring massive fees. This project positions El Salvador as a global reference for using blockchain technology to eliminate the possibility of document tampering.36

For TML, this serves as a blueprint for "Planetary Protection." Every AI decision that affects the environment or national policy can be anchored to the blockchain, creating an immutable memory of the system's impact.

---

## **10\. Conclusion — The Witness Who Does Not Judge**

OpenTimestamps acts as the silent, immutable conscience of the Ternary Moral Logic framework. It is a witness that cannot be bribed, intimidated, or silenced. It operates outside the jurisdiction of human courts and corporate boards, adhering only to the laws of mathematics and thermodynamics.

By reducing the function of witnessing to a pure cryptographic operation—anchoring a hash to a block—OTS strips away the subjectivity that plagues human auditing. It provides TML with a "Truth-in-Time" layer that is as rigid as the logic it monitors.

In this architecture, the AI agent provides the intent (The Lantern), the TML kernel provides the reasoning (The Logic), and OpenTimestamps provides the proof (The History). Together, they form a governance structure where trust is not required because verification is absolute.

**Final Thesis:** *"Time, once proven, cannot be argued with."*

---

Appendix: Technical Opcodes

The following opcodes are central to the .ots binary format verification logic 12, 33:

| Opcode (Hex) | Mnemonic | Function | Description |
| :---- | :---- | :---- | :---- |
| 0x08 | SHA256 | Hash | Applies SHA-256 to the current stack item. |
| 0xF0 | APPEND | Concatenate | Appends raw bytes to the current stack item. |
| 0xF1 | PREPEND | Concatenate | Prepends raw bytes to the current stack item. |
| 0x00 | ATTEST | Attest | Asserts the current value matches a known external anchor (e.g., Bitcoin Block). |

---

# **Works Cited**

1. **Three properties of Distributed Ledger Technology systems applied in the nuclear sector adding value to safeguards** – ESARDA, accessed January 12, 2026\.  
2. **OpenTimestamps** – opentimestamps.org, accessed January 12, 2026\.  
3. **Ethereum and Opentimestamps · Issue \#47** – GitHub, accessed January 12, 2026\.  
4. **Stampery Blockchain Timestamping Architecture (BTA) \- Version 6** – arXiv, accessed January 12, 2026\.  
5. **Is there a digital time-stamping scheme that does not rely on a time-stamping authority?** – Stack Exchange, accessed January 12, 2026\.  
6. **OpenTimestamps Guide and Stamping Facility** – dgi.io, accessed January 12, 2026\.  
7. **The Tech to Timestamp Data in Bitcoin's Blockchain Has Evolved Far Past Single-File Uploads** – Bitcoin.com, accessed January 12, 2026\.  
8. **Demystifying and Adjusting the Promises of Blockchain-based Data Management** – Roman Matzutt, accessed January 12, 2026\.  
9. **operation to commit to secp256k1 points? · Issue \#12** – GitHub, accessed January 12, 2026\.  
10. **Blockchain Notarization: extensions to the OpenTimestamps protocol** – POLITesi, accessed January 12, 2026\.  
11. **OpenTimestamps: Scalable, Trust-Minimized, Distributed Timestamping with Bitcoin** – Peter Todd, accessed January 12, 2026\.  
12. **sign-to-contract: how to achieve trustless digital timestamping with zero marginal cost** – POLITesi, accessed January 12, 2026\.  
13. **LOGIC IS CONSTITUTION: WHY MACHINES NEED PERMISSION TO SAY "I DON'T KNOW"** – Lev Goukassian, Medium, accessed January 12, 2026\.  
14. **OpenTimestamps and Knots/OCEAN** – Peter Todd, accessed January 12, 2026\.  
15. **sign-to-contract: how to achieve trustless digital timestamping with zero marginal cost** – POLITesi (PDF), accessed January 12, 2026\.  
16. **Bitcoin as an Interplanetary Monetary Standard with Proof-of-Transit Timestamping** – arXiv, accessed January 12, 2026\.  
17. **Safe Low Bandwidth SPV: A Formal Treatment of Simplified Payment Verification Protocols** – arXiv, accessed January 12, 2026\.  
18. **Bitcoin Standard Time.. Bitcoin Clocks** – Medium, accessed January 12, 2026\.  
19. **Vulnerability: Timestamp Dependence** – OWASP, accessed January 12, 2026\.  
20. **Timestamping via Blockchain Recognized as Judicial Evidence** – Gilliéron Avocat, accessed January 12, 2026\.  
21. **The High-Risk Gambit. Why Corporations Can't Plagiarize…** – Lev Goukassian, Medium, accessed January 12, 2026\.  
22. **Auditable AI by Design: How TML Turns Governance into Operational Fact** – Lev Goukassian, Medium, accessed January 12, 2026\.  
23. **The Goukassian Promise. A self-enforcing covenant between…** – Lev Goukassian, Medium, accessed January 12, 2026\.  
24. **FractonicMind/TernaryMoralLogic: Implementing Ethical Responsibility in AI Systems** – GitHub, accessed January 12, 2026\.  
25. **How Two New Rules for Self Authentication Will Save You Time and Money** – Judicature, accessed January 12, 2026\.  
26. **Self-Authentication of Electronic Evidence: New Rules 902(13)-(14)** – US Courts, accessed January 12, 2026\.  
27. **New Rules for Self-Authenticating Electronic Evidence** – American Bar Association, accessed January 12, 2026\.  
28. **Blockchain Records Affidavit** – Notary Colorado Springs, accessed January 12, 2026\.  
29. **QR Date – signed timestamps inside for verifying dates** – Hacker News, accessed January 12, 2026\.  
30. **(PDF) Time-Stamping in Blockchain for Legal Evidence Submission** – ResearchGate, accessed January 12, 2026\.  
31. **ESTABLISHING A LEGALLY DEFENSIBLE BLOCKCHAIN CHAIN OF CUSTODY TECHNICAL FRAMEWORK** – Scholars' Bank, accessed January 12, 2026\.  
32. **OpenTimeStamps MCP Server** – LobeHub, accessed January 12, 2026\.  
33. **How does OpenTimestamps work technically?** – Bitcoin Stack Exchange, accessed January 12, 2026\.  
34. **Auditable AI: tracing the ethical history of a model** – ResearchGate, accessed January 12, 2026\.  
35. **How OpenTimestamps 'Carbon Dated' (almost) The Entire Internet With One Bitcoin Transaction** – Peter Todd, accessed January 12, 2026\.  
36. **El Salvador Partners With Simple Proof To Timestamp Government Documents On Bitcoin Blockchain** – Bitcoin Magazine, accessed January 12, 2026\.

