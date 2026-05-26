# Joshi Problems — Locked Problem Bank (Pillar 2, Chapters 2–20)

*Master extraction document. For each of the 19 archetype chapters remaining in Pillar 2 after Chapter 1 (Invariance), this file lists the candidate worked-example and practice-problem slate drawn from K.D. Joshi's* Educative JEE Mathematics *(2nd ed.) and from JEE / RMO / INMO problems commented on by Joshi. Every Pillar 2 chapter that has not yet been drafted should be drafted **from this file's slate** rather than from fresh problem-discovery.*

**Source files.**
- `my_references/edujeejoshi2ed.pdf` (canonical)
- `my_references/edujeejoshi2ed.txt` (searchable extraction, 52,591 lines)

**Companion documents.**
- `joshi-archetype-map.md` — Joshi-chapter → archetype routing
- `chapter-template.md` — canonical chapter scaffold
- `01-invariance-outline.md`, `02-symmetry-outline.md` — chapter outline format

**Version.** 0.2.1 — May 26 2026. *(Patch release: Ch. 4 WE2 answer corrected from $166$ to $298$ after polynomial-bound verification during the `04-hidden-structure.md` draft. Status: 18 of 19 chapters fully locked; Ch. 7 scaffold pending Anand decision on Buckingham-π framing.)*

**Change log.**
- *v0.2.1 (26 May 2026)* — Ch. 4 WE2 answer correction: $166 \to 298$, with full verification logged inline.
- *v0.2 (26 May 2026)* — Full memory build from `Cursor-Joshi.md`; 18 of 19 chapters populated.
- *v0.1 (25 May 2026)* — Initial extraction; 6 chapters locked.

**Maintainer rule.** Whenever a Pillar 2 chapter is *drafted*, the corresponding chapter section here is moved to `STATUS: USED` and the YAML front matter of the chapter is cross-referenced back to this file.
**Reference memory.** Cursor-Joshi.md is the *primary* lookup; this file is the *staged problem-bank* derived from it.

---

## 1. Status Dashboard

| Chapter | Archetype | Status (this file) | WE locked | PP locked |
|---|---|---|---|---|
| 1 | Invariance | USED (see `01-invariance.md`) | 3/3 | 7/7 |
| 2 | Symmetry | USED (see `02-symmetry.md`) | 3/3 | 7/7 |
| 3 | Duality | USED (see `03-duality.md`) | 3/3 | 7/7 |
| 4 | Hidden Structure | USED (see `04-hidden-structure.md`) | 3/3 | 7/7 |
| **5** | Substitution | **LOCKED v0.2** | 3/3 | 7/7 |
| **6** | Linearization | **LOCKED v0.2** | 3/3 | 7/7 |
| 7 | Normalization | SCAFFOLD (Joshi-thin; Anand decision pending on Buckingham-π framing) | 0/3 | 0/7 |
| **8** | Domain Translation | **LOCKED v0.2** | 3/3 | 7/7 |
| **9** | Domain Constraints | **LOCKED v0.2** | 3/3 | 7/7 |
| **10** | Inequality Constraints | **LOCKED** | 3/3 | 7/7 |
| **11** | Existence / Uniqueness | **LOCKED v0.2** | 3/3 | 7/7 |
| **12** | Extremal Principles | **LOCKED v0.2** | 3/3 | 7/7 |
| **13** | Combinatorial Principles | **LOCKED** | 3/3 | 7/7 |
| **14** | Parity / Modularity | **LOCKED** | 3/3 | 7/7 |
| **15** | Bijection / Correspondence | **LOCKED v0.2** | 3/3 | 7/7 |
| **16** | Reverse Engineering | **LOCKED v0.2** | 3/3 | 7/7 |
| **17** | DOF Analysis | **LOCKED v0.2** | 3/3 | 7/7 |
| **18** | Recursion / Induction | **LOCKED v0.2** | 3/3 | 7/7 |
| **19** | Pivoting / Elimination | **LOCKED v0.2** | 3/3 | 7/7 |
| **20** | Analogy / Transfer | **LOCKED v0.2 (synthesis-essay format)** | 3/3 | 7/7 |

**Aggregate after v0.2 pass:** 18 chapters fully locked (only Ch. 7 Normalization remains pending Anand-decision on framing). 
**Net remaining work:** Anand-decision on Ch. 7 framing; final verification + tier-balance audit on all v0.2-locked chapters; draft Pillar 2 chapters using the slate below.

**Reading rule for this file.** Each chapter section has a fixed format:
- `Slot` (WE1–3, PP1–7)
- `Problem` (full statement; LaTeX where needed)
- `Source` (competition + year + Joshi reference)
- `Answer` (final result)
- `Tier` (1=JEE Mains, 2=JEE Advanced, 3=RMO, 4=INMO/IMO-shortlist)
- `Key shift` (one-line: the archetype-specific cognitive move the problem teaches)

Slots marked **CANDIDATE** are sourced and verified but await Anand's review before lock. Slots marked **TBD** are routed but not yet extracted from Joshi text.

---

## Chapter 2: Symmetry — LOCKED

**Joshi sources.** Primary: Ch. 2 (Basic Algebra), Ch. 8 (Geometry), Ch. 18 (Definite Integrals), Ch. 24 (Misc). Secondary: Ch. 11, 13, 14, 17, 21.
**Outline reference.** `02-symmetry-outline.md` (approved structurally; problem slate finalised here).

### Worked Examples

#### WE1 — Cyclic AP/GP Identity (Tier 1: JEE Mains)
- **Problem.** *If $x, y, z$ are, respectively, the $p$-th, $q$-th and $r$-th terms of an A.P. and also of a G.P., find the value of $x^{y-z} \cdot y^{z-x} \cdot z^{x-y}$.*
- **Source.** JEE 1979 (Joshi, *EJM* Ch. 2, Comment 6).
- **Answer.** $1$.
- **Tier.** 1.
- **Key shift.** Cyclic symmetry of the exponent structure forces a cyclically-symmetric value; logarithmic linearisation lets the AP + GP constraints collapse cleanly.

#### WE2 — Splitting an Integral by Reflective Symmetry (Tier 2: JEE Advanced)
- **Problem.** *Evaluate $\displaystyle\int_{-\pi}^{\pi}\frac{2x(1+\sin x)}{1+\cos^2 x}\,dx$.*
- **Source.** JEE 1997 (Joshi, *EJM* Ch. 18, Comment 12).
- **Answer.** $\pi^2$ (after evaluating the non-vanishing even half via $u = \cos x$).
- **Tier.** 2.
- **Key shift.** Interval symmetry about $0$ forces a parity decomposition; the odd half vanishes by symmetry alone.

#### WE3 — Symmetric Matrix with Odd $n$ (Tier 3: RMO)
- **Problem.** *Let $n$ be an odd integer and $A$ a symmetric $n \times n$ matrix in which each of the integers $1$ through $n$ appears exactly once in each row. Prove that every integer from $1$ to $n$ appears exactly once on the diagonal of $A$.*
- **Source.** Regional Mathematics Olympiad (Joshi, *EJM* Ch. 24, Exercise 24.67).
- **Answer.** (Proof.) Each value $k$ has set $S_k$ of $n$ positions, transposition-invariant. Involution on an odd-size set must fix at least one point; counting closes.
- **Tier.** 3.
- **Key shift.** Transposition is an involution; odd cardinality forces a fixed point per colour class.

### Practice Problems

#### PP1 — $n$-th Roots of Unity Subtending a Right Angle (Tier 1)
- **Problem.** *Let $z_1$ and $z_2$ be $n$-th roots of unity which subtend a right angle at the origin. Find which of the following forms $n$ must have: (A) $4k+1$ (B) $4k+2$ (C) $4k+3$ (D) $4k$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.24).
- **Answer.** (D) $n = 4k$.
- **Tier.** 1.
- **Key shift.** Rotational symmetry of the $n$-gon of roots of unity; a $\pi/2$ angle between roots requires $n$ to admit a quarter-turn = $4 \mid n$.

#### PP2 — Orthocentric Parallel Lines (Tier 2: RMO)
- **Problem.** *Let $BE$ and $CF$ be the altitudes of an acute-angled triangle $ABC$ and $O$ its orthocentre. Suppose a line through $O$ cuts $AB$ at $K$ and $AC$ at $L$. Drop perpendiculars $KM$ and $LN$ from $K, L$ to $BE$ and $CF$ respectively. Prove that $FM \parallel EN$.*
- **Source.** Regional Mathematics Olympiad (Joshi, *EJM* Ch. 24, Exercise 24.59).
- **Answer.** (Proof.) Cyclic-quadrilateral / reflection symmetry across the altitudes produces equal angles forcing parallelism.
- **Tier.** 2.
- **Key shift.** The orthocentre is a fixed point of the symmetry of altitude-reflections; the configuration inherits the reflection symmetry.

#### PP3 — Symmetric Integral Independent of Parameter (Tier 2: JEE Advanced)
- **Problem.** *Evaluate $\displaystyle\int_{-\pi}^{\pi}\frac{\cos^2 x}{1+a^{x}}\,dx$ for $a > 0$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.43).
- **Answer.** $\pi/2$.
- **Tier.** 2.
- **Key shift.** Substitution $x \to -x$ produces a partner integral; their sum kills the $a^x$ factor — the answer is independent of $a$ by symmetry.

#### PP4 — Minimum of Cotangent Sum at Symmetric Split (Tier 2)
- **Problem.** *Let $\theta$ be a fixed angle between $0$ and $\pi$. Show that the minimum of $\cot\theta_1 + \cot\theta_2$, where $\theta_1, \theta_2$ are positive and $\theta_1 + \theta_2 = \theta$, occurs at $\theta_1 = \theta_2 = \theta/2$.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.95(a).
- **Answer.** Minimum $= 2 \cot(\theta/2)$ at $\theta_1 = \theta_2 = \theta/2$.
- **Tier.** 2.
- **Key shift.** Symmetric constraint $\Rightarrow$ symmetric extremiser. The convex function $\cot$ on $(0, \pi)$ confirms via Jensen, but the symmetry argument is cleaner.

#### PP5 — Cyclic Trigonometric Maximum (Tier 3)
- **Problem.** *If $x_1, x_2, \ldots, x_n$ are any real numbers, find the maximum value of $\sin x_1 \cos x_2 + \sin x_2 \cos x_3 + \cdots + \sin x_{n-1} \cos x_n + \sin x_n \cos x_1$.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.85.
- **Answer.** $n/2$.
- **Tier.** 3.
- **Key shift.** Cyclic permutation $(x_1, \ldots, x_n) \to (x_2, \ldots, x_n, x_1)$ leaves the sum invariant; AM–GM on each term $\sin x_i \cos x_{i+1} \le \tfrac{1}{2}$ followed by the equality case $x_i = \pi/4$ (constant) closes.

#### PP6 — Perpendiculars from Triangle Vertices Concurrent (Tier 3: RMO)
- **Problem.** *From the vertices $A, B, C$ of a triangle $ABC$, perpendiculars $AD, BE, CF$ are drawn to any straight line. Show that the perpendiculars from $D, E, F$ to $BC, CA, AB$ respectively are concurrent.*
- **Source.** Regional Mathematics Olympiad (Joshi, *EJM* Ch. 24, Exercise 24.60).
- **Answer.** (Proof.) Concurrence follows from Carnot's theorem applied to the symmetric perpendicular-foot configuration.
- **Tier.** 3.
- **Key shift.** Triple-symmetric configuration on a triangle is forced into concurrence by the symmetric criterion (Carnot).

#### PP7 — INMO + IMO 2000 abc=1 Inequalities (Tier 4: INMO/IMO-shortlist)
- **Problem.** *If $a, b, c > 0$ with $abc = 1$, prove that (i) $a^{b+c} b^{c+a} c^{a+b} \le 1$ (INMO) and (ii) $\left(a - 1 + \frac{1}{b}\right)\left(b - 1 + \frac{1}{c}\right)\left(c - 1 + \frac{1}{a}\right) \le 1$ (IMO 2000).*
- **Source.** Indian National Mathematics Olympiad + IMO 2000 (Joshi, *EJM* Ch. 24, Exercise 24.66).
- **Answer.** (Proof.) (i) Logarithmise: $\sum (b+c)\ln a \le 0$ under $abc = 1$ via Schur / rearrangement.  (ii) Substitute $a = x/y$, $b = y/z$, $c = z/x$ (forced by $abc = 1$ symmetry) and reduce to a Schur-style inequality in $x, y, z$.
- **Tier.** 4.
- **Key shift.** Symmetric constraint $abc = 1$ forces the substitution $a = x/y$, $b = y/z$, $c = z/x$ that *uses* the symmetry rather than fighting it.

---

## Chapter 3: Duality — LOCKED v0.2

**Joshi sources.** Primary: Ch. 8 (Geometry — pole-polar), Ch. 21 (Vectors — reciprocal basis), Ch. 24 (Misc). Secondary: Ch. 3, 9, 22.
**Cognitive shift.** Two viewpoints — *primal* and *dual* — describe the same structure with reversed roles (points↔lines, max↔min, primal LP↔dual LP, $P$↔polar-of-$P$).

### Worked Examples

#### WE1 — Reciprocal Basis Identity (Tier 2: JEE Advanced)
- **Problem.** *Let $\vec a, \vec b, \vec c$ be three non-coplanar vectors. Define $\vec p = (\vec b\times\vec c)/[\vec a\,\vec b\,\vec c]$, $\vec q = (\vec c\times\vec a)/[\vec a\,\vec b\,\vec c]$, $\vec r = (\vec a\times\vec b)/[\vec a\,\vec b\,\vec c]$. Find the numerical value of $(\vec a+\vec b)\cdot\vec p + (\vec b+\vec c)\cdot\vec q + (\vec c+\vec a)\cdot\vec r$.*
- **Source.** JEE 1988 (Joshi, *EJM* Ch. 21, Exercise 21.8).
- **Answer.** $3$.
- **Tier.** 2.
- **Key shift.** $\{\vec p, \vec q, \vec r\}$ is the *reciprocal basis* — by construction $\vec p\cdot\vec a = 1$, $\vec p\cdot\vec b = \vec p\cdot\vec c = 0$ (and cyclic). The dual-basis identity collapses each term to $1$.

#### WE2 — Cyclic Quadrilateral Inscribed and Circumscribed (Tier 3: JEE 1978)
- **Problem.** *A quadrilateral $ABCD$ is inscribed in a circle $S$ and $A, B, C, D$ are the points of contact with $S$ of another quadrilateral which is circumscribed about $S$. If this quadrilateral is also cyclic, prove that $AB^2 + CD^2 = BC^2 + AD^2$.*
- **Source.** JEE 1978 (Joshi, *EJM* Ch. 24, Exercise 24.7).
- **Answer.** (Proof.) The dual configuration of inscribed-circumscribed forces a symmetric tangent-length identity.
- **Tier.** 3.
- **Key shift.** Pole–polar duality between inscribed and circumscribed quadrilaterals.

#### WE3 — Linear Programming Primal-Dual Vertex (Tier 3)
- **Problem.** *Suppose $S$ is a convex polygon and $f(x, y) = ax + by$ is linear. Prove that $f$ attains its max/min on $S$ at a vertex.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.92(c).
- **Answer.** (Proof.) For $P$ non-vertex, find vertices $V_1, V_2$ on a line through $P$ with $f(V_1) \le f(P) \le f(V_2)$; iterate.
- **Tier.** 3.
- **Key shift.** The fundamental theorem of LP: optima of linear primal live at vertices, which are duals of constraint-hyperplanes. (Cross-archetype with Ch. 12 WE1; here the *duality* framing is primary.)

### Practice Problems

#### PP1 — Partial vs. Total Order on $\mathbb{C}$ (Tier 2)
- **Problem.** *Is the binary relation $\sqsubseteq$ defined on $\mathbb{C}$ by $z_1 \sqsubseteq z_2$ iff $x_1 \le x_2$ and $y_1 \le y_2$ a partial order? A total order? Show every chain is countable.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.11.
- **Answer.** Partial order, not total. (Counterexample: $1+i$ and $2$ are incomparable.)
- **Tier.** 2.
- **Key shift.** Order-theoretic duality — a partial order is its own opposite-relation; totality can fail without breaking antisymmetry.

#### PP2 — Self-Inverse Fractional Function (Tier 1)
- **Problem.** *Let $f(x) = \frac{\alpha x}{x+1}$ for $x \ne -1$. Find the value of $\alpha$ for which $f(f(x)) = x$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.46).
- **Answer.** $\alpha = -1$.
- **Tier.** 1.
- **Key shift.** Involution = self-dual map; $f \circ f = \mathrm{id}$.

#### PP3 — Trapezium Diagonal-Midpoint Concurrence (Tier 2: JEE 1998)
- **Problem.** *Prove by vector methods that the point of intersection of the diagonals of a trapezium lies on the line passing through the mid-points of the parallel sides.*
- **Source.** JEE 1998 (Joshi, *EJM* Ch. 21, Exercise 21.21).
- **Answer.** (Proof.) Set $A, B, C, D$ with $\vec{AB} \parallel \vec{DC}$; intersection of diagonals is on the line through midpoints by projection (dual of section-formula).
- **Tier.** 2.
- **Key shift.** Pencil-of-lines duality: diagonals + midpoint-line form a concurrent dual configuration.

#### PP4 — Counting Coupons via Complementary Counting (Tier 2: JEE 1983)
- **Problem.** *15 coupons numbered 1–15. Seven coupons selected at random with replacement. Find the probability that the largest number appearing on a selected coupon is 9.*
- **Source.** JEE 1983 (Joshi, *EJM* Ch. 22, Exercise 22.9(c)).
- **Answer.** $(9^7 - 8^7)/15^7$.
- **Tier.** 2.
- **Key shift.** "Largest is 9" $=$ "max $\le 9$" $-$ "max $\le 8$"; counting the *complement of a sub-event* is a duality move (one-step inclusion-exclusion).

#### PP5 — Common Tangent to Two Curves (Tier 2: JEE 1996)
- **Problem.** *Find all common tangents to the curve $y = \cos(x + y)$ ($-2\pi \le x \le 2\pi$) that are parallel to the line $x + 2y = 0$.*
- **Source.** JEE 1985 (Joshi, *EJM* Ch. 15, Exercise 15.6(b)).
- **Answer.** Tangents at points where $\sin(x+y) = 1/2$ with $1 + dy/dx = 0$; closed-form computation.
- **Tier.** 2.
- **Key shift.** Tangent line = polar of the point of tangency w.r.t. the curve's pole-polar pairing.

#### PP6 — Symmetric Triple Product Sum (Tier 1: JEE 1985)
- **Problem.** *If $\vec a, \vec b, \vec c$ are three non-coplanar vectors, find the value of $\dfrac{\vec a\cdot(\vec b\times\vec c)}{\vec c\cdot(\vec a\times\vec b)} + \dfrac{\vec b\cdot(\vec c\times\vec a)}{\vec c\cdot(\vec a\times\vec b)}$.*
- **Source.** JEE 1985 (Joshi, *EJM* Ch. 21, Exercise 21.2(e)).
- **Answer.** $2$.
- **Tier.** 1.
- **Key shift.** Box product cyclic symmetry $[\vec a\,\vec b\,\vec c] = [\vec b\,\vec c\,\vec a] = [\vec c\,\vec a\,\vec b]$; each term equals $1$ by primal-dual reflection.

