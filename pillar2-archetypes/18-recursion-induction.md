---
chapter: 18
archetype: Recursion / Induction
subtitle: "Solve for One Step; Repeat to Infinity"
category: Meta-Reasoning (Archetypes 17–20) — second chapter
related_archetypes: [11, 13, 15, 17, 19]
key_gems: [A13, E01, E02, E03, E10, F11]
  - "Principle of mathematical induction: to prove $P(n)$ for all $n \\ge n_0$, it suffices to prove (i) the base case $P(n_0)$ and (ii) the inductive step $P(n) \\Rightarrow P(n + 1)$; equivalently for strong induction, $P(n_0), P(n_0 + 1), \\ldots, P(n) \\Rightarrow P(n + 1)$"
  - "Linear-recurrence closed form: a recurrence $T_n = c_1 T_{n-1} + c_2 T_{n-2} + \\cdots + c_k T_{n-k}$ has characteristic polynomial $\\chi(r) = r^k - c_1 r^{k-1} - \\cdots - c_k$; for distinct roots $r_1, \\ldots, r_k$, the general solution is $T_n = \\sum_i A_i r_i^n$ with $A_i$ determined by initial conditions"
  - "Fibonacci closed form (Binet): $F_n = (\\varphi^n - \\psi^n)/\\sqrt 5$ where $\\varphi = (1 + \\sqrt 5)/2$ and $\\psi = (1 - \\sqrt 5)/2$ are roots of $r^2 - r - 1 = 0$; matrix form $\\begin{pmatrix}1 & 1\\\\1 & 0\\end{pmatrix}^n = \\begin{pmatrix}F_{n+1} & F_n\\\\F_n & F_{n-1}\\end{pmatrix}$"
  - "Wallis reduction formula: $I_n = \\int_0^{\\pi/2} \\sin^n x\\,dx$ satisfies $I_n = \\frac{n-1}{n} I_{n-2}$ via integration by parts, with $I_0 = \\pi/2$ and $I_1 = 1$; specialised to $I_5 = 8/15$ and $I_6 = 5\\pi/32$"
  - "Tower-of-Hanoi recurrence: $T_n = 2 T_{n-1} + 1$ with $T_1 = 1$ has closed form $T_n = 2^n - 1$ via the substitution $T_n + 1 = 2(T_{n-1} + 1) \\Rightarrow T_n + 1 = 2^n$; the recursive solution structure mirrors the algorithm"
  - "Telescoping identity for inverse tangents: $\\tan^{-1}\\frac{1}{k^2 + k + 1} = \\tan^{-1}(k + 1) - \\tan^{-1}(k)$ collapses partial sums to $\\tan^{-1}(n + 1) - \\tan^{-1}(1)$; similarly $\\cot^{-1}(2k^2) = \\tan^{-1}(2k + 1) - \\tan^{-1}(2k - 1)$"
  - "Pascal's identity: $\\binom{n + 1}{r} = \\binom{n}{r - 1} + \\binom{n}{r}$, provable algebraically by factorial manipulation or combinatorially via the partition of $r$-subsets of $\\{1, \\ldots, n + 1\\}$ by whether they contain the element $n + 1$"
  - "Discrete Laplace equation (gambler's ruin): $P_k = (P_{k-1} + P_{k+1})/2$ on $0 < k < N$ with $P_0 = 1, P_N = 0$ has linear solution $P_k = 1 - k/N$; the characteristic polynomial $(r - 1)^2 = 0$ has a double root, yielding linear solutions"
  - "Strong-induction shift-coefficient technique: $S(n + 1) = a S(n) + (\\text{multiple of modulus})$, the canonical inductive-step pattern for divisibility proofs like $25 \\mid 7^{2n} + 2^{3n - 3} \\cdot 3^{n - 1}$"
  - "Binary-string Fibonacci bijection: the number of binary strings of length $n$ with no two consecutive 1's satisfies $a_n = a_{n - 1} + a_{n - 2}$ with $a_1 = 2, a_2 = 3$, giving $a_n = F_{n + 2}$ — a combinatorial-Fibonacci recurrence"
canonical_takeaway: "Solve for one step; repeat to infinity. A problem on $n$ becomes tractable by relating it to the same problem on $n - 1$ (induction) or by expressing the answer as a sequence satisfying a recurrence; the trick is identifying the right inductive parameter or recursion variable, and the inductive step is the engine that propagates a single solved case to the whole infinite family."
status: locked
last_revised: 2026-05-29
locked_on: 2026-05-29
sourcing_note: "All worked examples and practice problems in this chapter are drawn from K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), or from JEE / RMO / INMO examinations commented on in that text. See Blueprint §6.2 for the sourcing rule and `pillar2-archetypes/_template/joshi-problems-locked.md` §Ch. 18 for the locked slate. **Verification audit for this chapter caught zero slate errors** — all 10 answers (3 WE + 7 PP) verified clean on first pass (third clean-slate audit of Pillar 2 after Ch. 15 and Ch. 17). The chapter is the **second** of the Meta-Reasoning sub-pillar (Chs. 17–20), following Ch. 17 (Degrees of Freedom Analysis) and bridging to Ch. 19 (Pivoting / Elimination). **Cross-archetype notes**: WE2 ($25 \\mid 7^{2n} + 2^{3n-3} \\cdot 3^{n-1}$, JEE 1982) is the modular-induction archetype's flagship problem and connects to Ch. 14 (Parity / Modularity) where divisibility *recognition* is the move; here in Ch. 18 the move is divisibility *propagation* by induction. PP4 (Tower of Hanoi) and PP7 (binary strings without consecutive 1's) are both classical recursion-with-Fibonacci-flavour, with PP7's $a_n = F_{n+2}$ a direct combinatorial-Fibonacci bijection of the kind catalogued in Ch. 15 (Bijection / Correspondence). PP6 (gambler's ruin) is the discrete-Laplace recurrence whose continuous limit is the boundary-value problem $-\\Delta u = 0$ — bridging probabilistic recursion to PDE theory."
---

# Chapter 18 — Recursion / Induction

## *Solve for One Step; Repeat to Infinity*

---

## Opening Vignette

A Commissioner of Railway Safety (CRS) chief inspector at the Indian Railways Northern Circle headquarters in Lucknow is signing off the safety certification for a newly electrified 287-kilometre rail corridor running from Lucknow to Kanpur and onward to Allahabad. The corridor passes through *forty-three* intermediate stations, each with its own overhead traction substation, signalling installations, level crossings, and platform safety hardware. The pre-electrification certification protocol, established by the Railway Board over decades of operational experience, is *inductive* in its structural design: certification of station $k + 1$ is permitted only after certification of all stations $1, 2, \ldots, k$ has been completed, and the certification of station $k + 1$ is itself a *minimal increment* — the chief inspector verifies only the incremental safety conditions specific to station $k + 1$'s new hardware (substation transformer integrity, signalling-cable insulation resistance, contact-wire tension within tolerances) rather than re-running the full forty-seven-test battery on all stations $1, \ldots, k$. The inductive scheme is *the* design choice that makes the entire forty-three-station certification feasible: a naïve "test every station against every other station" protocol would require $\binom{43}{2} = 903$ pairwise inter-substation compatibility checks, infeasible within the four-month window. The inductive protocol replaces this with $43$ incremental certifications, each taking three to five working days, totalling a manageable hundred-and-thirty-day campaign. The CRS chief signs off on the *inductive scheme* itself — that is, she certifies the *single inductive step* (verifying that incremental testing at station $k + 1$ is sufficient given prior certification of stations $1, \ldots, k$), and the base case (station 1 has been independently certified by an offline test campaign before the inductive process begins). Once those two certifications are in place, the chief delegates the routine inductive sweeps to the section inspectors; her own attention is freed for the next corridor's design review.

Now turn to a different scene. A senior algorithm engineer at BYJU's, the Bangalore-headquartered online learning company, is sitting at her workstation late at night refining the *adaptive learning recommendation engine* that decides what Class 9 mathematics lesson to recommend next to a student who has just completed her current lesson. The recommendation algorithm faces a structurally massive task: BYJU's catalogue contains approximately 1,800 distinct micro-lessons for the Class 9 mathematics syllabus, each tagged with prerequisites, learning objectives, conceptual difficulty levels, and topic categories. The naïve approach — pre-compute the optimal next-lesson for every possible (student-state, completed-lesson) pair — would require evaluating $10^{12}$ pairs (rough order: a million students × a million possible state-completion combinations), infeasible at BYJU's daily recommendation load. The algorithm engineer's design choice, ratified during the company's algorithms-team design review, is to express the entire recommendation logic as *a single inductive recurrence*: given the student's current state $s_k$ at step $k$ and the just-completed lesson $\ell_k$, the recommended next lesson $\ell_{k + 1}$ and the updated student state $s_{k + 1}$ are computed by a *single function* $f(s_k, \ell_k)$, evaluated in approximately 12 milliseconds per call. The verification of the algorithm's correctness across all 1,800 lessons and all 10 million BYJU's students reduces to verifying *two things*: (i) the base case — the function $f$ produces a reasonable recommendation for the initial state $s_0$ (no completed lessons); (ii) the inductive step — given any plausible $(s_k, \ell_k)$, the recommendation $\ell_{k + 1}$ has been pedagogically vetted to be the correct next-lesson. Once $(i)$ and $(ii)$ are verified by the curriculum-design team and the algorithms-team's offline-evaluation pipeline, the recursion handles the entire 10-million-student × 1,800-lesson space automatically. The engineer's correctness-verification effort is *proportional to a single step*, not to the total number of student trajectories — *recursion compresses the verification work* from astronomical to manageable.

These two scenes look entirely unrelated. A Commissioner of Railway Safety certifying a forty-three-station rail corridor in Uttar Pradesh; an algorithm engineer at BYJU's certifying a 1,800-lesson recommendation engine in Bangalore. Yet they share the most important cognitive habit of the entire chapter: *solve for one step; repeat to infinity*. Both professionals replace an infeasible *flat* verification campaign with a feasible *inductive* one — the CRS chief replaces 903 pairwise station-inter-checks with 43 incremental certifications plus one inductive-scheme review; the algorithm engineer replaces $10^{12}$ pre-computations with one base-case verification plus one inductive-step verification. The cognitive operation is identical — recognise that the problem has *recursive structure*, identify the *inductive parameter* (station index $k$ in the railway case, lesson-completion index $k$ in the BYJU's case), prove the *inductive step* (the move from $k$ to $k + 1$), establish the *base case*, and trust the recursion to propagate the certification across the entire infinite (or astronomically large) family.

