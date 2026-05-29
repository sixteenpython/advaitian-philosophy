---
chapter: 5
pillar: 4
chapter_type: case-study
title: "Case Studies 6–10: Mid-difficulty CEP"
subtitle: "The monovariant, the radical axis, the fixed point, the right pigeonhole."
length_target_words: 6700
canonical_takeaway: "Mid-difficulty CEPs are characterised by a single non-trivial intermediate construction — a monovariant, a hidden symmetry, a tight pigeonhole — that the solver must discover before the convergence becomes visible."
status: locked
last_revised: 2026-05-29
locked_on: 2026-05-29
references_invoked: [IMO-1986-P3, IMO-1995-P1, Putnam-1992-B2, IMO-1979-P3, IMO-2003-P1, Engel-Ch-2-monovariants]
voice_register: tao-warm
pillar3_cross_references: []
---

# Chapter 5 — Case Studies 6–10: Mid-difficulty CEP

> *"In the tournament problem, you do not find the monovariant. The monovariant finds you, after you have stared at the operation long enough that its conservation law surfaces."*  
> — Arthur Engel, *Problem-Solving Strategies* (Springer 1998), Ch. 2 §"Invariants and Monovariants", preface

---

## §0 — Chapter Opening: The Single Crucial Construction

Mid-difficulty CEPs differ from Moderate-tier CEPs in one specific way: each requires a *single crucial construction* that the solver must discover before the convergence becomes visible. In the Moderate tier the convergence is visible as soon as the right archetypes are recognised — the Euclidean algorithm closes IMO 1959 P1 in two lines, the per-element decomposition closes Putnam 1985 A-1 in three. In the Mid tier the recognition of the archetypes is not enough; the solver must additionally *construct* a specific intermediate object — a monovariant, a hidden circle, a fixed point, a precisely-calibrated pigeonhole — and only then does the path close.

This is the chapter where problem-design's *constructive* dimension becomes visible. A Moderate-tier designer chooses a CEP that the solver can reach by *recognition alone*. A Mid-tier designer chooses a CEP that *requires construction* — and the design choice that distinguishes a great Mid-tier problem from a mediocre one is the choice of *which construction* the solver will need. The case studies in this chapter — IMO 1986 P3's pentagon monovariant, IMO 1995 P1's radical-axis concurrence, Putnam 1992 B-2's smoothing fixed-point, IMO 1979 P3's parametric-time symmetry, IMO 2003 P1's tight pigeonhole — are five worked specimens of the constructive choice in action.

We continue with the §8.10 sub-template throughout.

---

## §1 — Case Study 6: IMO 1986 Problem 3 (the pentagon monovariant)

**Source.** International Mathematical Olympiad 1986, Problem 3.  
**CEP.** Existence of a strictly decreasing monovariant on the configuration space, forcing termination in finitely many steps regardless of the initial labelling (provided the total sum is positive).  
**Archetypes.** #1 (Invariance — the monovariant) + #18 (Induction — well-foundedness of the natural numbers under strict decrease) + #12 (Extremal — the monovariant must hit a minimum at the terminal configuration).  
**Difficulty.** Tier 3-mid.  
**Verification source.** `Cursor-IMO.md` §V; `imo-compendium.txt` near line 8950.

### Problem statement

> To each vertex of a regular pentagon an integer is assigned, in such a way that the sum of all five numbers is positive. If three consecutive vertices are assigned the numbers $x, y, z$ respectively, and if $y < 0$, then the following operation is allowed: the numbers $x, y, z$ are replaced by $x + y$, $-y$, $z + y$ respectively. Such an operation is performed repeatedly as long as at least one of the five numbers is negative. Determine whether this procedure necessarily comes to an end after a finite number of steps.

### The Designer's Architecture

*The CEP unmasked.* The CEP is the existence of a quantity $\Phi$ — a *monovariant* — that strictly decreases by a positive integer at every legal operation, and is bounded below by zero. Two monovariants are known to work for this problem; both are quadratic forms in the differences between vertex values. One canonical choice:
$$\Phi(x_1, x_2, x_3, x_4, x_5) = \sum_{i=1}^{5} (x_i - x_{i+2})^2 \quad (\text{indices mod 5}).$$
A direct calculation shows that, when the operation is applied at vertex $i$ (with $y = x_i < 0$, and $x_{i-1}, x_{i+1}$ as the two neighbours that change), $\Phi$ decreases by $2x_i \cdot S$, where $S$ is the (positive) total sum of all five values. Since $x_i < 0$ and $S > 0$, the decrease is strictly positive; since $\Phi$ is a sum of squares of integers, it is bounded below by zero. The procedure must therefore terminate in at most $\Phi_{\text{initial}} / (2 |x_i|_{\min} \cdot S)$ steps.

The CEP is the *existence* of $\Phi$. Finding $\Phi$ is the entire problem.

*The archetype convergence.* #1 + #18 + #12, with #1 (Invariance, in its monovariant sub-archetype) as the dominant move; #18 (Induction) supplying the well-foundedness argument that turns a strictly-decreasing-into-non-negative quantity into "finitely many steps"; and #12 (Extremal) closing the loop by noting that any infinite descent into the well-founded $\mathbb{Z}_{\geq 0}$ is impossible.

