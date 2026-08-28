# ThinkMath Engine v2

> **Historical baseline.** This document records the v2 trust boundary. The current humane
> conversation, recovery escalation, problem-map caching, model resilience, and closure policy are
> specified in `HYBRID_MENTOR_ENGINE_V3_2.md`; the current interface contract is documented in
> `STUDENT_EXPERIENCE_V3.md`.

## Purpose

ThinkMath teaches the structural method expressed in the Advaitian book. It
does not act as a generic answer engine. Its operating contract is:

> Do not solve prematurely. Help the student discover and articulate the
> structural pivot first. Release a complete commentary only after a validated
> Setup–Move–Closure path, and label the level of proof assurance.

## Architecture

The initial implementation is a modular monolith:

```text
Streamlit UI
  -> deterministic learning orchestrator
  -> Advaitian Knowledge Asset
  -> task-based model registry and provider adapters
  -> deterministic verification + independent critic
  -> opt-in persistence and provenance
```

### Canonical asset

`thinkmath.domain.AdvaitianSession` is the source of truth. Messages are
evidence. The asset holds problem, phase, tier, student observations, seed and
archetype hypotheses, MVC, rejected approaches, connections, hint level,
verification evidence and provenance. Model updates are allow-listed and
versioned. A model cannot validate its own MVC proposal.

### Deterministic/LLM boundary

Deterministic responsibilities:

- phase-transition policy and Stage 2 gate;
- parsing and validation of model state;
- student confirmation of Setup, Move and Closure;
- model-role eligibility and capability thresholds;
- Six-Point structural checks and descent-closure checks;
- symbolic equivalence through SymPy;
- persistence consent, versioning and provenance;
- proof-assurance labels.

LLM responsibilities:

- interpret the student's mathematical language;
- propose candidate seeds and archetypes with evidence;
- ask Socratic questions and phrase graduated hints;
- draft qualitative connections and Six-Point commentary;
- conduct an independent semantic proof review.

No LLM result silently overrides deterministic state or calculations.

The current canonical MVC is injected into each mathematical turn as an
explicitly untrusted claim. Stage 2 must reconcile its proof with that MVC or
stop and identify the conflict; form edits are no longer invisible to the
commentary generator.

## Proof release policy

The critic parser defaults to `UNVERIFIED`, never `SOLID`. If a qualified
critic is absent, fails, or returns malformed output, the full proof is not
released as checked commentary. Deterministic checks can reject known failure
patterns, but arbitrary prose proofs remain only partially verified unless a
stronger formal method is available.

## Model policy

The local-first registry currently recognises:

| Role | Model | Licence |
|---|---|---|
| Mentor | Qwen3 8B | Apache-2.0 |
| Commentary | gpt-oss 20B | Apache-2.0 |
| Critic | Qwen2.5-Math 7B | Apache-2.0 |
| Commentary/critic alternative | DeepSeek-R1 Distill Qwen 14B | MIT |

Ollama is the private default. A public Streamlit host cannot provide unlimited
GPU inference merely because weights are free; optional no-cost hosted
fallbacks therefore remain operationally separate and quota-bound. The public
demo currently uses Groq only; SambaNova is excluded because it requires a
payment method.

Models are promoted by the Advaitian golden evaluation suite, not by name,
parameter count or generic benchmarks.

The Groq adapter uses low, hidden reasoning so reasoning tokens cannot consume
the visible-response allowance. It also caps prompt plus requested completion
to a conservative 7,400-token budget for the free tier. The full doctrine is
preserved in the repository; inference receives a compact core protocol plus a
prioritised knowledge supplement to avoid duplicating the same rules.

The renderer repairs unmatched display-math openers and inline Six-Point
headings produced by open models. Both `thinkmath-state` and schema-matching
generic JSON fences are removed from the visible response, including messages
already held in a live Streamlit session.

## Security and privacy

- No credential-shaped filename or fallback administrator PIN is in source.
- Team access uses a password control and constant-time comparison, not a URL.
- Conversation persistence is off by default.
- The previously issued Gemini key must be revoked manually at its provider;
  removing it from source cannot revoke it.
- New Firebase records carry a 30-day expiry marker and the UI can delete all
  copies created during the current browser session. A Firebase TTL policy
  should enforce `expires_at` operationally.

## Next verification increments

1. Expand the golden suite to at least 100 reviewed cases across all archetypes.
2. Extract algebraic claims into explicit SymPy verification requests.
3. Add property-based counterexample search for invariants and inequalities.
4. Add formal proof adapters for narrowly supported theorem families.
5. Promote models only after blind comparison on correctness, Socratic
   non-reveal, MVC gating, doctrine fidelity, latency and memory.
