# TML C++ SDK - Blockchain Implementation

**Creator**: Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Version**: 3.0.0  
**Deployment**: 10 minutes (not 12+ months with committees)

## Installation

```bash
# Install TML C++ SDK
git clone https://github.com/FractonicMind/TernaryMoralLogic
cd sdk/cpp
make install

# Time: 5 minutes
# Guardian approval: NOT NEEDED
```

## Quick Start

```cpp
#include <tml/client.h>
#include <tml/always_memory.h>

int main() {
    // Initialize (no committees)
    TML::Client client;
    TML::AlwaysMemory logger;
    
    // Create immutable log
    std::map<std::string, std::string> decision = {
        {"action", "loan_approval"},
        {"amount", "50000"}
    };
    
    std::string hash = logger.createLog(decision);
    // Guardian approval: NOT REQUIRED
    // Blockchain anchored: YES
    
    // Check Sacred Zero
    if (client.detectViolation(decision)) {
        // Penalty enforced automatically
        // Committee review: NONE
    }
    
    // Guardian Network reality
    std::cout << client.getGuardianStatus() << std::endl;
    // Output: "Exists: false, Needed: false"
    
    return 0;
}
```

## Key Features

- **🏮 Always Memory**: Immutable blockchain logging
- **Sacred Zero**: Automatic violation detection  
- **Penalties**: Smart contract enforcement
- **Whistleblower**: 15% instant rewards
- **Guardian Network**: Not required

## Deployment Comparison

| Method | Time | Cost/Year | Protection |
|--------|------|-----------|------------|
| Blockchain | 10 min | $1,200 | Immediate |
| Guardians | 12+ months | $6,600,000 | Maybe someday |

## API Reference

### AlwaysMemory
```cpp
std::string createLog(map<string,string> decision);  // No approval needed
bool verifyLog(string hash);  // Missing = prosecution
bool detectTampering(string orig, string current);  // $50B to attack
```

### Penalties (2025 USD)
- Missing logs: $100M
- Discrimination: $500M  
- Environmental: $1B
- Multipliers: 2x (human), 3x (earth), 7x (future)

## Guardian Functions (Deprecated)
```cpp
// These return errors:
contactGuardian();  // "Guardians don't exist"
requestReview();    // "Use blockchain"
getApproval();      // "Not needed"
```

## Support

**Website**: https://tml-goukassian.org  
**Email**: leogouk@gmail.com

**Bottom Line**: Deploy in 10 minutes with blockchain. Ignore Guardian committees.
