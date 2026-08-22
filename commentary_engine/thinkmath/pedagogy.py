"""Deterministic teaching safeguards that remain useful without model inference."""

from __future__ import annotations

import re
from dataclasses import dataclass

from .domain import MVCState


@dataclass(frozen=True, slots=True)
class ClosureCheck:
    label: str
    status: str
    detail: str


@dataclass(frozen=True, slots=True)
class ClosureAssessment:
    checks: tuple[ClosureCheck, ...]
    ready: bool

    @property
    def next_obligation(self) -> str:
        item = next((check for check in self.checks if check.status == "missing"), None)
        item = item or next((check for check in self.checks if check.status == "review"), None)
        return item.detail if item else "Reconcile the complete argument with the original target."


def assess_mvc(mvc: MVCState) -> ClosureAssessment:
    """Check proof architecture without pretending to certify the mathematics."""
    combined = " ".join((mvc.setup, mvc.move, mvc.closure, mvc.family)).casefold()
    iterative = bool(re.search(r"\b(descen|vieta|induct|iterat|minimal|extremal)\w*", combined))
    has_boundary = bool(re.search(
        r"\b(base case|terminat|boundary|stops?|minimal|least|zero|=\s*0|contradiction)\b",
        combined,
    ))
    has_justification = bool(re.search(
        r"\b(because|therefore|hence|implies|forces?|preserv|invariant|by\s+\w+ theorem)\b",
        mvc.closure.casefold(),
    )) or len(mvc.closure.split()) >= 12
    has_conditions = bool(re.search(
        r"\b(condition|positive|integer|domain|distinct|nonzero|hypothesis|valid|remain)\w*",
        combined,
    ))

    checks = (
        ClosureCheck("Setup", "pass" if mvc.setup.strip() else "missing", "State the exact mathematical reframing."),
        ClosureCheck("Move", "pass" if mvc.move.strip() else "missing", "Name the operation that advances the argument."),
        ClosureCheck(
            "Validity",
            "pass" if has_justification else "review",
            "Explain why the move is valid rather than only naming it.",
        ),
        ClosureCheck(
            "Conditions",
            "pass" if has_conditions else "review",
            "Check that the problem's required conditions survive the move.",
        ),
        ClosureCheck(
            "Boundary",
            "pass" if (not iterative or has_boundary) else "missing",
            "State where the process stops and what the boundary case gives.",
        ),
        ClosureCheck(
            "Target link",
            "pass" if mvc.closure.strip() else "missing",
            "Connect the closure explicitly to the requested conclusion.",
        ),
    )
    blocking = {"Setup", "Move", "Boundary", "Target link"}
    ready = all(check.status == "pass" for check in checks if check.label in blocking)
    return ClosureAssessment(checks, ready)


def substantial_work_summary(text: str) -> str:
    """Name techniques the student actually used; never invent one."""
    patterns = (
        (r"\bvieta|other root", "a Vieta-root transformation"),
        (r"\bdescen|minimal", "a descent/minimality argument"),
        (r"\binduct", "induction"),
        (r"\bdiscriminant|quadratic formula", "a discriminant check"),
        (r"\binvarian|stays? fixed", "an invariant"),
        (r"\bfactor", "factorisation"),
        (r"\bpigeonhole", "the pigeonhole principle"),
        (r"\bsymmetr", "symmetry"),
    )
    found = [label for pattern, label in patterns if re.search(pattern, text, re.I)]
    if not found:
        return "a substantial proof direction"
    return " and ".join(found[:2])


def stage2_gate_message(mvc: MVCState) -> str:
    assessment = assess_mvc(mvc)
    return (
        "We’re close, but I won’t present a structural draft as a finished proof. "
        f"The next proof obligation is: {assessment.next_obligation} "
        "Once that is explicit, I can build the Six-Point Commentary."
    )
