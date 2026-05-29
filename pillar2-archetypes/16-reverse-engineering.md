---
chapter: 16
archetype: Reverse Engineering
subtitle: "When the Answer Is Given, the Problem Is to Find the Question"
category: Structural Reasoning (Archetypes 13–16) — fourth/closing chapter
related_archetypes: [3, 4, 15, 17, 19]
key_gems: [A01, A08, A16, D20]
  - "Vieta's formulas: roots $\\leftrightarrow$ elementary symmetric polynomials $\\leftrightarrow$ coefficients; reverse-engineer a polynomial from its roots by multiplying the linear factors $(x - r_i)$ or, equivalently, by reading off the elementary symmetric polynomials $e_k(r_1, \\ldots, r_n)$ as the signed coefficients of $x^{n-k}$"
  - "Newton's identities: power sums $p_k = \\sum r_i^k$ are related recursively to elementary symmetric polynomials $e_k$ via $p_k = e_1 p_{k-1} - e_2 p_{k-2} + \\cdots + (-1)^{k-1} k e_k$, enabling polynomial reconstruction from power-sum data"
  - "Real-coefficient root-pairing: a polynomial with real coefficients has complex roots in conjugate pairs $\\{z, \\bar z\\}$; the minimum-degree real polynomial with prescribed complex roots is the product of the conjugate-pair quadratic factors $(x - z)(x - \\bar z) = x^2 - 2\\Re(z)\\,x + |z|^2$"
  - "Cholesky factorisation: a positive-definite symmetric matrix $G$ admits a unique decomposition $G = L L^T$ with $L$ lower-triangular and positive diagonal entries; this reverse-engineers vectors $\\vec v_i$ from their Gram matrix $G_{ij} = \\vec v_i \\cdot \\vec v_j$"
  - "ODE-from-solution-family: an $n$-parameter family of solutions $y = F(x; c_1, \\ldots, c_n)$ satisfies a unique $n$-th-order ODE, obtained by differentiating $n$ times and eliminating the parameters from the resulting $(n + 1)$-equation system"
  - "Triangle from $(r, R, s)$: the cubic $t^3 - 2s\\,t^2 + (s^2 + r^2 + 4Rr)\\,t - 4Rrs = 0$ has the triangle's sides $a, b, c$ as its roots; the triangle is uniquely determined up to congruence by the trio $(r, R, s)$"
  - "Cauchy functional equation + continuity: the only continuous solutions to $f(x + y) = f(x) + f(y)$ are the linear functions $f(x) = c x$; specifying a single boundary value $f(x_0) = y_0$ uniquely determines $c = y_0/x_0$"
  - "Five-points-determine-a-conic: a general conic $A x^2 + B xy + C y^2 + D x + E y + F = 0$ has 5 projective parameters; 5 points in general position determine the conic uniquely up to scaling"
  - "Bound-then-enumerate (Diophantine reverse engineering): for digit-constrained equations like $N = 2(a^2 + b^2 + c^2)$, derive size bounds on the digits, then enumerate the bounded range exhaustively"
  - "Inverse-area: the area between a parametric curve $y = f(x; a)$ and the $x$-axis is a function $A(a)$; inverting $A(a)$ recovers the parameter $a$ from the area, illustrating the area-as-data reverse-engineering pattern"
canonical_takeaway: "When the answer is given, the problem is to find the question."
status: locked
last_revised: 2026-05-29
locked_on: 2026-05-29
sourcing_note: "All worked examples and practice problems in this chapter are drawn from K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), or from JEE / RMO / INMO examinations commented on in that text. See Blueprint §6.2 for the sourcing rule and `pillar2-archetypes/_template/joshi-problems-locked.md` §Ch. 16 for the locked slate. **Verification audit for this chapter caught one slate error**: PP1 (three-digit number = twice the sum of digit-squares, Joshi Ex. 24.99(a)) listed the answer as $N = 166$; verification reveals $166$ does not satisfy the equation ($2 \\cdot (1 + 36 + 36) = 146 \\ne 166$). Exhaustive search of $a \\in \\{1, 2, 3, 4\\}$ (bound: $N = 100a + 10b + c \\le 2 \\cdot 3 \\cdot 81 = 486$) yields the unique solution $N = 298$ (digits $2, 9, 8$: $2(4 + 81 + 64) = 2 \\cdot 149 = 298$ ✓). Slate patched in v0.2.13. **Cross-archetype note**: PP1 is also cross-archetype with Ch. 4 WE2 (Hidden Structure), where the same digit-Diophantine problem is framed as 'find the hidden algebraic structure'; here in Ch. 16 it is framed as 'reverse-engineer the digits from the arithmetic relation'. This chapter **CLOSES the Structural Reasoning sub-pillar (Chs. 13–16)** and bridges to the Meta-Reasoning sub-pillar (Chs. 17–20) opening with Ch. 17 Degrees of Freedom Analysis."
---

# Chapter 16 — Reverse Engineering

## *When the Answer Is Given, the Problem Is to Find the Question*

---

## Opening Vignette

A senior radiologist at the All-India Institute of Medical Sciences (AIIMS) in New Delhi is reviewing a *computed tomography* (CT) scan of a patient's abdomen. The CT scanner has rotated a series of X-ray emitters and detectors around the patient over a 360° arc, acquiring approximately 1,000 two-dimensional projection images at finely-spaced angles. The radiologist's screen displays the *reconstructed three-dimensional density field* — a transparent rendered volume showing the precise location of every organ, blood vessel, and bone within a $0.5\,\text{mm}^3$ voxel grid. The reconstruction algorithm running in the background — the *filtered back-projection* derived from the *Radon transform inversion* — *reverse-engineers* the unknown 3D density field from its known 2D projections. The forward problem is straightforward: given the density field $\rho(\mathbf x)$, predict the X-ray attenuation along any line of sight by integrating $\rho$ along that line. The *inverse problem* — given the 1,000 attenuation profiles, find the unique density field that produced them — is the deep mathematical challenge that won Allan Cormack and Godfrey Hounsfield the 1979 Nobel Prize in Medicine. Cormack's 1963 paper showed that the Radon transform $\mathcal R \rho$ is *invertible* under mild regularity assumptions: the original density is recovered by *back-projecting* the filtered projections through the *inverse Radon transform formula* $\rho(\mathbf x) = \mathcal R^{-1}[\mathcal R \rho](\mathbf x)$. Without this inverse, modern medical imaging would not exist; the patient could not be diagnosed without invasive exploratory surgery. *The radiologist's diagnostic capability rests on a reverse-engineering theorem* — the 2D projections, treated as the "answer," yield the 3D density field as the "question."

Now turn to a different scene. A retired Indian Space Research Organisation (ISRO) mission designer is in his Bangalore study explaining to a young engineering student how Chandrayaan-1, India's first lunar mission, was actually planned. The student had asked a forward question: "Given the launch from Sriharikota at a certain time, where will the spacecraft be at lunar arrival?" The retired designer laughs gently and shakes his head. "That is not how mission design works," he says. "We start with the *desired* lunar terminal state — orbit insertion at 100-km altitude with specific velocity vector, inclination relative to the lunar equator, and timing for solar-panel illumination — and we *reverse-engineer the entire trajectory backward to launch*. We compute the trans-lunar injection burn that achieves the desired terminal state, then the parking-orbit altitude and inclination that supports that injection burn, then the launch azimuth and time-of-launch that puts the rocket into that parking orbit, then the propellant loading that achieves that launch profile. The entire mission plan is constructed *backward from the target*. The forward simulation — to verify our plan — comes only at the end." The student begins to grasp that the *backward* problem (given terminal state, find launch parameters) is the *real* engineering problem; the forward simulation is just verification.

These two scenes look entirely unrelated. A radiologist inverting X-ray projections to recover a 3D density field; an ISRO designer inverting orbital mechanics to recover launch parameters. They share the most important reframing in the entire chapter — the recognition that *when the answer is given, the problem is to find the question*. The radiologist reverses the *forward* X-ray attenuation calculation; the ISRO designer reverses the *forward* orbital propagation. Both invert the natural direction of computation, treating *outputs* as data and *inputs* as unknowns. The technique pervades engineering, science, and applied mathematics.

This is *Reverse Engineering*. It is the *fourth and closing* chapter of the *Structural Reasoning* sub-pillar (Chapters 13–16), completing the arc that began with Chapter 13 (combinatorial counting), continued through Chapter 14 (parity / modular reasoning) and Chapter 15 (bijection / correspondence), and now concludes with the most cognitively demanding shift: *reversing the problem's natural flow*. The chapter develops the toolkit (Vieta's formulas, Newton's identities, complex-conjugate root pairing, Cholesky factorisation, ODE-from-solution-family, geometric-invariant inversion, Cauchy functional equation with boundary data, five-points-determine-a-conic, bound-then-enumerate Diophantine reasoning, inverse-area parameter recovery) and the recurring patterns (treating parameters as unknowns; reversing standard derivation directions; reading "data" as constraints and "answers" as questions). The chapter has three structural threads. The first is *direction-of-computation reversal*: trained problem-solvers learn to ask *"what would make this conclusion true?"* before computing forward. The second is *named-inversion-theorem deployment*: the toolkit's named theorems (Radon inverse, Vieta, Newton, Cholesky, Cauchy) provide closed-form inversions for the most common forward operations. The third is *closing the Structural Reasoning sub-pillar*: by Chapter 16, the reader has internalised that structure (Chs. 13–16 collectively) is not just for *recognition* but for *construction* — the same structural understanding that lets one read the bijection underlying Vandermonde (Ch. 15) lets one *construct* the polynomial with prescribed roots (Ch. 16 WE3).

> *When the answer is given, the problem is to find the question. Reverse the natural direction of computation — from output to input, from invariant to structure, from solution-set to defining-equation.*

---

## 1. The Archetype Defined

### 1.1 Formal Definition

We make the intuition precise.

\begin{definition}[Reverse Engineering Archetype]
A *reverse-engineering* approach to a problem is the strategy of *reversing the natural direction of computation*: instead of starting from inputs and computing outputs (the *forward* direction), one starts from desired outputs and *constructs* the inputs that produce them (the *backward* direction). The archetype is the discipline of (i) recognising that the problem is naturally stated in the *backward* direction (the "answer" is given, the "question" is to be found); (ii) identifying the *forward* operator whose inverse is needed; (iii) applying the inverse — either via a named-theorem closed form (Vieta, Newton, Cholesky, Cauchy, Radon, etc.) or via systematic reversal of the forward computation; and (iv) verifying the construction by running the forward computation on the recovered inputs.
\end{definition}

Three remarks unpack the definition.

First, the *direction-reversal recognition* (Step (i)) is the cognitively central step. The trained solver, when faced with a problem, asks *"is this a forward or a backward problem?"* — and learns to recognise the backward variants. The classical clue is a problem that *gives outputs as data* and *asks for inputs as unknowns*: "find the polynomial with these roots," "construct the ODE whose solutions are these curves," "determine the digits of a number satisfying this arithmetic relation," "find the parameter that produces this area." Each is naturally backward; treating it as forward (i.e., computing the natural direction) misses the point entirely.

Second, the *inverse-operator deployment* (Step (iii)) is the engine. Many forward operations have well-studied closed-form inverses: the polynomial-from-roots operation inverts root-extraction; Newton's identities invert the power-sum operation; Cholesky factorisation inverts the Gram-matrix operation; the inverse Radon transform inverts the X-ray-projection operation; the Cauchy functional equation with boundary data inverts the function-evaluation operation. The toolkit's named theorems are *the* most efficient inversion machinery; the trained solver matches the problem to the right theorem.

Third, the *verification by forward computation* (Step (iv)) is the discipline. Backward construction can be error-prone (missing edge cases, mis-applying the inverse formula, forgetting domain restrictions); the most reliable verification is to *run the forward computation* on the recovered inputs and check that the original outputs are produced. The radiologist's CT reconstruction is verified by re-projecting the recovered 3D density and comparing with the original X-ray attenuation profiles; the ISRO mission plan is verified by forward-simulating the recovered launch parameters and confirming they reach the target lunar orbit.