This is *Recursion / Induction*. It is the *second* chapter of the *Meta-Reasoning* sub-pillar (Chapters 17–20), following Chapter 17 (Degrees of Freedom Analysis) and bridging to Chapter 19 (Pivoting / Elimination). The chapter develops the toolkit (mathematical induction, strong induction, linear recurrence closed-form theory, reduction formulas for integrals, telescoping identities, the Tower of Hanoi recurrence, the discrete Laplace equation for random walks, generating functions for combinatorial recurrences) and the recurring patterns (identifying the inductive parameter; writing down the inductive step; choosing between weak and strong induction; recognising shift-coefficient and double-induction techniques for difficult divisibility proofs; interpreting linear recurrences via characteristic-polynomial roots). The chapter has three structural threads. The first is *recursion as the structural-compression engine*: a recursion of length $n$ compresses an $n$-step computation into a 1-step description plus a base case, the most efficient encoding of an infinite family of solutions. The second is *inductive-parameter identification*: the trained solver, faced with a problem indexed by some parameter, asks *"what is the inductive parameter?"* — often $n$, sometimes the more subtle choices of *strong induction*, *double induction*, or *induction on a derived quantity*. The third is *the recursion ↔ induction equivalence*: every recursion defines an inductive statement (the recursion is correct), and every inductive proof of a statement parameterised by $n$ has an algorithmic recursive interpretation; the two are dual aspects of the same cognitive operation.

> *Solve for one step; repeat to infinity. A problem on $n$ becomes tractable by relating it to the same problem on $n - 1$ (induction) or by expressing the answer as a sequence satisfying a recurrence; the trick is identifying the right inductive parameter or recursion variable.*

---

## 1. The Archetype Defined

### 1.1 Formal Definition

We make the intuition precise.

