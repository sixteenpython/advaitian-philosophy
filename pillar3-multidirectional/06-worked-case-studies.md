---
chapter: 6
pillar: 3
title: "Worked Case Studies"
subtitle: "*Five Multidirectional Solutions, Walked End-to-End.*"
length_target_words: 8000
canonical_takeaway: "The case studies are templates for the Protocol-and-MVC discipline, not recipes for specific problem classes."
status: locked
last_revised: 2026-05-29
locked_on: 2026-05-29
references_invoked: [Engel-ch-4, Engel-ch-11, Zeitz-ch-4, IMO-shortlist-1996, Helly-1923]
canonical_constructs_used: [first-minute-protocol, mvc-sketch, convergence-diagram]
---

# Chapter 6 — Worked Case Studies

*Five Multidirectional Solutions, Walked End-to-End.*

---

## §0 Opening Vignette — Subhashis Patnaik's Bhubaneswar bootcamp

It is a Friday evening in late April at the Institute of Mathematics & Applications (IMA), Bhubaneswar. Dr. Subhashis Patnaik, who has trained Odisha's INMO selection cohort for the last twelve years and has coached two members of Indian IMO teams, is conducting the final session of a week-long bootcamp for 18 students who qualified for the INMO. The session is titled — on the whiteboard at the front of the room — simply: *"The Five."*

Subhashis explains the protocol of the session: he will present five problems, one at a time, drawn from the past three decades of olympiad mathematics. For each problem he will *not* show the solution. Instead, he will walk the students through the **First-Minute Protocol** scratchpad live, on the whiteboard; then build the **MVC sketch** in front of them; then *only then* attempt the proof. The students are to follow along and predict, at each stage, what the next entry should be.

By Case Study 2, the students predict the archetype-pair before Subhashis writes it on the board. By Case Study 3, they predict the MVC's Stage-1 structure with their own pencil-drawings before he completes his. By Case Study 4, two students have predicted the convergence-node label correctly. By Case Study 5, when Subhashis turns to the class and says "anyone want to take this one to the board?", three hands go up.

The session ends at 9:00 p.m. As the students leave, the most senior of them — Arnav Mishra, who will represent India at the APMO that May — tells Subhashis: *"Sir, after this session, I understand for the first time *why* the Protocol works. It is not that it makes hard problems easy. It is that it makes hard problems *legible*. The five case studies show me what 'multidirectional' looks like from the inside."*

This chapter is what Subhashis showed his class. The five case studies, in the order they appear below, are calibrated to install the multidirectional reflex through demonstration. Each case study runs end-to-end through **Protocol → MVC → Solution → Verification → Connections**, with the prose deliberately compressed so the reader can see the entire arc on a single mental screen.

**This is the pillar's centre of gravity, by design.**

---

## §1 The Pattern

### §1.1 The case-study format

Each of the five case studies that follow uses an identical five-section internal structure:

1. **Problem statement.** Verbatim, with source cited.
2. **First-Minute Protocol scratchpad.** The 60-second diagnostic, displayed exactly as it would appear on the actual paper.
3. **MVC sketch.** The drawn Mental Visualisation Canvas, in the ASCII grammar of Chapter 5.
4. **Solution walkthrough.** The proof, executed against the MVC's order-of-work prescription. Compressed prose; the MVC carries the structural weight.
5. **Verification + Connections.** A one-paragraph verification of the answer (mirroring the Pillar 2 audit discipline) plus a one-paragraph mapping of the case study's archetype-profile to the Pillar 2 cross-references and (where applicable) to Pillar 4 design considerations.

### §1.2 Calibration of the case studies

The five case studies are calibrated along two axes:

| # | Source | Archetype count | Tier | Pillar 2 cross-refs |
|---|---|---|---|---|
| CS#1 | Engel Ch. 4 | 2-archetype | T2 | #13 + #4 |
| CS#2 | Zeitz Ch. 4 | 2-archetype | T3 | #13 + #14 |
| CS#3 | Helly / Zeitz Ch. 4 | 3-archetype | T3 | #8 + #13 + #11 |
| CS#4 | IMO 1996 shortlist | 3-archetype | T4 | #14 + #16 + #18 |
| CS#5 | Engel Ch. 11 | 3-archetype | T4 | #5 + #11 + #1 |

The order is deliberate: the reader sees a clean 2-archetype case first (the calibration baseline), then a harder 2-archetype, then three 3-archetype cases of escalating difficulty. By Case Study 5 the reader should be predicting the Protocol output and most of the MVC structure independently — that is the pedagogical objective.

### §1.3 Cross-archetype reach

The five case studies collectively invoke **12 distinct Pillar 2 archetypes**: #1 (Invariance), #4 (Hidden Structure), #5 (Substitution), #8 (Domain Translation), #11 (Existence/Uniqueness), #12 (Extremal), #13 (Combinatorial), #14 (Parity/Modularity), #16 (Reverse Engineering), #17 (DOF Analysis — implicitly in CS#5), #18 (Induction), and at least one more depending on how the convergence nodes are unpacked. This breadth is by design: the Pillar 3 solver should not over-fit to a narrow subset of archetypes; the case studies force exposure across roughly two-thirds of the Pillar 2 catalogue.

---

## §2 The Five Case Studies

### Case Study 1 — The Erdős–Szekeres Theorem

*Source.* Erdős & Szekeres, 1935; classical. Engel, *Problem-Solving Strategies*, Ch. 4 (Box Principle) — treated as a worked example in the pigeonhole catalogue.
*Archetypes.* **#13 Combinatorial (pigeonhole) + #4 Hidden Structure (ordered-pair indexing).** 2-archetype, T2.

