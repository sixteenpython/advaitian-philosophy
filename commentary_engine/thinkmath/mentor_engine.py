"""Algorithmically governed mentorship for open-model mathematical dialogue.

The language model is a valuable candidate generator and conversationalist, but
it is not the owner of student state or pedagogy.  This module chooses the next
teaching action, validates model proposals, and maintains a compact problem map
that can be reused without another expensive analysis call.
"""

from __future__ import annotations

import hashlib
import re
import threading
from collections import OrderedDict
from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any

from .conversation import StudentTurn, TurnKind
from .domain import AdvaitianSession, SessionPhase


_PROBLEM_MAP_CACHE: OrderedDict[str, dict[str, Any]] = OrderedDict()
_PROBLEM_MAP_CACHE_LOCK = threading.Lock()
_PROBLEM_MAP_CACHE_LIMIT = 256


class MentorAction(str, Enum):
    RESPOND_TO_IDEA = "respond_to_idea"
    ASK_OBSERVATION = "ask_observation"
    NARROW_GOAL = "narrow_goal"
    TEST_SMALL_CASE = "test_small_case"
    OFFER_DIRECTIONS = "offer_directions"
    MODEL_MICRO_STEP = "model_micro_step"
    CHANGE_REPRESENTATION = "change_representation"
    CHECK_DISPUTED_STEP = "check_disputed_step"
    COMPARE_DIRECTIONS = "compare_directions"
    COMPLETE_MVC = "complete_mvc"
    RELEASE_COMMENTARY = "release_commentary"


@dataclass(frozen=True, slots=True)
class MentorDecision:
    action: MentorAction
    objective: str
    reveal_limit: str
    reason: str
    routing_profile: str = "reasoning"

    def to_dict(self) -> dict[str, str]:
        return {**asdict(self), "action": self.action.value}

    def prompt_instruction(self) -> str:
        return (
            "ALGORITHMIC MENTOR DECISION (binding):\n"
            f"- Action: {self.action.value}\n"
            f"- Teaching objective: {self.objective}\n"
            f"- Reveal boundary: {self.reveal_limit}\n"
            f"- Policy reason: {self.reason}\n"
            "You may reason creatively and phrase this naturally, but do not replace "
            "the selected action or cross its reveal boundary. Return at most one question."
        )


@dataclass(slots=True)
class ProblemMap:
    fingerprint: str = ""
    domain: str = "unknown"
    current_goal: str = "understand the problem's structure"
    observations: list[str] = field(default_factory=list)
    directions: list[dict[str, Any]] = field(default_factory=list)
    proof_obligations: list[str] = field(default_factory=list)
    misconceptions: list[str] = field(default_factory=list)
    candidate_mvc: dict[str, str] = field(default_factory=dict)
    confidence: float = 0.0
    source: str = "working"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, value: dict[str, Any] | None, problem: str = "") -> "ProblemMap":
        raw = value if isinstance(value, dict) else {}
        directions: list[dict[str, Any]] = []
        for item in raw.get("directions", [])[:6] if isinstance(raw.get("directions"), list) else []:
            if not isinstance(item, dict):
                continue
            name = _short_text(item.get("name"), 80)
            if not name:
                continue
            confidence = item.get("confidence", 0.0)
            try:
                confidence = max(0.0, min(1.0, float(confidence)))
            except (TypeError, ValueError):
                confidence = 0.0
            directions.append({
                "name": name,
                "reason": _short_text(item.get("reason"), 240),
                "confidence": confidence,
            })

        mvc = raw.get("candidate_mvc") if isinstance(raw.get("candidate_mvc"), dict) else {}
        return cls(
            fingerprint=_short_text(raw.get("fingerprint"), 64) or problem_fingerprint(problem),
            domain=_short_text(raw.get("domain"), 60) or "unknown",
            current_goal=_short_text(raw.get("current_goal"), 240)
            or "understand the problem's structure",
            observations=_text_list(raw.get("observations"), 8, 240),
            directions=directions,
            proof_obligations=_text_list(raw.get("proof_obligations"), 8, 240),
            misconceptions=_text_list(raw.get("misconceptions"), 6, 240),
            candidate_mvc={
                key: _short_text(mvc.get(key), 300)
                for key in ("setup", "move", "closure", "family")
                if _short_text(mvc.get(key), 300)
            },
            confidence=_bounded_float(raw.get("confidence")),
            source="compiled" if raw.get("source") == "compiled" else "working",
        )

    def prompt_context(self) -> str:
        directions = "; ".join(
            f"{item['name']} ({item.get('reason', '')})" for item in self.directions[:4]
        ) or "not mapped yet"
        obligations = "; ".join(self.proof_obligations[:4]) or "not mapped yet"
        return (
            "WORKING PROBLEM MAP (untrusted hypotheses; test before using):\n"
            f"Domain: {self.domain}\nCurrent goal: {self.current_goal}\n"
            f"Candidate directions: {directions}\nProof obligations: {obligations}\n"
            f"Map confidence: {self.confidence:.2f}"
        )


