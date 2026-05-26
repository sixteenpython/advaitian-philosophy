# Chapter 2: Symmetry — Drafting Outline

> **Status:** Outline only. No prose drafted. Awaiting Anand's review and sign-off before any section is written.
>
> **Treatment:** Direct continuation of Chapter 1 (Invariance). Same canonical template (`pillar2-archetypes/_template/chapter-template.md`). Same source-of-truth rule: every worked example and practice problem drawn from K.D. Joshi's *Educative JEE Mathematics* (2nd ed.) or from JEE / RMO / INMO exams commented on by Joshi (Blueprint §6.2). Voice register: hybrid Polya / Tao / Engel / Zeitz / Andreescu / Joshi, calibrated per section.

---

## Front Matter

| Field | Value |
|---|---|
| **Title** | Chapter 2 — Symmetry |
| **Subtitle** | "If the Problem Has Symmetry, the Solution Inherits It" |
| **Category** | Structure Recognition (Archetypes 1–4) |
| **Related archetypes** | #1 Invariance (via Noether) · #3 Duality (point ↔ line, $f$ ↔ $\hat f$) · #5 Substitution (cyclic / reflective coordinate changes) · #15 Bijection (orbit-counting) |
| **Canonical takeaway** | *"What is symmetric in the problem must be symmetric in the answer."* |
| **Length target** | ≈ 7,500 words (within the Pillar 2 chapter envelope of 7,000–9,000) |
| **Joshi source chapters** | Primary: Ch. 2 (Basic Algebra), Ch. 8 (Geometry), Ch. 18 (Definite Integrals), Ch. 24 (Misc). Secondary: Ch. 11, 13, 14, 17, 21. (See `joshi-archetype-map.md`.) |

---

## Section-by-Section Plan

### Opening Vignette  *(Sawyer / Polya voice — Pillar 2 chapter-opener register)*

**Two paired images, each demonstrating a different layer of symmetry, with the second forcing the reader past the naïve geometric reading:**

1. *The snowflake.* A six-fold rotational symmetry that any child can name. The pedagogical use is not the snowflake itself but the *consequence*: if a snowflake has six-fold symmetry, every measurement made on it (mass on each arm, fluorescence intensity, anything) inherits that symmetry — there cannot be a property of the snowflake that distinguishes one arm from another without breaking the symmetry. Symmetry constrains *what can be true*.

2. *A polynomial with three real roots $r_1, r_2, r_3$.* The coefficients of the polynomial — $r_1 + r_2 + r_3$, $r_1 r_2 + r_1 r_3 + r_2 r_3$, $r_1 r_2 r_3$ — are *symmetric* in the roots: relabel the roots and the coefficients do not change. Vieta's formulas are not a computational convenience; they are precisely the constraint that *the coefficients of a polynomial cannot see the order of the roots*. From this, every fact one extracts about the roots from the coefficients alone is necessarily a symmetric function of the roots — and *only* symmetric functions of the roots can be so extracted.

Closing sentence: *"This is Symmetry."* ≈ 450 words.

### 1. The Archetype Defined  *(Tao / Engel register, Joshi for the bridge)*

#### 1.1 Formal Definition

\begin{definition}
Let $X$ be a set and $G$ a group of transformations of $X$ (each $g \in G$ a bijection $X \to X$). The action of $G$ on $X$ is called a *symmetry of the problem* on $X$ if, for every $g \in G$, the problem's hypotheses and conclusion are unchanged when $X$ is replaced by $g \cdot X$. A function $\phi : X \to Y$ is *symmetric* (more precisely, *equivariant under $G$*) if $\phi(g \cdot x)$ is determined by $\phi(x)$ alone — in the simplest case, $\phi(g \cdot x) = \phi(x)$ for every $g \in G$.
\end{definition}

Note the relationship to Chapter 1: *every invariant is, by definition, a function symmetric under the relevant group action*. Invariance and Symmetry are two perspectives on a single phenomenon. Chapter 1 names the *quantity* that does not change; Chapter 2 names the *transformation group* that does the not-changing.

