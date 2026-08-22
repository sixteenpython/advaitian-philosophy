"""Canonical Advaitian Knowledge Asset.

Chat messages are evidence, not the source of truth.  This model records the
student's current mathematical understanding and can be persisted/versioned
independently of any LLM provider.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import IntEnum
from typing import Any


class SessionPhase(IntEnum):
    SEED = 1
    DIRECTIONS = 2
    CONVERGENCE = 3


@dataclass
class MVCState:
    setup: str = ""
    move: str = ""
    closure: str = ""
    family: str = ""
    validated: bool = False
    validation_notes: list[str] = field(default_factory=list)

    @property
    def complete(self) -> bool:
        return all(part.strip() for part in (self.setup, self.move, self.closure))


@dataclass
class ArchetypeHypothesis:
    name: str
    evidence: str = ""
    role: str = "candidate"
    confidence: float | None = None


@dataclass
class AdvaitianSession:
    schema_version: str = "1.0"
    revision: int = 1
    problem: str = ""
    phase: SessionPhase = SessionPhase.SEED
    tier: int = 3
    student_observations: list[str] = field(default_factory=list)
    seed_hypotheses: list[str] = field(default_factory=list)
    archetypes: list[ArchetypeHypothesis] = field(default_factory=list)
    mvc: MVCState = field(default_factory=MVCState)
    rejected_approaches: list[str] = field(default_factory=list)
    connections: list[str] = field(default_factory=list)
    hint_level: int = 0
    proof_status: str = "not_requested"
    verification_results: list[dict[str, Any]] = field(default_factory=list)
    provenance: list[dict[str, str]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["phase"] = int(self.phase)
        return data

    def apply_model_update(self, update: dict[str, Any]) -> None:
        """Apply only allow-listed, typed fields from an untrusted model."""
        for field_name in ("student_observations", "seed_hypotheses", "rejected_approaches", "connections"):
            value = update.get(field_name)
            if isinstance(value, list):
                cleaned = [str(item).strip() for item in value if str(item).strip()]
                setattr(self, field_name, cleaned[:20])
        mvc = update.get("mvc")
        if isinstance(mvc, dict):
            changed = False
            for name in ("setup", "move", "closure", "family"):
                if name in mvc and isinstance(mvc[name], str) and mvc[name].strip():
                    new_value = mvc[name].strip()
                    changed = changed or getattr(self.mvc, name) != new_value
                    setattr(self.mvc, name, new_value)
            # A model may propose MVC parts but cannot validate its own work.
            if changed:
                self.mvc.validated = False
        candidates = update.get("archetypes")
        if isinstance(candidates, list):
            parsed: list[ArchetypeHypothesis] = []
            for item in candidates[:10]:
                if isinstance(item, str) and item.strip():
                    parsed.append(ArchetypeHypothesis(item.strip()))
                elif isinstance(item, dict) and str(item.get("name", "")).strip():
                    confidence = item.get("confidence")
                    if not isinstance(confidence, (int, float)):
                        confidence = None
                    parsed.append(ArchetypeHypothesis(
                        name=str(item["name"]).strip(),
                        evidence=str(item.get("evidence", "")).strip(),
                        role=str(item.get("role", "candidate")).strip(),
                        confidence=float(confidence) if confidence is not None else None,
                    ))
            self.archetypes = parsed
        self.revision += 1

    @classmethod
    def from_dict(cls, data: dict[str, Any] | None) -> "AdvaitianSession":
        if not data:
            return cls()
        mvc = MVCState(**data.get("mvc", {}))
        archetypes = [ArchetypeHypothesis(**item) for item in data.get("archetypes", [])]
        allowed = {
            key: value for key, value in data.items()
            if key in cls.__dataclass_fields__ and key not in {"mvc", "archetypes", "phase"}
        }
        return cls(
            **allowed,
            phase=SessionPhase(int(data.get("phase", 1))),
            mvc=mvc,
            archetypes=archetypes,
        )
