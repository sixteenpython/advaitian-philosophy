"""Task-based open/open-weight model registry and routing policy."""

from __future__ import annotations

import os
from dataclasses import dataclass
from urllib.parse import urlparse


@dataclass(frozen=True)
class ModelSpec:
    provider: str
    model: str
    roles: tuple[str, ...]
    capability: int
    license: str
    local: bool = False
    context: int = 32768
    stability: str = "production"


# Candidates are promoted only after passing the repository's Advaitian evals.
OPEN_MODEL_REGISTRY = (
    ModelSpec("Ollama", "qwen3:8b", ("mentor",), 7, "Apache-2.0", True, 32768),
    ModelSpec("Ollama", "gpt-oss:20b", ("mentor", "commentary"), 9, "Apache-2.0", True, 32768),
    ModelSpec("Ollama", "qwen2.5-math:7b", ("critic",), 8, "Apache-2.0", True, 32768),
    ModelSpec("Ollama", "deepseek-r1:14b", ("critic", "commentary"), 8, "MIT", True, 32768),
    ModelSpec("Groq", "qwen/qwen3.6-27b", ("mentor", "commentary", "critic"), 9, "Apache-2.0", False, 131072, "preview"),
    ModelSpec("Groq", "openai/gpt-oss-20b", ("mentor", "critic"), 8, "Apache-2.0", False, 131072),
    ModelSpec("Groq", "openai/gpt-oss-120b", ("commentary", "critic"), 10, "Apache-2.0", False, 131072),
)


def ollama_base_url() -> str:
    configured = os.environ.get("OLLAMA_BASE_URL", "http://127.0.0.1:11434").rstrip("/")
    parsed = urlparse(configured)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("OLLAMA_BASE_URL must be an http(s) URL")
    return configured


def registry_rows() -> list[dict]:
    return [spec.__dict__.copy() for spec in OPEN_MODEL_REGISTRY]


def supports_role(provider: str, model: str, role: str) -> bool:
    matches = [spec for spec in OPEN_MODEL_REGISTRY if spec.provider == provider and spec.model == model]
    return bool(matches) and role in matches[0].roles


def capability_for(provider: str, model: str, fallback: int) -> int:
    matches = [spec for spec in OPEN_MODEL_REGISTRY if spec.provider == provider and spec.model == model]
    return matches[0].capability if matches else fallback


def stability_for(provider: str, model: str) -> str:
    matches = [spec for spec in OPEN_MODEL_REGISTRY if spec.provider == provider and spec.model == model]
    return matches[0].stability if matches else "unreviewed"
