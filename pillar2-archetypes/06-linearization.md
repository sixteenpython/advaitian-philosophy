---
chapter: 6
archetype: Linearisation
subtitle: "If Nonlinear, Find the Linear Core Underneath"
category: Method Selection (Archetypes 5–8)
related_archetypes: [5, 11, 17, 18, 20]
key_gems: [B12, E10, F03, F05, F08]
  - "Linearisation $L_a(x) = f(a) + f'(a)(x - a)$ as the best linear approximation"
  - "Mean Value Theorem (Lagrange): $f(b) - f(a) = f'(c)(b - a)$ for some $c \\in (a, b)$"
  - "Rolle's Theorem as the special case $f(a) = f(b) \\Rightarrow f'(c) = 0$"
  - "Taylor's Theorem with remainder: $f(x) = f(a) + f'(a)(x - a) + \\tfrac{1}{2} f''(\\xi)(x - a)^2$"
  - "L'Hôpital's rule as repeated linearisation at an indeterminate limit"
  - "Newton's iteration $x_{n+1} = x_n - f(x_n)/f'(x_n)$ as iterated linearisation"
  - "Characteristic polynomial for constant-coefficient linear ODEs"
  - "Integrating factor as multiplicative linearisation of the LHS"
  - "Euler–Mascheroni constant $\\gamma = \\lim_n (H_{n-1} - \\ln n)$"
  - "Differentiability: $f(x) = f(a) + f'(a)(x - a) + o(x - a)$ as $x \\to a$"
canonical_takeaway: "Replace the nonlinear object by its best linear approximation, then bound the error."
status: locked
last_revised: 2026-05-29
locked_on: 2026-05-29
sourcing_note: "All worked examples and practice problems in this chapter are drawn from K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), or from JEE / RMO / INMO examinations commented on in that text. See Blueprint §6.2 for the sourcing rule and `pillar2-archetypes/_template/joshi-problems-locked.md` §Ch. 6 for the locked slate."
---

# Chapter 6 — Linearisation

## *If Nonlinear, Find the Linear Core Underneath*

---

## Opening Vignette

A surveyor is hired to map a hundred-square-kilometre plot for a city's planning department. She arrives with a theodolite, a steel measuring tape, and a notebook. She does not arrive with a globe. She has never seriously considered that the Earth is round, because at her professional scale, *the Earth is flat*. Her measurements assume Euclidean geometry: parallel lines remain parallel, the angles of every triangle sum to $180°$, the Pythagorean theorem holds exactly. None of these statements is, strictly, true on a spherical Earth. The departures from flat geometry are real — over a hundred kilometres, the curvature of the Earth produces an angle-sum excess of perhaps a few seconds of arc, easily detected by a careful astronomer. But for the surveyor's purpose — siting roads, parcelling property, computing area — the spherical correction is *below her measurement precision*, and incorporating it would complicate her calculations enormously for no gain. The Earth, *in the surveyor's neighbourhood*, is indistinguishable from a plane.

Now consider an aerial scene. A small aircraft passes overhead at three hundred kilometres per hour. To a child watching from the ground, the plane has *a position* and *a direction*, and the child can predict — accurately enough to point a finger at where the plane will be in two seconds — that the plane will continue in a straight line at the same speed. The prediction will be wrong by some metres after thirty seconds, because the plane is actually turning slowly, climbing, drifting in a crosswind. But over two seconds, the linear extrapolation is dead-accurate. The pilot's instruments report essentially the same fact: at each instant, the plane has a velocity vector, and over the next instant, the motion is well approximated by *position plus velocity times time*. The aircraft's actual trajectory is a complicated curve in three-dimensional space; but at any moment, *the linear approximation is the trajectory for as long as it matters*.

These two scenes look unrelated. A surveyor's plot, a child watching a plane. They share one of the most consequential observations in mathematics. In each, *a curved object is approximated, in a small enough neighbourhood, by a flat or linear object*, and the approximation is so accurate within that neighbourhood that the underlying curvature simply does not enter the working description. The Earth is a sphere; the surveyor treats it as a plane. The plane's trajectory is curved; the child treats it as a straight line. Neither observer is naive. They have, instinctively, made the right approximation for the right scale.

This is *Linearisation*. It is the second archetype of the *Method Selection* sub-pillar, and where Substitution chose any clever variable to make a problem tractable, Linearisation commits to one specific variable — the *deviation from a chosen reference point* — and one specific approximation — the *tangent line, plane, or hyperplane* of the function at that point. The trade is that Linearisation is *only* a local statement, and its accuracy degrades as one moves away from the reference point. The astonishing fact, which this chapter will develop, is that the local statement is enough for an enormous range of problems: rate-of-change problems, tangent-line geometry, Newton's method for root-finding, the first-order theory of differential equations near an equilibrium, error analysis in numerical computation, perturbation theory in physics, and — most consequentially — the entire edifice of differential calculus.

Calculus is, on the deepest reading, the systematic study of one move: *replace a nonlinear object by its best linear approximation, work in the linear setting, and bound the error*. Newton and Leibniz did not discover linearisation; they discovered the bookkeeping that makes linearisation rigorous. The bookkeeping is the calculus.

> *In a small enough neighbourhood, every smooth function is its tangent line. The trained solver knows what "small enough" means and what to do with the tangent once it is found.*

---

## 1. The Archetype Defined

### 1.1 Formal Definition

We make the intuition precise.

\begin{definition}[Linearisation]
Let $f : I \to \mathbb{R}$ be a function differentiable at a point $a \in I$ (where $I$ is an open interval). The *linearisation of $f$ at $a$* is the affine function
\[
  L_a(x) \;=\; f(a) + f'(a)(x - a).
\]
The linearisation is uniquely characterised by the two conditions
\[
  L_a(a) \;=\; f(a), \qquad L_a'(a) \;=\; f'(a),
\]
that is, $L_a$ is the unique affine function that agrees with $f$ in both *value* and *first derivative* at $a$.
\end{definition}

Three points are worth unpacking. First, *the linearisation is local*. It is an excellent approximation to $f$ near $a$ and a generally poor one far from $a$. The error
\[
  E_a(x) \;:=\; f(x) - L_a(x)
\]
satisfies $E_a(a) = 0$, $E_a'(a) = 0$, and (when $f$ is twice differentiable) $E_a(x) = O((x - a)^2)$ as $x \to a$. The linearisation is the *unique* affine function for which the error decays *faster than linearly* — and this is the precise sense in which it is the *best* linear approximation.

Second, the definition extends to higher dimensions almost without change. For a differentiable function $f : \mathbb{R}^n \to \mathbb{R}$ at a point $\mathbf a$, the linearisation is
\[
  L_{\mathbf a}(\mathbf x) \;=\; f(\mathbf a) + \nabla f(\mathbf a) \cdot (\mathbf x - \mathbf a),
\]
where $\nabla f(\mathbf a) = (\partial f / \partial x_1, \ldots, \partial f / \partial x_n)|_{\mathbf x = \mathbf a}$ is the gradient at $\mathbf a$. For vector-valued $\mathbf f : \mathbb{R}^n \to \mathbb{R}^m$, the linearisation is $L_{\mathbf a}(\mathbf x) = \mathbf f(\mathbf a) + J_{\mathbf f}(\mathbf a)(\mathbf x - \mathbf a)$, where $J_{\mathbf f}(\mathbf a)$ is the Jacobian matrix. The structural fact — *the best linear approximation is the unique affine function agreeing with $f$ in value and first derivative* — survives in every dimension.

Third, *the differentiability of $f$ at $a$ is precisely the existence of a linear approximation with $o(x - a)$ error*. Differentiability is *not* defined as "the limit of difference quotients exists"; that is a *consequence* of the more basic definition
\[
  f(x) \;=\; f(a) + f'(a)(x - a) + o(x - a) \qquad \text{as } x \to a.
\]
The little-$o$ notation means: $\lim_{x \to a} [f(x) - L_a(x)] / (x - a) = 0$. The function $f'(a)$ — usually called the *derivative* — is defined as the *unique slope* such that this asymptotic identity holds. *Differentiability is linearisability*, and the derivative is the slope of the linearisation.

In this chapter we will encounter four characteristic forms of linearisation. As with previous archetypes, the taxonomy is not disjoint — a Mean Value Theorem application is at once Form I and Form III — but the four forms give a working diagnostic.

- **Form I — Tangent line (single variable).** $f(x) \approx f(a) + f'(a)(x - a)$ for $x$ near $a$. The most elementary form, used in tangent-line geometry, numerical estimation ($\sqrt{4.04} \approx 2 + (0.04)/(2 \cdot 2) = 2.01$), and Newton's method (the next iterate is where the tangent line crosses zero). *Examples.* WE1 (Tangent-Triangle Area), PP1 ($\sin(\pi\cos^2 x)/x^2$ limit), PP3 ($e^x - 1 - x$ limit), PP7 (Newton's method for $\sqrt{5}$).

- **Form II — Multivariable linear approximation.** $f(\mathbf x) \approx f(\mathbf a) + \nabla f(\mathbf a) \cdot (\mathbf x - \mathbf a)$ for $\mathbf x$ near $\mathbf a$. Used in error propagation (the delta method in statistics), in marginal analysis (economics), and in tangent-plane geometry. Less prominent in JEE-level problems but essential for the wider mathematical landscape.

- **Form III — Existence theorems via local linearity.** The Mean Value Theorem and Rolle's Theorem assert *the existence of a point* at which the local linearisation is exact. *Examples.* PP4 (Rolle's theorem on $f(x) = x^3 - 6x^2 + 11x - 6$), PP5 (MVT bound on $|\sin a - \sin b|$). The form is foundational: the entirety of single-variable existence-of-extrema theory rests on it.

