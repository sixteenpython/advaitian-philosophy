---
chapter: 12
archetype: Extremal Principles
subtitle: "Nature Optimizes; So Should Your Solution"
category: Constraint Exploitation (Archetypes 9–12) — fourth and closing chapter
related_archetypes: [1, 2, 10, 11, 13]
key_gems: [B01, B05, B07, F07, F12, G07]
  - "Weierstrass extreme-value theorem: a continuous real-valued function on a compact set attains its maximum and minimum"
  - "First-order necessary condition: at an interior extremum of a differentiable function, the gradient vanishes ($f'(x) = 0$ in 1-dim; $\\nabla f(\\mathbf x) = \\mathbf 0$ in $n$-dim)"
  - "Second-order sufficient condition (1-dim): $f''(x_0) > 0$ at $f'(x_0) = 0$ implies local minimum (and $< 0$ implies local maximum)"
  - "Hessian test (2-dim): at a critical point $\\nabla f = \\mathbf 0$, if $\\det H > 0$ and $f_{xx} > 0$ then local minimum (negative-definite cases give local maximum, indefinite gives saddle point)"
  - "Fundamental theorem of linear programming: the extremum of a linear functional on a bounded polytope is attained at a vertex"
  - "Lagrange multiplier theorem: at a constrained extremum subject to $g(\\mathbf x) = 0$, $\\nabla f = \\lambda \\nabla g$ for some real $\\lambda$"
  - "Equality-case principle (cross-reference Ch. 10): the extremum of a function bounded by an inequality is attained on the equality case of the inequality"
  - "Symmetry principle for extrema (cross-reference Ch. 2): an extremum of a symmetric function on a symmetric domain is typically attained at a symmetric configuration"
  - "Josephus survivor formula: in a circular elimination process with stride $2$, the survivor for $n$ contestants is at position $J(n) = 2r + 1$ where $n = 2^k + r$ with $0 \\le r < 2^k$"
  - "Erdős-Mordell inequality: for $P$ inside $\\triangle ABC$ with vertex-distances $p_a, p_b, p_c$ and pedal-distances $d_a, d_b, d_c$, $p_a + p_b + p_c \\ge 2(d_a + d_b + d_c)$, equality iff $\\triangle ABC$ is equilateral and $P$ is its centre"
canonical_takeaway: "The extremum is where the structure becomes sharp. Whether it lives at a vertex, on a boundary, or at an interior critical point is the first question — and often the most consequential one."
status: locked
last_revised: 2026-05-29
locked_on: 2026-05-29
sourcing_note: "All worked examples and practice problems in this chapter are drawn from K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), or from JEE / RMO / INMO / Putnam examinations commented on in that text. See Blueprint §6.2 for the sourcing rule and `pillar2-archetypes/_template/joshi-problems-locked.md` §Ch. 12 for the locked slate. **Verification audit for this chapter discovered two slate errors**: (a) WE3 (Joshi Ch. 13, Comment 6, closest point on parabola) listed the source point as $(2, -1/2)$ with distance $\\sqrt{13}/2$, but the answer $(1, 1)$ requires source $(2, 1/2)$ with distance $\\sqrt 5/2$ — the slate had a sign error in the source $y$-coordinate that propagated to a wrong distance; the answer point $(1, 1)$ is correct given the corrected source. (b) PP3(ii) (Joshi Ex. 24.91, quadratic form $x^2 + 2xy + 3y^2 - 6x - 2y$) listed the minimum as $-13/2$ at $(7/2, -1/2)$, but the correct critical point is $(4, -1)$ with value $-11$ — verified by gradient-zero analysis, Hessian-positivity test, and an independent completing-the-square argument. Both errors patched in slate v0.2.9; see WE3 and PP3 in the appendix for the corrected derivations."
---

# Chapter 12 — Extremal Principles

## *Nature Optimizes; So Should Your Solution*

---

## Opening Vignette

A revenue manager at an Indian carrier in Bengaluru is pricing the seats on tomorrow morning's Bengaluru-to-Singapore flight. The aircraft has $180$ seats. Three fare classes are open: economy (Rs. $E$ per seat), premium-economy (Rs. $P$), business (Rs. $B$), with $E < P < B$. The forecasting model gives expected demand at each price; the airline's revenue-management system has to choose how many seats to *protect* for each higher-fare class (i.e., refuse to sell at lower fare even if demand is there) and how many to *release* to economy. Mathematically, the problem is a *linear program*: maximise total expected revenue subject to (i) total seats allocated $\le 180$; (ii) demand-at-each-fare cap; (iii) non-negativity of each protection level. The revenue manager does not solve this by gradient descent or by iterating; she knows from the *fundamental theorem of linear programming* that the optimum is attained at a *vertex* of the feasible polytope. The polytope has a small finite number of vertices (one per choice of which constraints are *binding*), and the manager simply *enumerates the vertices* and picks the one with the highest revenue. The computation takes seconds. Without the vertex-extremum theorem, the search space would be the continuous feasible polytope — uncountably many points; with the theorem, the search is finite. The trained revenue manager processes hundreds of flights a day using this structural insight; her airline's quarterly revenue depends on it.

Now turn to a different scene. A carpenter in Mysuru is making a large rectangular dining table from a hemi-circular slab of teak — a half-disc of radius $1.2\,\text{m}$, the salvaged top of a much larger old circular table whose other half had warped and cracked. The carpenter wants the rectangle to be as large as possible, subject to fitting inside the semicircle with one side along the cut diameter. He sketches the configuration: the rectangle has its base on the diameter, the two upper corners on the curved arc. As he stares at the sketch, he realises the optimal rectangle must be *symmetric* — the rectangle is centred on the diameter; the two upper corners are symmetric about the perpendicular through the diameter's midpoint. Once the symmetry is fixed, only one parameter remains: the angle $\theta$ at which the upper corners sit, measured from the centre. The corners are at $(R\cos\theta, R\sin\theta)$ and $(-R\cos\theta, R\sin\theta)$; the rectangle has width $2R\cos\theta$ and height $R\sin\theta$; the area is $2R^2 \sin\theta\cos\theta = R^2 \sin 2\theta$, maximised when $2\theta = \pi/2$, i.e., $\theta = \pi/4$. At the optimum: width $= R\sqrt 2 \approx 1.70\,\text{m}$; height $= R/\sqrt 2 \approx 0.85\,\text{m}$; area $= R^2 = 1.44\,\text{m}^2$. The carpenter does not compute calculus on the four-variable problem (two corners times two coordinates); he recognises that the *symmetry of the configuration* fixes three of the four variables, leaving a one-variable optimisation that he solves by recognising $\sin 2\theta$ peaks at $\theta = \pi/4$. The trained craftsman uses the symmetry-extremum principle as routinely as his measuring tape.

These two scenes look unrelated. An airline revenue manager pricing seats; a carpenter shaping a table. They share the most important reframing in the entire chapter — the recognition that *where the extremum lives* is the first question to answer, often before the extremum's value is computed. The revenue manager knows the extremum lives at a *vertex* of the constraint polytope (because the objective is linear and the polytope is bounded — the LP vertex theorem); the carpenter knows the extremum lives at the *symmetric configuration* (because the objective and constraints are symmetric — the symmetry-extremum principle). In both cases, the location of the extremum is determined *structurally*, before any calculation, and the calculation that follows is essentially mechanical. The trained problem-solver internalises this two-step pattern: *first locate the extremum (by structure); then compute its value (by calculation)*. The two steps are *not* commutative — getting the location right makes the calculation tractable; getting the calculation right without the location wastes effort on points that cannot be optimal.

This is *Extremal Principles*. It is the closing chapter of the *Constraint Exploitation* sub-pillar (Chapters 9–12), unifying the inequality machinery of Chapter 10 (every inequality has an equality-case, which is an extremum) with the existence machinery of Chapter 11 (the Weierstrass extreme-value theorem guarantees that compact-set continuous-function optimisations *have* extrema to find). The chapter equips the reader with the named-theorem toolkit (Weierstrass extreme-value theorem; first- and second-derivative tests; Hessian test in higher dimensions; Lagrange multipliers; LP vertex theorem; symmetry-extremum principle; Erdős-Mordell-style geometric inequalities; Josephus-style combinatorial extremals) that converts *vague optimisation* into *structured solution*. The chapter has three structural threads. The first is the *toolkit*: the named extremum theorems and their deployment signatures. The second is the *location-first principle*: knowing *where* the extremum lives (interior, boundary, vertex, symmetric configuration) is the first and most consequential question. The third is the *cross-archetype unification*: extrema unify the inequality-constraint machinery (Ch. 10), the existence-and-uniqueness machinery (Ch. 11), the symmetry machinery (Ch. 2), and the invariance machinery (Ch. 1) into a single coherent picture — and the chapter makes this explicit.

> *The extremum is where the structure becomes sharp. Whether it lives at a vertex, on a boundary, or at an interior critical point is the first question — and often the most consequential one.*

---

## 1. The Archetype Defined

### 1.1 Formal Definition

We make the intuition precise.

\begin{definition}[Extremal Principle]
An *extremal principle* on a problem with variables $\mathbf x \in D$ and objective $f : D \to \mathbb R$ is a structural fact about *where* the extremum (maximum or minimum) of $f$ over $D$ is attained — whether at an interior critical point, on a boundary face, at a vertex, on a symmetric configuration, or at the equality case of a defining inequality. The archetype is the discipline of (i) verifying that the extremum *exists* (typically by Weierstrass on a compact set); (ii) identifying *where* the extremum is located by structural arguments; and (iii) computing the value at the located extremum.
\end{definition}

Three remarks unpack the definition. First, the *existence* question (Weierstrass: continuous $f$ on compact $D$ attains $\max$ and $\min$) is the prerequisite. Without compactness, the optimisation may have no attained extremum: $f(x) = x$ on $\mathbb R$ has no max or min; $f(x) = 1/x$ on $(0, 1]$ has no max (it diverges) and a min at $x = 1$. The trained solver verifies *compactness of the domain* and *continuity of the objective* before going further.

Second, the *location* question splits into several structural cases depending on the geometry of $D$ and the regularity of $f$. *Interior extremum* (smooth $f$, interior of $D$): first-derivative zero, second-derivative test for max-vs-min. *Boundary extremum* (smooth $f$, $D$ with boundary): equality case of a defining inequality (Lagrange multipliers, KKT conditions). *Vertex extremum* (linear or convex $f$, polytope $D$): LP vertex theorem. *Symmetric extremum* (symmetric $f$, symmetric $D$): the extremum often (but not always) sits at the symmetric configuration. The trained solver reads the geometry and the regularity, then matches to the right case.

Third, the *value* question reduces, after location is fixed, to a routine algebraic or calculus computation. The hard work is in the location; the value follows.

The chapter encounters five characteristic forms of extremal principle.