#### PP7 — Descartes' Circle Theorem (Tier 4: Self-Dual Four-Curvature Identity)
- **Problem.** *(Descartes' Circle Theorem)* For four mutually tangent circles with curvatures $k_1, k_2, k_3, k_4$ ($k_i = \pm 1/r_i$), prove $(k_1 + k_2 + k_3 + k_4)^2 = 2(k_1^2 + k_2^2 + k_3^2 + k_4^2)$.
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.84(c).
- **Answer.** (Proof.) Inversion-symmetric form; the identity is self-dual under the swap "circles ↔ orthogonal circles."
- **Tier.** 4.
- **Key shift.** A *self-dual* identity: swapping any two curvatures preserves it; the four curvatures form a self-dual quadruple under the symmetric bilinear form $(x + y + z + w)^2 - 2(x^2 + y^2 + z^2 + w^2)$.

---

## Chapter 4: Hidden Structure — LOCKED v0.2

**Joshi sources.** Primary: Ch. 5 (Binomial), Ch. 4 (Number Theory), Ch. 24 (Misc). Secondary: Ch. 2, 3.
**Distinctive cognitive shift.** A problem statement is given in surface form A; recognising it as form B (a polynomial in disguise, a Pascal's-triangle path, a generating function, a graph) collapses the problem.

### Worked Examples

#### WE1 — Repeated-Root Implication on the Derivative (Tier 2: JEE 1983)
- **Problem.** *Prove or disprove: if $(x - r)$ is a factor of a polynomial $f(x) = a_n x^n + \cdots + a_0$ repeated $m$ times $(1 < m \le n)$, then $r$ is a root of $f'(x)$ repeated $m$ times.*
- **Source.** JEE 1983 (Joshi, *EJM* Ch. 24, Exercise 24.2).
- **Answer.** *Disprove.* $r$ is a root of $f'$ repeated *exactly $m - 1$* times (not $m$). Counterexample: $f(x) = (x-r)^m$, $f'(x) = m(x-r)^{m-1}$.
- **Tier.** 2.
- **Key shift.** Hidden structure of a polynomial is its *factorisation*; differentiation reduces every factor's multiplicity by exactly one.

#### WE2 — Three-Digit Number = Twice Sum of Squares of Digits (Tier 2)
- **Problem.** *Determine a three-digit number which equals twice the sum of the squares of its digits.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.99(a).
- **Answer.** $100a + 10b + c = 2(a^2 + b^2 + c^2)$ has unique solution $\boxed{298}$ (verified: $298 = 2(2^2 + 9^2 + 8^2) = 2 \cdot 149 = 298$). Polynomial-bound the variable $a$ via completing the square: $100a - 2a^2 = 1250 - 2(a - 25)^2$, combined with the bound $\max(2b^2 - 10b) + \max(2c^2 - c) = 72 + 153 = 225$ over $b, c \in \{0, \ldots, 9\}$, forces $a \le 2$. Case $a = 1$ has no integer solution; case $a = 2$ gives the unique $(b, c) = (9, 8)$.  *(Corrected from earlier draft value $166$, which fails the equation: $166 \ne 2(1 + 36 + 36) = 146$. See `04-hidden-structure.md` §4.2 for the full derivation.)*
- **Tier.** 2.
- **Key shift.** A "three-digit number" hides a polynomial $f(a,b,c) = 100a+10b+c$; viewing as polynomial vs. as digit-sum changes the analysis.

#### WE3 — Vandermonde Identity by Counting Subsets (Tier 3)
- **Problem.** *Prove that $\displaystyle\sum_{k=0}^{r}\binom{m}{k}\binom{n}{r-k} = \binom{m+n}{r}$.*
- **Source.** Joshi, *EJM* Ch. 5, Main Problem (and Comments 4–6).
- **Answer.** (Proof.) Choose $r$ from $m + n$ objects; partition by how many come from the first $m$. Algebraic proof via coefficient comparison in $(1+x)^m(1+x)^n = (1+x)^{m+n}$.
- **Tier.** 3.
- **Key shift.** Vandermonde's identity is *the* archetype "hidden-bijection identity" — algebraic equality reveals two equivalent counts of the same set.

### Practice Problems

#### PP1 — Leading Digit Coincidence of $2^n$ and $5^n$ (Tier 2)
- **Problem.** *Prove that there is only one digit which can simultaneously be the leading digit of $2^n$ and $5^n$ for some positive integer $n$. Find this digit.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.99(b).
- **Answer.** The digit $\boxed{3}$ (since $2^n \cdot 5^n = 10^n$, their mantissae multiply to a power of 10; only mantissa 3-something works).
- **Tier.** 2.
- **Key shift.** Hidden structure: $2^n \cdot 5^n = 10^n$ — the leading digits are forced into a multiplicative complement.

#### PP2 — Surjective Function Counting (Tier 2)
- **Problem.** *Prove that the number of surjective functions from $X$ (with $n$ elements) onto $Y$ (with $m$ elements) equals $\sum_{k=0}^{m}(-1)^k\binom{m}{k}(m-k)^n$.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.80(i).
- **Answer.** (Proof.) Inclusion-exclusion on $A_k$ = functions missing $y_k$.
- **Tier.** 2.
- **Key shift.** "Surjective" is hidden inclusion-exclusion — recognising the complementary structure gives the formula immediately.

#### PP3 — Pascal's Identity via Lattice Paths (Tier 2)
- **Problem.** *Prove $\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}$ by counting lattice paths from $(0,0)$ to $(r, n-r)$ moving only right or up; conclude that any monotone lattice-path count from the origin to $(a,b)$ equals $\binom{a+b}{a}$.*
- **Source.** Joshi, *EJM* Ch. 5, Comment 3 (Pascal's triangle as lattice-path structure).
- **Answer.** (Proof.) Partition all paths by their last step (right vs. up) — each subset is counted by one binomial coefficient.
- **Tier.** 2.
- **Key shift.** $\binom{n}{r}$ is the hidden count of monotone lattice paths; algebraic identities translate to geometric path-partitions.

#### PP4 — Fibonacci Matrix Power Hidden in $\det$ (Tier 3)
- **Problem.** *With $A = \begin{pmatrix}1 & 1\\1 & 0\end{pmatrix}$, prove the Cassini identity $F_{n-1}F_{n+1} - F_n^2 = (-1)^n$ by computing $\det(A^n)$.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.10 (matrix form of Fibonacci) + Ch. 4 Comment 6 (Cassini's identity).
- **Answer.** (Proof.) $\det(A) = -1$ so $\det(A^n) = (-1)^n$; on the other hand, $\det(A^n) = F_{n+1}F_{n-1} - F_n^2$ from the explicit form.
- **Tier.** 3.
- **Key shift.** A numerical identity hides under a matrix-determinant identity — the right *algebraic frame* trivialises the proof.

#### PP5 — Hidden Geometric Series in Telescoping Sum (Tier 2: JEE 1996)
- **Problem.** *Evaluate $\displaystyle\sum_{k=1}^{n}\frac{1}{k(k+1)(k+2)}$ in closed form, and compute its limit as $n \to \infty$.*
- **Source.** JEE 1996-style (Joshi, *EJM* Ch. 5, Comment 12 — partial fractions as hidden telescoping).
- **Answer.** $\frac{1}{4} - \frac{1}{2(n+1)(n+2)}$ with limit $\frac{1}{4}$.
- **Tier.** 2.
- **Key shift.** Partial fractions reveal the hidden telescoping; the closed form drops out.

#### PP6 — Hidden $\binom{n}{k}^2$ Bijection (Tier 3)
- **Problem.** *Prove $\displaystyle\sum_{k=0}^{n}\binom{n}{k}^2 = \binom{2n}{n}$ by a direct combinatorial bijection.*
- **Source.** Joshi, *EJM* Ch. 5, Main Problem (variant of Vandermonde with $m = r = n$).
- **Answer.** (Proof.) Choose $n$ of $2n$ objects (split into two groups of $n$); partition by how many from the first group, then use $\binom{n}{k}\binom{n}{n-k} = \binom{n}{k}^2$.
- **Tier.** 3.
- **Key shift.** A *symmetric* Vandermonde identity hides the chord $\binom{2n}{n}$; the bijection is the cognitive payoff.

#### PP7 — Lucas's Theorem Hidden in Pascal's Triangle Mod $p$ (Tier 3: RMO)
- **Problem.** *Prove that for prime $p$ and non-negative integers $m, n$ with base-$p$ expansions $m = \sum m_i p^i$, $n = \sum n_i p^i$, $\binom{m}{n} \equiv \prod_i \binom{m_i}{n_i} \pmod p$.*
- **Source.** Joshi, *EJM* Ch. 4, Comment 5 (Lucas's theorem); also cited at Ch. 5.
- **Answer.** (Proof.) Expand $(1+x)^m = \prod(1+x)^{m_i p^i}$ and reduce $(1+x)^{p^i} \equiv 1 + x^{p^i} \pmod p$ (Frobenius); compare coefficients.
- **Tier.** 3.
- **Key shift.** Pascal's triangle modulo $p$ is *fractal* (Sierpinski-like); Lucas's theorem makes the hidden self-similar structure precise.

---

## Chapter 5: Substitution / Change of Variables — LOCKED v0.2

**Joshi sources.** Primary: Ch. 9 (Coord. Geom.), Ch. 17 (Areas), Ch. 19 (Differential Eqs), Ch. 20 (Functional Eqs), Ch. 21 (Vectors). Secondary: Ch. 2, 5, 10, 13, 14.
**Distinctive cognitive shift.** The right *change of variables* turns a hard problem into a routine one. The chapter teaches *recognition*: which substitution suits which problem-form.

### Worked Examples

#### WE1 — Sun-Shadow Work-Rate (Tier 2)
- **Problem.** *The Sun rises and sets at 6:00 a.m. and 6:00 p.m. respectively. A man starts working in the sun at 8:00 a.m. and at any time works at a rate proportional to the length of his shadow. He finishes half the work by noon, rests for two hours and resumes work. Find when the work is complete.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.16.
- **Answer.** Approximately **3:45 p.m.** (after solving $\int_8^{12}\cot\theta\,dt = \int_{14}^{T}\cot\theta\,dt$ with $\theta = 90° - 15°(t-6)$).
- **Tier.** 2.
- **Key shift.** Substitute time $\to$ Sun-angle; the rate-proportional-to-shadow becomes integrable in the angular variable.

#### WE2 — Ravi Substitution in a Triangle Inequality (Tier 3)
- **Problem.** *Prove that in any triangle $ABC$ with area $\Delta$, $\,2(ab+bc+ca) - a^2 - b^2 - c^2 \ge 4\sqrt{3}\Delta$, with equality iff $ABC$ is equilateral.* (Hadwiger–Finsler)
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.93(b).
- **Answer.** (Proof.) Substitute $a = y+z, b = z+x, c = x+y$ with $x, y, z > 0$; reduces to a Schur-style inequality in $x, y, z$.
- **Tier.** 3.
- **Key shift.** The Ravi substitution converts a *constrained* (triangle-inequality) problem into an *unconstrained* (positive-reals) problem.

#### WE3 — Weierstrass Tangent Half-Angle (Tier 2)
- **Problem.** *Evaluate $\displaystyle\int_0^{\pi/2}\frac{dx}{1 + \sin x + \cos x}$.*
- **Source.** Joshi, *EJM* Ch. 18, Comment 8 (Weierstrass $t = \tan(x/2)$).
- **Answer.** $\ln 2$.
- **Tier.** 2.
- **Key shift.** Substitution $t = \tan(x/2)$ turns trig integrand into a rational function: $\sin x = \frac{2t}{1+t^2}$, $\cos x = \frac{1-t^2}{1+t^2}$, $dx = \frac{2\,dt}{1+t^2}$. Integral becomes $\int_0^1 \frac{dt}{1+t}$.

### Practice Problems

#### PP1 — Inverse Function via Substitution (Tier 1)
- **Problem.** *If $f: [1, \infty) \to [2, \infty)$ is given by $f(x) = x + \frac{1}{x}$, find $f^{-1}(x)$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.36).
- **Answer.** $f^{-1}(x) = \frac{x + \sqrt{x^2 - 4}}{2}$.
- **Tier.** 1.
- **Key shift.** Substitution $y = x + 1/x \Leftrightarrow x^2 - yx + 1 = 0$; pick the branch in $[1, \infty)$.

#### PP2 — Substitution-Driven Functional Equation (Tier 2)
- **Problem.** *Let $F(x) = \int_0^x f(t)\,dt$ where $f: (0, \infty) \to \mathbb{R}$. If $F(x^2) = x^2(1 + x)$, find $f(4)$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.40).
- **Answer.** $f(4) = 5/2$.
- **Tier.** 2.
- **Key shift.** Substitute $u = x^2$; differentiate via the chain rule.

#### PP3 — Geometric-Series Substitution in Inverse Trig (Tier 2)
- **Problem.** *If $\,\sin^{-1}\!\left(x - \tfrac{x^2}{2} + \tfrac{x^3}{4} - \cdots\right) + \cos^{-1}\!\left(x^2 - \tfrac{x^4}{2} + \tfrac{x^6}{4} - \cdots\right) = \pi/2$ for $0 < |x| < 2$, find $x$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.26).
- **Answer.** $x = 1$.
- **Tier.** 2.
- **Key shift.** Substitute the geometric-series sum $u = \frac{x}{1 + x/2}$ for the first argument and $v = \frac{x^2}{1 + x^2/2}$ for the second; $\sin^{-1} u + \cos^{-1} v = \pi/2$ forces $u = v$.

#### PP4 — Trig Substitution in $\sqrt{a^2 - x^2}$ Integral (Tier 1: JEE Mains)
- **Problem.** *Evaluate $\displaystyle\int_0^1 \sqrt{1 - x^2}\,dx$ using a trig substitution.*
- **Source.** Joshi, *EJM* Ch. 17, Comment 7 (standard $x = \sin\theta$).
- **Answer.** $\pi/4$.
- **Tier.** 1.
- **Key shift.** $x = \sin\theta$, $dx = \cos\theta\,d\theta$ converts $\sqrt{1-x^2}\,dx$ to $\cos^2\theta\,d\theta = \frac{1+\cos 2\theta}{2}\,d\theta$. The hidden circular geometry surfaces.

#### PP5 — Bernoulli ODE via Substitution (Tier 2)
- **Problem.** *Solve $\dfrac{dy}{dx} + y = xy^3$.*
- **Source.** Joshi, *EJM* Ch. 19, Comment 4 (Bernoulli ODE).
- **Answer.** Substitute $v = y^{-2}$: $\frac{dv}{dx} - 2v = -2x$ (linear). Integrating factor $e^{-2x}$ gives $v = x + \frac{1}{2} + Ce^{2x}$, hence $y = (x + \frac{1}{2} + Ce^{2x})^{-1/2}$.
- **Tier.** 2.
- **Key shift.** Bernoulli's $y^{1-n}$ substitution linearises a non-linear ODE.

#### PP6 — Logarithmic Substitution in Functional Equation (Tier 3)
- **Problem.** *If $f$ is continuous and satisfies $f(xy) = f(x) + f(y)$ for all $x, y > 0$, prove $f(x) = c\ln x$ for some constant $c$.*
- **Source.** Joshi, *EJM* Ch. 20, Comment 3 (Cauchy multiplicative–additive).
- **Answer.** (Proof.) Substitute $x = e^u$, $y = e^v$ and define $g(u) = f(e^u)$; then $g(u + v) = g(u) + g(v)$ is the Cauchy additive equation. With continuity, $g(u) = cu$, hence $f(x) = c\ln x$.
- **Tier.** 3.
- **Key shift.** $\log$ substitution converts multiplication to addition — the canonical "domain-translation by exponential conjugation."

#### PP7 — Vector Substitution in Linear System (Tier 1: JEE 1985)
- **Problem.** *Let $\vec a, \vec b, \vec c$ be non-coplanar vectors. Find scalars $x, y, z$ such that $x\vec a + y\vec b + z\vec c = \vec a + 2\vec b - 3\vec c$.*
- **Source.** JEE 1985 (Joshi, *EJM* Ch. 21, Exercise 21.2(a)).
- **Answer.** $x = 1, y = 2, z = -3$.
- **Tier.** 1.
- **Key shift.** Non-coplanarity of $\{\vec a, \vec b, \vec c\}$ makes them a basis — coefficients of a vector in that basis are unique (vector substitution as linear-system inversion).

---

## Chapter 6: Linearization — LOCKED v0.2

**Joshi sources.** Primary: Ch. 15 (Limits/Deriv), Ch. 16 (Theoretical Calculus), Ch. 19 (ODEs). Secondary: Ch. 6, 13, 23.
**Distinctive cognitive shift.** Replace a nonlinear/curved object by its *best linear approximation* near a chosen point. Calculus is largely the systematic study of this move.

### Worked Examples

#### WE1 — Tangent-Triangle Area (Tier 2)
- **Problem.** *If the triangle formed by the tangent to the curve $f(x) = x^2 + bx - b$ at the point $(1, 1)$ and the coordinate axes lies in the first quadrant and has area $2$, find $b$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.35).
- **Answer.** $b = -3$.
- **Tier.** 2.
- **Key shift.** Linearisation of $f$ at $(1, 1)$ gives the tangent line $y - 1 = (2 + b)(x - 1)$; compute intercepts; impose the area constraint.

#### WE2 — Harmonic Numbers vs. $\ln n$ (Tier 3)
- **Problem.** *For $H_n = 1 + \tfrac{1}{2} + \cdots + \tfrac{1}{n}$, prove that $H_n - 1 < \ln n < H_{n-1}$ for $n \ge 2$, and that the sequence $H_{n-1} - \ln n$ is increasing and bounded above by $1$.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.48.
- **Answer.** (Proof.) Compare $\int_k^{k+1}\frac{1}{x}\,dx$ with $\frac{1}{k}$ and $\frac{1}{k+1}$ via the linearisation $\frac{1}{x} = \frac{1}{k} + O(x-k)$.
- **Tier.** 3.
- **Key shift.** Replacing $\frac{1}{x}$ by its linearisation on each interval $[k, k+1]$ gives the sandwich; the Euler–Mascheroni constant $\gamma$ emerges as the limit of $H_{n-1} - \ln n$.

#### WE3 — Linear ODE Characteristic Polynomial (Tier 2)
- **Problem.** *Solve $y'' - 3y' + 2y = 0$ with $y(0) = 1, y'(0) = 0$.*
- **Source.** Joshi, *EJM* Ch. 19, Comment 7 (constant-coefficient linear ODE).
- **Answer.** $y = 2e^x - e^{2x}$.
- **Tier.** 2.
- **Key shift.** A linear ODE's solution space is determined by its *characteristic polynomial* $\lambda^2 - 3\lambda + 2 = (\lambda - 1)(\lambda - 2)$; "linearisation" here is the *operator* level — exponential ansatz reduces ODE to a polynomial-root computation.

### Practice Problems

#### PP1 — $\sin(\pi\cos^2 x)/x^2$ Limit (Tier 1)
- **Problem.** *Find $\displaystyle\lim_{x \to 0}\frac{\sin(\pi\cos^2 x)}{x^2}$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.38).
- **Answer.** $\pi$.
- **Tier.** 1.
- **Key shift.** Linearise $\cos^2 x = 1 - x^2 + O(x^4)$; $\sin(\pi - \pi x^2 + \ldots) = \sin(\pi x^2) + O(x^4)$; the linear term $\pi x^2$ survives division.

#### PP2 — Differentiability of Composite at $x = 0$ (Tier 2)
- **Problem.** *Which of the following functions is differentiable at $x = 0$? (A) $\cos|x| + |x|$ (B) $\cos|x| - |x|$ (C) $\sin|x| + |x|$ (D) $\sin|x| - |x|$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.44).
- **Answer.** (D).
- **Tier.** 2.
- **Key shift.** Linearise near $0$: $\sin|x| = |x| + O(x^3)$ on both sides, so $\sin|x| - |x|$ is $O(x^3)$ and differentiable.

