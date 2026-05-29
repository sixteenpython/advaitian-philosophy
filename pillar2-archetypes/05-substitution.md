---
chapter: 5
archetype: Substitution / Change of Variables
subtitle: "The Right Coordinate System Makes the Problem Transparent"
category: Method Selection (Archetypes 5–8)
related_archetypes: [4, 6, 10, 14, 19, 20]
key_gems: [A17, D07c, F04a, F09, F10]
  - "Weierstrass tangent half-angle substitution $t = \\tan(x/2)$"
  - "Ravi substitution for triangle sides $a = y + z,\\ b = z + x,\\ c = x + y$"
  - "Bernoulli substitution $v = y^{1-n}$ linearises $y' + P(x)y = Q(x)y^n$"
  - "Algebraic substitution $y = x + 1/x$ for symmetric Laurent expressions"
  - "Trigonometric substitution $x = \\sin\\theta$ for $\\sqrt{1 - x^2}$ integrands"
  - "Logarithmic substitution $u = \\ln x$ converts multiplicative to additive structure"
  - "Parametric substitution of the unit circle $(\\tfrac{1 - t^2}{1 + t^2}, \\tfrac{2t}{1 + t^2})$"
  - "Change-of-variable theorem for definite integrals"
  - "Tschirnhaus shift $x \\mapsto x - a_{n-1}/(n a_n)$ to depress a polynomial"
  - "Polar–Cartesian transformation $(x, y) \\leftrightarrow (r, \\theta)$"
canonical_takeaway: "The right change of variables turns a hard problem into a routine one; the work is choosing the variable."
status: locked
last_revised: 2026-05-29
locked_on: 2026-05-29
sourcing_note: "All worked examples and practice problems in this chapter are drawn from K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), or from JEE / RMO / INMO examinations commented on in that text. See Blueprint §6.2 for the sourcing rule and `pillar2-archetypes/_template/joshi-problems-locked.md` §Ch. 5 for the locked slate."
---

# Chapter 5 — Substitution / Change of Variables

## *The Right Coordinate System Makes the Problem Transparent*

---

## Opening Vignette

A draughtsman is asked to draw the curve traced by a small bead at the end of a rigid rod that pivots about its other end while the rod uniformly lengthens. The motion is the simplest imaginable: turn the rod through equal angles in equal times, and let the rod's length grow at a steady rate. The bead traces a spiral. The draughtsman, working on a sheet of squared graph paper, sets up Cartesian axes and tries to write the curve as $y = f(x)$. The result is a tangled transcendental — multi-valued, oscillatory, defying any closed expression in elementary functions of $x$. He plots a few points by hand, sighs, and starts to wonder whether he has been handed an unsolvable problem.

A colleague, idly watching, hands him a sheet of polar-coordinate paper — concentric circles for the radial coordinate $r$, radial lines for the angular coordinate $\theta$. *Try this*, she says. The draughtsman re-reads the problem statement: equal angles in equal time, length growing steadily. In the new coordinates the curve is the equation $r = a\theta$, a single line on the polar grid — a child could plot it. The bead's motion has not changed. The grid has changed. And the description has collapsed from intractable to trivial.

Now consider an entirely different scene. An acoustics engineer is handed an oscilloscope trace of a musical chord — three notes sounded together by a string trio — recorded as a function of time. The trace is a chaotic squiggle, a continuous wiggle with no obvious structure, no period that the eye can pick out. The engineer is asked: *which three notes are these?* The squiggle gives up nothing.

She runs the signal through a Fourier transform. In the new representation — amplitude as a function of frequency, rather than amplitude as a function of time — the signal collapses to three crisp spikes at $440$, $554$, and $659$ Hertz: the A major triad. The information content is identical to the time-domain trace; the trio plays the same notes, the spikes encode the same pressure waves. But in the frequency-domain coordinates, the question *which three notes are these?* is answered by reading off three locations on a horizontal axis. In the time-domain coordinates, the same question is intractable.

These two scenes look unrelated. A draughtsman's spiral, an engineer's chord. They share a single deep architecture. In each, *one object lives in two coordinate systems*, and the *same operation* — naming the curve, naming the notes — is intractable in one system and trivial in the other. The cognitive act that closes the gap is small and decisive: *choose the right coordinates, and the problem dissolves.* The object on the page has not changed; the description has.

This is *Substitution / Change of Variables*. It is the first archetype of the *Method Selection* sub-pillar, and where the previous four chapters taught the eye to *recognise* the structure latent in a problem, this chapter teaches the hand to *execute* the move into the coordinates in which that structure is computable. Substitution and Hidden Structure are inseparable: Hidden Structure names the category the problem belongs to; Substitution carries the problem there. The two archetypes are routinely deployed in the same breath.

> *The right change of variables turns a hard problem into a routine one. The work is choosing the variable.*

---

## 1. The Archetype Defined

### 1.1 Formal Definition

We make the intuition precise.

\begin{definition}[Substitution / Change of Variables]
Let $P$ be a problem posed over a parameter space $V$ — that is, a question about an object (an integral, an equation, a configuration) expressed in the coordinates of $V$. A *substitution* is a map
\[
  \phi : W \to V
\]
from a second parameter space $W$ to $V$, together with the induced rule for transporting the problem $P$ on $V$ into an equivalent problem $\widetilde{P}$ on $W$, such that:
\begin{enumerate}
\item $\phi$ is bijective on the domain of interest (or, more generally, a local diffeomorphism whose Jacobian does not vanish where needed).
\item The transport rule respects the structure of $P$: for an integral, $dx = \phi'(t)\,dt$; for an equation, the unknown $x$ is replaced by $\phi(t)$ everywhere; for a constraint, the constraint on $V$ pulls back to a constraint on $W$ via $\phi^{-1}$.
\item Solving $\widetilde{P}$ in $W$ is *strictly easier* than solving $P$ in $V$ — either because the new parameter exposes a simplifying structure (symmetry, separation of variables, rationality) or because a standard theorem becomes directly applicable.
\item The answer to $\widetilde{P}$ in $W$ can be transported back to an answer for $P$ in $V$ via $\phi^{-1}$ without information loss.
\end{enumerate}
\end{definition}

Three points are worth unpacking. First, *substitution is always a two-step process*. The first step is the forward map $\phi : W \to V$; the second is the transport back via $\phi^{-1}$. A solver who executes only the first step has solved a *different* problem — the transported one — without translating the answer into the original setting. The transport back is small but indispensable.

Second, the gain from a substitution is *not* that the answer changes (it does not — the underlying object is unchanged) but that the *computation* becomes shorter, more transparent, or accessible to a standard theorem. The Weierstrass substitution does not change the value of $\int \frac{dx}{1 + \sin x + \cos x}$; it changes the integrand from a transcendental function of $x$ into a rational function of $t = \tan(x/2)$, putting the integral within the reach of partial fractions. The Ravi substitution does not change the truth of the Hadwiger–Finsler inequality; it converts the constrained problem (sides of a triangle) into an unconstrained one (positive reals), allowing the standard inequality machinery to apply.

Third, *the right substitution is far from arbitrary*. For any given problem, there is usually a *canonical* substitution dictated by the structure of the problem. A definite integral of a rational function of $\sin x$ and $\cos x$ calls for $t = \tan(x/2)$. A constrained inequality in the sides of a triangle calls for Ravi. A nonlinear first-order ODE of Bernoulli type calls for $v = y^{1-n}$. A symmetric Laurent expression in $x$ and $1/x$ calls for $y = x + 1/x$. A polynomial of degree $n$ in $x$ that one wishes to depress calls for the Tschirnhaus shift $x \mapsto x - a_{n-1}/(n a_n)$. The *recognition* of which canonical substitution fits is the central skill the chapter teaches.

In what follows we will encounter four characteristic forms of substitution. As with previous archetypes, the taxonomy is not disjoint — a Ravi substitution is at once geometric and algebraic, a Weierstrass substitution is at once trigonometric and integral — but the four forms give a working diagnostic. On first contact with a problem amenable to substitution, ask which kind is in play.

- **Form I — Algebraic substitution.** A new variable is defined as an algebraic expression in the old variable(s), chosen to expose a symmetric or rational structure. *Examples.* $y = x + 1/x$ to collapse a Laurent polynomial of degree $\le 2$ in $x$ into a polynomial of half the degree in $y$; $u = x^2$ to convert a function of $x^2$ alone into a function of one variable; the Tschirnhaus shift $x \mapsto x - a_{n-1}/(n a_n)$ to depress a polynomial (eliminate the second-highest term); the Vieta substitution in a cubic. Algebraic substitutions are most common in equations, functional equations, and problems where a symmetric or homogeneous structure is implicit.

- **Form II — Trigonometric substitution.** A new variable is defined as a trigonometric or inverse-trigonometric expression in the old, chosen to convert an algebraic structure with implicit angular content into an explicit angular structure (or vice versa). *Examples.* $x = \sin\theta$ to convert $\sqrt{1 - x^2}$ into $\cos\theta$; $x = \tan\theta$ to convert $1 + x^2$ into $\sec^2\theta$; $x = \sinh u$ to convert $\sqrt{x^2 + 1}$ into $\cosh u$; the Weierstrass tangent half-angle $t = \tan(x/2)$ to convert any rational function of $\sin x, \cos x$ into a rational function of $t$. Trigonometric substitutions dominate integration of algebraic functions with quadratic-radical structure and rational functions of trigonometric arguments.

- **Form III — Geometric substitution.** A new variable is defined as a *geometric* recoordinatization of a configuration — a new origin, a new frame, a new parametrization. *Examples.* The Ravi substitution $a = y + z, b = z + x, c = x + y$ converts a triangle (with the awkward triangle-inequality constraint $a < b + c$, etc.) into a triple of positive reals (with no constraint); the polar substitution $(x, y) \leftrightarrow (r, \theta)$ converts rotational structure into translation in $\theta$; the parametric substitution of the unit circle $(x, y) = ((1 - t^2)/(1 + t^2), 2t/(1 + t^2))$ converts an implicit circle equation into an explicit rational parameter. Geometric substitutions are the workhorse of olympiad geometry and of problems with an implicit symmetry group.

- **Form IV — Integral / differential substitution.** A new variable is defined inside an integral or differential equation, chosen to convert the integrand or the ODE into a recognisable standard form. *Examples.* Ordinary $u$-substitution $u = g(x)$ in a definite integral (so that the integrand becomes $f(u)\,du$); Bernoulli substitution $v = y^{1 - n}$ to linearise the nonlinear ODE $y' + P(x) y = Q(x) y^n$; the substitution $u = \ln y$ to convert a homogeneous ODE into a separable one; logarithmic substitution $u = \ln x$ in a functional equation $f(xy) = f(x) + f(y)$ to reduce it to the Cauchy additive equation. Integral and differential substitutions are the central technique of calculus past the freshman level.

### 1.2 The Core Principle

The principle of substitution, in one sentence, is the chapter's title.

> *Choose the variable in which the problem is easy.*

This sentence inverts a deeply ingrained reading habit. When a beginner encounters a problem, the instinct is to *accept the variables in which the problem is stated* and start computing within them. Computing in the given variables is sometimes the right move — when the variables are already adapted to the problem's structure — but it is just as often the wrong one. A problem stated in Cartesian coordinates may be far easier in polar; a problem stated in $x$ may be far easier in $t = \tan(x/2)$; a constrained problem in $a, b, c$ may be unconstrained in the Ravi parametrization. The trained solver does not regard the variables in the problem statement as a fixed setting; they regard them as the *first* setting, to be replaced if a better one is available.

To see the move in miniature, consider the integral
\[
  I = \int_0^1 \frac{dx}{1 + x^2}.
\]
The surface-reading student notes that $1 / (1 + x^2)$ is the derivative of $\arctan x$, applies the fundamental theorem, and writes $I = \arctan 1 - \arctan 0 = \pi/4$. This is correct and adequate. But it works because the substitution $\theta = \arctan x$ has been internalised — the student already *knows* the antiderivative of $1/(1 + x^2)$.

