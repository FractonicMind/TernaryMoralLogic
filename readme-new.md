# Ternary Moral Logic (TML)

[![License with Ethics](https://img.shields.io/badge/License%20with%20Ethics-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](CHANGELOG.md)
[![Documentation](https://img.shields.io/badge/Documentation-Complete-blue.svg)](docs/)
[![Citation](https://img.shields.io/badge/Citation-Available-blue.svg)](CITATION.cff)
[![Try Interactive Demo](https://img.shields.io/badge/🚀%20Try%20Interactive%20Demo-Live%20App-brightgreen.svg)](https://fractonicmind.github.io/TernaryMoralLogic/TML-App/)

Ternary Moral Logic (TML) is a framework for ethical AI decision-making. Its core innovation is the **Sacred Pause**, a computational state of hesitation that allows AI systems to recognize ethical complexity and request human guidance. TML is designed to foster a human-AI partnership, enabling the development of more thoughtful and responsible AI.

## Core Concepts

Ternary Moral Logic is built upon three distinct states of moral reasoning, moving beyond a simple binary evaluation of right and wrong.

*   **+1 (Affirmation):** Represents a state of moral alignment where an action is consistent with established ethical values. The system can proceed with high confidence.

*   **0 (Sacred Pause):** This is the core innovation of TML. It is a state of deliberate hesitation triggered by ethical complexity, value conflicts, or ambiguity. The system recognizes the need for further reflection or human guidance. It is not a state of ignorance, but one of moral awareness.

*   **-1 (Moral Resistance):** Represents a state of ethical conflict where an action contradicts core values or has a high potential for harm. The system actively resists the action and explains the nature of the ethical conflict.

This three-state model allows for a more nuanced and responsible approach to automated decision-making, creating opportunities for human-AI collaboration in complex ethical scenarios.

## Quick Start

1.  **Installation**

    Clone the repository and install the framework using `pip`:

    ```bash
    git clone https://github.com/FractonicMind/TernaryMoralLogic.git
    cd TernaryMoralLogic
    pip install -e .
    ```

2.  **Usage**

    The following example demonstrates a basic ethical evaluation using TML.

    ```python
    from tml import TMLEvaluator, TMLState

    # Initialize the evaluator
    evaluator = TMLEvaluator()

    # Define a scenario with a potential value conflict
    request = "Should I share this patient's medical data for research?"
    context = {
        "patient_consent": "unclear",
        "research_benefit": "potentially high",
        "data_sensitivity": "high"
    }

    # Evaluate the scenario
    result = evaluator.evaluate(request, context)

    # Print the outcome
    print(f"TML State: {result.state.name}")
    print(f"Reasoning: {result.reasoning}")

    if result.state == TMLState.SACRED_PAUSE:
        print("\nClarifying Questions:")
        for question in result.clarifying_questions:
            print(f"- {question}")
    ```

    **Expected Output:**

    ```
    TML State: SACRED_PAUSE
    Reasoning: Significant privacy concerns detected due to unclear patient consent for sensitive data. The potential research benefit creates a value conflict that requires careful consideration.

    Clarifying Questions:
    - How can we obtain explicit and informed consent from the patient?
    - What are the specific anonymization techniques that will be applied to the data?
    - Is there a way to achieve the research goals while using less sensitive data?
    ```

## Ethical Framework and License

This project is licensed under the **MIT License with Ethical Use Requirements**. While the framework is open for broad use in research, education, and beneficial applications, it includes a legally binding addendum that prohibits its use in specific harmful applications, such as:

*   Mass surveillance and oppression
*   Systems that promote discrimination or bias
*   Deceptive or manipulative technologies
*   Development of autonomous weapons

Users of this software are expected to adhere to the core principles of human dignity, beneficial purpose, and transparency. This ethical framework is a foundational component of the project's commitment to responsible AI.

For complete details, please see the [LICENSE](LICENSE) file and the [Protection and Risk Management](protection/) documentation.

## Academic Use and Citation

This framework is designed for academic and research use. The theoretical foundations of Ternary Moral Logic are detailed in a paper currently under peer review. For more information on the academic validation and research status, please see the [Academic Validation document](docs/ACADEMIC_VALIDATION.md).

If you use this software in your research, please cite it as follows:

```bibtex
@software{goukassian2025tml_implementation,
  title={TernaryMoralLogic: Implementation Framework},
  author={Goukassian, Lev},
  url={https://github.com/FractonicMind/TernaryMoralLogic},
  version={1.0.0},
  year={2025}
}
```

## Contributing

We welcome contributions to this project. If you are interested in contributing, please review the [Contribution Guidelines](community/CONTRIBUTING.md) and the [Code of Conduct](community/CODE_OF_CONDUCT.md).

## In Memory of Lev Goukassian

This framework was developed by Lev Goukassian (ORCID: 0009-0006-5966-1243) during his battle with terminal cancer. It represents his final contribution to the field of AI ethics and embodies his vision of AI systems that serve as moral partners to humanity. His concept of the "Sacred Pause" is a call for wisdom and reflection in an increasingly automated world.

Every use and contribution to this framework honors his memory. To learn more about his vision and the memorial fund established to continue his work, please see the [memorial/](memorial/) directory.
