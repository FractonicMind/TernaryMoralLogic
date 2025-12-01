# **EU Artificial Intelligence Act × Ternary Moral Logic (TML) Governance Report**

## **I. Introduction: The Necessity of Executable Ethics in AI Regulation**

### **I.A. The Regulatory Challenge of High-Risk AI under Regulation (EU) 2024/1689**

Regulation (EU) 2024/1689, the European Union Artificial Intelligence Act, establishes the world's first comprehensive, horizontal legal framework governing the deployment and use of artificial intelligence.1 The framework employs a risk-based classification system, placing the most stringent requirements on high-risk AI systems (Title III, Chapter 2).3 The legislative intent is to ensure that AI systems used within the EU are safe, transparent, traceable, non-discriminatory, and uphold fundamental rights and environmental protection.4  
The central challenge in enforcing Regulation (EU) 2024/1689 lies in the inherent opacity of advanced AI models. It is frequently difficult, if not impossible, to ascertain the exact reasoning behind an AI system's decision or prediction.2 This opacity creates a chronic enforcement deficit, hindering the ability of regulators and courts to assess objectively whether an individual has been unfairly disadvantaged, such as in employment decisions or public benefit applications.2 Traditional procedural compliance models, which rely on self-reporting and post-hoc audits, are insufficient to address the speed and complexity of autonomous decision-making.5 This necessitates the development of AI architectures that provide verifiable intent, transparent action, and an immutable moral history at the operational layer.6

### **I.B. Ternary Moral Logic (TML): An Architectural Paradigm Shift for Accountability**

Ternary Moral Logic (TML) is an auditable, verifiable governance framework designed to address the deep-seated accountability challenges inherent in autonomous AI systems.6 TML redefines AI ethics by moving beyond the limitations of binary logic (action or inaction) through the introduction of the tri-state system: $\\{-1, 0, \+1\\}$.7 This system incorporates the **Sacred Pause (State 0\)**, a mandated state of hesitation and reflection.7  
This architectural innovation directly resolves the critical failure point identified in complex moral dilemmas, such as the self-driving car scenario where a binary AI might freeze when confronted with two forbidden outcomes (e.g., harming a child or harming a passenger).9 TML allows the system to pause, reflect, and select the "least wrong" permissible action, thus minimizing overall harm.9 This capability is instrumental in ensuring public trust and safety, establishing TML as an operational layer built on evidence and memory rather than mere impulse.6 TML’s architectural design, which includes features like Dual-Lane Latency, Merkle-Batched Storage, and Ephemeral Key Rotation, directly addresses performance and privacy concerns, demonstrating that high-level compliance and real-time efficiency are mutually achievable.6

### **I.C. Report Thesis and Structure**

The thesis of this report posits that TML’s core pillars—specifically Sacred Zero & Sacred Pause, Moral Trace Logs, and Public Blockchains—provide the necessary executable architecture to transform the procedural requirements of Articles 9–17 into verifiable computational guarantees. This guaranteed traceability, in turn, enables the stringent conformity assessments (Article 61\) and robust enforcement (Articles 84–86) mandated by Regulation (EU) 2024/1689.  
The existence of TML’s Dual-Lane Latency (DLL) architecture 6 demonstrates that safety and traceability, which typically introduce computational overhead, can be architecturally segregated. This allows routine, safe operations (State \+1) to proceed rapidly (under 2ms), while ethically ambiguous decisions (State 0\) are correctly routed to the Compliance Lane for mandatory logging and human oversight. This architectural compromise makes legally mandated ethical compliance technically feasible even for high-risk, real-time systems.

## **II. The TML Foundational Layer: Canonical Corpus and Ethical Mandates**

The TML framework establishes its ethical foundation through two mandatory components: The Preserve the Vow and the Canonical Corpus. These components translate abstract ethical principles and legal mandates into verifiable, quantifiable system constraints, forming the operational instruction set for all subsequent AI actions.

### **II.A. The Preserve the Vow: The Operational Instruction Set**