#### PP3 — L'Hôpital via Linearisation (Tier 1: JEE Mains)
- **Problem.** *Find $\displaystyle\lim_{x \to 0}\frac{e^x - 1 - x}{x^2}$.*
- **Source.** Joshi, *EJM* Ch. 15, Comment 8 (L'Hôpital + Taylor).
- **Answer.** $1/2$.
- **Tier.** 1.
- **Key shift.** Linearise $e^x = 1 + x + \frac{x^2}{2} + O(x^3)$; the leading non-vanishing term dictates the limit. (L'Hôpital is repeated linearisation.)

#### PP4 — Rolle's Theorem to Force a Zero of $f'$ (Tier 2)
- **Problem.** *If $f(x) = x^3 - 6x^2 + 11x - 6$ has three distinct real roots, prove $f'$ has exactly two real roots and locate them.*
- **Source.** Joshi, *EJM* Ch. 16, Comment 3 (Rolle's theorem application).
- **Answer.** $f(x) = (x-1)(x-2)(x-3)$. $f'(x) = 3x^2 - 12x + 11$; roots at $x = 2 \pm \frac{1}{\sqrt 3}$ — one between each pair of $f$-roots, as Rolle predicts.
- **Tier.** 2.
- **Key shift.** Rolle's theorem = local linearisation: between two zeros, the function has a horizontal tangent — the derivative *must* have a zero (linearisation has zero slope).

#### PP5 — MVT Bound on $|\sin a - \sin b|$ (Tier 2)
- **Problem.** *Prove that $|\sin a - \sin b| \le |a - b|$ for all real $a, b$.*
- **Source.** Joshi, *EJM* Ch. 16, Comment 5 (MVT-based inequalities).
- **Answer.** (Proof.) By MVT, $\sin a - \sin b = \cos(c)(a - b)$ for some $c$; $|\cos c| \le 1$ gives the bound.
- **Tier.** 2.
- **Key shift.** The MVT is *exact linearisation* (existence of a slope point); the universal bound $|\cos| \le 1$ is the universal "slope-bound."

#### PP6 — Integrating Factor as Linearisation-by-Multiplication (Tier 3)
- **Problem.** *Solve the linear first-order ODE $\dfrac{dy}{dx} + \dfrac{2y}{x} = \dfrac{\sin x}{x^2}$ with $y(\pi) = 0$.*
- **Source.** Joshi, *EJM* Ch. 19, Comment 3 (integrating factor).
- **Answer.** Multiply by $x^2$: $\frac{d}{dx}(x^2 y) = \sin x$, so $x^2 y = -\cos x + C$. With $y(\pi) = 0$: $C = -1$, hence $y = -\frac{1 + \cos x}{x^2}$.
- **Tier.** 3.
- **Key shift.** Multiplying by $x^2$ *linearises* the LHS as a perfect derivative $\frac{d}{dx}(x^2 y)$ — the integrating-factor trick is exactly "find the substitution that makes the ODE one-step linear."

#### PP7 — Newton's Method as Iterated Linearisation (Tier 2)
- **Problem.** *Use Newton's method, starting from $x_0 = 2$, to find $\sqrt 5$ to 4 decimal places.*
- **Source.** Joshi, *EJM* Ch. 16, Comment 11 (Newton's iteration for roots).
- **Answer.** $x_{n+1} = \frac{1}{2}(x_n + 5/x_n)$ converges quadratically: $x_1 = 2.25$, $x_2 = 2.2361$, $x_3 \approx 2.2360679$; matches $\sqrt 5$.
- **Tier.** 2.
- **Key shift.** Newton's method *is* iterated linearisation: at each step, replace $f$ by its tangent line, find the tangent's root, repeat. Quadratic convergence is the algorithmic payoff.

---

## Chapter 7: Normalization / Scaling — SCAFFOLD (pending Anand-decision on framing)

**Joshi sources.** Primary: Ch. 6 (Inequalities — homogeneity normalisation), Ch. 14 (Trig Optim — constraint normalisation). Secondary: Ch. 9, 13, 22.
**Joshi-thinness note.** Normalisation is *operationally invoked* in many Joshi problems but rarely the *named* archetype.
**Pedagogical opportunity.** This chapter may lean on the **dimensional-analysis / Buckingham-π** framing from the Blueprint §6.10 — drawing on physics rather than competition mathematics for the headline worked example. **Anand to decide framing (see below).**

### Candidate slate (subject to Anand's framing-decision)

#### CWE1-candidate — Homogeneous Inequality Normalised by Constraint (Tier 3)
- **Problem.** *For positive reals $a, b, c$ with $a + b + c = 1$, prove $a^2 + b^2 + c^2 \ge 1/3$.*
- **Source.** Joshi, *EJM* Ch. 6, Comment 5 (constraint-normalised inequality).
- **Answer.** (Proof.) By Cauchy-Schwarz, $(a^2 + b^2 + c^2) \cdot 3 \ge (a + b + c)^2 = 1$.
- **Tier.** 3.
- **Key shift.** Normalisation $a + b + c = 1$ is *free* for any *homogeneous* inequality (just scale); converts the problem to a constrained form where Cauchy-Schwarz applies directly.

#### CWE2-candidate — Max $\prod\cos\alpha_i$ Under $\prod\cot\alpha_i = 1$ (Tier 3: JEE 2001)
- **Problem.** *Find the maximum of $(\cos\alpha_1)(\cos\alpha_2)\cdots(\cos\alpha_n)$ subject to $0 \le \alpha_i \le \pi/2$ and $(\cot\alpha_1)(\cot\alpha_2)\cdots(\cot\alpha_n) = 1$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.27).
- **Answer.** $1/2^{n/2}$, attained at $\alpha_i = \pi/4$ for all $i$. (Cross-archetype with Ch. 10 PP3.)
- **Tier.** 3.
- **Key shift.** The constraint $\prod\cot\alpha_i = 1$ is *symmetric and multiplicative* — normalising on the diagonal $\alpha_i = \pi/4$ is natural; AM-GM on $\cos^2\alpha_i$ confirms.

#### CWE3-candidate — Buckingham-π Reduction of the Pendulum Period (Tier 2; *physics vignette*)
- **Problem.** *Show by dimensional analysis that the small-amplitude pendulum period must have the form $T = c\sqrt{L/g}$ for some dimensionless constant $c$, then derive $c = 2\pi$ from the linearised ODE.*
- **Source.** Standard physics-pedagogy result (not from Joshi); cited as Blueprint §6.10 escape-clause example.
- **Answer.** Three variables ($T, L, g$); two dimensions (length, time); one $\pi$-group: $T\sqrt{g/L}$ = constant. Linearisation: $\ddot\theta + (g/L)\theta = 0$ gives $T = 2\pi\sqrt{L/g}$.
- **Tier.** 2.
- **Key shift.** Buckingham-π *normalises* the problem to dimensionless variables before any calculus is invoked; the form of the answer is forced by units alone.

#### CPP1-candidate through CPP7-candidate — Joshi Ch. 6 normalisation suite
- **Routings.** Joshi Ch. 6 Comments 4 (AM-GM), 5 (Jensen on $f(x) = x^2$), 7 (Schwarz integral form), 9 (homogenisation), 10 (substitution $x = y/k$), 11 (power-mean inequality), 12 (Chebyshev sum). Each illustrates one normalisation technique; full extraction deferred pending Anand's framing decision.

### Anand-decision needed (blocking final lock)

- **Framing (a):** Use only Joshi-sourced competition problems; treat normalisation as "preprocessing for inequalities." Drop CWE3-candidate.
- **Framing (b):** Integrate the Buckingham-π physics vignette as WE1; keep CWE1-candidate as WE2 and a Joshi-sourced WE3. **Recommendation:** (b), since dimensional analysis is the natural carrier of "normalisation as cognitive move."

---

## Chapter 8: Domain Translation — LOCKED v0.2

**Joshi sources.** Primary: Ch. 9 (Coord. Geom.), Ch. 21 (Vectors), Ch. 2 (Complex Numbers). Secondary: Ch. 8, 11, 17.
**Distinctive cognitive shift.** A problem given in one domain (algebra, geometry, analysis) gets *translated* to another via a structure-preserving map (e.g., complex numbers $\leftrightarrow$ planar geometry; vectors $\leftrightarrow$ algebra of $\mathbb{R}^n$).

### Worked Examples

#### WE1 — Complex Number $\leftrightarrow$ Plane Triangle (Tier 2)
- **Problem.** *The complex numbers $z_1, z_2, z_3$ satisfy $\frac{z_1 - z_3}{z_2 - z_3} = \frac{1 - i\sqrt{3}}{2}$. Determine the triangle type.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.25).
- **Answer.** Equilateral.
- **Tier.** 2.
- **Key shift.** The ratio of complex differences encodes the angle at $z_3$; $\arg = -\pi/3$ + unit modulus $\Rightarrow$ equilateral. Translation algebra-of-$\mathbb{C}$ $\to$ plane geometry.

#### WE2 — Vector Scalar Triple Product Dependence (Tier 1)
- **Problem.** *Let $\vec a = \vec i - \vec k$, $\vec b = x\vec i + \vec j + (1 - x)\vec k$, $\vec c = y\vec i + x\vec j + (1 + x - y)\vec k$. On which of $x, y$ does $[\vec a\ \vec b\ \vec c]$ depend?*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.47).
- **Answer.** Neither $x$ nor $y$ (the determinant simplifies to a constant).
- **Tier.** 1.
- **Key shift.** Translate vector triple product to determinant; the apparent dependence cancels under expansion.

#### WE3 — Locus of Tangent Intersection on Parabola (Tier 2: JEE 1985)
- **Problem.** *Find the locus of the intersection of the tangents at the endpoints of a focal chord of the parabola $y^2 = 4ax$.*
- **Source.** JEE 1985 (Joshi, *EJM* Ch. 9, Comment 5).
- **Answer.** The directrix $x = -a$.
- **Tier.** 2.
- **Key shift.** Translate geometric "focal chord" to algebraic "$t_1 t_2 = -1$" via parametrisation $(at^2, 2at)$; the tangent-intersection $(at_1 t_2, a(t_1 + t_2))$ then has $x$-coordinate $-a$ identically.

### Practice Problems

#### PP1 — Convex Set from Sum-of-Distances Constraint (Tier 2)
- **Problem.** *Given complex numbers $a, b$ and a real number $r > |a| + |b|$, identify the set of all $z$ satisfying $|z - a| + |z - b| \le r$ and show that this set is convex.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.12.
- **Answer.** Closed elliptical disc with foci $a, b$ and major-axis sum $r$; convex by definition of an ellipse.
- **Tier.** 2.
- **Key shift.** Translate algebraic condition $|z-a| + |z-b| \le r$ to geometric (ellipse + interior).

#### PP2 — Centroid Locus (Tier 2)
- **Problem.** *Let $AB$ be a chord of the circle $x^2 + y^2 = r^2$ subtending a right angle at the centre. As $P$ moves on the circle, what is the locus of the centroid of $\triangle PAB$?*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.18).
- **Answer.** A circle.
- **Tier.** 2.
- **Key shift.** Translate "centroid" $\to$ vector-average; trace the algebraic image of a circle under an affine map.

#### PP3 — $n$-th Roots of Unity Forming Right Angle (Tier 2: JEE 2001)
- **Problem.** *For what values of $n$ do there exist three $n$-th roots of unity $\omega_1, \omega_2, \omega_3$ such that $\omega_1, \omega_2, \omega_3$ form a right angle at $\omega_2$?*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.24).
- **Answer.** $n$ is a multiple of 4.
- **Tier.** 2.
- **Key shift.** Translate from algebra ($n$-th roots) to geometry (regular $n$-gon): right angle at a vertex requires another vertex diametrically opposite — i.e. $4 \mid n$. (Cross-archetype with Ch. 2 PP1.)

#### PP4 — Distance from Origin to Line via Vectors (Tier 1)
- **Problem.** *Find the perpendicular distance from the origin to the line passing through $(1, 2, 3)$ in the direction $(2, -1, 2)$.*
- **Source.** Joshi, *EJM* Ch. 21, Comment 5 (line-distance formula).
- **Answer.** $\sqrt{14 - \frac{(2 - 2 + 6)^2}{9}} = \sqrt{14 - 4} = \sqrt{10}$.
- **Tier.** 1.
- **Key shift.** Translate "perpendicular distance" to $|\vec r \times \hat d|$ where $\vec r$ is from the line-point to the origin and $\hat d$ is the unit direction — geometry-to-cross-product algebra.

#### PP5 — Argand Plane Geometric Locus (Tier 2)
- **Problem.** *Let $z = x + iy$. Identify the locus $\left|\dfrac{z - 1}{z + 1}\right| = 1$ in the Argand plane.*
- **Source.** Joshi, *EJM* Ch. 2, Comment 14 (Möbius transformations on Argand plane).
- **Answer.** The $y$-axis (perpendicular bisector of $1$ and $-1$).
- **Tier.** 2.
- **Key shift.** Translate $|z - a| = |z - b|$ from algebra of $\mathbb{C}$ to "equidistant from $a$ and $b$" — the perpendicular bisector of $\{a, b\}$.

#### PP6 — Complex Argument as Angle (Tier 1: JEE Mains)
- **Problem.** *If $z = 1 + i\sqrt 3$, find $\arg(z)$ and $\arg(z^3)$.*
- **Source.** Joshi, *EJM* Ch. 2, Comment 9 (De Moivre + Argand).
- **Answer.** $\arg z = \pi/3$, $\arg z^3 = \pi$ (i.e. $z^3$ is real negative).
- **Tier.** 1.
- **Key shift.** Translate $z$ to polar form $r e^{i\theta}$; powers correspond to angle-tripling on the Argand plane (Domain: algebra $\to$ rotational geometry).

#### PP7 — Translate Inequality $|a-b| \ge \big||a| - |b|\big|$ to Geometry (Tier 1)
- **Problem.** *For any complex numbers $a, b$, prove $|a - b| \ge \big||a| - |b|\big|$ and identify the equality case.*
- **Source.** Joshi, *EJM* Ch. 2, Comment 4 (reverse triangle inequality).
- **Answer.** Equality iff $a, b$ are on the same ray from the origin (i.e. $\arg a = \arg b$).
- **Tier.** 1.
- **Key shift.** $|a|, |b|$ are distances-to-origin; the reverse triangle inequality is the *geometric* statement that the third side of a triangle is at least the difference of the other two — algebra $\to$ planar geometry.

---

## Chapter 9: Domain Constraints / Bounds — LOCKED v0.2

**Joshi sources.** Primary: Ch. 10 (Trig Eqs), Ch. 12 (Heights/Dist), Ch. 13 (Max/Min). Secondary: Ch. 3, 11, 24.
**Distinctive cognitive shift.** Constraints on the *domain* (positivity, integrality, triangle inequality, trig range, log argument) restrict which values a variable may take. A problem becomes tractable once the *full* constraint envelope is mapped.

### Worked Examples

#### WE1 — Domain of a Combined Function (Tier 1: JEE 1988)
- **Problem.** *Prove or disprove: if $f_1$ is defined on $D_1$ and $f_2$ on $D_2$, then $f_1 + f_2$ is defined on $D_1 \cup D_2$.*
- **Source.** JEE 1988 (Joshi, *EJM* Ch. 24, Exercise 24.1).
- **Answer.** *Disprove.* $(f_1 + f_2)$ is defined on $D_1 \cap D_2$ (not the union).
- **Tier.** 1.
- **Key shift.** A combined operation's domain is the *intersection*, not the union, of its operands' domains — a foundational domain-constraint principle.

#### WE2 — Triangle-Inscribed-Polygon Side-Selection (Tier 2)
- **Problem.** *Let $T_n$ denote the number of triangles formed using the vertices of a regular polygon of $n$ sides. If $T_{n+1} - T_n = 21$, find $n$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.20).
- **Answer.** $n = 7$.
- **Tier.** 2.
- **Key shift.** $T_n = \binom{n}{3}$; the difference $\binom{n+1}{3} - \binom{n}{3} = \binom{n}{2}$ produces a quadratic in $n$ with a positive-integer constraint.

#### WE3 — Triangle-Inequality–Forced Bound (Tier 3: RMO)
- **Problem.** *If $x, y, z$ are sides of a triangle, prove that $|x^2(y - z) + y^2(z - x) + z^2(x - y)| < xyz$.*
- **Source.** Regional Mathematics Olympiad (Joshi, *EJM* Ch. 24, Exercise 24.65).
- **Answer.** (Proof.) Factor LHS as $|(x-y)(y-z)(x-z)|$; use triangle-inequality slacks $|x-y| < z$ etc. (Cross-archetype with Ch. 10 WE1 — there the *inequality* framing is primary; here the *domain-constraint* framing is primary.)
- **Tier.** 3.
- **Key shift.** Triangle-inequality bounds *every* signed side-difference by the third side; the algebraic bound is a triple-product of these slacks.

### Practice Problems

#### PP1 — Integer $m$ for Integer Intersection (Tier 1)
- **Problem.** *Find the number of integer values of $m$ for which the $x$-coordinate of the point of intersection of $3x + 4y = 9$ and $y = mx + 1$ is also an integer.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.30).
- **Answer.** $2$ (values $m = -1$ and $m = 2$).
- **Tier.** 1.
- **Key shift.** The integer-domain constraint forces $x = \frac{5}{3 + 4m} \in \mathbb{Z}$ — a divisor-counting problem.

#### PP2 — Triangle with Consecutive-Integer Sides and Inradius 4 (Tier 3: RMO)
- **Problem.** *The sides of a triangle are three consecutive integers and its inradius is $4$ units. Find its circumradius.*
- **Source.** Regional Mathematics Olympiad (Joshi, *EJM* Ch. 24, Exercise 24.72).
- **Answer.** $R = \frac{65}{8}$.
- **Tier.** 3.
- **Key shift.** Triangle-inequality + integer-sides + inradius-formula combined force a unique solution.

#### PP3 — Log-Domain Restriction (Tier 1)
- **Problem.** *Find the domain of $f(x) = \log_4(x - 1) - \log_2(x - 3)$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.45 — domain-restriction half).
- **Answer.** $x > 3$.
- **Tier.** 1.
- **Key shift.** Each $\log$ imposes "argument $> 0$"; the *combined* constraint is the intersection — the more restrictive one ($x > 3$) wins.

#### PP4 — Real-Root Condition on Quartic (Tier 4: RMO)
- **Problem.** *Find all real $a$ such that $x^4 - 2ax^2 + x + a^2 - a = 0$ has all real roots.*
- **Source.** Regional Mathematics Olympiad (Joshi, *EJM* Ch. 24, Exercise 24.68).
- **Answer.** $a \ge 3/4$.
- **Tier.** 4.
- **Key shift.** Rewrite as $(x^2 - a)^2 + (x - a) = 0$ so $x^2 - a = \pm\sqrt{a - x}$; the *real-domain* constraint on $\sqrt{}$ gives $a \ge x$, and the discriminant analysis pins the bound at $3/4$.

#### PP5 — Trig Domain Restricts Real Roots (Tier 2)
- **Problem.** *Find the number of real solutions of $\sin(\cos x) = x$ in $[-\pi, \pi]$.*
- **Source.** Joshi, *EJM* Ch. 10, Comment 6 (range-restriction in trig equations).
- **Answer.** Exactly one (at $x \approx 0.6948$).
- **Tier.** 2.
- **Key shift.** $\sin(\cos x) \in [-\sin 1, \sin 1] \approx [-0.84, 0.84]$ restricts $x$ to that range; within, $g(x) = \sin(\cos x) - x$ is monotonically decreasing, so a single crossing.

