# **The Persistence of Authorship in Ethical Governance: A Legal-Technical Evaluation of the Goukassian Promise and Ternary Moral Logic**

## **Abstract**

The rapid proliferation of autonomous artificial intelligence (AI) systems has precipitated a crisis in legal attribution and governance. As algorithmic decision-making becomes increasingly opaque, traditional frameworks of liability—predicated on clear chains of human agency—falter against the "Black Box" of neural networks. This manuscript evaluates **Ternary Moral Logic (TML)**, a governance architecture proposed by Lev Goukassian, which introduces a "Sacred Zero" state to enforce hesitation in the face of ethical ambiguity. Specifically, this research interrogates the legal and technical validity of the **"Goukassian Promise"**—a mandatory cryptographic binding of the author’s identity (via ORCID) and ethical mandates to the system’s runtime kernel. By synthesizing principles from Continental *droit moral* (moral rights), United States product liability jurisprudence, and cryptographic provenance standards (Merkle trees, Ephemeral Key Rotation), this report argues that the embedding of persistent authorship is not merely an act of ego, but a necessary "Root of Trust" for critical infrastructure. The analysis concludes that the hardcoded attribution serves as a liability anchor, transforming ethical guidelines from voluntary principles into auditable, immutable operational facts.

## ---

**1\. Introduction**

### **1.1 The Crisis of Anonymity in Algorithmic Governance**

The governance of artificial intelligence (AI) has historically been approached through the lens of post-hoc compliance: regulators analyze harm after it occurs, and developers patch vulnerabilities in response to litigation. This reactive cycle is increasingly untenable as AI systems migrate from recommendation engines to critical infrastructure controls—energy grids, medical triage, and financial settlement layers. The central failure of current governance models is the **severance of provenance**: once an AI model is deployed, the link between its outputs and its creators’ original intent is dissolved by the stochastic nature of machine learning and the legal shielding of corporate "terms of service".1  
Into this vacuum enters **Ternary Moral Logic (TML)**, a framework that proposes a fundamental restructuring of machine cognition from binary (0/1) to ternary (+1/0/-1) logic, explicitly encoding a state of "ethical suspension" or "hesitation".2 Unlike conventional AI guardrails, which function as external filters, TML integrates ethical constraints directly into the decision-making logic of the system. Central to this architecture is a controversial mechanism known as the **Goukassian Promise**, which mandates the permanent embedding of the creator’s identity—specifically the Open Researcher and Contributor ID (ORCID) of Lev Goukassian—alongside a binding ethical vow within the system’s immutable audit logs.3

### **1.2 The "Author Function" in Code**

Michel Foucault, in his seminal work *What Is an Author?*, argued that the "author function" is not merely a creative designation but a legal and punitive one—a way to assign responsibility to discourse.4 The author provides a locus of coherence and accountability. In the realm of software, however, this function has been systematically dismantled. Modern software development, characterized by massive open-source dependencies (CI/CD pipelines) and corporate ownership, often obscures individual contribution behind generic "contributor" labels or corporate brands.5  
When an algorithm causes harm, the "author" is rarely a person; it is a corporation, shielded by limited liability, or a diffuse community of contributors, shielded by the lack of direct causation. This "anonymity of the stack" creates a **Moral Hazard**: if no specific individual is tethered to the machine's ethical performance, there is no existential incentive to prevent catastrophic edge cases. The "Ghost in the Machine" becomes a liability shield.

### **1.3 Scope of Inquiry**

This manuscript evaluates the appropriateness of persistent attribution within the TML framework. Critics might dismiss the permanent embedding of an author's name as "technological narcissism" or a violation of open-source neutrality.6 However, proponents argue it represents a "Digital Watermark of Liability"—a mechanism to ensure that the "conscience" of the system cannot be stripped away by downstream commercial interests.7  
We analyze this through three lenses:

1. **Technical Viability:** Does TML’s architecture (Sacred Zero, Dual-Lane Latency, EKR) actually enable the enforcement of these ethical mandates without crippling performance?  
2. **Legal Jurisprudence:** Does the concept of "inalienable authorship" in code align with *droit moral* and emerging strict liability standards for software developers?  
3. **Ethical Governance:** Does the "Goukassian Promise" serve the public interest by preventing the "dilution of responsibility" common in decentralized systems?

The report posits that in an era of "Hallucinating AI," the only path to trust is **Auditable AI**. By forcing systems to "Pause when truth is uncertain" and creating an unbreakable chain of custody back to a human author, TML offers a prototype for the future of regulatory compliance.

## ---

**2\. Background: The Jurisprudence of Attribution and Liability**

To understand the necessity of the Goukassian Promise, one must first confront the legal and sociological frameworks that govern authorship, liability, and the naming of discoveries.

### **2.1 *Droit Moral* vs. Economic Copyright**

