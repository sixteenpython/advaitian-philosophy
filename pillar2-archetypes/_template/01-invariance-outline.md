# Chapter 1: Invariance — Drafting Outline

> **Status:** Outline only. No prose drafted. Awaiting Anand's review and sign-off before any section is written.
>
> **Treatment:** Baseline elevation of `knowledge_base/Chapter_1_Invariance.txt`. Existing structure preserved. Voice elevated to hybrid Polya / Tao / Engel / Zeitz / Andreescu / KD Joshi register, calibrated per section. 3 worked examples (Tier 1 → Tier 3). Formal definitions, named-theorem rigor, verified problem citations.

---

## Front Matter

| Field | Value |
|---|---|
| **Title** | Chapter 1 — Invariance |
| **Subtitle** | "If Something Stays Constant, Make It Your Anchor" |
| **Category** | Structure Recognition (Archetypes 1–4) |
| **Related archetypes** | #2 Symmetry (via Noether) · #9 Domain Constraints (as filter) · #17 Degrees of Freedom (as counting) · #12 Extremal Principles (under Lagrange multipliers) |
| **Canonical takeaway** | *"Track the invariant; let everything else move."* |
| **Length target** | ≈ 7,000 words (+40% over existing) |

---

## Section-by-Section Plan

### Opening Vignette  *(Polya / Joshi voice)*