\begin{definition}[Recursion / Induction Archetype]
A *recursion / induction* approach to a problem is the strategy of *expressing the solution as a function of a discrete parameter $n$ that satisfies a recurrence relation*. The archetype is the discipline of (i) identifying an *inductive parameter* $n$ (usually a non-negative integer indexing the problem's natural size, but sometimes a derived quantity); (ii) expressing the answer as a sequence $\{T(n)\}$ or a statement $\{P(n)\}$ parametrised by $n$; (iii) establishing a *recurrence* or *inductive step* linking $T(n + 1)$ to $T(n)$ (and possibly $T(n - 1), T(n - 2), \ldots$) or proving the implication $P(n) \Rightarrow P(n + 1)$; (iv) verifying the *base case* $T(n_0)$ or $P(n_0)$ for some small $n_0$; and (v) optionally, solving the recurrence for a closed-form expression $T(n) = \phi(n)$ when one is available.
\end{definition}

Three remarks unpack the definition.

First, the *inductive-parameter identification* (Step (i)) is the cognitively central step. The naïve choice is "induct on $n$" where $n$ is the problem's natural size; this works for the vast majority of problems but fails for the deeper ones. The trained solver, when faced with a non-trivial induction, asks *"what is the right inductive parameter?"* — and learns to spot the subtler choices: *strong induction* (assume the result for all $k \le n$ rather than just $k = n$); *double induction* (induct on two parameters $r$ and $n$ simultaneously); *induction on a derived quantity* (e.g., the height of a tree, the depth of a recursion, the number of digits, the size of a subset); *induction on a partial order* (well-founded induction on a poset structure). The PP2 problem of this chapter (divisibility of $r!$ into the product of $r$ consecutive integers) requires double induction; the WE2 problem requires strong induction with a shift-coefficient.

Second, the *inductive-step proof* (Step (iii)) is the engine. The inductive step takes the form *"assume $P(n)$; prove $P(n + 1)$"* (weak induction) or *"assume $P(n_0), P(n_0 + 1), \ldots, P(n)$; prove $P(n + 1)$"* (strong induction). For recurrences, the equivalent task is to *express $T(n + 1)$ in terms of $T(n)$* (and possibly earlier terms) by direct algebraic manipulation. The flagship technique for divisibility proofs (WE2) is the *shift-coefficient technique*: write $S(n + 1) = a \cdot S(n) + b \cdot M$ where $M$ is the modulus; if both $a S(n)$ (divisible by $M$ by IH) and $b M$ (divisible by $M$ trivially) are divisible by $M$, then so is $S(n + 1)$.

Third, the *closed-form derivation* (Step (v)) is the optional finishing flourish. Many recurrences have known closed-form solutions: the geometric recurrence $T_n = c T_{n-1}$ gives $T_n = c^n T_0$; the affine recurrence $T_n = c T_{n-1} + d$ gives $T_n = c^n (T_0 + d/(c-1)) - d/(c-1)$ (when $c \ne 1$); the linear recurrence $T_n = c_1 T_{n-1} + c_2 T_{n-2} + \cdots + c_k T_{n-k}$ has characteristic polynomial $\chi(r) = r^k - c_1 r^{k-1} - \cdots - c_k$, and the general solution is $T_n = \sum_i A_i r_i^n$ for distinct roots $r_i$ (with polynomial-in-$n$ corrections for repeated roots). The Fibonacci recurrence's Binet formula $F_n = (\varphi^n - \psi^n)/\sqrt 5$ is the canonical example. For non-linear recurrences (e.g., $T_n = T_{n-1}^2 + 1$), closed forms are rare; the recurrence itself is the answer.

The chapter encounters five characteristic forms of recursion / induction.

- **Form I — Weak induction (the standard form).** Prove $P(n_0)$ and $P(n) \Rightarrow P(n + 1)$; conclude $P(n)$ for all $n \ge n_0$. *Examples.* WE1 (Fibonacci matrix power), PP5 (Pascal's identity).

- **Form II — Strong induction.** Prove $P(n_0)$ and $P(n_0), P(n_0 + 1), \ldots, P(n) \Rightarrow P(n + 1)$. *Examples.* WE2 (JEE 1982 divisibility), and the standard fundamental-theorem-of-arithmetic proof.

- **Form III — Linear-recurrence closed form.** Solve $T_n = c_1 T_{n-1} + c_2 T_{n-2} + \cdots + c_k T_{n-k}$ via characteristic-polynomial roots and initial-condition matching. *Examples.* PP4 (Tower of Hanoi), PP6 (gambler's ruin), PP7 (binary strings without consecutive 1's).

- **Form IV — Reduction formula (integral / summation recurrences).** Express an integral or sum at parameter $n$ in terms of the same integral or sum at parameter $n - 1$ or $n - 2$ via integration by parts or summation by parts. *Examples.* WE3 (Wallis $I_n = \frac{n-1}{n} I_{n-2}$).

- **Form V — Telescoping.** Express the summand as a difference $a_k - a_{k-1}$ so that the partial sum collapses to $a_n - a_0$. *Examples.* PP1 ($\cot^{-1}(2k^2)$ telescope), PP3 (JEE 1999 $\tan^{-1}$ telescope).

### 1.2 The Core Principle

Stripped to its essence, the principle is one sentence.

> *Solve for one step; repeat to infinity.*

This sentence captures the recurrent observation that, across mathematics, computer science, and applied science, the *single inductive step* is the entire substantive content of an inductive proof; the recursion is the *automatic propagation* of that step across the infinite (or astronomical) range of indices. The CRS chief signs off on one inductive scheme + one base case to certify forty-three stations; the BYJU's engineer verifies one inductive step + one base case to deploy a million-trajectory recommendation engine. The cognitive work is *constant-bounded*; the recursion does the propagation for free.

The principle generalises far beyond classical mathematics. In *computer science*, recursive algorithms (quicksort, mergesort, divide-and-conquer in general) are the basic algorithmic-design pattern; correctness proofs are inductive on the input size. In *type theory* and *proof assistants* (Coq, Lean, Agda), structural induction over inductive data types is the fundamental proof tactic; the entire propositions-as-types correspondence (Curry–Howard) treats induction and recursion as dual aspects of the same construction. In *physics*, the dynamics of a discrete-time system $x_{n + 1} = F(x_n)$ is a recursion; the stability of equilibria, the period of orbits, and the chaotic-vs-regular transition are all inductive properties of the iterated map. In *economics*, dynamic-programming Bellman equations $V_n = \max_a [r(a) + \beta V_{n - 1}(F(a))]$ are recursive in the time horizon; the policy-iteration algorithm is the inductive solution method. Across these very different domains, the recursion-induction duality is the operative cognitive tool.

### 1.3 Why It Works

There are three reasons.

First, the *single inductive step is the substantive content of the entire infinite-family argument*. To prove a statement for all $n \ge n_0$, one needs only to prove the implication $P(n) \Rightarrow P(n + 1)$ and the base case $P(n_0)$; the chain of implications $P(n_0) \Rightarrow P(n_0 + 1) \Rightarrow P(n_0 + 2) \Rightarrow \cdots$ then propagates automatically. The compression ratio is *infinite* (a single proof certifies an infinite family); the technique is the *most efficient* possible argumentation pattern for infinite-family statements.

Second, the *recurrence structure is often the natural way the problem actually arises*. The Tower of Hanoi solution recursively reduces the $n$-disk problem to the $(n - 1)$-disk problem (move top $n - 1$, move biggest, move top $n - 1$ back); the recurrence $T_n = 2 T_{n - 1} + 1$ *is* the solution strategy. The Fibonacci recursion $F_n = F_{n - 1} + F_{n - 2}$ arises naturally from the rabbit-pair population-growth model that Fibonacci posed in 1202. The Wallis reduction formula $I_n = \frac{n - 1}{n} I_{n - 2}$ arises naturally from the integration-by-parts operation that connects $\sin^n$ to $\sin^{n - 2}$. In each case, the recursion is not an imposed abstraction; it is *how the problem is solved*.

Third, the *closed-form theory for linear recurrences is complete and computationally efficient*. For any linear recurrence with constant coefficients $T_n = c_1 T_{n-1} + \cdots + c_k T_{n-k}$, the closed-form solution can be derived in finite time via characteristic-polynomial root-finding. The closed-form allows efficient computation of $T_n$ for arbitrary $n$ (in time $O(\log n)$ via fast matrix exponentiation, vs $O(n)$ via direct iteration) and allows asymptotic analysis (the dominant eigenvalue $r_{\max}$ gives the asymptotic growth rate). The Tower of Hanoi $T_n = 2^n - 1$, the Fibonacci $F_n \sim \varphi^n / \sqrt 5$, the gambler's-ruin $P_k = 1 - k/N$ are all immediate consequences.

These three reasons — single-step compression, problem-structural naturalness, closed-form completeness — combine to make recursion / induction the *most universal proof and computation technique* in discrete mathematics.

---

## 2. Deep Structure

### 2.1 Anatomy of an Induction / Recursion Problem

Every recursion / induction problem has the same five-step anatomy.

\begin{enumerate}
\item \textbf{Inductive-parameter identification.} Identify the parameter on which to induct. The naïve choice is $n$ (the problem's natural size); the trained solver considers also strong induction (range $[n_0, n]$), double induction (two parameters), and induction on derived quantities (tree height, recursion depth, digit count).

\item \textbf{Inductive statement formulation.} Write down precisely the statement $P(n)$ or recurrence $T(n)$ being inducted on. The wording matters: ``the product of $r$ consecutive integers is divisible by $r!$'' (PP2) is one statement; ``$\binom{n + r - 1}{r}$ is an integer'' is a closely-related but distinct statement; the choice affects the difficulty of the inductive step.

\item \textbf{Base-case verification.} Verify $P(n_0)$ for the smallest $n_0$. The base case is often trivial; the discipline is to not skip it (more inductive ``proofs'' fail at the base case than at the inductive step).

\item \textbf{Inductive step.} Prove $P(n) \Rightarrow P(n + 1)$ (weak induction) or $P(n_0), \ldots, P(n) \Rightarrow P(n + 1)$ (strong induction). This is the substantive content; the chapter's worked examples and practice problems exercise this step.

\item \textbf{Conclusion / closed form.} Apply the induction principle to conclude $P(n)$ for all $n \ge n_0$; if a recurrence is involved, optionally derive the closed form via characteristic-polynomial theory.
\end{enumerate}

The five steps are universal: every recursion / induction problem follows them, often implicitly. Making them explicit is the chapter's pedagogical purpose.

### 2.2 The Three Modes of Induction

Three modes of induction recur across problems.

**Weak induction.** Assume $P(n)$; prove $P(n + 1)$. The standard case, sufficient for the majority of problems. *Examples.* WE1 (Fibonacci matrix), PP5 (Pascal), PP3 (JEE 1999 telescoping).

**Strong induction.** Assume $P(n_0), P(n_0 + 1), \ldots, P(n)$; prove $P(n + 1)$. Necessary when the inductive step requires not just the immediately preceding case but several earlier cases. *Examples.* WE2 (JEE 1982 divisibility, which uses the shift-coefficient technique requiring strong-induction framing), and the classical fundamental theorem of arithmetic ($n$ has a prime factorisation; induction at $n$ uses any factorisation of any smaller $m$).

**Double induction (or nested induction).** Induct on two parameters simultaneously, often in a triangular fashion (induct on $r$ while inducting on $n$ for each fixed $r$). *Examples.* PP2 (product of $r$ consecutive integers, with $r$ and the starting integer as two parameters).

A fourth mode worth noting:

**Well-founded / structural induction.** Induct over a well-founded partial order (no infinite descending chains) — e.g., induct on the structure of a tree, the height of a recursion, or the rank of an inductive data type. Common in computer science and formal logic; less common in olympiad practice but powerful when applicable.

The trained solver, faced with an inductive problem, considers each mode in turn: would weak induction work? if not, would strong induction handle the gap? if neither, is double induction the right move? Spending sixty seconds on this choice often saves hours of wasted inductive effort.

### 2.3 Common Pitfalls and How to Recognise Them

Five classical pitfalls recur in recursion / induction problems.

**Pitfall 1: Skipping the base case.** The most common failure: an elegant inductive step that nevertheless fails to establish the claim because the base case is wrong or missing. Classic example: the (in)famous ``all horses are the same colour'' fallacy, where the inductive step $P(n) \Rightarrow P(n + 1)$ is wrong at $n = 1$ (a set of two horses cannot be split into two overlapping subsets of size 1 that share a horse, so the colour-sharing argument fails). The fix: always verify the base case *first* and *separately*; do not assume it is trivial.

**Pitfall 2: Weak induction when strong is needed.** Some recurrences relate $T(n + 1)$ to $T(n - 1)$ or $T(n - 2)$ as well as $T(n)$; the Fibonacci recurrence is the prototypical example. Weak induction ("assume $P(n)$, prove $P(n + 1)$") is insufficient; strong induction (assume $P(n_0), \ldots, P(n)$, prove $P(n + 1)$) is needed. The fix: when the inductive step references multiple earlier cases, explicitly invoke strong induction.

**Pitfall 3: Wrong inductive parameter.** A problem indexed by two parameters $(r, n)$ might admit no clean weak induction on $n$ alone (or on $r$ alone) but might admit a clean *double* induction. PP2 (divisibility of $r!$ into the product of $r$ consecutive integers) is the canonical example: inducting on $n$ alone (fix $r$, vary the starting integer) requires inducting on $r$ as well. The fix: when one-parameter induction stalls, ask if a second parameter would help.

**Pitfall 4: Inductive step that secretly uses the conclusion.** Circular reasoning: the inductive step proves $P(n + 1)$ from $P(n)$ by an argument that implicitly assumes $P(n + 1)$ or a strengthening of it. This is subtle and accounts for many invalid "proofs." The fix: when writing the inductive step, *only* use $P(n)$ (or $P(n_0), \ldots, P(n)$ for strong induction) — verify that no later fact is being invoked.

**Pitfall 5: Recurrence with wrong characteristic-polynomial roots.** When solving linear recurrences in closed form, the characteristic polynomial's roots dictate the structure. *Repeated* roots require polynomial-in-$n$ corrections ($T_n = (A + Bn) r^n$ for a double root $r$); *complex* roots give oscillatory solutions ($T_n = r^n (A \cos n\theta + B \sin n\theta)$ for $r e^{i\theta}$ as a complex root). PP6 (gambler's ruin) is the canonical repeated-root example: the characteristic polynomial $r^2 - 2r + 1 = (r - 1)^2$ has the double root $r = 1$, giving linear (not exponential) solutions $T_n = A + B n$.

These five pitfalls account for the overwhelming majority of induction / recursion errors. Internalising them is the inductive-discipline's working capital.

---

## 3. The Diagnostic Toolkit

How does one *recognise*, when first encountering a problem, that recursion / induction is the right archetype to deploy? The following four-question diagnostic checklist serves as the trained solver's first scan.

\begin{itemize}
\item \textbf{Q1 (Discrete-parameter dependence).} \emph{Is the problem indexed by a discrete parameter $n$ (positive integer, integer, natural number)?} Any problem of the form ``prove for all positive integers $n$ that \ldots'' or ``find the number of \ldots of size $n$'' or ``find the value of \ldots at the $n$-th step'' is a candidate.

\item \textbf{Q2 (Step-to-step relation).} \emph{Can you express the answer at step $n + 1$ in terms of the answer at step $n$ (or earlier steps)?} If yes, you have a recurrence; the closed-form derivation or the inductive proof flows from there.

\item \textbf{Q3 (Base-case tractability).} \emph{Is the base case ($n = 1$ or $n = 0$) easy to verify directly?} Most problems have a trivial base case; the discipline is to check this is the case before committing to induction.

\item \textbf{Q4 (Linear-recurrence shape).} \emph{If a recurrence is involved, is it linear with constant coefficients?} If yes, the characteristic-polynomial theory gives a closed form. If non-linear, the recurrence itself may be the answer.
\end{itemize}

Two or more affirmative answers (especially Q1 + Q2) signal that recursion / induction is the right archetype. The trained solver, faced with any discrete-parameter problem, performs this diagnostic *first* — typically in under sixty seconds — before selecting any technical machinery.

A second-order diagnostic is *named-recurrence recognition*. Across hundreds of problems, only a handful of named recurrences recur:

- ``$T_n = T_{n - 1} + d$'' (arithmetic progression; $T_n = T_0 + nd$).
- ``$T_n = c \cdot T_{n - 1}$'' (geometric progression; $T_n = c^n T_0$).
- ``$T_n = c T_{n - 1} + d$'' (affine; $T_n = c^n (T_0 + d/(c-1)) - d/(c-1)$ for $c \ne 1$).
- ``$T_n = T_{n - 1} + T_{n - 2}$'' (Fibonacci; closed form via Binet).
- ``$T_n = 2 T_{n - 1} + 1$'' (Tower of Hanoi; $T_n = 2^n - 1$).
- ``$P_n = (P_{n - 1} + P_{n + 1})/2$'' (discrete Laplace; linear solutions).
- ``$\binom{n + 1}{r} = \binom{n}{r - 1} + \binom{n}{r}$'' (Pascal; the master combinatorial recursion).
- ``$I_n = \frac{n - 1}{n} I_{n - 2}$'' (Wallis; the master integral-reduction formula).

The trained solver recognises these named recurrences immediately and proceeds to the next move (apply the closed form, or use the recurrence in the inductive step) without re-deriving the structure.

---

## 4. Worked Examples

The three worked examples are organised by increasing depth of inductive technique. WE1 (Fibonacci matrix power) is a *tier-3* problem demonstrating the simplest weak-induction template in a matrix setting. WE2 (JEE 1982 divisibility) is a *tier-3* problem deploying the shift-coefficient strong-induction technique, the canonical method for divisibility proofs. WE3 (Wallis reduction formula) is a *tier-2* problem illustrating the integration-by-parts reduction formula, the integral analogue of induction.

### 4.1 WE1 — Fibonacci Matrix Power (Tier 3)

**Problem.** *Let $A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$. Prove that $A^n = \begin{pmatrix} F_{n + 1} & F_n \\ F_n & F_{n - 1} \end{pmatrix}$ for every positive integer $n$, where $F_n$ is the $n$th Fibonacci number with $F_0 = 0, F_1 = 1, F_2 = 1, \ldots$*

**Source.** Joshi, *Educative JEE Mathematics*, Ch. 24, Exercise 24.10.

#### SEED — The Setup

The matrix $A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ is the *Fibonacci shift operator*: applied to the column vector $\begin{pmatrix} F_{n + 1} \\ F_n \end{pmatrix}$, it produces

\[
A \begin{pmatrix} F_{n + 1} \\ F_n \end{pmatrix} = \begin{pmatrix} F_{n + 1} + F_n \\ F_{n + 1} \end{pmatrix} = \begin{pmatrix} F_{n + 2} \\ F_{n + 1} \end{pmatrix}.
\]

So $A$ shifts the Fibonacci sequence one step forward. Iterating $n$ times from the initial vector $\begin{pmatrix} F_1 \\ F_0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ should yield $\begin{pmatrix} F_{n + 1} \\ F_n \end{pmatrix}$. This is consistent with the claim that $A^n = \begin{pmatrix} F_{n + 1} & F_n \\ F_n & F_{n - 1} \end{pmatrix}$ (whose first column is $\begin{pmatrix} F_{n + 1} \\ F_n \end{pmatrix}$, as required).

The Fibonacci recursion $F_{n + 1} = F_n + F_{n - 1}$ is *exactly* the eigenvalue equation for $A$ written as a difference equation: the characteristic polynomial $\chi(r) = r^2 - r - 1$ has roots $\varphi = (1 + \sqrt 5)/2$ and $\psi = (1 - \sqrt 5)/2$, and the closed-form Binet $F_n = (\varphi^n - \psi^n)/\sqrt 5$ is the diagonalisation of $A$ in the eigenbasis. The matrix-power claim is the algebraic identity behind this analytic closed form.

#### BRUTE PATH — Direct Calculation

The naïve approach is to compute $A^n$ for several values of $n$ and look for a pattern. We can compute:

$A^1 = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} F_2 & F_1 \\ F_1 & F_0 \end{pmatrix}$.

$A^2 = A \cdot A = \begin{pmatrix} 1 \cdot 1 + 1 \cdot 1 & 1 \cdot 1 + 1 \cdot 0 \\ 1 \cdot 1 + 0 \cdot 1 & 1 \cdot 1 + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} F_3 & F_2 \\ F_2 & F_1 \end{pmatrix}$.

