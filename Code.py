import streamlit as st
import random

st.set_page_config(page_title="Social Battery Diagnostic Center", page_icon="🩺", layout="centered")

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

/* Hide streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }

/* All text inputs */
div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input,
div[data-testid="stSelectbox"] select {
    font-family: 'Courier Prime', monospace !important;
    background: #FFFFF0 !important;
    border: 2px inset #888 !important;
    color: #000 !important;
    border-radius: 0 !important;
    font-size: 14px !important;
}

/* Sliders */
div[data-testid="stSlider"] {
    accent-color: #000080;
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
    cursor: pointer !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}
div[data-testid="stButton"] button:hover {
    background: #A0A0A0 !important;
    border: 3px inset #888 !important;
}
div[data-testid="stButton"] button:active {
    border: 3px inset #555 !important;
}

/* Checkboxes */
div[data-testid="stCheckbox"] label {
    font-family: 'Courier Prime', monospace !important;
    font-size: 13px !important;
}

/* Labels */
div[data-testid="stMarkdownContainer"] p,
label, .stCheckbox, .stSelectbox {
    font-family: 'Courier Prime', monospace !important;
    font-size: 13px !important;
}

/* Select boxes */
div[data-baseweb="select"] * {
    font-family: 'Courier Prime', monospace !important;
    background: #FFFFF0 !important;
    border-radius: 0 !important;
}

hr {
    border: none;
    border-top: 2px solid #888;
    margin: 8px 0;
}

.marquee-box {
    background: #000080;
    color: #FFFF00;
    font-family: 'Courier Prime', monospace;
    font-size: 13px;
    padding: 4px 8px;
    overflow: hidden;
    white-space: nowrap;
}

.site-header {
    background: #000080;
    color: white;
    padding: 10px 16px;
    border-bottom: 3px solid #888;
    margin-bottom: 0;
}

.site-title {
    font-size: 22px;
    font-weight: 700;
    color: white;
    letter-spacing: 1px;
}

.site-subtitle {
    font-size: 11px;
    color: #AAAAFF;
    margin-top: 2px;
}

.nav-bar {
    background: #C0C0C0;
    border-bottom: 2px solid #888;
    border-top: 2px solid #fff;
    padding: 4px 10px;
    font-size: 12px;
    color: #000080;
}

.nav-bar a {
    color: #000080;
    text-decoration: underline;
    margin-right: 14px;
    cursor: pointer;
}

.content-box {
    background: #FFFFF0;
    border: 2px inset #888;
    padding: 14px 16px;
    margin: 10px 0;
    font-size: 13px;
}

.section-header {
    background: #000080;
    color: white;
    padding: 3px 8px;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 8px;
    letter-spacing: 1px;
}

.result-box {
    background: #FFFFF0;
    border: 2px inset #555;
    padding: 16px;
    margin: 10px 0;
}

.result-critical {
    background: #FFF0F0;
    border: 2px inset #CC0000;
}

.result-warning {
    background: #FFFDE0;
    border: 2px inset #888800;
}

.result-ok {
    background: #F0FFF0;
    border: 2px inset #006600;
}

.battery-bar-outer {
    background: #888;
    border: 2px inset #555;
    height: 28px;
    width: 100%;
    margin: 8px 0;
    position: relative;
}

.blink {
    animation: blinker 1s step-start infinite;
}
@keyframes blinker { 50% { opacity: 0; } }

.counter-badge {
    display: inline-block;
    background: #FF0000;
    color: white;
    font-size: 11px;
    padding: 1px 5px;
    font-weight: 700;
    margin-left: 4px;
}

.small-print {
    font-size: 10px;
    color: #555;
    margin-top: 4px;
}

.divider-text {
    text-align: center;
    font-size: 12px;
    color: #555;
    margin: 6px 0;
}

.prescription-box {
    background: #FFFFF0;
    border: 2px solid #000;
    padding: 14px;
    margin: 10px 0;
    position: relative;
}

.rx-header {
    font-size: 18px;
    font-weight: 700;
    border-bottom: 1px solid #000;
    padding-bottom: 4px;
    margin-bottom: 8px;
}

