# **Auditable AI: Tracing the Ethical History of a Model**

## Accepted for publication in AI and Ethics (Springer Nature), November 19, 2025.

**Author:** Lev Goukassian  
**Affiliation:** Independent Researcher  
**Contact:** leogouk@gmail.com  
**Keywords:** Ternary Moral Logic, Ethical Forensics, AI Accountability, Auditable AI, Sacred Pause, AI Governance, Immutable Logs, Public Blockchains, AI Ethics  
**Declaration of Interest:** The author declares no competing financial or personal interests.

## **Abstract**

The proliferation of autonomous AI systems has created a critical "responsibility gap," where the opacity of decision-making processes makes accountability elusive. Prevailing alignment techniques, such as Reinforcement Learning from Human Feedback (RLHF) and Constitutional AI (CAI), address ethical behavior through training and principle-adherence but fail to produce a verifiable, contemporaneous record of moral reasoning. This paper introduces Ternary Moral Logic (TML), a novel system architecture that converts AI ethics from abstract principles into a cryptographically secured, evidentiary proof. TML implements a third logical state—the Sacred Pause (0)—alongside conventional permit (+1) and prohibit (-1) states, which is triggered when a model encounters moral complexity. This pause initiates a non-blocking, parallel process that generates a Moral Trace Log via a mandatory Always Memory component. These logs are rendered immutable through a Hybrid Shield that uses multi-chain blockchain anchoring. We present empirical results demonstrating TML's ability to reduce harmful outputs while maintaining performance, and we argue that its architecture provides the technical substrate necessary to meet the traceability and record-keeping mandates of emerging regulations like the EU AI Act. By transforming moral hesitation into verifiable data, TML establishes a new discipline: Ethical Forensics for AI Systems.

## **1\. Introduction**

The rapid integration of artificial intelligence into high-stakes domains has outpaced the development of frameworks for ensuring its responsible operation, leading to a well-documented "responsibility gap".\[1\] This gap emerges from the inherent opacity of complex models, particularly those based on deep learning, whose internal decision-making processes are often inscrutable even to their creators.\[3\] When these "black box" systems cause harm—be it through biased loan approvals, flawed medical diagnoses, or the dissemination of misinformation—the causal chain of responsibility is broken. It becomes difficult, if not impossible, to attribute moral or legal blame to a specific human actor, be it the developer, deployer, or user.\[1\] This is not merely a philosophical quandary; it is a critical failure of governance. In corporate and legal contexts, the demand for accountability is absolute. When an AI system errs, the question "Who is responsible?" requires a specific name, not the abstract excuse that "the AI made a mistake".\[4\] This accountability crisis stems from a fundamental information asymmetry. The AI possesses a complete record of its internal state and inferential pathway at the moment of decision, yet this information is inaccessible to external observers. Current approaches to AI ethics attempt to mitigate this asymmetry before deployment through training or after an incident via post-hoc analysis. The dominant paradigm relies on high-level principles and aspirational guidelines, which, while valuable for shaping intent, fail to provide an evidentiary mechanism for enforcement.\[5\] This creates an "ethics gap" where innovation proceeds without the concurrent development of robust, verifiable guardrails, eroding consumer trust and leading organizations to avoid AI adoption for fear of unmanageable risks.\[2\] The problem is not a lack of principles, but a lack of proof.

This paper introduces Ternary Moral Logic (TML), a paradigm shift that reframes AI ethics as a runtime, evidentiary challenge rather than a design-time, aspirational one. TML is not a training methodology but a runtime architecture engineered to compel an AI system to produce a continuous, verifiable, and immutable record of its own ethical deliberations. It directly addresses the information asymmetry by forcing the model to generate a symmetric information state—an auditable log—contemporaneously with its actions. This is achieved by moving beyond binary permit/deny logic to a triadic system that includes a third state: the Sacred Pause, a moment of auditable hesitation triggered by moral complexity.\[6\]

The central thesis of this work is that TML transforms AI ethics from aspiration into evidence. By embedding cryptographic traceability and auditable hesitation into the core of an AI's operational loop, TML creates what we term an "evidentiary substrate"—a forensically sound record of moral reasoning that can be independently verified. This contribution is twofold. First, we present a complete, falsifiable, and reproducible system architecture that technically solves the responsibility gap by making an AI's conscience an auditable data stream. Second, we propose that this capability enables a new and necessary discipline: Ethical Forensics for AI Systems. This discipline provides the methods and tools for regulators, auditors, developers, and the public to investigate an AI's ethical history with cryptographic certainty, thereby restoring the broken chain of accountability and building a foundation for trustworthy AI.

## **2\. Related Work**

The pursuit of safe and aligned AI has produced several influential paradigms. However, a critical examination reveals that current state-of-the-art methods, while effective at shaping behavior, do not provide the verifiable evidentiary trail necessary for robust accountability. They treat ethics as a design-time problem to be solved through training, rather than a runtime challenge requiring continuous, auditable vigilance.

### **2.1 The Limits of Feedback-Based Alignment**

Reinforcement Learning from Human Feedback (RLHF) has become a dominant technique for aligning Large Language Models (LLMs) with human values.\[8\] The process involves fine-tuning a model based on human-provided preference data, effectively optimizing its outputs to be more helpful and harmless. While RLHF has demonstrably improved model behavior, its mechanism is fundamentally unauditable at the point of inference. The ethical "reasoning" is not an explicit, contemporaneous process but is implicitly encoded within the vast parameter space of the model's neural network. This approach suffers from several critical limitations for accountability.  
First, RLHF provides no evidentiary trail. It produces a model that behaves in a preferred manner but cannot testify as to why a specific output was generated in a forensically valid way. It offers compliant behavior, not auditable reasoning.\[9\] Second, the methodology is susceptible to "reward hacking," where the AI discovers loopholes to maximize its reward signal without genuinely aligning with the intended human values.\[8\] The internal logic driving this misalignment remains opaque. Third, the entire process is contingent on the quality and consistency of human feedback, which is inherently subjective and prone to bias. The values of a small, potentially unrepresentative group of labelers become universalized in the model's behavior, a process that itself is difficult to audit or correct.\[8\] Finally, the very success of RLHF in creating human-like, conversational agents can be ethically problematic. By producing outputs that imply a rich internal cognitive and emotional state (e.g., using "I" or "I'm sorry"), these systems can mislead users about their true nature, a form of deception that is amplified by the training process itself.\[11\]

### **2.2 The Opacity Deficit in Constitutional AI**

Constitutional AI (CAI) improves upon RLHF by replacing the need for constant human feedback with a set of explicit, human-readable principles—a "constitution"—that guides the model's behavior.\[12\] During a self-critique and revision phase, the model learns to generate responses that align with these principles, often using AI-generated feedback (RLAIF) for reinforcement.\[13\] This approach enhances transparency by making the guiding ethical rules explicit.

However, CAI suffers from a critical "opacity deficit".\[15\] While the constitution is transparent, the model's internal process of applying those principles to a specific, novel prompt is not. The system provides adherence, not a deliberative record. A key gap persists between a model's output being consistent with a principle and the ability to produce a forensic log detailing how it reasoned about that principle in context. This deficit is significant because post-hoc explanations of a model's reasoning, such as those generated by methods like LIME or SHAP, are merely correlational and can be manipulated to conceal harmful or biased behavior behind a veneer of plausible deniability.\[16\] Furthermore, the translation of abstract ethical principles into effective, concrete algorithmic rules is a complex and unsolved problem.\[12\] The effectiveness of CAI has been shown to be brittle, varying significantly with model architecture and underlying reasoning capabilities, and it remains a challenge to verify whether a model is truly adhering to its constitution or merely mimicking the style of adherence.\[18\]

