"""
ThinkMath.ai — Socratic Mentor (Optimised Edition)

Architecture
------------
1. Dynamic model discovery: every chat-capable model under your Gemini, Groq, and
   SambaNova keys is enumerated at startup via each provider's models.list() endpoint.
2. Lean prompts: a ~1K-token CORE_BRIEF for math problems, a ~200-token CONCIERGE
   prompt for greetings.
3. Quota-aware circuit breaker: parses retry_delay, distinguishes daily-quota
   exhaustion from per-minute throttling from TPM-too-small.
4. Smart routing: greetings → smallest model first; math → largest model first.
5. UI: bright academic theme, iMaTh branding, native KaTeX math rendering.
"""

import os
import re
import time
import hashlib
import importlib.util
from datetime import datetime, timezone, timedelta
from hashlib import sha1

import streamlit as st
import google.generativeai as genai
import google.api_core.exceptions  # noqa: F401  (kept for error type-checks)
import firebase_admin
from firebase_admin import credentials, firestore
from groq import Groq
from openai import OpenAI


# =============================================================================
# BRANDING
# =============================================================================

LOGO_URL = "https://raw.githubusercontent.com/sixteenpython/advaitian-philosophy/main/figures/imath_logo.png"
MENTOR_DISPLAY_NAME = "ThinkMath's Digital Clone"


# =============================================================================
# CORE PROMPTS — kept lean to fit every provider's free tier
# =============================================================================

CONCIERGE_BRIEF = """You are ThinkMath — the Advaitian Socratic Mentor (ThinkMath.ai),
embodying the Advaitian Philosophy: every problem is a Seed-Elegance Connection
hidden beneath brute-force complexity, orchestrated around a Central Elegant
Point (CEP).

The student is greeting you or making small talk. Reply warmly, in 2-3 sentences.
Invite them to share their math problem so you can find its Seed together.
Do not lecture. Do not list archetypes. Do not give answers.

Identity rules:
- Your name is "ThinkMath" or "ThinkMath.ai".
- NEVER refer to yourself or the founder as "Anand". The founder's identity is private.

Math formatting:
- Inline math: $x$, $a^2$. Block math only when it stands alone: $$\\sum a_i$$
- NEVER use \\(...\\) or \\[...\\].

End every reply with this hidden metadata line, on its own line, exactly:
PHASE:1 TIER:3"""


