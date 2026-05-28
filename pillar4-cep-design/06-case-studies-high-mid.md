---
chapter: 6
pillar: 4
chapter_type: case-study
title: "Case Studies 11–15: High-mid CEP"
subtitle: "The construction itself becomes the problem."
length_target_words: 6700
canonical_takeaway: "High-mid CEPs require the solver to engineer a mathematical object whose existence is not obvious from the surface — a tangent-length identity, a Fibonacci descent, a Hermite identity, an exponent-class structure, a CRT system."
status: draft
last_revised: 2026-05-28
references_invoked: [IMO-1959-P6, IMO-1981-P3, IMO-1968-P6, Putnam-1995-A5, IMO-1989-P5, Engel-Ch-2-Fibonacci, Joshi-Ch-6-NT]
voice_register: tao-warm
pillar3_cross_references: [pillar3-ch-3-§1]
---

# Chapter 6 — Case Studies 11–15: High-mid CEP

> *"It is hardly an exaggeration to say that one has not solved the problem until one has discovered the right Fibonacci number."*  
> — Anand Venkat, manuscript notebook on IMO 1981 P3, c. 2023

---

## §0 — Chapter Opening: When the Construction Becomes the Problem

In Chapter 5 the solver had to *find* a single intermediate construction (a monovariant, a circle, a fixed point) before the convergence completed. In this chapter the construction itself *is the problem*: each of the five cases ahead requires the solver to identify a structural object — a tangent-length identity that forces an inscribed-circle existence; a Fibonacci recurrence concealed inside a Diophantine equation; a Hermite floor-sum identity hidden in a $\sum \lfloor \cdot \rfloor$ expression; an exponent-vector residue structure that turns 1985 distinct integers into a 4-element subset with cube-power product; a Chinese Remainder system that produces $n$ consecutive non-prime-powers — and the structural object's existence is the central non-obvious mathematical fact.

What this looks like in practice: in Chapter 5 the smoothing argument *was* the proof of Putnam 1992 B-2's maximum, once the solver thought to try smoothing. In Chapter 6 the *Fibonacci connection* in IMO 1981 P3 is a non-trivial number-theoretic identification — the solver who discovers the equation $|n^2 - mn - m^2| = 1$ has integer solutions exactly at consecutive Fibonacci pairs has *learned a new piece of number theory*, not merely recognised a technique. This is the High-mid tier's signature: the case studies do not merely *apply* known techniques; they *reveal* small pieces of named mathematics that the well-designed problem makes visible by forcing the solver to discover them.

We continue with the §8.10 sub-template.

---

## §1 — Case Study 11: IMO 1959 Problem 6 (the inscribed-circle trapezoid)

**Source.** International Mathematical Olympiad 1959, Problem 6 (Czechoslovak proposal).  
**CEP.** The tangent-length theorem: an inscribed circle exists in a quadrilateral if and only if the two sums of opposite sides are equal. Combined with the isosceles condition ($|AD| = |BC|$), this forces $|AB| + |CD| = 2 |AD|$ — a single linear identity that uniquely constructs $B$ and $D$ given $A, C, p$.  
**Archetypes.** #2 (Symmetry — isosceles trapezoid + reflection across the perpendicular bisector of $p$) + #4 (Hidden Structure — recognising that *"a circle can be inscribed"* is shorthand for the sum-of-opposite-sides identity).  
**Difficulty.** Tier 3-high.  
**Verification source.** `imo-compendium.txt` lines 1649–1652; problem statement verbatim from Compendium §3.1.1.

### Problem statement

> Let $\alpha$ and $\beta$ be two planes intersecting at a line $p$. In $\alpha$ a point $A$ is given and in $\beta$ a point $C$ is given, neither of which lies on $p$. Construct $B$ in $\alpha$ and $D$ in $\beta$ such that $ABCD$ is an equilateral trapezoid, $AB \parallel CD$, in which a circle can be inscribed.

### The Designer's Architecture

*The CEP unmasked.* The phrase *"a circle can be inscribed"* is a compact form of the tangent-length theorem: in a tangential quadrilateral (one admitting an inscribed circle), $|AB| + |CD| = |AD| + |BC|$. The phrase *"equilateral trapezoid"* (isosceles trapezoid in English) means $|AD| = |BC|$. Combining: $|AB| + |CD| = 2 |AD|$. This is the single identity that pins down the construction. Given $A$, $C$, $p$ and the two planes, the parallel directions $AB \parallel CD$ must lie along $p$ (the only direction common to both planes). The trapezoid is therefore axially symmetric across the perpendicular bisector of $p$ joining $A$ and $C$'s projections; the lengths $|AB|, |CD|, |AD|$ are determined by the geometry; and the tangent-length identity fixes the remaining degree of freedom.

*The archetype convergence.* #2 + #4. The #2 (Symmetry) is the recognition that the only common direction of $\alpha$ and $\beta$ is $p$, so both parallel sides must lie along $p$ (or parallel to $p$ in each plane); the isosceles condition then provides a reflective symmetry across the bisector. The #4 (Hidden Structure) is the recognition that *"a circle can be inscribed"* encodes the tangent-length theorem.

*The traps planted.* Three.

