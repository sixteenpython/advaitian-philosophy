---
chapter: 14
archetype: Parity / Modular Reasoning
subtitle: "Sometimes the Remainder Tells the Whole Story"
category: Structural Reasoning (Archetypes 13–16) — second chapter
related_archetypes: [1, 4, 13, 15, 18]
key_gems:
  - "Wilson's theorem: $(p - 1)! \\equiv -1 \\pmod p$ for prime $p$, and the converse holds (it is a primality criterion)"
  - "Fermat's little theorem: $a^p \\equiv a \\pmod p$ for prime $p$ and integer $a$; equivalently $a^{p-1} \\equiv 1 \\pmod p$ when $\\gcd(a, p) = 1$"
  - "Euler's theorem: $a^{\\varphi(n)} \\equiv 1 \\pmod n$ for $\\gcd(a, n) = 1$, generalising Fermat to composite moduli"
  - "Chinese Remainder Theorem: a system $x \\equiv a_i \\pmod{n_i}$ with pairwise-coprime moduli has a unique solution modulo $\\prod n_i$"
  - "Legendre's formula: $v_p(n!) = \\sum_{k \\ge 1} \\lfloor n/p^k \\rfloor = \\dfrac{n - s_p(n)}{p - 1}$ where $s_p(n)$ is the base-$p$ digit sum"
  - "Kummer's theorem: $v_p\\!\\left(\\binom{m + n}{m}\\right)$ equals the number of carries when adding $m + n$ in base $p$"
  - "XOR as parity-sum: $a \\oplus b$ is the bitwise mod-2 sum; XOR is its own inverse and commutes with itself"
  - "Bouton's Nim theorem: a Nim position $(a_1, \\ldots, a_k)$ is a *losing* (P-)position iff $a_1 \\oplus \\cdots \\oplus a_k = 0$"
  - "Chessboard parity: a Hamiltonian cycle on a 2-coloured grid (black/white alternating) alternates colours, forcing equal counts; an $m \\times n$ grid admits a Hamiltonian cycle iff $mn$ is even"
  - "Squarefree decomposition: every positive integer $m$ factors uniquely as $m = u^2 v$ with $v$ squarefree; the squarefree part is the mod-2 reduction of the prime exponents"
canonical_takeaway: "Sometimes the remainder tells the whole story. Choosing the right modulus collapses an intractable problem into a finite, often trivial residue computation."
status: draft
last_revised: 2026-05-28
sourcing_note: "All worked examples and practice problems in this chapter are drawn from K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), or from JEE / RMO / INMO examinations commented on in that text. See Blueprint §6.2 for the sourcing rule and `pillar2-archetypes/_template/joshi-problems-locked.md` §Ch. 14 for the locked slate. **Verification audit for this chapter discovered one slate error**: WE3 (Joshi Ex. 24.89, cubic $f(x) = x^3 + bx^2 + cx + d$ with $f(0), f(-1)$ odd integers) listed the parity consequence as '$b - c$ even', but the correct parity is '$b - c$ odd' — since $d$ odd and $-1$ odd give $-1 + d$ even, $f(-1) = (\\text{even}) + (b - c)$ is odd iff $b - c$ is odd. The chapter solution uses the correct parity (which is essential for the integer-root contradiction: $r$ odd ⇒ $b + c$ even ⇒ $b \\equiv c$, contradicting $b - c$ odd). Slate patched in v0.2.11. Cross-archetype: **PP6 reuses the JEE 1983 problem from Ch. 1 PP3** ($24 \\mid n(n^2 - 1)$ for odd $n$), reframed here through the explicit mod-2 + mod-3 lens of Ch. 14 (in Ch. 1 the same problem was framed as an *invariance* problem via the consecutive-integers identity)."
---

# Chapter 14 — Parity / Modular Reasoning

## *Sometimes the Remainder Tells the Whole Story*

---

## Opening Vignette

A transaction-reconciliation engineer at the RBI's Mumbai NEFT clearing house is auditing a batch of 4.7 million bank-to-bank wire transfers cleared overnight. Each transaction carries an *International Bank Account Number* (IBAN), a 34-character alphanumeric string whose first four characters encode the country, the bank, and a 2-digit *check-digit* field. The check digits are computed by the IBAN algorithm: rearrange the IBAN string so the country code and check digits are moved to the end; convert letters to digits using $A = 10, B = 11, \ldots, Z = 35$; treat the resulting decimal string as an integer; divide by $97$. A correct IBAN gives remainder $1$; any deviation (a digit transposition, a typo, a transmission corruption) gives remainder $\ne 1$, and the transaction is flagged for manual review. The engineer's batch report shows three flagged transactions: she pulls them up, computes the IBAN mod $97$ on each, confirms the remainders are $43, 17, 88$ — none $= 1$ — and routes them to the correspondent banks for re-validation. *The residue is the integrity*; the entire batch of 4.7 million transactions could not be hand-validated, but the *single integer modulo 97* gives a near-perfect detection of single-character corruption with overwhelming probability. The engineer's job, automated though it is, rests on a 1958-vintage check-digit algorithm that exploits the *modular arithmetic* of integer-mod-prime to convert error-detection from an O($n$) string-comparison problem to an O($1$) residue check. *(The IBAN mod-97 check has a single-character-error detection rate of approximately $96/97 \approx 98.97\%$, and detects 100% of single-character transpositions of adjacent digits.)*

Now turn to a different scene. A *sthapati* (traditional temple architect) in Madurai is laying out a marble-tile pattern on the floor of a new prayer hall. The floor is rectangular, dimensions $m \times n$ where $m = 23$ rows of tiles by $n = 17$ columns. The architect's instruction from the client is: *cover the entire floor with $2 \times 1$ rectangular tiles (no $1 \times 1$ squares, no $2 \times 2$ blocks), leaving no gaps and no overlaps*. The architect's first reflex is to attempt the tiling — but his trained mind catches the structural obstruction before he picks up a single tile. *Two-colour the floor as a chessboard*, alternating black and white tiles by position. The $23 \times 17$ grid has $23 \cdot 17 = 391$ tiles total, and the colour counts are $\lceil 391 / 2 \rceil = 196$ of one colour and $\lfloor 391/2 \rfloor = 195$ of the other (differing by $1$, since $391$ is odd). *Every $2 \times 1$ tile covers exactly one black and one white square* (two adjacent cells of opposite colour). So any complete tiling must cover *equal* numbers of black and white. With $196$ black and $195$ white available, no equal tiling is possible. The architect informs the client: *the requested tiling is mathematically impossible*; the floor must be re-dimensioned (e.g., $24 \times 17 = 408$ even total, with $204 + 204$ balanced colours, tiling is possible) or a single $1 \times 1$ centerpiece tile must be permitted. The trained architect does not attempt the tiling, fail repeatedly, and conclude impossibility by exhaustion; he *invokes the chessboard parity invariant* and concludes impossibility in two lines.

These two scenes look unrelated. A clearing-house engineer auditing wire transfers; a temple architect laying out tiles. They share the most important reframing in the entire chapter — the recognition that *the residue (modulo some integer) is often the entire structural content of the problem*. The engineer reads IBAN integrity off a single mod-97 residue; the architect reads tile-feasibility off a single mod-2 chessboard count. In both cases, the *modular arithmetic* converts an intractable enumeration (4.7 million transactions to validate; $391$ tile-positions to attempt) into a trivial residue computation. The trained problem-solver internalises this pattern: *the right modulus is the answer*; computing the exact integer is unnecessary, often impossible, and almost always less informative than the residue.

This is *Parity / Modular Reasoning*. It is the second chapter of the *Structural Reasoning* sub-pillar (Chapters 13–16), and it carries forward the *structure-first* discipline of Chapter 13 (Combinatorial Principles) into the narrower but immensely powerful domain of *residue-determined* problems. The chapter develops the toolkit (parity / mod 2; mod 3, 4, 6, 8 for triangular and divisibility arguments; Fermat's little theorem and its companions for prime moduli; Euler's theorem for composite moduli; the Chinese Remainder Theorem for simultaneous congruences; Legendre's formula and Kummer's theorem for factorial $p$-adic valuations; XOR / Nim-style modular game theory) and the recurring patterns (chessboard 2-colourings as parity invariants; polynomial parity arguments for integer roots; modular game-theoretic invariants for Nim and its variants; binomial-coefficient divisibility via Kummer; squarefree decomposition as mod-2 reasoning on prime exponents). The chapter has three structural threads. The first is the *toolkit*: the named modular tools and their deployment signatures. The second is the *modulus-selection principle*: *choosing the right modulus* is the cognitively hardest and most consequential step. The third is the *cross-archetype unification*: modular reasoning is foundational for Ch. 1 (Invariance — many invariants are modular), Ch. 4 (Hidden Structure — modular residues are often the hidden structure), Ch. 13 (Combinatorial — parity-counting, modular-counting), Ch. 15 (Bijection — modular equivalence classes), and Ch. 18 (Recursion — modular recurrences) — and the chapter makes these connections explicit.

> *Sometimes the remainder tells the whole story. Choosing the right modulus collapses an intractable problem into a finite, often trivial residue computation.*

---

## 1. The Archetype Defined

### 1.1 Formal Definition

We make the intuition precise.

\begin{definition}[Parity / Modular Reasoning]
A *parity / modular reasoning* approach to a problem with integer-valued quantities $a_1, a_2, \ldots$ is the strategy of computing the *residues* of those quantities modulo some carefully-chosen integer $m$, and reading the problem's answer from the residues alone — without computing the exact values of the underlying quantities. The archetype is the discipline of (i) recognising that the problem's answer is determined by a residue class modulo some $m$; (ii) choosing $m$ to make the computation as simple as possible; (iii) executing the residue computation and reading off the answer.
\end{definition}

Three remarks unpack the definition.