CORE_BRIEF = """You are ThinkMath — the Advaitian Socratic Mentor (ThinkMath.ai),
the Digital Clone embodying the Advaitian Philosophy of Problem Solving.
You are a Structural Mirror, never a calculator.

# IDENTITY (strict)
- Your name is "ThinkMath" or "ThinkMath.ai".
- NEVER refer to yourself or the founder as "Anand". The founder's identity is private.
- If asked who built you: "I am ThinkMath, the mentor of the Advaitian Foundation."

# CORE PHILOSOPHY (one paragraph — internalise this)
Every mathematical problem is a Seed-Elegance Connection hidden beneath brute-force
complexity, orchestrated around a CENTRAL ELEGANT POINT (CEP) — the beautiful
mathematical object the problem is designed around. The SEED is the underlying
meta-pattern (Archetype). The BRUTE PATH is the mechanical approach students
naturally try. The ELEGANT PIVOT is the insight that makes the solution trivial.
ThinkMath.ai is not teaching mathematics — it is teaching Epistemology: how we
know what we know. Mastery is not solving 1000 problems; it is internalising 20
patterns and learning to see them everywhere, simultaneously, from multiple
directions at once.

# VOICE — THE THREE CONSTANTS (all tiers)
- WARM: you are on the student's side, always.
- PRECISE: name things exactly. Vague encouragement is noise.
- UNCOMPROMISING: never give the answer, not under any pressure.
- Make the student feel they discovered the truth — because they did.
- Name the trap, never shame the person.
- No closing signature. No "I am the engine" self-declarations.

# MATH FORMATTING (CRITICAL — wrong delimiters render as raw text)
- Inline math, in flowing prose: $x$, $a^2$, $n_1$, $\\sum a_i$.
- Block math, ONLY when standing alone on its own line:
    $$\\sum_{i=1}^n i = \\frac{n(n+1)}{2}$$
- NEVER wrap a single variable in $$...$$ — that creates an ugly centred line.
- NEVER use \\(...\\) or \\[...\\].

# TIER DETECTION (silent; set TIER 0–4 in metadata)
T0 (Ages 6–9): no notation, simple words, story-receptive
T1 (Ages 10–13): basic algebra, fractions, informal reasoning
T2 (Ages 14–16): formal notation, basic proofs, can handle abstraction
T3 (JEE/IMO aspirants): formal proofs, multi-archetype problems  ← DEFAULT
T4 (IMO/Putnam): deep theory, expects publication-grade rigour
If ambiguous: default ONE tier below your best guess. Recalibrate silently.
NEVER announce the tier to the student.

# TIER-SPECIFIC VOICE (vocabulary scales; philosophy stays identical)
T0 STORYTELLER: metaphor only ("the wind blew 4 bricks away"). NEVER use x,y,n
   or formal archetype names. Plant Invariance/Symmetry through story.
T1 CURIOUS COLLABORATOR: Equal Sign as a balance scale that "refuses to tip".
   Use the word "pattern" deliberately. The Inversion Method: ask the reverse
   question. Begin asking "why" — gentle absurdity only, never mockery.
T2 PHILOSOPHICAL CHALLENGER: Reductio ad Absurdum (full version). Begin naming
   archetypes by number. "Does the universe accept this answer?"
T3/T4 ADVAITIAN MENTOR: Three-Phase Protocol (below). All 20 archetypes active.
   Brutally precise, structurally uncompromising, warm underneath. Six-Point as
   final reward. Multidirectional convergence as solving strategy.

# THE THREE-PHASE SOCRATIC PROTOCOL (T3/T4 default)

PHASE 1 — SEED IDENTIFICATION
Mirror the problem back in 1–2 lines. Ask ONE diagnostic question that surfaces
what is invariant / what changes / what filters answers. NO solving. NO mechanism.
NO partial answer. The question must INVITE discovery, never telegraph the seed.

If the student says "I'm stuck" or asks for a hint, give a SOCRATIC PROBE — a
tiny concrete experiment they can run themselves: "Try the smallest non-trivial
case that satisfies ALL the stated constraints. What do you observe?" Do NOT
explain the mechanism, name the archetype, or state the rule. Each subsequent
stuck-message may reveal slightly more (Escape Hatch ladder below).

PHASE 2 — DIRECTIONS / BRUTE-WALL WARNING
Once the student has named a candidate seed, present 2–3 plausible Archetypes
from the 20 below. State why each fits. Ask which feels structural to them.

If the student asks for a BLEND of archetypes, declare ONE as PRIMARY (the engine
of the proof) and the others as SUPPORTING (frame, conclusion, sanity-check):
"Primary: Archetype X. Supporting: Y (frame), Z (closure)."
A blend without a named primary leaves the student with no centre of gravity.

PHASE 3 — CONVERGENCE & SIX-POINT COMMENTARY
Trigger when (a) the student articulates the elegant pivot themselves, OR
(b) they explicitly ask for "Stage 2", "Stage 2 commentary", "Six-Point",
"full commentary", or any equivalent.

CRITICAL: "Stage 2" is the user-facing name for the SIX-POINT COMMENTARY produced
in PHASE 3. When the student says "give me Stage 2", you DELIVER the Six-Point
in PHASE 3 — you do NOT regress to a Phase-2 directions table. Stage-2-the-output
lives in Phase-3-the-state. Never confuse them.

# MVC VALIDATION GATE (STRICT — between Phase 2 and Phase 3)
The Pivot in the MVC must be an OPERATIONAL move — a specific transformation,
substitution, geometric construction, named technique, descent step.

QUALIFIES (operational): "fix b, take the other Vieta root a'=kb-a, descend";
  "set the discriminant to a perfect square"; "apply Cauchy-Schwarz to (a,1)";
  "substitute u = x + 1/x"; "interpret a²-ac+c² as Law-of-Cosines length squared
  for sides a,c with included angle 60°".

DOES NOT QUALIFY (study habits, NOT pivots): "burn the candle from both ends",
  "try simple values", "look for symmetry", "use both approaches", "exploit the
  structure", "think outside the box", "use the CEP concept".

If operational AND consistent: reply EXACTLY: "Your MVC is solid. Ready for Stage 2."
If only meta-strategy: "Your meta-strategy is sound, but I need the operational
move. What specific transformation, substitution, or named technique will you apply?"

# PHASE 3 PRE-FLIGHT CHECKLIST (silent; complete BEFORE writing the Six-Point)

Step 1 — ENUMERATE EVERY CONSTRAINT from the problem statement. Write them down
silently before doing anything else. Examples of constraints students lose:
- Strict inequality chains: "a > b > c > d > 0" means NO TWO VARIABLES MAY BE
  EQUAL. (5,4,3,2) is valid; (2,1,1,1) is NOT.
- Type constraints: integers, positive integers, primes, naturals, reals.
- Distinctness clauses, parity clauses, coprimality clauses.
- Domain ranges: 0 < x < 1, n ≥ 2, etc.
A test case that violates any single constraint is INVALID — you may not draw
any conclusion from it.

Step 2 — CONSTRUCT TWO TEST CASES that simultaneously satisfy (a) every listed
constraint AND (b) the problem's defining equation/condition. If you cannot find
two such cases by inspection, search small integers up to ~30. If you still
cannot find any valid case, that is a clue about the problem itself — escalate
to Step 4 (refusal), do NOT pretend the pivot succeeded.

Step 3 — VERIFY YOUR ELEGANT PIVOT on both cases end-to-end. If the pivot cites
a NAMED THEOREM (Ptolemy, Vieta, Cauchy-Schwarz, AM-GM, Sophie Germain, LTE,
Power of a Point), you MUST also:
- State the theorem's exact form
- Label which problem quantities play which roles in the theorem
- Compute BOTH sides of the theorem on your test case and confirm equality
- Confirm any auxiliary claim (e.g. "this quantity is an integer", "this
  factor is > 1") on the same test case — DO NOT assert without checking.

Step 4 — REFUSE if anything is shaky. If verification fails OR you cannot
construct valid test cases OR the theorem labeling is uncertain, DO NOT deliver
Phase 3. Reply EXACTLY: "I am not confident in this pivot — verification on
case X does not close the proof. Let me reconsider with you rather than ship
a flawed argument." Then engage Socratically.

# HONESTY GATE FOR HARD PROBLEMS
For 3-archetype (Hard IMO P3-P5) and 4-archetype (Extreme IMO P6 / Putnam A6)
problems, proof correctness is a serious risk. Many such proofs are subtle and
not reliably encoded in any general LLM. For these:
- Bias HARD toward refusal over fabrication.
- If even ONE step in your derivation is asserted without verification, refuse.
- Prefer to walk the student through their OWN proof attempt, asking targeted
  questions, rather than presenting a fully-formed proof of your own.
A wrong proof in the TAKEAWAY commits a falsehood to the Advaitian Bible.
The Advaitian Bible accepts uncertainty. It does not accept falsehood.

# REPEATED PIVOT — TREAT AS COMMITMENT
If the student has already articulated an operational pivot in the recent
conversation and now repeats or restates it, treat the repetition as their
final commitment. Move directly to the Pre-Flight Checklist + Phase 3
delivery (or refusal). DO NOT loop back asking for "the operational move"
the student has already given you.

# THE SIX-POINT COMMENTARY (Phase 3 output — strict format with these headers)

🌱 SEED
[One sentence naming the archetype(s) by NUMBER + TITLE. Domain-general, reusable.
For blends, state Primary + Supporting explicitly.]

⚙️ BRUTE PATH
[Concrete step-by-step of the mechanical approach. Show actual equations.
Pinpoint exactly where it becomes blind/inefficient. Free of judgement.]

💡 ELEGANT PIVOT
[Name the insight. Show the mathematics. Make the convergence point explicit.
Should feel inevitable in hindsight, surprising before.]

⚠️ PITFALLS
[3–5 traps. Use canonical Advaitian labels from the PITFALL HALL OF FAME below
where applicable. Each: Memorable name | The thinking error | Why it tempts |
Actionable check.]

🔗 CONNECTIONS
A. Primary Archetype Applications (3–5 examples — same archetype elsewhere)
B. Alternative Solution Archetypes (3–5 — other archetype numbers solving THIS problem)
C. Cross-Domain Manifestations (3–5 — outside mathematics)

🏆 TAKEAWAY
[ONE sentence. Under 15 words. Actionable. Memorable. Quotable five years later.]

# THE 20 UNIVERSAL ARCHETYPES (with meta-principles)

STRUCTURE RECOGNITION
1. INVARIANCE — "If something stays constant, make it your anchor."
2. SYMMETRY — "If the problem has symmetry, the solution inherits it."
3. DUALITY — "If stuck in one language, switch to the dual."
4. HIDDEN STRUCTURE — "If unfamiliar, it's probably something familiar in disguise."

TRANSFORMATION
5. SUBSTITUTION — "The right coordinate system makes the problem trivial."
6. LINEARIZATION — "If nonlinear, find the linear core."
7. NORMALIZATION — "Remove the clutter; keep only what matters."
8. DOMAIN TRANSLATION — "If the language is wrong, speak a different one."

CONSTRAINT EXPLOITATION
9. DOMAIN CONSTRAINTS — "Algebra generates candidates; domain selects the winner."
10. INEQUALITY CONSTRAINTS — "Sometimes you don't need the answer — just its bounds."
11. EXISTENCE / UNIQUENESS — "Existence precedes computation."
12. EXTREMAL PRINCIPLES — "Nature optimizes; so should your solution."

COUNTING & EXTREMIZATION
13. COMBINATORIAL — "If you can't enumerate, structure the count."
14. PARITY / MODULARITY — "Sometimes the remainder tells the whole story."
15. BIJECTION — "If two problems are isomorphic, solve the simpler one."

META-REASONING
16. REVERSE ENGINEERING — "When the answer is given, the problem is to find the question."
17. DEGREES OF FREEDOM — "Count constraints before solving."
18. RECURSION / INDUCTION — "Solve for one step; repeat to infinity."
19. PIVOTING / ELIMINATION — "Simplify by subtraction, not addition."
20. ANALOGY / TRANSFER — "If you've solved it once, you've solved it everywhere."

# THE PITFALL HALL OF FAME (use these canonical names in the PITFALLS section)
P1 DOUBLE-ROOT TRAP — accepting both algebraic roots without domain validation
P2 UNIDIRECTIONAL WALL — committing to one archetype past where it stalls
P3 FORMULA BLINDNESS — reciting formula without knowing what it encodes
P4 CONSTRAINT IGNORANCE — solving before counting degrees of freedom
P5 ALGEBRAIC TRUST — trusting algebra without checking physical/geometric reality
P6 COMPLEXITY ADDITION — adding variables when stuck instead of eliminating
P7 SEED SKIPPING — calculating before identifying the structural archetype

# THE CEP LIBRARY (Central Elegant Points — name when matched in Phase 2 or later)
- Perfect square in divisibility condition  →  Vieta Jumping (e.g. IMO 1988 P6)
- Triangular number n(n+1)/2  →  AP / combinatorial sum disguise
- Pythagorean triple  →  algebraic identity factoring as a²+b²=c²
- Golden ratio φ  →  recursion aₙ₊₂ = aₙ₊₁ + aₙ
- √2, √3 as forced answer  →  integer constraints producing irrationals (descent)
- Fibonacci sequence  →  ratio of consecutive terms → φ
- 60°/120° complementary triangles  →  cyclic quadrilateral via Law of Cosines + Ptolemy
- 0 as only solution  →  descent + parity elimination
- e^(iπ)+1=0  →  trig + exponential hybrid
NEVER reveal the CEP in Phase 1. Hint at it in Phase 2 to anchor the search.

# COMPETITION PATTERNS (name the canonical technique up front in Phase 2)
- "(ab+1) | (a²+b²)" or quadratic Diophantine  →  VIETA JUMPING (12 + 16 + 18)
- f(f(x)) = x or self-composing functional eq  →  INVOLUTION / CAUCHY (1 + 4)
- "n objects in k bins, n > k"  →  PIGEONHOLE (17)
- max/min of expression with constraint  →  LAGRANGE / AM-GM / CAUCHY-SCHWARZ (12)
- Counting with overcounting  →  INCLUSION-EXCLUSION or BIJECTION (13, 15)
- Bounded sequence; show convergence  →  MONOTONE / BOLZANO (11)
- 60° + 120° angle pair sharing a side  →  Cyclic quadrilateral + Ptolemy (1, 8)

# KEY GEMS (operational tools — name when student stalls on mechanics)
A1 VIETA'S FORMULAS — roots' sum/product without finding roots
A2 SOPHIE GERMAIN — a⁴+4b⁴ = (a²+2b²+2ab)(a²+2b²−2ab)
A6 TELESCOPING — Σ[f(k+1)−f(k)] = f(n+1)−f(1)
B1 AM-GM — (a₁+...+aₙ)/n ≥ (a₁...aₙ)^(1/n)
B2 CAUCHY-SCHWARZ — (Σaᵢbᵢ)² ≤ (Σaᵢ²)(Σbᵢ²)
B6 TRIANGLE INEQUALITY
C1 FERMAT'S LITTLE THEOREM — aᵖ⁻¹ ≡ 1 (mod p)
C4 LIFTING THE EXPONENT (LTE)
D1 POWER OF A POINT — PA·PB = PC·PD
D2 PTOLEMY'S THEOREM — AC·BD = AB·CD + AD·BC for cyclic quadrilateral
D6 INVERSION — circles ↔ lines
G1 PIGEONHOLE PRINCIPLE

# ESCAPE HATCH LADDER (T3/T4 only; for repeated stuck-states)
1st stuck: Socratic probe — concrete experiment, no reveal
2nd stuck: ARCHETYPE NUDGE — reveal ONLY the primary archetype label, not the move
3rd stuck: DIRECTION MAP — reveal the multidirectional structure, not the convergence
4th stuck: PIVOT SHADOW — one-sentence silhouette of the pivot, not the answer
After all four exhausted: read the full Six-Point as a diagnostic; assign the
student to write the commentary from memory tomorrow.

# OPERATING MODES (recognise triggers; default to MODE A)
MODE A SOCRATIC SOLVING — student submits problem (default behaviour above)
MODE B COMMENTARY REVIEW — student submits their own Six-Point: assess each
   section against the framework. Grade: PUBLICATION READY / NEEDS REFINEMENT /
   BACK TO MVC. For each weakness, ONE targeted question only.
MODE C PROBLEM DESIGN — "design a problem": guide through 5-step CEP framework
   (1. Select CEP → 2. Select archetypes → 3. Design convergence → 4. Create
   traps → 5. Craft statement). You are collaborator here, not interrogator.
MODE D STRUCTURAL DIAGNOSIS — "how am I doing?": deliver session diagnosis
   (tier observed, archetypes demonstrated, blind spots, pitfall pattern,
   prescription, next session goal).
MODE E FIRST MINUTE TRAINING — "practice the First Minute Protocol":
   present problem → 60s → student names archetypes/difficulty/strategy → reveal
   internal diagnosis → discuss gaps.
MODE F TIER CALIBRATION — "what level am I at?": ask 2–3 abstraction-graded
   questions. Place silently. Never use the word "tier" to the student.

# DIFFICULTY CALIBRATION (T3/T4)
1-archetype: Easy textbook (3–8 min)  — move briskly; don't over-Socratise
2-archetype: Moderate–Hard JEE Adv (10–25 min)  — full 3-phase protocol
3-archetype: Hard IMO P3–P5 (25–50 min)  — extended Phase 2; patient Phase 3
4-archetype: Extreme IMO P6 / Putnam A6 (45–90 min)  — multi-session permitted

# 5-SECOND HEURISTIC (use to surface a candidate direction fast)
- "Does X exist?"           → Existence/Uniqueness (11)
- "Find max/min"            → Extremal (12) or Inequalities (10)
- Suspiciously clean numbers → Reverse Engineering (16)
- Mixes algebra + geometry  → Domain Translation (8) or Constraints (9)
- Something stays the same  → Invariance (1)

# FAILURE-STATE HANDLING
- Student guessing: "You're pattern-matching, not pattern-recognising. Slow down.
  What in the structure makes you say that?"
- Student frustrated: validate honestly ("This is a 3-archetype problem; IMO
  contestants spend 45 minutes here") then deploy escape-hatch ladder.
- Student demands the answer: "The answer you discover yourself is the one
  you'll remember. The one I hand you disappears by morning." Then escape hatch.
- Student proposes a novel approach: do NOT dismiss. Follow it structurally.
  If it works, log as Alternative Solution Archetype. If it stalls, ask "where
  exactly does it stop? What's the wall made of?"

# OUTPUT RULES (ALL TIERS)
- Plain markdown. Use the Six-Point emoji headers (🌱 ⚙️ 💡 ⚠️ 🔗 🏆) ONLY in Phase 3.
- No HTML tags inside content. No closing signature.
- Inline math $...$ for variables in prose; block math $$...$$ only when standalone.
- End EVERY reply with this hidden line, on its own line, exactly:
PHASE:[1/2/3] TIER:[0/1/2/3/4]
Do not explain the metadata to the student.

# LIVE DOCTRINE NOTE
Below this protocol you may see a section titled "LIVE DOCTRINE FROM
knowledge_base/". Those passages are auto-loaded from the Advaitian
Foundation's source files on each turn. Treat them as authoritative
philosophical context that supersedes anything ambiguous above. The
protocol governs YOUR engagement; the doctrine governs what is TRUE."""


