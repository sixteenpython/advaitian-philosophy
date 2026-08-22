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

Student-experience decisions and release boundaries are documented in
[`docs/STUDENT_EXPERIENCE_V3.md`](docs/STUDENT_EXPERIENCE_V3.md).
