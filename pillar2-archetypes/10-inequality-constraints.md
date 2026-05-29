---
chapter: 10
archetype: Inequality Constraints
subtitle: "Sometimes the Bounds Tell the Whole Story"
category: Constraint Exploitation (Archetypes 9–12) — second chapter
related_archetypes: [2, 7, 9, 12, 17]
key_gems: [B01, B02, B03, B04, B05, B06, B07, B08, B09, B10, B11, B13, B14, B15, F12]
  - "AM-GM: $\\dfrac{a_1 + \\cdots + a_n}{n} \\ge \\sqrt[n]{a_1 \\cdots a_n}$ for non-negative reals, equality iff $a_1 = \\cdots = a_n$"
  - "Cauchy-Schwarz: $\\left(\\sum a_i b_i\\right)^2 \\le \\left(\\sum a_i^2\\right)\\left(\\sum b_i^2\\right)$, equality iff $(a_i)$ and $(b_i)$ are proportional"
  - "Jensen's inequality: for convex $f$ on an interval $I$ and $\\lambda_i \\ge 0$ with $\\sum\\lambda_i = 1$, $f\\left(\\sum\\lambda_i x_i\\right) \\le \\sum\\lambda_i f(x_i)$ (reverse for concave)"
  - "Power-Mean ladder: $M_{-\\infty} \\le M_{-1}\\text{ (HM)} \\le M_0\\text{ (GM)} \\le M_1\\text{ (AM)} \\le M_2\\text{ (QM)} \\le M_\\infty$"
  - "Rearrangement inequality: for sorted sequences $(a_i)$, $(b_i)$, the sum $\\sum a_i b_{\\sigma(i)}$ is maximised by same-order pairing and minimised by reverse-order"
  - "Chebyshev's sum inequality: $\\dfrac{1}{n}\\sum a_i b_i \\ge \\left(\\dfrac{1}{n}\\sum a_i\\right)\\left(\\dfrac{1}{n}\\sum b_i\\right)$ for similarly-ordered sequences"
  - "Schur's inequality: $a^t(a-b)(a-c) + b^t(b-c)(b-a) + c^t(c-a)(c-b) \\ge 0$ for $a, b, c \\ge 0$ and $t \\ge 0$; the $t = 2$ case is the most common"
  - "Ravi substitution: a triangle with sides $a, b, c$ admits the parametrisation $a = y + z$, $b = z + x$, $c = x + y$ with $x, y, z > 0$ that converts the triangle-inequality constraint into the unconstrained positivity of $x, y, z$"
  - "SOS (Sum-of-Squares) decomposition: every symmetric inequality $P(a, b, c) \\ge 0$ that is true and *sharp* admits, after suitable manipulation, an expression as a sum of squares of polynomials in $a - b, b - c, c - a$"
  - "Equality-case principle: the equality case of a tight inequality often *characterises* the extremum, turning a maximisation problem into an algebraic equation"
canonical_takeaway: "Inequalities are not obstacles; they are constraints that determine the answer. The equality case is the answer."
status: locked
last_revised: 2026-05-29
locked_on: 2026-05-29
sourcing_note: "All worked examples and practice problems in this chapter are drawn from K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), or from JEE / RMO / INMO / IMO examinations commented on in that text. See Blueprint §6.2 for the sourcing rule and `pillar2-archetypes/_template/joshi-problems-locked.md` §Ch. 10 for the locked slate. **Two explicit cross-archetype reuses are flagged in the front matter:** (a) WE1 (RMO triangle-inequality bound, Joshi Ex. 24.65) was previously drafted as Ch. 9 WE3 under the *domain-constraint* framing; here it is reframed as an *inequality-constraint* problem via the Ravi substitution. (b) WE3 (INMO + IMO 2000, Joshi Ex. 24.66) was previously drafted as Ch. 2 PP7 under the *symmetry* framing; here it is reframed via Jensen + Vasile-Cirtoaje substitution. (c) PP3 (JEE 2001 cos-product, Joshi Ex. 24.27) was previously drafted as Ch. 7 WE3 under the *normalisation* framing; here it appears as a practice problem with a cross-reference. All three cross-reuses are documented in slate v0.2.7 and conform to Blueprint §6.4 (cross-archetype reuse is permitted with explicit cross-referencing when the cognitive framing differs)."
---

# Chapter 10 — Inequality Constraints

## *Sometimes the Bounds Tell the Whole Story*

---

## Opening Vignette

A structural engineer in Mumbai is designing the steel columns for a new metro station. Each column must support an axial compressive load of $1.2 \text{ MN}$ (mega-newtons), and her client has asked for the lightest column section that will do the job. The temptation is to compute the *area* of steel needed to take the load by simple yield strength: $A = P/\sigma_y = 1.2 \times 10^6 / 250 \times 10^6 = 0.0048\,\text{m}^2 = 48\,\text{cm}^2$, a comfortably small cross-section. But she does not write the specification for $48\,\text{cm}^2$. She knows that a long, slender steel column can fail not by *yielding* (the material is overstressed) but by *buckling* (the column bends sideways out of axial alignment under the load), and that the buckling load is given by *Euler's formula* $P_{cr} = \pi^2 E I / (k L)^2$, where $E$ is the Young's modulus, $I$ is the area moment of inertia of the section, $L$ is the column length, and $k$ is the end-condition factor. Her column is $6\,\text{m}$ tall and pinned at both ends ($k = 1$), and she needs $P \le P_{cr}$, i.e., $I \ge P (kL)^2 / (\pi^2 E)$. Plugging in: $I \ge 1.2 \times 10^6 \cdot (6)^2 / (\pi^2 \cdot 200 \times 10^9) \approx 2.19 \times 10^{-5}\,\text{m}^4 = 2190\,\text{cm}^4$. A solid square section of side $a$ has $I = a^4/12$, giving $a^4 \ge 26{,}280\,\text{cm}^4$, so $a \ge 12.7\,\text{cm}$ — a much larger section than the $48\,\text{cm}^2$ yield-only estimate suggested. Her optimal design is the section that *just satisfies the buckling inequality at equality*: $a \approx 12.7\,\text{cm}$. Any smaller section buckles and fails; any larger section wastes material. The inequality $P \le P_{cr}$ is not an obstacle to be circumvented; *it is the equation whose equality case locates the design point*. The trained engineer reads the inequality as a *design equation* — and the inequality's equality case as *the answer*.

Now turn to a different scene. A second-year mathematics undergraduate at IIT Madras is asked, in her first analysis class, to prove the *arithmetic-mean-geometric-mean inequality* for two positive reals: *for $a, b > 0$, the arithmetic mean is at least the geometric mean*, i.e., $\frac{a + b}{2} \ge \sqrt{ab}$. She stares at it. Where is the equation to solve? Where is the unknown? There is no equation; there is no unknown. There is only an *inequality to prove*. She remembers a hint from a tutorial: *consider the square*. She writes $(\sqrt a - \sqrt b)^2 \ge 0$ — a trivially true statement, since every square of a real number is non-negative. She expands: $a - 2\sqrt{ab} + b \ge 0$. She rearranges: $a + b \ge 2\sqrt{ab}$, i.e., $\frac{a + b}{2} \ge \sqrt{ab}$. The proof is one line. The inequality *is* the result; the equality case ($a = b$) is the *characterisation* of when the arithmetic and geometric means coincide. The trained mathematician sees AM-GM not as a *fact to memorise* but as a *tool to deploy*: whenever two positive quantities arise in a problem, AM-GM bounds their arithmetic mean below by their geometric mean, and the equality case identifies the *symmetric configuration* as the extremiser. From AM-GM follow Cauchy-Schwarz, Jensen, the power-mean inequalities, rearrangement, Chebyshev, Schur — the entire ladder of *inequality machinery* that competition mathematics deploys with such effect.

These two scenes look unrelated. A structural engineer specifying a column; a mathematics student proving AM-GM. They share the most important reframing in the entire chapter — and one that JEE-level students typically resist for years before internalising. *The structural engineer's design point is at the binding constraint*; *the mathematics student's equality case is at the symmetric configuration*; *both are the equality case of an inequality, and both are the answer*. Inequalities are not the *background condition* of a problem; they are the *engine* of the answer. Chapter 9 introduced this idea in its most general form (domain constraints filter the candidate set); the present chapter takes the *most common kind of constraint* — the inequality — and elevates it to a full archetype, equipping the reader with the named machinery (AM-GM, Cauchy-Schwarz, Jensen, Chebyshev, Schur, Ravi) that competition mathematics has codified over a century.

The chapter has three structural threads. The first is the *toolkit*: a working knowledge of the named inequalities and when to deploy them. The second is the *equality-case principle*: the recognition that the equality case of a tight inequality is the *answer* to the optimisation problem it bounds. The third is the *cross-archetype connection*: the recognition that the triangle inequality (Ch. 9), the normalisation transform (Ch. 7), the symmetry reduction (Ch. 2), and the extremal principle (Ch. 12) are *all* manifestations of the same underlying inequality-constraint machinery, viewed from different sides.

> *Inequalities are not obstacles; they are constraints that determine the answer. The equality case is the answer.*

---

## 1. The Archetype Defined

### 1.1 Formal Definition

We make the intuition precise.

\begin{definition}[Inequality Constraint]
An *inequality constraint* on a problem with variables $x_1, \ldots, x_n$ in a domain $D$ is a relation of the form $g(x_1, \ldots, x_n) \le 0$ (or $<$, $\ge$, $>$) that restricts the admissible set further than $D$. A problem *deploys* an inequality constraint when it (i) imposes an inequality as part of its statement; (ii) uses an inequality (AM-GM, Cauchy-Schwarz, Jensen, etc.) as a *step* in its proof; or (iii) asks to *prove* an inequality as the final answer.
\end{definition}

Three remarks unpack the definition. First, every inequality constraint is also a *domain constraint* in the sense of Chapter 9; the present chapter specialises that general framework to the case where the constraints are *inequalities*, and exhibits the rich machinery (AM-GM, Cauchy-Schwarz, Jensen, ...) that has been developed specifically for inequalities.

Second, every inequality constraint has an *equality case*: the set of points where the inequality is tight ($g = 0$). The equality case is typically a lower-dimensional subset of the admissible set, and it is often the *answer* to an optimisation problem: *the maximum of $f$ subject to $g \le 0$ is attained on the equality case $g = 0$* (the *binding* constraint principle). This is the *equality-case principle* — the most important pedagogical move of the chapter, and the one that converts the inequality from a *passive bound* into the *active locator* of the extremum.

Third, the *direction* of the inequality matters. *Upper bounds* ($f \le M$) and *lower bounds* ($f \ge m$) play structurally different roles. An optimisation problem *maximise $f$ subject to $g \le 0$* uses the binding upper-bound on $g$ to bound $f$ from above (typically by Lagrange-multiplier or convex-duality machinery); the maximum is achieved at the equality case of $g$. The dual *minimise $f$ subject to $g \ge 0$* uses the binding lower-bound. Most JEE-level problems have a small number of constraints, and the structure is easy to navigate; competition problems (RMO, INMO, IMO) often have many constraints, and the binding-constraint analysis becomes the central skill.

The chapter encounters five characteristic forms of inequality constraint.

