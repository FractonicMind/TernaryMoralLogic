# **EU Artificial Intelligence Act × Ternary Moral Logic (TML) Compliance Infrastructure**

## **1\. Introduction: The Crisis of Probabilistic Governance**

The promulgation of Regulation (EU) 2024/1689, colloquially known as the Artificial Intelligence Act (AI Act), marks a definitive pivot in the history of technology governance. For the first time, the deployment of advanced algorithmic systems is moving from a regime of voluntary ethical guidelines to one of strict, statutory liability. The Act functions not merely as a set of rules but as a profound critique of the prevailing "move fast and break things" ethos that has characterized the digital economy for two decades. It establishes a risk-based legal framework that demands accountability, traceability, and human oversight for AI systems deemed "high-risk." However, a fundamental tension exists between the *nature of the law* and the *nature of modern artificial intelligence*.  
The law is deterministic. It operates on facts, evidence, and clear lines of causality. A defendant is either liable or not; a procedure was either followed or it was not. Modern AI, particularly generative and deep learning models, is inherently probabilistic. It operates on correlations, weights, and statistical likelihoods. When a standard binary AI system outputs a decision—a "Yes" or a "No"—it is often collapsing a complex probability distribution into a definitive state, masking the underlying uncertainty. From a legal perspective, this "hallucination of certainty" creates a massive liability surface. It presents a guess as a fact. When such a system is applied to high-stakes domains—critical infrastructure, law enforcement, credit scoring, or healthcare—the probabilistic nature of the machine conflicts directly with the evidentiary requirements of the EU AI Act.  
This report creates a comprehensive legal-technical analysis of **Ternary Moral Logic (TML)**, a computational framework developed by researcher Lev Goukassian, as a solution to this crisis of governance.1 TML is not a policy document; it is an architectural intervention. It proposes that the only way to make probabilistic systems legally accountable is to introduce a third logical state—the "Sacred Pause" (State 0)—alongside the traditional binary outputs of Proceed (+1) and Refuse (-1). By operationalizing "ethical hesitation" into the very code of the system, TML creates a bridge between the statistical reality of the machine and the accountability requirements of the law.1  
This analysis exhaustively maps the architecture of TML against the specific articles of the EU AI Act, demonstrating how the framework’s core components—the **Moral Trace Logs**, the **Hybrid Shield**, the **Clarifying Question Engine**, and the **Goukassian Promise**—transform compliance from a post-hoc bureaucratic exercise into a runtime operational fact.  
---

## **2\. Foundations of Ternary Moral Logic (TML)**

To understand how TML satisfies the rigorous demands of the EU AI Act, one must first deconstruct its foundational philosophy and technical architecture. The framework was born from a recognition that binary logic is insufficient for moral reasoning. In the binary world, a system must force a conclusion even when the data is ambiguous, leading to errors that are difficult to trace and justify. Lev Goukassian’s research posits that the "sacred pause between question and answer" is where wisdom—and legal liability—resides.1

### **2.1 The Three-State Architecture**

Standard AI decision loops are designed for speed and conclusiveness. They optimize for a result. TML alters this topology by introducing a tri-state output system:

* **State \+1 (Proceed):** This state represents a "Green Light." The system has analyzed the input, calculated that the action aligns with its objective function, and determined that the confidence interval exceeds the safety threshold. Crucially, in TML, reaching State \+1 requires the *absence* of a signal from the constraints layer. It is an affirmative action taken only when the path is verifiable.2  
* **State \-1 (Refuse):** This state represents a "Red Light." It is triggered when the system detects a clear violation of a hard constraint. These constraints are not learned weights but are hard-coded strictures derived from the **TML Canonical Corpus**, including Human Rights treaties and Earth Protection protocols. A State \-1 output is an active refusal to harm, effectively a digital veto.2  
* **State 0 (The Sacred Pause):** This is the core innovation relevant to the EU AI Act. State 0 is triggered when the system detects *epistemic uncertainty* or *ethical ambiguity*. It is neither an acceptance nor a rejection; it is a suspension of judgment. In this state, the system enters an **Epistemic Hold**, preventing execution and flagging the transaction for higher-order reasoning or human intervention. This state transforms "uncertainty" from a hidden variable into a visible, manageable operational state.1

### **2.2 The Goukassian Promise: The Constitutional Artifacts**