The substitution-aware student executes the same move *explicitly*. They set $x = \tan\theta$, so $dx = \sec^2\theta\,d\theta$ and $1 + x^2 = \sec^2\theta$. The integrand becomes $\sec^2\theta\,d\theta / \sec^2\theta = d\theta$. The limits transform: $x = 0 \Rightarrow \theta = 0$; $x = 1 \Rightarrow \theta = \pi/4$. The integral collapses to $\int_0^{\pi/4} d\theta = \pi/4$. The substitution has *manifested* the underlying simplicity: the integrand $1 / (1 + x^2)$ in $x$-coordinates is the disguised version of the trivial integrand $1$ in $\theta$-coordinates. The "hard" integral was hard only because it was stated in the wrong variable.

This principle generalises. Behind almost every standard antiderivative in the Class-12 syllabus there is a substitution that exposes its triviality:
- $\int \frac{dx}{\sqrt{1 - x^2}} = \arcsin x$ comes from $x = \sin\theta$, exposing $d\theta$.
- $\int \sec x\,dx = \ln|\sec x + \tan x|$ comes from $t = \sec x + \tan x$, exposing $dt/t$.
- $\int \frac{dx}{x \ln x} = \ln|\ln x|$ comes from $u = \ln x$, exposing $du/u$.

In each case the antiderivative is not a deep fact about the original integrand; it is the *trivial* antiderivative in a hidden coordinate system. The substitution is the bridge.

The principle is sharper than its formulation suggests, however. *Most* problems are not stated in the optimal coordinates, because the natural language of problem-posing favours the *physical* or *concrete* variables (time, position, side-length, angle of incidence) rather than the *mathematically convenient* ones (sun-elevation angle, half-angle parameter, semi-perimeter). The solver's job is to perform the conversion. This is the structural reason that substitution is the workhorse of method selection: it is the operational complement to Hidden Structure (the recognition of which structural category a problem belongs to), and together they constitute the *transformation* half of Pillar 2.

### 1.3 The Cognitive Shift

Understanding substitution intellectually is one matter; reaching for it instinctively is another. The difficulty is again a habit installed early. From elementary algebra onward, students are trained to take the variables in a problem at face value: *let $x$ be the unknown; solve for $x$*. The variable in the problem is treated as the right variable. When the variable does not yield to standard manipulation, the student concludes that the problem is hard, not that the variable is wrong.

The cognitive shift is small in form and large in consequence. Most students, on encountering a problem, immediately ask: *what does the equation say about $x$?* The substitution-trained solver asks instead: *is $x$ the right variable, or is there a $y = \phi(x)$ in which the problem becomes routine?* This reordering — *choose the variable before solving* — is what separates the methodical professional from the diligent novice.

Consider how the shift plays out on a problem we will treat in §4.3. The problem asks: *evaluate $\int_0^{\pi/2} \frac{dx}{1 + \sin x + \cos x}$.* The novice, having read the problem, reaches for trigonometric identities, perhaps $\sin x + \cos x = \sqrt{2}\sin(x + \pi/4)$, and tries to massage the integrand into a recognisable form. The attempt is not wrong; with patience it can be made to work. But the novice is computing in the wrong variable. The integrand is a *rational function of $\sin x$ and $\cos x$*, and for any such integrand there is a single canonical substitution — $t = \tan(x/2)$ — that converts the trigonometric structure into rational structure. After the substitution, the integrand becomes $dt/(1 + t)$, the integration is one line, and the answer ($\ln 2$) drops out.

The substitution-trained solver pauses, recognises the *form* of the integrand (rational in $\sin, \cos$), reaches for the canonical substitution, and executes mechanically. The novice spends fifteen minutes; the trained solver spends two. The two solvers differ not in algebraic skill but in *first move*. The trained solver has learnt to ask *what variable would make this routine?* before reaching for any technique.

This shift manifests in four habits that distinguish substitution-aware solvers.

1. **A reflexive scan for canonical substitutions.** On encountering any integral, equation, inequality, or ODE, the trained solver runs a quick mental inventory: is the integrand rational in $\sin, \cos$ (Weierstrass)? Does $\sqrt{a^2 - x^2}$ appear (trig sub)? Is the ODE Bernoulli ($v = y^{1-n}$)? Are the sides of a triangle present (Ravi)? Is a Laurent polynomial in $x$ and $1/x$ involved ($y = x + 1/x$)? The inventory is short — perhaps twenty canonical substitutions in all of high-school and early-undergraduate mathematics — and the trained solver has memorised it.

2. **A willingness to introduce a new symbol.** Novices resist introducing a new variable. They feel they should solve the problem in its given variables, as if changing the symbol were sidestepping the question. The trained solver does the opposite: at the first sign of difficulty, they reach for a new symbol. *Let $t = \tan(x/2)$; let $u = \ln x$; let $a = y + z$, $b = z + x$, $c = x + y$.* The new symbol is the act of moving to the easier coordinates.

3. **Disciplined transport of the differential and the limits.** The most common failure mode for novices applying substitution is to transform the integrand and forget to transform $dx$, or to transform the integrand and forget to transform the limits. The trained solver always performs the substitution as a *triple* — integrand, differential, and limits — in lockstep.

4. **Transport-back as a final, separate step.** Every substitution is matched by an inverse. The trained solver, having solved the transformed problem, performs the inverse transport explicitly: *here is $t$; what is $x$?* The novice frequently leaves the answer in transformed variables, producing an "answer" that is technically correct but does not answer the original question.

The fourth habit is, again, the hardest. The transport-back step feels redundant after the hard work has been done. Skipping it is rarely fatal but is always a sign of incomplete execution. *Substitution is not finished until the answer has been expressed in the original variables.*

---

## 2. The Deep Structure

### 2.1 Mathematical Foundations

The strategy of substitution, like the previous four archetypes, is a feature of mathematical architecture and not a problem-solving technique invented in isolation. The foundational architecture is that *every mathematical structure admits coordinate-free expressions of its properties, but particular coordinate choices make particular properties manifest*. Substitution is the act of choosing coordinates to manifest the property one needs.

When we say a problem $P$ on parameter space $V$ admits a substitution $\phi : W \to V$, we are asserting the existence of an *isomorphism* between $V$ and $W$ in the relevant category — sets, smooth manifolds, algebraic varieties, or whatever the problem requires. The isomorphism transports the problem from one coordinate system to another. The structural fact behind the chapter is therefore that *isomorphic spaces support isomorphic problems*, and the operational skill is the recognition that for any given problem there is a coordinate isomorphism that simplifies it.

For competition mathematics, three foundational theorems organise the substitution archetype.

\begin{theorem}[Change of Variable for Definite Integrals]
Let $\phi : [\alpha, \beta] \to [a, b]$ be a continuously differentiable, monotone bijection with $\phi(\alpha) = a$ and $\phi(\beta) = b$, and let $f : [a, b] \to \mathbb{R}$ be continuous. Then
\[
  \int_a^b f(x)\,dx \;=\; \int_\alpha^\beta f(\phi(t)) \, \phi'(t)\,dt.
\]
\end{theorem}

The theorem is the analytic formalisation of the substitution operation in integration. The hypothesis that $\phi$ be monotone and continuously differentiable is essential: a non-monotone substitution would double-count regions; a non-differentiable substitution would have an undefined Jacobian $\phi'(t)$. The conclusion is that the *transported* integrand $f(\phi(t)) \phi'(t)$ on the new interval $[\alpha, \beta]$ has the same definite integral as the original $f(x)$ on $[a, b]$ — a *coordinate-invariance* statement for the Riemann integral. We use this theorem in Worked Example 1 (Sun-Shadow) and Worked Example 3 (Weierstrass).

\begin{theorem}[Inverse Function Theorem, one-variable form]
Let $f : U \to \mathbb{R}$ be continuously differentiable on an open interval $U \subseteq \mathbb{R}$, and suppose $f'(x_0) \ne 0$ for some $x_0 \in U$. Then there exists an open neighbourhood $V$ of $x_0$ on which $f$ is a bijection onto its image $f(V)$, the inverse $f^{-1} : f(V) \to V$ is continuously differentiable, and
\[
  (f^{-1})'(y) \;=\; \frac{1}{f'(f^{-1}(y))} \qquad \text{for } y \in f(V).
\]
\end{theorem}

The Inverse Function Theorem is the local guarantee that a substitution is invertible whenever its Jacobian is non-zero. In one dimension, *non-zero derivative* and *local bijection* are equivalent; in higher dimensions, the analogous statement involves the non-vanishing of the Jacobian determinant. The theorem is the structural reason that substitutions work *locally*: even when $\phi$ is not globally bijective (for example, $\phi(t) = \sin t$ on $\mathbb{R}$), it is locally bijective wherever its derivative is non-zero. The trained solver, working with a substitution like $x = \sin\theta$, always restricts the range of $\theta$ to an interval where $\cos\theta \ne 0$ — typically $[-\pi/2, \pi/2]$ — to ensure a global bijection in the working domain.

\begin{theorem}[Substitution as Functorial Pullback]
Let $\phi : W \to V$ be a smooth map, and let $\omega$ be a differential form on $V$. Then the pullback $\phi^* \omega$ is a differential form on $W$ given, in local coordinates, by the substitution rule
\[
  \phi^*\!(f(x_1, \ldots, x_n)\,dx_1 \wedge \cdots \wedge dx_n) \;=\; f(\phi(t_1, \ldots, t_n))\,J_\phi(t)\,dt_1 \wedge \cdots \wedge dt_n,
\]
where $J_\phi(t)$ is the Jacobian determinant. Integration is invariant under pullback: $\int_{\phi(W)} \omega = \int_W \phi^* \omega$ (when $\phi$ is an orientation-preserving diffeomorphism onto its image).
\end{theorem}

The pullback theorem (informal statement) is the multivariable generalisation of the change-of-variable formula. It is the structural fact behind every substitution in the calculus of several variables — polar coordinates in $\mathbb{R}^2$, spherical in $\mathbb{R}^3$, Jacobian determinants in change-of-variables formulas for multiple integrals. The Jacobian factor $\phi'(t)$ in one dimension generalises to the determinant $J_\phi(t)$ in higher dimensions; the substitution-as-pullback perspective explains why. We will not need the full multivariable version in this chapter, but the structural perspective — that substitution is a *functor* taking objects on $V$ to corresponding objects on $W$ — is the unifying foundation.

A fourth observation is worth stating, though we do not need it as a formal theorem. *Many substitutions are bijections only after a quotient*. The substitution $u = x^2$, for example, identifies $x$ and $-x$; on the half-line $x \ge 0$ it is a bijection. The substitution $t = \tan(x/2)$ is a bijection from $(-\pi, \pi)$ to $\mathbb{R}$, but not from any larger interval — at $x = \pm\pi$ the substitution is undefined. The substitution $x = \sin\theta$ is a bijection from $[-\pi/2, \pi/2]$ to $[-1, 1]$, but not from $[0, 2\pi]$. The competent solver, in choosing a substitution, also chooses the *domain* on which it is a bijection. We will see this care exercised throughout the worked examples.

### 2.2 Physical and Cross-Domain Foundations

The substitution archetype has rich cross-domain instances. We mention four.

In *classical mechanics*, the most consequential substitution is the move from Cartesian coordinates $(x, y, z)$ to *generalised coordinates* $(q_1, q_2, \ldots, q_n)$ adapted to the constraints of the system. A bead on a circular wire is awkward in Cartesian coordinates (the constraint $x^2 + y^2 = r^2$ is implicit in every equation) but trivial in polar coordinates (the constraint becomes "$r = r_0$ constant," and the only degree of freedom is the angular coordinate $\theta$). The Lagrangian and Hamiltonian formulations of mechanics elevate the choice of coordinates from a convenience to a *foundational principle*: the laws of motion are *invariant* under change of generalised coordinates, and the substitution from one set to another is the operational core of *canonical transformations* — the deepest expression of substitution in physics.