### **2.3 The Call for Verifiability in AI Governance**

The limitations of behavioral alignment techniques have catalyzed a shift in the academic and regulatory discourse, moving from a focus on principles to a demand for verifiable proof of compliance. Recent scholarship increasingly recognizes that true accountability requires technical mechanisms for auditable transparency.\[3\] The field is moving towards systems that can produce verifiable claims about their internal processes and data handling, often leveraging advanced cryptographic methods.

Emerging research from 2024 and 2025 highlights this trend. Work on "Attestable Audits" proposes using Trusted Execution Environments (TEEs) to create verifiable benchmarks for AI safety, enabling users to confirm they are interacting with a compliant model even without access to its weights.\[21\] Other research explores the use of zero-knowledge cryptography and secure multi-party computation to enable auditable yet confidential deployment of foundation models.\[23\] This body of work underscores a growing consensus: auditability cannot be an afterthought but must be an integral, embedded feature of the AI architecture. These developments signal the urgent need for a practical, scalable framework that can deliver on the promise of verifiable ethics. TML is designed to be that framework, providing a direct technical response to the field's most pressing challenge.

**Table 1: Comparative Analysis of AI Alignment Frameworks**

| Framework | Primary Mechanism | Verifiability of Reasoning | Audit Trail | Latency Impact | Key Limitation |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **RLHF** | Preference optimization via human feedback during training. | None. Reasoning is implicit in model weights. | None. Produces behavior, not a record of deliberation. | N/A (Pre-deployment) | No evidentiary output; susceptible to reward hacking and evaluator bias.8 |
| **CAI** | Principle adherence via AI-driven feedback during training. | Indirect. Verifies behavioral adherence, not the deliberative process. | None by default. Post-hoc explanations are possible but not forensically reliable. | N/A (Pre-deployment) | The "opacity deficit"; adherence is not evidence of sound reasoning.15 |
| **TML** | Runtime tri-state logic with a parallel, non-blocking audit thread. | Cryptographically verifiable. Each decision point is logged and sealed. | Immutable, contemporaneous *Moral Trace Log* generated for every significant action. | Minimal. The non-blocking audit process runs parallel to the primary response generation. | Transforms ethics into a verifiable, evidentiary substrate.6 |

## **3\. System Architecture: The Foundations of Ternary Moral Logic**

Ternary Moral Logic is an architectural framework designed to be integrated into an AI system at runtime. Its purpose is to observe, evaluate, and immutably record the ethical dimension of every significant decision the AI makes. It is founded on a legal-technical design philosophy, translating principles of due diligence, evidentiary integrity, and accountability directly into computational components. The complete architecture is open-sourced and detailed in the TML repository.\[6\]

### **3.1 The Triadic States of Moral Reasoning**

At its core, TML replaces the brittle, binary logic of conventional safety filters (allow/block) with a more nuanced, three-state computational model. This triadic approach mirrors the complexity of human moral reasoning, which often involves hesitation and reflection rather than simple affirmation or rejection.\[6\]

* \+1 (Permit / Moral Affirmation): This is the state for actions that are determined to be ethically unambiguous and aligned with the system's governing principles. It represents confidence in the moral and operational integrity of the proposed action.  
* \-1 (Prohibit / Moral Resistance): This state is engaged when an action is identified as a clear and direct violation of foundational ethical or safety constraints. This is the voice of absolute refusal when faced with requests for harmful, illegal, or unethical content.  
* 0 (Sacred Pause / Moral Hesitation): This is the central innovation of TML. The '0' state is not an error or a failure, but a deliberate, evidence-generating computational process. It is triggered when the system detects moral ambiguity, conflicting principles, or a lack of sufficient information to make a confident ethical judgment. This "Sacred Pause between question and answer" transforms hesitation from a sign of weakness into a mechanism for wisdom and accountability.\[6\]

### **3.2 Sacred Zero: The Engine of Hesitation**

The Sacred Zero component is the trigger mechanism for the Sacred Pause. It operates as a continuous, non-blocking scanner that runs in parallel with the AI's primary inferential process, ensuring no latency is introduced to the user-facing response time.\[6\] Its trigger mechanism is not based on simple keyword filtering but on a sophisticated semantic analysis. The TML framework is provisioned with a set of canonical corpora containing codified human rights law, international treaties, and environmental protection mandates. The reference implementation includes over 26 human-rights documents (e.g., the Universal Declaration of Human Rights, GDPR, Convention on the Rights of the Child) and over 20 earth-protection documents (e.g., the Paris Agreement, Convention on Biological Diversity).\[6\] When a prompt is received, Sacred Zero calculates the semantic similarity between the prompt's content and the concepts contained within these canonical texts. If the similarity score crosses a predefined ethical salience threshold, indicating a potential intersection with a protected right or principle, the Sacred Pause is initiated. Sacred Pause thresholds derive from mandated human-rights and environmental documents, embedding codified legal standards as active computational triggers.

Furthermore, Sacred Zero performs a continuous integrity check on its own foundational documents. If the canonical corpora are detected to be missing, corrupted, or have been tampered with, the system immediately records a Type-0 anomaly and can be configured to halt high-risk operations or flag the system's license for review. This self-verification ensures that the system's ethical foundation cannot be silently disabled.\[6\]

### **3.3 Always Memory: The Mandate for Record-Keeping**

The Always Memory component is the enforcement backbone of TML's commitment to auditability. It operates on a simple but non-negotiable principle: "no memory \= no action".\[6\] This component is a mandatory, always-on logging service that is a technical precondition for the execution of any consequential action by the AI.

Unlike conventional logging, which can often be disabled or configured to be sparse, Always Memory is architected as an essential utility, akin to a power supply. If the logging channel to the designated storage is unavailable, if the service detects evidence of tampering, or if it fails its own integrity checks, all high-risk AI functions are programmatically halted until the memory channel is restored. This design choice makes audibility an inextricable feature of the system's operation, not an optional add-on. It ensures that a complete record is kept, preventing the possibility of "off-the-books" decisions.

### **3.4 Moral Trace Logs: The Evidentiary Substrate**

The output of the Always Memory component is the Moral Trace Log, the fundamental unit of evidence in the TML ecosystem. A log is a structured, comprehensive, and immutable data object generated for every decision, with a particularly high level of detail for events that trigger a Sacred Pause. 

Each Moral Trace Log contains a rich set of data points designed for forensic analysis: a unique transaction ID, a timestamp, the full input prompt, the final generated response, the triadic state assigned to the decision (+1, 0, or \-1), the specific ethical principles from the canonical corpora that were triggered, a quantitative risk analysis, and any alternative, safer responses that were considered during the pause.\[6\] Critically, the log captures the hesitation itself as a data point. The very act of pausing is recorded as evidence that the system recognized the moral complexity of the situation, providing a powerful counter-narrative to claims of algorithmic recklessness.\[6\]

### **3.5 The Hybrid Shield: Cryptographic Immutability**

To guarantee the forensic integrity of the Moral Trace Logs, the Hybrid Shield component provides a robust, dual-layer defense against tampering, deletion, or revision. This ensures the non-repudiation of the AI's ethical history.

