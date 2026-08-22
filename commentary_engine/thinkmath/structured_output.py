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
STATE_KEYS = {
    "suggested_phase", "tier", "mvc", "seed_hypotheses", "archetypes",
    "mentor_action", "problem_map", "claims", "proof_obligation",
}


def _is_state_payload(payload: object) -> bool:
    return isinstance(payload, dict) and bool(STATE_KEYS.intersection(payload))


def _escape_control_chars_in_strings(text: str) -> str:
    result, in_string, escaped = [], False, False
    for char in text:
        if in_string and char in "\n\r\t":
            result.append({"\n": "\\n", "\r": "\\r", "\t": "\\t"}[char])
            continue
        result.append(char)
        if escaped:
            escaped = False
        elif char == "\\" and in_string:
            escaped = True
        elif char == '"':
            in_string = not in_string
    return "".join(result)


def _loads_tolerant(text: str) -> object:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return json.loads(_escape_control_chars_in_strings(text))


def _balanced_json_prefix(text: str) -> tuple[str, str] | None:
    start = text.find("{")
    if start < 0 or text[:start].strip(" `\n\r\t"):
        return None
    depth, in_string, escaped = 0, False, False
    for index in range(start, len(text)):
        char = text[index]
        if escaped:
            escaped = False
            continue
        if in_string and char == "\\":
            escaped = True
        elif char == '"':
            in_string = not in_string
        elif not in_string:
            if char == "{": depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    return text[start:index + 1], text[index + 1:]
    return None


def strip_private_state_blocks(text: str) -> str:
    # Some providers occasionally ignore the requested fence and return only
    # the state object.  It is still private application state and must never
    # be rendered in the chat transcript.
    try:
        standalone = _loads_tolerant(text.strip())
        if _is_state_payload(standalone):
            return ""
    except (json.JSONDecodeError, TypeError):
        pass

    visible = STATE_BLOCK_RE.sub("", text)

    def strip_generic(match: re.Match) -> str:
        try:
            return "" if _is_state_payload(json.loads(match.group(1))) else match.group(0)
        except json.JSONDecodeError:
            return match.group(0)
    visible = JSON_BLOCK_RE.sub(strip_generic, visible)
    balanced = _balanced_json_prefix(visible.strip())
    if balanced:
        candidate, remainder = balanced
        try:
            if _is_state_payload(_loads_tolerant(candidate)) and not remainder.strip(". `\n\r\t"):
                return ""
        except json.JSONDecodeError:
            if any(f'"{key}"' in candidate for key in STATE_KEYS) and not remainder.strip(". `\n\r\t"):
                return ""
    return visible


def safe_visible_fallback(state: dict[str, Any]) -> str:
    """Build a minimal student-facing reply when a model emits state only.

    Only archetype names and their evidence are eligible.  In particular, MVC
    fields remain private so an Archetype Nudge cannot accidentally reveal the
    operational move.
    """
    candidates = state.get("archetypes")
    if not isinstance(candidates, list):
        return ""
    for item in candidates:
        if not isinstance(item, dict):
            continue
        name = str(item.get("name", "")).strip()
        if not name:
            continue
        evidence = str(item.get("evidence", "")).strip()
        return f"**{name}**\n\n{evidence}" if evidence else f"**{name}**"
    return ""


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
            parsed = _loads_tolerant(state_match.group(1))
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
                parsed = _loads_tolerant(candidate.group(1))
                if _is_state_payload(parsed):
                    state = parsed
                    state_match = candidate
                    status = "structured"
                    break
            except json.JSONDecodeError:
                continue

        # Last-resort compatibility for providers that return the state object
        # without any Markdown fence.  Accept it only when it is the complete
        # response and has a recognized ThinkMath state key.
        if not state:
            try:
                balanced = _balanced_json_prefix(raw.strip())
                candidate = balanced[0] if balanced and not balanced[1].strip(". `\n\r\t") else raw.strip()
                parsed = _loads_tolerant(candidate)
                if _is_state_payload(parsed):
                    state = parsed
                    status = "structured"
            except (json.JSONDecodeError, TypeError):
                pass

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
