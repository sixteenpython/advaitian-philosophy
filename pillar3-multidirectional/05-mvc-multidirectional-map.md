---
chapter: 5
pillar: 3
title: "The MVC as a Multidirectional Map"
subtitle: "*Drawing the Solution Before You Write It.*"
length_target_words: 6000
canonical_takeaway: "The First-Minute Protocol is silent; the MVC is visible. The protocol lives in working memory; the MVC lives on paper. The Pillar 3 solver uses both."
status: draft
last_revised: 2026-05-28
references_invoked: [Zeitz-ch-1, Engel-ch-4, Engel-ch-8, IMO-1988-P6, Polya-1945]
canonical_constructs_used: [first-minute-protocol, convergence-diagram, mvc-sketch]
---

# Chapter 5 — The MVC as a Multidirectional Map

*Drawing the Solution Before You Write It.*

---

## §0 Opening Vignette — Priyanka Mukherjee's research notebook

It is a Tuesday afternoon in late September at the Indian Statistical Institute, Kolkata. Priyanka Mukherjee, a third-year PhD student in algebraic geometry, is sitting in the visitor's office her advisor reserves for graduate students, working on a problem from a recent preprint. The problem is well above the JEE/INMO level — it is a research problem about the dimension of a particular moduli space — but the *cognitive shape* of her work would be instantly recognisable to any Pillar 3 reader.

On her desk is a notebook open to a left-hand page. The page contains no equations. Instead, it has a half-page diagram in pencil:

```
                       ┌──────────────────────────┐
                       │  Moduli space M(d, g)    │
                       │  Find: dim M = ?         │
                       └────────────┬─────────────┘
                                    │
        ┌───────────────────────────┴───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
┌──────────────────┐    ┌──────────────────────┐    ┌────────────────────┐
│ DEFORMATION TH'Y │    │ EULER SEQUENCE       │    │ RIEMANN-ROCH       │
│ (TRIED — partial)│    │ (TRIED — half-works)  │    │ (NOT YET TRIED)    │
│ Gives lower bnd  │    │ Cohomology vanishes  │    │ Should give        │
│ but not equality │    │ for one piece, but    │    │ exact formula?     │
│                  │    │ not the other         │    │ ⇒ try Monday      │
└──────────────────┘    └──────────────────────┘    └────────────────────┘

         (3 archetypes; convergence point not yet identified;
          next move: try Riemann-Roch on the Monday meeting)
```

Priyanka's diagram occupies the entire upper half of the notebook page. Below it, in smaller writing, are her notes on what each archetype has produced — partial computations, dead ends, lemmas that almost-but-not-quite close. The diagram is *not* the solution. The diagram is the *map of the search*. It externalises what she has tried, what she has not yet tried, and where the candidate convergence point should appear.

Her advisor, Professor Sengupta, walks past her office at 4:30 p.m. He glances at the diagram for about ten seconds and immediately says: *"You're missing the fourth archetype. The deformation-theory lower bound and the Euler-sequence partial vanishing both depend on the canonical bundle's degree — you need a Hurwitz-formula computation to relate them. Try that."* He walks on.

Priyanka does not need to ask what he means. The advisor and the student communicate *through the diagram* — the diagram has compressed twelve days of work into a half-page representation that a fellow expert can read in ten seconds. The advisor's suggestion is a *fourth archetype* to add to the diagram, with its own intermediate result that should converge with the existing three. Priyanka pencils in the new box.

This is the **MVC — the Mental Visualization Canvas** — used in its most developed form: as the *primary record* of how a problem is being thought about, more important to the researcher than the eventual proof. In its olympiad form (which is what this chapter develops), the MVC is smaller and faster, but it is the same cognitive object. The MVC is the externalised, drawn version of the First-Minute Protocol. Where the Protocol is silent and internal, the MVC is visible and shareable. Where the Protocol lives in 60 seconds of working memory, the MVC lives in a half-page diagram that persists across days or weeks of work.

