"""Provider-independent retry and rate-limit helpers."""

from __future__ import annotations

import random
import re
import time
from collections.abc import Callable
from typing import Any


def classify_error(error: Exception | str) -> str:
    message = str(error).lower()
    compact = message.replace(" ", "")
    if "402" in message or "payment_method_required" in message or "billing" in message:
        return "billing_required"
    if "limit: 0" in message or "perdayper" in compact or "rpd" in message or "per day" in message:
        return "daily_quota"
    if "request too large" in message or "413" in message or "tokens per minute" in message:
        return "tpm_too_small"
    if "429" in message or "quota" in message or "rate limit" in message or "rate_limit" in message:
        return "minute_quota"
    if "401" in message or "403" in message or "api_key" in message or "unauthorized" in message or "permission" in message:
        return "auth"
    if "404" in message or "not found" in message or "model not found" in message:
        return "not_found"
    if any(
        re.search(rf"\b{code}\b", message)
        for code in ("408", "422", "424", "498", "500", "502", "503", "504")
    ):
        return "transient"
    if "empty response" in message or "timeout" in message or "network" in message or "connection" in message:
        return "transient"
    return "fatal"


def _response_headers(error: Exception | str) -> Any:
    response = getattr(error, "response", None)
    return getattr(response, "headers", None)


def retry_seconds(error: Exception | str, default: int = 60) -> int:
    """Read Retry-After first, then fall back to provider error text."""
    headers = _response_headers(error)
    if headers:
        value = headers.get("retry-after") or headers.get("Retry-After")
        try:
            return max(1, int(float(value))) + 1
        except (TypeError, ValueError):
            pass
        reset = headers.get("x-ratelimit-reset-requests")
        if reset:
            minutes = re.search(r"(\d+(?:\.\d+)?)m", str(reset), re.I)
            seconds = re.search(r"(\d+(?:\.\d+)?)s", str(reset), re.I)
            if minutes or seconds:
                total = (float(minutes.group(1)) * 60 if minutes else 0) + (
                    float(seconds.group(1)) if seconds else 0
                )
                return max(1, int(total)) + 1

    message = str(error)
    patterns = (
        r"retry_delay\s*\{\s*seconds:\s*(\d+)",
        r"retry in (\d+(?:\.\d+)?)s",
        r"try again in (\d+(?:\.\d+)?)\s*(?:s|sec|second)",
    )
    for pattern in patterns:
        match = re.search(pattern, message, re.I)
        if match:
            return int(float(match.group(1))) + 1
    return default


def run_model_ladder(
    candidates: list[dict[str, Any]],
    send: Callable[[dict[str, Any]], str],
    on_failure: Callable[[dict[str, Any], Exception, str], None],
    *,
    on_attempt: Callable[[dict[str, Any]], None] | None = None,
    on_retry: Callable[[dict[str, Any], Exception, float], None] | None = None,
    sleep: Callable[[float], None] = time.sleep,
    jitter: Callable[[float, float], float] = random.uniform,
) -> tuple[str, dict[str, Any]]:
    """Try every candidate, retrying a transient failure once with jitter."""
    last_error: Exception | None = None
    for candidate in candidates:
        if on_attempt:
            on_attempt(candidate)
        for attempt in range(2):
            try:
                text = send(candidate)
                if not text or not text.strip():
                    raise RuntimeError("empty response")
                return text, candidate
            except Exception as error:
                last_error = error
                kind = classify_error(error)
                if kind == "transient" and attempt == 0:
                    delay = jitter(0.15, 0.45)
                    if on_retry:
                        on_retry(candidate, error, delay)
                    sleep(delay)
                    continue
                on_failure(candidate, error, kind)
                break
    raise RuntimeError(
        f"All {len(candidates)} models failed. Last error: {last_error}"
    )
