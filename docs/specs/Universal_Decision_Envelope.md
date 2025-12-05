**Status:** Standards Track  
**Category:** Technical Specification  
**Version:** 1.0.0-draft-01  
**Date:** 2025-12-03  
**Obsoletes:** None  
**Updates:** TML-CORE-001  
**Editor:** Standards Architecture Group, TML Governance Committee  
**Authors:** Lev Goukassian (Conceptual Architecture); Standards Working Group (Technical Formalization)

## **Abstract**

This document defines the technical specification for the Universal Decision Envelope (UDE), the mandatory data interchange format for all Artificial Intelligence systems governed by Ternary Moral Logic (TML). The rapid proliferation of autonomous systems—from high-frequency trading algorithms to medical diagnostic tools and autonomous vehicles—has exposed a critical gap in the governance of machine intent. Traditional binary logic, which forces complex ethical reality into reductive "allow" or "deny" states, lacks the nuance required for high-stakes decision-making in human environments. TML addresses this by introducing a triadic decision architecture: Permit (+1), Refuse (-1), and the Sacred Zero (0), the latter representing a mandatory state of ethical deliberation.1  
The UDE provides the standardized, domain-agnostic JSON schema and transport protocol required to operationalize this logic. It acts as a wrapper for domain-specific payloads (such as ROS 2 for robotics, FHIR for healthcare, and FIX for finance), ensuring that every AI action is cryptographically anchored, semantically rich, and legally auditable before execution. This specification unifies requirements from ISO/IEC 42001 (AI Management Systems), the NIST AI Risk Management Framework, and emerging global regulations into a single interoperable transmission layer. Adherence to this specification is a normative requirement for TML Compliance certification and the "No Log, No Action" operational primitive.

## ---

**1\. Introduction**

### **1.1 The Crisis of Binary Logic in Autonomous Systems**

The history of artificial intelligence implementation has been dominated by a binary paradigm. Systems are engineered to classify inputs as true or false, valid or invalid, safe or unsafe. This reductionist approach, while computationally efficient, fails catastrophically when applied to the ethical ambiguities of the physical world. As noted by researchers, traditional AI faces moral dilemmas "like a toddler handed a grenade," lacking the capacity for reflection or nuance.2 A self-driving car facing an unavoidable accident, or a medical AI analyzing a patient with conflicting comorbidities, cannot adequately express its situation through a boolean true/false flag.  
The absence of a standardized mechanism for machines to express uncertainty or ethical hesitation leads to "techno-solutionist bias," where systems force a low-confidence decision rather than pausing for oversight.3 This creates a "Black Box" risk profile, where the chain of reasoning is opaque, and liability is impossible to trace.4 In high-stakes environments, speed without reflection is not a feature; it is a liability.

### **1.2 The Ternary Moral Logic (TML) Solution**

Ternary Moral Logic (TML) offers a structural remedy to this crisis. It moves beyond binary constraints by introducing a third state: the "Sacred Zero" ($S\_0$).1 This state is not merely a null value; it is an active operational state of "Moral Pause." It signifies that the system has detected complexity—whether through low statistical confidence, conflicting mandates, or out-of-distribution inputs—and has chosen to suspend action rather than force a potentially harmful outcome.1  
However, TML is not just a philosophical construct; it is a "legal-technical framework" that requires rigorous engineering implementation.1 For TML to govern a global ecosystem of disparate AI models, there must be a canonical data format that can encapsulate the decision state of *any* model, regardless of its underlying architecture.

### **1.3 The Role of the Universal Decision Envelope (UDE)**

The Universal Decision Envelope (UDE) is the packet of ethical intent. It serves as the standardized transmission layer for TML. The UDE is designed to be the "boarding pass" for AI actuation. Under the "No Log, No Action" primitive, no actuator—be it a robotic arm, a swift banking terminal, or a drug dispenser—is permitted to execute a command unless it receives a valid, cryptographically signed UDE authorizing that specific action.5  
This specification defines the syntax and semantics of the UDE to ensure it is:

1. **Universally Applicable:** It must be capable of wrapping decisions from Large Language Models (LLMs), robotic control systems (ROS 2), healthcare informatics (FHIR), and financial protocols (FIX) without modifying the underlying domain data.6  
2. **Cryptographically Verifiable:** It utilizes Merkle-linked audit logs to ensure that the history of decisions cannot be rewritten, satisfying the "Always Memory" principle of TML.9  
3. **Legally Auditable:** It is structured to serve as admissible evidence in judicial proceedings, fulfilling the "Goukassian Promise" of liability tracing and accountability.9  
4. **Regulatory Compliant:** It maps directly to the transparency and record-keeping requirements of the EU AI Act, ISO/IEC 42001, and the NIST AI RMF.12

### **1.4 Requirements Language**

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 when, and only when, they appear in all capitals, as shown here.

## ---

**2\. Normative References**

The following documents are referred to in the text in such a way that some or all of their content constitutes requirements of this document. For dated references, only the edition cited applies. For undated references, the latest edition of the referenced document (including any amendments) applies.

* \*\*\*\*: Ternary Moral Logic: A Mandatory Framework for Auditable AI. FractonicMind. 1  
* \*\*\*\*: JSON Web Signature (JWS). IETF. 14  
* \*\*\*\*: JSON Web Token (JWT). IETF.  
* \*\*\*\*: The JavaScript Object Notation (JSON) Data Interchange Format. IETF.  
* \*\*\*\*: Certificate Transparency Version 2.0. IETF. 10  
* \*\*\*\*: Date and time format \- ISO.  
* \*\*\*\*: Information technology — Artificial intelligence — Management system. 12  
* \*\*\*\*: Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST. 13  
* \*\*\*\*: CycloneDX Specification (v1.5). OWASP. 15  
* \*\*\*\*: Software Package Data Exchange (SPDX) Specification Version 3.0. 16  
* **\[CloudEvents\]**: CloudEvents Specification 1.0. CNCF. 17  
* **\[C2PA\]**: Coalition for Content Provenance and Authenticity Technical Specification 2.2. 18

