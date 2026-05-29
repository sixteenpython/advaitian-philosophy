---
chapter: 7
archetype: Normalisation / Scaling
subtitle: "Remove the Clutter; Keep Only the Structure"
category: Method Selection (Archetypes 5–8)
related_archetypes: [2, 5, 6, 10, 12, 17]
key_gems: [A17, B13, B14, D07d]
  - "Buckingham's $\\pi$ theorem: $n$ variables and $k$ independent dimensions yield $n - k$ dimensionless groups"
  - "Constraint normalisation: for an inequality homogeneous of any degree in $a, b, c$, WLOG $a + b + c = 1$ (or any other scale-fixing constraint)"
  - "Dimensional reduction of the pendulum period: $T = 2\\pi\\sqrt{L/g}$, with the $2\\pi$ supplied by linearisation"
  - "Cauchy-Schwarz on the unit sphere: $\\|u\\| = \\|v\\| = 1 \\Rightarrow |\\langle u, v \\rangle| \\le 1$"
  - "Symmetric-diagonal optimum: when constraint and objective share a permutation symmetry, the extremum lies on the diagonal $\\alpha_1 = \\cdots = \\alpha_n$"
  - "Euler's identity for homogeneous functions: $\\sum_i x_i \\, \\partial f / \\partial x_i = k\\, f$ for $f$ homogeneous of degree $k$"
  - "Power-mean inequality: $M_p \\le M_q$ for $p \\le q$, normalised over a probability measure"
  - "Chebyshev's sum inequality: $n \\sum a_i b_i \\ge \\left(\\sum a_i\\right)\\left(\\sum b_i\\right)$ for similarly ordered sequences"
  - "z-score normalisation: $(x - \\mu)/\\sigma$ as the canonical statistical rescaling that fixes mean $0$, variance $1$"
  - "Natural units in physics: setting $c = \\hbar = G = k_B = 1$ to expose the dimensionless skeleton of a theory"
canonical_takeaway: "Normalisation strips away every degree of freedom that doesn't matter; what remains is structure."
status: locked
last_revised: 2026-05-29
locked_on: 2026-05-29
sourcing_note: "All worked examples and practice problems in this chapter are drawn from K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), or from JEE / RMO / INMO examinations commented on in that text, **with one named exception**: Worked Example 1 (Buckingham-$\\pi$ Pendulum) is a standard physics-pedagogy result that illustrates dimensional normalisation more cleanly than any single Joshi problem can. The exception is permitted under Blueprint §6.10.07 (Normalisation scope), which explicitly anticipates the dimensional-analysis framing as the natural carrier of normalisation as a cognitive move. See Blueprint §6.2 for the general sourcing rule and `pillar2-archetypes/_template/joshi-problems-locked.md` §Ch. 7 for the locked slate and the framing-decision change-log."
---

# Chapter 7 — Normalisation / Scaling

## *Remove the Clutter; Keep Only the Structure*

---

## Opening Vignette

In November 2018, in a conference hall at Versailles, the international community of metrology did something quietly revolutionary. They redefined the kilogram. For one hundred and thirty years, the kilogram had been the mass of a single physical object — a platinum-iridium cylinder, the *International Prototype of the Kilogram* (IPK), kept under three nested bell jars in a vault outside Paris. To know what a kilogram was, one in principle had to compare to that cylinder. The trouble was that the cylinder, despite the bell jars, was slowly losing mass: traces of hydrocarbon contamination evaporated; microscopic shedding occurred; the very atoms of the platinum drifted. Over the twentieth century, the IPK was measured to have departed from its official replicas by some tens of micrograms. *The unit of mass was changing.* Worse: there was no way to detect this fact, because the IPK *was* the kilogram by definition. The 2018 redefinition severed this dependence. The kilogram was now to be the mass implied by fixing Planck's constant $h$ at exactly $6.62607015 \times 10^{-34}\,\text{J}\cdot\text{s}$ — a fundamental constant of nature. The new kilogram, unlike the old, was invariant under time because it was anchored to a quantity the universe itself underwrote.

