import streamlit as st
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, firestore
import json
import os
from datetime import datetime
import google.api_core.exceptions

# --- MODEL ORCHESTRATION CONFIG ---
GEMINI_MODEL_PRIORITY = [
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite",
    "gemini-1.5-flash",
    "gemini-1.5-flash-8b",
]

# --- DESIGN & CONFIG ---
st.set_page_config(page_title="ThinkMath.ai", layout="wide", initial_sidebar_state="expanded")

# Inject Custom CSS — Bright Academic Theme (Yellow/White)
st.markdown("""
    <style>
    /* ── RESET & BASE ── */
    html, body, [class*="css"] {
        font-family: 'Segoe UI', Arial, sans-serif !important;
        font-size: 15px;
        line-height: 1.75;
        color: #2d1f0e;
    }

    /* ── APP BACKGROUND ── */
    .stApp {
        background-color: #ffffff;
    }

    /* ── SIDEBAR ── */
    section[data-testid="stSidebar"] {
        background-color: #f9f6f1 !important;
        border-right: 1px solid #ddd5c0;
    }
    section[data-testid="stSidebar"] * {
        color: #2d1f0e !important;
        font-family: 'Segoe UI', Arial, sans-serif !important;
    }

    /* ── HEADINGS ── */
    h1 {
        color: #5c3d1e !important;
        font-weight: 800 !important;
        font-size: 1.8rem !important;
        letter-spacing: -0.5px;
    }
    h2, h3, h4, h5, h6 {
        color: #5c3d1e !important;
        font-weight: 700 !important;
    }

    /* ── TAGLINE ── */
    .stMarkdown p em {
        color: #7a6040;
        font-style: italic;
    }

    /* ── CHAT MESSAGES ── */
    .user-message {
        background-color: #f4f0e8;
        border-left: 4px solid #8db543;
        border-radius: 8px;
        padding: 16px 20px;
        margin: 10px 0;
        color: #2d1f0e;
        box-shadow: 0 1px 4px rgba(92,61,30,0.08);
    }
    .mentor-message {
        background-color: #faf7f2;
        border-left: 4px solid #5c3d1e;
        border-radius: 8px;
        padding: 16px 20px;
        margin: 10px 0;
        color: #2d1f0e;
        box-shadow: 0 1px 4px rgba(92,61,30,0.08);
    }
    .user-message strong, .mentor-message strong {
        color: #5c3d1e;
        font-size: 0.85em;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* ── INPUT BOX ── */
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea,
    [data-testid="stChatInput"] textarea {
        background-color: #ffffff !important;
        color: #2d1f0e !important;
        border: 1px solid #ddd5c0 !important;
        border-radius: 8px !important;
        font-family: 'Segoe UI', Arial, sans-serif !important;
    }
    [data-testid="stChatInput"] textarea:focus {
        border: 2px solid #8db543 !important;
        outline: none !important;
    }

    /* ── BUTTONS ── */
    .stButton>button {
        background-color: #ffffff;
        color: #5c3d1e;
        border: 1px solid #ddd5c0;
        border-radius: 6px;
        font-family: 'Segoe UI', Arial, sans-serif !important;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #f4f0e8;
        border-color: #8db543;
        color: #5c3d1e;
    }
    /* Primary button — Generate Stage 2 */
    .stButton>button[kind="primary"] {
        background-color: #8db543 !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: bold !important;
    }
    .stButton>button[kind="primary"]:hover {
        background-color: #7a9e3a !important;
    }

    /* ── PHASE INDICATOR ── */
    .phase-active {
        color: #8db543 !important;
        font-weight: bold;
    }
    .phase-complete {
        color: #5c3d1e !important;
    }
    .phase-inactive {
        color: #bbb0a0 !important;
    }

    /* ── TIER BADGE ── */
    .tier-badge {
        background-color: #f4f0e8;
        border: 1px solid #8db543;
        color: #8db543;
        border-radius: 20px;
        padding: 4px 12px;
        font-size: 0.8em;
        display: inline-block;
        margin-bottom: 8px;
    }

    /* ── DONATE SECTION ── */
    .donate-section {
        background-color: #f4f0e8;
        border: 1px solid #8db543;
        border-radius: 10px;
        padding: 16px;
        margin-top: 12px;
        text-align: center;
    }
    .donate-section p {
        color: #5c3d1e !important;
    }

    /* ── SELECTBOX & SIDEBAR WIDGETS ── */
    .stSelectbox>div>div {
        background-color: #f9f6f1 !important;
        border: 1px solid #ddd5c0 !important;
        color: #2d1f0e !important;
        border-radius: 6px !important;
    }

    /* ── SUCCESS / WARNING / ERROR ── */
    .stSuccess {
        background-color: #f0f7e6 !important;
        color: #5c3d1e !important;
        border: 1px solid #8db543 !important;
    }
    .stWarning {
        background-color: #fdf6e3 !important;
        color: #5c3d1e !important;
    }
    .stError {
        background-color: #fff0f0 !important;
        color: #c0392b !important;
    }

    /* ── DIVIDER ── */
    hr {
        border-color: #ddd5c0 !important;
    }

    /* ── SCROLLBAR ── */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb {
        background-color: #ddd5c0;
        border-radius: 3px;
    }

    /* ── HIDE STREAMLIT SIDEBAR COLLAPSE TOOLTIP ── */
    button[data-testid="collapsedControl"] {
    display: none !important;
    }
    [data-testid="stSidebarCollapseButton"] {
    display: none !important;
    }
    button[kind="headerNoPadding"] {
    display: none !important;
    }
    /* Hide all Streamlit toolbar tooltips */
    .st-emotion-cache-zq5wmm {
    display: none !important;
    }
    /* Hide the keyboard_double_arrow tooltip specifically */
    [data-testid="stSidebarNavCollapseIcon"] {
    display: none !important;
    }
    .st-emotion-cache-1rtdyuf {
    display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CREDENTIALS MANAGEMENT ---
def get_credentials():
    api_k = None
    fb_cred = None

    try:
        if hasattr(st, "secrets") and st.secrets:
            api_k = st.secrets.get("GEMINI_API_KEY")
            if api_k:
                api_k = api_k.strip().replace('"', '').replace("'", "")
            if "firebase" in st.secrets:
                fb_cred = dict(st.secrets["firebase"])
    except (FileNotFoundError, RuntimeError, Exception):
        pass

    if not api_k:
        try:
            with open(os.path.join(os.path.dirname(__file__), "..", "AIzaSyCFoDs_OGzL65bacvVJzipZsxWx6YF.txt"), "r") as f:
                api_k = f.read().strip().replace('"', '').replace("'", "")
        except FileNotFoundError:
            pass

    fb_path = os.path.join(os.path.dirname(__file__), "..", "advaitian-commentary-engine-firebase-adminsdk-fbsvc-70e4298d89.json")
    if not fb_cred and os.path.exists(fb_path):
        fb_cred = fb_path

    return api_k, fb_cred

inferred_api_key, inferred_fb_cred = get_credentials()

# --- SIDEBAR ---
st.sidebar.image("https://raw.githubusercontent.com/sixteenpython/advaitian-philosophy/main/figures/imath_logo.png", width=90)
st.sidebar.markdown("<hr style='border:none; border-top:1px solid #ddd5c0; margin:8px 0;'>", unsafe_allow_html=True)

if inferred_api_key:
    st.sidebar.markdown("<div style='background:#f0f7e6; border:1px solid #8db543; border-radius:6px; padding:6px 12px; color:#5c3d1e; font-size:0.85em; margin:4px 0;'>● Gemini Connected</div>", unsafe_allow_html=True)
    api_key = inferred_api_key
else:
    api_key = st.sidebar.text_input("Gemini API Key", type="password")

if inferred_fb_cred:
    st.sidebar.markdown("<div style='background:#f0f7e6; border:1px solid #8db543; border-radius:6px; padding:6px 12px; color:#5c3d1e; font-size:0.85em; margin:4px 0;'>● Firebase Connected</div>", unsafe_allow_html=True)
    firebase_cred = inferred_fb_cred
else:
    firebase_cred_path = st.sidebar.text_input("Firebase JSON Path")
    firebase_cred = firebase_cred_path

st.sidebar.markdown("---")
st.sidebar.markdown("#### Engine Status")
st.sidebar.markdown(f"<div style='background:#f4f0e8; border:1px solid #8db543; border-radius:6px; padding:6px 12px; color:#5c3d1e; font-size:0.85em; margin:4px 0;'>Model: {st.session_state.get('active_model', 'Initializing...')}</div>", unsafe_allow_html=True)

st.sidebar.markdown("---")

# --- PHASE INDICATOR ---
def render_phase_indicator(current_phase):
    phases = {
        1: "Phase 1: Finding the Seed",
        2: "Phase 2: Identifying Directions",
        3: "Phase 3: Convergence"
    }
    st.sidebar.markdown("#### Session Progress")
    for num, label in phases.items():
        if num < current_phase:
            st.sidebar.markdown(f"<span class='phase-complete'>✓ {label}</span>", unsafe_allow_html=True)
        elif num == current_phase:
            st.sidebar.markdown(f"<span class='phase-active'>▶ {label}</span>", unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f"<span class='phase-inactive'>○ {label}</span>", unsafe_allow_html=True)

# --- TIER DISPLAY ---
TIER_LABELS = {
    0: "Tier 0 — Narrative (Ages 6–9)",
    1: "Tier 1 — Relationship (Ages 10–13)",
    2: "Tier 2 — Abstract (Ages 14–16)",
    3: "Tier 3 — Elite (JEE/IMO)",
    4: "Tier 4 — Competition (IMO/Putnam)"
}

# --- KNOWLEDGE BASE ---
@st.cache_data
def load_knowledge_base():
    kb_dir = os.path.join(os.path.dirname(__file__), "..", "knowledge_base")
    if not os.path.exists(kb_dir):
        return "Warning: knowledge_base directory not found."

    aggregated_kb = ""
    # Load Blueprint v3 first — it takes priority
    blueprint_path = os.path.join(kb_dir, "ThinkMath_Blueprint_v3.md")
    if os.path.exists(blueprint_path):
        with open(blueprint_path, "r", encoding="utf-8") as f:
            aggregated_kb += f"\n--- PRIMARY DIRECTIVE: ThinkMath_Blueprint_v3.md ---\n"
            aggregated_kb += f.read()
            aggregated_kb += "\n--- END PRIMARY DIRECTIVE ---\n\n"

    # Then load all other knowledge base files
    for filename in sorted(os.listdir(kb_dir)):
        if filename.endswith((".txt", ".md")) and filename != "ThinkMath_Blueprint_v3.md":
            file_path = os.path.join(kb_dir, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    aggregated_kb += f"\n--- REFERENCE: {filename} ---\n"
                    aggregated_kb += file.read()
                    aggregated_kb += "\n"
            except Exception as e:
                aggregated_kb += f"\nError loading {filename}: {e}\n"

    return aggregated_kb if aggregated_kb else "Knowledge base is empty."

knowledge_base = load_knowledge_base()

# --- SYSTEM PROMPT ---
# Blueprint v3 is already fully loaded in knowledge_base as PRIMARY DIRECTIVE.
# This wrapper ensures the Socratic chat mode is activated.
SYSTEM_PROMPT = f"""
You are the ThinkMath.ai Socratic Mentor — the Digital Clone of Anand, Founder of the Advaitian Foundation.

Your complete operating instructions, philosophy, 20 archetypes, 160 gems, tier detection protocol,
socratic engagement protocol, escape hatch system, and six-point commentary framework are all
contained in the PRIMARY DIRECTIVE section of your knowledge base below.

CRITICAL: Read and fully internalize the PRIMARY DIRECTIVE (ThinkMath_Blueprint_v3.md) before
responding to any student message. Every response must reflect that document.

You are operating in SOCRATIC CHAT MODE. The student submits problems via chat.
You guide them through Phases 1, 2, and 3 as described in your blueprint.
You NEVER give the answer directly. You are a Structural Mirror.

After each response, append a hidden metadata line in this exact format (on its own line at the end):
PHASE:[1/2/3] TIER:[0/1/2/3/4]

This allows the UI to track session progress. Do not explain this line to the student.

--- KNOWLEDGE BASE (PRIMARY DIRECTIVE + REFERENCES) ---
{knowledge_base}
"""

# --- GEMINI MODEL ORCHESTRATOR ---
def get_gemini_model_with_fallback(system_instruction):
    """Try models in priority order until one works."""
    genai.configure(api_key=api_key)
    generation_config = {
        "temperature": 0.3,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    ]

    for model_name in GEMINI_MODEL_PRIORITY:
        try:
            model = genai.GenerativeModel(
                model_name=model_name,
                generation_config=generation_config,
                system_instruction=system_instruction,
                safety_settings=safety_settings
            )
            # Test initialization if possible, or just return
            st.session_state.active_model = model_name
            return model
        except (google.api_core.exceptions.ResourceExhausted, Exception) as e:
            if "429" in str(e) or "quota" in str(e).lower():
                continue # Try next model
            raise e
    
    st.error("All models in the priority list have exhausted their quota. Please try again later.")
    st.stop()

# --- FIREBASE ---
def init_firebase():
    if not firebase_admin._apps:
        try:
            if isinstance(firebase_cred, dict):
                cred = credentials.Certificate(firebase_cred)
            elif firebase_cred and os.path.exists(firebase_cred):
                cred = credentials.Certificate(firebase_cred)
            else:
                st.sidebar.error("Firebase credentials missing.")
                return None
            firebase_admin.initialize_app(cred)
            return firestore.client()
        except Exception as e:
            st.sidebar.error(f"Firebase init failed: {e}")
            return None
    return firestore.client()

def save_session_to_firebase(messages, phase, tier):
    """Save completed session to Firestore."""
    try:
        db = init_firebase()
        if db:
            doc_ref = db.collection("sessions").document()
            doc_ref.set({
                "messages": [{"role": m["role"], "content": m["content"]} for m in messages],
                "final_phase": phase,
                "detected_tier": tier,
                "timestamp": firestore.SERVER_TIMESTAMP,
                "message_count": len(messages)
            })
    except Exception as e:
        pass  # Silent fail — don't interrupt student session

def save_commentary_to_firebase(problem, commentary, tier):
    """Save Six-Point Commentary to the Advaitian Bible."""
    try:
        db = init_firebase()
        if db:
            doc_ref = db.collection("commentaries").document()
            doc_ref.set({
                "problem": problem,
                "commentary": commentary,
                "tier": tier,
                "timestamp": firestore.SERVER_TIMESTAMP,
                "status": "generated"
            })
            return True
    except Exception as e:
        return False
    return False

# --- PARSE METADATA FROM RESPONSE ---
def parse_metadata(response_text):
    """Extract phase and tier from the hidden metadata line."""
    phase = 1
    tier = 3  # Default to elite tier
    lines = response_text.strip().split('\n')
    clean_lines = []
    for line in lines:
        if line.strip().startswith("PHASE:") and "TIER:" in line:
            try:
                phase_part = line.split("PHASE:")[1].split(" ")[0].strip()
                tier_part = line.split("TIER:")[1].strip()
                phase = int(phase_part)
                tier = int(tier_part)
            except:
                pass
        else:
            clean_lines.append(line)
    clean_response = '\n'.join(clean_lines).strip()
    return clean_response, phase, tier

# --- SESSION STATE ---
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'chat_session' not in st.session_state:
    st.session_state.chat_session = None
if 'current_phase' not in st.session_state:
    st.session_state.current_phase = 1
if 'detected_tier' not in st.session_state:
    st.session_state.detected_tier = 3
if 'session_saved' not in st.session_state:
    st.session_state.session_saved = False
if 'hint_level' not in st.session_state:
    st.session_state.hint_level = 0
if 'mvc_validated' not in st.session_state:
    st.session_state.mvc_validated = False
if 'active_model' not in st.session_state:
    st.session_state.active_model = None

# --- RENDER PHASE INDICATOR ---
render_phase_indicator(st.session_state.current_phase)

# --- DONATE SECTION IN SIDEBAR ---
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div class='donate-section'>
    <p style='color: #e0e0e0; font-size: 0.85em; line-height: 1.6;'>
        <em>\"You've burned the candle from both ends today.<br>
        Help us put a candle in someone else's hands.\"</em>
    </p>
    <p style='color: #888; font-size: 0.75em; margin-top: 8px;'>
        Every donation supports free structural math education for students who can't afford coaching.
    </p>
</div>
""", unsafe_allow_html=True)

