---
pillar: 5
part: II
title: "The Gems — Operational Toolkit"
subtitle: "115 Named Tools That Execute the Pivots of Pillars 2–4"
clusters: 7
gem_count: 115
tiers: [Core, Stretch]
indexing: "cluster-letter + 2-digit number (e.g. A01, G17)"
voice: "Tao / Engel (spare, named, sourced); one Zeitz line of motivation per Stretch gem"
crossrefs: "provisional — verification deferred to a dedicated later pass (sole carve-out from lock)"
status: locked
last_revised: 2026-05-29
locked_on: 2026-05-29
lock_note: "Content, structure, and prose locked by Anand. Sole open carve-out: Pillar 2–4 cross-references remain provisional pending a dedicated verification pass (does not block lock)."
---

# Pillar 5, Part II — The Gems

## *The Operational Toolkit: 115 Named Tools That Execute the Pivots*

---

## What the gems are

The archetypes of Pillar 2 tell you *what a problem is*. The multidirectional method of Pillar 3 tells you *which way to enter it*. The design lens of Pillar 4 tells you *how a problem was built*. None of that moves a single symbol on the page. The **gems** are what move the symbols.

A gem is a named, reusable mathematical tool — an identity, an inequality, a theorem, a technique — that *implements* an elegant pivot, the third move of Pillar 1's *Seed → Brute Path → Elegant Pivot* grammar. When a solver recognises that a problem has a fixed sum and a product to bound, the recognition is the archetype (Invariance, Extremal); the execution is a gem (AM–GM). This pillar is the catalogue of those executions, organised so you can both **look a gem up** in seconds and **read a cluster through** as a refresher.

This is deliberately not an appendix of formulae. Every entry foregrounds *the move the gem makes* and *the signal that tells you to reach for it* — because a formula you cannot trigger on is dead weight, and a formula whose purpose you understand is a reflex.

---

## How to read an entry

Each gem is laid out in the same eight fields. Read the first three to *use* the gem; read all eight to *understand* it.

- **Statement** *(boxed)* — the exact mathematical claim. This is the lookup layer.
- **What it says** — the statement in one plain-English sentence.
- **The move** — the pivot this gem performs: what it turns into what. *This is the heart of the entry.*
- **When it fires** — the recognition signal, with a quotable **trigger** phrase. Read this and you will know, mid-problem, to reach for the gem.
- **Micro-example** — one or two lines showing the gem in flight. Not a full worked solution (those live in Pillars 2–4); just enough to see the mechanism.
- **Watch for** — the one or two ways students misapply it.
- **Used in / Neighbours** — where the gem fires in the rest of the book *(cross-references are provisional pending a verification pass against the locked chapters)*, and the adjacent gems it connects to.
- **Named proof** — a one-line pointer to a standard proof or source, for the reader who wants to see *why* the gem is true.

### The tier key

Every gem carries one of two badges, so you always know how far you are reaching:

- **Core** — a tool the **JEE Advanced** aspirant is expected to apply independently. Taught in Class 11–12, appears in JEE papers. These are the primary content of this pillar.
- **Stretch** — a tool the **INMO / IMO**-targeting student needs, but which lies outside the standard JEE syllabus. Clearly labelled so a JEE-only reader can skip them without losing the framework.

> Below the gems sits a third tier — **Foundation** — the seventeen prerequisite blocks of Part I. The full ladder is *Foundation → Core → Stretch*. If a gem leans on a foundation, its entry says so.

**Indexing.** Each gem has a permanent address: cluster letter + two digits (e.g. **A01**, **G17**). Pillars 2–4 cite gems by this address. Numbering is fixed and never re-issued.

---

# Cluster A — Algebraic Identities & Techniques

*The algebra of polynomials, symmetric expressions, and named factorisations. These gems convert structure that is hidden in an expression into structure you can read off — the workhorses behind the* Hidden Structure *and* Reverse Engineering *archetypes.*

---

### A01 · Vieta's Formulas — Core

> For $a_nx^n+\cdots+a_0$ with roots $r_1,\dots,r_n$: $\;\sum r_i=-\dfrac{a_{n-1}}{a_n}$, $\;\sum_{i<j}r_ir_j=\dfrac{a_{n-2}}{a_n}$, $\;\dots,\;\prod r_i=(-1)^n\dfrac{a_0}{a_n}$.

**What it says.** The coefficients of a polynomial *are* the elementary symmetric functions of its roots (up to sign and the leading coefficient).

**The move.** Trade the roots — which you may not be able to find — for the coefficients, which you can always read off. Symmetric information about the roots becomes free.

**When it fires.** You are asked about *symmetric* functions of roots (their sum, product, sum of squares) without needing the roots themselves. *Trigger:* "find $\sum r_i^2$ / the value of an expression symmetric in the roots."

**Micro-example.** Roots of $x^2-5x+6$ satisfy $r_1+r_2=5$, $r_1r_2=6$, so $r_1^2+r_2^2=5^2-2\cdot6=13$ — without solving.

**Watch for.** Forgetting the $a_n$ denominator for non-monic polynomials; sign errors in the alternating pattern.

**Used in.** P2 Ch. 8, 14; P3 Ch. 3 WE1 (IMO 1988); P4 Ch. 1, 3, 8 *(provisional)*. **Neighbours.** → A04 (Newton's identities turn these into power sums); the engine of *Vieta jumping* (P4 Case 25).

**Named proof.** Expand $a_n\prod(x-r_i)$ and match coefficients — elementary; see Lang, *Algebra*.

---

### A02 · Sophie Germain Identity — Core

> $a^4+4b^4=(a^2+2b^2+2ab)(a^2+2b^2-2ab)$.

**What it says.** A sum of a fourth power and four times a fourth power — which *looks* irreducible — factors into two quadratics.

**The move.** Complete the square inside a quartic by adding and subtracting $4a^2b^2$, exposing a difference of two squares.

**When it fires.** An expression of the form "fourth power $+\,4\times$ fourth power," especially when proving a number is composite. *Trigger:* "show $n^4+4$ (or $n^4+4^n$) is not prime."

**Micro-example.** $n^4+4=(n^2+2n+2)(n^2-2n+2)$, composite for every $n\ge 2$.

**Watch for.** Misremembering the cross term (it is $2ab$, giving $+4b^4$, not $b^4$); applying it when the coefficient is not exactly $4$.

**Used in.** P4 Case 2 (IMO 1969 P1) *(provisional)*. **Neighbours.** → A03 (both are difference-of-squares in disguise).

**Named proof.** Add and subtract $4a^2b^2$ to complete the square — Engel, *Problem-Solving Strategies*, Ch. 2.

---

### A03 · Factorisation of Power Differences & Sums — Core

> $a^2-b^2=(a-b)(a+b)$; $\;a^3\pm b^3=(a\pm b)(a^2\mp ab+b^2)$; $\;a^n-b^n=(a-b)\sum_{k=0}^{n-1}a^{n-1-k}b^k$.

**What it says.** Differences (and odd sums) of like powers always carry the factor $a-b$ (resp. $a+b$).

**The move.** Expose a guaranteed divisor of an expression, turning an additive form into a product you can reason about — divisibility, roots, telescoping.

**When it fires.** Divisibility claims about $a^n-b^n$; spotting that $a=b$ forces the expression to vanish. *Trigger:* "show $a-b \mid a^n-b^n$" or "factor this symmetric difference."

**Micro-example.** $2^n-1$ is divisible by $3$ whenever $n$ is even, since $2^2-1=3 \mid 2^{2k}-1$.

**Watch for.** $a^n+b^n$ factors over the reals only for *odd* $n$; the sign pattern in the long sum.

**Used in.** P2 Ch. 9 WE3; standard P4 number-theory factorisation *(provisional)*. **Neighbours.** → A02, A15 (cyclotomic refinement), C04 (LTE quantifies the power of each prime divisor).

**Named proof.** Direct verification of the geometric-series factor $\sum_k a^{n-1-k}b^k$ — standard.

---

### A04 · Newton's Identities (Power Sums) — Core

> With $p_k=\sum x_i^k$ and $e_k$ the elementary symmetric polynomials: $\;p_k-e_1p_{k-1}+\cdots+(-1)^{k-1}e_{k-1}p_1+(-1)^k k\,e_k=0$.

**What it says.** Power sums and elementary symmetric polynomials determine each other recursively.

**The move.** Climb between the two natural descriptions of a set of roots — "sum of $k$-th powers" and "coefficients" — without ever finding the roots.

**When it fires.** You know $\sum r_i$, $\sum r_ir_j$, … (i.e. the coefficients via A01) and need $\sum r_i^k$, or vice versa. *Trigger:* "express $\sum r_i^3$ in terms of the coefficients."

**Micro-example.** $p_1=e_1$; $p_2=e_1p_1-2e_2=e_1^2-2e_2$; $p_3=e_1p_2-e_2p_1+3e_3$.

**Watch for.** The standalone $k\,e_k$ term (easy to drop); the identities assume the $e_k$ beyond the degree are zero.

**Used in.** P2 Ch. 17 (locked slate: "Newton's identities recursively give $e_k$ from $p_k$") *(provisional)*. **Neighbours.** → A01 (supplies the $e_k$), A09 (symmetric-polynomial manipulation).

**Named proof.** Generating-function / induction argument — Macdonald, *Symmetric Functions and Hall Polynomials*, §I.2.

---

### A05 · Binomial Theorem — Core

> $(a+b)^n=\displaystyle\sum_{k=0}^{n}\binom{n}{k}a^{n-k}b^k$; for $|x|<1$ and real $\alpha$, $\;(1+x)^\alpha=\sum_{k\ge0}\binom{\alpha}{k}x^k$.

**What it says.** A power of a binomial expands into a weighted sum of monomials, the weights being binomial coefficients.

**The move.** Convert a product-form $(a+b)^n$ into a sum you can extract a single coefficient from — the bridge between algebra and counting.

**When it fires.** "Find the coefficient of $x^r$"; approximations via the generalised form; any identity provable by comparing coefficients. *Trigger:* "term independent of $x$ / coefficient of $x^k$."

**Micro-example.** Coefficient of $x^2$ in $(1+x)^5$ is $\binom{5}{2}=10$.

**Watch for.** Forgetting the general (fractional/negative) form converges only for $|x|<1$; off-by-one in "general term $T_{k+1}$."

**Used in.** P2 Ch. 13, 18; P4 number theory and combinatorics throughout *(provisional)*. **Neighbours.** → A12, A14 (Vandermonde and the multinomial generalisation), G02 (sign-alternating sums).

**Named proof.** Induction on $n$, or the counting argument for $\binom{n}{k}$ — standard.

---

### A06 · Telescoping (Sums & Products) — Core

> $\displaystyle\sum_{k=1}^{n}\big(f(k+1)-f(k)\big)=f(n+1)-f(1)$; multiplicatively $\prod \dfrac{g(k+1)}{g(k)}=\dfrac{g(n+1)}{g(1)}$.

**What it says.** A sum (or product) of consecutive differences (or ratios) collapses to its endpoints.

**The move.** Rewrite a term as a difference $f(k+1)-f(k)$ so that the interior cancels and only the boundary survives — an infinite-looking sum becomes two numbers.

**When it fires.** A sum whose general term splits via partial fractions or a trig/inverse-trig identity. *Trigger:* "evaluate $\sum \frac{1}{k(k+1)}$ / sum of $\cot^{-1}$ terms."

**Micro-example.** $\sum_{k=1}^{n}\frac{1}{k(k+1)}=\sum\big(\frac1k-\frac1{k+1}\big)=1-\frac1{n+1}$.

**Watch for.** Failing to find the right $f$; mishandling the surviving boundary terms.

**Used in.** P2 Ch. 6 WE2, Ch. 18 PP1, Ch. 9 slate PP5 *(provisional)*. **Neighbours.** → A11 (partial fractions reveal the telescope), E09 (Abel summation is its weighted cousin).

**Named proof.** Immediate from cancellation of consecutive terms — elementary.

---

### A07a · Factor Theorem — Core

> $f(a)=0 \iff (x-a)\mid f(x)$.

**What it says.** A number is a root of a polynomial exactly when the corresponding linear term divides it.

**The move.** Convert "is $a$ a root?" into "does $(x-a)$ divide $f$?" — and, once a root is found, peel off a linear factor to reduce the degree.

**When it fires.** Factoring a polynomial after guessing a root; proving a polynomial identity by exhibiting enough roots. *Trigger:* "one obvious root is …, so factor it out."

**Micro-example.** $f(x)=x^3-6x^2+11x-6$ has $f(1)=0$, so $(x-1)\mid f$, giving $f=(x-1)(x-2)(x-3)$.

**Watch for.** Assuming all roots are rational (use A16 to limit candidates); arithmetic in the division step.

**Used in.** P2 Ch. 14, 16; polynomial factorisation in P4 CEP design *(provisional)*. **Neighbours.** → A07b (the remainder it specialises), A16 (which roots to test).

**Named proof.** Corollary of the polynomial division algorithm — standard.

---

### A07b · Polynomial Remainder Theorem — Core

> The remainder of $f(x)\div(x-a)$ is $f(a)$.

**What it says.** Dividing by a linear factor, the leftover is just the polynomial evaluated at the root.

**The move.** Replace long division by a single evaluation — extract divisibility and remainder information for the cost of plugging in a number.

**When it fires.** "Find the remainder when $f(x)$ is divided by $(x-a)$"; checking divisibility without dividing. *Trigger:* "remainder on division by $x-a$."

**Micro-example.** Remainder of $x^{100}$ on division by $(x-1)$ is $1^{100}=1$.

**Watch for.** Only directly applies to linear divisors; for $(x-a)(x-b)$ use the remainder form $px+q$ and two evaluations.

**Used in.** P2 Ch. 14 WE3 (cubic parity argument) *(provisional)*. **Neighbours.** → A07a (its zero-remainder case), A01 (coefficient–root link).

**Named proof.** The division algorithm with a linear divisor $(x-a)$ — standard.

---

### A08 · Lagrange Interpolation Formula — Stretch

> The unique polynomial of degree $\le n-1$ through $(x_i,y_i)$, $i=1..n$, is $\displaystyle P(x)=\sum_{i=1}^{n}y_i\prod_{j\ne i}\frac{x-x_j}{x_i-x_j}$.

**What it says.** $n$ points determine exactly one polynomial of degree below $n$, and here it is, written explicitly.

**The move.** Reconstruct an unknown polynomial *from its values* — invert the usual direction, turning a zero-degrees-of-freedom constraint set into a formula.

**When it fires.** A polynomial is pinned down by its values at several points and you must evaluate it elsewhere. *Trigger:* "$P$ has degree $\le n-1$ and $P(x_i)=y_i$; find $P(\,\cdot\,)$."

**Micro-example.** The degree-$\le1$ polynomial with $P(0)=1,P(1)=3$ is $P(x)=1\cdot\frac{x-1}{0-1}+3\cdot\frac{x-0}{1-0}=1+2x$.

**Watch for.** Costly if you only need one value (finite differences may be faster); requires distinct nodes.

**Used in.** P2 Ch. 17 (degrees of freedom: "Lagrange interpolating polynomial through 4 points") *(provisional)*. **Neighbours.** → A07a, A16 (root structure); E10 (recurrences as an alternative reconstruction).

**Named proof.** Construct from the Lagrange basis polynomials; uniqueness by degree count — standard.

---

### A09 · Symmetric Factorisation Identity — Core

> $x^2(y-z)+y^2(z-x)+z^2(x-y)=(x-y)(y-z)(x-z)$  *(the sign form used in P2 Ch. 9)*.

**What it says.** A cyclic sum that looks like an unmanageable mess is, in fact, a clean product of three differences.

**The move.** Recognise a cyclic/antisymmetric expression and factor it on sight — the difference factors are forced because the expression vanishes whenever two variables coincide.

**When it fires.** A symmetric or cyclic polynomial that vanishes when two variables are equal; simplifying determinants and inequality set-ups. *Trigger:* "this expression is $0$ when $x=y$ — so $(x-y)$ is a factor."

**Micro-example.** Setting $x=y$ makes the left side $0$, so $(x-y)$ divides it; by symmetry so do $(y-z),(z-x)$.

**Watch for.** The overall sign and cyclic orientation; do not lose a factor by stopping at two differences.

**Used in.** P2 Ch. 9 WE3 Pitfalls ("the trained solver should recognise at sight") *(provisional)*. **Neighbours.** → A04 (symmetric-polynomial toolkit), B09 (SOS factorisations).

**Named proof.** Each of $(x-y),(y-z),(x-z)$ divides the LHS (it vanishes when the pair is equal); compare degree and a coefficient — elementary.

---

### A10 · Brahmagupta–Fibonacci Two-Square Identity — Stretch

> $(a^2+b^2)(c^2+d^2)=(ac-bd)^2+(ad+bc)^2$.

**What it says.** A product of two sums-of-two-squares is itself a sum of two squares — in two ways.

**The move.** Show that "expressible as a sum of two squares" is *closed under multiplication*, reducing such questions to the prime factors. It is exactly $|z_1z_2|^2=|z_1|^2|z_2|^2$ for Gaussian integers.

**When it fires.** Representing integers as sums of two squares; building large solutions from small ones. *Trigger:* "express $N=\,$(product) as a sum of two squares."

**Micro-example.** $(1^2+1^2)(2^2+1^2)=(2-1)^2+(1+2)^2=1+9=10=5\cdot2$.

**Watch for.** The two distinct pairings give two representations; sign choices matter.

**Used in.** P2 Ch. 20 (Analogy/Transfer: "Euler four-square identity via quaternions") *(provisional)*. **Neighbours.** → D08 (complex-modulus reading), C-cluster (sum-of-two-squares theorems).

**Named proof.** The Gaussian-integer norm identity $|z_1z_2|^2=|z_1|^2|z_2|^2$ — Hardy & Wright, *Theory of Numbers*, §12.6.

---

### A11 · Partial Fractions Decomposition — Core

> Every proper rational $\dfrac{P(x)}{Q(x)}$ splits into a sum of terms $\dfrac{A}{(x-a)^k}$ and $\dfrac{Bx+C}{(x^2+bx+c)^k}$.

**What it says.** Any proper rational function is a sum of simple, individually integrable/summable pieces.

**The move.** Break a single complicated fraction into atoms — which then telescope (in sums) or integrate to logs/arctangents (in calculus).

**When it fires.** Integrating a rational function; summing a series whose term is a rational function of $k$. *Trigger:* "the term is $\frac{1}{k(k+1)}$-shaped — split it."

**Micro-example.** $\frac{1}{x^2-1}=\frac12\big(\frac{1}{x-1}-\frac{1}{x+1}\big)$.

**Watch for.** The numerator degree must be lower than the denominator's (else divide first); repeated and irreducible-quadratic factors need the full template.

**Used in.** P2 Ch. 6, Ch. 18 PP1, Ch. 9 slate PP5 *(provisional)*. **Neighbours.** → A06 (telescoping it enables), F04c (standard integral forms).

**Named proof.** Existence and uniqueness of the decomposition over the splitting field — Apostol, *Calculus*, Vol. 1.

---

### A12 · Vandermonde's Identity — Core

> $\displaystyle\binom{m+n}{r}=\sum_{k=0}^{r}\binom{m}{k}\binom{n}{r-k}$.

**What it says.** Choosing $r$ from a combined group equals summing over how many come from each subgroup.

**The move.** Split a single binomial coefficient into a convolution — the algebraic shadow of a "choose from two pools" counting argument.

**When it fires.** Simplifying sums of products of binomial coefficients; proving combinatorial identities. *Trigger:* "$\sum_k \binom{m}{k}\binom{n}{r-k}$ appears."

**Micro-example.** $\sum_{k=0}^{n}\binom{n}{k}^2=\binom{2n}{n}$ (take $m=n$, $r=n$, and $\binom{n}{k}=\binom{n}{n-k}$).

**Watch for.** Index range must cover all valid splits; terms with $k>m$ or $r-k>n$ are zero.

**Used in.** P2 Ch. 15 (multinomial generalisation) *(provisional)*. **Neighbours.** → A05, A14, G03 (double counting is the bijective proof).

**Named proof.** Compare coefficients of $x^r$ in $(1+x)^{m+n}=(1+x)^m(1+x)^n$.

---

### A13 · Fibonacci–Cassini Identity — Stretch

> $F_{n+1}F_{n-1}-F_n^2=(-1)^n$.

**What it says.** Consecutive Fibonacci numbers obey a rigid product law with alternating sign.

**The move.** Capture a sequence's global structure in one local identity — proved instantly as the determinant of $\begin{psmallmatrix}1&1\\1&0\end{psmallmatrix}^n$.

**When it fires.** Problems pairing consecutive Fibonacci (or Lucas) terms; near-square or near-product constraints. *Trigger:* "$m^2-mn-n^2=\pm1$ — these are consecutive Fibonacci numbers."

**Micro-example.** $F_5F_3-F_4^2=5\cdot2-3^2=1=(-1)^4$.

**Watch for.** Sign depends on parity of $n$; generalises to Lucas sequences with a different constant.

**Used in.** P3 Ch. 3 PP3.1 (IMO 1981 P3 hint) *(provisional)*. **Neighbours.** → E02 (Fibonacci/golden ratio), E10 (characteristic-equation method), PR10 (matrix determinant).

**Named proof.** Take determinants of $\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)^n$ — Vajda, *Fibonacci & Lucas Numbers*.

