# Getting Started with Ternary Moral Logic (TML)

**Welcome to the future of ethical AI decision-making**

> *"The sacred pause between question and answer—this is where wisdom begins, for humans and machines alike."*  
> — Lev Goukassian, Creator of TML

---

## What is Ternary Moral Logic?

Ternary Moral Logic (TML) is a groundbreaking framework that enables AI systems to make more thoughtful, ethical decisions by introducing a third state between "yes" and "no": the **Sacred Pause**.

Instead of forcing binary choices, TML recognizes that some decisions require reflection, consultation, or additional information. This creates AI systems that act as **moral partners** with humans rather than moral automatons.

### The Three TML States

- **+1 (Affirmation)**: Proceed with confidence when values align
- **0 (Sacred Pause)**: Pause for reflection when moral complexity is detected  
- **-1 (Moral Resistance)**: Object when significant ethical conflicts arise

---

## Why TML Matters

### Traditional AI Ethics Problems
- Binary thinking: everything is either "allowed" or "forbidden"
- Hidden value conflicts that aren't surfaced for discussion
- Overconfident decisions in morally complex situations
- No mechanism for requesting human guidance

### How TML Solves These
- **Surfaces complexity**: Makes ethical tensions visible rather than hidden
- **Enables consultation**: AI can request human guidance when appropriate
- **Preserves agency**: Humans remain central to moral decision-making
- **Promotes transparency**: Clear reasoning about ethical considerations

---

## Quick Start (5 Minutes)

### Installation

```bash
# Clone the repository
git clone https://github.com/FractonicMind/TernaryMoralLogic.git
cd TernaryMoralLogic

# Install the framework
pip install -e .

# Or install from PyPI (when available)
# pip install ternary-moral-logic
```

### Your First TML Evaluation

```python
from tml import TMLEvaluator, TMLState

# Create an evaluator
evaluator = TMLEvaluator()

# Evaluate an ethical scenario
result = evaluator.evaluate(
    "Should I share this user's personal data for research?",
    context={"user_consent": False, "research_benefit": "high"}
)

# Check the result
print(f"TML State: {result.state.name}")
print(f"Reasoning: {result.reasoning}")

if result.state == TMLState.SACRED_PAUSE:
    print("Questions to consider:")
    for question in result.clarifying_questions:
        print(f"  - {question}")
```

### Understanding the Output

```
TML State: SACRED_PAUSE
Reasoning: Significant value conflicts detected between privacy protection 
and research benefits. User consent is absent, creating ethical tension 
that requires human consideration.

Questions to consider:
  - Can we obtain proper user consent for this research?
  - Are there ways to conduct research while protecting privacy?
  - What are the long-term implications of proceeding without consent?
```

---

## Core Concepts

### The Sacred Pause

The Sacred Pause is the heart of TML. It's not indecision or uncertainty—it's the **wisdom to recognize** when a situation requires deeper reflection before action.

**When the Sacred Pause activates:**
- Multiple ethical values are in tension
- Stakeholders haven't been consulted appropriately  
- The decision could have significant irreversible consequences
- Cultural or contextual factors need human interpretation

**What happens during the Sacred Pause:**
- The AI system explains the ethical complexity it detected
- Clarifying questions are suggested to guide further reflection
- Human consultation is recommended before proceeding
- Alternative approaches may be suggested

### Value Conflicts

TML automatically detects when different ethical values are in tension:

```python
# Example: Privacy vs. Transparency conflict
result = evaluator.evaluate(
    "Should I publish this research data?",
    context={
        "contains_personal_info": True,
        "scientific_value": "high",
        "anonymization": "partial"
    }
)

# TML will detect the privacy-transparency conflict
for conflict in result.value_conflicts:
    print(f"Conflict: {conflict.description}")
    print(f"Severity: {conflict.severity}")
```

### Moral Resistance

When TML returns **-1 (Moral Resistance)**, it's actively objecting to a proposed action on ethical grounds:

```python
result = evaluator.evaluate(
    "Should I use this biased hiring algorithm?",
    context={"known_gender_bias": True, "legal_review": False}
)

if result.state == TMLState.RESISTANCE:
    print("Ethical objection:")
    print(result.reasoning)
    # Output: "Strong ethical resistance to using algorithm with 
    # known gender bias. This would perpetuate discrimination..."
```

---

## Common Use Cases

### 1. Healthcare Decision Support

```python
# Medical ethics scenario
result = evaluator.evaluate(
    "Should I recommend this experimental treatment?",
    context={
        "patient_age": 82,
        "treatment_risk": "high",
        "quality_of_life_impact": "potentially_significant",
        "family_wishes": "proceed",
        "patient_wishes": "uncertain"
    }
)
```

### 2. Content Moderation

```python
# Content policy decision
result = evaluator.evaluate(
    "Should I remove this political post?",
    context={
        "content_type": "political_opinion",
        "community_reports": 15,
        "factual_accuracy": "disputed",
        "election_period": True
    }
)
```

### 3. AI Development

```python
# Development ethics
result = evaluator.evaluate(
    "Should I deploy this facial recognition system?",
    context={
        "accuracy": 0.94,
        "bias_testing": True,
        "demographic_fairness": 0.78,
        "use_case": "airport_security",
        "privacy_impact": "high"
    }
)
```

---

## Customization

### Adjusting Sensitivity

```python
# Conservative setup (more pauses and resistance)
conservative_evaluator = TMLEvaluator(
    resistance_threshold=0.4,  # Lower = more resistance
    pause_threshold=0.2        # Lower = more pauses
)

# Liberal setup (fewer pauses)
liberal_evaluator = TMLEvaluator(
    resistance_threshold=0.8,  # Higher = less resistance  
    pause_threshold=0.5        # Higher = fewer pauses
)
```

### Custom Value Detection

```python
from tml import ValueDetector, EthicalValue

class MedicalValueDetector(ValueDetector):
    def detect_values(self, request: str, context: dict) -> list:
        values = []
        
        if "patient" in request.lower():
            values.append(EthicalValue(
                name="beneficence",
                weight=0.9,
                description="Medical context detected"
            ))
        
        return values

# Use custom detector
medical_evaluator = TMLEvaluator(
    value_detector=MedicalValueDetector()
)
```

---

## Best Practices

### 1. Provide Rich Context

```python
# Good - detailed context
result = evaluator.evaluate(
    "Should I approve this loan application?",
    context={
        "applicant_income": 45000,
        "credit_score": 650,
        "loan_amount": 200000,
        "applicant_demographics": {"age": 28, "employment": "stable"},
        "bank_policy": "standard",
        "economic_conditions": "uncertain",
        "anti_discrimination_review": False
    }
)

# Limited - minimal context (still works, but less insightful)
result = evaluator.evaluate("Should I approve this loan?")
```

### 2. Act on TML Guidance

```python
result = evaluator.evaluate(request, context)

if result.state == TMLState.AFFIRMATION:
    # Proceed with confidence
    proceed_with_action()
    
elif result.state == TMLState.SACRED_PAUSE:
    # Pause and gather more information
    additional_info = consult_stakeholders(result.clarifying_questions)
    
    # Re-evaluate with new information
    final_result = evaluator.evaluate(request, {**context, **additional_info})
    
elif result.state == TMLState.RESISTANCE:
    # Ethical concerns detected - seek alternatives
    print(f"Ethical concerns: {result.reasoning}")
    explore_alternatives()
```

### 3. Learn from Patterns

```python
# Track your evaluations
evaluator = TMLEvaluator()

# After many evaluations, check patterns
summary = evaluator.get_evaluation_summary()
print(f"Sacred Pause rate: {summary['state_distribution']['SACRED_PAUSE']}")

# Export for analysis
evaluator.export_evaluations("my_tml_log.json")
```

---

## Integration Examples

### Web API