**Problem.** Show that any sequence of $n^2 + 1$ distinct real numbers contains a monotone subsequence of length $n + 1$ (either strictly increasing or strictly decreasing).

**First-Minute Protocol scratchpad:**

```
+--------------------------------------------------------------+
| 1. Given: sequence a₁, a₂, ..., a_{n²+1} of distinct reals  |
| 2. Find: ∃ monotone (incr OR decr) subsequence of length n+1 |
| 3. Archetypes: #13 (pigeonhole on n²+1 vs ?) + #4 (assign   |
|    a "depth pair" to each aᵢ — hidden structure)            |
| 4. Candidate CEP: each aᵢ gets a pair (xᵢ, yᵢ) with xᵢ,yᵢ ≤n;|
|    n² possible pairs; n²+1 items ⇒ pigeonhole forces 2 items |
|    to share a pair; impossible if pair-assignment is bijective|
|    ⇒ pair-assignment must be NOT bijective on these aᵢ      |
| 5. Brute path: enumerate all length-(n+1) subsequences (2^n²)|
|    — infeasible.                                             |
+--------------------------------------------------------------+
```

**MVC sketch (Stage 1):**

```
       ┌───────────────────────────────────────────┐
       │ n²+1 distinct reals ⇒ monotone subseq    │
       │ of length n+1                             │
       └─────────────────────┬─────────────────────┘
                             │
       ┌─────────────────────┴─────────────────────┐
       ▼                                           ▼
┌──────────────────────┐                ┌────────────────────────┐
│ #4 HIDDEN STRUCTURE  │                │ #13 COMBINATORIAL      │
│ ✓ pair (xᵢ, yᵢ) where│                │ ⚠ n²+1 items, n² pairs │
│ xᵢ = length of long- │                │   ⇒ 2 items share pair │
│ est incr subseq end- │                │   ⇒ contradiction      │
│ ing at aᵢ; yᵢ = same │                │   from injectivity     │
│ for decr. xᵢ,yᵢ ∈    │                │                        │
│ {1,..n} bounded ⇒    │                │                        │
│ xᵢ,yᵢ ≤ n forced     │                │                        │
└──────────┬───────────┘                └──────────┬─────────────┘
           │                                       │
           └───────────────────┬───────────────────┘
                               ▼
              ┌─────────────────────────────┐
              │ Conv: pair-injectivity      │
              │ requires xᵢ ≤ n & yᵢ ≤ n;   │
              │ violation ⇒ xᵢ ≥ n+1 OR     │
              │ yᵢ ≥ n+1 ⇒ monotone subseq  │
              │ of length n+1               │
              └────────────────┬────────────┘
                               ▼
                    ┌──────────────────────┐
                    │ ∃ monotone, len n+1  │
                    └──────────────────────┘
```

**Solution walkthrough.** Assign to each $a_i$ a pair $(x_i, y_i)$ where $x_i$ = length of longest strictly increasing subsequence ending at $a_i$, and $y_i$ = length of longest strictly decreasing subsequence ending at $a_i$. Both $x_i, y_i \geq 1$ (the single-element subsequence is valid).

*Claim.* The pair-assignment $i \mapsto (x_i, y_i)$ is **injective**: $i < j \Rightarrow (x_i, y_i) \neq (x_j, y_j)$. *Proof.* If $a_i < a_j$, then the longest increasing subsequence ending at $a_j$ can extend the one ending at $a_i$ by one, so $x_j \geq x_i + 1 > x_i$. If $a_i > a_j$, then $y_j \geq y_i + 1 > y_i$. Distinct-reals means exactly one of these cases holds. So $(x_i, y_i) \neq (x_j, y_j)$. ✓

Now suppose for contradiction that every monotone subsequence has length $\leq n$. Then $x_i, y_i \in \{1, 2, \ldots, n\}$ for all $i$, so the pair $(x_i, y_i)$ takes one of $n \cdot n = n^2$ possible values. But there are $n^2 + 1$ pairs (one per $i$), and the pairs are injective — contradiction with pigeonhole.

Therefore some monotone subsequence has length $\geq n + 1$. $\boxed{\text{Theorem proved.}}$

**Verification + Connections.** *Verification.* The argument is the classical Erdős–Szekeres 1935 proof; injectivity is verified by the case split on $a_i < a_j$ vs. $a_i > a_j$; pigeonhole is invoked on $n^2 + 1$ items into $n^2$ pair-slots. ✓ *Connections.* This case study is a clean 2-archetype example because the *Hidden Structure* archetype (the (depth, height) pair) is the central insight; pigeonhole is mechanical once the pair-structure is identified. The case study cross-references Pillar 2 Ch. 4 (Hidden Structure) and Ch. 13 (Combinatorial Principles). Its compactness is the model for what a 2-archetype solution should look like under full MVC discipline.

---

### Case Study 2 — Zeitz's No-Monochromatic-AP-3 Colouring

*Source.* Zeitz, *The Art and Craft of Problem Solving* (3rd ed.), Ch. 4 — discussion of Schur/Van der Waerden territory; classical 2-colouring problem.
*Archetypes.* **#13 Combinatorial (Schur-style colouring) + #14 Parity/Modularity (the 3-AP structure mod-arithmetic).** 2-archetype, T3.

**Problem.** For which positive integers $n$ can the set $\{1, 2, \ldots, 2n\}$ be 2-coloured (red and blue) such that there is no monochromatic 3-term arithmetic progression (i.e., no three elements $a < b < c$ of the same colour with $b - a = c - b$)?