The physicist working at the level of fundamental theory takes one further step. She sets the fundamental constants themselves to $1$: $c = 1$ (the speed of light), $\hbar = 1$ (Planck's reduced constant), $G = 1$ (Newton's gravitational constant), $k_B = 1$ (Boltzmann's constant). In these *natural units*, every physical quantity is dimensionless. Einstein's mass-energy relation becomes $E = m$. The Schwarzschild radius of a black hole is $2M$. The thermal energy at temperature $T$ is just $T$. The Compton wavelength of a particle of mass $m$ is $1/m$. What had been a forest of physical constants — letters in equations whose only function was to convert between units — becomes a clean algebraic landscape, and the relations between physical quantities stand revealed as relations between numbers. The constants did not disappear; they were absorbed into the choice of unit. The physics survives unchanged. What changes is the visibility of the structure.

Now consider a humbler scene. A graduate student is asked to draw a map of her university campus, useful for orienting an incoming class. She has a sheet of A4 paper. The campus, end to end, is about two kilometres across. What scale should she choose? At $1:1$, the map *is* the campus — every footpath rendered at full size, every building exactly where it stands. Such a map is mathematically perfect and physically useless. At $1:200{,}000$, the campus appears as a single dot on her sheet; the map shows the entire region, perhaps the whole metropolitan area, but tells the freshman nothing about how to walk from the residence halls to the lecture theatre. At $1:10{,}000$ — one centimetre on the page corresponds to one hundred metres on the ground — the campus fills the sheet, every building is identifiable, and the new arrival can locate herself in two seconds. The scale $1:10{,}000$ is not the *right* scale by some platonic criterion. It is the right scale *for the question being asked*. The cartographer's first decision, before any drawing, is choice of scale.

These two scenes look unrelated. A laboratory in Versailles redefining a base unit; a graduate student choosing the scale of a map. They share one of the most consequential observations in mathematics and the sciences. In each, *a problem is laden with a degree of freedom that does not matter to the question being asked*, and the resolution is the same: *choose a value for that degree of freedom — pick the scale — and the structure that does matter becomes visible*. The physicist sets $c = 1$ because the absolute speed of light is irrelevant to whether $E$ equals $mc^2$; what is relevant is the algebraic relation. The cartographer chooses $1:10{,}000$ because the absolute size of the campus is irrelevant to whether the freshman can find her way; what is relevant is the relative geometry. *In both cases, the move is identical: quotient out the irrelevant degree of freedom by fixing it to a convenient value.*

This is *Normalisation*. It is the third archetype of the *Method Selection* sub-pillar, and where Substitution chose a clever variable and Linearisation chose a local linear approximation, Normalisation chooses a *value for an irrelevant scaling degree of freedom*, thereby reducing the problem to a strictly smaller form in which only the structural content remains. The move appears under many names — *non-dimensionalisation*, *scale-fixing*, *WLOG-the-sum-equals-one*, *projective normalisation*, *gauge-fixing*, *z-score normalisation*, *Buckingham-$\pi$ reduction* — and it appears in every quantitative discipline. What unifies them is the same logic: *identify a transformation under which the problem is invariant; pick a representative orbit of that transformation; solve only on the representative*. The rest is bookkeeping.

> *Normalisation strips a problem of every degree of freedom that does not matter; what remains is the structure that does.*

---

## 1. The Archetype Defined

### 1.1 Formal Definition

We make the intuition precise.

\begin{definition}[Normalisation]
A problem $P$ involves variables $x_1, \ldots, x_n$ and possibly external parameters. Suppose there is a group $G$ acting on the variable space such that the truth value, the optimum, the existence of a solution, or some other quantity of interest in $P$ is *invariant* under the action of $G$ — for every $g \in G$ and every relevant input $x$, the answer for $x$ and the answer for $g \cdot x$ are the same. A *normalisation* of $P$ is a choice of one representative from each $G$-orbit, together with a rewriting of $P$ in terms of those representatives. The normalised problem $P_\text{norm}$ has *fewer free variables* than $P$ — typically $\dim P - \dim G$ — and its solution determines the solution of $P$ by inverting the chosen representative.
\end{definition}

This is abstract; three concrete instantiations make it operational. In each, identify the group $G$, the invariance, and the representative.

- **Constraint normalisation.** Let $f(a, b, c)$ be a function homogeneous of degree $k$ in $(a, b, c)$ — that is, $f(\lambda a, \lambda b, \lambda c) = \lambda^k f(a, b, c)$ for every $\lambda > 0$. The inequality $f(a, b, c) \ge g(a, b, c)$, where $g$ is homogeneous of the same degree $k$, is then invariant under the scaling $(a, b, c) \mapsto (\lambda a, \lambda b, \lambda c)$ for $\lambda > 0$ — the group $G = \mathbb{R}_{>0}$ acts diagonally. The natural representative of each orbit is the one in which $a + b + c = 1$ (or in which $a^2 + b^2 + c^2 = 1$, or in which $abc = 1$, depending on convenience). The normalised inequality has *two* free variables instead of three.

- **Dimensional normalisation.** Let a physical quantity $Q$ depend on $n$ variables $x_1, \ldots, x_n$ with physical dimensions, and suppose the variables involve $k$ independent base dimensions (say, length $L$, time $T$, mass $M$, etc.). The relation $Q = F(x_1, \ldots, x_n)$ is invariant under any change of base units, which forms a group $G = (\mathbb{R}_{>0})^k$. By the *Buckingham-$\pi$ theorem* (proved in §2.1), the problem reduces to a relation among $n - k$ dimensionless combinations $\pi_1, \ldots, \pi_{n-k}$ of the original variables.

- **Symmetric-diagonal normalisation.** When the problem is invariant under a permutation symmetry of its variables — say, $f(x_1, \ldots, x_n)$ is symmetric and the constraint is symmetric — the optimum, if unique, lies on the *symmetric diagonal* $x_1 = x_2 = \cdots = x_n$ (modulo subtleties about boundary or degenerate optima). The group $G$ is the symmetric group $S_n$; the symmetric-diagonal is the orbit-fixed locus; the $n$-variable optimisation reduces to a $1$-variable optimisation along the diagonal.

In each instantiation, the *count of degrees of freedom drops by exactly the dimension of $G$*. That is the operational benefit. The structural benefit, larger and more important, is that *the irrelevant freedom is now invisible*; nothing in the normalised problem depends on the scale, the units, or the labelling, and the solver's attention is no longer dispersed across them.

### 1.2 The Core Principle

The principle of normalisation, stripped to its essence, is one sentence.

> *When the problem is invariant under a transformation, fix the transformation; only the structure remains.*

This sentence is a refinement of, but not the same as, the central principle of Symmetry (Archetype 2). Symmetry says: *if the problem has a symmetry, the solution inherits it*. Normalisation says something stronger: *if the problem has a symmetry, fix a representative of each orbit and solve only on the representative*. Symmetry exploits the invariance to constrain the solution's shape. Normalisation exploits the invariance to *reduce the problem to a smaller one*. The two archetypes work together — every normalisation is fundamentally a symmetry — but the cognitive moves are distinct. A solver who recognises a problem as symmetric will conclude something about the answer. A solver who recognises a problem as normalisable will *change the problem*.

The principle inverts a deeply ingrained habit. When a novice encounters a problem stated in full generality — six positive reals satisfying some inequality, a physical relation with five dimensioned quantities, an $n$-variable optimisation with a symmetric constraint — the instinct is to *treat all the variables as essential* and to manipulate them symbolically. The instinct is not wrong; in some problems each variable plays an essential and distinct role. But it overlooks the alternative: *check first whether the problem has a scaling invariance, a dimensional invariance, or a permutation invariance, and if it does, quotient by that invariance before doing any work*. The remaining problem is strictly smaller, and the work spent on the symmetric directions was always wasted.

### 1.3 The Cognitive Shift

The cognitive shift Normalisation enforces is from *"all variables are independent"* to *"many problems are scale-invariant — pin one variable, the rest follow."* This is the WLOG-pricing move: *without loss of generality*, we may assume the perimeter is $1$, or the maximum entry is $1$, or the constants are in natural units. The shift sounds elementary; in practice, it is the single most underused move in JEE-level problem solving. Students who could halve their working on a homogeneous inequality by setting $a + b + c = 1$ instead grind through general $(a, b, c)$ for a page before reaching for AM-GM. The cost is not algebraic — the calculation works out either way — but cognitive: every symbol on the page is one more thing the solver must hold in mind, and the irrelevant degrees of freedom occupy working memory that the structural insight needs for itself.

A second shift, less obvious, is from *"answer in physical units"* to *"answer in dimensionless form."* In the physical sciences this shift is reflexive; the period of a pendulum is *not* "$2.0$ seconds" but "$2\pi \sqrt{L/g}$ seconds." The first form is the value of one experiment; the second is the *law* and applies to every pendulum in the universe. The dimensionless form $T \sqrt{g/L} = 2\pi$ is what survives across all choices of $L$ and $g$, and it is the dimensionless form that has scientific content. JEE problems rarely demand this explicitly — the answer is asked in concrete numbers, the parameters are given numerically — but the discipline of *writing the answer in dimensionless form first, then specialising at the end* is the discipline that scales from competition mathematics to research science. The trained solver internalises it early.

The third shift, which the chapter will develop in §2, is from *"calculate; then check"* to *"check the symmetry first; calculate only what survives."* The Buckingham-$\pi$ theorem, in this reading, is a labour-saving device: it tells the physicist, *before any calculation*, how many genuinely independent quantities are in the problem, and thus how much work she actually has to do. This is the same kind of accounting that Degrees-of-Freedom Analysis (Archetype 17) systematises across mathematics. Normalisation is the *first* such accounting move every trained solver makes.

---

## 2. The Deep Structure

### 2.1 Mathematical Foundations

Normalisation rests on three formal foundations, which we state in increasing generality.

The first is the theory of *homogeneous functions*. A function $f : \mathbb{R}^n_{>0} \to \mathbb{R}$ is *homogeneous of degree $k$* if
\[
  f(\lambda x_1, \ldots, \lambda x_n) \;=\; \lambda^k f(x_1, \ldots, x_n)
\]
for every $\lambda > 0$ and every $(x_1, \ldots, x_n) \in \mathbb{R}^n_{>0}$. Polynomials in which every monomial has the same total degree are homogeneous; ratios of homogeneous polynomials of equal degrees are homogeneous of degree $0$ (i.e., scale-invariant). The fundamental fact about homogeneous functions, due to Euler, is the identity
\[
  \sum_{i=1}^n x_i \, \frac{\partial f}{\partial x_i} \;=\; k\, f(x_1, \ldots, x_n) \qquad \text{(Euler's homogeneity identity)},
\]
proved by differentiating the homogeneity relation $f(\lambda x) = \lambda^k f(x)$ with respect to $\lambda$ at $\lambda = 1$. Euler's identity is the infinitesimal statement of homogeneity, and it is what justifies the move *fix one of the $x_i$ to a convenient value*: the constraint $f = c$ for some constant $c$, combined with homogeneity, picks out a single representative of each scaling orbit, and Euler's identity makes the constraint compatible with the homogeneity. For inequalities of the form $f \ge g$ where both sides are homogeneous of the same degree, the inequality $f / g \ge 1$ is homogeneous of degree $0$ — scale-invariant — and the WLOG-normalisation $\sum x_i = 1$ (or any equivalent) is *free*: it neither strengthens nor weakens the claim.

The second foundation is the *Buckingham-$\pi$ theorem*. Suppose a physical relation has the form $Q = F(x_1, \ldots, x_n)$, where $Q$ and the $x_i$ all carry physical dimensions expressible in terms of $k$ independent base dimensions (such as length $L$, time $T$, mass $M$). The relation must be invariant under the simultaneous rescaling of all base units — replacing every metre by every kilometre changes the numerical values of every variable but cannot change the truth of a physical law. The Buckingham-$\pi$ theorem states that under these conditions, the relation can be written equivalently as
\[
  \Phi(\pi_1, \pi_2, \ldots, \pi_{n-k}) \;=\; 0
\]
where $\pi_1, \ldots, \pi_{n-k}$ are *dimensionless* combinations of the original variables (and $\Phi$ is some function determined by the physics, not by the units). The proof is essentially linear algebra: the dimensions of the variables, written as $k$-vectors of exponents in the base dimensions, span a subspace of $\mathbb{R}^k$ of dimension at most $k$; the kernel of the corresponding linear map (from $\mathbb{R}^n$ to $\mathbb{R}^k$) has dimension at least $n - k$, and any vector in the kernel corresponds to a monomial $\prod x_i^{a_i}$ that is dimensionless. The dimensionless combinations form the *$\pi$-groups* of the problem. WE1 illustrates the theorem in its most elementary form: the pendulum problem has $n = 3$ variables and $k = 2$ dimensions, hence $n - k = 1$ dimensionless group, namely $T \sqrt{g/L}$.

The third foundation, the most general, is the theory of *group actions and quotient spaces*. Whenever a group $G$ acts on a space $X$ leaving a problem invariant, the natural object is the quotient $X/G$ — the space of $G$-orbits — and the problem descends to a problem on $X/G$. Normalisation is the choice of a *section* of the orbit projection $X \to X/G$: a way of picking one representative from each orbit so that the problem can be stated on the chosen representatives. The mathematical content of the problem is determined by the quotient $X/G$; the choice of section is a *gauge*, a convenience, with no intrinsic content beyond making computations tractable. This is the perspective of gauge theory in physics, of projective geometry, of moduli space, and of the equivariant cohomology of algebraic topology — and the elementary appearance in inequalities (*WLOG $\sum x_i = 1$*) is the special case where the group is $\mathbb{R}_{>0}$ acting by scaling, the section is the simplex $\{x : \sum x_i = 1\}$, and the quotient is the projective simplex.

### 2.2 Physical and Cross-Domain Foundations

The reach of normalisation extends well beyond competition mathematics. We sketch four domains.

In *physics*, dimensional analysis is the universal labour-saving device. The Reynolds number $\mathrm{Re} = \rho v L / \mu$ (density times velocity times length over viscosity) is what one obtains from non-dimensionalising the Navier-Stokes equations: the dimensionless number that emerges is the *signature of the flow regime*. At low Reynolds number the flow is laminar and the equations linear-dominated; at high Reynolds number the flow is turbulent and the nonlinearity dominates. The transition occurs at a specific value of $\mathrm{Re}$ (around $\mathrm{Re} \approx 2300$ for pipe flow) that is *universal* — independent of the size of the pipe, the speed of the fluid, the viscosity, the density. Without non-dimensionalisation, the engineer would have to re-derive this transition for every fluid and every geometry. With it, the entire taxonomy of fluid flow is governed by a small number of dimensionless groups (Reynolds, Mach, Péclet, Prandtl, Froude, Strouhal). The same is true of plasma physics, of aerodynamics, of heat transfer. The dimensionless groups are the *classification scheme* of the physics.

In *statistics*, the canonical normalisation is the *z-score*: given a random variable $X$ with mean $\mu$ and standard deviation $\sigma$, the standardised variable $Z = (X - \mu)/\sigma$ has mean $0$ and variance $1$. Two distinct distributions can then be compared *on the same scale*. The central limit theorem, properly stated, is a statement about the convergence of standardised sums to the standard normal distribution — *the standardisation is what makes the universality statement possible*. Without the standardisation, every sum of independent random variables would have its own scale; with it, they all converge to one limit, $N(0, 1)$. The discipline of standardisation is what allows statistics to make universal statements about phenomena that, in raw units, look entirely different.

In *economics*, the analogous normalisation is the *real* (versus nominal) value. A wage of Rs. 100 in 1980 and a wage of Rs. 1000 in 2020 are not comparable in nominal terms; deflating each by the relevant price index (the consumer price index, the GDP deflator) yields real wages in some chosen base year's units, which *are* comparable. Every cross-country GDP comparison is similarly preceded by purchasing-power-parity (PPP) normalisation, which converts nominal exchange rates into rates that equalise the cost of a standard basket of goods. The first thing every serious economist does to a number is normalise it; the normalisation is what allows comparison across time and place.

In *engineering*, the *per-unit system* in power engineering normalises every electrical quantity (voltage, current, impedance) by a chosen base value, so that the resulting per-unit quantities are dimensionless and lie in well-controlled ranges (typically near $1$). The base values are chosen so that transformer ratios drop out of the analysis: a transformer that steps voltage up by a factor of $10$ is invisible in the per-unit system, because its voltage on both sides is $1$ per-unit. The simplification is enormous. The per-unit system is the engineer's local version of Buckingham-$\pi$, applied not to fundamental physical constants but to design-chosen base values.

### 2.3 Cognitive Foundations

The cognitive payoff of normalisation is twofold. The first is *reduction of working memory load*. A problem with $n$ variables requires the solver to track $n$ symbols, $n$ partial derivatives, $n$ dependencies. A problem normalised down to $n - k$ effective variables requires the solver to track only $n - k$. For the JEE student working under time pressure, the saving is direct: every degree of freedom eliminated is a degree of attention freed for the structural insight. For the research scientist, the saving compounds: the dimensionless form of an equation is the form that *generalises*, the form whose validity extends from one problem to the entire family of problems sharing the same dimensionless structure.

The second payoff is *recognition*. When a problem is written in dimensioned variables, two structurally identical problems can look entirely different. The pendulum period in seconds, given $L$ in metres and $g$ in metres per second squared, is one expression. The same pendulum period in milliseconds, given $L$ in millimetres and $g$ in millimetres per millisecond squared, is a completely different-looking expression with different numerical constants. The dimensionless form $T\sqrt{g/L} = 2\pi$ is one expression for both. The discipline of writing answers in dimensionless form is the discipline that makes *recognition* of structural identity possible. The same point applies in pure mathematics: an inequality stated for $a + b + c = 1$ and the same inequality stated for general $a, b, c$ are the same inequality; recognising this is the move that lets the solver transfer a learned technique to a new instance.

---

## 3. The Diagnostic Toolkit

### 3.1 The Three Questions Method (Normalisation Edition)

Before any algebra, the trained solver asks three questions of the problem in front of her.

1. **Is there a scaling invariance?** Does the answer (or the inequality, or the existence of a solution) remain unchanged if every variable is multiplied by a common positive constant? If the problem involves a *homogeneous* relation — every term of the same degree — the answer is almost certainly yes. The remedy is constraint normalisation: fix the scale by adding a constraint like $\sum x_i = 1$ or $\prod x_i = 1$ or $\max_i x_i = 1$. The fixed constraint should be the one that makes the remaining algebra easiest.

2. **Are there irrelevant dimensions?** Does the problem involve dimensioned quantities (length, time, mass, currency, etc.)? If so, the answer is invariant under simultaneous rescaling of every base unit, and Buckingham-$\pi$ reduces the count of effective variables by the count of independent base dimensions. The remedy is dimensional analysis: write each variable's dimensions; form the dimensionless combinations; restate the problem in terms of the dimensionless variables alone.

3. **Is there a permutation symmetry?** Does the problem treat its variables symmetrically — both the constraint and the objective unchanged under relabelling? If so, the natural representative of each orbit is the *symmetric diagonal* $x_1 = x_2 = \cdots = x_n$, and the optimum, when unique, lies there. The remedy is symmetric-point normalisation: check whether the diagonal satisfies the constraint, evaluate the objective on the diagonal, and *verify* afterwards (by Lagrange or by direct argument) that the diagonal is in fact the optimum.

If all three answers are "no," normalisation is not the right archetype for this problem; reach for Substitution (Ch. 5) or Hidden Structure (Ch. 4) instead. If any answer is "yes," proceed with the corresponding normalisation *before* the main algebraic work.

### 3.2 Forms of Normalisation: A Comprehensive Guide

We collect the four characteristic forms encountered in the chapter, with one-line diagnostics for each.

- **Form I — Constraint normalisation (scale-fixing).** *Diagnostic:* the inequality, equation, or optimum is homogeneous in its variables. *Move:* fix one homogeneous combination (e.g., $\sum x_i = 1$, $\prod x_i = 1$, $\max_i x_i = 1$, $\sum x_i^2 = 1$). *Examples.* WE2 (Cauchy on $a + b + c = 1$), PP1 (min of $a^2 + b^2$ subject to $a + b = 6$), PP2 (homogeneous AM-GM cube), PP4 (QM $\ge$ AM via normalisation $\sum x_i = 0$ or $\sum x_i = 1$), PP5 (Schwarz integral form via $\|f\|_2 = \|g\|_2 = 1$).

- **Form II — Dimensional normalisation (Buckingham-$\pi$).** *Diagnostic:* the variables carry physical dimensions, and the answer is invariant under change of base units. *Move:* identify the $n - k$ dimensionless combinations and restate the problem in terms of them. *Examples.* WE1 (pendulum period $T = 2\pi\sqrt{L/g}$). The form is dominant in physics and engineering; in competition mathematics it appears only when a problem is set up with physical motivation, but the underlying mathematical content (Euler's homogeneity identity applied to the dimensions) is the same.

- **Form III — Symmetric-diagonal normalisation.** *Diagnostic:* the constraint and the objective are invariant under permutation of the variables. *Move:* test the diagonal $x_1 = \cdots = x_n$, evaluate the objective, then prove the diagonal is the optimum by AM-GM, Cauchy, Jensen, or Lagrange. *Examples.* WE3 (max of $\prod \cos \alpha_i$ on the diagonal $\alpha_i = \pi/4$), PP3 (max of $x + y + z$ subject to $x^2 + y^2 + z^2 = 9$ on the diagonal $x = y = z = \sqrt{3}$), PP6 (power-mean inequality, equality on the diagonal $x_1 = \cdots = x_n$), PP7 (Chebyshev's sum inequality, equality when one of the sequences is constant — a degenerate diagonal).

- **Form IV — Geometric scale-fixing (projective normalisation).** *Diagnostic:* a geometric problem in which the answer is independent of the absolute size of the configuration — angles, ratios, scale-invariant areas. *Move:* fix one length (e.g., the circumradius $R = 1$, the longest side $= 1$, the inradius $r = 1$) and compute the rest in terms of that unit. This form is closely related to Form I, but the geometric instinct deserves a separate name. *Examples.* Not directly in this chapter's WE/PP slate, but ubiquitous in Joshi Ch. 11 (Triangle Geometry) and Ch. 14 (Trigonometric Identities); the chapter's Connections section (§6.1) traces the link.

### 3.3 Common Pitfalls

Even with the diagnostic clearly identified, several errors are characteristic of beginners. Each has a memorable name; the trained solver carries the names as warnings.

- **The Fool's Scaling (applying scale-fixing to a non-homogeneous problem).** Setting $a + b + c = 1$ is *free* only when the problem is homogeneous. If the inequality is $a^2 + b^2 + c^2 + abc \ge 1$, the LHS is not homogeneous (the first three terms are degree $2$, the fourth degree $3$) — fixing $a + b + c = 1$ *changes the problem*. The check is mechanical: verify that every term of the inequality (or both sides) has the same total degree before scale-fixing. If they do not, *do not normalise*; reach for a different archetype (often Substitution to homogenise).

- **The Vanishing Dimension (incorrectly counting independent dimensions in Buckingham-$\pi$).** The theorem reduces $n$ variables by $k$ *independent* dimensions, not by the count of base dimensions appearing. If two of the variables involve only the same two dimensions in the same ratio, the effective dimension count is smaller, and the resulting number of dimensionless groups is larger than naive counting suggests. The remedy is to form the dimension matrix (variables as columns, base dimensions as rows) and compute its rank; the rank is $k$.

- **The Diagonal Fallacy (assuming a symmetric-diagonal optimum without verifying).** For symmetric constraints and symmetric objectives, the diagonal is the *natural candidate* for the optimum — but candidate is not certificate. The constraint $a + b + c = 1$ with $a, b, c \ge 0$ admits a symmetric optimum for $\max(a^2 + b^2 + c^2)$? No — the maximum is on the *boundary*, at $(1, 0, 0)$. The symmetric diagonal is a *minimum* there, not a maximum. The remedy is to verify by second-derivative test, by direct comparison with boundary values, or by an inequality argument.

- **The Constraint-Forgetting Sin (normalising correctly, then forgetting to scale back).** A problem stated in general $(a, b, c)$ is normalised to $a + b + c = 1$, solved, and the answer is reported — but the answer in the normalised problem is *not* the answer in the original problem unless one re-scales by the original $a + b + c$. For Form I constraint-normalisation of an *inequality* (where the inequality is scale-invariant), no rescaling is needed; for an *equation* or an *optimum value*, rescaling at the end is essential. The remedy is to write the homogeneity degree of every quantity at the start, and re-multiply by the appropriate power of $\sum x_i$ at the end.

- **The Dimensional Coincidence (treating two coincident dimensionless groups as independent).** When two distinct combinations of the variables happen to be dimensionless, they may or may not be independent. For instance, $T \sqrt{g/L}$ and $(T \sqrt{g/L})^2$ are both dimensionless but represent the same dimensionless group. The remedy is to verify independence in the dimension matrix's null space.

The five pitfalls, taken together, are the chapter's negative space — the patterns the trained solver pre-emptively checks against.

---

## 4. Worked Examples

We work three problems in detail, each in the six-point format. The first illustrates dimensional normalisation (Form II) in a physics setting; the second, constraint normalisation (Form I) on a classic homogeneous inequality; the third, symmetric-diagonal normalisation (Form III) on a JEE 2001 optimisation.

### 4.1 Example 1 — Buckingham-$\pi$ Pendulum

**Problem.** *Show by dimensional analysis that the small-amplitude period of a simple pendulum of length $L$ in a uniform gravitational field of acceleration $g$ must have the form $T = c \sqrt{L/g}$ for some dimensionless constant $c$. Then derive $c = 2\pi$ from the linearised equation of motion.* (Standard physics-pedagogy; see Blueprint §6.10.07 for the framing rationale.)

**SEED.** *Normalisation by dimensional analysis (Form II).* The period $T$ depends on physical quantities with dimensions; the law of motion must be invariant under change of unit; Buckingham-$\pi$ then forces the algebraic form of the answer. The dimensionless prefactor — and only the prefactor — requires the physics.

**BRUTE PATH.** A student first encountering the pendulum writes Newton's equation directly: for a point mass $m$ at the end of a massless rigid rod of length $L$, swinging in a uniform gravitational field $g$, the tangential equation of motion is
\[
  m L \ddot\theta \;=\; -m g \sin \theta,
\]
where $\theta$ is the angular displacement from the downward vertical. The mass $m$ cancels (Galileo's observation): $\ddot\theta = -(g/L) \sin\theta$. This is a *nonlinear* ODE; its exact solution is given in terms of the *Jacobi elliptic functions*, and the period as a function of amplitude $\theta_0$ is
\[
  T(\theta_0) \;=\; 4 \sqrt{\frac{L}{g}} \, K\!\left(\sin \frac{\theta_0}{2}\right),
\]
where $K(k) = \int_0^{\pi/2} d\varphi / \sqrt{1 - k^2 \sin^2\varphi}$ is the complete elliptic integral of the first kind. For $\theta_0 \to 0$, $K(0) = \pi/2$, giving $T(0) = 2\pi \sqrt{L/g}$. The brute path *succeeds* — it gives the exact period at every amplitude, of which the small-amplitude limit is one consequence — but it requires the entire apparatus of elliptic functions, an advanced topic by JEE or even by undergraduate-physics standards. The amount of machinery deployed is wildly disproportionate to the question asked.

**ELEGANT PIVOT.** Before invoking any equation of motion, we ask what variables the period can possibly depend on. Newton's laws are *local* — the period of a particular pendulum depends on the parameters that *describe* the pendulum and the field, not on parameters elsewhere in the universe. The candidate variables are:

- $L$: length of the rod, dimensions $[L] = L$.
- $g$: gravitational acceleration, dimensions $[g] = L T^{-2}$.
- $m$: mass of the bob, dimensions $[m] = M$.
- $\theta_0$: maximum angular amplitude, dimensionless.

We seek the dimensions of $T$, which are $[T] = T$.

*First reduction:* the mass $m$ involves a base dimension ($M$) that no other variable shares. The only way a function of $\{L, g, m, \theta_0\}$ can yield a quantity with dimension $T$ (no $M$) is if $m$ does not appear. So the period is independent of $m$. (This is Galileo's universality of free fall, recovered from pure dimensional analysis.)

*Second reduction:* by hypothesis (small amplitude), $\theta_0 \to 0$, and the period $T$ should approach a limit independent of $\theta_0$. So the small-amplitude period depends only on $L$ and $g$.

Now apply Buckingham-$\pi$. The remaining variables are $T, L, g$, with $n = 3$. The base dimensions appearing are $L$ and $T$, with $k = 2$. Therefore there are $n - k = 1$ independent dimensionless groups. To find it, seek exponents $a, b, c$ such that $T^a L^b g^c$ is dimensionless:
\[
  T^a L^b (L T^{-2})^c \;=\; L^{b+c} T^{a - 2c} \;=\; L^0 T^0.
\]
This forces $b + c = 0$ and $a - 2c = 0$, so $c = a/2$ and $b = -a/2$. Setting $a = 2$ for normalisation: $b = -1$, $c = 1$, giving $\pi_1 = T^2 g / L$. (Equivalently $\sqrt{\pi_1} = T \sqrt{g/L}$.) Buckingham-$\pi$ then asserts that *any* relation among $T, L, g$ must be expressible as
\[
  \pi_1 \;=\; T^2 g / L \;=\; \text{const},
\]
that is,
\[
  T \;=\; c \sqrt{L/g}
\]
for some dimensionless constant $c$. The form is *forced by dimensions alone*. The physics has not yet been invoked.

*Determining the constant.* The dimensionless constant $c$ is *not* extractable from dimensions; for that we need the actual physics, but only enough to fix one number. The linearised equation of motion, $\ddot \theta + (g/L) \theta = 0$, is the simplest dynamical equation in physics: a simple harmonic oscillator with angular frequency $\omega = \sqrt{g/L}$. The period of any simple harmonic oscillator is $T = 2\pi/\omega$. Hence
\[
  T \;=\; \frac{2\pi}{\sqrt{g/L}} \;=\; 2\pi \sqrt{L/g},
\]
giving $c = 2\pi$. The work expended on the physics is one line; the dimensional analysis took care of everything else.

**PITFALLS.**

- *The Vanishing Dimension.* A student new to Buckingham-$\pi$ might leave $m$ in the variable list, count $n = 4$ and $k = 3$ (dimensions $L, T, M$), conclude $n - k = 1$ dimensionless group — and then struggle to write the group, because $m$ does not in fact combine with $T, L, g$ to make anything dimensionless. The remedy is to *form the dimension matrix and compute its rank* before assuming $k$ equals the count of dimensions appearing. Here, the column for $m$ has only an $M$-entry, and the matrix has rank $k = 2$ (the $M$-column is independent but contributes a coordinate no other column shares). The kernel has dimension $n - \text{rank} = 4 - 2 = 2$, with one combination giving $\pi_1$ and the other giving $m^0$ — that is, $m$ itself cannot appear nontrivially, and the relation reduces to the same $T = c\sqrt{L/g}$.

- *The Linearisation Forgotten.* A student who applies Buckingham-$\pi$ correctly may then forget that the constant $c$ depends on the small-amplitude assumption. For large amplitude, $c$ becomes $c(\theta_0)$ — the elliptic-integral result of the brute path — and the period grows with amplitude (the *anharmonicity correction*). The small-amplitude $c = 2\pi$ is recovered as the leading term in a power series in $\theta_0^2$.

- *Mass Smuggled Back In.* Friction, air drag, or an inhomogeneous mass distribution can break the $m$-independence — in those refinements the period genuinely depends on $m$. The pure result $T = 2\pi\sqrt{L/g}$ is for an idealised simple pendulum. The trained physicist names the idealisation as she invokes the result.

- *The Wrong $g$.* On a non-uniform field (near a planet's centre, or in orbit) $g$ varies with position, and the dimensional argument applies only locally. Bafflement results from invoking the formula at altitudes where $g$ is no longer uniform on the scale of $L$.

- *Treating $\pi_1 = T\sqrt{g/L}$ as the Same Group as $\pi_1' = (T\sqrt{g/L})^2$.* These are functionally dependent (one is a function of the other), but they look distinct; Buckingham-$\pi$ guarantees only that *the relation is expressible in terms of one independent dimensionless group*. Listing both as if they were independent over-counts the degrees of freedom.

**CONNECTIONS.**

*Primary archetype applications.* Buckingham-$\pi$ governs (a) the period of *any* simple harmonic oscillator: $T = 2\pi \sqrt{m/k}$ for a mass on a spring, $T = 2\pi \sqrt{LC}$ for an LC electrical circuit, each derived dimensionally up to the $2\pi$; (b) the *terminal velocity* of a falling sphere in a viscous fluid, $v_\text{term} \sim \rho g R^2 / \mu$ (Stokes's law in dimensional form, modulo factors of $\pi$); (c) the *Kepler third law* $T^2 \propto R^3$ for planetary orbits, which falls out of dimensional analysis of $T, R, GM$ (and the dimensionless constant $4\pi^2$ comes from Newton's laws).

*Alternative solution archetypes.* The pendulum period can also be derived by *Linearisation* (Archetype 6) of the nonlinear ODE — which is in fact part of the elegant pivot above — or by *Hidden Structure* (Archetype 4): recognising the equation $\ddot\theta + \omega^2 \theta = 0$ as the canonical SHM equation. Each archetype contributes a piece: Normalisation forces the *form* of the answer, Linearisation supplies the *equation*, Hidden Structure supplies the *interpretation*.

*Cross-domain manifestations.* The Reynolds number $\mathrm{Re} = \rho v L / \mu$ in fluid dynamics, the Mach number $M = v / c_s$ in compressible flow, the Péclet number in heat transfer — each is a Buckingham-$\pi$ group, and each defines a regime of behaviour invariant under change of unit. In *biology*, the Strouhal number $\mathrm{St} = f L / v$ governs vortex shedding and animal locomotion, predicting (remarkably) that fish, birds, and insects propel themselves at universal values of $\mathrm{St}$ across a range of body sizes spanning many orders of magnitude. The single dimensionless group classifies the propulsion regime of the entire animal kingdom.

**TAKEAWAY.** *Units constrain the form of the answer; physics constrains only the constant.*

---

### 4.2 Example 2 — Cauchy-Schwarz on a Normalised Simplex

**Problem.** *For positive reals $a, b, c$ with $a + b + c = 1$, prove $a^2 + b^2 + c^2 \ge 1/3$, with equality if and only if $a = b = c = 1/3$.* (Joshi *EJM* Ch. 6, Comment 5; the inequality and its proof appear in the AM-QM commentary on Jensen's inequality applied to $f(x) = x^2$.)

**SEED.** *Normalisation by constraint (Form I).* The inequality, in its scale-invariant form $a^2 + b^2 + c^2 \ge (a + b + c)^2 / 3$, is homogeneous of degree $2$ in $(a, b, c)$; the constraint $a + b + c = 1$ is the natural representative of the scaling orbit. Once normalised, the inequality reduces to a single line of Cauchy-Schwarz.

**BRUTE PATH.** A student instinctively reaches for Lagrange multipliers. Minimise $f(a, b, c) = a^2 + b^2 + c^2$ subject to $g(a, b, c) = a + b + c - 1 = 0$. The Lagrangian is $\mathcal{L} = a^2 + b^2 + c^2 - \lambda(a + b + c - 1)$. Setting partial derivatives to zero:
\[
  \frac{\partial \mathcal{L}}{\partial a} = 2a - \lambda = 0, \quad
  \frac{\partial \mathcal{L}}{\partial b} = 2b - \lambda = 0, \quad
  \frac{\partial \mathcal{L}}{\partial c} = 2c - \lambda = 0,
\]
giving $a = b = c = \lambda/2$. The constraint forces $\lambda = 2/3$, so the critical point is $(1/3, 1/3, 1/3)$ with $f = 3 \cdot 1/9 = 1/3$. The Hessian is $2I$, positive definite, so this is the unique minimum. Therefore $a^2 + b^2 + c^2 \ge 1/3$. The path works — it gives the right answer with the right equality condition — but it expends multivariable calculus and a Hessian analysis on a problem that has the structure of a two-line inequality. For the JEE student or the Olympiad coach, the path is overkill.

**ELEGANT PIVOT.** We use Cauchy-Schwarz directly, in the form
\[
  \left( \sum_{i=1}^n a_i b_i \right)^2 \;\le\; \left( \sum_{i=1}^n a_i^2 \right) \left( \sum_{i=1}^n b_i^2 \right).
\]
Apply with $(a_1, a_2, a_3) = (a, b, c)$ and $(b_1, b_2, b_3) = (1, 1, 1)$:
\[
  (a \cdot 1 + b \cdot 1 + c \cdot 1)^2 \;\le\; (a^2 + b^2 + c^2)(1^2 + 1^2 + 1^2),
\]
that is,
\[
  (a + b + c)^2 \;\le\; 3 (a^2 + b^2 + c^2).
\]
Substituting the constraint $a + b + c = 1$ gives $1 \le 3(a^2 + b^2 + c^2)$, i.e., $a^2 + b^2 + c^2 \ge 1/3$. Equality in Cauchy-Schwarz holds iff the vectors $(a, b, c)$ and $(1, 1, 1)$ are proportional, which forces $a = b = c$; the constraint then yields $a = b = c = 1/3$.

*The normalisation insight.* The Cauchy-Schwarz proof has used the constraint $a + b + c = 1$ only at the final step, substituting it into a previously derived inequality. The inequality $(a + b + c)^2 \le 3(a^2 + b^2 + c^2)$ is *scale-invariant* — both sides are homogeneous of degree $2$ in $(a, b, c)$ — and therefore holds for *every* positive triple. In the unnormalised form, the statement reads
\[
  \frac{a^2 + b^2 + c^2}{(a + b + c)^2} \;\ge\; \frac{1}{3}.
\]
The ratio on the left is a degree-zero, scale-invariant quantity. The constraint $a + b + c = 1$ is therefore *free*: it picks one representative from each scaling orbit and changes nothing else. Imposing it converts a constrained-looking problem into an unconstrained inequality on the projective simplex, where the algebra is two lines. The constrained and the unconstrained forms are the same problem.

**PITFALLS.**

- *The Fool's Scaling.* The trick *only works* because $f(a, b, c) = a^2 + b^2 + c^2 - (a + b + c)^2 / 3$ is homogeneous of degree $2$. If the inequality had been $a^2 + b^2 + c^2 + abc \ge \alpha (a + b + c)$ — not homogeneous — then setting $a + b + c = 1$ would *not* be free; it would specialise the problem to one slice of the parameter space, and the resulting inequality would not entail the general one. Always check homogeneity *before* scale-fixing.

- *The Wrong Cauchy Pairing.* Cauchy-Schwarz with $(a, b, c)$ vs $(a, b, c)$ yields the trivial $(a^2 + b^2 + c^2)^2 \le (a^2 + b^2 + c^2)^2$. The productive pairing is $(a, b, c)$ vs $(1, 1, 1)$, because it introduces the *sum* $a + b + c$ on one side and the *sum of squares* on the other — exactly what the inequality relates.

- *Forgetting the Equality Case.* The problem asks for equality conditions. The Cauchy-Schwarz equality case (proportionality) immediately yields $a = b = c$, and the constraint then forces $1/3$. A student who omits the equality analysis loses points on a JEE Mains-style "necessary and sufficient" question.

- *Mistaking the Inequality for an Equality.* The result $a^2 + b^2 + c^2 \ge 1/3$ is a *lower bound*; the *upper bound* on $a^2 + b^2 + c^2$ subject to $a + b + c = 1$ and $a, b, c \ge 0$ is attained at the *boundary* (one of the variables equals $1$, the other two equal $0$), with value $1$. The bounds in the two directions come from *different* moves: Cauchy/Jensen for the lower bound (symmetric optimum), boundary inspection for the upper.

- *Jensen's Direction Confusion.* The function $f(x) = x^2$ is convex, so Jensen reads $f((a + b + c)/3) \le (f(a) + f(b) + f(c))/3$, i.e., $((a + b + c)/3)^2 \le (a^2 + b^2 + c^2)/3$. Multiplying by $3$: $(a + b + c)^2 / 3 \le a^2 + b^2 + c^2$, the *same* inequality as the Cauchy proof. (Jensen and Cauchy here give the same content; for general $p$, Jensen on $x^p$ recovers the power-mean inequality.) Confusing the direction of Jensen — applying it to a concave function and getting the wrong inequality — is a classic and easy slip.

**CONNECTIONS.**

*Primary archetype applications.* The same Cauchy-pattern controls (a) the *QM-AM inequality* $\sqrt{(x_1^2 + \cdots + x_n^2)/n} \ge (x_1 + \cdots + x_n)/n$, derived by the same Cauchy pairing with $(1, 1, \ldots, 1)$; (b) the *Cauchy-Schwarz integral form*, $(\int fg)^2 \le \int f^2 \cdot \int g^2$ (PP5), the continuous analogue obtained by the same WLOG-normalisation $\|f\|_2 = \|g\|_2 = 1$; (c) the *Engel / Titu lemma* $\sum a_i^2 / b_i \ge (\sum a_i)^2 / \sum b_i$, which is Cauchy-Schwarz after a rearrangement.

*Alternative solution archetypes.* Beyond Lagrange and Cauchy, the inequality admits a *Jensen* proof (cited above), an *AM-GM* proof on the squares $(a^2, b^2, c^2)$ combined with an algebraic identity, and a *direct expansion* proof using $(a - 1/3)^2 + (b - 1/3)^2 + (c - 1/3)^2 \ge 0$, which expands to $a^2 + b^2 + c^2 - 2(a + b + c)/3 + 1/3 \ge 0$ and uses the constraint. The Cauchy proof remains the shortest.

*Cross-domain manifestations.* The inequality $\sum x_i^2 \ge (\sum x_i)^2 / n$ is the statement that *the variance of a discrete distribution is non-negative*: writing $\mu = (\sum x_i)/n$, the difference $\sum x_i^2 / n - \mu^2$ is precisely the variance, which is $\ge 0$ with equality iff every $x_i$ equals $\mu$. The inequality is therefore the *positivity of variance* in probabilistic disguise. In *information theory*, the same Cauchy-pattern controls bounds on entropy and mutual information; in *machine learning*, the L2-norm bounds on weight vectors that prevent overfitting are descendants of the same inequality.

**TAKEAWAY.** *A homogeneous inequality is the same inequality after rescaling — fix the scale, and the constraint vanishes.*

---

### 4.3 Example 3 — Maximum of $\prod \cos \alpha_i$ on a Symmetric Diagonal

**Problem.** *Let $n \ge 1$ be a fixed integer and $\alpha_1, \alpha_2, \ldots, \alpha_n \in (0, \pi/2)$ satisfy*
\[
  \cot\alpha_1 \cdot \cot\alpha_2 \cdots \cot\alpha_n \;=\; 1.
\]
*Find the maximum value of $\cos\alpha_1 \cdot \cos\alpha_2 \cdots \cos\alpha_n$ and the configuration that attains it.* (JEE 2001; Joshi *EJM* Ch. 24, Exercise 24.27. The same problem will reappear as PP3 of Chapter 10 — *Inequality Constraints* — under a different framing.)

**SEED.** *Normalisation on the symmetric diagonal (Form III).* Both the constraint and the objective are symmetric in the $\alpha_i$'s. The natural candidate optimum is the symmetric-diagonal point $\alpha_1 = \cdots = \alpha_n$. The constraint then forces each $\alpha_i$ to satisfy $\cot^n \alpha_i = 1$, i.e., $\alpha_i = \pi/4$; AM-GM (or a slicker identity) then certifies that the diagonal is the maximum.

**BRUTE PATH.** Lagrange multipliers in $n$ variables. Maximise $f(\boldsymbol\alpha) = \prod_{i=1}^n \cos\alpha_i$ subject to $g(\boldsymbol\alpha) = \prod \cot\alpha_i - 1 = 0$. Taking $\partial / \partial \alpha_k$:
\[
  \frac{\partial f}{\partial \alpha_k} \;=\; -\sin\alpha_k \cdot \prod_{i \ne k} \cos\alpha_i \;=\; -\tan\alpha_k \cdot f.
\]
And $g + 1 = \prod \cot\alpha_i$, so $\log(g + 1) = \sum \log \cot\alpha_i$, and
\[
  \frac{\partial \log(g+1)}{\partial \alpha_k} \;=\; \frac{d}{d \alpha_k} \log\cot\alpha_k \;=\; \frac{-1}{\sin\alpha_k \cos\alpha_k} \;=\; \frac{-2}{\sin 2\alpha_k}.
\]
The Lagrange condition $\nabla f = \lambda \nabla g$ gives, after some manipulation, $\tan\alpha_k \cdot f = \mu / \sin 2\alpha_k$ for some constant $\mu$. Since $\tan\alpha / \sin 2\alpha = \tan\alpha / (2\sin\alpha\cos\alpha) = 1/(2\cos^2\alpha)$, the condition becomes $1/(2\cos^2\alpha_k) = \mu / f$ for every $k$, i.e., $\cos^2\alpha_k$ is the same for every $k$. Since $\alpha_k \in (0, \pi/2)$, this forces $\alpha_1 = \cdots = \alpha_n$. The constraint then forces $\cot\alpha = 1$, i.e., $\alpha = \pi/4$, and $f = (1/\sqrt 2)^n = 1/2^{n/2}$. The path *works*, but the $n$-variable Lagrange computation is heavy and obscures the algebraic structure.

**ELEGANT PIVOT.** Observe the constraint in its most informative form:
\[
  \cot\alpha_1 \cdots \cot\alpha_n \;=\; 1 \quad\Longleftrightarrow\quad \frac{\cos\alpha_1 \cdots \cos\alpha_n}{\sin\alpha_1 \cdots \sin\alpha_n} \;=\; 1 \quad\Longleftrightarrow\quad \prod_{i=1}^n \cos\alpha_i \;=\; \prod_{i=1}^n \sin\alpha_i.
\]
Write $P = \prod \cos\alpha_i = \prod \sin\alpha_i$ for the common value. Then
\[
  P^2 \;=\; \prod_{i=1}^n (\sin\alpha_i \cos\alpha_i) \;=\; \prod_{i=1}^n \frac{\sin 2\alpha_i}{2} \;=\; \frac{1}{2^n} \prod_{i=1}^n \sin 2\alpha_i.
\]
Since $\sin 2\alpha_i \le 1$ for every $i$ (with equality iff $2\alpha_i = \pi/2$, i.e., $\alpha_i = \pi/4$), we have $\prod \sin 2\alpha_i \le 1$, so
\[
  P^2 \;\le\; \frac{1}{2^n}, \qquad P \;\le\; \frac{1}{2^{n/2}}.
\]
Equality holds iff $\sin 2\alpha_i = 1$ for every $i$, i.e., $\alpha_i = \pi/4$ for every $i$. We verify the constraint at this point: $\cot(\pi/4) = 1$, so $\prod \cot(\pi/4) = 1^n = 1$. The constraint is satisfied, the maximum is attained, and
\[
  \boxed{\max \prod_{i=1}^n \cos\alpha_i \;=\; \frac{1}{2^{n/2}}, \text{ attained at } \alpha_1 = \alpha_2 = \cdots = \alpha_n = \pi/4.}
\]

The normalisation insight is the *symmetric-diagonal optimum*. Because both the constraint $\prod\cot\alpha_i = 1$ and the objective $\prod\cos\alpha_i$ are symmetric under permutation of the $\alpha_i$'s — and because the constraint set is connected and the objective continuous — the optimum, if unique, must lie on the *fixed-point locus* of the permutation action, which is the diagonal $\alpha_1 = \cdots = \alpha_n$. The $n$-variable problem reduces to a $1$-variable problem along the diagonal. The elegant pivot avoided Lagrange entirely by exploiting the diagonal structure from the outset: the trick $\cos\alpha\sin\alpha = (1/2)\sin 2\alpha$ converts the symmetric product into something to which AM-GM (or the elementary bound $\sin 2\alpha \le 1$) applies directly.

**PITFALLS.**

- *The Diagonal Fallacy.* For symmetric problems, the diagonal is the *natural candidate* — but it is not always the optimum. For example, maximising $\alpha_1^2 + \cdots + \alpha_n^2$ subject to $\alpha_1 + \cdots + \alpha_n = 1$ with $\alpha_i \ge 0$ attains its *maximum* at a boundary point ($\alpha_1 = 1$, others zero), not on the diagonal; the diagonal is the *minimum*. The trained solver checks the second variation or compares with boundary configurations. Here, $\alpha_i \in (0, \pi/2)$ is open, with no relevant boundary in the interior; the diagonal is the only critical point of the symmetric reduced problem; and the inequality $\sin 2\alpha \le 1$ certifies it as the maximum.

- *Treating the Constraint Independently for Each Variable.* The constraint $\prod \cot\alpha_i = 1$ is *coupled* — increasing $\alpha_i$ alone violates the constraint unless some other $\alpha_j$ decreases. A novice may try to maximise $\cos\alpha_i$ independently for each $i$ — pushing each $\alpha_i$ to $0$ — and then despair when the resulting configuration violates the constraint badly. The constraint must be respected throughout the maximisation; the elegant pivot does so by reformulating *both sides* of the constraint into the same product.

- *Forgetting to Verify the Constraint at the Optimum.* The bound $P \le 1/2^{n/2}$ requires only $\sin 2\alpha_i \le 1$; it does not by itself guarantee that the maximising point satisfies the constraint $\prod \cot\alpha_i = 1$. We checked separately that $\alpha_i = \pi/4$ for all $i$ satisfies the constraint. If it had not, the bound $1/2^{n/2}$ would have been a strict upper bound, not the maximum.

- *Missing the Identity $\sin\alpha \cos\alpha = (1/2) \sin 2\alpha$.* This double-angle identity is what converts the product $\sin\alpha \cos\alpha$ into a single bounded function. A student who does not see the identity will end up applying AM-GM crudely to $\sin\alpha_i \cos\alpha_i$ — which still gives a bound, but a *weaker* bound that does not match the optimum.

- *The Wrong $n$-Dependence.* The answer $1/2^{n/2}$ has a specific scaling in $n$: as $n$ grows, the maximum decreases exponentially. A student who reports $1/2$ (the answer for $n = 1$) or $1/\sqrt 2$ (the answer for $n = 2$) without checking the general formula has missed the $n$-dependence. Verifying small cases (the answer for $n = 1$ is indeed $1/\sqrt 2$, for $n = 2$ is $1/2$, for $n = 3$ is $1/2\sqrt 2$) catches this.

**CONNECTIONS.**

*Primary archetype applications.* The symmetric-diagonal argument controls (a) *AM-GM equality cases*: for any symmetric inequality $f(x_1, \ldots, x_n) \ge g(x_1, \ldots, x_n)$ with both sides invariant under permutation, equality holds on the diagonal $x_1 = \cdots = x_n$; (b) the *power-mean inequality* (PP6), with equality on the same diagonal; (c) *isoperimetric optima*, in which the regular $n$-gon maximises area for given perimeter (the maximally symmetric configuration is optimal).

*Alternative solution archetypes.* The same maximum can be obtained by *AM-GM directly* on the $\sin 2\alpha_i$'s: $\prod \sin 2\alpha_i \le \left(\frac{\sum \sin 2\alpha_i}{n}\right)^n$, with the constraint imposed via Lagrange or via a parametrisation. A more sophisticated approach uses *Jensen* on $\log\cos$ and $\log\sin$ jointly. The elegance of the pivot above is that it bypasses these by reducing the problem to a *pointwise* bound $\sin 2\alpha \le 1$, after the constraint has been used to identify the product structure.

*Cross-domain manifestations.* The *isothermal-isobaric* maximum-entropy distribution in statistical mechanics, when the underlying state space is permutation-symmetric, is the *uniform* distribution — the symmetric-diagonal in disguise. The *Nash equilibrium* of a symmetric game, when unique, is a symmetric profile in which every player adopts the same strategy. The general principle, in every domain: *when constraint and objective share a permutation symmetry, the optimum (if unique) sits on the symmetric diagonal*. Normalisation is the move that exploits this.

**TAKEAWAY.** *When constraint and objective share a symmetry group, the optimum sits on the symmetric diagonal.*

---

## 5. Practice Problems

Seven problems, statements only; full solutions appear in the Appendix. The slate spans Tier 1 (JEE Mains–level recognition) through Tier 3 (JEE Advanced and Olympiad register).

### 5.1 Minimum of $a^2 + b^2$ Subject to $a + b = 6$ (Joshi Ch. 6 / standard JEE Mains)

For positive reals $a, b$ with $a + b = 6$, find the minimum value of $a^2 + b^2$.

### 5.2 Homogeneous AM-GM: $(a + b + c)^3 \ge 27 abc$ (Joshi Ch. 6, Comment 4)

Prove that for all positive reals $a, b, c$,
\[
  (a + b + c)^3 \;\ge\; 27\, abc,
\]
with equality if and only if $a = b = c$. Identify the scaling invariance that makes the WLOG-normalisation $a + b + c = 1$ free, and complete the proof in the normalised setting.

### 5.3 Maximum of $x + y + z$ on a Sphere (JEE Mains-style; Joshi Ch. 6)

For real $x, y, z$ satisfying $x^2 + y^2 + z^2 = 9$, find the maximum value of $x + y + z$ and the point at which it is attained.

### 5.4 The QM-AM Inequality via Jensen (Joshi Ch. 6, Comment 5)

For positive reals $x_1, x_2, \ldots, x_n$, prove
\[
  \sqrt{\frac{x_1^2 + x_2^2 + \cdots + x_n^2}{n}} \;\ge\; \frac{x_1 + x_2 + \cdots + x_n}{n},
\]
with equality if and only if $x_1 = x_2 = \cdots = x_n$. Identify the normalisation that reduces the proof to a one-line application of either Jensen's inequality (on the convex function $f(x) = x^2$) or Cauchy-Schwarz.

### 5.5 The Cauchy-Schwarz Inequality for Integrals (Joshi Ch. 6, Comment 7)

For continuous functions $f, g : [0, 1] \to \mathbb{R}$, prove
\[
  \left( \int_0^1 f(x)\, g(x)\, dx \right)^2 \;\le\; \int_0^1 f(x)^2\, dx \cdot \int_0^1 g(x)^2\, dx.
\]
Use the normalisation $\int_0^1 f^2 = \int_0^1 g^2 = 1$ to reduce to a one-line proof.

### 5.6 The Power-Mean Inequality (Joshi Ch. 6, Comment 11)

For positive reals $x_1, x_2, \ldots, x_n$ and a non-zero real $r$, define
\[
  M_r(x_1, \ldots, x_n) \;=\; \left( \frac{1}{n} \sum_{i=1}^n x_i^r \right)^{1/r}.
\]
Prove that for any non-zero reals $p < q$,
\[
  M_p(x_1, \ldots, x_n) \;\le\; M_q(x_1, \ldots, x_n),
\]
with equality if and only if $x_1 = x_2 = \cdots = x_n$. The probability-measure normalisation $\sum (1/n) = 1$ on the weights is the key.

### 5.7 Chebyshev's Sum Inequality (Joshi Ch. 6, Comment 12)

Let $a_1 \le a_2 \le \cdots \le a_n$ and $b_1 \le b_2 \le \cdots \le b_n$ be similarly ordered sequences of real numbers. Prove
\[
  n \sum_{i=1}^n a_i b_i \;\ge\; \left( \sum_{i=1}^n a_i \right) \left( \sum_{i=1}^n b_i \right).
\]
Identify the normalisation (centring each sequence by its mean) that, while not strictly necessary, makes the algebraic identity transparent.

---

## 6. The Connections Web

Normalisation does not act in isolation. It connects to virtually every later archetype in the book and to almost every quantitative discipline.

### 6.1 Normalisation Across Mathematical Domains

*Algebra.* Every homogeneous polynomial inequality admits a scale-fixing normalisation. The standard moves are $\sum x_i = 1$ (when the constraint set is the simplex), $\sum x_i^2 = 1$ (when the constraint set is the unit sphere), $\prod x_i = 1$ (when the constraint set is the level surface of the geometric mean), and $\max_i x_i = 1$ (when the constraint set is the unit ball in the $\ell^\infty$ norm). Each choice picks a different *gauge* and may make different algebraic manipulations easier. The trained solver tries the most convenient first.

*Geometry.* Every angle-and-ratio statement about triangles, circles, and polygons is *scale-invariant* — multiplying every length by a constant changes nothing. The standard normalisations are circumradius $R = 1$, inradius $r = 1$, longest side $= 1$, or perimeter $= 1$. The Ravi substitution $a = y + z$, $b = z + x$, $c = x + y$ from Chapter 5 is, in this light, a normalisation that fixes a particular parametrisation of the triangle-side cone. Projective geometry takes the move to its limit: every projective property is invariant under rescaling of homogeneous coordinates, and the natural representative of each projective class is the one with last coordinate $= 1$ (when the point is finite) — yielding affine coordinates from projective ones.

*Linear algebra.* The matrix $A$ and its scalar multiple $\lambda A$ have the same eigenvectors (with eigenvalues scaled by $\lambda$). When one is interested only in eigenvectors — the direction in which the matrix acts as scalar multiplication — the natural normalisation is $\|v\| = 1$, choosing a unit-length representative of each eigenvector's scaling orbit. The singular-value decomposition extends this: every matrix admits orthonormal bases for input and output spaces in which the matrix is diagonal, and the diagonal entries (the *singular values*) are scale-invariant features of the matrix.

*Analysis.* The integral $\int f$ over a probability measure ($\int dP = 1$) is the natural normalisation in probability theory; the same integral over an arbitrary measure differs only by an overall scaling, and probability is precisely the normalised case. Every probability density is normalised so that $\int p\, dx = 1$; every conditional probability inherits a normalised denominator. The convergence theorems of measure theory all become cleaner in the probability-normalised setting.

### 6.2 Normalisation in Physics and Other Sciences

*Classical mechanics.* Beyond the pendulum (WE1), dimensional analysis controls the period of the spring oscillator ($T = 2\pi\sqrt{m/k}$), the orbital period (Kepler's third law $T^2 = 4\pi^2 R^3 / GM$), and the drag forces on objects in fluids (Stokes for low Reynolds, quadratic for high). In every case, dimensions force the algebraic form; physics supplies one constant.

*Fluid dynamics.* The dimensionless groups — Reynolds, Mach, Froude, Strouhal, Péclet, Prandtl — are the *classification scheme* of fluid flow. At a given combination of these numbers, the flow patterns are universal; the *Strouhal number for vortex shedding around a cylinder is $0.2$* whether the cylinder is a violin string at $440\,\text{Hz}$ or an oil-rig spar in a hundred-knot wind. The universality is dimensional analysis at work.

*Quantum mechanics.* In natural units ($\hbar = c = 1$), the Schrödinger equation $i \partial_t \psi = H \psi$ has no explicit dimensional constants; energy, momentum, and time are all measured in the same unit (inverse length, by convention). The Compton wavelength $\lambda_C = 1/m$ for a particle of mass $m$ is the natural length scale below which relativistic effects dominate. The de-Broglie wavelength $\lambda_{dB} = 1/p$ for momentum $p$ is the natural length below which quantum effects dominate. Both lengths arise from dimensional normalisation of the fundamental equations.

*Statistical mechanics.* In units where $k_B = 1$, the Boltzmann factor $e^{-E/T}$ has both $E$ and $T$ in the same dimension (energy). The thermal de-Broglie wavelength, the Debye temperature, and the Fermi energy are all *normalised* quantities, each defined to make a specific dimensionless ratio equal to $1$. The phase diagram of every condensed-matter system is parametrised by dimensionless ratios; the *critical exponents* of phase transitions are the universal numbers that survive after the dimensionful parameters have been scaled out.

### 6.3 Cross-Domain Manifestations

The reach extends beyond physics.

*Economics.* Real (deflated) quantities are normalised nominal quantities; the deflator is chosen so that the normalised quantity in a base year equals $1$. Purchasing-power-parity exchange rates are normalised market exchange rates; the basket-of-goods is the normalisation. The price-to-earnings ratio in finance is a normalised price, scaled by the firm's earnings — the resulting dimensionless ratio is comparable across firms of very different size.

*Statistics.* The z-score $(x - \mu)/\sigma$ normalises a random variable to have mean $0$ and variance $1$. The standardised test statistic in hypothesis testing — Student's $t$, the chi-squared, the $F$-statistic — is in every case a normalisation of a raw quantity by an estimated dispersion; the normalisation is what makes the test universal across scales of the underlying data. Bayesian normalisation — dividing the joint density by the marginal — produces the posterior. The act of normalisation pervades the subject.

*Computer science and machine learning.* Feature scaling — subtracting the mean and dividing by the standard deviation — is preprocessing for nearly every machine-learning algorithm. The *batch normalisation* and *layer normalisation* operations in deep neural networks normalise activations across a layer at training time, dramatically improving convergence. The *gradient normalisation* in optimisation prevents one direction from dominating updates. In every case, the algorithm is invariant under rescaling of its inputs only after explicit normalisation; without it, the optimisation diverges or stalls.

*Music and signal processing.* The decibel scale is a logarithmic normalisation of acoustic intensity. The musical pitch interval (the *cent*, $2^{1/1200}$) is the logarithmic normalisation that makes pitch ratios additive across octaves. The discrete Fourier transform of a sampled signal is conventionally normalised so that the inverse transform recovers the original — the normalisation factor (commonly $1/N$ or $1/\sqrt N$) is a convention but a crucial one.

### 6.4 Related Archetypes

Normalisation interacts with five other archetypes in particularly tight ways.

- **Archetype 2 (Symmetry).** Every normalisation is, at root, the recognition of a symmetry — the group $G$ under which the problem is invariant. Symmetry tells the solver that the answer has a certain form; Normalisation tells her to *quotient by the symmetry* and work on the smaller problem. The two archetypes are sibling moves: Symmetry constrains the answer's shape, Normalisation reduces the problem's dimension.

- **Archetype 5 (Substitution).** Many normalisations are implemented *as* substitutions. The substitution $a = x/(\sum x_i)$ for inequalities, $\alpha = \theta/(\theta_0)$ for the pendulum amplitude, $\tilde x = (x - \mu)/\sigma$ for z-score normalisation — each is a substitution that fixes the normalisation. Substitution is the *operational mechanism*; Normalisation is the *strategic reason*.

- **Archetype 6 (Linearisation).** Linearisation and normalisation often combine: the pendulum problem (WE1) requires both. Linearisation produces the equation $\ddot\theta + \omega^2\theta = 0$; normalisation produces the dimensional form $T = c\sqrt{L/g}$; together they yield $T = 2\pi\sqrt{L/g}$. In perturbation theory generally, the dimensionless small parameter is identified by normalisation, and the expansion is the linearisation in that parameter.

- **Archetype 10 (Inequality Constraints).** Almost every homogeneous inequality in Chapter 10 will be approached by first normalising — fixing the scale, then applying Cauchy, AM-GM, Jensen, or rearrangement. The cross-archetype reuse of WE3 (the JEE 2001 cos-product problem) between Chapter 7 (here, framed as symmetric-diagonal normalisation) and Chapter 10 (where it will reappear framed as a Lagrange-AM-GM exercise) is a deliberate illustration of how the two archetypes overlap on the same concrete problem.

- **Archetype 12 (Extremal Principles).** Symmetric-diagonal normalisation (Form III) is the most common *extremal-principle* heuristic in competition mathematics: *the maximum (or minimum) of a symmetric function under a symmetric constraint is attained on the symmetric diagonal*. This is the principle behind virtually every "find the maximum of $\sum x_i^k$ given $\sum x_i = c$" problem.

- **Archetype 17 (Degrees of Freedom Analysis).** Buckingham-$\pi$ is the prototypical *degrees-of-freedom* argument: count variables, subtract dimensions, get the count of effective unknowns. Chapter 17 will systematise this kind of counting across mathematics (Galois theory for solvability, the rank-nullity theorem for linear systems, the dimension of moduli space). Normalisation is the first place the reader meets the move; Chapter 17 is where the move becomes a chapter-length method.

---

## 7. Master Takeaways

Seven sentences. Each one is a complete operational principle; each one is meant to be quoted, internalised, and re-deployed.

1. *Normalisation strips a problem of every degree of freedom that does not matter; what remains is the structure that does.* (The canonical takeaway.)

2. *If the problem is homogeneous, the constraint $\sum x_i = 1$ is free.* (Form I.)

3. *Units constrain the form of the answer; physics constrains only the constant.* (WE1 takeaway, generalised; Form II.)

4. *When constraint and objective share a symmetry group, the optimum sits on the symmetric diagonal.* (WE3 takeaway; Form III.)

5. *Every geometric statement about angles and ratios is a statement on the projective simplex; fix one length, the rest are dimensionless.* (Form IV.)

6. *The dimensionless form of an equation is the form that generalises; the dimensioned form is the form of one experiment.*

7. *Before any algebra, ask: is there a scaling, a dimensional, or a permutation invariance? If yes, normalise first; the smaller problem is the real problem.*

---

## 8. Self-Assessment Checklist

You have absorbed Chapter 7 when, without re-opening it, you can do each of the following from memory.

- [ ] State the formal definition of normalisation in terms of a group action on a problem.
- [ ] State Euler's homogeneity identity and use it to justify the move "WLOG $\sum x_i = 1$" for any inequality homogeneous in its variables.
- [ ] State the Buckingham-$\pi$ theorem and apply it to derive the form of the pendulum period $T = c\sqrt{L/g}$.
- [ ] Identify the four forms of normalisation (constraint, dimensional, symmetric-diagonal, geometric scale-fixing) and a one-line diagnostic for each.
- [ ] Name and explain three of the five common pitfalls: the Fool's Scaling, the Vanishing Dimension, the Diagonal Fallacy, the Constraint-Forgetting Sin, the Dimensional Coincidence.
- [ ] Derive the Cauchy-Schwarz bound $a^2 + b^2 + c^2 \ge 1/3$ subject to $a + b + c = 1$ in two lines, and state the equality case.
- [ ] Derive the JEE 2001 cos-product maximum $1/2^{n/2}$ using the symmetric-diagonal argument, without invoking Lagrange.
- [ ] State the QM-AM inequality, the power-mean inequality, and Chebyshev's sum inequality, and identify the normalisation that simplifies the proof of each.
- [ ] Cite at least three cross-domain applications of dimensional analysis (Reynolds number, Mach number, Strouhal number, etc.) and explain why the universal value of the dimensionless group is meaningful.
- [ ] Articulate, in one sentence, how Normalisation differs from Symmetry (Archetype 2) — namely, Symmetry constrains the answer's form, Normalisation reduces the problem's dimension.

---

## Bridge to Chapter 8: Domain Translation

We end with a transition. Normalisation was the move *within* a chosen problem domain — given a problem stated in certain variables, reduce the number of effective variables by quotienting out a scaling, a dimension, or a permutation. We did not change the language of the problem; we only stripped its redundancies.

Chapter 8 — *Domain Translation* — takes the next step. Many problems are stated in one mathematical language but become transparent in another. A geometry problem solved by complex numbers; a real-analysis problem solved by going to $\mathbb{C}$; a combinatorics problem solved by generating functions; a differential equation solved by transforming to the frequency domain via Fourier. In each, the move is the same: *recognise that the language in which the problem was stated is not the language in which its structure is most visible, translate to the natural language, solve, translate back*. Where Normalisation reduced the problem within a fixed language, Domain Translation changes the language. The two archetypes complete the *Method Selection* sub-pillar: between them, they cover the cognitive moves of (a) *fixing irrelevant freedom* (Normalisation) and (b) *changing the descriptive frame* (Translation). With Chapter 8 in hand, the reader will have all four Method Selection archetypes — Substitution, Linearisation, Normalisation, Translation — and the toolkit for the third major sub-pillar, *Constraint Exploitation*, will be ready to open.

---

## Appendix — Solutions to Practice Problems

### Solution to 5.1 — Minimum of $a^2 + b^2$ Subject to $a + b = 6$

*Setting up.* The constraint $a + b = 6$ allows us to write $b = 6 - a$. Substituting,
\[
  f(a) \;=\; a^2 + (6 - a)^2 \;=\; 2a^2 - 12a + 36.
\]
This is a quadratic in $a$, opening upward; the minimum is at $a = -(-12)/(2 \cdot 2) = 3$, giving $b = 3$ and $f(3) = 2(9) - 36 + 36 = 18$.

*The normalisation reading.* Write $a = 3 + t$, $b = 3 - t$ — a *centred* parametrisation that normalises the constraint. Then $a^2 + b^2 = (3+t)^2 + (3-t)^2 = 18 + 2t^2$, which is manifestly minimised at $t = 0$ with value $18$. The centring is the normalisation: by translating to the mean, the constraint $a + b = 6$ becomes the trivial $0 + 0 = 0$ (in the centred variables), and the objective decouples into a single-variable quadratic.

*Alternative via QM-AM.* The quadratic mean of $a, b$ is $\sqrt{(a^2 + b^2)/2}$; the arithmetic mean is $(a + b)/2 = 3$. By QM $\ge$ AM, $\sqrt{(a^2 + b^2)/2} \ge 3$, so $a^2 + b^2 \ge 18$, with equality iff $a = b = 3$. The QM-AM proof is the same as the centring proof, in slightly more general language.

\[
  \boxed{\min(a^2 + b^2) \;=\; 18, \text{ attained at } a = b = 3.}
\]

---

### Solution to 5.2 — Homogeneous AM-GM: $(a + b + c)^3 \ge 27\, abc$

*The normalisation.* The inequality is homogeneous of degree $3$ in $(a, b, c)$: rescaling $(a, b, c) \mapsto (\lambda a, \lambda b, \lambda c)$ multiplies both sides by $\lambda^3$. Therefore the inequality is equivalent to its scale-invariant form,
\[
  \frac{(a + b + c)^3}{27\, abc} \;\ge\; 1,
\]
and we may WLOG normalise $a + b + c = 1$. The problem becomes: prove that for $a + b + c = 1$ with $a, b, c > 0$, $abc \le 1/27$.

*The AM-GM step.* By AM-GM on the three positive numbers $a, b, c$,
\[
  \frac{a + b + c}{3} \;\ge\; \sqrt[3]{abc}.
\]
Substituting $a + b + c = 1$: $1/3 \ge \sqrt[3]{abc}$, i.e., $abc \le 1/27$. Equality in AM-GM holds iff $a = b = c$, which combined with the constraint gives $a = b = c = 1/3$.

*Recovering the unnormalised result.* The inequality $abc \le 1/27$ in the normalised setting becomes, after re-multiplying by $(a + b + c)^3$:
\[
  abc \;\le\; \frac{(a + b + c)^3}{27}, \quad \text{i.e.,} \quad (a + b + c)^3 \;\ge\; 27\, abc.
\]
Equality holds iff $a = b = c$. \hfill$\blacksquare$

---

### Solution to 5.3 — Maximum of $x + y + z$ on a Sphere

*By Cauchy-Schwarz.* Apply the inequality $(\sum u_i v_i)^2 \le (\sum u_i^2)(\sum v_i^2)$ with $u_i = (x, y, z)$ and $v_i = (1, 1, 1)$:
\[
  (x + y + z)^2 \;\le\; (x^2 + y^2 + z^2)(1^2 + 1^2 + 1^2) \;=\; 9 \cdot 3 \;=\; 27.
\]
So $x + y + z \le \sqrt{27} = 3\sqrt 3$. Equality holds iff $(x, y, z) \propto (1, 1, 1)$, i.e., $x = y = z$. The constraint then forces $3x^2 = 9$, so $x = y = z = \sqrt 3$ (taking the positive root for the maximum).

*By symmetric-diagonal normalisation.* The objective $x + y + z$ and the constraint $x^2 + y^2 + z^2 = 9$ are both symmetric under permutation of $(x, y, z)$. The natural candidate maximum is the symmetric-diagonal point $x = y = z$; the constraint forces $x = \sqrt 3$, the objective evaluates to $3\sqrt 3$. (The Cauchy-Schwarz argument above certifies that this is the maximum, not merely a critical point.)

*Normalisation by sphere-radius.* The unit-sphere version of the problem — maximise $x + y + z$ subject to $x^2 + y^2 + z^2 = 1$ — has answer $\sqrt 3$, attained at $x = y = z = 1/\sqrt 3$. Rescaling by the radius $R = 3$ multiplies both the constraint and the linear functional by $R$, giving the present answer $\sqrt 3 \cdot 3 = 3\sqrt 3$.

\[
  \boxed{\max(x + y + z) \;=\; 3\sqrt 3, \text{ attained at } x = y = z = \sqrt 3.}
\]

---

### Solution to 5.4 — The QM-AM Inequality

*Statement.* For positive reals $x_1, \ldots, x_n$,
\[
  \sqrt{\frac{x_1^2 + \cdots + x_n^2}{n}} \;\ge\; \frac{x_1 + \cdots + x_n}{n}.
\]

*Squaring.* It suffices to prove the equivalent (and non-negative-both-sides) inequality
\[
  n \sum_{i=1}^n x_i^2 \;\ge\; \left( \sum_{i=1}^n x_i \right)^2.
\]

*Proof by Cauchy-Schwarz.* Apply with vectors $(x_1, \ldots, x_n)$ and $(1, 1, \ldots, 1)$:
\[
  \left( \sum_i x_i \cdot 1 \right)^2 \;\le\; \left( \sum_i x_i^2 \right) \left( \sum_i 1^2 \right) \;=\; n \sum_i x_i^2.
\]
Equality holds iff the vectors are proportional, i.e., $x_1 = x_2 = \cdots = x_n$.

*Proof by Jensen.* The function $f(x) = x^2$ is convex. By Jensen with weights $1/n$,
\[
  f\!\left( \frac{1}{n} \sum_i x_i \right) \;\le\; \frac{1}{n} \sum_i f(x_i),
\]
i.e.,
\[
  \left( \frac{\sum x_i}{n} \right)^2 \;\le\; \frac{\sum x_i^2}{n},
\]
which rearranges to the desired inequality. Equality in Jensen holds iff all $x_i$ are equal.

*The normalisation reading.* In *probabilistic* form, write $X$ for a random variable taking values $x_1, \ldots, x_n$ each with probability $1/n$. Then $\mathbb{E}[X] = (\sum x_i)/n$ and $\mathbb{E}[X^2] = (\sum x_i^2)/n$. The inequality reads $\mathbb{E}[X^2] \ge (\mathbb{E}[X])^2$, i.e., $\text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 \ge 0$. The normalisation $\sum (1/n) = 1$ on the weights turns the inequality into the *non-negativity of variance*, with equality iff the variable is constant ($x_1 = \cdots = x_n$). \hfill$\blacksquare$

---

### Solution to 5.5 — Cauchy-Schwarz for Integrals

*The normalisation.* Define $A^2 := \int_0^1 f^2$ and $B^2 := \int_0^1 g^2$. If either is zero (say $A = 0$), then $f \equiv 0$ almost everywhere, and both sides of the inequality are zero. Assume $A, B > 0$. Replace $f$ by $\tilde f := f / A$ and $g$ by $\tilde g := g / B$. Then $\int \tilde f^2 = \int \tilde g^2 = 1$, and the original inequality
\[
  \left( \int fg \right)^2 \;\le\; \int f^2 \cdot \int g^2 \;=\; A^2 B^2
\]
is equivalent (after dividing both sides by $A^2 B^2$) to
\[
  \left( \int \tilde f \tilde g \right)^2 \;\le\; 1, \qquad \text{i.e.,} \qquad \left| \int \tilde f \tilde g \right| \;\le\; 1.
\]

*The one-line proof.* For the normalised pair $(\tilde f, \tilde g)$,
\[
  0 \;\le\; \int_0^1 (\tilde f - \tilde g)^2 \, dx \;=\; \int_0^1 \tilde f^2 \;-\; 2 \int_0^1 \tilde f \tilde g \;+\; \int_0^1 \tilde g^2 \;=\; 1 - 2 \int_0^1 \tilde f \tilde g + 1.
\]
Hence $\int \tilde f \tilde g \le 1$. Applying the same argument with $\tilde f$ replaced by $-\tilde f$ gives $\int (-\tilde f) \tilde g \le 1$, i.e., $\int \tilde f \tilde g \ge -1$. Combining, $|\int \tilde f \tilde g| \le 1$, and squaring (and inverting the normalisation) yields
\[
  \left( \int_0^1 f g \right)^2 \;\le\; \int_0^1 f^2 \cdot \int_0^1 g^2.
\]
Equality holds iff $\tilde f = \pm \tilde g$ pointwise, i.e., iff $f$ and $g$ are linearly dependent. \hfill$\blacksquare$

*Remark.* The same proof works in any inner-product space: the move is *normalise the vectors to unit length, then $|\langle u, v \rangle| \le 1$ by expanding $\|u - v\|^2 \ge 0$*. The structure is universal; the integral case is one instance.

---

### Solution to 5.6 — The Power-Mean Inequality

*Statement.* For positive reals $x_1, \ldots, x_n$ and non-zero $p < q$, $M_p \le M_q$ where $M_r = ((1/n) \sum_i x_i^r)^{1/r}$, with equality iff all $x_i$ are equal.

*The normalisation.* The weights $w_i = 1/n$ satisfy $\sum w_i = 1$, so $(w_1, \ldots, w_n)$ is a probability distribution. The power mean is then $M_r = (\sum w_i x_i^r)^{1/r}$, which is the $L^r$-norm of $x$ under the probability measure $w$.

*Case $0 < p < q$.* The function $\varphi(t) = t^{q/p}$ is convex on $t > 0$ (since $q/p > 1$). Jensen's inequality applied to $\varphi$ with weights $w_i$ and values $y_i := x_i^p$ gives
\[
  \varphi\!\left( \sum_i w_i y_i \right) \;\le\; \sum_i w_i \varphi(y_i),
\]
i.e.,
\[
  \left( \sum_i w_i x_i^p \right)^{q/p} \;\le\; \sum_i w_i x_i^q.
\]
Taking the $(1/q)$-th power of both sides (the function $t \mapsto t^{1/q}$ is monotone-increasing for $q > 0$),
\[
  \left( \sum_i w_i x_i^p \right)^{1/p} \;\le\; \left( \sum_i w_i x_i^q \right)^{1/q},
\]
i.e., $M_p \le M_q$. Equality in Jensen holds iff $y_1 = \cdots = y_n$, i.e., $x_1 = \cdots = x_n$.

*Case $p < q < 0$.* Both $p$ and $q$ are negative; $q/p \in (0, 1)$ (since dividing two negatives, with the smaller in absolute value on top). The function $\varphi(t) = t^{q/p}$ is *concave* on $t > 0$ now; Jensen's direction reverses; but the $(1/q)$-th power involves $q < 0$, which is order-reversing; the two reversals cancel and the conclusion $M_p \le M_q$ stands. (A direct argument: replace $x_i$ by $1/x_i$ throughout to reduce to the previous case.)

*Case $p < 0 < q$.* Combine the previous cases through the intermediary $M_0$, the geometric mean, by continuous limits as $r \to 0$.

*Equality.* In every case, equality holds iff all the $x_i$ are equal, since this is the equality condition in the Jensen step.

The probability-measure normalisation is what turns the power mean into an $L^r$-norm, in turn making the Jensen-on-$\varphi(t) = t^{q/p}$ argument geometric: it says *the $L^q$-norm dominates the $L^p$-norm on a probability space when $q \ge p$*. \hfill$\blacksquare$

---

### Solution to 5.7 — Chebyshev's Sum Inequality

*Statement.* For $a_1 \le \cdots \le a_n$ and $b_1 \le \cdots \le b_n$ (similarly ordered), $n \sum a_i b_i \ge (\sum a_i)(\sum b_i)$.

*The identity.* For all $i, j \in \{1, \ldots, n\}$, the sequences are similarly ordered, so $(a_i - a_j)$ and $(b_i - b_j)$ have the same sign — both non-negative when $i \ge j$, both non-positive when $i \le j$. In either case, $(a_i - a_j)(b_i - b_j) \ge 0$. Summing over all pairs:
\[
  \sum_{i = 1}^n \sum_{j = 1}^n (a_i - a_j)(b_i - b_j) \;\ge\; 0.
\]

*Expanding the double sum.* Distribute:
\[
  \sum_{i, j} (a_i b_i - a_i b_j - a_j b_i + a_j b_j) \;=\; \sum_{i, j} a_i b_i \;-\; \sum_{i, j} a_i b_j \;-\; \sum_{i, j} a_j b_i \;+\; \sum_{i, j} a_j b_j.
\]
The first and fourth terms are each $n \sum_i a_i b_i$ (the index of summation can be relabelled). The second and third terms are each $(\sum_i a_i)(\sum_j b_j)$ (by separation of variables). Hence
\[
  2 n \sum_i a_i b_i \;-\; 2 \left( \sum_i a_i \right) \left( \sum_i b_i \right) \;\ge\; 0,
\]
which yields the desired inequality.

*The normalisation reading.* Substituting $a_i \mapsto a_i - \bar a$ and $b_i \mapsto b_i - \bar b$ (where $\bar a, \bar b$ are the means) preserves the *similarly-ordered* property and reduces the inequality, after some algebra, to $\sum_i (a_i - \bar a)(b_i - \bar b) \ge 0$. This is the *covariance* of the two centred sequences with respect to the uniform discrete distribution, and the inequality states that *similarly ordered random variables have non-negative covariance* — a special case of the FKG inequality in correlation theory. The centring normalisation, while not strictly needed for the proof, exposes the probabilistic content. \hfill$\blacksquare$

*Equality.* Holds iff $(a_i - a_j)(b_i - b_j) = 0$ for every pair, i.e., iff at least one of the sequences is constant.

---

*End of Chapter 7.*