The legal justification for persistent attribution finds its roots in the Continental European concept of *droit moral* (moral rights). Unlike United States copyright law, which treats intellectual property primarily as an economic asset that can be sold, transferred, and severed from the creator, French law recognizes the **Right of Paternity** (*droit a la paternité*)—the inalienable right of the author to claim authorship and prevent the distortion of their work.8  
Under the French Intellectual Property Code (Code de la propriété intellectuelle), the author enjoys an "exclusive intangible property right" that is "perpetual, inalienable and imprescriptible".11 This means that even if an author sells the economic rights to a software platform, they retain the right to have their name associated with it and to object to any "derogatory action" that would prejudice their honor or reputation.12  
In the context of TML, Lev Goukassian’s insistence on embedding his ORCID is an attempt to translate this legal concept into **cryptographic reality**. In the US, moral rights for software are weak or non-existent, often waived by contract.9 By embedding the ORCID and the Vow into the Merkle roots of the system 3, TML effectively creates a *smart contract of paternity* that resists the "alienability" (sale/removal) typical of US software licensing. It functions as a digital assertion of *droit moral* that transcends jurisdictional boundaries.

### **2.2 The "Matthew Effect" and Stigler's Law**

The sociology of science provides a compelling argument for rigorous attribution. Robert K. Merton’s "Matthew Effect" describes the phenomenon where credit for scientific work is disproportionately bestowed upon already famous researchers, while lesser-known contributors are ignored.14 This creates a self-reinforcing cycle where the "rich get richer" in terms of reputation.  
Complementing this is **Stigler’s Law of Eponymy**, which states that "no scientific discovery is named after its original discoverer".17 History is replete with examples: the Pythagorean theorem (known to Babylonians), Hubble’s Law (discovered by Lemaître), and Halley’s Comet (recorded by Chinese astronomers).19  
In the context of AI safety, this erasure of origin is dangerous. If a specific safety framework (like TML) is absorbed into a massive corporate AI product (e.g., "Google Safety Layer"), the specific ethical mandates—such as "No Spy" or "No Weapon"—are often stripped out or diluted during the rebranding process.7 The "Goukassian Promise" anticipates Stigler’s Law. By hardcoding the attribution, Goukassian ensures that the framework *cannot* be used without acknowledging its source and, by extension, its mandates. It is a defensive measure against the corporate dilution of ethical constraints.

### **2.3 The Failure of "Ethical Source" Licensing**

The open-source software (OSS) movement has traditionally been defined by "freedom zero"—the freedom to run the program for any purpose.20 However, the rise of AI has led to the "Ethical Source" movement, which seeks to restrict software usage based on moral criteria (e.g., the **Hippocratic License**, which prohibits human rights violations).6  
Critics argue that these licenses are legally unenforceable and technically ineffective. A text file saying "Do No Harm" does not prevent a drone from firing a missile. Furthermore, defining "harm" in a license leads to ambiguity and fragmentation.22 The "Goukassian Promise" represents a departure from this "legal-text" approach. It does not rely on a lawyer to enforce the license; it relies on the **runtime architecture** to enforce the pause. If the cryptographic signature (the "Lantern") is removed or invalidated, the system’s logic gates fail to close, and the AI enters a permanent "Sacred Zero" (pause) state.3 This represents a shift from "Code is Law" to **"Law is Code"**—making the ethical mandate an operational dependency rather than a legal request.

### **2.4 Strict Liability and the "Tornado Cash" Precedent**

The legal landscape for software developers is shifting rapidly toward strict liability. The case of **Tornado Cash**, where a developer was arrested for writing code that facilitated money laundering, demonstrates that "neutral code" is no longer a valid defense.23 Regulators are increasingly viewing developers of decentralized protocols as liable for the actions of their software.  
In this climate, anonymity is a liability. If a developer cannot be identified, the *entire network* may be sanctioned. Conversely, if a developer explicitly embeds their identity and safety protocols (like TML’s "Sacred Zero"), they establish a defense of "Due Care." By creating an immutable log of their ethical intent and the system’s adherence to it, they provide forensic evidence that any harm was a result of *misuse* or *modification*, not design defect.25 The persistent ORCID thus serves as a shield for the conscientious developer, proving they did not abandon the code to the winds of chance.

## ---

**3\. Overview of Ternary Moral Logic (TML)**

Ternary Moral Logic is not merely a philosophical construct; it is a rigorous technical specification designed to transform abstract ethical mandates into engineering constraints. It replaces the binary decision matrix of traditional computing (0/1) with a triadic structure (+1/0/-1), creating a formalized space for uncertainty and ethical reflection.

### **3.1 The Eight Pillars of TML**

The TML framework rests on eight foundational pillars, each addressing a specific vector of AI risk. The following table details their definitions, technical functions, and governance outcomes.2

| Pillar | Definition | Technical Function | Governance Outcome |
| :---- | :---- | :---- | :---- |
| **Sacred Zero** | The ethical trigger point for uncertainty. | Introduces a third logic state (0) alongside Permit (+1) and Prohibit (-1). | Forces "System-Level Hesitation" rather than probabilistic guessing. |
| **Always Memory** | Permanent record of ethical history. | Immutable logging of all decision pathways using Merkle chains. | "No Log \= No Action" enforcement; prevents "fleeting" errors. |
| **Goukassian Promise** | Truthfulness, restraint, and verifiable accountability. | Cryptographic binding of Author ORCID \+ Vow to runtime. | Prevents "conscience stripping" by downstream operators. |
| **Moral Trace Logs** | Structured evidence logs. | JSON/XML schemas recording *why* a decision was made. | Creates forensic evidence admissible under Federal Rule of Evidence 901\.25 |
| **Human Rights Mandate** | Alignment with rights frameworks. | Hardcoded constraints against specific harms (e.g., discrimination). | Automated compliance with UN/EU fundamental rights. |
| **Earth Protection Mandate** | Ecological responsibility. | Energy/resource usage logging and caps. | Accountability for the carbon cost of inference. |
| **Hybrid Shield** | Dual protection layer. | Combined institutional policy \+ cryptographic locks. | Protects against both external hacks and internal policy override. |
| **Public Blockchains** | Immutable anchoring. | Merkle roots anchored to public ledgers (e.g., Ethereum/Hyperledger). | Ensures logs cannot be altered retroactively by the host organization. |

