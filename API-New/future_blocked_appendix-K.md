## 2. future_blocked_appendix.md

### 2.1 Real-Time Per-Token Blockchain Anchoring

#### 2.1.1 Architectural Target

The architectural target of **real-time per-token blockchain anchoring** represents the maximal transparency ideal: every Permission Token, at the moment of its issuance, is individually and irreversibly recorded on a public blockchain, creating instantaneous global visibility into system moral decisions. This target eliminates the batching delay that the current Merkle-batched anchoring implementation introduces, reducing the window between decision and public accountability from minutes or hours to seconds or less. The monograph acknowledges this ideal in Section 2.4.1, where it describes Merkle-Batched Anchoring as an optimization rather than the ultimate form of transparency.

#### 2.1.2 Blocking Constraint: Throughput Asymmetry

The blocking constraint that prevents this target from becoming a shipping specification is **throughput asymmetry**: the fundamental mismatch between AI inference throughput and blockchain write capacity. Contemporary AI systems operate at **millions of transactions per second** during peak inference loads, while even the most performant public blockchains achieve **single-digit to low-double-digit transactions per second** for finalized writes. This asymmetry is not a temporary limitation awaiting technological improvement; it reflects the deliberate design tradeoffs of distributed consensus, where finality requires replication and validation across geographically dispersed nodes with bounded communication speed. The monograph identifies this constraint explicitly in **Section 10.2**, titled "Latency-Legitimacy Dilemma, Throughput Asymmetry," which quantifies the gap as "three to six orders of magnitude" and concludes that "real-time per-token anchoring at global AI scale remains beyond current technological feasibility."

| System Component | Throughput Capacity | Bottleneck Factor |
|:---|:---|:---|
| Global AI inference (aggregate) | ~10^6 TPS | Decision generation rate |
| Ethereum mainnet | ~15 TPS | Consensus protocol, block size |
| Optimistic L2 (e.g., Arbitrum) | ~40,000 TPS | Data availability, fraud proof window |
| ZK-Rollup L2 (theoretical max) | ~2,000 TPS | Prover computation, data compression |
| Required for per-token anchoring | ~10^6 TPS | Matching inference throughput |

#### 2.1.3 Mitigation and Remaining Gap

The mitigation that the monograph proposes, and that the current API specification implements, is **Merkle-batched anchoring**, which aggregates multiple Permission Tokens into a single Merkle tree whose root is anchored to the blockchain. This approach, operationalized through the `POST /blockchain/anchor` endpoint and `GET /audit/verifications/merkle-root/{logHash}` verification endpoint, reduces the blockchain write frequency by a factor of thousands while preserving individual token verifiability through Merkle inclusion proofs. The current `POST /blockchain/anchor` endpoint and `GET /audit/verifications/merkle-root/{logHash}` endpoint implement this mitigation, with `TSLF-State+1.audit_proof` containing the Merkle inclusion proof that connects individual tokens to batched roots.

The remaining unbuildable element is **per-token real-time finality at global AI scale**. While Merkle-batched anchoring provides eventual finality and individual verifiability, it introduces a **latency window** (batch accumulation time plus blockchain confirmation time, typically 2-10 minutes for Ethereum mainnet) during which tokens exist in a pre-anchored state. During this window, the system relies on internal cryptographic commitments rather than public blockchain finality for non-repudiation. The specification acknowledges this limitation by classifying the endpoint as `BETA` with `x-tml-blocking-constraint: "Section 10.2"` for any implementation claiming real-time per-token anchoring, and by documenting the batch latency in endpoint descriptions.

**Status: `FUTURE`**

**`x-tml-blocking-constraint: "Section 10.2"`**

### 2.2 Quantum-Proof Signature Migration

#### 2.2.1 Architectural Target

The architectural target of **quantum-proof signature migration** addresses the existential threat that quantum computing poses to the cryptographic foundations of TML governance. Current signatures use **ECDSA over secp256k1 or Ed25519**, both of which are vulnerable to Shor's algorithm running on a sufficiently powerful quantum computer. The target envisions complete migration to **post-quantum cryptography (PQC) algorithms**, specifically the lattice-based, hash-based, or multivariate schemes that NIST has standardized, for all signing operations within the TML system. This includes Inference Lane proposals, Anchoring Lane Permission Tokens, Merkle tree construction, and all audit verification proofs. The monograph identifies quantum threats as a "horizon risk" in Section 1.4, noting that "cryptographic agility is not optional but mandatory for constitutional longevity."

#### 2.2.2 Blocking Constraint: PQC Standardization and Performance

The blocking constraints are multiple and reinforcing. First, **NIST PQC standardization**, while advanced, remains in deployment phase as of 2025; the final standards were published in 2024, but ecosystem maturity (libraries, hardware support, interoperability testing) lags significantly. Second, **PQC signatures impose severe performance penalties**: CRYSTALS-Dilithium signatures are approximately **10-100 times larger than ECDSA signatures**, and verification is **2-10 times slower**. For the Anchoring Lane's <500ms target, this penalty consumes a substantial portion of the latency budget, potentially crowding out other governance operations. Third, the **hybrid transition period**, where both classical and PQC algorithms operate in parallel, introduces complexity that the monograph warns against as a "fragility vector" where implementation errors could compromise security during the transition. The monograph consolidates these constraints in **Section 10.7**, "Quantum Computing Horizon Risks," which states that "production-grade PQC deployment for latency-critical governance operations remains unvalidated."

| Signature Algorithm | Signature Size | Public Key Size | Verification Time | Quantum Resistance |
|:---|:---|:---|:---|:---|
| ECDSA (secp256k1) | 64 bytes | 33 bytes | ~0.1 ms | No |
| Ed25519 | 64 bytes | 32 bytes | ~0.05 ms | No |
| CRYSTALS-Dilithium (Level 2) | ~2,420 bytes | ~1,312 bytes | ~0.5 ms | Yes |
| CRYSTALS-Dilithium (Level 3) | ~3,293 bytes | ~1,952 bytes | ~0.8 ms | Yes |
| CRYSTALS-Dilithium (Level 5) | ~4,595 bytes | ~2,592 bytes | ~1.2 ms | Yes |

#### 2.2.3 Mitigation and Remaining Gap

The mitigation that the current API specification implements is **algorithm agility** through the `SignatureBlock.signatureAlgorithm` enum. The current enum includes `"ECDSA_P256"`, `"ECDSA_P384"`, and `"Ed25519"`, with documentation noting reserved identifiers for NIST PQC standards (e.g., `"ML_DSA_65"` for CRYSTALS-Dilithium, `"SLH_DSA_SHA2_128