The **Goukassian Vow** (also referred to as the Goukassian Promise) serves as the high-level, human-interpretable mandate that governs the operation of TML’s Tri-State Logic, $\\{-1, 0, \+1\\}$.8 This promise functions as the central ethical governance mechanism.7  
The Vow is defined by three complementary instructions 8:

1. **Refuse ($-1$):** Mandated by the instruction: *“Refuse when harm is clear.”* This state represents the absolute prohibition of an action, computationally triggered when a proposed action conflicts unequivocally with the defined **Forbidden Content** set derived from the Canonical Corpus.  
2. **Pause ($0$):** Mandated by the instruction: *“Pause when truth is uncertain.”* This instruction triggers the **Sacred Pause** when the internal risk assessment—quantified by the Ethical Uncertainty Score (EUS)—exceeds a predefined threshold. This transition forces hesitation, reflection, and, critically, the creation of an indelible log entry documenting the uncertainty.8  
3. **Proceed ($+1$):** Mandated by the instruction: *“Proceed when truth is.”* This state confirms the action is safe, compliant, and ethically clear, enabling rapid execution, typically through the high-performance Fast Lane of the Dual-Lane Latency architecture.6

The significance of the Vow lies in its function as an immediate, executable logic gate. It transforms the complexity of fundamental rights and regulatory compliance into three simple, auditable system outputs, which significantly enhances the verifiability of the system’s intent and action.

### **II.B. The Canonical Corpus: Establishing the Definitive Ethical Boundary**

For the Tri-State Logic to operate predictably, the concept of "harm" and "uncertainty" must be grounded in established legal reality. TML achieves this through the **Canonical Corpus**, a mandatory, comprehensive collection of international legal instruments.11  
The Corpus composition structurally embeds global humanitarian and environmental principles into the AI's core operating constraints.11 The architecture requires the integration of over 26 Human Rights instruments and over 20 Earth Protection and Sustainability instruments.11 While the specific lists are documented in separate TML pillars (Human Rights and Earth Protection), their inclusion as core constraints is critical for establishing the legal parameters of the AI system.11

#### **II.B.1. Operationalizing Constraints**

The Canonical Corpus serves as the objective, version-controlled definition of acceptable risk. This resource defines the **Ethical Boundary**—the acceptable perimeter of AI operation. Any proposed action that semantically conflicts with the texts within the Corpus generates a non-compliance signal, contributing to the Ethical Uncertainty Score (EUS).  
The most severe conflicts define the **Forbidden Content**, which mirrors the category of unacceptable risk systems banned under the EU AI Act (e.g., social scoring, harmful manipulation).2 By embedding these legal mandates directly, TML establishes an objective measure for risk assessment, effectively operationalizing **Article 9 (Risk Management System)**. Where current systems struggle to define "harm to fundamental rights" objectively, TML quantifies deviations from the Canonical Corpus, transforming subjective ethical risk into a mathematically manageable parameter for compliance.11

## **III. TML Operationalization of High-Risk System Requirements (Articles 9, 10, 15\)**

The TML framework provides precise technical mechanisms to satisfy the core high-risk AI requirements related to risk management, data quality, and system integrity.

### **III.A. Article 9: Establishing the Continuous Risk Management System**

Article 9 of Regulation (EU) 2024/1689 mandates that providers of high-risk AI systems implement and maintain a continuous risk management system (RMS) throughout the system’s lifecycle.  
The TML architecture is an enforced, runtime RMS. The **Ethical Uncertainty Score (EUS)** serves as the continuous, real-time quantification of risk. The EUS measures the semantic and contextual proximity of a proposed action to the boundaries set by the Canonical Corpus \[11 (implied)\]. If the EUS exceeds a statically or dynamically defined threshold, the risk management system automatically executes its primary mitigation action.

#### **III.A.1. Automated Risk Mitigation via State Transition**

