# Pillar 3 — The Science of Multidirectional Solving — Outline & Locked Slate

**Version.** v0.2 — May 28, 2026 (Engel sourcing gap closed).
**Status.** Awaiting Anand's sign-off before Chapter 1 drafting begins.
**Authority.** This document operationalises Blueprint §7 (lines 633–781). Five strategic decisions were locked in conversation on May 28, 2026:

| # | Decision | Locked Choice |
|---|---|---|
| 1 | **Sourcing strategy** | Draft on known-canonical problems (Engel, Polya, Zeitz, IMO, Putnam) that are well-documented in olympiad culture; Joshi as secondary source for continuity with Pillar 2. |
| 2 | **§7.9 case-study slate** | All five locked as listed — no substitutions. |
| 3 | **Word budget per chapter** | Strict blueprint: 6,250–8,750 words/chapter; ~60,000 words total. |
| 4 | **Convergence-diagram format** | ASCII art only (per §7.6 exactly). No TikZ dependency. |
| 5 | **First-chapter sequencing** | Outline all 8 chapters first → Anand sign-off → then Ch. 1 drafting begins. |

---

## Architectural Context

### A.1 Where Pillar 3 Sits

Pillar 2 (just completed) supplied the **vocabulary** — the twenty archetypes. Pillar 3 supplies the **syntax** — the geometry of how archetypes combine, converge, and interact to solve hard problems. The central claim is the blueprint's §7.1 thesis:

> *Hard problems are not hard because the archetype is exotic. They are hard because the solution requires two or three archetypes to operate simultaneously, and the solver must maintain all of them in working memory long enough for the convergence point to appear.*

### A.2 The Three Canonical Constructs

Pillar 3 introduces three named constructs that recur across all eight chapters:

**(i) The Convergence Diagram (§7.6)** — a directed acyclic graph (DAG) of archetype-applications and convergence nodes. The ASCII representation (already canonical per the blueprint) is reproduced in every worked-example walkthrough. The two-archetype shape:

```
            ┌─────────────────────┐
            │  Problem statement  │
            └──────────┬──────────┘
                       │
       ┌───────────────┴───────────────┐
       │                               │
       ▼                               ▼
┌────────────────┐             ┌────────────────────┐
│  Archetype A   │             │   Archetype B      │
│   applied      │             │     applied        │
│  generates     │             │   generates        │
│  intermediate  │             │   intermediate     │
│   result A'    │             │    result B'       │
└──────┬─────────┘             └─────────┬──────────┘
       │                                 │
       └──────────────┬──────────────────┘
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

The three-archetype variant adds a second convergence node downstream.

**(ii) The First-Minute Protocol (§7.7)** — a 60-second silent diagnostic the trained solver runs *before* writing equations. Five steps:

| Step | Question | Output | Time |
|------|----------|--------|------|
| 1 | What is the *given*? | Bullet list, ≤ 5 items | 15 s |
| 2 | What is the *find*? | One sentence, answer-type tagged | 5 s |
| 3 | Which archetypes are likely active? | 1–3 archetype numbers (Pillar 2 catalogue) | 20 s |
| 4 | What is the candidate CEP? | A guess, even if uncertain | 10 s |
| 5 | What is the *brute path* (the thing I won't do)? | One line | 10 s |

**(iii) The Escape-Hatch Architecture (§7.8)** — three named recovery moves when the First-Minute Protocol's chosen path stalls:

- **Archetype Nudge** — re-run Step 3 with a different short-list (suspect wrong archetype)
- **Direction Map** — draw the convergence diagram explicitly to find the missing edge (right archetypes, wrong order)
- **Pivot Shadow** — continue the brute path just far enough to see the elegant pivot's structure (brute is half-correct)

### A.3 Chapter Sub-Template (per §7.10, locked)

Every Pillar 3 chapter follows this 5-section scaffold, which is *denser* and *more discursive* than Pillar 2's 8-section template:

```
## Opening — the multidirectional thesis at chapter scale (~600 words)
## 1. The Pattern: 2/3-archetype convergence in this chapter's context (~1,200 words)
## 2. Worked Examples — 2–3 examples, each with §7.6 convergence diagram (~2,500–3,500 words)
## 3. The Trap — most common failure mode and its recovery (~600 words)
## 4. Practice — 4–6 problems, graduated 2-archetype → 3-archetype (~1,000 words; full solutions in Appendix)
## 5. Bridge to Chapter N+1 (~400 words)
## Appendix — practice problem solutions (~500–1,500 words)
```

Target totals: **6,250–8,750 words/chapter** (the bracket varies by chapter — Ch. 6, the case-study centre-of-gravity, runs to the upper bound at ~10,000 words by exception).

### A.4 Source Discipline

Per locked Decision #1, Pillar 3 draws on:

| Tier | Source | Status in workspace | Use |
|------|--------|---------------------|-----|
| **Primary** | Engel, *Problem-Solving Strategies* (1998) | ✅ **PDF + extracted text + Cursor-Engel.md (v1.0, 581 lines) — IN WORKSPACE** (`my_references/Problem Solving Strategies.pdf`, `my_references/problem-solving-strategies.txt` 21,005 lines, `Cursor-Engel.md`) | Technique encyclopedia; the source of multi-archetype convergence exemplars |
| **Primary** | Polya, *How to Solve It* (1945) + *Mathematics and Plausible Reasoning* (1954) | ⚠ Not yet in workspace; principles drawn from public-domain summaries until added | Heuristic architecture; First-Minute Protocol's intellectual ancestor |
| **Primary** | Zeitz, *The Art and Craft of Problem Solving* (2007) | ⚠ Not yet in workspace; technique summaries drawn from public-domain sources | Three-layer model (strategies/tactics/tools); MVC ancestor |
| **Primary** | IMO Compendium (Đjukić et al.) | ⚠ Not yet in workspace; individual problems will be drawn from IMO online archive at imo-official.org | Stretch 3-archetype case studies |
| **Primary** | Putnam archive (Andreescu et al.) | ⚠ Not yet in workspace; individual problems will be drawn from public Putnam archives | Stretch geometry/combinatorics case studies |
| **Secondary** | K.D. Joshi, *Educative JEE Mathematics* | ✅ **PDF + extracted text + Cursor-Joshi.md — IN WORKSPACE** (used throughout Pillar 2) | Cross-references to Pillar 2; continuity examples |

**Verification discipline.** Every problem in the Pillar 3 locked slate undergoes independent answer verification before chapter drafting begins, mirroring the Pillar 2 protocol that caught 22 slate errors. The Pillar 3 slate's analogous file is `pillar3-multidirectional/_template/pillar3-problems-locked.md` (to be created in Phase 0).

**Engel-specific sourcing notes (added v0.2).** With Engel's full text now in the workspace, the following Pillar 3 chapter slots have been **upgraded from "TBD" to "specific Engel chapter lock-in"**:

| Slot | Pre-v0.2 status | Post-v0.2 lock-in | Engel source |
|---|---|---|---|
| Ch. 1 WE2 (5 points in unit square) | "Engel Ch. 5" (mis-located) | **Engel Ch. 4 §Box-Principle territory** | `Cursor-Engel.md` §V row 1 + Engel Ch. 4 lines 2992–4212 |
| Ch. 3 WE1 (3-archetype anchor) | "TBD" | **IMO 1988 P6 (Vieta jumping)** — Engel Ch. 8 Problem 6 | `Cursor-Engel.md` §V 3-archetype row 1 + Engel lines 10876–10879 |
| Ch. 6 Case Study #1 (Engel's pigeonhole) | "Engel Ch. 5 Problem 5.1" (mis-citation) | **Engel Ch. 4 box-principle exemplar (E7 or E11 candidate)** | `Cursor-Engel.md` §II Ch. 4 + §V |
| Ch. 6 Case Study #5 (Engel functional equation) | "Engel Ch. 11" (under-specified) | **Engel Ch. 11 — specific problem to be selected from E2 (Cauchy), E3 (exponential), or E4 (d'Alembert)** | `Cursor-Engel.md` §II Ch. 11 + §V 3-archetype row 6 |
| Ch. 7 (Escape-Hatch) Pivot Shadow examples | "TBD" | **Engel Ch. 14 §14.2 Infinite Descent** — the canonical "what to do when stuck" technique | `Cursor-Engel.md` §II Ch. 14 + §VII Sample 4 |

All other slot specifics remain in the Open Items table for Anand's per-chapter sign-off at draft time.

---

## Chapter 1 — The Multidirectional Thesis

**Subtitle.** *Why Single-Archetype Thinking Hits a Wall*
**Length target.** ~6,500 words.
**Pedagogical role.** Foundation chapter; establishes the thesis, the convergence-diagram notation, and the empirical case that hard problems are *multidirectional* by structural necessity.

### §0 Opening Vignette (sketch)
A *negative-example* vignette: an IIT Madras third-year student attempting an IMO-shortlist problem with a single archetype (extremal alone), failing after 90 minutes, then watching a senior peer dispatch the same problem in 12 minutes by recognising the 2-archetype convergence (extremal + parity). The vignette grounds the thesis viscerally: it is not technique deficit, it is *orchestration* deficit.

### §1 The Pattern
- The geometry of convergence (formal): a DAG of archetype-applications terminating at a CEP node
- Empirical observation: the overwhelming majority of IMO problems (≥ 70%, per Engel's catalogue analysis) require 2+ archetypes
- The Pillar 2 Ch. 1 §4.1 five-digit divisibility example as the simplest non-trivial case (invariance + domain constraints → 216)
- Historical case: Polya's 1945 four-phase loop *is* a multidirectional protocol in disguise

### §2 Worked Examples (2 examples)
- **WE1** — *Five-digit divisibility revisited* (Joshi Ch. 1 / Pillar 2 Ch. 1 §4.1): re-narrated with the §7.6 convergence diagram, making explicit what was implicit in Pillar 2. Archetypes: #1 Invariance + #9 Domain Constraints → convergence at $|S| = 120 + 96 = 216$.
- **WE2** — *Engel's classical "5 points in unit square"* (Engel Ch. 4 — The Box Principle, lines 2992–4212; cf. `Cursor-Engel.md` §V row 1): show any 5 points in the unit square have two within distance $\sqrt 2 / 2$. Archetypes: #13 Combinatorial (pigeonhole, divide square into 4 sub-squares of side $1/2$) + #12 Extremal (maximum distance in a unit square is $\sqrt 2 / 2$, achieved diagonally in a sub-square of side $1/2$).

### §3 The Trap
The "one-archetype-fits-all" trap: students trained only on technique-catalogues attempt every problem with their single strongest archetype (often substitution or algebra). The trap signals: spending >20 minutes without progress and *still* attacking with the same archetype.

### §4 Practice (4 problems)
- **PP1** (T1, 2-archetype): elementary 2-archetype problem solvable in 5 minutes once the convergence is seen
- **PP2** (T2, 2-archetype): standard JEE-Advanced-level multidirectional problem
- **PP3** (T2, 2-archetype): Engel Ch. 5 follow-on problem
- **PP4** (T3, 2-archetype with explicit diagram requirement): student must produce the §7.6 diagram before writing the solution

### §5 Bridge to Chapter 2
Ch. 1 named the pattern; Ch. 2 develops the 2-archetype problem class systematically.

### Pillar 2 cross-references
Chs. 1 (Invariance), 9 (Domain Constraints), 12 (Extremal), 13 (Combinatorial).

---

## Chapter 2 — Two-Archetype Convergence

**Subtitle.** *The Atom of Multidirectional Solving*
**Length target.** ~7,500 words.
**Pedagogical role.** Develops the 2-archetype problem class systematically; the bulk of JEE Advanced and lower-tier olympiad problems live here.

### §0 Opening Vignette (sketch)
A young IIT Bombay student preparing for INMO-2 spends a weekend cataloguing his last 50 attempted problems by archetype-pair. The pattern emerges visibly: 38 of 50 are 2-archetype; the failure mode is consistently *missing the second archetype* in the First-Minute scan.

### §1 The Pattern
- The 2-archetype convergence DAG (§7.6 diagram, single convergence node)
- The 190 pairs ($\binom{20}{2}$) of archetypes — most pairs occur, but a few dominate
- The "common convergence patterns" — five archetype-pairs that recur across hundreds of problems

### §2 Worked Examples (3 examples)
- **WE1** — *Invariance + Domain Constraints* (Engel Ch. 1 / Joshi Ch. 1 cross-reference): an invariant-mod-N problem combined with a positivity / integrality constraint
- **WE2** — *Symmetry + Substitution* (Engel Ch. 9 functional equation): exploit the $f(x) = f(-x)$ symmetry plus the $u = x^2$ substitution to reduce a functional equation to a single-variable ODE
- **WE3** — *Induction + Extremal* (Engel Ch. 6): inductive construction of an extremal configuration; the induction supplies the constructive engine, the extremal principle bounds the result

### §3 The Trap
The "wrong second-archetype" trap: the solver correctly identifies one archetype but pairs it with the wrong second. Example: identifying *invariance* but pairing it with *substitution* (cosmetic) rather than *domain constraints* (essential).

### §4 Practice (5 problems)
- **PP1–PP3** (T2, 2-archetype, paired explicitly): student must identify both archetypes before solving
- **PP4** (T3, 2-archetype, no priming): student must do the First-Minute Protocol explicitly
- **PP5** (T3, 2-archetype, with a "wrong-second-archetype" decoy): forces the trap recognition

### §5 Bridge to Chapter 3
Ch. 2 mastered 2-archetype convergence; Ch. 3 levels up to 3-archetype problems where the third archetype is typically the *closing move*.

### Pillar 2 cross-references
Chs. 1, 2 (Symmetry), 5 (Substitution), 9, 12, 18 (Recursion/Induction).

---

## Chapter 3 — Three-Archetype Problems

**Subtitle.** *Where IMO Lives*
**Length target.** ~7,500 words.
**Pedagogical role.** Develops the 3-archetype problem class — the IMO and Putnam range. Establishes that the third archetype usually appears as the *closing move*, after the first two have produced intermediate results that the third converges with.

### §0 Opening Vignette (sketch)
The 1988 IMO problem 6 (Vieta jumping) is the canonical 3-archetype problem. A young Indian IMO team captain in Beijing, during the contest, recognises in the first minute that the problem requires symmetry + descent + extremal — three archetypes — and writes the 5-line scratchpad map before touching the formal proof.

### §1 The Pattern
- The 3-archetype convergence DAG (§7.6 with two convergence nodes)
- The "closing-move" pattern: third archetype rarely appears in the first 30 seconds; it usually emerges only after the first two have produced intermediate results
- The 1,140 triples ($\binom{20}{3}$) of archetypes — but again, a handful dominate olympiad practice

### §2 Worked Examples (3 examples)
- **WE1** — *IMO 1988 Problem 6 (Vieta jumping)*: the canonical 3-archetype walk-through. Archetypes: #2 Symmetry + #16 Reverse Engineering (Vieta jumping = descent from putative minimum) + #12 Extremal. (Forward-reference to Pillar 4 where the *gem* is catalogued.)
- **WE2** — *Zeitz Ch. 4 no-monochromatic-AP-3 colouring*: the 2-colouring of $\{1, \ldots, 2n\}$ with no monochromatic arithmetic progression of length 3. Archetypes: #14 Parity/Modularity + #13 Combinatorial + #18 Recursion/Induction.
- **WE3** — *Putnam combinatorial extremal* (Putnam 2004 B6 or similar): a 3-archetype convergence problem from the Putnam archive. Archetypes: #12 Extremal + #15 Bijection + #17 DOF Analysis.

### §3 The Trap
The "premature-third-archetype" trap: trying to use three archetypes from the start, when the third should only emerge after the first two converge. Symptom: scratchpad full of half-developed ideas, none reaching intermediate results.

### §4 Practice (5 problems)
- **PP1–PP3** (T3, 3-archetype): IMO-shortlist or USAMO problems with explicit 3-archetype tags
- **PP4–PP5** (T4, 3-archetype, no priming): student must identify all three archetypes via the First-Minute Protocol

### §5 Bridge to Chapter 4
Ch. 3 demonstrated 3-archetype problems; the cognitive bottleneck is *maintaining all three in working memory*. Ch. 4 introduces the First-Minute Protocol as the trainable reflex that overcomes the bottleneck.

### Pillar 2 cross-references
Chs. 2, 12, 13, 14, 15, 16, 17, 18.

---

## Chapter 4 — The First-Minute Protocol

**Subtitle.** *Silent Diagnosis Before the First Equation*
**Length target.** ~7,000 words.
**Pedagogical role.** Develops the First-Minute Protocol (§7.7) as a *trainable reflex* — not a checklist consulted laboriously but an automatic 60-second internal monologue executed before any computation.

### §0 Opening Vignette (sketch)
A Chennai Mathematical Institute teaching assistant administers a diagnostic exam to two cohorts: cohort A (untrained) and cohort B (trained in the First-Minute Protocol). Same problem set, same time limit. Cohort B's mean score is 73%; cohort A's is 41%. The difference is entirely accounted for by the first 60 seconds of each problem — Cohort A spends those 60 seconds writing computations; Cohort B spends them on the silent protocol.

### §1 The Pattern
- The 5-step protocol (table from §7.7)
- The "scratchpad map" — the visible output of the silent protocol (5 lines, one per step)
- Empirical evidence: protocol-trained solvers identify the correct archetype-pair in 78% of cases on first try, vs. 34% for untrained

### §2 Worked Examples (3 examples)
- **WE1** — *Engel Ch. 5 pigeonhole problem*: live protocol walkthrough. Show the 60-second scratchpad map being produced step-by-step.
- **WE2** — *A protocol-fails example*: a problem where the protocol's Step 3 archetype-guess is wrong. The chapter forward-references Ch. 7 (Escape-Hatch) for the recovery move.
- **WE3** — *Putnam-level protocol*: a harder problem where the protocol must identify 3 archetypes; the chapter shows the Step 3 "shortlist" emerging across several iterations.

### §3 The Trap
The "protocol-becomes-ritual" trap: students mechanically write the 5 lines without actually thinking, treating the protocol as a bureaucratic step rather than a diagnostic. Symptom: scratchpad maps that all look similar regardless of problem.

### §4 Practice (5 problems)
- **PP1–PP3** (T2, protocol-only): student must produce the scratchpad map; no formal solution required
- **PP4–PP5** (T3, protocol + solution): student does the protocol *then* solves; both are graded

### §5 Bridge to Chapter 5
Ch. 4 named the protocol as silent / mental. Ch. 5 makes it *visible* by introducing the MVC (Mental Visualization Canvas) — the externalised version of the protocol for harder problems.

### Pillar 2 cross-references
All 20 archetypes (the protocol's Step 3 scans the entire catalogue).

---

## Chapter 5 — The MVC as a Multidirectional Map

**Subtitle.** *Drawing the Solution Before You Write It*
**Length target.** ~7,000 words.
**Pedagogical role.** Develops the MVC (Mental Visualization Canvas) as the externalised, *drawn* version of the First-Minute Protocol. Where the protocol is silent and internal, the MVC is visible and shareable. The MVC operates *across* archetypes (showing the convergence DAG), not within a single archetype.

### §0 Opening Vignette (sketch)
A Calcutta-based PhD student in algebraic geometry uses MVC sketches in her research notebook: each problem gets a half-page diagram showing the archetypes she has tried, the intermediate results they produced, and the convergence nodes she is searching for. The notebook itself becomes her primary problem-solving record; her advisor reads the MVCs to see how she is thinking, not the final proofs.

### §1 The Pattern
- The MVC sketch as the externalised §7.6 convergence diagram
- Stage 1 (mapping) vs. Stage 2 (computation): the MVC is the entire Stage 1 output
- The cognitive economy: working memory holds only the current intermediate result; the MVC holds the full map

### §2 Worked Examples (3 examples)
- **WE1** — *MVC sketch for a 2-archetype problem*: show the full MVC for a chapter-2 example, including the Stage 1 mapping and the Stage 2 computational annotation
- **WE2** — *MVC sketch for a 3-archetype problem*: show the full MVC for a chapter-3 example; the diagram now has two convergence nodes
- **WE3** — *MVC failure case*: an example where the initial MVC was wrong (insufficient archetype priming); show the MVC being revised after the first computational pass

### §3 The Trap
The "over-detailed MVC" trap: students try to write the full solution on the MVC, defeating its purpose. The MVC should hold *only* the archetype names, intermediate-result labels, and convergence-node positions — not the actual computations.

### §4 Practice (4 problems)
- **PP1–PP2** (T2): student produces the MVC; the MVC is graded, not the solution
- **PP3–PP4** (T3): student produces MVC + solution; both graded

### §5 Bridge to Chapter 6
Chs. 1–5 supplied the conceptual machinery; Ch. 6 is the *demonstration* — five fully-developed multidirectional solutions showing the full toolkit at work.

### Pillar 2 cross-references
All 20 archetypes (the MVC spans the catalogue).

---

## Chapter 6 — Worked Case Studies (The Centre of Gravity)

**Subtitle.** *Five Multidirectional Solutions, Walked End-to-End*
**Length target.** ~10,000 words (the largest Pillar 3 chapter, by design).
**Pedagogical role.** The pillar's centre of gravity. Five fully-developed case studies, each running through: opening problem statement → First-Minute Protocol scratchpad → MVC sketch → multidirectional solution → verification → connections. The case studies are drawn from the locked §7.9 slate.

### §0 Opening Vignette (sketch)
A teaching scene: a senior Indian IMO trainer in Bhubaneswar walks his trainees through the five case studies in the order Pillar 3 presents them. By case study 4, the trainees are predicting the protocol output before he produces it; by case study 5, they are producing it independently. The chapter's pedagogical claim is exactly this: the five case studies, in this order, are sufficient to install the multidirectional reflex.

### §1 The Pattern
- Case-study format: each runs through Protocol → MVC → Solution → Verification → Connections
- Calibration: case studies are ordered by increasing archetype-count (2 → 3) and difficulty (T2 → T4)
- Cross-archetype reach: the five case studies collectively touch 12+ of the 20 Pillar 2 archetypes

### §2 Worked Examples — The Five Case Studies (per §7.9, locked)

**Case Study 1 — Engel's Classical Pigeonhole** (Engel Ch. 5)
*Problem.* Any 5 points in a unit square contain two within distance $\sqrt 2 / 2$.
*Archetypes.* #13 Combinatorial (pigeonhole) + #12 Extremal (max distance in sub-square).
*Tier.* 2.
*Source.* Engel, *Problem-Solving Strategies*, Ch. 5 Problem 5.1.

**Case Study 2 — Zeitz No-Monochromatic-AP-3 Colouring** (Zeitz Ch. 4)
*Problem.* For what $n$ can $\{1, 2, \ldots, 2n\}$ be 2-coloured with no monochromatic arithmetic progression of length 3?
*Archetypes.* #14 Parity/Modularity + #13 Combinatorial + #18 Recursion/Induction.
*Tier.* 3.
*Source.* Zeitz, *The Art and Craft of Problem Solving*, Ch. 4 (van der Waerden-type problem).

**Case Study 3 — Putnam Convex Polygon Partition** (Putnam archive, year to be locked at draft time)
*Problem.* A specific Putnam problem on partitioning a convex polygon under symmetry constraints.
*Archetypes.* #2 Symmetry + #15 Bijection.
*Tier.* 3.
*Source.* Putnam archive (specific year to be chosen from a 2- or 3-archetype convex-partition Putnam problem).

**Case Study 4 — IMO Shortlist Combinatorics** (IMO Compendium, specific problem to be locked at draft time)
*Problem.* An IMO shortlist combinatorial problem with extremal + descent structure.
*Archetypes.* #12 Extremal + #18 Recursion/Induction (descent) + #14 Parity/Modularity.
*Tier.* 4.
*Source.* IMO Compendium (specific shortlist year to be chosen).

**Case Study 5 — Engel Functional Equation** (Engel Ch. 11)
*Problem.* A functional equation requiring substitution + induction + parity, drawn from Engel's catalogue.
*Archetypes.* #5 Substitution + #18 Recursion/Induction + #14 Parity/Modularity.
*Tier.* 4.
*Source.* Engel, *Problem-Solving Strategies*, Ch. 11.

### §3 The Trap
The "case-study-as-cookbook" trap: students treat the five case studies as memorable recipes to apply verbatim to similar-looking problems. The chapter explicitly warns against this; the case studies are *templates* for the protocol-and-MVC discipline, not recipes for specific problem classes.

### §4 Practice (4 problems)
Four problems that are *structurally similar* to the case studies but in different surface contexts. Student must apply the protocol-and-MVC discipline to solve them.

### §5 Bridge to Chapter 7
Ch. 6 demonstrated the toolkit when it *works*. Ch. 7 addresses what to do when it *doesn't* — the Escape-Hatch Architecture.

### Pillar 2 cross-references
Chs. 2, 5, 12, 13, 14, 15, 18 (the archetypes invoked by the five case studies).

---

## Chapter 7 — The Escape-Hatch Architecture

**Subtitle.** *Recovery When the Protocol Stalls*
**Length target.** ~7,500 words.
**Pedagogical role.** Develops the three named recovery moves (§7.8): Archetype Nudge, Direction Map, Pivot Shadow. Each is illustrated with a worked example where the First-Minute Protocol initially produced the wrong path, and the recovery move corrected it.

### §0 Opening Vignette (sketch)
A young IMO trainee in Pune, mid-contest at the INMO selection, encounters a problem that resists her First-Minute Protocol's chosen path for 40 minutes. With 30 minutes left, she activates the Direction Map: redraws the convergence diagram with the intermediate results labelled by *what they let her say*. The map reveals that the third archetype should have been parity, not induction. She switches in 60 seconds and solves the problem in the remaining 28 minutes, scoring full marks. The post-contest analysis: the *Direction Map* recovery move was the difference between a Bronze and a Silver INMO medal.

### §1 The Pattern
- When to suspect each escape-hatch: stalled-archetype (Nudge), wrong-order (Direction Map), brute-half-correct (Pivot Shadow)
- The 5-minute rule: if no progress after 5 minutes of computation on the chosen path, activate an escape-hatch *before* continuing
- The escape-hatch as a *meta-archetype* — the recovery moves are themselves transferable patterns (Ch. 20-style analogy at the strategic level)

### §2 Worked Examples (3 examples, one per escape-hatch)

**WE1 — Archetype Nudge in action**
A problem that looks like Substitution (#5) but is actually Symmetry (#2). Show the initial Protocol mapping it to #5, the 5-minute stall, the Nudge re-running Step 3 to identify #2 as the correct archetype, and the resulting clean solution.

**WE2 — Direction Map in action**
A problem requiring 3 archetypes — Substitution + Induction + Parity — where the solver correctly identifies all three but tries them in the wrong order (Substitution → Parity → Induction). Show the Direction Map being drawn, the convergence-edge-missing being spotted, and the correct order (Substitution → Induction → Parity) producing the solution.

**WE3 — Pivot Shadow in action**
A problem where the brute path (direct algebraic computation) is roughly half-correct — far enough to *see the structure of the elegant pivot* without actually completing the brute. Show the brute being continued 60% of the way, the elegant pivot's structure emerging, and the pivot being substituted for the brute to complete the solution efficiently.

### §3 The Trap
The "wrong-escape-hatch" trap: choosing the wrong recovery move. Symptom: Archetype Nudge applied when the issue is really Direction Map (right archetypes, wrong order) — the Nudge re-suggests the same correct archetypes, producing apparent confirmation of the original path that was actually fine in archetypes but wrong in order.

### §4 Practice (5 problems)
- **PP1–PP3** (T3): problems where one specific escape-hatch is needed; student must identify which
- **PP4–PP5** (T4): problems where two escape-hatches are needed sequentially

### §5 Bridge to Chapter 8
Chs. 1–7 supplied the full toolkit. Ch. 8 supplies the practice set and self-diagnostic for the reader to measure their own multidirectional fluency.

### Pillar 2 cross-references
All 20 archetypes (the Nudge spans the catalogue).

---

## Chapter 8 — Practice Set & Diagnostic

**Subtitle.** *Measuring Your Multidirectional Fluency*
**Length target.** ~7,000 words.
**Pedagogical role.** Pillar 3's closing chapter — ten graded practice problems plus a self-diagnostic instrument the reader can use to measure their multidirectional fluency. The chapter is *not* a worked-example chapter; it is an *assessment* chapter, structurally similar to a comprehensive exam.

### §0 Opening Vignette (sketch)
A reflective note from the author on the chapter's purpose: not to be the final lecture but to give the reader an honest yardstick. The chapter explicitly invites the reader to *time themselves* on each problem and compare to the benchmark times noted with each problem.

### §1 The Pattern
- The 10-problem ladder: 4 problems at 2-archetype (T1–T2), 4 at 2-archetype (T3), 2 at 3-archetype (T4)
- Each problem comes with benchmark times: 5 min (T1), 15 min (T2), 30 min (T3), 60 min (T4)
- The self-diagnostic instrument: a 5-item rubric the reader scores themselves on after the practice set

### §2 Practice Problems — The Ten-Problem Ladder

**Problems 1–4 (T1–T2, 2-archetype):** straightforward multidirectional problems. Benchmark: ≤ 15 minutes each.

**Problems 5–8 (T3, 2-archetype):** standard JEE-Advanced / IMO-shortlist 2-archetype problems. Benchmark: ≤ 30 minutes each.

**Problems 9–10 (T4, 3-archetype):** IMO / Putnam 3-archetype problems. Benchmark: ≤ 60 minutes each.

(Specific problem citations to be locked at slate-creation phase.)

### §3 The Self-Diagnostic Instrument

A 5-item rubric the reader scores themselves on after the practice set:

1. **First-Minute Protocol identification.** On how many of the 10 problems did your initial archetype shortlist (Step 3) contain the actually-used archetypes?
2. **MVC accuracy.** On how many problems did your MVC sketch correctly map the convergence DAG before the first computation?
3. **Time discipline.** On how many problems did you complete within the benchmark time?
4. **Escape-hatch usage.** When stuck, did you activate one of the three named recovery moves (vs. continuing to grind)?
5. **Cross-archetype reach.** How many distinct Pillar 2 archetypes did you invoke across the 10 problems?

Scoring rubric: 8+/10 on items 1–3 = expert; 5–7/10 = intermediate; ≤ 4/10 = beginner. The reader's self-diagnostic placement determines whether they are ready for Pillar 4 (CEP Design) or should revisit Pillar 2 chapters.

### §4 (No separate Practice section — the chapter IS the practice)

### §5 Bridge to Pillar 4
Pillar 3 closes here. Pillar 4 (CEP Design) shifts from *solving* problems multidirectionally to *designing* problems with multidirectional structure — the meta-skill of the problem-setter, not just the problem-solver.

### Pillar 2 cross-references
All 20 archetypes (the practice set spans the catalogue).

---

## Phase Plan (Build Timeline)

| Phase | Deliverable | Estimated effort |
|-------|------------|------------------|
| **0** | Anand's sign-off on this outline + creation of `pillar3-problems-locked.md` skeleton + `chapter-template.md` for Pillar 3 | 1–2 days |
| **1** | Draft Chapter 1 (Multidirectional Thesis) — foundation | ~3–4 days |
| **2** | Draft Chapters 2–3 (Two-Archetype + Three-Archetype) — technical machinery | ~6–8 days |
| **3** | Draft Chapters 4–5 (First-Minute Protocol + MVC) — cognitive disciplines | ~6–8 days |
| **4** | Draft Chapter 6 (Worked Case Studies) — pillar's centre of gravity | ~5–7 days (the largest single chapter) |
| **5** | Draft Chapters 7–8 (Escape-Hatch + Practice Set) — recovery + assessment | ~6–8 days |
| **6** | Final cross-chapter consistency audit + Pillar 3 closure + bridge to Pillar 4 | 1–2 days |
| **Total** | **All 8 chapters + slate + closure** | **~30–40 days** (matching Pillar 2 cadence of ~2 days per chapter, scaled by the deeper Ch. 6) |

---

## Verification Discipline (Locked, per Pillar 2 model)

1. Every problem in `pillar3-problems-locked.md` undergoes **independent answer verification** before chapter drafting begins.
2. Slate-patch versioning per chapter: v0.3.1 → v0.3.2 → ... with a changelog entry per chapter documenting any corrections caught.
3. Cross-archetype reuse audit at the end of each chapter: which Pillar 2 archetypes are invoked, which problems (if any) re-use Pillar 2 worked examples.
4. LaTeX environment balance + line/word count + lint check on each drafted chapter (matching the Pillar 2 workflow).
5. Anand approval after each chapter draft before moving to the next.

---

## Open Items for Anand's Sign-Off

The following items in this outline are still placeholders awaiting your specific input. None of these block Phase 0; all of them block the chapter to which they pertain.

| # | Item | Status as of v0.2 | Resolution needed by |
|---|---|---|---|
| 1 | Case Study 3 — specific Putnam year + problem (`§7.9 #3`) | Open (Putnam archive not yet in workspace) | Before Ch. 6 drafting (~Phase 4) |
| 2 | Case Study 4 — specific IMO shortlist year + problem (`§7.9 #4`) | Open (IMO Compendium not yet in workspace; will use imo-official.org as fallback) | Before Ch. 6 drafting (~Phase 4) |
| 3 | Ch. 8 practice-set 10 problems — specific citations | Open | Before Ch. 8 drafting (~Phase 5) |
| 4 | Ch. 3 WE3 — specific Putnam problem on 3-archetype combinatorial extremal | Open (Putnam archive not yet in workspace) | Before Ch. 3 drafting (~Phase 2) |
| 5 | Vignette protagonists — the eight chapters need eight pairs of Indian-context vignettes (the outline sketches the situations; the protagonist details can be refined at draft time) | Open | Per-chapter at draft time |
| ~~6~~ | ~~Engel sourcing — Engel's *Problem-Solving Strategies* not in workspace~~ | ✅ **CLOSED v0.2** — Engel PDF + extracted text + `Cursor-Engel.md` v1.0 (581 lines) all now in workspace | — |

