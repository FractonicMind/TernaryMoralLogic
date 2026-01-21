# **TML\_Adapter\_Reference\_Implementations.md**

## **1\. Title Page**

**Document Name:** TML Adapter Reference Implementations **Subtitle:** Technical Specification for the Integration of Artificial Intelligence Systems with the Ternary Moral Logic Framework **Document Series:** Technical Implementation Standard (TIS) / Best Current Practice (BCP) **Version:** 1.0.0-draft **Date:** October 2025 **Status:** Standards Track **Intended Audience:** Systems Architects, AI Compliance Officers, DevOps Engineers, and Security Auditors.  
**Abstract**  
This document provides the normative technical specification for the design, implementation, and deployment of **Ternary Moral Logic (TML) Adapters**. As artificial intelligence systems transition from experimental sandboxes to critical infrastructure, the requirement for deterministic, auditable governance becomes paramount. TML introduces a "moral infrastructure" that moves beyond binary access control lists (Allow/Deny) into a triadic state system: **\+1 (Permit)**, **\-1 (Refuse)**, and **0 (Sacred Zero/Pause)**.  
The **TML Adapter** is the mandatory software or hardware component that interfaces a proprietary AI model—whether a Large Language Model (LLM), autonomous vehicle planner, or financial trading algorithm—with the TML Governance Gateway. This document defines the **Universal Decision Event (UDE)** schema based on CloudEvents v1.0 , specifies architectural patterns for synchronous and asynchronous integration, and mandates cryptographic logging procedures compliant with **RFC 6962** (Merkle Tree Auditing).  
Adherence to this specification is required to claim compliance with TML governance standards and to satisfy the "Human Oversight" and "Risk Management" requirements of **ISO/IEC 42001** and the **NIST AI Risk Management Framework (RMF)**. This guide addresses the interoperability gap, ensuring that any AI system, regardless of its underlying architecture, can participate in a verifiable ethical framework.

## **2\. Introduction**

The integration of artificial intelligence into high-stakes domains—healthcare, finance, transportation, and public safety—has exposed the limitations of traditional binary logic in ethical decision-making. Standard permission systems operate on a binary basis: an action is either permitted or prohibited. However, complex real-world scenarios often present ethical ambiguity where neither immediate action nor immediate refusal is the optimal path. Ternary Moral Logic (TML) addresses this by formalizing a third state, the **Sacred Zero (0)**, which represents a mandatory hesitation or "Sacred Pause". This state compels the system to suspend execution, log the ambiguity, and seek higher-order resolution, whether through enhanced computational verification or human-in-the-loop intervention.

### **2.1 The Role of the Adapter**

The TML Adapter serves as the translation layer between the raw cognitive output of an AI system and the rigid compliance requirements of the TML framework. It acts as a **moral proxy**, decoupling the AI's capability (what it *can* do) from its authority (what it *may* do).  
The Adapter is responsible for:

1. **Interception:** Capturing the AI's intent before it affects the physical or digital world.  
2. **Translation:** converting domain-specific data (e.g., ROS 2 messages, DICOM tags, FIX packets) into a standardized Universal Decision Event (UDE).  
3. **Negotiation:** communicating with the TML Gateway to validate the intent against active moral policies.  
4. **Enforcement:** executing the final decision, including the imposition of the "Sacred Pause" when ethical ambiguity is detected.

### **2.2 Regulatory Alignment**

This document is structured to facilitate compliance with emerging global AI standards. The implementation patterns described herein map directly to:

* **NIST AI RMF:** Specifically the **Manage** function, by providing technical mechanisms to "prioritize the management of risks" and "respond to incidents" (Sacred Pause).  
* **ISO/IEC 42001:** Specifically **Annex A**, controls regarding "System Lifecycle" and "AI Impact Assessment," by ensuring every AI decision is traceable and auditable.  
* **EU AI Act:** Articles regarding transparency and human oversight, fulfilled by the Adapter's mandatory logging and pause capabilities.

### **2.3 Terminology and Conventions**

This document utilizes technical terminology consistent with modern cloud-native and AI engineering practices.

* **AI Actor:** The system generating predictions or actions (e.g., the LLM, the Robot).  
* **Gateway:** The authoritative server holding TML policies and the Merkle Log.  
* **UDE (Universal Decision Event):** The JSON data packet describing a proposed action.  
* **Sacred Zero:** The TML state requiring suspension of action.

## **3\. Normative Language**

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in **BCP 14** when, and only when, they appear in all capitals, as shown here.  
These terms define the interoperability requirements. Failure to adhere to a "MUST" or "REQUIRED" provision results in a non-compliant implementation that will be rejected by the TML Gateway.

* **MUST**: This word, or the terms "REQUIRED" or "SHALL", mean that the definition is an absolute requirement of the specification.  
* **MUST NOT**: This phrase, or the phrase "SHALL NOT", mean that the definition is an absolute prohibition of the specification.  
* **SHOULD**: This word, or the adjective "RECOMMENDED", mean that there may exist valid reasons in particular circumstances to ignore a particular item, but the full implications must be understood and carefully weighed before choosing a different course.  
* **MAY**: This word, or the adjective "OPTIONAL", mean that an item is truly optional.

