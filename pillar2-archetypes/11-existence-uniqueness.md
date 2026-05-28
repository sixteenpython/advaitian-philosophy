---
chapter: 11
archetype: Existence / Uniqueness Conditions
subtitle: "Existence Precedes Computation"
category: Constraint Exploitation (Archetypes 9–12) — third chapter
related_archetypes: [1, 9, 10, 12, 18]
key_gems:
  - "Intermediate Value Theorem (IVT): if $f$ is continuous on $[a, b]$ and $f(a) \\cdot f(b) < 0$, then $\\exists\\, c \\in (a, b)$ with $f(c) = 0$"
  - "Mean Value Theorem (MVT): if $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, then $\\exists\\, c \\in (a, b)$ with $f'(c) = \\dfrac{f(b) - f(a)}{b - a}$"
  - "Rolle's Theorem: MVT special case for $f(a) = f(b)$, giving $f'(c) = 0$ for some $c \\in (a, b)$"
  - "Brouwer's 1-dim fixed-point theorem: every continuous $f : [a, b] \\to [a, b]$ has a fixed point (proved by IVT applied to $g(x) = f(x) - x$)"
  - "Banach's contraction-mapping theorem: every contraction $f : X \\to X$ on a complete metric space $X$ has a unique fixed point; iteration $x_{n+1} = f(x_n)$ from any seed converges to it geometrically"
  - "Maximum Principle for ODEs: solutions of $f'' + g f' - f = 0$ on $[a, b]$ with $f \\ge 0$ on the boundary cannot attain a positive interior maximum"
  - "Cauchy's functional equation theorem: every continuous $f : \\mathbb R \\to \\mathbb R$ satisfying $f(x + y) = f(x) + f(y)$ is linear: $f(x) = c\\,x$ for some $c = f(1)$"
  - "Rolle-iteration corollary: a real polynomial of degree $n$ with $n$ distinct real roots has a derivative with exactly $n - 1$ distinct real roots, all in the convex hull of the original roots"
  - "Odd-degree-polynomial existence: every polynomial of odd degree with real coefficients has at least one real root (IVT applied at $\\pm\\infty$)"
  - "Existence-then-uniqueness pattern: many problems split into a separate existence proof (constructive or non-constructive) and a separate uniqueness proof (typically by contradiction or by a contraction / convexity argument)"
canonical_takeaway: "Prove it exists before you find it. Existence and uniqueness are separable questions; many problems ask only one of the two."
status: draft
last_revised: 2026-05-28
sourcing_note: "All worked examples and practice problems in this chapter are drawn from K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), or from JEE / RMO / INMO examinations commented on in that text. See Blueprint §6.2 for the sourcing rule and `pillar2-archetypes/_template/joshi-problems-locked.md` §Ch. 11 for the locked slate. **Verification audit for this chapter discovered one slate error**: PP1 (JEE 2001 non-differentiability of $\\max\\{x, x^3\\}$) listed two non-differentiability points ($x = -1, 0$), but the correct count is **three** — the curves cross at $x = -1, 0, 1$ and at every crossing the active-branch slopes differ. Patched in slate v0.2.8; see PP1 in the appendix for the corrected derivation. **Terminology note for WE3**: the locked slate names the 1-dim Brouwer fixed-point theorem (every continuous $f : [a, b] \\to [a, b]$ has a fixed point, proved by IVT) as 'Banach', but Banach's contraction-mapping theorem is a strictly stronger statement requiring contraction (not just continuity); the chapter uses the correct names — Brouwer / IVT-route for WE3, Banach / contraction-route for PP7."
---

# Chapter 11 — Existence / Uniqueness Conditions

## *Existence Precedes Computation*

---

## Opening Vignette

An aerospace engineer at the Indian Space Research Organisation in Bengaluru is certifying the parachute deployment system for the next-generation crew-recovery capsule. The capsule re-enters the atmosphere at hypersonic speed, decelerates through the upper atmosphere by aerodynamic drag, and at a precisely specified altitude — between $7.0$ and $7.5\,\text{km}$ above sea level — must release its drogue parachute. The release is triggered by an onboard barometric-pressure sensor: when the sensor reading falls below a calibrated threshold $P_t$ (corresponding to the $7.5\,\text{km}$ altitude in the standard atmosphere model), a pyrotechnic charge fires and the drogue deploys. The engineer's task is not to compute *exactly when* the deployment fires (the precise altitude varies with atmospheric conditions on the day of the flight); her task is to *certify the existence of a deployment moment* within the safe altitude band for every admissible atmospheric profile. Her certification argument is structurally an intermediate-value theorem: at the upper end of the band ($7.5\,\text{km}$), the sensor reading $P(t_1)$ exceeds $P_t$ (parachute not yet armed); at the lower end ($7.0\,\text{km}$), $P(t_2)$ is below $P_t$ (parachute *must* deploy by now, or the mission fails); the pressure $P(t)$ is a *continuous* function of time during atmospheric descent. By IVT, *there exists* a time $t^* \in (t_1, t_2)$ at which $P(t^*) = P_t$ — the deployment moment. The certifier does not need to know what $t^*$ is for any particular flight; she needs to know it *exists*. The IVT argument is the certification, and the certificate is *existence, not value*.

