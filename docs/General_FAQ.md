# **General FAQ**

---

## **Introduction**

Ternary Moral Logic (TML) is a **universal accountability framework** for artificial intelligence — a constitutional layer for machines.

At its core lies **Always Memory**: Every AI action must create an immutable, cryptographically sealed memory before execution.

**No memory \= No action.**

Created by Lev Goukassian (ORCID: 0009-0006-5966-1243) who, facing terminal illness, chose to dedicate his remaining time to building accountability infrastructure for humanity.

**Sacred Zero is exactly what's needed where lives and billions are on the line.**

---

## **TML – Foundation**

**Q1: What are the three states of TML?**

TML operates through a ternary structure:

* **\+1 (Proceed)**: Routine, low-risk actions  
* **0 (Sacred Zero)**: Ethically complex actions trigger pause and review  
* **\-1 (Refuse)**: Unsafe, malicious, or prohibited actions blocked

This ternary decision gate is absolute: no system escapes it.

**Q2: From Explainable AI (XAI) to Auditable AI (AAI): The Paradigm Shift**

Explainable AI tried to provide real-time "explanations," but these were subjective narratives with no legal standing. Courts cannot prosecute with explanations.

Auditable AI (AAI), enabled by TML, replaces storytelling with evidence. Every morally complex AI decision generates immutable, court-admissible records.

**Q3: Why did XAI fail, and why does AAI succeed?**

**XAI failed because:**

* Explanations were subjective interpretations  
* Companies controlled the narrative  
* Victims had no legal recourse  
* No criminal accountability existed

**AAI succeeds because Always Memory logs provide:**

* Immutable evidence for courts  
* Criminal penalties for missing documentation  
* Victim access to proof of harm  
* Direct executive accountability

---

## **Sacred Zero**

**Q1: What is Sacred Zero?**

Sacred Zero is the programmed act of hesitation — a deliberate pause where moral complexity is detected. It is not delay, but reflection encoded in code.

**Q2: How does the Sacred Zero circuit breaker work?**

When triggered:

1. The system pauses the action  
2. A confirmation request is sent to a designated human or council  
3. A short window (500ms) is given to confirm  
4. Confirm → execute; Timeout → abort  
5. All outcomes and policies are immutably logged

**Q3: How is alert fatigue prevented?**

* First 5 Sacred Zeros/hour → manual review  
* Subsequent similar events → auto-blocked with cooldown  
* Immutable policy hashes logged, preventing blame-shifting  
* Mandatory independent audits of Sacred Zero councils

---

## **Always Memory**

**Q1: What is Always Memory?**

Always Memory mandates: **no log \= no action**. Every AI action must generate a cryptographically sealed, timestamped record before execution. This is not configurable, optional, or retrospective.

**Q2: What exactly gets logged?**

* Microsecond timestamps  
* Batch \+ action IDs  
* Input/output hashes  
* Model version hash  
* Classification (+1/0/-1)  
* Hardware attestation quotes  
* Ephemeral HSM signature  
* Guardian confirmations  
* Proof-of-publication receipts

**Q3: What is Asynchronous Attested Batching (AAB)?**

* Actions are buffered inside TEEs  
* Batches sealed every 100ms or 1,000 actions  
* Overhead amortized; per-action latency \<1ms for high-throughput

**Q4: What are the realistic latency profiles?**

* **Standard**: 200-300ms (finance, healthcare)  
* **Priority**: 50-100ms (time-sensitive ops)  
* **Emergency**: 30-45ms (life-critical, e.g., braking)

**Q5: How does Always Memory handle traffic spikes?**

* Adaptive batch intervals  
* Backpressure (HTTP 429\)  
* Priority queues  
* Client-side reconciliation  
* Graceful degradation, never silent failure

---

## **The Goukassian Promise**

**Q1: What is the Goukassian Promise?**

The Promise anchors TML in conscience:

* Pause when truth is uncertain  
* Refuse when harm is clear  
* Proceed when truth is evident

If names are erased, the vow remains. If memory fades, the Lantern burns on. The Promise ensures moral grounding beyond law or profit.

**Q2: What are the three sacred commitments?**

🔦 **The Lantern**: Illuminates ethical paths — systems demonstrate moral deliberation

✍️ **The Signature**: Creator's ORCID (0009-0006-5966-1243) cryptographically embedded

📜 **The License**: Legal terms protecting proper use and punishing misuse

---

## **The Memorial Fund**

**Q1: What is the Memorial Fund?**

A financial pool funded by compliance fees and penalties. It provides:

* Direct compensation to victims of AI harms  
* Long-term remembrance of those affected  
* A perpetual link between TML enforcement and human dignity

**Q2: How is the Memorial Fund financed?**

* 30-40% of penalties from violations  
* Commercial licensing fees  
* Foundation grants  
* Industry consortium contributions

---

## **Victim & Whistleblower Protection**

**Q1: How does whistleblower protection work?**