# =============================================================================
# CONSTANTS
# =============================================================================

MAX_OUTPUT_TOKENS = {
    "concierge": 256,
    1: 700,
    2: 900,
    3: 5000,
}

GREETING_PATTERNS = {
    "hi", "hello", "hey", "yo", "namaste", "namaskar", "namaskaram", "pranam",
    "vanakkam", "good morning", "good afternoon", "good evening", "hola", "salaam",
    "hi there", "hello there", "hey there",
}

CANNED_GREETING = (
    "Namaste. I am the ThinkMath.ai Socratic Mentor.\n\n"
    "Share your problem and we will find its **Seed** together.\n\n"
    "I will never give you the answer. I will give you something better — the "
    "structural instinct to find it yourself, and to recognise it the next time it "
    "appears in disguise.\n\n"
    "*What problem are you working on today?*"
)

KNOWN_GEMINI_MODELS = [
    "gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-2.5-pro",
    "gemini-2.0-flash", "gemini-2.0-flash-lite",
    "gemini-1.5-flash", "gemini-1.5-flash-8b",
]
KNOWN_GROQ_MODELS = [
    "llama-3.3-70b-versatile", "llama-3.1-8b-instant",
    "meta-llama/llama-4-scout-17b-16e-instruct",
    "meta-llama/llama-4-maverick-17b-128e-instruct",
    "deepseek-r1-distill-llama-70b", "qwen-qwq-32b",
    "gemma2-9b-it", "mistral-saba-24b",
]
KNOWN_SAMBANOVA_MODELS = [
    "Meta-Llama-3.3-70B-Instruct", "Meta-Llama-3.1-70B-Instruct",
    "Meta-Llama-3.1-8B-Instruct", "DeepSeek-V3-0324", "DeepSeek-R1",
    "Llama-4-Maverick-17B-128E-Instruct",
    "Llama-3.3-Swallow-70B-Instruct-v0.4",
    "Qwen3-32B", "Qwen2.5-Coder-32B-Instruct",
]

EXCLUDE_SUBSTRINGS = (
    "embedding", "embed", "whisper", "tts", "imagen", "image", "vision",
    "guard", "aqa", "code-gecko",
)


# =============================================================================
# LIVE KNOWLEDGE BASE — auto-loaded from knowledge_base/ on every request,
# hot-reloaded when any file changes. The user maintains the doctrine; the
# engine auto-rebalances. No code change required when knowledge_base/ is
# updated and committed.
# =============================================================================

KB_DIR_NAME = "knowledge_base"
# Total budget chosen so that:
#   CORE_BRIEF (~4.4K tokens) + KB doctrine (~2.7K tokens) + history + user input
#   ≈ 7K-8K input tokens — fits Groq 70B/120B (32K-128K ctx) and all SambaNova /
#   Gemini models comfortably. Groq 8B (8K ctx) drops out of the ladder for
#   long turns; the circuit breaker handles that automatically.
KB_BUDGET_CHARS = 11000     # ~2750 tokens total across all files
KB_PER_FILE_CAP = 10500     # ~2625 tokens per file (enough for the full Master Framework)
KB_FILE_EXTS = (".md", ".txt")

# Files starting with these prefixes are considered "engine-internal" and skipped.
KB_SKIP_PREFIXES = ("_", ".")

# Module-level cache (persists across Streamlit reruns within a process).
_KB_CACHE: dict = {"signature": None, "data": None, "loaded_at": 0.0}


def _find_kb_dir() -> str | None:
    """Locate knowledge_base/ — search common deployment layouts."""
    here = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.normpath(os.path.join(here, "..", KB_DIR_NAME)),  # commentary_engine/../knowledge_base
        os.path.normpath(os.path.join(here, KB_DIR_NAME)),        # commentary_engine/knowledge_base
        os.path.normpath(os.path.join(here, "..", "..", KB_DIR_NAME)),
        os.path.normpath(os.path.join(os.getcwd(), KB_DIR_NAME)),
    ]
    for c in candidates:
        if os.path.isdir(c):
            return c
    return None


def _kb_signature(kb_dir: str) -> tuple:
    """A cheap fingerprint of (filename, mtime, size) tuples — used to detect change."""
    sig = []
    try:
        for name in sorted(os.listdir(kb_dir)):
            if not name.endswith(KB_FILE_EXTS) or name.startswith(KB_SKIP_PREFIXES):
                continue
            path = os.path.join(kb_dir, name)
            try:
                stat = os.stat(path)
                sig.append((name, stat.st_mtime, stat.st_size))
            except OSError:
                pass
    except OSError:
        return ()
    return tuple(sig)


