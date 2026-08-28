# ThinkMath Engine

ThinkMath is an Advaitian Socratic mathematics mentor. The chat is the learning
experience, but chat history is not the source of truth. The canonical
`AdvaitianSession` records the problem, seed hypotheses, archetype map, MVC,
verification evidence and provenance.

## Student Experience v3.2

The public application now treats the evolving reasoning—not provider controls—as the main visual
object. Its four student views are:

- **Learn:** one-question-at-a-time Socratic conversation and an explicit four-level hint ladder;
- **Thinking Map:** canonical observations, candidate Seed, direction map and progressively revealed
  Setup–Move–Closure;
- **Commentary:** the earned Six-Point payoff rendered as readable learning sections, followed by a
  same-Seed transfer challenge;
- **My Journey:** a downloadable Pattern Passport and a visual before/after account of the student's
  reasoning.

Three curated demonstration journeys remain usable without any model or API capacity. Provider and
quota failures use student-facing recovery paths instead of exposing raw infrastructure errors.

## Hybrid mentor intelligence

ThinkMath uses open models deliberately, but the model does not own learning state or progression.
Each turn follows a governed loop:

1. a deterministic policy selects a typed teaching action and reveal boundary;
2. the model interprets the student's language, reasons about candidate directions, and speaks naturally;
3. only student-grounded state proposals are accepted;
4. model-inferred ideas remain in a separate, untrusted working problem map;
5. SymPy checks supported symbolic claims, while the validated Setup–Move–Closure gate owns progression;
6. an independent critic remains mandatory before checked Six-Point commentary is released.

Confident problem maps are cached in bounded process memory so identical problems do not require fresh
analysis while the app instance remains alive. Conversational recovery uses the smallest qualified stable
model first; deep reasoning and proof release retain stronger routes. If every provider is unavailable,
the selected teaching action is rendered deterministically and the conversation continues.

The implementation and trust boundary are documented in
[`docs/HYBRID_MENTOR_ENGINE_V3_2.md`](docs/HYBRID_MENTOR_ENGINE_V3_2.md).

## Humane teacher contract

The mentor treats “I don’t know,” “I am confused,” uncertainty, and partial attempts as different
teaching situations rather than failed inputs. It acknowledges the student's position, preserves
substantial work already offered, and asks one answerable next question. Repeated confusion increases
support through a deterministic ladder—narrow the goal, test a small case, offer two choices, model
one micro-step, then change representation—without inventing evidence or advancing the learning phase.

Long student arguments are summarized through the mathematical techniques they actually used before
the mentor names one load-bearing proof obligation. Generic restarts such as “what changes and what
stays fixed?” are rejected when the student has already supplied substantial reasoning.

## Proof assurance and operational honesty

ThinkMath distinguishes **Exploratory**, **Structural draft**, **Structurally checked**, **Needs
mathematical review**, and **Curated demonstration** states. A complete-looking response is never
presented as formally certified merely because an open model produced it. Commentary release remains
fail-closed when its deterministic checks or independent review obligations are unavailable.

Open or open-weight models remove licence fees; they do not create unlimited hosted compute. Local
Ollama is the private, user-funded capacity path. Hosted Groq routes remain optional and quota-bound,
while curated journeys and deterministic teaching actions preserve continuity when inference rests.

## Run locally with open models

1. Install [Ollama](https://ollama.com/).
2. Pull at least a mentor model: `ollama pull qwen3:8b`.
3. For full commentary, pull `gpt-oss:20b`.
4. For an independent critic, pull `qwen2.5-math:7b`.
5. Install `requirements.txt` and run `streamlit run app.py` from this folder.

`OLLAMA_BASE_URL` may point at another private Ollama host. Groq is the optional
no-cost hosted fallback for the public demo and is restricted to registered
open/open-weight models. SambaNova is intentionally unsupported because its
current service requires billing configuration. The application has no
paid-LLM dependency.

## Privacy

Learning sessions are private by default. Firebase persistence occurs only
after the user enables **Save this learning session**, or explicitly presses
**Commit to Advaitian Bible**. Admin mode is fail-closed and requires an
`ADMIN_PIN` secret; no fallback credential exists. New records carry a 30-day
expiry and the user can delete copies created during the current browser session.

## Tests

From `commentary_engine/`:

```powershell
python -m unittest discover -s tests -v
```

The golden evaluation dataset in `evals/golden_cases.json` is the model
promotion gate. Generic leaderboard position is not sufficient for a model to
become the mentor, commentary generator or critic.

The regression suite includes recovery-language classification, non-advancing confusion turns,
substantial-work recognition, closure obligations, proof-assurance copy, model routing, rendering,
verification, deterministic demonstrations, and the Streamlit student shell.

Student-experience decisions and release boundaries are documented in
[`docs/STUDENT_EXPERIENCE_V3.md`](docs/STUDENT_EXPERIENCE_V3.md).
