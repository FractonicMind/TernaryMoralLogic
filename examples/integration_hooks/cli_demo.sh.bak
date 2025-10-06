#!/usr/bin/env bash
# Usage: ./cli_demo.sh "your prompt"

PROMPT="${1:-Hello there}"
python3 - <<'PY'
from examples.integration_hooks.simple_wrapper import DummyModel, RiskEngine
prompt = """'"''" + """  # placeholder to avoid shell escaping issues
PY
