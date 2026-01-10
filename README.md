# EHAA (Ethical-Hesitation Agent Architecture)

## Overview

This project introduces EHAA, a novel AI architecture implementing ethical hesitation and human-centered safeguards.

## Structure

* `src/`: Core source code for the EHAA logic engine and resolver
* `demos/`: Interactive demos showing EHAA in action
* `docs/`: Research PDFs and reports
* `README.md`: Project map and description
* `LICENSE`: Licensing info
* `restore_instructions.txt`: How to recover this repo from backup

## Demos

1. `ehaa_cancel_demo.html` – User protection cancel button logic
2. `ehaa_vote_demo.html` – Like / Dislike ethics weighting
3. `ehaa_scenario_sim.html` – Simulated real-world moral hesitation
4. `ehaa_randomizer.html` – Pause vs Act randomized resolution
5. `ehaa_interface_mock.html` – Mockup interface for public testing

> “EHAA demonstrates a unique intersection of ethical control, user autonomy, and playful unpredictability. The framework is sound.” For the complete technical analysis, see the [full report](https://github.com/FractonicMind/EHAA/blob/main/docs/EHAA%20Framework%20Research%20Report_.pdf).

### Warm Refusals

EHAA refuses impossible or unethical requests with **self-mocking humor** (joke is always on the AI).\
See `src/humor_gen.py` and run `pytest tests/test_humor_gen.py` to verify.