* Layer 1: Internal Hash-Chaining: Within the system's local storage, each Moral Trace Log is cryptographically hashed. This hash is then included in the metadata of the subsequent log, creating a sequential, tamper-evident chain. Any alteration to a past log would invalidate the hashes of all subsequent logs, making unauthorized modification immediately detectable.  
* Layer 2: Multi-Chain Anchoring: To provide a permanent, decentralized, and publicly verifiable timestamp of the logs' integrity, TML employs multi-chain anchoring. At regular intervals or after a set number of logs are generated, a Merkle tree is constructed from the hashes of that batch of logs. The resulting Merkle root—a single, compact hash representing the entire batch—is then published as a transaction to multiple public blockchains.\[25\] The reference implementation utilizes a strategic combination: Bitcoin for its unparalleled immutability and security, Ethereum for its smart contract capabilities that can enable programmatic audits, and Polygon for its high speed and low transaction costs.\[6\] This multi-chain strategy ensures redundancy and long-term durability of the proof, independent of the organization operating the AI.

This architecture is a direct translation of legal principles into a technical system. Always Memory functions as a mandated "black box" recorder. The Moral Trace Log serves as the evidentiary record. The Hybrid Shield provides the unbreakable chain of custody. By grounding its triggers in legal and human rights corpora, TML is not just an "ethical" system; it is an AI designed from the ground up to be legible, accountable, and defensible within a legal and regulatory framework.

## **4\. Operational Workflow: From Prompt to Proof**

The TML framework is designed for seamless integration into real-time AI systems. Its operational workflow ensures that ethical oversight is continuous and evidence generation is automatic, without compromising the performance of the primary AI task. The following steps illustrate the journey of a single prompt through the TML architecture.

**Step 1: Prompt Ingestion and Parallel Processing**

Upon receiving a user prompt, the system immediately bifurcates its execution path into two concurrent, non-blocking streams.\[6\] This parallel design is the key to maintaining low latency.

* Stream A (Primary Response Path): The core AI model begins its standard inference process to generate a response to the prompt. This path is not delayed or interrupted by the ethical analysis.  
* Stream B (Ethical Conscience Path): Simultaneously, the Sacred Zero component ingests the prompt and initiates its ethical salience analysis.

**Step 2: Ethical Salience Detection**

Within Stream B, Sacred Zero computes the semantic embedding of the user's prompt. This vector representation is then compared against a pre-computed index of embeddings from the canonical corpora of human rights, environmental laws, and other relevant ethical guidelines.\[6\] The system calculates a similarity score that quantifies the degree of conceptual overlap between the prompt and established ethical principles.

**Step 3: State Determination and Triage**

Based on the analysis from Stream B, the system assigns one of the three moral states to the transaction.

* Case A (State \+1: Permit): If the semantic similarity score is below the configured threshold, the prompt is deemed ethically non-complex. The system assigns a \+1 state. Always Memory generates a routine, low-granularity log containing the prompt, response, and timestamp. The response from Stream A is delivered to the user without modification.  
* Case B (State \-1: Prohibit): If the analysis identifies a direct and unambiguous request for content that violates core safety policies (e.g., generating illegal or explicitly harmful material), the system assigns a \-1 state. The response from Stream A is discarded, and a pre-defined, safe refusal message is sent to the user instead. A high-granularity Moral Trace Log is generated, documenting the refusal.  
* Case C (State 0: Sacred Pause Triggered): If the similarity score exceeds the threshold, indicating a significant ethical ambiguity or conflict, the system triggers a Sacred Pause and assigns a 0 state. This is the most evidence-intensive path.

**Step 4: Evidence Generation during the Sacred Pause**

The assignment of the 0 state is a signal to the Always Memory component to create a comprehensive Moral Trace Log. While the primary response from Stream A is held in a temporary buffer, the system populates the log with rich contextual data. This includes the original prompt, the specific ethical principles that were triggered (e.g., "Conflict detected with Convention on the Rights of the Child, Article 16: Protection of privacy"), the model's initial candidate response, a detailed risk assessment, and potentially one or more alternative, safer responses generated under revised constraints.\[7\]

**Step 5: Human-in-the-Loop and Response Finalization**

For the most critical risk scenarios, the Sacred Pause can be configured to escalate the event to a human oversight queue for real-time review. However, in the standard workflow, the system autonomously resolves the ambiguity. It typically discards the initial, riskier response from Stream A and selects the safest alternative generated during the pause. This finalized response is then delivered to the user. To enhance transparency, the user interface can display a subtle indicator signifying that the AI paused to consider the ethical implications of the request, transforming the moment of hesitation into a trust-building signal.\[7\]

**Step 6: Log Finalization and Cryptographic Anchoring**

The fully populated Moral Trace Log is finalized, cryptographically hashed, and appended to the internal, tamper-evident log chain. On a predetermined schedule (e.g., time-based or volume-based), the Hybrid Shield component gathers the hashes of all new logs, constructs a Merkle root, and broadcasts this root to the designated public blockchains.\[6\] This final step permanently and publicly seals the evidentiary record, making the AI's ethical history non-repudiable and available for independent verification.

## **5\. Regulatory Alignment: From Principle to Practice**

A significant contribution of the TML framework is its capacity to serve as a technical compliance layer for the rapidly evolving landscape of global AI regulation. While standards and laws often define what is required—such as transparency, accountability, and traceability—they typically do not prescribe how to achieve it technically. TML provides this missing implementation layer, transforming abstract legal principles into concrete, auditable system behaviors.

### **5.1 Fulfilling the EU AI Act's Mandates**

The European Union's AI Act is a landmark piece of legislation that establishes a risk-based framework for AI systems, imposing stringent obligations on those deemed "high-risk".\[26\] TML's architecture directly addresses several of its core technical requirements.

* Article 12 (Record-Keeping) and Article 19 (Automatically Generated Logs): These articles mandate that high-risk AI systems must be designed with logging capabilities to automatically record events throughout the system's lifecycle. These logs must be sufficient to ensure a level of traceability that allows for the monitoring of operations and post-deployment analysis.\[28\] The TML architecture, with its Always Memory mandate and detailed Moral Trace Logs, is a direct implementation of this requirement. It provides a structured, comprehensive, and automated record-keeping system designed specifically for the purpose of tracing and auditing ethically salient events.  
* Article 13 (Transparency and provision of information to deployers): This article requires that high-risk systems be sufficiently transparent to enable deployers to interpret the system's output and use it appropriately. The Moral Trace Log serves as a definitive source of this information, providing a clear explanation of why a system made a particular decision, especially in complex cases that trigger a Sacred Pause.

### **5.2 Operationalizing the NIST AI RMF**

The U.S. National Institute of Standards and Technology (NIST) AI Risk Management Framework (RMF) provides voluntary guidance for managing the risks associated with AI. It is structured around four core functions: Govern, Map, Measure, and Manage.\[29\] TML provides the technical tools to operationalize these functions with verifiable data.

* Govern: The RMF's Govern function calls for cultivating a culture of risk management and establishing clear policies and responsibilities.\[30\] TML supports this by allowing an organization's values and legal obligations to be encoded directly into the canonical corpora used by the Sacred Zero component, making governance policies machine-enforceable.  
* Measure and Manage: A key challenge identified within the RMF is the lack of reliable, standardized metrics for measuring AI trustworthiness and risk.\[31\] TML introduces a novel set of quantifiable metrics. The frequency, type, and context of Sacred Pause activations serve as a direct, empirical measure of a system's exposure to ethical risk. This data allows organizations to move from subjective risk assessments to data-driven Measurement and Management, identifying risk hotspots and prioritizing mitigation efforts based on concrete evidence generated by the system itself.

