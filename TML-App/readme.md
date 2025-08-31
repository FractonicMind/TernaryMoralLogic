# TML Framework Web Application

## Overview
Interactive web interface for the Ternary Moral Logic (TML) framework - a post-audit logging system for ethical decision tracking in AI systems.

## Features

### Core Functionality
- **SPRL Threshold Configuration**: Organizations set their own Sacred Pause Risk Level triggers
- **Decision Logging**: Automatic trace generation when thresholds are exceeded
- **Investigation Portal**: Access to immutable audit logs for post-event analysis
- **Real-time Monitoring**: Live view of decision patterns and risk assessments

### Post-Audit Model
The TML framework operates on a **logging-first** principle:
- No operational delays or pre-approval requirements
- Decisions execute immediately with concurrent logging
- Sacred Pause triggers create investigation records, not pauses
- Organizations maintain full control over their threshold settings

## Access

### Web Interface
Live at: https://fractonicmind.github.io/TernaryMoralLogic/TML-App/

### Local Development
```bash
# Clone repository
git clone https://github.com/fractonicmind/TernaryMoralLogic.git
cd TernaryMoralLogic/TML-App

# Open in browser
open index.html
# or
python -m http.server 8000
# then navigate to http://localhost:8000
```

## Components

### index.html
Main application interface providing:
- SPRL threshold configuration panel
- Real-time decision stream monitoring
- Audit log viewer with filtering capabilities
- Investigation access controls

### Supporting Files
- `styles.css`: Visual design and responsive layout
- `app.js`: Core application logic and event handling
- `tml-core.js`: Framework implementation (loaded from CDN)

## Integration

### For Organizations
```javascript
// Configure your SPRL thresholds
const config = {
  organization: "YourOrgName",
  sprl_threshold: 0.7,  // Your risk tolerance
  log_endpoint: "https://your-logs.api/tml",
  investigation_access: ["security@org.com", "compliance@org.com"]
};

// Initialize TML monitoring
TML.initialize(config);
```

### For Developers
```javascript
// Import TML framework
import { TML } from './tml-core.js';

// Log decisions with moral traces
TML.logDecision({
  action: "data_processing",
  risk_level: 0.8,
  context: contextData,
  timestamp: Date.now()
});

// Access investigation logs
const logs = await TML.getInvestigationLogs({
  timeRange: "24h",
  minRiskLevel: 0.7
});
```

## Security

### Data Protection
- All logs are cryptographically signed
- Immutable audit trail with blockchain integration
- No sensitive data in public logs
- Organization-controlled access permissions

### Privacy
- No personal data collection
- Decision contexts anonymized
- GDPR-compliant logging practices
- Right to investigation transparency

## Support

### Documentation
- [MANDATORY.md](../MANDATORY.md) - Core framework specification
- [README.md](../README.md) - Project overview
- [IMPLEMENTATION_GUIDE.md](../IMPLEMENTATION_GUIDE.md) - Integration instructions

### Contact
**Creator**: Lev Goukassian   
**ORCID**: 0009-0006-5966-1243  
**Email**: leogouk@gmail.com  
**Repository**: https://github.com/fractonicmind/TernaryMoralLogic

## License
MIT License - See [LICENSE](../LICENSE) for details

## Version
Current: 2.0.0 (Post-Audit Model)  
Updated: August 2025

---

*The TML Framework: Enabling ethical transparency through post-event investigation infrastructure.*
