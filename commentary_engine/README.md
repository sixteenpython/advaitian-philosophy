# ThinkMath Engine

ThinkMath is an Advaitian Socratic mathematics mentor. The chat is the learning
experience, but chat history is not the source of truth. The canonical
`AdvaitianSession` records the problem, seed hypotheses, archetype map, MVC,
verification evidence and provenance.

## Run locally with open models

1. Install [Ollama](https://ollama.com/).
2. Pull at least a mentor model: `ollama pull qwen3:8b`.
3. For full commentary, pull `gpt-oss:20b`.
4. For an independent critic, pull `qwen2.5-math:7b`.
5. Install `requirements.txt` and run `streamlit run app.py` from this folder.

`OLLAMA_BASE_URL` may point at another private Ollama host. Hosted Groq and
SambaNova adapters are optional, no-cost fallbacks for the public demo and are
restricted to registered open/open-weight model families. The application has
no paid-LLM dependency.

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