### **3.2 The Sacred Zero: Operationalizing "Hesitation"**

The core innovation of TML is the **Sacred Zero** (or "Sacred Pause").2 In conventional binary systems, a probability score of 51% often triggers a "True" action, leading to "hallucinations" where the AI confidently asserts falsehoods. In TML, any probability falling below a defined "Certainty Threshold" or triggering a "Moral Conflict" flag forces the system into the 0 state.  
This 0 state is not an error; it is a **blocking operation** in the logic flow.

* **Binary Logic:** Input \-\> Model \-\> Output (Action)  
* **Ternary Logic:** Input \-\> Model \-\> (Check Confidence/Harm) \-\> \-\> Log \-\> Human Review \-\> Action

This mechanism directly addresses the "Hallucination" problem. By mandating a pause when truth is uncertain, the system adheres to the first clause of the Goukassian Vow: *"Pause when truth is uncertain"*.7 This state functions similarly to **Optimistic Concurrency Control** in database theory, where transactions are checked for conflicts before commitment, but with an added ethical dimension.30

### **3.3 The Goukassian Promise: A Constitutional Layer**

The **Goukassian Promise** constitutes the "Constitutional Layer" of TML. It consists of three artifacts: **The Lantern** (proof of hesitation), **The Signature** (Lev Goukassian’s ORCID), and **The License** (No Weapon / No Spy).3  
The Vow—*"Pause when truth is uncertain. Refuse when harm is clear. Proceed where truth is."*—is operationalized into executable code:

1. **Pause when truth is uncertain:** $\\rightarrow$ State 0 (Triggered by low confidence interval).  
2. **Refuse when harm is clear:** $\\rightarrow$ State \-1 (Triggered by violation of Human Rights Mandate).  
3. **Proceed where truth is:** $\\rightarrow$ State \+1 (Triggered by high confidence \+ mandate compliance).

The embedding of the ORCID (0009-0006-5966-1243) serves as the "Root of Trust." It is the anchor point for the entire cryptographic chain. If this anchor is removed, the Merkle proofs fail validation, and the system is flagged as "corrupted" or "unverified".3

## ---

**4\. Technical Operationalization: From Ethics to Architecture**

The validity of the Goukassian Promise rests on the efficacy of the TML architecture. If the system cannot technically enforce the pause or the logging without destroying performance, the attribution is meaningless. TML employs advanced cryptographic and architectural patterns to ensure "Auditable AI" is also "Performant AI."

### **4.1 Dual-Lane Latency Architecture**

A common critique of "Human-in-the-loop" systems is latency. Real-time systems (e.g., autonomous driving, high-frequency trading) cannot wait for human review. TML addresses this via **Dual-Lane Latency**.27

#### **4.1.1 The Fast Lane (Synchronous / Non-Blocking)**

The "Fast Lane" handles clear-cut \+1 (Permit) or \-1 (Refuse) decisions. These are executed instantly (≤ 2 ms).

* **Mechanism:** This utilizes **non-blocking I/O** (as seen in high-performance proxies like Envoy or NGINX).33 The system checks the "Triadic Logic Rulesets" (pre-computed ethical heuristics). If the input clearly falls within safe parameters, it is processed immediately.  
* **Sidecar Pattern:** TML is often deployed using a **Sidecar Pattern** (e.g., in Kubernetes), where the TML logic runs in a separate container alongside the main application.35 This sidecar intercepts traffic, applies the logic, and forwards the request, adding minimal overhead (single-digit milliseconds).

#### **4.1.2 The Slow Lane (Asynchronous / Blocking)**

The "Slow Lane" is activated *only* during the Sacred Zero (0).

* **Mechanism:** When the "Sacred Pause" is triggered, the system enters a **blocking state** for that specific transaction. It effectively "fails safe."  
* **Latency:** This lane operates at "Human Speed" (≤ 500 ms for automated checks, or indefinitely for human review).2 While this introduces latency, it is *intentional*. In high-stakes scenarios (e.g., releasing a loan, firing a weapon, diagnosing a disease), speed is secondary to accuracy.  
* **Asynchronous Logging:** While the decision blocks, the *logging* of that decision is handled asynchronously to prevent system lockup. The log is pushed to a queue (e.g., Kafka) and then batched for blockchain anchoring.37

### **4.2 Merkle-Batched Storage and Certificate Transparency**

To create an immutable record without exposing sensitive data, TML utilizes **Merkle Trees** and principles from **Certificate Transparency** (CT) logs.39

* **Merkle Compression:** Rather than uploading terabytes of logs to a public blockchain (which is slow and expensive), TML batches thousands of logs into a **Merkle Tree**.  
  * Each log entry is hashed.  
  * Hashes are paired and hashed again until a single **Root Hash** remains.  
  * Only this Root Hash is anchored on-chain.25  