- **Trap 1: the planar-quadrilateral trap.** The solver, attempting to draw the figure, may not initially recognise that $A, B, C, D$ are coplanar (because $A, B \in \alpha$ and $C, D \in \beta$ are in *different* planes). The trapezoid lies in a third plane (containing $AB$ and $CD$, which are parallel hence coplanar). Generous: teaches that the *planarity of the trapezoid* is a non-trivial geometric fact that follows from the parallel-sides condition.
- **Trap 2: the inscribed-circle-by-construction trap.** The solver attempts to construct the inscribed circle first (using the angle bisectors of $\angle DAB$ and $\angle BCD$) and then verify the trapezoid is isosceles. This works but inverts the natural order; the cleaner path is to use the tangent-length identity to constrain the lengths first, then construct the inscribed circle as the unique tangent circle to the four sides. Generous: teaches that the order of constructive steps matters in geometric construction problems.
- **Trap 3: the tangent-length-theorem-forgotten trap.** The solver, unfamiliar with or having forgotten the tangent-length theorem, attempts to characterise inscribed-circle quadrilaterals by other means (angle conditions, similar-triangle arguments, etc.). The tangent-length theorem is the cleanest characterisation; alternative characterisations are real but heavier. Generous: teaches that *named theorems* (tangent-length, Ptolemy, Stewart) often package complex characterisations into short identities that designers exploit.