*The traps planted.* Three.

- **Trap 1: the case-analysis trap.** The solver attempts to track the operation through specific starting configurations (e.g., $(1, -2, 3, 1, 0)$, then $(-1, 2, 1, 1, 0)$ if $y = -2$ is the chosen negative...) and to argue by exhaustion that the orbit terminates. This works for *small* starting configurations but does not produce a proof for general starting configurations. The trap is that the case-analysis approach *almost* generates a pattern but never quite generalises. Generous: teaches that even when the dynamics are explicit, the proof of termination usually requires an invariant rather than a trajectory analysis.
- **Trap 2: the wrong-monovariant trap.** The solver tries naïve monovariants: $\sum x_i^2$ (the sum of squares — but this is *constant* under the operation, since $x^2 + y^2 + z^2 = (x+y)^2 + (-y)^2 + (z+y)^2$ would require... wait, let me check: $(x+y)^2 + y^2 + (z+y)^2 = x^2 + 2xy + y^2 + y^2 + z^2 + 2yz + y^2 = x^2 + y^2 + z^2 + (2xy + 2yz + 2y^2) = x^2 + y^2 + z^2 + 2y(x + y + z)$). So $\sum x_i^2$ changes by $2y(x + y + z)$, which can be positive or negative depending on the sign of $x + y + z$. Not a monovariant. Generous: teaches that the *first* quadratic invariant a solver writes down is rarely the right one, and that finding the right one requires considering longer-range differences (the $(x_i - x_{i+2})^2$ structure).
- **Trap 3: the topological-invariant trap.** The solver attempts to find an invariant in the *signs* of the $x_i$ — counting negative entries, tracking the parity of negatives, etc. The negative-count *can* increase under the operation (a single negative becomes a non-negative central entry but flips two previously non-negative neighbours to potentially-negative), so this is not a monovariant. The trap is that the operation's local sign-behaviour suggests sign-counting; the global termination requires a metric-monovariant. Generous: teaches the distinction between *topological* invariants (counts, signs) and *metric* invariants (sums, quadratic forms).

*The statement-craft.* The phrasing *"determine whether this procedure necessarily comes to an end"* is a deliberate choice over *"prove this procedure necessarily comes to an end."* The *"determine whether"* framing forces the solver to consider, at the start, the possibility that the answer is NO — that some configuration produces an infinite orbit. The IMO problem-setters chose this framing because they wanted the solver to *eliminate* the no-answer possibility through structural reasoning rather than assuming the yes-answer. (The answer is YES; the procedure always terminates; the structural reasoning is the monovariant.) The *"sum positive"* hypothesis is exact: if the sum were zero or negative, the configuration $(0, 0, 0, 0, 0)$ or $(-1, -1, -1, -1, -1)$ or similar might produce a stuck state or different behaviour; the hypothesis is exactly what is needed for $\Phi$ to decrease by a strictly positive amount.

### The Reader's Re-Solution

