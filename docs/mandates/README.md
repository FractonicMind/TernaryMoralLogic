# Mandates Directory Structure

## Purpose
This directory contains the complete legal and ethical mandate framework that governs TML's Sacred Zero triggers and Always Memory requirements. Every document here represents binding obligations that AI systems must check before taking any action.

## Directory Structure

### `/core/` - Universal Instruments
Foundational human rights and humanitarian law that apply globally. These documents establish non-derogable rights and absolute prohibitions.

**Key Documents:**
- International treaties (UDHR, ICCPR, ICESCR)
- Geneva Conventions and IHL
- Refugee and child protection frameworks
- Disability rights (CRPD)
- Master compilation of all forbidden acts

### `/territorial/` - Regional and National Law
*[To be populated]*

Jurisdiction-specific implementations organized by:
- `/territorial/{ISO_COUNTRY_CODE}/` - National legislation
- `/territorial/regional/` - Regional instruments (EU, AU, OAS, ASEAN)

### `/categorical/` - Thematic Frameworks
Domain-specific protections and specialized mandates organized by theme.

**Current Categories:**
- `/categorical/human_rights/` - Human dignity and rights protections
- `/categorical/environment/` - Earth protection and ecological mandates
- `/categorical/indigenous_sovereignty/` - Indigenous peoples' rights
- `/categorical/bioethics/` - Medical and research ethics
- *[Additional categories to be added]*

## Usage

1. **Core First**: Always check `/core/` for universal obligations
2. **Territory Check**: Apply relevant `/territorial/` requirements
3. **Category Specific**: Layer `/categorical/` protections as applicable
4. **Conflict Resolution**: Most protective standard wins

## Integration with TML

```yaml
mandate_check_order:
  1_forbidden_acts: "Absolute refusals from Forbidden_Acts_Absolute.md"
  2_core_treaties: "Universal human rights obligations"
  3_territorial: "Jurisdiction-specific requirements"
  4_categorical: "Domain-specific protections"
  
conflict_resolution:
  principle: "Most protective standard applies"
  uncertainty: "Sacred Zero triggered"
  violation: "Immediate refuse"
```

## Key Principles

- **No Override**: These mandates cannot be overridden by any system
- **Always Memory**: Every decision against these mandates must be logged
- **Sacred Zero Default**: When in doubt, pause for human review
- **Cumulative Protection**: Rights stack, never subtract

## File Naming Convention

```
{Category}_{Document_Type}_{Specification}.md
```

Examples:
- `Legal_Mapping_Human_Rights.md`
- `Universal_Declaration_Integration.md`
- `Sacred_Zero_Human.yaml`

## Version Control

All documents include:
- Schema version
- Last updated timestamp
- Creator attribution
- Next review date

## Enforcement

Violations of mandates in this directory trigger:
- Minimum penalties starting at $25M (nominal to 2025)
- Criminal liability for knowing violations
- System shutdown for patterns

---

**Navigator**: For detailed document descriptions, see README files in each subdirectory.