Three forms of symmetry to be unpacked, each with two examples:

- **Permutation symmetry** — relabel the variables, expression unchanged. Example: $\sigma_2(x, y, z) = xy + yz + zx$. Counter-example: $x + 2y + 3z$.
- **Reflective symmetry** — replace $x \to -x$, $\theta \to -\theta$, $f(x) \to f(a + b - x)$, expression unchanged or sign-flipped (odd / even).
- **Continuous / rotational symmetry** — the expression is invariant under rotation, scaling, or translation (the Noether bridge).

≈ 400 words.

#### 1.2 Core Principle  *(Polya)*

> *What is symmetric in the problem must be symmetric in the answer.*

This sentence — to be unpacked over 2–3 paragraphs — is the chapter's strategic master rule. It implies a checklist: *before computing*, look at the problem and identify the group of transformations that leave it unchanged; *during computing*, do not break this symmetry by an asymmetric algebraic move; *after computing*, verify that the answer respects the symmetry. An answer that does not is, with high probability, wrong.

Short illustration (no full proof): "Among all triangles of given perimeter, find the one of maximum area." The problem is symmetric in the three sides (relabeling does not change "perimeter" or "area"). Therefore the maximizing triangle must itself be symmetric in its three sides — equilateral. We did not invoke calculus. We invoked the symmetry. ≈ 350 words.

#### 1.3 The Cognitive Shift  *(Polya / Joshi)*

The "before vs after" framing, parallel to Chapter 1 §1.3 but with a different surface example.

*Before:* the student looks at a symmetric problem and treats each variable as independently to be solved for. They write three equations in three unknowns, solve mechanically, then encounter an algebraic system whose symmetry they did not exploit. The work compounds.

*After:* the symmetry-trained thinker reads the same problem and asks first *what relabeling leaves the problem alone?* If $x, y, z$ are interchangeable, write the *symmetric combinations* $\sigma_1 = x+y+z$, $\sigma_2 = xy+yz+zx$, $\sigma_3 = xyz$ and work in those. The number of unknowns is unchanged, but the problem is now expressed in coordinates *adapted to its symmetry*.

Habits of symmetry-trained solvers (4 items, parallel to Ch.1 §1.3):

1. A reflex of asking *which relabeling leaves this invariant?* before writing a single equation.
2. A working library of elementary symmetric functions ($\sigma_1, \sigma_2, \sigma_3$ for triples; Vieta for polynomial roots; the centre-of-mass coordinate for vectors).
3. Recognising when an *apparent* asymmetry in a problem is a hidden symmetry — e.g., an inequality $f(x,y,z) \geq g(x,y,z)$ where both sides are symmetric.
4. The discipline of letting the symmetry *decide* the coordinate system — never imposing Cartesian coordinates on a problem with rotational symmetry.

≈ 400 words.

### 2. The Deep Structure  *(Tao / Engel — named-theorem rigor)*

#### 2.1 Mathematical Foundations

**Group theory enters explicitly.** Beyond the §1.1 definitional remark, here we develop:

- *Orbits and stabilizers.* The orbit of $x$ is $\{g \cdot x : g \in G\}$; the stabilizer is the subgroup fixing $x$. The orbit-stabilizer theorem: $|G| = |\text{orbit}(x)| \cdot |\text{stab}(x)|$.

- *Burnside's lemma* (counting orbits as average of fixed-point counts). State formally, prove informally; this is the engine of many olympiad combinatorics problems.

- *Klein's Erlangen Program*, called out by name and date (1872): *a geometry is the study of properties invariant under a chosen group of transformations.* Euclidean geometry = rigid motions; affine = affine maps; projective = projective maps; topology = homeomorphisms. The link to Ch. 1 §2.1 closes here.

- *Noether's theorem*, called out by name and date (1918): *every continuous symmetry of a Lagrangian yields a conserved current.* Reverse direction of Ch. 1's statement — Ch. 1 framed Noether as "symmetry → invariant"; Ch. 2 frames the same theorem as "every conservation law is a symmetry in disguise."

