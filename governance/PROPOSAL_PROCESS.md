# Ternary Moral Logic: Proposal Process Protocol

### **How Governance Proposals Are Submitted, Classified, and Ratified**

**Architect:** Lev Goukassian
**ORCID:** [0009-0006-5966-1243](https://orcid.org/0009-0006-5966-1243)
**Parent Document:** [`governance/Tri_Cameral_Constitution.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/governance/Tri_Cameral_Constitution.md)
**Status:** Operational Protocol

---

## Purpose

This document defines the complete lifecycle of a governance proposal: who may submit, how proposals are classified, what the Section 7A survivability-class protocol requires step by step, and how ratification is recorded on-chain. It is the operational companion to the constitutional principles in `Tri_Cameral_Constitution.md`.

---

## Part I: Who May Propose

Only Technical Council members may submit governance proposals. Stewardship Custodians hold binding veto authority only -- they may not initiate proposals.

A Technical Council member submits a proposal in their institutional capacity. The proposing institution bears full responsibility for the proposal text, the survivability-class classification, and the consequences of Section 7A activation where applicable.

---

## Part II: Proposal Classification

Every proposal must be classified at submission as either **Standard** or **Survivability-Class**.

### Standard Proposals

Standard proposals cover operational matters that do not touch the constitutional enforcement chain. Examples include:

- Adding a new compliance mapping to the Constitutional Compliance Matrix
- Updating documentation, examples, or training materials
- Extending the API with non-constitutional new endpoints
- Adjusting monitoring thresholds that are not schema-enforced constants

Standard proposals require simple majority in both chambers with no Stewardship Custodian veto.

### Survivability-Class Proposals

A proposal is survivability-class if it modifies any of the following:

- The NL=NA enforcement chain at any of the five layers (schema, API contract, EIP-712, on-chain, prose)
- The three-state model (+1, 0, -1) or the Sacred Zero definition
- The Eight Pillar definitions or pillar identifiers
- Chamber composition or quorum thresholds
- Any `const`, `required`, or `unevaluatedProperties` constraint in `API/tml_schema.json`
- The Goukassian Vow text
- The Immutable Mandates (No Spy, No Weapon, No Switch Off)
- The Dual-Lane Architecture WCET bounds

**When in doubt, classify as survivability-class.** A misclassification that understates severity is a constitutional violation. A misclassification that overstates severity costs time but causes no harm.

Forced State +1 proposals are constitutionally void. They may not be submitted, classified, or processed. Any submission targeting Forced State +1 is rejected at registration and recorded as an `UnauthorizedOverride` attempt.

---

## Part III: Standard Proposal Workflow

```
1. Proposer drafts proposal text
2. Proposer submits via registerTriCameralProposal (survivabilityClass: false)
3. 14-day public comment period opens
4. Technical Council votes (simple majority of seatedActiveMembers)
5. Stewardship Custodians vote (simple majority; veto available)
   -- If vetoExercised: true -- proposal constitutionally blocked, process ends
   -- If majority reached in both chambers -- proposal passes
6. executeTriCameralRatification called -- Smart Contract Treasury records ratification
7. Proposal implemented
```

Total minimum elapsed time: 14 days (public comment) plus vote scheduling.

---

## Part IV: Section 7A Survivability-Class Workflow

The Section 7A protocol is mandatory for all survivability-class proposals. It cannot be waived, abbreviated, or accelerated by any authority.

### Step 1: Submission, Proposer Exit, and Testimony Rights

The proposing Technical Council member submits via `registerTriCameralProposal` with `survivabilityClass: true`.

At the moment of submission:
- The `clockStartTimestamp` is set -- the 180-day evaluation window begins immediately
- The proposer's chamber membership is suspended -- they may not vote on this proposal for its entire lifecycle
- The proposer's institution is banned from filling any vacated seat for one year from `clockStartTimestamp`
- The `proposerExitConfirmed` field is set to `true` on-chain

**The exit is unconditional and applies to all survivability-class proposals without exception -- including proposals that are critical to the framework's survival.** The separation between proposing and voting is structural, not punitive. It is precisely the proposals with the highest stakes where this separation matters most.

**However, the exit applies to voting only -- not to knowledge.** A suspended Technical Council member retains the right and the obligation to testify. During both 180-day evaluation windows they may:

- Present technical evidence to both chambers
- Answer questions from Stewardship Custodians and Technical Council members
- Submit written analysis, security assessments, and implementation guidance
- Respond to objections and clarify technical details

They may not: advocate for passage, lobby individual members, or participate in the vote count in any form.

This distinction matters most precisely when the proposer's expertise is irreplaceable -- a critical security patch, a hardware vulnerability fix, a zero-day constitutional threat. The framework does not waste that expertise. It insulates the vote from the proposer's institutional interest while preserving access to their knowledge.

The clock cannot be paused, reset, or extended. Vacancies created after submission do not affect the clock.

### Step 2: Quarantine Assessment

Any Technical Council or Stewardship Custodian member newly appointed within 90 days of `clockStartTimestamp` is quarantined from voting on this specific proposal. Their seat counts as abstain for this proposal only. Quarantine is recorded in `quarantinedAppointees`.

### Step 3: 180-Day Evaluation Window

During the first 180-day window:
- Public comment is open to all stakeholders
- Technical Council and Stewardship Custodians may request clarifications from the suspended proposer
- Independent security, constitutional, and regulatory review is encouraged
- The proposer may testify but not advocate

At the close of the first 180-day window, Vote 1 is scheduled.

### Step 4: Vote 1 (voteNumber: 1)

Both chambers vote independently.

**Technical Council (9 members, proposal rights only):**
- Threshold: 75% of `seatedActiveMembers` (excluding suspended proposer and quarantined appointees)
- Vote recorded via `recordTriCameralVote` with `chamber: 0`, `voteNumber: 1`

**Stewardship Custodians (11 members, binding veto):**
- Threshold: 75% of `seatedActiveMembers` (excluding quarantined appointees)
- Vote recorded via `recordTriCameralVote` with `chamber: 1`, `voteNumber: 1`
- If `vetoExercised: true` -- proposal constitutionally blocked, `TriCameralConstitutionalVeto` emitted, process ends
- Institution ban clock confirmed active

If Vote 1 passes both chambers at 75% with no veto -- proceed to Step 5.
If Vote 1 fails threshold in either chamber -- proposal fails. Proposer's institution may not resubmit the same proposal for one year.

### Step 5: Second 180-Day Window

A second mandatory 180-day evaluation window opens after Vote 1 passage. This window exists to detect second-order effects, implementation risks, and slow-emerging objections that were not visible at Vote 1.

No acceleration is permitted. The second window runs its full 180 days regardless of political urgency, technical readiness, or external pressure. The suspended proposer may continue to testify during this window.

### Step 6: Vote 2 (voteNumber: 2)

Both chambers vote again under identical conditions as Vote 1. The same thresholds apply. Stewardship Custodians retain their binding veto for Vote 2.

If Vote 2 passes both chambers at 75% with no veto -- proposal is ratified.
If Vote 2 fails -- proposal fails. A new proposal with the same substance may not be submitted for one year.

### Step 7: Ratification and Execution

`executeTriCameralRatification` is called with the `treasuryAttestation` generated automatically by the Smart Contract Treasury. No human supplies or modifies this attestation.

The `TriCameralRatificationExecuted` event is emitted on-chain. The ratification is immutable from this point. The proposal enters implementation.

### Step 8: Proposer Reinstatement

Once the proposal is either ratified or failed, the proposing Technical Council member's suspension ends. Their seat is reinstated. If their seat was filled during the suspension period (after the one-year institution ban expires), the reinstatement process follows the standard vacancy confirmation procedure in [`governance/SEAT_SELECTION.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/governance/SEAT_SELECTION.md).

---

## Part V: Veto Consequences

When a Stewardship Custodian exercises their binding veto:

- `TriCameralConstitutionalVeto` is emitted on-chain with `proposalId`, `vetoTimestamp`, and `survivabilityClass`
- The proposal is constitutionally blocked -- no appeal, no re-vote, no override
- The `vetoTimestamp` is the start of the one-year institution ban for the proposer's institution
- The blocked proposal is permanently recorded in the governance audit trail

A vetoed survivability-class proposal may be redesigned and resubmitted as a new proposal after one year. The new proposal is treated as an entirely new submission with a new `clockStartTimestamp`.

---

## Part VI: Proposal Registry

Every proposal -- standard or survivability-class, passed or blocked -- is permanently recorded on-chain via `registerTriCameralProposal`. The registry is public and immutable. It includes:

- `proposalId` -- unique identifier
- `proposalHash` -- SHA-256 hash of the full proposal text
- `survivabilityClass` -- boolean
- `clockStartTimestamp` -- submission timestamp
- `proposerMemberId` -- identity of the submitting Technical Council member
- All vote records from both chambers
- Final status: ratified, blocked by veto, or failed threshold

The registry constitutes the complete constitutional amendment history of TML. It cannot be expunged, altered, or hidden.

---

## Part VII: Proposal Text Requirements

All proposal text must:

- State the specific schema, code, or document sections being modified
- Provide the exact before and after text for every change
- Include a survivability-class justification or non-survivability-class justification
- Include a regulatory impact assessment (EU AI Act, NIST RMF, ISO 42001)
- Confirm that Forced State +1 is not introduced anywhere in the proposed changes
- Confirm that the Goukassian Vow is not modified
- Be written without em dashes -- hyphens or rewritten sentences only

---

## Authority

**Architect:** Lev Goukassian
**ORCID:** [0009-0006-5966-1243](https://orcid.org/0009-0006-5966-1243)
**Parent Constitution:** [`governance/Tri_Cameral_Constitution.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/governance/Tri_Cameral_Constitution.md)
**On-Chain Enforcement:** [`API/tml_abi.json`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/API/tml_abi.json)
**Schema:** [`API/tml_schema.json`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/API/tml_schema.json) -- `TriCameralApproval`

---

*"Pause when truth is uncertain. Refuse when harm is clear. Proceed where truth is."*
-- The Goukassian Vow
