# Chapter Template — Pillar 3 (The Science of Multidirectional Solving)

> **Purpose.** Single canonical chassis for all 8 chapters of Pillar 3. Every chapter inherits this skeleton. Diverge from the section list only with explicit reason and Anand's sign-off — drift compounds across 8 chapters and silently rots the pillar.
>
> **This template implements Blueprint §7.10 exactly.**

---

## Front Matter (YAML, for build pipeline & cross-reference graph)

```yaml
---
chapter: <int>            # 1 through 8
pillar: 3
title: "<Chapter title>"
subtitle: "<one-line meta-principle, italicised in book>"
length_target_words: 6250  # default; Ch. 3 and Ch. 6 may run to 8750
canonical_takeaway: "<one quotable sentence>"
status: outline | draft | review | locked
last_revised: YYYY-MM-DD
references_invoked: [Engel-ch-X, Zeitz-ch-Y, Joshi-ch-Z, IMO-YYYY-PN, Putnam-YYYY-AN]
canonical_constructs_used: [convergence-diagram | first-minute-protocol | escape-hatch]
---
```

---

## Section Map (canonical for all 8 Pillar 3 chapters, per Blueprint §7.10)

### §0 Opening Vignette  (≈400–600 words)

**Voice register:** Zeitz-warm-conversational (per Blueprint mapping) + Joshi-grounded (Indian context).

A vivid, **Indian-context, named-protagonist** vignette that embodies the chapter's thesis viscerally. Two protagonists where appropriate (one struggling, one succeeding — to dramatise the cognitive shift). Specific institution (IIT Madras, IIT Bombay, IIT Kanpur, IIT Delhi, ISI Kolkata, ISI Bangalore, CMI, Chennai Math Camp, Bengaluru music college, etc.) and concrete situation. Closes with a single-sentence naming of the chapter's pattern.

### §1 The Pattern  (≈1,400–1,800 words)

**Voice register:** Engel-terse for definitions + Polya/Zeitz for cognitive framing.

#### §1.1 The structural model

State the chapter's central pattern. Include the §7.6 convergence diagram (ASCII) where relevant — every Pillar 3 chapter uses the diagram in at least one place. The 2-archetype diagram or 3-archetype diagram appears with annotated nodes labelled by the chapter's specific archetypes.

#### §1.2 The empirical case

Why does this pattern matter? Cite *real* problem distributions where possible (IMO problem analyses, Putnam catalogues, Engel's chapter structure as an implicit empirical map of multi-archetype frequencies). Avoid hand-waving — give numbers or specific cited evidence.

#### §1.3 The historical case

Where in the problem-solving literature did this pattern first appear? Polya 1945? Engel 1998? Zeitz 2017? Trace one strong intellectual ancestry per chapter.

### §2 Worked Examples  (≈2,200–3,000 words; typically 2–3 examples)

**Voice register:** Engel-terse for the worked solution + Polya for the post-solution commentary.

Each worked example follows this internal structure:

```
**Worked Example N — [One-line gist]**

*Source.* [Engel Ch. X / Zeitz Ex Y.Z / Joshi Ch. W / IMO YYYY PN — verbatim citation]
*Archetypes invoked.* [#a + #b (+ #c if 3-archetype)]
*Convergence type.* [2-archetype convergence | 3-archetype convergence]

**Problem statement.** (verbatim, properly cited)

**Convergence diagram.**
[ASCII §7.6 diagram with nodes labelled by this problem's specific archetype applications]

**Solution walkthrough.** 
- Stage 1: Application of archetype #a → intermediate result A'
- Stage 2: Application of archetype #b → intermediate result B'  
- Convergence: A' + B' → CEP
- Final answer: [boxed]

**Commentary — why the convergence matters.** (1–2 paragraphs)
- What does the convergence diagram reveal that a linear proof would conceal?
- What would have gone wrong if the solver had used only #a or only #b?
- How does this example connect to the chapter's central thesis?
```

### §3 The Trap  (≈700–1,000 words)

**Voice register:** Polya/Zeitz-mentor — direct, anti-pedantic, "I have seen students do this" honest.

One **specific failure mode** that solvers fall into when this chapter's pattern is mis-applied. Diagnose the failure mode (what *looks* right but isn't). Then **the recovery**: which of the three Escape-Hatch moves (Archetype Nudge, Direction Map, Pivot Shadow) recovers, and why? Brief worked illustration of the failure-then-recovery sequence.