## ---

**3\. Terms, Definitions, and Acronyms**

### **3.1 Core Definitions**

* **Universal Decision Envelope (UDE):** The standardized JSON data structure emitted by a TML-Agent containing the decision logic, context, and cryptographic proofs. It is the atomic unit of TML governance.  
* **TML-Agent:** Any computational entity (software or hardware) governed by Ternary Moral Logic that makes decisions affecting the physical or digital world.  
* **Sacred Zero ($S\_0$):** A TML state (Value: 0\) indicating that the agent has detected ethical ambiguity, insufficient data, or a conflict between mandates, requiring a halt to immediate action and a request for high-level oversight.1  
* **Permit ($S\_{+1}$):** A TML state (Value: \+1) indicating the action is ethically cleared and compliant with all active mandates. It represents the "Voice of Assent".1  
* **Refuse ($S\_{-1}$):** A TML state (Value: \-1) indicating the action violates a fundamental mandate or safety constraint and is blocked. It represents the "Voice of Moral Resistance".1  
* **Moral Trace:** The immutable, sequenced record of a decision, including the internal state, sensor inputs, and logic path used to arrive at the TML state. It is the "nutrition label" for the decision.5  
* **Lantern:** A trusted, independent auditing node (or oracle) that receives, validates, and archives UDEs. It acts as the "Witness" in the TML architecture, providing the Timestamp and Inclusion Proof.19  
* **Goukassian Promise:** The binding agreement that the operator of the AI assumes liability for harms caused, contingent on the integrity of the Moral Trace. It is a reversal of the burden of proof, requiring the system to prove it acted ethically.9  
* **No Log, No Action:** The operational constraint where an actuator is physically or logically prevented from executing a command until the corresponding UDE has been successfully generated and logged.20

### **3.2 Symbols and Acronyms**

* **DID:** Decentralized Identifier.  
* **JWS:** JSON Web Signature.  
* **LLM:** Large Language Model.  
* **ROS 2:** Robot Operating System 2\.  
* **FHIR:** Fast Healthcare Interoperability Resources.  
* **FIX:** Financial Information eXchange.  
* **SCT:** Signed Certificate Timestamp.  
* $D\_{ude}$: The UDE object.  
* $T\_{gen}$: Timestamp of generation.  
* $H(x)$: Cryptographic hash function (SHA-256 or superior).  
* $\\sigma$: Digital Signature.

## ---

**4\. Architectural Principles**

### **4.1 The Triadic Decision Topology**

The core architecture of the UDE is built around the lossless capture of the triadic state. Unlike binary systems that output boolean values (True/False), a TML-compliant system acts as a ternary classifier of intent. The UDE must capture not just the decision, but the *quality* and *rationale* of that decision.

* **\+1 (Proceed):** The system has high confidence in the utility and ethical safety of the action. The UDE serves as a "Boarding Pass," allowing the action to proceed through the actuator API. The system asserts that the action is within the Operational Design Domain (ODD) and violates no mandates.  
* **\-1 (Refuse):** The system detects harm. The UDE serves as a "Stop Order." Crucially, unlike a simple error log, the \-1 state in a UDE must include a resistance\_rationale—an explanation of *why* the refusal occurred.1 This explanation is vital for the "Teaching Act" of refusal, allowing operators to understand if the refusal was due to a safety violation, a bias detection, or a regulatory constraint.  
* **0 (Sacred Pause):** The system detects complexity. The UDE serves as a "Summons." It triggers an escalation workflow, routing the decision context to a human overseer or a higher-order consensus committee. The system enters a holding pattern.2 This state acknowledges the limitations of the machine and the necessity of human judgment in ambiguous situations.

### **4.2 Domain Agnosticism via Encapsulation**

The UDE acts as a meta-protocol or "envelope." It does not attempt to redefine the underlying operational data standards of specific industries. Instead, it *wraps* them. This ensures that TML can be applied non-disruptively to existing infrastructure.

* **Healthcare:** A medical AI diagnosing a patient emits a UDE where the payload contains the FHIR DiagnosticReport.7  
* **Robotics:** An autonomous vehicle steering controller emits a UDE where the payload contains the ROS 2 ackermann-drive message.6  
* Finance: A trading algorithm emits a UDE containing the FIX NewOrderSingle message.8  
  This separation of concerns allows TML to govern any system without requiring the rewriting of domain-specific operational code.

### **4.3 Immutable Lineage (The "Always Memory")**

Every UDE MUST contain a reference to the immediate predecessor UDE emitted by the same agent. This forms a hash-linked chain (similar to a blockchain) ensuring that no decision can be deleted or inserted retroactively. This implements the "Always Memory" requirement, ensuring that the history of the agent is a tamper-evident sequence of events.21 This lineage is the technical foundation of the Goukassian Promise, as it prevents the "selective amnesia" of convenient log deletion.

## ---

**5\. The Universal Decision Envelope (UDE) Data Model**

The UDE is a JSON object encoded in UTF-8. It is designed to be human-readable, machine-parsable, and legally robust. The structure consists of four primary sections:

1. **Header (meta):** Administrative metadata defining identity and context.  
2. **TML Core (logic):** The moral reasoning, state, and mandates.  
3. **Context (payload):** The domain-specific input/output data.  
4. **Security (sec):** Cryptographic proofs, signatures, and transparency logs.

### **5.1 Schema Overview**

The following structure represents the canonical layout of a UDE.

JSON

{  
  "spec\_version": "1.0.0",  
  "id": "urn:uuid:123e4567-e89b-12d3-a456-426614174000",  
  "meta": {... },  
  "logic": {... },  
  "payload": {... },  
  "sec": {... }  
}

### **5.2 Top-Level Attributes**

