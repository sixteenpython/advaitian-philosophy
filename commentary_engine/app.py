import streamlit as st
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials, firestore
import json
import os
from datetime import datetime

# --- DESIGN & CONFIG ---
st.set_page_config(page_title="Advaitian Foundry Workbench", layout="wide", initial_sidebar_state="expanded")

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
    </style>
    """, unsafe_allow_html=True)

# --- CREDENTIALS MANAGEMENT ---
def get_credentials():
    # 1. Try Streamlit Secrets (for Streamlit Cloud deployment)
    api_k = None
    fb_cred = None
    
    # Check if st.secrets is available and not empty
    try:
        if hasattr(st, "secrets") and st.secrets:
            api_k = st.secrets.get("GEMINI_API_KEY")
            if "firebase" in st.secrets:
                fb_cred = dict(st.secrets["firebase"])
    except (FileNotFoundError, RuntimeError, Exception):
        # Streamlit raises errors if it can't find secrets file
        pass
    
    # 2. Try Local Files (for local development)
    if not api_k:
        try:
            with open(os.path.join(os.path.dirname(__file__), "..", "AIzaSyCFoDs_OGzL65bacvVJzipZsxWx6YF.txt"), "r") as f:
                api_k = f.read().strip()
        except FileNotFoundError:
            pass

    fb_path = os.path.join(os.path.dirname(__file__), "..", "advaitian-commentary-engine-firebase-adminsdk-fbsvc-70e4298d89.json")
    if not fb_cred and os.path.exists(fb_path):
        fb_cred = fb_path # Pass the file path if using local

    return api_k, fb_cred

inferred_api_key, inferred_fb_cred = get_credentials()

st.sidebar.title("⚗️ Settings")

if inferred_api_key:
    st.sidebar.success("✅ Gemini API Key Loaded")
    api_key = inferred_api_key
else:
    api_key = st.sidebar.text_input("Gemini API Key", type="password", help="Got this from Google AI Studio")

if inferred_fb_cred:
    st.sidebar.success("✅ Firebase Credentials Loaded")
    firebase_cred = inferred_fb_cred
else:
    firebase_cred_path = st.sidebar.text_input("Firebase JSON Path", help="Path to your serviceAccountKey.json file")
    firebase_cred = firebase_cred_path

st.sidebar.markdown("---")
st.sidebar.title("🤖 Model Selection")
# Gemini 1.5 Flash has higher free-tier limits than 2.0
selected_model = st.sidebar.selectbox(
    "Choose Gemini Model:",
    ["gemini-1.5-flash-8b", "gemini-1.5-flash", "gemini-2.0-flash", "gemini-1.5-pro"],
    index=0,
    help="Switch to 1.5-flash-8b for the highest rate limits (most stable for Free Tier)."
)

# Read Local Knowledge Base
@st.cache_data
def load_knowledge_base():
    # Adjust this path if the knowledge base is located elsewhere relative to this script
    kb_path = os.path.join(os.path.dirname(__file__), "..", "Advaitian_Master_Framework.txt")
    try:
        with open(kb_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return f"Error loading Knowledge Base: {e}. Please ensure Advaitian_Master_Framework.txt exists in the parent directory."

knowledge_base = load_knowledge_base()

# --- INITIALIZE GEMINI ---
def get_gemini_model(system_instruction):
    genai.configure(api_key=api_key)
    
    generation_config = {
      "temperature": 0.2, 
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

system_prompt = f"""You are the Advaitian Commentary Agent. Your goal is to expand an MVC into a Stage 2 Commentary.
STRICT RULE: Use only the 20 Archetypes and 160 Gems in the attached knowledge base.

WORKFLOW:
Validation: Analyze the user's MVC for: Seed (Archetype), Brute Trap, and Elegant Pivot.
If valid: Respond with EXACTLY: "Your MVC is solid. Ready for Stage 2." (And provide your brief reasoning).
If invalid: Challenge the user gently.

Stage 2: When the user explicitly asks for "Stage 2", generate a 6-point framework: 1. SEED, 2. BRUTE PATH, 3. ELEGANT PIVOT, 4. PITFALLS, 5. CONNECTIONS, 6. TAKEAWAY.