In *electrical engineering*, the substitution from time-domain to frequency-domain via the Fourier transform is the workhorse of signal processing. A signal $f(t)$ in the time domain (Hertz of pressure, say) is the same object as its Fourier transform $\hat f(\omega)$ in the frequency domain (amplitude as a function of frequency). The *operations* of convolution, filtering, differentiation, and modulation each have a simpler form in one domain than in the other; the practitioner moves freely between domains, doing each operation in whichever domain makes it easy. This is the engineering version of the chapter's principle: *choose the variable in which the problem is easy.*

In *number theory*, the substitution from $\mathbb{Z}$ to $\mathbb{Z}/p\mathbb{Z}$ — that is, reducing modulo a prime $p$ — is the move that converts an arithmetic problem into a finite-field problem, often vastly easier. Fermat's little theorem ($a^{p - 1} \equiv 1 \pmod p$) is the substitution-into-$\mathbb{F}_p$ version of a statement about integers. The proof of Wilson's theorem, the statement that $(p - 1)! \equiv -1 \pmod p$ for prime $p$, proceeds by substituting into $\mathbb{F}_p$ and using the group structure of $\mathbb{F}_p^\times$. The substitution is informal — we have not "substituted a variable" so much as "reduced the parameter space" — but the cognitive move is the same: *change the setting so the operation becomes easy.*

In *computer science*, the substitution of one variable name for another — *alpha-conversion* in the lambda calculus, *variable renaming* in compiler optimisation, *substitution of a value for a free variable* in beta-reduction — is the operational core of programming-language semantics. Two programs that differ only by a renaming of bound variables are by definition the same program; the substitution is a coordinate change in the space of programs. Compiler optimisations frequently consist in finding the substitution (a constant for a variable, a tail-recursive form for a recursive form) that makes a program shorter or faster. *Substitution is the canonical move in any setting where one expression is to be replaced by an equivalent one.*

The point is the same in each case: *the world is structurally invariant under change of coordinates, and choosing the right coordinates is the cognitive operation that converts an intractable representation into a tractable one*. Substitution in mathematics is the formal expression of a near-universal cognitive operation.

### 2.3 Cognitive Foundations

The cognitive function that allows a human solver to perform substitutions fluently is, broadly, the capacity for *representational re-encoding* — the ability to recognise that two distinct representations of the same object are equivalent under a translation rule, and to switch between them at will. This capacity is what allows a fluent reader to translate between languages without thinking of either language as the "real" one; it is what allows a chess master to switch between algebraic and descriptive notation without losing track of the game; it is what allows a fluent mathematician to switch between Cartesian and polar coordinates without losing track of the figure.

Representational re-encoding is *learned*. It is built up by exposure to many problems in which a particular substitution recurs. A student who has worked through fifty problems involving the Weierstrass substitution recognises it on the fifty-first as quickly as one recognises a familiar face. The capacity is not memorisation of a substitution table; it is structured pattern recognition — the trained eye sees the *form* of the integrand (rational in $\sin, \cos$) and instantly reaches for the substitution.

A further cognitive ingredient deserves comment. Substitution requires the solver to *hold two representations in mind simultaneously* — the original in $x$ and the substituted in $t$ — and to compute fluently in both. The mental burden is non-trivial; novices often "lose" one of the representations mid-computation, producing answers in the wrong variable or computing with the wrong differential. The discipline of writing down the substitution explicitly — *let $t = \tan(x/2)$; then $\sin x = 2t/(1+t^2)$, $\cos x = (1 - t^2)/(1 + t^2)$, $dx = 2\,dt/(1 + t^2)$* — is the mechanical compensation for this cognitive cost. It externalises one of the two representations, allowing the working memory to focus on the other.

The mature mathematician internalises both representations and switches effortlessly. The student arriving at olympiad-level work is still building this fluency. A useful exercise is to perform each canonical substitution explicitly *ten times* on representative problems, until the substitution becomes automatic. After ten repetitions, the substitution rule is no longer a thing to be recalled; it is a thing one *is*.

---

## 3. The Diagnostic Toolkit

### 3.1 The Three Questions Method (Substitution Edition)

We now collect, in operational form, the questions a trained solver asks on first contact with a problem that may admit a substitution.

**Question 1 — What variable is making the problem hard?** Look at the integrand, the equation, the constraint, the ODE, and identify *which variable* is the source of the difficulty. Is it a transcendental variable (a trigonometric function) appearing inside an algebraic expression? Is it a constrained variable (a triangle side) coupled to a complicated inequality? Is it a nonlinear variable appearing inside an ODE? The hard variable is the one to replace.

**Question 2 — What substitution would make that variable disappear or simplify?** Once the hard variable is identified, the canonical substitution is usually visible. A rational function of $\sin x, \cos x$ wants $t = \tan(x/2)$. A $\sqrt{1 - x^2}$ wants $x = \sin\theta$. A triangle-side constraint wants Ravi. A Bernoulli ODE wants $v = y^{1-n}$. A multiplicative functional equation wants $u = \ln x$. The list is short, and a trained solver has internalised it.

**Question 3 — How do I transport the answer back?** Every substitution comes with an inverse. After solving the transformed problem in $W$, compute the inverse $\phi^{-1}$ explicitly, and write the answer in the original variables of $V$. The transport-back step is small, but skipping it answers a different question.

The Three Questions Method (Substitution Edition) is the conversation between a novice and an experienced solver, internalised. Practising it for a few weeks installs it as instinct.

### 3.2 Forms of Substitution: A Comprehensive Guide

We now lay out, for reference, the four canonical forms of substitution and a working diagnostic for each.

- **Form I — Algebraic substitution.** *Diagnostic.* The problem features a polynomial, rational, or algebraic expression with a *symmetric* or *homogeneous* structure that the surface variables obscure. *Move.* Introduce a new variable that is an algebraic combination of the old, chosen to expose the symmetric or homogeneous structure. *Primer.* The substitution $y = x + 1/x$ converts a Laurent polynomial $a x^2 + b x + c + b / x + a / x^2$ (palindromic, degree $4$ in $x$ and $1/x$) into a polynomial $a y^2 + b y + (c - 2 a)$ (degree $2$ in $y$) — *halving the degree of the unknown*. Tschirnhaus's shift $x \mapsto x - a_{n-1}/(n a_n)$ eliminates the second-highest coefficient of any degree-$n$ polynomial, yielding the *depressed* form to which Cardano's cubic formula and Ferrari's quartic formula apply. *Examples.* PP1 (the inverse of $f(x) = x + 1/x$); PP2 (the substitution-driven functional equation $F(x^2) = x^2(1 + x)$); PP7 (vector substitution into a linear system). Algebraic substitutions are most common in equations, functional equations, and any problem with a hidden symmetric structure.

- **Form II — Trigonometric substitution.** *Diagnostic.* The integrand or expression contains an algebraic radical of the form $\sqrt{a^2 - x^2}$ (use $x = a \sin\theta$), $\sqrt{a^2 + x^2}$ (use $x = a \tan\theta$ or $x = a \sinh u$), $\sqrt{x^2 - a^2}$ (use $x = a \sec\theta$ or $x = a \cosh u$); or the integrand is a rational function of $\sin x$ and $\cos x$ (use the Weierstrass $t = \tan(x/2)$). *Move.* Replace the algebraic radical with its trigonometric counterpart (e.g., $\sqrt{1 - \sin^2\theta} = |\cos\theta|$), transforming the integrand into a function in which trigonometric identities apply directly. *Primer.* The Weierstrass substitution $t = \tan(x/2)$ is the *universal* converter from trig-rational integrals to rational integrals; it is to trig what the partial-fraction decomposition is to polynomials. *Examples.* WE3 (Weierstrass tangent half-angle for $\int_0^{\pi/2} \frac{dx}{1 + \sin x + \cos x}$); PP3 (geometric-series substitution paired with inverse-trig identity); PP4 ($x = \sin\theta$ in $\int_0^1 \sqrt{1 - x^2}\,dx$). Trigonometric substitutions are the backbone of integration of algebraic and trigonometric expressions.

- **Form III — Geometric substitution.** *Diagnostic.* The configuration involves a constrained geometric object (a triangle with side-length constraints; a point on a curve; a point in a region) whose constraint is awkward in the natural coordinates. *Move.* Recoordinatise to a parametrisation in which the constraint becomes automatic (Ravi substitution makes the triangle inequality automatic) or trivial (parametric representation of the unit circle makes $x^2 + y^2 = 1$ automatic). *Primer.* The Ravi substitution $a = y + z, b = z + x, c = x + y$ for $x, y, z > 0$ is the canonical "swallow-the-triangle-inequality" move. *Examples.* WE2 (Ravi substitution in the Hadwiger–Finsler inequality). Cross-archetype: the polar–Cartesian substitution surfaces in many of the Symmetry-archetype worked examples in Chapter 2. Geometric substitutions dominate olympiad geometry and triangle inequalities.

- **Form IV — Integral / differential substitution.** *Diagnostic.* The problem is an integral, a definite integral with limits, or an ODE in which the integrand or right-hand side is a composite function $f(g(x))$ or a power $y^n$ with $n \ne 0, 1$. *Move.* For integrals: $u = g(x)$, $du = g'(x)\,dx$, converting $\int f(g(x))\,g'(x)\,dx$ into $\int f(u)\,du$. For ODEs of Bernoulli type $y' + P(x) y = Q(x) y^n$: $v = y^{1-n}$, converting the nonlinear ODE into the linear ODE $v' + (1 - n) P(x) v = (1 - n) Q(x)$. For functional equations on $(0, \infty)$: $u = \ln x$, converting multiplicative arguments into additive ones. *Examples.* WE1 (Sun-Shadow, time-to-angle substitution in a definite integral); WE3 (Weierstrass, also Form IV); PP4 ($x = \sin\theta$); PP5 (Bernoulli ODE); PP6 (logarithmic substitution in Cauchy multiplicative–additive). Integral and differential substitutions are the workhorse of calculus past the freshman level.

The four forms are not mutually exclusive. The Weierstrass substitution is at once Form II and Form IV. The Ravi substitution is at once Form I (algebraic in $x, y, z$) and Form III (geometric in the triangle). The trained solver does not parse a substitution into its forms in the moment; the forms are a *retrospective* taxonomy, useful for pedagogy and for cataloguing the canonical substitutions. In the moment, the solver simply reaches for the right substitution.

### 3.3 Common Pitfalls

The substitution archetype exposes the solver to five recurring errors. The first four are mechanical; the fifth is strategic. Knowing them in advance is half the cure.

**Pitfall 1 — Failing to transform the differential.** The most common error in substitution is to replace $x$ by $\phi(t)$ in the integrand but to leave $dx$ unchanged. The differential must transform: $dx = \phi'(t)\,dt$. A solver who writes $\int_0^1 \sqrt{1 - x^2}\,dx$ and substitutes $x = \sin\theta$ must also write $dx = \cos\theta\,d\theta$. The integrand becomes $\cos\theta \cdot \cos\theta\,d\theta = \cos^2\theta\,d\theta$. Forgetting the $\cos\theta$ from the differential produces a wrong answer by a factor of $\cos\theta$ — and worse, the wrong answer is dimensionally wrong (the integrand has the wrong units), so the error is detectable. The cure is the *triple discipline*: transform integrand, differential, *and* limits in lockstep.

**Pitfall 2 — Failing to transform the limits of integration.** A close cousin of Pitfall 1. A solver substitutes $x = \sin\theta$ but leaves the limits of integration as $0$ and $1$ rather than transforming them to $0$ and $\pi/2$. The resulting integral has the wrong domain and produces a wrong (and undetectable, in many cases) answer. The cure is the triple discipline: transform integrand, differential, and limits together, *always*.