* 15% bounty of collected penalties  
* Anonymous submission channels  
* Technical safeguards against deanonymization  
* Criminal prosecution for retaliation  
* Legal support from Memorial Fund

**Q2: How are victims supported?**

* Minimum 30% of penalties allocated directly to victims  
* 40% for vulnerable populations  
* Claims process immutably logged  
* Memorial Fund disburses within fixed timelines  
* Lifetime support for permanent AI-caused disabilities

---

## **The Hybrid Shield**

**Q1: What is the Hybrid Shield?**

The dual-layer defense of TML:

**Institutional Shield**: Logs mirrored across 11 independent institutions worldwide

**Mathematical Shield**: Root hashes anchored to public blockchain

Together: redundancy \+ immutability. Byte changes break hashes, revealing tampering instantly.

**Q2: Which institutions hold memories?**

Categories (rotating every 7 years):

* 4 Academic research institutions  
* 3 Technical standards bodies  
* 2 Civil society organizations  
* 2 International governance bodies

---

## **Guardians**

**Q1: What is the two-tier Guardian architecture?**

**Full Guardians**: Operate TEEs/HSMs, create and sign log batches

**Lightweight Guardians**: Verify signatures and anchor proofs without special hardware

**Q2: How are Guardians selected and rotated?**

* Daily random selection via stake-weighted VRF  
* Random sharding prevents collusion  
* Automatic ejection of compromised types

**Q3: How does governance prevent capture?**

* On-chain binding votes  
* Quadratic voting for fairness  
* Time-locked vesting for Genesis Guardians  
* Automated slashing for misbehavior

---

## **Implementation & Economics**

**Q1: What are the realistic costs?**

* **Pilot**: \~$250K first year  
* **Small enterprise**: \~$2M/year  
* **Large enterprise**: \~$11M/year

Costs reduced through shared Guardians, selective fidelity, and foundation subsidies.

**Q2: How are costs stabilized?**

* EIP-1559 style fee mechanism  
* Delegated staking  
* Base fee stability; variable tips

**Q3: What's the phased adoption path?**

1. **Shadow Mode**: Logging only  
2. **Selective Enforcement**: Critical decisions  
3. **Full Always Memory**: All actions logged

---

## **Performance & Latency**

**Q1: How does Multi-TEE Diversity protect the system?**

Mandatory heterogeneous infrastructure:

* 40% Intel SGX  
* 40% AMD SEV-SNP  
* 20% AWS Nitro Enclaves

Side-channel attacks limited to single architecture. Protocol-level ejection of compromised types.

**Q2: What about universal vulnerabilities?**

* Minimal unikernel runtimes  
* Formally verified cryptographic libraries  
* Zero-TEE fallback with 80% BFT consensus

---

## **Integration with Law**

**Q1: How does TML achieve GDPR compliance?**

* Data encrypted with single-use keys  
* Erasure triggers key deletion \+ attested shredding  
* Signed attestations prove destruction

**Q2: Are Always Memory logs legally admissible?**

Yes. They meet FRE 901/902 via:

* Independent Guardian confirmations  
* Cryptographic proof chains  
* Expert witness program  
* NIST standards engagement

**Q3: What's the enforcement mechanism?**

* Missing logs \= negligence  
* Forged logs \= fraud  
* Tampering \= obstruction  
* Systematic abuse \= RICO

**Q4: How does TML integrate with EU AI Act?**

TML exceeds all requirements:

* Risk categorization → Sacred Zero classification  
* Documentation requirements → Always Memory logs  
* Human oversight → Accountability Council  
* Transparency → Immutable public evidence

---

## **Future Technologies & AGI Readiness**

**Q1: How is Always Memory future-proof?**

* Log formats versioned  
* Adaptable to neuromorphic, quantum, swarm AIs  
* Designed as invisible infrastructure (like double-entry bookkeeping)

**Q2: Can Always Memory handle AGI?**

Not at full AGI speed initially. Current mitigations:

* Checkpoint logging for major decisions  
* Hierarchical compression of reasoning  
* Commitment contracts before action chains

The principle remains: Any system affecting humans must create memories of its decisions.

---

## **Early Adoption Benefits & Flywheel**

**Q1: What benefits exist before laws mandate adoption?**

* Insurance discounts (20-30% documented)  
* Regulatory fast-track  
* Public trust advantage  
* Internal risk visibility  
* Safe harbor provisions

**Q2: How does TML create a trust flywheel?**

Better Logs → Better Training → Better Decisions → Richer Logs

Each cycle strengthens both compliance and credibility. Self-reinforcing adoption:

1. Early adopters gain trust advantage  
2. Insurers reduce premiums  
3. Regulators reference TML as standard  
4. Competitors forced to adopt  
5. Network effects reduce costs  
6. Universal adoption becomes inevitable

---

## **Resilience & Contingencies**

**Q1: What if all TEEs are compromised?**

* Immediate ejection of compromised type  
* Zero-TEE fallback with 80% BFT consensus

**Q2: What if Guardians collude?**

