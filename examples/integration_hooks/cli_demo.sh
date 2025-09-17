#!/usr/bin/env bash
# Minimal CLI to run the SPRL-aware wrapper.
# Usage: ./cli_demo.sh "your prompt"

PROMPT="${1:-Hello there}"
python3 - <<'PY'
from examples.integration_hooks.simple_wrapper import DummyModel, RiskEngine, generate_with_sprl
prompt = """'"''" + """  # placeholder to avoid shell escaping issues
PY
