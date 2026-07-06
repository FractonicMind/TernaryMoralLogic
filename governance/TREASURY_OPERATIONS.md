# Ternary Moral Logic: Treasury Operations Protocol

### **How the Smart Contract Treasury Initializes, Encodes, and Executes**

**Architect:** Lev Goukassian
**ORCID:** [0009-0006-5966-1243](https://orcid.org/0009-0006-5966-1243)
**Parent Document:** [`governance/Tri_Cameral_Constitution.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/governance/Tri_Cameral_Constitution.md)
**Status:** Operational Protocol

---

## Purpose

The Smart Contract Treasury is the execution layer of TML governance. It has no vote rights, no discretion, and no admin key. It executes ratified proposals automatically. It cannot be halted, paused, redirected, or shut down by any authority. This document defines how it is initialized, how disbursement rules are encoded, and how execution works in practice.

---

## Part I: What the Treasury Is

The Smart Contract Treasury is not a financial institution. It does not hold funds for operational expenses. It holds the constitutional execution authority for governance ratification.

Its three functions are:

**Record** -- every ratified proposal is permanently recorded on-chain via `executeTriCameralRatification`. The record is immutable.

**Execute** -- when both chambers have passed a proposal at the required threshold and all Section 7A requirements are satisfied, the Treasury executes the ratification automatically. No human instruction is required or accepted.

**Enforce** -- the Treasury enforces the ratification chain. A proposal that has not completed the full ratification process will revert `TriCameralNotRatified` on any execution attempt. There is no bypass.

---

## Part II: No Admin Key

The Smart Contract Treasury has no admin key. This is not a policy. It is an architectural property encoded at deployment.

What this means in practice:

- No individual can instruct the Treasury to execute a non-ratified proposal
- No institution can instruct the Treasury to block a ratified proposal
- No government, regulator, or court order can compel the Treasury to reverse a completed execution
- No emergency override mechanism applies to the Treasury -- the `executeEmergencyOverride` function in `TML_Core` explicitly excludes Treasury state from its scope
- No upgrade proxy exists that could be used to modify Treasury logic after deployment

The absence of an admin key is the No Switch Off mandate applied to governance execution itself. An institution that cannot halt execution cannot be pressured to halt execution.

---

## Part III: Initialization

The Treasury is initialized once at deployment. Initialization requires Joint-Approval: a confirmed vote from both the Technical Council and the Stewardship Custodians under the standard proposal process defined in [`governance/PROPOSAL_PROCESS.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/governance/PROPOSAL_PROCESS.md).

### Initialization Parameters

The following parameters are set at initialization and are survivability-class -- they cannot be modified without the full Section 7A dual-vote protocol:

| Parameter | Description |
|---|---|
| `ratificationThreshold` | 75% of seatedActiveMembers in both chambers |
| `survivabilityDualVoteRequired` | true -- enforces two-vote requirement for survivability-class proposals |
| `adminKey` | address(0) -- no admin key, permanently |
| `upgradeProxy` | address(0) -- no upgrade proxy, permanently |
| `voteNumberRequired` | 2 for survivability-class, 1 for standard |
| `institutionBanDuration` | 365 days from clockStartTimestamp |
| `quarantineWindow` | 90 days from clockStartTimestamp |

These parameters are written to the contract at deployment and enforced by the contract logic. They cannot be overwritten by any subsequent transaction.

---

## Part IV: Joint-Approval for Encoding Disbursement Rules

If the Treasury is used to encode disbursement rules -- for example, directing penalty funds to the Memorial Fund, or allocating governance resources to seated custodians -- those rules require Joint-Approval before encoding.

Joint-Approval means:

- A governance proposal defining the disbursement rules is submitted through the standard proposal process
- Both chambers vote at simple majority (standard proposal) or 75% dual-vote (survivability-class, if the disbursement rules touch constitutional parameters)
- No Stewardship Custodian veto is exercised
- `executeTriCameralRatification` is called and the ratification is recorded on-chain
- Only then are the disbursement rules encoded into the Treasury contract

No disbursement rule may be encoded unilaterally by either chamber, by the architect, or by any external party. The Joint-Approval requirement is enforced at the contract level -- disbursement encoding functions revert unless a valid `ratificationTransactionHash` is provided that corresponds to a confirmed on-chain ratification record.

---

## Part V: Execution Mechanics

When a proposal has completed the full ratification chain, `executeTriCameralRatification` is called.

### Inputs

| Input | Type | Source |
|---|---|---|
| `proposalId` | bytes32 | The ratified proposal identifier |
| `treasuryAttestation` | bytes | Generated automatically by the Treasury contract |

The `treasuryAttestation` is generated by the Treasury contract itself upon verification that both chambers have passed at threshold and all Section 7A requirements are satisfied. No human generates, supplies, or modifies this value. Any attempt to supply a manually constructed `treasuryAttestation` will revert -- the contract verifies the attestation against its own internal state.

### Execution Sequence

```
1. Contract verifies proposalId exists in registry
2. Contract verifies both chambers passed at 75% of seatedActiveMembers
3. Contract verifies voteNumber requirements satisfied
   -- Standard: voteNumber 1 passed
   -- Survivability-class: both voteNumber 1 and voteNumber 2 passed
4. Contract verifies no TriCameralConstitutionalVeto was emitted for this proposalId
5. Contract verifies Section 7A requirements (proposerExitConfirmed, clockStartTimestamp elapsed)
6. Contract generates treasuryAttestation internally
7. Contract emits TriCameralRatificationExecuted event
8. Contract records executionTransactionHash and executedAt timestamp
9. Disbursement rules execute if encoded for this proposal type
```

If any verification step fails, the transaction reverts with `TriCameralNotRatified` and a human-readable `missingRequirement` string identifying exactly which condition was not met.

### Outputs

| Output | Type | Description |
|---|---|---|
| `executionTransactionHash` | bytes32 | On-chain transaction hash of the execution event |
| `executedAt` | uint256 | Unix epoch timestamp of execution |

Both outputs are permanently recorded and publicly queryable.

---

## Part VI: What the Treasury Cannot Do

For constitutional clarity:

The Treasury cannot execute a proposal that was vetoed. Once `TriCameralConstitutionalVeto` is emitted for a `proposalId`, that proposal is permanently blocked at the contract level.

The Treasury cannot execute a survivability-class proposal after only one vote. The `voteNumber: 2` record must exist on-chain before execution proceeds.

The Treasury cannot be paused by any emergency override. The `BREAK_GLASS_SHUTDOWN` and `KILL_SWITCH` override types explicitly exclude Treasury execution from their scope.

The Treasury cannot backdate an execution. The `executedAt` timestamp is set by the block timestamp at the moment of execution. It cannot be set to a past or future value.

The Treasury cannot execute a proposal whose `clockStartTimestamp` has not elapsed the required evaluation window. Time-based requirements are enforced by comparing block timestamps against the recorded `clockStartTimestamp`.

---

## Part VII: Audit and Transparency

Every Treasury action is publicly visible on-chain. Any party may query:

- The complete registry of ratified proposals and their execution timestamps
- The complete registry of blocked proposals and their veto timestamps
- The current Treasury initialization parameters
- The ratification status of any specific `proposalId`

The Treasury emits structured events for every significant state change. These events are indexed by `proposalId` and queryable by any blockchain explorer or audit tool.

Regulators, courts, and researchers may verify the complete governance history of TML without requiring access to any private system, any off-chain database, or any cooperation from any institution. The blockchain is the sole and sufficient source of truth for governance execution.

---

## Part VIII: Relationship to Other Governance Documents

The Treasury Operations Protocol is the final layer in a four-document operational stack:

| Document | Governs |
|---|---|
| `SEAT_SELECTION.md` | Who sits in each chamber |
| `PROPOSAL_PROCESS.md` | How proposals are submitted and ratified |
| `VETO_PROTOCOL.md` | How the binding veto is exercised |
| `TREASURY_OPERATIONS.md` | How ratification is executed and recorded |

All four documents are operational companions to [`governance/Tri_Cameral_Constitution.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/governance/Tri_Cameral_Constitution.md), which is the primary constitutional authority. In the event of any conflict between an operational document and the constitution, the constitution governs.

---

## Authority

**Architect:** Lev Goukassian
**ORCID:** [0009-0006-5966-1243](https://orcid.org/0009-0006-5966-1243)
**Parent Constitution:** [`governance/Tri_Cameral_Constitution.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/governance/Tri_Cameral_Constitution.md)
**On-Chain Enforcement:** [`API/tml_abi.json`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/API/tml_abi.json) -- `executeTriCameralRatification`
**Schema:** [`API/tml_schema.json`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/API/tml_schema.json) -- `TriCameralApproval.smartContractTreasuryExecution`

---

*"Pause when truth is uncertain. Refuse when harm is clear. Proceed where truth is."*
-- The Goukassian Vow
