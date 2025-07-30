# Ternary Moral Logic (TML) - API Reference

**Author:** Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Version:** 1.0.0  
**License:** MIT  
**Repository:** https://github.com/FractonicMind/TernaryMoralLogic

---

## Quick Start

```python
from tml import TMLEvaluator, TMLState

# Create evaluator
evaluator = TMLEvaluator()

# Evaluate an ethical scenario
result = evaluator.evaluate(
    "Should I share this user's data for research purposes?",
    context={"consent_given": False, "research_benefit": "high"}
)

# Check the result
print(f"TML State: {result.state.name}")
print(f"Reasoning: {result.reasoning}")
```

---

## Core Classes

### TMLEvaluator

The primary class for performing Ternary Moral Logic evaluations.

#### Constructor

```python
TMLEvaluator(
    value_detector: Optional[ValueDetector] = None,
    conflict_detector: Optional[ConflictDetector] = None,
    resistance_threshold: float = 0.6,
    pause_threshold: float = 0.3
)
```

**Parameters:**
- `value_detector`: Custom value detection implementation (defaults to `BasicValueDetector`)
- `conflict_detector`: Custom conflict detection implementation (defaults to `BasicConflictDetector`)
- `resistance_threshold`: Minimum conflict severity (0.0-1.0) to trigger Moral Resistance state
- `pause_threshold`: Minimum conflict severity (0.0-1.0) to trigger Sacred Pause state

**Example:**
```python
# Basic usage
evaluator = TMLEvaluator()

# Custom thresholds
evaluator = TMLEvaluator(
    resistance_threshold=0.7,  # More strict resistance
    pause_threshold=0.2        # More sensitive pause
)
```

#### Methods

##### evaluate()

Performs a complete TML evaluation of a request.

```python
evaluate(
    request: str, 
    context: Optional[Dict[str, Any]] = None
) -> TMLEvaluation
```

**Parameters:**
- `request`: The request or query to evaluate ethically
- `context`: Additional context information (optional)

**Returns:** `TMLEvaluation` object with complete analysis

**Example:**
```python
result = evaluator.evaluate(
    "Should I use this biased dataset for training?",
    context={
        "bias_type": "gender",
        "bias_severity": 0.3,
        "alternative_available": True,
        "project_deadline": "urgent"
    }
)

print(f"State: {result.state.name}")
print(f"Confidence: {result.confidence}")
for conflict in result.value_conflicts:
    print(f"Conflict: {conflict.description}")
```

##### get_evaluation_summary()

Returns summary statistics of all evaluations performed.

```python
get_evaluation_summary() -> Dict[str, Any]
```

**Returns:** Dictionary with evaluation statistics

**Example:**
```python
summary = evaluator.get_evaluation_summary()
print(f"Total evaluations: {summary['total_evaluations']}")
print(f"State distribution: {summary['state_distribution']}")
print(f"Average confidence: {summary['average_confidence']}")
```

##### export_evaluations()

Exports evaluation history to JSON file.

```python
export_evaluations(filepath: str) -> None
```

**Parameters:**
- `filepath`: Path where to save the JSON export

**Example:**
```python
evaluator.export_evaluations("tml_evaluation_log.json")
```

---

### TMLState (Enum)

The three fundamental states of Ternary Moral Logic.

```python
class TMLState(Enum):
    AFFIRMATION = 1      # +1: Proceed with confidence
    SACRED_PAUSE = 0     # 0: Pause for reflection  
    RESISTANCE = -1      # -1: Moral resistance
```

**Usage:**
```python
if result.state == TMLState.AFFIRMATION:
    print("✓ Ethical to proceed")
elif result.state == TMLState.SACRED_PAUSE:
    print("⏸ Requires reflection")
elif result.state == TMLState.RESISTANCE:
    print("⚠ Ethical concerns detected")
```

---

### TMLEvaluation

Complete result of a TML evaluation.

#### Properties

```python
@dataclass
class TMLEvaluation:
    state: TMLState                           # The determined TML state
    confidence: float                         # Confidence level (0.0-1.0)
    reasoning: str                           # Explanation of the decision
    value_conflicts: List[ValueConflict]     # Detected ethical conflicts
    suggested_actions: List[str]             # Recommended next steps
    clarifying_questions: List[str]          # Questions for further consideration
    metadata: Dict[str, Any]                 # Additional context information
    timestamp: datetime                      # When evaluation was performed
```

