# Advaitian Book — Volume 1 Blueprint

*Source-of-truth document for the Advaitian Foundation's first volume. All chapter writing, problem selection, voice calibration, and build decisions defer to this file.*

**Author:** Anand Venkat  
**Working title:** *The Advaitian Philosophy of Problem Solving — Volume 1*  
**Status:** **v3.0 — VOLUME 1 BUILD COMPLETE (May 29, 2026).** All five pillars locked. Previous: v2.5 (pre-flight May 29); v2.4 (Pillar 4 closure, May 28); v2.3 (Pillar 3 closure); v2.2 (Pillar 4 sourcing in workspace); v2.0 (Production-mode setup, May 26).  
**Format:** Markdown canonical → LaTeX (Pandoc) → Overleaf-friendly `.txt`  
**Repository root:** `advaitian-philosophy/`

---

> ## 🌑 VOLUME 1 — BUILD COMPLETE (v3.0, May 29, 2026)
>
> **All five pillars are locked.** The first-draft build of *The Advaitian Philosophy of Problem Solving — Volume 1* is complete.
>
> | Pillar | Scope | State |
> |---|---|---|
> | **1 — The Six-Point Framework** | 1 chapter (~6,200 words) | **LOCKED** |
> | **2 — The 20 Universal Archetypes** | 20 chapters | **LOCKED** (Chs. 1–4 Anand-approved; 5–20 locked as-is) |
> | **3 — Multidirectional Solving** | 8 chapters + problems-locked | **LOCKED** |
> | **4 — CEP-Based Problem Design** | 9 chapters + 25-case slate v0.2.0 + 31-problem record | **LOCKED** |
> | **5 — Mathematical Gems** | 17 prerequisites + 115 gems + cross-ref tables | **LOCKED** (cross-refs provisional) |
>
> **"Build complete" means:** every pillar has a locked draft. It does **not** mean every verification item is closed — those are tracked as a post-build punch-list (§16.5) and do not block the milestone, per Anand's May 29 sign-off (ship-now).
>
> **Remaining (post-build, non-blocking):** the §16.3 verification punch-list, plus editorial polish, build pipeline (Pandoc→LaTeX→Overleaf), and front matter + closing essays + Appendix A.

---

## SECTION 0 — HOW TO USE THIS DOCUMENT

This blueprint is the fixed point. It binds four layers of decision:

1. **Doctrine** — what the book teaches (Sections 1–3).
2. **Architecture** — how the book is built (Sections 4–9).
3. **Operations** — how the book is written, cited, and produced (Sections 10–17).
4. **Production substrate** — the conventions, build pipeline, and verification rhythm that make Pillar-2-through-5 drafting mechanical rather than improvisational (Sections 19–21).

Read top to bottom on first encounter. After that, treat it as a reference: every chapter draft should declare which sections it implements, and any drift from the blueprint should be reconciled here before drift becomes precedent.

When the blueprint and a chapter disagree, the chapter loses. When the blueprint and the master's intent disagree, the master wins — and the blueprint is updated to reflect the new alignment.

This document supersedes all earlier scattered notes in `knowledge_base/`, `chatgpt-*` and `claude-chat-*` exports, and `Thinkmath_04May.md`. Those documents remain as historical record but no longer hold authority.

---

## SECTION 1 — PROJECT IDENTITY & MISSION

### 1.1 What This Book Is

This book is a **bhāṣya** — a structured commentary — on the wisdom of nine masters of mathematical thinking, organised around a single architectural insight: that every mathematical problem is a *Seed–Elegance Connection* orchestrated around a *Central Elegant Point*, and that the entire landscape of solvable problems collapses into roughly twenty fundamental archetypes.

It is, in its essence:

- A **distillation** of nine independent traditions of problem-solving thought into one coherent operating system.
- A **scaffolding** that lets a serious aspirant — JEE Advanced, Olympiad, Putnam, or beyond — see the *deep grammar* underlying the surface chaos of problem types.
- A **manual** for both solving problems and *designing* them, written for the student who wants to stop chasing techniques and start owning the structure.

The volume's charge is to make a working mathematician of the reader — not a more efficient pattern-matcher.

### 1.2 What This Book Is Not

It is not a problem book. It is not a JEE crash-course. It is not a coffee-table popularisation. It does not compete with Joshi's *Educative JEE Mathematics*, Engel's *Problem-Solving Strategies*, or Andreescu's olympiad volumes — it stands on their shoulders.

It does not contain a thousand problems. It contains roughly eighty, chosen with surgical care, each illustrating a structural principle that generalises to ten thousand others.

It is not authored from a position of original problem invention. The problems we use are taken from established sources — primarily K.D. Joshi's *Educative JEE Mathematics* for Pillar 2, the IMO Compendium for Pillar 4, and the Engel/Polya/Zeitz canon for Pillar 3. Our contribution is the *commentary architecture* — the lens through which they are read.

### 1.3 The Bhāṣya Thesis

In the classical Indian intellectual tradition, a bhāṣya is not a translation, summary, or critique. It is a structured re-reading that reveals the architecture latent in the source — making explicit what the original author left implicit, weaving disparate strands into a single fabric, and binding the whole to a unifying principle.

This volume positions itself as a bhāṣya on:

- Polya's *How to Solve It* (the heuristic tradition)
- Tao's *Solving Mathematical Problems* and selected blog essays (the modern olympiad intuition)
- Engel's *Problem-Solving Strategies* (the technique catalog)
- Zeitz's *The Art and Craft of Problem Solving* (the strategic synthesis)
- Andreescu's olympiad corpus (problem culture and competitive precision)
- K.D. Joshi's *Educative JEE Mathematics* (Indian pedagogical depth and commentary structure)
- Lockhart's *Mathematician's Lament* (the philosophical stance)
- Sawyer's *Mathematician's Delight* and *Prelude to Mathematics* (the affective onramp)
- Stewart's *Concepts of Modern Mathematics* and selected popular works (structural maturity)

The unifying principle is the **Advaitian doctrine** (Section 2) — the view that problems are not isolated artifacts but instantiations of a finite library of structural archetypes, each accessible through the same six-point grammar.

### 1.4 Production Posture (May 26, 2026)

The project has crossed from "exploratory" into "production-mode setup." Chapter 1 (Invariance) is drafted and re-instrumented to Joshi sources. The Joshi-to-archetype map is laid. Chapter 2 (Symmetry) is at outline. The pillars 3, 4, 5 are scoped to the level where their first chapters can enter draft on demand.

There is still no deadline. The only standard is *publishability against international peers* — the volume that sits beside Engel and Andreescu on a serious shelf, not a notch below. The 25-day pressure-frame of `Thinkmath_04May.md` is permanently retired in favor of an Anand-paced, Anand-verified production cadence (Section 21).

### 1.5 The Intended Reader (locked)

The book commits to a single anchor reader: **a serious JEE Advanced aspirant aiming for INMO / IMO selection** — a Tier 3–4 student in the developmental schema of Section 5.8.

Every voice choice, every difficulty calibration, every cross-reference assumes this reader. The book is not addressed to the casual hobbyist (too rigorous), the elementary JEE Mains candidate (too difficult past Pillar 2 Tier 1), or the post-graduate (the rigor is below research level). Coaches and trainers benefit downstream from the book — but the *primary address* is the student doing the mathematics.

Consequences of this choice:

- The student has technical fluency at the JEE Advanced level — full algebra, single-variable calculus, basic combinatorics, coordinate / vector geometry, elementary number theory.
- The student does not yet have problem-solving fluency at the olympiad level — that fluency is what the book builds.
- The student is intellectually committed; the book can demand sustained attention without apology.
- The student reads English at a Class 12 / first-year-undergraduate level — sophisticated but not obscure.

---

## SECTION 2 — PHILOSOPHICAL FOUNDATION

### 2.1 The Advaitian Doctrine

The doctrinal core, distilled from the project's `knowledge_base/Advaitian_Master_Framework.txt` and `knowledge_base/ThinkMath_Blueprint_v3.md`:

> Every mathematical problem is a **Seed–Elegance Connection**, hidden beneath the trap of brute-force complexity, orchestrated around a **Central Elegant Point (CEP)**.

Three primitives:

- **Seed** — the underlying meta-pattern (the Archetype). Domain-general, transferable, reusable.
- **Brute Path** — the mechanical, expensive approach that almost every student reaches for first. It is not wrong, only blind.
- **Elegant Pivot** — the single insight that collapses the brute path into a one-line solution. Often a constraint, a symmetry, an invariant, or a change of frame.

Around these three primitives, two further structures organise the doctrine:

- **The Six-Point Framework** — the canonical commentary grammar (Pillar 1): Seed → Brute Path → Elegant Pivot → Pitfalls → Connections → Takeaway.
- **The Twenty Universal Archetypes** — the finite vocabulary of structural patterns through which all problems can be read (Pillar 2).

The Advaitian (अद्वैत, "non-dual") name signals the philosophical claim that beneath the apparent multiplicity of mathematical problem types lies a single underlying structural reality, and that mastery is precisely the recognition of the One within the many.

### 2.2 The Mastery Thesis

The book's pedagogical wager, repeated throughout:

> Mastery is not solving 1,000 problems. Mastery is internalising 20 patterns and learning to see them everywhere, simultaneously, from multiple directions at once.

This is the inversion of the volume-based pedagogy that dominates Indian competitive coaching. We do not deny the value of practice; we deny that practice without structural recognition compounds. A student who has internalised the twenty archetypes will read a new problem the way a chess grandmaster reads a position — by structural pattern, not piece-by-piece calculation.

### 2.3 The Structural Mirror Stance

The book's authorial stance, inherited from the ThinkMath operating manual:

> The author is a **structural mirror**. The reader must always feel that they discovered the truth, because they did. We only held up the mirror.

In practice this means:

- We never give the elegant pivot before walking the reader through the brute path.
- We never reveal the CEP until the reader is one step away from it.
- We never validate a mechanical formula-application as "a good approach."
- We name traps without shaming the trapped.
- We end every chapter with a takeaway the reader could quote five years later.

---

## SECTION 3 — THE SOURCE CANON: NINE MASTERS

The book's authority derives from its conversation with nine independent traditions of mathematical thought. Each master is cited in the front matter and serves a specific structural role.

### 3.1 George Polya (1887–1985)
- **Key works:** *How to Solve It* (1945), *Mathematics and Plausible Reasoning* (1954), *Mathematical Discovery* (1962).
- **Contribution:** The original heuristic vocabulary — *understand the problem, devise a plan, carry out the plan, look back*. The four-phase loop is the proto-form of our six-point framework.
- **Where he appears:** Pillar 1 (framework foundations), Pillar 3 (heuristic geometry), opening epigraphs.
- **Voice signature:** Conversational, confiding, and didactically generous. Polya writes as a mentor at a chalkboard, not as an authority.

### 3.2 Terence Tao (b. 1975)
- **Key works:** *Solving Mathematical Problems* (1992), *Analysis I/II*, the Polymath blog essays on problem-solving.
- **Contribution:** The modern olympiad intuition — the discipline of *not* taking the obvious approach until it has been tested, the practice of converting problems into cleaner equivalent problems, and the meta-habit of asking "what kind of problem is this?" before computing.
- **Where he appears:** Pillar 2 (commentary on classical archetypes), Pillar 4 (philosophical depth on problem design).
- **Voice signature:** Calm, precise, slightly austere. Tao trusts the reader's competence and does not over-explain.

### 3.3 Arthur Engel (1928–2022)
- **Key works:** *Problem-Solving Strategies* (1998).
- **Contribution:** The most thorough catalog of olympiad techniques in print — invariants, extremal principles, pigeonhole, the box principle, induction, infinite descent, coloring, generating functions. Engel is the **technique encyclopedia**.
- **Where he appears:** Pillar 3 baseline (the science/geometry of multidirectional solving). Many of the techniques Engel catalogs are exactly what we re-architect as archetypes in Pillar 2.
- **Voice signature:** Encyclopedic, German-rigorous, terse but exhaustive. Engel does not waste words.

### 3.4 Paul Zeitz
- **Key works:** *The Art and Craft of Problem Solving* (1999, 2nd ed. 2007).
- **Contribution:** The strategic synthesis — Zeitz organises problem-solving around three layers (strategies, tactics, tools) that map cleanly onto our pillars (archetypes, multidirectional moves, gems). His "investigate–wishful thinking–draw a picture" preamble is the intellectual ancestor of our MVC protocol.
- **Where he appears:** Pillar 3 baseline, Pillar 4 (problem-design heuristics).
- **Voice signature:** Patient, expansive, openly affectionate toward problems. Zeitz writes as someone who genuinely loves the mathematics.

### 3.5 Titu Andreescu (b. 1956)
- **Key works:** *Mathematical Olympiad Treasures*, *104 Number Theory Problems*, *Putnam and Beyond*, and the wider Awesome Math corpus.
- **Contribution:** The competitive precision and the discipline of citation — every problem traceable to a year, a country, a round. Andreescu sets the international standard for Olympiad problem culture.
- **Where he appears:** Pillar 4 (case-study source-of-truth alongside the IMO Compendium), Pillar 2 (when a Joshi exemplar needs an Olympiad cousin for cross-domain reach).
- **Voice signature:** Clean, formal, internationally calibrated. No ornament, full rigor.

### 3.6 K.D. Joshi (IIT Bombay)
- **Key works:** *Educative JEE Mathematics* (2nd ed., the 1039-page volume in `my_references/edujeejoshi2ed.pdf`).
- **Contribution:** **The single most important reference for this book.** Joshi is the only author in the world canon who has written a JEE-anchored problem book in the *commentary mode* — every Main Problem is followed by extended Comments that surface alternative approaches, generalisations, pitfalls, and connections. This is, in microcosm, exactly our six-point framework. Joshi is also the **sole problem bank for Pillar 2**: every worked example and practice problem in the Twenty Archetypes chapters is sourced from his book or from JEE/RMO/INMO exams he himself has commented on.
- **Where he appears:** Pillar 2 (problem source-of-truth, voice baseline), the front-matter dedication, the methodological appendix.
- **Voice signature:** Senior Indian-academic — formally precise, generous in commentary, faithful to the JEE reader's frame of reference. Joshi treats the JEE student as an intellectual peer, not a customer.

### 3.7 Paul Lockhart
- **Key works:** *A Mathematician's Lament* (2009), *Measurement* (2012), *Arithmetic* (2017).
- **Contribution:** The philosophical conscience of the volume — the reminder that mathematics is an art before it is a service industry, and that the entire competitive-coaching apparatus risks burning the very thing it claims to teach.
- **Where he appears:** Pillar 4 introduction (problem design as art), select interludes between archetype chapters, the closing essay.
- **Voice signature:** Romantic, polemical, intentionally informal. Lockhart writes against the grain on purpose.

### 3.8 W.W. Sawyer (1911–2008)
- **Key works:** *Mathematician's Delight* (1943), *Prelude to Mathematics* (1955), *A Concrete Approach to Abstract Algebra* (1959).
- **Contribution:** The affective onramp — Sawyer is the master at converting an abstract mathematical idea into an experience the reader has *already had* without realising it. Where Polya teaches heuristics, Sawyer teaches *recognition that mathematics is yours by birthright*.
- **Where he appears:** Chapter 1 opening vignettes across Pillar 2, the Pillar 1 introduction.
- **Voice signature:** Warm, English-pedagogical, quietly subversive of mathematical self-importance.

### 3.9 Ian Stewart (b. 1945)
- **Key works:** *Concepts of Modern Mathematics* (1975), *Galois Theory*, *Letters to a Young Mathematician* (2006), and the wider popular corpus.
- **Contribution:** Structural maturity — Stewart shows how a sophisticated abstract idea can be communicated to a serious general reader without being either dumbed down or technically gatekept.
- **Where he appears:** Cross-domain manifestations (the Connections sections in Pillar 2 chapters), the Pillar 4 essay on the aesthetics of well-posed problems.
- **Voice signature:** British-popular-mathematician — playful, broadly cultured, structurally serious.

### 3.10 The Hybrid Voice (locked, mixed-register)

The book's **voice is not any single one of these**. It is a deliberately calibrated **hybrid** that draws from each master in the section where their register is most appropriate. **The mixed-register rule (locked May 26, 2026):**

| Section type | Person | Tense | Master signature |
|---|---|---|---|
| Philosophical interludes, chapter openers, takeaways | **First person ("I")** | Present, reflective | Lockhart, Sawyer |
| Worked examples, walk-throughs, narrative proofs | **First-person-plural ("we")** | Present, collaborative | Polya, Joshi, Zeitz |
| Definitions, theorems, formal propositions | **Impersonal (third-person, passive where natural)** | Present timeless | Tao, Engel, Andreescu |

Section-by-section voice mapping is given in Section 10. The mixed-register rule is enforced by every chapter-end editorial pass.

---

## SECTION 4 — THE FIVE-PILLAR ARCHITECTURE (OVERVIEW)

The book is organised as five pillars. Each pillar has a distinct pedagogical function, a distinct voice register, and a distinct problem-source canon. They are not five independent books — they are five floors of one building, and the staircase between floors is explicit.

| Pillar | Title | Pedagogical Function | Primary Source | Write Order | Status |
|--------|-------|----------------------|----------------|-------------|--------|
| 1 | The Six-Point Framework | Meta-grammar: the analytical lens applied to every problem in the book | `ThinkMath_Blueprint_v3.md` | **Last (5th)** | Pending |
| 2 | The Twenty Universal Archetypes | Conceptual clarity: what each structural pattern is, how to recognise it | K.D. Joshi *EJM* + JEE/RMO | **First (1st)** | Chapter 1 drafted, Chapter 2 outlined |
| 3 | The Science of Multidirectional Solving | Technique geometry: how archetypes combine and converge | Engel, Polya, Zeitz | **Second (2nd)** | Scoped (Section 7); drafting begins after Pillar 2 mid-point |
| 4 | The Art of Problem Framing | CEP design: how problems are built and dissected | IMO Compendium + Tao, Lockhart, Sawyer | **Third (3rd)** | 25-case slate locked (Section 8.9) |
| 5 | The Gems | Operational execution toolkit: the 108 identities and theorems that implement the pivots | Synthesised from all pillars | **Fourth (4th)** | 108 target locked; cluster targets defined |