.stamp {
    display: inline-block;
    border: 3px solid #CC0000;
    color: #CC0000;
    font-size: 16px;
    font-weight: 700;
    padding: 2px 10px;
    transform: rotate(-8deg);
    margin-top: 8px;
    letter-spacing: 2px;
}

.visitor-counter {
    font-size: 11px;
    background: #000;
    color: #00FF00;
    padding: 2px 8px;
    display: inline-block;
    letter-spacing: 2px;
}
</style>

<!-- Header -->
<div class='site-header'>
    <div class='site-title'>🩺 SOCIAL BATTERY DIAGNOSTIC CENTER</div>
    <div class='site-subtitle'>
        Established 1994 &nbsp;|&nbsp; Dr. H. Introvert, MD, PhD, BRB &nbsp;|&nbsp;
        <span class='blink'>● ONLINE</span>
    </div>
</div>

<div class='nav-bar'>
    <a href='#'>Home</a>
    <a href='#'>About the Doctor</a>
    <a href='#'>Patient Testimonials</a>
    <a href='#'>Contact Us (We Will Not Respond)</a>
    &nbsp;&nbsp;&nbsp;
    <span style='float:right;'>
        Visitors: <span class='visitor-counter'>0049271</span>
    </span>
</div>

<div class='marquee-box'>
    *** IMPORTANT NOTICE: This diagnostic tool is certified by the International Board of People Who Are Tired. Results are legally binding. *** NEW: Now accepting walk-ins (please do not walk in) ***
</div>
""", unsafe_allow_html=True)

# ── Intro blurb ───────────────────────────────────────────────────────────────
st.markdown("""
<div class='content-box'>
    <div class='section-header'>WELCOME TO THE DIAGNOSTIC CENTER</div>
    <p>
    Thank you for visiting. Please fill out the intake form below <em>honestly</em>.
    The doctor will review your social activity log and produce a certified assessment
    of your current Social Battery Level (SBL), along with a personalised recovery plan.<br><br>
    <strong>NOTE:</strong> This service is free. Do not ask why. Do not make eye contact with the website.
    </p>
    <p class='small-print'>
    * Results are 94.7% accurate. The other 5.3% is your fault. By proceeding you agree to our Terms &amp;
    Conditions (we also have not read them). Dr. Introvert accepts no responsibility for
    outcomes, feelings, or eye contact made during this session.
    </p>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  INTAKE FORM
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("<div class='section-header'>▶ SECTION 1 — PATIENT INTAKE FORM</div>", unsafe_allow_html=True)

name = st.text_input("Patient Name (first name only, we don't need more)", placeholder="e.g. Dave")

st.markdown("<div class='section-header'>▶ SECTION 2 — SOCIAL ACTIVITY LOG (past 7 days)</div>", unsafe_allow_html=True)

st.markdown("<div class='content-box'>", unsafe_allow_html=True)
st.markdown("**Please check all that apply:**")

col1, col2 = st.columns(2)
with col1:
    had_party       = st.checkbox("Attended a party or gathering")
    had_wedding     = st.checkbox("Attended a wedding / birthday / event")
    had_family      = st.checkbox("Spent time with family (involuntary counts double)")
    had_work_calls  = st.checkbox("Back-to-back work calls / meetings")
    had_smalltalk   = st.checkbox("Made small talk with a stranger")
with col2:
    had_date        = st.checkbox("Went on a date")
    had_cancelled   = st.checkbox("Cancelled plans last minute (recovery credit)")
    had_networking  = st.checkbox("Attended a 'networking' event (God help you)")
    had_phonecall   = st.checkbox("Talked on the phone (not texted — actually called)")
    had_alone_time  = st.checkbox("Had at least one full day completely alone")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='section-header'>▶ SECTION 3 — SEVERITY ASSESSMENT</div>", unsafe_allow_html=True)

people_count = st.slider(
    "How many different people did you interact with this week?",
    0, 50, 5,
    help="Cashiers count. So does your dentist."
)

awkward_moments = st.selectbox(
    "Number of awkward silences you personally caused:",
    ["0 — I am a social god", "1-2 — Manageable", "3-5 — It was a week", "6+ — Please help me"]
)