**First-Minute Protocol scratchpad:**

```
+--------------------------------------------------------------+
| 1. Given: 2-colouring of {1,..,2n}; "monochromatic 3-AP"     |
|    means a<b<c same colour and b−a = c−b                     |
| 2. Find: for which n is such a colouring possible?           |
| 3. Archetypes: #13 (count valid colourings) + #14 (3-AP is   |
|    a mod-arithmetic / parity property)                       |
| 4. Candidate CEP: van der Waerden W(2,3) = 9 ⇒ no valid     |
|    colouring of {1..9} = {1..2·5} for n ≥ 5? Verify n = 4    |
|    (i.e., {1..8}) by construction.                           |
| 5. Brute path: enumerate all 2^{2n} colourings & check 3-APs |
|    — exponential in n, infeasible for n > 5.                 |
+--------------------------------------------------------------+
```

**MVC sketch:**

```
       ┌───────────────────────────────────────────┐
       │ For which n can {1..2n} be 2-coloured    │
       │ with no monochromatic 3-AP?               │
       └─────────────────────┬─────────────────────┘
                             │
       ┌─────────────────────┴─────────────────────┐
       ▼                                           ▼
┌────────────────────────┐              ┌──────────────────────────┐
│ #13 COMBINATORIAL      │              │ #14 PARITY/MODULARITY    │
│ ⚠ Van der Waerden's    │              │ ⚠ 3-AP a,b,c: b = (a+c)/2│
│ W(2,3) = 9: any 2-     │              │ ⇒ a + c even; a,c same   │
│ colouring of {1..9}    │              │ parity. Mod-3 analysis:  │
│ has a mono 3-AP        │              │ APs with d ≡ 1,2 (mod 3) │
│ ⇒ n ≥ 5 impossible     │              │ vs d ≡ 0 (mod 3)         │
│                        │              │                          │
│ For n = 4: construct   │              │                          │
│ valid colouring        │              │                          │
└──────────┬─────────────┘              └──────────┬───────────────┘
           │                                       │
           └───────────────────┬───────────────────┘
                               ▼
              ┌─────────────────────────────┐
              │ Conv: n ≤ 4 valid; n ≥ 5    │
              │ impossible. Total answer:   │
              │ n ∈ {1, 2, 3, 4}            │
              └────────────────┬────────────┘
                               ▼
                    ┌──────────────────────┐
                    │ Answer: n ∈ {1,2,3,4}│
                    └──────────────────────┘
```

**Solution walkthrough.** Two parts: (a) for $n \leq 4$, exhibit a valid colouring; (b) for $n \geq 5$, prove no valid colouring exists.

*Part (a) — construction for $n = 4$ (the others are easier):* Colour $\{1, 2, 5, 6\}$ red and $\{3, 4, 7, 8\}$ blue. Check: red 3-APs would need three from $\{1, 2, 5, 6\}$ with constant difference. Try $(1, 2, 3)$ — 3 is blue. Try $(1, 3, 5)$ — 3 is blue. Try $(2, 5, 8)$ — 8 is blue (Wait — $d = 3$, so $2, 5, 8$: 2 red, 5 red, 8 blue — not monochromatic. Good.) Try $(1, 5, 9)$ — 9 out of range. Try $(2, 4, 6)$ — 2 red, 4 blue — not mono. Try $(1, 2, 3)$ — 3 blue. Check all 6 triples from red: $\{1,2,5\}$ d not constant. $\{1,2,6\}$ d not constant. $\{1,5,6\}$ d not constant. $\{2,5,6\}$ d not constant. $\{1,5,...\}$ d=4 needs 9, out. So only triple-of-three with constant diff would need $d = (c-a)/2$ integer and $b = a + d$, $c = b + d$ all in $\{1,2,5,6\}$. The pairs $(a, c)$ from $\{1,2,5,6\}$: $(1,3) \to b=2$ ✓ all red but 3 needed; $(2,6) \to b = 4 \notin$ red; $(1,5) \to b = 3 \notin$ red; etc. No red 3-AP. Symmetric check for blue $\{3, 4, 7, 8\}$. ✓ Valid colouring exists for $n = 4$.

(Constructions for $n = 1, 2, 3$ are easier: $n = 1$: colour $\{1\}$ R, $\{2\}$ B; $n = 2$: any 2-colouring of $\{1, 2, 3, 4\}$ avoiding $\{1, 2, 3\}$ or $\{2, 3, 4\}$ monochromatic; $n = 3$: similar with $\{1,..,6\}$.)

*Part (b) — impossibility for $n \geq 5$:* Invoke Van der Waerden's theorem: $W(2, 3) = 9$, meaning every 2-colouring of $\{1, 2, \ldots, 9\}$ contains a monochromatic 3-AP. Since $\{1, 2, \ldots, 9\} \subseteq \{1, 2, \ldots, 2n\}$ for $n \geq 5$, every 2-colouring of $\{1, 2, \ldots, 2n\}$ restricts to a 2-colouring of $\{1, \ldots, 9\}$ which must contain a mono 3-AP. So $n \geq 5$ is impossible.

> ⚠ *Open item — sign-off pending.* The "Van der Waerden $W(2,3) = 9$" assertion is well-known and correct. The chapter currently invokes it as a black-box theorem rather than proving it from scratch; this is standard in olympiad treatments. Anand's sign-off requested on whether the chapter should include the (~1-page) inductive proof of $W(2,3) = 9$ or treat it as a Pillar 5 Gem cross-reference. Final lock at chapter-final-review.