**Sequencing rationale:**
- Pillar 2 first because it establishes the vocabulary every other pillar uses.
- Pillar 3 second because it builds on the archetype vocabulary to discuss multi-archetype convergence.
- Pillar 4 third because problem-design analysis requires fluency in both archetypes and multidirectional strategy.
- Pillar 5 fourth because the right inventory of gems emerges organically from the problems chosen in Pillars 2–4.
- Pillar 1 last because the six-point framework, while logically prior, is best introduced *after* the reader has seen it applied throughout — then the meta-grammar becomes a recognition, not an imposition.

---

## SECTION 5 — PILLAR 1: THE SIX-POINT FRAMEWORK

### 5.1 Role and Scope

Pillar 1 is the meta-grammar of the book. It teaches the reader *how to think about* a problem before and after solving it. Every worked example in every other pillar is formatted using the six-point commentary — so by the time the reader arrives at the Pillar 1 chapter, the framework will feel like naming something already known.

### 5.2 Canonical Source

The authoritative source for Pillar 1 is `knowledge_base/ThinkMath_Blueprint_v3.md`, the ThinkMath Advaitian Socratic Mentor operating manual (v3.0). All structural decisions about what the six-point framework is, how it was arrived at, and how it scales across developmental tiers are settled in that document. Pillar 1's job is to externalize and narrativize what `ThinkMath_Blueprint_v3.md` encodes operationally.

### 5.3 The Six-Point Framework (Canonical Definition)

Every commentary produced by this book — worked example, case study, problem-design analysis — includes exactly these six sections in this order:

1. **SEED** — One sentence naming the underlying structural archetype. Domain-general, reusable. Names the archetype by its title and number.
2. **BRUTE PATH** — The mechanical approach a student would naturally attempt. Concrete, with enough algebra to show where it becomes blind or expensive. Delivered without judgment — the brute path is not wrong, only costly.
3. **ELEGANT PIVOT** — The key insight that collapses the brute path. Named explicitly. The mathematics shown in full. The convergence point of any multidirectional approach made visible. Should feel inevitable in hindsight, surprising before.
4. **PITFALLS** — Three to five named cognitive traps, each with a memorable one-line name, a description of the thinking error, why it is tempting, and an actionable check to avoid it.
5. **CONNECTIONS** — Three mandatory sub-sections: (A) *Primary Archetype Applications* — three to five instances of this archetype appearing elsewhere; (B) *Alternative Solution Archetypes* — two to three other structural approaches to the same problem; (C) *Cross-Domain Manifestations* — two to three appearances of the same structure outside mathematics entirely.
6. **TAKEAWAY** — One sentence, under fifteen words, actionable, memorable. The student must be able to quote it five years later.

### 5.4 The MVC Protocol (Minimum Viable Commentary)

Before Stage 2 (the full six-point commentary), the doctrine requires a Stage 1 validation — the MVC:

> "The seed here is [X]. Most students will try [brute path] because [Y]. The key insight is [Z]. The constraint that prunes everything is [W]."

MVC is valid when: seed is present, brute trap is visible, and the pivot is at least gestured at. The MVC is the reader's proof-of-understanding before the full apparatus is revealed.

### 5.5 Chapter Structure for Pillar 1 (locked detail)

Pillar 1 is a single multi-section chapter (not twenty sub-chapters). Sections, with content scope:

**§5.5.1 The Problem with Problem-Solving Books** *(Lockhart-register opening, "I" voice; ~800 words)*
Why the existing literature mostly fails: the rote-technique books treat problems as instances of known recipes; the philosophy books talk about problem-solving without doing any. The book's positioning between these failures. Names the reader (Section 1.5) and the contract: *if you give this book sustained attention, you will leave with a different way of seeing.*

**§5.5.2 What a Commentary Is — and Why You Need a Grammar** *("we" voice; ~1,000 words)*
The bhāṣya tradition; what a commentary does that a solution does not. The grammar metaphor: just as a language without grammar is incommunicable, problem-solving without a grammar is unteachable. The six points as the grammar.

**§5.5.3 The Six Points: A Walking Tour Through One Problem** *("we" voice; ~1,500 words)*
The running example: **the polygon-with-AP-angles problem** (the original Chapter 1 Worked Example, freed up by the Joshi re-instrumentation; its simplicity makes it the perfect didactic vehicle for the framework). Walk the reader through SEED → BRUTE PATH → ELEGANT PIVOT → PITFALLS → CONNECTIONS → TAKEAWAY in full, naming each move as it happens. The point is not to solve the problem (the reader has seen it) but to make the *framework itself* visible.

**§5.5.4 The MVC Protocol: Thinking Before Writing** *(impersonal for definition, "we" for walk-through; ~700 words)*
Define MVC formally. Walk through MVC on the same polygon problem. Contrast MVC with "I'll figure it out as I go" — the discipline argument.

**§5.5.5 The Developmental Tiers: How the Grammar Scales** *(impersonal definitional, "we" for examples; ~1,200 words)*
Define Tiers 0–4 (Section 5.8 below). Show how the same six-point grammar produces different commentary density at each tier — a Tier 1 commentary is a paragraph; a Tier 4 commentary is a page. Examples from the chapters already drafted.

**§5.5.6 Reading the Masters Through the Six Points** *("we" voice; ~1,200 words)*
Brief re-readings of two classical solutions — one from Polya's *How to Solve It* (Polya's own example, e.g., the inscribed-square-in-a-triangle problem), one from Joshi's *EJM* (e.g., the JEE 1989 five-digit problem from Pillar 2 Chapter 1 WE1). Show that the six-point grammar fits naturally onto solutions written *without* knowledge of the grammar — i.e., the grammar is a description of the structure that good mathematical commentary has always had.

**§5.5.7 Self-Diagnosis: Which Points Come Naturally? Which Are Your Blind Spots?** *("I" voice for opening, "we" for diagnostic; ~600 words)*
A self-administered checklist: 12 questions, each pointing at a specific point in the framework. The reader scores themselves and identifies where their solving habits are thinnest. Bridges into the rest of the book as targeted practice.

**Total Pillar 1 length:** ~7,000 words (within the 5.5 length-budget envelope of 8,000–10,000 in Section 13).

### 5.6 Write Status

**LOCKED (May 29, 2026).** Content, structure, and prose approved by Anand after a full back-test against all `knowledge_base/` + `my_references/` docs (three corrections accepted). Length ~6,200 words accepted as final. Drafted as `pillar1-framework/01-six-point-framework.md` — a single multi-section chapter covering all seven sub-sections per §5.5.1–§5.5.7: §1 The Problem with Problem-Solving Books (Lockhart-polemic "I" voice); §2 What a Commentary Is — the bhāṣya grammar + the six points' forced order; §3 a full six-point walking tour of the locked running example (polygon-with-AP-angles, §5.7); §4 the MVC Protocol walked on the same problem; §5 the Developmental Tiers 0–4 with a Tier-1-vs-Tier-4 density demonstration on the polygon; §6 Reading the Masters (Pólya's inscribed-square + Joshi's JEE 1989 five-digit problem, both decomposed through the grammar); §7 a 12-question self-diagnosis keyed to the six points + MVC, bridging into the rest of the book. Built from a full read of `ThinkMath_Blueprint_v3.md` (canonical source, §5.2) and the locked running example. **Back-tested May 29, 2026** against all `knowledge_base/` docs (Master Framework, Masterclass, Philosophy Framework, White Paper, Seed-Elegance, Chapter-1-Invariance, Advaitian.md) and the `my_references/` docs (positioning via `why_this_book.txt`; voice via `lockhart-lament.txt`): polygon six-point treatment verified verbatim against the gold-standard commentary; corrected the Pólya inscribed-square locus (passes through a triangle vertex, not the apex) and aligned the polygon takeaway to the canonical "Algebra generates candidates; Geometry selects the winner"; enriched §1 positioning from a binary to the canonical trichotomy (technique / philosophy / culture books → empty quadrant) with the headline "first to treat problem-solving as having a grammar" claim. Now ~6,200 words. Status: **draft** — awaiting Anand's line review.

### 5.7 The Running Example — Locked

Pillar 1 §5.5.3 and §5.5.4 will both use the **polygon-with-AP-angles** problem as the running example:

> *The interior angles of a convex polygon are in arithmetic progression, with smallest angle $120°$ and common difference $5°$. Find the number of sides.*

This problem was the original Chapter 1 Worked Example 1, and was retired from Pillar 2 Chapter 1 in the May 26 Joshi re-instrumentation. It is now reserved for Pillar 1 exclusively — perfect for the framework demonstration because it (a) is two-archetype (Invariance + Domain Constraints) at JEE Mains level, (b) has a clean six-point decomposition, and (c) is solvable by a student in <5 minutes once the framework is in hand.

### 5.8 The Developmental Tiers (locked)

Tiers describe reader-developmental stages, *not* problem difficulty. They calibrate the *density* of the six-point commentary delivered for a given problem.

| Tier | Reader stage | Commentary density | Where the book primarily addresses |
|---|---|---|---|
| 0 | Pre-recognition: solves by formula recall | All six points expanded, ~5–10 sentences each | (Not addressed.) |
| 1 | Surface recognition: spots familiar patterns | 6 points present, ~3–5 sentences each | Pillar 2 PP1–PP2; warm-up half of each chapter |
| 2 | Pattern fluency: applies recognised archetype | 6 points present, terser; ~2–4 sentences each | Pillar 2 PP3–PP4; WE1–WE2 |
| 3 | Multi-archetype: holds 2–3 archetypes simultaneously | 6 points sometimes compressed to 4–5; emphasis on convergence | Pillar 2 WE3; Pillar 3 baseline; Pillar 4 cases 1–10 |
| 4 | Designer: reverse-engineers problems from CEPs | 6 points as analytic skeleton; analysis exceeds them | Pillar 4 cases 11–25; Pillar 5 advanced commentary |

The book primarily addresses **Tiers 3–4**. Tier 1 is the entry difficulty (PP1, PP2 of each Pillar 2 chapter); Tier 4 is the stretch (Pillar 4 case studies 16–25).

---

## SECTION 6 — PILLAR 2: THE TWENTY UNIVERSAL ARCHETYPES

### 6.1 Role and Scope

Pillar 2 is the conceptual core — the vocabulary. It teaches the reader to identify, name, and apply each of the twenty structural archetypes that account for all solvable mathematical problems at the JEE Advanced / Olympiad / Putnam level.

The standard for each archetype chapter: a student who has read and internalised it should be able to look at any unseen problem that belongs to that archetype and — before writing a single equation — name the archetype, describe the brute path, and gesture at the pivot. That recognition is the deliverable, not the ability to write the solution.

### 6.2 Problem-Source Canon for Pillar 2

**Rule: Every worked example and every practice problem in Pillar 2 is sourced from K.D. Joshi's *Educative JEE Mathematics* or from actual JEE/RMO/INMO examinations that Joshi has commented on.**

Rationale: Pillar 2 is the conceptual-clarity pillar. At this stage, the reader should not be wrestling with olympiad-level difficulty; they should be wrestling with *recognition*. Joshi's problems sit at the right difficulty tier (JEE Mains baseline, JEE Advanced ceiling) and come with built-in commentary infrastructure that aligns perfectly with our six-point framework. Using a single problem bank also lets teachers assign a single reference alongside this book.

The reader is the JEE Advanced student of Section 1.5; Joshi's problem corpus is exactly the difficulty band that reader operates in.

The only exception: when no Joshi problem cleanly illustrates a specific archetype, a problem from JEE/RMO archives (which Joshi cites) may be used, provided the citation is exact.

The map of Joshi chapters → archetypes is maintained in `pillar2-archetypes/_template/joshi-archetype-map.md` and is the pre-drafting reference for every Pillar 2 chapter.

### 6.3 The Twenty Archetypes (Canonical Listing)

The archetypes are organised into five categories. Numbers are stable identifiers used throughout the book.

**Category 1 — Structure Recognition (Seeing the Hidden Architecture)**

| # | Archetype | Meta-Principle |
|---|-----------|---------------|
| 1 | **Invariance** | If something stays constant, make it your anchor. |
| 2 | **Symmetry** | If the problem has symmetry, the solution inherits it. |
| 3 | **Duality** | If stuck in one language, speak the dual. |
| 4 | **Hidden Structure** | If it looks unfamiliar, it is probably something familiar in disguise. |

**Category 2 — Transformation Thinking (Changing Representation)**

| # | Archetype | Meta-Principle |
|---|-----------|---------------|
| 5 | **Substitution / Change of Variables** | The right coordinate system makes the problem transparent. |
| 6 | **Linearisation** | If nonlinear, find the linear core underneath. |
| 7 | **Normalisation / Scaling** | Remove the clutter; keep only the structure. |
| 8 | **Domain Translation** | If the language is wrong, speak a different one. |

**Category 3 — Constraint Exploitation (Using Restrictions as Solutions)**

| # | Archetype | Meta-Principle |
|---|-----------|---------------|
| 9 | **Domain Constraints / Bounds** | Algebra generates candidates; domain selects the winner. |
| 10 | **Inequality Constraints** | Sometimes the bounds tell the whole story. |
| 11 | **Existence / Uniqueness Conditions** | Existence precedes computation. |
| 12 | **Extremal Principles** | Nature optimises; so should your solution. |

**Category 4 — Counting and Extremisation (Structuring Chaos)**

| # | Archetype | Meta-Principle |
|---|-----------|---------------|
| 13 | **Combinatorial Principles** | If you cannot enumerate, structure the count. |
| 14 | **Parity / Modularity** | Sometimes the remainder tells the whole story. |
| 15 | **Bijection / Correspondence** | If two problems are isomorphic, solve the simpler one. |

**Category 5 — Meta-Reasoning (Thinking About Problem Structure)**

| # | Archetype | Meta-Principle |
|---|-----------|---------------|
| 16 | **Reverse Engineering** | When the answer is given, the problem is to find the question. |
| 17 | **Degrees of Freedom Analysis** | Count constraints before solving. |
| 18 | **Recursion / Induction** | Solve for one step; repeat to infinity. |
| 19 | **Pivoting / Elimination** | Simplify by subtraction, not addition. |
| 20 | **Analogy / Transfer** | If you have solved it once, you have solved it everywhere. |

### 6.4 Chapter Scaffold (Canonical Template)

Every archetype chapter follows the same structural chassis, defined in `pillar2-archetypes/_template/chapter-template.md`. The canonical scaffold:

```
YAML front matter
  archetype-number, archetype-name, difficulty-tier, joshi-source, word-target

## 0. Opening Vignette  (Sawyer register: a lived observation, not a problem statement)
## 1. The Insight in Plain Language  (Polya register: conversational, definitional)
## 2. The Deep Structure  (Tao/Joshi register: formal definition + group-action framing where relevant)
## 3. The Recognition Algorithm  (Zeitz register: how to spot it in 60 seconds)
## 4. Worked Examples  (Six-Point commentary for each; 3 examples, Joshi-sourced)
## 5. Practice Problems  (7 problems, Joshi-sourced, difficulty tiered)
## 6. Connections Web  (Engel register: this archetype vs. its neighbors)
## 7. Master Takeaways  (bullet: one per key sub-pattern discovered in the chapter)
## 8. Self-Assessment Checklist
## Bridge to Chapter N+1
## Appendix — Solutions to Practice Problems
```

### 6.5 Worked Example Economy

**Three worked examples per chapter.** Each is a full six-point commentary, sourced from Joshi. Difficulty graduation:
- WE1: JEE Mains level (archetype is cleanly isolated, no secondary archetype needed)
- WE2: JEE Advanced level (archetype is the primary driver, one secondary archetype present)
- WE3: JEE Advanced / RMO level (the archetype appears in a non-obvious guise, or the convergence with a second archetype produces the elegant pivot)

### 6.6 Practice Problem Economy

