"""Fail-closed configuration helpers."""

from __future__ import annotations

import hmac
import os


def admin_enabled(configured_pin: str | None, supplied_pin: str | None) -> bool:
    """No configured secret means no admin mode; there is no fallback PIN."""
    if not configured_pin or not supplied_pin:
        return False
    return hmac.compare_digest(str(configured_pin), str(supplied_pin))


def env_truthy(name: str, default: bool = False) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.strip().casefold() in {"1", "true", "yes", "on"}