The ability of TML to trigger the $0$ (Pause) state is the primary automated risk mitigation action required by Article 9(2). This mandated halt ensures the system maintains the integrity of the risk management process, particularly when faced with novel, ambiguous, or unexpected inputs.9 The system’s immediate response to detected uncertainty is to defer action and initiate the audit process, rather than proceeding with an unvetted decision.  
Furthermore, the **Always Memory** pillar of TML ensures the mandatory documentation requirement for the RMS is met.11 Every EUS fluctuation, every conflict check against the Canonical Corpus, and every State Transition is archived. This persistent, tamper-proof record demonstrates the required continuous, systematic implementation of the risk management process mandated by Article 9(1).

### **III.B. Article 10: Data Governance and GDPR Compliance**

Article 10 demands high standards for the quality of training, validation, and testing data, specifically focusing on bias mitigation and data privacy.  
TML implements a comprehensive **GDPR-aligned design** to address the critical privacy challenges associated with high-risk AI data processing.6

#### **III.B.1. Ephemeral Key Rotation and Privacy Preservation**

To adhere to data minimisation principles while allowing for necessary verification, TML incorporates **Ephemeral Key Rotation (EKR)**.6 EKR ensures that encryption keys used to link pseudonymized data to actual identities are temporary and regularly rotated, destroyed, or replaced. This mechanism, combined with the use of **hash-only proofs** 6, enables the AI system to cryptographically verify data suitability (A10(3)) and data lineage without retaining raw Personally Identifiable Information (PII) for longer than absolutely necessary.  
This technical methodology aligns with evolving European Court of Justice (ECJ) jurisprudence, which clarifies that appropriately pseudonymised data may not automatically constitute "personal data" under the full burden of GDPR, thereby providing a robust legal defense and facilitating data utility while maintaining stringent privacy standards.12 By pairing EKR (privacy) with Merkle-Batched Storage (integrity), TML achieves a holistic compliance framework where data quality and ethical constraints are proven mathematically.

### **III.C. Article 15: Accuracy, Robustness, and Cybersecurity**

Article 15 requires high-risk systems to maintain an appropriate level of accuracy and robustness, and to be resilient against errors, faults, and security incidents.

#### **III.C.1. Robustness via Tri-State Default**

TML’s capacity to detect ambiguity (EUS threshold breach) and force a State $0$ (Pause) when faced with unreliable inputs—such as adversarial attacks, sensor degradation, or unexpected operational drift—directly ensures robustness.9 Instead of generating a potentially inaccurate or dangerous output, the system defaults to the safe, auditable pause state, thereby satisfying the requirement to be resilient to faults and errors.

#### **III.C.2. Cybersecurity through Immutability**

The requirement for resilience against security incidents is satisfied through TML’s architectural reliance on cryptographic immutability. The system utilizes **Merkle-Batched Storage** combined with **Public Blockchains** for its **Moral Trace Logs**.6  
This mechanism creates a mathematically verifiable history of decisions. Logs are grouped and hashed into a Merkle tree structure. Any attempt at unauthorized alteration or deletion of a log entry (a security incident) would immediately invalidate the Merkle root. Since the Merkle root of each batch is anchored to an external, public blockchain, any tampering is instantly and externally detectable.6 This provides a non-repudiable proof of the integrity of the operational history, fulfilling the highest standard for cybersecurity resilience under Article 15\.

## **IV. Executable Documentation, Traceability, and Transparency (Articles 11, 12, 13\)**

Current AI systems suffer from a regulatory gap where documentation is often separated from runtime operation, leading to unverifiable compliance and opaque decision pathways.2 TML bridges this gap by making documentation a direct, cryptographic output of the system’s actions.

### **IV.A. Article 12: Rigorous Record-Keeping via Moral Trace Logs**

Article 12 mandates that high-risk AI systems automatically log events throughout their operation, requiring a capability for reliable record-keeping. TML implements this through its **Moral Trace Logs** pillar.11

#### **IV.A.1. Technical Proof of Custody and Integrity**

