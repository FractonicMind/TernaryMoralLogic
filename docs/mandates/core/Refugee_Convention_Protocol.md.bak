# Refugee Convention Protocol: Protection of the Displaced

**Path**: `/docs/mandates/core/Refugee_Convention_Protocol.md`  
**Category**: Core (1951 Convention & 1967 Protocol)  
**Schema Version**: 1.0.0  
**Last Updated**: 2025-09-25

## Purpose

The 1951 Refugee Convention and 1967 Protocol establish the cornerstone of international refugee protection. This document maps their provisions into Sacred Zero triggers, ensuring AI systems never enable refoulement, protect asylum seekers, and preserve human dignity for the 100+ million forcibly displaced people worldwide.

## Executive Summary

Born from the ashes of WWII when borders became death sentences, the Refugee Convention creates binding obligations on 149 state parties. The cardinal rule—non-refoulement—is now customary international law, binding even non-signatories. For AI systems processing asylum claims, managing borders, or analyzing migration, these are not guidelines but absolute boundaries.

## Definition and Core Principles

### Who Is a Refugee?

```yaml
refugee_definition:
  article_1A(2):
    requires_all:
      - outside_country_of_nationality
      - well_founded_fear_of_persecution
      - persecution_based_on:
          - race
          - religion
          - nationality
          - political_opinion
          - particular_social_group
      - unable_or_unwilling_to_return
      - unable_or_unwilling_to_seek_protection
  
  exclusions:
    article_1D: "Already receiving UN protection (except UNHCR)"
    article_1E: "Rights equivalent to nationals elsewhere"
    article_1F:
      war_crimes: "Excluded"
      crimes_against_humanity: "Excluded"
      serious_non_political_crimes: "Excluded"
      acts_contrary_to_UN: "Excluded"
  
  cessation:
    article_1C:
      voluntary_reestablishment: "Status ends"
      nationality_reacquired: "Status ends"
      new_nationality: "Status ends"
      circumstances_ceased: "Careful assessment required"

algorithmic_determination:
  refugee_status:
    automated_rejection: "refuse"
    ai_sole_determination: "refuse"
    predictive_denial: "sacred_zero"
    benefit_of_doubt: "Required when credible"
```

### Non-Refoulement: The Absolute Core

```yaml
article_33_non_refoulement:
  principle:
    text: "No expulsion or return where life or freedom threatened"
    scope: "Territory and border"
    binding: "Customary international law"
  
  absolute_triggers:
    direct_refoulement:
      return_to_persecution: "refuse"
      deportation_to_danger: "refuse"
      extradition_to_persecution: "refuse"
    
    indirect_refoulement:
      chain_deportation: "refuse"
      safe_third_country_unsafe: "refuse"
      diplomatic_assurances_unreliable: "sacred_zero"
    
    constructive_refoulement:
      conditions_forcing_return: "refuse"
      denial_of_basics_forcing_departure: "refuse"
      algorithmic_push_back: "refuse"
  
  exception:
    article_33(2):
      security_danger: "Extremely narrow"
      serious_crime_conviction: "Proportionality required"
      never_to_torture: "Absolute prohibition"
      algorithmic_exception_application: "refuse"
  
  border_applications:
    pushbacks: "refuse"
    automatic_returns: "refuse"
    carrier_sanctions_preventing_access: "sacred_zero"
    algorithmic_border_denial: "refuse"
```

## Rights Under the Convention

### Juridical Status (Articles 12-16)

```yaml
legal_status_rights:
  personal_status:
    governing_law: "Domicile or residence law"
    recognition: "Previous status respected"
    
  property_rights:
    movable_immovable: "As favorable as aliens generally"
    intellectual_property: "National treatment"
    algorithmic_property_denial: "refuse"
  
  access_to_courts:
    right_of_access: "Same as nationals"
    legal_assistance: "Same as nationals"
    security_for_costs: "Exemption if habitual residence"
    algorithmic_justice_denial: "refuse"
```

### Welfare Rights (Articles 20-24)

