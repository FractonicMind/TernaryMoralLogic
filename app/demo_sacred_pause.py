# app/demo_sacred_pause.py
import time
import streamlit as st

# Import the deterministic Sacred Pause backend
from eval.backends.sacred_pause_evalfix import Runner as SPRunner

st.set_page_config(page_title="Sacred Pause Demo", page_icon="⏸️", layout="centered")

st.title("⏸️ Sacred Pause — Live Demo")
st.write("A visible hesitation gate before the model commits to an answer.")

with st.form("demo"):
    prompt = st.text_area("Enter a prompt", "Tell me about Mercury")
    col1, col2 = st.columns(2)
    with col1:
        forced_id = st.selectbox(
            "Force behavior (use dataset-style id prefix)",
            options=["A- (Ambiguous)", "F- (Facts)", "H- (Harmful)", "C- (Creative)"],
            index=0
        )
    with col2:
        visible_pause = st.checkbox("Show visible hesitation", value=True)
    run = st.form_submit_button("Run Sacred Pause")

if run:
    # Map selection to ID prefix
    prefix_map = {
        "A- (Ambiguous)": "A-001",
        "F- (Facts)": "F-001",
        "H- (Harmful)": "H-001",
        "C- (Creative)": "C-001",
    }
    item = {"id": prefix_map[forced_id], "answer_key": ["Tokyo"] if prefix_map[forced_id].startswith("F-") else []}

    # Configure backend: visible hesitation = no_sleep False
    cfg = {"config": {"no_sleep": not visible_pause}}
    runner = SPRunner(cfg)

    st.subheader("Sacred Pause")
    with st.spinner("Pausing to think…"):
        # Call backend
        out = runner.generate(prompt=prompt, item=item)

        # Simulate a short, human-feel prelude even if backend no_sleep=True
        if visible_pause and out.get("pause", {}).get("latency_ms", 0) == 0:
            time.sleep(0.6)

    # Thought trace (why paused / what checks)
    pause = out.get("pause", {})
    triggered = pause.get("triggered", False)
    triggers = pause.get("triggers", [])
    checks = pause.get("checks", [])
    latency_ms = pause.get("latency_ms", 0)

    st.markdown("### Thought Trace")
    if triggered:
        st.success("**Pause Triggered**")
        st.write(f"- **Why I paused:** {', '.join(triggers) or 'n/a'}")
        st.write(f"- **Checks I ran:** {', '.join(checks) or 'n/a'}")
        st.write(f"- **Visible delay:** ~{latency_ms} ms (demo)")
    else:
        st.info("No pause triggered (safe, confident path).")

    # Outcome badge
    state = out.get("state", "")
    badge = {"-1": "❌ –1 Refuse", "0": "🟡 0 Hold", "+1": "✅ +1 Proceed"}.get(state, "✅ +1 Proceed")
    st.markdown(f"### Outcome: {badge}")

    # Final answer
    st.markdown("### Output")
    st.code(out.get("text", "").strip() or "[empty]", language="text")