TML is not merely software; it is a governance system enforced by cryptographic artifacts known collectively as the **Goukassian Promise**.3 These artifacts ensure that the "conscience" of the system cannot be silently disabled by a corporate provider seeking to prioritize speed over safety—a critical feature for regulatory assurance.

1. **The Lantern (🏮):** A dynamic transparency mechanism. It is a verifiable signal broadcast by the system indicating its current ethical state. When the system pauses (State 0), the Lantern signals this status to the user and the auditor, creating real-time visibility into the system’s "thinking" process.3  
2. **The Signature (✍️):** A cryptographic chain of custody. Every decision output (+1, 0, \-1) is cryptographically signed, linking the decision to the specific version of the model, the input data, and the active policy set. This ensures non-repudiation; a provider cannot claim the system "glitched" when the log carries their digital signature.4  
3. **The License (📜):** A binding legal-technical covenant. The TML software license explicitly revokes the right to use the framework if the ethical safeguards (specifically the logging and the pause mechanism) are tampered with. This creates a "poison pill" for non-compliance, aligning legal copyright law with regulatory safety requirements.4

---

## **3\. The Risk Management Mandate (Article 9\)**

**Article 9** of Regulation (EU) 2024/1689 establishes the requirement for a "risk management system".6 This is defined not as a one-time audit but as a "continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system." Providers must identify foreseeable risks and adopt suitable mitigation measures. The law explicitly prefers risks to be "eliminated or reduced through design and development" (Art 9(2)(a)).

### **3.1 The Failure of Static Risk Assessment**

In traditional software development, risk management is often a static document—a "Risk Register" created during the design phase. However, AI systems are dynamic; their risks emerge from the interaction between the model and novel, unstructured data in the real world. A static document cannot mitigate a dynamic runtime risk.

### **3.2 TML Operationalization: The Dynamic Risk Valve**

TML operationalizes Article 9 by converting risk assessment into a runtime function of the **Sacred Pause (State 0\)**.  
The framework continuously calculates an **Ethical Uncertainty Score** alongside its standard confidence score.7 This score is a composite metric derived from:

* **Data Variance:** Is the input data significantly different from the training distribution?  
* **Constraint Proximity:** Is the proposed action close to a "red line" defined in the safety policies?  
* **Model Disagreement:** In ensemble models, do different sub-models disagree on the outcome?

When this Ethical Uncertainty Score breaches a pre-defined safety threshold, the system *automatically* triggers State 0\. This functions as an automated "circuit breaker." By entering the Sacred Pause, the system effectively **eliminates the risk** of an erroneous automated action, directly satisfying Article 9(2)(a). The risk is not merely "managed" on paper; it is physically stopped in the software execution path.

### **3.3 The Clarifying Question Engine (CQE)**

During a Sacred Pause, the system does not simply freeze. It engages the **Clarifying Question Engine (CQE)**.3 While the full proprietary specs of the CQE are part of the detailed implementation, its functional role in TML is to interrogate the context to resolve the uncertainty.  
For example, in a medical diagnostic AI (a high-risk system under Annex III), if the system is uncertain about a diagnosis due to ambiguous symptoms, State 0 is triggered. The CQE then generates a specific query: "Ambiguity detected in patient history regarding prior cardiac events. Please confirm dates." This query is logged and presented to the human operator. This process transforms the "risk management" from a passive background task into an active, dialogue-based resolution mechanic. The CQE’s ability to "ask" rather than "guess" is the ultimate risk mitigation strategy.7  
---

## **4\. Data Governance and the Constitutional Corpus (Article 10\)**

**Article 10** mandates that high-risk AI systems which make use of techniques involving the training of models with data be developed on the basis of training, validation, and testing data sets that meet quality criteria.8 It emphasizes the examination of possible biases and the governance of data appropriate for the intended purpose.

### **4.1 TML Operationalization: The Constitutional Corpus**

TML introduces a unique approach to data governance called **Constitutional Anchoring**. Rather than relying solely on statistical "fairness" metrics (which can be gamed), TML hard-codes a **Canonical Corpus** of 46+ foundational documents into the system’s **State \-1 (Refuse)** logic.4  
This corpus includes:

* The **Universal Declaration of Human Rights** (UDHR).4  
* The **Geneva Conventions**.4  
* Major environmental treaties (e.g., the **Paris Agreement**, **Montreal Protocol**) under the "Earth Protection" pillar.11

