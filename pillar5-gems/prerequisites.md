---
pillar: 5
part: I
title: "Foundations — The Prerequisites"
subtitle: "Everything Class 10 Did Not Yet Give You, Refreshed in One Sitting"
tier: Foundation
blocks: 17
indexing: PR01–PR17
voice: "Sawyer / Joshi (warm, 'you already know this') with house-voice opener"
status: locked
last_revised: 2026-05-29
locked_on: 2026-05-29
lock_note: "Content, structure, and prose locked by Anand."
---

# Pillar 5, Part I — Foundations

## *Everything Between Class 10 and the Five Pillars, Refreshed in One Sitting*

---

## Why this part exists

I made a promise in the introduction to this book: that a student who has finished Class 10 — nothing more — can pick up the Advaitian framework and climb all the way to the olympiad. This part is where I keep that promise.

What follows is not a syllabus and not a textbook. It is a **refresher** — a compact reactivation of the seventeen blocks of mathematics, drawn from the Class 11 and Class 12 NCERT / JEE curriculum, that the rest of this book quietly assumes you can already use. You met all of it in school. Here we wake it up, name the few facts that matter for *problem-solving* (as opposed to examination), and point each one forward to the gems it will later unlock.

Read this part the way you would stretch before a run. If a block feels obvious, pass the **fluency check** at its foot and move on in thirty seconds. If a check makes you hesitate, that block is exactly where your preparation has a gap — close it now, before the gems in Part II ask you to stand on it.

> **The depth ladder of this pillar.** *Foundation* (this part, PR01–PR17) → *Core* (the JEE-Advanced gems of Part II) → *Stretch* (the INMO/IMO gems of Part II). Each rung stands on the one below. Nothing here is optional; everything here is fast.

**How to read a block.** Each block opens with two or three sentences of orientation, lists the handful of facts that earn their place, and closes with a *fluency check* — a few prompts that take under two minutes. Pass the check and you are ready for the gems that build on the block. Inline pointers such as *(→ Gem D08)* tell you where in Part II the foundation gets used.

---

## PR01 · Sets, Relations & Functions
*Foundation · Class 11 NCERT, Ch. 1–2*

Every later structure — a sequence, a transformation, a symmetry group — is ultimately a *function* between *sets*. This is the vocabulary the whole book speaks; we reactivate it precisely so that words like *onto*, *invertible*, and *well-defined* never slow you down.

- **Sets & operations.** Union $A\cup B$, intersection $A\cap B$, complement $A^c$, difference $A\setminus B$; De Morgan's laws $(A\cup B)^c=A^c\cap B^c$. Venn diagrams as a thinking tool, not decoration.
- **Relations.** Domain, codomain, range; an *equivalence relation* is reflexive, symmetric, and transitive, and it *partitions* a set into classes. *(→ Gem C-cluster: congruence mod $n$ is the prototype equivalence relation.)*
- **Functions.** *Injective* (one-one), *surjective* (onto), *bijective* (both). A function is invertible iff it is bijective; then $f^{-1}$ exists and $f^{-1}\circ f=\mathrm{id}$.
- **Composition.** $(f\circ g)(x)=f(g(x))$; associative, generally **not** commutative.
- **Standard real functions.** Polynomial, rational, modulus $|x|$, signum, greatest-integer (floor) $\lfloor x\rfloor$.

> **Fluency check.** (a) Is $f(x)=x^2$ from $\mathbb{R}\to\mathbb{R}$ injective? surjective? (b) Why must a function be bijective to have an inverse? (c) Compute $(f\circ g)$ and $(g\circ f)$ for $f(x)=2x$, $g(x)=x+1$ and confirm they differ.

---

## PR02 · Mathematical Induction & Proof Logic
*Foundation · Class 11 NCERT, Ch. 4*

Half of the gems in Part II are *proved* by induction or by contradiction. You do not need to invent these methods — you need them so automatic that you recognise, mid-problem, "this is an induction" or "assume the opposite."

