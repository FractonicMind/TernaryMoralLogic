# SPRL Integration Hooks (Quick Start)

These minimal hooks show how to integrate the dual-layer SPRL mechanism with an AI inference pipeline. They are intentionally lightweight and non-framework-specific.

## Files
- `simple_wrapper.py` — Python wrapper around a model’s generate() that streams DS updates and emits SA.
- `webhook_stub.js` — Example of forwarding logs to an external endpoint (e.g., governance mirror).
- `cli_demo.sh` — One-line demo to run the wrapper with a sample prompt.

## Assumptions
- Your SPRL implementation exposes a `RiskEngine` with:
  - `start_session(prompt)` → returns `session_id`
  - `update(token)` → updates DS risk; returns `{risk, crossed_anchor?: bool, anchor_time?}`
  - `emit_anchor(session_id)` → writes the Static Anchor (SA)
  - `log_lite_trace(session_id, metadata)`
  - `finalize(session_id, decision)`

Replace the placeholders with your real engine bindings.

## Notes
- Logging is non-blocking. The wrapper must not delay model tokenization.
- SA emission is immediate at threshold crossing. No numeric SLA is specified here.
- Lite Traces are encouraged for sub-threshold ethical complexity.

See `docs/SPRL_OPERATION_MODES.md` for runtime obligations.