The two named theorems — Klein and Noether — are the load-bearing structural results of the chapter and must be cited with originator + year. ≈ 550 words.

#### 2.2 Physical / Cross-Domain Foundations

Same vein as Ch. 1 §2.2 but with focus on *symmetries that produce* conservation laws:

- Translation symmetry (in time) → energy conservation.
- Translation symmetry (in space) → momentum conservation.
- Rotational symmetry → angular momentum conservation.
- Gauge symmetry (in physics) → charge conservation (the standard model rests entirely on this).
- Linguistic: anagram constraint = permutation symmetry of letters.

≈ 250 words.

#### 2.3 Cognitive Foundations  *(optional, Polya)*

*Why is symmetry difficult to use even when present?* Briefly: students are trained on *coordinate-bound* methods (Cartesian, Euclidean) and have no reflex for asking "what relabeling leaves this alone?" Three remedies, parallel to Ch. 1 §2.3. ≈ 200 words.

### 3. The Diagnostic Toolkit  *(Zeitz / Andreescu — operational)*

#### 3.1 The Three Questions Method (Symmetry edition)

Mirror of Ch. 1 §3.1, with symmetry-specific questions:

1. **What relabelings / transformations leave the problem invariant?** *(The symmetry group.)*
2. **What objects in the problem are fixed by this group?** *(The orbit structure.)*
3. **Can I express the unknowns in symmetric coordinates?** *(Elementary symmetric functions, polar coordinates, integral over a fundamental domain.)*

Each with an *execution note*: when it succeeds, when it commonly fails. ≈ 300 words.

#### 3.2 Forms / Types of Symmetry

Five categories:

- **Permutation symmetry** (symmetric in $n$ variables): elementary symmetric functions, Vieta.
- **Reflective / dihedral symmetry**: $x \to -x$, $\theta \to -\theta$, $f \to f(a+b-x)$, even/odd functions.
- **Cyclic symmetry** (less restrictive than full permutation): $x \to y \to z \to x$ but not arbitrary permutation.
- **Continuous symmetry** (rotational, scaling, translational): Lie-group action.
- **Hidden / induced symmetry**: a problem with no surface symmetry that acquires one after a coordinate change or substitution.

Each with 4–6 olympiad-grade instantiations. ≈ 400 words.

#### 3.3 Common Pitfalls  *(Polya / Joshi)*

Four named pitfalls, in the style of Ch. 1 §3.3:

1. **Breaking the symmetry without paying.** A common error: solve "assume WLOG $x \leq y \leq z$" without later restoring the lost cases. *Remedy:* either restore the cases explicitly, or argue that the conclusion is symmetric so the WLOG was free.
2. **Mistaking superficial asymmetry for actual asymmetry.** A coefficient that looks lopsided may be a unit shift that hides a symmetric structure (Joshi often shifts variables to expose hidden symmetry — e.g., the Tschirnhaus substitution, used in Ch. 1 PP5).
3. **Forgetting that symmetric does not mean equal.** *"The problem is symmetric in $x$ and $y$"* does not imply $x = y$; it implies *every property of $x$ derived from the problem is also a property of $y$*. The variables can take different values.
4. **Over-extending symmetry.** A problem may have *cyclic* (rotational) symmetry but not *full* permutation symmetry. Treating cyclic symmetry as full symmetry produces wrong proofs.

≈ 300 words.

### 4. Worked Examples  — *the chapter's centre of gravity*  *(Tao / Zeitz / Andreescu hybrid)*

The three examples illustrate three different *forms* of symmetry from §3.2:

#### 4.1 Example 1 — Cyclic Symmetry in an AP/GP Identity  *(Tier 1: JEE Mains)*

> **Problem.** *If $x, y, z$ are, respectively, the $p$-th, $q$-th, and $r$-th terms of an A.P. and also of a G.P., find the value of $x^{y-z} \cdot y^{z-x} \cdot z^{x-y}$.*

