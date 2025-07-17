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

Research Foundation
This implementation is based on academic research currently under peer review:
Paper: "Ternary Moral Logic: Implementing Ethical Hesitation in AI Systems"
Author: Lev Goukassian
Journal: AI and Ethics (under review)
Installation


---

> *"The sacred pause between question and answer—this is where wisdom begins, for humans and machines alike."*

---

**⭐ Star this repository if you believe AI systems should be moral partners, not just moral automatons!**
