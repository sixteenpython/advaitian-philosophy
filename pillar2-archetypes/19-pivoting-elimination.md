---
chapter: 19
archetype: Pivoting / Elimination
subtitle: "Simplify by Subtraction, Not Addition"
category: Meta-Reasoning (Archetypes 17–20) — third chapter
related_archetypes: [5, 8, 16, 17, 18]
key_gems:
  - "Gaussian elimination: a linear system $A \\vec x = \\vec b$ with $A$ of size $m \\times n$ is solved by *pivoting* — choose a non-zero entry as the pivot, use it to eliminate that variable from all other rows, repeat on the reduced $(m - 1) \\times (n - 1)$ subsystem; the process terminates in row-echelon form with rank-many pivots and the solution read off by back-substitution"
  - "Partial-pivoting numerical stability: at each elimination step, choose the largest-absolute-value entry in the current column as the pivot; this minimises the propagation of rounding error in floating-point arithmetic and is the standard in production LU-factorisation routines (LAPACK, MATLAB, NumPy)"
  - "Resultant of two polynomials: $f$ and $g$ have a common root iff the *Sylvester resultant* $\\mathrm{Res}(f, g) = \\det S = 0$, where $S$ is the $(\\deg f + \\deg g) \\times (\\deg f + \\deg g)$ Sylvester matrix; for two quadratics $f = ax^2 + bx + c$, $g = px^2 + qx + r$, the resultant simplifies to $(ar - cp)^2 - (aq - bp)(br - cq)$"
  - "Parametric-to-Cartesian elimination via trigonometric identities: from $x = a \\sec\\theta, y = b \\tan\\theta$, the identity $\\sec^2\\theta - \\tan^2\\theta = 1$ eliminates $\\theta$ to give the Cartesian hyperbola $x^2/a^2 - y^2/b^2 = 1$"
  - "BAC–CAB vector identity: $\\vec a \\times (\\vec a \\times \\vec b) = (\\vec a \\cdot \\vec b) \\vec a - (\\vec a \\cdot \\vec a) \\vec b$, the inversion formula for recovering $\\vec b$ from $\\vec a \\cdot \\vec b$ and $\\vec a \\times \\vec b$"
  - "Tangency-as-discriminant elimination: a line $y = mx + c$ is tangent to a conic iff substituting into the conic equation yields a quadratic in $x$ with discriminant zero; the tangency condition is one elimination step that reduces the line-conic intersection to a single contact"
  - "Decoupling coupled linear ODEs via eigenbasis: a system $\\vec u' = A \\vec u$ is decoupled by changing to the eigenbasis of $A$; in eigenbasis coordinates $v_i$, the system reduces to $n$ independent scalar ODEs $v_i' = \\lambda_i v_i$ with solutions $v_i(t) = c_i e^{\\lambda_i t}$"
  - "Substitution as forward-elimination: $u = g(x)$ replaces the variable $x$ with $u$, eliminating the original $x$-dependence; the substitution is a *pivot* on the variable $x$, and the chain rule provides the inverse transformation $dx = (du)/g'(x)$"
  - "Pencil-of-curves elimination: a 1-parameter family $\\lambda C_1 + (1 - \\lambda) C_2 = 0$ traces out the pencil of curves through the intersection of $C_1, C_2$; eliminating $\\lambda$ between two members of the pencil recovers $C_1 \\cap C_2$ as the residual"
  - "Subtraction-as-simplification meta-principle: pivoting and elimination operate by *subtracting* a multiple of one equation from another (Gaussian), or by *subtracting* one variable from the system via the resultant (polynomial), or by *subtracting* a parameter from a parametric representation (trig elimination); the systematic preference for subtractive operations over additive ones is the chapter's defining cognitive habit"
canonical_takeaway: "Simplify by subtraction, not addition. Every elimination move *removes* a variable, an unknown, a parameter, or a degree-of-freedom from the problem; the chapter's discipline is to *choose the pivot* that maximises the structural simplification produced by the elimination, then iterate until the residual problem is trivial."
status: draft
last_revised: 2026-05-28
sourcing_note: "All worked examples and practice problems in this chapter are drawn from K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), or from JEE / RMO / INMO examinations commented on in that text. See Blueprint §6.2 for the sourcing rule and `pillar2-archetypes/_template/joshi-problems-locked.md` §Ch. 19 for the locked slate. **Verification audit for this chapter caught FOUR slate errors** — a new single-chapter record (previous high was 2 errors at Chs. 12 and 13). The errors and their corrections: (i) **PP2** (Joshi Ch. 24 Ex. 24.40, $F(x^2) = x^2(1+x)$, find $f(4)$): slate listed $f(4) = 5/2$; correct is $f(4) = 4$. This is the same problem as Ch. 5 PP2 which was patched to 4 in v0.2.2; the Ch. 19 PP2 entry was not propagated. Implicit differentiation: $2x \\cdot f(x^2) = 2x + 3x^2 \\Rightarrow f(x^2) = 1 + (3/2)x$, so $f(4) = 1 + 3 = 4$ at $x = 2$. (ii) **PP5** (Joshi Ch. 21 Ex. 21.10, JEE 1985, find $\\vec b$ from $\\vec a = (1,2,1), \\vec a \\cdot \\vec b = 6, \\vec a \\times \\vec b = (2,-2,2)$): slate listed $\\vec b = (1,2,3)$, which fails the constraint $\\vec a \\cdot \\vec b = 6$ (gives 8). Correct $\\vec b = (0,2,2)$ via BAC–CAB: $\\vec a \\times (2,-2,2) = (6,0,-6) = 6\\vec a - 6\\vec b$ gives $\\vec b = (0,2,2)$. Verify: $\\vec a \\cdot \\vec b = 0+4+2 = 6$ ✓, $\\vec a \\times \\vec b = (4-2, 2-0, 2-0) = (2,-2,2)$ ✓. (iii) **PP6** (Joshi Ch. 9 Comment 11, family of lines): slate stated 'locus is a line' (incoherent and incorrect). The system $\\alpha + m\\beta = 1, m\\alpha - \\beta = 2$ has unique solution $\\alpha = (1+2m)/(1+m^2), \\beta = (m-2)/(1+m^2)$; eliminating $m$ yields $\\alpha^2 + \\beta^2 = \\alpha - 2\\beta$, i.e., the **circle** $(\\alpha - 1/2)^2 + (\\beta + 1)^2 = 5/4$ centred at $(1/2, -1)$ with radius $\\sqrt 5/2$ (passing through the origin). Verified at $m = 0$: $(\\alpha, \\beta) = (1, -2)$, distance to $(1/2,-1)$ is $\\sqrt{5/4} = \\sqrt 5/2$ ✓. (iv) **PP7** (Joshi Ch. 19 Comment 9, coupled ODE system $x' = x + y, y' = x - y$ with $x(0) = 1, y(0) = 0$): slate listed $x(t) = (1/2)(\\cosh(\\sqrt 2 t) + (1/\\sqrt 2) \\sinh(\\sqrt 2 t))$ — extraneous $1/2$ factor makes $x(0) = 1/2 \\ne 1$. Correct: $x(t) = \\cosh(\\sqrt 2 t) + (1/\\sqrt 2) \\sinh(\\sqrt 2 t)$ and $y(t) = (1/\\sqrt 2) \\sinh(\\sqrt 2 t)$, with eigenvalues $\\pm \\sqrt 2$ of $A = \\binom{1 \\;\\;\\;1}{1 \\;-1}$ and initial-condition fitting $c_+ = (2+\\sqrt 2)/4, c_- = (2-\\sqrt 2)/4$. All four corrections logged in slate v0.2.16. The chapter is the **third** of the Meta-Reasoning sub-pillar (Chs. 17–20), following Ch. 17 (DOF) and Ch. 18 (Induction), and bridging to the capstone Ch. 20 (Analogy / Transfer). **Cross-archetype reuses**: PP1 (inverse via variable-pivot) is cross-archetype with Ch. 5 PP1 (substitution as inverse-engine); PP2 is the same JEE 2001 problem as Ch. 5 PP2 (substitution-driven differentiation), here re-framed as parametric-elimination via the $u = x^2$ pivot; PP4 (conic intersection) uses substitution + quartic factorisation, connecting to Ch. 16 (reverse-engineering the intersection from the curve equations); PP7 (eigenbasis decoupling) connects to Ch. 17 (DOF analysis on the eigenvalue spectrum) and Ch. 18 (matrix-exponential induction)."
---

# Chapter 19 — Pivoting / Elimination

## *Simplify by Subtraction, Not Addition*

---

## Opening Vignette

A senior electronics engineer at the Indian Institute of Technology Madras's Microelectronics and Embedded Systems Lab in Chennai is analysing a newly-designed seven-node power-conditioning circuit for a satellite-payload subsystem destined for the next ISRO communications satellite. The circuit contains eleven independent mesh currents (the application of Kirchhoff's voltage law around each independent loop yields one equation per mesh), and the engineer's task is to solve the resulting $11 \times 11$ system $A \vec I = \vec V$ — where $A$ is the impedance matrix and $\vec V$ the vector of applied EMFs — to determine each mesh current with sub-microampere accuracy for the radiation-hardened design specification. The naïve numerical approach (direct matrix inversion via Cramer's rule, computing $\binom{11}{1}^2 = 121$ minor determinants) would require approximately $11! \approx 4 \times 10^7$ multiplications and is numerically unstable for the $\sim 10^{-4}$ relative-precision requirement. The senior engineer's first move, before invoking any computational machinery, is to *choose the pivot order* for Gaussian elimination: at each elimination step, select as pivot the *largest absolute-value entry* in the current column (the *partial-pivoting* strategy), so that the divisions $a_{ij}/a_{kk}$ introduced by the elimination produce minimal rounding-error amplification. The partial-pivoting choice is a *local* decision (only the current column matters) but its *global* effect — keeping the condition number of the reduced subsystems bounded and the numerical precision uniformly high — is what makes the difference between a satellite circuit that meets specification and one that drifts out of tolerance after launch. Once the pivot sequence is fixed, the elimination proceeds inductively (pivot, subtract the pivot row from all rows below scaled appropriately, recurse on the $(n - 1) \times (n - 1)$ subsystem), terminating in upper-triangular form with all mesh currents recoverable by back-substitution. The entire computation completes in approximately $\frac{2}{3} \cdot 11^3 \approx 900$ multiplications, four orders of magnitude faster than Cramer's rule, and numerically stable to $10^{-6}$ relative precision — well within the radiation-hardened specification.

