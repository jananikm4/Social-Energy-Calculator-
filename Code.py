import streamlit as st
import random

st.set_page_config(page_title="Social Battery Diagnostic Center", page_icon="🩺", layout="centered")

# ── Random jump scare on load ─────────────────────────────────────────────────
if "jump_scare_roll" not in st.session_state:
    st.session_state.jump_scare_roll = random.random()
if st.session_state.jump_scare_roll < 0.4:
    SCARES = [
        "⚠ WARNING: A wild extrovert has been detected in your vicinity. Stay calm. Do not make eye contact. This message will not repeat. (It might repeat.)",
        "⚠ ALERT: Someone nearby just said 'we should hang out sometime' and meant it. Brace yourself.",
        "⚠ CAUTION: An unread group chat notification is approaching. The doctor recommends looking away.",
        "⚠ NOTICE: Someone just replied 'K' to your paragraph. The doctor is aware. The doctor is also angry.",
    ]
    scare_idx = int(st.session_state.jump_scare_roll * 10) % len(SCARES)
    st.error(SCARES[scare_idx])

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

div[data-testid="stTextInput"] input {
    font-family: 'Courier Prime', monospace !important;
    background: #FFFFF0 !important;
    border: 2px inset #888 !important;
    color: #000 !important;
    border-radius: 0 !important;
    font-size: 14px !important;
}
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
div[data-baseweb="select"] span { color: #000000 !important; font-family: 'Courier Prime', monospace !important; }
ul[data-baseweb="menu"] { background: #FFFFF0 !important; border: 2px solid #888 !important; border-radius: 0 !important; }
ul[data-baseweb="menu"] li { background: #FFFFF0 !important; color: #000 !important; font-family: 'Courier Prime', monospace !important; font-size: 13px !important; }
ul[data-baseweb="menu"] li:hover { background: #000080 !important; color: white !important; }

div[data-testid="stSlider"] { accent-color: #000080; }
div[data-testid="stSlider"] label { color: #1a1a1a !important; font-family: 'Courier Prime', monospace !important; font-size: 13px !important; }

div[data-testid="stButton"] button {
    font-family: 'Courier Prime', monospace !important;
    font-weight: 700 !important;
    background: #C0C0C0 !important;
    border: 3px outset #ffffff !important;
    color: #000000 !important;
    border-radius: 0 !important;
    font-size: 13px !important;
    padding: 6px 18px !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}
div[data-testid="stButton"] button:hover { background: #A0A0A0 !important; border: 3px inset #888 !important; }

div[data-testid="stCheckbox"] label p { font-family: 'Courier Prime', monospace !important; font-size: 13px !important; color: #1a1a1a !important; }
label p, div[data-testid="stMarkdownContainer"] p { font-family: 'Courier Prime', monospace !important; color: #1a1a1a !important; }
div[data-testid="stSelectbox"] label p { font-family: 'Courier Prime', monospace !important; font-size: 13px !important; color: #1a1a1a !important; }

/* Force all markdown HTML text black, with exceptions */
div[data-testid="stMarkdownContainer"] div,
div[data-testid="stMarkdownContainer"] span:not([style*="color:#CC0000"]):not([style*="color:#00FF00"]):not([style*="color:#FFFF00"]):not([style*="color:#AAAAFF"]),
div[data-testid="stMarkdownContainer"] p,
div[data-testid="stMarkdownContainer"] strong,
div[data-testid="stMarkdownContainer"] em {
    color: #1a1a1a !important;
    font-family: 'Courier Prime', monospace !important;
}
/* White text on dark bg elements */
div[data-testid="stMarkdownContainer"] div[style*="background:#000080"],
div[data-testid="stMarkdownContainer"] div[style*="background:#000080"] div,
div[data-testid="stMarkdownContainer"] div[style*="background:#000080"] span,
div[data-testid="stMarkdownContainer"] div[style*="background:#000080"] a { color: white !important; }
div[data-testid="stMarkdownContainer"] div[style*="background:#C0C0C0"],
div[data-testid="stMarkdownContainer"] div[style*="background:#C0C0C0"] a { color: #000080 !important; }
div[data-testid="stMarkdownContainer"] div[style*="background:#CC0000"],
div[data-testid="stMarkdownContainer"] div[style*="background:#CC0000"] span { color: white !important; }
div[data-testid="stMarkdownContainer"] div[style*="background:#006600"],
div[data-testid="stMarkdownContainer"] div[style*="background:#006600"] span { color: white !important; }
div[data-testid="stMarkdownContainer"] div[style*="background:#CC6600"],
div[data-testid="stMarkdownContainer"] div[style*="background:#CC6600"] span { color: white !important; }
div[data-testid="stMarkdownContainer"] div[style*="background:#AAAA00"],
div[data-testid="stMarkdownContainer"] div[style*="background:#AAAA00"] span { color: white !important; }
div[data-testid="stMarkdownContainer"] div[style*="background:#004488"],
div[data-testid="stMarkdownContainer"] div[style*="background:#004488"] span { color: white !important; }
div[data-testid="stMarkdownContainer"] div[style*="color:#FFFF00"] { color: #FFFF00 !important; }
div[data-testid="stMarkdownContainer"] div[style*="color:#AAAAFF"],
div[data-testid="stMarkdownContainer"] div[style*="color:#AAAAFF"] span { color: #AAAAFF !important; }
div[data-testid="stMarkdownContainer"] span[style*="background:#000"] { color: #00FF00 !important; }

.blink { animation: blinker 1s step-start infinite; }
@keyframes blinker { 50% { opacity: 0; } }

/* CSS ticker tape — replaces marquee */
.ticker-text {
    display: inline-block;
    white-space: nowrap;
    color: #FFFF00;
    font-size: 13px;
    font-family: 'Courier Prime', monospace;
    font-weight: 700;
    animation: ticker 32s linear infinite;
}
@keyframes ticker {
    0%   { transform: translateX(900px); }
    100% { transform: translateX(-2000px); }
}

/* Under construction stripe */
.under-construction {
    background: repeating-linear-gradient(
        45deg, #FFD700, #FFD700 10px, #000 10px, #000 20px
    );
    color: #FFD700;
    font-weight: 700;
    font-size: 12px;
    text-align: center;
    padding: 5px;
    letter-spacing: 2px;
    border-top: 2px solid #888;
    border-bottom: 2px solid #888;
    animation: blinker 1.2s step-start infinite;
    font-family: 'Courier Prime', monospace;
}

.odometer {
    font-family: 'Courier Prime', monospace;
    background: #000;
    color: #00FF00;
    border: 3px inset #333;
    padding: 2px 10px;
    letter-spacing: 4px;
    font-size: 14px;
    font-weight: 700;
    display: inline-block;
    box-shadow: inset 0 0 8px #00FF00;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style='background:#000080; color:white; padding:10px 16px; border-bottom:3px solid #888;'>
    <div style='font-size:22px; font-weight:700; letter-spacing:1px; color:white;'>
        🩺 SOCIAL BATTERY DIAGNOSTIC CENTER
    </div>
    <div style='font-size:11px; color:#AAAAFF; margin-top:2px;'>
        Established 1994 &nbsp;|&nbsp; Dr. H. Introvert, MD, PhD, BRB &nbsp;|&nbsp;
        <span class='blink' style='color:#AAAAFF;'>● ONLINE</span>
    </div>
</div>

<div style='background:#C0C0C0; border-bottom:2px solid #888; border-top:2px solid #fff;
            padding:4px 10px; font-size:12px;'>
    <a href='#' style='color:#000080; margin-right:14px; text-decoration:underline;'>Home</a>
    <a href='#' style='color:#000080; margin-right:14px; text-decoration:underline;'>About the Doctor</a>
    <a href='#' style='color:#000080; margin-right:14px; text-decoration:underline;'>Patient Testimonials</a>
    <a href='#' style='color:#000080; margin-right:14px; text-decoration:underline;'>Contact Us (We Will Not Respond)</a>
    <span style='float:right;'>
        Visitors: <span class='odometer'>0049271</span>
    </span>
</div>

<div style='background:#000080; overflow:hidden; padding:6px 0; border-bottom:2px solid #333;'>
    <div class='ticker-text'>
        *** WARNING: LOW BATTERY EMERGENCIES SHOULD REPORT TO THE NEAREST BEDROOM ***
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        *** IMPORTANT: Certified by the International Board of People Who Are Tired ***
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        *** NEW: Now accepting walk-ins (please do not walk in) ***
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        *** REMINDER: Eye contact with this website is strongly discouraged ***
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    </div>
</div>

<div style='background:#FFFFF0; border:2px inset #888; padding:14px 16px; margin:10px 0; font-size:13px;'>
    <div style='background:#000080; color:white; padding:3px 8px; font-size:13px;
                font-weight:700; margin-bottom:8px; letter-spacing:1px;'>
        WELCOME TO THE DIAGNOSTIC CENTER
    </div>
    Thank you for visiting. Please fill out the intake form below <em>honestly</em>.
    The doctor will review your social activity log and produce a certified assessment
    of your current Social Battery Level (SBL), along with a personalised recovery plan.<br><br>
    <strong>NOTE:</strong> This service is free. Do not ask why. Do not make eye contact with the website.
    <br><br>
    <span style='font-size:10px; color:#555;'>
        * Results are 94.7% accurate. The other 5.3% is your fault. By proceeding you agree to our
        Terms &amp; Conditions (we also have not read them). Dr. Introvert accepts no responsibility
        for outcomes, feelings, or eye contact made during this session.
    </span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='under-construction'>
    🚧 &nbsp; THIS PAGE IS UNDER CONSTRUCTION &nbsp; 🚧 &nbsp;
    PLEASE CHECK BACK IN 1998 &nbsp; 🚧
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  FORM
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("<div style='background:#000080; color:white; padding:3px 8px; font-size:13px; font-weight:700; letter-spacing:1px; margin-bottom:8px; margin-top:10px;'>▶ SECTION 1 — PATIENT INTAKE FORM</div>", unsafe_allow_html=True)
name = st.text_input("Patient Name (first name only, we don't need more)", placeholder="e.g. Dave")

# Name validation — penalise full names
name_penalty = 0
name_warning = ""
if name.strip():
    if " " in name.strip():
        name_warning = "⚠ We said first name only. We are deducting 5% for making us read two names. The doctor is sighing."
        name_penalty = -5
    elif len(name.strip()) > 12:
        name_warning = "⚠ That is a very long name. The doctor had to stand up to read it. Deducting 3% for the inconvenience."
        name_penalty = -3
if name_warning:
    st.markdown(f"<div style='background:#FFFDE0; border:2px inset #888800; padding:8px 12px; font-size:12px; color:#1a1a1a;'>{name_warning}</div>", unsafe_allow_html=True)

st.markdown("<div style='background:#000080; color:white; padding:3px 8px; font-size:13px; font-weight:700; letter-spacing:1px; margin:12px 0 8px;'>▶ SECTION 2 — SOCIAL ACTIVITY LOG (past 7 days)</div>", unsafe_allow_html=True)
st.markdown("<div style='background:#FFFFF0; border:2px inset #888; padding:10px 16px; margin:0 0 6px; font-size:13px;'><strong>Please check all that apply:</strong></div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    had_party      = st.checkbox("Attended a party or gathering")
    had_wedding    = st.checkbox("Attended a wedding / birthday / event")
    had_family     = st.checkbox("Spent time with family (involuntary counts double)")
    had_work_calls = st.checkbox("Back-to-back work calls / meetings")
    had_smalltalk  = st.checkbox("Made small talk with a stranger")
    had_waiter     = st.checkbox('Said "You too" after waiter said "enjoy your meal"')
    had_wave       = st.checkbox("Waved back at someone waving at the person behind you")
with col2:
    had_date       = st.checkbox("Went on a date")
    had_networking = st.checkbox("Attended a 'networking' event (God help you)")
    had_phonecall  = st.checkbox("Talked on the phone (not texted — actually called)")
    had_relative   = st.checkbox("Had to explain your job to an older relative")
    had_lie        = st.checkbox("Fabricated an elaborate excuse to escape a text conversation")
    had_cancelled  = st.checkbox("Cancelled plans last minute (+15% recovery credit)")
    had_ghosted    = st.checkbox("Left a party without saying goodbye to anyone (+20% Ghost Credit)")
    had_cancelled_on = st.checkbox("The other person cancelled on YOU (+50% Jackpot Credit 🎰)")
    had_alone_time = st.checkbox("Had at least one full day completely alone (+20%)")

st.markdown("<div style='background:#000080; color:white; padding:3px 8px; font-size:13px; font-weight:700; letter-spacing:1px; margin:12px 0 8px;'>▶ SECTION 3 — SEVERITY ASSESSMENT</div>", unsafe_allow_html=True)

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

# ═══════════════════════════════════════════════════════════════════════════════
#  DATA
# ═══════════════════════════════════════════════════════════════════════════════
DIAGNOSES = {
    "critical": ["ACUTE SOCIAL SATURATION SYNDROME (ASSS)",
                 "SEVERE INTERPERSONAL OVEREXPOSURE DISORDER",
                 "TERMINAL SMALL-TALK TOXICITY (STAGE 4)",
                 "CHRONIC PEOPLE POISONING — ADVANCED"],
    "low":      ["MODERATE SOCIAL BATTERY DEPLETION",
                 "SUBACUTE HUMAN INTERACTION FATIGUE",
                 "MILD-TO-MODERATE CROWD EXHAUSTION",
                 "PROGRESSING PARTY AFTERMATH SYNDROME"],
    "medium":   ["BORDERLINE SOCIAL CAPACITY (BSC)",
                 "PRE-INTROVERT COLLAPSE SYNDROME",
                 "FUNCTIONAL BUT FRAGILE (FBF) — WATCH CLOSELY",
                 "SOCIAL OVERDRAFT WARNING"],
    "ok":       ["ACCEPTABLE BATTERY LEVELS DETECTED",
                 "STABLE — BUT DO NOT PUSH IT",
                 "WITHIN NORMAL PARAMETERS (BARELY)",
                 "CAUTIOUSLY OPERATIONAL"],
    "full":     ["ANOMALOUS ENERGY READINGS — EXTROVERTED PSYCHOPATHY SUSPECTED",
                 "SUSPICIOUSLY WELL-RESTED — FURTHER TESTS NEEDED",
                 "FULL CHARGE DETECTED — DOCTOR IS UNCOMFORTABLE",
                 "YOU ARE FINE. THIS IS UNUSUAL. PLEASE LEAVE THE WEBSITE."],
}

PRESCRIPTIONS = [
    ("2 full episodes of a comfort show",          "To be consumed horizontally. Snacks mandatory."),
    ("1 afternoon of not replying to anyone",       "Deliver with zero guilt. Side effects: peace."),
    ("Exactly 4 hours of staring at the wall",      "Do not think. Do not plan. Just stare."),
    ("One (1) long shower with no agenda",          "Stand there. Let water happen to you."),
    ("A hot beverage consumed in complete silence", "No podcasts. No phone. Just you and the mug."),
    ("A full day in your pyjamas",                  "Diagnostic dose: 24 hours. Do not get dressed."),
    ("One nap, minimum 47 minutes",                 "Set an alarm but ignore it."),
    ("A walk with no destination",                  "Not for exercise. Just to exist outside briefly."),
    ("Cancellation of one upcoming plan",           "For therapeutic purposes. Tell them the doctor said so."),
    ("Three hours of a hobby nobody knows about",   "Bring no one. Tell no one. This is yours."),
    ("One (1) pizza. Eaten alone. In silence.",     "Do not share. This is medicine."),
    ("A weighted blanket and zero responsibilities","Wrap yourself in it. Become the blanket."),
]

DOCTOR_NOTES = {
    "critical": [
        "CRITICAL. DO NOT MOVE. If someone speaks to you, hiss loudly.",
        "Patient has clearly overcommitted to being perceived. Do not RSVP to anything for 14 days. Actually, cancel everything.",
        "In 30 years of practice I have not seen readings this low. Patient is ordered to disappear until further notice.",
        "This is a public health matter. Patient must be isolated from all further social obligations. Immediately. Go.",
    ],
    "low": [
        "Patient is running on fumes and politeness. This is not sustainable. The doctor is watching.",
        "Battery depleted but not critical. Patient advised to become mysteriously unavailable for 48 hours.",
        "Readings suggest patient has been saying yes to things they did not want to attend. This must stop today.",
        "Mild concern. Cancel at least one thing this week. Any one thing. Do not overthink which one. Cancel.",
    ],
    "medium": [
        "Patient is technically functional. This does not mean they should do more things. It means fewer things.",
        "Stable but fragile. Like a phone at 12%. Do not open any more apps. Do not accept any more invitations.",
        "Borderline. The doctor recommends patient stop accepting invitations on a trial basis and report back in 7 days.",
        "Patient is managing. Barely. The doctor has seen this before. It does not end well unless they cancel something.",
    ],
    "ok": [
        "Readings are acceptable. Do not interpret this as a green light. It is a yellow light. Proceed slowly.",
        "Patient is doing fine. The doctor finds this mildly suspicious but will not investigate further at this time.",
        "You are okay. This week. Do not schedule anything for next week. Let us not get cocky about this.",
        "Normal levels. The doctor recommends maintaining current antisocial habits. They are working.",
    ],
    "full": [
        "DIAGNOSIS: Extroverted Psychopathy. The doctor is uncomfortable with your energy levels. Please leave the website.",
        "Full charge. Unprecedented. The doctor will be publishing a paper about this. You will not be named. Probably.",
        "These numbers cannot be right. Please retake after attending one (1) mandatory team lunch and report back.",
        "Patient reports feeling fine. The doctor does not believe them. No one who is fine has ever used this website.",
    ],
}

WARNING_LABELS = {
    "critical": "STATUS: CRITICAL — DO NOT MAKE EYE CONTACT WITH ANYONE",
    "low":      "STATUS: LOW — SOCIAL OBLIGATIONS SUSPENDED",
    "medium":   "STATUS: MODERATE — PROCEED WITH CARE",
    "ok":       "STATUS: STABLE — MONITOR CLOSELY",
    "full":     "STATUS: FULL CHARGE — RECHECK INPUTS",
}

BAR_FILLS = {
    "critical": ("#CC0000", 8),
    "low":      ("#CC6600", 28),
    "medium":   ("#AAAA00", 52),
    "ok":       ("#006600", 75),
    "full":     ("#004488", 97),
}

RESULT_COLORS = {
    "critical": ("#FFF0F0", "#CC0000"),
    "low":      ("#FFFDE0", "#888800"),
    "medium":   ("#FFFDE0", "#666600"),
    "ok":       ("#F0FFF0", "#006600"),
    "full":     ("#F0F0FF", "#000080"),
}

def compute_battery(had_party, had_wedding, had_family, had_work_calls, had_smalltalk,
                    had_waiter, had_wave, had_date, had_networking, had_phonecall,
                    had_relative, had_lie, had_cancelled, had_ghosted, had_cancelled_on,
                    had_alone_time, people_count, awkward_moments, worst_event, recharge,
                    name_penalty=0):
    score = 60
    if had_party:        score -= 18
    if had_wedding:      score -= 22
    if had_family:       score -= 20
    if had_work_calls:   score -= 15
    if had_smalltalk:    score -= 8
    if had_waiter:       score -= 15
    if had_wave:         score -= 20
    if had_date:         score -= 12
    if had_networking:   score -= 30
    if had_phonecall:    score -= 10
    if had_relative:     score -= 14
    if had_lie:          score -= 8
    if had_cancelled:    score += 15
    if had_ghosted:      score += 20
    if had_cancelled_on: score += 50
    if had_alone_time:   score += 20
    score -= min(people_count * 1.2, 30)
    awkward_penalty = {"0 — I am a social god": 0, "1-2 — Manageable": -5,
                       "3-5 — It was a week": -12, "6+ — Please help me": -22}
    score += awkward_penalty.get(awkward_moments, 0)
    if "networking" in worst_event:      score -= 20
    elif "family" in worst_event:        score -= 15
    elif "mandatory fun" in worst_event: score -= 18
    elif "group dinner" in worst_event:  score -= 12
    elif "meeting" in worst_event:       score -= 10
    elif "stayed home" in worst_event:   score += 10
    if "floor" in recharge or "surviving" in recharge: score += 5
    else: score += 8
    score += name_penalty
    score = max(2, min(99, int(score)))
    if score <= 10:   tier = "critical"
    elif score <= 35: tier = "low"
    elif score <= 55: tier = "medium"
    elif score <= 80: tier = "ok"
    else:             tier = "full"
    return score, tier

# ═══════════════════════════════════════════════════════════════════════════════
#  SUBMIT
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    submit = st.button("[ SUBMIT FOR DIAGNOSIS ]", use_container_width=True)

if submit:
    if not name.strip():
        st.session_state.result = None
        st.session_state.error  = True
        st.session_state.networking_override = False
    else:
        score, tier = compute_battery(
            had_party, had_wedding, had_family, had_work_calls, had_smalltalk,
            had_waiter, had_wave, had_date, had_networking, had_phonecall,
            had_relative, had_lie, had_cancelled, had_ghosted, had_cancelled_on,
            had_alone_time, people_count, awkward_moments, worst_event, recharge,
            name_penalty
        )
        rx1, rx1_note = random.choice(PRESCRIPTIONS)
        rx2, rx2_note = random.choice([p for p in PRESCRIPTIONS if p[0] != rx1])
        st.session_state.error = False
        st.session_state.networking_override = had_networking and "networking" in worst_event
        st.session_state.result = {
            "name":        name.strip(),
            "score":       score,
            "tier":        tier,
            "bar_color":   BAR_FILLS[tier][0],
            "bar_pct":     BAR_FILLS[tier][1],
            "bg_color":    RESULT_COLORS[tier][0],
            "border_col":  RESULT_COLORS[tier][1],
            "diagnosis":   random.choice(DIAGNOSES[tier]),
            "doctor_note": random.choice(DOCTOR_NOTES[tier]),
            "warning":     WARNING_LABELS[tier],
            "rx1": rx1, "rx1_note": rx1_note,
            "rx2": rx2, "rx2_note": rx2_note,
            "ref_num":     random.randint(10000, 99999),
            "bar_blocks":  "█" * (BAR_FILLS[tier][1] // 8),
        }
        st.session_state.rating_done = False

if st.session_state.get("error"):
    st.markdown("<div style='background:#FFFDE0; border:2px inset #888800; padding:14px; margin:10px 0; font-size:13px; color:#1a1a1a;'>ERROR: Patient name is required. The doctor cannot diagnose a ghost. (Or can he. He would rather not.)</div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
#  RESULTS
# ═══════════════════════════════════════════════════════════════════════════════
r = st.session_state.get("result")
if r:
    st.markdown("<br>", unsafe_allow_html=True)

    # ── Networking override ───────────────────────────────────────────────────
    if st.session_state.get("networking_override"):
        st.markdown(f"""
        <div style='background:#CC0000; color:white; padding:20px; text-align:center;
                    border:4px solid #880000; margin-bottom:10px; font-size:15px;'>
            <strong>EMERGENCY OVERRIDE — REF: SBL-{r['ref_num']}</strong><br><br>
            Patient: <strong>{r['name'].upper()}</strong><br><br>
            It's over.<br><br>
            We are ordering you a pizza and a weighted blanket.<br>
            Do not fight it.<br><br>
            <span style='font-size:11px; color:#FFAAAA;'>
            (The doctor has reviewed your file, closed your file, and gone home for the day.)
            </span>
        </div>
        """, unsafe_allow_html=True)

    else:
        # ── Section header ────────────────────────────────────────────────────
        st.markdown(
            f"<div style='background:#000080; color:white; padding:3px 8px; font-size:13px; "
            f"font-weight:700; letter-spacing:1px; margin-bottom:0;'>"
            f"DIAGNOSTIC RESULTS — PATIENT: {r['name'].upper()}</div>",
            unsafe_allow_html=True)

        st.markdown(
            f"<div style='background:{r['bg_color']}; border:2px solid {r['border_col']}; "
            f"border-top:none; padding:14px 16px 4px; font-size:11px; color:#555;'>"
            f"SOCIAL BATTERY DIAGNOSTIC CENTER &nbsp;|&nbsp; REF: SBL-{r['ref_num']}</div>",
            unsafe_allow_html=True)

        st.markdown(
            f"<div style='background:{r['bg_color']}; border-left:2px solid {r['border_col']}; "
            f"border-right:2px solid {r['border_col']}; padding:6px 16px; font-size:16px; font-weight:700;'>"
            f"DIAGNOSIS: {r['diagnosis']}</div>",
            unsafe_allow_html=True)

        st.markdown(
            f"<div style='background:{r['bg_color']}; border-left:2px solid {r['border_col']}; "
            f"border-right:2px solid {r['border_col']}; padding:4px 16px; font-size:12px;'>"
            f"<strong>{r['warning']}</strong></div>",
            unsafe_allow_html=True)

        st.markdown(
            f"<div style='background:{r['bg_color']}; border-left:2px solid {r['border_col']}; "
            f"border-right:2px solid {r['border_col']}; padding:8px 16px; font-size:12px;'>"
            f"SOCIAL BATTERY LEVEL (SBL): <strong>{r['score']}%</strong>"
            f"<div style='background:#888; height:26px; margin-top:6px;'>"
            f"<div style='background:{r['bar_color']}; width:{r['bar_pct']}%; height:100%; "
            f"padding-left:6px; display:flex; align-items:center; color:white; font-size:11px; font-weight:700;'>"
            f"{r['bar_blocks']} {r['score']}%</div></div></div>",
            unsafe_allow_html=True)

        st.markdown(
            f"<div style='background:{r['bg_color']}; border:2px solid {r['border_col']}; "
            f"border-top:none; padding:10px 16px 14px; font-size:12px; margin-bottom:10px;'>"
            f"<strong>DOCTOR'S CLINICAL NOTE:</strong><br>{r['doctor_note']}</div>",
            unsafe_allow_html=True)

        # ── Prescription ──────────────────────────────────────────────────────
        st.markdown("<div style='background:#FFFFF0; border:2px solid #000; padding:14px 16px 4px;'>"
                    "<span style='font-size:17px; font-weight:700;'>Rx &nbsp; OFFICIAL PRESCRIPTION</span>"
                    "<hr style='border:none; border-top:1px solid #000; margin:8px 0;'></div>",
                    unsafe_allow_html=True)

        st.markdown(
            f"<div style='background:#FFFFF0; border-left:2px solid #000; border-right:2px solid #000; "
            f"padding:4px 16px; font-size:12px;'>"
            f"<strong>Patient:</strong> {r['name'].title()} &nbsp;&nbsp;"
            f"<strong>Date:</strong> Today (The doctor does not know what day it is)</div>",
            unsafe_allow_html=True)

        st.markdown(
            f"<div style='background:#FFFFF0; border-left:2px solid #000; border-right:2px solid #000; "
            f"padding:8px 16px; font-size:12px;'>"
            f"<strong>Rx 1:</strong> {r['rx1']}<br>"
            f"<span style='font-size:11px; color:#555;'>Instructions: {r['rx1_note']}</span></div>",
            unsafe_allow_html=True)

        st.markdown(
            f"<div style='background:#FFFFF0; border-left:2px solid #000; border-right:2px solid #000; "
            f"padding:8px 16px; font-size:12px;'>"
            f"<strong>Rx 2:</strong> {r['rx2']}<br>"
            f"<span style='font-size:11px; color:#555;'>Instructions: {r['rx2_note']}</span></div>",
            unsafe_allow_html=True)

        st.markdown(
            "<div style='background:#FFFFF0; border-left:2px solid #000; border-right:2px solid #000; "
            "padding:8px 16px; font-size:12px;'>"
            "<strong>Refills:</strong> Unlimited. Take as needed. Take more than needed.<br>"
            "<strong>Warnings:</strong> Do not operate social obligations while on this prescription.</div>",
            unsafe_allow_html=True)

        st.markdown(
            "<div style='background:#FFFFF0; border:2px solid #000; border-top:none; "
            "padding:10px 16px 14px; text-align:right; margin-bottom:10px;'>"
            "<span style='border:3px solid #CC0000; color:#CC0000; font-size:14px; "
            "font-weight:700; padding:3px 12px; letter-spacing:2px;'>DR. APPROVED</span></div>",
            unsafe_allow_html=True)

    # ── Rating buttons ────────────────────────────────────────────────────────
    if not st.session_state.get("rating_done"):
        st.markdown("<div style='background:#FFFFF0; border:2px inset #888; padding:12px 16px 6px; "
                    "font-size:12px; margin-bottom:4px;'><strong>RATE THIS DIAGNOSIS:</strong></div>",
                    unsafe_allow_html=True)
        rc1, rc2, rc3, rc4 = st.columns(4)
        with rc1:
            if st.button("Excellent", key="rate_excellent"):
                st.session_state.rating_msg = "Thank you. Please do not tell anyone about this site. We do not want the traffic."
                st.session_state.rating_done = True
                st.rerun()
        with rc2:
            if st.button("Very Good", key="rate_verygood"):
                st.session_state.rating_msg = "Noted. The doctor will add this to his refrigerator."
                st.session_state.rating_done = True
                st.rerun()
        with rc3:
            if st.button("Good", key="rate_good"):
                st.session_state.rating_msg = "Good is fine. The doctor has been called worse."
                st.session_state.rating_done = True
                st.rerun()
        with rc4:
            if st.button("Why Did I Come Here", key="rate_why"):
                st.session_state.rating_msg = "The doctor understands. He also does not know why you came here. He does not know why he built this. We are all just tired."
                st.session_state.rating_done = True
                st.rerun()

    if st.session_state.get("rating_done"):
        st.markdown(
            f"<div style='background:#FFFFF0; border:2px inset #888; padding:12px 16px; "
            f"font-size:12px; margin-bottom:10px; font-style:italic;'>"
            f"📋 {st.session_state.rating_msg}</div>",
            unsafe_allow_html=True)

    # ── Disclaimer ────────────────────────────────────────────────────────────
    st.markdown(
        "<div style='background:#FFFFF0; border:2px inset #888; padding:14px 16px; "
        "margin:0 0 10px; font-size:11px; color:#555;'>"
        "<strong>DISCLAIMER:</strong> This diagnosis is certified by the International Board of "
        "People Who Just Need a Minute. Results valid for 7 days or until someone invites you "
        "to something, whichever comes first. The doctor is not responsible for any plans you "
        "cancel as a result of this report. That was going to happen anyway.</div>",
        unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<br>
<div style='border-top:2px solid #888; padding-top:10px; font-size:10px; color:#555; text-align:center;'>

    <div style='margin-bottom:10px;'>
        <span style='border:2px solid #888; padding:4px 8px; font-size:10px; background:#C0C0C0; color:#000080;'>
            🔗 INTROVERT WEBRING [&lt;&lt; PREV] [RANDOM] [NEXT &gt;&gt;]
        </span>
        &nbsp;&nbsp;
        <span style='border:2px solid #888; padding:4px 8px; font-size:10px; background:#C0C0C0;'>
            <span style='color:#CC0000; font-weight:700;'>e</span> Best viewed in Internet Explorer 4.0
        </span>
        &nbsp;&nbsp;
        <span style='border:2px solid #888; padding:4px 8px; font-size:10px;
                     background:#000080; color:#FFFF00; font-weight:700;'>
            ★ NETSCAPE NOW ★
        </span>
    </div>

    &copy; 1994&ndash;2026 Social Battery Diagnostic Center &nbsp;|&nbsp;
    Best viewed at 800&times;600 &nbsp;|&nbsp;
    <span class='blink'>NEW</span> Now Y2K compliant &nbsp;|&nbsp;
    Dr. Introvert is not a real doctor. Results are not real results. You knew this.
</div>
<br>
""", unsafe_allow_html=True)