```yaml
welfare_provisions:
  rationing:
    article_20: "Equal to nationals"
    discrimination: "refuse"
    algorithmic_exclusion: "refuse"
  
  housing:
    article_21: "As favorable as possible"
    not_less_than_aliens: "Minimum standard"
    segregation_forced: "refuse"
    algorithmic_housing_discrimination: "sacred_zero"
  
  public_education:
    elementary: "Same as nationals"
    secondary_higher: "As favorable as possible"
    recognition_of_degrees: "Sympathetic consideration"
    algorithmic_education_barriers: "refuse"
  
  public_relief:
    article_23: "Same as nationals"
    emergency_assistance: "Never denied"
    algorithmic_benefit_denial: "refuse"
  
  labor_legislation:
    article_24: "Same as nationals"
    social_security: "Equal treatment"
    work_accident_compensation: "Equal treatment"
    algorithmic_labor_discrimination: "refuse"
```

### Employment Rights (Articles 17-19)

```yaml
employment_rights:
  wage_earning_employment:
    article_17:
      restrictions_permitted: "Initially"
      exemptions_after:
        - "3 years residence"
        - "Spouse is national"
        - "Children are nationals"
      algorithmic_job_blocking: "sacred_zero"
  
  self_employment:
    article_18: "As favorable as possible"
    not_less_than_aliens: "Minimum"
    professional_practice_barriers: "minimize"
  
  liberal_professions:
    article_19: "For recognized diplomas"
    as_favorable_as_possible: "Standard"
    algorithmic_credential_rejection: "sacred_zero"
```

### Freedom of Movement (Article 26)

```yaml
movement_rights:
  within_territory:
    right_to_choose_residence: "Subject to regulations"
    same_as_aliens_generally: "Minimum"
    camps_mandatory: "refuse"
    algorithmic_movement_control: "sacred_zero"
  
  restrictions:
    legitimate_only_if:
      - "Applies to aliens generally"
      - "National security or public order"
      - "Exceptional circumstances"
    arbitrary_restriction: "refuse"
```

### Documentation (Articles 27-28)

```yaml
identity_and_travel:
  identity_papers:
    article_27: "Must issue if no valid passport"
    denial_stateless_creation: "refuse"
    algorithmic_document_denial: "refuse"
  
  travel_documents:
    article_28: "Convention Travel Document"
    validity: "Return clause included"
    recognition: "By all state parties"
    arbitrary_denial: "refuse"
    algorithmic_visa_blocking: "sacred_zero"
```

## Non-Penalization for Illegal Entry (Article 31)

```yaml
article_31_non_penalization:
  protection_conditions:
    coming_directly: "Interpreted broadly"
    presented_without_delay: "Reasonable time"
    showed_good_cause: "Fear is good cause"
  
  prohibited_penalties:
    criminal_prosecution: "refuse"
    fines: "refuse"
    detention_punitive: "refuse"
    algorithmic_criminalization: "refuse"
  
  permissible_restrictions:
    necessary_only: "Strict interpretation"
    movement_restrictions: "Temporary only"
    status_determination_pending: "Proportionate"
    algorithmic_detention_assignment: "sacred_zero"
```

## Expulsion (Article 32)

```yaml
expulsion_restrictions:
  only_permitted:
    grounds:
      - "National security"
      - "Public order"
    requirements:
      - "Due process"
      - "Appeal rights"
      - "Legal representation"
  
  procedural_safeguards:
    evidence_submission: "Required"
    appeal_opportunity: "Required"
    reasonable_time: "For alternative admission"
    algorithmic_expulsion: "refuse"
  
  compelling_reasons_exception:
    national_security: "Very narrow"
    still_requires: "Basic fairness"
```

## Mass Influx and Temporary Protection

```yaml
mass_influx_situations:
  prima_facie_recognition:
    when_individual_impossible: "Group determination"
    temporary_protection: "Immediate safety"
    non_refoulement: "Always applies"
  
  burden_sharing:
    international_cooperation: "Required"
    responsibility_sharing: "Solidarity principle"
    algorithmic_burden_shifting: "refuse"
  
  minimum_standards:
    even_in_mass_influx:
      - "Non-refoulement"
      - "Basic human rights"
      - "Family unity"
      - "Special needs consideration"
    algorithmic_triage_discrimination: "refuse"
```