---

### A14 · Multinomial Theorem — Core

> $(x_1+\cdots+x_k)^n=\displaystyle\sum_{|\alpha|=n}\frac{n!}{\alpha_1!\cdots\alpha_k!}\,x_1^{\alpha_1}\cdots x_k^{\alpha_k}$.

**What it says.** The binomial theorem for any number of terms; the coefficients count arrangements with repetition.

**The move.** Expand a power of a sum of many terms and read off a single multinomial coefficient — converts an algebraic expansion into a counting of arrangements.

**When it fires.** Coefficient extraction in $(x_1+\cdots+x_k)^n$; counting words with prescribed letter multiplicities. *Trigger:* "coefficient of $x^ay^bz^c$ in $(x+y+z)^n$."

**Micro-example.** Coefficient of $x^2yz$ in $(x+y+z)^4$ is $\frac{4!}{2!1!1!}=12$.

**Watch for.** The exponents must sum to $n$; factorials in the denominator are per-variable.

**Used in.** P2 Ch. 15 ("natural generalisation of the binomial theorem") *(provisional)*. **Neighbours.** → A05, A12, G05 (stars-and-bars indexes the terms).

**Named proof.** Induction on the number of terms $k$, reducing to A05 — standard.

---

### A15 · Cyclotomic Factorisation — Stretch

> $x^n-1=\displaystyle\prod_{d\mid n}\Phi_d(x)$, where $\Phi_d$ is the $d$-th cyclotomic polynomial.

**What it says.** $x^n-1$ factors over $\mathbb{Z}$ into pieces indexed by the divisors of $n$, each piece carrying the primitive $d$-th roots of unity.

**The move.** Refine the crude factor $x-1$ of A03 into the *finest* integer factorisation, exposing rotational/order structure invisible in the raw difference.

**When it fires.** Divisibility of $a^n-1$ by primitive-root structure; problems about orders modulo $p$; sums over roots of unity. *Trigger:* "primitive $n$-th root of unity" or "$\Phi_n$ appears."

**Micro-example.** $x^6-1=(x-1)(x+1)(x^2+x+1)(x^2-x+1)=\Phi_1\Phi_2\Phi_3\Phi_6$.

**Watch for.** $\Phi_n$ is not "$x^n-1$ over lower factors" naively — use the divisor product; coefficients are not always in $\{-1,0,1\}$ (first exception at $n=105$).

**Used in.** P2 Ch. 8 domain translation (roots of unity toolkit) *(provisional)*. **Neighbours.** → A03, C11/C12 (orders and primitive roots), D08 (roots of unity as geometry).

**Named proof.** Möbius inversion over the divisor lattice — Ireland & Rosen, *A Classical Introduction to Modern Number Theory*, Ch. 13.

---

### A16 · Rational Root Theorem — Core

> If $f(x)=a_nx^n+\cdots+a_0\in\mathbb{Z}[x]$ has a rational root $\tfrac{p}{q}$ in lowest terms, then $p\mid a_0$ and $q\mid a_n$.

**What it says.** Any rational root is built from a divisor of the constant term over a divisor of the leading coefficient.

**The move.** Turn an infinite search for roots into a *finite* checklist — the candidate set is just $\{\pm\,\text{divisor of }a_0 / \text{divisor of }a_n\}$.

**When it fires.** Factoring an integer polynomial; proving a root is irrational by exhausting the rational candidates. *Trigger:* "find a rational root of …" or "show this root is irrational."

**Micro-example.** For $2x^3-3x^2-3x+2$, candidates are $\pm1,\pm2,\pm\tfrac12$; testing gives $x=2$ as a root.

**Watch for.** Only finds *rational* roots; absence of a rational root does not mean no real root.

**Used in.** P2 Ch. 9 (integer-domain candidates), Ch. 14 (integer-root parity) *(provisional)*. **Neighbours.** → A07a, A07b (peel off the found root); PR05 (polynomial basics).

**Named proof.** Gauss's lemma on primitive polynomials — standard.

---

### A17 · Ravi Substitution — Core

> For triangle sides $a,b,c$: set $a=y+z,\;b=z+x,\;c=x+y$ with $x,y,z>0$; then $\Delta^2=xyz(x+y+z)$.

**What it says.** The constraint "$a,b,c$ are sides of a triangle" is exactly "$x,y,z>0$" in the new variables.

**The move.** Dissolve the triangle inequalities entirely — three awkward constraints become three free positive variables, after which symmetric tools (AM–GM, SOS) apply unobstructed.

**When it fires.** Any inequality or optimisation over triangle sides. *Trigger:* "$a,b,c$ are sides of a triangle and we must prove an inequality."

**Micro-example.** Heron's $\Delta=\sqrt{s(s-a)(s-b)(s-c)}$ becomes $\sqrt{xyz(x+y+z)}$, with $s=x+y+z$.

**Watch for.** Valid only when the triangle inequalities are *strict*; remember to translate the target inequality fully into $x,y,z$.

**Used in.** P2 Ch. 5 WE2 ("Ravi reduces to AM–GM + SOS"; Heron in Ravi coords) *(provisional)*. **Neighbours.** → B01, B09 (the tools it unlocks), D09 (Heron), D18 (triangle metric relations).

**Named proof.** Direct algebraic substitution, verified by expansion — Engel; standard olympiad texts.

---

# Cluster B — Inequalities

*The art of bounding one quantity by another. These gems are the executable core of the* Inequality Constraints *and* Extremal *archetypes: each one converts a hard optimisation into a one-line comparison, and most pin the extremum at a symmetric point.*

---

### B01 · AM–GM Inequality — Core

> For nonnegative reals $a_1,\dots,a_n$: $\;\dfrac{a_1+\cdots+a_n}{n}\ge\sqrt[n]{a_1\cdots a_n}$, with equality iff all $a_i$ are equal.

**What it says.** The arithmetic mean never falls below the geometric mean; they meet only when the numbers are equal.

**The move.** Convert a fixed *sum* into a bound on a *product* (or vice versa) and pin the extremum at the all-equal point — collapsing a multivariable optimisation into a single symmetric case, with no calculus.

**When it fires.** Fixed sum, bound a product (or fixed product, bound a sum); symmetric expressions; optimisation without Lagrange multipliers. *Trigger:* "maximise/minimise … given the sum/product is fixed."

**Micro-example.** $x+\tfrac1x\ge2\sqrt{x\cdot\tfrac1x}=2$ for $x>0$, equality at $x=1$.

**Watch for.** Dropping nonnegativity; asserting equality is *attainable* when a constraint forbids all variables being equal; using it in the wrong direction.