* **Verification:** This allows any auditor to verify the integrity of a specific log entry by requesting the "Merkle Proof" (the path from the leaf to the root) without needing to see the entire dataset. This proves the *integrity* of the logs while preserving *privacy*.41

### **4.3 Ephemeral Key Rotation (EKR)**

Companies hesitate to use auditable AI because they fear leaking trade secrets (model weights) or user privacy (GDPR data). TML employs **Ephemeral Key Rotation (EKR)** to solve this.42

* **The Mechanism:** Logs are encrypted with short-lived keys (Ephemeral Keys) that exist only for the duration of the audit window (e.g., 24 hours or per session).  
* **Forward Secrecy:** Once the key rotates, the *content* of the logs is no longer decryptable by the system itself, but the *integrity proofs* (hashes) remain on the blockchain forever.  
* **Access Control:** The keys are managed via a multi-party custody protocol (Hybrid Shield). Regulators or auditors can request the keys for a specific time window to decrypt the evidence, but the system owner cannot unilaterally decrypt (and thus alter) past records.42  
* **GDPR Compliance:** Sensitive user data is pseudonymized or deleted *before* hashing. The "Always Memory" applies to the *decision logic*, not the *user PII*.27 This ensures the "Right to be Forgotten" is respected while the "Duty to Document" is upheld.

### **4.4 The Reflection Cycle**

TML enables a **Reflection Cycle** that turns the "Sacred Zero" into a learning mechanism.2

1. **Hesitation:** System hits 0 (Uncertainty).  
2. **Logging:** Context is recorded in Moral Trace Log.  
3. **Review:** Human or Higher-Order Model reviews the log.  
4. **Training:** The resolution of the hesitation becomes new training data (RLHF \- Reinforcement Learning from Human Feedback).44  
5. Refinement: The system learns to resolve that specific ambiguity, turning future 0s into \+1 or \-1s.  
   This transforms the AI from a static model into a self-correcting ethical system.

## ---

**5\. Discussion: The Ethics of Persistent Attribution**

### **5.1 Authorship as a "Root of Trust"**

In the decentralized web (Web3) and cryptographic systems, trust is usually established through math, not people ("Don't Trust, Verify"). However, TML argues that *someone* must define the parameters of the verification. The **ORCID (0009-0006-5966-1243)** serves as the "Genesis Block" of the ethical chain.

* **Interoperability:** ORCID is a global standard for researcher identity.45 Using it allows TML to integrate with academic and scientific infrastructures, ensuring that the "author" is a verified entity, not a pseudonym.  
* **Traceability:** It allows investigators to trace the "Moral lineage" of the software. If a derivative system causes harm, the audit trail reveals whether the "Goukassian Promise" was kept intact or bypassed. This is critical for **Digital Forensics**.46

### **5.2 Ego vs. Civic Duty: The Defense of Stigler's Law**

Critics may argue that embedding Goukassian’s name is an act of ego. However, in the context of **Stigler’s Law** and **Strict Liability**, it is an act of **civic bravery** and strategic defense.

* **Liability Magnet:** By placing his name on the "conscience" of the system, Goukassian potentially exposes himself to reputational risk or litigation if the system fails (though strict liability usually targets the deployer, the "architect" is often deposed).24  
* **Anti-Dilution:** Corporations often release "Open" models that are actually black boxes. A verifiable authorship anchor forces transparency. It says, "This specific human logic is running here." If a corporation removes the name, they break the "Lantern," signaling to auditors that the system is no longer the "Safe" version.3

### **5.3 Technological Paternalism**

The "No Weapon / No Spy" mandate 47 represents a form of **Technological Paternalism**—the designer imposing limits on the user for their own safety.48

* **The Critique:** Paternalism is often seen as a violation of user autonomy. Users (or nations) should decide how to use the tool.  
* **The Defense:** In the context of "Dual-Use" technology (like AI that can guide missiles), paternalism is a moral obligation. The "Sacred Zero" prevents the AI from becoming a "moral zombie" that follows orders blindly. By hardcoding the refusal to spy or kill, TML ensures that the technology remains aligned with human rights *regardless* of the user's intent.

### **5.4 Comparison with "Tornado Cash"**

The contrast with **Tornado Cash** is instructive. The developers of Tornado Cash claimed they had no control over the software once deployed, yet they were held liable for its misuse because they designed it to be *anonymizing*.23 TML takes the opposite approach: it designs the software to be *attributable*.

* **Tornado Cash:** "I built it, but I am not responsible." (Result: Arrest).  
* **TML:** "I built it, and my name is embedded in every decision to prove I am responsible for the *logic* (but not the misuse)." (Result: Auditable Defense).

## ---

**6\. Comparison: Proactive Auditing vs. Post-Hoc Compliance**

### **6.1 The Post-Hoc Model (Current State)**

Conventional AI governance follows a "Deploy and Pray" model:

1. **Training:** Optimize for accuracy/speed.  
2. **Deployment:** Release to production.  
3. **Incident:** Harm occurs (e.g., bias, accident).  
4. **Audit:** Forensic teams try to reconstruct what happened from unstructured logs.  
5. **Regulation:** Fines are levied (e.g., GDPR).

This model is **inefficient** and **high-risk**. The harm has already occurred.

### **6.2 The Proactive TML Model**

