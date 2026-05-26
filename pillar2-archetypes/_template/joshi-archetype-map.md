# Joshi → Archetype Map

*Working pre-drafting reference for Pillar 2 chapters. Maps each chapter of K.D. Joshi's* Educative JEE Mathematics *(2nd ed., 1039 pp.) to the Twenty Universal Archetypes of the Advaitian Philosophy of Problem Solving (Blueprint §6.3). Every Pillar 2 chapter drafted from Chapter 2 (Symmetry) onward should consult this map before problem selection.*

**Source:** `my_references/edujeejoshi2ed.pdf` (canonical) and `my_references/edujeejoshi2ed.txt` (searchable extraction, 52,591 lines).

**Status:** v0.1 — initial mapping, May 26 2026. To be refined as each archetype chapter is drafted. When Pillar 2 Chapter $n$ is drafted, the archetype-$n$ row of this map should be audited and tightened against the actual problems used.

**Reading rule.** A given Joshi chapter typically *foregrounds* one or two archetypes and *uses* several others as machinery. The columns below distinguish:

- **Primary** — archetypes this Joshi chapter is best suited to teach. Use Joshi problems from this chapter when drafting the corresponding Pillar 2 chapter.
- **Secondary** — archetypes that appear inside the chapter's worked examples but are not its central focus. These problems can serve as PP6–PP7 stretch material.

---

## 1. The Twenty Archetypes (reference)

| # | Archetype | Category |
|---|-----------|----------|
| 1 | Invariance | Structure Recognition |
| 2 | Symmetry | Structure Recognition |
| 3 | Duality | Structure Recognition |
| 4 | Hidden Structure | Structure Recognition |
| 5 | Substitution / Change of Variables | Transformation Thinking |
| 6 | Linearization | Transformation Thinking |
| 7 | Normalization / Scaling | Transformation Thinking |
| 8 | Domain Translation | Transformation Thinking |
| 9 | Domain Constraints / Bounds | Constraint Exploitation |
| 10 | Inequality Constraints | Constraint Exploitation |
| 11 | Existence / Uniqueness Conditions | Constraint Exploitation |
| 12 | Extremal Principles | Constraint Exploitation |
| 13 | Combinatorial Principles | Counting & Extremization |
| 14 | Parity / Modularity | Counting & Extremization |
| 15 | Bijection / Correspondence | Counting & Extremization |
| 16 | Reverse Engineering | Meta-Reasoning |
| 17 | Degrees of Freedom Analysis | Meta-Reasoning |
| 18 | Recursion / Induction | Meta-Reasoning |
| 19 | Pivoting / Elimination | Meta-Reasoning |
| 20 | Analogy / Transfer | Meta-Reasoning |

---

## 2. Joshi Chapter → Archetype Mapping

### Chapter 1 — Counting Problems (pp. 1–32)

| Slot | Archetypes |
|------|-----------|
| Primary | **#1 Invariance** (divisibility rules, decomposition invariants), **#13 Combinatorial Principles**, **#15 Bijection** |
| Secondary | #9 Domain Constraints (leading-zero, no-two-adjacent), #14 Parity, #17 DOF |

**Joshi worked examples already routed to Pillar 2 Chapter 1 (Invariance):**

- *Comment 1.* JEE 1989 — five-digit numbers divisible by 3 using $\{0,1,2,3,4,5\}$. Answer 216. **→ Ch. 1 WE1.**
- *Comment 4.* JEE 1979 — six boys and six girls in a row, probability girls together. Answer $1/132$. **→ Ch. 1 PP1.**
- *Comment 10.* JEE 1981 — 30 sets of 5 / $n$ sets of 3, find $n$. Answer 45. **→ Ch. 1 WE2.**

**Reserved for future archetype chapters:**

- *Comment 3.* Boxes / balls with restrictions (decomposition). **→ Ch. 13 Combinatorial Principles.**
- *Comment 5.* JEE 1983 — $m$ men, $n$ women, no two women together. **→ Ch. 15 Bijection / Ch. 13 Combinatorial Principles.**
- *Comment 12.* Twelve-coins puzzle (information-theoretic counting). **→ Ch. 13 Combinatorial Principles.**
- *Exercise 1.4.* JEE 1988 — six "+" and four "−" with no two "−" adjacent. **→ Ch. 15 Bijection.**

### Chapter 2 — Basic Algebra (pp. 32–84)

