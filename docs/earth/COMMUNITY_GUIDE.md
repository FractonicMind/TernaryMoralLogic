# Community Participation Guide: Indigenous & Local Ecological Witnesses

## Purpose

This guide enables Indigenous peoples, local communities, and ecological stewards to participate as sovereign data contributors to TML's Earth Protection system. Your knowledge triggers Sacred Zero when ecosystems face harm.

## Core Principles

### Indigenous Data Sovereignty (IDS)

Your data remains **yours**:
- You control collection, storage, and access
- You define governance protocols
- You retain ownership permanently
- TML only receives what you choose to share

### CARE Principles

- **Collective benefit**: Data serves your community first
- **Authority to control**: You decide how data is used
- **Responsibility**: Users must respect your protocols
- **Ethics**: Relationships built on trust, not extraction

## Registration Process

### Online Registration

```json
{
  "community_id": "auto-generated",
  "name": "Your community name",
  "territory": "GeoJSON boundaries or description",
  "governance": {
    "type": "consensus_council|elder_council|assembly|custom",
    "description": "How decisions are made",
    "representatives": ["Names or roles, not required"],
    "contact_protocol": "How to reach legitimate representatives"
  },
  "ecological_focus": ["watersheds", "forests", "species", "seasonal_patterns"],
  "connectivity": "online|hybrid|offline"
}
```

### Offline Registration

For communities without reliable internet:

#### Method 1: SMS Registration

Send to designated regional numbers:

```
REG COMMUNITY [name]
TERRITORY [description]
GOVERN [council type]
FOCUS [watersheds/forests/etc]
```

Receive confirmation code within 48 hours.

#### Method 2: Partner NGO

Work with verified organizations:
1. Fill paper forms (available in local languages)
2. NGO verifies and submits
3. Receive USB key with credentials
4. Updates via monthly courier

#### Method 3: Satellite Terminal

Periodic access points:
- Mobile units visit quarterly
- Government/NGO offices
- Regional universities

## Submitting Ecological Data

### What Triggers Sacred Zero

Your observations can pause AI decisions when detecting:

- Water source contamination or depletion
- Deforestation or habitat destruction
- Species population changes
- Seasonal pattern disruptions
- Sacred site disturbances
- Traditional resource degradation

### Data Format

#### Simple Format (SMS/Voice)

```
ALERT WATER
LOCATION [village/coordinates]
ISSUE [contamination/depletion/diversion]
SEVERITY [low/medium/critical]
```

#### Detailed Format

```json
{
  "observation": {
    "type": "water_depletion",
    "location": "River Name at Village",
    "gps": [optional],
    "date": "2025-09-23",
    "severity": "critical",
    "evidence": {
      "description": "River 80% below normal",
      "traditional_indicator": "Fish migration failed",
      "photo_hash": "optional",
      "witnesses": 3
    }
  },
  "governance_approval": {
    "method": "council_consensus",
    "date": "2025-09-22",
    "verification": "threshold_signature"
  }
}
```

### Offline Data Submission

#### USB Courier Protocol

1. Record observations on provided encrypted USB
2. Multiple witnesses sign with PGP keys
3. Courier collects monthly
4. Receive confirmation via next courier
5. Payments/tokens delivered same route

#### SMS Bridge

```
DATA [type] [severity]
LOC [description]
DATE [when observed]
WIT [number of witnesses]
```

System responds with:
- Confirmation code
- Next steps
- Token credit notification

## Verification Without Internet

### Community Attestation

Instead of digital signatures, use:

1. **Witness Quorum**: Minimum 3 community members
2. **Traditional Verification**: Elder or council approval
3. **Physical Tokens**: Tamper-evident seals on USB devices
4. **Voice Recording**: Oral testimony with multiple speakers

### Trust Building

Your reputation grows through:
- Consistent accurate reporting
- Following your stated governance protocol
- Collaborative verification with neighbors
- Long-term ecosystem monitoring

## Economic Participation

### Stewardship Tokens

Non-tradeable reputation points:
- Earned through verified observations
- Increase influence in Sacred Zero decisions
- Cannot be sold or transferred
- Persist across generations

### Micro-Grants

Direct payments for:
- Critical ecological alerts: $50-500
- Regular monitoring: $20-100/month
- Infrastructure support: $200-1000/year
- Emergency response: $500-5000

### Payment Methods

- **Mobile money** (M-Pesa, etc.)
- **Bank transfer** (where available)
- **NGO distribution** (cash/goods)
- **Community fund** (collective account)

## Governance Participation

### Recognition, Not Accreditation

TML recognizes your existing governance:
- No external certification required
- You define legitimate processes
- Changes updated through same channels
- Disputes resolved by your protocols

### Council Participation

Communities can nominate members for:
- Regional Sacred Zero councils
- Ecosystem-specific working groups
- Annual assembly
- Emergency response committees

## Security & Privacy

### Data Protection

- Your location data can be generalized
- Personal names are optional
- Sensitive sites can be masked
- Traditional knowledge marked confidential

### Anti-Retaliation

If reporting threatens your safety:
- Anonymous submission available
- Regional aggregation hides sources
- Legal protection fund access
- Emergency relocation support

## Technical Support

### Training Available

Free workshops covering:
- Basic data collection
- GPS and mapping tools
- Photo verification
- Secure communication
- Token management

### Languages

Materials available in:
- Major regional languages
- Indigenous languages (on request)
- Audio/visual formats
- Pictographic guides

### Help Channels

- SMS: Text HELP to regional number
- WhatsApp: Encrypted support groups
- Voice: Call centers with local languages
- In-person: Partner NGO offices

## Getting Started Checklist

- [ ] Identify community governance structure
- [ ] Choose online/hybrid/offline pathway
- [ ] Register through preferred method
- [ ] Receive confirmation and credentials
- [ ] Submit first observation
- [ ] Receive tokens and confirmation
- [ ] Join regional network

## FAQ

**Q: Do we need smartphones?**
No. SMS, voice calls, and paper forms all work.

**Q: Who sees our data?**
Only what you explicitly share. Location can be generalized, names optional.

**Q: Can our governance change?**
Yes. Update through the same channel you registered.

**Q: What if we disagree internally?**
Follow your traditional resolution process. TML doesn't intervene.

**Q: Are tokens real money?**
No, they're reputation points. Micro-grants are real money.

**Q: Can corporations buy our data?**
Never. Data sovereignty is permanent and non-transferable.

## Contact

- **Global SMS**: +1-555-TML-EARTH
- **Regional coordinators**: See appendix
- **Email**: community@tml-goukassian.org
- **Emergency**: 24/7 hotline for urgent ecological threats

---

**Remember**: Your knowledge has protected ecosystems for generations. TML simply makes that wisdom visible to machines, ensuring AI cannot ignore what you've always known.

---

**Creator**: Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Email**: leogouk@gmail.com  
**Repository**: https://github.com/FractonicMind/TernaryMoralLogic  
**Support**: support@tml-goukassian.org