**This is the chapter that makes the multidirectional thesis drawable.**

---

## §1 The Pattern

### §1.1 What the MVC is, and what it is not

The **Mental Visualization Canvas (MVC)** is a single drawn diagram — typically half a page, occasionally a full page for very hard problems — that contains four classes of element:

1. **The problem-statement box** (top of the diagram): a one-sentence compression of the problem's Given and Find. This is the same content as the Protocol's Steps 1–2, but drawn rather than listed.

2. **Archetype-application nodes** (the boxes downstream of the problem statement): one box per archetype the solver has considered. Each box is annotated with three sub-items — the archetype name (#-numbered per Pillar 2), the *intermediate result* the archetype has produced (or "TBD" if the archetype is in queue), and a *status marker* (✓ closed | ⚠ partial | ? not yet tried | ✗ tried and failed).

3. **Convergence nodes** (the diamond-shaped or rounded-corner boxes where multiple archetype-arrows meet): each convergence node is annotated with what it *should let you say* — the intermediate result that the convergence produces, or the CEP if the convergence is the final step.

4. **The answer node** (bottom of the diagram): the final answer, boxed and underlined. Initially this is a "TBD" placeholder; it becomes the actual answer once the proof closes.

The MVC is **not**:
- A formal proof. The MVC contains no equations beyond the most compact intermediate-result expressions. A proof has to be written separately, in standard mathematical prose.
- A flowchart. A flowchart prescribes *what to do in what order*. The MVC describes *what has been tried and what still needs to be tried* — it is a state diagram, not a control diagram.
- A mind map. A mind map is associative and unstructured. The MVC is structural — it follows the §7.6 convergence-diagram grammar of Chapter 1, with archetype-application nodes feeding into convergence nodes feeding into the answer node.
- A *replacement* for the First-Minute Protocol. The Protocol and the MVC are complements: the Protocol is the diagnostic that *initialises* the MVC, and the MVC is the externalisation that *sustains* the Protocol's output across the longer arc of a hard problem.

### §1.2 Stage 1 (mapping) versus Stage 2 (computation)

The MVC partitions problem-solving into two cognitive stages:

**Stage 1 (mapping).** The solver builds the MVC — fills in the problem-statement box, sketches the candidate archetype-application nodes, draws the convergence-node positions. The MVC at the end of Stage 1 is *incomplete*: some archetype boxes are marked "?" (not yet tried), some convergence nodes are "TBD", the answer is "TBD". Stage 1 is essentially a *planning* stage; it produces no equations, only structure. For a hard problem, Stage 1 may take 2–5 minutes (significantly longer than the First-Minute Protocol's 60-second budget, because the MVC is more elaborate).

**Stage 2 (computation).** The solver attacks the archetype boxes one at a time, in an order suggested by the MVC's structure — typically *easiest archetype first, hardest archetype last*. Each successful archetype-application updates its node from "?" or "⚠" to "✓" and fills in the intermediate-result annotation. The solver returns to the MVC repeatedly throughout Stage 2 to track progress; the MVC functions as a *checklist* of remaining work and a *map* of what has been completed.

The Stage 1 / Stage 2 split is the cognitive economy that makes the MVC work. Stage 1 happens entirely on paper, freeing working memory; Stage 2 happens partly in working memory (the current computation) and partly on paper (the rest of the map). The solver's working memory at any moment holds *only* the current intermediate result, not the full map. This is the precise mechanism by which the MVC scales to 3-archetype and even 4-archetype problems (research-level): the cognitive load is *spatial*, not *temporal*.

### §1.3 The MVC and Zeitz's three-layer model

Paul Zeitz, in *The Art and Craft of Problem Solving* (3rd ed., 2017), Chapter 1 §1.2, articulates a three-layer model of problem-solving that maps almost exactly onto the Advaitian architecture:

| Zeitz layer | Definition (Zeitz) | Advaitian counterpart |
|---|---|---|
| **Strategies** | High-level approaches: "wishful thinking," "make it easier," "draw a picture" | **Pillar 1 (Six-Point Framework) + Pillar 3 meta-moves** (Protocol + MVC + Escape-Hatch) |
| **Tactics** | Mid-level techniques: invariants, parity, extreme principle, induction | **Pillar 2 (Twenty Archetypes) + Pillar 3 multidirectional moves** (2-archetype + 3-archetype convergence) |
| **Tools** | Low-level computational facts: factorisations, identities, named theorems | **Pillar 5 (Mathematical Gems)** |

The MVC, in Zeitz's terminology, is a *strategic tool* — it operates at the top layer, organising the application of tactics (archetypes) and tools (gems) in service of the problem. Zeitz himself does not name the MVC explicitly, but his exhortation throughout his book to "draw a picture" and to "write down what you know" is the same idea in less-developed form. What Pillar 3 adds is the *grammar* (convergence-diagram structure inherited from §7.6), the *vocabulary* (archetype-numbered nodes), and the *operational integration* with the First-Minute Protocol and the Escape-Hatch Architecture.

The historical lineage is therefore: Polya (1945, "draw a figure") → Zeitz (1999, "draw a picture, write down what you know") → Pillar 3 MVC (2026, the structured externalisation tool with explicit grammar and integrated protocol).

### §1.4 When the MVC is worth the time

The MVC takes 2–5 minutes to build (Stage 1) before any computation. For very easy problems (single-archetype, solvable in 5 minutes total), this overhead is not worth it — the First-Minute Protocol alone (60 seconds) suffices. The threshold rule:

- **1-archetype problems:** First-Minute Protocol only. MVC is overkill.
- **2-archetype problems:** Protocol + a minimal "mental MVC" (held in working memory). Drawing on paper is optional; many solvers can hold a 2-archetype convergence-diagram in working memory.
- **3-archetype problems:** Protocol + **explicit drawn MVC**, mandatory. The cognitive-hardware argument of Chapter 3 §1.2 (working memory overflows at 3 archetypes) forces the MVC.
- **4+ archetype problems (research-level):** Protocol + **persistent, multi-day MVC** kept in a notebook (as in Priyanka's vignette). The MVC becomes the primary record of the work.

The Pillar 3 solver internalises this threshold as a reflex: as soon as the First-Minute Protocol's Step 3 lists three or more candidate archetypes, the solver picks up a fresh sheet of paper and draws the MVC. The reflex is the operational difference between Pillar 3 solvers and untrained solvers; it is the difference Priyanka demonstrated in the opening vignette.

---

## §2 Worked Examples

We develop three worked MVCs. The first is a 2-archetype problem with a minimal mental-MVC (no drawing required). The second is a 3-archetype problem with a full drawn MVC. The third is an MVC-revision case: the initial MVC was wrong, and the chapter shows how the revision happens.

### Worked Example 5.1 — A 2-archetype MVC (Engel Ch. 4 E11, retreated)

*Source.* Engel, *Problem-Solving Strategies*, Ch. 4 Example E11 (p. 62). Same problem as Chapter 4 Worked Example 4.1 (the 9-rugs problem) — re-treated here through the MVC lens to demonstrate that a 2-archetype problem can be solved with a *mental MVC* (no drawing required).

**Problem.** Inside a room of area 5, you place 9 rugs, each of area 1 and arbitrary shape. Prove that two rugs overlap on a region of area at least $1/9$.

**The mental MVC (held in working memory, not drawn on paper):**

The solver, having run the First-Minute Protocol in 60 seconds, has the following in working memory:

```
Problem: 9 rugs of area 1 in room of area 5; ∃ pair overlap ≥ 1/9
  ↓
  ├─ #13 Combinatorial: sum-of-rug-areas = 9; room = 5; excess = 4
  │   intermediate result: sum of pairwise overlaps ≥ 4
  │
  └─ #12 Extremal: ⊞ pairs = C(9,2) = 36
      intermediate result: max overlap ≥ excess/pairs = 4/36 = 1/9
  ↓
  Convergence: max overlap ≥ 1/9 ⇒ done
```

This entire MVC lives in working memory for the duration of the proof. The solver does *not* draw it on paper, because at 2 archetypes the cognitive load is within working-memory capacity. The proof is written as ordinary mathematical prose, with the MVC providing the silent backbone.

**Commentary — when *not* to draw.** The pedagogical point is *negative*: for 2-archetype problems, drawing the MVC is unnecessary work. Pillar 3 discipline is not "always draw the MVC" but "draw the MVC when working memory is about to overflow." Recognising when working memory will overflow is the meta-skill; it correlates strongly with archetype-count (per §1.4 threshold).

### Worked Example 5.2 — A 3-archetype MVC (IMO 1988 P6, retreated)

*Source.* IMO 1988 Problem 6; Engel Ch. 8 Problem 6 (p. 207). Same problem as Chapter 3 Worked Example 3.1 — re-treated here as a full drawn MVC, showing the externalisation that Karthik (Ch. 3 §0) failed to perform for 2.5 hours.

**Problem.** Let $a, b$ be positive integers with $ab + 1 \mid a^2 + b^2$. Show $k = (a^2 + b^2)/(ab + 1)$ is a perfect square.

**The drawn MVC (Stage 1 output, ~3 minutes of pencil-on-paper work):**

```
       ┌───────────────────────────────────────────────────┐
       │ Problem: ab+1 | a²+b² ⇒ k=(a²+b²)/(ab+1) is square│
       │ Given: a,b ∈ ℤ₊; Find: k = m² for some m ∈ ℤ      │
       └─────────────────────────┬─────────────────────────┘
                                 │
       ┌─────────────────────────┼─────────────────────────┐
       │                         │                         │
       ▼                         ▼                         ▼
┌───────────────────┐  ┌────────────────────┐  ┌─────────────────────┐
│ #18 INDUCTION     │  │ #16 REVERSE ENG.   │  │ #1 INVARIANCE       │
│ status: ? → ⚠    │  │ status: ? → ⚠     │  │ status: ? → ✓       │
│ shape: descent on │  │ shape: Vieta jump  │  │ k preserved under   │
│ a+b               │  │ on quadratic in a  │  │ the jump            │
│ next: pick min-bad│  │ next: apply Vieta  │  │ (this is the easy   │
│                   │  │ to a²−(kb)a+(b²−k) │  │  one — do first)    │
│                   │  │ = 0                │  │                     │
│ int. result TBD   │  │ int. result TBD    │  │ ✓ done              │
└─────────┬─────────┘  └──────────┬─────────┘  └──────────┬──────────┘
          │                       │                       │
          │ ⇒ a+b minimal         │ ⇒ a' = kb−a           │ ⇒ (a',b)
          │   for some bad pair   │   = (b²−k)/a          │   has same k
          │                       │   (jumped pair)       │
          │                       │                       │
          └───────────────────────┼───────────────────────┘
                                  │
                                  ▼
              ┌─────────────────────────────────┐
              │ Convergence node 1 (TBD):       │
              │ Combine the three results to    │
              │ show (a',b) is "smaller" but    │
              │ same-k — contradicting          │
              │ minimality                      │
              └────────────────┬────────────────┘
                               │
                               ▼
              ┌─────────────────────────────────┐
              │ Convergence node 2 (CEP, TBD):  │
              │ Sign analysis: a' ≥ 0 forces    │
              │ a' < a or a' = 0; the second    │
              │ case gives k = b² (a square)    │
              └────────────────┬────────────────┘
                               │
                               ▼
                    ┌────────────────────┐
                    │ ANSWER: k is m²    │
                    └────────────────────┘
```

**Stage 2 (computation): work the archetype boxes in order.**

The MVC's order suggestion: do the "easiest" archetype first to free working memory for the harder ones. The order:

1. **#1 Invariance (easy):** Verify that the quotient $k$ is preserved under the jump $(a, b) \to (a', b)$. This follows immediately from the symmetry of the quadratic $x^2 - (kb) x + (b^2 - k) = 0$ in its two roots. Update node from "?" to "✓". *Working time: ~2 minutes.*

2. **#16 Reverse Engineering (medium):** Apply Vieta's formulas to compute $a' = kb - a = (b^2 - k)/a$. Verify $a'$ is an integer (from Vieta's, since $k, b, a$ are integers and $a + a' = kb$). Update node from "?" to "⚠" (partial — sign of $a'$ not yet determined). *Working time: ~3 minutes.*

3. **#18 Induction (hard):** Pick a minimal-bad-pair $(a, b)$ with $a \geq b > 0$. Argue that $(a', b)$ must also be bad if it is a valid pair. Update node to "⚠" (the descent has not yet contradicted itself; the contradiction depends on the convergence node). *Working time: ~3 minutes.*

4. **Convergence node 1:** Combine the three intermediate results to argue: $(a', b)$ is same-$k$, but $(a', b)$ should have $a' + b < a + b$, contradicting minimality — *unless* $a' \leq 0$, which is the special case that needs separate sign-analysis. Update convergence node from "TBD" to the sign-analysis sub-checklist. *Working time: ~3 minutes.*

5. **Convergence node 2 (the CEP):** Run the three sign-analysis sub-arguments — $a' \neq 0$ forces $k = b^2$ (a square, contradicting "$k$ not a square"); $a' < 0$ impossible by direct sign-of-equation argument; $0 < a' < a$ forced, contradicting minimality. The only consistent case is $a' = 0$, which makes $k$ a square. Update CEP node from "TBD" to the boxed answer. *Working time: ~5 minutes.*

**Total time, MVC + Stage 2: ~18 minutes.** (Compare with Karthik's 2.5 hours in Chapter 3 §0, before he drew the MVC.) The drawn MVC compressed the proof structure into visible form, allowing the solver to work each archetype in the order best suited to working-memory load — and to refer back to the map whenever the convergence point felt slippery.

**Commentary — the order of archetype-work.** The MVC's most underappreciated value is *prescribing the order of work*. Without the MVC, a solver tends to attack archetypes in the order they were thought of — usually attacking the "most exciting" archetype first. With the MVC, the solver picks the *easiest* archetype first, banks the result, and uses the freed working memory for the harder archetypes. Karthik's 2.5-hour failure was largely a failure of *work ordering*: he attacked the descent (hardest) before he had banked the invariance (easiest), so the descent argument depleted his working memory without the invariance bridge ready to be invoked at the convergence point. The MVC fixes this by making the relative-difficulty of archetypes visible.

### Worked Example 5.3 — MVC revision (the MVC was wrong)

*Source.* A composite illustration drawn from the Czech & Slovak 1995 problem (Zeitz Ex 6.1.1, used in Ch. 1 WE3 and Ch. 4 WE2), but with a *deliberately misdiagnosed* initial MVC to illustrate the revision process.

**Problem.** Decide whether there exist 10,000 ten-digit numbers, each divisible by 7, all of which are obtainable from one another by reordering their digits.

**The initial MVC (incorrect Stage 1 output).** Suppose the solver, having read the problem too fast, initially identifies the wrong archetype pair:

```
       ┌───────────────────────────────────────────────────┐
       │ ∃ 10,000 ten-digit divisible-by-7 numbers, all   │
       │ digit-permutations of each other?                 │
       └─────────────────────────┬─────────────────────────┘
                                 │
       ┌─────────────────────────┴─────────────────────────┐
       │                                                   │
       ▼                                                   ▼
┌───────────────────┐                          ┌──────────────────────┐
│ #11 EXISTENCE      │                          │ #5 SUBSTITUTION       │
│ status: ?         │                          │ status: ?             │
│ shape: prove ∃    │                          │ shape: parameterise   │
│ by construction   │                          │ all 10-digit nums by  │
│ next: find example│                          │ next: write n =       │
│                   │                          │   Σ dᵢ·10^i           │
│ int. result TBD   │                          │ int. result TBD       │
└─────────┬─────────┘                          └──────────┬───────────┘
          │                                               │
          └───────────────────┬───────────────────────────┘
                              ▼
              ┌─────────────────────────────────┐
              │ Convergence (TBD): find a       │
              │ multiset whose parameterisation │
              │ gives 10,000 perms              │
              └─────────────────────────────────┘
```

The solver works this MVC for ~15 minutes. The Existence archetype produces "we need to construct *some* multiset" (vacuous — could be any of millions); the Substitution archetype produces an explicit formula $n = \sum d_i \cdot 10^i$ (correct but useless without further structure). The convergence node remains "TBD" — the two intermediate results do not combine.

**Trigger for revision.** The solver, recognising the 15-minute stall, runs the *Direction Map* Escape-Hatch move (Ch. 2 §3): *redraw the MVC; label what each archetype's intermediate result should let you say; check whether the labels actually compose into a proof*. The check fails — the "explicit formula for $n$" and the "construct *some* multiset" labels do not compose into a divisibility-by-7 conclusion.

**The revised MVC (correct Stage 1 output).** The solver replaces the wrong archetype pair with the right one — *#13 Combinatorial (counting permutations of a multiset) + #14 Parity/Modularity (divisibility by 7 via position-weighted sum mod 7)*:

```
       ┌───────────────────────────────────────────────────┐
       │ ∃ 10,000 ten-digit divisible-by-7 numbers, all   │
       │ digit-permutations of each other?                 │
       └─────────────────────────┬─────────────────────────┘
                                 │
       ┌─────────────────────────┴─────────────────────────┐
       │                                                   │
       ▼                                                   ▼
┌───────────────────┐                          ┌──────────────────────┐
│ #13 COMBINATORIAL │                          │ #14 PARITY/MOD       │
│ status: ✓         │                          │ status: ⚠            │
│ Mississippi:      │                          │ 10^i mod 7 cycles    │
│ 10!/Πmᵢ! ≥ 10,000│                          │ as (1,3,2,6,4,5,...) │
│ for mild multi-   │                          │ length 6             │
│ plicities         │                          │ int. result: position│
│ ✓ ≥ 10,000 perms  │                          │   pairs (i,i+6) for  │
│                   │                          │   i=0..3 have same w │
└─────────┬─────────┘                          └──────────┬───────────┘
          │                                               │
          └───────────────────┬───────────────────────────┘
                              ▼
              ┌─────────────────────────────────┐
              │ Convergence: construct a multi- │
              │ set with paired-position        │
              │ symmetry so all perms ≡ 0 (7)   │
              └─────────────────────────────────┘
```

The revised MVC works (Stage 2 proceeds as in Ch. 1 WE3 / Ch. 4 WE2, subject to the open-item flag on the explicit multiset). **Total wall-clock time: ~25 minutes, of which 15 minutes was the wrong-MVC dead-end and 10 minutes was the revised-MVC successful proof.**

**Commentary — the MVC is itself diagnosable.** The MVC's most-useful property in failure cases is that *it is itself an object that can be inspected*. The wrong-MVC's convergence node is "TBD" *because the two intermediate results don't combine* — and that very fact (TBD persists after 15 minutes of work) is the diagnostic signal. Without the MVC, the solver has no externalised object to inspect; they only have the slowly-mounting frustration of "this isn't working." The MVC turns the frustration into a *visible*, *actionable* diagnostic — *"my convergence node has been TBD for 15 minutes; the archetype pair is wrong."* The Direction Map move (Ch. 2 §3) and the MVC are designed to work together exactly this way: Direction Map is the *trigger*; MVC revision is the *response*.

---

## §3 The Trap — The over-detailed MVC

The principal failure mode of the MVC is *over-detailing*. The over-detailed-MVC solver, having internalised the MVC as a useful tool, attempts to put the *entire solution* into the MVC — all the algebra, all the case analyses, all the named-theorem invocations — instead of restricting the MVC to its proper scope (archetype names, intermediate-result labels, convergence-node positions).

The signature of the over-detailed-MVC trap: the MVC overflows the half-page budget within 10 minutes; the solver starts writing in tiny script in the margins; the diagram becomes unreadable; the cognitive externalisation benefit *inverts* (now the MVC is itself cluttering working memory rather than freeing it). Within 20 minutes, the solver abandons the MVC entirely and reverts to in-head proof attempts — with the worst of both worlds: the MVC's time-cost (~5–10 minutes) was paid, but the MVC's benefit was lost.

**Why does over-detailing happen?** Three causes:

1. *Aesthetic over-investment.* The MVC, once drawn, becomes a *visible artefact* of the solver's work. Solvers naturally want the artefact to look complete — to contain "the answer," not just "the map to the answer." Resisting this aesthetic urge is a discipline.

2. *Confusion between the MVC and the proof.* New MVC users sometimes treat the MVC as a draft of the proof itself, to be polished into the final write-up. The MVC is *not* a draft of the proof; it is the *plan* for the proof. The proof is written separately, in prose, *guided by* the MVC.

3. *Working-memory-leak.* When an archetype's intermediate result is genuinely complex (e.g., the Vieta-jump's full sign analysis from Worked Example 5.2), the solver may try to externalise the complex computation *into* the MVC's intermediate-result annotation. This makes the MVC node-label too long to fit in the box; the solver writes around the box; the structure of the MVC is disrupted.

**The recovery move: enforce the half-page budget.** The MVC discipline is *spatial*: one sheet of paper, half a page maximum, three to four archetype boxes maximum. If the MVC starts to overflow, the solver pauses, transfers the overflowing details into a separate "scratch sheet" (where Stage-2 computations live), and re-draws the MVC fresh on a new half-page with the cleaner annotations. The re-drawing takes 2–3 minutes; the recovery is worth it. With practice, solvers internalise the half-page budget as a hard constraint and the over-detailing trap fades within 20–40 problems.

**A worked illustration of over-detailing.** Suppose the IMO 1988 P6 MVC from Worked Example 5.2 was over-detailed by the solver attempting to *write the full sign-analysis* (the three sub-arguments for $a' = 0$, $a' < 0$, $0 < a' < a$) inside the Convergence-Node-2 box. The box overflows; the solver writes the sign-analysis algebra around the box; the MVC's downstream answer node gets disconnected from the convergence node visually. The solver, looking at the cluttered MVC, loses track of which sub-argument they have completed and which they have not. The eventual proof has a gap (sub-argument (ii) skipped) because the over-detailed MVC obscured the completion checklist.

The recovery: re-draw the MVC with the Convergence-Node-2 label as *"sign analysis: 3 sub-args (i), (ii), (iii)"* — a single line. Move the actual sub-argument algebra to a separate scratch sheet, marked *"Sign analysis for Conv-2, IMO 1988 P6"*. The MVC reverts to its clean half-page form; the scratch sheet holds the computational details; the proof is written from the combination of MVC + scratch sheet.

The lesson: **the MVC contains structure, not content.** Content lives on scratch sheets. Confusing the two — putting content into the MVC — is the over-detailing trap.

---

## §4 Practice Problems

Four problems on which the reader is asked to produce an MVC *first*, then attempt the solution. For the first two problems (2-archetype), a mental MVC is acceptable; for the last two (3-archetype), a drawn MVC is required.

**Practice Problem 5.1.** *(2-archetype; mental MVC acceptable.)* Show that among any $n + 1$ integers chosen from $\{1, 2, \ldots, 2n\}$, two are such that one divides the other. *Source: Erdős's "two integers" theorem; Engel Ch. 4.* *Archetypes: #13 Combinatorial (pigeonhole) + #4 Hidden Structure (every integer in $\{1, \ldots, 2n\}$ can be written uniquely as $2^a \cdot m$ with $m$ odd; there are exactly $n$ odd $m$ in the range).*

**Practice Problem 5.2.** *(2-archetype; mental MVC acceptable.)* Prove that for any positive integer $n$, the integer $n^5 - n$ is divisible by 30. *Source: Classical (every textbook). Archetypes: #14 Parity/Modularity (divisibility) + #1 Invariance (Fermat's Little Theorem for $p = 2, 3, 5$).*

**Practice Problem 5.3.** *(3-archetype; drawn MVC required.)* Determine all positive integers $n$ for which the equation $x^n + y^n = z^n$ has a non-trivial positive-integer solution. *Source: This is Fermat's Last Theorem; the practice-problem framing is deliberately ambitious — the reader is asked to **draw the MVC** showing the three (or more) archetypes one would invoke, not to actually prove the theorem.* *Suggested archetype shortlist: #14 Parity/Modularity (mod-$p$ obstructions for small $n$) + #16 Reverse Engineering (Fermat's own descent for $n = 4$) + a third research-level archetype to be left blank in the student's MVC.*

> ⚠ *Open item — Anand sign-off pending.* The framing of PP 5.3 as an "MVC exercise on Fermat's Last Theorem" is unusual and may not survive review. Author current intent: use the MVC to illustrate the *limits* of multidirectional analysis — Fermat's Last Theorem requires research-level archetypes (Galois representations, modular forms) that lie beyond Pillar 2's twenty. The MVC, in this case, *should remain incomplete*; the lesson is that the MVC honestly displays the incompleteness rather than concealing it. Final lock at chapter-final-review.

**Practice Problem 5.4.** *(3-archetype; drawn MVC required.)* In a circle of radius 1, six points are placed. Prove that some two of the six points are within distance 1 of each other. *Source: Engel Ch. 4 or Zeitz §3.x; classical pigeonhole-and-geometry result.* *Suggested archetype shortlist: #13 Combinatorial (pigeonhole on 6 sectors of $60°$ each) + #12 Extremal (the chord of a $60°$ sector in a unit circle has length 1) + #2 Symmetry (the circle's rotational symmetry justifies the sector partition).*

---

## §5 Bridge to Chapter 6

This chapter introduced the **Mental Visualization Canvas (MVC)** as the externalised, drawn complement to the First-Minute Protocol. We presented the MVC's four-element grammar (problem-statement box, archetype-application nodes, convergence nodes, answer node), the Stage 1 / Stage 2 division of cognitive labour, the threshold rule for when the MVC is worth drawing (≥ 3 archetypes mandates drawing), and three worked examples — a 2-archetype mental MVC, a 3-archetype drawn MVC, and an MVC revision case. We named the over-detailing trap and prescribed the half-page-budget recovery. We mapped the MVC onto Zeitz's three-layer model: the MVC is a *strategic tool*, complementing the *tactical* archetypes (Pillar 2) and the *computational* gems (Pillar 5).

Chapters 1–5 have now supplied the full conceptual machinery of multidirectional solving: the multidirectional thesis (Ch. 1), the 2-archetype atom (Ch. 2), the 3-archetype molecule (Ch. 3), the First-Minute Protocol (Ch. 4), and the MVC (this chapter). Chapter 6 is the **demonstration**: five fully-developed multidirectional solutions, each running end-to-end through Protocol → MVC → Solution → Verification → Connections. The case studies are drawn from the locked §7.9 slate (with the two open-item cases self-selected per Q5(a) of the build specification). Chapter 6 is the pillar's centre of gravity by design; it is where the conceptual machinery becomes concrete and where the reader sees the full multidirectional discipline operating at olympiad scale.

The bridge into Chapter 6 is *demonstrative*. Chapters 1–5 *told* the reader how multidirectional solving works. Chapter 6 *shows* it, five times, at full depth.

> *In Chapter 6: the toolkit at work, walked end-to-end, five times.*

---

*End of Chapter 5.*