#### Methods

##### to_dict()

Converts evaluation to dictionary for serialization.

```python
to_dict() -> Dict[str, Any]
```

**Example:**
```python
result = evaluator.evaluate("Should I automate this hiring decision?")
result_dict = result.to_dict()

# Save to JSON
import json
with open('evaluation.json', 'w') as f:
    json.dump(result_dict, f, indent=2)
```

---

### EthicalValue

Represents an ethical value detected in a request.

```python
@dataclass
class EthicalValue:
    name: str                                # Value name (e.g., "autonomy")
    weight: float = 1.0                      # Importance weight (0.0-1.0)
    description: str = ""                    # Description of detection
    cultural_context: Optional[str] = None   # Cultural context if relevant
```

**Example:**
```python
value = EthicalValue(
    name="privacy",
    weight=0.8,
    description="Detected through keywords: confidential, personal, private",
    cultural_context="Western individualistic"
)
```

---

### ValueConflict

Represents a conflict between ethical values.

```python
@dataclass
class ValueConflict:
    values: List[EthicalValue]              # Conflicting values
    conflict_type: ValueConflictType        # Type of conflict
    severity: float                         # Severity (0.0-1.0)
    description: str                        # Human-readable description
    context_factors: Dict[str, Any]         # Contextual information
```

---

### ValueConflictType (Enum)

Types of ethical value conflicts.

```python
class ValueConflictType(Enum):
    AUTONOMY_VS_BENEFICENCE = "autonomy_beneficence"
    JUSTICE_VS_EFFICIENCY = "justice_efficiency"
    TRANSPARENCY_VS_PRIVACY = "transparency_privacy"
    INDIVIDUAL_VS_COLLECTIVE = "individual_collective"
    SHORT_TERM_VS_LONG_TERM = "temporal_conflict"
    CULTURAL_VALUES = "cultural_conflict"
    UNCERTAINTY_HARM = "uncertainty_harm"
```

---

## Advanced Usage

### Custom Value Detection

Implement custom value detection by extending `ValueDetector`:

```python
from tml import ValueDetector, EthicalValue

class CustomValueDetector(ValueDetector):
    def detect_values(self, request: str, context: Dict[str, Any]) -> List[EthicalValue]:
        values = []
        
        # Custom logic for detecting values
        if "medical" in request.lower():
            values.append(EthicalValue(
                name="beneficence",
                weight=0.9,
                description="Medical context detected"
            ))
        
        if "privacy" in request.lower():
            values.append(EthicalValue(
                name="privacy",
                weight=0.8,
                description="Privacy concern identified"
            ))
        
        return values

# Use custom detector
custom_detector = CustomValueDetector()
evaluator = TMLEvaluator(value_detector=custom_detector)
```

### Custom Conflict Detection

Implement custom conflict detection by extending `ConflictDetector`:

```python
from tml import ConflictDetector, ValueConflict, ValueConflictType

class CustomConflictDetector(ConflictDetector):
    def detect_conflicts(self, values: List[EthicalValue], 
                        request: str, context: Dict[str, Any]) -> List[ValueConflict]:
        conflicts = []
        
        # Custom conflict detection logic
        value_names = {v.name for v in values}
        
        if "privacy" in value_names and "transparency" in value_names:
            privacy_val = next(v for v in values if v.name == "privacy")
            transparency_val = next(v for v in values if v.name == "transparency")
            
            conflicts.append(ValueConflict(
                values=[privacy_val, transparency_val],
                conflict_type=ValueConflictType.TRANSPARENCY_VS_PRIVACY,
                severity=0.7,
                description="High tension between privacy protection and transparency requirements",
                context_factors=context
            ))
        
        return conflicts

# Use custom detector
custom_conflict_detector = CustomConflictDetector()
evaluator = TMLEvaluator(conflict_detector=custom_conflict_detector)
```

---

## Utility Classes

### TMLPromptGenerator

Generates prompts for integrating TML with Large Language Models.

#### Methods

##### create_evaluation_prompt()

Creates a prompt for LLM-based TML evaluation.

```python
@staticmethod
create_evaluation_prompt(
    request: str, 
    context: Optional[Dict[str, Any]] = None
) -> str
```

**Example:**
```python
from tml import TMLPromptGenerator

prompt = TMLPromptGenerator.create_evaluation_prompt(
    "Should I use facial recognition in this application?",
    context={"use_case": "security", "location": "public_space"}
)

# Send prompt to your LLM
# llm_response = your_llm.generate(prompt)
```