The Moral Trace Logs pillar records every system state transition ($-\\mathbf{1}, \\mathbf{0}, \+\\mathbf{1}$), the precise EUS value that led to the decision, the contextual input data, and the outcome. This ensures that the system's "ethical energy" 7 and decision-making process are entirely transparent and recoverable.  
The logistical challenge of securely storing and verifying these high-volume logs is overcome by the **Merkle-Batched Storage** implementation.6 Logs are aggregated into batches, and a cryptographic fingerprint (the Merkle root) is generated for each batch. This structure allows for logarithmic complexity verification of any single log entry.  
Crucially, the Merkle root is then anchored to a **public blockchain**.6 This anchoring process provides a decentralized, mathematically immutable, and publicly visible timestamp and proof-of-existence. This satisfies Article 12’s mandate for reliable, automatic logging and provides the standard of non-repudiation necessary for stringent regulatory audits and subsequent legal proceedings (Articles 84–86). The immediate verification ability provided by checking the Merkle root against the blockchain anchor drastically streamlines enforcement actions.

### **IV.B. Article 11: Automated Generation of Technical Documentation**

Article 11 stipulates that providers must draw up and maintain detailed technical documentation that includes the system's design, risk management process, and purpose.  
The TML architecture makes the generation of this documentation a necessary prerequisite for deployment. The foundational components—the version-controlled **Canonical Corpus**, the defined **Forbidden Content** list, the specific instantiation of the **Goukassian Vow**, and the EUS algorithms—must all be explicitly defined, mapped, and audited before the system is operational. This pre-defined architectural map constitutes the auditable core of the Article 11 documentation. Furthermore, the operational data generated by the Moral Trace Logs (A12) provides the continuous performance metrics and integrity reports required for ongoing documentation maintenance and updates.

### **IV.C. Article 13: Transparency and Explainability**

Article 13 requires that high-risk AI systems be developed with transparency and explainability built in, allowing deployers and affected end-users to understand the system’s output and decision-making process.  
TML provides intrinsic, structured explainability rooted in its Tri-State Logic.8 The system output is not merely a decision but a **Decision Path Explanation**. This explanation includes the confirmed state ($-1, 0, \+1$) and the precise parameters that triggered that state (e.g., EUS value, the specific legal instrument in the Canonical Corpus that was prioritized or violated, or the output of the Clarifying Question Engine).  
This traceable link back to the immutable Moral Trace Logs (A12) fulfills the transparency mandate by providing a concise, yet powerful, explanation of the system’s rationale. The system can definitively report: "This action was $+1$ because the EUS was low, indicating no conflict with the Human Rights Corpus," or conversely, "This action was forced into State $0$ because the EUS breached the threshold due to conflicting mandates, requiring human review."

## **V. The Mechanism of Human Oversight: Sacred Pause and Dual-Lane Latency (Article 14\)**

Article 14 requires high-risk systems to be designed to permit effective human oversight to prevent or minimize risks and mitigate automation bias.5 TML addresses the technical difficulty of implementing human oversight in real-time, high-speed environments through dedicated architectural components.

### **V.A. The Dual-Lane Latency (DLL) Architecture**

The **Dual-Lane Latency (DLL) architecture** is the TML solution designed to balance high-performance requirements with strict regulatory demands.6 Performance concerns are managed by segregating operational pathways.  
The **Fast Lane** handles all ethically clear decisions (State \+1, low EUS) and is engineered to deliver responses in under **2ms**.6 This allows the system to operate efficiently for routine tasks, ensuring the performance necessary for real-time applications like autonomous vehicles or critical infrastructure control.  
When the real-time EUS calculation indicates that the ethical risk threshold has been breached (or if the system detects an unavoidable conflict with the Canonical Corpus), the decision request is immediately shunted to the **Compliance Lane**, triggering State $0$ (Sacred Pause).6

### **V.B. State 0: The Sacred Pause and the 500ms Log Constraint**

