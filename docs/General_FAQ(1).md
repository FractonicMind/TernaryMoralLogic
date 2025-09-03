# General FAQ on Ternary Moral Logic (TML) and Auditable AI

---

## Chapter 1: Core Framework

**Q1: What is the Ternary Moral Logic (TML) Framework**  
TML is an enforcement framework that requires organizations to generate and preserve **Moral Trace Logs** whenever AI makes ethically complex decisions. These logs are cryptographically sealed, time-stamped, and designed to be admissible in court. If logs are missing, liability attaches to the organization. TML shifts accountability from voluntary ethics to verifiable evidence.  

**Q2: How is TML different from Explainable AI (XAI)**  
Explainable AI provides interpretations such as graphs or heat maps. These are useful for engineers but inadmissible in court. TML produces signed logs that satisfy legal standards for digital evidence. Courts accept authenticated logs, not visualizations. TML is about **evidence, not explanation**.  

**Q3: Why is Auditable AI necessary**  
Because without records, there is no accountability. If an AI harms someone, companies can deny fault. Victims cannot prove their case. Regulators cannot enforce compliance. Auditable AI ensures that accountability is based on permanent, verifiable logs that no organization can erase or rewrite.  

**Q4: What is a Moral Trace Log**  
It is the backbone of TML. Each log records:  
- Who may be affected  
- What risks exist  
- What alternatives were considered  
- What principles were applied  
- What action was chosen  

Logs are hashed, signed, and preserved. Under the Federal Rules of Evidence, such authenticated records can be admitted in court under Rule 901 (authentication), Rule 902 (self-authenticating records), and Rule 803(6) (business records exception).  

**Q5: What counts as an ethically complex decision**  
Any AI decision that could affect human welfare, dignity, or rights. Examples include:  
- Medical recommendations  
- Loan approvals or denials  
- Hiring decisions  
- Autonomous driving choices  
- Content moderation and free speech  
- Insurance claims  
- Child protection assessments  
- Elder care recommendations  

---

## Chapter 2: The Sacred Pause and Risk

**Q6: What is the Sacred Pause**  
The Sacred Pause is a checkpoint. When the AI reaches an ethically complex decision, it must record its reasoning before completing the action. This log is generated in parallel and does not delay the outward response. It ensures that serious decisions never vanish into silence.  

**Q7: What are the three states of TML**  
+1 Proceed: Routine decisions with basic record keeping  
0 Sacred Pause: Complex decisions requiring detailed logs  
−1 Prohibit: Too dangerous, the system must refuse and explain why  

**Q8: What is Stakeholder Proportional Risk Level (SPRL)**  
SPRL is a risk score measuring who could be affected, how severe harm might be, the probability of harm, and whether vulnerable groups are involved.  

**Q9: How do companies use SPRL**  
Organizations set thresholds. Lower thresholds create more logs, higher thresholds create fewer. Both extremes are subject to audit. A normal range of logs is expected. Outliers attract scrutiny.  

**Q10: What prevents manipulation of thresholds**  
Thresholds are monitored through statistical auditing, competitor comparisons, and council oversight. If logs are too few, fraud is presumed. If logs are excessively frequent without cause, evasion is presumed. Silence itself is evidence.  

**Q11: What about adversarial attempts to bypass SPRL**  
TML anticipates such attacks. Input streams are monitored with anomaly detection. Training data is cryptographically signed. Oversight councils require penetration testing. Even if adversarial attempts succeed, responsibility remains with the deploying organization.  

---

## Chapter 3: Victim Rights and Support

**Q12: What rights do victims gain under TML**  
Victims gain powerful legal tools:  
- Right to demand logs that show what the AI did  
- Automatic liability for organizations when logs are missing  
- Free legal representation from the Memorial Fund  
- Expert witnesses to explain harm  
- Class action coordination for systemic harms  
- Priority assistance for vulnerable populations  

**Q13: What is the Lev Goukassian Memorial Fund**  
It is financed by penalties, not taxpayers. It provides victims with emergency medical help, legal teams, psychological support, expert testimony, and public advocacy. Its mission is to ensure that victims of AI are never left without recourse.  

---

## Chapter 4: Legal Framework and Admissibility

**Q14: What penalties enforce TML compliance**  
TML relies on existing laws. For example:  
- False attestation under **18 U.S.C. §1001**: up to five years imprisonment for organizations  
- Log tampering under **18 U.S.C. §1519**: up to twenty years  
- Threshold manipulation: prosecuted as fraud with treble damages  
- Repeated violations: corporate sanctions or dissolution under jurisdictional law  

**Q15: Are Moral Trace Logs admissible in court**  
Yes. Logs are designed for admissibility.  
- **Authentication**: Rule 901 requires proof of authenticity, satisfied by hashes and metadata.  
- **Self-authentication**: Rule 902(13) and (14) allow certified electronic records without outside proof.  
- **Business records**: Rule 803(6) covers logs made in the regular course of operation.  

Courts have upheld that the possibility of tampering does not exclude digital evidence if integrity safeguards exist.  

