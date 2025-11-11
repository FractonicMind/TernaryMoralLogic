# **NIST and TML: From Culture to Code. A Technical-Policy Whitepaper on the Integration of Ternary Moral Logic with the NIST AI Risk Management Framework**

**Author:** Lev Goukassian  
**Affiliation:** Independent Researcher  
**Contact:** leogouk@gmail.com  
**Keywords:** AI Governance, NIST, Accountability, Sacred Pause, Ternary Moral Logic, AI Ethics, Auditable AI, Immutable Logs, Public Blockchains

## **Executive Summary: The Accountability Architecture**

**Thesis Statement:** The National Institute of Standards and Technology (NIST) AI Risk Management Framework (AI RMF) provides an essential, consensus-driven guide for *what* constitutes trustworthy AI management.1 However, its explicitly voluntary nature creates a persistent "enforcement gap," relying on an organization's "risk culture" 4 rather than verifiable proof.5 This whitepaper demonstrates how Ternary Moral Logic (TML) provides the "how"—a concrete computational architecture that transforms NIST's four functions (Govern, Map, Measure, Manage) into a verifiable, auditable, and enforceable system.  
**The TML Solution:** TML bridges the gap from abstract policy to embedded code. It operationalizes NIST's principles through four key mechanisms:

1. **The Sacred Pause (State 0):** Enforces mandatory deliberation for high-risk decisions.  
2. **The Ethical Uncertainty Score (EUS):** Quantifies moral and normative ambiguity against a defined legal corpus.  
3. **The Clarifying Question Engine (CQE):** Provides a structured, auditable human-in-the-loop (HITL) mechanism to resolve uncertainty.  
4. **The Immutable Moral Trace Log & Hybrid Shield:** Creates a cryptographically secure "flight data recorder" for every ethical decision, proving compliance.

**Core Argument:** TML does not replace NIST; it fulfills it. It provides the technical implementation that allows an organization to *prove* its compliance with the RMF, moving beyond subjective "trust claims" 6 to objective, measurable, and "accountability architecture."  
**The NIST AI RMF $\\times$ TML Implementation Matrix**

| NIST Function | Objective (Per NIST RMF) | TML Mechanism | Result (Verifiable Compliance) |
| :---- | :---- | :---- | :---- |
| **Govern** | Establish accountability, oversight, and feedback mechanisms.6 | Sacred Pause (State 0\) \+ Clarifying Question Engine (CQE) \+ Immutable Logs. | Demonstrable "human-in-the-loop" control 8; structural governance enforced in code; creates auditable proof of deliberation satisfying GOVERN 3.2 & 5.2. |
| **Map** | Identify AI context, purpose, and potential negative impacts on individuals, society, and the planet.6 | Ethical Uncertainty Score (EUS) thresholds \+ Ethical Taxonomy Triggers (derived from 46+ documents). | Detects moral complexity and normative ambiguity *before* deployment or output 9; transforms static mapping 10 into a continuous, live process. |
| **Measure** | Evaluate and quantify risk, bias, and uncertainty using defined metrics.6 | Quantified EUS scores \+ CQE feedback loops.11 | Converts qualitative ethics ("fairness," "accountability") into a measurable, quantitative indicator 4; produces traceable evidence.6 |
| **Manage** | Implement mitigation and enable continuous monitoring and incident response.6 | Hybrid Shield 13 \+ Anchored Immutable Logs \+ Continuous Audit Cycles. | Continuous verification of ethical integrity; provides a cryptographically verifiable "flight data recorder" 15 for incident response and audit.16 |

---

## **Part I: The NIST Mandate and the Enforcement Gap**

### **1.1 The NIST AI RMF: A Framework for a Trustworthy AI Culture**

The National Institute of Standards and Technology (NIST) AI Risk Management Framework (AI RMF 1.0), released in January 2023, is a landmark document developed in response to the National Artificial Intelligence Initiative Act of 2020\.1 It represents a comprehensive, consensus-driven effort, forged in collaboration with public and private sectors, to create a resource for "organizations designing, developing, deploying, or using AI systems to help manage the many risks of AI and promote trustworthy and responsible development".2  
The framework’s core architecture is organized into four key functions, designed to be iterative and continuous: **Govern, Map, Measure, and Manage**.1 These functions provide a vocabulary and a methodology for incorporating "trustworthiness considerations" (such as validity, reliability, safety, fairness, and accountability) into the entire AI lifecycle.1  
A central and defining feature of the RMF is its "voluntary" mandate.1 NIST explicitly states the framework is "intended for voluntary use" and is "non-sector specific, and use-case agnostic".2 This strategic flexibility is designed to encourage broad adoption across diverse industries and applications. This flexibility is further evidenced by NIST's "profile" concept. A profile is a specific "implementation of the AI RMF functions" tailored for a "specific setting, application, or technology," such as the Generative AI Profile.18 This clearly indicates that NIST's intention is for the RMF to serve as a *foundational* framework upon which organizations must build their own *specific, concrete implementations*.  
This voluntary, flexible design positions the RMF as a *performance standard* rather than a *prescriptive standard*. It defines a desirable end-state—"trustworthy and responsible AI" 2—but it does not mandate the specific technical mechanisms, algorithms, or architectural choices required to achieve it. Instead, the RMF seeks to help organizations "cultivate trust in AI technologies" 1 by fostering an internal "risk management culture".4 This very flexibility, however, creates a significant challenge. Culture, by its nature, is intangible, difficult to audit, and often unreliable under market or operational pressure. This creates a critical "enforcement gap," leaving a void between the RMF's stated goals and the verifiable proof of their achievement.

### **1.2 The Implementation Deficit: From "Risk Culture" to Verifiable Proof**

The RMF’s reliance on "trust" and "culture" creates an implementation deficit. The stated goal is to "build a foundation for ethical, secure, and transparent AI practices that strengthen public trust".19 However, in high-stakes domains, trust is not a starting point; it is the *result* of auditable, verifiable proof. Without such proof, "trust" is merely a marketing claim. The RMF's descriptive guidelines on "trustworthiness" 2 are insufficient for a compliance or legal officer who must *demonstrate* adherence to a regulator.  
This deficit is most acute in the concept of "human-in-the-loop" (HITL) oversight, a common method proposed for ensuring accountability.22 As critics and even legal testimony have pointed out, HITL is "no panacea".23 In many real-world systems, HITL is implemented as a passive "review" function that creates "loopholes with the potential to dramatically undermine the law".23 A human operator tasked with reviewing thousands of AI-generated decisions is highly susceptible to "automation bias" 22, merely "rubber-stamping" the machine's recommendation to clear a queue. This fails to achieve meaningful governance.  
The RMF itself points to this gap in its own language. It repeatedly calls for mechanisms that it does not, and was not designed to, define:

* **GOVERN 5.2** states, "Mechanisms are established to enable... adjudicated feedback".6 It does not specify the mechanism.  
* **MAP 2.1** states, "Potential negative impacts... are identified and documented".6 It does not provide the taxonomy of "impacts."  
* **MEASURE 1.1** states, "Approaches and metrics for measurement... are selected".6 It does not define the metrics.

The RMF leaves the *how*—the *specific* mechanisms, the *comprehensive* taxonomies, and the *quantifiable* metrics—as an exercise for the implementer.  
This is precisely where TML provides its value. NIST's "profile" model explicitly invites implementable solutions.18 While other "profiles" have been proposed, such as the U.S. State Department's "Human Rights Profile" 9, these remain *policy* documents. They advise organizations on what to "consider" 9 but do not provide the *computational architecture* for doing so.  
Ternary Moral Logic is not another policy document; it is an **architectural profile**. It provides the concrete, code-level implementation of the RMF's policies. It delivers the specific, auditable mechanisms 24 that the RMF 6 and its derivative profiles 9 call for but do not provide. TML directly solves this "implementation deficit" by providing the technical "how" to NIST's "what," transforming the RMF from a set of abstract "best practices" 1 into a verifiable "accountability architecture."  
---

## **Part II: Architectural Implementation of the NIST Functions via TML**

This section provides a systematic, function-by-function analysis of how Ternary Moral Logic's computational mechanisms provide the verifiable implementation of the NIST RMF's objectives.

### **2.1 GOVERN: Architecting Structural Accountability**

**NIST Objective (GOVERN):** The GOVERN function is the "cross-cutting function" 6 designed to establish the "organizational accountability" 7 and "oversight... for AI risk".10 It is the foundation upon which the other functions are built. Its subcategories explicitly call for concrete roles, documentation, and feedback mechanisms. Key requirements include:

* **GOVERN 1.1:** "Legal and regulatory requirements... are understood, managed, and documented".18  
* **GOVERN 3.2:** "Policies and procedures are in place to define and differentiate roles and responsibilities for human-AI configurations and oversight".6  
* **GOVERN 4.1:** "Organizational policies and practices are in place to foster a critical thinking and safety-first mindset".6  
* **GOVERN 4.2:** "Organizational teams document the risks and potential impacts".6  
* **GOVERN 5.2:** "Mechanisms are established to enable the team... to regularly incorporate adjudicated feedback from relevant AI actors".6

TML Integration: From Policy to Pipeline:  
TML integrates these "policies" 27 directly into the AI's decision-making pipeline, transforming them from static documents in a compliance folder into active, computational components. This structural integration is the only way to ensure governance is not a "loophole" 23 but an enforced reality.

1. **The Sacred Pause (State 0):** This mechanism is the *architectural enforcement* of GOVERN 4.1's "safety-first mindset".6 In a standard system, an AI's high-uncertainty (or "low confidence") output is often still presented as a valid option, leading to "automation bias" 22 where a human supervisor passively accepts it. The Sacred Pause, by contrast, is an *active computational state* of *moral deliberation*.28 When TML's EUS (see 2.3) detects high normative risk, the system is programmatically forced into this "pause" state. This functions as an "AI circuit breaker" 29, *mandating* a halt to automated execution and initiating a "handover contract" 8 to a human. This structurally enforces "critical thinking" 6 by making it non-optional.  
2. **The Clarifying Question Engine (CQE):** The Sacred Pause is not an error message; it is the *trigger* for the CQE. The CQE *is* the "mechanism... for adjudicated feedback" required by GOVERN 5.2.6 It initiates a structured, human-in-the-loop (HITL) dialogue.11 This process is explicitly designed to fulfill GOVERN 3.2 6 by engaging a *defined role* (e.g., a "Human Moral Authority") who is responsible for oversight. The CQE presents the moral dilemma, the conflicting principles it has identified, and asks a structured question (e.g., "This action may promote $Principle A$ but risks violating $Principle B$. Please provide justification for proceeding."). This active, interrogative process forces the human overseer to *create* a "justification trace" 25, converting an ambiguous ethical dilemma into an explicit, documented, and *adjudicated* decision.  
3. **Immutable Moral Trace Logs:** This mechanism *is* the "documentation" required by GOVERN 4.2 6 and the management of "legal and regulatory requirements" under GOVERN 1.1.18 Every Sacred Pause, every EUS score, every question posed by the CQE, and every "adjudicated" justification from the human overseer is recorded in a cryptographically secured log (see 2.4). This log *is* the verifiable proof that the governance process was followed.

The problem with standard AI governance is its decoupling from the AI's execution pipeline. A policy document 27 stored on a corporate intranet does not stop an algorithm from making a discriminatory or harmful decision in milliseconds. NIST's calls in GOVERN 3.2 6 and GOVERN 5.2 6 for "configurations" and "mechanisms" are a clear acknowledgment of this problem, while critics 23 warn that "human review exemptions" are a critical loophole. TML's Pause $\\rightarrow$ CQE $\\rightarrow$ Log sequence *is* the "meaningful human oversight" 8 that the RMF demands and that standard HITL systems fail to provide.  
This sequence is an *architectural* solution 24 that enforces a "solve-verify asymmetry" 8: the AI *solves* (i.e., generates a proposed action), but for all high-risk cases, a human *must verify* (i.e., provide an auditable justification). This creates a form of *computational due process*, where a decision with high normative impact cannot be finalized until it has passed a mandatory, documented, and verifiable deliberative step. TML thus hard-wires accountability directly into the system's architecture.

### **2.2 MAP: From Static Checklists to Continuous Contextual Awareness**

**NIST Objective (MAP):** The MAP function "establishes the context to frame risks".4 It is the foundational risk-finding phase. Its subcategories demand a comprehensive, holistic understanding of the system and its potential harms:

* **MAP 1.1 / 1.2:** "The capabilities, limitations, and intended purpose of the AI system are documented" and "Context-specific information... is documented, including... foreseeable misuse".6  
* **MAP 2.1:** "Potential negative impacts (harms) to individuals, groups, organizations, communities, society, the environment, and the planet are identified and documented".6  
* **MAP 2.4:** "Components and data, including their provenance and limitations, that may affect the trustworthy characteristics... are identified and documented".6