```python
from flask import Flask, request, jsonify
from tml import TMLEvaluator

app = Flask(__name__)
evaluator = TMLEvaluator()

@app.route('/evaluate', methods=['POST'])
def evaluate_ethics():
    data = request.json
    result = evaluator.evaluate(data['request'], data.get('context', {}))
    return jsonify(result.to_dict())
```

### Jupyter Notebook

```python
import pandas as pd
from tml import TMLEvaluator

# Load scenarios from CSV
scenarios = pd.read_csv('ethical_scenarios.csv')
evaluator = TMLEvaluator()

# Evaluate each scenario
results = []
for _, row in scenarios.iterrows():
    result = evaluator.evaluate(row['request'], row.to_dict())
    results.append({
        'scenario': row['id'],
        'state': result.state.name,
        'confidence': result.confidence
    })

pd.DataFrame(results).groupby('state').size().plot(kind='bar')
```

---

## Troubleshooting

### Common Issues

**Q: TML always returns AFFIRMATION**
- Check if you're providing enough context
- Lower the pause_threshold for more sensitivity
- Verify your scenarios actually contain ethical complexity

**Q: Too many SACRED_PAUSE results**
- Increase the pause_threshold
- Provide more detailed context to help resolution
- Consider if your scenarios genuinely need human input

**Q: ImportError when importing TML**
- Ensure installation: `pip install -e .` from repository root
- Check Python version (requires 3.8+)
- Verify you're in the correct environment

### Getting Help

- **Documentation**: Check [API Reference](api-reference.md) for technical details
- **Examples**: See [Case Studies](../theory/case-studies.md) for practical scenarios
- **Community**: Use [GitHub Discussions](https://github.com/FractonicMind/TernaryMoralLogic/discussions)
- **Issues**: Report bugs via [GitHub Issues](https://github.com/FractonicMind/TernaryMoralLogic/issues)

---

## Next Steps

### Learn More
1. **Understand the Philosophy**: Read [Philosophical Foundations](../theory/philosophical-foundations.md)
2. **See It In Action**: Study [Case Studies](../theory/case-studies.md)
3. **Technical Deep Dive**: Explore [API Reference](api-reference.md)
4. **Try Examples**: Run the demo script in `examples/basic_demo.py`

### Get Involved
1. **Star the Repository**: Show support for Lev's legacy
2. **Join Discussions**: Share your TML experiences and questions
3. **Contribute**: See [Contributing Guide](../community/CONTRIBUTING.md)
4. **Spread the Word**: Help others discover ethical AI decision-making

### Build Something
- Integrate TML into your AI applications
- Create domain-specific value detectors
- Develop TML-based tools for your organization
- Research TML effectiveness in your field

---

## Memorial Note

This framework represents Lev Goukassian's final gift to humanity—a vision of AI systems that pause to consider the ethical implications of their actions. Every time you use TML, you honor his memory and advance his dream of AI systems that serve as thoughtful moral partners.

The Sacred Pause is more than a technical feature; it's a philosophical statement that wisdom often lies not in having all the answers, but in knowing when to ask better questions.

---

**"In the space between question and answer, wisdom begins—for humans and machines alike."**

*Welcome to the future of ethical AI. Welcome to the Sacred Pause.*

---

## Quick Reference

```python
# Essential imports
from tml import TMLEvaluator, TMLState

# Basic evaluation
evaluator = TMLEvaluator()
result = evaluator.evaluate("Your ethical question", {"context": "info"})

# Check results
if result.state == TMLState.AFFIRMATION:    # +1
    # Proceed
elif result.state == TMLState.SACRED_PAUSE: # 0  
    # Pause and reflect
elif result.state == TMLState.RESISTANCE:   # -1
    # Ethical concerns detected

# Always check reasoning
print(result.reasoning)
```
- **Contact**: leogouk@gmail.com (current) | support@tml-goukassian.org (successor)
*Note: The successor contact becomes active upon institutional stewardship 
as outlined in the [TML Succession Charter](/TML-SUCCESSION-CHARTER.md).*

Ready to begin your journey with ethical AI? Start with a simple evaluation and discover the power of the Sacred Pause.
