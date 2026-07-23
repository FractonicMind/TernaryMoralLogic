# TML Dual-Lane Architecture: Constitutional Amendment v1.0

## **Terminology Correction and Latency Reframing**

**Architect:** Lev Goukassian   
**ORCID:** [0009-0006-5966-1243](https://orcid.org/0009-0006-5966-1243)   
**Document Status:** Active Constitutional Amendment   
**Amends:** All four audit documents in this folder (February 2026 vintage)   
**License:** CC BY 4.0

---

## Preamble

The four independent engineering audits in this folder were completed in February 2026. They are rigorous, accurate, and constitute the foundational technical validation of the Commit-Bound Dual-Latency Architecture. They are not being rewritten. They are being amended.

Two corrections are required:

**Correction 1 -- Terminology:** The audit documents use "Fast Lane" and "Slow Lane." The canonical TML constitutional terminology is "Inference Lane" and "Anchoring Lane." This amendment formally declares the equivalence so that the audits remain authoritative while conforming to constitutional terminology standards.

**Correction 2 -- Latency Framing:** The audit documents treat 500ms as the Slow Lane / Anchoring Lane specification. This conflates two distinct things: the hardware-owned Provisional Permission Token (PPT) issuance time, and the operator-configured Final Permission Token (FPT) completion time that depends on external blockchain infrastructure. The 500ms figure accurately describes current FPT timing on permissioned chains. It does not describe the owned hardware specification. This amendment formally separates them.

Neither correction changes the architecture. Neither correction changes the security analysis. Neither correction changes the failure mode classifications. The audits are correct. Their framing is being made more precise.

---

## Correction 1: Terminology Equivalence

The following terminology equivalences are constitutionally declared. In all four audit documents, wherever "Fast Lane" appears, read "Inference Lane." Wherever "Slow Lane" appears, read "Anchoring Lane."

| Audit Document Term | Constitutional Term | Notes |
|---|---|---|
| Fast Lane | Inference Lane | Identical function, updated name |
| Slow Lane | Anchoring Lane | Identical function, updated name |
| Fast Lane LLM | Inference Lane model | Identical function, updated name |
| Slow Lane validation | Anchoring Lane validation | Identical function, updated name |
| Slow Lane timeout | Anchoring Lane timeout | Identical function, updated name |
| Slow Lane capacity | Anchoring Lane capacity | Identical function, updated name |

This equivalence applies retroactively to all four audit documents without requiring their text to be changed. Any future document in this folder uses Inference Lane and Anchoring Lane exclusively. The audit documents retain their original terminology as historical record.

**Why the terminology changed:** "Fast" and "Slow" describe latency characteristics. "Inference" and "Anchoring" describe constitutional function. The constitutional framing is more precise and aligns with TML's Eight Pillar architecture, where the Anchoring Lane performs the governance and immutability functions that Pillars II, IV, VII, and VIII describe. A lane named for what it does is more durable than a lane named for how quickly it does it -- especially now that the Anchoring Lane issues its Provisional Permission Token in under 50ms.

---

## Correction 2: Latency Reframing

### The Problem With 500ms as a Specification

The audit documents state the Slow Lane / Anchoring Lane has a "≤500ms local log sealing target." This number appears in:

- `Production-Grade Hardening of Commit-Bound Dual-Latency Architecture.md` -- lines 45, 61, 67, 87, 182 and throughout
- `Architecting Trust in AI...md` -- line 17 and throughout
- `Infrastructure-Realism-and-Economic-Viability...md` -- multiple references
- `Transactional-Integrity-and-Hardware-Aware-Intent-Classification...md` -- multiple references

The 500ms figure is accurate for what it describes. It is the target for complete log sealing including local TEE attestation plus external blockchain anchoring confirmation. The problem is not the number. The problem is that it conflates two distinct components with very different properties:

**Component A -- Owned hardware processing (PPT):**
- SHA-256 hashing of the action state: ~1 microsecond
- Merkle pre-computation: ~16 microseconds at 1GHz
- HSM signing of the Moral Trace Log: ~5-10 milliseconds
- C-element Sacred Zero release: ~1 nanosecond
- **Total: under 50ms -- entirely on hardware we control**

**Component B -- External infrastructure anchoring (FPT):**
- Network transmission to anchoring service: variable
- Blockchain consensus wait: variable (depends on chain choice)
- Anchor receipt confirmation: variable
- **Total: operator-configured -- integration parameter, not hardware specification**

The 500ms figure is Component A + Component B combined. Component A alone is under 50ms.

### The Constitutional Correction

**The Provisional Permission Token (PPT)** is the authorizing artifact issued at the completion of Component A. It is issued in under 50ms on hardware we own. It satisfies the Muller C-element. It releases the Sacred Zero. It authorizes execution. All of this happens before any external infrastructure is consulted.

**The Final Permission Token (FPT)** supersedes the PPT when Component B completes. FPT timing is the operator's integration parameter. It may be 300-500ms on a permissioned chain, minutes on a public chain with multiple confirmations, or nanoseconds on future infrastructure. The DLLA hardware makes no claims about FPT timing.

### Errata Table

The following statements in the audit documents are superseded by this amendment:

| Document | Original Statement | Superseded By |
|---|---|---|
| Production-Grade Hardening, line 45 | "≤500 ms local log sealing target" | PPT under 50ms (hardware-owned); FPT operator-configured |
| Production-Grade Hardening, line 61 | "Local TEE Sealing -- 500 ms" | PPT under 50ms via HSM; FPT asynchronous |
| Production-Grade Hardening, line 67 | "Local sealing (500 ms) is decoupled from global settlement" | Correct that they are decoupled -- PPT is under 50ms, FPT is operator-configured |
| Architecting Trust, line 17 | "total time from intent detection to approval under...500ms" | Total PPT issuance under 50ms; FPT asynchronous |
| All four documents | Any reference to Slow Lane latency as 500ms | Read as "Anchoring Lane PPT under 50ms / FPT operator-configured" |

The decoupling principle described in the audit documents -- "local sealing decoupled from global settlement" -- is constitutionally correct and is the foundation of the PPT/FPT distinction. This amendment makes that decoupling explicit at the specification level.

---

## The Two-Token Architecture

The PPT/FPT distinction formalizes a constitutional two-token model first described in the TL companion specification (`DLLA_PPT_SPECIFICATION_ADDENDUM.md`):

**Provisional Permission Token (PPT) -- issued under 50ms:**
- Issued after local HSM signing and Merkle pre-computation
- Satisfies the Muller C-element -- Sacred Zero releases
- Authorizes provisional execution
- Carries `provisionalExpiry`: if FPT does not arrive within the configured window, the C-element automatically reverts the provisional commit
- Hardware-enforced -- no software can prevent the automatic revert

**Final Permission Token (FPT) -- issued at operator-configured time:**
- Issued when external anchoring confirms
- Supersedes the PPT -- execution is now fully and publicly anchored
- Timing is the operator's infrastructure choice, not a hardware specification

**The headline specification:** *"Hardware-enforced moral governance authorization in under 50ms."*

This is owned. It is determined by hardware physics. It will not change unless the hardware design changes.

---

## What This Amendment Does Not Concede

**The 500ms figure in the audit documents is not wrong.** It accurately describes the total time for PPT issuance plus FPT completion on permissioned blockchain infrastructure with sub-second block times. This amendment does not claim the audits made an error. It claims the number needs to be decomposed into its owned and operator-configured components.

**The Fail-Closed analysis in the audit documents is not changed.** Anchoring Lane timeout behavior, degraded mode classification, and the Pessimistic Mode requirement for hard-state domains (Finance, Medical, Autonomous Actuation) are all correct and remain fully in force. The PPT/FPT distinction does not affect fail-safe logic -- if the Anchoring Lane fails to issue a PPT within the configured window, the system halts. That is unchanged.

**The security analysis in the audit documents is not changed.** The race condition analysis, the intent classifier hardening requirements, the pre-execution authorization model, and the action state machine are all correct. This amendment only changes what latency number is associated with the Anchoring Lane authorization.

**The four audit documents remain the authoritative technical validation of the architecture.** This amendment sits on top of them. It does not replace them.

---

## Companion Documents

| Document | Location |
|---|---|
| PPT Specification Addendum (TL) | [`TernaryLogic/Dual_Latency_Architecture/DLLA_PPT_SPECIFICATION_ADDENDUM.md`](https://github.com/FractonicMind/TernaryLogic/blob/main/Dual_Latency_Architecture/DLLA_PPT_SPECIFICATION_ADDENDUM.md) |
| Engineering Gaps v1.0 (TL) | [`TernaryLogic/Dual_Latency_Architecture/DLLA_ENGINEERING_GAPS_v1.md`](https://github.com/FractonicMind/TernaryLogic/blob/main/Dual_Latency_Architecture/DLLA_ENGINEERING_GAPS_v1.md) |
| Consumer Applications (TL) | [`TernaryLogic/Dual_Latency_Architecture/DLLA_CONSUMER_APPLICATIONS.md`](https://github.com/FractonicMind/TernaryLogic/blob/main/Dual_Latency_Architecture/DLLA_CONSUMER_APPLICATIONS.md) |
| TML DLLA readme | [`TernaryMoralLogic/Dual_Latency_Architecture/readme.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/Dual_Latency_Architecture/readme.md) |

---

## Authority

**Architect:** Lev Goukassian   
**ORCID:** [0009-0006-5966-1243](https://orcid.org/0009-0006-5966-1243)   
**Amends:** All documents in [`TernaryMoralLogic/Dual_Latency_Architecture/`](https://github.com/FractonicMind/TernaryMoralLogic/tree/main/Dual_Latency_Architecture)   
**Constitutional Governance:** [`governance/Tri_Cameral_Constitution.md`](https://github.com/FractonicMind/TernaryMoralLogic/blob/main/governance/Tri_Cameral_Constitution.md)   

---



*"Pause when truth is uncertain. Refuse when harm is clear. Proceed where truth is."*
-- The Goukassian Vow