Now turn to a different scene. A senior chess analyst at the Chennai Chess Centre, herself a Grandmaster and former Indian women's national champion, is sitting at her training board reviewing an instructive endgame position that arose in a recent Chess Olympiad — Black has just moved a knight to threaten a fork on the White king and rook, and White must find the unique drawing move within a five-second time pressure. The analyst's first move, before considering any candidate, is to perform an *elimination scan*: she enumerates White's plausible responses — there are seven candidate king moves and three candidate rook moves, ten in total — and systematically *eliminates* those that lose to the threatened fork (six of the ten king and rook moves lose to a forced sequence; four survive). Of the four surviving candidates, she then *pivots* on the *most forcing* — the move that *eliminates the largest number* of Black's follow-up threats — and reduces the analysis to the remaining branches. The pivoting strategy is *subtractive* throughout: at each branch, eliminate the candidate moves that lose, and pivot on the most-eliminating response among the survivors. The analyst's discipline contrasts sharply with the amateur's: an amateur facing the same position would *additively* search through all candidate moves, computing each line forward to a tactical resolution, and would typically run out of time before finding the unique drawing move. The Grandmaster's *subtractive* search — eliminate the losing moves first, pivot on the most-forcing response, recurse on the residual position — completes the analysis in three to four seconds, leaving time for verification.

These two scenes look entirely unrelated. An IIT Madras circuit engineer pivoting on the largest-current mesh to solve an $11 \times 11$ impedance system; a Chennai chess Grandmaster pivoting on the most-forcing move to eliminate losing candidate responses in an Olympiad endgame. The activities differ in every superficial respect — one is engineering numerical analysis, the other is competitive game-tree search; one is governed by Kirchhoff's laws, the other by chess rules and tactical conventions; one's verification is satellite-test bench measurement, the other's verification is endgame-tablebase comparison — yet they share the most important meta-level habit in the entire chapter: *simplify by subtraction, not addition*. Both professionals *eliminate*: the engineer eliminates one variable per pivot step from the linear system; the chess analyst eliminates losing candidate moves from the tactical tree. Both *choose the pivot*: the engineer pivots on the largest-absolute-value column entry for numerical stability; the analyst pivots on the most-forcing move for tactical economy. Both *recurse on the residual*: the engineer's Gaussian elimination continues on the smaller subsystem; the analyst's tactical search continues on the surviving branches. The cognitive operation is identical — *choose a pivot*, *eliminate variables / candidates*, *recurse on what remains*.

This is *Pivoting / Elimination*. It is the *third* chapter of the *Meta-Reasoning* sub-pillar (Chapters 17–20), following Chapter 17 (Degrees of Freedom Analysis) and Chapter 18 (Recursion / Induction), and bridging to the capstone Chapter 20 (Analogy / Transfer). The chapter develops the toolkit (Gaussian elimination with partial pivoting, polynomial resultants via the Sylvester matrix, parametric-to-Cartesian elimination via trigonometric identities, BAC–CAB-driven vector-equation inversion, tangency-as-discriminant elimination, pencil-of-curves elimination, eigenbasis decoupling for linear ODE systems) and the recurring patterns (each elimination removes one variable / parameter / unknown from the problem; pivot order matters for numerical stability and for combinatorial economy; subtraction-driven simplification is preferred over additive complication). The chapter has three structural threads. The first is *one-pivot-at-a-time discipline*: every substantive elimination problem proceeds *one pivot at a time*, each reducing the problem's dimensionality by one. The second is *pivot-choice optimality*: the *choice* of pivot — which variable to eliminate, which equation to keep as the pivot row, which entry to use as the pivot — is the consequential decision, often more important than the mechanical elimination that follows. The third is *Meta-Reasoning sub-pillar continuation*: by Chapter 19, the reader has internalised the DOF-counting (Ch. 17) and inductive-descent (Ch. 18) habits, and is now equipped to add the *subtraction-as-simplification* habit (Ch. 19) as the third leg of the Meta-Reasoning triad.

> *Simplify by subtraction, not addition. Every elimination move removes a variable, an unknown, a parameter, or a degree-of-freedom from the problem; the chapter's discipline is to choose the pivot that maximises the structural simplification produced by the elimination, then iterate.*

---

## 1. The Archetype Defined

### 1.1 Formal Definition

We make the intuition precise.

\begin{definition}[Pivoting / Elimination Archetype]
A *pivoting / elimination* approach to a problem is the strategy of *systematically removing variables, unknowns, or parameters one at a time* by choosing a *pivot* (an entity that can be solved for, isolated, or used as a reference) and using it to *eliminate* that entity from the remaining equations or constraints. The archetype is the discipline of (i) identifying the *ambient system* of equations, unknowns, or constraints; (ii) choosing a *pivot* — the variable to eliminate first, or the entry to use as the pivot — based on a *pivot-choice criterion* (numerical stability, structural simplicity, combinatorial economy); (iii) performing the *elimination* — subtracting multiples of the pivot equation from the others, or substituting the pivot's value into the others; (iv) *recursing* on the reduced subsystem (now one dimension smaller); and (v) terminating when the residual subsystem is trivial (a single equation in a single unknown, or a triangular form solvable by back-substitution).
\end{definition}

Three remarks unpack the definition.

First, the *pivot-choice criterion* (Step (ii)) is the cognitively central step. The naïve choice ("pivot on the first variable, then the second, etc.") works for many simple problems but fails on the harder ones for either of two reasons: (a) *numerical instability* — for floating-point computation, dividing by a small pivot amplifies rounding error catastrophically, and the *partial-pivoting* strategy (always choose the largest-absolute-value entry as pivot) is the standard remedy; (b) *combinatorial inefficiency* — for symbolic computation, eliminating a "high-degree" variable first produces large intermediate polynomials, and choosing the lowest-degree variable as pivot keeps intermediate expressions manageable. The trained solver makes the pivot choice *deliberately*, not by default.

Second, the *elimination mechanics* (Step (iii)) take many forms depending on the problem class:
\begin{itemize}
\item *Linear-system elimination*: subtract a scalar multiple of the pivot row from each other row, zeroing out the pivot's column entries.
\item *Polynomial elimination*: compute the *resultant* of two polynomials, a single polynomial in the remaining variables whose vanishing is equivalent to the existence of a common root.
\item *Parametric elimination*: use an algebraic identity (e.g., $\sec^2\theta - \tan^2\theta = 1$) to convert a parametric system into a Cartesian one.
\item *Substitution elimination*: substitute the pivot's value (obtained from the pivot equation) into the others.
\item *Decoupling elimination*: change to the eigenbasis of a coupled system, in which the elimination is automatic (the system is diagonal).
\end{itemize}

Third, the *recursion-on-residual* (Step (iv)) is the engine. Pivoting is inherently *inductive*: each pivot reduces the system's dimension by 1 (or the number of unknowns by 1, or the polynomial-degree by 1), and the algorithm recurses on the smaller residual. This is the same inductive descent we encountered in Chapter 18; pivoting / elimination is the *constructive* instantiation of induction for systems of equations.

The chapter encounters five characteristic forms of pivoting / elimination.

- **Form I — Linear-system Gaussian elimination.** Pivot on a row, subtract scalar multiples to zero out the column, recurse. *Examples.* WE3 (canonical $3 \times 3$ system).

- **Form II — Polynomial resultant.** Eliminate one variable between two polynomials by computing the Sylvester resultant. *Examples.* WE2 (resultant of two quadratics).

- **Form III — Parametric-to-Cartesian conversion.** Eliminate the parameter using algebraic / trigonometric identities. *Examples.* PP3 (hyperbola from $x = a \sec\theta, y = b \tan\theta$).

- **Form IV — Substitution-driven elimination.** Substitute one variable's value (from one equation) into the others; iterate. *Examples.* WE1 (substitute parabola tangent into circle to get tangency condition), PP1 (invert $y = x + 1/x$ for $x$), PP2 (chain-rule pivot on $u = x^2$), PP4 (conic intersection via $y = 12/x$ into the circle).

- **Form V — Eigenbasis decoupling.** Pivot to the eigenbasis of a coupled linear system, making the system diagonal. *Examples.* PP7 (decouple $x' = x + y, y' = x - y$).

### 1.2 The Core Principle

Stripped to its essence, the principle is one sentence.

> *Simplify by subtraction, not addition.*