- **Form IV — Operator linearisation.** A differential operator $L$ acting on functions, near a "reference" function (often zero or an equilibrium), is approximated by its linear part. *Examples.* WE3 (linear constant-coefficient ODE $y'' - 3y' + 2y = 0$ solved via the characteristic polynomial), PP6 (integrating-factor method for first-order linear ODEs). The form generalises to vector fields near equilibria (linear stability analysis) and to partial differential equations.

### 1.2 The Core Principle

The principle of linearisation, stripped to its essence, is one sentence.

> *Replace the curve by its tangent; in a small enough neighbourhood, the tangent is the curve.*

This sentence inverts a deeply ingrained reading habit. When a novice encounters a problem involving a nonlinear function — a quadratic, a transcendental, an algebraic radical — the instinct is to *compute with the nonlinear function directly*, using whatever identities or algebraic manipulations are available. The instinct is not wrong; on many problems it is the right move. But it overlooks a powerful alternative: *if only local information is needed, replace the function by its tangent at the relevant point, and compute with the tangent instead*. The tangent is a polynomial of degree $1$, the simplest non-trivial function class; computation in the tangent is trivial; the result is *exact for the linearisation* and *approximate for the function*, with an error that is one order smaller than any first-order quantity.

To see the move in miniature, consider the limit
\[
  \lim_{x \to 0} \frac{\sin x}{x}.
\]
The novice may try to compute the limit by a $\delta$-$\epsilon$ argument or by squeeze theorem on $\cos x \le \sin x / x \le 1$. Both approaches work and give the answer $1$. But the linearisation-trained student executes one line: *near $x = 0$, $\sin x = x + O(x^3)$ by Taylor, so $\sin x / x = 1 + O(x^2) \to 1$*. The "computation" is the recognition that the leading-order behaviour of $\sin x$ near $0$ is *linear* with slope $1$, hence $\sin x / x = 1$ in the limit. The full transcendental nature of the sine function is irrelevant; only its tangent at $0$ matters.

The principle generalises. Every *indeterminate limit* of type $0/0$, $\infty/\infty$, or $0 \cdot \infty$ is, structurally, a problem to be solved by linearisation. L'Hôpital's rule — replace numerator and denominator by their derivatives at the limiting point — is the operational form of "compute with the leading-order Taylor terms." Repeated application of L'Hôpital is repeated linearisation: each round of differentiation extracts one more Taylor coefficient. The student who has internalised linearisation recognises L'Hôpital not as a separate rule but as the natural consequence of "$\sin x \approx x$ near $0$, $e^x \approx 1 + x$ near $0$, $\cos x \approx 1 - x^2/2$ near $0$" — the Taylor lookup table of basic functions. We will work several such examples in §4 and §5.

The principle is sharper than its formulation suggests. *Most* problems involving smooth functions can be reduced, by appropriate linearisation, to problems about linear functions. The work is in *choosing the right point of linearisation* and *bounding the error correctly*. We will see throughout the chapter that the right point is usually dictated by the problem (the point where the answer is sought; the equilibrium of a dynamical system; the root being approximated) and that the error bound is usually a Taylor remainder or a Mean Value Theorem estimate.

### 1.3 The Cognitive Shift

Understanding linearisation intellectually is one matter; reaching for it instinctively is another. The difficulty is again a habit installed early. From their first encounter with nonlinear functions, students are trained to *compute with the function as given*: factor a quadratic, apply a trig identity, expand a binomial. The cognitive habit is to treat the function as the working object. When the function is too complex to manipulate directly, the student feels stuck — they have not been trained to *replace* the function by something simpler.

The cognitive shift is small in form and large in consequence. Most students, on encountering a nonlinear function in a problem, immediately ask: *how do I manipulate this function?* The linearisation-trained solver asks instead: *do I need the full function, or do I only need its behaviour near a point?* If the latter — which is the case in any problem about limits, tangents, rates of change, or local extrema — the trained solver replaces the function by its linearisation at the relevant point and proceeds with the polynomial of degree $1$ that results. The replacement is *exact* in its first-order content and the error is *bounded* by the Taylor remainder.

Consider how the shift plays out concretely on a problem we will treat in §4.1. The problem asks: *the tangent to the curve $f(x) = x^2 + bx - b$ at the point $(1, 1)$ forms a triangle with the coordinate axes of area $2$; find $b$.* The novice reads the problem and pauses: the *curve* is a parabola, and parabolas are not lines, so how does one talk about the "tangent" without first developing some calculus machinery? The trained solver writes immediately:
\[
  L_1(x) \;=\; f(1) + f'(1)(x - 1) \;=\; 1 + (2 + b)(x - 1),
\]
identifies the $x$- and $y$-intercepts of this linear function, sets up the area equation, and solves for $b$. The parabola is irrelevant; only its tangent at $(1, 1)$ matters; the tangent is a line; lines are easy. The full computation takes four lines.

The two solvers differ not in algebraic skill but in *first move*. The trained solver has recognised that the problem asks for a property of the *tangent* — a linear object — at a *specific point*, and has linearised the parabola at that point before doing any geometry. The novice would, eventually, write the same tangent equation, but only after a struggle with the unfamiliar concept of "tangent to a curve."

This shift manifests in four habits that distinguish linearisation-aware solvers.

1. **A reflexive recognition of "local" problems.** Limits, tangents, rates of change, marginal quantities, small perturbations, error propagation, Newton's method, stability of equilibria — all of these are *local* in the precise sense that only the linearisation of the relevant function matters. The trained solver recognises these problem types at sight and reaches for the linearisation without further thought.

2. **A mental Taylor-table of common functions.** The five most useful local expansions — $\sin x = x + O(x^3)$, $\cos x = 1 - x^2/2 + O(x^4)$, $e^x = 1 + x + x^2/2 + O(x^3)$, $\ln(1 + x) = x - x^2/2 + O(x^3)$, $(1 + x)^\alpha = 1 + \alpha x + O(x^2)$ — are the trained solver's Rolodex. Every limit problem they meet, they translate into operations on these basic Taylor expansions.

3. **A habit of writing $L_a(x)$ explicitly.** Linearisation is most fluent when the linearisation function is written as a *new symbol*, distinguishing it from the original $f$. This externalisation prevents the common error of confusing $f$ (full function) with $L_a$ (its tangent) mid-computation.

4. **Disciplined error tracking.** The linearisation is approximate; the error is $O((x - a)^2)$. In problems where the answer is sought *to a given precision*, the error must be tracked. The trained solver knows when the linear approximation suffices (most problems, in practice) and when a higher-order term is needed (precision-sensitive numerical work). The discipline is *one order higher than the answer demands*: if the answer is wanted to leading order, the linearisation suffices; if to second-order accuracy, the quadratic Taylor term is needed.

The fourth habit is, again, the hardest. The error term is invisible in the computation — the linear approximation looks like an exact identity, and the temptation is to treat it as one. The trained solver knows that the equation $f(x) = L_a(x)$ is *not* an identity but an approximation, and they keep the error term in mind as a *bound* on how far the approximation can be trusted.

---

## 2. The Deep Structure

### 2.1 Mathematical Foundations

The strategy of linearisation, like the previous five archetypes, is a feature of mathematical architecture and not a problem-solving technique invented in isolation. The foundational architecture is the *fundamental theorem of differential calculus*: every differentiable function admits a unique best linear approximation at every point of its domain, and the error of this approximation decays faster than linearly. Calculus, on this reading, is the systematic exploitation of this single fact.

Three foundational theorems organise the linearisation archetype for our purposes.

\begin{theorem}[Mean Value Theorem (Lagrange, 1797)]
Let $f : [a, b] \to \mathbb{R}$ be continuous on the closed interval $[a, b]$ and differentiable on the open interval $(a, b)$. Then there exists a point $c \in (a, b)$ such that
\[
  f(b) - f(a) \;=\; f'(c)\,(b - a).
\]
\end{theorem}

The Mean Value Theorem (henceforth MVT) is the *exact* form of linearisation. It asserts that for any chord of the graph of $f$ (the line segment from $(a, f(a))$ to $(b, f(b))$), there is some intermediate point $c$ at which the tangent line has the same slope as the chord. The chord *is* the linearisation between two points; the tangent at $c$ *is* the local linearisation at $c$; the MVT says they have the same slope. The theorem is the structural reason that local linearisations contain global information: by integrating local slopes (via the fundamental theorem of calculus), one recovers global differences.

\begin{theorem}[Rolle's Theorem (Rolle, 1691)]
Let $f : [a, b] \to \mathbb{R}$ be continuous on $[a, b]$, differentiable on $(a, b)$, with $f(a) = f(b)$. Then there exists a point $c \in (a, b)$ such that $f'(c) = 0$.
\end{theorem}

Rolle's Theorem is the special case of the MVT in which the chord has zero slope. Geometrically, if a smooth function takes the same value at two distinct points, then somewhere strictly between them, its tangent is horizontal. The theorem is the existence-theoretic content of "between two equal values, there must be a turn." It is the foundational tool for *locating critical points of derivatives* and is the linearisation-theoretic analogue of the Intermediate Value Theorem (which locates zeros of continuous functions). We use Rolle in PP4.

\begin{theorem}[Taylor's Theorem with Remainder]
Let $f : I \to \mathbb{R}$ be $(n + 1)$ times differentiable on an open interval $I$ containing $a$. Then for every $x \in I$, there exists a point $\xi$ strictly between $a$ and $x$ such that
\[
  f(x) \;=\; \sum_{k = 0}^{n} \frac{f^{(k)}(a)}{k!}\,(x - a)^k \;+\; \frac{f^{(n + 1)}(\xi)}{(n + 1)!}\,(x - a)^{n + 1}.
\]
\end{theorem}

Taylor's Theorem is the generalisation of the linearisation. The case $n = 0$ is the MVT (with $f^{(1)}(\xi) = f'(c)$); the case $n = 1$ extends the linearisation $L_a(x) = f(a) + f'(a)(x - a)$ to the quadratic approximation $L_a(x) + (1/2) f''(\xi)(x - a)^2$. The general case provides a polynomial approximation of any desired order, with the remainder bound expressed in terms of an unknown intermediate point $\xi$ and the next derivative $f^{(n + 1)}(\xi)$. The remainder bound is the rigorous content of "the error in linearisation is $O((x - a)^2)$."

A fourth observation deserves comment, though it is not, strictly, a theorem: *the derivative is the linearisation*. The standard textbook definition of the derivative as a limit of difference quotients is *equivalent* to (but pedagogically obscure compared with) the definition of $f'(a)$ as the *unique slope* such that $f(x) = f(a) + f'(a)(x - a) + o(x - a)$. The two definitions are interchangeable, but the second exposes the structural content: *the derivative is the slope of the local linearisation*, and differentiability is the property of *being linearisable to first order with error $o(x - a)$*. Once this view is internalised, the derivative becomes a concrete object — *the slope of the tangent* — rather than the somewhat mysterious limit of a quotient.

### 2.2 Physical and Cross-Domain Foundations

The linearisation archetype has rich cross-domain instances. We mention four.

In *classical mechanics*, the *linearisation of a restoring force about an equilibrium* is the foundational technique of small-oscillation theory. A pendulum's equation of motion is $\ddot\theta = -(g/L) \sin\theta$, exact for any amplitude. For small $\theta$, the linearisation $\sin\theta \approx \theta$ yields $\ddot\theta = -(g/L)\theta$ — the equation of simple harmonic motion, with period $2\pi\sqrt{L/g}$ independent of amplitude. The full pendulum is nonlinear and admits no closed-form solution; the linearised pendulum is *the* textbook example of harmonic motion. The same move underlies the small-oscillation analysis of every physical equilibrium: replace the restoring force by its tangent at equilibrium, solve the linear problem, accept that the analysis is valid for amplitudes small compared with the radius of validity of the linearisation.

In *electrical engineering*, the *small-signal model* of a transistor or amplifier is the linearisation of the device's full nonlinear input-output characteristic about a chosen *operating point* (or *quiescent point* or *Q-point*). The device's actual behaviour is nonlinear in the input voltage; the small-signal model treats the device as a linear amplifier with constant gain, valid for input fluctuations small compared with the operating-point voltage. The success of analogue electronics rests on this approximation: every analogue circuit is *designed* to operate at a Q-point at which the linearisation is accurate, and the circuit's transfer function is computed in the linearised model. When the input becomes large, the linearisation breaks down — this is the onset of *distortion*, and it is the engineer's signal to reduce input amplitude or accept the nonlinear consequences.

In *economics*, the *marginal cost*, *marginal revenue*, *marginal utility* concepts are all linearisations of the corresponding total functions. Total cost $C(q)$ as a function of quantity $q$ is generally nonlinear; the marginal cost $C'(q)$ is the slope of the local linearisation, interpretable as "the cost of producing one more unit, *if the production were to continue at the current rate*." The marginal-analysis framework of microeconomics is, structurally, the systematic application of linearisation to economic functions, with each marginal quantity being the derivative of the corresponding total. The *first-order optimality conditions* of constrained optimisation (Lagrange multipliers, KKT conditions) are linearisation statements about the gradient of the objective at the optimum.

In *statistics*, the *delta method* for the asymptotic distribution of a smooth function of an estimator is the linearisation of the function at the true parameter value. If $\hat\theta$ is a consistent estimator of $\theta$ with $\sqrt n(\hat\theta - \theta) \to N(0, \sigma^2)$, then for a smooth function $g$, the linearisation $g(\hat\theta) \approx g(\theta) + g'(\theta)(\hat\theta - \theta)$ yields $\sqrt n(g(\hat\theta) - g(\theta)) \to N(0, (g'(\theta))^2 \sigma^2)$ by the central limit theorem. The delta method is the workhorse of asymptotic statistical analysis and is, structurally, one line of linearisation plus the convergence of linear combinations of normal random variables.

