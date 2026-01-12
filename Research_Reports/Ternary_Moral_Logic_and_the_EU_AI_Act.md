# **Ternary Moral Logic (TML) and the EU AI Act: A Technical Backbone for Enforceable Accountability**

**Author:** Lev Goukassian  
**Affiliation:** Independent Researcher  
**Contact:** leogouk@gmail.com  
**Keywords:** AI Governance, EU AI Act, Accountability, Sacred Pause, Ternary Moral Logic, Ethics, Auditable AI, Immutable Logs

### 

### **Abstract**

**[Interactive Webpage and Audio Overview](https://fractonicmind.github.io/TernaryMoralLogic/Research_Reports/Ternary_Moral_Logic_and_the_EU_AI_Act.html)**

The European Union's Artificial Intelligence Act (AI Act) represents a landmark regulatory effort to establish a global standard for trustworthy AI, mandating robust risk management, data governance, transparency, and human oversight for high-risk systems. However, the Act primarily relies on procedural compliance and *post-hoc* auditing, creating a significant gap between legal intent and technical enforcement. This paper introduces Ternary Moral Logic (TML) as a novel governance architecture that provides a verifiable, *proactive*, and machine-enforced backbone for the Act's requirements. TML’s three-state logic (Permissible, Impermissible, Indeterminate) enforces a mandatory "Sacred Pause" (State 0\) when an AI system confronts ethical or operational uncertainty that exceeds a quantifiable threshold. We analyze how this architecture directly operationalizes the mandates of EU AI Act Articles 9 through 15\. TML’s Sacred Pause provides the enforceable "effective oversight" required by Article 14, while its cryptographically secured, Immutable Moral Trace Logs fulfill the record-keeping and transparency mandates of Articles 12 and 10 with a degree of integrity conventional logging cannot match. We argue that TML shifts the paradigm from asserting compliance via documentation to proving it with an immutable, real-time audit trail, offering a technical prototype for the future of enforceable AI governance.

### **I. Introduction**

The European Union's Regulation on Artificial Intelligence (EU AI Act) is poised to become the global benchmark for AI governance \[1\]. By establishing a risk-based framework, the Act imposes stringent legal and ethical obligations on systems deemed "high-risk," including those used in critical infrastructure, law enforcement, and medical devices. The Act's core ambition is to ensure that AI systems placed on the Union market are safe, transparent, non-discriminatory, and subject to meaningful human oversight.  
A critical challenge, however, lies in the Act's implementation. The primary compliance mechanisms detailed in the legislation rely heavily on *post-hoc* conformity assessments, technical documentation, and post-market surveillance \[2\]. While necessary, these measures are procedural and retroactive. They verify that a process was *claimed* to be followed but lack the technical teeth to enforce compliance at the moment of computation. This creates a critical gap: how can regulators, users, and operators be certain that an AI system, in a novel, real-world scenario, is *actually* adhering to its documented risk management policies and "human-in-the-loop" safeguards?  
This paper argues that this gap between legal principle and technical reality can be bridged by a new class of "governance-native" architectures. We present Ternary Moral Logic (TML) as a foundational framework designed specifically to provide verifiable, real-time, and enforceable accountability \[3\]. TML is a safety and governance overlay that reframes an AI’s decision-making process. Instead of a conventional binary (allow/deny) output, TML operates on three states:

1. **Permissible (State 1):** The action is safe and aligned with its objectives.  
2. **Impermissible (State 2):** The action is harmful or violates defined constraints.  
3. **Indeterminate (State 0):** The system's ethical or operational uncertainty exceeds a predefined threshold, mandating a "Sacred Pause."

The central thesis of this paper is that TML’s architecture, particularly its mandatory Sacred Pause and its Immutable Moral Trace Logs, provides the technical backbone to operationalize the EU AI Act’s most critical requirements for high-risk systems. It transforms abstract legal mandates for transparency (Art. 10), record-keeping (Art. 12), and human oversight (Art. 14\) into verifiable, auditable, and enforceable system behaviors. This paper will first provide a background on the relevant EU AI Act provisions and the TML framework, followed by a direct analysis mapping TML's components to these articles. We will then discuss how this approach enables a proactive auditing model that supersedes post-hoc compliance, before concluding on TML's role as a governance prototype.

### **II. Background**

#### **A. The EU AI Act's High-Risk Mandates (Articles 9-15)**

The EU AI Act’s rigor is concentrated in Title III, Chapter 2, which outlines the obligations for high-risk AI systems. These articles collectively form a blueprint for trustworthy AI, though they remain largely procedural.

* **Article 9 (Risk management system):** Mandates a "continuous iterative process" for risk identification, analysis, and mitigation throughout the AI's lifecycle.  
* **Article 10 (Data and data governance):** Requires high-quality, representative training data and processes to detect and mitigate bias.  
* **Article 12 (Record-keeping):** Requires high-risk systems to be capable of "automatically generating logs" of their operation to ensure traceability.  
* **Article 13 (Transparency and provision of information):** Obligates providers to furnish users with clear information on the system's capabilities, limitations, and the logic of its decisions.  
* **Article 14 (Human oversight):** This is a cornerstone provision, requiring that high-risk systems be designed to "be effectively overseen by natural persons." This includes the ability for a human to "intervene in the operation of the system or to interrupt... its operation through a 'stop' button or a similar procedure."

The overarching challenge of these articles is their reliance on the provider's diligence and the auditor's ability to reconstruct events from documentation. The Act mandates a "stop" button but cannot, by text alone, mandate the wisdom to know *when* to press it.

#### **B. Ternary Moral Logic (TML) Architecture**

TML is an open-source governance framework designed to enforce ethics and safety, not as a post-processing filter, but as a core part of the system's operational logic \[3\]. Its architecture is built upon eight pillars, including the **Goukassian Promise** (a commitment to not be used for weaponry or surveillance) and the integration of foundational legal and ethical texts (the **Human Rights** pillar, based on 26+ instruments, and the **Earth Protection** pillar, based on 20+ instruments) \[4\].

For this analysis, the most relevant components are its core operational mechanics:

1. **Ethical Uncertainty Score (EUS):** TML continuously measures an AI's proposed action against its ethical and operational constraints. The EUS is a quantifiable metric of the system's uncertainty. A high EUS is generated when a system encounters a novel scenario, conflicting data, or a situation with high potential for bias or harm (as defined by the Human Rights and Earth Protection pillars).  
2. **Sacred Pause (State 0):** When the EUS of a given action exceeds a predefined threshold, TML automatically triggers a "Sacred Pause." This is not merely a "stop" button; it is a mandatory, architectural halt. The system is forbidden from proceeding autonomously and must escalate to a human.  
3. **Clarifying Question Engine (CQE):** During a Sacred Pause, the TML framework generates a human-readable prompt. This CQE prompt explains *why* the system paused (e.g., "Proposed loan denial has high correlation with a protected demographic, risking a biased outcome. Please review.")  
4. **Immutable Moral Trace Logs:** The entire event, from the inputs and the EUS calculation to the CQE prompt and the final human decision, is recorded in a log. This log is cryptographically hashed and anchored to public blockchains via TML's **Hybrid Shield** \[5\]. This makes the record permanent, tamper-proof, and verifiable by any third party, fulfilling the "Always Memory" pillar.  

### **III. Analysis: Mapping TML to EU AI Act Mandates**

TML's architecture provides a direct and verifiable technical implementation for the procedural requirements of Articles 9-15.

#### **A. Article 14: From Human Oversight to Enforceable Intervention**

Article 14's call for "effective" human oversight is the Act's most crucial and, perhaps, most abstract mandate. A passive "stop" button only fulfills this requirement if a human is present, attentive, and possesses the superhuman ability to detect algorithmic error in real time.  
TML operationalizes Article 14 by making the AI system itself the first line of defense.

* **Effective Oversight:** The **Sacred Pause (State 0\)** is the architectural enforcement of Article 14\. It is the system's own "stop" button, triggered automatically by its own quantified uncertainty (the EUS). This *guarantees* that a human is brought into the loop precisely when they are most needed, rather than relying on their constant, fallible vigilance.  
* **Informed Intervention:** The **Clarifying Question Engine (CQE)** provides the context necessary for oversight to be "effective." A human operator presented with a simple "Stop?" prompt is ineffective. An operator presented with a CQE prompt explaining *why* the system is uncertain can make an informed, justifiable decision. This transforms the human from a passive monitor into an active, empowered overseer.

#### **B. Article 12 & 10: From Traceability to Verifiable Truth**

Article 12 demands "record-keeping," and Article 10 demands "transparency." Conventional system logs fulfill a weak version of this; they are often opaque, proprietary, and, most critically, mutable. An administrator can edit, delete, or obscure logs to hide a compliance failure or an adverse event.

TML's logging mechanism provides a solution that is orders of magnitude more robust.

* **Verifiable Record-Keeping (Art. 12):** The **Immutable Moral Trace Logs** are "compliance-grade" by default. Through the **Hybrid Shield** and **Public Blockchain** pillars, TML provides a mathematically verifiable guarantee that the record of an event is complete and unaltered \[5\]. For a regulator conducting a post-incident audit, this is the difference between reviewing a curated, unreliable report and reviewing a definitive, time-stamped, and tamper-proof piece of evidence.  
* **Actionable Transparency (Art. 10):** TML provides transparency at two stages. *In-situ*, the **CQE** provides immediate, plain-language transparency to the user/operator at the moment of uncertainty. *Ex-post*, the **Moral Trace Logs** provide deep, forensic transparency for auditors, regulators, and the public, creating a "glass box" that explains not only what the system did, but *why* it hesitated and *who* made the final call.

#### **C. Article 9 & 13: From Risk Documentation to Continuous Verification**

Article 9 requires a "continuous iterative process" for risk management, and Article 13 requires "technical documentation" to prove it. In practice, this often results in static, pre-deployment risk assessments and documentation that quickly becomes obsolete.

TML transforms this static process into a dynamic, continuous, and self-documenting one.

* **Continuous Risk Management (Art. 9):** The **Ethical Uncertainty Score (EUS)** is the engine of a continuous risk management system. It actively analyzes risk (of bias, harm, or novelty) on a case-by-case basis. The system is not just *assessed* for risk before deployment; it *manages* its own risk in real time.  
* **Living Technical Documentation (Art. 13):** The **Moral Trace Logs** *are* the living technical documentation of the risk management system in action. An auditor does not need to read a 200-page static document describing how the system *should* handle bias; they can instead analyze the immutable logs to see exactly how many times the system *did* detect and escalate potential bias, and how those events were resolved.

### **IV. Discussion: Proactive Auditing vs. Post-Hoc Compliance**

The fundamental difference introduced by TML is the shift from a *post-hoc*, trust-based compliance model to a *proactive*, verifiable auditing model.

The standard EU AI Act model is:

1. **Build:** An organization builds an AI system.  
2. **Assert:** It conducts a conformity assessment and generates documentation (Art. 13\) *asserting* that the system meets the requirements (Art. 9, 10, 14, etc.).  
3. **Deploy:** The system is placed on the market.  
4. **Audit (Post-Hoc):** If an incident occurs, regulators initiate an audit, attempting to reconstruct the event from documentation and conventional logs, which may or may not be complete or truthful.

The TML-enabled model is:

1. **Build:** An organization builds an AI system *with* TML.  
2. **Deploy:** The system operates in the real world.  
3. **Audit (Proactive & Continuous):** The system audits *itself* in real time. Every instance of high uncertainty (a potential risk) *automatically* triggers a halt (Art. 14\) and *automatically* generates an immutable evidentiary log (Art. 12).  
4. **Verify (Post-Hoc):** Regulators do not need to "reconstruct" an incident; they "review" the mathematically guaranteed, verifiable record of it.

This proactive model is enabled by the full integration of TML’s Eight Pillars. The **Human Rights** and **Earth Protection** pillars provide the ethical and legal content for the risk taxonomy. The **Goukassian Promise** defines its non-negotiable ethical boundary. The **Sacred Pause (State 0\)** provides the enforcement mechanism. And the **Moral Trace Logs**, protected by the **Hybrid Shield** and **Public Blockchains**, provide the immutable proof. This creates an architecture where compliance is not an assertion to be proven, but a property to be verified.

### **V. Conclusion**

The EU AI Act provides the essential legal "what" for a future of trustworthy AI. Ternary Moral Logic provides a powerful technical "how." It translates the Act's most critical legal and ethical mandates, for oversight, transparency, and accountability, into verifiable, enforceable, and robust architectural mechanisms.  
By mandating a Sacred Pause in the face of uncertainty, TML provides a structural guarantee of effective human oversight that a simple "stop" button cannot. By generating immutable, cryptographically secured logs, it transforms the ambiguous requirement for "record-keeping" into a system of provable, forensic-grade evidence. This architecture does not replace the need for human judgment or robust regulatory frameworks; rather, it empowers both.  
TML is more than a simple compliance tool. It is a prototype for a new class of "governance-native" systems that are auditable by design. As regulators and societies grapple with how to enforce trust in an increasingly autonomous world, adopting architectures that build accountability into the code itself, moving from "trust us" to "verify us", will be the critical next step. TNext-generation regulations will require next-generation architectures to enforce them, and TML provides a compelling blueprint for that future.

### 

### **References**

\[1\] Regulation of the European Parliament and of the Council on Laying Down Harmonised Rules on Artificial Intelligence (Artificial Intelligence Act), COM(2021) 206 final, Apr. 2021\.  
\[2\] V. T. B. D. D'Avila, "The EU AI Act: A technical-legal analysis of the procedural challenges," Journal of European Law and Technology, vol. 14, no. 2, 2023\.  
\[3\] Ternary Moral Logic Project, "TML: A Verifiable Governance Architecture," TML Project Repository, 2025\. \[Online\]. Available: \[Stable Project URL or DOI\]  
\[4\] Ternary Moral Logic Project, "MANDATORY.md: The 46+ Foundational Instruments," TML Project Repository, 2025\. \[Online\]. Available: \[Stable Project URL or DOI\]  
\[5\] Ternary Moral Logic Project, "Hybrid\_Shield.md: Immutable Log Anchoring," TML Project Repository, 2025\. \[Online\]. Available: \[Stable Project URL or DOI\]  
\[6\] B. Shneiderman, "Human-centered AI: A framework for reliable, safe, and trustworthy systems," IEEE Trans. Technol. Soc., vol. 2, no. 3, pp. 110-125, Aug. 2021\.  
\[7\] F. Pasquale, "The new architectures of accountability," Journal of AI and Law, vol. 1, no. 1, pp. 22-45, 2024\.