**Pitfall 3 — Choosing a substitution that does not simplify.** A solver, eager to substitute, picks a substitution that *technically* works but does not make the problem easier. *Let $u = x + 1$* on $\int \sin x\,dx$ produces $\int \sin(u - 1)\,du$, which is no easier than the original. The substitution must be chosen with a specific simplification in mind; substitution for its own sake is wasted effort. The cure is to *anticipate* the simplification before substituting: *"after this substitution, the integrand will be $f(u)$ for some recognisable $f$."*

**Pitfall 4 — Forgetting the domain restriction.** Many substitutions are bijections only on a restricted domain. The substitution $x = \sin\theta$ is a bijection from $[-\pi/2, \pi/2]$ to $[-1, 1]$, not from any larger interval. The substitution $t = \tan(x/2)$ is a bijection from $(-\pi, \pi)$ to $\mathbb{R}$, but at $x = \pm\pi$ it diverges. The substitution $u = \ln x$ requires $x > 0$. A solver who applies a substitution outside its valid domain produces an incorrect answer, or worse, a confusing one. The cure is to *state the domain of validity* when introducing the substitution and to verify that the working range is inside it.

**Pitfall 5 — Failing to transport the answer back to the original variables.** A solver computes $\int \frac{dt}{1 + t}$ in transformed variables and concludes $\ln 2$ — correct as the value of the definite integral, since the substitution was performed with transformed limits. But if the original problem asked for an *indefinite* integral or an answer expressed in $x$, the solver must transport back via $x = 2 \arctan t$. The cure is the *transport-back checklist*: every substitution has an inverse, and the answer in transformed variables is not the answer to the original question until the inverse has been applied.

The five pitfalls are sufficiently general that a checklist applied to every substitution — *integrand transformed? differential transformed? limits transformed? domain inside the substitution's range? answer transported back?* — would catch the vast majority of errors. We recommend it.

---

## 4. Worked Examples

We turn now from the diagnostic to the operational. Three worked examples follow. Each illustrates a distinct form of substitution. Each is sourced from K.D. Joshi's *Educative JEE Mathematics* — Chapters 18 and 24. The presentation follows the six-point framework of Pillar 1: Seed, Brute Path, Elegant Pivot, Pitfalls, Connections, Takeaway.

### 4.1 Example 1 — Sun-Shadow Work-Rate

\begin{problem}
The Sun rises and sets at $6{:}00$ a.m. and $6{:}00$ p.m. respectively. A man starts working in the sun at $8{:}00$ a.m. At any time his rate of work is proportional to the length of his shadow. He finishes half his work by noon, rests for two hours, then resumes. When does he complete the work? (Assume the Sun's elevation is a piecewise-linear function of time, with maximum elevation $90°$ at noon, and that the shadow length is proportional to $\cot\alpha$, where $\alpha$ is the elevation angle.)
\end{problem}

**Source.** K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), Chapter 24, Exercise 24.16.

**Seed.** The problem is, on the surface, a word problem about a worker and the Sun. The structural category is a *definite-integral equation*: the work done from $t_1$ to $t_2$ is $\int_{t_1}^{t_2} L(t)\,dt$, where $L(t) \propto \cot(\alpha(t))$ is the shadow length, and $\alpha(t)$ is the Sun's elevation at time $t$. The unknown is the time $T$ at which $\int_{14}^T L(t)\,dt = \int_8^{12} L(t)\,dt$ (afternoon work equals morning work; each is half the total). The hard variable is *time* $t$, because $\cot(\alpha(t))$ as a function of $t$ is awkward to integrate. The right variable is the *elevation* $\alpha$ itself, because $\cot\alpha$ has the trivial antiderivative $\ln|\sin\alpha|$.

**Brute path.** Set up the integrand $\cot(\alpha(t))$ explicitly in $t$ and attempt to integrate. Define the Sun's elevation as the piecewise linear function $\alpha(t) = (\pi/12)(t - 6)$ for $t \in [6, 12]$ (morning, in radians) and $\alpha(t) = (\pi/12)(18 - t)$ for $t \in [12, 18]$ (afternoon). The morning integrand is $\cot((\pi/12)(t - 6))$. Trying to integrate this in $t$ directly leads to $\int \cot(at + b)\,dt = (1/a) \ln|\sin(at + b)| + C$ — which is correct but is, structurally, *exactly* the substitution we are about to perform, dressed up as a "table" entry. The brute path is the substitution in disguise.

**Elegant pivot.** Substitute the elevation $\alpha$ as the integration variable. For the morning, with $\alpha = (\pi/12)(t - 6)$, we have $d\alpha = (\pi/12)\,dt$, so $dt = (12/\pi)\,d\alpha$. The limits transform: $t = 8 \Rightarrow \alpha = \pi/6$; $t = 12 \Rightarrow \alpha = \pi/2$. The morning work integral becomes
\[
  W_{\text{morning}} \;=\; \int_8^{12} \cot(\alpha(t))\,dt \;=\; \frac{12}{\pi} \int_{\pi/6}^{\pi/2} \cot\alpha\,d\alpha \;=\; \frac{12}{\pi} \big[ \ln|\sin\alpha| \big]_{\pi/6}^{\pi/2} \;=\; \frac{12}{\pi} \ln 2.
\]
(We used $\sin(\pi/2) = 1$ and $\sin(\pi/6) = 1/2$, so $\ln 1 - \ln(1/2) = \ln 2$.)

By the problem's data, $W_{\text{morning}} = (1/2) W_{\text{total}}$, so $W_{\text{total}} = (24/\pi) \ln 2$ and the afternoon work also equals $(12/\pi) \ln 2$.

For the afternoon ($t \in [12, 18]$), with $\alpha = (\pi/12)(18 - t)$, we have $d\alpha = -(\pi/12)\,dt$, so $dt = -(12/\pi)\,d\alpha$. The limits transform: $t = 14 \Rightarrow \alpha = \pi/3$; $t = T \Rightarrow \alpha_T := (\pi/12)(18 - T)$. The afternoon work integral is
\[
  W_{\text{afternoon}} \;=\; \int_{14}^T \cot(\alpha(t))\,dt \;=\; -\frac{12}{\pi} \int_{\pi/3}^{\alpha_T} \cot\alpha\,d\alpha \;=\; \frac{12}{\pi} \int_{\alpha_T}^{\pi/3} \cot\alpha\,d\alpha \;=\; \frac{12}{\pi} \ln\frac{\sin(\pi/3)}{\sin\alpha_T}.
\]
Set this equal to $(12/\pi) \ln 2$:
\[
  \ln\frac{\sin(\pi/3)}{\sin\alpha_T} \;=\; \ln 2 \quad\Longrightarrow\quad \frac{\sqrt{3}/2}{\sin\alpha_T} \;=\; 2 \quad\Longrightarrow\quad \sin\alpha_T \;=\; \frac{\sqrt{3}}{4}.
\]
Therefore $\alpha_T = \arcsin(\sqrt{3}/4)$. To convert back to clock time:
\[
  T \;=\; 18 - \frac{12}{\pi}\,\alpha_T \;=\; 18 - \frac{12}{\pi}\,\arcsin\!\frac{\sqrt{3}}{4}.
\]
Numerically, $\sqrt{3}/4 \approx 0.4330$ and $\arcsin(0.4330) \approx 0.4479$ radians $\approx 25.66°$, so $T \approx 18 - (12/\pi)(0.4479) \approx 18 - 1.711 \approx 16.29$ hours. Converting the fractional part: $0.29 \times 60 \approx 17.3$ minutes. The man finishes at approximately $T \approx 4{:}17$ p.m.

**Pitfalls.**
- Setting up $\alpha(t)$ incorrectly. The Sun's elevation is *not* $90° - 15°(t - 6)$ for all $t$ — that formula is wrong on the morning leg (it gives elevation $> 90°$ at sunrise). The correct piecewise model is $\alpha(t) = (\pi/12)(t - 6)$ for $t \in [6, 12]$ and $\alpha(t) = (\pi/12)(18 - t)$ for $t \in [12, 18]$, equivalent to $\alpha(t) = (\pi/12)(6 - |t - 12|)$ on $[6, 18]$. The trained solver checks the boundary values ($\alpha(6) = 0$, $\alpha(12) = \pi/2$, $\alpha(18) = 0$) before proceeding.
- Forgetting the negative sign on $d\alpha/dt$ in the afternoon. After noon, the Sun's elevation *decreases* with time, so $d\alpha/dt < 0$. A solver who substitutes mechanically without tracking the sign will obtain the wrong limits of integration.
- Treating the rest period as if work continued. The man does *no work* between noon and $2$ p.m.; the integral over $[12, 14]$ contributes zero to the total. A solver who integrates over $[12, T]$ (omitting the break) will compute the wrong afternoon work.
- Stopping at $\alpha_T$ without converting back to clock time. The answer the problem demands is a *clock time*, not an angular value. The transport-back step (Pitfall 5) is essential here.

**Connections.**
- The same time-to-angle substitution underlies many problems in *uniform angular motion*: pendulum displacement as a function of time, planetary motion in Kepler's first law (with elliptical orbits), the angular position of a clock hand. In each case, the angular variable is *adapted to the physics* and the temporal variable is the wrong one for computation.
- The integrand $\cot\alpha\,d\alpha = d(\ln\sin\alpha)$ is the differential of $\ln\sin\alpha$ — an instance of the more general identity $\cot \cdot d(\sin) = d(\ln \sin)$. This is the *Form-IV substitution* in its most compact statement: the differential of a composite reveals the antiderivative.
- The numerical answer $\sin\alpha_T = \sqrt{3}/4$ has a curious geometric reading: at the moment the work is complete, the Sun's elevation is such that $\sin\alpha_T = \sqrt{3}/4$ — the same ratio that arises in inscribed-equilateral-triangle problems on the unit circle. The connection is coincidental but pedagogically pleasing.

**Takeaway.** *Whenever an integrand depends on a variable through a smooth monotone function, substitute that function as the new variable. The new variable's differential is the derivative of the function; the new limits are the function's values at the original limits; the integrand simplifies because the substituted variable is the one in which the original physical setup was "really" written. Time was the wrong variable; the Sun's elevation was always the right one.*

### 4.2 Example 2 — Ravi Substitution in the Hadwiger–Finsler Inequality

\begin{problem}
Let $ABC$ be a triangle with side lengths $a, b, c$ and area $\Delta$. Prove that
\[
  2(ab + bc + ca) - (a^2 + b^2 + c^2) \;\ge\; 4\sqrt{3}\,\Delta,
\]
with equality if and only if $ABC$ is equilateral.
\end{problem}

**Source.** K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), Chapter 24, Exercise 24.93(b); the inequality is classically attributed to Hadwiger and Finsler.

**Seed.** The inequality is in the three side-lengths $a, b, c$ of a triangle, with the area $\Delta$ on the right. The triple $(a, b, c)$ is *constrained* by the three triangle inequalities $a < b + c$, $b < c + a$, $c < a + b$, which are awkward to use directly. The structural category is a *constrained inequality in three positive variables*, and the natural strategy is to *un-constrain* the variables via a substitution that automatically respects the triangle inequalities.

**Brute path.** Attempt the inequality in $(a, b, c)$ directly. One can try to use Heron's formula $\Delta^2 = s(s - a)(s - b)(s - c)$ with $s = (a + b + c)/2$, squaring the inequality, and grinding through the algebra in $a, b, c$. This is feasible but ugly: the resulting polynomial inequality has six monomials on each side, and the triangle-inequality constraints have to be invoked piecemeal to bound terms. The proof is correct but uninstructive.