$A^3 = A^2 \cdot A = \begin{pmatrix} 2 \cdot 1 + 1 \cdot 1 & 2 \cdot 1 + 1 \cdot 0 \\ 1 \cdot 1 + 1 \cdot 1 & 1 \cdot 1 + 1 \cdot 0 \end{pmatrix} = \begin{pmatrix} 3 & 2 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix} F_4 & F_3 \\ F_3 & F_2 \end{pmatrix}$.

The pattern is clear: $A^n = \begin{pmatrix} F_{n + 1} & F_n \\ F_n & F_{n - 1} \end{pmatrix}$.

But "the pattern is clear" is not a proof; it confirms the conjecture but does not establish it for all $n$. The induction below makes the argument rigorous.

#### ELEGANT PIVOT — Weak Induction on $n$

The pivot is to *induct on $n$*.

**Base case** ($n = 1$): $A^1 = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$, and the RHS is $\begin{pmatrix} F_2 & F_1 \\ F_1 & F_0 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$. They match. ✓

**Inductive step:** Assume $A^n = \begin{pmatrix} F_{n + 1} & F_n \\ F_n & F_{n - 1} \end{pmatrix}$. Compute $A^{n + 1} = A^n \cdot A$:

\[
A^{n + 1} = \begin{pmatrix} F_{n + 1} & F_n \\ F_n & F_{n - 1} \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} F_{n + 1} + F_n & F_{n + 1} \\ F_n + F_{n - 1} & F_n \end{pmatrix}.
\]

Apply the Fibonacci recurrence $F_{n + 1} + F_n = F_{n + 2}$ and $F_n + F_{n - 1} = F_{n + 1}$:

\[
A^{n + 1} = \begin{pmatrix} F_{n + 2} & F_{n + 1} \\ F_{n + 1} & F_n \end{pmatrix}.
\]

This is the claimed formula with $n$ replaced by $n + 1$. ✓

By the principle of mathematical induction, the formula holds for all positive integers $n$. $\blacksquare$

The boxed conclusion is

\[ \boxed{A^n = \begin{pmatrix} F_{n + 1} & F_n \\ F_n & F_{n - 1} \end{pmatrix} \text{ for every positive integer } n.} \]

#### PITFALLS

\begin{itemize}
\item \textbf{Pitfall 1.} Computing only the first few powers and concluding ``by pattern.'' Patterns are conjectures, not proofs; the induction is the proof.

\item \textbf{Pitfall 2.} Forgetting to verify the base case. Without the base, the inductive step is logically inert (it propagates from nothing).

\item \textbf{Pitfall 3.} Mis-applying the Fibonacci recurrence in the inductive step. The recurrence is $F_{n + 1} = F_n + F_{n - 1}$; care with indices is essential.

\item \textbf{Pitfall 4.} Using induction on the matrix entry positions rather than on $n$. The induction is on the integer exponent $n$, not on the matrix structure.
\end{itemize}

#### CONNECTIONS

\begin{itemize}
\item \textbf{Ch. 17 (Degrees of Freedom)} — the 2-dimensional vector $\begin{pmatrix} F_{n + 1} \\ F_n \end{pmatrix}$ has 2 DOFs, encoding two consecutive Fibonacci values; the matrix $A$ is the 1-step shift operator on this 2-DOF state space. The Fibonacci recursion is the natural inductive descent on the 2-DOF state space.

\item \textbf{Ch. 19 (Pivoting / Elimination)} — the eigenvalue computation for $A$ (giving the closed-form Binet) is a pivoting/elimination operation: solve $(A - r I) \vec v = 0$ by row-reduction.

\item \textbf{Linear algebra and dynamical systems} — the matrix-power approach generalises to any linear recurrence: if $T_n = c_1 T_{n - 1} + c_2 T_{n - 2} + \cdots + c_k T_{n - k}$, the corresponding companion matrix is a $k \times k$ matrix whose powers encode the recurrence; the closed form follows from the eigenvalue decomposition.

\item \textbf{Computer science} — the matrix-power formulation enables computing $F_n$ in time $O(\log n)$ (by repeated squaring of $A$), vs $O(n)$ by direct iteration. Asymptotically optimal Fibonacci computation goes through this matrix-power identity.
\end{itemize}

#### TAKEAWAY

The Fibonacci matrix-power identity is the chapter's cleanest demonstration of the recursion-induction duality: the matrix recurrence $A^{n + 1} = A^n \cdot A$ *is* the Fibonacci recurrence in disguise, and the inductive proof of $A^n = \begin{pmatrix} F_{n + 1} & F_n \\ F_n & F_{n - 1} \end{pmatrix}$ is just the iteration of the matrix recurrence with the algebra of Fibonacci numbers tracking the entries. The identity is the foundation of the $O(\log n)$ Fibonacci algorithm and of the Binet closed-form derivation.

### 4.2 WE2 — $25 \mid 7^{2n} + 2^{3n - 3} \cdot 3^{n - 1}$ (Tier 3: JEE 1982)

**Problem.** *Prove that $25 \mid 7^{2n} + 2^{3n - 3} \cdot 3^{n - 1}$ for every positive integer $n$.*

**Source.** JEE 1982 (Joshi, *EJM* Ch. 4, Comment 8).

#### SEED — The Setup

Let $S(n) = 7^{2n} + 2^{3n - 3} \cdot 3^{n - 1}$. The claim is that $25 \mid S(n)$ for every positive integer $n$.

Verify the base case: $S(1) = 7^2 + 2^0 \cdot 3^0 = 49 + 1 = 50 = 2 \cdot 25$. ✓

The structural insight: the two summands grow at different rates ($7^{2n} = 49^n$ grows like $49^n$, while $2^{3n - 3} \cdot 3^{n - 1} = \frac{1}{24} \cdot 24^n$ grows like $24^n / 24$), but their sum is *always* divisible by 25. This suggests the modular arithmetic mod 25 has a *cancellation* mechanism that makes the sum vanish modulo 25 regardless of $n$.

Direct modular reduction: $49 \equiv -1 \pmod{25}$, so $7^{2n} = 49^n \equiv (-1)^n \pmod{25}$. And $24 \equiv -1 \pmod{25}$, so $2^{3n - 3} \cdot 3^{n - 1} = 24^n / 24 \equiv (-1)^n / (-1) = -(-1)^n \pmod{25}$. Sum: $(-1)^n + [-(-1)^n] = 0 \pmod{25}$. ✓

This *direct modular* proof is elegant and short, but the chapter's induction-archetype goal is to demonstrate the *induction-via-shift-coefficient* technique, which is the canonical inductive method for divisibility proofs. We give that proof.

#### BRUTE PATH — Direct Modular Arithmetic

The direct modular proof above (49 ≡ -1, 24 ≡ -1 mod 25) is clean but does not exercise the inductive machinery. It relies on the lucky observation that $7^2 = 49 \equiv -1 \pmod{25}$ and $24 = 2^3 \cdot 3 \equiv -1 \pmod{25}$; these reductions happen to make the sum cancel cleanly.

The pedagogical limitation of the brute approach is that it does *not* generalise: many divisibility problems do *not* admit such clean direct-modular reductions; the inductive approach below is the *robust* technique that works for the general class of divisibility-by-induction problems.

#### ELEGANT PIVOT — Strong Induction via Shift-Coefficient

The pivot is to *induct on $n$ using the shift-coefficient technique*.

**Inductive step.** Assume $25 \mid S(n) = 7^{2n} + 2^{3n - 3} \cdot 3^{n - 1}$ (IH).

Compute $S(n + 1) = 7^{2(n + 1)} + 2^{3(n + 1) - 3} \cdot 3^{(n + 1) - 1} = 7^{2n + 2} + 2^{3n} \cdot 3^n$.