worst_event = st.selectbox(
    "What was your most draining event this week?",
    [
        "Nothing, I stayed home (suspicious)",
        "A meeting that was definitely an email",
        "A group dinner with people I half-know",
        "A work event with mandatory fun",
        "A family gathering with unsolicited opinions",
        "A party where I didn't know anyone",
        "A networking event (selecting this adds 50 damage points)",
    ]
)

recharge = st.selectbox(
    "How have you been recharging?",
    [
        "Lying on the floor staring at the ceiling",
        "Watching the same show for the 4th time",
        "Talking to my pet / plant / houseplant I named",
        "Online shopping without buying anything",
        "Sleeping aggressively",
        "I have not been recharging. I have been surviving.",
    ]
)
st.markdown("</div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  DIAGNOSIS ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

DIAGNOSES = {
    "critical": [
        "ACUTE SOCIAL SATURATION SYNDROME (ASSS)",
        "SEVERE INTERPERSONAL OVEREXPOSURE DISORDER",
        "TERMINAL SMALL-TALK TOXICITY (STAGE 4)",
        "CHRONIC PEOPLE POISONING — ADVANCED",
    ],
    "low": [
        "MODERATE SOCIAL BATTERY DEPLETION",
        "SUBACUTE HUMAN INTERACTION FATIGUE",
        "MILD-TO-MODERATE CROWD EXHAUSTION",
        "PROGRESSING PARTY AFTERMATH SYNDROME",
    ],
    "medium": [
        "BORDERLINE SOCIAL CAPACITY (BSC)",
        "PRE-INTROVERT COLLAPSE SYNDROME",
        "FUNCTIONAL BUT FRAGILE (FBF) — WATCH CLOSELY",
        "SOCIAL OVERDRAFT WARNING",
    ],
    "ok": [
        "ACCEPTABLE BATTERY LEVELS DETECTED",
        "STABLE — BUT DO NOT PUSH IT",
        "WITHIN NORMAL PARAMETERS (BARELY)",
        "CAUTIOUSLY OPERATIONAL",
    ],
    "full": [
        "ANOMALOUS ENERGY READINGS — RECHECK INPUTS",
        "SUSPICIOUSLY WELL-RESTED — FURTHER TESTS NEEDED",
        "FULL CHARGE DETECTED — DOCTOR IS CONCERNED",
        "YOU ARE FINE. THIS IS UNUSUAL. WE'LL MONITOR YOU.",
    ]
}

PRESCRIPTIONS = [
    ("2 full episodes of a comfort show", "To be consumed horizontally, snacks mandatory."),
    ("1 afternoon of not replying to anyone", "Deliver with zero guilt. Side effects: peace."),
    ("Exactly 4 hours of staring at the wall", "Do not think. Do not plan. Just stare."),
    ("One (1) long shower with no agenda", "Stand there. Let water happen to you."),
    ("A hot beverage consumed in complete silence", "No podcasts. No phone. Just you and the mug."),
    ("A full day in your pyjamas", "Diagnostic dose: 24 hours. Do not get dressed."),
    ("One nap, minimum 47 minutes", "Set an alarm but ignore it."),
    ("A walk with no destination", "Not for exercise. Just to exist outside briefly."),
    ("Complete cancellation of one upcoming plan", "For therapeutic purposes. Tell them the doctor said so."),
    ("Three hours of a hobby nobody knows about", "Bring no one. Tell no one. This is yours."),
]

DOCTOR_NOTES = {
    "critical": [
        "Patient has clearly overcommitted to being perceived. Immediate rest advised. Do not RSVP to anything for 14 days.",
        "In my 30 years of practice I have not seen readings this low. Patient is advised to disappear for the weekend.",
        "The human body was not designed for this many group chats. I am genuinely concerned. Go home.",
        "This is a public health matter. Patient must be isolated from all further social obligations.",
    ],
    "low": [
        "Patient is running on fumes and politeness. This is not sustainable. The doctor is watching.",
        "Mild concern. Patient should cancel at least one thing this week. Any one thing. Pick something.",
        "Battery is depleted but not critical. Patient is advised to become mysteriously unavailable for 48 hours.",
        "Readings suggest patient has been saying 'yes' to things they did not want to attend. This must stop.",
    ],
    "medium": [
        "Patient is technically functional. This does not mean they should do more things. It means they should do fewer things.",
        "Borderline. The doctor recommends patient stop accepting invitations on a trial basis and report back.",
        "Stable but fragile. Like a phone at 12%. Do not open any more apps.",
        "Patient is managing. Barely. The doctor has seen this before. It does not end well.",
    ],
    "ok": [
        "Readings are acceptable. Do not interpret this as a green light. It is a yellow light. Proceed slowly.",
        "Patient is doing fine. The doctor finds this mildly suspicious but will not investigate further.",
        "You are okay. This week. Do not schedule anything for next week. Let's not get cocky.",
        "Normal levels. The doctor recommends maintaining current antisocial habits.",
    ],
    "full": [
        "Patient's readings are dangerously high. Either they have been alone for weeks or they are lying on this form.",
        "Full charge. Unprecedented. The doctor will be publishing a paper about this case.",
        "These numbers cannot be right. Please retake the assessment after attending one (1) mandatory team lunch.",
        "Patient reports feeling fine. The doctor does not believe them but appreciates the optimism.",
    ]
}

WARNING_LABELS = {
    "critical": "⚠ CRITICAL — DO NOT MAKE EYE CONTACT WITH ANYONE",
    "low":      "⚠ LOW — SOCIAL OBLIGATIONS SUSPENDED",
    "medium":   "⚡ MODERATE — PROCEED WITH CAUTION",
    "ok":       "✔ STABLE — MONITOR CLOSELY",
    "full":     "★ FULL — RECHECK INPUTS",
}

BAR_FILLS = {
    "critical": ("#CC0000", 8),
    "low":      ("#CC6600", 28),
    "medium":   ("#AAAA00", 52),
    "ok":       ("#006600", 75),
    "full":     ("#004488", 97),
}

def compute_battery(had_party, had_wedding, had_family, had_work_calls,
                    had_smalltalk, had_date, had_cancelled, had_networking,
                    had_phonecall, had_alone_time, people_count, awkward_moments,
                    worst_event, recharge):
    score = 60  # start at 60%

    if had_party:       score -= 18
    if had_wedding:     score -= 22
    if had_family:      score -= 20
    if had_work_calls:  score -= 15
    if had_smalltalk:   score -= 8
    if had_date:        score -= 12
    if had_networking:  score -= 30
    if had_phonecall:   score -= 10
    if had_cancelled:   score += 15
    if had_alone_time:  score += 20

    score -= min(people_count * 1.2, 30)

    awkward_penalty = {"0 — I am a social god": 0, "1-2 — Manageable": -5,
                       "3-5 — It was a week": -12, "6+ — Please help me": -22}
    score += awkward_penalty.get(awkward_moments, 0)

    if "networking" in worst_event: score -= 20
    elif "family" in worst_event:   score -= 15
    elif "mandatory fun" in worst_event: score -= 18
    elif "group dinner" in worst_event: score -= 12
    elif "meeting" in worst_event:  score -= 10
    elif "stayed home" in worst_event: score += 10

    if "floor" in recharge or "surviving" in recharge: score += 5
    else: score += 8

    score = max(2, min(98, int(score)))

    if score <= 15:   tier = "critical"
    elif score <= 35: tier = "low"
    elif score <= 55: tier = "medium"
    elif score <= 80: tier = "ok"
    else:             tier = "full"

    return score, tier

# ═══════════════════════════════════════════════════════════════════════════════
#  SUBMIT
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,2,1])
with col2:
    submit = st.button("[ SUBMIT FOR DIAGNOSIS ]", use_container_width=True)

