# Indigenous FPIC Protocol: Free, Prior, and Informed Consent

**Path**: `/docs/mandates/categorical/human_rights/Indigenous_FPIC_Protocol.md`  
**Category**: Categorical (Human Rights)  
**Schema Version**: 1.0.0  
**Last Updated**: 2025-09-26

## Purpose

Free, Prior, and Informed Consent (FPIC) is not a bureaucratic checkbox but the operationalization of Indigenous self-determination. This document establishes mandatory protocols ensuring Indigenous peoples control decisions affecting their territories, resources, cultures, and futures. Every algorithm processing Indigenous data or affecting Indigenous lands must implement these protocols absolutely.

## Executive Summary

FPIC represents the minimum standard for engagement with Indigenous peoples, grounded in centuries of resistance to colonization and decades of international law development. It means Indigenous peoples can say no—and that no means no. For AI systems, this translates to hard stops, not soft suggestions.

## Legal Foundation

```yaml
international_instruments:
  binding:
    ILO_169:
      year: 1989
      articles: [6, 7, 15, 16]
      status: "Legally binding on ratified states"
    
    treaty_rights:
      status: "Supreme law in many jurisdictions"
      interpretation: "In favor of Indigenous peoples"
  
  declaratory:
    UNDRIP:
      year: 2007
      articles: [10, 11, 19, 28, 29, 32]
      status: "Universal consensus, customary law emerging"
    
    ADRIP:
      year: 2016
      region: "Americas"
      enhancement: "Stronger than UNDRIP"
  
  jurisprudence:
    inter_american_court:
      cases: ["Awas Tingni", "Saramaka", "Kaliña and Lokono"]
      principle: "FPIC required for survival"
    
    african_commission:
      cases: ["Endorois", "Ogiek"]
      standard: "Consent for major projects"
    
    national_courts:
      recognition: "Increasing globally"
      enforcement: "Growing teeth"
```

## FPIC Components

### FREE - Without Coercion

```yaml
free_consent:
  no_coercion:
    threats:
      physical: "refuse"
      economic: "refuse"
      legal: "refuse"
      political: "refuse"
    
    pressure:
      time_pressure: "refuse"
      divide_and_conquer: "refuse"
      bribery: "refuse"
      intimidation: "refuse"
      algorithmic_manipulation: "refuse"
  
  no_conditioning:
    services_withheld:
      basic_services: "refuse"
      development_programs: "refuse"
      rights_enjoyment: "refuse"
    
    quid_pro_quo:
      consent_for_services: "refuse"
      consent_for_rights: "refuse"
      consent_for_protection: "refuse"
  
  voluntary_participation:
    opt_in:
      not_default: "Must choose to engage"
      withdrawal_right: "Anytime"
      no_penalty: "For non-participation"
    
    representation:
      self_selected: "Community chooses"
      not_imposed: "No external appointment"
      accountable: "To community"
```

### PRIOR - Before Any Action

```yaml
prior_consent:
  timing:
    before:
      project_approval: "Required"
      permits_issued: "Required"
      investments_made: "Required"
      commitments_binding: "Required"
      algorithms_deployed: "Required"
    
    sufficient_time:
      internal_consultation: "As needed"
      deliberation: "Community pace"
      consensus_building: "Traditional methods"
      no_artificial_deadlines: "refuse"
  
  stages_requiring_consent:
    initial:
      conception: "Idea stage"
      planning: "Before design"
      assessment: "Scope and methods"
    
    implementation:
      each_phase: "Separate consent"
      changes: "New consent"
      expansion: "Additional consent"
    
    ongoing:
      monitoring: "Consent to methods"
      evaluation: "Participation rights"
      closure: "Decommissioning plans"
  
  retroactive_invalid:
    past_actions:
      cannot_legitimize: "After the fact"
      requires_remedy: "For violations"
      algorithmic_fait_accompli: "refuse"
```

### INFORMED - Full Understanding