Re-express the two summands in terms of $S(n)$'s summands:
\begin{itemize}
\item $7^{2n + 2} = 49 \cdot 7^{2n}$.
\item $2^{3n} \cdot 3^n = 2^3 \cdot 2^{3n - 3} \cdot 3 \cdot 3^{n - 1} = 8 \cdot 3 \cdot (2^{3n - 3} \cdot 3^{n - 1}) = 24 \cdot 2^{3n - 3} \cdot 3^{n - 1}$.
\end{itemize}

So $S(n + 1) = 49 \cdot 7^{2n} + 24 \cdot 2^{3n - 3} \cdot 3^{n - 1}$.

Now apply the *shift-coefficient technique*: write $S(n + 1)$ as a linear combination of $S(n)$ and a multiple of 25.

\[
S(n + 1) = 49 \cdot 7^{2n} + 24 \cdot 2^{3n - 3} \cdot 3^{n - 1} = 24 \cdot (7^{2n} + 2^{3n - 3} \cdot 3^{n - 1}) + (49 - 24) \cdot 7^{2n} = 24 \cdot S(n) + 25 \cdot 7^{2n}.
\]

Both terms on the RHS are divisible by 25: the first because $25 \mid S(n)$ by IH (and $24 \cdot S(n)$ inherits the divisibility), the second because $25 \mid 25 \cdot 7^{2n}$ trivially.

Hence $25 \mid S(n + 1)$, completing the inductive step.

**Base case.** $S(1) = 49 + 1 = 50 = 2 \cdot 25$, so $25 \mid S(1)$. ✓

By the principle of mathematical induction, $25 \mid S(n)$ for every positive integer $n$. $\blacksquare$

The boxed conclusion is

\[ \boxed{25 \mid 7^{2n} + 2^{3n - 3} \cdot 3^{n - 1} \text{ for every positive integer } n.} \]

#### PITFALLS

\begin{itemize}
\item \textbf{Pitfall 1.} Failing to recognise the shift-coefficient pattern $S(n + 1) = a \cdot S(n) + b \cdot M$. The technique is universal for divisibility proofs; learn to spot the right coefficients $a, b$ from the exponent shifts.

\item \textbf{Pitfall 2.} Forgetting to verify the base case. The inductive step is correct but the conclusion fails without the base.

\item \textbf{Pitfall 3.} Trying to factor $S(n)$ directly. Factorisation is not the path; the inductive recurrence on $S(n)$ is.

\item \textbf{Pitfall 4.} Using the direct modular proof ($49 \equiv -1, 24 \equiv -1 \pmod{25}$) instead of induction. The direct proof is elegant but the inductive technique is the generalisable tool; the JEE 1982 problem is the chapter's training ground for the inductive divisibility technique.
\end{itemize}

#### CONNECTIONS

