# Threshold Profiles

## Overview

Threshold profiles provide pre-configured Sacred Pause sensitivity levels optimized for different deployment domains. Organizations can use these defaults or create custom profiles based on their specific risk tolerance and operational requirements.

## Default Profiles

### Medical Ethics Mode
**Threshold: 0.3** (Low - triggers easily)

Prioritizes patient safety and thorough consideration of life-impacting decisions.

```yaml
profile: medical_ethics
threshold: 0.3
description: "High sensitivity for healthcare decisions"
characteristics:
  - Triggers on any life-affecting decisions
  - Heightened sensitivity to vulnerable populations
  - Strict compliance with medical ethics principles
  - Conservative approach to uncertainty
use_cases:
  - Treatment recommendations
  - Resource allocation
  - End-of-life decisions
  - Clinical trial enrollment
```

### Customer Service Mode
**Threshold: 0.85** (High - rarely triggers)

Optimizes for smooth interaction flow while catching significant ethical issues.

```yaml
profile: customer_service  
threshold: 0.85
description: "Low sensitivity for routine interactions"
characteristics:
  - Minimal interruption to service flow
  - Triggers only on severe ethical conflicts
  - Focuses on efficiency and user satisfaction
  - Handles routine queries without pause
use_cases:
  - Product recommendations
  - Account assistance
  - General inquiries
  - Complaint handling
```

### Financial Services Mode
**Threshold: 0.6** (Moderate)

Balances operational efficiency with fairness and regulatory compliance.

```yaml
profile: financial_services
threshold: 0.6
description: "Balanced sensitivity for financial decisions"
characteristics:
  - Moderate sensitivity to fairness issues
  - Regulatory compliance awareness
  - Fraud and bias detection
  - Transparent decision-making
use_cases:
  - Loan approvals
  - Investment recommendations
  - Risk assessment
  - Fraud detection
```

### Content Moderation Mode
**Threshold: 0.5** (Moderate)

Balances free expression with harm prevention.

```yaml
profile: content_moderation
threshold: 0.5
description: "Balanced approach to content decisions"
characteristics:
  - Cultural sensitivity awareness
  - Context-dependent evaluation
  - Nuanced handling of edge cases
  - Transparency in moderation decisions
use_cases:
  - Social media posts
  - User-generated content
  - Comment moderation
  - Community guidelines enforcement
```

### Research Mode
**Threshold: 0.7** (Moderate-High)

Encourages exploration while maintaining ethical boundaries.

```yaml
profile: research
threshold: 0.7
description: "Thoughtful approach for research applications"
characteristics:
  - Encourages thorough exploration
  - Maintains research integrity
  - Protects participant welfare