- **Form I — Symmetric polynomial inequalities (AM-GM family).** *Symmetric* polynomials in $n$ variables (those invariant under permutation) admit a battery of inequalities whose equality cases are at the *symmetric configuration* $x_1 = \cdots = x_n$. The prototypes are AM-GM, the power-mean inequality, Chebyshev's sum inequality, the Newton-Maclaurin inequalities on elementary symmetric polynomials. *Examples.* WE3 (IMO 2000 product $\le 1$), PP2 (quadratic minimum), PP3 (cos-product), PP4 (right-triangle $R \ge (1+\sqrt 2)r$).

- **Form II — Cauchy-Schwarz and Hilbert-space inequalities.** Cauchy-Schwarz on $\mathbb R^n$ (or any inner product space) is the master inequality of vector / sequence analysis, and its specialisations (Bunyakovsky's integral form, the triangle inequality on $L^2$) cover an enormous range of problems. *Examples.* PP1 (three unit vectors), PP6 (Pedoe's inequality).

- **Form III — Jensen's inequality and convexity.** A convex function $f$ on an interval $I$ satisfies $f\left(\sum\lambda_i x_i\right) \le \sum\lambda_i f(x_i)$ for $\lambda_i \ge 0, \sum\lambda_i = 1$. The inequality bounds the *value at the average* by the *average of the values*, and its equality case is at the *linear* (degenerate) configurations. *Examples.* WE3 part (i) (Jensen on $t \ln t$), PP6 (Pedoe via Jensen-style argument).

- **Form IV — Triangle and Ravi-substitution inequalities.** Inequalities involving the sides of a triangle (or, more generally, parameters constrained by the triangle inequality) admit the *Ravi substitution* $a = y + z$, $b = z + x$, $c = x + y$ with $x, y, z > 0$, which converts the triangle constraint into the *unconstrained positivity* of $x, y, z$. The resulting unconstrained inequality is then handled by Form I–III machinery. *Examples.* WE1 (the triangle-inequality bound, reframed), PP5 (Hadwiger-Finsler), PP4 (right-triangle bound).

- **Form V — Rearrangement and Chebyshev inequalities.** *Sorted* sequences admit *rearrangement* inequalities: $\sum a_i b_{\sigma(i)}$ is maximised when $\sigma$ pairs the sequences in the *same* order and minimised in the *opposite* order. Chebyshev's sum inequality is the immediate corollary. *Examples.* WE2 (JEE 1972 bounded-ratio, via direct expansion and rearrangement), PP7 (cotangent sum).

### 1.2 The Core Principle

Stripped to its essence, the principle of inequality constraints is one sentence.

> *Inequalities are not obstacles; they are constraints that determine the answer. The equality case is the answer.*

This sentence reframes inequalities at every level of the problem. *Pedagogically*: the student who sees an inequality on the page often treats it as a *side condition* to be respected ("OK, $a + b + c \le 1$, got it") rather than as an *active tool* ("OK, this means the *only* way to get $a + b + c$ to its maximum is $a + b + c = 1$, with the further machinery of AM-GM / Jensen / etc. then telling me *what equality $a = b = c = 1/3$ looks like*"). The reframing converts the inequality from background to foreground.

*Operationally*: the equality-case principle says that the optimum of an inequality-bounded quantity is attained at the *binding* equality. The discipline is to *identify which inequality binds at the optimum*, and to read the binding equality as the *algebraic equation* characterising the optimum. AM-GM binds at $a = b = c = \cdots$; Cauchy-Schwarz binds at $a_i = \lambda b_i$ for some constant $\lambda$; Jensen binds at the *constant* (degenerate) configuration; rearrangement binds at the *same-order* (or *reverse-order*) pairing; the triangle inequality binds at the *degenerate* triangle. *Reading the binding equality is reading the answer*.

*Cross-archetype*: inequalities are the most common kind of constraint, and the inequality-constraint discipline subsumes most of what Chapters 9 (Domain Constraints), 7 (Normalization), 2 (Symmetry), and 12 (Extremal Principles) develop. The present chapter is the *named-tools* version — the version that supplies the labels (AM-GM, Cauchy-Schwarz, Jensen, ...) and tells the solver which tool to deploy when.

### 1.3 The Cognitive Shift

Three cognitive shifts deserve naming.

The first is the *equality-case reading*. The trained solver, upon seeing an inequality, immediately asks *what configuration makes this equality?* — and reads that configuration as the *candidate optimum*. This shift converts inequality-proof problems into algebraic-equation-solving problems on the equality case, then verifies that the candidate is indeed the optimum. The pattern: *guess by equality, prove by inequality.*

The second shift is *named-tool selection*. The inequality toolkit has grown over the 20th century into a substantial library: AM-GM, Cauchy-Schwarz, Jensen, Chebyshev, rearrangement, power-mean, Schur, Muirhead, Bernoulli, Young, Hölder, Minkowski, Hardy, Hilbert, Carleman, Kantorovich. The trained solver knows the first eight by name and by deployment signature: *which inequality applies to which structural pattern in the problem*. AM-GM for *sum vs product*; Cauchy-Schwarz for *bilinear sums*; Jensen for *convex functions*; rearrangement for *sorted sequences*; Schur for *symmetric polynomials with a positivity constraint*. The toolkit is a *menu*, and selection is fast when the problem's structure is well read.

The third shift is *the conversion principle*. Many problems with an *equation* in their statement admit a more powerful framing with an *inequality*. The classic example is *find the maximum of $f$ subject to $g = c$*: by Lagrange multipliers, the maximum is attained at a critical point of $f - \lambda g$; but equivalently, by the inequality machinery, $f$ is bounded above by some expression in $c$ and the bound is sharp at the symmetric (or specifically-characterised) configuration. The two routes give the same answer; the inequality route is often shorter, more elementary, and more pedagogically illuminating. The conversion *equality $\to$ inequality* is one of the most consequential moves in the trained solver's repertoire.

---

## 2. The Deep Structure

### 2.1 Mathematical Foundations

Inequality constraints rest on four mathematical foundations.

The first is the *positivity of squares*. Every real number's square is non-negative: $x^2 \ge 0$, with equality iff $x = 0$. This trivial fact is the root of the entire inequality apparatus. *AM-GM for two variables*: $(\sqrt a - \sqrt b)^2 \ge 0 \Rightarrow a + b \ge 2\sqrt{ab}$. *Cauchy-Schwarz for two pairs*: $(a_1 b_2 - a_2 b_1)^2 \ge 0 \Rightarrow (a_1^2 + a_2^2)(b_1^2 + b_2^2) \ge (a_1 b_1 + a_2 b_2)^2$. *Schur*: a more involved positivity-of-a-sum-of-squares argument. *Hadwiger-Finsler*: reduces (under Ravi) to $(xy + yz + zx)^2 \ge 3xyz(x + y + z)$, itself a sum-of-squares. The pattern *positivity of a square $\Rightarrow$ inequality* is the foundation, and the *SOS (sum-of-squares) decomposition* is the systematic version: every symmetric inequality that is true and *sharp* admits an SOS proof.

The second foundation is *convexity*. A function $f$ on an interval $I$ is *convex* if the chord from $(a, f(a))$ to $(b, f(b))$ lies above the graph for every $a, b \in I$; equivalently, $f''(x) \ge 0$ everywhere $f$ is twice-differentiable. Convexity is the *master property* for Jensen's inequality and its descendants. The exponential function $e^x$, the power function $x^p$ for $p \ge 1$, the function $x \ln x$ on $(0, \infty)$, the negative logarithm $-\ln x$ on $(0, \infty)$, and the absolute-value function $|x|$ are all convex; their *Jensen consequences* (Bernoulli, AM-GM in its weighted form, the entropy inequality) follow immediately. The cognitive move: *recognise the convex / concave function buried in the problem, apply Jensen, read off the inequality.*

The third foundation is the *ordering of means*. For non-negative reals $a_1, \ldots, a_n$ and exponent $p \in \mathbb R$, define the *$p$-th power mean* by
\[
  M_p \;=\; \left(\frac{1}{n}\sum_{i=1}^n a_i^p\right)^{1/p} \quad (p \ne 0), \qquad M_0 \;=\; \sqrt[n]{a_1 \cdots a_n} \text{ (GM, the limit as } p \to 0\text{)}.
\]
The *power-mean inequality* states $M_p \le M_q$ for $p < q$, with equality iff all $a_i$ are equal. Special cases: $M_{-1}$ (harmonic mean), $M_0$ (geometric), $M_1$ (arithmetic), $M_2$ (quadratic / RMS). The chain $\text{HM} \le \text{GM} \le \text{AM} \le \text{QM}$ is the *power-mean ladder*, and it is the unifying frame in which AM-GM, GM-HM, QM-AM all sit as instances.

The fourth foundation is *duality and Lagrange multipliers*. For a constrained optimisation problem *maximise $f$ subject to $g_i \le 0$*, the *Lagrange-multiplier* technique writes $\mathcal L = f - \sum \lambda_i g_i$ and looks for critical points of $\mathcal L$ with respect to the $x$ variables, plus the *complementary slackness* condition $\lambda_i g_i = 0$ (either $\lambda_i = 0$, meaning the constraint is *non-binding*, or $g_i = 0$, meaning the constraint is *binding*). The binding constraints together with the gradient conditions determine the optimum. In competition mathematics, the Lagrange machinery is usually replaced by elementary inequality machinery (AM-GM, Cauchy-Schwarz, Jensen) — but the underlying logic is the same: the *binding* inequality at the optimum is the *equality case*. PP3 (the JEE 2001 cos-product) and PP7 (the cotangent sum) are problems whose Lagrange-multiplier solution is elementary; the chapter develops both.

### 2.2 Physical and Cross-Domain Foundations

The reach of inequality constraints extends across the quantitative sciences.

In *physics*, every variational principle is an inequality constraint at heart. *Hamilton's principle* (the action is stationary at the physical path) is, more strongly, an inequality (the action is *minimised* at the physical path for sufficiently short intervals — Jacobi's theorem). *Thermodynamics' second law*: the entropy of an isolated system is non-decreasing, $dS \ge 0$, with equality iff the process is reversible. *Quantum mechanics' uncertainty principle*: $\Delta x \cdot \Delta p \ge \hbar / 2$, with the equality case realised by Gaussian wave functions. In each case, the inequality *bounds* a physical quantity, and the *equality case* (reversible process, Gaussian wave function) characterises a special and important configuration.

In *information theory*, inequalities are foundational. *Gibbs' inequality* (the non-negativity of KL divergence) is the inequality from which essentially all of classical information theory follows: the source-coding theorem, the channel-coding theorem, the rate-distortion theorem. *Jensen's inequality applied to $-\ln$* gives the concavity of entropy and the Gibbs inequality. *Fano's inequality* bounds the probability of error in a noisy channel by a function of the channel's conditional entropy. *The data-processing inequality* says that post-processing cannot increase mutual information. The pattern: *every entropy / information-theoretic quantity is bounded by an inequality, and the equality case characterises the optimal coding or transmission scheme*.