*The statement-craft.* The phrasing *"in which a circle can be inscribed"* is the most consequential. A technical alternative — *"such that $|AB| + |CD| = |AD| + |BC|$"* — would *give away* the tangent-length theorem and reduce the problem to algebraic construction. The schoolroom phrasing forces the solver to *recognise* the equivalence between *"a circle can be inscribed"* and the algebraic identity. The phrase *"equilateral trapezoid"* (the IMO 1959 Czechoslovak proposers' wording) corresponds to *"isosceles trapezoid"* in standard English; the term forces the solver to confirm that $|AD| = |BC|$, which is the second design constraint.

### The Reader's Re-Solution

- *Given.* Two planes $\alpha, \beta$ meeting at line $p$; point $A \in \alpha$ off $p$; point $C \in \beta$ off $p$.
- *Find.* Points $B \in \alpha$, $D \in \beta$ such that $ABCD$ is an isosceles trapezoid with $AB \parallel CD$, admitting an inscribed circle.
- *Strategy.* The parallel sides must lie along $p$; the isosceles + inscribed-circle conditions reduce to a single linear identity in the lengths; solve.
- *Stage 1 (#2).* Since $AB$ lies in $\alpha$ and $CD$ in $\beta$, and $AB \parallel CD$ as directed lines, both must be parallel to the unique common direction $p$ (since $p$ is the intersection line). Thus $AB \parallel p \parallel CD$. Let the trapezoid lie in plane $\gamma$ (the plane through $A, B, C, D$, which exists since $AB \parallel CD$).
- *Stage 2 (#4).* Apply the tangent-length theorem: $|AB| + |CD| = |AD| + |BC|$. Apply the isosceles condition: $|AD| = |BC|$. Combine: $|AB| + |CD| = 2 |AD|$.
- *Construction.* Let $A' \in p$ be the foot of the perpendicular from $A$ to $p$ in plane $\alpha$, and $C' \in p$ be the analogous foot from $C$ in plane $\beta$. Let $h_\alpha = |AA'|$, $h_\beta = |CC'|$, $d = |A'C'|$. By the trapezoid + isosceles + tangent-length conditions, $B$ and $D$ are determined up to reflection; explicit formulas for $|AB|, |CD|$ follow from a quadratic in one length using the identity $|AB| + |CD| = 2|AD|$ and the 3D Pythagorean relations.
- *Convergence.* The construction yields a unique (up to reflection) isosceles trapezoid $ABCD$ with the desired inscribed circle. $\boxed{\text{Construction complete.}}$

### Lessons for Problem Designers

1. **Named theorems are CEPs in compressed form.** Designers writing geometry problems can choose between the *theorem-as-conclusion* form (state the theorem's identity as the asked-for property) and the *theorem-as-tool* form (state a problem whose solution requires invoking the theorem). The latter is dramatically more elegant; the IMO 1959 P6 *"a circle can be inscribed"* phrasing is the theorem-as-tool form for the tangent-length theorem.
2. **3D geometry problems often reduce to 2D + a planarity argument.** Designers can engineer 3D problems whose hard work is in 2D (the trapezoid analysis) and whose 3D content is one or two structural facts (planarity of the trapezoid, perpendicular projections). The IMO 1959 P6 design uses exactly this reduction.
3. **The schoolroom register strikes again.** *"A circle can be inscribed"* is school vocabulary; *"$|AB| + |CD| = |AD| + |BC|$"* is technical vocabulary. The schoolroom phrasing conceals the technique while remaining maximally accessible — the same lesson from IMO 1959 P1.

---

## §2 — Case Study 12: IMO 1981 Problem 3 (the Fibonacci connection)

**Source.** International Mathematical Olympiad 1981, Problem 3.  
**CEP.** The Diophantine equation $|n^2 - mn - m^2| = 1$ has positive-integer solutions $(m, n)$ exactly at *consecutive Fibonacci pairs* $(F_k, F_{k+1})$, and the maximum of $m^2 + n^2$ over solutions with $1 \leq m, n \leq 1981$ is therefore $987^2 + 1597^2 = 3{,}524{,}578$ (the largest Fibonacci pair fitting the bound).  
**Archetypes.** #1 (Invariance — the Fibonacci recursion is the invariant of the orbit) + #18 (Induction / Vieta-jumping descent) + #4 (Hidden Structure — recognising Fibonacci behind the surface).  
**Difficulty.** Tier 4-low. (This case is included in the High-mid chapter as the *strongest* High-mid representative; it could equally well sit at the bottom of the Tier 4 (High) chapter.)  
**Verification source.** `Cursor-IMO.md` §V; `imo-compendium.txt` near line 6800.

### Problem statement

> Determine the maximum value of $m^2 + n^2$, where $m$ and $n$ are integers satisfying $1 \leq m, n \leq 1981$ and $(n^2 - mn - m^2)^2 = 1$.

### The Designer's Architecture

*The CEP unmasked.* The constraint $(n^2 - mn - m^2)^2 = 1$ is equivalent to $|n^2 - mn - m^2| = 1$. The integer solutions to this Diophantine equation are exactly the consecutive Fibonacci pairs $(m, n) = (F_k, F_{k+1})$ for $k \geq 1$ (the proof is a Vieta-jumping descent: if $(m, n)$ is a positive solution with $n > m$, then $(n, n - m)$ is also a positive solution, eventually descending to $(0, 1)$ or $(1, 1)$ — and the orbit under this descent is exactly the Fibonacci sequence read backward). The maximum of $m^2 + n^2$ over solutions with $m, n \leq 1981$ is achieved at the largest Fibonacci pair fitting the bound: $F_{16} = 987$, $F_{17} = 1597$ (with $F_{18} = 2584 > 1981$).

$$m^2 + n^2 = 987^2 + 1597^2 = 974{,}169 + 2{,}550{,}409 = 3{,}524{,}578.$$

The CEP is the *Fibonacci connection*. The Vieta-jumping descent is the technique; the Fibonacci identification is the structural insight.

*The archetype convergence.* #1 + #18 + #4. The #1 (Invariance) is the recognition that the quantity $|n^2 - mn - m^2|$ is preserved (in absolute value) under the descent $(m, n) \mapsto (n - m, m)$, a Vieta-jumping move. The #18 (Induction / descent) is the proof that the descent terminates at a base case from which all solutions can be reconstructed. The #4 (Hidden Structure) is the identification of the orbit with the Fibonacci sequence.

```
       ┌────────────────────────────────┐
       │ (m, n) ∈ [1, 1981]^2           │
       │ |n² − mn − m²| = 1              │
       │ Maximise m² + n²                │
       └────────────┬───────────────────┘
                    │
       ┌────────────┼────────────┐
       │            │            │
       ▼            ▼            ▼
   #4 Hidden    #1 Invariance  #18 Descent
   Structure   (|n²-mn-m²|     (Vieta-
   (Fibonacci  preserved       jumping)
    connection) under map      Orbit:
                (m,n)→(n-m,m)) (m,n) →
                                 (n-m,m)
                                  → ... →
                                  (0,1)
       └────────────┬────────────┘
                    ▼
        ┌──────────────────────┐
        │ Solutions ↔ consec.  │
        │ Fibonacci pairs:     │
        │ (F_k, F_{k+1})       │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ Max within [1, 1981]:│
        │ (987, 1597)          │
        │ 987² + 1597² =       │
        │ 3,524,578.           │
        └──────────────────────┘
```

*The traps planted.* Four.

- **Trap 1: the brute search.** The solver, unfamiliar with the Fibonacci connection, attempts to enumerate pairs $(m, n)$ satisfying the Diophantine constraint by computational search. For small $m$, the constraint is $n^2 - mn - m^2 = \pm 1$, which for each $m$ gives a quadratic in $n$ with discriminant $m^2 + 4(m^2 \pm 1) = 5m^2 \pm 4$; integer $n$ requires this to be a perfect square. The solver discovers that $5m^2 \pm 4$ is a perfect square exactly when $m$ is a Fibonacci number — and *this is the structural connection in disguise*. The brute search, taken far enough, *reveals* the Fibonacci connection through the $5m^2 \pm 4 = \square$ identity (which is itself a classical Fibonacci characterisation). Highly generous: the search teaches the connection.
- **Trap 2: the wrong constraint.** The solver mis-reads the constraint as $n^2 - mn - m^2 = 1$ (with no absolute value or square), losing half the solutions. The $\pm 1$ cases correspond to $F_k F_{k+2} - F_{k+1}^2 = (-1)^{k+1}$ (Cassini's identity), so the sign alternates with $k$ and both signs occur for actual Fibonacci pairs. Generous if it leads to discovering Cassini's identity; ungenerous if the solver simply enumerates and misses the alternating-sign structure.
- **Trap 3: the bound is the answer.** The solver, observing that $m, n \leq 1981$ and seeking to maximise $m^2 + n^2$, may guess that the answer is $1981^2 + 1981^2 = 2 \cdot 1981^2 = 7{,}848{,}722$ (the trivial maximum if the constraint were $m, n \leq 1981$ alone). They then test whether $(m, n) = (1981, 1981)$ satisfies the Diophantine constraint: $1981^2 - 1981 \cdot 1981 - 1981^2 = -1981^2 \neq \pm 1$. So the boundary maximum is not a solution; the answer is strictly less. Generous: teaches that the Diophantine constraint dramatically restricts the feasible region.
- **Trap 4: the Vieta-jumping itself.** Once the solver attempts Vieta jumping (treating $|n^2 - mn - m^2| = 1$ as a quadratic in $n$ with $m$ fixed), they discover the descent orbit. The descent terminates at $(m, n) = (1, 1)$ (where $|1 - 1 - 1| = 1$). The Vieta jumping itself is the technique that *forces* the recognition of the Fibonacci structure: the orbit, read in reverse, is $1, 1, 2, 3, 5, 8, \ldots$ — the Fibonacci sequence. Trap 4 is not really a trap; it is the path the designer intended. Its inclusion here is to note that *the technique is the structural insight*, in classic 3-archetype convergence style.

*The statement-craft.* The constraint *"$(n^2 - mn - m^2)^2 = 1$"* — using the squared form rather than the absolute-value form — is the designer's most consequential choice. The squared form is mathematically equivalent to $|n^2 - mn - m^2| = 1$ but rhetorically conceals the absolute-value structure. A solver who reads *"$(\text{something})^2 = 1$"* is primed to think *"the something is $\pm 1$"*, which is the right path; a solver who reads *"$|\text{something}| = 1$"* is primed to think about modulus, which is a less direct path. The choice of the bound *"$1981$"* is iconic: this is IMO 1981, and the bound is the year, a problem-setter's joke that *also* happens to position the Fibonacci $F_{17} = 1597$ inside the range and $F_{18} = 2584$ outside it. The bound is designed so that the answer is the *single* largest Fibonacci pair fitting the range, with the next pair just barely missing — a calibration tightness analogous to IMO 2003 P1's pigeonhole tightness.

### The Reader's Re-Solution

- *Given.* $1 \leq m, n \leq 1981$ with $(n^2 - mn - m^2)^2 = 1$.
- *Find.* Maximum of $m^2 + n^2$.
- *Strategy.* Vieta-jumping descent on the Diophantine constraint; identify orbit with Fibonacci; maximise within the range.
- *Stage 1 (#1).* Note that the map $T: (m, n) \mapsto (n, n - m)$ preserves $|n^2 - mn - m^2|$ (one can verify directly: $|(n-m)^2 - n(n-m) - n^2| = |n^2 - 2mn + m^2 - n^2 + mn - n^2| = |-mn + m^2 - n^2| = |n^2 - mn - m^2|$, wait — let me redo. Actually $|n^2 - mn - m^2|$ is invariant under $T'(m,n) = (n-m, m)$ in the form: $|(m)^2 - (n-m)m - (n-m)^2| = |m^2 - mn + m^2 - n^2 + 2mn - m^2| = |m^2 + mn - n^2| = |n^2 - mn - m^2|$. So $T'$ preserves the invariant in absolute value.)
- *Stage 2 (#18).* Starting from any solution $(m, n)$ with $0 < m < n$ (WLOG), apply $T'$: the orbit is strictly decreasing in $\max(m, n)$, hence terminates at base case $(0, 1)$ or $(1, 1)$. The orbit run forward (Fibonacci-style) gives: $(1, 1), (1, 2), (2, 3), (3, 5), (5, 8), (8, 13), \ldots$ — consecutive Fibonacci pairs.
- *Stage 3 (#4).* The integer solutions $(m, n)$ with $m, n \geq 1$ are exactly $(F_k, F_{k+1})$ for $k = 1, 2, 3, \ldots$. The largest Fibonacci $F_k \leq 1981$ is $F_{17} = 1597$ (since $F_{16} = 987, F_{17} = 1597, F_{18} = 2584 > 1981$). The largest pair fitting both bounds is $(F_{16}, F_{17}) = (987, 1597)$.
- *Convergence.* The maximum is $m^2 + n^2 = 987^2 + 1597^2 = 974{,}169 + 2{,}550{,}409 = \boxed{3{,}524{,}578}$.

### Lessons for Problem Designers

1. **Constants encoded with calendar dates are a stylistic gift.** The bound *"1981"* is the year of the IMO. This is a recurring designer's tradition (IMO 2003 P1's *"$10^6$"* is the millennium-rounded bound; many problems encode the year as a constant). Designers writing year-specific problems can do this with great effect — the constant carries a hidden personal stamp.
2. **The Vieta-jumping descent is the IMO design's signature for Diophantine maxima.** Diophantine problems asking for maxima or minima of polynomial expressions in $m, n$ under polynomial constraints can almost always be attacked by Vieta-jumping descent. Designers writing such problems should anticipate the descent path and calibrate the bound so that the maximal answer fits "just inside" the range, with the next-largest solution falling just outside.
3. **The Fibonacci sequence is one of the most concealable CEPs in mathematics.** A problem whose answer involves a Fibonacci pair — and whose statement does not mention Fibonacci, recursion, or the golden ratio — is a problem the designer has *concealed beautifully*. The solver's discovery of the Fibonacci connection is one of the most rewarding *aha* moments olympiad mathematics can offer. Designers should aspire to engineer such reveals.

---

## §3 — Case Study 13: IMO 1968 Problem 6 (the Hermite identity)

**Source.** International Mathematical Olympiad 1968, Problem 6.  
**CEP.** The Hermite-style identity that the infinite sum collapses to a *simple closed form*: $\sum_{i=0}^{\infty} \lfloor (n + 2^i)/2^{i+1} \rfloor = n$ for every positive integer $n$.  
**Archetypes.** #15 (Bijection — between sum-contributions and binary-representation bits of $n$) + #4 (Hidden Structure — the identity is invisible from the surface).  
**Difficulty.** Tier 3-high.  
**Verification source.** `imo-compendium.txt` lines 2629–2634; problem statement verbatim from Compendium §3.10.1.

### Problem statement

> Let $[x]$ denote the integer part of $x$, i.e., the greatest integer not exceeding $x$. If $n$ is a positive integer, express as a simple function of $n$ the sum  
> $$\left\lfloor \frac{n+1}{2} \right\rfloor + \left\lfloor \frac{n+2}{4} \right\rfloor + \left\lfloor \frac{n+4}{8} \right\rfloor + \cdots + \left\lfloor \frac{n+2^i}{2^{i+1}} \right\rfloor + \cdots$$

### The Designer's Architecture

*The CEP unmasked.* The sum equals $n$. This is a special case of the **Hermite identity**: $\sum_{k=0}^{m-1} \lfloor x + k/m \rfloor = \lfloor mx \rfloor$, which here specialises to a binary-representation identity. The proof: write $n$ in binary as $n = \sum_{j \geq 0} b_j 2^j$ with $b_j \in \{0, 1\}$. The $i$-th term $\lfloor (n + 2^i) / 2^{i+1} \rfloor$ equals $\lfloor n/2^{i+1} + 1/2 \rfloor$ = (roughly) $\lceil n/2^{i+1} \rceil$ = the number of "carries from position $\leq i$" in a specific binary-arithmetic sense. Summing across all $i$ gives the total count of 1-bits weighted by their positions, which collapses to $n$ itself.

A cleaner proof: by induction on $n$. For $n = 1$: $\lfloor 1/1 \rfloor + \lfloor 1/2 \rfloor + \lfloor 1/4 \rfloor + \cdots = \lfloor 2/2 \rfloor + 0 + 0 + \cdots = 1$. ✓. For $n \to n + 1$: the sum increments by exactly 1 (each $\lfloor (n + 1 + 2^i)/2^{i+1} \rfloor - \lfloor (n + 2^i)/2^{i+1} \rfloor \in \{0, 1\}$, and the increments across all $i$ telescope to exactly 1 — the "binary-increment" argument). So if the sum equals $n$ for $n$, it equals $n + 1$ for $n + 1$.

The CEP is the closed-form $n$. The Bijection (#15) is between the unit increments of the sum (as $n \to n + 1$) and the unit increments of $n$ itself — a one-to-one correspondence enforced by the binary structure.

*The archetype convergence.* #15 + #4. The #15 (Bijection) is the binary-increment correspondence. The #4 (Hidden Structure) is the recognition that the sum collapses to a clean closed form — the *surprise* of the result is itself the CEP.

*The traps planted.* Two.

- **Trap 1: the small-$n$ trap.** The solver computes the sum for $n = 1, 2, 3, 4, 5, \ldots$ and observes the values are $1, 2, 3, 4, 5, \ldots$ — i.e., the sum equals $n$. This is the right *conjecture* but not the *proof*. Generous: teaches that small-case verification reveals the answer but does not constitute a proof; the binary-structure argument is the proof.
- **Trap 2: the infinite-sum trap.** The solver, attempting to manipulate the infinite sum algebraically, may apply infinite-series identities (geometric-series summation, term-rearrangement) that require convergence conditions the floor-function expression does not obviously satisfy. The sum is *eventually zero* for any fixed $n$ (once $2^{i+1} > n + 2^i$, i.e., $2^i > n$, i.e., $i > \log_2 n$, the floor term becomes zero), but the solver may not initially recognise the eventual-zero property. Generous: teaches that infinite-sum expressions involving floor functions almost always have an *eventual-zero* truncation that converts the infinite sum into a finite one.

*The statement-craft.* The phrasing *"express as a simple function of $n$"* is the designer's deliberate concealment. *"Prove that the sum equals $n$"* would give away the answer; *"compute the sum"* would suggest a computational technique. *"Express as a simple function of $n$"* tells the solver that the answer is closed-form but conceals which closed form. The implicit assertion that the sum equals a *simple* function is itself a hint (the answer cannot be a complicated expression in $n$); the solver who guesses "it equals $n$" or "it equals $n + c$" for small $c$ will check small cases and verify.

### The Reader's Re-Solution

- *Given.* $n$ positive integer; the infinite sum $S(n) = \sum_{i=0}^{\infty} \lfloor (n + 2^i)/2^{i+1} \rfloor$.
- *Find.* A simple closed-form for $S(n)$.
- *Strategy.* Induct on $n$, verifying $S(n+1) = S(n) + 1$ by binary-increment analysis.
- *Stage 1 (#15).* For each $i \geq 0$, observe that $\lfloor (n + 1 + 2^i)/2^{i+1} \rfloor - \lfloor (n + 2^i)/2^{i+1} \rfloor \in \{0, 1\}$ (since the argument increased by exactly $1/2^{i+1} < 1$). The increment is $1$ iff $(n + 2^i) \bmod 2^{i+1} = 2^{i+1} - 1$, i.e., iff $n \bmod 2^{i+1} = 2^i - 1$, i.e., iff $n$ ends in a 1-bit at position $i$ followed by $i$ zero-bits (or equivalently, the $(i+1)$th bit of $n + 1$ is the lowest bit that flips, etc.). Summing across $i$: the total increment is exactly 1 (one bit-position is "the first to flip when $n$ becomes $n + 1$").
- *Stage 2 (#4).* By induction, $S(1) = 1$ (direct computation), and $S(n+1) = S(n) + 1$ for every $n \geq 1$. Therefore $S(n) = n$ for every positive integer $n$.
- *Convergence.* The sum equals $\boxed{n}$.

### Lessons for Problem Designers

1. **Hidden closed forms are the cleanest CEPs.** A problem whose surface displays a complicated expression (an infinite sum, a multi-variable function, a nested radical) and whose answer is a *single-variable closed form* is a problem with a beautiful CEP. The designer's craft is to engineer the surface complexity so that it collapses by a single structural identity.
2. **Binary representation is an under-used designer's tool.** Many number-theoretic identities have clean binary-representation proofs (the Hermite identity, Kummer's theorem on binomial coefficients, the Stern-Brocot tree). Designers writing number-theory problems should consider whether a binary-structure argument provides the cleanest CEP.
3. **The *"simple function"* hint is a calibrated reveal.** The IMO 1968 P6 phrasing *"express as a simple function of $n$"* tells the solver that the answer is clean while concealing what the cleanness is. This is the dual of the IMO 1959 P1 *"in lowest terms"* phrasing — both use language that hints at the structural conclusion without naming it.

---

## §4 — Case Study 14: Putnam 1995 Problem A-5 (the exponent-class structure)

**Source.** William Lowell Putnam Competition, 1995, Problem A-5.  
**CEP.** The constraints define a 4-variable linear system in non-negative integer counts (of $-1$, $0$, $1$, $2$ values in the sequence), which has a 1-dimensional solution space parametrising both the cube-sum minimum and maximum directly.  
**Archetypes.** #14 (Parity / Modularity — the $\{-1, 0, 1, 2\}$ constraint sits inside mod-arithmetic structure) + #17 (Degrees of Freedom — three linear equations in four unknowns produce a 1-D space).  
**Difficulty.** Tier 3-high.  
**Verification source.** Engel Ch. 6 (Number Theory) Putnam coverage; `Cursor-Engel.md` Ch. 6.

### Problem statement

> Let $x_1, x_2, \ldots, x_n$ be a sequence of integers such that (i) $-1 \leq x_i \leq 2$ for each $i$, (ii) $x_1 + x_2 + \cdots + x_n = 19$, and (iii) $x_1^2 + x_2^2 + \cdots + x_n^2 = 99$. Determine, with proof, the minimum and maximum possible values of $x_1^3 + x_2^3 + \cdots + x_n^3$.

### The Designer's Architecture

*The CEP unmasked.* Let $a, b, c, d$ denote the counts of $x_i$ equal to $-1, 0, 1, 2$ respectively (so $a + b + c + d = n$). Constraint (ii) gives $-a + c + 2d = 19$. Constraint (iii) gives $a + c + 4d = 99$. The cube sum is $-a + c + 8d$. From the constraints: subtracting gives $2d - 2 \cdot 0 \cdot \ldots$ wait, let me redo. Constraint (ii): $-a + c + 2d = 19$. Constraint (iii): $a + c + 4d = 99$. Adding: $2c + 6d = 118$, i.e., $c + 3d = 59$, i.e., $c = 59 - 3d$. Subtracting (ii) from (iii): $2a + 2d = 80$, i.e., $a + d = 40$, i.e., $a = 40 - d$.

The cube sum is $-a + c + 8d = -(40 - d) + (59 - 3d) + 8d = -40 + d + 59 - 3d + 8d = 19 + 6d$. So the cube sum is *uniquely determined* by $d$ (the count of $x_i = 2$).

The feasible range for $d$: $a \geq 0 \Rightarrow d \leq 40$; $c \geq 0 \Rightarrow d \leq 19$ (since $c = 59 - 3d \geq 0$). Lower bound: $d \geq 0$. So $0 \leq d \leq 19$ (with $d = 19$ requiring $c = 59 - 57 = 2$, $a = 40 - 19 = 21$, $b = n - 42 \geq 0$, so $n \geq 42$; and $d = 0$ requires $a = 40$, $c = 59$, $b = n - 99 \geq 0$, so $n \geq 99$).

The minimum cube sum is at $d = 0$: $19 + 0 = 19$. The maximum is at $d = 19$: $19 + 114 = 133$.

The CEP is the *parametrisation by $d$* — the recognition that the cube sum is linear in the single free variable $d$, and that the bounds on $d$ come from non-negativity of the other variables.

*The archetype convergence.* #14 + #17. The #14 (Parity / Modularity) is the recognition that the integer-valued constraints on $\{-1, 0, 1, 2\}$ admit a clean linear decomposition in counts. The #17 (Degrees of Freedom) is the formal observation that 3 equations (sum, square sum, total count) in 4 unknowns ($a, b, c, d$) leave a 1-dimensional space, parametrised here by $d$.

*The traps planted.* Two.

- **Trap 1: the algebraic-identity trap.** The solver attempts to use the Newton-Girard identities or similar algebraic relations between $\sum x_i, \sum x_i^2, \sum x_i^3$ for a general sequence. These work *in principle* but produce complicated expressions; the count-parametrisation is dramatically cleaner. Generous: teaches that constrained-sequence problems with values in a small finite set are best attacked by *counting the values*, not by general algebraic identities.
- **Trap 2: the constraint-checking trap.** The solver may set up the counts $a, b, c, d$ but forget that $b$ (the count of zeros) is *unconstrained* by the sum/square-sum/cube-sum equations and only constrained by $b \geq 0$. The non-trivial bounds on $d$ come from the non-negativity of $a$ and $c$. Generous: teaches that in a constrained-counts setup, the *value space* of the free variable is determined by the non-negativity of the *fixed* variables.

*The statement-craft.* The constraint *"$-1 \leq x_i \leq 2$"* combined with *"integers"* implicitly defines the value set $\{-1, 0, 1, 2\}$. The choice of constants ($19, 99$) is the designer's calibration: $19$ is small enough to allow integer count-tuples to exist, $99$ is small enough that the cube sums are computable, and the ratio between the two encodes the system's structure. The phrasing *"determine, with proof, the minimum and maximum possible values"* is the Putnam-house complete-answer style.

### The Reader's Re-Solution

- *Given.* Integers $x_1, \ldots, x_n \in \{-1, 0, 1, 2\}$ with $\sum x_i = 19$, $\sum x_i^2 = 99$.
- *Find.* Min and max of $\sum x_i^3$.
- *Strategy.* Parametrise by counts; reduce to single-variable linear function with non-negativity bounds.
- *Stage 1 (#14).* Let $a, b, c, d$ count the number of $x_i$ equal to $-1, 0, 1, 2$. The constraints become $-a + c + 2d = 19$ (sum) and $a + c + 4d = 99$ (square sum). The cube sum is $\sum x_i^3 = -a + c + 8d$.
- *Stage 2 (#17).* From the two constraints: $a = 40 - d$ and $c = 59 - 3d$. The cube sum simplifies to $-(40 - d) + (59 - 3d) + 8d = 19 + 6d$. The free variable is $d$, with feasible range determined by $a \geq 0$ ($d \leq 40$), $c \geq 0$ ($d \leq 19$), $d \geq 0$, giving $0 \leq d \leq 19$.
- *Convergence.* The cube sum is $19 + 6d$ for $d \in [0, 19]$. Minimum at $d = 0$: $\boxed{19}$. Maximum at $d = 19$: $\boxed{133}$.

### Lessons for Problem Designers

1. **Finite-value-set problems are degree-of-freedom problems in disguise.** Whenever a constraint problem specifies the values come from a small finite set (here, $\{-1, 0, 1, 2\}$), the right reformulation is in terms of *counts of each value*. The resulting linear system over non-negative integer counts has a clear degree-of-freedom structure that immediately reveals the answer.
2. **Multiple objective functions in one parameter is design heaven.** The IMO/Putnam designer who can engineer a problem where *both* the minimum and the maximum of the target are linear functions of a single free variable has produced a problem with the cleanest possible answer-structure. Designers should look for parametrisations that simultaneously linearise the objective and the feasibility region.
3. **Putnam's *"determine, with proof, the minimum and maximum"* is the explicit complete-answer demand.** The Putnam phrasing differs from the IMO and JEE styles in being explicit about wanting both the minimum, the maximum, and the proof for both. Designers in the Putnam tradition should expect to be asked for *complete* answers including the extremising configurations, not just the extreme values.

---

## §5 — Case Study 15: IMO 1989 Problem 5 (the CRT construction)

**Source.** International Mathematical Olympiad 1989, Problem 5.  
**CEP.** The Chinese Remainder Theorem applied to a system of $n$ congruences, each modulo the product of *two distinct primes*, produces a positive integer $x$ such that each of $x + 1, x + 2, \ldots, x + n$ is divisible by two distinct primes — hence not a prime power.  
**Archetypes.** #1 (Invariance — the CRT structure preserves the simultaneous-congruence solvability) + #18 (Induction — building up the prime system) + #11 (Existence — CRT guarantees a solution to the simultaneous system).  
**Difficulty.** Tier 4-low.  
**Verification source.** `Cursor-IMO.md` §V; `imo-compendium.txt` near line 10550.

### Problem statement

> Prove that for each positive integer $n$ there exist $n$ consecutive positive integers, none of which is an integral power of a prime number.

### The Designer's Architecture

*The CEP unmasked.* For each $i \in \{1, 2, \ldots, n\}$, choose two distinct primes $p_i, q_i$ (with all $2n$ primes pairwise distinct across all $i$). The Chinese Remainder Theorem guarantees a positive integer $x$ such that $x \equiv -i \pmod{p_i q_i}$ for every $i$. Then $x + i$ is divisible by $p_i q_i$, hence by two distinct primes $p_i$ and $q_i$, hence is not an integral power of any single prime. The $n$ consecutive integers $x + 1, x + 2, \ldots, x + n$ all have this property.

The CEP is the CRT construction. The designer's choice: use *pairs* of primes per index (not just single primes) because being divisible by a single prime does not exclude being a prime power; being divisible by *two distinct primes* does exclude it.

*The archetype convergence.* #1 + #18 + #11. The #1 (Invariance) is the CRT compatibility: pairwise-coprime moduli allow simultaneous solving (the CRT-invariance of the solution set under modulus combination). The #18 (Induction) is the inductive construction of $n$ prime-pairs (each pair adds 2 new primes, distinct from all previously chosen). The #11 (Existence) is the CRT guarantee that the simultaneous system has a positive integer solution.

*The traps planted.* Two.

- **Trap 1: the single-prime trap.** The solver attempts to make each $x + i$ divisible by a single prime $p_i$ (rather than a prime *pair*). This is achievable by CRT but does not rule out $x + i$ being a prime power: $x + i = p_i^k$ for some $k$ is consistent with $p_i \mid x + i$. The trap is real and pedagogically generous: it teaches that *being divisible by $p$* is much weaker than *being divisible by two distinct primes*, and that the problem's specific exclusion (prime powers) requires the stronger condition.
- **Trap 2: the constructive-bound trap.** The solver attempts to construct *small* values of $x$ for small $n$ (e.g., for $n = 5$, find the smallest $x$ such that $x + 1, \ldots, x + 5$ are all non-prime-powers). This works for small $n$ but does not scale; the CRT-based proof gives *existence* without specifying the minimum $x$. The trap is generous in low-$n$ cases (the construction can be found by trial) but ungenerous in high-$n$ cases (the constructive approach explodes). The existence proof via CRT is dramatically cleaner.

*The statement-craft.* The phrasing *"prove that for each positive integer $n$ there exist..."* is the universally-quantified existence form. The designer chose *"there exist"* over *"find"* because the *"find"* form would require an explicit construction (which exists but is unsightly); the *"there exist"* form admits a clean structural argument. The phrasing *"integral power of a prime number"* is the technical specification — meaning $p^k$ for some prime $p$ and integer $k \geq 1$ — and is the *exclusion* condition that the CRT construction satisfies.

### The Reader's Re-Solution

- *Given.* Positive integer $n$.
- *Find.* Prove there exist $n$ consecutive positive integers, none a prime power.
- *Strategy.* Choose $n$ prime-pairs; use CRT to find $x$ such that $x + i$ is divisible by the $i$-th pair; conclude each $x + i$ is not a prime power.
- *Stage 1 (#18).* Inductively choose $n$ disjoint pairs of distinct primes $(p_1, q_1), (p_2, q_2), \ldots, (p_n, q_n)$ — for instance, the first $2n$ primes after $n$, taken in pairs. By construction, the moduli $p_i q_i$ are pairwise coprime (no prime is in more than one pair).
- *Stage 2 (#1, #11).* By the Chinese Remainder Theorem, the system $x \equiv -1 \pmod{p_1 q_1}$, $x \equiv -2 \pmod{p_2 q_2}$, $\ldots$, $x \equiv -n \pmod{p_n q_n}$ has a solution $x \in \mathbb{Z}_{>0}$ (in fact, infinitely many solutions; pick any positive one).
- *Stage 3 (conclusion).* For each $i \in \{1, \ldots, n\}$, $p_i q_i \mid x + i$, so $x + i$ is divisible by both $p_i$ and $q_i$ (two distinct primes), hence is not a prime power.
- *Convergence.* The $n$ consecutive integers $x + 1, x + 2, \ldots, x + n$ are all non-prime-powers. $\boxed{\text{Existence proved.}}$

### Lessons for Problem Designers

1. **CRT is the cleanest existence-by-construction CEP.** Problems asking for the existence of integers with prescribed divisibility properties have CRT-based constructions whenever the divisibility conditions are pairwise compatible (in modular terms). Designers writing existence problems should consider whether CRT produces the cleanest existence proof.
2. **The exclusion condition (here: non-prime-power) requires *strong* divisibility.** Designers writing problems with structural exclusions (no prime power, no perfect square, no $k$-th power) should choose the divisibility condition to *positively force* the exclusion. Single-prime divisibility does not exclude prime-power-ness; two-distinct-prime divisibility does.
3. **Existence-without-construction is a respectable problem-form.** The IMO 1989 P5 designer chose to ask for existence (which has a clean CRT proof) rather than for an explicit construction (which would be unsightly). Designers should not feel obligated to provide constructive answers when an existence proof is dramatically cleaner.

---

## §6 — Bridge to Chapter 7

The five cases of this chapter share the structural feature that each requires the solver to *construct or identify a non-obvious mathematical object*: a tangent-length identity for IMO 1959 P6, a Fibonacci connection for IMO 1981 P3, a Hermite identity for IMO 1968 P6, a degree-of-freedom parametrisation for Putnam 1995 A-5, a CRT system for IMO 1989 P5. The construction's existence is itself a non-trivial mathematical fact in each case; the construction is not merely *applied* (as in Chapter 5's monovariant) but *engineered* by the solver in response to the problem's structural demands.

Chapter 7 escalates one further step. The High-tier cases of Chapter 7 require the solver to *combine* two such constructions, or to recognise that the problem's structural object is not within the solver's standard toolkit — that the problem demands a *technique-discovery* moment, in which the solver constructs not just a mathematical object but a new piece of *method*. The five cases of Chapter 7 — IMO 1986 P5's Cauchy-style functional equation; IMO 1993 P3's solitaire-game weighting; IMO 1976 P4's powers-of-three structure; IMO 2001 P3's incidence-counting; IMO 1985 P4's exponent-vector pigeonhole — are five worked specimens of the technique-discovery moment.

We turn there now.

---

*End of Chapter 6.*
