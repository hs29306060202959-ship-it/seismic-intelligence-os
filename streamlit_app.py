"""Streamlit wrapper for the Aether Seismic — Intelligence OS.

The screens are the original interactive Stitch pages (unchanged). This file just
lets Streamlit Cloud serve them: it reads each `code.html` and renders it in a
full-width iframe. Navigation is via the sidebar (the pages' own cross-links can't
resolve inside Streamlit's sandboxed iframe, so we switch screens here instead).
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).parent

SCREENS = {
    "01 · Analytics Dashboard": "seismic_analytics_dashboard/code.html",
    "02 · Live Inference": "live_inference_aether_seismic/code.html",
    "03 · Prospect Intelligence AI": "prospect_intelligence_ai/code.html",
    "04 · Geological Report Viewer": "geological_report_viewer/code.html",
    "EX · 3D Experiment (three.js)": "three.js/code.html",
    "EX · Shader Study": "shader/code.html",
}

st.set_page_config(page_title="Aether Seismic — Intelligence OS", layout="wide")

# Trim Streamlit chrome so the screen fills the page.
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0.5rem 0.5rem 0 0.5rem; max-width: 100%;}
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("### Aether Seismic")
    st.caption("Seismic Intelligence OS")
    choice = st.radio("Screen", list(SCREENS.keys()), label_visibility="collapsed")
    height = st.slider("Viewport height (px)", 700, 2400, 1200, 50)
    st.caption("Screens load Tailwind, fonts, and three.js from CDNs — internet required.")

html_path = ROOT / SCREENS[choice]
if html_path.exists():
    components.html(html_path.read_text(encoding="utf-8"), height=height, scrolling=True)
else:
    st.error(f"Missing screen file: {SCREENS[choice]}")
