import streamlit as st
import random

st.set_page_config(page_title="Social Battery Diagnostic Center", page_icon="🩺", layout="centered")

# --- Custom CSS Styles ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Courier Prime', 'Courier New', monospace !important;
    background-color: #D4C9A8 !important;
    color: #1a1a1a !important;
}
.stApp {
    background-color: #D4C9A8;
    max-width: 780px;
    margin: 0 auto;
}
#MainMenu, footer, header { visibility: hidden; }

/* Text input */
div[data-testid="stTextInput"] input {
    font-family: 'Courier Prime', monospace !important;
    background: #FFFFF0 !important;
    border: 2px inset #888 !important;
    color: #000 !important;
    border-radius: 0 !important;
    font-size: 14px !important;
}

/* Selectbox */
div[data-baseweb="select"] {
    background: #FFFFF0 !important;
    border-radius: 0 !important;
}
div[data-baseweb="select"] > div {
    background: #FFFFF0 !important;
    border: 2px inset #888 !important;
    border-radius: 0 !important;
    font-family: 'Courier Prime', monospace !important;
    color: #000000 !important;
    font-size: 13px !important;
}

/* Buttons */
div[data-testid="stButton"] button {
    font-family: 'Courier Prime', monospace !important;
    font-weight: 700 !important;
    background: #C0C0C0 !important;
    border: 3px outset #ffffff !important;
    color: #000000 !important;
    border-radius: 0 !important;
    font-size: 14px !important;
    padding: 6px 18px !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}

.blink {
    animation: blinker 1s step-start infinite;
}
@keyframes blinker { 50% { opacity: 0; } }
</style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown("""
<div style='background:#000080; color:white; padding:10px 16px; border-bottom:3px solid #888;'>
    <div style='font-size:22px; font-weight:700; letter-spacing:1px;'>
        🩺 SOCIAL BATTERY DIAGNOSTIC CENTER
    </div>
    <div style='font-size:11px; color:#AAAAFF; margin-top:2px;'>
        Established 1994 &nbsp;|&nbsp; Dr. H. Introvert, MD, PhD, BRB &nbsp;|&nbsp;
        <span class='blink'>● ONLINE</span>
    </div>
</div>

<div style='background:#C0C0C0; border-bottom:2px solid #888; border-top:2px solid #fff;
            padding:4px 10px; font-size:12px; color:#000080;'>
    <a href='#' style='color:#000080; margin-right:14px;'>Home</a>
    <a href='#' style='color:#000080