The point is the same in each case: *the world is locally linear*, and the practitioner's task is to identify the right point of linearisation, perform the linearisation explicitly, and work within the linear theory for as long as it is accurate. Linearisation in mathematics is the formal expression of an operational principle that pervades every quantitative discipline.

### 2.3 Cognitive Foundations

The cognitive function that allows a human solver to reach for linearisation fluently is what philosophers of mathematics sometimes call *local-global reasoning* — the capacity to recognise that a global object (a curve, a vector field, a manifold) is, at every point, well-approximated by a simpler local object (a line, a constant vector, a plane), and that many problems about the global object reduce to problems about its local approximations.

Local-global reasoning is *learned*. It is built up by working through the canonical examples of linearisation — tangent lines to parabolas, small-oscillation analysis of pendulums, Newton's method for square roots — until the move becomes instinctive. A student who has computed twenty tangent lines learns to *see* the tangent before computing it. A student who has solved a dozen linearisation-of-pendulum problems learns to *recognise* small-oscillation regimes at sight. The recognition is not memorisation of a formula; it is structured pattern matching built up by use.

A further cognitive ingredient deserves comment. Linearisation requires the solver to *trust the approximation* — to commit to working in the linearised setting and treat the result as if exact, while keeping a separate mental track of the error bound. This is a non-trivial cognitive load: the working memory is asked to hold two representations (the linearisation and the error term) simultaneously, while computing fluently in the first. Novices often *forget* the error term or *over-trust* the linearisation outside its radius of validity. The discipline of explicitly writing "$+ O((x - a)^2)$" after every Taylor expansion is the externalisation that compensates for the cognitive cost.

The mature mathematician trusts the linearisation in the right neighbourhood and rejects it outside; the boundary of "right" and "outside" is something the practitioner has internalised through experience. The student arriving at olympiad-level work is still building this judgment. A useful exercise is to take a non-trivial nonlinear function (a polynomial of degree $5$, say), linearise it at several different points, and compare the linearisation with the actual function on intervals of increasing size. The exercise builds intuition for the size of the radius of accuracy and for the way the error grows quadratically (or worse) away from the linearisation point.

---

## 3. The Diagnostic Toolkit

### 3.1 The Three Questions Method (Linearisation Edition)

We now collect, in operational form, the questions a trained solver asks on first contact with a problem that may admit a linearisation.

**Question 1 — Where is the linearisation to be performed?** Linearisation is local: it requires a specific point $a$ at which to compute $f(a)$ and $f'(a)$. The point is dictated by the problem: it is the point where a tangent is sought (tangent-line geometry), the point at which a limit is taken (indeterminate forms), the equilibrium of a dynamical system (stability), or the point at which an iteration begins (Newton's method). Identifying the point is the first move.

**Question 2 — What is $L_a(x) = f(a) + f'(a)(x - a)$ explicitly?** Compute the linearisation as a concrete affine function of $x$. The computation is two evaluations ($f(a)$, $f'(a)$) and one substitution into the formula; it is mechanical. Writing the linearisation as a *separate symbol* $L_a$ rather than informally substituting "$\approx$" for "$=$" reinforces the discipline of distinguishing the function from its approximation.

**Question 3 — What is the error, and does the problem care?** The linearisation error is $f(x) - L_a(x) = O((x - a)^2)$ as $x \to a$ (when $f$ is twice differentiable). For most problems — tangent-line geometry, leading-order limits, first-order existence theorems — the error does not enter the answer; the linearisation itself is the answer. For precision-sensitive problems (numerical computation to a given decimal accuracy; iterative methods with convergence-rate analysis), the error must be bounded explicitly via Taylor's remainder. Identifying which class of problem one is in is the third move.

The Three Questions Method (Linearisation Edition) is the conversation between a novice and an experienced solver, internalised. Practising it for a few weeks installs it as instinct.

### 3.2 Forms of Linearisation: A Comprehensive Guide

We now lay out, for reference, the four canonical forms of linearisation and a working diagnostic for each.

- **Form I — Tangent line (single variable).** *Diagnostic.* The problem involves a smooth function on $\mathbb{R}$ and asks about local behaviour at or near a specific point: the tangent line, a local linear estimate ($\sqrt{4.04}$ from $\sqrt 4 = 2$), the first non-vanishing term of a Taylor expansion, the limit of an indeterminate form. *Move.* Compute $L_a(x) = f(a) + f'(a)(x - a)$. *Primer.* For $\sqrt{1 + x}$ near $x = 0$: $f(0) = 1$, $f'(0) = 1/2$, so $L_0(x) = 1 + x/2$. Numerical estimates: $\sqrt{1.04} \approx 1.02$ (actual $\sqrt{1.04} = 1.0198\ldots$, error $\sim 0.0002$). *Examples.* WE1 (tangent-triangle area), PP1 ($\sin(\pi\cos^2 x)/x^2$), PP3 ($e^x - 1 - x$).

- **Form II — Multivariable linear approximation.** *Diagnostic.* The problem involves a smooth function on $\mathbb{R}^n$ and asks about local behaviour. *Move.* Compute the gradient $\nabla f(\mathbf a)$ and form $L_{\mathbf a}(\mathbf x) = f(\mathbf a) + \nabla f(\mathbf a) \cdot (\mathbf x - \mathbf a)$. *Primer.* Less common in JEE-level work; central to economics (marginal analysis), statistics (delta method), and optimisation. We do not treat a Form II worked example in this chapter but note its existence for completeness.

- **Form III — Existence theorems via local linearity.** *Diagnostic.* The problem asks for the *existence* of a point at which a derivative satisfies some condition: a horizontal tangent (Rolle), a chord-matching tangent (MVT), an intermediate value of a derivative (Darboux). The full nonlinear function is irrelevant; only the local-linear behaviour matters. *Move.* Apply the appropriate existence theorem (Rolle, MVT, Cauchy, generalised MVT). The theorem produces the existence of a point $c$ in some interval; properties of $f'(c)$ then yield the conclusion. *Examples.* PP4 (Rolle locates roots of $f' = 3x^2 - 12x + 11$ in $(1, 2)$ and $(2, 3)$), PP5 (MVT bounds $|\sin a - \sin b| \le |a - b|$).

- **Form IV — Operator linearisation.** *Diagnostic.* The problem is a differential equation, a difference equation, or an evolution equation, with a linear differential operator $L$ acting on functions. *Move.* The kernel of $L$ (homogeneous solutions) is determined by the *characteristic polynomial* for constant-coefficient operators, or by the structure of $L$ for variable-coefficient operators. Particular solutions are constructed by integrating factors, variation of parameters, or Laplace transforms. *Examples.* WE3 (constant-coefficient linear ODE $y'' - 3y' + 2y = 0$), PP6 (integrating-factor method for $y' + (2/x) y = \sin x / x^2$).

The four forms are not mutually exclusive. Newton's method (PP7) is Form I in execution (each step is a tangent-line approximation) and Form III conceptually (existence of fixed points of the Newton iteration). L'Hôpital's rule (PP3) is Form I in execution and Form III in justification (the existence of a limit follows from the existence of derivatives). The trained solver does not parse a problem into its forms in the moment; the forms are a *retrospective* taxonomy, useful for catalogue and pedagogy. In the moment, the solver simply *linearises at the appropriate point and proceeds*.

### 3.3 Common Pitfalls

The linearisation archetype exposes the solver to five recurring errors. Knowing them in advance is half the cure.

**Pitfall 1 — Linearising outside the radius of validity.** The tangent-line approximation $\sqrt{1 + x} \approx 1 + x/2$ is excellent for $|x| < 0.1$ (error $\sim x^2/8$) and dreadful for $|x| > 0.5$ (error $\sim 0.03$). A solver who applies the linearisation to compute $\sqrt{10}$ from $\sqrt 1 = 1$ (taking $x = 9$ and writing $\sqrt{10} \approx 1 + 9/2 = 5.5$, when the true value is $3.16$) has committed Pitfall 1. The cure is to *choose the linearisation point close to the value of interest* — for $\sqrt{10}$, use $\sqrt 9 = 3$ as the base point, giving $\sqrt{10} \approx 3 + 1/(2 \cdot 3) = 3.167$, much closer to the true value.

**Pitfall 2 — Linearising at a non-differentiable point.** The function $f(x) = |x|$ is not differentiable at $x = 0$; it has a corner, not a tangent line. A solver who attempts to "linearise $|x|$ at $0$" by setting $f'(0) = 0$ (since $|x|$ takes the value $0$ at $0$ and is non-negative everywhere) produces nonsense; the true behaviour of $|x|$ near $0$ is *not* well-approximated by any single line, because the left and right derivatives differ. The cure is to *verify differentiability* before linearising, and where one-sided differentiability is the best one can do (corners, cusps), to use separate one-sided linearisations.