**Elegant pivot.** Apply the *Ravi substitution*:
\[
  a \;=\; y + z, \qquad b \;=\; z + x, \qquad c \;=\; x + y \qquad (x, y, z > 0).
\]
This substitution is a bijection between the open set $\{(a, b, c) : a, b, c > 0,\ a < b + c,\ b < c + a,\ c < a + b\}$ and the open positive octant $\{(x, y, z) : x, y, z > 0\}$, with the explicit inverse
\[
  x \;=\; \frac{-a + b + c}{2}, \qquad y \;=\; \frac{a - b + c}{2}, \qquad z \;=\; \frac{a + b - c}{2}.
\]
(All three of $x, y, z$ are positive precisely when all three triangle inequalities hold; this is the *content* of the Ravi substitution.) Under Ravi, the inequality becomes an *unconstrained* inequality in three positive reals.

*Transform the LHS.* We compute
\[
  ab + bc + ca \;=\; (y + z)(z + x) + (z + x)(x + y) + (x + y)(y + z).
\]
Expand each product:
\[
\begin{aligned}
(y + z)(z + x) &= z^2 + xy + xz + yz, \\
(z + x)(x + y) &= x^2 + xy + xz + yz, \\
(x + y)(y + z) &= y^2 + xy + xz + yz.
\end{aligned}
\]
Sum: $ab + bc + ca = x^2 + y^2 + z^2 + 3(xy + yz + zx)$, so
\[
  2(ab + bc + ca) \;=\; 2(x^2 + y^2 + z^2) + 6(xy + yz + zx).
\]
Similarly,
\[
  a^2 + b^2 + c^2 \;=\; (y + z)^2 + (z + x)^2 + (x + y)^2 \;=\; 2(x^2 + y^2 + z^2) + 2(xy + yz + zx).
\]
Therefore the LHS of the inequality is
\[
  2(ab + bc + ca) - (a^2 + b^2 + c^2) \;=\; 4(xy + yz + zx).
\]

*Transform the RHS.* By Heron's formula with $s = x + y + z$ (note $s = (a + b + c)/2 = x + y + z$ under Ravi), $s - a = x$, $s - b = y$, $s - c = z$, so
\[
  \Delta^2 \;=\; s(s - a)(s - b)(s - c) \;=\; (x + y + z) \cdot x \cdot y \cdot z \;=\; xyz(x + y + z).
\]
Hence $\Delta = \sqrt{xyz(x + y + z)}$ and the RHS is $4\sqrt{3}\,\sqrt{xyz(x + y + z)}$.

*The reduced inequality.* In $(x, y, z)$, the inequality reads
\[
  4(xy + yz + zx) \;\ge\; 4\sqrt{3}\,\sqrt{xyz(x + y + z)} \quad\Longleftrightarrow\quad xy + yz + zx \;\ge\; \sqrt{3}\,\sqrt{xyz(x + y + z)}.
\]
Squaring both sides (legitimate since both are positive):
\[
  (xy + yz + zx)^2 \;\ge\; 3\,xyz(x + y + z). \qquad (\star)
\]

*Proof of $(\star)$.* Expand the LHS:
\[
  (xy + yz + zx)^2 \;=\; x^2 y^2 + y^2 z^2 + z^2 x^2 + 2xyz(x + y + z),
\]
where we used $2(xy \cdot yz + yz \cdot zx + zx \cdot xy) = 2xyz(y + x + z)$ after factoring $xyz$. Substituting:
\[
  (xy + yz + zx)^2 - 3 xyz(x + y + z) \;=\; x^2 y^2 + y^2 z^2 + z^2 x^2 - xyz(x + y + z).
\]
We now exhibit a *sum-of-squares* identity that shows this expression is non-negative:
\[
  x^2 y^2 + y^2 z^2 + z^2 x^2 - xyz(x + y + z) \;=\; \frac{1}{2}\Big[ (xy - yz)^2 + (yz - zx)^2 + (zx - xy)^2 \Big]. \qquad (\dagger)
\]
*Verification of $(\dagger)$.* Expand the right-hand side:
\[
\begin{aligned}
(xy - yz)^2 &= x^2 y^2 - 2xy^2 z + y^2 z^2, \\
(yz - zx)^2 &= y^2 z^2 - 2xyz^2 + z^2 x^2, \\
(zx - xy)^2 &= z^2 x^2 - 2x^2 yz + x^2 y^2.
\end{aligned}
\]
Sum: $2(x^2 y^2 + y^2 z^2 + z^2 x^2) - 2xyz(x + y + z)$. Half this is $x^2 y^2 + y^2 z^2 + z^2 x^2 - xyz(x + y + z)$, as claimed.

The right-hand side of $(\dagger)$ is manifestly non-negative (a sum of squares), hence $(\star)$ holds. Equality in $(\dagger)$ holds iff $xy = yz = zx$. Since $x, y, z > 0$, $xy = yz$ implies $x = z$, and $yz = zx$ implies $y = x$, so equality requires $x = y = z$. Under Ravi, $x = y = z$ corresponds to $a = b = c$, i.e., the equilateral case.

This completes the proof of the Hadwiger–Finsler inequality. $\blacksquare$

**Pitfalls.**
- Attempting the inequality in $(a, b, c)$ without the Ravi substitution. The Ravi substitution converts a *constrained* problem (sides of a triangle) into an *unconstrained* problem (positive reals), and unconstrained inequalities are vastly easier to handle.
- Forgetting to verify the equality case. Many inequality problems require *both* the inequality and the characterisation of equality. The SOS form $(\dagger)$ makes the equality case immediate: equality in a sum-of-squares holds iff each square vanishes.
- Using Heron's formula in a form that obscures the Ravi parameters. The form $\Delta^2 = s(s - a)(s - b)(s - c)$ is the right form; after Ravi, $s = x + y + z$ and $s - a, s - b, s - c$ are precisely $x, y, z$, giving the clean expression $\Delta^2 = xyz(x + y + z)$.
- Forgetting that the Ravi inverse map $(a, b, c) \mapsto (x, y, z) = ((-a+b+c)/2, (a-b+c)/2, (a+b-c)/2)$ has positive image *exactly* when the triangle inequalities hold. The substitution is a parametrisation of the *space of triangles*, not of arbitrary triples.

**Connections.**
- The intermediate inequality $(\star)$, $(xy + yz + zx)^2 \ge 3xyz(x + y + z)$, is a well-known symmetric-function inequality, often proved via Schur's inequality. The SOS proof we have given is the most elementary; Schur's inequality with $t = 1$ gives the same conclusion via a less transparent path. *Schur's inequality* states that for $x, y, z \ge 0$ and $t \ge 0$, $x^t(x - y)(x - z) + y^t(y - x)(y - z) + z^t(z - x)(z - y) \ge 0$, with the $t = 1$ specialisation equivalent to $(\star)$.
- The same Ravi substitution proves *Weitzenböck's inequality* ($a^2 + b^2 + c^2 \ge 4\sqrt{3}\,\Delta$) — strictly weaker than Hadwiger–Finsler — by an identical setup. Indeed, Hadwiger–Finsler can be written as Weitzenböck *plus* $(a - b)^2 + (b - c)^2 + (c - a)^2 \ge 0$, with equality iff the triangle is equilateral. This is the *refinement structure* between the two inequalities.
- The Ravi substitution recurs throughout olympiad triangle-inequality problems. It is the canonical "swallow-the-triangle-inequality" move and will reappear in Chapter 10 (Inequality) when we treat Erdős–Mordell, the AM-GM in triangle form, and the comparison of inradius and circumradius.
- Cross-archetype reuse: Ex. 24.93 also routes to Chapter 10 (Inequality) PP5 under the inequality-archetype framing. The two chapter treatments differ in emphasis — Chapter 5 names the substitution; Chapter 10 will name the inequality machinery — but the underlying problem is the same.

**Takeaway.** *Whenever a constraint awkwardly couples your variables, look for a substitution that absorbs the constraint into the parametrisation. The Ravi substitution converts "$a, b, c$ are sides of a triangle" into "$x, y, z$ are positive reals" at no cost to the problem. Unconstrained problems are always easier. After the substitution, standard inequality machinery (AM-GM, Cauchy–Schwarz, Schur, sum-of-squares) applies directly, and the equality case is read off from the structure of the proof.*

### 4.3 Example 3 — Weierstrass Tangent Half-Angle Substitution

\begin{problem}
Evaluate
\[
  I \;=\; \int_0^{\pi/2} \frac{dx}{1 + \sin x + \cos x}.
\]
\end{problem}

**Source.** K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), Chapter 18 (Definite Integrals), Comment 8. The Weierstrass tangent half-angle substitution is the canonical converter from trigonometric-rational integrals to ordinary rational integrals.

**Seed.** The integrand is a *rational function of $\sin x$ and $\cos x$* — that is, a ratio of polynomial expressions in $\sin x$ and $\cos x$. For any such integrand, there is a single canonical substitution — the *Weierstrass tangent half-angle*
\[
  t \;=\; \tan(x/2)
\]
— that converts the trigonometric structure into rational structure, after which the integral becomes a rational integral solvable by partial fractions or direct antidifferentiation. The hard variable is $x$ (the trigonometric argument); the easy variable is $t$.

**Brute path.** Attempt to evaluate the integral by trigonometric manipulation. One can write $1 + \sin x + \cos x = 1 + \sqrt{2}\sin(x + \pi/4)$, and try to massage the integral into a standard form. With patience, this works — one obtains $I = \ln 2$ — but the path is fiddly, error-prone, and not generalisable. The brute approach also blinds the solver to the *structural* fact that *every* integral of a rational function of $\sin x, \cos x$ submits to the same substitution; learning the substitution converts an entire class of problems into routine ones.

**Elegant pivot.** Apply the Weierstrass substitution $t = \tan(x/2)$. The standard identities are:
\[
  \sin x \;=\; \frac{2t}{1 + t^2}, \qquad \cos x \;=\; \frac{1 - t^2}{1 + t^2}, \qquad dx \;=\; \frac{2\,dt}{1 + t^2}.
\]
*Derivation (sketch).* Use the double-angle formulas. With $\theta = x/2$, we have $\sin x = 2 \sin\theta \cos\theta$ and $\cos x = \cos^2\theta - \sin^2\theta$. Dividing numerator and denominator by $\cos^2\theta$ in each (and using $\sec^2\theta = 1 + \tan^2\theta = 1 + t^2$) gives the displayed identities. The differential follows from $\theta = \arctan t$ and $x = 2\theta$: $dx = 2\,d\theta = 2\,dt/(1 + t^2)$.

*Transform the integrand.* The denominator becomes
\[
  1 + \sin x + \cos x \;=\; 1 + \frac{2t}{1 + t^2} + \frac{1 - t^2}{1 + t^2} \;=\; \frac{(1 + t^2) + 2t + (1 - t^2)}{1 + t^2} \;=\; \frac{2 + 2t}{1 + t^2} \;=\; \frac{2(1 + t)}{1 + t^2}.
\]
So the integrand becomes
\[
  \frac{1}{1 + \sin x + \cos x} \;=\; \frac{1 + t^2}{2(1 + t)}.
\]
Multiplying by $dx = 2\,dt/(1 + t^2)$:
\[
  \frac{dx}{1 + \sin x + \cos x} \;=\; \frac{1 + t^2}{2(1 + t)} \cdot \frac{2\,dt}{1 + t^2} \;=\; \frac{dt}{1 + t}.
\]
The integrand has collapsed from a rational function of $\sin x, \cos x$ to a rational function of $t$ — and a particularly simple one.

*Transform the limits.* When $x = 0$, $t = \tan 0 = 0$. When $x = \pi/2$, $t = \tan(\pi/4) = 1$. The limits of integration are $0$ and $1$.

*Compute the integral.* We have
\[
  I \;=\; \int_0^1 \frac{dt}{1 + t} \;=\; \big[\ln(1 + t)\big]_0^1 \;=\; \ln 2 - \ln 1 \;=\; \ln 2.
\]
Therefore $I = \ln 2 \approx 0.693$. $\blacksquare$

