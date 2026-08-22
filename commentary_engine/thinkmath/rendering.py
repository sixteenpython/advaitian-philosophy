"""Repairs common Markdown/LaTeX defects from open reasoning models."""

from __future__ import annotations

import re

from .structured_output import strip_private_state_blocks


BLOCK_LATEX_RE = re.compile(r"\\\[(.*?)\\\]", re.S)
INLINE_LATEX_RE = re.compile(r"\\\((.*?)\\\)", re.S)
MISSING_BLOCK_OPEN_RE = re.compile(
    r"(?m)^(?P<indent>\s*)(?P<body>\\(?:frac|begin|sum|prod|int|left|sqrt)[^\n]*?\$\$)"
)
SIX_POINT_INLINE_RE = re.compile(r"\s*(\*\*[🌱⚙️💡⚠️🔗🏆][^*]*\*\*)")
NUMBERED_ITEM_RE = re.compile(r"(?<!\n)\s+(\d+\.\s+\*\*)")
BULLET_ITEM_RE = re.compile(r"(?<!\n)\s+(-\s+\*\*)")


def prepare_markdown(text: str) -> str:
    if not text:
        return text
    rendered = strip_private_state_blocks(text)
    rendered = BLOCK_LATEX_RE.sub(lambda match: f"$${match.group(1).strip()}$$", rendered)
    rendered = INLINE_LATEX_RE.sub(lambda match: f"${match.group(1).strip()}$", rendered)

    # A frequent open-model defect is `\frac{...}...$$`: the closing display
    # delimiter exists but the opening one was omitted. Repair only lines that
    # begin with an unmistakable LaTeX command to avoid changing prose.
    def add_block_open(match: re.Match) -> str:
        body = match.group("body")
        if body.lstrip().startswith("$$"):
            return match.group(0)
        return f'{match.group("indent")}$${body}'

    rendered = MISSING_BLOCK_OPEN_RE.sub(add_block_open, rendered)
    rendered = SIX_POINT_INLINE_RE.sub(r"\n\n\1\n", rendered)
    rendered = NUMBERED_ITEM_RE.sub(r"\n\1", rendered)
    rendered = BULLET_ITEM_RE.sub(r"\n\1", rendered)
    rendered = re.sub(r"\n{3,}", "\n\n", rendered)
    return rendered.strip()
