# **Ternary Moral Logic (TML) – General FAQ v5.0 (Resilience Edition)**

---

## **Introduction**

Ternary Moral Logic (TML) is a **universal accountability framework** for artificial intelligence — a constitutional layer for machines.

At its core lies **Always Log Mode (ALM)**:

**No log \= No action.**

Every AI decision, trivial or profound, is preceded by an immutable, cryptographically sealed log. This transforms ethics from aspiration into **evidence**.

TML is not a commercial product. It is a **legacy project**, created by Lev Goukassian (ORCID: 0009-0006-5966-1243) who, facing terminal illness, chose to dedicate his remaining time to building accountability infrastructure for humanity.

**Sacred Zero is exactly what's needed where lives and billions are on the line.**

---

## **Core Principles**

**Q1: What are the three states of TML?**

* **\+1 (Proceed)**: Routine, low-risk actions execute with minimal metadata  
* **0 (Sacred Zero)**: Ethically complex actions trigger a deliberate act of reflection — a log of reasoning, alternatives, and risks  
* **\-1 (Refuse)**: Unsafe, malicious, or prohibited actions are blocked, with refusal logged

All three states receive identical logging treatment. The classification aids human investigation, not system behavior.

**Q2: What is Always Log Mode (ALM)?**

ALM mandates that every AI action produces a cryptographically signed log before execution. This principle is absolute. ALM v5.0 incorporates:

* **Asynchronous Attested Batching (AAB)** for realistic performance  
* **Multi-TEE diversity** with Zero-TEE fallback  
* **Two-tier validator architecture** for economic viability  
* **Cryptographic erasure with attested shredding** for GDPR compliance  
* **Sacred Zero circuit breaker** with policy-defined human oversight  
* **Comprehensive residual risk mitigations** from external due diligence

**Q3: What exactly gets logged?**

Each batch log includes:

* Timestamp range (microsecond precision)  
* Unique batch and action identifiers  
* Input/output hashes for each action  
* Model name, version, configuration hash  
* Classification array (+1/0/-1)  
* Hardware attestation quote (TEE-specific)  
* Cryptographic signature (ephemeral HSM key)  
* Proof-of-publication receipts  
* Validator confirmations (k-of-n threshold)  
* Goukassian Promise elements

---

## **The Goukassian Promise**

**Q4: What is the Goukassian Promise?**

Three sacred commitments embedded in every TML implementation:

🔦 **The Lantern**: Illuminates ethical paths — systems demonstrate capacity for moral deliberation

✍️ **The Signature**: Creator's ORCID (0009-0006-5966-1243) cryptographically embedded in every log

📜 **The License**: Legal terms that protect proper use and punish misuse

These aren't decorative. They're functional commitments that bind the technology to its ethical purpose:

* Pause when truth is uncertain  
* Refuse when harm is clear  
* Proceed where truth is

---

## **The Hybrid Shield**

**Q5: What is the Hybrid Shield?**

TML ensures logs cannot be erased or falsified through dual armor:

**Layer 1 \- Institutional Shield**:

* Real-time replication to 11 independent institutions  
* Geographic and jurisdictional diversity  
* Rotating institutions prevent capture

**Layer 2 \- Mathematical Shield**:

* Daily root hashes to public blockchains  
* Mathematical proof against tampering  
* Permanent checkpoints even if validators collude

*Alter one byte? Hash breaks.*

---

## **Performance & Scalability**

**Q6: What is Asynchronous Attested Batching (AAB)?**

AAB improves performance by buffering actions inside TEEs and sealing them in batches:

* Amortizes TEE transition cost (\~17,000 cycles) across thousands of actions  
* Reduces per-action overhead to \<1ms in high-throughput systems  
* Enables tiered latency modes for different use cases

**Q7: What are the realistic latency profiles?**

**Standard ALM** (200-300ms):

* Use: Financial decisions, medical diagnostics  
* Full distributed validation

**Priority ALM** (50-100ms):

* Use: Time-sensitive business logic  
* Fee-based priority processing

**Emergency ALM** (30-45ms):

* Use: Autonomous braking, life-critical only  
* Requires proof that Standard ALM causes harm

**Q8: How does ALM handle traffic spikes?**