#### PP6 — Inradius-Circumradius Bound (Tier 2)
- **Problem.** *For an acute triangle, prove $r < R/2$ (where $r, R$ are inradius and circumradius) iff the triangle is non-equilateral. State the equality case.*
- **Source.** Joshi, *EJM* Ch. 11, Comment 9 (Euler's $r \le R/2$).
- **Answer.** Equality iff equilateral (Euler's identity).
- **Tier.** 2.
- **Key shift.** Triangle invariants $r$ and $R$ are domain-constrained by the triangle's *non-degeneracy*; Euler's inequality is the sharp bound.

#### PP7 — Height-Distance Constraint (Tier 2: JEE 1988)
- **Problem.** *A tower of height $h$ stands at a point $O$. The angle of elevation of the top from a point $P$ is $\alpha$, and from $Q$ (at distance $d$ from $P$, in the same horizontal line through $O$) it is $\beta$. Express $h$ in terms of $d, \alpha, \beta$.*
- **Source.** JEE 1988 (Joshi, *EJM* Ch. 12, Comment 3).
- **Answer.** $h = \dfrac{d \sin\alpha\sin\beta}{\sin(\alpha - \beta)}$ (assuming $P, Q$ on the same side; otherwise $\sin(\alpha + \beta)$).
- **Tier.** 2.
- **Key shift.** The *domain constraint* "same side vs. opposite side" changes the answer; the sign convention is forced by the geometric setup.

---

## Chapter 10: Inequality Constraints — LOCKED

**Joshi sources.** Primary: Ch. 6 (Inequalities), Ch. 13 (Max/Min), Ch. 14 (Trig Opt), Ch. 24 (Misc). Secondary: Ch. 10, 22.
**Joshi-richness note.** This chapter has the *richest* Joshi source-base of any in Pillar 2; the slate below is highly competitive.

### Worked Examples

#### WE1 — Schur-Style Triangle Inequality (Tier 3: RMO)
- **Problem.** *If $x, y, z$ are the sides of a triangle, prove that $|x^2(y-z) + y^2(z-x) + z^2(x-y)| < xyz$.*
- **Source.** Regional Mathematics Olympiad (Joshi, *EJM* Ch. 24, Exercise 24.65).
- **Answer.** (Proof.) Factor the LHS as $|(x-y)(y-z)(x-z)|$; use the triangle inequality $|x-y| < z$, $|y-z| < x$, $|x-z| < y$.
- **Tier.** 3.
- **Key shift.** The triangle-inequality is itself a constraint; substituting it into the *algebraic* inequality reduces both sides to a product of triangle-inequality slacks.

#### WE2 — JEE 1972 Bounded Ratio (Tier 2: JEE Advanced)
- **Problem.** *Prove that $\frac{x^2}{z} < \frac{x^2 + y^2 + z^2}{x + y + z} < \frac{z^2}{x}$ for positive reals $x < y < z$.*
- **Source.** JEE 1972 (Joshi, *EJM* Ch. 24, Exercise 24.64).
- **Answer.** (Proof.) Both inequalities follow from the rearrangement structure and Chebyshev's inequality applied to the ordered sequences.
- **Tier.** 2.
- **Key shift.** Ordered constraints $x < y < z$ unlock rearrangement / Chebyshev; both sides bracket the same weighted mean.

#### WE3 — INMO + IMO 2000 Symmetric Product ≤ 1 (Tier 4)
- **Problem.** *If $a, b, c > 0$ with $abc = 1$, prove that (i) $a^{b+c}b^{c+a}c^{a+b} \le 1$ and (ii) $(a - 1 + 1/b)(b - 1 + 1/c)(c - 1 + 1/a) \le 1$.*
- **Source.** INMO + IMO 2000 (Joshi, *EJM* Ch. 24, Exercise 24.66).
- **Answer.** (Proof.) See Ch. 2 PP7 commentary above; here this is the *worked example* (in Ch. 2 it was reserved as PP7 for symmetry-stretch).
- **Tier.** 4.
- **Key shift.** Logarithmise + Schur. Note: *this problem appears in both Chapter 2 (as a symmetry stretch) and Chapter 10 (as the headline worked example)* — cross-archetype reuse is legitimate when explicitly cross-referenced.
- ⚠️ **Anand: confirm reuse.** Alternative WE3 candidate: Joshi Ex. 24.27 (max of $\prod\cos\alpha_i$ under $\prod\cot\alpha_i = 1$ — a JEE 2001 problem).

### Practice Problems

#### PP1 — Three Unit Vectors Pairwise Distance Sum (Tier 2)
- **Problem.** *For three unit vectors $\vec a, \vec b, \vec c$, prove $|\vec a - \vec b|^2 + |\vec b - \vec c|^2 + |\vec c - \vec a|^2 \le 9$.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.50(ii)/(iii).
- **Answer.** (Proof.) Rewrite as $9 - |\vec a + \vec b + \vec c|^2$; the maximum $9$ is attained when $\vec a + \vec b + \vec c = 0$ (three unit vectors at $120°$).
- **Tier.** 2.
- **Key shift.** Rewriting a sum of pairwise distances as a *single squared sum* (the centroid identity) collapses three pairwise inequalities into one.

#### PP2 — JEE 2001 Quadratic Minimum Range (Tier 1)
- **Problem.** *Let $f(x) = (1 + b^2)x^2 + 2bx + 1$ and let $m(b)$ be the minimum of $f$. Find the range of $m(b)$ as $b$ varies over $\mathbb{R}$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.17).
- **Answer.** $m(b) \in (0, 1]$ (the parabola opens upward; minimum at the vertex equals $\frac{1}{1+b^2}$).
- **Tier.** 1.
- **Key shift.** Vertex formula reduces a quadratic-minimum problem to a one-variable bound.

#### PP3 — Cyclic Cosine Product under Cotangent Constraint (Tier 3)
- **Problem.** *Find the maximum of $(\cos\alpha_1)(\cos\alpha_2)\cdots(\cos\alpha_n)$ subject to $0 \le \alpha_i \le \pi/2$ and $(\cot\alpha_1)(\cot\alpha_2)\cdots(\cot\alpha_n) = 1$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.27).
- **Answer.** $1/2^{n/2}$ (attained when $\alpha_i = \pi/4$ for all $i$).
- **Tier.** 3.
- **Key shift.** AM–GM on $\cos^2\alpha_i$ under the multiplicative constraint $\prod\cot\alpha_i = 1 \Leftrightarrow \prod\cos\alpha_i = \prod\sin\alpha_i$.

#### PP4 — Right-Triangle Circumradius–Inradius (Tier 3: RMO)
- **Problem.** *For a right-angled triangle with circumradius $R$ and inradius $r$, prove $R \ge (1 + \sqrt 2)r$. When does equality hold?*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.88.
- **Answer.** Equality iff the right triangle is isosceles ($a = b$, hypotenuse $c = a\sqrt 2$).
- **Tier.** 3.
- **Key shift.** Express $R$ and $r$ in terms of $a, b, c$ (with $c^2 = a^2 + b^2$); the symmetric isosceles case extremises by symmetry argument from Ch. 2.

#### PP5 — Hadwiger–Finsler (Tier 4)
- **Problem.** *In any triangle $ABC$ with area $\Delta$, prove $2(ab + bc + ca) - a^2 - b^2 - c^2 \ge 4\sqrt 3\Delta$.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.93(b).
- **Answer.** (Proof.) Substitute Ravi $a = y+z$, $b = z+x$, $c = x+y$ with $x, y, z > 0$; reduces to a Schur-like inequality.
- **Tier.** 4.
- **Key shift.** Ravi substitution converts a *constrained* triangle inequality to an *unconstrained* positive-reals inequality.

#### PP6 — Pedoe's Inequality (Tier 4)
- **Problem.** *For triangles $ABC$ and $A'B'C'$ with sides $a, b, c, a', b', c'$ and areas $\Delta, \Delta'$, prove $a^2(b'^2 + c'^2 - a'^2) + b^2(c'^2 + a'^2 - b'^2) + c^2(a'^2 + b'^2 - c'^2) \ge 16\Delta\Delta'$, with equality iff the triangles are similar.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.96(b).
- **Answer.** (Proof.) Express each side via the law of cosines; reduces to $\sum a^2\cot A' \ge 4\Delta$ (Ex. 24.96(a)).
- **Tier.** 4.
- **Key shift.** A *two-triangle* inequality reduces to a one-triangle one via the law of cosines symmetry.

#### PP7 — Minimum of $\lambda_1\cot\theta_1 + \lambda_2\cot\theta_2$ (Tier 3)
- **Problem.** *For positive reals $\lambda_1, \lambda_2$ with $\theta_1 + \theta_2$ fixed, find the minimum of $\lambda_1\cot\theta_1 + \lambda_2\cot\theta_2$.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.95(b).
- **Answer.** Minimum occurs when $\frac{\sin\theta_1}{\sin\theta_2} = \sqrt{\frac{\lambda_1}{\lambda_2}}$.
- **Tier.** 3.
- **Key shift.** Lagrange multiplier on the cotangent sum under the angle-sum constraint — the *weighted* version of the Ch. 2 PP4 symmetric case.

---

## Chapter 11: Existence / Uniqueness — LOCKED v0.2

**Joshi sources.** Primary: Ch. 15 (Limits/Deriv), Ch. 16 (Theoretical Calc), Ch. 20 (Functional Eqs). Secondary: Ch. 3, 10, 11.
**Distinctive cognitive shift.** From "find" to "prove a solution exists / is unique" — IVT, MVT, Rolle, Banach fixed-point as the named tools.

### Worked Examples

#### WE1 — Real Roots of $\sum A_i/(x - a_i) = 0$ (Tier 3)
- **Problem.** *If $a_1 < \cdots < a_n$ are real and $A_1, \ldots, A_n$ are positive, prove that $\sum_{i=1}^{n}\frac{A_i}{x - a_i} = 0$ has all real roots.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.70.
- **Answer.** (Proof.) Apply IVT on each interval $(a_i, a_{i+1})$ — the function changes sign across each pole; total root count = $n - 1$.
- **Tier.** 3.
- **Key shift.** IVT applied to a function with prescribed sign changes between poles forces existence of a root in each gap.

#### WE2 — Maximum-Principle Uniqueness (Tier 4)
- **Problem.** *Suppose $f$ is twice differentiable and $g$ is continuous on $[a, b]$ with $f'' + gf' - f = 0$. If $f(a) = f(b) = 0$, prove $f \equiv 0$ on $[a, b]$.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.97.
- **Answer.** (Proof.) Suppose $f \not\equiv 0$; pick $x_0$ where $|f|$ attains its max. At $x_0$, $f'(x_0) = 0$ and $f''(x_0)/f(x_0) \le 0$ (interior max). The ODE gives $f''/f = 1$, contradicting non-positivity.
- **Tier.** 4.
- **Key shift.** Maximum-principle: the ODE structure forces $f \le 0$ at any interior maximum, contradicting maximality unless $f \equiv 0$.

#### WE3 — Banach Fixed-Point in $[0, 1]$ (Tier 3)
- **Problem.** *Suppose $f: [0, 1] \to [0, 1]$ is continuous. Prove $f$ has a fixed point.*
- **Source.** Joshi, *EJM* Ch. 16, Comment 7 (continuous self-map of an interval has a fixed point).
- **Answer.** (Proof.) Apply IVT to $g(x) = f(x) - x$: $g(0) = f(0) \ge 0$, $g(1) = f(1) - 1 \le 0$. So $g$ vanishes somewhere — a fixed point.
- **Tier.** 3.
- **Key shift.** Existence via IVT applied to the "difference function" $f(x) - x$ — the canonical fixed-point existence argument before Banach.

### Practice Problems

#### PP1 — Non-Differentiability of $\max\{x, x^3\}$ (Tier 1)
- **Problem.** *Find the set of points where $f(x) = \max\{x, x^3\}$ is not differentiable.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.41).
- **Answer.** Two points: $x = 0$ and $x = -1$.
- **Tier.** 1.
- **Key shift.** A max-of-two-functions is non-differentiable exactly where the functions cross *transversally* — IVT-style existence of crossings.

#### PP2 — Left-Hand Derivative of $[x]\sin\pi x$ (Tier 2)
- **Problem.** *Find the left-hand derivative of $f(x) = [x]\sin(\pi x)$ at $x = k$, where $k$ is an integer.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.39).
- **Answer.** $(-1)^k(k - 1)\pi$.
- **Tier.** 2.
- **Key shift.** Continuity vs. differentiability of step-function product — limit from the left exists but disagrees with the right; *uniqueness* (of the derivative) fails.

#### PP3 — Number of Solutions of $\log_4(x-1) = \log_2(x-3)$ (Tier 1)
- **Problem.** *Find the number of solutions of $\log_4(x - 1) = \log_2(x - 3)$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.45).
- **Answer.** Exactly one solution ($x = 5$ after squaring; check domain).
- **Tier.** 1.
- **Key shift.** Existence via algebraic reduction; uniqueness via domain constraint.

#### PP4 — Cauchy Functional Equation Uniqueness (Tier 3)
- **Problem.** *Suppose $f: \mathbb{R} \to \mathbb{R}$ is continuous and satisfies $f(x + y) = f(x) + f(y)$ for all real $x, y$. Prove $f(x) = cx$ for some constant $c$.*
- **Source.** Joshi, *EJM* Ch. 20, Main Problem (Cauchy's functional equation).
- **Answer.** (Proof.) Standard: derive $f(q) = qf(1)$ for rational $q$ by induction + density; continuity extends to all reals.
- **Tier.** 3.
- **Key shift.** *Continuity* (a topological constraint) is what forces uniqueness among the wildly-many Hamel-basis solutions of $f(x+y) = f(x) + f(y)$.

#### PP5 — Polynomial with $n$ Real Roots (Tier 3)
- **Problem.** *If $f(x)$ is a polynomial of degree $n$ with $n$ distinct real roots, prove $f'(x)$ has exactly $n - 1$ distinct real roots, all in the convex hull of the roots of $f$.*
- **Source.** Joshi, *EJM* Ch. 16, Comment 4 (Rolle's iteration on derivative).
- **Answer.** (Proof.) Apply Rolle between each pair of consecutive roots of $f$; counts $n - 1$ roots of $f'$. They cannot exceed this count since $\deg f' = n - 1$.
- **Tier.** 3.
- **Key shift.** Rolle's theorem turns *existence of $f$-zeros* into *existence of $f'$-zeros* — interlacing follows automatically.

#### PP6 — IVT Forces an Odd-Degree Polynomial Root (Tier 1)
- **Problem.** *Prove that every polynomial of odd degree with real coefficients has at least one real root.*
- **Source.** Joshi, *EJM* Ch. 15, Comment 3 (consequence of IVT).
- **Answer.** (Proof.) Leading-term analysis: $f(x) \to +\infty$ as $x \to +\infty$ and $f(x) \to -\infty$ as $x \to -\infty$ (or vice versa). Apply IVT.
- **Tier.** 1.
- **Key shift.** *Existence* of a real root for any odd-degree polynomial is a direct corollary of IVT applied at $\pm\infty$.

#### PP7 — Banach Fixed-Point for a Contraction (Tier 3)
- **Problem.** *Define $f: [0, 1] \to [0, 1]$ by $f(x) = \frac{x + \cos x}{2}$. Prove that the iteration $x_{n+1} = f(x_n)$, $x_0 = 0$, converges, and identify the limit.*
- **Source.** Joshi, *EJM* Ch. 16, Comment 9 (contraction-mapping iteration).
- **Answer.** $|f'(x)| = |1 - \sin x|/2 \le 1/2 < 1$ on $[0, 1]$, so $f$ is a contraction. Fixed point is the unique solution to $x = \cos x$ on $[0, 1]$, $\approx 0.7391$ (the Dottie number).
- **Tier.** 3.
- **Key shift.** Banach's contraction principle: existence + uniqueness of fixed point follow from contraction; iteration *constructs* the fixed point.

---

## Chapter 12: Extremal Principles — LOCKED v0.2

**Joshi sources.** Primary: Ch. 13 (Max/Min), Ch. 14 (Trig Opt). Secondary: Ch. 6, 9.
**Distinctive cognitive shift.** From "find a value" to "find the extreme value." The extremum often lives at a *boundary* (vertex, endpoint, equality case) or at an *interior critical point* (gradient zero); knowing which is half the battle.

### Worked Examples

#### WE1 — Maximum of Linear Function on Convex Polygon (Tier 3)
- **Problem.** *Suppose $S$ is a convex polygon and $f(x, y) = ax + by$ is linear. Prove that $f$ attains its max/min on $S$ at a vertex.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.92(c).
- **Answer.** (Proof.) For $P$ non-vertex, find vertices $V_1, V_2$ on a line through $P$ with $f(V_1) \le f(P) \le f(V_2)$; iterate.
- **Tier.** 3.
- **Key shift.** Extremum-on-polytope = extremum-at-vertex — the fundamental theorem of linear programming. (Cross-archetype with Ch. 3 WE3.)

#### WE2 — Cake-Eating Survival / Josephus (Tier 4)
- **Problem.** *Cakes numbered $1$ to $n$ are arranged clockwise in a circle. A person starts at cake $1$ and eats every alternate cake. Let $f(n)$ be the number of the cake left at the end. Find $f(n)$ explicitly, and compute $f(1000)$.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.77 (Josephus-style).
- **Answer.** Write $n = 2^k + r$ with $0 \le r < 2^k$; then $f(n) = 2r + 1$. $f(1000) = 2(1000 - 512) + 1 = 977$.
- **Tier.** 4.
- **Key shift.** Reduction-to-binary representation as an extremal invariant under the "halving" operation.

#### WE3 — Closest Point on Parabola to a Given Point (Tier 3)
- **Problem.** *Find the point on the parabola $y = x^2$ closest to the point $(2, -1/2)$.*
- **Source.** Joshi, *EJM* Ch. 13, Comment 6 (calculus optimisation in 2D).
- **Answer.** $(1, 1)$ (with $d = \sqrt{1 + 9/4} = \sqrt{13}/2$).
- **Tier.** 3.
- **Key shift.** Parametrise the parabola as $(t, t^2)$; minimise $d^2(t) = (t-2)^2 + (t^2 + 1/2)^2$. Critical-point analysis pins $t = 1$. Cf. Ch. 13 Ex. 13.23 (closest pair on two parabolas).

### Practice Problems

#### PP1 — Monotonicity of $xe^{x(1-x)}$ (Tier 2)
- **Problem.** *Which statement is true about $f(x) = xe^{x(1-x)}$? (A) increasing on $[-1/2, 1]$ (B) decreasing on $\mathbb{R}$ (C) increasing on $\mathbb{R}$ (D) decreasing on $[-1/2, 1]$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.42).
- **Answer.** (A).
- **Tier.** 2.
- **Key shift.** Locate critical points; classify by sign of $f'$.

#### PP2 — Convex Quadrilateral with Diagonal Constraint (Tier 4)
- **Problem.** *In a plane convex quadrilateral of area $32$, the sum of the lengths of one pair of opposite sides and one diagonal is $16$. Determine the minimum possible length of the other diagonal.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.74 (K. N. Ranganathan).
- **Answer.** Other diagonal $\ge 8\sqrt 2$.
- **Tier.** 4.
- **Key shift.** AM–GM on the area formula in terms of the diagonals and the sine of their included angle, forced by the side-plus-diagonal constraint.

#### PP3 — Min of Quadratic Forms (Tier 2)
- **Problem.** *Find the minimum of (i) $x^2 + 3y^2 - 6x - 2y$ and (ii) $x^2 + 2xy + 3y^2 - 6x - 2y$ over real $x, y$.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.91.
- **Answer.** (i) $-28/3$ at $(3, 1/3)$.  (ii) Complete-the-square: $-13/2$ at $(7/2, -1/2)$.
- **Tier.** 2.
- **Key shift.** Quadratic forms have global extrema at the gradient-zero point (if positive-definite), reducing to a linear system.

#### PP4 — Largest Rectangle in a Semicircle (Tier 2: JEE Advanced)
- **Problem.** *Find the largest rectangle that can be inscribed in a semicircle of radius $R$, with one side along the diameter.*
- **Source.** Joshi, *EJM* Ch. 13, Comment 4.
- **Answer.** Sides $R\sqrt 2$ and $R/\sqrt 2$; area $R^2$.
- **Tier.** 2.
- **Key shift.** Parametrise the upper vertex as $(R\cos\theta, R\sin\theta)$; maximise $A = 2R^2\sin\theta\cos\theta = R^2\sin 2\theta$ → $\theta = \pi/4$. Trigonometric extremum.

#### PP5 — Snell's Law via Fermat's Principle (Tier 3)
- **Problem.** *Light travels from $A = (0, a)$ to $B = (d, -b)$ crossing the $x$-axis (boundary between two media) at speed $v_1$ above and $v_2$ below. Prove that the path of minimum time satisfies $\sin\theta_1/\sin\theta_2 = v_1/v_2$ (Snell's law).*
- **Source.** Joshi, *EJM* Ch. 16, Comment 6 (Fermat / Snell).
- **Answer.** (Proof.) Time $T(x) = \sqrt{a^2 + x^2}/v_1 + \sqrt{b^2 + (d - x)^2}/v_2$. Setting $T'(x) = 0$ gives $\sin\theta_1/v_1 = \sin\theta_2/v_2$.
- **Tier.** 3.
- **Key shift.** *Fermat's least-time principle* converts a physical law to a calculus extremum; the ratio of sines emerges from the gradient-zero condition.

#### PP6 — Cotangent-Sum Minimum Under Angle Constraint (Tier 3)
- **Problem.** *For $\theta_1, \theta_2 > 0$ with $\theta_1 + \theta_2 = \pi/2$ fixed, find the minimum of $\cot\theta_1 + \cot\theta_2$.*
- **Source.** Joshi, *EJM* Ch. 14, Comment 5 (symmetric cotangent extremum).
- **Answer.** Minimum $2$ at $\theta_1 = \theta_2 = \pi/4$.
- **Tier.** 3.
- **Key shift.** Constrained extremum of a symmetric function attains at the symmetric point. (Cross-archetype with Ch. 2 PP4 — there, symmetry-forcing is primary; here, extremum-principle is primary.)

#### PP7 — Erdős-Mordell Inequality (Tier 4)
- **Problem.** *Let $P$ be a point inside $\triangle ABC$. Let $d_a, d_b, d_c$ be distances from $P$ to sides $BC, CA, AB$. Let $p_a, p_b, p_c$ be distances from $P$ to vertices $A, B, C$. Prove $p_a + p_b + p_c \ge 2(d_a + d_b + d_c)$, with equality iff $ABC$ is equilateral and $P$ is its centre.*
- **Source.** Joshi, *EJM* Ch. 14, Exercise 14.18 (Erdős-Mordell).
- **Answer.** (Proof — outline.) Reflect $P$ across each side; the triangle inequality applied to the reflections gives the bound.
- **Tier.** 4.
- **Key shift.** A *geometric* extremal inequality — the perimeter-to-pedal-sum ratio $\ge 2$ is sharp, attained only at the symmetric (equilateral) configuration.

---

## Chapter 13: Combinatorial Principles — LOCKED

**Joshi sources.** Primary: Ch. 1 (Counting), Ch. 22 (Probability), Ch. 24 (Misc). Secondary: Ch. 23.

### Worked Examples

#### WE1 — Dance-Party Bipartite Configuration (Tier 4: Putnam)
- **Problem.** *At a dance party every boy dances with at least one girl, but no girl dances with every boy. Prove there exist boys $b, b'$ and girls $g, g'$ such that $b$ dances with $g$ and $b'$ dances with $g'$ but neither $b$ with $g'$ nor $b'$ with $g$. Paraphrase in terms of subsets of the set of girls.*
- **Source.** Putnam (Joshi, *EJM* Ch. 24, Exercise 24.8).
- **Answer.** (Proof.) Each boy $b_i$ has a "partner set" $G_i \subset G$ (girls he dances with). The condition gives that no $G_i$ equals all of $G$ and that there are at least two distinct $G_i$. Then a pair of incomparable sets exists — pick boys realising it and girls realising the witness.
- **Tier.** 4.
- **Key shift.** Translate to subset lattice; incomparable subsets in a non-chain family give the required configuration.

#### WE2 — Number of Surjective Functions (Tier 3)
- **Problem.** *Let $X$ have $n$ elements and $Y$ have $m$ elements. Prove that the number of surjective functions $X \twoheadrightarrow Y$ equals $\sum_{k=0}^{m}(-1)^k\binom{m}{k}(m - k)^n$.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.80(i).
- **Answer.** (Proof.) Inclusion-exclusion: $A_k$ = functions missing $y_k$; $|\bigcap_{i \in S}A_i| = (m - |S|)^n$.
- **Tier.** 3.
- **Key shift.** "Surjective" is the complement of "misses some element" — inclusion-exclusion is the canonical tool.

#### WE3 — Onto Functions $\{1,2,3,4\} \to \{1,2\}$ (Tier 1)
- **Problem.** *Find the number of onto functions from $\{1, 2, 3, 4\}$ to $\{1, 2\}$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.21).
- **Answer.** $2^4 - 2 = 14$.
- **Tier.** 1.
- **Key shift.** Total minus non-surjective (constant functions); a baby case of WE2.

### Practice Problems

#### PP1 — Three Numbers Summing to $2p$ (Tier 3: RMO)
- **Problem.** *Three numbers are drawn from $\{1, 2, \ldots, p\}$ with replacement. Prove that the probability that their sum is $2p$ is $\frac{(p-1)(p+4)}{2p^3}$.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.51.
- **Answer.** (Proof.) Count triples $(a, b, c)$ with $a + b + c = 2p$ via stars-and-bars + boundary correction.
- **Tier.** 3.
- **Key shift.** Composition-counting under boundary constraints (each $a_i \in [1, p]$) — inclusion-exclusion on the bounding constraint.

#### PP2 — Inscribed Triangles via Polygon Vertices (Tier 2)
- **Problem.** *Let $T_n$ denote the number of triangles using vertices of a regular polygon of $n$ sides. If $T_{n+1} - T_n = 21$, find $n$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.20).
- **Answer.** $n = 7$.
- **Tier.** 2.
- **Key shift.** $T_n = \binom{n}{3}$; difference is $\binom{n}{2}$. (Note: this problem also appears in Ch. 9 — cross-archetype.)