TML Integration: Using International Law as the Risk Taxonomy:  
The central challenge of the MAP function is MAP 2.1.6 Its scope is cosmic: how does a private organization or even a government agency begin to "identify" all potential harms to "individuals, groups... society, the environment, and the planet"?  
TML's solution is to *not* invent a new, proprietary ethical framework. Instead, it leverages the 75+ years of international consensus codified in foundational human rights and environmental law. This approach is explicitly called for by human rights-based risk assessments, which translate "the UN Guiding Principles on Business and Human Rights into a three-part methodology".9

1. **The Normative Corpus (Appendices A & B):** TML ingests a vast corpus of 46+ foundational legal and environmental documents as its *primary "ethical taxonomy."* This corpus (detailed in Appendices A and B) *is* TML's baseline definition of "harm." It provides a globally-recognized, defensible, and stable foundation for risk-mapping.  
   * **Human Rights (Appendix A):** The 26+ documents, including the International Bill of Human Rights, the Convention on the Elimination of All Forms of Discrimination against Women (CEDAW), the Convention on the Rights of the Child (CRC), and the International Convention on the Elimination of All Forms of Racial Discrimination (ICERD), provide the taxonomy for harms to "individuals, groups, organizations, communities".32  
   * **Environmental Law (Appendix B):** The 20+ documents, including the three Rio Conventions (UNFCCC, CBD, UNCCD), the Paris Agreement, the Montreal Protocol, and the Basel Convention, provide the taxonomy for harms to "society, the environment, and the planet".37  
2. **The Ethical Uncertainty Score (EUS) as a "Mapper":** The EUS is TML's *primary* mapping mechanism. It functions as a continuous, real-time "context-mapper".4 It computationally analyzes a proposed AI action (e.g., a text output, a resource allocation decision) and measures its *semantic ambiguity or conflict* against the normative vectors derived from this 46+ document corpus.43  
   * **Example 1 (Human Rights):** An AI model used for content moderation proposes to delete a political comment. TML's EUS simultaneously maps this action against Article 19 of the Universal Declaration of Human Rights (UDHR) ("right to freedom of opinion and expression") 34 and Article 4 of ICERD (which calls for the prohibition of "all dissemination of ideas based on racial superiority or hatred").32 The high semantic conflict between these two *equally valid* legal principles generates a high EUS, forcing a Sacred Pause and human "adjudication".6  
   * **Example 2 (Environmental):** An AI optimizing a supply chain recommends a shipping route that is cheapest but uses a high-sulfur fuel in a protected maritime zone. The EUS maps this recommendation against the International Convention for the Prevention of Pollution from Ships (MARPOL) 45 and the UN Convention on the Law of the Sea (UNCLOS).37 The clear violation of these environmental protocols generates a high EUS and triggers a human review, *before* the harmful recommendation is ever executed.

This approach reveals a critical flaw in traditional AI risk management. Standard practices treat "mapping" as a static, pre-deployment "phase" or a "structured workshop".10 This model is fundamentally broken in the age of generative AI. Generative AI systems are defined by *emergent behaviors* 18 and "unanticipated impacts" 18 that no pre-deployment checklist could ever capture. A "map" of risks created in January is obsolete by February.  
TML's EUS-based approach, grounded in the legal corpus, transforms MAP from a static "phase" into a *continuous, live, at-inference process*. The mapping of risk 9 is not a one-time event; it happens *at the moment of decision*. This is the only viable methodology for managing the dynamic, emergent, and "context-collapse" risks 18 of modern AI systems.

### **2.3 MEASURE: The Quantification of Ethical Uncertainty**

**NIST Objective (MEASURE):** The MEASURE function "employs quantitative, qualitative, or mixed-method tools, techniques, and methodologies to analyze, assess, benchmark, and monitor AI risk".6 It is the function that demands *evidence*. Key subcategories include:

* **MEASURE 1.1:** "Approaches and metrics for measurement of AI risks enumerated during the MAP function are selected... The risks or trustworthiness characteristics that will not – or cannot – be measured are properly documented".6  
* **MEASURE 2.3:** "AI system performance... criteria are measured qualitatively or quantitatively and demonstrated for conditions similar to deployment setting(s)".6  
* **MEASURE 3.1 / 3.2 / 3.3:** "Procedures are established to enable... feedback... to report problems and appeal system outcomes," which are then "integrated into AI system evaluation metrics".6  
* **MEASURE (General):** Critically, the RMF states that these processes must include "associated measures of uncertainty".4

TML Integration: The EUS as the Core Metric of "Trustworthiness":  
TML provides a direct, technical answer to the core challenge of the MEASURE function: how to quantify abstract ethical risks.

1. **The EUS as the MEASURE 1.1 Metric:** The **Ethical Uncertainty Score (EUS)** *is* the "approach and metric" 6 that MEASURE 1.1 demands. It is a quantitative, "risk-sensitive metric" 31 that operationalizes the very concept of "uncertainty" 6 that NIST calls for.  
2. **Extending "Uncertainty":** NIST's traditional guidance on "uncertainty" 47 is often statistical (e.g., standard uncertainties, probability distributions). This is necessary but insufficient for AI. TML introduces a vital, parallel concept: **Normative Uncertainty**.12 This is the measurable ambiguity that arises when:  
   * **Data Insufficiency:** The AI's training data is insufficient to make a normatively-sound decision (e.g., it has no data on a vulnerable population's specific needs).  
   * **Action-Norm Conflict:** The AI's proposed action (the "output") is in *direct semantic conflict* 43 with a legal principle in the normative corpus (Appendices A & B).  
   * **Norm-Norm Conflict:** Two or more legal principles from the corpus are in direct conflict in a given context, creating a true "moral dilemma".48 For example, the "right to privacy" 35 may conflict with a "right to security" in a law enforcement context. TML is designed to *detect* this conflict, not arbitrarily "solve" it.

The EUS quantifies this normative uncertainty, providing a score from 0 to 1\. A low EUS (e.g., 0.1) means the proposed action is normatively clear and maps to no known harms in the corpus. A high EUS (e.g., 0.9) signifies a "hard case" with high semantic conflict, indicating a high probability of legal, ethical, or human rights infringement.

