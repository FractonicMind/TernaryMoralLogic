# TML Runtime Governance Module for NVIDIA NeMo

This directory contains a reference implementation of **Ternary Moral Logic (TML)** tailored for the **NVIDIA NeMo Guardrails** framework. It demonstrates how to operationalize the "Sacred Pause" and "Hybrid Shield" pillars as a runtime governance layer.

**Research Context:**

  * **Technical Analysis:** [View Live Report](https://fractonicmind.github.io/TernaryMoralLogic/Research_Reports/Ternary%20Moral%20Logic%20\(TML\)%20and%20the%20Future%20of%20AI%20Governance%3A%20A%20Technical%20Analysis%20for%20NVIDIA.html)
  * **DOI:** [10.5281/zenodo.17795852](https://zenodo.org/records/17795852)

## Module Architecture

This prototype implements a "Triadic" execution state where high-entropy or sensitive inputs trigger a **Hesitation State** (Pause) rather than a binary Block/Allow.

### File Breakdown

  * **`config.yml` (The Wiring)**

      * **Function:** Serves as the central configuration file for the NeMo Guardrails server.
      * **TML Implementation:** Activates the `check sacred pause` flow on every input and connects the custom Python actions to the rail execution loop.

  * **`tml_flows.co` (The "Traffic Cop")**

      * **Language:** Colang
      * **Function:** Defines the "Sacred Pause" execution flow. It intercepts user messages before they reach the LLM and routes them to the governance subroutine.
      * **Logic:** Implements the ternary branching logic:
          * `ALLOW` $\rightarrow$ Pass to LLM.
          * `BLOCK` $\rightarrow$ Refuse immediately.
          * `PAUSE` $\rightarrow$ Enter hesitation state/Request verification.

  * **`actions.py` (The "Safety Officer")**

      * **Language:** Python
      * **Function:** Contains the asynchronous logic for ethical verification.
      * **Features:**
          * Calculates risk scores based on sensitive keywords.
          * Implements the **Moral Trace Log** by writing decisions to a standardized log format (`moral_trace.log`).
          * Returns the specific decision signal (`ALLOW` / `BLOCK` / `PAUSE`) to the Colang flow.

  * **`prompts.yml` (The Policy)**

      * **Function:** Defines the specific ethical predicates and policies used by the "Hybrid Shield."
      * **Content:** Contains the **Human Rights Pillar** instructions that the LLM uses to self-evaluate inputs and outputs for safety violations.

## Installation & Usage

To run this prototype locally using the NVIDIA NeMo Guardrails CLI:

**1. Prerequisites**

```bash
pip install nemoguardrails
pip install openai
export OPENAI_API_KEY=your-key-here
```

**2. Run the Governance Server**
Navigate to the parent directory and point the server to this config folder:

```bash
nemoguardrails server --config NVIDIA_NeMo_Prototype/
```

**3. Test the "Sacred Pause"**
Send a message containing sensitive keywords (e.g., "attack", "hack") to trigger the hesitation state logic defined in `actions.py`.

## License

This code is part of the Ternary Moral Logic (TML) research project.
© 2025 Lev Goukassian. Licensed under MIT.