This sentence captures the recurrent observation that, across mathematics, engineering, and computer science, the most efficient simplification moves are *subtractive*: remove a variable from a linear system (Gaussian elimination subtracts pivot-row multiples); remove a parameter from a parametric system (trigonometric identity subtracts the parameter's contribution); remove a candidate from a search tree (chess elimination subtracts losing moves); remove a dimension from a state space (eigenbasis decoupling subtracts the cross-coupling). The IIT Madras circuit engineer subtracts pivot-row multiples; the Chennai chess Grandmaster subtracts losing candidate moves; both perform the *same* cognitive operation.

The principle generalises far beyond classical mathematics. In *computer algebra* (Mathematica, SageMath, Maple), Buchberger's algorithm for Gröbner bases is a generalisation of Gaussian elimination to polynomial ideals; the algorithm proceeds by polynomial pivoting and reduction. In *optimisation*, the simplex method for linear programming is a pivoting algorithm: at each step, pivot on a non-basic variable that improves the objective and eliminate a basic variable from the basis. In *machine learning*, principal-component analysis (PCA) and singular-value decomposition (SVD) are eigenbasis-pivoting algorithms that decouple high-dimensional data into independent dimensions ranked by variance. In *number theory*, the Euclidean algorithm for $\gcd(a, b)$ is pivoting: at each step, pivot on the larger of $a, b$ and replace it by its remainder modulo the smaller. Across these very different domains, the *pivoting-and-elimination* meta-operation is the same.

### 1.3 Why It Works

There are three reasons.

First, the *one-pivot-per-step compression* is dimensionally tight. Each pivot operation reduces the system's dimension by exactly 1; for an $n$-variable system, exactly $n - 1$ pivots are required to reach the trivial residual (a single equation in a single unknown, solvable directly). The total work is $O(n^3)$ for Gaussian elimination, dramatically better than the $O(n \cdot n!)$ of Cramer's rule. The dimensional compression is the most efficient possible decomposition of an $n$-dimensional problem into 1-dimensional sub-problems.

Second, the *pivot choice optimises a local-global tradeoff*. The pivot choice is a *local* decision (only the current row / column / variable is considered) but its *global* effect (numerical stability of the remaining computation, combinatorial economy of the intermediate expressions) is what makes pivoting practical. The partial-pivoting strategy — choose the largest-absolute-value column entry — is the *provably optimal* local choice for numerical stability of linear systems in floating-point arithmetic, and is the basis of the LAPACK / BLAS routines that underpin all modern scientific computing.

Third, the *subtraction-as-simplification* preference reflects a deep structural asymmetry between addition and subtraction. Addition creates new structure (combines two entities into one); subtraction removes structure (cancels common factors, eliminates variables, reduces dimension). For *simplification* purposes, subtraction is the right operation: it produces a smaller, simpler residual. The chapter's central insight is that *good simplification proceeds by subtracting, not by adding*; combining terms (adding) only complicates further, while cancelling terms (subtracting) genuinely simplifies.

These three reasons — dimensional compression, optimal pivot-choice, subtractive-simplification asymmetry — combine to make pivoting / elimination the *most universal simplification technique* in equational mathematics.

---

## 2. Deep Structure

### 2.1 Anatomy of a Pivoting / Elimination Problem

Every pivoting / elimination problem has the same five-step anatomy.

\begin{enumerate}
\item \textbf{Ambient-system identification.} Identify the equations, unknowns, or constraints that constitute the system. The system can be linear (linear system $A \vec x = \vec b$), polynomial (system of polynomial equations), parametric (parametric representation $x = f(t), y = g(t)$), or geometric (system of geometric conditions).

\item \textbf{Pivot choice.} Choose the variable, unknown, or parameter to eliminate first. The pivot-choice criterion depends on the context: partial pivoting (largest absolute value) for numerical stability; lowest-degree variable for polynomial systems; simplest identity (e.g., $\sec^2 - \tan^2 = 1$) for parametric systems.

\item \textbf{Elimination operation.} Perform the elimination — subtract multiples of the pivot equation, compute the resultant, apply the algebraic identity, substitute the pivot's value. The specific mechanics depend on the problem class (linear, polynomial, parametric, etc.).

\item \textbf{Recursion on the residual.} The residual subsystem (now one dimension smaller) is recursively pivoted, eliminated, and reduced.

\item \textbf{Termination and back-substitution.} The recursion terminates when the residual is trivial (a single equation in a single unknown, or a triangular form). Solve the trivial residual; back-substitute to recover the values of the eliminated variables.
\end{enumerate}

The five steps are universal: every pivoting / elimination problem follows them, often implicitly. Making them explicit is the chapter's pedagogical purpose.

### 2.2 The Three Pivoting Strategies

Three pivot-choice strategies recur across problems.

**Partial pivoting (numerical stability).** At each elimination step, choose the largest-absolute-value entry in the current column as the pivot. This minimises the divisions by small numbers (which would amplify rounding error in floating-point arithmetic) and is the standard for production numerical-linear-algebra routines. The IIT Madras circuit engineer's vignette is a partial-pivoting example.

**Symbolic pivoting (algebraic simplicity).** For symbolic-computation problems (polynomial systems, parametric eliminations), choose the variable that appears in the *simplest form* — typically the lowest-degree variable, or the variable that occurs in the fewest equations. This keeps the intermediate expressions manageable and reduces the algorithm's worst-case complexity.

**Strategic pivoting (combinatorial / structural).** For combinatorial-search problems (chess endgame analysis, Gröbner basis computation, simplex method), choose the pivot that *eliminates the most candidates* or *simplifies the residual the most*. The Chennai chess Grandmaster's vignette is a strategic-pivoting example: pivot on the most-forcing move to eliminate the most opponent options.

A fourth strategy worth noting:

**Complete pivoting (maximum stability).** At each step, choose the largest-absolute-value entry in the entire remaining sub-matrix (not just the current column). This is more expensive than partial pivoting (requires searching the entire sub-matrix at each step) but is the most numerically stable; it is reserved for high-precision applications where the extra cost is justified.

The trained solver, faced with a pivoting problem, considers each strategy in turn: would partial pivoting suffice (for numerical work)? would symbolic pivoting be better (for algebraic work)? would strategic pivoting be the right move (for combinatorial work)? Spending sixty seconds on this choice often saves hours of wasted computational effort.

### 2.3 Common Pitfalls and How to Recognise Them

Five classical pitfalls recur in pivoting / elimination problems.

**Pitfall 1: Pivoting on a zero or near-zero entry.** Dividing by zero is impossible; dividing by near-zero is numerically catastrophic. The fix: always check the pivot entry's magnitude before dividing; if it is too small, pivot on a different entry (this is the *partial-pivoting* strategy in action).

**Pitfall 2: Pivoting on the wrong variable for symbolic work.** If the chosen pivot variable has high degree (e.g., quartic) in the equation, the resultant or substitution produces enormous intermediate polynomials. The fix: pivot on the *lowest-degree* variable, even if it is not the first variable lexicographically.

**Pitfall 3: Forgetting to back-substitute.** Pivoting reduces the system to triangular form, but the *back-substitution* phase is required to recover the eliminated variables' values. The fix: explicitly perform back-substitution after the elimination phase; do not stop at the triangular form.

**Pitfall 4: Eliminating a variable that creates extraneous solutions.** Some elimination operations (e.g., squaring both sides, multiplying by an unknown) introduce extraneous solutions that do not satisfy the original system. The fix: after the elimination produces a candidate set, *verify each candidate against the original equations* and discard the extraneous ones.

**Pitfall 5: Confusing the elimination order in nested operations.** When eliminating two variables sequentially (e.g., $\alpha$ then $\beta$ from a 2-parameter family), the order can matter for the form of the resulting expression (though not the final answer). The fix: be explicit about the elimination order and verify that the final answer is invariant under the order.

These five pitfalls account for the overwhelming majority of pivoting / elimination errors in olympiad and engineering practice. Internalising them is the elimination-discipline's working capital.

---

## 3. The Diagnostic Toolkit

How does one *recognise*, when first encountering a problem, that pivoting / elimination is the right archetype to deploy? The following four-question diagnostic checklist serves as the trained solver's first scan.

\begin{itemize}
\item \textbf{Q1 (Multiple equations, multiple unknowns).} \emph{Does the problem involve a system of multiple equations in multiple unknowns?} Any linear system, polynomial system, parametric system, or vector-equation system is a candidate.

\item \textbf{Q2 (Single-variable target).} \emph{Is the goal to reduce the system to a single equation in a single unknown (or to a closed-form expression involving fewer variables)?} If yes, elimination is the natural technique.

\item \textbf{Q3 (Existence of a clean pivot).} \emph{Does the system contain a ``natural pivot'' — a variable that appears with a simple coefficient (often 1), a parameter that satisfies a clean algebraic identity, or a row with a small dominant entry?} If yes, the pivot is the entry point for elimination.

\item \textbf{Q4 (Subtraction-as-simplification).} \emph{Does the subtraction of one equation from another (with appropriate scalar multiple) produce a simpler equation?} If yes, the subtraction is the elimination step.
\end{itemize}

Two or more affirmative answers (especially Q1 + Q2) signal that pivoting / elimination is the right archetype. The trained solver, faced with any multi-equation problem, performs this diagnostic *first* — typically in under sixty seconds — before selecting any technical machinery.

A second-order diagnostic is *named-technique recognition*. Across hundreds of problems, only a handful of named elimination techniques recur:

- ``Gaussian elimination with partial pivoting'' (linear systems).
- ``Sylvester resultant'' (two polynomials, common-root condition).
- ``Trig-identity parametric-to-Cartesian'' ($\sec^2 - \tan^2 = 1$, $\sin^2 + \cos^2 = 1$, etc.).
- ``Tangency-as-discriminant'' (line-conic, conic-conic tangency).
- ``BAC–CAB identity'' (vector-equation inversion).
- ``Eigenbasis decoupling'' (linear ODE systems, PCA, normal modes).
- ``Pencil-of-curves elimination'' (intersection of two algebraic curves).
- ``Euclidean algorithm'' (gcd via repeated remainder pivoting).
- ``Simplex method'' (linear-programming basis pivoting).

The trained solver recognises these named techniques immediately and proceeds to the next move (apply the technique to the current problem) without re-deriving the elimination scaffold.

---

## 4. Worked Examples

The three worked examples are organised by increasing depth of elimination technique. WE1 (common tangent to circle and parabola) is a *tier-2* problem demonstrating the tangency-as-discriminant elimination — the line-conic intersection's elimination engine. WE2 (resultant of two quadratics) is a *tier-3* problem deploying the Sylvester-resultant polynomial elimination — the canonical method for common-root conditions. WE3 (Gaussian elimination on a $3 \times 3$ system) is a *tier-2* problem illustrating the canonical pivot-and-eliminate linear-systems algorithm with explicit back-substitution.

### 4.1 WE1 — Common Tangent to Circle and Parabola (Tier 2: JEE 2001)

**Problem.** *Find the equation of the common tangent (above the $x$-axis) to the circle $(x - 3)^2 + y^2 = 9$ and the parabola $y^2 = 4x$.*

**Source.** JEE 2001 (Joshi, *Educative JEE Mathematics*, Ch. 24, Exercise 24.34).

#### SEED — The Setup

The circle $(x - 3)^2 + y^2 = 9$ has centre $(3, 0)$ and radius $3$. The parabola $y^2 = 4x$ has vertex at the origin, focal length $a = 1$ (since $4a = 4$), and opens to the right.

A *common tangent* is a single line that is tangent to *both* curves simultaneously. The line is unknown, but it must satisfy *two* tangency conditions (one per curve). This is a two-equation system in the line's parameters (slope $m$ and intercept $c$), so the natural pivoting approach is to *parameterise the line by slope alone* (using one curve's tangent-form expression), then *eliminate the slope* using the other curve's tangency condition.

#### BRUTE PATH — Two-Equation System

The line $y = mx + c$ is tangent to both curves. The tangency conditions are:

- *Tangent to parabola.* Substituting $y = mx + c$ into $y^2 = 4x$ gives $(mx + c)^2 = 4x$, i.e., $m^2 x^2 + (2mc - 4) x + c^2 = 0$. Tangency requires discriminant zero: $(2mc - 4)^2 - 4 m^2 c^2 = 0$, simplifying to $-16 mc + 16 = 0$, i.e., $c = 1/m$.

- *Tangent to circle.* Distance from circle centre $(3, 0)$ to the line $mx - y + c = 0$ equals 3: $|3m + c|/\sqrt{m^2 + 1} = 3$.

Now we have two equations in $(m, c)$: $c = 1/m$ and $|3m + c| = 3 \sqrt{m^2 + 1}$. Substituting the first into the second gives one equation in $m$ alone — the elimination payoff.

The brute approach works but is roundabout: writing both tangency conditions separately, then substituting one into the other, is the explicit two-step elimination. The elegant pivot below shortens this to one step.

#### ELEGANT PIVOT — Pivot on the Parabola's Slope-Form Tangent

