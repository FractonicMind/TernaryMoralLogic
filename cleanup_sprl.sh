#!/bin/bash
echo "Starting SPRL cleanup..."
rm -rf src/tml_sprl/
rm -f benchmark/generate_coverage.py
rm -f benchmark/metrics.py
rm -f compliance/framework_integrity.py
rm -f compliance/missing_logs.py
rm -f compliance/simple_tml_validator.py
rm -f examples/SPRL_Dynamic_vs_Static.py
rm -f tests/isolated_test.py
rm -f tests/prohibition_enforcement.py
rm -f tests/sacred_pause_trigger.py
rm -f tests/test_tml_core.py
rm -f examples/medical_ai_triage.py
rm -f examples/autonomous_vehicle.py
rm -f examples/basic_demo.py
rm -f examples/content_moderation.py
rm -f examples/financial_ai.py
rm -f benchmark/SPRL_*
rm -f docs/SPRL_*
rm -f docs/Stakeholder_Proportional_Risk_Level*
rm -f governance/SPRL_*
rm -f protection/SPRL_*
rm -f protection/sprl-enforcement.md
rm -f research/SPRL_*
rm -f security/SPRL_*
rm -f ui/SPRL_*
rm -rf marketing/
rm -f benchmark/SPRL_TestSet_v1.json
rm -rf benchmark/datasets/
rm -rf eval/
echo "SPRL cleanup complete!"
