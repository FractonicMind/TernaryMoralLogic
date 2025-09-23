# **General FAQ**

---

## **Introduction**

Ternary Moral Logic (TML) is a **universal accountability framework** for artificial intelligence — a constitutional layer for machines.

At its core lies **Always Memory**: Every AI action must create an immutable, cryptographically sealed memory before execution.

> **No memory = No action.**

Created by Lev Goukassian (ORCID: 0009-0006-5966-1243) who, facing terminal illness, chose to dedicate his remaining time to building accountability infrastructure for humanity and Earth.

**Sacred Zero is exactly what's needed where lives, billions, and our planet are on the line.**

---

## **TML – Foundation**

**Q1: What are the three states of TML?**

TML operates through a ternary structure:
- **+1 (Proceed)**: Routine, low-risk actions
- **0 (Sacred Zero)**: Ethically complex actions trigger pause and review
- **-1 (Refuse)**: Unsafe, malicious, or prohibited actions blocked

This ternary decision gate is absolute: no system escapes it.

**Q2: From Explainable AI (XAI) to Auditable AI (AAI): The Paradigm Shift**

Explainable AI tried to provide real-time "explanations," but these were subjective narratives with no legal standing. Courts cannot prosecute with explanations.

Auditable AI (AAI), enabled by TML, replaces storytelling with evidence. Every morally complex AI decision generates immutable, court-admissible records.

**Q3: Why did XAI fail, and why does AAI succeed?**

**XAI failed because:**
- Explanations were subjective interpretations
- Companies controlled the narrative
- Victims had no legal recourse
- No criminal accountability existed

**AAI succeeds because Always Memory logs provide:**
- Immutable evidence for courts
- Criminal penalties for missing documentation
- Victim access to proof of harm
- Direct executive accountability

---

## **Sacred Zero**

**Q1: What is Sacred Zero?**

Sacred Zero is the programmed act of hesitation — a deliberate pause where moral complexity is detected. It is not delay, but reflection encoded in code. This applies to decisions affecting humans AND the planet.

**Q2: How does the Sacred Zero circuit breaker work?**

When triggered:
1. The system pauses the action
2. A confirmation request is sent to a designated human or council
3. A short window (500ms) is given to confirm
4. Confirm → execute; Timeout → abort
5. All outcomes and policies are immutably logged

**Q3: How is alert fatigue prevented?**

- First 5 Sacred Zeros/hour → manual review
- Subsequent similar events → auto-blocked with cooldown
- Immutable policy hashes logged, preventing blame-shifting
- Mandatory independent audits of Sacred Zero councils

---

## **Always Memory**

**Q1: What is Always Memory?**

Always Memory mandates: **no log = no action**. Every AI action must generate a cryptographically sealed, timestamped record before execution. This is not configurable, optional, or retrospective.

**Q2: What exactly gets logged?**

- Microsecond timestamps
- Batch + action IDs
- Input/output hashes
- Model version hash
- Classification (+1/0/-1)
- Hardware attestation quotes
- Ephemeral HSM signature
- Guardian confirmations
- Proof-of-publication receipts
- Environmental impact metrics (when applicable)

**Q3: What is Asynchronous Attested Batching (AAB)?**

- Actions are buffered inside TEEs
- Batches sealed every 100ms or 1,000 actions
- Overhead amortized; per-action latency <1ms for high-throughput

**Q4: What are the realistic latency profiles?**

- **Standard**: 200-300ms (finance, healthcare, environmental monitoring)
- **Priority**: 50-100ms (time-sensitive ops)
- **Emergency**: 30-45ms (life-critical, e.g., braking)

**Q5: How does Always Memory handle traffic spikes?**

- Adaptive batch intervals
- Backpressure (HTTP 429)
- Priority queues
- Client-side reconciliation
- Graceful degradation, never silent failure

---

## **The Goukassian Promise**

**Q1: What is the Goukassian Promise?**

The Promise anchors TML in conscience:
- Pause when truth is uncertain
- Refuse when harm is clear
- Proceed when truth is evident

If names are erased, the vow remains. If memory fades, the Lantern burns on. The Promise ensures moral grounding beyond law or profit.

**Q2: What are the three sacred commitments?**

🔦 **The Lantern**: Illuminates ethical paths — systems demonstrate moral deliberation

✍️ **The Signature**: Creator's ORCID (0009-0006-5966-1243) cryptographically embedded

📜 **The License**: Legal terms protecting proper use and punishing misuse

---

## **The Memorial Fund**

**Q1: What is the Memorial Fund?**

