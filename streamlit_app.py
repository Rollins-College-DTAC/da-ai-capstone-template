"""Placeholder dashboard. Claude Code replaces this in milestone 5.

Deploy it on setup night anyway, so the Streamlit Cloud connection is proven early.
"""
import os

import streamlit as st

st.set_page_config(page_title="Capstone", page_icon="📊")
st.title("My capstone dashboard")
st.write("Coming soon: live flow chart, step panels, MoE view, analytics and governance.")


def has(name):
    try:
        if st.secrets.get(name):
            return True
    except Exception:
        pass
    return bool(os.getenv(name))


st.subheader("Setup check")
for name in ["ANTHROPIC_API_KEY", "TURSO_DATABASE_URL", "TURSO_AUTH_TOKEN"]:
    st.write(("✅ " if has(name) else "⬜ ") + name)
st.caption("Shows only whether each secret is present, never its value.")