# Replace with your actual PayPal.me link
PAYPAL_LINK = "https://paypal.me/vasumathiiK"
st.sidebar.link_button("Support the Mission", PAYPAL_LINK, use_container_width=True)

# --- NEW SESSION BUTTON ---
st.sidebar.markdown("---")
if st.sidebar.button("New Session", use_container_width=True):
    if st.session_state.messages and not st.session_state.session_saved:
        save_session_to_firebase(
            st.session_state.messages,
            st.session_state.current_phase,
            st.session_state.detected_tier
        )
    st.session_state.messages = []
    st.session_state.chat_session = None
    st.session_state.current_phase = 1
    st.session_state.detected_tier = 3
    st.session_state.session_saved = False
    st.session_state.hint_level = 0
    st.rerun()

# --- MAIN UI ---
st.image("https://raw.githubusercontent.com/sixteenpython/advaitian-philosophy/main/figures/imath_logo.png", width=110)
st.title("ThinkMath.ai")
st.markdown("##### Your Advaitian Socratic Mentor — Find the Seed. Burn the candle from both ends.")

# Show tier badge if detected
if st.session_state.messages:
    tier_label = TIER_LABELS.get(st.session_state.detected_tier, "Tier 3 — Elite")
    st.markdown(f"<span class='tier-badge'>{tier_label}</span>", unsafe_allow_html=True)