| Slot | Archetypes |
|------|-----------|
| Primary | **#2 Symmetry** (symmetric polynomials), **#5 Substitution**, **#19 Pivoting / Elimination** |
| Secondary | #1 Invariance (Vieta — sum / product of roots), #18 Recursion (AP / GP / HP) |

**Likely Chapter 2 (Symmetry) candidates from this chapter:**

- *AP / GP problems with a symmetric anchor* — e.g. JEE 1979 problem on $x, y, z$ in both AP and GP (line 2287, "*find $x^{y-z} y^{z-x} z^{x-y}$*"). The symmetric exponent structure is the archetype.
- *Symmetric polynomial identities involving $a + b + c, ab + bc + ca, abc$* — fertile territory for Ch. 2 worked examples.
- *Inserting means between $a$ and $b$* — AP / GP / HP means; the centroid/midpoint as symmetric centre.

### Chapter 3 — Theory of Equations (pp. 84–124)

| Slot | Archetypes |
|------|-----------|
| Primary | **#1 Invariance** (Vieta's relations are *the* canonical invariant family), **#2 Symmetry** (elementary symmetric functions), **#16 Reverse Engineering** (constructing a polynomial with given root properties) |
| Secondary | #5 Substitution (Tschirnhaus), #9 Domain Constraints (discriminant analysis), #11 Existence (real-roots conditions) |

**Reserved candidates:**

- *Common-root problems (JEE 1985, 1989 modified)* — two polynomials sharing a root. The invariant: the shared root; the move: resultant or substitution. **→ Ch. 3 (Duality) or Ch. 19 (Pivoting / Elimination).**
- *Discriminant invariants.* The discriminant is a structural invariant of the polynomial under affine change of coordinates — perfect Ch. 1 (Invariance) reinforcement and Ch. 9 (Domain Constraints) material.

### Chapter 4 — Number Theory (pp. 124–157)

| Slot | Archetypes |
|------|-----------|
| Primary | **#14 Parity / Modularity**, **#18 Recursion / Induction** (Joshi explicitly notes "in JEE, number theory problems… are mostly asked as problems on induction"), **#1 Invariance** (digital invariants, modular invariants) |
| Secondary | #4 Hidden Structure (Lucas / Kummer base-$p$), #15 Bijection (combinatorial proofs of divisibility) |

**Joshi material already routed to Pillar 2 Chapter 1 (Invariance):**

- *Main Problem.* Number of $n \in [10, 1000]$ with all $\binom{n}{k}$ odd. Answer 6. **→ Ch. 1 WE3.** Kummer / Lucas invariance on the binary expansion.
- *Comment 8.* JEE 1983 — $n(n^2 - 1)$ divisible by 24 for odd $n$. **→ Ch. 1 PP3.**
- *Comment 8.* JEE 1985 — $2 \cdot 7^n + 3 \cdot 5^n - 5$ divisible by 24. **→ Ch. 1 PP2.**

**Reserved for future archetype chapters:**

- *Comment 8.* JEE 1982 — $7^{2n} + 2^{3n-3} 3^{n-1}$ divisible by 25. **→ Ch. 18 Recursion / Induction** (shifted-linear-combination technique).
- *Comment 9.* JEE 1985 — product of any $r$ consecutive integers divisible by $r!$. **Double induction.** **→ Ch. 18.**
- *Comment 10.* JEE 1992 — $\alpha^n + \beta^n$ integer and not divisible by $p$, with $\alpha, \beta$ roots of a quadratic. **→ Ch. 18.**

### Chapter 5 — Binomial Identities (pp. 157–190)

| Slot | Archetypes |
|------|-----------|
| Primary | **#15 Bijection / Correspondence** (combinatorial proofs of identities), **#5 Substitution** ($x = 1, x = -1$ specialisations), **#1 Invariance** (closed-form identities surviving variable shifts) |
| Secondary | #18 Recursion (Pascal's identity), #4 Hidden Structure (generating functions) |

**Note:** Chapter 5 is the natural source for Pillar 2 Chapter 15 (Bijection). Many of Joshi's combinatorial-proof commentaries here are book-grade.

### Chapter 6 — Inequalities (pp. 190–234)

| Slot | Archetypes |
|------|-----------|
| Primary | **#10 Inequality Constraints**, **#12 Extremal Principles**, **#2 Symmetry** (symmetric inequalities collapse to one-variable cases) |
| Secondary | #5 Substitution (normalisation), #7 Normalization / Scaling, #6 Linearization (tangent-line trick) |