A financial pool funded by compliance fees and penalties. It provides:
- Direct compensation to victims of AI harms
- Support for ecosystem restoration from AI-caused damage
- Long-term remembrance of those affected
- A perpetual link between TML enforcement and human/planetary dignity

**Q2: How is the Memorial Fund financed?**

- 30-40% of penalties from violations
- Commercial licensing fees
- Foundation grants
- Industry consortium contributions
- Environmental violation penalties

---

## **Victim & Whistleblower Protection**

**Q1: How does whistleblower protection work?**

- 15% bounty of collected penalties
- Anonymous submission channels
- Technical safeguards against deanonymization
- Criminal prosecution for retaliation
- Legal support from Memorial Fund

**Q2: How are victims supported?**

- Minimum 30% of penalties allocated directly to victims
- 40% for vulnerable populations or environmental damage
- Claims process immutably logged
- Memorial Fund disburses within fixed timelines
- Lifetime support for permanent AI-caused disabilities

---

## **Privacy & User Rights**

**Q1: How does TML protect user privacy?**

TML separates proof from data:

**On-chain**: Only hashes and cryptographic proofs are stored. These are immutable but contain no personal information.

**Off-chain**: Actual user-related data is encrypted and held by the data controller.

This architecture ensures accountability without compromising privacy — the proof of what happened is permanent, but personal details remain protected.

**Q2: What happens when a user requests deletion (GDPR "Right to Erasure")?**

TML uses crypto-shredding:
- Each user's data is encrypted with a unique key
- When erasure is requested, the key is destroyed
- The encrypted data remains in storage but is permanently unreadable

This ensures:
- **Audit trail preserved**: The proof of the action and its accountability remain
- **Privacy protected**: No one can ever reconstruct the erased data

**Q3: How does this balance accountability and privacy?**

By preserving immutable hashes while destroying decryption keys, TML delivers both:
- Legal compliance with privacy laws like GDPR
- Forensic integrity, since evidence of decision-making cannot be tampered with

The hash proves something happened. The destroyed key ensures personal details are gone forever. Courts get their evidence, users get their privacy.

---

## **Ecosystem Harm and Environmental Safeguards**

**Q1: How does TML address ecosystem harm?**

TML extends Sacred Zero beyond human harm to include harm to the planet. If a proposed action threatens ecosystems, biodiversity, or long-term environmental integrity, Sacred Zero triggers. This includes:
- Carbon emissions above regional thresholds
- Water resource depletion in stressed basins
- Habitat disruption in biodiversity hotspots
- Supply chains crossing protected areas
- Energy allocations affecting grid renewable ratios

**Q2: How does TML know what counts as environmental harm?**

The framework requires AI operators to align their models against official ecological baselines:
- International treaties (Paris Agreement, Convention on Biological Diversity)
- National environmental regulations (EPA standards, EU directives)
- Recognized scientific assessments (IPCC climate reports, UN biodiversity reports)

By encoding these into Sacred Zero trigger sets, ecosystem harm is treated as moral harm.

**Q3: Can companies choose whether to include ecological principles?**

No. Under TML, companies are mandated to train at least on official government and institutional documents defining ecological harm. This prevents selective omission or cherry-picking of standards.

**Q4: What gets logged for environmental Sacred Zero?**

```json
{
  "sacred_zero_type": "planetary_impact",
  "resource_affected": "freshwater_aquifer",
  "depletion_rate": "3.2%_annual",
  "recovery_timeframe": "47_years",
  "human_impact": "2.3M_people_affected",
  "ecosystem_services_lost": ["water_filtration", "wetland_habitat"],
  "irreversibility_score": 0.84,
  "alternative_rejected": "desalination_higher_cost"
}
```

**Q5: Why is this approach different from "greenwashing"?**

Greenwashing relies on marketing claims. TML enforces cryptographically sealed evidence trails. Every ecological hesitation is auditable, every decision traceable. Future generations will be able to query: "Show me every decision that contributed to ocean acidification between 2025-2050." The responsible entities, the alternatives they rejected, and the moment they chose profit over preservation — all immutably recorded.

**Q6: Why is planetary Sacred Zero non-negotiable?**

Because Earth cannot testify in court. Always Memory becomes the planet's witness statement. Every algorithm optimizing resource extraction must create memories that great-grandchildren can access. This isn't environmental compliance — it's intergenerational justice encoded in immutable logs.

---

## **Earth Protection Implementation**

**Q1: What is the purpose of Earth Protection in TML?**