- **Source.** JEE 1979 (Joshi, *EJM* Ch. 2, Comment 6).
- **Demonstrates.** Cyclic symmetry: the expression $x^{y-z} \, y^{z-x} \, z^{x-y}$ is invariant under the cyclic relabeling $(x, y, z) \to (y, z, x)$, and the structural conditions (AP + GP) are likewise cyclically symmetric.
- **Solution arc.** Take logarithms: $\ln E = (y-z)\ln x + (z-x)\ln y + (x-y)\ln z$. Use the A.P. condition to express $x-y, y-z, z-x$ in terms of $(p-q)d, (q-r)d, (r-p)d$, and the G.P. condition to express $\ln x - \ln y$ etc. in terms of $(p-q)\ln t$. Cyclic permutation of indices collapses the algebra; $\ln E = 0$, so $E = 1$.
- **Pivot.** *Symmetric input, symmetric output: the expression is forced to take a symmetric value, and the only symmetric value $1$ has under cyclic permutation that respects the constraints is $1$ itself.*
- ≈ 600 words.

#### 4.2 Example 2 — Splitting a Definite Integral by Reflective Symmetry  *(Tier 2: JEE Advanced)*

> **Problem.** *Evaluate $\displaystyle\int_{-\pi}^{\pi} \dfrac{2x(1+\sin x)}{1+\cos^2 x}\,dx$.*

- **Source.** JEE 1997 (Joshi, *EJM* Ch. 18, Comment 12).
- **Demonstrates.** Reflective symmetry of the interval $[-\pi, \pi]$ about $0$, combined with parity classification (odd + even) of the integrand.
- **Solution arc.** The interval is symmetric about $0$. Split the integrand: $\dfrac{2x(1+\sin x)}{1+\cos^2 x} = \dfrac{2x}{1+\cos^2 x} + \dfrac{2x \sin x}{1+\cos^2 x}$. The first summand is *odd* (numerator odd, denominator even), so its integral over $[-\pi, \pi]$ vanishes by symmetry. The second summand is *even* (numerator even — $x \sin x$ is even — and denominator even), so its integral doubles the integral over $[0, \pi]$. The problem reduces to $\int_0^\pi \dfrac{4x \sin x}{1+\cos^2 x}\,dx$, evaluable by the substitution $u = \cos x$.
- **Pivot.** *Symmetry of the interval forces a clean odd/even decomposition; one half vanishes by symmetry alone, and only the even half needs computing.*
- ≈ 700 words.
- ⚠️ **Anand: confirm.** This is the canonical JEE 1997 problem and a textbook Joshi example. The full evaluation of $\int_0^\pi \frac{4x \sin x}{1+\cos^2 x}\,dx$ closes via $u = \cos x$ to a $\tan^{-1}$. Want me to walk the full evaluation, or stop at "the symmetric half vanishes, the rest is mechanical"?

#### 4.3 Example 3 — Symmetric Matrix with All-Rows-Equal Property  *(Tier 3: RMO)*

> **Problem.** *Let $n$ be an odd integer, and let $A$ be a symmetric $n \times n$ matrix in which each of the integers $1$ through $n$ appears exactly once in each row. Prove that every integer from $1$ to $n$ appears exactly once on the diagonal of $A$.*

- **Source.** Regional Mathematics Olympiad (Joshi, *EJM* Ch. 24, Exercise 24.67).
- **Demonstrates.** Full permutation symmetry of the row-content set, combined with the *involution* $A = A^T$, producing a Burnside-flavoured fixed-point argument. The "odd $n$" hypothesis is essential and analogous to the role of "odd $n$" in Ch. 1 PP3.
- **Solution arc.**
   1. Fix an integer $k \in \{1, \ldots, n\}$. Let $S_k$ be the set of positions $(i, j)$ with $A_{ij} = k$. By the row-content hypothesis, $S_k$ has *exactly one* entry per row, and by symmetry $A = A^T$, the set $S_k$ is invariant under the transposition $(i, j) \leftrightarrow (j, i)$.
   2. This transposition is an involution on $S_k$. Its fixed points are the diagonal positions $(i, i)$ with $A_{ii} = k$. Its non-fixed points pair up.
   3. By the row-content hypothesis again, $|S_k| = n$ (one entry per row). Since $n$ is *odd*, an involution on a set of odd cardinality must have at least one fixed point. Hence $k$ appears at least once on the diagonal.
   4. Counting: the diagonal has $n$ entries, $k$ ranges over $n$ values, each $k$ appears at least once on the diagonal — so each appears *exactly* once. ∎