```yaml
informed_consent:
  information_requirements:
    complete:
      all_impacts: "Positive and negative"
      all_risks: "Known and potential"
      all_benefits: "Realistic assessment"
      all_alternatives: "Including no project"
      all_costs: "Hidden and visible"
    
    accessible:
      languages: "All Indigenous languages affected"
      formats: "Oral, visual, written as appropriate"
      technical_level: "Understandable"
      cultural_translation: "Concepts explained"
    
    accurate:
      evidence_based: "Not speculation"
      uncertainty_disclosed: "What's unknown"
      independent_verification: "Available"
      misleading_information: "refuse"
  
  specific_content:
    project_details:
      - nature_scope_pace
      - duration_reversibility
      - locations_areas_affected
      - personnel_involved
      - procedures_methods
    
    impact_assessments:
      environmental: "Full disclosure"
      social: "Community cohesion"
      cultural: "Tangible and intangible"
      spiritual: "Sacred sites, practices"
      economic: "Short and long term"
      health: "Individual and collective"
      cumulative: "With other projects"
    
    legal_framework:
      rights_affected: "Clearly identified"
      remedies_available: "Explained"
      dispute_resolution: "Mechanisms"
      international_standards: "Applied"
    
    data_and_IP:
      traditional_knowledge: "How protected"
      genetic_resources: "Access and benefit"
      cultural_expressions: "Use restrictions"
      data_sovereignty: "Control maintained"
      algorithmic_use: "Every application"
```

### CONSENT - Collective Decision

```yaml
consent_process:
  decision_making:
    collective:
      not_individual: "No cherry-picking"
      customary_processes: "Respected"
      consensus_methods: "Traditional"
      time_required: "As needed"
    
    representative:
      legitimate_authorities: "Traditionally chosen"
      not_imposed: "No puppet leaders"
      accountable: "To community"
      mandate_clear: "Scope defined"
    
    inclusive:
      all_affected: "Must participate"
      women: "Equal participation"
      youth: "Voice included"
      elders: "Wisdom centered"
  
  forms_of_consent:
    explicit_yes:
      clear_agreement: "Documented"
      conditions_specified: "If any"
      timeline_defined: "Duration"
      review_points: "Built in"
    
    explicit_no:
      veto_absolute: "Must be respected"
      no_override: "Ever"
      no_retaliation: "Protected"
      algorithmic_circumvention: "refuse"
    
    conditional:
      specific_requirements: "Must be met"
      monitoring: "Compliance verified"
      withdrawal: "If conditions broken"
    
    silence_is_not_consent:
      no_response: "Means no"
      absence: "Means no"
      division: "Means no"
```

## Scope of Application

### Territorial Rights

```yaml
land_and_territories:
  covered_areas:
    titled_lands:
      legal_ownership: "Absolute FPIC"
      subsurface_rights: "Included"
      airspace: "Controlled"
    
    traditional_territories:
      ancestral_domains: "Whether titled or not"
      customary_use: "Historical presence"
      seasonal_use: "Migration routes"
      sacred_sites: "Wherever located"
    
    resources:
      forests: "All uses"
      water: "Surface and ground"
      minerals: "Extraction"
      biodiversity: "Access"
      genetic: "Resources"
  
  activities_requiring_fpic:
    extractive:
      mining: "All phases"
      logging: "Commercial"
      oil_gas: "Exploration and extraction"
      water_extraction: "Large scale"
    
    infrastructure:
      dams: "Hydroelectric"
      roads: "Through territories"
      pipelines: "Any type"
      transmission_lines: "Power"
      algorithmic_infrastructure: "Data centers"
    
    conservation:
      protected_areas: "Establishment"
      carbon_projects: "REDD+"
      biodiversity: "Access agreements"
      ecosystem_services: "Payments"
    
    development:
      tourism: "In territories"
      agriculture: "Industrial"
      urbanization: "Expansion"
      digitalization: "Infrastructure"
```

### Cultural and Intellectual Property

```yaml
cultural_heritage:
  traditional_knowledge:
    medicinal:
      plants: "Use and commercialization"
      practices: "Documentation"
      formulations: "Development"
      algorithmic_analysis: "sacred_zero"
    
    ecological:
      indicators: "Climate, seasons"
      management: "Fire, water, forest"
      conservation: "Methods"
      ai_training_data: "refuse without consent"
    
    agricultural:
      seeds: "Varieties"
      techniques: "Cultivation"
      calendars: "Planting"
      breeding: "Methods"
  
  cultural_expressions:
    tangible:
      artifacts: "Repatriation"
      sites: "Access"
      remains: "Ancestors"
      
    intangible:
      songs: "Recording, use"
      stories: "Publication"
      dances: "Performance"
      ceremonies: "Documentation"
      languages: "Digital preservation"
    
    digital_sovereignty:
      data_about_peoples: "Control"
      images: "Use rights"
      recordings: "Access"
      algorithmic_representation: "Consent required"
```