**Pitfalls.**
- Forgetting to transform the differential. A solver who replaces $\sin x, \cos x$ with their $t$-expressions but leaves $dx$ as $dx$ obtains a wrong integral. The triple discipline (integrand, differential, limits) is essential.
- Forgetting to transform the limits. A solver who computes the integrand in $t$ but leaves the limits as $0$ and $\pi/2$ obtains a different (and incorrect) integral. The new limits are $0$ and $1$.
- Misremembering the half-angle identities. The Weierstrass identities are standard but easy to garble. The trained solver derives them quickly from the double-angle formulas at the moment of use, or memorises the three lines as a unit. The most common error is to write $\sin x = 2t/(1 - t^2)$ (with a minus) or $\cos x = (1 + t^2)/(1 - t^2)$ — both wrong.
- Applying Weierstrass to an integral over an interval containing $x = \pi$ (or $\pm \pi$ modulo $2\pi$). At $x = \pi$, $t = \tan(\pi/2)$ is undefined; the substitution is singular. For intervals containing $\pi$, one must split the integral or use a different substitution.

**Connections.**
- The substitution $t = \tan(x/2)$ is, geometrically, the *stereographic projection* of the unit circle from the point $(-1, 0)$ onto the vertical line $x = 1$. Each point $(\cos x, \sin x)$ on the circle (with $\cos x \ne -1$) corresponds to the parameter $t = \tan(x/2)$ via the projection. This is the same parametrisation that generates *Pythagorean triples*: setting $t = q/p$ for integers $p, q$ gives the rational point $((p^2 - q^2)/(p^2 + q^2), 2pq/(p^2 + q^2))$ on the unit circle, hence the integer triple $(p^2 - q^2, 2pq, p^2 + q^2)$ satisfying $a^2 + b^2 = c^2$.
- The Weierstrass substitution is the *universal* trig-to-rational substitution: it converts *every* rational function of $\sin x, \cos x$ into a rational function of $t$, after which partial-fraction decomposition completes the integration in finitely many steps. The combination of Weierstrass + partial fractions is a *decision procedure* for the indefinite integration of any rational function of $\sin x, \cos x$.
- The same parametrisation $((1 - t^2)/(1 + t^2), 2t/(1 + t^2))$ of the unit circle is a special case of the *rational parametrisation* of an arbitrary conic. Every smooth conic admits a rational parametrisation; the Weierstrass substitution is the conic-parametrisation toolkit applied to a particular conic (the circle).
- Cross-archetype: this substitution will reappear in Chapter 14 (Geometric Identities) as the canonical rational parametrisation of the unit circle, and in Chapter 17 (a hypothetical placeholder for the *transcendence-to-algebra* archetype) as the prototype of "converting transcendental structure into algebraic structure."

**Takeaway.** *Whenever an integrand is a rational function of $\sin x$ and $\cos x$, apply the Weierstrass substitution $t = \tan(x/2)$. The three identities $\sin x = 2t/(1 + t^2)$, $\cos x = (1 - t^2)/(1 + t^2)$, $dx = 2\,dt/(1 + t^2)$ convert the integrand into a rational function of $t$, after which the integration is mechanical. The substitution is universal: every rational trig integrand submits to it. Memorise it.*

---

## 5. Practice Problems

The following seven problems exercise the substitution archetype across its four forms. Full solutions are in the appendix at the end of the chapter; the solver is encouraged to attempt each problem before consulting the solution.

### 5.1 Inverse of $f(x) = x + 1/x$ via Algebraic Substitution (JEE 2001; Joshi Ch. 24, Ex. 24.36)

Let $f : [1, \infty) \to [2, \infty)$ be defined by $f(x) = x + 1/x$. Find $f^{-1}(x)$.

### 5.2 Substitution-Driven Functional Equation (JEE 2001; Joshi Ch. 24, Ex. 24.40)

Let $F : (0, \infty) \to \mathbb{R}$ be the antiderivative $F(x) = \int_0^x f(t)\,dt$ of a continuous function $f$. If $F(x^2) = x^2(1 + x)$ for all $x > 0$, find $f(4)$.

### 5.3 Geometric-Series Substitution in an Inverse-Trig Identity (JEE 2001; Joshi Ch. 24, Ex. 24.26)

For $0 < |x| < \sqrt{2}$, find all $x$ satisfying
\[
  \sin^{-1}\!\Big(x - \tfrac{x^2}{2} + \tfrac{x^3}{4} - \cdots\Big) \;+\; \cos^{-1}\!\Big(x^2 - \tfrac{x^4}{2} + \tfrac{x^6}{4} - \cdots\Big) \;=\; \frac{\pi}{2}.
\]
(The two series are convergent geometric series in their respective arguments on this domain.)

### 5.4 Trigonometric Substitution for $\sqrt{1 - x^2}$ (Joshi Ch. 17, Comment 7)

Evaluate $\displaystyle\int_0^1 \sqrt{1 - x^2}\,dx$ by the substitution $x = \sin\theta$, and identify the geometric quantity computed.

### 5.5 Bernoulli ODE via Power Substitution (Joshi Ch. 19, Comment 4)

Solve the first-order ODE
\[
  \frac{dy}{dx} + y \;=\; x y^3.
\]

### 5.6 Logarithmic Substitution in the Multiplicative Cauchy Equation (Joshi Ch. 20, Comment 3)

Let $f : (0, \infty) \to \mathbb{R}$ be a continuous function satisfying
\[
  f(xy) \;=\; f(x) + f(y) \qquad \text{for all } x, y > 0.
\]
Prove that there exists a constant $c \in \mathbb{R}$ such that $f(x) = c \ln x$ for all $x > 0$.

### 5.7 Vector Substitution in a Linear System (JEE 1985; Joshi Ch. 21, Ex. 21.2(a))

Let $\vec a, \vec b, \vec c$ be non-coplanar vectors in $\mathbb{R}^3$. Find scalars $x, y, z$ such that
\[
  x \vec a + y \vec b + z \vec c \;=\; \vec a + 2 \vec b - 3 \vec c.
\]

---

## 6. The Connections Web

### 6.1 Substitution Across Mathematical Domains

The substitution archetype recurs across every major mathematical domain. We give one representative instance per domain.

- **Algebra.** A substitution is a *change of basis*. The transition from the basis $\{1, x, x^2, \ldots\}$ of the polynomial ring to the basis $\{1, x - a, (x - a)^2, \ldots\}$ centred at $x = a$ is a substitution that exposes the local structure at $a$. The Tschirnhaus shift (eliminating the second-highest term) is the algebraic substitution that simplifies the *form* of a polynomial.
- **Geometry.** A coordinate transformation — Cartesian to polar, rectangular to oblique, affine to projective — is a substitution. The same geometric object lives in many coordinate systems; the practitioner chooses the system in which the relevant property is most transparent.
- **Calculus & Analysis.** Definite-integral substitution ($u$-substitution), differential-equation substitution (Bernoulli, homogeneous, integrating factors), and Taylor expansion (substitution of a polynomial for a function, locally) are the three pillars of substitution in calculus.
- **Number Theory.** *Modular reduction* — passing from $\mathbb{Z}$ to $\mathbb{Z}/p\mathbb{Z}$ — is a substitution that converts an integer problem into a finite-field problem. Many statements (Fermat's little theorem, Wilson's theorem, quadratic reciprocity) are proved by modular substitution.
- **Combinatorics.** Generating-function substitution — passing from a sequence $\{a_n\}$ to $A(x) = \sum a_n x^n$, then substituting $x = 1$ or $x = -1$ to extract partial sums and alternating sums — is the substitution toolkit of analytic combinatorics.
- **Topology.** A *change of chart* on a smooth manifold is a substitution: the same point on the manifold has coordinates in many charts; the transition between charts is a smooth substitution. The substitution rule for differential forms ($\phi^*$) is the local expression of this idea.
- **Linear Algebra.** A *similarity transformation* $A \mapsto P^{-1} A P$ is a substitution of basis: the same linear map looks different in different bases. The substitution into an *eigenbasis* converts a complicated matrix into a diagonal one, exposing the underlying spectral structure.

The list is not exhaustive; it is meant to communicate the *ubiquity* of substitution and to suggest that recognising substitution in any one of these settings is *the same cognitive act* as recognising it in any other.

### 6.2 Substitution in Physics and Other Sciences

The substitution archetype recurs across disciplines.

- **Classical mechanics.** *Generalised coordinates* and *canonical transformations* (Hamilton–Jacobi) are the most consequential substitutions in physics. A constrained system in Cartesian coordinates is unconstrained in generalised coordinates adapted to the constraints; the Lagrangian formalism makes the choice of coordinates a *first-class principle* rather than a convenience.
- **Quantum mechanics.** A *change of basis* in Hilbert space — position basis to momentum basis via the Fourier transform, or to any other basis adapted to a particular observable — is the central computational move in quantum problem-solving. The Fourier transform is the substitution that diagonalises the momentum operator.
- **Statistical mechanics.** The *partition function* in a different ensemble (canonical, grand canonical, microcanonical) is a different functional of the same underlying microstate space; passing between ensembles is a substitution in the space of statistical descriptions, often via a Legendre transform.
- **Electrical engineering.** Time-domain to frequency-domain via Fourier; transient analysis to steady-state via the Laplace transform; circuit equations in one node basis vs. another. Each is a substitution chosen to make a particular operation easy.
- **Chemistry.** *Normal-mode coordinates* in a vibrating molecule decouple the equations of motion, converting a coupled system in Cartesian displacements into uncoupled oscillators in normal-mode amplitudes. The substitution is the diagonalisation of the dynamical matrix.

In each case, the substitution is *not* a clever trick local to one problem; it is a *structural feature* of the discipline. The mature practitioner moves between coordinates effortlessly, doing each operation in whichever coordinates make it easy.

### 6.3 Cross-Domain Manifestations

Beyond formal disciplines, substitution recurs across cognitive domains.

- **Linguistics.** Translation between languages is the cognitive analog of mathematical substitution. The same proposition can be expressed in English, Sanskrit, or German; the cognitive content is *invariant*, but particular ideas are expressible more economically in one language than another.
- **Computer Science.** *Alpha-conversion* in the lambda calculus, variable renaming in compiler optimisation, beta-reduction (substituting a value for a free variable) — these are the operational core of programming-language semantics, and they are substitution operations in the strictest sense.
- **Music Theory.** *Transposition* of a melody by a fixed interval is a substitution in the space of pitches; the melody is structurally invariant under transposition. *Modulation* between keys is a more sophisticated substitution that changes the harmonic basis.
- **Cartography.** *Map projections* — Mercator, Lambert, polar — are substitutions that convert the curved surface of the Earth into a flat representation. Each projection preserves some properties (angles, areas, shapes) and distorts others; the cartographer chooses the projection adapted to the purpose.

The cross-domain recurrence is, again, the signature of a foundational cognitive archetype.

### 6.4 Related Archetypes

Substitution interacts richly with several other archetypes in the Pillar 2 taxonomy.