- **Induction.** Base case + inductive step ($P(k)\Rightarrow P(k+1)$). *Strong* induction assumes $P(j)$ for all $j<n$ — essential when the step reaches back more than one rung.
- **Contradiction.** Assume the negation, derive an impossibility. The engine behind irrationality proofs and many existence arguments.
- **Logic vocabulary.** Converse, inverse, contrapositive (a statement and its contrapositive are equivalent); proving "if and only if" means proving *both* directions.

> **Fluency check.** (a) Prove $1+2+\cdots+n=\tfrac{n(n+1)}{2}$ by induction. (b) State the contrapositive of "if $n^2$ is even then $n$ is even." (c) When is strong induction necessary rather than ordinary induction?

---

## PR03 · Complex Numbers
*Foundation · Class 11 NCERT, Ch. 5*

You first met these as "numbers where $i^2=-1$." For this book their power is **geometric**: a complex number is a point you can rotate and scale by multiplying. This single idea later becomes one of the sharpest tools in the geometry cluster.

- **Algebra & conjugate.** $z=a+bi$; $\bar z=a-bi$; $|z|^2=z\bar z=a^2+b^2$. Divide by multiplying numerator and denominator by the conjugate.
- **Argand plane.** $z$ is a point/vector; addition is vector addition; $|z_1-z_2|$ is the distance between two points. *(→ Gem D08: Complex Numbers as Geometry.)*
- **Polar form.** $z=r(\cos\theta+i\sin\theta)$, $r=|z|$, $\theta=\arg z$; **multiplication adds angles and multiplies moduli**.
- **Roots of unity.** $z^n=1\Rightarrow z=e^{2\pi i k/n}$, $k=0,\dots,n-1$; they sit equally spaced on the unit circle and **sum to zero**. *(→ Gem A15: Cyclotomic Factorisation.)*
- **Quadratics over $\mathbb{C}$.** Discriminant $\Delta=b^2-4ac$; complex-conjugate roots when $\Delta<0$.

> **Fluency check.** (a) Compute $\dfrac{1+i}{1-i}$. (b) Describe the locus $|z-2|=3$ geometrically. (c) Write the three cube roots of unity and verify their sum is $0$.

---

## PR04 · Trigonometric Functions
*Foundation · Class 11 NCERT, Ch. 3*

Trigonometry is the language of periodicity and of triangles, and it reappears in calculus, geometry, and complex numbers. We keep only the identities you must wield *without looking up*.

- **Radian measure.** Arc length $s=r\theta$; convert degrees $\leftrightarrow$ radians.
- **Unit-circle definitions** of $\sin,\cos,\tan$ (and $\sec,\csc,\cot$); the sign of each in every quadrant.
- **Pythagorean identities.** $\sin^2\theta+\cos^2\theta=1$; $1+\tan^2\theta=\sec^2\theta$; $1+\cot^2\theta=\csc^2\theta$. *(→ Gem A09, the invariant of Chapter 1.)*
- **Addition formulas.** $\sin(A\pm B)$, $\cos(A\pm B)$, $\tan(A\pm B)$. *(→ Gems D07c, D07d.)*
- **Double / half angle.** $\sin 2A=2\sin A\cos A$; $\cos 2A=1-2\sin^2A$; $\sin^2\tfrac{A}{2}=\tfrac{1-\cos A}{2}$.
- **General solutions** of $\sin\theta=k$, $\cos\theta=k$, $\tan\theta=k$.

> **Fluency check.** (a) Derive $\cos 2A=1-2\sin^2 A$ from the addition formula. (b) Solve $\sin\theta=\tfrac12$ for all $\theta$. (c) Without a calculator, evaluate $\tan 75^\circ$ using the addition formula.

---

## PR05 · Linear Inequalities & Algebraic Foundations
*Foundation · Class 11 NCERT, Ch. 6*

Inequalities are an entire cluster of gems (Part II, Cluster B). Before those, you must be utterly comfortable manipulating inequalities and the absolute value — including the one rule beginners forget.

