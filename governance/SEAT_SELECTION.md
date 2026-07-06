# Ternary Moral Logic: Seat Selection Protocol

### **How Open Institutional Seats Are Filled in the Tri-Cameral Governance Structure**

**Architect:** Lev Goukassian
**ORCID:** [0009-0006-5966-1243](https://orcid.org/0009-0006-5966-1243)
**Parent Document:** [`governance/Tri_Cameral_Constitution.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/governance/Tri_Cameral_Constitution.md)
**Status:** Operational Protocol

---

## Purpose

The Tri-Cameral governance structure has three chambers: the Technical Council (9 members), the Stewardship Custodians (11 members), and the Smart Contract Treasury (no members -- automatic execution). This document governs how seats in the Technical Council and Stewardship Custodians are filled, confirmed, rotated, and vacated.

No seat is pre-assigned to any named organization. Every seat is an open institutional position. The criteria for filling a seat are defined here. The organization that fills it is determined by the nomination and confirmation process defined here.

---

## Part I: Seat Categories

### Technical Council -- 9 Seats

The Technical Council holds proposal rights only. Its members submit governance proposals; they do not vote on survivability-class proposals they themselves submitted. Seat categories are defined by domain expertise required, not by organizational identity:

| Seat | Domain | Expertise Required |
|---|---|---|
| TC-1 | Cryptographic Engineering | Key management, threshold signatures, PQC migration |
| TC-2 | Smart Contract Architecture | Solidity, EVM, on-chain governance execution |
| TC-3 | AI Systems Engineering | Model architecture, inference pipelines, WCET enforcement |
| TC-4 | Hardware Security | HSM, DITL circuits, Triadic Coprocessor Architecture |
| TC-5 | Distributed Systems | Merkle architecture, blockchain anchoring, consensus |
| TC-6 | API and Schema Design | OpenAPI, JSON Schema, EIP-712, constitutional enforcement layers |
| TC-7 | Privacy Engineering | GDPR, EKR, Shamir Secret Sharing, PII handling |
| TC-8 | Regulatory Alignment | EU AI Act, NIST RMF, ISO 42001, Basel III/IV |
| TC-9 | Open Source Governance | Repository integrity, licensing, community stewardship |

### Stewardship Custodians -- 11 Seats

The Stewardship Custodians hold binding veto authority only. They do not submit proposals. Seat categories are defined by institutional mandate:

| Seat | Domain | Mandate |
|---|---|---|
| SC-1 | Technical Infrastructure | Repository integrity, infrastructure defense, open-source continuity |
| SC-2 | Human Rights Enforcement | Monitoring of human rights compliance, victim support |
| SC-3 | Earth Protection | Environmental treaty enforcement, ecological harm prevention |
| SC-4 | AI Ethics Research | Independent framework validation, algorithmic accountability research |
| SC-5 | Medical and Victim Compensation | Memorial Fund administration, victim compensation oversight |
| SC-6 | Legal and Constitutional | Constitutional law, international jurisdiction, evidence standards |
| SC-7 | Privacy and Civil Liberties | Surveillance prevention, data rights, No Spy mandate oversight |
| SC-8 | Academic Validation | Peer review, independent replication, longitudinal framework assessment |
| SC-9 | Community Representative | Elected by TML stakeholder community, implementer interests |
| SC-10 | Jurisdictional Diversity I | Institution domiciled outside North America and Europe |
| SC-11 | Jurisdictional Diversity II | Institution domiciled outside North America and Europe, different jurisdiction from SC-10 |

**Jurisdictional constraint:** No more than two Stewardship Custodians may reside within the same legal jurisdiction. No more than two may represent corporate entities.

---

## Part II: Nomination Process

### Who May Nominate

Any Technical Council member may nominate a candidate institution for a vacant seat. Self-nomination by an institution is permitted -- the nominating Technical Council member sponsors the application.

Nominations for Stewardship Custodian seats SC-9 (Community Representative) are submitted through a separate community election process defined in [`governance/earth/COMMUNITY_SEAT_RULES.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/governance/earth/COMMUNITY_SEAT_RULES.md).

### Nomination Package

A nomination package must contain:

1. Institution name, domicile jurisdiction, and legal entity type
2. Seat being nominated for (TC-1 through TC-9, or SC-1 through SC-11)
3. Evidence of domain expertise or mandate alignment
4. Conflict of interest disclosure -- any financial, contractual, or organizational relationship with the TML architect, any current chamber member, or any entity with a pending governance proposal
5. Jurisdictional confirmation -- confirming that seating this institution does not violate the two-per-jurisdiction constraint
6. Institutional commitment letter -- signed by an authorized officer of the nominating institution, committing to the Goukassian Vow: *"Pause when truth is uncertain. Refuse when harm is clear. Proceed where truth is."*

---

## Part III: Confirmation Process

### Technical Council Seats (TC-1 through TC-9)

Confirmation of a Technical Council nominee requires:

- Simple majority of seated active Stewardship Custodians (no veto applies to confirmations -- veto applies only to framework amendment proposals)
- 30-day public comment period before confirmation vote
- Conflict of interest review by at least two seated Stewardship Custodians not affiliated with the nominating institution

### Stewardship Custodian Seats (SC-1 through SC-11, except SC-9)

Confirmation of a Stewardship Custodian nominee requires:

- Simple majority of seated active Technical Council members
- Simple majority of seated active Stewardship Custodians
- 45-day public comment period before confirmation vote
- Conflict of interest review by at least three seated Stewardship Custodians not affiliated with the nominating institution

### SC-9: Community Representative

The Community Representative seat is filled by election, not confirmation. Election procedures are governed by [`governance/earth/COMMUNITY_SEAT_RULES.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/governance/earth/COMMUNITY_SEAT_RULES.md).

---

## Part IV: Term Lengths and Rotation

| Chamber | Term Length | Stagger |
|---|---|---|
| Technical Council | 3 years | 3 seats expire per year (years 1, 2, 3 cycle) |
| Stewardship Custodians | 4 years | 3 seats expire in years 1-3; 2 seats expire in year 4 |
| SC-9 Community Representative | 2 years | Independent election cycle |

No institution may hold the same seat for more than two consecutive terms. After two consecutive terms, a minimum one-term gap is required before re-nomination to the same seat. An institution may hold different seats consecutively without restriction.

---

## Part V: Vacancy Rules

### Standard Vacancy

A seat becomes vacant when:

- A term expires and no renewal is confirmed
- An institution voluntarily resigns with 90 days written notice
- A conflict of interest is identified that cannot be remediated
- The institution ceases to exist as a legal entity

Standard vacancies are filled through the nomination and confirmation process. Vacant seats count as abstain in all votes until filled. The 90-day nomination-and-confirmation clock starts from the date the vacancy is declared.

### Section 7A Vacancy

When a Technical Council member submits a survivability-class proposal, their seat is suspended -- not vacated -- for the duration of the Section 7A dual-vote process. The suspension ends when:

- The proposal is ratified (both votes passed)
- The proposal is vetoed by Stewardship Custodians
- The 360-day dual-vote window expires without ratification

During suspension the seat counts as abstain. The institution's seat is not available for reassignment. The proposer's institution is banned from filling any other vacated seat for one year from the `clockStartTimestamp`.

### Quarantine

New appointees confirmed within 90 days of a survivability-class proposal submission are quarantined from voting on that specific proposal. They may vote on all other matters. Quarantine ends when the Section 7A process for that specific proposal concludes.

---

## Part VI: Removal

A seated member may be removed by:

- Unanimous vote of the other chamber (all seated active members of the opposing chamber)
- Demonstrated material breach of the Goukassian Vow
- Confirmed conflict of interest that was not disclosed at nomination
- Failure to participate in three consecutive votes without documented cause

Removal triggers a standard vacancy. The removed institution is banned from re-nomination to any seat for two years from the removal date.

---

## Part VII: On-Chain Registration

Every confirmed seat holder is registered on-chain via the `registerPermissionToken` function in `TML_Core`. The `CustodianHeartbeat` endpoint in the TML API confirms active seat status. Seat suspension, quarantine, and removal are recorded as on-chain state changes, creating an immutable governance audit trail.

The `TriCameralApproval` schema in [`API/tml_schema.json`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/API/tml_schema.json) references `seatedActiveMembers` -- this value is derived from the on-chain seat registry, not from any off-chain list.

---

## Authority

**Architect:** Lev Goukassian
**ORCID:** [0009-0006-5966-1243](https://orcid.org/0009-0006-5966-1243)
**Parent Constitution:** [`governance/Tri_Cameral_Constitution.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/governance/Tri_Cameral_Constitution.md)
**On-Chain Enforcement:** [`API/tml_abi.json`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/API/tml_abi.json) -- `registerTriCameralProposal`, `recordTriCameralVote`

---

*"Pause when truth is uncertain. Refuse when harm is clear. Proceed where truth is."*
-- The Goukassian Vow
