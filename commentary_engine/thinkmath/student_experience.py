"""Deterministic student-journey view models for ThinkMath Engine v3."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from .domain import AdvaitianSession, ArchetypeHypothesis, MVCState, SessionPhase

PHASE_LABELS = {
    SessionPhase.SEED: ("Notice Structure", "What changes? What stays fixed?"),
    SessionPhase.DIRECTIONS: (
        "Explore Directions",
        "Which pattern governs the problem?",
    ),
    SessionPhase.CONVERGENCE: (
        "Prove & Connect",
        "What exact move closes the argument?",
    ),
}

HINT_LADDER = (
    (
        "Small experiment",
        "Give me a Socratic probe—a tiny experiment I can run myself, with no reveal.",
    ),
    (
        "Archetype nudge",
        "Name the most likely primary archetype, but do not reveal the operational move.",
    ),
    (
        "Direction map",
        "Show me the plausible directions and how they differ, but not the convergence point.",
    ),
    (
        "Pivot shadow",
        "Give me a one-sentence silhouette of the elegant pivot, without completing the proof.",
    ),
)


@dataclass(frozen=True, slots=True)
class ThinkingMap:
    phase_number: int
    phase_name: str
    phase_question: str
    progress: float
    observations: tuple[str, ...]
    seed_candidates: tuple[str, ...]
    directions: tuple[str, ...]
    setup: str
    move: str
    closure: str
    open_question: str
    complete: bool


@dataclass(frozen=True, slots=True)
class ProviderReadiness:
    state: str
    headline: str
    detail: str
    available_count: int


@dataclass(frozen=True, slots=True)
class CommentarySection:
    title: str
    body: str


def build_thinking_map(asset: AdvaitianSession) -> ThinkingMap:
    phase_name, phase_question = PHASE_LABELS[asset.phase]
    directions = tuple(
        f"{item.name} — {item.role}" + (f": {item.evidence}" if item.evidence else "")
        for item in asset.archetypes
    )
    established = sum(
        bool(value)
        for value in (
            asset.problem,
            asset.student_observations,
            asset.seed_hypotheses,
            asset.archetypes,
            asset.mvc.setup,
            asset.mvc.move,
            asset.mvc.closure,
        )
    )
    progress = min(1.0, established / 7)
    if not asset.problem:
        open_question = "Bring one problem into the workspace."
    elif not asset.student_observations:
        open_question = "What changes, and what appears to remain fixed?"
    elif not asset.seed_hypotheses:
        open_question = "What reusable pattern might explain those observations?"
    elif not asset.archetypes:
        open_question = "Which archetype is the engine, and which ones only support it?"
    elif not asset.mvc.setup:
        open_question = "How will you reframe the problem?"
    elif not asset.mvc.move:
        open_question = "What exact transformation will you perform?"
    elif not asset.mvc.closure:
        open_question = "What forces the conclusion or stops the process?"
    elif not asset.mvc.validated:
        open_question = "Check that Setup, Move and Closure form one valid argument."
    else:
        open_question = "The structural spine is ready for checked commentary."
    return ThinkingMap(
        phase_number=int(asset.phase),
        phase_name=phase_name,
        phase_question=phase_question,
        progress=progress,
        observations=tuple(asset.student_observations),
        seed_candidates=tuple(asset.seed_hypotheses),
        directions=directions,
        setup=asset.mvc.setup,
        move=asset.mvc.move,
        closure=asset.mvc.closure,
        open_question=open_question,
        complete=asset.mvc.validated and asset.phase == SessionPhase.CONVERGENCE,
    )


def provider_readiness(
    models: list[dict[str, Any]], blocked_keys: set[str]
) -> ProviderReadiness:
    available = [
        model
        for model in models
        if f"{model.get('provider')}::{model.get('model')}" not in blocked_keys
    ]
    if not models:
        return ProviderReadiness(
            "offline",
            "Live mentor unavailable",
            "Use a demonstration journey now, or run the private Ollama profile locally.",
            0,
        )
    if not available:
        return ProviderReadiness(
            "resting",
            "Free inference is resting",
            "Every configured model is temporarily rate-limited. Demonstrations remain available.",
            0,
        )
    providers = sorted({str(model.get("provider")) for model in available})
    return ProviderReadiness(
        "ready",
        "Socratic mentor ready",
        f"{len(available)} open-model route(s) available via {', '.join(providers)}.",
        len(available),
    )


def friendly_provider_error(error: Exception | str) -> tuple[str, str]:
    message = str(error).lower()
    if "no models" in message or "no open model" in message:
        return (
            "The live mentor is unavailable",
            "Explore a curated journey now, or run ThinkMath privately with a local Ollama model.",
        )
    if "402" in message or "payment method" in message or "billing" in message:
        return (
            "The free mentor route is unavailable",
            "A configured provider now requires billing. ThinkMath will not ask you to pay; try a demonstration or the local Ollama profile.",
        )
    if (
        "429" in message
        or "rate" in message
        or "quota" in message
        or "exhaust" in message
    ):
        return (
            "The mentor has reached today’s free capacity",
            "Your work is still here. Retry shortly, explore a demonstration, or continue privately with Ollama.",
        )
    if "timeout" in message or "network" in message or "connection" in message:
        return (
            "The mentor could not be reached",
            "This looks temporary. Your reasoning has not been lost; wait a moment and try again.",
        )
    if "top-tier" in message or "phase 3" in message:
        return (
            "Checked commentary is temporarily unavailable",
            "Continue exploring the proof now and request the final commentary when a qualified model and critic are available.",
        )
    return (
        "ThinkMath could not complete that turn",
        "Your current Thinking Map is safe. Retry, use a smaller hint, or export the session.",
    )


SECTION_NAMES = (
    "THE SEED",
    "BRUTE-FORCE WALL",
    "BRUTE PATH",
    "ELEGANT PIVOT",
    "COMPLETE REASONING",
    "PITFALLS",
    "CONNECTIONS",
    "TAKEAWAY",
)
SECTION_RE = re.compile(
    r"(?im)^\s*(?:#{1,6}\s*)?(?:\*\*)?[🌱⚙🧱💡🧭⚠🔗🏆]?\ufe0f?\s*"
    r"("
    + "|".join(re.escape(name) for name in SECTION_NAMES)
    + r")\s*(?:\*\*)?[:\-]?\s*$"
)


def split_commentary(text: str) -> tuple[CommentarySection, ...]:
    matches = list(SECTION_RE.finditer(text or ""))
    if not matches:
        return (CommentarySection("Commentary", (text or "").strip()),)
    sections: list[CommentarySection] = []
    prefix = text[: matches[0].start()].strip()
    if prefix:
        sections.append(CommentarySection("Opening", prefix))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[match.end() : end].strip()
        if body:
            sections.append(CommentarySection(match.group(1).title(), body))
    return tuple(sections) or (CommentarySection("Commentary", text.strip()),)


def passport_entry(asset: AdvaitianSession) -> dict[str, Any] | None:
    if not asset.problem or not asset.mvc.validated:
        return None
    return {
        "problem": asset.problem,
        "seed": asset.seed_hypotheses[0]
        if asset.seed_hypotheses
        else "Unlabelled seed",
        "archetypes": [item.name for item in asset.archetypes],
        "setup": asset.mvc.setup,
        "move": asset.mvc.move,
        "closure": asset.mvc.closure,
        "proof_status": asset.proof_status,
    }


def transfer_challenge(asset: AdvaitianSession) -> tuple[str, str]:
    vocabulary = " ".join(
        [*asset.seed_hypotheses, *(item.name for item in asset.archetypes)]
    ).lower()
    if "pigeon" in vocabulary:
        return (
            "Transfer challenge",
            "A drawer contains socks in 4 colours. How many socks guarantee that three share a colour—and what are the pigeons and holes?",
        )
    if "induct" in vocabulary or "layer" in vocabulary:
        return (
            "Same Seed, new disguise",
            r"Can you explain geometrically why $1+2+\cdots+n=\frac{n(n+1)}2$ without beginning with algebra?",
        )
    if "symmetr" in vocabulary or "invar" in vocabulary:
        return (
            "Same Seed, new disguise",
            "If $x+1/x=4$, determine $x^2+1/x^2$ without solving for $x$.",
        )
    return (
        "Transfer challenge",
        "Invent a new problem where the same Setup–Move–Closure would work, but the surface story looks different.",
    )


DEMO_CATALOG = {
    "odd-layers": {
        "label": "Odd numbers become squares",
        "level": "Visual pattern",
        "problem": "Prove that the sum of the first $n$ odd positive integers is $n^2$.",
        "observations": [
            "Each next odd number is exactly the border needed for the next square."
        ],
        "seed": "Geometric layering reveals an invariant square shape.",
        "archetypes": [
            ArchetypeHypothesis(
                "Domain Translation",
                "Turn a sum into growing square layers.",
                "primary",
            ),
            ArchetypeHypothesis(
                "Induction", "Each new border advances one case.", "supporting"
            ),
        ],
        "mvc": MVCState(
            "Represent $1$ as one unit square and each later odd number as an L-shaped border.",
            "Add the border of $2k+1$ units around a $k\\times k$ square.",
            "The border creates exactly a $(k+1)\\times(k+1)$ square, so after $n$ layers the area is $n^2$.",
            "domain-translation",
            True,
        ),
        "commentary": """🌱 THE SEED