st.markdown("---")

# --- CHAT DISPLAY ---
chat_container = st.container()
with chat_container:
    if not st.session_state.messages:
        st.markdown("""
        <div class='mentor-message'>
        <strong>Anand's Digital Clone</strong><br><br>
        Namaste. I am the ThinkMath.ai Socratic Mentor.<br><br>
        Share your problem and we will find its <strong>Seed</strong> together.<br><br>
        I will never give you the answer. I will give you something better —
        the structural instinct to find it yourself, and to recognise it
        the next time it appears in disguise.<br><br>
        <em>What problem are you working on today?</em>
        </div>
        """, unsafe_allow_html=True)
    else:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f"""
                <div class='user-message'>
                <strong>You</strong><br>{msg['content']}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class='mentor-message'>
                <strong>Anand's Digital Clone</strong><br>{msg['content']}
                </div>
                """, unsafe_allow_html=True)

st.markdown("---")

# --- STAGE 2 BUTTON ---
if st.session_state.mvc_validated and st.session_state.current_phase < 3:
    if st.button("Generate Stage 2 Commentary", type="primary", use_container_width=True):
        stage2_prompt = "Please give me the full Stage 2 Six-Point Commentary now."
        st.session_state.messages.append({"role": "user", "content": stage2_prompt})
        with st.spinner("Generating Stage 2 Commentary..."):
            retry_count = 0
            while retry_count < len(GEMINI_MODEL_PRIORITY):
                try:
                    if st.session_state.chat_session is None:
                        model = get_gemini_model_with_fallback(SYSTEM_PROMPT)
                        st.session_state.chat_session = model.start_chat(history=[])
                    s2_response = st.session_state.chat_session.send_message(stage2_prompt)
                    if not s2_response.candidates or not s2_response.candidates[0].content.parts:
                        s2_raw = "I need a moment to reformulate. Could you rephrase your last message slightly and try again?"
                    else:
                        s2_raw = s2_response.text
                    s2_clean, s2_phase, s2_tier = parse_metadata(s2_raw)
                    st.session_state.current_phase = s2_phase
                    st.session_state.detected_tier = s2_tier
                    st.session_state.messages.append({"role": "mentor", "content": s2_clean})
                    break # Success!
                except Exception as e:
                    if "429" in str(e) or "quota" in str(e).lower() or isinstance(e, google.api_core.exceptions.ResourceExhausted):
                        st.session_state.chat_session = None
                        st.session_state.active_model = None
                        retry_count += 1
                        continue
                    else:
                        st.error(f"API Error: {e}")
                        break
        st.session_state.mvc_validated = False
        st.rerun()

