---
chapter: 9
archetype: Domain Constraints / Bounds
subtitle: "Algebra Generates Candidates; Domain Selects the Winner"
category: Constraint Exploitation (Archetypes 9–12) — opening chapter
related_archetypes: [1, 10, 11, 14, 17]
key_gems: [A16, A17, C16]
  - "Triangle inequality $|x - y| < z$, $|y - z| < x$, $|x - z| < y$ for sides of a non-degenerate triangle"
  - "Heron's formula $K = \\sqrt{s(s-a)(s-b)(s-c)}$ with $s = (a+b+c)/2$"
  - "$r = K/s$ (inradius) and $R = abc / (4K)$ (circumradius)"
  - "Euler's inequality $R \\ge 2r$ for every triangle, with equality iff equilateral; proved by $OI^2 = R(R - 2r) \\ge 0$"
  - "Domain of $f_1 + f_2$ (or $f_1 \\cdot f_2$, or any pointwise combination) is $D_1 \\cap D_2$ — the intersection, never the union"
  - "Logarithm $\\log_b x$ requires $x > 0$, $b > 0$, $b \\ne 1$"
  - "Square root $\\sqrt{x}$ (real-valued) requires $x \\ge 0$"
  - "Range bounds $\\sin x, \\cos x \\in [-1, 1]$ cascade through composition: $|\\sin(\\cos x)| \\le \\sin 1$"
  - "Discriminant condition $b^2 - 4ac \\ge 0$ for real roots of $ax^2 + bx + c$, generalising to $\\Delta \\ge 0$ for higher-order reality conditions"
  - "Algebraic identity $x^2(y-z) + y^2(z-x) + z^2(x-y) = (x-y)(y-z)(x-z)$"
canonical_takeaway: "Algebra generates candidates; the domain selects the winner."
status: locked
last_revised: 2026-05-29
locked_on: 2026-05-29
sourcing_note: "All worked examples and practice problems in this chapter are drawn from K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), or from JEE / RMO / INMO examinations commented on in that text. See Blueprint §6.2 for the sourcing rule and `pillar2-archetypes/_template/joshi-problems-locked.md` §Ch. 9 for the locked slate. **Verification audit for this chapter discovered one slate-listing typo**: PP1 (integer-$m$ count) listed the two valid $m$-values as $\\{-1, 2\\}$, but the correct pair is $\\{-1, -2\\}$. The *count* of $2$ values is correct; only the second-listed value was a copy-typo. Patched in slate v0.2.6; see PP1 solution in the appendix for the corrected derivation."
---

# Chapter 9 — Domain Constraints / Bounds

## *Algebra Generates Candidates; Domain Selects the Winner*

---

## Opening Vignette

A clinical pharmacist in a hospital pharmacy receives a written order from a paediatric oncologist: *administer methotrexate at $12\,\text{mg}/\text{m}^2$ to a child with a body-surface area of $0.83\,\text{m}^2$*. She multiplies: $12 \times 0.83 = 9.96\,\text{mg}$. The arithmetic is correct. The number is real, positive, and clinically plausible. But she does not write the prescription for $9.96\,\text{mg}$. She writes it for $10\,\text{mg}$ — because the drug is supplied only in $2.5\,\text{mg}$ tablets, and $9.96$ is not a multiple of $2.5$. Then she pauses. She checks the formulary: the maximum single-dose tolerated for a child of that surface area is $15\,\text{mg}$ — her $10$ passes. She checks the cumulative weekly dose: the child has had three earlier doses this week, total $30\,\text{mg}$, and the weekly cap is $40$; her $10$ would bring the total to exactly $40$, hitting the ceiling. She checks contraindications: the child is on a folate-rescue protocol that requires a six-hour delay after each dose, and the next dose is due at $14{:}00$, exactly six hours after the previous; her $10$ at $14{:}00$ is compatible. She checks renal function: creatinine clearance is $48\,\text{mL/min}$, above the cutoff of $30$; her $10$ is safe. Only after every constraint clears does she scan the prescription into the dispensing system. The arithmetic produced a candidate dose; the *domain envelope* — pill sizes, weekly cap, scheduling rules, organ function — produced the prescription. The arithmetic, by itself, was always insufficient.

Now turn to a different scene. A land surveyor in northern Karnataka is asked to verify the boundaries of a triangular plot whose sides the owner claims are $40\,\text{m}$, $50\,\text{m}$, and $100\,\text{m}$. She measures with her electronic distance meter: the three numbers come back as advertised, within instrument tolerance. The three numbers are real, positive, all in reasonable units; algebraically there is nothing wrong with them. But she immediately knows something is wrong, because no plane triangle can have these three sides: $40 + 50 = 90 < 100$, and a triangle's *third side must be strictly less than the sum of the other two*. She drives back to the field, this time walking the boundary with her own pace, and discovers that one of the boundary stones had been moved during a fencing dispute, displacing one corner by $11\,\text{m}$ — turning a $50\,\text{m}$ side into something that *measured* $50$ but was *positioned* wrong. The arithmetic measurements were correct in isolation; the triangle-existence domain — that the three sides must satisfy the triangle inequality — rejected them as a whole.

These two scenes look unrelated. A pharmacist filling a prescription; a surveyor checking a plot. They share one of the most consequential observations in applied mathematics, and one of the most underused observations in Indian competition mathematics. In each, *the algebra (or the measurement) generated a candidate*, and *the domain (of allowable values, of geometric existence, of regulatory compliance) filtered the candidate against constraints that the algebra by itself could not see*. The pharmacist's $9.96\,\text{mg}$ became $10\,\text{mg}$ because of the discrete domain of available pill sizes. The surveyor's three numbers became "no triangle" because of the triangle-existence constraint. Neither professional was confused or sloppy; both were applying *the second step of every careful quantitative analysis* — the step that the first step (the algebra, the measurement) cannot perform on itself. *The candidate-generation step and the domain-filtering step are two steps; conflating them is the most common source of error in JEE problems where students get the algebra right but the answer wrong.*

This is *Domain Constraints / Bounds*. It is the first archetype of the *Constraint Exploitation* sub-pillar (Chapters 9–12), and where Method Selection (Chapters 5–8) was about choosing the right *representation* of a problem, Constraint Exploitation is about *using the restrictions* that the problem's natural setting imposes. The move appears under many names — *domain analysis*, *feasibility check*, *constraint propagation*, *type-checking*, *triangle-inequality verification*, *discriminant analysis*, *range bounding*, *integer-solution filtering*, *non-degeneracy condition* — and it appears in every problem that has a natural setting. What unifies them is the same logic: *the algebra generates a set of candidate solutions; the domain envelope selects which of those candidates are real solutions; the algebra alone is necessary but never sufficient*.

Section 4.1 of Chapter 1 (Invariance) already introduced the two-step *candidate-then-filter* pattern as one of the four ways an invariant operates. This chapter elevates the filter step itself to a named archetype, traces its forms across mathematical sub-disciplines, and exhibits the catastrophic JEE failure modes that occur when the filter is skipped.

> *Algebra generates candidates; the domain selects the winner.*

---

## 1. The Archetype Defined

### 1.1 Formal Definition

We make the intuition precise.

\begin{definition}[Domain Constraint / Bound]
A *domain constraint* (or *domain bound*) on a problem with variables $x_1, \ldots, x_n$ is a specification of the *domain* $D \subseteq \mathbb{R}^n$ (or $\mathbb{C}^n$, or any appropriate ambient space) of admissible values: only $(x_1, \ldots, x_n) \in D$ are *solutions* to the problem, regardless of whether they satisfy the problem's algebraic equations. A *solution* is a point that simultaneously satisfies the algebraic equations *and* lies in $D$. The *candidate set* generated by the algebra alone may be strictly larger than $D$; the actual solution set is the intersection.
\end{definition}

Three remarks unpack the abstraction. First, the *domain* $D$ encodes everything that the problem's setting requires of its variables — positivity, integrality, real-valuedness, the inside of a triangle, the upper half-plane, the unit interval, a probability simplex, the natural numbers, whatever the problem demands. The domain is *not* derived from the algebra; it is *separately given* by the problem's statement (often implicitly), and the solver's first task is to read it correctly. A problem that says *"let $x$ be a positive real"* has $D = \mathbb{R}_{>0}$; a problem about *"the sides of a triangle"* has $D = \{(a, b, c) \in \mathbb{R}_{>0}^3 : a + b > c, b + c > a, c + a > b\}$; a problem about *"the number of subsets"* has $D = \mathbb{Z}_{\ge 0}$; a problem about *"the inradius and circumradius of a triangle"* has $D = \{(r, R) : 0 < r \le R/2\}$ by Euler's inequality.

Second, the *candidate set* is the set of points that satisfy the algebraic equations *without regard to the domain*. The algebra is structurally blind to the domain: solving a quadratic by the quadratic formula produces two roots irrespective of whether they are positive, whether they are integers, whether they correspond to triangles, whether they lie in $[-1, 1]$. The candidate set is *what the algebra produces*; the solution set is *the candidate set restricted to $D$*. A problem whose algebraic candidate set has $k$ elements and whose intersection with $D$ has $\ell$ elements has *$\ell$ solutions*, not $k$.

Third, the move splits naturally into two operations: *enumerate the candidates* (do the algebra) and *filter against $D$* (apply the domain constraints). The two operations are essentially independent — the algebra does not depend on the domain (except in the sense that the domain is what tells the solver to do the algebra at all), and the filter does not depend on the algebra's internal mechanics (only on its outputs). The pedagogical observation, repeated by every JEE coach, is that students typically remember the first operation and forget the second; the answer they report is the candidate set, not the solution set.

In this chapter we encounter four characteristic forms of domain constraint. The four forms together cover essentially every JEE-level instance.

- **Form I — Function-domain constraints (analytic).** The natural domain of an analytic expression is the set on which every sub-expression is defined: $\log_b x$ requires $x > 0$, $b > 0$, $b \ne 1$; $\sqrt{x}$ (real-valued) requires $x \ge 0$; $1/x$ requires $x \ne 0$; $\arcsin x, \arccos x$ require $x \in [-1, 1]$; $\arctan x$ is total. The domain of a *combination* of functions is the *intersection* of the individual domains. *Examples.* WE1 (the domain of $f_1 + f_2$), PP3 (domain of a difference of two logarithms).