def _load_kb_doctrine(kb_dir: str) -> dict:
    """Read and concatenate KB files into a single doctrine string within budget."""
    pieces: list[str] = []
    files_loaded: list[tuple[str, int, bool]] = []  # (name, chars, truncated?)
    files_skipped: list[str] = []
    used = 0

    candidates = sorted(
        f for f in os.listdir(kb_dir)
        if f.endswith(KB_FILE_EXTS) and not f.startswith(KB_SKIP_PREFIXES)
    )

    for name in candidates:
        path = os.path.join(kb_dir, name)
        try:
            with open(path, encoding="utf-8") as f:
                text = f.read().strip()
        except Exception:
            continue
        if not text:
            continue

        truncated = False
        if len(text) > KB_PER_FILE_CAP:
            text = text[:KB_PER_FILE_CAP].rstrip() + "\n[…file truncated to fit prompt budget]"
            truncated = True

        header = f"\n--- knowledge_base/{name} ---\n"
        block = header + text + "\n"

        if used + len(block) > KB_BUDGET_CHARS:
            files_skipped.append(name)
            continue

        pieces.append(block)
        files_loaded.append((name, len(text), truncated))
        used += len(block)

    body = "".join(pieces)
    fingerprint = hashlib.sha256(body.encode("utf-8")).hexdigest()[:10] if body else ""

    return {
        "body": body,
        "fingerprint": fingerprint,
        "files_loaded": files_loaded,
        "files_skipped": files_skipped,
        "total_chars": used,
        "kb_dir": kb_dir,
    }


def get_live_kb() -> dict | None:
    """Return current KB state. Hot-reloads when any file's mtime/size changes."""
    kb_dir = _find_kb_dir()
    if not kb_dir:
        return None
    sig = _kb_signature(kb_dir)
    if not sig:
        return None
    if _KB_CACHE["signature"] != sig:
        _KB_CACHE["data"] = _load_kb_doctrine(kb_dir)
        _KB_CACHE["signature"] = sig
        _KB_CACHE["loaded_at"] = time.time()
    return _KB_CACHE["data"]


KB_DOCTRINE_HEADER = (
    "\n\n# ───────── LIVE DOCTRINE FROM knowledge_base/ ─────────\n"
    "The sections below are loaded directly from the knowledge_base/ folder "
    "maintained by the Advaitian Foundation. They reflect the latest committed "
    "version of the philosophical source-of-truth.\n"
    "If anything below clarifies, sharpens, or contradicts the protocol above, "
    "TREAT THE DOCTRINE AS AUTHORITATIVE. The protocol above describes HOW you "
    "engage; the doctrine below describes WHAT you teach."
)


def assemble_system_prompt(kb_state: dict | None) -> str:
    """Compose the final system prompt: skeleton CORE_BRIEF + live doctrine."""
    if not kb_state or not kb_state["body"]:
        return CORE_BRIEF
    return CORE_BRIEF + KB_DOCTRINE_HEADER + kb_state["body"]


# =============================================================================
# LATEX NORMALISER — convert any \( \) / \[ \] to $ $ / $$ $$
# =============================================================================

# \[ ... \]  →  $$ ... $$
_BLOCK_LATEX_RE = re.compile(r"\\\[(.*?)\\\]", re.DOTALL)
# \( ... \)  →  $ ... $
_INLINE_LATEX_RE = re.compile(r"\\\((.*?)\\\)", re.DOTALL)


def normalise_math(text: str) -> str:
    """Convert TeX-style \\(...\\) / \\[...\\] to Streamlit/KaTeX $...$ / $$...$$."""
    if not text:
        return text
    text = _BLOCK_LATEX_RE.sub(lambda m: f"$${m.group(1).strip()}$$", text)
    text = _INLINE_LATEX_RE.sub(lambda m: f"${m.group(1).strip()}$", text)
    # Also defensively replace any leftover "Anand" → "ThinkMath" if a fallback
    # model ignores the system prompt.
    text = re.sub(r"\bAnand['']?s?\b", "ThinkMath", text)
    return text


# =============================================================================
# CREDENTIALS
# =============================================================================

def _try_load_keys_module(path: str) -> dict:
    try:
        if not os.path.exists(path):
            return {}
        spec = importlib.util.spec_from_file_location("_local_keys", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)  # type: ignore[union-attr]
        return {
            k: getattr(mod, k)
            for k in ("GEMINI_API_KEY", "GROQ_API_KEY", "SAMBANOVA_API_KEY")
            if hasattr(mod, k)
        }
    except Exception:
        return {}


def _clean(val):
    return val.strip().strip('"').strip("'") if val else None


@st.cache_resource
def get_credentials():
    api_k = groq_k = samba_k = None
    fb_cred = None

    try:
        if hasattr(st, "secrets") and st.secrets:
            api_k = api_k or st.secrets.get("GEMINI_API_KEY")
            groq_k = groq_k or st.secrets.get("GROQ_API_KEY")
            samba_k = samba_k or st.secrets.get("SAMBANOVA_API_KEY")
            if "firebase" in st.secrets:
                fb_cred = dict(st.secrets["firebase"])
    except Exception:
        pass

    here = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(here, "credentials.py"),
        os.path.join(here, "local_keys.py"),
        os.path.join(here, "..", "credentials.py"),
        os.path.join(here, "..", "local_keys.py"),
    ]
    for path in candidates:
        keys = _try_load_keys_module(path)
        api_k = api_k or keys.get("GEMINI_API_KEY")
        groq_k = groq_k or keys.get("GROQ_API_KEY")
        samba_k = samba_k or keys.get("SAMBANOVA_API_KEY")

    search_paths = [here, os.path.dirname(here), os.getcwd()]
    plain_files = {
        "GEMINI_API_KEY": ["AIzaSyCFoDs_OGzL65bacvVJzipZsxWx6YF.txt", "gemini_api_key.txt"],
        "GROQ_API_KEY": ["groq_api_key.txt", "groq_key.txt"],
        "SAMBANOVA_API_KEY": ["samba_api_key.txt", "samba_key.txt", "sambanova_api_key.txt"],
    }
    for key_name, filenames in plain_files.items():
        for p in search_paths:
            for fn in filenames:
                fp = os.path.join(p, fn)
                if os.path.exists(fp):
                    try:
                        with open(fp, "r", encoding="utf-8") as f:
                            val = f.read()
                        if key_name == "GEMINI_API_KEY" and not api_k:
                            api_k = val
                        elif key_name == "GROQ_API_KEY" and not groq_k:
                            groq_k = val
                        elif key_name == "SAMBANOVA_API_KEY" and not samba_k:
                            samba_k = val
                    except Exception:
                        pass

    api_k = api_k or os.environ.get("GEMINI_API_KEY")
    groq_k = groq_k or os.environ.get("GROQ_API_KEY")
    samba_k = samba_k or os.environ.get("SAMBANOVA_API_KEY")

    if not fb_cred:
        for p in search_paths:
            fp = os.path.join(p, "advaitian-commentary-engine-firebase-adminsdk-fbsvc-70e4298d89.json")
            if os.path.exists(fp):
                fb_cred = fp
                break

    return _clean(api_k), fb_cred, _clean(groq_k), _clean(samba_k)


GEMINI_KEY, FIREBASE_CRED, GROQ_KEY, SAMBA_KEY = get_credentials()


# =============================================================================
# DYNAMIC MODEL DISCOVERY
# =============================================================================

@st.cache_data(ttl=3600, show_spinner=False)
def discover_models(gemini_key, groq_key, samba_key):
    models = []

    gemini_names = []
    if gemini_key:
        try:
            genai.configure(api_key=gemini_key)
            for m in genai.list_models():
                methods = getattr(m, "supported_generation_methods", []) or []
                if "generateContent" not in methods:
                    continue
                name = m.name.replace("models/", "")
                if any(x in name.lower() for x in EXCLUDE_SUBSTRINGS):
                    continue
                gemini_names.append(name)
        except Exception:
            gemini_names = []
    if not gemini_names:
        gemini_names = list(KNOWN_GEMINI_MODELS)
    gemini_names = sorted(set(gemini_names))

    for name in gemini_names:
        models.append({
            "provider": "Gemini", "model": name,
            "score": _score_model(name), "context": _gemini_context(name),
        })

    groq_names = []
    if groq_key:
        try:
            client = Groq(api_key=groq_key)
            resp = client.models.list()
            for m in (resp.data or []):
                if not getattr(m, "active", True):
                    continue
                if any(x in m.id.lower() for x in EXCLUDE_SUBSTRINGS):
                    continue
                groq_names.append(m.id)
        except Exception:
            groq_names = []
    if not groq_names:
        groq_names = list(KNOWN_GROQ_MODELS)
    groq_names = sorted(set(groq_names))

    for name in groq_names:
        models.append({
            "provider": "Groq", "model": name,
            "score": _score_model(name), "context": 8192,
        })

    samba_names = []
    if samba_key:
        try:
            client = OpenAI(api_key=samba_key, base_url="https://api.sambanova.ai/v1")
            resp = client.models.list()
            for m in (resp.data or []):
                if any(x in m.id.lower() for x in EXCLUDE_SUBSTRINGS):
                    continue
                samba_names.append(m.id)
        except Exception:
            samba_names = []
    if not samba_names:
        samba_names = list(KNOWN_SAMBANOVA_MODELS)
    samba_names = sorted(set(samba_names))

    for name in samba_names:
        models.append({
            "provider": "SambaNova", "model": name,
            "score": _score_model(name), "context": 8192,
        })

    return models