**Used in.** P2 Ch. 7, 10; P4 Case 5 (Joshi Ch. 24 Comment 8; archetypes #10 + #12) — the most-used single gem in the book. *(Case 5 verified; P2 refs provisional.)* **Neighbours.** → B02, B03 (AM–GM is Jensen on $\log$), B05 ($M_0\le M_1$ rung), B13 (weighted form).

**Named proof.** Cauchy's forward–backward induction, or convexity of $-\log$ — Hardy, Littlewood & Pólya, *Inequalities*, §2.5.

---

### B02 · Cauchy–Schwarz Inequality (Finite) — Core

> $\big(\sum a_ib_i\big)^2\le\big(\sum a_i^2\big)\big(\sum b_i^2\big)$; Engel/Titu form: $\displaystyle\sum\frac{a_i^2}{b_i}\ge\frac{(\sum a_i)^2}{\sum b_i}$.

**What it says.** The squared dot product never exceeds the product of squared norms; equality iff the vectors are proportional.

**The move.** Decouple a sum of products into two independent sums you control — or, in Titu form, bound a sum of fractions from below by a single fraction.

**When it fires.** A sum of products to bound; a sum of squares-over-terms (Titu); proving an inequality with a "$\sum a_ib_i$" shape. *Trigger:* "$\sum \frac{a_i^2}{b_i}$" or "bound $\sum a_ib_i$."

**Micro-example.** $(1+1+1)(a^2+b^2+c^2)\ge(a+b+c)^2$, so $a^2+b^2+c^2\ge\tfrac{(a+b+c)^2}{3}$.

**Watch for.** Choosing the wrong split of the terms into $a_i,b_i$; Titu form needs $b_i>0$.

**Used in.** P2 Ch. 7 WE2, PP4–5; Ch. 10 *(provisional)*. **Neighbours.** → B05, B11 (Nesbitt via Titu), B14 (integral form), B15 (Young/Hölder family).

**Named proof.** Nonnegativity of the discriminant of $\sum(a_it-b_i)^2\ge0$ — Steele, *The Cauchy–Schwarz Master Class*.

---

### B03 · Jensen's Inequality — Core

> $f$ convex on $I$: $\;f\!\big(\sum w_ix_i\big)\le\sum w_if(x_i)$ for weights $w_i\ge0$, $\sum w_i=1$ (reverse for concave $f$).

**What it says.** A convex function of an average is at most the average of the function.

**The move.** Push a convex/concave function through an average to manufacture an inequality — the single principle from which AM–GM, power-mean, and many named inequalities descend.

**When it fires.** A sum $\sum f(x_i)$ with $f$ visibly convex/concave (e.g. $\ln,\,t\ln t,\,x^p$); symmetric constraints. *Trigger:* "the summand is a convex function of each variable."

**Micro-example.** $\ln$ is concave, so $\tfrac1n\sum\ln a_i\le\ln\tfrac{\sum a_i}{n}$ — which is AM–GM.

**Watch for.** Getting convex vs. concave backwards; weights must sum to $1$; the function must be convex on the whole range used.

**Used in.** P2 Ch. 7 WE2, Ch. 10 WE3 (Jensen on $t\ln t$ + AM–GM) *(provisional)*. **Neighbours.** → B01, B05, B15 (Young); PR13 (convexity via $f''$).

**Named proof.** Supporting-line (tangent) argument for convex $f$ — Hardy, Littlewood & Pólya, *Inequalities*, §3.14.

---

### B04 · Chebyshev's Sum Inequality — Stretch

> If $a_1\le\cdots\le a_n$ and $b_1\le\cdots\le b_n$ (same order): $\;n\sum a_ib_i\ge\big(\sum a_i\big)\big(\sum b_i\big)$ (reverse if oppositely ordered).

**What it says.** Similarly-sorted sequences correlate; their average product beats the product of averages.

**The move.** Exploit a *monotonic alignment* between two sequences to compare a sum of products with a product of sums. (Distinct from Chebyshev's *probability* inequality.)

**When it fires.** Two sequences known to be sorted the same way; symmetric sums where order is controlled. *Trigger:* "both sequences increase together — pair them."

**Micro-example.** For $a\ge b\ge c$: $3(a^2+b^2+c^2)\ge(a+b+c)(a+b+c)$, i.e. the QM–AM step.

**Watch for.** Requires *known* ordering of both sequences; reverses if they are oppositely sorted.

**Used in.** P2 Ch. 9 WE3, Ch. 10 WE2, Ch. 7 PP7 *(provisional)*. **Neighbours.** → B07 (rearrangement is the finer statement), B05.

**Named proof.** Sum the rearrangement inequality over all cyclic shifts — Hardy, Littlewood & Pólya, *Inequalities*, §2.17.

---

### B05 · Power Mean Inequality — Core

> For $p\le q$: $\;M_p(x)\le M_q(x)$, where $M_p=\big(\tfrac1n\sum x_i^p\big)^{1/p}$. Hence $\min\le \text{HM}\le \text{GM}\le \text{AM}\le \text{QM}\le\max$.

**What it says.** Means indexed by their exponent increase monotonically in that exponent.

**The move.** Place AM, GM, HM, QM on a single ladder so you can jump between any two means in one inequality.

**When it fires.** An expression involving several different means of the same numbers; bounding QM by AM or AM by GM. *Trigger:* "compare $\sqrt{\frac{\sum x_i^2}{n}}$ with $\frac{\sum x_i}{n}$."

**Micro-example.** QM $\ge$ AM gives $\sqrt{\tfrac{a^2+b^2}{2}}\ge\tfrac{a+b}{2}$.

**Watch for.** The $p\to0$ limit *is* the geometric mean; signs of $p$ and positivity of $x_i$ matter.

**Used in.** P2 Ch. 7 PP6 ("Jensen on $\varphi(t)=t^{q/p}$") *(provisional)*. **Neighbours.** → B01, B03 (proved via Jensen), B02.

**Named proof.** Jensen applied to $t\mapsto t^{q/p}$ — Hardy, Littlewood & Pólya, *Inequalities*, §2.9.

---

### B06 · Triangle Inequality (Metric) — Core

> $|a+b|\le|a|+|b|$; reverse: $\big|\,|a|-|b|\,\big|\le|a-b|$. Holds for reals, complex numbers, and vectors.

**What it says.** A straight path is shortest; norms are subadditive.

**The move.** Bound a combined magnitude by separate magnitudes — or, in reverse, bound a difference of magnitudes from below — converting geometry of distance into algebra.

**When it fires.** Estimating $|a+b|$ or $|a-b|$; existence of a triangle; bounding sums of complex numbers or vectors. *Trigger:* "bound the size of a sum/difference."

**Micro-example.** $|z_1+z_2|\le|z_1|+|z_2|$ bounds the modulus of a sum of complex numbers.

**Watch for.** Equality needs same-direction (real, nonnegative ratio) vectors; the reverse form's outer absolute value.

**Used in.** P2 Ch. 8 PP7 (reverse triangle inequality), Ch. 9 WE3 *(provisional)*. **Neighbours.** → PR03, PR16 (complex/vector norms), B02.

**Named proof.** Square both sides and apply Cauchy–Schwarz to the cross term — standard.

---

### B07 · Rearrangement Inequality — Stretch

> For $a_1\le\cdots\le a_n$ and $b_1\le\cdots\le b_n$: the sum $\sum a_ib_{\sigma(i)}$ is **maximised** by the same-order pairing and **minimised** by the reverse-order pairing.

**What it says.** To maximise a sum of paired products, match large with large; to minimise, match large with small.

**The move.** Replace an optimisation over all pairings (a permutation search) with a single sorting decision.

**When it fires.** "Over all permutations, maximise/minimise $\sum a_ib_{\sigma(i)}$"; many symmetric inequalities reduce to it. *Trigger:* "which pairing of these two lists is largest?"

**Micro-example.** $a^2+b^2\ge 2ab$ is the two-term rearrangement (same-order beats cross-order).

**Watch for.** Both sequences must be sortable on a common scale; ties are fine but track them.

**Used in.** P2 Ch. 9 WE3, Ch. 10 WE2 *(provisional)*. **Neighbours.** → B04 (its averaged corollary), B01.

**Named proof.** Exchange argument: swapping any out-of-order pair increases the sum — Hardy, Littlewood & Pólya, *Inequalities*, §10.2.

---

### B08 · Schur's Inequality — Stretch

> For $a,b,c\ge0$ and $t>0$: $\;a^t(a-b)(a-c)+b^t(b-a)(b-c)+c^t(c-a)(c-b)\ge0$. The case $t=1$ is most common.

**What it says.** A specific cyclic combination of three nonnegative numbers is always nonnegative.

**The move.** Supply the "missing" term that AM–GM and Cauchy–Schwarz cannot reach in tight three-variable symmetric inequalities — often the final lemma in an SOS attack.

**When it fires.** A symmetric three-variable inequality that is *tight* and resists AM–GM. *Trigger:* "equality at $a=b=c$ *and* at $(t,t,0)$ — suspect Schur."

**Micro-example.** $t=1$ gives $a^3+b^3+c^3+abc\cdot3\ge ab(a+b)+\cdots$, i.e. $a^3+b^3+c^3+3abc\ge \sum_{sym}a^2b$.

**Watch for.** WLOG ordering $a\ge b\ge c$ to prove it; it is *not* symmetric-by-AM-GM and can fail if signs are wrong.

**Used in.** P2 Ch. 5 WE2 (alternative route), Ch. 10 WE3 *(provisional)*. **Neighbours.** → B09 (SOS), B10 (Muirhead), A17 (Ravi).

**Named proof.** WLOG $a\ge b\ge c$, group the first two terms and check the sign — Engel, *Problem-Solving Strategies*, Ch. 7.

---

### B09 · SOS (Sum of Squares) Decomposition — Stretch

> Write $f(a,b,c)=\sum S_a(b-c)^2$ with coefficients $S_a,S_b,S_c$; if each $S\ge0$ (or under known orderings), then $f\ge0$.

**What it says.** Many symmetric inequalities can be rewritten as a manifestly nonnegative combination of squared differences.

**The move.** Reduce "prove $f\ge0$" to "exhibit $f$ as a sum of squares" — turning an inequality into an algebra-of-squares identity with a sign check on the coefficients.

**When it fires.** Symmetric inequalities with equality at $a=b=c$; after Ravi or normalisation. *Trigger:* "rewrite the difference as $\sum S_a(b-c)^2$."

**Micro-example.** $a^2+b^2+c^2-ab-bc-ca=\tfrac12\big[(a-b)^2+(b-c)^2+(c-a)^2\big]\ge0$.

**Watch for.** Nonnegativity of each $S$ may need the ordering $a\ge b\ge c$ and the "SOS criterion," not just inspection.

**Used in.** P2 Ch. 5 WE2 (proof method for Hadwiger–Finsler) *(provisional)*. **Neighbours.** → B08, B10, A09 (symmetric factorisation).

**Named proof.** Exhibit the explicit squared-difference identity and sign-check coefficients — Pham Kim Hung, *Secrets in Inequalities*.

---

### B10 · Muirhead's Inequality — Stretch

> If the exponent vector $(\alpha)$ **majorises** $(\beta)$, then $\sum_{sym} x^{\alpha}\ge\sum_{sym} x^{\beta}$ for nonnegative $x_i$.

**What it says.** Symmetric-sum monomials compare according to how "spread out" their exponent vectors are.

**The move.** Settle a whole class of symmetric monomial inequalities by a single combinatorial check on exponent vectors (majorisation), bypassing ad-hoc AM–GM bookkeeping.

**When it fires.** Comparing two symmetric sums of monomials of the same degree. *Trigger:* "$\sum_{sym} a^3b \ge \sum_{sym} a^2b^2$?" — check majorisation.

**Micro-example.** $(2,0)\succ(1,1)$, so $a^2+b^2\ge 2ab$ (the symmetric-sum reading).

**Watch for.** Both sides must be symmetric sums of the **same degree**; majorisation requires equal totals and the dominance condition; not a substitute for cited rigor at IMO (prove via AM–GM if asked).

**Used in.** Blueprint §9.7 seed; P2 Ch. 10 symmetric-polynomial inequalities *(provisional)*. **Neighbours.** → B01, B08, B09.

**Named proof.** Repeated AM–GM along the majorisation (Robin Hood) steps — Hardy, Littlewood & Pólya, *Inequalities*, §2.18.

---

### B11 · Nesbitt's Inequality — Core

> For $a,b,c>0$: $\;\dfrac{a}{b+c}+\dfrac{b}{a+c}+\dfrac{c}{a+b}\ge\dfrac32$.

**What it says.** The canonical three-variable cyclic fraction sum is bounded below by $\tfrac32$.

**The move.** Serve as the benchmark whose proof *teaches the methods* — it falls to Titu/Cauchy–Schwarz, to AM–GM, and to rearrangement, so it is the standard rehearsal for symmetric fraction inequalities.

**When it fires.** A cyclic sum of single-variable-over-sum-of-others. *Trigger:* "$\sum \frac{a}{b+c}$ shape."

**Micro-example.** By Titu: $\sum\frac{a^2}{a(b+c)}\ge\frac{(a+b+c)^2}{2(ab+bc+ca)}\ge\frac32$.

**Watch for.** Strictly positive variables; the final step uses $(a+b+c)^2\ge3(ab+bc+ca)$.

**Used in.** P2 Ch. 10 (JEE-standard family) *(provisional)*. **Neighbours.** → B02 (Titu), B01, B09.

**Named proof.** Titu/Cauchy–Schwarz then $(a+b+c)^2\ge3(ab+bc+ca)$ — standard.

---

### B12 · Bernoulli's Inequality — Core

> $(1+x)^n\ge 1+nx$ for $x>-1$ and integer $n\ge1$ (more generally real $n\ge1$); equality iff $x=0$ or $n=1$.

**What it says.** A power of $1+x$ is at least its linear (tangent-line) approximation.

**The move.** Replace an awkward power by a clean linear lower bound — the discrete ancestor of the linearisation $e^x\ge1+x$.

**When it fires.** Bounding $(1+x)^n$ from below; growth/limit estimates; inductive inequality steps. *Trigger:* "estimate $(1+\text{small})^n$."

**Micro-example.** $(1.01)^{100}\ge1+100(0.01)=2$.

**Watch for.** The hypothesis $x>-1$; the inequality reverses for $0<n<1$.

**Used in.** Blueprint §9.7; P2 Ch. 5 PP5 (Bernoulli ODE context) *(provisional)*. **Neighbours.** → F08 (analytic linearisation $e^x\ge1+x$), B01.

**Named proof.** Induction on $n$, or convexity of $x\mapsto(1+x)^n$ — standard.

---

### B13 · Weighted AM–GM — Core

> For $w_i\ge0$ with $\sum w_i=1$: $\;\sum w_ia_i\ge\prod a_i^{\,w_i}$.

**What it says.** The weighted arithmetic mean dominates the weighted geometric mean.

**The move.** Tune the weights to the structure of a specific problem — the flexible form that hits equality exactly where you need it, which the equal-weight B01 cannot.

**When it fires.** An inequality whose equality case is *not* "all variables equal," or where terms carry natural weights. *Trigger:* "the equality point is asymmetric — weight the means."

**Micro-example.** With weights $\tfrac23,\tfrac13$: $\tfrac23a+\tfrac13b\ge a^{2/3}b^{1/3}$.

**Watch for.** Weights must be nonnegative and sum to $1$; choosing them is the whole skill.

**Used in.** P2 Ch. 7 WE2 (Cauchy normalisation, B01 as special case) *(provisional)*. **Neighbours.** → B01 (equal-weight case), B03 (Jensen on $\ln$), B15 (Young).

**Named proof.** Jensen on $\ln$ with the prescribed weights — Hardy, Littlewood & Pólya, *Inequalities*, §2.5.

---

### B14 · Cauchy–Schwarz, Integral Form — Core

> $\Big(\displaystyle\int_a^b fg\Big)^2\le\Big(\int_a^b f^2\Big)\Big(\int_a^b g^2\Big)$.

**What it says.** The finite Cauchy–Schwarz inequality, with sums replaced by integrals.

**The move.** Carry the decoupling power of B02 into function space — bound an integral of a product by the product of $L^2$ norms; proved by $\int(f-\lambda g)^2\ge0$.

**When it fires.** An integral of a product $\int fg$; estimates on $\big(\int f\big)^2$; inner-product arguments for functions. *Trigger:* "$\int fg$ to be bounded."

**Micro-example.** $\big(\int_0^1 f\big)^2\le\int_0^1 1^2\cdot\int_0^1 f^2=\int_0^1 f^2$ (take $g\equiv1$).

**Watch for.** $f,g$ must be square-integrable; equality iff $f=\lambda g$ a.e.

**Used in.** P2 Ch. 7 PP5 (normalised $\|f\|_2=\|g\|_2=1$) *(provisional)*. **Neighbours.** → B02 (discrete form), B15, F04b (integration by parts).

**Named proof.** Minimise $\int(f-\lambda g)^2\ge0$ over $\lambda$ — standard real-analysis text.

---

### B15 · Young's Inequality — Stretch

> For $a,b\ge0$ and conjugate exponents $\tfrac1p+\tfrac1q=1$ ($p,q>1$): $\;ab\le\dfrac{a^p}{p}+\dfrac{b^q}{q}$.

**What it says.** A product is bounded by a weighted sum of powers determined by conjugate exponents.

**The move.** Split a product into two power-terms you can control separately — the seed from which Hölder's inequality (and hence much of $L^p$ analysis) grows; $p=q=2$ recovers $ab\le\tfrac{a^2+b^2}{2}$.

**When it fires.** A stubborn product $ab$ inside a larger estimate; proving Hölder; analysis-flavoured olympiad bounds. *Trigger:* "break $ab$ into $\frac{a^p}{p}+\frac{b^q}{q}$."

**Micro-example.** With $p=q=2$: $ab\le\tfrac12a^2+\tfrac12b^2$.

**Watch for.** Exponents must be conjugate; both $a,b\ge0$.

**Used in.** Analysis foundation; bridges B01→B03→B05 toward Hölder *(provisional)*. **Neighbours.** → B01 ($p=q=2$), B03, B13.

**Named proof.** Convexity of $\exp$, or integrate $y=x^{p-1}$ and its inverse — Rudin, *Real & Complex Analysis*.

---

# Cluster C — Number Theory

*The arithmetic of integers modulo $n$, divisibility, and primes. These gems power the* Parity / Modularity *and* Hidden Structure *archetypes — they let you replace a problem about all integers with a problem about finitely many residues.*

---

### C01 · Fermat's Little Theorem — Core

> $p$ prime, $p\nmid a$ $\Rightarrow$ $a^{p-1}\equiv1\pmod p$; equivalently $a^p\equiv a\pmod p$ for all $a$.

**What it says.** Raising to the $(p-1)$-th power collapses every nonzero residue to $1$ modulo a prime.

**The move.** Reduce arbitrarily large exponents modulo $p-1$ — turning $a^{\text{huge}}$ into $a^{\text{small}}$ in one step.

**When it fires.** Computing $a^N\bmod p$ for large $N$; proving divisibility by a prime; modular inverses. *Trigger:* "find $a^N \bmod p$" with $p$ prime.

**Micro-example.** $2^{100}\bmod 7$: since $2^6\equiv1$, $2^{100}=2^{96}\cdot2^4\equiv2^4=16\equiv2$.

**Watch for.** Requires $p$ prime and $p\nmid a$; reduce the *exponent* mod $p-1$, the base mod $p$.

**Used in.** P2 Ch. 14; P4 NT cases throughout *(provisional)*. **Neighbours.** → C02 (composite generalisation), C06 (inverse $a^{p-2}$), C11 (order divides $p-1$).

**Named proof.** Lagrange's theorem on $(\mathbb{Z}/p)^\times$, or binomial induction — Hardy & Wright, *Theory of Numbers*, §6.

---

### C02 · Euler's Totient Theorem — Core

> $\gcd(a,n)=1$ $\Rightarrow$ $a^{\varphi(n)}\equiv1\pmod n$, where $\varphi(n)=n\prod_{p\mid n}(1-\tfrac1p)$.

**What it says.** Fermat's theorem for any modulus: the totient is a universal exponent for units mod $n$.

**The move.** Reduce large exponents modulo $\varphi(n)$ for *composite* moduli, extending C01 beyond primes.

**When it fires.** $a^N\bmod n$ with $n$ composite and $\gcd(a,n)=1$; periodicity of powers. *Trigger:* "find the last two digits of $a^N$" (work mod $100$).

**Micro-example.** Last two digits of $3^{1000}$: $\varphi(100)=40$, $3^{1000}=3^{40\cdot25}\equiv1\pmod{100}$ — ends in $01$.

**Watch for.** Needs $\gcd(a,n)=1$; reduce exponent mod $\varphi(n)$, not mod $n$.

**Used in.** P2 Ch. 14; P4 Cases 22, 23 (order arguments) *(provisional)*. **Neighbours.** → C01, C11, C12 (cyclic structure of units).

**Named proof.** Lagrange's theorem applied to the group of units $(\mathbb{Z}/n)^\times$ — Hardy & Wright, §6.

---

### C03 · Chinese Remainder Theorem (CRT) — Core

> For pairwise-coprime $m_1,\dots,m_k$, the system $x\equiv a_i\pmod{m_i}$ has a unique solution modulo $\prod m_i$.

**What it says.** Independent congruences with coprime moduli always glue into one congruence.

**The move.** Split a problem modulo a composite $N$ into independent sub-problems modulo its prime-power factors — divide and conquer for arithmetic.

**When it fires.** Solving simultaneous congruences; counting solutions mod $N$ by factoring $N$; constructing integers with prescribed residues. *Trigger:* "find $x$ with $x\equiv\cdots$ mod several coprime numbers."

**Micro-example.** $x\equiv2\pmod3,\;x\equiv3\pmod5\Rightarrow x\equiv8\pmod{15}$.

**Watch for.** Moduli must be pairwise coprime; the answer is unique only modulo the product.

**Used in.** P4 Case 15 *(provisional)*. **Neighbours.** → C02 ($\varphi$ is multiplicative via CRT), C01, G02.

**Named proof.** Explicit construction via modular inverses (or a counting/bijection argument) — Ireland & Rosen, Ch. 3.

---

### C04 · Lifting-the-Exponent Lemma (LTE) — Stretch

> For odd prime $p\mid a-b$ (and $p\nmid a,b$): $\;v_p(a^n-b^n)=v_p(a-b)+v_p(n)$. A separate $p=2$ variant exists.

**What it says.** The exact power of $p$ dividing $a^n-b^n$ is computable from the power dividing $a-b$ plus the power dividing $n$.

**The move.** Track the *exact* $p$-adic valuation through an exponentiation, replacing clumsy factoring with one additive formula.

**When it fires.** "What is the largest power of $p$ dividing $a^n\pm b^n$?"; bounding valuations in divisibility chains. *Trigger:* "$v_p$ of a power difference."

**Micro-example.** $v_3(10^6-1)=v_3(10-1)+v_3(6)=2+1=3$, so $27\mid 10^6-1$ but $81\nmid$.

**Watch for.** The $p=2$ case has a different formula; needs $p\mid a-b$ and $p\nmid ab$.

**Used in.** Blueprint §9.7 seed; olympiad divisibility chains *(provisional)*. **Neighbours.** → A03 (factoring it refines), C05, C01.

**Named proof.** Induction on $v_p(n)$ via the factorisation A03 — standard LTE references (e.g. Sriram, *Lifting the Exponent*).

---

### C05 · Legendre's Formula — Stretch

> $v_p(n!)=\displaystyle\sum_{k\ge1}\left\lfloor\frac{n}{p^k}\right\rfloor=\frac{n-S_p(n)}{p-1}$, where $S_p(n)$ is the base-$p$ digit sum.

**What it says.** The power of a prime in $n!$ is a sum of floor functions — equivalently, $(n$ minus its digit sum$)/(p-1)$.

**The move.** Compute factorial valuations and binomial-coefficient valuations exactly, converting a counting-of-multiples question into a digit computation.

**When it fires.** Trailing zeros of $n!$; divisibility of $\binom{n}{k}$; $p$-adic analysis of factorials. *Trigger:* "how many times does $p$ divide $n!$ (or $\binom{m+n}{m}$)?"

**Micro-example.** Trailing zeros of $100!$: $v_5(100!)=20+4=24$.

**Watch for.** Sum the floors of *all* powers of $p\le n$; the digit-sum form is a shortcut, not a different fact.

**Used in.** P2 Ch. 14 WE1 ("Kummer/Legendre $p$-adic proof") *(provisional)*. **Neighbours.** → C08 (Kummer counts carries), C16 (floor function), A05.

**Named proof.** Count multiples of $p,p^2,\dots$ among $1,\dots,n$ — Hardy & Wright, §6.

---

### C06 · Bézout's Identity & Modular Inverse — Core

> $\exists\,m,n\in\mathbb{Z}:\;ma+nb=\gcd(a,b)$. If $\gcd(a,n)=1$, then $a^{-1}\bmod n$ exists (and equals $a^{\varphi(n)-1}$, or $a^{p-2}$ for prime $n=p$).

**What it says.** The gcd of two integers is an integer combination of them; coprimality is exactly invertibility mod $n$.

**The move.** Manufacture a modular inverse (or solve $ax\equiv c$) via the extended Euclidean algorithm — the backbone of all modular arithmetic.

**When it fires.** Solving linear congruences; existence of inverses; expressing $\gcd$ as a combination. *Trigger:* "solve $ax\equiv c\pmod n$" or "find $a^{-1}\bmod n$."

**Micro-example.** $3\cdot 7\equiv1\pmod{20}$, so $3^{-1}\equiv7\pmod{20}$.

**Watch for.** Inverse exists *only* when $\gcd(a,n)=1$; the Bézout coefficients are not unique.

**Used in.** Blueprint §9.7; P4 NT background *(provisional)*. **Neighbours.** → C01, C03, A03 (Euclidean step is gcd-invariant).

**Named proof.** The extended Euclidean algorithm, run backwards — standard.

---

### C07 · Wilson's Theorem — Stretch

> $p$ is prime $\iff (p-1)!\equiv-1\pmod p$.

**What it says.** A prime is detected exactly by the residue of the factorial just below it.

**The move.** Pair each residue with its inverse (only $\pm1$ are self-inverse) so the factorial collapses to $-1$ — a clean primality criterion and a source of factorial congruences.

**When it fires.** Factorial residues mod $p$; proving a number prime/composite via factorials; problems mentioning $(p-1)!$. *Trigger:* "$(p-1)! \bmod p$ appears."

**Micro-example.** $(5-1)!=24\equiv-1\equiv4\pmod5$.

**Watch for.** It is an iff but impractical as a primality *test* (factorial is huge); mainly a theoretical lever.

**Used in.** P2 Ch. 14 PP1 ("$\{2,3,5\}$ via Wilson") *(provisional)*. **Neighbours.** → C01, C06 (inverse pairing), C10.

**Named proof.** Pair each residue with its distinct inverse; only $\pm1$ self-pair — Hardy & Wright, §6.

---

### C08 · Kummer's Theorem — Stretch

> $v_p\!\big(\binom{m+n}{m}\big)$ equals the number of carries when adding $m$ and $n$ in base $p$.

**What it says.** The prime power dividing a binomial coefficient is literally a count of base-$p$ carries.

**The move.** Convert a divisibility question about $\binom{m+n}{m}$ into a base-$p$ addition you can do by hand.

**When it fires.** "Is $\binom{n}{k}$ divisible by $p$ (or $p^j$)?"; structure of Pascal's triangle mod $p$. *Trigger:* "$v_p$ of a binomial coefficient."

**Micro-example.** $\binom{4}{2}=6$: adding $2+2$ in base $3$ is $11_3$ with one carry, so $3^1\mid6$.

**Watch for.** Carries are base-$p$ specific; equivalent to Legendre applied three times.

**Used in.** P2 Ch. 14 WE1 (modular-lens alternative) *(provisional)*. **Neighbours.** → C05, C09 (Lucas), A05.

**Named proof.** Apply Legendre's formula (C05) to $(m+n)!,m!,n!$ and read carries — Ireland & Rosen, Ch. 1.

---

### C09 · Lucas's Theorem — Stretch

> $\binom{m}{n}\equiv\prod_i\binom{m_i}{n_i}\pmod p$, where $m_i,n_i$ are the base-$p$ digits of $m,n$.

**What it says.** A binomial coefficient mod $p$ is the product of binomial coefficients of the base-$p$ digits.

**The move.** Reduce a giant binomial coefficient mod $p$ to a product of tiny ones — and explain why Pascal's triangle mod $p$ is a Sierpiński fractal.

**When it fires.** $\binom{m}{n}\bmod p$ for large $m,n$; counting odd entries in Pascal's triangle. *Trigger:* "$\binom{m}{n}\bmod p$, $m$ large."

**Micro-example.** $\binom{6}{3}\bmod2$: $6=110_2$, $3=011_2$; some digit has $n_i>m_i$, so $\binom{6}{3}\equiv0$ (indeed $20$ is even).

**Watch for.** If any digit $n_i>m_i$ the whole product is $0$; base-$p$ digits, not base $10$.

**Used in.** P2 Ch. 14 PP7 ("Lucas Hidden in Pascal's Triangle Mod $p$") *(provisional)*. **Neighbours.** → C08, C05, A05.

**Named proof.** Expand $(1+x)^m\bmod p$ using $(1+x)^p\equiv1+x^p$ — Fine (1947); standard.

---

### C10 · Quadratic Reciprocity (Legendre Symbol) — Stretch

> For distinct odd primes $p,q$: $\;\left(\dfrac{p}{q}\right)\!\left(\dfrac{q}{p}\right)=(-1)^{\frac{(p-1)(q-1)}{4}}$, where $\left(\tfrac{a}{p}\right)=\pm1$ encodes whether $a$ is a quadratic residue.

**What it says.** Whether $p$ is a square mod $q$ is tied, by a sign rule, to whether $q$ is a square mod $p$.

**The move.** Flip a hard "is $a$ a QR mod $p$?" question into easier ones with smaller moduli — the deep symmetry that makes Legendre symbols computable.

**When it fires.** Deciding solvability of $x^2\equiv a\pmod p$; existence of square roots mod $p$. *Trigger:* "is $a$ a quadratic residue mod $p$?"

**Micro-example.** Is $5$ a QR mod $7$? $\left(\tfrac57\right)\left(\tfrac75\right)=(-1)^{(4)(6)/4}=1$, and $\left(\tfrac75\right)=\left(\tfrac25\right)=-1$, so $\left(\tfrac57\right)=-1$: no.

**Watch for.** Supplementary laws for $\left(\tfrac{-1}{p}\right)$ and $\left(\tfrac{2}{p}\right)$ are needed alongside; both primes odd.

**Used in.** Blueprint §9.7; P2 Ch. 2 outline (QR as symmetry of Legendre symbols) *(provisional)*. **Neighbours.** → C15 (Euler's criterion computes the symbol), C07.

**Named proof.** Gauss's lemma plus the Eisenstein lattice-point count — Ireland & Rosen, Ch. 5.

---

### C11 · Multiplicative Order of an Element — Stretch

> $\operatorname{ord}_m(a)=\min\{k>0:a^k\equiv1\pmod m\}$; it divides $\varphi(m)$. If $\operatorname{ord}_p(a)=p-1$, $a$ is a *primitive root*.

**What it says.** Every unit has a smallest exponent returning it to $1$, and that order divides $\varphi(m)$.

**The move.** Pin down the exact period of $a$'s powers — the key invariant for "what is the smallest $n$ with $a^n\equiv1$?" arguments.

**When it fires.** Smallest exponent / period questions; proving an exponent must be divisible by something. *Trigger:* "smallest $n$ with $a^n\equiv1\pmod m$."

**Micro-example.** $\operatorname{ord}_7(2)=3$ since $2^3=8\equiv1\pmod7$, and $3\mid\varphi(7)=6$.

**Watch for.** Order *divides* $\varphi(m)$ (not necessarily equals it); $a$ must be a unit.

**Used in.** P4 Cases 22, 23 (order-theoretic arguments) *(provisional)*. **Neighbours.** → C01, C02, C12 (primitive roots), A15.

**Named proof.** Lagrange's theorem: the order divides the group order — standard.

---

### C12 · Primitive Root Existence — Stretch

> Every prime $p$ has a primitive root $g$ with $\operatorname{ord}_p(g)=p-1$; equivalently $(\mathbb{Z}/p\mathbb{Z})^\times$ is cyclic of order $p-1$.

**What it says.** The nonzero residues mod a prime are all powers of a single generator.

**The move.** Replace multiplicative structure mod $p$ by *additive* structure in the exponent (a discrete logarithm), linearising products into sums.

**When it fires.** Counting solutions of $x^k\equiv a$; reducing multiplicative problems mod $p$ to arithmetic mod $p-1$. *Trigger:* "let $g$ be a primitive root mod $p$."

**Micro-example.** $3$ is a primitive root mod $7$: $3^1,3^2,\dots,3^6\equiv3,2,6,4,5,1$ — all units.

**Watch for.** Primitive roots exist mod $1,2,4,p^k,2p^k$ only — *not* every modulus.

**Used in.** Blueprint §9.7 (unifies C01, C02, C11) *(provisional)*. **Neighbours.** → C11, C01, C02, A15.

**Named proof.** Count elements of each order via $\sum_{d\mid n}\varphi(d)=n$ — Ireland & Rosen, Ch. 4.

---

### C13 · Zsygmondy's Theorem (Bang's Theorem) — Stretch

> For $a>b\ge1$ coprime, $a^n-b^n$ has a prime factor dividing no $a^k-b^k$ with $k<n$ — with finitely many explicit exceptions.

**What it says.** Each new exponent introduces a *brand-new* (primitive) prime factor, save for a short list of exceptions.

**The move.** Guarantee a fresh prime at each stage, which forces sequences of values to have ever-growing prime support — a powerful finiteness/uniqueness lever.

**When it fires.** "Show $a^n-b^n$ has a prime factor not seen before"; bounding solutions of exponential Diophantine equations. *Trigger:* "primitive prime divisor of $a^n-b^n$."

**Micro-example.** $2^6-1=63=7\cdot9$; the prime $7$ does not divide $2^k-1$ for $k<6$.

**Watch for.** Memorise the exceptions ($a=2,b=1,n=6$; $n=1,2$ cases; $2^1+1$ analogue for sums); coprimality required.

**Used in.** Blueprint §9.7 (primitive prime divisors) *(provisional)*. **Neighbours.** → A03, C04, C14.

**Named proof.** Cyclotomic-polynomial valuation argument — Zsygmondy (1892); see Roitman's survey.

---

### C14 · Bertrand's Postulate — Stretch

> For every integer $n\ge1$, there is a prime $p$ with $n<p\le2n$.

**What it says.** Primes are never too sparse — one always sits between $n$ and $2n$.

**The move.** Supply "a prime in a controlled range" on demand — the existence ingredient many counting and divisibility constructions need.

**When it fires.** Arguments needing a prime between bounds; showing certain products are never perfect powers. *Trigger:* "choose a prime $p$ with $n<p\le2n$."

**Micro-example.** Between $10$ and $20$ lies the prime $11$ (in fact several).

**Watch for.** Gives existence, not a specific prime; the bound $2n$ is the classical one (sharper versions exist).

**Used in.** P4 NT background *(provisional)*. **Neighbours.** → C13, C05.

**Named proof.** Erdős's central-binomial-coefficient argument — Aigner & Ziegler, *Proofs from THE BOOK*.

---

### C15 · Euler's Criterion for Quadratic Residues — Stretch

> For odd prime $p$ and $p\nmid a$: $\;a^{\frac{p-1}{2}}\equiv\left(\dfrac{a}{p}\right)\pmod p$.

**What it says.** Raising to the $\tfrac{p-1}{2}$ power returns $+1$ for quadratic residues and $-1$ for non-residues.

**The move.** Compute the Legendre symbol directly by a modular exponentiation — a usable test for "is $a$ a square mod $p$?" without invoking full reciprocity.

**When it fires.** Testing quadratic residues computationally; bridging Fermat (C01) and reciprocity (C10). *Trigger:* "decide if $a$ is a QR mod $p$ by computing $a^{(p-1)/2}$."

**Micro-example.** Is $2$ a QR mod $7$? $2^3=8\equiv1$, so yes ($3^2\equiv2$).

**Watch for.** Only for odd primes and $p\nmid a$; result is $\pm1$ mod $p$ (i.e. $1$ or $p-1$).

**Used in.** P4 NT cases (QR testing) *(provisional)*. **Neighbours.** → C10, C01, C07.

**Named proof.** Factor $a^{p-1}-1=(a^{(p-1)/2}-1)(a^{(p-1)/2}+1)$ and apply FLT — Ireland & Rosen, Ch. 5.

---

### C16 · Floor Function & Hermite's Identity — Core

> $\lfloor nx\rfloor=\displaystyle\sum_{k=0}^{n-1}\left\lfloor x+\frac{k}{n}\right\rfloor$; also $\lfloor x\rfloor+\lfloor -x\rfloor=-1$ for $x\notin\mathbb{Z}$.

**What it says.** The floor of $nx$ distributes as a sum of shifted floors; floors of $x$ and $-x$ are tightly linked.

**The move.** Manipulate floor expressions algebraically — split, shift, and combine them — turning "integer part" obstacles into identities you can compute with.

**When it fires.** Sums of floor functions; counting lattice points/multiples; Legendre's formula derivations. *Trigger:* "$\lfloor\cdot\rfloor$ inside a sum or count."

**Micro-example.** $\lfloor 2x\rfloor=\lfloor x\rfloor+\lfloor x+\tfrac12\rfloor$ (the $n=2$ Hermite identity).

**Watch for.** Boundary behaviour at integers; $\{x\}=x-\lfloor x\rfloor\in[0,1)$.

**Used in.** P2 Ch. 9 (integer-domain constraints), Ch. 14 (floor/modular) *(provisional)*. **Neighbours.** → C05 (Legendre), PR05, E01.

**Named proof.** Partition $[0,1)$ into $n$ equal subintervals and locate $\{x\}$ — standard.

---

# Cluster D — Geometry

*Synthetic, trigonometric, coordinate, and complex-number geometry. These gems supply the* Domain Translation *archetype its richest playground: each lets you re-express a geometric configuration in the language where it becomes computable.*

---

### D01 · Power of a Point — Core

> For point $P$ and a circle, along any line through $P$ meeting it at $A,B$: $\;PA\cdot PB$ is constant $=|\,d^2-r^2\,|$ (and $=PT^2$ for a tangent).

**What it says.** All secants/tangents from a fixed point to a circle share one product.

**The move.** Replace separate chord lengths by a single invariant of the point-circle pair — converting circle-chord problems into one multiplicative equation.

**When it fires.** Intersecting chords/secants/tangents; concyclic-point conditions. *Trigger:* "two chords/secants through one point."

**Micro-example.** Chords $AB,CD$ meet at $P$: $PA\cdot PB=PC\cdot PD$.

**Watch for.** Sign/length convention (use unsigned lengths for the basic JEE form); tangent case uses $PT^2$.

**Used in.** Blueprint §9.7 seed; P2 Ch. 2, 3 geometry connections *(provisional)*. **Neighbours.** → D11 (radical axis is the equal-power locus), D02.

**Named proof.** Similar triangles from the inscribed-angle theorem — Coxeter & Greitzer, *Geometry Revisited*, §2.1.

---

### D02 · Ptolemy's Theorem (+ Inequality) — Core

> Cyclic $ABCD$: $\;AC\cdot BD=AB\cdot CD+AD\cdot BC$. For general quadrilaterals, $AC\cdot BD\le AB\cdot CD+AD\cdot BC$.

**What it says.** In a cyclic quadrilateral the product of diagonals equals the sum of products of opposite sides.

**The move.** Turn a concyclicity hypothesis into a length equation (and the failure of equality measures non-concyclicity).

**When it fires.** Cyclic quadrilaterals; proving trigonometric identities (via a cyclic configuration); distance inequalities. *Trigger:* "$ABCD$ is cyclic — relate the sides and diagonals."

**Micro-example.** A rectangle is cyclic: diagonals $d$ satisfy $d^2=a\cdot a+b\cdot b$ — Pythagoras as a special case.

**Watch for.** Equality requires concyclicity *in order* $A,B,C,D$; the inequality holds always.

**Used in.** Blueprint §9.7 seed; P4 cyclic-quadrilateral case studies *(provisional)*. **Neighbours.** → D14 (Brahmagupta area), D01, D07a.

**Named proof.** Construct a point making similar triangles, or use the trig/complex form — Coxeter & Greitzer, §2.6.

---

### D03 · Angle Bisector Theorem — Core

> The internal bisector of $\angle A$ in $\triangle ABC$ meets $BC$ at $D$ with $\dfrac{BD}{DC}=\dfrac{AB}{AC}$ (external bisector: the same ratio, externally).

**What it says.** A bisector divides the opposite side in the ratio of the adjacent sides.

**The move.** Convert an angle condition into a length ratio — feeding directly into Ceva/Menelaus and mass-point arguments.

**When it fires.** Bisectors, incenter, ratios on a side. *Trigger:* "$AD$ bisects angle $A$."

**Micro-example.** Sides $AB=6,AC=4$: the bisector splits $BC$ as $BD:DC=3:2$.

**Watch for.** Internal vs. external bisector sign; the incenter divides each bisector in a known ratio too.

**Used in.** Blueprint §9.7 seed; P2 Ch. 2 symmetry geometry *(provisional)*. **Neighbours.** → D04b (Ceva), D13 (trig Ceva), D18.

**Named proof.** Law of Sines in the two sub-triangles sharing the bisector — standard.

---

### D04a · Menelaus's Theorem — Stretch

> Points $X,Y,Z$ on lines $BC,CA,AB$ (extended) are **collinear** $\iff \dfrac{BX}{XC}\cdot\dfrac{CY}{YA}\cdot\dfrac{AZ}{ZB}=-1$ (signed ratios).

**What it says.** A signed product of three side-ratios equals $-1$ exactly when the three points line up.

**The move.** Reduce a collinearity question to one multiplicative equation in signed ratios.

**When it fires.** Proving three points collinear; transversal cutting a triangle. *Trigger:* "show $X,Y,Z$ are collinear."

**Micro-example.** A line cutting two sides and the extension of the third yields the product $-1$.

**Watch for.** **Signed** ratios (the $-1$); contrast Ceva's $+1$ for concurrency.

**Used in.** Blueprint §9.7 seed; olympiad synthetic geometry *(provisional)*. **Neighbours.** → D04b (concurrency dual), D13, D12.

**Named proof.** Signed ratios via perpendiculars dropped to the transversal — Coxeter & Greitzer, §3.4.

---

### D04b · Ceva's Theorem — Stretch

> Cevians $AD,BE,CF$ are **concurrent** $\iff \dfrac{AF}{FB}\cdot\dfrac{BD}{DC}\cdot\dfrac{CE}{EA}=1$.

**What it says.** A product of three side-ratios equals $1$ exactly when the three cevians meet at a point.

**The move.** Reduce a concurrency question to one multiplicative equation — the dual of Menelaus.

**When it fires.** Proving cevians concurrent (medians, bisectors, altitudes). *Trigger:* "show $AD,BE,CF$ are concurrent."

**Micro-example.** Medians: each ratio is $1$, product $1$ — concurrent at the centroid.

**Watch for.** Product is $+1$ (unsigned form for internal cevians); use the trig form (D13) when angles are natural.

**Used in.** Blueprint §9.7 seed; P4 geometry *(provisional)*. **Neighbours.** → D04a, D03, D13, D12.

**Named proof.** Ratios of sub-triangle areas, or apply Menelaus twice — Coxeter & Greitzer, §3.1.

---

### D05 · Euler's Polyhedra Formula — Core

> For any convex polyhedron (or connected planar graph): $\;V-E+F=2$.

**What it says.** Vertices minus edges plus faces is always $2$ — a topological invariant.

**The move.** Tie three independently varying counts together with one equation, so any two determine the third — a counting invariant in the spirit of Chapter 1.

**When it fires.** Counting faces/edges/vertices; planarity arguments; map-colouring set-ups. *Trigger:* "count faces of a polyhedron / planar graph."

**Micro-example.** Cube: $V=8,E=12,F=6$, and $8-12+6=2$.

**Watch for.** Requires connectivity / sphere-topology (genus $0$); for a torus the constant is $0$.

**Used in.** Blueprint §9.7 seed; P2 Ch. 1 (invariance) *(provisional)*. **Neighbours.** → G17 (handshaking), G01.

**Named proof.** Induction on edges (remove one at a time), or a planar-graph argument — Aigner & Ziegler, *Proofs from THE BOOK*.

---

### D06 · Circle Inversion — Stretch

> Inversion in centre $O$, radius $r$ sends $P\mapsto P'$ on ray $OP$ with $OP\cdot OP'=r^2$; it maps lines/circles to lines/circles and preserves angles.

**What it says.** A transformation that turns the inside of a circle out, swapping lines and circles while keeping angles.

**The move.** Send a troublesome circle to a straight line (or a tangency to a parallelism), trivialising configurations full of circles.

**When it fires.** Many mutually tangent circles; problems where circles through a common point appear. *Trigger:* "invert about the common point."

**Micro-example.** Circles through the centre of inversion become straight lines.

**Watch for.** Choosing the centre well is the whole art; track where each object goes and back.

**Used in.** Blueprint §9.7 seed; P2 Ch. 15 slate *(provisional)*. **Neighbours.** → D19 (Möbius), D01, D17.

**Named proof.** Coordinate/complex computation $z\mapsto r^2/\bar z$ — Coxeter & Greitzer, §5.3.

---

### D07a · Law of Sines — Core

> $\dfrac{a}{\sin A}=\dfrac{b}{\sin B}=\dfrac{c}{\sin C}=2R$; area $K=\tfrac12ab\sin C=\dfrac{abc}{4R}$.

**What it says.** Each side over the sine of its opposite angle equals the circumdiameter.

**The move.** Convert between sides and angles of a triangle, introducing the circumradius $R$ as a unifying constant.

**When it fires.** Triangle solving with an angle–opposite-side pair; circumradius problems. *Trigger:* "given an angle and its opposite side."

**Micro-example.** $A=30^\circ,a=5\Rightarrow 2R=\tfrac{5}{\sin30^\circ}=10$, so $R=5$.

**Watch for.** The ambiguous (SSA) case can give two triangles.

**Used in.** P2 Ch. 7, 9 throughout *(provisional)*. **Neighbours.** → D07b, D18, D09.

**Named proof.** Drop an altitude, or use the inscribed-angle theorem on the circumcircle — standard.

---

### D07b · Law of Cosines — Core

> $a^2=b^2+c^2-2bc\cos A$.

**What it says.** A generalised Pythagoras carrying the angle's cosine as the correction term.

**The move.** Resolve a triangle from SSS or SAS data; convert an angle into the three side lengths and back.

**When it fires.** Two sides and the included angle, or all three sides. *Trigger:* "SAS or SSS triangle."

**Micro-example.** $b=c=1,A=60^\circ\Rightarrow a^2=1+1-2\cos60^\circ=1$, equilateral.

**Watch for.** Sign of $\cos A$ flags obtuse vs. acute; reduces to Pythagoras at $A=90^\circ$.

**Used in.** P2 Ch. 8 WE1 (triangle type from complex ratio) *(provisional)*. **Neighbours.** → D07a, D12 (Stewart), D18.

**Named proof.** Expand $|\,\vec{b}-\vec{c}\,|^2$ via the dot product, or project onto a side — standard.

---

### D07c · Tangent Addition Formula — Core

> $\tan(A\pm B)=\dfrac{\tan A\pm\tan B}{1\mp\tan A\tan B}$.

**What it says.** The tangent of a sum is a rational function of the individual tangents.

**The move.** Combine or split angles inside tangents — and, run backwards, motivates the Weierstrass substitution $t=\tan(x/2)$.

**When it fires.** Angle-sum tangent expressions; slopes/angle between lines; $\arctan$ telescoping. *Trigger:* "$\tan$ of a sum/difference of angles."

**Micro-example.** $\tan(45^\circ+30^\circ)=\dfrac{1+\tfrac{1}{\sqrt3}}{1-\tfrac{1}{\sqrt3}}=2+\sqrt3$.

**Watch for.** Undefined when the denominator vanishes (sum is $90^\circ$); sign pairing $\mp$.

**Used in.** P2 Ch. 7 (angle constraints), Ch. 5 WE3 (Weierstrass context) *(provisional)*. **Neighbours.** → F09 (Weierstrass), D07d, PR04, A06.

**Named proof.** Divide the sine addition formula by the cosine addition formula — standard.

---

### D07d · Product-to-Sum / Sum-to-Product Formulas — Core

> $2\sin A\cos B=\sin(A+B)+\sin(A-B)$; $\;2\cos A\cos B=\cos(A-B)+\cos(A+B)$; and the sum-to-product duals.

**What it says.** Products of sinusoids convert to sums, and sums to products.

**The move.** Switch a product (hard to sum) into a sum that telescopes, or a sum into a product that factors — the trig analogue of partial fractions.

**When it fires.** Summing trig series; factoring $\sin x\pm\sin y$; integrals of products of sinusoids. *Trigger:* "a product (or sum) of sines/cosines to simplify."

**Micro-example.** $\sin75^\circ-\sin15^\circ=2\cos45^\circ\sin30^\circ=\tfrac{\sqrt2}{2}$.

**Watch for.** Keep the $(A+B)$ vs. $(A-B)$ pairing straight; sign in cosine product formula.

**Used in.** P2 Ch. 7, 10 (trig products), Ch. 3 PP7 *(provisional)*. **Neighbours.** → D07c, A06 (telescoping), F04c.

**Named proof.** Add and subtract the cosine (resp. sine) addition formulas — standard.

---

### D08 · Complex Numbers as Geometry (De Moivre) — Core

> $(\cos\theta+i\sin\theta)^n=\cos n\theta+i\sin n\theta$; multiplication by $re^{i\theta}$ is rotation by $\theta$ and scaling by $r$.

**What it says.** Complex multiplication *is* rotation-and-scaling; powers rotate by multiples of the angle.

**The move.** Encode a planar configuration as complex numbers so that rotations, similarities, and regular polygons become one-line algebra.

**When it fires.** Equilateral/regular-polygon conditions; rotations about a point; nth-roots problems. *Trigger:* "rotate $90^\circ$/$60^\circ$" or "vertices of a regular polygon."

**Micro-example.** $A,B,C$ equilateral $\iff a+\omega b+\omega^2 c=0$ where $\omega=e^{2\pi i/3}$.

**Watch for.** Orientation of rotation (sign of $\theta$); pick a convenient origin.

**Used in.** P2 Ch. 8 WE1 (equilateral detection), PP6 (De Moivre, $z^3=-8$) *(provisional)*. **Neighbours.** → PR03, A15 (roots of unity), D17 (spiral similarity).

**Named proof.** Induction on $n$ from the angle-addition of complex multiplication — standard.

---

### D09 · Heron's Formula — Core

> $K=\sqrt{s(s-a)(s-b)(s-c)}$, $\;s=\tfrac{a+b+c}{2}$; in Ravi coordinates $K=\sqrt{xyz(x+y+z)}$.

**What it says.** A triangle's area from its three sides alone, no angle needed.

**The move.** Get area from side data directly — and, rewritten in Ravi variables, feed area into symmetric inequalities.

**When it fires.** Area from SSS; inequalities mixing area and sides. *Trigger:* "area given the three sides."

**Micro-example.** $13,14,15$: $s=21$, $K=\sqrt{21\cdot8\cdot7\cdot6}=84$.

**Watch for.** Numerical stability for thin triangles; ensure the sides actually form a triangle.

**Used in.** P2 Ch. 5 WE2, Ch. 9 PP2 *(provisional)*. **Neighbours.** → A17 (Ravi), D14 (Brahmagupta), D18.

**Named proof.** Law of Cosines for $\cos C$ substituted into $K=\tfrac12ab\sin C$ — standard.

---

### D10 · Nine-Point Circle — Stretch

> The three side-midpoints, three feet of the altitudes, and three Euler-point midpoints of $\triangle ABC$ lie on one circle of radius $R/2$.

**What it says.** Nine naturally-defined triangle points are concyclic.

**The move.** Replace nine separate points by membership in a single circle, collapsing several configuration facts into one.

**When it fires.** Configurations involving midpoints, altitude feet, and the orthocentre. *Trigger:* "midpoints and altitude feet appear together."

**Micro-example.** Its centre is the midpoint of the segment from the orthocentre to the circumcentre.

**Watch for.** The radius is exactly half the circumradius $R$; many associated centres lie on the Euler line.

**Used in.** P2 Ch. 2 geometry connections *(provisional)*. **Neighbours.** → D16 (Simson), D18, D11.

**Named proof.** Homothety of ratio $\tfrac12$ centred at the orthocentre — Coxeter & Greitzer, §1.8.

---

### D11 · Radical Axis — Core

> The locus of points of equal power w.r.t. two circles is a line $\perp$ to the line of centres; three circles give a common *radical centre*.

**What it says.** Equal-power points form a line; three circles' radical axes concur.

**The move.** Turn a "two circles" relationship into a single line — and concurrency/collinearity proofs into power computations.

**When it fires.** Two or three circles; common-chord problems; "show three lines concur." *Trigger:* "common chord / equal tangents to two circles."

**Micro-example.** For two intersecting circles, the radical axis is the line through their two intersection points.

**Watch for.** Power can be negative (inside the circle); axis exists even when circles do not intersect.

**Used in.** P2 Ch. 2, 3 duality connections *(provisional)*. **Neighbours.** → D01 (power of a point), D06.

**Named proof.** Subtract the two circle equations; the quadratic terms cancel, leaving a line — standard.

---

### D12 · Stewart's Theorem — Core

> Cevian $AD=d$ to $D$ on $BC$ with $BD=m,DC=n$: $\;b^2m+c^2n=a(d^2+mn)$ (where $a=m+n$). Mnemonic: "$man+dad=bmb+cnc$."

**What it says.** A relation among a cevian's length, the side it cuts, and the triangle's sides.

**The move.** Compute any cevian length (median, bisector) from side data without coordinates.

**When it fires.** Length of a median/bisector/arbitrary cevian. *Trigger:* "find the length of cevian $AD$."

**Micro-example.** Median to side $a$: set $m=n=\tfrac a2$ to get $m_a^2=\tfrac{2b^2+2c^2-a^2}{4}$.

**Watch for.** Keep $m,n$ on the correct sides; reduces to the median/bisector length formulas.

**Used in.** P2 Ch. 9 (metric relations) *(provisional)*. **Neighbours.** → D07b, D04b, D18.

**Named proof.** Law of Cosines on the two sub-triangles with supplementary angles at $D$ — Coxeter & Greitzer.

---

### D13 · Trigonometric Form of Ceva — Stretch

> $AD,BE,CF$ concurrent $\iff \dfrac{\sin\angle BAD}{\sin\angle DAC}\cdot\dfrac{\sin\angle CBE}{\sin\angle EBA}\cdot\dfrac{\sin\angle ACF}{\sin\angle FCB}=1$.

**What it says.** Ceva's concurrency condition, written in the angles the cevians make rather than the segments they cut.

**The move.** Prove concurrency when *angles* are the natural data (isogonals, bisectors), where length-Ceva is awkward.

**When it fires.** Isogonal cevians, angle bisectors, symmedians. *Trigger:* "cevians defined by angle conditions."

**Micro-example.** The three angle bisectors: each sine ratio is $1$, so they concur (the incenter).

**Watch for.** Directed angles for rigor; pairs of sines per vertex must be in the right order.

**Used in.** P2 Ch. 2 (angle/symmetry arguments) *(provisional)*. **Neighbours.** → D04b, D03, D07a.

**Named proof.** Convert each length ratio in Ceva (D04b) via the Law of Sines — standard.

---

### D14 · Brahmagupta's Formula — Core

> Cyclic quadrilateral with sides $a,b,c,d$: $\;K=\sqrt{(s-a)(s-b)(s-c)(s-d)}$, $\;s=\tfrac{a+b+c+d}{2}$.

**What it says.** The area of a cyclic quadrilateral from its four sides — Heron's formula's big sibling.

**The move.** Get maximal-area (cyclic) quadrilateral area from side data, and bound general quadrilaterals by it.

**When it fires.** Cyclic quadrilaterals; "maximise area for given sides" (the max is cyclic). *Trigger:* "area of a cyclic quadrilateral."

**Micro-example.** A square of side $s$: $K=\sqrt{(\tfrac{4s}{2}-s)^4}=s^2$ — recovering the obvious.

**Watch for.** Holds only for *cyclic* quadrilaterals (Bretschneider's formula is the general one).

**Used in.** P4 (cyclic-quad CEP design); P2 Ch. 20 (Analogy/Transfer) *(provisional)*. **Neighbours.** → D09 (Heron special case), D02, D18.

**Named proof.** Law of Cosines on both diagonals using supplementary cyclic angles — standard.

---

### D15 · Pole–Polar Duality — Core

> The polar of $P=(x_0,y_0)$ w.r.t. a conic is got by the "split-the-equation" rule (e.g. for $y^2=4ax$: $yy_0=2a(x+x_0)$); the focus's polar w.r.t. a parabola is its directrix.

**What it says.** Each point has a dual line (its polar) w.r.t. a conic, and vice versa.

**The move.** Swap a point-problem for a line-problem via projective duality, often turning "find a locus" into "find an envelope."

**When it fires.** Chord of contact from an external point; tangents; conic dualities. *Trigger:* "chord of contact / polar of a point."

**Micro-example.** The chord of contact of tangents from $P$ to a circle is exactly the polar of $P$.

**Watch for.** Conic-specific polar rule; pole and polar swap roles under duality.

**Used in.** P2 Ch. 8 ("the focus's polar w.r.t. a parabola is the directrix") *(provisional)*. **Neighbours.** → D20 (parametric conics), D11.

**Named proof.** Chord-of-contact computation, or harmonic-conjugate (projective) argument — Coxeter, *Projective Geometry*.

---

### D16 · Simson Line — Stretch

> The feet of the perpendiculars from a point $P$ to the sides of $\triangle ABC$ are collinear $\iff P$ lies on the circumcircle.

**What it says.** Three projections collapse onto one line exactly when the source point is on the circumcircle.

**The move.** Convert "is $P$ on the circumcircle?" into a collinearity, and vice versa — a concyclicity detector.

**When it fires.** Configurations with perpendicular feet; concyclicity proofs. *Trigger:* "drop perpendiculars to the three sides."

**Micro-example.** For $P$ a vertex, the Simson line degenerates to an altitude.

**Watch for.** Only circumcircle points give collinearity; the line's direction relates to $P$'s position.

**Used in.** P2 Ch. 2 geometry connections *(provisional)*. **Neighbours.** → D10, D17, D02.

**Named proof.** Cyclic-quadrilateral angle chase on the three pedal points — Coxeter & Greitzer, §2.5.

---

### D17 · Spiral Similarity — Stretch

> A rotation composed with a homothety about a fixed centre; in the complex plane $z\mapsto \alpha z+\beta$ with $\alpha\in\mathbb{C}^\times$. It maps any segment to any other segment.

**What it says.** The unique direct similarity carrying one segment onto another, realised by complex multiplication plus translation.

**The move.** Identify the hidden centre that maps one pair of points to another, dissolving "two similar triangles" into a single transformation.

**When it fires.** Two segments/triangles related by rotation+scaling; "common centre" points. *Trigger:* "$\triangle ABC\sim\triangle ADE$ — find the spiral centre."

**Micro-example.** The centre of the spiral similarity sending $AB\to CD$ is the second intersection of circles $(ABX)$ and $(CDX)$.

**Watch for.** Direct vs. opposite similarity; the centre lies on two specific circles.

**Used in.** P2 Ch. 8 geometry connections *(provisional)*. **Neighbours.** → D08, D19, D06.

**Named proof.** Realise as the complex map $z\mapsto\alpha z+\beta$ and read off centre/ratio — standard.

---

### D18 · Triangle Metric Relations ($r,R,s,K$ family) — Core

> $K=rs$, $\;R=\dfrac{abc}{4K}$, $\;r=4R\sin\tfrac A2\sin\tfrac B2\sin\tfrac C2$, $\;OI^2=R(R-2r)\Rightarrow R\ge2r$ (Euler).

**What it says.** Inradius, circumradius, semiperimeter, and area are bound by a web of identities, capped by Euler's $R\ge2r$.

**The move.** Translate freely among a triangle's metric quantities, so that whichever you are given yields the rest.

**When it fires.** Problems mixing $r,R,s,K$; proving triangle inequalities like $R\ge2r$. *Trigger:* "relate inradius and circumradius / area and perimeter."

**Micro-example.** Equilateral triangle: $R=2r$, the equality case of Euler's inequality.

**Watch for.** $R\ge2r$ holds for *all* triangles (not just acute); keep the identities' hypotheses straight.

**Used in.** P2 Ch. 9 PP6 (Euler $R\ge2r$), Ch. 5, 9 *(provisional)*. **Neighbours.** → D07a, D09, D14, A17.

**Named proof.** Trigonometric identities in the triangle; Euler's $OI^2=R(R-2r)$ for $R\ge2r$ — Coxeter & Greitzer, §2.

---

### D19 · Möbius Transformation — Stretch

> $z\mapsto\dfrac{az+b}{cz+d}$ with $ad-bc\ne0$; preserves the cross-ratio and the family of circles-and-lines; conformal on the Riemann sphere.

**What it says.** The fractional-linear maps of the extended complex plane, generated by inversions and similarities.

**The move.** Normalise three points to convenient positions ($0,1,\infty$) and exploit cross-ratio invariance — the most flexible conformal change of coordinates.

**When it fires.** Cross-ratio problems; mapping circles to lines; three-point normalisations. *Trigger:* "send these three points to $0,1,\infty$."

**Micro-example.** $z\mapsto\tfrac{1}{z}$ swaps inside and outside of the unit circle and fixes $\pm1$.

**Watch for.** $\infty$ is a genuine point here; $ad-bc\ne0$ is required for invertibility.

**Used in.** P2 Ch. 8 front-matter key gems *(provisional)*. **Neighbours.** → D06 (inversion is a special case), D17, D08.

**Named proof.** Factor into translations, dilations, and an inversion — Needham, *Visual Complex Analysis*, Ch. 3.

---

### D20 · Parametric Conic Properties — Core

> Parabola $(at^2,2at)$: focal chord $\iff t_1t_2=-1$; tangent $ty=x+at^2$; directrix $x=-a$. Ellipse $(a\cos\theta,b\sin\theta)$; semi-latus rectum $\ell=b^2/a$.

**What it says.** Conics in parametric form expose chord, tangent, and focal relations as clean conditions on the parameters.

**The move.** Replace messy $(x,y)$ conic algebra by one parameter per point, turning chord and tangent conditions into simple equations in $t$ or $\theta$.

**When it fires.** Chords, tangents, normals, focal properties of conics. *Trigger:* "a chord/tangent of the parabola/ellipse."

**Micro-example.** Tangents at $t_1,t_2$ on $y^2=4ax$ meet at $x=at_1t_2$; for a focal chord this is $-a$, the directrix.

**Watch for.** Parametrisation differs per conic; sign conventions for focus/directrix.

**Used in.** P2 Ch. 8 WE3 (tangent intersection at the directrix) *(provisional)*. **Neighbours.** → D15 (pole–polar), PR08.

**Named proof.** Substitute the parametrisation into the chord/tangent equations — standard.

---

# Cluster E — Sequences & Series

*Discrete and limiting processes: progressions, recurrences, generating functions, and convergence. These gems implement the* Recursion / Induction *and* Linearisation *archetypes — they let you describe an infinite process by a finite rule.*

---

### E01 · AP / GP Toolkits — Core

> AP: $a_n=a+(n-1)d$, $S_n=\tfrac n2(a+l)$. GP: $a_n=ar^{n-1}$, $S_n=\dfrac{a(r^n-1)}{r-1}$, $S_\infty=\dfrac{a}{1-r}$ ($|r|<1$).

**What it says.** Closed forms for the two fundamental progressions and their sums.

**The move.** Replace term-by-term addition with a closed formula — the first compression a solver reaches for in any linear or geometric pattern.

**When it fires.** Any arithmetic/geometric pattern; AGP; telescoping products. *Trigger:* "constant difference (AP) or constant ratio (GP)."

**Micro-example.** $\prod_{k=1}^{n}\big(1+\tfrac1k\big)=\dfrac{n+1}{1}$ telescopes a product into a ratio.

**Watch for.** $S_\infty$ needs $|r|<1$; index conventions (first term $a$ vs. $a_0$).

**Used in.** Blueprint §9.7; P2 Ch. 18, 6 *(provisional)*. **Neighbours.** → E10, A06 (telescoping), PR07.

**Named proof.** Pair-and-add (Gauss) for the AP sum; multiply-by-$r$-and-subtract for the GP sum — standard.

---

### E02 · Fibonacci Sequence & Golden Ratio — Core

> $F_{n+2}=F_{n+1}+F_n$; Binet: $F_n=\dfrac{\varphi^n-\psi^n}{\sqrt5}$ with $\varphi=\tfrac{1+\sqrt5}{2}$, $\psi=\tfrac{1-\sqrt5}{2}$.

**What it says.** The Fibonacci numbers have a closed form built from the golden ratio and its conjugate.

**The move.** Convert a recursive sequence into an exponential closed form, exposing growth rate and identities at a glance.

**When it fires.** Fibonacci/Lucas problems; growth-rate estimates; continued-fraction connections. *Trigger:* "$a_{n}=a_{n-1}+a_{n-2}$."

**Micro-example.** $F_n/F_{n-1}\to\varphi$ as $n\to\infty$.

**Watch for.** $\psi^n\to0$ so $F_n\approx\varphi^n/\sqrt5$ (round to nearest integer); Binet needs $\sqrt5$ irrational arithmetic.

**Used in.** Blueprint §9.7; P3 PP3.1 (IMO 1981) *(provisional)*. **Neighbours.** → A13 (Cassini), E10 (characteristic equation), PR07.

**Named proof.** Solve the characteristic equation $r^2=r+1$ and fit initial values — Vajda, *Fibonacci & Lucas Numbers*.

---

### E03 · Generating Functions & Formal Power Series — Stretch

> Encode $(a_n)$ as $A(x)=\sum_{n\ge0}a_nx^n$ (OGF) or $\sum a_n\tfrac{x^n}{n!}$ (EGF); recurrences become algebraic equations; $[x^n]A(x)$ extracts $a_n$.

**What it says.** A whole sequence is stored as one power series, on which algebra mirrors combinatorial operations.

**The move.** Turn a recurrence or counting problem into an *algebra* problem — solve for $A(x)$ in closed form, then read off coefficients.

**When it fires.** Linear recurrences; counting with constraints; convolution identities. *Trigger:* "let $A(x)=\sum a_nx^n$."

**Micro-example.** Fibonacci: $A(x)=\dfrac{x}{1-x-x^2}$, whose coefficients are the $F_n$.

**Watch for.** OGF vs. EGF choice (products mean different things); convergence is irrelevant for *formal* manipulation.

**Used in.** P2 Ch. 8 domain translation Form IV *(provisional)*. **Neighbours.** → E10, E04/E11, G05.

**Named proof.** Formal-power-series ring algebra (no convergence needed) — Wilf, *generatingfunctionology*.

---

### E04 · Stirling Numbers (First & Second Kind) — Stretch

> $S(n,k)$ = set partitions into $k$ blocks; $s(n,k)$ = permutations with $k$ cycles; $x^n=\sum_k S(n,k)\,x^{\underline{k}}$; surjections $[n]\to[k]$ number $k!\,S(n,k)$.

**What it says.** The two families converting between ordinary powers and falling factorials, counting partitions and cycles.

**The move.** Translate between "powers" and "falling factorials," and count partitions/surjections in closed combinatorial form.

**When it fires.** Counting set partitions, surjections, permutation cycles; power-to-factorial conversions. *Trigger:* "partition a set into blocks" or "count surjections."

**Micro-example.** Surjections $[4]\to[2]$: $2!\,S(4,2)=2\cdot7=14$.

**Watch for.** Two kinds with different recurrences; signed vs. unsigned first-kind.

**Used in.** Blueprint §9.7; P2 Ch. 13 (surjection counting) *(provisional)*. **Neighbours.** → E11 (Bell), G02 (inclusion–exclusion), G14.

**Named proof.** Recurrence $S(n,k)=kS(n-1,k)+S(n-1,k-1)$ by last-element placement — Stanley, *Enumerative Combinatorics*, Vol. 1.

---

### E05 · Catalan Numbers — Core

> $C_n=\dfrac{1}{n+1}\dbinom{2n}{n}=\dbinom{2n}{n}-\dbinom{2n}{n+1}$; counts Dyck paths, triangulations, balanced parentheses, full binary trees.

**What it says.** One number sequence counts a dozen seemingly unrelated families of objects.

**The move.** Recognise a "balanced/non-crossing" structure and collapse the count to a Catalan number, proved cleanly by André's reflection.

**When it fires.** Balanced brackets, lattice paths under a diagonal, polygon triangulations, non-crossing structures. *Trigger:* "count the ways that never go below / never cross."

**Micro-example.** Triangulations of a convex hexagon: $C_4=14$.

**Watch for.** Off-by-one in $n$; the reflection subtraction form is the quick proof.

**Used in.** P2 Ch. 15 WE3 (André reflection) *(provisional)*. **Neighbours.** → G10 (ballot/reflection), G03 (bijections), A05.

**Named proof.** André's reflection principle on Dyck paths — Stanley, *Enumerative Combinatorics*, Vol. 2.

---

### E06 · Harmonic Series & Euler–Mascheroni Constant — Core

> $H_n=\sum_{k=1}^n\tfrac1k$; $\;\ln(n+1)<H_n<1+\ln n$; $\;\gamma=\lim_{n\to\infty}(H_n-\ln n)\approx0.5772$.

**What it says.** The harmonic sum diverges, but only logarithmically, trailing $\ln n$ by the constant $\gamma$.

**The move.** Bound a sum by an integral (and vice versa), pinning the growth rate of $H_n$ between two logarithms.

**When it fires.** Estimating $\sum 1/k$; divergence rates; integral comparison. *Trigger:* "$\sum 1/k$ or its growth."

**Micro-example.** $H_n\approx\ln n+\gamma$, so $H_{100}\approx4.61+0.58=5.19$.

**Watch for.** Diverges (no finite sum); the bounds come from $\int\tfrac1x$.

**Used in.** P2 Ch. 6 WE2 *(provisional)*. **Neighbours.** → E08 (comparison test), F04c (the integral $\int 1/x$).

**Named proof.** Integral comparison $\int_1^{n+1}\tfrac{dx}{x}<H_n<1+\int_1^{n}\tfrac{dx}{x}$ — Apostol, *Calculus*, Vol. 1.

---

### E07 · Wallis Product & Reduction Formulas — Core

> $I_n=\int_0^{\pi/2}\sin^n x\,dx$ satisfies $I_n=\tfrac{n-1}{n}I_{n-2}$; e.g. $I_5=\tfrac{8}{15}$, $I_6=\tfrac{5\pi}{32}$; Wallis: $\tfrac\pi2=\prod_k\tfrac{4k^2}{4k^2-1}$.

**What it says.** Powers of sine integrate via a downward recursion, yielding the Wallis product for $\pi$.

**The move.** Replace integrating $\sin^n$ directly by a recursion that drops the exponent by $2$ each step — integration by parts made systematic.

**When it fires.** $\int\sin^n,\;\int\cos^n,\;\int\sin^m\cos^n$; products approximating $\pi$. *Trigger:* "integral of a high power of sine/cosine."

**Micro-example.** $I_4=\tfrac34\cdot\tfrac12\cdot\tfrac\pi2=\tfrac{3\pi}{16}$.

**Watch for.** Parity of $n$ decides whether a $\tfrac\pi2$ factor survives; limits matter.

**Used in.** P2 Ch. 18 WE3 (Wallis IBP recurrence) *(provisional)*. **Neighbours.** → F04b (by parts), E06.

**Named proof.** Integration by parts on $\int\sin^n x\,dx$ giving the downward recursion — standard.

---

### E08 · Convergence Tests — Core

> Comparison; ratio (D'Alembert) $\tfrac{a_{n+1}}{a_n}\to L$; root (Cauchy) $a_n^{1/n}\to L$ (converge if $L<1$); Leibniz: an alternating series with terms $\downarrow0$ converges, error $<$ first omitted term.

**What it says.** A toolkit deciding whether an infinite series converges.

**The move.** Certify convergence (and bound the tail) before manipulating a series — the licence to treat an infinite sum as a number.

**When it fires.** Any infinite series; interval of convergence of a power series; tail estimates. *Trigger:* "does $\sum a_n$ converge?"

**Micro-example.** $\sum \tfrac{1}{n!}$ converges by the ratio test ($\tfrac{a_{n+1}}{a_n}=\tfrac{1}{n+1}\to0$).

**Watch for.** Ratio/root tests are inconclusive at $L=1$; alternating-series bound needs monotone decrease.

**Used in.** P2 Ch. 6 WE2 (alternating series tail) *(provisional)*. **Neighbours.** → E06, F05 (Taylor remainder), E09.

**Named proof.** Comparison with a geometric series (ratio/root); alternating-series sign argument — Rudin, *Principles of Mathematical Analysis*, Ch. 3.

---

### E09 · Abel Summation / Summation by Parts — Stretch

> $\displaystyle\sum_{k=1}^{n}a_kb_k=A_nb_{n}-\sum_{k=1}^{n-1}A_k(b_{k+1}-b_k)$, where $A_k=a_1+\cdots+a_k$.

**What it says.** The discrete analogue of integration by parts, trading a sum of products for a sum involving partial sums and differences.

**The move.** Move the "hard" factor onto its partial sums and the "smooth" factor onto its differences — taming sums where one factor telescopes or is monotone.

**When it fires.** Sums $\sum a_kb_k$ where $\sum a_k$ is known and $b_k$ is monotone; Dirichlet/Abel convergence tests. *Trigger:* "$\sum a_kb_k$ with one factor summable, the other monotone."

**Micro-example.** Bounds $\sum \tfrac{\sin k}{k}$ by summing $\sin k$ (bounded partial sums) against $\tfrac1k\downarrow0$.

**Watch for.** Track the boundary term $A_nb_n$; index ranges in the difference.

**Used in.** Olympiad series arguments *(provisional)*. **Neighbours.** → A06 (telescoping), F04b (IBP analogue), E08.

**Named proof.** Rearrange the double sum $\sum a_kb_k$ using partial sums $A_k$ — Apostol, *Introduction to Analytic Number Theory*, §4.

---

### E10 · Recurrence Relations (Characteristic Equation) — Core

> $a_n=p\,a_{n-1}+q\,a_{n-2}$ has characteristic equation $r^2=pr+q$; distinct roots $\Rightarrow a_n=Ar_1^n+Br_2^n$; repeated root $r$ $\Rightarrow a_n=(A+Bn)r^n$.

**What it says.** Linear recurrences solve like linear ODEs — through the roots of a characteristic polynomial.

**The move.** Convert a recursive definition into a closed exponential form, fixing constants from initial values.

**When it fires.** Any linear recurrence with constant coefficients (Fibonacci, tilings, etc.). *Trigger:* "$a_n$ defined from previous terms linearly."

**Micro-example.** $a_n=3a_{n-1}-2a_{n-2}$: roots $1,2$, so $a_n=A+B\cdot2^n$.

**Watch for.** Repeated roots need the $n\,r^n$ term; complex roots give oscillation (trig form).

**Used in.** P2 Ch. 6 WE3, Ch. 18 *(provisional)*. **Neighbours.** → E02 (Fibonacci case), E03 (generating-function alternative), F11 (ODE analogue).

**Named proof.** Substitute the ansatz $a_n=r^n$ to get the characteristic polynomial — standard.

---

### E11 · Bell Numbers & Set-Partition Theory — Stretch

> $B_n=\sum_{k=0}^{n}S(n,k)$ = number of partitions of an $n$-set; recurrence $B_{n+1}=\sum_k\binom{n}{k}B_k$; EGF $e^{e^x-1}$.

**What it says.** The Bell number counts *all* set partitions, summing Stirling numbers over block-count.

**The move.** Count "all ways to partition" in one stroke, via a recurrence built on "which block contains the last element."

**When it fires.** Total number of set partitions; equivalence-relation counts. *Trigger:* "number of ways to partition a set (any number of blocks)."

**Micro-example.** $B_3=5$: the partitions of $\{1,2,3\}$.

**Watch for.** $B_n$ sums over all $k$ (unlike a single $S(n,k)$); the recurrence convolves with binomials.

**Used in.** Completes E04 (Stirling); partition-lattice combinatorics *(provisional)*. **Neighbours.** → E04, G02, G03.

**Named proof.** Last-element-block recurrence $B_{n+1}=\sum_k\binom{n}{k}B_k$ — Stanley, *Enumerative Combinatorics*, Vol. 1.

---

# Cluster F — Calculus

*The analysis of change, accumulation, and limits. These gems carry the* Linearisation *and* Existence / Uniqueness *archetypes — they turn local information (a derivative, a continuity) into global conclusions (an extremum, a root, a fixed point).*

---

### F01 · Mean Value Theorem / Rolle's Theorem — Core

> Rolle: $f$ continuous on $[a,b]$, differentiable on $(a,b)$, $f(a)=f(b)$ $\Rightarrow\exists c:f'(c)=0$. MVT: $\exists c:f'(c)=\dfrac{f(b)-f(a)}{b-a}$.

**What it says.** Somewhere inside an interval, the instantaneous rate equals the average rate.

**The move.** Promote *global* information (two endpoint values) into the *existence* of a point with a prescribed derivative — the workhorse existence theorem of calculus.

**When it fires.** Existence of a root of $f'$; bounding $f$ from its derivative; "exactly one solution" arguments. *Trigger:* "show some $c$ has $f'(c)=\cdots$."

**Micro-example.** $|\sin x-\sin y|\le|x-y|$, since $|\cos c|\le1$ by MVT.

**Watch for.** Needs continuity on $[a,b]$ *and* differentiability on $(a,b)$; gives existence, not the value of $c$.

**Used in.** Blueprint §9.7; P2 Ch. 11 (existence/uniqueness) *(provisional)*. **Neighbours.** → F02, F05 (Taylor remainder), PR13.

**Named proof.** Rolle from the extreme-value theorem; MVT by tilting to a chord — Rudin, *Principles of Mathematical Analysis*, Ch. 5.

---

### F02 · Intermediate Value Theorem (IVT) — Core

> $f$ continuous on $[a,b]$ and $f(a)<y<f(b)$ $\Rightarrow\exists c\in(a,b):f(c)=y$.

**What it says.** A continuous function attains every value between two of its values.

**The move.** Guarantee a root by a *sign change* — the simplest existence proof, requiring no formula for the root.

**When it fires.** "Show the equation has a solution"; root-existence; 1-D fixed points. *Trigger:* "a continuous function changes sign."

**Micro-example.** $x=\cos x$ has a solution since $g(x)=x-\cos x$ has $g(0)<0<g(1)$.

**Watch for.** Continuity is essential; gives existence, not uniqueness or location.

**Used in.** Blueprint §9.7; P2 Ch. 11 WE3 (1-D Brouwer via IVT) *(provisional)*. **Neighbours.** → F06 (fixed points), F01.

**Named proof.** Completeness: take the supremum of $\{x:f(x)<y\}$ — Rudin, *Principles*, Ch. 4.

---

### F03 · L'Hôpital's Rule — Core

> For $\tfrac00$ or $\tfrac{\infty}{\infty}$: $\;\lim\dfrac{f}{g}=\lim\dfrac{f'}{g'}$, when the right limit exists.

**What it says.** Indeterminate quotient limits can be evaluated by differentiating top and bottom.

**The move.** Convert a stuck quotient limit into a (hopefully simpler) derivative quotient, repeating as needed.

**When it fires.** $\tfrac00$ or $\tfrac\infty\infty$ limits; after rewriting $0\cdot\infty$, $\infty-\infty$, $1^\infty$ into a quotient. *Trigger:* "the limit is indeterminate $\tfrac00$."

**Micro-example.** $\lim_{x\to0}\dfrac{1-\cos x}{x^2}=\lim\dfrac{\sin x}{2x}=\dfrac12$ (two applications).

**Watch for.** Only for genuine indeterminacies; verify the new limit exists; Taylor series is often faster.

**Used in.** P2 Ch. 6 WE1 (two sequential applications) *(provisional)*. **Neighbours.** → F05 (Taylor alternative), PR11.

**Named proof.** The Cauchy (generalised) mean value theorem — Rudin, *Principles*, Ch. 5.

---

### F04a · Integration by Substitution — Core

> $\displaystyle\int f(g(x))g'(x)\,dx=\int f(u)\,du$ with $u=g(x)$.

**What it says.** The reverse chain rule: a composite-with-its-derivative integrates by renaming.

**The move.** Re-coordinate an integral so a messy integrand becomes standard — the first technique to try on any non-elementary-looking integral.

**When it fires.** An inner function and (a multiple of) its derivative both appear. *Trigger:* "I see $g(x)$ and $g'(x)$ together."

**Micro-example.** $\int 2x\,e^{x^2}dx=e^{x^2}+C$ with $u=x^2$.

**Watch for.** Change the limits when the integral is definite; the $du$ must match up to a constant.

**Used in.** Blueprint §9.7; Ch. 5 WE3 (Weierstrass is a named special case) *(provisional)*. **Neighbours.** → F09 (Weierstrass), F04b, F04c.

**Named proof.** The chain rule read backwards, with the Fundamental Theorem of Calculus — Apostol, *Calculus*, Vol. 1.

---

### F04b · Integration by Parts — Core

> $\displaystyle\int u\,dv=uv-\int v\,du$; choose $u$ by ILATE (Inverse-trig, Log, Algebraic, Trig, Exponential).

**What it says.** The reverse product rule, trading one integral for an (easier) one.

**The move.** Differentiate the awkward factor and integrate the friendly one — repeatedly, to build reduction formulas.

**When it fires.** Products of unlike functions ($x e^x$, $x\ln x$, $e^x\sin x$); reduction formulas. *Trigger:* "a product of a polynomial/log with a trig/exponential."

**Micro-example.** $\int x e^x dx=xe^x-\int e^x dx=(x-1)e^x+C$.

**Watch for.** ILATE picks $u$; cyclic cases ($\int e^x\sin x$) require solving for the integral.

**Used in.** P2 Ch. 18 WE3 (Wallis recurrence) *(provisional)*. **Neighbours.** → E07 (Wallis), B14 (integral Cauchy–Schwarz), F04a.

**Named proof.** The product rule integrated over $[a,b]$ — Apostol, *Calculus*, Vol. 1.

---

### F04c · Standard Integration Forms — Core

> $\displaystyle\int\frac{dx}{x^2+a^2}=\frac1a\arctan\frac xa$; $\;\int\frac{dx}{\sqrt{a^2-x^2}}=\arcsin\frac xa$; plus $\int x^n,\int e^x,\int\sec x$, etc. — the memorised toolkit.

**What it says.** The canonical antiderivatives every solver carries in memory.

**The move.** Pattern-match an integrand to a known form, so substitution/parts only need reduce *to* a standard form, not all the way to first principles.

**When it fires.** Any integral; the target shape after manipulation. *Trigger:* "reduce to $\frac{1}{x^2+a^2}$ / $\frac{1}{\sqrt{a^2-x^2}}$ form."

**Micro-example.** $\int\dfrac{dx}{x^2+4}=\tfrac12\arctan\tfrac x2+C$.

**Watch for.** Complete the square to reach these forms; mind the constant $a$.

**Used in.** JEE Advanced integration; derivable from F04a+F04b+A11 *(provisional)*. **Neighbours.** → A11 (partial fractions), F04a, F04b, PR12.

**Named proof.** Differentiate the claimed antiderivative to recover the integrand — standard.

---

### F05 · Taylor / Maclaurin Series — Core

> $f(x)=\displaystyle\sum_{n\ge0}\frac{f^{(n)}(a)}{n!}(x-a)^n$; remainder $R_n=\dfrac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}$.

**What it says.** A smooth function equals its polynomial expansion plus a controllable remainder.

**The move.** Replace a function locally by a polynomial — linearisation is just the degree-$1$ truncation — turning limits, approximations, and inequalities into polynomial algebra.

**When it fires.** Limits ($\tfrac00$), approximations, inequality proofs near a point, estimating error. *Trigger:* "expand near $x=a$" or a stubborn limit.

**Micro-example.** $e^x\approx1+x+\tfrac{x^2}{2}$; so $\lim_{x\to0}\tfrac{e^x-1-x}{x^2}=\tfrac12$.

**Watch for.** Convergence radius; the remainder must be controlled for rigorous bounds.

**Used in.** Blueprint §9.7; P2 Ch. 6 (Linearisation = first Taylor term) *(provisional)*. **Neighbours.** → F03, F08, E08.

**Named proof.** Repeated integration by parts, or the Cauchy form of the remainder — Rudin, *Principles*, Ch. 5.

---

### F06 · Fixed-Point Theorems (Banach + 1-D Brouwer) — Stretch

> Banach: a contraction $f$ ($|f(x)-f(y)|\le k|x-y|$, $k<1$) on a complete space has a unique fixed point, reached by iteration. Brouwer (1-D): a continuous self-map of $[a,b]$ has a fixed point.

**What it says.** Under contraction (unique) or mere continuity on an interval (existence), $f(x)=x$ has a solution.

**The move.** Convert "solve $f(x)=x$" into either an iteration that provably converges (Banach) or a sign-change existence (Brouwer via IVT).

**When it fires.** Iterative schemes; existence of equilibria; "$f(x)=x$ has a solution." *Trigger:* "iterate $x_{n+1}=f(x_n)$" or "self-map of an interval."

**Micro-example.** $x_{n+1}=\cos x_n$ converges to the Dottie number (contraction near the fixed point).

**Watch for.** Banach needs a genuine contraction ($k<1$) and completeness; Brouwer 1-D gives existence only.

**Used in.** P2 Ch. 11 WE3 (1-D Brouwer), PP7 (Banach/Dottie) *(provisional)*. **Neighbours.** → F02 (IVT), F01.

**Named proof.** Banach: the iterates form a Cauchy sequence in a complete space; Brouwer-1D via IVT on $g=f-\mathrm{id}$ — Rudin, *Principles*, Ch. 9 / Ch. 4.

---

### F07 · Differentiation Under the Integral Sign — Core

> $\dfrac{d}{dt}\displaystyle\int_{a(t)}^{b(t)}f(x,t)\,dx=\int_{a(t)}^{b(t)}\frac{\partial f}{\partial t}\,dx+f(b,t)b'(t)-f(a,t)a'(t)$ (Leibniz rule).

**What it says.** You may differentiate an integral with respect to a parameter, with boundary-correction terms.

**The move.** Introduce a parameter into a hard integral, differentiate to get an easy one, then integrate back — Feynman's trick.

**When it fires.** A definite integral resisting standard methods but generalisable by a parameter; variable limits. *Trigger:* "introduce a parameter $t$ and differentiate."

**Micro-example.** $I(t)=\int_0^1 x^t dx=\tfrac{1}{t+1}$; differentiating gives $\int_0^1 x^t\ln x\,dx=-\tfrac{1}{(t+1)^2}$.

**Watch for.** Justify the interchange (uniform convergence); do not forget boundary terms with variable limits.

**Used in.** P2 Ch. 12 (extremal/optimisation) *(provisional)*. **Neighbours.** → F04b, F12.

**Named proof.** Difference quotient under the integral with dominated/uniform convergence — Protter & Morrey, *A First Course in Real Analysis*.

---

### F08 · Analytic Inequalities from Linearisation — Core

> $\ln(1+x)\le x$; $\;\sin x\le x$ ($x\ge0$); $\;e^x\ge1+x$ — all from convexity/concavity (tangent- or chord-line bounds).

**What it says.** Smooth functions are bounded by their tangent lines (convex) or chords (concave).

**The move.** Replace a transcendental function by a linear bound to crack an inequality or estimate — the analytic face of Bernoulli (B12).

**When it fires.** Inequalities mixing $\ln,\exp,\sin$ with polynomials; tail/limit estimates. *Trigger:* "bound $\ln(1+x)$ or $e^x$ by a line."

**Micro-example.** $\tfrac1n>\ln\!\big(1+\tfrac1n\big)$, used to bound harmonic-vs-log gaps.

**Watch for.** Direction depends on convex (above tangent) vs. concave (below tangent); valid range of $x$.

**Used in.** P2 Ch. 6 WE2 *(provisional)*. **Neighbours.** → B12 (Bernoulli), F05 (Taylor), B03 (Jensen).

**Named proof.** Tangent-line bound from the sign of $f''$ (convexity/concavity) — standard.

---

### F09 · Weierstrass Substitution — Core

> $t=\tan\tfrac x2$: $\;\sin x=\dfrac{2t}{1+t^2},\;\cos x=\dfrac{1-t^2}{1+t^2},\;dx=\dfrac{2\,dt}{1+t^2}$.

**What it says.** The half-angle tangent rationalises every trigonometric integral.

**The move.** Convert a rational-in-$\sin,\cos$ integrand into a rational function of $t$ — which partial fractions then finish.

**When it fires.** $\int R(\sin x,\cos x)\,dx$ for rational $R$. *Trigger:* "a rational function of sine and cosine."

**Micro-example.** $\int\dfrac{dx}{1+\sin x}$ becomes $\int\dfrac{2\,dt}{(1+t)^2}$.

**Watch for.** Can introduce removable issues at $x=\pi$; sometimes a simpler substitution beats it.

**Used in.** P2 Ch. 5 WE3 (Joshi Ch. 18 Comment 8, answer $\ln 2$) *(provisional)*. **Neighbours.** → F04a, A11, D07c.

**Named proof.** Substitute the half-angle identities and verify $dx=\tfrac{2\,dt}{1+t^2}$ — standard.

---

### F10 · Cauchy Functional Equation — Stretch

> $f(x+y)=f(x)+f(y)$ with any regularity (continuity, monotonicity, or boundedness on an interval) $\Rightarrow f(x)=cx$.

**What it says.** Additivity plus mild regularity forces linearity; without regularity, pathological solutions exist (via a Hamel basis).

**The move.** Pin down an unknown function from a structural equation — the prototype of all functional-equation problems.

**When it fires.** A functional equation reducible to additivity/multiplicativity; "find all $f$ with …". *Trigger:* "$f(x+y)=f(x)+f(y)$" or a variant.

**Micro-example.** $f(x+y)=f(x)f(y)$ with continuity gives $f(x)=a^x$ (take logs to reach Cauchy).

**Watch for.** State the regularity you use; without it, uniqueness fails (Axiom of Choice pathologies).

**Used in.** P3 Ch. 6 Case 5 (Substitution + Existence + Invariance) *(provisional)*. **Neighbours.** → F02, G16 (existence flavour), PR01.

**Named proof.** Extend $\mathbb{Q}$-linearity, then use regularity to pass to $\mathbb{R}$ — Aczél, *Lectures on Functional Equations*.

---

### F11 · ODE Toolkit — Core

> Separable $\tfrac{dy}{dx}=f(x)g(y)$; linear $\tfrac{dy}{dx}+P(x)y=Q(x)$ via $\mu=e^{\int P\,dx}$; Bernoulli $y'=P y+Q y^n$ linearised by $u=y^{1-n}$.

**What it says.** Three solvable first-order ODE forms and the substitution that linearises the nonlinear one.

**The move.** Recognise which of the three solvable forms a differential equation fits, then apply its closed recipe.

**When it fires.** First-order ODEs; growth/decay models; Bernoulli-type nonlinearities. *Trigger:* "$\tfrac{dy}{dx}=\cdots$."

**Micro-example.** $y'+y=e^x$: $\mu=e^x$, $(e^xy)'=e^{2x}$, $y=\tfrac12e^x+Ce^{-x}$.

**Watch for.** Identify the form first; Bernoulli's substitution $u=y^{1-n}$ is the key trick.

**Used in.** P2 Ch. 5 PP5 (Bernoulli), Ch. 6 WE3 *(provisional)*. **Neighbours.** → E10 (discrete analogue), F04a, PR15.

**Named proof.** Each form solved by separation / integrating factor, verified by differentiation — Tenenbaum & Pollard, *Ordinary Differential Equations*.

---

### F12 · Lagrange Multipliers / Constrained Optimisation — Core

> Extremise $f$ subject to $g=0$: at an extremum $\nabla f=\lambda\nabla g$; with second-order (bordered-Hessian) conditions to classify.

**What it says.** At a constrained extremum, the gradients of objective and constraint are parallel.

**The move.** Convert a constrained optimisation into a system of equations (gradients + constraint), the calculus counterpart to AM–GM's symmetric-point insight.

**When it fires.** Optimise $f$ under a constraint when symmetry/AM–GM do not obviously apply. *Trigger:* "maximise $f$ subject to $g=0$."

**Micro-example.** Max of $xy$ with $x+y=s$: $\nabla(xy)=\lambda\nabla(x+y)$ gives $x=y=\tfrac s2$ (agreeing with AM–GM).

**Watch for.** Finds critical points only — check boundaries and classify; multiple constraints need multiple $\lambda$'s.

**Used in.** P2 Ch. 12 (extremal principles) *(provisional)*. **Neighbours.** → B01 (often a cleaner route), F07, PR13.

**Named proof.** At a constrained extremum the gradients align (implicit function theorem) — Rudin, *Principles*, Ch. 9.

---

# Cluster G — Combinatorics

*Counting, existence, and structure in finite sets and graphs. These gems are the executable core of the* Combinatorial Principles *and* Extremal *archetypes — and the home of the deepest "exists without constructing" arguments in the book.*

---

### G01 · Pigeonhole Principle — Core

> $n+1$ objects in $n$ boxes $\Rightarrow$ some box holds $\ge2$; generally, $kn+1$ objects $\Rightarrow$ some box holds $\ge k+1$.

**What it says.** You cannot distribute more objects than boxes without doubling up somewhere.

**The move.** Force the *existence* of a collision or repetition without ever finding it — the simplest existence proof in mathematics.

**When it fires.** "Show two of them are equal/close/share a property"; existence among finitely many cases. *Trigger:* "more objects than categories."

**Micro-example.** Among any $13$ people, two share a birth month ($13>12$).

**Watch for.** Designing the right boxes is the whole problem; the generalised form for $\ge k+1$.

**Used in.** Blueprint §9.7; P3 Ch. 5 PP5.1, PP5.4; Ch. 6 CS#1 (Erdős–Szekeres) *(provisional)*. **Neighbours.** → G09 (Ramsey), G16, G17.

**Named proof.** Contradiction: if every box held $\le k$, the total would be $\le kn$ — Aigner & Ziegler, *Proofs from THE BOOK*.

---

### G02 · Inclusion–Exclusion Principle — Core

> $\big|\bigcup A_i\big|=\sum|A_i|-\sum|A_i\cap A_j|+\cdots+(-1)^{n+1}|A_1\cap\cdots\cap A_n|$.

**What it says.** Count a union by adding singles, subtracting overlaps, re-adding triple overlaps, and so on.

**The move.** Convert a hard "count the union / count those with no bad property" into a signed sum of easy intersection counts.

**When it fires.** Counting with "at least one" or "none of" conditions; surjections, derangements, coprime counts. *Trigger:* "count elements avoiding all of several properties."

**Micro-example.** Integers in $[1,100]$ divisible by $2$ or $3$: $50+33-16=67$.

**Watch for.** The alternating signs; intersections must be genuinely easier to count.

**Used in.** Blueprint §9.7; P2 Ch. 13 WE2 (surjections), Ch. 14 *(provisional)*. **Neighbours.** → G14 (derangements), E04 (Stirling), A05.

**Named proof.** Indicator-function expansion / binomial sign sum — Stanley, *Enumerative Combinatorics*, Vol. 1.

---

### G03 · Double Counting / Bijection Principle — Core

> Count one set two ways to get an identity; or exhibit a bijection $\varphi:A\to B$ to conclude $|A|=|B|$.

**What it says.** If two expressions count the same thing, they are equal; if two sets biject, they are equinumerous.

**The move.** Prove an identity or an equality of counts *structurally*, with no algebra — the gold standard of combinatorial proof.

**When it fires.** Proving a combinatorial identity; "show these two quantities are equal." *Trigger:* "count the same configuration two different ways."

**Micro-example.** $\sum_{v}\deg(v)=2|E|$ counts edge-endpoints two ways (this is G17).

**Watch for.** The bijection must be genuinely well-defined and invertible; "obvious" maps can miss elements.

**Used in.** Blueprint §9.7; P2 Ch. 13, 15 throughout *(provisional)*. **Neighbours.** → G17, A12 (Vandermonde), E05 (Catalan).

**Named proof.** Count a chosen set two ways, or give an explicit bijection and its inverse — Aigner & Ziegler.

---

### G04 · Linearity of Expectation — Core

> $E[X_1+\cdots+X_n]=E[X_1]+\cdots+E[X_n]$, **regardless of dependence**.

**What it says.** Expectation of a sum is the sum of expectations — always, even for dependent variables.

**The move.** Decompose a complicated random count into indicator variables, expect each trivially, and add — sidestepping all dependence.

**When it fires.** "Expected number of …"; counting via averaging; existence by expectation. *Trigger:* "expected count of events $\Rightarrow$ sum of indicator probabilities."

**Micro-example.** Expected fixed points of a random permutation of $[n]$: $n\cdot\tfrac1n=1$.

**Watch for.** Independence is *not* needed (its great strength); variance does *not* share this property.

**Used in.** Blueprint §9.7; P2 Ch. 13 PP3(b) *(provisional)*. **Neighbours.** → G16 (probabilistic method), PR17, G14.

**Named proof.** Linearity of the sum/integral defining expectation — Alon & Spencer, *The Probabilistic Method*, Ch. 2.

---

### G05 · Stars and Bars — Core

> Nonnegative integer solutions of $x_1+\cdots+x_k=n$ number $\dbinom{n+k-1}{k-1}$; positive solutions number $\dbinom{n-1}{k-1}$.

**What it says.** Distributing $n$ identical items into $k$ boxes is a binomial coefficient, via a stars-and-bars string bijection.

**The move.** Convert "distribute identical objects" into "choose bar positions," a pure binomial count.

**When it fires.** Distributing identical items; counting monomials of given degree; nonnegative-integer equations. *Trigger:* "$x_1+\cdots+x_k=n$, count solutions."

**Micro-example.** $x+y+z=5$, $x,y,z\ge0$: $\binom{7}{2}=21$ solutions.

**Watch for.** Positive vs. nonnegative changes the formula; upper bounds need inclusion–exclusion on top.

**Used in.** Blueprint §9.7; P2 Ch. 15 (Joshi Ch. 1 Comment 7) *(provisional)*. **Neighbours.** → A14 (multinomial), G02, A12.

**Named proof.** Bijection with binary strings of $n$ stars and $k-1$ bars — Stanley, *Enumerative Combinatorics*, Vol. 1.

---

### G06 · Burnside's Lemma (Orbit-Counting) — Stretch

> Number of orbits $=\dfrac{1}{|G|}\displaystyle\sum_{g\in G}|\mathrm{Fix}(g)|$.

**What it says.** Distinct objects under a symmetry group equal the average number of arrangements each symmetry fixes.

**The move.** Count "configurations up to symmetry" by averaging fixed points — the right tool for "necklaces / colourings up to rotation."

**When it fires.** Counting colourings/arrangements modulo a symmetry group. *Trigger:* "count up to rotation/reflection."

**Micro-example.** $2$-colour necklaces of $3$ beads under rotation: $\tfrac13(2^3+2+2)=4$.

**Watch for.** Sum over *all* group elements (including identity, which fixes everything); Pólya enumeration refines it.

**Used in.** P2 Ch. 1 (double-counting engine), Ch. 2 §4.3 (involution in WE3), Ch. 13. *(Named-reference verified in Ch. 1–2; exact §-locations provisional.)* **Neighbours.** → G03, A15 (group/roots-of-unity structure).

**Named proof.** Count the incidences $\{(g,x):g\cdot x=x\}$ two ways via orbit–stabiliser — Rotman, *An Introduction to the Theory of Groups*.

---

### G07 · Turán's Theorem (Extremal Graph Theory) — Stretch

> A $K_{r+1}$-free graph on $n$ vertices has at most $\Big(1-\tfrac1r\Big)\tfrac{n^2}{2}$ edges, with equality for the Turán graph $T(n,r)$.

**What it says.** Avoiding a clique caps the number of edges, and the extremal graph is the balanced complete multipartite one.

**The move.** Convert a "no $K_{r+1}$" structural constraint into a sharp numeric edge bound — the prototypical extremal-graph result.

**When it fires.** Max edges/connections under a "no large clique" condition; densest triangle-free graphs ($r=2$). *Trigger:* "graph with no $(r+1)$-clique, maximise edges."

**Micro-example.** Triangle-free graph on $n$ vertices: at most $\lfloor n^2/4\rfloor$ edges (complete bipartite).

**Watch for.** Equality requires the *balanced* multipartite graph; the bound is for $K_{r+1}$-free, not $K_r$-free.

**Used in.** P4 Case 21 (IMO 1992 P3) *(provisional)*. **Neighbours.** → G17, G09, G01.

**Named proof.** Zykov symmetrisation / weight-shifting to the complete multipartite graph — Aigner & Ziegler, *Proofs from THE BOOK*.

---

### G08 · Hall's Marriage Theorem — Stretch

> A bipartite graph has a perfect matching saturating $L$ $\iff$ every $S\subseteq L$ satisfies $|N(S)|\ge|S|$ (Hall's condition).

**What it says.** A complete matching exists exactly when no subset of one side has too few neighbours.

**The move.** Reduce "can everyone be matched?" to a checkable neighbourhood-size condition — existence of a system of distinct representatives.

**When it fires.** Assignment/matching problems; systems of distinct representatives; Latin-square completions. *Trigger:* "can each be paired with a distinct partner?"

**Micro-example.** $3$ applicants each qualified for $\ge$ their share of jobs, with no deficient subset, can all be hired.

**Watch for.** Must check *all* subsets $S$ (the deficient one breaks it); bipartite setting.

**Used in.** INMO/IMO combinatorics *(provisional)*. **Neighbours.** → G03, G16, G07.

**Named proof.** Augmenting-path argument, or induction on $|L|$ — Bondy & Murty, *Graph Theory*.

---

### G09 · Ramsey Theory (Basic) — Stretch

> $R(3,3)=6$: any $2$-colouring of $K_6$'s edges has a monochromatic triangle; generally $R(r,s)\le\binom{r+s-2}{r-1}$.

**What it says.** Complete disorder is impossible — large enough structures force monochromatic patterns.

**The move.** Guarantee an *ordered* substructure inside any colouring, once the ground set is large enough — pigeonhole with structure.

**When it fires.** "Among any $N$, some monochromatic/ordered configuration exists." *Trigger:* "$2$-colour the edges / pairs and find a pattern."

**Micro-example.** Among any $6$ people, three are mutual friends or three are mutual strangers.

**Watch for.** Ramsey numbers grow fast and are mostly unknown; existence threshold, not construction.

**Used in.** P3 Ch. 6 CS#2 *(provisional)*. **Neighbours.** → G01 (pigeonhole), G12 (Van der Waerden).

**Named proof.** Greedy neighbour-set pigeonhole on one vertex's incident colours — Aigner & Ziegler.

---

### G10 · Ballot Problem / André Reflection Principle — Stretch

> If $A$ gets $a$ votes and $B$ gets $b<a$, the probability $A$ leads throughout is $\dfrac{a-b}{a+b}$; proved by reflecting "bad" lattice paths.

**What it says.** Counting paths that stay strictly on one side of a line, via reflecting the offending ones.

**The move.** Count constrained lattice paths by *subtracting reflected bad paths* — the engine behind Catalan numbers and the cycle lemma.

**When it fires.** Lattice paths staying above a line; sequences with a running-majority condition. *Trigger:* "paths that never touch / never go below."

**Micro-example.** Paths from origin staying strictly positive map, by reflection, to a clean difference of binomials.

**Watch for.** The reflection must biject bad paths with an easily-counted set; boundary conditions ($\ge$ vs. $>$).

**Used in.** P2 Ch. 15 (André reflection, ballot, cycle lemma, LGV) *(provisional)*. **Neighbours.** → E05 (Catalan), G03, A05.

**Named proof.** Reflect the lattice paths that touch the diagonal across it — Feller, *An Introduction to Probability Theory*, Vol. 1.

---

### G11 · Cayley's Formula (Labelled Trees) — Stretch

> There are $n^{n-2}$ labelled trees on $n$ vertices; proved by the Prüfer-sequence bijection (sequences of length $n-2$ over $[n]$).

**What it says.** The number of spanning trees on $n$ labelled vertices is exactly $n^{n-2}$.

**The move.** Encode each tree as a unique short sequence (Prüfer), reducing tree-counting to counting strings.

**When it fires.** Counting labelled trees/forests/spanning trees. *Trigger:* "how many labelled trees on $n$ vertices?"

**Micro-example.** $n=3$: $3^{1}=3$ labelled trees (three choices of the central vertex's... in fact the three paths).

**Watch for.** Labelled, not unlabelled; the Prüfer code has length $n-2$.

**Used in.** P2 Ch. 15 (Prüfer-sequence bijection) *(provisional)*. **Neighbours.** → G03 (bijection), G17, E04.

**Named proof.** The Prüfer-sequence bijection between trees and length-$(n-2)$ strings — Aigner & Ziegler.

---

### G12 · Van der Waerden's Theorem — Stretch

> For any $k$-colouring of $\mathbb{Z}^+$ and any length $m$, there is a monochromatic arithmetic progression of length $m$; $W(2,3)=9$.

**What it says.** Any finite colouring of the integers contains arbitrarily long monochromatic APs.

**The move.** Guarantee an arithmetic structure inside any colouring of a long enough initial segment — Ramsey theory for progressions.

**When it fires.** "Colour $1..N$; find a monochromatic AP"; partition-regularity arguments. *Trigger:* "$k$-colour the integers, find a monochromatic progression."

**Micro-example.** $W(2,3)=9$: any $2$-colouring of $\{1,\dots,9\}$ has a monochromatic $3$-term AP.

**Watch for.** Existence threshold ($W$) grows enormously; this is existence, not construction.

**Used in.** P3 Ch. 6 CS#2 *(provisional)*. **Neighbours.** → G09 (Ramsey), G01.

**Named proof.** Double induction on the number of colours and the target length — Graham, Rothschild & Spencer, *Ramsey Theory*.

---

### G13 · Erdős–Ko–Rado Theorem — Stretch

> An intersecting family of $k$-subsets of $[n]$ (with $n\ge2k$) has size at most $\dbinom{n-1}{k-1}$, achieved by all sets containing a fixed element.

**What it says.** The largest family of $k$-sets in which any two intersect is the "star" through a fixed point.

**The move.** Pin the extremal intersecting family exactly — a benchmark extremal-set-theory result.

**When it fires.** "Largest family of subsets, pairwise intersecting." *Trigger:* "every two chosen sets must share an element."

**Micro-example.** $k=2,n=4$: at most $\binom{3}{1}=3$ pairwise-intersecting $2$-subsets.

**Watch for.** Needs $n\ge2k$ (else all $k$-sets intersect trivially); equality is the star.

**Used in.** Blueprint §9.7 seed *(provisional)*. **Neighbours.** → G08, G07, G01.

**Named proof.** Katona's cyclic-permutation argument — Aigner & Ziegler, *Proofs from THE BOOK*.

---

### G14 · Derangements ($D_n$) — Core

> $D_n=n!\displaystyle\sum_{k=0}^{n}\frac{(-1)^k}{k!}$; $\;\dfrac{D_n}{n!}\to\dfrac1e$; recurrence $D_n=(n-1)(D_{n-1}+D_{n-2})$.

**What it says.** The number of permutations with no fixed point, the canonical inclusion–exclusion count.

**The move.** Count "nothing in its place" by inclusion–exclusion over the fixed-point events — and note the probability tends to $1/e$.

**When it fires.** Permutations avoiding fixed points; "no one gets their own hat." *Trigger:* "permutations with no element fixed."

**Micro-example.** $D_4=9$ derangements of $4$ objects.

**Watch for.** $D_n$ is *not* $n!/e$ exactly (it is the nearest integer); off-by-one in the alternating sum.

**Used in.** P2 Ch. 13 (I–E on permutations) *(provisional)*. **Neighbours.** → G02 (inclusion–exclusion), G04, E04.

**Named proof.** Inclusion–exclusion over the $n$ fixed-point events — Stanley, *Enumerative Combinatorics*, Vol. 1.

---

### G15 · Cauchy–Davenport Theorem — Stretch

> For nonempty $A,B\subseteq\mathbb{Z}/p\mathbb{Z}$ ($p$ prime): $\;|A+B|\ge\min(p,\;|A|+|B|-1)$.

**What it says.** Sumsets modulo a prime cannot be too small — they grow at least additively until they fill the group.

**The move.** Lower-bound a sumset's size, the foundational estimate of additive combinatorics over $\mathbb{Z}/p$.

**When it fires.** "How small can $A+B$ be?"; covering all residues by sums; additive-basis arguments. *Trigger:* "size of a sumset mod $p$."

**Micro-example.** If $|A|=|B|=\tfrac{p+1}{2}$ then $A+B=\mathbb{Z}/p\mathbb{Z}$ (every residue is a sum).

**Watch for.** Requires $p$ prime (fails for composite moduli); the $\min$ with $p$ caps the bound.

**Used in.** Bridges Clusters C and G *(provisional)*. **Neighbours.** → C03, G05, C12.

**Named proof.** The $e$-transform, or the polynomial method (Combinatorial Nullstellensatz) — Nathanson, *Additive Number Theory*.

---

### G16 · Probabilistic Method (Existence by Expectation) — Stretch

> If $E[X]>0$ then $X>0$ for some outcome; if $E[X]<1$ (integer $X\ge0$) then $X=0$ somewhere. Existence without explicit construction.

**What it says.** An object with a desired property exists if a random object has it with positive probability (or if the expected count of "bad" features is below $1$).

**The move.** Prove existence by *averaging* rather than constructing — choose at random, show the bad event is unlikely.

**When it fires.** "Show there exists a configuration with property $P$" when construction is hard. *Trigger:* "a random choice works with positive probability."

**Micro-example.** A random $2$-colouring of $K_n$ has expected monochromatic $K_k$ count $<1$ for suitable $n$ — so a good colouring exists.

**Watch for.** Gives existence, not a construction; choosing the right random model and event is the craft.

**Used in.** P3 Ch. 6 CS#5 note (probabilistic-method candidate) *(provisional)*. **Neighbours.** → G04 (linearity), PR17, G01.

**Named proof.** Averaging: if $E[X]<1$ (integer $X\ge0$) some outcome has $X=0$ — Alon & Spencer, *The Probabilistic Method*.

---

### G17 · Handshaking Lemma / Degree-Sum Formula — Core

> In any graph, $\displaystyle\sum_{v\in V}\deg(v)=2|E|$; consequently the number of odd-degree vertices is even.

**What it says.** Summing all vertex degrees double-counts the edges.

**The move.** Tie local data (degrees) to a global count (edges) by double counting — the first lemma of every graph argument, and a parity engine.

**When it fires.** Counting edges from degrees; parity arguments on graphs; "an even number of odd-degree vertices." *Trigger:* "sum of degrees" or "odd-degree vertices."

**Micro-example.** A graph cannot have exactly three odd-degree vertices (the count of odd-degree vertices is even).

**Watch for.** Counts each edge twice; loops contribute $2$ to a degree.

**Used in.** P4 Case 19 (IMO 2001 P3 incidence counting) *(provisional)*. **Neighbours.** → G03 (double counting), D05 (Euler's formula), G07.

**Named proof.** Double-count edge–endpoint incidences — Bondy & Murty, *Graph Theory*.

---

# Part III — Cross-Reference Tables

*The gems are organised by mathematical family above. But you will reach for them along three other axes: from an **archetype** you have recognised, from a **chapter** you are reading, and from a **prerequisite** you have just refreshed. These three indices are what make Pillar 5 operational rather than encyclopedic.*

> **All cross-references in this part are provisional**, pending a verification pass against the locked chapters of Pillars 2–4. Treat them as a navigational draft, not a citation of record.

---

## III.1 — Archetype → Gems

*You have recognised the archetype (Pillar 2). These are the gems that execute its pivot.*

| # | Archetype | Primary gems |
|---|---|---|
| 1 | Invariance | A01, A04, A09, C16, D05, D18, G17 |
| 2 | Symmetry | A09, B08, B09, B10, B11, C10, D03, D13, G06 |
| 3 | Duality | D04a, D04b, D11, D15, G02 |
| 4 | Hidden Structure | A02, A09, A15, C08, C09, D08, E03 |
| 5 | Substitution | A17, F04a, F09, F10, D07c |
| 6 | Linearisation | B12, E10, F03, F05, F08 |
| 7 | Normalisation | A17, B13, B14, D07d |
| 8 | Domain Translation | A10, A15, D06, D08, D19, E03 |
| 9 | Domain Constraints | A16, A17, C16, PR05-built bounds |
| 10 | Inequality Constraints | B01–B15, F12 |
| 11 | Existence / Uniqueness | A08, F01, F02, F06, G01, G16 |
| 12 | Extremal Principles | B01, B05, B07, F07, F12, G07 |
| 13 | Combinatorial Principles | A05, A12, A14, G01–G06, G14 |
| 14 | Parity / Modularity | A07b, C01–C09, C16, G17 |
| 15 | Bijection / Correspondence | A12, E05, G03, G05, G10, G11 |
| 16 | Reverse Engineering | A01, A08, A16, D20 |
| 17 | Degrees of Freedom | A04, A08, A14, F12 |
| 18 | Recursion / Induction | A13, E01, E02, E03, E10, F11 |
| 19 | Pivoting / Elimination | A01, A06, A11, B-cluster pivots |
| 20 | Analogy / Transfer | A10, D09, D14, A15 |

---

## III.2 — Chapter / Case → Gems Invoked  *(reverse-lookup)*

*You are reading a chapter and want the gems it uses gathered in one place. This is the §9.2 reverse-lookup made permanent.*

### Pillar 2 — The Archetypes

| Chapter | Gems invoked |
|---|---|
| Ch. 1 Invariance | A01, C09, D05, G17 |
| Ch. 2 Symmetry | C10, D03, D10, D11, D13, D16, G06 |
| Ch. 3 Duality | D01, D11 |
| Ch. 5 Substitution | A17, B08, B09, D09, F09, F11 |
| Ch. 6 Linearisation | A06, A11, E06, E08, E10, F03, F05, F08 |
| Ch. 7 Normalisation | B01, B02, B03, B05, B13, B14, D07a, D07c, D07d |
| Ch. 8 Domain Translation | A10, A15, B06, D07b, D08, D15, D17, D19, D20, E03 |
| Ch. 9 Domain Constraints | A03, A09, A16, B04, B06, B07, C16, D07a, D09, D12, D18 |
| Ch. 10 Inequality Constraints | B01, B02, B03, B04, B07, B08, B10, B11, D07d |
| Ch. 11 Existence / Uniqueness | F01, F02, F06 |
| Ch. 12 Extremal Principles | F07, F12 |
| Ch. 13 Combinatorial Principles | A05, E04, G02, G03, G04, G06, G14 |
| Ch. 14 Parity / Modularity | A07b, A16, C01, C02, C05, C07, C08, C09, G02 |
| Ch. 15 Bijection / Correspondence | A12, A14, D06, E05, G03, G05, G10, G11 |
| Ch. 16 Reverse Engineering | A07a, A01 |
| Ch. 17 Degrees of Freedom | A04, A08 |
| Ch. 18 Recursion / Induction | A05, A06, E01, E07, E10, F04b |
| Ch. 20 Analogy / Transfer | A10, D14 |

### Pillar 3 — Multidirectional

| Location | Gems invoked |
|---|---|
| Ch. 3 (convergence problems) | A01 (IMO 1988), A13 (IMO 1981) |
| Ch. 5 (multidirectional map) | G01 |
| Ch. 6 Case Studies | F10 (CS5), G01 (CS1), G09 (CS2), G12 (CS2), G16 (CS5) |

### Pillar 4 — CEP Design

| Case | Gems invoked |
|---|---|
| Case 2 (IMO 1969 P1) | A02 |
| Case 5 | B01 |
| Case 12 | E02 |
| Case 15 | C03 |
| Case 19 (IMO 2001 P3) | G17 |
| Case 21 (IMO 1992 P3) | G07 |
| Cases 22–23 | C02, C11 |
| Case 25 | A01 (Vieta jumping) |
| Ch. 9 Ex. 2 | E02 (golden ratio) |

---

## III.3 — Prerequisite → Gems Unlocked

*You have just refreshed a Foundation block (Part I). These are the gems it makes accessible.*

| Block | Unlocks |
|---|---|
| PR01 Sets, Relations & Functions | F10, G03; vocabulary for all |
| PR02 Induction & Proof Logic | A13, E10; proof method for most |
| PR03 Complex Numbers | A10, A15, D08, D17, D19 |
| PR04 Trigonometric Functions | A09, D07a, D07b, D07c, D07d, F09 |
| PR05 Inequalities & Algebra | A07a, A16, B01–B15 |
| PR06 Permutations, Combinations & Probability | A05, A12, G01–G05, G14 |
| PR07 Binomial Theorem & Sequences | A05, E01, E02, E10 |
| PR08 Coordinate Geometry | D01, D11, D15, D20 |
| PR09 3D Geometry | D-cluster spatial work, PR16 |
| PR10 Matrices & Determinants | A01, A04, A13, D05 |
| PR11 Limits, Continuity & Differentiability | F01, F02, F03, F05 |
| PR12 Inverse Trigonometric Functions | A06, F04c |
| PR13 Applications of Derivatives | B03, F08, F12 |
| PR14 Integrals | E07, F04a, F04b, F04c, F09 |
| PR15 Differential Equations | F11 |
| PR16 Vector Algebra | D-cluster geometry |
| PR17 Statistics & Probability II | G04, G16 |

---

## Coda — How the pillar is meant to be used

Read one way, this is a reference: you meet *"(See Gem B01)"* in a chapter, you turn here, you read the boxed statement and *the move*, you return. Read the other way, it is a course: you climb Cluster by Cluster, and each gem's *trigger* trains the reflex that lets you reach for it unprompted.

Either way, the gems are not the mathematics — they are its *executable layer*. The archetypes told you what the problem was; these tell you how to move. Keep this pillar at your elbow until the day you no longer need it, which is the day every trigger here has become a reflex.

🌑