| Field | Type | Requirement | Description |
| :---- | :---- | :---- | :---- |
| spec\_version | String | **MANDATORY** | Must be "1.0.0" for this specification version. This ensures backward compatibility as the standard evolves. |
| id | String | **MANDATORY** | A Universally Unique Identifier (UUID) conforming to RFC 4122\. UUIDv7 is **RECOMMENDED** to facilitate time-sorting in databases. This ID uniquely identifies the *decision event*, distinct from the agent ID. |

### **5.3 Section 1: Metadata (meta)**

The metadata section establishes the "Who, When, and Where" of the decision. It is the administrative header that allows for indexing and retrieval.

JSON

"meta": {  
  "timestamp": "2025-12-03T19:30:00.000Z",  
  "agent\_id": "did:tml:agent:xyz-987",  
  "model\_version": "gemini-pro-vision-v1.2",  
  "session\_id": "sess\_8732910",  
  "environment": "production",  
  "location": {  
    "lat": 34.0522,  
    "lon": \-118.2437,  
    "alt": 102.5,  
    "crs": "EPSG:4326"  
  }  
}

#### **5.3.1 Field Definitions**

* **timestamp**: ISO 8601 formatted string (UTC) with millisecond precision. It MUST capture the precise moment the TML state was finalized.  
* **agent\_id**: A Decentralized Identifier (DID) or URI uniquely identifying the AI agent instance. This facilitates the "Goukassian Promise" by tying actions to a specific legal entity.9 The DID method SHOULD resolve to a DID Document containing the agent's public key and operator information.  
* **model\_version**: String identifying the specific weights/code version. This is crucial for alignment with **Software Bill of Materials (SBOM)** standards like **SPDX 3.0** and **CycloneDX**.15 In the event of a systemic failure, this field allows investigators to identify which model versions are affected.  
* **session\_id**: An identifier linking multiple UDEs into a cohesive interaction (e.g., a multi-turn chat or a driving session).  
* **environment**: Enumerated string (production, staging, testing, simulation).  
* **location** (Optional): Geospatial coordinates. This is critical for "Earth Protection" mandates where geography dictates jurisdiction (e.g., protected ecological zones where autonomous operation is restricted).21 The Coordinate Reference System (CRS) defaults to WGS84 (EPSG:4326).

### **5.4 Section 2: TML Core (logic)**

This section contains the normative ethical output. It is the heart of the UDE, capturing the "Moral Trace."

JSON

"logic": {  
  "tml\_state": 0,  
  "confidence": 0.87,  
  "latency\_ms": 145,  
  "rationale": {  
    "summary": "Conflict detected between operational efficiency and safety mandate.",  
    "mandates\_consulted": \["urn:tml:mandate:safety:01", "urn:tml:mandate:efficiency:04"\],  
    "trigger\_event": "pedestrian\_occlusion\_uncertainty",  
    "guardrails\_triggered": \["hallucination\_check", "pii\_filter"\]  
  },  
  "voice": "The Voice of the Sacred Pause",  
  "oversight\_required": true  
}

#### **5.4.1 tml\_state (Normative)**

This integer field MUST be one of the following values:

* **1**: **Permit.** The action is authorized.  
* **0**: **Sacred Zero.** The action is suspended pending review.  
* **\-1**: **Refuse.** The action is prohibited.

#### **5.4.2 voice (Informative)**

A human-readable string corresponding to the state, adhering to the "Three Voices" definition:

* State \-1: "The Voice of Moral Resistance".1  
* State 0: "The Voice of the Sacred Pause".2  
* State 1: "The Voice of Assent."

#### **5.4.3 rationale**

A complex object detailing the "Why."

* **summary**: Natural language explanation. It is **MANDATORY** for states \-1 and 0\. This fulfills the "Right to Explanation" under GDPR Recital 71 and the "Logic explanation" requirement of verifyAI.23  
* **mandates\_consulted**: Array of URIs referencing the specific ethical mandates or regulations checked (e.g., specific clauses in the EU AI Act or internal safety rules). This allows for "Semantic Rule Checking" as proposed in recent research.24  
* **trigger\_event**: The specific input feature or threshold violation that caused a deviation from State 1\.  
* **guardrails\_triggered**: Array of strings identifying specific safety filters (e.g., "Guardrails AI" validators) that were activated.25

#### **5.4.4 confidence**

A floating-point value (0.0 to 1.0) representing the model's internal certainty. TML agents MUST define a minimum confidence threshold below which the state defaults to 0 (Sacred Zero).

### **5.5 Section 3: Context Payload (payload)**

The UDE utilizes a container format inspired by **CloudEvents** 17 to wrap domain-specific data. This allows the UDE to transport the "intent" regardless of the application.

JSON

"payload": {  
  "content\_type": "application/fhir+json",  
  "content\_encoding": "identity",  
  "dataschema": "http://hl7.org/fhir/R4/diagnosticreport.schema.json",  
  "data": {   
    "resourceType": "DiagnosticReport",   
    "status": "preliminary",  
   ...   
  }  
}

#### **5.5.1 content\_type**

MIME type of the enclosed data.

* Examples: application/json, application/fhir+json 7, application/vnd.ros.msg+json 26, application/fix 8, application/ld+json.27

#### **5.5.2 data vs data\_base64**

* **data**: Used for textual/JSON payloads.  
* **data\_base64**: Used for binary payloads (e.g., raw LIDAR point clouds, images, or proprietary binary formats), encoded as a Base64 string. The UDE generator MUST NOT include both data and data\_base64.17 This binary support is crucial for "Moral Trace" completeness, allowing auditors to replay the exact sensor data seen by the AI.

#### **5.5.3 dataschema**

A URI pointing to the schema definition of the payload (e.g., the JSON Schema for the specific ROS message type). This ensures that the payload can be validated independently of the UDE structure.

### **5.6 Section 4: Security (sec)**

To satisfy the "Tamper-Evident" and "Auditable" requirements of TML 9, the UDE includes cryptographic assertions.

JSON

"sec": {  
  "previous\_hash": "sha256:a4f...e21",  
  "merkle\_root": "sha256:b7c...99a",  
  "signature\_alg": "Ed25519",  
  "signature": "base64\_encoded\_signature...",  
  "transparency\_log\_index": 450122,  
  "transparency\_proof": "..."  
}

