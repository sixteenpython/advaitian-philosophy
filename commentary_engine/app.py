import streamlit as st
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, firestore
from groq import Groq
from openai import OpenAI
import json
import os
from datetime import datetime
import google.api_core.exceptions

# --- MODEL ORCHESTRATION CONFIG ---
FAST_TIER = [
    ("Gemini", "gemini-1.5-flash"),
    ("Groq", "llama3-8b-8192"),
    ("Gemini", "gemini-1.5-flash-8b")
]

REASONING_TIER = [
    ("Gemini", "gemini-2.0-flash"),
    ("SambaNova", "Meta-Llama-3.1-405B-Instruct"),
    ("Groq", "llama-3.1-70b-versatile"),
    ("Gemini", "gemini-1.5-flash")
]

def detect_math_intent(text):
    """Heuristic to detect if input is a math problem vs greeting."""
    math_indicators = ["+", "-", "*", "/", "=", "x", "n", "p", "q", "sum", "odd", "even", "integer", "prime", "prove", "if", "then", "archetype", "seed"]
    # Check for numbers or common math symbols
    if any(char.isdigit() for char in text):
        return True
    words = text.lower().split()
    if any(indicator in words for indicator in math_indicators):
        return True
    if len(text) > 60: # Long messages are usually problems
        return True
    return False

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
    [data-testid="stSidebarNavCollapseIcon"] {
        display: none !important;
    }

    </style>
    """, unsafe_allow_html=True)

# --- CREDENTIALS MANAGEMENT ---
def get_credentials():
    api_k = None
    fb_cred = None
    groq_k = None
    samba_k = None

    # 1. Try Streamlit Secrets
    try:
        if hasattr(st, "secrets") and st.secrets:
            api_k = st.secrets.get("GEMINI_API_KEY")
            groq_k = st.secrets.get("GROQ_API_KEY")
            samba_k = st.secrets.get("SAMBANOVA_API_KEY")
            if "firebase" in st.secrets:
                fb_cred = dict(st.secrets["firebase"])
    except: pass

    # 2. Try Local File Fallbacks (for Gemini/Firebase)
    def clean_key(val):
        return val.strip().replace('"', '').replace("'", "") if val else None

    if not api_k:
        try:
            with open(os.path.join(os.path.dirname(__file__), "..", "AIzaSyCFoDs_OGzL65bacvVJzipZsxWx6YF.txt"), "r") as f:
                api_k = clean_key(f.read())
        except: pass

    if not groq_k:
        try:
            with open(os.path.join(os.path.dirname(__file__), "..", "groq_api_key.txt"), "r") as f:
                groq_k = clean_key(f.read())
        except: pass

    if not samba_k:
        try:
            with open(os.path.join(os.path.dirname(__file__), "..", "samba_api_key.txt"), "r") as f:
                samba_k = clean_key(f.read())
        except: pass

    fb_path = os.path.join(os.path.dirname(__file__), "..", "advaitian-commentary-engine-firebase-adminsdk-fbsvc-70e4298d89.json")
    if not fb_cred and os.path.exists(fb_path):
        fb_cred = fb_path

    # Standardize values
    return clean_key(api_k), fb_cred, clean_key(groq_k), clean_key(samba_k)

api_key, firebase_cred, groq_api_key, samba_api_key = get_credentials()

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
        return "Warning: folder not found.", ""

    core_kb = ""
    ref_kb = ""
    
    # Load Blueprint v3 and Master Framework first — these are CORE (Sent in System Prompt)
    core_files = ["ThinkMath_Blueprint_v3.md", "Advaitian_Master_Framework.txt"]
    for cf in core_files:
        path = os.path.join(kb_dir, cf)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                core_kb += f"\n--- CORE DIRECTIVE: {cf} ---\n{f.read()}\n"

    # Load all other reference files (Stored in session but not sent in every System Prompt)
    for filename in sorted(os.listdir(kb_dir)):
        if filename.endswith((".txt", ".md")) and filename not in core_files:
            path = os.path.join(kb_dir, filename)
            try:
                with open(path, "r", encoding="utf-8") as file:
                    ref_kb += f"\n--- REFERENCE: {filename} ---\n{file.read()}\n"
            except: pass

    return core_kb, ref_kb

core_kb, reference_kb = load_knowledge_base()

# --- SYSTEM PROMPT ---
# We keep this as lean as possible to save quota. History and Blueprint are the priority.
SYSTEM_PROMPT = f"""
You are the ThinkMath.ai Socratic Mentor — the Digital Clone of ThinkMath.

CRITICAL: Your entire operating logic is defined in the CORE DIRECTIVES below. 
You are a structural mirror. You NEVER give the answer. You guide by Socratic questioning.