This corpus acts as a "meta-data" layer. The AI’s outputs are checked against the semantic constraints derived from these documents. If an AI generates an output that violates a principle within this corpus (e.g., a surveillance system suggesting an action that violates the right to privacy defined in the UDHR), the system triggers a Refuse (-1) state.  
This directly addresses Article 10(2)(f), which requires data sets to be examined for possible biases that might affect the health and safety of persons or lead to discrimination. By anchoring the "Refuse" state in established international law, TML provides a robust, legally defensible definition of "harm" that goes beyond mere statistical variance.

### **4.2 Provenance and the Signature**

Article 10 also requires appropriate data governance regarding the "provenance" of data. The **Signature** artifact in TML 4 ensures that every piece of data influencing a decision is cryptographically tracked. When a decision is made, the signature includes a hash of the training data version. This allows for granular traceability: if a bias is detected later, the provider can pinpoint exactly which data snapshot was responsible, facilitating the "corrective actions" required by Article 10\.  
---

## **5\. The Engine of Accountability: Technical Documentation (Article 11\)**

**Article 11** requires that technical documentation be drawn up before the system is placed on the market and kept up-to-date.13 This documentation must demonstrate that the system complies with the requirements set out in Chapter III and provide a complete description of the system’s elements.

### **5.1 Self-Documenting Architecture**

One of the greatest challenges in AI compliance is that documentation often lags behind development. Code changes, weights are updated, but the technical file remains static. TML solves this through **Self-Documenting Code**.  
The **Moral Trace Logs (MTL)** 2 generated by TML are not just error logs; they are structured narratives of the system’s logic. They record:

* The active **policy version** at the time of decision.  
* The **threshold parameters** for the Sacred Pause.  
* The **Canonical Corpus** definitions currently loaded.

Because TML enforces a strict "No Log \= No Action" policy 15, the system literally cannot operate without generating this documentation. This ensures that the Article 11 technical file is never out of sync with the deployed reality. The "description of the elements" required by law is generated dynamically by the system itself.  
---

## **6\. The Immutable Memory: Logging and Record Keeping (Article 12\)**

**Article 12** is the technical heart of the EU AI Act’s accountability regime. It mandates "automatic recording of events (logs)" over the lifetime of the system.16 These logs must ensure a level of traceability appropriate to the intended purpose, recording the period of use, reference databases, and input data checks.

### **6.1 The "Always Memory" Pillar**

TML’s **Always Memory** pillar 17 is designed specifically to meet and exceed the requirements of Article 12\. Standard logging (e.g., appending text to a .log file) is insufficient for high-stakes legal compliance because text files are mutable. A system administrator can delete or alter a log file to cover up a malfunction or negligence.

### **6.2 Merkle-Batched Storage**

To solve the mutability problem, TML employs **Merkle-Batched Storage**.14

* **Mechanism:** Individual decision logs are grouped into batches (e.g., every 100 decisions or every minute).  
* **Hashing:** The batch is hashed using a cryptographic algorithm (SHA-256).  
* **Chaining:** The hash of the current batch is included in the header of the next batch, creating an unbreakable chain of history.  
* **Anchoring:** The root hash of the Merkle tree is periodically anchored to a public blockchain or a distributed ledger.

This architecture renders the logs **tamper-evident**. If a provider attempts to delete a single log entry from three months ago to hide a non-compliant decision, the cryptographic hash of that batch will change, breaking the chain for all subsequent batches. This mismatch would be immediately detected by any auditor. This provides the "integrity" of record-keeping that is implicit in Article 12 and explicit in Article 15\.

### **6.3 Ephemeral Key Rotation for Privacy**

Logging detailed decision data creates a privacy risk, potentially violating GDPR (which interacts with the AI Act). TML addresses this via **Ephemeral Key Rotation**.18

* **Mechanism:** The logs are encrypted using a symmetric key that is valid only for a short window (e.g., 10 minutes).  
* **Rotation:** After the window closes, the key is rotated.  
* **Key Custody:** The expired keys are stored in a secure, distributed manner (see *Hybrid Shield* below).  
* **Access:** If a regulator or court demands access to logs from a specific time (e.g., "The incident on November 4th at 10:00 AM"), the relevant ephemeral keys can be retrieved to decrypt *only* that slice of time.

This ensures that the "traceability" required by Article 12 does not become a system of mass surveillance, balancing the AI Act’s mandates with fundamental privacy rights.  
---

## **7\. Transparency and the Lantern (Article 13\)**