### §4 Practice Problems  (≈900–1,300 words; 4–6 problems)

**Voice register:** Engel-encyclopedic — problem-statement only, with hints in a separate appendix-style block.

4–6 problems graded **2-archetype → 3-archetype** in difficulty. Each problem includes:
- Problem statement (verbatim, properly cited)
- Source citation
- **Archetypes flagged in italics** (so reader can self-check the First-Minute Protocol output against the actual archetype profile)
- Hint (1 sentence, sealed in a `\begin{hint}...\end{hint}` LaTeX environment for the typeset book; in markdown, render as a *Hint* paragraph below the problem)
- For final 1-2 problems: a "stretch" challenge with no hint

### §5 Bridge to Chapter N+1  (≈300–500 words)

**Voice register:** Joshi-discursive — explicit pedagogical pointing.

Three things this section must do:
1. Re-state this chapter's central pattern in one sentence
2. Name the next chapter's pattern and motivate why it is the natural next step
3. One forward-reference to the specific worked example in the next chapter where this chapter's archetype reappears

---

## Voice Register Calibration (per Blueprint §7.10)

Pillar 3 chapters are **denser and more discursive** than Pillar 2 chapters — but they must NOT degenerate into pedagogical hand-waving. Maintain the discipline by mixing three voice registers throughout:

| Register | Source | Use in Pillar 3 |
|---|---|---|
| **Zeitz-warm** | Zeitz preface + Ch. 2 | §0 Opening Vignette, §3 The Trap |
| **Engel-terse** | Engel Ch. 1–14 worked examples | §2 Worked Examples (the solution itself) |
| **Polya/Joshi-discursive** | Polya 1945 + Joshi voice samples | §1 The Pattern (cognitive framing), §5 Bridge |

The three-register mix prevents both Pillar-3-becomes-textbook-dry and Pillar-3-becomes-self-help-fluff.

---

## Canonical Constructs (per Blueprint §7.6–§7.8)

Every Pillar 3 chapter is expected to invoke at least one of the three canonical constructs:

### Construct 1: The Convergence Diagram (§7.6) — ASCII

```
            ┌─────────────────┐
            │ Problem statement │
            └────────┬──────────┘
                     │
       ┌─────────────┴──────────────┐
       │                            │
       ▼                            ▼
┌────────────────┐         ┌────────────────────┐
│  Archetype A   │         │   Archetype B      │
│   applied      │         │     applied        │
│  generates     │         │   generates        │
│  intermediate  │         │   intermediate     │
│   result A'    │         │    result B'       │
└──────┬─────────┘         └─────────┬──────────┘
       │                             │
       └────────────┬────────────────┘
                    ▼
            ┌───────────────┐
            │  Convergence  │
            │   (the CEP)   │
            └───────┬───────┘
                    │
                    ▼
              ┌──────────┐
              │  Answer  │
              └──────────┘
```

**Three-archetype variant** adds a second convergence node downstream (cf. Blueprint §7.6 figure for IMO 1988 P6 territory).