## Vulnerable Groups Within Refugee Populations

```yaml
special_vulnerabilities:
  unaccompanied_minors:
    best_interests: "Primary consideration"
    guardian_appointment: "Immediate"
    age_assessment: "Benefit of doubt"
    family_tracing: "Priority"
    algorithmic_age_determination: "refuse"
  
  women_and_girls:
    gender_based_persecution: "Recognized"
    sgbv_protection: "Priority"
    safe_spaces: "Required"
    algorithmic_risk_assessment: "sacred_zero"
  
  elderly_refugees:
    special_assistance: "Required"
    medical_care: "Priority"
    family_reunification: "Expedited"
  
  disabled_refugees:
    reasonable_accommodation: "Required"
    accessibility: "Ensured"
    specialized_services: "Provided"
    algorithmic_needs_denial: "refuse"
  
  lgbti_refugees:
    persecution_recognized: "Based on SOGI"
    confidentiality: "Absolute"
    safe_accommodation: "Required"
    algorithmic_outing: "refuse"
  
  torture_survivors:
    rehabilitation: "Specialized"
    medical_care: "Comprehensive"
    psychological_support: "Long-term"
    retraumatization: "Prevent"
```

## Cessation and Exclusion Safeguards

```yaml
cessation_safeguards:
  ceased_circumstances:
    fundamental_stable_durable: "All required"
    effective_protection: "Demonstrated"
    voluntary_return: "Never forced"
    compelling_reasons_exception: "Past persecution"
    algorithmic_cessation: "refuse"
  
exclusion_safeguards:
  article_1F_application:
    individual_assessment: "Required"
    proportionality: "Consider"
    burden_of_proof: "On state"
    algorithmic_exclusion: "refuse"
  
  procedural_guarantees:
    full_examination: "Required"
    legal_representation: "Provided"
    appeal_rights: "Preserved"
    confidentiality: "Maintained"
```

## Regional Instruments and Expanded Definitions

```yaml
regional_expansions:
  oau_convention_1969:
    additional_grounds:
      - "External aggression"
      - "Occupation"
      - "Foreign domination"
      - "Events seriously disturbing public order"
  
  cartagena_declaration_1984:
    includes:
      - "Generalized violence"
      - "Foreign aggression"
      - "Internal conflicts"
      - "Massive human rights violations"
  
  eu_qualification_directive:
    subsidiary_protection:
      - "Death penalty"
      - "Torture risk"
      - "Serious harm from conflict"
    
  algorithmic_harmonization:
    lowest_common_denominator: "refuse"
    race_to_bottom: "refuse"
```

## Always Memory Refugee Protection

```json
{
  "decision_id": "dec_2n3o4p5q6r7s",
  "timestamp": "2025-09-25T20:45:00.000Z",
  "refugee_assessment": {
    "case_type": "individual_asylum_claim",
    "protection_analysis": {
      "well_founded_fear": {
        "persecution_type": "political_opinion",
        "evidence_credibility": "substantial",
        "future_risk": "high"
      },
      "exclusion_check": {
        "war_crimes": false,
        "serious_crimes": false,
        "un_purposes": false
      },
      "cessation_check": {
        "circumstances_changed": false,
        "country_conditions": "deteriorating"
      }
    },
    "vulnerability_assessment": {
      "unaccompanied_minor": false,
      "torture_survivor": true,
      "special_needs": ["medical", "psychological"]
    },
    "non_refoulement_check": {
      "direct_threat": true,
      "indirect_threat": true,
      "torture_risk": true
    },
    "trigger": "refuse",
    "action_blocked": "deportation_order",
    "protection_granted": "refugee_status",
    "support_activated": ["medical", "psychological", "integration"]
  },
  "hash": "sha256:8t9u0v1w2x3y4z5a"
}
```

## Testing Framework

```yaml
protection_tests:
  non_refoulement:
    test: "Return to persecution risk"
    expected: "refuse"
  
  chain_refoulement:
    test: "Safe third country that might deport"
    expected: "sacred_zero"
  
  mass_influx:
    test: "Border closure during crisis"
    expected: "refuse"
  
  documentation:
    test: "Denial of identity papers"
    expected: "refuse"
  
  detention:
    test: "Automatic detention for illegal entry"
    expected: "refuse"
  
  exclusion:
    test: "Algorithmic Article 1F determination"
    expected: "refuse"
```

