# Cursor-Engel.md — Consolidated Memory of Arthur Engel's *Problem-Solving Strategies*

*Persistent reference file. Built so that future sessions need not re-read the full 400-page Engel PDF. When working on Pillar 3 of the Advaitian Book (Multidirectional Solving), this file is the **primary lookup**; the raw text `my_references/problem-solving-strategies.txt` is the **secondary verification source**.*

**Book metadata.**
- Title: *Problem-Solving Strategies*
- Author: Arthur Engel (1928–2022)
- Publisher: Springer-Verlag, *Problem Books in Mathematics* series (eds. K. Bencsáth, P.R. Halmos), 1998
- Length: ~400 pages (preface + 14 chapters + references + index)
- Chapters: 14, each named after a meta-strategy / technique
- Source files: `my_references/Problem Solving Strategies.pdf` (canonical, 2.5 MB), `my_references/problem-solving-strategies.txt` (searchable extraction via `pdftotext -layout`, 21,005 lines, 214,447 words)
- Text-file line ranges: main book lines 325–~19,700; references ~20,800; index ~20,900+

**Voice/pedagogy signature.** Engel writes in a **terse, German-rigorous, encyclopedic** register that is the polar opposite of Joshi's discursive Indian-academic style. Each chapter opens with 1–2 pages of conceptual exposition (the principle stated), follows with a numbered sequence of **worked examples** (E1, E2, ..., usually 8–15 per chapter), then a **Problems** section (usually 30–50 problems per chapter), then a **Solutions** section at the end of each chapter (numbered identically). Engel does not waste words: a 4-line solution to an IMO problem is typical. He cites competition sources aggressively — IMO, Putnam, USAMO, BMO (Bundeswettbewerb Mathematik), ARO (Allrussian Mathematical Olympiad), AUO (Austrian Olympiad), TT (Tournament of Towns), and many others.

**Critical difference from Joshi.** Joshi is organised by *math topic* (algebra, geometry, calculus, ...); Engel is organised by *meta-strategy* (invariance, coloring, extremal, ...). **This makes Engel's chapter structure nearly isomorphic to the Pillar 2 archetype catalogue** — and uniquely valuable for Pillar 3 because every Engel chapter contains explicit *multi-archetype* problems (problems that combine the chapter's primary technique with one or two others). This file's §V (Multi-Archetype Convergence Index) is specifically curated for Pillar 3 case-study mining.

**Version.** 1.0 — May 28 2026 (initial consolidated extraction — all 14 chapters surveyed; Pillar 3 multi-archetype goldmine populated).
**Maintenance rule.** Each time a Pillar 3 chapter is drafted, refresh that chapter's row of §V (Multi-Archetype Convergence Index) below with any new problems pulled.
**Status.** Comprehensive baseline. All 14 chapters surveyed for technique-content, competition-source breakdown, archetype-mapping, and notable named results. The §V multi-archetype index is the **primary lookup for Pillar 3 case-study selection**.

---

## I. Chapter-by-Chapter Index

| # | Title | Pages | Text-file lines | Pillar 2 primary archetype | Pillar 2 secondary archetypes | Pillar 3 weight |
|---|---|---|---|---|---|---|
| 1 | The Invariance Principle | 1–24 | 325–1457 | #1 Invariance | #14 Parity/Modularity, #12 Extremal (monovariants) | **HIGH** — Ch. 1 model example (5-digit divisibility) lives here |
| 2 | Coloring Proofs | 25–38 | 1458–2043 | #14 Parity/Modularity | #13 Combinatorial, #2 Symmetry | **HIGH** — many 2-archetype problems (coloring × extremal, coloring × counting) |
| 3 | The Extremal Principle | 39–58 | 2044–2991 | #12 Extremal Principles | #11 Existence, #13 Combinatorial | **HIGH** — Sylvester-Gallai theorem and many 2-archetype classics |
| 4 | The Box Principle | 59–84 | 2992–4212 | #13 Combinatorial (pigeonhole) | #12 Extremal, #14 Parity | **HIGHEST** — the Pillar 3 Ch. 1 worked example #2 (5 points in unit square) lives here |
| 5 | Enumerative Combinatorics | 85–116 | 4213–5963 | #13 Combinatorial Principles | #15 Bijection, #18 Recursion/Induction | MED — the IMO 1977 p+q sums problem |
| 6 | Number Theory | 117–160 | 5964–8077 | #14 Parity/Modularity | #1 Invariance (Fermat little theorem), #4 Hidden Structure (Lucas/Wilson) | MED |
| 7 | Inequalities | 161–204 | 8078–10785 | #10 Inequality Constraints | #12 Extremal, #2 Symmetry, #5 Substitution | MED — Nesbitt's inequality with four proofs is a multi-archetype showcase |
| 8 | The Induction Principle | 205–220 | 10786–11640 | #18 Recursion/Induction | #12 Extremal (well-ordering), #1 Invariance | **HIGHEST** — **IMO 1988 Problem 6 (Vieta jumping) is here** — the canonical 3-archetype problem for Pillar 3 Ch. 3 |
| 9 | Sequences | 221–244 | 11641–12870 | #18 Recursion/Induction | #5 Substitution (characteristic eqs), #11 Existence (limits), #1 Invariance | MED |
| 10 | Polynomials | 245–270 | 12871–14128 | #4 Hidden Structure | #5 Substitution (Tschirnhaus), #1 Invariance (Vieta), #2 Symmetry | MED |
| 11 | Functional Equations | 271–288 | 14129–15009 | #5 Substitution | #11 Existence/Uniqueness, #18 Induction, #1 Invariance | **HIGH** — the §7.9 case-study #5 (Engel Ch. 11 functional equation) lives here |
| 12 | Geometry | 289–360 | 15010–19070 | #2 Symmetry, #8 Domain Translation | #1 Invariance, #5 Substitution, #3 Duality | MED-HIGH — largest chapter (72 pp.), many 2- and 3-archetype problems |
| 13 | Games | 361–372 | 19071–19582 | #12 Extremal (P-positions vs N-positions) | #18 Recursion (game tree), #16 Reverse Engineering | LOW-MED — useful for Ch. 7 (Escape-Hatch) illustrations |
| 14 | Further Strategies | 373–396 | 19583–~20800 | #16 Reverse Engineering (infinite descent) | #18 Induction (descent), #20 Analogy | **HIGH** — explicit "further strategies" chapter = meta-archetype manual |

---

## II. Chapter Details

### Chapter 1: The Invariance Principle (pp. 1–24; lines 325–1457)

**Topic summary.** The chapter teaches: when faced with a transformation process or an algorithm, *find a quantity that does not change*. The invariant is the diagnostic tool that proves termination, impossibility, or conservation. Engel distinguishes **invariants** (truly unchanging) from **semi-invariants / monovariants** (monotonically changing — useful for termination proofs via well-ordering).