**Seven practice problems per chapter.** Difficulty:
- PP1–PP2: JEE Mains level (direct application)
- PP3–PP4: JEE Advanced level (requires recognition)
- PP5–PP6: RMO level (archetype in disguise or combined with one secondary archetype)
- PP7: INMO level (the chapter's deepest stretch problem; may require two archetypes and a gem)

Solutions appear in the chapter-end appendix of the same file.

### 6.7 Length Budget

Target: **7,000–9,000 words per archetype chapter.** Chapter 1 (Invariance) established this range as achievable and appropriate for the content density.

Total Pillar 2 estimate: 20 chapters × 8,000 words average = **~160,000 words** (approximately 480–550 typeset pages).

### 6.8 Chapter 1 Status (Invariance)

**File:** `pillar2-archetypes/01-invariance.md`
**Draft status:** Joshi-re-instrumented May 26, 2026. All worked examples and practice problems sourced from Joshi *EJM*; Vieta-jumping content relocated to Pillar 4 with forward-reference in place.

**Locked problem set (matches Section 6.10.01 below):**

| Slot | Source | Problem | Tier |
|------|--------|---------|------|
| WE1 | JEE 1989 (Joshi Ch 1 Comment 1) | Five-digit numbers divisible by 3 using $\{0,1,2,3,4,5\}$. Answer 216. | 1 — Mains |
| WE2 | JEE 1981 (Joshi Ch 1 Comment 10) | 30 sets of 5 / $n$ sets of 3, double counting. Answer $n = 45$. | 2 — Adv |
| WE3 | Joshi Ch 4 Main Problem | Number of $n \in [10, 1000]$ with all $\binom{n}{k}$ odd. Answer 6. | 3 — RMO |
| PP1 | JEE 1979 (Joshi Ch 1 Comment 4) | 6 boys / 6 girls in a row; probability girls together | 1 |
| PP2 | JEE 1985 (Joshi Ch 4 Comment 8) | $2 \cdot 7^n + 3 \cdot 5^n - 5$ divisible by 24 | 2 |
| PP3 | JEE 1983 (Joshi Ch 4 Comment 8) | $n(n^2-1)$ divisible by 24 for odd $n$ | 2 |
| PP4 | RMO (Joshi Ex 24.62) | Product of first 1000 evens vs. odds, divisibility by 2001 | 2 |
| PP5 | RMO (Joshi Ex 24.13) | $\alpha^3-3\alpha^2+5\alpha=17$, $\beta^3-3\beta^2+5\beta=-11$; find $\alpha+\beta$ | 2 |
| PP6 | RMO (Joshi Ex 24.75) | 1000 doors / divisor-parity invariant | 2 |
| PP7 | INMO (Joshi Ex 24.69) | $f(x+y)=f(x)f(y)f(xy)$, find all real $f$ | 3 |

### 6.9 Preliminary Joshi-to-Archetype Map

The full archetype-to-chapter mapping for K.D. Joshi's *EJM* lives in `pillar2-archetypes/_template/joshi-archetype-map.md` (v0.1, May 26 2026). Mandatory reading before drafting any Pillar 2 chapter from Chapter 2 onward.

### 6.10 Per-Archetype Chapter Scope (locked, all 20)

The following per-archetype scopes pre-stage problem candidates and structural commitments for chapters 2–20. They are not full outlines (those are produced separately for each chapter, in the style of `pillar2-archetypes/_template/01-invariance-outline.md`) but they are tight enough that an outline can be produced in one pass from the scope.

Format per archetype: **Joshi primary chapter** → **WE candidate sources** → **PP candidate sources** → **Distinctive cognitive shift** → **Forward-references**.

#### 6.10.01 Archetype 1: Invariance — **DRAFTED**

See Section 6.8. Reference: `pillar2-archetypes/01-invariance.md`.

#### 6.10.02 Archetype 2: Symmetry — **OUTLINED**

Joshi primary: Ch. 2 (Basic Algebra), Ch. 18 (Definite Integrals), Ch. 24 (RMO/INMO).
WE candidates: JEE 1979 cyclic AP/GP (Joshi Ch. 2); JEE 1997 odd/even split integral (Joshi Ch. 18); RMO Ex. 24.67 symmetric matrix involution.
PP candidates: Joshi Ch. 6 inequality (TBD), $\int_0^{\pi/2} dx/(1+\tan^n x)$, Joshi Ex. 24.60 (perpendicular concurrence, RMO), Joshi Ex. 24.66 ($abc=1$ inequality, INMO/IMO 2000).
Distinctive cognitive shift: From "what doesn't change" (Invariance) to "what looks the same from multiple perspectives" — the group-action lens.
Forward-references: #1 (Noether bridge), #3 (Duality preview), #15 (Burnside).
Reference: `pillar2-archetypes/_template/02-symmetry-outline.md`.

#### 6.10.03 Archetype 3: Duality

Joshi primary: Ch. 3 (Theory of Equations), Ch. 8 (Geometry), Ch. 21 (Vectors).
WE candidates: A polynomial common-roots problem (Joshi Ch. 3); a pole-polar geometry problem (Joshi Ch. 8); a vector / linear-functional duality (Joshi Ch. 21).
PP candidates: Joshi Ch. 3 discriminant problems; Joshi Ex. 24.11 (partial-order on $\mathbb{C}$).
Distinctive cognitive shift: From single-language solving to language-switching — *if stuck in algebra, speak geometry; if stuck in geometry, speak algebra*. The Felix Klein lens (every geometry has its dual algebraic structure).
Forward-references: #2 (Symmetry; reflection ↔ involution), #5 (Substitution; coordinate change as duality), #19 (Pivoting; primal-dual in linear programming).
Status: **scope only; outline pending.**

#### 6.10.04 Archetype 4: Hidden Structure

Joshi primary: Ch. 5 (Binomial Identities), Ch. 4 (Number Theory).
WE candidates: A binomial identity proved combinatorially (Joshi Ch. 5); a number-theory problem whose solution recognises a hidden modular structure (Joshi Ch. 4).
PP candidates: Joshi Ch. 5 reduction-formula problems; Joshi Ex. 24.49 ($(2m)!(2n)!/(m+n)!$ integer).
Distinctive cognitive shift: From surface-pattern matching to *recognising that an unfamiliar problem is something familiar in disguise*. The unmasking move — "this is really a..." (binomial, recursion, group action, etc.).
Forward-references: #5 (Substitution is the most common disguise-remover), #20 (Analogy is its meta-cousin).
Status: **scope only; outline pending.**

#### 6.10.05 Archetype 5: Substitution / Change of Variables

Joshi primary: Ch. 9 (Coordinate Geometry), Ch. 17 (Areas and Antiderivatives), Ch. 19 (Differential Equations), Ch. 20 (Functional Equations).
WE candidates: A coordinate-choice problem where polar / shifted coordinates collapse the geometry (Joshi Ch. 9); an integral where substitution kills a hard integrand (Joshi Ch. 17); an ODE solved by substitution (Joshi Ch. 19).
PP candidates: Tschirnhaus-substitution problems (Joshi Ch. 3); Weierstrass $t = \tan(\theta/2)$ problems (Joshi Ch. 10); Joshi Ex. 24.13 (the affine shift from Pillar 2 Ch. 1 PP5 reappears here as Tier-1 illustration).
Distinctive cognitive shift: From "the variables given are sacred" to "the variables are coordinates, and the right coordinates make the problem transparent." The Cartesian-coordinates illusion is broken here.
Forward-references: #4 (Hidden Structure; substitution is the move that reveals it), #7 (Normalisation is a special case), #8 (Domain Translation as substitution-across-domains).
Status: **scope only; outline pending.**

#### 6.10.06 Archetype 6: Linearisation

Joshi primary: Ch. 13 (Maxima, Minima and Concavity), Ch. 15 (Limits, Continuity and Derivatives), Ch. 16 (Theoretical Calculus).
WE candidates: A non-linear optimisation with linear-approximation insight (Joshi Ch. 13); a derivative-as-linearisation problem (Joshi Ch. 15); an MVT-style existence proof (Joshi Ch. 16).
PP candidates: Tangent-line-trick inequalities (Joshi Ch. 6); concavity / convexity problems (Joshi Ch. 13).
Distinctive cognitive shift: From "non-linear means difficult" to "non-linear has a linear core — find it." Newton's method as the canonical illustration; Taylor expansion as the systematic case.
Forward-references: #12 (Extremal Principles; linearisation is how extrema get located), #11 (Existence; IVT/MVT live here).
Status: **scope only; outline pending.**

#### 6.10.07 Archetype 7: Normalisation / Scaling

Joshi primary: Ch. 6 (Inequalities), Ch. 13 (Max/Min).
WE candidates: An AM-GM problem where WLOG-normalise-the-sum kills the constraint (Joshi Ch. 6); a homogeneous geometry problem solved by scale-fixing (Joshi Ch. 11).
PP candidates: Joshi Ch. 6 normalisation problems; Buckingham-$\pi$-style dimensional-analysis sketches.
Distinctive cognitive shift: From "all the variables are independent" to "many problems are scale-invariant — pin one variable, the rest follow." WLOG-pricing is the move.
Forward-references: #5 (Substitution; a special form of it), #2 (Symmetry; scaling is a continuous symmetry).
Status: **scope only; outline pending.**

#### 6.10.08 Archetype 8: Domain Translation

Joshi primary: Ch. 9 (Coordinate Geometry), Ch. 21 (Vectors).
WE candidates: A geometry problem solved by complex-number coordinates (Joshi Ch. 21); a real-analysis problem solved by going to $\mathbb{C}$ (Joshi Ch. 8 or 21); a combinatorics problem solved by generating functions (Joshi Ch. 5).
PP candidates: Joshi Ch. 21 complex-as-rotation problems; standard combinatorial-to-algebraic crossings.
Distinctive cognitive shift: From "this is a geometry problem, solve it geometrically" to "the natural language for this problem may not be the language it was given in." Translate, then solve, then translate back.
Forward-references: #5 (Substitution at the language level), #3 (Duality — domain translation between dual structures).
Status: **scope only; outline pending.**

#### 6.10.09 Archetype 9: Domain Constraints / Bounds

Joshi primary: Ch. 3 (Theory of Equations — discriminant analysis), Ch. 10 (Trigonometric Equations), Ch. 11 (Solution of Triangles).
WE candidates: A polynomial-roots problem where reality / positivity filters candidates (Joshi Ch. 3); a trig-equation problem where the domain filters solutions (Joshi Ch. 10); a triangle problem filtered by triangle-inequality (Joshi Ch. 11).
PP candidates: Joshi Ch. 3 discriminant problems; Joshi Ch. 11 triangle existence problems; Joshi Ex. 24.73 (50-element subset with no two summing to 100).
Distinctive cognitive shift: From "algebra is the answer" to "algebra is the candidate-generator; the domain is the filter." Section 4.1 of Chapter 1 (Invariance) already established this two-step pattern — Chapter 9 makes the filter step itself the archetype.
Forward-references: #1 (Invariance; closest cousin), #10 (Inequality Constraints; the most common kind of filter), #11 (Existence; the most rigorous form of filter).
Status: **scope only; outline pending.**

#### 6.10.10 Archetype 10: Inequality Constraints

Joshi primary: Ch. 6 (Inequalities).
WE candidates: AM-GM applied non-obviously (Joshi Ch. 6); Cauchy–Schwarz in a competition setting (Joshi Ch. 6); Jensen's inequality (Joshi Ch. 6 or 13).
PP candidates: Joshi Ch. 6 SOS-style problems; Joshi Ex. 24.65 (sides-of-triangle inequality, RMO).
Distinctive cognitive shift: From "inequalities are obstacles" to "inequalities are constraints that *determine the answer*." The canonical move: convert an equality problem into an inequality problem (or vice versa) when one form makes the structure visible.
Forward-references: #7 (Normalisation; the WLOG step), #9 (Domain Constraints; bounded by inequality), #12 (Extremal Principles; equality cases of inequalities are extrema).
Status: **scope only; outline pending.**

#### 6.10.11 Archetype 11: Existence / Uniqueness Conditions

Joshi primary: Ch. 15 (Limits, Continuity, Derivatives), Ch. 16 (Theoretical Calculus), Ch. 20 (Functional Equations).
WE candidates: An IVT existence proof (Joshi Ch. 16); an MVT existence-of-a-point (Joshi Ch. 16); a functional-equation uniqueness proof (Joshi Ch. 20).
PP candidates: Joshi Ch. 16 Rolle / MVT problems; uniqueness-of-fixed-point problems.
Distinctive cognitive shift: From "compute the answer" to "first prove the answer exists and is unique." The structural move: separate the existence question from the computation question; sometimes only one of the two is asked.
Forward-references: #18 (Induction / Recursion; existence via construction), #9 (Domain Constraints; existence is a filter).
Status: **scope only; outline pending.**

#### 6.10.12 Archetype 12: Extremal Principles

Joshi primary: Ch. 13 (Max/Min and Concavity), Ch. 14 (Trigonometric Optimisation).
WE candidates: An optimisation solved by Lagrange-multiplier-style invariance + extremum (Joshi Ch. 13); a trig-optimisation solved by symmetry (Joshi Ch. 14); an *extremal*-set problem (e.g., the largest subset of $\{1, \ldots, n\}$ with property $P$).
PP candidates: Joshi Ch. 13 calculus optimisation; Joshi Ch. 14 trig optimisation; Joshi Ex. 24.74 (extremal quadrilateral).
Distinctive cognitive shift: From "optimise by calculus" to "the extremum is where the structure breaks down." Pigeon-hole-extremal duality: extremal arguments often reach into structures the smooth optimisation cannot see.
Forward-references: #10 (Inequality; extremum = equality case), #1 (Invariance; the conserved quantity at the optimum), #2 (Symmetry; extrema sit at symmetric points).
Status: **scope only; outline pending.**

#### 6.10.13 Archetype 13: Combinatorial Principles

Joshi primary: Ch. 1 (Counting), Ch. 22 (Finitistic Probability).
WE candidates: Inclusion-exclusion at the right level (Joshi Ch. 1); a complementary-counting problem (Joshi Ch. 1); a partition-by-cases problem (Joshi Ch. 1).
PP candidates: Joshi Ch. 1 standard problems; Joshi Ex. 24.55–24.57 probability problems.
Distinctive cognitive shift: From "list-and-count" to "structure-then-count." The canonical move: find the *invariant or symmetry of the count* before enumerating. Burnside's lemma sits at the boundary with Chapter 2 (Symmetry).
Forward-references: #14 (Parity; parity-counting), #15 (Bijection; the most powerful counting tool), #2 (Symmetry; Burnside).
Status: **scope only; outline pending.**

#### 6.10.14 Archetype 14: Parity / Modularity

Joshi primary: Ch. 4 (Number Theory), Ch. 24 (RMO/INMO).
WE candidates: A problem where parity argument alone closes the proof (Joshi Ch. 4); a modular-arithmetic problem where remainder determines the answer (Joshi Ch. 4); a coloring-as-modular-invariance problem.
PP candidates: Joshi Ch. 4 divisibility problems; Joshi Ex. 24.49 (parity-as-invariance).
Distinctive cognitive shift: From "compute exactly" to "compute mod $m$ — the structure mod $m$ may be all the structure that matters." The canonical move: choose the right modulus.
Forward-references: #1 (Invariance; parity is the prototypical Type-IV invariant), #13 (Combinatorial; parity-counting is the same move), #18 (Induction; modular induction).
Status: **scope only; outline pending.**

#### 6.10.15 Archetype 15: Bijection / Correspondence

Joshi primary: Ch. 5 (Binomial Identities), Ch. 1 (Counting), Ch. 22 (Probability).
WE candidates: A binomial identity proved by combinatorial bijection (Joshi Ch. 5); a "no two adjacent" problem solved by bijection-to-positions (Joshi Ch. 1 Comment 5, JEE 1983); a probability-via-counting problem.
PP candidates: Joshi Ch. 5 bijection problems; Joshi Ex. 24.57 (subset-pair bijection).
Distinctive cognitive shift: From "two seemingly different problems" to "one bijection makes them the same." The orbit-and-equivalence-class lens.
Forward-references: #13 (Combinatorial; same move via different language), #2 (Symmetry; Burnside is a bijection-of-orbits theorem), #20 (Analogy; bijection at the structural level).
Status: **scope only; outline pending.**

#### 6.10.16 Archetype 16: Reverse Engineering

Joshi primary: Ch. 3 (Theory of Equations), Ch. 24 (constructing polynomials with given properties).
WE candidates: Construct a polynomial whose roots have a prescribed property (Joshi Ch. 3); construct a sequence whose closed form has a prescribed structure; construct a problem from a given CEP (forward-references Pillar 4).
PP candidates: Joshi Ch. 3 problems; reverse-engineered Diophantine equations.
Distinctive cognitive shift: From "solve the given problem" to "what problem would have this answer?" The designer's lens. Pillar 4 picks up where this archetype ends — Chapter 16 of Pillar 2 *introduces* the move; Pillar 4 generalises it to systematic CEP design.
Forward-references: **Pillar 4** (the natural extension), #5 (Substitution; reverse-substitution is its first instance), #20 (Analogy).
Status: **scope only; outline pending.**

#### 6.10.17 Archetype 17: Degrees of Freedom Analysis

Joshi primary: Ch. 1 (Counting), Ch. 22 (Probability).
WE candidates: A combinatorial problem solved by DOF-counting (Joshi Ch. 1); a probability-of-favourable-cases problem framed by DOF (Joshi Ch. 22); a geometry-by-DOF problem (Joshi Ch. 9 — "the number of parameters determines the conic").
PP candidates: Joshi Ch. 1 problems; Joshi Ch. 22 conditional-probability problems.
Distinctive cognitive shift: From "solve the system" to "count the equations first." DOF analysis as the cheapest first move: how many unknowns, how many invariants, is the system over- / under- / well-determined?
Forward-references: #1 (Invariance; each invariant kills one DOF), #11 (Existence; uniqueness = DOF zero), #12 (Extremal; Lagrange-multiplier framing).
Status: **scope only; outline pending.**

#### 6.10.18 Archetype 18: Recursion / Induction

Joshi primary: Ch. 4 (Number Theory — Joshi notes induction is the JEE workhorse here), Ch. 5 (Binomial), Ch. 23 (Infinitistic Probability).
WE candidates: A divisibility proof by induction with non-trivial shift-coefficient (Joshi Ch. 4 Comment 8 — the JEE 1982 $7^{2n}+\ldots$ problem); a recursive-sequence closed-form derivation (Joshi Ch. 23); a binomial-identity inductive proof (Joshi Ch. 5).
PP candidates: Joshi Ch. 4 induction problems; Joshi Ch. 23 random-walk recurrences.
Distinctive cognitive shift: From "solve directly" to "solve for one step, propagate by structure." The canonical move: identify the right *inductive parameter* — and recognise when double induction or shift-difference techniques are needed.
Forward-references: #4 (Hidden Structure; the right inductive hypothesis), #20 (Analogy; the inductive step is structural analogy).
Status: **scope only; outline pending.**

#### 6.10.19 Archetype 19: Pivoting / Elimination

Joshi primary: Ch. 3 (Theory of Equations), Ch. 9 (Coordinate Geometry), Ch. 21 (Vectors).
WE candidates: An elimination-via-resultant problem (Joshi Ch. 3); an elimination-of-$y$-between-curves problem (Joshi Ch. 9); a Gaussian-elimination geometry problem (Joshi Ch. 21).
PP candidates: Joshi Ch. 3 common-roots problems; Joshi Ch. 9 intersection problems.
Distinctive cognitive shift: From "add an equation" to "subtract an equation" — pivot on a variable to eliminate it. The dual to substitution. Subtractive simplification rather than additive complication.
Forward-references: #5 (Substitution; the inverse move), #3 (Duality; primal-dual in linear programming is pivoting in matrix form).
Status: **scope only; outline pending.**

#### 6.10.20 Archetype 20: Analogy / Transfer

Joshi primary: Ch. 24 (synthesis), and all chapters via the *connections* sub-section in Joshi's Comments.
WE candidates: A problem from one domain whose solution structure is identical to a famous problem in another (e.g., a counting problem isomorphic to a geometry problem); a problem solved by *carrying over* a technique from a different archetype-chapter.
PP candidates: Cross-domain transfer problems; Joshi Ex. 24.20 (regular-polygon-triangle-count).
Distinctive cognitive shift: From "this problem is new" to "this problem is structurally identical to one I have already solved." The fluency-payoff archetype — late in Pillar 2, the reader has seen 19 archetypes; Chapter 20 is the chapter where they realise *all 19 generalise*.
Forward-references: **Pillar 3** (multidirectional convergence is analogy at the level of solution-paths), all earlier archetypes.
Status: **scope only; outline pending. Note: Chapter 20 is positioned as the Pillar 2 capstone and should be drafted *last*, after all other archetype chapters are stable — its content is partially a synthesis of them.**

---

## SECTION 7 — PILLAR 3: THE SCIENCE OF MULTIDIRECTIONAL SOLVING

### 7.1 Role and Scope

Pillar 3 teaches the *geometry* of problem-solving — how archetypes combine, converge, and interact. If Pillar 2 gives the vocabulary (the twenty archetypes), Pillar 3 gives the syntax: how to work from two or three directions simultaneously and recognise when they are about to converge on the Central Elegant Point.

The central claim of Pillar 3: **hard problems are not hard because the archetype is exotic. They are hard because the solution requires two or three archetypes to operate simultaneously, and the solver must maintain all of them in working memory long enough for the convergence point to appear.**

### 7.2 Reference Baseline

- **Engel** (*Problem-Solving Strategies*) — The technique encyclopedia; Pillar 3 draws heavily on Engel's structural catalogs (invariants, extremal, induction, coloring, etc.) and re-reads them as examples of archetype interaction.
- **Polya** (*How to Solve It*, *Mathematics and Plausible Reasoning*) — The heuristic architecture; Polya's four-phase loop is re-read as the prototype of the multidirectional protocol.
- **Zeitz** (*The Art and Craft of Problem Solving*) — The three-layer model (strategies / tactics / tools) maps directly onto (archetypes / multidirectional moves / gems) and is explicitly acknowledged.

Problem sources for Pillar 3: **Engel, Polya, Zeitz** for baseline examples; **IMO Compendium and Putnam archive** for stretch examples. Joshi may be cited as a secondary source, but is no longer the exclusive problem bank at this pillar level.

### 7.3 Chapter Structure for Pillar 3 (locked, 8 chapters)

The eight chapters are locked. Each chapter follows a sub-template described in §7.10 below.

1. **The Multidirectional Thesis** — Why single-archetype thinking hits a wall; the geometry of convergence; the historical and pedagogical case for multidirectionalism.
2. **Two-Archetype Convergence** — The 2-archetype problem class; the convergence model of §7.6; case studies in Invariance + Domain Constraints, Symmetry + Substitution, Induction + Extremal.
3. **Three-Archetype Problems** — The IMO-level problem class; what it feels like to hold three structural lenses simultaneously; how the third archetype usually appears as the *closing move*.
4. **The First-Minute Protocol** — Silent internal diagnosis before writing; the checklist (§7.7); the practiced reflex.
5. **The MVC as a Multidirectional Map** — How to use Stage 1 thinking to map all active archetypes before Stage 2; the chapter shows MVC operating *across* archetypes rather than within one.
6. **Worked Case Studies** — Five fully developed multidirectional solutions, Engel/Zeitz-sourced, re-read through the Advaitian lens. This chapter is the pillar's centre of gravity.
7. **The Escape-Hatch Architecture** — What to do when stuck (§7.8); Archetype Nudge, Direction Map, Pivot Shadow; the recovery protocol.
8. **Practice Set + Diagnostic** — Ten problems graded from 2-archetype to 3-archetype, with a chapter-end self-diagnostic measuring multidirectional fluency.

### 7.4 Length Budget

Target: **50,000–70,000 words** for Pillar 3 as a whole (roughly 150–200 typeset pages).

### 7.5 Write Status

**Pending.** Drafting begins after Pillar 2 Chapter 5 is drafted (when 5 of the 20 archetypes have stable text — enough Pillar 2 vocabulary to build Pillar 3 on).

### 7.6 The Structural Model of Multidirectional Convergence (NEW)

A multidirectional solution is *a directed acyclic graph* of intermediate insights, in which each node is an archetype-application and each edge is a *convergence* — the moment when two intermediate results combine into one.

**The simplest non-trivial case is the two-archetype problem.** Diagrammatically:

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

**Pillar 2 Chapter 1 §4.1 (the five-digit-divisibility problem) is exactly this shape:**

- Archetype A = Invariance (the digit-sum-mod-3 rule). Intermediate result: the excluded digit must be 0 or 3. This produces the two-case decomposition.
- Archetype B = Domain Constraints (the leading-zero rule). Intermediate result: in the case where 0 is among the digits, 24 of the $5! = 120$ permutations are invalid.
- Convergence: $|S| = 120 + 96 = 216$.

**The three-archetype case** adds a second convergence:

```
A ───┐
     ├──> Convergence 1 ──┐
B ───┘                    │
                          ├──> Convergence 2 (CEP) ──> Answer
                  C ──────┘
```

IMO 1988 P6 (Vieta jumping, treated in Pillar 4) is the canonical illustration. Pillar 3 Chapter 3 develops three-archetype problems systematically.

**Cognitive hardware claim.** Holding two intermediate results in working memory long enough to recognise their convergence is *the central cognitive bottleneck* of multidirectional solving. Working-memory load grows linearly with the number of active archetypes; the practical ceiling for an unaided human solver is three. Beyond three, paper-and-pencil externalization becomes mandatory.

This claim is the structural justification for the *First-Minute Protocol* (§7.7): externalize the active archetypes *before* attempting the solution.

### 7.7 The First-Minute Protocol (NEW)

The First-Minute Protocol is the silent internal diagnostic the trained multidirectional solver runs before writing a single equation. Five steps, each measured in seconds:

| Step | Question | Output (written on scratchpad) | Time |
|---|---|---|---|
| 1 | What is the *given*? | Bullet list, ≤ 5 items | 15 s |
| 2 | What is the *find*? | One sentence, with the answer's type | 5 s |
| 3 | Which archetypes are likely active? | List of 1–3 archetype numbers (from Pillar 2) | 20 s |
| 4 | What is the candidate CEP? | A guess, even if uncertain | 10 s |
| 5 | What is the *brute path* (the thing I won't do)? | One line | 10 s |

Total: 60 seconds. Output: a 5-line scratchpad map of the problem before any computation. Pillar 3 Chapter 4 develops this protocol as a *trainable reflex* with chapter-end exercises.

### 7.8 The Escape-Hatch Architecture (NEW)

When the First-Minute Protocol fails to produce a candidate solution path, or when the chosen path stalls mid-solution, three named recovery moves activate. Each has a distinct cognitive purpose.

**Archetype Nudge.** Suspect the wrong archetype. Re-run the First-Minute Protocol's Step 3 with a different short-list. Particularly useful when the problem looks "almost like" a familiar form but has resisted standard approaches — the resemblance is misleading and a different archetype is the true seed.

**Direction Map.** Suspect the right archetypes but wrong order of application. Draw the two- or three-archetype convergence diagram (§7.6) explicitly on paper, with the intermediate results labelled by what they should *let you say*. The map shows whether an intermediate result is missing or has been incorrectly anchored.

**Pivot Shadow.** Suspect the brute path is half-correct. Continue the brute computation just far enough to *see the structure of what the elegant pivot would have to look like*. The brute path is often a "shadow" of the elegant pivot — the algebraic structure that would emerge from a clean solution is visible in the brute computation, even when the brute computation itself is too heavy to complete.

Pillar 3 Chapter 7 develops each move in detail with worked illustrations.

### 7.9 Case-Study Slate (locked candidates)

Five worked case studies in Chapter 6, drawn from the Pillar 3 reference baseline:

| # | Problem | Source | Archetypes |
|---|---|---|---|
| 1 | The classical pigeonhole — *show any 5 points in a unit square have two within distance $\sqrt{2}/2$* | Engel Ch. 5 | #13 + #12 |
| 2 | *The $n$-coloring of $\{1, \ldots, 2n\}$ with no monochromatic AP-3* | Zeitz Ch. 4 | #14 + #13 + #18 |
| 3 | *Putnam problem on convex polygon partition* | Putnam archive (year TBD) | #2 + #15 |
| 4 | *IMO shortlist combinatorics with extremal + descent structure* | IMO Compendium | #12 + #18 + #14 |
| 5 | *A functional equation requiring substitution + induction + parity* | Engel Ch. 11 | #5 + #18 + #14 |

⚠️ Anand: please confirm or substitute. The slate above is balanced for technique-coverage but not yet locked.

### 7.10 Chapter Sub-Template for Pillar 3

Each Pillar 3 chapter follows this internal scaffold (denser than the Pillar 2 chapter scaffold; Pillar 3 is more discursive):

```
## Opening — the multidirectional thesis at chapter scale
## 1. The Pattern: 2/3-archetype convergence in this chapter's context
## 2. Worked Examples — typically 2-3, each shown with the §7.6 diagram
## 3. The Trap — the most common failure mode and its recovery
## 4. Practice — 4-6 problems graduated 2-archetype → 3-archetype
## 5. Bridge to Chapter N+1
```

---

## SECTION 8 — PILLAR 4: THE ART OF CEP-BASED PROBLEM DESIGN

### 8.1 Role and Scope

Pillar 4 is the book's most original contribution. Most problem-solving books are written from the solver's perspective. Pillar 4 deliberately inverts the frame: it teaches the reader to think like a *problem designer* — to understand how a beautiful problem is engineered around a Central Elegant Point, and to use that understanding both for dissection (reading a hard problem from the inside out) and for construction (building new problems of deliberate elegance).

The two modes are:
- **Descriptive:** Analyzing 25 IMO/Putnam/JEE problems as case studies in CEP design. What was the designer's CEP? How were the traps planted? How does the problem's surface disguise its deep structure?
- **Prescriptive:** A 5-step framework for constructing a problem from a CEP — so that the reader can begin designing problems of their own.

### 8.2 The CEP (Central Elegant Point)

The CEP Library (from `knowledge_base/ThinkMath_Blueprint_v3.md`) lists canonical CEPs organised by difficulty:

| Tier | CEP | Structural Signature |
|------|-----|---------------------|
| Moderate | Perfect square (n²) | Hidden in a divisibility condition |
| Moderate | Triangular number n(n+1)/2 | Disguised as AP or combinatorial sum |
| Moderate | Pythagorean triple | Algebraic identity factoring as a² + b² = c² |
| Hard | Golden ratio (phi) | Recursion a_{n+2} = a_{n+1} + a_n |
| Hard | sqrt(2), sqrt(3) | Integer constraints producing irrationals |
| Hard | Fibonacci sequence | Ratio of consecutive terms approaches phi |
| Extreme | e^(i*pi) + 1 = 0 | Trig + exponential hybrid |
| Extreme | Catalan numbers | Recursive ballot-type counting |
| Extreme | 0 (only solution) | Infinite descent + parity elimination |

The Vieta jumping result in IMO 1988 Problem 6 — that $(a^2 + b^2)/(ab + 1)$ must be a perfect square — is the canonical example of a problem designed around a CEP (the perfect square). It belongs to Pillar 4's case-study corpus, and is Case Study 25 (the capstone) of §8.9 below.

### 8.3 The 5-Step CEP Design Framework

(Adapted from `knowledge_base/ThinkMath_Blueprint_v3.md`, Mode C: Problem Design)

1. **Select the CEP** — Choose the beautiful mathematical object at the center: what answer, identity, or structural truth do you want the solver to discover?
2. **Select the Archetypes** — Which two or three archetypes will converge on the CEP? The problem's difficulty is largely determined by the number of archetypes and the non-obviousness of their combination.
3. **Design the Convergence** — How does the solver travel from the surface statement to the CEP? Design the path, including the dead ends.
4. **Plant the Traps** — What brute-path approaches will look plausible but fail? These are not sadistic; they are instructive. Each trap is a lesson.
5. **Craft the Statement** — The surface statement must be clean, unambiguous, and give away nothing about the interior structure. The most beautiful problems look simpler on the surface than they are inside.

### 8.4 Reference Corpus for Pillar 4

- **IMO Compendium** — Primary problem source for the 25 case studies. Every case study is a real IMO problem, cited with year and problem number.
- **Tao** — Philosophical depth on problem design: what makes a problem mathematically honest, what constitutes artificial difficulty vs. genuine depth.
- **Lockhart** (*A Mathematician's Lament*) — The aesthetic and ethical case for problems as art objects. Lockhart's essay is the framing for Pillar 4's opening chapter.
- **Sawyer** — The reader-recognition angle: how the best-designed problems give the solver the feeling of discovery rather than the feeling of being trapped.
- **Andreescu** — Technical precision on problem-statement craft and competitive problem culture.

### 8.5 Length Budget

Target: **40,000–55,000 words** for Pillar 4 (roughly 120–160 typeset pages).

### 8.6 Chapter Structure for Pillar 4 (locked, 9 chapters)

1. **The Problem as Art Object** *(Lockhart register: opening polemic + Sawyer-warmth; "I" voice)* — Why problems matter as cultural artifacts, not just exam fodder.
2. **Anatomy of a Well-Designed Problem** *(Tao register, "we" voice)* — Walk through one canonical problem identifying the CEP, archetypes, traps, statement-craft. Sets the analytical vocabulary.
3. **The 5-Step CEP Design Framework** *(Prescriptive, "we" voice)* — The 5 steps formalised, with a step-by-step construction of one author-designed problem to demonstrate.
4. **Case Studies 1–5** *(IMO problems, Tier 3-low / Tier 3-mid)* — Moderate-CEP cases. Sub-template per §8.10 below.
5. **Case Studies 6–10** *(Tier 3-mid / Tier 3-high)* — Increasing archetypal complexity.
6. **Case Studies 11–15** *(Tier 3-high / Tier 4-low)*.
7. **Case Studies 16–20** *(Tier 4-mid, including some genuinely difficult IMO problems)*.
8. **Case Studies 21–25** *(Tier 4-high, including IMO 1988 P6 as the capstone)*.
9. **Design Your Own + The Ethics of Difficulty** *("I" + "we" voice, philosophical + practical)* — Three guided design exercises (§8.11); closing essay on hard-and-deep vs. hard-and-arbitrary.

### 8.7 Write Status

**DRAFTED (Phase E.1 complete, May 28, 2026).** All 9 chapters first-draft complete; total ≈ 53,218 words, fitting comfortably inside the 40,000–55,000 budget (§8.5). Batch 1 (Chs. 1–4) approved May 28; Batch 2 (Chs. 5–9) approved May 28. Slate v0.2.0 locked all 25 case studies (`pillar4-case-study-slate-v0.1.0.md` carries the v0.2.0 LOCKED status in-file). Verification record at `pillar4-cep-design/pillar4-problems-locked.md` v0.2.0 covers 31 distinct problems (26 ✓ / 2 ◆ corrections noted / 3 ☼ Compendium-verification deferred to Anand's pass).

**Per-chapter word counts (first draft):**

| Chapter | Words | Status |
|---|---|---|
| Ch. 1 — Problem as Art Object | 5,111 | ✓ drafted |
| Ch. 2 — Anatomy of a Designed Problem | 5,050 | ✓ drafted |
| Ch. 3 — 5-Step CEP Design Framework | 6,030 | ✓ drafted |
| Ch. 4 — Case Studies (Moderate) | 5,516 | ✓ drafted |
| Ch. 5 — Case Studies (Mid) | 6,330 | ✓ drafted |
| Ch. 6 — Case Studies (High-mid) | 6,437 | ✓ drafted |
| Ch. 7 — Case Studies (High) | 6,733 | ✓ drafted |
| Ch. 8 — Case Studies (Extreme, capstone IMO 1988 P6) | 6,977 | ✓ drafted |
| Ch. 9 — Design Your Own + Ethics of Difficulty | 5,034 | ✓ drafted |
| **TOTAL** | **53,218** | All 9 lint-clean |

**Open items at v0.2.0** (carried to Anand's verification pass): Case 19 (IMO 2001 P3 refined incidence-counting), Case 21 (IMO 1992 P3 explicit Turán construction), Case 22 (IMO 2003 P6 order-theoretic precision). All three are flagged ☼ in `pillar4-problems-locked.md` and have cautious draft phrasing in the chapters.

### 8.8 Note on Vieta jumping placement

IMO 1988 P6 was originally treated in Pillar 2 Chapter 1 (Invariance) §4.3. As of the May 26 re-instrumentation, it is relocated to Pillar 4 as Case Study 25 (the capstone). Pillar 2 Chapter 1 retains a forward-reference paragraph pointing to Pillar 4 for full treatment.

### 8.9 Full Case-Study Slate (locked candidates, 25 problems)

The full slate of 25 case studies, organised by Pillar 4 chapter. Each case is identified by: source, problem-statement gist, CEP, archetype combination. Slate is locked at *candidate* level; final lock occurs at Pillar 4 chapter drafting.

#### Chapter 4 (cases 1–5): Moderate CEP

| # | Source | Problem gist | CEP | Archetypes |
|---|---|---|---|---|
| 1 | IMO 1959 P1 | Show $(21n+4)/(14n+3)$ is in lowest terms for every $n$ | Fraction in lowest terms (gcd = 1) | #14 (Parity/Modularity) + #11 (Existence) |
| 2 | IMO 1969 P1 | Polynomial $z = x^4 + y^4 + (x+y)^4$ ; values it takes | Identity $2(x^2+xy+y^2)^2$ | #4 (Hidden Structure) + #5 (Substitution) |
| 3 | Putnam 1985 A-1 | Distance function on a set | Triangle inequality structure | #11 + #12 |
| 4 | IMO 1972 P1 | Subset-pair always has two coprime | gcd(a, b) = 1 forced | #13 + #14 |
| 5 | JEE Adv (chosen via Joshi Ch 24) | A Tier 3 transition problem | TBD | TBD |

#### Chapter 5 (cases 6–10): Mid-difficulty CEP

| # | Source | Problem gist | CEP | Archetypes |
|---|---|---|---|---|
| 6 | IMO 1986 P3 | Pentagon-vertex integer-replacement terminates | Monovariant exists | #1 + #18 + #12 |
| 7 | IMO 1995 P1 | Geometric: chords and tangents | Concyclic-quadrilateral relation | #2 + #3 (Duality) |
| 8 | Putnam 1992 B-2 | Sequence inequality | Fixed point | #11 + #12 |
| 9 | IMO 1979 P3 | Plane subdivision | Euler characteristic | #1 + #13 |
| 10 | IMO 2003 P1 | Subset with sum property | Pigeonhole at the right level | #13 + #12 |

#### Chapter 6 (cases 11–15): High-mid CEP

| # | Source | Problem gist | CEP | Archetypes |
|---|---|---|---|---|
| 11 | IMO 1959 P6 | Tangent lines and cyclic | Specific angle equality | #2 + #3 |
| 12 | IMO 1981 P3 | Diophantine $m^2 - mn - n^2 = \pm 1$ | Fibonacci recurrence | #1 + #18 (descent) + #4 |
| 13 | IMO 1968 P6 | Subset sums of $\{1, \ldots, n\}$ | Specific count formula | #13 + #15 (bijection) |
| 14 | Putnam 1995 A-5 | Distinct sums modulo $n$ | Cyclic-group structure | #14 + #2 |
| 15 | IMO 1989 P5 | Sequence of integer pairs | Periodicity emerges | #1 + #18 |

#### Chapter 7 (cases 16–20): High CEP

| # | Source | Problem gist | CEP | Archetypes |
|---|---|---|---|---|
| 16 | IMO 1986 P5 | Sequence of polynomials | Closed-form expressible | #18 + #4 + #20 |
| 17 | IMO 1993 P3 | Game-theoretic combinatorics | Winning strategy exists | #11 + #16 (Reverse Engineering) |
| 18 | IMO 1976 P4 | Largest product = ? | $3^k$ structure | #12 + #4 |
| 19 | IMO 2001 P3 | Combinatorial geometry | Specific configuration | #13 + #2 |
| 20 | IMO 1985 P4 | Real-number set with squaring | Closed-form structure | #5 + #4 + #18 |

#### Chapter 8 (cases 21–25): Extreme CEP

| # | Source | Problem gist | CEP | Archetypes |
|---|---|---|---|---|
| 21 | IMO 1992 P3 | 9-point geometric construction | Specific 9-point structure | #2 + #3 + #13 |
| 22 | IMO 2003 P6 | Function-equation on primes | $p$-adic structure | #5 + #14 + #4 |
| 23 | IMO 1990 P3 | $2^n \mid n^? - 1$ | Specific power-of-2 invariant | #14 + #18 + #4 |
| 24 | IMO 2001 P6 | Cyclic-quadrilateral inequality | Ptolemy + reverse | #3 + #10 (Inequality) + #2 |
| 25 | **IMO 1988 P6** | $(a^2+b^2)/(ab+1)$ perfect square | **Perfect square via Vieta-jumping orbit** | #16 + #18 + #1 |

⚠️ **Anand: review and lock.** Cases 1–6, 12, and 25 are tight to specific archetype mappings; cases 7–11, 13–24 are candidate-level — each can be substituted with a problem of equivalent CEP-tier and archetype profile if Anand has a stronger preference.

### 8.10 Per-Case-Study Sub-Template

Each of the 25 case studies, in Chapters 4–8 of Pillar 4, follows this internal structure (~800–1200 words each):

```
## Case Study N — [Problem title or one-line gist]

**Source:** [IMO YYYY, Problem K | Putnam YYYY, A/B-N]
**CEP:** [The beautiful mathematical object at the centre]
**Archetypes:** [#X + #Y + #Z]
**Difficulty:** Tier 3-low | Tier 3-mid | Tier 3-high | Tier 4-low | Tier 4-mid | Tier 4-high

### Problem statement
(verbatim, properly cited)

### The Designer's Architecture
- *The CEP unmasked.* What did the designer want the solver to discover?
- *The archetype convergence.* Which archetypes were chosen and why these?
- *The traps planted.* What brute paths look plausible but fail? (Each trap named.)
- *The statement-craft.* What does the surface statement reveal? What does it conceal?

### The Reader's Re-Solution
- A clean Pillar-2-style six-point commentary (≤ 500 words).

### Lessons for Problem Designers
- Two or three bullet-point design moves the reader could lift and apply.
```

### 8.11 Design-Your-Own Problems (Chapter 9)

Three guided design exercises. The reader is given a CEP and asked to design a problem around it, then their problem is "graded" against a designer's-eye rubric.

| # | Given CEP | Target archetype profile | Sample (one such design) |
|---|---|---|---|
| 1 | $7$ (the prime $7$) | 2-archetype, JEE Adv level | "Find all integers $n$ such that $n^2 + n + 7$ is a perfect square" — uses #14 (Parity/Mod) + #11 |
| 2 | Golden ratio $\varphi$ | 3-archetype, RMO level | A Fibonacci-flavoured recurrence problem with concealed $\varphi$ — uses #18 + #4 + #16 |
| 3 | $0$ as unique solution | 3-archetype, IMO-shortlist level | A Diophantine equation whose only solution is the trivial one — uses #18 (infinite descent) + #14 + #1 |

The rubric in the chapter ends with five criteria: cleanness of surface statement, depth of CEP, traps quality, archetype non-obviousness, and pedagogical lift. A self-assessment grid is provided.

---

## SECTION 9 — PILLAR 5: THE GEMS (108 TARGET, LOCKED)

### 9.1 Role and Scope

Pillar 5 is the operational execution toolkit — the collection of specific identities, inequalities, theorems, and computational tools that implement the elegant pivots identified in Pillars 2–4. Where archetypes tell the solver *what* the problem is, gems tell the solver *how* to execute the insight once it is recognised.

### 9.2 Write Status

**LOCKED (May 29, 2026).** Content, structure, and prose approved by Anand. Sole open carve-out: the Pillar 2–4 cross-references remain *(provisional)* pending a dedicated verification pass — this does **not** block the lock. Drafted as two files under `pillar5-gems/`:
- `prerequisites.md` — **Part I, Foundations**: 17 prerequisite blocks (PR01–PR17), Foundation tier, each with orientation + concept list + fluency check, spanning Class 11–12 NCERT (Complex Numbers → Probability). The "pickable-up right after Class 10" on-ramp.
- `gems.md` — **Part II, The Gems**: 115 named gems across Clusters A–G (70 Core / 45 Stretch), each with the seven-field entry (Statement · What it says · The move · When it fires/trigger · Micro-example · Watch for · Used in/Neighbours), plus **Part III** cross-reference tables (Archetype→Gems, Chapter/Case→Gems reverse-lookup, Prerequisite→Gems).

Entry template extends §9.6 with two added fields — **"The move"** and **"When it fires (trigger)"** — to keep entries conceptual rather than appendix-like (approved May 29). Tiering is **Foundation → Core → Stretch**. All Pillar 2–4 cross-references are marked *(provisional)* pending a verification pass against the locked chapters.

Pre-condition had been satisfied: Pillars 2 (20/20), 3 (8/8 signed off), and 4 (9/9 closed at Phase E.1) were all first-draft complete, so the gem set was determined by which pivots actually appeared in the solved problems across the other pillars.

**Pillar-5-to-Pillars-2/3/4 reverse-lookup needed at drafting start.** Before drafting begins, scan the as-drafted chapters for explicit gem invocations (e.g., AM-GM in Pillar 2 Ch. 10 + Pillar 4 Case 5; Vieta jumping in Pillar 4 Case 25; CRT in Pillar 4 Case 15; Sophie Germain in Pillar 4 Case 2; Fibonacci in Pillar 4 Case 12; the golden ratio in Pillar 4 Ch. 9 Ex. 2; the order-modulo-p argument in Pillar 4 Cases 22, 23; etc.) and reconcile against the §9.7 working list. The 4 archetypes deliberately uncovered in Pillar 4 (#3 Reduction, #6 Linearisation, #7 Normalisation, #19 Pivoting — see `pillar4-problems-locked.md` v0.2.0 Coverage Matrix) must each surface in Pillar 5 through gem-coverage of their canonical instances.

### 9.3 Gem Count (locked at 108)

Pillar 5 will contain **108 named gems**, expanding the current working inventory of 45. The number 108 is chosen for three reasons:

1. **Mathematical density** — comparable to Engel's catalog density; the right granularity for a competition-prep reference.
2. **Symbolic resonance** — 108 in Indian tradition (108 Upanishads, 108 names, 108 beads on a mala) marks completeness, signaling the Advaitian identity of the volume.
3. **Practical limit** — beyond ~120 gems the catalog becomes encyclopedic and stops being usable as a study tool.

The final number may drift by ±10 depending on what Pillars 2–4 expose; the *target* is locked at 108.

> **Reconciliation (May 29, 2026).** After a MECE re-audit against the as-drafted Pillars 2–4, the count settled at **115** (within the stated ±10 band): every named tool became its own entry (splits at A07, D04, D07, F04), three used-but-unlisted gems were added (A16, A17, G17), two cited-but-not-applied results were removed (Dirichlet, Hensel), and one pair was merged (generating functions). 70 Core + 45 Stretch. Part I's 17 Foundation blocks sit below the gem tier and are not counted among the 115.

### 9.4 Cluster Targets (locked)

The seven clusters with their gem-count targets:

| Cluster | Name | Current count | Target |
|---|---|---|---|
| A | Algebraic Identities | 8 | **15** |
| B | Inequalities | 8 | **15** |
| C | Number Theory | 6 | **18** |
| D | Geometry | 8 | **20** |
| E | Sequences and Series | 5 | **12** |
| F | Calculus | 5 | **12** |
| G | Combinatorics | 5 | **16** |
| **Total** | | **45** | **108** |

Cluster C (Number Theory) and Cluster G (Combinatorics) expand the most because Pillars 2–4 will surface many number-theoretic and combinatorial pivots.

### 9.5 Indexing Scheme (NEW — locked)

Every gem is cited by **cluster-letter + 2-digit number**, e.g., **A03** (Algebraic Identity #03) or **G11** (Combinatorics Gem #11). Numbering is fixed at first publication of Pillar 5 and is never re-issued. Forward-references from Pillars 2, 3, 4 to Pillar 5 use this scheme even before Pillar 5 is drafted:

> *(See Gem A01: Vieta's Formulas, Pillar 5.)*

When the gem number is provisional (because Pillar 5 is not yet drafted), the form is:

> *(See Gem A01 [provisional]: Vieta's Formulas.)*

This convention allows Pillar 2 chapters to cite gems immediately while Pillar 5 ordering remains fluid.

### 9.6 Per-Gem Entry Template (NEW)

Every Pillar 5 gem entry has the following structure (300–600 words each):

```
## Gem [Cluster-letter][NN] — [Gem name]

**Statement:** [Exact mathematical statement, in display math]
**Hypothesis / scope:** [Where the gem applies; where it does not]
**Named proof:** [Reference to canonical proof — Hardy & Wright, Engel, etc. — not reproduced here]
**Archetype uses:**
  - #X (Archetype name) — [where the gem implements this archetype's pivot]
  - #Y — [...]
**Worked applications:**
  - Pillar 2 Chapter K, Worked Example M (if applicable)
  - Pillar 3 Chapter K, Case Study M (if applicable)
  - Pillar 4 Case Study M (if applicable)
**Common misuses:** [1–2 specific ways students misapply the gem]
**Connection to neighboring gems:** [E.g., Cauchy-Schwarz → Jensen → Power Mean]
```

### 9.7 Working Gem List (provisional — to be expanded to 108)

The current 45-gem list from `ThinkMath_Blueprint_v3.md` is the seed. Below is the initial assignment of provisional numbers — final Pillar 5 numbering remains pending until Pillar 5 drafting.

**Cluster A — Algebraic Identities (8 → 15, +7 new)**
A01 Vieta's Formulas · A02 Sophie Germain Identity · A03 Sum/Difference of Cubes · A04 Newton's Identity · A05 Binomial Theorem · A06 Telescoping · A07 Factor Theorem · A08 Lagrange Interpolation · *(+7 to add: e.g., Symmetric-Function Identities, Polynomial-Remainder, …)*

**Cluster B — Inequalities (8 → 15, +7 new)**
B01 AM-GM · B02 Cauchy-Schwarz · B03 Jensen · B04 Chebyshev · B05 Power Mean · B06 Triangle Inequality · B07 Rearrangement · B08 Schur · *(+7 to add: Muirhead, SOS, Bernoulli, etc.)*

**Cluster C — Number Theory (6 → 18, +12 new)**
C01 Fermat's Little Theorem · C02 Euler's Theorem · C03 Chinese Remainder Theorem · C04 Lifting-the-Exponent Lemma · C05 Legendre's Formula · C06 Bezout's Identity · *(+12 to add: Wilson's Theorem, Kummer's Theorem, Lucas' Theorem (used in Pillar 2 Ch. 1 WE3), Quadratic Reciprocity sketch, Order of an element, etc.)*

**Cluster D — Geometry (8 → 20, +12 new)**
D01 Power of a Point · D02 Ptolemy's Theorem · D03 Angle Bisector Theorem · D04 Menelaus / Ceva · D05 Euler's Polyhedra Formula · D06 Inversion · D07 Trigonometric Arsenal · D08 Complex Numbers as Geometry · *(+12 to add)*

**Cluster E — Sequences and Series (5 → 12, +7 new)**
E01 AP/GP toolkits · E02 Fibonacci / Golden Ratio · E03 Generating Functions · E04 Stirling numbers · E05 Catalan numbers · *(+7 to add)*

**Cluster F — Calculus (5 → 12, +7 new)**
F01 MVT / Rolle · F02 IVT · F03 L'Hôpital · F04 Integration Arsenal · F05 Taylor / Maclaurin · *(+7 to add)*

**Cluster G — Combinatorics (5 → 16, +11 new)**
G01 Pigeonhole · G02 Inclusion-Exclusion · G03 Double Counting / Bijection · G04 Expected Value Linearity · G05 Stars and Bars · *(+11 to add: Burnside, Catalan numbers' combinatorial interpretation, Erdős-Ko-Rado, etc.)*

---

## SECTION 10 — VOICE AND REGISTER

### 10.1 The Hybrid Voice: Core Principles

The book's voice is a deliberate composite, not a compromise. Each master's register is deployed where it is most effective; no section sounds like all masters at once. The rule: **every section has a primary voice and at most one secondary voice**.

The three constants that hold across all voices (from `ThinkMath_Blueprint_v3.md`, Section 1.3):
- **Warm** — the author is on the reader's side, always.
- **Precise** — things are named exactly. Vague encouragement is noise.
- **Uncompromising** — the elegant pivot is never handed over before it is earned.

**The mixed-register rule (Section 3.10) is the master discipline:**

| Section type | Person | Voice register source |
|---|---|---|
| Philosophical interludes, chapter openers, takeaways | **First person ("I")** | Lockhart, Sawyer |
| Worked examples, walk-throughs | **First-person-plural ("we")** | Polya, Joshi, Zeitz |
| Definitions, theorems, propositions | **Impersonal** | Tao, Engel, Andreescu |

### 10.2 Section-by-Section Voice Map

| Section Type | Primary Voice | Person | Secondary Voice | Notes |
|-------------|---------------|---|-----------------|-------|
| Opening Vignettes (Pillar 2 Chapter openers) | Sawyer | I | Polya | Warm, observational; mathematics as something the reader already knows |
| Plain-language archetype introductions | Polya | we | Sawyer | Conversational, definitional; heuristic vocabulary |
| Formal definitions and theorems | Tao | impersonal | Joshi | Spare, precise; no unnecessary decoration |
| Worked Example: Brute Path | Joshi | we | Zeitz | Commentary mode; generous in showing the mechanical path |
| Worked Example: Elegant Pivot | Tao | we | Engel | Compressed, rigorous; the "now it is trivial" moment made visible |
| Pitfalls sections | Zeitz | we | Polya | Narrative traps named; slightly ironic but never mocking |
| Connections sections | Engel | impersonal | Stewart | Encyclopedic lateral scan; cross-domain reach |
| Practice Problem statements | Andreescu | impersonal | Joshi | Clean, precise, internationally calibrated |
| Chapter Takeaways | Advaitian (house) | I | Polya | Under 15 words; memorable; actionable; the book's own voice |
| Pillar 3: Multidirectional Thesis | Zeitz | we | Polya | Patient, expansive; openly affectionate toward problem structure |
| Pillar 4: CEP Design opening | Lockhart | I | Sawyer | Polemical, romantic; the art-object framing |
| Pillar 4: Case Studies | Tao | we | Andreescu | Calm, precise; structural dissection without ornament |
| Pillar 4: Design Ethics | Tao | I | Lockhart | The hard questions about what mathematical difficulty actually is |
| Pillar 1: Meta-Grammar Introduction | Advaitian (house) | I | Polya | The book talking about itself — should feel like arrival |
| Pillar 5: Gem statements | Tao | impersonal | Engel | Each gem entry: spare, named, sourced |

### 10.2.1 De-facto voice amendment (RATIFIED May 29, 2026 — §16.6 B1)

The drafted volume converged on a consistent house style that **supersedes** the original "Sawyer-I opener / house-I takeaway" prescription in the table above:

- **Chapter openers** are **third-person professional vignettes** ("A juggler tosses five balls…"; "A high-frequency trader in Mumbai monitors…"), not first-person "I". This is uniform across all 20 Pillar 2 chapters and Pillar 3, and is hereby the canonical opener style. (Pillar 1 §1 and Pillar 4 Ch. 1 retain the Lockhart-"I" polemic, which remains correct for those philosophical openings.)
- **Takeaways** are short principle statements (italic/blockquote), not necessarily first-person.
- **Bodies** use **"we" / instructional "you" / impersonal** per the section type, as in the table above (this part held up well).

The three constants (warm, precise, uncompromising) and the worked-example / definition registers in §10.2 remain in force. Treat §10.2's "Person" column for *openers/takeaways* as superseded by this amendment.

### 10.2.2 Pillar 2 scaffold families (SIGNPOSTED May 29, 2026 — §16.6 B4)

Pillar 2's twenty chapters do **not** all use an identical section scaffold, and the variation is **deliberate, not drift**. Three families exist:

| Family | Chapters | Scaffold | Rationale |
|---|---|---|---|
| **Standard archetype** | 1–16 | Opening vignette → Archetype Defined → worked examples (WE) → practice problems (PP) → Master Takeaways → bridge | The default teaching unit: a single technique drilled through worked + practice problems. |
| **Meta-reasoning** | 17–19 | Same as standard, but the WE/PP operate *one level above* the problem (DOF budgets, recursion variables, pivot choices) | These archetypes are *about how to reason*, so their examples are meta-problems; the scaffold is unchanged but the content register lifts. |
| **Capstone synthesis** | 20 | Opening vignette → synthesis essay → three anchor WE (themselves meta-problems about transfer) → seven *transfer prompts* (not fully-worked PP) → 20-archetype master synthesis | Ch. 20 *integrates* the catalogue rather than extending it, so it adopts a synthesis-essay form distinct from Chs. 2–19. |

Each affected chapter also self-signposts in its opening (Ch. 17 line 39 "first chapter of the Meta-Reasoning sub-pillar"; Ch. 20 line 42 "synthesis-essay form, distinct from Chapters 2–19's worked-example form"). A reader encountering a different shape at Ch. 17 or Ch. 20 is meeting an intended variation, not an inconsistency.

### 10.3 Voice Checkpoints

At each major drafting milestone, run a voice checkpoint: read the last 500 words aloud and ask:
1. Is the *person* (I / we / impersonal) consistent with the section type per §10.2?
2. Is there a single identifiable primary voice? (If it sounds like nobody in particular, it sounds like everybody at once, which is worse.)
3. Has any mathematical content been sacrificed for readability? (The rigor is non-negotiable.)
4. Is there a single sentence in the most recent section that a student could quote five years from now? (If not, the takeaway structure is not yet earning its place.)

### 10.4 What the Voice Is Not

- Not lecture-note terse. The voice does not say "it is easy to show that" without showing.
- Not popular-science loose. The voice does not sacrifice precision for accessibility; it earns accessibility through precision.
- Not uniformly Polya-warm. The formal sections are colder by design.
- Not India-specific. The book is internationally calibrated in all respects except its problem bank (Pillar 2), where Joshi is used intentionally.

---

## SECTION 11 — CITATION DISCIPLINE AND PROBLEM-SOURCING RULES

### 11.1 The Cardinal Rule

**Every problem in this book carries a complete citation.** No problem is presented without: source (author/competition), year, chapter or problem number. The word *(author-designed)* is used if and only if no real source exists.

### 11.2 Pillar-by-Pillar Sourcing

| Pillar | Permitted Sources | Prohibited |
|--------|-------------------|-----------|
| Pillar 2 | K.D. Joshi *EJM* (primary); actual JEE/RMO/INMO exams (secondary) | Custom-designed problems without citation; IMO problems at this pillar (reserved for Pillar 4) |
| Pillar 3 | Engel, Polya, Zeitz, Joshi, JEE/RMO/Putnam archives | Problems not traceable to a published source |
| Pillar 4 | IMO Compendium, Putnam archive, Andreescu corpus, JEE Advanced | Unpublished problems (design examples in §8.11 may be author-created, clearly marked) |
| Pillar 5 | Standard mathematical references (Hardy & Wright, etc.); all gem statements are classical | Attribution is to the theorem name and originator, not to a problem book |

### 11.3 Citation Format (in Markdown)

```
**Source:** [Author Last Name], *[Book/Competition Title]*, [Year], [Problem or Chapter Reference]
```

Examples:
```
**Source:** Joshi, *Educative JEE Mathematics* (2nd ed.), Ch. 4, Main Problem.
**Source:** IMO 1988, Problem 6.
**Source:** JEE Advanced 1985, Paper 1, Q.3.
```

### 11.4 "Author-Designed" Problems

When no real source exists and an author-designed problem is needed, the label is:
```
*(Author-designed; JEE Advanced level)*
```
These should be used sparingly — at most one per chapter in Pillar 2 (and only if the Joshi inventory genuinely has no suitable exemplar for that archetype's sub-pattern), and only in §8.11 of Pillar 4.

### 11.5 Copyright Posture

Joshi's problems are reproduced in paraphrase-and-cite mode, not verbatim. The problem statement is re-expressed in the book's own mathematical register while preserving all conditions exactly. The citation is always present. The same standard applies to all competition problems.

### 11.6 Cross-Pillar Reuse Policy

Once a problem has been used as a worked example or practice problem in one pillar, it does **not** reappear as a worked example or practice problem in another. *Exception:* a problem may be *referenced* (with a brief sentence) in a later pillar to illustrate a connection, without being re-solved. *Second exception:* a problem appearing in Pillar 2 Chapter K may be re-examined in Pillar 4 as a CEP-design case study (a different lens on the same problem) — this is exactly the IMO 1988 P6 trajectory.

---

## SECTION 12 — FORMAT AND BUILD PIPELINE

### 12.1 Canonical Format

**Markdown (`.md`) is the canonical authoring format.** All intellectual content — argument, prose, mathematical exposition — is written first in Markdown. LaTeX is a derived format, not a co-equal one. This means:

- Math is written in Markdown with LaTeX delimiters: `$...$` for inline, `$$...$$` for display.
- Theorem/definition/problem environments use Pandoc-compatible fenced div syntax:
  ```
  ::: {.definition}
  A function $Q : X \to \mathbb{R}$ is called an *invariant*...
  :::
  ```
- All figures are described in Markdown alt-text and produced separately as vector graphics.

### 12.2 LaTeX Generation

LaTeX is generated from Markdown via **Pandoc** with a custom template. The build script (`scripts/build.ps1` for Windows; `scripts/build.sh` for Unix-likes) will:

1. Run `pandoc --from markdown --to latex --template=scripts/advaitian-template.tex` on each chapter file.
2. Assemble the chapter `.tex` files into a master `book.tex` with `\input{}` commands.
3. Run `pdflatex` (or `xelatex` for Unicode support) twice to resolve cross-references.

### 12.3 Overleaf-Friendly Output

For every chapter, a self-contained, compilable LaTeX file is generated as a `.txt` file for pasting directly into Overleaf:

```
[chapter-slug]-overleaf.txt
```

This file contains: the `\documentclass`, all preamble packages, `\begin{document}`, the chapter's full LaTeX body, and `\end{document}`. It should compile in Overleaf with a single paste-and-compile, with no external dependencies.

### 12.4 Math Typesetting Conventions

These conventions apply in both Markdown source and generated LaTeX:

- Displayed equations: `\[ ... \]` (not `equation` environment, not `$$` in LaTeX)
- Numbered equations: `\begin{equation} ... \end{equation}` only when the equation is explicitly referenced later
- Theorem/definition/problem: use custom environments (`\begin{theorem}`, `\begin{definition}`, `\begin{problem}`) defined in the preamble
- Inline math: `$...$` in Markdown, `$...$` in LaTeX (consistent)
- Bold vectors: `\mathbf{v}`, not `\vec{v}`
- Sets: `\mathbb{R}`, `\mathbb{Z}`, `\mathbb{N}`, `\mathbb{Q}`
- "Such that" in set-builder: `\mid` (vertical bar with spacing), not `|`
- QED: `\blacksquare` at the right margin
- Binomial coefficient: `\binom{n}{k}` (not `^nC_k`, not `C(n,k)`)

### 12.5 File Naming Convention

```
pillar2-archetypes/01-invariance.md          (canonical Markdown, Chapter 1)
pillar2-archetypes/02-symmetry.md            (Chapter 2, etc.)
pillar2-archetypes/_template/chapter-template.md
pillar2-archetypes/_template/01-invariance-outline.md
pillar2-archetypes/_template/joshi-archetype-map.md
_overleaf-downloads/01-invariance-overleaf.txt
```

### 12.6 LaTeX Preamble Specification (NEW)

The shared LaTeX preamble lives at `templates/advaitian-preamble.tex`. It defines (verbatim, to be implemented before any chapter is built):

```latex
\documentclass[11pt, a4paper, twoside]{book}

% Mathematics
\usepackage{amsmath, amssymb, amsthm, mathtools}

% Theorem environments
\newtheorem{theorem}{Theorem}[chapter]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}

% Problem environment (custom for this book)
\newtheoremstyle{problem}%
  {12pt}{6pt}%      space above/below
  {}%                body font
  {}%                indent
  {\bfseries}%       head font
  {.}%               punctuation after head
  { }%               space after head
  {\thmname{#1}\thmnumber{ #2}\thmnote{ (#3)}}%
\theoremstyle{problem}
\newtheorem{problem}{Problem}[chapter]

% Cross-referencing
\usepackage{hyperref}
\hypersetup{
  colorlinks=true,
  linkcolor=blue!50!black,
  citecolor=blue!50!black,
  urlcolor=blue!50!black
}

% Layout
\usepackage[a4paper, margin=1in, top=1.2in, bottom=1.2in]{geometry}
\usepackage{microtype}

% Section numbering
\setcounter{secnumdepth}{3}
\setcounter{tocdepth}{2}

% Custom commands
\newcommand{\archetype}[1]{\textbf{Archetype \##1}}
\newcommand{\gem}[1]{\textbf{Gem #1}}
\newcommand{\pillar}[1]{\textbf{Pillar #1}}
```

The full preamble file (to be created during build-pipeline construction) will exceed this stub by ~30–50 lines, but the structure above defines the load-bearing environments.

### 12.7 Pandoc Template (NEW)

The Pandoc template `scripts/advaitian-template.tex` is the bridge from Markdown to LaTeX. It is invoked as:

```
pandoc --from markdown --to latex \
       --template=scripts/advaitian-template.tex \
       --metadata-file=scripts/book-metadata.yaml \
       -o build/[chapter-slug].tex \
       pillar2-archetypes/[chapter-slug].md
```

The template handles:
- Front-matter YAML → LaTeX `\chapter{}`, `\section{}`, etc.
- Math passthrough (Markdown `$...$` → LaTeX `$...$`)
- Theorem/Problem fenced divs (`::: {.theorem}` → `\begin{theorem}...\end{theorem}`)
- Citations (Markdown `**Source:**` lines → footnotes in LaTeX)
- Code blocks and tables (standard Pandoc handling)

### 12.8 Build Scripts (NEW)

Two scripts coordinate the full book build:

**`scripts/build-chapter.ps1` (Windows) / `build-chapter.sh` (Unix)**

Single-chapter build:
1. Validate Markdown source (lint front-matter, check for `\end{problem>`-style typos)
2. Pandoc → `.tex`
3. pdflatex (twice, for cross-refs)
4. Output: `build/[chapter-slug].pdf` and `_overleaf-downloads/[chapter-slug]-overleaf.txt`

**`scripts/build-book.ps1` / `build-book.sh`**

Full-volume build:
1. For each chapter in canonical order, run `build-chapter`
2. Assemble all `.tex` files into `book.tex` via `\input{}`
3. pdflatex twice on `book.tex` → `Advaitian-Vol1.pdf`
4. Generate index and cross-reference report

Both scripts emit a build log at `build/build-YYYY-MM-DD.log` capturing warnings, errors, and the rendering status of every chapter.

### 12.9 Overleaf Format Specification (NEW)

The Overleaf-paste `.txt` file is a *self-contained* LaTeX document with the following structure:

```
\documentclass[11pt, a4paper]{article}
[FULL PREAMBLE FROM templates/advaitian-preamble.tex, inlined]

\begin{document}
[CHAPTER BODY in LaTeX]
\end{document}
```

The file is `.txt` (not `.tex`) by design — Overleaf treats `.txt` paste as raw content that the user wraps with their own document. The file is also intentionally *plain text*, no special encoding, so it can be pasted via copy-buffer into any Overleaf project. Every Overleaf `.txt` must compile on a fresh Overleaf project with zero external dependencies.

---

## SECTION 13 — LENGTH BUDGETS

| Component | Target Words | Target Typeset Pages |
|-----------|-------------|----------------------|
| Pillar 1 (one multi-section chapter) | 8,000–10,000 | 25–30 |
| Pillar 2 (20 chapters × ~8,000 words) | 150,000–165,000 | 450–500 |
| Pillar 3 (8 chapters) | 50,000–70,000 | 150–200 |
| Pillar 4 (9 chapters × ~5,000 words + 25 case studies × ~1,000 words) | 60,000–75,000 | 180–225 |
| Pillar 5 (108 gem entries × ~400 words + cluster intros) | 50,000–60,000 | 150–180 |
| Front matter (Preface, Acknowledgments, How to Use) | 3,000–5,000 | 10–15 |
| **Total Volume 1** | **~321,000–385,000** | **~965–1,150** |

This is a substantial volume — larger than Engel's *Problem-Solving Strategies* (600 pp.) and approaching Joshi's *EJM* (1,039 pp.). The word count will be managed at the chapter level; no chapter is permitted to run more than 20% over its target without an architectural review.

---

## SECTION 14 — SEQUENCING AND CURRENT STATUS

### 14.1 Work Order

```
Phase 1 (Complete):   Re-instrument Chapter 1 (Invariance) — DONE May 26, 2026
Phase 2:              Draft Chapters 2–5 (Symmetry, Duality, Hidden Structure, Substitution)
Phase 3:              Draft Chapters 6–10
Phase 4:              Draft Chapters 11–15
Phase 5:              Draft Chapters 16–19
Phase 6:              Pillar 3 entry — begin parallel drafting once Pillar 2 mid-point reached
Phase 7:              Draft Chapter 20 (Analogy / Transfer) — Pillar 2 capstone, written last
Phase 8 (Complete):   Complete Pillar 3 (all 8 chapters) — DONE May 28, 2026
Phase 9 (Complete):   Draft Pillar 4 (all 9 chapters + 25 case studies + 3 design exercises) — DONE May 28, 2026
                      (Phase E.1 closure: slate v0.2.0 LOCKED + problems-locked v0.2.0 + Blueprint v2.4)
Phase 10 (Complete):  Draft Pillar 5 (gem catalog) — LOCKED May 29, 2026 (115 gems + 17 prerequisite blocks; cross-refs provisional)
Phase 11 (Complete):  Draft Pillar 1 (meta-grammar) — LOCKED May 29, 2026 (single chapter, ~6,200 words, all 7 sub-sections; back-tested)
Phase 12:             Draft front matter and closing essays
Phase 13:             Full editorial pass — voice consistency, citation audit, length trim
Phase 14:             Build pipeline final — Pandoc LaTeX generation, Overleaf validation
```

### 14.2 Current Status by File (May 29, 2026 — v3.0, Volume 1 build complete)

| File | Status | Notes |
|------|--------|-------|
| `pillar2-archetypes/` (all 20 chapters) | **LOCKED (May 29, 2026)** | Chs. 1–4 Anand-approved (May 26); Chs. 5–20 locked as-is May 29. Ch. 1 carries two tracked Anand-verification flags (PP4 argument, PP7 functional-equation closure) — see §16.5 punch-list. |
| `pillar2-archetypes/_template/chapter-template.md` | Complete | Canonical scaffold; do not modify without a version bump |
| `pillar2-archetypes/_template/01-invariance-outline.md` | Complete | Approved outline; historical reference |
| `pillar2-archetypes/_template/02-symmetry-outline.md` | Stable | Outline approved-pending; 7 decisions flagged for Anand |
| `pillar2-archetypes/_template/joshi-archetype-map.md` | Stable | v0.1 working map; full archetype-to-chapter routing |
| `pillar3-multidirectional/` (all 8 chapters) | **LOCKED (May 29, 2026)** | All 8 chapters + `pillar3-problems-locked.md` + slate locked (prior "signed off" May 28, relabelled to locked for consistency) |
| `pillar4-cep-design/01-problem-as-art-object.md` | **Drafted (5,111 words)** | Lockhart polemic + Tao warmth register |
| `pillar4-cep-design/02-anatomy-of-designed-problem.md` | **Drafted (5,050 words)** | Tao register; 4-axis anatomy + IMO 1959 P1 demo |
| `pillar4-cep-design/03-cep-design-framework.md` | **Drafted (6,030 words)** | Polya-inverted 5-step framework; author-designed demo |
| `pillar4-cep-design/04-case-studies-moderate.md` | **Drafted (5,516 words)** | Cases 1–5 (Moderate CEP) |
| `pillar4-cep-design/05-case-studies-mid.md` | **Drafted (6,330 words)** | Cases 6–10 (Mid CEP) |
| `pillar4-cep-design/06-case-studies-high-mid.md` | **Drafted (6,437 words)** | Cases 11–15 (High-mid CEP) |
| `pillar4-cep-design/07-case-studies-high.md` | **Drafted (6,733 words)** | Cases 16–20 (High CEP); 1 ☼ open item (Case 19) |
| `pillar4-cep-design/08-case-studies-extreme.md` | **Drafted (6,977 words)** | Cases 21–25 (Extreme); capstone IMO 1988 P6; 2 ☼ open items (Cases 21, 22) |
| `pillar4-cep-design/09-design-your-own.md` | **Drafted (5,034 words)** | 3 design exercises + 5-criterion Rubric + 6-commitment Ethics |
| `pillar4-cep-design/pillar4-case-study-slate-v0.1.0.md` | **v0.2.0 LOCKED** | 25 cases locked May 28 |
| `pillar4-cep-design/pillar4-problems-locked.md` | **v0.2.0 LOCKED** | 31 distinct problems verified |
| `pillar4-cep-design/_template/chapter-template.md` | Complete | Pillar 4 canonical scaffold (3 chassis types) |
| `pillar5-gems/prerequisites.md` | **LOCKED (May 29, 2026)** | Part I, Foundations: 17 blocks PR01–PR17 (Class 11–12 NCERT on-ramp) |
| `pillar5-gems/gems.md` | **LOCKED (May 29, 2026)** | Part II, The Gems: 115 gems (70 Core / 45 Stretch), 7 clusters, 7-field entries + Part III cross-ref tables. Cross-refs *(provisional)* — sole carve-out |
| `pillar1-framework/01-six-point-framework.md` | **LOCKED (May 29, 2026)** | Single multi-section chapter (~6,200 words); all 7 sub-sections (§5.5.1–§5.5.7); running example = polygon-with-AP-angles. Back-tested against all knowledge_base + my_references docs; prose approved |
| `advaitian-philosophy/Cursor-Joshi.md` | Stable | Joshi consolidated memory file |
| `advaitian-philosophy/Cursor-Engel.md` | Stable | Engel consolidated memory file |
| `advaitian-philosophy/Cursor-Zeitz.md` | Stable | Zeitz consolidated memory file |
| `advaitian-philosophy/Cursor-Polya.md` | Stable | Polya memory file (image-PDF caveats noted) |
| `advaitian-philosophy/Cursor-IMO.md` | Stable | IMO Compendium memory file |
| `advaitian-philosophy/Cursor-Lockhart.md` | Stable | Lockhart memory file |
| `advaitian-philosophy/Cursor-Tao.md` | Stable | Tao memory file |
| `knowledge_base/ThinkMath_Blueprint_v3.md` | Stable (read-only reference) | Primary source for Pillar 1 |
| `knowledge_base/Advaitian_Master_Framework.txt` | Stable (read-only reference) | The 20 archetypes + Six-Point Framework canonical definition |
| `Advaitian_Book_vol1_Blueprint.md` | **This file** | v3.0 — source of truth (Volume 1 build complete, May 29) |

---

## SECTION 15 — IMMEDIATE COMMITMENTS

These are the concrete deliverables for the immediate work sessions, updated to reflect Pillar-4 closure and the May 29 plan.

### 15.1 Completed through May 28, 2026

1. ✅ **Pillar 2 — Universal Archetype Catalog** (20/20 chapters drafted; Chs. 1–4 Anand-approved per Part C; Chs. 5–20 first-draft, line-review pending).
2. ✅ **Pillar 3 — Science of Multidirectional Solving** (8/8 chapters drafted + signed off May 28; `pillar3-problems-locked.md` complete).
3. ✅ **Pillar 4 — Art of CEP-Based Problem Design** (9/9 chapters drafted; Batch 1 + Batch 2 approved May 28; slate v0.2.0 LOCKED; 31-problem locked record v0.2.0 with 3 ☼ Compendium-detail items deferred to Anand's verification pass).
4. ✅ **Reference corpus expanded** — 7 Cursor memory files (Joshi + Engel + Zeitz + Polya + IMO + Lockhart + Tao), totalling ~52K words of consolidated reference doctrine. All copyrighted source PDFs in workspace but untracked per Part C precedent.
5. ✅ **Blueprint v2.0 → v2.5** — sources-in-hand, status table, repository map, write-status flips for Pillar 1 + Pillar 5, immediate commitments all refreshed.
6. ✅ **Commits pushed to GitHub** — `565677c` (Pillar 2 Chs. 1–4 + supporting framework), `5fd4efa` (Pillars 2 completion + 3 + 4 + Cursor memory files + Blueprint v2.4).
7. ✅ **Pillar 5 — Mathematical Gems** (May 29, 2026) — **LOCKED.** `prerequisites.md` (17 Foundation blocks PR01–PR17) + `gems.md` (115 gems = 70 Core / 45 Stretch across 7 clusters, seven-field entries incl. "The move" / "When it fires" / "Micro-example" / "Named proof", + Part III cross-ref tables). `key_gems` metadata populated in all 20 Pillar 2 chapters. Sole open carve-out: Pillar 2–4 cross-references remain *(provisional)*, deferred to a dedicated verification pass.
8. ✅ **Pillar 1 — Six-Point Framework** (May 29, 2026) — **LOCKED.** `pillar1-framework/01-six-point-framework.md`, single multi-section chapter (~6,200 words), all 7 sub-sections per §5.5.1–§5.5.7, locked running example (polygon-with-AP-angles), Pólya + Joshi master-readings, 12-question self-diagnosis. Back-tested against all `knowledge_base/` + `my_references/` docs (three corrections accepted: Pólya locus, gold-standard takeaway, §1 trichotomy positioning); prose approved. Length ~6,200 words accepted as final.

### 15.2 With Pillars 1 + 5 drafted, Volume 1 is first-draft complete

All five pillars now have a first draft. The remaining work is no longer drafting but consolidation:
- **Anand line review of Pillar 1** (and the line-review-pending Pillar 2 Chs. 5–20).
- **Deferred Pillar 5 cross-ref verification pass** — promote the *(provisional)* tags to verified against the locked chapters.
- **End-of-session deliverables (May 29):** Blueprint **v3.0 — Volume 1 build complete** (all 5 pillars locked; banner at top; §16.5 punch-list); `Thinkmath_04May.md` Parts E + F + G appended; commit + push (final session of the Volume-1 first-draft sprint).

### 15.3 Post-Volume-1-first-draft (after May 29)

10. **Editorial pass** — voice consistency check across all 5 pillars; citation audit (Pillar 4 ☼ items, Pillar 2 Anand-flagged solution-sketch gaps from Ch. 1 PP4 / PP7); length-trim where chapters exceed Blueprint length budgets.
11. **Pillar 4 ☼ items** — Anand's verification pass on Cases 19, 21, 22 against IMO Compendium; on completion, promotes locked file to v0.2.1.
12. **Build pipeline** (Blueprint §12) — Pandoc → LaTeX → PDF; Overleaf-friendly `.txt` generation for each chapter.
13. **Front matter + closing essays** — Preface, Introduction, Vision chapter; glossary; cross-pillar index by archetype + gem.
14. **8-commentary Appendix A** — insert the polished commentaries from Volume 2 pipeline.
15. **Pre-publication review** per Section 21.

---

## SECTION 16 — OPEN ITEMS AND SOURCE ACQUISITION

### 16.1 Sources Already in Hand

| Source | Location | Status |
|--------|----------|--------|
| K.D. Joshi, *Educative JEE Mathematics* (2nd ed.) | `my_references/edujeejoshi2ed.pdf` + `.txt` | IN WORKSPACE; Cursor-Joshi.md memory file built |
| Arthur Engel, *Problem-Solving Strategies* (Springer, 1998) | `my_references/engel-problem-solving-strategies.pdf` + `.txt` | IN WORKSPACE; Cursor-Engel.md memory file built |
| Paul Zeitz, *The Art and Craft of Problem Solving* (2nd ed.) | `my_references/zeitz-art-craft.pdf` + `.txt` | IN WORKSPACE; Cursor-Zeitz.md memory file built |
| George Polya, *How to Solve It* (Princeton, 1945/2004) | `my_references/PolyaHowToSolveIt.pdf` + `polya-pages/*.png` | IN WORKSPACE (image-only PDF; PNG rasters extracted; Cursor-Polya.md memory file built with transparent caveats) |
| IMO Compendium (Dušan Djukić et al., Springer) | `my_references/imo_compendium.pdf` + `imo-compendium.txt` | IN WORKSPACE; Cursor-IMO.md memory file built |
| Paul Lockhart, *A Mathematician's Lament* | `my_references/A Mathematician's Lament - Paul Lockhart.pdf` + `lockhart-lament.txt` | IN WORKSPACE; Cursor-Lockhart.md memory file built |
| Terence Tao, *Solving Mathematical Problems* | `my_references/solving-mathematical-problems-terence-tao.pdf` + `tao-solving-math-problems.txt` | IN WORKSPACE; Cursor-Tao.md memory file built |
| ThinkMath Advaitian operating manual v3 | `knowledge_base/ThinkMath_Blueprint_v3.md` | Stable |
| Advaitian Master Framework | `knowledge_base/Advaitian_Master_Framework.txt` | Stable |
| Prior chatGPT/Claude discussion archives | `chatgpt-*`, `claude-chat-*` files in repo root | Historical record; not authoritative |

**Sourcing note (Pillar 4 closure, May 28, 2026):** All Pillar-3 and Pillar-4 primary references are now in workspace with consolidated Cursor memory files. The Polya PDF is image-only and was processed via PNG rasterisation; the `Cursor-Polya.md` file documents the caveats and reconstructs Polya's framework from visual transcription + training knowledge. No further source acquisition is required for Pillar 4. Pillar 5 (Mathematical Gems) will continue to use these references plus Hardy & Wright (still to acquire — low priority).

### 16.2 Sources to Acquire Before Pillar 5

Only one remaining acquisition:

| Source | Needed For | Priority |
|--------|-----------|----------|
| Hardy & Wright, *An Introduction to the Theory of Numbers* | Pillar 5 Cluster C reference (number-theory gems) | Low |
| Andreescu, *Mathematical Olympiad Treasures* | Pillar 5 supplementary (already covered by IMO Compendium for case-study purposes) | Optional |
| Sawyer, *Mathematician's Delight* | Pillar 1 vignettes (deferred to Pillar 1 drafting phase) | Low |

### 16.3 Open Architectural Questions (updated May 26, 2026)

Resolved since v1.0:

1. ✅ Case-study count for Pillar 4 — **locked at 25**.
2. ✅ Gem count for Pillar 5 — **locked at 108** (±10 drift permitted).
3. ✅ Intended reader — **locked: serious JEE Advanced aspirant aiming at INMO/IMO**.
4. ✅ Authorial voice — **locked: mixed-register per Section 3.10**.
5. ✅ Vieta jumping placement — **locked: Pillar 4 Case Study 25**.

Resolved at Pillar 3 / Pillar 4 closure (May 28, 2026):

6. ✅ **Pillar 3 chapter count** — locked at 8 chapters (drafted and signed off May 28).
7. ✅ **Pillar 3 case-study slate** — locked and drafted (see `pillar3-multidirectional/pillar3-problems-locked.md`).
8a. ✅ **Pillar 4 chapter count** — locked at 9 chapters (drafted May 28).
8b. ✅ **Pillar 4 case-study slate** — locked at 25 cases (`pillar4-case-study-slate-v0.1.0.md` v0.2.0 LOCKED).
8c. ✅ **Pillar 4 problems-locked** — 31 distinct problems verified (`pillar4-problems-locked.md` v0.2.0).

Still open (pending Anand decision):
8. **Developmental tiers in the printed book** — Section 5.8 defines five tiers (0–4); the book primarily addresses 3–4. Should Tier 0–2 be visible to the reader at all, or only referenced obliquely? My recommendation: brief mention in Pillar 1 §5.5.5; otherwise invisible.
9. **Index design** — every problem will carry an archetype-tag (e.g., `[1, 9]` for a problem using Invariance + Domain Constraints). The aggregate index at end of volume will list all problems by primary archetype. Build pipeline (Section 12.8) generates this automatically from front-matter YAML.
10. **Pre-publication Anand review checkpoints** — per Section 21.

### 16.4 Issues Pending in Drafted Material

Chapter 1 (Invariance):

11. PP4 (RMO 2001-divisibility) — solution-sketch argument leans on a *clean-but-not-tightest* prime-decomposition route. A more elegant Wilson-style pairing exists; Anand to choose.
12. PP7 (INMO functional equation) — solution closes the three constant solutions but flags an analytic gap in the "no non-constant solution exists" closure. Anand to expand or accept.

Chapter 2 (Symmetry, outline only):

13. Outline §4.2 WE2 — JEE 1997 integral, depth of full evaluation. Stop at "symmetric half vanishes" or push to closed-form?
14. Outline §4.3 WE3 — RMO Ex. 24.67 (symmetric matrix involution). Confirm; or substitute with Ex. 24.60 / 24.61.
15. Outline §5 — four practice problems (5.1, 5.3, 5.4, 5.5) proposed by category, not by locked problem statement. Anand may pre-lock.

### 16.5 Post-Build Verification Punch-List (tracked; non-blocking for the v3.0 build milestone)

Per Anand's May 29 sign-off, Volume 1 is **build-complete** with the following items deliberately deferred to a verification/editorial pass. None of these block the v3.0 milestone; all five pillars are locked as-is.

> **Closeout (May 29, PM) — declared CLOSED at the manuscript-complete bar.** Pre-close batch shipped: master TOC created (`Advaitian_Book_vol1_TOC.md`); editorial pass B5/B2/B4 + V10 (British spelling); V8 placeholder refs removed; **V9 done**. Verification run and **flagged for sign-off, not auto-fixed**: V1 (reciprocity audit — 60 confirmed / 127 mismatches), **V6 (Case 17 conflation — needs your ruling)**, V3 (PP7 analytic gap — self-flagged). Remaining open and **owned post-close**: V1 reconciliation, V2 (P4 Compendium checks), V3, V4 (P2 Chs. 5–20 line review), V6, V7 (P3 sourcing — Anand owns), V8 (NT prereq block + Zeitz lines). These are polish/verification, not manuscript blockers.

| # | Item | Pillar | Scope |
|---|------|--------|-------|
| V1 | **Pillar 5 cross-reference verification** | 5 | Promote the *(provisional)* Archetype→Gems / Chapter→Gems / Prerequisite→Gems references in `gems.md` to verified against the locked chapters. **Audited May 29 (reciprocity script, P2):** 60 gem↔chapter pairs reciprocally confirmed; **60 gem→chapter + 67 chapter→gem orphan mismatches** remain (the `Used in` claims and chapter `key_gems` lists were built independently). Reconciliation needs a source-of-truth decision (trust gem-claims vs `key_gems`) before promoting; 113/115 gems stay *(provisional)*. The dead `Blueprint §9.7` placeholder prefix was stripped from all 27 lines (real locations retained). |
| V2 | **Pillar 4 ☼ Compendium-detail items** | 4 | Cases 19, 21, 22 — verify against the IMO Compendium; on completion, promote `pillar4-problems-locked.md` to v0.2.1. |
| V3 | **Pillar 2 Ch. 1 Anand flags** | 2 | PP4 (RMO 2001 divisibility) elegance choice; PP7 (INMO functional equation) analytic-gap closure (see §16.4 items 11–12). |
| V4 | **Pillar 2 Chs. 5–20 line review** | 2 | Locked as-is at the build milestone; Anand prose line-review still desirable (Chs. 1–4 already approved). |
| V5 | **Pillar 2 Ch. 2+ outline-stage decisions** | 2 | §16.4 items 13–15 (WE/practice-problem locks) where any chapter retains outline-stage choices. |
| V6 | **Pillar 4 Case 17 — problem conflation** | 4 | **Sharpened May 29:** the case CEP (golden-ratio weighting, "row 5 unreachable") is the **Conway's Soldiers** solution, but the slate labels it **IMO 1993 P3** and the stated problem is the *n×n* jump-solitaire (real answer *3 ∤ n* via a mod-3 colouring, not the golden ratio). The two are conflated. Resolve by either relabelling the case as Conway's Soldiers, or re-solving the genuine IMO 1993 P3 with the mod-3 invariant. Self-flagged at `07-case-studies-high.md:99,111,115`. |
| V7 | **Pillar 3 problem bank unsigned** | 3 | Ch. 8 diagnostic (10 problems), Ch. 6 CS#2–4, Ch. 4 WE4.3, the Czech & Slovak construction; and `pillar3-multidirectional/_template/pillar3-problems-locked.md` still marks Chs. 5–8 "TBD" though those chapters are locked. Reconcile the locked-index with the drafted chapters. |
| V8 | **Pillar 5 foundation + cross-ref gaps** | 5 | **Refs DONE May 29** (the 27 `Blueprint §9.7` placeholders removed, real locations kept). **Still open:** no Number-Theory prerequisite block for Cluster C (C01–C16) in `prerequisites.md`; the per-Stretch-gem Zeitz motivation line promised in front matter is absent (45 Stretch gems). |
| V9 | **Pillar 1 dual-role + tier note — DONE May 29** | 1 | ~~Add capstone/spiral re-read language to §7; reconcile "exactly six points" with the Tier-3 "compress to four or five" line.~~ Done: added "Read first, re-read last" closing note to §7, and clarified that Tier-3 compression is in the *written* prose (adjacent points merge) while all six remain in the analysis. |
| V10 | **Book-wide spelling: British (RESOLVED May 29)** | all | Ruling: **British** `-ise/-isation` throughout (matches the dominant prose). Executed May 29: canonical labels #6/#7 → **Linearisation** / **Normalisation**; British normalisation pass applied to Pillar 2 Chs. 5–7, 10, 20 prose and this Blueprint (`organis-`, `recognis-`, `generalis-`, `internalis-`, `realis-`, `synthesis-`, `popularis-`, `emphasis-`, `parametris-`). **Filenames keep their American slugs** (`06-linearization.md`) to preserve links/history. No American `-ize/-ization` outstanding from the May 29 scan; a light confirmatory sweep of Pillars 1, 3–5 prose is the only residual. |

**Post-build, beyond verification:** editorial pass (voice consistency across all 5 pillars; length-trim), build pipeline (Pandoc→LaTeX→Overleaf), front matter + closing essays, and the 8-commentary Appendix A.

### 16.6 Editorial-Pass Rulings (May 29, 2026 — post whole-volume coherence review)

A whole-volume coherence review (all 5 pillars read in reading order against the §4/§10/§20 spec) surfaced four hard errors (now fixed: Ch. 20 CEP definition + Ch. 1/2 names + an obsolete Pillar 3/4/5 bridge; Pillar 4 Case 2 diagram `4k^2`→`4k^4`; locked-index `n^2+5n+9`→`n^2+5n+5`; Pillar 5 "seven fields"→"eight"), plus five systemic consistency decisions. Anand's rulings:

- **B1 — Voice: RATIFY the de-facto voice.** The book consistently uses **third-person professional-vignette chapter openers** and **we/impersonal bodies** (not the original §10.2 "Sawyer-I openers / house-I takeaways"). This is now the house style; **§10.2 is amended to match** (see the note appended to §10.2). No re-voicing of chapters required.
- **B2 — Core motif chain: LIGHT FIX.** Standardize capitalization of **Seed / Brute Path / Elegant Pivot / CEP** where they appear, and add **one bridging callback per pillar** tying its local vocabulary back to the chain. Do **not** force the word "Seed" into Pillars 3–5 where specialized vocabulary (convergence, CEP, "the move") reads better.
- **B3 — Archetype names: LOCK the canonical table** below and enforce it everywhere (fixes "Induction"→"Recursion / Induction", "Counting"→"Combinatorial Principles", "DOF Analysis"→"Degrees of Freedom", British/American spelling drift, etc.).
- **B4 — Pillar 2 scaffold: SIGNPOST.** Keep the three families (Chs. 1–16 standard; 17–19 meta-reasoning; 20 capstone) but add a short editorial signpost (in Pillar 1 or a Pillar 2 front-page) explaining that the meta-reasoning cluster and capstone deliberately differ in structure.
- **B5 — Takeaways: TIGHTEN.** A pass to bring every `canonical_takeaway` and in-text takeaway to the ≤~15-word house rule; replace Ch. 20's ~80-word "takeaway" paragraph with a true one-line takeaway; reconcile Ch. 1's YAML takeaway with its in-text quotable line.

**Canonical 20-archetype name table (B3 — authoritative; spelling normalises to these forms):**

| # | Canonical name | # | Canonical name |
|---|---|---|---|
| 1 | Invariance | 11 | Existence / Uniqueness |
| 2 | Symmetry | 12 | Extremal Principles |
| 3 | Duality | 13 | Combinatorial Principles |
| 4 | Hidden Structure | 14 | Parity / Modularity |
| 5 | Substitution / Change of Variables | 15 | Bijection / Correspondence |
| 6 | Linearisation | 16 | Reverse Engineering |
| 7 | Normalisation / Scaling | 17 | Degrees of Freedom |
| 8 | Domain Translation | 18 | Recursion / Induction |
| 9 | Domain Constraints | 19 | Pivoting / Elimination |
| 10 | Inequality Constraints | 20 | Analogy / Transfer |

*Separator convention: compound names use a spaced slash ` / ` (not `&` or en-dash). Spelling follows the book-wide **British** ruling (V10, resolved May 29): #6 **Linearisation**, #7 **Normalisation / Scaling**. Filenames retain their American slugs (`06-linearization.md`, `07-normalization.md`) as stable internal identifiers.*

These rulings govern the editorial pass; the pass itself (B2–B5 enforcement across chapters) is the next unit of work after this review.

---

## SECTION 17 — REPOSITORY MAP

The full repository tree at `advaitian-philosophy/` as of May 26, 2026:

```
advaitian-philosophy/
|
|-- Advaitian_Book_vol1_Blueprint.md      <- THIS FILE (v2.0 source of truth)
|-- Thinkmath_04May.md                    <- Historical context (not authoritative)
|
|-- knowledge_base/
|   |-- ThinkMath_Blueprint_v3.md         <- Source for Pillar 1
|   |-- Advaitian_Master_Framework.txt    <- 20 archetypes + Six-Point Framework
|   |-- Advaitian_Philosophy_Framework.txt
|   |-- Advaitian_White_Paper.txt
|   |-- Advaitian.md
|   |-- Chapter_1_Invariance.txt
|   |-- Seed_Elegance_Connections.txt
|   |-- Masterclass_Problem_Solving.txt
|
|-- my_references/
|   |-- edujeejoshi2ed.pdf                <- K.D. Joshi EJM (primary problem bank)
|   |-- edujeejoshi2ed.txt                <- Searchable text extraction (52,591 lines)
|   |-- extracted_text.txt                <- Earlier extracted reference
|   |-- [3 x .docx files]                 <- Earlier working documents
|
|-- pillar1-framework/                    <- Write last
|-- pillar2-archetypes/
|   |-- 01-invariance.md                  <- Chapter 1 (DRAFTED, Joshi-instrumented)
|   |-- _template/
|       |-- chapter-template.md           <- Canonical scaffold
|       |-- 01-invariance-outline.md      <- Approved outline (historical)
|       |-- 02-symmetry-outline.md        <- NEW: Chapter 2 outline awaiting sign-off
|       |-- joshi-archetype-map.md        <- NEW: 24-chapter to 20-archetype map
|
|-- pillar3-multidirectional/             <- COMPLETE (8 chapters drafted + problems-locked)
|-- pillar4-cep-design/                   <- COMPLETE (9 chapters drafted + slate v0.2.0 + problems-locked v0.2.0)
|   |-- 01-problem-as-art-object.md       <- Ch.1 (5,111 words)
|   |-- 02-anatomy-of-designed-problem.md <- Ch.2 (5,050 words)
|   |-- 03-cep-design-framework.md        <- Ch.3 (6,030 words)
|   |-- 04-case-studies-moderate.md       <- Ch.4 (5,516 words)
|   |-- 05-case-studies-mid.md            <- Ch.5 (6,330 words)
|   |-- 06-case-studies-high-mid.md       <- Ch.6 (6,437 words)
|   |-- 07-case-studies-high.md           <- Ch.7 (6,733 words)
|   |-- 08-case-studies-extreme.md        <- Ch.8 (6,977 words; capstone IMO 1988 P6)
|   |-- 09-design-your-own.md             <- Ch.9 (5,034 words)
|   |-- pillar4-case-study-slate-v0.1.0.md <- v0.2.0 LOCKED (25 cases)
|   |-- pillar4-problems-locked.md        <- v0.2.0 LOCKED (31 distinct problems)
|   |-- _template/chapter-template.md     <- Pillar 4 canonical scaffold (3 chassis types)
|-- pillar5-gems/                         <- 108 target locked; cluster targets set (CURRENT next-pillar)
|
|-- templates/                            <- LaTeX preamble (to be created — Section 12.6)
|-- scripts/                              <- Pandoc build scripts (to be created — Section 12.8)
|-- _overleaf-downloads/                  <- Generated LaTeX .txt files land here
|-- figures/
|-- appendices/
```

---

## SECTION 18 — GLOSSARY OF ADVAITIAN TERMS

A compact reference for the book's specialized vocabulary. Every term here is used precisely throughout the volume; imprecise use is a voice error, not a stylistic choice.

| Term | Definition |
|------|-----------|
| **Advaitian** | From Sanskrit *advaita* (non-dual): the philosophical claim that beneath the multiplicity of problem types lies a single structural reality. |
| **Archetype** | One of the twenty universal structural patterns that account for all solvable mathematical problems at the target difficulty level. Identified by number (1–20) and name. |
| **Archetype Nudge** | An escape-hatch move (§7.8): when stuck, suspect a wrongly chosen archetype and re-run the First-Minute Protocol's archetype-short-list step. |
| **Bhāṣya** | Sanskrit: a structured commentary that reveals the architecture latent in a source tradition. The genre-label for this book. |
| **Brute Path** | The mechanical, expensive approach a student naturally reaches for. Not wrong — only costly, and instructive about what the elegant pivot is not. |
| **CEP (Central Elegant Point)** | The beautiful mathematical object at the heart of a well-designed problem. The solver's destination; the designer's starting point. |
| **Cluster** | One of seven groupings of gems in Pillar 5 (A–G; see Section 9.4). |
| **Commentary mode** | The analytical register of this book: every problem is followed by a structured commentary, not just a solution. Inherited from Joshi's *EJM*. |
| **Convergence** | In multidirectional solving (Pillar 3): the moment when two or three archetype-driven approaches agree, pointing at the same CEP. The structural model is in §7.6. |
| **Direction Map** | An escape-hatch move (§7.8): when stuck, draw the two- or three-archetype convergence diagram explicitly on paper. |
| **Elegant Pivot** | The single insight that collapses the brute path into a clean solution. Named, explained, and shown in full in every six-point commentary. |
| **First-Minute Protocol** | The 60-second silent internal diagnostic run before writing a single equation (§7.7). Identify the given, the find, the active archetypes, the candidate CEP, and the brute path to avoid. |
| **Gem** | One of the 108 specific identities, inequalities, and theorems in Pillar 5 (§9.3) that implement the elegant pivots. Gems are tools; archetypes are lenses. Cited as `[Cluster-letter][NN]`, e.g., A03 or G11. |
| **Meta-principle** | The archetype's one-sentence generalisation, written in domain-general language. Appears in the six-point commentary Seed section. |
| **Mixed-register voice** | The locked voice rule (§3.10): "I" for philosophical interludes, "we" for worked examples, impersonal for definitions. |
| **Monovariant** | A quantity that strictly increases or decreases with each step of a process; used in proofs of termination. A special case of invariance. |
| **MVC (Minimum Viable Commentary)** | Stage 1 of the two-stage commentary process: a conversational paragraph capturing the seed, brute trap, and pivot, written before the full six-point apparatus. |
| **Pillar** | One of the five structural divisions of the book (Section 4). Cited as **Pillar K**, e.g., Pillar 2. |
| **Pivot Shadow** | An escape-hatch move (§7.8): when stuck on a brute computation, continue it just far enough to see the structural shape the elegant pivot would have to take. |
| **Seed** | The underlying structural archetype of a problem, expressed in one domain-general sentence. The first point of the six-point framework. |
| **Six-Point Framework** | The canonical commentary grammar: Seed, Brute Path, Elegant Pivot, Pitfalls, Connections, Takeaway. The output standard for every worked example in the book. |
| **Structural mirror** | The mentor stance: reflecting the reader's own logic back with precision and friction, until the "Aha" moment occurs without being handed. |
| **Takeaway** | The sixth and final point of the six-point commentary: one sentence, under fifteen words, actionable, memorable. The claim is that a student should be able to quote it five years later. |
| **Tier** | One of five developmental levels (0–4; Section 5.8) distinguishing reader readiness, *not* problem difficulty. The book primarily addresses Tiers 3–4 (JEE Advanced → INMO/IMO). |
| **Vieta jumping** | An advanced technique used to prove that a quantity is a perfect square; canonical example: IMO 1988 P6. Treated in Pillar 4 Case Study 25, with a forward-reference from Pillar 2 Chapter 1. |

---

## SECTION 19 — CROSS-REFERENCE AND NUMBERING CONVENTION (NEW)

Stable cross-referencing is essential for a multi-chapter, multi-pillar volume. The following conventions are locked at v2.0 and propagate through every chapter draft.

### 19.1 Section Numbering

- **Pillar-level prefix:** Each pillar contributes a stable letter (`P1`, `P2`, `P3`, `P4`, `P5`).
- **Chapter-level:** Numerical within the pillar. Pillar 2 Chapter 1 → `P2.1`.
- **Section-level:** Decimal within the chapter, mirroring the Markdown `##`/`###` structure. P2.1 §3.2 → `P2.1.3.2`.

In running text, the shorter form is permitted ("§3.2" within the same chapter, "Pillar 2 Chapter 1 §3.2" across chapters, "P2.1.3.2" in the index).

### 19.2 Theorem / Proposition / Definition Numbering

Numbered **per chapter**, restarting at each chapter. A chapter's first theorem is `Theorem 1`, its first definition is `Definition 1`, etc. The LaTeX preamble (§12.6) sets this up via `[chapter]` counter scope.

Cross-pillar references: "Theorem P3.2.4" means Pillar 3, Chapter 2, Theorem 4.

### 19.3 Problem Numbering

Per chapter, in the form `5.K` where 5 is the practice-problems-section number and K is the problem number (1–7). The Pillar 2 Chapter 1 PP3 is `Problem 5.3` (read aloud as "Problem 5.3 of Chapter 1").

Cross-pillar: "P2.1 Problem 5.3" or, in the index, simply "Inv-5.3" using the archetype-prefix shorthand.

### 19.4 Equation Numbering

**Sparse.** Equations are numbered only when they are referenced later in the same chapter or in a forward-pointing footnote. The discipline: write the equation without a number first; add the number only when a downstream reference requires it.

This avoids the "every equation is numbered" anti-pattern that makes the book read like a research monograph rather than a teaching volume.

### 19.5 Forward and Backward References

Forward references (to material not yet read):
- Form: *"(See §X.Y of Pillar K, treated later in this book.)"*
- Used sparingly; only when the forward concept is genuinely needed to understand the current discussion.

Backward references (to material already covered):
- Form: *"(See §X.Y above.)"* or *"(See Pillar K Chapter L §X.Y.)"*
- Used freely; reinforces structural memory in the reader.

Pillar 5 gem references from earlier pillars: see Section 9.5.

### 19.6 Citation of Masters

Inline citation of one of the nine masters uses the form:

> *"As Polya (1945) observes, ..."*

with a single bibliography entry per master at the volume's end. The nine-master citation system is intentionally lighter than a research-monograph bibliography — the masters are *interlocutors*, not sources of literal quotations.

### 19.7 Internal Index Tags

Every problem in the book carries a YAML front-matter tag for its archetype use:

```yaml
problem_id: P2.1.WE1
archetypes: [1, 9]
tier: 1
source: "JEE 1989"
```

The build pipeline (§12.8) extracts these tags and assembles an archetype-indexed appendix that lets a reader find all problems using, say, archetype #1 + archetype #9 in combination.

---

## SECTION 20 — THE READER'S PROGRESSION MODEL (NEW)

How a single reader — the JEE Advanced aspirant of Section 1.5 — moves through the book over a sustained period of months.

### 20.1 The Recommended Path

The book is **not** structured for linear reading cover to cover (though linear reading is supported). It is structured for a *spiral* path: the reader cycles through the pillars at progressively higher tiers of fluency.

**First pass (months 1–3):** Pillar 2 Chapters 1–10. Read for *recognition*, not yet for fluency. Each chapter's WE1 + WE2 + PP1–PP4 is the reader's working diet. PP5–PP7 are skipped on first pass.

**Second pass (months 4–6):** Pillar 2 Chapters 11–20 (full) + Pillar 3 Chapters 1–4. The vocabulary is in place; the reader is now ready for the multidirectional grammar. Pillar 3 reading interleaves with Pillar 2 PP5–PP7 (the stretch problems re-attempted with the multidirectional lens).

**Third pass (months 7–9):** Pillar 3 Chapters 5–8 + Pillar 4 Chapters 1–4 (cases 1–10). The reader is now solving olympiad-tier problems with the convergence apparatus; Pillar 4 begins introducing the *designer's* perspective.

**Fourth pass (months 10–12):** Pillar 4 Chapters 5–9 (cases 11–25) + Pillar 5 (as reference). The reader operates at Tier 4 — reverse-engineering problems from CEPs, with the Gem catalog as an operational reference rather than reading material.

**Capstone (months 13+):** Re-read Pillar 1. The meta-grammar now feels like a recognition rather than an imposition, exactly as Section 4 promised.

### 20.2 Per-Chapter Self-Testing Rhythm

Each Pillar 2 chapter ends with a Self-Assessment Checklist (Pillar 2 chapter scaffold §8). The reader uses these as gating signals:

- **All checkpoints unhesitating:** proceed to next chapter.
- **One or two unhesitating:** re-read the chapter's §1 (plain-language intro) and §4 (worked examples). Do not advance to next chapter.
- **More than two failures:** the chapter is not yet absorbed. Wait a week, re-attempt.

The discipline: *recognition* before progress. A reader who has not internalised Chapter $K$ is not ready for Chapter $K+1$.

### 20.3 The Coach / Teacher Reader

Although the book's anchor reader is the student (Section 1.5), it can be used by a coach. The coach's path:
- **Read all of Pillar 1 first** (treats the meta-grammar as the teaching framework).
- **Read all of Pillar 2 in one pass** (assimilate the full vocabulary).
- **Use Pillar 3 as the teaching geometry**: each chapter maps to a 1–2-week coaching unit.
- **Use Pillar 4 as the elite-track**: case studies become coach-led seminars.
- **Use Pillar 5 as a teaching reference**: gems are tools to assign to students by gap.

The book contains no separate "coach's edition"; the same volume serves both readers, with the coach's depth-pass replacing the student's recognition-pass.

### 20.4 Anti-Patterns the Book Resists

- **Skim-and-skip:** the book is not designed for chapter-flipping. The chapter scaffold (Pillar 2 §6.4) is a *progressive* unfolding that breaks under selective reading.
- **Solve-without-reading:** the practice problems do not stand alone; the worked examples and the §1–§3 exposition are the necessary scaffolding. A reader who only does practice problems is using the book as a problem bank — which it explicitly is not (Section 1.2).
- **Memorization-over-recognition:** the Six-Point Framework is not a recipe to memorize; it is a grammar to internalise. The book repeatedly reminds the reader that the goal is *seeing*, not *remembering*.

---

## SECTION 21 — PRODUCTION CADENCE AND VERIFICATION (NEW)

How the book is written, verified, and released.

### 21.1 Roles

- **Author (Anand Venkat):** owns mathematical correctness, pedagogical strategy, voice authority, and all final commits.
- **AI co-author (Claude Opus 4.7):** owns drafting velocity, structural editing, cross-pillar consistency, citation checking, and build-pipeline construction.

The split is structurally important: AI cannot certify a mathematical claim. Every theorem, every solution, every problem statement is Anand-verified before it leaves draft status.

### 21.2 Drafting Cadence

**Per chapter (typical):**

1. *Outline.* AI produces an outline using the canonical template. ~1–2 sessions.
2. *Outline sign-off.* Anand reviews; flagged decisions are resolved.
3. *Draft.* AI produces a complete chapter draft, citing all sources, flagging all uncertainties. ~3–5 sessions for a Pillar 2 chapter.
4. *Mathematical verification.* Anand reads every theorem, every worked example, every solution. Marks corrections.
5. *Revision.* AI applies corrections; produces revised draft.
6. *Voice pass.* AI runs the §10.3 voice checkpoint; Anand reviews any flagged register inconsistencies.
7. *Commit and move on.* The chapter is marked `status: review` in its YAML front matter.

**Per pillar:**

8. After all chapters in a pillar are at `status: review`, Anand reads the entire pillar end-to-end for cross-chapter consistency. AI prepares the consistency-check report (cross-reference validity, voice consistency, citation consistency).
9. Pillar is then bumped to `status: locked`.

**Volume-level:**

10. Once all five pillars are at `status: locked`, AI performs the final editorial pass (citation audit, length-budget audit, index assembly, glossary expansion, bibliography compilation).
11. Anand performs the final read-through.
12. Build pipeline (§12.8) produces the camera-ready PDF.

### 21.3 Verification Levels

| Level | Verifier | Standard |
|---|---|---|
| Spelling / grammar | AI (automated) | Standard linting |
| Citation correctness | AI (automated) | Every citation traceable to `my_references/` or named-master reference |
| Mathematical correctness | **Anand (always)** | Every theorem proven; every solution worked; every claim verifiable |
| Voice consistency | AI + Anand | §10.3 voice checkpoints + Anand's editorial ear |
| Pedagogical adequacy | **Anand (always)** | Does this chapter teach what it claims to? |
| Cross-pillar consistency | AI (automated via build) | No archetype #X redefined between pillars; no gem cited that does not exist |

### 21.4 The Math-Correctness Floor (non-negotiable)

The book's *single hardest commitment*: every mathematical claim must be verifiable. The ThinkMath.ai project established the principle ("the Bible accepts uncertainty, it does not accept falsehood"); the book inherits it.

In practice:

- AI never publishes a mathematical claim without it being Anand-verified.
- When AI is uncertain, the draft contains an explicit flag (e.g., *"⚠️ Anand: please verify"*) rather than a guess.
- The book contains no "left to the reader" handwave that masks an AI uncertainty. If the proof is non-obvious, it is shown in full or genuinely deferred to a cited source.

### 21.5 Volume 1 Release Criteria

The book is ready for publication when:

- All five pillars are at `status: locked`.
- Every problem has a verified citation.
- Every theorem has either a proof in the text or a cited canonical proof.
- The bibliography is complete and verified.
- The index is generated, cross-checked, and human-reviewed.
- The build pipeline produces a deterministic, reproducible PDF.
- A pre-publication reading (Anand + 1–2 external readers) finds no mathematical errors and no major voice inconsistencies.

There is **no fixed release date**. The release criterion is *quality*, not *time*.

---

*End of Blueprint.*

**Version:** 2.0 — May 26, 2026  
**Previous version:** 1.0 — May 13, 2026 (Day 1)  
**Next review:** After Chapter 2 (Symmetry) outline sign-off and Chapter 2 enters draft. v2.1 will reflect any further decisions surfaced during Chapter 2 drafting.

*This document is the fixed point. When in doubt, return here.*

🌑