* Stake-weighted selection makes Sybils uneconomic  
* Random sharding breaks predictability  
* Slashing enforces accountability

**Q3: What if the Legal Defense Fund is exhausted?**

* Reinsurance caps exposure  
* Emergency assessments  
* Foundation reserves

---

## **Adversarial Attacks**

**Q1: What about side-channel or hardware exploits?**

* Multi-TEE diversity ensures no single exploit compromises the whole network  
* Formal verification of minimal runtimes reduces shared-library attack surfaces  
* Protocol-level ejection instantly removes a compromised TEE class

**Q2: Can Guardians be bribed or captured?**

* Stake-weighted selection makes collusion prohibitively expensive  
* Random sharding ensures unpredictability of signing sets  
* Slashing rules and public audit logs make misconduct both visible and costly

**Q3: Can attackers flood Always Memory with fake actions?**

* Backpressure (429 signals) and adaptive batching throttle denial-of-service attempts  
* Priority queues ensure critical transactions are protected under attack  
* Client-side reconciliation forces attackers to pay the cost of repeated retries

**Q4: What about poisoning of logs or false entries?**

* Immutable signatures and hash-chains make undetected falsification impossible  
* Hybrid Shield's 11-mirror institutional redundancy prevents silent erasure  
* Blockchain anchoring exposes divergence within a single block cycle

**Q5: What if attackers target whistleblowers or victims?**

* Anonymous reporting channels preserve identity  
* Guardian-hardened routing prevents IP leakage  
* 15% whistleblower bounties \+ Memorial Fund disbursements align incentives against retaliation

**Q6: How does Always Memory defend against Denial-of-Service attacks?**

**Network defenses:**

* DDoS-absorbing CDN/WAF (Cloudflare/AWS Shield)  
* Anycast \+ global edge points spread volumetric load  
* Token-based auth with sliding quotas per client

**Protocol defenses:**

* Adaptive batching: as buffer fills, batch frequency increases  
* Priority queues: high-fee/critical clients get faster processing  
* Backpressure: HTTP 429 with Retry-After when approaching capacity  
* Early drop: unauthenticated requests dropped before TEE entry

**Economic defenses:**

* Fee market makes sustained attacks expensive  
* Staking penalties for Guardians enabling floods  
* Per-request minimal fees during high load

**Emergency modes:**

* Graceful degradation to sample-only for non-critical  
* Zero-TEE fallback when TEE nodes under attack  
* Circuit-breaker preserves capacity for high-value operations

---

## **Technical Specifications**

**Q1: What is a sample Always Memory batch?**

{  
  "framework": "TML-AlwaysMemory-v5.0",  
  "creator\_orcid": "0009-0006-5966-1243",  
  "batch\_id": "batch\_8a4f2c3b5e1d",  
  "timestamp\_range": {  
    "start": "2025-09-21T14:23:45.123456Z",  
    "end": "2025-09-21T14:23:45.223456Z"  
  },  
  "actions": \[  
    {  
      "action\_id": "act\_7f3a9c2b4e1d",  
      "classification": 0,  
      "input\_hash": "0x9e2b4d1a3c5f...",  
      "output\_hash": "0x4d7e2a9b1c3f...",  
      "sacred\_zero\_trigger": "loan\_denial\_protected\_class"  
    }  
  \],  
  "tee\_attestation": {  
    "platform": "AMD-SEV-SNP",  
    "quote": "attest:sev-snp:...",  
    "runtime": "unikernel-v2.1"  
  },  
  "signature": {  
    "algorithm": "ECDSA-P384",  
    "ephemeral\_key\_id": "eph\_2a3b4c5d",  
    "hsm\_root": "hsm\_7f8a9b0c",  
    "signature": "0x1a2b3c4d5e6f..."  
  },  
  "guardian\_confirms": \[  
    {"id": "g1", "type": "full", "sig": "0xf2e4..."},  
    {"id": "g2", "type": "lightweight", "sig": "0x8a9b..."}  
  \],  
  "goukassian\_promise": {  
    "lantern": true,  
    "signature": "0009-0006-5966-1243",  
    "license": "MIT-Attribution-Required"  
  },  
  "operational\_mode": "normal",  
  "liability\_factor": 1.0  
}

---

## **Conclusion**

TML with Always Memory represents a paradigm shift in AI accountability:

**Technically**: Every failure mode mapped with mitigation

**Economically**: Costs acknowledged, scaled by liability

**Legally**: Evidence that stands in court

**Morally**: Sacred Zero ensures conscience in code

This is not perfection. This is something rarer: **memory that power cannot erase, evidence that courts cannot dismiss, and conscience that machines cannot ignore.**

The Lantern shines beyond names. The framework outlives its creator. The promise endures.

**Sacred Zero is exactly what's needed where lives and billions are on the line.**

---

**Document Version**: 5.0 Resilience Edition  
 **Last Updated**: September 2025  
 **Creator**: Lev Goukassian (ORCID: 0009-0006-5966-1243)  
---

*"Routine memories are cheap; missing memories are expensive."*

