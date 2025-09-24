# Scientific Advisory Council Charter

## Purpose

The Scientific Advisory Council provides independent, evidence-based validation of ecological baselines used in TML's Earth Protection framework. The Council ensures Sacred Zero triggers reflect current scientific consensus, not political or commercial interests.

## Composition

### Council Structure

```yaml
total_members: 15
distribution:
  climate_science: 3
  biodiversity/ecology: 3
  water_resources: 2
  soil/agriculture: 2
  ocean_systems: 2
  atmospheric_chemistry: 1
  indigenous_knowledge: 2  # Traditional Ecological Knowledge holders

term_limits:
  standard_term: 4_years
  maximum_consecutive: 2_terms
  mandatory_gap: 4_years
  staggered_rotation: 25%_annually
```

### Expertise Requirements

**Mandatory Qualifications:**
- Published peer-reviewed research in relevant field
- 10+ years specialized experience
- No fossil fuel industry funding (past 5 years)
- No conviction for scientific misconduct
- Commitment to open science principles

**Preferred Attributes:**
- IPCC or equivalent international body experience
- Cross-disciplinary research background
- Global South representation
- Indigenous knowledge systems expertise
- Early career researchers (minimum 2 seats)

## Selection Process

### Nomination Sources

```yaml
nomination_pathways:
  scientific_societies: 40%
  guardian_institutions: 30%
  community_networks: 20%
  self_nomination: 10%

vetting_process:
  - publication_review
  - conflict_of_interest_disclosure
  - peer_references (5_required)
  - public_comment_period (30_days)
  - guardian_vote (8/11_required)
```

### Diversity Requirements

- Geographic: All continents represented
- Gender: Minimum 40% any gender
- Career stage: At least 2 early-career scientists
- Institutional: Maximum 2 from same institution
- Disciplinary: No more than 4 from same field

## Core Responsibilities

### 1. Baseline Validation

**Monthly Tasks:**
- Review treaty updates for scientific accuracy
- Validate new IPCC/IUCN assessments
- Verify regional regulation changes
- Certify ecological thresholds

**Quarterly Reviews:**
- Comprehensive baseline audit
- Emerging threat assessment
- Threshold adjustment recommendations
- Cross-source conflict resolution

### 2. Trigger Calibration

```python
def calibrate_triggers():
    """
    Council reviews and adjusts Sacred Zero triggers
    based on latest scientific evidence
    """
    review_items = {
        "carbon_budgets": "Annual update per IPCC",
        "tipping_points": "Quarterly risk assessment",
        "biodiversity_thresholds": "IUCN Red List updates",
        "water_stress": "Regional basin analysis",
        "pollution_limits": "WHO/EPA guidelines"
    }
    
    for item in review_items:
        current_threshold = get_current_trigger(item)
        scientific_consensus = council_assessment(item)
        
        if divergence > 10%:
            recommend_adjustment()
            require_supermajority(10/15)
```

### 3. Dispute Resolution

**Scientific Conflicts Protocol:**

1. **Data Source Conflicts**
   - Identify divergent sources
   - Weight by methodology rigor
   - Apply precautionary principle
   - Document uncertainty ranges

2. **Regional vs Global**
   - Local data prioritized for local impacts
   - Global models for systemic risks
   - Synthesis approach when possible
   - Transparency about limitations

3. **Traditional vs Western Science**
   - Equal initial weighting
   - Complementary validation sought
   - Long-term observation valued
   - Both perspectives documented

## Independence Safeguards

### Funding Independence

```yaml
funding_sources:
  memorial_fund: 60%
  guardian_institutions: 30%
  research_grants: 10%  # Pre-approved sources only

prohibited_funding:
  - Fossil fuel companies
  - Industrial agriculture
  - Mining corporations
  - Conflicted governments

financial_disclosure:
  frequency: annual
  public_access: yes
  audit_requirement: external
```

### Decision Autonomy

- No veto power by Guardian Network
- Recommendations implemented unless 10/11 Guardians object
- Direct communication channel to public
- Whistleblower protections for members

### Conflict of Interest

**Mandatory Recusal:**
- Financial interest in affected industry
- Prior employment (5 years)
- Family members with conflicts
- Active litigation involvement

**Disclosure Requirements:**
- All funding sources (personal and institutional)
- Consulting arrangements
- Board memberships
- Stock holdings over $10,000*

*All amounts are nominal to 2025 USD

## Integration with TML

### Oracle Network Validation