* Adaptive batching intervals based on load  
* Backpressure signaling (HTTP 429\)  
* Priority fee-based queues  
* Client-side reconciliation for in-flight transactions  
* Graceful degradation rather than catastrophic failure

---

## **Security Architecture**

**Q9: How does Multi-TEE Diversity protect the system?**

Mandatory heterogeneous infrastructure:

* 40% Intel SGX nodes  
* 40% AMD SEV-SNP nodes  
* 20% AWS Nitro Enclaves  
* Side-channel attacks limited to single architecture  
* Protocol-level ejection of compromised TEE types  
* Formal verification of core attestation logic

**Q10: What about universal vulnerabilities?**

* Minimal unikernel runtimes (reduce shared attack surface)  
* Formally verified cryptographic libraries  
* Zero-TEE fallback mode with 80% BFT consensus  
* Emergency operations continue even with total TEE failure

**Q11: How are HSMs secured?**

* Ephemeral, single-use credentials per batch  
* Mandatory 30-day key rotation  
* Automated IAM policy scanning  
* HashiCorp Vault for secrets management  
* API anomaly detection  
* Reference Terraform modules provided

---

## **Validator Network & Governance**

**Q12: What is the two-tier validator architecture?**

**Full Validators**:

* Run TEEs and HSMs  
* Create and sign attested batches  
* Higher rewards, higher requirements

**Lightweight Validators**:

* No specialized hardware required  
* Verify signatures and anchor proofs  
* Enable academic/NGO participation

**Q13: How are validators selected and rotated?**

* Stake-weighted VRF selection (prevents Sybil attacks)  
* Daily rotation of active validator set  
* Random sharding per batch (prevents collusion)  
* 7-year maximum terms with staggered rotation

**Q14: How does governance prevent capture?**

* **Quadratic Voting**: Prevents plutocracy by making successive votes increasingly expensive  
* **Time-locked vesting**: Genesis Partners cannot consolidate power immediately  
* **Automated slashing**: Protocol-enforced penalties for provable misbehavior  
* **Master Validator Agreement**: Legal framework for disputes  
* **Binding on-chain votes**: Major decisions require community consensus

---

## **Economics & Implementation**

**Q15: What are the realistic costs?**

**Pilot** (1 model, 1M tx/month):

* Year 1: \~$250K  
* Ongoing: \~$150K/year

**Small Enterprise** (10 models, 100M tx/month):

* Year 1: \~$2.5M  
* Ongoing: \~$2M/year

**Large Enterprise** (100+ models, 10B+ tx/month):

* Year 1: \~$15M  
* Ongoing: \~$11M/year

**Q16: How are costs stabilized?**

* EIP-1559 style base fee \+ tip mechanism  
* Delegated staking creates reputation markets  
* ALM Foundation negotiates bulk hardware rates  
* Tiered storage (hot/warm/cold) optimization  
* Selective fidelity for non-critical operations

**Q17: What's the phased adoption path?**

**Phase 1** (Months 1-3): Shadow Mode

* Parallel logging without enforcement  
* Performance benchmarking  
* No WALT requirement

**Phase 2** (Months 4-6): Selective Enforcement

* Critical decisions only  
* Human-in-loop for Sacred Zero  
* Gradual rollout

**Phase 3** (Months 7+): Full ALM

* All decisions logged  
* Full hardware enforcement  
* Degraded mode protocols active

---

## **Legal & Compliance**

**Q18: How does TML achieve GDPR compliance?**

* **Cryptographic erasure**: Key destruction renders data inaccessible  
* **Attested shredding**: Physical overwrite with signed attestation  
* **Regional modes**: EU (no blockchain), US/Asia (full anchoring)  
* **Zero-knowledge proofs**: Optional for cross-border compliance

**Q19: Are ALM logs legally admissible?**

Yes, satisfying Federal Rules of Evidence:

* Authentication through cryptographic signatures (FRE 901\)  
* Self-authenticating with validator certificates (FRE 902\)  
* Immutable chain of custody  
* Expert witness panel maintained  
* NIST standards engagement ongoing

**Q20: What's the enforcement mechanism?**

* Missing logs \= automatic negligence  
* Forged logs \= criminal fraud  
* Tampered logs \= obstruction of justice  
* Pattern violations \= RICO charges