3. **The CQE as the MEASURE 3.0 Feedback Mechanism:** The **Clarifying Question Engine (CQE)** *is* the "procedure... for feedback" and "appeal" required by MEASURE 3.1, 3.2, and 3.3.6 When the EUS *quantifies* uncertainty (the "what"), the CQE *qualifies* it by initiating a dialogue with a human.11 The human's response—the "adjudicated feedback" from GOVERN 5.2 6—is then captured, measured for its impact on reducing the EUS, and immutably logged. This *closes the measurement loop* 11, precisely as MEASURE 3.3 demands, by "integrat\[ing\]" the feedback "into AI system evaluation metrics."

The greatest challenge in "AI ethics" is its "abstract," "qualitative" nature 31, which makes it difficult for engineers and risk managers to act upon. The EU AI Act 48 and other global frameworks 49 are mandating "risk-based approaches," but the *metrics* themselves remain ill-defined.  
TML's EUS cracks this problem. It translates the abstract legal principles of the 46+ documents 9 into a *computable risk score*. For the first time, a Chief Compliance Officer, a General Counsel, or a regulator can set a *quantitative threshold* for ethical risk (e.g., "No autonomous action may be taken for any decision with an EUS \> 0.8"). This makes "ethical risk" 12 a concrete, measurable, and *manageable* Key Performance Indicator (KPI), just like "financial risk" or "system downtime." It satisfies NIST's demand for "quantitative... tools" 6 and moves AI ethics from a "philosophy" discussion to an "engineering" discipline.

### **2.4 MANAGE: Continuous Verification and Cryptographic Oversight**

**NIST Objective (MANAGE):** The MANAGE function "entail\[s\] allocating risk resources to mapped and measured risks".6 This is the operational function that requires continuous monitoring, incident response, and proof of mitigation. Key subcategories include:

* **MANAGE 1.2:** "Processes and resources are in place for risk treatment (mitigation) and acceptance".6  
* **MANAGE 1.3:** "Incidents, threats, and events are documented and communicated to the appropriate AI actors".6  
* **MANAGE 2.2:** "AI systems... are subject to continual, routine, and structured monitoring, maintenance, and update processes".6  
* **MANAGE (General):** This function implies a robust system for "log management" 15 and "continuous monitoring" 17 to ensure deployed systems remain compliant and safe.

TML Integration: The Verifiable "Flight Data Recorder" for AI:  
TML's architecture provides a closed-loop, verifiable system for managing risk, moving beyond simple "log collection" to cryptographic proof of compliance.