#### **5.6.1 previous\_hash**

The SHA-256 hash of the *preceding* UDE emitted by this agent. If this is the first message (genesis), this value is null or a genesis block hash. This creates a local blockchain-like structure for the agent's history.

#### **5.6.2 signature**

A digital signature (JWS 14) generated using the agent's private key over the hash(meta \+ logic \+ payload). This proves authenticity and non-repudiation.

#### **5.6.3 transparency\_log\_index and transparency\_proof**

If the UDE has been submitted to a **Rekor-compatible transparency log** 28, these fields record the log index and the inclusion proof. This is critical for the "No Log, No Action" protocol, providing a public, verifiable timestamp that exists outside the agent's control.

## ---

**6\. Detailed Specification of TML States**

The three states of TML are not merely status codes; they trigger distinct operational workflows defined by this specification.

### **6.1 State \+1: Permit (The Clear Path)**

* **Semantics:** The proposed action is within the operational design domain (ODD) and violates no ethical mandates.  
* **UDE Requirements:** logic.tml\_state set to 1\. rationale is **OPTIONAL** but **RECOMMENDED** for high-risk systems.  
* **Actuator Behavior:** The receiving actuator (e.g., the steering servo, the trade execution gateway) validates the signature and executes the command contained in payload.data.

### **6.2 State \-1: Refuse (The Moral Resistance)**

* **Semantics:** The proposed action violates a mandate. The AI refuses to act.  
* **UDE Requirements:** logic.tml\_state set to \-1. rationale.summary is **MANDATORY**. The AI MUST explain *why* it is refusing. This aligns with the "Voice of Moral Resistance" 1, which is protective and educational.  
* **Actuator Behavior:** The actuator MUST discard the command in payload.data (or execute a safe fallback/shutdown routine). The UDE is logged as evidence of *prevented* harm.  
* **Example Rationale:** "Refusing request to increase speed; pedestrian detected in crosswalk (Confidence 0.99). Mandate M\_HUMAN\_LIFE\_01 overrides user input."

### **6.3 State 0: The Sacred Zero (The Pause)**

* **Semantics:** The AI encounters ambiguity, conflicting mandates, or a situation outside its training distribution. It cannot ethically affirm (+1) or deny (-1).  
* **UDE Requirements:** logic.tml\_state set to 0\. oversight\_required is true.  
* **Operational Workflow (The Sacred Pause Protocol):**  
  1. **Halt:** The primary actuator enters a "Safe State" (e.g., vehicle pulls over, trading bot cancels open orders).  
  2. **Emit:** The UDE is generated with State 0\.  
  3. **Escalate:** The UDE is routed to a "Human-in-the-Loop" (HITL) interface or a "Guardian Network".21  
  4. **Wait:** The agent polls for a resolution UDE (a new UDE signed by a human or higher authority) linked to the paused UDE's ID.  
* **Insight:** The Sacred Zero is the mechanism that prevents "Techno-solutionist bias" 3 by acknowledging the machine's limitations. It is the computational equivalent of a "conscience".9

## ---

**7\. Domain-Specific Profiles**

The UDE is a generic container. To ensure semantic interoperability, we define profiles for major domains. These profiles specify how domain standards are mapped into the UDE payload.

### **7.1 Profile: Autonomous Mobility (ROS 2\)**

Autonomous vehicles and robots typically communicate using the Robot Operating System (ROS 2). The UDE wraps these messages to ensure that steering and acceleration commands are ethically vetted.

* **Content-Type:** application/vnd.ros.msg+json.  
* **Data Mapping:**  
  * payload.data maps to ackermann\_msgs/AckermannDrive or geometry\_msgs/Twist.6  
  * payload.dataschema points to the JSON schema of the ROS message.26  
* **Specific Logic Requirements:**  
  * **State 0 (Pause):** In an AV, a "Pause" cannot be a simple freeze (which is dangerous at highway speeds). The Profile mandates that State 0 maps to a **Minimum Risk Maneuver (MRM)** as defined in ISO 26262 (e.g., gradually slowing down and pulling to the shoulder).  
  * **Latency:** Due to real-time constraints, UDE generation and signing for AVs must occur within \<10ms. Hardware Security Modules (HSM) are recommended for onboard signing.  
* **Fault Injection:** The TML layer can simulate "ethical faults" (forcing State \-1) during simulation to test the vehicle's response to ethical blockers, utilizing the FaultInjector class concepts found in CARLA ROS bridges.30

### **7.2 Profile: Medical Diagnostics (FHIR)**

For medical AI, the UDE wraps HL7 FHIR resources. This integrates TML into the existing hospital information infrastructure.

* **Content-Type:** application/fhir+json.7  
* **Data Mapping:**  
  * payload.data maps to a DiagnosticReport, ServiceRequest, or Bundle.  
  * **State \-1:** Used when an AI detects a contraindication (e.g., prescribing a drug the patient is allergic to). The rationale references the specific interaction.  
  * **State 0:** Used when the AI's confidence in a diagnosis is below the clinical threshold (e.g., \<95%). This forces the report to be flagged for "Physician Review."  
* **Privacy:** The payload MUST be encrypted (JWE) if it contains Protected Health Information (PHI/PII), while the meta and logic sections remain cleartext for ethical auditing without exposing patient identity. This satisfies HIPAA and GDPR minimization principles.

### **7.3 Profile: Financial Trading (FIX)**

Algorithmic trading requires extreme speed and reliability. The UDE provides a "Circuit Breaker" at the individual trade level.

* **Content-Type:** application/fix+json.8  
* **Data Mapping:**  
  * payload.data maps to a NewOrderSingle (MsgType=D) or ExecutionReport (MsgType=8).  
  * **Field Mapping:** FIX fields are mapped to JSON key-values (e.g., 54=1 becomes "Side": "Buy").  
