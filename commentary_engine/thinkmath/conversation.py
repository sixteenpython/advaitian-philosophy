"""Conversation signals that adapt teaching without changing mathematical truth."""

from __future__ import annotations

import re
from dataclasses import dataclass
from enum import Enum


class TurnKind(str, Enum):
    SUBSTANTIVE = "substantive"
    PARTIAL = "partial"
    STUCK = "stuck"
    CONFUSED = "confused"
    REPEAT = "repeat"
    EXAMPLE = "example"
    DISAGREE = "disagree"


RECOVERY_KINDS = {
    TurnKind.STUCK,
    TurnKind.CONFUSED,
    TurnKind.REPEAT,
    TurnKind.EXAMPLE,
    TurnKind.DISAGREE,
}


@dataclass(frozen=True, slots=True)
class StudentTurn:
    kind: TurnKind
    text: str

    @property
    def is_recovery(self) -> bool:
        return self.kind in RECOVERY_KINDS


def classify_student_turn(text: str | None) -> StudentTurn:
    raw = (text or "").strip()
    lowered = re.sub(r"\s+", " ", raw.casefold().replace("’", "'"))

    uncertain = re.search(
        r"\b(i (?:do not|don't|dont) know|i (?:do not|don't|dont) get it|i (?:cannot|can't) think|no idea|no clue|not sure|unsure|i(?:'| a)?m stuck|can't do|cannot do|help me)\b",
        lowered,
    )
    if uncertain and (
        re.search(r"\b(maybe|perhaps|but|i think|could it|might)\b", lowered)
        or re.search(r"\bhow to (?:prove|solve|show|find|calculate)\b", lowered)
    ):
        return StudentTurn(TurnKind.PARTIAL, raw)
    if uncertain:
        return StudentTurn(TurnKind.STUCK, raw)
    if re.search(r"\b(confused|lost|not following|don't understand|dont understand|doesn't make sense|doesnt make sense)\b", lowered):
        return StudentTurn(TurnKind.CONFUSED, raw)
    if re.search(r"\b(repeat|say that again|explain again|what do you mean|rephrase)\b", lowered):
        return StudentTurn(TurnKind.REPEAT, raw)
    if re.search(r"\b(give|show|need|want|see)\b.{0,24}\b(example|small case)\b", lowered):
        return StudentTurn(TurnKind.EXAMPLE, raw)
    if len(lowered.split()) <= 12 and re.search(
        r"\b(that(?:'s| is) wrong|you(?:'re| are) wrong|i disagree|not true|incorrect)\b",
        lowered,
    ):
        return StudentTurn(TurnKind.DISAGREE, raw)
    return StudentTurn(TurnKind.SUBSTANTIVE, raw)


def next_support_level(previous: int, turn: StudentTurn) -> int:
    if turn.is_recovery:
        return min(5, max(0, int(previous)) + 1)
    if turn.kind == TurnKind.PARTIAL:
        return max(0, int(previous) - 1)
    return 0


def accepted_state_update(turn: StudentTurn, update: dict) -> dict:
    """Recovery language may shape dialogue but may not modify math state."""
    return {} if turn.is_recovery else update


def accepted_phase_suggestion(
    turn: StudentTurn,
    current_phase: int,
    model_suggested_phase: int,
) -> int:
    return current_phase if turn.is_recovery else model_suggested_phase


def mentor_conversation_context(turn: StudentTurn, support_level: int) -> str:
    """Return a compact, hidden instruction for the current teaching move."""
    if turn.kind == TurnKind.SUBSTANTIVE:
        return (
            "CONVERSATION MOVE: Respond to the student's exact idea before guiding. "
            "Use natural prose and ask at most one focused question."
        )
    if turn.kind == TurnKind.PARTIAL:
        return (
            "CONVERSATION MOVE: The student is uncertain but has offered a possible idea. "
            "Separate what is promising from what still needs checking; do not discard the idea. "
            "Ask one small verification question."
        )

    moves = {
        1: "Rephrase the last question in plain language and point to one specific object to inspect.",
        2: "Offer a tiny numerical or visual experiment the student can perform immediately.",
        3: "Offer two concrete directions and ask the student to choose one; avoid an open-ended question.",
        4: "Demonstrate one micro-step, explain why it is allowed, then ask the student for only the next micro-step.",
        5: "Reset the explanation using a different representation, summarize what is already known, and rebuild from the smallest case.",
    }
    kind_guidance = {
        TurnKind.STUCK: "Treat 'I don't know' as a request for smaller cognitive steps, not as failure.",
        TurnKind.CONFUSED: "Briefly identify where the explanation likely jumped, then step back without blame.",
        TurnKind.REPEAT: "Do not repeat the same wording; change representation or use a concrete case.",
        TurnKind.EXAMPLE: "Give the smallest useful example without revealing the original problem's full move.",
        TurnKind.DISAGREE: "Take the objection seriously, re-check the claim, and invite the student to locate the disputed step.",
    }
    level = min(5, max(1, int(support_level)))
    return (
        f"CONVERSATION RECOVERY: {kind_guidance[turn.kind]} {moves[level]} "
        "Acknowledge naturally in one short sentence. Do not use headings, tables, generic praise, "
        "or the phrases 'Seed' and 'diagnostic question'. Ask at most one question. "
        "Do not advance the phase or treat this utterance as mathematical evidence."
    )


def recovery_acknowledgement(turn: StudentTurn) -> str:
    openings = {
        TurnKind.STUCK: "That's okay—let's make the next step smaller.",
        TurnKind.CONFUSED: "I can see where this became unclear—let's step back one step.",
        TurnKind.REPEAT: "Of course—let me explain it a different way.",
        TurnKind.EXAMPLE: "Let's make it concrete with a small example.",
        TurnKind.DISAGREE: "That's a fair challenge—let's check the disputed step carefully.",
    }
    return openings.get(turn.kind, "")


def model_user_message(turn: StudentTurn, support_level: int) -> str:
    """Wrap recovery turns so small open models reliably follow the teacher move."""
    if not turn.is_recovery:
        return turn.text
    opening = recovery_acknowledgement(turn)
    return (
        f'The student\'s exact message is: "{turn.text}"\n\n'
        f'Begin your student-facing reply exactly with: "{opening}"\n'
        f"Then follow this private teaching instruction: "
        f"{mentor_conversation_context(turn, support_level)}\n"
        "Return only the student-facing reply followed by the required private state block."
    )


def ensure_recovery_acknowledgement(turn: StudentTurn, visible_text: str) -> str:
    """Guarantee a humane opening even when a small model ignores the instruction."""
    opening = recovery_acknowledgement(turn)
    text = (visible_text or "").strip()
    normalized_text = text.casefold().replace("’", "'").replace("–", "-").replace("—", "-")
    normalized_opening = opening.casefold().replace("’", "'").replace("–", "-").replace("—", "-")
    if not opening or normalized_text.startswith(normalized_opening):
        return text
    return f"{opening}\n\n{text}" if text else opening


def first_substantive_user_message(messages: list[dict], fallback: str = "") -> str:
    for message in messages:
        if message.get("role") != "user":
            continue
        text = str(message.get("content", "")).strip()
        if text and not classify_student_turn(text).is_recovery:
            return text
    return fallback