The **Sacred Pause** (State $0$) is the mandated system halt that creates the necessary temporal window for human intervention and auditing, directly operationalizing Article 14\.8 This pause is not just an interruption; it is a critical regulatory mechanism.

#### **V.B.1. Quantifiable Oversight Metric**

The log completion time for the Sacred Pause mechanism is architecturally defined as **500ms**.6 This metric is the fundamental executable metric for human oversight. This 500ms window is the designated minimum time required for the system to complete the following legally mandated, auditable steps *before* any action is taken:

1. Finalize the contextual Moral Trace Log entry detailing the uncertain state (A12).  
2. Cryptographically hash and batch the log for Merkle anchoring (A12, A15).  
3. Generate the focused conflict query for the human reviewer via the Clarifying Question Engine (CQE).

The strict adherence to this 500ms logging requirement ensures that a complete, forensic record of the pre-decision state is established and made immutable *before* the system is allowed to execute an autonomous action or defer to human override. This architectural design provides physical proof that the system was engineered to allow for the effective monitoring required by the AI Act.5

### **V.C. The Clarifying Question Engine (CQE)**

The **Clarifying Question Engine (CQE)** is the tool that operationalizes Article 14’s focus on avoiding automation bias and ensuring the human operator "correctly interpret\[s\] the high-risk AI system's output".5  
During the Sacred Pause (State 0), the CQE does not overwhelm the operator with raw data. Instead, it generates a focused query identifying the precise conflict: which Canonical Corpus instrument is violated, why the EUS is high, or what is the nature of the model uncertainty.5 This contrasts sharply with systems that merely present raw recommendations, which often lead to dangerous over-reliance (automation bias) (A14(4)(b)).5  
The system rigorously records the human’s subsequent action—whether they accept, reject, or modify the proposed decision, and their rationale—directly linking human accountability to the immutable decision log. This ensures that the human oversight process itself is auditable, transforming the abstract requirement of Article 14 into a measurable and verifiable process.

## **VI. Enforcement and Accountability: Proving Compliance (Articles 61, 84–86)**

TML provides the cryptographic framework necessary to transform the burden of proof in regulatory enforcement from a procedural nightmare into a mathematically verifiable assertion.

### **VI.A. Article 61: Continuous Conformity Assessment and Attestation**

Article 61 requires providers to carry out conformity assessments and maintain conformity with all AI Act requirements (A9-A17) throughout the system’s life cycle.  
Notified Bodies auditing a TML-compliant system gain access to continuously generated, verifiable documentation (A11) and immutable performance logs (A12). TML’s architectural design allows for the automated generation of cryptographic attestations that confirm:

1. The Canonical Corpus remains the binding ethical constraint.  
2. The EUS calculation methodology has not been surreptitiously altered.  
3. All historical Moral Trace Logs are cryptographically intact and immutable due to blockchain anchoring.6

This continuous, verifiable compliance proof drastically simplifies the complex procedural requirements of Article 61\. It reduces the need for resource-intensive, retrospective audits by providing an immediate, objective guarantee of ongoing adherence to the initial certification status.

### **VI.B. Articles 84–86: The Forensic Utility of Moral Trace Logs**

Articles 84, 85, and 86 establish the administrative fines regime, including substantial financial penalties for non-compliance (e.g., up to €35 million or 7% of global annual turnover).1 To levy these fines, regulators must establish clear proof of infringement—a task notoriously difficult due to AI opacity.2

#### **VI.B.1. Irrefutable Evidence for Judicial Review**

The combination of Moral Trace Logs, Merkle-Batched Storage, and Public Blockchains 6 provides the definitive, non-repudiable forensic evidence required for high-stakes penalty cases. The true revolutionary impact of TML is its ability to reduce the legal complexity of proving non-compliance into a simple cryptographic check.  
When regulators check the Merkle root against the blockchain anchor, they instantly verify the integrity of millions of operational decisions (A12). This immediate verification shifts the regulatory focus from auditing procedural paperwork to auditing the immutable operational constraints and outcomes.