\begin{itemize}
\item \textbf{Ch. 14 (Parity / Modularity)} — the divisibility-by-25 claim is a modular statement; Ch. 14 develops the modular-arithmetic toolkit (mod $p$, mod $p^2$, Fermat's little theorem, CRT) that the direct modular proof of this problem uses. Ch. 18 ($\Leftarrow$) gives the inductive proof; the two chapters illuminate the same problem from complementary angles.

\item \textbf{Ch. 17 (DOF)} — the inductive proof has 1 DOF (the parameter $n$); the inductive scheme \emph{is} the DOF descent.

\item \textbf{Ch. 19 (Pivoting / Elimination)} — the shift-coefficient technique is a form of algebraic pivoting: re-express $S(n + 1)$ in the basis $\{S(n), 25 \cdot \text{anything}\}$.

\item \textbf{JEE history} — this problem is among the most famous of the JEE 1982 mathematics paper and is the canonical training problem for the shift-coefficient inductive divisibility technique; generations of Indian JEE aspirants have learnt the technique on this problem.
\end{itemize}

#### TAKEAWAY

The JEE 1982 problem is the cleanest illustration of the *shift-coefficient inductive divisibility* technique: re-express $S(n + 1)$ as $a S(n) + b \cdot M$ where $M$ is the modulus, then both terms are divisible by $M$ (the first by IH, the second by inspection), so $S(n + 1)$ is. The technique is universal for divisibility proofs; the discipline is to identify the right coefficient $a$ that makes the IH-bound term emerge cleanly.

### 4.3 WE3 — Reduction Formula for $I_n = \int_0^{\pi/2} \sin^n x \, dx$ (Tier 2)

**Problem.** *Establish the reduction formula $I_n = \frac{n - 1}{n} I_{n - 2}$ for $I_n = \int_0^{\pi/2} \sin^n x \, dx$, and use it to evaluate $I_5$ and $I_6$.*

**Source.** Joshi, *EJM* Ch. 18, Comment 4 (reduction formulas).

#### SEED — The Setup

Wallis's integral $I_n = \int_0^{\pi/2} \sin^n x \, dx$ is a 1-parameter family of definite integrals indexed by the non-negative integer $n$. For specific small $n$:

- $I_0 = \int_0^{\pi/2} 1 \, dx = \pi/2$.
- $I_1 = \int_0^{\pi/2} \sin x \, dx = [-\cos x]_0^{\pi/2} = 0 - (-1) = 1$.
- $I_2 = \int_0^{\pi/2} \sin^2 x \, dx = \int_0^{\pi/2} \frac{1 - \cos 2x}{2} \, dx = \pi/4$.

The pattern of $I_2 = \pi/4 = (1/2) \cdot I_0$ already suggests $I_2 = ((2 - 1)/2) I_0 = (1/2) I_0$, hence the reduction formula $I_n = \frac{n - 1}{n} I_{n - 2}$ as the inductive recurrence to establish.

#### BRUTE PATH — Direct Evaluation

Compute $I_5$ directly: $\int_0^{\pi/2} \sin^5 x \, dx = \int_0^{\pi/2} \sin x (1 - \cos^2 x)^2 \, dx$. Substitute $u = \cos x$, $du = -\sin x \, dx$:
\[
I_5 = -\int_1^0 (1 - u^2)^2 \, du = \int_0^1 (1 - 2u^2 + u^4) \, du = 1 - 2/3 + 1/5 = 15/15 - 10/15 + 3/15 = 8/15.
\]
This works for *odd* $n$ via the $u = \cos x$ substitution, but for *even* $n$ (like $n = 6$) the integrand has no such elementary substitution; the brute approach branches awkwardly between the odd and even cases.

The reduction formula handles both cases uniformly, and that uniformity is the technique's payoff.

#### ELEGANT PIVOT — Integration by Parts

The pivot is to *integrate by parts*.

Write $\sin^n x = \sin^{n - 1} x \cdot \sin x$, and apply integration by parts with $u = \sin^{n - 1} x$ and $dv = \sin x \, dx$, so $du = (n - 1) \sin^{n - 2} x \cos x \, dx$ and $v = -\cos x$:

\[
I_n = [-\sin^{n - 1} x \cos x]_0^{\pi/2} + (n - 1) \int_0^{\pi/2} \sin^{n - 2} x \cos^2 x \, dx.
\]

The boundary term vanishes: at $x = \pi/2$, $\cos x = 0$; at $x = 0$, $\sin x = 0$. Hence

\[
I_n = (n - 1) \int_0^{\pi/2} \sin^{n - 2} x \cos^2 x \, dx = (n - 1) \int_0^{\pi/2} \sin^{n - 2} x (1 - \sin^2 x) \, dx = (n - 1) I_{n - 2} - (n - 1) I_n.
\]

Solving for $I_n$:
\[
I_n + (n - 1) I_n = (n - 1) I_{n - 2} \quad \Longleftrightarrow \quad n \cdot I_n = (n - 1) I_{n - 2} \quad \Longleftrightarrow \quad I_n = \frac{n - 1}{n} I_{n - 2}.
\]

This is the reduction formula. ✓

**Apply to $I_5$.** Iterate the recurrence on the odd-index thread, descending from $I_5$ to $I_3$ to $I_1$:
\[
I_5 = \frac{4}{5} I_3 = \frac{4}{5} \cdot \frac{2}{3} I_1 = \frac{4}{5} \cdot \frac{2}{3} \cdot 1 = \frac{8}{15}.
\]

**Apply to $I_6$.** Iterate the recurrence on the even-index thread, descending from $I_6$ to $I_4$ to $I_2$ to $I_0$:
\[
I_6 = \frac{5}{6} I_4 = \frac{5}{6} \cdot \frac{3}{4} I_2 = \frac{5}{6} \cdot \frac{3}{4} \cdot \frac{1}{2} I_0 = \frac{5}{6} \cdot \frac{3}{4} \cdot \frac{1}{2} \cdot \frac{\pi}{2} = \frac{15 \pi}{96} = \frac{5\pi}{32}.
\]

The boxed conclusions are

\[ \boxed{I_n = \frac{n - 1}{n} I_{n - 2}; \quad I_5 = \frac{8}{15}; \quad I_6 = \frac{5\pi}{32}.} \]

#### PITFALLS

\begin{itemize}
\item \textbf{Pitfall 1.} Forgetting to apply $\cos^2 = 1 - \sin^2$ in the inductive step; this re-expression is what makes the recurrence on $I_n$ close.

\item \textbf{Pitfall 2.} Confusing the odd-index and even-index threads. The recurrence $I_n = \frac{n - 1}{n} I_{n - 2}$ descends from $n$ to $n - 2$; the two threads (odd $n$ descending to $I_1$; even $n$ descending to $I_0$) are independent.

\item \textbf{Pitfall 3.} Computing $I_5$ or $I_6$ directly by substitution. The reduction formula is dramatically faster and is the technique's payoff.

\item \textbf{Pitfall 4.} Missing the boundary-term-vanishes observation. The boundary term $[-\sin^{n - 1} x \cos x]_0^{\pi/2}$ vanishes only because $\sin 0 = 0$ and $\cos(\pi/2) = 0$; for an integration over a different interval (e.g., $\int_0^\pi$), the boundary term may not vanish.
\end{itemize}

#### CONNECTIONS

\begin{itemize}
\item \textbf{Ch. 5 (Substitution)} — the substitution $u = \cos x$ for odd $n$ (the brute path) is a Ch. 5 archetype; the reduction formula generalises across both odd and even $n$ via the inductive technique.

\item \textbf{Wallis's formula and $\pi$} — iterating the reduction formula gives Wallis's product $\frac{\pi}{2} = \prod_{n = 1}^{\infty} \frac{(2n)^2}{(2n - 1)(2n + 1)}$, a celebrated representation of $\pi$ via an infinite product.

\item \textbf{Beta function and Gamma function} — $I_n = \frac{1}{2} B((n + 1)/2, 1/2)$ where $B$ is the Beta function; the reduction formula is the discrete-shift identity $B(x + 1, y) = \frac{x}{x + y} B(x, y)$.

\item \textbf{Probability theory} — $I_n / I_0$ for even $n$ gives the moments of the absolute value of a uniform random variable on $[-\pi/2, \pi/2]$.
\end{itemize}

#### TAKEAWAY

The Wallis reduction formula is the chapter's archetypal *integral reduction*: integration by parts yields a recurrence on the integer parameter $n$, descending by 2 at each step, with a finite chain of recurrences terminating at the base cases $I_0 = \pi/2$ and $I_1 = 1$. The technique generalises across the entire family of *reduction formulas* (Joshi's Ch. 18 catalogue), each of which converts an apparently hard integral into a closed-form expression via an inductive recurrence on a discrete parameter. This is the integral analogue of mathematical induction.

---

## 5. Practice Problems

The seven practice problems, with answers boxed and full solutions in the Appendix, traverse the five characteristic forms of induction / recursion surveyed in §1.1.

### PP1 — Telescoping Inverse-Cotangent Sum (Tier 2)

Sum the infinite series $\displaystyle \sum_{k = 1}^{\infty} \cot^{-1}(2 k^2)$.

\[ \boxed{\sum_{k = 1}^{\infty} \cot^{-1}(2 k^2) = \pi / 4.} \]

### PP2 — Product of $r$ Consecutive Integers (Tier 3)

Prove that the product of any $r$ consecutive positive integers is divisible by $r!$.

\[ \boxed{r! \mid n (n + 1) \cdots (n + r - 1) \text{ for all positive integers } n, r.} \]

### PP3 — JEE 1999 Inverse-Tangent Series (Tier 2)

Prove by induction: $\tan^{-1}\frac{1}{3} + \tan^{-1}\frac{1}{7} + \cdots + \tan^{-1}\frac{1}{n^2 + n + 1} = \tan^{-1}\frac{n}{n + 2}$.

\[ \boxed{\sum_{k = 1}^{n} \tan^{-1} \frac{1}{k^2 + k + 1} = \tan^{-1} \frac{n}{n + 2}.} \]

### PP4 — Tower of Hanoi (Tier 2)

Prove that the minimum number of moves to transfer $n$ disks in the Tower of Hanoi from one peg to another is $2^n - 1$.

\[ \boxed{T_n = 2^n - 1 \text{ moves (minimum), with } T_n = 2 T_{n - 1} + 1, T_1 = 1.} \]

### PP5 — Pascal's Identity by Induction (Tier 1: JEE Mains)

Prove $\binom{n + 1}{r} = \binom{n}{r - 1} + \binom{n}{r}$ by induction on $n$.

\[ \boxed{\binom{n + 1}{r} = \binom{n}{r - 1} + \binom{n}{r}.} \]

### PP6 — Random Walk Recursion (Gambler's Ruin) (Tier 3)

A gambler starts with $k$ rupees, wins or loses 1 rupee per round with probability $1/2$, and stops at $0$ (ruin) or $N$ (win). Set up the recurrence for $P_k$ = probability of ruin starting from $k$; solve.

\[ \boxed{P_k = (P_{k - 1} + P_{k + 1}) / 2 \text{ with } P_0 = 1, P_N = 0; \text{ solution } P_k = 1 - k / N.} \]

### PP7 — Binary Strings without Consecutive 1's (Tier 3)

Let $a_n$ = number of binary strings of length $n$ with no two consecutive $1$'s. Set up the recurrence and identify $a_n$.

\[ \boxed{a_n = a_{n - 1} + a_{n - 2} \text{ with } a_1 = 2, a_2 = 3; \quad a_n = F_{n + 2}.} \]

---

## 6. Connections Web

The Recursion / Induction archetype connects intimately with the rest of Pillar 2. The most important connections:

- **Ch. 11 (Existence / Uniqueness)** — inductive constructions are the most common existence proofs: ``construct an $n$-element solution by extending an $(n-1)$-element solution.'' The chapter's PP4 (Tower of Hanoi) and PP7 (binary strings) are both existence proofs via inductive construction.

- **Ch. 13 (Combinatorial Principles)** — combinatorial identities like Pascal's (PP5) and Vandermonde's are the canonical training ground for inductive techniques; the inductive proof of Pascal's identity is the entry point to the entire Pascal-triangle combinatorics.

- **Ch. 14 (Parity / Modularity)** — divisibility proofs (WE2: $25 \mid 7^{2n} + 2^{3n - 3} \cdot 3^{n - 1}$) connect to Ch. 14's modular-arithmetic toolkit; the inductive technique is one of two complementary approaches (the other being direct modular reduction, e.g. $49 \equiv -1 \pmod{25}$).

- **Ch. 15 (Bijection / Correspondence)** — combinatorial recurrences (PP7: binary strings without consecutive 1's, satisfying $a_n = a_{n - 1} + a_{n - 2}$ and equalling $F_{n + 2}$) are bijective in spirit: each side of the recurrence counts a partition of the configuration set by some natural feature (the last character of the string).

- **Ch. 17 (Degrees of Freedom)** — the inductive parameter is the *DOF descent variable*: induct on $n$ descends from the $n$-DOF problem to the $(n - 1)$-DOF problem. The Meta-Reasoning sub-pillar's first two chapters (17 and 18) form a tight pair: Ch. 17 names the inductive parameter; Ch. 18 uses it as the inductive index.

- **Ch. 19 (Pivoting / Elimination)** — Gaussian elimination is a multi-step inductive procedure: at each step, pivot on one variable and reduce to a smaller system; the inductive correctness of the elimination procedure is the *invariant* maintained at each step (the row echelon form is preserved across pivots).

- **Ch. 20 (Analogy / Transfer)** — inductive proofs often *transfer* across problems: the technique that works for one combinatorial identity (e.g., Pascal's) often works for many others (Vandermonde's, hockey-stick, etc.); the analogy is the meta-recognition that the inductive scaffold is the same.

The chapter therefore sits at the structural crossroads between the *Meta-Reasoning* sub-pillar's opening (Ch. 17, Degrees of Freedom Analysis, which scoped the parameter-and-constraint count) and the sub-pillar's continuation (Ch. 19, Pivoting / Elimination, which builds inductive techniques into the linear-algebra elimination procedure). Chapter 18 is the *engine* of meta-reasoning; the single inductive step is the most efficient form of mathematical argumentation.

---

## 7. Master Takeaways

Six master takeaways summarise the chapter's central lessons.

\begin{enumerate}
\item \textbf{Solve for one step; the recursion does the rest.} The inductive step (or recurrence) is the entire substantive content; the propagation across all $n \ge n_0$ is automatic. This is the most efficient possible proof / computation structure for infinite-family statements.

\item \textbf{Identify the right inductive parameter first.} The naïve choice ``induct on $n$'' works for the majority of problems; the deeper problems require strong induction, double induction, or induction on a derived quantity. Spending 60 seconds on this choice saves hours of wasted inductive effort.

\item \textbf{Shift-coefficient technique for divisibility.} For divisibility proofs of the form ``prove $M \mid S(n)$,'' re-express $S(n + 1) = a S(n) + b \cdot M$. The first term is divisible by $M$ via IH; the second is divisible by $M$ trivially. This is the canonical inductive divisibility technique (WE2 is the JEE 1982 paradigm).

\item \textbf{Reduction formulas are the integral analogue of induction.} Integration by parts often yields a recurrence on the integer parameter (e.g., Wallis $I_n = \frac{n - 1}{n} I_{n - 2}$); the recurrence + base case give the closed form. This integral-recurrence technique is universal across the chapter of reduction formulas in calculus.

\item \textbf{Linear-recurrence closed forms via characteristic polynomial.} Every linear recurrence $T_n = c_1 T_{n - 1} + \cdots + c_k T_{n - k}$ has a characteristic polynomial $\chi(r) = r^k - c_1 r^{k - 1} - \cdots - c_k$; the closed form is $T_n = \sum_i A_i r_i^n$ for distinct roots, with polynomial-in-$n$ corrections for repeated roots. The Fibonacci Binet formula, the Tower-of-Hanoi $T_n = 2^n - 1$, and the gambler's-ruin $P_k = 1 - k/N$ are all immediate applications.

\item \textbf{Telescoping is hidden induction.} A sum $\sum_k f(k)$ with $f(k) = g(k) - g(k - 1)$ telescopes to $g(n) - g(0)$; the cancellation is the inductive propagation in disguise. PP1 ($\cot^{-1}(2 k^2)$) and PP3 (JEE 1999 $\tan^{-1}$) are the chapter's two telescoping exemplars.
\end{enumerate}

---

## 8. Self-Assessment Checklist

The reader is encouraged to test internalisation with the following five-question checklist. A confident affirmative answer to all five indicates mastery.

\begin{enumerate}
\item Given a divisibility claim like ``prove $M \mid S(n)$,'' can you immediately set up the shift-coefficient inductive recurrence $S(n + 1) = a S(n) + b \cdot M$ and identify the right $a, b$ from the exponent shifts?

\item Given a linear recurrence $T_n = c_1 T_{n - 1} + \cdots + c_k T_{n - k}$, can you write down the characteristic polynomial, find its roots, and derive the closed-form expression $T_n = \sum_i A_i r_i^n$ with initial-condition fitting?

\item Can you recognise when weak induction is insufficient and strong induction is needed? Can you recognise when double induction (on two parameters) is the right move?

\item Can you set up the integration-by-parts reduction formula $I_n = \frac{n - 1}{n} I_{n - 2}$ for Wallis's integral, and use it to evaluate $I_n$ for arbitrary $n$ in closed form?

\item Can you recognise a telescoping sum: that is, can you spot when a summand $f(k)$ can be re-expressed as $g(k) - g(k - 1)$ for some $g$, so the partial sum collapses?
\end{enumerate}

A second-order self-assessment: take any divisibility problem from a JEE or RMO past-paper and attempt the inductive proof from scratch. The chapter's central skill is the *shift-coefficient technique*; once internalised, the technique handles the majority of olympiad divisibility problems with a uniform inductive scaffold.

---

## Bridge to Chapter 19

Chapter 18 continues the *Meta-Reasoning* sub-pillar with the discipline of *solving for one step and propagating by recursion*. The inductive step is the substantive content; the recursion automates the rest. This is the most efficient proof / computation structure for infinite-family statements.

Chapter 19 continues the Meta-Reasoning arc with **Pivoting / Elimination**: *simplify by subtraction, not addition*. If Chapter 18 taught the solver to *descend* on the inductive parameter, Chapter 19 teaches the solver to *eliminate* one variable at a time — to *choose a pivot* (the variable being eliminated at the current step) and reduce a $k$-variable system to a $(k - 1)$-variable system. Gaussian elimination, Gauss–Jordan reduction, polynomial-long-division, partial-fraction decomposition, and the Euclidean algorithm are all instances of pivoting / elimination.

The bridge from 18 to 19 is the realisation that *Gaussian elimination is an inductive procedure*. At each step of elimination, pivot on one variable, then recursively eliminate from the remaining $(k - 1)$-variable system. The inductive correctness of the elimination procedure is the *invariant* maintained at each step (the row-echelon form is preserved across pivots), and the algorithm terminates when no further pivot is possible (the system is in reduced form). The two chapters (18 induction, 19 elimination) are tightly paired: 18 descends on a single parameter $n$; 19 descends on the count of remaining variables.

Joshi's *Educative JEE Mathematics* supplies the Chapter 19 problem set: Gaussian elimination on a $4 \times 4$ system (WE1), polynomial long division with remainder structure (WE2), partial-fraction decomposition by elimination of basis coefficients (WE3), and seven practice problems exercising the full range of pivoting techniques (Euclidean algorithm, Cramer's rule, Newton-Raphson iteration as numerical pivoting, etc.). The reader who has internalised the inductive perspective is now ready to descend on the variable count one pivot at a time, recursively.

---

## Appendix — Practice Problem Solutions

### Solution to PP1 — Telescoping Inverse-Cotangent Sum

Want: $\displaystyle \sum_{k = 1}^{\infty} \cot^{-1}(2 k^2) = \pi / 4$.

Re-express $\cot^{-1}(2 k^2)$ using the inverse-tangent subtraction identity. Compute $\tan(\tan^{-1}(2k + 1) - \tan^{-1}(2k - 1))$:
\[
\tan(\tan^{-1}(2k + 1) - \tan^{-1}(2k - 1)) = \frac{(2k + 1) - (2k - 1)}{1 + (2k + 1)(2k - 1)} = \frac{2}{1 + (4 k^2 - 1)} = \frac{2}{4 k^2} = \frac{1}{2 k^2}.
\]

Since both $\tan^{-1}(2 k + 1)$ and $\tan^{-1}(2 k - 1)$ lie in $(0, \pi/2)$ for $k \ge 1$, their difference is positive and lies in $(0, \pi/2)$, so the inverse-tangent of the result agrees with the difference (no branch correction needed):

\[
\tan^{-1}(2 k + 1) - \tan^{-1}(2 k - 1) = \tan^{-1}\frac{1}{2 k^2} = \cot^{-1}(2 k^2).
\]

The partial sum telescopes:
\[
\sum_{k = 1}^{N} \cot^{-1}(2 k^2) = \sum_{k = 1}^{N} [\tan^{-1}(2 k + 1) - \tan^{-1}(2 k - 1)] = \tan^{-1}(2 N + 1) - \tan^{-1}(1).
\]

Take $N \to \infty$: $\tan^{-1}(2 N + 1) \to \pi/2$ and $\tan^{-1}(1) = \pi/4$, so the sum equals $\pi/2 - \pi/4 = \pi/4$.

The boxed answer:

\[ \boxed{\sum_{k = 1}^{\infty} \cot^{-1}(2 k^2) = \pi / 4.} \]

*Verification.* The telescoping cancellation pattern: $\tan^{-1}(3) - \tan^{-1}(1) + \tan^{-1}(5) - \tan^{-1}(3) + \tan^{-1}(7) - \tan^{-1}(5) + \cdots$ collapses to $\lim_{N \to \infty} \tan^{-1}(2 N + 1) - \tan^{-1}(1) = \pi/2 - \pi/4 = \pi/4$ ✓.

### Solution to PP2 — Product of $r$ Consecutive Integers

Claim: for all positive integers $n, r$, the product $P(n, r) := n (n + 1) (n + 2) \cdots (n + r - 1)$ is divisible by $r!$.

The cleanest proof uses *double induction* on $r$ and $n$, or equivalently the combinatorial identity $P(n, r) / r! = \binom{n + r - 1}{r}$, which is the cardinality of an $r$-multiset on $\{1, \ldots, n\}$ — necessarily a non-negative integer.

We give the inductive proof.

**Outer induction: on $r$.**

*Base case* ($r = 1$): $P(n, 1) = n$, which is divisible by $1! = 1$ trivially. ✓

*Outer inductive step:* Assume $r! \mid P(n, r)$ for all $n \ge 1$ (IH on $r$). Prove $(r + 1)! \mid P(n, r + 1)$ for all $n \ge 1$.

**Inner induction: on $n$.**

*Base case* ($n = 1$): $P(1, r + 1) = 1 \cdot 2 \cdots (r + 1) = (r + 1)!$, divisible by $(r + 1)!$ trivially. ✓

*Inner inductive step:* Assume $(r + 1)! \mid P(n, r + 1)$ (inner IH). Prove $(r + 1)! \mid P(n + 1, r + 1)$.

Compute the *forward difference*:
\[
P(n + 1, r + 1) - P(n, r + 1) = (n + 1)(n + 2) \cdots (n + r + 1) - n (n + 1) \cdots (n + r).
\]

Both products share the common factor $(n + 1)(n + 2) \cdots (n + r)$, so factor it out:
\[
P(n + 1, r + 1) - P(n, r + 1) = (n + 1)(n + 2) \cdots (n + r) \cdot [(n + r + 1) - n] = (r + 1) \cdot P(n + 1, r).
\]

By the outer IH on $r$: $r! \mid P(n + 1, r)$. Hence $(r + 1) \cdot r! = (r + 1)! \mid (r + 1) \cdot P(n + 1, r) = P(n + 1, r + 1) - P(n, r + 1)$.

By the inner IH: $(r + 1)! \mid P(n, r + 1)$. Adding: $(r + 1)! \mid P(n, r + 1) + (P(n + 1, r + 1) - P(n, r + 1)) = P(n + 1, r + 1)$.

This completes the inner inductive step. By the principle of mathematical induction (inner), $(r + 1)! \mid P(n, r + 1)$ for all $n \ge 1$, completing the outer inductive step. By the principle of mathematical induction (outer), $r! \mid P(n, r)$ for all $n \ge 1, r \ge 1$. $\blacksquare$

The boxed answer:

\[ \boxed{r! \mid n (n + 1) \cdots (n + r - 1) \text{ for all positive integers } n, r.} \]

*Verification.* The combinatorial proof: $P(n, r) / r! = \binom{n + r - 1}{r}$ is the cardinality of the set of $r$-multisets from $\{1, \ldots, n\}$, which is a non-negative integer. The inductive proof above arrives at the same conclusion via the recurrence $P(n + 1, r + 1) - P(n, r + 1) = (r + 1) P(n + 1, r)$, which is the multinomial Pascal-like identity in disguise.

### Solution to PP3 — JEE 1999 Inverse-Tangent Series

Want: $\sum_{k = 1}^{n} \tan^{-1} \frac{1}{k^2 + k + 1} = \tan^{-1} \frac{n}{n + 2}$.

The telescoping identity: $\tan(\tan^{-1}(k + 1) - \tan^{-1}(k)) = \frac{(k + 1) - k}{1 + k (k + 1)} = \frac{1}{k^2 + k + 1}$, hence

\[
\tan^{-1} \frac{1}{k^2 + k + 1} = \tan^{-1}(k + 1) - \tan^{-1}(k).
\]

The partial sum telescopes:
\[
\sum_{k = 1}^{n} \tan^{-1}\frac{1}{k^2 + k + 1} = \sum_{k = 1}^{n} [\tan^{-1}(k + 1) - \tan^{-1}(k)] = \tan^{-1}(n + 1) - \tan^{-1}(1) = \tan^{-1}(n + 1) - \pi/4.
\]

Re-express $\tan^{-1}(n + 1) - \pi/4$ in the closed form claimed:
\[
\tan(\tan^{-1}(n + 1) - \pi/4) = \frac{(n + 1) - 1}{1 + (n + 1)} = \frac{n}{n + 2},
\]

so $\tan^{-1}(n + 1) - \pi/4 = \tan^{-1}\frac{n}{n + 2}$ (the principal-branch identity holds since both sides lie in $(0, \pi/2)$ for $n \ge 1$).

The boxed answer:
\[ \boxed{\sum_{k = 1}^{n} \tan^{-1} \frac{1}{k^2 + k + 1} = \tan^{-1}\frac{n}{n + 2}.} \]

*Verification.* At $n = 1$: LHS $= \tan^{-1}(1/3)$, RHS $= \tan^{-1}(1/3)$ ✓. At $n = 2$: LHS $= \tan^{-1}(1/3) + \tan^{-1}(1/7)$; sum formula gives $\tan^{-1}\frac{(1/3) + (1/7)}{1 - (1/3)(1/7)} = \tan^{-1}\frac{10/21}{20/21} = \tan^{-1}(1/2)$; RHS $= \tan^{-1}(2/4) = \tan^{-1}(1/2)$ ✓.

### Solution to PP4 — Tower of Hanoi

The Tower of Hanoi: $n$ disks of decreasing size on peg A, the goal is to transfer them all to peg C (with peg B as auxiliary), moving one disk at a time and never placing a larger disk on a smaller one.

**Recursive solution structure.** To move $n$ disks from A to C:
\begin{enumerate}
\item Move the top $n - 1$ disks from A to B (using C as auxiliary).
\item Move the largest disk from A to C.
\item Move the $n - 1$ disks from B to C (using A as auxiliary).
\end{enumerate}

Let $T_n$ = minimum number of moves for $n$ disks. The recursion gives $T_n = T_{n - 1} + 1 + T_{n - 1} = 2 T_{n - 1} + 1$, with $T_1 = 1$ (a single disk takes one move).

**Closed-form derivation.** Add 1 to both sides of $T_n = 2 T_{n - 1} + 1$: $T_n + 1 = 2 T_{n - 1} + 2 = 2 (T_{n - 1} + 1)$. So the sequence $\{T_n + 1\}$ satisfies the geometric recurrence $a_n = 2 a_{n - 1}$ with $a_1 = T_1 + 1 = 2$. Hence $a_n = 2^n$, i.e., $T_n + 1 = 2^n$, so $T_n = 2^n - 1$.

**Optimality.** The recursive scheme above is *sufficient* (achieves $2^n - 1$ moves). It is also *necessary* (no strategy achieves fewer moves), because to move the largest disk, all $n - 1$ smaller disks must first be moved to the auxiliary peg (requiring $\ge T_{n - 1}$ moves by IH), then the largest is moved (1 move), then the smaller disks are moved to the goal peg ($\ge T_{n - 1}$ moves by IH). Total $\ge 2 T_{n - 1} + 1 = T_n$.

The boxed answer:
\[ \boxed{T_n = 2^n - 1 \text{ moves (minimum), via the recurrence } T_n = 2 T_{n - 1} + 1, T_1 = 1.} \]

*Verification.* $T_1 = 1, T_2 = 3, T_3 = 7, T_4 = 15, \ldots$. Direct count: $T_2 = 3$ is achievable as (small to B, big to C, small to C); no strategy can do it in 2 moves ✓.

### Solution to PP5 — Pascal's Identity by Induction

Claim: $\binom{n + 1}{r} = \binom{n}{r - 1} + \binom{n}{r}$ for all integers $0 \le r \le n + 1$.

We give two proofs: algebraic (direct from the factorial definition) and combinatorial (the subset-partition argument). Both are inductive in spirit; the combinatorial proof is the cleanest.

**Algebraic proof.** Compute the RHS using $\binom{m}{k} = \frac{m!}{k! (m - k)!}$:
\[
\binom{n}{r - 1} + \binom{n}{r} = \frac{n!}{(r - 1)! (n - r + 1)!} + \frac{n!}{r! (n - r)!}.
\]

Common factor: $\frac{n!}{(r - 1)! (n - r)!}$ pulls out of both terms (since $r! = r \cdot (r - 1)!$ and $(n - r + 1)! = (n - r + 1)(n - r)!$):

\[
\binom{n}{r - 1} + \binom{n}{r} = \frac{n!}{(r - 1)! (n - r)!} \left[ \frac{1}{n - r + 1} + \frac{1}{r} \right] = \frac{n!}{(r - 1)! (n - r)!} \cdot \frac{r + (n - r + 1)}{r (n - r + 1)} = \frac{n!}{(r - 1)! (n - r)!} \cdot \frac{n + 1}{r (n - r + 1)}.
\]

Simplify: $\frac{n! (n + 1)}{r (r - 1)! (n - r + 1) (n - r)!} = \frac{(n + 1)!}{r! (n - r + 1)!} = \binom{n + 1}{r}$. ✓

**Combinatorial proof.** $\binom{n + 1}{r}$ counts $r$-subsets of $\{1, 2, \ldots, n + 1\}$. Partition these subsets by whether they contain the element $n + 1$:
\begin{itemize}
\item Subsets containing $n + 1$: choose the remaining $r - 1$ elements from $\{1, \ldots, n\}$, in $\binom{n}{r - 1}$ ways.
\item Subsets not containing $n + 1$: choose all $r$ elements from $\{1, \ldots, n\}$, in $\binom{n}{r}$ ways.
\end{itemize}

The two cases are mutually exclusive and exhaustive, so $\binom{n + 1}{r} = \binom{n}{r - 1} + \binom{n}{r}$. ✓

The boxed answer:
\[ \boxed{\binom{n + 1}{r} = \binom{n}{r - 1} + \binom{n}{r}.} \]

*Inductive-on-$n$ framing.* The combinatorial proof above is structural; an explicit induction on $n$ proceeds as follows. Base $n = 0$: $\binom{1}{r} = \binom{0}{r - 1} + \binom{0}{r}$. For $r = 1$: $1 = 0 + 1$ ✓. For $r = 0$: $1 = 0 + 1$ (with the convention $\binom{0}{-1} = 0$) ✓. For $r \ge 2$: $0 = 0 + 0$ ✓. Inductive step: given the identity at $n$, derive it at $n + 1$ via the algebraic factorial manipulation above (which holds for any $n$, not just inductively). The algebraic proof is the most efficient route.

### Solution to PP6 — Gambler's Ruin

A gambler starts with $k$ rupees, $0 \le k \le N$. Each round: wins or loses 1 rupee with probability $1/2$ each. Stops when reaching 0 (ruin) or $N$ (win). Let $P_k$ = probability of ruin starting from $k$.

**Boundary conditions.** $P_0 = 1$ (already ruined), $P_N = 0$ (already won).

**Recurrence.** For $1 \le k \le N - 1$, condition on the first move:
\[
P_k = \tfrac{1}{2} P_{k - 1} + \tfrac{1}{2} P_{k + 1}.
\]

Rearrange: $P_{k - 1} - 2 P_k + P_{k + 1} = 0$ — the *discrete Laplace equation*.

**Closed-form solution.** The characteristic polynomial is $\chi(r) = 1 - 2 r + r^2 = (r - 1)^2$, with a *double root* $r = 1$. By the linear-recurrence theory with repeated roots, the general solution is

\[
P_k = (A + B k) \cdot 1^k = A + B k.
\]

Apply boundary conditions: $P_0 = A = 1$ and $P_N = A + B N = 1 + B N = 0$, giving $B = -1/N$. Hence

\[
P_k = 1 - \frac{k}{N}.
\]

The boxed answer:
\[ \boxed{P_k = (P_{k - 1} + P_{k + 1})/2; \quad \text{solution } P_k = 1 - k / N.} \]

*Verification at extremes.* $P_0 = 1$ ✓ (immediate ruin). $P_N = 0$ ✓ (immediate win). $P_{N/2} = 1/2$ (symmetric position has 50-50 chance) ✓. The probability decreases linearly in $k$, consistent with the symmetric-random-walk intuition.

*Interpretation.* The function $P_k = 1 - k/N$ is the discrete harmonic function on $\{0, 1, \ldots, N\}$ with boundary values $P_0 = 1, P_N = 0$. The discrete Laplace equation is the recurrence governing harmonic functions on a 1-D lattice; in the continuous limit (large $N$, scaling $k = xN$ with $x \in [0, 1]$), $P_k \to 1 - x$, the unique solution of the boundary-value problem $-u''(x) = 0$ on $[0, 1]$ with $u(0) = 1, u(1) = 0$. This is the probabilistic version of Dirichlet's principle.

### Solution to PP7 — Binary Strings without Consecutive 1's

Let $a_n$ = number of binary strings of length $n$ with no two consecutive 1's.

**Recurrence derivation.** Partition the valid strings of length $n$ by their last character:
\begin{itemize}
\item String ends in 0: the prefix (length $n - 1$) is any valid string. There are $a_{n - 1}$ such strings.
\item String ends in 1: the prefix's last character must be 0 (else two consecutive 1's). So the prefix has the form (valid string of length $n - 2$) followed by 0. There are $a_{n - 2}$ such strings.
\end{itemize}