1. Immutable Moral Trace Logs as the MANAGE 1.3 Solution: The TML logs are the definitive documentation for MANAGE 1.3.6 A standard system log (e.g., syslog, application log) is insufficient for "forensic analysis" 51 of an ethical failure. It records what the system did, but not what it considered, why it was uncertain, or what deliberative process occurred.  
   The Immutable Moral Trace Log is a "record of events" 15 designed specifically for ethical and legal auditing. Each log entry is a comprehensive data packet that contains:  
   * The *proposed* action (the AI's initial intent).  
   * The *EUS score* (the quantified risk measurement).  
   * The *specific vectors* from the Normative Corpus (Appendices A & B) that were triggered.  
   * The *activation* of the Sacred Pause (proof of GOVERN 4.1).  
   * The *specific question(s)* asked by the CQE (proof of GOVERN 5.2).  
   * The *human's response* and time-stamped justification (the "adjudicated feedback").  
   * The final "risk treatment" decision (mitigation, acceptance, or avoidance) (proof of MANAGE 1.2).  
     This log is not a byproduct; it is the purpose of the TML architecture. It is a "flight data recorder" for AI ethics.  
2. **The Hybrid Shield as the MANAGE 2.2 Enforcer:** A log is forensically useless if it can be tampered with. An internal-only log can be altered or deleted by a bad actor or a compromised system. The **Hybrid Shield** 13 is TML's security architecture that makes the "Moral Trace Logs" *immutable*. It provides a hybrid defense 13:  
   * **Institutional Redundancy:** Logs are mirrored across firewalled, operationally independent institutional siloes (e.g., Legal, Compliance, and Engineering).  
   * Mathematical Redundancy: Cryptographic hashes (e.g., $SHA-256$) of the logs are anchored to multiple, heterogeneous public blockchains or distributed ledgers.  
     This combination provides cryptographic proof 16 that the "Immutable Moral Trace Log" is authentic and has not been altered post-facto. This is the only way to create a truly verifiable audit trail that can withstand legal and regulatory scrutiny.  
3. **The Continuous Audit Cycle:** The combination of the EUS as a real-time risk *threshold* 52 and the *immutable log* 15 creates the "continual, routine, and structured monitoring" system that MANAGE 2.2 6 demands. The system is *always* monitoring its own *normative uncertainty*. This creates a "continuous monitoring strategy" 17 that is automated, verifiable, and running at all times.

The current paradigm for AI auditing is *post-hoc* and *forensic*. An incident happens, a "high-risk" event is identified 51, and auditors are sent in to "reconstruct" the event from disparate "log data".15 This is a fundamentally broken model. TML's Log \+ Shield architecture changes this paradigm from *post-hoc forensic auditing* to *contemporaneous assurance*. The audit trail is built *as the decision is being made*. The "Immutable Moral Trace Log" is not just a "log"—it is a *verifiable asset* that *proves* the governance process (Part 2.1), the risk-mapping (Part 2.2), and the measurement (Part 2.3) were all executed for that specific decision. This proves compliance with the *entire* NIST RMF in a single, cryptographically secure, and time-stamped data packet. This is the *only* viable path to real, scalable, and provable accountability for advanced AI systems.  
---

## **Part III: Conclusion: From Risk Management Culture to Risk Accountability Architecture**

This whitepaper has demonstrated that the NIST AI Risk Management Framework provides the essential, globally-recognized *goals* for trustworthy AI.1 It correctly identifies the core functions of **Govern, Map, Measure, and Manage**. However, its "voluntary" 2 nature, which relies on organizations to cultivate a "risk culture" 4, creates a critical "implementation deficit".23 This gap leaves organizations exposed to risk and regulators without a means of verification, reducing "accountability" to a "trust claim".6  
Ternary Moral Logic provides the missing *architectural implementation* to bridge this gap. TML is not a competing framework; it is the *enforcement layer* that makes the RMF's goals a technical reality.

* TML fulfills **GOVERN** by hard-wiring a "Sacred Pause" 28 and a "Clarifying Question Engine" 11 into the decision pipeline. This transforms "human oversight" from a "loophole" 23 into a verifiable, "structural accountability" 25 that satisfies GOVERN 3.2 and GOVERN 5.2.  
* TML fulfills **MAP** by using a vast corpus of 46+ international legal documents (Appendices A & B) as its "risk taxonomy".9 This makes the MAP 2.1 function *continuous* and *dynamic* 18, driven by the "Ethical Uncertainty Score" (EUS).  
* TML fulfills **MEASURE** by defining the "EUS" as the *quantitative metric* for "normative uncertainty".4 This makes abstract ethical risk a computable, measurable KPI 12, satisfying MEASURE 1.1.  
* TML fulfills **MANAGE** by producing "Immutable Moral Trace Logs" 15 protected by a "Hybrid Shield".13 This creates a cryptographically verifiable "flight data recorder" for continuous, automated auditing 52, satisfying MANAGE 1.3 and MANAGE 2.2.

Where NIST *asks* institutions to be trustworthy 3, TML provides the mechanism that *makes* trust measurable. It is the architectural bridge that moves the global AI industry from a voluntary "risk management culture" to a verifiable, enforceable "risk accountability architecture." This provides a definitive, defensible, and implementation-ready pathway for any organization seeking to prove, with cryptographic certainty, its commitment to safe and responsible AI.  
---

## **Part IV: Appendices (The Normative Foundation)**

The following tables constitute the foundational "ethical taxonomy" referenced by the TML architecture. This corpus is the ground truth for the **MAP** function's identification of harm 6 and the **MEASURE** function's calculation of the Ethical Uncertainty Score (EUS).6 This approach aligns with global calls for human rights-based risk assessments.9

### **Appendix A: The Human Rights Corpus (Taxonomy of Individual & Group Harm)**

This corpus of 27 documents provides the normative basis for MAP 2.1's requirement to identify "harms to individuals, groups, organizations, \[and\] communities."

| Category | Document |
| :---- | :---- |
| **The International Bill of Human Rights** | 1\. Universal Declaration of Human Rights (UDHR) 34 |
|  | 2\. International Covenant on Civil and Political Rights (ICCPR) 32 |
|  | 3\. International Covenant on Economic, Social and Cultural Rights (ICESCR) 32 |
| **Core UN Treaties (The "Big Nine")** | 4\. International Convention on the Elimination of All Forms of Racial Discrimination (ICERD) 32 |
|  | 5\. Convention on the Elimination of All Forms of Discrimination against Women (CEDAW) 32 |
|  | 6\. Convention against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment (CAT) 32 |
|  | 7\. Convention on the Rights of the Child (CRC) 33 |
|  | 8\. International Convention on the Protection of the Rights of All Migrant Workers and Members of Their Families (ICMW) 33 |
|  | 9\. Convention on the Rights of Persons with Disabilities (CRPD) 33 |
|  | 10\. International Convention for the Protection of All Persons from Enforced Disappearance (CPED) 55 |
| **Key Optional Protocols** | 11\. Optional Protocol to the ICCPR (on complaints) 56 |
|  | 12\. Second Optional Protocol to the ICCPR (on abolition of death penalty) 56 |
|  | 13\. Optional Protocol to the ICESCR 55 |
|  | 14\. Optional Protocol to CEDAW 58 |
|  | 15\. Optional Protocol to CAT 58 |
|  | 16\. Optional Protocol to the CRC (on involvement of children in armed conflict) 58 |
|  | 17\. Optional Protocol to the CRC (on the sale of children, child prostitution and child pornography) 58 |
|  | 18\. Optional Protocol to the CRC (on a communications procedure) 56 |
|  | 19\. Optional Protocol to CRPD 33 |
| **Foundational Declarations & Conventions** | 20\. Convention on the Prevention and Punishment of the Crime of Genocide (Genocide Convention) 33 |
|  | 21\. Convention relating to the Status of Refugees (Refugee Convention) 33 |
|  | 22\. Declaration on the Rights of Indigenous Peoples (UNDRIP) 32 |
|  | 23\. Vienna Declaration and Programme of Action 32 |
|  | 24\. Beijing Declaration and Platform for Action 32 |
|  | 25\. Declaration of the Rights of the Child 32 |
|  | 26\. Declaration on the Rights of Disabled Persons 32 |
|  | 27\. Declaration on the Right to Development 32 |

### **Appendix B: The Earth Protection Corpus (Taxonomy of Societal & Environmental Harm)**

This corpus of 26 documents provides the normative basis for MAP 2.1's requirement to identify "harms to... society, the environment, and the planet."

| Category | Document |
| :---- | :---- |
| **The Rio Conventions (The "Big Three")** | 1\. United Nations Framework Convention on Climate Change (UNFCCC) 37 |
|  | 2\. Convention on Biological Diversity (CBD) 37 |
|  | 3\. United Nations Convention to Combat Desertification (UNCCD) 38 |
| **Foundational UN Declarations** | 4\. Rio Declaration on Environment and Development 60 |
|  | 5\. Agenda 21 (Global Programme of Action on Sustainable Development) 60 |
|  | 6\. Declaration of the United Nations Conference on the Human Environment (Stockholm Declaration) 60 |
| **Major Climate Agreements** | 7\. The Paris Agreement 37 |
|  | 8\. Kyoto Protocol 37 |
| **Atmosphere & Ozone Protection** | 9\. Vienna Convention for the Protection of the Ozone Layer 38 |
|  | 10\. Montreal Protocol on Substances that Deplete the Ozone Layer 37 |
|  | 11\. Convention on Long-range Transboundary Air Pollution (LRTAP) 38 |
| **Chemicals & Waste Management** | 12\. Stockholm Convention on Persistent Organic Pollutants (POPs) 37 |
|  | 13\. Basel Convention on the Control of Transboundary Movements of Hazardous Wastes 37 |
|  | 14\. Minamata Convention on Mercury 38 |
|  | 15\. Rotterdam Convention (on Prior Informed Consent \- PIC) 66 |
| **Biodiversity & Natural Heritage** | 16\. Convention on International Trade in Endangered Species (CITES) 37 |
|  | 17\. Ramsar Convention on Wetlands 37 |
|  | 18\. Convention on Migratory Species (Bonn Convention) 41 |
|  | 19\. UNESCO Convention Concerning the Protection of the World Cultural and Natural Heritage 60 |
| **Marine & Water Protection** | 20\. United Nations Convention on the Law of the Sea (UNCLOS) 37 |
|  | 21\. International Convention for the Prevention of Pollution from Ships (MARPOL 73/78) 45 |
|  | 22\. London Convention (on Ocean Dumping) 45 |
|  | 23\. Cartagena Convention (for the Protection and Development of the Marine Environment of the Wider Caribbean Region) 45 |
| **Cross-Cutting Frameworks** | 24\. Sendai Framework for Disaster Risk Reduction 60 |
|  | 25\. Addis Ababa Action Agenda (on financing for development) 60 |
|  | 26\. Transforming our world: the 2030 Agenda for Sustainable Development (SDGs) 60 |

#### **Works cited**

1. AI Risk Management Framework | NIST \- National Institute of Standards and Technology, accessed November 11, 2025, [https://www.nist.gov/itl/ai-risk-management-framework](https://www.nist.gov/itl/ai-risk-management-framework)  
2. Artificial Intelligence Risk Management Framework (AI RMF 1.0) | NIST, accessed November 11, 2025, [https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10)  
3. Understanding the NIST AI Risk Management Framework: A complete guide \- Thoropass, accessed November 11, 2025, [https://www.thoropass.com/blog/nist-ai-rmf](https://www.thoropass.com/blog/nist-ai-rmf)  
4. The National Institute of Standards and Technology (NIST) Artificial Intelligence Risk Management | TrustArc, accessed November 11, 2025, [https://trustarc.com/regulations/nist-ai-rmf/](https://trustarc.com/regulations/nist-ai-rmf/)  
5. NIST AI Risk Management Framework (RMF 1.0) \- Digital Government Hub, accessed November 11, 2025, [https://digitalgovernmenthub.org/library/nist-ai-risk-management-framework/](https://digitalgovernmenthub.org/library/nist-ai-risk-management-framework/)  
6. Artificial Intelligence Risk Management Framework (AI RMF 1.0) \- NIST Technical Series Publications, accessed November 11, 2025, [https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)  
7. NIST AI Risk Management Framework (AI RMF) \- Palo Alto Networks, accessed November 11, 2025, [https://www.paloaltonetworks.com/cyberpedia/nist-ai-risk-management-framework](https://www.paloaltonetworks.com/cyberpedia/nist-ai-risk-management-framework)  
8. (PDF) Designing Meaningful Human Oversight in AI \- ResearchGate, accessed November 11, 2025, [https://www.researchgate.net/publication/395540553\_Designing\_Meaningful\_Human\_Oversight\_in\_AI](https://www.researchgate.net/publication/395540553_Designing_Meaningful_Human_Oversight_in_AI)  
9. Risk Management Profile for Artificial Intelligence and Human Rights \- State Department, accessed November 11, 2025, [https://2021-2025.state.gov/risk-management-profile-for-ai-and-human-rights/](https://2021-2025.state.gov/risk-management-profile-for-ai-and-human-rights/)  
10. How to Implement NIST AI RMF for Enterprises: A Practical Guide \- Net Solutions, accessed November 11, 2025, [https://www.netsolutions.com/insights/nist-ai-rmf-case-study/](https://www.netsolutions.com/insights/nist-ai-rmf-case-study/)  
11. Constructing Ethical AI Based on the “Human-in-the-Loop” System \- MDPI, accessed November 11, 2025, [https://www.mdpi.com/2079-8954/11/11/548](https://www.mdpi.com/2079-8954/11/11/548)  
12. Common ethical challenges in AI \- Human Rights and Biomedicine \- The Council of Europe, accessed November 11, 2025, [https://www.coe.int/en/web/human-rights-and-biomedicine/common-ethical-challenges-in-ai](https://www.coe.int/en/web/human-rights-and-biomedicine/common-ethical-challenges-in-ai)  
13. Advancements in cache management: a review of machine learning innovations for enhanced performance and security \- Frontiers, accessed November 11, 2025, [https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1441250/full](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1441250/full)  
14. Applied Machine Learning for Analyzing and Defending against Side Channel Threats \- eScholarship, accessed November 11, 2025, [https://escholarship.org/content/qt43v6p8c5/qt43v6p8c5\_noSplash\_0d981228d41c61be89ae290622868e45.pdf](https://escholarship.org/content/qt43v6p8c5/qt43v6p8c5_noSplash_0d981228d41c61be89ae290622868e45.pdf)  
15. NIST SP 800-92r1 initial public draft, Cybersecurity Log Management Planning Guide, accessed November 11, 2025, [https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-92r1.ipd.pdf](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-92r1.ipd.pdf)  
16. Mitigating Artificial Intelligence (AI) Risk: Safety and Security Guidelines for Critical Infrastructure Owners and Operators, accessed November 11, 2025, [https://www.dhs.gov/sites/default/files/2024-04/24\_0426\_dhs\_ai-ci-safety-security-guidelines-508c.pdf](https://www.dhs.gov/sites/default/files/2024-04/24_0426_dhs_ai-ci-safety-security-guidelines-508c.pdf)  
17. Defense Counterintelligence and Security Agency Assessment and Authorization Process Manual, accessed November 11, 2025, [https://www.dcsa.mil/Portals/91/Documents/CTP/tools/DCSA%20Assessment%20and%20Authorization%20Process%20Manual%20Version%202.2.pdf](https://www.dcsa.mil/Portals/91/Documents/CTP/tools/DCSA%20Assessment%20and%20Authorization%20Process%20Manual%20Version%202.2.pdf)  
18. Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile \- NIST Technical Series Publications, accessed November 11, 2025, [https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)  
19. NIST AI Risk Management Framework: A tl;dr \- Wiz, accessed November 11, 2025, [https://www.wiz.io/academy/nist-ai-risk-management-framework](https://www.wiz.io/academy/nist-ai-risk-management-framework)  
20. AI Risk Management Framework: Second Draft \- August 18, 2022 \- National Institute of Standards and Technology, accessed November 11, 2025, [https://www.nist.gov/document/ai-risk-management-framework-2nd-draft](https://www.nist.gov/document/ai-risk-management-framework-2nd-draft)  
21. AI Risk: Evaluating and Managing It Using the NIST Framework | Skadden, accessed November 11, 2025, [https://www.skadden.com/insights/publications/2023/05/evaluating-and-managing-ai-risk-using-the-nist-framework](https://www.skadden.com/insights/publications/2023/05/evaluating-and-managing-ai-risk-using-the-nist-framework)  
22. Human in the Loop: Ensuring Accuracy and Ethics in AI Systems \- Openxcell, accessed November 11, 2025, [https://www.openxcell.com/blog/human-in-the-loop/](https://www.openxcell.com/blog/human-in-the-loop/)  
23. Uploaded by: Katie Fry Hester Position: FAV \- Maryland, accessed November 11, 2025, [https://mgaleg.maryland.gov/cmte\_testimony/2025/fin/27141\_02262025\_91540-65.pdf](https://mgaleg.maryland.gov/cmte_testimony/2025/fin/27141_02262025_91540-65.pdf)  
24. Governable AI: Provable Safety Under Extreme Threat Models \- arXiv, accessed November 11, 2025, [https://arxiv.org/html/2508.20411v1](https://arxiv.org/html/2508.20411v1)  
25. Governing Advanced AI: Conceptual Frameworks for Self-Modification Defence, Alignment, and Transparent Oversight \- Figshare, accessed November 11, 2025, [https://figshare.com/articles/thesis/Governing\_Advanced\_Artificial\_Intelligence\_The\_SMD\_I-HVAGI\_and\_PD-TU\_Frameworks\_for\_Asymptotic\_Safety\_Verifiable\_Self-Modification\_and\_Computational\_Due\_Process/29235719](https://figshare.com/articles/thesis/Governing_Advanced_Artificial_Intelligence_The_SMD_I-HVAGI_and_PD-TU_Frameworks_for_Asymptotic_Safety_Verifiable_Self-Modification_and_Computational_Due_Process/29235719)  
26. NIST AI Risk Management Framework (AI RMF 1.0) Explained \- Securiti, accessed November 11, 2025, [https://securiti.ai/nist-ai-risk-management-framework/](https://securiti.ai/nist-ai-risk-management-framework/)  
27. Implementing the NIST Artificial Intelligence Risk Management Framework – Govern, accessed November 11, 2025, [https://angle.ankura.com/post/102j119/implementing-the-nist-artificial-intelligence-risk-management-framework-govern](https://angle.ankura.com/post/102j119/implementing-the-nist-artificial-intelligence-risk-management-framework-govern)  
28. FractonicMind/TernaryMoralLogic: Implementing Ethical ... \- GitHub, accessed November 11, 2025, [https://github.com/FractonicMind/TernaryMoralLogic](https://github.com/FractonicMind/TernaryMoralLogic)  
29. Improving Alignment and Robustness with Circuit Breakers \- arXiv, accessed November 11, 2025, [https://arxiv.org/html/2406.04313v2](https://arxiv.org/html/2406.04313v2)  
30. Improving AI Cybersecurity using Circuit Breakers | by Valdez Ladd | Medium, accessed November 11, 2025, [https://medium.com/@oracle\_43885/improving-ai-cybersecurity-using-short-circuit-breakers-df7dbeeaddcf](https://medium.com/@oracle_43885/improving-ai-cybersecurity-using-short-circuit-breakers-df7dbeeaddcf)  
31. Assessing Human Rights Risks in AI: A Framework for Model Evaluation \- arXiv, accessed November 11, 2025, [https://arxiv.org/html/2510.05519v1](https://arxiv.org/html/2510.05519v1)  
32. International human rights instruments \- Wikipedia, accessed November 11, 2025, [https://en.wikipedia.org/wiki/International\_human\_rights\_instruments](https://en.wikipedia.org/wiki/International_human_rights_instruments)  
33. Human Rights Treaties, accessed November 11, 2025, [https://www.humanrightscommission.ky/human-rights-treaties](https://www.humanrightscommission.ky/human-rights-treaties)  
34. Universal Declaration of Human Rights \- the United Nations, accessed November 11, 2025, [https://www.un.org/en/about-us/universal-declaration-of-human-rights](https://www.un.org/en/about-us/universal-declaration-of-human-rights)  
35. Human Rights \- the United Nations, accessed November 11, 2025, [https://www.un.org/en/global-issues/human-rights](https://www.un.org/en/global-issues/human-rights)  
36. The United Nations Human Rights Treaty System, accessed November 11, 2025, [https://humanrights.gov.au/sites/default/files/content/social\_justice/international\_docs/pdf/factsheet\_on\_treatysystem.pdf](https://humanrights.gov.au/sites/default/files/content/social_justice/international_docs/pdf/factsheet_on_treatysystem.pdf)  
37. Key International Environmental Agreements to Know for Environmental Policy and Law, accessed November 11, 2025, [https://fiveable.me/lists/key-international-environmental-agreements](https://fiveable.me/lists/key-international-environmental-agreements)  
38. List of international environmental agreements \- Wikipedia, accessed November 11, 2025, [https://en.wikipedia.org/wiki/List\_of\_international\_environmental\_agreements](https://en.wikipedia.org/wiki/List_of_international_environmental_agreements)  
39. United Nations Framework Convention on Climate Change | UNFCCC, accessed November 11, 2025, [https://unfccc.int/process-and-meetings/united-nations-framework-convention-on-climate-change](https://unfccc.int/process-and-meetings/united-nations-framework-convention-on-climate-change)  
40. United Nations Framework Convention on Climate Change \- Wikipedia, accessed November 11, 2025, [https://en.wikipedia.org/wiki/United\_Nations\_Framework\_Convention\_on\_Climate\_Change](https://en.wikipedia.org/wiki/United_Nations_Framework_Convention_on_Climate_Change)  
41. Multilateral actions to safeguard the environment: A timeline \- UNEP, accessed November 11, 2025, [https://www.unep.org/multilateral-actions-safeguard-environment-timeline](https://www.unep.org/multilateral-actions-safeguard-environment-timeline)  
42. The Rio Conventions | UNFCCC, accessed November 11, 2025, [https://unfccc.int/process-and-meetings/the-rio-conventions](https://unfccc.int/process-and-meetings/the-rio-conventions)  
43. Measurement of Text Similarity: A Survey \- MDPI, accessed November 11, 2025, [https://www.mdpi.com/2078-2489/11/9/421](https://www.mdpi.com/2078-2489/11/9/421)  
44. Document Processing: Methods for Semantic Text Similarity Analysis \- ResearchGate, accessed November 11, 2025, [https://www.researchgate.net/publication/344243591\_Document\_Processing\_Methods\_for\_Semantic\_Text\_Similarity\_Analysis](https://www.researchgate.net/publication/344243591_Document_Processing_Methods_for_Semantic_Text_Similarity_Analysis)  
45. Selected Multilateral Environmental Instruments In Force for the U.S. | US EPA, accessed November 11, 2025, [https://www.epa.gov/international-cooperation/selected-multilateral-environmental-instruments-force-us](https://www.epa.gov/international-cooperation/selected-multilateral-environmental-instruments-force-us)  
46. Mastering ethical AI: Unpacking NIST's game-changing risk framework \- Polymer DLP, accessed November 11, 2025, [https://www.polymerhq.io/blog/generative-ai/mastering-ethical-ai-unpacking-nists-game-changing-risk-framework/](https://www.polymerhq.io/blog/generative-ai/mastering-ethical-ai-unpacking-nists-game-changing-risk-framework/)  
47. Simple Guide for Evaluating and Expressing the Uncertainty of NIST Measurement Results, accessed November 11, 2025, [https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.1900.pdf](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.1900.pdf)  
48. Navigating Artificial Intelligence from a Human Rights Lens \- Geneva Graduate Institute, accessed November 11, 2025, [https://www.graduateinstitute.ch/sites/internet/files/2023-09/AI%26HR%20Final%20Report%20-%20Publication.pdf](https://www.graduateinstitute.ch/sites/internet/files/2023-09/AI%26HR%20Final%20Report%20-%20Publication.pdf)  
49. Ethical Framework to Assess and Quantify the Trustworthiness of Artificial Intelligence Techniques: Application Case in Remote Sensing \- MDPI, accessed November 11, 2025, [https://www.mdpi.com/2072-4292/16/23/4529](https://www.mdpi.com/2072-4292/16/23/4529)  
50. COMMITTEE ON ARTIFICIAL INTELLIGENCE (CAI) \- https: //rm. coe. int, accessed November 11, 2025, [https://rm.coe.int/cai-2024-16rev2-methodology-for-the-risk-and-impact-assessment-of-arti/1680b2a09f](https://rm.coe.int/cai-2024-16rev2-methodology-for-the-risk-and-impact-assessment-of-arti/1680b2a09f)  
51. Rev. 5 AI-RMF Mapping \- Regulations.gov, accessed November 11, 2025, [https://downloads.regulations.gov/NIST-2024-0001-0048/attachment\_1.xlsx](https://downloads.regulations.gov/NIST-2024-0001-0048/attachment_1.xlsx)  
52. Secure Software Development Practices for Generative AI and Dual-Use Foundation Models: An SSDF Community Profile \- NIST Technical Series Publications, accessed November 11, 2025, [https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf)  
53. Topology Poisoning Attacks and Prevention in Hybrid Software-Defined Networks | Request PDF \- ResearchGate, accessed November 11, 2025, [https://www.researchgate.net/publication/354263430\_Topology\_Poisoning\_Attacks\_and\_Prevention\_in\_Hybrid\_Software-Defined\_Networks](https://www.researchgate.net/publication/354263430_Topology_Poisoning_Attacks_and_Prevention_in_Hybrid_Software-Defined_Networks)  
54. Advancements in cache management: a review of machine learning innovations for enhanced performance and security \- NIH, accessed November 11, 2025, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11893820/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11893820/)  
55. The Core International Human Rights Instruments and their monitoring bodies | OHCHR, accessed November 11, 2025, [https://www.ohchr.org/en/core-international-human-rights-instruments-and-their-monitoring-bodies](https://www.ohchr.org/en/core-international-human-rights-instruments-and-their-monitoring-bodies)  
56. \- OHCHR Dashboard, accessed November 11, 2025, [https://indicators.ohchr.org/](https://indicators.ohchr.org/)  
57. CHAPTER IV : Human Rights \- UNTC, accessed November 11, 2025, [https://treaties.un.org/pages/treaties.aspx?id=4\&subid=A\&lang=en](https://treaties.un.org/pages/treaties.aspx?id=4&subid=A&lang=en)  
58. The Core International Human Rights Treaties \- ohchr, accessed November 11, 2025, [https://www.ohchr.org/documents/publications/coretreatiesen.pdf](https://www.ohchr.org/documents/publications/coretreatiesen.pdf)  
59. International Human Rights Treaties | ILGA World Database, accessed November 11, 2025, [https://database.ilga.org/international-human-rights-treaties](https://database.ilga.org/international-human-rights-treaties)  
60. Major Agreements & Conventions .:. Sustainable Development Knowledge Platform, accessed November 11, 2025, [https://sustainabledevelopment.un.org/index.php?menu=122](https://sustainabledevelopment.un.org/index.php?menu=122)  
61. The Rio Earth Summit: summary of the United Nations conference on Environment and Development (BP-317E) \- à www.publications.gc.ca, accessed November 11, 2025, [https://publications.gc.ca/Pilot/LoPBdP/BP/bp317-e.htm](https://publications.gc.ca/Pilot/LoPBdP/BP/bp317-e.htm)  
62. United Nations Conference on Environment & Development, accessed November 11, 2025, [https://sustainabledevelopment.un.org/content/documents/Agenda21.pdf](https://sustainabledevelopment.un.org/content/documents/Agenda21.pdf)  
63. The Paris Agreement | UNFCCC, accessed November 11, 2025, [https://unfccc.int/process-and-meetings/the-paris-agreement](https://unfccc.int/process-and-meetings/the-paris-agreement)  
64. Paris to Kyoto: The History of UN Climate Agreements | Council on Foreign Relations, accessed November 11, 2025, [https://www.cfr.org/backgrounder/paris-global-climate-change-agreements](https://www.cfr.org/backgrounder/paris-global-climate-change-agreements)  
65. History of the Convention \- UNFCCC, accessed November 11, 2025, [https://unfccc.int/process/the-convention/history-of-the-convention](https://unfccc.int/process/the-convention/history-of-the-convention)  
66. Multilateral Environmental Agreements (MEAs) \- Environment \- European Commission, accessed November 11, 2025, [https://environment.ec.europa.eu/international-cooperation/multilateral-environmental-agreements-meas\_en](https://environment.ec.europa.eu/international-cooperation/multilateral-environmental-agreements-meas_en)  
67. List of Major Environmental Treaties, Rules, and Other Initiatives that Lindy Johnson Played a Key Role in Shaping \- NOAA, accessed November 11, 2025, [https://www.gc.noaa.gov/documents/gcil\_lindy\_summary.pdf](https://www.gc.noaa.gov/documents/gcil_lindy_summary.pdf)