- **Solving inequalities.** One and two variables; **the direction flips when multiplying or dividing by a negative**; graphical regions in the plane.
- **Absolute value.** $|x|=x$ if $x\ge 0$, else $-x$; $|x-a|$ is the distance from $a$; the triangle inequality $|a+b|\le|a|+|b|$. *(→ Gem B06.)*
- **Intervals.** Open, closed, half-open; bounded vs. unbounded.
- **Polynomial algebra.** Degree, leading term, factorisation, the idea of a rational root. *(→ Gems A07a, A16.)*

> **Fluency check.** (a) Solve $|x-3|<5$. (b) Solve $-2x+1>7$ and state where you flipped the sign. (c) Sketch the region $x+y\le 4$, $x\ge 0$, $y\ge 0$.

---

## PR06 · Permutations, Combinations & Basic Probability
*Foundation · Class 11 NCERT, Ch. 7 & 14*

Counting is a pillar-wide skill and the whole of Cluster G. Master the two counting principles and the difference between *order matters* and *order does not* before anything fancier.

- **Counting principles.** Multiplication rule (AND), addition rule (OR).
- **Permutations.** $P(n,r)=\dfrac{n!}{(n-r)!}$; circular arrangements $(n-1)!$; arrangements with repetition.
- **Combinations.** $C(n,r)=\dfrac{n!}{r!(n-r)!}$; Pascal's identity $C(n,r)+C(n,r-1)=C(n+1,r)$. *(→ Gems A05, A12.)*
- **Classical probability.** $P(A)=\dfrac{\text{favourable}}{\text{total}}$; complement $P(A^c)=1-P(A)$; addition rule $P(A\cup B)=P(A)+P(B)-P(A\cap B)$. *(→ Gem G02.)*

> **Fluency check.** (a) In how many ways can $5$ people sit around a round table? (b) How many $4$-letter words use distinct letters from $\{a,\dots,h\}$? (c) State Pascal's identity and explain it by a counting argument.

---

## PR07 · Binomial Theorem & Sequences
*Foundation · Class 11 NCERT, Ch. 8–9*

The binomial theorem and the two classical progressions are the seeds of Cluster E (Sequences & Series) and recur in algebra and number theory.

- **Binomial theorem.** $(a+b)^n=\sum_{k=0}^{n}C(n,k)a^{n-k}b^k$; general term $T_{k+1}=C(n,k)a^{n-k}b^k$. *(→ Gem A05.)*
- **Arithmetic progression.** $a_n=a+(n-1)d$; $S_n=\tfrac{n}{2}\big(2a+(n-1)d\big)$.
- **Geometric progression.** $a_n=ar^{n-1}$; $S_n=\dfrac{a(r^n-1)}{r-1}$; $S_\infty=\dfrac{a}{1-r}$ for $|r|<1$.
- **Standard sums.** $\sum k=\tfrac{n(n+1)}{2}$, $\sum k^2=\tfrac{n(n+1)(2n+1)}{6}$, $\sum k^3=\big(\tfrac{n(n+1)}{2}\big)^2$. *(→ Gem E01.)*
- **AGP** and the **method of differences**.

> **Fluency check.** (a) Find the term independent of $x$ in $\big(x+\tfrac1x\big)^6$. (b) Sum $2+5+8+\cdots$ to $n$ terms. (c) Evaluate $\sum_{k=1}^{n}k^2$ from memory.

---

## PR08 · Coordinate Geometry: Lines & Conics
*Foundation · Class 11 NCERT, Ch. 10–11*

Coordinate geometry turns geometry into algebra — the *domain translation* archetype in action. The conics return throughout Cluster D, often in their parametric disguise.