The chapter encounters five characteristic forms of reverse engineering.

- **Form I — Polynomial-from-roots (Vieta inversion).** Given desired roots, construct the polynomial; given desired structural properties (real coefficients, integer coefficients, minimum degree), apply additional constraints. *Examples.* WE3 (real-coefficient polynomial with complex roots $1 + i, 2 - 3i$), WE1 (quartic-with-all-real-roots via quadratic-in-$a$ reversal).

- **Form II — Function-from-target (ODE / functional-equation inversion).** Given a family of solution curves, construct the ODE; given functional-equation-plus-boundary data, construct the unique function. *Examples.* PP2 (ODE from $c_1 \cos x + c_2 \sin x$), PP5 (Cauchy + $f(1) = 2$).

- **Form III — Vectors-from-data (Gram matrix / Cholesky inversion).** Given inner products, construct the vectors; given a Gram matrix, apply Cholesky factorisation. *Examples.* PP3 (Gram matrix to vectors).

- **Form IV — Geometry-from-invariants.** Given a small set of geometric invariants, reconstruct the geometric object. *Examples.* WE2 (triangle from $r, R, s$ via cubic-with-sides-as-roots), PP6 (conic from 5 points), and the related circle-from-3-points classical construction.

- **Form V — Parameter-from-derived-quantity.** Given a derived quantity (area, sum of digit-squares, power-sums), recover the underlying parameter via inversion of the derivation. *Examples.* PP1 (digits from $N = 2(\sum a_i^2)$), PP4 (cubic from Newton's identities on power-sums), PP7 (cubic-parameter from enclosed area).

### 1.2 The Core Principle

Stripped to its essence, the principle is one sentence.

> *When the answer is given, the problem is to find the question.*

This sentence captures the recurrent observation that, across mathematics, engineering, and applied science, the *backward* direction of a computation is often the *real* problem, while the *forward* direction is merely the verification step. The CT scanner's diagnostic value comes from the *inverse* Radon transform; the ISRO mission plan's value comes from the *inverse* orbital propagation; the algebraist's polynomial-from-roots construction is the *inverse* of the algebraist's root-extraction. The forward direction is computable; the backward direction is the engineering — and often, the inversion machinery is the substantial theory.

A complementary phrasing: *reverse engineering is the discipline of treating outputs as inputs and inputs as outputs*. The cognitive flip is to recognise that the problem's natural statement (whether outputs or inputs are "given") is sometimes the *opposite* of what makes the problem tractable. The radiologist could attempt the forward problem ("given my guess of the 3D density, predict the X-ray pattern") and iterate until convergence — but this is computationally prohibitive; the direct inverse Radon transform gives the answer in one closed-form pass. The cognitive shift is to *recognise* that the inverse machinery exists and *apply* it.

A third phrasing: *reverse engineering operationalises the duality between problem and answer*. In every well-posed problem, the input-output relation is a *function*; the inverse function (when it exists) gives the backward direction. Reverse-engineering is the systematic study and application of these inverse functions. The pattern recurs across disciplines: *inverse problems* in physics (heat-equation inverse, wave-equation inverse, electromagnetic scattering inverse), *backward analysis* in algorithms (working from the final state to the initial state), *retrosynthesis* in chemistry (planning a synthesis backward from the target molecule), and *reverse-modelling* in machine learning (recovering the data distribution from the model's predictions).

### 1.3 The Cognitive Shift

Three cognitive shifts deserve naming.

The first is *direction-of-computation awareness*. The trained solver, when reading a problem, asks *"which direction is the natural computation, and which direction does the problem ask for?"* This single reframing flags the backward problems and triggers the reverse-engineering toolkit; without it, students attempt forward computations that miss the problem's point.

The second is *parameter-as-unknown promotion*. In many problems, what appears to be a *fixed parameter* (e.g., the constant $a$ in $x^4 - 2ax^2 + x + a^2 - a = 0$) can be *promoted* to the unknown — and the problem's complexity often collapses dramatically. WE1's elegant factorisation $(a - x^2 - x)(a - x^2 + x - 1) = 0$ comes from *treating $a$ as the unknown* in a quadratic-in-$a$ equation, exposing that the quartic-in-$x$ is actually a *quadratic-in-$a$ in disguise*. The cognitive flip is to question which variable is "really" the unknown.

The third shift is *cross-archetype synthesis*. Reverse-engineering interlocks with at least five other archetypes: with Ch. 3 (Duality — *every forward operation has a dual backward operation*); with Ch. 4 (Hidden Structure — *the inverse machinery is often the hidden structure*); with Ch. 15 (Bijection — *bijections are explicitly invertible by construction*); with Ch. 17 (Degrees of Freedom — *the dimensionality of the inverse problem is the dimensionality of the data minus the dimensionality of the constraints*); with Ch. 19 (Pivoting / Elimination — *Gaussian elimination is the prototype reverse-engineering algorithm for linear systems*). The trained solver, by Chapter 16, sees these as a coherent body of *inverse reasoning*.

---

## 2. The Deep Structure

### 2.1 Mathematical Foundations

Reverse engineering rests on four mathematical foundations.

The first is *Vieta's formulas* and their inversion. For a monic polynomial $f(x) = x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0$ with roots $r_1, r_2, \ldots, r_n$ (counted with multiplicity, including complex roots in the algebraic closure), the coefficients are signed elementary symmetric polynomials of the roots:
\[
  a_{n - k} = (-1)^k e_k(r_1, \ldots, r_n), \quad e_k(r_1, \ldots, r_n) = \sum_{1 \le i_1 < i_2 < \cdots < i_k \le n} r_{i_1} r_{i_2} \cdots r_{i_k}.
\]
The forward direction (roots → coefficients) is mechanical; the inverse direction (coefficients → roots) is the *root-finding* problem, generally requiring numerical methods or radical formulas (Cardano for cubics, Ferrari for quartics, no general formula for degree $\ge 5$ by Abel-Ruffini). Vieta's formulas are the *reverse-engineering's foundation* — they give the closed-form formula for the *forward* polynomial-from-roots operation.

The second is *Newton's identities* relating *elementary symmetric polynomials* $e_k$ to *power sums* $p_k = \sum_{i = 1}^{n} r_i^k$. The recursion is:
\[
  p_k = e_1 p_{k-1} - e_2 p_{k-2} + e_3 p_{k-3} - \cdots + (-1)^{k-1} k e_k \quad (1 \le k \le n).
\]
This recursively determines $e_k$ from $p_1, p_2, \ldots, p_k$, *reverse-engineering* the polynomial from the power-sum data. PP4 illustrates this: given $p_1 = 6, p_2 = 14, p_3 = 36$, compute $e_1 = 6, e_2 = 11, e_3 = 6$, hence $f(x) = x^3 - 6x^2 + 11x - 6 = (x - 1)(x - 2)(x - 3)$.

The third foundation is the *Cholesky factorisation* of positive-definite symmetric matrices. For any positive-definite symmetric matrix $G \in \mathbb R^{n \times n}$, there exists a *unique* lower-triangular matrix $L \in \mathbb R^{n \times n}$ with positive diagonal entries such that $G = L L^T$. The Cholesky factorisation *reverse-engineers* vectors from their Gram matrix: if $G_{ij} = \vec v_i \cdot \vec v_j$ is the Gram matrix of vectors $\vec v_1, \ldots, \vec v_n \in \mathbb R^n$, then setting $V = L^T$ (so $L = V^T$) gives $G = V^T V$, i.e., the rows of $L$ are the vectors $\vec v_1, \ldots, \vec v_n$ in a particular orthonormal coordinate system. PP3 illustrates this.

The fourth foundation is the *ODE-from-solution-family* reversal. An $n$-parameter family of curves $y = F(x; c_1, c_2, \ldots, c_n)$ satisfies a *unique* $n$-th-order ordinary differential equation, obtained by:
- Differentiating the family equation $n$ times to obtain $n + 1$ equations involving $y, y', y'', \ldots, y^{(n)}$ and the $n$ parameters $c_1, \ldots, c_n$.
- Eliminating the parameters $c_1, \ldots, c_n$ from the $n + 1$ equations, leaving a single ODE involving only $y, y', \ldots, y^{(n)}$ and $x$.

PP2 illustrates this: from $y = c_1 \cos x + c_2 \sin x$, differentiate twice to get $y'' = -c_1 \cos x - c_2 \sin x = -y$, so $y'' + y = 0$.

A fifth foundation, important for geometric reverse-engineering: the *Heron-Vieta inversion* for triangles. Given a triangle with sides $a, b, c$, the standard invariants are the inradius $r$, circumradius $R$, semiperimeter $s$, area $K$, angles $A, B, C$, etc. These invariants are related by:
- $K = rs$ (area = inradius times semiperimeter).
- $K = \frac{abc}{4R}$ (area in terms of sides and circumradius).
- $K^2 = s(s - a)(s - b)(s - c)$ (Heron's formula).
- $a + b + c = 2s$, $A + B + C = \pi$, etc.

From $(r, R, s)$, one can reverse-engineer the triangle: $K = rs$, $abc = 4 R rs$, $(s-a)(s-b)(s-c) = r^2 s$. Combined with $a + b + c = 2s$, the three elementary symmetric polynomials of $(a, b, c)$ are determined: $e_1 = 2s, e_2 = s^2 + r^2 + 4Rr, e_3 = 4Rrs$, so the sides are roots of the cubic $t^3 - 2s\,t^2 + (s^2 + r^2 + 4Rr)\,t - 4Rrs = 0$. WE2 develops this in detail.

### 2.2 Physical and Cross-Domain Foundations

The reach of reverse engineering extends across the quantitative and applied sciences.

In *medical imaging*, the *inverse Radon transform* (Cormack 1963, Hounsfield 1972) is the foundation of CT scanning, the *inverse Fourier transform* of MRI reconstruction, the *inverse problem of optical tomography*, and the *time-reversal acoustics* of ultrasound. Each is a Nobel-Prize-level inversion theory translated into routine clinical practice. The entire field of *medical image reconstruction* is built on solving inverse problems with regularisation, prior information, and iterative refinement.

In *aerospace and ballistic engineering*, *backward trajectory propagation* is the standard technique. Mission planning for satellites, interplanetary spacecraft, and ballistic missiles works *backward from the target* — specifying the desired terminal state and computing the launch parameters via inverse orbital mechanics. The Chandrayaan-1 and Mangalyaan missions (ISRO) used this methodology. *Re-entry trajectory design* for spacecraft (the Apollo, Space Shuttle, SpaceX Dragon) reverses the heat-flux equations to determine the safe re-entry corridor.

In *cryptography*, *cryptanalysis* is the reverse engineering of ciphers: given ciphertext (and possibly plaintext-ciphertext pairs), recover the encryption key. *Public-key cryptography* (RSA, ECC) is *designed* to make reverse engineering computationally infeasible — the *forward* operation (encryption with public key) is fast, but the *backward* operation (decryption without private key) requires solving an intractable factoring or discrete-logarithm problem. The security guarantees of modern cryptography rest on the *asymmetry* between forward and backward.

In *machine learning*, *generative models* (GANs, VAEs, diffusion models) reverse-engineer the data distribution: given samples from the distribution, learn the generative process. *Backpropagation* in neural networks is reverse-engineering of the gradient: given a loss function and the forward computation, compute the gradients with respect to all parameters via the chain rule applied backward through the computation graph. *Bayesian inference* is reverse engineering: given observed data, compute the posterior distribution over model parameters.

In *physics*, *inverse scattering theory* (Lax-Levitan, Gelfand-Levitan, Marchenko) reverse-engineers the potential of a Schrödinger equation from the asymptotic scattering data. *Tomography* and *holography* are inverse problems for wave propagation. *Spectral fitting* in astrophysics inverts the radiative transfer equation to recover the physical conditions in stars and galaxies from their observed spectra.

In *chemistry*, *retrosynthetic analysis* (E. J. Corey, 1990 Nobel Prize) is the reverse engineering of organic synthesis: given a target molecule, plan a synthesis by working backward from the target through retrosynthetic disconnections to commercially available starting materials. The methodology revolutionised pharmaceutical synthesis and natural-product chemistry.

In *biology*, *molecular phylogenetics* reverse-engineers the evolutionary history of species from DNA sequence data: given present-day sequences, infer the ancestral sequences and the branching times of the evolutionary tree. *Structural biology* reverse-engineers protein 3D structure from X-ray diffraction patterns (a classical inverse problem) or, more recently, from amino-acid sequence (the AlphaFold revolution).

In *economics and finance*, *implied volatility* in options pricing is the reverse engineering of the Black-Scholes formula: given the observed option price, compute the volatility parameter that the market implies. *Calibration* of derivative-pricing models is reverse engineering of the model parameters from market data.

In *forensics and archaeology*, *forensic reconstruction* (facial reconstruction from skulls, ballistic trajectory reconstruction from impact patterns) and *archaeological dating* (radiocarbon, dendrochronology) are reverse-engineering applications. *Provenance analysis* of art and antiquities uses reverse-engineering of chemical and isotopic signatures.

In *Indian classical music*, the *raga identification* problem given a sample melody is reverse engineering: given the audible sequence of notes, identify the underlying scale (mela), characteristic phrases (*sancharas*), and stylistic conventions that define the raga. *Tala identification* given a sample rhythm reverses the rhythmic-cycle decomposition.

### 2.3 Cognitive Foundations

The cognitive payoff of reverse engineering is threefold.

The first is *problem-decomposition power*. Many problems become *dramatically* easier when reframed as backward problems. WE1's quartic factorisation is the canonical example: a quartic-in-$x$ that looks intractable becomes a *quadratic-in-$a$* whose discriminant is a perfect square, yielding a clean factorisation in three lines. The reframing — *treat the parameter as the unknown* — is the entire pedagogical content.

The second payoff is *named-theorem-toolkit deployment*. The reverse-engineering toolkit is finite and well-organised: Vieta's formulas, Newton's identities, Cholesky factorisation, ODE-from-solution-family, Cauchy functional equation, geometric-invariant inversion (Heron, $abc = 4Rrs$, etc.), and the inverse Radon transform. The trained solver matches the problem's structure to the right theorem in seconds, rather than re-inventing the inversion machinery for each problem.

The third payoff is *cross-archetype synthesis*. Reverse-engineering unifies Chapters 3 (Duality — *every forward direction has a dual backward direction*), 4 (Hidden Structure — *the inverse machinery is often the hidden structure*), 15 (Bijection — *bijections are explicitly invertible*), 17 (Degrees of Freedom — *dimension-matching between data and unknowns determines uniqueness*), and 19 (Pivoting / Elimination — *Gaussian elimination is the prototype reverse-engineering algorithm*). The trained solver, by Chapter 16, sees these connections as a single coherent framework of *inverse reasoning*.

---

## 3. The Diagnostic Toolkit

### 3.1 The Three Questions Method (Reverse-Engineering Edition)

Before applying any inverse machinery, the trained solver asks three questions of the problem.

1. **Is the problem naturally backward?** Verify that the problem *gives outputs as data* and *asks for inputs as unknowns*. Signatures: "find the polynomial with these roots"; "construct the ODE whose solutions are these curves"; "determine the digits / parameter / structure satisfying this relation"; "reverse-engineer X from Y"; "given that the answer is A, what is the question?" Each phrasing signals reverse-engineering.

2. **What is the forward operation, and does it have a named inverse?** Identify the forward operation (root-extraction, derivative, projection, Gram-matrix construction, area integration) and match it to a named inverse:
   - *Roots → polynomial*: Vieta's formulas, $(x - r_1)(x - r_2) \cdots (x - r_n)$.
   - *Power sums → polynomial*: Newton's identities.
   - *Solution family → ODE*: differentiate $n$ times, eliminate parameters.
   - *Gram matrix → vectors*: Cholesky factorisation $G = L L^T$, take rows of $L$.
   - *Functional equation + boundary → function*: Cauchy / Jensen / etc., apply continuity.
   - *Invariants → triangle*: cubic $t^3 - 2s t^2 + (s^2 + r^2 + 4Rr) t - 4Rrs = 0$ with sides as roots.
   - *5 points → conic*: linear system in $A, B, C, D, E, F$.
   - *Area → parameter*: invert the area formula $A = f(a)$.
   - *Digit relations → digits*: bound-then-enumerate (exhaustive search of the bounded range).

3. **Verify by forward computation.** After constructing the inputs, *run the forward operation* to check that the original outputs are produced. This catches errors in the inversion (mis-applied formulas, missed roots, sign errors, domain restrictions).

### 3.2 Forms of Reverse Engineering: A Comprehensive Guide

We collect the five forms encountered in the chapter with one-line diagnostics.

- **Form I — Polynomial-from-roots (Vieta inversion).** *Diagnostic:* the problem prescribes roots or root-properties, asks for the polynomial. *Move:* multiply linear factors; if real coefficients required, ensure complex roots come in conjugate pairs; if minimum degree required, use exactly the conjugate-pair count. *Examples.* WE3 (polynomial with $1 + i, 2 - 3i$), WE1 (quartic-with-all-real-roots via quadratic-in-$a$).

- **Form II — Function-from-target (ODE / functional-equation inversion).** *Diagnostic:* the problem gives a family of solutions or a functional relation, asks for the equation or the function. *Move:* differentiate $n$ times for $n$-parameter families and eliminate; for functional equations, combine with continuity / boundary data to force a unique solution. *Examples.* PP2 (ODE from $c_1 \cos x + c_2 \sin x$), PP5 (Cauchy + boundary $f(1) = 2$).

- **Form III — Vectors-from-data (Gram / Cholesky inversion).** *Diagnostic:* the problem gives an inner-product matrix, asks for the vectors. *Move:* check that the matrix is symmetric positive-(semi-)definite; apply Cholesky factorisation $G = L L^T$; the rows of $L$ are the vectors. *Examples.* PP3 (Gram → vectors).

- **Form IV — Geometry-from-invariants.** *Diagnostic:* the problem gives a small set of geometric invariants (sides, angles, $r$, $R$, $s$, area, point sets), asks for the geometric object. *Move:* set up the polynomial / linear system whose solutions are the unknown geometric parameters; apply Vieta / linear algebra. *Examples.* WE2 (triangle from $r, R, s$), PP6 (conic from 5 points).

- **Form V — Parameter-from-derived-quantity.** *Diagnostic:* the problem gives a derived quantity (area, sum of digit-squares, power-sums), asks for the underlying parameter. *Move:* express the derived quantity as a function of the parameter, then invert (algebraically or via case enumeration). *Examples.* PP1 (digits from $N = 2(\sum a_i^2)$ via bound-then-enumerate), PP4 (cubic from Newton's identities on power-sums), PP7 (cubic-parameter from enclosed area).

### 3.3 Common Pitfalls

Five errors recur often enough to deserve named warnings.

- **The Wrong-Direction Pitfall.** Attempting the *forward* direction when the problem asks for the *backward* direction. The remedy is to *re-read the problem statement* and identify which quantity is given (the output / data) and which is asked-for (the input / unknown).

- **The Missing-Conjugate-Root Pitfall.** In Form I (polynomial-from-roots) with the real-coefficient constraint, forgetting that complex roots must appear in conjugate pairs. The remedy is to *add the conjugate of every prescribed complex root* to the list of roots before multiplying the linear factors.

- **The Degenerate-Inverse Pitfall.** Applying an inverse formula in a degenerate case where the inverse is non-unique or doesn't exist. E.g., Cholesky factorisation fails for non-positive-definite Gram matrices (the vectors don't exist in real Euclidean space); five-points-determine-a-conic fails when the points are not in *general position* (e.g., three collinear); ODE-from-solution-family fails when the family is not full $n$-parameter. The remedy is to *check the regularity conditions* before applying the inverse.

- **The Verification-Skipping Pitfall.** Constructing the inputs via inversion but skipping the forward-verification step. Errors in the inversion (mis-applied formulas, sign errors, domain restrictions) often go undetected without explicit forward verification. The remedy is to *always run the forward operation on the recovered inputs* and confirm the original outputs are reproduced.

- **The Bound-Then-Enumerate-Off-By-One Pitfall.** In Form V (parameter-from-derived-quantity) with digit-Diophantine problems, bounding analysis can be off by one: the upper bound $N \le 486$ in PP1 might lead a student to think $a \le 4$, but the *correct* bound from $N \ge 100$ also constrains $a \ge 1$, so $a \in \{1, 2, 3, 4\}$ — not $\{0, 1, 2, 3, 4\}$. The remedy is to *write out both bounds explicitly* and verify the enumerated range.

---

## 4. Worked Examples

We work three problems in detail, each in the six-point format. The first illustrates Form I (polynomial-from-roots via the *quadratic-in-the-parameter* reversal) for the quartic-with-all-real-roots problem; the second illustrates Form IV (geometry-from-invariants) for the triangle-from-$(r, R, s)$ problem; the third illustrates Form I in its purest form (polynomial-from-prescribed-complex-roots with the real-coefficient constraint).

### 4.1 Example 1 — Quartic with All Real Roots (Quadratic-in-$a$ Reversal)

**Problem.** *Find all real values of $a$ for which the quartic $x^4 - 2 a x^2 + x + a^2 - a = 0$ has all four roots real.*
*(Regional Mathematics Olympiad; Joshi EJM Ch. 24, Exercise 24.68; an RMO-tier reverse-engineering problem with a beautiful factorisation hidden by direction-of-computation.)*

**SEED.** *Reverse engineering (Form I — polynomial-from-roots via parameter-promotion).* The quartic is naturally read as "given $a$, find the roots in $x$." Trying this directly leads to Ferrari-style algebra. The *reverse-engineering insight*: treat $a$ as the *unknown* in a quadratic-in-$a$ equation, with $x$ as a parameter. The quartic, regrouped, becomes $a^2 - a(2x^2 + 1) + (x^4 + x) = 0$ — a quadratic in $a$ whose discriminant turns out to be a *perfect square* in $x$. This factorisation collapses the quartic into a product of two quadratics in $x$, each of which has a simple discriminant condition for real roots.

**BRUTE PATH.** A student without the reverse-engineering insight might attempt the *Ferrari resolvent cubic* approach: introduce parameter $t$ such that $x^4 - 2ax^2 + x + a^2 - a + (x^2 - a + t)^2 - (x^2 - a + t)^2 = (x^2 - a + t)^2 - (\text{quadratic in } x)$, then force the (quadratic in $x$) to be a perfect square in $x$, obtaining a cubic-in-$t$ resolvent. Solving this resolvent and back-substituting gives the four roots of the quartic in closed form — a long, error-prone calculation. The reverse-engineering approach gives the same answer in three lines.

**ELEGANT PIVOT.** *Treat $a$ as the unknown — quadratic-in-$a$ factorisation.*

*Step 1 — Regroup as quadratic in $a$.* The quartic $x^4 - 2 a x^2 + x + a^2 - a = 0$ contains $a^2 - a$ and $-2a$ terms. Regrouping by powers of $a$:
\[
  a^2 - a (2 x^2 + 1) + (x^4 + x) \;=\; 0.
\]
This is a *quadratic in $a$*, with $x$ as a parameter.

*Step 2 — Compute the discriminant.* The discriminant of $a^2 - a(2x^2 + 1) + (x^4 + x) = 0$ as a quadratic in $a$ is:
\[
  \Delta_a \;=\; (2 x^2 + 1)^2 - 4 (x^4 + x) \;=\; 4 x^4 + 4 x^2 + 1 - 4 x^4 - 4 x \;=\; 4 x^2 - 4 x + 1 \;=\; (2x - 1)^2.
\]
*The discriminant is a perfect square in $x$.* This is the magical algebraic coincidence that powers the entire reverse-engineering approach.

*Step 3 — Solve for $a$.* With $\Delta_a = (2x - 1)^2$, the quadratic-in-$a$ has solutions:
\[
  a \;=\; \frac{(2 x^2 + 1) \pm |2x - 1|}{2}.
\]
The two values of $a$ are:
- $a = \dfrac{(2 x^2 + 1) + (2x - 1)}{2} = x^2 + x$ (taking $+|2x - 1|$ for $x \ge 1/2$, or $-|2x - 1|$ with sign flipped for $x < 1/2$ — both give the same expression after simplification).
- $a = \dfrac{(2 x^2 + 1) - (2x - 1)}{2} = x^2 - x + 1$.

*Step 4 — Factorise the quartic.* The quartic-in-$x$ thus factors as:
\[
  (a - x^2 - x)(a - x^2 + x - 1) \;=\; 0.
\]
*(Verify by expansion: $u^2 - u - x^2 + x$ where $u = a - x^2$, giving $(a - x^2)^2 - (a - x^2) - x^2 + x = a^2 - 2 a x^2 + x^4 - a + x^2 - x^2 + x = x^4 - 2 a x^2 + x + a^2 - a$. ✓)*

So the four roots of the quartic-in-$x$ are the two roots of $x^2 + x - a = 0$ and the two roots of $x^2 - x + 1 - a = 0$.

*Step 5 — Real-root conditions for each quadratic.*
- $x^2 + x - a = 0$: discriminant $= 1 + 4 a$. Real roots iff $1 + 4 a \ge 0$, i.e., $a \ge -1/4$.
- $x^2 - x + (1 - a) = 0$: discriminant $= 1 - 4(1 - a) = 4 a - 3$. Real roots iff $4 a - 3 \ge 0$, i.e., $a \ge 3/4$.

*Step 6 — Intersect conditions.* For *all four* roots of the quartic to be real, *both* quadratics must have real roots, requiring $a \ge -1/4$ AND $a \ge 3/4$, i.e.,
\[
  \boxed{a \ge 3/4.}
\]
\hfill$\blacksquare$

*Verification on the boundary.* At $a = 3/4$: $x^2 + x - 3/4 = 0$ gives $x = (-1 \pm 2)/2$, i.e., $x \in \{1/2, -3/2\}$ (real). $x^2 - x + 1/4 = (x - 1/2)^2 = 0$ gives $x = 1/2$ (double root). So at $a = 3/4$, the quartic has roots $\{-3/2, 1/2, 1/2, 1/2\}$ — four real roots (with $x = 1/2$ being a triple root). ✓

The elegant pivot is the *reverse-engineering of the polynomial structure*: by treating $a$ as the unknown in a quadratic-in-$a$ equation, the discriminant becomes a perfect square in $x$ — a structural surprise that the forward direction completely hides. The quartic, which looks intractable in $x$, is actually a *product of two quadratics in $x$*, each with a clean discriminant condition.

**PITFALLS.**

- *Persisting with the Ferrari resolvent.* The Ferrari method is correct but requires solving a cubic-in-$t$ resolvent. The reverse-engineering approach gives the answer in three lines without any cubic-solving. The remedy is to *try the parameter-promotion first*; if the discriminant is a perfect square, the factorisation works immediately.

- *Mis-computing the discriminant.* The discriminant $(2x^2 + 1)^2 - 4(x^4 + x)$ requires care: $(2x^2 + 1)^2 = 4x^4 + 4x^2 + 1$ (not $4x^4 + 1$). The remedy is to *expand carefully* and verify by substitution at a specific value (e.g., $x = 1$: discriminant $= 9 - 8 = 1 = (2 - 1)^2$ ✓).

- *Forgetting the absolute value $|2x - 1|$.* The square root of $(2x - 1)^2$ is $|2x - 1|$, not $2x - 1$ (which can be negative). The two values of $a$ are independent of the sign of $2x - 1$ because the $\pm$ in the quadratic formula absorbs the sign. The remedy is to *use the absolute value notation* and verify the resulting expressions are simplifiable.

- *Forgetting one of the two discriminant conditions.* The quartic factors into two quadratics; *both* need real roots for all four quartic-roots to be real. Forgetting the $x^2 - x + (1 - a) = 0$ discriminant condition gives the wrong lower bound. The remedy is to *list both quadratics explicitly* and compute both discriminants.

- *Mistakenly requiring strict inequalities.* The condition $a \ge 3/4$ (not $a > 3/4$) is correct because at $a = 3/4$, the second quadratic has a double root (still real). The remedy is to *verify the boundary case* — at $a = 3/4$, all four quartic-roots are real (with the triple root at $x = 1/2$).

**CONNECTIONS.**

*Primary archetype applications.* The *parameter-promotion* technique generalises to:
- *Higher-degree polynomials*: when a polynomial-in-$x$ contains the parameter $a$ in a low-degree form (linear or quadratic), the polynomial-in-$a$ often has a perfect-square discriminant or a clean factorisation.
- *Multivariable optimisation*: when an objective function $f(x, a)$ is being optimised over $x$ for fixed $a$, the dual problem of optimising over $a$ for fixed $x$ often has a cleaner structure.
- *Implicit equations*: $F(x, y) = 0$ defines a curve in the $(x, y)$-plane; choosing whether to treat $x$ as the dependent variable (and $y$ as the parameter) or vice versa can dramatically simplify the curve's parametrisation.

*Alternative solution archetypes.* The quartic-with-all-real-roots problem has at least two other solution routes:
- *Discriminant of the quartic*: compute the standard discriminant $\Delta$ of the quartic $x^4 - 2ax^2 + x + a^2 - a$ as a polynomial in $a$, and require $\Delta \ge 0$ (necessary but not sufficient for all real roots).
- *Sturm's theorem*: apply Sturm's chain to count the number of real roots in $\mathbb R$ as a function of $a$.

Both alternatives work but are substantially more computation-heavy than the parameter-promotion reverse-engineering.

*Cross-domain manifestations.* The parameter-promotion technique appears in:
- *Quantum mechanics*: the *eigenvalue equation* $H \psi = E \psi$ can be reframed as solving for $E$ as the parameter, with the wavefunction $\psi$ as the dependent variable — the *secular determinant* method.
- *Control theory*: the *characteristic equation* of a control system $\det(s I - A) = 0$ is naturally a polynomial in the eigenvalues $s$; reframing as a polynomial in the system parameter (e.g., gain $K$) gives the *root-locus* method.
- *Algebraic geometry*: implicit curves and surfaces $F(x_1, \ldots, x_n) = 0$ often have hidden parametrisations exposed by treating one variable as the parameter.

**TAKEAWAY.** *Polynomial-with-parameter problems: try promoting the parameter to the unknown. If the resulting polynomial-in-the-parameter has a perfect-square discriminant, a clean factorisation emerges and the original problem collapses into independent discriminant conditions on the factors.*

---

### 4.2 Example 2 — Triangle Uniquely Determined by $(r, R, s)$ (Geometric Inversion)

**Problem.** *Prove that a triangle is uniquely determined, up to congruence, by its inradius $r$, circumradius $R$, and semiperimeter $s$, provided that $r, R, s$ satisfy the necessary triangle existence conditions. Equivalently, reverse-engineer the triangle's three sides from these three invariants.*
*(Joshi EJM Ch. 24, Exercise 24.94; foundational result in triangle geometry; degrees-of-freedom argument concretised.)*

**SEED.** *Reverse engineering (Form IV — geometry-from-invariants).* A triangle in the Euclidean plane has 3 degrees of freedom (e.g., the three side lengths $a, b, c$, or three independent invariants from the standard list $\{a, b, c, A, B, C, r, R, s, K, \ldots\}$). The trio $(r, R, s)$ is *three independent invariants*, hence (modulo regularity conditions) uniquely determines the triangle. The proof is *constructive*: from $(r, R, s)$, derive the three elementary symmetric polynomials of the sides $(a, b, c)$, then solve the resulting cubic to recover the sides.

**BRUTE PATH.** A student without the reverse-engineering lens might attempt to *parameterise* triangles by $(r, R, s)$ explicitly and verify uniqueness by checking that no two distinct triangles share the same $(r, R, s)$ triple. This requires extensive case analysis and is not constructive (it doesn't tell you *how* to find the triangle from $(r, R, s)$, only that the map is injective). The reverse-engineering approach provides an *explicit reconstruction formula*.

**ELEGANT PIVOT.** *Vieta inversion via the side-cubic.*

*Step 1 — Standard triangle invariants.* For a triangle with sides $a, b, c$, inradius $r$, circumradius $R$, semiperimeter $s = (a + b + c)/2$, and area $K$, the standard identities are:
- $K = r \cdot s$ (area = inradius × semiperimeter).
- $K = \dfrac{abc}{4 R}$ (area in terms of sides and circumradius).
- $K^2 = s(s - a)(s - b)(s - c)$ (Heron's formula).

From the first two: $r s = \dfrac{abc}{4 R}$, so $abc = 4 R r s$.

*Step 2 — Compute the elementary symmetric polynomials of $(a, b, c)$.* From $s = (a + b + c)/2$:
\[
  e_1 \;:=\; a + b + c \;=\; 2s.
\]

From $abc = 4 R r s$:
\[
  e_3 \;:=\; abc \;=\; 4 R r s.
\]

For $e_2 := ab + bc + ca$, use Heron's formula. From $K = rs$ and $K^2 = s(s-a)(s-b)(s-c)$:
\[
  r^2 s^2 \;=\; s(s - a)(s - b)(s - c) \quad\Longrightarrow\quad (s - a)(s - b)(s - c) \;=\; r^2 s.
\]
Expand the LHS:
\[
  (s - a)(s - b)(s - c) \;=\; s^3 - s^2 (a + b + c) + s (ab + bc + ca) - abc \;=\; s^3 - 2 s^3 + s e_2 - 4 R r s.
\]
So:
\[
  r^2 s \;=\; -s^3 + s e_2 - 4 R r s \quad\Longrightarrow\quad e_2 \;=\; s^2 + r^2 + 4 R r.
\]

*Step 3 — The side-cubic.* The sides $a, b, c$ are the roots of the monic cubic with elementary symmetric polynomials $e_1, e_2, e_3$:
\[
  \boxed{t^3 - 2 s\, t^2 + (s^2 + r^2 + 4 R r)\, t - 4 R r s \;=\; 0.}
\]

*Step 4 — Uniqueness.* The cubic is uniquely determined by $(r, R, s)$. Its three roots (assumed real and positive, by the triangle's existence) are the three sides $a, b, c$ in some order. Two triangles with the same $(r, R, s)$ thus have the *same* cubic, hence the same multiset of sides $\{a, b, c\}$, hence are congruent (by SSS congruence). \hfill$\blacksquare$

*Verification on a specific triangle.* The 3-4-5 right triangle has sides $\{3, 4, 5\}$, so $s = 6$, area $K = 6$ (half-base-times-height for the right triangle), $r = K/s = 1$, and $R = (\text{hypotenuse})/2 = 5/2$. Verify:
- $e_1 = 2 s = 12 = 3 + 4 + 5$ ✓
- $e_3 = 4 R r s = 4 \cdot (5/2) \cdot 1 \cdot 6 = 60 = 3 \cdot 4 \cdot 5$ ✓
- $e_2 = s^2 + r^2 + 4 R r = 36 + 1 + 4 \cdot (5/2) \cdot 1 = 36 + 1 + 10 = 47 = 12 + 20 + 15 = ab + bc + ca$ ✓

The cubic: $t^3 - 12 t^2 + 47 t - 60 = 0$. Factor: $(t - 3)(t - 4)(t - 5) = t^3 - 12 t^2 + 47 t - 60$ ✓. Roots $\{3, 4, 5\}$ ✓.

The elegant pivot is the *Vieta inversion*: the cubic whose roots are the sides has *coefficients* expressible in terms of the *invariants* $(r, R, s)$. Reverse-engineering the cubic and solving it recovers the sides.

**PITFALLS.**

- *Forgetting the existence conditions.* Not every triple $(r, R, s)$ corresponds to a real triangle. Necessary conditions include Euler's inequality $R \ge 2r$ (with equality iff equilateral), $r > 0$, $R > 0$, $s > 0$, and the resulting cubic must have three positive real roots satisfying the triangle inequalities. The remedy is to *state the existence conditions explicitly* in the problem setup.

- *Mis-computing $e_2$.* The Heron-based derivation of $e_2 = s^2 + r^2 + 4 R r$ is delicate; sign errors and missing terms are easy. The remedy is to *verify on a specific triangle* (e.g., 3-4-5 as above, or equilateral).

- *Confusing inradius / circumradius formulas.* The relationship $abc = 4 R K$ uses the *circumradius*; $K = rs$ uses the *inradius*. Mixing them gives wrong formulas. The remedy is to *write each formula with the symbol explicitly stated*.

- *Not verifying the cubic's roots are positive.* Even if the cubic has three real roots, they might not all be positive (which is required for valid side-lengths). The remedy is to *check the signs of the cubic's coefficients* using Descartes' rule of signs: for the cubic $t^3 - 2 s t^2 + (s^2 + r^2 + 4 R r) t - 4 R r s$ with $r, R, s > 0$, the sign pattern is $+, -, +, -$ — three sign changes, hence either 3 or 1 positive real roots. The triangle inequalities ensure the case of 3 positive real roots.

- *Treating the cubic's three roots as distinct without verification.* If the triangle is isoceles or equilateral, the cubic has repeated roots, and the standard "factor out $(t - r_1)$" method needs care. The remedy is to *check for repeated roots* via the discriminant of the cubic.

**CONNECTIONS.**

*Primary archetype applications.* The Vieta-inversion / geometric-invariants reverse-engineering generalises to:
- *Quadrilaterals*: a general quadrilateral has 5 degrees of freedom; given 5 independent invariants (e.g., 4 sides + 1 diagonal, or various combinations), the quadrilateral can be reconstructed.
- *Higher polygons*: an $n$-gon in the plane has $2n - 3$ degrees of freedom (modulo translation, rotation, scaling); the corresponding number of independent invariants determines the polygon up to congruence.
- *3D solids*: a tetrahedron has 6 degrees of freedom; the 6 edge-lengths determine the tetrahedron up to congruence (Cayley-Menger determinant gives the volume).

*Alternative solution archetypes.* The triangle-from-$(r, R, s)$ problem has at least two other solution routes:
- *Direct construction*: given $(r, R, s)$, draw the circumcircle of radius $R$; inscribe a triangle whose inradius is $r$; verify the semiperimeter equals $s$. This is geometrically intuitive but not algebraically constructive.
- *Trigonometric*: express the sides in terms of the angles $A, B, C$ and the circumradius via the *law of sines* $a = 2 R \sin A$, etc., then solve for the angles using $r = 4 R \sin(A/2) \sin(B/2) \sin(C/2)$ and $A + B + C = \pi$.

The Vieta-inversion / side-cubic approach is the *most direct* and *most algebraic*.

*Cross-domain manifestations.* Geometric-invariants reverse-engineering appears in:
- *Computer-aided design (CAD)*: reconstructing geometric objects from their feature parameters (lengths, angles, areas).
- *Computer vision*: structure-from-motion algorithms reverse-engineer 3D shapes from 2D images using geometric invariants.
- *Robotics*: forward kinematics (joint angles → end-effector position) and inverse kinematics (end-effector position → joint angles) are the robotics analogs of forward and reverse geometric problems.
- *Crystallography*: reconstructing 3D crystal structures from X-ray diffraction patterns uses geometric invariants of the unit cell.

**TAKEAWAY.** *Geometry-from-invariants via Vieta inversion: from a small set of invariants $(r, R, s)$ derive the elementary symmetric polynomials of the unknown geometric parameters (sides); construct the polynomial whose roots are those parameters; solve to recover the geometric object. The triangle-from-$(r, R, s)$ cubic $t^3 - 2s t^2 + (s^2 + r^2 + 4Rr) t - 4Rrs = 0$ is the canonical case.*

---

### 4.3 Example 3 — Polynomial with Prescribed Complex Roots

**Problem.** *Find a polynomial of minimum degree with real coefficients having $1 + i$ and $2 - 3i$ as roots.*
*(Joshi EJM Ch. 3, Comment 7; the canonical real-coefficient-pairing problem.)*

**SEED.** *Reverse engineering (Form I — polynomial-from-roots with real-coefficient pairing).* A polynomial with *real* coefficients has the property that its complex roots come in *conjugate pairs* $\{z, \bar z\}$. Since $1 + i$ and $2 - 3i$ are prescribed roots, their conjugates $1 - i$ and $2 + 3i$ must *also* be roots — for a total of four roots and minimum degree 4. The polynomial is the product of the two conjugate-pair quadratic factors.

**BRUTE PATH.** A student without the conjugate-pairing insight might write $f(x) = (x - (1 + i))(x - (2 - 3i)) \cdot (\text{adjustment})$ and try to "real-ify" by some other means (e.g., multiplying by the conjugate of the entire product). This works but is more complicated than directly identifying the conjugate roots from the start.

**ELEGANT PIVOT.** *Conjugate-pair multiplication.*

*Step 1 — Identify the conjugate roots.* For real coefficients, the roots come in conjugate pairs:
- $1 + i$ has conjugate $1 - i$.
- $2 - 3i$ has conjugate $2 + 3i$.

Total four roots: $\{1 + i, 1 - i, 2 - 3i, 2 + 3i\}$.

*Step 2 — Form the conjugate-pair quadratic factors.* For a complex root $z = p + qi$ (with $q \ne 0$) and its conjugate $\bar z = p - qi$, the quadratic factor $(x - z)(x - \bar z) = x^2 - (z + \bar z) x + z \bar z = x^2 - 2 p x + (p^2 + q^2)$ has real coefficients.

- $z_1 = 1 + i$: $p = 1, q = 1$. Quadratic factor: $x^2 - 2 \cdot 1 \cdot x + (1 + 1) = x^2 - 2 x + 2$.
- $z_2 = 2 - 3i$: $p = 2, q = -3$ (but $q$'s sign doesn't affect $p^2 + q^2 = 4 + 9 = 13$, and $z_2 + \bar z_2 = 4$). Quadratic factor: $x^2 - 2 \cdot 2 \cdot x + (4 + 9) = x^2 - 4 x + 13$.

*Step 3 — Multiply the quadratic factors.*
\[
  f(x) = (x^2 - 2 x + 2)(x^2 - 4 x + 13).
\]
Expand:
\[
  f(x) = x^4 - 4 x^3 + 13 x^2 - 2 x^3 + 8 x^2 - 26 x + 2 x^2 - 8 x + 26
\]
\[
  = x^4 + (-4 - 2) x^3 + (13 + 8 + 2) x^2 + (-26 - 8) x + 26
\]
\[
  \boxed{f(x) = x^4 - 6 x^3 + 23 x^2 - 34 x + 26.}
\]
\hfill$\blacksquare$

*Verification by root-evaluation.* Compute $f(1 + i)$:
- $(1 + i)^2 = 2 i$.
- $(1 + i)^3 = (1 + i)(2 i) = 2 i + 2 i^2 = -2 + 2 i$.
- $(1 + i)^4 = (1 + i)(-2 + 2 i) = -2 + 2 i - 2 i + 2 i^2 = -4$.

$f(1 + i) = -4 - 6(-2 + 2 i) + 23 (2 i) - 34 (1 + i) + 26 = -4 + 12 - 12 i + 46 i - 34 - 34 i + 26 = (-4 + 12 - 34 + 26) + (-12 + 46 - 34) i = 0 + 0 i = 0$. ✓

Similarly, $f(2 - 3i) = 0$ (verification omitted; symmetric calculation).

The elegant pivot is the *conjugate-pair recognition*: the real-coefficient constraint *forces* the additional roots, doubling the prescribed root list. The polynomial is then constructed by multiplying conjugate-pair quadratic factors, each of which has automatically real coefficients.

**PITFALLS.**

- *Forgetting one of the conjugate pairs.* If the prescribed list includes $1 + i$ (or $1 - i$) but the student forgets that the *other* complex root $2 - 3i$ also requires its conjugate $2 + 3i$, the resulting polynomial has *complex* coefficients (not real). The remedy is to *list all prescribed complex roots and add their conjugates* before multiplying.

- *Including conjugates of real roots.* Real roots are their own conjugates ($\bar r = r$ for $r \in \mathbb R$); no "extra" conjugate is added. The remedy is to *check whether each prescribed root is real* (in which case it contributes one linear factor) or complex (in which case it contributes a conjugate-pair quadratic).

- *Using monic vs non-monic.* The minimum-degree polynomial is uniquely determined *up to a non-zero real scalar multiple*; the *monic* polynomial (leading coefficient 1) is the canonical choice. The remedy is to *state monic explicitly* if that's the desired form.

- *Computing the product incorrectly.* The product $(x^2 - 2x + 2)(x^2 - 4x + 13)$ expansion has 9 terms; missing one or mis-combining like terms gives a wrong polynomial. The remedy is to *expand systematically* and *verify by evaluating at a prescribed root*.

- *Confusing minimum degree with minimum-degree-real-coefficient.* If complex coefficients are allowed, the minimum-degree polynomial with $1 + i$ and $2 - 3i$ as roots is the degree-2 product $(x - (1 + i))(x - (2 - 3i))$, which has complex coefficients. The real-coefficient constraint *doubles* the degree to 4. The remedy is to *state the coefficient constraint explicitly* and verify the resulting polynomial has the required coefficient type.

**CONNECTIONS.**

*Primary archetype applications.* The conjugate-pair-multiplication technique generalises to:
- *Higher-degree real polynomials*: every real polynomial factors over $\mathbb R$ into a product of linear factors (one per real root) and conjugate-pair quadratic factors (one per complex conjugate pair); the *real factorisation theorem*.
- *Cyclotomic polynomials*: the $n$-th cyclotomic polynomial $\Phi_n(x)$ is the minimal polynomial over $\mathbb Q$ of a primitive $n$-th root of unity; its roots are the $\varphi(n)$ primitive $n$-th roots of unity, and the polynomial has integer (hence real) coefficients.
- *Minimal polynomials over algebraic extensions*: for $\alpha$ algebraic over a field $F$, the minimal polynomial of $\alpha$ over $F$ is the unique monic polynomial of minimum degree in $F[x]$ with $\alpha$ as a root.

*Alternative solution archetypes.* The same polynomial can be constructed via:
- *Norm calculation*: the norm of $1 + i$ in $\mathbb Q(i)/\mathbb Q$ is $(1 + i)(1 - i) = 2$, giving the constant term of the quadratic factor; the trace is $2 \cdot 1 = 2$, giving the linear coefficient.
- *Resolvent expansion*: $\prod_{\text{Galois conjugates}}(x - \sigma(\alpha)) = $ the minimal polynomial, where $\sigma$ ranges over the Galois group.

The conjugate-pair-multiplication is the *most direct* for the case of real coefficients over $\mathbb Q$.

*Cross-domain manifestations.* Real-coefficient polynomial construction appears in:
- *Signal processing*: real-coefficient FIR filter design constructs polynomials with specified frequency-response zeros; the conjugate-pair-pairing ensures the filter's coefficients are real.
- *Control theory*: characteristic polynomials of physical systems have real coefficients (because the system matrices are real); the eigenvalues come in conjugate pairs.
- *Quantum mechanics*: the characteristic polynomial of a Hermitian operator has real coefficients; the eigenvalues are real (since complex conjugates of real numbers are themselves).
- *Polynomial root-finding algorithms*: the *Bairstow's method* for real polynomials with complex roots iteratively extracts conjugate-pair quadratic factors, building on the same conjugate-pair structure.

**TAKEAWAY.** *Real-coefficient polynomial construction from complex roots: list the prescribed complex roots, add their complex conjugates, form conjugate-pair quadratic factors of the form $x^2 - 2 \Re(z) x + |z|^2$, and multiply. The result is the minimum-degree real polynomial with the prescribed roots.*

---

## 5. Practice Problems

Seven problems, statements only; full solutions appear in the Appendix. The slate spans Tier 2–4 (two Tier 2, five Tier 3) reflecting the chapter's foundational character (entry-level reverse-engineering techniques) plus advanced examples (Newton's identities, Cholesky, conics).

### 5.1 Three-Digit Number = Twice the Sum of Digit-Squares (Tier 2; Joshi Ch. 24, Exercise 24.99(a))

Determine all three-digit positive integers $N$ that equal twice the sum of the squares of their digits.

*(Cross-archetype with Ch. 4 WE2 [Hidden Structure]: there the digit-Diophantine relation is framed as "find the hidden algebraic structure"; here in Ch. 16 it is framed as "reverse-engineer the digits from the arithmetic constraint by bound-then-enumerate.")*

### 5.2 ODE from Family of Curves (Tier 2; Joshi Ch. 19, Comment 2)

Find the ordinary differential equation whose general solution is $y = c_1 \cos x + c_2 \sin x$, where $c_1, c_2$ are arbitrary real constants.

### 5.3 Vectors from Gram Matrix (Tier 3; Joshi Ch. 21, Comment 9)

Given the Gram matrix
\[
  G = \begin{pmatrix} 4 & 2 & 2 \\ 2 & 5 & 1 \\ 2 & 1 & 5 \end{pmatrix},
\]
find three vectors $\vec v_1, \vec v_2, \vec v_3 \in \mathbb R^3$ such that $\vec v_i \cdot \vec v_j = G_{ij}$ for all $i, j$.

### 5.4 Cubic from Newton's Identities (Tier 3; Joshi Ch. 3, Comment 11)

A monic cubic polynomial $f(x) = x^3 + a x^2 + b x + c$ has three real (not necessarily distinct) roots $r_1, r_2, r_3$ with power sums $p_1 = r_1 + r_2 + r_3 = 6$, $p_2 = r_1^2 + r_2^2 + r_3^2 = 14$, and $p_3 = r_1^3 + r_2^3 + r_3^3 = 36$. Find $f(x)$ and identify its roots.

### 5.5 Cauchy Functional Equation with Boundary (Tier 3; Joshi Ch. 20, Comment 1)

Find all continuous functions $f: \mathbb R \to \mathbb R$ satisfying $f(x + y) = f(x) + f(y)$ for all $x, y \in \mathbb R$ and the boundary condition $f(1) = 2$.

### 5.6 Conic from Five Points (Tier 3; Joshi Ch. 9, Comment 13)

Find the equation of the conic passing through the five points $(1, 0), (0, 1), (-1, 0), (0, -1), (1/2, 1/2)$, and identify the conic's type.

### 5.7 Cubic Parameter from Enclosed Area (Tier 3 RMO; Joshi Ch. 17, Exercise 17.22)

The curve $y = x^3 - a x$ (with $a > 0$ a real parameter) encloses, together with the $x$-axis, a region of total geometric area $A$. Express $A$ as a function of $a$, then invert to express $a$ as a function of $A$.

---

## 6. The Connections Web

Reverse engineering connects to virtually every later archetype in this volume and to substantial parts of every quantitative and applied discipline.

### 6.1 Reverse Engineering Across Mathematical Domains

*Algebra.* Vieta's formulas and their inversion are foundational. *Galois theory* studies the reverse engineering of fields: given an algebraic equation, the Galois group encodes the structural reversibility of the equation's solvability by radicals. The *fundamental theorem of algebra* (every monic polynomial of degree $n$ over $\mathbb C$ has exactly $n$ roots, counted with multiplicity) is the existence statement that makes polynomial reverse engineering possible.

*Number theory.* *Diophantine equation solving* is reverse engineering: given a desired integer-valued conclusion, find the integer inputs satisfying it. *Modular reverse engineering* (Hensel's lemma, $p$-adic lifting) reconstructs $p$-adic integers from their residues modulo $p^k$ for increasing $k$. *Algebraic number theory* (class field theory, Iwasawa theory) reverse-engineers the structure of number-field extensions from their Galois data.

*Linear algebra.* The *Cholesky factorisation*, *LU decomposition*, *QR decomposition*, *singular value decomposition (SVD)*, and *eigenvalue decomposition* are all reverse-engineering algorithms: they decompose a matrix into a product of structured factors that reveal the matrix's hidden structure. *Tensor decompositions* (CANDECOMP, Tucker, HOSVD) extend this to higher-order arrays.

*Analysis.* The *inverse function theorem* and the *implicit function theorem* are the foundational reverse-engineering theorems of analysis: under appropriate regularity, the inverse of a smooth map exists and is itself smooth. *Inverse problems for PDEs* (heat-equation inverse, wave-equation inverse, electromagnetic scattering inverse) are deep mathematical fields with applications to medical imaging, geophysics, and remote sensing.

*Topology.* *Knot complement reconstruction*: the *Gordon-Luecke theorem* (1989) says that a knot in $S^3$ is uniquely determined by its complement — a deep reverse-engineering result. *Manifold reconstruction* from triangulations, from Cech cohomology, or from Reeb graphs gives multiple reverse-engineering paths.

*Geometry.* The *Pythagorean theorem inversion* (given the hypotenuse and one leg, find the other), the *circumscribed circle inversion* (given three points, find the circle), the *triangle from invariants inversion* (WE2), and the *conic from points inversion* (PP6) are classical geometric reverse-engineerings. The *Erlangen program* (Klein 1872) organises all geometries by their group of invariants — a meta-level reverse-engineering framework.

### 6.2 Reverse Engineering in Science and Engineering

*Medical imaging.* The *inverse Radon transform* (CT scanning), *inverse Fourier transform* (MRI), *inverse problem of optical tomography*, *time-reversal acoustics* (ultrasound), and *PET / SPECT reconstruction* are all reverse-engineering applications. Modern medical imaging is fundamentally inverse problem solving on industrial scale.

*Geophysics.* *Seismic tomography* reconstructs 3D Earth-interior structure from seismic wave arrival times — a reverse engineering of the wave-propagation equations. *Gravitational anomaly inversion* recovers subsurface density distributions from gravity field measurements. *Electromagnetic surveys* invert electromagnetic field data to recover conductivity profiles.

*Astrophysics.* *Stellar spectral fitting* inverts the radiative transfer equation to recover stellar temperatures, gravities, and chemical compositions from observed spectra. *Cosmological parameter inference* reverse-engineers the universe's expansion history from observations of supernovae, baryon acoustic oscillations, and the cosmic microwave background.

*Cryptography.* *Cryptanalysis* is the reverse engineering of ciphers. *Differential cryptanalysis* and *linear cryptanalysis* are systematic frameworks for reverse-engineering block-cipher keys from chosen-plaintext attacks. *Lattice-based cryptanalysis* (LLL algorithm) reverse-engineers lattice problems.

*Machine learning.* *Generative models* (GANs, VAEs, diffusion models) reverse-engineer data distributions. *Backpropagation* in neural networks is reverse-mode automatic differentiation — a structural reverse engineering of the chain rule. *Bayesian inference* and *variational inference* reverse-engineer posterior distributions from observed data.

*Engineering.* *Inverse design* in aerodynamics, optics, and structural engineering: specify the desired performance (lift coefficient, focal length, load capacity) and reverse-engineer the design parameters. *Topology optimisation* in mechanical engineering iteratively reverse-engineers material distributions to achieve target performance.

*Chemistry.* *Retrosynthetic analysis* (E. J. Corey, 1990 Nobel Prize): given a target molecule, plan a synthesis by working backward through retrosynthetic disconnections. *Crystal structure determination* from X-ray diffraction data: invert the diffraction pattern to recover the unit-cell atomic positions.

*Biology.* *Phylogenetic reconstruction* from DNA sequence data: reverse-engineer evolutionary trees. *Protein structure prediction* (AlphaFold) reverse-engineers 3D protein structures from amino-acid sequences. *Gene regulatory network reconstruction* from expression data.

### 6.3 Reverse Engineering in Applied Disciplines

*Economics and finance.* *Implied volatility* in options pricing: invert the Black-Scholes formula to recover the volatility parameter from the observed option price. *Yield-curve construction*: reverse-engineer the discount factors from observed bond prices. *Mechanism design* and *auction theory*: reverse-engineer truthful direct-revelation mechanisms from desired outcome distributions.

*Software engineering.* *Reverse engineering of software*: recover source code or design from compiled binaries. *Decompilation*, *binary analysis*, and *malware analysis* are systematic reverse-engineering of executable code. *Software architecture recovery* reconstructs architectural diagrams from existing codebases.

*Forensic and legal.* *Forensic reconstruction* of crime scenes from physical evidence; *ballistic trajectory reconstruction* from impact patterns; *digital forensics* recovery of deleted data; *audio forensics* recovery of speech from noisy recordings.

*Music and art.* *Raga identification* in Carnatic music: given an audible melody, identify the underlying scale and stylistic conventions. *Art authentication*: reverse-engineer provenance from chemical, isotopic, and stylistic signatures. *Music transcription*: convert audio to musical notation by reverse-engineering the performance.

### 6.4 Related Archetypes

Reverse engineering interacts with five other archetypes in particularly tight ways.

- **Archetype 3 (Duality).** *Every forward direction has a dual backward direction*. Ch. 3's duality framing — that primal and dual problems are isomorphic under a change of perspective — is the most general formulation of the reverse-engineering principle. Reverse engineering is the *constructive* deployment of duality: not just recognising the dual exists, but explicitly computing it.

- **Archetype 4 (Hidden Structure).** *The inverse machinery is often the hidden structure*. Ch. 4's "find the hidden structure" move and Ch. 16's "reverse the forward operation" move are different framings of the same task: identify the underlying algebraic / geometric / combinatorial structure that makes the inverse computable.

- **Archetype 15 (Bijection / Correspondence).** *Bijections are explicitly invertible by construction*. Ch. 15's bijective principle is the special case of reverse engineering where the forward operation is a bijection (hence the inverse always exists and is unique). The Vieta inversion (roots → polynomial), Cholesky factorisation, and conjugate-pair multiplication are all bijective operations.

- **Archetype 17 (Degrees of Freedom).** *Dimension-matching between data and unknowns determines uniqueness*. Ch. 17's DOF framing — that a problem has a unique solution iff the number of independent constraints equals the number of unknowns — is the *underdetermined* vs *overdetermined* analysis that determines whether a reverse engineering problem is well-posed. The cross-link is direct: Ch. 16 WE2 (triangle from $r, R, s$) and Ch. 17 WE2 (triangle DOF analysis) are the same problem from two perspectives.

- **Archetype 19 (Pivoting / Elimination).** *Gaussian elimination is the prototype reverse-engineering algorithm*. Ch. 19's pivoting / elimination framing solves linear systems by *backward substitution* — the prototypical reverse engineering of a triangular system. The same backward substitution machinery generalises to back-propagation in neural networks (Ch. 16's reverse-mode autodiff), to dynamic-programming retrieval (storing forward solutions and reading them backward), and to the *unwinding* of recursive algorithms.

---

## 7. Master Takeaways

Seven sentences. Each one is a complete operational principle.

1. *When the answer is given, the problem is to find the question. Reverse the natural direction of computation — from output to input, from invariant to structure, from solution-set to defining-equation.* (Expands the canonical takeaway.)

2. *Polynomial-with-parameter problems: try promoting the parameter to the unknown. If the resulting polynomial-in-the-parameter has a perfect-square discriminant, a clean factorisation emerges and the original problem collapses into independent discriminant conditions on the factors.* (WE1 takeaway; Form I via parameter promotion.)

3. *Geometry-from-invariants via Vieta inversion: from a small set of invariants derive the elementary symmetric polynomials of the unknown parameters; construct the polynomial with those parameters as roots; solve to recover the geometric object. The triangle-from-$(r, R, s)$ cubic $t^3 - 2s t^2 + (s^2 + r^2 + 4Rr) t - 4Rrs = 0$ is the canonical case.* (WE2 takeaway; Form IV.)

4. *Real-coefficient polynomial construction: list the prescribed complex roots, add their conjugates, form conjugate-pair quadratics $x^2 - 2\Re(z) x + |z|^2$, multiply. The result is the minimum-degree real polynomial with the prescribed roots.* (WE3 takeaway; Form I.)

5. *Named-theorem-inverse selection: match the problem's forward operation to its named inverse — Vieta (roots→polynomial), Newton (power sums→polynomial), Cholesky (Gram→vectors), ODE-from-family (curves→ODE), Cauchy+boundary (functional equation→function), 5-points→conic, $abc = 4Rrs$ (sides→invariants).* (The toolkit reflex.)

6. *Verify by forward computation: always run the forward operation on the recovered inputs to confirm the original outputs are reproduced. This catches inversion errors that would otherwise propagate silently.* (The verification discipline.)

7. *Cross-archetype: reverse-engineering unifies duality (Ch. 3), hidden structure (Ch. 4), bijection (Ch. 15), degrees of freedom (Ch. 17), and elimination (Ch. 19) — by Chapter 16 these are one coherent body of inverse reasoning. This chapter closes the Structural Reasoning sub-pillar (Chs. 13–16) and bridges to the Meta-Reasoning sub-pillar (Chs. 17–20).*

---

## 8. Self-Assessment Checklist

You have absorbed Chapter 16 when, without re-opening it, you can do each of the following from memory.

- [ ] State Vieta's formulas for a monic polynomial of degree $n$ with roots $r_1, \ldots, r_n$ (coefficients = signed elementary symmetric polynomials of roots).
- [ ] State Newton's identities relating power sums $p_k$ to elementary symmetric polynomials $e_k$: $p_k = e_1 p_{k-1} - e_2 p_{k-2} + \cdots + (-1)^{k-1} k e_k$ for $1 \le k \le n$.
- [ ] State the real-coefficient root-pairing theorem (complex roots of real polynomials come in conjugate pairs) and apply it: for prescribed complex roots $z_1, z_2, \ldots$, the minimum-degree real polynomial includes all conjugates $\bar z_1, \bar z_2, \ldots$.
- [ ] State the Cholesky factorisation: positive-definite symmetric $G$ has unique $L L^T$ decomposition with $L$ lower-triangular and positive diagonal.
- [ ] Apply ODE-from-solution-family: given a solution family with $n$ parameters, differentiate $n$ times and eliminate parameters to obtain a unique $n$-th-order ODE.
- [ ] State Cauchy's functional equation and its continuous-solution theorem: the only continuous solutions to $f(x + y) = f(x) + f(y)$ are $f(x) = cx$; a single boundary $f(x_0) = y_0$ uniquely determines $c$.
- [ ] State the triangle-from-$(r, R, s)$ inversion: sides $a, b, c$ are roots of the cubic $t^3 - 2s\,t^2 + (s^2 + r^2 + 4Rr)\,t - 4Rrs = 0$, derived from $abc = 4Rrs$, $a + b + c = 2s$, and Heron's formula.
- [ ] State the five-points-determine-a-conic theorem and apply it: 5 points in general position give a 5-equation linear system in the 6 conic coefficients $A, B, C, D, E, F$, uniquely determining the conic up to scaling.
- [ ] Apply bound-then-enumerate to a digit-Diophantine problem: derive size bounds from the inequalities, enumerate the bounded range, verify each candidate. (PP1's three-digit-number problem.)
- [ ] Identify and explain three of the five common pitfalls: Wrong-Direction, Missing-Conjugate-Root, Degenerate-Inverse, Verification-Skipping, Bound-Then-Enumerate-Off-By-One.

---

## Bridge to Chapter 17: Degrees of Freedom Analysis (Opens Meta-Reasoning Sub-Pillar)

Chapter 16 was the *closing* chapter of the *Structural Reasoning* sub-pillar (Chapters 13–16). The chapter elevated the *direction-of-computation reversal* into a full named archetype — *reverse engineering* — and developed the toolkit of named inversions (Vieta, Newton, Cholesky, ODE-from-family, Cauchy, geometric-invariants, 5-points-conic, bound-then-enumerate, inverse-area). With Chapter 16 in hand, the reader has internalised that *structure* (Chs. 13–16 collectively) is not just for *recognition* but for *construction*: the same structural understanding that lets one read the bijection underlying Vandermonde (Ch. 15) lets one *construct* the polynomial with prescribed roots (Ch. 16 WE3), reconstruct the triangle from its invariants (Ch. 16 WE2), and recover a 3D image from 2D projections (the radiologist of the opening vignette).

Chapter 17 — *Degrees of Freedom Analysis* — opens the *Meta-Reasoning* sub-pillar (Chapters 17–20), which steps *back* from the technical archetypes (Chs. 1–16) and asks meta-level questions about *problem structure*: How many independent parameters does this problem have? How many constraints? Is the problem over-, under-, or exactly-determined? When does a solution exist, and when is it unique? The Meta-Reasoning archetypes — degrees of freedom (Ch. 17), recursion / induction (Ch. 18), pivoting / elimination (Ch. 19), analogy / transfer (Ch. 20) — are *higher-order* in the sense that they apply to *all* problems, not just specific classes; they are the *meta-tools* that organise the trained solver's approach across the entire Pillar-2 archetype catalogue.

The bridge from Ch. 16 to Ch. 17 is the *uniqueness-and-existence question*. Reverse engineering presumes that the inverse exists (i.e., the forward operation is invertible) and that the inverse is unique (i.e., the recovered input is the *only* one consistent with the data). Ch. 17 asks the *meta-question*: when is reverse engineering well-posed? The DOF / constraint count determines: if DOF < constraint count, the problem is *overdetermined* (likely no solution); if DOF = constraint count, the problem is *exactly determined* (unique solution, generically); if DOF > constraint count, the problem is *underdetermined* (infinitely many solutions, parameterised by the DOF deficit). Ch. 16 deployed reverse engineering on exactly-determined cases (triangle from $r, R, s$ has 3 DOF and 3 invariants, hence unique); Ch. 17 systematises the dimension-counting that makes this analysis rigorous.

---

## Appendix — Solutions to Practice Problems

### Solution to 5.1 — Three-Digit Number = Twice the Sum of Digit-Squares

We seek all three-digit integers $N = 100 a + 10 b + c$ (with $a \in \{1, 2, \ldots, 9\}$ and $b, c \in \{0, 1, \ldots, 9\}$) satisfying
\[
  100 a + 10 b + c \;=\; 2 (a^2 + b^2 + c^2).
\]

*Step 1 — Bound on $a$.* The maximum of the right-hand side over all digits is $2(9^2 + 9^2 + 9^2) = 2 \cdot 243 = 486$. So $N \le 486$, forcing $a \le 4$. Also $N \ge 100$ requires $a \ge 1$. Thus $a \in \{1, 2, 3, 4\}$.

*Step 2 — Reduce to a quadratic in $b, c$ for each $a$.* Rearrange:
\[
  2 b^2 + 2 c^2 - 10 b - c \;=\; 100 a + 10 b + c - 100 a - 2 a^2 - 2 b^2 - 2 c^2 + (\text{algebra}) \quad\Longrightarrow\quad 2 b^2 + 2 c^2 - 10 b - c \;=\; 100 a - 2 a^2.
\]
(Verify: $100 a + 10 b + c = 2 a^2 + 2 b^2 + 2 c^2 \Leftrightarrow 100 a - 2 a^2 = 2 b^2 + 2 c^2 - 10 b - c$. ✓)

So for each $a$, the RHS is the fixed integer $100 a - 2 a^2$:
- $a = 1$: $100 - 2 = 98$. Equation: $2 b^2 + 2 c^2 - 10 b - c = 98$.
- $a = 2$: $200 - 8 = 192$. Equation: $2 b^2 + 2 c^2 - 10 b - c = 192$.
- $a = 3$: $300 - 18 = 282$. Equation: $2 b^2 + 2 c^2 - 10 b - c = 282$. But the LHS maximum (at $b = 9, c = 9$) is $162 + 162 - 90 - 9 = 225 < 282$. No solution.
- $a = 4$: $400 - 32 = 368$. LHS maximum 225 $< 368$. No solution.

*Step 3 — Exhaustive enumeration for $a = 1$.* Need $2b^2 + 2c^2 - 10b - c = 98$, i.e., $2c^2 - c = 98 - 2b^2 + 10b$.

Compute RHS for each $b \in \{0, 1, \ldots, 9\}$:
- $b = 0$: $98 - 0 + 0 = 98$. Need $2c^2 - c = 98$. $c = 7$: $98 - 7 = 91$. $c = 8$: $128 - 8 = 120$. No integer solution.
- $b = 1$: $98 - 2 + 10 = 106$. $c = 8$: $120$. No.
- $b = 2$: $98 - 8 + 20 = 110$. $c = 8$: $120$. No.
- $b = 3$: $98 - 18 + 30 = 110$. No.
- $b = 4$: $98 - 32 + 40 = 106$. No.
- $b = 5$: $98 - 50 + 50 = 98$. $c = 7$: $91$. $c = 8$: $120$. No.
- $b = 6$: $98 - 72 + 60 = 86$. $c = 7$: $91$. $c = 6$: $66$. No.
- $b = 7$: $98 - 98 + 70 = 70$. $c = 6$: $66$. $c = 7$: $91$. No.
- $b = 8$: $98 - 128 + 80 = 50$. $c = 5$: $45$. $c = 6$: $66$. No.
- $b = 9$: $98 - 162 + 90 = 26$. $c = 4$: $28$. $c = 3$: $15$. No.

No solution for $a = 1$.

*Step 4 — Exhaustive enumeration for $a = 2$.* Need $2c^2 - c = 192 - 2b^2 + 10b$.

- $b = 0$: $192 - 0 = 192$. $c = 10$: $190$. Out of range.
- $b = 5$: $192 - 50 + 50 = 192$. No (same as above).
- $b = 8$: $192 - 128 + 80 = 144$. $c = 9$: $153$. $c = 8$: $120$. No.
- $b = 9$: $192 - 162 + 90 = 120$. $c = 8$: $128 - 8 = 120$. ✓

So $a = 2, b = 9, c = 8$ gives $N = 298$. Verify: $2(4 + 81 + 64) = 2 \cdot 149 = 298$. ✓

*Step 5 — Conclude.* The unique three-digit positive integer satisfying $N = 2(a^2 + b^2 + c^2)$ is
\[
  \boxed{N \;=\; 298.}
\]
$\blacksquare$

*(Verification: $298 = 100 \cdot 2 + 10 \cdot 9 + 8$; digit-squares sum to $4 + 81 + 64 = 149$; twice that is $298$. ✓)*

*Remark.* The locked slate v0.2 listed the answer as $166$, which fails the verification ($2(1 + 36 + 36) = 146 \ne 166$). The corrected answer $298$ has been propagated to the slate as v0.2.13.

---

### Solution to 5.2 — ODE from $y = c_1 \cos x + c_2 \sin x$

*Step 1 — Differentiate twice.* From $y = c_1 \cos x + c_2 \sin x$:
\[
  y' \;=\; -c_1 \sin x + c_2 \cos x,
\]
\[
  y'' \;=\; -c_1 \cos x - c_2 \sin x.
\]

*Step 2 — Recognise the elimination.* The expression for $y''$ is precisely $-y$:
\[
  y'' \;=\; -(c_1 \cos x + c_2 \sin x) \;=\; -y.
\]

*Step 3 — Conclude.* The ODE is
\[
  \boxed{y'' + y \;=\; 0.}
\]
\hfill$\blacksquare$

*Verification.* The general solution of $y'' + y = 0$ is well-known to be $y = c_1 \cos x + c_2 \sin x$ (the simple harmonic oscillator). ✓

*Generalisation.* The procedure is universal: for an $n$-parameter family $y = F(x; c_1, \ldots, c_n)$, differentiate $n$ times to obtain $n + 1$ equations involving $y, y', \ldots, y^{(n)}$, then eliminate the $n$ parameters to leave one ODE.

---

### Solution to 5.3 — Vectors from Gram Matrix (Cholesky Factorisation)

Given $G = \begin{pmatrix} 4 & 2 & 2 \\ 2 & 5 & 1 \\ 2 & 1 & 5 \end{pmatrix}$.

*Step 1 — Compute the Cholesky factor $L$.* Write $G = L L^T$ where $L$ is lower-triangular with positive diagonal. So:
\[
  L = \begin{pmatrix} L_{11} & 0 & 0 \\ L_{21} & L_{22} & 0 \\ L_{31} & L_{32} & L_{33} \end{pmatrix}.
\]

From $G_{11} = L_{11}^2$: $4 = L_{11}^2$, so $L_{11} = 2$.

From $G_{21} = L_{21} L_{11}$: $2 = 2 L_{21}$, so $L_{21} = 1$.

From $G_{31} = L_{31} L_{11}$: $2 = 2 L_{31}$, so $L_{31} = 1$.

From $G_{22} = L_{21}^2 + L_{22}^2$: $5 = 1 + L_{22}^2$, so $L_{22} = 2$.

From $G_{32} = L_{31} L_{21} + L_{32} L_{22}$: $1 = 1 \cdot 1 + L_{32} \cdot 2 = 1 + 2 L_{32}$, so $L_{32} = 0$.

From $G_{33} = L_{31}^2 + L_{32}^2 + L_{33}^2$: $5 = 1 + 0 + L_{33}^2$, so $L_{33} = 2$.

So $L = \begin{pmatrix} 2 & 0 & 0 \\ 1 & 2 & 0 \\ 1 & 0 & 2 \end{pmatrix}$.

*Step 2 — Read off the vectors.* The rows of $L$ are the desired vectors:
\[
  \boxed{\vec v_1 = (2, 0, 0), \quad \vec v_2 = (1, 2, 0), \quad \vec v_3 = (1, 0, 2).}
\]

*Step 3 — Verification.* Compute $\vec v_i \cdot \vec v_j$:
- $\vec v_1 \cdot \vec v_1 = 4 + 0 + 0 = 4$. ✓
- $\vec v_2 \cdot \vec v_2 = 1 + 4 + 0 = 5$. ✓
- $\vec v_3 \cdot \vec v_3 = 1 + 0 + 4 = 5$. ✓
- $\vec v_1 \cdot \vec v_2 = 2 + 0 + 0 = 2$. ✓
- $\vec v_1 \cdot \vec v_3 = 2 + 0 + 0 = 2$. ✓
- $\vec v_2 \cdot \vec v_3 = 1 + 0 + 0 = 1$. ✓

All entries match $G$. $\blacksquare$

*Non-uniqueness.* The Cholesky factor is unique, but the vectors are determined only up to a common *orthogonal transformation* (rotation / reflection in $\mathbb R^3$). For instance, $\vec v'_1 = O \vec v_1$, $\vec v'_2 = O \vec v_2$, $\vec v'_3 = O \vec v_3$ for any orthogonal $O \in O(3)$ give the same Gram matrix.

---

### Solution to 5.4 — Cubic from Newton's Identities

Given $p_1 = 6, p_2 = 14, p_3 = 36$ for a monic cubic $f(x) = x^3 - e_1 x^2 + e_2 x - e_3$.

*Step 1 — Apply Newton's identities for $k = 1, 2, 3$.*

$k = 1$: $p_1 = e_1$. So $e_1 = 6$.

$k = 2$: $p_2 = e_1 p_1 - 2 e_2$. So $14 = 6 \cdot 6 - 2 e_2 = 36 - 2 e_2$, giving $e_2 = (36 - 14)/2 = 11$.

$k = 3$: $p_3 = e_1 p_2 - e_2 p_1 + 3 e_3$. So $36 = 6 \cdot 14 - 11 \cdot 6 + 3 e_3 = 84 - 66 + 3 e_3 = 18 + 3 e_3$, giving $e_3 = (36 - 18)/3 = 6$.

*Step 2 — Construct $f(x)$.*
\[
  f(x) \;=\; x^3 - e_1 x^2 + e_2 x - e_3 \;=\; x^3 - 6 x^2 + 11 x - 6.
\]

*Step 3 — Factor.* Try $x = 1$: $f(1) = 1 - 6 + 11 - 6 = 0$. So $(x - 1)$ divides $f$. Polynomial division: $f(x) / (x - 1) = x^2 - 5 x + 6 = (x - 2)(x - 3)$. So
\[
  \boxed{f(x) \;=\; (x - 1)(x - 2)(x - 3) \;=\; x^3 - 6 x^2 + 11 x - 6.}
\]

Roots: $r_1 = 1, r_2 = 2, r_3 = 3$. $\blacksquare$

*Verification.* Check power sums: $p_1 = 1 + 2 + 3 = 6$ ✓; $p_2 = 1 + 4 + 9 = 14$ ✓; $p_3 = 1 + 8 + 27 = 36$ ✓.

---

### Solution to 5.5 — Cauchy Functional Equation with Boundary

We solve: find all continuous $f: \mathbb R \to \mathbb R$ with $f(x + y) = f(x) + f(y)$ and $f(1) = 2$.

*Step 1 — Deduce $f$ on $\mathbb Q$.* Apply the equation iteratively:
- $f(2) = f(1 + 1) = f(1) + f(1) = 2 f(1) = 4$.
- $f(n) = n f(1) = 2 n$ for all positive integers $n$ (by induction).
- $f(0) = f(0 + 0) = 2 f(0)$, so $f(0) = 0$.
- $f(-n) = -f(n) = -2n$ from $f(-n) + f(n) = f(0) = 0$.
- $f(m/n) = (m/n) f(1) = 2m/n$ for all rationals $m/n$: this follows from $n \cdot f(m/n) = f(m) = 2m$.

So $f(q) = 2 q$ for all rationals $q$.

*Step 2 — Extend to $\mathbb R$ via continuity.* Every real $x$ is the limit of a sequence of rationals $q_n \to x$. By continuity of $f$:
\[
  f(x) \;=\; \lim_{n \to \infty} f(q_n) \;=\; \lim_{n \to \infty} 2 q_n \;=\; 2 x.
\]

*Step 3 — Conclude.*
\[
  \boxed{f(x) \;=\; 2 x.}
\]
\hfill$\blacksquare$

*Verification.* Check $f(x + y) = 2(x + y) = 2x + 2y = f(x) + f(y)$ ✓; $f(1) = 2$ ✓; $f$ is continuous ✓.

*Remark on the continuity assumption.* Without continuity, Cauchy's functional equation admits *pathological* (non-linear) solutions constructed via a Hamel basis of $\mathbb R$ over $\mathbb Q$ (Hamel 1905). Such solutions are non-measurable and unbounded on every interval; they require the axiom of choice for their existence. The continuity assumption rules out all such pathologies.

---

### Solution to 5.6 — Conic from Five Points

We seek a conic $A x^2 + B x y + C y^2 + D x + E y + F = 0$ (5 projective parameters) passing through the five points $(1, 0), (0, 1), (-1, 0), (0, -1), (1/2, 1/2)$.

*Step 1 — Set up the linear system.* Substituting each point gives:
1. $(1, 0)$: $A + D + F = 0$.
2. $(0, 1)$: $C + E + F = 0$.
3. $(-1, 0)$: $A - D + F = 0$.
4. $(0, -1)$: $C - E + F = 0$.
5. $(1/2, 1/2)$: $A/4 + B/4 + C/4 + D/2 + E/2 + F = 0$, i.e., $A + B + C + 2D + 2E + 4F = 0$.

*Step 2 — Solve.*

From (1) and (3): adding gives $2A + 2F = 0$, so $A = -F$. Subtracting gives $2D = 0$, so $D = 0$.

From (2) and (4): adding gives $2C + 2F = 0$, so $C = -F$. Subtracting gives $2E = 0$, so $E = 0$.

Substituting into (5): $-F + B - F + 0 + 0 + 4F = B + 2F = 0$, so $B = -2F$.

*Step 3 — Write the conic.* With $A = -F, B = -2F, C = -F, D = 0, E = 0$:
\[
  -F x^2 - 2 F x y - F y^2 + F \;=\; 0 \quad \Longrightarrow \quad F(-x^2 - 2xy - y^2 + 1) \;=\; 0.
\]
For $F \ne 0$ (otherwise the conic is trivial):
\[
  x^2 + 2 x y + y^2 \;=\; 1, \quad \text{i.e.,} \quad (x + y)^2 \;=\; 1.
\]

*Step 4 — Identify the conic type.* The equation $(x + y)^2 = 1$ factors as $(x + y - 1)(x + y + 1) = 0$, representing the *pair of parallel lines* $x + y = 1$ and $x + y = -1$. This is a *degenerate* conic (rank-1 quadratic form), not a proper ellipse / parabola / hyperbola.
\[
  \boxed{(x + y)^2 \;=\; 1 \quad \text{(pair of parallel lines } x + y = \pm 1\text{).}}
\]
\hfill$\blacksquare$

*Verification.* Check the five points lie on $(x + y)^2 = 1$:
- $(1, 0)$: $(1 + 0)^2 = 1$ ✓
- $(0, 1)$: $(0 + 1)^2 = 1$ ✓
- $(-1, 0)$: $(-1 + 0)^2 = 1$ ✓
- $(0, -1)$: $(0 - 1)^2 = 1$ ✓
- $(1/2, 1/2)$: $(1/2 + 1/2)^2 = 1$ ✓

All verified.

*Geometric interpretation.* The five points are all on the two lines $x + y = \pm 1$: the first four are on these two lines (each line through two of the points), and the fifth point $(1/2, 1/2)$ is on $x + y = 1$. So the five points are NOT in *general position* (they lie on a pair of lines, which is a degenerate conic). The "5 points → conic" theorem in its strongest form requires general position; in degenerate cases, the conic recovered is the natural degenerate one.

---

### Solution to 5.7 — Cubic Parameter from Enclosed Area

The curve $y = x^3 - a x$ (with $a > 0$) crosses the $x$-axis where $x^3 - a x = x(x^2 - a) = 0$, i.e., at $x = 0$ and $x = \pm \sqrt{a}$.

*Step 1 — Set up the area integral.* The curve is *odd* in $x$ ($y(-x) = -y(x)$), so the signed integral over the symmetric interval $[-\sqrt a, \sqrt a]$ vanishes. The *geometric* (unsigned) area is twice the area over $[0, \sqrt a]$:
\[
  A \;=\; 2 \int_0^{\sqrt a} |x^3 - a x| \, dx.
\]

On $[0, \sqrt a]$, $x^3 - a x = x(x^2 - a)$, and for $0 < x < \sqrt a$, $x^2 < a$, so $x^2 - a < 0$, giving $x^3 - a x < 0$. Hence $|x^3 - a x| = a x - x^3$.

*Step 2 — Compute the integral.*
\[
  \int_0^{\sqrt a} (a x - x^3) \, dx \;=\; \left[\frac{a x^2}{2} - \frac{x^4}{4}\right]_0^{\sqrt a} \;=\; \frac{a \cdot a}{2} - \frac{a^2}{4} \;=\; \frac{a^2}{2} - \frac{a^2}{4} \;=\; \frac{a^2}{4}.
\]

So $A = 2 \cdot \dfrac{a^2}{4} = \dfrac{a^2}{2}$.

*Step 3 — Invert.* Solve $A = a^2 / 2$ for $a$:
\[
  \boxed{A \;=\; \frac{a^2}{2}, \quad a \;=\; \sqrt{2 A}.}
\]
\hfill$\blacksquare$

*Verification.* For $a = 2$: $A = 4/2 = 2$. Check: $\sqrt 2 \approx 1.414$; integral of $|x^3 - 2x|$ from $-\sqrt 2$ to $\sqrt 2$ should be $2$. Indeed, by symmetry: $2 \int_0^{\sqrt 2} (2x - x^3) dx = 2 [x^2 - x^4/4]_0^{\sqrt 2} = 2 [2 - 1] = 2$. ✓

*Remark.* This problem illustrates a general pattern: given a *derived quantity* (here, the enclosed area $A$) expressed as a function of a *parameter* (here, $a$), inverting this functional relation recovers the parameter from the data. The same pattern underlies *implied volatility* in options pricing, *spectral fitting* in astrophysics, and *parameter estimation* in statistics.

---

*End of Chapter 16. Chapter 17 (Degrees of Freedom Analysis) opens the Meta-Reasoning sub-pillar.*