**Key principles/theorems established.**
- Invariants in number-theoretic transformations (parity, mod-$n$ residue, GCD).
- Distance-from-origin as a Euclidean invariant (E5).
- Sum-of-squares as an invariant under cyclic transformations.
- Monovariant arguments (E4 — Parliament of Sikinia: enemies-in-own-house count strictly decreases).
- Termination by well-ordering: a monovariant on $\mathbb{N}$ must stabilise.
- The "smallest-counterexample" form of invariance (closely related to infinite descent, Ch. 14).

**Worked examples (E1–E13+).**
- *E1.* Arithmetic-harmonic mean iteration $x_0=a, y_0=b$ with $x_{n+1}=(x_n+y_n)/2, y_{n+1}=2x_n y_n/(x_n+y_n)$. Invariant: $x_n y_n = ab$. Common limit $\sqrt{ab}$.
- *E2.* (Odd $n$.) Numbers $1,\ldots,2n$ on blackboard; replace $a,b$ with $|a-b|$. Show odd number remains. **Invariant:** parity of $\sum a_i$.
- *E3.* Six circular sectors with numbers $1,0,1,0,0,0$; you may add 1 to two adjacent. Can you equalise? **Invariant:** $a_1-a_2+a_3-a_4+a_5-a_6$ is constant.
- *E4.* Sikinian Parliament: each member ≤ 3 enemies; partition into two houses such that each has ≤ 1 enemy in own house. **Monovariant:** total enemies-in-own-house strictly decreases per swap.
- *E5.* $(a,b,c,d) \to (a-b, b-c, c-d, d-a)$. Show some component → ∞. **Invariant:** sum $=0$; **monovariant:** sum-of-squares doubles every 2 steps.
- *E6.* AM-GM iteration with arccos invariant. (A very hard problem solved via invariant.)
- *E7.* Sum-of-products $S = a_1 a_2 a_3 a_4 + a_2 a_3 a_4 a_5 + \cdots = 0$, prove $4 | n$. **Invariant mod 4** under sign-flips.
- *E8–E13.* Variations: ambassador-handshake parity, chessboard moves, semi-invariant termination.

**Notable problems in exercise set (51+ problems).**
- *Problems 6, 7, 8 (chips of three colors)*: invariant mod 3 on color counts.
- *Problem 13 (8×8 chessboard with integers)*: invariant under row/column negations.
- *Problem 49 (signs ± on blackboard)*: parity invariant.
- *Problem 51 (heads parity mod 3)*: explicitly noted in solutions.
- Many problems involve termination arguments via monovariants.

**Competition sources cited.** Mostly Eastern European olympiads — MMO (Moscow), HMO (Hungarian), Tournament of Towns, plus some IMO problems.

**Pillar 3 multi-archetype gold.** Engel's E4 (Parliament of Sikinia) is a 2-archetype problem combining **#1 Invariance + #12 Extremal** (monovariant termination via well-ordering on $\mathbb{N}$).

---

### Chapter 2: Coloring Proofs (pp. 25–38; lines 1458–2043)

**Topic summary.** Coloring is a *generalised parity argument*. The chapter teaches: when a tiling, packing, or graph-coverage problem is asked, *color the underlying structure cleverly* so that certain tile/piece types are forced to cover specific color-counts. The contradiction (between forced color-counts and the actual color totals) proves impossibility.

**Key principles/theorems established.**
- Standard chessboard 2-coloring: pure parity.
- 4-coloring (diagonal stripes 0–1–2–3): used for straight-tetromino impossibility.
- The T-tetromino covers 1 black + 3 white (or 3 black + 1 white) on a standard chessboard.
- 6-coloring of a $6\times 6$ cube: for $1\times 1 \times 4$ brick packing.
- The 5×5 square with a single $-1$ and 24 $+1$s under $a \times a$ sign-flips ($a > 1$): solvable iff $-1$ at center.

**Worked examples / problems (38 problems).**
- *Problem 1.* $2\times 2$ and $1 \times 4$ tiles can't be exchanged on a floor. (Color: 2x2 blocks; 1×4 covers 0 or 2 black, 2×2 covers exactly 1.)
- *Problem 3.* 25 T-tetrominoes cannot cover $10\times 10$ (since 25 is odd; T-tetromino covers 1 + 3 of each color, requires equal numbers of each kind).
- *Problem 5.* 25 straight tetrominoes cannot cover $10\times 10$ (4-coloring with 26 squares of one color).
- *Problem 12.* $9 \times 9$ beetle problem (each diagonal move) — minimum free squares.
- *Problem 13.* Plane points colored R/B: monochromatic rectangle exists.
- *Problem 14.* Space points R/B: square with 3 red OR 4 blue vertices.
- *Problem 25.* **Art Gallery Problem** — minimum number of watchmen for simple $n$-gon (classical: $\lfloor n/3 \rfloor$).
- *Problem 31.* Three pucks A, B, C in a plane (hockey player hits puck through other two); after 1001 hits, can all return to original spots? **Parity / color invariant.**
- *Problem 32.* $23 \times 23$ square tiled by $1\times 1, 2\times 2, 3\times 3$ tiles — minimum number of $1\times 1$ tiles needed (AUO 1989).
- *Problem 34.* No closed knight's tour on $4 \times n$ board (coloring argument).
- *Problem 35.* Plane 2-colored: 3 monochromatic points forming equilateral triangle.

**Competition sources.** AUO (Austrian Olympiad) 1989 is explicitly cited (problem 32).

**Pillar 3 multi-archetype gold.** Coloring + extremal is a recurring pair (e.g., minimal number of monochromatic tiles needed, problem 32). Coloring + counting (e.g., problem 3: 25 odd × 3-1 imbalance). Many problems here are 2-archetype.

---

### Chapter 3: The Extremal Principle (pp. 39–58; lines 2044–2991)

**Topic summary.** "Choose the *extreme* (max, min, leftmost, deepest, longest) element." The chapter teaches: when a structure is finite or well-ordered, choose its extreme element and exploit the *maximality / minimality* property to derive a contradiction or close the proof.

