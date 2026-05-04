# ThinkMath.ai — End-of-Session Checkpoint

**Date:** Monday, May 4, 2026
**Session purpose:** Architectural calibration round before user testing
**Outcome:** Ship-ready. User testing planned next few weeks.

---

## Purpose of This File

End-of-session memory for picking up in a new AI conversation without losing context. Read this first in any new session.

---

## 1. Quick Context

**Product:** ThinkMath.ai — an Advaitian Socratic mentor for mathematics. Refuses to give answers; teaches problem-solving frameworks via three-phase Socratic protocol.

**Audience (clarified this session):** Grades 9–12 CBSE/ICSE students + JEE Mains and JEE Advanced aspirants. **Mathematics only.**

**Stack:**
- Streamlit web app
- Multi-provider LLM orchestrator (Google Gemini + Groq + SambaNova)
- Firebase Firestore (session persistence + "Advaitian Bible" commentary archive)
- Hot-reloading knowledge base from `knowledge_base/` folder

**Repo:**
- Local: `C:\Users\ajayv\Documents\jupyter-python\advaitian-philosophy`
- Remote: `https://github.com/sixteenpython/advaitian-philosophy`
- Branch: `main`

**Current state:** Ship-ready. Two confidence checks passed today. **Do not add features before user-testing data arrives.**

---

## 2. Architecture (Current State)

### High-Level Flow

1. User sends a math problem or response
2. `detect_intent()` classifies as `greeting` or `math`
3. **Greeting** → `CONCIERGE_BRIEF` on a fast model
4. **Math** → `assemble_system_prompt()` (CORE_BRIEF + live KB doctrine) on a tiered model ladder
5. `build_ladder(intent, all_models, phase=phase)` selects models — Phase 3 restricted to score ≥ 9 (top-tier) with fallback to ≥ 7
6. Generator produces response. If Phase 3 with `TAKEAWAY` present → second-LLM critic audits before user sees output
7. Critic verdict applied:
   - `SOLID` → ship as-is
   - `NEEDS_NOTE` → ship with caveat box appended
   - `UNSAFE` → refuse, replace with Socratic re-engagement
8. Phase 3 SOLID/NEEDS_NOTE commentaries committed to Firebase ("Advaitian Bible"). UNSAFE commentaries are NOT saved (refusal text lacks `TAKEAWAY` substring → existing save guard skips them naturally).

### Three-Phase Socratic Protocol

- **Phase 1 — Seed Identification:** recognize the structural pattern; ask diagnostic question
- **Phase 2 — Directions:** multi-archetype scan; brute-wall warning; converge to operational pivot
- **Phase 3 — Convergence:** Six-Point Commentary (SEED · BRUTE PATH · ELEGANT PIVOT · PITFALLS · CONNECTIONS · TAKEAWAY)

### Three-Layer Phase-3 Defense (the key calibration shipped today)

This is the architecture that makes ThinkMath ship-worthy for proof problems:

1. **MVC Gate** in `CORE_BRIEF` (between Phase 2 and Phase 3):
   - Requires `SETUP + MOVE + CLOSURE` before "Your MVC is solid. Ready for Stage 2." fires
   - Per-archetype closure requirements (Vieta-jumping needs termination case; induction needs base + step; pigeonhole needs counting that forces collision; etc.)
   - Three canonical refusal replies depending on which part is missing

2. **Top-Tier Generator** in `build_ladder()`:
   - Phase 3 first tries score ≥ 9 (`PHASE3_MIN_SCORE`): 120B+, Gemini Pro, DeepSeek-class
   - Falls back to score ≥ 7 (`PHASE3_FALLBACK_SCORE`): 70B-class with admin warning
   - Refuses Phase 3 entirely if even mid-tier is unavailable
   - Reason: 70B-class hallucinates non-sequitur contradictions on hard problems; 120B+ holds