def _short_text(value: Any, limit: int) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()[:limit]


def _text_list(value: Any, count: int, item_limit: int) -> list[str]:
    if not isinstance(value, list):
        return []
    return [text for item in value[:count] if (text := _short_text(item, item_limit))]


def _bounded_float(value: Any) -> float:
    try:
        return max(0.0, min(1.0, float(value)))
    except (TypeError, ValueError):
        return 0.0


def problem_fingerprint(problem: str) -> str:
    normalized = re.sub(r"\s+", " ", (problem or "").casefold()).strip()
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:16] if normalized else ""


_COMPILED_PROBLEM_MAPS = {
    problem_fingerprint("Prove that the sum of the first n odd positive integers is n^2."): {
        "domain": "algebra and induction",
        "current_goal": "notice how consecutive square totals change",
        "observations": ["successive totals add the next odd number"],
        "directions": [
            {"name": "Induction / Recursion", "reason": "compare consecutive partial sums", "confidence": 1.0},
            {"name": "Geometric decomposition", "reason": "odd layers grow a square", "confidence": 1.0},
        ],
        "proof_obligations": ["establish the first case", "show the next odd layer creates the next square"],
        "confidence": 1.0,
        "source": "compiled",
    },
    problem_fingerprint("Show that among 13 people, at least two were born in the same month."): {
        "domain": "combinatorics",
        "current_goal": "identify the objects and the available categories",
        "observations": ["there are more people than months"],
        "directions": [
            {"name": "Pigeonhole Principle", "reason": "13 objects occupy 12 categories", "confidence": 1.0},
        ],
        "proof_obligations": ["define pigeons and holes", "state what a collision means"],
        "confidence": 1.0,
        "source": "compiled",
    },
    problem_fingerprint("If x+1/x=3, find x^2+1/x^2 without solving for x."): {
        "domain": "algebra",
        "current_goal": "preserve the symmetric expression instead of solving for x",
        "observations": ["the target and given are symmetric under x ↔ 1/x"],
        "directions": [
            {"name": "Symmetry", "reason": "both expressions are unchanged by reciprocal exchange", "confidence": 1.0},
            {"name": "Hidden Structure", "reason": "the target appears in the square of the given", "confidence": 1.0},
        ],
        "proof_obligations": ["expand the square", "account for the cross term"],
        "confidence": 1.0,
        "source": "compiled",
    },
}


def cached_problem_map(problem: str) -> ProblemMap | None:
    """Return a defensive copy of a previously analyzed identical problem."""
    fingerprint = problem_fingerprint(problem)
    if not fingerprint:
        return None
    compiled = _COMPILED_PROBLEM_MAPS.get(fingerprint)
    if compiled is not None:
        return ProblemMap.from_dict(compiled, problem)
    with _PROBLEM_MAP_CACHE_LOCK:
        value = _PROBLEM_MAP_CACHE.get(fingerprint)
        if value is None:
            return None
        _PROBLEM_MAP_CACHE.move_to_end(fingerprint)
        return ProblemMap.from_dict(value, problem)


def cache_problem_map(problem: str, problem_map: ProblemMap) -> None:
    """Bound process memory while avoiding repeat analysis across sessions."""
    fingerprint = problem_fingerprint(problem)
    if not fingerprint or problem_map.confidence <= 0:
        return
    value = problem_map.to_dict()
    value["fingerprint"] = fingerprint
    with _PROBLEM_MAP_CACHE_LOCK:
        _PROBLEM_MAP_CACHE[fingerprint] = value
        _PROBLEM_MAP_CACHE.move_to_end(fingerprint)
        while len(_PROBLEM_MAP_CACHE) > _PROBLEM_MAP_CACHE_LIMIT:
            _PROBLEM_MAP_CACHE.popitem(last=False)