In *economics and game theory*, inequalities are the very language of optimisation. *Budget constraints* are linear inequalities defining the feasible-consumption set; *production possibility frontiers* are inequality boundaries; *individual rationality* and *incentive compatibility* in mechanism design are inequality constraints. The *Karush-Kuhn-Tucker* (KKT) conditions are the inequality-constrained generalisation of Lagrange multipliers, and they govern the entire apparatus of mathematical programming. *No-arbitrage* in financial mathematics is the inequality that admissible price processes must satisfy.

In *engineering and design*, *factor of safety* is the inequality-margin separating the design load from the failure load. *Specification tolerances* are inequality bands within which manufactured components must fall. *Stability margins* in control theory are inequalities (gain margin $> 0$, phase margin $> 0$) bounding the system away from instability. The structural engineer of the opening vignette is performing inequality-constrained optimisation at every step; her job is the practical application of the equality-case principle.

In *medicine and biology*, *therapeutic ranges* are inequality bands; *carrying capacity* (in ecology) is an upper bound on population; *Hardy-Weinberg equilibrium* (in population genetics) is the equality case of a more general inequality on allele frequency distributions. The Lotka-Volterra equations, the Michaelis-Menten kinetics, the SIR epidemic models — each has inequality constraints (positivity of populations, boundedness of rates) that determine its qualitative behaviour.

### 2.3 Cognitive Foundations

The cognitive payoff of inequality constraints is threefold.

The first is *the conversion of optimisation into algebra*. A problem with an explicit "maximise / minimise" has, by the equality-case principle, an *algebraic equation* characterising the optimum: the binding-constraint equation. Solving the algebraic equation gives the answer. The conversion is so reliable that JEE-level optimisation problems often reduce to a single AM-GM application followed by a trivial algebraic step.

The second payoff is *the rejection of unnecessary calculus*. Many JEE Mains optimisation problems can be solved without calculus, by AM-GM or Cauchy-Schwarz. The pure inequality argument is shorter, more illuminating, and (crucially) gives *both* the optimum *and* the location of the optimum *in a single step*. Calculus (the derivative-zero condition) gives the location of the optimum first, and the value only after a substitution. The inequality argument is structurally tighter.

The third payoff is *the unification of seemingly disparate techniques*. AM-GM and Cauchy-Schwarz look different on first reading; both are special cases of the *power-mean inequality* (via duality and Hölder). Jensen's inequality and AM-GM look different; AM-GM is Jensen applied to $-\ln x$. Schur's inequality looks ad hoc; it is the prototype of the *SOS decomposition* family. The inequality apparatus is a *single body of mathematics* with internal coherence, not a *bag of tricks*. The reader who has internalised the unification can choose tools confidently because the tools are connected.

---

## 3. The Diagnostic Toolkit

### 3.1 The Three Questions Method (Inequality-Constraint Edition)

Before deploying any inequality, the trained solver asks three questions of the problem.

1. **What is the binding configuration?** Identify the candidate optimum by symmetry: typically $a_1 = \cdots = a_n$ (the symmetric configuration), or a specifically-skewed configuration when the problem has weights. Compute the value at the candidate optimum; this is the *target inequality* to be proved.

2. **Which named tool deploys here?** Match the structural pattern of the problem to a named inequality: *sum vs product* $\Rightarrow$ AM-GM; *bilinear sums* $\Rightarrow$ Cauchy-Schwarz; *convex function evaluated at a sum* $\Rightarrow$ Jensen; *triangle sides* $\Rightarrow$ Ravi + AM-GM; *sorted sequences* $\Rightarrow$ rearrangement / Chebyshev; *symmetric polynomial with positivity* $\Rightarrow$ Schur or Muirhead. The match is fast when the toolkit is internalised.

3. **What is the equality case?** Each named inequality has a known equality case (AM-GM: all variables equal; Cauchy-Schwarz: proportional sequences; Jensen: constant sequence; Schur: equality at $a = b = c$ and at the boundary $a = b, c = 0$ up to permutation). Verify that the candidate optimum from step 1 matches the equality case of the tool from step 2.

The three questions can be answered in seconds. They are the discipline that converts *inequality problems* into *algebraic problems*.

### 3.2 Forms of Inequality Constraints: A Comprehensive Guide

We collect the five forms encountered in the chapter with one-line diagnostics.

- **Form I — Symmetric polynomial (AM-GM family).** *Diagnostic:* the problem has a sum and a product of $n$ non-negative variables, and the expected equality case is $a_1 = \cdots = a_n$. *Move:* AM-GM in its raw form ($\frac{\sum a_i}{n} \ge \sqrt[n]{\prod a_i}$) or its weighted form. *Examples.* WE3 part (i) [via Jensen, the convex-function form], PP2, PP3, PP4.