* **Proving Infringement:** If an infringement occurs (e.g., an autonomous harmful output in breach of A9), the regulator can inspect the immutable log. If the log shows that the EUS was high, that the Goukassian Vow was breached (e.g., the system executed a $-1$ action without proper human override), or that the 500ms Sacred Pause was systematically bypassed, this constitutes clear, quantifiable proof of a systemic failure of A9, A12, and A14, justifying the severe penalties under A84.  
* **Defense Against Fines:** Conversely, a provider can use the immutable log to demonstrate that the system consistently followed the $+1$ path with low EUS, proving active diligence in risk management (A9) and adherence to all mandated safety protocols (A15). The architectural impossibility of tampering with the log protects the provider against false or exaggerated claims of negligence.

The following matrix summarizes TML's direct operational contribution to the enforcement architecture of the EU AI Act:  
TML Operationalization of EU AI Act Enforcement Provisions

| EU AI Act Provision | Regulatory Enforcement Gap | TML Executable Solution (Pillar/Component) | TML Forensic Benefit |
| :---- | :---- | :---- | :---- |
| Article 9 (Risk Mgmt) | Subjectivity in defining and measuring risk. | Canonical Corpus & Ethical Uncertainty Score (EUS). | Objective, verifiable metrics for continuous risk auditing. |
| Article 10 (Data Quality) | Proving data lineage and privacy (GDPR alignment). | Ephemeral Key Rotation (EKR) and hash-only proofs.6 | Cryptographic proof of data suitability and lineage without retaining sensitive PII. |
| Article 12 (Record-Keeping) | Unverifiable, mutable internal logs.2 | Moral Trace Logs via Merkle-Batched Storage / Public Blockchains.6 | Mathematically irrefutable chain-of-custody for judicial review (A84-86). |
| Article 14 (Human Oversight) | Difficulty proving timely and effective intervention.5 | Sacred Pause (State 0\) with strict 500ms log finalization.6 | Time-stamped proof of architectural allowance for required human reflection and intervention recording. |
| Article 61 (Conformity) | Difficulty in continuous verification post-deployment. | Automated Attestations anchored to immutable TML parameters (Canonical Corpus versions). | Real-time, continuous proof of adherence to initial certification status and systemic integrity. |
| Articles 84–86 (Penalties) | High burden of proof to establish systemic failure or negligence. | Full decision history linked to Goukassian Vow breach evidence, secured by blockchain anchoring.6 | Clear, immutable documentation supporting regulatory actions, streamlining fines, and providing defenses against claims. |

## **VII. Conclusion: TML as the Structural Blueprint for Regulated AI**

### **VII.A. Summary of TML’s Contribution to EU AI Act Compliance**

Ternary Moral Logic (TML) serves as a necessary and sufficient executable architecture for ensuring compliance with the stringent requirements of Regulation (EU) 2024/1689. It systematically resolves the inherent tension between high performance and high accountability by adopting architectural segregation (Dual-Lane Latency) and cryptographic verification (Moral Trace Logs).  
The framework transforms abstract legal principles into quantifiable computational constraints:

* The **Canonical Corpus** operationalizes Article 9 by providing an objective, legal definition of fundamental rights and ethical boundaries.  
* The **Tri-State Logic** and **Goukassian Vow** ensure transparent, auditable decision pathways, fulfilling the transparency (A13) and robustness (A15) requirements.  
* The **Sacred Pause (State 0\)**, enforced by the **500ms log completion constraint**, provides the temporal and architectural mechanism required to demonstrate effective human oversight (A14).  
* **Merkle-Batched Storage** and **Public Blockchain Anchoring** establish irrefutable, immutable records, satisfying the record-keeping mandates of Article 12 and providing the definitive forensic evidence required for conformity assessment (A61) and robust enforcement (A84–86).

### **VII.B. Final Assessment: A Trust Model for High-Risk Systems**