**Pitfall 3 — Confusing linearisation with global linear approximation.** The linearisation $L_a$ is an excellent approximation *near* $a$ and a poor one far from $a$. A solver who uses the linearisation $L_0(x) = 1 + x$ for $e^x$ to compute, say, $e^{10} \approx 11$ (when the true value is $\approx 22026$) has committed Pitfall 3. The cure is to *remember the local nature* of linearisation and reach for global techniques (full Taylor series, asymptotic expansions, contour integrals) for global problems.

**Pitfall 4 — Forgetting the higher-order term in precision-sensitive computations.** In numerical analysis, the linearisation error $O((x - a)^2)$ is the *only* error if the linearisation is computed exactly. A solver who needs an answer to four decimal places from a linearisation with quadratic error of order $10^{-2}$ has not achieved the required precision; they need a quadratic Taylor term, or a smaller step from $a$. The cure is to *bound the error explicitly* using Taylor's remainder and verify it satisfies the precision target.

**Pitfall 5 — Applying L'Hôpital to a determinate limit.** L'Hôpital's rule applies to indeterminate forms $0/0$ and $\infty/\infty$; applied to a determinate limit, it produces a wrong answer. A solver who computes $\lim_{x \to 0} (x + 1) / (x + 2)$ by L'Hôpital, getting $\lim 1/1 = 1$ (when the true value is $1/2$), has committed Pitfall 5. The cure is to *verify the indeterminate form* before applying L'Hôpital.

The five pitfalls share a common root: *linearisation is not free*; it carries a bounded error, applies only in a bounded neighbourhood, and presupposes differentiability. The disciplined solver tracks each of these constraints.

---

## 4. Worked Examples

We turn now from the diagnostic to the operational. Three worked examples follow. Each illustrates a distinct form of linearisation. Each is sourced from K.D. Joshi's *Educative JEE Mathematics* — Chapters 19 and 24, with cross-references to Chapters 15, 16. The presentation follows the six-point framework of Pillar 1: Seed, Brute Path, Elegant Pivot, Pitfalls, Connections, Takeaway.

### 4.1 Example 1 — Tangent-Triangle Area

\begin{problem}
The tangent to the curve $f(x) = x^2 + bx - b$ at the point $(1, 1)$, together with the coordinate axes, bounds a triangle that lies entirely in the first quadrant and has area $2$. Find $b$.
\end{problem}

**Source.** JEE 2001; K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), Chapter 24, Exercise 24.35.

**Seed.** The problem mixes calculus and coordinate geometry. The calculus content is the *tangent line at $(1, 1)$* — a Form-I linearisation of the parabola $f$ at $x = 1$. The geometric content is the *triangle bounded by the tangent and the axes*, an area-based equation in the slope $f'(1)$. Once the linearisation is computed, the geometry is a one-line area-of-triangle problem. The structural difficulty is identifying that *only the tangent line matters* — the rest of the parabola is irrelevant to the problem. (Sanity check: $f(1) = 1 + b - b = 1$, so the point $(1, 1)$ lies on the curve for every $b$. The problem is well-posed.)

**Brute path.** Attempt to write the parabola, its tangent at $(1, 1)$, and the resulting triangle in some unified framework, perhaps in terms of the discriminant or by guessing values of $b$. The approach is not exactly wrong but is needlessly indirect: the tangent line itself, computed by linearisation, *is* the object the problem is about.

**Elegant pivot.** Linearise $f$ at $x = 1$. We compute
\[
  f(1) \;=\; 1 + b - b \;=\; 1, \qquad f'(x) \;=\; 2x + b, \qquad f'(1) \;=\; 2 + b.
\]
The linearisation is
\[
  L_1(x) \;=\; 1 + (2 + b)(x - 1).
\]
This is the tangent line at $(1, 1)$.

*Intercepts.* The $y$-intercept is $L_1(0) = 1 + (2 + b)(0 - 1) = 1 - (2 + b) = -1 - b$. The $x$-intercept is the solution to $L_1(x) = 0$, i.e., $1 + (2 + b)(x - 1) = 0$, giving $x = 1 - 1/(2 + b) = (1 + b)/(2 + b)$ (provided $2 + b \ne 0$).

*First-quadrant constraint.* The triangle bounded by the tangent and the coordinate axes lies in the first quadrant if and only if both intercepts are positive. The $y$-intercept $-1 - b > 0$ requires $b < -1$. The $x$-intercept $(1 + b)/(2 + b) > 0$ requires $1 + b$ and $2 + b$ to have the same sign; combined with $b < -1$ (so $1 + b < 0$), we need $2 + b < 0$, i.e., $b < -2$.

So $b < -2$ is the working range.

*Area equation.* The triangle has legs $|x\text{-intercept}|$ and $|y\text{-intercept}|$ along the axes; its area is half the product:
\[
  \mathrm{Area} \;=\; \tfrac{1}{2}\,|x\text{-intercept}|\,|y\text{-intercept}| \;=\; \tfrac{1}{2} \cdot \frac{|1 + b|}{|2 + b|} \cdot |1 + b| \;=\; \frac{(1 + b)^2}{2\,|2 + b|}.
\]
Setting this equal to $2$ and noting that $|2 + b| = -(2 + b)$ for $b < -2$:
\[
  \frac{(1 + b)^2}{-2(2 + b)} \;=\; 2 \quad\Longleftrightarrow\quad (1 + b)^2 \;=\; -4(2 + b) \;=\; -8 - 4b.
\]
Expanding the left side: $(1 + b)^2 = 1 + 2b + b^2$. So
\[
  b^2 + 2b + 1 \;=\; -8 - 4b \quad\Longleftrightarrow\quad b^2 + 6b + 9 \;=\; 0 \quad\Longleftrightarrow\quad (b + 3)^2 \;=\; 0.
\]
Hence $b = -3$ is the unique solution.

*Verification.* At $b = -3$: slope $f'(1) = 2 + (-3) = -1$. Tangent: $y - 1 = -(x - 1)$, i.e., $y = 2 - x$. $x$-intercept at $x = 2$; $y$-intercept at $y = 2$. Triangle vertices $(0, 0)$, $(2, 0)$, $(0, 2)$; area $= (1/2)(2)(2) = 2$. ✓ $\blacksquare$

**Pitfalls.**
- Failing to verify that the problem statement makes the point $(1, 1)$ lie on the curve. The verification $f(1) = 1$ for all $b$ is a one-line check that the setup is consistent. A solver who skipped this check might worry the problem is over-determined.
- Forgetting that the first-quadrant condition restricts the working range of $b$. Without the restriction $b < -2$, the area equation may admit spurious solutions corresponding to triangles in other quadrants.
- Sign errors in the absolute value. The intercepts are negative when $b < -2$; carrying their absolute values through the area equation is essential.
- Failing to verify the answer geometrically. The check that the triangle $(0, 0)$, $(2, 0)$, $(0, 2)$ has area $2$ takes one line and validates the entire chain of reasoning.

**Connections.**
- The linearisation $L_1(x)$ is the *first-order Taylor expansion* of $f$ about $x = 1$. The next-order Taylor term, $f''(1)(x - 1)^2 / 2 = (x - 1)^2$, captures the *curvature* of the parabola — the deviation of the parabola from its tangent. For the area-of-triangle problem, only the tangent line matters; the parabola's curvature is irrelevant. This is the characteristic posture of Form-I linearisation: *use only the information you need*.
- The same linearisation-and-area technique solves a wide class of *tangent-line geometry* problems: tangent to an ellipse at a point, tangent to a hyperbola, tangent to a polar curve, normal line and its intercept. In each case, the calculus produces a line; the geometry produces an equation in the line's parameters; standard algebra solves for the unknown.
- The condition $(b + 3)^2 = 0$ — a *repeated root* — is characteristic of problems with a *unique* extremal configuration. In algebraic terms, the area function (as a function of $b$ for $b < -2$) is minimised at $b = -3$ and equals $2$ at that minimum; the area $2$ is achieved at exactly one value of $b$.

**Takeaway.** *Whenever a problem mixes a smooth curve with geometric or algebraic operations on its tangent line, linearise the curve at the relevant point and proceed in the affine world. The tangent is a line of degree $1$; lines are easy; computations in lines are mechanical. The original curve's higher-order behaviour is irrelevant to tangent-line problems and should be set aside without regret.*

### 4.2 Example 2 — Harmonic Numbers vs. $\ln n$

\begin{problem}
Let $H_n = 1 + \tfrac{1}{2} + \tfrac{1}{3} + \cdots + \tfrac{1}{n}$ denote the $n$-th partial sum of the harmonic series. Prove that for all integers $n \ge 2$,
\[
  H_n - 1 \;<\; \ln n \;<\; H_{n - 1},
\]
and prove that the sequence $a_n := H_{n - 1} - \ln n$ is increasing and bounded above by $1$.
\end{problem}

**Source.** K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), Chapter 24, Exercise 24.48.

**Seed.** The problem juxtaposes a *discrete* quantity ($H_n$, a partial sum of $1/k$ over integers) with a *continuous* quantity ($\ln n = \int_1^n (1/x)\,dx$, the integral of $1/x$ on a real interval). The connection between the two is the *linearisation of $1/x$ on each unit interval* $[k, k + 1]$: $1/x$ is well-approximated by its endpoint values, and the integral on each unit interval is sandwiched between the endpoint values. Summing the sandwiches yields the desired inequality. The structural insight is that *a Riemann-sum sandwich is a linearisation sandwich on each subinterval*.

**Brute path.** Compute $H_n$ and $\ln n$ numerically for small $n$, observe the inequality empirically, and attempt to prove it by induction. The induction goes through but is unenlightening: it does not expose *why* the sandwich is tight, nor does it set up the analysis of $a_n = H_{n - 1} - \ln n$ as a convergent sequence. The integral-sandwich proof is both more illuminating and more general.

**Elegant pivot.** Exploit the monotonicity of $1/x$. On the interval $[k, k + 1]$ with $k \ge 1$, the function $1/x$ is strictly decreasing, so for $x \in [k, k + 1]$:
\[
  \frac{1}{k + 1} \;\le\; \frac{1}{x} \;\le\; \frac{1}{k}.
\]
Integrating over $[k, k + 1]$ (an interval of length $1$):
\[
  \frac{1}{k + 1} \;<\; \int_k^{k + 1} \frac{dx}{x} \;<\; \frac{1}{k}. \qquad (\star)
\]
*(Strict inequality holds because $1/x$ is not constant on $[k, k + 1]$.)*