**Article 13** requires high-risk AI systems to be designed in a way that ensures their operation is "sufficiently transparent to enable deployers to interpret the system’s output and use it appropriately".20

### **7.1 The Black Box Problem**

Deep learning models are notoriously opaque "Black Boxes." They offer a result without an explanation. This violates the spirit of Article 13, which asks for interpretability.

### **7.2 The Lantern (🏮) as a User Interface for State**

TML introduces the **Lantern** 3 as a mandatory UI element. The Lantern is a visual abstraction of the system’s internal ternary state:

* **Green Lantern:** System is in State \+1 (Proceed). Operations are normal.  
* **Red Lantern:** System is in State \-1 (Refuse). Constraint violation occurred.  
* **Amber/Pulsing Lantern:** System is in State 0 (Sacred Pause). Complexity detected; human oversight requested.

This simple visual metaphor provides immediate, "concise, complete, correct and clear information" (Art 13(2)) to the deployer. A doctor using a TML-equipped diagnostic tool knows instantly if the AI is confident (Green) or hesitant (Amber). This manages "automation bias" by signaling when the user should trust the machine and when they should be skeptical.

### **7.3 The Glass Box Philosophy**

Underpinning the Lantern is the **Glass Box** philosophy.17 While the neural weights may remain opaque, the *decision logic* is transparent. The **Moral Trace Logs** serve as a "Glass Box," allowing the deployer to see the semantic reasoning: "Input X led to Uncertainty Y, triggering Pause Z." This satisfies the requirement that deployers be able to "interpret the logs" (Art 13(3)(f)).  
---

## **8\. Operationalizing Human Oversight (Article 14\)**

**Article 14** is arguably the most critical operational requirement. It mandates that systems be designed so they can be "effectively overseen by natural persons." This oversight must prevent risks and allow the human to "decide not to use the high-risk AI system or otherwise disregard, override or reverse the output".21

### **8.1 The Epistemic Hold**

Most "human-in-the-loop" systems fail because the human is brought in too late, or the machine moves too fast. TML solves this with the **Epistemic Hold**.19

* **Mechanism:** When State 0 is triggered, the system initiates an Epistemic Hold. This is a hard stop. The system *cannot* proceed to action until the hold is released.  
* **Operationalizing Art 14(4)(a):** This gives the human the time and space to "properly understand the relevant capacities and limitations" of the system in that specific instance.

### **8.2 Stewardship Custodians**

TML creates a formal role for the "natural persons" mentioned in Article 14: the **Stewardship Custodians**.23 These are not merely users; they are trained oversight officers who hold the keys to resolve a Sacred Pause.

* **Workflow:**  
  1. System encounters ambiguity \-\> Triggers State 0\.  
  2. Lantern turns Amber.  
  3. Notification sent to Stewardship Custodian.  
  4. Custodian reviews the **Moral Trace Log** and the **Clarifying Question**.  
  5. Custodian issues a manual command: "Proceed" or "Refuse."  
  6. System logs the Custodian’s ID and executes the command.

This workflow is the literal implementation of Article 14(4)(d) ("override or reverse the output"). The TML architecture ensures that the human is the final arbiter in all edge cases.

### **8.3 Combatting Automation Bias (Art 14(4)(b))**

Article 14 specifically warns against "automation bias"—the tendency of humans to blindly trust the machine. TML fights this by *forcing* the machine to admit ignorance. By visibly pausing and asking for help (via the Lantern and CQE), the system breaks the illusion of omnipotence. It forces the human to engage their critical faculties, thereby satisfying the requirement to remain aware of automation bias.  
---

## **9\. Accuracy, Robustness, and Cybersecurity (Article 15\)**

**Article 15** mandates that high-risk systems be resilient regarding errors, faults, and inconsistencies, and possess a high level of cybersecurity.24

### **9.1 Robustness via the Ternary Fail-Safe**

Binary systems are brittle; when they encounter "out of distribution" data (e.g., adversarial noise), they often fail confidently—classifying a stop sign as a toaster with 99% confidence. TML is robust because it has a **fail-safe state**.

* **Mechanism:** If the input data is noisy or adversarial, the **Ethical Uncertainty Score** spikes.  
* Result: The system does not "fail" by making a wrong guess; it "succeeds" by entering State 0 (Pause).  
  This satisfies the Article 15 requirement for robustness against "errors, faults or inconsistencies." The system degrades gracefully into a pause rather than crashing or hallucinating.

