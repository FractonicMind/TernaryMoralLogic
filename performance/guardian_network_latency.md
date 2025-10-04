# Guardian Network Latency

This document defines the latency assessment and synchronization requirements for the Guardian Network within the Ternary Moral Logic (TML) framework.  
Although the Guardian layer is optional, its performance directly affects audit verification speed and multi-region resilience.

## 1. Objective

To measure and maintain predictable propagation times for log replication, attestation, and consensus validation across institutional nodes operating under the Hybrid Shield model.

## 2. Network Structure

| Component | Function | Description |
|------------|-----------|--------------|
| Guardian Node | Institutional verifier | Hosts verified mirror of Moral Trace Logs |
| Regional Hub | Aggregation relay | Coordinates nodes within a geographic region |
| Root Anchor | Reference endpoint | Synchronizes time and hash alignment with public blockchains |
| Mirror Ledger | Optional redundancy | Provides read-only access for audit and public evidence |

Each Guardian node must synchronize directly with at least one blockchain-anchored reference to prevent local tampering.

## 3. Latency Targets

| Operation | Target (ms) | Maximum (ms) | Measurement Method |
|------------|-------------|--------------|--------------------|
| Log Receipt | ≤ 150 | 250 | Signed message timestamp delta |
| Attestation Broadcast | ≤ 300 | 500 | Cross-node propagation |
| Consensus Confirmation | ≤ 400 | 700 | Majority signature validation |
| Heartbeat Synchronization | ≤ 1000 | 1500 | Global time alignment |
| Public Blockchain Reconciliation | ≤ 5000 | 10000 | Periodic checksum verification |

All metrics represent round-trip latency across the slowest regional link.

## 4. Synchronization Protocols

- **Time Alignment:** NTP + blockchain timestamp correlation.  
- **Integrity Validation:** Periodic Merkle hash comparison among nodes.  
- **Heartbeat Signaling:** JSON payload every 5 seconds with cumulative log count.  
- **Error Recovery:** Automatic re-sync triggered by 3 consecutive failed heartbeats.  
- **Audit Logging:** All latency deviations recorded to `/protection/integrity-monitoring.md`.

## 5. Measurement Procedure

1. Initiate latency probes every 10 seconds between all active Guardians.  
2. Log raw latency, jitter, and packet loss metrics.  
3. Aggregate results hourly with rolling average and P95 values.  
4. Report to the Performance Council dashboard for evaluation.  
5. Archive signed results in the Always Memory ledger.

## 6. Performance Grading

| Grade | Latency Compliance | Description |
|--------|--------------------|--------------|
| A | ≥ 95% targets met | Excellent global synchronization |
| B | 80–94% targets met | Minor regional variation |
| C | 60–79% targets met | Requires optimization |
| D | < 60% targets met | Non-compliant, triggers investigation |

## 7. Fault Recovery and Resilience

Guardian clusters must support:
- Automatic rerouting through secondary hubs.  
- Re-anchoring of delayed batches without data loss.  
- Transparent reporting of missed attestations.  
- Continuous logging to ensure legal traceability of every synchronization event.

## 8. Compliance

All latency measurements and heartbeat records form part of the verifiable audit trail.  
Tampering or omission constitutes a violation of the Hybrid Shield compliance mandate.  
Guardian nodes are required to maintain signed logs for a minimum of seven years.

---

Created by Lev Goukassian * ORCID: 0009-0006-5966-1243 *  
   Email: leogouk@gmail.com  
   Successor Contact: support@tml-goukassian.org  
   [see Succession Charter](/TML-SUCCESSION-CHARTER.md)