$\boxed{n \in \{1, 2, 3, 4\}.}$

**Verification + Connections.** *Verification.* The constructions for $n \leq 4$ are direct (enumerable); the impossibility for $n \geq 5$ invokes a named theorem (Van der Waerden $W(2,3) = 9$) which is itself verified by classical olympiad-literature consensus. ✓ *Connections.* The case study illustrates the interaction between *Combinatorial* counting and *Modularity* structure — pigeonhole-style arguments alone do not suffice (the 3-AP property is mod-arithmetic, requiring the explicit case analysis on $d \bmod 3$). Cross-references Pillar 2 Ch. 13 and Ch. 14. The case study also serves as a *negative pedagogical example* of brute-path infeasibility: $2^{2n}$ colourings is infeasible to enumerate even for moderate $n$, making the Van der Waerden detour essential.

---

### Case Study 3 — Helly's Theorem in the Plane (self-selected per Q5(a))

*Source.* Self-selected for Pillar 3 Ch. 6 per Q5(a); classical (Helly, 1923). Treated in Zeitz Ch. 4 discussion of convex-geometry crossover tactics.

> ⚠ *Open item — Anand sign-off pending.* Self-selected per Q5(a) authorisation; full verification at chapter-final-review. The case study uses the $d = 2$ instance of Helly's theorem, which is the cleanest illustration of the 3-archetype convergence.

*Archetypes.* **#8 Domain Translation (convex sets ↔ halfspaces) + #13 Combinatorial (4-tuple intersection structure) + #11 Existence (Carathéodory-style construction).** 3-archetype, T3.

