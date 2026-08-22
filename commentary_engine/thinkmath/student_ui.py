"""Reusable Streamlit presentation components for the ThinkMath student experience."""

from __future__ import annotations

import html
import json
from typing import Any

import streamlit as st

from .domain import AdvaitianSession, SessionPhase
from .student_experience import (
    DEMO_CATALOG,
    ProviderReadiness,
    ThinkingMap,
    passport_entry,
    split_commentary,
    transfer_challenge,
)


def inject_student_theme() -> None:
    st.markdown(
        """
        <style>
        .block-container { max-width: 1260px; padding-top: 2.2rem; padding-bottom: 4rem; }
        .tm-hero { border-bottom: 1px solid #e6dfd2; padding: .2rem 0 1.2rem; margin-bottom: 1rem; }
        .tm-kicker { color:#a45f18; font-size:.76rem; font-weight:800; letter-spacing:.13em; }
        .tm-hero h1 { color:#16211d !important; font-family: Georgia, serif !important;
                      font-size:3rem !important; margin:.25rem 0 .2rem; letter-spacing:-.04em; }
        .tm-hero p { color:#4e5a54; font-size:1.08rem; margin:0; }
        .tm-phase { display:grid; grid-template-columns:repeat(3,1fr); gap:.55rem; margin:.6rem 0 1.2rem; }
        .tm-phase-step { border:1px solid #ded8cb; border-radius:10px; padding:.65rem .8rem;
                         color:#7d817e; background:#fbfaf7; }
        .tm-phase-step strong { display:block; color:inherit; font-size:.88rem; }
        .tm-phase-step span { font-size:.76rem; }
        .tm-phase-step.active { border-color:#d28a36; color:#7d4510; background:#fff7e9; }
        .tm-phase-step.complete { border-color:#668b74; color:#355b43; background:#f2f8f3; }
        .tm-map-card { background:#fbfaf7; border:1px solid #e1dbcf; border-radius:12px;
                       padding:.9rem 1rem; margin:.5rem 0; }
        .tm-map-label { color:#9a672c; font-size:.72rem; font-weight:800; letter-spacing:.08em;
                        text-transform:uppercase; margin-bottom:.25rem; }
        .tm-map-value { color:#26312c; line-height:1.55; }
        .tm-open-question { background:#fff6e7; border-left:4px solid #d28a36; padding:.8rem 1rem;
                            border-radius:0 9px 9px 0; margin:.7rem 0; }
        .tm-zero { background:linear-gradient(135deg,#fffaf1,#f4f8f3); border:1px solid #e2dccf;
                   border-radius:16px; padding:1.2rem 1.3rem; margin:.7rem 0 1rem; }
        .tm-zero h3 { margin-top:0; color:#24332b !important; }
        .tm-section-title { color:#985c1c; font-size:.76rem; font-weight:800;
                            letter-spacing:.1em; text-transform:uppercase; }
        [data-testid="stChatMessage"] { border:1px solid #e3ddd2 !important; border-left:0 !important;
                                        border-radius:12px !important; background:#fff !important;
                                        box-shadow:none !important; }
        [data-testid="stChatInput"] textarea { min-height:76px !important; }
        .stTabs [data-baseweb="tab-list"] { gap:1rem; border-bottom:1px solid #e1dbcf; }
        .stTabs [data-baseweb="tab"] { height:3rem; padding:0 .2rem; }
        .stTabs [aria-selected="true"] { color:#9a5d1c !important; }
        div[data-testid="stVerticalBlockBorderWrapper"] { border-radius:12px !important;
                                                           border-color:#e1dbcf !important; }
        @media(max-width:768px) {
          .tm-hero h1 { font-size:2.1rem !important; }
          .tm-phase { grid-template-columns:1fr; }
          .block-container { padding-top:1rem; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero(engine_version: str) -> None:
    st.markdown(
        """
        <div class="tm-hero">
          <div class="tm-kicker">ADVAITIAN MATHEMATICAL THINKING</div>
          <h1>ThinkMath.ai</h1>
          <p>See the structure. Find the Seed. Build the proof.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption(
        f"Student Experience v{engine_version} · Socratic by design · Open-model intelligence"
    )


def render_phase_path(current_phase: int) -> None:
    steps = (
        (1, "Notice Structure", "What changes? What stays fixed?"),
        (2, "Explore Directions", "Which pattern governs the problem?"),
        (3, "Prove & Connect", "What closes the argument?"),
    )
    cards = []
    for number, title, caption in steps:
        css_class = (
            "complete"
            if number < current_phase
            else "active"
            if number == current_phase
            else ""
        )
        mark = "✓" if number < current_phase else str(number)
        cards.append(
            f'<div class="tm-phase-step {css_class}"><strong>{mark}. {title}</strong>'
            f"<span>{caption}</span></div>"
        )
    st.markdown(f'<div class="tm-phase">{"".join(cards)}</div>', unsafe_allow_html=True)


def render_zero_state(readiness: ProviderReadiness) -> None:
    st.markdown(
        """
        <div class="tm-zero">
          <h3>What mathematical problem are you wrestling with?</h3>
          <p>Bring it exactly as you received it. ThinkMath will ask one precise question at a time—
          without rushing to reveal the answer.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if readiness.state != "ready":
        st.info(f"**{readiness.headline}.** {readiness.detail}")
    st.markdown("#### Or walk through a completed journey")


def render_demo_picker() -> str | None:
    selected: str | None = None
    columns = st.columns(len(DEMO_CATALOG))
    for column, (demo_id, item) in zip(columns, DEMO_CATALOG.items()):
        with column:
            with st.container(border=True):
                st.caption(str(item["level"]))
                st.markdown(f"**{item['label']}**")
                st.caption(str(item["problem"]))
                if st.button(
                    "Explore journey", key=f"demo-{demo_id}", use_container_width=True
                ):
                    selected = demo_id
    return selected


def render_thinking_map(view: ThinkingMap) -> None:
    st.subheader("Your Thinking Map")
    st.caption(
        "This—not the transcript—is the current source of truth for your reasoning."
    )
    st.progress(view.progress)
    _map_card("What you noticed", view.observations, "No observation established yet.")
    _map_card(
        "Candidate Seed", view.seed_candidates, "The underlying pattern is still open."
    )
    _map_card(
        "Direction Map",
        view.directions,
        "No mathematical direction has been confirmed.",
    )
    if view.claim_ledger:
        labels = {
            "verified": "✓ Verified",
            "promising": "◇ Promising",
            "needs_proof": "△ Needs proof",
            "corrected": "↺ Corrected",
        }
        with st.container(border=True):
            st.markdown('<div class="tm-map-label">Claim Check</div>', unsafe_allow_html=True)
            for claim in view.claim_ledger[-5:]:
                label = labels.get(claim.get("status", ""), "△ Review")
                st.markdown(f"**{label}:** {claim.get('text', '')}")
                if claim.get("reason"):
                    st.caption(claim["reason"])
    if view.phase_number >= int(SessionPhase.DIRECTIONS) or any(
        (view.setup, view.move, view.closure)
    ):
        _map_card(
            "Setup",
            (view.setup,) if view.setup else (),
            "How will you reframe the problem?",
        )
        _map_card(
            "Move",
            (view.move,) if view.move else (),
            "What exact operation will you perform?",
        )
        _map_card(
            "Closure",
            (view.closure,) if view.closure else (),
            "What forces the conclusion?",
        )
    st.markdown(
        f'<div class="tm-open-question"><div class="tm-map-label">What remains open</div>'
        f'<div class="tm-map-value">{html.escape(view.open_question)}</div></div>',
        unsafe_allow_html=True,
    )


def _map_card(label: str, values: tuple[str, ...], empty: str) -> None:
    with st.container(border=True):
        st.markdown(
            f'<div class="tm-map-label">{html.escape(label)}</div>',
            unsafe_allow_html=True,
        )
        if values:
            for value in values:
                st.markdown(value)
        else:
            st.caption(empty)


def render_structured_commentary(text: str) -> None:
    sections = split_commentary(text)
    for section in sections:
        with st.container(border=True):
            st.markdown(
                f'<div class="tm-section-title">{html.escape(section.title)}</div>',
                unsafe_allow_html=True,
            )
            st.markdown(section.body)


def render_transfer(asset: AdvaitianSession) -> None:
    title, challenge = transfer_challenge(asset)
    st.subheader(title)
    st.markdown(challenge)
    st.caption("Do not solve it yet. First name the familiar Seed in its new disguise.")


def render_passport(entries: list[dict[str, Any]], asset: AdvaitianSession) -> None:
    current = passport_entry(asset)
    combined = list(entries)
    if current and current not in combined:
        combined.append(current)
    st.subheader("Pattern Passport")
    st.caption(
        "A record of structures you have learned to recognise—not points or streaks."
    )
    if not combined:
        st.info("Complete a Setup–Move–Closure journey to add the first pattern.")
        return
    for index, entry in enumerate(combined, start=1):
        with st.container(border=True):
            st.markdown(f"**{index}. {entry['seed']}**")
            st.caption(entry["problem"])
            if entry.get("archetypes"):
                st.markdown(" · ".join(entry["archetypes"]))
    st.download_button(
        "Download my Pattern Passport",
        json.dumps(combined, ensure_ascii=False, indent=2),
        file_name="thinkmath-pattern-passport.json",
        mime="application/json",
        use_container_width=True,
    )