TML inverts this workflow:

1. **Definition:** Embed Mandates (Goukassian Promise).  
2. **Runtime:** Input $\\rightarrow$ **Sacred Zero Check**.  
3. **Audit (Log):** The audit happens *simultaneously* with the decision. The "Moral Trace Log" is generated *before* the action is taken.  
4. **Action:** The system only acts if the log is successfully anchored ("No Log \= No Action").

This **"Audit-First"** architecture ensures that no decision—harmful or helpful—escapes the "Moral Trace." It transforms compliance from a "cost center" into an "operational guarantee."

### **6.3 Compliance with the EU AI Act**

The TML architecture aligns with, and effectively automates, key provisions of the **EU AI Act**:

* **Article 12 (Record-Keeping):** The "Always Memory" and "Moral Trace Logs" provide the automatic, continuous recording of events required by the Act.50  
* **Article 14 (Human Oversight):** The "Sacred Zero" state explicitly *demands* human intervention. It does not replace the human; it forces the system to wait for one. This satisfies the "Human-in-the-loop" requirement not just procedurally, but architecturally.51

## ---

**7\. Conclusion: The Verdict on the Goukassian Promise**

The inquiry of this report was whether it is appropriate for the **Goukassian Promise** and the associated **ORCID identifier** to remain permanently embedded in Ternary Moral Logic.

### **7.1 Summary of Findings**

1. **Provenance is Security:** In a digital ecosystem flooded with synthetic media and autonomous agents, knowing the **origin** of a system's logic is a security requirement. The ORCID acts as a **Digital Chain of Custody**, preventing the "Orphan Code" problem where no one is responsible for a malfunctioning AI.  
2. **Ethics Requires a Face:** Abstract ethical principles ("Do No Harm") are easily ignored. Personalized ethical vows ("I, Lev Goukassian, vow...") carry a weight of **reputational collateral**. The embedding operationalizes the **Right of Paternity** (*droit moral*) in a way that aligns with the immutability of blockchain ledgers.  
3. **The Lantern Must Not Be Extinguished:** The mechanism of the "Lantern" (the proof that the AI can hesitate) relies on the integrity of the Promise. Removing the signature breaks the chain of trust. Therefore, the persistence of the name is not vanity; it is **load-bearing architecture**.  
4. **Technical Feasibility:** The use of **Dual-Lane Latency**, **Merkle Batching**, and **Ephemeral Key Rotation** demonstrates that this level of auditing is technically feasible without destroying the utility of the AI.

### **7.2 Reasoned Judgment**

The **Goukassian Promise** should be viewed not as a software license, but as a **Constitutional Amendment** for the AI codebase. It represents a shift from "Move Fast and Break Things" to **"Pause, Reflect, and Record."**  
For regulators, TML offers a blueprint for **Auditable AI**. It demonstrates that speed and safety are not mutually exclusive, provided one is willing to accept the **"burden of memory"**—the immutable logging of every hesitation.  
In the final analysis, the persistence of Lev Goukassian’s name serves a function higher than ego: it serves as a **reminder**. It reminds the machine that it was made by a human, and it reminds the human that they are responsible for the machine. In the age of the Black Box, this persistent human anchor is the only thing keeping the light on.  
**Verdict:** The Name Remains.

### ---

**Addendum: Key Terminology Definitions**

* **Sacred Zero:** A logic state (0) triggering a mandatory pause for ethical evaluation.2  
* **Goukassian Promise:** The tripartite vow and cryptographic binding of authorship to the TML framework.3  
* **Moral Trace Log:** An immutable, schema-validated record of an AI's decision-making process, admissible as evidence.50  
* **Ephemeral Key Rotation (EKR):** A security protocol using short-lived encryption keys to protect log privacy while ensuring integrity.42  
* **Merkle Tree:** A cryptographic structure used to efficiently verify the integrity of large datasets (logs) via a single root hash.53  
* **ORCID:** A persistent digital identifier that distinguishes researchers and links their identity to their work.45  
* **Sidecar Pattern:** A deployment pattern where auxiliary tasks (like logging) run in a separate container alongside the main application.35

#### **Works cited**