**Most fertile chapter for Pillar 2 Ch. 10 (Inequality Constraints) and Ch. 12 (Extremal Principles).**

### Chapter 7 — Trigonometric Identities (pp. 234–260)

| Slot | Archetypes |
|------|-----------|
| Primary | **#1 Invariance** ($\sin^2 + \cos^2 = 1$ is the prototypical relational invariant), **#2 Symmetry** (sum-to-product, product-to-sum) |
| Secondary | #5 Substitution (Weierstrass $t = \tan(\theta/2)$), #20 Analogy (Euler's formula bridge) |

**Note:** Ch. 7 is a natural complementary source for Pillar 2 Chapter 1 (Invariance) — $\sin^2 + \cos^2 = 1$ is the textbook example of a Type-III relational invariant. Reserved as cross-reference, not as a primary problem source.

### Chapter 8 — Geometry (pp. 260–287)

| Slot | Archetypes |
|------|-----------|
| Primary | **#2 Symmetry** (reflection / rotation arguments), **#3 Duality** (point–line, pole–polar, projective duality), **#1 Invariance** (Euclidean / projective invariants per Klein) |
| Secondary | #15 Bijection, #4 Hidden Structure (recognising a triangle in disguise) |

**Strongest source for Pillar 2 Ch. 2 (Symmetry) and Ch. 3 (Duality).**

### Chapter 9 — Coordinate Geometry (pp. 287–329)

| Slot | Archetypes |
|------|-----------|
| Primary | **#5 Substitution / Change of Variables** (coordinate choice as the central move), **#8 Domain Translation** (algebra ↔ geometry), **#19 Pivoting / Elimination** (eliminating $y$ between two curves) |
| Secondary | #1 Invariance (rigid-motion invariants of coordinate descriptions), #2 Symmetry |

### Chapters 10 — Trigonometric Equations (pp. 329–362)

| Slot | Archetypes |
|------|-----------|
| Primary | **#5 Substitution**, **#11 Existence / Uniqueness** (filtering candidate solutions by domain), **#9 Domain Constraints** |
| Secondary | #2 Symmetry (periodicity), #18 Recursion |

### Chapter 11 — Solution of Triangles (pp. 362–391)

| Slot | Archetypes |
|------|-----------|
| Primary | **#1 Invariance** (law of sines / cosines as relational invariants), **#2 Symmetry** (equilateral / isosceles arguments) |
| Secondary | #3 Duality (in / circumradius), #9 Domain Constraints (triangle inequality) |

### Chapter 12 — Heights and Distances (pp. 391–409)

| Slot | Archetypes |
|------|-----------|
| Primary | **#9 Domain Constraints**, **#5 Substitution** (angle-of-elevation parametrisation) |
| Secondary | #11 Existence, #20 Analogy (recognising the standard trapezium / triangle setup) |

**Note:** Largely applied-trigonometry; lighter pillar source. Useful for Ch. 9 (Domain Constraints) stretch problems.

### Chapter 13 — Maxima, Minima and Concavity (pp. 409–444)

| Slot | Archetypes |
|------|-----------|
| Primary | **#12 Extremal Principles**, **#9 Domain Constraints**, **#5 Substitution** (parameter reduction) |
| Secondary | #2 Symmetry (extrema at symmetric points), #10 Inequality Constraints |

### Chapter 14 — Trigonometric Optimisation (pp. 444–475)

| Slot | Archetypes |
|------|-----------|
| Primary | **#12 Extremal Principles**, **#2 Symmetry** |
| Secondary | #5 Substitution (Weierstrass), #10 Inequality Constraints (Cauchy–Schwarz / Jensen) |

### Chapter 15 — Limits, Continuity and Derivatives (pp. 475–512)

| Slot | Archetypes |
|------|-----------|
| Primary | **#11 Existence / Uniqueness** (IVT-style), **#6 Linearization** (derivative as best linear approximation) |
| Secondary | #5 Substitution (L'Hôpital), #20 Analogy |

### Chapter 16 — Theoretical Calculus (pp. 512–545)

| Slot | Archetypes |
|------|-----------|
| Primary | **#11 Existence / Uniqueness** (MVT, Rolle, IVT), **#6 Linearization**, **#1 Invariance** (parametrisation-invariant integration) |
| Secondary | #18 Recursion, #20 Analogy |