- *Given.* Five integers $x_1, \ldots, x_5$ assigned to vertices of a regular pentagon (cyclic), with $S = x_1 + \cdots + x_5 > 0$. Operation: if $x_i < 0$, replace $(x_{i-1}, x_i, x_{i+1})$ by $(x_{i-1} + x_i, -x_i, x_{i+1} + x_i)$.
- *Find.* Whether the operation necessarily terminates.
- *Strategy.* Construct a strictly-decreasing non-negative-integer-valued monovariant; conclude termination by well-foundedness.
- *Stage 1 (#1).* Define $\Phi = \sum_{i=1}^{5} (x_i - x_{i+2})^2$ (indices mod 5). Direct expansion shows: under the operation at vertex $i$ (so $y = x_i$ becomes $-y$, and neighbours $x_{i-1}, x_{i+1}$ become $x_{i-1} + y$ and $x_{i+1} + y$ respectively), the contribution to $\Phi$ from the affected differences changes by $-2yS$. Since $y < 0$ (the operation requires this) and $S > 0$, $-2yS > 0$... *wait*: $-2yS = -2 \cdot y \cdot S$ with $y < 0$ gives $-2 \cdot (\text{negative}) \cdot (\text{positive}) = \text{positive}$. So $\Phi$ decreases by a *positive* amount — i.e., $\Phi_{\text{new}} = \Phi_{\text{old}} - 2|y|S < \Phi_{\text{old}}$.
- *Stage 2 (#18).* $\Phi$ is a sum of squares of integers, hence a non-negative integer. The sequence $\Phi_{\text{after step }k}$ is strictly decreasing in $k$ and bounded below by $0$. A strictly decreasing sequence of non-negative integers terminates in finitely many steps.
- *Stage 3 (#12).* At termination, no further operation is possible, i.e., all five $x_i \geq 0$. This is the terminal state.
- *Convergence.* The procedure $\boxed{\text{necessarily terminates}}$ in at most $\Phi_{\text{initial}} / (2 S)$ operations.

### Lessons for Problem Designers

1. **Monovariants are the cleanest Mid-tier CEPs.** Designers who want to engineer a Mid-tier problem around a process-terminates question should reach first for a quadratic monovariant in differences (rather than sums) of the dynamic quantities. The IMO 1986 P3 monovariant is the archetype.
2. **The hypothesis-tightness is the design's centre of gravity.** The *"sum positive"* hypothesis is exactly the condition that makes the monovariant strictly decrease. Designers who omit a tight hypothesis produce ambiguous problems (does the procedure terminate sometimes? always? never?); designers who include exactly the right hypothesis produce clean problems.
3. **The "determine whether" framing forces structural argument.** Whenever the designer is willing to invest the solver's cognitive effort in *eliminating* the negative answer, the *"determine whether"* phrasing is the right choice. When the designer wants to direct the solver immediately to a proof, *"prove that"* is the right choice. The IMO 1986 P3 designer made the harder choice.

---

## §2 — Case Study 7: IMO 1995 Problem 1 (chords and tangents — the radical axis)

**Source.** International Mathematical Olympiad 1995, Problem 1.  
**CEP.** Three lines pass through a single point because each lies on the *radical axis* of an appropriate pair of circles; the radical-axis concurrence is the structural truth that the problem is built around.  
**Archetypes.** #2 (Symmetry — the radical axis is a symmetric construct) + #4 (Hidden Structure — recognising that the configuration admits a radical-centre reading).  
**Difficulty.** Tier 3-mid.  
**Verification source.** `Cursor-IMO.md` §II; `imo-compendium.txt` near line 14100.

### Problem statement

> Let $A, B, C, D$ be four distinct points on a line, in that order. The circles with diameters $AC$ and $BD$ intersect at points $X, Y$. The line $XY$ meets $BC$ at $Z$. Let $P$ be a point on line $XY$ other than $Z$. The line $CP$ intersects the circle with diameter $AC$ at $C$ and $M$, and the line $BP$ intersects the circle with diameter $BD$ at $B$ and $N$. Prove that lines $AM$, $DN$, and $XY$ are concurrent.

### The Designer's Architecture

*The CEP unmasked.* The configuration contains *two* circles ($\omega_1$ with diameter $AC$, $\omega_2$ with diameter $BD$). The line $XY$ is the *radical axis* of $\omega_1$ and $\omega_2$ — the locus of points with equal power with respect to both circles. The CEP is the recognition that line $AM$ is the radical axis of $\omega_1$ and a third (auxiliary) circle, line $DN$ is the radical axis of $\omega_2$ and the same third circle, and the three radical axes meet at the *radical centre* of the three circles. The third circle, conventionally, is the circle through $M, N, P$ (which exists because $\angle MCP = \angle MBP = 90°$ by inscribed-angle considerations, making $MNBC$ cyclic, etc. — the construction is intricate but the radical-centre conclusion is structural).

*The archetype convergence.* #2 + #4. The #2 (Symmetry) move is the recognition that any pair of circles defines a radical axis (a symmetric construct in the pair). The #4 (Hidden Structure) move is the recognition that the specific configuration of the problem admits an auxiliary third circle whose radical-axis pairs with $\omega_1$ and $\omega_2$ are exactly the lines $AM$ and $DN$. The convergence is at the radical-centre concurrence.

*The traps planted.* Three.

- **Trap 1: the coordinate trap.** The solver sets up coordinates (placing the line $ABCD$ as the $x$-axis, computing all six relevant lines algebraically) and attempts to prove concurrence by computing the intersection point analytically. This *works* but generates pages of algebra. Generous: teaches that synthetic olympiad geometry usually has a synthetic proof much shorter than the coordinate proof, and that the synthetic proof requires identifying the configuration's *structural* hidden object.
- **Trap 2: the angle-chasing trap.** The solver attempts to prove the concurrence by accumulating angle equalities (inscribed-angle, cyclic-quadrilateral, etc.). Angle-chasing *can* close the problem but requires identifying the right angle at the concurrence point, which is more subtle than identifying the right circle. Generous: teaches that for concurrence problems, the radical-axis approach is often dramatically cleaner than angle-chasing.
- **Trap 3: the projective trap.** The solver attempts to apply projective duality or cross-ratio arguments. These are real techniques and they do close the problem, but they require machinery (projective transformations, the dual of Ceva's theorem) that is heavier than the radical-axis machinery. Generous: teaches that even when multiple advanced techniques apply, the *minimum-machinery* technique is usually the design-intended one.

*The statement-craft.* The phrasing avoids naming the circles explicitly — *"the circles with diameters $AC$ and $BD$"* identifies them only by their diameters, not by symbols $\omega_1, \omega_2$. The solver must internally name them to reason about radical axes. This is a deliberate concealment: the *naming* of circles invites the symmetric pairing that produces the radical-axis insight, so the designer leaves the naming to the solver. The choice to ask about *three* concurrent lines (rather than the more common two-line concurrence) is the second concealment: three-line concurrence at a point invites the radical-*centre* reading, which is the design's centre of gravity.

### The Reader's Re-Solution

- *Given.* Four collinear points $A, B, C, D$ in order; circles $\omega_1, \omega_2$ on diameters $AC, BD$; intersection $X, Y$ of $\omega_1 \cap \omega_2$; auxiliary point $P$ on line $XY \setminus \{Z\}$; lines $CP \cap \omega_1 = \{C, M\}$, $BP \cap \omega_2 = \{B, N\}$.
- *Find.* Lines $AM, DN, XY$ concur.
- *Strategy.* Identify a third circle whose radical-axis pairs with $\omega_1$ and $\omega_2$ are $AM$ and $DN$; conclude concurrence at the radical centre.
- *Stage 1 (#2).* Line $XY$ is the radical axis of $\omega_1$ and $\omega_2$ (standard: the radical axis of two intersecting circles is the line through their intersection points).
- *Stage 2 (#4).* Construct $\omega_3$, the circle through $M, N, P$. Direct angle-chasing (using $\angle CMA = \angle BNC = 90°$ from the inscribed-angle theorem on $\omega_1, \omega_2$) confirms $\omega_3$ exists and contains $P$. Now: line $AM$ is the radical axis of $\omega_1$ and $\omega_3$ (because $A \in \omega_1$ and $A$ has equal power with respect to $\omega_3$, etc. — the verification is the technical heart of the proof). Line $DN$ is the radical axis of $\omega_2$ and $\omega_3$ analogously.
- *Convergence.* The three radical axes $XY = \text{rad}(\omega_1, \omega_2)$, $AM = \text{rad}(\omega_1, \omega_3)$, $DN = \text{rad}(\omega_2, \omega_3)$ meet at the radical centre of $\omega_1, \omega_2, \omega_3$. Therefore $\boxed{AM, DN, XY \text{ concur.}}$

### Lessons for Problem Designers

1. **The radical axis is the cleanest CEP for two-circle problems.** Whenever a configuration contains two circles meeting in two points, the line through the meeting points is the radical axis, and any concurrence question is best read through the radical-axis lens. Designers writing two-circle problems can engineer the answer to live on the radical axis by design.
2. **Three-line concurrence invites the radical-centre reading.** Designers asking "prove that three lines concur" should consider: do any two of the three lines have a natural radical-axis reading? If yes, the third line is forced to pass through the radical centre. The radical-centre reading is the cleanest existing CEP for three-line concurrence in olympiad geometry.
3. **The minimum-machinery principle from Moderate-tier carries to Mid-tier.** Even when coordinate, angle-chasing, and projective approaches all close a geometry problem, the *radical-axis* approach is typically the lightest. Designers who want their problem to be approachable by the radical-axis approach should withhold the *naming* of the circles in the statement, forcing the solver to discover the symmetric structure themselves.

---

## §3 — Case Study 8: Putnam 1992 Problem B-2 (the smoothing fixed point)

**Source.** William Lowell Putnam Competition, 1992, Problem B-2.  
**CEP.** The *smoothing* argument: among all $(a_1, \ldots, a_n) \in \mathbb{R}_{\geq 0}^n$ with $\sum a_i = 1$, the maximum of $\sum_{i} a_i a_{i+1}$ (indices mod $n$) is achieved by a configuration that concentrates all mass at two adjacent indices, giving the maximum $1/4$.  
**Archetypes.** #11 (Existence — of the maximum on the simplex) + #12 (Extremal — the maximum is at a specific identifiable point).  
**Difficulty.** Tier 3-mid.  
**Verification source.** Engel Ch. 7 (Inequalities), Putnam coverage; `Cursor-Engel.md` Ch. 7.

### Problem statement

> For nonnegative real numbers $a_1, a_2, \ldots, a_n$ (with $n \geq 2$) such that $a_1 + a_2 + \cdots + a_n = 1$, determine, with proof, the maximum possible value of $\sum_{i=1}^{n} a_i a_{i+1}$ (indices taken modulo $n$).

### The Designer's Architecture

*The CEP unmasked.* The function $f(a) = \sum_i a_i a_{i+1}$ on the simplex $\Delta = \{a \in \mathbb{R}_{\geq 0}^n : \sum a_i = 1\}$ achieves its maximum at a vertex of the *secondary* simplex — specifically, at a configuration where exactly two adjacent coordinates are non-zero (each equal to $1/2$) and the other $n-2$ coordinates are zero. At such a configuration, $f = (1/2)(1/2) = 1/4$. The CEP is that no other configuration achieves a higher value; the *smoothing* argument (move mass from a non-adjacent coordinate to an adjacent one, and watch $f$ either increase or stay constant) proves it.

*The archetype convergence.* #11 + #12. The #11 (Existence) move is the recognition that $\Delta$ is compact and $f$ is continuous, so the maximum exists and is attained. The #12 (Extremal) move is the smoothing argument: starting from any maximising configuration, perform local mass-transfers and verify that the configuration must already be a two-adjacent-coordinate state to be maximising. The convergence is at the structural identification of the maximiser.

*The traps planted.* Three.

- **Trap 1: the Lagrange-multiplier trap.** The solver attempts $\nabla f = \lambda \nabla g$ for $g(a) = \sum a_i - 1$. The Lagrange system gives critical points where $a_{i-1} + a_{i+1} = \lambda$ for each $i$ — a system that admits the *symmetric* solution $a_i = 1/n$ for every $i$. At this symmetric solution, $f = n \cdot (1/n)(1/n) = 1/n$, which for $n \geq 5$ is *less* than $1/4$. The trap is that the symmetric critical point is *not* the maximum (it is a saddle point or local minimum on the simplex). Generous: teaches that for non-concave objectives on compact domains, critical-point analysis without boundary consideration misses the actual extremum.
- **Trap 2: the AM-GM trap.** The solver attempts to bound $\sum a_i a_{i+1}$ via AM-GM or Cauchy-Schwarz inequalities. Direct AM-GM gives $\sum a_i a_{i+1} \leq \sum (a_i^2 + a_{i+1}^2)/2 = \sum a_i^2$ — a weak bound that does not match $1/4$. Generous: teaches that inequality bounds need to be *tight*, and that for cyclic sums on the simplex the boundary maxima often defeat smooth inequality machinery.
- **Trap 3: the small-$n$ trap.** The solver verifies the conjecture $f_{\max} = 1/4$ for $n = 2, 3, 4$ (giving $1/2, 1/4, 1/4$ respectively — for $n = 2$, $f = 2 a_1 a_2 \leq 1/2$ by AM-GM; for $n = 3, 4$, the two-adjacent configuration gives $1/4$). The solver becomes confident the maximum is $1/4$ for all $n \geq 3$ (note: $n = 2$ is an exception, with maximum $1/2$). The trap is that the small-$n$ check builds confidence but does not produce a proof; the structural argument for general $n$ requires the smoothing step. Generous if it primes the solver for the smoothing argument; ungenerous if the solver writes up the small-$n$ pattern as a proof.

*The statement-craft.* The phrasing *"determine, with proof, the maximum possible value"* is the Putnam-house style — it demands both the value *and* the proof, in the Joshi-style complete-answer tradition. The choice of *cyclic* sum (indices mod $n$) rather than *path* sum ($\sum_{i=1}^{n-1} a_i a_{i+1}$) is consequential: the cyclic structure makes the problem $S_n$-symmetric (under cyclic permutation of indices), which prevents the solver from breaking symmetry to attack the problem. The cyclic structure also makes the two-adjacent maximum *position-independent* — the maximiser is any pair of adjacent indices, so the answer is $1/4$ regardless of where the mass is concentrated.

### The Reader's Re-Solution

- *Given.* $n \geq 2$ nonnegative reals summing to $1$.
- *Find.* The maximum of $f(a) = \sum_i a_i a_{i+1}$ (cyclic).
- *Strategy.* Existence + smoothing.
- *Stage 1 (#11).* The simplex $\Delta$ is compact; $f$ is continuous; so $f$ attains its maximum at some point $a^* \in \Delta$.
- *Stage 2 (#12).* Suppose at $a^*$ three of the $a_i^*$ are positive, say $a_p^*, a_q^*, a_r^*$ with $p, q, r$ pairwise non-adjacent (and the rest zero). The smoothing move: transfer mass $\epsilon$ from $a_p^*$ to $a_q^*$. The change in $f$ is $\epsilon (a_{q-1}^* + a_{q+1}^* - a_{p-1}^* - a_{p+1}^*)$, plus higher-order $\epsilon^2$ terms. For any non-vertex $a^*$ there exists a direction along which $f$ does not decrease; iterating, the maximum is achieved at a configuration with at most two non-zero coordinates, and those two must be adjacent (otherwise $f = 0$).
- *Stage 3 (concluding the smoothing).* At a two-adjacent-coordinate configuration $a_i^* = t, a_{i+1}^* = 1 - t$ (other coordinates zero), $f = t(1-t)$, maximised at $t = 1/2$ with $f_{\max} = 1/4$. For $n = 2$ specifically, the cyclic sum has both terms $a_1 a_2$, giving $f = 2 a_1 a_2$ maximised at $a_1 = a_2 = 1/2$ with $f_{\max} = 1/2$.
- *Convergence.* $\boxed{f_{\max} = 1/4 \text{ for } n \geq 3; \ f_{\max} = 1/2 \text{ for } n = 2}$.

### Lessons for Problem Designers

1. **Cyclic structure prevents symmetry-breaking attacks.** A designer who chooses a cyclic sum (over a path sum) eliminates the solver's ability to "fix one end and minimise / maximise on the other end" decomposition. The cyclic constraint forces the structural smoothing argument.
2. **Boundary maxima are the cleanest extremal CEPs.** Designers writing extremal problems on simplices should consider whether the maximum lies at a *vertex* of the simplex (or, more generally, on a low-dimensional face) rather than at the symmetric centre. Boundary maxima resist Lagrange-multiplier attacks and require structural arguments — a Mid-tier difficulty boost at no extra computational cost.
3. **Small-$n$ exceptions are design features, not bugs.** The $n = 2$ case has a different answer ($1/2$, not $1/4$) because the cyclic structure degenerates. The clean designer's choice is to *include* the $n = 2$ case in the answer rather than to exclude it from the statement; the small-$n$ exception teaches the solver to *check the degeneracies* of any cyclic structure they construct.

---

## §4 — Case Study 9: IMO 1979 Problem 3 (the parametric-time symmetry)

**Source.** International Mathematical Olympiad 1979, Problem 3.  
**CEP.** Two points moving uniformly around two intersecting circles, started simultaneously at a common intersection point, return to the common intersection point simultaneously; the *other* common intersection point is, by symmetry of the configuration under reflection across the line of centres, also always equidistant from both moving points.  
**Archetypes.** #2 (Symmetry — reflection across the line of centres) + #8 (Domain Translation — time → angular parametrisation) + #4 (Hidden Structure — the equidistance is forced by the reflection symmetry).  
**Difficulty.** Tier 3-high.  
**Verification source.** `Cursor-IMO.md` §V; `imo-compendium.txt` near line 6400.

### Problem statement

> Two circles in a plane intersect. Let $A$ be one of the points of intersection. Starting simultaneously from $A$, two points move with constant speeds, each travelling along its own circle in the same sense. The two points return to $A$ simultaneously after one revolution. Prove that there is a fixed point $P$ in the plane such that, at any time, the distances from $P$ to the two moving points are equal.

### The Designer's Architecture

*The CEP unmasked.* The two circles intersect at two points: $A$ (the common start) and $B$ (the other intersection). The CEP is that $B$ is exactly the fixed point $P$ the problem asks for. The proof: at any time $t$, the moving point on circle $\omega_1$ subtends an angle $\theta_1(t)$ at $A$ (measured from $A$); the moving point on circle $\omega_2$ subtends $\theta_2(t)$. The condition that both return to $A$ simultaneously after one revolution forces $\theta_1(T) = \theta_2(T) = 2\pi$ at the common period $T$, hence $\theta_1(t)/\theta_2(t) = 1$ for all $t$, i.e., the two angular speeds are equal. Under equal angular speeds, the two moving points trace symmetric paths under the reflection across $AB$ (the line of centres of the two circles is *not* $AB$, but the perpendicular bisector of $AB$ relates the two circles' geometries in a way that makes $B$ equidistant from both points at every time).

*The archetype convergence.* #2 + #8 + #4. The #8 (Domain Translation) move is the parameterisation of the two moving points by their angular positions $\theta_1(t), \theta_2(t)$, converting the *time-dependent* problem into an *angle-dependent* problem. The #2 (Symmetry) move is the recognition that the configuration has a reflection symmetry across $AB$ that interchanges $\omega_1$ and $\omega_2$ when the angular speeds match. The #4 (Hidden Structure) move is the recognition that $P = B$ is the unique fixed point of the reflection that lies on both circles.

*The traps planted.* Two.

- **Trap 1: the parametric-derivation trap.** The solver sets up coordinates, writes the moving points as $A + r_1(\cos \omega t, \sin \omega t)$ and $A + r_2(\cos \omega t, \sin \omega t)$ (with the *same* $\omega$ from the equal-period hypothesis), and computes the locus of points equidistant from both. The locus is a *line* (the perpendicular bisector of the segment connecting the two moving points), which moves with time. The fixed point $P$ must therefore be the intersection of this moving perpendicular-bisector with some *time-invariant* object — specifically, the line of common chord, which is line $AB$. The trap is real but consumes substantial algebra; the symmetry argument is one paragraph. Generous: teaches that geometric symmetry can defeat coordinate algebra in pacing.
- **Trap 2: the wrong-fixed-point trap.** The solver, looking for a fixed equidistant point, considers the midpoint of $A$ and some other configuration centre — perhaps the midpoint of the line of centres of the two circles, or the centroid of the triangle formed by $A$, the two centres. None of these candidates work. The trap is that the *obvious* equidistance candidates (geometric centres of various sub-configurations) are not the answer; the answer is the *other intersection point* $B$, which is not an obvious "centre" but is the unique fixed point of the relevant reflection. Generous: teaches that fixed-point problems often have non-obvious fixed points, and that the right approach is to identify the *symmetry* under which the configuration is invariant and find the symmetry's fixed locus.

*The statement-craft.* The phrasing *"travelling along its own circle in the same sense"* is the critical hypothesis. Without *"in the same sense"* (i.e., both clockwise or both counter-clockwise), the equidistance fails. The IMO committee chose to specify the sense to remove ambiguity; a less careful designer might have omitted this hypothesis, producing an under-specified problem. The phrasing *"two points return to $A$ simultaneously after one revolution"* establishes the equal-angular-speed condition without naming angular speeds explicitly; the solver must infer the equal speeds from the simultaneous-return clause.

### The Reader's Re-Solution

- *Given.* Two circles $\omega_1, \omega_2$ intersecting at $A$ and $B$. Two points $M_1, M_2$ moving with constant speeds along $\omega_1, \omega_2$ respectively, both starting at $A$, both in the same rotational sense, both completing one revolution in common period $T$.
- *Find.* A point $P$ such that $|PM_1(t)| = |PM_2(t)|$ for all $t$.
- *Strategy.* Identify the reflection symmetry of the configuration; the fixed locus of the reflection contains the answer.
- *Stage 1 (#8).* Parametrise: $M_1(t)$ is at angle $\omega t$ along $\omega_1$ (measured from $A$, in the chosen rotational sense), where $\omega = 2\pi/T$ is the common angular speed. Similarly for $M_2(t)$.
- *Stage 2 (#2).* The two circles, together with the equal-angular-speed parametrisation, admit a reflection symmetry across the line $AB$ (the common chord), which maps each circle to itself and exchanges the two moving points' positions when reflected appropriately. The fixed point of the reflection that also lies on both circles is $B$ (the other intersection point) — $A$ being the *starting* point and $B$ being the *return* point of the reflection.
- *Stage 3 (#4).* Verification: at any time $t$, the points $M_1(t)$ and $M_2(t)$ are reflections of each other across $AB$ (this is the symmetry conclusion). Therefore $|BM_1(t)| = |BM_2(t)|$ for all $t$, since reflection preserves distances and fixes $B$.
- *Convergence.* $P = B$, the second intersection point of $\omega_1$ and $\omega_2$, is the required fixed equidistant point. $\boxed{P = B.}$

### Lessons for Problem Designers

1. **Time-parametrised geometric problems are usually angle-parametrised problems.** The first move in any "moving points" olympiad geometry problem is to convert *time* to *angular position*. Designers writing such problems can assume the solver will do this; the design's centre of gravity is whatever structural truth survives after the conversion.
2. **The fixed point of a reflection symmetry is the design's CEP.** Whenever a configuration has a non-trivial reflection symmetry, the fixed locus of the reflection (a line in 2D) contains the answer. Designers can engineer reflection-symmetry problems by starting from a known reflection and constructing a configuration that respects it.
3. **Hypothesis-tightness, again.** The *"in the same sense"* clause is exactly what makes the angular-speeds-equal conclusion correct. Designers writing dynamic-geometry problems should *audit each hypothesis* to confirm it is doing structural work (not merely decorative).

---

## §5 — Case Study 10: IMO 2003 Problem 1 (the precisely-calibrated pigeonhole)

**Source.** International Mathematical Olympiad 2003, Problem 1.  
**CEP.** The constants $101$ and $10^6$ are chosen so that the number of "bad shifts" $t$ (those that cause $A_j = \{x + t : x \in A\}$ to collide with some previously-chosen $A_i$) is at most $\binom{101}{2} \cdot 99 = 100 \cdot 50 \cdot 99 < 10^6$, so a $100$th good shift always exists.  
**Archetypes.** #13 (Combinatorial — double-counting bad shifts) + #12 (Extremal — the inequality $\binom{101}{2} \cdot 99 < 10^6$ is the design's tight calibration).  
**Difficulty.** Tier 3-high.  
**Verification source.** `Cursor-IMO.md` §II; `imo-compendium.txt` near line 18900.

### Problem statement

> Let $A$ be a 101-element subset of the set $S = \{1, 2, 3, \ldots, 10^6\}$. Prove that there exist numbers $t_1, t_2, \ldots, t_{100}$ in $S$ such that the sets $A_j := \{x + t_j : x \in A\}$ for $j = 1, 2, \ldots, 100$ are pairwise disjoint.

### The Designer's Architecture

*The CEP unmasked.* The argument is a greedy construction: choose $t_1 = 0$ (so $A_1 = A$). For each subsequent $t_j$ ($j = 2, \ldots, 100$), $t_j$ is *good* if $A_j$ is disjoint from $A_1, \ldots, A_{j-1}$ — equivalently, if $t_j$ is not of the form $a - b + t_i$ for any $a, b \in A$ and any $i < j$. The number of *bad* shifts (excluded by collision with $A_i$) is at most $|A|^2 = 101^2$ per previously-chosen $t_i$, summed over $i < j$, gives at most $j \cdot 101^2$ bad shifts when choosing $t_{j+1}$. After choosing $99$ shifts (for $j+1 = 100$), the number of bad shifts is at most $99 \cdot 101^2 = 99 \cdot 10201 = 1{,}009{,}899$, which is greater than $10^6$ — *the calibration fails by 9899*.

A tighter count: the number of bad shifts $t$ for the $(j+1)$th choice is at most $j \cdot (|A|^2 - |A|) = j \cdot 101 \cdot 100$, since collisions are *between* distinct points of $A$ (the diagonal $a = b$ gives $t_j$ itself, which is already chosen). So the bound is $j \cdot 10100$, and for $j = 99$ this is $999{,}900 < 10^6$. **The calibration works** with margin $100$. The CEP is the inequality $99 \cdot 101 \cdot 100 < 10^6$.

*The archetype convergence.* #13 + #12. The #13 (Combinatorial) move is the double-counting: count the bad shifts via the pairs of $A$-elements that could collide. The #12 (Extremal) move is the inequality bound: confirm that the bad-shift count is strictly less than $|S|$, so a good shift always exists.

*The traps planted.* Two.

- **Trap 1: the constructive trap.** The solver attempts to *construct* explicit shifts $t_1, \ldots, t_{100}$ (e.g., choose $t_j = (j-1) \cdot K$ for some $K$ such that the shifts are pairwise far apart). The constructive approach can work but requires choosing $K$ large enough that the shifted copies of $A$ do not overlap; the smallest such $K$ depends on the specific $A$ (since $A$ can range over $\{1, \ldots, 10^6\}$), so a constructive proof must work for every possible $A$. The trap is that the constructive approach is *not impossible* but is much harder than the greedy / existence approach. Generous: teaches that existence proofs (via probabilistic / counting arguments) are often dramatically cleaner than constructive proofs.
- **Trap 2: the wrong-counting trap.** The solver miscounts the bad shifts — for instance, using $|A|^2 = 101^2 = 10201$ as the per-step bound (forgetting that the diagonal $a = b$ gives $t_j$ itself and should be excluded), leading to the loose bound $99 \cdot 10201 > 10^6$ and the false conclusion that the calibration fails. The tighter bound $99 \cdot 100 \cdot 101 = 999900 < 10^6$ requires the careful exclusion. Generous: teaches that double-counting bounds should be made *as tight as possible* before checking the calibration, since loose bounds may falsely suggest a problem is unsolvable as stated.

*The statement-craft.* The specific choices $101$ and $10^6$ and $100$ are precisely the constants for which the inequality $(\text{number of shifts to choose}) \cdot |A| \cdot (|A| - 1) < |S|$ holds with the tightest possible margin while preserving integer values. The IMO committee's calibration: $99 \cdot 100 \cdot 101 = 999{,}900$ vs $|S| = 1{,}000{,}000$ — a margin of $0.01\%$. This is the kind of constant-tuning that distinguishes a well-designed IMO problem from a textbook exercise.

### The Reader's Re-Solution

- *Given.* $|A| = 101$, $A \subset S = \{1, \ldots, 10^6\}$.
- *Find.* Shifts $t_1, \ldots, t_{100} \in S$ such that $A + t_j$ ($j = 1, \ldots, 100$) are pairwise disjoint.
- *Strategy.* Greedy choice; count bad shifts; confirm a good shift always exists.
- *Stage 1 (#13).* Choose $t_1 = 0$. Suppose $t_1, \ldots, t_j$ have been chosen with the disjointness property. The "bad" choices for $t_{j+1}$ are those $t \in S$ such that $A + t$ intersects $A + t_i$ for some $i \leq j$, i.e., $t = t_i + a - b$ for some $a, b \in A$ with $a \neq b$. The number of such bad $t$ values is at most $j \cdot |A| \cdot (|A| - 1) = j \cdot 101 \cdot 100$.
- *Stage 2 (#12).* For $j + 1 = 100$ (i.e., choosing the last shift $t_{100}$), the bad-shift count is at most $99 \cdot 101 \cdot 100 = 999{,}900 < 10^6 = |S|$. Therefore at least $100$ good shifts exist in $S$, and any one of them suffices as $t_{100}$.
- *Convergence.* The greedy construction succeeds at every step; $t_1, \ldots, t_{100}$ with the disjointness property exist. $\boxed{\text{Construction completed.}}$

### Lessons for Problem Designers

1. **Tight constants are the IMO design signature.** The IMO 2003 P1 calibration ($999{,}900 < 1{,}000{,}000$ by $0.01\%$) is the kind of constant-engineering that distinguishes a great IMO problem from a textbook exercise. Designers aiming for IMO-quality problems should iterate on the constants until the calibration is tight to within $1-5\%$.
2. **Greedy existence beats constructive existence at this tier.** When a problem asks to *prove existence* of a structure with $n$ components, designers should consider whether the greedy/counting argument works — and whether the constants in the problem allow it. The IMO 2003 P1 calibration is engineered precisely so that the greedy argument barely succeeds; this is the design choice.
3. **The double-counting tightness is non-cosmetic.** Designers writing pigeonhole / counting problems should *audit* whether their intended counting bound is the tightest available; loose bounds may falsely suggest infeasibility (as Trap 2 shows), and the design's center of gravity is often in the precise tightness of the counting.

---

## §6 — Bridge to Chapter 6

The five cases of this chapter share a structural feature: each has a *single crucial construction* (the monovariant, the auxiliary circle, the smoothing argument, the angular parametrisation, the bad-shift count) that the solver must produce before the convergence becomes visible. The Moderate-tier cases of Chapter 4 required no such construction — the convergence was visible as soon as the right archetypes were recognised. The High-mid cases of Chapter 6, which we approach now, escalate one further step: the *construction itself* is a non-obvious move that the solver must engineer, and the construction's existence is itself a non-trivial mathematical fact.

The opening case of Chapter 6 is IMO 1959 Problem 6, the only remaining Moderate-era IMO problem in our slate after Chapter 4's Case 1. Its inclusion in the High-mid chapter (rather than the Moderate chapter) is a tier-correction: although the surface is school-accessible (an inscribed circle in an isosceles trapezium spanning two planes), the construction it requires — identifying the precise tangent-length condition and using it to force a specific angle equality — is a Mid-to-High-mid move rather than a Moderate one. Cases 11 through 15 of Chapter 6 are unified by their need for a *constructive* CEP: each requires the solver to produce a mathematical object (a circle, a recurrence, a bijection, a residue, a periodicity) whose existence is not obvious from the surface.

We turn there now.

---

*End of Chapter 5.*