*Summing for the upper bound of $\ln n$.* Sum $(\star)$ over $k = 1, 2, \ldots, n - 1$. The middle sum telescopes:
\[
  \sum_{k = 1}^{n - 1} \int_k^{k + 1} \frac{dx}{x} \;=\; \int_1^n \frac{dx}{x} \;=\; \ln n.
\]
The right sum is $\sum_{k = 1}^{n - 1} 1/k = H_{n - 1}$. Hence
\[
  \ln n \;<\; H_{n - 1}.
\]
*Summing for the lower bound of $\ln n$.* The left sum is $\sum_{k = 1}^{n - 1} 1/(k + 1) = \sum_{j = 2}^{n} 1/j = H_n - 1$. Hence
\[
  H_n - 1 \;<\; \ln n.
\]
Combining: $H_n - 1 < \ln n < H_{n - 1}$ for $n \ge 2$, as required.

*Analysis of $a_n = H_{n - 1} - \ln n$.* We show $a_n$ is increasing and bounded above by $1$.

*Boundedness.* From the inequality just proved, $\ln n > H_n - 1 = H_{n - 1} + 1/n - 1$, so
\[
  a_n \;=\; H_{n - 1} - \ln n \;<\; H_{n - 1} - (H_{n - 1} + 1/n - 1) \;=\; 1 - 1/n \;<\; 1.
\]
So $a_n < 1 - 1/n < 1$ for all $n \ge 2$.

*Monotonicity.* Compute
\[
  a_{n + 1} - a_n \;=\; (H_n - \ln(n + 1)) - (H_{n - 1} - \ln n) \;=\; \frac{1}{n} - \ln\!\left(\frac{n + 1}{n}\right) \;=\; \frac{1}{n} - \ln\!\left(1 + \frac{1}{n}\right).
\]
We need this expression to be positive. Linearise $\ln(1 + u)$ at $u = 0$:
\[
  \ln(1 + u) \;=\; u - \frac{u^2}{2} + \frac{u^3}{3} - \cdots \qquad (|u| < 1).
\]
For $u = 1/n > 0$, the alternating series gives
\[
  \ln\!\left(1 + \frac{1}{n}\right) \;=\; \frac{1}{n} - \frac{1}{2 n^2} + \frac{1}{3 n^3} - \cdots \;<\; \frac{1}{n}.
\]
(More carefully: the alternating series is *bounded above by its first term* because the second term is negative and the subsequent partial sums oscillate around $\ln(1 + 1/n)$ with decreasing amplitude.) Hence $a_{n + 1} - a_n > 0$, so $\{a_n\}$ is strictly increasing.

*The Euler–Mascheroni constant.* The sequence $\{a_n\}$ is strictly increasing and bounded above (by $1$); by the monotone convergence theorem, it converges. Its limit is the *Euler–Mascheroni constant*:
\[
  \gamma \;=\; \lim_{n \to \infty} (H_{n - 1} - \ln n) \;\approx\; 0.5772156649\ldots
\]
The constant $\gamma$ is one of the most famous constants in mathematics; whether it is rational or irrational is, remarkably, still an open problem. $\blacksquare$

**Pitfalls.**
- Confusing $H_{n - 1}$ with $H_n$ in the sandwich. The asymmetry is essential: the upper bound on $\ln n$ is $H_{n - 1}$ (omitting the last term $1/n$), while the lower bound is $H_n - 1$ (omitting the first term $1$). The careful solver writes out the indexing on the telescoping sum to keep track.
- Using non-strict inequalities. Because $1/x$ is *not constant* on each unit interval, the inequalities in $(\star)$ are *strict*; the same strict inequality propagates to the sum. A solver who writes $\le$ everywhere is technically correct but loses the information that $a_n$ never equals $0$ or $1$.
- Asserting the monotonicity of $a_n$ without proof. The reverse inequality (that $a_{n + 1} > a_n$ requires $\ln(1 + 1/n) < 1/n$) is the *content* of the linearisation-of-log estimate; the solver who omits this step has not proved monotonicity.
- Conflating $\gamma$ with $\ln 2$, $1/2$, or other elementary constants. The Euler–Mascheroni constant is a transcendental-looking number with no known closed form in terms of elementary functions; it is *not* equal to any familiar constant.

**Connections.**
- The integral-sandwich technique generalises to any *monotone* function: if $f$ is positive and decreasing on $[1, \infty)$, then for $n \ge 2$,
  \[
    \sum_{k = 2}^{n} f(k) \;\le\; \int_1^n f(x)\,dx \;\le\; \sum_{k = 1}^{n - 1} f(k).
  \]
  The technique is the basis of the *integral test* for series convergence and of *Riemann-sum approximations* to integrals.
- The Euler–Mascheroni constant arises in many seemingly unrelated contexts: the digamma function $\psi(z)$ at $z = 1$ equals $-\gamma$; the Mertens product theorem gives $\prod_{p \le N} (1 - 1/p) \sim e^{-\gamma}/\ln N$; the Riemann zeta function's Laurent expansion at $s = 1$ has $\gamma$ as the constant term: $\zeta(s) = 1/(s - 1) + \gamma + O(s - 1)$.
- The linearisation $\ln(1 + u) \approx u$ for small $u$ is the *most useful single Taylor expansion in elementary mathematics*. It appears in compound-interest computations ($(1 + r/n)^n \to e^r$ as $n \to \infty$), in the proof of $e = \lim (1 + 1/n)^n$, in entropy estimates ($-\sum p_i \ln p_i$ for nearly-uniform $p_i$), and throughout asymptotic analysis. The trained solver writes "$\ln(1 + u) \approx u$" reflexively whenever $u$ is small.

**Takeaway.** *Whenever a problem juxtaposes a discrete sum (or product) with a continuous integral (or limit), the connecting tool is usually the linearisation of an underlying function on each unit interval, summed to give a global comparison. The Euler–Mascheroni constant, the integral test, the Stirling approximation $n! \approx (n/e)^n \sqrt{2\pi n}$ — all rest on this technique. Linearisation, summed, converts discrete asymptotics into continuous ones, and vice versa.*

### 4.3 Example 3 — Constant-Coefficient Linear ODE via Characteristic Polynomial

\begin{problem}
Solve the initial-value problem
\[
  y'' - 3 y' + 2 y \;=\; 0, \qquad y(0) \;=\; 1, \qquad y'(0) \;=\; 0.
\]
\end{problem}

**Source.** K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), Chapter 19 (Differential Equations), Comment 7 (constant-coefficient linear ODEs). The technique — exponential ansatz and characteristic polynomial — is the canonical reduction of a linear ODE to a polynomial equation.

**Seed.** The equation is a *second-order linear ODE with constant coefficients*. The differential operator $L = D^2 - 3D + 2$ (with $D = d/dx$) is *linear* — that is, $L(u + v) = Lu + Lv$ and $L(\alpha u) = \alpha Lu$ for scalars $\alpha$ — so the set of solutions to $Ly = 0$ is a *vector space*. The structural fact, central to the theory of linear ODEs, is that the solution space is two-dimensional (matching the order of the equation), and a basis is exhibited by the *exponential ansatz* $y = e^{\lambda x}$, which reduces the ODE to the *characteristic polynomial equation* $\lambda^2 - 3\lambda + 2 = 0$.

**Brute path.** Try a power-series solution $y = \sum_{n \ge 0} a_n x^n$, substitute into the ODE, derive a recursion for $a_n$, and solve the recursion. The approach works and is the standard route for non-constant-coefficient equations, but for constant-coefficient ODEs it is needlessly heavy: the exponential ansatz reduces the problem to a polynomial equation in one variable, and the answer is one line.

**Elegant pivot.** Apply the *exponential ansatz* $y = e^{\lambda x}$. Then $y' = \lambda e^{\lambda x}$ and $y'' = \lambda^2 e^{\lambda x}$, so the ODE becomes
\[
  (\lambda^2 - 3\lambda + 2) e^{\lambda x} \;=\; 0.
\]
Since $e^{\lambda x} \ne 0$ for any $\lambda$, the equation reduces to the *characteristic polynomial*
\[
  \lambda^2 - 3\lambda + 2 \;=\; 0 \quad\Longleftrightarrow\quad (\lambda - 1)(\lambda - 2) \;=\; 0,
\]
with roots $\lambda_1 = 1$ and $\lambda_2 = 2$. By the linearity of $L$, the general solution to the homogeneous ODE is the linear combination
\[
  y(x) \;=\; A\,e^x + B\,e^{2x},
\]
where $A, B \in \mathbb{R}$ are constants determined by initial or boundary conditions.

*Apply the initial conditions.* At $x = 0$:
\[
  y(0) \;=\; A + B \;=\; 1, \qquad y'(0) \;=\; A + 2 B \;=\; 0.
\]
Subtracting the first equation from the second: $B = -1$, and so $A = 1 - B = 2$. The particular solution is
\[
  y(x) \;=\; 2 e^x - e^{2x}.
\]

*Verification.* Compute $y' = 2 e^x - 2 e^{2x}$, $y'' = 2 e^x - 4 e^{2x}$. Then
\[
  y'' - 3 y' + 2 y \;=\; (2 e^x - 4 e^{2x}) - 3(2 e^x - 2 e^{2x}) + 2(2 e^x - e^{2x}) \;=\; (2 - 6 + 4) e^x + (-4 + 6 - 2) e^{2x} \;=\; 0. \checkmark
\]
Initial conditions: $y(0) = 2 - 1 = 1$ ✓; $y'(0) = 2 - 2 = 0$ ✓. $\blacksquare$

