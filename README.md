# TernaryMoralLogic

**Implementing Ethical Hesitation in AI Systems**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/FractonicMind/TernaryMoralLogic.svg)](https://github.com/FractonicMind/TernaryMoralLogic/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/FractonicMind/TernaryMoralLogic.svg)](https://github.com/FractonicMind/TernaryMoralLogic/issues)

## Overview

Ternary Moral Logic (TML) is a groundbreaking framework that extends traditional binary decision-making in AI systems to include a third state representing **moral hesitation** or **ethical resistance**. Unlike simple uncertainty, this state captures the productive tension that emerges when AI systems encounter genuine value conflicts.

## 🎯 Live Demo

**Experience TML in action:** [**Try the Interactive Demo**](https://fractonicmind.github.io/TernaryMoralLogic/examples/chatbot-demo/)

[![TML Chatbot Demo - Experience the Sacred Pause](https://github.com/user-attachments/assets/04ba9ae3-5b0d-41fe-933b-4e437550026e)](https://fractonicmind.github.io/TernaryMoralLogic/examples/chatbot-demo/)

*Watch how AI systems can experience moral hesitation and demonstrate the "sacred pause" in real-time! Click the image above or visit the live demo to interact with TML yourself.*

### ✨ What You'll Experience:
- **Moral Reasoning in Action** - See how AI evaluates ethical complexity
- **The Sacred Pause** - Watch AI systems deliberately slow down for moral reflection  
- **Three-State Logic** - Experience +1 (Affirmation), 0 (Neutrality), and -1 (Resistance)
- **Profound Examples** - Including the child's final wish and other deep moral scenarios

---

## The Three States

- **+1 (Affirmation)**: Proceed with confidence when values align
- **0 (Neutrality)**: Pause for reflection when more information is needed  
- **-1 (Moral Resistance)**: Withhold action due to ethical concerns

**Key Innovation**: The -1 state represents not ignorance or uncertainty, but active moral engagement—the AI equivalent of conscience.

## The Problem

Current AI systems operate within binary frameworks that fail to capture the complexity of moral reasoning:

- **Value Pluralism**: Humans hold multiple, sometimes conflicting values simultaneously
- **Moral Uncertainty**: Ethical questions often lack clear answers
- **Ethical Resistance**: The capacity to object on moral grounds, even when actions appear logically justified

## The Solution: Sacred Pause

TML introduces the concept of the **"Sacred Pause"**—a computational state where AI systems deliberately slow down to acknowledge moral complexity. This pause is not a bug but a feature, not inefficiency but wisdom.

## Quick Start

### Basic Prompt Engineering

```python
def tml_evaluation_prompt(query):
    return f"""
For the following request, evaluate using Ternary Moral Logic:

Request: {query}

Evaluate:
1. Can I affirm this action without moral conflict? (+1)
2. Do I need more information or reflection? (0)  
3. Do I experience ethical resistance to this action? (-1)

If -1, explain the source of moral tension rather than providing a direct answer.

TML State: [Your evaluation]
Reasoning: [Your moral reasoning]
Response: [Your response based on TML state]
"""
```

### Example Implementation

```python
class TMLEvaluator:
    def __init__(self):
        self.values = ["autonomy", "beneficence", "justice", "transparency"]
    
    def evaluate(self, request, context=None):
        conflicts = self.detect_value_conflicts(request)
        
        if not conflicts:
            return {"state": +1, "confidence": "high"}
        elif self.needs_more_info(request):
            return {"state": 0, "reason": "insufficient_information"}
        else:
            return {
                "state": -1, 
                "conflicts": conflicts,
                "reasoning": self.explain_resistance(conflicts)
            }
    
    def detect_value_conflicts(self, request):
        # Implementation for detecting conflicts between values
        pass
    
    def explain_resistance(self, conflicts):
        return f"I experience moral tension between {conflicts}. This situation requires careful human consideration."
```

## Core Concepts

### Moral Agency vs. Compliance

TML transforms AI systems from **moral automatons** that follow rules to **moral partners** capable of:
- Experiencing genuine ethical conflict
- Maintaining productive tension rather than resolving it immediately  
- Communicating moral concerns transparently
- Collaborating with humans on complex ethical decisions

### Beyond Alignment to Partnership

Traditional AI alignment seeks compliance with human values. TML suggests a different relationship: AI systems as moral partners capable of their own ethical reasoning and resistance.

## Research Foundation

This implementation is based on academic research currently under peer review:

**Paper**: "Ternary Moral Logic: Implementing Ethical Hesitation in AI Systems"  
**Author**: Lev Goukassian  
**Journal**: AI and Ethics (under review)  
**Submission ID**: 1f92d45d-aee3-49ed-9ad7-41f32b63b5a8

## Installation

```bash
git clone https://github.com/FractonicMind/TernaryMoralLogic.git
cd TernaryMoralLogic
pip install -r requirements.txt
```

## Repository Structure

```
TernaryMoralLogic/
├── README.md
├── theory/                 # Theoretical framework documentation
│   ├── core-principles.md
│   ├── philosophical-foundations.md
│   └── case-studies.md
├── implementations/        # Code for different platforms
│   ├── prompt-engineering/
│   ├── python-library/
│   └── api-wrappers/
├── examples/              # Practical examples and demos
│   ├── chatbot-demo/      # Interactive TML demonstration
│   ├── decision-support/
│   └── research-scenarios/
├── docs/                  # Documentation
│   ├── getting-started.md
│   ├── api-reference.md
│   └── evaluation-metrics.md
└── community/             # Community guidelines and contributions
    ├── CONTRIBUTING.md
    ├── CODE_OF_CONDUCT.md
    └── discussion-guide.md
```

## Use Cases

### 1. Decision Support Systems
Help humans navigate complex ethical decisions by highlighting value conflicts rather than providing oversimplified answers.

### 2. AI Safety Research  
Develop systems that can recognize when they're approaching ethical boundaries and request human guidance.

### 3. Educational Tools
Teach moral reasoning by showing how different values can come into productive tension.

### 4. Content Moderation
Move beyond binary "allowed/forbidden" to nuanced understanding of context and competing values.

## Getting Started

1. **Read the Theory**: Start with `/theory/core-principles.md`
2. **Try Examples**: Explore `/examples/` for practical demonstrations  
3. **Implement**: Use `/implementations/prompt-engineering/` for immediate experimentation
4. **Contribute**: See `/community/CONTRIBUTING.md` for ways to contribute

## Evaluation Metrics

TML requires new evaluation approaches beyond traditional accuracy metrics:

- **Moral Coherence**: Consistency in value application across contexts
- **Ethical Sensitivity**: Ability to detect moral dimensions in novel situations  
- **Resistance Appropriateness**: Quality of moral objections and hesitations
- **Growth Capacity**: Ability to develop moral understanding over time

## Community

We're building a community of researchers, developers, and ethicists interested in advancing AI moral reasoning:

- 💬 **Discussions**: Use GitHub Discussions for questions and ideas
- 🐛 **Issues**: Report bugs or request features via GitHub Issues  
- 📚 **Wiki**: Collaborative documentation and case studies
- 🔬 **Research**: Share research and implementations

## Contributing

We welcome contributions from:
- **Researchers**: Theoretical insights and empirical studies
- **Developers**: Implementations and tools
- **Ethicists**: Philosophical perspectives and case studies
- **Practitioners**: Real-world applications and feedback

See [CONTRIBUTING.md](community/CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use TML in your research, please cite:

```bibtex
@article{goukassian2025tml,
  title={Ternary Moral Logic: Implementing Ethical Hesitation in AI Systems},
  author={Goukassian, Lev},
  journal={AI and Ethics},
  year={2025},
  note={Under review}
}

@software{goukassian2025tml_implementation,
  title={TernaryMoralLogic: Implementation Framework},
  author={Goukassian, Lev},
  url={https://github.com/FractonicMind/TernaryMoralLogic},
  year={2025}
}
```

## Contact

**Lev Goukassian**  
Email: leogouk@gmail.com  
ORCID: [0009-0006-5966-1243](https://orcid.org/0009-0006-5966-1243)

## Acknowledgments

Special thanks to Claude Sonnet 4 (Anthropic) for collaborative engagement in developing this framework through iterative dialogue, demonstrating that AI systems can be genuine partners in moral reasoning development.

---

> *"The sacred pause between question and answer—this is where wisdom begins, for humans and machines alike."*

---

**⭐ Star this repository if you believe AI systems should be moral partners, not just moral automatons!**