Example: Doelger v. JPMorgan \- family lost $50M+ because bank's logs were "unavailable"

---

## **Protection Programs**

**Q21: What is the Memorial Fund?**

Established in Lev Goukassian's memory to:

* Support victims of AI harm (30-40% of penalties)  
* Fund whistleblower rewards (15% of penalties)  
* Maintain validator infrastructure  
* Support framework development  
* Provide legal defense resources

**Q22: How does whistleblower protection work?**

* 15% of recovered penalties paid directly to whistleblowers  
* Anonymous reporting through secure channels  
* Multiparty validator oversight prevents retaliation  
* Criminal prosecution for retaliation attempts  
* Legal support from Memorial Fund

**Q23: How are victims supported?**

* 30% minimum of penalties to victims  
* 40% if victims include vulnerable populations  
* Right to demand logs (missing \= automatic liability)  
* Immediate emergency support for critical cases  
* Lifetime support for permanent AI-caused disabilities

---

## **Sacred Zero & Accountability**

**Q24: What is Sacred Zero?**

A deliberate act of reflection: when an AI confronts moral ambiguity, it pauses, logs, and escalates. Not a gimmick — a conscience checkpoint.

Sacred Zero marks moments requiring special moral consideration. The name carries weight intentionally — when investigators see Sacred Zero in logs, they know to pay attention.

**Q25: How does the Sacred Zero circuit breaker work?**

1. **Pause**: Action halted upon Sacred Zero detection  
2. **Request**: Authenticated confirmation sent to designated authority  
3. **Window**: 500ms for human/policy response  
4. **Resolution**: Explicit confirm executes; timeout aborts  
5. **Log**: Complete decision chain recorded with policy hash

**Q26: How is alert fatigue prevented?**

* Dynamic rate-limiting: First 5 events/hour require review  
* Subsequent similar events auto-blocked with cool-down  
* Immutable policy attestation prevents blame-shifting  
* Mandatory third-party audits tied to insurance premiums  
* Accountability Council governance of trigger policies

---

## **Resilience & Contingencies**

**Q27: What if all TEEs are compromised?**

* Immediate protocol-level ejection of affected types  
* Zero-TEE emergency mode activation  
* 80% BFT consensus required for operations  
* Higher cost/latency but maintains continuity

**Q28: What if validators collude?**

* Stake-weighted selection makes it economically infeasible  
* Random sharding prevents prediction  
* Public audit logs ensure transparency  
* Automated slashing for provable misbehavior  
* Quadratic voting prevents capture

**Q29: What if the legal defense fund is exhausted?**

* Reinsurance policies cap single-case exposure  
* Multiple funding sources ensure replenishment  
* Emergency assessment mechanisms  
* Foundation reserve requirements

---

## **Technical Specifications**

**Q30: Sample ALM v5.0 batch structure:**

{  
  "framework": "TML-ALM-v5.0",  
  "creator\_orcid": "0009-0006-5966-1243",  
  "batch\_id": "batch\_8a4f2c3b5e1d",  
  "timestamp\_range": {  
    "start": "2025-01-07T14:23:45.123456Z",  
    "end": "2025-01-07T14:23:45.223456Z"  
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
  "validator\_confirms": \[  
    {"id": "val1", "type": "full", "sig": "0xf2e4..."},  
    {"id": "val2", "type": "lightweight", "sig": "0x8a9b..."}  
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

TML v5.0 with ALM is not about perfection. It is about **raising the bar** for AI accountability:

* **Immutable logs** that cannot be erased  
* **Independent validation** that cannot be captured  
* **Hybrid Shield protection** that preserves evidence  
* **Sacred Zero** as the conscience of machines  
* **Whistleblower and victim safeguards** that ensure justice

This is **memory that power cannot erase, evidence that courts cannot dismiss, and conscience that machines cannot ignore.**

The Lantern shines beyond names. The framework outlives its creator. The promise endures.

**Sacred Zero is exactly what's needed where lives and billions are on the line.**

---

**Document Version**: 5.0 Resilience Edition  
 **Last Updated**: September 2025  
 **Creator**: Lev Goukassian (ORCID: 0009-0006-5966-1243)  
---

*"Routine logs are cheap; missing logs are expensive. Sacred Zero is exactly what's needed where lives and billions are on the line."*