--- CORE DIRECTIVES ---
{core_kb}
"""

# --- PROVIDER WRAPPERS ---
class ModelWrapper:
    def __init__(self, provider, model_name, system_instruction):
        self.provider = provider
        self.model_name = model_name
        self.system_instruction = system_instruction
        self.history = []

    def send_message(self, text):
        # To be implemented by subclasses
        pass

class GeminiWrapper(ModelWrapper):
    def __init__(self, model_name, system_instruction):
        super().__init__("Gemini", model_name, system_instruction)
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name=model_name,
            system_instruction=system_instruction,
            generation_config={"temperature": 0.3, "top_p": 0.95, "max_output_tokens": 8192}
        )
        self.chat = self.model.start_chat(history=[])

    def send_message(self, text):
        return self.chat.send_message(text)

class GroqWrapper(ModelWrapper):
    def __init__(self, model_name, sys_instr):
        super().__init__("Groq", model_name, sys_instr)
        self.client = Groq(api_key=groq_api_key)

    def send_message(self, text):
        self.history.append({"role": "user", "content": text})
        messages = [{"role": "system", "content": self.system_instruction}] + self.history
        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=0.3,
            max_tokens=4096
        )
        response_text = completion.choices[0].message.content
        self.history.append({"role": "assistant", "content": response_text})
        # Mocking Gemini's response object structure
        class MockResponse:
            def __init__(self, text):
                self.text = text
                self.candidates = [True]
        return MockResponse(response_text)

class SambaNovaWrapper(ModelWrapper):
    def __init__(self, model_name, sys_instr):
        super().__init__("SambaNova", model_name, sys_instr)
        self.client = OpenAI(
            api_key=samba_api_key,
            base_url="https://api.sambanova.ai/v1"
        )

    def send_message(self, text):
        self.history.append({"role": "user", "content": text})
        messages = [{"role": "system", "content": self.system_instruction}] + self.history
        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=0.3,
            max_tokens=4096
        )
        response_text = completion.choices[0].message.content
        self.history.append({"role": "assistant", "content": response_text})
        class MockResponse:
            def __init__(self, text):
                self.text = text
                self.candidates = [True]
        return MockResponse(response_text)



# --- SIDEBAR ---
st.sidebar.image("https://raw.githubusercontent.com/sixteenpython/advaitian-philosophy/main/figures/imath_logo.png", width=90)
st.sidebar.markdown("<hr style='border:none; border-top:1px solid #ddd5c0; margin:8px 0;'>", unsafe_allow_html=True)

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
        <strong>ThinkMath's Digital Clone</strong><br><br>
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
                <strong>ThinkMath's Digital Clone</strong><br>{msg['content']}
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

    with st.status("Thinking structurally...", expanded=True) as status:
        # Intent-Aware Routing
        is_math = detect_math_intent(user_input)
        active_tier = REASONING_TIER if is_math else FAST_TIER
        tier_name = "REASONING" if is_math else "FAST"
        
        status.write(f"Intent detected: {'Mathematical Structure' if is_math else 'Conversational/Greeting'}")
        status.write(f"Routing to {tier_name} model tier...")
        
        retry_count = 0
        while retry_count < len(active_tier):
            provider, model_name = active_tier[retry_count]
            status.write(f"Connecting to {provider} ({model_name})...")
            
            try:
                # Initialize appropriate wrapper
                if provider == "Gemini":
                    if not api_key: 
                        status.write(f"⚠️ {provider} API Key missing. Skipping...")
                        retry_count += 1
                        continue
                    session = GeminiWrapper(f"models/{model_name}" if "/" not in model_name else model_name, SYSTEM_PROMPT)
                elif provider == "Groq":
                    if not groq_api_key:
                        status.write(f"⚠️ {provider} API Key missing. Skipping...")
                        retry_count += 1
                        continue
                    session = GroqWrapper(model_name, SYSTEM_PROMPT)
                elif provider == "SambaNova":
                    if not samba_api_key:
                        status.write(f"⚠️ {provider} API Key missing. Skipping...")
                        retry_count += 1
                        continue
                    session = SambaNovaWrapper(model_name, SYSTEM_PROMPT)
                
                st.session_state.active_model = f"{provider}: {model_name}"
                
                status.write(f"Generating structural response via {provider}...")
                response = session.send_message(user_input)
                status.write("Response received. Parsing...")
                
                raw_response = response.text

                # Parse metadata and clean response
                clean_response, phase, tier = parse_metadata(raw_response)

                if not clean_response:
                    clean_response = "[Empty response from engine. Please check your prompt.]"

                # Add Model Indicator to response for verification
                display_response = f"{clean_response}\n\n<div style='font-size:0.7em; color:#bbb0a0; margin-top:8px; border-top:1px solid #f0e6d6; padding-top:4px;'>Powered by {provider} {model_name}</div>"

                # Update session state with successful response
                st.session_state.current_phase = phase
                st.session_state.detected_tier = tier
                st.session_state.messages.append({"role": "mentor", "content": display_response})
                st.session_state.chat_session = session # Persist successful session
                
                # Detect MVC validation signal
                if "ready for stage 2" in clean_response.lower():
                    st.session_state.mvc_validated = True

                # Auto-save to Firebase when Phase 3 completes (commentary generated)
                if phase == 3 and "TAKEAWAY" in clean_response.upper():
                    problem = st.session_state.messages[0]["content"] if st.session_state.messages else ""
                    save_commentary_to_firebase(problem, clean_response, tier)
                    st.session_state.session_saved = True

                status.update(label="Response generated successfully!", state="complete")
                st.rerun()
                break # Success!

            except Exception as e:
                status.error(f"Failure on {provider} ({model_name}): {e}")
                # Retry on quota (429) or rate limits
                if "429" in str(e) or "quota" in str(e).lower() or isinstance(e, google.api_core.exceptions.ResourceExhausted):
                    retry_count += 1
                    status.warning(f"Quota exceeded on {provider}. Pivoting to next provider level...")
                    continue
                else:
                    st.error(f"Fatal Engine Error: {e}")
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
