"""Inference adapters kept separate from pedagogy and UI."""

from __future__ import annotations

from groq import Groq
from openai import OpenAI


GROQ_FREE_TPM_BUDGET = 7800
MIN_COMPLETION_TOKENS = 384


def _messages(system_instruction: str, history: list, user_message: str) -> list[dict[str, str]]:
    messages = [{"role": "system", "content": system_instruction}]
    for item in history:
        role = "user" if item["role"] == "user" else "assistant"
        messages.append({"role": role, "content": item["content"]})
    messages.append({"role": "user", "content": user_message})
    return messages


def _estimated_tokens(messages: list[dict[str, str]]) -> int:
    return sum((len(item["content"]) // 3) + 12 for item in messages)


def _fit_groq_budget(messages: list[dict[str, str]]) -> tuple[list[dict[str, str]], int]:
    """Drop oldest history until a useful completion fits the free TPM cap."""
    fitted = list(messages)
    while len(fitted) > 2 and _estimated_tokens(fitted) + MIN_COMPLETION_TOKENS > GROQ_FREE_TPM_BUDGET:
        fitted.pop(1)
    available = GROQ_FREE_TPM_BUDGET - _estimated_tokens(fitted)
    if available < MIN_COMPLETION_TOKENS:
        raise ValueError("request too large for the configured Groq token budget")
    return fitted, available


class GroqAdapter:
    provider = "Groq"

    def __init__(self, model_name: str, system_instruction: str, api_key: str | None = None, client=None):
        self.model_name = model_name
        self.system_instruction = system_instruction
        self._client = client or Groq(api_key=api_key, timeout=30.0, max_retries=0)

    def send(self, user_message: str, history: list, max_output_tokens: int) -> str:
        reasoning_options = {}
        if "gpt-oss" in self.model_name.lower() or "qwen" in self.model_name.lower():
            # Without these controls, reasoning models can consume the complete
            # allowance in hidden reasoning and return empty visible content.
            reasoning_options = {"reasoning_effort": "low", "reasoning_format": "hidden"}
        messages, available_output_tokens = _fit_groq_budget(
            _messages(self.system_instruction, history, user_message)
        )
        # Groq accounts for prompt + requested completion against TPM. A
        # conservative character estimate prevents a nominal 5K completion
        # from making an otherwise small request invalid as history grows.
        output_tokens = min(max_output_tokens, available_output_tokens)
        completion = self._client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=0.3,
            max_tokens=output_tokens,
            **reasoning_options,
        )
        return completion.choices[0].message.content or ""


class OllamaAdapter:
    provider = "Ollama"

    def __init__(self, model_name: str, system_instruction: str, base_url: str, client=None):
        self.model_name = model_name
        self.system_instruction = system_instruction
        self._client = client or OpenAI(api_key="ollama-local", base_url=f"{base_url}/v1")

    def send(self, user_message: str, history: list, max_output_tokens: int) -> str:
        completion = self._client.chat.completions.create(
            model=self.model_name,
            messages=_messages(self.system_instruction, history, user_message),
            temperature=0.25,
            max_tokens=max_output_tokens,
        )
        return completion.choices[0].message.content or ""