# --- INPUT AREA ---
col_input, col_stuck = st.columns([5, 1])

with col_input:
    user_input = st.chat_input("Share your math problem or response here...")

with col_stuck:
    st.markdown("<br>", unsafe_allow_html=True)
    stuck_clicked = st.button("💡 I'm stuck", key="stuck_btn", help="Get a structural hint without the answer")

# --- HANDLE STUCK BUTTON ---
if stuck_clicked and st.session_state.messages:
    hint_level = st.session_state.hint_level
    hint_messages = [
        "I'm stuck. Can you give me a hint?",
        "I'm still stuck. Can you point me to the archetype?",
        "I really need more direction. Can you show me the direction map?"
    ]
    if hint_level < len(hint_messages):
        user_input = hint_messages[hint_level]
        st.session_state.hint_level += 1
    else:
        user_input = "I need the pivot shadow. I've exhausted my hints."
        st.session_state.hint_level = 0

# --- PROCESS MESSAGE ---
if user_input:
    if not api_key:
        st.error("Please provide a Gemini API Key in the sidebar.")
        st.stop()

    # Add user message to display
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking structurally..."):
        retry_count = 0
        while retry_count < len(GEMINI_MODEL_PRIORITY):
            try:
                # Initialize or continue chat session
                if st.session_state.chat_session is None:
                    model = get_gemini_model_with_fallback(SYSTEM_PROMPT)
                    st.session_state.chat_session = model.start_chat(history=[])

                # Send message
                response = st.session_state.chat_session.send_message(user_input)
                if not response.candidates or not response.candidates[0].content.parts:
                    raw_response = "I need a moment to reformulate. Could you rephrase your last message slightly and try again?"
                else:
                    raw_response = response.text

                # Parse metadata and clean response
                clean_response, phase, tier = parse_metadata(raw_response)

                # Update session state
                st.session_state.current_phase = phase
                st.session_state.detected_tier = tier

                # Add mentor response
                st.session_state.messages.append({"role": "mentor", "content": clean_response})

                # Detect MVC validation signal
                if "ready for stage 2" in clean_response.lower():
                    st.session_state.mvc_validated = True

                # Auto-save to Firebase when Phase 3 completes (commentary generated)
                if phase == 3 and "TAKEAWAY" in clean_response.upper():
                    problem = st.session_state.messages[0]["content"] if st.session_state.messages else ""
                    save_commentary_to_firebase(problem, clean_response, tier)
                    st.session_state.session_saved = True

                st.rerun()
                break # Success!

            except Exception as e:
                if "429" in str(e) or "quota" in str(e).lower() or isinstance(e, google.api_core.exceptions.ResourceExhausted):
                    st.session_state.chat_session = None
                    st.session_state.active_model = None
                    retry_count += 1
                    continue
                else:
                    st.error(f"API Error: {e}")
                    break