--- KNOWLEDGE BASE ---
{knowledge_base}
"""

# --- FIREBASE SETUP ---
def init_firebase():
    if not firebase_admin._apps:
        try:
            if isinstance(firebase_cred, dict):
                # Using Streamlit Secrets dictionary
                cred = credentials.Certificate(firebase_cred)
            elif firebase_cred and os.path.exists(firebase_cred):
                # Using local file path
                cred = credentials.Certificate(firebase_cred)
            else:
                st.sidebar.error("Firebase Details Missing or Invalid Path.")
                return None
            
            firebase_admin.initialize_app(cred)
            return firestore.client()
        except Exception as e:
            st.sidebar.error(f"Failed to init Firebase: {e}")
            return None
    return firestore.client()

# --- APP STATE ---
if 'chat_session' not in st.session_state:
    st.session_state.chat_session = None
if 'validation_passed' not in st.session_state:
    st.session_state.validation_passed = False
if 'stage2_generated' not in st.session_state:
    st.session_state.stage2_generated = False
if 'validation_response' not in st.session_state:
    st.session_state.validation_response = ""
if 'stage2_output' not in st.session_state:
    st.session_state.stage2_output = ""


# --- MAIN UI ---
st.title("Advaitian Foundry Workbench")
st.markdown("### The Structural Thinking Commentary Engine")

col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown("#### Input")
    problem_statement = st.text_area("Problem Statement", height=150, placeholder="Paste the math/physics problem here...")
    mvc_intuition = st.text_area("MVC Intuition", height=200, placeholder="E.g., Seed: #3 Duality. Brute: Expansion of terms. Pivot: Recognizing the Law of Cosines structure.")
    
    if st.button("Validate MVC"):
        if not api_key:
            st.error("Please provide a Gemini API Key in the sidebar.")
        elif not problem_statement or not mvc_intuition:
            st.error("Please provide both the Problem and your MVC.")
        else:
            with st.spinner("Analyzing MVC against Master Framework..."):
                try:
                    model = get_gemini_model(system_prompt)
                    chat = model.start_chat(history=[])
                    st.session_state.chat_session = chat
                    
                    user_message = f"Here is the problem and the MVC:\nProblem: {problem_statement}\nMVC: {mvc_intuition}"
                    response = chat.send_message(user_message)
                    
                    st.session_state.validation_response = response.text
                    
                    if "Your MVC is solid. Ready for Stage 2" in response.text:
                        st.session_state.validation_passed = True
                        st.success("Validation Passed!")
                    else:
                        st.session_state.validation_passed = False
                        st.warning("Validation Failed or Needs Refinement.")
                except Exception as e:
                    if "429" in str(e) or "quota" in str(e).lower():
                        st.error(f"⚠️ **Quota Exceeded (429) on {selected_model}:** Please switch to **gemini-1.5-flash-8b** in the sidebar and try again.")
                    else:
                        st.error(f"API Error: {e}")

with col2:
    st.markdown("#### Output")
    
    if st.session_state.validation_response:
        st.markdown("**Validation Gate Reasoning:**")
        st.info(st.session_state.validation_response)
        
    if st.session_state.validation_passed:
        if st.button("Generate Stage 2", type="primary"):
            with st.spinner("Forging Gold Standard Commentary..."):
                try:
                    chat = st.session_state.chat_session
                    response = chat.send_message("Give me Stage 2 commentary.")
                    st.session_state.stage2_output = response.text
                    st.session_state.stage2_generated = True
                except Exception as e:
                    if "429" in str(e) or "quota" in str(e).lower():
                        st.error(f"⚠️ **Quota Exceeded (429) on {selected_model}:** Please switch to **gemini-1.5-flash-8b** in the sidebar and try again.")
                    else:
                        st.error(f"API Error: {e}")
                    
    if st.session_state.stage2_generated:
        st.markdown("**Final Stage 2 Commentary:**")
        st.markdown(st.session_state.stage2_output)
        
        st.markdown("---")
        if st.button("Commit to Bible 📖"):
            if not firebase_cred:
                st.error("Please provide Firebase Credentials.")
            else:
                db = init_firebase()
                if db:
                    try:
                        doc_ref = db.collection("commentaries").document()
                        doc_ref.set({
                            "problem_statement": problem_statement,
                            "mvc": mvc_intuition,
                            "stage2_commentary": st.session_state.stage2_output,
                            "timestamp": firestore.SERVER_TIMESTAMP,
                            "status": "published"
                        })
                        st.success("Successfully committed to the Advaitian Bible (Firestore)!")
                        st.balloons()
                    except Exception as e:
                        st.error(f"Failed to commit to database: {e}")