- **Straight lines.** Slope $m=\tfrac{y_2-y_1}{x_2-x_1}$; distance and section/midpoint formulas; forms (slope-intercept, point-slope, two-point, intercept, general $ax+by+c=0$); parallel $m_1=m_2$, perpendicular $m_1m_2=-1$.
- **Circle.** $(x-h)^2+(y-k)^2=r^2$; general $x^2+y^2+2gx+2fy+c=0$. *(→ Gems D01, D11.)*
- **Parabola.** $y^2=4ax$; focus $(a,0)$, directrix $x=-a$; parametric $(at^2,2at)$. *(→ Gem D20.)*
- **Ellipse.** $\tfrac{x^2}{a^2}+\tfrac{y^2}{b^2}=1$; foci $(\pm ae,0)$; $b^2=a^2(1-e^2)$, $e<1$.
- **Hyperbola.** $\tfrac{x^2}{a^2}-\tfrac{y^2}{b^2}=1$; $e>1$; asymptotes $y=\pm\tfrac{b}{a}x$.

> **Fluency check.** (a) Equation of the line through $(1,2)$ perpendicular to $y=3x$. (b) Centre and radius of $x^2+y^2-4x+6y-3=0$. (c) For $y^2=8x$, give the focus and directrix.

---

## PR09 · Introduction to 3D Geometry
*Foundation · Class 11 NCERT, Ch. 12 / Class 12, Ch. 11*

Three dimensions add one coordinate and the language of *direction*. This block pairs with vector algebra (PR16) and supports spatial reasoning in several gems.

- **Coordinates in space.** Distance and section formulas in $\mathbb{R}^3$.
- **Direction cosines / ratios.** $l^2+m^2+n^2=1$; ratios $a:b:c$.
- **Line in space.** $\dfrac{x-x_0}{a}=\dfrac{y-y_0}{b}=\dfrac{z-z_0}{c}=t$.
- **Plane.** $ax+by+cz+d=0$; normal vector $(a,b,c)$; distance from a point to a plane.
- **Angles.** Between two lines; line and plane; two planes.

> **Fluency check.** (a) Distance between $(1,0,2)$ and $(4,4,2)$. (b) Direction cosines of the line with ratios $2:3:6$. (c) Distance from the origin to $2x-y+2z=6$.

---

## PR10 · Matrices & Determinants
*Foundation · Class 12 NCERT, Ch. 3–4*

Matrices are how linear structure is stored and manipulated; the determinant is the single most important *invariant* attached to a square matrix — the opening example of Chapter 1.

- **Matrices.** Order; types (square, diagonal, identity, symmetric, skew-symmetric); addition, scalar multiple, product; $(AB)^T=B^TA^T$; multiplication is **not** commutative.
- **Determinant.** $2\times2$ and $3\times3$ by cofactor expansion; row-operation properties; $\det(AB)=\det A\det B$. *(→ Chapter 1, Invariance.)*
- **Geometry.** Area of a triangle and the collinearity condition via a determinant.
- **Inverse.** $A^{-1}=\dfrac{\operatorname{adj}A}{\det A}$; singular ($\det=0$) vs. non-singular.
- **Linear systems.** Solving $A\mathbf{x}=\mathbf{b}$ via $A^{-1}$ or Cramer's rule.

> **Fluency check.** (a) Compute $\det\begin{psmallmatrix}1&2\\3&4\end{psmallmatrix}$. (b) Why does $\det(AB)=\det A\det B$ make the determinant a *multiplicative invariant*? (c) When does $A\mathbf{x}=\mathbf{b}$ fail to have a unique solution?

---

## PR11 · Calculus I — Limits, Continuity & Differentiability
*Foundation · Class 12 NCERT, Ch. 5*

Calculus is Cluster F, and it begins here. The conceptual core is the *limit*; the derivative and everything after it are built on it.

- **Limit.** $\lim_{x\to a}f(x)=L$; left- and right-hand limits; a limit exists iff they agree.
- **Standard limits.** $\lim_{x\to0}\tfrac{\sin x}{x}=1$; $\lim_{x\to0}\tfrac{e^x-1}{x}=1$; $\lim_{x\to0}(1+x)^{1/x}=e$.
- **Continuity.** $\lim_{x\to a}f(x)=f(a)$; removable, jump, infinite discontinuities.
- **Differentiability.** $f'(x)=\lim_{h\to0}\tfrac{f(x+h)-f(x)}{h}$; differentiable $\Rightarrow$ continuous (not the converse). *(→ Gems F01, F02.)*
- **Rules & standard derivatives.** Sum, product, quotient, chain; $x^n,\sin x,\cos x,\tan x,e^x,\ln x,\arcsin x,\arctan x$.