The arithmetic sum is the growth record of one geometric object: a square.

🧱 BRUTE-FORCE WALL
Manipulating the series term by term proves the identity, but hides why odd numbers appear.

💡 ELEGANT PIVOT
Read each odd number as the new L-shaped boundary of a larger square.

🧭 COMPLETE REASONING
Start with one unit square. A $k\\times k$ square needs exactly $2k+1$ new unit squares—one row and one column with the corner counted once—to become $(k+1)\\times(k+1)$. Repeating this from $1$ through the first $n$ odd numbers produces an $n\\times n$ square. Therefore the sum is $n^2$.

⚠️ PITFALLS
Do not merely draw several examples; explain why the next border always contains $2k+1$ squares.

🔗 CONNECTIONS
The same picture is induction without symbolic bookkeeping: the geometry contains the base case, move and closure.

🏆 TAKEAWAY
When a sequence grows by successive differences, ask whether those differences are the visible layers of a familiar object.""",
    },
    "pigeonhole": {
        "label": "Thirteen people, twelve months",
        "level": "Counting structure",
        "problem": "Show that among 13 people, at least two were born in the same month.",
        "observations": ["There are more people than possible birth months."],
        "seed": "More objects than categories forces a collision.",
        "archetypes": [
            ArchetypeHypothesis(
                "Pigeonhole Principle",
                "13 assignments enter only 12 categories.",
                "primary",
            )
        ],
        "mvc": MVCState(
            "Treat the 13 people as pigeons and the 12 months as holes.",
            "Assign each person to their birth-month hole.",
            "If every month held at most one person, there could be at most 12 people; the thirteenth forces a shared month.",
            "pigeonhole",
            True,
        ),
        "commentary": """🌱 THE SEED