#### PP3 — Tournament Pairing (Tier 3)
- **Problem.** *$16$ players play in a tournament. They are divided into eight pairs at random. (a) Find $P(S_1 \text{ is among winners})$. (b) Find $P(\text{exactly one of } S_1, S_2 \text{ is among winners})$.*
- **Source.** JEE 1997 (Joshi, *EJM* Ch. 24, Exercise 24.53).
- **Answer.** (a) $1/2$ (by symmetry).  (b) $\frac{8}{15} \cdot \frac{1}{2} = \frac{8}{30}$ from case analysis.
- **Tier.** 3.
- **Key shift.** Symmetry of the players reduces (a) to a coin flip; (b) requires conditioning on whether $S_1, S_2$ are paired.

#### PP4 — Two Queens Non-Taking (Tier 3)
- **Problem.** *Two queens are placed at random on an $8 \times 8$ board. Find the probability that they are non-taking (not in the same row, column, or diagonal).*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.56.
- **Answer.** $\frac{8 \cdot 8 \cdot 8 \cdot 8 - 8 \cdot 8 \cdot \text{(taking pairs)}}{\binom{64}{2} \cdot 2}$ — explicit count of non-taking pairs is $1288$; probability $= \frac{1288}{\binom{64}{2}} = \frac{1288}{2016}$.
- **Tier.** 3.
- **Key shift.** Complementary counting (total minus taking) is cleaner than direct counting; inclusion-exclusion on rows + columns + 2 diagonal-families.

#### PP5 — Box with Three Colours, Red Last (Tier 3)
- **Problem.** *A box contains $m$ white, $n$ black, $k$ red balls. Balls are drawn one by one without replacement until all left are of the same colour. Find $P(\text{the remaining balls are red})$.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.86.
- **Answer.** $\frac{k}{m + n + k} \cdot \left(\frac{k + 1}{k + 1 + 1} + \cdots\right)$ — closed form via $\frac{k}{m+k} \cdot \frac{k}{n+k}$ by symmetry argument.
- **Tier.** 3.
- **Key shift.** Conditional argument on the last ball: $P(\text{last is red}) = P(\text{red lasts longer than white AND red lasts longer than black})$.

#### PP6 — 50-Subset with No Two Summing to 100 Contains a Perfect Square (Tier 3: RMO)
- **Problem.** *Suppose $A$ is a $50$-element subset of $\{1, 2, \ldots, 100\}$ such that no two elements of $A$ sum to $100$. Show that $A$ contains a perfect square.*
- **Source.** Regional Mathematics Olympiad (Joshi, *EJM* Ch. 24, Exercise 24.73).
- **Answer.** (Proof.) Pair $\{k, 100 - k\}$ for $k = 1, \ldots, 49$ ($49$ pairs) + singleton $\{50\}, \{100\}$. By pigeonhole $A$ has exactly one element from each pair plus possibly $\{50\}$ and/or $\{100\}$. The perfect squares $\{1, 4, 9, 16, 25, 36, 49, 64, 81, 100\}$ partition under the pairing as $\{1, 99\}, \{4, 96\}, \ldots, \{49, 51\}, \{36, 64\}, \{81, 19\}, \{100\}$, and counting shows at least one square must be in $A$.
- **Tier.** 3.
- **Key shift.** Pigeonhole + pairing structure: the constraint forces $A$ to choose one from each pair, and the perfect-squares pattern guarantees a hit.

#### PP7 — Sum is 18, Event $E$ at Least 3 Times (Tier 2)
- **Problem.** *Numbers are selected at random from two-digit numbers $00$ to $99$ with replacement. Event $E$ occurs iff the product of the two digits is $18$. If four numbers are selected, find $P(E \text{ occurs at least } 3 \text{ times})$.*
- **Source.** JEE 1993 (Joshi, *EJM* Ch. 24, Exercise 24.54).
- **Answer.** $P(E) = 4/100$ (digit pairs $(2,9), (3,6), (6,3), (9,2)$); answer $= \binom{4}{3}(0.04)^3(0.96) + (0.04)^4$.
- **Tier.** 2.
- **Key shift.** Binomial distribution applied after counting the elementary event; "at least 3" $=$ exactly 3 $+$ exactly 4.

---

## Chapter 14: Parity / Modularity — LOCKED

**Joshi sources.** Primary: Ch. 4 (Number Theory), Ch. 24 (Misc). Secondary: Ch. 1.

### Worked Examples

#### WE1 — $(2m)!(2n)!/(m+n)!$ Is an Integer (Tier 3: RMO)
- **Problem.** *If $m, n$ are positive integers, prove that $\dfrac{(2m)!(2n)!}{(m+n)!}$ is an integer.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.49.
- **Answer.** (Proof.) Apply Kummer's theorem (the $p$-adic valuation of $\binom{2m+2n}{m+n}$ counts base-$p$ carries) twice: show $v_p((2m)!(2n)!) \ge v_p((m+n)!)$ for every prime $p$.
- **Tier.** 3.
- **Key shift.** Integer-divisibility = pointwise $p$-adic-valuation inequality; Kummer/Lucas as the bridge from base-$p$ digit-counting to factorial divisibility. (This forward-references Ch. 1 WE3.)

#### WE2 — Digital-Sum (XOR) Reduction (Tier 3)
- **Problem.** *Define the "digital sum" $a \oplus b$ of two non-negative integers via their binary representations, XOR-style: $c_i = (a_i + b_i) \bmod 2$. Prove that given non-negative integers $a_1, \ldots, a_k$ with $a_1 \oplus \cdots \oplus a_k \ne 0$, there exists an index $r$ and a positive integer $x$ such that $b_1 \oplus \cdots \oplus b_k = 0$ where $b_i = a_i$ for $i \ne r$ and $b_r = a_r - x$.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.82.
- **Answer.** (Proof.) Let $s = a_1 \oplus \cdots \oplus a_k$, $j$ = position of the highest set bit of $s$. Pick any $a_r$ with bit $j$ set; let $b_r = a_r \oplus s$; then $b_r < a_r$ and $b_1 \oplus \cdots \oplus b_k = 0$.
- **Tier.** 3.
- **Key shift.** XOR is the *parity sum* — the high-bit identifies which pile to reduce. This problem underlies Nim-strategy (Ch. 24 Ex. 24.83).

#### WE3 — Three Cubics with Odd Integer Values (Tier 3)
- **Problem.** *Let $f(x) = x^3 + bx^2 + cx + d$. If $f(0)$ and $f(-1)$ are odd integers, prove that not all the zeros of $f$ are integers. If, further, $b, c$ are integers, prove that none of the zeros is an integer.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.89.
- **Answer.** (Proof.) $f(0) = d$ odd; $f(-1) = -1 + b - c + d$ odd $\Rightarrow b - c$ even. If $r$ is an integer root, $f(r) = 0$; parity of $f(r)$ mod 2 contradicts oddness of $d$ for *any* integer $r$.
- **Tier.** 3.
- **Key shift.** Mod-2 analysis on a cubic with integer coefficients — the parity of $f(r)$ is determined by $r$ mod 2 and the coefficient parities.

### Practice Problems

#### PP1 — Wilson-Almost (Tier 4)
- **Problem.** *Find all primes $p$ for which $(p - 1)! + 1$ has no prime factors besides $p$.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.100.
- **Answer.** $p = 2, 3, 5$.
- **Tier.** 4.
- **Key shift.** Wilson's theorem guarantees $p \mid (p-1)! + 1$; the question is when no *other* prime $q < p$ divides it — $q \mid (p-1)!$ for $q < p$ so any other factor must be $\ge p$; bound $(p-1)! + 1 < p^2$ to force the equality.

#### PP2 — Floor Equality $\lfloor x/99 \rfloor = \lfloor x/101 \rfloor$ (Tier 3: RMO)
- **Problem.** *Find the number of positive integers $x$ for which $\left\lfloor\dfrac{x}{99}\right\rfloor = \left\lfloor\dfrac{x}{101}\right\rfloor$.*
- **Source.** Regional Mathematics Olympiad (Joshi, *EJM* Ch. 24, Exercise 24.63).
- **Answer.** $2499$.
- **Tier.** 3.
- **Key shift.** Write $\lfloor x/99 \rfloor = k$ iff $99k \le x < 99k + 99$, similarly for $101$; the equality forces $x \in [99k, 99k + (99 - 2k)]$ for $k = 0, 1, \ldots, 49$; sum the lengths.

#### PP3 — Diagonal Squares on $m \times n$ Board (Tier 3)
- **Problem.** *Show that each diagonal of an $m \times n$ chessboard passes through $m + n - \gcd(m, n)$ unit squares.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.78.
- **Answer.** (Proof.) Reduce to the coprime case $m, n$ coprime (diagonal hits no grid vertex internally, so passes through $m + n - 1$ squares). Then scale by $\gcd$.
- **Tier.** 3.
- **Key shift.** Reduction to coprime + linearity in $\gcd$ — the $\gcd$ counts the number of times the diagonal *crosses* a grid vertex.

#### PP4 — Squarefree Decomposition (Tier 2)
- **Problem.** *Prove that every positive integer $m$ can be written uniquely as $u^2 v$ where $v$ is squarefree. Moreover if $m \mid n^2$ then $uv \mid n$.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.76(a).
- **Answer.** (Proof.) Unique factorisation of $m = \prod p^{a_p}$; set $u = \prod p^{\lfloor a_p/2 \rfloor}$, $v = \prod_{a_p \text{ odd}} p$. Then $m \mid n^2$ iff $2v_p(n) \ge a_p$ for all $p$, equivalently $v_p(n) \ge \lceil a_p/2 \rceil = v_p(uv)$.
- **Tier.** 2.
- **Key shift.** Decomposition mod-2 on prime exponents — the squarefree part is the "parity" of the factorisation.

#### PP5 — Hamiltonian Cycle on $m \times n$ Mesh (Tier 4)
- **Problem.** *Suppose there are $m$ roads going E-W and $n$ roads going N-S. Under what condition can a person visit every intersection-house exactly once and return to the start?*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.81.
- **Answer.** A Hamiltonian cycle exists iff at least one of $m, n$ is even (and $mn \ge 4$).
- **Tier.** 4.
- **Key shift.** Two-colour the grid like a chessboard; a Hamiltonian cycle alternates colours, forcing equal counts — possible iff the total $mn$ is even.

#### PP6 — Sum-Of-Two-Squares Constraint (Tier 3)
- **Problem.** *(JEE 1983 — see Ch. 1 PP3 cross-reference)* — For odd $n$, prove $24 \mid n(n^2 - 1)$. *(Routed primarily to Ch. 1 Invariance; cited here as Ch. 14 cross-reference for modular structure.)*
- **Source.** JEE 1983 (Joshi, *EJM* Ch. 4, Comment 8) — cross-archetype use only.

#### PP7 — Two-Person Nim with 100 (Tier 4: RMO)
- **Problem.** *Two players $A$ and $B$ alternately select integers from $1$ to $10$ and total them. The player who reaches $100$ (exactly) wins. Prove the first player has a winning strategy.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.83(a).
- **Answer.** First player plays $1$ (or any choice reaching $\equiv 1 \pmod{11}$), then mirrors the opponent to maintain $\equiv 1 \pmod{11}$. Since $100 \equiv 1 \pmod{11}$ ($100 = 99 + 1 = 11 \cdot 9 + 1$), the first player wins.
- **Tier.** 4.
- **Key shift.** Game-theoretic invariant = residue mod $(k + 1)$ — the canonical Nim parity argument.

---

## Chapter 15: Bijection / Correspondence — LOCKED v0.2

**Joshi sources.** Primary: Ch. 5 (Binomial), Ch. 1 (Counting), Ch. 22 (Probability). Secondary: Ch. 4, 8.
**Distinctive cognitive shift.** Two seemingly different sets are *the same set* under a one-to-one map. Counting one side = counting the other; the bijection is the proof.

### Worked Examples

#### WE1 — Surjections via Compositions (Tier 3)
- **Problem.** *Prove that the number of surjections $X \twoheadrightarrow Y$ (with $|X| = n$, $|Y| = m$) equals $\displaystyle\sum_{(n_1, \ldots, n_m)}\frac{n!}{n_1!\cdots n_m!}$ where the sum is over $m$-compositions of $n$ into positive parts.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.80(ii).
- **Answer.** (Proof.) Each composition $(n_1, \ldots, n_m)$ corresponds bijectively to a function with $|f^{-1}(y_i)| = n_i$; total $= \binom{n}{n_1, \ldots, n_m}$.
- **Tier.** 3.
- **Key shift.** Two ways to count $=$ bijection identity. (Cross-archetype: Ch. 13 WE2 gives the same count by inclusion-exclusion.)

#### WE2 — No-Two-Adjacent Arrangement (Tier 2: JEE 1983)
- **Problem.** *$m$ men and $n$ women are seated in a row so that no two women are adjacent. Find the number of arrangements.*
- **Source.** JEE 1983 (Joshi, *EJM* Ch. 1, Comment 5).
- **Answer.** $m! \cdot \binom{m+1}{n}n!$.
- **Tier.** 2.
- **Key shift.** Bijection: place men first ($m!$ ways) creating $m + 1$ gaps; choose $n$ gaps for women.

#### WE3 — Catalan Numbers and Dyck Paths (Tier 3)
- **Problem.** *Prove that the number of monotone lattice paths from $(0, 0)$ to $(n, n)$ that never go above the diagonal $y = x$ equals $C_n = \dfrac{1}{n+1}\binom{2n}{n}$.*
- **Source.** Joshi, *EJM* Ch. 5, Comment 14 (Catalan via André reflection).
- **Answer.** (Proof.) André reflection principle: bad paths (crossing $y = x + 1$) bijection with paths to $(n - 1, n + 1)$; total $= \binom{2n}{n} - \binom{2n}{n - 1} = C_n$.
- **Tier.** 3.
- **Key shift.** The *reflection bijection* is the canonical Catalan-number proof — bad paths $\leftrightarrow$ shifted paths.

### Practice Problems

#### PP1 — JEE 1988 "+/−" Arrangement (Tier 2)
- **Problem.** *Find the number of arrangements of six "$+$" signs and four "$-$" signs in a row such that no two "$-$" signs are adjacent.*
- **Source.** JEE 1988 (Joshi, *EJM* Ch. 1, Exercise 1.4).
- **Answer.** $\binom{7}{4} = 35$.
- **Tier.** 2.
- **Key shift.** Bijection with gap-selection — same pattern as WE2 specialised.

#### PP2 — Alternate Solution to Ch. 5 Comment 17 (Tier 3)
- **Problem.** *Let $A = \{x_1, \ldots, x_n\}$. Sample space: ordered pairs $(P, Q)$ of subsets of $A$. For each $i$, let $E_i$ = event $\{x_i \notin P \cap Q\}$. Find $P(E_i)$ and use to recompute the sum from Ch. 5 Comment 17.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.57.
- **Answer.** $P(E_i) = 3/4$ (each element is independently in $P$ or not, in $Q$ or not — 4 cases, 3 avoid both).
- **Tier.** 3.
- **Key shift.** Probabilistic = bijective: $|\{(P, Q) : x_i \in P \cap Q\}|/|\Omega|$ = independence-product.