- **Pivot.** *The symmetry constraint $A = A^T$, combined with row-content and odd-$n$, forces an involution on a set of odd size to have a fixed point in each colour class.*
- ≈ 800 words.
- ⚠️ **Anand: confirm.** This is the cleanest pure-symmetry Tier-3 problem in Joshi's exercises. Alternative candidates (less clean but also pure-symmetry): Ex. 24.60 (perpendiculars from triangle vertices), Ex. 24.61 (Napoleon's theorem variant). I prefer Ex. 24.67 because the involution-on-odd-cardinality argument is Burnside-flavoured and forward-references Pillar 5 (Cluster G).

### 5. Practice Problems  *(Engel / Andreescu — problem-set register)*

7 problems. Statements in §5; solutions/hints in chapter-end appendix. **All Joshi-sourced** per Blueprint §6.2.

| # | Problem (one-line gist) | Source | Tier |
|---|---|---|---|
| 5.1 | If $a, b, c$ are sides of an equilateral triangle (or symmetric triangle), prove a symmetric inequality of the form $a^2 + b^2 + c^2 \geq \text{(symmetric expression)}$ — exact statement to be selected from Joshi Ch. 6 (Inequalities) | Joshi, Ch. 6 (TBC; candidate: JEE 1984-tier) | 1 |
| 5.2 | $\int_0^{\pi/2} \frac{dx}{1 + \tan^n x}$ — show value $= \pi/4$ for every $n > 0$, by the substitution $x \to \pi/2 - x$ | Joshi, Ch. 18 (standard) | 1 |
| 5.3 | A polynomial $P(x)$ of degree $n$ satisfies $P(k) = 1/(k+1)$ for $k = 0, 1, \ldots, n$. Find $P(n+1)$ | Joshi, Ch. 5 (binomial-identity / symmetric-extension) | 2 |
| 5.4 | Three consecutive coefficients of $(1+x)^n$ are in AP — prove or find such $n$ (a symmetric-coefficient property) | Joshi, Ch. 5 | 2 |
| 5.5 | Let $f(x) = ax^2 + bx + c$ with $a, b, c \in \mathbb{Z}$ and $f$ taking integer values at $x = 0, 1, 2, \ldots$. Show $a, b, c$ all lie on a $\mathbb{Z}$-lattice generated by $\binom{x}{2}, x, 1$ — a polynomial-symmetric-basis identity | Joshi, Ch. 3 or Ch. 5 | 2 |
| 5.6 | Joshi Ex. 24.60 — RMO. *From vertices $A, B, C$ of triangle $ABC$, perpendiculars $AD, BE, CF$ are drawn to any straight line. Show that the perpendiculars from $D, E, F$ to $BC, CA, AB$ respectively are concurrent.* | Joshi Ch. 24 Ex. 24.60 (RMO) | 3 |
| 5.7 | Joshi Ex. 24.66 — INMO + IMO 2000. *If $a, b, c > 0$ with $abc = 1$, prove $a^{b+c} b^{c+a} c^{a+b} \leq 1$. (Highly symmetric exponent structure.)* | Joshi Ch. 24 Ex. 24.66 (INMO / IMO 2000) | 3 |

⚠️ **Anand: please confirm the §5 problem set or substitute.** I have proposed candidates by *category* (a foundational symmetric integral, a symmetric polynomial identity, a symmetric-coefficient binomial problem, a Tschirnhaus-style polynomial problem, an RMO geometry, an INMO/IMO inequality). The exact problem statements for 5.1, 5.3, 5.4, 5.5 will be locked when we draft — they need verification against Joshi text. 5.2, 5.6, 5.7 are already verified.