### Chapter 17 — Areas and Antiderivatives (pp. 545–593)

| Slot | Archetypes |
|------|-----------|
| Primary | **#5 Substitution**, **#1 Invariance** (parametrisation invariance of definite integrals) |
| Secondary | #2 Symmetry (even/odd functions), #18 Recursion (reduction formulas) |

### Chapter 18 — Definite Integrals (pp. 593–624)

| Slot | Archetypes |
|------|-----------|
| Primary | **#1 Invariance** ($\int_0^a f = \int_0^a f(a - x)$ is *the* symmetry-of-integration trick), **#2 Symmetry**, **#5 Substitution** |
| Secondary | #18 Recursion (reduction formulas) |

**Note:** This chapter's $\int_0^a f(x)\,dx = \int_0^a f(a-x)\,dx$ identity is a canonical Pillar 2 Ch. 1 reinforcement and a candidate WE2 / WE3 for Pillar 2 Ch. 2 (Symmetry).

### Chapter 19 — Differential Equations (pp. 624–660)

| Slot | Archetypes |
|------|-----------|
| Primary | **#5 Substitution**, **#6 Linearization** (integrating factors, exact equations), **#1 Invariance** (conservation laws as ODE invariants) |
| Secondary | #11 Existence, #18 Recursion |

### Chapter 20 — Functional Equations (pp. 660–675)

| Slot | Archetypes |
|------|-----------|
| Primary | **#5 Substitution** (the universal tool — set $x = 0$, $y = 1$, $y = -x$, $y = x$), **#11 Existence / Uniqueness**, **#1 Invariance** (additive / multiplicative invariants forced by the functional equation) |
| Secondary | #18 Recursion, #20 Analogy |

**Note:** PP7 of Ch. 1 (INMO functional equation) draws here. Chapter 20 is a *primary* source for Pillar 2 Ch. 5 (Substitution) and Ch. 11 (Existence / Uniqueness).

### Chapter 21 — Vectors (pp. 675–710)

| Slot | Archetypes |
|------|-----------|
| Primary | **#5 Substitution** (vector-as-coordinate-system), **#1 Invariance** (vector magnitudes, dot products under rotation), **#3 Duality** (vector / linear-functional) |
| Secondary | #2 Symmetry, #8 Domain Translation |

### Chapter 22 — Finitistic Probability (pp. 710–744)

| Slot | Archetypes |
|------|-----------|
| Primary | **#13 Combinatorial Principles**, **#15 Bijection / Correspondence** (favourable / total as a bijection problem), **#1 Invariance** (linearity of expectation as a Type-I summative invariant) |
| Secondary | #17 DOF, #20 Analogy |

### Chapter 23 — Infinitistic Probability (pp. 744–776)

| Slot | Archetypes |
|------|-----------|
| Primary | **#18 Recursion** (geometric series for probability of a recurring event), **#1 Invariance** (stationary distributions) |
| Secondary | #6 Linearization, #11 Existence |

### Chapter 24 — Miscellaneous Tips and Review (pp. 776–end)

| Slot | Archetypes |
|------|-----------|
| Primary | **ALL twenty.** Chapter 24 is Joshi's meta-pedagogical synthesis and exercise compendium, with the heaviest concentration of RMO / INMO / IMO-shortlist problems in the book. |

**Mandatory reading before drafting any Pillar 2 chapter.** Joshi here states his own framework for problem-solving strategy, which aligns closely with the Advaitian six-point structure. The 76+ exercises in Ch. 24 are the richest single source of RMO-tier and INMO-tier problems for Pillar 2 stretch material.

**Joshi 24-exercises already routed to Pillar 2 Ch. 1 (Invariance):**

- Exercise 24.13. RMO — $\alpha^3 - 3\alpha^2 + 5\alpha = 17$ and $\beta^3 - 3\beta^2 + 5\beta = -11$, find $\alpha + \beta$. Answer $\alpha + \beta = 2$. **→ Ch. 1 PP5.**
- Exercise 24.62. RMO — product of first 1000 evens vs. product of first 1000 odds, divisibility by 2001. **→ Ch. 1 PP4.**
- Exercise 24.69. INMO — $f(x + y) = f(x)f(y)f(xy)$. **→ Ch. 1 PP7.**
- Exercise 24.75. RMO — 1000 doors / divisor-parity invariant. Answer 969 open. **→ Ch. 1 PP6.**