### Research and Data

```yaml
research_protocols:
  academic_research:
    all_disciplines:
      social_sciences: "FPIC required"
      natural_sciences: "FPIC required"
      health: "FPIC required"
      linguistic: "FPIC required"
      algorithmic: "FPIC required"
    
    requirements:
      ethics_approval: "Plus FPIC"
      benefit_sharing: "Agreed"
      capacity_building: "Included"
      co_authorship: "Considered"
      results_return: "Guaranteed"
  
  commercial_research:
    bioprospecting:
      genetic_resources: "Access agreements"
      traditional_knowledge: "Protection"
      benefit_sharing: "Mandatory"
      patents: "Joint or prohibited"
    
    market_research:
      data_collection: "Consent"
      use_limitations: "Specified"
      commercialization: "Separate consent"
  
  data_governance:
    collection:
      purpose_specific: "Limited"
      minimization: "Only necessary"
      consent_granular: "Each use"
    
    storage:
      location: "Community controlled"
      access: "Restricted"
      security: "Maximum"
      duration: "Limited"
    
    use:
      original_purpose: "Only"
      secondary: "New consent"
      sharing: "Prohibited default"
      algorithmic: "Transparent"
    
    sovereignty:
      ownership: "Indigenous"
      control: "Complete"
      jurisdiction: "Indigenous law"
      algorithmic_sovereignty: "Recognized"
```

## Implementation Framework

### Process Requirements

```yaml
fpic_process:
  initiation:
    first_contact:
      through: "Proper channels"
      protocols: "Traditional"
      representatives: "Legitimate"
      languages: "Indigenous"
    
    preliminary_engagement:
      information_sharing: "Initial"
      relationship_building: "Time for"
      cultural_protocols: "Followed"
      good_faith: "Demonstrated"
  
  consultation_phases:
    scoping:
      what_requires_consent: "Defined"
      who_affected: "Mapped"
      how_proceed: "Agreed"
      timeline: "Flexible"
    
    information_sharing:
      multiple_rounds: "As needed"
      different_formats: "Various"
      questions_answered: "All"
      experts_available: "Independent"
    
    internal_deliberation:
      community_only: "Private"
      traditional_methods: "Used"
      time_needed: "Respected"
      no_interference: "Absolute"
    
    decision_communication:
      formal_response: "Clear"
      conditions: "If any"
      documentation: "Agreed format"
      witnesses: "If requested"
  
  documentation:
    required_records:
      process_followed: "Each step"
      information_provided: "All"
      participants: "Who involved"
      decisions_made: "Clear"
      conditions_attached: "Specific"
    
    formats:
      written: "If agreed"
      audio: "If preferred"
      video: "If chosen"
      traditional: "Recognized"
    
    custody:
      copies_to_community: "Always"
      secure_storage: "Protected"
      access_rights: "Defined"
```

### Institutional Requirements

```yaml
institutional_framework:
  corporate_obligations:
    policy:
      fpic_commitment: "Public"
      implementation_procedures: "Clear"
      accountability_mechanisms: "Defined"
      training_programs: "Regular"
    
    due_diligence:
      identify_peoples: "All affected"
      assess_impacts: "Comprehensive"
      prevent_harm: "Proactive"
      remedy_violations: "Immediate"
    
    grievance_mechanisms:
      culturally_appropriate: "Designed with"
      accessible: "Multiple channels"
      transparent: "Process clear"
      effective: "Remedies available"
  
  state_obligations:
    legislative:
      recognize_fpic: "In law"
      enforce_requirements: "Actively"
      penalize_violations: "Severely"
    
    administrative:
      agencies_trained: "All relevant"
      procedures_clear: "Published"
      monitoring_active: "Ongoing"
    
    judicial:
      access_to_courts: "Guaranteed"
      remedies_effective: "Enforced"
      precedents_protective: "Building"
```

## Remedies and Enforcement

### Violations and Consequences