**Pitfalls.**
- Mishandling the case of *repeated roots* of the characteristic polynomial. If the characteristic polynomial had a double root $\lambda$, the general solution would be $y = (A + B x) e^{\lambda x}$, not $A e^{\lambda x} + B e^{\lambda x} = (A + B) e^{\lambda x}$ (which is a one-parameter family). The doubled factor $x$ is *necessary* to span the two-dimensional solution space; missing it produces a wrong "general solution" that does not capture all initial conditions.
- Mishandling the case of *complex roots*. If the characteristic polynomial had roots $\lambda = \alpha \pm i\beta$ (with $\beta \ne 0$), the general real solution would be $y = e^{\alpha x}(A \cos\beta x + B \sin\beta x)$, obtained from the complex exponential basis $e^{(\alpha \pm i\beta) x}$ by taking real and imaginary parts. The trained solver knows this transformation and applies it without hesitation.
- Forgetting that the *order* of the ODE equals the *dimension* of the solution space. A first-order linear ODE has a one-parameter family of solutions; a second-order has two; an $n$-th order has $n$. Counting the number of arbitrary constants is the first sanity check on any ODE solution.
- Confusing the *homogeneous* ODE $Ly = 0$ with the *inhomogeneous* ODE $Ly = g(x)$. The general solution of the inhomogeneous equation is the sum of *any* particular solution and the general homogeneous solution. The exponential-ansatz technique gives only the homogeneous part; the particular solution requires additional methods (undetermined coefficients, variation of parameters, integrating factors, Green's functions).

**Connections.**
- The *characteristic polynomial* of a linear ODE generalises to the *characteristic polynomial of a square matrix*: for a linear ODE $y^{(n)} + a_{n - 1} y^{(n - 1)} + \cdots + a_0 y = 0$, the characteristic polynomial $\lambda^n + a_{n - 1} \lambda^{n - 1} + \cdots + a_0$ is the same as the characteristic polynomial of the *companion matrix* of the ODE. The roots are the eigenvalues of the companion matrix; the exponential basis $\{e^{\lambda_i x}\}$ is the analogue of the eigenvector basis. This connection makes linear ODEs a special case of *linear dynamics on vector spaces*, treated in Chapter 19's locked slate via the operator framework.
- The *Laplace transform* converts a linear ODE with constant coefficients into a polynomial equation in the transform variable $s$; the polynomial equation is the *same* polynomial as the characteristic polynomial. The Laplace transform thus formalises the exponential-ansatz technique: it is the operational version of "look for solutions of the form $e^{\lambda x}$."
- The *exponential ansatz* extends to linear ODEs with non-constant coefficients via *Frobenius series* (when the coefficients have regular singular points), and to *partial differential equations* via *separation of variables*. In every case, the technique is the same: reduce a linear differential equation to a sequence of algebraic equations.
- The characteristic polynomial of $y'' - 3y' + 2y = 0$ is $(\lambda - 1)(\lambda - 2)$, with positive roots; the solutions $e^x$ and $e^{2x}$ are *exponentially growing*. The qualitative behaviour of a linear ODE — growing, decaying, oscillating — is read directly from the *signs* of the real parts of the characteristic roots: positive real parts give growth, negative give decay, non-real give oscillation. This is the foundational principle of *linear stability analysis* in dynamical systems theory.

**Takeaway.** *A linear differential operator with constant coefficients acts on an exponential $e^{\lambda x}$ by multiplication by a polynomial in $\lambda$ — the characteristic polynomial. Solving the ODE is reduced to factoring the characteristic polynomial and combining the exponential solutions linearly. This is Form-IV linearisation in its cleanest expression: the differential operator $L$ is itself the linearisation (it is linear by construction), and the spectral theory of $L$ — its eigenvalues and eigenfunctions — solves any ODE in its kernel.*

---

## 5. Practice Problems

The following seven problems exercise the linearisation archetype across its four forms. Full solutions are in the appendix at the end of the chapter; the solver is encouraged to attempt each problem before consulting the solution.

### 5.1 The Limit $\sin(\pi \cos^2 x) / x^2$ (JEE 2001; Joshi Ch. 24, Ex. 24.38)

Evaluate
\[
  \lim_{x \to 0} \frac{\sin(\pi \cos^2 x)}{x^2}.
\]

### 5.2 Differentiability of a Composite at $x = 0$ (JEE 2001; Joshi Ch. 24, Ex. 24.44)

Which of the following functions is differentiable at $x = 0$?
\[
  \text{(A)} \quad \cos|x| + |x|, \qquad \text{(B)} \quad \cos|x| - |x|, \qquad \text{(C)} \quad \sin|x| + |x|, \qquad \text{(D)} \quad \sin|x| - |x|.
\]

### 5.3 L'Hôpital via Linearisation (Joshi Ch. 15, Comment 8)

Evaluate
\[
  \lim_{x \to 0} \frac{e^x - 1 - x}{x^2}.
\]

### 5.4 Rolle's Theorem to Locate Roots of $f'$ (Joshi Ch. 16, Comment 3)

The polynomial $f(x) = x^3 - 6x^2 + 11x - 6$ has three distinct real roots. Find them, prove that $f'(x)$ has exactly two real roots, and locate the roots of $f'$ explicitly.

### 5.5 The MVT Bound $|\sin a - \sin b| \le |a - b|$ (Joshi Ch. 16, Comment 5)

Prove that for all real numbers $a$ and $b$,
\[
  |\sin a - \sin b| \;\le\; |a - b|.
\]

### 5.6 Integrating-Factor Solution of a First-Order Linear ODE (Joshi Ch. 19, Comment 3)

Solve the initial-value problem
\[
  \frac{dy}{dx} + \frac{2 y}{x} \;=\; \frac{\sin x}{x^2}, \qquad y(\pi) \;=\; 0.
\]

### 5.7 Newton's Method for $\sqrt 5$ (Joshi Ch. 16, Comment 11)

Apply Newton's method to $f(x) = x^2 - 5$, starting from $x_0 = 2$, to compute $\sqrt 5$ to four decimal places. Verify quadratic convergence by comparing the error at successive iterations.

---

## 6. The Connections Web

### 6.1 Linearisation Across Mathematical Domains

The linearisation archetype recurs across every major mathematical domain. We give one representative instance per domain.

- **Algebra.** *Taylor expansion* is linearisation extended to higher order. The first-order term is the linearisation; the second-order term captures curvature; the $n$-th order term captures the $n$-th derivative's local contribution. The Taylor series of a smooth function at a point *is* the function, in the analytic case, on the disk of convergence.
- **Geometry.** *Tangent line* (1D), *tangent plane* (2D), *tangent hyperplane* (general). The tangent space at a point on a smooth manifold *is* the local linearisation of the manifold at that point. Differential geometry is built on this foundation.
- **Calculus & Analysis.** *Differentiation* is the operation of computing the linearisation at each point. The Mean Value Theorem, the Inverse Function Theorem, the Implicit Function Theorem, Taylor's Theorem, L'Hôpital's rule, and Newton's method are all consequences of the linearisation principle.
- **Linear Algebra.** *Spectral theory* is the linearisation-by-operator framework. A linear operator on a finite-dimensional space is determined, up to similarity, by its characteristic polynomial; the eigenvalues and eigenvectors of the operator are the structural data extracted from the operator's action on each one-dimensional eigenspace.
- **Combinatorics.** Linearisation-style techniques less central, but the *generating-function* approach to recurrences amounts to viewing the recurrence as a *linear operator* on the space of sequences, and solving by finding the operator's eigenvectors (typically geometric or polynomial sequences). The Fibonacci closed form via the characteristic polynomial $\lambda^2 - \lambda - 1$ is the prototype.
- **Topology.** The *tangent bundle* of a smooth manifold collects all tangent spaces into a single object; vector fields are sections of this bundle. *Linearisation at a fixed point* of a smooth map produces a linear map between tangent spaces, the *differential* of the map at that point — the foundational object of differential topology.

The list is not exhaustive; it is meant to communicate the *ubiquity* of linearisation and to suggest that recognising linearisation in any one of these settings is *the same cognitive act* as recognising it in any other.

### 6.2 Linearisation in Physics and Other Sciences

The linearisation archetype recurs across disciplines.

- **Classical mechanics.** *Small-oscillation theory* about an equilibrium linearises the restoring force; the resulting harmonic-oscillator equations are the foundation of normal-mode analysis and the basis of all wave-propagation theory.
- **Quantum mechanics.** *First-order perturbation theory* linearises the Hamiltonian about a reference Hamiltonian whose eigenstates are known; the corrections are computed term by term in powers of the perturbation. The technique is the workhorse of atomic and molecular physics.
- **Engineering.** *Small-signal analysis* in electronics (transistor amplifiers about an operating point); *linearisation of control systems* about a setpoint; *finite-element analysis* of structures (locally linear approximation of stress-strain on each element); *Kalman filtering* (linearised state-space models for state estimation in noisy systems).
- **Economics.** *Marginal analysis* (marginal cost, marginal revenue, marginal utility); *first-order optimality conditions* in constrained optimisation (Lagrangians, KKT); *linear approximation* of demand and supply curves about an equilibrium price.
- **Statistics.** *Delta method* (linearisation of a smooth function of an estimator); *linear regression* (best linear approximation of a response by predictors); *Gauss–Markov theorem* (optimality of linear estimators under suitable assumptions).

In each case, linearisation is the bridge that converts an intractable nonlinear problem into a tractable linear one, *locally*. The mature practitioner accepts the local restriction and extracts what is valid; the novice sometimes attempts to extend the linearisation globally and gets the wrong answer.

### 6.3 Cross-Domain Manifestations

Beyond formal disciplines, linearisation recurs across cognitive domains.

- **Cartography.** *Local maps* of small regions of the Earth treat the Earth as flat. Larger regions require explicit handling of curvature (cylindrical, conic, or stereographic projections), but for small enough scales the flat-Earth approximation is operationally exact.
- **Navigation.** *Dead reckoning* — extrapolating from current position and velocity — is a linearisation of trajectory in time. For short intervals, the linear extrapolation is dead-accurate; for longer intervals, corrections (wind, ocean currents, rotational drag) become essential.
- **Marginal economics in everyday life.** The decision to *spend one more hour studying* rests on an implicit comparison of *marginal cost* (the hour foregone) with *marginal benefit* (the expected improvement on the next quiz). The marginal-quantity language is everyday-language linearisation.
- **Sports.** A batsman's *form* on a given day is a linearisation of his average over a small window — the recent few innings — and is used to predict the next innings.

The cross-domain recurrence is, again, the signature of a foundational cognitive archetype.

### 6.4 Related Archetypes

Linearisation interacts richly with several other archetypes in the Pillar 2 taxonomy.

- **Archetype 5: Substitution.** *Linearisation is the canonical local substitution* — replacement of $f$ by its tangent at a point. The two archetypes are siblings: Substitution chooses any clever variable, Linearisation commits to the specific variable of *deviation from a fixed point* with the specific approximation of *tangent line*.
- **Archetype 11: Existence / Uniqueness.** Many existence theorems in calculus — the Mean Value Theorem, Rolle's Theorem, the Inverse Function Theorem, the Implicit Function Theorem — assert the *existence* of a point at which the linearisation satisfies some condition. The local-linearity content of differentiability is the structural input to these theorems.
- **Archetype 17: DOF Analysis.** *Counting degrees of freedom* at a regular point of a constraint surface uses the linearisation (the tangent plane) of the constraint to determine the number of *independent* directions. The Implicit Function Theorem makes the connection rigorous: the Jacobian's rank at a regular point determines the local dimension.
- **Archetype 18: Recursion / Induction.** *Newton's method* is iterated linearisation: at each step, linearise the function at the current iterate and take the linear root as the next iterate. The *quadratic convergence* of Newton's method is the algorithmic payoff of linearisation, and it generalises to *higher-order convergence* via Halley's method (using a quadratic Taylor term) and beyond.
- **Archetype 20: Analogy / Transfer.** The *linear analogue* of a nonlinear problem is often more tractable and serves as a *first guess* at the nonlinear answer. The progression "linear theory → nonlinear corrections → full theory" is the standard structure of every applied-mathematical investigation, from celestial mechanics to fluid dynamics to general relativity.

The five related archetypes — Substitution, Existence/Uniqueness, DOF Analysis, Recursion/Induction, and Analogy — together with Linearisation itself form the operational vocabulary of *method selection past structural recognition*: the chapters in which the transformation of a problem into a more tractable form is the central skill.

---

## 7. Master Takeaways

We collect the seven master takeaways of this chapter, in the language of working strategy.

1. **Replace the curve by its tangent; in a small enough neighbourhood, the tangent is the curve.** No further glossing: this *is* the chapter, in one sentence.

2. **Calculus is the systematic study of linearisation.** Differentiation computes the linearisation; integration sums local linearisations to recover global quantities; Taylor's theorem extends linearisation to higher-order approximations with bounded errors. The single move — *linearise, work in the linear setting, bound the error* — generates the entire calculus.

3. **Differentiability is linearisability.** The derivative $f'(a)$ is *defined* as the unique slope such that $f(x) - L_a(x) = o(x - a)$. Conceptually, this is more fundamental than the textbook definition of $f'(a)$ as a limit of difference quotients; the limit-of-quotients formulation is a consequence.

4. **The right point of linearisation is the one near which the answer is sought.** For limits, it is the limit point. For tangent geometry, it is the point of tangency. For Newton's method, it is the current iterate. For stability analysis, it is the equilibrium. Choosing the wrong point produces a correct but inaccurate linearisation; choosing the right point produces a linearisation that is exact in its first-order content.

5. **The error is $O((x - a)^2)$.** The linearisation captures *first-order* information exactly and *misses* second-order information by a quadratic-in-deviation amount. For problems where only first-order information matters, the error is irrelevant; for precision-sensitive numerical problems, the error must be bounded explicitly via Taylor's remainder.

6. **Iterated linearisation is exponentially more powerful than a single linearisation.** Newton's method achieves *quadratic convergence* — the number of correct digits roughly doubles per iteration — by re-linearising at each step. Perturbation theory in physics, the Euler method in numerical ODEs, and the multigrid method in finite-element analysis are all iterated-linearisation techniques.

7. **Linearisation fails where differentiability fails.** At corners, cusps, discontinuities, and singularities, the linearisation is undefined and the technique does not apply. The disciplined solver checks differentiability before linearising, and where one-sided derivatives are the best one can do, uses separate one-sided linearisations.

---

## 8. Self-Assessment Checklist

The following ten checkpoints test whether the chapter's content has become *unhesitating knowledge*. Each should evoke an immediate, confident yes. If any is hesitant, return to the relevant section before moving on.

- [ ] I can write down the linearisation $L_a(x) = f(a) + f'(a)(x - a)$ from memory, and I know it is the unique affine function agreeing with $f$ in value and slope at $a$.
- [ ] I can recite the linearisations of $\sin x$, $\cos x$, $e^x$, $\ln(1 + x)$, $(1 + x)^\alpha$ at $x = 0$ from memory, including the first two non-zero terms.
- [ ] I can recognise a tangent-line geometry problem at sight and solve it by linearisation without resorting to coordinate-geometry calisthenics.
- [ ] I can state the Mean Value Theorem with its hypotheses (continuity on $[a, b]$, differentiability on $(a, b)$) and apply it to bound differences such as $|\sin a - \sin b| \le |a - b|$.
- [ ] I can state Rolle's Theorem and use it to prove that between any two roots of a differentiable function, there is at least one root of its derivative.
- [ ] I can solve any constant-coefficient linear ODE $a_n y^{(n)} + \cdots + a_0 y = 0$ by writing the characteristic polynomial, factoring it, and combining the exponential solutions linearly.
- [ ] I can apply Newton's method to a smooth function and explain why the convergence is quadratic when the iterate is near a simple root.
- [ ] I can apply L'Hôpital's rule with the *verification* that the form is indeterminate, and I can solve the same limit by direct Taylor expansion as a cross-check.
- [ ] I can name at least three contexts outside this chapter (e.g., small-oscillation analysis, marginal cost, delta method) in which linearisation is the central technique.
- [ ] I can explain to a beginner why the error in linearisation is $O((x - a)^2)$, citing Taylor's theorem with remainder, and I can estimate when the linearisation is and is not accurate enough for a given precision target.

---

## Bridge to Chapter 7: Normalisation / Scaling

Linearisation has answered: *near a given point, what affine function best approximates this nonlinear function?* The next archetype — *Normalisation* — answers a *global* counterpart of this question: *across the whole problem, what change of scale makes the essential features stand out at unit size, with no extraneous parameters?*

Where Linearisation is *local* (it works in a neighbourhood of a chosen point), Normalisation is *global* (it rescales the entire problem). Where Linearisation replaces a curve by its tangent, Normalisation rescales the axes so that the problem's natural scales appear as $1$. Where Linearisation commits to one specific substitution (deviation from a fixed point) with one specific approximation (tangent), Normalisation invites a *family* of rescalings, each chosen to expose different structural features of the problem. The two archetypes share a common purpose — *simplification by adapted coordinates* — but differ in scope: one is the microscope, the other is the change of magnification.

The reader will recognise that the linearisation $\sqrt{1 + x} \approx 1 + x/2$ already contained a normalisation in disguise: by writing $\sqrt{1 + x}$ instead of, say, $\sqrt{a + b x}$, we have *normalised* the leading constant to $1$ and the coefficient of $x$ to $1$. The normalisation makes the linearisation's content universal: it is a statement about any first-order radical, not about a particular numerical instance. Chapter 7 will formalise this kind of move and treat the systematic technique of *dimensional analysis and Buckingham-π normalisation* in physics, the *constraint normalisation* technique in inequality proofs (where homogeneity allows free rescaling), and the *non-dimensionalization* of differential equations to expose universal scaling laws.

Linearisation (Chapter 6) and Normalisation (Chapter 7) together complete the second half of the *Method Selection* sub-pillar of Pillar 2 (Chapters 5–8): the chapters in which the transformation of a problem into a more tractable form is the central skill. After Chapter 8 (Domain Translation, the closing chapter of this sub-pillar), we will turn in Chapter 9 to the *Constraint Exploitation* sub-pillar, where the focus shifts from transforming the problem to *using* the structure of the constraints directly.

---

## Appendix — Solutions to Practice Problems

### Solution to 5.1 — The Limit $\sin(\pi \cos^2 x) / x^2$

Expand $\cos^2 x$ using the linearisation of $\cos$ at $0$:
\[
  \cos x \;=\; 1 - \frac{x^2}{2} + O(x^4), \qquad \cos^2 x \;=\; 1 - x^2 + O(x^4).
\]
Multiply by $\pi$:
\[
  \pi \cos^2 x \;=\; \pi - \pi x^2 + O(x^4).
\]
Now use the identity $\sin(\pi - u) = \sin u$ (a property of $\sin$ on the real line):
\[
  \sin(\pi \cos^2 x) \;=\; \sin(\pi - \pi x^2 + O(x^4)) \;=\; \sin(\pi x^2 - O(x^4)).
\]
Linearise $\sin$ at $0$: $\sin u = u + O(u^3)$ as $u \to 0$. With $u = \pi x^2 - O(x^4) = O(x^2)$, we have $u^3 = O(x^6)$, so
\[
  \sin(\pi \cos^2 x) \;=\; \pi x^2 + O(x^4).
\]
Dividing by $x^2$:
\[
  \frac{\sin(\pi \cos^2 x)}{x^2} \;=\; \pi + O(x^2) \;\longrightarrow\; \pi \quad \text{as } x \to 0.
\]
The limit is $\boxed{\pi}$. $\blacksquare$

**Key lesson.** The problem is a *Form-I linearisation* of a composite function. The trick is to recognise that $\pi \cos^2 x = \pi - \pi x^2 + O(x^4)$ — that the leading deviation from $\pi$ is $-\pi x^2$ — and then to use $\sin(\pi - u) = \sin u$ to convert the deviation into the argument of $\sin$. Two linearisations chained together. The leading non-vanishing term in the numerator is $\pi x^2$, which exactly cancels the $x^2$ in the denominator, leaving $\pi$.

### Solution to 5.2 — Differentiability of a Composite at $x = 0$

We linearise each function at $x = 0$ and check whether the resulting expansion contains a $|x|$ term (which would make the function non-differentiable, since $|x|$ has different one-sided derivatives at $0$).

- $\cos|x| + |x|$: $\cos|x| = 1 - x^2/2 + O(x^4)$ (even function of $|x|$, hence even in $x$); $\cos|x| + |x| = 1 + |x| - x^2/2 + O(x^4)$. The $|x|$ term has different one-sided derivatives at $0$ (slope $+1$ from the right, $-1$ from the left), so this function is not differentiable at $0$.

- $\cos|x| - |x|$: $\cos|x| - |x| = 1 - |x| - x^2/2 + O(x^4)$. Same issue: the $|x|$ term has different one-sided derivatives. Not differentiable.

- $\sin|x| + |x|$: $\sin|x| = |x| - |x|^3/6 + O(|x|^5)$ (Taylor of $\sin$ applied to the argument $|x|$); $\sin|x| + |x| = 2|x| - |x|^3/6 + O(|x|^5)$. The $2|x|$ term has different one-sided derivatives. Not differentiable.

- $\sin|x| - |x|$: $\sin|x| - |x| = -|x|^3/6 + O(|x|^5)$. The $|x|^3/6$ term is *cubic in $|x|$* and hence equals $|x| \cdot x^2 / 6$, which can be written more carefully as $\mathrm{sgn}(x) \cdot x^3/6$ for $x \ne 0$. The derivative at $0$ from the right is $\lim_{h \to 0^+} (-h^3/6)/h = -h^2/6 \to 0$; from the left, $\lim_{h \to 0^-} (-(-h)^3/6)/h = (h^3/6)/h = h^2/6 \to 0$. Both one-sided derivatives equal $0$, so the function *is* differentiable at $0$ with derivative $0$.

The answer is $\boxed{\text{(D)}}$. $\blacksquare$

**Key lesson.** Differentiability at a point is *the existence of a linearisation* — a single linear function that matches both one-sided values. The function $|x|$ has a corner: its one-sided derivatives at $0$ are $+1$ and $-1$, so no single line linearises it. The function $|x|^3$, by contrast, has matching one-sided derivatives both equal to $0$, and is differentiable at $0$ despite the absolute value. The trick is to recognise that $|x|^k$ for *odd* $k \ge 3$ is differentiable at $0$ (because $|x|^k = x \cdot |x|^{k - 1}$ has zero derivative from both sides), while $|x|^k$ for $k = 1$ is not.

### Solution to 5.3 — L'Hôpital via Linearisation

Expand $e^x$ at $0$ to second order:
\[
  e^x \;=\; 1 + x + \frac{x^2}{2} + O(x^3).
\]
Substitute:
\[
  e^x - 1 - x \;=\; \frac{x^2}{2} + O(x^3).
\]
Dividing by $x^2$:
\[
  \frac{e^x - 1 - x}{x^2} \;=\; \frac{1}{2} + O(x) \;\longrightarrow\; \frac{1}{2} \quad \text{as } x \to 0.
\]
The limit is $\boxed{1/2}$. $\blacksquare$

*Alternative via L'Hôpital.* The limit is $0/0$. Applying L'Hôpital once: $\lim_{x \to 0} (e^x - 1)/(2x)$. Still $0/0$. Apply L'Hôpital again: $\lim_{x \to 0} e^x / 2 = 1/2$. ✓ Two applications of L'Hôpital extract two derivative orders, which is exactly the order of the leading non-vanishing term in the Taylor expansion.

**Key lesson.** *L'Hôpital is repeated linearisation*. Each application of L'Hôpital differentiates numerator and denominator, equivalent to advancing one order in the Taylor expansion. The number of L'Hôpital applications needed equals the order of the leading non-vanishing terms in the Taylor expansions of numerator and denominator. The trained solver, having internalised the Taylor expansion approach, often skips L'Hôpital entirely and reads off the answer from the Taylor expansions; this is faster and cleaner.

### Solution to 5.4 — Rolle's Theorem to Locate Roots of $f'$

*Factor $f$.* Try $x = 1$: $f(1) = 1 - 6 + 11 - 6 = 0$. ✓ So $(x - 1)$ is a factor. Divide:
\[
  f(x) \;=\; x^3 - 6x^2 + 11x - 6 \;=\; (x - 1)(x^2 - 5x + 6) \;=\; (x - 1)(x - 2)(x - 3).
\]
The three roots are $\boxed{x = 1, 2, 3}$.

*Apply Rolle's theorem to locate roots of $f'$.* Since $f$ has three distinct real roots $r_1 = 1 < r_2 = 2 < r_3 = 3$, and $f$ is differentiable everywhere, Rolle's theorem applies to the intervals $[r_1, r_2] = [1, 2]$ and $[r_2, r_3] = [2, 3]$:
- In $(1, 2)$, there exists a point $c_1$ with $f'(c_1) = 0$ — a root of $f'$.
- In $(2, 3)$, there exists a point $c_2$ with $f'(c_2) = 0$ — another root of $f'$.

So $f'$ has at least two real roots. Since $f' = 3x^2 - 12x + 11$ is a quadratic, it has at most two real roots. Hence $f'$ has *exactly* two real roots.

*Locate the roots of $f'$ explicitly.* Apply the quadratic formula to $f'(x) = 3x^2 - 12x + 11 = 0$:
\[
  x \;=\; \frac{12 \pm \sqrt{144 - 132}}{6} \;=\; \frac{12 \pm \sqrt{12}}{6} \;=\; \frac{12 \pm 2\sqrt 3}{6} \;=\; 2 \pm \frac{1}{\sqrt 3}.
\]
Numerically: $2 - 1/\sqrt 3 \approx 1.42$ and $2 + 1/\sqrt 3 \approx 2.58$. As predicted by Rolle, one root lies in $(1, 2)$ and the other in $(2, 3)$. $\blacksquare$

**Key lesson.** *Rolle's theorem is the existence-of-zeros theorem for the derivative*. Between any two zeros of a differentiable function, there is at least one zero of the derivative. The theorem provides only existence (not location); explicit location requires solving the derivative equation. In our problem, Rolle gives the *count* (at least two roots of $f'$) and the *intervals* (one in $(1, 2)$, one in $(2, 3)$); the quadratic formula gives the *values* $2 \pm 1/\sqrt 3$. The combination of qualitative existence (Rolle) with quantitative computation (quadratic formula) is the standard pattern of olympiad-level calculus.

