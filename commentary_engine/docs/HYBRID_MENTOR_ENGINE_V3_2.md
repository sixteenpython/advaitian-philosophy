# Hybrid Mentor Engine v3.2

## Operating principle

ThinkMath is algorithmically governed and LLM-powered:

> The model proposes; mathematical tools test; the mentor policy decides; the model communicates.

Open models remain responsible for the parts of olympiad mentorship that need semantic judgment:
interpreting informal reasoning, generating candidate directions, recognizing structural analogies,
maintaining an untrusted working problem map, and speaking like a teacher. They are not restricted to
cosmetic paraphrasing.

The application owns student state, teaching progression, reveal boundaries, hint escalation, selected
difficulty, verification labels, provider routing, and release of complete commentary.

## Turn pipeline

1. `conversation.classify_student_turn` classifies recovery and substantive language.
2. `mentor_engine.choose_mentor_action` selects one typed pedagogical action.
3. The action, objective, and reveal boundary are binding prompt context.
4. A normal turn makes one model request containing visible dialogue plus a structured state proposal.
5. `mentor_engine.validate_state_proposal` accepts only claims grounded in the student's current words.
6. Model-inferred archetypes and MVC candidates remain in `ProblemMap`, not student-owned state.
7. `verification.verify_student_claims` checks narrowly supported plain symbolic identities.
8. `state_machine.evaluate_transition` advances only from accepted evidence and the validated MVC gate.
9. Phase 3 retains deterministic commentary checks plus an independent model critic.

## Teaching actions

The current policy can ask for an observation, narrow the goal, test a small case, offer bounded
directions, demonstrate one micro-step, change representation, check a disputed step, compare directions,
complete MVC, stress-test an idea, or release checked commentary.

Repeated recovery escalates support deterministically:

1. narrow the goal;
2. use the smallest useful case;
3. offer two concrete choices;
4. model one justified micro-step;
5. change representation and rebuild.

Recovery never creates mathematical evidence or advances a phase.

## Humane conversational policy

Human-like mentorship is implemented as policy, not left to a persona prompt. The turn classifier
separates confusion, “I don’t know,” uncertainty, partial mathematical answers, substantial proposed
proofs, and ordinary substantive reasoning. The visible response must:

- acknowledge the student's present state without judgment;
- retain and name mathematical techniques already attempted;
- choose one typed teaching action and one answerable question;
- avoid repeating an opening diagnostic after useful work exists;
- increase scaffolding only as the recovery count requires;
- keep recovery turns outside canonical mathematical evidence and phase progression.

For a substantial argument, `substantial_work_summary` extracts the student's actual techniques and
the deterministic fallback names one load-bearing obligation. `ensure_teacher_response` rejects a
generic “what changes / what remains” reset when it would ignore that work.

## Proof closure and assurance

Setup–Move–Closure is a logical gate, not a field-completion checklist. Descent arguments, for example,
must state both an extremal move and the boundary or termination mechanism. When closure is missing,
the mentor asks for that precise obligation instead of rendering a polished commentary.

Student-facing assurance labels remain calibrated to recorded evidence:

- **Exploratory** — a direction to test;
- **Structural draft** — the intended architecture is present but technical checks remain;
- **Structurally checked** — available architecture and symbolic checks passed, with independent
  mathematical review still recommended;
- **Needs mathematical review** — a load-bearing check remains unresolved;
- **Curated demonstration** — a reviewed, bundled learning journey.

No label claims general formal proof certification.

## Problem maps and cost control

`ProblemMap` records a bounded set of candidate observations, directions, proof obligations,
misconceptions, and a candidate MVC. It is explicitly untrusted. A confident map is reused within the
session and in a 256-entry process-local LRU cache keyed by a normalized problem fingerprint.
The three existing demonstration problems also have compiled maps, establishing the same no-analysis
path that a larger reviewed historical-IMO library can use.

Routine recovery prefers the smallest qualified stable mentor model. Structural analysis uses the normal
reasoning ladder. Complete commentary uses the proof route and independent critic. Static doctrine appears
before dynamic session context in the prompt, preserving provider prefix-cache opportunities.

Provider failure does not end a learning turn. The deterministic renderer expresses the already-selected
teaching action and retains the student's work. Full proof release still fails closed when qualified
verification is unavailable.

Free model weights and free hosted inference are separate concerns. Ollama provides private capacity
on hardware controlled by the user; public Groq inference is operationally quota-bound. Curated maps,
the bounded problem-map cache, and deterministic action rendering reduce inference demand but do not
misrepresent hosted capacity as unlimited.

## Deliberate limits

- A failed symbolic identity is marked for review, not declared false, because hidden assumptions may exist.
- The parser accepts only a narrow arithmetic expression language and rejects attribute/private-name syntax.
- Process-local problem-map caching is an availability optimization, not a permanent certified library.
- A problem map becomes compiled/certified content only after human or formal review; that editorial workflow
  is the next expansion of the historical IMO library.