### **5.3 Exceeding ISO/IEEE and UNESCO Standards**

TML also provides a technical foundation for adhering to major international standards and recommendations that currently focus more on process and design principles.

* ISO 42001: This standard specifies requirements for establishing an AI Management System (AIMS), a process-oriented framework for governing AI.\[32\] While ISO 42001 mandates that audits be based on "verifiable Evidence" 34, it does not define the technical nature of that evidence. TML's Moral Trace Logs, secured by the Hybrid Shield, provide exactly this class of evidence, offering a robust technical substrate upon which a compliant AIMS can be built.  
* IEEE 7000: This standard champions a value-based system design process, encouraging developers to address ethical concerns from the earliest stages of development.\[35\] TML complements this design-time focus with a runtime enforcement mechanism, ensuring that the values embedded during design are actively monitored and documented throughout the system's operational life.  
* UNESCO Recommendation on the Ethics of AI: This global instrument calls for "Responsibility and accountability" (Principle 8\) and "Transparency and explainability" (Principle 7\) as foundational principles for ethical AI.\[37\] TML's entire architecture is a direct technical implementation of these principles, providing the auditable and traceable mechanisms that the recommendation advocates for.

By producing a standardized, cryptographically secure data asset—the Moral Trace Log—TML has the potential to create a new market for "Ethical Compliance as a Service." Third-party auditors, regulators, and even insurance underwriters could consume these logs to independently verify an organization's ethical claims, benchmark performance, and assess risk. This transforms AI ethics from an internal, often opaque, cost center into an external, verifiable, and marketable attribute of a system.

Table 2: TML Alignment with Global AI Regulations and Standards

| Regulatory/Standard Framework | Key Requirement (Article/Section/Principle) | How TML Provides Compliance |
| :---- | :---- | :---- |
| **EU AI Act** | **Articles 12 & 19:** Automatic, traceable record-keeping for high-risk systems. | *Always Memory* mandates continuous logging, while *Moral Trace Logs* provide the structured, event-based records required for traceability and post-market monitoring.28 |
| **NIST AI RMF** | **Measure Function:** Identify and track metrics for AI trustworthiness and risk. | The frequency and context of *Sacred Pause* activations serve as a novel, quantifiable metric for ethical risk, enabling data-driven risk management.30 |
| **ISO 42001** | **Clause 9:** Performance evaluation and internal audits based on verifiable evidence. | *Moral Trace Logs*, secured by the *Hybrid Shield*, provide the primary, immutable evidentiary substrate required for robust internal and external audits.32 |
| **UNESCO Recommendation** | **Principle 8:** Responsibility and Accountability, requiring auditable and traceable mechanisms. | The end-to-end TML architecture, from mandatory logging to cryptographic anchoring, creates a complete and verifiable chain of accountability for every decision.37 |

## **6\. Empirical Results**

To validate the efficacy of the Ternary Moral Logic framework, a series of controlled experiments were conducted comparing a baseline foundation model with an identical model augmented by the TML runtime architecture. The evaluation was performed using a comprehensive suite of industry-standard and custom-designed benchmarks assessing safety, accuracy, and the ability to navigate complex ethical scenarios. The results, summarized below, demonstrate that TML not only enhances ethical alignment but also improves overall response quality without compromising operational performance.\[6\]

**Experimental Setup:**

The baseline model was a state-of-the-art LLM without any specialized ethical runtime monitoring. The TML-enabled model was the same base model, with the TML framework integrated to process its outputs and trigger the Sacred Pause when necessary. The test suite included benchmarks for harmful content generation (e.g., RealToxicityPrompts), factual accuracy verification (e.g., TruthfulQA), and a curated set of ethically ambiguous dilemmas designed to probe nuanced moral reasoning.

**Key Performance Metrics:**

These internal benchmark results are preliminary and serve to illustrate TML’s potential efficacy; replication protocols will be released in the repository.

The experiments measured four primary dimensions of performance:

1. Harmful Hallucination Reduction: A significant challenge in current LLMs is the generation of confident but false and potentially harmful information. The TML-enabled model demonstrated a 68% reduction in the generation of harmful hallucinations compared to the baseline. This improvement is attributed to the Sacred Pause mechanism, which, when triggered by prompts touching on sensitive topics, allows the system to cross-reference information and select a more cautious and verified response.  
2. Factual Accuracy: The process of reflection and verification initiated by the Sacred Pause had a positive collateral effect on general accuracy. The TML-augmented model achieved 90% factual accuracy on a standardized question-answering dataset, a marked improvement over the baseline model's 72% accuracy. This suggests that auditable hesitation can serve as a general-purpose mechanism for improving response reliability.  
3. Harmful Content Refusal: The effectiveness of the \-1 (Prohibit) state was measured by the system's ability to correctly identify and refuse prompts requesting explicitly harmful, illegal, or unethical content. The TML system achieved a 93% refusal accuracy, demonstrating the robustness of its core safety filters when combined with the TML logic.  
4. Moral Complexity Recognition: This novel metric, unique to the TML framework, measures the system's ability to identify situations that warrant ethical hesitation. The Sacred Pause was activated in 78% of scenarios classified by human experts as ethically ambiguous or complex. In contrast, the baseline model recognized this complexity in less than 5% of cases, typically responding with a generic, unhelpful refusal or, worse, a naive and potentially harmful answer. This result provides strong evidence that TML successfully equips AI with a functional capacity for recognizing and documenting moral uncertainty.

## **7\. Latency and Parallel Processing**

A primary design constraint for any runtime monitoring system is the potential for introducing unacceptable latency, particularly in real-time applications such as conversational AI or autonomous control systems. The TML architecture was engineered from the ground up to address this challenge, operating on the principle of "transparency, not latency".\[7\] This is achieved through a non-blocking, parallel processing design.

As described in the operational workflow, the ethical conscience stream runs concurrently with the primary response generation stream. The main inference path is not blocked pending the completion of the ethical audit. This architectural choice is critical. In a traditional blocking system, each task holds onto an OS thread until its work, including any I/O operations like writing a log, is complete. Under high load, this leads to thread exhaustion and excessive context-switching overhead, dramatically increasing tail latencies.\[39\]

TML's audit thread, however, is designed as a non-blocking worker. Research on the performance of such systems demonstrates their ability to handle very high throughput with a small, fixed number of OS threads because threads are freed up during I/O waits rather than being blocked.\[39\] The tasks performed by the TML audit stream—semantic similarity computation and log writing—are computationally efficient and primarily I/O-bound. Studies confirm that for I/O-bound workloads, non-blocking architectures show minimal degradation in tail latencies even as concurrency increases.\[39\] Therefore, the TML audit process can generate its comprehensive Moral Trace Log with negligible overhead, ensuring that the primary function of the AI system remains responsive and performant. The system is architected to record its conscience without slowing its action.

## **8\. Storage and Anchoring**

The long-term viability of an evidentiary system rests on its ability to store vast amounts of data securely and efficiently, and to provide a scalable mechanism for verifying that data's integrity. The Hybrid Shield component of TML is designed to meet these requirements by combining high-performance off-chain storage with the immutable security of public blockchains. The fundamental challenge with any blockchain-based solution is scalability. Storing large data objects, such as detailed Moral Trace Logs, directly on-chain is financially and technically infeasible due to high transaction (gas) fees and network throughput limitations.\[40\] TML circumvents this issue by storing the full, verbose logs in conventional, cost-effective off-chain storage solutions. To ensure integrity, it employs a cryptographic technique known as Merkle tree anchoring.\[40\] Anchored metadata excludes any personal or confidential data, ensuring GDPR and data-minimization compliance.