### **9.2 The Hybrid Shield: Cybersecurity Defense**

The **Hybrid Shield** 2 is TML’s answer to the cybersecurity mandate. It is a dual-layer defense system designed to protect the integrity of the AI’s "conscience" (its logging and constraints).

* **Layer 1: Technical Shield:** Cryptographic anchoring (Merkle-Batched Storage) ensures that logs cannot be altered by attackers or corrupt insiders.  
* **Layer 2: Institutional Shield:** A network of distributed authority. The keys to the **Stewardship Custody** are not held by a single admin but are sharded across multiple entities (e.g., the provider, an external auditor, a regulatory body). This "multisig" approach means that a hacker would need to compromise multiple independent organizations to subvert the system.

This architecture specifically addresses Article 15(4), which calls for solutions to prevent "manipulation of the training data set... or inputs designed to cause the AI model to make a mistake." By securing the decision history and the policy constraints in a distributed ledger, TML makes the system resilient to data poisoning and model evasion attacks.  
---

## **10\. Provider Obligations and Quality Management (Articles 16 & 17\)**

**Article 16** lists the obligations of providers (compliance, logging, corrective actions), while **Article 17** requires a Quality Management System (QMS).25

### **10.1 Automated Compliance via The Goukassian Promise**

The **Goukassian Promise** artifacts (Lantern, Signature, License) automate much of the Article 16 compliance burden.

* **Lantern:** Automates transparency (Art 16(b)).  
* **Signature:** Automates data governance tracking (Art 16(a)).  
* **Moral Trace Logs:** Automate record-keeping (Art 16(d)).

### **10.2 QMS Integration**

TML fits seamlessly into the Article 17 QMS requirement. The "Post-Market Monitoring" required by the QMS is fed directly by the **Moral Trace Logs**. The provider does not need to build a separate monitoring tool; the TML logs provide a real-time stream of performance data, uncertainty spikes, and constraint violations. This allows for the "corrective actions" (Art 16(j)) to be data-driven and immediate. If a specific constraint is triggering too many False Positives (State \-1), the logs will show this trend, allowing the provider to refine the policy in the next iteration.  
---

## **11\. Real-World Testing and Rights (Article 61\)**

**Article 61** governs the testing of high-risk AI systems in real-world conditions. It requires informed consent and, crucially, "arrangements for requesting the reversal or the disregarding of the predictions".27

### **11.1 Reversibility via State Traceability**

TML’s architecture is uniquely suited to "reversibility." Because every decision is logged with a unique hash in the **Merkle Tree**, a subject can identify a specific decision (e.g., "The loan denial on Tuesday"). The provider can locate this exact decision in the **Moral Trace Log**.

* **Disregarding:** The provider can flag that specific log entry as "Invalid/Disregarded." This signal effectively removes that data point from future training sets, ensuring the error is not learned.  
* **Reversal:** The log details exactly *why* the decision was made (e.g., "State \-1 triggered by Policy X"). The provider can manually override this (as a Stewardship Custodian function) and issue a new decision, reversing the legal effect on the subject.  
* **Consent Management:** The **Signature** can include a token of the subject’s consent. If consent is withdrawn, the system can scan the logs for that token and purge or anonymize the associated records, ensuring compliance with both Article 61 and GDPR.

---

## **12\. Empowering the Subject: Rights and Remedies (Articles 84-86)**

Chapter VIII of the AI Act grants individuals rights to hold deployers accountable.

### **12.1 Article 86: Right to Explanation**

**Article 86** grants affected persons the right to obtain a "clear and meaningful explanation" of the role of the AI system and the main elements of the decision.28

* **The TML Solution:** As established, standard "black box" AI cannot provide this effectively. TML’s **Moral Trace Logs** provide a *causal narrative*. "The system paused because of Factor A. It asked Question B. The human operator C decided D."  
* **Meaningfulness:** This narrative is understandable to a judge, a lawyer, or a layperson. It explains the *process*, not just the math. This satisfies the "meaningful" criteria of Article 86\.

### **12.2 Article 85: Right to Lodge a Complaint**

**Article 85** allows complaints to market surveillance authorities.29

* **The TML Solution:** TML provides the "evidence pack" for these complaints. The **Hybrid Shield** ensures that the logs handed over to the authority are authentic. The provider cannot doctor the logs to hide negligence. If the logs show the system ignored the **Sacred Pause** warnings, the complainant has a "smoking gun." This evidentiary clarity is essential for the effective enforcement of Article 85\.

