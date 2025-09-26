# TML SDK Reference Implementations

**Path**: `/sdk/README.md`  
**Version**: 1.0.0  
**Creator**: Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Last Updated**: 2025-09-27

## Overview

This directory contains production-ready Software Development Kits (SDKs) for integrating the Ternary Moral Logic (TML) framework into applications. The SDKs provide comprehensive implementations of Sacred Zero discrimination detection, Always Memory immutable logging, environmental impact monitoring, and multi-stakeholder governance including ecosystem protection.

## Available SDKs

### 🔵 Java SDK (`/sdk/java/`)
Enterprise-grade implementation for JVM-based applications.

**Files:**
- `TMLClient.java` - Main client interface for TML operations
- `TMLConfig.java` - Configuration management with environment profiles
- `TMLException.java` - Comprehensive error handling with severity levels
- `SacredZeroTrigger.java` - Discrimination detection and prevention system
- `AlwaysMemoryLogger.java` - Immutable logging with cryptographic verification
- `Example.java` - Complete usage examples for all features

**Key Features:**
- Thread-safe operations with concurrent collections
- CompletableFuture support for async operations
- Spring Boot integration ready
- JMX monitoring capabilities
- Maven/Gradle compatible

### 🟢 Go SDK (`/sdk/go/`)
High-performance implementation for cloud-native applications.

**Files:**
- `tml_client.go` - Main client with connection pooling
- `sacred_zero.go` - Sacred Zero violation detection
- `always_memory.go` - Immutable logging with merkle trees
- `config.go` - Configuration with multiple environment presets
- `errors.go` - Structured error handling with escalation
- `example.go` - 8 comprehensive usage examples

**Key Features:**
- Goroutine-safe with channels and mutexes
- Context support for cancellation/timeouts
- Efficient batch processing
- Native cloud integration
- Minimal dependencies

### 🔴 C++ SDK (`/sdk/cpp/`)
Low-latency implementation for embedded and high-performance systems.

**Files:**
- `tml_client.h` / `tml_client.cpp` - Core client with PIMPL pattern
- `sacred_zero.h` / `sacred_zero.cpp` - Statistical bias detection
- `always_memory.h` / `always_memory.cpp` - Cryptographic logging
- `example.cpp` - Real-world usage scenarios

**Key Features:**
- Header-only options available
- RAII resource management
- Template metaprogramming for type safety
- OpenSSL integration for cryptography
- C++17 standard compliant

## Core Capabilities

All SDKs implement the complete TML specification including:

### 🛡️ Sacred Zero Protection
- Real-time discrimination detection
- Protected characteristic monitoring
- Intersectional bias analysis
- Emergency halt mechanisms
- Vulnerable population safeguards

### 📝 Always Memory Logging
- Immutable audit trails
- SHA-256 cryptographic hashing
- Merkle tree verification
- Guardian Network synchronization
- Blockchain anchoring support

### 🌍 Environmental Monitoring
- Carbon footprint calculation
- Water usage tracking
- E-waste estimation
- Renewable energy metrics
- Mitigation suggestions

### 👥 Multi-Stakeholder Governance
- Human community impact assessment
- Indigenous data sovereignty (FPIC)
- Non-human entity protection
- Future generation consideration
- Ecosystem health monitoring

### 📊 Compliance Reporting
- GDPR compliance tracking
- EU AI Act alignment
- UN Human Rights compliance
- Paris Agreement metrics
- UNDRIP requirements

## Quick Start

### Java
```java
import com.tml.sdk.*;

TMLConfig config = new TMLConfig.Builder()
    .withGuardianUrl("https://guardian.tml-network.org")
    .withDiscriminationThreshold(0.2)
    .build();

TMLClient client = new TMLClient(config);
client.connect();
```

### Go
```go
import "github.com/tml/sdk/go/tml"

config := tml.DefaultConfig()
client := tml.NewClient(config)
client.Connect()
```

### C++
```cpp
#include "tml_client.h"

auto config = std::make_shared<TML::Config>();
TML::TMLClient client(config);
client.Connect();
```

## Configuration

All SDKs support configuration through:
- Configuration files (JSON/YAML)
- Environment variables
- Programmatic API
- Default presets (Production, Development, High Security, Strict Environmental)

## Guardian Network Integration

Each SDK includes built-in support for:
- Automatic failover between Guardian nodes
- Connection pooling and retry logic
- TLS certificate validation
- Batch transmission optimization
- Real-time event streaming

## Security Features

- **Trusted Execution Environment (TEE)** support
- **Ed25519 signature verification**
- **HMAC authentication**
- **End-to-end encryption**
- **Audit mode for enhanced logging**

## Performance

Typical benchmarks (on standard cloud hardware):
- Sacred Zero evaluation: < 10ms
- Log entry creation: < 1ms
- Guardian sync: < 100ms
- Batch processing: 10,000 logs/second

## Requirements

### Java SDK
- Java 11 or higher
- Maven 3.6+ or Gradle 6+

### Go SDK
- Go 1.19 or higher
- CGO enabled for OpenSSL

### C++ SDK
- C++17 compatible compiler
- OpenSSL 1.1.1+
- zlib for compression
- JsonCpp for serialization

## Testing

Each SDK includes:
- Unit tests with >90% coverage
- Integration tests with mock Guardian
- Performance benchmarks
- Self-test diagnostics
- Simulated violation scenarios

## Documentation

- [Java SDK Documentation](https://tml.org/docs/sdk/java)
- [Go SDK Documentation](https://tml.org/docs/sdk/go)
- [C++ SDK Documentation](https://tml.org/docs/sdk/cpp)
- [API Reference](https://tml.org/api)
- [Integration Guide](https://tml.org/docs/integration)

## Support

- **GitHub**: https://github.com/FractonicMind/TernaryMoralLogic
- **Email**: sdk-support@tml-goukassian.org
- **Discord**: https://discord.gg/tml-community

## License

Licensed under the TML Public Benefit License v1.0
See LICENSE file in repository root for details.

## Contributing

Contributions welcome! Please see CONTRIBUTING.md for guidelines.
All contributions must maintain Sacred Zero compliance.

---

*"Code with conscience. Build with balance. Deploy with dignity."*