- **Form I — Interior smooth extremum (calculus).** $f$ smooth, $D$ open or interior; extremum at gradient-zero point. *Examples.* WE3 (closest point on parabola), PP1 (monotonicity of $xe^{x(1-x)}$), PP3 (quadratic-form minima), PP5 (Snell's law via Fermat).

- **Form II — Boundary / vertex extremum (linear programming, KKT).** $f$ linear or convex, $D$ a bounded polytope; extremum at a vertex. *Examples.* WE1 (linear on convex polygon).

- **Form III — Symmetric extremum.** $f$ and $D$ symmetric under a group action; extremum at the symmetric configuration. *Examples.* PP6 (cotangent sum at $\theta_1 = \theta_2 = \pi/4$), PP4 (rectangle in semicircle).

- **Form IV — Inequality-equality-case extremum (cross-archetype with Ch. 10).** $f$ bounded by an inequality (AM-GM, Cauchy-Schwarz, Jensen); extremum at the equality case. *Examples.* PP2 (convex quadrilateral, where AM-GM forces $p = 8$ exactly), PP7 (Erdős-Mordell equality at equilateral).

- **Form V — Combinatorial / discrete extremum.** $D$ a finite or discrete set, $f$ a counting or combinatorial quantity; extremum found by structural recursion (Josephus, pigeonhole-extremal duality, $n$-th-cake-survival). *Examples.* WE2 (Josephus cake-survival).

### 1.2 The Core Principle

Stripped to its essence, the principle is one sentence.

> *The extremum is where the structure becomes sharp.*

This sentence captures the recurrent observation that, across mathematics, the extremum of a well-structured problem is *not* a generic point of the domain — it is a *special* point, identified by the structure itself. *Vertex* of a polytope (the LP case); *symmetric configuration* of a symmetric problem (the AM-GM equality case); *interior critical point* of a smooth function (the gradient-zero case); *boundary equality* of an inequality constraint (the KKT case); *survivor of a recursion* (the Josephus case). In each case, the extremum *cannot* be a generic interior point; the structure *picks out* a small set of candidate extrema, and the trained solver enumerates the candidates rather than searching the entire domain.

The cognitive shift is from *"optimise by exhaustive search over the domain"* to *"identify the structural candidates first; check only those."* The reframing converts continuous-search problems into finite-enumeration problems, often reducing the computational complexity from infinite to a small constant.

A complementary phrasing: *the extremum is where the structure breaks down* — where some constraint becomes binding, where some symmetry-distinguished point sits, where some inequality becomes equality. The structure that *holds elsewhere* (interior, away from boundary, asymmetric, strict-inequality) *breaks down* at the extremum (boundary, equality, symmetric). The trained solver looks for *the breakdown* and finds the extremum.

### 1.3 The Cognitive Shift

Three cognitive shifts deserve naming.

The first is *location-before-value*. The trained solver, when faced with an optimisation problem, asks *where does the extremum live?* — separately from *what is its value?* This reframing prevents a class of inefficient calculations: trying to compute the extremum at points that *cannot* be optimal because the structural location-principles rule them out. The revenue manager's enumeration of vertices is faster than gradient descent on the polytope; the carpenter's symmetric ansatz is faster than four-variable calculus.

The second shift is *named-theorem selection*. The location-determining theorems are finite and well-organised: *Weierstrass* (existence on compact sets); *first-derivative zero* (interior smooth extremum); *Hessian test* (max-vs-min classification); *LP vertex theorem* (linear on polytope); *Lagrange multipliers* (constrained extremum); *KKT conditions* (inequality-constrained extremum); *symmetry principle* (symmetric extrema at symmetric configurations); *AM-GM equality case* (algebraic extremum via inequality). The trained solver matches the problem's structure to the theorem in seconds.

The third shift is *cross-archetype synthesis*. Extremal principles unify Chapters 1 (Invariance — the *conserved quantity* often *vanishes* at the extremum), 2 (Symmetry — the extremum is at the *symmetric configuration*), 10 (Inequality Constraints — the extremum is the *equality case*), and 11 (Existence — Weierstrass guarantees the extremum *exists*). The trained solver, by Chapter 12, sees these as a single coherent framework rather than four separate techniques, and chooses the framing the problem most naturally invites.

---

## 2. The Deep Structure

### 2.1 Mathematical Foundations

Extremal principles rest on four mathematical foundations.

The first is the *Weierstrass extreme-value theorem*: every continuous real-valued function on a compact subset of $\mathbb R^n$ (or any compact metric space) attains its maximum and minimum. *Compactness* is the topological property that converts "supremum" (least upper bound, may not be attained) into "maximum" (attained at some point). The theorem is the foundation of *all* of optimisation; without compactness (and continuity), the optimisation may have no attained extremum, and the *first-derivative zero* and other location-tools have nothing to certify. Weierstrass is the *existence* theorem; the location-tools then *identify* where the extremum sits.

The second foundation is the *first-order necessary condition* (Fermat's theorem in one dimension, the gradient-zero condition in higher dimensions). If $f$ is differentiable and attains a local extremum at an interior point $\mathbf x_0$ of its domain, then $\nabla f(\mathbf x_0) = \mathbf 0$. The converse is *not* automatic: gradient-zero points (critical points) may be local maxima, local minima, *or saddle points*. The classification requires the *second-order test* — the sign of $f''(x_0)$ in 1-dim, the *Hessian matrix* in higher dimensions. *Positive-definite* Hessian: local minimum. *Negative-definite*: local maximum. *Indefinite*: saddle point (the function increases in some directions and decreases in others). The second-order test is *sufficient* (with the strict-definiteness) but not *necessary* (a function can have a local minimum at a critical point with positive-semidefinite but not positive-definite Hessian).

The third foundation is *Lagrange multipliers and the KKT conditions*. For constrained optimisation *maximise $f$ subject to $g(\mathbf x) = 0$*, at a constrained extremum the gradient of the objective is *parallel* to the gradient of the constraint: $\nabla f = \lambda \nabla g$ for some real $\lambda$ (the *Lagrange multiplier*). The KKT generalisation handles *inequality* constraints $h_i(\mathbf x) \le 0$ with *complementary slackness* ($\lambda_i h_i = 0$, either the constraint is non-binding or the multiplier is zero). The Lagrange and KKT machinery converts *constrained optimisation* into *unconstrained optimisation of an augmented Lagrangian* — and the solution lives at a critical point of the Lagrangian.

The fourth foundation is the *fundamental theorem of linear programming*: the extremum of a linear functional on a bounded polytope is attained at a vertex (or, if the polytope is unbounded, possibly at infinity along an edge). *Proof sketch*: a linear functional is bounded on a bounded polytope (compactness + linearity = continuity); the level sets of a linear functional are parallel hyperplanes; the highest level set that intersects the polytope must touch it at a vertex (else the level set could be moved further). The *simplex method* of LP is a vertex-walking algorithm that exploits this structure. The vertex theorem extends to convex objectives on polytopes (the extremum is on the boundary, possibly at a vertex but always on the boundary).

A fifth foundation, important for combinatorial extremal problems: *recursion and the substitution principle*. For a discrete extremum problem with a recursive structure (Josephus, Tower-of-Hanoi survival counts, certain shortest-path problems), the extremum often satisfies a *recursive equation* that can be solved in closed form via substitution. The Josephus formula $J(2m + 1) = 2 J(m) + 1$ and $J(2m) = 2 J(m) - 1$ unfolds to $J(n) = 2(n - 2^{\lfloor \log_2 n \rfloor}) + 1$ — a closed form obtained by structural recursion, not by exhaustive search.

### 2.2 Physical and Cross-Domain Foundations

The reach of extremal principles extends across the quantitative sciences.

In *classical mechanics*, *Hamilton's principle of least action* says that the physical trajectory of a system between fixed endpoints is the one that *extremises* (more precisely, makes stationary) the *action functional* $\int L\,dt$, where $L = T - V$ is the Lagrangian. The Euler-Lagrange equations (the first-order necessary conditions of the variational problem) are equivalent to Newton's laws. The entire framework of classical mechanics — Lagrangian, Hamiltonian, canonical transformations — is built on extremal principles. The trained physicist reads classical equations as *extrema of action functionals*.

In *quantum mechanics*, the *variational principle* says: the ground-state energy of a quantum system is the infimum of $\langle\psi|H|\psi\rangle / \langle\psi|\psi\rangle$ over all *trial wave functions* $\psi$, and equality is attained at the actual ground-state wave function. The principle is the foundation of variational quantum methods (Hartree-Fock, density-functional theory, the variational Monte Carlo method) — methods that *find* the ground state by minimising a trial energy over a parametrised family of wave functions.

In *thermodynamics and statistical mechanics*, the *second law* says that an isolated system evolves to a state of *maximum entropy* subject to its conserved-quantity constraints. The maximum-entropy principle (Jaynes) is a Bayesian-information-theoretic reformulation: in the absence of additional information, the least-biased probability distribution consistent with the constraints is the *maximum-entropy* distribution. The Gibbs distribution (the Boltzmann factor $e^{-E/kT}$) is the maximum-entropy distribution at fixed mean energy. *Phase transitions* are non-analyticities in the extremum's dependence on parameters.

In *optics*, *Fermat's principle of least time* says that light travels between two points along the path of *minimum time*. Snell's law (the refraction-index ratio) is the first-order necessary condition of the variational problem (PP5 develops this). The *eikonal equation* of geometric optics is the Euler-Lagrange equation of the Fermat functional. *Mirages, rainbows, lens design* all follow from Fermat.

In *economics*, *utility maximisation* (each consumer maximises utility subject to a budget constraint) and *profit maximisation* (each firm maximises profit subject to technology constraints) are the foundational extremal principles. *Pareto optimality* is the multi-objective extremum: a feasible allocation is Pareto-optimal iff no other feasible allocation gives strictly more to at least one agent without giving less to any other. *Equilibrium analysis* in general-equilibrium theory uses fixed-point and extremum methods together.

In *engineering*, *least-squares regression*, *minimum-energy designs*, *minimum-time controllers*, *minimum-cost configurations* — all are extremal-principle problems. The *calculus of variations* and *optimal control theory* (Pontryagin's maximum principle) are the named tools that engineers deploy. The opening vignette's revenue manager and carpenter are everyday examples.

In *biology*, *optimal foraging theory*, *evolutionary stable strategies* (Maynard Smith), *minimum-action principles in morphogenesis* — biological systems often appear to extremise some fitness or efficiency functional. The interpretation is subtle (evolution does not *optimise* in a teleological sense; the apparent optimisation is the result of selection pressure), but the mathematical apparatus is the same.

### 2.3 Cognitive Foundations

The cognitive payoff of extremal principles is threefold.

The first is *complexity reduction*. Identifying the structural location of the extremum (vertex, symmetric configuration, boundary equality) reduces the search space from continuous-and-vast to finite-and-small. The revenue manager enumerates a handful of vertices; the carpenter optimises a one-parameter family. The reduction is often dramatic: a 100-variable LP has at most $\binom{100}{50}$ vertices to examine; gradient descent on the polytope would have to traverse the entire interior.

The second payoff is *robustness*. The structural location of the extremum is *stable* under small perturbations of the problem: a small change in the objective coefficients of an LP usually moves the vertex slightly but does not change *which constraints are binding*. A small change in a symmetric problem usually preserves the symmetric extremum. This robustness is what makes structural location-tools useful in practice — they survive the noisy real-world data that purely-numerical methods can be fragile to.

The third payoff is *cross-archetype synthesis*. By Chapter 12, the reader has seen extrema arise as: *the equality case of an inequality* (Ch. 10); *the existence-conclusion of Weierstrass* (Ch. 11); *the symmetric configuration of a symmetric problem* (Ch. 2); *the vertex of a polytope* (the LP version of "where the structure is sharpest"); *the survivor of a combinatorial recursion* (the Josephus version). The chapter makes these connections explicit and the trained solver, by chapter end, recognises that *an extremum is a structurally-distinguished point*, and the structural distinction is what to look for.

---

## 3. The Diagnostic Toolkit

### 3.1 The Three Questions Method (Extremal-Principle Edition)

Before deploying any optimisation tool, the trained solver asks three questions of the problem.

1. **Does an extremum exist?** Verify Weierstrass's hypotheses: *the domain is compact* (closed and bounded in $\mathbb R^n$; finite for combinatorial problems); *the objective is continuous*. If both hold, $\max$ and $\min$ are attained; if either fails, the extremum may not exist (and the problem may need re-statement, e.g., asking for $\inf$ / $\sup$ instead of $\min$ / $\max$).

2. **Where is the extremum located?** Match the problem's structure to the location-determining theorem:
   - *Smooth $f$, interior of $D$:* first-derivative zero (1-dim) or gradient zero (higher-dim).
   - *Linear $f$, bounded polytope:* LP vertex theorem; enumerate vertices.
   - *Symmetric $f$ and $D$:* extremum at symmetric configuration (often).
   - *Inequality-bounded $f$:* extremum at the equality case (Ch. 10 cross-link).
   - *Constrained smooth optimisation:* Lagrange multipliers; or KKT for inequality constraints.
   - *Combinatorial recursion:* recursive equation for the extremum; solve by substitution.

3. **What is the value at the located extremum?** Compute the value at the identified candidate point(s); for the LP-vertex case, enumerate and pick the highest / lowest; for the smooth-interior case, evaluate $f$ at the critical points and compare with boundary values.

The three questions can be answered in seconds. They are the discipline that converts *vague optimisation* into *structured solution*.

### 3.2 Forms of Extremal Principles: A Comprehensive Guide

We collect the five forms encountered in the chapter with one-line diagnostics.

- **Form I — Interior smooth extremum (calculus).** *Diagnostic:* $f$ is differentiable and the domain has interior; the extremum is at a gradient-zero point. *Move:* set $f'(x) = 0$ (1-dim) or $\nabla f(\mathbf x) = \mathbf 0$ (higher-dim); solve for critical points; classify by second-derivative / Hessian test. *Examples.* WE3 (closest point on parabola), PP1 ($xe^{x(1-x)}$ monotonicity), PP3 (quadratic forms), PP5 (Snell via Fermat).

- **Form II — Boundary / vertex extremum (linear programming).** *Diagnostic:* $f$ is linear or convex; $D$ is a bounded polytope or convex set with extreme points. *Move:* identify the vertices (extreme points) of $D$; evaluate $f$ at each; pick the extremum. *Examples.* WE1 (linear on convex polygon).

- **Form III — Symmetric extremum.** *Diagnostic:* $f$ and $D$ are invariant under a symmetry group; the extremum (often, not always) sits at a fixed point of the group action. *Move:* impose the symmetric ansatz; verify by substitution that the resulting candidate is the extremum (the second-derivative test may be needed to rule out saddle points). *Examples.* PP6 (symmetric cotangent sum), PP4 (rectangle in semicircle).

- **Form IV — Inequality-equality-case extremum (cross-archetype with Ch. 10).** *Diagnostic:* the objective is bounded above (or below) by a known inequality (AM-GM, Cauchy-Schwarz, Jensen); the extremum is the bound, attained at the equality case. *Move:* identify the inequality that gives the bound; identify the equality case; verify the configuration is in the domain. *Examples.* PP2 (convex quadrilateral, AM-GM forces $p = 8$), PP7 (Erdős-Mordell at equilateral).

- **Form V — Combinatorial / discrete extremum.** *Diagnostic:* $D$ is finite or discrete; $f$ is a counting or combinatorial quantity; the extremum has a recursive structure. *Move:* derive the recursion for the extremum; solve by substitution or by recognising a closed-form pattern. *Examples.* WE2 (Josephus survivor).

### 3.3 Common Pitfalls

Five errors recur often enough to deserve named warnings.

- **The Existence-Skipped Pitfall.** Searching for an extremum without first verifying that one exists. If $D$ is open or unbounded, the extremum may not be attained; the candidate "$\sup f = +\infty$" or "$\inf f$ not attained" is then the correct answer, not a number. The remedy is the §3.1 Q1 discipline: *verify Weierstrass before searching*.

- **The Critical-Point Confusion.** Identifying a gradient-zero point as a maximum (or minimum) without applying the second-derivative test. A gradient-zero point can be a local max, a local min, or a saddle. The remedy is the second-derivative test: $f''(x_0) > 0 \Rightarrow$ min; $f''(x_0) < 0 \Rightarrow$ max; $f''(x_0) = 0 \Rightarrow$ further analysis required.

- **The Boundary-Ignored Pitfall.** Searching for the extremum only at interior critical points, ignoring the *boundary* of the domain. The extremum may be on the boundary (especially for constrained problems), and the interior search will miss it. The remedy is to evaluate $f$ at the interior critical points *and* on the boundary, then compare.

- **The Symmetry-Assumed Pitfall.** Assuming that a symmetric problem's extremum is at the symmetric configuration, without verification. *Most* symmetric problems have their extremum at the symmetric configuration, but exceptions exist (e.g., symmetry-breaking phase transitions in physics; the *thrackle conjecture* and similar in combinatorics). The remedy is to *verify* the symmetric-configuration candidate (second-derivative test, or comparison with explicit asymmetric candidates).

- **The Vertex-Missed Pitfall.** Searching for the extremum of a linear objective in the *interior* of a polytope, when the LP vertex theorem says it must be at a vertex. The interior search wastes effort. The remedy is to *recognise linear objectives* and immediately enumerate vertices.

---

## 4. Worked Examples

We work three problems in detail, each in the six-point format. The first illustrates Form II (vertex extremum) for linear-on-polygon; the second illustrates Form V (combinatorial recursion) for the Josephus cake-survival; the third illustrates Form I (smooth interior extremum) for the closest-point-on-parabola problem — with the verification-audit-revealed source-point correction.

### 4.1 Example 1 — Maximum of a Linear Function on a Convex Polygon

**Problem.** *Let $S$ be a convex polygon (a bounded convex region in $\mathbb R^2$ with finitely many vertices $V_1, V_2, \ldots, V_k$). Let $f(x, y) = ax + by$ be a linear function. Prove that $f$ attains its maximum (and minimum) on $S$ at a vertex.*
*(Joshi EJM Ch. 24, Exercise 24.92(c); the fundamental theorem of linear programming in 2 dimensions.)*

**SEED.** *Extremal principle (Form II — vertex extremum on a polytope).* The objective is linear; the domain is a bounded polytope. By the LP vertex theorem, the extremum is at a vertex. The proof is by *iterated convexity*: any interior or boundary point can be written as a convex combination of vertices, and linearity of $f$ then bounds $f(P)$ by the maximum (or minimum) of $f$ at the vertices.

**BRUTE PATH.** A student who does not know the LP vertex theorem might try to optimise $f(x, y) = ax + by$ over $S$ by setting up the gradient: $\nabla f = (a, b)$, which is non-zero (assuming $a, b$ not both zero). Since the gradient is *constant* and *non-zero*, $f$ has no interior critical points. The extrema must therefore be on the boundary. On each edge of $S$, $f$ restricted to the edge is again linear, and its extremum on the edge is at an endpoint of the edge (a vertex). So the candidate extrema are the *vertices*. This brute path works, but it is essentially a re-derivation of the LP vertex theorem; the structural recognition shortcuts the argument.

**ELEGANT PIVOT.** *Direct application of the vertex theorem.*

*Step 1 — Polygon as convex hull of vertices.* By the definition of a convex polygon, every point $P \in S$ can be written as a convex combination of the vertices:
\[
  P \;=\; \sum_{i=1}^k \lambda_i V_i, \quad \text{with } \lambda_i \ge 0 \text{ and } \sum_{i=1}^k \lambda_i = 1.
\]

*Step 2 — Linearity preserves convex combinations.* Apply $f$ to both sides:
\[
  f(P) \;=\; f\!\left(\sum_i \lambda_i V_i\right) \;=\; \sum_i \lambda_i f(V_i),
\]
using the linearity of $f$ (constant-multiple and additivity).

*Step 3 — Bound by maximum and minimum at the vertices.* Let $V_{\max}$ and $V_{\min}$ be vertices where $f$ attains its max and min over $\{V_1, \ldots, V_k\}$, respectively. Then $f(V_i) \le f(V_{\max})$ for every $i$, so
\[
  f(P) \;=\; \sum_i \lambda_i f(V_i) \;\le\; \sum_i \lambda_i \cdot f(V_{\max}) \;=\; f(V_{\max}),
\]
since $\sum_i \lambda_i = 1$. Hence $\max_{P \in S} f(P) \le f(V_{\max})$. But the reverse inequality is trivial ($V_{\max}$ itself is in $S$), so $\max_{P \in S} f(P) = f(V_{\max})$. Symmetrically, $\min_{P \in S} f(P) = f(V_{\min})$. \hfill$\blacksquare$

The elegant pivot is a one-step convex-combination argument: every point of the polygon is a convex combination of vertices; the linear objective is bounded by the maximum-and-minimum vertex values via the convex-combination identity. The argument generalises seamlessly to higher dimensions (the *Caratheodory theorem*: every point of an $n$-dim polytope is a convex combination of at most $n + 1$ vertices) and to *convex objectives* (a convex function on a polytope is bounded by its vertex values, by convexity; the extremum is on the boundary but not necessarily at a single vertex).

**PITFALLS.**

- *Forgetting that "linear" includes the constant-term subtleties.* A *linear* function is $f(x, y) = ax + by$ (no constant term); an *affine* function is $f(x, y) = ax + by + c$. The vertex theorem holds for both (since affine functions are linear functions plus a constant, and the constant shifts all values equally). The remedy is to *check whether the problem says "linear" or "affine"*, but in practice the theorem applies to both.

- *Assuming the polygon must be in $\mathbb R^2$.* The vertex theorem holds in $\mathbb R^n$ for any $n$: the extremum of a linear function on a bounded polytope is at a vertex. The 2-dim case (polygon) is the elementary version; the $n$-dim case is the foundation of the simplex algorithm. The remedy is to *recognise the theorem's scope*.

- *Forgetting the bounded hypothesis.* If $S$ is *unbounded*, the linear function may not attain a maximum on $S$ — the LP can be *unbounded*. (E.g., $f(x, y) = x$ on the half-plane $y \ge 0$ has $\sup f = +\infty$, not attained.) The vertex theorem applies only to bounded polytopes. The remedy is to *verify boundedness*.

- *Conflating "extremum" with "unique extremum".* The vertex theorem says the extremum is *attained at some vertex*; it does not say the extremum is attained *only* at a vertex. If the linear function is constant along an edge (i.e., the level set of $f$ contains the edge), then the extremum is attained at *every point* of that edge (not just the endpoints). The remedy is to *not assume uniqueness*.

- *Searching for extrema in the interior.* Linear functions have no interior critical points (their gradient is constant and non-zero in general). Searching the interior wastes effort. The remedy is to *recognise the structural form (linear objective) and apply the vertex theorem immediately*.

**CONNECTIONS.**

*Primary archetype applications.* The vertex theorem is the foundation of *linear programming*, an enormous body of optimisation theory and practice. The *simplex method* of Dantzig (1947) is a vertex-walking algorithm; the *interior-point methods* of Karmarkar (1984) and Nesterov-Todd (1990s) are alternatives that work in the interior but converge to a vertex. *Integer programming, mixed-integer programming, branch-and-bound, cutting-plane methods* are all developments of the basic vertex-theorem insight.

*Alternative solution archetypes.* The vertex theorem is the *symmetry-breaking* version of the symmetric-extremum principle (Form III): a linear objective on a convex polytope has *no* symmetric extremum at the centroid (unless the polytope is symmetric and the objective is zero — a degenerate case); the extremum is at a vertex precisely because the vertex *breaks* the polytope's local convexity. The vertex theorem is also a *cross-archetype with Ch. 3 (Duality)*: LP has a dual, and the *strong duality theorem* says the primal optimum equals the dual optimum, with the optimum attained at a vertex of both the primal and dual polytopes.

*Cross-domain manifestations.* The vertex theorem is the foundation of *combinatorial optimisation* (network flows, assignment problems, the travelling salesman problem's LP relaxation), of *game theory* (the *minimax theorem* of von Neumann is the LP-duality theorem applied to two-player zero-sum games), of *economics* (Walrasian equilibria are vertex-extrema of certain LP-duality structures), and of *operations research* (production planning, transportation problems, vehicle routing, scheduling).

**TAKEAWAY.** *Linear objective + bounded polytope = extremum at a vertex; enumerate vertices instead of searching the interior.*

---

### 4.2 Example 2 — The Josephus Cake-Survival Problem

**Problem.** *Cakes numbered $1, 2, \ldots, n$ are arranged clockwise in a circle. A person starts at cake $1$. The cakes are eaten in the following pattern: starting from position $1$, skip the cake at position $1$, eat the cake at position $2$, skip $3$, eat $4$, ..., and continue cyclically (always alternating skip-eat, going around the circle) until only one cake remains. Let $f(n)$ be the number of the cake that survives. Find a closed-form expression for $f(n)$, and compute $f(1000)$.*
*(Joshi EJM Ch. 24, Exercise 24.77; the classical Josephus problem with $k = 2$.)*

**SEED.** *Extremal principle (Form V — combinatorial recursion).* The survivor's position is the *extremal* element of the elimination process (the one that survives every round). The position satisfies a recurrence based on the binary structure of $n$, and the recursion unfolds to a closed-form involving the largest power of $2$ at most $n$. *The combinatorial extremum is identified by the recursion, not by case-by-case enumeration.*

**BRUTE PATH.** Simulate the process for small $n$:
- $n = 1$: only cake $1$; survives. $f(1) = 1$.
- $n = 2$: cake $1$ skipped, cake $2$ eaten; cake $1$ survives. $f(2) = 1$.
- $n = 3$: skip $1$, eat $2$; remaining cycle $\{1, 3\}$, continuing from $3$; skip $3$, eat $1$. Cake $3$ survives. $f(3) = 3$.
- $n = 4$: skip $1$, eat $2$; skip $3$, eat $4$; remaining $\{1, 3\}$, continuing from $4$; the next position is $1$, skip it (skip after eating $4$); eat $3$. Cake $1$ survives. $f(4) = 1$.
- $n = 5$: skip $1$, eat $2$; skip $3$, eat $4$; skip $5$, eat $1$; remaining $\{3, 5\}$, continuing; skip $3$, eat $5$. Cake $3$ survives. $f(5) = 3$.
- $n = 6$: $f(6) = 5$ (by similar simulation).
- $n = 7$: $f(7) = 7$.
- $n = 8$: $f(8) = 1$.
- $n = 9$: $f(9) = 3$.

The brute path gives a pattern: $f(n) = 1, 1, 3, 1, 3, 5, 7, 1, 3, 5, 7, 9, 11, 13, 15, 1, \ldots$. Whenever $n$ is a power of $2$, $f(n) = 1$. Between consecutive powers of $2$, $f(n)$ grows by $2$ each step. *The pattern suggests a binary-decomposition formula.*

**ELEGANT PIVOT.** *Establish the recurrence and solve by binary decomposition.*

*Step 1 — Recurrence for $f(2m)$.* In the first pass through the $2m$ cakes, the even-indexed ones ($2, 4, 6, \ldots, 2m$) are eaten, and the odd-indexed ones ($1, 3, 5, \ldots, 2m - 1$) remain. After the first pass, the cycle is $\{1, 3, 5, \ldots, 2m - 1\}$, and the elimination continues from the position *after* the last eaten ($2m$), which is back to *cake $1$*. So we are starting again at cake $1$, but with $m$ cakes; by the original problem, the survivor among $\{1, 3, 5, \ldots, 2m - 1\}$ in *their* re-labelled positions $\{1, 2, 3, \ldots, m\}$ is at position $f(m)$. Translating back: the survivor in the original labelling is $2 f(m) - 1$.

So $f(2m) = 2 f(m) - 1$.

*Step 2 — Recurrence for $f(2m + 1)$.* In the first pass through the $2m + 1$ cakes, the even-indexed ones ($2, 4, \ldots, 2m$) are eaten in the first $m$ steps. After that, cake $2m + 1$ remains as the next candidate; it is *eaten* next (since we have just skipped $2m - 1$ and eaten $2m$ — wait, let me redo this more carefully).

Actually, for $n = 2m + 1$ odd: the first pass skips $1$, eats $2$, skips $3$, eats $4$, ..., skips $2m - 1$, eats $2m$. We have eaten $m$ cakes and now stand at $2m + 1$, about to skip-or-eat. The pattern is *skip-eat-skip-eat-...* starting with *skip $1$*. So after skipping $1$, eating $2$, ..., eating $2m$, we have alternated $2m$ times. The next action is *skip $2m + 1$*. Then the next is *eat $1$* (since $1$ is the next clockwise position after $2m + 1$). After eating $1$, we have eaten $m + 1$ cakes and skipped $m + 1$.

After this, the remaining cakes are $\{3, 5, 7, \ldots, 2m + 1\}$ — a set of $m$ cakes. We continue from the position after $1$ (which is $3$, the next undiscarded cake). The next action is *skip $3$, eat $5$, skip $7$, eat $9$, ..., or skip $3$, eat $5$, ...* Since the previous action was *eat $1$*, the next is *skip $3$* (alternating). So we re-label $\{3, 5, 7, \ldots, 2m + 1\}$ as $\{1', 2', 3', \ldots, m'\}$ (so original $3$ becomes $1'$, etc.; original $2k + 1$ becomes $k'$), and the elimination proceeds as the $m$-cake Josephus from position $1'$.

The survivor (in the re-labelled positions) is $f(m)$. Translating back: original $f(m)$-th position in the re-labelled set $\{3, 5, \ldots, 2m + 1\}$ is $2 f(m) + 1$.

So $f(2m + 1) = 2 f(m) + 1$.

*Step 3 — Solve the recurrence by binary decomposition.* Write $n = 2^k + r$ with $0 \le r < 2^k$ and $k$ the largest integer with $2^k \le n$. We claim $f(n) = 2 r + 1$.

*Proof by induction on $k$.* Base: $k = 0$, so $n = 2^0 + r = 1 + r$ with $r = 0$ (since $r < 2^0 = 1$), giving $n = 1$ and $f(1) = 1 = 2(0) + 1$. ✓

Inductive step: assume the formula holds for all powers $\le 2^{k-1}$. Consider $n = 2^k + r$ with $0 \le r < 2^k$.

Case A: $r$ even, $r = 2s$ with $0 \le s < 2^{k-1}$. Then $n = 2^k + 2s = 2(2^{k-1} + s)$, even. By step 1: $f(n) = 2 f(2^{k-1} + s) - 1$. By inductive hypothesis with $m = 2^{k-1} + s$ (and $s$ as the offset since $0 \le s < 2^{k-1}$): $f(2^{k-1} + s) = 2s + 1$. So $f(n) = 2(2s + 1) - 1 = 4s + 1 = 2(2s) + 1 = 2r + 1$. ✓

Case B: $r$ odd, $r = 2s + 1$ with $0 \le s$ and $2s + 1 < 2^k$, i.e., $s < (2^k - 1)/2$. Then $n = 2^k + 2s + 1 = 2(2^{k-1} + s) + 1$, odd. By step 2: $f(n) = 2 f(2^{k-1} + s) + 1$. By inductive hypothesis: $f(2^{k-1} + s) = 2s + 1$. So $f(n) = 2(2s + 1) + 1 = 4s + 3 = 2(2s + 1) + 1 = 2r + 1$. ✓

In both cases, $f(n) = 2r + 1$ as claimed.

*Step 4 — Compute $f(1000)$.* The largest power of $2$ at most $1000$ is $2^9 = 512$. So $r = 1000 - 512 = 488$ and
\[
  f(1000) \;=\; 2 \cdot 488 + 1 \;=\; \boxed{977.}
\]
$\blacksquare$

The elegant pivot is the *combinatorial recursion*: the survival problem for $n$ cakes reduces to the survival problem for $\lfloor n/2 \rfloor$ cakes, with a structured re-labelling. The recursion unfolds in $\log_2 n$ steps to a closed form involving the binary representation of $n$.

**PITFALLS.**

- *Mis-setting up the recurrence.* The cases $n = 2m$ (even) and $n = 2m + 1$ (odd) give different recurrences ($f(2m) = 2f(m) - 1$ vs $f(2m+1) = 2f(m) + 1$); confusing them gives wrong results. The remedy is to *track the parity of $n$ carefully*.

- *Mis-identifying the largest $2^k$.* For $n = 1000$, the largest power of $2$ at most $1000$ is $2^9 = 512$, not $2^{10} = 1024$ (which exceeds $1000$). The remedy is to *compute $\lfloor \log_2 n \rfloor$ explicitly*: $\log_2 1000 \approx 9.97$, so $k = 9$.

- *Confusing "starting at cake $1$" with "starting *eating* at cake $1$".* The standard Josephus convention is to *skip* cake $1$ first (then eat $2$), as the problem says "starts at cake $1$ and eats every alternate cake." A different convention ("starts by eating cake $1$") gives a different problem with a different formula. The remedy is to *read the problem statement carefully and verify on small cases*.

- *Mistaking the formula's domain.* The formula $f(n) = 2r + 1$ requires $n = 2^k + r$ with $r \ge 0$ and $k$ the largest with $2^k \le n$. If $n = 2^k$ exactly (so $r = 0$), then $f(n) = 1$. The remedy is to *verify the boundary cases*.

- *Treating this as a smooth optimisation problem.* The Josephus problem is *combinatorial* and *discrete*; smooth calculus is irrelevant. The "extremum" is the *combinatorial survivor*, not a calculus-extremum. The remedy is to *recognise the discrete-recursion structure*.

**CONNECTIONS.**

*Primary archetype applications.* The Josephus formula is the prototype of *combinatorial-extremum-via-recursion*, a family of problems where the survivor / extremal element satisfies a recursive equation that unfolds to a closed form. *Variants*: the Josephus with stride $k \ne 2$ (no closed form for general $k$, but the recurrence $J_k(n) = (J_k(n - 1) + k) \mod n$, with $J_k(1) = 0$, gives an $O(n)$ algorithm); the *Boustrophedon* recurrence in combinatorial identities; the *Catalan number* recurrence $C_{n+1} = \sum_i C_i C_{n-i}$.

*Alternative solution archetypes.* The Josephus problem also yields to *Hidden Structure* (Ch. 4): the binary representation of $n$ encodes the survivor in a strikingly clean way (*the binary representation of $n$ with the leading $1$ moved to the end gives the survivor*: e.g., $1000_{10} = 1111101000_2 \to 1111010001_2 = 977_{10}$). Cross-reference with Ch. 14 (Parity / Modularity) would highlight the role of parity in the recurrence.

*Cross-domain manifestations.* The Josephus problem has a curious applied life: in *parallel-computation scheduling* (which thread is left running after iterated halving of the thread pool), in *cryptographic key-elimination protocols* (which key survives a stride-elimination), in *epidemiological-model survival analysis* (the *last patient standing* in certain stochastic-elimination models), and in the *literal historical original* (Josephus's account of his own survival from a Roman mass-suicide pact, by computing the position to claim in the elimination circle). The mathematical structure is universal; the applications are varied.

**TAKEAWAY.** *Combinatorial extremum via recursion: write the recurrence for the survival problem; solve by binary decomposition; the answer is $J(n) = 2r + 1$ where $n = 2^k + r$.*

---

### 4.3 Example 3 — Closest Point on the Parabola $y = x^2$

**Problem.** *Find the point on the parabola $y = x^2$ closest to the point $(2, 1/2)$.*
*(Joshi EJM Ch. 13, Comment 6; the closest-point problem on a smooth curve via calculus.)*

*[Verification-audit note: the locked slate listed the source point as $(2, -1/2)$ with distance $\sqrt{13}/2$, but the slate's stated answer $(1, 1)$ requires source $(2, 1/2)$ and distance $\sqrt 5 / 2$; the slate had a sign typo in the source's $y$-coordinate. The chapter uses the corrected source point $(2, 1/2)$; the slate is patched in v0.2.9.]*

**SEED.** *Extremal principle (Form I — smooth interior extremum).* The parabola is a smooth 1-dim manifold (parametrised by $t \mapsto (t, t^2)$); the distance from a point on the parabola to a given external point is a smooth function of the parameter; the minimum is at a *critical point* (where the derivative vanishes). The geometric interpretation: at the closest point, the *tangent* to the parabola is *perpendicular* to the line joining the closest point to the external point.

**BRUTE PATH.** Trying to find the closest point by sketching the parabola and the external point, then visually estimating, gives only an approximate answer. A more systematic brute path: substitute $y = x^2$ into the distance formula $d^2(x, y) = (x - 2)^2 + (y - 1/2)^2$, getting a one-variable function $d^2(x) = (x-2)^2 + (x^2 - 1/2)^2$. Then expand and differentiate — but the expanded form is a fourth-degree polynomial, and the critical-point analysis becomes algebraically heavy. The brute path *works*; the elegant pivot uses parametrisation more cleanly.

**ELEGANT PIVOT.** *Parametrise the parabola, minimise squared distance, apply the gradient-zero condition.*

*Step 1 — Parametrisation.* Every point on the parabola $y = x^2$ has the form $(t, t^2)$ for some real $t$. The squared distance from $(t, t^2)$ to the external point $(2, 1/2)$ is
\[
  d^2(t) \;=\; (t - 2)^2 + \left(t^2 - \tfrac{1}{2}\right)^2.
\]
(Minimising the squared distance is equivalent to minimising the distance, since both are non-negative and the square-root function is increasing on $[0, \infty)$.)

*Step 2 — Expand and differentiate.* Expanding:
\[
  d^2(t) \;=\; (t^2 - 4t + 4) + \left(t^4 - t^2 + \tfrac{1}{4}\right) \;=\; t^4 - 4t + \tfrac{17}{4}.
\]
Differentiate:
\[
  \frac{d}{dt}\, d^2(t) \;=\; 4 t^3 - 4 \;=\; 4(t^3 - 1).
\]
Setting equal to zero: $t^3 = 1$, so $t = 1$ (the unique real solution; the other two roots $t = e^{\pm 2\pi i/3}$ are complex and not on the real parabola).

*Step 3 — Verify the critical point is a minimum.* Second derivative:
\[
  \frac{d^2}{dt^2}\, d^2(t) \;=\; 12 t^2.
\]
At $t = 1$: $12 > 0$. The second derivative is positive, confirming a local minimum. Since $d^2(t) \to +\infty$ as $|t| \to \infty$, the local minimum is the *global* minimum.

*Step 4 — Compute the closest point and the distance.* At $t = 1$: the closest point on the parabola is $(1, 1)$. The distance is
\[
  d(1) \;=\; \sqrt{(1 - 2)^2 + \left(1 - \tfrac{1}{2}\right)^2} \;=\; \sqrt{1 + \tfrac{1}{4}} \;=\; \sqrt{\tfrac{5}{4}} \;=\; \boxed{\frac{\sqrt 5}{2}.}
\]
$\blacksquare$

*Geometric interpretation.* At $(1, 1)$, the tangent line to the parabola has slope $y'(1) = 2$, so the tangent direction is $(1, 2)$ and the perpendicular direction (the normal) is $(2, -1)$. The vector from the closest point $(1, 1)$ to the external point $(2, 1/2)$ is $(2 - 1, 1/2 - 1) = (1, -1/2)$. This vector is parallel to the normal $(2, -1)$ (ratio $1/2 = -1/2 / -1$). ✓ The geometric condition *perpendicular from closest point to tangent* is satisfied.

The elegant pivot deploys *parametric calculus*: the parabola becomes a 1-dim parameter family; the squared distance becomes a 1-variable function; the critical-point analysis pins the minimum at $t = 1$. The geometric interpretation (perpendicular tangent at the closest point) is a useful sanity check.

**PITFALLS.**

- *Forgetting to square the distance.* Minimising $d(t) = \sqrt{(t-2)^2 + (t^2 - 1/2)^2}$ directly involves a square root, complicating the derivative. Minimising $d^2(t)$ avoids the square root and is equivalent (both have their minimum at the same $t$). The remedy is to *always minimise the squared distance for closest-point problems*.

- *Mis-identifying the parametrisation.* The parabola $y = x^2$ is parametrised by $t \mapsto (t, t^2)$, *not* $t \mapsto (t^2, t)$ (which parametrises the *sideways* parabola $x = y^2$). The remedy is to *write out the parametrisation explicitly and verify it lies on the curve*.

- *Skipping the second-derivative test.* A critical point can be a minimum, a maximum, or a saddle (inflection in 1-dim). Without the second-derivative check, the critical-point candidate is not certified as a minimum. The remedy is *always check the second derivative*.

- *Confusing local with global minimum.* For a *bounded* domain (like a compact interval), a local minimum may not be the global minimum (the boundary may have lower values). For the parabola (an unbounded curve), $d^2(t) \to +\infty$ as $|t| \to \infty$, so the *unique* local minimum is automatically the global minimum. The remedy is to *check behaviour at infinity for unbounded domains*.

- *Mis-reading the source point's coordinates.* The verification audit caught a slate typo: source $(2, -1/2)$ vs $(2, 1/2)$. The two points give *different* closest-point problems with different answers (and indeed, for $(2, -1/2)$ the critical equation is $4t^3 + 4t - 4 = 0$, giving an irrational $t \approx 0.6823$, not $t = 1$). The remedy is to *verify the answer by substituting back into the gradient condition*.

**CONNECTIONS.**

*Primary archetype applications.* The closest-point-on-curve technique generalises to *closest point on a surface* (parametrise the surface; minimise squared distance; apply the gradient-zero condition in two parameters). It is the foundation of *projection* operations in numerical analysis (projecting a point onto an algebraic variety or onto a manifold), of *level-set methods* in image processing (the closest point on a level set), and of *manifold learning* in machine learning (finding the closest point on a learned low-dim manifold approximating high-dim data).

*Alternative solution archetypes.* The same problem admits a *Lagrange multiplier* solution: minimise $(x - 2)^2 + (y - 1/2)^2$ subject to $y = x^2$, i.e., $y - x^2 = 0$. Setting $\nabla[(x-2)^2 + (y - 1/2)^2] = \lambda \nabla[y - x^2]$: $(2(x - 2), 2(y - 1/2)) = \lambda (-2x, 1)$, giving $2(x - 2) = -2\lambda x$ and $2(y - 1/2) = \lambda$. Combined with $y = x^2$: $\lambda = 2(x^2 - 1/2)$ and $x - 2 = -\lambda x = -2x(x^2 - 1/2) = -2x^3 + x$. So $-2 = -2x^3$, $x^3 = 1$, $x = 1$. ✓ Lagrange route gives the same answer as parametric calculus but with more machinery.

*Cross-domain manifestations.* The closest-point problem appears throughout applied mathematics: in *robotics* (a robot arm computing the closest point on a target surface for an end-effector); in *computer graphics* (ray-tracing computes the closest intersection of a ray with a scene); in *operations research* (the *facility-location problem* — where to place a facility to minimise the maximum distance to clients); in *physics* (the *eikonal equation* of geometric optics, with light rays following closest-path trajectories in inhomogeneous media).

**TAKEAWAY.** *Closest-point-on-smooth-curve via parametric calculus: parametrise; minimise squared distance; verify with the second-derivative test; sanity-check the geometric interpretation (perpendicular tangent).*

---

## 5. Practice Problems

Seven problems, statements only; full solutions appear in the Appendix. The slate spans Tier 2 through Tier 4, with three Tier-2 problems anchoring accessibility and two Tier-4 problems pushing to RMO / olympiad standard.

### 5.1 Monotonicity of $f(x) = xe^{x(1-x)}$ (Tier 2; JEE 2001; Joshi Ch. 24, Exercise 24.42)

Consider $f(x) = xe^{x(1-x)}$. Which of the following is true?
(A) $f$ is increasing on $[-1/2, 1]$.
(B) $f$ is decreasing on $\mathbb R$.
(C) $f$ is increasing on $\mathbb R$.
(D) $f$ is decreasing on $[-1/2, 1]$.

### 5.2 Convex Quadrilateral with Diagonal Constraint (Tier 4; Joshi Ch. 24, Exercise 24.74)

In a planar convex quadrilateral of area $32$, the sum of the lengths of one pair of opposite sides and one diagonal is $16$. Determine the minimum possible length of the other diagonal.

### 5.3 Minimum of Quadratic Forms (Tier 2; Joshi Ch. 24, Exercise 24.91)

Find the minimum value of each of the following functions of two real variables:
(i) $f_1(x, y) = x^2 + 3y^2 - 6x - 2y$.
(ii) $f_2(x, y) = x^2 + 2xy + 3y^2 - 6x - 2y$.

*[Verification-audit note: the locked slate listed part (ii)'s minimum as $-13/2$ at $(7/2, -1/2)$, but the correct minimum is $-11$ at $(4, -1)$; see the appendix solution and the slate v0.2.9 patch for the corrected derivation.]*

### 5.4 Largest Rectangle in a Semicircle (Tier 2 JEE Advanced; Joshi Ch. 13, Comment 4)

Find the largest rectangle that can be inscribed in a semicircle of radius $R$, with one side along the diameter.

### 5.5 Snell's Law via Fermat's Principle (Tier 3; Joshi Ch. 16, Comment 6)

Light travels from $A = (0, a)$ above the $x$-axis to $B = (d, -b)$ below it, crossing the $x$-axis (the boundary between two media) at some point. The speed of light is $v_1$ above the $x$-axis and $v_2$ below. By Fermat's principle, the light follows the path of minimum total time. Prove that the path of minimum time satisfies *Snell's law*: $\sin\theta_1 / \sin\theta_2 = v_1 / v_2$, where $\theta_1$ and $\theta_2$ are the angles between the path and the normal to the $x$-axis above and below, respectively.

### 5.6 Cotangent-Sum Minimum (Tier 3; Joshi Ch. 14, Comment 5)

For positive real $\theta_1, \theta_2$ with $\theta_1 + \theta_2 = \pi/2$ (fixed), find the minimum value of $\cot\theta_1 + \cot\theta_2$.

### 5.7 Erdős-Mordell Inequality (Tier 4; Joshi Ch. 14, Exercise 14.18)

Let $P$ be a point inside $\triangle ABC$. Let $p_a, p_b, p_c$ denote the distances from $P$ to the vertices $A, B, C$ respectively, and let $d_a, d_b, d_c$ denote the (perpendicular) distances from $P$ to the sides $BC, CA, AB$ respectively. Prove that
\[
  p_a + p_b + p_c \;\ge\; 2(d_a + d_b + d_c),
\]
with equality if and only if $\triangle ABC$ is equilateral and $P$ is its centre.

---

## 6. The Connections Web

Extremal principles connect to nearly every later archetype and to substantial parts of every quantitative discipline.

### 6.1 Extremal Principles Across Mathematical Domains

*Calculus.* Differential calculus is, structurally, the study of *extrema* of functions: the *derivative-zero* condition for interior extrema, the *second-derivative* and *higher-derivative* tests for max-vs-min classification, the *mean value theorem* for the secant-tangent extremum, *Taylor's theorem* for polynomial-approximation extremals. *Integral calculus* extends this: the *isoperimetric inequality* (the circle maximises area for fixed perimeter) is a continuum extremum; the *calculus of variations* (Euler-Lagrange, Hamilton-Jacobi) systematises extremal problems on function spaces.

*Linear algebra.* The *singular value decomposition* expresses every matrix as a sum of rank-one outer products; the *largest singular value* extremises the operator norm. The *Rayleigh quotient* $R(\mathbf x) = \mathbf x^T A \mathbf x / \mathbf x^T \mathbf x$ for symmetric $A$ has its extremum at the *eigenvectors* with eigenvalue equal to the Rayleigh quotient value; this is the *spectral characterisation* of eigenvalues as extrema of the Rayleigh quotient. *Courant-Fischer min-max theorem* characterises all eigenvalues simultaneously as min-max extrema.

*Real analysis.* The *isoperimetric inequality*, the *Sobolev inequalities* (extremal functions related to the Yamabe problem), the *Hardy inequalities* (extremal sequences). Many of these have *extremal* (or *extremiser*) functions whose explicit form is itself an object of study.

*Combinatorics.* The *extremal set theory* (Erdős, Ko, Rado, Sperner): what is the maximum size of a family of subsets of $\{1, \ldots, n\}$ satisfying certain intersection conditions? *Turán's theorem* in extremal graph theory: the maximum number of edges in a graph on $n$ vertices without a complete subgraph $K_{r+1}$. *Ramsey theory*: the minimum $n$ such that every 2-colouring of edges of $K_n$ contains a monochromatic $K_r$.

*Number theory.* *Extremal sequences* like the *Beatty sequence* and *Stern-Brocot* fractions; *extremal Diophantine approximations* (the *continued fraction expansion* gives optimal rational approximations to irrationals); *extremal density* problems (the densest packing of spheres in $\mathbb R^n$, the Hales-Ferguson-Maryland resolution of the Kepler conjecture).

*Geometry.* The *isoperimetric inequality* (circle in the plane, sphere in space), the *Minkowski mixed volumes* (extremal under various symmetry-breaking conditions), the *Brunn-Minkowski inequality* and its generalisations. *Geodesics* are extremal curves on Riemannian manifolds; *minimal surfaces* (mean curvature zero) are extremals of the area functional.

### 6.2 Extremal Principles in Physics, Engineering, and Beyond

*Classical mechanics.* *Hamilton's principle of least action* and its descendants (Maupertuis, Lagrange, Hamilton, Jacobi). The entire *analytical mechanics* edifice (Lagrangian, Hamiltonian, Routhian, Hamilton-Jacobi) is an extremum-based reformulation of Newton's laws. *Noether's theorem* connects symmetries of the action to conserved quantities — a deep cross-archetype with Ch. 1 (Invariance).

*Quantum mechanics.* The *variational principle* for the ground state. The *time-energy uncertainty* inequality has extremal wave functions (Gaussian wavepackets minimising the product). *Path integrals* are infinite-dimensional extremum-type calculations.

*Statistical mechanics.* *Maximum entropy* (Jaynes) is the variational principle for equilibrium distributions. *Variational free energy* methods (mean-field, Bogoliubov inequality) give upper bounds on the partition function via trial Hamiltonians.

*Optics.* *Fermat's principle of least time* (light follows the minimum-time path). The *eikonal equation* of geometric optics. Lens design optimises lens shapes to minimise aberrations.

*Engineering.* *Optimal control* (Pontryagin's maximum principle, the calculus of variations applied to control problems). *Topology optimisation* (the optimal shape for a structural element with given load constraints — a continuum extremum problem). *Model predictive control* (real-time solution of constrained extremum problems on receding horizons).

*Economics.* *Utility maximisation* (consumers), *profit maximisation* (firms), *welfare maximisation* (social planner). *Game-theoretic equilibria* are fixed-points of best-response correspondences — extremum-related. *Mechanism design* searches over mechanisms for one that *maximises* the principal's objective subject to incentive-compatibility constraints.

*Biology.* *Optimal foraging theory*. *Evolutionarily stable strategies* (Maynard Smith). *Morphogenesis under minimum-energy principles*. *Resource allocation in cellular metabolism*.

### 6.3 Cross-Domain Manifestations

*Music.* A musical composition is, in some interpretations, an *extremum* of an aesthetic-cost functional (some pieces are maximally "tense"; some are maximally "resolved"). *Schenkerian analysis* identifies the *fundamental structure* of a tonal piece as an extremal-reduction of the surface.

*Architecture.* *Catenary curves* (the shape of a hanging chain) are extremal under gravity; *Gaudí's* hanging-chain models for the Sagrada Familia are physical computations of structural extrema. *Solar-orientation* of buildings is an extremum of light absorption (or shade-rejection, depending on climate).

*Linguistics.* *Optimality theory* in phonology and syntax: linguistic forms are extrema of constraint-ranking functionals. The output of a grammar is the form that *minimally violates* the highest-ranked constraints.

*Politics.* *Voting theory* (Arrow's impossibility theorem, the *median voter* theorem). *Apportionment* (the optimal allocation of legislative seats to subgroups). *Gerrymandering* (the *maximally* — or *minimally* — partisan district map).

### 6.4 Related Archetypes

Extremal principles interact with five other archetypes in particularly tight ways.

- **Archetype 1 (Invariance).** *Noether's theorem*: every continuous symmetry of an action functional gives a conserved quantity. The conserved quantity is *invariant* along the extremal trajectory. Chapters 1 (Invariance) and 12 (Extremal Principles) interlock at Noether's theorem.

- **Archetype 2 (Symmetry).** The extremum of a symmetric function on a symmetric domain often sits at the symmetric configuration. The PP6 cotangent-sum problem and the PP4 rectangle-in-semicircle problem are direct instances of this principle.

- **Archetype 10 (Inequality Constraints).** Every extremum is the *equality case* of an inequality; every inequality has an extremum on its *equality case*. Chapter 10 (Inequality Constraints) and Chapter 12 (Extremal Principles) are two sides of the same coin — Chapter 10 names the inequality machinery, Chapter 12 locates the extremum.

- **Archetype 11 (Existence / Uniqueness).** The *Weierstrass extreme-value theorem* (continuous functions on compact sets attain their extrema) is the foundational existence theorem for extremal principles. Without Weierstrass, the location-tools have nothing to certify.

- **Archetype 13 (Combinatorial Principles).** Combinatorial-extremal problems (Josephus, Turán, Sperner, Ramsey) involve discrete extrema; Chapter 13 develops the named-tools (inclusion-exclusion, pigeonhole, the probabilistic method) that often complement the recursion-based attack of Form V.

---

## 7. Master Takeaways

Seven sentences. Each one is a complete operational principle.

1. *The extremum is where the structure becomes sharp.* (The canonical takeaway.)

2. *Linear objective + bounded polytope = extremum at a vertex; enumerate vertices instead of searching the interior.* (WE1 takeaway; Form II.)

3. *Combinatorial extremum via recursion: write the recurrence; solve by binary decomposition (or other structural identity).* (WE2 takeaway; Form V.)

4. *Closest-point-on-smooth-curve via parametric calculus: parametrise; minimise squared distance; verify with second-derivative; sanity-check the geometric perpendicularity.* (WE3 takeaway; Form I.)

5. *Verify existence (Weierstrass) before searching for the extremum's location.*

6. *Match the location-determining theorem to the structure: smooth interior $\Rightarrow$ gradient zero; linear-on-polytope $\Rightarrow$ vertex; symmetric problem $\Rightarrow$ symmetric configuration; inequality-bounded $\Rightarrow$ equality case; discrete recursion $\Rightarrow$ closed-form via substitution.*

7. *Cross-archetype: extrema unify invariance (conserved quantities), symmetry (symmetric configurations), inequality constraints (equality cases), and existence (Weierstrass) — by Chapter 12 these are one coherent framework.*

---

## 8. Self-Assessment Checklist

You have absorbed Chapter 12 when, without re-opening it, you can do each of the following from memory.

- [ ] State the Weierstrass extreme-value theorem (continuous functions on compact sets attain their max and min) and identify the failure modes for non-compact or non-continuous problems.
- [ ] State the first-derivative necessary condition for interior extrema and the second-derivative sufficient condition for max-vs-min classification (in 1-dim).
- [ ] State the Hessian test for two-variable extrema: at $\nabla f = \mathbf 0$, $\det H > 0$ + $f_{xx} > 0$ $\Rightarrow$ local min; $\det H > 0$ + $f_{xx} < 0$ $\Rightarrow$ local max; $\det H < 0$ $\Rightarrow$ saddle.
- [ ] State the fundamental theorem of linear programming (linear functional on bounded polytope has extremum at a vertex) and prove it via the convex-combination identity.
- [ ] State the Lagrange multiplier theorem and apply it to a constrained optimisation problem (e.g., maximise $f$ subject to $g = 0$).
- [ ] State the equality-case principle (the extremum of an inequality-bounded function is on the equality case) and link it to AM-GM, Cauchy-Schwarz, Jensen via their equality cases.
- [ ] State the symmetry-extremum principle (extrema of symmetric problems often sit at symmetric configurations) and identify when it fails (symmetry-breaking phase transitions, asymmetric extrema).
- [ ] Derive the Josephus survivor formula $J(n) = 2r + 1$ where $n = 2^k + r$, $0 \le r < 2^k$; compute $J(1000) = 977$ from $1000 = 2^9 + 488$.
- [ ] State and prove the Erdős-Mordell inequality $p_a + p_b + p_c \ge 2(d_a + d_b + d_c)$ for $P$ inside $\triangle ABC$, with equality iff equilateral and $P$ at centre.
- [ ] Identify and explain three of the five common pitfalls: Existence-Skipped, Critical-Point Confusion, Boundary-Ignored, Symmetry-Assumed, Vertex-Missed.

---

## Bridge to Chapter 13: Combinatorial Principles

Chapter 12 closed the *Constraint Exploitation* sub-pillar (Chapters 9–12). The four chapters together developed the constraint-side of problem-solving: Domain Constraints (Ch. 9) introduced filtering; Inequality Constraints (Ch. 10) supplied the named-inequality toolkit; Existence / Uniqueness (Ch. 11) developed the existence-and-uniqueness theorems; Extremal Principles (Ch. 12) unified the previous three by elevating *the equality case of an inequality* and *the existence-and-location of an extremum* into a single coherent framework. With Chapter 12 in hand, the reader has internalised that constraints — domain, inequality, existence, extremum — are not obstacles to problem-solving but the very *engine* of structured solution.

Chapter 13 — *Combinatorial Principles* — opens the *Structural Reasoning* sub-pillar (Chapters 13–16), which moves from *constraints on individual problems* to *structures shared across problem families*. The named tools shift to *inclusion-exclusion* (the universal counting decomposition), *pigeonhole* (the universal existence-by-counting tool), *complementary counting* (the dual of direct counting), *generating functions* (the algebraic encoding of combinatorial sequences), *the probabilistic method* (proving existence by showing the expected count is positive), and *Burnside's lemma* (the symmetry-aware counting tool that sits at the boundary with Ch. 2). The cognitive shift: from *enumerate-and-count* to *structure-first-then-count*, where the *structure of the count* — its symmetries, its recursions, its inclusion-exclusion decomposition — is identified before the count itself is computed.

With Chapter 13 in hand, the reader will have begun the *Structural Reasoning* sub-pillar, leading naturally through Chapter 14 (Parity / Modular Reasoning), Chapter 15 (Continuity / Topological Reasoning), and Chapter 16 (Algebraic Structure Recognition).

---

## Appendix — Solutions to Practice Problems

### Solution to 5.1 — Monotonicity of $f(x) = xe^{x(1-x)}$

Differentiate:
\[
  f'(x) \;=\; e^{x(1-x)} + x \cdot e^{x(1-x)} \cdot (1 - 2x) \;=\; e^{x(1-x)} \big(1 + x(1 - 2x)\big) \;=\; e^{x(1-x)} (1 + x - 2x^2).
\]
Since $e^{x(1-x)} > 0$ for every real $x$, the sign of $f'$ equals the sign of $1 + x - 2x^2 = -(2x^2 - x - 1) = -(2x + 1)(x - 1)$.

Sign of $-(2x + 1)(x - 1)$:
- For $x < -1/2$: $(2x + 1) < 0$ and $(x - 1) < 0$, so $(2x + 1)(x - 1) > 0$, so $-(\cdot) < 0$, so $f'(x) < 0$. $f$ is *decreasing*.
- For $-1/2 < x < 1$: $(2x + 1) > 0$ and $(x - 1) < 0$, so $(2x + 1)(x - 1) < 0$, so $-(\cdot) > 0$, so $f'(x) > 0$. $f$ is *increasing*.
- For $x > 1$: both factors positive, so $(2x + 1)(x - 1) > 0$, so $-(\cdot) < 0$, so $f'(x) < 0$. $f$ is *decreasing*.

Hence $f$ is increasing on $[-1/2, 1]$ — option **(A)** is correct. $\blacksquare$

---

### Solution to 5.2 — Convex Quadrilateral with Diagonal Constraint

Set up coordinates: place the diagonal $AC$ along the $x$-axis, with $A$ at the origin and $C$ at $(p, 0)$ where $p = AC$. Since the quadrilateral $ABCD$ is convex, $B$ lies *above* the $x$-axis at $(x_B, y_B)$ with $y_B > 0$, and $D$ lies *below* at $(x_D, y_D)$ with $y_D < 0$.

*Side lengths and constraint.* WLOG suppose the constrained pair of opposite sides are $AB$ and $CD$, and the constrained diagonal is $AC$. Then $AB = \sqrt{x_B^2 + y_B^2}$, $CD = \sqrt{(x_D - p)^2 + y_D^2}$, and the constraint $AB + CD + AC = 16$ becomes
\[
  \sqrt{x_B^2 + y_B^2} + \sqrt{(x_D - p)^2 + y_D^2} + p \;=\; 16.
\]

*Area.* The area of the quadrilateral (decomposed into $\triangle ABC$ above the $x$-axis and $\triangle ACD$ below):
\[
  32 \;=\; [\text{Area } ABCD] \;=\; \tfrac{1}{2} p \cdot y_B + \tfrac{1}{2} p \cdot |y_D| \;=\; \tfrac{1}{2} p (y_B - y_D)
\]
(using $y_D < 0$ so $|y_D| = -y_D$). Hence $p (y_B - y_D) = 64$.

*Key inequality.* For each of the two sides, $AB \ge |y_B|$ (since $AB^2 = x_B^2 + y_B^2 \ge y_B^2$, so $AB \ge |y_B| = y_B$ for $y_B > 0$), with equality iff $x_B = 0$. Similarly $CD \ge |y_D| = -y_D$ with equality iff $x_D = p$.

Combining: $AB + CD \ge y_B + (-y_D) = y_B - y_D = 64 / p$. From the constraint: $AB + CD = 16 - p$. So
\[
  16 - p \;\ge\; \frac{64}{p} \quad\Longleftrightarrow\quad p(16 - p) \;\ge\; 64 \quad\Longleftrightarrow\quad p^2 - 16 p + 64 \;\le\; 0 \quad\Longleftrightarrow\quad (p - 8)^2 \;\le\; 0.
\]
This forces $p = 8$ *exactly*. The constraint is so tight that the diagonal $AC$ is *uniquely determined* by the data.

*Equality conditions for the inequality.* The inequality $AB \ge y_B$ is equality iff $x_B = 0$, i.e., $B$ lies directly above $A$. Similarly $x_D = p = 8$, i.e., $D$ lies directly below $C$.

So $B = (0, y_B)$ with $y_B = AB$, and $D = (8, y_D)$ with $|y_D| = CD$. From $y_B - y_D = 8$ and $AB + CD = 8$: $y_B + |y_D| = 8$ as well. The two are the same equation.

*Compute the other diagonal $BD$.*
\[
  BD^2 \;=\; (8 - 0)^2 + (y_D - y_B)^2 \;=\; 64 + (y_B - y_D)^2 \;=\; 64 + 64 \;=\; 128.
\]
\[
  \boxed{BD \;=\; 8\sqrt 2.}
\]

The minimum length of the other diagonal is exactly $8\sqrt 2$ — and the constraint is so tight that this is also the *only* achievable length (the constraints force every legitimate configuration to have $BD = 8\sqrt 2$). $\blacksquare$

---

### Solution to 5.3 — Minimum of Quadratic Forms

*(i) $f_1(x, y) = x^2 + 3y^2 - 6x - 2y$.*

Gradient zero: $\partial_x f_1 = 2x - 6 = 0 \Rightarrow x = 3$. $\partial_y f_1 = 6y - 2 = 0 \Rightarrow y = 1/3$.

Critical point: $(3, 1/3)$. Value:
\[
  f_1(3, 1/3) \;=\; 9 + 3 \cdot \tfrac{1}{9} - 18 - \tfrac{2}{3} \;=\; 9 + \tfrac{1}{3} - 18 - \tfrac{2}{3} \;=\; -9 - \tfrac{1}{3} \;=\; -\tfrac{28}{3}.
\]
Hessian: $\partial_{xx} = 2, \partial_{yy} = 6, \partial_{xy} = 0$; $\det H = 12 > 0$, $\partial_{xx} > 0$, so local min and (by positive-definiteness of the quadratic part) global min.

Verify by completing the square:
\[
  f_1 \;=\; (x - 3)^2 - 9 + 3\big(y - \tfrac{1}{3}\big)^2 - \tfrac{1}{3} \;=\; (x - 3)^2 + 3\big(y - \tfrac{1}{3}\big)^2 - \tfrac{28}{3}.
\]
Minimum: $\boxed{-\tfrac{28}{3}}$ at $(3, 1/3)$. ✓

*(ii) $f_2(x, y) = x^2 + 2xy + 3y^2 - 6x - 2y$.*

Gradient zero: $\partial_x f_2 = 2x + 2y - 6 = 0 \Rightarrow x + y = 3$. $\partial_y f_2 = 2x + 6y - 2 = 0 \Rightarrow x + 3y = 1$.

Subtracting: $-2y = 2 \Rightarrow y = -1$. Then $x = 3 - y = 4$. Critical point: $(4, -1)$.

Value:
\[
  f_2(4, -1) \;=\; 16 + 2 \cdot 4 \cdot (-1) + 3 \cdot 1 - 24 - (-2) \;=\; 16 - 8 + 3 - 24 + 2 \;=\; -11.
\]
Hessian: $\partial_{xx} = 2, \partial_{yy} = 6, \partial_{xy} = 2$; $\det H = 12 - 4 = 8 > 0$, $\partial_{xx} > 0$, so local min (and by positive-definiteness, global).

Verify by completing the square. Set $u = x + y$ (the cross-term $2xy$ suggests this substitution): $x = u - y$, so
\begin{align*}
  f_2
  &= (x^2 + 2xy + y^2) + 2y^2 - 6x - 2y \\
  &= (x + y)^2 + 2y^2 - 6(u - y) - 2y \\
  &= u^2 + 2y^2 - 6u + 6y - 2y \\
  &= u^2 - 6u + 2y^2 + 4y \\
  &= (u - 3)^2 - 9 + 2(y + 1)^2 - 2 \\
  &= (u - 3)^2 + 2(y + 1)^2 - 11.
\end{align*}
Minimum: $\boxed{-11}$ at $u = 3, y = -1$, i.e., $(x, y) = (4, -1)$. ✓

*Correction note.* The locked slate v0.2 stated the minimum of $f_2$ as $-13/2$ at $(7/2, -1/2)$. This is wrong: the point $(7/2, -1/2)$ does *not* satisfy the gradient-zero conditions ($\partial_x f_2|_{(7/2, -1/2)} = 7 - 1 - 6 = 0$ — actually this does check out — let me recompute. $\partial_x f_2 = 2x + 2y - 6 = 2(7/2) + 2(-1/2) - 6 = 7 - 1 - 6 = 0$. ✓ $\partial_y f_2 = 2x + 6y - 2 = 7 - 3 - 2 = 2 \ne 0$. ✗). So $(7/2, -1/2)$ fails the $\partial_y$ condition, confirming the slate is wrong. The correct critical point and value are $(4, -1)$ and $-11$, as derived. Slate patched in v0.2.9.

---

### Solution to 5.4 — Largest Rectangle in a Semicircle

Place the semicircle as the upper half of $\{(x, y) : x^2 + y^2 \le R^2\}$ (i.e., $y \ge 0$), with the diameter along the $x$-axis from $(-R, 0)$ to $(R, 0)$.

A rectangle with one side on the diameter has its base on the $x$-axis and its two upper corners on the semicircle. By symmetry, the optimal rectangle is centred on the $y$-axis, with upper corners at $(\pm R\cos\theta, R\sin\theta)$ for some $\theta \in [0, \pi/2]$.

*Dimensions and area.* Width $= 2 R\cos\theta$; height $= R\sin\theta$. Area:
\[
  A(\theta) \;=\; (2 R\cos\theta)(R\sin\theta) \;=\; 2 R^2 \sin\theta\cos\theta \;=\; R^2 \sin 2\theta.
\]

*Maximise.* $\sin 2\theta$ is maximised at $2\theta = \pi/2$, i.e., $\theta = \pi/4$. Maximum value: $\sin(\pi/2) = 1$, so $A_{\max} = R^2 \cdot 1 = R^2$.

*Dimensions at maximum.* At $\theta = \pi/4$: width $= 2 R \cos(\pi/4) = 2 R / \sqrt 2 = R\sqrt 2$; height $= R\sin(\pi/4) = R/\sqrt 2$.

\[
  \boxed{\text{Sides } R\sqrt 2 \text{ and } R/\sqrt 2; \text{ area } R^2.}
\]
$\blacksquare$

The structural insight: the *single-parameter* trigonometric formulation $A(\theta) = R^2 \sin 2\theta$ converts the rectangle optimisation into the trivial maximisation of $\sin$. The *symmetry assumption* (rectangle centred on the perpendicular bisector of the diameter) is verified by the elementary observation that any asymmetric rectangle can be replaced by its symmetric counterpart with the same dimensions and the same area, but better centred.

---

### Solution to 5.5 — Snell's Law via Fermat's Principle

Let the light path cross the $x$-axis at the point $(x, 0)$. The total path length consists of two segments: from $A = (0, a)$ to $(x, 0)$ above, traversed at speed $v_1$, and from $(x, 0)$ to $B = (d, -b)$ below, traversed at speed $v_2$.

*Total time.*
\[
  T(x) \;=\; \frac{\sqrt{x^2 + a^2}}{v_1} + \frac{\sqrt{(d - x)^2 + b^2}}{v_2}.
\]

*Fermat's principle (extremum).* The light follows the path of *minimum* total time. Setting $T'(x) = 0$:
\[
  T'(x) \;=\; \frac{x}{v_1 \sqrt{x^2 + a^2}} - \frac{(d - x)}{v_2 \sqrt{(d - x)^2 + b^2}} \;=\; 0.
\]

*Geometric interpretation.* Let $\theta_1$ be the angle between the incoming light path and the normal to the $x$-axis (the $y$-axis direction). At the point $(x, 0)$, the incoming path's slope is $(a - 0)/(0 - x) = -a/x$ (from $(0, a)$ to $(x, 0)$); the direction along the path is $(x, -a)/\sqrt{x^2 + a^2}$. The angle from the negative-$y$-direction (normal pointing down) to the path-direction satisfies $\sin\theta_1 = x / \sqrt{x^2 + a^2}$. (Think: the horizontal component of the path direction is $x/\sqrt{x^2+a^2}$; this is $\sin\theta_1$.)

Similarly, the outgoing path from $(x, 0)$ to $(d, -b)$ has direction $(d - x, -b)/\sqrt{(d-x)^2 + b^2}$, and the angle from the normal satisfies $\sin\theta_2 = (d - x)/\sqrt{(d-x)^2 + b^2}$.

*Fermat's equation:*
\[
  \frac{\sin\theta_1}{v_1} \;=\; \frac{\sin\theta_2}{v_2} \quad\Longleftrightarrow\quad \boxed{\frac{\sin\theta_1}{\sin\theta_2} \;=\; \frac{v_1}{v_2}.}
\]
This is *Snell's law of refraction*. $\blacksquare$

*Physical interpretation.* The ratio $v_1 / v_2$ equals the ratio of refractive indices $n_2 / n_1$ (since $v_i = c / n_i$). Snell's law in optics is conventionally written $n_1 \sin\theta_1 = n_2 \sin\theta_2$, which is the same equation rearranged. *Fermat's principle gives Snell's law*; equivalently, *Snell's law is the first-order necessary condition of the variational problem $\min T$*.

---

### Solution to 5.6 — Cotangent-Sum Minimum

With $\theta_1 + \theta_2 = \pi/2$, substitute $\theta_2 = \pi/2 - \theta_1$. Then $\cot\theta_2 = \cot(\pi/2 - \theta_1) = \tan\theta_1$.

The objective becomes
\[
  F(\theta_1) \;=\; \cot\theta_1 + \tan\theta_1.
\]

*Apply AM-GM* (both $\cot\theta_1$ and $\tan\theta_1$ are positive for $\theta_1 \in (0, \pi/2)$):
\[
  \cot\theta_1 + \tan\theta_1 \;\ge\; 2 \sqrt{\cot\theta_1 \cdot \tan\theta_1} \;=\; 2 \sqrt{1} \;=\; 2,
\]
with equality iff $\cot\theta_1 = \tan\theta_1$, i.e., $\tan^2\theta_1 = 1$, i.e., $\theta_1 = \pi/4$. Then $\theta_2 = \pi/2 - \pi/4 = \pi/4$.

Minimum: $\boxed{2}$ at $\theta_1 = \theta_2 = \pi/4$. $\blacksquare$

*Symmetry interpretation.* The function and the constraint are symmetric under $\theta_1 \leftrightarrow \theta_2$; the symmetric extremum at $\theta_1 = \theta_2 = \pi/4$ realises the minimum. This is the Form III (symmetric extremum) instance — a clean illustration of the symmetry-extremum principle.

*Cross-archetype connection.* This problem reframes Ch. 2 (Symmetry) PP4 from the *extremum* side: there, the symmetry was used to *force* the symmetric configuration; here, the extremum principle *locates* the configuration at the symmetric point. The two framings give the same answer through complementary lenses.

---

### Solution to 5.7 — Erdős-Mordell Inequality

We outline the classical proof using reflections (the elegant proof; alternative proofs use Ptolemy's inequality or the Cauchy-Schwarz inequality on the trigonometric expansion of the distances).

*Setup.* Let $P$ be inside $\triangle ABC$. Reflect $P$ across each side: let $P_a, P_b, P_c$ be the reflections of $P$ across $BC, CA, AB$ respectively. Then $PP_a = 2 d_a$ (twice the perpendicular distance), and similarly $PP_b = 2 d_b$, $PP_c = 2 d_c$.

*Key geometric identity (from a triangle-inequality argument).* Reflect $A$ across line $BC$ as $A'$; then $AA' = 2 h_A$ where $h_A$ is the altitude from $A$. The reflections of $P$ across the three sides yield three new points, and the triangle inequality on certain configurations gives the bound $p_a + p_b + p_c \ge 2(d_a + d_b + d_c)$.

*Classical Bankoff / Komornik–style proof sketch.* For each vertex, the distance from $P$ to the vertex is bounded below by a weighted sum of pedal-distances. Specifically, one proves
\[
  p_a \;\ge\; \frac{c \cdot d_c + b \cdot d_b}{a}, \quad p_b \;\ge\; \frac{a \cdot d_a + c \cdot d_c}{b}, \quad p_c \;\ge\; \frac{a \cdot d_a + b \cdot d_b}{c},
\]
by trigonometric / reflection arguments. Summing these three inequalities:
\[
  p_a + p_b + p_c \;\ge\; d_a \left(\frac{b}{c} + \frac{c}{b}\right) + d_b \left(\frac{a}{c} + \frac{c}{a}\right) + d_c \left(\frac{a}{b} + \frac{b}{a}\right).
\]
By AM-GM, each parenthesised sum is $\ge 2$. Hence
\[
  p_a + p_b + p_c \;\ge\; 2(d_a + d_b + d_c),
\]
as required.

*Equality conditions.* Equality in AM-GM requires $b = c, a = c, a = b$ — i.e., $a = b = c$, equilateral. Equality in the trigonometric bounds requires $P$ at the *symmetric* point of the equilateral triangle — i.e., the centroid (= incentre = circumcentre = orthocentre in an equilateral). $\blacksquare$

The Erdős-Mordell inequality is the prototype of a *geometric extremal inequality*: a relationship between two geometric quantities (vertex-distances and pedal-distances) where the bound is *sharp* and attained only at the *symmetric* configuration (equilateral). The proof combines *reflection* (a Form-I cross-archetype with substitution), *trigonometric bounds* (Form III symmetric extremum), and *AM-GM* (Form IV inequality-equality-case). It is a fitting closing problem for the *Constraint Exploitation* sub-pillar.

---

*End of Chapter 12. End of the Constraint Exploitation sub-pillar (Chapters 9–12).*