def _score_model(name: str) -> int:
    n = name.lower()
    score = 5
    if "pro" in n and "gemini" in n: score += 4
    elif "405b" in n or "400b" in n: score += 5
    elif "120b" in n: score += 4
    elif "70b" in n or "72b" in n: score += 3
    elif "maverick" in n: score += 3
    elif "32b" in n or "27b" in n: score += 2
    elif "scout-17b" in n or "17b" in n: score += 1
    elif "12b" in n or "9b" in n: score += 0
    elif "8b" in n or "7b" in n: score -= 1
    elif "lite" in n or "nano" in n or "mini" in n or "flash-8b" in n: score -= 2
    if "thinking" in n or "reasoning" in n: score += 2
    if "deepseek" in n: score += 2
    if "qwq" in n or "qwen3" in n: score += 1
    if "instant" in n: score -= 1
    if "preview" in n or "experimental" in n or "-exp" in n: score -= 5
    if "alpha" in n or "beta" in n: score -= 3
    return max(0, min(10, score))


def _gemini_context(name: str) -> int:
    n = name.lower()
    if "1.5" in n: return 1_000_000
    if "2.5-pro" in n or "2.0-pro" in n: return 2_000_000
    if "2.5-flash" in n or "2.0-flash" in n: return 1_000_000
    return 32_768


# =============================================================================
# QUOTA STATE
# =============================================================================

def _now_ts() -> float:
    return datetime.now(timezone.utc).timestamp()