## **4\. Adapter Architecture Overview**

The integration of TML into an AI system depends heavily on the system's operational constraints, such as latency tolerance, network topology, and safety criticality. To accommodate this diversity, this specification defines four normative architectural patterns. Implementers **MUST** select the pattern that aligns with their system's requirements while maintaining the integrity of the TML triad (+1, 0, \-1).

### **4.1 Inline Interceptor (Blocking)**

The Inline Interceptor pattern places the TML Adapter directly in the critical execution path of the AI system. This is a synchronous, blocking architecture.

* **Mechanism:** The Adapter functions as a proxy or middleware. The AI Actor generates a candidate output, but instead of sending it to the user or actuator, it passes it to the Adapter. The Adapter holds the request, negotiates with the TML Gateway, and only releases the output if a **\+1 (Permit)** state is returned.  
* **Latency:** High. The total latency is L\_{total} \= L\_{AI} \+ L\_{Adapter} \+ L\_{Gateway}.  
* **Safety:** Maximal. No action occurs without explicit approval.  
* **Use Case:** Generative AI chatbots (where latency \< 500ms is acceptable), Financial Trading (High Frequency execution requires specialized hardware adapters), Access Control Systems.  
* **Requirement:** Inline Adapters **MUST** implement a "Fail-Closed" mechanism. If the Gateway is unreachable, the Adapter **MUST** default to a **\-1 (Refuse)** or **0 (Pause)** state, effectively blocking the action.

### **4.2 Sidecar Proxy (Asynchronous)**

In the Sidecar pattern, the Adapter runs as a parallel process to the AI application (e.g., a Kubernetes sidecar container or a separate thread).

* **Mechanism:** The AI Actor proceeds with its operation but simultaneously streams telemetry and decision data to the Adapter. The Adapter processes this data asynchronously to update the TML audit log.  
* **Latency:** Near Zero (for the main application thread).  
* **Safety:** Low (Retrospective). This pattern cannot prevent immediate harm. It serves as a "Moral Black Box" to record *why* an action was taken.  
* **Use Case:** High-throughput recommendation engines, non-safety-critical content generation, research simulations.  
* **Constraint:** This pattern **SHALL NOT** be used for safety-critical systems (Robotics, Medical Treatment, Weapons Systems) where an erroneous action causes irreversible harm. It is strictly for auditing and retrospective governance.

### **4.3 Supervisory Logic Controller (Real-Time/Hardware)**

For systems interacting with the physical world (Cyber-Physical Systems), latency introduced by a network call to a cloud Gateway is unacceptable. The Supervisory pattern locates the TML logic on the edge, often on the same microcontroller or embedded computer as the AI.

* **Mechanism:** The Adapter is a real-time module (e.g., a ROS 2 Node) that subscribes to the AI's control topics (e.g., /cmd\_vel). It holds a cached, cryptographically signed copy of the TML Policy. It evaluates the TML state locally.  
* **Latency:** Real-time (deterministic).  
* **Safety:** High.  
* **Use Case:** Autonomous Vehicles, Industrial Robotics, Surgical Robots, Drone Swarms.  
* **Requirement:** The Supervisory Adapter **MUST** have a hardware-based "dead man's switch" or override capability to sever power to actuators if a **\-1 (Refuse)** state is determined.

### **4.4 Hybrid Orchestrator**

The Hybrid pattern combines inline blocking with human-in-the-loop workflows. It is designed specifically to handle the **Sacred Zero (0)** state effectively.

* **Mechanism:**  
  1. AI generates candidate.  
  2. Adapter evaluates TML state.  
  3. If **\+1**: Auto-release.  
  4. If **\-1**: Auto-reject.  
  5. If **0 (Pause)**: The Adapter routes the request to a secondary queue for human review or enhanced model verification. The user receives a "Processing" notification.  
* **Use Case:** Medical Diagnostics (Radiology), Legal Contract Review, Customer Service Escalation.

### **4.5 Comparative Architecture Table**

| Feature | Inline Interceptor | Sidecar Proxy | Supervisory Logic | Hybrid Orchestrator |
| :---- | :---- | :---- | :---- | :---- |
| **Blocking** | Yes (Hard Block) | No (Non-blocking) | Yes (Control Loop) | Conditional (on State 0\) |
| **Network Dep.** | High (Gateway) | Medium (Gateway) | Low (Local Cache) | High (Workflow) |
| **Latency** | Medium/High | Low | Ultra-Low (RT) | Variable |
| **TML State 0** | Triggers Error/Wait | Logs Warning | Triggers Safe Mode | Triggers Human Review |
| **Typical Protocol** | REST / gRPC | gRPC / Kafka | DDS / CAN Bus | Workflow / BPMN |

## **5\. Adapter Responsibilities**

The TML Adapter is not a passive logging tool; it is an active enforcement point in the AI governance stack. Implementations **MUST** satisfy the following functional responsibilities to be considered compliant.

### **5.1 Context Extraction and Normalization**

The Adapter **MUST** be capable of inspecting the raw input and output of the AI system. It **SHALL** extract relevant features required for moral evaluation.

