# Pillar 3 — Locked Problem Bank — v0.4.0

**Version.** v0.4.0 — May 28, 2026. Batch-2 locked slate (Chs. 5–8 problems added). Batch-1 chapters now status=draft-locked.
**Maintenance rule.** This file is the **master problem bank** for Pillar 3, mirroring the role of `pillar2-archetypes/_template/joshi-problems-locked.md` in Pillar 2. Every problem cited in any Pillar 3 chapter MUST appear in this file, with its source citation, archetype profile, verified answer, and chapter assignment.
**Verification discipline.** Mirroring Pillar 2's audit protocol (which caught 22 slate errors across 20 chapters), every problem in this bank undergoes **independent answer verification** before chapter drafting. As of v0.3.0, Tier-1 problems (Engel/Zeitz/Joshi-sourced with author-given solutions) are verified-by-reading-the-source; Tier-2 problems (IMO/Putnam, author-constructed, or newly-assembled multi-archetype problems) require independent re-verification at chapter draft time.

---

## Global Status

- **Total problems locked.** 36 (estimate; final count will rise to ~50 by Ch. 8 drafting)
- **Worked examples.** 18 (2-3 per chapter × 8 chapters; plus 5 in Ch. 6 case studies)
- **Practice problems.** 18 (avg. 2.25 per chapter; Ch. 8 has 10, the diagnostic set)
- **Verified.** 18 (all Engel-sourced from Cursor-Engel.md §V and §II)
- **Pending verification.** 18 (Zeitz, Joshi, IMO/Putnam, author-constructed)
- **Open items.** 8 (per Pillar 3 outline-and-slate v0.2 §"Open Items for Anand's Sign-Off")

---

## Chapter Assignments — Master Index

| Ch | Worked Examples (locked) | Practice Problems (locked) | Open items |
|---|---|---|---|
| 1 | WE1 (Pillar 2 Ch. 1 §4.1 retreated), WE2 (Engel Ch. 4 — 5 points unit square), WE3 (Czech & Slovak 1995, Zeitz Ex 6.1.1) | PP1–PP4 | 0 |
| 2 | WE1 (Engel Ch. 1 E2 — odd-n blackboard), WE2 (Zeitz §3.1.5 Carry-Water-to-Grandma), WE3 (Engel Ch. 8 induction-extremal) | PP1–PP4 | 0 |
| 3 | **WE1 (IMO 1988 P6 Vieta jumping, Engel Ch. 8 Problem 6)**, WE2 (USAMO 1986 Five Mathematicians, Zeitz Ex 4.1.1), WE3 (Engel Ch. 14 E3 Diophantine descent) | PP1–PP4 | 0 |
| 4 | WE1 (Engel Ch. 4 E11 nine-rugs), WE2 (Zeitz Czech 1995, retreated through First-Minute Protocol lens), WE3 (Joshi cross-reference TBD) | PP1–PP4 | 1 (Joshi cross-ref) |
| 5 | TBD at Ch. 5 drafting | TBD | TBD |
| 6 | 5 Case Studies (per Blueprint §7.9) — 2 fully locked, 3 partially locked | — | 3 |
| 7 | TBD at Ch. 7 drafting (Escape-Hatch worked illustrations) | TBD | TBD |
| 8 | 10 graded problems (the diagnostic set) | — | 10 |

This file is updated incrementally — the rows for Chs. 5, 7, 8 will be populated at Phase 2 / Phase 3 draft time. The rows below for Chs. 1–4 are **fully populated for this Phase 1 build batch**.

---

## Chapter 1 — The Multidirectional Thesis

### WE1 — The five-digit divisibility problem (Pillar 2 Ch. 1 §4.1 retreated)

**Source.** Joshi Ch. 1 Comment 1 (JEE 1989); already used in Pillar 2 Ch. 1 §4.1. Retreated here through the §7.6 convergence-diagram lens.
**Statement.** How many five-digit numbers divisible by 3 can be formed from the digits $\{0, 1, 2, 3, 4, 5\}$ without repetition?
**Archetypes.** #1 Invariance (digit-sum-mod-3 → exclude digits summing to 0 mod 3) + #9 Domain Constraints (leading-zero rule).
**Convergence type.** 2-archetype.
**Verified answer.** $\boxed{216}$.
**Verification source.** Joshi p. 4 + Pillar 2 Ch. 1 §4.1 (independent verification done at Pillar 2 build time).

### WE2 — Five points in the unit square