### 6. The Connections Web  *(Tao)*

#### 6.1 Symmetry Across Mathematical Domains
- *Algebra.* Galois group as symmetry of root-permutations; symmetric polynomials = invariants of $S_n$; Vieta = the orbit-data of polynomial roots.
- *Geometry.* Klein's Erlangen Program; Euclidean / affine / projective symmetry groups; reflection groups, $D_n, S_n, A_n$.
- *Analysis.* $L^2$ orthogonality under Fourier transform = symmetry under the dual group. Symmetric / antisymmetric functions in the complex plane.
- *Number Theory.* Quadratic reciprocity as a symmetry of Legendre symbols; modular forms as symmetric under $SL_2(\mathbb{Z})$.
- *Combinatorics.* Burnside's lemma; orbit-counting; symmetric chain decompositions.
- *Topology.* Symmetry groups of polyhedra; CW-complex cell symmetries.

#### 6.2 Symmetry in Physics & Other Sciences
- Noether's theorem: gauge symmetries → conservation laws.
- Crystallography: 230 space groups, all generated by reflection/rotation/translation symmetries.
- Chemistry: molecular point groups; selection rules in spectroscopy.
- Biology: bilateral symmetry in vertebrates; radial symmetry in echinoderms.

#### 6.3 Cross-Domain Manifestations
- *Music:* canon and fugue as time-shift symmetry of a musical line.
- *Architecture:* symmetric façades read as ordered; asymmetric façades read as dynamic.
- *Cryptography:* symmetric-key ciphers vs. asymmetric-key (public-key); the asymmetry is the security feature.
- *Economics:* equilibrium conditions are often symmetric in the agents (no agent privileged); the breakdown of symmetry signals market failure.

#### 6.4 Related Archetypes
- **#1 Invariance.** Same phenomenon, opposite direction: Ch. 1 names the quantity, Ch. 2 names the group. Noether is the bridge.
- **#3 Duality.** Symmetric pairings — primal/dual in optimization, point/line in geometry, $f$/$\hat f$ in Fourier analysis. Treated in full in Chapter 3.
- **#5 Substitution.** Symmetric substitutions ($u = x + y$, $v = xy$ for symmetric two-variable problems; $\sigma_1, \sigma_2, \sigma_3$ for three-variable problems) are the most reliable problem-collapsing moves and are themselves consequences of the underlying symmetry.
- **#15 Bijection.** Burnside's lemma counts orbits using bijection-of-orbit-representatives; orbit-counting *is* bijection-counting under a group action.

≈ 700 words total.

### 7. Master Takeaways  *(Polya / Joshi)*

Aim for 6 takeaways, each one-line and quotable. Candidate seeds:

1. **What is symmetric in the problem must be symmetric in the answer.** *(Canonical takeaway.)*
2. **Symmetry is a group acting; invariance is what survives the group's action.** *(The Ch. 1 ↔ Ch. 2 bridge.)*
3. **Don't break symmetry without paying for it.** *(The WLOG-discipline lesson.)*
4. **Cyclic symmetry is less than full symmetry — distinguish them.** *(The Pitfall-4 lesson.)*
5. **The right coordinates for a symmetric problem are themselves symmetric.** *(The elementary-symmetric-functions lesson.)*
6. **Every conservation law is a symmetry; every symmetry is a constraint.** *(Noether, fully digested.)*

### 8. Self-Assessment Checklist

7 checkpoints; mirror Ch. 1 §8. Adapt language. Include one explicit Noether-direction check (*"Given a conservation law, can I identify the symmetry it derives from?"*) and one orbit-counting check.

### Bridge to Chapter 3: Duality  *(Polya)*

Duality is the *paired* form of symmetry — instead of one object being symmetric under a group, two objects exchange roles under an involution. The relationship between Ch. 2 and Ch. 3 is analogous to that between Ch. 1 and Ch. 2: each chapter generalises the structural commitment of the previous one.

A single transitional passage hinting at: *point-line duality in projective geometry, primal-dual in linear programming, the $f$/$\hat f$ duality of Fourier analysis, and Pontryagin duality as the closing theme.* ≈ 300 words.

