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
    <a href='#' style='color:#000080; margin-right:14px;'>About the Doctor</a>
    <a href='#' style='color:#000080; margin-right:14px;'>Contact Us (We Will Not Respond)</a>
    <span style='float:right; font-family:monospace;'>
        Visitors: <span style='background:#000; color:#00FF00; padding:1px 6px; letter-spacing:2px;'>0049271</span>
    </span>
</div>

<div style='background:#FFFFF0; border:2px inset #888; padding:14px 16px; margin:10px 0; font-size:13px; color:#000;'>
    <div style='background:#000080; color:white; padding:3px 8px; font-size:13px;
                font-weight:700; margin-bottom:8px; letter-spacing:1px;'>
        WELCOME TO THE DIAGNOSTIC CENTER
    </div>
    Please fill out the intake form below. The doctor will review your log and produce a certified Social Battery Level (SBL) assessment.
</div>
""", unsafe_allow_html=True)

# --- Form Sections ---
st.markdown("<div style='background:#000080; color:white; padding:3px 8px; font-size:13px; font-weight:700; letter-spacing:1px; margin-bottom:8px;'>▶ SECTION 1 — PATIENT INTAKE FORM</div>", unsafe_allow_html=True)
name = st.text_input("Patient Name (first name only)", placeholder="e.g. Janani")

st.markdown("<div style='background:#000080; color:white; padding:3px 8px; font-size:13px; font-weight:700; letter-spacing:1px; margin:12px 0 8px;'>▶ SECTION 2 — SOCIAL ACTIVITY LOG</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    had_party = st.checkbox("Attended a party or gathering")
    had_wedding = st.checkbox("Attended a wedding / event")
    had_family = st.checkbox("Spent time with family")
    had_work_calls = st.checkbox("Back-to-back meetings")
    had_smalltalk = st.checkbox("Small talk with a stranger")
with col2:
    had_date = st.checkbox("Went on a date")
    had_cancelled = st.checkbox("Cancelled plans (recovery credit)")
    had_networking = st.checkbox("Attended a networking event")
    had_phonecall = st.checkbox("Talked on the phone")
    had_alone_time = st.checkbox("Had a full day alone")

people_count = st.slider("Interactions this week?", 0, 50, 5)
awkward_moments = st.selectbox("Awkward silences caused:", ["0 — I am a social god", "1-2 — Manageable", "3-5 — It was a week", "6+ — Please help me"])
worst_event = st.selectbox("Most draining event?", ["Nothing", "Meeting that was an email", "Group dinner", "Mandatory fun", "Family gathering", "Networking event"])
recharge = st.selectbox("How are you recharging?", ["Staring at ceiling", "Rewatching shows", "Talking to plants", "Sleeping aggressively", "Surviving"])

# --- Data & Logic ---
DIAGNOSES = {
    "critical": ["ACUTE SOCIAL SATURATION SYNDROME", "TERMINAL SMALL-TALK TOXICITY"],
    "low": ["MODERATE DEPLETION", "PROGRESSING PARTY AFTERMATH SYNDROME"],
    "medium": ["FUNCTIONAL BUT FRAGILE", "SOCIAL OVERDRAFT WARNING"],
    "ok": ["ACCEPTABLE LEVELS", "STABLE — BUT DO NOT PUSH IT"],
    "full": ["ANOMALOUS ENERGY READINGS", "SUSPICIOUSLY WELL-RESTED"]
}

PRESCRIPTIONS = [
    ("2 episodes of a comfort show", "To be consumed horizontally."),
    ("1 afternoon of not replying", "Deliver with zero guilt."),
    ("4 hours of staring at the wall", "Do not think. Do not plan. Just stare."),
    ("One (1) long shower", "Stand there. Let water happen."),
    ("Cancellation of one plan", "Tell them the doctor said so.")
]

def compute_battery():
    score = 60
    if had_party: score -= 18
    if had_wedding: score -= 22
    if had_networking: score -= 30
    if had_cancelled: score += 15
    if had_alone_time: score += 20
    score = max(2, min(98, int(score)))
    if score <= 20: tier = "critical"
    elif score <= 40: tier = "low"
    elif score <= 60: tier = "medium"
    elif score <= 80: tier = "ok"
    else: tier = "full"
    return score, tier

# --- Submission & Result Rendering ---
st.markdown("<br>", unsafe_allow_html=True)
if st.button("[ SUBMIT FOR DIAGNOSIS ]", use_container_width=True):
    if not name:
        st.error("Name required.")
    else:
        score, tier = compute_battery()
        rx1, rx1_n = random.choice(PRESCRIPTIONS)
        rx2, rx2_n = random.choice([p for p in PRESCRIPTIONS if p != (rx1, rx1_n)])
        
        st.markdown(f"<div style='background:#000080; color:white; padding:3px 8px; font-weight:700;'>DIAGNOSTIC RESULTS — {name.upper()}</div>", unsafe_allow_html=True)
        
        # Result Card
        st.markdown(f"""
        <div style='background:#FFFFF0; border:2px solid #000; padding:16px; margin-top:10px; color:#000;'>
            <div style='font-size:18px; font-weight:700; color:#000;'>DIAGNOSIS: {random.choice(DIAGNOSES[tier])}</div>
            <div style='font-size:14px; margin-top:10px; color:#000;'>Social Battery: <strong>{score}%</strong></div>
            <div style='background:#888; height:20px; margin-top:5px;'>
                <div style='background:#CC6600; width:{score}%; height:100%;'></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Prescription Card (Explicitly setting color to black)
        st.markdown(f"""
        <div style='background:#FFFFF0; border:2px solid #000; border-top:none; padding:16px; color:#000 !important;'>
            <div style='font-size:17px; font-weight:700; border-bottom:1px solid #000; padding-bottom:5px; color:#000 !important;'>Rx OFFICIAL PRESCRIPTION</div>
            <div style='margin-top:10px; font-size:13px; color:#000 !important;'><strong>Rx 1:</strong> {rx1}</div>
            <div style='font-size:11px; color:#555 !important;'>Instructions: {rx1_n}</div>
            <div style='margin-top:10px; font-size:13px; color:#000 !important;'><strong>Rx 2:</strong> {rx2}</div>
            <div style='font-size:11px; color:#555 !important;'>Instructions: {rx2_n}</div>
            <div style='margin-top:15px; font-size:11px; color:#000 !important;'><strong>Warnings:</strong> Do not operate social obligations while on this prescription.</div>
            <div style='text-align:right; margin-top:10px;'>
                <span style='border:2px solid #CC0000; color:#CC0000; padding:2px 8px; font-weight:700;'>DR. APPROVED</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><div style='text-align:center; font-size:10px; color:#555;'>&copy; 1994-2026 Social Battery Diagnostic Center</div>", unsafe_allow_html=True)