Hence $a_n = a_{n - 1} + a_{n - 2}$ for $n \ge 3$. This is the Fibonacci recurrence.

**Base cases.** $a_1 = 2$ (the two strings ``0'' and ``1''). $a_2 = 3$ (the three strings ``00'', ``01'', ``10''; the string ``11'' has two consecutive 1's and is excluded).

**Closed-form identification.** Compute the first few values: $a_1 = 2, a_2 = 3, a_3 = 5, a_4 = 8, a_5 = 13, \ldots$. The values are $F_3, F_4, F_5, F_6, F_7, \ldots$ (where $F_1 = 1, F_2 = 1, F_3 = 2, F_4 = 3, F_5 = 5, \ldots$). Hence $a_n = F_{n + 2}$.

**Verification by induction.** Base: $a_1 = 2 = F_3$ ✓; $a_2 = 3 = F_4$ ✓. Inductive step: assuming $a_{n - 1} = F_{n + 1}$ and $a_{n - 2} = F_n$, get $a_n = a_{n - 1} + a_{n - 2} = F_{n + 1} + F_n = F_{n + 2}$ ✓.

The boxed answer:
\[ \boxed{a_n = a_{n - 1} + a_{n - 2}, \quad a_1 = 2, a_2 = 3, \quad a_n = F_{n + 2}.} \]

*Verification.* At $n = 3$: $a_3 = a_2 + a_1 = 3 + 2 = 5 = F_5$. Direct enumeration of valid length-3 strings: "000", "001", "010", "100", "101" — five strings ✓.

*Connection to Ch. 15 (Bijection).* The Fibonacci recurrence $a_n = a_{n - 1} + a_{n - 2}$ encodes a *bijection* between (valid length-$n$ strings) and ((valid length-$(n - 1)$ strings) $\sqcup$ (valid length-$(n - 2)$ strings)). The bijection is: a length-$n$ string ending in 0 corresponds to a length-$(n - 1)$ string (drop the trailing 0); a length-$n$ string ending in 1 (necessarily preceded by 0) corresponds to a length-$(n - 2)$ string (drop the trailing ``01''). This is a direct combinatorial-Fibonacci bijection in the style of Ch. 15.

---

*End of Chapter 18.*