### Solution to 5.5 — The MVT Bound $|\sin a - \sin b| \le |a - b|$

Without loss of generality, assume $a \ne b$; otherwise the inequality is $0 \le 0$, trivially true. The function $\sin : \mathbb{R} \to \mathbb{R}$ is continuous on $[a, b]$ (taking the convention $a < b$ if necessary) and differentiable on $(a, b)$, with derivative $\cos$. By the Mean Value Theorem, there exists $c \in (a, b)$ such that
\[
  \sin a - \sin b \;=\; \cos(c) \cdot (a - b).
\]
Taking absolute values:
\[
  |\sin a - \sin b| \;=\; |\cos c| \cdot |a - b|.
\]
The universal bound $|\cos c| \le 1$ (valid for any real $c$) gives
\[
  |\sin a - \sin b| \;\le\; |a - b|.
\]
The inequality holds for all real $a, b$. $\blacksquare$

**Key lesson.** *The MVT is exact linearisation* — it asserts the *existence* of a slope $\cos c$ such that the chord from $(a, \sin a)$ to $(b, \sin b)$ has *exactly* that slope. The slope is bounded by $1$ in absolute value because $|\cos| \le 1$ is a *uniform* bound — independent of $c$. The combination "MVT exists + uniform bound on derivative" gives a *uniform Lipschitz constant* for $\sin$, namely $1$. The same technique proves $|f(a) - f(b)| \le M |a - b|$ for any function $f$ with $|f'| \le M$ on the relevant interval — the *Lipschitz inequality*, foundational throughout analysis.