1. Lev Goukassian | HackerNoon, accessed December 24, 2025, [https://hackernoon.com/about/lev-goukassian](https://hackernoon.com/about/lev-goukassian)  
2. FractonicMind/TernaryMoralLogic: Implementing Ethical Responsibility in AI Systems \- GitHub, accessed December 24, 2025, [https://github.com/FractonicMind/TernaryMoralLogic](https://github.com/FractonicMind/TernaryMoralLogic)  
3. How a Terminal Diagnosis Inspired a New Ethical AI System \- Hackernoon, accessed December 24, 2025, [https://hackernoon.com/how-a-terminal-diagnosis-inspired-a-new-ethical-ai-system](https://hackernoon.com/how-a-terminal-diagnosis-inspired-a-new-ethical-ai-system)  
4. Michel Foucault, “What Is an Author?” (extract), accessed December 24, 2025, [http://individual.utoronto.ca/bmclean/hermeneutics/foucault\_suppl/what\_is\_an\_author\_excerpt.htm](http://individual.utoronto.ca/bmclean/hermeneutics/foucault_suppl/what_is_an_author_excerpt.htm)  
5. AI Ethics in the Age of Decentralization: Navigating the New Frontier | by Vincenzo Boellis, accessed December 24, 2025, [https://medium.com/@vincenzoboellis/ai-ethics-in-the-age-of-decentralization-navigating-the-new-frontier-273c2254efa0](https://medium.com/@vincenzoboellis/ai-ethics-in-the-age-of-decentralization-navigating-the-new-frontier-273c2254efa0)  
6. Trying to understand why "Ethical Source Software" is a bad idea? : r/freesoftware \- Reddit, accessed December 24, 2025, [https://www.reddit.com/r/freesoftware/comments/18cz1tn/trying\_to\_understand\_why\_ethical\_source\_software/](https://www.reddit.com/r/freesoftware/comments/18cz1tn/trying_to_understand_why_ethical_source_software/)  
7. The Goukassian Vow. The origin story of the Lantern, the… \- Medium, accessed December 24, 2025, [https://medium.com/@leogouk/the-goukassian-vow-16d099262b9a](https://medium.com/@leogouk/the-goukassian-vow-16d099262b9a)  
8. Creative Commons: America's Moral Rights? \- The Fordham Law Archive of Scholarship and History, accessed December 24, 2025, [https://ir.lawnet.fordham.edu/cgi/viewcontent.cgi?article=1809\&context=iplj](https://ir.lawnet.fordham.edu/cgi/viewcontent.cgi?article=1809&context=iplj)  
9. The Integrity Right of an MP3: How the Introduction of Moral Rights into U.S. Law Can Help Combat Illegal Peer-to-Peer Music File Sharing \- eRepository @ Seton Hall, accessed December 24, 2025, [https://scholarship.shu.edu/context/shlr/article/1034/viewcontent/Spangler.pdf](https://scholarship.shu.edu/context/shlr/article/1034/viewcontent/Spangler.pdf)  
10. Copyright law of France \- Wikipedia, accessed December 24, 2025, [https://en.wikipedia.org/wiki/Copyright\_law\_of\_France](https://en.wikipedia.org/wiki/Copyright_law_of_France)  
11. Creative Commons licences, accessed December 24, 2025, [https://www.centre-mersenne.org/en/creative-commons-licences/](https://www.centre-mersenne.org/en/creative-commons-licences/)  
12. Copyright Policy \- OpenBSD, accessed December 24, 2025, [https://www.openbsd.org/policy.html](https://www.openbsd.org/policy.html)  
13. Simple permissive license that requires author statement in addition to copyright statement, accessed December 24, 2025, [https://opensource.stackexchange.com/questions/6691/simple-permissive-license-that-requires-author-statement-in-addition-to-copyrigh](https://opensource.stackexchange.com/questions/6691/simple-permissive-license-that-requires-author-statement-in-addition-to-copyrigh)  
14. Matthew: Effect or Fable? Working Paper \- Harvard Business School, accessed December 24, 2025, [https://www.hbs.edu/ris/download.aspx?name=12-049.pdf](https://www.hbs.edu/ris/download.aspx?name=12-049.pdf)  
15. The Matthew effect in empirical data \- PMC \- PubMed Central, accessed December 24, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC4233686/](https://pmc.ncbi.nlm.nih.gov/articles/PMC4233686/)  
16. Matthew effect \- Wikipedia, accessed December 24, 2025, [https://en.wikipedia.org/wiki/Matthew\_effect](https://en.wikipedia.org/wiki/Matthew_effect)  
17. When Einstein Walked with Gödel \- Bookey, accessed December 24, 2025, [https://cdn.bookey.app/files/pdf/book/en/when-einstein-walked-with-g%C3%B6del.pdf](https://cdn.bookey.app/files/pdf/book/en/when-einstein-walked-with-g%C3%B6del.pdf)  
18. List of eponymous laws \- Wikipedia, accessed December 24, 2025, [https://en.wikipedia.org/wiki/List\_of\_eponymous\_laws](https://en.wikipedia.org/wiki/List_of_eponymous_laws)  
19. Stigler's Law of Eponymy \- by Chad Woodard \- Medium, accessed December 24, 2025, [https://medium.com/@chadwoodard78/stiglers-law-of-eponymy-ca7d8ed97f0c](https://medium.com/@chadwoodard78/stiglers-law-of-eponymy-ca7d8ed97f0c)  
20. Various Licenses and Comments about Them \- GNU Project \- Free Software Foundation, accessed December 24, 2025, [https://www.gnu.org/licenses/license-list.en.html](https://www.gnu.org/licenses/license-list.en.html)  
21. Shower thought: First Do No Harm License is less like the Hippocrates Oath than free software : r/freesoftware \- Reddit, accessed December 24, 2025, [https://www.reddit.com/r/freesoftware/comments/nbgggs/shower\_thought\_first\_do\_no\_harm\_license\_is\_less/](https://www.reddit.com/r/freesoftware/comments/nbgggs/shower_thought_first_do_no_harm_license_is_less/)  
22. Post-Open Source \- boringcactus, accessed December 24, 2025, [https://www.boringcactus.com/2020/08/13/post-open-source.html](https://www.boringcactus.com/2020/08/13/post-open-source.html)  
23. Deep Dive on Delisting of Tornado Cash: Potential Implications? \- DeFi Education Fund, accessed December 24, 2025, [https://www.defieducationfund.org/deep-dive-on-delisting-of-tornado-cash-potential-implications/](https://www.defieducationfund.org/deep-dive-on-delisting-of-tornado-cash-potential-implications/)  
24. When Criminals Abuse the Blockchain: Establishing Personal Jurisdiction in a Decentralised Environment \- MDPI, accessed December 24, 2025, [https://www.mdpi.com/2075-471X/12/2/33](https://www.mdpi.com/2075-471X/12/2/33)  
25. I Accidentally Weaponized Philosophy Against Silicon Valley | by Lev Goukassian \- Medium, accessed December 24, 2025, [https://medium.com/@leogouk/i-accidentally-weaponized-philosophy-against-silicon-valley-80b68909ecb0](https://medium.com/@leogouk/i-accidentally-weaponized-philosophy-against-silicon-valley-80b68909ecb0)  
26. Negligence Liability for AI Developers \- Lawfare, accessed December 24, 2025, [https://www.lawfaremedia.org/article/negligence-liability-for-ai-developers](https://www.lawfaremedia.org/article/negligence-liability-for-ai-developers)  
27. The Day We Accidentally Became Disciples of a Dead Man's Digital Testament | by Lev Goukassian | Dec, 2025 | Medium, accessed December 24, 2025, [https://medium.com/@leogouk/the-day-we-accidentally-became-disciples-of-a-dead-mans-digital-testament-b83d96d46671](https://medium.com/@leogouk/the-day-we-accidentally-became-disciples-of-a-dead-mans-digital-testament-b83d96d46671)  
28. FractonicMind/TernaryLogic: Ternary Logic enforces evidence based economics. It stops risky actions during uncertainty, records every decision with immutable proof, exposes hidden manipulation, anchors economic history across public blockchains, protects stakeholders from opaque systems, and ensures capital flows remain accountable to society and the planet. \- GitHub, accessed December 24, 2025, [https://github.com/FractonicMind/TernaryLogic](https://github.com/FractonicMind/TernaryLogic)  
29. A UNESCO Researcher's Unexpected Morning | by Lev Goukassian | Nov, 2025 | Medium, accessed December 24, 2025, [https://medium.com/@leogouk/tml-to-unesco-the-operational-layer-you-forgot-to-write-down-e61b60d0e2da](https://medium.com/@leogouk/tml-to-unesco-the-operational-layer-you-forgot-to-write-down-e61b60d0e2da)  
30. Database Transactions and Optimistic Concurrency Control \- Azure Cosmos DB, accessed December 24, 2025, [https://learn.microsoft.com/en-us/azure/cosmos-db/database-transactions-optimistic-concurrency](https://learn.microsoft.com/en-us/azure/cosmos-db/database-transactions-optimistic-concurrency)  
31. Concurrency control in Amazon Aurora DSQL | AWS Database Blog, accessed December 24, 2025, [https://aws.amazon.com/blogs/database/concurrency-control-in-amazon-aurora-dsql/](https://aws.amazon.com/blogs/database/concurrency-control-in-amazon-aurora-dsql/)  
32. The Day the House Entered Epistemic Hold: A Story of Ternary Logic, Congress, and Credible Evidence | HackerNoon, accessed December 24, 2025, [https://hackernoon.com/the-day-the-house-entered-epistemic-hold-a-story-of-ternary-logic-congress-and-credible-evidence](https://hackernoon.com/the-day-the-house-entered-epistemic-hold-a-story-of-ternary-logic-congress-and-credible-evidence)  
33. Block unsafe prompts targeting your LLM endpoints with Firewall for AI \- The Cloudflare Blog, accessed December 24, 2025, [https://blog.cloudflare.com/block-unsafe-llm-prompts-with-firewall-for-ai/](https://blog.cloudflare.com/block-unsafe-llm-prompts-with-firewall-for-ai/)  
34. Non-Blocking Operations \- MuleSoft Documentation, accessed December 24, 2025, [https://docs.mulesoft.com/mule-sdk/latest/non-blocking-operations](https://docs.mulesoft.com/mule-sdk/latest/non-blocking-operations)  
35. Kubernetes Sidecars: A Comprehensive Guide \- Plural, accessed December 24, 2025, [https://www.plural.sh/blog/kubernetes-sidecar-guide/](https://www.plural.sh/blog/kubernetes-sidecar-guide/)  
36. Sidecar pattern \- Azure Architecture Center | Microsoft Learn, accessed December 24, 2025, [https://learn.microsoft.com/en-us/azure/architecture/patterns/sidecar](https://learn.microsoft.com/en-us/azure/architecture/patterns/sidecar)  
37. How to Build Real-Time Compliance & Audit Logging With Apache Kafka \- Confluent, accessed December 24, 2025, [https://www.confluent.io/blog/build-real-time-compliance-audit-logging-kafka/](https://www.confluent.io/blog/build-real-time-compliance-audit-logging-kafka/)  
38. How Meta built large-scale cryptographic monitoring, accessed December 24, 2025, [https://engineering.fb.com/2024/11/12/security/how-meta-built-large-scale-cryptographic-monitoring/](https://engineering.fb.com/2024/11/12/security/how-meta-built-large-scale-cryptographic-monitoring/)  
39. Certificate Transparency Logs: Your Early Warning System for SSL, accessed December 24, 2025, [https://cybersierra.co/blog/ssl-certificate-transparency-logs/](https://cybersierra.co/blog/ssl-certificate-transparency-logs/)  
40. Transparent Logs for Skeptical Clients \- research\!rsc, accessed December 24, 2025, [https://research.swtch.com/tlog](https://research.swtch.com/tlog)  
41. Don't trust your logs\! Implementing a Merkle tree for an Immutable Verifiable Log (in Go), accessed December 24, 2025, [https://arriqaaq.medium.com/dont-trust-your-logs-implementing-a-merkle-tree-for-an-immutable-verifiable-log-in-go-c242b558ae00](https://arriqaaq.medium.com/dont-trust-your-logs-implementing-a-merkle-tree-for-an-immutable-verifiable-log-in-go-c242b558ae00)  
42. Six Tech CEOs Accidentally Read the Wrong Paper and Nearly Rewrote Reality \- Medium, accessed December 24, 2025, [https://medium.com/@leogouk/six-tech-ceos-accidentally-read-the-wrong-paper-and-nearly-rewrote-reality-84d21a856481](https://medium.com/@leogouk/six-tech-ceos-accidentally-read-the-wrong-paper-and-nearly-rewrote-reality-84d21a856481)  
43. (PDF) SecureLLM: A Unified Framework for Privacy-Focused Large Language Models, accessed December 24, 2025, [https://www.researchgate.net/publication/390661744\_SecureLLM\_A\_Unified\_Framework\_for\_Privacy-Focused\_Large\_Language\_Models](https://www.researchgate.net/publication/390661744_SecureLLM_A_Unified_Framework_for_Privacy-Focused_Large_Language_Models)  
44. The Landscape of Agentic Reinforcement Learning for LLMs: A Survey \- OpenReview, accessed December 24, 2025, [https://openreview.net/pdf/c255d0345cad2239f28eee0d7932aabadecf1ef1.pdf](https://openreview.net/pdf/c255d0345cad2239f28eee0d7932aabadecf1ef1.pdf)  
45. Persistent identifiers \- OA Journals Toolkit, accessed December 24, 2025, [https://www.oajournals-toolkit.org/infrastructure/persistent-identifiers](https://www.oajournals-toolkit.org/infrastructure/persistent-identifiers)  
46. Expert Evidence and Digital Open Source Information | Journal of International Criminal Justice | Oxford Academic, accessed December 24, 2025, [https://academic.oup.com/jicj/article/21/4/661/7502637](https://academic.oup.com/jicj/article/21/4/661/7502637)  
47. The House Entered Epistemic Hold \- Medium, accessed December 24, 2025, [https://medium.com/@leogouk/the-day-the-house-entered-epistemic-hold-2492a52b04cd](https://medium.com/@leogouk/the-day-the-house-entered-epistemic-hold-2492a52b04cd)  
48. Governmental and Technological Paternalism (Chapter 4\) \- The Intelligence of Intuition, accessed December 24, 2025, [https://www.cambridge.org/core/books/intelligence-of-intuition/governmental-and-technological-paternalism/6A110DCF5799A1DF18531D8F7B2C5184](https://www.cambridge.org/core/books/intelligence-of-intuition/governmental-and-technological-paternalism/6A110DCF5799A1DF18531D8F7B2C5184)  
49. (PDF) Technology paternalism \- Wider implications of ubiquitous computing \- ResearchGate, accessed December 24, 2025, [https://www.researchgate.net/publication/225652621\_Technology\_paternalism\_-\_Wider\_implications\_of\_ubiquitous\_computing](https://www.researchgate.net/publication/225652621_Technology_paternalism_-_Wider_implications_of_ubiquitous_computing)  
50. The Email That Broke Brussels (Or: How I Learned to Stop Worrying and Love the Sacred Pause) | by Lev Goukassian | Nov, 2025 | Medium, accessed December 24, 2025, [https://medium.com/@leogouk/the-email-that-broke-brussels-or-how-i-learned-to-stop-worrying-and-love-the-sacred-pause-04c05c1a4c53](https://medium.com/@leogouk/the-email-that-broke-brussels-or-how-i-learned-to-stop-worrying-and-love-the-sacred-pause-04c05c1a4c53)  
51. Seven World Powers Accidentally Adopted a Dead Man's Constitution | by Lev Goukassian, accessed December 24, 2025, [https://medium.com/@leogouk/seven-world-powers-accidentally-adopted-a-dead-mans-constitution-510e11003be4](https://medium.com/@leogouk/seven-world-powers-accidentally-adopted-a-dead-mans-constitution-510e11003be4)  
52. When Your Law Professor Assigns a 40-Page Tech Ethics Doc and Says "Pop Quiz in 40 Minutes" | by Lev Goukassian \- Medium, accessed December 24, 2025, [https://medium.com/@leogouk/when-your-law-professor-assigns-a-40-page-tech-ethics-doc-and-says-pop-quiz-in-40-minutes-5b27631841d0](https://medium.com/@leogouk/when-your-law-professor-assigns-a-40-page-tech-ethics-doc-and-says-pop-quiz-in-40-minutes-5b27631841d0)  
53. RFC 9162 \- Certificate Transparency Version 2.0 \- IETF Datatracker, accessed December 24, 2025, [https://datatracker.ietf.org/doc/html/rfc9162](https://datatracker.ietf.org/doc/html/rfc9162)