def choose_mentor_action(
    asset: AdvaitianSession,
    turn: StudentTurn,
    support_level: int,
    user_text: str,
) -> MentorDecision:
    """Select the pedagogical move independently of any model recommendation."""
    level = max(0, min(5, int(support_level)))

    if turn.kind == TurnKind.DISAGREE:
        return MentorDecision(
            MentorAction.CHECK_DISPUTED_STEP,
            "locate and test the exact disputed claim",
            "Do not defend the prior response or reveal a new solution step.",
            "The student's objection requires verification before progression.",
            "reasoning",
        )
    if turn.kind == TurnKind.EXAMPLE or (turn.is_recovery and level == 2):
        return MentorDecision(
            MentorAction.TEST_SMALL_CASE,
            "make one structural feature visible in the smallest useful case",
            "Reveal the example's computation, not the original problem's operational move.",
            "A concrete experiment reduces cognitive load while preserving discovery.",
            "conversational",
        )
    if turn.is_recovery:
        recovery_actions = {
            1: (MentorAction.NARROW_GOAL, "reduce the current task to one observable feature"),
            2: (MentorAction.TEST_SMALL_CASE, "make the structure concrete in a tiny case"),
            3: (MentorAction.OFFER_DIRECTIONS, "offer two bounded choices the student can compare"),
            4: (MentorAction.MODEL_MICRO_STEP, "demonstrate exactly one justified micro-step"),
            5: (MentorAction.CHANGE_REPRESENTATION, "restart from a visual, numerical, or equivalent representation"),
        }
        action, objective = recovery_actions.get(max(1, level), recovery_actions[1])
        return MentorDecision(
            action,
            objective,
            "Do not advance phase, record mathematical evidence, or expose the full pivot.",
            "Recovery language changes support, not mathematical truth.",
            "conversational" if level <= 2 else "reasoning",
        )

    if asset.phase == SessionPhase.CONVERGENCE:
        return MentorDecision(
            MentorAction.RELEASE_COMMENTARY,
            "connect the completed proof to reusable olympiad structure",
            "A complete proof is allowed, but every load-bearing claim must be checkable.",
            "The validated MVC gate has already been crossed.",
            "proof",
        )
    if asset.phase == SessionPhase.DIRECTIONS:
        if not asset.mvc.complete:
            return MentorDecision(
                MentorAction.COMPLETE_MVC,
                "help the student supply the next missing Setup–Move–Closure component",
                "Reveal at most one missing component and prefer a question when possible.",
                "A structural hypothesis exists, but the proof mechanism is incomplete.",
                "reasoning",
            )
        return MentorDecision(
            MentorAction.RESPOND_TO_IDEA,
            "stress-test the proposed Setup–Move–Closure path",
            "Do not call the path validated; the application owns validation.",
            "All MVC components exist and now require reconciliation.",
            "reasoning",
        )
    if asset.student_observations or asset.seed_hypotheses or asset.archetypes:
        return MentorDecision(
            MentorAction.COMPARE_DIRECTIONS,
            "compare two or three plausible mechanisms against the student's evidence",
            "Name candidate archetypes if useful, but do not reveal their operational moves.",
            "The student has supplied enough evidence to compare structural directions.",
            "reasoning",
        )
    return MentorDecision(
        MentorAction.ASK_OBSERVATION,
        "surface one invariant, constraint, symmetry, or repeated structure",
        "Do not name the primary archetype or begin solving.",
        "No student-owned structural observation is recorded yet.",
        "reasoning",
    )


def deterministic_fallback(decision: MentorDecision, problem_map: ProblemMap | None = None) -> str:
    """Keep mentorship alive when every inference route is unavailable."""
    goal = (problem_map.current_goal if problem_map else "the current goal").rstrip(".")
    responses = {
        MentorAction.ASK_OBSERVATION: f"Let’s stay with the structure. Our immediate goal is to {goal}. In the problem, what changes—and what appears unable to change?",
        MentorAction.NARROW_GOAL: f"That’s okay—let’s make the next step smaller. Focus only on this: {goal}. What is one fact you can read directly from the problem?",
        MentorAction.TEST_SMALL_CASE: "Let’s make it concrete. Try the smallest non-trivial case satisfying every condition; what survives when you compute it?",
        MentorAction.OFFER_DIRECTIONS: "Let’s reduce the choice: would you rather test a small case, or rewrite the condition in an equivalent form?",
        MentorAction.MODEL_MICRO_STEP: "I’ll take one small step: write the given condition in its most literal algebraic form. What single simplification would you make next?",
        MentorAction.CHANGE_REPRESENTATION: "Let’s restart in a different form. Can you represent the same condition with a short table, diagram, or sequence of small cases?",
        MentorAction.CHECK_DISPUTED_STEP: "That’s a fair challenge. Which exact equality or implication should we test first?",
        MentorAction.COMPARE_DIRECTIONS: "Two useful tests are available: preserve what stays fixed, or rewrite the condition to expose hidden structure. Which fits your observation better?",
        MentorAction.COMPLETE_MVC: "We have a direction, but one link is still missing. What operation turns the setup into something that forces the conclusion?",
        MentorAction.RESPOND_TO_IDEA: "Let’s test that idea at its load-bearing step. Which implication would make the argument fail if it were false?",
        MentorAction.RELEASE_COMMENTARY: "The proof path is retained, but a checked full commentary needs an available reasoning model. We can still verify it one step at a time—what step should we inspect first?",
    }
    return responses[decision.action]