> **Fluency check.** (a) Evaluate $\lim_{x\to0}\tfrac{\sin 3x}{x}$. (b) Give a function that is continuous but not differentiable at a point. (c) Differentiate $x^2\sin x$ by the product rule.

---

## PR12 · Inverse Trigonometric Functions
*Foundation · Class 12 NCERT, Ch. 2*

A small but sharp block: the inverse trig functions, their principal branches, and the few identities that crack telescoping and substitution problems later.

- **Principal branches.** $\arcsin:[-\tfrac\pi2,\tfrac\pi2]$; $\arccos:[0,\pi]$; $\arctan:(-\tfrac\pi2,\tfrac\pi2)$.
- **Key identities.** $\arcsin x+\arccos x=\tfrac\pi2$; $\arctan x+\arctan y=\arctan\tfrac{x+y}{1-xy}$ (for $xy<1$); $\arctan\tfrac1x=\tfrac\pi2-\arctan x$ ($x>0$). *(→ Gem A06, telescoping $\cot^{-1}$ sums.)*
- **Derivatives.** $\dfrac{d}{dx}\arcsin x=\dfrac{1}{\sqrt{1-x^2}}$; $\dfrac{d}{dx}\arctan x=\dfrac{1}{1+x^2}$.

> **Fluency check.** (a) Evaluate $\arctan 1+\arctan 2+\arctan 3$. (b) Why is the range of $\arcsin$ restricted? (c) State $\tfrac{d}{dx}\arctan x$.

---

## PR13 · Calculus II — Applications of Derivatives
*Foundation · Class 12 NCERT, Ch. 6*

The derivative as a tool: tangents, monotonicity, and optimisation. This block feeds directly into the *extremal* archetype and Gem F12.

- **Tangent & normal.** From $f'(x_0)$ at a point on a curve.
- **Monotonicity.** $f'>0\Rightarrow$ increasing; $f'<0\Rightarrow$ decreasing.
- **Extrema.** First-derivative test; second-derivative test ($f''(x_0)<0\Rightarrow$ local max).
- **Global extrema** on $[a,b]$: check critical points *and* endpoints.
- **Mean-value results.** Rolle and MVT at the applied level. *(→ Gem F01.)*

> **Fluency check.** (a) Find the local extrema of $f(x)=x^3-3x$. (b) On $[0,2]$, where is $f(x)=x^3-3x$ maximised? (c) State the second-derivative test.

---

## PR14 · Calculus III — Integrals
*Foundation · Class 12 NCERT, Ch. 7–8*

Integration reverses differentiation and measures accumulation. The techniques here become Gems F04a–F04c; the definite-integral symmetries underlie elegant JEE pivots.

- **Antiderivatives.** $\int x^n\,dx$, $\int\sin x\,dx$, $\int e^x\,dx$, $\int\tfrac1x\,dx$; the constant of integration.
- **Substitution.** $t=g(x)$ (reverse chain rule). *(→ Gem F04a.)*
- **By parts.** $\int u\,dv=uv-\int v\,du$ (ILATE). *(→ Gem F04b.)*
- **Definite integral & FTC.** $\int_a^b f=F(b)-F(a)$; properties $\int_a^b f=-\int_b^a f$, $\int_a^a f=0$, linearity.
- **Area** under and between curves.
- **King's property.** $\int_0^a f(x)\,dx=\int_0^a f(a-x)\,dx$ — a recurring elegant pivot.

> **Fluency check.** (a) Evaluate $\int_0^1 x e^x\,dx$ by parts. (b) Use the King's property on $\int_0^{\pi/2}\tfrac{\sin x}{\sin x+\cos x}dx$. (c) State the Fundamental Theorem of Calculus.

---

## PR15 · Differential Equations
*Foundation · Class 12 NCERT, Ch. 9*

A differential equation describes a quantity through its rate of change. The three solvable forms here become Gem F11 and appear wherever a process is modelled.

