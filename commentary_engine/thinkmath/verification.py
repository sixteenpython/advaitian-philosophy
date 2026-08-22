"""Deterministic checks that complement, but never defer to, an LLM critic."""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass

import sympy as sp


SAFE_EXPRESSION_RE = re.compile(r"^[A-Za-z0-9_+\-*/^().\s]+$")
SAFE_FUNCTIONS = {
    "sin": sp.sin,
    "cos": sp.cos,
    "tan": sp.tan,
    "sqrt": sp.sqrt,
    "log": sp.log,
    "exp": sp.exp,
    "pi": sp.pi,
    "E": sp.E,
}


def _safe_sympify(value: str, *, evaluate: bool = True):
    expression = str(value or "").strip().replace("^", "**")
    if not expression or len(expression) > 240 or not SAFE_EXPRESSION_RE.fullmatch(expression):
        raise ValueError("expression contains unsupported syntax")
    if "__" in expression or re.search(r"(?<!\d)\.|\.(?!\d)", expression):
        raise ValueError("attribute access is not allowed")
    names = set(re.findall(r"[A-Za-z_][A-Za-z0-9_]*", expression))
    if any(name.startswith("_") for name in names):
        raise ValueError("private names are not allowed")
    local_dict = {
        name: SAFE_FUNCTIONS.get(name, sp.Symbol(name))
        for name in names
    }
    return sp.sympify(expression, locals=local_dict, evaluate=evaluate)


@dataclass(frozen=True)
class VerificationCheck:
    name: str
    status: str
    detail: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


def verify_equivalence(lhs: str, rhs: str) -> VerificationCheck:
    """Safely check a single algebraic identity with SymPy.

    This deliberately accepts only expressions, not arbitrary Python code.
    """
    try:
        left = _safe_sympify(lhs, evaluate=True)
        right = _safe_sympify(rhs, evaluate=True)
        difference = sp.simplify(left - right)
        equivalent = difference == 0
        return VerificationCheck(
            "symbolic_equivalence",
            "pass" if equivalent else "fail",
            "Expressions are symbolically equivalent."
            if equivalent else f"Simplified difference is {difference}.",
        )
    except (sp.SympifyError, TypeError, ValueError) as exc:
        return VerificationCheck("symbolic_equivalence", "review", f"Could not parse expression: {exc}")


PLAIN_EQUATION_RE = re.compile(
    r"(?<![<>=!])([A-Za-z0-9_+\-*/^(). ]{1,120})=([A-Za-z0-9_+\-*/^(). ]{1,120})(?![=])"
)


def _parseable_expression_suffix(value: str) -> str:
    """Drop conversational prose before a plain symbolic expression."""
    candidates = [value]
    candidates.extend(value[index + 1:] for index, char in enumerate(value) if char.isspace())
    for candidate in candidates:
        candidate = candidate.strip().replace("^", "**")
        if not candidate:
            continue
        if re.match(r"(?i)^(?:i|we|think|perhaps|maybe|suppose|because|so|then|that)\b", candidate):
            continue
        try:
            _safe_sympify(candidate, evaluate=False)
            return candidate
        except (sp.SympifyError, TypeError, ValueError, SyntaxError):
            continue
    return value.strip().replace("^", "**")


def verify_student_claims(text: str) -> list[VerificationCheck]:
    """Check plain symbolic equalities without pretending to understand prose.

    A failed identity is labelled for review rather than declared false because
    the surrounding conversation may contain assumptions that SymPy has not
    encoded. LaTeX and ambiguous prose are deliberately left to the reasoning
    layer instead of being unsafely coerced.
    """
    checks: list[VerificationCheck] = []
    for match in PLAIN_EQUATION_RE.finditer(text or ""):
        lhs, rhs = (_parseable_expression_suffix(part) for part in match.groups())
        if not lhs or not rhs:
            continue
        result = verify_equivalence(lhs, rhs)
        checks.append(VerificationCheck(
            "student_symbolic_claim",
            "pass" if result.status == "pass" else "review",
            result.detail if result.status == "pass" else f"Needs assumptions or revision: {result.detail}",
        ))
        if len(checks) >= 3:
            break
    return checks


def verify_commentary(problem: str, commentary: str) -> list[VerificationCheck]:
    checks: list[VerificationCheck] = []
    text = commentary or ""
    upper = text.upper()

    required = ("SEED", "BRUTE", "PIVOT", "PITFALL", "CONNECTION", "TAKEAWAY")
    missing = [section for section in required if section not in upper]
    checks.append(VerificationCheck(
        "six_point_structure",
        "pass" if not missing else "fail",
        "All Six-Point sections present." if not missing else f"Missing: {', '.join(missing)}",
    ))

    if re.search(r"\b(descen|vieta.?jump|minimal pair)\w*", text, re.I):
        has_extremal = bool(re.search(r"\b(minim|minimal|least|extremal)\w*", text, re.I))
        has_boundary = bool(re.search(r"\b(terminat|boundary|stops?|a\s*['′]?\s*=\s*0|base case)\w*", text, re.I))
        checks.append(VerificationCheck(
            "descent_closure",
            "pass" if has_extremal and has_boundary else "fail",
            "Extremal choice and boundary/termination are explicit."
            if has_extremal and has_boundary
            else "A descent proof needs both an extremal choice and an explicit boundary/termination case.",
        ))

    problem_constraints = set(re.findall(r"(?:>|<|≥|≤|!=|≠|positive|integer|prime|real)", problem, re.I))
    if problem_constraints:
        echoed = sum(1 for token in problem_constraints if token.casefold() in text.casefold())
        checks.append(VerificationCheck(
            "constraint_trace",
            "pass" if echoed else "review",
            f"Referenced {echoed} of {len(problem_constraints)} detected constraint markers; semantic review remains required.",
        ))

    checks.append(VerificationCheck(
        "formal_proof",
        "review",
        "No general-purpose deterministic checker can certify arbitrary prose proofs; independent review is required.",
    ))
    return checks


def verification_label(checks: list[VerificationCheck], critic_status: str | None) -> str:
    if any(check.status == "fail" for check in checks) or critic_status == "UNSAFE":
        return "unverified"
    if critic_status == "SOLID" and checks and all(check.status in {"pass", "review"} for check in checks):
        return "partially_verified"
    return "structural_draft"