- **Archetype 4: Hidden Structure.** *Substitution executes what Hidden Structure recognises.* When the polynomial-in-disguise reading of "a three-digit number $\overline{abc} = 100a + 10b + c$" reveals the hidden structure, the substitution $u = 100a + 10b + c$ (or its equivalent) is the operational move that exploits it. The two archetypes are inseparable: Hidden Structure names the category; Substitution carries the problem there.
- **Archetype 6: Linearization** (next chapter). *Linearization is a special substitution* — the replacement of a function by its tangent line at a point. Near $x = a$, $f(x) \approx f(a) + f'(a)(x - a)$ is the linear substitution that converts a nonlinear problem into a local linear one. The full Taylor expansion is iterated linearization; each iteration is a substitution.
- **Archetype 10: Inequality.** *The Ravi substitution is the canonical "swallow-the-constraint" move* for triangle inequalities; analogous substitutions exist for other constrained inequalities (the substitution $a = \sec\alpha, b = \sec\beta, c = \sec\gamma$ for problems where $a, b, c \ge 1$ couples to a sum-of-arguments constraint; the substitution $x = \cos^2\theta, y = \sin^2\theta$ for the constraint $x + y = 1$ with $x, y \ge 0$). Substitution is the bridge from constrained to unconstrained inequalities.
- **Archetype 14: Geometric Identities** (placeholder name). *Trigonometric substitutions are geometric identities in disguise.* The Weierstrass substitution is the stereographic projection of the unit circle; the substitution $x = \sin\theta$ for $\sqrt{1 - x^2}$ is the parametrisation of a right triangle.
- **Archetype 19: Functional Equations.** *Logarithmic substitution* converts multiplicative functional equations into additive ones (PP6). The substitution is the bridge that reduces an unfamiliar functional equation to the canonical Cauchy additive equation.
- **Archetype 20: Analogy.** *Substitution is the operational form of analogy.* When we say "this problem is analogous to that one," we mean that there is a substitution that converts one into the other. The most powerful analogies are precisely the most powerful substitutions.

The six related archetypes — Hidden Structure, Linearization, Inequality, Geometric Identities, Functional Equations, and Analogy — show how substitution is the *connective tissue* of method selection. Mastery of substitution is mastery of the operational vocabulary that links structural recognition to algebraic execution.

---

## 7. Master Takeaways

We collect the seven master takeaways of this chapter, in the language of working strategy.

1. **The right change of variables turns a hard problem into a routine one; the work is choosing the variable.** No further glossing: this *is* the chapter, in one sentence.

2. **Substitution and Hidden Structure are two faces of one move.** Hidden Structure recognises the category to which a problem belongs; Substitution carries the problem there. A solver fluent in only one of the two has only half the toolkit.

3. **Substitute first; compute second.** Most problems are not stated in the optimal coordinates. The trained solver, on first contact, asks *is this the right variable?* before doing any algebra. The reordering is the cognitive shift.

4. **The substitution that respects the problem's symmetry is the most powerful.** Ravi respects the cyclic symmetry of the triangle inequalities; Weierstrass respects the periodicity of the trigonometric functions; logarithmic substitution respects the multiplicative structure of the positive reals. The substitution that aligns with the problem's underlying symmetry is the substitution that makes the problem simplest.

5. **Always transform the differential and the limits.** Every substitution is a triple operation: integrand, differential, limits. Skipping the differential gives a wrong factor; skipping the limits gives a wrong domain. The triple discipline is non-negotiable.

6. **Always transport the answer back to the original variables.** A substitution is a round trip: forward via $\phi$, work in the new variables, return via $\phi^{-1}$. The return trip is what makes the final answer *answer the original question*.

7. **Memorise the canonical substitutions; their recognition is half the work.** The list is short — perhaps twenty substitutions across all of high-school and early-undergraduate mathematics — and the trained solver has internalised every one. When the integrand has $\sqrt{1 - x^2}$, the hand reaches for $x = \sin\theta$ before the conscious mind has finished reading the integral. This is fluency.

---

## 8. Self-Assessment Checklist

The following ten checkpoints test whether the chapter's content has become *unhesitating knowledge*. Each should evoke an immediate, confident yes. If any is hesitant, return to the relevant section before moving on.

- [ ] I can apply the Weierstrass substitution $t = \tan(x/2)$ from memory and recite the three identities $\sin x = 2t/(1 + t^2)$, $\cos x = (1 - t^2)/(1 + t^2)$, $dx = 2\,dt/(1 + t^2)$ without looking them up.
- [ ] I can recognise *at sight* an integrand that is a rational function of $\sin x$ and $\cos x$, and I reach for Weierstrass before any other technique.
- [ ] I can apply the Ravi substitution $a = y + z, b = z + x, c = x + y$ to any constrained inequality in triangle sides, and I can derive Heron's formula in Ravi coordinates ($\Delta^2 = xyz(x + y + z)$).
- [ ] I can solve any Bernoulli ODE $y' + P(x) y = Q(x) y^n$ ($n \ne 0, 1$) by the substitution $v = y^{1 - n}$, and I know the resulting linear equation $v' + (1 - n) P(x) v = (1 - n) Q(x)$ by structure.
- [ ] I can perform a definite-integral substitution $u = g(x)$ as a *triple* (integrand, differential, limits) without omitting any of the three, and I can state the change-of-variable theorem with its monotonicity hypothesis.
- [ ] I can recognise when a functional equation on $(0, \infty)$ admits a logarithmic substitution $u = \ln x$ to reduce to the Cauchy additive equation, and I know the continuity hypothesis is essential for the conclusion $f(x) = c \ln x$.
- [ ] I can compute the inverse of $f(x) = x + 1/x$ on $[1, \infty)$ from memory: $f^{-1}(x) = (x + \sqrt{x^2 - 4})/2$, choosing the $+$ branch by the domain constraint.
- [ ] I can state and verify the domain of validity of every canonical substitution I use (e.g., $x = \sin\theta$ requires $\theta \in [-\pi/2, \pi/2]$; $t = \tan(x/2)$ excludes $x = \pm\pi$).
- [ ] I can name at least five canonical substitutions outside the four worked examples, and I can give the diagnostic that calls each one (e.g., $x = a\sec\theta$ for $\sqrt{x^2 - a^2}$, $u = x^2$ for symmetric-in-sign expressions, Tschirnhaus shift for depressing a polynomial).
- [ ] I can explain to a beginner *why* the substitution that respects the problem's symmetry is the most powerful, and I can give one example each from algebra, integration, ODEs, and geometry.

---

## Bridge to Chapter 6: Linearization

Substitution has answered: *what change of variables makes the problem easy?* The next archetype — *Linearization* — answers a paired but more specific question: *what is the simplest substitution we can make, and when does it suffice?*

Linearization is itself a substitution — the replacement of a function $f(x)$ by its tangent line $f(a) + f'(a)(x - a)$ at a point $a$. The substitution is local: it is exact only at the point $a$ and approximate in a neighbourhood. But within that neighbourhood it is the *cheapest* substitution possible — a polynomial of degree $1$ replacing a function of unknown degree. The astonishing fact, which Chapter 6 will develop, is that this single move — linearise at a chosen point, work in the linear approximation, transport back — suffices for an enormous range of problems: rate-of-change problems, tangent-line geometry, Newton's method for root-finding, the first-order theory of differential equations near an equilibrium, error analysis in numerical computation, perturbation theory in physics, and the entire infinitesimal calculus.

Where Substitution chooses any clever variable, Linearization commits to one specific variable: the *deviation from a fixed point*. Where Substitution converts a problem into an equivalent one of comparable difficulty (and is exact), Linearization converts a hard nonlinear problem into an easy linear one (and is approximate). The two archetypes are siblings: Linearization is the *trade-off cousin* of Substitution, exchanging exactness for tractability.

The reader will recognise that several of this chapter's worked examples already contained linearization in disguise. The Sun-Shadow problem (WE1) used a *linear* model of the Sun's elevation as a function of time — the simplest possible substitution, and the one for which the integral has a closed form. The Hadwiger–Finsler proof (WE2) used the *linear* sum-of-squares identity $(\dagger)$ — a quadratic expression rewritten as a sum of *linear* differences squared. The Weierstrass substitution (WE3), though formally trigonometric, has a *linear* differential $dx = 2\,dt/(1 + t^2)$ that the integrand simply multiplies. The next chapter will name these linear moves as a single archetype and give them their own deep structure.

Together, Substitution (Chapter 5) and Linearization (Chapter 6) form the first half of the *Method Selection* sub-pillar of Pillar 2: the chapters in which the *transformation* of a problem into a more tractable form is the central skill. The second half (Chapters 7 and 8 — Telescoping and Normalization) will complete the sub-pillar, after which we will turn in Chapter 9 to the *Constraint Exploitation* sub-pillar, where the focus shifts from transforming the problem to *using* the structure of the constraints directly.

---

## Appendix — Solutions to Practice Problems

### Solution to 5.1 — Inverse of $f(x) = x + 1/x$

We are given $f : [1, \infty) \to [2, \infty)$, $f(x) = x + 1/x$. Set $y = x + 1/x$. Multiplying through by $x$ (positive on the domain): $xy = x^2 + 1$, i.e.,
\[
  x^2 - yx + 1 \;=\; 0.
\]
By the quadratic formula,
\[
  x \;=\; \frac{y \pm \sqrt{y^2 - 4}}{2}.
\]
We must pick the branch that lies in $[1, \infty)$. At $y = 2$, both roots coincide at $x = 1$; for $y > 2$, the two roots are $(y + \sqrt{y^2 - 4})/2 > 1$ and $(y - \sqrt{y^2 - 4})/2 < 1$. Since the domain of $f$ is $[1, \infty)$, we take the $+$ branch:
\[
  f^{-1}(y) \;=\; \frac{y + \sqrt{y^2 - 4}}{2}.
\]
*Verification.* Compute $f(f^{-1}(y))$. Let $x = (y + \sqrt{y^2 - 4})/2$; then $1/x = 2/(y + \sqrt{y^2 - 4}) = 2(y - \sqrt{y^2 - 4})/((y)^2 - (y^2 - 4)) = (y - \sqrt{y^2 - 4})/2$. Therefore $x + 1/x = (y + \sqrt{y^2 - 4})/2 + (y - \sqrt{y^2 - 4})/2 = y$. $\blacksquare$

**Key lesson.** The substitution $y = x + 1/x$ is *Form-I algebraic*: it converts a Laurent expression in $x$ into a polynomial in $y$. Inverting requires solving a quadratic in $x$ for given $y$, and the branch choice is dictated by the domain restriction. The substitution-and-branch-choice pair is the operational core of Form-I substitution in inverse-function problems.

### Solution to 5.2 — Substitution-Driven Functional Equation

We are given $F(x) = \int_0^x f(t)\,dt$, so by the Fundamental Theorem of Calculus, $F'(x) = f(x)$ for all $x > 0$. We are also given $F(x^2) = x^2(1 + x) = x^2 + x^3$ for all $x > 0$.

Differentiate both sides of $F(x^2) = x^2 + x^3$ with respect to $x$:
\[
  F'(x^2) \cdot 2x \;=\; 2x + 3 x^2.
\]
Divide both sides by $2x$ (valid for $x > 0$):
\[
  F'(x^2) \;=\; 1 + \tfrac{3}{2} x.
\]
But $F'(u) = f(u)$, so $f(x^2) = 1 + (3/2) x$. To find $f(4)$, set $x^2 = 4$, i.e., $x = 2$ (positive branch, since the domain is $x > 0$):
\[
  f(4) \;=\; 1 + \tfrac{3}{2}(2) \;=\; 1 + 3 \;=\; 4.
\]
*Verification.* Compute $F(u) = u + u^{3/2}$ (since $f(u) = 1 + (3/2) u^{1/2}$ integrates to $u + u^{3/2}$, with $F(0) = 0$). Then $F(4) = 4 + 8 = 12$. And the original equation says $F(x^2) = x^2(1 + x) = 4 \cdot 3 = 12$ at $x = 2$. ✓ $\blacksquare$

**Key lesson.** The substitution $u = x^2$ is *Form-I algebraic* (in the equation) combined with *implicit differentiation*: the chain rule produces the factor $2x$ on the LHS, which one then solves for $F'(x^2) = f(x^2)$. The transport-back step is $u = x^2 \Rightarrow x = \sqrt{u}$, yielding the closed form $f(u) = 1 + (3/2)\sqrt{u}$. *(Note: an earlier draft of the locked slate gave $f(4) = 5/2$; that value is inconsistent with the equation as stated. The correct value, verified independently above, is $f(4) = 4$. The locked slate has been patched accordingly.)*

### Solution to 5.3 — Geometric-Series Substitution in an Inverse-Trig Identity