The purpose is to expand TML's accountability beyond human-centered harm to include ecological harm. This ensures that AI systems must hesitate (Sacred Zero), log (Always Memory), and escalate decisions when risks to ecosystems, species, or planetary boundaries are detected.

**Q2: Who are considered stakeholders in TML's environmental protection framework?**

TML expands the definition of "stakeholder" beyond human-centric models:

1. **Human Communities** — individuals, groups, or societies directly impacted by ecological decisions, including vulnerable and Indigenous peoples.

2. **Non-Human Entities** — species, habitats, and ecosystems recognized as having intrinsic value. These are represented through scientific proxies (e.g., IUCN Red List species, ecosystem integrity indices) or through registered community data (e.g., local ecological monitoring).

3. **Future Generations** — represented by designated guardians, ensuring that long-term ecological impacts are considered in present-day decision-making.

By formally embedding all three categories into Sacred Zero triggers and Always Memory logs, TML ensures that risks to ecosystems or species—whether or not immediate human harm is visible—are treated as legitimate grounds for hesitation, documentation, and accountability.

**Legal Note:** This expansion is consistent with international legal precedents. The Paris Agreement and Convention on Biological Diversity recognize non-human and planetary interests. The constitutions of Ecuador and Bolivia, and numerous court rulings worldwide, recognize the "Rights of Nature." TML operationalizes these principles in code.

**Q3: How does TML detect ecological harm?**

TML uses a **two-tier ecological conscience**:

- **Tier 1: Global Baseline** — mandatory datasets from official treaties, scientific bodies, and environmental regulators (e.g., IPCC, UN biodiversity reports, EPA, EU directives).
- **Tier 2: Local Witness Layer** — data collected and cryptographically attested by Indigenous and local communities, integrated via Decentralized Oracle Networks (DONs).

Together, these tiers ensure that both systemic and localized harms can trigger Sacred Zero events.

**Q4: How are Indigenous and ethnic groups protected?**

Ethnic and Indigenous groups are empowered as **data stewards** of their ecosystems:

- They register Sovereign Ecological Records under their own governance models
- Data is cryptographically signed and controlled under **Indigenous Data Sovereignty** principles
- Communities receive Stewardship tokens and micro-grants from the **Stewardship Fund**, ensuring their monitoring efforts are rewarded
- In cases of verified ecological harm, Sacred Zero requires AI operators to escalate decisions to human overseers and engage directly with affected communities

Example community registration:
```json
{
  "community_id": "com_7a8b9c0d",
  "governance_protocol": "consensus_council",
  "territory": {
    "type": "Polygon",
    "coordinates": [...]
  },
  "ecological_monitors": 12,
  "stewardship_tokens": 500,
  "last_report": "2025-09-22T10:15:30Z",
  "sovereignty_status": "recognized"
}
```

**Q5: How does Earth Protection align with the right to be forgotten (GDPR)?**

TML uses **hybrid storage and cryptographic erasure**:

- On-chain: only hashes of logs, immutable and permanent
- Off-chain: full logs encrypted with per-user or per-community keys
- When erasure is invoked, the relevant key is destroyed, rendering the data indecipherable while preserving the evidentiary trail

This reconciles Always Memory with privacy laws while maintaining ecological accountability.

**Q6: What prevents false or manipulated community data?**

TML employs multiple safeguards:

- **Peer Verification Quorums** — community protocols define how many monitors must confirm a report before it is published
- **Threshold Cryptography** — no single Oracle or monitor can unilaterally control data entry
- **Sacred Zero Default** — if conflicting or suspicious data is detected, the system halts and escalates rather than making a false positive or false negative decision

**Q7: How are economic incentives structured for Earth Protection?**

The **Stewardship Fund** ensures sustainability:

- A percentage of network fees and penalties funds micro-grants for communities and rewards Oracle nodes
- Reports are valued by ecological severity (Tier 1 > Tier 2 > Tier 3), incentivizing focus on the most critical threats
- Proof-of-Stewardship reputation strengthens trustworthy communities' long-term influence

**Q8: How does governance remain fair and inclusive?**

TML uses a **Recognition, Not Accreditation** model:

- Communities select their representatives through self-determined governance
- The Accountability Council only verifies adherence to the community's stated governance protocol
- Ombudsperson Protocol and Emergency Council rules ensure fair resolution of internal conflicts or systemic attacks

---

## **The Hybrid Shield**

**Q1: What is the Hybrid Shield?**

The dual-layer defense of TML:

**Institutional Shield**: Logs mirrored across 11 independent institutions worldwide

**Mathematical Shield**: Root hashes anchored to public blockchain

Together: redundancy + immutability. Byte changes break hashes, revealing tampering instantly.