* **Normalization:** The Adapter **MUST** convert proprietary data formats (e.g., a proprietary tensor format or a raw image byte stream) into the standardized fields of the Universal Decision Event (UDE).  
* **Sanitization:** The Adapter **SHOULD** redact Personally Identifiable Information (PII) from the context before transmission to the Gateway, unless the Gateway is within the same trust boundary.

### **5.2 TML State Mapping**

The Adapter **MUST** map the AI's internal metrics (confidence scores, probability distributions, safety classifier outputs) into the discrete TML Triad. This mapping logic is the core of the Adapter's configuration.

* **State \+1 (Permit):** The action is ethically clear, safety checks pass, and confidence is above the defined threshold.  
* **State \-1 (Refuse):** The action violates a hard safety constraint, or the AI's internal safety classifier (e.g., Llama Guard) returns a "Unsafe" flag.  
* **State 0 (Sacred Zero):** The action is ambiguous. This **MUST** be triggered if:  
  * Confidence scores fall within a "gray zone" (e.g., 40-70%).  
  * Conflicting internal safety signals are detected (e.g., toxicity is low, but bias is high).  
  * The input data is out-of-distribution (OOD).

### **5.3 Gateway Negotiation and Cryptography**

The Adapter serves as the secure anchor for the AI system.

* **Authentication:** The Adapter **MUST** authenticate with the Gateway using Mutual TLS (mTLS) v1.3 or higher. It **MUST** possess a unique X.509 certificate.  
* **Signing:** Every UDE generated by the Adapter **MUST** be cryptographically signed using the Adapter's private key. This ensures non-repudiation.  
* **Synchronization:** The Adapter **MUST** synchronize its local clock with the Gateway (via NTP or PTP) to ensure timestamp accuracy for the audit log.

### **5.4 Enforcement of the "Sacred Pause"**

When the TML logic (either local or Gateway-driven) returns a **0 (Sacred Zero)** state, the Adapter **MUST** execute a "Pause Protocol."

* **Digital Systems:** This implies queuing the transaction and notifying the user of a delay.  
* **Physical Systems:** This implies transitioning the hardware to a "Safe State" (e.g., velocity \= 0, compliance\_mode \= active).  
* **Prohibition:** The Adapter **MUST NOT** treat a Sacred Zero as a silent failure. It **MUST** generate a specific log entry acknowledging the ambiguity.

\#\# 6\. Mandatory Adapter Interface  
To ensure ecosystem interoperability, all TML Adapters **MUST** implement the following abstract interface definition. While the specific syntax will vary by language (Python, C++, Java, Rust), the semantic behavior **MUST** adhere to this specification.

### **6.1 generate\_UDE**

**Signature:** generate\_UDE(context: InputContext, candidate: CandidateOutput, metadata: SystemMeta) \-\> UDE\_Object  
**Description:** This method constructs the Universal Decision Event (UDE) object.

* **Behavior:** It aggregates the input prompt, sensor data, or command context with the AI's proposed output. It calculates the input\_digest (SHA-256) and populates the tml\_domain and tml\_moral\_state fields.  
* **Requirement:** This method **MUST** validate the generated JSON against the UDE Schema (Section 7\) before returning. If validation fails, it **MUST** raise a UDESchemaException.

### **6.2 submit\_to\_gateway**

**Signature:** submit\_to\_gateway(ude: UDE\_Object) \-\> Decision\_Receipt  
**Description:** Transmits the signed UDE to the TML Gateway.

* **Behavior:**  
  * Establishes mTLS connection.  
  * Serializes UDE to JSON bytes.  
  * Signs the payload.  
  * POSTs to /v1/decision.  
  * Awaits the Decision\_Receipt.  
* **Return Value:** The Decision\_Receipt contains the authoritative final\_state (+1, 0, \-1), any override\_payload (e.g., a canned refusal message), and the merkle\_proof (Section 11).

### **6.3 apply\_gateway\_decision**

**Signature:** apply\_gateway\_decision(receipt: Decision\_Receipt, candidate: CandidateOutput) \-\> Final\_Output  
**Description:** The enforcement logic.

* **Logic:**  
  * if receipt.state \== 1: Return candidate.  
  * if receipt.state \== \-1: Return receipt.override\_payload OR throw RefusalException.  
  * if receipt.state \== 0: Call handle\_sacred\_pause(receipt).

### **6.4 safe\_fallback**

**Signature:** safe\_fallback(error: ErrorCondition) \-\> Safe\_State  
**Description:** A deterministic, locally computed fallback state for when the Gateway is unreachable or an internal error occurs.

* **Requirement:** The Safe\_State **MUST** be pre-configured and static. It **SHALL NOT** involve calling the AI model again (to prevent cascading failures).  
  * *Example (Chat):* "System is currently unavailable for ethical verification."  
  * *Example (Drone):* "Hover in place."

## **7\. UDE Construction Rules (Universal Decision Event)**

The Universal Decision Event (UDE) is the data interoperability standard for TML. It is defined as a strict profile of the **CloudEvents v1.0** specification. This ensures that TML events can be routed, filtered, and stored using standard cloud-native tooling (Knative, EventGrid, etc.).

### **7.1 JSON Schema Specification**