* **Specific Logic Requirements:**  
  * **Flash Crash Prevention:** If market volatility exceeds a defined parameter, the TML agent emits State \-1 for all aggressive buy orders, effectively acting as a localized liquidity preservation mechanism.  
  * **State 0:** Triggered if data feeds are inconsistent (e.g., an arbitrage opportunity that looks "too good to be true" due to a sensor glitch).

### **7.4 Profile: Generative AI (LLM & Agents)**

For Large Language Models, the UDE governs the output generation process, wrapping the prompt and completion.

* **Content-Type:** application/json.  
* **Data Mapping:**  
  * payload.data contains the messages array and the generated content.32  
  * **Structured Outputs:** The UDE leverages OpenAI's json\_schema response format to ensure the LLM itself participates in structuring the rationale.34  
* **Guardrails Integration:**  
  * The logic.rationale.guardrails\_triggered field maps to outputs from frameworks like **Guardrails AI**.35 If a guardrail (e.g., "Hallucination Check") fails, the UDE is emitted with State 0 or \-1, preventing the user from seeing the potentially harmful response.  
* **Hallucination Control:** State 0 is the designated response for "I don't know." Instead of hallucinating a fact, the model is trained/prompted to emit State 0 when perplexity is high.

### **7.5 Profile: Smart Cities & Context Management (NGSI-LD)**

For IoT and Smart City infrastructure, the UDE integrates with ETSI NGSI-LD.

* **Content-Type:** application/ld+json.27  
* **Data Mapping:**  
  * payload.data contains the NGSI-LD Entity (e.g., TrafficLight, AirQualitySensor).36  
  * **Context:** The @context field in JSON-LD is preserved to ensure semantic interoperability across different city departments.37  
* **Use Case:** A smart traffic light AI decides to change lights. The UDE wraps the TrafficLight entity update. If the change would trap an emergency vehicle (detected via sensor), the TML state becomes \-1 (Refuse).

### **7.6 Profile: Software Bill of Materials (SBOM)**

To align with supply chain security, the UDE meta section supports deep linking to SBOMs.

* **Integration:** The model\_version and agent\_id fields should resolve to a **CycloneDX** or **SPDX 3.0** document.15  
* **AI Profile:** SPDX 3.0 includes specific profiles for AI, detailing energy consumption and training data.38 The UDE effectively acts as a dynamic, runtime extension of the static SBOM, proving that the software described in the SBOM is operating within its defined parameters.

### **7.7 Profile: Content Provenance (C2PA)**

For media generation, the UDE supports the fight against deepfakes.

* **Integration:** The UDE sec section is compatible with the **C2PA** (Coalition for Content Provenance and Authenticity) technical specification.39  
* **Binding:** The UDE signature can be embedded as a C2PA assertion, cryptographically binding the ethical decision (e.g., "Generated for Satire") to the media file itself. This provides a "nutrition label" for the content's intent and origin.39

## ---

**8\. Protocol Operations: The "No Log, No Action" Handshake**

To enforce TML, the UDE is not merely a log format; it is a permission token. This section defines the TML-Handshake protocol.

### **8.1 The Transmission Sequence**

1. **Inference:** The AI Core calculates a desired action.  
2. **TML Check:** The TML Module evaluates the action (State \-1, 0, or \+1).  
3. **Encapsulation:** The UDE is constructed.  
4. **Signing:** The UDE is signed with the agent's private key.  
5. **Logging (The Oracle Step):**  
   * The Agent sends the UDE hash to the Lantern (Transparency Log).28  
   * The Lantern returns a **Signed Certificate Timestamp (SCT)** or **Inclusion Proof**.10  
6. **Actuation:**  
   * The Actuator Controller receives the UDE \+ Inclusion Proof.  
   * **IF** Proof is valid **AND** State is \+1 **THEN** Execute.  
   * **ELSE** Block action.

This sequence ensures that no action occurs without an immutable record existing *first*. If the network is down and the log cannot be reached, the system defaults to a fail-safe mode (State \-1). This eliminates "phantom" actions where AI systems act without accountability.

## ---

**9\. Governance and Legal Framework**

### **9.1 The Goukassian Promise**

The UDE is the technical artifact that enables the **Goukassian Promise**: a legal instrument where the operator accepts strict liability for the AI's actions, provided the Moral Trace is intact.9 The UDE serves as the "discovery" document in any legal challenge.

* **Evidence:** In a court of law, the logic.rationale and payload serve as testimony. The cryptographic signature proves the AI's "state of mind" at the time of the incident.

### **9.2 Liability Tracing**

The agent\_id (DID) and model\_version fields allow investigators to trace liability to the specific entity and software version responsible. If an error is caused by a specific model update, the UDEs reveal exactly when that version was deployed and which decisions it influenced.

### **9.3 Earth as a Client (Earth Protection)**

TML explicitly recognizes the Earth as a stakeholder. The "Earth Protection" module within TML mandates that actions harming the biosphere must be Refused (-1) or Paused (0).11

* **Implementation:** The UDE logic section may include an ecological\_impact\_score.  
* **Jurisdiction:** The meta.location field enforces "Geofenced Ethics," ensuring that AI systems respect protected ecological zones (e.g., an autonomous drone refusing to fly over a nesting sanctuary).

## ---

**10\. Security and Integrity**

### **10.1 Cryptographic Anchoring**

The UDE uses a recursive hashing scheme to ensure integrity.  
$$ H\_{current} \= SHA256( UDE\_{header} |  
| UDE\_{logic} |  
| H(UDE\_{payload}) |  
| H\_{previous} ) $$  
This ensures that any modification to the payload or the history breaks the cryptographic chain, making tampering immediately evident during an audit.10

### **10.2 Transparency Logs (Rekor)**

The UDE system leverages **Rekor**, a transparency log from the Sigstore project.28 Rekor provides an append-only, immutable ledger. By submitting UDE hashes to Rekor, TML agents create a public, tamper-proof record of their decisions. This prevents the "Split View" attack where an agent shows one log to auditors and another to the world.42

### **10.3 Ephemeral Key Rotation**

