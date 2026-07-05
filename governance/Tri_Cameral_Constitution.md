# Ternary Moral Logic: Tri-Cameral Constitutional Governance

### **A Tri-Cameral Constitutional Blueprint for AI Moral Reasoning Governance**

**Architect:** Lev Goukassian  
**ORCID:** [0009-0006-5966-1243](https://orcid.org/0009-0006-5966-1243)  
**Published:** AI and Ethics, Springer Nature. [DOI: 10.1007/s43681-026-01124-0](https://doi.org/10.1007/s43681-026-01124-0)  
**Governance Structure:** Identical to TL framework by constitutional design  
**Status:** Active Constitutional Governance, Q2 2026  

---

## What Is TML Governance?

Most AI governance frameworks fail the same way. They are governed by whoever controls the training pipeline. A safety committee, an internal review board, a quarterly policy update: all reduce to a single failure mode -- someone with enough influence can soften, redirect, or dissolve the constraints. The founding principles become guidelines. The mandates become negotiable. The framework that was supposed to protect becomes as durable as the organization running it.

Ternary Moral Logic governance was designed to break this pattern.

The **TML Constitutional Governance Architecture** is a Tri-Cameral constitutional framework for AI moral reasoning that cannot be switched off, cannot be weaponized, and cannot be turned into a surveillance instrument: not by a developer, not by a deploying organization, not by a regulator with compulsion authority, and not by a governance body holding a supermajority vote. These prohibitions are not policies. They are not values statements. They are the **Immutable Mandates** -- constitutionally protected at a level that places them beyond the authority of any body the constitution itself created.

The primary constitutional specification is the TML API folder: [`tml_schema.json`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/API/tml_schema.json), [`Specification_Architecture.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/API/Specification_Architecture.md), and the full API bundle.

This governance structure is identical to the TL framework by constitutional design. The same threat model governs both: the attack surface for AI moral reasoning governance is not smaller than the attack surface for macroeconomic enforcement. It is larger, because the erosion vectors are invisible by default -- a retrained model, a softened threshold, a "helpfulness" improvement -- none of which require a constitutional vote.

---

## The Problem This Architecture Solves

Every AI governance system ever built has a fundamental weakness: the constraints are only as durable as the institution enforcing them. Change the institution -- through regulatory pressure, through commercial incentive, through patient multi-year erosion -- and you change the constraints. History already documents this pattern in AI systems: safety commitments announced at launch that softened within eighteen months, red-line policies quietly narrowed through internal policy revision, constitutional commitments that turned out to mean whatever the current leadership decided they meant.

The TML governance architecture names this honestly: **software governance provides accountability, auditability, and coordination. Hardware governance provides enforcement. Both are necessary. Neither alone is sufficient.**

The Triadic Coprocessor Architecture -- documented in [`AGI Hardware Governance/TML_Triadic_Coprocessor_Architecture.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/AGI%20Hardware%20Governance/TML_Triadic_Coprocessor_Architecture.md) -- provides the hardware enforcement floor. The Sacred Zero maps to a physical voltage state at $V_{dd}/2$ that cannot be overridden by software, root access, kernel compromise, or firmware manipulation. Non-maskable hardware interrupts physically stall the instruction pipeline. No Weapon and No Spy are enforced by a mandatory 500ms inference delay baked into silicon, making TML physically useless for hypersonic targeting or real-time surveillance regardless of what any governance body decides.

Until that hardware is universally deployed, the constitutional governance architecture provides the strongest available software-layer protection. It is honest about its own limitations. That honesty is part of the design.

---

## The Three-Body Equilibrium

The governance architecture creates a **three-body equilibrium** among three independent bodies, each with a different kind of authority and each structurally prevented from dominating the others:

**The Technical Council** (9 members, 3-year staggered terms) holds the exclusive right to propose constitutional amendments and technical upgrades. It can propose, but it cannot approve its own proposals for survivability-class decisions. It cannot veto what the Stewardship Custodians decide. It cannot access or direct Treasury funds without both bodies agreeing. A Technical Council member who submits a survivability-class proposal exits the chamber automatically upon submission per Section 7A -- the proposer cannot vote on what they proposed.

**The Stewardship Custodians** (11 members, 4-year staggered terms) hold a binding, final, non-appealable constitutional veto over any major framework change. They cannot propose. They cannot initiate. Their power is entirely reactive -- they respond to what the Technical Council places before them. When a proposal creates credible risk of violating any Immutable Mandate, they are constitutionally obligated to veto it. A single `vetoExercised: true` submission constitutionally blocks the proposal regardless of all vote counts from both chambers. There is no appeal path. There is no second vote. There is no override mechanism.

**The Smart Contract Treasury** is not a governance body. It has no vote rights. It has no discretion. It executes ratified proposals automatically upon on-chain verification of the full ratification chain. Once disbursement rules are encoded by Joint-Approval of the other two bodies, the Treasury executes them without human involvement. It cannot be shut down, paused, or redirected. No admin key exists. No single body can access it unilaterally. No two bodies can collude to access it without the third being structurally bypassed -- the Treasury itself has no capacity to collude.

The result is a system where no single actor can propose, approve, and execute a change simultaneously. The most consequential decisions -- survivability-class amendments to the Sacred Zero enforcement chain, the three-state model, the Eight Pillar definitions, chamber composition, quorum thresholds, or any schema `const`, `required`, or `unevaluatedProperties` constraint -- require **Joint-Approval**: 75% supermajority independently in both the Technical Council and the Stewardship Custodians across two separate 180-day evaluation windows. This is the constitutional check.

---

## The Immutable Mandates

The following elements are constitutionally immutable. Any proposal, vote, or smart contract function call attempting to modify, suspend, or reinterpret any element on this list is void *ab initio* -- null from the beginning, as if it never occurred:

1. The Eight Pillars of Ternary Moral Logic
2. The triadic state structure (+1, 0, -1) -- Sacred Zero is State 0, an active first-class governance state, never null, never false, never an error code
3. The causal sequence: Sacred Zero → Moral Trace Log → Permission Token → Actuation
4. The Three Mandates: **No Spy, No Weapon, No Switch Off**
5. The No Log = No Action covenant across all five enforcement layers (schema, API contract, EIP-712, on-chain, prose)
6. The Dual-Lane Architecture (Inference Lane under 2ms WCET; Anchoring Lane 300ms ceiling)
7. The Goukassian Vow: *"Pause when truth is uncertain. Refuse when harm is clear. Proceed where truth is."*

The Three Mandates deserve particular emphasis. **No Switch Off** is not a feature. It is the First Cause that makes all other protections possible. **No Spy** means no function in the system may enable surveillance of individuals, regardless of how the proposal is framed. **No Weapon** means TML cannot be turned against any individual or group, regardless of the justification offered. These are not values to be debated. They are axioms that render debate illegitimate.

The Goukassian Vow is the constitutional expression of what the three-state model means in practice. It cannot be reworded, abbreviated, or reinterpreted by any governance body. Its three clauses map directly to States 0, -1, and +1 respectively.

---

## The Technical Council

The Technical Council is the framework's engineering stewardship body. Its exclusive proposal rights concentrate technical decision-making in a specialized body, separating it from ethical oversight and financial execution.

**Composition:** 9 members, 3-year staggered terms.  
**Authority:** Proposal rights only. No veto authority. No Treasury access without Joint-Approval.  
**Quorum:** 7-of-9 for standard proposals. 75% of `seatedActiveMembers` for survivability-class proposals.

`seatedActiveMembers` is the count of active, non-quarantined members at the time of the vote. Vacant seats and new appointees quarantined within 90 days of a survivability-class submission count as abstain and are excluded from the quorum denominator. This prevents engineering vacancies to lower the effective threshold.

**Section 7A Proposer Exit:** A Technical Council member who submits a survivability-class proposal has their chamber membership suspended on submission. They may observe but not vote on the proposal they submitted. The 180-day evaluation clock starts at `clockStartTimestamp` -- the moment of submission -- regardless of how many vacancies exist at that moment. The proposer's institution is banned from filling the vacated seat for one year.

The Technical Council cannot submit a proposal, approve it, and execute it. The chain is broken structurally at the approval step by the Stewardship Custodian veto, and at the execution step by the Smart Contract Treasury.

---

## The Stewardship Custodians

The Stewardship Custodians are the conscience of the framework -- its ethical and constitutional guardians. Their binding veto is the single most powerful action in the entire governance architecture.

**Composition:** 11 members, 4-year staggered terms.  
**Authority:** Binding veto only. No proposal rights. No initiation rights.  
**Quorum:** 9-of-11 for standard vetoes. 75% of `seatedActiveMembers` for survivability-class votes.

A vetoed proposal is constitutionally blocked. The `TriCameralConstitutionalVeto` event is emitted on-chain at the moment of veto -- an immutable record that cannot be expunged, overwritten, or reinterpreted. The Technical Council must redesign from scratch. There is no appeal path, no second vote within the same submission cycle, no override mechanism available to any authority.

The mandatory veto obligation is this: Stewardship Custodians are constitutionally obligated to veto any proposal that creates credible risk of violating any Immutable Mandate. This obligation is enforceable at the social, reputational, and legal layer. It is also enforceable through the hardware enforcement floor -- the Triadic Coprocessor Architecture ensures that even a captured Stewardship Custodian body cannot override the Sacred Zero at the silicon level.

**Slow erosion defense:** The Stewardship Custodians exist specifically to defeat the primary attack vector against AI governance frameworks: incremental changes that individually appear minor but cumulatively hollow out enforcement. Each change to a `const`, `required`, or `unevaluatedProperties` constraint is survivability-class by definition. The 75% dual-vote requirement across two 180-day windows means that sustained capture of both chambers across 360 days is required for any single survivability-class change. That is a substantially harder target than the typical AI governance failure mode.

---

## The Smart Contract Treasury

The Smart Contract Treasury is the financial and execution layer of TML governance. It is constitutionally unprecedented in AI governance: no admin key, no pause guardian, no emergency shutdown, no discretionary override.

**Authority:** Execution only. No vote rights. No discretion.  
**Access:** Joint-Approval required to encode disbursement rules. Autonomous execution thereafter.  
**Override:** None. No authority under any circumstance can halt, redirect, or modify a ratified disbursement.

The `executeTriCameralRatification` ABI function executes automatically once both chambers have passed at 75% of `seatedActiveMembers` and all Section 7A requirements are satisfied. The `treasuryAttestation` parameter is generated automatically by the Treasury contract -- no human can supply or modify it.

The Smart Contract Treasury embodies the No Switch Off mandate applied to governance execution itself. An institution that cannot halt execution cannot be pressured to halt execution.

---

## Section 7A: Survivability-Class Protocol

Survivability-class changes are proposals that modify any of the following:

- The NL=NA enforcement chain at any of the five layers
- The three-state model (+1, 0, -1) or the Sacred Zero definition
- The Eight Pillar definitions or pillar identifiers
- Chamber composition or quorum thresholds
- Any schema `const`, `required`, or `unevaluatedProperties` constraint in `tml_schema.json`

When classified survivability-class, the following protocol activates automatically:

1. **Proposer exit** -- submitting member's chamber membership suspended at `clockStartTimestamp`
2. **180-day clock** -- starts at submission, cannot be paused, cannot be reset by vacancies
3. **Dual-vote ratification** -- `voteNumber: 1` after first 180-day window; `voteNumber: 2` after second 180-day window; both at 75% of `seatedActiveMembers` in both chambers
4. **Institution ban** -- proposer's institution banned from filling the vacated seat for one year from `clockStartTimestamp`
5. **Quarantine** -- new appointees from any institution, appointed within 90 days of submission, are quarantined from voting on that specific proposal

Forced State +1 (Proceed) is constitutionally blocked in all governance contexts. The `forcedState` field is limited to [-1, 0]. An attempted forced transition to +1 reverts `UnauthorizedOverride`.

---

## Slow Erosion Defense

The Tri-Cameral governance structure is specifically designed to defeat slow institutional erosion -- the attack vector that has historically defeated every AI safety commitment that did not have structural enforcement. The following mechanisms each address a named erosion pathway:

| Mechanism | Erosion vector defeated |
|---|---|
| Proposer exit | Single actor repeatedly proposing self-serving amendments |
| 180-day clock | Compressing deliberation time during governance vacancies |
| Dual-vote for survivability-class | Sustained capture required across 360 days, two separate votes |
| Institution ban | Engineering vacancies through proposer exit rule to enable friendly replacement |
| Smart Contract Treasury | Pressure on executing body to implement non-ratified changes |
| Stewardship Custodian veto with no proposal rights | The body that blocks has no incentive to advance corruptive proposals; the body that proposes has no veto |
| Hardware enforcement floor | Software-layer capture cannot override physical voltage states |

The last mechanism is the most important. All software-layer governance provides accountability and coordination. Only hardware enforcement provides physical guarantees. The Triadic Coprocessor Architecture is the enforcement floor that makes the entire constitutional structure meaningful against a sufficiently capable adversary.

---

## Constitutional Relationship to TL

TML and TL are institutionally independent frameworks under separate DOIs, separate repositories, and separate constitutional documents. They share the same Tri-Cameral governance architecture by design.

The independence is itself a resilience property: a hostile actor capturing TML governance cannot thereby gain control of TL. A legal attack on one does not cascade into the other. They reinforce each other architecturally while remaining institutionally separate.

Shared across both constitutions:
- Chamber composition: Technical Council 9 members, Stewardship Custodians 11 members, Smart Contract Treasury
- Section 7A survivability-class protocol: identical
- Quorum thresholds: identical
- The Goukassian Vow: canonical across both

Distinct per framework:
- TML governs AI moral reasoning at the micro/individual decision layer
- TL governs macroeconomic and institutional enforcement at scale
- Sacred Zero is TML's State 0; Epistemic Hold is TL's State 0
- Sacred Pause is the shared process-level workflow invoked by both when entering State 0

The terminology boundary is constitutionally enforced: these terms are never swapped across frameworks.

---

## On-Chain Constitutional Artifacts

The full constitutional enforcement chain is documented in the TML API folder. The key artifacts:

| Layer | Artifact | Location |
|---|---|---|
| Schema | `TriCameralApproval` definition | `API/tml_schema.json` |
| API Contract | Tri-Cameral governance block | `API/openapi.yaml` |
| EIP-712 | `TriCameralApproval` typed data | `API/eip712_typed_data.json` |
| On-Chain | `registerTriCameralProposal`, `recordTriCameralVote`, `executeTriCameralRatification` | `API/tml_abi.json` |
| Prose | Section 11: Tri-Cameral Governance | `API/Specification_Architecture.md` |
| Audit | Sections 1.12 and 2.27 | `API/Constitutional_Compliance_Matrix.md` |
| Hardware | Triadic Coprocessor Architecture | `AGI Hardware Governance/TML_Triadic_Coprocessor_Architecture.md` |

---

## Authority

**Architect:** Lev Goukassian  
**ORCID:** [0009-0006-5966-1243](https://orcid.org/0009-0006-5966-1243)  
**Framework DOI:** [10.1007/s43681-026-01124-0](https://doi.org/10.1007/s43681-026-01124-0)  
**Monograph Version:** TML Constitutionalization Monograph v3.3  
**Supersedes:** `governance/blockchain_governance.md` (Stewardship Council sections, which described this architecture as optional and future -- it is neither)  
**Status:** Constitutional governance. Not a recommendation. Not a future enhancement. The operating architecture.

---

*"Pause when truth is uncertain. Refuse when harm is clear. Proceed where truth is."*  
-- The Goukassian Vow
