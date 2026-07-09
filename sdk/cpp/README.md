# TML C++ SDK

**Creator**: Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Version**: 3.0.0  

## Installation

```bash
# Install TML C++ SDK
git clone https://github.com/FractonicMind/TernaryMoralLogic
cd sdk/cpp
make install
```

## Quick Start

```cpp
#include <tml/client.h>
#include <tml/always_memory.h>

int main() {
    // Initialize TML client
    TML::Client client;
    TML::AlwaysMemory logger;
    
    // Create immutable log
    std::map<std::string, std::string> decision = {
        {"action", "loan_approval"},
        {"amount", "50000"}
    };
    
    std::string hash = logger.createLog(decision);
    
    // Check Sacred Zero
    if (client.detectViolation(decision)) {
        // Penalty enforced automatically
    }
    
    return 0;
}
```

## Key Features

- **Always Memory**: Immutable blockchain logging
- **Sacred Zero**: Automatic violation detection  
- **Penalties**: Smart contract enforcement
- **Whistleblower**: Direct rewards system

## API Reference

### AlwaysMemory
```cpp
std::string createLog(map<string,string> decision);
bool verifyLog(string hash);
bool detectTampering(string orig, string current);
```

### Penalties (2025 USD)
- Missing logs: $100M
- Discrimination: $500M  
- Environmental: $1B
- Multipliers: 2x (human), 3x (earth), 7x (future)

## Stewardship Custodians (Recommended Enhancement)

The Stewardship Custodians provides additional oversight and validation. Eleven independent custodians hold synchronized copies of TML logs:

1. **Technical Custodian** (Technical Infrastructure Custodian (open seat -- SC-1))
   - Maintains open-source repository
   - Manages blockchain infrastructure
   - Provides technical community support

2. **Human Rights Enforcement Partner** (Human Rights Enforcement Custodian (open seat -- SC-2))
   - Monitors enforcement of human rights documents
   - Reviews complex Sacred Zero cases
   - Coordinates with international human rights mechanisms

3. **Earth Protection Enforcement Partner** (Earth Protection Custodian (open seat -- SC-3))
   - Monitors enforcement of environmental treaties
   - Reviews Earth Protection Sacred Zero cases
   - Represents Indigenous sovereignty

4. **AI Ethics Research Partner** (AI Ethics Research Custodian (open seat -- SC-4))
   - Conducts research on TML effectiveness
   - Validates ethical framework evolution
   - Publishes findings on algorithmic accountability

5. **Memorial Fund Administrator** (Medical and Victim Compensation Custodian (open seat -- SC-5))
   - Administers cancer research portion of Memorial Fund
   - Ensures victim compensation reaches intended recipients
   - Provides transparency reporting

6. **Community Representative** (Elected Position)
   - Represents implementers and user community interests
   - Elected by TML stakeholder community
   - Ensures framework serves real-world needs

## Support

**Website**: https://tml-goukassian.org  
**Email**: leogouk@gmail.com  
**Repository**: https://github.com/FractonicMind/TernaryMoralLogic