```python
def validate_oracle_data(source, data):
    """
    Council provides scientific validation 
    for oracle network data
    """
    if source.tier == "GLOBAL_TREATY":
        return council.verify_scientific_basis(data)
    
    if source.tier == "COMMUNITY":
        return council.validate_observation_methodology(data)
    
    if conflict_detected(data):
        return council.resolve_with_evidence(data)
```

### Sacred Zero Oversight

**Council Authority:**
- Recommend new triggers
- Adjust existing thresholds
- Validate community observations
- Certify emergency overrides

**Council Limitations:**
- Cannot remove protections
- Cannot weaken thresholds unilaterally
- Must document all decisions
- Subject to transparency requirements

## Working Groups

### Standing Committees

```yaml
climate_systems:
  members: 5
  focus: "Carbon budgets, temperature targets, tipping points"
  meeting_frequency: biweekly

biodiversity_integrity:
  members: 5
  focus: "Species protection, habitat thresholds, ecosystem services"
  meeting_frequency: biweekly

pollution_thresholds:
  members: 3
  focus: "Air, water, soil contamination limits"
  meeting_frequency: monthly

indigenous_knowledge:
  members: 2
  focus: "Traditional indicators, community observations"
  meeting_frequency: continuous
```

### Ad Hoc Groups

Formed for:
- Emerging threats (novel chemicals, technologies)
- Regional crises (ecosystem collapse events)
- Technological assessment (geoengineering, GMOs)
- Rapid response (< 72 hours formation)

## Decision Making

### Voting Thresholds

```yaml
standard_decisions: 8/15  # Simple majority
threshold_adjustments: 10/15  # Supermajority
emergency_declarations: 5/15  # Rapid response
trigger_removal: 13/15  # Near consensus
```

### Minority Reports

- Any 3 members can file dissent
- Published alongside majority decision
- Equal visibility in Always Memory
- Triggers review if evidence emerges

## Transparency Requirements

### Public Disclosure

**Published Monthly:**
- Meeting minutes (non-confidential)
- Threshold adjustments
- Data source validations
- Conflict resolutions

**Published Annually:**
- Complete member disclosures
- Funding sources and amounts
- Decision statistics
- Accuracy assessments

### Always Memory Integration

Every Council decision logged:

```json
{
  "council_action": "threshold_adjustment",
  "scientific_basis": ["peer_reviewed_studies"],
  "vote_count": {"for": 10, "against": 3, "abstain": 2},
  "minority_report": "link_to_dissent",
  "uncertainty_range": "±15%",
  "implementation_date": "2025-10-01",
  "review_schedule": "quarterly"
}
```

## Performance Metrics

### Accuracy Tracking

- Prediction accuracy rate: >85% target
- False positive rate: <10% for triggers
- Response time to threats: <72 hours
- Consensus achievement: >70% decisions

### Annual Review

Council performance evaluated on:
- Scientific rigor of decisions
- Timeliness of threat detection
- Integration of diverse knowledge
- Transparency compliance
- Stakeholder confidence

## Succession Planning

### Knowledge Transfer

- 1-year overlap for rotating members
- Mentorship program for new members
- Document repository maintained
- Institutional memory preserved

### Emergency Succession

If member cannot continue:
1. Temporary appointment by working group
2. Full selection process within 90 days
3. Guardian confirmation required
4. Term continues from predecessor

## Budget

```yaml
annual_budget: $3M*
distribution:
  member_stipends: 40%  # $800K
  research_support: 25%  # $500K
  meetings/travel: 15%  # $300K
  technical_infrastructure: 10%  # $200K
  public_engagement: 5%  # $100K
  reserve: 5%  # $100K

*All amounts are nominal to 2025 USD
```

## Appeals Process

### Scientific Challenges

Any party can challenge Council decisions with:
- New peer-reviewed evidence
- Methodological errors identified
- Conflict of interest discovered
- Traditional knowledge overlooked

### Review Mechanism

1. Initial review by working group (14 days)
2. Full Council consideration (30 days)
3. External peer review if needed (60 days)
4. Final determination published

## Charter Amendments

- Proposed by any 5 Council members
- Public comment period: 60 days
- Guardian review required
- 12/15 Council vote to adopt
- Annual review mandatory

---

**Founding Principle**: Science in service of Earth, not profit. Evidence in service of protection, not exploitation.

---

**Document Version**: 1.0  
**Charter Established**: September 2025  
**Next Review**: September 2026

**Creator**: Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Repository**: https://github.com/FractonicMind/TernaryMoralLogic
