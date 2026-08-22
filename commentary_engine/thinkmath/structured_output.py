"""Strict parsing for model-produced state updates.

The visible response may remain natural language.  An optional fenced JSON
block updates the canonical asset; malformed updates are ignored and surfaced
as unverified rather than being trusted.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any


STATE_BLOCK_RE = re.compile(r"```thinkmath-state\s*(\{.*?\})\s*```", re.I | re.S)
JSON_BLOCK_RE = re.compile(r"```json\s*(\{.*?\})\s*```", re.I | re.S)
LEGACY_METADATA_RE = re.compile(r"^\s*PHASE:\s*(\d+)\s+TIER:\s*(\d+)\s*$", re.M)
STATE_KEYS = {"suggested_phase", "tier", "mvc", "seed_hypotheses", "archetypes"}


def _is_state_payload(payload: object) -> bool:
    return isinstance(payload, dict) and bool(STATE_KEYS.intersection(payload))


def strip_private_state_blocks(text: str) -> str:
    visible = STATE_BLOCK_RE.sub("", text)

    def strip_generic(match: re.Match) -> str:
        try:
            return "" if _is_state_payload(json.loads(match.group(1))) else match.group(0)
        except json.JSONDecodeError:
            return match.group(0)

    return JSON_BLOCK_RE.sub(strip_generic, visible)


@dataclass
class ModelEnvelope:
    visible_text: str
    suggested_phase: int = 1
    tier: int = 3
    state_update: dict[str, Any] = field(default_factory=dict)
    parse_status: str = "legacy"


def parse_model_response(text: str | None) -> ModelEnvelope:
    raw = text or ""
    state_match = STATE_BLOCK_RE.search(raw)
    state: dict[str, Any] = {}
    status = "legacy"
    if state_match:
        try:
            parsed = json.loads(state_match.group(1))
            if not isinstance(parsed, dict):
                raise ValueError("state update must be an object")
            state = parsed
            status = "structured"
        except (json.JSONDecodeError, ValueError):
            status = "invalid"
    else:
        # Some open models ignore the custom fence name and emit ```json```.
        # Treat it as private state only when its keys match our state schema;
        # ordinary JSON used in a mathematical explanation remains visible.
        for candidate in JSON_BLOCK_RE.finditer(raw):
            try:
                parsed = json.loads(candidate.group(1))
                if _is_state_payload(parsed):
                    state = parsed
                    state_match = candidate
                    status = "structured"
                    break
            except json.JSONDecodeError:
                continue

    metadata = LEGACY_METADATA_RE.search(raw)
    phase = state.get("suggested_phase", 1)
    tier = state.get("tier", 3)
    if metadata:
        phase = state.get("suggested_phase", int(metadata.group(1)))
        tier = state.get("tier", int(metadata.group(2)))

    try:
        phase = max(1, min(3, int(phase)))
    except (TypeError, ValueError):
        phase = 1
        status = "invalid"
    try:
        tier = max(0, min(4, int(tier)))
    except (TypeError, ValueError):
        tier = 3
        status = "invalid"

    visible = strip_private_state_blocks(raw)
    visible = LEGACY_METADATA_RE.sub("", visible).strip()
    return ModelEnvelope(visible, phase, tier, state, status)
