# Ternary Moral Logic: Veto Protocol

### **How the Stewardship Custodians Exercise Their Binding Constitutional Veto**

**Architect:** Lev Goukassian
**ORCID:** [0009-0006-5966-1243](https://orcid.org/0009-0006-5966-1243)
**Parent Document:** [`governance/Tri_Cameral_Constitution.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/governance/Tri_Cameral_Constitution.md)
**Status:** Operational Protocol

---

## Purpose

The Stewardship Custodians' binding veto is the single most powerful action in the TML governance architecture. This document defines precisely how it is exercised, what it produces on-chain, and what its consequences are. It exists so that the veto is never ambiguous, never deniable, and never reversible.

---

## Part I: The Nature of the Veto

The Stewardship Custodian veto is not a vote against a proposal. It is a constitutional block. The distinction matters:

A vote against requires counting. A threshold must be crossed. A coalition must form. This makes it vulnerable to pressure, persuasion, and erosion over time.

A constitutional block requires only one Stewardship Custodian to act. A single `vetoExercised: true` submission from any seated active Stewardship Custodian supersedes all vote counts from both chambers. It does not matter whether the Technical Council voted 9-0 in favor. It does not matter whether the other ten Stewardship Custodians voted in favor. One veto blocks constitutionally.

This asymmetry is intentional and permanent. It is the primary defense against the slow erosion attack vector -- the gradual softening of constitutional constraints through incremental proposals that each appear minor but cumulatively hollow out enforcement.

The veto has no appeal path. There is no override mechanism. There is no authority that can reverse it.

---

## Part II: Veto Eligibility

Any seated active Stewardship Custodian may exercise the veto. The following conditions apply:

- The member must be a confirmed, seated Stewardship Custodian at the time of the vote
- The member must not be quarantined from this specific proposal (appointed within 90 days of `clockStartTimestamp`)
- The member must not have a disclosed, unresolved conflict of interest with respect to this proposal

A quarantined member may not exercise the veto on the specific proposal for which they are quarantined. They may exercise the veto on all other proposals.

There is no minimum threshold for the veto. A single eligible Stewardship Custodian acting alone is constitutionally sufficient.

---

## Part III: The Mandatory Veto Obligation

The veto is not merely a right. It is an obligation under defined conditions.

A Stewardship Custodian is constitutionally obligated to veto any proposal that creates credible risk of violating any Immutable Mandate:

- No Switch Off
- No Spy
- No Weapon
- The three-state model (+1, 0, -1)
- The Goukassian Vow
- The NL=NA enforcement chain

Failure to veto a proposal that violates an Immutable Mandate is a breach of the Stewardship Custodian's institutional commitment. It is enforceable at the social, reputational, and legal layer. It is grounds for removal under the procedures in [`governance/SEAT_SELECTION.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/governance/SEAT_SELECTION.md).

This obligation exists because the hardware enforcement floor -- the Triadic Coprocessor Architecture -- provides the ultimate backstop only for deployments on compliant hardware. The Stewardship Custodian veto is the constitutional backstop for the software governance layer. Both must function.

---

## Part IV: Veto Signing Process

The veto is exercised through the `recordTriCameralVote` ABI function with `vetoExercised: true`. It must be accompanied by a valid EIP-712 signature under the `StewardshipCustodianVote` typed data schema defined in [`API/eip712_typed_data.json`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/API/eip712_typed_data.json).

### Required Fields

| Field | Value | Purpose |
|---|---|---|
| `proposalId` | bytes32 | Identifies the proposal being vetoed |
| `chamber` | 1 | Identifies Stewardship Custodian chamber |
| `vetoExercised` | true | Triggers constitutional block |
| `voteNumber` | 1 or 2 | Which vote in the dual-vote sequence |
| `seatedActiveMembers` | current count | Confirms quorum context |
| `chamberAttestation` | bytes | EIP-712 signature from the vetoing institution |

### Signing Steps

1. The vetoing institution's authorized officer generates the `StewardshipCustodianVote` typed data structure with `vetoExercised: true`
2. The structure is signed using the institution's registered EIP-712 key
3. The signed attestation is submitted via `recordTriCameralVote`
4. The on-chain contract verifies the signature against the registered seat holder
5. `TriCameralConstitutionalVeto` event is emitted

The signature cannot be forged, backdated, or repudiated. The on-chain record is permanent.

---

## Part V: On-Chain Consequences

When `vetoExercised: true` is submitted and verified, the following occur automatically and simultaneously:

**`TriCameralConstitutionalVeto` event emitted** with:
- `proposalId` (indexed) -- the blocked proposal
- `vetoTimestamp` -- Unix epoch timestamp of the veto
- `survivabilityClass` -- whether this was a survivability-class proposal

**Proposal status set to BLOCKED** -- the `executeTriCameralRatification` function will revert `TriCameralNotRatified` for this proposal permanently.

**Institution ban clock started** -- the proposing Technical Council member's institution is banned from filling any vacated seat for one year from `vetoTimestamp`.

**Governance registry updated** -- the blocked proposal is permanently recorded with its full vote history and the veto record.

None of these consequences can be reversed, expunged, or modified by any authority. The Smart Contract Treasury has no function to undo a constitutional veto. No admin key exists that could alter the record.

---

## Part VI: Public Disclosure

The `TriCameralConstitutionalVeto` event is publicly visible on-chain. Any party may query the blockchain to confirm that a specific proposal was constitutionally blocked, by which chamber, at what timestamp, and whether it was survivability-class.

The vetoing institution is identified by their registered seat. The specific individual who signed the attestation within that institution is identified by their EIP-712 key.

There is no provision for anonymous vetoes. Constitutional acts of this magnitude require institutional accountability.

---

## Part VII: Post-Veto Procedures

### For the Blocked Proposal

The proposal is permanently blocked in its current form. It cannot be resubmitted as-is. A redesigned proposal addressing the concerns that motivated the veto may be submitted after one year from `vetoTimestamp`. The redesigned proposal is treated as a new submission with a new `clockStartTimestamp`.

### For the Vetoing Institution

The vetoing institution has no special procedural obligations after exercising the veto. They continue as a seated Stewardship Custodian with full veto authority on subsequent proposals.

### For the Proposing Institution

The proposing institution's chamber membership suspension continues until the Section 7A clock expires. The one-year institution ban on filling vacated seats runs from `vetoTimestamp`. The institution may continue to participate in other governance activities -- submitting new proposals on unrelated matters, participating in seat confirmation votes -- subject to the ban constraint.

### For the Governance Record

The complete veto record -- proposal text hash, vote history, veto timestamp, vetoing institution identity -- is permanently stored in the on-chain governance registry. It is included in all future governance audit exports and accessible to any regulator, court, or researcher querying the blockchain.

---

## Part VIII: What the Veto Cannot Do

For constitutional clarity:

The veto cannot be used to block the Goukassian Vow. The Vow is an Immutable Mandate -- it is not subject to any governance process, including the veto.

The veto cannot be used retroactively. It applies only to proposals currently in the active vote cycle.

The veto cannot be delegated. An institution's authorized officer must personally sign the EIP-712 attestation. Proxy vetoes are not recognized.

The veto cannot be exercised by the Technical Council. Proposal rights and veto rights are constitutionally separated. A Technical Council member who attempts to submit `vetoExercised: true` will receive a revert -- the contract enforces this separation at the ABI layer.

The veto cannot be reversed by a subsequent Stewardship Custodian vote. Once `TriCameralConstitutionalVeto` is emitted, the block is permanent.

---

## Authority

**Architect:** Lev Goukassian
**ORCID:** [0009-0006-5966-1243](https://orcid.org/0009-0006-5966-1243)
**Parent Constitution:** [`governance/Tri_Cameral_Constitution.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/governance/Tri_Cameral_Constitution.md)
**Seat Selection:** [`governance/SEAT_SELECTION.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/governance/SEAT_SELECTION.md)
**Proposal Process:** [`governance/PROPOSAL_PROCESS.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/governance/PROPOSAL_PROCESS.md)
**On-Chain Enforcement:** [`API/tml_abi.json`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/API/tml_abi.json) -- `recordTriCameralVote`, `TriCameralConstitutionalVeto`
**EIP-712 Schema:** [`API/eip712_typed_data.json`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/API/eip712_typed_data.json) -- `StewardshipCustodianVote`

---

*"Pause when truth is uncertain. Refuse when harm is clear. Proceed where truth is."*
-- The Goukassian Vow