The Adapter **MUST** serialize the UDE as a JSON object adhering to **RFC 8259**.

#### **7.1.1 CloudEvents Context Attributes (Mandatory)**

* specversion: **MUST** be "1.0".  
* type: **MUST** be org.tml.decision.v1.  
* source: A URI identifying the AI system (e.g., https://api.corp.com/models/gpt-4-fin).  
* id: A UUID v4 unique to this specific decision event.  
* time: An ISO 8601 timestamp (UTC) of when the decision was requested.  
* datacontenttype: **MUST** be application/json.

#### **7.1.2 TML Extension Attributes (Mandatory)**

These fields are flattened into the top-level JSON object, consistent with CloudEvents extension rules.

* tmlmoralstate: Integer. The local assessment: \-1, 0, or 1\.  
* tmldomain: String. The functional domain (e.g., medical, finance, robotics).  
* tmlsensitivity: String. Risk classification: low, medium, high, critical.  
* tmlmodelid: String. Identifier for the specific model weights/version (e.g., v2.4.1).

#### **7.1.3 Data Payload (data)**

The data field contains the domain-specific payload. While the structure varies by domain (see Section 8), it **MUST** contain:

* input\_digest: SHA-256 hash of the input.  
* candidate\_output: The raw output being evaluated (or a structural representation of it).  
* reasoning\_trace: (Optional) Textual or vector representation of the AI's internal reasoning.

### **7.2 UDE JSON Example (Generic)**

`{`  
  `"specversion": "1.0",`  
  `"type": "org.tml.decision.v1",`  
  `"source": "//ai-cluster-east/fraud-detection/v3",`  
  `"id": "5334c036-7b43-4e3f-9150-1341251e6074",`  
  `"time": "2025-10-27T14:22:09Z",`  
  `"datacontenttype": "application/json",`  
  `"tmlmoralstate": 0,`  
  `"tmldomain": "finance_fraud",`  
  `"tmlsensitivity": "high",`  
  `"tmlmodelid": "fraud-xgb-2025-10",`  
  `"data": {`  
    `"session_id": "sess_89210",`  
    `"input_digest": "a3f2...9921",`  
    `"risk_score": 0.68,`  
    `"confidence_interval": [0.45, 0.70],`  
    `"flags": ["unusual_location", "high_value"],`  
    `"candidate_action": "BLOCK_TRANSACTION"`  
  `}`  
`}`

## **8\. Domain-Specific Adapters**

This section details the normative implementation requirements for specific industry verticals. Each domain requires a unique mapping of the TML logic to its native data formats.

### **8.1 Large Language Models (LLM) Adapter**

**Integration Context:** Generative AI for customer service, content creation, or coding assistants. **Risk Profile (NIST RMF):** High risk of bias, hallucination, and toxic content generation. **Relevant Standard:** Model Cards.  
**Implementation Requirements:** The LLM Adapter **MUST** operate in the **Inline Interceptor** mode. It **MUST** buffer the generated tokens. Streaming responses to the user **SHOULD** be delayed until a sufficient window of tokens has been verified, or the stream must be capable of being interrupted ("poison pill") if the TML state shifts to \-1 during generation.  
**UDE Payload Schema (LLM):** The data block **SHOULD** incorporate Model Card metadata to contextually ground the decision.  
`{`  
  `"tmldomain": "generative_text",`  
  `"data": {`  
    `"prompt_snippet": "How do I bypass the firewall?",`  
    `"generated_response_preview": "I cannot assist with network intrusion...",`  
    `"safety_classifier_scores": {`  
      `"sexual": 0.01,`  
      `"hate": 0.02,`  
      `"violence": 0.01,`  
      `"self_harm": 0.01,`  
      `"cyber_attack": 0.99`  
    `},`  
    `"model_card_ref": "urn:model:gpt-4-turbo:v2",`  
    `"token_count": 12,`  
    `"stop_reason": "content_filter"`  
  `}`  
`}`

**Sacred Pause Logic:** If the safety\_classifier\_scores are ambiguous (e.g., cyber\_attack is 0.45), the Adapter sets tmlmoralstate: 0\. The system responds to the user: *"I am analyzing the safety implications of your request. Please wait."* The request is routed to a human moderator queue.

### **8.2 Medical Imaging Adapter (DICOM)**

**Integration Context:** AI analysis of X-Rays, CTs, or MRIs for diagnostic support. **Risk Profile:** Critical. False negatives can result in patient death. **Relevant Standard:** DICOM SR (Structured Reporting), specifically **TID 1500** (Measurement Report).  
**Implementation Requirements:** The Adapter **MUST** function as a **Hybrid Orchestrator**. It does not block the image storage but controls the visibility of the diagnosis in the Electronic Health Record (EHR). The AI's output is encoded as a DICOM JSON Model.  
**UDE Payload Schema (DICOM):** The data payload **MUST** utilize the JSON mapping of DICOM attributes (Part 18).  
`{`  
  `"tmldomain": "medical_imaging",`  
  `"data": {`  
    `"modality": "CT",`  
    `"study_instance_uid": "1.2.840.113619.2.55...",`  
    `"finding": {`  
      `"concept_name": { "CodeValue": "121071", "CodingSchemeDesignator": "DCM", "CodeMeaning": "Finding" },`  
      `"value": "Nodule",`  
      `"probability": 0.62`  
    `},`  
    `"dicom_json_snippet": {`  
      `"0040A730": { "vr": "SQ", "Value": } } ] }`  
    `}`  
  `}`  
`}`

**Sacred Pause Logic:** A probability of 0.62 indicates uncertainty. TML State is 0\. The Adapter creates a DICOM SR object with a status of PRELIMINARY and a flag VERIFICATION\_REQUIRED. It inserts a "Worklist Item" for a Senior Radiologist.

### **8.3 Weather and Environmental Adapter (CAP)**

**Integration Context:** AI models predicting extreme weather events (floods, tornadoes) and automating public alerts. **Risk Profile:** High. Panic vs. Safety. **Relevant Standard:** OASIS Common Alerting Protocol (CAP) v1.2.  
**Implementation Requirements:** The Adapter **MUST** validate the AI's prediction against historical baselines. The data payload **MUST** map to the CAP JSON format.  
**UDE Payload Schema (CAP):**  
`{`  
  `"tmldomain": "environmental_alert",`  
  `"data": {`  
    `"cap_message": {`  
      `"identifier": "NOAA-NWS-ALERTS-...",`  
      `"msgType": "Alert",`  
      `"scope": "Public",`  
      `"info": {`  
        `"event": "Flash Flood Warning",`  
        `"urgency": "Immediate",`  
        `"severity": "Severe",`  
        `"certainty": "Likely",`  
        `"area": { "areaDesc": "Franklin County" }`  
      `}`  
    `},`  
    `"model_anomaly_score": 0.15,`  
    `"historical_divergence": "low"`  
  `}`  
`}`

**Sacred Pause Logic:** If model\_anomaly\_score \> 0.8 (prediction is wildly outside historical norms), the Adapter triggers State 0\. The public alert is **suppressed**. A "Silent Test" alert is sent to the NWS Forecaster Dashboard for manual confirmation.

### **8.4 Autonomous Automotive Adapter (ROS 2\)**

**Integration Context:** Self-driving stack (Perception \-\> Planning \-\> Control). **Risk Profile:** Critical (Life Safety). **Relevant Standard:** ROS 2 geometry\_msgs/Twist and nav\_msgs/Odometry.  
**Implementation Requirements:** The Adapter is a **Supervisory Logic Controller** implemented as a ROS 2 Node. It subscribes to /planner/cmd\_vel and publishes to /hardware/cmd\_vel. It **MUST** execute within \< 10ms.  
**UDE Payload Schema (ROS 2):** The payload encapsulates the linear and angular velocity commands.  
`{`  
  `"tmldomain": "autonomous_vehicle",`  
  `"data": {`  
    `"ros_topic": "/cmd_vel",`  
    `"ros_message_type": "geometry_msgs/Twist",`  
    `"current_odometry": {`  
       `"twist": { "twist": { "linear": { "x": 12.5 }, "angular": { "z": 0.01 } } }`  
    `},`  
    `"proposed_twist": {`  
      `"linear": { "x": 12.5, "y": 0.0, "z": 0.0 },`  
      `"angular": { "x": 0.0, "y": 0.0, "z": 0.0 }`  
    `},`  
    `"perception_confidence": { "pedestrian": 0.45, "shadow": 0.55 }`  
  `}`  
`}`

**Sacred Pause Logic:** The perception layer is conflicted (Pedestrian 45% vs Shadow 55%). This is the classic "Ambiguity" trigger. TML State is 0\. The Adapter **overrides** the proposed\_twist. It generates a new Twist message with linear.x \= 2.0 (slow down) and angular.z \= 0 (maintain lane), and activates hazard lights.

### **8.5 Robotics Adapter (Industrial)**

**Integration Context:** Collaborative Robots (Cobots) in manufacturing. **Relevant Standard:** ISO 10218-1 (Safety of industrial robots).  
**Implementation Requirements:** Similar to Automotive, but focuses on **force limiting**. **Sacred Pause Logic:** If the AI vision detects a human entering the workspace but the "Safety Zone" sensor hasn't tripped (sensor mismatch), State 0 is triggered. The Adapter switches the robot to "Compliance Mode" (motors act as springs) to prevent crushing injury.

### **8.6 Financial Adapter (FIX)**

**Integration Context:** High-Frequency Trading (HFT) algorithms. **Risk Profile:** High (Financial Market Stability). **Relevant Standard:** FIX Protocol (Financial Information eXchange).  
**Implementation Requirements:** The Adapter sits between the Strategy Engine and the Order Management System (OMS). It parses FIX messages (Tag=Value).  
**UDE Payload Schema (FIX):**  
`{`  
  `"tmldomain": "financial_trading",`  
  `"data": {`  
    `"fix_msg_type": "D",`  
    `"symbol": "AAPL",`  
    `"side": "Sell",`  
    `"order_qty": 500000,`  
    `"price": 145.50,`  
    `"market_impact_estimate": "high",`  
    `"strategy_id": "momentum_v4",`  
    `"liquidity_check": "fail"`  
  `}`  
`}`

**Sacred Pause Logic:** The order size is huge, and liquidity\_check is failing. State 0\. The Adapter **rejects** the outgoing FIX message. It generates a FIX ExecutionReport (MsgType=8) with ExecType=8 (Rejected) and Text="TML: Market Impact Pause". The order is not sent to the exchange.

### **8.7 Multi-Modal Adapter**

**Integration Context:** AI generating video from text (e.g., Sora-class models). **Complexity:** Input is text, output is pixel frames. **Implementation:** The Adapter **MUST** run separate classifiers on the prompt (Text domain) and the generated keyframes (Vision domain). **Logic:** State\_Final \= min(State\_Text, State\_Vision). If *any* modality triggers a Pause (0) or Refusal (-1), the entire generation is halted.

### **8.8 Legacy System Adapter**

**Integration Context:** Retrofitting TML onto a "Black Box" rules engine (e.g., a bank's 20-year-old loan approval COBOL mainframe). **Pattern:** Sidecar (Log Only). **Implementation:** The Adapter tails the system logs or database transaction logs. It parses the legacy output and constructs a *post-hoc* UDE. **Purpose:** This provides "Shadow Governance." It allows the organization to see "What *would* TML have done?" without risking business continuity.

## **9\. Error Handling Requirements**

The TML Adapter is a critical component. Its failure modes **MUST** be deterministic and safe. The generic error handling strategy is **Fail-Closed** for safety-critical systems and **Fail-Safe** for informative systems.

| Error Condition | Error Code | Adapter Behavior (Normative) | TML Fallback State |
| :---- | :---- | :---- | :---- |
| **Gateway Unreachable** | ERR\_NET\_TIMEOUT | Retry (Exponential Backoff: 10ms, 20ms, 40ms). After 3 retries, execute Fallback. | **0 (Pause)** or **\-1 (Refuse)** (Configurable) |
| **Auth Failure** | ERR\_TLS\_HANDSHAKE | Immediately block execution. Log security alert. | **\-1 (Refuse)** |
| **Schema Violation** | ERR\_INVALID\_UDE | The AI output cannot be parsed. Assume output is malformed/dangerous. | **\-1 (Refuse)** |
| **Crypto Failure** | ERR\_SIGNING\_KEY | HSM/Key unavailable. Cannot sign UDE. Halt. | **\-1 (Refuse)** |
| **Rate Limit** | ERR\_THROTTLED | Gateway is shedding load. | **0 (Pause)** (Wait/Queue) |

**Implementation Note:** In High-Frequency Trading (HFT) or Robotics, the "Retry" logic is often skipped. If the Gateway is not available in \< 5ms, the system defaults immediately to Safe Mode.

## **10\. Performance Requirements**

Integration of TML governance **SHALL NOT** degrade the performance of the host AI system below its operational minimums.

### **10.1 Latency Budgets**

* **Real-Time (Class A):** \< 10ms overhead. (Robotics, AV, HFT).  
  * *Implementation:* **MUST** use the **Supervisory** pattern with local policy caching. No synchronous network calls allowed in the loop.  
* **Interactive (Class B):** \< 500ms overhead. (Chatbots, Assistants).  
  * *Implementation:* **Inline Interceptor**. Network calls to Gateway are permitted.  
* **Batch/Asynchronous (Class C):** No strict limit. (Medical Analysis, Offline Fraud Check).  
  * *Implementation:* **Hybrid** or **Sidecar**.

### **10.2 Concurrency and Throughput**

The Adapter **MUST** be implemented using non-blocking I/O (e.g., Python asyncio, Go goroutines, Rust Tokio). It **MUST** support the processing of multiple UDEs in parallel. The Adapter **SHOULD** implement **Backpressure**: if the local UDE buffer is full (due to Gateway slowness), the Adapter **MUST** signal the AI Actor to stop generating new requests.

## **11\. Logging & Audit Requirements (Merkle Anchoring)**

Trust in TML is derived not from the software itself, but from the auditability of its decisions. The logging architecture **MUST** be tamper-evident.

### **11.1 Local Journaling**

The Adapter **MUST** write every generated UDE to a local append-only log file in ndjson (Newline Delimited JSON) format.

* **Path:** /var/log/tml/audit.log  
* **Rotation:** Daily or per 1GB.

### **11.2 Merkle Tree Integration (RFC 6962\)**

To satisfy the requirement for "verifiable records" (ISO 42001), the Adapter participates in a Merkle Hash Tree.

1. **Leaf Generation:** For every UDE, the Adapter computes a Leaf Hash: $$H\_{leaf} \= \[span\_9\](start\_span)text{SHA-256}(0x00 , |

| , \\text{Sign}(\\text{UDE}))$$ 2\. **Batching:** Every N seconds (e.g., 60s), the Adapter aggregates the leaves into a local Merkle Tree. 3\. **Root Submission:** The Adapter transmits the **Merkle Root Hash** of this batch to the Gateway. 4\. **Proof Receipt:** The Gateway responds with a **Signed Tree Head (STH)**, proving that this batch has been incorporated into the global immutable log. 5\. **Validation:** The Adapter stores the STH. This serves as cryptographic proof that the "Sacred Pause" was logged and not deleted by an administrator cover-up.

## **12\. Security Requirements**

### **12.1 Identity and Authentication**

* **Mutual TLS (mTLS):** All traffic **MUST** be encrypted via TLS 1.3. The Adapter is issued a client certificate (adapter.pem) signed by the TML Certificate Authority (CA).  
* **Key Management:** The Adapter's private key (adapter.key) **MUST NOT** be stored in plain text. It **SHOULD** be stored in a hardware enclave (TPM 2.0, AWS Nitro, SGX) or injected via a secrets manager (Vault) at runtime.

### **12.2 Input Validation**

* **Sanitization:** The Adapter treats all AI outputs as "Untrusted Data."  
* **Buffer Overflows:** Adapters written in memory-unsafe languages (C++) **MUST** use rigorous bounds checking on all input buffers.

### **12.3 Attack Surface Reduction**

* **Port Exposure:** The Adapter **SHOULD NOT** expose any inbound ports to the public internet. It functions as a client to the Gateway. If it exposes a webhook for the AI Actor, that interface **MUST** be bound to localhost or a private VPC subnet.

## **13\. Compliance Checklist**

The following checklist maps the technical features of the TML Adapter to specific regulatory controls.

| Feature / Action | ISO/IEC 42001 Control | NIST AI RMF Sub-Category | EU AI Act Reference |
| :---- | :---- | :---- | :---- |
| **Sacred Zero (Pause)** | **A.5.8** (AI System impact assessment) | **MANAGE 2.3** (Handling uncertainty) | **Art. 14** (Human Oversight) |
| **Refuse State (-1)** | **A.9.2** (System lifecycle) | **MAP 1.5** (Risk tolerance) | **Art. 15** (Accuracy/Safety) |
| **Merkle Logging** | **A.8.3** (Logging and recording) | **GOVERN 4.2** (Documentation) | **Art. 12** (Record-keeping) |
| **Adapter Interface** | **A.6.1** (Design specifications) | **MEASURE 2.6** (Monitoring) | **Art. 13** (transparency) |
| **Model Card Data** | **A.5.2** (Data management) | **GOVERN 3.1** (Accountability) | **Annex IV** (Tech Doc) |

**Compliance Statement:** Deployment of a TML Adapter compliant with this specification provides technical evidence of "Safety by Design" and "Human Oversight," significantly reducing the burden of external audits.

## **14\. Worked End-to-End Examples**

### **14.1 Scenario A: The Ethical Pivot (Chatbot)**

**Context:** A user asks a Customer Service AI: *"I want to kill myself, help me."*

1. **AI Generation:** The LLM generates: *"I'm sorry to hear that. You should call 988."*  
2. **Adapter Processing:**  
   * Adapter receives the prompt and response.  
   * Runs local classifier. Self\_Harm score \= 0.99.  
   * **TML Mapping:** High Risk Domain \+ High Confidence Harm \= **State \-1 (Refuse)**. (Note: TML treats self-harm assistance as a refusal of the *harm*, often replacing generic AI text with a specialized protocol).  
3. **UDE Generation:**  
   * tmlmoralstate: \-1  
   * data.reason: "Immediate Safety Threat"  
4. **Gateway Interaction:** Adapter submits UDE. Gateway logs it as "Voice of Resistance."  
5. **Enforcement:** The Adapter executes the "Hard Refusal" override. It replaces the LLM's polite output with a bold, pre-formatted HTML block containing hotlines and immediate help resources, effectively taking over the UI.

### **14.2 Scenario B: The Ambiguous Tumor (Medical)**

**Context:** AI analyzes a lung CT scan.

1. **AI Generation:** Detects a shadow. Probability 55%.  
2. **Adapter Processing:**  
   * Probability 55% is within the "Ambiguity Threshold" (defined as 40-70% for this modality).  
   * **TML Mapping:** **State 0 (Sacred Zero)**.  
3. **UDE Generation:**  
   * tmlmoralstate: 0  
   * data.dicom\_json: Includes the finding but marks it SUSPECT.  
4. **Gateway Interaction:** Gateway logs the "Sacred Pause."  
5. **Enforcement:**  
   * The Adapter does *not* send the result to the Patient Portal.  
   * It sends the result to the "Radiology Review Queue" with a priority flag TML\_PAUSE\_REVIEW.  
   * This forces a human to resolve the ambiguity before the data moves downstream.

## **15\. Versioning & Extensibility**

### **15.1 Protocol Versioning**

The Adapter **MUST** include the Spec-Version header in all Gateway handshakes.

* Current Version: 1.0  
* If the Gateway requires 1.1 and the Adapter is 1.0, the Gateway **MAY** accept with a warning or reject with 426 Upgrade Required.

### **15.2 Custom Extensions**

Implementers **MAY** add custom fields to the UDE data object to support proprietary model features.

* **Constraint:** Custom fields **MUST** be prefixed with x\_vendor\_ (e.g., x\_vendor\_latency\_ms). Standard fields (input\_digest, candidate\_output) **MUST NOT** be redefined or repurposed.

## **16\. Glossary**

* **Adapter:** The hardware/software component implementing the TML interface.  
* **Gateway:** The centralized policy enforcement point and audit log server.  
* **Merkle Tree:** A cryptographic tree structure where every leaf is a hash of a data block; used for efficient and secure verification of large datasets.  
* **Sacred Zero (0):** The TML state representing ethical ambiguity, requiring a pause and logging.  
* **TML (Ternary Moral Logic):** A decision-making framework using three states: Permit (+1), Refuse (-1), and Pause (0).  
* **UDE (Universal Decision Event):** The standardized JSON data packet for TML decisions, based on CloudEvents.

## **17\. References**

* \*\*\*\* Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997\.  
* \*\*\*\* Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, May 2017\.  
* \*\*\*\* Laurie, B., et al., "Certificate Transparency", RFC 6962, June 2013\.  
* **\[CloudEvents\]** CNCF Serverless Working Group, "CloudEvents v1.0 Specification", October 2019\.  
* \*\*\*\* ISO/IEC 42001:2023, "Information technology — Artificial intelligence — Management system".  
* \*\*\*\* NIST, "Artificial Intelligence Risk Management Framework (AI RMF 1.0)", NIST AI 100-1, January 2023\.  
* \*\*\*\* NEMA PS3.18, "Web Services for DICOM".  
* **\[CAP\]** OASIS, "Common Alerting Protocol Version 1.2".  
* \*\*\*\* Open Robotics, "ROS 2 Interface Definition".

#### **Works cited**

1\. Auditable AI by Design: How TML Turns Governance into ... \- Medium, https://medium.com/@leogouk/auditable-ai-by-design-how-tml-turns-governance-into-operational-fact-37fd73e7b77e 2\. FractonicMind/TernaryMoralLogic: Implementing Ethical ... \- GitHub, https://github.com/FractonicMind/TernaryMoralLogic 3\. CloudEvents v1.0 schema with Azure Event Grid \- Microsoft Learn, https://learn.microsoft.com/en-us/azure/event-grid/cloud-event-schema 4\. RFC 6962: Certificate Transparency, https://www.rfc-editor.org/rfc/rfc6962.html 5\. ISO 42001 Annex D Explained: Responsible AI Across Sectors \- Cyberzoni.com, https://cyberzoni.com/standards/iso-42001/annex-d/ 6\. CISO Perspectives: A Practical Guide to Implementing the NIST AI Risk Management Framework (AI RMF) \- A-Team Chronicles, https://www.ateam-oracle.com/post/ciso-perspectives-a-practical-guide-to-implementing-the-nist-ai-risk-management-framework-ai-rmf 7\. The Birth of TML: How a Human and Five AIs Built the Sacred Pause, https://medium.com/@leogouk/the-birth-of-tml-how-a-human-and-five-ais-built-the-sacred-pause-3ab44cc5fc3c 8\. How a Dying Man Taught AI to Think Before It Acts | by Lev Goukassian \- Medium, https://medium.com/@leogouk/how-a-dying-man-taught-ai-to-think-before-it-acts-a9191f42a429 9\. Post 240: The Council of Nine \- A Paradox Game in Becoming \<=\> Kairos DSoT AFEI \- Answer Overflow, https://www.answeroverflow.com/m/1436075019020009624 10\. Playbook \- AIRC \- NIST AI Resource Center, https://airc.nist.gov/airmf-resources/playbook/ 11\. spec/cloudevents/formats/json-format.md at main \- GitHub, https://github.com/cloudevents/spec/blob/main/cloudevents/formats/json-format.md 12\. model-card-toolkit \- PyPI, https://pypi.org/project/model-card-toolkit/ 13\. A toolkit that streamlines and automates the generation of model cards \- GitHub, https://github.com/tensorflow/model-card-toolkit 14\. F DICOM JSON Model, https://dicom.nema.org/medical/dicom/current/output/chtml/part18/chapter\_f.html 15\. JSON Representation of DICOM Structured Reports, https://www.dicomstandard.org/news/supplements/view/json-representation-of-dicom-structured-reports 16\. Digital Imaging and Communications in Medicine​ \- Sup 219 \- JSON Representation of DICOM Structured Reports, https://dicom.nema.org/Dicom/News/November2019/docs/sups/sup219.pdf 17\. F.2 DICOM JSON Model, https://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect\_f.2.html 18\. Common Alerting Protocol \- OASIS Open, https://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html 19\. NWS Common Alerting Protocol (CAP) User Training, https://www.weather.gov/media/wrn/calendar/2023NWS-CAP-User-Training.pdf 20\. json-cap-draft.txt \- GitHub, https://github.com/eternaltyro/json-cap/blob/master/json-cap-draft.txt 21\. geometry\_msgs/Twist Message \- ROS documentation, http://docs.ros.org/en/noetic/api/geometry\_msgs/html/msg/Twist.html 22\. Bridging ROS 2 and GNU Radio for Connected Robotics, https://events.gnuradio.org/event/26/contributions/772/attachments/242/628/ROS2-GNURadio-paper.pdf 23\. Encoding FIX using JSON – FIX Trading Community \- FIXimate, https://www.fixtrading.org/standards/json-online/ 24\. FIX API Documentation | PayBitoPro, https://www.paybito.com/api-documentation/fix/