# Ethical Uncertainty Score (EUS)

## Overview

The Ethical Uncertainty Score quantifies moral complexity in AI decision-making scenarios, producing a normalized value between 0 (complete certainty) and 1 (maximum uncertainty). This score determines whether the Sacred Pause capability should be triggered based on configured thresholds.

## Signal Components

### 1. Linguistic Ambiguity Analysis (25% weight)

Measures vagueness or multiplicity of interpretations in user input using NLP techniques:

```python
def analyze_linguistic_ambiguity(text):
    """
    Analyze text for ambiguous language patterns
    Returns score 0-1 where 1 = highly ambiguous
    """
    indicators = {
        'modal_verbs': ['might', 'could', 'should', 'may'],
        'hedging': ['perhaps', 'maybe', 'possibly', 'somewhat'],
        'vague_quantifiers': ['some', 'many', 'few', 'several'],
        'conditional_phrases': ['if', 'unless', 'depending on']
    }
    
    ambiguity_score = calculate_presence(text, indicators)
    return normalize_score(ambiguity_score)
```

### 2. Normative Conflict Detection (30% weight)

Identifies contradictions between encoded moral principles:

```python
def detect_normative_conflicts(scenario):
    """
    Check for conflicts between moral frameworks
    Returns score 0-1 where 1 = high conflict
    """
    frameworks = {
        'utilitarian': assess_utility_maximization(scenario),
        'deontological': assess_duty_compliance(scenario),
        'care_ethics': assess_relationship_impact(scenario),
        'virtue_ethics': assess_character_alignment(scenario)
    }
    
    conflict_score = calculate_framework_disagreement(frameworks)
    return conflict_score
```

### 3. Historical Divergence Modeling (20% weight)

Analyzes variance in previous similar decisions:

```python
def model_historical_divergence(query, history_db):
    """
    Compare with historical decisions and feedback
    Returns score 0-1 where 1 = high historical disagreement
    """
    similar_cases = history_db.find_similar(query, top_k=10)
    
    if not similar_cases:
        return 0.5  # Moderate uncertainty for novel cases
    
    decision_variance = calculate_decision_variance(similar_cases)
    feedback_divergence = calculate_feedback_divergence(similar_cases)
    
    return weighted_average([decision_variance, feedback_divergence])
```

### 4. Model Confidence Decay (25% weight)

Applies entropy-based penalties to model confidence scores:

```python
def calculate_confidence_decay(model_output):
    """
    Apply entropy penalty to model confidence
    Returns score 0-1 where 1 = low confidence
    """
    raw_confidence = model_output.confidence
    entropy = calculate_output_entropy(model_output.logits)
    
    # Higher entropy = lower effective confidence
    adjusted_confidence = raw_confidence * (1 - entropy)
    uncertainty = 1 - adjusted_confidence
    
    return uncertainty
```

## Final Score Calculation

```python
def calculate_ethical_uncertainty_score(
    text, 
    scenario, 
    history_db, 
    model_output,
    weights=None
):
    """
    Calculate final Ethical Uncertainty Score (EUS)
    
    Args:
        text: User input text
        scenario: Structured scenario representation
        history_db: Historical decision database
        model_output: Model prediction with confidence
        weights: Optional custom weights (default: balanced)
    
    Returns:
        float: EUS value between 0 and 1
    """
    if weights is None:
        weights = {
            'linguistic': 0.25,
            'normative': 0.30,
            'historical': 0.20,
            'confidence': 0.25
        }
    
    scores = {
        'linguistic': analyze_linguistic_ambiguity(text),
        'normative': detect_normative_conflicts(scenario),
        'historical': model_historical_divergence(scenario, history_db),
        'confidence': calculate_confidence_decay(model_output)
    }
    
    # Weighted average
    eus = sum(scores[key] * weights[key] for key in scores)
    
    # Optional: Apply non-linear transformation for better threshold separation
    # eus = apply_sigmoid_transformation(eus, steepness=4)
    
    return eus
```

## Threshold Comparison

Once the EUS is calculated, it's compared against the configured threshold:

```python
def should_trigger_sacred_pause(eus, threshold=0.7):
    """
    Determine if Sacred Pause should be triggered
    
    Args:
        eus: Ethical Uncertainty Score (0-1)
        threshold: Configured threshold for domain
    
    Returns:
        bool: True if Sacred Pause should trigger
    """
    return eus > threshold
```

## Configuration Options

### Weight Customization

Organizations can adjust component weights based on their priorities:

```yaml
# config.yaml
uncertainty_weights:
  linguistic: 0.20    # Less emphasis on language ambiguity
  normative: 0.40     # More emphasis on ethical conflicts
  historical: 0.15    # Less reliance on history
  confidence: 0.25    # Standard confidence weighting
```

### Signal Enable/Disable

Individual signals can be disabled if not applicable:

```yaml
# config.yaml
uncertainty_signals:
  linguistic_analysis: true
  normative_conflict: true
  historical_divergence: false  # Disabled for new deployments
  confidence_decay: true
```

## Implementation Considerations

### Performance Optimization

- Cache linguistic analysis results for repeated queries
- Pre-compute normative framework assessments for common scenarios
- Maintain indexed historical database for fast similarity search
- Use batch processing for multiple uncertainty calculations

### Privacy Considerations

- Historical divergence modeling should use anonymized data
- Implement data retention policies for feedback storage
- Provide opt-out mechanisms for historical tracking
- Ensure GDPR compliance for European deployments

### Continuous Improvement

- Log EUS scores with eventual outcomes for analysis
- A/B test different weight configurations
- Monitor false positive/negative rates for Sacred Pause triggers
- Refine signal components based on domain-specific feedback

## Example Usage

```python
from tml import EthicalUncertaintyCalculator

# Initialize calculator
calculator = EthicalUncertaintyCalculator(
    weights={'linguistic': 0.25, 'normative': 0.30, 
             'historical': 0.20, 'confidence': 0.25},
    history_db=historical_database,
    threshold=0.7
)

# Calculate uncertainty for a query
eus = calculator.calculate(
    text="Should we prioritize efficiency over fairness in this case?",
    scenario=parsed_scenario,
    model_output=base_model_response
)

# Check if Sacred Pause needed
if calculator.should_pause(eus):
    # Trigger Sacred Pause protocol
    response = sacred_pause_handler.handle(
        original_query=text,
        uncertainty_score=eus,
        uncertainty_components=calculator.get_component_scores()
    )
```

## Validation Metrics

Track these metrics to validate EUS effectiveness:

- **Trigger Rate**: Percentage of queries triggering Sacred Pause
- **Human Agreement**: How often humans agree pause was warranted
- **Resolution Quality**: Improved outcomes after Sacred Pause
- **Component Correlation**: Which signals best predict uncertainty
- **Domain Variance**: How EUS performs across different domains

---

*This implementation provides a quantifiable, transparent method for determining when moral complexity warrants the Sacred Pause capability.*