**Q16: How is chain of custody maintained**  
Every access, transfer, or verification of logs is itself logged with cryptographic receipts. Chain of custody is not a claim, it is a record of records.  

---

## Chapter 5: Governance and Oversight

**Q17: Who oversees TML**  
TML is governed by an international council of eleven institutions:  

- **Universities**: Stanford, MIT, Harvard, Oxford, Cambridge  
- **Research bodies**: Brookings Institution, RAND Corporation, Alan Turing Institute  
- **International organizations**: United Nations, World Health Organization, European Commission  

### Voting System  
The council uses a **weighted voting system**:  
- Each of the 11 institutions has one vote.  
- Decisions on investigations and access require a simple majority (6 of 11).  
- Decisions on penalties, sanctions, or standards require a supermajority (8 of 11).  
- Emergency actions to prevent imminent harm require two-thirds approval but can be triggered provisionally by any three institutions, pending full council review.  
- Leadership rotates annually to prevent dominance by any one region.  

**Q18: What powers does the council have**  
The council can review logs, subpoena missing records, authorize whistleblower rewards, refer violations to regulators, and publish findings. It may also act in emergencies to prevent imminent harm.  

**Q19: How is access controlled**  
Access is read-only, time-limited, and cryptographically signed. Every viewing generates a receipt, creating transparency even for investigators.  

---

### The Watchdog Role of Whistleblowers

**Q20: Why are whistleblowers essential**  
Because insiders often see misconduct before audits detect it. Without whistleblowers, silent log deletions or threshold gaming might never come to light.  

**Q21: How are whistleblowers protected**  
They can report anonymously. They receive rewards funded from penalties. Retaliation against them creates new liability.  

**Q22: What prevents abuse of whistleblower protections**  
False reports are investigated, and knowingly fraudulent claims are prosecuted. This balance ensures integrity: genuine whistleblowers are protected, while abusers are deterred.  

**Q23: Why can organizations not silence whistleblowers**  
Because retaliation itself becomes evidence. Attempts to silence insiders only strengthen the case against the organization.  

---

## Chapter 6: Implementation

**Q24: How do organizations implement TML**  
Step by step:  
1. Install logging functions alongside existing systems  
2. Set initial SPRL thresholds  
3. Validate coverage with audits  
4. Train staff on procedures  
5. Pilot deployment on a limited percentage of systems  
6. Expand to full deployment  

**Q25: What is the cost of a pilot**  
Limited pilots require modest engineering and minimal storage. Cryptographic services already exist in most infrastructures. The cost is far lower than litigation or reputational loss.  

**Q26: What challenges do organizations face during implementation**  
Challenges include calibrating thresholds, training teams, and ensuring legacy systems can be retrofitted. These are transitional costs, not permanent burdens.  

---

## Chapter 7: Integration with Laws

**Q27: How does TML integrate with the EU AI Act**  
It makes compliance provable. Companies can show regulators the logs as evidence of conformity.  

**Q28: How does TML integrate with GDPR**  
Logs preserve reasoning but anonymize identities. This protects privacy while keeping accountability intact.  

**Q29: How does TML integrate with HIPAA**  
Logs record medical AI recommendations. Hospitals can demonstrate that decisions were documented in line with patient safety.  

**Q30: How does TML align with NIST standards**  
NIST sets the standards for AI risk management. TML complements this by producing forensic logs that prove whether standards were followed.  

**Q31: How does TML work across borders**  
Moral Trace Logs are cryptographically universal. They can be admitted under UNCITRAL model laws and digital evidence frameworks worldwide.  

---

## Chapter 8: Adoption and Benefits

**Q32: Why should organizations adopt TML early**  
Because it provides both shield and advantage. Logs defend against legal claims, generate trust, and create proprietary datasets that improve AI. Early adopters set the standards others must follow.  

**Q33: What is the strategic value of adoption**  
Adoption builds reputational trust, secures regulatory goodwill, and creates competitive advantage. Organizations that adopt late face penalties without preparation.  

**Q34: What is the long-term organizational benefit**  
TML transforms accountability into an asset. Logs provide evidence, reduce exposure to liability, and generate feedback that continuously improves systems.  

---

## Chapter 9: Future Systems

**Q35: What about Artificial General Intelligence (AGI)**  
TML is essential. AGI will make millions of decisions per second across domains. Without logs, it becomes unaccountable. With logs, it remains auditable.  

**Q36: Does TML apply proportionally**  
Yes. TML targets ethically complex decisions, not trivial ones. This proportionality ensures efficiency and relevance.  

**Q37: Does TML conflict with privacy laws**  
No. Logs anonymize or pseudonymize personal identifiers. They preserve accountability while protecting individuals.  

**Q38: What prevents misuse of logs by malicious actors**  
Logs are read-only, sealed, and court-supervised. Sensitive data may be redacted, and misuse attempts are prosecutable.  

---

**Closing Statement**  
TML is the foundation of Auditable AI. It transforms accountability from principle into law. Moral Trace Logs create verifiable evidence, protect victims, and strengthen trust. For organizations, early adoption is a shield and an advantage. For societies, it is a safeguard against unaccountable intelligence.  
