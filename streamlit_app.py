import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

# Page config (mobile-friendly)
st.set_page_config(
    page_title="💘",
    page_icon="💖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit UI elements (clean romantic look)
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Load your HTML file
html_path = Path("valentine.html")

if html_path.exists():
    html_content = html_path.read_text(encoding="utf-8")

    # Render HTML full screen
    components.html(
        html_content,
        height=800,     # increase if needed
        scrolling=False
    )
else:
    st.error("Valentine HTML file not found 💔")

