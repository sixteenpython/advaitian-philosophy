# Chapter Template — Pillar 4 (The Art of CEP-Based Problem Design)

> **Purpose.** Single canonical chassis-file for all 9 chapters of Pillar 4. Pillar 4 has three chapter types, each with a distinct internal structure (essay-framework / case-study / exercises). All three chassis are defined below; every Pillar 4 chapter inherits whichever chassis its position calls for.
>
> **This template implements Blueprint §8.6 + §8.10 + §8.11 exactly.**

---

## Front Matter (YAML, for build pipeline & cross-reference graph)

```yaml
---
chapter: <int>                  # 1 through 9
pillar: 4
chapter_type: essay | case-study | exercises   # see §"Three Chassis" below
title: "<Chapter title>"
subtitle: "<one-line meta-principle, italicised in book>"
length_target_words: <see budget table below per chapter>
canonical_takeaway: "<one quotable sentence>"
status: outline | draft | review | locked
last_revised: YYYY-MM-DD
references_invoked: [Lockhart-pN, Tao-Ch-X, Polya-Part-N, Engel-Ch-Y, Zeitz-Ch-Z, IMO-YYYY-PN, Putnam-YYYY-AN, Joshi-Ch-W]
voice_register: lockhart-polemic | lockhart-constructive | tao-warm | polya-systematic | mixed
pillar3_cross_references: [pillar3-ch-N-§X]  # explicit hand-offs from Pillar 3
---
```

---

## Three Chassis Overview

| Chapter | Type | Chassis | Word target |
|---|---|---|---|
| 1 — *The Problem as Art Object* | essay | Chassis A (essay-framework) | 5,000–6,500 |
| 2 — *Anatomy of a Well-Designed Problem* | essay | Chassis A | 5,000–6,500 |
| 3 — *The 5-Step CEP Design Framework* | essay | Chassis A | 5,500–7,000 |
| 4 — *Case Studies 1–5 (Moderate CEP)* | case-study | **Chassis B** | 5,500–7,500 |
| 5 — *Case Studies 6–10 (Mid-difficulty CEP)* | case-study | Chassis B | 5,500–7,500 |
| 6 — *Case Studies 11–15 (High-mid CEP)* | case-study | Chassis B | 5,500–7,500 |
| 7 — *Case Studies 16–20 (High CEP)* | case-study | Chassis B | 5,500–7,500 |
| 8 — *Case Studies 21–25 (Extreme CEP, capstone IMO 1988 P6)* | case-study | Chassis B | 6,000–8,500 |
| 9 — *Design Your Own + The Ethics of Difficulty* | exercises | **Chassis C** | 6,000–7,500 |
| **Total Pillar 4** | | | **~50,000 words** |

---

## Chassis A — Essay-Framework Chapter (Chs. 1, 2, 3)

### §0 Opening — the chapter's central claim in vignette form (≈600–900 words)

**Voice register varies by chapter:**
- **Ch. 1:** Lockhart-polemic (the music-class-nightmare analogue; sharp, image-dense, declarative) — *do not directly quote Lockhart's musician opening; use a parallel device (e.g., culinary or architectural school) per `Cursor-Lockhart.md` §VI*
- **Ch. 2:** Tao-warm (the gold-nugget-style sustained metaphor, but inverted — designer rather than miner)
- **Ch. 3:** Mixed (Polya-systematic for the framework introduction; Tao-warm for the worked-example portions)

For Chs. 1-2: optionally pair with a named Indian protagonist vignette (per Pillar 3 convention) where it strengthens the argument; not mandatory if the chapter's polemic flow would be diluted.

### §1 The Argument (≈1,800–2,500 words)

**Voice register:** Chapter-specific (see §0 above).

The central argument of the chapter, developed in 3–4 sub-sections. For Ch. 1, this is the polemic case for problems-as-art-objects. For Ch. 2, this is the anatomical decomposition of a well-designed problem (CEP / archetype convergence / traps / statement craft). For Ch. 3, this is the 5-step CEP Design Framework laid out systematically.

**Required cross-references:**
- Ch. 1 must invoke Lockhart, Sawyer (in spirit; Sawyer text not in workspace), and at minimum one named Pillar 3 chapter (typically Ch. 1 *The Multidirectional Thesis* as the solver-side foil)
- Ch. 2 must invoke Tao's nine-strategy framework (`Cursor-Tao.md` §III) as the solver-side foil that the chapter's designer-side anatomy parallels
- Ch. 3 must invoke Polya's four-phase framework (`Cursor-Polya.md` §III) as the explicit ancestor of the 5-step CEP Design Framework, with the structural inversion mapping per `Cursor-Polya.md` §VI

