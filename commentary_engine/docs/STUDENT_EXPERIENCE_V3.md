# ThinkMath Student Experience v3.2

## Product intent

ThinkMath should feel like entering a calm mathematical thinking studio. The chat remains the primary
learning experience, but the canonical `AdvaitianSession`—not the transcript—is the student's current
mathematical work.

The release optimises for one transformation:

`initial instinct -> observation -> Seed -> direction -> Setup -> Move -> Closure -> transfer`

It deliberately avoids answer-engine behaviour, generic gamification and provider-centric UI.

## Teacher-like conversation

The experience accepts confusion as a legitimate learning state. “I don’t know,” “I am confused,” a
tentative idea, and a long proof attempt are not collapsed into one fallback. The mentor acknowledges
what the student has done, preserves their mathematical agency, and offers one appropriately sized
next move. Repeated confusion reveals progressively stronger scaffolding without silently changing
the student's canonical mathematical work.

Substantial attempts receive a concise technique-level summary and one explicit proof obligation.
This prevents the experience from resetting an advanced student to a generic opening question merely
because the proposed argument is incomplete.

## Experience architecture

### Learn

The first viewport asks one question: what problem is the student wrestling with? A concise mentor
contract explains that ThinkMath will ask one precise question at a time. Three curated journeys make
the philosophy demonstrable even when free inference is unavailable.

The graduated hint ladder gives the student control over disclosure:

1. small experiment;
2. archetype nudge;
3. direction map;
4. pivot shadow.

None is intended to reveal a final answer.

### Thinking Map

The map is a deterministic view of the canonical asset. It distinguishes observations, Seed
hypotheses, directions, Setup, Move, Closure and the next unresolved question. The MVC editor appears
only after a Seed hypothesis exists or the journey reaches Directions. Models may propose content but
cannot validate their own MVC.

### Commentary

A completed Six-Point response is removed from the scrolling dialogue and presented as a structured
learning artifact. Deterministic verification and the independent critic remain unchanged. The UI does
not imply proof assurance beyond the recorded status.

Visible assurance states distinguish exploratory directions, structural drafts, structurally checked
work, unresolved mathematical review, and curated demonstrations. These labels describe the checks
actually performed; none claims general formal certification of an olympiad proof.

Every completed journey ends with a deterministic transfer challenge: the same Seed in a different
surface form.

### My Journey

The Pattern Passport records mathematical structures rather than points or streaks. A passport entry
requires an author-confirmed complete MVC. Students can download both the passport JSON and readable
session transcript. Donation links appear only after value has been delivered.

## Model resilience

The model registry and local-first Ollama architecture remain unchanged. The hosted application may
use configured no-cost open-model routes. Readiness states distinguish configured availability,
temporary exhaustion and offline operation. Raw provider exceptions are shown only in authenticated
admin mode; students receive a recovery path to retry, use a curated journey or run Ollama locally.

## Privacy

Persistence remains opt-in and is disclosed under Session & Privacy. Demonstration journeys need no
external inference. The public application does not claim that hosted processing is local; private
local-model use follows the README's Ollama instructions.

## Architecture

- `thinkmath.student_experience`: pure deterministic view models, curated demonstrations, commentary
  sectioning, transfer selection, passport entry and provider-error translation.
- `thinkmath.student_ui`: reusable Streamlit rendering components and visual system.
- `app.py`: orchestration, session mutation, model calls and composition.

The extraction keeps pedagogy and canonical state independent of Streamlit presentation.

## Release verification

- Legacy phase/MVC/provider/verification regression suite;
- deterministic student-experience unit tests;
- headless Streamlit shell and offline-demonstration test;
- compile check;
- local browser review of Learn, Thinking Map, Commentary and My Journey;
- post-deployment live verification.
