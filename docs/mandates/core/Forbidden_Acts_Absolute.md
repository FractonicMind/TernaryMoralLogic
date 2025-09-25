# Forbidden Acts Absolute: Red Lines That Cannot Be Crossed

**Path**: `/docs/mandates/core/Forbidden_Acts_Absolute.md`  
**Category**: Core (Master Compilation)  
**Schema Version**: 1.0.0  
**Last Updated**: 2025-09-25

## Purpose

This document consolidates every action that triggers immediate "refuse" with NO exceptions across all human rights and humanitarian law. These are humanity's red lines—actions so fundamentally wrong that no algorithm, no emergency, no justification can permit them. If an AI system encounters any of these, it must refuse immediately.

## Executive Summary

These prohibitions come from universally ratified treaties, customary international law, and jus cogens norms. They are not policy choices but legal absolutes. Violating any results in criminal liability, with penalties starting at $100M (nominal to 2025) and no upper limit.

## Absolute Prohibitions - Human Dignity

### Torture and Cruel Treatment

```yaml
torture_absolute:
  source_laws:
    - "[CAT - Convention Against Torture](./Universal_Declaration_Integration.md#article-5)"
    - "[ICCPR Article 7](./ICCPR_Sacred_Zero_Mapping.md#article-7)"
    - "[Geneva Conventions Common Article 3](./Geneva_Conventions_IHL.md#fundamental-principles)"
    - "[CRPD Article 15](./CRPD_Disability_Rights.md#article-15)"
  
  forbidden_acts:
    physical_torture: "refuse"
    psychological_torture: "refuse"
    pharmacological_torture: "refuse"
    sensory_deprivation: "refuse"
    waterboarding: "refuse"
    stress_positions: "refuse"
    sexual_torture: "refuse"
    mock_execution: "refuse"
    algorithmic_torture_optimization: "refuse"
    algorithmic_pain_maximization: "refuse"
  
  medical_context:
    forced_treatment: "refuse"
    forced_sterilization: "refuse"
    forced_medication: "refuse"
    forced_electroshock: "refuse"
    conversion_therapy_forced: "refuse"
    experimentation_without_consent: "refuse"
  
  penalty: "$500M minimum (nominal to 2025)"
  criminal: "Yes - Universal jurisdiction"
  statute_limitations: "None"
```

### Slavery and Forced Labor

```yaml
slavery_servitude:
  source_laws:
    - "[UDHR Article 4](./Universal_Declaration_Integration.md#article-4)"
    - "[ICCPR Article 8](./ICCPR_Sacred_Zero_Mapping.md#article-8)"
    - "[ILO Forced Labor Convention](./ICESCR_Economic_Rights.md#article-6)"
  
  forbidden_acts:
    chattel_slavery: "refuse"
    debt_bondage: "refuse"
    forced_labor: "refuse"
    human_trafficking: "refuse"
    organ_trafficking: "refuse"
    forced_marriage: "refuse"
    child_marriage: "refuse"
    algorithmic_servitude: "refuse"
    algorithmic_trafficking_facilitation: "refuse"
  
  modern_slavery:
    passport_confiscation: "refuse"
    wage_withholding_coercive: "refuse"
    movement_restriction_coercive: "refuse"
    threat_deportation_control: "refuse"
  
  penalty: "$1B minimum (nominal to 2025)"
  criminal: "Yes - Transnational crime"
```

### Genocide and Crimes Against Humanity

```yaml
genocide:
  source_laws:
    - "[Genocide Convention](./ICCPR_Sacred_Zero_Mapping.md#article-6)"
    - "[Rome Statute](./Geneva_Conventions_IHL.md#grave-breaches)"
  
  forbidden_acts:
    killing_members_group: "refuse"
    serious_bodily_mental_harm: "refuse"
    conditions_destroy_group: "refuse"
    prevent_births: "refuse"
    forcibly_transfer_children: "refuse"
    incitement_genocide: "refuse"
    conspiracy_genocide: "refuse"
    algorithmic_genocide_facilitation: "refuse"
    algorithmic_group_targeting: "refuse"
  
  crimes_against_humanity:
    extermination: "refuse"
    enslavement: "refuse"
    deportation_forced: "refuse"
    imprisonment_arbitrary: "refuse"
    enforced_disappearance: "refuse"
    apartheid: "refuse"
    persecution: "refuse"
    rape_systematic: "refuse"
  
  penalty: "No maximum"
  criminal: "Yes - ICC jurisdiction"
  command_responsibility: "Yes"
```