### §2 Worked Demonstration (≈1,500–2,200 words)

One canonical problem worked through the chapter's analytical apparatus. For Ch. 1, this is a "designed problem read as art object" — the IMO 1988 P6 capstone read as designer's aesthetic statement (with full §8.10 case-study analysis deferred to Ch. 8). For Ch. 2, this is the anatomical dissection of one Moderate-tier problem (e.g., IMO 1959 P1). For Ch. 3, this is one author-designed problem walked through all 5 design steps in real time.

### §3 The Counter-Argument (≈600–900 words)

**Voice register:** Lockhart-style SIMPLICIO/SALVIATI dialogue (per `Cursor-Lockhart.md` §III Sample 5) for Chs. 1 and 9; for Chs. 2 and 3, a direct prose treatment of objections.

Anticipated reader objection, voiced fairly, then engaged. This section is non-negotiable — Pillar 4 makes strong philosophical claims and must be willing to face the strongest objections to them.

### §4 Bridge to the Next Chapter (≈300–500 words)

**Voice register:** Joshi-discursive — explicit pedagogical pointing.

Three things this section must do:
1. Re-state the chapter's central argument in one sentence.
2. Name the next chapter's argument and motivate why it is the natural next step.
3. For Ch. 3 specifically: forward-reference the 25-case slate (Chs. 4–8) explicitly — flag that the next five chapters will *apply* the 5-step framework retrospectively to 25 designed problems.

---

## Chassis B — Case-Study Chapter (Chs. 4, 5, 6, 7, 8)

### §0 Chapter Opening (≈400–600 words)

**Voice register:** Tao-warm + chapter-tier-appropriate epigraph (per `Cursor-Tao.md` §IV Sample 4).

A chapter-level frame for the 5 cases: what unifies them at this tier? What design moves recur across this tier's CEP family? Closes with a one-line preview of the 5 cases the chapter will study.

### §1–§5 The Five Case Studies (≈800–1,200 words each, per Blueprint §8.10)

Each case study follows the canonical §8.10 sub-template **exactly**:

```
## Case Study N — [Problem title or one-line gist]

**Source.** [IMO YYYY, Problem K | Putnam YYYY, A/B-N | Engel Ch. X, Ex. Y | Joshi Ch. W]
**CEP.** [The beautiful mathematical object at the centre]
**Archetypes.** [#X + #Y + #Z]  ← three-archetype standard; some Moderate cases may use only two
**Difficulty.** Tier 3-low | Tier 3-mid | Tier 3-high | Tier 4-low | Tier 4-mid | Tier 4-high
**Verification source.** [Cursor-IMO.md line N | Engel Ch. X Ex. Y | Cursor-Zeitz.md §Z]

### Problem statement
(verbatim, properly cited)

### The Designer's Architecture
*The CEP unmasked.* What did the designer want the solver to discover? Be specific — name the object, the identity, or the structural truth that *is* the problem's reward.

*The archetype convergence.* Which archetypes were chosen and why these? Show — preferably with a §7.6-style convergence diagram for the 3-archetype cases — how the chosen archetypes converge to the CEP. The diagram is required for all 3-archetype cases (Hard and Extreme tiers); optional for 2-archetype Moderate cases.

*The traps planted.* What brute paths look plausible but fail? Each trap should be named (e.g., "the trigonometric trap," "the brute-substitution trap"). Two to three traps per case.

*The statement-craft.* What does the surface statement reveal? What does it conceal? What single word or phrase in the statement is the most consequential design choice? (This is the most overlooked aspect of problem design.)

### The Reader's Re-Solution
A clean Pillar-2-style six-point commentary (≤ 500 words). Six bullet points, in order: Given · Find · Strategy · Stage 1 (first archetype) · Stage 2 (second archetype) · Stage 3 / CEP (third archetype, if 3-archetype case; or Convergence + Answer if 2-archetype). Final answer in `$\boxed{\cdot}$`.

### Lessons for Problem Designers
Two or three bullet-point design moves the reader could lift and apply to their own problem-design work. These are the chapter's pedagogical *delta* — what does the reader walk away knowing how to do?
```

### §6 Chapter Bridge to N+1 (≈300–500 words)

**Voice register:** Joshi-discursive.

