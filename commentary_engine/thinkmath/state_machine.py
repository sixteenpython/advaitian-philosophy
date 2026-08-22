"""Deterministic phase-transition policy for the learning journey."""

from __future__ import annotations

from dataclasses import dataclass

from .domain import AdvaitianSession, SessionPhase


STAGE2_PHRASES = (
    "stage 2", "stage-2", "six-point", "six point", "full commentary",
    "phase 3", "phase-3",
)


@dataclass(frozen=True)
class TransitionDecision:
    phase: SessionPhase
    allowed: bool
    reason: str


def explicitly_requests_commentary(text: str) -> bool:
    lowered = text.casefold()
    return any(phrase in lowered for phrase in STAGE2_PHRASES)


def evaluate_transition(
    asset: AdvaitianSession,
    user_text: str,
    model_suggested_phase: int | None = None,
) -> TransitionDecision:
    """Own phase progression outside the model.

    A model may recommend a phase but cannot bypass the MVC gate. Explicit
    requests also remain gated: the mentor should help finish the MVC first.
    """
    current = asset.phase
    suggested = SessionPhase(max(1, min(3, int(model_suggested_phase or current))))

    if current == SessionPhase.CONVERGENCE:
        return TransitionDecision(current, True, "Convergence already reached.")

    wants_commentary = explicitly_requests_commentary(user_text)
    if suggested == SessionPhase.CONVERGENCE or wants_commentary:
        if not (asset.mvc.complete and asset.mvc.validated):
            return TransitionDecision(
                max(current, SessionPhase.DIRECTIONS),
                False,
                "Stage 2 requires a validated MVC with setup, move and closure.",
            )
        return TransitionDecision(SessionPhase.CONVERGENCE, True, "Validated MVC permits convergence.")

    if suggested >= SessionPhase.DIRECTIONS:
        if asset.seed_hypotheses or asset.archetypes:
            return TransitionDecision(SessionPhase.DIRECTIONS, True, "A structural hypothesis is recorded.")
        return TransitionDecision(current, False, "Record a seed or archetype hypothesis first.")

    return TransitionDecision(current, True, "Remain in seed discovery.")