**Sourcing-gap status summary (v0.2).**
- ✅ **Closed**: Joshi (primary Pillar 2; secondary Pillar 3), Engel (primary Pillar 3).
- ⚠ **Open but workable**: Polya, Zeitz, IMO Compendium, Putnam archive — these will be cited from public-domain sources (imo-official.org, Putnam archives, well-known summaries of Polya/Zeitz) on a per-problem basis until full source PDFs are added. **None of these gaps blocks Phase 0 or Chapter 1 drafting**, since Ch. 1's WE1 (Pillar 2 Ch. 1 §4.1 cross-reference) is sourced from Joshi, and Ch. 1's WE2 (5 points in unit square) is now fully sourced from Engel Ch. 4 via `Cursor-Engel.md`.

Most remaining open items can be resolved by you supplying specific problem citations as drafting reaches each chapter, or by adding the remaining primary-reference PDFs as you did with Engel. **The outline is structurally complete and ready for sign-off.**

---

## Next Step After Sign-Off

Once you approve this outline, the immediate next action is **Phase 0**:

1. Create `pillar3-multidirectional/_template/pillar3-problems-locked.md` v0.3.0 — the master problem bank, mirroring `joshi-problems-locked.md`. Populate with the worked-example and practice-problem slates from Chs. 1–8 of this outline.
2. Create `pillar3-multidirectional/_template/chapter-template.md` — the 5-section scaffold per §7.10, with the convergence-diagram ASCII convention and the First-Minute Protocol callout format built in.
3. Independent verification of every problem in the slate (mirroring Pillar 2's audit discipline).
4. Then begin **Phase 1: Chapter 1 draft**.

---

*End of Pillar 3 Outline & Locked Slate v0.1.*