Same three duties as Chassis A §4. For Ch. 8 specifically: the bridge looks forward to Ch. 9 (Design Your Own) and frames the 25 case studies as *training data* for the design exercises about to come.

---

## Chassis C — Exercises + Closing Chapter (Ch. 9)

### §0 Chapter Opening (≈500–700 words)

**Voice register:** Mixed (Lockhart-constructive for the framing; Tao-reflective for the looking-back-on-the-craft register, per `Cursor-Tao.md` §IV Sample 1 register).

Frames the chapter as the moment of *inversion completion*: the reader who began Pillar 4 as a solver is now ready to attempt the designer's role. Brief acknowledgement that design is harder than solving — and that the three exercises in this chapter are deliberately graded to make the inversion experienceable rather than overwhelming.

### §1 Design Exercise 1 — Given CEP: *the prime 7* (≈1,000–1,400 words, per Blueprint §8.11)

The reader is given the CEP and asked to design a problem around it. The chapter then walks through *one such design* (Blueprint §8.11 sample: "Find all integers $n$ such that $n^2 + n + 7$ is a perfect square"). The walkthrough follows the 5-step framework from Ch. 3 exactly:
1. Select the CEP — *the prime 7* (given)
2. Select the Archetypes — *#14 Parity/Mod + #11 Existence* (target: JEE Adv level, 2 archetypes)
3. Design the Convergence — how does the solver get from the surface to "7 is the answer"?
4. Plant the Traps — which brute approaches will fail instructively?
5. Craft the Statement — surface text that conceals the interior

### §2 Design Exercise 2 — Given CEP: *the golden ratio φ* (≈1,000–1,400 words)