**Sample 24-exercises reserved for future Pillar 2 chapters:**

- Exercise 24.11. Partial / total order on $\mathbb{C}$. **→ Ch. 3 (Duality) or Ch. 9 (Domain Constraints).**
- Exercise 24.49. $(2m)! (2n)! / (m+n)!$ integer. **→ Ch. 14 (Parity / Modularity).**
- Exercise 24.58. RMO — internal-angle-bisector triangle problem. **→ Ch. 2 (Symmetry) or Ch. 11 (Existence).**
- Exercise 24.60. Three perpendiculars from triangle vertices are concurrent. **→ Ch. 2 (Symmetry) / Ch. 3 (Duality).**
- Exercise 24.66. INMO + IMO 2000 — $abc = 1$ inequalities. **→ Ch. 10 (Inequality Constraints).**
- Exercise 24.67. RMO — symmetric $n \times n$ matrix with each integer $1..n$ appearing exactly once per row. **→ Ch. 2 (Symmetry).**
- Exercise 24.73. RMO — 50-element subset of $\{1, \ldots, 100\}$ with no two summing to 100; show contains a perfect square. **→ Ch. 13 (Combinatorial Principles) or Ch. 9.**

---

## 3. Aggregate Routing Table (problems-per-archetype, projected)

This table is the *inverse* of §2: for each of the twenty archetypes, which Joshi chapters are the primary problem source?

| Archetype | Primary Joshi Chapter(s) | Secondary Joshi Chapter(s) |
|---|---|---|
| 1. Invariance | **1, 4, 7, 18, 24** | 3, 11, 16, 19, 21 |
| 2. Symmetry | **2, 8, 18, 24** | 11, 13, 14, 17, 21 |
| 3. Duality | **8, 24** | 3, 9, 21 |
| 4. Hidden Structure | **5, 4, 24** | 2, 3 |
| 5. Substitution | **9, 17, 19, 20, 21** | 2, 5, 10, 13, 14 |
| 6. Linearization | **15, 16, 19** | 6, 13, 23 |
| 7. Normalization / Scaling | **6** | 9, 13 |
| 8. Domain Translation | **9, 21** | 8, 11 |
| 9. Domain Constraints | **10, 12, 13** | 3, 11, 24 |
| 10. Inequality Constraints | **6, 13, 14, 24** | 10, 22 |
| 11. Existence / Uniqueness | **15, 16, 20** | 3, 10, 11 |
| 12. Extremal Principles | **13, 14** | 6, 9 |
| 13. Combinatorial Principles | **1, 5, 22** | 23 |
| 14. Parity / Modularity | **4, 24** | 1 |
| 15. Bijection / Correspondence | **5, 1, 22** | 4, 8 |
| 16. Reverse Engineering | **3, 24** | 5 |
| 17. DOF Analysis | **1, 22** | 9, 21 |
| 18. Recursion / Induction | **4, 5, 23** | 18, 19, 20 |
| 19. Pivoting / Elimination | **3, 9, 21** | 2 |
| 20. Analogy / Transfer | **24** | 5, 7, 11, 15, 16 |

---

## 4. Use-of-Map Discipline

1. **Before any Pillar 2 chapter is drafted,** audit the corresponding row of §3 above. Pull the candidate problems from the *primary* Joshi chapter(s); reserve *secondary*-chapter problems for the PP6–PP7 stretch slots.

2. **Citation discipline.** Every Pillar 2 worked example and practice problem must be drawn from `my_references/edujeejoshi2ed.pdf` or from a JEE / RMO / INMO source that Joshi has commented on. Cite by competition name + year + Joshi chapter/exercise reference.

3. **No reuse.** Once a Joshi problem has been used in one Pillar 2 chapter, mark it here and do not re-use it in another (excepting deliberate cross-references where one archetype is the *secondary* lens on a problem whose *primary* lens has already been treated).

4. **Update protocol.** When a Pillar 2 chapter is completed, update this map's §2 with the actual routings (move "reserved candidates" up to "already routed"), and bump the version stamp.

---

**Version:** 0.1 — May 26 2026.
**Next review:** after Pillar 2 Chapter 2 (Symmetry) is drafted; the Joshi-2 + Joshi-8 mappings will be the first to need refinement.

🌑
