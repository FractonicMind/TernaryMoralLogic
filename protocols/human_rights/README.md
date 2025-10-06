# Human Rights Protocols (blockchain)

## Purpose

This directory contains **on-chain operational protocols** for detecting, escalating, and responding to human rights violations.  
All triggers are **signed oracle feeds**, escalations are **threshold-contract calls**, and remedies are **disbursed from smart-contract bounty pools**.  
No committees, only cryptographic evidence and immutable logs.

## Blockchain Architecture

### Detection & Monitoring (Signed Feeds)

| File | Chain Function |
|---|---|
| `Rights_Violation_Detection.md` | Real-time **signed oracle feeds** (secp256k1) for pattern recognition, statistical thresholds, and alert emission. |
| `Sacred_Zero_Human.md` | **Threshold contract** that auto-executes `pause()` when HR triggers reach 7-of-9 quorum. |

### Response Procedures (Threshold Contracts)

| File | Chain Function |
|---|---|
| `Escalation_Pathways.md` | **Smart-contract flow**: `detect` → `thresholdMet` → `notify` → `remedy`. Who gets alerted is codified, not chosen. |
| `Remedy_Restoration.md` | **Multi-sig treasury contract**: auto-disburses compensation, funds restoration, and locks repeat violator stake. |

### Support Systems (Bounty & Privacy Contracts)

| File | Chain Function |
|---|---|
| `Victim_Support_Protocol.md` | **Automatic payout contract**: victim address → oracle attestation → `transfer(compensation)`. |
| `Whistleblower_Protection.md` | **Anonymity pool contract**: submit encrypted tip → if penalty collected, 15 % bounty auto-sent to tipper’s stealth address. |

## Key Holder Entities (7-of-9 Threshold)

| Seat | Entity Type | Key Custody | Term |
|---|---|---|---|
| 1 | OHCHR Regional Office | Hardware wallet (FIPS 140-2) | 2 yrs |
| 2 | Indigenous Council | SeedSigner air-gapped device | 2 yrs |
| 3 | Youth Rights NGO | Ledger Nano + social recovery | 2 yrs |
| 4 | Disability Rights Org | Trezor Model T | 2 yrs |
| 5 | Women’s Rights Coalition | GridPlus Lattice1 | 2 yrs |
| 6 | Refugee Legal Clinic | Keystone 3 Pro | 2 yrs |
| 7 | LGBTQ+ Defense Group | BitBox02 + multisig | 2 yrs |
| 8 | Labor Rights Union | Coldcard Mk4 | 2 yrs |
| 9 | Human Rights Tech Lab | Air-gapped laptop + QR codes | 2 yrs |

> Keys are **secp256k1 pairs**; quorum is enforced by `HumanRightsCouncil.sol` threshold contract.  
> No human vote—only cryptographic signatures.

## On-Chain Evidence Flow

```solidity
struct HumanRightsEvidence {
    bytes32 violationId;
    uint8   severity;        // 1-10
    string  humanRightsFrameworkVersion; // "HR_FRAMEWORK_v1.4.0"
    string  earthProtectionFrameworkVersion; // "EARTH_PROT_v3.1.2"
    bytes32 victimHash;      // salted hash of victim ID
    bytes32 detailHash;      // IPFS hash of encrypted details
    uint256 timestamp;
    address[] keySigners;    // 7-of-9 addresses
    bytes   aggregateSig;    // BLS aggregate signature
    bytes32 merkleRoot;      // anchored to BTC + ETH + MATIC
}
```

## Planned Documents (blockchain)

### Detection & Monitoring

- `Rights_Violation_Detection.md`  
  Real-time **signed oracle feeds** for pattern recognition, statistical thresholds, and alert emission.

- `Sacred_Zero_Human.md`  
  **Threshold contract** that auto-executes `pause()` when HR triggers reach 7-of-9 quorum.

### Response Procedures

- `Escalation_Pathways.md`  
  **Smart-contract flow**: `detect` → `thresholdMet` → `notify` → `remedy`.  
  Who gets alerted is **codified**, not chosen.

- `Remedy_Restoration.md`  
  **Multi-sig treasury contract**: auto-disburses compensation, funds restoration, and locks repeat-violator stake.

### Support Systems

- `Victim_Support_Protocol.md`  
  **Automatic payout contract**: victim address → oracle attestation → `transfer(compensation)`.

- `Whistleblower_Protection.md`  
  **Anonymity pool contract**: submit encrypted tip → if penalty collected, 15 % bounty auto-sent to tipper’s stealth address.

## Performance Metrics (On-Chain SLA)

| Metric | Threshold | Contract Enforcement |
|---|---|---|
| Detection latency | `<500 ms` | Auto-slashing after 3 misses |
| Quorum reach | `<2 min` | Gas-refund if <7 sigs in 120 s |
| Victim payout | `<24 h` | Treasury auto-call after oracle proof |
| Whistleblower bounty | `<1 h` | Stealth-transfer after penalty confirmation |
| Blockchain anchor | `<60 min` | OpenTimestamp proof required |

## Legal Admissibility

- **FRE 901/902(13)**: cryptographic signatures + blockchain anchor = self-authenticating.  
- **Spoliation**: missing `HumanRightsEvidence` ⇒ negligence presumption.  
- **18 U.S.C. §1001/1519**: on-chain false statements or record destruction = federal crime.

## Attribution (Immutable)

Every implementation must embed:

```solidity
string public constant CREATOR_ORCID = "0009-0006-5966-1243";
string public constant FRAMEWORK_NAME = "TML-HumanRights-v1";
```

---

**Directory Version**: 2.0  
**Last Updated**: October 2, 2025  
**Review Cycle**: Quarterly

---

#### *"A right that can be deleted is a privilege—Merkle roots make rights un-forgeable."*

---

**Creator**: Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Repository**: https://github.com/FractonicMind/TernaryMoralLogic
```