### Solution to 5.6 — Integrating-Factor Solution of a First-Order Linear ODE

The ODE is $y' + (2/x) y = \sin x / x^2$. This is a *first-order linear* ODE; the standard technique is the *integrating factor*. The integrating factor for an ODE of the form $y' + P(x) y = Q(x)$ is
\[
  \mu(x) \;=\; \exp\!\left(\int P(x)\,dx\right).
\]
Here $P(x) = 2/x$, so
\[
  \int P(x)\,dx \;=\; 2 \ln|x| \;=\; \ln(x^2) \qquad (\text{taking } x > 0),
\]
and $\mu(x) = e^{\ln x^2} = x^2$.

Multiply the ODE by $\mu = x^2$:
\[
  x^2 y' + 2 x y \;=\; \sin x.
\]
The LHS is exactly $(d/dx)(x^2 y)$:
\[
  \frac{d}{dx}(x^2 y) \;=\; \sin x.
\]
Integrate both sides:
\[
  x^2 y \;=\; -\cos x + C.
\]
Apply the initial condition $y(\pi) = 0$:
\[
  \pi^2 \cdot 0 \;=\; -\cos\pi + C \;=\; 1 + C \quad\Longrightarrow\quad C \;=\; -1.
\]
Therefore
\[
  x^2 y \;=\; -\cos x - 1 \;=\; -(1 + \cos x) \quad\Longrightarrow\quad y \;=\; -\frac{1 + \cos x}{x^2}.
\]
$\blacksquare$

**Key lesson.** *The integrating factor is a multiplicative linearisation*: it converts the LHS $y' + P(x) y$ — which is a nonlinear expression in the unknown $y$ and the operator $d/dx$ — into a *perfect derivative* $(d/dx)(\mu y)$. The mechanism is that the integrating factor $\mu = e^{\int P\,dx}$ satisfies $\mu' = P \mu$, so $(\mu y)' = \mu' y + \mu y' = \mu(P y + y') = \mu(P y + y')$, which equals $\mu Q$ after the ODE is invoked. The "linearisation" sense here is that the LHS becomes a single-term *linear-in-$y$* expression $(d/dx)(x^2 y)$, with no $y'$-term separate from $y$.

### Solution to 5.7 — Newton's Method for $\sqrt 5$

The square root $\sqrt 5$ is the positive root of $f(x) = x^2 - 5$. Newton's iteration is
\[
  x_{n + 1} \;=\; x_n - \frac{f(x_n)}{f'(x_n)} \;=\; x_n - \frac{x_n^2 - 5}{2 x_n} \;=\; \frac{x_n^2 + 5}{2 x_n} \;=\; \frac{1}{2}\!\left(x_n + \frac{5}{x_n}\right).
\]
Starting from $x_0 = 2$:
\[
\begin{aligned}
x_0 &\;=\; 2, \\
x_1 &\;=\; \tfrac{1}{2}(2 + 5/2) \;=\; \tfrac{1}{2}(2 + 2.5) \;=\; 2.25, \\
x_2 &\;=\; \tfrac{1}{2}(2.25 + 5/2.25) \;=\; \tfrac{1}{2}(2.25 + 2.22222\ldots) \;=\; 2.23611\ldots, \\
x_3 &\;=\; \tfrac{1}{2}(x_2 + 5/x_2) \;=\; 2.236067977\ldots.
\end{aligned}
\]
Compare with the true value $\sqrt 5 = 2.236067977499\ldots$:

| Iterate | Value | Error $|x_n - \sqrt 5|$ |
|---|---|---|
| $x_0$ | $2.000000$ | $2.4 \times 10^{-1}$ |
| $x_1$ | $2.250000$ | $1.4 \times 10^{-2}$ |
| $x_2$ | $2.236111$ | $4.3 \times 10^{-5}$ |
| $x_3$ | $2.2360680$ | $4 \times 10^{-10}$ |

To *four decimal places*, $\sqrt 5 = \boxed{2.2361}$ (rounding $x_3$'s value).

*Quadratic convergence.* Observe the errors at successive iterations:
\[
  e_0 \approx 0.24, \qquad e_1 \approx 0.014, \qquad e_2 \approx 4.3 \times 10^{-5}, \qquad e_3 \approx 4 \times 10^{-10}.
\]
Each error is approximately the square of the previous (within a constant factor): $e_1 \approx e_0^2 / 4$, $e_2 \approx e_1^2 / 4$, $e_3 \approx e_2^2 / 4$. This is *quadratic convergence* — the number of correct digits roughly doubles per iteration. After three iterations from the modest starting point $x_0 = 2$, we have $\sqrt 5$ to nine correct decimal places. $\blacksquare$

**Key lesson.** *Newton's method is iterated Form-I linearisation*. At each step, the function $f$ is replaced by its tangent line at the current iterate; the root of the tangent line is taken as the next iterate; repeat. The quadratic convergence is the algorithmic payoff: $|x_{n + 1} - r| \le C \cdot |x_n - r|^2$ for some constant $C$ depending on $f$ near the simple root $r$. The constant $C \approx |f''(r)| / (2|f'(r)|)$ controls the rate; for our problem, $C = 2/(2 \cdot 2 \sqrt 5) = 1/(2\sqrt 5) \approx 0.224$, consistent with the observed contraction. Iterated linearisation is *exponentially* more powerful than a single linearisation: with each iteration, the error squares, so the number of correct digits doubles. This is why Newton's method has been the workhorse of numerical root-finding for three centuries.

This closes the chapter's practice slate and the chapter itself.

> *Linearisation, at its deepest, is the recognition that calculus is one move repeated and that the move can be iterated to exponential effect. Differentiation finds the linearisation; integration sums local linearisations to global statements; Newton iterates the linearisation to compute roots. Three centuries of mathematical physics rest on this one act.*

---

🌑

*End of Chapter 6 — Linearisation. Next: Chapter 7 — Normalisation / Scaling.*