_SIGNIFICANT = re.compile(r"[a-z][a-z0-9_-]{2,}|\d+", re.I)


def _grounded(candidate: str, user_text: str) -> bool:
    candidate_tokens = {token.casefold() for token in _SIGNIFICANT.findall(candidate)}
    user_tokens = {token.casefold() for token in _SIGNIFICANT.findall(user_text)}
    if not candidate_tokens:
        return False
    return len(candidate_tokens & user_tokens) >= min(2, len(candidate_tokens))


def validate_state_proposal(
    asset: AdvaitianSession,
    turn: StudentTurn,
    user_text: str,
    proposal: dict[str, Any],
) -> tuple[dict[str, Any], ProblemMap | None, list[str]]:
    """Accept only student-grounded state; retain model reasoning as a problem map.

    Model-inferred directions can guide the mentor, but are never silently
    attributed to the student and never authorize a phase transition.
    """
    if not isinstance(proposal, dict):
        return {}, None, ["model proposal was not an object"]

    notes: list[str] = []
    proposed_map = proposal.get("problem_map")
    problem_map = None
    if isinstance(proposed_map, dict):
        # Open models often emit a partial map on later turns. Preserve prior
        # analysis for omitted/empty fields instead of letting a terse response
        # erase useful proof obligations or candidate directions.
        merged_map = dict(asset.problem_map) if isinstance(asset.problem_map, dict) else {}
        for key, value in proposed_map.items():
            if value not in (None, "", [], {}):
                merged_map[key] = value
        problem_map = ProblemMap.from_dict(merged_map, asset.problem)
    if turn.is_recovery:
        return {}, problem_map, ["recovery turn cannot modify mathematical state"]

    accepted: dict[str, Any] = {}
    for key in ("student_observations", "seed_hypotheses", "rejected_approaches"):
        grounded = [item for item in _text_list(proposal.get(key), 12, 300) if _grounded(item, user_text)]
        if grounded:
            existing = [str(item) for item in getattr(asset, key, [])]
            accepted[key] = list(dict.fromkeys([*existing, *grounded]))[:20]
        elif proposal.get(key):
            notes.append(f"ignored ungrounded {key}")

    accepted_archetypes = []
    for item in proposal.get("archetypes", [])[:8] if isinstance(proposal.get("archetypes"), list) else []:
        if not isinstance(item, dict):
            continue
        name = _short_text(item.get("name"), 80)
        if name and (_grounded(name, user_text) or any(a.name.casefold() == name.casefold() for a in asset.archetypes)):
            accepted_archetypes.append(item)
        elif name:
            notes.append(f"kept model-inferred archetype '{name}' outside student state")
            if problem_map is not None and not any(d["name"].casefold() == name.casefold() for d in problem_map.directions):
                problem_map.directions.append({
                    "name": name,
                    "reason": _short_text(item.get("evidence"), 240),
                    "confidence": _bounded_float(item.get("confidence")),
                })
    if accepted_archetypes:
        by_name = {
            item.name.casefold(): {
                "name": item.name,
                "evidence": item.evidence,
                "role": item.role,
                "confidence": item.confidence,
            }
            for item in asset.archetypes
        }
        by_name.update({str(item["name"]).casefold(): item for item in accepted_archetypes})
        accepted["archetypes"] = list(by_name.values())[:10]

    mvc = proposal.get("mvc")
    if isinstance(mvc, dict):
        accepted_mvc = {
            key: text
            for key in ("setup", "move", "closure", "family")
            if (text := _short_text(mvc.get(key), 300)) and _grounded(text, user_text)
        }
        if accepted_mvc:
            accepted["mvc"] = accepted_mvc
        if any(_short_text(mvc.get(key), 300) for key in ("setup", "move", "closure")) and len(accepted_mvc) < 3:
            notes.append("kept model-authored MVC outside student state")
            if problem_map is None:
                problem_map = ProblemMap.from_dict({}, asset.problem)
            problem_map.candidate_mvc = {
                key: _short_text(mvc.get(key), 300)
                for key in ("setup", "move", "closure", "family")
                if _short_text(mvc.get(key), 300)
            }

    connections = _text_list(proposal.get("connections"), 10, 300)
    if connections:
        accepted["connections"] = connections
    return accepted, problem_map, notes