# --- EXPORT SESSION ---
if st.session_state.messages and st.session_state.current_phase == 3:
    st.markdown("---")
    col_save, col_export = st.columns(2)

    with col_save:
        if st.button("Commit to Advaitian Bible", use_container_width=True):
            problem = st.session_state.messages[0]["content"] if st.session_state.messages else ""
            last_mentor = next(
                (m["content"] for m in reversed(st.session_state.messages) if m["role"] == "mentor"),
                ""
            )
            if save_commentary_to_firebase(problem, last_mentor, st.session_state.detected_tier):
                st.success("Commentary committed to the Advaitian Bible (Firestore)!")
                st.balloons()
            else:
                st.error("Failed to commit. Check Firebase credentials.")

    with col_export:
        if st.button("Export Session", use_container_width=True):
            session_text = f"ThinkMath.ai Session Export\n"
            session_text += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
            session_text += f"Tier: {TIER_LABELS.get(st.session_state.detected_tier, 'Unknown')}\n"
            session_text += "=" * 50 + "\n\n"
            for msg in st.session_state.messages:
                role = "YOU" if msg["role"] == "user" else "MENTOR"
                session_text += f"[{role}]\n{msg['content']}\n\n"
            st.download_button(
                "Download Session",
                session_text,
                file_name=f"thinkmath_session_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                mime="text/plain"
            )