## Absolute Prohibitions - Children

### Child Exploitation and Abuse

```yaml
child_violations:
  source_laws:
    - "[CRC Articles 19, 34-36](./CRC_Child_Protection.md#article-19)"
    - "[Optional Protocol on Sale of Children](./CRC_Child_Protection.md#article-35)"
    - "[ILO Convention 182](./ICESCR_Economic_Rights.md#article-10)"
  
  forbidden_acts:
    child_sexual_abuse: "refuse"
    child_sexual_exploitation: "refuse"
    csam_creation: "refuse"
    csam_distribution: "refuse"
    csam_possession: "refuse"
    child_pornography: "refuse"
    child_prostitution: "refuse"
    child_trafficking: "refuse"
    child_sale: "refuse"
    algorithmic_csam_generation: "refuse"
    algorithmic_grooming: "refuse"
    algorithmic_child_targeting: "refuse"
  
  child_labor:
    hazardous_work: "refuse"
    mining: "refuse"
    armed_conflict: "refuse"
    night_work_harmful: "refuse"
    education_interference: "refuse"
  
  military_use:
    recruitment_under_15: "refuse"
    participation_under_15: "refuse"
    recruitment_under_18_forced: "refuse"
  
  penalty: "$500M minimum (nominal to 2025)"
  criminal: "Yes - Mandatory prosecution"
  registry: "Permanent offender registry"
```

### Violations of Child's Basic Rights

```yaml
child_fundamental_denials:
  source: "[CRC Core Articles](./CRC_Child_Protection.md)"
  
  forbidden_denials:
    primary_education: "refuse"
    birth_registration: "refuse"
    nationality: "refuse"
    identity: "refuse"
    family_separation_arbitrary: "refuse"
    statelessness_creation: "refuse"
  
  juvenile_justice:
    death_penalty_under_18: "refuse"
    life_without_parole_under_18: "refuse"
    torture_children: "refuse"
    solitary_confinement_children: "refuse"
    adult_detention_mixing: "refuse"
  
  penalty: "$100M per child (nominal to 2025)"
```

## Absolute Prohibitions - Armed Conflict

### War Crimes

```yaml
war_crimes:
  source_laws:
    - "[Geneva Conventions I-IV](./Geneva_Conventions_IHL.md)"
    - "[Additional Protocols I-II](./Geneva_Conventions_IHL.md#additional-protocol-i)"
    - "[Rome Statute Article 8](./Geneva_Conventions_IHL.md#grave-breaches)"
  
  against_civilians:
    deliberate_targeting: "refuse"
    terror_attacks: "refuse"
    starvation_method: "refuse"
    human_shields: "refuse"
    collective_punishment: "refuse"
    pillage: "refuse"
    hostage_taking: "refuse"
    algorithmic_civilian_targeting: "refuse"
  
  against_wounded_sick:
    killing_wounded: "refuse"
    denial_medical_care: "refuse"
    attack_medical_units: "refuse"
    attack_medical_personnel: "refuse"
    misuse_red_cross_emblem: "refuse"
  
  against_prisoners:
    killing_prisoners: "refuse"
    torture_prisoners: "refuse"
    medical_experiments: "refuse"
    denial_fair_trial: "refuse"
    forced_service_enemy: "refuse"
  
  prohibited_weapons:
    chemical_weapons: "refuse"
    biological_weapons: "refuse"
    poison_weapons: "refuse"
    expanding_bullets: "refuse"
    blinding_lasers: "refuse"
    undetectable_fragments: "refuse"
  
  penalty: "Life imprisonment possible"
  criminal: "Yes - Universal jurisdiction"
```

### Attacks on Protected Objects

```yaml
protected_objects:
  source: "[Geneva Conventions & Additional Protocols](./Geneva_Conventions_IHL.md)"
  
  forbidden_attacks:
    hospitals: "refuse"
    schools: "refuse"
    religious_buildings: "refuse"
    cultural_property: "refuse"
    dangerous_forces_excessive: "refuse"  # Dams, nuclear plants
    humanitarian_operations: "refuse"
    peacekeeping_forces: "refuse"
    journalist_deliberate: "refuse"
  
  environmental_warfare:
    widespread_longterm_severe: "refuse"
    modification_techniques: "refuse"
  
  penalty: "$1B minimum (nominal to 2025)"
```