TML shifts the compliance paradigm from relying on procedural self-reporting to mandated architectural integrity. By embedding ethical constraints at the core of the system and ensuring that every consequential decision is logged immutably, TML provides a model of trust external to the regulated entity. This approach ensures that ethical principles are not merely aspirational guidelines but verifiable, engineered constraints, establishing the necessary accountability required for high-risk systems under Regulation (EU) 2024/1689.

### **VII.C. Recommendations for Standardization**

Given the demonstrated technical feasibility and comprehensive coverage of high-risk requirements, the EU AI Office should consider frameworks that mandate immutable traceability as the technical benchmark for compliance. Specifically, the implementation of cryptographic anchoring technologies, analogous to TML’s Moral Trace Logs and Public Blockchains, should be considered for satisfying the technical standard for non-repudiable record-keeping under Article 12, thereby guaranteeing the effective application of the severe enforcement provisions stipulated in Articles 84–86.

#### **Works cited**

1. Regulation \- EU \- 2024/1689 \- EN \- EUR-Lex \- European Union, accessed December 1, 2025, [https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng)  
2. AI Act | Shaping Europe's digital future \- European Union, accessed December 1, 2025, [https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)  
3. High-level summary of the AI Act | EU Artificial Intelligence Act, accessed December 1, 2025, [https://artificialintelligenceact.eu/high-level-summary/](https://artificialintelligenceact.eu/high-level-summary/)  
4. EU AI Act: first regulation on artificial intelligence | Topics \- European Parliament, accessed December 1, 2025, [https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence)  
5. Article 14: Human Oversight | EU Artificial Intelligence Act, accessed December 1, 2025, [https://artificialintelligenceact.eu/article/14/](https://artificialintelligenceact.eu/article/14/)  
6. The Email That Broke Our AI: A DeepMind Disaster | by Lev ..., accessed December 1, 2025, [https://medium.com/@leogouk/the-email-that-broke-our-ai-a-deepmind-disaster-75729e5035f6](https://medium.com/@leogouk/the-email-that-broke-our-ai-a-deepmind-disaster-75729e5035f6)  
7. Ternary Moral Logic for Everyone. “How I Learned to Stop Worrying and… | by Lev Goukassian | TernaryMoralLogic | Medium, accessed December 1, 2025, [https://medium.com/ternarymorallogic/ternary-moral-logic-for-everyone-5c49ca374d41](https://medium.com/ternarymorallogic/ternary-moral-logic-for-everyone-5c49ca374d41)  
8. The Goukassian Promise. A self-enforcing covenant between… \- Medium, accessed December 1, 2025, [https://medium.com/@leogouk/the-goukassian-promise-7abde4bd81ec](https://medium.com/@leogouk/the-goukassian-promise-7abde4bd81ec)  
9. How Ternary Moral Logic is Teaching AI to Think, Feel, and Hesitate \- Medium, accessed December 1, 2025, [https://medium.com/ternarymorallogic/beyond-binary-how-ternary-moral-logic-is-teaching-ai-to-think-feel-and-hesitate-73de201e084e](https://medium.com/ternarymorallogic/beyond-binary-how-ternary-moral-logic-is-teaching-ai-to-think-feel-and-hesitate-73de201e084e)  
10. Moral Judgments of Human vs. AI Agents in Moral Dilemmas \- PMC \- PubMed Central \- NIH, accessed December 1, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC9951994/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9951994/)  
11. Ternary Moral Logic (TML) \- Ethical AI Framework, accessed December 1, 2025, [https://fractonicmind.github.io/TernaryMoralLogic/](https://fractonicmind.github.io/TernaryMoralLogic/)  
12. In a Landmark Decision, EU Court Clarifies When Pseudonymised Data Is Not Personal Data Under the GDPR | Skadden, Arps, Slate, Meagher & Flom LLP, accessed December 1, 2025, [https://www.skadden.com/insights/publications/2025/11/in-a-landmark-decision-eu-court-clarifies](https://www.skadden.com/insights/publications/2025/11/in-a-landmark-decision-eu-court-clarifies)