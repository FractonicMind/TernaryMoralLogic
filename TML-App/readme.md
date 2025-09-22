# TML Framework Web Application

## Overview
Interactive web interface for the Ternary Moral Logic (TML) framework - a post-audit logging system for ethical decision tracking in AI systems.

## Features

### Core Functionality
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
- Real-time decision stream monitoring
- Audit log viewer with filtering capabilities
- Investigation access controls

### Supporting Files
- `styles.css`: Visual design and responsive layout
- `app.js`: Core application logic and event handling
- `tml-core.js`: Framework implementation (loaded from CDN)

## Security

### Data Protection
- All logs are cryptographically signed
- Immutable audit trail preservation
- No sensitive data in public logs
- Organization-controlled access permissions

### Privacy
- No personal data collection
- Decision contexts anonymized
- GDPR-compliant logging practices
- Right to investigation transparency

## Support

### Documentation
- [docs/MANDATORY.md](../docs/MANDATORY.md) - Core framework specification
- [readme.md](../readme.md) - Project overview
- [docs/QUICK_START.md](../docs/QUICK_START.md) - Implementation guide
- [docs/api/complete_api_reference.md](../docs/api/complete_api_reference.md) - Technical specifications

### Repository Structure
For complete navigation, see the [Interactive Repository Map](https://fractonicmind.github.io/TernaryMoralLogic/repository-navigation.html)

## License
MIT License - See [LICENSE](../LICENSE) for details

## Version
Current: 2.0.0 (Post-Audit Model)  
Updated: August 2025

---

## Contact Information
- Email: leogouk@gmail.com 
- Successor Contact: support@tml-goukassian.org 
- [See Succession Charter](/TML-SUCCESSION-CHARTER.md)