A collision becomes unavoidable when there are more objects than available categories.

🧱 BRUTE-FORCE WALL
Listing birthdays or guessing a repeated month confuses one example with a proof.

💡 ELEGANT PIVOT
Forget the calendar dates; retain only the twelve month categories.

🧭 COMPLETE REASONING
Place each of the 13 people into the month of their birth. If no two shared a month, each of the 12 months could contain at most one person, accounting for at most 12 people. Because there are 13, at least one month contains two or more.

⚠️ PITFALLS
The conclusion guarantees a shared month, not a shared birthday.

🔗 CONNECTIONS
The principle generalises to $n+1$ objects assigned to $n$ categories.

🏆 TAKEAWAY
Before counting details, count the number of possible containers.""",
    },
    "symmetric-expression": {
        "label": "Keep the symmetry intact",
        "level": "Algebraic structure",
        "problem": "If $x+1/x=3$, find $x^2+1/x^2$ without solving for $x$.",
        "observations": [
            "The target is the square of the given symmetric expression, minus a constant."
        ],
        "seed": "Preserve a symmetric expression instead of separating its parts.",
        "archetypes": [
            ArchetypeHypothesis(
                "Symmetry", "$x$ and $1/x$ occur as one balanced object.", "primary"
            )
        ],
        "mvc": MVCState(
            "Treat $x+1/x$ as one object and square it.",
            "Use $(x+1/x)^2=x^2+2+1/x^2$.",
            "The given value makes the left side 9, so subtracting 2 forces the target to equal 7.",
            "symmetry",
            True,
        ),
        "commentary": """🌱 THE SEED
The problem gives a symmetric object and asks for another symmetric object built from it.

🧱 BRUTE-FORCE WALL
Solving the quadratic for $x$ creates two roots and unnecessary substitution.

💡 ELEGANT PIVOT
Square the expression you already know while keeping $x$ and $1/x$ paired.

🧭 COMPLETE REASONING
From $x+1/x=3$, square both sides: $x^2+2+1/x^2=9$. Therefore $x^2+1/x^2=7$.

⚠️ PITFALLS
Do not forget the cross-term $2x(1/x)=2$.

🔗 CONNECTIONS
The same recurrence generates $x^n+1/x^n$ from lower symmetric powers.

🏆 TAKEAWAY
When both the data and target are symmetric, preserve the symmetry rather than solving for the pieces.""",
    },
}


def demonstration(demo_id: str) -> tuple[AdvaitianSession, list[dict[str, Any]]]:
    item = DEMO_CATALOG[demo_id]
    asset = AdvaitianSession(
        problem=item["problem"],
        phase=SessionPhase.CONVERGENCE,
        tier=2,
        student_observations=list(item["observations"]),
        seed_hypotheses=[str(item["seed"])],
        archetypes=list(item["archetypes"]),
        mvc=item["mvc"],
        proof_status="demonstration",
    )
    messages = [
        {"role": "user", "content": item["problem"]},
        {
            "role": "mentor",
            "content": (
                "Let us ignore calculation for a moment. What familiar structure is being "
                "built—or what collision is being forced—by the information in the problem?"
            ),
            "model": "Curated demonstration",
        },
        {
            "role": "user",
            "content": item["observations"][0],
        },
        {
            "role": "mentor",
            "content": item["commentary"],
            "model": "Curated demonstration",
            "proof_status": "demonstration",
        },
    ]
    return asset, messages