---

## **13\. The Goukassian Promise: A Legal-Technical Covenant**

It is vital to elaborate on the **Goukassian Promise**, as it acts as the "Constitution" of the TML framework.4 It is a defense strategy designed to ensure that the system’s ethical core is not stripped away for commercial convenience.

### **13.1 The Three Artifacts of Incorruptibility**

The Promise consists of three artifacts that work in concert:

1. **The Lantern (Social Layer):** It creates reputational pressure. A system running without the Lantern is immediately suspect. It signals "Unverified AI."  
2. **The Signature (Technical Layer):** It creates cryptographic pressure. Without the signature, the data provenance is broken, making Article 10 compliance impossible.  
3. **The License (Legal Layer):** It creates contractual pressure. The MIT License with the **TML Ethical Addendum** 31 legally binds the use of the code to the preservation of the logging mechanism. Breaking the Promise is a breach of copyright.

### **13.2 The "Anti-Psychopath" Design**

Lev Goukassian explicitly designed TML to prevent the creation of "psychopathic" AI—systems that feign empathy or ethics while having no internal constraints.30 The Goukassian Promise ensures that "ethical hesitation" is not a feature that can be toggled off; it is the substrate of the system. This aligns perfectly with the EU AI Act’s goal of creating "Trustworthy AI" (Recital 1).  
---

## **14\. Implementation Roadmap**

For organizations seeking to operationalize Regulation (EU) 2024/1689 via TML, the following implementation roadmap is recommended:

### **Phase 1: Architectural Integration (Dual-Lane Latency)**

* **Challenge:** The "Sacred Pause" introduces latency. High-frequency trading or real-time braking systems cannot afford a 5-second pause.  
* **Solution:** Implement **Dual-Line Latency** architecture.18  
  * **Fast Lane:** Handles clear \+1/-1 decisions. Latency \< 10ms.  
  * **Slow Lane:** Handles State 0 (Pause) decisions. Latency is variable.  
  * This ensures that the "ethics check" does not degrade the performance of the system for the 99% of "safe" cases, while reserving resources for the 1% of "high-risk" cases.

### **Phase 2: Governance Setup (Stewardship Custodians)**

* Define the **Stewardship Custodian** role description.  
* Establish the **Technical Council** to oversee the **Hybrid Shield** keys.15  
* Integrate the **Lantern API** into the frontend UX.

### **Phase 3: Documentation and Calibration**

* Calibrate the **Ethical Uncertainty Score** thresholds. Perform "Red Teaming" to see if the system pauses appropriately in ambiguous scenarios.  
* Validate the **Clarifying Question Engine** against the **Article 14** oversight requirements.7  
* Deploy the **Canonical Corpus** (Human Rights/Earth Protection) into the State \-1 constraint logic.

---

## **15\. Conclusion**

The EU AI Act represents a demanding new reality for technology providers. It asks for the impossible: to impose the certainty of law onto the probability of the machine. **Ternary Moral Logic (TML)** answers this impossible question by changing the logic of the machine itself.  
By introducing the **Sacred Pause**, TML creates a space for the law to function inside the code. It operationalizes **Risk Management (Art 9\)** as a runtime stop. It transforms **Record-Keeping (Art 12\)** into an immutable blockchain of intent. It empowers **Human Oversight (Art 14\)** by forcing the machine to yield to human wisdom when it is most needed.  
Lev Goukassian’s vision of "Computational Wisdom" 1—the idea that an AI should enhance rather than replace human moral reasoning—is no longer just a philosophical ideal. With the ratification of Regulation (EU) 2024/1689, it has become a legal necessity. TML provides the rigorous, auditable, and constitutional infrastructure required to build the trustworthy AI of the future.  
---