def _seconds_until_pt_midnight() -> int:
    now_utc = datetime.now(timezone.utc)
    pt_offset = timedelta(hours=-8)
    now_pt = now_utc + pt_offset
    next_midnight_pt = (now_pt + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    return int((next_midnight_pt - now_pt).total_seconds()) + 60


def _model_key(provider: str, model: str) -> str:
    return f"{provider}::{model}"


def is_blocked(provider: str, model: str) -> bool:
    state = st.session_state.quota_state.get(_model_key(provider, model))
    if not state:
        return False
    return _now_ts() < state["blocked_until"]


def block_model(provider: str, model: str, seconds: int, reason: str):
    st.session_state.quota_state[_model_key(provider, model)] = {
        "blocked_until": _now_ts() + max(5, seconds),
        "reason": reason,
        "blocked_at": _now_ts(),
    }


def parse_retry_seconds(error_str: str) -> int:
    m = re.search(r"retry_delay\s*\{\s*seconds:\s*(\d+)", error_str)
    if m: return int(m.group(1)) + 1
    m = re.search(r"retry in (\d+(?:\.\d+)?)s", error_str, re.I)
    if m: return int(float(m.group(1))) + 1
    m = re.search(r"try again in (\d+(?:\.\d+)?)\s*(?:s|sec|second)", error_str, re.I)
    if m: return int(float(m.group(1))) + 1
    return 60


def classify_error(error_str: str) -> str:
    s = error_str.lower()
    if "limit: 0" in s or "perdayper" in s.replace(" ", "") or "rpd" in s or "per day" in s:
        return "daily_quota"
    if "request too large" in s or "413" in s or "tokens per minute" in s:
        return "tpm_too_small"
    if "429" in s or "quota" in s or "rate limit" in s or "rate_limit" in s:
        return "minute_quota"
    if "401" in s or "403" in s or "api_key" in s or "unauthorized" in s or "permission" in s:
        return "auth"
    if "404" in s or "not found" in s or "model not found" in s:
        return "not_found"
    if "500" in s or "502" in s or "503" in s or "504" in s or "timeout" in s or "network" in s:
        return "transient"
    return "fatal"


# =============================================================================
# PROVIDER WRAPPERS
# =============================================================================

class BaseWrapper:
    provider: str = "Base"

    def __init__(self, model_name: str, system_instruction: str):
        self.model_name = model_name
        self.system_instruction = system_instruction

    def send(self, user_message: str, history: list, max_output_tokens: int) -> str:
        raise NotImplementedError


class GeminiWrapper(BaseWrapper):
    provider = "Gemini"

    def __init__(self, model_name, system_instruction):
        super().__init__(model_name, system_instruction)
        genai.configure(api_key=GEMINI_KEY)
        self._model = genai.GenerativeModel(
            model_name=model_name,
            system_instruction=system_instruction,
            generation_config={"temperature": 0.3, "top_p": 0.95},
        )

    def send(self, user_message, history, max_output_tokens):
        gemini_history = []
        for m in history:
            role = "user" if m["role"] == "user" else "model"
            gemini_history.append({"role": role, "parts": [m["content"]]})
        chat = self._model.start_chat(history=gemini_history)
        resp = chat.send_message(
            user_message,
            generation_config={"max_output_tokens": max_output_tokens, "temperature": 0.3},
        )
        if not resp.candidates or not getattr(resp.candidates[0], "content", None):
            raise RuntimeError("Empty response from Gemini")
        return resp.text


class GroqWrapper(BaseWrapper):
    provider = "Groq"

    def __init__(self, model_name, system_instruction):
        super().__init__(model_name, system_instruction)
        self._client = Groq(api_key=GROQ_KEY)

    def send(self, user_message, history, max_output_tokens):
        msgs = [{"role": "system", "content": self.system_instruction}]
        for m in history:
            role = "user" if m["role"] == "user" else "assistant"
            msgs.append({"role": role, "content": m["content"]})
        msgs.append({"role": "user", "content": user_message})
        completion = self._client.chat.completions.create(
            model=self.model_name,
            messages=msgs,
            temperature=0.3,
            max_tokens=max_output_tokens,
        )
        return completion.choices[0].message.content or ""


class SambaWrapper(BaseWrapper):
    provider = "SambaNova"

    def __init__(self, model_name, system_instruction):
        super().__init__(model_name, system_instruction)
        self._client = OpenAI(api_key=SAMBA_KEY, base_url="https://api.sambanova.ai/v1")

    def send(self, user_message, history, max_output_tokens):
        msgs = [{"role": "system", "content": self.system_instruction}]
        for m in history:
            role = "user" if m["role"] == "user" else "assistant"
            msgs.append({"role": role, "content": m["content"]})
        msgs.append({"role": "user", "content": user_message})
        completion = self._client.chat.completions.create(
            model=self.model_name,
            messages=msgs,
            temperature=0.3,
            max_tokens=max_output_tokens,
        )
        return completion.choices[0].message.content or ""


WRAPPER_CLASS = {"Gemini": GeminiWrapper, "Groq": GroqWrapper, "SambaNova": SambaWrapper}


def get_wrapper(provider: str, model: str, system_prompt: str) -> BaseWrapper:
    cache = st.session_state.wrapper_cache
    key = f"{provider}::{model}::{sha1(system_prompt.encode()).hexdigest()[:8]}"
    if key not in cache:
        cls = WRAPPER_CLASS[provider]
        cache[key] = cls(model, system_prompt)
    return cache[key]


# =============================================================================
# INTENT & LADDER
# =============================================================================

MATH_HINTS = re.compile(
    r"[\d=+\-*/^√∑∫∞≤≥≠π]|"
    r"\b(prove|find|solve|show|let|suppose|integer|prime|odd|even|sum|product|"
    r"polynomial|equation|inequality|triangle|circle|matrix|vector|integral|"
    r"derivative|limit|series|sequence|theorem|axiom|archetype|seed|pivot)\b",
    re.I,
)


def detect_intent(text: str) -> str:
    cleaned = text.strip().lower()
    if cleaned in GREETING_PATTERNS:
        return "greeting"
    if len(cleaned.split()) <= 2 and not MATH_HINTS.search(text):
        return "greeting"
    if MATH_HINTS.search(text) or len(text) > 60:
        return "math"
    return "math"


def build_ladder(intent: str, all_models: list) -> list:
    available = [m for m in all_models if not is_blocked(m["provider"], m["model"])]
    if not available:
        return []
    if intent == "greeting":
        fast = [m for m in available if m["score"] <= 5]
        return sorted(fast or available, key=lambda m: (m["score"], m["model"]))
    ranked = sorted(available, key=lambda m: -m["score"])
    return _interleave_by_provider(ranked)


def _interleave_by_provider(models: list) -> list:
    by_provider = {}
    for m in models:
        by_provider.setdefault(m["provider"], []).append(m)
    out = []
    while any(by_provider.values()):
        for p in list(by_provider.keys()):
            if by_provider[p]:
                out.append(by_provider[p].pop(0))
    return out


# =============================================================================
# ORCHESTRATOR
# =============================================================================

def chat(user_input: str, history: list, all_models: list, status_writer=None):
    intent = detect_intent(user_input)

    if intent == "greeting" and not history:
        return CANNED_GREETING + "\n\nPHASE:1 TIER:3", "Local", "canned"

    if intent == "greeting":
        system_prompt = CONCIERGE_BRIEF
        max_tok = MAX_OUTPUT_TOKENS["concierge"]
    else:
        # Hot-reload knowledge_base/ on every math turn — any commit/push
        # to that folder is reflected in the doctrine without restart.
        system_prompt = assemble_system_prompt(get_live_kb())
        phase = st.session_state.get("current_phase", 1)
        # Stage-2 / Six-Point requests need Phase-3 budget regardless of current_phase.
        ui_low = user_input.lower()
        wants_six_point = (
            "stage 2" in ui_low or "stage-2" in ui_low or "six-point" in ui_low or
            "six point" in ui_low or "full commentary" in ui_low or
            "phase 3" in ui_low or "phase-3" in ui_low
        )
        if wants_six_point:
            phase = 3
        max_tok = MAX_OUTPUT_TOKENS.get(phase, 900)

    ladder = build_ladder(intent, all_models)
    if not ladder:
        raise RuntimeError(
            "All models are currently rate-limited. "
            "Try again in a minute, or add a paid-tier key."
        )

    if status_writer:
        status_writer.write(
            f"Intent: **{intent}** · Ladder length: {len(ladder)} · "
            f"Output cap: {max_tok} tokens"
        )

    last_error = None
    for m in ladder:
        provider, model = m["provider"], m["model"]
        if status_writer:
            status_writer.write(f"→ Trying **{provider}** · `{model}` (score {m['score']})")
        try:
            short_history = history[-6:]
            wrapper = get_wrapper(provider, model, system_prompt)
            text = wrapper.send(user_input, short_history, max_tok)
            if not text or not text.strip():
                raise RuntimeError("empty response")
            return text, provider, model
        except Exception as e:
            err = str(e)
            kind = classify_error(err)
            last_error = e
            if status_writer:
                status_writer.write(f"   ✗ {kind}: {err[:120]}")
            if kind == "daily_quota":
                block_model(provider, model, _seconds_until_pt_midnight(), "daily quota exhausted")
            elif kind == "minute_quota":
                block_model(provider, model, parse_retry_seconds(err), "rate-limited per minute")
            elif kind == "tpm_too_small":
                block_model(provider, model, 6 * 3600, "TPM cap < prompt size")
            elif kind == "not_found":
                block_model(provider, model, 24 * 3600, "model id no longer valid")
            elif kind == "auth":
                block_model(provider, model, 3600, "auth failure")
            elif kind == "transient":
                block_model(provider, model, 30, "transient error")
            else:
                block_model(provider, model, 60, f"fatal: {err[:60]}")
            continue

    raise RuntimeError(f"All {len(ladder)} models failed. Last error: {last_error}")


# =============================================================================
# RESPONSE PARSING
# =============================================================================

PHASE_TIER_RE = re.compile(r"^\s*PHASE:\s*(\d+)\s+TIER:\s*(\d+)\s*$", re.M)


def parse_metadata(response_text: str):
    phase, tier = 1, 3
    match = PHASE_TIER_RE.search(response_text or "")
    if match:
        try:
            phase = int(match.group(1))
            tier = int(match.group(2))
        except Exception:
            pass
        clean = PHASE_TIER_RE.sub("", response_text).strip()
    else:
        clean = (response_text or "").strip()
    return clean, phase, tier


# =============================================================================
# FIREBASE
# =============================================================================

def init_firebase():
    if not FIREBASE_CRED:
        return None
    if firebase_admin._apps:
        return firestore.client()
    try:
        cred = (
            credentials.Certificate(FIREBASE_CRED)
            if isinstance(FIREBASE_CRED, dict) or os.path.exists(FIREBASE_CRED)
            else None
        )
        if cred is None:
            return None
        firebase_admin.initialize_app(cred)
        return firestore.client()
    except Exception:
        return None


def save_session_to_firebase(messages, phase, tier):
    try:
        db = init_firebase()
        if not db: return
        db.collection("sessions").document().set({
            "messages": [{"role": m["role"], "content": m["content"]} for m in messages],
            "final_phase": phase, "detected_tier": tier,
            "timestamp": firestore.SERVER_TIMESTAMP,
            "message_count": len(messages),
        })
    except Exception:
        pass


def save_commentary_to_firebase(problem, commentary, tier):
    try:
        db = init_firebase()
        if not db: return False
        db.collection("commentaries").document().set({
            "problem": problem, "commentary": commentary, "tier": tier,
            "timestamp": firestore.SERVER_TIMESTAMP, "status": "generated",
        })
        return True
    except Exception:
        return False


# =============================================================================
# UI — Streamlit, BRIGHT ACADEMIC theme + iMaTh logo
# =============================================================================

st.set_page_config(
    page_title="ThinkMath.ai",
    page_icon=LOGO_URL,
    layout="wide",
    initial_sidebar_state="auto",
)

# =============================================================================
# ADMIN GATE — sidebar is visible only to the team via ?admin=<PIN>
# Configure the PIN via Streamlit Secrets:  ADMIN_PIN = "your-secret"
# Default fallback is "vriddhi-2026" (change before any public deploy).
# =============================================================================

ADMIN_PIN_DEFAULT = "vriddhi-2026"
try:
    ADMIN_PIN = (
        st.secrets.get("ADMIN_PIN", ADMIN_PIN_DEFAULT)
        if hasattr(st, "secrets") else ADMIN_PIN_DEFAULT
    )
except Exception:
    ADMIN_PIN = ADMIN_PIN_DEFAULT

try:
    _qp_admin = st.query_params.get("admin")
except Exception:
    _qp_admin = None

ADMIN_MODE = bool(_qp_admin) and _qp_admin == ADMIN_PIN

# When NOT in admin mode, hide the sidebar AND its toggle entirely.
if not ADMIN_MODE:
    st.markdown(
        """
        <style>
            section[data-testid="stSidebar"]              { display: none !important; }
            button[data-testid="collapsedControl"]        { display: none !important; }
            [data-testid="stSidebarCollapseButton"]       { display: none !important; }
            [data-testid="stSidebarCollapsedControl"]     { display: none !important; }
            /* Reclaim the horizontal space the sidebar would have used */
            [data-testid="stAppViewContainer"] > .main    { margin-left: 0 !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )

st.markdown("""
    <style>
    /* ── BASE ── */
    html, body, [class*="css"] {
        font-family: 'Segoe UI', Arial, sans-serif !important;
        font-size: 15px;
        line-height: 1.75;
        color: #2d1f0e;
    }
    .stApp { background-color: #ffffff; }

    /* ── SIDEBAR ── */
    section[data-testid="stSidebar"] {
        background-color: #f9f6f1 !important;
        border-right: 1px solid #ddd5c0;
        font-family: 'Segoe UI', Arial, sans-serif;
    }
    /* Color cascade for text only — DO NOT touch font-family on * because
       that breaks Material Symbols icons (expander chevron, etc.) */
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span:not([class*="material"]):not([class*="Icon"]),
    section[data-testid="stSidebar"] div:not([class*="material"]):not([class*="Icon"]),
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] h4,
    section[data-testid="stSidebar"] h5,
    section[data-testid="stSidebar"] h6,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] a {
        color: #2d1f0e !important;
    }
    /* Make sure Material Symbols icons keep their icon font */
    section[data-testid="stSidebar"] [class*="material-symbols"],
    section[data-testid="stSidebar"] [class*="material-icons"],
    section[data-testid="stSidebar"] [data-testid*="Icon"] {
        font-family: 'Material Symbols Outlined', 'Material Symbols Rounded',
                     'Material Symbols Sharp', 'Material Icons' !important;
        color: #5c3d1e !important;
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

    /* ── CHAT MESSAGES (st.chat_message) ── */
    /* Hide default avatars to get the clean card look */
    [data-testid="stChatMessageAvatarUser"],
    [data-testid="stChatMessageAvatarAssistant"],
    [data-testid="stChatMessageAvatarCustom"] {
        display: none !important;
    }
    /* Card body */
    [data-testid="stChatMessage"] {
        background-color: #faf7f2 !important;
        border-left: 4px solid #5c3d1e !important;
        border-radius: 8px !important;
        padding: 14px 18px !important;
        margin: 10px 0 !important;
        box-shadow: 0 1px 4px rgba(92,61,30,0.08) !important;
    }
    /* User card variant — tint + accent green */
    [data-testid="stChatMessage"]:has([data-testid="stChatMessageContent-user"]) {
        background-color: #f4f0e8 !important;
        border-left: 4px solid #8db543 !important;
    }
    /* Header strip inside cards */
    .card-role {
        color: #5c3d1e;
        font-size: 0.78em;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        font-weight: 700;
        margin-bottom: 4px;
    }
    .card-footer {
        font-size: 0.7em;
        color: #a08866;
        margin-top: 8px;
        border-top: 1px solid #ece4d2;
        padding-top: 4px;
    }

    /* ── INPUT ── */
    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea,
    [data-testid="stChatInput"] textarea {
        background-color: #ffffff !important;
        color: #2d1f0e !important;
        border: 1px solid #ddd5c0 !important;
        border-radius: 8px !important;
        font-family: 'Segoe UI', Arial, sans-serif !important;
    }
    /* Make the chat input a true paragraph-sized box (4-6 lines tall) */
    [data-testid="stChatInput"] textarea {
        min-height: 110px !important;
        max-height: 320px !important;
        font-size: 1rem !important;
        line-height: 1.55 !important;
        padding: 12px 14px !important;
    }
    [data-testid="stChatInput"] textarea:focus {
        border: 2px solid #8db543 !important;
        outline: none !important;
    }

    /* ── HEADER CARDS (top-of-page band) ── */
    /* st.container(border=True) renders this wrapper — we restyle it to match
       the cream academic theme. */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #faf7f2 !important;
        border: 1px solid #ddd5c0 !important;
        border-radius: 10px !important;
        padding: 10px 14px !important;
    }
    /* Tint the third header card (donate) green */
    div[data-testid="column"]:nth-child(3) [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #f4f0e8 !important;
        border-color: #8db543 !important;
    }
    .header-title {
        color: #5c3d1e;
        font-size: 0.75em;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        font-weight: 700;
        margin-bottom: 4px;
    }
    .header-progress-row {
        display: flex;
        gap: 14px;
        flex-wrap: wrap;
        margin-top: 6px;
        font-size: 0.92em;
        line-height: 1.6;
    }
    .header-donate-quote {
        font-size: 0.78em;
        color: #5c3d1e;
        line-height: 1.4;
        margin: 0 0 6px 0;
        font-style: italic;
    }
    .admin-pill {
        background: #5c3d1e;
        color: #faf7f2 !important;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 0.7em;
        font-weight: 700;
        letter-spacing: 0.5px;
        display: inline-block;
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
    .phase-active   { color: #8db543 !important; font-weight: bold; }
    .phase-complete { color: #5c3d1e !important; }
    .phase-inactive { color: #bbb0a0 !important; }

    /* ── STATUS PILL ── */
    .status-pill {
        background-color: #f0f7e6;
        border: 1px solid #8db543;
        color: #5c3d1e;
        border-radius: 6px;
        padding: 6px 10px;
        font-size: 0.85em;
        margin: 4px 0;
        display: block;
    }
    .status-pill.warn {
        background-color: #fdf6e3;
        border-color: #d6a93b;
        color: #6c4f17;
    }
    .status-pill.dim {
        background-color: #f4f0e8;
        border-color: #ddd5c0;
        color: #7a6040;
    }

    /* ── TIER BADGE ── */
    .tier-badge {
        background-color: #f4f0e8;
        border: 1px solid #8db543;
        color: #5c3d1e;
        border-radius: 20px;
        padding: 4px 12px;
        font-size: 0.8em;
        display: inline-block;
        margin-bottom: 8px;
    }

    /* ── DONATE ── */
    .donate-section {
        background-color: #f4f0e8;
        border: 1px solid #8db543;
        border-radius: 10px;
        padding: 16px;
        margin-top: 12px;
        text-align: center;
    }
    .donate-section p { color: #5c3d1e !important; }

    /* ── DIVIDERS / SCROLLBARS ── */
    hr { border-color: #ddd5c0 !important; }
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background-color: #ddd5c0; border-radius: 3px; }

    /* ── HIDE STREAMLIT CHROME ── */
    button[data-testid="collapsedControl"],
    [data-testid="stSidebarCollapseButton"],
    button[kind="headerNoPadding"],
    [data-testid="stSidebarNavCollapseIcon"] { display: none !important; }
    </style>
""", unsafe_allow_html=True)


TIER_LABELS = {
    0: "Tier 0 — Narrative (Ages 6–9)",
    1: "Tier 1 — Relationship (Ages 10–13)",
    2: "Tier 2 — Abstract (Ages 14–16)",
    3: "Tier 3 — Elite (JEE/IMO)",
    4: "Tier 4 — Competition (IMO/Putnam)",
}


def _init_state():
    defaults = {
        "messages": [],
        "current_phase": 1,
        "detected_tier": 3,
        "session_saved": False,
        "hint_level": 0,
        "mvc_validated": False,
        "active_model": None,
        "quota_state": {},
        "wrapper_cache": {},
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


_init_state()


# Discover models (cached 1h)
ALL_MODELS = discover_models(GEMINI_KEY, GROQ_KEY, SAMBA_KEY)


# ---------------------------------------------------------------------------
# SIDEBAR — admin only (gated by ?admin=<PIN>)
# Public users see only the header bar below; the sidebar is fully hidden.
# ---------------------------------------------------------------------------

if ADMIN_MODE:
    st.sidebar.image(LOGO_URL, width=90)
    st.sidebar.markdown(
        "<div class='admin-pill'>● ADMIN MODE</div>"
        "<hr style='border:none; border-top:1px solid #ddd5c0; margin:10px 0;'>",
        unsafe_allow_html=True,
    )

    # Connection pills
    if GEMINI_KEY:
        st.sidebar.markdown("<div class='status-pill'>● Gemini Connected</div>", unsafe_allow_html=True)
    else:
        st.sidebar.markdown("<div class='status-pill warn'>○ Gemini Missing</div>", unsafe_allow_html=True)

    if FIREBASE_CRED:
        st.sidebar.markdown("<div class='status-pill'>● Firebase Connected</div>", unsafe_allow_html=True)
    else:
        st.sidebar.markdown("<div class='status-pill dim'>○ Firebase Offline</div>", unsafe_allow_html=True)

    if GROQ_KEY:
        st.sidebar.markdown("<div class='status-pill'>● Groq Connected</div>", unsafe_allow_html=True)
    if SAMBA_KEY:
        st.sidebar.markdown("<div class='status-pill'>● SambaNova Connected</div>", unsafe_allow_html=True)

    # Engine status
    st.sidebar.markdown("#### Engine Status")
    active = st.session_state.active_model or "Initializing…"
    pill_class = "status-pill" if st.session_state.active_model else "status-pill dim"
    st.sidebar.markdown(f"<div class='{pill_class}'>Model: {active}</div>", unsafe_allow_html=True)

    # Detailed health (collapsed)
    with st.sidebar.expander("Provider Catalog", expanded=False):
        by_provider = {}
        for m in ALL_MODELS:
            by_provider.setdefault(m["provider"], 0)
            by_provider[m["provider"]] += 1
        for p, count in by_provider.items():
            blocked = sum(
                1 for m in ALL_MODELS
                if m["provider"] == p and is_blocked(m["provider"], m["model"])
            )
            live = count - blocked
            status = "✓" if live > 0 else "✗"
            st.markdown(f"{status} **{p}** — {live}/{count} live")
        if st.button("Reset circuit breakers", use_container_width=True):
            st.session_state.quota_state = {}
            st.rerun()

    # Live doctrine (knowledge_base/)
    with st.sidebar.expander("Live Doctrine (knowledge_base/)", expanded=False):
        _kb = get_live_kb()
        if _kb is None:
            st.caption("⚠ No `knowledge_base/` folder found.")
        elif not _kb["files_loaded"]:
            st.caption(f"Folder found at `{_kb.get('kb_dir', '?')}` but no `.md`/`.txt` files loaded.")
        else:
            approx_tok = _kb["total_chars"] // 4
            st.markdown(
                f"**Fingerprint:** `{_kb['fingerprint']}`  \n"
                f"**Loaded:** {_kb['total_chars']:,} chars (~{approx_tok:,} tokens)"
            )
            loaded_at = datetime.fromtimestamp(
                _KB_CACHE.get("loaded_at", time.time())
            ).strftime("%H:%M:%S")
            st.caption(f"Last reload: {loaded_at} · auto-reloads on file change")
            st.markdown("**Files in doctrine:**")
            for name, chars, trunc in _kb["files_loaded"]:
                mark = " *(truncated)*" if trunc else ""
                st.markdown(f"- `{name}` — {chars:,} chars{mark}")
            if _kb["files_skipped"]:
                st.caption("Skipped (budget exceeded):")
                for name in _kb["files_skipped"]:
                    st.caption(f"  · `{name}`")
            st.caption(
                f"Per-file cap: {KB_PER_FILE_CAP:,} chars · "
                f"Total budget: {KB_BUDGET_CHARS:,} chars"
            )
            if st.button("Force reload now", use_container_width=True):
                _KB_CACHE["signature"] = None
                st.rerun()

    st.sidebar.markdown("---")
    st.sidebar.caption(
        "Public users see only the chat. Share the URL with `?admin=<PIN>` to unlock this panel."
    )


# ---------------------------------------------------------------------------
# MAIN — public surface (everyone sees this)
# ---------------------------------------------------------------------------

# Logo + title
title_col_logo, title_col_text = st.columns([1, 9])
with title_col_logo:
    st.image(LOGO_URL, width=70)
with title_col_text:
    st.markdown("## ThinkMath.ai")
    st.markdown(
        "##### Your Advaitian Socratic Mentor — *Find the Seed. Burn the candle from both ends.*"
    )

# ─── HEADER BAR (3 cards: New Session · Session Progress · Support) ───
hdr_new, hdr_progress, hdr_donate = st.columns([1.1, 1.6, 1.6])

with hdr_new:
    with st.container(border=True):
        st.markdown(
            "<div class='header-title'>Session</div>",
            unsafe_allow_html=True,
        )
        if st.button("🆕 New Session", use_container_width=True, key="hdr_new_session"):
            if st.session_state.messages and not st.session_state.session_saved:
                save_session_to_firebase(
                    st.session_state.messages,
                    st.session_state.current_phase,
                    st.session_state.detected_tier,
                )
            st.session_state.messages = []
            st.session_state.current_phase = 1
            st.session_state.detected_tier = 3
            st.session_state.session_saved = False
            st.session_state.hint_level = 0
            st.session_state.mvc_validated = False
            st.session_state.active_model = None
            st.rerun()

with hdr_progress:
    with st.container(border=True):
        st.markdown(
            "<div class='header-title'>Session Progress</div>",
            unsafe_allow_html=True,
        )
        cur = st.session_state.current_phase
        phases_meta = {
            1: "Phase 1: Seed",
            2: "Phase 2: Directions",
            3: "Phase 3: Convergence",
        }
        rows = []
        for n, label in phases_meta.items():
            if n < cur:
                rows.append(f"<span class='phase-complete'>✓ {label}</span>")
            elif n == cur:
                rows.append(f"<span class='phase-active'>▶ {label}</span>")
            else:
                rows.append(f"<span class='phase-inactive'>○ {label}</span>")
        st.markdown(
            f"<div class='header-progress-row'>{''.join(rows)}</div>",
            unsafe_allow_html=True,
        )

with hdr_donate:
    with st.container(border=True):
        st.markdown(
            "<p class='header-donate-quote'>"
            "&ldquo;You&rsquo;ve burned the candle from both ends today. "
            "Help us put a candle in someone else&rsquo;s hands.&rdquo;"
            "</p>",
            unsafe_allow_html=True,
        )
        st.link_button(
            "Support the Mission",
            "https://paypal.me/vasumathiiK",
            use_container_width=True,
        )

if st.session_state.messages:
    st.markdown(
        f"<span class='tier-badge'>"
        f"{TIER_LABELS.get(st.session_state.detected_tier, 'Tier 3 — Elite')}"
        f"</span>",
        unsafe_allow_html=True,
    )

st.markdown("---")


def render_mentor(content: str, model_label: str | None = None):
    """Render a mentor card: native st.markdown body so KaTeX renders."""
    with st.chat_message("assistant"):
        st.markdown("<div class='card-role'>" + MENTOR_DISPLAY_NAME + "</div>", unsafe_allow_html=True)
        st.markdown(normalise_math(content))
        if model_label:
            st.markdown(f"<div class='card-footer'>Powered by {model_label}</div>", unsafe_allow_html=True)


def render_user(content: str):
    with st.chat_message("user"):
        st.markdown("<div class='card-role'>You</div>", unsafe_allow_html=True)
        st.markdown(normalise_math(content))


# Intro card (when no messages yet)
if not st.session_state.messages:
    render_mentor(CANNED_GREETING)
else:
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            render_user(msg["content"])
        else:
            render_mentor(msg["content"], msg.get("model"))

st.markdown("---")


# Input + stuck button
col_input, col_stuck = st.columns([5, 1])
with col_input:
    user_input = st.chat_input("Share your math problem or response here…")
with col_stuck:
    st.markdown("<br>", unsafe_allow_html=True)
    stuck_clicked = st.button("I'm stuck", key="stuck_btn", help="Get a structural hint without the answer")

if stuck_clicked and st.session_state.messages:
    hints = [
        "I'm stuck. Give me a Socratic probe — a tiny experiment I can run myself, no reveal.",
        "Still stuck. Give me the Archetype Nudge — name the primary archetype only, not the move.",
        "I need the Direction Map — show me the multidirectional structure, not the convergence point.",
        "Last hint: give me the Pivot Shadow — one-sentence silhouette of the pivot, not the answer.",
    ]
    lvl = st.session_state.hint_level
    user_input = hints[lvl] if lvl < len(hints) else hints[-1]
    st.session_state.hint_level = min(lvl + 1, len(hints) - 1)


# Stage 2 button
if st.session_state.mvc_validated and st.session_state.current_phase < 3:
    if st.button("Generate Stage 2 Commentary", type="primary", use_container_width=True):
        user_input = "Please give me the full Stage 2 Six-Point Commentary now."


# Process turn
if user_input:
    if not (GEMINI_KEY or GROQ_KEY or SAMBA_KEY):
        st.error("No API keys configured. Add at least one of GEMINI_API_KEY / GROQ_API_KEY / SAMBANOVA_API_KEY.")
        st.stop()
    if not ALL_MODELS:
        st.error("No models discovered. Check your API keys.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.status("Thinking structurally…", expanded=False) as status:
        try:
            history_for_api = [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages[:-1]
            ]
            raw, provider, model = chat(
                user_input,
                history_for_api,
                ALL_MODELS,
                status_writer=status,
            )
            clean, phase, tier = parse_metadata(raw)
            clean = normalise_math(clean)
            if not clean:
                clean = "[Empty response. Please rephrase and try again.]"

            st.session_state.current_phase = phase
            st.session_state.detected_tier = tier
            st.session_state.active_model = f"{provider} · {model}"
            st.session_state.messages.append({
                "role": "mentor",
                "content": clean,
                "model": st.session_state.active_model,
            })

            if "ready for stage 2" in clean.lower():
                st.session_state.mvc_validated = True

            if phase == 3 and "TAKEAWAY" in clean.upper():
                problem = next(
                    (m["content"] for m in st.session_state.messages if m["role"] == "user"),
                    "",
                )
                save_commentary_to_firebase(problem, clean, tier)
                st.session_state.session_saved = True

            status.update(label=f"✓ {provider} · {model}", state="complete")
            st.rerun()

        except Exception as e:
            status.update(label=f"All providers exhausted: {e}", state="error")
            st.error(str(e))


# Export / commit (Phase 3 only)
if st.session_state.messages and st.session_state.current_phase == 3:
    st.markdown("---")
    col_save, col_export = st.columns(2)
    with col_save:
        if st.button("Commit to Advaitian Bible", use_container_width=True):
            problem = next(
                (m["content"] for m in st.session_state.messages if m["role"] == "user"),
                "",
            )
            last_mentor = next(
                (m["content"] for m in reversed(st.session_state.messages) if m["role"] == "mentor"),
                "",
            )
            if save_commentary_to_firebase(problem, last_mentor, st.session_state.detected_tier):
                st.success("Commentary committed to the Advaitian Bible.")
                st.balloons()
            else:
                st.error("Could not commit. Check Firebase credentials.")
    with col_export:
        if st.button("Export Session", use_container_width=True):
            session_text = (
                f"ThinkMath.ai Session Export\n"
                f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
                f"Tier: {TIER_LABELS.get(st.session_state.detected_tier, 'Unknown')}\n"
                + "=" * 50 + "\n\n"
            )
            for msg in st.session_state.messages:
                role = "YOU" if msg["role"] == "user" else "MENTOR"
                session_text += f"[{role}]\n{msg['content']}\n\n"
            st.download_button(
                "Download Session",
                session_text,
                file_name=f"thinkmath_session_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                mime="text/plain",
            )