- **Order & degree** of a DE.
- **Formation.** Eliminate arbitrary constants from a family of curves.
- **Separable.** $\dfrac{dy}{dx}=f(x)g(y)\Rightarrow\int\tfrac{dy}{g(y)}=\int f(x)\,dx$.
- **Linear first-order.** $\dfrac{dy}{dx}+P(x)y=Q(x)$; integrating factor $\mu=e^{\int P\,dx}$.
- **Homogeneous.** $\dfrac{dy}{dx}=F(y/x)$; substitute $y=vx$.
- **Geometric meaning.** Slope field; solution as a family of curves. *(→ Gem F11.)*

> **Fluency check.** (a) Solve $\dfrac{dy}{dx}=xy$. (b) Identify the integrating factor for $y'+2y=e^x$. (c) State the order and degree of $\big(y''\big)^2+y=0$.

---

## PR16 · Vector Algebra
*Foundation · Class 12 NCERT, Ch. 10*

Vectors unify direction and magnitude and give geometry an algebra of its own. The dot, cross, and triple products are quietly used across the geometry and physics connections of every pillar.

- **Vectors.** Magnitude, direction, position vectors; addition (parallelogram law), scalar multiple; unit vector $\hat{a}=\tfrac{\mathbf a}{|\mathbf a|}$.
- **Dot product.** $\mathbf a\cdot\mathbf b=|\mathbf a||\mathbf b|\cos\theta=\sum a_ib_i$; projection of $\mathbf a$ on $\mathbf b$.
- **Cross product.** $|\mathbf a\times\mathbf b|=|\mathbf a||\mathbf b|\sin\theta$; right-hand rule; area of a parallelogram.
- **Scalar triple product.** $[\mathbf a,\mathbf b,\mathbf c]=\mathbf a\cdot(\mathbf b\times\mathbf c)=\det[\mathbf a\;\mathbf b\;\mathbf c]$; volume of a parallelepiped; coplanarity $\Leftrightarrow$ triple product $=0$.

> **Fluency check.** (a) Angle between $(1,0,0)$ and $(1,1,0)$. (b) Area of the parallelogram on $(1,2,0)$ and $(0,1,1)$. (c) Are $(1,0,0),(0,1,0),(1,1,0)$ coplanar?

---

## PR17 · Statistics & Probability II
*Foundation · Class 12 NCERT, Ch. 13 (+ Class 11, Ch. 15)*

The probabilistic foundation that supports Gems G04 (linearity of expectation) and G16 (the probabilistic method), and that every quantitative discipline relies on.

- **Descriptive statistics.** Mean, variance, standard deviation (grouped and ungrouped).
- **Conditional probability.** $P(A\mid B)=\dfrac{P(A\cap B)}{P(B)}$; multiplication rule.
- **Independence.** $P(A\cap B)=P(A)P(B)$.
- **Bayes' theorem.** $P(A_i\mid B)=\dfrac{P(B\mid A_i)P(A_i)}{\sum_j P(B\mid A_j)P(A_j)}$.
- **Random variables.** Distribution table; $E[X]=\sum xP(X=x)$; $\operatorname{Var}(X)=E[X^2]-(E[X])^2$. *(→ Gem G04.)*
- **Binomial distribution.** $P(X=k)=C(n,k)p^k(1-p)^{n-k}$; $E[X]=np$, $\operatorname{Var}(X)=np(1-p)$.

> **Fluency check.** (a) Two fair dice: $P(\text{sum}=7)$? (b) State Bayes' theorem and explain the denominator. (c) For $B(n,p)$, why is $E[X]=np$ immediate from linearity of expectation?

---

## You are ready

If you passed the seventeen fluency checks, you hold every prerequisite the rest of this book assumes. The floor is now level. From here the ground rises: Part II turns these foundations into **gems** — named tools that implement the elegant pivots of Pillars 2 through 4 — and labels each one *Core* (JEE Advanced) or *Stretch* (INMO/IMO) so you always know how far you are reaching.

Turn the page. The climb begins.

🌑