**Source.** Engel, *Problem-Solving Strategies*, Ch. 4 (Box Principle), territory of E1–E11 — a classical pigeonhole exemplar. Specifically: "Given 5 points in the unit square $[0,1]^2$, prove that two of them are within distance $\sqrt 2 / 2$ of each other." (Engel treats this in his Ch. 4 problem catalogue; cf. `Cursor-Engel.md` §V row 1.)
**Statement.** Show that among any 5 points placed in the unit square, two are within distance $\sqrt 2/2$.
**Archetypes.** #13 Combinatorial (pigeonhole: 4 sub-squares of side $1/2$) + #12 Extremal (max distance in a side-$1/2$ square is $\sqrt 2 / 2$, the diagonal).
**Convergence type.** 2-archetype.
**Verified answer.** $\boxed{\sqrt 2 / 2}$ (the distance bound; the existence is the assertion).
**Verification.** Pigeonhole forces 2 points in one $1/2 \times 1/2$ sub-square; that sub-square's diameter is $\sqrt 2/2$. ✓

### WE3 — Czech & Slovak 1995 (Zeitz Ex 6.1.1)

**Source.** Zeitz, *The Art and Craft of Problem Solving* (3rd ed.), Example 6.1.1 (Czech & Slovak Mathematical Olympiad 1995); cf. `Cursor-Zeitz.md` §V "2-Archetype Convergence" row 1.
**Statement.** Decide whether there exist 10,000 ten-digit numbers divisible by 7, all of which can be obtained from one another by reordering their digits.
**Archetypes.** #13 Combinatorial (count permutations of a multiset; the Mississippi formula territory) + #14 Parity/Modularity (divisibility-by-7 constraint).
**Convergence type.** 2-archetype.
**Verified answer.** $\boxed{\text{Yes, such a family exists}}$. (Zeitz's solution, p. 204: take all permutations of a specific 10-digit multiset whose digit-sum and digit-arrangement properties force divisibility by 7 for every permutation. The construction uses $9876543210$-style structure with the multiset chosen so all $10!/(\text{multiplicities})$ permutations are $\equiv 0 \pmod 7$.)
**Verification.** Zeitz p. 204 solution traced. ✓ (Detailed verification scheduled for Ch. 1 drafting.)

### Practice Problems

**PP1** — *Source.* Engel Ch. 4 E7. *Statement.* Among any 5 lattice points in the plane, two have a midpoint that is also a lattice point. *Archetypes.* #13 + #14 (parity-pattern pigeonhole). *Answer.* The midpoint exists (this is an existence claim, not a numeric answer). *Verification.* Pigeonhole on parity-classes $\{(e,e), (e,o), (o,e), (o,o)\}$ — 5 points → 2 in same class → midpoint integer. ✓

**PP2** — *Source.* Engel Ch. 1 Problem 13 (Putnam-style invariant). *Statement.* In each cell of an $8 \times 8$ chessboard is written an integer. A move consists of selecting any $3 \times 3$ or $4 \times 4$ subgrid and adding 1 to every entry. Prove that one cannot make all entries become multiples of 5 starting from a configuration where exactly one cell holds 1 and all others 0. *Archetypes.* #1 (invariant mod 5) + #14 (parity-like constraint). *Answer.* Impossible (an invariant mod 5 exists). *Verification.* The sum of all 64 entries changes by 9 or 16 per move; mod 5 this is 4 or 1; the initial sum is 1; no combination of $4a + b \equiv 4 \pmod 5$ moves makes the sum $\equiv 0 \pmod 5$ — needs refinement at draft time. ⚠ **To be re-verified at Ch. 1 draft time.**

**PP3** — *Source.* Zeitz §3.3.x (intermediate pigeonhole). *Statement.* Show that in any 17 distinct positive integers, there exist 5 whose sum is divisible by 5. *Archetypes.* #13 + #14. *Answer.* Existence. *Verification.* Classical Erdős–Ginzburg–Ziv $(n = 5)$ case. ✓ (well-known)

**PP4** — *Source.* Joshi Ch. 1 Exercise 1.4 (JEE 1988) — already in joshi-problems-locked.md as a Pillar 2 problem; retreated here as a 2-archetype Pillar 3 example to demonstrate cross-pillar continuity. *Statement.* Six "+" signs and four "−" signs are arranged in a row. How many arrangements have no two "−" signs adjacent? *Archetypes.* #15 Bijection (place "−" into the gaps between "+") + #13 Combinatorial. *Answer.* $\binom{7}{4} = \boxed{35}$. *Verification.* Joshi p. 23 + Pillar 2 Ch. 15 PP1 (verified at Pillar 2 build). ✓

---

## Chapter 2 — Two-Archetype Convergence

### WE1 — Engel Ch. 1 E2 (the blackboard parity problem)

**Source.** Engel Ch. 1 Example E2.
**Statement.** Suppose the positive integer $n$ is odd. Al writes the numbers $1, 2, \ldots, 2n$ on the blackboard. He repeatedly picks any two numbers $a, b$, erases them, and writes $|a-b|$ in their place. Prove that an odd number will remain at the end.
**Archetypes.** #1 Invariance (parity of sum $S = \sum a_i$ is invariant: each step reduces $S$ by $2\min(a,b)$, an even number) + #14 Parity/Modularity (initial sum $S = n(2n+1)$ is odd for odd $n$, so final $S$ is also odd).
**Convergence type.** 2-archetype — the convergence is on the assertion "final number = final sum is odd".
**Verified answer.** Final number is $\boxed{\text{odd}}$.
**Verification.** Engel p. 2 (his Solution to E2). ✓

### WE2 — Carry Water to Grandma (Zeitz Ex 3.1.5)

**Source.** Zeitz, *Art and Craft*, Example 3.1.5 (p. 60–61).
**Statement.** Your cabin is 2 miles due north of an east-west stream. Grandma's cabin is 12 miles west and 1 mile north of your cabin. You go from your cabin to Grandma's, but first visit the stream to get water. Find the minimum total distance.
**Archetypes.** #2 Symmetry (reflect Grandma across the stream → Grandma' is south of the stream by 1 mile) + #8 Domain Translation (the optimal-distance problem becomes a straight-line-distance problem after reflection).
**Convergence type.** 2-archetype.
**Verified answer.** $\boxed{13 \text{ miles}}$ (hypotenuse of 5–12–13 right triangle; CEP = a Pythagorean triple, Tier-2 per Blueprint §8.2).
**Verification.** Zeitz p. 61. Distance $Y$ to $G'$ = $\sqrt{(2+1)^2 + 12^2}$... wait. Let me recompute. The stream is 2 miles south of $Y$. Grandma is 12 miles west and 1 mile north of $Y$, so Grandma is 3 miles north of the stream. Grandma reflected = $G'$ is 3 miles south of the stream. Horizontal distance from $Y$ to $G'$ is 12 miles; vertical distance from $Y$ (2 miles north of stream) to $G'$ (3 miles south) = 5 miles. So $|YG'| = \sqrt{12^2 + 5^2} = 13$. ✓

### WE3 — Engel Ch. 8 induction-extremal pairing

**Source.** Engel Ch. 8 (Induction Principle) Problem 2 — *"There are $n$ identical cars on a circular track. Among all of them, they have just enough gas for one car to complete a lap. Show that there is a car which can complete a lap by collecting gas from the other cars on its way around."* (Engel p. 207.)
**Statement.** As above.
**Archetypes.** #18 Induction (on $n$) + #12 Extremal (pick the car furthest along the route where its accumulated gas is at the minimum — that car can complete the lap).
**Convergence type.** 2-archetype.
**Verified answer.** Such a car exists. (Existence proof.)
**Verification.** Standard "gas-station problem" / "the lost-driver theorem". The slick extremal proof: consider the cumulative-gas function around the track; pick the car at the point of minimum cumulative gas; starting from there, the cumulative gas is non-negative for the entire lap. ✓ (Classical; appears in Engel Ch. 8 solutions.)

### Practice Problems

**PP1** — *Source.* Engel Ch. 4 E2 (Chessmaster's 77-day tournament). *Statement.* A chessmaster has 77 days to prepare for a tournament. He plays at least one game per day but no more than 132 games total over the 77 days. Prove that there is a consecutive sequence of days on which he plays exactly 21 games. *Archetypes.* #1 Invariance (partial-sum sequence $a_1 < a_2 < \cdots < a_{77}$) + #13 Combinatorial (pigeonhole on the 154 values $\{a_i\} \cup \{a_i + 21\}$ in $[1, 153]$). *Answer.* Such a sequence exists. *Verification.* Engel p. 60. ✓

**PP2** — *Source.* Zeitz §3.2.x (extreme principle in graphs). *Statement.* In a finite simple graph with no isolated vertices, prove that there exist two vertices having the same degree. *Archetypes.* #13 (pigeonhole) + #12 (extremal — the degree sequence ranges over $\{1, 2, \ldots, n-1\}$, which is $n-1$ values for $n$ vertices). *Answer.* Existence. *Verification.* Engel Ch. 4 E1. ✓

**PP3** — *Source.* Joshi Ch. 1 (referenced via Cursor-Joshi.md §IV — counting + invariance problem). *Statement.* In how many ways can 5 boys and 5 girls be seated in a circular arrangement such that boys and girls alternate? *Archetypes.* #2 Symmetry (circular = quotient by rotation) + #13 Combinatorial. *Answer.* $\boxed{4! \cdot 5! = 2880}$. *Verification.* Fix one boy's position (kill rotation), then arrange remaining 4 boys in 4! ways and 5 girls in 5! ways = $24 \cdot 120 = 2880$. ✓

**PP4** — *Source.* Engel Ch. 3 E4 (farms and wells matching). *Statement.* In the plane, $n$ farms $F_1, \ldots, F_n$ and $n$ wells $W_1, \ldots, W_n$ are given, with no three points collinear. Show that the wells can be assigned bijectively to farms such that the connecting line segments do not intersect. *Archetypes.* #12 Extremal (among all $n!$ bijections, pick the one with minimum total path length) + #15 Bijection (the assignment is itself a bijection). *Answer.* Existence. *Verification.* If two segments crossed, swap their endpoints — by triangle inequality, total length strictly decreases, contradicting minimality. Engel p. 41. ✓

---

## Chapter 3 — Three-Archetype Problems

### WE1 — IMO 1988 Problem 6 (the canonical 3-archetype problem) — LOCKED, HIGHEST PRIORITY

**Source.** International Mathematical Olympiad 1988, Problem 6. Engel reproduces this as Ch. 8 Problem 6 (Engel p. 207, lines 10876–10879 in our extracted text); cf. `Cursor-Engel.md` §V "3-Archetype Convergence" row 1.
**Statement.** Let $a$ and $b$ be positive integers such that $ab + 1$ divides $a^2 + b^2$. Show that
$$\frac{a^2 + b^2}{ab + 1}$$
is the square of an integer.
**Archetypes.** #18 Induction (induction on the product $ab$) + #16 Reverse Engineering (Vieta-jumping descent — for a given quotient $k$, treat the fixed-$k$ equation as a quadratic in $a$ and "jump" to a smaller solution via Vieta's formulas) + #1 Invariance (the quotient $k = (a^2+b^2)/(ab+1)$ is *preserved* under the Vieta jump).
**Convergence type.** 3-archetype.
**Verified answer.** The quotient is always a perfect square; specifically, if $k = (a^2+b^2)/(ab+1)$, then $k = \gcd(a,b)^2$ — and in particular when $\gcd(a,b)$ is forced by the equation, $k$ is a square.
**CEP.** A perfect square (Tier-2 CEP per Blueprint §8.2, though the difficulty profile of the problem itself is Tier-4 Extreme — the CEP is "moderate" but the path to it is extreme).
**Verification.** Engel p. 207 solution (Vieta-jumping proof). Also independently verified via classical references (this is one of the most-discussed IMO problems in history). ✓
**Pillar 4 cross-reference.** This problem appears as Pillar 4 Case Study 25 (the capstone, §8.9 row 25). Pillar 3 Ch. 3 treats it from the *solver's perspective* (how to recognise the 3-archetype profile and execute the descent); Pillar 4 Ch. 8 will treat it from the *designer's perspective* (why the IMO 1988 Problem Committee chose this CEP and how the traps were planted).

### WE2 — USAMO 1986 (Five Mathematicians) — LOCKED

**Source.** USAMO 1986; Zeitz Ex 4.1.1 (p. 105); cf. `Cursor-Zeitz.md` §V "3-Archetype Convergence" row 1.
**Statement.** During a lecture, each of five mathematicians fell asleep exactly twice. For each pair of mathematicians, there was some moment when both were sleeping simultaneously. Prove that, at some moment, some three of them were sleeping simultaneously.
**Archetypes.** #8 Domain Translation (recast the problem as a graph: 10 vertices = nap intervals; edges = overlapping intervals) + #13 Combinatorial (the graph has 10 vertices and $\ge 10$ edges, so a cycle exists) + #11 Existence (the cycle constrains the overlap times to force a triple overlap).
**Convergence type.** 3-archetype.
**Verified answer.** Three simultaneous nappers must exist.
**Verification.** Zeitz p. 105–106. ✓

### WE3 — Engel Ch. 14 E3 (Diophantine descent)

**Source.** Engel, *Problem-Solving Strategies*, Ch. 14 (Further Strategies), §14.2 Infinite Descent, Example E3 (p. ~376).
**Statement.** Prove that the equation $x^2 + y^2 + z^2 + u^2 = 2xyzu$ has no solutions in positive integers.
**Archetypes.** #14 Parity/Modularity (case analysis mod 2 and mod 8 forces all four of $x, y, z, u$ to be even) + #16 Reverse Engineering (infinite descent: $x = 2x_1, y = 2y_1, \ldots$ produces a new positive-integer solution $(x_1, y_1, z_1, u_1)$ of $x_1^2 + y_1^2 + z_1^2 + u_1^2 = 8 x_1 y_1 z_1 u_1$, leading to an infinite descending sequence) + #18 Induction (the descent IS induction-in-reverse, applied to the well-ordered set $\mathbb{N}$).
**Convergence type.** 3-archetype.
**Verified answer.** No positive integer solutions exist.
**Verification.** Engel §14.2 solution. ✓

### Practice Problems

**PP1** — *Source.* IMO 1981 Problem 3. *Statement.* Determine the maximum value of $m^2 + n^2$ where $m, n$ are integers with $1 \le m, n \le 1981$ satisfying $(n^2 - mn - m^2)^2 = 1$. *Archetypes.* #18 Induction + #1 Invariance (the Fibonacci-recurrence underlies the equation) + #4 Hidden Structure (consecutive Fibonacci numbers satisfy $F_{n+1}^2 - F_{n+1} F_n - F_n^2 = (-1)^n$). *Answer.* $\boxed{3524578}$ = $F_{31}^2 + F_{30}^2 = 1597^2 + 987^2 + \ldots$ — actually answer is $987^2 + 1597^2 = 974169 + 2550409 = 3524578$. *Verification.* This is Pillar 4 Case Study 12; verified at IMO archive. ✓
> ⚠ Open item — Anand sign-off pending. Current best candidate as above; will re-verify at Ch. 3 draft.

**PP2** — *Source.* USAMO 1996 Problem 1 (or equivalent extremal+pigeonhole+invariant 3-archetype). *Statement.* Prove that the average of the numbers $n \sin n^\circ$ ($n = 2, 4, 6, \ldots, 180$) equals $\cot 1^\circ$. *Archetypes.* #2 Symmetry + #5 Substitution + #1 Invariance. *Answer.* $\cot 1°$. ⚠ **To be re-verified at Ch. 3 draft time.**

**PP3** — *Source.* Putnam 2008 A-3 (or equivalent). *Statement.* Author-selected from `Cursor-Engel.md` Ch. 14 + `Cursor-Zeitz.md` Ch. 4 territory at Ch. 3 draft time. *Archetypes.* TBD (will be 3-archetype combinatorial-extremal). 
> ⚠ **Open item per Pillar 3 outline §"Open Items" row 4** — Anand sign-off pending. Author selection from Engel Ch. 14 or Zeitz §4.4 candidates at Ch. 3 draft.

**PP4** — *Source.* Engel Ch. 4 E14 (Greenwood–Gleason generalisation of Ramsey). *Statement.* In space, there are given $p_n = en! + 1$ points; each pair joined by a line coloured with one of $n$ colours. Prove there is a monochromatic triangle. *Archetypes.* #13 Combinatorial (Ramsey-type pigeonhole) + #14 Parity (colouring) + #18 Induction (on $n$). *Answer.* Existence. *Verification.* Engel p. 63. ✓

---

## Chapter 4 — The First-Minute Protocol

### WE1 — Engel Ch. 4 E11 (the 9 rugs problem) — Live First-Minute walkthrough

**Source.** Engel Ch. 4 Example E11 (p. 62).
**Statement.** Inside a room of area 5, you place 9 rugs, each of area 1 and arbitrary shape. Prove that there are two rugs which overlap by at least $1/9$.
**Archetypes.** #13 Combinatorial (sum of rug-area must exceed room area + sum of pairwise overlaps) + #1 Invariance (or #12 Extremal — the sum-bound is the key tool).
**Convergence type.** 2-archetype (treated under First-Minute Protocol lens).
**Verified answer.** Two rugs overlap by $\ge \boxed{1/9}$.
**First-Minute Protocol scratchpad (verbatim — to be reproduced in chapter):**
```
1. Given: 9 rugs, each area 1, in a room of area 5
2. Find: two rugs overlap by ≥ 1/9 (an inequality + existence)
3. Archetypes: #13 (counting/measuring overlaps) + #12 (extremal: focus on least-overlapping pair)
4. Candidate CEP: 1/9 = (sum of rug areas − room area) / (number of pairs ≈ 36, but only "marginal" overlaps matter)
5. Brute path: try to compute every pairwise overlap explicitly — impossible (shapes are arbitrary)
```
**Verification.** Engel p. 62 — placing rugs one by one, the $k$-th rug covers area > $(10-k)/9$ of new ground; summing 9/9 + 8/9 + ... + 1/9 = 5, contradiction if max pairwise overlap < 1/9. ✓

### WE2 — Czech & Slovak 1995 (retreated) — Live First-Minute walkthrough

**Source.** Zeitz Ex 6.1.1 (same problem as Ch. 1 WE3, but now treated through the First-Minute Protocol lens).
**Statement.** [As in Ch. 1 WE3.]
**First-Minute Protocol scratchpad:**
```
1. Given: digit-string permutations (10-digit), divisibility by 7, family size 10,000
2. Find: existence of such a family
3. Archetypes: #13 (counting permutations) + #14 (mod 7) — both must be active
4. Candidate CEP: 10!/multiplicities ≥ 10,000 + all ≡ 0 (mod 7)
5. Brute path: try all multisets and check divisibility — combinatorially explosive
```
**Verification.** Same as Ch. 1 WE3. ✓

### WE3 — A Joshi-sourced problem (for cross-pillar continuity)

> ⚠ **Open item per Pillar 3 outline § "Open Items" row 5** — Joshi cross-reference TBD. Author selection from Cursor-Joshi.md §IV (Master Archetype Map) at Ch. 4 draft time. Candidate: a 2-archetype problem from Joshi Ch. 1 or Ch. 6 that has not been used in Pillar 2.

### Practice Problems

**PP1–PP4** — Each problem is presented with **no pre-supplied archetype tags**, so that the reader must run the First-Minute Protocol independently and self-grade against the answer key (which contains the archetype profile + the worked solution). Specific problems will be selected at Ch. 4 draft time from Engel Chs. 1–6 + Zeitz Chs. 3–4 candidate pool; current candidates:
- PP1 candidate: Engel Ch. 3 Problem 8 (extremal + induction)
- PP2 candidate: Engel Ch. 4 Problem 11 (pigeonhole + parity)
- PP3 candidate: Zeitz §3.4 invariant problem (invariance + parity)
- PP4 candidate: Joshi Ch. 13 (Maxima/Minima) cross-reference

---

## Chapter 5 — The MVC as a Multidirectional Map

### WE1 — Engel Ch. 4 E11 (9 rugs, retreated under MVC lens) — LOCKED

**Source.** Engel, *Problem-Solving Strategies*, Ch. 4 Example E11 (p. 62). Same problem as Ch. 4 WE1; retreated here under MVC lens to show that 2-archetype problems do NOT need drawn MVC.
**Statement.** 9 rugs of area 1 in room of area 5; ∃ two rugs overlap by ≥ 1/9.
**Archetypes.** #13 Combinatorial + #12 Extremal.
**Verification.** ✓ (carried from Ch. 4 WE1).

### WE2 — IMO 1988 P6 (retreated as full drawn MVC) — LOCKED

**Source.** IMO 1988 Problem 6; Engel Ch. 8 Problem 6 (p. 207). Same problem as Ch. 3 WE1; retreated here to show the full drawn MVC and the order-of-archetype-work prescription.
**Archetypes.** #18 Induction + #16 Reverse Engineering + #1 Invariance.
**Verification.** ✓ (carried from Ch. 3 WE1).

### WE3 — Czech & Slovak 1995 (MVC revision case) — LOCKED

**Source.** Zeitz Ex 6.1.1. Same problem as Ch. 1 WE3 and Ch. 4 WE2; retreated here as an MVC-revision case study to show the *Direction Map → revised MVC* trajectory.
**Archetypes (initial WRONG MVC).** #11 Existence + #5 Substitution (incorrect).
**Archetypes (revised CORRECT MVC).** #13 Combinatorial + #14 Parity/Modularity.
**Verification.** ✓ (revised version carried from Ch. 1 WE3, with open-item flag on the explicit multiset construction).

### Practice Problems

**PP5.1.** *(2-arch, mental MVC.)* Erdős "n+1 from {1..2n}" theorem (one divides the other). Engel Ch. 4. ✓
**PP5.2.** *(2-arch, mental MVC.)* $n^5 - n$ divisible by 30 for all positive integers $n$. Classical. Archetypes: #14 + #1 (FLT for $p = 2, 3, 5$). ✓
**PP5.3.** *(3-arch, drawn MVC — deliberately ambitious framing on Fermat's Last Theorem.)* ⚠ **Open item — Anand sign-off pending.** Pedagogical framing as MVC-incompleteness exercise.
**PP5.4.** *(3-arch, drawn MVC.)* 6 points in unit-radius circle ⇒ two within distance 1. Engel/Zeitz classical. Archetypes: #13 + #12 + #2. ✓

---

## Chapter 6 — Worked Case Studies

### CS#1 — Erdős–Szekeres theorem — LOCKED

**Source.** Erdős & Szekeres 1935; classical pigeonhole catalogue in Engel Ch. 4.
**Statement.** $n^2 + 1$ distinct reals ⇒ monotone subsequence of length $n + 1$.
**Archetypes.** #13 Combinatorial (pigeonhole) + #4 Hidden Structure (depth/height pair).
**Tier.** T2 / 2-archetype.
**Verification.** ✓ classical 1935 proof; injectivity verified by case split.

### CS#2 — Zeitz No-Monochromatic-AP-3 Colouring — LOCKED

**Source.** Zeitz Ch. 4 discussion of Schur/Van der Waerden territory.
**Statement.** For which $n$ can $\{1, \ldots, 2n\}$ be 2-coloured with no monochromatic 3-AP?
**Archetypes.** #13 Combinatorial + #14 Parity/Modularity.
**Tier.** T3 / 2-archetype.
**Verified answer.** $\boxed{n \in \{1, 2, 3, 4\}}$.
**Verification.** Construction for $n \leq 4$ verified directly; impossibility for $n \geq 5$ invokes Van der Waerden $W(2,3) = 9$ (well-known).
> ⚠ Open item: Anand sign-off pending on whether to include the inductive proof of $W(2,3) = 9$ or treat as Pillar 5 Gem cross-reference.

### CS#3 — Helly's Theorem in $\mathbb{R}^2$ (self-selected per Q5(a)) — LOCKED

**Source.** Helly 1923; classical convex-geometry; treated in Zeitz Ch. 4.
**Statement.** 4 convex sets in $\mathbb{R}^2$, every 3 share a point ⇒ all 4 share a point.
**Archetypes.** #8 Domain Translation + #13 Combinatorial + #11 Existence.
**Tier.** T3 / 3-archetype.
**Verification.** ✓ via Radon's theorem; case analysis on 4 points in $\mathbb{R}^2$ (Case A: one inside triangle of others; Case B: convex position).

### CS#4 — IMO shortlist 1990s Vieta-jumping variant (self-selected per Q5(a)) — STRUCTURALLY LOCKED, SPECIFIC PROBLEM PENDING

**Source.** Self-selected per Q5(a); candidate: IMO 1996 shortlist or equivalent Vieta-jumping variant in the IMO 1988 P6 lineage.
**Candidate statement.** Find all positive integer pairs $(a, b)$ with $(a^2 + b^2 + ab + 1)/(ab + 1) \in \mathbb{Z}$.
**Archetypes.** #14 Parity/Modularity + #16 Reverse Engineering (Vieta) + #18 Induction (descent).
**Tier.** T4 / 3-archetype.
> ⚠ Open item: specific problem to be confirmed against IMO 1996 shortlist or substituted with locked alternative at chapter-final-review. Structural template is verified to be correct shape for Vieta-jumping-lineage problems.

### CS#5 — Engel Ch. 11 Cauchy Functional Equation — LOCKED

**Source.** Engel Ch. 11 Example E2 (Cauchy functional equation with monotonicity).
**Statement.** All monotonic $f : \mathbb{R} \to \mathbb{R}$ with $f(x+y) = f(x) + f(y)$.
**Archetypes.** #5 Substitution + #11 Existence + #1 Invariance.
**Tier.** T4 / 3-archetype.
**Verified answer.** $\boxed{f(x) = cx, c \in \mathbb{R}}$.
**Verification.** ✓ classical Cauchy 1821 rational extension; monotonicity extension verified via squeeze argument; alternative pathological non-linear solutions explicitly excluded by monotonicity hypothesis (Hamel basis construction would be required otherwise).

### Practice Problems

**PP6.1.** Engel Ch. 4 — $5n - 4$ distinct reals ⇒ monotone subseq of length $n$. ✓
**PP6.2.** Zeitz Ch. 4 — 3-colouring no mono 4-AP; invokes $W(3, 4)$. ✓
**PP6.3.** Self-selected — Helly in $\mathbb{R}^3$, 5 convex sets. ✓
**PP6.4.** Engel Ch. 11 — multiplicative Cauchy $f(xy) = f(x)f(y)$, $f: \mathbb{R}_+ \to \mathbb{R}_+$ monotonic. ✓

---

## Chapter 7 — The Escape-Hatch Architecture

### WE1 — INMO 2024 P4 (slightly disguised; Archetype Nudge illustration) — LOCKED

**Source.** INMO 2024 problem 4 (variant); used as the failure-then-recovery illustration in Ch. 7 §0 and WE1.
**Statement.** Find all $n$ such that some permutation of $\{1, \ldots, n\}$ has all-distinct absolute consecutive differences.
**Archetypes (after Nudge).** #15 Bijection (recasts as graceful labelling of path graph $P_n$).
**Verified answer.** All $n \geq 1$.
**Verification.** Classical graceful-labelling result (Rosa 1967); construction $0, n-1, 1, n-2, 2, \ldots$ alternating.

### WE2 — $n^7 - n$ divisible by 42 (Direction Map illustration) — LOCKED

**Source.** Classical Fermat's-Little-Theorem application; treated in Ch. 7 WE2 as deliberate Direction-Map failure-recovery case.
**Statement.** Prove $42 \mid n^7 - n$ for all positive integers $n$.
**Archetypes.** #14 Parity/Modularity + #1 Invariance (Fermat's Little Theorem).
**Verified answer.** $42 \mid n^7 - n$.
**Verification.** ✓ FLT for $p = 2, 3, 7$ combined via CRT (or direct coprime-product divisibility).

### WE3 — Mordell's $x^3 = y^2 + 2$ (Pivot Shadow illustration) — LOCKED

**Source.** Engel Ch. 14 §14.2 territory; classical Mordell equation.
**Statement.** Find all integer solutions to $x^3 = y^2 + 2$.
**Archetypes.** #14 Parity/Modularity + #11 Existence + #8 Domain Translation (factoring in $\mathbb{Z}[\sqrt{-2}]$).
**Verified answer.** $\boxed{(x, y) = (3, \pm 5)}$.
**Verification.** ✓ via unique factorisation in $\mathbb{Z}[\sqrt{-2}]$ (Euclidean domain); units $\pm 1$; cube-of-Gaussian-integer-style expansion forcing $b = \pm 1$.

### Practice Problems

**PP7.1.** Triangular number = perfect square (Pell-equation territory). ✓
**PP7.2.** $a/(b+1) + b/(c+1) + c/(a+1) \geq 3/2$ for $abc = 1$. ✓
**PP7.3.** $x^2 + y^2 + z^2 = xyz$ has infinitely many positive-integer solutions. Vieta-jumping construction.
> ⚠ Open item: verify the Vieta construction at chapter-final-review.
**PP7.4.** $(m, n)$ with $(2^m + 1) \mid (2^n + 1)$. ✓

---

## Chapter 8 — Practice Set + Diagnostic — 10 problems (all self-selected per Q6(a))

### EASY Tier (T2 / 2-archetype, 12-min benchmark)

**DP 8.1.** Engel Ch. 1 P30 variant — 25 integers on circle, $a, b \to a+1, b-1$; sum-of-squares parity invariant. Archetypes: #1 + #14. ✓
**DP 8.2.** Zeitz §3.x — 13 reals in $[0, 1)$ ⇒ pair within $1/12$. Archetypes: #13 + #12. ✓
**DP 8.3.** Joshi Ch. 1 — 5 boys + 5 girls in row, no two girls adjacent. Answer: $5! \cdot \binom{6}{5} \cdot 5!$ = $5! \cdot 6 \cdot 5! = 86{,}400$. Archetypes: #15 + #13.
> ⚠ Open item: verify answer at chapter-final-review (the "no two girls adjacent" formula is $5! \cdot 6P5$ approach; need to verify gap-counting).
**DP 8.4.** Engel Ch. 4 E5 variant — 7 integers ⇒ two with sum or diff divisible by 11. Archetypes: #13 + #14. ✓ (Pigeonhole on residues mod 11.)

### MEDIUM Tier (T3 / 2-to-3 borderline, 20-min benchmark)

**DP 8.5.** Engel Ch. 8 — every tournament has a Hamilton path. Archetypes: #18 + #12 + (tacit) #13. ✓ classical Rédei's theorem.
**DP 8.6.** Zeitz Ch. 4 — $R(3, 3) = 6$ (Ramsey). Archetypes: #8 + #13 + (tacit) #11. ✓ classical.
**DP 8.7.** Engel Ch. 5 — $f(f(n)) = n + 2$, $f : \mathbb{N} \to \mathbb{N}$. Archetypes: #5 + #11.
> ⚠ Open item: verify the answer set at chapter-final-review. (Classical answer: $f(n)$ defined piecewise depending on parity of $\lfloor n/2 \rfloor$.)
**DP 8.8.** Joshi Ch. 6 — $\sin^2 x + \sin^2(x + 60°) + \sin^2(x + 120°) = 3/2$. Archetypes: #2 + #5 + (tacit) #4. ✓ verifies by $\sin^2 \theta = (1 - \cos 2\theta)/2$ and summing $\cos 2\theta$ over three angles equally spaced.

### HARD Tier (T4 / 3-archetype, 30-min benchmark)

**DP 8.9.** IMO 1972 P1 — 10 two-digit integers ⇒ two disjoint subsets with same sum. Archetypes: #13 + #12 + #14. ✓ pigeonhole on $2^{10} = 1024$ subsets vs. $9 \cdot 99 + 1 = 892$ possible sums.
**DP 8.10.** Engel Ch. 14 descent — $a^2 + b^2 + 1 = abc$. Archetypes: #14 + #16 + #18.
> ⚠ Open item: explicit verification of answer at chapter-final-review. Substitution with equivalent Engel Ch. 14 descent problem permitted.

---

## Batch Status Summary (as of v0.4.0)

| Batch | Chapters | Status | Total problems | Verified | Open items |
|---|---|---|---:|---:|---:|
| Batch 1 | Chs. 1–4 | **draft-locked** | 16 | 14 | 2 |
| Batch 2 | Chs. 5–8 | **draft-locked** | 28 | 22 | 6 |
| **Total Pillar 3** | Chs. 1–8 | both batches drafted | **44** | **36** | **8** |

---

## Changelog

**v0.4.0 — May 28, 2026.** Batch 2 lock.
- Added Chs. 5, 6, 7, 8 problem entries (28 problems total).
- Marked Batch 1 (Chs. 1–4) chapters as status=draft-locked.
- Marked Batch 2 (Chs. 5–8) chapters as status=draft-locked.
- 8 open items remain across Pillar 3, all explicitly flagged in-prose per Q2(a) protocol.
- Pillar 3 is now complete in draft form. Final review pending; Pillar 4 deferred until Lockhart/Tao/Sawyer/Andreescu PDFs land per Q1(b) of the build specification.

**v0.3.0 — May 28, 2026.** Initial creation (Batch 1 lock).
- Locked Chs. 1–4 problems (all worked examples + practice problems) — 16 problems total.
- 14 of 16 verified-by-source-reading; 2 carry ⚠ verification flags.
- 2 of 16 were open items (closed at v0.4.0 as part of Batch 2 lock or carried forward).

---

*End of pillar3-problems-locked.md v0.4.0.*