On the domain $0 < |x| < \sqrt{2}$, both geometric series converge:
\[
\begin{aligned}
  x - \tfrac{x^2}{2} + \tfrac{x^3}{4} - \cdots &\;=\; x \cdot \sum_{k = 0}^{\infty} \big(-\tfrac{x}{2}\big)^k \;=\; \frac{x}{1 + x/2} \;=\; \frac{2x}{2 + x}, \\
  x^2 - \tfrac{x^4}{2} + \tfrac{x^6}{4} - \cdots &\;=\; x^2 \cdot \sum_{k = 0}^{\infty} \big(-\tfrac{x^2}{2}\big)^k \;=\; \frac{x^2}{1 + x^2/2} \;=\; \frac{2x^2}{2 + x^2}.
\end{aligned}
\]
(The first series requires $|x/2| < 1$, i.e., $|x| < 2$; the second requires $|x^2/2| < 1$, i.e., $|x| < \sqrt{2}$. The intersection of these conditions, with $x \ne 0$, is the stated domain.)

Let $u = 2x/(2 + x)$ and $v = 2x^2/(2 + x^2)$. The identity becomes $\sin^{-1} u + \cos^{-1} v = \pi/2$.

Using the standard identity $\sin^{-1} t + \cos^{-1} t = \pi/2$ for $t \in [-1, 1]$, the given equation is satisfied if and only if $u = v$:
\[
  \frac{2x}{2 + x} \;=\; \frac{2x^2}{2 + x^2}.
\]
Divide both sides by $2x$ (valid since $x \ne 0$):
\[
  \frac{1}{2 + x} \;=\; \frac{x}{2 + x^2} \quad\Longleftrightarrow\quad 2 + x^2 \;=\; x(2 + x) \;=\; 2x + x^2 \quad\Longleftrightarrow\quad 2 \;=\; 2x \quad\Longleftrightarrow\quad x = 1.
\]
We verify $x = 1$ is in the stated domain ($0 < |1| < \sqrt{2}$): ✓. Both arguments are then $2/3 \in [-1, 1]$: ✓.

Therefore $x = 1$ is the unique solution. $\blacksquare$

**Key lesson.** The substitution here is *double Form-I algebraic*: each series is recognised as a geometric series and substituted by its closed-form sum, converting the transcendental-looking identity into a rational equation in $x$. The inverse-trig identity $\sin^{-1} t + \cos^{-1} t = \pi/2$ then forces equality of the two rational expressions, which solves to $x = 1$. The two substitutions in sequence — series-to-sum, then identity-to-equation — show how compound substitutions extract structure efficiently.

### Solution to 5.4 — Trigonometric Substitution for $\sqrt{1 - x^2}$

Apply $x = \sin\theta$, $dx = \cos\theta\,d\theta$. The integrand becomes $\sqrt{1 - \sin^2\theta} = |\cos\theta| = \cos\theta$ (since $\theta \in [0, \pi/2]$, where cosine is non-negative). The limits transform: $x = 0 \Rightarrow \theta = 0$, $x = 1 \Rightarrow \theta = \pi/2$. The integral becomes
\[
  \int_0^1 \sqrt{1 - x^2}\,dx \;=\; \int_0^{\pi/2} \cos\theta \cdot \cos\theta\,d\theta \;=\; \int_0^{\pi/2} \cos^2\theta\,d\theta.
\]
Apply the power-reduction identity $\cos^2\theta = (1 + \cos 2\theta)/2$:
\[
  \;=\; \frac{1}{2}\int_0^{\pi/2} d\theta + \frac{1}{2}\int_0^{\pi/2} \cos 2\theta\,d\theta \;=\; \frac{1}{2} \cdot \frac{\pi}{2} + \frac{1}{4}\big[\sin 2\theta\big]_0^{\pi/2} \;=\; \frac{\pi}{4} + 0 \;=\; \frac{\pi}{4}.
\]
*Geometric interpretation.* The integral $\int_0^1 \sqrt{1 - x^2}\,dx$ is the area under the curve $y = \sqrt{1 - x^2}$ from $x = 0$ to $x = 1$, which is the area of a quarter of the unit disc — namely, $\pi/4$. The trigonometric substitution makes this geometric content manifest: the parametrisation $(x, y) = (\sin\theta, \cos\theta)$ is the parametrisation of the unit quarter-circle, and the integral $\int_0^{\pi/2} \cos^2\theta\,d\theta = \pi/4$ is the area in the angular parameter. The substitution converts a calculus computation into a piece of circle geometry. $\blacksquare$

**Key lesson.** The substitution $x = \sin\theta$ is *Form-II trigonometric*: it converts the algebraic radical $\sqrt{1 - x^2}$ into the clean expression $\cos\theta$. The price is that the differential picks up a factor $\cos\theta\,d\theta$, but the trade is favourable because $\cos\theta$ is a polynomial-like object in trigonometric arguments, where the original $\sqrt{1 - x^2}$ was a radical. The geometric interpretation — the integrand is a quarter-circle area — is the reason the substitution is natural: $x = \sin\theta$ is the parametrisation of a circle, and our integrand was implicitly a piece of circle geometry from the start.

### Solution to 5.5 — Bernoulli ODE via Power Substitution

The equation $dy/dx + y = x y^3$ is *Bernoulli* with $n = 3$. The canonical substitution is $v = y^{1 - n} = y^{-2}$. Differentiating, $dv/dx = -2 y^{-3}\,dy/dx$, so $dy/dx = -(1/2) y^3\,dv/dx$.

Divide the original ODE by $y^3$:
\[
  y^{-3} \frac{dy}{dx} + y^{-2} \;=\; x.
\]
Substitute: $y^{-3}\,dy/dx = -(1/2)\,dv/dx$ and $y^{-2} = v$, so
\[
  -\tfrac{1}{2}\frac{dv}{dx} + v \;=\; x \quad\Longleftrightarrow\quad \frac{dv}{dx} - 2v \;=\; -2x.
\]
This is a *linear* first-order ODE in $v$. The integrating factor is $\mu(x) = e^{-2x}$, and
\[
  \frac{d}{dx}\big[v \, e^{-2x}\big] \;=\; -2x \, e^{-2x}.
\]
Integrate the right side by parts: let $u = -2x$, $dw = e^{-2x}\,dx$, so $du = -2\,dx$ and $w = -(1/2) e^{-2x}$. Then
\[
  \int -2x \, e^{-2x}\,dx \;=\; -2x \cdot \big(-\tfrac{1}{2}\big) e^{-2x} - \int (-2)\big(-\tfrac{1}{2}\big) e^{-2x}\,dx \;=\; x e^{-2x} - \int e^{-2x}\,dx \;=\; x e^{-2x} + \tfrac{1}{2} e^{-2x} + C.
\]
So $v \, e^{-2x} = x e^{-2x} + (1/2) e^{-2x} + C$, i.e.,
\[
  v \;=\; x + \tfrac{1}{2} + C \, e^{2x}.
\]
Transporting back: $v = y^{-2}$, so $y^{-2} = x + 1/2 + C e^{2x}$, hence
\[
  y \;=\; \Big(x + \tfrac{1}{2} + C e^{2x}\Big)^{-1/2}.
\]
$\blacksquare$

**Key lesson.** The substitution $v = y^{1 - n}$ for the Bernoulli ODE $y' + P(x) y = Q(x) y^n$ is *Form-IV differential*: it linearises a nonlinear ODE. The transport-back step (solving for $y$ from $v$) is essential — the answer must be in the original variable. Bernoulli is the prototype "nonlinear-to-linear" substitution; analogous substitutions exist for Riccati equations ($y' = a(x) + b(x) y + c(x) y^2$ reduces to a linear second-order via $y = -u'/(c(x) u)$), for homogeneous ODEs ($y = vx$), and for several other named classes.

### Solution to 5.6 — Logarithmic Substitution in the Multiplicative Cauchy Equation

We are given a continuous $f : (0, \infty) \to \mathbb{R}$ satisfying $f(xy) = f(x) + f(y)$ for all $x, y > 0$.

Apply the substitution $x = e^u$, $y = e^v$, and define $g : \mathbb{R} \to \mathbb{R}$ by $g(u) = f(e^u)$. Then for any $u, v \in \mathbb{R}$,
\[
  g(u + v) \;=\; f(e^{u + v}) \;=\; f(e^u e^v) \;=\; f(e^u) + f(e^v) \;=\; g(u) + g(v).
\]
So $g$ satisfies the *Cauchy additive functional equation* $g(u + v) = g(u) + g(v)$. Moreover, $g$ is continuous (as the composition of continuous functions $f$ and $e^{(\cdot)}$).

It is a classical theorem that the only continuous solutions to the Cauchy additive equation $g(u + v) = g(u) + g(v)$ on $\mathbb{R}$ are the *linear* functions $g(u) = c u$ for some constant $c \in \mathbb{R}$. (The proof: from $g(0 + 0) = g(0) + g(0)$, $g(0) = 0$. By induction, $g(n u) = n g(u)$ for all positive integers $n$. By symmetry and the additive identity, $g(-u) = -g(u)$, so $g(n u) = n g(u)$ for all integers $n$. Setting $u = 1/n$ for positive $n$, $g(1) = n g(1/n)$, so $g(1/n) = g(1)/n$. Combining, $g(q) = q g(1)$ for all rationals $q$. By continuity of $g$ and the density of $\mathbb{Q}$ in $\mathbb{R}$, $g(u) = u g(1)$ for all real $u$. So $g$ is linear with $c = g(1)$.)

Transporting back: $f(x) = f(e^u) = g(u) = c u = c \ln x$ for all $x > 0$. The constant $c$ is determined by, e.g., $c = f(e)$. $\blacksquare$

**Key lesson.** The substitution $u = \ln x$ is *Form-IV* (a change of variables in the functional equation) and *Form-III* (a geometric change from the multiplicative group $(\mathbb{R}_{> 0}, \cdot)$ to the additive group $(\mathbb{R}, +)$, of which $\ln$ is the canonical isomorphism). It converts a *multiplicative* structure into an *additive* one, exposing the underlying Cauchy equation. The continuity hypothesis is essential: without it, the Cauchy additive equation admits highly pathological solutions (Hamel-basis constructions over $\mathbb{R}$ as a $\mathbb{Q}$-vector space). The substitution + continuity together force the linear solution.

### Solution to 5.7 — Vector Substitution in a Linear System

Given non-coplanar vectors $\vec a, \vec b, \vec c \in \mathbb{R}^3$ and the equation
\[
  x \vec a + y \vec b + z \vec c \;=\; \vec a + 2 \vec b - 3 \vec c.
\]
*Non-coplanarity* of three vectors in $\mathbb{R}^3$ is equivalent to *linear independence*, which is equivalent to forming a *basis* of $\mathbb{R}^3$. In any basis, the expansion of a vector is *unique*: if $\sum \alpha_i \vec v_i = \sum \beta_i \vec v_i$ then $\alpha_i = \beta_i$ for all $i$.

Applying uniqueness to our equation:
\[
  x \;=\; 1, \qquad y \;=\; 2, \qquad z \;=\; -3.
\]
$\blacksquare$

**Key lesson.** The "substitution" here is implicit: we are *substituting* into the basis-expansion identity, comparing coefficients in the basis $\{\vec a, \vec b, \vec c\}$. This is *Form-I algebraic substitution* in its most general categorical form — comparison of expansions in a chosen basis. Non-coplanarity is the geometric statement that $\{\vec a, \vec b, \vec c\}$ is a basis; uniqueness of expansion in a basis is the algebraic consequence. The problem is one-line because the substitution is invisible — the basis choice has been made for us by the problem's hypothesis.

This closes the chapter's practice slate and the chapter itself.

> *Substitution, at its deepest, is the recognition that mathematical structures are coordinate-free, and that the practitioner's task is to choose the coordinates in which the structure is computable.*

---

🌑

*End of Chapter 5 — Substitution / Change of Variables. Next: Chapter 6 — Linearization.*
