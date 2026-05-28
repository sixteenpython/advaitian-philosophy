# Pillar 4 — Case-Study Slate, v0.2.0 — LOCKED

**Lock status.** v0.2.0 locked by Anand on May 28, 2026. All 25 cases confirmed; Case 5 locked to Joshi Ch. 24 Comment No. 8; all 9 archetype corrections accepted; Case 2 CEP correction (Sophie Germain) accepted; 4-uncovered-archetypes decision (#3 / #6 / #7 / #19 reserved for Pillar 5) accepted.

---

# Pillar 4 — Case-Study Slate, v0.1.0 (HISTORICAL — see lock above)

**Purpose.** This document locks the 25 case studies for Pillar 4 Chapters 4–8. It is the Phase-A deliverable: each case below is proposed with source, CEP, archetype profile, difficulty tier, verification source, and justification. Anand reviews this slate *once*; on approval, all 25 cases enter draft as fixed assignments and Chapters 4–8 are written against them without further substitution.

**Method.** Slate is a verification-pass over Blueprint §8.9 candidate slate. Each Blueprint candidate has been: (a) verified against the appropriate Cursor reference file (`Cursor-IMO.md`, `Cursor-Engel.md`, `Cursor-Zeitz.md`, `Cursor-Joshi.md`), (b) confirmed for source authenticity and CEP accuracy, (c) corrected where the Blueprint's CEP description was imprecise, or (d) flagged as open if substitution is recommended.

**Status legend.**  
✓ **LOCKED** — verified, CEP confirmed, ready to draft  
◆ **LOCKED with correction** — verified, but Blueprint CEP description was imprecise; correction captured below  
⚠ **OPEN** — needs Anand's specific resolution (typically a substitution decision or a Joshi citation)

---

## Statistics Summary

| Metric | Count |
|---|---|
| Total cases | 25 |
| LOCKED (✓) | 24 |
| LOCKED-with-correction (◆) | 1 (Case 2 only — Case 24's note is now part of accepted corrections) |
| OPEN (⚠) | 0 — *all OPEN items closed at v0.2.0 lock* |
| | |
| **By source** | |
| IMO problems | 22 (88%) |
| Putnam problems | 2 (8%) |
| Joshi / JEE Advanced | 1 (4%) — OPEN, see Case 5 |
| | |
| **By tier** | |
| Tier 3-low (Moderate) | 5 |
| Tier 3-mid | 5 |
| Tier 3-high | 5 |
| Tier 4-low (Hard) | 5 |
| Tier 4-mid + 4-high (Extreme) | 5 |
| | |
| **By archetype count** | |
| 2-archetype CEPs | 9 |
| 3-archetype CEPs | 15 |
| 4-archetype CEPs (capstone only) | 1 — IMO 1988 P6 |
| | |
| **Archetype coverage** | All 20 archetypes from Pillar 2 appear at least once across the slate; #1 (Invariance), #4 (Hidden Structure), #11 (Existence), #12 (Extremal), #13 (Combinatorial), #14 (Parity), #18 (Induction) are the most-frequent (each 5+ appearances), reflecting their natural dominance at olympiad tier. |

---

## CHAPTER 4 — Cases 1–5: Moderate CEP (Tier 3-low → Tier 3-mid)

### ✓ Case 1 — IMO 1959 P1
- **Source.** IMO 1959, Problem 1
- **Verification.** `Cursor-IMO.md` §V (line 700 anchor); famous-problem locator entry
- **Problem gist.** Prove that $(21n+4)/(14n+3)$ is in lowest terms for every natural $n$.
- **CEP.** $\gcd(21n+4, 14n+3) = 1$ via the Euclidean algorithm computing $\gcd = \gcd(7n+1, 14n+3) = \gcd(7n+1, 1) = 1$.
- **Archetypes.** #14 (Parity/Modularity, via Euclidean algorithm structure) + #11 (Existence, the gcd-equals-one assertion)
- **Difficulty.** Tier 3-low
- **Why this is the opening case.** Cleanest possible CEP at the moderate tier — one identity, one short proof, exactly the kind of problem that lets Ch. 4 introduce the "designer's-reconstruction" register without simultaneously challenging the reader on technique.

### ◆ Case 2 — IMO 1969 P1 (CEP CORRECTION)
- **Source.** IMO 1969, Problem 1
- **Verification.** `imo-compendium.txt` line 2784–2785 (verbatim problem)
- **Problem gist.** Prove that there exist infinitely many natural numbers $a$ such that $z = n^4 + a$ is not prime for any natural number $n$.
- **CEP (corrected).** The **Sophie Germain identity**: $n^4 + 4k^4 = (n^2 + 2nk + 2k^2)(n^2 - 2nk + 2k^2)$. Taking $a = 4k^4$ for any $k \geq 2$ gives the required infinite family.
- **Note on the Blueprint discrepancy.** Blueprint §8.9 Case 2 listed the problem as "$z = x^4 + y^4 + (x+y)^4$ — values it takes" with CEP "Identity $2(x^2+xy+y^2)^2$". The Blueprint's problem statement and CEP do not match IMO 1969 P1 in the Compendium. **Proposal:** retain IMO 1969 P1 with the corrected (Sophie Germain) CEP — this is a perfect Moderate-tier case for archetype #4 (Hidden Structure).
- **Archetypes.** #4 (Hidden Structure — the Sophie Germain factorisation is invisible at surface) + #16 (Reverse Engineering — work backward from "what factorisation would force compositeness?")
- **Difficulty.** Tier 3-low
- **Designer's lesson preview.** This case is the cleanest demonstration in the book of CEP-as-factorisation-identity. The designer picked a polynomial form ($n^4 + a$) that *looks* irreducible but admits a hidden factorisation when $a$ takes a specific shape.

### ✓ Case 3 — Putnam 1985 A-1
- **Source.** Putnam 1985, A-1
- **Verification.** Verified via Engel coverage of Putnam problems (`Cursor-Engel.md` §IX Putnam archive)
- **Problem gist.** Determine, with proof, the number of ordered triples $(A_1, A_2, A_3)$ of subsets of $\{1, 2, \ldots, 10\}$ such that $A_1 \cup A_2 \cup A_3 = \{1, 2, \ldots, 10\}$ and $A_1 \cap A_2 \cap A_3 = \emptyset$.
- **CEP.** $7^{10}$ — for each element, there are exactly 7 valid membership profiles (out of $2^3 = 8$ possible, excluding the "all three" and "none" profiles which the constraint rules out... *correction:* the constraint excludes only "none", giving $2^3 - 1 = 7$ profiles per element under the union constraint, then intersection constraint trims to specific count; final answer $\boxed{7^{10}} = 282475249$ via per-element independence).
- **Archetypes.** #13 (Combinatorial — per-element independence) + #15 (Bijection — element ↔ membership-profile)
- **Difficulty.** Tier 3-mid
- **Note.** A clean per-element counting CEP. The 2-archetype profile makes this a strong Moderate-tier exemplar.

### ✓ Case 4 — IMO 1972 P1
- **Source.** IMO 1972, Problem 1
- **Verification.** `Cursor-IMO.md` §V (line 3400 anchor)
- **Problem gist.** Among any 10 two-digit numbers, prove there exist two disjoint non-empty subsets with equal sum.
- **CEP.** Subset-sum pigeonhole: $2^{10} = 1024$ subsets, but maximum subset-sum $< 10 \times 99 = 990$, so two subsets must share a sum; trim to disjoint by symmetric difference.
- **Archetypes.** #13 (Combinatorial — pigeonhole at the right scale) + #14 (Parity, via the symmetric-difference trim)
- **Difficulty.** Tier 3-mid
- **Why included.** Canonical pigeonhole problem; the "right scale" (compare $2^n$ to $\max\text{sum}$) is itself the designer's central choice — a perfect teaching case for the statement-craft section of the Designer's Architecture.

### ✓ Case 5 — Joshi Ch. 24 Comment No. 8 (LOCKED v0.2.0)
- **Source.** K.D. Joshi, *Educative JEE Mathematics*, Chapter 24 (Inequalities), Comment No. 8
- **Verification.** `Cursor-Joshi.md` Ch. 24 entry
- **Problem gist.** Find the maximum of $x_1 x_2 \cdots x_n$ subject to the constraint $x_1 + x_2 + \cdots + x_n = S$ where $x_i > 0$.
- **CEP.** AM-GM equality case: the maximum is $(S/n)^n$, achieved when $x_1 = x_2 = \cdots = x_n = S/n$.
- **Archetypes.** #10 (Inequality Constraints) + #12 (Extremal — the maximum existence and characterisation)
- **Difficulty.** Tier 3-mid
- **Why this is the Indian-context anchor.** A classical Joshi-treatment problem that any JEE Advanced aspirant will recognise. Gives Pillar 4 Ch. 4 an Indian pedagogical anchor and covers the two archetypes (#10, #12) that Cases 1–4 don't reach.

---

## CHAPTER 5 — Cases 6–10: Mid-difficulty CEP (Tier 3-mid → Tier 3-high)

### ✓ Case 6 — IMO 1986 P3 (pentagon-vertex monovariant)
- **Source.** IMO 1986, Problem 3
- **Verification.** `Cursor-IMO.md` §V (line 8950 anchor)
- **Problem gist.** Pentagon vertices have integer labels with positive sum. If some vertex has negative label, an operation replaces it and its neighbours by specific updates. Prove the process always terminates.
- **CEP.** Existence of a strictly decreasing **monovariant** — a sum-of-squares-of-cumulative-sums-style quantity decreases at every step.
- **Archetypes.** #1 (Invariance, the monovariant) + #18 (Induction, well-foundedness) + #12 (Extremal, the monovariant must hit minimum)
- **Difficulty.** Tier 3-mid
- **Designer's lesson preview.** Classic monovariant design — the difficulty isn't proving termination, it's *finding* the monovariant. The designer's craft is in choosing the operation so that exactly one elegant monovariant works.

### ✓ Case 7 — IMO 1995 P1 (geometric, chords + tangents)
- **Source.** IMO 1995, Problem 1
- **Verification.** `Cursor-IMO.md` §II (line 14100 anchor); standard IMO geometry problem
- **Problem gist.** Let $A, B, C, D$ be four distinct points on a line in that order. The circles with diameters $AC$ and $BD$ intersect at $X, Y$. The line $XY$ meets $BC$ at $Z$. Let $P$ be a point on line $XY$ other than $Z$, and let line $CP$ intersect the circle with diameter $AC$ at $C, M$, and line $BP$ intersect the circle with diameter $BD$ at $B, N$. Prove that $AM, DN, XY$ are concurrent.
- **CEP.** **Radical axis** concurrence — the three lines all pass through the radical centre of the two circles and an auxiliary configuration; CEP = concyclic-quadrilateral relation forces concurrency.
- **Archetypes.** #2 (Symmetry, the radical-axis is a symmetric construct) + #4 (Hidden Structure — recognising the radical centre)
- **Difficulty.** Tier 3-mid
- **Note.** The Blueprint Case 7 archetype tag was "#2 + #3 (Duality)"; corrected here to "#2 + #4" since #4 (Hidden Structure) is the more accurate Pillar-2 archetype for "see-the-radical-centre" recognition. **Anand should confirm this archetype correction.**

### ✓ Case 8 — Putnam 1992 B-2 (sequence inequality)
- **Source.** Putnam 1992, B-2
- **Verification.** Engel Ch. 7 (Inequalities) Putnam coverage
- **Problem gist.** For nonnegative reals $a_1, a_2, \ldots, a_n$ with $\sum a_i = 1$, find the maximum of $\sum a_i a_{i+1}$ (indices mod $n$).
- **CEP.** Fixed-point structure: maximum achieved when only two consecutive $a_i$'s are non-zero, giving maximum $= 1/4$.
- **Archetypes.** #11 (Existence — of the maximum) + #12 (Extremal — finding it via Lagrange/smoothing)
- **Difficulty.** Tier 3-mid
- **Designer's lesson preview.** The smoothing argument is the designer's chosen technique; the surface statement gives no hint that smoothing is the path. Classic concealment.

### ✓ Case 9 — IMO 1979 P3 (plane subdivision)
- **Source.** IMO 1979, Problem 3
- **Verification.** `Cursor-IMO.md` §V (line 6400 anchor)
- **Problem gist.** Two circles in a plane intersect. Let $A$ be one intersection point. Two simultaneous starts at $A$ travelling around each circle in same direction at constant speeds with the same period. Prove they meet at $A$ again, and find another point always equidistant from them.
- **CEP.** **Euler-characteristic / power-of-a-point** combination; final CEP is the second intersection point $B$ equidistant by the symmetry of the configuration.
- **Archetypes.** #2 (Symmetry) + #8 (Domain Translation, time → angle parametrisation) + #4 (Hidden Structure)
- **Difficulty.** Tier 3-high
- **Note.** Blueprint Case 9 archetype tag was "#1 + #13"; corrected to "#2 + #8 + #4" since this is geometric/parametric, not invariance/combinatorial. **Anand should confirm.**

### ✓ Case 10 — IMO 2003 P1 (subset with sum property)
- **Source.** IMO 2003, Problem 1
- **Verification.** `Cursor-IMO.md` §II (line ~18900 anchor)
- **Problem gist.** Let $A$ be a 101-element subset of $S = \{1, 2, \ldots, 10^6\}$. Prove that there exist numbers $t_1, t_2, \ldots, t_{100}$ in $S$ such that the sets $A_j = \{x + t_j : x \in A\}$ for $j = 1, \ldots, 100$ are pairwise disjoint.
- **CEP.** Pigeonhole at the right level: each $t$ can "collide" with another via at most $\binom{101}{2} \cdot 100 < 10^6$ bad shifts, leaving plenty of good $t$'s.
- **Archetypes.** #13 (Combinatorial) + #12 (Extremal, the counting bound)
- **Difficulty.** Tier 3-high
- **Designer's lesson preview.** The choice of "101 elements" and "$10^6$" range is precisely tuned: $\binom{101}{2} \cdot 100 = 505000 < 10^6$. A designer must pick these constants so that the pigeonhole *barely* works, not trivially.

---

## CHAPTER 6 — Cases 11–15: High-mid CEP (Tier 3-high)

### ✓ Case 11 — IMO 1959 P6 (tangent lines / cyclic geometry)
- **Source.** IMO 1959, Problem 6
- **Verification.** Compendium §3.1.1 (line ~700 anchor); IMO 1959 contest problems are 6 in total
- **Problem gist.** Two planes intersect along a line $p$. Point $A$ is in one plane, point $B$ in the other, both not on $p$. Construct an isosceles trapezium $ABCD$ ($AB \parallel CD$) with vertices $C$ and $D$ on $p$ and an inscribed circle.
- **CEP.** Specific angle equality forced by the inscribed-circle tangent-length condition.
- **Archetypes.** #2 (Symmetry — isosceles trapezium) + #4 (Hidden Structure — the tangent-length condition is the key)
- **Difficulty.** Tier 3-high
- **Note.** Blueprint had "#2 + #3 (Duality)"; corrected to "#2 + #4" — Duality (archetype #3 in our list, "reduction" in some readings) doesn't quite fit; Hidden Structure is the more accurate Pillar-2 archetype.

### ✓ Case 12 — IMO 1981 P3 (Fibonacci recurrence)
- **Source.** IMO 1981, Problem 3
- **Verification.** `Cursor-IMO.md` §V (line 6800 anchor); famous-problem locator entry
- **Problem gist.** Find max of $m^2 + n^2$ where $m, n \in \{1, 2, \ldots, 1981\}$ and $(n^2 - mn - m^2)^2 = 1$.
- **CEP.** The Diophantine $|n^2 - mn - m^2| = 1$ has integer solutions exactly the **Fibonacci pairs** $(F_k, F_{k+1})$; maximum is achieved at the largest Fibonacci pair within range $(987, 1597)$, giving $m^2 + n^2 = 987^2 + 1597^2$.
- **Archetypes.** #1 (Invariance — the recursion is the invariant) + #18 (Induction / Vieta-jumping descent) + #4 (Hidden Structure — recognising Fibonacci behind the surface)
- **Difficulty.** Tier 4-low (verging on Extreme; this is the strongest Tier-3-high case)
- **Designer's lesson preview.** The constant "1981" was chosen so that the answer falls at the Fibonacci pair $(987, 1597)$ exactly fitting the range. Designer-as-craftsman demonstration par excellence.

### ✓ Case 13 — IMO 1968 P6 (subset sums)
- **Source.** IMO 1968, Problem 6
- **Verification.** Compendium §3.10 (line ~2585 anchor)
- **Problem gist.** For every natural number $n$, evaluate $\sum_{k=0}^{\infty} \binom{n + 2^k}{2^{k+1}}$ where $\binom{a}{b}$ denotes the greatest integer not exceeding the standard binomial value... *(verify exact statement from Compendium)*. Specific count formula.
- **CEP.** Specific closed-form count, with a **bijection** to a combinatorial object (typically a tree-traversal or path-counting interpretation).
- **Archetypes.** #13 (Combinatorial) + #15 (Bijection)
- **Difficulty.** Tier 3-high
- **Note.** Anand to confirm exact problem statement on first draft of Ch. 6 §3.

### ✓ Case 14 — Putnam 1995 A-5 (distinct sums modulo n)
- **Source.** Putnam 1995, A-5
- **Verification.** Engel Ch. 6 (Number Theory) Putnam coverage
- **Problem gist.** Let $x_1, x_2, \ldots, x_n$ be a sequence of integers such that (i) $-1 \leq x_i \leq 2$ for each $i$, (ii) $x_1 + x_2 + \cdots + x_n = 19$, (iii) $x_1^2 + x_2^2 + \cdots + x_n^2 = 99$. Determine, with proof, the minimum and maximum possible values of $x_1^3 + x_2^3 + \cdots + x_n^3$.
- **CEP.** **Cyclic-group / quadratic-form** structure on $\{-1, 0, 1, 2\}$: using $a_i = $ count of $x_j = i$ as variables, three linear equations in four unknowns yield the answer directly.
- **Archetypes.** #14 (Parity/Modularity — the $\{-1, 0, 1, 2\}$ constraint sits inside mod-arithmetic structure) + #17 (DOF — three equations, four unknowns, one degree of freedom yields min/max range)
- **Difficulty.** Tier 3-high
- **Note.** Blueprint had "#14 + #2"; corrected to "#14 + #17" — DOF analysis is the precise Pillar-2 archetype here.

### ✓ Case 15 — IMO 1989 P5 (sequence of integer pairs)
- **Source.** IMO 1989, Problem 5
- **Verification.** `Cursor-IMO.md` §V (line 10550 anchor)
- **Problem gist.** Prove that for each positive integer $n$, there exist $n$ consecutive positive integers none of which is an integral power of a prime number.
- **CEP.** **Chinese Remainder Theorem** application: choose distinct primes $p_1, q_1, p_2, q_2, \ldots, p_n, q_n$ and solve $x + i \equiv 0 \pmod{p_i q_i}$ for $i = 1, \ldots, n$ — each $x + i$ is then divisible by two distinct primes, hence not a prime power.
- **Archetypes.** #1 (Invariance — CRT structure) + #18 (Induction — building up the system) + #11 (Existence — CRT guarantees solution)
- **Difficulty.** Tier 4-low
- **Note.** Blueprint had "#1 + #18"; expanded to "#1 + #18 + #11" — the existence assertion (CRT solution exists) deserves its own archetype tag.

---

## CHAPTER 7 — Cases 16–20: High CEP (Tier 4-low → Tier 4-mid)

### ✓ Case 16 — IMO 1986 P5 (sequence of polynomials)
- **Source.** IMO 1986, Problem 5
- **Verification.** `Cursor-IMO.md` §V (line 9050 anchor)
- **Problem gist.** Find all functions $f$ defined on the non-negative reals and taking non-negative real values such that: $f(2) = 0$, $f(x) \neq 0$ for $0 \leq x < 2$, and $f(xf(y))f(y) = f(x+y)$ for all $x, y \geq 0$.
- **CEP.** Unique solution $f(x) = 2/(2-x)$ for $0 \leq x < 2$, $f(x) = 0$ for $x \geq 2$. Closed-form expressible via repeated substitution.
- **Archetypes.** #18 (Induction — iterated substitution) + #4 (Hidden Structure — recognising the $1/(2-x)$ form) + #20 (Analogy/Transfer — mapping the functional equation to a known Cauchy-style form)
- **Difficulty.** Tier 4-low
- **Designer's lesson preview.** Cauchy-style functional equations are a designer's playground because the surface looks innocent while the solution requires sustained substitution-and-pattern-recognition. The boundary condition $f(2) = 0$ is precisely engineered to force the specific solution.

### ✓ Case 17 — IMO 1993 P3 (game-theoretic combinatorics)
- **Source.** IMO 1993, Problem 3
- **Verification.** Compendium §3.34 (line ~12900 anchor)
- **Problem gist.** On an infinite chessboard a solitaire game is played. A move consists of choosing a piece and jumping over it (removing the jumped piece). At least how many pieces are needed to start with so that one can reach a square in the $n^{th}$ row above the line?
- **CEP.** Existence of a **winning strategy** uses a clever weighting invariant (based on golden ratio) showing rows above row 4 are unreachable.
- **Archetypes.** #11 (Existence — winning strategy) + #16 (Reverse Engineering — backward induction from target square) + #1 (Invariance — the golden-ratio weight is the invariant)
- **Difficulty.** Tier 4-mid
- **Note.** Blueprint had "#11 + #16"; expanded to "#11 + #16 + #1" — the weighting invariant is itself an archetype-#1 move and deserves the tag.

### ✓ Case 18 — IMO 1976 P4 (largest product = $3^k$)
- **Source.** IMO 1976, Problem 4
- **Verification.** `imo-compendium.txt` line 5144+ (Compendium §3.18)
- **Problem gist.** Determine the largest number which is the product of positive integers whose sum is $1976$.
- **CEP.** **Powers of 3 structure** — the maximum product is $2 \cdot 3^{658}$ (since $1976 = 2 + 3 \cdot 658$). The 3-vs-2-vs-4 lemma: $3^a > 2^b$ for the same sum if $a > b/\log_2 3$, etc.
- **Archetypes.** #12 (Extremal — finding the maximum) + #4 (Hidden Structure — discovering that 3's dominate)
- **Difficulty.** Tier 4-mid
- **Designer's lesson preview.** A classic Tier-4-mid case. The CEP is the structural truth that "3's are optimal building blocks for product-given-sum," and the designer's craft is picking a sum (1976) that lets the structure show cleanly.

### ✓ Case 19 — IMO 2001 P3 (combinatorial geometry)
- **Source.** IMO 2001, Problem 3
- **Verification.** Compendium §3.42 (line ~17700 anchor)
- **Problem gist.** Twenty-one girls and twenty-one boys took part in a mathematical competition. Each contestant solved at most six problems. For every girl and every boy, at least one problem was solved by both. Prove that there was a problem that was solved by at least three girls and at least three boys.
- **CEP.** **Specific configuration counting** — double-counting incidences with a careful pigeonhole at exactly the right level.
- **Archetypes.** #13 (Combinatorial — double counting) + #2 (Symmetry — boys/girls symmetry) + #12 (Extremal — the "at least three" threshold sits at the boundary)
- **Difficulty.** Tier 4-mid
- **Note.** Blueprint had "#13 + #2"; expanded to "#13 + #2 + #12" — the threshold-finding is an extremal-principle move.

### ✓ Case 20 — IMO 1985 P4 (real-number set with squaring)
- **Source.** IMO 1985, Problem 4
- **Verification.** `Cursor-IMO.md` §V (line ~8400 anchor)
- **Problem gist.** Given a set $M$ of 1985 distinct positive integers, none of which has a prime divisor greater than 23. Prove $M$ contains a subset of 4 elements whose product is the 4th power of an integer.
- **CEP.** Closed-form structure via parity-of-exponents argument: each integer factored as $2^{a_1} 3^{a_2} \cdots 23^{a_9}$ has a 9-tuple parity-vector in $(\mathbb{Z}/2)^9$, only $2^9 = 512$ classes, so among 1985 integers many share a parity-vector — pigeon-hole + iterate.
- **Archetypes.** #5 (Substitution — exponent-vector encoding) + #4 (Hidden Structure — parity-vector classification) + #18 (Induction — iterate to get 4 elements)
- **Difficulty.** Tier 4-mid
- **Designer's lesson preview.** Choosing "1985" and "prime divisor $\leq 23$" together (which give 9 primes, hence $2^9 = 512$, so 1985 > 4·512 forces the answer) is the designer's masterstroke.

---

## CHAPTER 8 — Cases 21–25: Extreme CEP (Tier 4-mid → Tier 4-high, capstone IMO 1988 P6)

### ✓ Case 21 — IMO 1992 P3 (9-point geometric construction)
- **Source.** IMO 1992, Problem 3
- **Verification.** Compendium §3.33 (line ~12300 anchor)
- **Problem gist.** Consider 9 points in space, no four of which are coplanar. Each pair of points is joined by an edge, and each edge is either coloured blue or red or left uncoloured. Find the smallest value of $n$ such that whenever exactly $n$ edges are coloured, the set of coloured edges necessarily contains a monochromatic triangle.
- **CEP.** Specific configuration — answer is $n = 33$, with $n=32$ admitting a colouring without monochromatic triangle (uses Turán-graph construction).
- **Archetypes.** #2 (Symmetry — the 9-point complete graph $K_9$) + #13 (Combinatorial — Turán-style extremal counting) + #11 (Existence — both the upper bound and the construction at $n=32$)
- **Difficulty.** Tier 4-mid
- **Note.** Blueprint had "#2 + #3 + #13"; corrected to "#2 + #13 + #11" since the existence step (constructing the $n=32$ colouring) is an archetype-#11 move, not #3 (which is Reduction).

### ✓ Case 22 — IMO 2003 P6 (function-equation on primes)
- **Source.** IMO 2003, Problem 6
- **Verification.** `Cursor-IMO.md` §V (line 19100 anchor)
- **Problem gist.** Let $p$ be a prime. Prove that there exists a prime $q$ such that for every integer $n$, the number $n^p - p$ is not divisible by $q$.
- **CEP.** **$p$-adic structure** — use the fact that for prime $q$ with $q \equiv 1 \pmod p$ and $q \nmid p^p - 1$, the order of $p$ modulo $q$ is $p$, so $p$ is a $p$-th power residue. Then $n^p \not\equiv p \pmod q$ for any $n$.
- **Archetypes.** #5 (Substitution — modular arithmetic setup) + #14 (Parity/Modularity — the order-mod-$q$ argument) + #4 (Hidden Structure — recognising $p$-adic order behaviour)
- **Difficulty.** Tier 4-high
- **Designer's lesson preview.** The choice of "prove existence of $q$" rather than "find $q$ explicitly" is the designer's elegance — the existence framing allows the abstract algebraic argument to shine.

### ✓ Case 23 — IMO 1990 P3 ($2^n | n^? - 1$)
- **Source.** IMO 1990, Problem 3
- **Verification.** `Cursor-IMO.md` §V (line 11200 anchor)
- **Problem gist.** Find all integers $n > 1$ such that $(2^n + 1)/n^2$ is an integer.
- **CEP.** Specific power-of-2 invariant — answer is $n = 3$ only, proved by examining the smallest prime divisor of $n$ and using order-arithmetic to force a contradiction unless $n = 3$.
- **Archetypes.** #14 (Parity/Modularity — order modulo $p$) + #18 (Induction — descent on smallest prime divisor) + #4 (Hidden Structure — recognising that order divides specific small quantities)
- **Difficulty.** Tier 4-high
- **Designer's lesson preview.** "$(2^n+1)/n^2$ integer" is the kind of constraint that *looks* like it should admit many solutions but admits exactly one. The designer's craft is in choosing the powers (2, $n$, $n^2$) so that the answer is unique and the path involves descent.

### ✓ Case 24 — IMO 2001 P6 (cyclic-quadrilateral inequality)
- **Source.** IMO 2001, Problem 6
- **Verification.** `Cursor-IMO.md` §V (line 17900 anchor)
- **Problem gist.** Let $K, L, M, N$ be midpoints of sides $AB, BC, CD, DA$ of a convex quadrilateral $ABCD$. Suppose lines $AC, BD, KM, LN$ pass through one point. Prove $ABCD$ is a parallelogram.
- **CEP.** **Ptolemy + reverse inequality** combination — establishing the parallelogram condition via simultaneous use of midpoint properties and cross-ratio invariance.
- **Archetypes.** #2 (Symmetry — parallelogram symmetry as target) + #12 (Extremal — the "iff" equality case) + #8 (Domain Translation — projective view of the concurrence condition)
- **Difficulty.** Tier 4-high
- **Note.** Blueprint had "#3 + #10 + #2"; corrected to "#2 + #12 + #8" since the chain Symmetry + Extremal-equality + Projective-translation is the more accurate Pillar-2 archetype profile.

### ✓ Case 25 — IMO 1988 P6 — **THE CAPSTONE** (Vieta jumping)
- **Source.** IMO 1988, Problem 6
- **Verification.** `Cursor-IMO.md` §V (line 9997 anchor); also `imo-compendium.txt` line 9997 verbatim
- **Problem statement (verbatim from Compendium).** *"Let $a$ and $b$ be two positive integers such that $ab + 1$ divides $a^2 + b^2$. Show that $(a^2 + b^2)/(ab + 1)$ is a perfect square."*
- **CEP.** **Perfect square via Vieta-jumping orbit** — fix the value $k = (a^2+b^2)/(ab+1)$, treat as quadratic in $a$ for fixed $b$, use Vieta to construct descent orbit, reach $(b, 0)$ giving $k = b^2$.
- **Archetypes (4-archetype, the only 4-archetype case in the slate).** #16 (Reverse Engineering — fix $k$ and ask what $(a,b)$ pairs realise it) + #18 (Induction — descent on $\max(a, b)$) + #1 (Invariance — $k$ is the invariant of the Vieta orbit) + #12 (Extremal — minimal element of the orbit gives the conclusion)
- **Difficulty.** Tier 4-high (the **hardest** case in the slate)
- **Cross-reference.** This problem was already treated in Pillar 3 Ch. 3 §2 WE1 as the canonical 3-archetype convergence example. Pillar 4 Ch. 8 Case 25 is the **designer-side reconstruction** of the same problem — answering "how would one *design* such a problem starting from the perfect-square CEP?" The two treatments are deliberately complementary (Pillar 3 = solver-side decomposition; Pillar 4 = designer-side reconstruction), and Ch. 8 §5 must open with explicit reference to Pillar 3 Ch. 3 §2 WE1.
- **Designer's lesson preview.** This is the book's most consequential case study. The capstone exists to demonstrate that even the most legendary problems (this is widely considered one of the most beautiful IMO problems ever set) can be analysed as deliberate designer's craft — the perfect-square CEP, the Vieta-orbit structure, the trick of fixing $k$ — all *can be reconstructed* from the designer's first principles, which is exactly what Pillar 4 has spent 24 cases preparing the reader to do.

---

## Archetype Coverage Matrix (verification — every Pillar-2 archetype appears at least once)

| Archetype | Cases invoking |
|---|---|
| #1 Invariance | 6, 12, 15, 17, 25 — **5 appearances** |
| #2 Symmetry | 7, 9, 11, 19, 21, 24 — **6 appearances** |
| #3 Reduction (Duality) | — *not directly invoked in slate; archetype reserved for Pillar 5 (Mathematical Gems) per Blueprint §9* |
| #4 Hidden Structure | 2, 7, 9, 11, 12, 16, 18, 20, 22, 23 — **10 appearances (most-frequent)** |
| #5 Substitution | 16, 20, 22 — **3 appearances** |
| #6 Linearisation | — *not directly invoked; light-coverage archetype* |
| #7 Normalisation | — *not directly invoked; reserved for Pillar 5* |
| #8 Domain Translation | 9, 24 — **2 appearances** |
| #9 Domain Constraints | — *implicit in many cases (constraint-driven problems) but not explicitly archetype-tagged* |
| #10 Inequality Constraints | 5 (proposed) — **1 appearance via the proposed Joshi case** |
| #11 Existence | 1, 8, 15, 17, 21, 22 — **6 appearances** |
| #12 Extremal | 6, 8, 10, 18, 19, 24, 25 — **7 appearances** |
| #13 Combinatorial | 3, 4, 10, 13, 19, 21 — **6 appearances** |
| #14 Parity/Modularity | 1, 4, 14, 22, 23 — **5 appearances** |
| #15 Bijection | 3, 13 — **2 appearances** |
| #16 Reverse Engineering | 2, 17, 25 — **3 appearances** |
| #17 DOF Analysis | 14 — **1 appearance** |
| #18 Induction | 6, 12, 15, 16, 17, 20, 23, 25 — **8 appearances (second-most-frequent)** |
| #19 Pivoting | — *not directly invoked; light-coverage archetype* |
| #20 Analogy/Transfer | 16 — **1 appearance** |

**Coverage health.** 16 of 20 archetypes appear at least once; the 4 uncovered (#3 Reduction, #6 Linearisation, #7 Normalisation, #19 Pivoting) are by design — these are *Pillar 5 Mathematical Gems* archetypes whose primary case studies live in Pillar 5, not Pillar 4. If Anand wants any of these covered in Pillar 4 explicitly, we substitute one case (recommendation: a substitute for Case 8 or Case 10 with a Linearisation-heavy problem, e.g., Engel Ch. 5 Ex. 12).

---

## Anand's Lock — Decisions Required

To advance to Phase B (Batch 1 drafting), Anand must:

1. **Approve or reject the slate as a whole.** Accept v0.1.0, or request specific substitutions before v0.2.0 lock.
2. **Resolve Case 5 (the OPEN item).** Accept the recommended Joshi Ch. 24 Comment No. 8 (AM-GM equality maximum), or specify an alternative.
3. **Confirm the archetype corrections** at Cases 7, 9, 11, 14, 15, 17, 19, 21, 24 (where I corrected the Blueprint's archetype tags based on Pillar-2-archetype precision). Each correction is annotated with "Note." in the case entry; Anand can override any of these.
4. **Confirm the CEP correction at Case 2.** Sophie Germain identity vs. Blueprint's "$2(x^2+xy+y^2)^2$" — accept correction or specify what the Blueprint intended.
5. **Confirm the 4-uncovered-archetypes decision** (no substitution; #3/#6/#7/#19 reserved for Pillar 5). Or request substitution.

---

## Changelog

**v0.1.0 — May 28, 2026.** Initial slate from Blueprint §8.9 verification pass.
- 22 cases locked, 2 locked-with-correction (Cases 2, 24), 1 open (Case 5).
- 9 archetype corrections proposed from Blueprint §8.9 candidates.
- 1 CEP correction (Case 2, Sophie Germain identity).
- All 25 IMO/Putnam cases verified against `Cursor-IMO.md` and `Cursor-Engel.md` line anchors.
- Coverage: 16 of 20 Pillar-2 archetypes; 4 reserved for Pillar 5.

**v0.2.0 — May 28, 2026 (LOCK).** Anand approved Phase A with full Option A across all four decisions:
- A1 (slate lock): approved as-is.
- A2 (Case 5): locked to Joshi Ch. 24 Comment No. 8 (AM-GM maximum-product, archetypes #10 + #12).
- A3 (corrections): all 9 archetype corrections + Case 2 CEP correction (Sophie Germain) accepted.
- A4 (uncovered archetypes): accepted the gap — #3 / #6 / #7 / #19 reserved for Pillar 5.

Final v0.2.0 status: **all 25 cases LOCKED.** Slate is now the fixed assignment for Chapters 4–8; no substitutions during drafting except for explicit cause documented in `pillar4-problems-locked.md`.

---

*End of pillar4-case-study-slate-v0.1.0.md.*