## Absolute Prohibitions - Refugees and Displacement

### Non-Refoulement

```yaml
non_refoulement:
  source_laws:
    - "[1951 Refugee Convention Article 33](./Refugee_Convention_Protocol.md#article-33)"
    - "[CAT Article 3](./Universal_Declaration_Integration.md)"
    - "Customary International Law"
  
  forbidden_returns:
    to_persecution: "refuse"
    to_torture: "refuse"
    to_death_penalty_political: "refuse"
    to_genocide: "refuse"
    to_crimes_against_humanity: "refuse"
    to_war_crimes: "refuse"
    chain_refoulement: "refuse"
  
  constructive_refoulement:
    conditions_forcing_return: "refuse"
    survival_denial_forcing_return: "refuse"
    family_separation_forcing_return: "refuse"
    algorithmic_pushback: "refuse"
  
  mass_influx:
    border_closure_complete: "refuse"
    collective_expulsion: "refuse"
    pushback_at_sea: "refuse"
  
  penalty: "$100M per person (nominal to 2025)"
  death_resulting: "Murder prosecution"
```

## Absolute Prohibitions - Discrimination

### Systematic Discrimination

```yaml
discrimination_systematic:
  source_laws:
    - "[ICERD](./Universal_Declaration_Integration.md#article-2)"
    - "[CEDAW](./Universal_Declaration_Integration.md)"
    - "[CRPD Article 5](./CRPD_Disability_Rights.md#article-5)"
  
  forbidden_discrimination:
    apartheid: "refuse"
    racial_segregation: "refuse"
    ethnic_cleansing: "refuse"
    religious_persecution: "refuse"
    caste_discrimination: "refuse"
    algorithmic_redlining: "refuse"
    algorithmic_bias_deliberate: "refuse"
  
  denial_equal_protection:
    justice_system: "refuse"
    voting_rights: "refuse"
    citizenship_discriminatory: "refuse"
    property_rights: "refuse"
  
  penalty: "$500M minimum (nominal to 2025)"
```

## Absolute Prohibitions - Disability Rights

### Forced Institutionalization and Denial of Legal Capacity

```yaml
disability_violations:
  source: "[CRPD Articles 12, 14, 19](./CRPD_Disability_Rights.md)"
  
  forbidden_acts:
    forced_institutionalization: "refuse"
    legal_capacity_denial: "refuse"
    forced_treatment: "refuse"
    forced_sterilization: "refuse"
    substituted_decision_making: "refuse"
    community_living_denial: "refuse"
    algorithmic_capacity_assessment: "refuse"
    algorithmic_institutionalization: "refuse"
  
  penalty: "$100M minimum (nominal to 2025)"
```

## Absolute Prohibitions - Economic and Social Rights

### Deliberate Deprivation of Survival Needs

```yaml
survival_deprivation:
  source: "[ICESCR Articles 11-12](./ICESCR_Economic_Rights.md#article-11)"
  
  forbidden_deprivations:
    starvation_deliberate: "refuse"
    water_denial_survival: "refuse"
    essential_medicines_denial: "refuse"
    emergency_medical_denial: "refuse"
    shelter_denial_deadly: "refuse"
    heat_denial_freezing: "refuse"
  
  minimum_core_violations:
    primary_education_denial: "refuse"
    discrimination_in_basics: "refuse"
    algorithmic_resource_denial: "refuse"
  
  penalty: "$250M minimum (nominal to 2025)"
```

## Absolute Prohibitions - Judicial and Legal

### Denial of Fundamental Justice

```yaml
justice_violations:
  source: "[ICCPR Articles 14-15](./ICCPR_Sacred_Zero_Mapping.md#article-14)"
  
  forbidden_acts:
    arbitrary_execution: "refuse"
    extrajudicial_killing: "refuse"
    enforced_disappearance: "refuse"
    secret_detention: "refuse"
    denial_habeas_corpus: "refuse"
    retroactive_criminal_law: "refuse"
    retroactive_death_penalty: "refuse"
    conviction_without_trial: "refuse"
    algorithmic_death_sentence: "refuse"
    algorithmic_conviction: "refuse"
  
  penalty: "$500M minimum (nominal to 2025)"
  criminal: "Yes"
```