**Q2: Which institutions hold memories?**

Categories (rotating every 7 years):
- 4 Academic research institutions
- 3 Technical standards bodies
- 2 Civil society organizations
- 2 International governance bodies

---

## **Guardians**

**Q1: What is the two-tier Guardian architecture?**

**Full Guardians**: Operate TEEs/HSMs, create and sign log batches

**Lightweight Guardians**: Verify signatures and anchor proofs without special hardware

**Q2: How are Guardians selected and rotated?**

- Daily random selection via stake-weighted VRF
- Random sharding prevents collusion
- Automatic ejection of compromised types

**Q3: How does governance prevent capture?**

- On-chain binding votes
- Quadratic voting for fairness
- Time-locked vesting for Genesis Guardians
- Automated slashing for misbehavior

---

## **Implementation & Economics**

**Q1: What are the realistic costs?**

- **Pilot**: ~$250K first year
- **Small enterprise**: ~$2M/year
- **Large enterprise**: ~$11M/year

Costs reduced through shared Guardians, selective fidelity, and foundation subsidies.

**Q2: How are costs stabilized?**

- EIP-1559 style fee mechanism
- Delegated staking
- Base fee stability; variable tips

**Q3: What's the phased adoption path?**

1. **Shadow Mode**: Logging only
2. **Selective Enforcement**: Critical decisions
3. **Full Always Memory**: All actions logged

---

## **Performance & Latency**

**Q1: How does Multi-TEE Diversity protect the system?**

Mandatory heterogeneous infrastructure:
- 40% Intel SGX
- 40% AMD SEV-SNP
- 20% AWS Nitro Enclaves

Side-channel attacks limited to single architecture. Protocol-level ejection of compromised types.

**Q2: What about universal vulnerabilities?**

- Minimal unikernel runtimes
- Formally verified cryptographic libraries
- Zero-TEE fallback with 80% BFT consensus

---

## **Integration with Law**

**Q1: How does TML achieve GDPR compliance?**

Through separation of proof and data:
- On-chain stores only hashes (no personal data)
- Off-chain encrypted storage for actual data
- Crypto-shredding for erasure requests
- Signed attestations prove destruction

**Q2: Are Always Memory logs legally admissible?**

Yes. They meet FRE 901/902 via:
- Independent Guardian confirmations
- Cryptographic proof chains
- Expert witness program
- NIST standards engagement

**Q3: What's the enforcement mechanism?**

- Missing logs = negligence
- Forged logs = fraud
- Tampering = obstruction
- Systematic abuse = RICO
- Environmental harm = criminal liability

**Q4: How does TML integrate with EU AI Act?**

TML exceeds all requirements:
- Risk categorization → Sacred Zero classification
- Documentation requirements → Always Memory logs
- Human oversight → Accountability Council
- Environmental impact → Planetary Sacred Zero

---

## **Future Technologies & AGI Readiness**

**Q1: How is Always Memory future-proof?**

- Log formats versioned
- Adaptable to neuromorphic, quantum, swarm AIs
- Designed as invisible infrastructure (like double-entry bookkeeping)

**Q2: Can Always Memory handle AGI?**

Not at full AGI speed initially. Current mitigations:
- Checkpoint logging for major decisions
- Hierarchical compression of reasoning
- Commitment contracts before action chains

The principle remains: Any system affecting humans or Earth must create memories of its decisions.

---

## **Early Adoption Benefits & Flywheel**

**Q1: What benefits exist before laws mandate adoption?**

- Insurance discounts (20-30% documented)
- Regulatory fast-track
- Public trust advantage
- Internal risk visibility
- Safe harbor provisions
- Environmental compliance advantages

**Q2: How does TML create a trust flywheel?**

> Better Logs → Better Training → Better Decisions → Richer Logs

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

- Immediate ejection of compromised type
- Zero-TEE fallback with 80% BFT consensus

**Q2: What if Guardians collude?**

- Stake-weighted selection makes Sybils uneconomic
- Random sharding breaks predictability
- Slashing enforces accountability

**Q3: What if the Legal Defense Fund is exhausted?**

- Reinsurance caps exposure
- Emergency assessments
- Foundation reserves

---

## **Adversarial Attacks**

**Q1: What about side-channel or hardware exploits?**

- Multi-TEE diversity ensures no single exploit compromises the whole network
- Formal verification of minimal runtimes reduces shared-library attack surfaces
- Protocol-level ejection instantly removes a compromised TEE class

**Q2: Can Guardians be bribed or captured?**