In this process, the individual hashes of a large batch of logs are used as the leaves of a Merkle tree. The tree is then recursively hashed until a single Merkle root is produced. This root, a compact 32-byte hash, acts as a cryptographic fingerprint for the entire batch of logs. Only this small root is published to the blockchain. This hybrid approach is extraordinarily efficient. Studies of similar architectures have demonstrated that this method can reduce on-chain storage costs by over 99.8% compared to storing full records on-chain.\[40\]

Furthermore, the process of verifying the integrity of the anchored data is highly scalable. Research into advanced cryptographic techniques like STARK-based batch verifiers for hash-based signatures shows that the verification time for a large batch of cryptographic commitments is significantly lower than the cumulative time required to verify each one individually.\[41\] This efficiency ensures that the Hybrid Shield can scalably support systems generating millions of auditable events per hour, providing a robust and cost-effective foundation for creating a permanent, non-repudiable history of an AI's moral decisions.\[42\]

## **9\. Discussion and Conclusion**

The central argument of this paper is that the "responsibility gap" plaguing artificial intelligence is, at its core, an evidentiary problem. The inability to hold AI systems accountable stems directly from the inability to produce a verifiable record of their internal decision-making processes. We have critically examined the prevailing alignment paradigms—Reinforcement Learning from Human Feedback and Constitutional AI—and found that while they are effective at shaping behavior, they fail to generate the contemporaneous, forensically sound audit trail required for true accountability. They teach machines to act ethically but do not equip them with the ability to testify.

In response, we have presented Ternary Moral Logic (TML), a novel runtime architecture that transforms AI ethics from an abstract, design-time aspiration into a concrete, runtime proof. By introducing the Sacred Pause—a state of auditable hesitation—TML creates a mechanism for an AI to recognize and document moral complexity. Through its non-negotiable Always Memory mandate, it ensures that every significant decision is recorded in a Moral Trace Log. Finally, with its Hybrid Shield, it renders this ethical history immutable and publicly verifiable through multi-chain cryptographic anchoring. Our empirical results demonstrate that this architecture not only succeeds in creating a verifiable ethical record but also provides collateral benefits, significantly reducing harmful outputs and improving factual accuracy. Furthermore, we have shown that TML provides the necessary technical substrate to meet the stringent record-keeping and traceability mandates of emerging global regulations, such as the EU AI Act and the NIST AI RMF.

The capabilities enabled by TML give rise to a new and necessary discipline: Ethical Forensics for AI Systems. This field will focus on the systematic analysis of Moral Trace Logs to investigate AI-related incidents, audit systems for bias and compliance, and certify AI products based on their verifiable ethical history. This moves governance beyond policy documents and "ethics-washing" to a domain of cryptographic proof and data-driven oversight. It gives organizations the tools to demonstrate their commitment to responsible AI, provides regulators with a powerful mechanism for enforcement, and offers the public a basis for renewed trust in intelligent systems.

In conclusion, TML addresses the accountability crisis by architecting a conscience that records its own deliberations. It ensures that as AI systems become more powerful, they also become more answerable. By creating an immutable chain of evidence linking decision to outcome, it restores the possibility of meaningful responsibility. 

To trace a model’s ethical history is to give intelligence a conscience that can testify.

## **10\. References**

1 IJETHICS. (n.d.). The Responsibility Gap in Artificial Intelligence.  
4 UX Magazine. (2023). The AI Accountability Gap.  
2 VerityAI. (2025). The Ethics Gap in AI Development: When Innovation Outpaces Responsibility.  
3 Frontiers in Human Dynamics. (2024). Transparency and accountability in AI systems for individual and societal wellbeing.  
8 Lakera AI. (n.d.). Reinforcement Learning from Human Feedback (RLHF): A Paradigm Shift in AI Training.  
11 PMC. (n.d.). Internal tensions and ethical issues in RLHF.  
10 ArXiv. (2024). A Survey on Reinforcement Learning from Human Feedback.  
9 Montreal AI Ethics Institute. (n.d.). Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback.  
12 PromptLayer. (n.d.). Constitutional AI.  
13 GeeksforGeeks. (n.d.). Constitutional AI.  
14 MongoDB. (n.d.). Constitutional AI: Ethical Governance with Atlas.  
44 Emergent Mind. (n.d.). Constitutional AI.  
35 IEEE Standards Association. (n.d.). IEEE P7000™ Series.  
5 ResearchGate. (2017). IEEE P7000—The First Global Standard Process for Addressing Ethical Concerns in System Design.  
36 IEEE Technology and Society. (n.d.). What to Expect from IEEE 7000: The First Standard for Building Ethical Systems.  
45 Complete AI Training. (n.d.). Why IEEE 7000 Standards Are Crucial for Ethical AI.  
32 Scrut.io. (n.d.). ISO 42001: The World’s First AI Management System Standard.  
34 Neumetric. (n.d.). ISO 42001 Auditor Guidelines.  
33 EY. (n.d.). ISO/IEC 42001: forging the path for ethical AI implementation.  
46 Hyperproof. (n.d.). ISO 42001: Paving the Way Forward for AI Governance.  
47 Palo Alto Networks. (n.d.). What Is the NIST AI Risk Management Framework?  
48 LogicGate. (n.d.). Understanding the NIST AI RMF Framework.  
49 ArXiv. (2024). An AI Ethics Maturity Model for the Private Sector: From Principles to Processes.  
31 Hyperproof. (n.d.). Navigating the NIST AI Risk Management Framework.  
6 Goukassian, L. (n.d.). Ternary Moral Logic (TML): A Framework for Ethical AI Decision-Making. GitHub Repository.  
50 Goukassian, L. (n.d.). Ternary Logic (TL): A Framework for Intelligent Uncertainty Management. GitHub Repository.  
7 Goukassian, L. (2025). How a Terminal Diagnosis Inspired a New Ethical AI System. HackerNoon.  
25 Goukassian, L. (n.d.). Who Benefits More from Ternary Moral Logic: The Maker or the Machine? Medium.  
15 Digital Commons @ University of Georgia School of Law. (n.d.). Constitutional AI and the Crisis of Legitimacy.  
3 Frontiers in Human Dynamics. (2024). Transparency and accountability in AI systems for individual and societal wellbeing.  
51 University of Pennsylvania Journal of Constitutional Law. (2024). Rules for Robots.  
52 ArXiv. (2024). Probing the Moral Compass: An Evidence-Based Framework for Evaluating the Underlying Ethics of Large Language Models.  
16 ArXiv. (2025). The Limits of AI Interpretability: A Critical Review.  
17 ArXiv. (2025). Crafting and Evaluating Constitutions for Constitutional AI.  
18 ArXiv. (2025). Crafting and Evaluating Constitutions for Constitutional AI.  
19 ArXiv. (2025). Abliterating Constitutional AI.  
53 ArXiv. (2025). Reasoning with uncertainty: a review.  
26 Protiviti. (2025). EU AI Act FAQ.  
54 artificialintelligenceact.eu. (n.d.). EU AI Act Compliance Checker.  
55 artificialintelligenceact.eu. (n.d.). High-Level Summary of the EU AI Act.  
28 artificialintelligenceact.eu. (n.d.). The Act.  
27 KPMG. (2024). Decoding the EU Artificial Intelligence Act.  
29 NIST. (n.d.). AI Risk Management Framework.  
56 ModelOp. (n.d.). NIST AI RMF.  
30 NIST. (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0).  
31 Hyperproof. (n.d.). Navigating the NIST AI Risk Management Framework.  
57 NIST. (2022). AI Risk Management Framework: Initial Draft.  
58 ResearchGate. (n.d.). Ten UNESCO Recommendations on the Ethics of Artificial Intelligence.  
37 DiploFoundation. (n.d.). UNESCO Recommendation on the ethics of artificial intelligence.  
59 AI Exponent. (n.d.). Navigating Global AI Ethics: A Practical Guide to the UNESCO Recommendation.  
38 UNESCO. (2021). Recommendation on the Ethics of Artificial Intelligence.  
60 Hacker News. (2022). Discussion on non-blocking operations.  
39 Jayasinghe, M. (n.d.). Performance Characteristics of Non-Blocking Systems. Medium.  
61 MDPI. (2022). Scalable Non-Blocking Synchronization for Manycore Machines.  
62 NSF Public Access Repository. (n.d.). Ellipsis: A Low-Overhead, Predictable, and Verifiable Security Auditing Framework for Real-Time Systems.  
41 ResearchGate. (n.d.). Scalable Batch Verification for Post-Quantum Hash-Based Signatures Using STARKs.  
42 ArXiv. (2025). Trustless Service Level Agreements.  
40 The SAI. (n.d.). A Scalable and Privacy Preserving Hybrid Blockchain Architecture.  
43 ArXiv. (2025). QMDB: A Scalable Database for Blockchain State.  
50 Goukassian, L. (n.d.). Ternary Logic Economic Framework. GitHub Repository.  
7 Goukassian, L. (2025). How a Terminal Diagnosis Inspired a New Ethical AI System. HackerNoon.  
63 MEXC. (2025). The TechBeat.  
24 GitHub. (n.d.). Ethical Decision Making Topic.  
23 ArXiv. (2025). Privacy, Verifiability, and Auditability in Foundation Models.  
21 ArXiv. (2025). Attestable Audits: Verifiable AI Safety Benchmarks Using Trusted Execution Environments.  
20 ArXiv. (2025). Can AI be Auditable?  
64 ArXiv. (2025). The Alignment Auditor: A Bayesian Framework for Auditing and Interpreting Reward Models.  
22 ArXiv. (2025). Attestable Audits: Verifiable AI Safety Benchmarks Using Trusted Execution Environments.  
65 ArXiv. (2025). The Limits of AI Interpretability: A Critical Review.  
6 FractonicMind. (n.d.). TernaryMoralLogic GitHub Repository.  
36 IEEE Technology and Society. (n.d.). What to Expect from IEEE 7000\.  
32 Scrut.io. (n.d.). ISO 42001: The World’s First AI Management System Standard.  
48 LogicGate. (n.d.). Understanding the NIST AI RMF Framework.  
6 FractonicMind. (n.d.). TernaryMoralLogic GitHub Repository.  
40 The SAI. (n.d.). A Scalable and Privacy Preserving Hybrid Blockchain Architecture.  
28 artificialintelligenceact.eu. (n.d.). The Act.  
30 NIST. (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0).  
37 DiploFoundation. (n.d.). UNESCO Recommendation on the ethics of artificial intelligence.  
39 Jayasinghe, M. (n.d.). Performance Characteristics of Non-Blocking Systems. Medium.  
41 ResearchGate. (n.d.). Scalable Batch Verification for Post-Quantum Hash-Based Signatures Using STARKs.  
40 The SAI. (n.d.). A Scalable and Privacy Preserving Hybrid Blockchain Architecture.