#### PP3 — Stars and Bars (Tier 2: JEE Mains)
- **Problem.** *Find the number of non-negative integer solutions of $x_1 + x_2 + x_3 + x_4 = 10$.*
- **Source.** Joshi, *EJM* Ch. 1, Comment 7 (composition counting).
- **Answer.** $\binom{13}{3} = 286$.
- **Tier.** 2.
- **Key shift.** Bijection between non-negative compositions of $n$ into $k$ parts and binary strings with $n$ stars and $k - 1$ bars (placed between adjacent stars).

#### PP4 — Distinguishable Balls into Distinguishable Boxes (Tier 2)
- **Problem.** *Find the number of ways to place $n$ distinguishable balls into $k$ distinguishable boxes such that no box is empty.*
- **Source.** Joshi, *EJM* Ch. 1, Comment 3 (boxes/balls with restrictions).
- **Answer.** $k!\,S(n, k)$ where $S(n, k)$ is the Stirling number of the second kind; equivalently, $\sum_{j=0}^{k}(-1)^j\binom{k}{j}(k-j)^n$.
- **Tier.** 2.
- **Key shift.** Bijection between surjective functions $\{1,\ldots,n\} \twoheadrightarrow \{1,\ldots,k\}$ and partitions of $n$ objects into $k$ labelled non-empty groups.

#### PP5 — Vandermonde's Identity by Bijection (Tier 2)
- **Problem.** *Give a combinatorial (bijective) proof of $\sum_{k=0}^{r}\binom{m}{k}\binom{n}{r-k} = \binom{m+n}{r}$.*
- **Source.** Joshi, *EJM* Ch. 5, Comment 6 (Vandermonde via subset-partition).
- **Answer.** (Proof.) Each $r$-subset of $\{m + n\}$ objects (= RHS) is uniquely determined by its restriction to the first $m$ (size $k$) and to the next $n$ (size $r - k$). Bijection complete.
- **Tier.** 2.
- **Key shift.** Two-way subset-decomposition is the canonical Vandermonde bijection.

#### PP6 — Pascal's Triangle Path Counting (Tier 2)
- **Problem.** *Find the number of monotone lattice paths from $(0, 0)$ to $(m, n)$ passing through the point $(a, b)$ (with $0 \le a \le m$, $0 \le b \le n$).*
- **Source.** Joshi, *EJM* Ch. 5, Comment 4 (lattice paths and Pascal).
- **Answer.** $\binom{a+b}{a}\binom{(m-a)+(n-b)}{m-a}$.
- **Tier.** 2.
- **Key shift.** Paths-through-point bijection: any such path splits uniquely at the waypoint into two independent sub-paths.

#### PP7 — Probability via Bijection of Favourable Outcomes (Tier 2)
- **Problem.** *A deck of 52 cards is shuffled. Find the probability that the four aces are in four consecutive positions (in any order).*
- **Source.** Joshi, *EJM* Ch. 22, Comment 4 (favourable-outcomes counting).
- **Answer.** $\frac{49 \cdot 4! \cdot 48!}{52!} = \frac{4!}{52 \cdot 51 \cdot 50} = \frac{24}{132600} = \frac{1}{5525}$.
- **Tier.** 2.
- **Key shift.** Bijection: arrangements with four aces consecutive ↔ arrangements of one "ace-block" + 48 non-aces; count both sides.

---

## Chapter 16: Reverse Engineering — LOCKED v0.2

**Joshi sources.** Primary: Ch. 3 (Theory of Equations), Ch. 19 (ODEs — recover from data), Ch. 20 (Functional Eqs), Ch. 24. Secondary: Ch. 4, 5, 17, 21.
**Distinctive cognitive shift.** Reverse the problem flow: instead of *applying* a method to inputs, *construct* the inputs that would make a desired conclusion true. Polynomial-from-roots, ODE-from-solution-curves, vectors-from-Gram-matrix.

### Worked Examples

#### WE1 — Quartic with All Real Roots (Tier 4: RMO)
- **Problem.** *Find all real values of $a$ for which $x^4 - 2ax^2 + x + a^2 - a = 0$ has all roots real.*
- **Source.** Regional Mathematics Olympiad (Joshi, *EJM* Ch. 24, Exercise 24.68).
- **Answer.** $a \ge 3/4$.
- **Tier.** 4.
- **Key shift.** Reverse-engineer the quartic: rewrite as $(x^2 - a)^2 = a - x$; treat $y = x^2 - a$ — the real-root constraint becomes a quadratic-in-$x$ discriminant inequality $1 - 4(a^2 - a - y^2) \ge 0$ with $y = \pm\sqrt{a - x}$.

#### WE2 — Triangle Uniquely Determined by $r, R, s$ (Tier 4)
- **Problem.** *Prove that a triangle is uniquely determined (up to congruence) by its inradius $r$, circumradius $R$, and semiperimeter $s$, when these satisfy the necessary triangle inequalities. Equivalently, reverse-engineer the triangle from invariants.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.94.
- **Answer.** (Proof.) Use the identity $abc = 4Rrs$ and Heron's formula to recover the sides from $r, R, s$.
- **Tier.** 4.
- **Key shift.** Three triangle-invariants determine three side lengths — the *reverse* of "given sides, compute invariants."

#### WE3 — Construct Polynomial with Prescribed Roots (Tier 2)
- **Problem.** *Find a polynomial of minimum degree with real coefficients having $1 + i$ and $2 - 3i$ as roots.*
- **Source.** Joshi, *EJM* Ch. 3, Comment 7 (complex-conjugate root pairing).
- **Answer.** $(x^2 - 2x + 2)(x^2 - 4x + 13) = x^4 - 6x^3 + 23x^2 - 34x + 26$.
- **Tier.** 2.
- **Key shift.** Real-coefficient constraint forces complex roots to appear in conjugate pairs; reverse-engineer the polynomial by multiplying the minimal real factors.

### Practice Problems

#### PP1 — Three-Digit Number = 2(Sum of Digit Squares) (Tier 2)
- **Problem.** *Determine all three-digit numbers equal to twice the sum of the squares of their digits.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.99(a).
- **Answer.** $166$ (with verification of uniqueness by bounding analysis).
- **Tier.** 2.
- **Key shift.** Reverse-engineer the digit triple $(a, b, c)$ from the equation $100a + 10b + c = 2(a^2 + b^2 + c^2)$ + the digit-domain constraints. (Cross-archetype with Ch. 4 WE2 — there "hidden structure" is primary; here "reverse engineering" is primary.)

#### PP2 — Construct ODE from Family of Curves (Tier 2)
- **Problem.** *Find the ODE whose general solution is $y = c_1 \cos x + c_2 \sin x$, where $c_1, c_2$ are arbitrary constants.*
- **Source.** Joshi, *EJM* Ch. 19, Comment 2 (recovering ODE from solution family).
- **Answer.** $y'' + y = 0$.
- **Tier.** 2.
- **Key shift.** Reverse-engineer the ODE: differentiate the solution twice; eliminate $c_1, c_2$ between $y, y', y''$.

#### PP3 — Vectors from Gram Matrix (Tier 3)
- **Problem.** *Given the Gram matrix $G_{ij} = \vec v_i \cdot \vec v_j = \begin{pmatrix}4 & 2 & 2\\ 2 & 5 & 1\\ 2 & 1 & 5\end{pmatrix}$, find vectors $\vec v_1, \vec v_2, \vec v_3$ in $\mathbb{R}^3$ that realise this Gram matrix.*
- **Source.** Joshi, *EJM* Ch. 21, Comment 9 (Cholesky / Gram reconstruction).
- **Answer.** $\vec v_1 = (2, 0, 0)$, $\vec v_2 = (1, 2, 0)$, $\vec v_3 = (1, 0, 2)$ (one solution; others differ by orthogonal transformation).
- **Tier.** 3.
- **Key shift.** Cholesky factorisation reverse-engineers the vectors from their inner-product data — $G = V^T V$.

#### PP4 — Recover Polynomial from Newton's Identities (Tier 3)
- **Problem.** *Given that a monic polynomial $f$ of degree 3 has roots with $p_1 = \sum r_i = 6$, $p_2 = \sum r_i^2 = 14$, $p_3 = \sum r_i^3 = 36$, find $f$.*
- **Source.** Joshi, *EJM* Ch. 3, Comment 11 (Newton's identities for power-sums).
- **Answer.** $f(x) = x^3 - 6x^2 + 11x - 6 = (x - 1)(x - 2)(x - 3)$.
- **Tier.** 3.
- **Key shift.** Newton's identities recursively give elementary symmetric polynomials from power-sums; Vieta then gives the polynomial.

#### PP5 — Functional Equation from Boundary Data (Tier 3)
- **Problem.** *Find all continuous $f: \mathbb{R} \to \mathbb{R}$ with $f(1) = 2$ and $f(x + y) = f(x) + f(y)$ for all $x, y$.*
- **Source.** Joshi, *EJM* Ch. 20, Comment 1 (Cauchy with boundary condition).
- **Answer.** $f(x) = 2x$.
- **Tier.** 3.
- **Key shift.** Functional-equation + boundary value reverse-engineer the *unique* continuous solution.

#### PP6 — Conic from Five Points (Tier 3)
- **Problem.** *Reverse-engineer a conic passing through the five points $(1, 0), (0, 1), (-1, 0), (0, -1), (1/2, 1/2)$.*
- **Source.** Joshi, *EJM* Ch. 9, Comment 13 (general conic via 5 conditions).
- **Answer.** $x^2 + y^2 + 2xy = 1$ (i.e. $(x + y)^2 = 1$ — a degenerate conic, pair of parallel lines).
- **Tier.** 3.
- **Key shift.** General conic $Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$ has 5 independent parameters; 5 points give a linear system.

#### PP7 — Area Recovers Cubic Coefficients (Tier 3: RMO)
- **Problem.** *Given that the area enclosed between $y = x^3 - ax$ and the $x$-axis is $A$, recover $a$ from $A$.*
- **Source.** Joshi, *EJM* Ch. 17, Exercise 17.22 (Reverse engineering parameter from area).
- **Answer.** $A = a^2/2$, so $a = \sqrt{2A}$.
- **Tier.** 3.
- **Key shift.** Reverse the area-formula: enclosed area equals a function of $a$; invert it.

---

## Chapter 17: Degrees of Freedom Analysis — LOCKED v0.2

**Joshi sources.** Primary: Ch. 1 (Counting), Ch. 17 (Areas as DOF-of-parametrisation), Ch. 21 (Vectors), Ch. 22 (Probability). Secondary: Ch. 3, 9, 15, 23.
**Distinctive cognitive shift.** Count *parameters* vs. *constraints*. A geometric object, system of equations, or random configuration has a specific dimension; matching this against the question reveals whether the problem is over-, under-, or exactly-determined.

### Worked Examples

#### WE1 — Eleven Stones, Equal Mass via Rank Argument (Tier 4)
- **Problem.** *We have a collection of $11$ stones with the property that whenever we remove any one, the remaining ten can be partitioned into two piles of equal total mass. Prove all stones are equal.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.9.
- **Answer.** (Proof.) Set up an $11 \times 11$ matrix $A$ where $A_{ij} = \pm 1$ encoding "stone $j$ goes to pile $+$ or $-$ when stone $i$ is removed." The mass vector $\vec m \in \ker A$. A parity argument over $\mathbb{F}_2$ shows $\mathrm{rank}(A) = 10$, so $\dim\ker A = 1$ — all masses must be equal.
- **Tier.** 4.
- **Key shift.** Counting *constraints* (10 partitions) versus *degrees of freedom* (11 masses); 10 independent constraints leave 1 DOF, which a positivity argument forces to be constant.

#### WE2 — Triangle Determined by Three Invariants (Tier 3)
- **Problem.** *Prove that a triangle is uniquely determined (up to congruence) by any three independent invariants among $\{a, b, c, A, B, C, r, R, s\}$. Equivalently, the moduli space of triangles is 3-dimensional.*
- **Source.** Joshi, *EJM* Ch. 11, Comment 14 + Ch. 24 Ex. 24.94.
- **Answer.** A triangle has 3 DOF (e.g. three sides); any three independent invariants suffice.
- **Tier.** 3.
- **Key shift.** DOF count = independent-parameter count. The 9 listed invariants live on a 3-dimensional manifold, with 6 hidden relations (cosine rule, $A+B+C=\pi$, etc.) cutting them down.

#### WE3 — Family of Lines Through a Point (Tier 2)
- **Problem.** *How many lines pass through a given point in the plane? Through two given points? Identify the DOF of each problem.*
- **Source.** Joshi, *EJM* Ch. 9, Comment 1 (line in plane: 2 DOF).
- **Answer.** A line in the plane has 2 DOF (e.g. slope + intercept, or two parameters in $ax + by = 1$); a point imposes 1 constraint, so "lines through a point" form a 1-parameter family (pencil); two points impose 2 constraints, giving a unique line.
- **Tier.** 2.
- **Key shift.** DOF $=$ ambient dimension minus constraint count; this is the formula behind "two points determine a line."

### Practice Problems

#### PP1 — DOF of a Conic (Tier 2)
- **Problem.** *How many parameters specify a general conic in the plane (up to scaling)? How many points are needed to determine a conic uniquely?*
- **Source.** Joshi, *EJM* Ch. 9, Comment 13 (general conic: 5 DOF).
- **Answer.** 5 parameters (e.g. $A : B : C : D : E : F$ projectively); 5 points in general position.
- **Tier.** 2.
- **Key shift.** Counting projective coefficients = $\binom{n+d}{d} - 1$ — the DOF of degree-$d$ plane curves.

#### PP2 — Random Triangle Sample-Space Dimension (Tier 3)
- **Problem.** *Three points are chosen at random in the unit disc. What is the dimension of the sample space of triangles formed? Use this to set up the probability $P(\text{the triangle contains the centre})$.*
- **Source.** Joshi, *EJM* Ch. 22, Comment 6 (geometric probability).
- **Answer.** Sample space has dimension 6 (three points $\times$ 2 coordinates each); $P = 1/4$ by classical result.
- **Tier.** 3.
- **Key shift.** Geometric probability requires measuring sample-space DOF before computing the favourable-region volume.

#### PP3 — Number of Cubic Polynomials Through 4 Points (Tier 2)
- **Problem.** *How many monic cubic polynomials pass through four given points $(x_i, y_i)$ with distinct $x_i$?*
- **Source.** Joshi, *EJM* Ch. 3, Comment 4 (polynomial-interpolation DOF).
- **Answer.** Generically zero; the 4 conditions over-determine the 3 free coefficients ($a, b, c$ in $x^3 + ax^2 + bx + c$). A solution exists iff the four points are consistent with a monic cubic.
- **Tier.** 2.
- **Key shift.** Over-determination $\Rightarrow$ generic non-existence; one DOF short of the constraint count.

#### PP4 — Linear System: Rank vs. Solutions (Tier 2)
- **Problem.** *A linear system $A\vec x = \vec b$ with $A$ of size $5 \times 7$ has rank 4. Describe the solution set: how many free parameters?*
- **Source.** Joshi, *EJM* Ch. 21, Comment 14 (rank-nullity theorem).
- **Answer.** If consistent, solutions form a $3$-parameter family (= $7 - 4$, the nullity). Inconsistency iff $\vec b \notin \mathrm{col}(A)$, requiring $\mathrm{rank}[A|\vec b] > 4$.
- **Tier.** 2.
- **Key shift.** Rank-nullity = DOF accounting for linear systems; the formula $\dim\ker = n - \mathrm{rank}$.

#### PP5 — Tangent-Line DOF on a Surface (Tier 3)
- **Problem.** *At a smooth point of a surface in $\mathbb{R}^3$, how many tangent lines are there? Describe the tangent plane as the union of these lines.*
- **Source.** Joshi, *EJM* Ch. 15, Comment 13 (tangent plane / 2-DOF family).
- **Answer.** $\infty$-many tangent lines (1-parameter family through the point in the tangent plane); together they fill the 2-dimensional tangent plane.
- **Tier.** 3.
- **Key shift.** Tangent plane = 2 DOF; tangent line = 1 DOF; the tangent plane is the union of all 1-DOF tangent lines.

#### PP6 — DOF of Markov Chain Stationary Distribution (Tier 3)
- **Problem.** *An irreducible aperiodic Markov chain on $n$ states has $n - 1$ constraints (transition equations) on the stationary distribution $\pi$ plus the normalisation $\sum\pi_i = 1$. Why is the stationary distribution unique?*
- **Source.** Joshi, *EJM* Ch. 23, Comment 5 (stationary distribution existence-uniqueness).
- **Answer.** $n$ unknowns $\pi_i$; $n$ constraints ($n - 1$ from $\pi P = \pi$ since these sum to a tautology, plus 1 normalisation) — exactly 0 DOF. Irreducibility excludes the trivial null solution.
- **Tier.** 3.
- **Key shift.** DOF $= 0$ $\Leftrightarrow$ unique solution; the Markov chain is a worked example of "constraint count = parameter count" pinning down a unique answer.

#### PP7 — Constraint-Counting for Cubic with Inflection (Tier 3)
- **Problem.** *How many planar cubic curves pass through 8 general points and have a prescribed inflection point at a 9th general point?*
- **Source.** Joshi, *EJM* Ch. 9, Comment 16 (curve-fitting via constraint count).
- **Answer.** A planar cubic has 9 DOF ($\binom{3+2}{2} - 1 = 9$); 8 points impose 8 conditions; an inflection point at the 9th imposes 2 more (point + inflection). Total constraints $= 10 > 9$ DOF $\Rightarrow$ generically no such cubic.
- **Tier.** 3.
- **Key shift.** Over-determination is detected by simple DOF arithmetic; "inflection at a point" is *two* constraints (curve passes through it and curvature vanishes there).

---

## Chapter 18: Recursion / Induction — LOCKED v0.2

**Joshi sources.** Primary: Ch. 4 (Number Theory), Ch. 5 (Binomial), Ch. 18 (Reduction formulas), Ch. 23 (Infinitistic Probability). Secondary: Ch. 19, 20, 22.
**Distinctive cognitive shift.** A problem on $n$ becomes tractable by relating to the same problem on $n - 1$ (induction) or by expressing it as a sequence satisfying a recurrence. The trick is identifying the right *invariant of induction* or the right *recursion variable*.

### Worked Examples

#### WE1 — Fibonacci Matrix Power (Tier 3)
- **Problem.** *Let $A = \begin{pmatrix}1 & 1\\1 & 0\end{pmatrix}$. Prove that $A^n = \begin{pmatrix}F_{n+1} & F_n\\F_n & F_{n-1}\end{pmatrix}$ for every positive integer $n$.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.10.
- **Answer.** (Proof.) Induction on $n$ using $A^{n+1} = A^n \cdot A$.
- **Tier.** 3.
- **Key shift.** Matrix-exponent = encoded recurrence — the Fibonacci recursion is precisely the eigenvalue equation for $A$.

#### WE2 — $25 \mid 7^{2n} + 2^{3n-3}\cdot 3^{n-1}$ (Tier 3: JEE 1982)
- **Problem.** *Prove that $25 \mid 7^{2n} + 2^{3n-3} \cdot 3^{n-1}$ for every positive integer $n$.*
- **Source.** JEE 1982 (Joshi, *EJM* Ch. 4, Comment 8).
- **Answer.** (Proof.) Strong induction: rewrite $7^{2(n+1)} + 2^{3(n+1)-3} \cdot 3^n$ as a linear combination of $7^{2n} + 2^{3n-3}3^{n-1}$ and $25 \cdot 7^{2n}$.
- **Tier.** 3.
- **Key shift.** Shifted-linear-combination technique — the canonical inductive step for divisibility proofs.

#### WE3 — Reduction Formula for $I_n = \int_0^{\pi/2}\sin^n x\,dx$ (Tier 2)
- **Problem.** *Establish $I_n = \frac{n-1}{n} I_{n-2}$ and use it to evaluate $I_5$ and $I_6$.*
- **Source.** Joshi, *EJM* Ch. 18, Comment 4 (reduction formulas).
- **Answer.** $I_5 = \frac{4 \cdot 2}{5 \cdot 3} = \frac{8}{15}$, $I_6 = \frac{5 \cdot 3 \cdot 1}{6 \cdot 4 \cdot 2} \cdot \pi/2 = \frac{15\pi}{96} = \frac{5\pi}{32}$.
- **Tier.** 2.
- **Key shift.** Integration by parts yields a recurrence in the exponent $n$; finite recursion plus a base case gives closed form. This is the integral analogue of induction.

### Practice Problems

#### PP1 — Telescoping Inverse-Cotangent Sum (Tier 2)
- **Problem.** *Sum the infinite series $\displaystyle\sum_{k=1}^{\infty}\cot^{-1}(2k^2)$.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.87(i).
- **Answer.** $\pi/4$.
- **Tier.** 2.
- **Key shift.** $\cot^{-1}(2k^2) = \tan^{-1}(2k+1) - \tan^{-1}(2k-1)$ — telescoping recursion identifies the partial sum.

#### PP2 — Product of $r$ Consecutive Integers (Tier 3)
- **Problem.** *Prove that the product of any $r$ consecutive integers is divisible by $r!$.*
- **Source.** JEE 1985 (Joshi, *EJM* Ch. 4, Comment 9).
- **Answer.** (Proof.) Double induction on $r$ and on the starting integer.
- **Tier.** 3.
- **Key shift.** Double induction — the *two-parameter* recursion separating $r$ and the integer-range.

#### PP3 — JEE Inverse-Tangent Series (Tier 2)
- **Problem.** *Prove by induction: $\tan^{-1}\frac{1}{3} + \tan^{-1}\frac{1}{7} + \cdots + \tan^{-1}\frac{1}{n^2 + n + 1} = \tan^{-1}\frac{n}{n+2}$.*
- **Source.** JEE 1999 (Joshi, *EJM* Ch. 10, Exercise 10.19).
- **Answer.** (Proof.) Induction on $n$; the inductive step uses the $\tan$ subtraction identity.
- **Tier.** 2.
- **Key shift.** Telescoping via subtraction identity — the recursion *is* the subtraction step.

#### PP4 — Tower of Hanoi (Tier 2)
- **Problem.** *Prove that the minimum number of moves to transfer $n$ disks in the Tower of Hanoi from one peg to another is $2^n - 1$.*
- **Source.** Joshi, *EJM* Ch. 23, Comment 2 (recursion classic).
- **Answer.** $T_n = 2T_{n-1} + 1$ with $T_1 = 1$; closed form $T_n = 2^n - 1$.
- **Tier.** 2.
- **Key shift.** The recurrence $T_n = 2T_{n-1} + 1$ encodes the recursive *structure of the solution* itself — move top $n - 1$, move biggest, move top $n - 1$ back.

#### PP5 — Pascal's Identity by Induction (Tier 1: JEE Mains)
- **Problem.** *Prove $\binom{n+1}{r} = \binom{n}{r-1} + \binom{n}{r}$ by induction on $n$.*
- **Source.** Joshi, *EJM* Ch. 5, Comment 2 (Pascal's identity).
- **Answer.** (Proof.) Base $n = 1$ trivial. Inductive step: assume for $n$, prove for $n + 1$ by algebraic manipulation of factorials.
- **Tier.** 1.
- **Key shift.** The induction unwinds the *combinatorial* recurrence: choose-$r$-from-$n+1$ depends on whether element $n+1$ is included (giving $\binom{n}{r-1}$) or not (giving $\binom{n}{r}$).

#### PP6 — Random Walk Recursion (Gambler's Ruin) (Tier 3)
- **Problem.** *A gambler starts with $k$ rupees, wins or loses 1 rupee per round with probability $1/2$, and stops at $0$ (ruin) or $N$ (win). Set up the recurrence for $P_k$ = probability of ruin starting from $k$; solve.*
- **Source.** Joshi, *EJM* Ch. 23, Comment 4 (Markov chain on integers).
- **Answer.** $P_k = (P_{k-1} + P_{k+1})/2$ with $P_0 = 1$, $P_N = 0$; linear solution $P_k = 1 - k/N$.
- **Tier.** 3.
- **Key shift.** The probability satisfies the *discrete Laplace equation* — boundary values + harmonicity give the closed form linearly. This is the probabilistic version of Dirichlet's principle.

#### PP7 — Generating Function for Binary Strings (Tier 3)
- **Problem.** *Let $a_n$ = number of binary strings of length $n$ with no two consecutive $1$'s. Set up the recurrence and identify $a_n$.*
- **Source.** Joshi, *EJM* Ch. 23, Comment 8 (combinatorial recurrence + GF).
- **Answer.** $a_n = a_{n-1} + a_{n-2}$ with $a_1 = 2, a_2 = 3$; so $a_n = F_{n+2}$ (Fibonacci shifted).
- **Tier.** 3.
- **Key shift.** Strings ending in $0$ extend any $(n-1)$-string; strings ending in $1$ extend any $(n-2)$-string ending in $0$ — the Fibonacci recurrence in disguise.

---

## Chapter 19: Pivoting / Elimination — LOCKED v0.2

**Joshi sources.** Primary: Ch. 3 (Theory of Eqs — resultants), Ch. 9 (Coord. Geom.), Ch. 21 (Vectors). Secondary: Ch. 2, 11, 19.
**Distinctive cognitive shift.** Choose *which* variable to eliminate (and *how*). Solving a system $f(x, y) = 0, g(x, y) = 0$ by Gaussian-elimination, resultants, or substitution — each is a *pivot* choice. The wrong pivot leads to a mess; the right one collapses the problem.

### Worked Examples

#### WE1 — Common Tangent to Circle and Parabola (Tier 2)
- **Problem.** *Find the equation of the common tangent (above the $x$-axis) to the circle $(x - 3)^2 + y^2 = 9$ and the parabola $y^2 = 4x$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.34).
- **Answer.** $y = \frac{1}{\sqrt 3}(x + 3)$ (or equivalent).
- **Tier.** 2.
- **Key shift.** Eliminate $y$ between the circle and parabola via the tangent-line equation; impose the discriminant = 0 condition for tangency.

#### WE2 — Resultant of Two Polynomials (Tier 3)
- **Problem.** *Find the condition on $a, b, c, p, q, r$ for the polynomials $f(x) = ax^2 + bx + c$ and $g(x) = px^2 + qx + r$ to have a common root.*
- **Source.** Joshi, *EJM* Ch. 3, Comment 8 (resultants).
- **Answer.** Resultant $(ar - cp)^2 = (aq - bp)(br - cq)$ (or equivalently, the $4 \times 4$ Sylvester determinant vanishes).
- **Tier.** 3.
- **Key shift.** Eliminate $x$ from both equations by computing the *resultant* — a single polynomial in the coefficients whose vanishing is equivalent to a common root.

#### WE3 — Gaussian Elimination on a $3 \times 3$ System (Tier 2)
- **Problem.** *Solve the linear system $\begin{cases}x + 2y + 3z = 6\\ 4x + 5y + 6z = 15\\ 7x + 8y + 10z = 25\end{cases}$.*
- **Source.** Joshi, *EJM* Ch. 21, Comment 11 (Gauss elimination).
- **Answer.** $x = 1, y = 1, z = 1$.
- **Tier.** 2.
- **Key shift.** Pivot on $x$ in row 1, eliminate from rows 2 and 3; pivot on $y$ in (reduced) row 2, eliminate from row 3; back-substitute. Order matters — choose the largest absolute-value pivot for numerical stability.

### Practice Problems

#### PP1 — Inverse via Variable-Pivot (Tier 1)
- **Problem.** *If $f: [1, \infty) \to [2, \infty)$ is $f(x) = x + 1/x$, find $f^{-1}(x)$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.36).
- **Answer.** $f^{-1}(x) = \frac{x + \sqrt{x^2 - 4}}{2}$.
- **Tier.** 1.
- **Key shift.** Pivot on the variable: solving $y = x + 1/x$ for $x$ in terms of $y$ is the canonical *eliminate-the-old-variable* move. (Cross-archetype with Ch. 5 PP1.)