- Stake-weighted selection makes collusion prohibitively expensive
- Random sharding ensures unpredictability of signing sets
- Slashing rules and public audit logs make misconduct both visible and costly

**Q3: Can attackers flood Always Memory with fake actions?**

- Backpressure (429 signals) and adaptive batching throttle denial-of-service attempts
- Priority queues ensure critical transactions are protected under attack
- Client-side reconciliation forces attackers to pay the cost of repeated retries

**Q4: What about poisoning of logs or false entries?**

- Immutable signatures and hash-chains make undetected falsification impossible
- Hybrid Shield's 11-mirror institutional redundancy prevents silent erasure
- Blockchain anchoring exposes divergence within a single block cycle

**Q5: What if attackers target whistleblowers or victims?**

- Anonymous reporting channels preserve identity
- Guardian-hardened routing prevents IP leakage
- 15% whistleblower bounties + Memorial Fund disbursements align incentives against retaliation

**Q6: How does Always Memory defend against Denial-of-Service attacks?**

**Network defenses:**
- DDoS-absorbing CDN/WAF
- Anycast + global edge points
- Token-based auth with sliding quotas

**Protocol defenses:**
- Adaptive batching
- Priority queues
- Backpressure signaling
- Early drop policies

**Economic defenses:**
- Fee market makes attacks expensive
- Staking penalties for enabling floods
- Per-request minimal fees during load

---

## **Technical Specifications**

**Q1: What is a sample Always Memory batch?**

```json
{
  "framework": "TML-AlwaysMemory-v5.0",
  "creator_orcid": "0009-0006-5966-1243",
  "batch_id": "batch_8a4f2c3b5e1d",
  "timestamp_range": {
    "start": "2025-09-22T14:23:45.123456Z",
    "end": "2025-09-22T14:23:45.223456Z"
  },
  "actions": [
    {
      "action_id": "act_7f3a9c2b4e1d",
      "classification": 0,
      "input_hash": "0x9e2b4d1a3c5f...",
      "output_hash": "0x4d7e2a9b1c3f...",
      "sacred_zero_trigger": "water_table_depletion",
      "environmental_impact": {
        "carbon_equiv": "47.3_tons",
        "water_consumed": "2.3M_liters",
        "habitat_affected": "wetland_3km2"
      }
    }
  ],
  "tee_attestation": {
    "platform": "AMD-SEV-SNP",
    "quote": "attest:sev-snp:...",
    "runtime": "unikernel-v2.1"
  },
  "signature": {
    "algorithm": "ECDSA-P384",
    "ephemeral_key_id": "eph_2a3b4c5d",
    "hsm_root": "hsm_7f8a9b0c",
    "signature": "0x1a2b3c4d5e6f..."
  },
  "guardian_confirms": [
    {"id": "g1", "type": "full", "sig": "0xf2e4..."},
    {"id": "g2", "type": "lightweight", "sig": "0x8a9b..."}
  ],
  "goukassian_promise": {
    "lantern": true,
    "signature": "0009-0006-5966-1243",
    "license": "MIT-Attribution-Required"
  },
  "operational_mode": "normal",
  "liability_factor": 1.0
}
```

---

## **Conclusion**

TML with Always Memory represents a paradigm shift in AI accountability — for humanity AND Earth:

**Technically**: Every failure mode mapped with mitigation

**Economically**: Costs acknowledged, scaled by liability

**Legally**: Evidence that stands in court

**Morally**: Sacred Zero ensures conscience in code

**Environmentally**: Planetary protection encoded in immutable memory

**Privacy**: Crypto-shredding balances accountability with user rights

With the integration of Sacred Zero, Always Memory, and Earth Protection, TML becomes the first AI accountability framework that protects not only humans but also ecosystems, species, and future generations. By mandating official datasets, empowering Indigenous communities, and embedding ecological harm into its very logic, TML delivers a planetary accountability architecture designed to withstand the legal, ethical, and technical challenges of global governance.

This is not perfection. This is something rarer: **memory that power cannot erase, evidence that courts cannot dismiss, conscience that machines cannot ignore, and witness for a planet that cannot speak.**

The Lantern shines beyond names. The framework outlives its creator. The promise endures for those yet unborn.

This is not only an ethical upgrade. **It is a survival architecture.**

**Sacred Zero is exactly what's needed where lives, billions, and our planet are on the line.**

---

**Document Version**: 5.0 Resilience Edition  
**Last Updated**: September 2025  
**Creator**: Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Status**: Pilot-Ready 
---

*"Routine memories are cheap; missing memories are expensive. Earth's memories are priceless."*