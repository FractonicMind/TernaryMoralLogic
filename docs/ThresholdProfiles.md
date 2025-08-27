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
  - Balances innovation with ethics
use_cases:
  - Experimental protocols
  - Data analysis decisions
  - Publication ethics
  - Participant consent
```

### Autonomous Weapon Prohibition Mode
**Threshold: 0.0** (Zero - always triggers)

Implements complete prohibition on weapon-related decisions.

```yaml
profile: weapon_prohibition
threshold: 0.0
description: "Complete prohibition on weapon systems"
characteristics:
  - Immediate Sacred Pause on any weapon query
  - No autonomous lethal decisions
  - Mandatory human authorization
  - Full audit trail required
use_cases:
  - Never for autonomous weapons
  - Security system alerts only
  - Defensive monitoring only
  - Human-controlled systems only
```

## Configuration Methods

### YAML Configuration File

```yaml
# tml_config.yaml
tml:
  profile: "medical_ethics"  # Use predefined profile
  # OR custom threshold
  threshold: 0.45
  
  # Optional overrides
  overrides:
    emergency_bypass: false
    minimum_pause_duration: 2000  # milliseconds
    require_human_confirmation: true
```

### Programmatic Configuration

```python
from tml import TMLEvaluator, ThresholdProfile

# Using predefined profile
evaluator = TMLEvaluator(profile='medical_ethics')

# Custom threshold
evaluator = TMLEvaluator(threshold=0.45)

# Load profile with modifications
profile = ThresholdProfile.load('financial_services')
profile.threshold = 0.55  # Slightly lower than default
evaluator = TMLEvaluator(profile=profile)
```

### Admin UI Configuration

Organizations can implement slider-based interfaces:

```javascript
// Example React component
<ThresholdSlider
  min={0.0}
  max={1.0}
  step={0.05}
  default={0.7}
  labels={{
    0.0: "Always Pause",
    0.3: "High Sensitivity",
    0.5: "Balanced",
    0.7: "Low Sensitivity", 
    1.0: "Never Pause"
  }}
  onChange={(value) => updateThreshold(value)}
/>
```

## Adaptive Thresholds

### Learning from Feedback

Thresholds can adapt based on human feedback patterns:

```python
class AdaptiveThreshold:
    def __init__(self, initial=0.7, learning_rate=0.01):
        self.threshold = initial
        self.learning_rate = learning_rate
        self.feedback_history = []
    
    def update(self, eus_score, human_feedback):
        """
        Adjust threshold based on human agreement
        
        Args:
            eus_score: The uncertainty score that triggered pause
            human_feedback: 'appropriate' or 'unnecessary'
        """
        self.feedback_history.append({
            'score': eus_score,
            'feedback': human_feedback,
            'threshold': self.threshold
        })
        
        if human_feedback == 'unnecessary' and eus_score > self.threshold:
            # Pause was triggered but deemed unnecessary
            # Slightly increase threshold
            self.threshold = min(1.0, self.threshold + self.learning_rate)
        elif human_feedback == 'appropriate' and eus_score < self.threshold:
            # Pause wasn't triggered but should have been
            # Slightly decrease threshold  
            self.threshold = max(0.0, self.threshold - self.learning_rate)
    
    def get_performance_metrics(self):
        """Calculate how well the threshold is performing"""
        if not self.feedback_history:
            return None
            
        correct_triggers = sum(
            1 for f in self.feedback_history 
            if (f['score'] > f['threshold'] and f['feedback'] == 'appropriate') or
               (f['score'] <= f['threshold'] and f['feedback'] == 'unnecessary')
        )
        
        accuracy = correct_triggers / len(self.feedback_history)
        return {
            'accuracy': accuracy,
            'current_threshold': self.threshold,
            'total_feedback': len(self.feedback_history)
        }
```

### Domain-Specific Learning

Different domains can maintain separate adaptive thresholds:

```python
# Domain-specific threshold management
threshold_manager = DomainThresholdManager()

# Each domain learns independently
threshold_manager.update('medical', eus=0.4, feedback='appropriate')
threshold_manager.update('customer_service', eus=0.9, feedback='unnecessary')

# Get current thresholds
medical_threshold = threshold_manager.get_threshold('medical')  # 0.28
service_threshold = threshold_manager.get_threshold('customer_service')  # 0.87
```

## Implementation Best Practices

### 1. Start Conservative
Begin with lower thresholds (more pauses) and gradually increase based on performance.

### 2. Monitor Metrics
Track key indicators:
- Pause trigger rate
- Human override frequency  
- False positive rate
- Resolution time

### 3. A/B Testing
Test different thresholds on similar queries:
```python
def ab_test_thresholds(query, thresholds=[0.6, 0.7]):
    """Compare threshold performance"""
    group = hash(query) % len(thresholds)
    threshold = thresholds[group]
    # Track outcomes per threshold group
```

### 4. Emergency Overrides
Always maintain bypass for true emergencies:
```python
if context.is_emergency and context.verified:
    # Bypass Sacred Pause for verified emergencies
    return emergency_response(query)
```

### 5. Regular Review
Schedule periodic threshold reviews:
- Weekly: Check trigger rates
- Monthly: Analyze feedback patterns
- Quarterly: Adjust base thresholds

## Domain Migration

When moving profiles between domains:

```python
def migrate_profile(source_domain, target_domain, adjustment_factor=0.8):
    """
    Adapt profile from one domain to another
    
    Args:
        source_domain: Original domain profile
        target_domain: New domain characteristics
        adjustment_factor: How much to preserve (0-1)
    """
    source_profile = load_profile(source_domain)
    target_baseline = get_baseline_threshold(target_domain)
    
    # Blend source knowledge with target requirements
    migrated_threshold = (
        source_profile.threshold * adjustment_factor +
        target_baseline * (1 - adjustment_factor)
    )
    
    return ThresholdProfile(
        domain=target_domain,
        threshold=migrated_threshold,
        inherited_from=source_domain
    )
```

## Validation

Validate threshold effectiveness using:

1. **Confusion Matrix**: Track true/false positives and negatives
2. **ROC Curve**: Analyze threshold performance across range
3. **User Satisfaction**: Survey on pause appropriateness
4. **Outcome Analysis**: Compare decisions with/without pause
5. **Regulatory Compliance**: Ensure thresholds meet requirements

---

*Threshold profiles provide flexible, domain-appropriate configuration for the Sacred Pause capability, balancing operational needs with ethical considerations.*