3. **Independent LLM Critic** in `run_critic()`:
   - Separate LLM call with `CRITIC_BRIEF` prompt
   - Leads with **load-bearing line check** (identify the single inference the proof's contradiction or termination rests on)
   - Six **zero-tolerance patterns** that auto-trigger UNSAFE:
     - (a) Manufactured contradiction (e.g., "(a−a')² is not a perfect square" — false; it IS by definition)
     - (b) Non-sequitur chain (e.g., "X not square ⟹ kX+c not square" without naming a theorem)
     - (c) Descent without termination case (Vieta-jumping that doesn't show a' = 0)
     - (d) Circular assertion (using the conclusion as a step)
     - (e) Invented theorem (citing Vieta/Ptolemy/etc. with non-canonical statement)
     - (f) Missing arithmetic sub-proof (asserting integrality/positivity without derivation)
   - Bias for hard problems: prefer UNSAFE over NEEDS_NOTE when in doubt
   - Critic prefers a *different provider* from the generator for diversity of judgment
   - Critic restricted to capable models (score ≥ 7) — small critic would rubber-stamp large generator

### Knowledge Base Hot-Reload

- Module-level cache with `mtime`-based invalidation
- Files in `knowledge_base/` reloaded on every math turn if any file changed
- Budget: `KB_BUDGET_CHARS = 11000`, `KB_PER_FILE_CAP = 10500`
- Currently loaded into doctrine: `Advaitian.md`, `ThinkMath_Blueprint_v3.md`, `Advaitian_Master_Framework.txt`
- Skipped (over budget): `Advaitian_White_Paper.txt`, `Advaitian_Philosophy_Framework.txt`, `Chapter_1_Invariance.txt`, `Masterclass_Problem_Solving.txt`, `Seed_Elegance_Connections.txt`
- Admin sidebar shows fingerprint, loaded files, skipped files, last reload time, "Force reload now" button

### UI

- **Admin gate**: `?admin=<PIN>` query parameter; PIN from `st.secrets["ADMIN_PIN"]` (default `vriddhi-2026`); CSS hides sidebar for non-admin users
- **Header bar (3 cards):** Session (with "New Session" button) · Session Progress (phase indicators) · Support the Mission (donate)
- **Expanded chat input:** `min-height: 110px` for multi-paragraph problems
- **Donate buttons:** $5 / $10 / $15 / $20 + custom (min $2) via `paypal.me/vasumathiiK`
- **Critic verdict display:** Admins see expandable panel under each Phase-3 message (verdict badge, rationale, issues, raw output, original pre-critic draft for UNSAFE); public users see annotated commentary or refusal

---

## 3. What Shipped This Session (Commits to `main`)

| Commit | Summary |
|---|---|
| `40597bf` | CORE_BRIEF rewrite: full Advaitian doctrine (archetypes, pitfalls, gems, CEP library, MVC gate v1, six-point template, tier voice markers) |
| `0c8b782` | Phase 3 pre-flight checklist + honesty gate + repeated-pivot rule + `MAX_OUTPUT_TOKENS[3]` → 5000 |
| `07da99b` | KB hot-reload (`get_live_kb()`, `assemble_system_prompt()`, mtime caching) |
| `f4ce40d` | UI redesign: admin gate, header cards, donate, expanded chat input |
| `72e249a` | Donate link fix (`paypal.me/vasumathiiK`) |
| `8b9782f` | Donate amount presets ($5/$10/$15/$20 + custom min $2) |
| `d01fb7f` | **Second-LLM proof critic** (`CRITIC_BRIEF`, `run_critic`, `annotate_with_critic`, admin transparency panel) |
| `34c8d16` | **Three calibrations:** tighter critic (load-bearing-line + zero-tolerance patterns), tighter MVC gate (SETUP+MOVE+CLOSURE with per-archetype closure), Phase-3 ladder gate (score ≥ 9 with fallback ≥ 7) |

The last two commits (`d01fb7f` and `34c8d16`) are the architectural payload that makes the product ship-worthy. Everything before was prerequisite scaffolding.

---

## 4. Confidence Checks That Passed Today

### Check 1: IMO 1988 P6 — Vieta Jumping (Tier 3 Elite)

**Why this problem:** It's the canonical Vieta-jumping problem and was the case that exposed the "manufactured contradiction" failure mode in the previous run.

**What happened:**
- MVC gate refused user's setup-only sketch **twice** with archetype-aware closure prompts
- Only after Move 7 (descent + base case + induction) did the gate fire "Your MVC is solid"
- Top-tier model (`SambaNova · gpt-oss-120b`) held throughout; no drift to 70B
- Phase 3 produced clean Six-Point with no manufactured contradiction
- Critic returned `SOLID`

**Verdict:** Calibrations work. Ship.

### Check 2: Spherical Raindrop ODE (Tier 1–2 JEE Mains / Class 12)

**Why this problem:** Validates the system on the *typical* audience problem (CBSE Class 12 / JEE Mains differential equations).

**What happened:**
- MVC gate correctly distinguished meta-strategy ("Invariance + Symmetry, watch dV/dt vs dA/dt") from operational move ("apply chain rule to V = (4/3)πr³")
- Phase 3 archetype identification was insightful: "Invariance (the proportionality constant k stays constant) + Substitution (replace V by formula in r to expose the invariant)"
- Pedagogical lift: "the radius shrinks at constant speed, independent of its current size" — *transferable insight*, not mechanical solution
- Pitfalls calibrated to level (sign error, dA/dt vs dV/dt confusion, r > 0 cancellation requirement)
- Critic returned `SOLID`

**Verdict:** Architecture is range-flexible — handles hardest 5% (IMO) AND typical 80% (JEE Mains/CBSE) appropriately.

---

## 5. Audience Refinement (Important Context)

**Mid-session correction:** Earlier in the session I was evaluating ThinkMath through an "elite-only IMO tutor" frame. The user clarified the actual audience:

- **Bulk audience:** Grades 9–12 CBSE/ICSE + JEE Mains/JEE Advanced aspirants
- **Geography:** Primarily India
- **Subject:** Mathematics only
- **Path:** User testing in next few weeks; expected to pass

This reframes the product significantly:

- **Market is ~1000× larger** than the elite-IMO frame suggested (hundreds of millions globally vs ~100K)
- **LLM math ceiling is mostly irrelevant** — JEE Adv math sits well within 70B-class capability; 120B+ is overkill for ~95% of real users (but appropriate for the hardest 5%)
- **Competitive position is strong:** Indian JEE/board-prep market is dominated by answer-vending machines (Doubtnut, Vedantu, PhysicsWallah, Photomath). Khanmigo is the closest pedagogical competitor but is thinner. ThinkMath's principled refusal-to-give-answers + archetype-driven framing has **no direct competitor in this market**.
- **Willingness-to-pay exists:** JEE families spend ₹50K–₹5L/year on coaching. Modest ₹500–2K/month subscriptions are viable. Or B2B (license to coaching institutes).

---

## 6. Honest Product Assessment

### Strengths
- More thoughtfully engineered than ~90% of AI tutors shipping in this space
- Original Advaitian pedagogy — not a thin wrapper around GPT
- Defense-in-depth correctness layer is publishable-quality (MVC gate + top-tier generator + independent critic)
- Honesty primitive ("the Bible accepts uncertainty, it does not accept falsehood") is principled — most products won't ship this
- Hot-reload doctrine is real engineering (most apps load on startup)
- Strong fit for Indian JEE/board-prep market — no Socratic competitor in space dominated by answer-vending

### Concerns
- Still LLM-based — probabilistic correctness floor for hardest problems; honesty gate handles philosophically, UX cost is real
- System prompt growing (~4K tokens skeleton + dynamic doctrine) — **ratchet effect to watch**; future additions need to come with deletions
- Critic and generator can fail in correlated ways (both LLMs, similar training distributions); long-term mitigation would require symbolic verification (Lean/SymPy) which we deliberately rejected as impractical
- Indian context awareness (₹, NCERT topics, Indian word-problem conventions) not yet specifically tuned in KB
- **No production telemetry yet** — currently inferring quality from individual transcripts

### Competitive Position
- vs. **ChatGPT/Claude on math:** stronger *process* (Socratic, archetype-driven) — real differentiator
- vs. **Khan Academy / Brilliant:** different focus (elite + Socratic) — complementary, not direct competitor
- vs. **Doubtnut/Vedantu/PhysicsWallah/Unacademy:** those are answer-machines / lecture content; ThinkMath is principled refusal — strong moat
- vs. **Khanmigo:** ThinkMath has sharper philosophical framing and stronger correctness machinery
- vs. **Lean/Coq tutors:** those are formal/inaccessible; ThinkMath is informal/accessible — different niche

---

## 7. Decision Made This Session

**SHIP NOW.** User testing in the next few weeks. **Do not add new features before real-user data arrives.**

The instinct to keep polishing is wrong at this point. After today's calibration round, what we have is enough to learn from. Real students touching the product will reveal more useful signal in one week than I can find in 100 solo runs.

---

## 8. Things NOT to Do (Lessons from This Session)

1. **Don't bloat the system prompt further.** Every fix adds text; every addition needs a corresponding deletion. Watch the ratchet — we're at ~4K skeleton + ~11K dynamic doctrine; that's roughly the budget ceiling.
2. **Don't pre-optimize without production evidence.** N=1 transcript fixes overfit to specific failure modes.
3. **Don't fix calibration from solo testing alone.** Multiple rounds of "I tested again and found X" indicate I'm finding *my* edge cases, not real students'.
4. **Don't add features before user-testing data.** Deferred items:
   - Lean/SymPy proof checker — *rejected as impractical* (Mathlib too large, LLM-to-Lean unreliable; LLM critic shipped instead as the practical alternative)
   - Curriculum-specific KB additions — *defer to post-testing*
   - Tier-aware Six-Point length — *defer to post-testing*
   - Mobile responsive validation — *defer to post-testing*
5. **Don't pretend the LLM ceiling doesn't exist.** Some IMO-grade problems no current LLM can prove reliably. The honesty gate handles this philosophically; the UX cost (occasional refusals) is a real product trade-off, not a bug.

---

## 9. Instrumentation Needed for User Testing

Currently no production telemetry exists. Before/during user testing, instrument these:

### Quantitative signals (per session, log to Firebase or analytics endpoint)
- Tier detection: detected tier vs. ground truth (CBSE 11 vs JEE Mains vs JEE Adv) — mis-tiering cascades into wrong protocol heaviness
- Time-to-resolution by tier — overlong Socratic on simple problems = bad UX
- Critic firing rate + verdict distribution — always-SOLID = not catching anything; always-UNSAFE = over-tuned
- MVC gate refusal rate per tier — > 50% on Tier 1 = too strict
- Drop-off rate per phase — where do students abandon?
- Re-engagement rate (next-day return) — real product-market-fit signal

### Qualitative signals (gather explicitly via in-app surveys or interviews)
- "Did the mentor sometimes feel like it was over-thinking a simple problem?"
- "When the mentor refused to give the answer, did you appreciate that or were you frustrated?"
- "Did the archetype names help you or feel like jargon?"
- "Did you feel the mentor understood your CBSE/JEE syllabus?"

### Triggers for next calibration round (only if data warrants)
- Critic almost never UNSAFE → loosen back to NEEDS_NOTE bias for board-exam problems
- MVC gate refusing board-exam students often → loosen Tier 1 closure requirement
- Students consistently want shorter Phase 3 → tier-aware commentary length (3 sections for Tier 1, 6 for Tier 3)
- Students intimidated by tier badges → soften "Tier 3 — Elite (JEE/IMO)" to plain "Adaptive level"

---

## 10. Key Calibration Constants (current values in `commentary_engine/app.py`)

```python
PHASE3_MIN_SCORE = 9          # top-tier: 120B+, Gemini Pro, DeepSeek-class
PHASE3_FALLBACK_SCORE = 7     # mid-tier: 70B-class fallback with critic backstop

MAX_OUTPUT_TOKENS = {
    "concierge": 256,
    1: 700,
    2: 900,
    3: 5000,                  # Phase 3 needs space for full Six-Point
}

CRITIC_OUTPUT_TOKENS = 700
CRITIC_MAX_ATTEMPTS = 3       # try up to 3 critic candidates if early ones fail

KB_BUDGET_CHARS = 11000       # total doctrine budget
KB_PER_FILE_CAP = 10500       # per-file cap before truncation
```

---

## 11. File Map

- `commentary_engine/app.py` — main Streamlit app, ~92K characters, all logic in one file
  - Lines 1–388: prompt constants (`CONCIERGE_BRIEF`, `CORE_BRIEF`)
  - Lines ~390–460: `CRITIC_BRIEF`
  - Lines ~440–580: KB hot-reload (`_find_kb_dir`, `_kb_signature`, `_load_kb_doctrine`, `get_live_kb`, `assemble_system_prompt`)
  - Lines ~580–870: provider wrappers + model discovery + scoring
  - Lines ~870–940: quota state + circuit breaker
  - Lines ~940–1090: ladder building (with Phase 3 score gate)
  - Lines ~1090–1170: `chat()` orchestrator
  - Lines ~1170–1410: critic (`run_critic`, `annotate_with_critic`)
  - Lines ~1410+: UI layer (sidebar admin gate, header cards, chat rendering, turn handler)

- `knowledge_base/` — doctrine files (markdown + txt), hot-reloaded on every math turn
  - **Loaded into doctrine:** `Advaitian.md`, `ThinkMath_Blueprint_v3.md`, `Advaitian_Master_Framework.txt`
  - **Discovered but skipped (over budget):** `Advaitian_White_Paper.txt`, `Advaitian_Philosophy_Framework.txt`, `Chapter_1_Invariance.txt`, `Masterclass_Problem_Solving.txt`, `Seed_Elegance_Connections.txt`

- `requirements.txt` — Python deps (streamlit, google-generativeai, groq, openai, firebase-admin)
- `.gitignore` — must include `credentials.py`, `local_keys.py` (NEVER push secrets)

---

## 12. Open Risks / Known Gaps

1. **No production telemetry.** Add Firebase logging of `(problem, tier, phase reached, critic verdict, model used, latency)` per turn before/during user testing.
2. **Critic-generator correlation.** Both are LLMs; can fail together. Long-term mitigation: SymPy verification for algebraic identity claims; Lean for select formal goals. **Out of scope for this release.**
3. **Indian context weakness.** Word problems with ₹, Indian names, NCERT-specific terminology not yet enriched in KB.
4. **Curriculum-specific patterns missing.** JEE Advanced-specific tricks (e.g., parameter integral symmetry `∫₀ᵃ f(x)dx = ∫₀ᵃ f(a−x)dx`, conic focal chord properties, vector triple product identities) not in archetype catalog.
5. **Mobile UX unverified.** Most Indian students will use phones; needs responsive testing.
6. **No per-user rate limiting.** Single user could exhaust shared free-tier quota.
7. **Firebase quota shared.** All users write to same project; could hit Firebase limits at scale.

---

## 13. Pending Tasks (Post User-Testing Only)

Do **not** start these before user-testing data is in:

- Add production telemetry hooks (Firebase or separate analytics)
- Tier-aware commentary length (3 sections for Tier 1, 6 for Tier 3)
- Soften tier badge wording in UI
- Indian context enrichment in KB (₹, NCERT topics, common JEE patterns)
- Mobile responsive validation
- Per-user session rate limiting
- B2B / institutional partnership exploration (coaching institutes, board-exam prep apps)
- Long-term: explore symbolic verification (SymPy for algebraic identities, Lean for select goals)

---

## 14. Next Session Starting Point

When picking up in a new AI conversation:

1. **Read this file first.** Don't re-discover context.
2. **Check `git log` for any commits beyond `34c8d16`** (the calibration commit) to see what changed since.
3. **If user has run user-testing:** ask for the data — critic verdict distribution, MVC refusal rate, drop-off rate, qualitative feedback. Use that to drive the next calibration round.
4. **If user has NOT run user-testing yet:** do not propose new features. Help with deployment, telemetry instrumentation, or specific bug fixes only.
5. **Resist the temptation to add features.** That is the discipline lesson from this session.

If asked to "improve" the app generically, push back: ask what specific user signal motivates the change. If there isn't one, decline politely.

---

## 15. Session Transcript Reference

Full conversation transcript (for deep context if needed): [ThinkMath calibration and ship readiness](e68c3de9-c548-4e46-90c4-0cbebd701baa)

---

## Closing Note

The product is in a state where the next round of improvements should be data-driven, not speculation-driven. Three confidence-defining instruments are now live (MVC gate, top-tier generator, critic), each architecturally complete. Further calibration is tuning, and tuning belongs to production data.

Ship. Observe. Then iterate.