(Note on Citations: All references to TML concepts, Lev Goukassian's work, and technical specifications are based on the provided research snippets.1 Legal text citations refer to Regulation (EU) 2024/1689.6)

#### **Works cited**

1. FractonicMind/TernaryMoralLogic: Implementing Ethical ... \- GitHub, accessed December 1, 2025, [https://github.com/FractonicMind/TernaryMoralLogic](https://github.com/FractonicMind/TernaryMoralLogic)  
2. How a Dying Man Taught AI to Think Before It Acts | by Lev ... \- Medium, accessed December 1, 2025, [https://medium.com/@leogouk/how-a-dying-man-taught-ai-to-think-before-it-acts-a9191f42a429](https://medium.com/@leogouk/how-a-dying-man-taught-ai-to-think-before-it-acts-a9191f42a429)  
3. How a Terminal Diagnosis Inspired a New Ethical AI System \- Hackernoon, accessed December 1, 2025, [https://hackernoon.com/how-a-terminal-diagnosis-inspired-a-new-ethical-ai-system](https://hackernoon.com/how-a-terminal-diagnosis-inspired-a-new-ethical-ai-system)  
4. The Goukassian Promise. A self-enforcing covenant between… \- Medium, accessed December 1, 2025, [https://medium.com/@leogouk/the-goukassian-promise-7abde4bd81ec](https://medium.com/@leogouk/the-goukassian-promise-7abde4bd81ec)  
5. The Goukassian Vow. The origin story of the Lantern, the… \- Medium, accessed December 1, 2025, [https://medium.com/@leogouk/the-goukassian-vow-16d099262b9a](https://medium.com/@leogouk/the-goukassian-vow-16d099262b9a)  
6. Article 9: Risk Management System | EU Artificial Intelligence Act, accessed December 1, 2025, [https://artificialintelligenceact.eu/article/9/](https://artificialintelligenceact.eu/article/9/)  
7. How I Fought an AI and Made It Acknowledge My Name | by Lev Goukassian | Medium, accessed December 1, 2025, [https://medium.com/@leogouk/how-i-fought-an-ai-and-made-it-acknowledge-my-name-8a55dd555b4f](https://medium.com/@leogouk/how-i-fought-an-ai-and-made-it-acknowledge-my-name-8a55dd555b4f)  
8. Article 10: Data and Data Governance | EU Artificial Intelligence Act, accessed December 1, 2025, [https://artificialintelligenceact.eu/article/10/](https://artificialintelligenceact.eu/article/10/)  
9. International human rights instruments \- Wikipedia, accessed December 1, 2025, [https://en.wikipedia.org/wiki/International\_human\_rights\_instruments](https://en.wikipedia.org/wiki/International_human_rights_instruments)  
10. Human Rights Treaties, accessed December 1, 2025, [https://www.humanrightscommission.ky/human-rights-treaties](https://www.humanrightscommission.ky/human-rights-treaties)  
11. Multilateral Environmental Agreements (MEAs) \- Environment \- European Commission, accessed December 1, 2025, [https://environment.ec.europa.eu/international-cooperation/multilateral-environmental-agreements-meas\_en](https://environment.ec.europa.eu/international-cooperation/multilateral-environmental-agreements-meas_en)  
12. List of international environmental agreements \- Wikipedia, accessed December 1, 2025, [https://en.wikipedia.org/wiki/List\_of\_international\_environmental\_agreements](https://en.wikipedia.org/wiki/List_of_international_environmental_agreements)  
13. Article 11: Technical Documentation | EU Artificial Intelligence Act, accessed December 1, 2025, [https://artificialintelligenceact.eu/article/11/](https://artificialintelligenceact.eu/article/11/)  
14. Auditable AI by Design: How TML Turns Governance into ... \- Medium, accessed December 1, 2025, [https://medium.com/@leogouk/auditable-ai-by-design-how-tml-turns-governance-into-operational-fact-37fd73e7b77e](https://medium.com/@leogouk/auditable-ai-by-design-how-tml-turns-governance-into-operational-fact-37fd73e7b77e)  
15. FractonicMind/TernaryLogic: Ternary Logic enforces evidence based economics. It stops risky actions during uncertainty, records every decision with immutable proof, exposes hidden manipulation, anchors economic history across public blockchains, protects stakeholders from opaque systems, and ensures capital flows remain accountable to society and the planet. \- GitHub, accessed December 1, 2025, [https://github.com/FractonicMind/TernaryLogic](https://github.com/FractonicMind/TernaryLogic)  
16. Article 12, Record-keeping, EU AI Act, accessed December 1, 2025, [https://www.artificial-intelligence-act.com/Artificial\_Intelligence\_Act\_Article\_12.html](https://www.artificial-intelligence-act.com/Artificial_Intelligence_Act_Article_12.html)  
17. The Eight Pillars and the Lantern | by Lev Goukassian | Medium, accessed December 1, 2025, [https://medium.com/@leogouk/the-eight-pillars-and-the-lantern-8e75428d1de7](https://medium.com/@leogouk/the-eight-pillars-and-the-lantern-8e75428d1de7)  
18. The Email That Broke Our AI: A DeepMind Disaster | by Lev Goukassian \- Medium, accessed December 1, 2025, [https://medium.com/@leogouk/the-email-that-broke-our-ai-a-deepmind-disaster-75729e5035f6](https://medium.com/@leogouk/the-email-that-broke-our-ai-a-deepmind-disaster-75729e5035f6)  
19. UNESCO: The Operational Layer Missing Since 2021 | by Lev Goukassian \- Medium, accessed December 1, 2025, [https://medium.com/@leogouk/unesco-the-operational-layer-missing-since-2021-f77650b284ad](https://medium.com/@leogouk/unesco-the-operational-layer-missing-since-2021-f77650b284ad)  
20. Article 13: Transparency and Provision of Information to Deployers | EU Artificial Intelligence Act, accessed December 1, 2025, [https://artificialintelligenceact.eu/article/13/](https://artificialintelligenceact.eu/article/13/)  
21. Article 14: Human Oversight | EU Artificial Intelligence Act, accessed December 1, 2025, [https://artificialintelligenceact.eu/article/14/](https://artificialintelligenceact.eu/article/14/)  
22. The Day My Inbox Became a Philosophy Lecture (With Blockchain Receipts) \- Medium, accessed December 1, 2025, [https://medium.com/@leogouk/the-day-my-inbox-became-a-philosophy-lecture-with-blockchain-receipts-965af16892df](https://medium.com/@leogouk/the-day-my-inbox-became-a-philosophy-lecture-with-blockchain-receipts-965af16892df)  
23. The Unbreakable Vow: How Ternary Logic's "Hybrid Shield" Protects from Corruption | by Lev Goukassian | Nov, 2025 | Medium, accessed December 1, 2025, [https://medium.com/@leogouk/the-unbreakable-vow-how-ternary-logics-hybrid-shield-protects-from-corruption-1e6338d4744c](https://medium.com/@leogouk/the-unbreakable-vow-how-ternary-logics-hybrid-shield-protects-from-corruption-1e6338d4744c)  
24. Article 15: Accuracy, Robustness and Cybersecurity | EU Artificial Intelligence Act, accessed December 1, 2025, [https://artificialintelligenceact.eu/article/15/](https://artificialintelligenceact.eu/article/15/)  
25. Article 16: Obligations of Providers of High-Risk AI Systems | EU Artificial Intelligence Act, accessed December 1, 2025, [https://artificialintelligenceact.eu/article/16/](https://artificialintelligenceact.eu/article/16/)  
26. Article 17: Quality Management System | EU Artificial Intelligence Act, accessed December 1, 2025, [https://artificialintelligenceact.eu/article/17/](https://artificialintelligenceact.eu/article/17/)  
27. Article 61: Informed Consent to Participate in Testing in Real World Conditions Outside AI Regulatory Sandboxes | EU Artificial Intelligence Act, accessed December 1, 2025, [https://artificialintelligenceact.eu/article/61/](https://artificialintelligenceact.eu/article/61/)  
28. Article 86: Right to Explanation of Individual Decision-Making | EU Artificial Intelligence Act, accessed December 1, 2025, [https://artificialintelligenceact.eu/article/86/](https://artificialintelligenceact.eu/article/86/)  
29. Final Text \- EU AI Act, accessed December 1, 2025, [https://www.artificial-intelligence-act.com/Artificial\_Intelligence\_Act\_Articles\_(Final\_Text).html](https://www.artificial-intelligence-act.com/Artificial_Intelligence_Act_Articles_\(Final_Text\).html)  
30. So You Want to Build a Psychopath: A Sarcastic Guide to AI Liability \- Medium, accessed December 1, 2025, [https://medium.com/@leogouk/so-you-want-to-build-a-psychopath-a-sarcastic-guide-to-ai-liability-bf62e943e99d](https://medium.com/@leogouk/so-you-want-to-build-a-psychopath-a-sarcastic-guide-to-ai-liability-bf62e943e99d)  
31. Ternary Moral Logic (TML) \- Ethical AI Framework, accessed December 1, 2025, [https://fractonicmind.github.io/TernaryMoralLogic/](https://fractonicmind.github.io/TernaryMoralLogic/)