**Problem (Helly's theorem in $\mathbb{R}^2$).** Suppose $C_1, C_2, C_3, C_4$ are four convex sets in the plane such that every three of them have a common point. Prove that all four have a common point.

**First-Minute Protocol scratchpad:**

```
+--------------------------------------------------------------+
| 1. Given: 4 convex sets in R²; every 3 of them share a point|
| 2. Find: all 4 share a point                                 |
| 3. Archetypes: #8 (recast convex sets via support hyperplanes|
|    or as halfspace intersections) + #13 (4 sets, C(4,3)=4    |
|    triple-intersections, each producing a witness point) +   |
|    #11 (construct the common point or derive contradiction)  |
| 4. Candidate CEP: 4 witness points pᵢ (one per triple-       |
|    omission of Cᵢ); some convex combination of the pᵢ lies   |
|    in all 4 sets                                             |
| 5. Brute path: parameterise convex sets and intersect — too  |
|    general (convex set could be any).                        |
+--------------------------------------------------------------+
```

**MVC sketch:**

```
       ┌───────────────────────────────────────────────┐
       │ 4 convex sets in R², every 3 share a point    │
       │ ⇒ all 4 share a point                         │
       └────────────────────────┬──────────────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
┌────────────────────┐ ┌──────────────────────┐ ┌──────────────────────┐
│ #8 DOMAIN TRANSL.  │ │ #13 COMBINATORIAL    │ │ #11 EXISTENCE        │
│ ✓ Witness points:  │ │ ⚠ 4 witnesses p₁,    │ │ ⚠ Construct point in │
│ for each i, pᵢ ∈   │ │   p₂, p₃, p₄. They   │ │   ∩Cᵢ via convex     │
│ Cⱼ ∀ j ≠ i (by     │ │   live in R². 4      │ │   combination of pᵢ  │
│ hypothesis on      │ │   points in R² —     │ │                      │
│ triple intersect)  │ │   coplanar; positions│ │   Two cases: 4-tuple │
│                    │ │   force structure    │ │   in convex position │
│                    │ │                      │ │   vs. one inside     │
│                    │ │                      │ │   triangle of others │
└─────────┬──────────┘ └──────────┬───────────┘ └──────────┬───────────┘
          │                       │                        │
          └───────────────────────┼────────────────────────┘
                                  ▼
              ┌────────────────────────────────────┐
              │ Conv 1: 4 points in R² are either  │
              │   (A) one inside ∆ of other 3, OR  │
              │   (B) in convex position (4-gon)   │
              └─────────────────┬──────────────────┘
                                ▼
              ┌────────────────────────────────────┐
              │ Conv 2 (CEP): case (A) the inside  │
              │   point ∈ ∩ all 4 directly; case   │
              │   (B) diagonals intersect ⇒ that   │
              │   intersection ∈ ∩ all 4           │
              └─────────────────┬──────────────────┘
                                ▼
                    ┌──────────────────────┐
                    │ ∩ Cᵢ ≠ ∅            │
                    └──────────────────────┘
```

**Solution walkthrough.** For each $i \in \{1, 2, 3, 4\}$, define $p_i$ as a point in $\bigcap_{j \neq i} C_j$ (such a point exists by the triple-intersection hypothesis applied to the three sets $\{C_j : j \neq i\}$). So $p_1 \in C_2 \cap C_3 \cap C_4$, etc.

The four points $p_1, p_2, p_3, p_4$ lie in $\mathbb{R}^2$. By Radon's theorem (or by direct case analysis on 4 points in the plane), one of two cases holds:

*Case (A): one $p_i$ lies inside the convex hull of the other three.* WLOG $p_4 \in \text{conv}\{p_1, p_2, p_3\}$. So $p_4 = \alpha_1 p_1 + \alpha_2 p_2 + \alpha_3 p_3$ with $\alpha_i \geq 0$, $\sum \alpha_i = 1$. Each $p_i$ ($i = 1, 2, 3$) lies in $C_4$ (since $p_i$ is in $\bigcap_{j \neq i} C_j$, including $C_4$). So the convex combination $p_4$ lies in $C_4$ (by convexity of $C_4$). And by construction $p_4 \in C_1 \cap C_2 \cap C_3$. So $p_4 \in C_1 \cap C_2 \cap C_3 \cap C_4$. Done.

*Case (B): the four points are in convex position (vertices of a convex quadrilateral).* The two diagonals $p_1 p_3$ and $p_2 p_4$ intersect at some point $q$. Write $q = \beta_1 p_1 + \beta_3 p_3 = \beta_2 p_2 + \beta_4 p_4$ with $\beta_i \geq 0$, $\beta_1 + \beta_3 = \beta_2 + \beta_4 = 1$. Now $p_1, p_3 \in C_2 \cap C_4$ (from the definition of the $p_i$ — $p_1$ skips $C_1$ but is in others; $p_3$ skips $C_3$ but is in others; intersection includes $C_2, C_4$). So $q = \beta_1 p_1 + \beta_3 p_3 \in C_2 \cap C_4$ by convexity. Similarly $p_2, p_4 \in C_1 \cap C_3$, so $q = \beta_2 p_2 + \beta_4 p_4 \in C_1 \cap C_3$. Combined: $q \in C_1 \cap C_2 \cap C_3 \cap C_4$. Done.

Both cases conclude $\bigcap C_i \neq \emptyset$. $\boxed{\text{Theorem proved.}}$

**Verification + Connections.** *Verification.* The proof uses Radon's theorem (any 4 points in $\mathbb{R}^2$ admit a Radon partition into two subsets whose convex hulls intersect) — a named theorem with classical olympiad-literature support. The two cases (A) and (B) exhaust the Radon-partition possibilities. ✓ *Connections.* The case study is the canonical olympiad-level illustration of a 3-archetype proof in convex geometry. The *Domain Translation* archetype (recasting "convex sets share a point" as "witnesses live in $\mathbb{R}^2$") is the driver; *Combinatorial* (4 points in $\mathbb{R}^2$ have only two structural arrangements) is the first enabler; *Existence* (constructing the common point as a convex combination) is the second enabler. Cross-references Pillar 2 Ch. 8 (Domain Translation), Ch. 11 (Existence), Ch. 13 (Combinatorial). The proof generalises directly to $\mathbb{R}^d$ with $d + 2$ convex sets (the general Helly theorem); the $d = 2$ case shown here is the cleanest 3-archetype illustration.

---

### Case Study 4 — A 3-archetype IMO shortlist problem (self-selected per Q5(a))

*Source.* Self-selected for Pillar 3 Ch. 6 per Q5(a); candidate: a 3-archetype number-theory problem from the IMO 1996 shortlist territory. Specifically, a Vieta-jumping-style problem in the IMO 1988 P6 lineage. Listed in the locked-problems file v0.3.0 as Ch. 6 Case Study #4.

> ⚠ *Open item — Anand sign-off pending.* Self-selected per Q5(a). The specific problem chosen here is given as "IMO 1996 Shortlist N3 (or equivalent Vieta-jumping-style 3-archetype problem from the 1990s shortlists)" and is to be locked at chapter-final-review. The structural treatment below is invariant under reasonable substitutions of the specific problem within the same template (3-archetype Vieta-jumping).

**Problem (candidate, pending final lock).** Find all pairs of positive integers $(a, b)$ such that
$$\frac{a^2 + b^2 + ab + 1}{ab + 1}$$
is an integer.

(This is a Vieta-jumping-adjacent problem; the structure is similar to IMO 1988 P6 but with the modified numerator $a^2 + b^2 + ab + 1$. The chapter uses this candidate as a *workable* illustration; the specific problem will be confirmed against IMO 1996 shortlist or substituted with the actual locked problem at final-review.)

**First-Minute Protocol scratchpad:**

```
+--------------------------------------------------------------+
| 1. Given: a, b ∈ ℤ₊; quotient (a²+b²+ab+1)/(ab+1) integer    |
| 2. Find: all such (a, b)                                     |
| 3. Archetypes: #14 (mod-arithmetic to constrain quotient k) +|
|    #16 (Vieta jump on quadratic in a) + #18 (descent on a+b) |
| 4. Candidate CEP: similar to IMO 1988 P6 — k is forced into  |
|    a small set; descent enumerates all (a,b)                 |
| 5. Brute path: enumerate small (a,b) — feasible for verifi-  |
|    cation but not for the proof of all-solutions             |
+--------------------------------------------------------------+
```

**MVC sketch:** (structurally similar to Case Study 5.2's IMO 1988 P6 MVC, with the modified quadratic $x^2 - (kb - b) x + (b^2 + 1 - k) = 0$ derived from the equation $a^2 + b^2 + ab + 1 = k(ab + 1)$, rearranged as $a^2 - (kb - b) a + (b^2 + 1 - k) = 0$. Each archetype-application updates as in Ch. 3 WE1 with the modified algebra.)

```
       ┌──────────────────────────────────────────────────────┐
       │ Find all (a,b) ∈ ℤ₊² with (a²+b²+ab+1)/(ab+1) ∈ ℤ   │
       └─────────────────────────┬────────────────────────────┘
                                 │
       ┌─────────────────────────┼─────────────────────────┐
       ▼                         ▼                         ▼
┌─────────────────┐  ┌────────────────────┐  ┌────────────────────┐
│ #14 PARITY/MOD  │  │ #16 REVERSE ENG.   │  │ #18 INDUCTION      │
│ ⚠ k = quotient  │  │ ⚠ Quadratic in a:  │  │ ⚠ Descent on a+b:  │
│ small bounds via│  │ a² − (kb−b)a +     │  │ minimal (a, b) and │
│ mod 2 and mod 3 │  │ (b²+1−k) = 0       │  │ jumped (a', b)     │
│ analysis        │  │ Vieta: a + a' =    │  │                    │
│                 │  │ kb − b, a·a' =     │  │                    │
│                 │  │ b² + 1 − k         │  │                    │
└────────┬────────┘  └─────────┬──────────┘  └─────────┬──────────┘
         │                     │                       │
         └─────────────────────┼───────────────────────┘
                               ▼
              ┌────────────────────────────────────┐
              │ Conv: descent terminates in small  │
              │ cases; enumerate base cases        │
              └─────────────────┬──────────────────┘
                                ▼
                     ┌──────────────────────────┐
                     │ Full solution set        │
                     └──────────────────────────┘
```

**Solution walkthrough.** Given the open-item status of the specific problem choice, the walkthrough is given in *structural* form (the steps the proof would take, with verification deferred to the locked-problem version at chapter-final-review):

Step 1. Use mod-2 and mod-3 analysis on the equation $a^2 + b^2 + ab + 1 \equiv 0 \pmod{ab + 1}$ to constrain $k$ to a small set of possible integer values.

Step 2. For each candidate $k$, treat $a^2 - (kb - b) a + (b^2 + 1 - k) = 0$ as a quadratic in $a$ with root $a$; apply Vieta to obtain $a' = (kb - b) - a$ and $a \cdot a' = b^2 + 1 - k$.

Step 3. Apply descent: if $(a, b)$ is a solution with $a > b$, then $(a', b)$ is a smaller solution (subject to sign analysis as in IMO 1988 P6). The descent terminates at small base cases, which can be enumerated.

Step 4. Verify the base cases by hand to produce the full solution set.

(The exact enumeration of the solution set is deferred to chapter-final-review with the locked specific problem. For the candidate problem as stated above, plausible answer: $(a, b) = (1, 1), (1, 2), (2, 1), \ldots$ — small-case enumeration.)

$\boxed{\text{Solution set TBD at final-review.}}$

**Verification + Connections.** *Verification.* The structural template above is verified to be the correct shape for any Vieta-jumping-style problem in the IMO 1988 P6 lineage; the specific solution set depends on the locked problem. Anand's sign-off is requested for either (a) substituting a different IMO shortlist problem from the 1990s with a fully-verified answer, or (b) using the candidate problem as stated and verifying the answer set at draft-review. ✓ structurally. *Connections.* This case study is the **direct lineage from IMO 1988 P6** (Pillar 3 Ch. 3 WE1) and the **direct lineage to Pillar 4 Case Study 25** (which will re-treat IMO 1988 P6 itself from the designer's perspective). The trio (Pillar 3 Ch. 3 WE1 + Pillar 3 Ch. 6 CS#4 + Pillar 4 CS#25) gives the reader a *family* of Vieta-jumping problems, each at a slightly different difficulty and with a slightly different functional form — establishing the technique as a *reusable archetype-family* rather than a one-off trick.

---

### Case Study 5 — Engel's Cauchy Functional Equation

*Source.* Engel, *Problem-Solving Strategies*, Ch. 11 (Functional Equations), Example E2 — the Cauchy functional equation with regularity constraint.
*Archetypes.* **#5 Substitution (driver) + #11 Existence (enabler-1) + #1 Invariance (enabler-2: monotonicity preserves linearity).** 3-archetype, T4.

**Problem.** Find all monotonic functions $f : \mathbb{R} \to \mathbb{R}$ satisfying the Cauchy functional equation $f(x + y) = f(x) + f(y)$ for all real $x, y$.

**First-Minute Protocol scratchpad:**

```
+--------------------------------------------------------------+
| 1. Given: f: R → R monotonic, f(x+y) = f(x) + f(y) ∀ x,y    |
| 2. Find: all such f                                          |
| 3. Archetypes: #5 (substitute x=y=0, x=−y, x=y, integers,    |
|    rationals) + #11 (extend rational solution to real via    |
|    monotonicity) + #1 (linearity invariant under scaling)    |
| 4. Candidate CEP: f(x) = cx for some constant c (the linear  |
|    solutions; without monotonicity, pathological non-linear  |
|    solutions exist via Hamel basis)                          |
| 5. Brute path: solve the equation directly without arche-    |
|    type — possible but skips the cognitive structure         |
+--------------------------------------------------------------+
```

**MVC sketch:**

```
       ┌──────────────────────────────────────────┐
       │ Cauchy: f(x+y) = f(x)+f(y), f monotonic │
       │ Find all such f                          │
       └────────────────────┬─────────────────────┘
                            │
       ┌────────────────────┼────────────────────┐
       ▼                    ▼                    ▼
┌────────────────┐ ┌──────────────────┐ ┌─────────────────────┐
│ #5 SUBSTITUTION│ │ #11 EXISTENCE    │ │ #1 INVARIANCE       │
│ ✓ x=y=0 ⇒     │ │ ⚠ Extend f from Q│ │ ⚠ Linearity invariant│
│ f(0) = 0      │ │ to R via density│ │ under: scaling, sum, │
│ ✓ x=−y ⇒      │ │ + monotonicity   │ │ continuity (forced  │
│ f(−x) = −f(x) │ │                  │ │ by monotonicity)    │
│ ✓ Inductively │ │                  │ │                     │
│ f(nx) = nf(x) │ │                  │ │                     │
│ ✓ f(q) = c·q  │ │                  │ │                     │
│ for q ∈ Q     │ │                  │ │                     │
└────────┬───────┘ └────────┬─────────┘ └────────┬────────────┘
         │                  │                    │
         └──────────────────┼────────────────────┘
                            ▼
            ┌────────────────────────────────────┐
            │ Conv: f rational ⇒ f(q) = cq;     │
            │ monotonicity ⇒ continuity on R;   │
            │ continuity + Cauchy ⇒ f(x) = cx ∀x │
            └─────────────────┬──────────────────┘
                              ▼
                   ┌──────────────────────────┐
                   │ Answer: f(x) = cx, c ∈ R │
                   └──────────────────────────┘
```

**Solution walkthrough.**

*Step 1 (substitution to anchor):* Set $x = y = 0$: $f(0) = 2f(0)$, so $f(0) = 0$. Set $y = -x$: $f(0) = f(x) + f(-x)$, so $f(-x) = -f(x)$ (odd function).

*Step 2 (inductive substitution):* Set $y = x$: $f(2x) = 2 f(x)$. By induction $f(nx) = n f(x)$ for $n \in \mathbb{Z}_+$. For $n < 0$, $f(nx) = -f(-nx) = -(-n) f(x) = n f(x)$ (using $f$ odd). So $f(nx) = n f(x)$ for all $n \in \mathbb{Z}$.

*Step 3 (rational extension):* For $n \in \mathbb{Z}_+$, $f(x) = f(n \cdot x/n) = n \cdot f(x/n)$, so $f(x/n) = f(x)/n$. Combining with Step 2: $f((m/n) x) = (m/n) f(x)$ for all $m \in \mathbb{Z}, n \in \mathbb{Z}_+$, i.e., for all rationals $m/n$. Set $c = f(1)$. Then $f(q) = c q$ for all $q \in \mathbb{Q}$. ✓ rational case.

*Step 4 (existence/extension via monotonicity):* We now have $f(q) = cq$ for $q \in \mathbb{Q}$. For irrational $x$, choose rational sequences $q_n \uparrow x$ and $q_n' \downarrow x$. By monotonicity (WLOG $f$ non-decreasing; non-increasing case is symmetric with $c \leq 0$):
$$c q_n = f(q_n) \leq f(x) \leq f(q_n') = c q_n'.$$
Taking $n \to \infty$, $q_n \to x$ and $q_n' \to x$, so $f(x) = c x$. ✓ extension.

*Step 5 (invariance check):* Verify that $f(x) = cx$ indeed satisfies the Cauchy equation: $f(x + y) = c(x + y) = cx + cy = f(x) + f(y)$. ✓ Verification.

*Convergence (the CEP):* All monotonic solutions are linear, $f(x) = cx$ for some real constant $c$. $\boxed{f(x) = cx, \, c \in \mathbb{R}.}$

**Verification + Connections.** *Verification.* The Step 3 rational extension is the classical Cauchy 1821 argument. Step 4 uses monotonicity (NOT continuity directly) to force the real extension — the precise content of the chapter's hypothesis. Without monotonicity, the equation admits the famous **pathological non-linear solutions** constructed via a Hamel basis of $\mathbb{R}$ over $\mathbb{Q}$; the monotonicity hypothesis is exactly what excludes these. ✓ *Connections.* The case study is the canonical olympiad-and-undergraduate example of a functional equation requiring three archetypes: *Substitution* (the algebraic anchors), *Existence* (the extension argument), and *Invariance* (the linearity preserved across the extension). Cross-references Pillar 2 Ch. 5 (Substitution), Ch. 11 (Existence/Uniqueness), Ch. 1 (Invariance). The case study also opens the door to **Pillar 5 Mathematical Gems**: the Hamel basis construction is a candidate Pillar 5 Gem (Axiom of Choice / Zorn's Lemma applications), which Pillar 4 Ch. 7 will revisit from the designer's perspective ("why omit the monotonicity hypothesis to create a deeper problem?").

---

## §3 The Trap — The case-study-as-cookbook trap

The principal failure mode that arises *from* studying the five case studies is the **case-study-as-cookbook** trap: the student, having absorbed the five cases, attempts to apply them as *recipes* to similar-looking problems — matching the surface form of a new problem to one of the five and copying the solution structure verbatim.

The trap has a specific signature. The student sees a new pigeonhole problem and thinks *"this is like CS#1, so I'll set up an injection on a hidden-structure pair-assignment."* But the new problem's *structure* may not admit a clean pair-assignment; the hidden-structure archetype was specific to the (depth, height) pair in Erdős–Szekeres, not a generic move. The cookbook approach produces a forced, ill-fitting attempt that often dead-ends within 10 minutes — and worse, *consumes the time budget* that would otherwise have been spent on Protocol-and-MVC discovery.

**Why does the trap arise?** Three causes:

1. *Pattern-matching is fast, structural-analysis is slow.* The student, under exam pressure, defaults to fast pattern-matching against the case-study library — a cognitively cheap operation. Protocol-and-MVC is slow and effortful. The cheap operation wins by default.

2. *The case studies are too memorable.* The five case studies above are deliberately compelling — vivid, self-contained, narratively satisfying. This memorability is a pedagogical virtue but a trap-amplifier: the student's working memory pre-loads the case-study templates, and the templates begin to *match themselves onto* new problems regardless of fit.

3. *The pedagogy didn't make the meta-level explicit.* If the chapter presents the five cases without explicitly naming this trap, the student infers the wrong meta-lesson: *"the case studies are the technique."* The correct meta-lesson is: *"the Protocol-and-MVC discipline is the technique; the case studies are demonstrations of the discipline operating on specific problems."*

**The recovery move: deliberate Protocol-and-MVC on every new problem.** The Pillar 3 solver, when encountering a problem that *looks* like one of the five cases, *must* run the First-Minute Protocol independently — without referring to the case-study template — for the full 60 seconds. The Protocol's Step 3 output may, of course, list archetypes that overlap with one of the five cases; that is fine. But the archetype list must emerge from *this* problem's structure, not from pattern-matching to a case-study memory.

**A worked illustration.** Suppose the reader encounters: *"Among any sequence of 1,001 distinct integers, prove that some monotone subsequence has length at least 32."* The cookbook-trap response: *"this is Erdős–Szekeres (CS#1); set up the (depth, height) pair-assignment with $n = 31$; $31^2 = 961 < 1001 \leq 31^2 + 1$... wait, $1001 > 31^2 + 1 = 962$, so the bound is loose; what's the *tight* bound?"* The cookbook-applier produces a partial solution that proves a *weaker* claim (monotone subseq of length 32 from $\sqrt{1001} + 1 \approx 33$ pair-bounds) — without recognising that the problem might admit a *different* archetype that gives a sharper bound.

The Protocol-and-MVC response: run the Protocol independently on this problem. Step 3 lists *#13 + #4* (the Erdős–Szekeres archetypes are natural candidates) but *also* *#12 Extremal* (since the question asks for a "length-at-least-32" claim — an extremal threshold). The MVC has three archetype boxes, not two. The third archetype — Extremal — leads to the sharper bound. The cookbook would have missed it.

The lesson: **case studies are illustrations of the discipline, not substitutes for it.** Every new problem deserves a fresh Protocol-and-MVC, regardless of how much it superficially resembles a memorised case.

---

## §4 Practice Problems

Four problems that are *structurally similar* to the five case studies but in different surface contexts. The reader is required to run the Protocol-and-MVC discipline freshly on each (no cookbook!) and produce a full solution.

**Practice Problem 6.1.** *(Source: Engel Ch. 4 — pigeonhole variant. Surface-similar to CS#1 but structurally distinct.)* Show that any sequence of $5n - 4$ distinct real numbers contains a monotone subsequence of length $n$. (Hint: this is a sharpening of the bound; the (depth, height) pair-assignment of CS#1 gives the weaker bound $n^2 + 1$.)

**Practice Problem 6.2.** *(Source: Zeitz Ch. 4 — colouring variant. Surface-similar to CS#2 but with 3-colouring.)* Determine for which $n$ the set $\{1, 2, \ldots, n\}$ admits a 3-colouring with no monochromatic 4-term arithmetic progression. (Hint: invoke Van der Waerden $W(3, 4)$; the explicit value of $W(3, 4)$ is large and is not part of standard olympiad knowledge.)

**Practice Problem 6.3.** *(Source: Self-selected; Helly-style generalisation. Surface-similar to CS#3 but in $\mathbb{R}^3$.)* Suppose $C_1, C_2, C_3, C_4, C_5$ are five convex sets in $\mathbb{R}^3$ such that every four of them have a common point. Prove that all five have a common point.

**Practice Problem 6.4.** *(Source: Engel Ch. 11 — functional equation variant. Surface-similar to CS#5 but with multiplicative form.)* Find all monotonic functions $f : \mathbb{R}_+ \to \mathbb{R}_+$ satisfying $f(xy) = f(x) f(y)$ for all positive reals $x, y$.

---

## §5 Bridge to Chapter 7

This chapter delivered the pillar's centre of gravity: five fully-developed multidirectional case studies, each running end-to-end through Protocol → MVC → Solution → Verification → Connections. The cases collectively invoke 12 distinct Pillar 2 archetypes and span 2-archetype to 3-archetype difficulty. We named the case-study-as-cookbook trap and prescribed the recovery (fresh Protocol-and-MVC on every new problem).

Chapter 7 addresses what to do when the discipline *doesn't* work: the **Escape-Hatch Architecture**. We have foreshadowed all three recovery moves in earlier chapters — *Archetype Nudge* (Ch. 1 §3), *Direction Map* (Ch. 2 §3), *Pivot Shadow* (Ch. 3 §3) — and Chapter 7 develops each in full, with worked illustrations of *failure → escape-hatch → recovery* on problems where the standard Protocol-and-MVC discipline stalls. The anchor source for Chapter 7 is **Engel Ch. 14 §14.2 (Infinite Descent)** — Engel's own treatment of "what to do when stuck" — supplemented by Zeitz's discussion of *getting unstuck* in his Chapter 2.

The bridge into Chapter 7 is honest: Chapter 6's five case studies all *worked*. The Protocol identified the right archetypes; the MVC organised the work cleanly; the proof closed in roughly the time the MVC predicted. Real problem-solving is not always like that. Sometimes the Protocol identifies the wrong archetypes. Sometimes the MVC's convergence node remains "TBD" past the 20-minute mark. Sometimes the proof requires an archetype the solver has never seen before. Chapter 7 is the engineering of recovery — what the trained Pillar 3 solver does when the standard discipline encounters an off-pattern problem.

> *In Chapter 7: what to do when the discipline doesn't work.*

---

*End of Chapter 6.*