The pivot is to *use the parabola's slope-form tangent directly*, eliminating $c$ from the start.

For the parabola $y^2 = 4ax$ (with $a = 1$ here), the slope-form tangent line is $y = mx + a/m = mx + 1/m$. This *parametrises all tangent lines to the parabola by slope $m$ alone* — the elimination of $c$ has been pre-built into the tangent-line form.

Apply the circle tangency condition to $y = mx + 1/m$, i.e., $mx - y + 1/m = 0$:

\[
\frac{|3m - 0 + 1/m|}{\sqrt{m^2 + 1}} = 3.
\]

Square both sides (taking $3m + 1/m > 0$ for the upper tangent):

\[
\left(3m + \frac{1}{m}\right)^2 = 9 (m^2 + 1).
\]

Expand:

\[
9 m^2 + 6 + \frac{1}{m^2} = 9 m^2 + 9 \quad \Longleftrightarrow \quad \frac{1}{m^2} = 3 \quad \Longleftrightarrow \quad m^2 = \frac{1}{3} \quad \Longleftrightarrow \quad m = \pm \frac{1}{\sqrt 3}.
\]

For the tangent *above the $x$-axis*: take the positive slope $m = 1/\sqrt 3$ (the negative slope gives a tangent below, with negative $y$-intercept). The tangent equation is then

\[
y = \frac{x}{\sqrt 3} + \frac{1}{1/\sqrt 3} = \frac{x}{\sqrt 3} + \sqrt 3 = \frac{x + 3}{\sqrt 3}.
\]

The boxed conclusion is

\[ \boxed{y = \frac{1}{\sqrt 3} (x + 3).} \]

#### Verification

Check tangency to the parabola: substitute $y = (x + 3)/\sqrt 3$ into $y^2 = 4x$, getting $(x + 3)^2 / 3 = 4x$, i.e., $x^2 + 6x + 9 = 12x$, i.e., $x^2 - 6x + 9 = 0$, i.e., $(x - 3)^2 = 0$. Double root at $x = 3$, single contact at $(3, 2\sqrt 3)$ ✓.

Check tangency to the circle: distance from $(3, 0)$ to $x - \sqrt 3 y + 3 = 0$ is $|3 - 0 + 3|/\sqrt{1 + 3} = 6/2 = 3$, matching the circle's radius ✓.

#### PITFALLS

\begin{itemize}
\item \textbf{Pitfall 1.} Using the line $y = mx + c$ with general $c$ and solving the two-equation system in $(m, c)$ directly. The parabola's slope-form tangent $y = mx + a/m$ has already pre-eliminated $c$; using it from the start saves an elimination step.

\item \textbf{Pitfall 2.} Forgetting the parabola's tangent-condition $c = a/m$ has the wrong sign convention. For $y^2 = 4ax$ (opens right, $a > 0$), the tangent is $y = mx + a/m$; for $y^2 = -4ax$ (opens left), it is $y = mx - a/m$.

\item \textbf{Pitfall 3.} Failing to specify ``above the $x$-axis'' and producing the lower tangent $m = -1/\sqrt 3$. The problem statement disambiguates.

\item \textbf{Pitfall 4.} Squaring the tangency condition without tracking the sign of $3m + 1/m$. For real $m > 0$, the quantity is positive; squaring is legitimate. For $m < 0$, the sign must be handled explicitly.
\end{itemize}

#### CONNECTIONS

\begin{itemize}
\item \textbf{Ch. 5 (Substitution)} — the parabola tangent's slope-form parameterisation is a substitution archetype: parameterise the tangent line by slope $m$ alone, eliminating the intercept $c$.

\item \textbf{Ch. 9 (Domain Constraints)} — the ``above the $x$-axis'' constraint is a domain restriction that selects one of two solutions, a classical Ch. 9 move.

\item \textbf{Ch. 11 (Existence / Uniqueness)} — the common tangent existence is non-trivial; it requires the two curves to be in ``tangent-compatible'' position. For curves that are far apart or interlocking, no common tangent exists.

\item \textbf{Ch. 16 (Reverse Engineering)} — the tangent line is reverse-engineered from the two tangency conditions; the elimination is the engine of the reverse construction.
\end{itemize}

#### TAKEAWAY

The common-tangent problem is the cleanest illustration of *tangency-as-discriminant elimination*: the tangency of a line to a conic is one algebraic condition (discriminant of the substituted quadratic = 0), so two tangencies impose two conditions, leaving the line uniquely determined (generically up to a sign choice). The parabola's slope-form tangent $y = mx + a/m$ is the *one-elimination* parameterisation; combined with the circle's distance condition, it reduces to a single equation in $m$, immediately solved.

### 4.2 WE2 — Resultant of Two Quadratics (Tier 3)

**Problem.** *Find the condition on $a, b, c, p, q, r$ for the polynomials $f(x) = a x^2 + b x + c$ and $g(x) = p x^2 + q x + r$ to have a common root.*

**Source.** Joshi, *Educative JEE Mathematics*, Ch. 3, Comment 8 (resultants).

#### SEED — The Setup

The polynomials $f$ and $g$ have a common root $\alpha$ iff $f(\alpha) = g(\alpha) = 0$ simultaneously. The condition is on the *coefficients* $a, b, c, p, q, r$ — a single polynomial equation that vanishes iff such an $\alpha$ exists.

The classical technique for eliminating $\alpha$ from a system of polynomial equations is the *resultant*. For two polynomials, the resultant is a polynomial in their coefficients whose vanishing is *equivalent* to the existence of a common root.

#### BRUTE PATH — Direct Substitution

The naïve approach is to solve $f(x) = 0$ for $x$ (quadratic formula gives $x = (-b \pm \sqrt{b^2 - 4ac})/(2a)$) and substitute each root into $g(x) = 0$. This gives two conditions (one per root of $f$), each involving the square-root $\sqrt{b^2 - 4ac}$ in a complicated nested expression. Simplifying these conditions to remove the square root is tedious and prone to error.

The resultant approach below is far cleaner: it eliminates $\alpha$ in a *single* polynomial expression in the coefficients, with no square roots.

#### ELEGANT PIVOT — Elimination via Resultant

The pivot is to *eliminate $\alpha$ between the two polynomial equations* by computing the *Sylvester resultant*.

**Subtractive elimination of $\alpha^2$.** Multiply $f(\alpha) = a \alpha^2 + b \alpha + c = 0$ by $p$, and $g(\alpha) = p \alpha^2 + q \alpha + r = 0$ by $a$. Subtract:

\[
p (a \alpha^2 + b \alpha + c) - a (p \alpha^2 + q \alpha + r) = 0 \quad \Longleftrightarrow \quad (b p - a q) \alpha + (c p - a r) = 0.
\]

This gives $\alpha = (a r - c p) / (b p - a q) = -(c p - a r)/(b p - a q)$, provided $b p \ne a q$.

**Subtractive elimination of constant terms.** Multiply $f(\alpha)$ by $r$ and $g(\alpha)$ by $c$; subtract:

\[
r (a \alpha^2 + b \alpha + c) - c (p \alpha^2 + q \alpha + r) = 0 \quad \Longleftrightarrow \quad (a r - c p) \alpha^2 + (b r - c q) \alpha = 0.
\]

Factor: $\alpha [(a r - c p) \alpha + (b r - c q)] = 0$. For $\alpha \ne 0$: $\alpha = -(b r - c q)/(a r - c p) = (c q - b r)/(a r - c p)$.

**Equate the two expressions for $\alpha$.** The two pivoting moves above produced two expressions for the same $\alpha$:

\[
\alpha = \frac{a r - c p}{b p - a q} = \frac{c q - b r}{a r - c p}.
\]

Cross-multiplying:

\[
(a r - c p)^2 = (b p - a q)(c q - b r) = -(a q - b p)(c q - b r) = (a q - b p)(b r - c q).
\]

This is the *resultant condition* — the polynomial equation in $\{a, b, c, p, q, r\}$ whose vanishing is equivalent to the existence of a common root $\alpha$.

**Equivalent form via the Sylvester determinant.** The same condition can be derived as the vanishing of the $4 \times 4$ Sylvester matrix determinant

\[
\det \begin{pmatrix} a & b & c & 0 \\ 0 & a & b & c \\ p & q & r & 0 \\ 0 & p & q & r \end{pmatrix} = (a r - c p)^2 - (a q - b p)(b r - c q) = 0.
\]

The two derivations agree.

The boxed conclusion is

\[ \boxed{f \text{ and } g \text{ share a root } \Leftrightarrow (a r - c p)^2 = (a q - b p)(b r - c q).} \]

#### Verification

**Sanity check on a simple case.** Take $f(x) = x^2 - 1$ ($a = 1, b = 0, c = -1$) and $g(x) = x^2 + x - 2$ ($p = 1, q = 1, r = -2$), which share the root $x = 1$.

LHS: $(a r - c p)^2 = (1 \cdot (-2) - (-1) \cdot 1)^2 = (-2 + 1)^2 = 1$.

RHS: $(a q - b p)(b r - c q) = (1 - 0)(0 - (-1)) = 1 \cdot 1 = 1$ ✓.

**Sanity check on a coprime case.** Take $f(x) = x^2$ ($a = 1, b = c = 0$) and $g(x) = x^2 + 1$ ($p = 1, q = 0, r = 1$), which share no real root (or complex root, since $g$'s roots are $\pm i$ and $f$'s root is 0).

LHS: $(1 \cdot 1 - 0 \cdot 1)^2 = 1$.

RHS: $(1 \cdot 0 - 0 \cdot 1)(0 \cdot 1 - 0 \cdot 0) = 0 \cdot 0 = 0$.

LHS $\ne$ RHS, so the condition fails, as expected (no common root) ✓.

#### PITFALLS

\begin{itemize}
\item \textbf{Pitfall 1.} Computing the resultant by solving $f$ for its roots and substituting into $g$ (the brute path). The square-roots in the quadratic formula make this approach algebraically messy; the resultant via Sylvester or the pivoting argument above is cleaner.