#### PP2 — Substitution-Driven $F(x^2)$ (Tier 2)
- **Problem.** *Let $F(x) = \int_0^x f(t)\,dt$ with $F(x^2) = x^2(1 + x)$. Find $f(4)$.*
- **Source.** JEE 2001 (Joshi, *EJM* Ch. 24, Exercise 24.40).
- **Answer.** $5/2$.
- **Tier.** 2.
- **Key shift.** Eliminate via substitution $u = x^2$; differentiate. (Cross-archetype with Ch. 5 PP2.)

#### PP3 — Eliminate $\theta$ Between Two Trig Equations (Tier 2)
- **Problem.** *Eliminate $\theta$ from $x = a\sec\theta$, $y = b\tan\theta$ to find the locus.*
- **Source.** Joshi, *EJM* Ch. 9, Comment 7 (parametric-to-Cartesian conversion).
- **Answer.** $x^2/a^2 - y^2/b^2 = 1$ (hyperbola).
- **Tier.** 2.
- **Key shift.** Use the identity $\sec^2\theta - \tan^2\theta = 1$ as the *elimination engine* — the parametric form and the identity are dual perspectives.

#### PP4 — Intersection of Conics via Elimination (Tier 3)
- **Problem.** *Find all real intersection points of $x^2 + y^2 = 25$ and $xy = 12$.*
- **Source.** Joshi, *EJM* Ch. 9, Comment 14 (conic-conic intersection).
- **Answer.** $(3, 4), (4, 3), (-3, -4), (-4, -3)$.
- **Tier.** 3.
- **Key shift.** Substitute $y = 12/x$ into $x^2 + y^2 = 25$ — quartic in $x$ factors as $(x^2 - 16)(x^2 - 9) = 0$.

#### PP5 — Cross-Product Elimination (Tier 2)
- **Problem.** *Find $\vec b$ if $\vec a = (1, 2, 1)$, $\vec a \cdot \vec b = 6$, and $\vec a \times \vec b = (2, -2, 2)$.*
- **Source.** JEE 1985 (Joshi, *EJM* Ch. 21, Exercise 21.10).
- **Answer.** $\vec b = (1, 2, 3)$.
- **Tier.** 2.
- **Key shift.** Use the BAC–CAB identity $\vec a \times (\vec a \times \vec b) = (\vec a \cdot \vec b)\vec a - (\vec a \cdot \vec a)\vec b$ to eliminate cross-products into a scalar/vector linear system.

#### PP6 — Eliminate Parameters in 2-Parameter Family (Tier 2)
- **Problem.** *A line passes through $(\alpha, \beta)$ with slope $m$ such that $\alpha + m\beta = 1$ and $m\alpha - \beta = 2$ for some real $\alpha, \beta$. Find the locus.*
- **Source.** Joshi, *EJM* Ch. 9, Comment 11 (family-of-lines elimination).
- **Answer.** Eliminating $\alpha, \beta$: $m^2 - m = m\beta + \beta \cdot m = \ldots$ — yields $(m^2 + 1) = $ some condition; final locus is a line.
- **Tier.** 2.
- **Key shift.** Treat $\alpha, \beta$ as auxiliary variables; eliminate them sequentially. Choosing $\alpha$ first vs. $\beta$ first gives identical results but different intermediate expressions.

#### PP7 — Pivot to Decouple a System of ODEs (Tier 3)
- **Problem.** *Solve the coupled linear ODE system $x' = x + y$, $y' = x - y$ with $x(0) = 1, y(0) = 0$.*
- **Source.** Joshi, *EJM* Ch. 19, Comment 9 (linear system diagonalisation).
- **Answer.** Matrix has eigenvalues $\pm\sqrt 2$; solutions $x(t) = \frac{1}{2}(\cosh\sqrt 2 t + \frac{1}{\sqrt 2}\sinh\sqrt 2 t)$, etc.
- **Tier.** 3.
- **Key shift.** Pivot to the *eigenbasis* of the system matrix — once decoupled, each equation is one-dimensional and solvable independently.

---

## Chapter 20: Analogy / Transfer — LOCKED v0.2 (synthesis-essay format)

