import streamlit as st
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, firestore
import json
import os
from datetime import datetime

# --- DESIGN & CONFIG ---
st.set_page_config(page_title="ThinkMath.ai", layout="wide", initial_sidebar_state="expanded")

# Inject Custom CSS for dark minimalist theme and monospaced fonts
st.markdown("""
    <style>
    /* Base theme overrides */
    html, body, [class*="css"] {
        font-family: 'Courier New', Courier, monospace !important;
    }
    .stApp {
        background-color: #121212;
        color: #e0e0e0;
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #1e1e1e !important;
        color: #e0e0e0 !important;
        border: 1px solid #333 !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    .stButton>button {
        background-color: #2b2b2b;
        color: #ffffff;
        border: 1px solid #444;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #3b3b3b;
        border-color: #666;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }
    .stMarkdown p {
        color: #cccccc;
    }

    /* Chat message styling */
    .user-message {
        background-color: #1a1a2e;
        border-left: 3px solid #6c63ff;
        padding: 12px 16px;
        border-radius: 0 8px 8px 0;
        margin: 8px 0;
        color: #e0e0e0;
    }
    .mentor-message {
        background-color: #0d1117;
        border-left: 3px solid #00b4d8;
        padding: 12px 16px;
        border-radius: 0 8px 8px 0;
        margin: 8px 0;
        color: #e0e0e0;
    }
    .phase-indicator {
        background-color: #1e1e1e;
        border: 1px solid #333;
        border-radius: 8px;
        padding: 12px;
        margin: 8px 0;
    }
    .phase-active {
        color: #00b4d8;
        font-weight: bold;
    }
    .phase-inactive {
        color: #555;
    }
    .phase-complete {
        color: #4caf50;
    }
    .donate-section {
        background-color: #1a1a1a;
        border: 1px solid #333;
        border-radius: 8px;
        padding: 16px;
        margin-top: 16px;
        text-align: center;
    }
    .tier-badge {
        background-color: #2b2b2b;
        border: 1px solid #6c63ff;
        border-radius: 12px;
        padding: 4px 10px;
        font-size: 0.75em;
        color: #6c63ff;
        display: inline-block;
        margin-bottom: 8px;
    }
    .stuck-button>button {
        background-color: #1a1a2e !important;
        border: 1px solid #6c63ff !important;
        color: #6c63ff !important;
        font-size: 0.85em !important;
        padding: 4px 12px !important;
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
st.sidebar.title("⚙️ ThinkMath.ai")

if inferred_api_key:
    st.sidebar.success("✅ Gemini API Key Loaded")
    api_key = inferred_api_key
else:
    api_key = st.sidebar.text_input("Gemini API Key", type="password")

if inferred_fb_cred:
    st.sidebar.success("✅ Firebase Connected")
    firebase_cred = inferred_fb_cred
else:
    firebase_cred_path = st.sidebar.text_input("Firebase JSON Path")
    firebase_cred = firebase_cred_path

st.sidebar.markdown("---")
st.sidebar.title("🤖 Model")
selected_model = st.sidebar.selectbox(
    "Choose Gemini Model:",
    ["gemini-2.5-flash", "gemini-2.5-pro", "gemini-2.0-flash-lite"],
    index=0
)

st.sidebar.markdown("---")

# --- PHASE INDICATOR ---
def render_phase_indicator(current_phase):
    phases = {
        1: "🔍 Phase 1: Finding the Seed",
        2: "🧭 Phase 2: Identifying Directions",
        3: "💡 Phase 3: Convergence"
    }
    st.sidebar.markdown("### 📊 Session Progress")
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

# --- GEMINI MODEL ---
def get_gemini_model(system_instruction):
    genai.configure(api_key=api_key)
    generation_config = {
        "temperature": 0.3,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    return genai.GenerativeModel(
        model_name=selected_model,
        generation_config=generation_config,
        system_instruction=system_instruction
    )

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

# --- RENDER PHASE INDICATOR ---
render_phase_indicator(st.session_state.current_phase)

# --- DONATE SECTION IN SIDEBAR ---
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div class='donate-section'>
    <p style='color: #e0e0e0; font-size: 0.85em; line-height: 1.6;'>
        <em>"You've burned the candle from both ends today.<br>
        Help us put a candle in someone else's hands."</em>
    </p>
    <p style='color: #888; font-size: 0.75em; margin-top: 8px;'>
        Every donation supports free structural math education for students who can't afford coaching.
    </p>
</div>
""", unsafe_allow_html=True)

# Replace with your actual PayPal.me link
PAYPAL_LINK = "https://paypal.me/AdvaitianFoundation"
st.sidebar.link_button("❤️ Support the Mission", PAYPAL_LINK, use_container_width=True)

# --- NEW SESSION BUTTON ---
st.sidebar.markdown("---")
if st.sidebar.button("🔄 New Session", use_container_width=True):
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
st.title("🌑 ThinkMath.ai")
st.markdown("##### Your Advaitian Socratic Mentor — *Find the Seed. Burn the candle from both ends.*")

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
        try:
            # Initialize or continue chat session
            if st.session_state.chat_session is None:
                model = get_gemini_model(SYSTEM_PROMPT)
                st.session_state.chat_session = model.start_chat(history=[])

            # Send message
            response = st.session_state.chat_session.send_message(user_input)
            raw_response = response.text

            # Parse metadata and clean response
            clean_response, phase, tier = parse_metadata(raw_response)

            # Update session state
            st.session_state.current_phase = phase
            st.session_state.detected_tier = tier

            # Add mentor response
            st.session_state.messages.append({"role": "mentor", "content": clean_response})

            # Auto-save to Firebase when Phase 3 completes (commentary generated)
            if phase == 3 and "TAKEAWAY" in clean_response.upper():
                problem = st.session_state.messages[0]["content"] if st.session_state.messages else ""
                save_commentary_to_firebase(problem, clean_response, tier)
                st.session_state.session_saved = True

            st.rerun()

        except Exception as e:
            if "429" in str(e) or "quota" in str(e).lower():
                st.error(f"⚠️ Quota exceeded on {selected_model}. Switch model in sidebar and retry.")
            else:
                st.error(f"API Error: {e}")

# --- EXPORT SESSION ---
if st.session_state.messages and st.session_state.current_phase == 3:
    st.markdown("---")
    col_save, col_export = st.columns(2)

    with col_save:
        if st.button("📖 Commit to Advaitian Bible", use_container_width=True):
            problem = st.session_state.messages[0]["content"] if st.session_state.messages else ""
            last_mentor = next(
                (m["content"] for m in reversed(st.session_state.messages) if m["role"] == "mentor"),
                ""
            )
            if save_commentary_to_firebase(problem, last_mentor, st.session_state.detected_tier):
                st.success("✅ Commentary committed to the Advaitian Bible (Firestore)!")
                st.balloons()
            else:
                st.error("Failed to commit. Check Firebase credentials.")

    with col_export:
        if st.button("📥 Export Session", use_container_width=True):
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