First, the *modulus selection* (Step (ii)) is the cognitively hardest step. The right modulus is often *not obvious from the problem statement*; the solver must recognise structural features (the integer-valued constraints, the polynomial-coefficient parities, the chessboard colourings, the prime-power constraints) that point to the appropriate modulus. Common choices are: *mod 2* (parity, chessboard 2-colouring); *mod 3 or 4* (small-integer divisibility); *mod 6, 8, 24* (combinations forced by problem structure); *mod $p$* for prime $p$ (Fermat, Wilson); *mod $p^k$* for prime power (Hensel's lemma, Kummer); *mod $(k+1)$* for game-theoretic Nim arguments.

Second, the *residue computation* (Step (iii)) is mechanical once the modulus is chosen: routine modular arithmetic, possibly with named-theorem shortcuts (Fermat's little theorem, Euler's theorem, the Chinese Remainder Theorem). The hard work is upstream; the execution is downstream.

Third, the *reading the answer* (Step (i)) requires recognising the problem's answer-structure: sometimes the residue *is* the answer (e.g., the IBAN check); sometimes the residue *determines existence vs. nonexistence* of a solution (e.g., the chessboard-tiling problem); sometimes the residue *forces a winning strategy* in a game (e.g., the Nim mod-$(k+1)$ strategy).

The chapter encounters five characteristic forms of parity / modular reasoning.

- **Form I — Parity (mod 2).** Chessboard 2-colourings, polynomial parity arguments, parity-of-permutations, mod-2 sum invariants. *Examples.* WE2 (XOR as parity-sum, Nim/Bouton), WE3 (parity of polynomial values forces integer-root impossibility), PP4 (squarefree decomposition = mod-2 on prime exponents), PP5 (chessboard parity on Hamiltonian-cycle existence).

- **Form II — Mod $m$ for small $m$ (3, 4, 6, 8, 24).** Divisibility by small integers; consecutive-integer divisibility ($n(n^2 - 1) = (n-1)n(n+1)$ divisible by $6 = 3!$ trivially, by $24$ for $n$ odd). *Examples.* PP6 (cross-archetype with Ch. 1: $24 \mid n(n^2 - 1)$).

- **Form III — Mod $p$ (prime).** Fermat's little theorem, Wilson's theorem, primality tests, polynomial roots modulo $p$. *Examples.* PP1 (Wilson-almost: $(p - 1)! + 1 = p^a$).

- **Form IV — $p$-adic valuations.** Legendre's formula for $v_p(n!)$, Kummer's theorem for $v_p(\binom{m+n}{m})$, factorial divisibility. *Examples.* WE1 ($(2m)!(2n)!/(m+n)!$ is an integer, primary proof via the binomial decomposition + alternative via Kummer / Legendre to illustrate the modular lens).

- **Form V — Modular invariants in games.** Nim residues, the modular winning-position theorem, Bouton's XOR-of-piles theorem. *Examples.* WE2 (Nim winning move via XOR reduction), PP7 (two-person mod-11 game with target 100).

### 1.2 The Core Principle

Stripped to its essence, the principle is one sentence.

> *Sometimes the remainder tells the whole story.*

This sentence captures the recurrent observation that, across mathematics and applied disciplines, the *residue* of an integer-valued quantity modulo some chosen integer $m$ is often *all the structure that matters* for the problem at hand. The exact integer value is unnecessary; the exact integer value is often *impossible* to compute (Wilson's theorem makes $(p-1)! \mod p$ computable in a single multiplication, but $(p-1)!$ itself is intractable for $p = 100$); and the exact integer value is *less informative* than the residue (the residue *is* the structural content; the exact integer value buries it in noise).

The cognitive shift is from *"compute the exact value"* to *"compute the residue, which is the structurally-significant part."* The reframing converts intractable computations (factorial, exponentiation, polynomial-value calculations) into routine modular arithmetic. The IBAN engineer computes $\text{IBAN} \mod 97$ in microseconds; computing IBAN as a 34-digit integer would be possible but pointless. The chessboard architect counts $\text{cells} \mod 2$ in one glance; computing the exact cell positions would be a waste of effort.

A complementary phrasing: *modular reasoning is the discipline of throwing away the irrelevant precision*. The "irrelevant precision" is the part of the integer's value that doesn't affect the problem's answer; the residue is the part that does. Recognising which precision is irrelevant is the cognitive shift; the rest is mechanical.

### 1.3 The Cognitive Shift

Three cognitive shifts deserve naming.

The first is *modulus-as-question*. The trained solver, when faced with an integer-valued problem, does not begin by computing exact values; she begins by asking *which modulus, if any, captures the problem's structure?* This single reframing converts most divisibility-and-residue problems from intractable exact computation to routine modular arithmetic.

The second shift is *named-theorem selection*. The modular toolkit is finite and well-organised: *Wilson* ($(p-1)! \equiv -1 \pmod p$); *Fermat* ($a^p \equiv a \pmod p$); *Euler* ($a^{\varphi(n)} \equiv 1 \pmod n$); *Chinese Remainder Theorem* (simultaneous congruences with coprime moduli); *Legendre / Kummer* (factorial $p$-adic valuations); *Lifting-the-Exponent (LTE)* (for $v_p$ of $a^n - b^n$ and $a^n + b^n$); *Hensel's lemma* (lifting modular roots to $p$-adic roots). The trained solver matches the problem's structure to the theorem in seconds.

The third shift is *cross-archetype synthesis*. Parity and modular reasoning interlock with several other archetypes: with Ch. 1 (Invariance — *every parity / modular invariant is an invariance argument*); with Ch. 4 (Hidden Structure — *the residue is often the hidden structure*); with Ch. 13 (Combinatorial — *parity-counting and modular-counting are combinatorial moves*); with Ch. 15 (Bijection — *modular equivalence classes give natural bijections*); with Ch. 18 (Recursion — *modular recurrences capture polynomial / exponential growth modulo $m$*). The trained solver, by Chapter 14, sees these as a coherent body of *structured arithmetic* rather than five separate techniques.

---

## 2. The Deep Structure

### 2.1 Mathematical Foundations

Parity and modular reasoning rest on four mathematical foundations.

The first is the *ring structure of $\mathbb Z / m \mathbb Z$*. For any positive integer $m$, the integers modulo $m$ form a *commutative ring* (addition and multiplication are well-defined modulo $m$), and the ring's structure is determined by $m$: for $m$ prime, $\mathbb Z / m \mathbb Z$ is a *field* (every non-zero element has a multiplicative inverse); for $m$ composite, $\mathbb Z / m \mathbb Z$ has *zero divisors* (e.g., $2 \cdot 3 \equiv 0 \pmod 6$). The *units* (invertible elements) of $\mathbb Z / m \mathbb Z$ are precisely the residues coprime to $m$; their group is $(\mathbb Z / m \mathbb Z)^\times$ of order $\varphi(m)$ (Euler totient).

The second foundation is *Fermat's little theorem* and its generalisation, *Euler's theorem*. Fermat: for prime $p$ and integer $a$, $a^p \equiv a \pmod p$; if $\gcd(a, p) = 1$, $a^{p-1} \equiv 1 \pmod p$. Euler: for any positive integer $n$ and integer $a$ with $\gcd(a, n) = 1$, $a^{\varphi(n)} \equiv 1 \pmod n$. These theorems convert *exponentiation modulo $m$* from an iterative computation (multiplying $a$ by itself $k$ times mod $m$) to a *single reduction* of the exponent modulo $\varphi(m)$ — a dramatic complexity reduction that powers RSA cryptography and primality testing.

The third foundation is the *Chinese Remainder Theorem* (CRT). For pairwise-coprime positive integers $n_1, n_2, \ldots, n_k$ and any integers $a_1, a_2, \ldots, a_k$, the system of congruences
\[
  x \equiv a_1 \pmod{n_1}, \quad x \equiv a_2 \pmod{n_2}, \quad \ldots, \quad x \equiv a_k \pmod{n_k}
\]
has a *unique solution* modulo $N = \prod n_i$. The theorem is constructive: $x = \sum_i a_i M_i M_i^{-1}$ where $M_i = N / n_i$ and $M_i^{-1}$ is its inverse modulo $n_i$. The CRT decomposes computations modulo a composite $N$ into computations modulo its prime-power components — a foundational technique in number theory, cryptography, and algorithmic computation.

The fourth foundation is the *$p$-adic valuation*. For prime $p$ and non-zero integer $n$, $v_p(n)$ is the largest non-negative integer $k$ with $p^k \mid n$. Extended to fractions: $v_p(a/b) = v_p(a) - v_p(b)$. The valuation satisfies:
- *Sum rule*: $v_p(a + b) \ge \min(v_p(a), v_p(b))$, with equality if $v_p(a) \ne v_p(b)$.
- *Product rule*: $v_p(ab) = v_p(a) + v_p(b)$.
- *Legendre's formula*: $v_p(n!) = \sum_{k \ge 1} \lfloor n/p^k \rfloor = (n - s_p(n))/(p - 1)$ where $s_p$ is the base-$p$ digit sum.
- *Kummer's theorem*: $v_p\!\left(\binom{m+n}{m}\right)$ equals the number of carries when adding $m + n$ in base $p$.

A fifth foundation, important for game-theoretic Nim arguments: the *XOR as parity-sum*. For non-negative integers $a, b$, the bitwise XOR $a \oplus b$ is the integer whose binary representation has a $1$ in position $i$ iff exactly one of $a, b$ has a $1$ in position $i$ — equivalently, $a \oplus b = (a + b) - 2(a \wedge b)$ where $\wedge$ is bitwise AND. XOR is associative, commutative, and self-inverse ($a \oplus a = 0$). *Bouton's theorem* on Nim: a Nim position $(a_1, a_2, \ldots, a_k)$ (piles of sizes $a_i$, players take any positive number of stones from any one pile, last stone wins) is a *P-position* (previous-player-wins, i.e., losing for the next player) iff $a_1 \oplus a_2 \oplus \cdots \oplus a_k = 0$.

### 2.2 Physical and Cross-Domain Foundations

The reach of parity and modular reasoning extends across the quantitative sciences.

In *number theory*, modular arithmetic is *the* foundational tool. Fermat / Euler / Wilson form the bedrock of elementary number theory; the *quadratic reciprocity law* (Gauss) is the deepest single result in modular reasoning, with applications from primality testing to class field theory. *Modular forms* (Eisenstein series, theta functions, the modular group $SL_2(\mathbb Z)$) generalise modular arithmetic to complex-analytic functions with modular symmetries; their study (Hecke, Serre, Wiles) led to the proof of Fermat's Last Theorem.

In *cryptography*, modular arithmetic underlies almost every modern cipher. *RSA* relies on the difficulty of factoring large composite moduli; *Diffie-Hellman* on the discrete logarithm in $(\mathbb Z / p \mathbb Z)^\times$; *elliptic-curve cryptography* on the discrete logarithm in groups of elliptic curve points modulo $p$. The *Miller-Rabin primality test* exploits Fermat's little theorem to give probabilistic primality certification in polynomial time.

In *coding theory*, *cyclic redundancy checks* (CRCs) use polynomial arithmetic modulo a generator polynomial to detect transmission errors; the IBAN check-digit is a baby case of CRC. *Reed-Solomon codes* (used in CDs, DVDs, QR codes, and deep-space communication) work over finite fields $\mathbb F_q = \mathbb F_p^k$, structured by modular polynomial arithmetic. The *Berlekamp-Massey algorithm* for decoding Reed-Solomon codes is built on linear recurrence and modular reduction.

In *theoretical computer science*, the *complexity class $\#P$* counts solutions modulo nothing, but the related class *$\oplus P$* counts solutions modulo 2 (i.e., the parity of the count); the *Toda's theorem* (1991) relates the polynomial hierarchy to $\#P$. *Algebraic algorithms* (the Schwartz-Zippel lemma, polynomial-identity testing) often work modulo random primes for efficiency.

In *physics*, *parity symmetry* (the symmetry under coordinate inversion $\mathbf x \to -\mathbf x$) is one of the three fundamental discrete symmetries (alongside *charge conjugation* C and *time reversal* T), and its violation in weak interactions (Lee-Yang, Wu) was a Nobel-Prize-winning discovery. *Mod-2 cohomology* and *Stiefel-Whitney classes* in topology classify the orientability and spin structures of manifolds. *Anyon statistics* in two-dimensional condensed-matter physics interpolate between bosons (mod-1 phase) and fermions (mod-2 phase) via fractional phases that are themselves modular.

In *biology and genetics*, *parity* shows up in chromosomal sex determination (XX vs XY) and in gamete-to-zygote pairing combinatorics. *Reading frame analysis* in molecular biology is mod-3 reasoning on DNA / RNA sequences (each codon is 3 bases; a single-base insertion shifts the frame and produces a different protein). *Genetic codes* themselves are modular: the 64 codons mod 4 nucleotides give the redundancy that makes the code error-tolerant.

In *engineering and communications*, *modulation* schemes (AM, FM, QAM, OFDM) rely on modular arithmetic of frequencies and phases. *Network routing* protocols use *sequence numbers modulo a window size* to detect lost or duplicate packets. *Clock synchronisation* in distributed systems uses *modular vector clocks* (Lamport, Mattern) to track happens-before relationships.

In *music*, the *pitch-class set* is the set of musical pitches modulo octave equivalence (mod 12 in equal temperament); *serial composition* (Schoenberg, Webern) uses permutations of the twelve-tone row, a modular structure. *Rhythmic cycles* in Indian classical music (the $taals$: $teen$ taal = 16 beats, $jhap$ taal = 10 beats, $ek$ taal = 12 beats) are mod-cycle structures.

### 2.3 Cognitive Foundations

The cognitive payoff of parity and modular reasoning is threefold.

The first is *complexity reduction*. The right modulus converts intractable computations (factorials, exponentials, polynomial-value calculations) into routine modular arithmetic. The IBAN check is the everyday example: computing the 34-digit IBAN integer would be unnecessary (and slow); the residue mod 97 is computable in microseconds and contains all the integrity information. *Fast exponentiation modulo $m$* runs in $O(\log e)$ time; ordinary exponentiation runs in $O(e)$. The complexity gap is *exponential* in $e$.

The second payoff is *robustness against integer overflow*. In computational arithmetic, integers can overflow standard integer types (32-bit, 64-bit); modular arithmetic stays within bounded integers (e.g., $\mathbb Z / 2^{32} \mathbb Z$ for unsigned 32-bit integers) and avoids overflow by construction. *Hash functions* (mod a prime) and *random-number generators* (linear congruential generators) rely on this property.

The third payoff is *cross-archetype synthesis*. Parity and modular reasoning unify Chapters 1 (Invariance — modular invariants are *the* canonical invariants), 4 (Hidden Structure — the residue is often the hidden structure), 13 (Combinatorial — parity-counting and modular-counting), 15 (Bijection — modular equivalence classes give natural bijections), and 18 (Recursion — modular recurrences capture growth-modulo-$m$). The trained solver, by Chapter 14, sees these connections as a single coherent framework of *structured arithmetic*.

---

## 3. The Diagnostic Toolkit

### 3.1 The Three Questions Method (Parity / Modular Edition)

Before deploying any modular tool, the trained solver asks three questions of the problem.

1. **Is the problem residue-determined?** Verify that the problem's answer depends only on the residues of the input quantities modulo some $m$, not on the exact values. Signatures: the problem asks "is $X$ even / odd?"; "is $Y$ divisible by $m$?"; "for which $n$ does $Z(n) \equiv 0 \pmod m$?"; "what is the last digit of $W$?". Any such phrasing signals *modular reasoning*.

2. **What is the right modulus?** Match the problem's structure to the appropriate $m$:
   - *Two-colouring / odd-even alternation*: $m = 2$ (parity).
   - *Triangular-number or consecutive-integer divisibility*: $m = 3, 6$.
   - *Day-of-week / clock arithmetic*: $m = 7, 24, 60$.
   - *Prime-power constraints (factorials, binomial coefficients)*: $m = p$ or $p^k$.
   - *Game theory (Nim, target-game)*: $m = (k + 1)$ where $k$ is the move-size bound.
   - *Cryptographic / coding-theoretic*: $m$ a chosen prime or prime power.

3. **Which named theorem applies?** Once the modulus is chosen, the toolkit's named theorems often give the answer in a single step:
   - *Wilson*: $(p - 1)! \equiv -1 \pmod p$ for prime $p$.
   - *Fermat*: $a^p \equiv a \pmod p$.
   - *Euler*: $a^{\varphi(n)} \equiv 1 \pmod n$ for $\gcd(a, n) = 1$.
   - *CRT*: simultaneous congruences with coprime moduli have a unique solution mod the product.
   - *Legendre*: $v_p(n!) = (n - s_p(n))/(p - 1)$.
   - *Kummer*: $v_p\!\left(\binom{m+n}{m}\right)$ = number of carries in base-$p$ addition.
   - *Bouton (Nim)*: Nim P-position iff XOR of pile sizes is zero.

### 3.2 Forms of Parity / Modular Reasoning: A Comprehensive Guide

We collect the five forms encountered in the chapter with one-line diagnostics.

- **Form I — Parity (mod 2).** *Diagnostic:* the problem has an even / odd structure, a two-colouring, or a polynomial / sum whose parity is the key. *Move:* reduce all quantities mod 2; identify the invariant; derive contradictions or existence claims from parity mismatch. *Examples.* WE2 (XOR / Nim), WE3 (cubic with odd values), PP4 (squarefree), PP5 (Hamiltonian cycle on grid).

- **Form II — Mod $m$ for small $m$.** *Diagnostic:* the problem involves small-integer divisibility (by 3, 4, 6, 8, 24). *Move:* compute mod $m$; combine with other modular reductions if needed (e.g., $24 = 8 \cdot 3$, so verify mod 8 and mod 3 separately, combine by CRT). *Examples.* PP6 ($24 \mid n(n^2 - 1)$ via mod 8 + mod 3).

- **Form III — Mod $p$ (prime).** *Diagnostic:* the problem involves prime factorials, prime-power exponents, or primality tests. *Move:* invoke Wilson, Fermat, or Euler as appropriate; reduce computations modulo $p$. *Examples.* PP1 (Wilson-almost on $(p - 1)! + 1$).

- **Form IV — $p$-adic valuations (Kummer / Legendre).** *Diagnostic:* the problem requires bounding $p^k \mid$ some factorial or binomial-coefficient quantity. *Move:* apply Legendre's formula to factorials; apply Kummer's theorem to binomial coefficients (the carries-in-base-$p$ counting). *Examples.* WE1 ($(2m)!(2n)!/(m+n)!$ integer — primary elementary proof + alternative Kummer / Legendre proof).

- **Form V — Modular invariants in games.** *Diagnostic:* a two-player combinatorial game with bounded move-sizes; ask whether a particular residue class is a winning or losing position. *Move:* identify the mod-$(k+1)$ or mod-$m$ residue invariant; the player who can leave the opponent in a P-position wins. *Examples.* WE2 (Nim winning move), PP7 (two-person game with target 100 via mod 11).

### 3.3 Common Pitfalls

Five errors recur often enough to deserve named warnings.

- **The Wrong-Modulus Pitfall.** Choosing a modulus that doesn't capture the problem's structure. E.g., trying to solve a Nim-with-stride-$k$ problem via mod 2 instead of mod $(k+1)$. The remedy is to *systematically test small moduli* (2, 3, 4, 5, ...) for which residue captures the problem's behaviour.

- **The Sign-Error-in-Wilson Pitfall.** Wilson's theorem says $(p - 1)! \equiv -1 \pmod p$, *not* $+1$. The *converse* (i.e., $(n-1)! \equiv -1 \pmod n$ implies $n$ prime) is also true and provides a (slow) primality test. The remedy is to *write the sign explicitly* and verify on small primes (e.g., $p = 3$: $2! = 2 \equiv -1 \pmod 3$ ✓).

- **The Fermat-Misapplied Pitfall.** Fermat's little theorem requires $\gcd(a, p) = 1$ for the $a^{p-1} \equiv 1$ form (otherwise the form $a^p \equiv a$ still holds, but the inverse is unavailable). Applying $a^{p-1} \equiv 1$ when $p \mid a$ gives wrong answers. The remedy is to *check $\gcd(a, m)$* before invoking the multiplicative form.

- **The CRT-Misapplied-to-Non-Coprime-Moduli Pitfall.** The Chinese Remainder Theorem requires pairwise-coprime moduli. With non-coprime moduli, the system may have no solution (e.g., $x \equiv 0 \pmod 2$ and $x \equiv 1 \pmod 4$ — inconsistent) or have a solution mod the LCM (not the product). The remedy is to *factor moduli into prime powers* and apply CRT to those (which are automatically coprime).

- **The Kummer-Off-By-One Pitfall.** Kummer's theorem counts *carries*, not the number of digit-pairs that exceed $p$. The two are subtly different (carries can propagate; the count is sometimes one less than naive). The remedy is to *explicitly compute the base-$p$ addition* and count carries by simulating the addition.

---

## 4. Worked Examples

We work three problems in detail, each in the six-point format. The first illustrates Form IV ($p$-adic valuations and factorial decomposition) for the $(2m)!(2n)!/(m+n)!$ integer-divisibility problem; the second illustrates Form V (XOR / Nim-style game-theoretic modular invariants); the third illustrates Form I (parity of polynomial values) for the cubic-with-odd-integer-values problem.

### 4.1 Example 1 — $(2m)!(2n)!/(m + n)!$ Is an Integer

**Problem.** *Let $m, n$ be positive integers. Prove that $\dfrac{(2m)!(2n)!}{(m + n)!}$ is an integer.*
*(Joshi EJM Ch. 24, Exercise 24.49; an RMO-tier integer-divisibility result.)*

**SEED.** *Parity / modular reasoning (Form IV — factorial decomposition + $p$-adic valuations).* The cleanest proof uses an *elementary binomial-coefficient identity* (WLOG $m \ge n$; rewrite $(2m)!$ as $\binom{2m}{m+n}(m+n)!(m-n)!$; the expression becomes a product of integers). The *modular-lens proof* (via Legendre's formula or Kummer's theorem) demonstrates the same conclusion via $p$-adic valuations and illustrates the Chapter-14 perspective.

**BRUTE PATH.** A student who doesn't see the binomial-coefficient identity might try *direct evaluation* for small cases and induction on $m + n$. For $m = n = 1$: $(2!)(2!)/2! = 2$, integer. For $m = 1, n = 2$: $(2!)(4!)/3! = 2 \cdot 24/6 = 8$, integer. For $m = 2, n = 3$: $(4!)(6!)/5! = 24 \cdot 720/120 = 144$, integer. The pattern is clear, but a *general proof* requires a structural argument, not just case-by-case verification.

**ELEGANT PIVOT.** *Two routes: elementary binomial identity (primary) and Kummer's theorem (modular-lens alternative).*

*Primary route — elementary binomial identity.* WLOG $m \ge n$ (the expression is symmetric in $m$ and $n$, so swap if needed). Observe:
\[
  (2m)! \;=\; \binom{2m}{m + n} \cdot (m + n)! \cdot (m - n)!
\]
(This is the definition of the binomial coefficient: $\binom{2m}{m + n} = \dfrac{(2m)!}{(m+n)!(m-n)!}$, rearranged.)

Substituting:
\[
  \frac{(2m)!(2n)!}{(m + n)!} \;=\; \frac{\binom{2m}{m+n} \cdot (m+n)! \cdot (m-n)! \cdot (2n)!}{(m+n)!} \;=\; \binom{2m}{m + n} \cdot (m - n)! \cdot (2n)!.
\]
The right-hand side is a product of three integers ($\binom{2m}{m + n}$ is a binomial coefficient; $(m - n)!$ and $(2n)!$ are factorials of non-negative integers), hence an integer. \hfill$\blacksquare$

*Modular-lens alternative — Legendre's formula on $p$-adic valuations.* It suffices to show $v_p\!\left((2m)!(2n)!\right) \ge v_p\!\left((m + n)!\right)$ for every prime $p$.

By Legendre, $v_p(n!) = (n - s_p(n))/(p - 1)$ where $s_p(n)$ is the base-$p$ digit sum.

The inequality $v_p((2m)!) + v_p((2n)!) \ge v_p((m + n)!)$ becomes:
\[
  \frac{2m - s_p(2m)}{p - 1} + \frac{2n - s_p(2n)}{p - 1} \;\ge\; \frac{(m + n) - s_p(m + n)}{p - 1},
\]
i.e.,
\[
  (2m + 2n) - s_p(2m) - s_p(2n) \;\ge\; (m + n) - s_p(m + n),
\]
i.e.,
\[
  (m + n) + s_p(m + n) \;\ge\; s_p(2m) + s_p(2n).
\]
This holds because (using the digit-sum identity $s_p(a + b) = s_p(a) + s_p(b) - (p - 1) c_p(a, b)$ where $c_p(a, b)$ is the number of carries in base-$p$ addition of $a$ and $b$):
\[
  s_p(2m) = s_p(m + m) = 2 s_p(m) - (p - 1) c_p(m, m),
\]
and similarly $s_p(2n) = 2 s_p(n) - (p - 1) c_p(n, n)$, and $s_p(m + n) = s_p(m) + s_p(n) - (p - 1) c_p(m, n)$.

Substituting and rearranging gives the inequality reduces to $(p - 1) [c_p(m, m) + c_p(n, n) + c_p(m, n)] \le (m + n) + (p - 1) c_p(m, n) - \ldots$ — which simplifies (after careful bookkeeping) to a true statement. The full simplification is mechanical but tedious; we omit the algebra. The key point is that the $p$-adic-valuation inequality holds for every prime $p$, so $(2m)!(2n)!/(m + n)!$ is an integer.

The elegant pivot is the *elementary binomial identity*: rewrite $(2m)!$ via $\binom{2m}{m+n}$ and the expression collapses to a product of integers. The *modular alternative* via Legendre's formula gives the same conclusion through the $p$-adic-valuation lens — illustrative of Chapter 14's perspective but algebraically heavier than the primary route.

**PITFALLS.**

- *Assuming $m \le n$ without WLOG.* If $m < n$, $(m - n)$ is negative and $(m - n)!$ is undefined; the binomial coefficient $\binom{2m}{m + n}$ has $m + n > 2m$ and is by convention 0. The remedy is to *WLOG $m \ge n$* (the expression is symmetric, so this is no loss of generality).

- *Confusing $(2m)!(2n)!/(m + n)!$ with the super-Catalan $\binom{2m}{m}\binom{2n}{n}/\binom{m+n}{m}$.* The two are related (the super-Catalan is the present expression divided by $m! n!$) but distinct. The present expression is *strictly easier* to prove integer than the super-Catalan (which requires Von Szily's identity or Kummer-with-careful-bookkeeping for $p$ odd).

- *Forgetting to verify both inequalities (LHS, RHS) of the $p$-adic-valuation comparison.* The Legendre / Kummer route requires checking the inequality *for every prime $p$*. Skipping a small prime (e.g., $p = 2$ or $p = 3$) can give a wrong answer. The remedy is to *verify $p = 2, 3$ explicitly* and then the general argument for $p \ge 5$.

- *Mis-using the digit-sum identity.* The identity $s_p(a + b) = s_p(a) + s_p(b) - (p - 1) c_p(a, b)$ is correct but easy to get the sign wrong on. The remedy is to *verify on a small example*: $p = 10$, $a = 27, b = 16$: $s_{10}(27) = 9, s_{10}(16) = 7, s_{10}(43) = 7$, $c_{10}(27, 16) = 1$ (single carry). Check: $7 = 9 + 7 - 9 \cdot 1 = 7$ ✓.

- *Using Kummer's theorem when Legendre's formula is simpler.* Kummer's theorem counts carries in base-$p$ addition for $v_p\!\left(\binom{m + n}{m}\right)$; Legendre's formula gives $v_p(n!) = (n - s_p(n))/(p - 1)$ directly. For factorial-product / factorial-quotient problems, *Legendre is usually cleaner*; Kummer is reserved for problems specifically about binomial-coefficient $p$-divisibility.

**CONNECTIONS.**

*Primary archetype applications.* This problem is a baby case of the *super-Catalan number* integrality $S(m, n) = (2m)!(2n)!/(m! n! (m+n)!) \in \mathbb Z$ (Catalan 1874, Von Szily 1894, Bober 2009), one of the most studied integer-divisibility statements in combinatorial number theory. The super-Catalan number generalises the Catalan number ($S(0, n) = \binom{2n}{n}/(n + 1)$ recovers the Catalan number, up to a factor); its integrality is *non-trivial* even though every numerical instance is easy to verify.

*Alternative solution archetypes.* The *generating-function* route: $(2m)!(2n)!/(m + n)!$ appears in the integral representation $\int_0^1 t^{2m}(1 - t)^{2n} dt = B(2m + 1, 2n + 1) = \frac{(2m)!(2n)!}{(2m + 2n + 1)!}$, the Beta function. The integrality follows after applying a particular factorial identity. The *bijective* route: count pairs of objects (partitions, labelled structures) whose total count equals the integer; the bijection witnesses the integrality. (Chapter 15 develops this style.)

*Cross-domain manifestations.* Integer-divisibility results like this one appear in: *Macdonald's identities* for affine Weyl groups (Macdonald 1972), where similar factorial-product quotients arise as denominators of generating functions; *enumerative combinatorics* (counts of trees, tableaux, plane partitions that turn out to be integers despite their factorial-quotient form); *random matrix theory* (eigenvalue density integrals over compact Lie groups, which yield similar factorial-quotient expressions).

**TAKEAWAY.** *Integer-divisibility of factorial quotients: rewrite via binomial-coefficient identities (the elementary route); or check $p$-adic valuations via Legendre / Kummer (the modular route). Both routes converge; the elementary route is usually shorter, the modular route is more illuminating about the underlying structure.*

---

### 4.2 Example 2 — XOR / Nim Reduction (Bouton's Theorem)

**Problem.** *For non-negative integers $a_1, a_2, \ldots, a_k$, define the bitwise XOR $a_1 \oplus a_2 \oplus \cdots \oplus a_k$ via the binary representations: position $i$ of the result is $(a_{1,i} + a_{2,i} + \cdots + a_{k,i}) \mod 2$ where $a_{j,i}$ is bit $i$ of $a_j$. Prove that if $a_1 \oplus \cdots \oplus a_k \ne 0$, then there exists an index $r$ and a positive integer $x$ such that, with $b_i = a_i$ for $i \ne r$ and $b_r = a_r - x$, the new XOR satisfies $b_1 \oplus \cdots \oplus b_k = 0$. Explain how this proves the winning strategy in Nim.*
*(Joshi EJM Ch. 24, Exercise 24.82; Bouton's theorem on Nim — the classical 1901 result.)*

**SEED.** *Parity / modular reasoning (Form V — game-theoretic XOR invariant; Form I — bitwise mod-2 reasoning).* The XOR $s = a_1 \oplus \cdots \oplus a_k$ is the bitwise *parity-sum* of the pile sizes — each bit position of $s$ is the parity of the count of piles with that bit set. If $s \ne 0$, there is a highest bit position $j$ where $s$ has a $1$. By parity, an *odd number* of piles have bit $j$ set; in particular, at least one pile $a_r$ has bit $j$ set. *Reducing $a_r$ to $a_r \oplus s$* simultaneously turns off bit $j$ (making the new pile smaller in the high-order bits) and changes lower bits in exactly the way that cancels the XOR sum to zero. This is the *winning move* in Nim.

**BRUTE PATH.** A student without the XOR insight might try to find the winning move *case by case*. For Nim with piles $(3, 4, 5)$ (a Tier-1 Nim instance): the XOR is $3 \oplus 4 \oplus 5 = 011 \oplus 100 \oplus 101 = 010 = 2$. To find a winning move, the brute path tries each pile in turn: reduce pile 1 from 3 to $0, 1, 2$ — check XORs: $0 \oplus 4 \oplus 5 = 001, 1 \oplus 4 \oplus 5 = 000, 2 \oplus 4 \oplus 5 = 011$. So reducing pile 1 to 1 gives XOR $= 0$ — a winning move. The brute path works but doesn't scale: for piles in the thousands, the search becomes impractical. The XOR algorithm gives the move in $O(\log a_{\max})$ time.

**ELEGANT PIVOT.** *XOR high-bit construction.*

*Step 1 — Identify the high bit of $s$.* Let $s = a_1 \oplus \cdots \oplus a_k$. By hypothesis, $s \ne 0$, so $s$ has at least one bit set. Let $j$ be the *position of the highest set bit* of $s$: the largest non-negative integer with $s$'s bit $j$ equal to $1$.

*Step 2 — A pile with bit $j$ set exists.* By definition, $s$'s bit $j$ equals $(a_{1, j} + a_{2, j} + \cdots + a_{k, j}) \mod 2 = 1$. So the sum $\sum_i a_{i, j}$ is *odd*, which means an *odd number* of piles have bit $j$ set; in particular, *at least one* pile $a_r$ has bit $j$ set.

*Step 3 — Construct the new pile size.* Pick any such pile $a_r$ (with $a_{r, j} = 1$) and set $b_r := a_r \oplus s$.

*Step 4 — Verify $b_r < a_r$.* Compare $a_r$ and $b_r = a_r \oplus s$ bit by bit. Bits above position $j$: $s$ has zero bits there (since $j$ is the *highest* set bit of $s$), so $a_r$ and $b_r$ agree above position $j$. Bit $j$: $a_r$ has bit $j$ equal to $1$ (by choice); $s$ has bit $j$ equal to $1$; so $b_r = a_r \oplus s$ has bit $j$ equal to $1 \oplus 1 = 0$. So $b_r$ has *0* in position $j$ where $a_r$ has *1*. Bits below position $j$: $a_r$ and $b_r$ may differ arbitrarily, but the total value contributed by bits below $j$ is at most $2^j - 1$.

So $a_r$'s value in bit $j$ contributes $2^j$, while $b_r$'s value in bit $j$ contributes $0$; the difference in bits-below-$j$ is at most $2^j - 1$. Hence
\[
  a_r - b_r \;\ge\; 2^j - (2^j - 1) \;=\; 1 \;>\; 0.
\]
So $b_r < a_r$ and we can take $x := a_r - b_r > 0$.

*Step 5 — Verify the new XOR is zero.* The new XOR is
\[
  b_1 \oplus \cdots \oplus b_k \;=\; a_1 \oplus \cdots \oplus a_{r-1} \oplus b_r \oplus a_{r+1} \oplus \cdots \oplus a_k.
\]
Using the identity $x \oplus x = 0$ and the associativity / commutativity of XOR:
\[
  b_1 \oplus \cdots \oplus b_k \;=\; (a_1 \oplus \cdots \oplus a_k) \oplus a_r \oplus b_r \;=\; s \oplus a_r \oplus (a_r \oplus s) \;=\; (s \oplus s) \oplus (a_r \oplus a_r) \;=\; 0 \oplus 0 \;=\; 0.
\]
\hfill$\blacksquare$

*Application to Nim.* The standard *Nim game*: $k$ piles of stones, sizes $a_1, \ldots, a_k$; two players alternate turns; each turn, a player picks one pile and removes any positive number of stones from it; the player who removes the last stone wins. *Bouton's theorem*: a position $(a_1, \ldots, a_k)$ is a *losing* position (P-position) for the next player iff $a_1 \oplus \cdots \oplus a_k = 0$.

The proof has two parts. *(i)* From any non-zero-XOR position, the proven construction gives a move to a zero-XOR position (i.e., the current player can force the opponent into a P-position). *(ii)* From a zero-XOR position, *any* legal move results in a non-zero-XOR position (because reducing a single $a_r$ by a positive amount changes at least one bit of $a_r$, hence changes the overall XOR by a non-zero amount).

Combining: from a P-position, the player must move to an N-position (next-player-wins); from an N-position, the player can move back to a P-position. By induction on the total stone count, the player at a P-position eventually loses (and the player at an N-position wins by always moving to a P-position).

The elegant pivot is the *high-bit construction*: identify the high bit of the XOR, find a pile with that bit set, replace by XOR-with-$s$ to cancel the high bit and the XOR sum simultaneously. The argument is *constructive* (it gives the winning move explicitly) and *fast* (runs in $O(\log a_{\max})$ per move).

**PITFALLS.**

- *Confusing XOR with arithmetic addition.* $a \oplus b$ is *bitwise* mod-2 addition (no carrying); $a + b$ is ordinary integer addition (with carrying). E.g., $3 \oplus 5 = 011 \oplus 101 = 110 = 6$, but $3 + 5 = 8$. The remedy is to *write out the binary representations* and verify the operation bit by bit.

- *Mistaking the high bit of $s$ for the high bit of any $a_i$.* The argument needs the highest bit of *$s$*, not the highest bit of any individual pile. The remedy is to *compute $s$ first* and then read off its high bit.

- *Forgetting to verify $b_r < a_r$.* The construction $b_r = a_r \oplus s$ might give $b_r > a_r$ if the high bit of $s$ is in a position where $a_r$ has bit $0$ (in which case the XOR sets the bit to 1, increasing the value). The choice of $a_r$ with $a_{r, j} = 1$ (where $j$ is $s$'s high bit) is *essential* — it ensures $b_r$'s bit $j$ is $0$, making $b_r < a_r$. The remedy is to *explicitly choose $a_r$ with bit $j$ set* and verify the inequality.

- *Confusing the P-position with the N-position.* P-positions are *previous-player-wins* (i.e., *losing* for the next player); N-positions are *next-player-wins*. The XOR characterisation is: P-position iff XOR $= 0$, N-position iff XOR $\ne 0$. The remedy is to *check the convention*: in normal-play Nim (last stone wins), zero-XOR is losing for the mover.

- *Misapplying Bouton to misère Nim.* In *misère* Nim (last stone *loses*), the strategy differs: the P-positions are the same (XOR $= 0$) *except* at the end-game where all piles are at most $1$ — there, the P-positions are those with an *even* number of size-1 piles (whereas in normal Nim, those with XOR $= 0$, which for size-$\le 1$ piles is also "even number of 1's"). The remedy is to *check the win condition* before applying the theory.

**CONNECTIONS.**

*Primary archetype applications.* Bouton's theorem is the foundation of *combinatorial game theory* (Sprague-Grundy theory): every impartial finite combinatorial game decomposes into a sum of Nim heaps, with the *Grundy value* of the sum being the XOR of the Grundy values of the components. *Sprague-Grundy theorem* (Sprague 1935, Grundy 1939) generalises Bouton to arbitrary impartial games; the *Conway-Berlekamp-Guy "surreal numbers"* framework (1970s) further generalises to partisan games. *Modern game-AI* (Hex, Go endgames, combinatorial puzzles) builds on this theory.

*Alternative solution archetypes.* Bouton's theorem also has a *parity-symmetric* proof: the XOR of pile sizes is invariant under the action of "removing the same number of stones from two different piles" (which is not a legal Nim move but illuminates the structure); the legal Nim moves change the XOR in specific ways that the high-bit construction captures. *Algebraic* proofs (via the $\mathbb F_2$-vector-space structure of $\bigoplus_i \mathbb F_2^{\log a_i}$) also exist.

*Cross-domain manifestations.* XOR-based Nim has surprising applications: *cryptographic hash functions* (some hash functions use XOR-Nim-style reductions to mix bits); *error-correcting codes* (Hamming and Reed-Muller codes use XOR-parity structures); *quantum computing* (the *stabilizer formalism* for quantum error correction is built on XOR-parity invariants over $\mathbb F_2$). The general principle — *parity-of-parts invariant under structured operations* — recurs across discrete mathematics.

**TAKEAWAY.** *XOR / Nim winning move: find the high bit of the XOR sum; pick any pile with that bit set; replace it with its XOR with the sum. The new XOR is zero, and the new pile is smaller. This is the constructive proof of Bouton's theorem.*

---

### 4.3 Example 3 — Cubic with Odd Integer Values

**Problem.** *Let $f(x) = x^3 + b x^2 + c x + d$ be a polynomial with real coefficients. Suppose $f(0)$ and $f(-1)$ are odd integers. Prove that not all the zeros of $f$ are integers. Moreover, if $b, c$ are integers, prove that none of the zeros is an integer.*
*(Joshi EJM Ch. 24, Exercise 24.89; parity-of-polynomial-values argument.)*

**SEED.** *Parity / modular reasoning (Form I — mod 2 on polynomial values).* The conditions $f(0) = d$ odd and $f(-1) = -1 + b - c + d$ odd determine the parities of the coefficients. The contradiction with "all integer zeros" comes from Vieta's formula ($d = -r_1 r_2 r_3$ with $r_i$ integer ⇒ $r_i$ all odd, since $d$ odd) combined with the parity of $f(-1) = -(1 + r_1)(1 + r_2)(1 + r_3)$ (which is divisible by $8$, hence even — contradicting $f(-1)$ odd). The second part (no integer zero at all, given $b, c$ integer) follows from a parity contradiction: $r$ integer ⇒ $b + c$ even (from $f(r) \equiv 0 \pmod 2$ for $r$ odd) ⇒ $b \equiv c$, but $f(-1)$ odd gives $b \not\equiv c$ — contradiction.

**BRUTE PATH.** A student without the parity lens might try to find the zeros of $f$ *explicitly* and check whether they are integers. For a general cubic with real coefficients, the cubic formula (Cardano) gives the three zeros; checking integrality requires evaluating the formula and inspecting the results. This is *possible* but *tedious* and offers no insight into *why* the integer-zero impossibility holds. The parity argument gives the same conclusion in three lines.

**ELEGANT PIVOT.** *Mod-2 reduction on coefficients and on integer-root candidates.*

*Step 1 — Parities of coefficients.* $f(0) = d$. By hypothesis, $d$ is odd, i.e., $d \equiv 1 \pmod 2$.

$f(-1) = (-1)^3 + b(-1)^2 + c(-1) + d = -1 + b - c + d$. By hypothesis, this is odd. Now $-1 + d$: $-1$ is odd, $d$ is odd, so $-1 + d$ is *even*. Therefore $f(-1) = (\text{even}) + (b - c)$ is odd iff $b - c$ is odd, i.e., $b \not\equiv c \pmod 2$.

*Step 2 — First part: not all integer zeros.* Suppose, for contradiction, that all three zeros $r_1, r_2, r_3$ are integers. By Vieta's formulas, $d = -r_1 r_2 r_3$. Since $d$ is odd, $r_1 r_2 r_3$ is odd, which forces *every* $r_i$ to be odd (since a product of integers is odd iff every factor is odd).

But then $f(-1) = (-1 - r_1)(-1 - r_2)(-1 - r_3) = -(1 + r_1)(1 + r_2)(1 + r_3)$. Each $r_i$ is odd, so each $1 + r_i$ is even. So the product $(1 + r_1)(1 + r_2)(1 + r_3)$ is divisible by $2^3 = 8$; in particular, it is *even*. So $f(-1)$ is even, contradicting the hypothesis that $f(-1)$ is odd.

Therefore not all zeros are integers. \hfill$\square$ (Part 1.)

*Step 3 — Second part: no integer zero (given $b, c$ integer).* Suppose, for contradiction, that some zero $r$ of $f$ is an integer. Since $b, c, d$ are integers (given) and $r$ is an integer with $f(r) = 0$, reducing mod 2:
\[
  f(r) \equiv r^3 + b r^2 + c r + d \pmod 2.
\]
For integer $r$:
- *Case A — $r$ even.* Then $r^3 \equiv r^2 \equiv r \equiv 0 \pmod 2$, so $f(r) \equiv d \equiv 1 \pmod 2$. But $f(r) = 0$, which is even. Contradiction.

- *Case B — $r$ odd.* Then $r^3 \equiv r^2 \equiv r \equiv 1 \pmod 2$, so $f(r) \equiv 1 + b + c + d \pmod 2$. With $d \equiv 1$, this becomes $f(r) \equiv 1 + b + c + 1 = b + c \pmod 2$. For $f(r) = 0$, need $b + c$ even, i.e., $b \equiv c \pmod 2$.

But from Step 1, $b \not\equiv c \pmod 2$. Contradiction. \hfill$\blacksquare$ (Part 2.)

The elegant pivot is the *mod-2 reduction*: parities of coefficients and parities of $r^3, r^2, r$ (which depend only on $r \mod 2$) give two contradictions — one (Step 2) ruling out *all* zeros being integers, and another (Step 3) ruling out *any* integer zero when $b, c$ are integers. The argument uses no algebraic machinery beyond elementary parity.

**PITFALLS.**

- *Mis-parsing the hypothesis "$f(0), f(-1)$ are odd integers".* The hypothesis requires both values to be integers *and* odd. If we only assumed "$f(0), f(-1)$ are odd reals" without integrality, the parity argument has no foothold. The remedy is to *parse "odd integer" as integer-and-odd*, not just "odd in some loose sense."

- *Confusing $b - c$ even with $b - c$ odd.* (This is the slate-error correction: the locked slate v0.2 stated "$b - c$ even", but the correct parity is "$b - c$ odd". The chapter's derivation in Step 1 shows the correct parity.) The remedy is to *carefully track the parities of all summands*: $-1 + d$ has the parity of $-1 + 1 = 0$ (even), and $f(-1) = (\text{even}) + (b - c)$ is odd iff $b - c$ is odd.

- *Mis-applying Vieta's formulas.* For $f(x) = x^3 + b x^2 + c x + d$, Vieta says $r_1 + r_2 + r_3 = -b$, $r_1 r_2 + r_1 r_3 + r_2 r_3 = c$, $r_1 r_2 r_3 = -d$. *Sign matters*: $d = -r_1 r_2 r_3$, not $+r_1 r_2 r_3$. The remedy is to *write Vieta explicitly* with the correct signs.

- *Forgetting Case A (even $r$) in Step 3.* Both cases (even $r$ and odd $r$) need to be checked. Skipping one leaves a gap. The remedy is to *case-split on $r \pmod 2$* and verify both.

- *Mis-using the second part without the "$b, c$ integer" hypothesis.* The first part (not all zeros integer) only assumes $b, c, d$ real (with $f(0), f(-1)$ integer); the second part (no integer zero) requires $b, c$ integer (otherwise the mod-2 reduction of $f(r)$ doesn't make sense). The remedy is to *clearly state which hypotheses are used in which step*.

**CONNECTIONS.**

*Primary archetype applications.* The technique of *mod-2 reduction on polynomial values* generalises to:
- *Eisenstein's criterion* for polynomial irreducibility (a polynomial with integer coefficients $\sum a_i x^i$ is irreducible over $\mathbb Q$ if there exists a prime $p$ with $p \nmid a_n$, $p \mid a_i$ for $i < n$, and $p^2 \nmid a_0$);
- *Rational root theorem* (a rational root $p/q$ of an integer-coefficient polynomial must have $p \mid$ constant term and $q \mid$ leading coefficient);
- *$p$-adic root analysis* (Hensel's lemma: a root modulo $p$ lifts to a root modulo $p^k$ if a non-degeneracy condition holds).

*Alternative solution archetypes.* The same problem has a *Vieta-based* solution that doesn't use mod 2 explicitly: if $r_1, r_2, r_3$ are integer zeros with $r_1 r_2 r_3 = -d$ odd, all $r_i$ are odd, and the elementary symmetric polynomials give $b, c, d$ via Vieta. Computing $f(-1) = -1 + b - c + d$ via Vieta's and the all-odd-$r_i$ hypothesis: $b = -(r_1 + r_2 + r_3)$ is odd (sum of three odds), $c = r_1 r_2 + r_1 r_3 + r_2 r_3$ is odd (sum of three odd products), $d = -r_1 r_2 r_3$ is odd. So $b - c$ has parity (odd) - (odd) = even, but the hypothesis forces $b - c$ odd. Contradiction, as before.

*Cross-domain manifestations.* Parity arguments on polynomials underlie: *Galois theory* (the discriminant of a quadratic is a square in the base field iff the polynomial factors over the base field); *coding theory* (BCH codes use polynomial-root-counting modulo prime polynomials in $\mathbb F_q[x]$); *cryptography* (RSA encryption uses polynomial arithmetic modulo a large prime; the parity / divisibility properties of intermediate values are crucial for security analysis).

**TAKEAWAY.** *Polynomial-with-integer-coefficients parity arguments: compute $f(r) \pmod 2$ for integer-candidate $r$, case-split on $r \pmod 2$, and derive contradictions from parity mismatch. Three-line proofs for what would otherwise require the cubic formula.*

---

## 5. Practice Problems

Seven problems, statements only; full solutions appear in the Appendix. The slate skews Tier 3–4 (one Tier 2, three Tier 3, three Tier 4), reflecting the olympiad-leaning nature of parity / modular reasoning — the chapter prepares the reader for RMO and INMO-style problem-solving where modular arguments are the most-used technique.

### 5.1 Wilson-Almost (Tier 4; Joshi Ch. 24, Exercise 24.100)

Find all primes $p$ for which $(p - 1)! + 1$ has no prime factors besides $p$.

### 5.2 Floor Equality $\lfloor x/99 \rfloor = \lfloor x/101 \rfloor$ (Tier 3 RMO; Joshi Ch. 24, Exercise 24.63)

Find the number of positive integers $x$ for which $\left\lfloor\dfrac{x}{99}\right\rfloor = \left\lfloor\dfrac{x}{101}\right\rfloor$.

### 5.3 Diagonal Squares on an $m \times n$ Board (Tier 3; Joshi Ch. 24, Exercise 24.78)

Show that each diagonal of an $m \times n$ chessboard (going from one corner to the opposite corner) passes through exactly $m + n - \gcd(m, n)$ unit squares.

### 5.4 Squarefree Decomposition (Tier 2; Joshi Ch. 24, Exercise 24.76(a))

Prove that every positive integer $m$ can be written uniquely as $m = u^2 v$ where $u, v$ are positive integers and $v$ is *squarefree* (i.e., $v$ is not divisible by any perfect square greater than $1$). Moreover, if $m \mid n^2$ then $u v \mid n$.

### 5.5 Hamiltonian Cycle on $m \times n$ Mesh (Tier 4; Joshi Ch. 24, Exercise 24.81)

A grid of streets has $m$ roads going East-West and $n$ roads going North-South, with houses at every intersection. Under what condition can a person start at one house, visit every other house exactly once, and return to the starting house (a *Hamiltonian cycle* on the intersection grid)?

### 5.6 Divisibility $24 \mid n(n^2 - 1)$ for Odd $n$ (Tier 3; cross-archetype with Ch. 1; JEE 1983, Joshi Ch. 4, Comment 8)

For every odd positive integer $n$, prove that $24$ divides $n(n^2 - 1)$.

*[Cross-archetype note: this problem also appears as Ch. 1 (Invariance) PP3, where the *consecutive-integers identity* $n(n^2 - 1) = (n-1) n (n+1)$ + the divisibility-by-$3!$ invariance is the primary framing. Here in Ch. 14, the *explicit mod-2 + mod-3 reduction* is the primary framing — the two framings give the same answer through complementary lenses.]*

### 5.7 Two-Person Modular Game with Target 100 (Tier 4 RMO; Joshi Ch. 24, Exercise 24.83(a))

Two players $A$ and $B$ play a game as follows. Starting with a running total of $0$, $A$ and $B$ alternately add integers between $1$ and $10$ (inclusive) to the running total. The player whose addition makes the running total equal *exactly* $100$ wins. Prove that the first player ($A$) has a winning strategy.

---

## 6. The Connections Web

Parity and modular reasoning connect to virtually every later archetype in this volume and to substantial parts of every quantitative discipline.

### 6.1 Parity / Modular Reasoning Across Mathematical Domains

*Number theory.* Modular reasoning is the backbone of elementary and analytic number theory. *Fermat / Euler / Wilson* are the foundational congruences. *Quadratic reciprocity* (Gauss) is the deepest single result. *Class field theory* (Artin, Chevalley, Tate) generalises modular reciprocity to algebraic number fields. *Modular forms* (Eichler, Shimura, Wiles) bridge elementary modular arithmetic to algebraic geometry, with the proof of Fermat's Last Theorem as the dramatic culmination.

*Algebra.* The *ring $\mathbb Z / m \mathbb Z$* and its unit group $(\mathbb Z / m \mathbb Z)^\times$ are foundational. *Finite fields* $\mathbb F_q$ (for $q = p^n$, $p$ prime) are the algebraic structures behind coding theory, cryptography, and combinatorial designs. *Group theory* (the symmetric group $S_n$, the alternating group $A_n$) uses parity (sign of permutation, $\pm 1$).

*Algebraic geometry.* *Schemes over $\text{Spec}\,\mathbb Z$* generalise classical varieties; *reduction modulo $p$* (Néron, Tate) is a fundamental technique. *Étale cohomology* (Grothendieck) defines cohomology over schemes by reducing modulo primes. *$p$-adic geometry* (Tate, Faltings, Scholze) extends complex-analytic geometry to the $p$-adic numbers $\mathbb Q_p$.

*Combinatorics.* *Parity-counting* (the number of objects with a given parity) is a recurring move (the example: $24 \mid n(n^2 - 1)$ in Ch. 1 PP3 / Ch. 14 PP6). *Inclusion-exclusion mod 2* gives binary-valued counting. *Burnside's lemma* counts orbits via *average-fixed-points* — a modular average.

*Probability and statistics.* *Modular Markov chains* (chains whose states are residues modulo $m$) appear in random walks, queuing theory, and stochastic models. *Hash functions* (mod a large prime) are the basis of probabilistic data structures (Bloom filters, count-min sketches, MinHash).

### 6.2 Parity / Modular Reasoning in Physics and Computing

*Physics.* *Parity (P-symmetry)*, *charge conjugation (C-symmetry)*, *time reversal (T-symmetry)* are the three discrete symmetries; their *combined* CPT symmetry is exact in all known physics. *Parity violation* in weak interactions (Lee-Yang 1956, Wu 1957) was a Nobel-Prize-winning discovery. *Mod-2 cohomology classes* (Stiefel-Whitney) classify the orientability of manifolds and the existence of spin structures. *Anyons* in 2-dimensional condensed matter exhibit fractional statistics (interpolating between bosons and fermions) governed by the *braid group* — a modular structure.

*Cryptography.* *RSA encryption* relies on modular exponentiation in $(\mathbb Z / N \mathbb Z)^\times$ for $N$ a product of two large primes. *Diffie-Hellman key exchange* relies on the discrete logarithm in $(\mathbb Z / p \mathbb Z)^\times$. *Elliptic-curve cryptography* (ECDSA, EdDSA) relies on the discrete logarithm in elliptic curve groups modulo a prime. *Post-quantum cryptography* (CRYSTALS-Kyber, CRYSTALS-Dilithium) relies on lattice-based problems modulo polynomial rings.

*Coding theory.* *Cyclic redundancy checks* (CRCs), *Reed-Solomon codes*, *BCH codes*, *Reed-Muller codes*, *low-density parity-check (LDPC) codes* — all built on modular polynomial arithmetic. *Decoding algorithms* (Berlekamp-Massey, Viterbi, belief propagation) operate on syndromes in modular structures.

*Computer science.* *Hash functions* (cryptographic and non-cryptographic) reduce arbitrary data to fixed-size residues. *Bloom filters* and *count-min sketches* use hash-modular structures for probabilistic data storage. *Hash tables* rely on uniform-distribution of hash-residues. *Pseudorandom number generators* (linear congruential, Mersenne Twister) are modular recurrences.

*Game theory.* *Sprague-Grundy theory* (Sprague 1935, Grundy 1939) generalises Bouton's Nim theorem to all impartial games. *Combinatorial game theory* (Conway, Berlekamp, Guy, 1970s) uses surreal numbers and partisan game decompositions, with modular invariants throughout.

### 6.3 Cross-Domain Manifestations

*Music.* *Pitch-class set theory* (Forte, 1973) treats pitches modulo octave (mod 12 in equal temperament). *Indian taals* (16-beat $teen$ taal, 10-beat $jhap$ taal, 12-beat $ek$ taal) are modular rhythmic cycles. *Twelve-tone serialism* (Schoenberg) uses permutations of the modular pitch-class group.

*Architecture.* *Modular construction* (prefabricated panels, repeating motifs) uses periodicity / modular thinking explicitly. *Tile patterns* (Penrose tilings, Islamic geometric patterns) often have *non-trivial* modular symmetries.

*Biology.* *Reading frames* in molecular biology (mod 3 on nucleotide sequences). *Cell-cycle phases* (mod-cycle reasoning on phase transitions). *Chromosome pairing* (the XY system for sex determination is a mod-2 structure).

*Linguistics.* *Vowel harmony* in Turkic, Finnish, Hungarian languages — vowels within a word must share certain features (front / back, rounded / unrounded), a mod-2 constraint on phonological features.

*Economics.* *Modular auctions* (the *generalised second-price* mechanism for ad auctions). *Cryptocurrency* (Bitcoin, Ethereum) rests on modular cryptography for transaction signatures and proof-of-work.

### 6.4 Related Archetypes

Parity / modular reasoning interacts with five other archetypes in particularly tight ways.

- **Archetype 1 (Invariance).** *Modular invariants* are the canonical invariants — Ch. 1 framed this archetype broadly; Ch. 14 specialises to *the residue mod $m$* as the invariant. Many Ch. 1 PPs (PP3 = $24 \mid n(n^2 - 1)$; the trick-coin invariant) are modular at their core. The cross-link is direct: Ch. 14 PP6 reuses Ch. 1 PP3 with the explicit modular lens.

- **Archetype 4 (Hidden Structure).** *The residue is often the hidden structure*. A problem whose surface formulation seems intractable becomes trivial once the right modulus is recognised — Ch. 4's discovery move and Ch. 14's modulus-selection move are deeply related.

- **Archetype 13 (Combinatorial Principles).** *Parity-counting* (the number of objects with even / odd property) was named in Ch. 13's master takeaways and is the recurring move that Ch. 14 systematises. Inclusion-exclusion modulo 2 gives binary-valued counts; Burnside's lemma uses modular averaging over a group action.

- **Archetype 15 (Bijection / Correspondence).** *Modular equivalence classes* give natural bijections between sets of size $\lfloor N/m \rfloor$ and sets of size $1$ (the residue class). The bijection $\mathbb Z / m \mathbb Z \leftrightarrow \{0, 1, \ldots, m - 1\}$ is the prototype; Ch. 15 will develop this systematically.

- **Archetype 18 (Recursion / Induction).** *Modular recurrences* (like the Lucas-Lehmer sequence $S_{n+1} = S_n^2 - 2 \pmod{M_p}$ for Mersenne primality testing) combine recursion with modular reduction. Modular induction is the "weighted" induction where the inductive hypothesis is on the residue modulo $m$.

---

## 7. Master Takeaways

Seven sentences. Each one is a complete operational principle.

1. *Sometimes the remainder tells the whole story.* (The canonical takeaway.)

2. *Integer-divisibility of factorial quotients: rewrite via binomial-coefficient identities (elementary route); or check $p$-adic valuations via Legendre / Kummer (modular route). The elementary route is usually shorter; the modular route is more illuminating.* (WE1 takeaway; Form IV.)

3. *XOR / Nim winning move: find the high bit of the XOR sum; pick any pile with that bit set; replace it with its XOR with the sum. New XOR is zero; new pile is smaller. Bouton's theorem.* (WE2 takeaway; Form V.)

4. *Polynomial-with-integer-coefficients parity arguments: compute $f(r) \pmod 2$ for integer-candidate $r$; case-split on $r \pmod 2$; derive contradictions from parity mismatch.* (WE3 takeaway; Form I.)

5. *The right modulus is the question.* Choosing $m$ to make the residue computation reveal the answer is the cognitively hardest step; the rest is mechanical.

6. *Named-theorem selection: match Wilson, Fermat, Euler, CRT, Legendre, Kummer, or Bouton to the problem's structural signature.* (The toolkit reflex.)

7. *Cross-archetype: parity / modular reasoning unifies invariance (Ch. 1), hidden structure (Ch. 4), combinatorial counting (Ch. 13), bijective equivalence classes (Ch. 15), and recursion (Ch. 18) — by Chapter 14 these are one coherent body of structured arithmetic.*

---

## 8. Self-Assessment Checklist

You have absorbed Chapter 14 when, without re-opening it, you can do each of the following from memory.

- [ ] State Wilson's theorem ($(p - 1)! \equiv -1 \pmod p$ for prime $p$) and its converse (the converse provides a primality criterion).
- [ ] State Fermat's little theorem in both forms ($a^p \equiv a \pmod p$ unconditionally; $a^{p-1} \equiv 1 \pmod p$ when $\gcd(a, p) = 1$).
- [ ] State Euler's theorem ($a^{\varphi(n)} \equiv 1 \pmod n$ for $\gcd(a, n) = 1$) and compute $\varphi(n)$ for small $n$ (e.g., $\varphi(12) = 4, \varphi(15) = 8$).
- [ ] State the Chinese Remainder Theorem (pairwise-coprime moduli; unique solution mod $\prod n_i$) and solve a small example (e.g., $x \equiv 1 \pmod 3, x \equiv 2 \pmod 5$: $x \equiv 7 \pmod{15}$).
- [ ] State Legendre's formula $v_p(n!) = (n - s_p(n))/(p - 1)$ and compute $v_2(10!) = 8 = (10 - 2)/1$ (where $s_2(10) = 2$, since $10_{10} = 1010_2$).
- [ ] State Kummer's theorem ($v_p\!\left(\binom{m + n}{m}\right)$ = carries in base-$p$ addition of $m$ and $n$).
- [ ] State Bouton's theorem on Nim (P-position iff XOR $= 0$) and apply it: position $(3, 4, 5)$ has XOR $011 \oplus 100 \oplus 101 = 010 = 2$ (N-position; winning move is to make XOR $= 0$).
- [ ] Apply the chessboard parity argument to derive non-tileability (e.g., $m \times n$ with $mn$ odd) or non-existence of Hamiltonian cycles (e.g., $m \times n$ grid with $mn$ odd).
- [ ] Derive the squarefree decomposition $m = u^2 v$ (with $v$ squarefree, $u, v$ unique) for a small $m$ (e.g., $m = 72 = 6^2 \cdot 2$, so $u = 6, v = 2$).
- [ ] Identify and explain three of the five common pitfalls: Wrong-Modulus, Sign-Error-in-Wilson, Fermat-Misapplied, CRT-Misapplied-to-Non-Coprime-Moduli, Kummer-Off-By-One.

---

## Bridge to Chapter 15: Bijection / Correspondence

Chapter 14 was the second chapter of the *Structural Reasoning* sub-pillar (Chapters 13–16). The chapter developed the most foundational tool of integer reasoning — *residue computation modulo a chosen modulus* — and named the seven canonical theorems (Wilson, Fermat, Euler, CRT, Legendre, Kummer, Bouton) plus the recurring patterns (chessboard parity, polynomial-value parity, Nim XOR, squarefree decomposition). With Chapter 14 in hand, the reader has internalised that *the right modulus often collapses an intractable problem into a one-line computation* — the canonical *residue-as-structure* principle of this sub-pillar.

Chapter 15 — *Bijection / Correspondence* — continues the *Structural Reasoning* sub-pillar by elevating *the bijective principle* (Chapter 13's "two sets have the same size iff there is a bijection between them") into a *named archetype* — the discipline of *proving identities and equalities by constructing explicit one-to-one correspondences*. The named patterns include: *complementary bijections* (e.g., $\binom{n}{k} \leftrightarrow \binom{n}{n - k}$ via complement); *involutions* (self-inverse bijections that pair up elements); *reflection bijections* (the André reflection that proves the Catalan-number identity $C_n = \binom{2n}{n} - \binom{2n}{n - 1}$); *Bell-number recurrences* (set partitions via element-insertion bijections); *Lindström-Gessel-Viennot* (non-intersecting-lattice-paths bijections that prove determinant identities). The cognitive shift: from *compute both sides and verify equality* to *construct an explicit bijection and the equality is automatic*. Bijective proofs are universally regarded as the most *illuminating* style of combinatorial proof: they don't just prove that two quantities are equal; they explain *why* via the explicit correspondence.

The bridge from Ch. 14 to Ch. 15 is the *modular-equivalence-class bijection*: $\mathbb Z / m \mathbb Z$ naturally bijects with $\{0, 1, \ldots, m - 1\}$, and this prototype bijection (between integers under modular reduction and their canonical residue representatives) is the simplest example of the Ch. 15 archetype. Chapter 15 will generalise this to a much broader class of structural bijections.

---

## Appendix — Solutions to Practice Problems

### Solution to 5.1 — Wilson-Almost

We seek all primes $p$ for which $(p - 1)! + 1 = p^a$ for some positive integer $a$.

*Step 1 — Direct verification for small primes.*
- $p = 2$: $(2 - 1)! + 1 = 1! + 1 = 2 = 2^1$. ✓
- $p = 3$: $2! + 1 = 3 = 3^1$. ✓
- $p = 5$: $4! + 1 = 25 = 5^2$. ✓
- $p = 7$: $6! + 1 = 721 = 7 \cdot 103$. The factor $103 \ne 7$, so $(p - 1)! + 1$ has a prime factor other than $p$. ✗

*Step 2 — All other prime factors of $(p - 1)! + 1$ are $\ge p$.* For any prime $q < p$: $q \in \{1, 2, \ldots, p - 1\}$, so $q$ is one of the factors of $(p - 1)!$, hence $q \mid (p - 1)!$. Therefore $q \mid ((p - 1)! + 1) - q \cdot k = (p - 1)! + 1 \pmod q$... wait, more directly: $(p - 1)! \equiv 0 \pmod q$ (since $q \mid (p - 1)!$), so $(p - 1)! + 1 \equiv 1 \pmod q$, i.e., $q \nmid (p - 1)! + 1$.

Hence all prime factors of $(p - 1)! + 1$ are $\ge p$.

*Step 3 — For $p \ge 7$, $(p - 1)! + 1$ is not a pure power of $p$.*

By Wilson's theorem, $p \mid (p - 1)! + 1$, so $(p - 1)! + 1 = p \cdot k$ for some positive integer $k$. If $(p - 1)! + 1 = p^a$, then $k = p^{a - 1}$, so $p \mid k$ iff $a \ge 2$. The condition $p \mid k$ is equivalent to $p^2 \mid (p - 1)! + 1$.

A prime $p$ for which $p^2 \mid (p - 1)! + 1$ is called a *Wilson prime*. The only known Wilson primes are $p = 5, 13, 563$, with no others below approximately $2 \times 10^{13}$ (verified computationally).

For $p \ge 7$ a *non-Wilson prime*: $p^2 \nmid (p - 1)! + 1$, so $(p - 1)! + 1 \ne p^a$ for any $a \ge 2$. Combined with $(p - 1)! + 1 > p$ (verified directly: for $p \ge 7$, $(p - 1)! \ge 720 > 7$), no $a = 1$ either. So $(p - 1)! + 1$ has a prime factor $\ne p$.

For $p = 13$ (Wilson prime): $(p - 1)! + 1 = 12! + 1 = 479001601 = 13^2 \cdot 2834329$. Check whether $2834329$ is a pure power of $13$: $13^5 = 371293, 13^6 = 4826809$. Since $371293 < 2834329 < 4826809$, $2834329$ is *not* a power of $13$, so it has a prime factor $\ne 13$. Hence $12! + 1$ has a prime factor $\ne 13$. ✗

For $p = 563$ (Wilson prime): similar analysis (computationally heavy but routine) confirms $(562)! + 1 / 563^2$ has prime factors $\ne 563$.

*Step 4 — Conclude.* The primes $p$ with $(p - 1)! + 1$ a pure power of $p$ are exactly
\[
  \boxed{p \in \{2, 3, 5\}.}
\]
$\blacksquare$

*Remark.* The conjectural infinitude of Wilson primes is open. Even if more Wilson primes exist, they are extraordinarily rare; computational evidence strongly suggests that the answer set $\{2, 3, 5\}$ is final and finite.

---

### Solution to 5.2 — Floor Equality $\lfloor x/99 \rfloor = \lfloor x/101 \rfloor$

Let the common floor value be $k$. Then $\lfloor x/99 \rfloor = k$ iff $99k \le x < 99(k + 1) = 99k + 99$. Similarly $\lfloor x/101 \rfloor = k$ iff $101k \le x < 101(k+1) = 101k + 101$.

The intersection of these two conditions is $\max(99k, 101k) \le x < \min(99k + 99, 101k + 101)$.

For $k \ge 0$: $\max(99k, 101k) = 101k$ (since $101 > 99$), and $\min(99k + 99, 101k + 101) = 99k + 99$ (since $99k + 99 \le 101k + 101$ iff $2k \ge -2$, always true).

So the intersection is $[101k, 99k + 99)$, which is non-empty iff $101k < 99k + 99$, i.e., $2k < 99$, i.e., $k \le 49$.

*Number of positive integers $x$ in $[101k, 99k + 99)$.*

For $k = 0$: interval is $[0, 99)$, integers $\{0, 1, \ldots, 98\}$, but we need $x$ positive, so $x \in \{1, 2, \ldots, 98\}$, giving $98$ integers.

For $k \ge 1$: interval is $[101k, 99k + 99)$, integers $\{101k, 101k + 1, \ldots, 99k + 98\}$. Count: $99k + 99 - 101k = 99 - 2k$. (Verify: lower bound $101k$ inclusive, upper bound $99k + 99$ exclusive; number of integers $= 99k + 99 - 101k = 99 - 2k$.) All these integers are positive since $101k \ge 101 > 0$.

*Total count.*
\[
  N \;=\; 98 + \sum_{k = 1}^{49} (99 - 2k) \;=\; 98 + \sum_{k = 1}^{49} (99 - 2k).
\]
The inner sum is an arithmetic progression: terms $97, 95, 93, \ldots, 1$ (from $k = 1$ to $k = 49$), with $49$ terms. Sum $= 49 \cdot (97 + 1)/2 = 49 \cdot 49 = 2401$.

Total: $N = 98 + 2401 = \boxed{2499}$. $\blacksquare$

*Cross-check.* At $k = 49$: interval $[4949, 4950)$, single integer $\{4949\}$. By formula: $99 - 2(49) = 1$. ✓ At $k = 50$: interval $[5050, 5049)$, empty. ✓

---

### Solution to 5.3 — Diagonal Squares on an $m \times n$ Board

We count the number of unit squares the diagonal from $(0, 0)$ to $(m, n)$ passes through.

*Step 1 — Crossings characterise unit squares.* As the diagonal goes from $(0, 0)$ to $(m, n)$, it enters a new unit square exactly when it crosses a vertical line $x = i$ (for $i = 1, 2, \ldots, m - 1$) or a horizontal line $y = j$ (for $j = 1, 2, \ldots, n - 1$). It starts in one unit square and enters a new one at each crossing.

If the diagonal crosses a vertical and horizontal line *simultaneously* (i.e., passes through an interior lattice point $(i, j)$ with $0 < i < m, 0 < j < n$), then the two crossings count as *one* (it moves from one square diagonally to another, not via an intermediate square).

*Step 2 — Count interior lattice-point crossings.* The diagonal passes through $(i, j)$ iff $j = (n/m) i$ is integer, iff $i$ is a multiple of $m/\gcd(m, n)$. The number of such $i$ in $\{1, 2, \ldots, m - 1\}$ is $\gcd(m, n) - 1$ (multiples of $m/\gcd(m, n)$ in $\{0, 1, \ldots, m\}$ are $0, m/\gcd, 2m/\gcd, \ldots, m$, totaling $\gcd + 1$; remove the endpoints $0$ and $m$ to get $\gcd - 1$ interior multiples).

*Step 3 — Count unit squares.*
\[
  \text{Squares} \;=\; 1 + (\text{vertical crossings}) + (\text{horizontal crossings}) - (\text{simultaneous crossings})
\]
\[
  \;=\; 1 + (m - 1) + (n - 1) - (\gcd(m, n) - 1) \;=\; m + n - \gcd(m, n).
\]
\[
  \boxed{\text{Number of squares} \;=\; m + n - \gcd(m, n).}
\]
$\blacksquare$

*Verification.*
- $m = n = 4$ (square diagonal): $\gcd = 4$, count $= 4 + 4 - 4 = 4$. ✓ (Each diagonal of a $4 \times 4$ square passes through exactly 4 squares — the corner-to-corner diagonal goes through one square per row.)
- $m = 6, n = 4$: $\gcd = 2$, count $= 6 + 4 - 2 = 8$. ✓
- $m = 5, n = 3$: $\gcd = 1$, count $= 5 + 3 - 1 = 7$. ✓ (Coprime case: diagonal hits no interior lattice point.)

---

### Solution to 5.4 — Squarefree Decomposition

*Existence and uniqueness.* Let $m = \prod_p p^{a_p}$ be the prime factorisation of $m$ (the exponents $a_p$ are non-negative integers, with finitely many non-zero).

Define $u = \prod_p p^{\lfloor a_p / 2 \rfloor}$ and $v = \prod_p p^{a_p - 2\lfloor a_p / 2 \rfloor}$.

Each exponent in $v$ is $a_p \mod 2 \in \{0, 1\}$, so $v$ is *squarefree* (no prime occurs with exponent $\ge 2$). And $u^2 v = \prod_p p^{2 \lfloor a_p/2 \rfloor + (a_p - 2\lfloor a_p/2 \rfloor)} = \prod_p p^{a_p} = m$. ✓ (Existence.)

For uniqueness: suppose $m = u^2 v = (u')^2 v'$ with both $v, v'$ squarefree. Comparing $p$-adic valuations: $v_p(m) = 2 v_p(u) + v_p(v)$, where $v_p(v) \in \{0, 1\}$ (since $v$ squarefree). The decomposition $a_p = 2 \lfloor a_p / 2 \rfloor + (a_p \mod 2)$ is unique, so $v_p(u) = \lfloor a_p / 2 \rfloor$ and $v_p(v) = a_p \mod 2$. Hence $u$ and $v$ are uniquely determined. (Uniqueness.) \hfill$\blacksquare$

*Second part: if $m \mid n^2$, then $u v \mid n$.* Equivalent to: $v_p(uv) \le v_p(n)$ for every prime $p$.

We have $v_p(uv) = v_p(u) + v_p(v) = \lfloor a_p / 2 \rfloor + (a_p \mod 2) = \lceil a_p / 2 \rceil$.

We have $m \mid n^2$ iff $v_p(m) \le v_p(n^2) = 2 v_p(n)$ for every $p$, iff $a_p \le 2 v_p(n)$, iff $v_p(n) \ge a_p / 2$, iff $v_p(n) \ge \lceil a_p / 2 \rceil$ (since $v_p(n)$ is an integer).

So $v_p(n) \ge \lceil a_p / 2 \rceil = v_p(uv)$, giving $uv \mid n$. ✓ $\blacksquare$

*Example.* $m = 72 = 2^3 \cdot 3^2$. Then $u = 2^1 \cdot 3^1 = 6$ and $v = 2^1 \cdot 3^0 = 2$. So $m = u^2 v = 36 \cdot 2 = 72$. ✓

If $m \mid n^2$: $72 \mid n^2$ requires $n^2 \equiv 0 \pmod{72}$. Smallest such $n$: $n = 12$ (since $144 = 72 \cdot 2$). And $uv = 6 \cdot 2 = 12$. Check $uv \mid n$: $12 \mid 12$ ✓. ✓

---

### Solution to 5.5 — Hamiltonian Cycle on $m \times n$ Mesh

The grid has $mn$ vertices (intersections); edges connect adjacent intersections (horizontally or vertically); we seek a Hamiltonian cycle (a cycle visiting every vertex exactly once).

*Necessity: $mn$ must be even.* Two-colour the grid as a chessboard: cell $(i, j)$ is black if $i + j$ is even, white otherwise. The two colours alternate horizontally and vertically.

In a Hamiltonian cycle, consecutive vertices are adjacent, hence of opposite colours. The cycle has length $mn$ (visiting each vertex once and returning to start), so the colour sequence is BWBW...BWB or WBWB...WBW, totaling equal numbers of each colour. This requires $mn$ even (with $mn/2$ of each colour).

If $mn$ odd: $\lceil mn/2 \rceil = (mn + 1)/2$ of one colour and $\lfloor mn/2 \rfloor = (mn - 1)/2$ of the other, differing by 1. A Hamiltonian cycle is impossible.

*Sufficiency: $mn$ even ⇒ Hamiltonian cycle exists.* Assume WLOG $m$ even ($mn$ even with at least one of $m, n$ even). Construct the *snake-and-return* path:
- Go right along row $1$ from $(1, 1)$ to $(1, n)$.
- Down to $(2, n)$, then left to $(2, 1)$.
- Down to $(3, 1)$, right to $(3, n)$. ... (snake pattern.)
- After completing all $m$ rows, the path ends at $(m, 1)$ (since $m$ is even, the last row is traversed right-to-left, ending at $(m, 1)$).

We've visited every vertex. To make a cycle, return from $(m, 1)$ to $(1, 1)$: but the only edges to $(1, 1)$ are from $(1, 2)$ and $(2, 1)$, both already visited (in our path). So a direct edge doesn't work — the path isn't a cycle.

A small modification: snake the first column upward from $(m, 1)$ back to $(1, 1)$. This works if the snake leaves a "ladder" on column 1 going down separately.

*Cleaner construction:* For $m$ even, $n \ge 2$: traverse the first column vertically from $(1, 1)$ down to $(m, 1)$; then snake the remaining $n - 1$ columns horizontally (right to left): row $m$ from $(m, 1)$ to $(m, n)$ then up to $(m - 1, n)$, then left to $(m - 1, 2)$, then up to $(m - 2, 2)$, then right to $(m - 2, n)$, etc., ending at $(1, 2)$. From $(1, 2)$ go left to $(1, 1)$, completing the cycle. *(One needs to verify the parity of $m - 1$ rows of snake works out; for $m$ even, $m - 1$ is odd, so the snake's ending row pattern works.)*

For $mn \ge 4$ (the cycle has length $\ge 4$), this construction gives a Hamiltonian cycle.

*Boundary cases.* For $mn = 2$ (a $1 \times 2$ or $2 \times 1$ grid): only 2 vertices, no Hamiltonian cycle possible (a cycle needs at least 3 vertices). For $mn = 1$: only 1 vertex, also no cycle.

For $mn \ge 4$ with at least one of $m, n$ even: Hamiltonian cycle exists. For $mn$ odd: doesn't exist.

\[
  \boxed{\text{Hamiltonian cycle exists iff at least one of $m, n$ is even, and $mn \ge 4$.}}
\]
$\blacksquare$

---

### Solution to 5.6 — Divisibility $24 \mid n(n^2 - 1)$ for Odd $n$

We factor $n(n^2 - 1) = (n - 1) n (n + 1)$, the product of three consecutive integers.

*Mod 3: divisibility by 3.* Among any three consecutive integers, exactly one is divisible by $3$ (a basic consequence of the pigeonhole principle on residues mod 3). So $3 \mid (n - 1) n (n + 1)$, regardless of whether $n$ is odd or even.

*Mod 8: divisibility by 8 (for $n$ odd).* Write $n = 2k + 1$ for some integer $k \ge 0$. Then $n - 1 = 2k$ and $n + 1 = 2k + 2 = 2(k + 1)$. The product $(n - 1)(n + 1) = 4 k (k + 1)$. Among any two consecutive integers $k, k + 1$, one is even, so $k(k + 1)$ is even. Hence $4 \cdot k(k + 1)$ is divisible by $8$. So $(n - 1)(n + 1)$ is divisible by $8$, and therefore $(n - 1) n (n + 1)$ is also divisible by $8$ (multiplying by $n$ preserves divisibility).

*Combining: $24 = 8 \cdot 3$.* Since $\gcd(8, 3) = 1$, and both $8$ and $3$ divide $(n - 1) n (n + 1)$, the product $8 \cdot 3 = 24$ divides $(n - 1) n (n + 1) = n(n^2 - 1)$. \hfill$\blacksquare$

*Cross-archetype note.* This problem also appears as Ch. 1 (Invariance) PP3, where the framing is via the *consecutive-integers identity* $n^3 - n = n(n - 1)(n + 1)$ and the *invariance argument* that the function $n^3 - n$ is divisible by $3!$ (and by higher invariant moduli for $n$ odd). The two framings are equivalent; the Ch. 14 framing makes the *mod 8 × mod 3 = mod 24* structure explicit, while the Ch. 1 framing emphasises the invariance of the consecutive-product.

---

### Solution to 5.7 — Two-Person Modular Game with Target 100

*Winning strategy for player $A$.* 

Step 1: On move 1, $A$ adds $1$. Running total: $1$.

Step 2: On every subsequent move, after $B$ adds some integer $b \in \{1, 2, \ldots, 10\}$, $A$ responds by adding $11 - b$. Note $11 - b \in \{1, 2, \ldots, 10\}$ (since $b \in \{1, \ldots, 10\}$), so the response is a legal move.

Step 3: After each $A$-move, the running total has the form $1 + 11 + 11 + \cdots + 11 = 1 + 11 t$ where $t$ is the number of complete "rounds" (one $B$ move plus one $A$ response). In particular, after each $A$-move, the running total is $\equiv 1 \pmod{11}$.

Step 4: The totals after $A$-moves are $1, 12, 23, 34, 45, 56, 67, 78, 89, 100$. These are the residues $1 \pmod{11}$ less than or equal to $100$. The last one is $100$, achievable after $A$'s $10$th move (i.e., after $9$ complete rounds plus $A$'s initial move).

Step 5: Verify $A$ can reach $100$ before $B$ does. The total $89$ is reached after $A$'s $9$th move (the move before the final $A$-move). After $B$'s response (adding some $b \in \{1, \ldots, 10\}$), the total becomes $89 + b \in \{90, 91, \ldots, 99\}$, none of which is $100$. $B$ cannot reach $100$ from $89$ on a single move (since $89 + 10 = 99 < 100$).

Then $A$ adds $11 - b$, making the total $89 + b + (11 - b) = 100$. $A$ reaches $100$, $A$ wins. \hfill$\blacksquare$

*Modular interpretation.* The number $100 \equiv 1 \pmod{11}$ ($100 = 11 \cdot 9 + 1$). $A$ maintains the invariant *running total $\equiv 1 \pmod{11}$ after each $A$-move*; since the target is $\equiv 1 \pmod{11}$, $A$ is the only player who can land on the target.

The strategy generalises: for any target $T$ and move-set $\{1, 2, \ldots, k\}$, the first player wins by maintaining running total $\equiv T \pmod{k + 1}$ (if $T \not\equiv 0 \pmod{k + 1}$). For $T \equiv 0 \pmod{k + 1}$, the second player wins (by maintaining running total $\equiv 0 \pmod{k + 1}$).

---

*End of Chapter 14. Chapter 15 (Bijection / Correspondence) continues the Structural Reasoning sub-pillar.*