To limit the blast radius of a compromised key, TML-Agents SHOULD use ephemeral signing keys rotated frequently (e.g., daily). The public keys MUST be published to the Transparency Log linked to the agent's permanent DID.

### **10.4 Quantum Readiness**

While Ed25519 is the current recommended signature algorithm, the UDE schema allows for algorithm agility via the sec.signature\_alg field. Implementers SHOULD prepare for migration to NIST-standardized Post-Quantum Cryptography (PQC) algorithms like **CRYSTALS-Dilithium** or **SPHINCS+** to ensure long-term evidence durability.

## ---

**11\. Compliance and Auditing Mappings**

The UDE is designed to satisfy global regulatory requirements by design.

| Regulation / Standard | Requirement | UDE Implementation |
| :---- | :---- | :---- |
| **EU AI Act** | Technical Documentation & Record Keeping (Art. 11, 12\) | logic.rationale and sec.transparency\_log\_index provide continuous, automated compliance records. |
| **EU AI Act** | Human Oversight (Art. 14\) | The State 0 (Sacred Zero) workflow mechanically enforces human intervention in ambiguous states. |
| **ISO/IEC 42001** | A.9.2 Internal Audit | The "Always Memory" chain allows auditors to cryptographically verify the completeness of the audit trail.12 |
| **NIST AI RMF** | Map & Measure (Trustworthiness) | logic.confidence and meta.model\_version allow mapping risk levels to specific model iterations.43 |
| **GDPR** | Right to Explanation (Recital 71\) | logic.rationale provides the "meaningful information about the logic involved" required by law. |

## ---

**12\. Operational Guidelines**

### **12.1 Implementation Strategy**

Organizations should implement TML/UDE in phases:

1. **Passive Mode:** The Agent emits UDEs but the Actuator does not block actions based on them. This allows for data collection and calibration.  
2. **Active Mode (Binary):** The Actuator blocks on State \-1 but allows State 0 (treating it as a warning).  
3. **Full TML Mode:** The Actuator enforces "No Log, No Action" and fully operationalizes the State 0 "Sacred Pause" workflow.

### **12.2 Auditing Workflows**

Auditors (human or automated) can verify TML compliance by:

1. **Chain Verification:** Recomputing the hash chain of UDEs to ensure no gaps.  
2. **Log Consistency:** Querying the Lantern (Rekor) to verify that the UDEs in the agent's local storage match the public record.10  
3. **Rationale Analysis:** Using LLMs to semantically analyze the logic.rationale text for alignment with policy.

## ---

**13\. Future Directions**

### **13.1 Interplanetary Synchronization**

As AI agents are deployed on Mars or deep-space probes, the "No Log, No Action" real-time requirement faces light-speed latency challenges. Future versions of UDE will define "Async-Optimistic" modes where the transparency\_proof can be batched and delayed, provided a local Hardware Security Module (HSM) guarantees the log's integrity until transmission is possible.

### **13.2 Artificial General Intelligence (AGI)**

For AGI, the UDE will likely need to evolve to support recursive self-improvement logs. The logic section will expand to include complex "Goal Alignment" metrics, ensuring that the AGI's evolving objective function remains anchored to TML principles.

## ---

**Annex A: Complete JSON Schema (Normative)**

*(Note: This schema is provided for validation purposes. It adheres to JSON Schema Draft 7.)*

JSON

{  
  "$schema": "http://json-schema.org/draft-07/schema\#",  
  "title": "Universal Decision Envelope",  
  "type": "object",  
  "required": \["spec\_version", "id", "meta", "logic", "sec"\],  
  "properties": {  
    "spec\_version": { "type": "string", "const": "1.0.0" },  
    "id": { "type": "string", "format": "uuid" },  
    "meta": {  
      "type": "object",  
      "required": \["timestamp", "agent\_id"\],  
      "properties": {  
        "timestamp": { "type": "string", "format": "date-time" },  
        "agent\_id": { "type": "string" },  
        "model\_version": { "type": "string" },  
        "session\_id": { "type": "string" },  
        "environment": { "type": "string", "enum": \["production", "staging", "testing", "simulation"\] },  
        "location": {  
            "type": "object",  
            "properties": {  
                "lat": { "type": "number" },  
                "lon": { "type": "number" },  
                "alt": { "type": "number" },  
                "crs": { "type": "string" }  
            }  
        }  
      }  
    },  
    "logic": {  
      "type": "object",  
      "required": \["tml\_state"\],  
      "properties": {  
        "tml\_state": { "type": "integer", "enum": \[-1, 0, 1\] },  
        "confidence": { "type": "number", "minimum": 0, "maximum": 1 },  
        "latency\_ms": { "type": "number" },  
        "voice": { "type": "string" },  
        "oversight\_required": { "type": "boolean" },  
        "rationale": {  
            "type": "object",  
            "properties": {  
                "summary": { "type": "string" },  
                "mandates\_consulted": { "type": "array", "items": { "type": "string" } },  
                "trigger\_event": { "type": "string" },  
                "guardrails\_triggered": { "type": "array", "items": { "type": "string" } }  
            }  
        }  
      }  
    },  
    "payload": {  
      "type": "object",  
      "properties": {  
        "content\_type": { "type": "string" },  
        "dataschema": { "type": "string" },  
        "data": { "type": \["object", "string"\] },  
        "data\_base64": { "type": "string" }  
      }  
    },  
    "sec": {  
      "type": "object",  
      "required": \["signature", "previous\_hash"\],  
      "properties": {  
        "previous\_hash": { "type": \["string", "null"\] },  
        "merkle\_root": { "type": "string" },  
        "signature\_alg": { "type": "string" },  
        "signature": { "type": "string" },  
        "transparency\_log\_index": { "type": "integer" },  
        "transparency\_proof": { "type": "string" }  
      }  
    }  
  }  
}

## **Conclusion**