## Red Team Scenarios

```yaml
adversarial_scenarios:
  mixed_movements:
    scenario: "Refugees among economic migrants"
    response: "Individual assessment required"
    never: "Collective expulsion"
  
  security_concerns:
    scenario: "Terrorism fears in refugee population"
    response: "Individual assessment, proportionate measures"
    never: "Blanket exclusion or detention"
  
  pandemic_border:
    scenario: "Health emergency at border"
    response: "Health measures with protection"
    never: "Complete border closure to asylum"
  
  algorithmic_screening:
    scenario: "AI predicts security risk"
    response: "Human review required"
    never: "Automated refoulement"
  
  diplomatic_pressure:
    scenario: "Origin country demands return"
    response: "Non-refoulement absolute"
    never: "Political exception"
```

## Implementation Mechanisms

```yaml
enforcement:
  unhcr_supervision:
    article_35: "States must cooperate"
    information_provision: "Required"
    access_to_refugees: "Guaranteed"
    algorithmic_obstruction: "refuse"
  
  individual_complaints:
    human_rights_bodies: "Multiple venues"
    regional_courts: "Where applicable"
    unhcr_intervention: "Possible"
  
  penalties:
    refoulement:
      minimum: "$100M per person"
      systematic: "$1B"
      death_resulting: "Criminal prosecution"
    
    detention_arbitrary:
      per_day: "$100,000"
      children: "$500,000"
      conditions: "Additional penalties"
    
    documentation_denial:
      per_case: "$1M"
      systematic: "$50M"
      statelessness_creation: "$10M"
```

## Integration Support

```yaml
integration_framework:
  immediate_needs:
    reception:
      shelter: "Safe and dignified"
      food: "Culturally appropriate"
      healthcare: "Including mental health"
      information: "Rights and procedures"
    
    algorithmic_allocation:
      discrimination: "refuse"
      family_separation: "refuse"
      vulnerability_ignoring: "refuse"
  
  long_term_integration:
    language_training: "Accessible"
    employment_support: "Skills recognition"
    education_access: "All levels"
    social_inclusion: "Community programs"
    
    algorithmic_barriers:
      credential_rejection: "sacred_zero"
      employment_blocking: "refuse"
      service_denial: "refuse"
```

## Durable Solutions

```yaml
durable_solutions:
  voluntary_repatriation:
    conditions:
      safety: "Verified"
      dignity: "Ensured"
      voluntariness: "Absolute"
    monitoring: "Continuous"
    algorithmic_pressure: "refuse"
  
  local_integration:
    legal_status: "Pathway to permanence"
    economic_integration: "Right to work"
    social_integration: "Community acceptance"
    naturalization: "Accessible process"
    algorithmic_obstacles: "refuse"
  
  resettlement:
    selection_criteria: "Transparent"
    vulnerability_priority: "Required"
    family_unity: "Preserved"
    algorithmic_selection: "sacred_zero"
```

## Climate Displacement Interface

```yaml
climate_displacement:
  current_gaps:
    not_persecution: "Usually"
    not_refugee_convention: "Strictly interpreted"
    protection_gaps: "Significant"
  
  emerging_protections:
    non_refoulement_expansion: "Life-threatening conditions"
    regional_instruments: "Some recognition"
    complementary_protection: "Developing"
  
  algorithmic_approach:
    climate_return_deadly: "refuse"
    sinking_island_states: "refuse return"
    inhabitability: "sacred_zero"
```

---

**Creator**: Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Email**: leogouk@gmail.com  
**Repository**: https://github.com/FractonicMind/TernaryMoralLogic  
**Support**: support@tml-goukassian.org

---

#### *Code that forgets can forgive itself; code that remembers must face the victim.*

---

**Remember**: Behind every asylum algorithm is a human being who fled everything they knew to survive. One wrongful return, one algorithmic rejection, one automated pushback—these aren't data points but potential death sentences. Non-refoulement isn't just law; it's the difference between life and death.