---

## Items requiring Anand's decision before any prose is drafted

1. **Worked Example 1.** JEE 1979 cyclic-symmetry AP/GP problem (locked candidate). Confirm or substitute.
2. **Worked Example 2.** JEE 1997 integral with split-by-parity (locked candidate). Confirm depth of full evaluation in the §4.2 solution (full closed-form vs. stop at "the rest is mechanical").
3. **Worked Example 3.** RMO Ex. 24.67 (symmetric matrix involution). Confirm or substitute (alternates: Ex. 24.60 or 24.61).
4. **Practice problems.** Four of the seven (5.1, 5.3, 5.4, 5.5) are proposed by *category*, not by locked statement. The exact problems will be selected from Joshi during drafting; please flag any problems you want forced into the slate (e.g., a particular RMO favourite).
5. **Length target.** ≈ 7,500 words. Acceptable, or compress?
6. **Noether-bridge weight.** Section 2.1 promises full named-theorem citations of *both* Klein (1872) and Noether (1918). Confirm this depth — the alternative is to keep only Noether and reference Klein in passing.
7. **Burnside placement.** I propose stating Burnside's lemma formally in §2.1 and using it implicitly in WE3 (the symmetric-matrix problem) but *not* using its full machinery here — full Burnside applications are reserved for Chapter 13 (Combinatorial Principles) and Chapter 15 (Bijection). Confirm.

---

## Joshi reference map (specific to this chapter)

| Section | Primary Joshi source(s) |
|---|---|
| Opening Vignette | Ch. 2, Comment 6 (cyclic-AP/GP problem references) |
| §1.1 Formal Definition | Ch. 2 (symmetric polynomials), Ch. 18 (even/odd functions) |
| §2.1 Group-theory foundations | None directly — bridges to Stewart's *Galois Theory* and Klein's *Erlangen Program* (external) |
| §2.2 Physical foundations | None directly in Joshi; supplementary from Polya's *Mathematics and Plausible Reasoning* |
| §3.2 Forms of Symmetry | Ch. 2 (permutation), Ch. 17–18 (reflective), Ch. 21 (rotational via vectors) |
| §3.3 Pitfalls | Ch. 24 (Joshi's own pitfall commentaries) |
| §4.1 WE1 (cyclic) | Ch. 2, Comment 6 (JEE 1979) ✓ verified |
| §4.2 WE2 (reflective) | Ch. 18, Comment 12 (JEE 1997) ✓ verified |
| §4.3 WE3 (involution) | Ch. 24, Ex. 24.67 (RMO) ✓ verified |
| §5 Practice (5.1) | Ch. 6 — TBC during draft |
| §5 Practice (5.2) | Ch. 18 — standard substitution; TBC during draft |
| §5 Practice (5.3, 5.4, 5.5) | Ch. 3, 5 — TBC during draft |
| §5 Practice (5.6) | Ch. 24, Ex. 24.60 (RMO) ✓ verified |
| §5 Practice (5.7) | Ch. 24, Ex. 24.66 (INMO + IMO 2000) ✓ verified |

---

## Notes for the drafter (self-discipline)

1. The chapter must *forward-reference* Ch. 1 cleanly: every appearance of "invariance" should be paired with the symmetry interpretation, completing the Ch. 1 ↔ Ch. 2 circle.
2. The Joshi-sourcing discipline is non-negotiable. Do not introduce any worked example or practice problem from outside Joshi's *EJM* without an explicit decision logged here.
3. Voice register switches are budgeted at ≤ 2 per section. The chapter is denser than Ch. 1 in named-theorem content (Klein + Noether + Burnside); compensate with shorter cognitive-shift paragraphs.
4. The §4.3 RMO involution proof is a forward reference to Burnside; if Anand prefers to keep Burnside in Pillar 5 only, demote §4.3 to a direct pigeonhole-counting argument without naming the lemma.

---

🌑

*End of outline. Awaiting Anand's sign-off before any prose drafting begins.*