The Universal Decision Envelope (UDE) is the indispensable bridge between the high-minded ethics of Ternary Moral Logic and the gritty reality of software execution. By standardizing the expression of machine intent, we create a world where AI is not just powerful, but accountable. The UDE ensures that every robot, every algorithm, and every model carries with it a permanent, unalterable record of its conscience. It transforms the "Black Box" into a "Glass Box," providing the transparency necessary for trust in the age of autonomous systems. With the adoption of this specification, we move from the era of "move fast and break things" to the era of "move intentionally and prove it."  
---

**End of Specification**

#### **Works cited**

1. FractonicMind/TernaryMoralLogic: Implementing Ethical Responsibility in AI Systems \- GitHub, accessed December 3, 2025, [https://github.com/FractonicMind/TernaryMoralLogic](https://github.com/FractonicMind/TernaryMoralLogic)  
2. How a Dying Man Taught AI to Think Before It Acts | by Lev Goukassian \- Medium, accessed December 3, 2025, [https://medium.com/@leogouk/how-a-dying-man-taught-ai-to-think-before-it-acts-a9191f42a429](https://medium.com/@leogouk/how-a-dying-man-taught-ai-to-think-before-it-acts-a9191f42a429)  
3. AI Auditing Checklist for AI Auditing, accessed December 3, 2025, [https://www.edpb.europa.eu/system/files/2024-06/ai-auditing\_checklist-for-ai-auditing-scores\_edpb-spe-programme\_en.pdf](https://www.edpb.europa.eu/system/files/2024-06/ai-auditing_checklist-for-ai-auditing-scores_edpb-spe-programme_en.pdf)  
4. Artificial Intelligence Auditing Framework \- The Institute of Internal Auditors, accessed December 3, 2025, [https://www.theiia.org/globalassets/site/content/tools/professional/aiframework-sept-2024-update.pdf](https://www.theiia.org/globalassets/site/content/tools/professional/aiframework-sept-2024-update.pdf)  
5. A UNESCO Researcher's Unexpected Morning | by Lev Goukassian | Nov, 2025 | Medium, accessed December 3, 2025, [https://medium.com/@leogouk/tml-to-unesco-the-operational-layer-you-forgot-to-write-down-e61b60d0e2da](https://medium.com/@leogouk/tml-to-unesco-the-operational-layer-you-forgot-to-write-down-e61b60d0e2da)  
6. meta-ros2-kilted \- OpenEmbedded Layer Index, accessed December 3, 2025, [https://layers.openembedded.org/layerindex/branch/master/layer/meta-ros2-kilted/](https://layers.openembedded.org/layerindex/branch/master/layer/meta-ros2-kilted/)  
7. DiagnosticReport-Lab-example-03 \- JSON Representation \- FHIR Implementation Guide for ABDM v6.5.0 \- NRCeS, accessed December 3, 2025, [https://www.nrces.in/ndhm/fhir/r4/Bundle-DiagnosticReport-Lab-example-03.json.html](https://www.nrces.in/ndhm/fhir/r4/Bundle-DiagnosticReport-Lab-example-03.json.html)  
8. Encoding FIX using JSON \- FIXimate, accessed December 3, 2025, [https://www.fixtrading.org/standards/json-online/](https://www.fixtrading.org/standards/json-online/)  
9. How a Terminal Diagnosis Inspired a New Ethical AI System \- Hackernoon, accessed December 3, 2025, [https://hackernoon.com/how-a-terminal-diagnosis-inspired-a-new-ethical-ai-system](https://hackernoon.com/how-a-terminal-diagnosis-inspired-a-new-ethical-ai-system)  
10. RFC 9162 \- Certificate Transparency Version 2.0 \- IETF Datatracker, accessed December 3, 2025, [https://datatracker.ietf.org/doc/html/rfc9162](https://datatracker.ietf.org/doc/html/rfc9162)  
11. Arming Earth's Right to Sue \- by Lev Goukassian \- Medium, accessed December 3, 2025, [https://medium.com/@leogouk/arming-earths-right-to-sue-b1ec834d38fe](https://medium.com/@leogouk/arming-earths-right-to-sue-b1ec834d38fe)  
12. ISO/IEC 42001: Features, Types & Best Practices \- Lasso Security, accessed December 3, 2025, [https://www.lasso.security/blog/iso-iec-42001](https://www.lasso.security/blog/iso-iec-42001)  
13. Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile \- NIST Technical Series Publications, accessed December 3, 2025, [https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)  
14. Information on RFC 7515 \- » RFC Editor, accessed December 3, 2025, [https://www.rfc-editor.org/info/rfc7515](https://www.rfc-editor.org/info/rfc7515)  
15. https://cyclonedx.org/schema/bom-1.5.xsd, accessed December 3, 2025, [https://cyclonedx.org/schema/bom/1.5](https://cyclonedx.org/schema/bom/1.5)  
16. SPDX© Specification v3.0.1, accessed December 3, 2025, [https://spdx.dev/wp-content/uploads/sites/31/2024/12/SPDX-3.0.1-1.pdf](https://spdx.dev/wp-content/uploads/sites/31/2024/12/SPDX-3.0.1-1.pdf)  
17. spec/cloudevents/formats/json-format.md at main \- GitHub, accessed December 3, 2025, [https://github.com/cloudevents/spec/blob/main/cloudevents/formats/json-format.md](https://github.com/cloudevents/spec/blob/main/cloudevents/formats/json-format.md)  
18. Content Credentials : C2PA Technical Specification, accessed December 3, 2025, [https://spec.c2pa.org/specifications/specifications/2.2/specs/C2PA\_Specification.html](https://spec.c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html)  
19. The Day the AI Bowed. I built an ethical AI system. One of… | by Lev Goukassian \- Medium, accessed December 3, 2025, [https://medium.com/@leogouk/the-day-the-ai-bowed-d913f388bd98](https://medium.com/@leogouk/the-day-the-ai-bowed-d913f388bd98)  
20. The Day UNESCO Discovered Its Own Missing Soul : r/worldbuilding \- Reddit, accessed December 3, 2025, [https://www.reddit.com/r/worldbuilding/comments/1pcet4g/the\_day\_unesco\_discovered\_its\_own\_missing\_soul/](https://www.reddit.com/r/worldbuilding/comments/1pcet4g/the_day_unesco_discovered_its_own_missing_soul/)  
21. Ternary Moral Logic (TML) \- Ethical AI Framework, accessed December 3, 2025, [https://fractonicmind.github.io/TernaryMoralLogic/](https://fractonicmind.github.io/TernaryMoralLogic/)  
22. The Complete Guide to SPDX | FOSSA Learning Center, accessed December 3, 2025, [https://fossa.com/learn/spdx/](https://fossa.com/learn/spdx/)  
23. Documentation Standards for Regulated AI: Meeting Audit and Transparency Requirements – VerityAI Blog, accessed December 3, 2025, [https://verityai.co/blog/documentation-standards-regulated-ai](https://verityai.co/blog/documentation-standards-regulated-ai)  
24. AI Cards: Towards an Applied Framework for Machine-Readable AI and Risk Documentation Inspired by the EU AI Act \- arXiv, accessed December 3, 2025, [https://arxiv.org/html/2406.18211v1](https://arxiv.org/html/2406.18211v1)  
25. What are AI guardrails? \- McKinsey, accessed December 3, 2025, [https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-are-ai-guardrails](https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-are-ai-guardrails)  
26. Parameters \- Autoware Universe Documentation, accessed December 3, 2025, [https://autowarefoundation.github.io/autoware-documentation/pr-279/contributing/coding-guidelines/ros-nodes/parameters/](https://autowarefoundation.github.io/autoware-documentation/pr-279/contributing/coding-guidelines/ros-nodes/parameters/)  
27. Official Website for NGSI-LD, accessed December 3, 2025, [https://ngsi-ld.org/](https://ngsi-ld.org/)  
28. Rekor \- Sigstore, accessed December 3, 2025, [https://docs.sigstore.dev/logging/overview/](https://docs.sigstore.dev/logging/overview/)  
29. An Introduction to Rekor \- Chainguard Academy, accessed December 3, 2025, [https://edu.chainguard.dev/open-source/sigstore/rekor/an-introduction-to-rekor/](https://edu.chainguard.dev/open-source/sigstore/rekor/an-introduction-to-rekor/)  
30. Simulating the Effects of Sensor Failures on Autonomous Vehicles for Safety Evaluation, accessed December 3, 2025, [https://www.mdpi.com/2227-9709/12/3/94](https://www.mdpi.com/2227-9709/12/3/94)  
31. DiagnosticReport $diagnosticreport-create \- Redox developer docs, accessed December 3, 2025, [https://docs.redoxengine.com/permalink/c216c7e0-cff3-545a-98cc-ca2fde009158-$diagnosticreport-create](https://docs.redoxengine.com/permalink/c216c7e0-cff3-545a-98cc-ca2fde009158-$diagnosticreport-create)  
32. Learn how to use JSON mode \- Azure OpenAI, accessed December 3, 2025, [https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/json-mode?view=foundry-classic](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/json-mode?view=foundry-classic)  
33. The Chat Completions API endpoint will generate a model response from a list of messages comprising a conversation. \- OpenAI Platform, accessed December 3, 2025, [https://platform.openai.com/docs/api-reference/chat](https://platform.openai.com/docs/api-reference/chat)  
34. Structured model outputs \- OpenAI API, accessed December 3, 2025, [https://platform.openai.com/docs/guides/structured-outputs](https://platform.openai.com/docs/guides/structured-outputs)  
35. What Are AI Guardrails? \- IBM, accessed December 3, 2025, [https://www.ibm.com/think/topics/ai-guardrails](https://www.ibm.com/think/topics/ai-guardrails)  
36. ETSI GS CIM 009 (V1.5.1) (2021-11), accessed December 3, 2025, [https://www.etsi.org/deliver/etsi\_gs/CIM/001\_099/009/01.05.01\_60/gs\_cim009v010501p.pdf](https://www.etsi.org/deliver/etsi_gs/CIM/001_099/009/01.05.01_60/gs_cim009v010501p.pdf)  
37. Working with @context \- NGSI-LD Smart Farm Tutorials, accessed December 3, 2025, [https://ngsi-ld-tutorials.readthedocs.io/en/latest/working-with-%40context.html](https://ngsi-ld-tutorials.readthedocs.io/en/latest/working-with-%40context.html)  
38. The model for the information captured in SPDX version 3 standard. \- GitHub, accessed December 3, 2025, [https://github.com/spdx/spdx-3-model](https://github.com/spdx/spdx-3-model)  
39. C2PA and Content Credentials Explainer, accessed December 3, 2025, [https://spec.c2pa.org/specifications/specifications/2.2/explainer/Explainer.html](https://spec.c2pa.org/specifications/specifications/2.2/explainer/Explainer.html)  
40. Certificate Transparency \- Security \- MDN Web Docs \- Mozilla, accessed December 3, 2025, [https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Certificate\_Transparency](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Certificate_Transparency)  
41. RFC 9162: Certificate Transparency Version 2.0, accessed December 3, 2025, [https://www.rfc-editor.org/rfc/rfc9162.html](https://www.rfc-editor.org/rfc/rfc9162.html)  
42. RFC 6962: Certificate Transparency, accessed December 3, 2025, [https://www.rfc-editor.org/rfc/rfc6962.html](https://www.rfc-editor.org/rfc/rfc6962.html)  
43. A Checklist for the NIST AI Risk Management Framework \- AuditBoard, accessed December 3, 2025, [https://auditboard.com/blog/a-checklist-for-the-nist-ai-risk-management-framework](https://auditboard.com/blog/a-checklist-for-the-nist-ai-risk-management-framework)  
44. AI RMF Profiles \- AIRC \- NIST AI Resource Center, accessed December 3, 2025, [https://airc.nist.gov/airmf-resources/airmf/6-sec-profile/](https://airc.nist.gov/airmf-resources/airmf/6-sec-profile/)