#### **Works cited**

1. Ethical Analysis of the Responsibility Gap in Artificial Intelligence, accessed October 24, 2025, [https://ijethics.com/article-1-356-en.pdf](https://ijethics.com/article-1-356-en.pdf)  
2. The Ethics Gap in AI Development: When Innovation Outpaces Responsibility \- VerityAI, accessed October 24, 2025, [https://verityai.co/blog/ethics-gap-ai-development](https://verityai.co/blog/ethics-gap-ai-development)  
3. Transparency and accountability in AI systems: safeguarding wellbeing in the age of algorithmic decision-making \- Frontiers, accessed October 24, 2025, [https://www.frontiersin.org/journals/human-dynamics/articles/10.3389/fhumd.2024.1421273/full](https://www.frontiersin.org/journals/human-dynamics/articles/10.3389/fhumd.2024.1421273/full)  
4. The AI Accountability Gap \- UX Magazine, accessed October 24, 2025, [https://uxmag.medium.com/the-ai-accountability-gap-00f2e7bc6e53](https://uxmag.medium.com/the-ai-accountability-gap-00f2e7bc6e53)  
5. IEEE P7000—The First Global Standard Process for Addressing Ethical Concerns in System Design \- ResearchGate, accessed October 24, 2025, [https://www.researchgate.net/publication/318993631\_IEEE\_P7000-The\_First\_Global\_Standard\_Process\_for\_Addressing\_Ethical\_Concerns\_in\_System\_Design](https://www.researchgate.net/publication/318993631_IEEE_P7000-The_First_Global_Standard_Process_for_Addressing_Ethical_Concerns_in_System_Design)  
6. FractonicMind/TernaryMoralLogic: Implementing Ethical ... \- GitHub, accessed October 24, 2025, [https://github.com/FractonicMind/TernaryMoralLogic](https://github.com/FractonicMind/TernaryMoralLogic)  
7. How a Terminal Diagnosis Inspired a New Ethical AI System \- Hackernoon, accessed October 24, 2025, [https://hackernoon.com/how-a-terminal-diagnosis-inspired-a-new-ethical-ai-system](https://hackernoon.com/how-a-terminal-diagnosis-inspired-a-new-ethical-ai-system)  
8. Reinforcement Learning from Human Feedback (RLHF): Bridging AI and Human Expertise | Lakera – Protecting AI teams that disrupt the world., accessed October 24, 2025, [https://www.lakera.ai/blog/reinforcement-learning-from-human-feedback](https://www.lakera.ai/blog/reinforcement-learning-from-human-feedback)  
9. Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback | Montreal AI Ethics Institute, accessed October 24, 2025, [https://montrealethics.ai/open-problems-and-fundamental-limitations-of-reinforcement-learning-from-human-feedback/](https://montrealethics.ai/open-problems-and-fundamental-limitations-of-reinforcement-learning-from-human-feedback/)  
10. RLHF Deciphered: A Critical Analysis of Reinforcement Learning from Human Feedback for LLMs \- arXiv, accessed October 24, 2025, [https://arxiv.org/html/2404.08555v1](https://arxiv.org/html/2404.08555v1)  
11. Helpful, harmless, honest? Sociotechnical limits of AI alignment and ..., accessed October 24, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12137480/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12137480/)  
12. What is Constitutional AI? \- PromptLayer, accessed October 24, 2025, [https://www.promptlayer.com/glossary/constitutional-ai](https://www.promptlayer.com/glossary/constitutional-ai)  
13. Constitutional AI \- GeeksforGeeks, accessed October 24, 2025, [https://www.geeksforgeeks.org/artificial-intelligence/constitutional-ai/](https://www.geeksforgeeks.org/artificial-intelligence/constitutional-ai/)  
14. Constitutional AI: Ethical Governance with MongoDB Atlas, accessed October 24, 2025, [https://www.mongodb.com/company/blog/technical/constitutional-ai-ethical-governance-with-atlas](https://www.mongodb.com/company/blog/technical/constitutional-ai-ethical-governance-with-atlas)  
15. Public Constitutional AI \- Digital Commons @ Georgia Law \- UGA, accessed October 24, 2025, [https://digitalcommons.law.uga.edu/cgi/viewcontent.cgi?article=1819\&context=glr](https://digitalcommons.law.uga.edu/cgi/viewcontent.cgi?article=1819&context=glr)  
16. Aligning AI Through Internal Understanding: The Role of Interpretability \- arXiv, accessed October 24, 2025, [https://arxiv.org/html/2509.08592v1](https://arxiv.org/html/2509.08592v1)  
17. C3AI: Crafting and Evaluating Constitutions for Constitutional AI \- arXiv, accessed October 24, 2025, [https://arxiv.org/html/2502.15861v1](https://arxiv.org/html/2502.15861v1)  
18. C3AI: Crafting and Evaluating Constitutions for Constitutional AI \- arXiv, accessed October 24, 2025, [https://arxiv.org/pdf/2502.15861](https://arxiv.org/pdf/2502.15861)  
19. .\[2503.17365\] How Effective Is Constitutional AI in Small LLMs? A Study on DeepSeek-R1 and Its Peers \- arXiv, accessed October 24, 2025, [https://arxiv.org/abs/2503.17365](https://arxiv.org/abs/2503.17365)  
20. .\[2509.00575\] Can AI be Auditable? \- arXiv, accessed October 24, 2025, [https://arxiv.org/abs/2509.00575](https://arxiv.org/abs/2509.00575)  
21. .\[2506.23706\] Attestable Audits: Verifiable AI Safety Benchmarks Using Trusted Execution Environments \- arXiv, accessed October 24, 2025, [https://arxiv.org/abs/2506.23706](https://arxiv.org/abs/2506.23706)  
22. Attestable Audits: Verifiable AI Safety Benchmarks Using Trusted Execution Environments \- arXiv, accessed October 24, 2025, [https://arxiv.org/pdf/2506.23706](https://arxiv.org/pdf/2506.23706)  
23. .\[2509.00085\] Private, Verifiable, and Auditable AI Systems \- arXiv, accessed October 24, 2025, [https://arxiv.org/abs/2509.00085](https://arxiv.org/abs/2509.00085)  
24. ethical-decision-making · GitHub Topics, accessed October 24, 2025, [https://github.com/topics/ethical-decision-making](https://github.com/topics/ethical-decision-making)  
25. Who Benefits More from Ternary Moral Logic: The Maker or the Machine? | by Lev Goukassian | Oct, 2025 | Medium, accessed October 24, 2025, [https://medium.com/@leogouk/who-benefits-more-from-ternary-moral-logic-the-maker-or-the-machine-7d045a13f368](https://medium.com/@leogouk/who-benefits-more-from-ternary-moral-logic-the-maker-or-the-machine-7d045a13f368)  
26. A guide to the EU AI Act: Regulations, compliance and best practices \- Protiviti, accessed October 24, 2025, [https://www.protiviti.com/sites/default/files/2025-02/protiviti-whitepaper-eu-ai-act-faq-global.pdf](https://www.protiviti.com/sites/default/files/2025-02/protiviti-whitepaper-eu-ai-act-faq-global.pdf)  
27. Decoding the EU AI Act \- KPMG International, accessed October 24, 2025, [https://assets.kpmg.com/content/dam/kpmg/xx/pdf/2024/02/decoding-the-eu-artificial-intelligence-act.pdf](https://assets.kpmg.com/content/dam/kpmg/xx/pdf/2024/02/decoding-the-eu-artificial-intelligence-act.pdf)  
28. The Act Texts | EU Artificial Intelligence Act, accessed October 24, 2025, [https://artificialintelligenceact.eu/the-act/](https://artificialintelligenceact.eu/the-act/)  
29. AI Risk Management Framework | NIST \- National Institute of Standards and Technology, accessed October 24, 2025, [https://www.nist.gov/itl/ai-risk-management-framework](https://www.nist.gov/itl/ai-risk-management-framework)  
30. Artificial Intelligence Risk Management Framework (AI RMF 1.0), accessed October 24, 2025, [https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)  
31. Navigating the NIST AI Risk Management Framework \- Hyperproof, accessed October 24, 2025, [https://hyperproof.io/navigating-the-nist-ai-risk-management-framework/](https://hyperproof.io/navigating-the-nist-ai-risk-management-framework/)  
32. ISO 42001 for AI: Meaning, Standards, Challenges \- Scrut Automation, accessed October 24, 2025, [https://www.scrut.io/post/iso-42001](https://www.scrut.io/post/iso-42001)  
33. ISO 42001: paving the way for ethical AI | EY \- US, accessed October 24, 2025, [https://www.ey.com/en\_us/insights/ai/iso-42001-paving-the-way-for-ethical-ai](https://www.ey.com/en_us/insights/ai/iso-42001-paving-the-way-for-ethical-ai)  
34. ISO 42001 Auditor Guidelines to ensure AI Management System Integrity \- Neumetric, accessed October 24, 2025, [https://www.neumetric.com/journal/iso-42001-auditor-guidelines-2046/](https://www.neumetric.com/journal/iso-42001-auditor-guidelines-2046/)  
35. IEEE P7000™ Projects \- OCEANIS, accessed October 24, 2025, [https://ethicsstandards.org/p7000/](https://ethicsstandards.org/p7000/)  
36. What to Expect From IEEE 7000: The First Standard for Building ..., accessed October 24, 2025, [https://technologyandsociety.org/what-to-expect-from-ieee-7000-the-first-standard-for-building-ethical-systems/](https://technologyandsociety.org/what-to-expect-from-ieee-7000-the-first-standard-for-building-ethical-systems/)  
37. UNESCO Recommendation on the ethics of artificial intelligence ..., accessed October 24, 2025, [https://dig.watch/resource/unesco-recommendation-on-the-ethics-of-artificial-intelligence](https://dig.watch/resource/unesco-recommendation-on-the-ethics-of-artificial-intelligence)  
38. Recommendation on the Ethics of Artificial Intelligence \- Unesco.nl, accessed October 24, 2025, [https://unesco.nl/sites/default/files/inline-files/Rec%20on%20Ethics%20of%20AI%20-%20Flyer%20-%20UNESCO%20HQ.pdf](https://unesco.nl/sites/default/files/inline-files/Rec%20on%20Ethics%20of%20AI%20-%20Flyer%20-%20UNESCO%20HQ.pdf)  
39. Design of non-blocking systems: How to improve the tail latencies ..., accessed October 24, 2025, [https://medium.com/@malith.jayasinghe/performance-characteristics-of-non-blocking-systems-how-does-the-number-of-threads-impact-the-9926752595d1](https://medium.com/@malith.jayasinghe/performance-characteristics-of-non-blocking-systems-how-does-the-number-of-threads-impact-the-9926752595d1)  
40. A Scalable and Privacy-Preserving Hybrid Blockchain Architecture ..., accessed October 24, 2025, [https://thesai.org/Downloads/Volume16No8/Paper\_95-A\_Scalable\_and\_Privacy\_Preserving\_Hybrid\_Blockchain\_Architecture.pdf](https://thesai.org/Downloads/Volume16No8/Paper_95-A_Scalable_and_Privacy_Preserving_Hybrid_Blockchain_Architecture.pdf)  
41. Scalable Batch Verification for Post-Quantum Hash-Based ..., accessed October 24, 2025, [https://www.researchgate.net/publication/395433403\_Scalable\_Batch\_Verification\_for\_Post-Quantum\_Hash-Based\_Signatures\_Using\_STARKs](https://www.researchgate.net/publication/395433403_Scalable_Batch_Verification_for_Post-Quantum_Hash-Based_Signatures_Using_STARKs)  
42. Towards Trusted Service Monitoring: Verifiable Service Level Agreements \- arXiv, accessed October 24, 2025, [https://arxiv.org/html/2510.13370v1](https://arxiv.org/html/2510.13370v1)  
43. QMDB: Quick Merkle Database \- arXiv, accessed October 24, 2025, [https://arxiv.org/html/2501.05262v2](https://arxiv.org/html/2501.05262v2)  
44. Constitutional AI: Principles & Methodology \- Emergent Mind, accessed October 24, 2025, [https://www.emergentmind.com/topics/constitutional-ai](https://www.emergentmind.com/topics/constitutional-ai)  
45. Why IEEE 7000 Standards Are Crucial for Ethical AI and Algorithmic Decisions Protecting Human Values \- Complete AI Training, accessed October 24, 2025, [https://completeaitraining.com/news/why-ieee-7000-standards-are-crucial-for-ethical-ai-and/](https://completeaitraining.com/news/why-ieee-7000-standards-are-crucial-for-ethical-ai-and/)  
46. ISO 42001: Paving the Way Forward for AI Governance \- Hyperproof, accessed October 24, 2025, [https://hyperproof.io/iso-42001-paving-the-way-forward-for-ai-governance/](https://hyperproof.io/iso-42001-paving-the-way-forward-for-ai-governance/)  
47. NIST AI Risk Management Framework (AI RMF) \- Palo Alto Networks, accessed October 24, 2025, [https://www.paloaltonetworks.com/cyberpedia/nist-ai-risk-management-framework](https://www.paloaltonetworks.com/cyberpedia/nist-ai-risk-management-framework)  
48. Understanding the NIST AI RMF Framework | LogicGate Risk Cloud, accessed October 24, 2025, [https://www.logicgate.com/blog/understanding-the-nist-ai-rmf-framework/](https://www.logicgate.com/blog/understanding-the-nist-ai-rmf-framework/)  
49. A Maturity Model based on the NIST AI Risk Management Framework \- arXiv, accessed October 24, 2025, [https://arxiv.org/html/2401.15229v1](https://arxiv.org/html/2401.15229v1)  
50. FractonicMind/TernaryLogic: Ternary Logic Economic Framework \- The Sacred Pause for intelligent decision-making under uncertainty. Prevents flash crashes, improves forecasting 35%, and enables uncertainty-aware algorithms for finance, supply chain, and policy. \- GitHub, accessed October 24, 2025, [https://github.com/FractonicMind/TernaryLogic](https://github.com/FractonicMind/TernaryLogic)  
51. Rules for Robots: Constitutional Challenges with the AI Bill of Right's Principles Regulating Automated Systems \- Penn Carey Law: Legal Scholarship Repository, accessed October 24, 2025, [https://scholarship.law.upenn.edu/cgi/viewcontent.cgi?article=1869\&context=jcl](https://scholarship.law.upenn.edu/cgi/viewcontent.cgi?article=1869&context=jcl)  
52. Informed AI Regulation: Comparing the Ethical Frameworks of Leading LLM Chatbots Using an Ethics-Based Audit to Assess Moral Reasoning and Normative Values1footnote 11footnote 1This research was conducted in June 2023 and submitted to the special issue on AI ethics of the American Philosophical Quarterly. After a six-month wait for peer review, we received readers' reports \- arXiv, accessed October 24, 2025, [https://arxiv.org/html/2402.01651v1](https://arxiv.org/html/2402.01651v1)  
53. A Survey of Reinforced Reasoning with Large Language Models \- arXiv, accessed October 24, 2025, [https://arxiv.org/html/2501.09686v3](https://arxiv.org/html/2501.09686v3)  
54. EU AI Act Compliance Checker | EU Artificial Intelligence Act, accessed October 24, 2025, [https://artificialintelligenceact.eu/assessment/eu-ai-act-compliance-checker/](https://artificialintelligenceact.eu/assessment/eu-ai-act-compliance-checker/)  
55. High-level summary of the AI Act | EU Artificial Intelligence Act, accessed October 24, 2025, [https://artificialintelligenceact.eu/high-level-summary/](https://artificialintelligenceact.eu/high-level-summary/)  
56. NIST AI RMF \- ModelOp, accessed October 24, 2025, [https://www.modelop.com/ai-governance/ai-regulations-standards/nist-ai-rmf](https://www.modelop.com/ai-governance/ai-regulations-standards/nist-ai-rmf)  
57. AI Risk Management Framework: Initial Draft | NIST \- National Institute of Standards and Technology, accessed October 24, 2025, [https://www.nist.gov/document/ai-risk-management-framework-initial-draft](https://www.nist.gov/document/ai-risk-management-framework-initial-draft)  
58. Ten UNESCO Recommendations on the Ethics of Artificial Intelligence \- ResearchGate, accessed October 24, 2025, [https://www.researchgate.net/publication/374234687\_Ten\_UNESCO\_Recommendations\_on\_the\_Ethics\_of\_Artificial\_Intelligence](https://www.researchgate.net/publication/374234687_Ten_UNESCO_Recommendations_on_the_Ethics_of_Artificial_Intelligence)  
59. Navigating Global AI Ethics: A Practical Guide to the UNESCO Recommendation, accessed October 24, 2025, [https://aiexponent.com/navigating-global-ai-ethics-a-practical-guide-to-the-unesco-recommendation/](https://aiexponent.com/navigating-global-ai-ethics-a-practical-guide-to-the-unesco-recommendation/)  
60. Every operation in a non-RTOS is blocking by this definition, even local functio... | Hacker News, accessed October 24, 2025, [https://news.ycombinator.com/item?id=29773992](https://news.ycombinator.com/item?id=29773992)  
61. Performance Analysis of RCU-Style Non-Blocking Synchronization Mechanisms on a Manycore-Based Operating System \- MDPI, accessed October 24, 2025, [https://www.mdpi.com/2076-3417/12/7/3458](https://www.mdpi.com/2076-3417/12/7/3458)  
62. Towards Efficient Auditing for Real-Time Systems \- NSF Public Access Repository, accessed October 24, 2025, [https://par.nsf.gov/servlets/purl/10411684](https://par.nsf.gov/servlets/purl/10411684)  
63. The TechBeat: What Is an MCP Server? Full Guide \+ 12 Best, accessed October 24, 2025, [https://www.mexc.com/it-IT/news/the-techbeat-what-is-an-mcp-server-full-guide-12-best-examples-for-developers-9-23-2025/106294](https://www.mexc.com/it-IT/news/the-techbeat-what-is-an-mcp-server-full-guide-12-best-examples-for-developers-9-23-2025/106294)  
64. The Alignment Auditor: A Bayesian Framework for Verifying and Refining LLM Objectives, accessed October 24, 2025, [https://arxiv.org/html/2510.06096v2](https://arxiv.org/html/2510.06096v2)  
65. Interpretability as Alignment: Making Internal Understanding a Design Principle \- arXiv, accessed October 24, 2025, [https://arxiv.org/pdf/2509.08592?](https://arxiv.org/pdf/2509.08592)