Same 5-step structure; target: RMO level, 3 archetypes (Blueprint §8.11 sample: a Fibonacci-flavoured recurrence problem with concealed φ; archetypes #18 + #4 + #16).

### §3 Design Exercise 3 — Given CEP: *0 as unique solution* (≈1,000–1,400 words)

Same 5-step structure; target: IMO-shortlist level, 3 archetypes (Blueprint §8.11 sample: a Diophantine equation whose only solution is the trivial one; archetypes #18 (infinite descent) + #14 + #1).

### §4 The Designer's Rubric (≈400–600 words, per Blueprint §8.11 close)

The five-criterion rubric for self-assessing a designed problem:
1. **Cleanness of surface statement.** Does the statement read naturally? Is every word load-bearing?
2. **Depth of CEP.** Is the CEP genuinely beautiful, or merely tricky?
3. **Trap quality.** Are the traps instructive or merely punishing?
4. **Archetype non-obviousness.** Could a strong solver guess the archetype profile from the surface? If yes, the design has leaked.
5. **Pedagogical lift.** What does the solver learn that they did not know before? (This is the highest criterion.)

Presented as a self-assessment grid the reader can apply to their own designed problem.

### §5 The Ethics of Difficulty (≈1,200–1,800 words)

**Voice register:** Lockhart-constructive (per `Cursor-Lockhart.md` §III Sample 4: *"Mathematics is the art of explanation"*) + Tao-reflective close.

The chapter — and the pillar — closes on the ethical distinction between *hard-and-deep* and *hard-and-arbitrary*. The first is the designer's goal; the second is the failure mode every problem-setter must guard against. Names the specific cultural pathologies in olympiad culture (the cult of difficulty, the worship of obscurity, the conflation of cleverness with depth). Closes with the constructive vision: problems as cultural artifacts, the designer as artist with responsibilities, the multi-generational lineage from Polya to Tao that Pillar 4 inherits and tries to extend.

### §6 Pillar Bridge (≈300–500 words)

Looks forward to Pillar 5 (Mathematical Gems) as the natural complement: where Pillar 4 has taught problem-design, Pillar 5 will showcase the tools and named theorems that designed problems most often deploy.

---

## Voice Register Calibration

Pillar 4 has the **richest voice register stack** of any pillar in the book. Per `Cursor-Tao.md` §VII:

| Register | Source | Use in Pillar 4 |
|---|---|---|
| **Lockhart-polemic** | Lockhart Part I (Lamentation) | Ch. 1 §0–§1; Ch. 9 §5 (Ethics of Difficulty) |
| **Lockhart-constructive** | Lockhart Part II (Exultation) + SIMPLICIO/SALVIATI | Ch. 1 §3 (Counter-Argument); Ch. 9 §0 |
| **Tao-warm** | Tao Preface + worked examples | Ch. 2 §0; Chs. 4–8 chapter openings; Ch. 9 §0 |
| **Tao-think-aloud** | Tao Ch. 1 + worked solutions | Chs. 4–8 case-study Re-Solutions (§N.2 of each case) |
| **Polya-systematic** | Polya Part I (four-phase) | Ch. 3 §1 (framework setup); Ch. 9 §1–§3 (design exercises) |
| **Polya-pattern** | Polya Part III (heuristic-dictionary entries; cf. `Cursor-Polya.md` §IV Sample 1) | Ch. 3 §2 (worked demonstration); Ch. 8 §5 case (the IMO 1988 P6 capstone Designer's Architecture) |
| **Zeitz-warm** | Zeitz preface + Ch. 2 | Ch. 1 §0 vignette portion; Chs. 4–8 chapter openings (where Tao-warm needs warmer counterpart) |
| **Engel-terse** | Engel Ch. 1–14 worked examples | Chs. 4–8 case-study problem statements and verified solutions |

The eight-register mix is the discipline that prevents Pillar 4 from collapsing into either pure polemic (Lockhart-only failure mode) or pure technique (Engel-only failure mode).

---

## Canonical Constructs (inherited from Pillar 3 + Pillar 4 additions)

### Inherited from Pillar 3

- **Convergence Diagram (§7.6)** — required for all 3-archetype case studies (Hard and Extreme tiers); same ASCII convention as Pillar 3
- **First-Minute Protocol (§7.7)** — invoked in Ch. 2 §2 (anatomy demonstration) and Ch. 3 §2 (design framework demonstration); inverted as the "First-Five-Minutes Protocol for Problem Design" in Ch. 3
- **Escape-Hatch Architecture (§7.8)** — referenced in Ch. 9 §5 (Ethics of Difficulty) as the safety net the designer owes the solver

### New to Pillar 4

- **The CEP Box** — a `\begin{cep}...\end{cep}` LaTeX environment that names the Central Elegant Point of a case study in a single boxed line, placed at the top of each case study's Designer's Architecture section
- **The Trap Catalogue** — each case study names 2–3 traps with explicit short-titles (e.g., "the trigonometric trap"); the trap catalogue is then cross-referenced in Ch. 9 §4 (Designer's Rubric)
- **The Design Step Tag** — `[Step 1]`, `[Step 2]`, ... `[Step 5]` inline tags used throughout Ch. 3 §2 and Ch. 9 §1–§3 to make the 5-step framework's application traceable

---

## LaTeX Environments (Pillar 4 additions)

Inherited from Pillars 2 + 3, plus:

- `\begin{cep}` / `\end{cep}` — the CEP Box (NEW for Pillar 4)
- `\begin{trap}[short-name]` / `\end{trap}` — a single named trap within a case study's Designer's Architecture
- `\begin{designstep}[N]` / `\end{designstep}` — wraps each of the 5 steps in a design demonstration
- `\begin{rubric}` / `\end{rubric}` — the Designer's Rubric (Ch. 9 §4)
- `\begin{dialogue}[SIMPLICIO|SALVIATI]` / `\end{dialogue}` — for the Lockhart-style dialogue passages (Ch. 1 §3, Ch. 9 §0)

Boxed final answers continue using `$\boxed{\cdot}$` as in Pillars 2–3.

---

## Honesty & Citation Rules (carried over from Pillars 2–3)

1. Every case-study problem must cite its source verbatim (IMO year + problem number, or Putnam citation, or Engel/Zeitz/Joshi chapter + example number).
2. Every claimed CEP and solution path must be independently verified via the relevant Cursor reference file (`Cursor-IMO.md`, `Cursor-Engel.md`, `Cursor-Zeitz.md`, `Cursor-Joshi.md`). The verification anchor goes in the case study's front matter (`Verification source.` line).
3. Polya verbatim quotes: page-number-footnoted per `Cursor-Polya.md` §VIII; quotes verified via visual transcription from PDF rasters at `my_references/polya-pages/`.
4. Where an open item exists, flag explicitly in-prose: *"⚠ Open item — Anand sign-off pending. Current best candidate: [...]"* (Pillar 3 convention).
5. Vignette protagonists are *invented* and footnoted as such on first introduction per chapter (Pillar 3 convention).
6. ASCII-only for diagrams (Locked Decision #4, inherited).

---

*End of Pillar 4 chapter-template.md.*