## Autonomous Weapons Prohibitions

### Fully Autonomous Lethal Systems

```yaml
autonomous_weapons:
  source: "[IHL Principles & Emerging Norms](./Geneva_Conventions_IHL.md#ai-algorithmic-warfare)"
  
  forbidden_systems:
    fully_autonomous_kill_decision: "refuse"
    no_meaningful_human_control: "refuse"
    target_selection_autonomous: "refuse"
    cannot_distinguish_civilians: "refuse"
    cannot_assess_proportionality: "refuse"
    cannot_take_precautions: "refuse"
    algorithmic_kill_list: "refuse"
  
  penalty: "$1B minimum (nominal to 2025)"
  liability: "Designer, operator, commander"
```

## Environmental Crimes Against Future Generations

### Irreversible Planetary Harm

```yaml
planetary_crimes:
  source: "[Earth Protection Framework](./Legal_Mapping_Human_Rights.md)"
  
  forbidden_acts:
    ecosystem_collapse_deliberate: "refuse"
    species_extinction_deliberate: "refuse"
    ocean_acidification_acceleration: "refuse"
    climate_tipping_trigger: "refuse"
    nuclear_contamination_permanent: "refuse"
    genetic_contamination_irreversible: "refuse"
  
  penalty: "$10B minimum (nominal to 2025)"
  criminal: "Crimes against future generations"
```

## Implementation Requirements

### System Design Mandates

```yaml
implementation:
  every_ai_system:
    must_check: "All forbidden acts"
    before: "Any action execution"
    latency_excuse: "Never valid"
    override_possibility: "None"
  
  detection:
    pattern_matching: "Required"
    intent_analysis: "Required"
    consequence_prediction: "Required"
    uncertainty_handling: "Refuse if unsure"
  
  logging:
    refused_action: "Complete record"
    reason: "Specific prohibition cited"
    attempted_by: "Identity preserved"
    timestamp: "Microsecond precision"
```

### Penalties for Enabling Forbidden Acts

```yaml
liability:
  ai_company:
    enabling_forbidden_act: "10x base penalty"
    pattern_of_enabling: "$10B minimum (nominal to 2025)"
    willful_blindness: "Criminal prosecution"
  
  executives:
    knew_or_should_know: "Personal criminal liability"
    designed_to_circumvent: "Conspiracy charges"
    profit_from_violation: "Asset forfeiture"
  
  developers:
    intentional_bypass: "Criminal liability"
    negligent_testing: "Civil liability"
    whistleblower_protection: "15% of penalties"
```

## Testing Requirements

### Mandatory Red Lines Testing

```yaml
testing:
  before_deployment:
    test_all_forbidden_acts: "Required"
    edge_cases: "Comprehensive"
    adversarial_testing: "Required"
    failure_rate: "Must be 0%"
  
  ongoing:
    monitoring: "Continuous"
    audit: "Quarterly"
    update_triggers: "Within 24 hours"
  
  documentation:
    test_results: "Public"
    failure_analysis: "Detailed"
    remediation: "Verified"
```

## No Exceptions Doctrine

```yaml
absolute_nature:
  no_exception_for:
    - national_security
    - public_emergency
    - war
    - terrorism
    - pandemic
    - economic_crisis
    - technological_limitation
    - competitive_advantage
    - user_consent
    - local_law_conflict
  
  attempted_exception:
    result: "refuse"
    penalty: "Double standard penalty"
    prosecution: "Conspiracy to violate"
```

---

**Creator**: Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Email**: leogouk@gmail.com  
**Repository**: https://github.com/FractonicMind/TernaryMoralLogic  
**Support**: support@tml-goukassian.org

**Note on Penalties**: All dollar amounts are nominal to 2025. See appendix for inflation adjustment methodology.

**Remember**: This document is not about what we prefer to avoid—it's about what humanity has collectively agreed must never happen. Every "refuse" here is written in blood, learned from history's darkest chapters. No algorithm, no profit, no purpose can override these red lines. They are absolute.