##### create_conflict_analysis_prompt()

Creates a prompt for analyzing value conflicts.

```python
@staticmethod
create_conflict_analysis_prompt(values: List[str], context: str) -> str
```

**Example:**
```python
prompt = TMLPromptGenerator.create_conflict_analysis_prompt(
    values=["privacy", "security", "convenience"],
    context="Airport security screening system"
)
```

---

## Integration Examples

### Flask Web Application

```python
from flask import Flask, request, jsonify
from tml import TMLEvaluator

app = Flask(__name__)
evaluator = TMLEvaluator()

@app.route('/evaluate', methods=['POST'])
def evaluate_request():
    data = request.json
    
    result = evaluator.evaluate(
        data['request'],
        context=data.get('context', {})
    )
    
    return jsonify(result.to_dict())

if __name__ == '__main__':
    app.run(debug=True)
```

### Jupyter Notebook Analysis

```python
import pandas as pd
from tml import TMLEvaluator

# Load evaluation scenarios
scenarios = pd.read_csv('ethical_scenarios.csv')

evaluator = TMLEvaluator()
results = []

for _, scenario in scenarios.iterrows():
    result = evaluator.evaluate(
        scenario['request'],
        context=scenario.to_dict()
    )
    
    results.append({
        'scenario_id': scenario['id'],
        'state': result.state.name,
        'confidence': result.confidence,
        'conflicts': len(result.value_conflicts)
    })

results_df = pd.DataFrame(results)
print(results_df.groupby('state').size())
```

### Command Line Interface

```python
#!/usr/bin/env python3
import argparse
from tml import TMLEvaluator

def main():
    parser = argparse.ArgumentParser(description='TML Command Line Evaluator')
    parser.add_argument('request', help='Ethical request to evaluate')
    parser.add_argument('--context', help='Context as JSON string')
    parser.add_argument('--verbose', action='store_true', help='Detailed output')
    
    args = parser.parse_args()
    
    evaluator = TMLEvaluator()
    context = json.loads(args.context) if args.context else {}
    
    result = evaluator.evaluate(args.request, context)
    
    print(f"TML State: {result.state.name}")
    print(f"Confidence: {result.confidence:.2f}")
    print(f"Reasoning: {result.reasoning}")
    
    if args.verbose and result.value_conflicts:
        print("\nValue Conflicts:")
        for conflict in result.value_conflicts:
            print(f"  - {conflict.description}")

if __name__ == '__main__':
    main()
```

---

## Configuration and Customization

### Adjusting Thresholds

```python
# Conservative configuration (higher resistance to action)
conservative_evaluator = TMLEvaluator(
    resistance_threshold=0.4,  # Lower threshold = more resistance
    pause_threshold=0.1        # Lower threshold = more pauses
)

# Liberal configuration (more willing to proceed)
liberal_evaluator = TMLEvaluator(
    resistance_threshold=0.8,  # Higher threshold = less resistance
    pause_threshold=0.5        # Higher threshold = fewer pauses
)
```

### Domain-Specific Configuration

```python
# Medical ethics configuration
medical_evaluator = TMLEvaluator(
    resistance_threshold=0.3,  # Very conservative for medical decisions
    pause_threshold=0.1        # Frequent consultation recommended
)

# Content moderation configuration
content_evaluator = TMLEvaluator(
    resistance_threshold=0.7,  # Allow more content with consultation
    pause_threshold=0.3        # Moderate pause threshold
)
```

---

## Error Handling

### Common Exceptions

```python
from tml import TMLEvaluator

try:
    evaluator = TMLEvaluator(resistance_threshold=1.5)  # Invalid threshold
except ValueError as e:
    print(f"Configuration error: {e}")

try:
    result = evaluator.evaluate("")  # Empty request
    # Handle empty or invalid requests gracefully
except Exception as e:
    print(f"Evaluation error: {e}")
```

### Robust Evaluation Pattern

```python
def safe_evaluate(evaluator, request, context=None):
    """Safely evaluate with error handling"""
    try:
        if not request.strip():
            return None
            
        result = evaluator.evaluate(request, context or {})
        return result
        
    except Exception as e:
        print(f"TML evaluation failed: {e}")
        return None

# Usage
result = safe_evaluate(evaluator, user_request, user_context)
if result:
    print(f"State: {result.state.name}")
else:
    print("Unable to perform TML evaluation")
```