```yaml
violation_types:
  absence_of_fpic:
    no_attempt: "$500M minimum (nominal to 2025)"
    fake_consultation: "$750M (nominal to 2025)"
    ignored_refusal: "$1B (nominal to 2025)"
    algorithmic_bypass: "$2B (nominal to 2025)"
  
  defective_process:
    inadequate_information: "$250M (nominal to 2025)"
    insufficient_time: "$300M (nominal to 2025)"
    wrong_representatives: "$400M (nominal to 2025)"
    coercion_used: "$1B (nominal to 2025)"
  
  breach_of_consent:
    conditions_violated: "$500M (nominal to 2025)"
    scope_exceeded: "$600M (nominal to 2025)"
    consent_withdrawn_ignored: "$1B (nominal to 2025)"
  
  cultural_violations:
    sacred_site_desecration: "$1B (nominal to 2025)"
    traditional_knowledge_theft: "$2B (nominal to 2025)"
    cultural_appropriation: "$500M (nominal to 2025)"
```

### Remedial Measures

```yaml
remedies:
  immediate:
    stop_work: "All activities"
    prevent_further_harm: "Protective measures"
    secure_sites: "From damage"
    
  restitution:
    land_return: "If taken"
    resource_restoration: "If damaged"
    cultural_items: "Repatriated"
    data_deletion: "If required"
  
  compensation:
    economic_losses: "Full"
    cultural_losses: "Assessed collectively"
    opportunity_costs: "Calculated"
    future_generations: "Considered"
  
  rehabilitation:
    environmental: "Full restoration"
    cultural: "Revitalization support"
    social: "Healing programs"
    economic: "Development support"
  
  satisfaction:
    public_acknowledgment: "Of violations"
    apology: "Formal and public"
    guarantees: "Non-repetition"
    memorial: "If requested"
  
  systemic_change:
    policy_reform: "To prevent recurrence"
    institutional_change: "Structures fixed"
    legal_reform: "If needed"
    algorithmic_redesign: "Complete overhaul"
```

## Special Considerations

### Vulnerable Contexts

```yaml
special_vulnerabilities:
  isolated_peoples:
    no_contact_policy: "Absolute"
    buffer_zones: "Protected"
    fpic_impossible: "Therefore no project"
    algorithmic_location: "refuse"
  
  recently_contacted:
    extreme_caution: "Required"
    health_protocols: "Strict"
    cultural_mediators: "Essential"
    time_extended: "Years if needed"
  
  conflict_affected:
    heightened_protection: "Required"
    security_guaranteed: "First"
    no_militarization: "Of consultations"
    safe_spaces: "For dialogue"
  
  climate_displaced:
    relocation_consent: "Required"
    cultural_continuity: "Ensured"
    territory_connection: "Maintained"
    loss_and_damage: "Compensated"
```

### Cross-Border Peoples

```yaml
transboundary:
  consultation:
    all_affected_parts: "Required"
    cross_border_coordination: "Facilitated"
    legal_harmonization: "Sought"
    
  consent:
    each_community: "Separately"
    collective_if_chosen: "Respected"
    different_decisions: "All respected"
```

## Monitoring and Compliance

```yaml
monitoring_framework:
  community_monitoring:
    rights:
      access_to_sites: "Guaranteed"
      information_access: "Complete"
      external_support: "If requested"
      report_violations: "Protected"
    
    support:
      capacity_building: "Provided"
      technical_assistance: "Available"
      financial_resources: "Adequate"
      legal_assistance: "Accessible"
  
  independent_monitoring:
    bodies:
      human_rights_institutions: "Mandate"
      UN_mechanisms: "Access"
      civil_society: "Partnership"
      academic: "Research"
    
    tools:
      indicators: "Developed with communities"
      baselines: "Established"
      regular_assessment: "Scheduled"
      public_reporting: "Transparent"
  
  algorithmic_compliance:
    automated_checks:
      fpic_verification: "Before processing"
      consent_validity: "Continuous"
      scope_compliance: "Monitored"
      violation_detection: "Immediate alert"
    
    audit_trail:
      all_interactions: "Logged"
      consent_records: "Immutable"
      decision_points: "Documented"
      violation_response: "Tracked"
```

---

**Creator**: Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Email**: leogouk@gmail.com  
**Repository**: https://github.com/FractonicMind/TernaryMoralLogic  
**Support**: support@tml-goukassian.org

---
#### *"Free, prior and informed consent is the minimum price for every inch of ancestral land."* - Lev Goukassian
---
**Remember**: FPIC is not about getting to yes. It's about respecting the no. Every algorithm that touches Indigenous data, territories, or knowledge must understand: consent is not a hurdle to overcome but sovereignty to respect.