if submit:
    if not name.strip():
        st.markdown("""
        <div class='content-box result-warning'>
            ⚠ ERROR: Patient name is required. The doctor cannot diagnose a ghost.
            (Or can he. He'd rather not.)
        </div>
        """, unsafe_allow_html=True)
    else:
        score, tier = compute_battery(
            had_party, had_wedding, had_family, had_work_calls,
            had_smalltalk, had_date, had_cancelled, had_networking,
            had_phonecall, had_alone_time, people_count, awkward_moments,
            worst_event, recharge
        )

        bar_color, bar_pct = BAR_FILLS[tier]
        diagnosis   = random.choice(DIAGNOSES[tier])
        doctor_note = random.choice(DOCTOR_NOTES[tier])
        warning     = WARNING_LABELS[tier]
        rx1, rx1_note = random.choice(PRESCRIPTIONS)
        rx2, rx2_note = random.choice([p for p in PRESCRIPTIONS if p[0] != rx1])

        result_class = {"critical":"result-critical","low":"result-warning",
                        "medium":"result-warning","ok":"result-ok","full":"result-ok"}[tier]

        st.markdown(f"""
        <br>
        <div class='section-header'>▶ DIAGNOSTIC RESULTS — PATIENT: {name.upper()}</div>

        <div class='content-box {result_class}'>
            <div style='font-size:11px; color:#555; margin-bottom:4px;'>
                SOCIAL BATTERY DIAGNOSTIC CENTER &nbsp;|&nbsp; REF: SBL-{random.randint(10000,99999)}
            </div>
            <div style='font-size:17px; font-weight:700; margin-bottom:6px;'>
                DIAGNOSIS: {diagnosis}
            </div>
            <div style='font-size:12px; margin-bottom:10px; color:#333;'>
                STATUS: <strong>{warning}</strong>
            </div>

            <div style='font-size:12px; margin-bottom:4px;'>
                SOCIAL BATTERY LEVEL (SBL): <strong>{score}%</strong>
            </div>
            <div class='battery-bar-outer'>
                <div style='background:{bar_color}; width:{bar_pct}%; height:100%;
                            display:flex; align-items:center; justify-content:center;
                            color:white; font-size:11px; font-weight:700;'>
                    {"█" * (bar_pct // 8)} {score}%
                </div>
            </div>

            <hr>
            <div style='font-size:12px; margin-top:8px;'>
                <strong>DOCTOR'S CLINICAL NOTE:</strong><br>
                {doctor_note}
            </div>
        </div>

        <div class='prescription-box'>
            <div class='rx-header'>℞ &nbsp; OFFICIAL PRESCRIPTION</div>
            <div style='font-size:12px;'>
                <strong>Patient:</strong> {name} &nbsp;&nbsp;
                <strong>Date:</strong> Today (The doctor does not know what day it is)<br><br>
                <strong>Rx 1:</strong> {rx1}<br>
                <em style='font-size:11px; color:#555;'>Sig: {rx1_note}</em><br><br>
                <strong>Rx 2:</strong> {rx2}<br>
                <em style='font-size:11px; color:#555;'>Sig: {rx2_note}</em><br><br>
                <strong>Refills:</strong> Unlimited. Take as needed. Take more than needed.<br>
                <strong>Warnings:</strong> Do not operate social obligations while using this prescription.
            </div>
            <div style='text-align:right; margin-top:10px;'>
                <span class='stamp'>DR. APPROVED</span>
            </div>
        </div>

        <div class='content-box' style='font-size:11px; color:#555;'>
            <strong>DISCLAIMER:</strong> This diagnosis is certified by the International Board of
            People Who Just Need a Minute. Results valid for 7 days or until someone invites you
            to something, whichever comes first. The doctor is not responsible for any plans you
            cancel as a result of this report. That was going to happen anyway.
            <br><br>
            <div style='text-align:center;'>
                ★ RATE THIS DIAGNOSIS: [Excellent] [Very Good] [Good] [Why Did I Come Here]
            </div>
        </div>
        """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<br>
<div style='border-top:2px solid #888; padding-top:8px; font-size:10px; color:#555; text-align:center;'>
    © 1994–2026 Social Battery Diagnostic Center &nbsp;|&nbsp;
    Best viewed in Netscape Navigator 2.0 at 800×600 &nbsp;|&nbsp;
    <span class='blink'>NEW</span> Now Y2K compliant &nbsp;|&nbsp;
    Dr. Introvert is not a real doctor. Results are not real results. You knew this.
</div>
<br>
""", unsafe_allow_html=True)