- Keep the **juggler image** (it works, it's been earned). Compress the prose by ~25% — the existing version is slightly meandering.
- Add a *second* image immediately after, to demonstrate the archetype's range: the **determinant of a matrix surviving wild row operations** — a quantity that persists through algebraic violence. Two images make the archetype feel universal, not merely physical.
- ≈ 400 words. Closes: *"This is Invariance."*

### 1. The Archetype Defined

#### 1.1 Formal Definition  *(Tao / Engel)*  — **NEW: formal definition added**

\begin{definition}
A quantity $Q : X \to \mathbb{R}$ is *invariant* under a group $G$ acting on $X$ if $Q(g \cdot x) = Q(x)$ for all $g \in G$ and all $x \in X$.
\end{definition}

- Then unpack each component in plain English (group, action, what "constant" really means relative to the group).
- Existing 4 forms preserved: **summative · multiplicative · relational · structural**, each with 1–2 olympiad-grade examples added (e.g., for multiplicative: "the product of complex roots of $\sum a_i x^i$, by Vieta").
- ≈ 350 words.

#### 1.2 Core Principle  *(Polya)*

- Existing principle preserved verbatim — it's already crystalline:
  *"In every problem, certain things change and certain things don't. The invariant is what stays fixed, and is almost always the key to the solution."*
- Cognitive-reframing paragraph (existing, polished).
- One short illustrative example (the "three positives summing to 15, find max product" — existing, tightened).
- ≈ 300 words.

#### 1.3 The Cognitive Shift  *(Polya / Joshi)*

- Existing **Before vs After** framing preserved, tightened.
- Existing concrete demonstration via the polygon-AP problem preserved (functions as preview of Worked Example 1).
- Habits of invariant-aware solvers: 4 habits, sharpened.
- ≈ 400 words.

### 2. The Deep Structure

#### 2.1 Mathematical Foundations  *(Tao / Engel)*  — **NEW: formal Noether + Klein-Erlangen**

- Group theory treatment preserved + small formalization (definition of group action, orbit, invariant).
- **NEW** — `\begin{theorem}[Noether's Theorem, informal statement]`
  *Every continuous one-parameter symmetry of an action functional yields a corresponding conserved current.*
  Followed by 1 paragraph of intuition; *not* a proof. Cited (Noether, 1918).
- **NEW** — Klein's *Erlangen Program* (1872) called out by name: *"A geometry is the study of properties invariant under a chosen group of transformations."* This single sentence reframes the previous paragraph and ties §2.1 forward to Symmetry.
- Euler characteristic preserved.
- ≈ 500 words.

#### 2.2 Physical Foundations  *(Engel / Andreescu — encyclopedic, tightened)*

- Existing treatment preserved (energy, momentum, angular momentum, electric charge).
- Compress: the existing pendulum exposition is too long. Replace with one sharp sentence:
  *"Conservation laws are invariants enforced by the structure of physical law itself; a proposed solution that violates them is not merely incorrect — it is impossible."*
- ≈ 250 words.

#### 2.3 Cognitive Foundations  *(Polya)*

- Existing "change bias" framing preserved.
- Three concrete remedies preserved, tightened.
- ≈ 200 words.

### 3. The Diagnostic Toolkit

#### 3.1 The Three Questions Method  *(Zeitz / Andreescu — operational)*

Existing three questions preserved verbatim — they are already gold:
1. What are the moving parts?
2. What's the fixed relationship?
3. Can I anchor my solution around the invariant?

Add a one-line *execution note* after each — when the question succeeds, where it commonly fails. ≈ 300 words.

#### 3.2 Types of Invariants: A Comprehensive Guide  *(Engel — taxonomic)*

- Four types preserved (summative, multiplicative, relational, structural).
- Each type's example list expanded by 1–2 olympiad-grade instances.
- ≈ 350 words.

#### 3.3 Common Pitfalls  *(Polya / Joshi)*

- Existing 4 pitfalls preserved, language sharpened. Names harmonized with Blueprint v3 Pitfall Hall of Fame where overlap exists.
- ≈ 250 words.

### 4. Worked Examples — *the chapter's center of gravity*  *(Tao / Zeitz / Andreescu)*

#### 4.1 Example 1 — Polygon with Arithmetic-Progression Angles  *(Tier 1, simulated)*

> **Problem.** *The interior angles of a convex polygon are in arithmetic progression. The smallest angle is 120°, and the common difference is 5°. Find the number of sides.*

- **Source:** simulated; the canonical Advaitian example. Cited as such.
- **Demonstrates:** Invariance + Domain Constraints (#9) — bidirectional convergence.
- **Solution arc:** Three Questions Method → AP-sum vs polygon-sum → quadratic $n^2 - 25n + 144 = 0$ → roots $n=9, 16$ → domain filter (largest angle < 180°) → only $n=9$ survives.
- **Pivot:** *"Algebra generates candidates; geometry selects the winner."*
- ≈ 600 words.

#### 4.2 Example 2 — The Mutilated Chessboard, Generalized  *(Tier 2 — JEE Adv / Putnam B-level)*

> **Problem.** *(Proposed.)* For which integers $n \geq 3$ can an $n \times n$ chessboard with two opposite corners removed be tiled by $1 \times 2$ dominoes?

- **Source:** simulated. Real reference: the classic mutilated-chessboard ($n = 8$) is well-known and attributed to Max Black (1946). My generalization to arbitrary $n$ is a teaching extension.
- **Demonstrates:** Invariance via *coloring parity* — a structural invariant disguised as a tiling problem.
- **Solution arc:** Standard chess coloring → each domino covers exactly one black + one white → invariant: black-count = white-count in any tileable region → the two corners removed are *the same color* iff $n$ is even → for even $n$, invariant is violated, tiling impossible; for odd $n$, an explicit construction works.
- **Pivot:** *the coloring is itself the invariant.* It is not a "trick" — it is the structure made visible.
- ≈ 700 words.
- ⚠️ **Anand: confirm or substitute.** Is this Tier 2 or borderline Tier 1? Stronger Tier 2 candidates: a Putnam problem on $n$-step transformation invariants, or the IMO-shortlist "infinite chip-firing" type. I'll defer to your call.

#### 4.3 Example 3 — Vieta Jumping  *(Tier 3 — IMO P5/P6 level)*

> **Problem.** *Let $a, b$ be positive integers such that $ab + 1$ divides $a^2 + b^2$. Show that $\dfrac{a^2 + b^2}{ab + 1}$ is a perfect square.*

- **Source: IMO 1988, Problem 6.** The canonical Vieta-jumping problem. (Verified citation.)
- **Demonstrates:** Invariance (the value $k = \frac{a^2+b^2}{ab+1}$ over the orbit) + Reverse Engineering (#16) + Recursion / Descent (#18). Triple-archetype convergence — perfect Tier 3 demonstration.
- **Solution arc:** Fix $k$; consider the set $S_k = \{(a, b) \in \mathbb{Z}_{>0}^2 : a^2 + b^2 = k(ab+1)\}$. Show $S_k$ is closed under the *Vieta jump* $(a, b) \mapsto (b, kb - a)$. Pick the element of $S_k$ minimizing $a + b$. Show that the jump applied at this minimal element forces $kb - a = 0$ or $\leq 0$, which (after careful case analysis) forces $a = 0$ in a "shadow" instance — at which point $k = b^2$. Q.E.D.
- **Pivot:** *the orbit is the invariant, not any single $(a, b)$.* This is the deep lesson — invariance can live at the level of *sets*, not just of *quantities*.
- ≈ 900 words. The chapter's mathematical climax.
- ⚠️ **Anand: confirm.** This is the canonical version (and the actually-correct citation). Should we instead use a tamer warm-up version (e.g., the $\frac{a^2 + b^2 + 1}{ab + 1}$ variant) and reserve IMO 1988 P6 for Pillar 3 (Multidirectional)? My instinct: keep IMO 1988 P6 here. It is the cleanest single-archetype use of invariance at the elite level. Pillar 3 can use IMO 2001 P6 (cyclic quadrilateral), which is genuinely multidirectional.

### 5. Practice Problems  *(Engel / Andreescu)*

7 problems. Statements in §5; solutions/hints in chapter-end appendix.

| # | Problem | Source | Tier |
|---|---|---|---|
| 5.1 | Hat-switching parity puzzle | Existing 5.1 (Soviet, simulated) | 1 |
| 5.2 | Triangle angles in AP, smallest = 40° | Existing 5.2 (classic) | 1 |
| 5.3 | Roots of $x^2 + px + q = 0$ in ratio 2:3 — express $q$ in terms of $p$ | Existing 5.3 (classic) | 2 |
| 5.4 | Fibonacci-like recurrence: $a_1 = 1, a_2 = 2, a_{n+2} = a_{n+1} + a_n$. Prove $S_n = a_{n+2} - 2$. | Existing 5.5 (classic) | 2 |
| 5.5 | (NEW) **IMO 1986, Problem 3.** Each vertex of a regular pentagon is assigned an integer; their sum is positive. If three consecutive vertices have integers $x, y, z$ with $y < 0$, the operation replaces them with $(x+y, -y, z+y)$. Prove the process terminates. | IMO 1986 P3 | 3 |
| 5.6 | (NEW, designed) Sequence invariant: $a_1 = a_2 = 1$ and $a_{n+1} = (a_n^2 + 2)/a_{n-1}$ for $n \geq 2$. Show that every $a_n$ is a positive integer, and that the quantity $a_{n+1} a_{n-1} - a_n^2$ takes the same value for all $n$. | JEE Adv (designed) | 2 |
| 5.7 | (NEW, designed) Lattice walk: a particle on $\mathbb{Z}^2$ starts at the origin; each step is a knight-move-doubled, i.e., $(\pm 2, \pm 1)$ or $(\pm 1, \pm 2)$. Identify a linear invariant of position and use it to determine the set of all reachable points. | JEE Adv (designed) | 2 |

**Confirmed with Anand (May 13):** IMO 1986 P3 stays as 5.5; problems 5.6 and 5.7 are my designs at JEE Advanced level (not IMO). The chapter's IMO-tier coverage is concentrated in Worked Example 4.3 (IMO 1988 P6 — Vieta jumping); practice problems lean to the audience's actual operating range, with 5.5 as a single stretch problem.

### 6. The Connections Web  *(Tao)*

#### 6.1 Invariance Across Mathematical Domains
1 paragraph each: Algebra (Vieta, determinant) · Geometry (Euclidean, projective, topological — Klein again) · Analysis (parametrization-invariant integration; Parseval) · Number Theory (orbit invariants under the modular group) · Combinatorics (parity arguments, double counting) · Topology (Euler characteristic, fundamental group).

#### 6.2 Invariance in Physics & Other Sciences
Energy / momentum / charge conservation. Loop invariants in CS. Budget constraints in economics. Hardy–Weinberg equilibrium in population genetics. Brief — the connections, not the primer.

#### 6.3 Cross-Domain Manifestations Outside Mathematics
4–6 instances, one sentence each: economics, computer science, biology, information theory.

#### 6.4 Related Archetypes
Forward pointers: **#2 Symmetry** (via Noether) · **#9 Domain Constraints** (as filter, after invariance generates candidates) · **#17 Degrees of Freedom** (each invariant kills one DOF) · **#12 Extremal Principles** (Lagrange multipliers = optimization subject to invariant constraints).

≈ 700 words total.

### 7. Master Takeaways  *(Polya / Joshi)*

Existing 7 takeaways preserved largely verbatim — they are crystalline. Wording polish only. Add 1 if a strong new candidate emerges during drafting (only if it earns its place).

### 8. Self-Assessment Checklist

Existing 7 checkpoints preserved with light language polish. Add 1 new: *"Can I formulate Noether's Theorem in plain English?"* — connects forward to Chapter 2.

### Bridge to Chapter 2: Symmetry  *(Polya)*

Existing bridge largely preserved, tightened. Insert one explicit Noether-bridge sentence:
*"Where Invariance asks 'what doesn't change?', Symmetry asks 'what looks the same?' Noether's theorem will tell us, in Chapter 2, that these are the same question viewed from opposite sides."*

≈ 300 words.

---

## Items requiring Anand's decision before I draft any prose

1. **Worked Example 2** — mutilated-chessboard generalization. Right level, or substitute? (My instinct: keep, but I want your call.)
2. **Worked Example 3** — IMO 1988 P6 in Chapter 1, or move to Pillar 3 and use a tamer cousin here? (My instinct: keep IMO 1988 P6 here; use IMO 2001 P6 in Pillar 3.)
3. **Practice problem 5.5** — IMO 1986 P3 cited from memory; please verify or substitute.
4. **Practice problems 5.6, 5.7** — designed by me; substitute freely if you have stronger problems in mind.
5. **Length** — ≈ 7,000 words target. Acceptable, or compress to ≈ 5,500?
6. **Chapter-end appendix vs in-text solutions** — do practice-problem solutions live at the end of the chapter, or as a separate `01-invariance-solutions.md` file? (My instinct: in-chapter appendix, so reader doesn't lose context.)

---

🌑
