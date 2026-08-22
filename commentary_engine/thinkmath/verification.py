"""Deterministic checks that complement, but never defer to, an LLM critic."""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass

import sympy as sp


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
        left = sp.sympify(lhs, evaluate=True)
        right = sp.sympify(rhs, evaluate=True)
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
    if any(check.status == "fail" for check in checks) or critic_status in {"UNSAFE", "ERROR", "UNAVAILABLE", "UNVERIFIED"}:
        return "unverified"
    if critic_status == "SOLID" and checks and all(check.status in {"pass", "review"} for check in checks):
        return "partially_verified"
    return "unverified"