- **Form II — Number-theoretic constraints (integrality, divisibility, rationality).** Many JEE and RMO problems restrict variables to $\mathbb{Z}$, $\mathbb{N}$, $\mathbb{Q}$, or some divisibility-defined sub-lattice. The algebra generates real-valued candidates; the integrality filter selects which are admissible. The remedy is often a divisor count or a congruence analysis. *Examples.* WE2 (positive-integer $n$ from a binomial-coefficient equation), PP1 (integer $m$ values forcing integer $x$-coordinate), PP2 (consecutive-integer triangle sides).

- **Form III — Geometric existence constraints (non-degeneracy).** A configuration must *actually exist* as a geometric object: a triangle's three sides must satisfy the triangle inequality; a quadrilateral's angles must sum to $2\pi$; a chord must have positive length; a tangent must touch the curve at a single point. *Examples.* WE3 (triangle-inequality bound on a symmetric expression), PP2 (consecutive-integer triangle), PP6 (Euler's inequality bounding $r/R$), PP7 (height-distance with same-side vs. opposite-side cases).

- **Form IV — Reality / discriminant constraints (algebraic positivity).** A polynomial equation has real roots iff its discriminant is non-negative; a quadratic form is positive-definite iff its principal minors are positive; a probability distribution is admissible iff its density is non-negative and integrates to $1$. *Examples.* PP4 (quartic with all real roots), PP5 (range bound from trig composition restricts solutions).

### 1.2 The Core Principle

The principle of domain constraints, stripped to its essence, is one sentence.

> *Algebra generates candidates; the domain selects the winner.*

This sentence inverts an instinct that algebra-fluent students cultivate inadvertently. A student who is good at algebra learns to *trust the algebra* — to set up the equations, manipulate them, solve them, and report the answer. The instinct serves them well at the level of straightforward equation-solving. But the instinct has a structural blind spot: it treats *the algebra as if it were the entire problem*, forgetting that the algebra was always operating inside a domain that the problem statement specified. A quadratic equation with two complex-conjugate roots is *no solution* to a "find the real number $x$" problem, not "two solutions." A trigonometric equation whose general solution includes $x = 3\pi$ is *no solution* to a problem on $[0, 2\pi]$. A formula that yields $-3$ is *no solution* to a "number of pencils" problem.

Domain Constraints is the discipline of breaking the trust in algebra at exactly the right moment — *after* the algebra has produced candidates but *before* any answer is reported — and inserting an explicit check: *do the candidates lie in the domain the problem asked for?* The check costs seconds; the omission of the check costs marks on every JEE paper.

The principle also imposes a positive discipline: when the algebra produces *no* candidate that lies in the domain, the correct answer is *no solution* (or *no triangle*, *no integer $m$*, etc.). This is a substantive answer, not a sign of failure. A surprising number of JEE problems have *no solution* as the intended answer; a student who reports "I tried but the algebra gave a nonsense answer" is reading the problem wrong. The algebra succeeded; the domain filtered; the filtered result is *no solution*.

### 1.3 The Cognitive Shift

The cognitive shift Domain Constraints enforces is from *"algebra is the answer"* to *"algebra is the candidate-generator; the domain is the filter."* This is, at first, a small reframing. In practice, it changes everything about how a problem is processed. The student who has internalised the shift opens each problem by asking *what is the domain?* — separately from *what is the equation?* — and writes the domain down in the margin before starting. The domain accompanies the algebra throughout, and the final answer is *the algebraic candidates ∩ the domain*. Without the discipline, the domain is recalled (if at all) only after the algebra has finished, and only when something in the result looks suspicious enough to prompt a check.

A second shift, less obvious, is from *"the domain is a side condition"* to *"the domain is a co-equal half of the problem."* In a well-posed JEE problem, the domain is part of the problem statement, not an afterthought. *"For positive reals $a, b, c$ that are sides of a triangle, prove ..."* — the qualifier *"that are sides of a triangle"* is not background colour; it is the second-most-important sentence in the problem (after the inequality itself). The same is true of *"for $x \in [0, 2\pi]$"*, of *"for integer $n$"*, of *"for $z$ on the unit circle"*. The trained solver reads the domain with the same precision as the equation, because the domain often *makes the problem solvable* (by ruling out the infinite candidate set that would otherwise apply) or *forces a particular answer* (by intersecting with a finite candidate set).

A third shift is from *"the domain is checked at the end"* to *"the domain is exploited throughout."* The most powerful uses of domain constraints are not as a final filter but as a *structuring device*. WE3 (the triangle-inequality bound) is an example: the algebra produces a quantity $(x-y)(y-z)(x-z)$, and the domain ($x, y, z$ are triangle sides) bounds each factor; the bound is *combined with the algebraic identity* to produce the result. The domain is not consulted at the end; it is consulted at every step, and the algebra is *guided* by what the domain allows. The trained solver uses the domain as a positive tool, not a negative gate.

---

## 2. The Deep Structure

### 2.1 Mathematical Foundations

Domain constraints rest on three formal foundations.

The first is the *intersection structure of admissibility*. When a problem imposes multiple domain constraints — *$x$ is positive AND an integer AND less than $100$ AND not a multiple of $7$* — the admissible domain is the *intersection* of the four constraint sets. Each constraint defines a subset of the ambient space; the admissible set is the meet of those subsets. The intersection structure is *contravariant* in the number of constraints: each additional constraint can only shrink (or leave unchanged) the admissible set. The corollary is a useful one: *the more constrained a problem, the smaller its solution set, and often the easier the problem*. WE1 illustrates this in miniature: the domain of $f_1 + f_2$ is the *intersection* $D_1 \cap D_2$, not the union, because the sum is defined precisely where *both* summands are defined.

The second is the *separation of the candidate-generation and filtering steps*. The candidate set is determined by the algebraic structure of the problem alone; the filter is determined by the domain alone; the solution set is their intersection. This separation has both pedagogical and computational value. *Pedagogically*: students who have one or the other but not both succeed at part of the problem and fail at the other part. The remedy is the explicit two-step format: list candidates, then filter. *Computationally*: in constraint-satisfaction programming (which underpins SAT solvers, integer programming, and constraint logic programming), the separation is built into the algorithmic structure — generate-and-test, branch-and-bound, constraint propagation. The mathematical move that this chapter elevates to an archetype is what computer science has elevated to an entire discipline.

The third foundation is the role of the *existence quantifier*. Many problems ask *do there exist values in the domain satisfying the equation?* — the answer being either *yes (with examples)* or *no (with a proof of non-existence)*. WE3 is an instance: the question is whether the triangle inequality on $x, y, z$ forces an inequality on a symmetric expression, and the answer is *yes, the algebraic bound is forced by the domain*. PP3 (number of real solutions of $\sin(\cos x) = x$) is another: the algebra produces a candidate equation, the domain (the range of $\sin(\cos x)$) intersects with the candidate domain ($x \in [-\pi, \pi]$) to give the intersection $[-\sin 1, \sin 1]$, and the equation on that intersection is shown to have *exactly one* solution. The existence quantifier is the natural language for the question; the candidate-filter framework is the natural method.

A deeper foundation, beyond the chapter's required machinery, is the *theory of constraint satisfaction*: every domain constraint problem is an instance of a CSP, and the universal CSP framework (with its branching, propagation, and inference algorithms) gives a uniform treatment. The constraint-satisfaction perspective is what makes problems with many interacting constraints tractable in industrial applications — vehicle routing, scheduling, configuration, automated reasoning. The competition-mathematics version is the same idea at the elementary level: read the constraints carefully, propagate them as far as possible before resorting to brute search, and use the constraint structure to prune.

### 2.2 Physical and Cross-Domain Foundations

The reach of domain constraints extends across the quantitative sciences.

In *physics*, almost every quantity is constrained by some positivity or boundedness condition. Masses, energies, temperatures (in absolute scale), probabilities, densities, distances, lengths of intervals — all are non-negative. Some are strictly positive (a temperature of $0\,\text{K}$ is unattainable in finite time, by the third law of thermodynamics). Others are bounded above as well as below: probabilities are in $[0, 1]$; angles are in $[0, 2\pi)$ modulo identification; speeds are bounded by $c$. A *candidate solution* to a physical equation that returns a negative mass or a superluminal velocity is *not a solution*; it is a sign that the model has been applied outside its domain of validity, or that an unphysical branch of a multi-valued function has been selected. The dimensional-analysis discipline of Chapter 7 is the *labour-saving* version of this insight; the domain-constraint discipline of the present chapter is the *correctness-guaranteeing* version.

In *economics*, domain constraints are pervasive and consequential. Prices are typically non-negative; quantities demanded and supplied are non-negative; the *no-arbitrage* constraint in finance is a strict inequality (no risk-free profit) that filters the set of admissible asset prices to those consistent with market equilibrium. A model that produces a *negative* equilibrium price is announcing that the model has misspecified the supply or demand schedule. A model that produces a *positive but implausibly large* equilibrium price (say, the price of a litre of milk computed as $10^6$ rupees) is announcing that the model's parameters are mis-estimated. The *domain envelope* of plausible-economic-quantities is what allows the analyst to detect the failure modes.

In *engineering*, the domain envelope is given by *specifications*: the operating range of a transistor (current, voltage, temperature), the load envelope of a structural beam, the bandwidth and dynamic range of a sensor. A design that requires the device to operate *outside* its specification is a design error, not a viable engineering solution. Every engineering analysis is preceded by a domain check — *is the proposed solution within the device's operating envelope?* — and the failure to perform the check is the failure mode behind a long history of catastrophic engineering failures (the Tacoma Narrows bridge, the Challenger O-rings, the Therac-25 radiation overdose).

In *medicine and pharmacology*, the domain envelope is the *therapeutic window*: the range of doses, frequencies, and timings within which a drug is both effective and safe. The pharmacist of the opening vignette is performing a multi-axis domain check at every prescription; the entire field of *clinical pharmacology* is the science of mapping these envelopes for each drug. *Dose-response curves* are the empirical determination of the lower edge of effectiveness; *toxicology* is the empirical determination of the upper edge of safety; the *therapeutic index* is the ratio between them. A drug with a wide therapeutic index (high index value) is forgiving — small errors in dosing have small consequences. A drug with a narrow therapeutic index (low index value) is unforgiving — the domain check must be performed exactly. The pharmacist's discipline in the opening vignette is the difference between safe practice and harm.

In *computer science*, *type checking* is the universal domain-constraint discipline. A program that attempts to add a string to an integer is rejected by a strongly-typed language *before* it runs; the type system is a domain check that catches a class of errors at compile time. *Refinement types* extend the discipline: a type like *"integer between 1 and 100"* allows the type checker to reject any program that would violate the constraint. *Contract programming* (Eiffel, Ada, modern C++ concepts) is the same discipline applied to function preconditions and postconditions. The entire safety story of modern programming languages is, structurally, a story of treating domain constraints as first-class citizens of the language.

### 2.3 Cognitive Foundations

The cognitive payoff of domain constraints is twofold.

The first is *error-reduction*. A student who applies the candidate-then-filter discipline on every problem catches a class of errors — extraneous roots, out-of-range solutions, non-geometric configurations, integer-violating values — that algebra alone cannot catch. The pattern is the *checklist culture* of medicine and aviation: a list of items to verify before the procedure is complete, the omission of any one of which is the most common source of failure. In JEE problems specifically, the candidate-then-filter discipline catches the single most common source of lost marks: *correct algebra, wrong answer because the wrong root was selected*.

The second payoff is *problem-tractability*. Many problems are *only* tractable because the domain reduces the candidate set to a manageable size. WE2 is a clean example: the candidate equation $\binom{n}{2} = 21$ has the candidate set $n = 7$ or $n = -6$; the integer-positive domain forces $n = 7$. PP4 is a starker example: the quartic has at most four real roots; the discriminant condition $a \ge 3/4$ is *what makes the problem about $a$ have a non-trivial answer at all*. The domain is not merely a filter; it is the structure that converts an open-ended problem into a closed-form one.

The deeper observation is that *a well-posed problem is one whose domain is sufficient to determine a unique answer*. The art of problem-design (the subject of Pillar 4) is the art of choosing equations and domains that pin down the intended answer without over- or under-constraining. From the solver's perspective, the *under-constrained* problem is the one with infinitely many candidates and an inadequate domain; the *over-constrained* problem is the one in which the algebra and the domain are inconsistent (no solution). The well-posed problem is the *Goldilocks* problem: candidates and domain together yield exactly one solution (or a small, enumerable set).

---

## 3. The Diagnostic Toolkit

### 3.1 The Three Questions Method (Domain-Constraint Edition)

Before any algebra, the trained solver asks three questions of the problem.

1. **What is the domain?** Read the problem statement and write down, *explicitly and separately*, the set of admissible values. Look for: *real / positive / integer / rational*, *interval restrictions* ($x \in [0, 2\pi]$), *geometric existence* (triangle, polygon, convex region), *function-definition restrictions* ($x > 0$ inside a log, $x \ne 0$ inside a reciprocal, $|x| \le 1$ inside an arcsin/arccos), and *implicit constraints* (probabilities in $[0, 1]$, divisors of a given number, divisors that share a factor with a parameter). Write the domain down *before* writing the equation.

2. **What candidate set does the algebra produce?** Solve the algebraic equation in the *largest* natural space (often $\mathbb{C}$ or $\mathbb{R}$ depending on the context), without yet imposing the domain. The candidate set is the set of points satisfying the equation; it may be finite, infinite, or empty. Compute it cleanly.

3. **What is the intersection?** Filter the candidate set by the domain, point by point. The intersection is the solution set. Report it. If the intersection is empty, report *no solution* with confidence; if it is a single point, report it; if it is finite, list all elements; if it is infinite, describe it parametrically.

The three questions can be answered in seconds. They are the discipline that converts *good algebra* into *correct answers*.

### 3.2 Forms of Domain Constraints: A Comprehensive Guide

We collect the four characteristic forms encountered in the chapter, with one-line diagnostics.

- **Form I — Function-domain constraints (analytic).** *Diagnostic:* the problem involves analytic expressions whose natural domain is restricted ($\log$, $\sqrt{}$, division, inverse trig, etc.). *Move:* compute the natural domain of each sub-expression; intersect; use the intersection as the implicit domain for any subsequent algebra. *Examples.* WE1 ($D_{f_1 + f_2} = D_{f_1} \cap D_{f_2}$), PP3 (intersection of two log-domain restrictions).

- **Form II — Number-theoretic constraints.** *Diagnostic:* variables are restricted to integers, positive integers, rationals, divisors of some number, or congruence-class subsets. *Move:* solve algebraically over the reals first; then enforce integrality (or rationality) by examining the algebraic form. Often reduces to a *divisor count* (how many integers divide $5$? Answer: four — $\pm 1, \pm 5$) or a *congruence check* (does $42 / 2$ give an integer? yes). *Examples.* WE2 (positive-integer $n$ from quadratic), PP1 (integer $m$-count), PP2 (consecutive-integer triangle).

- **Form III — Geometric existence (non-degeneracy).** *Diagnostic:* the variables purport to describe a triangle, polygon, conic, or other geometric configuration; the configuration must actually exist. *Move:* apply the triangle inequality $|a - b| < c < a + b$, the convexity condition, the discriminant of a conic, etc.; verify that the candidate parameters yield a non-degenerate object. *Examples.* WE3 (triangle inequality on $|x - y|$, etc.), PP2 (existence of triangle from consecutive integers), PP6 (Euler's $R \ge 2r$ bounds the $r/R$ ratio for non-degenerate triangles).

- **Form IV — Reality / discriminant constraints.** *Diagnostic:* the problem requires *real* roots or *real-valued* solutions, but the algebra would otherwise admit complex candidates. *Move:* compute the discriminant (for quadratics) or the more general discriminant condition (for cubics, quartics, via Sturm sequences or the resolvent cubic); set $\ge 0$ for all-real, $> 0$ for distinct-real, $= 0$ for double roots. *Examples.* PP4 (quartic factored into two quadratics; both discriminants $\ge 0$ forces $a \ge 3/4$), PP5 (range of $\sin(\cos x)$ restricts $x$ to $[-\sin 1, \sin 1]$).

### 3.3 Common Pitfalls

Five errors recur often enough to deserve named warnings.

- **The Forgotten Domain.** Solving the algebra without writing down the domain at the outset, and reporting the candidate set as the answer. The student who computes $x = -3$ as the answer to "find the number of pencils" without checking that the number must be a positive integer is committing this sin. The remedy is the discipline of §3.1 question 1: *write the domain in the margin before writing the equation*.

- **The Extraneous Root.** Producing a candidate solution by an algebraic manipulation that is *not reversible* on the original equation. The most common case is squaring both sides of an equation: $\sqrt{x + 2} = x \Rightarrow x + 2 = x^2 \Rightarrow x = 2$ or $x = -1$, but $x = -1$ does not satisfy the original equation (since $\sqrt{1}$ is $+1$, not $-1$). The remedy is to *check each candidate back in the original equation* — every candidate generated by squaring, by clearing denominators, by multiplying through by a factor that may be zero, must be explicitly verified.

- **The Union-Confusion.** Believing that the domain of a *combination* of functions is the *union* of the individual domains, when in fact it is the *intersection*. The domain of $\log x + \sqrt{x - 1}$ is *not* "$x > 0$ or $x \ge 1$" (which would be $x > 0$, since the second is contained in the first); it is *"$x > 0$ AND $x \ge 1$"*, which simplifies to $x \ge 1$. WE1 makes this point at the formal level.

- **The Boundary Confusion.** Confusing $<$ with $\le$ at the domain boundary, with answers off by one (in counting problems) or by a single boundary point (in interval problems). A triangle's sides must satisfy $|a - b| < c$ (strict) for non-degeneracy; $|a - b| = c$ gives a *degenerate triangle* (a line segment). A log requires $x > 0$ (strict); $x = 0$ gives $\log 0 = -\infty$, not a value. A square root allows $x \ge 0$; $x = 0$ gives $\sqrt{0} = 0$. The remedy is to *write each constraint with the correct inequality sign* — strict or non-strict — at the moment of stating the domain.

- **The Sign-Convention Error.** In geometric or trigonometric problems with multiple possible configurations (same side vs opposite side, acute vs obtuse, clockwise vs counter-clockwise), reporting a formula that is correct for one configuration but wrong for another. PP7 is an instance: the formula $h = d\sin\alpha\sin\beta/\sin(\alpha - \beta)$ applies to the *same-side* configuration, while $h = d\sin\alpha\sin\beta/\sin(\alpha + \beta)$ applies to the *opposite-side* configuration. The remedy is to *consider all geometric configurations consistent with the problem's wording*, and either report all branches or specify the convention used.

---

## 4. Worked Examples

We work three problems in detail, each in the six-point format. The first illustrates Form I (function-domain) at the JEE Mains level; the second, Form II (number-theoretic) at the JEE Advanced level; the third, Form III (geometric non-degeneracy) at the RMO Olympiad level.

### 4.1 Example 1 — The Domain of a Combined Function

**Problem.** *Prove or disprove the following claim. If $f_1$ is a function defined on the domain $D_1$ and $f_2$ is a function defined on the domain $D_2$, then $f_1 + f_2$ is a function defined on the domain $D_1 \cup D_2$.* (JEE 1988; Joshi *EJM* Ch. 24, Exercise 24.1.)

**SEED.** *Domain constraint (Form I — function-domain analysis).* The combined operation $f_1 + f_2$ is meaningful at a point $x$ only if *both* $f_1(x)$ and $f_2(x)$ are defined; the natural domain of the sum is therefore the *intersection*, never the union, of the individual domains.

**BRUTE PATH.** A student who has been doing only routine function-evaluation problems might *believe* the claim and try to prove it — only to fail at constructing a proof, since the claim is false. A more careful student tries a few examples: take $f_1(x) = 1/x$ on $D_1 = \mathbb{R} \setminus \{0\}$ and $f_2(x) = 1/(x-1)$ on $D_2 = \mathbb{R} \setminus \{1\}$. What is the domain of $(f_1 + f_2)(x) = 1/x + 1/(x-1)$? The expression $1/x + 1/(x-1)$ is undefined at $x = 0$ (the first summand) and at $x = 1$ (the second summand); it is *defined everywhere else*. So the domain of $f_1 + f_2$ is $\mathbb{R} \setminus \{0, 1\}$. Now, $D_1 \cup D_2 = (\mathbb{R} \setminus \{0\}) \cup (\mathbb{R} \setminus \{1\}) = \mathbb{R}$ (since every point is in at least one of $D_1, D_2$). The claim therefore asserts that $f_1 + f_2$ is defined on all of $\mathbb{R}$ — but it is not, since $f_1 + f_2$ is undefined at both $0$ and $1$. The claim is *false*, and the example provides the disproof. The brute path *works*, but it works by accident — it stumbles into the disproof rather than seeing the structural reason.

**ELEGANT PIVOT.** We argue *structurally*. For $f_1 + f_2$ to be defined at a point $x$, *both* $f_1(x)$ and $f_2(x)$ must be defined — the sum of two numbers requires both numbers to exist. Therefore the domain of $f_1 + f_2$ is precisely
\[
  D_{f_1 + f_2} \;=\; \{ x : f_1(x) \text{ is defined and } f_2(x) \text{ is defined}\} \;=\; D_{f_1} \cap D_{f_2} \;=\; D_1 \cap D_2.
\]
The claim of the problem asserts that the domain is $D_1 \cup D_2$; this is *strictly larger* than $D_1 \cap D_2$ whenever $D_1 \ne D_2$ (i.e., whenever the two functions have different domains). The two sets coincide only when $D_1 = D_2$.

*Concrete disproof.* Take $f_1(x) = \log x$ with $D_1 = (0, \infty)$, $f_2(x) = \log(1 - x)$ with $D_2 = (-\infty, 1)$. Then $D_1 \cup D_2 = \mathbb{R}$, while $D_1 \cap D_2 = (0, 1)$. The sum $f_1(x) + f_2(x) = \log x + \log(1 - x) = \log(x(1 - x))$ is defined precisely when $x(1 - x) > 0$, i.e., when $0 < x < 1$ — matching $D_1 \cap D_2$, not $D_1 \cup D_2$. The claim is *disproved* by this example, and the correct general principle is that the domain of any *pointwise combination* of functions (sum, product, difference, quotient where the denominator is non-zero) is the *intersection* of the individual domains.

The elegant pivot is the recognition that the entire content of the problem is a *misunderstanding of where the operation "+" requires both arguments*. The structural fact — sum requires both arguments to be defined — gives the answer immediately, and the example simply concretises the disproof.

**PITFALLS.**

- *The Union-Confusion.* The whole point of the problem is to catch the student who would *believe* the false union-claim. The remedy is the structural reading: an operation requires all its operands; the domain of the combined expression is therefore the intersection of the operand-domains.

- *Conflating $f_1$ + $f_2$ with the "natural" extension.* Some textbooks extend $f_1 + f_2$ to a larger domain by *defining* it to equal $f_1$ on $D_1 \setminus D_2$ (where $f_2$ is undefined) and $f_2$ on $D_2 \setminus D_1$. This is a *redefinition*, not the usual sum, and it produces a function on $D_1 \cup D_2$ that disagrees with the usual sum on the *intersection* of the domains in a peculiar way. The remedy is to read "$f_1 + f_2$" with its ordinary meaning: pointwise addition, defined where both summands are defined.

- *Forgetting that the Domain Depends on More than the Algebraic Expression.* A function is *not* an algebraic expression; it is an algebraic expression *together with a domain*. Two functions with the same algebraic expression but different domains are different functions. The function $\log x$ on $(0, \infty)$ is *not* the same function as the (more general) complex $\log z$ on $\mathbb{C} \setminus \{0\}$. The pedagogical practice of separating the algebraic expression from the domain is part of the discipline.

- *Reporting "Defined Where the Algebra Works" Instead of $D_1 \cap D_2$.* The two are equivalent *when the algebra exactly captures the domain restrictions* (every sub-expression's natural domain is checked). In practice, students often forget a sub-expression and report a domain that is too generous. The remedy is to check *every* sub-expression individually.

- *Confusing "Domain" with "Range".* The *domain* of $f$ is the set of inputs $x$ on which $f(x)$ is defined; the *range* is the set of outputs $f(x)$ as $x$ varies over the domain. The two are independently constrained. PP5 will exploit a range bound; the current problem is about domains.

**CONNECTIONS.**

*Primary archetype applications.* The intersection-of-domains principle controls (a) every problem on the natural domain of a multi-piece analytic expression; (b) every problem on simultaneous solvability of multiple equations (the solution set is the intersection of the solution sets of the individual equations); (c) every problem on the consistency of multiple inequalities (the feasible region is the intersection of the half-planes / half-spaces defined by each inequality).

*Alternative solution archetypes.* The claim can also be disproved by *Counter-example construction* (Form-IV of Symmetry, Ch. 2) — find any specific $f_1, f_2$ for which the claim fails. The structural pivot is more general and more illuminating; the counter-example is faster.

*Cross-domain manifestations.* The intersection-of-domains principle is the foundation of *type-safety* in modern programming: the type of `a + b` is computed by *unifying* the types of `a` and `b`, and the unified type is defined only where both individual types are defined. *Constraint solvers* in operations research use the same principle: the feasible region of a constraint satisfaction problem is the intersection of all the individual constraint sets. *Database joins* are the same idea: the join of two relations contains records that satisfy *both* relations' conditions.

**TAKEAWAY.** *A combined operation requires all its operands — the domain is the intersection, never the union.*

---

### 4.2 Example 2 — Triangle Count Among Vertices of a Regular Polygon

**Problem.** *Let $T_n$ denote the number of triangles whose vertices are chosen from the vertices of a regular polygon with $n$ sides. If $T_{n+1} - T_n = 21$, find $n$.* (JEE 2001; Joshi *EJM* Ch. 24, Exercise 24.20.)

**SEED.** *Domain constraint (Form II — number-theoretic).* The algebra produces a quadratic in $n$ with two roots; the domain (positive integer) filters to a single value. The selection is the entire content of the problem.

**BRUTE PATH.** A student who does not know the formula for $T_n$ might try to enumerate. For $n = 3$: $T_3 = 1$. For $n = 4$: $T_4 = 4$. For $n = 5$: $T_5 = 10$. For $n = 6$: $T_6 = 20$. For $n = 7$: $T_7 = 35$. For $n = 8$: $T_8 = 56$. The differences are: $T_4 - T_3 = 3$, $T_5 - T_4 = 6$, $T_6 - T_5 = 10$, $T_7 - T_6 = 15$, $T_8 - T_7 = 21$. *We found $n + 1 = 8$, so $n = 7$.* The brute path works, but only because the numbers are small. For a problem with $T_{n+1} - T_n = 4950$, this strategy would require enumerating up to $n = 99$, which is impractical.

**ELEGANT PIVOT.** Recognise that *any three distinct vertices of a regular $n$-gon form a triangle* (the regularity is irrelevant; vertices are in general position in the sense that no three are collinear). Therefore $T_n = \binom{n}{3}$ — the number of ways to choose three vertices from $n$. The difference is
\[
  T_{n+1} - T_n \;=\; \binom{n+1}{3} - \binom{n}{3} \;=\; \binom{n}{2},
\]
by Pascal's identity $\binom{n+1}{k} = \binom{n}{k} + \binom{n}{k-1}$. Setting $T_{n+1} - T_n = 21$:
\[
  \binom{n}{2} \;=\; \frac{n(n-1)}{2} \;=\; 21 \quad\Longleftrightarrow\quad n(n-1) \;=\; 42 \quad\Longleftrightarrow\quad n^2 - n - 42 \;=\; 0.
\]
The quadratic factors as $(n - 7)(n + 6) = 0$, giving candidates $n = 7$ and $n = -6$.

*Domain filter.* The problem specifies that $n$ is the number of sides of a polygon; thus $n \in \mathbb{Z}_{\ge 3}$ (a polygon needs at least three sides). The candidate $n = -6$ is filtered out by the domain. The remaining candidate is
\[
  \boxed{n \;=\; 7.}
\]

The elegant pivot took three short steps: recognise the formula for $T_n$, apply Pascal's identity to get the difference, solve the quadratic and filter by the domain. The combinatorial identity does the algebraic work; the domain filter does the selection work.

**PITFALLS.**

- *Forgetting Pascal's Identity.* The student who does not know $\binom{n+1}{k} = \binom{n}{k} + \binom{n}{k-1}$ may compute $\binom{n+1}{3} - \binom{n}{3}$ directly by writing out the factorials and simplifying. This works but takes longer and is more error-prone. The identity is gem-level (Pillar 5); the trained solver knows it.

- *Reporting Both Roots of the Quadratic.* The unconditional answer to $n^2 - n - 42 = 0$ is $n \in \{7, -6\}$. The conditional answer (after domain filtering) is $n = 7$. A student who reports "$n = 7$ or $n = -6$" loses marks on the JEE MCQ that has only $n = 7$ as a choice.

- *Forgetting to Verify $n \ge 3$.* Even for a positive integer answer, the polygon-domain requires $n \ge 3$. If the equation had given $n = 2$ as a candidate, the answer would still be filtered out (a "polygon with 2 sides" is degenerate). Always verify the full domain.

- *Confusing $T_n$ with "Number of Triangles in a Different Sense".* The problem says *triangles whose vertices are chosen from the polygon's vertices*. It does *not* say "triangles inscribed in the polygon with non-overlapping sides," or "triangles fitting inside the polygon," or any other geometric subtlety. The straight reading is *combinatorial*: $\binom{n}{3}$. Other readings would give different formulas and different answers.

- *Mis-applying Pascal's Identity Sign.* Pascal's identity has a *plus* sign: $\binom{n+1}{k} = \binom{n}{k} + \binom{n}{k-1}$. A student who mis-recalls it as a difference may compute $T_{n+1} - T_n$ wrongly. The remedy is to derive the identity from the definition rather than from memory: $\binom{n+1}{k}$ counts subsets of size $k$ from $\{1, \ldots, n+1\}$; those subsets either include $n+1$ (and contribute $\binom{n}{k-1}$) or do not (and contribute $\binom{n}{k}$).

**CONNECTIONS.**

*Primary archetype applications.* The combinatorial identity $\binom{n+1}{k} - \binom{n}{k} = \binom{n}{k-1}$ controls every problem involving *differences of consecutive binomial coefficients*. The integer-positive domain filter is universal in counting problems — every count is a non-negative integer, and a candidate that fails this test is rejected. The pattern *quadratic candidates filtered by integer-positivity* is one of the most common in JEE algebra: it appears in problems on arithmetic progressions ("how many terms?"), geometric series, combinatorial identities, sequences with integer constraints.

*Alternative solution archetypes.* The same problem can be solved by *Hidden Structure* (Ch. 4): recognise that $T_n$ is generated by a generating function $\sum_n \binom{n}{3} x^n = x^3 / (1 - x)^4$, and the difference $T_{n+1} - T_n$ is the coefficient extraction from a shifted generating function. The combinatorial approach is faster on this problem; the generating-function approach generalises to more complex difference patterns.

*Cross-domain manifestations.* The "candidate-quadratic, filter-by-integrality" pattern appears in *combinatorial chemistry* (counting isomers of a hydrocarbon with $n$ carbons), in *graph theory* (counting graphs with $n$ vertices and certain properties), in *coding theory* (counting codewords of a certain weight), in *combinatorial design* (counting balanced incomplete block designs). In every case, the algebra produces a continuous expression and the integer domain filters to the relevant cases.

**TAKEAWAY.** *Recognise the combinatorial structure first; the algebra is then routine, and the integer domain selects the unique answer.*

---

### 4.3 Example 3 — Triangle-Inequality–Forced Bound

**Problem.** *Let $x, y, z$ be the lengths of the sides of a triangle. Prove that*
\[
  |x^2 (y - z) + y^2 (z - x) + z^2 (x - y)| \;<\; xyz.
\]
*(Regional Mathematics Olympiad; Joshi EJM Ch. 24, Exercise 24.65.)*

**SEED.** *Domain constraint (Form III — triangle-inequality non-degeneracy).* The algebra produces a symmetric expression on the left; the algebraic identity factorises it into a triple product; the triangle-inequality bound on each factor produces the result.

**BRUTE PATH.** A student who does not know the factorisation of the symmetric expression might try to expand and bound term-by-term. The expression $x^2(y - z) + y^2(z - x) + z^2(x - y)$ expands to
\[
  x^2 y - x^2 z + y^2 z - y^2 x + z^2 x - z^2 y,
\]
which has six terms with mixed signs. Bounding each term individually (e.g., $|x^2 y| \le x^2 y$, but the signs are not all positive) and combining gives a coarse bound much weaker than $xyz$ — usually around $3 xyz$ or worse. The brute path *works for an upper bound* but does not produce the sharp bound $xyz$, and so does not solve the problem as stated.

**ELEGANT PIVOT.** *Factorise* the LHS first; then *use the triangle inequality* on each factor.

*Step 1 — Algebraic identity.* The symmetric expression factorises as
\[
  x^2 (y - z) + y^2 (z - x) + z^2 (x - y) \;=\; (x - y)(y - z)(x - z).
\]
*Proof.* Group the terms in pairs and factor:
\begin{align*}
  x^2(y - z) + y^2(z - x) + z^2(x - y)
  &= x^2 y - x^2 z + y^2 z - y^2 x + z^2 x - z^2 y \\
  &= xy(x - y) - z(x^2 - y^2) + z^2(x - y) \\
  &= xy(x - y) - z(x - y)(x + y) + z^2(x - y) \\
  &= (x - y)\big[ xy - z(x + y) + z^2 \big] \\
  &= (x - y)\big[ x(y - z) - z(y - z) \big] \\
  &= (x - y)(y - z)(x - z).
\end{align*}

*Step 2 — Triangle inequality on each factor.* The condition that $x, y, z$ are the sides of a (non-degenerate) triangle is the three strict inequalities
\[
  |x - y| \;<\; z, \qquad |y - z| \;<\; x, \qquad |x - z| \;<\; y.
\]
(*Proof of $|x - y| < z$.* By the standard triangle inequality, $x < y + z$ and $y < x + z$, giving $x - y < z$ and $y - x < z$, hence $|x - y| < z$. The other two inequalities are symmetric.)

*Step 3 — Combine.* Taking absolute values of the factorisation and using the triangle bounds,
\[
  |x^2(y - z) + y^2(z - x) + z^2(x - y)| \;=\; |x - y| \cdot |y - z| \cdot |x - z| \;<\; z \cdot x \cdot y \;=\; xyz.
\]

The bound is strict because each of the three triangle inequalities is strict for a non-degenerate triangle. \hfill$\blacksquare$

The elegant pivot has two ingredients: the *algebraic identity* (which turns the six-term symmetric expression into a clean triple product) and the *domain constraint* (the triangle inequality, which bounds each factor by a side length). Neither ingredient alone suffices: without the identity, the LHS is not amenable to factor-by-factor bounding; without the triangle inequality, the factors are not bounded by anything specific.

**PITFALLS.**

- *Trying to Bound Term-by-Term.* Term-by-term bounding produces $|x^2 y| + |x^2 z| + |y^2 z| + |y^2 x| + |z^2 x| + |z^2 y|$, which equals $x^2 y + x^2 z + y^2 z + y^2 x + z^2 x + z^2 y$ — much larger than $xyz$ (typically by a factor of $3$ or more for a roughly equilateral triangle). The triangle inequality is too weak to recover the sharp bound from the unfactored form.

- *Forgetting the Strict-Inequality Version of the Triangle Inequality.* The standard triangle inequality $x < y + z$ (and cyclic) gives $|x - y| < z$ (strict); the *degenerate* triangle inequality $x \le y + z$ gives only $|x - y| \le z$. For a non-degenerate triangle (which is what "the sides of a triangle" means), the strict version applies, and the conclusion $|x - y| \cdot |y - z| \cdot |x - z| < xyz$ is strict. A student who uses the non-strict version reports $\le$ instead of $<$ and loses precision.

- *Not Recognising the Symmetric-Factorisation Identity.* The identity $x^2(y-z) + y^2(z-x) + z^2(x-y) = (x-y)(y-z)(x-z)$ is a *gem* (Pillar 5) — a frequently-recurring algebraic identity that the trained solver should recognise at sight. Without it, the problem cannot be solved cleanly. The remedy is to internalise the identity as part of the standard kit of symmetric polynomial factorisations (alongside Newton's identities, Vieta's relations, and the symmetric-power expansions).

- *Multiplying Inequalities of the Wrong Sign.* For inequalities to multiply cleanly, all factors must be *non-negative* (or all non-positive, with appropriate sign-tracking). Here we take absolute values *first*, then multiply non-negative inequalities — a clean operation. A student who multiplies *signed* differences directly may produce sign errors and reach a wrong inequality.

- *Forgetting the Closure-of-Inequalities Under Multiplication.* The product of three strict inequalities $a < a'$, $b < b'$, $c < c'$ (all factors positive) gives the strict $abc < a'b'c'$. The remedy is to verify that all factors are strictly positive before applying the closure (here, the factors $|x - y|, |y - z|, |x - z|$ are strictly positive iff $x, y, z$ are pairwise distinct — and the strict bound holds even when some factors are zero, since both sides are then zero or smaller).

**CONNECTIONS.**

*Primary archetype applications.* The triangle-inequality bound is the universal Form-III filter for problems involving triangles. Variants include: *bounding a symmetric expression by some side product*; *forcing a triangle's altitudes, medians, or angle bisectors to satisfy specific relations*; *proving existence or non-existence of a triangle with given parameters*. The factorisation $x^2(y-z) + y^2(z-x) + z^2(x-y) = (x-y)(y-z)(x-z)$ is the prototype of *symmetric polynomial identities for three variables*; many other identities (e.g., Vandermonde's, Schur's, Newton-Girard) follow the same pattern of *symmetric expression $\to$ factorisation into differences*.

*Alternative solution archetypes.* The bound can also be obtained by *Substitution* (Ch. 5) via the *Ravi substitution* $x = u + v, y = v + w, z = w + u$ for positive $u, v, w$ (which we deployed in Ch. 5 WE2). Under Ravi, $x - y = u - w$, $y - z = v - u$, $x - z = v - w$, and the triangle inequality becomes the *automatic positivity* of $u, v, w$. The Ravi substitution is the elegant pivot for many triangle-inequality problems; here it requires more algebra than the factorisation route.

*Cross-domain manifestations.* The pattern *algebraic identity + domain constraint $\to$ tight bound* appears in *information theory* (the Cauchy-Schwarz bound on mutual information; Fano's inequality), in *quantum mechanics* (the Robertson-Schrödinger uncertainty relation), in *statistics* (the Chebyshev inequality, the Cramér-Rao bound). In every case, an algebraic identity (often a positivity-of-a-square argument) is combined with a domain constraint to produce a bound that is sharp because both ingredients are sharp.

**TAKEAWAY.** *Factorise first; the domain constraint then bounds each factor — and the product is the answer.*

---

## 5. Practice Problems

Seven problems, statements only; full solutions appear in the Appendix. The slate spans Tier 1 (JEE Mains) through Tier 4 (RMO Olympiad).

### 5.1 Integer-$m$ Count for Integer Intersection (JEE 2001; Joshi Ch. 24, Exercise 24.30)

Find the number of integer values of $m$ for which the $x$-coordinate of the point of intersection of the lines $3x + 4y = 9$ and $y = mx + 1$ is itself an integer.

### 5.2 Triangle with Consecutive-Integer Sides and Inradius $4$ (RMO; Joshi Ch. 24, Exercise 24.72)

The sides of a triangle are three consecutive positive integers, and its inradius is $4$ units. Determine its circumradius.

### 5.3 Log-Domain Restriction (JEE 2001; Joshi Ch. 24, Exercise 24.45 — domain half)

Find the natural domain of the function
\[
  f(x) \;=\; \log_4 (x - 1) \;-\; \log_2 (x - 3).
\]

### 5.4 Real-Root Condition on a Quartic (RMO; Joshi Ch. 24, Exercise 24.68)

Find all real values of $a$ such that the equation
\[
  x^4 - 2 a x^2 + x + a^2 - a \;=\; 0
\]
has all four roots real.

### 5.5 Trig-Range Restricts Real Roots (Joshi Ch. 10, Comment 6)

Find the number of real solutions $x \in [-\pi, \pi]$ of the equation
\[
  \sin(\cos x) \;=\; x.
\]

### 5.6 Euler's Inradius-Circumradius Bound (Joshi Ch. 11, Comment 9)

For *every* triangle (not just acute), prove that the inradius $r$ and the circumradius $R$ satisfy $R \ge 2r$, with equality if and only if the triangle is equilateral. State the equality case explicitly.

### 5.7 Tower Height from Two Angles of Elevation (JEE 1988; Joshi Ch. 12, Comment 3)

A vertical tower stands at a point $O$ on level ground. The angle of elevation of the top of the tower from a point $P$ on the ground is $\alpha$. From a second point $Q$, at distance $d$ from $P$ along the same horizontal line through $O$, the angle of elevation is $\beta$ (with $0 < \beta < \alpha < \pi/2$). Express the height $h$ of the tower in terms of $d, \alpha, \beta$. Distinguish the two cases (a) $P$ and $Q$ on the *same* side of $O$, and (b) $O$ *between* $P$ and $Q$.

---

## 6. The Connections Web

Domain constraints connect to virtually every later archetype in the book and to almost every quantitative discipline.

### 6.1 Domain Constraints Across Mathematical Domains

*Algebra.* The natural domain of every algebraic expression is the union of restrictions: denominators must be non-zero, even roots require non-negative radicands, logarithms require positive arguments, inverse trig functions require restricted ranges. Every algebraic equation is implicitly *defined on its natural domain*; the solution set is the intersection of the candidate set with the domain. This intersection-then-solve pattern is the foundation of every algebra textbook's *"check for extraneous roots"* instruction.

*Geometry.* Every geometric configuration is *constrained to exist*: triangles by the triangle inequality, polygons by their angle sum, conics by the discriminant of the defining quadratic. The Euler inequality $R \ge 2r$ for triangles is a non-trivial constraint on the *combination* of inradius and circumradius — a bound that pins down which $(r, R)$ pairs correspond to actual triangles. PP6 develops this.

*Number theory.* Integrality is the universal domain constraint in number theory: the algebra runs over $\mathbb{Q}$ or $\mathbb{R}$, but the *number-theoretic content* is the intersection with $\mathbb{Z}$. The fundamental theorem of arithmetic, Fermat's little theorem, the Chinese remainder theorem, and the entire apparatus of diophantine equations are statements about integer-constrained solutions of algebraic equations. PP1 and WE2 are JEE-level instances of the same discipline.

*Analysis.* The *radius of convergence* of a power series is the implicit domain constraint for convergence; convergence outside the disc is meaningless. The *domain of differentiability* of a function may be strictly smaller than the domain on which the function is defined; the *domain of continuity* may be smaller still. Every theorem in real and complex analysis carries an implicit "for $x$ in this domain" qualifier; misapplying the theorem outside its domain produces the standard failure modes (divergent series treated as convergent, non-differentiable functions treated as differentiable).

*Probability theory.* A probability measure must satisfy $\mu(\Omega) = 1$ (normalisation, Ch. 7 connection) and $\mu(A) \ge 0$ for every event $A$ (positivity — a domain constraint). A function on a measurable space is a probability density iff it is non-negative and integrates to $1$; both conditions are domain constraints. Bayes' theorem is, structurally, a domain-constraint check: $P(A | B)$ is defined only on $B$ — the conditional restricts the domain.

### 6.2 Domain Constraints in Physics and Other Sciences

*Classical mechanics.* Energy is non-negative (in absolute scale, modulo a choice of zero point). Mass is strictly positive. Time intervals are non-negative. A computed solution to an equation of motion that produces negative kinetic energy or negative mass is announcing that the problem has been set up incorrectly or the wrong branch of a multi-valued square root has been selected. The discipline of checking each physical quantity for positivity is built into the standard physics curriculum.

*Quantum mechanics.* Probabilities (the squared moduli of wave-function amplitudes) must lie in $[0, 1]$; total probability must be $1$ (normalisation, again). Energy eigenvalues for a system in a confining potential are real (the Hamiltonian is Hermitian); a computed eigenvalue with non-zero imaginary part is announcing a numerical or conceptual error. The exclusion principle is a domain constraint: identical fermions cannot occupy the same quantum state, so candidate wave functions that violate antisymmetry are filtered out.

*Statistical mechanics.* Temperatures (in absolute scale) are non-negative. Partition functions are positive (they are sums of positive Boltzmann weights). Entropies are non-negative for any well-defined macrostate. The *third law* (entropy approaches a constant as $T \to 0$) is a domain-bound on entropy at the absolute zero.

*Engineering.* Every design quantity has *specification limits* — minimum, maximum, allowed range. Voltages, currents, temperatures, pressures, stresses, deflections are all bounded by what the components can withstand. The *factor of safety* is the multiplicative margin between the design load and the failure load — a deliberate over-specification of the domain envelope. The catastrophic failures of engineering history are, almost without exception, *domain-envelope violations*: the device or structure was operated outside its specification.

*Medicine.* Doses, frequencies, and timings are constrained by the therapeutic window. Vital signs (heart rate, blood pressure, body temperature, oxygen saturation, respiratory rate) have normal ranges; values outside the ranges are the medical signals that initiate intervention. The opening vignette's pharmacist is the canonical example.

### 6.3 Cross-Domain Manifestations

The reach extends beyond physics.

*Economics.* Prices, quantities, and probabilities are non-negative; budget constraints define feasible-consumption regions; production functions have *isoquants* that bound the feasible-production region. Every optimisation in economics is *constrained* — by budget, by technology, by regulation — and the constrained optimum is generally distinct from the unconstrained one. The *Lagrange-multiplier* technique (Pillar 5 / Ch. 12) is the systematic machinery for handling constrained optimisation, and it builds on the candidate-then-filter pattern of the present chapter.

*Computer science.* Type checking, contract programming, refinement types, dependent types — all are domain-constraint disciplines applied to program correctness. *Static analysis* tools verify domain constraints at compile time; *dynamic analysis* tools verify them at run time. *Formal verification* methods prove that no execution of a program can violate stated constraints. The entire safety story of modern software engineering is, structurally, the candidate-then-filter discipline made systematic.

*Law and policy.* Legal rules are domain constraints on permissible behaviour. *Constitutional law* defines the outermost domain (what is constitutionally permissible). *Statutory law* defines finer-grained restrictions. *Regulatory law* defines the operating-envelope for specific industries (banking, pharmaceuticals, telecommunications). *Case law* refines the interpretation of these constraints in specific factual settings. The *compliance* function in a corporation is, structurally, the candidate-then-filter discipline applied to business decisions.

*Music composition.* Tonal music operates inside a domain envelope: a *key*, with its scale, its set of allowed chords (functional harmony), its voice-leading constraints. *Counterpoint* species rules are explicit domain constraints (no parallel fifths, no voice-crossing, leap-then-step). A composition that violates these constraints (without justification) is heard as *wrong*; the listener has internalised the domain envelope. The same is true of every artistic genre — every genre defines an *envelope of allowable moves*, and competence within the genre is competence within the envelope.

### 6.4 Related Archetypes

Domain constraints interact with five other archetypes in particularly tight ways.

- **Archetype 1 (Invariance).** Chapter 1 §4.1 introduced the candidate-then-filter pattern as one of the four ways an invariant operates. The present chapter elevates the *filter* step to a named archetype. The reader who has internalised Ch. 1 should find Ch. 9 a natural extension; the reader who has internalised Ch. 9 should find Ch. 1 §4.1 a *prefiguring* of the present material.

- **Archetype 10 (Inequality Constraints).** Inequalities are the most common kind of domain constraint. Where Domain Constraints (Ch. 9) treats the *general filter* — anything that restricts the domain — Inequality Constraints (Ch. 10) treats the *specific case* in which the constraints are inequalities (AM-GM, Cauchy-Schwarz, Jensen, power-mean). The two chapters together cover the constraint-side of problem solving; Chapter 10 inherits the structural machinery developed here.

- **Archetype 11 (Existence / Uniqueness Conditions).** The most rigorous form of a domain constraint is an *existence* condition: does there exist a value satisfying the equation? The most rigorous form of an answer is *yes (with example)* or *no (with proof)*. Chapter 11 develops this; it will use Domain Constraints as a routine sub-technique.

- **Archetype 14 (Parity / Modularity).** Parity constraints — *the answer must be even, must be a multiple of $3$, must be $\equiv 1 \pmod 4$* — are the modular-arithmetic version of integrality constraints. Chapter 14 will use parity as a candidate-filter in number-theory problems. The pattern is structurally identical to the integer-divisor counting in WE2 and PP1 of the present chapter; the language is modular rather than divisor-based.

- **Archetype 17 (Degrees of Freedom Analysis).** Counting the number of free variables and subtracting the number of constraints gives the *effective degrees of freedom* of a problem. Chapter 17 will systematise this. The relation to the present chapter: each domain constraint is, structurally, a *constraint* in the DOF sense, and the dimension of the admissible set equals the number of variables minus the number of independent constraints (when the constraints are generic).

---

## 7. Master Takeaways

Seven sentences. Each one is a complete operational principle; each is meant to be quoted, internalised, and re-deployed.

1. *Algebra generates candidates; the domain selects the winner.* (The canonical takeaway.)

2. *A combined operation requires all its operands — the domain of $f_1 + f_2$ is $D_1 \cap D_2$, never $D_1 \cup D_2$.* (WE1 takeaway; Form I.)

3. *Solve over the reals first; then enforce integrality by examining the algebraic form.* (WE2 takeaway; Form II.)

4. *Factorise first; the domain constraint then bounds each factor.* (WE3 takeaway; Form III.)

5. *Every squaring (or cross-multiplication, or division by an expression) introduces an extraneous candidate — check each one back in the original equation.*

6. *A well-posed problem is one whose domain plus equations together determine a unique solution; the domain is half the problem.*

7. *Write the domain in the margin before writing the equation.*

---

## 8. Self-Assessment Checklist

You have absorbed Chapter 9 when, without re-opening it, you can do each of the following from memory.

- [ ] State the formal definition of a domain constraint as the intersection of admissibility conditions, and explain why the domain of a combined operation is the intersection, never the union.
- [ ] Identify, for any given analytic expression, the natural domain (intersection of sub-expression domains: logs $> 0$, square roots $\ge 0$, denominators $\ne 0$, $\arcsin$/$\arccos$ in $[-1, 1]$).
- [ ] State the triangle inequality in both the standard ($x + y > z$) and the equivalent symmetric-difference ($|x - y| < z$) forms.
- [ ] State Heron's formula $K = \sqrt{s(s-a)(s-b)(s-c)}$ and the inradius / circumradius formulas $r = K/s$, $R = abc / (4K)$.
- [ ] State Euler's inequality $R \ge 2r$ for every triangle and prove it from $OI^2 = R(R - 2r) \ge 0$ where $O, I$ are the circumcentre and incentre.
- [ ] State the symmetric-polynomial identity $x^2(y - z) + y^2(z - x) + z^2(x - y) = (x - y)(y - z)(x - z)$ and derive it by pair-grouping and factoring.
- [ ] State Pascal's identity $\binom{n+1}{k} = \binom{n}{k} + \binom{n}{k-1}$ and derive it combinatorially (subsets including vs not including a chosen element).
- [ ] For a given quadratic / quartic / polynomial equation, state the discriminant condition for all-real roots, and apply it to filter the parameter values.
- [ ] Name and explain three of the five common pitfalls: the Forgotten Domain, the Extraneous Root, the Union-Confusion, the Boundary Confusion, the Sign-Convention Error.
- [ ] Articulate, in one sentence, how Domain Constraints (Ch. 9) relates to Inequality Constraints (Ch. 10) — Chapter 10 specialises Ch. 9 to the case where the constraints are inequalities, importing AM-GM, Cauchy-Schwarz, Jensen.

---

## Bridge to Chapter 10: Inequality Constraints

Chapter 9 opened the *Constraint Exploitation* sub-pillar by elevating the *filter step* of the candidate-then-filter pattern to a named archetype. The four forms (function-domain, number-theoretic, geometric non-degeneracy, reality/discriminant) cover essentially every JEE / RMO instance of explicit domain filtering, and the discipline of *writing the domain in the margin before the equation* will accompany every later chapter of the book.

Chapter 10 — *Inequality Constraints* — takes the *most common kind of filter* and elevates it to its own archetype. Where Domain Constraints treats any restriction on the admissible set, Inequality Constraints treats the special case in which the restriction is given by an inequality. This special case is dominant in competition mathematics: every inequality-proof problem (AM-GM, Cauchy-Schwarz, Jensen, power-mean, Chebyshev's sum, rearrangement, Schur) is, structurally, an *inequality constraint* problem in which the algebra produces a candidate quantity and the inequality bounds it. The cross-archetype reuse of the JEE 2001 cos-product problem (Ch. 7 WE3 reappears as Ch. 10 PP3) and of the RMO triangle-inequality bound (Ch. 9 WE3 reappears as Ch. 10 WE1) is the deliberate illustration of how *one concrete problem* may be framed under either archetype depending on which structural feature is being studied.

With Chapter 10 in hand, the reader will have seen the two foundational *constraint* archetypes — domain filtering and inequality bounding — and will be positioned for Chapters 11 (Existence / Uniqueness Conditions) and 12 (Extremal Principles), which complete the *Constraint Exploitation* sub-pillar.

---

## Appendix — Solutions to Practice Problems

### Solution to 5.1 — Integer-$m$ Count for Integer Intersection

*Setting up the intersection.* Substitute $y = mx + 1$ into $3x + 4y = 9$:
\[
  3x + 4(mx + 1) \;=\; 9 \quad\Longrightarrow\quad (3 + 4m) x \;=\; 5 \quad\Longrightarrow\quad x \;=\; \frac{5}{3 + 4m}.
\]
(The line $3x + 4y = 9$ and the line $y = mx + 1$ are distinct lines for every $m$; they intersect in a single point unless they are parallel. The slopes are $-3/4$ and $m$, so they are parallel iff $m = -3/4$, which is not an integer.)

*Domain filter — integer $x$.* The value $x = 5/(3 + 4m)$ is an integer if and only if $3 + 4m$ is a *divisor* of $5$. The divisors of $5$ are $\pm 1$ and $\pm 5$, giving four cases:
\begin{align*}
  3 + 4m &= 1 &&\Longrightarrow m = -1/2 &&\text{(not an integer; reject)} \\
  3 + 4m &= -1 &&\Longrightarrow m = -1 &&\text{(integer; accept; gives } x = -5\text{)} \\
  3 + 4m &= 5 &&\Longrightarrow m = 1/2 &&\text{(not an integer; reject)} \\
  3 + 4m &= -5 &&\Longrightarrow m = -2 &&\text{(integer; accept; gives } x = -1\text{)}
\end{align*}

*Conclusion.* There are *exactly two integer values of $m$* that yield an integer $x$-coordinate: $m = -1$ (giving intersection $(-5, 6)$) and $m = -2$ (giving intersection $(-1, 3)$). The answer is $\boxed{2}$. \hfill$\blacksquare$

*Correction note.* The v0.2 locked slate listed the two valid values as "$m = -1$ and $m = 2$." The correct second value is $m = -2$ (verified: $3 + 4(-2) = -5$, so $x = 5/(-5) = -1 \in \mathbb{Z}$; whereas $3 + 4(2) = 11$, so $x = 5/11 \notin \mathbb{Z}$). The *count* of two is correct; only the second listed value was a copy-typo. Slate patched to v0.2.6.

---

### Solution to 5.2 — Triangle with Consecutive-Integer Sides and Inradius $4$

*Setting up.* Let the three sides be $n - 1, n, n + 1$ for some positive integer $n \ge 2$ (so the smallest side is at least $1$). The semi-perimeter is
\[
  s \;=\; \frac{(n-1) + n + (n+1)}{2} \;=\; \frac{3n}{2}.
\]

*Area by Heron's formula.*
\[
  K \;=\; \sqrt{s(s - (n-1))(s - n)(s - (n+1))} \;=\; \sqrt{\frac{3n}{2} \cdot \frac{n + 2}{2} \cdot \frac{n}{2} \cdot \frac{n - 2}{2}}
  \;=\; \sqrt{\frac{3n^2(n^2 - 4)}{16}} \;=\; \frac{n}{4}\sqrt{3(n^2 - 4)}.
\]

*Inradius equation.* By $r = K / s$:
\[
  r \;=\; \frac{(n/4)\sqrt{3(n^2 - 4)}}{3n/2} \;=\; \frac{\sqrt{3(n^2 - 4)}}{6}.
\]
Setting $r = 4$:
\[
  \sqrt{3(n^2 - 4)} \;=\; 24 \quad\Longrightarrow\quad 3(n^2 - 4) \;=\; 576 \quad\Longrightarrow\quad n^2 - 4 \;=\; 192 \quad\Longrightarrow\quad n^2 \;=\; 196 \quad\Longrightarrow\quad n \;=\; 14.
\]
(Taking the positive root, since $n \ge 2$.)

*Domain check.* The sides are $13, 14, 15$ — three positive integers satisfying the triangle inequality ($13 + 14 = 27 > 15$). All good.

*Circumradius.* By $R = abc / (4K)$ with $K = (14/4)\sqrt{3 \cdot 192} = (14/4) \cdot 24 = 84$:
\[
  R \;=\; \frac{13 \cdot 14 \cdot 15}{4 \cdot 84} \;=\; \frac{2730}{336} \;=\; \frac{65}{8}.
\]
(Cancelling $\gcd(2730, 336) = 42$: $2730/42 = 65$, $336/42 = 8$.)

*Sanity check.* The triangle $13$–$14$–$15$ is a well-known classical triangle (the smallest Heronian triangle with consecutive integer sides) with area $84$, inradius $4$, and circumradius $65/8$. Our answer matches the classical value.

\[
  \boxed{R \;=\; \tfrac{65}{8} \;=\; 8.125 \text{ units.}}
\]

The domain-constraint here is *triple*: the sides must be consecutive integers (Form II), they must form a non-degenerate triangle (Form III), and the inradius must equal the specified value (an *equation* domain). The three constraints together pin down a unique answer.

---

### Solution to 5.3 — Log-Domain Restriction

*Domain analysis.* The function $f(x) = \log_4 (x - 1) - \log_2(x - 3)$ involves two logarithms. The natural domain is the intersection of the two log-argument-positivity conditions:
\[
  x - 1 \;>\; 0 \quad\text{(from $\log_4$)}, \qquad x - 3 \;>\; 0 \quad\text{(from $\log_2$)}.
\]
Solving: $x > 1$ AND $x > 3$. The intersection is the *stricter* of the two, namely $x > 3$.

*Verification.* For $x > 3$, both $x - 1$ and $x - 3$ are positive, so both logarithms are defined. For $1 < x \le 3$, the first logarithm is defined but the second is not, so $f$ is undefined. For $x \le 1$, neither logarithm is defined. Hence
\[
  \boxed{D_f \;=\; (3, \infty).}
\]
\hfill$\blacksquare$

*Pitfall.* A student who reads "$\log_4(x - 1) - \log_2(x - 3)$" as a *combined* expression might try to simplify first — using the base-change identity $\log_4 t = (1/2) \log_2 t$ — and obtain $(1/2)\log_2(x-1) - \log_2(x-3) = \log_2 \sqrt{x-1} - \log_2(x-3) = \log_2 \frac{\sqrt{x-1}}{x-3}$. This *simplified* form has the constraint $(x-3) > 0$ (denominator) and $x > 1$ (radicand) plus the requirement that the *ratio* $\sqrt{x-1}/(x-3)$ be positive (which it is, since both numerator and denominator are positive when $x > 3$). The simplified form has the same domain $(3, \infty)$ — but only by accident; in general, *simplification can change the domain*, and the domain of the original expression must be computed from the original expression, before simplification.

---

### Solution to 5.4 — Real-Root Condition on a Quartic

*Setting up.* The equation is $x^4 - 2ax^2 + x + a^2 - a = 0$. We seek all real $a$ for which all four roots are real.

*Key step — factorisation as a product of two quadratics.* Treat the equation as a *quadratic in $a$* with $x$ as a parameter:
\[
  a^2 - (2x^2 + 1) a + (x^4 + x) \;=\; 0.
\]
The discriminant in $a$ is
\[
  (2x^2 + 1)^2 - 4(x^4 + x) \;=\; 4x^4 + 4x^2 + 1 - 4x^4 - 4x \;=\; 4x^2 - 4x + 1 \;=\; (2x - 1)^2.
\]
The discriminant is a perfect square — so the quadratic factors nicely:
\[
  a \;=\; \frac{(2x^2 + 1) \pm (2x - 1)}{2}.
\]
The two roots in $a$ are $a = x^2 + x$ and $a = x^2 - x + 1$.

*Factorisation of the original quartic.* The quartic must therefore factor as $(a - x^2 - x)(a - x^2 + x - 1) = 0$, i.e.,
\[
  (x^2 + x - a)(x^2 - x + 1 - a) \;=\; 0.
\]
(One can verify the factorisation by direct expansion: $(x^2 + x - a)(x^2 - x + 1 - a) = x^4 - 2ax^2 + x + a^2 - a$, matching the original.)

*Reality conditions on each quadratic factor.* The roots of the original quartic are the roots of the two quadratics $x^2 + x - a = 0$ and $x^2 - x + 1 - a = 0$. For all four roots to be real, both quadratics must have real roots, i.e., both discriminants must be non-negative.

\begin{itemize}
\item For $x^2 + x - a = 0$: discriminant $= 1 + 4a \ge 0$, i.e., $a \ge -1/4$.
\item For $x^2 - x + 1 - a = 0$: discriminant $= 1 - 4(1 - a) = 4a - 3 \ge 0$, i.e., $a \ge 3/4$.
\end{itemize}

*Intersection of the two conditions.* All four roots are real iff *both* discriminants are non-negative, i.e., iff $a \ge -1/4$ AND $a \ge 3/4$. The intersection is the stricter condition,
\[
  \boxed{a \;\ge\; 3/4.}
\]
\hfill$\blacksquare$

The domain constraint here is *Form IV* — reality of polynomial roots — and the trick was the auxiliary observation that *the quartic is a quadratic in $a$ with parameter $x$*, which let us factor it as a product of two simpler quadratics. Without the factorisation, the discriminant analysis of the original quartic (using the general quartic discriminant) is substantially more involved.

---

### Solution to 5.5 — Trig-Range Restricts Real Roots

*Range bound on the LHS.* For every real $x$, $\cos x \in [-1, 1]$, so $\sin(\cos x) \in [\sin(-1), \sin 1] = [-\sin 1, \sin 1]$ (since $\sin$ is monotone increasing on $[-1, 1] \subset [-\pi/2, \pi/2]$). Numerically, $\sin 1 \approx 0.8415$.

*Domain filter on $x$.* The equation $\sin(\cos x) = x$ requires the LHS to equal $x$. Since the LHS lies in $[-\sin 1, \sin 1]$, the equation can have a solution only for $x \in [-\sin 1, \sin 1] \approx [-0.8415, 0.8415]$. Within $[-\pi, \pi]$, the candidate window is $[-\sin 1, \sin 1]$.

*Monotonicity on the candidate window.* Define $g(x) = \sin(\cos x) - x$. Then
\[
  g'(x) \;=\; \cos(\cos x) \cdot (-\sin x) - 1 \;=\; -\cos(\cos x) \sin x - 1.
\]
For $x \in [-\sin 1, \sin 1] \subset [-0.84, 0.84]$, we have $|\sin x| \le \sin 0.84 \approx 0.74$; $\cos x \in [\cos 0.84, 1] \approx [0.67, 1] \subset [0, 1]$; $\cos(\cos x) \in [\cos 1, \cos 0.67] \approx [0.54, 0.78]$, in particular positive and at most $1$. Hence $|\cos(\cos x) \sin x| \le 1 \cdot 0.74 < 1$, giving $g'(x) = -\cos(\cos x)\sin x - 1 \in [-1.74, -0.26]$. In particular $g'(x) < 0$ throughout the candidate window — $g$ is strictly decreasing.

*Endpoint values.*
\[
  g(-\sin 1) \;=\; \sin(\cos(-\sin 1)) + \sin 1 \;=\; \sin(\cos(\sin 1)) + \sin 1 \;\approx\; \sin(0.667) + 0.841 \;\approx\; 0.619 + 0.841 \;=\; 1.460 \;>\; 0,
\]
\[
  g(\sin 1) \;=\; \sin(\cos(\sin 1)) - \sin 1 \;\approx\; 0.619 - 0.841 \;=\; -0.222 \;<\; 0.
\]

*Conclusion.* The strictly-decreasing continuous function $g$ goes from $+1.460$ to $-0.222$ on $[-\sin 1, \sin 1]$, hence by the intermediate value theorem crosses zero *exactly once*. Outside this window (for $|x| > \sin 1$), $|\sin(\cos x)| \le \sin 1 < |x|$, so $\sin(\cos x) \ne x$. The total number of real solutions in $[-\pi, \pi]$ is $\boxed{1}$.

*Numerical value.* Iteration $x_{n+1} = \sin(\cos x_n)$ from $x_0 = 0.7$ converges to the fixed point $x \approx 0.6948$ within a few steps. \hfill$\blacksquare$

The domain constraint here is the *range bound* of the LHS, which forces $x$ into a small interval; the monotonicity argument plus IVT then pins down the unique solution. The pattern *range bound + monotonicity + IVT* is the universal Form-IV approach for counting zeros of a function on an interval.

---

### Solution to 5.6 — Euler's Inradius-Circumradius Bound

*Statement.* For every triangle $ABC$ with circumradius $R$ and inradius $r$, $R \ge 2r$, with equality if and only if $ABC$ is equilateral.

*Proof via Euler's identity.* Let $O$ and $I$ denote the circumcentre and the incentre of $ABC$. *Euler's identity for the triangle* states
\[
  OI^2 \;=\; R^2 - 2Rr \;=\; R(R - 2r).
\]
(*Proof of Euler's identity:* a standard exercise using $O$'s defining property $|OA| = |OB| = |OC| = R$, $I$'s defining property as the equidistant-from-the-sides point with $r = $ this distance, and the law of cosines / power-of-a-point on the configuration $A, O, I$. Joshi Ch. 11 Comment 9 gives the derivation in full; we cite the identity as established.)

The squared length $OI^2$ is non-negative, hence
\[
  R(R - 2r) \;\ge\; 0.
\]
Since $R > 0$ (a non-degenerate triangle has a positive circumradius), the inequality reduces to $R - 2r \ge 0$, i.e., $R \ge 2r$. \hfill$\blacksquare$

*Equality condition.* Equality $R = 2r$ holds iff $OI^2 = 0$, i.e., iff $O = I$ — the circumcentre coincides with the incentre. *This happens if and only if the triangle is equilateral*: in an equilateral triangle, all four classical centres (centroid, circumcentre, incentre, orthocentre) coincide at a single point; in any non-equilateral triangle, no two of these centres coincide (a standard fact in triangle geometry).

*Comment on the slate's "acute" restriction.* The problem statement in the locked slate restricts to acute triangles, but the result holds for *every* triangle (acute, right, obtuse), as the proof above does not use acuteness. The "acute" restriction is therefore redundant; we have stated and proved the result in its general form.

The domain constraint here is the *non-degeneracy* of the triangle, encoded in $R > 0$ and in the existence of the incentre and circumcentre. The inequality $R \ge 2r$ is the *sharp* bound on the $r$-to-$R$ ratio for any non-degenerate triangle, and the equality case identifies the *boundary* of the constraint as the equilateral configuration.

---

### Solution to 5.7 — Tower Height from Two Angles of Elevation

*Setting up coordinates.* Place the tower foot $O$ at the origin, the tower along the positive $y$-axis with top at $(0, h)$. Let the horizontal line through $O$ on which $P$ and $Q$ lie be the $x$-axis.

*Case (a) — $P$ and $Q$ on the same side of $O$.* Take both on the positive $x$-axis: $P = (p, 0)$ and $Q = (q, 0)$ with $0 < p < q$ (so $P$ is closer; thus $\alpha > \beta$).

From $P$: the angle of elevation to $(0, h)$ is $\alpha$, so $\tan \alpha = h / p$, giving $p = h \cot\alpha$.
From $Q$: the angle of elevation is $\beta$, so $\tan \beta = h / q$, giving $q = h \cot\beta$.
The distance $d$ from $P$ to $Q$ is $d = q - p = h(\cot\beta - \cot\alpha)$.

Using the identity $\cot\beta - \cot\alpha = \frac{\cos\beta}{\sin\beta} - \frac{\cos\alpha}{\sin\alpha} = \frac{\cos\beta\sin\alpha - \cos\alpha\sin\beta}{\sin\alpha\sin\beta} = \frac{\sin(\alpha - \beta)}{\sin\alpha\sin\beta}$,
\[
  d \;=\; h \cdot \frac{\sin(\alpha - \beta)}{\sin\alpha\sin\beta} \quad\Longrightarrow\quad h \;=\; \boxed{\frac{d \sin\alpha\sin\beta}{\sin(\alpha - \beta)}}. \quad (\text{same-side})
\]

*Case (b) — $O$ between $P$ and $Q$.* Take $P = (-p, 0)$ on the negative $x$-axis and $Q = (q, 0)$ on the positive, with $p, q > 0$.

From $P$: $\tan\alpha = h / p$, so $p = h \cot\alpha$.
From $Q$: $\tan\beta = h / q$, so $q = h \cot\beta$.
Distance $d$ from $P$ to $Q$ is $d = p + q = h(\cot\alpha + \cot\beta) = h \cdot \frac{\sin(\alpha + \beta)}{\sin\alpha\sin\beta}$.
\[
  h \;=\; \boxed{\frac{d \sin\alpha\sin\beta}{\sin(\alpha + \beta)}}. \quad (\text{opposite-side})
\]

*Domain check.* In both cases, $0 < \beta < \alpha < \pi/2$, so $\sin\alpha, \sin\beta > 0$. In Case (a), $\alpha - \beta \in (0, \pi/2)$, so $\sin(\alpha - \beta) > 0$ and $h > 0$ as required. In Case (b), $\alpha + \beta \in (0, \pi)$, so $\sin(\alpha + \beta) > 0$ and $h > 0$. Both formulas give a positive height — the *domain constraint* "tower height is positive" is automatically satisfied for the specified angle ranges.

The sign-convention domain check here is *Form III* in the §3.2 taxonomy — the geometric configuration (same side vs. opposite side) is a discrete domain choice that *changes the formula*. Without distinguishing the two cases, a student might apply the same-side formula in the opposite-side configuration, getting $h$ off by a factor of $\sin(\alpha + \beta)/\sin(\alpha - \beta)$ — sometimes catastrophically wrong. The discipline of *considering all configurations consistent with the problem's wording* catches this. \hfill$\blacksquare$

---

*End of Chapter 9.*