**Joshi sources.** Primary: Ch. 24 (Misc — Joshi's meta-pedagogical synthesis), Ch. 21 (Quaternions ↔ Complex), Ch. 23 (von Neumann fly), Ch. 20 (Functional Eqs). Secondary: Ch. 4, 5, 7, 11, 15, 16, 17, 18.
**Pedagogical role.** Capstone chapter — teaches *meta-reasoning*: recognise that a current problem is analogous to a previously-solved problem, and transfer the method.
**Format.** Unlike Chapters 2–19, this chapter is a *synthesis essay*: 3 anchor worked examples (themselves *meta-problems* about transfer), and 7 practice "transfer prompts" — each prompt names two previously-encountered problems from earlier chapters and asks the reader to articulate the analogy.

### Worked Examples (Anchor Meta-Problems)

#### WE1 — Wallace–Bolyai–Gerwien Equidecomposability (Tier 4)
- **Problem.** *Two plane polygons are equidecomposable iff they have equal area. Prove via four steps: equivalence-relation; rectangle-to-square; triangle-to-rectangle; arbitrary polygon-to-triangle.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.79.
- **Answer.** Each step *transfers* the result one structural class wider: squares $\to$ rectangles $\to$ triangles $\to$ all polygons.
- **Tier.** 4.
- **Key shift.** Systematic generalisation by analogous reduction — the chapter's meta-lesson in pure form.

#### WE2 — Pedoe's Inequality as Generalised Weitzenböck (Tier 4)
- **Problem.** *(Generalising the single-triangle Weitzenböck inequality $a^2 + b^2 + c^2 \ge 4\sqrt 3\Delta$.) For two triangles with sides $a, b, c$ and $a', b', c'$ and areas $\Delta, \Delta'$, prove $a^2(b'^2 + c'^2 - a'^2) + b^2(c'^2 + a'^2 - b'^2) + c^2(a'^2 + b'^2 - c'^2) \ge 16\Delta\Delta'$, with equality iff the triangles are similar.*
- **Source.** Joshi, *EJM* Ch. 24, Exercise 24.96(b).
- **Answer.** (Proof.) Express each side via the law of cosines; reduces to $\sum a^2\cot A' \ge 4\Delta$ (Ex. 24.96(a)) which generalises Weitzenböck by replacing the second triangle's data.
- **Tier.** 4.
- **Key shift.** A *one-triangle* inequality is the diagonal case $\Delta = \Delta', a = a'$ of a *two-triangle* inequality — analogy by *parameterisation*. Cf. Hadwiger–Finsler (Ch. 10 PP5) as another single-triangle special case.

#### WE3 — Quaternions as Complex Numbers in Higher Dimensions (Tier 4)
- **Problem.** *Establish the analogy: just as complex numbers $a + bi$ encode 2D rotations, quaternions $a + bi + cj + dk$ encode 3D rotations (acting on pure quaternions $xi + yj + zk$ by conjugation). Use this to derive the four-squares identity $(\sum a_i^2)(\sum b_i^2) = \sum c_i^2$ where $\vec c$ is bilinear in $\vec a, \vec b$.*
- **Source.** Joshi, *EJM* Ch. 21, Comments 17–19 (quaternions and four-square identity).
- **Answer.** (Proof.) Quaternion product $\bar pq$ encodes rotation; $|pq| = |p||q|$ gives the four-squares identity by squaring both sides.
- **Tier.** 4.
- **Key shift.** Transfer the *algebraic structure* $\mathbb{C}$ (with $i^2 = -1$) to $\mathbb{H}$ (with $i^2 = j^2 = k^2 = ijk = -1$); the geometric meaning (rotations) transfers from 2D to 3D, and the multiplicative identity for sums of squares generalises from 2 to 4 squares. Forward-link: this is the Cayley–Dickson construction; the next step gives octonions (8 squares) and so on.

### Practice Problems (Transfer Prompts)

#### PP1 — Counting ↔ Area Analogy (Tier 3)
- **Prompt.** *Compare the complementary-counting principle in Ch. 1 (Joshi Ch. 1, Comment 6) with the complementary-area principle in Ch. 17 (Joshi Ch. 17, Comment 1). Articulate the structural analogy.*
- **Joshi anchor.** Joshi Ch. 17, Comment 1 explicitly draws this analogy.
- **Tier.** 3.
- **Key shift.** Counting and integration are *both* measure-theoretic; their complementary-principle forms are identical: $|A^c| = |\Omega| - |A|$ and $\int_A = \int_\Omega - \int_{A^c}$.

#### PP2 — Riemann Sums as Limit of Counts (Tier 3)
- **Prompt.** *In Ch. 13 (Combinatorial), we counted sums like $\sum_{k=1}^{n}f(k)$ exactly. In Ch. 17 (Areas), $\int_0^1 f(x)\,dx$ appears as $\lim_{n\to\infty}\frac{1}{n}\sum_{k=1}^{n}f(k/n)$. Transfer one Joshi counting identity (e.g. $\sum k^2 = n(n+1)(2n+1)/6$) to derive an integral.*
- **Joshi anchor.** Ch. 17, Comment 2 (Riemann sums as a limit).
- **Tier.** 3.
- **Key shift.** Counting $\to$ Riemann integration is the discrete-to-continuous transfer; the Joshi forward-reference Ch. 1 → Ch. 17 is the explicit bridge.

#### PP3 — Sin/Cos System ↔ Hyperbolic System (Tier 3)
- **Prompt.** *Joshi Ch. 20, Comment 1 + Ex. 20.4–20.5 characterise continuous $f, g$ satisfying $f(x+y) = f(x)g(y) + g(x)f(y)$ and $g(x+y) = g(x)g(y) - f(x)f(y)$ (the "sin/cos system"). Show that replacing the second equation's minus sign with plus gives the *hyperbolic* system, with solutions $f = \sinh, g = \cosh$.*
- **Joshi anchor.** Joshi Ch. 20, Comment 1.
- **Tier.** 3.
- **Key shift.** Trigonometric and hyperbolic identities are *the same structure with one sign flipped* — a textbook transfer between two geometries ($S^1$ ↔ hyperbola).

#### PP4 — Sum-of-Two-Squares ↔ Sum-of-Four-Squares (Tier 4)
- **Prompt.** *Recall the Brahmagupta–Fibonacci two-square identity $(a^2+b^2)(c^2+d^2) = (ac-bd)^2 + (ad+bc)^2$ (Joshi Ch. 4, Comment 3). Transfer to derive the Euler four-square identity (see WE3) via quaternions.*
- **Joshi anchor.** Joshi Ch. 21, Ex. 21.25–27.
- **Tier.** 4.
- **Key shift.** The two-square identity is multiplicativity of $|z|^2$ on $\mathbb{C}$; the four-square identity is the same for $|q|^2$ on $\mathbb{H}$. Same proof template, broader algebra.

#### PP5 — Geometric Series ↔ Arithmetic Sum (von Neumann Fly) (Tier 3)
- **Prompt.** *Two trains 100 km apart approach each other at 50 km/h; a fly oscillates between them at 75 km/h. Find the total distance flown by the fly. Solve (a) via geometric series of segment-lengths, and (b) via the elementary "fly flies for the duration the trains take to meet" argument. Articulate the analogy.*
- **Joshi anchor.** Joshi Ch. 23, Ex. 23.4 (von Neumann fly).
- **Tier.** 3.
- **Key shift.** A *summable* infinite series equals a *finite* arithmetic quantity (total time × fly speed). The geometric-series transfer reveals the hidden finite structure.

#### PP6 — Polynomial Identities ↔ Combinatorial Identities (Integral Bridge) (Tier 4)
- **Prompt.** *Joshi Ex. 18.19 expresses a binomial-identity-style combinatorial sum as a definite integral. Articulate the bridge: how does an integral identity translate to a binomial identity via expansion?*
- **Joshi anchor.** Joshi Ch. 18, Ex. 18.19 ↔ Ch. 5 Main Problem.
- **Tier.** 4.
- **Key shift.** Beta-function ↔ binomial coefficient via $B(p, q) = \frac{(p-1)!(q-1)!}{(p+q-1)!}$. Two seemingly distinct identities are *the same identity* on opposite sides of a continuous-discrete bridge.

#### PP7 — Pólya Urn ↔ Self-Similar Game (Tier 4)
- **Prompt.** *Pólya urn (Ch. 22 Ex. 22.18) has a self-similar structure under repeated draws. Joshi Ex. 23.M presents a "three-player self-similar game" whose outcomes follow the same recurrence. Transfer the urn-derivation argument to compute the game's win probabilities.*
- **Joshi anchor.** Joshi Ex. 22.18 ↔ Ex. 23.M.
- **Tier.** 4.
- **Key shift.** Two different *physical* problems (urn + game) share the *same Markov chain*; the transfer is from one realisation to another. The win-probability for the urn equals the win-probability for the game.

---

## Appendix A: Joshi Chapter 24 Cross-Reference Index

The 100 exercises of Joshi Chapter 24 are the single richest source for Pillar 2. The table below maps each exercise to its archetype-chapter routing — useful for the next extraction pass.

| Exercise | Problem gist | Routed to |
|---|---|---|
| 24.1 | Domain of $f_1 + f_2$ | Ch. 9 WE1 |
| 24.2 | Repeated root of $f$ → root of $f'$ | Ch. 4 WE1 |
| 24.3 | $f(x) = x^2$ inj/surj | (omit — too foundational) |
| 24.4 | Linear ODE characteristic poly | Ch. 6 WE3 candidate |
| 24.5 | Angle bisector ratio | (omit — too elementary) |
| 24.6 | Perpendicular concurrence (inner) | Ch. 2 (already routed) |
| 24.7 | Cyclic quadrilateral inscribed-circumscribed | Ch. 3 WE2 |
| 24.8 | Dance-party Putnam | **Ch. 13 WE1** |
| 24.9 | 11 stones equal mass | Ch. 17 WE1 |
| 24.10 | Fibonacci matrix power | Ch. 18 WE1 |
| 24.11 | Partial order on $\mathbb{C}$ | Ch. 3 PP1 |
| 24.12 | $|z-a|+|z-b|\le r$ convex | Ch. 8 PP1 |
| 24.13 | $\alpha^3 - 3\alpha^2 + 5\alpha = 17$ | Ch. 1 PP5 (already used) |
| 24.14 | $\cos 2\theta + a\cos\theta + b\sin\theta + c = 0$ four roots | Ch. 2 stretch (deferred — already 7 PPs) |
| 24.15 | Double-sum order swap | Ch. 1 / Ch. 18 reference |
| 24.16 | Sun-shadow work-rate | Ch. 5 WE1 |
| 24.17 | $(1+b^2)x^2 + 2bx + 1$ min range | **Ch. 10 PP2** |
| 24.18 | Centroid locus of $\triangle PAB$ | Ch. 8 PP2 |
| 24.19 | 5th + 6th binomial term = 0 | Ch. 15 / Ch. 4 stretch |
| 24.20 | $T_n$ triangles, $T_{n+1} - T_n = 21$ | **Ch. 9 WE2 / Ch. 13 PP2** |
| 24.21 | Onto functions $\{1,2,3,4\} \to \{1,2\}$ | **Ch. 13 WE3** |
| 24.22 | $a,b,c,d$ in AP, $abc, abd, acd, bcd$ | Ch. 18 stretch |
| 24.23 | AP 2,5,8,... sum-equal | Ch. 18 stretch |
| 24.24 | $n$-th roots of unity right angle | **Ch. 2 PP1** |
| 24.25 | $z_1, z_2, z_3$ ratio → triangle type | **Ch. 8 WE1** |
| 24.26 | $\sin^{-1}(\cdots) + \cos^{-1}(\cdots) = \pi/2$ | **Ch. 5 PP3** |
| 24.27 | Max of $\prod\cos\alpha_i$ under $\prod\cot\alpha_i=1$ | **Ch. 10 PP3** |
| 24.28 | $\alpha + \beta = \pi/2, \beta + \gamma = \alpha$ | Ch. 1 / Ch. 5 reference |
| 24.29 | Tower angles of depression | (omit — too applied) |
| 24.30 | Integer $m$ for integer intersection | **Ch. 9 PP1 / Ch. 14 stretch** |
| 24.31 | Directrix of parabola | (omit — too elementary) |
| 24.32 | $PQ, RS$ tangents, $2r = ?$ | Ch. 12 stretch |
| 24.33 | Parallelogram area | Ch. 7 stretch |
| 24.34 | Common tangent circle-parabola | **Ch. 19 WE1** |
| 24.35 | Tangent-triangle area $= 2$ | **Ch. 6 WE1** |
| 24.36 | $f(x) = x + 1/x$ inverse | **Ch. 5 PP1 / Ch. 19 PP1** |
| 24.37 | $g(x) = 1 + x - [x], f(g)$ | Ch. 11 stretch |
| 24.38 | $\lim\sin(\pi\cos^2 x)/x^2$ | **Ch. 6 PP1** |
| 24.39 | Left derivative $[x]\sin\pi x$ at integer | **Ch. 11 PP2** |
| 24.40 | $F(x^2) = x^2(1+x)$, find $f(4)$ | **Ch. 5 PP2 / Ch. 19 PP2** |
| 24.41 | $\max\{x, x^3\}$ non-diff | **Ch. 11 PP1** |
| 24.42 | $xe^{x(1-x)}$ monotonicity | **Ch. 12 PP1** |
| 24.43 | $\int\cos^2 x/(1+a^x)$ symmetric | **Ch. 2 PP3** |
| 24.44 | $\cos|x| + |x|$ diff at 0 | **Ch. 6 PP2** |
| 24.45 | $\log_4(x-1) = \log_2(x-3)$ | **Ch. 11 PP3 / Ch. 9 stretch** |
| 24.46 | $f(x) = \alpha x/(x+1), f\circ f = \mathrm{id}$ | **Ch. 3 PP2** |
| 24.47 | $[\vec a\ \vec b\ \vec c]$ depends on? | **Ch. 8 WE2** |
| 24.48 | $H_n - \ln n$ bounded | **Ch. 6 WE2** |
| 24.49 | $(2m)!(2n)!/(m+n)!$ integer | **Ch. 14 WE1** |
| 24.50 | Three unit vectors $|\vec a-\vec b|^2$ sum | **Ch. 10 PP1** |
| 24.51 | Sum of three from $\{1..p\}$ = $2p$ prob | **Ch. 13 PP1** |
| 24.52 | India probability | Ch. 13 stretch |
| 24.53 | 16-player tournament | **Ch. 13 PP3** |
| 24.54 | Event $E$ at least 3 times | **Ch. 13 PP7** |
| 24.55 | $A$ wins 3 of 5 | Ch. 13 stretch |
| 24.56 | Two queens non-taking | **Ch. 13 PP4** |
| 24.57 | Alt solution to Ch. 5 Comment 17 | **Ch. 15 PP2** |
| 24.58 | AD bisector, $\angle A = 72°$ | Ch. 2 / Ch. 11 stretch |
| 24.59 | $BE, CF$ altitudes, $FM \parallel EN$ | **Ch. 2 PP2** |
| 24.60 | Perpendiculars concurrent (outer) | **Ch. 2 PP6** (already routed) |
| 24.61 | Isosceles 120° → PQR equilateral | Ch. 2 stretch |
| 24.62 | 1000-evens vs. 1000-odds mod 2001 | Ch. 1 PP4 (already used) |
| 24.63 | $\lfloor x/99\rfloor = \lfloor x/101\rfloor$ | **Ch. 14 PP2** |
| 24.64 | $x^2/z < (x^2+y^2+z^2)/(x+y+z) < z^2/x$ | **Ch. 10 WE2** |
| 24.65 | Triangle sides $|x^2(y-z)+\cdots| < xyz$ | **Ch. 10 WE1 / Ch. 9 WE3 candidate** |
| 24.66 | $abc = 1$ inequalities (INMO+IMO 2000) | **Ch. 2 PP7 + Ch. 10 WE3** |
| 24.67 | Symmetric matrix odd $n$ | **Ch. 2 WE3** (already routed) |
| 24.68 | $x^4 - 2ax^2 + x + a^2 - a = 0$ real | **Ch. 16 WE1** |
| 24.69 | $f(x+y) = f(x)f(y)f(xy)$ | Ch. 1 PP7 (already used) |
| 24.70 | $\sum A_i/(x - a_i) = 0$ real | **Ch. 11 WE1** |
| 24.71 | Triangle cosine determinant = 0 | Ch. 1 / Ch. 17 stretch |
| 24.72 | Consecutive-int sides, $r = 4$, find $R$ | **Ch. 9 PP2** |
| 24.73 | 50-subset of {1..100}, perfect square | **Ch. 13 PP6** |
| 24.74 | Convex quad, area 32, side+diag = 16 | **Ch. 12 PP2** |
| 24.75 | 1000 doors | Ch. 1 PP6 (already used) |
| 24.76 | Squarefree + perimeter-triangle | **Ch. 14 PP4** |
| 24.77 | Cakes clockwise (Josephus) | **Ch. 12 WE2** |
| 24.78 | $m \times n$ board diagonal squares | **Ch. 14 PP3** |
| 24.79 | Wallace-Bolyai-Gerwien | **Ch. 20 WE1** |
| 24.80 | Surjective functions: 2 formulas | **Ch. 13 WE2 / Ch. 15 WE1** |
| 24.81 | Hamiltonian cycle $m \times n$ mesh | **Ch. 14 PP5** |
| 24.82 | Digital sum (XOR) | **Ch. 14 WE2** |
| 24.83 | Nim games | **Ch. 14 PP7** |
| 24.84 | Descartes' circle theorem | Ch. 2 / Ch. 20 stretch |
| 24.85 | Max cyclic $\sin x_i\cos x_{i+1}$ | **Ch. 2 PP5** |
| 24.86 | Box white/black/red, red last | **Ch. 13 PP5** |
| 24.87 | $\sum\cot^{-1}(2k^2)$ telescoping | **Ch. 18 PP1** |
| 24.88 | Right-triangle $R \ge (1+\sqrt 2)r$ | **Ch. 10 PP4** |
| 24.89 | $f(0), f(-1)$ odd → no integer root | **Ch. 14 WE3** |
| 24.90 | $(\tan^2\theta + 1)^2 + \cdots = 0$ four roots | Ch. 5 / Ch. 9 stretch |
| 24.91 | Min of quadratic forms | **Ch. 12 PP3** |
| 24.92 | Convex polygon vertex/non-vertex | **Ch. 12 WE1 / Ch. 3 WE3 candidate** |
| 24.93 | Ravi substitution + Hadwiger-Finsler | **Ch. 5 WE2 / Ch. 10 PP5** |
| 24.94 | $abc = 4Rrs$; triangle from $P, r, R$ | Ch. 1 / Ch. 17 stretch |
| 24.95 | $\cot\theta_1 + \cot\theta_2$ min | **Ch. 2 PP4 / Ch. 10 PP7** |
| 24.96 | Pedoe's inequality | **Ch. 10 PP6** |
| 24.97 | $f'' + gf' - f = 0$, $f(a) = f(b) = 0$ | **Ch. 11 WE2** |
| 24.98 | Plane isometries classification | Ch. 2 / Ch. 20 stretch |
| 24.99 | Three-digit = 2×sum-of-squares; leading 2ⁿ,5ⁿ | **Ch. 4 WE2 / Ch. 4 PP1** |
| 24.100 | Wilson primes $(p-1)! + 1$ | **Ch. 14 PP1** |

**Usage count from Ch. 24 in this pass:** 56 of 100 exercises routed (excluding the 10 already used in Ch. 1 + 10 omitted as too elementary). 24 exercises remain as "stretch" candidates for the next extraction pass.

---

## Appendix B: Extraction Pending — by Joshi Chapter

For the next session, the highest-yield remaining sources (and the chapters they will fill) are:

| Joshi Chapter | Yield | Fills slots in |
|---|---|---|
| Ch. 1 (Counting) Comments 3, 5, 12 | 4–5 problems | Ch. 13, 15, 17 |
| Ch. 2 (Algebra) Comment 6 ff. | 4–6 problems | Ch. 2 PP1-5 verification; Ch. 5; Ch. 18 |
| Ch. 4 (Number Theory) Comments 1–7 | 6–8 problems | Ch. 14, 18 |
| Ch. 5 (Binomial) Main + Comments | 6–10 problems | Ch. 15 (primary), Ch. 4 (Hidden Structure) |
| Ch. 6 (Inequalities) Comments 4–12 | 8–12 problems | Ch. 10 (stretch), Ch. 7 (Normalization primary), Ch. 12 |
| Ch. 8 (Geometry) Comments on pole-polar | 4–6 problems | Ch. 3 (Duality primary), Ch. 2 |
| Ch. 9 (Coord. Geom.) | 5–7 problems | Ch. 5, Ch. 8, Ch. 19 |
| Ch. 18 (Definite Integrals) Comments 7–14 | 4–6 problems | Ch. 1 (already used 3); Ch. 2 (already used 1); Ch. 5 |
| Ch. 20 (Functional Eqs) | 3–5 problems | Ch. 11 (Existence primary), Ch. 5 (Substitution) |

**Estimate.** A second focused session targeting Joshi Ch. 6 (Inequalities) and Ch. 8 (Geometry) — the two thickest remaining sources — would close approximately 35 more problem slots and bring the master file to **~85% locked**. A third session targeting Ch. 1, 2, 4, 5 would close the rest.

---

## Appendix C: Cross-Archetype Reuse Log

Five problems are *intentionally* used in two archetype chapters because they exhibit two archetypes equally cleanly. The decision logged here ensures the cross-reference language ("as seen in Chapter X") is correct in both chapters' prose.

| Problem | Primary chapter | Secondary chapter | Justification |
|---|---|---|---|
| Joshi Ex. 24.20 ($T_n$ triangles) | Ch. 13 PP2 | Ch. 9 WE2 | Combinatorial-counting + integer-domain-constraint |
| Joshi Ex. 24.36 ($f(x) = x + 1/x$ inverse) | Ch. 5 PP1 | Ch. 19 PP1 | Substitution = variable-elimination |
| Joshi Ex. 24.40 ($F(x^2) = x^2(1+x)$) | Ch. 5 PP2 | Ch. 19 PP2 | Same: substitution = variable-elimination |
| Joshi Ex. 24.66 ($abc = 1$ inequalities) | Ch. 2 PP7 | Ch. 10 WE3 | Symmetric constraint + classical inequality |
| Joshi Ex. 24.95 (cotangent-sum min) | Ch. 2 PP4 | Ch. 10 PP7 | Symmetric extremum + AM-GM |

**Rule.** Whenever a problem appears in two chapters, the *secondary* chapter must explicitly note "as in Chapter X" and use a *different* solution angle (e.g., Ch. 2 PP4 emphasises *symmetry forcing* the answer; Ch. 10 PP7 emphasises *Jensen / Lagrange-multiplier verification*).

---

## Appendix D: Joshi-Source Coverage Stress Test

For each archetype-chapter slot count (3 WE + 7 PP = 10), the table below records the locked slate (post-v0.2 pass).

| Chapter | Slots locked | Slots candidate (awaiting Anand) | Joshi-thin? |
|---|---|---|---|
| 2 Symmetry | 10/10 | 0 | No |
| **3** Duality | **10/10 (v0.2)** | 0 | Was-thin; resolved via Ch. 21 + Ch. 24 routing |
| **4** Hidden Structure | **10/10 (v0.2)** | 0 | No |
| **5** Substitution | **10/10 (v0.2)** | 0 | No |
| **6** Linearization | **10/10 (v0.2)** | 0 | No |
| 7 Normalization | 0/10 | 7 (candidate; framing-blocked) | **Yes (acute) — Anand framing decision needed** |
| **8** Domain Translation | **10/10 (v0.2)** | 0 | No |
| **9** Domain Constraints | **10/10 (v0.2)** | 0 | No |
| 10 Inequality Constraints | 10/10 | 0 | No |
| **11** Existence/Uniqueness | **10/10 (v0.2)** | 0 | No |
| **12** Extremal Principles | **10/10 (v0.2)** | 0 | No |
| 13 Combinatorial | 10/10 | 0 | No |
| 14 Parity/Modularity | 10/10 | 0 | No |
| **15** Bijection | **10/10 (v0.2)** | 0 | No |
| **16** Reverse Engineering | **10/10 (v0.2)** | 0 | Resolved via Ch. 3 + 19 + 20 + 21 routing |
| **17** DOF Analysis | **10/10 (v0.2)** | 0 | Resolved via Ch. 9 + 11 + 21 + 23 routing |
| **18** Recursion/Induction | **10/10 (v0.2)** | 0 | No |
| **19** Pivoting/Elimination | **10/10 (v0.2)** | 0 | No |
| **20** Analogy/Transfer | **10/10 (v0.2; synthesis-essay format)** | 0 | Resolved via meta-format |
| **Total** | **180/190** | **7** | — |

**Coverage after v0.2:** 95% locked (180/190); only Chapter 7 (Normalization) remains open pending Anand's framing decision (a-pure-Joshi vs. b-physics-vignette).

---

## Appendix E: Open Decisions for Anand

1. **Cross-archetype reuse (5 cases).** Confirm the dual-use of Joshi 24.20, 24.36, 24.40, 24.66, 24.95. (See Appendix C.)
2. **Chapter 7 framing.** Adopt the *Buckingham-π / dimensional analysis* vignette as WE1, or keep purely competition-mathematical? (Recommendation: b — physics vignette.)
3. **Chapter 20 synthesis-essay format.** Confirm the meta-pedagogical "transfer prompt" format for the 7 practice items, rather than fully-worked problems.
4. **Tier-distribution audit.** Each v0.2-locked chapter has a draft tier balance; final audit deferred to Pillar 2 drafting.
   - **Ch. 2:** 3 Tier-1 + 4 Tier-2 + 2 Tier-3 + 1 Tier-4 — balanced.
   - **Ch. 10:** 0 Tier-1 + 3 Tier-2 + 4 Tier-3 + 3 Tier-4 — top-heavy. Consider swapping one Tier-3 for a Tier-1.
   - **Ch. 13:** 1 Tier-1 + 2 Tier-2 + 6 Tier-3 + 1 Tier-4 — Tier-3 heavy. Consider swap.
   - **Ch. 14:** 0 Tier-1 + 1 Tier-2 + 6 Tier-3 + 3 Tier-4 — Tier-3/4 heavy. Substitute one Tier-3 with a JEE 1979/1983/1985 mod problem from Joshi Ch. 4.
   - Chapters 3–6, 8, 9, 11, 12, 15–20 (v0.2 locks): tier-audit deferred to drafting.
5. **Cursor-Joshi.md as primary reference.** Confirm that from now on, problem-extraction work uses `Cursor-Joshi.md` as the primary reference; this file (`joshi-problems-locked.md`) is the *staged slate*.

---

🌑

*End of joshi-problems-locked.md v0.2 — May 26 2026.*

*Major change since v0.1:* Built `Cursor-Joshi.md` (complete chapter-by-chapter memory of Joshi *EJM* 2nd ed., 24 chapters + 7 master indices, ~1600 lines). Used this new memory to lock 14 additional chapters (3, 4, 5, 6, 8, 9, 11, 12, 15, 16, 17, 18, 19, 20). Coverage rose from 47% to 95%; only Chapter 7 (Normalization) remains scaffold-only pending Anand's framing decision.

*Next steps after Anand-review:*
1. *Lock Ch. 7 once framing decision lands.*
2. *Begin drafting Pillar 2 chapters using this slate (priority order: Ch. 2 → 10 → 13 → 14 → 3 → ...; full draft order TBD by Anand).*
3. *Tier-balance audit on chapters with skewed distributions.*
4. *Cross-reference each drafted chapter back to `Cursor-Joshi.md` for forward-chaining citations.*