Now turn to a second scene. A nuclear engineer at the Bhabha Atomic Research Centre is simulating the coolant-flow temperature distribution inside a pressurised heavy-water reactor. The flow is governed by an elliptic partial differential equation (a Laplacian plus a source term from the reactor's fission profile) with boundary conditions specifying the inlet and outlet temperatures of the coolant loops. The engineer runs the simulation; it converges to a temperature field $T(\mathbf r)$ that looks plausible and satisfies the PDE. But before reporting the result, she invokes the *maximum principle for elliptic PDEs*: a solution of the equation $\nabla^2 T + s(\mathbf r) = 0$ (with $s$ a known fission-source distribution) on a bounded domain $\Omega$ is *uniquely determined* by its boundary values on $\partial\Omega$, provided the source term and the boundary data are compatible. The maximum principle says: if two solutions $T_1, T_2$ agreed on the boundary, then their difference $w = T_1 - T_2$ satisfies $\nabla^2 w = 0$ on $\Omega$ with $w = 0$ on $\partial\Omega$, and by the maximum principle for harmonic functions, $w \equiv 0$ on $\Omega$. Hence the simulation's solution is the *only* solution consistent with the boundary data — *uniqueness*. Without uniqueness, the simulation would be useless: a second engineer running a second simulation might converge to a different temperature field, and there would be no principled way to choose between them. *Uniqueness is what makes simulation trustworthy as engineering*. The maximum-principle argument is the certificate, and the certificate is *uniqueness, not value*.

These two scenes look unrelated. An ISRO engineer certifying a parachute trigger; a BARC engineer trusting a coolant simulation. They share one of the most consequential reframings in mathematical engineering, and one of the most under-appreciated reframings in JEE / RMO problem solving. *The ISRO engineer proves an existence claim; the BARC engineer proves a uniqueness claim; both are doing problem-solving without computing the answer*. The certification of existence (or uniqueness) is the *deliverable*; the actual value of the deployment time (or temperature) is irrelevant to the certification — it would be irrelevant even if it were computable. The mathematical structure of "prove it exists" is *fundamentally different* from "compute the answer", and the trained solver knows to *separate the two questions* and answer each on its own terms.

This is *Existence / Uniqueness Conditions*. It is the third chapter of the *Constraint Exploitation* sub-pillar (Chapters 9–12). Where Chapter 9 (Domain Constraints) treated constraints as *filters on candidate solutions* and Chapter 10 (Inequality Constraints) treated them as the *engine of optimisation*, Chapter 11 treats existence and uniqueness as *separate, askable questions*. The chapter equips the reader with the named-theorem toolkit (IVT, MVT, Rolle, Brouwer, Banach, maximum principle, Cauchy functional equation) that converts *continuity and boundary conditions* into *existence and uniqueness certificates*, and develops the discipline of *recognising which question the problem actually asks*.

The chapter has three structural threads. The first is the *toolkit*: the named existence and uniqueness theorems, and the signatures by which they are recognised. The second is the *separation principle*: existence and uniqueness are independent questions; many problems ask only one of them, and the trained solver can identify which is asked and answer it without the other. The third is the *constructive vs. non-constructive distinction*: some existence proofs build the object (Banach's iteration constructs the fixed point), while others merely certify it (IVT certifies a zero exists without identifying which point it is). The trained solver knows the distinction and chooses the route the problem allows.

> *Prove it exists before you find it. Existence and uniqueness are separable questions; many problems ask only one of the two.*

---

## 1. The Archetype Defined

### 1.1 Formal Definition

We make the intuition precise.

\begin{definition}[Existence / Uniqueness Condition]
An *existence condition* on a problem with variables $x \in D$ is a statement of the form *there exists $x \in D$ such that $P(x)$ holds*, where $P$ is a property (typically an equation, inequality, or fixed-point relation). A *uniqueness condition* is a statement of the form *there is at most one $x \in D$ such that $P(x)$ holds*. The two conditions are *logically independent*: a problem may have existence without uniqueness (multiple solutions), uniqueness without existence (vacuously — at most one), or both (a *well-posed* problem). The archetype is the discipline of *separating the two questions* and answering each by the appropriate machinery.
\end{definition}

Three remarks unpack the definition. First, the *two questions are independent*: a problem may ask only one of them. *"Does an odd-degree polynomial have a real root?"* asks only for existence; the count and location are irrelevant to the answer (*yes*). *"Show that $f(x) = e^x + x$ has a unique fixed point in $\mathbb R$"* asks for both — existence (proved by IVT) and uniqueness (proved by strict monotonicity). *"Show that the integral $\int_0^\infty \frac{\sin x}{x}\,dx$ converges to $\pi/2$"* asks for existence (the improper integral converges) and then for the *value*. The trained solver reads which questions are asked and answers them in the order specified.

Second, existence proofs come in two flavours — *constructive* (the proof builds the object) and *non-constructive* (the proof certifies existence without building it). *Constructive*: Banach's iteration $x_{n+1} = f(x_n)$ builds the fixed point in the limit; Newton's method builds the root; the Euclidean algorithm builds the gcd. *Non-constructive*: IVT certifies a zero without locating it; Brouwer's fixed-point theorem in dimensions $\ge 2$ is non-constructive (the proof goes through degree theory, not an explicit fixed point); Bolzano-Weierstrass certifies a convergent subsequence without choosing one. The distinction matters: a non-constructive existence proof gives *no* algorithm for finding the object, only the guarantee that it exists.

Third, uniqueness proofs typically have one of three forms: *by contradiction* (assume two solutions, derive a contradiction); *by contraction* (the map is contractive; any two starting points converge to the same limit); *by convexity / monotonicity* (the solution set is a singleton because the equation has a strictly monotonic structure). The maximum principle for elliptic PDEs is a *combination*: it certifies uniqueness by showing that the *difference* of any two solutions has zero on the boundary and zero maximum inside, hence is identically zero.

The chapter encounters five characteristic forms of existence / uniqueness condition.

- **Form I — IVT / Bolzano (continuity-based existence).** The Intermediate Value Theorem and its specialisations. *Diagnostic:* the problem asks for the existence of a *zero* (or a *value attained*) of a continuous function on an interval. *Examples.* WE1 (real roots of the rational-sum equation), WE3 (1-dim Brouwer via IVT on $f(x) - x$), PP6 (odd-degree polynomial root).

- **Form II — Rolle / MVT (differentiability-based existence).** The Mean Value Theorem and its specialisations (Rolle, Cauchy, Lagrange forms). *Diagnostic:* the problem asks for the existence of a point where the *derivative* satisfies some condition. *Examples.* PP5 (Rolle iteration on polynomial-root interlacing).

- **Form III — Banach / contraction-mapping (constructive existence + uniqueness).** A contractive self-map of a complete metric space has a unique fixed point, found by iteration. *Diagnostic:* the problem has a fixed-point equation $x = f(x)$ where $f$ is *contractive* (Lipschitz constant $< 1$). *Examples.* PP7 (Dottie-number iteration for $x = \cos x$).

- **Form IV — Maximum principle / energy argument (uniqueness for ODEs and PDEs).** The maximum principle says that solutions of certain elliptic / parabolic equations attain their extrema on the boundary. *Diagnostic:* the problem has an ODE / PDE with boundary conditions and asks for uniqueness of the solution. *Examples.* WE2 (max-principle uniqueness for an ODE).

- **Form V — Functional equation theorems (uniqueness in the presence of structural constraints).** A functional equation in conjunction with a topological constraint (continuity, monotonicity, measurability) often determines the solution up to a finite-dimensional family. *Diagnostic:* the problem gives a functional equation and a regularity hypothesis. *Examples.* PP4 (Cauchy functional equation: continuity forces $f(x) = cx$).

### 1.2 The Core Principle

Stripped to its essence, the principle of existence / uniqueness conditions is one sentence.

> *Prove it exists before you find it. Existence and uniqueness are separable questions; many problems ask only one of the two.*

This sentence has three layers. The first layer is *order of business*: *prove existence first*, then (if asked) compute the value. This order is not a stylistic preference; it is a logical necessity. *Computing a value* (by an algebraic manipulation, a calculus operation, an algorithm) is only meaningful if the value *exists*. A computation that produces $-2$ for the number of real roots of a polynomial has not "found" the answer; it has merely demonstrated that the computational procedure does not respect the existence question.

The second layer is *separation*: existence and uniqueness are *independent* questions, and a problem may ask only one of them. The trained solver reads the problem carefully — *"how many real roots does this polynomial have?"* asks for existence (at least one? at least three? exactly seven?) and not for the roots themselves. *"Is the solution to this differential equation unique?"* asks for uniqueness and presupposes existence. *"Find the unique fixed point of $f$"* asks for both, in that order. Misreading which question is asked is the single most common source of misdirected effort in this archetype.

The third layer is the *constructive / non-constructive distinction*: existence proofs come in two flavours, and the choice between them is sometimes the problem's central technical decision. *Constructive* proofs (Banach, Newton, Euclidean algorithm) give a procedure that builds the object; *non-constructive* proofs (IVT, Brouwer in higher dimensions, Bolzano-Weierstrass) certify the object's existence without identifying it. For problems asking only for existence, either route suffices; for problems asking for the object itself, only the constructive route delivers. The trained solver knows which route is needed and chooses accordingly.

### 1.3 The Cognitive Shift

Three cognitive shifts deserve naming.

The first is the *existence-first reading*. The trained solver, upon seeing a problem of the form *"the solution to this equation is ..."*, first asks *does a solution exist?* — separately from *what is the solution?* This shift converts the apparent single question into two: the *existence* question (usually fast — IVT, MVT, or a fixed-point theorem) and the *value* question (often slower — algebraic manipulation, numerical computation, special-function evaluation). The existence question is *answerable independently* and often *cannot be skipped*; the value question depends on existence.

The second shift is *named-theorem recognition*. The toolkit of existence / uniqueness theorems is finite and well-organised: IVT for continuity-based existence on intervals; Rolle and MVT for differentiability-based existence; Brouwer for fixed points of continuous self-maps; Banach for contractive fixed points; maximum principle for elliptic ODEs / PDEs; Cauchy-equation theorem for additive functions with continuity. The trained solver matches the problem's structural pattern to the appropriate theorem in seconds and deploys it confidently.

The third shift is *constructive-vs-non-constructive awareness*. The trained solver knows that *some* existence proofs build the object (Banach's iteration converges) while *others* only certify it (IVT certifies a zero without locating it). For problems where the object's location matters (numerical approximation, algorithm design), the constructive route is mandatory; for problems where existence alone suffices (theoretical guarantees, certification), the non-constructive route is acceptable. The distinction is not pedantic; it is the difference between a *proof that an algorithm exists* and *the algorithm itself*.

---

## 2. The Deep Structure

### 2.1 Mathematical Foundations

Existence / uniqueness conditions rest on four mathematical foundations.

The first is *continuity and the topological structure of the real line*. The Intermediate Value Theorem is, structurally, a statement about the *connectedness* of intervals in $\mathbb R$: a continuous function maps connected sets to connected sets, and a connected subset of $\mathbb R$ that contains $f(a)$ and $f(b)$ (with $f(a) < f(b)$, say) also contains every value in between. The IVT is the elementary specialisation; the deeper foundation is the *topological category* in which continuity is the morphisms. The generalisation to higher dimensions (Brouwer's fixed-point theorem, the Borsuk-Ulam theorem) requires *algebraic topology* (homology, degree theory) — but the 1-dim case is elementary enough that JEE / RMO problems exercise it directly.

The second is *differentiability and the Rolle-MVT family*. Rolle's theorem (the special case of MVT where $f(a) = f(b)$) is the foundation: a differentiable function on a closed interval with equal endpoint values has a critical point in the interior. The MVT is the affinisation: any continuous-and-differentiable $f$ on $[a, b]$ has, at some interior point $c$, $f'(c) = \frac{f(b) - f(a)}{b - a}$ — i.e., the secant slope is attained as an instantaneous slope somewhere. Cauchy's MVT (the parametric form) and Taylor's theorem with remainder are the generalisations. The interlacing-of-derivatives corollary (PP5) follows from iterated Rolle.

The third foundation is *completeness and Banach's contraction-mapping theorem*. A *complete* metric space is one in which every Cauchy sequence converges. The real line $\mathbb R$ is complete; so are $\mathbb R^n$, closed intervals, closed subsets of complete spaces, $C[a, b]$ with the sup norm, $L^2$ spaces. Banach's contraction-mapping theorem says: if $X$ is complete and $f : X \to X$ is *contractive* (i.e., $d(f(x), f(y)) \le k \cdot d(x, y)$ for some constant $k < 1$), then $f$ has a unique fixed point, and iteration $x_{n+1} = f(x_n)$ from any seed $x_0$ converges to it geometrically. Banach's theorem is both an *existence* theorem (a fixed point exists), a *uniqueness* theorem (it is the only one), and a *constructive* theorem (the iteration builds it). The theorem is the workhorse of numerical methods: Newton's method is a near-Banach iteration; the contraction-mapping principle underlies the existence-uniqueness theorems for ODEs (Picard-Lindelöf) and the implicit function theorem.

The fourth foundation is the *maximum principle*. For solutions of elliptic ODEs and PDEs (such as the Laplace equation $\nabla^2 u = 0$ or the more general $\nabla^2 u + c(x) u = f$ with appropriate sign conditions on $c$), the *maximum principle* states that the solution attains its extrema on the *boundary* of the domain, not in the *interior*. The consequence: if two solutions agree on the boundary, their difference is a solution with zero boundary values, and the maximum principle forces the difference to be identically zero — *uniqueness*. The maximum principle is the universal tool for uniqueness in elliptic-PDE theory, and its discrete version (the maximum principle for finite-difference schemes) underlies the convergence theory of numerical PDE solvers.

A deeper foundation, beyond the chapter's required machinery, is *Picard-Lindelöf* (the existence-and-uniqueness theorem for ordinary differential equations): for an ODE $\dot x = F(x, t)$ with $F$ Lipschitz in $x$ on a closed set, the initial-value problem has a unique solution on some interval. The proof is a *contraction-mapping* argument on the function space $C[a, b]$, applied to the integral form $x(t) = x_0 + \int_a^t F(x(s), s)\,ds$. Picard-Lindelöf is the *master* existence-and-uniqueness theorem of ODE theory; it underlies almost all of mathematical physics' confidence that the equations of motion have well-defined solutions.

### 2.2 Physical and Cross-Domain Foundations

The reach of existence / uniqueness conditions extends across the quantitative sciences.

In *physics*, the existence of *equilibrium states* (a static configuration where all forces balance) and the *uniqueness of trajectories* (a particle with given initial conditions follows one definite path) are foundational. *Newton's second law* $F = ma$, viewed as a second-order ODE in $x(t)$, has — by Picard-Lindelöf — a unique solution given $x(0)$ and $\dot x(0)$ (provided $F$ is Lipschitz). The *uniqueness of trajectory* is what makes classical mechanics *deterministic*: knowing the initial conditions and the forces uniquely determines the future. In *quantum mechanics*, the Schrödinger equation $i\hbar \partial_t \psi = H\psi$ is a linear first-order ODE in the function space of wave functions, and its solutions (the *time evolution*) are unique. The *measurement axiom* introduces apparent non-uniqueness (collapse to an eigenstate); but the *unitary evolution* between measurements is uniquely determined.

In *engineering*, the existence and uniqueness of *equilibrium designs* underlies every successful engineering project. The opening vignette's ISRO engineer certifies existence; the BARC engineer certifies uniqueness. *Structural engineering* relies on the maximum principle (for stress distributions in elastic bodies); *electrical engineering* relies on the uniqueness of solutions to Maxwell's equations under boundary conditions; *control engineering* relies on the existence of stable feedback loops (Brouwer's fixed-point in the design of Lyapunov functions). The trained engineer reads every specification as an *existence-and-uniqueness* problem: *does an admissible design exist?* and *is it the only one?*

In *economics and game theory*, *equilibrium existence* is the foundational question. *Nash's theorem*: every finite game has at least one Nash equilibrium in mixed strategies (proved by Brouwer's fixed-point theorem). *Arrow-Debreu*: every Walrasian-equilibrium economy under suitable convexity assumptions has at least one equilibrium price vector (proved by the Kakutani fixed-point theorem, a Brouwer-generalisation to set-valued maps). *Uniqueness* is harder and typically requires additional structure (gross substitutability, strict concavity of utility functions). The entire framework of *general equilibrium theory* is, structurally, an existence theorem; uniqueness is a desideratum, not a guarantee.

In *biology and medicine*, *steady-state existence* (a homeostatic configuration of the body) and *trajectory uniqueness* (a disease progression follows one definite path given initial conditions) are foundational. *Epidemiological models* (SIR, SEIR, SIRD): existence and uniqueness of solutions follow from Picard-Lindelöf; the qualitative features of the trajectory (the *basic reproduction number* $R_0$, the *peak time*, the *final size*) are uniquely determined by the model parameters and the initial conditions. *Pharmacokinetics*: drug-concentration trajectories are uniquely determined by the dosing schedule and the pharmacological parameters.

In *computer science*, *type inference* (does a well-typed program exist?), *program termination* (does the program halt?), *system equilibrium* (does the protocol reach a stable state?), and *deadlock freedom* (is the system free of mutually-blocking states?) are all existence / uniqueness questions. *Algorithm design* often reduces to *proving existence of a feasible solution* and then *constructing the optimal one*. The *halting problem* (does a given Turing machine halt on a given input?) is a foundational *existence* question — and its undecidability is one of the foundational results of computability theory.

### 2.3 Cognitive Foundations

The cognitive payoff of existence / uniqueness conditions is threefold.

The first is *separation of concerns*. The trained solver who internalises the *existence-first* reading processes problems differently. They ask: *what does the problem actually require? Existence? Uniqueness? Value?* They allocate effort accordingly. The split prevents the most common time-sink in problem solving: *trying to compute a value when only existence was asked, or trying to certify uniqueness when only existence was asked*.

The second payoff is *toolkit efficiency*. The named-theorem toolkit (IVT, Rolle, MVT, Brouwer, Banach, maximum principle, Cauchy-equation) is finite and well-organised. The trained solver knows when to deploy each, and the choice is fast: IVT for *continuity + zero existence*; Rolle / MVT for *differentiability + critical-point existence*; Banach for *contractive fixed-point existence + uniqueness*; maximum principle for *elliptic-ODE / PDE uniqueness*; Cauchy-equation theorem for *additive functions + continuity → linearity*. The toolkit is a menu, and selection is fast.

The third payoff is *constructive-vs-non-constructive discernment*. The trained solver knows that some problems admit *only* a non-constructive proof of existence (Brouwer in dimensions $\ge 2$, the existence of transcendental numbers via cardinality), while others admit a *constructive* proof that *also* gives an algorithm (Banach iteration, Newton's method). For applications where the *object's location* matters (numerical computation, algorithm design), only the constructive route works; for *theoretical guarantees*, the non-constructive route suffices. The trained solver matches the route to the problem's requirements.

---

## 3. The Diagnostic Toolkit

### 3.1 The Three Questions Method (Existence / Uniqueness Edition)

Before deploying any theorem, the trained solver asks three questions of the problem.

1. **Which question is asked?** Read the problem carefully and identify whether it asks for *existence* (does a solution exist?), *uniqueness* (is the solution the only one?), or *value* (what is the solution?). Many problems ask only one of the three; some ask two; some ask all three (in the order existence → uniqueness → value).

2. **Which named theorem deploys here?** Match the problem's structural pattern to the appropriate theorem: *continuity + sign change* $\Rightarrow$ IVT; *differentiability + equal endpoints* $\Rightarrow$ Rolle; *differentiability + secant question* $\Rightarrow$ MVT; *continuous self-map of an interval* $\Rightarrow$ 1-dim Brouwer (via IVT); *contractive self-map of a complete space* $\Rightarrow$ Banach; *elliptic ODE / PDE with boundary data* $\Rightarrow$ maximum principle; *additive function with continuity* $\Rightarrow$ Cauchy-equation theorem.

3. **Constructive or non-constructive?** If the problem asks for the *value* of the solution (not just existence), determine whether the chosen theorem is constructive (Banach iterates, Newton iterates) or merely existence-certifying (IVT, Brouwer in higher dims). For non-constructive theorems, supplement with a separate construction (algebraic manipulation, numerical method, special-function evaluation).

The three questions can be answered in seconds. They are the discipline that converts *existence / uniqueness problems* into *direct application of the appropriate theorem*.

### 3.2 Forms of Existence / Uniqueness Conditions: A Comprehensive Guide

We collect the five forms encountered in the chapter with one-line diagnostics.

- **Form I — IVT / Bolzano (continuity-based existence).** *Diagnostic:* the problem asks for the existence of a *zero* of a continuous function on an interval, or of a point where a continuous function attains a given value. *Move:* check sign change (or value-attainment) at the endpoints; cite IVT. *Examples.* WE1, WE3, PP6.

- **Form II — Rolle / MVT (differentiability-based existence).** *Diagnostic:* the problem asks for the existence of a point where the *derivative* takes a specified value, or where the *secant slope* is realised as a tangent. *Move:* verify the function's continuity and differentiability; cite Rolle (if endpoints agree) or MVT (general). *Examples.* PP5 (iterated Rolle on polynomial derivatives).

- **Form III — Brouwer / Banach (fixed-point theorems).** *Diagnostic:* the problem has the form $x = f(x)$, with $f$ a self-map of a domain. *Move:* if $f$ is continuous and the domain is a closed interval, use Brouwer (1-dim Brouwer is proved by IVT on $g(x) = f(x) - x$); if $f$ is contractive on a complete space, use Banach (existence + uniqueness + constructive iteration). *Examples.* WE3 (Brouwer), PP7 (Banach + Dottie number).

- **Form IV — Maximum principle (ODE / PDE uniqueness).** *Diagnostic:* the problem has an ODE or PDE with boundary conditions, and asks for uniqueness of the solution. *Move:* assume two solutions, take the difference; apply the maximum principle to the difference (which has zero boundary values) and conclude the difference is identically zero. *Examples.* WE2 (max-principle for a second-order ODE).

- **Form V — Functional equation theorems (uniqueness with regularity hypotheses).** *Diagnostic:* the problem has a functional equation (Cauchy, Jensen, d'Alembert, Pexider) plus a regularity hypothesis (continuity, monotonicity, measurability). *Move:* derive the value on a dense subset (rationals, dyadic numbers) by induction or substitution; extend to the full domain by the regularity hypothesis. *Examples.* PP4 (Cauchy functional equation).

### 3.3 Common Pitfalls

Five errors recur often enough to deserve named warnings.

- **The Existence-Skipped Pitfall.** Computing a value (by algebra, calculus, or numerical method) without first verifying that the value exists. The student who solves $\sqrt{x - 1} = x - 3$ by squaring and getting $x = 2$ or $x = 5$, then reports both, has skipped the existence check: at $x = 2$, $\sqrt{1} = 1$ but $x - 3 = -1$; existence fails. (PP3 develops this in detail.) The remedy is to *check existence at the candidate values*.

- **The Uniqueness-Assumed Pitfall.** Treating a problem's solution as unique without verification, and reporting only one of multiple solutions. The student who finds one root of a polynomial and stops has assumed uniqueness; the polynomial may have more roots. The remedy is *count the solutions before reporting*.

- **The Wrong-Theorem Pitfall.** Citing IVT for a discontinuous function, Rolle for a non-differentiable one, Banach for a non-contractive map, or the maximum principle for a non-elliptic ODE. Each theorem has specific hypotheses, and the hypotheses must be *verified* before the theorem is cited. The remedy is the §3.1 Q2 discipline: *match the theorem to the verified hypotheses*.

- **The Constructive-Confused Pitfall.** Reporting a *value* for a problem whose existence proof is non-constructive (IVT says a zero exists but doesn't say where). The remedy is to *separate the existence step from the location step*: cite IVT for existence; then deploy a separate algorithm (bisection, Newton's method, or algebraic root-finding) for location.

- **The Boundary-vs-Interior Pitfall.** Applying Rolle or the maximum principle without correctly identifying whether the extremum is at the boundary or in the interior. Rolle gives an *interior* critical point; the maximum principle for elliptic equations says the *maximum is on the boundary* (or the function is constant). Mis-identifying which is the case gives the wrong conclusion. The remedy is *check the boundary values first*, then apply the appropriate theorem.

---

## 4. Worked Examples

We work three problems in detail, each in the six-point format. The first illustrates Form I (IVT) for proving a polynomial-like equation has all real roots; the second illustrates Form IV (maximum principle) for proving uniqueness of an ODE solution; the third illustrates Form III (Brouwer via IVT) for the 1-dim fixed-point theorem.

### 4.1 Example 1 — Real Roots of a Rational-Sum Equation

**Problem.** *Let $a_1 < a_2 < \cdots < a_n$ be distinct real numbers, and let $A_1, A_2, \ldots, A_n$ be positive real numbers. Prove that the equation*
\[
  \sum_{i=1}^n \frac{A_i}{x - a_i} \;=\; 0
\]
*has $n - 1$ real roots, one in each open interval $(a_i, a_{i+1})$ for $i = 1, 2, \ldots, n - 1$.*
*(Joshi EJM Ch. 24, Exercise 24.70.)*

**SEED.** *Existence (Form I — IVT applied across each pole).* The function $f(x) = \sum_i A_i / (x - a_i)$ has $n$ simple poles at $x = a_i$, between consecutive poles it is continuous and changes sign from $+\infty$ to $-\infty$; IVT then forces a zero in each gap. The polynomial-degree count caps the total at $n - 1$, so the gap count *equals* the total root count, and all roots are accounted for.

**BRUTE PATH.** Clear denominators: multiply both sides by $\prod_{j=1}^n (x - a_j)$. The equation becomes
\[
  \sum_{i=1}^n A_i \prod_{j \ne i} (x - a_j) \;=\; 0,
\]
which is a polynomial equation in $x$ of degree $n - 1$. A polynomial of degree $n - 1$ has at most $n - 1$ real roots. To prove that *all* $n - 1$ roots are real requires showing the discriminant is non-negative — a $(2n - 2)$-th degree polynomial-discriminant computation that is intractable for general $n$. The brute path *works in principle* but is computationally hopeless beyond $n = 4$ or so.

**ELEGANT PIVOT.** *Apply IVT in each gap.*

*Step 1 — Continuity in each gap.* The function $f(x) = \sum_{i=1}^n A_i / (x - a_i)$ is a finite sum of continuous functions (each $A_i / (x - a_i)$ is continuous for $x \ne a_i$); hence $f$ is continuous on the complement of the pole set, $\mathbb R \setminus \{a_1, \ldots, a_n\}$. In particular, $f$ is continuous on each open interval $(a_i, a_{i+1})$ for $i = 1, \ldots, n - 1$.

*Step 2 — Sign analysis at each pole.* Consider the behaviour of $f$ as $x$ approaches a pole $a_k$. Among the $n$ summands of $f$:
- The $k$-th summand $A_k / (x - a_k)$ dominates as $x \to a_k$; the others remain bounded.
- As $x \to a_k^+$ (from above), $x - a_k \to 0^+$, so $A_k / (x - a_k) \to +\infty$. Hence $f(x) \to +\infty$.
- As $x \to a_k^-$ (from below), $x - a_k \to 0^-$, so $A_k / (x - a_k) \to -\infty$. Hence $f(x) \to -\infty$.

*Step 3 — IVT in each gap.* Fix $i \in \{1, \ldots, n - 1\}$ and consider the gap $(a_i, a_{i+1})$.
- As $x \to a_i^+$: $f(x) \to +\infty$ (by step 2 at the left pole $a_i$).
- As $x \to a_{i+1}^-$: $f(x) \to -\infty$ (by step 2 at the right pole $a_{i+1}$).
- $f$ is continuous on $(a_i, a_{i+1})$.

By the Intermediate Value Theorem, *there exists $c_i \in (a_i, a_{i+1})$ with $f(c_i) = 0$* (any value between $+\infty$ and $-\infty$, including $0$, is attained). So each gap contains at least one zero.

*Step 4 — Total root count.* We have proved the existence of at least $n - 1$ zeros (one in each of the $n - 1$ gaps). On the other hand, when the equation is cleared of denominators (as in the brute path), it becomes a polynomial equation of degree $n - 1$, which has *at most* $n - 1$ real roots. Hence the gap count *equals* the total root count: there are *exactly* $n - 1$ real roots, all of which lie in the bounded interval $(a_1, a_n)$, one in each gap.

*Step 5 — No zeros outside $[a_1, a_n]$.* For $x > a_n$: every summand $A_i / (x - a_i) > 0$ (since $A_i > 0$ and $x - a_i > 0$), so $f(x) > 0$. For $x < a_1$: every summand $A_i / (x - a_i) < 0$, so $f(x) < 0$. Hence no zeros outside $(a_1, a_n)$, confirming that all $n - 1$ zeros are in the gaps. \hfill$\blacksquare$

The elegant pivot deploys IVT *non-constructively* (we know each gap contains a zero, but the proof gives no procedure for finding it) and combines with a *degree-count upper bound* (the polynomial form, used as an inequality on the root count, not as a computational tool). The combination of *IVT from below* and *degree-count from above* is the technique's beauty: each alone is weak; together they pin the count to exactly $n - 1$.

**PITFALLS.**

- *Treating $f$ as a polynomial.* The function $\sum A_i / (x - a_i)$ is *not* a polynomial; it is a rational function with $n$ simple poles. Trying to apply polynomial-root-counting theorems to $f$ directly without clearing denominators is incorrect. The remedy is to *clear denominators first* (for the degree-count) and *not clear* (for the IVT-in-gaps argument).

- *Forgetting that the $A_i$ are positive.* The pole-sign analysis (step 2) relies on $A_k > 0$: if $A_k$ could be negative, the sign of $f$ at $x \to a_k^\pm$ would reverse, and the IVT gap-by-gap argument would fail. For mixed-sign $A_i$, the count of real roots can be less than $n - 1$. The remedy is to *check the sign hypothesis on the $A_i$ before invoking step 2*.

- *Missing zeros outside $(a_1, a_n)$.* The argument needs step 5 (no zeros outside $[a_1, a_n]$) to conclude that the IVT zeros in the gaps account for *all* the roots. Without step 5, the proof shows *at least* $n - 1$ real roots but not *exactly* $n - 1$. The remedy is to *also analyse $f$ outside the pole-cluster*.

- *Mis-applying IVT to a function with poles.* The IVT requires *continuity* on a closed interval; the function $f$ is not continuous on $[a_i, a_{i+1}]$ (because of the poles at the endpoints), only on the open interval $(a_i, a_{i+1})$. The IVT applies to the *open* interval by taking limits at the endpoints. The remedy is to *carefully state* that the IVT is being applied on an open interval with prescribed limit behaviour at the endpoints.

- *Confusing "exactly one root per gap" with "the count is at least one per gap".* IVT alone gives *at least* one root per gap; the degree-count gives *at most* $n - 1$ in total; together, *exactly* one per gap. A student who reports "at least $n - 1$ roots" has done only half the work. The remedy is to *combine the two bounds explicitly*.

**CONNECTIONS.**

*Primary archetype applications.* The IVT-in-gaps technique is the universal tool for proving *root-existence-in-intervals* claims for rational functions with prescribed pole behaviour. It generalises to *interlacing* claims for sequences of polynomials (Sturm sequences, orthogonal polynomials), to *eigenvalue interlacing* in linear algebra (Cauchy's interlacing theorem for symmetric matrices), and to *spectral theory* (the eigenvalues of a Sturm-Liouville operator interlace with those of a perturbation).

*Alternative solution archetypes.* The same result admits a *Rolle-iteration* proof (Form II): consider the antiderivative $F(x) = \sum_i A_i \ln|x - a_i|$, which has a critical point (i.e., a zero of $F' = f$) between each pair of consecutive vertical asymptotes. The Rolle-iteration is structurally elegant but requires more machinery (the antiderivative); IVT is the elementary route.

*Cross-domain manifestations.* The pattern *function with poles + continuity in gaps + sign changes at poles* $\to$ *at least one zero per gap* recurs across mathematics. In *spectral theory*, the eigenvalues of a symmetric Jacobi matrix interlace with those of its top-left-corner sub-matrix, by exactly this argument. In *control theory*, the *root locus* of a feedback system has branches that interlace with the system's poles, by the same continuity-of-roots argument. In *quantum mechanics*, the *energy levels* of a 1-dim potential interlace with the eigenvalues of a comparison potential (Sturm's comparison theorem).

**TAKEAWAY.** *IVT in each gap + degree-count upper bound = exact root count for rational-sum equations with prescribed pole behaviour.*

---

### 4.2 Example 2 — Maximum-Principle Uniqueness for a Second-Order ODE

**Problem.** *Let $f : [a, b] \to \mathbb R$ be twice differentiable and let $g : [a, b] \to \mathbb R$ be continuous. Suppose $f$ satisfies the ODE*
\[
  f''(x) + g(x) f'(x) - f(x) \;=\; 0 \quad \text{for all } x \in [a, b],
\]
*and the boundary conditions $f(a) = f(b) = 0$. Prove that $f \equiv 0$ on $[a, b]$.*
*(Joshi EJM Ch. 24, Exercise 24.97.)*

**SEED.** *Uniqueness (Form IV — maximum-principle argument).* The ODE has the structural form *$f'' = f - g\,f'$* (the leading coefficient of $f$ on the RHS is $+1$, the "wrong" sign for the maximum principle to work directly on $f$; but the *interior-extremum analysis* still works). At an interior maximum of $f$, $f' = 0$ and $f'' \le 0$, but the ODE forces $f'' = f - g \cdot 0 = f > 0$ (if the maximum is positive). Contradiction unless $f \le 0$ at every interior point. Symmetric argument for the minimum. Combining: $f \equiv 0$.

**BRUTE PATH.** A student who knows the existence-and-uniqueness theorem for linear second-order ODEs (Picard-Lindelöf for the second-order linear case) could cite it: *the IVP $f'' + g f' - f = 0$ with $f(a) = 0, f'(a) = c$ has a unique solution for each $c$. The boundary condition $f(b) = 0$ then constrains $c$, and the trivial solution $f \equiv 0$ corresponds to $c = 0$. Whether non-trivial $c$ exists depends on $g$.* The brute path requires the heavy machinery of linear ODE theory and the *boundary-value problem* analysis (specifically, whether the Sturm-Liouville eigenvalue problem $f'' + gf' - \lambda f = 0$ has $\lambda = 1$ as an eigenvalue for the given $g$). For competition mathematics, this is unwieldy.

**ELEGANT PIVOT.** *Maximum-principle argument.*

*Step 1 — Setup.* Suppose, for contradiction, that $f \not\equiv 0$. Since $f$ is continuous on the closed interval $[a, b]$ (in fact, twice-differentiable), $f$ attains its maximum $M$ and minimum $m$ on $[a, b]$. We claim that *both* $M \le 0$ and $m \ge 0$, which combined give $f \equiv 0$.

*Step 2 — Maximum is $\le 0$.* Suppose $M > 0$. Then $M$ is attained at some point $x_0 \in [a, b]$. Since $f(a) = f(b) = 0 < M$, $x_0 \ne a$ and $x_0 \ne b$, so $x_0 \in (a, b)$ — an *interior* point.

At $x_0$:
- $f'(x_0) = 0$ (necessary condition for an interior maximum of a differentiable function).
- $f''(x_0) \le 0$ (sufficient condition for an interior maximum to be a local max — by the second-derivative test, or by the fact that a twice-differentiable function with positive second derivative is locally convex and so does not have a local max).

Substitute $x = x_0$ into the ODE:
\[
  f''(x_0) + g(x_0) \cdot 0 - f(x_0) \;=\; 0 \quad\Longrightarrow\quad f''(x_0) \;=\; f(x_0) \;=\; M \;>\; 0.
\]
But $f''(x_0) \le 0$ by the interior-maximum condition. *Contradiction.* Hence the assumption $M > 0$ is false, and $M \le 0$.

*Step 3 — Minimum is $\ge 0$.* By symmetry, replace $f$ by $-f$. Since the ODE is *linear in $f$* (with no constant term — the equation is *homogeneous*), if $f$ satisfies the ODE then so does $-f$, with the same boundary conditions $-f(a) = -f(b) = 0$. The argument of step 2 applied to $-f$ gives $\max(-f) \le 0$, i.e., $-\min(f) \le 0$, i.e., $m = \min(f) \ge 0$.

*Step 4 — Conclusion.* Combining: $M \le 0 \le m$. But $m \le M$ trivially (min is at most max). Hence $m = M = 0$, i.e., $f \equiv 0$ on $[a, b]$. \hfill$\blacksquare$

The elegant pivot is a single application of the *interior-extremum analysis*: at an interior maximum, the second derivative is non-positive, but the ODE forces it to be *equal* to the positive function value. The contradiction forces the maximum to be $\le 0$; symmetric argument for the minimum; combination gives $f \equiv 0$. The proof avoids the heavy machinery of Sturm-Liouville theory entirely.

**PITFALLS.**

- *Forgetting the boundary conditions in the interior-max argument.* The argument requires that the maximum is attained at an *interior* point — which in turn requires that the boundary values $f(a), f(b)$ are *smaller* than the maximum. The boundary conditions $f(a) = f(b) = 0$ guarantee this whenever the maximum is positive (i.e., $M > 0$). Without the boundary conditions (e.g., if $f(a) = M > 0$ were allowed), the maximum could be at the boundary, and the interior-derivative analysis would not apply. The remedy is to *check that the maximum is interior* before applying the derivative test.

- *Mis-applying the second-derivative test.* The second-derivative test says $f''(x_0) \le 0$ at an interior local maximum *if* $f$ is twice differentiable at $x_0$. A function that has a corner or cusp at $x_0$ does not satisfy the test. The problem's hypothesis ($f$ twice differentiable) covers this. The remedy is to *verify the twice-differentiability hypothesis*.

- *Treating the ODE as inhomogeneous.* The equation $f'' + gf' - f = 0$ is *homogeneous* (no constant term). Hence $-f$ also satisfies the equation, and the symmetric argument in step 3 is valid. For an inhomogeneous equation $f'' + gf' - f = h(x)$ with $h \ne 0$, the symmetric argument fails: $-f$ would satisfy $f'' + gf' - f = -h$, not the original equation. The remedy is to *verify the equation is homogeneous before invoking the symmetric argument*.

- *Confusing "maximum is $\le 0$" with "$f \le 0$".* The maximum is $\le 0$ means $\max f \le 0$, which is equivalent to $f(x) \le 0$ for all $x$. Combined with the symmetric $f(x) \ge 0$, we get $f(x) = 0$ for all $x$. The remedy is to *track the logical chain explicitly*.

- *Trying to prove this by a constructive method.* The maximum-principle proof is *non-constructive*: it does not *find* the solution (it merely certifies that the only solution is the trivial one). Trying to construct $f$ explicitly from the ODE is harder and unnecessary. The remedy is to *recognise that uniqueness arguments are typically non-constructive*.

**CONNECTIONS.**

*Primary archetype applications.* The maximum-principle argument is the universal uniqueness-tool for linear second-order elliptic ODEs (and their PDE generalisations). It is the foundation of the *uniqueness theory* for the Laplace equation, the Poisson equation, the steady-state heat equation, and many other elliptic equations. The technique appears in mathematical physics (uniqueness of equilibrium configurations), in numerical analysis (convergence of finite-difference schemes), and in financial mathematics (uniqueness of arbitrage-free derivative prices via the Black-Scholes PDE).

*Alternative solution archetypes.* The same result admits an *energy argument*: multiply the ODE by $f$ and integrate; the boundary conditions kill the boundary terms, leaving a quadratic form in $f$ and $f'$ that is non-positive only if $f \equiv 0$. The energy method is more general than the maximum principle (it works for non-linear equations and higher-order systems) but requires more computation. For competition mathematics, the maximum principle is the elementary route.

*Cross-domain manifestations.* The *maximum principle* is one of the most universally applicable techniques in analysis. In *complex analysis*, *Liouville's theorem* (bounded entire functions are constant) is a maximum-principle argument on the modulus of the function. In *information theory*, the *data processing inequality* is a maximum-principle-style statement on the entropy after post-processing. In *probability theory*, the *martingale optional stopping theorem* is a maximum-principle-style statement on stopped processes. The maximum principle is, structurally, the assertion that *certain functionals attain their extrema on the boundary of their domain* — a deep and universal property.

**TAKEAWAY.** *Maximum-principle uniqueness: assume two solutions; at any interior extremum of their difference, the second-derivative test contradicts the equation; difference is identically zero.*

---

### 4.3 Example 3 — Brouwer's Fixed-Point Theorem in One Dimension

**Problem.** *Let $f : [0, 1] \to [0, 1]$ be continuous. Prove that $f$ has a fixed point, i.e., there exists $x^* \in [0, 1]$ with $f(x^*) = x^*$.*
*(Joshi EJM Ch. 16, Comment 7; the 1-dimensional case of Brouwer's fixed-point theorem.)*

**SEED.** *Existence (Form III — Brouwer via IVT on the difference function).* The map $g(x) = f(x) - x$ is continuous on $[0, 1]$ (difference of two continuous functions). At the boundary points: $g(0) = f(0) - 0 = f(0) \ge 0$ (since $f$ maps into $[0, 1]$), and $g(1) = f(1) - 1 \le 0$ (since $f(1) \le 1$). If either endpoint gives $g = 0$, we are done; otherwise $g(0) > 0$ and $g(1) < 0$, and IVT supplies $x^*$ with $g(x^*) = 0$, i.e., $f(x^*) = x^*$.

**BRUTE PATH.** A student who has not seen Brouwer's fixed-point theorem might try to *construct* a fixed point by iteration $x_{n+1} = f(x_n)$ starting from some seed. This works in *some* cases (e.g., when $f$ is contractive — see PP7) but not in general: for $f(x) = 1 - x$, the iteration starting from $x_0 = 0$ goes $0 \to 1 \to 0 \to 1 \to \cdots$ and never converges (yet the fixed point $x^* = 1/2$ exists). The brute path of iteration *can fail* to construct a fixed point that *does exist*; we need a more powerful existence argument.

**ELEGANT PIVOT.** *Define the difference function and apply IVT.*

*Step 1 — The difference function.* Define $g : [0, 1] \to \mathbb R$ by $g(x) = f(x) - x$. Since $f$ is continuous on $[0, 1]$ (by hypothesis) and $x \mapsto x$ is continuous, $g = f - x$ is continuous on $[0, 1]$.

*Step 2 — Sign analysis at the endpoints.*
- $g(0) = f(0) - 0 = f(0)$. Since $f$ maps into $[0, 1]$, $f(0) \in [0, 1]$, so $f(0) \ge 0$, i.e., $g(0) \ge 0$.
- $g(1) = f(1) - 1$. Since $f(1) \in [0, 1]$, $f(1) - 1 \le 0$, i.e., $g(1) \le 0$.

*Step 3 — Apply IVT (or its specialisation).*
- *Case A:* $g(0) = 0$. Then $f(0) = 0$, so $x^* = 0$ is a fixed point. Done.
- *Case B:* $g(1) = 0$. Then $f(1) = 1$, so $x^* = 1$ is a fixed point. Done.
- *Case C:* $g(0) > 0$ and $g(1) < 0$. Then $g$ changes sign on $[0, 1]$; by IVT, there exists $x^* \in (0, 1)$ with $g(x^*) = 0$, i.e., $f(x^*) = x^*$. Done.

In all three cases, a fixed point exists. \hfill$\blacksquare$

*A note on uniqueness.* The argument proves *existence* but says nothing about *uniqueness*: a continuous self-map of $[0, 1]$ may have one, several, or even infinitely many fixed points. For example: $f(x) = x$ on $[0, 1]$ has *every* point as a fixed point. The classical counterexample to higher-uniqueness — the *staircase function* — has finitely many fixed points. The Brouwer-via-IVT argument is sharp on existence; for uniqueness, additional hypotheses (contraction, monotonicity, convexity) are needed. PP7 illustrates the contractive case (Banach), where existence *and* uniqueness *and* constructive convergence all follow together.

*A note on the name "Brouwer".* The 1-dim fixed-point theorem (this result) is the elementary specialisation of Brouwer's *general* fixed-point theorem, which states: every continuous self-map of a *closed ball* in $\mathbb R^n$ has a fixed point. The 1-dim proof is the elementary IVT argument above; the higher-dim proof requires *algebraic topology* (degree theory, simplicial approximation, the Sperner-lemma route). The locked slate's title "Banach Fixed-Point in $[0, 1]$" is a *misnomer*: Banach's theorem applies only to *contractive* maps and gives *uniqueness* in addition to existence; what is proved here is the *Brouwer 1-dim fixed-point theorem* via IVT, which applies to *continuous* maps (no contraction required) and gives only existence. We correct the terminology here.

**PITFALLS.**

- *Misnaming the theorem as "Banach".* As noted in the framing, the theorem proved here is the *1-dim Brouwer* (also called *Knaster-Tarski* for ordered sets), not Banach. Banach requires contraction and gives uniqueness; Brouwer requires only continuity and gives only existence. Misnaming the theorem confuses what hypothesis is being invoked. The remedy is to *match the theorem name to the hypothesis*: continuity $\Rightarrow$ Brouwer; contraction $\Rightarrow$ Banach.

- *Forgetting the endpoint analysis.* The IVT argument requires *sign change* at the endpoints (or one endpoint giving a zero). The endpoint sign analysis — $g(0) \ge 0$, $g(1) \le 0$ — is mandatory; without it, IVT does not apply. The remedy is to *compute the endpoint values explicitly*.

- *Trying to construct the fixed point.* The IVT argument is *non-constructive*: it certifies a fixed point exists but does not identify which point it is. For a constructive identification, a separate algorithm (bisection on the equation $f(x) - x = 0$, or contractive iteration if $f$ is contractive) is needed. The remedy is to *separate the existence step from the location step*.

- *Assuming the fixed point is unique.* The 1-dim Brouwer gives *existence only*. Uniqueness requires additional hypotheses. The remedy is to *check whether the problem asks for existence, uniqueness, or both, and apply the appropriate hypotheses*.

- *Assuming the domain is a closed interval.* The argument uses that $[0, 1]$ is *closed and bounded* — the IVT requires a closed interval, and the endpoint values are well-defined because the interval includes its endpoints. For *open* intervals (like $(0, 1)$), continuous self-maps may have *no* fixed point (e.g., $f(x) = x/2$ on $(0, 1]$ — wait, this isn't a self-map of $(0,1)$ since $f(1) = 0.5 \in (0,1)$ — let me retry: $f(x) = x + (1 - x)/2 = (x + 1)/2$ on $(0, 1)$ maps to $(1/2, 1)$, no fixed point in $(0, 1)$, since $x = (x+1)/2 \Leftrightarrow x = 1$, which is on the boundary). The remedy is to *check the closed-domain hypothesis*.

**CONNECTIONS.**

*Primary archetype applications.* The IVT-on-difference-function technique is the universal 1-dim approach to fixed-point existence and to the IVT generalisations (Bolzano-Cauchy theorem, Darboux's theorem on the intermediate-value property of derivatives). It generalises to higher dimensions (Brouwer in $n$-dim via degree theory), to set-valued maps (Kakutani's fixed-point theorem), to compact convex subsets of normed spaces (Schauder's theorem), and to non-expansive maps on Hilbert spaces (the Browder-Göhde-Kirk theorem).

*Alternative solution archetypes.* The fixed-point can also be proved *constructively* via *bisection*: at each step, bisect the interval where $g$ changes sign and continue on the half-interval that still has sign change. The bisection converges to the fixed point at a rate of $2^{-n}$ per iteration. The bisection is constructive (it gives an algorithm) but slow; Newton's method on $g$ is faster (quadratically convergent) but requires $g$ to be differentiable.

*Cross-domain manifestations.* The Brouwer fixed-point theorem is the foundation of *Nash's equilibrium existence theorem* in game theory (a Nash equilibrium of an $n$-player finite game in mixed strategies exists, proved by Brouwer in $\mathbb R^{n \cdot k}$). It is also the foundation of *Arrow-Debreu's general-equilibrium theorem* in economics (via Kakutani's set-valued generalisation). It appears in *topology* (the no-retraction theorem, equivalent to Brouwer), in *algebraic geometry* (the existence of fixed points of group actions), in *dynamical systems* (the existence of periodic orbits via Poincaré's recurrence theorem), and in *computer science* (the existence of fixed points of monotone operators in domain theory, underpinning the semantics of recursive programs).

**TAKEAWAY.** *1-dim Brouwer fixed-point: define $g(x) = f(x) - x$, check sign change at endpoints, apply IVT. The theorem is named "Brouwer", not "Banach"; the proof is IVT, not contractive.*

---

## 5. Practice Problems

Seven problems, statements only; full solutions appear in the Appendix. The slate spans Tier 1 through Tier 3, with three JEE-Mains-level problems (PP1, PP3, PP6) anchoring accessibility and the harder ones (PP4, PP5, PP7) pushing to RMO / olympiad standard.

### 5.1 Non-Differentiability of $\max\{x, x^3\}$ (Tier 1; JEE 2001; Joshi Ch. 24, Exercise 24.41)

Find the set of points where the function $f(x) = \max\{x, x^3\}$ is not differentiable. *(Note: the locked slate v0.2 listed two such points; the verification audit for this chapter discovered the correct count is three — see the appendix solution and the slate v0.2.8 patch for the corrected derivation.)*

### 5.2 Left-Hand Derivative of $[x]\sin(\pi x)$ (Tier 2; JEE 2001; Joshi Ch. 24, Exercise 24.39)

For $k$ a positive integer, find the left-hand derivative of $f(x) = [x]\sin(\pi x)$ at $x = k$, where $[x]$ denotes the greatest-integer function.

### 5.3 Number of Solutions of $\log_4(x - 1) = \log_2(x - 3)$ (Tier 1; JEE 2001; Joshi Ch. 24, Exercise 24.45)

Find the number of real solutions of the equation
\[
  \log_4 (x - 1) \;=\; \log_2 (x - 3).
\]

### 5.4 Cauchy Functional Equation Uniqueness (Tier 3; Joshi Ch. 20, Main Problem)

Let $f : \mathbb R \to \mathbb R$ be continuous and satisfy
\[
  f(x + y) \;=\; f(x) + f(y) \quad \text{for all } x, y \in \mathbb R.
\]
Prove that there exists $c \in \mathbb R$ such that $f(x) = c\,x$ for all $x \in \mathbb R$.

### 5.5 Polynomial-Derivative Interlacing via Rolle (Tier 3; Joshi Ch. 16, Comment 4)

Let $f(x)$ be a polynomial of degree $n$ with $n$ distinct real roots $r_1 < r_2 < \cdots < r_n$. Prove that $f'(x)$ has exactly $n - 1$ distinct real roots, each lying in one of the open intervals $(r_i, r_{i+1})$ for $i = 1, 2, \ldots, n - 1$.

### 5.6 Odd-Degree Polynomial Has a Real Root (Tier 1; Joshi Ch. 15, Comment 3)

Prove that every polynomial of odd degree with real coefficients has at least one real root.

### 5.7 Dottie Number as a Banach Fixed Point (Tier 3; Joshi Ch. 16, Comment 9)

Define $f : [0, 1] \to [0, 1]$ by $f(x) = (x + \cos x) / 2$. Prove that $f$ is a contraction on $[0, 1]$. Conclude that the iteration $x_{n+1} = f(x_n)$ from any seed $x_0 \in [0, 1]$ converges to the unique fixed point $x^* \in (0, 1)$ — the *Dottie number*, which is also the unique solution to $x = \cos x$ on $[0, 1]$.

---

## 6. The Connections Web

Existence / uniqueness conditions connect to nearly every later archetype and to substantial parts of every quantitative discipline.

### 6.1 Existence and Uniqueness Across Mathematical Domains

*Real analysis.* The *Bolzano-Weierstrass theorem* (every bounded sequence has a convergent subsequence) is a non-constructive *existence* theorem on the structure of $\mathbb R$. The *Heine-Borel theorem* (closed and bounded $\subset \mathbb R$ iff compact) is a *characterisation* theorem with existence-uniqueness content (every open cover has a finite subcover). The *uniform-continuity* theorem (continuous functions on compact sets are uniformly continuous) is an existence statement on the modulus of continuity.

*Complex analysis.* The *fundamental theorem of algebra* (every non-constant polynomial with complex coefficients has a complex root) is the foundational existence theorem of complex analysis. *Liouville's theorem* (bounded entire functions are constant) is a uniqueness statement (the only bounded entire functions are the constants). *The Cauchy integral formula* gives both existence (of analytic continuations) and uniqueness (analytic functions agreeing on an open set agree everywhere on their connected domain).

*Functional analysis.* The *Hahn-Banach theorem* gives existence of continuous linear extensions of bounded linear functionals. The *Banach-Steinhaus / uniform boundedness principle* gives uniform-bound existence for families of pointwise-bounded operators. The *open mapping theorem* and *closed graph theorem* are existence-uniqueness theorems for bounded inverses. The *Riesz representation theorem* characterises continuous linear functionals on $L^p$ spaces — existence of a representing function and uniqueness up to almost-everywhere equivalence.

*Algebraic structures.* *Group theory*: the existence and uniqueness of *quotients*, of *direct sums*, of *free groups* on given generators. *Ring theory*: existence and uniqueness of *factorisations* (the fundamental theorem of arithmetic and its UFD generalisations). *Field theory*: existence and uniqueness of *algebraic closures* (every field has a unique algebraic closure up to isomorphism).

*Topology.* *Brouwer's fixed-point theorem* and its generalisations (Kakutani, Schauder, Lefschetz). *The Borsuk-Ulam theorem* (every continuous map $S^n \to \mathbb R^n$ has a pair of antipodal points with the same image). *Tychonoff's theorem* (the product of compact spaces is compact, a maximally non-constructive existence theorem requiring the axiom of choice). *The classification of surfaces* (a foundational uniqueness result up to homeomorphism).

### 6.2 Existence and Uniqueness in Physics, Engineering, and Beyond

*Classical mechanics.* The Picard-Lindelöf theorem applied to $F = ma$ gives the unique trajectory of a point particle from given initial conditions. *Hamilton's least-action principle* gives existence of physical trajectories as extrema of the action functional. *Liouville's theorem in Hamiltonian mechanics* (the phase-space volume is conserved under Hamiltonian flow) is a *uniqueness* statement on the flow's volume-preservation.

*Quantum mechanics.* The Schrödinger equation has unique solutions for given initial data (under appropriate self-adjointness hypotheses on the Hamiltonian). *Eigenvalue existence* for the time-independent Schrödinger equation is a *spectral existence* theorem; *eigenvalue multiplicity* is a uniqueness question on the eigenspace dimension.

*Statistical mechanics.* The *Gibbs-distribution uniqueness theorem*: for a system with a given Hamiltonian and a given temperature, the equilibrium distribution is the unique distribution maximising entropy subject to the energy constraint (equivalently, the unique fixed point of the inverse-temperature evolution). *Phase-transition existence* (the existence of multiple Gibbs measures at a critical temperature) is a non-uniqueness phenomenon.

*Engineering.* Every successful engineering design rests on existence and uniqueness of the designed object: a structural design must *exist* (be buildable) and be *unique* (have a definite performance profile). The opening vignette's ISRO and BARC engineers exemplify the discipline.

*Economics and game theory.* *Nash's theorem* (every finite game has at least one Nash equilibrium in mixed strategies — existence via Brouwer's fixed-point). *Arrow-Debreu* (every Walrasian-equilibrium economy has at least one equilibrium price vector under suitable convexity hypotheses — existence via Kakutani). *Uniqueness* of equilibrium typically requires additional hypotheses (gross substitutability for prices, strict concavity for preferences).

*Computer science.* The *halting problem* (does a given Turing machine halt on a given input?) is the foundational *undecidable* existence question. *Type inference* (does a well-typed assignment exist for a given program?) is an existence question that is decidable for some type systems and undecidable for others (e.g., undecidable for ML's full polymorphism). *Termination analysis* (does the program terminate on all inputs?) is an existence-of-bound question.

### 6.3 Cross-Domain Manifestations

*Information theory.* *Shannon's source-coding theorem*: there exists a code with rate arbitrarily close to the entropy. *Shannon's channel-coding theorem*: there exists a code with arbitrarily small error probability at rates below the channel capacity. Both are *existence* theorems; the *constructive* version (an algorithm for the code) is much harder and is the subject of the *coding-theory* literature.

*Operations research.* *Linear programming*: existence of a feasible solution (Phase I of the simplex method); existence and uniqueness of an optimal solution (under non-degeneracy hypotheses); existence of dual variables (duality theory).

*Control theory.* *Existence of stabilising controllers* (the *controllability* of a system); *uniqueness of stable trajectories* (Lyapunov's stability theorems); *existence of optimal controllers* (the *Hamilton-Jacobi-Bellman* equation has solutions under suitable hypotheses).

*Architecture and design.* *Existence of feasible designs* satisfying all specifications; *uniqueness up to symmetry* (a tower may be unique up to reflection / rotation). *Constructibility* (does an instrument or construction *exist* given the available tools and materials?).

### 6.4 Related Archetypes

Existence / uniqueness conditions interact with five other archetypes in particularly tight ways.

- **Archetype 1 (Invariance).** Existence theorems often rest on the *invariance* of a structural feature (the connectedness preserved by continuous maps, the boundedness preserved by compact images). The IVT is a statement about the *invariance* of the property "contains a zero" under continuous deformation of the function.

- **Archetype 9 (Domain Constraints).** Existence is a domain-constraint question (*does there exist $x$ in the admissible domain $D$ satisfying $P(x)$?*). The Ch. 9 candidate-filter pattern is, structurally, the existence-question pattern: the algebra generates candidates, the domain filters them, and the *existence of a non-empty filtered set* is the existence question.

- **Archetype 10 (Inequality Constraints).** The IVT is the universal *inequality-to-existence* converter: a sign change (inequality at the endpoints) implies existence of a zero (equality at the interior). Chapter 10's inequality machinery and Chapter 11's existence machinery interlock at exactly this conversion: *boundary inequalities $\Rightarrow$ interior equalities*.

- **Archetype 12 (Extremal Principles).** The existence of an extremum (max or min) is a foundational existence question. The *Weierstrass extreme-value theorem* (continuous functions on compact sets attain their extrema) is the universal extremum-existence theorem; Chapter 12 systematises the location of extrema once their existence is certified.

- **Archetype 18 (Induction / Recursion).** Existence-by-construction (the constructive route) often proceeds by *induction* (build the object at each finite stage; pass to the limit) or by *recursion* (define the object recursively). Chapter 18 develops both. Banach's iteration is a recursive construction; the polynomial-root-finding algorithms are inductive on degree.

---

## 7. Master Takeaways

Seven sentences. Each one is a complete operational principle.

1. *Prove it exists before you find it. Existence and uniqueness are separable questions; many problems ask only one of the two.* (The canonical takeaway.)

2. *IVT in each gap + degree-count upper bound = exact root count for rational-sum equations with prescribed pole behaviour.* (WE1 takeaway; Form I.)

3. *Maximum-principle uniqueness: assume two solutions; at any interior extremum of their difference, the second-derivative test contradicts the equation; the difference is identically zero.* (WE2 takeaway; Form IV.)

4. *1-dim Brouwer fixed-point: define $g(x) = f(x) - x$, check sign change at endpoints, apply IVT. The theorem is named "Brouwer", not "Banach"; the proof is IVT, not contractive.* (WE3 takeaway; Form III.)

5. *Match the theorem to its hypotheses: continuity $\Rightarrow$ IVT / Brouwer; differentiability $\Rightarrow$ Rolle / MVT; contraction $\Rightarrow$ Banach; elliptic ODE / PDE $\Rightarrow$ maximum principle; additive function + continuity $\Rightarrow$ Cauchy-equation theorem.*

6. *Constructive proofs (Banach, Newton, Euclidean algorithm) build the object; non-constructive proofs (IVT, Brouwer in higher dims) merely certify it — match the route to the problem's requirements.*

7. *Many problems ask only for existence (or only for uniqueness, or only for value) — read the problem carefully and answer the question actually asked.*

---

## 8. Self-Assessment Checklist

You have absorbed Chapter 11 when, without re-opening it, you can do each of the following from memory.

- [ ] State the Intermediate Value Theorem (continuity + sign change at endpoints $\Rightarrow$ zero in between), and verify each hypothesis on a specific problem.
- [ ] State the Mean Value Theorem and Rolle's theorem; derive Rolle as the special case of MVT with equal endpoint values.
- [ ] State the 1-dim Brouwer fixed-point theorem (every continuous self-map of a closed interval has a fixed point), and prove it via IVT applied to $g(x) = f(x) - x$.
- [ ] State Banach's contraction-mapping theorem (a contractive self-map of a complete metric space has a unique fixed point, found by iteration), and distinguish it from the 1-dim Brouwer.
- [ ] State the maximum principle for second-order linear ODEs (and recall the elliptic PDE generalisation), and apply it to derive uniqueness of solutions for a boundary-value problem.
- [ ] State the Cauchy functional equation theorem (continuous solutions of $f(x + y) = f(x) + f(y)$ are $f(x) = cx$), and outline the rationals-density proof.
- [ ] Apply iterated Rolle to derive the *polynomial-derivative interlacing* property (a polynomial of degree $n$ with $n$ distinct real roots has a derivative with exactly $n - 1$ real roots, one in each gap).
- [ ] Apply IVT at $\pm \infty$ to prove the existence of a real root for every odd-degree polynomial with real coefficients.
- [ ] Identify and explain three of the five common pitfalls: the Existence-Skipped, the Uniqueness-Assumed, the Wrong-Theorem, the Constructive-Confused, the Boundary-vs-Interior pitfalls.
- [ ] Articulate, in one sentence, how Existence / Uniqueness (Ch. 11) relates to Inequality Constraints (Ch. 10) and Extremal Principles (Ch. 12): Ch. 10's inequality at the endpoints converts via IVT to Ch. 11's existence at the interior; Ch. 11's existence of an extremum is the foundational step before Ch. 12's location of the extremum.

---

## Bridge to Chapter 12: Extremal Principles

Chapter 11 closed the *existence-and-uniqueness* leg of the *Constraint Exploitation* sub-pillar (Chs. 9–12). The chapter equipped the reader with the named-theorem toolkit (IVT, Rolle, MVT, Brouwer, Banach, maximum principle, Cauchy-equation theorem), the separation principle (existence and uniqueness are independent questions), and the constructive-vs-non-constructive discernment that determines whether a proof gives an algorithm or merely a guarantee.

Chapter 12 — *Extremal Principles* — closes the *Constraint Exploitation* sub-pillar by combining the inequality machinery of Ch. 10 with the existence machinery of Ch. 11. The chapter takes the foundational observation that *every constrained optimisation problem* asks *(i) does an extremum exist?* and *(ii) where is it located?*, and develops the systematic apparatus for answering both. The named tools shift accordingly: *Weierstrass extreme-value theorem* (existence on compact sets); *interior-extremum analysis* (gradient zero in the interior); *boundary-extremum analysis* (KKT conditions for inequality-constrained problems); *symmetry-driven extremum identification* (the equality case of an inequality is at the symmetric configuration). Each is, structurally, a *bridge* between the inequality (Ch. 10) and the existence (Ch. 11) machinery, and Chapter 12 makes the bridge explicit.

With Chapter 12 in hand, the reader will have completed the *Constraint Exploitation* sub-pillar (Chs. 9–12) and will be positioned for the *Structural Reasoning* sub-pillar (Chs. 13–16), which moves from *constraints on individual problems* to *structures shared across problem families* — Counting & Combinatorial Symmetries (Ch. 13), Parity / Modular Reasoning (Ch. 14), Continuity / Topological Reasoning (Ch. 15), and Algebraic Structure Recognition (Ch. 16).

---

## Appendix — Solutions to Practice Problems

### Solution to 5.1 — Non-Differentiability of $\max\{x, x^3\}$

*Identify the crossings.* The curves $y = x$ and $y = x^3$ cross where $x = x^3$, i.e., $x(x^2 - 1) = 0$, giving $x = -1, 0, 1$ — *three* crossings.

*Determine the active branch on each subinterval.*
- For $x < -1$ (e.g., $x = -2$): $x = -2$, $x^3 = -8$; $x > x^3$, so $\max = x$.
- For $-1 < x < 0$ (e.g., $x = -0.5$): $x = -0.5$, $x^3 = -0.125$; $x^3 > x$, so $\max = x^3$.
- For $0 < x < 1$ (e.g., $x = 0.5$): $x = 0.5$, $x^3 = 0.125$; $x > x^3$, so $\max = x$.
- For $x > 1$ (e.g., $x = 2$): $x = 2$, $x^3 = 8$; $x^3 > x$, so $\max = x^3$.

The active branch switches at each of the three crossings.

*Check differentiability at each crossing.* At a crossing, the function $f = \max\{x, x^3\}$ is differentiable iff the left-derivative equals the right-derivative.

- *At $x = -1$:* Left-derivative = derivative of $x$ at $-1$ = $1$. Right-derivative = derivative of $x^3$ at $-1$ = $3 \cdot (-1)^2 = 3$. *Different; non-differentiable.*

- *At $x = 0$:* Left-derivative = derivative of $x^3$ at $0$ = $3 \cdot 0^2 = 0$. Right-derivative = derivative of $x$ at $0$ = $1$. *Different; non-differentiable.*

- *At $x = 1$:* Left-derivative = derivative of $x$ at $1$ = $1$. Right-derivative = derivative of $x^3$ at $1$ = $3 \cdot 1^2 = 3$. *Different; non-differentiable.*

The function is *non-differentiable at exactly three points*: $\boxed{x \in \{-1, 0, 1\}}$. $\blacksquare$

*Correction note.* The v0.2 locked slate stated that the function is non-differentiable at two points ($x = -1$ and $x = 0$). This is incorrect; the verification audit during this chapter's drafting identified the third non-differentiability point at $x = 1$, where the left-derivative ($1$, from $y = x$) differs from the right-derivative ($3$, from $y = x^3$). The slate is patched in v0.2.8 to reflect the three-point answer. The slip in the slate was a lookalike-of-symmetry error: the *negative* crossings ($x = -1$ and the slope change at $x = 0$) catch attention more readily than the *positive* crossing ($x = 1$), but all three are genuine non-differentiability points.

---

### Solution to 5.2 — Left-Hand Derivative of $[x]\sin(\pi x)$ at $x = k$

For $x$ slightly less than the integer $k$ (i.e., $x = k - h$ with $h \to 0^+$), the greatest-integer function gives $[x] = [k - h] = k - 1$ (since $k - 1 \le k - h < k$ for small $h > 0$). So
\[
  f(k - h) \;=\; (k - 1)\sin(\pi(k - h)) \;=\; (k - 1)\sin(\pi k - \pi h).
\]
At $x = k$ exactly: $[k] = k$ and $\sin(\pi k) = 0$, so $f(k) = k \cdot 0 = 0$.

The left-hand derivative is
\[
  f'_{-}(k) \;=\; \lim_{h \to 0^+} \frac{f(k - h) - f(k)}{(k - h) - k} \;=\; \lim_{h \to 0^+} \frac{(k - 1)\sin(\pi k - \pi h) - 0}{-h}.
\]

Use the sine-difference identity $\sin(A - B) = \sin A \cos B - \cos A \sin B$ with $A = \pi k$ and $B = \pi h$:
\[
  \sin(\pi k - \pi h) \;=\; \sin(\pi k)\cos(\pi h) - \cos(\pi k)\sin(\pi h) \;=\; 0 - (-1)^k \sin(\pi h) \;=\; -(-1)^k \sin(\pi h).
\]
(We used $\sin(\pi k) = 0$ and $\cos(\pi k) = (-1)^k$ for integer $k$.)

Substituting:
\[
  f'_{-}(k) \;=\; \lim_{h \to 0^+} \frac{(k - 1) \cdot \big(-(-1)^k \sin(\pi h)\big)}{-h} \;=\; (k - 1)(-1)^k \lim_{h \to 0^+} \frac{\sin(\pi h)}{h}.
\]

The standard limit $\lim_{h \to 0} \frac{\sin(\pi h)}{h} = \pi$. Hence
\[
  \boxed{f'_{-}(k) \;=\; (-1)^k (k - 1) \pi.}
\]
$\blacksquare$

*Sign-check.* For $k = 1$: $f'_{-}(1) = -1 \cdot 0 \cdot \pi = 0$. Verify: for $x$ slightly less than $1$, $[x] = 0$, so $f(x) = 0 \cdot \sin(\pi x) = 0$; the left-derivative is $0$. ✓

For $k = 2$: $f'_{-}(2) = (+1)(1)\pi = \pi$. For $x$ slightly less than $2$, $[x] = 1$, so $f(x) = \sin(\pi x)$; $f'(x) = \pi\cos(\pi x)$; $f'(2^-) = \pi \cos(2\pi^-) = \pi \cdot 1 = \pi$. ✓

---

### Solution to 5.3 — Number of Solutions of $\log_4(x - 1) = \log_2(x - 3)$

*Convert to a common base.* Use $\log_4 t = \frac{\log_2 t}{\log_2 4} = \frac{1}{2}\log_2 t$:
\[
  \frac{1}{2} \log_2(x - 1) \;=\; \log_2(x - 3) \quad\Longrightarrow\quad \log_2(x - 1) \;=\; 2 \log_2(x - 3) \;=\; \log_2 (x - 3)^2.
\]
Since $\log_2$ is one-to-one (where defined), this gives
\[
  x - 1 \;=\; (x - 3)^2 \;=\; x^2 - 6x + 9.
\]
Rearranging: $x^2 - 7x + 10 = 0$, factoring: $(x - 2)(x - 5) = 0$. Candidate solutions: $x = 2$ and $x = 5$.

*Domain filter.* Both logarithms must have positive arguments:
\[
  x - 1 > 0 \text{ AND } x - 3 > 0, \quad\text{i.e.,}\quad x > 3.
\]
Among the candidates: $x = 2$ fails ($2 < 3$), $x = 5$ passes ($5 > 3$).

*Existence.* The candidate $x = 5$ is the unique solution: substitute back: $\log_4(5 - 1) = \log_4 4 = 1$; $\log_2(5 - 3) = \log_2 2 = 1$. ✓

There is *exactly one* solution: $\boxed{x = 5}$. $\blacksquare$

*Existence-and-uniqueness reading.* The algebraic step (squaring or equivalently raising to $\log_2$) is *not reversible*: it potentially introduces *extraneous candidates*. The candidate $x = 2$ is extraneous (it satisfies the squared equation but not the original equation, because $x - 3 < 0$ at $x = 2$ and the original $\log_2(x - 3)$ is undefined). The domain filter is what *enforces uniqueness*: among the two algebraic candidates, only one is in the natural domain.

---

### Solution to 5.4 — Cauchy Functional Equation Uniqueness

*Step 1 — Compute $f$ on the integers.* Setting $x = y = 0$: $f(0 + 0) = f(0) + f(0)$, so $f(0) = 0$. Setting $y = -x$: $f(0) = f(x) + f(-x)$, so $f(-x) = -f(x)$ — $f$ is *odd*. Setting $x = y = z$ and iterating: $f(2z) = f(z) + f(z) = 2f(z)$, $f(3z) = f(z + 2z) = f(z) + 2f(z) = 3f(z)$, and by induction $f(nz) = n f(z)$ for every positive integer $n$ and every real $z$. Extending to negative $n$ via oddness, $f(nz) = nf(z)$ for every integer $n$.

*Step 2 — Compute $f$ on the rationals.* Let $c = f(1)$. By step 1, $f(n) = n c$ for every integer $n$. For a positive integer $m$ and the rational $1/m$: by step 1 applied with $z = 1/m$, $f(m \cdot (1/m)) = m \cdot f(1/m)$, i.e., $f(1) = m f(1/m)$, so $f(1/m) = c/m$. For a general rational $p/q$ with $p \in \mathbb Z, q \in \mathbb Z_{>0}$: $f(p/q) = f(p \cdot (1/q)) = p f(1/q) = p \cdot (c/q) = c \cdot (p/q)$. Hence $f(r) = c r$ for every rational $r$.

*Step 3 — Extend to the reals by continuity.* Fix $x \in \mathbb R$. By the density of $\mathbb Q$ in $\mathbb R$, there exists a sequence $(r_n)$ of rationals with $r_n \to x$. By continuity of $f$:
\[
  f(x) \;=\; f\left(\lim_{n \to \infty} r_n\right) \;=\; \lim_{n \to \infty} f(r_n) \;=\; \lim_{n \to \infty} c \, r_n \;=\; c \cdot \lim_{n \to \infty} r_n \;=\; c \cdot x.
\]
Hence $f(x) = cx$ for all $x \in \mathbb R$. $\blacksquare$

*Why continuity is essential.* Without the continuity hypothesis, the Cauchy functional equation has *uncountably many* non-linear solutions (constructed via a *Hamel basis* of $\mathbb R$ over $\mathbb Q$, requiring the axiom of choice). Continuity is what *forces uniqueness* among the wildly-many additive functions; the topological constraint is the source of structure.

---

### Solution to 5.5 — Polynomial-Derivative Interlacing via Rolle

Let $f(x)$ be a polynomial of degree $n$ with $n$ distinct real roots $r_1 < r_2 < \cdots < r_n$.

*Step 1 — Existence of derivative roots via Rolle.* Fix $i \in \{1, 2, \ldots, n - 1\}$. The function $f$ is a polynomial, hence continuous and differentiable everywhere. The values $f(r_i) = f(r_{i+1}) = 0$ are equal. By *Rolle's theorem* applied to $f$ on the interval $[r_i, r_{i+1}]$, there exists $s_i \in (r_i, r_{i+1})$ with $f'(s_i) = 0$.

Hence $f'$ has *at least one* zero in each of the $n - 1$ gaps $(r_i, r_{i+1})$ for $i = 1, \ldots, n - 1$. Total: *at least* $n - 1$ zeros of $f'$.

*Step 2 — Degree-count upper bound on derivative roots.* The derivative $f'$ is a polynomial of degree $n - 1$, which has *at most* $n - 1$ real roots (counting multiplicity, but for *distinct* real roots, exactly at most $n - 1$).

*Step 3 — Combining.* From step 1, at least $n - 1$ distinct real roots of $f'$ (one in each gap, all distinct). From step 2, at most $n - 1$. Hence *exactly* $n - 1$ distinct real roots of $f'$, one in each gap $(r_i, r_{i+1})$.

The roots of $f'$ all lie in the open interval $(r_1, r_n)$, the *convex hull* of the roots of $f$. $\blacksquare$

*The interlacing property.* The roots of $f'$ *interlace* with the roots of $f$:
\[
  r_1 \;<\; s_1 \;<\; r_2 \;<\; s_2 \;<\; r_3 \;<\; \cdots \;<\; s_{n-1} \;<\; r_n.
\]
The interlacing is a foundational property of *orthogonal polynomials* (the zeros of consecutive orthogonal polynomials interlace) and of *spectral theory* (the eigenvalues of a symmetric matrix interlace with those of its principal submatrices).

---

### Solution to 5.6 — Odd-Degree Polynomial Has a Real Root

Let $f(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0$ with $a_n \ne 0$ and $n$ odd. WLOG assume $a_n > 0$ (else replace $f$ by $-f$, which has the same zeros).

*Behaviour as $x \to \pm \infty$.* The leading term $a_n x^n$ dominates as $|x|$ grows. Since $n$ is odd and $a_n > 0$:
- As $x \to +\infty$: $a_n x^n \to +\infty$ (positive value of a positive coefficient times a large positive odd-power); hence $f(x) \to +\infty$.
- As $x \to -\infty$: $a_n x^n \to -\infty$ (negative value of a positive coefficient times a large negative odd-power, since odd power preserves sign); hence $f(x) \to -\infty$.

*Application of IVT.* By the divergence to $\pm \infty$, there exist real numbers $A < 0 < B$ with $f(A) < 0$ and $f(B) > 0$. The polynomial $f$ is continuous on $[A, B]$ (every polynomial is continuous everywhere). By the Intermediate Value Theorem, there exists $c \in (A, B)$ with $f(c) = 0$.

Hence every polynomial of odd degree with real coefficients has at least one real root. $\blacksquare$

*Sharpness.* The result is sharp in the sense that *odd degree* is essential. The polynomial $x^2 + 1$ (even degree) has no real roots. The polynomial $x^4 + 1$ (even degree) has no real roots. The polynomial $x^3 - 6x^2 + 11x - 6 = (x - 1)(x - 2)(x - 3)$ (odd degree) has *three* real roots; the polynomial $x^3 - x = x(x - 1)(x + 1)$ has three real roots. The result *only guarantees at least one*; the actual count can be 1, 3, 5, ..., up to $n$.

---

### Solution to 5.7 — Dottie Number as a Banach Fixed Point

*Step 1 — Verify $f$ maps $[0, 1]$ into $[0, 1]$.* Compute the values at the endpoints:
- $f(0) = (0 + \cos 0)/2 = (0 + 1)/2 = 1/2 \in [0, 1]$.
- $f(1) = (1 + \cos 1)/2 \approx (1 + 0.5403)/2 \approx 0.770 \in [0, 1]$.

For monotonicity, $f'(x) = (1 - \sin x)/2$. On $[0, 1]$, $\sin x \in [0, \sin 1] \approx [0, 0.841]$, so $1 - \sin x \in [0.159, 1]$, so $f'(x) \in [0.080, 0.5]$. In particular $f' \ge 0$ on $[0, 1]$, so $f$ is non-decreasing. Thus $f([0, 1]) \subseteq [f(0), f(1)] \subseteq [1/2, 0.77] \subseteq [0, 1]$. The self-map property is verified.

*Step 2 — Verify $f$ is a contraction.* By the mean value theorem, for any $x, y \in [0, 1]$ there exists $\xi$ between $x$ and $y$ with
\[
  |f(x) - f(y)| \;=\; |f'(\xi)| \cdot |x - y| \;=\; \frac{|1 - \sin\xi|}{2} \cdot |x - y|.
\]
Since $\sin\xi \in [0, 1]$ for $\xi \in [0, 1]$, $1 - \sin\xi \in [0, 1]$, so $|1 - \sin\xi|/2 \le 1/2$. Hence
\[
  |f(x) - f(y)| \;\le\; \frac{1}{2} |x - y|.
\]
$f$ is a contraction with Lipschitz constant $k = 1/2 < 1$.

*Step 3 — Apply Banach's contraction-mapping theorem.* The interval $[0, 1]$ with the standard metric is *complete* (closed subset of $\mathbb R$). $f : [0, 1] \to [0, 1]$ is a contraction. By *Banach's contraction-mapping theorem*, $f$ has a *unique* fixed point $x^* \in [0, 1]$, and the iteration $x_{n+1} = f(x_n)$ from any seed $x_0 \in [0, 1]$ converges to $x^*$ geometrically (at rate $1/2$ per iteration, so error bound $|x_n - x^*| \le (1/2)^n |x_0 - x^*|$).

*Step 4 — Identify the fixed point.* The fixed-point equation is
\[
  x^* \;=\; f(x^*) \;=\; \frac{x^* + \cos x^*}{2} \quad\Longleftrightarrow\quad 2 x^* \;=\; x^* + \cos x^* \quad\Longleftrightarrow\quad x^* \;=\; \cos x^*.
\]
This is the famous *Dottie equation*, whose unique real solution is the *Dottie number*,
\[
  \boxed{x^* \;\approx\; 0.7390851332151607.}
\]
$\blacksquare$

*Numerical demonstration.* Starting from $x_0 = 0$:
\begin{align*}
  x_1 &= f(0) = 0.500000 \\
  x_2 &= f(0.500000) = (0.500 + \cos 0.500)/2 = (0.500 + 0.8776)/2 = 0.6888 \\
  x_3 &= f(0.6888) = (0.6888 + \cos 0.6888)/2 = (0.6888 + 0.7717)/2 = 0.7303 \\
  x_4 &= f(0.7303) = (0.7303 + 0.7448)/2 = 0.7375 \\
  x_5 &= f(0.7375) = (0.7375 + 0.7400)/2 = 0.7388 \\
  x_6 &= f(0.7388) = (0.7388 + 0.7391)/2 = 0.7390 \\
\end{align*}
Convergence at rate $(1/2)$ per iteration. The fixed point is approached rapidly.

*Constructive vs non-constructive.* Banach's theorem is *constructive*: the iteration $x_{n+1} = f(x_n)$ explicitly *builds* the fixed point as the limit of the sequence, with quantitative convergence bounds. This is in contrast to the *Brouwer* (or 1-dim Brouwer) fixed-point theorem of WE3, which gives only *existence* without a construction. The contraction hypothesis is what enables the constructive identification.

---

*End of Chapter 11.*