**Rendering rule.** ASCII only (per locked Decision #4). Use box-drawing characters: ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼ ▼ ▲.

### Construct 2: The First-Minute Protocol (§7.7) — five-step checklist

```
+----+-----------------------------------+---------------------------------------+
| #  | Question                          | Output (scratchpad)                   |
+----+-----------------------------------+---------------------------------------+
| 1  | What is the *given*?              | Bullet list, ≤ 5 items   (15 s)       |
| 2  | What is the *find*?               | One sentence + answer-type (5 s)      |
| 3  | Which archetypes are likely?      | List of 1–3 archetype #s   (20 s)     |
| 4  | What is the candidate CEP?        | A guess, even if uncertain (10 s)     |
| 5  | What is the *brute path*?         | One line — the path I won't take      |
|    |                                   |   (10 s)                              |
+----+-----------------------------------+---------------------------------------+
                                          Total: 60 seconds
```

**Usage rule.** Every chapter from Ch. 4 onward should show at least one worked example with an explicit First-Minute Protocol scratchpad reproduced verbatim.

### Construct 3: The Escape-Hatch Architecture (§7.8) — three recovery moves

| Move | When to use | What to do |
|---|---|---|
| **Archetype Nudge** | "Wrong archetype" suspicion | Re-run First-Minute Protocol Step 3 with a different short-list |
| **Direction Map** | "Right archetypes, wrong order" suspicion | Draw the §7.6 diagram explicitly; label what each intermediate result *should let you say* |
| **Pivot Shadow** | "Brute path is half-correct" suspicion | Continue the brute computation just enough to see the structure of the elegant pivot |

**Usage rule.** Ch. 7 develops all three moves in detail. Chs. 1–6 each may invoke one move where it organically helps recovery in §3 The Trap.

---

## LaTeX Environments (Pillar 3 specific)

Inherited from Pillar 2 + added:

- `\begin{definition}` / `\end{definition}` — formal definitions
- `\begin{theorem}[Optional Name]` / `\end{theorem}` — named theorems  
- `\begin{example}` / `\end{example}` — worked examples
- `\begin{hint}` / `\end{hint}` — practice-problem hints
- `\begin{convergence}` / `\end{convergence}` — **NEW for Pillar 3**: wraps a convergence diagram + its archetype-node labels
- `\begin{protocol}` / `\end{protocol}` — **NEW for Pillar 3**: wraps a First-Minute Protocol scratchpad
- `\begin{escape}[Archetype Nudge | Direction Map | Pivot Shadow]` / `\end{escape}` — **NEW for Pillar 3**: wraps an Escape-Hatch move invocation

Boxed final answers continue using `$\boxed{\cdot}$` as in Pillar 2.

---

## Length Budget Discipline

| Section | Target words | Hard cap |
|---|---|---|
| §0 Opening Vignette | 400–600 | 700 |
| §1 The Pattern | 1,400–1,800 | 2,000 |
| §2 Worked Examples | 2,200–3,000 | 3,300 |
| §3 The Trap | 700–1,000 | 1,200 |
| §4 Practice Problems | 900–1,300 | 1,500 |
| §5 Bridge | 300–500 | 600 |
| **Total** | **5,900–8,200** | **9,300** |

Chapters typically land at **6,250–8,750 words** (Blueprint §7.4 budget). Ch. 6 (Worked Case Studies — the pillar's centre of gravity) is the exception that may run to 10,000 words.

---

## Honesty & Citation Rules (carried over from Pillar 2)

1. Every problem must cite its source verbatim. If pulled from Engel/Zeitz/Joshi, cite chapter and example/problem number. If from IMO/Putnam/etc., cite year and problem number. If newly-constructed by the author, label as *"Author's construction, after [archetype/source]"*.
2. Every claimed answer must be independently verified (per Pillar 2 audit discipline). The locked-problems file `pillar3-problems-locked.md` is the verification record.
3. Where an open item exists (e.g., a problem citation TBD per Pillar 3 outline-and-slate v0.2), flag it explicitly in-prose: *"⚠ Open item — Anand sign-off pending. Current best candidate: [...]"*.
4. ASCII-only for diagrams (Locked Decision #4). No TikZ, no Unicode math beyond what the markdown renderer + LaTeX environments handle naturally.

---

*End of Pillar 3 chapter-template.md.*