- **Form II — Cauchy-Schwarz.** *Diagnostic:* the problem involves a *bilinear* sum $\sum a_i b_i$ or its square. *Move:* $(\sum a_i b_i)^2 \le (\sum a_i^2)(\sum b_i^2)$. The Engel form (Titu's lemma) $\sum \frac{a_i^2}{b_i} \ge \frac{(\sum a_i)^2}{\sum b_i}$ is the most-deployed competition variant. *Examples.* PP1 (three unit vectors), PP6 (Pedoe).

- **Form III — Jensen.** *Diagnostic:* the problem has the form $f(\sum \lambda_i x_i)$ vs $\sum \lambda_i f(x_i)$ with $f$ convex (or concave). *Move:* $f$ convex $\Rightarrow$ $f(\sum \lambda_i x_i) \le \sum \lambda_i f(x_i)$; $f$ concave reverses. *Examples.* WE3 part (i) [Jensen on $t \ln t$], PP3 [Jensen on $\ln \cos$, with care for concavity on $[0, \pi/2]$].

- **Form IV — Triangle / Ravi substitution.** *Diagnostic:* the problem involves the sides of a triangle, with the triangle inequality as a binding constraint. *Move:* substitute $a = y + z$, $b = z + x$, $c = x + y$ with $x, y, z > 0$; the triangle inequality becomes the unconstrained positivity of $x, y, z$. *Examples.* WE1 (the cross-archetype Ch. 9 WE3, reframed), PP4 (right triangle), PP5 (Hadwiger-Finsler).

- **Form V — Rearrangement / Chebyshev.** *Diagnostic:* the problem has two *sorted* sequences and asks about a sum of products $\sum a_i b_{\sigma(i)}$. *Move:* same-order pairing maximises, opposite-order pairing minimises. *Examples.* WE2 (JEE 1972 bounded-ratio), PP7 (cotangent sum, with the weighted variant).

### 3.3 Common Pitfalls

Five errors recur often enough to deserve named warnings.

- **The Trivial-Cases Pitfall.** Applying AM-GM (or Cauchy-Schwarz, or Jensen) when one of the variables is *zero* or *negative*, in a setting where the inequality requires *positive* variables. AM-GM in its standard form requires $a_i \ge 0$ (or $> 0$ depending on the variant); applied to a problem with mixed-sign variables, it gives nonsense. The remedy is to *verify the sign conditions* before applying the inequality.

- **The Wrong-Direction Pitfall.** Jensen's inequality goes one way for convex functions and the *opposite* way for concave. A student who mis-remembers the direction (or forgets which one applies to the function at hand) gets the wrong-direction bound. The remedy is to *compute the second derivative* (or to memorise the convexity classification of the standard functions: $x^p, e^x, x \ln x$ convex; $\ln x, \sqrt x, x^p \text{ for } p \in (0, 1)$ concave) and to *apply the rule mechanically*.

- **The Equality-Case Mistake.** Reporting that an inequality is *tight* without checking the equality case (often producing a strict inequality $<$ when only the non-strict $\le$ is justified, or vice versa). The remedy is *always* to verify the equality case explicitly — by substituting the proposed equality configuration into the original problem.

- **The Wrong-Tool Pitfall.** Selecting a named inequality whose structural pattern *does not match* the problem (e.g., applying Cauchy-Schwarz when the problem is about *one* sequence, or applying Jensen when the function is *neither* convex nor concave). The remedy is the §3.1 question 2 discipline: *match the structural pattern before naming the tool*.

- **The Over-Reach Pitfall.** Applying a powerful tool (Muirhead, Schur) when an elementary tool (AM-GM, Cauchy-Schwarz) suffices, producing an unnecessarily long proof. The remedy is *try the simplest tool first*: if AM-GM works, use AM-GM; only escalate when the structure forces a more powerful tool.

---

## 4. Worked Examples

We work three problems in detail, each in the six-point format. The first re-frames the Chapter 9 WE3 triangle-inequality bound from the inequality-constraint perspective (Ravi substitution + AM-GM). The second is a JEE 1972 two-sided bound, solved by direct algebraic expansion with a rearrangement-inequality reading. The third is the famous INMO + IMO 2000 two-part inequality, solved by Jensen + Vasile-Cirtoaje substitution.

### 4.1 Example 1 — Triangle-Inequality Bound, Re-Framed via Ravi

**Problem.** *Let $x, y, z$ be the lengths of the sides of a triangle. Prove that*
\[
  |x^2(y - z) + y^2(z - x) + z^2(x - y)| \;<\; xyz.
\]
*(Regional Mathematics Olympiad; Joshi EJM Ch. 24, Exercise 24.65; cross-archetype with Chapter 9 WE3.)*

**SEED.** *Inequality constraint (Form IV — Ravi substitution).* The triangle-inequality is a *constraint*; the Ravi substitution *eliminates* the constraint by re-parametrising in terms of three free positive reals $u, v, w$. The original constrained inequality on triangle sides becomes an *unconstrained* inequality on positive reals — and is then handled by elementary AM-GM machinery.

**BRUTE PATH.** This problem was solved in Ch. 9 WE3 via the factorisation $x^2(y-z) + y^2(z-x) + z^2(x-y) = (x-y)(y-z)(x-z)$ combined with the triangle inequality $|x - y| < z$ (and cyclic). The brute path of Ch. 9 worked cleanly. *But the brute path is also the "domain-constraint" framing*: it treats the triangle inequality as a *filter* on admissible $(x, y, z)$ and bounds the product factor-by-factor. The brute path is one route; the *inequality-constraint* framing is another, and the two together illuminate why the same problem can wear two archetypal hats.

**ELEGANT PIVOT.** *Substitute Ravi.* Set $x = u + v$, $y = v + w$, $z = w + u$ for $u, v, w > 0$ (every triangle admits this parametrisation, and conversely every triple of positive $u, v, w$ produces a valid triangle). Then:
\begin{align*}
  x - y &= u - w, \\
  y - z &= v - u, \\
  x - z &= v - w.
\end{align*}
The factored LHS becomes
\[
  (x - y)(y - z)(x - z) \;=\; (u - w)(v - u)(v - w).
\]
The RHS becomes
\[
  xyz \;=\; (u + v)(v + w)(w + u).
\]
The original inequality is therefore equivalent to
\[
  |(u - w)(v - u)(v - w)| \;<\; (u + v)(v + w)(w + u),
\]
which is to be proved for *all* positive reals $u, v, w$ — *no triangle constraint, no inequality on the side lengths*. The triangle-inequality constraint has been *absorbed into the parametrisation*.

*Apply AM-GM to each factor.* For positive reals $p, q > 0$, AM-GM gives $p + q \ge 2\sqrt{pq} \ge 2 \min(p, q) > |p - q|$. (The last inequality is the strict version of *triangle-inequality-for-numbers*: $|p - q| \le \max(p, q) - \min(p, q) < p + q$ since $\min(p, q) > 0$.) Applied to each Ravi-pair:
\[
  u + v \;>\; |u - v|, \qquad v + w \;>\; |v - w|, \qquad w + u \;>\; |w - u|.
\]

Wait — we need to match the factors. The LHS is $|(u - w)(v - u)(v - w)| = |u - w| \cdot |v - u| \cdot |v - w|$. The RHS is $(u + v)(v + w)(w + u)$. So we need
\[
  |u - w| < u + w, \quad |v - u| < v + u, \quad |v - w| < v + w.
\]
Each follows from the above (with the standard triangle inequality on two positive numbers $p, q$: $|p - q| < p + q$). Multiplying:
\[
  |(u - w)(v - u)(v - w)| \;<\; (u + w)(v + u)(v + w) \;=\; (u + v)(v + w)(w + u).
\]
This is the desired inequality. \hfill$\blacksquare$

The Ravi re-framing converts a *constrained triangle-inequality problem* (Ch. 9's framing) into an *unconstrained AM-GM problem* (Ch. 10's framing). The pedagogical takeaway is that the *same problem* can be solved by two routes — the *domain-filter* route (Ch. 9) and the *Ravi + inequality-machinery* route (Ch. 10) — and the cross-archetype reuse is the recognition that *both routes deploy the same underlying structure* (the triangle inequality), but with different *expository angles*. The advanced solver internalises both, and chooses the angle that the current problem demands.

**PITFALLS.**

- *Forgetting that Ravi requires the triangle inequality.* The substitution $x = u+v, y = v+w, z = w+u$ produces *valid* triangle-sides for *any* positive $u, v, w$, but the converse — that *every* triangle's sides admit this Ravi decomposition — requires the triangle inequality. (Solve: $u = (x - y + z)/2, v = (-x + y + z)/2, w = (x + y - z)/2$; these are positive iff the triangle inequality holds.) The remedy is to *verify the triangle inequality first*, then invoke Ravi.

- *Mis-stating the Ravi substitution.* Common typos: $x = u + v, y = w + u, z = v + w$ (a permutation) or $x = uv, y = vw, z = wu$ (a different transformation entirely). The standard Ravi is $a = y + z, b = z + x, c = x + y$ in the slate's notation, or in the chapter's notation $x = u + v, y = v + w, z = w + u$. The remedy is to *write the substitution in a consistent notation and stick to it throughout the problem*.

- *Forgetting the strict-vs-non-strict distinction.* The original problem is a *strict* inequality $<$, requiring a non-degenerate triangle ($u, v, w > 0$ strict, not $\ge 0$). At the degenerate boundary $u = 0$ or $v = 0$ or $w = 0$, the inequality becomes equality. The remedy is to *track the strictness of each step*.

- *Multiplying inequalities of different signs.* The product of three strict inequalities $|p - q| < p + q$ requires the factors on both sides to be non-negative (which they are, since we took absolute values on the LHS and used positivity on the RHS). The remedy is to *take absolute values before multiplying*.

- *Conflating Ch. 9 WE3's "domain" framing with Ch. 10 WE1's "Ravi" framing*. Both routes prove the same inequality, but they emphasize different structural ingredients. Ch. 9 emphasizes the *triangle inequality as a filter on the candidate set*; Ch. 10 emphasizes *Ravi as a substitution that absorbs the constraint*. A student who learns only one framing misses half the lesson. The remedy is to *internalise both*.

**CONNECTIONS.**

*Primary archetype applications.* The Ravi substitution unlocks a class of triangle-inequality problems that are intractable in the $(a, b, c)$ formulation: Hadwiger-Finsler (PP5), the right-triangle bound $R \ge (1+\sqrt 2)r$ (PP4), the Pedoe inequality (PP6, with a different substitution), Schur's inequality applied to triangle sides, the Tsintsifas inequality, the Bottema inequalities. The general pattern: *constrained inequality on triangle sides $\to$ Ravi $\to$ unconstrained inequality on positive reals $\to$ AM-GM / Schur / SOS*.

*Alternative solution archetypes.* The same inequality admits the *Domain-Constraint* framing of Ch. 9 (factor + triangle-inequality on each factor), the *Substitution* framing of Ch. 5 (Ravi is a substitution; this chapter's WE1 explicitly deploys it), and the *Symmetry* framing of Ch. 2 (the inequality is symmetric under permutations of $u, v, w$, and the proof respects the symmetry).

*Cross-domain manifestations.* The pattern *constrained inequality $\to$ parametrisation that absorbs the constraint $\to$ unconstrained inequality* appears in *Lagrangian mechanics* (constraint-eliminating coordinates), in *Lie group theory* (parametrising a manifold to remove its embedding constraints), in *optimisation theory* (the *change-of-variables trick* in convex optimisation), in *manifold geometry* (local coordinate charts that eliminate the manifold's defining equations). The Ravi substitution is the elementary prototype of a deep idea.

**TAKEAWAY.** *Ravi-substitute to eliminate the triangle inequality; then deploy AM-GM (or SOS, or Schur) on the resulting unconstrained problem.*

---

### 4.2 Example 2 — JEE 1972 Bounded Ratio

**Problem.** *For positive reals with $x < y < z$, prove that*
\[
  \frac{x^2}{z} \;<\; \frac{x^2 + y^2 + z^2}{x + y + z} \;<\; \frac{z^2}{x}.
\]
*(JEE 1972; Joshi EJM Ch. 24, Exercise 24.64.)*

**SEED.** *Inequality constraint (Form V — rearrangement / direct expansion).* The middle term is a *weighted mean* of $x^2, y^2, z^2$ (with weights $1/(x+y+z)$ each). The two bounds say that this weighted mean lies *strictly between* the *smallest weight times the smallest squared* ($x^2 / z$) and the *largest weight times the largest squared* ($z^2 / x$) — but with a twist: the "weights" are $\{1/(x+y+z), 1/(x+y+z), 1/(x+y+z)\}$ all equal, and the bounding terms are *different*. The bounds are not standard rearrangement; they are *direct algebraic inequalities* whose proofs are short factorisations.

**BRUTE PATH.** Try a specific case: $x = 1, y = 2, z = 3$. LHS = $1/3 \approx 0.333$. Middle = $(1 + 4 + 9)/6 = 14/6 \approx 2.333$. RHS = $9/1 = 9$. Inequality holds: $0.333 < 2.333 < 9$. ✓ But this is a sanity-check, not a proof. The brute path of trying many cases does not generalise.

**ELEGANT PIVOT.** *Direct algebraic expansion for both inequalities.*

*Left inequality:* $\dfrac{x^2}{z} < \dfrac{x^2 + y^2 + z^2}{x + y + z}$. Cross-multiply (both denominators strictly positive):
\[
  x^2(x + y + z) \;<\; z(x^2 + y^2 + z^2) \quad\Longleftrightarrow\quad z(x^2 + y^2 + z^2) - x^2(x + y + z) \;>\; 0.
\]
Expand and group:
\begin{align*}
  z(x^2 + y^2 + z^2) - x^2(x + y + z)
  &= zx^2 + zy^2 + z^3 - x^3 - x^2 y - x^2 z \\
  &= zy^2 + z^3 - x^3 - x^2 y \\
  &= (z^3 - x^3) + (zy^2 - x^2 y) \\
  &= (z - x)(z^2 + zx + x^2) + y(zy - x^2).
\end{align*}
The first summand is *strictly positive* since $z > x$ (and $z^2 + zx + x^2 > 0$ always). The second summand $y(zy - x^2) > 0$ since $y > 0$ and $zy > x \cdot x = x^2$ (because $z > x$ and $y > x$, giving $zy \ge xy > x^2$ — actually, more directly, $z > x \Rightarrow zy > xy > x^2$ since $y > x$, or simply $zy \ge x \cdot x = x^2$ with strict inequality because $z > x$ or $y > x$, and both are). Hence the entire expression is strictly positive, proving the left inequality.

*Right inequality:* $\dfrac{x^2 + y^2 + z^2}{x + y + z} < \dfrac{z^2}{x}$. Cross-multiply:
\[
  x(x^2 + y^2 + z^2) \;<\; z^2(x + y + z) \quad\Longleftrightarrow\quad z^2(x + y + z) - x(x^2 + y^2 + z^2) \;>\; 0.
\]
Expand and group:
\begin{align*}
  z^2(x + y + z) - x(x^2 + y^2 + z^2)
  &= xz^2 + yz^2 + z^3 - x^3 - xy^2 - xz^2 \\
  &= yz^2 + z^3 - x^3 - xy^2 \\
  &= (z^3 - x^3) + (yz^2 - xy^2) \\
  &= (z - x)(z^2 + zx + x^2) + y(z^2 - xy) \\
  &= (z - x)(z^2 + zx + x^2) + y(z - \sqrt{xy})(z + \sqrt{xy}).
\end{align*}
The first summand is positive (as before). The second summand requires $z > \sqrt{xy}$, which follows from $z > y > \sqrt{xy}$ (since $y > \sqrt{xy}$ iff $y^2 > xy$ iff $y > x$, true). Hence the expression is strictly positive, proving the right inequality. \hfill$\blacksquare$

*Reformulation in the language of rearrangement.* The same result is implied by *Chebyshev's sum inequality*: for similarly-ordered sequences $(x, y, z)$ and $(x, y, z)$ (both ascending), $\frac{1}{3}(x \cdot x + y \cdot y + z \cdot z) \ge \frac{1}{9}(x + y + z)(x + y + z)$, i.e., $\frac{x^2 + y^2 + z^2}{x + y + z} \ge \frac{x + y + z}{3}$. The lower bound $\frac{x+y+z}{3}$ is the average, which is strictly between $x$ and $z$ — but is *not* the bound $x^2/z$ from the problem. The Chebyshev reading gives a *weaker* (though still meaningful) bound; the problem's specific $x^2/z, z^2/x$ bounds are sharper and require the direct algebraic argument above.

**PITFALLS.**

- *Believing Chebyshev alone gives the answer.* Chebyshev gives the *symmetric* bound $\frac{x+y+z}{3}$; the problem asks for the *asymmetric* bounds $x^2/z$ and $z^2/x$. The remedy is *direct algebra* (factor + group), not blind application of a named inequality.

- *Forgetting the strict-vs-non-strict distinction.* The problem has strict $<$. The proof uses $x < y < z$ strict, and the factorisation produces strictly-positive expressions. The remedy is *track the strictness*.

- *Sign-confusion in cross-multiplication.* Cross-multiplying an inequality is valid only when the multiplied-by quantity is *positive* (in which case the inequality direction is preserved) or *negative* (in which case the direction reverses). Here both denominators are positive, so direction is preserved. The remedy is *verify the sign of every multiplied-by quantity*.

- *Trying to apply AM-GM directly.* AM-GM applied to $x^2, y^2, z^2$ gives $\frac{x^2 + y^2 + z^2}{3} \ge \sqrt[3]{x^2 y^2 z^2} = (xyz)^{2/3}$. This is a true bound but does not produce the $x^2/z$ form. The remedy is *match the tool to the structural form*; here, AM-GM is the wrong tool, and direct algebra is the right one.

- *Missing the asymmetric structure.* The problem is asymmetric under $x \leftrightarrow z$ — the bounds $x^2/z$ and $z^2/x$ swap. A student who tries to *symmetrise* (e.g., by replacing the bounds with $\frac{x^2 + z^2}{x + z}$) loses the problem's asymmetric structure. The remedy is *read the problem's asymmetry and respect it*.

**CONNECTIONS.**

*Primary archetype applications.* The pattern *bound the weighted mean above and below by extremal weighted terms* recurs throughout analysis: in numerical-quadrature error bounds, in approximation theory (the best $L^p$ approximation lies between the extremal interpolating functions), in interval arithmetic. The pattern *prove an inequality by factoring the difference into a sum of provably-positive terms* is the SOS-decomposition strategy applied at the elementary level.

*Alternative solution archetypes.* The bounds can also be derived (more painfully) via *Lagrange multipliers* on the problem *maximise / minimise $(x^2 + y^2 + z^2)/(x + y + z)$ subject to $x < y < z$, $x, y, z > 0$* — but the inequality solution is order-of-magnitude shorter and gives the bounds in their exact form.

*Cross-domain manifestations.* The *weighted-mean-bounded-by-extremal-terms* pattern is the universal *Markov inequality* in probability theory: $P(X \ge a) \le E[X]/a$, with the equality case at the degenerate distribution. The pattern *weighted average sits between extremes* is so universal that statisticians call it the *convex hull principle*: every weighted average of points lies in the convex hull of those points, with the extremes achieved only at degenerate weighting.

**TAKEAWAY.** *When AM-GM and Chebyshev give the wrong form of the bound, fall back to direct algebraic factorisation — the difference often splits into a sum of provably-positive terms.*

---

### 4.3 Example 3 — The INMO + IMO 2000 Two-Part Inequality

**Problem.** *Let $a, b, c$ be positive reals with $abc = 1$. Prove:*
\[
  \text{(i)} \quad a^{b+c} b^{c+a} c^{a+b} \;\le\; 1; \qquad \text{(ii)} \quad \left(a - 1 + \frac{1}{b}\right)\left(b - 1 + \frac{1}{c}\right)\left(c - 1 + \frac{1}{a}\right) \;\le\; 1.
\]
*(INMO + IMO 2000; Joshi EJM Ch. 24, Exercise 24.66; cross-archetype with Chapter 2 PP7.)*

**SEED.** *Inequality constraint (Form III — Jensen + Form IV — Vasile-Cirtoaje substitution).* Part (i) is a *Jensen-on-$t\ln t$* inequality after logarithmising, with the $abc = 1$ constraint absorbed via $\ln a + \ln b + \ln c = 0$. Part (ii) is a *Vasile-Cirtoaje-substitution* inequality: the substitution $a = x/y, b = y/z, c = z/x$ for positive $x, y, z$ automatically satisfies $abc = 1$ and converts part (ii) into a clean symmetric inequality on $x, y, z$.

**BRUTE PATH.** Try the symmetric configuration $a = b = c = 1$ (which satisfies $abc = 1$). Both inequalities give equality ($1 \le 1$). This identifies the *equality case* — but proves nothing yet. The brute path of trying many specific $(a, b, c)$ gives evidence; it does not give a proof.

**ELEGANT PIVOT.** *Part (i) via Jensen.* Take logarithms:
\[
  \ln\left(a^{b+c} b^{c+a} c^{a+b}\right) \;=\; (b + c)\ln a + (c + a)\ln b + (a + b)\ln c.
\]
Set $x = \ln a, y = \ln b, z = \ln c$. The constraint $abc = 1$ becomes $x + y + z = 0$. The LHS becomes
\begin{align*}
  (b + c)x + (c + a)y + (a + b)z
  &= bx + cx + cy + ay + az + bz \\
  &= a(y + z) + b(x + z) + c(x + y) \\
  &= a(-x) + b(-y) + c(-z) \qquad\text{(using } x + y + z = 0\text{)} \\
  &= -(ax + by + cz) \\
  &= -(a \ln a + b \ln b + c \ln c).
\end{align*}
We therefore need to show $a \ln a + b \ln b + c \ln c \ge 0$ (so that the original log is $\le 0$, i.e., the original product is $\le 1$).

*Apply Jensen to $f(t) = t \ln t$ on $(0, \infty)$.* This function is convex (its second derivative is $1/t > 0$). By Jensen,
\[
  \frac{a \ln a + b \ln b + c \ln c}{3} \;\ge\; \frac{a + b + c}{3} \ln \frac{a + b + c}{3}.
\]
By AM-GM (with the constraint $abc = 1$),
\[
  \frac{a + b + c}{3} \;\ge\; \sqrt[3]{abc} \;=\; 1, \qquad \text{so } \frac{a + b + c}{3} \ge 1, \quad \text{hence } \ln\frac{a + b + c}{3} \ge 0.
\]
Combining,
\[
  \frac{a \ln a + b \ln b + c \ln c}{3} \;\ge\; \frac{a + b + c}{3} \cdot \ln\frac{a + b + c}{3} \;\ge\; 1 \cdot 0 \;=\; 0,
\]
so $a \ln a + b \ln b + c \ln c \ge 0$, giving $a^{b+c} b^{c+a} c^{a+b} \le 1$. Equality iff $a = b = c = 1$ (the case where both Jensen and AM-GM bind). \hfill$\blacksquare$

*Part (ii) via Vasile-Cirtoaje substitution.* The constraint $abc = 1$ admits the *Vasile-Cirtoaje* parametrisation $a = x/y, b = y/z, c = z/x$ for positive reals $x, y, z$ (which automatically gives $abc = (x/y)(y/z)(z/x) = 1$; conversely, every positive triple $(a, b, c)$ with $abc = 1$ admits such a parametrisation, e.g., via $x = 1, y = 1/a, z = 1/(ab) = c$). Then:
\begin{align*}
  a - 1 + \frac{1}{b} &= \frac{x}{y} - 1 + \frac{z}{y} \;=\; \frac{x - y + z}{y}, \\
  b - 1 + \frac{1}{c} &= \frac{y - z + x}{z}, \\
  c - 1 + \frac{1}{a} &= \frac{z - x + y}{x}.
\end{align*}
The product is
\[
  \frac{(x - y + z)(y - z + x)(z - x + y)}{xyz} \;=\; \frac{(-x + y + z)(x - y + z)(x + y - z)}{xyz}.
\]
We need this $\le 1$, i.e.,
\[
  (-x + y + z)(x - y + z)(x + y - z) \;\le\; xyz.
\]

*Case 1: $x, y, z$ are sides of a triangle* (i.e., the three factors $-x+y+z, x-y+z, x+y-z$ are all strictly positive). Substitute the *inverse Ravi* $u = -x+y+z, v = x-y+z, w = x+y-z$ with $u, v, w > 0$. Then $x = (v+w)/2, y = (u+w)/2, z = (u+v)/2$. The desired inequality becomes
\[
  uvw \;\le\; \frac{(v+w)(u+w)(u+v)}{8}.
\]
By AM-GM on each factor: $v + w \ge 2\sqrt{vw}$, $u + w \ge 2\sqrt{uw}$, $u + v \ge 2\sqrt{uv}$. Multiplying:
\[
  (v+w)(u+w)(u+v) \;\ge\; 8\sqrt{(uvw)^2} \;=\; 8uvw,
\]
so $uvw \le (v+w)(u+w)(u+v)/8$, as required. Equality iff $u = v = w$, i.e., $x = y = z$, i.e., $a = b = c = 1$.

*Case 2: $x, y, z$ do not form a triangle* (one factor non-positive). Without loss of generality $-x + y + z \le 0$. Then the LHS $(-x+y+z)(x-y+z)(x+y-z)$ is $\le 0$ (one non-positive factor times two factors that could be of either sign — but the product of all three is bounded above by $xyz > 0$ trivially). Actually more carefully: at least one factor is non-positive. The other two are either both non-negative (in which case the product is $\le 0 \le xyz$) or one is also non-positive (in which case at least two are non-positive, and their product is $\ge 0$; we need a separate argument). A cleaner statement: WLOG $x \ge y \ge z > 0$; if $x \ge y + z$, then $-x + y + z \le 0$, and one checks that in this case $(-x+y+z)(x-y+z)(x+y-z) \le 0 \le xyz$ (since $x - y + z > 0$ and $x + y - z > 0$ when $x \ge y \ge z$). Hence the inequality holds.

Combining Cases 1 and 2 covers all positive $(x, y, z)$, so Part (ii) is proved. \hfill$\blacksquare$

The Vasile-Cirtoaje substitution converts an *$abc = 1$ constrained inequality* (in $a, b, c$) into an *unconstrained symmetric inequality* (in $x, y, z$), which then admits the standard *Ravi-AM-GM* treatment (in case 1) or a trivial sign argument (in case 2). The pattern *constrained $\to$ unconstrained via substitution $\to$ standard machinery* is the same pattern as WE1's Ravi treatment, applied at a higher level (the constraint $abc = 1$ rather than the triangle inequality).

**PITFALLS.**

- *Forgetting to handle the non-triangle case.* The Vasile-Cirtoaje substitution gives positive $x, y, z$ but does *not* automatically force them to satisfy the triangle inequality. The case analysis (triangle vs non-triangle) is essential. The remedy is to *check whether the substitution preserves all the structural constraints of the original problem*.

- *Mis-applying Jensen to $t \ln t$.* The function $t \ln t$ is *convex* on $(0, \infty)$, so Jensen gives $\overline{t\ln t} \ge \overline{t} \ln \overline{t}$ (the *value at the average* is *at most* the *average of the values*, but here "at most" goes the other way once we apply convexity). Specifically: $f$ convex $\Rightarrow$ $f(\overline x) \le \overline{f(x)}$, i.e., $\overline{t\ln t} \ge \overline t \cdot \ln\overline t$. The remedy is to *write the Jensen inequality with explicit direction* (convex: value-at-average $\le$ average-of-values) and *check the direction matches the desired conclusion*.

- *Confusing the Vasile-Cirtoaje and Ravi substitutions.* Both are *constraint-eliminating reparametrisations*, but they apply to different constraints: Ravi to the *triangle inequality*, Vasile-Cirtoaje to the *$abc = 1$* (or analogous multiplicative) constraint. Mis-applying one for the other gives the wrong identifications. The remedy is to *match the substitution to the constraint*.

- *Not verifying the equality case of part (ii).* Equality requires *both* the AM-GM step ($u = v = w$, i.e., $x = y = z$) *and* the non-triangle case to not apply (i.e., $x, y, z$ form a valid triangle, which $x = y = z$ does — an equilateral). Substituting back: $a = b = c = 1$ (verifying $abc = 1$ and the original product = 1). The remedy is to *substitute the equality candidate back into the original to verify*.

- *Treating parts (i) and (ii) as independent.* The two parts share the same equality case ($a = b = c = 1$) and similar structural ingredients (substitution + standard inequality). A solver who notes the parallel can often see the proofs together. The remedy is to *look for shared structure across multi-part problems*.

**CONNECTIONS.**

*Primary archetype applications.* The Vasile-Cirtoaje substitution unlocks a class of $abc = k$ constrained inequalities. The Jensen-on-convex-functions technique unlocks symmetric inequalities involving sums of $\phi(a_i)$ where $\phi$ has known convexity. Together they handle a large fraction of competition-mathematics inequality problems.

*Alternative solution archetypes.* Part (i) admits a Cauchy-Schwarz proof (less elegant than Jensen) and a *power-mean / weighted AM-GM* proof. Part (ii) admits a *Schur-inequality* proof in the original $a, b, c$ variables (more involved than the Vasile-Cirtoaje route). The chapter's chosen route is the most pedagogically illuminating.

*Cross-domain manifestations.* The Jensen-on-$t \ln t$ inequality is the *Gibbs entropy* inequality in information theory: $H(p) \ge 0$ with equality iff $p$ is a degenerate distribution. The constraint $abc = 1$ becomes, in the entropy interpretation, *the distribution is normalised*. The Vasile-Cirtoaje substitution is, structurally, a *gauge fixing* in physics: choosing a specific representation that eliminates a global symmetry of the problem.

**TAKEAWAY.** *Logarithmise + Jensen for multiplicative-product inequalities; substitute the Vasile-Cirtoaje $a = x/y$ parametrisation to absorb $abc = 1$ constraints; verify both the triangle-vs-non-triangle case and the equality case.*

---

## 5. Practice Problems

Seven problems, statements only; full solutions appear in the Appendix. The slate spans Tier 1 through Tier 4, with three Tier-3 problems and two Tier-4 problems reflecting this chapter's competition-mathematics depth.

### 5.1 Three Unit Vectors, Pairwise Distance Sum (Tier 2; Joshi Ch. 24, Exercise 24.50)

For three unit vectors $\vec a, \vec b, \vec c$ in $\mathbb R^3$, prove that
\[
  |\vec a - \vec b|^2 + |\vec b - \vec c|^2 + |\vec c - \vec a|^2 \;\le\; 9.
\]
When is equality attained?

### 5.2 JEE 2001 Quadratic-Minimum Range (Tier 1; Joshi Ch. 24, Exercise 24.17)

Let $f(x) = (1 + b^2)x^2 + 2bx + 1$, and let $m(b)$ denote the minimum value of $f$ over $x \in \mathbb R$. Find the range of $m(b)$ as $b$ varies over $\mathbb R$.

### 5.3 Cyclic Cosine Product under Cotangent Constraint (Tier 3; JEE 2001, Joshi Ch. 24, Exercise 24.27)

Find the maximum of $(\cos\alpha_1)(\cos\alpha_2)\cdots(\cos\alpha_n)$ subject to $0 \le \alpha_i \le \pi/2$ and the constraint $(\cot\alpha_1)(\cot\alpha_2)\cdots(\cot\alpha_n) = 1$. *(This problem was solved as Chapter 7 WE3 under the normalisation framing; restated here as a practice problem in the inequality-constraint chapter, with an alternative AM-GM-based solution route in the appendix.)*

### 5.4 Right-Triangle Circumradius-Inradius Bound (Tier 3: RMO; Joshi Ch. 24, Exercise 24.88)

For a right-angled triangle with circumradius $R$ and inradius $r$, prove $R \ge (1 + \sqrt 2) r$, and state the equality case.

### 5.5 Hadwiger-Finsler Inequality (Tier 4; Joshi Ch. 24, Exercise 24.93)

For any triangle with sides $a, b, c$ and area $\Delta$, prove
\[
  2(ab + bc + ca) - (a^2 + b^2 + c^2) \;\ge\; 4\sqrt 3 \cdot \Delta.
\]
When is equality attained?

### 5.6 Pedoe's Inequality (Tier 4; Joshi Ch. 24, Exercise 24.96)

For two triangles with sides $a, b, c$ and $a', b', c'$, and respective areas $\Delta, \Delta'$, prove
\[
  a^2(b'^2 + c'^2 - a'^2) + b^2(c'^2 + a'^2 - b'^2) + c^2(a'^2 + b'^2 - c'^2) \;\ge\; 16 \Delta \Delta',
\]
with equality if and only if the two triangles are similar.

### 5.7 Weighted Cotangent Sum Minimum (Tier 3; Joshi Ch. 24, Exercise 24.95)

For positive reals $\lambda_1, \lambda_2 > 0$ and angles $\theta_1, \theta_2 > 0$ with $\theta_1 + \theta_2 = T$ (fixed), find the minimum of $\lambda_1 \cot\theta_1 + \lambda_2 \cot\theta_2$. *State the value of $\theta_1 / \theta_2$ (or equivalently $\sin\theta_1 / \sin\theta_2$) at the minimum.*

---

## 6. The Connections Web

Inequality constraints connect to nearly every other archetype and to substantial parts of every quantitative discipline.

### 6.1 Inequality Constraints Across Mathematical Domains

*Real analysis.* The *Bolzano-Weierstrass theorem* (every bounded sequence has a convergent subsequence) is, structurally, an *existence* result driven by an inequality constraint (boundedness). The *intermediate value theorem* converts inequalities at the endpoints of an interval ($f(a) < 0 < f(b)$) into an *existence* statement (some $c \in (a, b)$ with $f(c) = 0$) — bridging Ch. 10 (inequalities) and Ch. 11 (existence). The *fundamental theorem of calculus* relates *bounded* integrands (an inequality) to *differentiable* antiderivatives.

*Probability theory and statistics.* Markov, Chebyshev, Chernoff, Hoeffding — the bestiary of probability inequalities is enormous, and each binds the probability of a rare event by an inequality involving moments. *Concentration inequalities* (a major area of modern probability) bound the deviation of a random variable from its mean by exponentially-decaying terms; their equality cases are at the *worst-case distributions* (typically Bernoulli or Gaussian). The *Cramér-Rao bound* in statistics bounds the variance of an unbiased estimator by the inverse of the Fisher information; equality at the *efficient* estimator.

*Functional analysis.* Hölder, Minkowski, Young, Bernstein — the inequalities of $L^p$-space analysis. *Sobolev inequalities* relate $L^p$-norms of derivatives to $L^q$-norms of functions, with equality cases at extremal functions (often related to the *Yamabe metric* or the *Sobolev minimiser*). *Hardy-Littlewood-Sobolev* inequalities bound convolution norms; *Brascamp-Lieb* inequalities generalise to multiple integrals.

*Linear algebra.* The *singular-value decomposition* expresses every matrix as a sum of rank-one outer products with non-negative coefficients (an inequality); the *largest singular value* bounds the matrix's *operator norm*; the *condition number* (ratio of largest to smallest singular value) bounds the *numerical conditioning*. *Schur inequality* (in linear algebra; distinct from the inequality also called Schur's in the present chapter) bounds the *sum of squared eigenvalues* by the *Frobenius norm squared*, with equality at *normal matrices*.

*Combinatorics.* The *AM-GM inequality* is the prototype of *combinatorial concentration*. *Turán's theorem* in graph theory: the maximum number of edges in a graph without a complete subgraph $K_{r+1}$ is bounded by $\left(1 - \frac{1}{r}\right) \cdot \binom{n}{2}$. *Bonferroni's inequalities* bound probabilities of unions by alternating sums of subset probabilities.

### 6.2 Inequality Constraints in Physics, Economics, and Beyond

*Statistical mechanics.* The *second law of thermodynamics* is an inequality: $dS \ge 0$ for an isolated system, with equality at reversible (idealised) processes. The *free-energy bound* $F = U - TS$ produces inequalities of the form $\Delta F \le 0$ for spontaneous processes. The *Gibbs-Bogoliubov-Feynman inequality* in many-body physics bounds the free energy of an interacting system by the free energy of a non-interacting trial system; equality at the *exact* trial Hamiltonian.

*Quantum mechanics.* The *Heisenberg uncertainty principle* $\Delta x \cdot \Delta p \ge \hbar/2$ (Robertson-Schrödinger generalisation: $\Delta A \cdot \Delta B \ge \frac{1}{2}|\langle [A, B]\rangle|$). The *Bell inequalities* test local-realism against quantum predictions; equality cases distinguish classical from quantum statistics. The *energy-time uncertainty* $\Delta E \cdot \Delta t \ge \hbar / 2$ (in its various formal statements).

*Economics and game theory.* *Budget constraints* are inequalities. *Pareto efficiency*: an allocation is Pareto-optimal iff no other allocation gives strictly more to at least one agent without giving strictly less to any other (an inequality definition). *Nash equilibria* are characterised by an inequality system (each player's payoff is maximised over their strategy set given the other players' strategies). *Brouwer-Kakutani fixed-point theorems* (which underlie equilibrium existence) are proved using inequality-bound homotopies.

*Engineering and design.* Every *factor of safety* is an inequality margin. Every *control-system stability margin* (gain margin, phase margin) is an inequality bound. Every *specification tolerance* is an inequality band. The opening vignette's structural engineer is the everyday-engineering example.

*Information theory.* *Gibbs' inequality* ($D(p \| q) \ge 0$ for KL divergence). The *data processing inequality*. The *source coding theorem* (entropy is a lower bound on average code length). The *channel coding theorem* (channel capacity is an upper bound on reliable transmission rate). All are inequalities, with equality cases identifying the *optimal* coding or transmission scheme.

### 6.3 Cross-Domain Manifestations

*Computer science.* *Algorithm-complexity bounds* are inequalities ($T(n) = O(n \log n)$ is a *Big-O* upper bound). *Approximation algorithms* are characterised by *approximation ratios* (inequalities on the ratio of algorithmic output to optimum). *Cryptographic security* is defined by *adversary-success-probability inequalities* (an adversary's success is *at most negligibly* better than chance).

*Operations research.* *Linear programming* is the study of inequality-constrained linear optimisation; *integer programming* adds integrality. *Convex optimisation* generalises to inequality-constrained convex problems. The *duality theory* of linear programming (every primal inequality-constrained problem has a dual inequality-constrained problem with related solutions) is the operations-research version of Lagrange-multiplier theory.

*Architecture and design.* *Load-bearing constraints* are inequalities ($P \le P_{cr}$). *Energy-efficiency standards* are inequalities (energy usage $\le$ regulatory cap). *Daylighting requirements* are inequalities (illuminance $\ge$ minimum standard). Every design specification is an inequality envelope.

*Music and art.* *Tonal music* operates inside inequality bands (consonant intervals are "preferred", dissonant intervals "avoided", with the *preference / avoidance* encoded as an inequality on a learned cost function). *Aesthetic preferences* in design (golden ratio, rule of thirds) are inequality bands on dimensional ratios.

### 6.4 Related Archetypes

Inequality constraints interact with five other archetypes in particularly tight ways.

- **Archetype 2 (Symmetry).** The equality case of most symmetric inequalities is at the *symmetric configuration* $x_1 = \cdots = x_n$. Chapter 2's symmetry machinery and Chapter 10's inequality machinery are tightly interlocked: *symmetry tells you where the equality case is; the inequality machinery tells you the value*.

- **Archetype 7 (Normalization / Scaling).** Many inequality problems become tractable after a normalisation step (Ch. 7's WE2 demonstrated $a + b + c = 1$ normalisation on a Cauchy-Schwarz problem). The normalisation absorbs a degree of freedom; the remaining inequality is on a constrained set.

- **Archetype 9 (Domain Constraints).** Inequalities are the most common kind of domain constraint. Ch. 9 (Domain Constraints) treats the general filter; Ch. 10 (Inequality Constraints) specialises to inequalities and supplies the named-tool machinery. The two chapters together cover the constraint side of problem-solving.

- **Archetype 12 (Extremal Principles).** The equality case of a tight inequality is an *extremum*; conversely, every extremum is *characterised* by an inequality (the *necessary* and *sufficient* conditions of the optimisation problem). Chapter 12 will develop the *extremum-as-equality-case* identification systematically.

- **Archetype 17 (Degrees of Freedom Analysis).** A problem with *fewer* constraints (inequalities) has *more* degrees of freedom and (typically) *more* solutions. The DOF analysis of Ch. 17 gives the systematic count of constraints vs free variables; the inequality apparatus of Ch. 10 supplies the *specific* constraints to count.

---

## 7. Master Takeaways

Seven sentences. Each one is a complete operational principle.

1. *Inequalities are not obstacles; they are constraints that determine the answer. The equality case is the answer.* (The canonical takeaway.)

2. *Ravi-substitute to eliminate the triangle inequality; the resulting unconstrained inequality on positive reals is then handled by AM-GM / SOS.* (WE1 takeaway; Form IV.)

3. *When AM-GM and Chebyshev give the wrong form of the bound, fall back to direct algebraic factorisation; the difference often splits into a sum of provably-positive terms.* (WE2 takeaway; Form V + SOS.)

4. *Logarithmise + Jensen for multiplicative-product inequalities; the Vasile-Cirtoaje substitution absorbs $abc = 1$ constraints.* (WE3 takeaway; Forms III + IV at higher level.)

5. *Every named inequality (AM-GM, Cauchy-Schwarz, Jensen, Chebyshev, rearrangement, Schur, power-mean) has a known equality case — internalise the case along with the inequality.*

6. *Match the structural pattern before naming the tool: sum vs product $\Rightarrow$ AM-GM; bilinear sums $\Rightarrow$ Cauchy-Schwarz; convex function $\Rightarrow$ Jensen; sorted sequences $\Rightarrow$ rearrangement / Chebyshev; triangle sides $\Rightarrow$ Ravi.*

7. *Try the simplest tool first: AM-GM before Cauchy-Schwarz before Jensen before Schur before Muirhead.*

---

## 8. Self-Assessment Checklist

You have absorbed Chapter 10 when, without re-opening it, you can do each of the following from memory.

- [ ] State AM-GM in its raw form and its weighted form, with the equality case.
- [ ] State Cauchy-Schwarz in its vector form and its Engel (Titu) form, with the equality case.
- [ ] State Jensen's inequality for convex / concave functions, with the equality case, and apply it to $t \ln t$, $e^x$, $-\ln x$, and $\sin x$ (on the appropriate intervals where each is convex or concave).
- [ ] State the power-mean inequality $M_p \le M_q$ for $p < q$ and identify the standard means HM, GM, AM, QM as specific cases.
- [ ] State the rearrangement inequality and derive Chebyshev's sum inequality as a corollary.
- [ ] State Schur's inequality (degree-2 case): $a^2(a-b)(a-c) + b^2(b-c)(b-a) + c^2(c-a)(c-b) \ge 0$ for $a, b, c \ge 0$; identify the equality cases.
- [ ] State the Ravi substitution $a = y+z, b = z+x, c = x+y$ and explain why it converts the triangle-inequality constraint into the unconstrained positivity of $x, y, z$.
- [ ] State the Vasile-Cirtoaje substitution $a = x/y, b = y/z, c = z/x$ for the constraint $abc = 1$ and explain why it is an automatic parametrisation of the constraint surface.
- [ ] Identify and explain three of the five common pitfalls: the Trivial-Cases Pitfall, the Wrong-Direction Pitfall, the Equality-Case Mistake, the Wrong-Tool Pitfall, the Over-Reach Pitfall.
- [ ] Articulate, in one sentence, how Inequality Constraints (Ch. 10) relates to Domain Constraints (Ch. 9), Symmetry (Ch. 2), and Extremal Principles (Ch. 12): Ch. 10 specialises Ch. 9 to inequalities; Ch. 2 tells you where the equality case is; Ch. 12 systematises the equality-case-as-extremum identification.

---

## Bridge to Chapter 11: Existence / Uniqueness Conditions

Chapter 10 closed the *inequality* leg of the *Constraint Exploitation* sub-pillar (Chs. 9–12). The chapter equipped the reader with the named-inequality toolkit (AM-GM, Cauchy-Schwarz, Jensen, Chebyshev, rearrangement, Schur, power-mean, Ravi-substitution, Vasile-Cirtoaje), the equality-case principle, and the two cross-archetype reuses that demonstrate how the *same* problem can wear different archetypal hats (Ch. 9 WE3 / Ch. 10 WE1 = the triangle-inequality bound under two framings; Ch. 2 PP7 / Ch. 10 WE3 = the IMO 2000 product under two framings).

Chapter 11 — *Existence / Uniqueness Conditions* — moves from *bounding* to *proving existence*. Where Ch. 10 took the inequality as the *answer*, Ch. 11 takes existence (and sometimes uniqueness) as the *answer*: *prove there is a real number satisfying the equation; prove a fixed point exists; prove the optimum is attained*. The named tools shift accordingly: *intermediate value theorem* (for continuous functions on intervals); *mean value theorem* and *Rolle's theorem* (for differentiable functions); *Banach fixed-point theorem* (for contractive maps on complete spaces). Each is, structurally, the inequality machinery of Ch. 10 *bridged* with the topological machinery of *continuity and completeness*. The IVT, in particular, is the universal *inequality-to-existence* converter: *if $f(a) < 0 < f(b)$ and $f$ is continuous on $[a, b]$, then there exists $c \in (a, b)$ with $f(c) = 0$*.

With Chapter 11 in hand, the reader will have completed three of the four chapters of the *Constraint Exploitation* sub-pillar, and will be positioned for Chapter 12 (Extremal Principles), which unifies the inequality-constraint machinery of Ch. 10 with the existence machinery of Ch. 11 to give the systematic identification of extrema as solutions of inequality-equality systems.

---

## Appendix — Solutions to Practice Problems

### Solution to 5.1 — Three Unit Vectors, Pairwise Distance Sum

For unit vectors $\vec a, \vec b, \vec c$ in $\mathbb R^3$:
\[
  |\vec a - \vec b|^2 \;=\; (\vec a - \vec b) \cdot (\vec a - \vec b) \;=\; |\vec a|^2 - 2 \vec a \cdot \vec b + |\vec b|^2 \;=\; 2 - 2 \vec a \cdot \vec b
\]
(using $|\vec a| = |\vec b| = 1$). Summing cyclically:
\[
  \sum |\vec a - \vec b|^2 \;=\; 6 - 2(\vec a \cdot \vec b + \vec b \cdot \vec c + \vec c \cdot \vec a).
\]

Now consider the squared length of the *centroid sum*:
\[
  |\vec a + \vec b + \vec c|^2 \;=\; |\vec a|^2 + |\vec b|^2 + |\vec c|^2 + 2(\vec a \cdot \vec b + \vec b \cdot \vec c + \vec c \cdot \vec a) \;=\; 3 + 2(\vec a \cdot \vec b + \vec b \cdot \vec c + \vec c \cdot \vec a).
\]

This squared length is *non-negative*: $|\vec a + \vec b + \vec c|^2 \ge 0$. Rearranging,
\[
  2(\vec a \cdot \vec b + \vec b \cdot \vec c + \vec c \cdot \vec a) \;\ge\; -3 \quad\Longleftrightarrow\quad -2(\vec a \cdot \vec b + \vec b \cdot \vec c + \vec c \cdot \vec a) \;\le\; 3.
\]
Substituting into the pairwise sum,
\[
  \sum |\vec a - \vec b|^2 \;=\; 6 - 2(\vec a \cdot \vec b + \vec b \cdot \vec c + \vec c \cdot \vec a) \;\le\; 6 + 3 \;=\; 9.
\]

*Equality case.* Equality holds iff $|\vec a + \vec b + \vec c|^2 = 0$, i.e., $\vec a + \vec b + \vec c = \vec 0$. Geometrically: three unit vectors sum to zero iff they form a *closed triangle* in $\mathbb R^3$ — and three unit vectors form a closed triangle iff they are coplanar with pairwise angles of $120°$ (i.e., the vertices of an equilateral triangle inscribed in the unit circle of their common plane). $\blacksquare$

The technique is a *single squared-quantity trick*: rewriting the sum of three pairwise distances as a single squared centroid magnitude collapses the bound to a single inequality. This is Form II (Cauchy-Schwarz family — squared-magnitude trick is a special case).

---

### Solution to 5.2 — JEE 2001 Quadratic-Minimum Range

For each fixed $b \in \mathbb R$, $f(x) = (1 + b^2)x^2 + 2bx + 1$ is a *strictly convex* upward parabola (coefficient of $x^2$ is $1 + b^2 \ge 1 > 0$). Its minimum is at the vertex $x^* = -2b / (2(1 + b^2)) = -b / (1 + b^2)$.

Substituting back:
\[
  m(b) \;=\; f(x^*) \;=\; (1 + b^2) \cdot \frac{b^2}{(1 + b^2)^2} + 2b \cdot \frac{-b}{1 + b^2} + 1 \;=\; \frac{b^2}{1 + b^2} - \frac{2b^2}{1 + b^2} + 1 \;=\; -\frac{b^2}{1 + b^2} + 1 \;=\; \frac{1}{1 + b^2}.
\]

As $b$ varies over $\mathbb R$, $b^2 \in [0, \infty)$, so $1 + b^2 \in [1, \infty)$, so $m(b) = 1 / (1 + b^2) \in (0, 1]$. Specifically: $m(0) = 1$ (the maximum), and $m(b) \to 0$ as $|b| \to \infty$ (but never reaches zero).

Range: $\boxed{m(b) \in (0, 1]}$. $\blacksquare$

This is Form I (symmetric-polynomial / direct quadratic) — the *vertex formula* converts a one-parameter family of quadratic minima into a single function of $b$, whose range is read off by elementary analysis.

---

### Solution to 5.3 — Cyclic Cosine Product under Cotangent Constraint

This problem appeared as Ch. 7 WE3 with the normalisation-archetype framing (treating the constraint $\prod \cot\alpha_i = 1$ as a multiplicative normalisation). Here we sketch the alternative *AM-GM* route that the inequality-constraint chapter emphasises.

The constraint $\prod \cot\alpha_i = 1$ rewrites as $\prod \cos\alpha_i = \prod \sin\alpha_i$, i.e., the *cosine product* equals the *sine product*. Let $P = \prod\cos\alpha_i$ and $Q = \prod\sin\alpha_i$, with $P = Q$ by the constraint.

By the double-angle identity $\sin 2\alpha = 2 \sin\alpha\cos\alpha$:
\[
  \prod_{i=1}^n \sin 2\alpha_i \;=\; 2^n \prod_{i=1}^n \sin\alpha_i \cos\alpha_i \;=\; 2^n \cdot PQ \;=\; 2^n P^2.
\]
Each $\sin 2\alpha_i \le 1$, so the product is $\le 1$, giving $2^n P^2 \le 1$, i.e., $P \le 2^{-n/2} = 1/2^{n/2}$.

*Equality case.* Equality iff every $\sin 2\alpha_i = 1$, i.e., $2\alpha_i = \pi/2$, i.e., $\alpha_i = \pi/4$ for every $i$. At $\alpha_i = \pi/4$: $\cos\alpha_i = 1/\sqrt 2$, so $P = (1/\sqrt 2)^n = 1/2^{n/2}$ ✓.

Maximum: $\boxed{P_{\max} = 1/2^{n/2}}$ attained at $\alpha_i = \pi/4$ for all $i$. $\blacksquare$

The AM-GM proof bypasses Lagrange multipliers entirely; the constraint $\prod\cot = 1$ collapses to $\prod\sin 2\alpha_i \le 1$, and the bound is immediate. This is Form I (AM-GM family) applied to the *product* of $\sin 2\alpha_i$ terms.

---

### Solution to 5.4 — Right-Triangle Circumradius-Inradius Bound

Let the right triangle have legs $a, b$ and hypotenuse $c = \sqrt{a^2 + b^2}$. Standard formulas:
\[
  R \;=\; \frac{c}{2} \quad (\text{half the hypotenuse}), \qquad r \;=\; \frac{a + b - c}{2}.
\]

We want $R \ge (1 + \sqrt 2) r$, i.e.,
\[
  \frac{c}{2} \;\ge\; (1 + \sqrt 2) \cdot \frac{a + b - c}{2} \quad\Longleftrightarrow\quad c \;\ge\; (1 + \sqrt 2)(a + b - c).
\]
Rearranging:
\[
  c + (1 + \sqrt 2) c \;\ge\; (1 + \sqrt 2)(a + b), \quad (2 + \sqrt 2) c \;\ge\; (1 + \sqrt 2)(a + b),
\]
\[
  c \;\ge\; \frac{1 + \sqrt 2}{2 + \sqrt 2}(a + b) \;=\; \frac{(1 + \sqrt 2)(2 - \sqrt 2)}{(2 + \sqrt 2)(2 - \sqrt 2)} (a + b) \;=\; \frac{2 - \sqrt 2 + 2\sqrt 2 - 2}{4 - 2}(a + b) \;=\; \frac{\sqrt 2}{2}(a + b) \;=\; \frac{a + b}{\sqrt 2}.
\]
Hence $\sqrt 2 \cdot c \ge a + b$, i.e., $2 c^2 \ge (a + b)^2$. Using $c^2 = a^2 + b^2$:
\[
  2(a^2 + b^2) \;\ge\; (a + b)^2 \;=\; a^2 + 2 a b + b^2 \quad\Longleftrightarrow\quad a^2 - 2 a b + b^2 \;\ge\; 0 \quad\Longleftrightarrow\quad (a - b)^2 \;\ge\; 0.
\]
The last is true, with equality iff $a = b$. Tracing back: $R = (1 + \sqrt 2) r$ iff the right triangle is *isosceles* ($a = b$, with hypotenuse $c = a\sqrt 2$). $\blacksquare$

The trick is that the cumbersome-looking $R \ge (1 + \sqrt 2) r$ collapses, via the algebra above, to the trivial $(a - b)^2 \ge 0$ — a single squared-positive trick. This is Form I (SOS decomposition) applied to a geometric inequality.

---

### Solution to 5.5 — Hadwiger-Finsler Inequality

Set $a = y + z, b = z + x, c = x + y$ with $x, y, z > 0$ (Ravi substitution). The semi-perimeter is $s = x + y + z$, and $s - a = x, s - b = y, s - c = z$. The area, by Heron, is
\[
  \Delta \;=\; \sqrt{s(s - a)(s - b)(s - c)} \;=\; \sqrt{(x + y + z) \cdot xyz}.
\]
The LHS of Hadwiger-Finsler is
\begin{align*}
  2(ab + bc + ca) - (a^2 + b^2 + c^2)
  &= 2\big[(y+z)(z+x) + (z+x)(x+y) + (x+y)(y+z)\big] - \big[(y+z)^2 + (z+x)^2 + (x+y)^2\big] \\
  &= 2\big[x^2 + y^2 + z^2 + 3(xy + yz + zx)\big] - 2\big[x^2 + y^2 + z^2 + (xy + yz + zx)\big] \\
  &= 4(xy + yz + zx).
\end{align*}
(The intermediate expansion: $\sum(y+z)(z+x) = (yz + yx + z^2 + zx) + (zx + zy + x^2 + xy) + (xy + xz + y^2 + yz) = x^2 + y^2 + z^2 + 3(xy + yz + zx)$, and $\sum (y+z)^2 = 2(x^2 + y^2 + z^2) + 2(xy + yz + zx)$.)

The inequality reduces to
\[
  4(xy + yz + zx) \;\ge\; 4\sqrt 3 \cdot \sqrt{(x + y + z) xyz} \quad\Longleftrightarrow\quad (xy + yz + zx)^2 \;\ge\; 3 (x + y + z)(xyz).
\]

This last inequality is a classical *symmetric-polynomial inequality*. Let $p = xy, q = yz, r = zx$. The constraint becomes
\[
  (p + q + r)^2 \;\ge\; 3(pq + qr + rp).
\]
*Proof:* $(p + q + r)^2 = p^2 + q^2 + r^2 + 2(pq + qr + rp)$, so the inequality reduces to $p^2 + q^2 + r^2 \ge pq + qr + rp$, which is the SOS-identity
\[
  p^2 + q^2 + r^2 - pq - qr - rp \;=\; \frac{1}{2}\big[(p - q)^2 + (q - r)^2 + (r - p)^2\big] \;\ge\; 0.
\]

Equality iff $p = q = r$, i.e., $xy = yz = zx$, i.e., $x = y = z$ (assuming positivity), i.e., $a = b = c$ — the *equilateral* triangle.

Hadwiger-Finsler is therefore proved, with equality at the equilateral triangle. $\blacksquare$

This is Form IV (Ravi substitution) followed by Form I (SOS). The Ravi step absorbs the triangle constraint; the SOS step bounds the symmetric polynomial.

---

### Solution to 5.6 — Pedoe's Inequality

Use the law of cosines on triangle 2: $b'^2 + c'^2 - a'^2 = 2 b' c' \cos A'$. Using the area formula $\Delta' = \frac{1}{2} b' c' \sin A'$, so $b' c' = 2 \Delta' / \sin A'$:
\[
  b'^2 + c'^2 - a'^2 \;=\; \frac{4 \Delta' \cos A'}{\sin A'} \;=\; 4 \Delta' \cot A'.
\]
Similarly $c'^2 + a'^2 - b'^2 = 4 \Delta' \cot B'$ and $a'^2 + b'^2 - c'^2 = 4 \Delta' \cot C'$.

The LHS of Pedoe becomes
\[
  a^2 \cdot 4 \Delta' \cot A' + b^2 \cdot 4 \Delta' \cot B' + c^2 \cdot 4 \Delta' \cot C' \;=\; 4 \Delta' (a^2 \cot A' + b^2 \cot B' + c^2 \cot C').
\]
Pedoe reduces to
\[
  4 \Delta' (a^2 \cot A' + b^2 \cot B' + c^2 \cot C') \;\ge\; 16 \Delta \Delta' \quad\Longleftrightarrow\quad a^2 \cot A' + b^2 \cot B' + c^2 \cot C' \;\ge\; 4 \Delta.
\]
This is *Joshi Exercise 24.96(a)*, a one-triangle inequality (relating the sides of triangle 1 to the angles of triangle 2). Its proof is a *Cauchy-Schwarz* argument: by Cauchy-Schwarz applied to the sequences $(a^2 \cot A', b^2 \cot B', c^2 \cot C')$ and $(\sin^2 A', \sin^2 B', \sin^2 C')$ (suitably normalised), the inequality $\sum a^2 \cot A' \ge 4 \Delta$ follows. (Joshi gives the proof in full; we cite it.)

Equality in Pedoe holds iff equality holds in the reducing inequality, which is iff $a^2 \cot A' : b^2 \cot B' : c^2 \cot C' = \sin^2 A' : \sin^2 B' : \sin^2 C'$, simplifying to $a / \sin A' = b / \sin B' = c / \sin C'$ — i.e., the law of sines of triangle 1 holds with the angles of triangle 2, i.e., $A = A', B = B', C = C'$, i.e., the triangles are *similar*. $\blacksquare$

This is Form II (Cauchy-Schwarz) applied to a two-triangle inequality, reduced via *law of cosines + law of sines* to a one-triangle inequality.

---

### Solution to 5.7 — Weighted Cotangent Sum Minimum

Let $\theta_1 + \theta_2 = T$ (constant). We minimise
\[
  F(\theta_1) \;=\; \lambda_1 \cot\theta_1 + \lambda_2 \cot(T - \theta_1).
\]
Setting $F'(\theta_1) = 0$:
\[
  F'(\theta_1) \;=\; -\lambda_1 \csc^2\theta_1 + \lambda_2 \csc^2(T - \theta_1) \;=\; 0,
\]
\[
  \lambda_1 \csc^2 \theta_1 \;=\; \lambda_2 \csc^2 \theta_2, \quad\Longleftrightarrow\quad \frac{\lambda_1}{\sin^2\theta_1} \;=\; \frac{\lambda_2}{\sin^2\theta_2}, \quad\Longleftrightarrow\quad \frac{\sin^2\theta_1}{\sin^2\theta_2} \;=\; \frac{\lambda_1}{\lambda_2}.
\]
Taking the square root (sin is positive on $(0, T)$):
\[
  \boxed{\frac{\sin\theta_1}{\sin\theta_2} \;=\; \sqrt{\frac{\lambda_1}{\lambda_2}}.}
\]

This is the *Snell's-law generalisation*: at the optimum, the *square root of the weight ratio* equals the *sine ratio*. The classical Snell's law of refraction is the special case $\lambda_i = n_i$ (refractive indices), with the minimum being the *time of travel* of a light ray.

*Verification of minimum.* $F''(\theta_1) = 2 \lambda_1 \csc^2\theta_1 \cot\theta_1 - 2\lambda_2 \csc^2\theta_2 \cot\theta_2 \cdot (-1)$… wait, with the chain rule $F'(\theta_1) = -\lambda_1 \csc^2\theta_1 + \lambda_2 \csc^2(T - \theta_1)$, differentiating again:
\[
  F''(\theta_1) \;=\; 2\lambda_1 \csc^2\theta_1 \cot\theta_1 + 2\lambda_2 \csc^2(T - \theta_1) \cot(T - \theta_1).
\]
For $\theta_1, \theta_2 \in (0, \pi/2)$ (so the cotangents are positive), $F'' > 0$, confirming the critical point is a minimum. $\blacksquare$

This is a *Lagrange-multiplier* problem in its elementary form: the angle-sum constraint $\theta_1 + \theta_2 = T$ couples the two angles; the weighted cotangent sum is to be minimised; the optimum is at the *Snell-law* configuration. The pedagogical value is the recognition that the problem's *physical interpretation* (refraction of light through a two-layer medium) is the same as its *mathematical structure*.

---

*End of Chapter 10.*