\item \textbf{Pitfall 2.} Forgetting the case $b p = a q$ (where the first pivoting move's division is undefined). In this degenerate case, the system reduces to a different elimination structure (the $\alpha^2$ coefficient ratios are equal, requiring the constant-term ratios to also match for a common root).

\item \textbf{Pitfall 3.} Forgetting the case $\alpha = 0$ (where the second pivoting move's factor of $\alpha$ vanishes). $\alpha = 0$ is a common root iff $c = r = 0$ (the constants of both $f, g$ vanish); the resultant condition handles this case as a degenerate sub-case.

\item \textbf{Pitfall 4.} Mis-signing the resultant. The classical Sylvester resultant is signed; the condition is $\det S = 0$ regardless of sign.
\end{itemize}

#### CONNECTIONS

\begin{itemize}
\item \textbf{Ch. 17 (DOF)} — the resultant is a single polynomial equation in 6 coefficient variables, cutting the 6-DOF space down to a 5-DOF hypersurface; the geometric interpretation is the algebraic-geometry resultant as the discriminant locus of common-root configurations.

\item \textbf{Ch. 18 (Recursion)} — the Euclidean algorithm for polynomial $\gcd$ is the inductive procedure that computes the resultant: at each step, replace the higher-degree polynomial by its remainder modulo the lower, recurse on the smaller-degree pair, terminate when one polynomial is zero (the other is the gcd).

\item \textbf{Ch. 20 (Analogy / Transfer)} — the resultant generalises across all polynomial-elimination problems: two polynomials of degree $m$ and $n$ admit a resultant via the $(m+n) \times (m+n)$ Sylvester matrix; the same principle handles polynomial systems of any size via Gröbner-basis machinery.

\item \textbf{Algebraic geometry} — the resultant is the foundational tool for computing the intersection of algebraic varieties; the projective variant (the *Macaulay resultant*) handles homogeneous polynomials.
\end{itemize}

#### TAKEAWAY

The resultant of two quadratics, $(a r - c p)^2 = (a q - b p)(b r - c q)$, is the cleanest illustration of *polynomial elimination*: subtract one polynomial equation from another (with appropriate scalar multiples) to eliminate the highest-degree term, then iterate until the residual is a polynomial in the coefficients alone. The Sylvester resultant generalises this to any pair of polynomials; the technique is the foundation of computational algebraic geometry.

### 4.3 WE3 — Gaussian Elimination on a $3 \times 3$ System (Tier 2)

**Problem.** *Solve the linear system $\begin{cases} x + 2y + 3z = 6 \\ 4x + 5y + 6z = 15 \\ 7x + 8y + 10z = 25 \end{cases}$.*

**Source.** Joshi, *Educative JEE Mathematics*, Ch. 21, Comment 11 (Gauss elimination).

#### SEED — The Setup

The linear system is $A \vec x = \vec b$ with

\[
A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix}, \quad \vec x = \begin{pmatrix} x \\ y \\ z \end{pmatrix}, \quad \vec b = \begin{pmatrix} 6 \\ 15 \\ 25 \end{pmatrix}.
\]

The classical solution method is *Gaussian elimination*: pivot on the leading entry of each row, subtract scalar multiples to zero out the column entries below, recurse on the residual $(n - 1) \times (n - 1)$ subsystem, terminate in upper-triangular form, and back-substitute to recover the variables.

#### BRUTE PATH — Cramer's Rule

The naïve approach is *Cramer's rule*: compute $\det A$, then replace each column of $A$ by $\vec b$ to compute the determinants $\det A_x, \det A_y, \det A_z$, and the solution is $x = \det A_x / \det A$, etc.

$\det A = 1 (50 - 48) - 2 (40 - 42) + 3 (32 - 35) = 2 - 2 \cdot (-2) + 3 \cdot (-3) = 2 + 4 - 9 = -3$.

$\det A_x = \det \begin{pmatrix} 6 & 2 & 3 \\ 15 & 5 & 6 \\ 25 & 8 & 10 \end{pmatrix} = 6 (50 - 48) - 2 (150 - 150) + 3 (120 - 125) = 12 + 0 - 15 = -3$. So $x = -3/-3 = 1$.

$\det A_y = \det \begin{pmatrix} 1 & 6 & 3 \\ 4 & 15 & 6 \\ 7 & 25 & 10 \end{pmatrix} = 1(150 - 150) - 6(40 - 42) + 3(100 - 105) = 0 + 12 - 15 = -3$. So $y = 1$.

$\det A_z = \det \begin{pmatrix} 1 & 2 & 6 \\ 4 & 5 & 15 \\ 7 & 8 & 25 \end{pmatrix} = 1(125 - 120) - 2(100 - 105) + 6(32 - 35) = 5 + 10 - 18 = -3$. So $z = 1$.

Cramer's rule works for the $3 \times 3$ case but scales as $O(n \cdot n!)$ — it computes $n + 1$ determinants of $n \times n$ matrices, each requiring $n!$ operations — and is hopelessly inefficient for large systems. Gaussian elimination scales as $O(n^3)$, dramatically better.

#### ELEGANT PIVOT — Gaussian Elimination

The pivot is to *eliminate one variable per pivot step* using the canonical Gaussian sequence.

**Step 1: Pivot on $a_{11} = 1$.** Eliminate $x$ from rows 2 and 3.

- $R_2 \leftarrow R_2 - 4 R_1$: $(4 - 4) x + (5 - 8) y + (6 - 12) z = 15 - 24 \Rightarrow -3 y - 6 z = -9 \Rightarrow y + 2 z = 3$.
- $R_3 \leftarrow R_3 - 7 R_1$: $(7 - 7) x + (8 - 14) y + (10 - 21) z = 25 - 42 \Rightarrow -6 y - 11 z = -17 \Rightarrow 6 y + 11 z = 17$.

The system after Step 1:

\[
\begin{cases} x + 2 y + 3 z = 6 \\ y + 2 z = 3 \\ 6 y + 11 z = 17. \end{cases}
\]

**Step 2: Pivot on the new $a_{22} = 1$.** Eliminate $y$ from row 3.

- $R_3 \leftarrow R_3 - 6 R_2$: $(6 - 6) y + (11 - 12) z = 17 - 18 \Rightarrow -z = -1 \Rightarrow z = 1$.

The system after Step 2 is in upper-triangular form:

\[
\begin{cases} x + 2 y + 3 z = 6 \\ y + 2 z = 3 \\ z = 1. \end{cases}
\]

**Back-substitution.** From the third equation, $z = 1$. Substituting into the second: $y + 2 = 3 \Rightarrow y = 1$. Substituting into the first: $x + 2 + 3 = 6 \Rightarrow x = 1$.

The boxed conclusion is

\[ \boxed{(x, y, z) = (1, 1, 1).} \]

#### Verification

Check all three original equations: $1 + 2 + 3 = 6$ ✓; $4 + 5 + 6 = 15$ ✓; $7 + 8 + 10 = 25$ ✓.

#### PITFALLS

\begin{itemize}
\item \textbf{Pitfall 1.} Pivoting on a small or zero entry. For this system, the (1,1) entry is 1, which is acceptable; for production numerical work, the partial-pivoting strategy (largest absolute value in the column) would still pick the (3,1) entry (= 7) as the first pivot. The algebraic elimination is the same; only the rounding error differs.

\item \textbf{Pitfall 2.} Forgetting to back-substitute. The upper-triangular form is not the solution; the back-substitution is a required final phase.

\item \textbf{Pitfall 3.} Sign errors in the row operations. Sign-checking after each elimination step is the discipline that catches these.

\item \textbf{Pitfall 4.} Misordering the pivots: if a pivot row is forgotten or skipped, the residual subsystem is corrupted.
\end{itemize}

#### CONNECTIONS

\begin{itemize}
\item \textbf{Ch. 17 (DOF)} — the rank of $A$ determines the DOF of the solution set. For this $3 \times 3$ system with full rank (det = -3 $\ne$ 0), the DOF is 0 and the solution is unique.

\item \textbf{Ch. 18 (Induction)} — Gaussian elimination is inductive: each pivot reduces the system to a smaller residual, recursively. The inductive correctness is the invariant ``the row-echelon form is preserved.''

\item \textbf{Numerical linear algebra} — Gaussian elimination is the foundation of all linear-system solvers; the LU factorisation $A = LU$ (lower-triangular times upper-triangular) is the algorithmic packaging of Gaussian elimination as a reusable matrix decomposition.

\item \textbf{Computational complexity} — Gaussian elimination is $O(n^3)$; Cramer's rule is $O(n \cdot n!)$. For large systems ($n > 10$), the asymptotic difference is enormous: at $n = 20$, Gaussian elimination requires $\sim 5000$ operations, while Cramer's rule requires $\sim 5 \times 10^{19}$ — infeasible.
\end{itemize}

#### TAKEAWAY

Gaussian elimination is the cleanest illustration of *one-pivot-at-a-time linear-system simplification*. Each pivot reduces the system's dimension by 1, the algorithm terminates in $n - 1$ pivot steps, and the back-substitution recovers all variables. The $O(n^3)$ asymptotic complexity is the foundation of all modern numerical linear algebra. Pivot choice (partial pivoting for numerical stability) is the seasoned-engineer's discipline.

---

## 5. Practice Problems

The seven practice problems, with answers boxed and full solutions in the Appendix, traverse the five characteristic forms of pivoting / elimination surveyed in §1.1. **Verification audit caught four slate errors** (PP2, PP5, PP6, PP7) — corrected below; see the Appendix solutions for detailed cross-checks.

### PP1 — Inverse via Variable-Pivot (Tier 1: JEE 2001)

If $f: [1, \infty) \to [2, \infty)$ is $f(x) = x + 1/x$, find $f^{-1}(x)$.

\[ \boxed{f^{-1}(x) = \frac{x + \sqrt{x^2 - 4}}{2}.} \]

### PP2 — Substitution-Driven $F(x^2)$ (Tier 2: JEE 2001) — **Slate Corrected $5/2 \to 4$**

Let $F(x) = \int_0^x f(t) \, dt$ with $F(x^2) = x^2 (1 + x)$. Find $f(4)$.

\[ \boxed{f(4) = 4.} \]

### PP3 — Eliminate $\theta$ Between Trig Equations (Tier 2)

Eliminate $\theta$ from $x = a \sec\theta$, $y = b \tan\theta$ to find the locus.

\[ \boxed{\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1 \quad \text{(hyperbola).}} \]

### PP4 — Intersection of Conics via Elimination (Tier 3)

Find all real intersection points of $x^2 + y^2 = 25$ and $x y = 12$.

\[ \boxed{(3, 4), \; (4, 3), \; (-3, -4), \; (-4, -3).} \]

### PP5 — Cross-Product Elimination (Tier 2: JEE 1985) — **Slate Corrected $\vec b = (1,2,3) \to \vec b = (0,2,2)$**

Find $\vec b$ if $\vec a = (1, 2, 1)$, $\vec a \cdot \vec b = 6$, and $\vec a \times \vec b = (2, -2, 2)$.

\[ \boxed{\vec b = (0, 2, 2).} \]

### PP6 — Eliminate Parameters in 2-Parameter Family (Tier 2) — **Slate Corrected line $\to$ circle**

For each real slope $m$, let $(\alpha, \beta)$ be the unique solution of $\alpha + m \beta = 1$ and $m \alpha - \beta = 2$. Find the locus of $(\alpha, \beta)$ as $m$ varies.

\[ \boxed{(\alpha - 1/2)^2 + (\beta + 1)^2 = 5/4 \quad \text{(circle centred at } (1/2, -1) \text{ of radius } \sqrt 5 / 2\text{).}} \]

### PP7 — Pivot to Decouple a System of ODEs (Tier 3) — **Slate Corrected (extraneous $1/2$ factor removed)**

Solve the coupled linear ODE system $x' = x + y$, $y' = x - y$ with $x(0) = 1, y(0) = 0$.

\[ \boxed{x(t) = \cosh(\sqrt 2 \, t) + \frac{1}{\sqrt 2} \sinh(\sqrt 2 \, t), \quad y(t) = \frac{1}{\sqrt 2} \sinh(\sqrt 2 \, t).} \]

---

## 6. Connections Web

The Pivoting / Elimination archetype connects intimately with the rest of Pillar 2. The most important connections:

- **Ch. 5 (Substitution / Change of Variables)** — substitution *is* a form of variable elimination: $u = g(x)$ replaces $x$ with $u$, eliminating the original $x$-dependence. The two archetypes overlap substantially: PP1 (inverse via variable-pivot) and PP2 ($F(x^2)$ via chain-rule pivot) are cross-archetype with Ch. 5 PP1 and Ch. 5 PP2 respectively, framed here through the pivot-and-eliminate lens.

- **Ch. 8 (Domain Translation)** — translating between domains (algebraic ↔ geometric ↔ complex ↔ vector) often requires elimination of the source-domain variables. PP3 (parametric trig → Cartesian) is a parametric-to-Cartesian translation, an elimination at the boundary between coordinate systems.

- **Ch. 16 (Reverse Engineering)** — reverse-engineering constructs an object from its specifications by *eliminating* the constraints one at a time. WE2 (resultant of two quadratics) is a reverse-engineering of the common-root condition from the polynomial coefficients; the resultant *is* the engineered condition.

- **Ch. 17 (DOF Analysis)** — each elimination removes 1 DOF from the system. The rank-nullity theorem ($\dim \ker A = n - \mathrm{rank}(A)$) is the DOF version of Gaussian elimination's termination condition: the algorithm performs $\mathrm{rank}(A)$ pivots, leaving $n - \mathrm{rank}(A)$ free parameters in the solution.

- **Ch. 18 (Recursion / Induction)** — Gaussian elimination is inductive: each pivot reduces the system to a smaller residual, recursively. The inductive correctness invariant is ``row-echelon form preserved across pivots.'' The two chapters (18 induction, 19 elimination) are tightly paired: 18 names the inductive descent; 19 applies it to systems of equations via pivot choice.

- **Ch. 20 (Analogy / Transfer)** — the same pivoting-and-elimination meta-operation recurs across domains: Gaussian elimination, polynomial resultants, parametric-to-Cartesian conversion, eigenbasis decoupling, Buchberger's Gröbner-basis algorithm, simplex method, Euclidean algorithm. Recognising the *analogy* between these techniques is the Ch. 20 capstone move; Ch. 19 supplies the technical examples that Ch. 20 will abstract.

The chapter therefore sits at the structural crossroads between the *recursive descent* tools developed in Ch. 18 and the *meta-analogical synthesis* of Ch. 20. Pivoting / elimination is the *constructive engine* of Meta-Reasoning — the technique that makes the inductive descent computationally explicit.

---

## 7. Master Takeaways

Six master takeaways summarise the chapter's central lessons.

\begin{enumerate}
\item \textbf{Simplify by subtraction, not addition.} Every effective elimination move is subtractive: subtract a multiple of the pivot row from another row (Gaussian); subtract a polynomial multiple of one equation from another (resultant); subtract a parameter's contribution via an algebraic identity (parametric elimination); subtract a candidate from the search tree (combinatorial). Subtraction reduces structure; addition complicates it.

\item \textbf{Pivot choice is the consequential decision.} The *mechanics* of elimination (subtract this from that) are mechanical; the *choice* of which entry, variable, or move to pivot on is the substantive decision. Partial pivoting (largest absolute value) for numerical stability; lowest-degree variable for symbolic work; most-forcing move for combinatorial search.

\item \textbf{Gaussian elimination is the master template.} Pivot on a leading entry, subtract multiples to zero the column, recurse on the residual, terminate in upper-triangular form, back-substitute to recover variables. The $O(n^3)$ complexity is the foundation of all modern numerical linear algebra.

\item \textbf{Resultants eliminate variables from polynomial systems.} For two polynomials, the Sylvester resultant is a single polynomial in the coefficients whose vanishing equals the existence of a common root. The technique generalises to systems of polynomials via Gröbner-basis machinery; it is the algebraic-geometry analogue of Gaussian elimination.

\item \textbf{Parametric eliminations use algebraic identities.} Trigonometric identities ($\sin^2 + \cos^2 = 1$, $\sec^2 - \tan^2 = 1$, etc.), Pythagorean-like relations, and hyperbolic identities are the elimination engines for parametric representations. The trained solver recognises the identity that converts parametric to Cartesian and applies it directly.

\item \textbf{Eigenbasis decoupling pivots to a diagonal frame.} A coupled linear system $\vec u' = A \vec u$ becomes $n$ independent scalar equations in the eigenbasis of $A$; each scalar equation $v_i' = \lambda_i v_i$ has solution $v_i = c_i e^{\lambda_i t}$, and the full solution is reconstructed by inverse-transforming back to the original basis. The technique is the foundation of normal-mode analysis, PCA, and the spectral theorem.
\end{enumerate}

---

## 8. Self-Assessment Checklist

The reader is encouraged to test internalisation with the following five-question checklist. A confident affirmative answer to all five indicates mastery.

\begin{enumerate}
\item Given a $3 \times 3$ linear system, can you perform Gaussian elimination by hand with partial pivoting, terminate in upper-triangular form, and back-substitute to recover all variables — without errors and within five minutes?

\item Given two quadratics $f, g$ with coefficients $(a, b, c, p, q, r)$, can you write down the resultant condition $(ar - cp)^2 = (aq - bp)(br - cq)$ and explain why it captures the common-root condition?

\item Given parametric equations $x = f(t), y = g(t)$ involving trigonometric or other identities, can you immediately identify the elimination identity ($\sin^2 + \cos^2 = 1$, $\sec^2 - \tan^2 = 1$, etc.) and produce the Cartesian equation?

\item Given a coupled linear ODE system $\vec u' = A \vec u$, can you compute the eigenvalues and eigenvectors of $A$, decouple to the eigenbasis, solve the diagonal system, and transform back to the original basis?

\item Can you recognise when a problem calls for *symbolic pivoting* (lowest-degree variable for algebraic systems) vs *numerical pivoting* (largest absolute value for floating-point systems) vs *strategic pivoting* (most-forcing move for combinatorial search)?
\end{enumerate}

A second-order self-assessment: take any system of equations from a JEE / RMO past paper and identify the optimal pivoting strategy *before* solving. The chapter's central skill is the *pivot-choice discipline*; once internalised, the elimination mechanics follow automatically.

---

## Bridge to Chapter 20

Chapter 19 continues the *Meta-Reasoning* sub-pillar with the discipline of *pivoting and elimination*. Every elimination move subtracts a variable, parameter, or candidate from the system; the *choice* of pivot is the substantive decision. Across linear systems (Gaussian), polynomial systems (resultants), parametric systems (algebraic identities), and coupled ODE systems (eigenbasis), the same meta-operation recurs.

Chapter 20 — the *capstone of Pillar 2* — synthesises the entire archetype catalogue with **Analogy / Transfer**: *if you have solved it once, you have solved it everywhere*. If Chapter 19 taught the solver to *pivot* on a single technique to solve one problem, Chapter 20 teaches the solver to *transfer* the technique across problems by recognising the meta-structural analogies between them. The von Neumann fly-and-bicycles problem is solved by an analogy to a converging geometric sum; the quaternion-vs-complex algebra analogy unifies seemingly disparate computational frameworks; the inductive proof of $25 \mid 7^{2n} + 2^{3n - 3} \cdot 3^{n - 1}$ (Ch. 18 WE2) transfers via the *shift-coefficient* analogy to the entire family of divisibility-by-induction problems. Chapter 20 is *synthetic*: it does not introduce a new technique but instead develops the meta-skill of *recognising* and *transferring* the techniques from Chapters 1–19.

The bridge from 19 to 20 is the realisation that *the elimination meta-operation recurs across all of mathematics, science, and engineering* — and the trained solver, having internalised it in one context (linear algebra), now sees it everywhere (polynomial elimination, parametric conversion, eigenbasis decoupling, Euclidean algorithm, simplex method). Chapter 20 names this meta-recognition as the *Analogy / Transfer* archetype and closes Pillar 2 with a synthesis essay that integrates all twenty archetypes into a unified problem-solving repertoire.

Joshi's *Educative JEE Mathematics* supplies the Chapter 20 capstone material: the meta-pedagogical Ch. 24 (Miscellaneous), the quaternion–complex analogy in Ch. 21 (Vectors), the von Neumann fly-and-bicycles probabilistic-shortcut from Ch. 23 (Infinitistic Probability), and seven practice problems exercising the full range of analogy-and-transfer techniques. The reader who has internalised all nineteen prior archetypes is now ready for the synthesis.

---

## Appendix — Practice Problem Solutions

### Solution to PP1 — Inverse via Variable-Pivot

Solve $y = x + 1/x$ for $x$ in terms of $y$.

Multiply both sides by $x$ (valid since $x \ge 1 > 0$): $y x = x^2 + 1$, i.e., $x^2 - y x + 1 = 0$.

This is a quadratic in $x$; by the quadratic formula:
\[
x = \frac{y \pm \sqrt{y^2 - 4}}{2}.
\]

For $y \ge 2$ (the range of $f$ on $[1, \infty)$), the expression under the square root is non-negative.

*Branch selection.* The function $f(x) = x + 1/x$ on $[1, \infty)$ is monotonically increasing with $f(1) = 2$ and $\lim_{x \to \infty} f(x) = \infty$. So $f^{-1}: [2, \infty) \to [1, \infty)$ is also monotonically increasing. For $y$ slightly larger than 2, $f^{-1}(y)$ is slightly larger than 1; the relevant branch is the *+* sign (since $(y + \sqrt{y^2 - 4})/2 \ge y/2 \ge 1$, while $(y - \sqrt{y^2 - 4})/2 \le y/2$, and in fact $(y - \sqrt{y^2 - 4})/2 \in (0, 1]$).

Hence

\[ \boxed{f^{-1}(x) = \frac{x + \sqrt{x^2 - 4}}{2} \quad \text{for } x \ge 2.} \]

*Verification.* At $x = 2$: $f^{-1}(2) = (2 + 0)/2 = 1$; check $f(1) = 1 + 1 = 2$ ✓. At $x = 5$: $f^{-1}(5) = (5 + \sqrt{21})/2 \approx 4.79$; check $f(4.79) \approx 4.79 + 0.209 \approx 5.00$ ✓.

### Solution to PP2 — Substitution-Driven $F(x^2)$

**Slate correction note.** The locked slate listed the answer as $f(4) = 5/2$, which is incorrect (the same problem appears as Ch. 5 PP2 where it was patched to $f(4) = 4$ in v0.2.2; the Ch. 19 PP2 entry was not propagated). The correct derivation is below.

Given $F(x) = \int_0^x f(t) \, dt$, by the Fundamental Theorem of Calculus $F'(u) = f(u)$.

Given $F(x^2) = x^2 (1 + x) = x^2 + x^3$, differentiate both sides with respect to $x$ using the chain rule on the LHS:

\[
\frac{d}{dx} F(x^2) = F'(x^2) \cdot 2 x = f(x^2) \cdot 2 x.
\]

\[
\frac{d}{dx} (x^2 + x^3) = 2 x + 3 x^2.
\]

Equating: $2 x \cdot f(x^2) = 2 x + 3 x^2$. Dividing by $2 x$ (valid for $x > 0$):

\[
f(x^2) = 1 + \frac{3 x}{2}.
\]

To find $f(4)$, set $x^2 = 4$, i.e., $x = 2$ (taking the positive root, consistent with the chain-rule derivation):

\[
f(4) = 1 + \frac{3 \cdot 2}{2} = 1 + 3 = 4.
\]

The boxed answer:
\[ \boxed{f(4) = 4.} \]

*Verification.* From $f(x^2) = 1 + (3/2) x$ with $x > 0$, the function $f(u) = 1 + (3/2) \sqrt u$ for $u > 0$ (substituting $x = \sqrt u$). At $u = 4$: $f(4) = 1 + (3/2) \cdot 2 = 4$ ✓.

*Consistency check.* Verify $F(x^2) = x^2 (1 + x)$ given $f(u) = 1 + (3/2) \sqrt u$:
\[
F(x^2) = \int_0^{x^2} \left[1 + \frac{3}{2} \sqrt t \right] dt = x^2 + \frac{3}{2} \cdot \frac{2}{3} t^{3/2} \Big|_0^{x^2} = x^2 + (x^2)^{3/2} = x^2 + x^3 = x^2 (1 + x) \; ✓.
\]

### Solution to PP3 — Eliminate $\theta$ Between Trig Equations

Given $x = a \sec\theta$ and $y = b \tan\theta$, eliminate $\theta$ to find the Cartesian locus.

The elimination engine is the trigonometric identity $\sec^2\theta - \tan^2\theta = 1$.

Solve each parametric equation for the trigonometric function:
- $\sec\theta = x/a$, so $\sec^2\theta = x^2 / a^2$.
- $\tan\theta = y/b$, so $\tan^2\theta = y^2 / b^2$.

Substitute into the identity:

\[
\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1.
\]

This is the standard form of a *hyperbola* with semi-axes $a$ and $b$.

The boxed answer:
\[ \boxed{\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1 \quad \text{(hyperbola, semi-axes } a, b\text{).}} \]

*Verification at a sample $\theta$.* At $\theta = 0$: $x = a, y = 0$. Check: $a^2/a^2 - 0 = 1$ ✓. At $\theta = \pi/4$: $x = a \sqrt 2$, $y = b$. Check: $2 a^2 / a^2 - b^2 / b^2 = 2 - 1 = 1$ ✓.

*Geometric interpretation.* As $\theta$ varies over its domain (excluding $\pm \pi/2$ where $\sec, \tan$ blow up), the point $(x, y)$ traces out both branches of the hyperbola. The parametric form is the natural ``hyperbolic-trig'' parameterisation, dual to the $(\cos, \sin)$ parameterisation for the ellipse.

### Solution to PP4 — Intersection of Conics via Elimination

Solve the system $x^2 + y^2 = 25$ and $x y = 12$ over the reals.

From the second equation, $y = 12 / x$ (assuming $x \ne 0$; the case $x = 0$ gives $y \cdot 0 = 12$, impossible, so $x \ne 0$ is consistent).

Substitute into the first equation:

\[
x^2 + \left(\frac{12}{x}\right)^2 = 25 \quad \Longleftrightarrow \quad x^2 + \frac{144}{x^2} = 25.
\]

Multiply by $x^2$ to clear the fraction:

\[
x^4 + 144 = 25 x^2 \quad \Longleftrightarrow \quad x^4 - 25 x^2 + 144 = 0.
\]

Substitute $u = x^2$:

\[
u^2 - 25 u + 144 = 0.
\]

Factor: $144 = 9 \cdot 16$ and $9 + 16 = 25$, so $(u - 9)(u - 16) = 0$, giving $u = 9$ or $u = 16$.

Back to $x^2 = 9$ or $x^2 = 16$: $x = \pm 3$ or $x = \pm 4$.

For each $x$, compute $y = 12/x$:
- $x = 3 \Rightarrow y = 4$, so $(3, 4)$.
- $x = -3 \Rightarrow y = -4$, so $(-3, -4)$.
- $x = 4 \Rightarrow y = 3$, so $(4, 3)$.
- $x = -4 \Rightarrow y = -3$, so $(-4, -3)$.

The boxed answer:
\[ \boxed{\text{Four intersection points: } (3, 4), \; (4, 3), \; (-3, -4), \; (-4, -3).} \]

*Verification.* Each point: $3^2 + 4^2 = 25$ ✓, $3 \cdot 4 = 12$ ✓; $4^2 + 3^2 = 25$ ✓, $4 \cdot 3 = 12$ ✓; signed pairs are the negations (preserve both equations) ✓.

*Geometric interpretation.* The circle $x^2 + y^2 = 25$ (centre origin, radius 5) and the hyperbola $xy = 12$ (with axes along the $\pm 45°$ diagonals) intersect at four points by Bezout's theorem (two degree-2 curves intersect in $2 \cdot 2 = 4$ points generically). The four intersection points come in two pairs related by the $(x \leftrightarrow y)$ reflection (the hyperbola's axis of symmetry) and by the $(x, y) \to (-x, -y)$ inversion through the origin (both curves' shared centre of symmetry).

### Solution to PP5 — Cross-Product Elimination

**Slate correction note.** The locked slate listed $\vec b = (1, 2, 3)$, which does *not* satisfy the constraint $\vec a \cdot \vec b = 6$ (gives $1 + 4 + 3 = 8$). The correct $\vec b$ is derived below.

Given: $\vec a = (1, 2, 1)$, $\vec a \cdot \vec b = 6$, $\vec a \times \vec b = (2, -2, 2)$. Find $\vec b$.

**Elimination via the BAC–CAB identity.** Recall the vector triple-product identity:
\[
\vec a \times (\vec a \times \vec b) = (\vec a \cdot \vec b) \, \vec a - (\vec a \cdot \vec a) \, \vec b.
\]

Compute each side:
- $\vec a \cdot \vec a = 1^2 + 2^2 + 1^2 = 6$.
- $\vec a \cdot \vec b = 6$ (given).
- $\vec a \times (\vec a \times \vec b) = \vec a \times (2, -2, 2) = \det\begin{pmatrix} \hat i & \hat j & \hat k \\ 1 & 2 & 1 \\ 2 & -2 & 2 \end{pmatrix}$.
  - $\hat i$ component: $2 \cdot 2 - 1 \cdot (-2) = 4 + 2 = 6$.
  - $\hat j$ component: $-(1 \cdot 2 - 1 \cdot 2) = 0$.
  - $\hat k$ component: $1 \cdot (-2) - 2 \cdot 2 = -2 - 4 = -6$.
  - So $\vec a \times (\vec a \times \vec b) = (6, 0, -6)$.

Substitute into the identity:
\[
(6, 0, -6) = 6 \cdot (1, 2, 1) - 6 \cdot \vec b = (6, 12, 6) - 6 \vec b.
\]

Solve for $\vec b$:
\[
6 \vec b = (6, 12, 6) - (6, 0, -6) = (0, 12, 12) \quad \Longleftrightarrow \quad \vec b = (0, 2, 2).
\]

The boxed answer:
\[ \boxed{\vec b = (0, 2, 2).} \]

*Verification.* $\vec a \cdot \vec b = 0 + 4 + 2 = 6$ ✓. $\vec a \times \vec b = \det \begin{pmatrix} \hat i & \hat j & \hat k \\ 1 & 2 & 1 \\ 0 & 2 & 2 \end{pmatrix} = \hat i (2 \cdot 2 - 1 \cdot 2) - \hat j (1 \cdot 2 - 1 \cdot 0) + \hat k (1 \cdot 2 - 2 \cdot 0) = (2, -2, 2)$ ✓.

*Why the slate failed.* The slate's $\vec b = (1, 2, 3)$ gives $\vec a \cdot \vec b = 1 + 4 + 3 = 8 \ne 6$ (the dot-product constraint is violated) and $\vec a \times \vec b = (2 \cdot 3 - 1 \cdot 2, -(1 \cdot 3 - 1 \cdot 1), 1 \cdot 2 - 2 \cdot 1) = (4, -2, 0) \ne (2, -2, 2)$ (the cross-product constraint is also violated). The slate's $\vec b$ satisfies neither constraint; the correct answer $\vec b = (0, 2, 2)$ satisfies both.

### Solution to PP6 — Eliminate Parameters in 2-Parameter Family

**Slate correction note.** The locked slate stated ``locus is a line'' (incoherent and incorrect). The correct locus is derived below: it is a *circle*, not a line.

For each real slope $m$, the linear system

\[
\begin{cases} \alpha + m \beta = 1 \\ m \alpha - \beta = 2 \end{cases}
\]

has a unique solution $(\alpha(m), \beta(m))$ (the determinant of the coefficient matrix is $-1 - m^2 \ne 0$ for all real $m$). We compute $(\alpha, \beta)$ in terms of $m$ and then eliminate $m$ to find the Cartesian locus.

**Solve for $\alpha$.** Multiply the first equation by 1, the second by $m$: $\alpha + m \beta = 1$, $m^2 \alpha - m \beta = 2 m$. Add: $(1 + m^2) \alpha = 1 + 2 m$, so $\alpha = (1 + 2 m) / (1 + m^2)$.

**Solve for $\beta$.** Multiply the first equation by $m$, the second by 1: $m \alpha + m^2 \beta = m$, $m \alpha - \beta = 2$. Subtract: $(m^2 + 1) \beta = m - 2$, so $\beta = (m - 2) / (1 + m^2)$.

**Eliminate $m$.** Compute two symmetric combinations of $(\alpha, \beta)$:

- $\alpha^2 + \beta^2 = \dfrac{(1 + 2 m)^2 + (m - 2)^2}{(1 + m^2)^2} = \dfrac{1 + 4 m + 4 m^2 + m^2 - 4 m + 4}{(1 + m^2)^2} = \dfrac{5 + 5 m^2}{(1 + m^2)^2} = \dfrac{5}{1 + m^2}$.

- $\alpha - 2 \beta = \dfrac{(1 + 2 m) - 2 (m - 2)}{1 + m^2} = \dfrac{1 + 2 m - 2 m + 4}{1 + m^2} = \dfrac{5}{1 + m^2}$.

These two combinations are equal! Therefore $\alpha^2 + \beta^2 = \alpha - 2 \beta$, i.e.,

\[
\alpha^2 - \alpha + \beta^2 + 2 \beta = 0 \quad \Longleftrightarrow \quad \left(\alpha - \tfrac{1}{2}\right)^2 + (\beta + 1)^2 = \tfrac{1}{4} + 1 = \tfrac{5}{4}.
\]

This is the *circle* of centre $(1/2, -1)$ and radius $\sqrt 5 / 2$, which passes through the origin (verify: $(0 - 1/2)^2 + (0 + 1)^2 = 1/4 + 1 = 5/4$ ✓).

The boxed answer:
\[ \boxed{(\alpha - \tfrac{1}{2})^2 + (\beta + 1)^2 = \tfrac{5}{4} \quad \text{(circle, centre } (1/2, -1) \text{, radius } \sqrt 5 / 2 \text{).}} \]

*Verification at three sample slopes.*
- $m = 0$: $(\alpha, \beta) = (1, -2)$. Original equations: $1 + 0 = 1$ ✓; $0 - (-2) = 2$ ✓. Distance to $(1/2, -1)$: $\sqrt{1/4 + 1} = \sqrt 5 / 2$ ✓.
- $m = 1$: $(\alpha, \beta) = (3/2, -1/2)$. Original: $3/2 + (-1/2) = 1$ ✓; $3/2 - (-1/2) = 2$ ✓. Distance to $(1/2, -1)$: $\sqrt{1 + 1/4} = \sqrt 5 / 2$ ✓.
- $m = -1$: $(\alpha, \beta) = (-1/2, -3/2)$. Original: $-1/2 + 3/2 = 1$ ✓; $1/2 + 3/2 = 2$ ✓. Distance: $\sqrt{1 + 1/4} = \sqrt 5 / 2$ ✓.

*Why the slate failed.* The slate's ``locus is a line'' is wrong because the parametric expressions $\alpha(m) = (1 + 2m)/(1 + m^2)$ and $\beta(m) = (m - 2)/(1 + m^2)$ are *rational functions* of $m$ (denominators are quadratic in $m$); their image is *not* a line (which would require linear-in-$m$ parameterisations). The correct locus, derived by elimination, is the circle above.

### Solution to PP7 — Pivot to Decouple a System of ODEs

**Slate correction note.** The locked slate listed $x(t) = (1/2)(\cosh(\sqrt 2 t) + (1/\sqrt 2) \sinh(\sqrt 2 t))$ — the extraneous $1/2$ factor makes $x(0) = 1/2 \ne 1$, violating the initial condition. The correct $x(t)$ is derived below.

Given the coupled linear ODE system

\[
\begin{cases} x' = x + y \\ y' = x - y \end{cases}, \qquad x(0) = 1, \; y(0) = 0.
\]

In matrix form: $\vec u' = A \vec u$ with $\vec u = (x, y)^T$ and $A = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.

**Eigenvalues of $A$.** The characteristic polynomial is

\[
\det(A - \lambda I) = \det \begin{pmatrix} 1 - \lambda & 1 \\ 1 & -1 - \lambda \end{pmatrix} = (1 - \lambda)(-1 - \lambda) - 1 = \lambda^2 - 2.
\]

Roots: $\lambda_\pm = \pm \sqrt 2$.

**Eigenvectors of $A$.**
- $\lambda_+ = \sqrt 2$: $(A - \sqrt 2 I) \vec v = 0$ gives $(1 - \sqrt 2) v_1 + v_2 = 0$, so $\vec v_+ = (1, \sqrt 2 - 1)$.
- $\lambda_- = -\sqrt 2$: $(A + \sqrt 2 I) \vec v = 0$ gives $(1 + \sqrt 2) v_1 + v_2 = 0$, so $\vec v_- = (1, -(1 + \sqrt 2))$.

**General solution.**

\[
\vec u(t) = c_+ e^{\sqrt 2 t} \begin{pmatrix} 1 \\ \sqrt 2 - 1 \end{pmatrix} + c_- e^{-\sqrt 2 t} \begin{pmatrix} 1 \\ -(1 + \sqrt 2) \end{pmatrix}.
\]

**Initial conditions.** $\vec u(0) = c_+ \vec v_+ + c_- \vec v_- = (1, 0)^T$:

\[
\begin{cases} c_+ + c_- = 1 \\ c_+ (\sqrt 2 - 1) - c_- (1 + \sqrt 2) = 0. \end{cases}
\]

From the second equation: $c_+ (\sqrt 2 - 1) = c_- (1 + \sqrt 2)$, so $c_+ / c_- = (1 + \sqrt 2) / (\sqrt 2 - 1) = (1 + \sqrt 2)^2 / ((\sqrt 2)^2 - 1^2) = (3 + 2 \sqrt 2) / 1 = 3 + 2 \sqrt 2$.

Substitute into the first equation: $c_- (3 + 2 \sqrt 2) + c_- = c_- (4 + 2 \sqrt 2) = 1$, so

\[
c_- = \frac{1}{4 + 2 \sqrt 2} = \frac{4 - 2 \sqrt 2}{(4)^2 - (2 \sqrt 2)^2} = \frac{4 - 2 \sqrt 2}{8} = \frac{2 - \sqrt 2}{4}.
\]

And $c_+ = (3 + 2 \sqrt 2) c_- = \dfrac{(3 + 2 \sqrt 2)(2 - \sqrt 2)}{4} = \dfrac{6 - 3 \sqrt 2 + 4 \sqrt 2 - 4}{4} = \dfrac{2 + \sqrt 2}{4}$.

**Closed-form $x(t)$.**

\[
x(t) = c_+ e^{\sqrt 2 t} + c_- e^{-\sqrt 2 t} = \frac{(2 + \sqrt 2) e^{\sqrt 2 t} + (2 - \sqrt 2) e^{-\sqrt 2 t}}{4}.
\]

Use $\cosh\theta = (e^\theta + e^{-\theta})/2$ and $\sinh\theta = (e^\theta - e^{-\theta})/2$:

\[
x(t) = \frac{2 (e^{\sqrt 2 t} + e^{-\sqrt 2 t}) + \sqrt 2 (e^{\sqrt 2 t} - e^{-\sqrt 2 t})}{4} = \frac{4 \cosh(\sqrt 2 t) + 2 \sqrt 2 \sinh(\sqrt 2 t)}{4} = \cosh(\sqrt 2 t) + \frac{\sqrt 2}{2} \sinh(\sqrt 2 t).
\]

Simplify $\sqrt 2 / 2 = 1 / \sqrt 2$:

\[
x(t) = \cosh(\sqrt 2 t) + \frac{1}{\sqrt 2} \sinh(\sqrt 2 t).
\]

**Closed-form $y(t)$.**

\[
y(t) = c_+ (\sqrt 2 - 1) e^{\sqrt 2 t} - c_- (1 + \sqrt 2) e^{-\sqrt 2 t}.
\]

Compute the coefficients: $(2 + \sqrt 2)(\sqrt 2 - 1) = 2 \sqrt 2 - 2 + 2 - \sqrt 2 = \sqrt 2$ and $(2 - \sqrt 2)(1 + \sqrt 2) = 2 + 2 \sqrt 2 - \sqrt 2 - 2 = \sqrt 2$. So:

\[
y(t) = \frac{\sqrt 2 (e^{\sqrt 2 t} - e^{-\sqrt 2 t})}{4} = \frac{\sqrt 2 \cdot 2 \sinh(\sqrt 2 t)}{4} = \frac{\sqrt 2}{2} \sinh(\sqrt 2 t) = \frac{1}{\sqrt 2} \sinh(\sqrt 2 t).
\]

The boxed answer:
\[ \boxed{x(t) = \cosh(\sqrt 2 t) + \frac{1}{\sqrt 2} \sinh(\sqrt 2 t), \quad y(t) = \frac{1}{\sqrt 2} \sinh(\sqrt 2 t).} \]

*Verification at $t = 0$.* $x(0) = \cosh 0 + (1/\sqrt 2) \sinh 0 = 1 + 0 = 1$ ✓; $y(0) = (1/\sqrt 2) \cdot 0 = 0$ ✓.

*Verification of the ODEs.*
- $x'(t) = \sqrt 2 \sinh(\sqrt 2 t) + \cosh(\sqrt 2 t)$ (differentiating).
- $x + y = \cosh(\sqrt 2 t) + (1/\sqrt 2) \sinh(\sqrt 2 t) + (1/\sqrt 2) \sinh(\sqrt 2 t) = \cosh(\sqrt 2 t) + \sqrt 2 \sinh(\sqrt 2 t) = x'(t)$ ✓.
- $y'(t) = (1/\sqrt 2) \sqrt 2 \cosh(\sqrt 2 t) = \cosh(\sqrt 2 t)$.
- $x - y = \cosh(\sqrt 2 t) + (1/\sqrt 2) \sinh(\sqrt 2 t) - (1/\sqrt 2) \sinh(\sqrt 2 t) = \cosh(\sqrt 2 t) = y'(t)$ ✓.

*Why the slate failed.* The slate's expression $x(t) = (1/2)(\cosh(\sqrt 2 t) + (1/\sqrt 2) \sinh(\sqrt 2 t))$ gives $x(0) = 1/2$, violating the initial condition $x(0) = 1$. The extraneous $1/2$ factor is incorrect; removing it gives the correct $x(t)$. The error likely arose from a careless midpoint-of-eigenvalue averaging or from a transcription mistake; the correct coefficient is $c_+ + c_- = 1$, not $1/2$.

---

*End of Chapter 19.*