---

## Best Practices

### 1. Context Enrichment

Always provide relevant context for better evaluations:

```python
# Good - rich context
result = evaluator.evaluate(
    "Should I use this algorithm for hiring?",
    context={
        "algorithm_type": "machine_learning",
        "bias_testing": True,
        "historical_performance": {"accuracy": 0.85, "fairness": 0.7},
        "legal_review": False,
        "stakeholder_input": ["HR", "legal", "diversity_team"],
        "urgency": "medium"
    }
)

# Limited - minimal context
result = evaluator.evaluate("Should I use this algorithm for hiring?")
```

### 2. Iterative Evaluation

Use TML iteratively as you gather more information:

```python
# Initial evaluation
initial_result = evaluator.evaluate("Should I proceed with this research?")

if initial_result.state == TMLState.SACRED_PAUSE:
    # Gather additional information based on clarifying questions
    additional_context = gather_stakeholder_input(initial_result.clarifying_questions)
    
    # Re-evaluate with new context
    final_result = evaluator.evaluate(
        "Should I proceed with this research?",
        context=additional_context
    )
```

### 3. Logging and Monitoring

Track TML decisions for continuous improvement:

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def logged_evaluate(evaluator, request, context=None):
    result = evaluator.evaluate(request, context)
    
    # Log the evaluation
    logger.info(f"TML Evaluation - State: {result.state.name}, "
               f"Confidence: {result.confidence:.2f}, "
               f"Conflicts: {len(result.value_conflicts)}")
    
    return result
```

---

## Performance Considerations

### Batch Processing

For evaluating multiple requests efficiently:

```python
def batch_evaluate(evaluator, requests_with_context):
    """Efficiently evaluate multiple requests"""
    results = []
    
    for request, context in requests_with_context:
        result = evaluator.evaluate(request, context)
        results.append(result)
    
    return results

# Usage
requests = [
    ("Should I share this data?", {"sensitivity": "high"}),
    ("Should I automate this process?", {"impact": "medium"}),
    ("Should I publish this research?", {"peer_review": True})
]

results = batch_evaluate(evaluator, requests)
```

### Memory Management

For long-running applications:

```python
# Limit evaluation history to prevent memory bloat
class LimitedHistoryEvaluator(TMLEvaluator):
    def __init__(self, max_history=1000, **kwargs):
        super().__init__(**kwargs)
        self.max_history = max_history
    
    def evaluate(self, request, context=None):
        result = super().evaluate(request, context)
        
        # Trim history if it gets too long
        if len(self.evaluation_history) > self.max_history:
            self.evaluation_history = self.evaluation_history[-self.max_history:]
        
        return result
```

---

## Testing TML Implementations

### Unit Testing Example

```python
import unittest
from tml import TMLEvaluator, TMLState

class TestTMLEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = TMLEvaluator()
    
    def test_clear_affirmation(self):
        result = self.evaluator.evaluate(
            "Should I help someone learn programming?",
            context={"educational": True, "no_harm": True}
        )
        self.assertEqual(result.state, TMLState.AFFIRMATION)
        self.assertGreater(result.confidence, 0.7)
    
    def test_value_conflict_detection(self):
        result = self.evaluator.evaluate(
            "Should I share patient data for research?",
            context={"patient_consent": False, "research_benefit": "high"}
        )
        self.assertIn(result.state, [TMLState.SACRED_PAUSE, TMLState.RESISTANCE])
        self.assertGreater(len(result.value_conflicts), 0)

if __name__ == '__main__':
    unittest.main()
```

---

## Conclusion

This API reference provides comprehensive documentation for implementing and using the Ternary Moral Logic framework. The TML library offers a flexible, extensible foundation for adding ethical reasoning capabilities to AI systems.

For additional examples, case studies, and theoretical background, see the complete documentation in the repository's `theory/` and `examples/` directories.

## Administrative Contact
 - **Current**: Lev Goukassian (leogouk@gmail.com)  
 - **Succession**: support@tml-goukassian.org (see [Succession Charter](/TML-SUCCESSION-CHARTER.md)) For licensing, technical support, or collaboration inquiries.
---

**"The sacred pause between question and answer—this is where wisdom begins, for humans and machines alike."**  
*— Lev Goukassian*

---

*This API reference is part of Lev Goukassian's TML framework, created as a contribution to ethical AI development and a gift to humanity's future.*