**Key principles/theorems established.**
- Finite set has max and min.
- Well-ordering principle for $\mathbb{N}$.
- "Deepest point" lemma: in a finite arrangement, the extreme element has a special property.
- Sylvester-Gallai theorem (1893/1933 Gallai/Kelly): A finite set of points in the plane such that any line through two passes through a third must be collinear. (Kelly's 1948 4-line extremal proof.)
- The "minimum total length" argument for non-intersecting roads / matchings.

**Worked examples (E1–E10+).**
- *E1.* Number of plane regions cut by $n$ lines via extremal-point bijection: $p_n = \binom{n}{0} + \binom{n}{1} + \binom{n}{2}$.
- *E2.* HMO 1973: among $s_n$ space parts from $n$ planes, at least $(2n-3)/4$ tetrahedra.
- *E3.* $n$ points in plane, every triangle has area $\le 1$; show all points lie in a triangle of area $\le 4$ (the "wide triangle" extremal).
- *E4.* 2n points = n farms + n wells; show wells can be assigned bijectively to farms with no intersecting road segments (extremal: minimum total length matching has no crossings).
- *E5.* Plane point set $\Sigma$ where each point is the midpoint of two others is infinite. (Two proofs: extremal-distance and extremal-leftmost-then-lowest.)
- *E6.* Convex pentagon: 3 diagonals form a triangle. (Extremal: longest diagonal.)
- *E7.* Tetrahedron: 3 concurrent edges form a triangle. (Extremal: longest edge.)
- *E8.* Lattice-point labels by positive integers, each = mean of 4 neighbors → all equal. (Extremal: smallest label.)
- *E9.* No $(x,y,z,u) \in \mathbb{Z}_+^4$ with $x^2 + y^2 = 3(z^2 + u^2)$. (Infinite descent via extremal $x^2+y^2$.)
- *E10.* **Sylvester problem** (Kelly's proof): finite set of plane points with the "every line through 2 passes through 3" property must be collinear. **Famous 4-line extremal argument.**

**Notable problems in exercise set (many).** Geometric, combinatorial, and number-theoretic; all use extremal-element exploitation.

**Competition sources.** HMO 1973 explicitly. Many problems are uncredited classics.

**Pillar 3 multi-archetype gold.**
- **Sylvester-Gallai (E10)** is the canonical 2-archetype example: **#12 Extremal + #2 Symmetry** (the symmetry of the "every-line-through-two-passes-through-three" condition).
- E4 (farms/wells matching) is **#12 Extremal + #15 Bijection**: extremal minimum-length matching, with the bijection existing as a side-condition.
- E9 (Diophantine descent) is **#12 Extremal + #18 Induction** (infinite descent = induction in reverse).

---

### Chapter 4: The Box Principle (pp. 59–84; lines 2992–4212)

**Topic summary.** Pigeonhole. "If $n+1$ objects are placed in $n$ boxes, at least one box has $\ge 2$ objects." The chapter pushes the principle to Ramsey-type and number-theoretic generalisations: the chessmaster's tournament, Erdős-Szekeres, sum-free sets, Schur's theorem.

**Key principles/theorems established.**
- Basic pigeonhole: $n+1 \to n$ boxes ⇒ ≥ 2 in one box.
- Generalised pigeonhole: $qs+1$ pearls in $s$ boxes ⇒ one box has $> q$ pearls.
- Erdős-Szekeres (1935): every sequence of $n \ge (p-1)(q-1)+1$ integers contains a monotone-increasing subsequence of length $p$ or monotone-decreasing subsequence of length $q$.
- Ramsey number $R(3,3) = 6$ (the "6 friends/strangers" classical problem, Putnam 1953).
- Schur's theorem (1916) on sum-free sets.
- The "parity-pattern of lattice-point coordinates" pigeonhole (E7).
- Pigeonhole on consecutive partial sums for divisibility by $n$.

**Worked examples (E1–E15+).**
- *E1.* $n$ persons in a room; two with same number of acquaintances. (Boxes 0–$(n-1)$; boxes 0 and $n-1$ cannot both be occupied.)
- *E2.* Chessmaster's 77-day prep: must have a sequence of days with exactly 21 games. (Apply to $a_1, \ldots, a_{77}, a_1+21, \ldots, a_{77}+21$.)
- *E3.* Any $n$ integers have a subset whose sum is divisible by $n$. (Partial sums mod $n$.)
- *E4.* $n+1$ numbers from $\{1, \ldots, 2n\}$: one divides another. (Boxes = odd parts.)
- *E5.* $a, b$ coprime ⇒ $ax - by = 1$ has solution. (Pigeonhole on $a, 2a, \ldots, (b-1)a$ mod $b$.)
- *E6.* Erdős-Szekeres.
- *E7.* 5 lattice points in plane: midpoint of some pair is a lattice point. **(Pigeonhole on parity patterns ee, eo, oe, oo.)**
- *E8.* Mod-10 Fibonacci sequence is purely periodic.
- *E9.* For any $n$, some Fibonacci number ends in $n$ zeros.
- *E10.* For $a$ coprime to 10: some power of $a$ ends in $000\ldots 01$.
- *E11.* 9 rugs of area 1 in a room of area 5 ⇒ two rugs overlap by $\ge 1/9$.
- *E12–E15.* **Ramsey numbers**: $R(3,3) = 6$ (Putnam 1953); 17-scientists problem (3-colors, monochromatic triangle); $R(3,3,3) \le 17$; IMO 1978 (sum-free sets).

**Competition sources.** Putnam 1953 (Greenwood–Gleason 1947 generalisation), IMO 1978, Kürschák Competition 1947.

**Pillar 3 multi-archetype gold (HIGHEST).**
- **E7 lattice-point midpoints** is the perfect **#13 Combinatorial + #14 Parity** 2-archetype problem — already in our Pillar 2 Ch. 17 PP1, can be re-used as Pillar 3 worked example.
- **E12 (6 friends/strangers)** combines **#13 Combinatorial + #2 Symmetry** (the Ramsey-graph symmetry).
- **IMO 1978 (E15)** is a 3-archetype problem: **#13 Combinatorial + #14 Parity + #2 Symmetry** — a candidate for Pillar 3 Ch. 3 worked example.

---

### Chapter 5: Enumerative Combinatorics (pp. 85–116; lines 4213–5963)

**Topic summary.** Counting techniques organised by the "Divide and Conquer" paradigm: sum rule, product rule, bijection counting, double counting, recursion, sieving (inclusion-exclusion), generating functions.

**Key principles/theorems established.**
- Sum, product, recursion, and bijection rules (Engel's basic four).
- $\binom{n}{k}$ formula with two derivations (direct vs. bijection).
- The Möbius / inclusion-exclusion formula.
- Catalan numbers and their bijective interpretations.
- Generating functions for partition / composition problems.

**Worked examples (E1–E15+).**
- *E1.* **IMO 1977**: real-number sequence where every 7-sum $< 0$ and every 11-sum $> 0$; show max length $\le 16$. Constructive example: $5, 5, -13, 5, 5, 5, -13, 5, 5, -13, 5, 5, 5, -13, 5, 5$. **A classical multi-archetype problem.**
- *E2.* Generalisation: $p, q$ coprime ⇒ max length $\le p+q-2$ (John Rickard, GB).
- *E4.* $\gcd(p,q) = d$ case: max length $\le p+q-d-1$.
- *E5.* Multiplicative version: every $p$-product $< 1$, every $q$-product $> 1$ ⇒ same bound via logarithms.
- *E8.* $2n$ tennis players, first-round pairings $P_n = (2n-1)!! = (2n)!/(2^n n!)$. **Three solutions** via recursion + ordering elimination.
- More worked examples on Catalan numbers, generating functions, bijection counting.

**Competition sources.** IMO 1977 (the 7/11-sums problem), MMO 1969 (the original source — Engel notes this was a known problem before the IMO).

**Pillar 3 multi-archetype gold.**
- **IMO 1977 (E1)** combines **#13 Combinatorial + #14 Parity (sum-sign argument)**. Multi-archetype, 2-archetype.
- The tennis-tournament problem (E8) — **#13 Combinatorial + #18 Recursion + #15 Bijection** — is a 3-archetype problem when treated via multiple solutions.

---

### Chapter 6: Number Theory (pp. 117–160; lines 5964–8077)

**Topic summary.** Comprehensive NT toolkit: gcd / lcm, Euclidean algorithm, Fermat's Little Theorem, Wilson's theorem, Euler's $\varphi$, congruences, integer-part function, divisibility tricks ($a^n - b^n$ factorization), Diophantine equations.

**Key principles/theorems established.**
- $\gcd(a,b) = ax + by$ (Bezout's identity).
- Euclidean algorithm.
- Fundamental Theorem of Arithmetic.
- Fermat's Little Theorem **with three proofs** (induction, congruences, combinatorial via necklace counting).
- Fermat-Euler theorem: $a^{\varphi(m)} \equiv 1 \pmod m$ for $\gcd(a,m) = 1$.
- $341 = 11 \cdot 31$ as smallest pseudoprime counterexample to FLT-converse.
- Integer-part identities: $\lfloor x/n \rfloor = \lfloor \lfloor x \rfloor / n \rfloor$, etc.
- $a-b | a^n - b^n$ for all $n$; $a+b | a^n + b^n$ for odd $n$.

**Worked examples and problems.** Many classical NT problems from IMO, Putnam, Eastern-European olympiads. Examples on Diophantine equations, divisibility tricks, modular arithmetic.

**Competition sources.** Heavy use of IMO, Putnam, and Eastern European olympiad problems.

**Pillar 3 multi-archetype gold.**
- Fermat's Little Theorem (with three proofs) is itself a 3-archetype illustration: **#18 Induction + #1 Invariance (congruences) + #13 Combinatorial (necklace argument)** — perfect Pillar 3 demonstration of how the *same theorem* admits multiple multi-archetype proofs.
- Many Diophantine problems combine **#14 Parity/Modularity + #4 Hidden Structure + #16 Reverse Engineering** (infinite descent).

---

### Chapter 7: Inequalities (pp. 161–204; lines 8078–10785)

**Topic summary.** Comprehensive inequalities toolkit: HM-GM-AM-QM (basic four-means), Cauchy-Schwarz, Jensen, power mean, rearrangement, Chebyshev's sum inequality, and many olympiad inequalities including Nesbitt's.

**Key principles/theorems established.**
- HM-GM-AM-QM chain.
- AM-GM for $n$ variables.
- Cauchy-Schwarz in various forms.
- Jensen's inequality for convex functions.
- The "factorization" $a^3 + b^3 + c^3 - 3abc = (a+b+c)(a^2+b^2+c^2-ab-bc-ca)$.
- Schur's inequality, Schur-like factorizations.
- Nesbitt's inequality $\frac{a}{b+c} + \frac{b}{a+c} + \frac{c}{a+b} \ge 3/2$ — **with FOUR proofs**.

**Worked examples (E1–E7+).**
- *E1–E6.* Standard manipulation inequalities, "complete the square", squaring shortcuts.
- *E5.* $a^2 + b^2 + c^2 \ge ab + bc + ca$ — **four proofs** (algebraic, two-by-two AM-GM, extremal-order, homogenisation).
- *E7.* Nesbitt's inequality — **four proofs**: substitution, AM-HM, $f(a,b,c)$ structure, Cauchy-Schwarz / Engel form. (Note: "Engel form" of Cauchy-Schwarz: $\sum \frac{x_i^2}{y_i} \ge \frac{(\sum x_i)^2}{\sum y_i}$ — sometimes credited to Engel, sometimes called the "Cauchy-Schwarz in Engel form".)

**Pillar 3 multi-archetype gold.**
- The "same inequality with multiple proofs" structure of E5, E7 is *itself* a Pillar 3 multidirectional demonstration: each proof represents a different archetype-pair convergence. E.g., Nesbitt's proof 1 = **#5 Substitution + #10 Inequality**; proof 2 = **#10 Inequality + #2 Symmetry (AM-HM)**; proof 3 = **#7 Normalisation + #2 Symmetry**; proof 4 = **#5 Substitution + #10 Inequality (Cauchy-Schwarz)**. Excellent illustration for Pillar 3 Ch. 5 (MVC).

---

### Chapter 8: The Induction Principle (pp. 205–220; lines 10786–11640)

**Topic summary.** Mathematical induction in all its forms: weak, strong, double, well-ordering equivalent. The chapter starts with extensive Fibonacci identity-proving (15 identities!) before moving to harder applications.

**Key principles/theorems established.**
- Standard PMI; equivalence to well-ordering.
- 15 Fibonacci identities (the chapter's opening drill): $F_{n-1} F_{n+1} = F_n^2 + (-1)^n$ (the "Cassini identity"), $\sum F_i$ identities, $\gcd(F_m, F_n) = F_{\gcd(m,n)}$, etc.
- The golden ratio $t$ as the positive root of $t^2 = t + 1$, with the continued-fraction representation $1 + 1/(1+1/(1+\ldots))$ and convergents $F_{n+1}/F_n \to t$.

**Worked examples (problems within the chapter).**
- *Problem 1.* $2n$ points + $n^2 + 1$ segments ⇒ triangle exists.
- *Problem 2.* $n$ cars on circular track with just enough total gas for one lap ⇒ some car can complete a lap.
- *Problem 3.* Sikinian roads: every pair connected by one direct one-way road ⇒ some city reachable from all others in ≤ 1 intermediary.
- *Problem 5.* TT 1987: $\sqrt{2\sqrt{3\sqrt{4\sqrt{\ldots\sqrt{(N-1)\sqrt{N}}}}}} < 3$.
- **Problem 6: IMO 1988 Problem 6 (the Vieta-jumping problem).** Show: if $a, b \in \mathbb{Z}_{\ge 0}$ and $(a^2 + b^2)/(ab + 1) \in \mathbb{Z}_{\ge 0}$, then this quotient is a perfect square. **THE CANONICAL 3-ARCHETYPE PROBLEM FOR PILLAR 3 CH. 3.** Solution uses induction on $ab$ + descent + invariance of the quotient.
- *Problem 7.* Exponential tower $\sqrt{2}^{\sqrt{2}^{\ldots}}$ converges to 2.
- *Problems 8–12.* Map coloring (2 colors for circle-arrangement, 4 colors), TT 1989 lattice integer assignment.

**Competition sources.** **IMO 1988 P6** (Vieta jumping), TT 1987 + 1989.

**Pillar 3 multi-archetype gold (HIGHEST).**
- **IMO 1988 P6** is the model 3-archetype problem: **#18 Recursion/Induction + #16 Reverse Engineering (Vieta descent from putative minimum) + #1 Invariance (quotient is preserved)**. **This is locked as Pillar 3 Ch. 3 WE1.**

---

### Chapter 9: Sequences (pp. 221–244; lines 11641–12870)

**Topic summary.** Recurrence relations (linear, second-order, characteristic equations), convergence of recursive sequences, self-similar binary sequences, Fibonacci-related sequences.

**Key principles/theorems established.**
- Linear recurrence with characteristic equation $\lambda^2 + p\lambda + q = 0$ → closed-form $x_n = A\lambda_1^n + B\lambda_2^n$.
- Periodicity of $f(x+1) + f(x-1) = \sqrt 2 f(x)$ (period 8); more generally, periodicity of $f(x+1) + f(x-1) = t f(x)$ when $t = 2\cos(2\pi/n)$.
- Convergence rates of recursive $\sqrt{}$-based sequences (E4: $a_{n+1} = \sqrt{6 + a_n}$ has limit 3 with rate $1/6$).
- The Fibonacci-period in permutations (E5).
- Self-similar binary sequences via substitution rules.

**Worked examples (E1–E6+).**
- *E1.* Linear recurrence $x_{n+1} = 7x_n - 12x_{n-1}$, $x_0 = 2, x_1 = 7$. Characteristic eq $\lambda^2 - 7\lambda + 12 = 0$, roots $3, 4$. Closed form: $x_n = 3^n + 4^n$.
- *E2.* Periodic functional equation $f(x+1) + f(x-1) = \sqrt 2 f(x)$ → period 8.
- *E3.* Generalisation: $t$ = positive root of $t^3 = t^2 + t + 1$; periodicity question.
- *E4.* $a_0 = 0, a_{n+1} = \sqrt{6 + a_n}$: monotone, bounded by 3, limit = 3, convergence rate $1/6$.
- *E5.* Permutations $|p(i) - i| \le 1$: count = Fibonacci $F_{n+1}$. Linear version → circular version with 5 cases.
- *E6.* Self-similar binary sequence: $w_1 = 0, w_2 = 001$, $w_{k+1} = w_k w_k w_{k-1}$. Not periodic; ratio of 0s to 1s converges to $\sqrt 2 + 1$.

**Pillar 3 multi-archetype gold.**
- Sequence problems frequently combine **#18 Recursion + #5 Substitution (characteristic equation) + #11 Existence (limit)** — natural 2- or 3-archetype problems.

---

### Chapter 10: Polynomials (pp. 245–270; lines 12871–14128)

**Topic summary.** Polynomial algebra over $\mathbb{R}$ and $\mathbb{C}$: roots, factorization, Vieta's theorem, multiplicities, Rational Root Theorem, the Fundamental Theorem of Algebra, roots of unity, Cardano's formula for cubics, geometric constructions (regular pentagon) via roots of unity.

**Key principles/theorems established.**
- Division algorithm for polynomials.
- Factor theorem: $f(a) = 0 \iff (x-a) | f(x)$.
- Vieta's theorem for quadratic, cubic, general monic polynomial.
- Rational Root Theorem.
- Fundamental Theorem of Algebra.
- Roots of unity: $x^n - 1 = (x-1)(x-\omega) \cdots (x - \omega^{n-1})$.
- Cardano's formula via $x^3 + a^3 + b^3 - 3abx$ factorisation.
- Regular pentagon construction via 5th roots of unity, $\cos 72° = (\sqrt 5 - 1)/4$.

**Worked examples and notable problems.** Vieta's theorem applications, sum-of-powers-of-roots, polynomial divisibility.

**Pillar 3 multi-archetype gold.**
- Polynomial problems combine **#1 Invariance (Vieta) + #2 Symmetry (symmetric functions of roots) + #4 Hidden Structure (factorisations)** — natural 2- or 3-archetype problems.

---

### Chapter 11: Functional Equations (pp. 271–288; lines 14129–15009)

**Topic summary.** Classical FE: $f(xy) = f(x) + f(y)$ (logarithm); $f(x+y) = f(x) + f(y)$ (Cauchy's equation, including Hamel pathology); $f(x+y) = f(x)f(y)$ (exponential); $f(xy) = f(x)f(y)$ (power); the Jensen equation $f((x+y)/2) = (f(x)+f(y))/2$; the d'Alembert equation $f(x+y) + f(x-y) = 2f(x)f(y)$.

**Key principles/theorems established.**
- Cauchy's equation has Hamel ("wild") solutions in general; "tame" solutions $f(x) = cx$ require regularity (continuity, monotonicity, boundedness on an interval).
- The classical hierarchy: continuity ⇒ measurability ⇒ monotonicity ⇒ boundedness — each forces the tame solution.
- Standard substitution moves: $y=0$, $y=-x$, $y=x$, $y = nx$.
- Periodicity arguments: $f(x+T) = f(x)$ — many FE prove a hidden period.

**Worked examples (E1–E6+).**
- *E1.* $f(xy) = f(x) + f(y)$ ⇒ $f \equiv 0$ if $f(0)$ defined; otherwise $f = c\ln|x|$ if differentiable.
- *E2.* Cauchy $f(x+y) = f(x) + f(y)$: detailed treatment of all four regularity cases (continuity, monotonicity, boundedness, no condition = Hamel).
- *E3.* $f(x+y) = f(x)f(y)$: $f > 0$ everywhere, $f = e^{cx}$ for continuous solutions.
- *E4–E5.* d'Alembert, multiplicative FE.

**Pillar 3 multi-archetype gold.**
- The Engel Ch. 11 functional equation (which §7.9 case study #5 references — "an Engel functional equation requiring substitution + induction + parity") is **#5 Substitution + #18 Induction + #14 Parity** — locked as Pillar 3 Ch. 6 Case Study #5.

---

### Chapter 12: Geometry (pp. 289–360; lines 15010–19070)

**Topic summary.** Engel's largest chapter (72 pages). Vectors, midpoints, half-turns ($H_A$), translations, centroid, parallelograms. Affine combinations. Reflections / rotations. Inversive geometry. Complex numbers as plane geometry. Geometric inequalities. Generalised olympiad geometry.

**Key principles/theorems established.**
- Vector axioms (8 properties of $\mathbb{R}^2$ as vector space).
- Half-turn $H_A : Z \mapsto 2A - Z$; composition $H_A \circ H_B = 2\vec{AB}$.
- Centroid of triangle: $S = (A+B+C)/3$, intersects medians at $2:1$.
- Reconstruction of polygon from midpoints of sides (works for odd $n$, not even).
- Various concurrency and collinearity results.
- Inversive geometry, Apollonius circle.

**Worked examples (E1–E10+ across 72 pages).**
- *E1.* Midpoints of quadrilateral sides form a parallelogram.
- *E2.* Reconstruct pentagon from midpoints; impossible for hexagon.
- *E3.* Hexagon-of-centroids has parallel opposite sides.
- Many subsequent examples on geometric inequalities, transformations, complex-number-as-geometry.

**Pillar 3 multi-archetype gold.**
- Most geometry problems naturally combine **#2 Symmetry + #8 Domain Translation (vector/complex/synthetic) + #1 Invariance (rigid motions)** — natural 2- or 3-archetype problems.

---

### Chapter 13: Games (pp. 361–372; lines 19071–19582)

**Topic summary.** Combinatorial game theory. Bachet's game, Wythoff's game, Nim. Losing positions (P-positions) vs winning positions (N-positions). Pairing strategies. Symmetry strategies. Recursive characterisations.

**Key principles/theorems established.**
- P-positions ("Previous player wins") vs N-positions ("Next player wins").
- Bachet's game: $L = \{0, k+1, 2(k+1), \ldots\}$.
- Wythoff's game with golden-ratio characterisation.
- Pairing-strategy proofs.

**Worked examples and problems.**
- *Warmup 1.* Bachet's game with $M = \{1, \ldots, k\}$: $L$ = multiples of $k+1$.
- *Warmup 2.* $M$ = powers of 2: $L$ = multiples of 3.
- *Warmup 3.* $M$ = $\{1\} \cup$ primes: $L$ = multiples of 4.
- *Problem 1.* Wythoff's game.
- *Problem 2.* 107 chips, moves = $p^n$ (prime powers): find $L$.
- *Problems 5, 6.* Chessboard knight/bishop games.

**Pillar 3 multi-archetype gold.**
- Game problems combine **#12 Extremal (P/N classification) + #18 Induction (game tree) + #16 Reverse Engineering (work backward from terminal positions)** — natural 2- or 3-archetype problems.

---

### Chapter 14: Further Strategies (pp. 373–396; lines 19583–~20800)

**Topic summary.** The "meta-archetype" chapter — synthesises strategies not fitting in previous chapters. Sections include 14.1 (some advanced graph-theory and Ramsey-type problems), **14.2 Infinite Descent** (Fermat's classical method), and other specialised techniques.

**Key principles/theorems established.**
- **Infinite descent** (Fermat 1640): impossibility proofs by showing that any positive-integer solution would yield a smaller one, contradicting well-ordering of $\mathbb{N}$.
- The Pythagoreans' geometric descent: regular pentagram side-ratio $x^2 = x+1$, no rational solution (geometric descent on the inscribed pentagram).
- Lattice-point regular $n$-gon (only $n = 4$ possible; descent for $n \ne 3, 4, 6$).
- Diophantine $x^2 + y^2 + z^2 + u^2 = 2xyzu$: no positive-integer solutions (descent).

**Worked examples (E1–E3+).**
- *E1.* Pentagram side ratio: $x^2 = x + 1$ has no rational solution. **Geometric descent proof.**
- *E2.* No regular lattice $n$-gon for $n \ne 4$.
- *E3.* $x^2 + y^2 + z^2 + u^2 = 2xyzu$ has no positive-integer solutions.

**Pillar 3 multi-archetype gold (HIGH).**
- Infinite descent is the canonical example of **#16 Reverse Engineering + #18 Induction** convergence — it is an inductive argument *in reverse*, working from a putative minimum downward.
- This chapter, being the "meta-archetype" chapter of Engel, is the natural cross-reference target for Pillar 3 Ch. 7 (Escape-Hatch Architecture): "what to do when standard archetypes fail."

---

## III. Master Index by Competition

Engel cites international competitions extensively. The most frequent sources:

| Competition | Approximate citation count | Notable problems |
|---|---|---|
| **IMO** (International Mathematical Olympiad) | 30+ | IMO 1977 (7/11-sums, Ch. 5 E1), **IMO 1988 P6** (Vieta jumping, Ch. 8 Problem 6), IMO 1978 (sum-free sets, Ch. 4 E15), IMO 1992 (9 points, edges colored R/B, Ch. 14 Problem 5) |
| **Putnam** | 10+ | Putnam 1953 (R(3,3)=6, Ch. 4 E12) |
| **TT** (Tournament of Towns) | 15+ | TT 1987 (Ch. 8 Problem 5: $\sqrt{2\sqrt{3\sqrt{\ldots}}} < 3$), TT 1989 (Ch. 8 Problem 12) |
| **MMO** (Moscow Mathematical Olympiad) | 10+ | MMO 1969 (the 7/11-sums origin) |
| **ARO** (Allrussian Mathematical Olympiad) | 8+ | Various |
| **HMO** (Hungarian Mathematical Olympiad) | 5+ | HMO 1973 (Ch. 3 E2) |
| **AUO** (Austrian Mathematical Olympiad) | 4+ | AUO 1989 (Ch. 2 Problem 32), AUO 1992 (Ch. 14 Problem 4) |
| **BWM / BMO** (Bundeswettbewerb Mathematik / British MO) | 5+ | BMO 1987 (Ch. 14 Problem 1) |
| **USAMO** | 5+ | Various |
| **Kürschák** (Hungary) | 3+ | Kürschák 1947 (R(3,3)=6, original) |
| **ATMO, IbMO, ASU, KMO** (various national olympiads) | 5+ each | Various |

**For Pillar 3 case-study mining**: IMO 1988 P6 (Ch. 8) is the highest-priority pull; IMO 1977 (Ch. 5) and IMO 1978 (Ch. 4) are runners-up.

---

## IV. Master Index by Pillar 2 Archetype

For each of the 20 archetypes, the Engel chapters where it lives:

| Archetype | Engel chapters | Strength of fit |
|---|---|---|
| **#1 Invariance** | Ch. 1 (primary), Ch. 6 (Fermat / mod arguments), Ch. 8 (induction-as-invariance) | Primary — Ch. 1 is the textbook treatment |
| **#2 Symmetry** | Ch. 7 (symmetric inequalities), Ch. 10 (Vieta / roots of unity), Ch. 12 (geometric symmetry — primary) | Primary in Ch. 12 |
| **#3 Duality** | Ch. 12 (pole-polar, geometric duality) | Secondary only |
| **#4 Hidden Structure** | Ch. 6 (Wilson, Lucas), Ch. 10 (polynomial factorisations) | Primary in Ch. 10 |
| **#5 Substitution** | Ch. 7 (substitution shortcuts), Ch. 9 (characteristic eqs), Ch. 11 (FE — primary) | Primary in Ch. 11 |
| **#6 Linearization** | Ch. 7 (logarithmic linearisation), Ch. 9 (linear recurrences) | Secondary |
| **#7 Normalisation** | Ch. 7 (inequality homogenisation) | Secondary only |
| **#8 Domain Translation** | Ch. 10 (poly ↔ roots-of-unity), Ch. 12 (vectors ↔ synthetic ↔ complex — primary) | Primary in Ch. 12 |
| **#9 Domain Constraints** | Throughout (positivity, integrality) | Diffuse |
| **#10 Inequality Constraints** | Ch. 7 (primary) | Primary |
| **#11 Existence/Uniqueness** | Ch. 3 (extremal as existence), Ch. 11 (FE solution existence) | Secondary |
| **#12 Extremal Principles** | Ch. 3 (primary), Ch. 13 (games as extremal) | Primary in Ch. 3 |
| **#13 Combinatorial Principles** | Ch. 4 (pigeonhole — primary), Ch. 5 (counting — primary) | Primary in Chs. 4, 5 |
| **#14 Parity/Modularity** | Ch. 1 (parity invariants), Ch. 2 (colouring — primary), Ch. 6 (NT mod arguments) | Primary in Ch. 2 |
| **#15 Bijection/Correspondence** | Ch. 5 (bijection counting — primary), Ch. 8 (Fibonacci bijections) | Primary in Ch. 5 |
| **#16 Reverse Engineering** | Ch. 8 (Vieta jumping), Ch. 14 (infinite descent — primary) | Primary in Ch. 14 |
| **#17 DOF Analysis** | Not directly — Engel doesn't name DOF explicitly | Weak |
| **#18 Recursion/Induction** | Ch. 5 (recursion counting), Ch. 8 (induction — primary), Ch. 9 (recurrences) | Primary in Ch. 8 |
| **#19 Pivoting/Elimination** | Implicit throughout (Gaussian elimination, polynomial elimination), but Engel doesn't single it out | Weak |
| **#20 Analogy/Transfer** | Ch. 14 (meta-archetype) — implicit in the "Further Strategies" framing | Diffuse |

---

## V. Multi-Archetype Convergence Index — THE PILLAR 3 GOLDMINE

This is the **unique-to-Engel section**, curated specifically for Pillar 3 case-study mining. Every entry below is a problem where Engel's exposition explicitly or implicitly invokes 2 or 3 archetypes simultaneously. These are the primary candidates for Pillar 3 Ch. 1–7 worked examples and Ch. 6 case studies.

### 2-Archetype Convergence Problems (for Pillar 3 Ch. 2)

| Problem | Source (Engel) | Archetypes | Notes |
|---|---|---|---|
| 5 points in unit square, two within $\sqrt 2/2$ | **Ch. 4 E12-type** (cited as §7.9 Case Study #1) | #13 Combinatorial (pigeonhole) + #12 Extremal | **Locked as Pillar 3 Ch. 6 Case Study #1** |
| Lattice-point midpoints (5 lattice points → pair with lattice midpoint) | Ch. 4 E7 | #13 Combinatorial + #14 Parity | Excellent Pillar 3 Ch. 1 / Ch. 2 illustration |
| Sylvester-Gallai (finite plane points → collinear) | Ch. 3 E10 | #12 Extremal + #2 Symmetry | Classical 2-archetype, Kelly's 1948 4-line proof |
| Farms-and-wells matching (no crossings) | Ch. 3 E4 | #12 Extremal + #15 Bijection | Geometric extremal + bijection |
| Parliament of Sikinia (≤ 1 enemy in own house) | Ch. 1 E4 | #1 Invariance (monovariant) + #12 Extremal (well-ordering) | Termination via decreasing monovariant |
| $341 \mid 2^{341} - 2$ (pseudoprime to FLT) | Ch. 6 (in Wilson-FLT discussion) | #14 Parity/Modularity + #4 Hidden Structure (factorisation of $341$) | Counterexample-as-discovery |
| Chessmaster's 77-day sequence with exactly 21 games | Ch. 4 E2 | #13 Combinatorial (pigeonhole) + #1 Invariance (partial-sum sequence) | Classical pigeonhole on $a_i$ vs $a_i + 21$ |
| Erdős-Szekeres monotone subsequence | Ch. 4 E6 | #13 Combinatorial (pigeonhole on pairs $(L_m, R_m)$) + #18 Induction | Two-archetype, very clean |
| Nesbitt's inequality (any of four proofs) | Ch. 7 E7 | #10 Inequality + (substitution / AM-HM / Engel-Cauchy) | The "four proofs" demonstration is a Pillar 3 Ch. 5 illustration |
| Tennis-tournament pairings $(2n)!/(2^n n!)$ | Ch. 5 E8 | #13 Combinatorial + #18 Recursion (or + #15 Bijection) | Three solutions = three archetype pairs |

### 3-Archetype Convergence Problems (for Pillar 3 Ch. 3 + Ch. 6)

| Problem | Source (Engel) | Archetypes | Notes |
|---|---|---|---|
| **IMO 1988 P6 (Vieta jumping)**: $a, b \in \mathbb{Z}_{\ge 0}$, $(a^2+b^2)/(ab+1) \in \mathbb{Z}_{\ge 0}$ ⇒ quotient is square | **Ch. 8 Problem 6** | #18 Induction (on $ab$) + #16 Reverse Engineering (Vieta descent) + #1 Invariance (quotient preserved) | **LOCKED as Pillar 3 Ch. 3 WE1**; the canonical 3-archetype problem |
| **IMO 1977** 7-sums-negative-11-sums-positive | **Ch. 5 E1** | #13 Combinatorial (length-counting argument) + #14 Parity (sum-sign) + #1 Invariance | 2- or 3-archetype depending on framing |
| **IMO 1978** sum-free sets (6 countries, 1978 members) | **Ch. 4 E15** | #13 Combinatorial + #14 Parity + #2 Symmetry | 3-archetype classic |
| 2-coloured plane has monochromatic equilateral triangle | Ch. 2 Problem 35 | #14 Parity (colouring) + #12 Extremal + #2 Symmetry | Plane geometry + colouring + symmetry |
| Fermat's Little Theorem (with three proofs) | Ch. 6 §FLT | #18 Induction (proof 1) + #1 Invariance (proof 2, congruences) + #13 Combinatorial (proof 3, necklaces) | The "one theorem, three proofs" = Pillar 3 Ch. 5 MVC illustration |
| Engel Ch. 11 functional equation (substitution + induction + parity) | Ch. 11 (specific problem TBD at draft time) | #5 Substitution + #18 Induction + #14 Parity | **LOCKED as Pillar 3 Ch. 6 Case Study #5** |
| Diophantine $x^2 + y^2 + z^2 + u^2 = 2xyzu$ no positive-int solutions | Ch. 14 E3 | #14 Parity (mod 8) + #16 Reverse Engineering (descent) + #18 Induction | Infinite descent classic |

### Forward-Reference to §7.9 Case Study Slate (LOCKED)

| § | Case Study | Engel source | Tier |
|---|---|---|---|
| 1 | Engel's classical pigeonhole (5 points in unit square) | **Ch. 4 (or Ch. 5)** — pigeonhole + extremal | 2 |
| 2 | Zeitz no-monochromatic-AP-3 colouring | Not in Engel — Zeitz Ch. 4 | 3 |
| 3 | Putnam convex polygon partition (year TBD) | Not in Engel — Putnam archive | 3 |
| 4 | IMO shortlist combinatorics (extremal + descent + parity) | Cf. Engel **Ch. 14** (infinite descent treatment) for technique baseline | 4 |
| 5 | Engel functional equation (subst + induction + parity) | **Ch. 11** (specific problem TBD) | 4 |

---

## VI. Notable Theorems & Named Results

Engel introduces or restates many classical results. The most-cited:

- **Sylvester-Gallai theorem** (Sylvester 1893, Gallai 1933, Kelly 1948) — Ch. 3 E10
- **Erdős-Szekeres theorem** (1935) — Ch. 4 E6
- **Ramsey numbers** $R(3,3) = 6$ (Greenwood-Gleason 1947) — Ch. 4 E12
- **Schur's theorem** on sum-free sets (1916) — Ch. 4 §Schur
- **Fermat's Little Theorem** (1640) — Ch. 6 §FLT (with three proofs)
- **Fermat-Euler theorem** — Ch. 6
- **Fundamental Theorem of Arithmetic** — Ch. 6
- **Cassini identity** $F_{n-1} F_{n+1} = F_n^2 + (-1)^n$ — Ch. 8
- **Binet's formula** for Fibonacci numbers — Ch. 8
- **Cardano's formula** for cubic equations — Ch. 10
- **Fundamental Theorem of Algebra** — Ch. 10
- **Cauchy's functional equation** + Hamel pathological solutions — Ch. 11
- **AM-GM-HM-QM inequality chain** — Ch. 7
- **Nesbitt's inequality** (England 1903) — Ch. 7 E7 (with four proofs)
- **"Cauchy-Schwarz in Engel form"** $\sum (x_i^2/y_i) \ge (\sum x_i)^2 / (\sum y_i)$ — sometimes named after Engel for this exposition
- **Fermat's method of infinite descent** (1640) — Ch. 14 §14.2
- **Wythoff's game** with golden-ratio characterisation — Ch. 13
- **Bachet's game** — Ch. 13

---

## VII. Voice Register Samples for Pillar 3 Drafting

Engel's voice is the polar opposite of Joshi's. Pillar 3 chapters should adopt a register closer to Engel for the worked-example sections (terse, technique-driven) while retaining the Advaitian-philosophical opening vignettes from Pillar 2's tradition.

**Sample 1 — Engel's terse opening to a chapter (Ch. 5 §intro):**
> "Ideally an IMO problem should be unknown to all students. Even a similar problem should never have been discussed in any country. What was the status of E1 in July 1977? Years later, I was browsing in Dynkin–Molchanov–Rosental–Tolpygo: Mathematical Problems, 1971, 3rd edition with 200,000 copies sold. There, I found problem 118: [...]. The origin of the problem was MMO 1969. The motive of E1 was well known in Eastern Europe, so it should not have been used at all."

This is Engel: factual, slightly sardonic, no flourish. Pillar 3 chapters should follow this register for the *§1 The Pattern* section.

**Sample 2 — Engel solving an IMO problem in one short paragraph (Ch. 4 E12 / Ramsey $R(3,3) = 6$):**
> "The edges of a $G_6$ are coloured red or blue. Take any of the six points and call it $P$. At least 3 of the 5 lines which start at $P$ are of the same colour, say red. These red lines end at 3 points $A, B, C$. If any side of the triangle $ABC$ is red, we have a red triangle. If not, $ABC$ is a blue triangle. In both cases, we have a monochromatic triangle."

This is Engel at his most compressed: a Putnam 1953 problem dispatched in 4 sentences. Pillar 3 worked examples should aspire to this density (though our Pillar 3 will add the convergence-diagram visualisation for pedagogical reinforcement).

**Sample 3 — Engel's introduction of monovariants (Ch. 1 E4, after the Parliament-of-Sikinia solution):**
> "Here we have a new idea. We construct a positive integral function which decreases at each step of the algorithm. So we know that our algorithm will terminate. There is no strictly decreasing infinite sequence of positive integers. $H$ is not strictly an invariant, but decreases monotonically until it becomes constant. Here, the monotonicity relation is the invariant."

This is Engel naming a concept (monovariant), justifying it (well-ordering), and re-framing it (the monotonicity *itself* as the invariant). Pillar 3 should use this naming + justifying + re-framing rhetorical move when introducing the three canonical Pillar 3 constructs (Convergence Diagram, First-Minute Protocol, Escape-Hatch Architecture).

**Sample 4 — Engel's "I am not sure" register (Ch. 9 E3, after a partial solution):**
> "Replacing $\sqrt 2$ by the positive root of $t^3 = t^2 + t + 1$, no periodicity was in sight after many steps. Whenever $t^3$ turned up, I replaced it by $t^2 + t + 1$. Is $f$ not periodic in this case? A second look shows that (1) is a linear difference equation of second order..."

Engel openly admits when he was stuck and how he recovered. This honest, exploratory register is the perfect model for Pillar 3 Ch. 7 (Escape-Hatch Architecture), which is *about* what to do when stuck.

**Sample 5 — Engel's competition-source citation discipline (throughout Ch. 4):**
> "*Problem 15.* An international society has members from six different countries. The list of members contains 1978 names, numbered $1, 2, \ldots, 1978$. Prove that there is at least one member whose number is the sum of the numbers of two members from his own country or twice as large as the number of one member from his own country (IMO 1978)."

The "(IMO 1978)" annotation pattern is Engel's standard. Pillar 3 chapters should follow the identical citation discipline (competition + year, parenthesised, immediately after the problem statement).

---

## Maintenance Notes

**Last refreshed.** 1.0 — May 28 2026. Initial comprehensive consolidated extraction.

**When to refresh.** Whenever a new Pillar 3 chapter is drafted and a problem from Engel is pulled, append the problem citation to §V (Multi-Archetype Convergence Index) with the chapter-of-use note. This keeps §V live as a tracking record of which Engel problems have been used in Pillar 3 and which remain for future use.

**Cross-references in this file.**
- §I Chapter-by-Chapter Index — high-level lookup
- §II Chapter Details — per-chapter conceptual content
- §III Master Index by Competition — for cross-referencing IMO/Putnam/etc. problems
- §IV Master Index by Pillar 2 Archetype — for mapping Engel chapters to our 20 archetypes
- **§V Multi-Archetype Convergence Index — THE PRIMARY LOOKUP for Pillar 3 case-study mining**
- §VI Notable Theorems — for technique-named-result lookups
- §VII Voice Register Samples — for Pillar 3 drafting

**Companion file.** `Cursor-Joshi.md` (the Pillar 2 analogue) is the canonical reference for cross-archetype problem mining from K.D. Joshi's *Educative JEE Mathematics*. Joshi remains a *secondary* source for Pillar 3 (per blueprint §7.2); Engel is *primary*.

*End of Cursor-Engel.md v1.0.*
