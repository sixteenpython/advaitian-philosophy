---
chapter: 4
pillar: 4
chapter_type: case-study
title: "Case Studies 1–5: Moderate CEP"
subtitle: "The Polya Inventor's Paradox in five clean specimens."
length_target_words: 6500
canonical_takeaway: "Moderate-tier CEPs are not 'easy' — they are the clearest demonstration that elegant problem design is independent of difficulty tier."
status: locked
last_revised: 2026-05-29
locked_on: 2026-05-29
references_invoked: [IMO-1959-P1, IMO-1969-P1, Putnam-1985-A1, IMO-1972-P1, Joshi-Ch-24-Comment-8, Polya-Inventor's-Paradox]
voice_register: tao-warm
pillar3_cross_references: []
---

# Chapter 4 — Case Studies 1–5: Moderate CEP

> *"The more ambitious plan may have more chances of success."*  
> — G. Polya, *How to Solve It*, Part III §"Inventor's Paradox" (1957 ed., p. 121)

---

## §0 — Chapter Opening: What Makes a Moderate Problem Moderate

There is a temptation, on first reading the case-study chapters of a problem-design book, to assume that the *Moderate* tier is the *easy* tier — the chapter the serious reader should skim, the warm-up before the real material begins in the Hard tier. The temptation is to be resisted. The Moderate-tier case studies you will work through in this chapter are not warm-ups. They are, in many ways, the *clearest* demonstrations the pillar will offer of designer's craft, precisely because the technical machinery they invoke is light and the design choices are correspondingly visible. When you read IMO 1988 Problem 6 — the capstone of Chapter 8 — the technical depth of the Vieta-jumping technique can distract from the design choices that *led* the designer to choose Vieta jumping in the first place. When you read IMO 1959 Problem 1, there is no technical depth to distract. There is only the eighteen-word statement, the four planted traps, the two-step Euclidean closure, and the schoolroom register. Everything that distinguishes good design from bad is *visible*.

The five cases in this chapter are arranged in ascending order along two simultaneous axes: the *unfamiliarity* of the CEP (from the most-school-familiar gcd identity to the most-IMO-specific Sophie Germain factorisation) and the *archetypal complexity* (from clean 2-archetype convergences to convergences that lean on one archetype as the dominant move and a second as a quieter support). Three of the five cases are problems whose answer is, in one form or another, an *inventor's paradox* — *"no positive integer satisfies the equation,"* or *"the fraction is in lowest terms for every $n$,"* or *"there are infinitely many $a$ for which..."*. The Polya observation that ambition (of the assertion) often makes the assertion *easier* to prove will recur as the chapter's quiet through-line.

The fifth case is the *Indian-context anchor* — a problem from K.D. Joshi's *Educative JEE Mathematics*, Chapter 24 on inequalities. We end the chapter there because the AM-GM equality case it teaches is the most universally applicable Moderate-tier CEP in the entire pillar, and because the Joshi-treatment style is a genealogical thread that runs from the Indian school-mathematics tradition into the olympiad lineage we will inhabit for the rest of the pillar.

We begin.

---

## §1 — Case Study 1: IMO 1959 Problem 1

**Source.** International Mathematical Olympiad 1959, Problem 1.  
**CEP.** The Euclidean algorithm applied to $(21n+4,\ 14n+3)$ terminates in two reduction steps at $\gcd = 1$, with $n$-independent reduction coefficients.  
**Archetypes.** #14 (Parity / Modularity, in its Euclidean-algorithm specialisation) + #11 (Existence, in its non-existence specialisation).  
**Difficulty.** Tier 3-low.  
**Verification source.** `Cursor-IMO.md` §V; `imo-compendium.txt` near line 700; full anatomical treatment in this book's Chapter 2 §2.

### Problem statement

> Prove that, for every natural number $n$, the fraction $\frac{21n+4}{14n+3}$ is in lowest terms.

### The Designer's Architecture

The full four-axis analysis appears in Chapter 2 §2 and is not repeated in full here. The headline observations were:

*The CEP unmasked.* The Euclidean algorithm closes in exactly two reduction steps with reduction coefficients $1$ and $2$, both independent of $n$. The minimum constants for this property are $(21, 14, 4, 3)$ — the designer selected the smallest integers compatible with the two-step closure.

*The archetype convergence.* #14 + #11, with the convergence point being *"the Euclidean algorithm produces $\gcd = 1$ regardless of $n$."* The designer's choice of this archetype pair (rather than the alternative #14-only mod-$p$ approach, or the #5 substitution-and-parametrisation approach) is justified by the minimal-machinery criterion: the chosen pair shares the smallest common toolkit (the Euclidean algorithm itself) and converges *inside* that toolkit without external scaffolding.

*The traps planted.* Three. Brute-search confirmation (empirical evidence is not proof); attempted polynomial factorisation (the bilinears do not factor); attempted parametric simplification via the visible factor of $7$ (cosmetic, not operative).

*The statement-craft.* The schoolroom phrasing *"in lowest terms"* — rather than the technical *"$\gcd = 1$"* — is the single most consequential word-choice. It conceals the Euclidean algorithm from any solver who has not previously recognised the equivalence between *"in lowest terms"* and *"$\gcd = 1$"*, while remaining maximally accessible to the broadest student audience.

### The Reader's Re-Solution

- *Given.* The fraction $\dfrac{21n+4}{14n+3}$, for natural $n$.
- *Find.* Prove the fraction is in lowest terms — i.e., that $\gcd(21n+4,\ 14n+3) = 1$ — for every $n$.
- *Strategy.* Apply the Euclidean algorithm to the numerator and denominator, expecting termination at $1$ regardless of $n$.
- *Stage 1 (#14).* Reduce: $\gcd(21n+4,\ 14n+3) = \gcd(21n+4 - (14n+3),\ 14n+3) = \gcd(7n+1,\ 14n+3)$.
- *Stage 2 (#11).* Reduce again: $\gcd(7n+1,\ 14n+3) = \gcd(7n+1,\ 14n+3 - 2(7n+1)) = \gcd(7n+1,\ 1) = 1$.
- *Convergence.* The Euclidean algorithm has hit $1$ in two steps, independent of $n$. Therefore $\gcd(21n+4,\ 14n+3) = 1$ for every natural $n$, and the fraction is $\boxed{\text{in lowest terms for every } n}$.

### Lessons for Problem Designers

1. **The schoolroom phrasing conceals more than the technical phrasing.** A designer who wants to set a number-theory problem at the accessible end of the difficulty spectrum should use *"in lowest terms"* or *"a common factor of"* or *"divides evenly into"* rather than *"$\gcd$"* or *"$\equiv \pmod{n}$"*. The schoolroom register denies the solver the surface-level naming of the technique, forcing them to *discover* the technique's relevance.
2. **Minimum-constants design produces the shortest proof.** When the CEP is *"the Euclidean reduction closes in $k$ steps,"* the designer should search for the smallest integers compatible with the desired $k$. Larger constants do not produce a more sophisticated problem; they produce a more arithmetically tedious problem with the same structural content.
3. **Universal-quantifier problems are inventor's-paradox problems.** *"For every $n$..."* is more ambitious than *"for $n = 7$..."*. Polya's observation applies: the universal claim forces the structural argument that the existential claim would have allowed the solver to evade.

---

## §2 — Case Study 2: IMO 1969 Problem 1

**Source.** International Mathematical Olympiad 1969, Problem 1.  
**CEP.** The **Sophie Germain identity**: $n^4 + 4k^4 = (n^2 + 2nk + 2k^2)(n^2 - 2nk + 2k^2)$. Taking $a = 4k^4$ for any integer $k \geq 2$ produces an infinite family of values of $a$ for which $n^4 + a$ factors non-trivially for every $n$, hence is never prime.  
**Archetypes.** #4 (Hidden Structure — the Sophie Germain factorisation is invisible at the surface of the quartic) + #16 (Reverse Engineering — the designer works backward from "what shape of $a$ would force a factorisation?").  
**Difficulty.** Tier 3-mid.  
**Verification source.** `imo-compendium.txt` line 2784; problem statement verified verbatim from the Compendium.

### Problem statement

> Prove that there exist infinitely many natural numbers $a$ with the following property: the number $z = n^4 + a$ is not prime for any natural number $n$.

### The Designer's Architecture

*The CEP unmasked.* The Sophie Germain identity is a beautiful piece of nineteenth-century number theory that gives a non-trivial factorisation of $n^4 + 4k^4$ for any $k$. The designer chose this identity as the CEP because it provides an *infinite* family of $a$-values (namely $a = 4k^4$ for $k = 2, 3, 4, \ldots$) that satisfy the asked-for property, all at once, by a single structural identity. The problem's "infinitely many" requirement is *immediately* dispatched the moment the solver discovers Sophie Germain; before the discovery, the requirement looks like it might require sophisticated machinery (analytic number theory, perhaps, or a sieve argument).

*The archetype convergence.* #4 + #16. The #4 (Hidden Structure) move is the recognition that $n^4 + 4k^4$ admits a non-obvious factorisation; this is the *visible* archetype in the proof. The #16 (Reverse Engineering) move is the *designer's-side* archetype — the move by which the designer arrived at *"choose $a$ of the form $4k^4$"* rather than guessing. Read forward (solver-side), the proof uses #4 alone; read backward (designer-side), the choice of $a$-form is #16.

```
            ┌─────────────────────────────┐
            │ Find infinitely many a so   │
            │ that n^4 + a is never prime │
            └──────────────┬──────────────┘
                           │
       ┌───────────────────┴───────────────────┐
       │                                       │
       ▼                                       ▼
┌──────────────────────┐               ┌──────────────────────┐
│  #16 Reverse Eng     │               │  #4 Hidden Structure │
│  (designer's side)   │               │  (solver's side)     │
│                      │               │                      │
│  Ask: what shape of  │               │  Test: does n^4+4k^4 │
│  a would force a     │               │  factor? Yes:        │
│  factorisation for   │               │  (n^2+2nk+2k^2) ·    │
│  every n?            │               │  (n^2-2nk+2k^2)      │
└──────────┬───────────┘               └──────────┬───────────┘
           │                                      │
           └───────────────────┬──────────────────┘
                               ▼
                ┌──────────────────────────┐
                │  Convergence: Sophie     │
                │  Germain identity gives  │
                │  a = 4k^2 for all k >= 2 │
                └────────────┬─────────────┘
                             │
                             ▼
                ┌──────────────────────────┐
                │ Infinitely many a exist; │
                │ both factors > 1 for     │
                │ every n >= 1, k >= 2.    │
                └──────────────────────────┘
```

*The traps planted.* Two main traps.

- **Trap 1: the prime-density trap.** The solver attempts to bound the density of $a$-values such that $n^4 + a$ is composite for *all* $n$, via prime-counting or sieve heuristics. This is a substantial mathematical investment that leads nowhere — the bound either is not tight enough to give *infinitely many* or requires deeper analytic technology than the IMO toolkit. Generous trap: teaches that sometimes the structural answer (an explicit infinite family) is cleaner than the analytic answer.
- **Trap 2: the small-$a$ trap.** The solver computes $n^4 + a$ for $a = 1, 2, 3, \ldots$ and tries to identify by inspection which $a$ produce never-prime sequences. This brute search finds nothing useful (small $a$ tend to give prime values for small $n$) and consumes substantial time. Generous: teaches that the wanted family may live in a *parametrised* form rather than at small integer values.

*The statement-craft.* The choice of *"there exist infinitely many natural numbers $a$"* — rather than *"find all natural numbers $a$"* — is deliberate. The *"find all"* version would be a much harder problem (probably unsolved at IMO-1969 difficulty) because characterising every $a$ with the property requires far more machinery than producing infinitely many. The *"there exist"* version converts the problem into a *construction* problem: produce an infinite family. The Sophie Germain family is the simplest construction, and the *"there exist infinitely many"* phrasing *invites* the solver to look for a parametrised family rather than a complete characterisation.

### The Reader's Re-Solution

- *Given.* No specific data — the problem asks for an infinite family.
- *Find.* Infinitely many natural numbers $a$ such that $n^4 + a$ is composite for every natural $n$.
- *Strategy.* Find a structural identity that factors $n^4 + a$ non-trivially when $a$ takes a specific parametrised form; then verify both factors exceed $1$.
- *Stage 1 (#4).* Recall the Sophie Germain identity: $n^4 + 4k^4 = (n^2 + 2nk + 2k^2)(n^2 - 2nk + 2k^2)$. The identity is verified by direct expansion: $(n^2 + 2nk + 2k^2)(n^2 - 2nk + 2k^2) = (n^2 + 2k^2)^2 - (2nk)^2 = n^4 + 4k^4$.
- *Stage 2 (#16).* Set $a = 4k^4$ for any integer $k \geq 2$. The set $\{4 \cdot 2^4,\ 4 \cdot 3^4,\ 4 \cdot 4^4,\ldots\} = \{64,\ 324,\ 1024,\ldots\}$ is infinite.
- *Verification (the "both factors $> 1$" step).* For $k \geq 2$ and $n \geq 1$: the smaller factor is $n^2 - 2nk + 2k^2 = (n - k)^2 + k^2 \geq k^2 \geq 4 > 1$. The larger factor exceeds the smaller, hence also $> 1$.
- *Convergence.* For every $k \geq 2$ and every $n \geq 1$, $n^4 + 4k^4$ is the product of two integers each $> 1$, hence composite. Therefore there exist $\boxed{\text{infinitely many such } a}$, namely $a = 4k^4$ for $k = 2, 3, 4, \ldots$.

### Lessons for Problem Designers

1. **A known identity can be the CEP.** Designers often think CEPs must be novel insights; they need not be. A classical identity (Sophie Germain, the factorisation of $x^n - 1$, the AM-GM equality, the Pythagorean parametrisation) becomes a CEP the moment it is *concealed* behind a surface that does not name it. The designer's job is to find an asked-for property whose proof reduces to the identity.
2. **"Infinitely many" is easier than "find all."** The existential-quantifier framing converts a characterisation problem into a construction problem. The construction can use any single parametrised family; the characterisation requires *all* families. Designers who want a Moderate-tier inventor's-paradox problem should reach first for the *"there exist infinitely many"* framing.
3. **Reverse engineering is the designer's quiet partner.** Every Moderate-tier case has a designer-side archetype (typically #16) that the solver does not invoke but that *guided the designer* to the chosen problem. Naming this archetype in the case study makes the design's craft visible.

---

## §3 — Case Study 3: Putnam 1985 A-1

**Source.** William Lowell Putnam Competition, 1985, Problem A-1.  
**CEP.** Per-element independence: each of the 10 elements of $\{1, \ldots, 10\}$ has, independently of the others, exactly 6 valid membership profiles among the $2^3 = 8$ possible profiles into $(A_1, A_2, A_3)$. The answer is therefore $6^{10}$.  
**Archetypes.** #13 (Combinatorial — per-element independence) + #15 (Bijection — element ↔ membership-profile).  
**Difficulty.** Tier 3-mid.  
**Verification source.** Engel Ch. 1 (Invariance Principle); `Cursor-Engel.md` Ch. 1 anchor.

### Problem statement

> Determine, with proof, the number of ordered triples $(A_1, A_2, A_3)$ of subsets of the set $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$ such that $A_1 \cup A_2 \cup A_3 = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$ and $A_1 \cap A_2 \cap A_3 = \emptyset$.

### The Designer's Architecture

*The CEP unmasked.* The problem invites the reader to count *triples of sets* simultaneously satisfying a union constraint and an intersection constraint. The surface temptation is to attempt inclusion-exclusion on the set of all triples, or to enumerate by case analysis on the sizes of $A_1, A_2, A_3$. Both approaches are computationally heavy and conceptually obscure. The CEP is the recognition that the two constraints can be re-cast as *per-element constraints*: each element $i \in \{1, \ldots, 10\}$ either is or is not in each of $A_1, A_2, A_3$, giving $2^3 = 8$ membership-profile options per element; the union constraint excludes the all-zero profile (the element is in none of the three sets); the intersection constraint excludes the all-one profile (the element is in all three sets). This leaves $8 - 2 = 6$ valid profiles per element. The constraints are *independent across elements*, so the answer is $6^{10}$.

*The archetype convergence.* #13 + #15. The #13 (Combinatorial) move is the per-element independence. The #15 (Bijection) move is the implicit one-to-one correspondence between *triples of subsets satisfying both constraints* and *functions from $\{1, \ldots, 10\}$ to the 6-element set of valid membership profiles*. The bijection is what makes the per-element decomposition rigorous.

*The traps planted.* Three.

- **Trap 1: the inclusion-exclusion trap.** The solver attempts $|\{\text{triples with union} = \{1,\ldots,10\}\}| - |\{\text{triples with union} = \{1,\ldots,10\} \text{ and intersection} \neq \emptyset\}|$. The first term is computable via inclusion-exclusion at the *triple* level (count triples whose union misses a specific subset $S$, sum over $S$, alternate signs). The computation is tedious but tractable. The second term is much messier. Generous: teaches that the per-element decomposition is dramatically simpler than the triple-level decomposition, and that recognising this simplification is itself the problem.
- **Trap 2: the size-case trap.** The solver enumerates by sizes $|A_1|, |A_2|, |A_3|$. With ten possible sizes each, this is $11^3 = 1331$ cases, each requiring its own counting argument. Generous: teaches that case analysis at the wrong granularity (sets-as-objects rather than elements-as-objects) explodes.
- **Trap 3: the symmetry trap.** The solver notices the problem is symmetric under permutations of $(A_1, A_2, A_3)$ and attempts to count unordered triples first, then multiply by symmetry factors. The symmetry argument is correct but introduces overcounting corrections (when two of $A_1, A_2, A_3$ coincide) that are themselves non-trivial to enumerate. The simpler per-element decomposition avoids the symmetry calculation entirely. Generous: teaches that exploitable symmetry sometimes hides simpler symmetry-free arguments.

*The statement-craft.* The problem's explicit listing of $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$ — twice — is a Putnam stylistic convention (Putnam problem statements are notoriously precise to the point of redundancy). The size *ten* is deliberately *not large* — the answer is $6^{10} = 60{,}466{,}176$, a number small enough that the solver can verify (by partial enumeration for size-3 sets, say) without computational tools. Had the designer chosen size $100$, the answer would be $6^{100}$, which is correct but unwieldy; the size-$10$ choice keeps the answer human-scale while preserving the structural content.

### The Reader's Re-Solution

- *Given.* The set $S = \{1, 2, \ldots, 10\}$, with $|S| = 10$.
- *Find.* The number of ordered triples $(A_1, A_2, A_3)$ of subsets of $S$ such that $A_1 \cup A_2 \cup A_3 = S$ and $A_1 \cap A_2 \cap A_3 = \emptyset$.
- *Strategy.* Decompose at the element level rather than the set level.
- *Stage 1 (#13).* For each element $i \in S$, the *membership profile* of $i$ is $(b_1, b_2, b_3) \in \{0, 1\}^3$ where $b_j = 1$ iff $i \in A_j$. There are $2^3 = 8$ possible profiles.
- *Stage 2 (#15).* The constraint $A_1 \cup A_2 \cup A_3 = S$ requires each element to be in at least one set, so the profile $(0, 0, 0)$ is excluded. The constraint $A_1 \cap A_2 \cap A_3 = \emptyset$ requires no element to be in all three sets, so the profile $(1, 1, 1)$ is excluded. Each element therefore has $8 - 2 = 6$ valid profiles, independent of the choices for other elements.
- *Convergence.* The total number of valid triples is the number of functions from $S$ to the 6-element set of valid profiles: $6^{|S|} = 6^{10} = \boxed{60{,}466{,}176}$.

### Lessons for Problem Designers

1. **Per-element decomposition is the cleanest combinatorial CEP.** When a counting problem involves multiple objects (sets, sequences, functions) simultaneously satisfying constraints, ask: *can the constraints be re-cast as per-element constraints*? If yes, the per-element answer is almost always cleanest.
2. **The constraints' interaction is the design's centre of gravity.** Each constraint individually removes some profiles; the *combination* of constraints removes exactly two profiles (all-zero and all-one) in this case. Designers can construct families of similar problems by choosing which subsets of $\{0, 1\}^3$ to exclude — each choice gives a different answer-shape (e.g., excluding $\{(0,0,0), (1,1,1), (1,0,0)\}$ gives $5^{10}$, with a slightly more complex story).
3. **Putnam-style redundancy in statement-craft is itself a design choice.** The double-listing of $\{1, \ldots, 10\}$ in the original problem is not stylistic carelessness; it is the Putnam committee's signal that the problem is rigorously specified and that the solver should not look for ambiguities in the statement. Different competitions have different statement-craft conventions; Indian olympiad statements tend to be tighter, IMO statements are precision-optimised, Putnam statements are pedantically explicit. The conventional choice is itself meaningful.

---

## §4 — Case Study 4: IMO 1972 Problem 1

**Source.** International Mathematical Olympiad 1972, Problem 1.  
**CEP.** Pigeonhole at the right scale: $2^{10} = 1024$ subsets of a 10-element set, each with a sum bounded above by $10 \times 99 = 990$; by pigeonhole two distinct subsets share a sum; their symmetric difference produces two disjoint non-empty subsets with equal sum.  
**Archetypes.** #13 (Combinatorial — pigeonhole at the right scale) + #14 (Parity/Modularity — the symmetric-difference trim).  
**Difficulty.** Tier 3-mid.  
**Verification source.** `Cursor-IMO.md` §V; `imo-compendium.txt` near line 3400.

### Problem statement

> Prove that from a set of ten distinct two-digit numbers (in base 10), it is always possible to select two disjoint non-empty subsets whose members have the same sum.

### The Designer's Architecture

*The CEP unmasked.* The CEP is the precise calibration $2^{10} > 990$: the number of subsets of a 10-element set (namely $1024$) strictly exceeds the maximum possible sum of any subset (at most $10 \times 99 = 990$, since each element is at most $99$). By pigeonhole, two distinct subsets must share a sum. The two subsets are not yet disjoint; the symmetric difference removes their common elements, yielding two *disjoint* subsets whose sums are also equal (since equal sums minus equal removed elements remain equal).

The calibration is exact. The problem requires *two-digit* numbers (so the maximum element is $99$); it requires *ten* such numbers (so $2^{10} = 1024$ subsets); $1024$ exceeds $990$ by exactly $34$, just enough margin for the pigeonhole to bite. If the problem said *nine* numbers, $2^9 = 512 < 891$ and the pigeonhole would fail; if it said *one-digit* numbers (maximum $9$), $2^{10} = 1024 > 90$ and the pigeonhole would be trivial. The designer chose ten two-digit numbers precisely so that the calibration is non-trivial but works.

*The archetype convergence.* #13 + #14. The #13 (Combinatorial) move is the pigeonhole. The #14 (Parity/Modularity) move is the symmetric-difference trim: if two subsets $A$ and $B$ have equal sums, then so do $A \setminus (A \cap B)$ and $B \setminus (A \cap B)$ (both equal to the original sum minus the sum of $A \cap B$), and the trimmed subsets are disjoint by construction. The trim is, structurally, a Parity/Modularity move because it relies on the additive cancellation that defines the symmetric difference.

*The traps planted.* Two.

- **Trap 1: the wrong-pigeonhole trap.** The solver attempts to apply pigeonhole at the level of *individual elements* (e.g., "two of the ten numbers must share a digit") or at the level of *pairs*. Neither approach has the right counting balance to produce the desired conclusion. Generous: teaches that pigeonhole's power depends on choosing the right *pigeon-set* and *hole-set*, and that the right choice here is *subsets-as-pigeons*, *possible-sums-as-holes*.
- **Trap 2: the symmetric-difference-trivially-empty trap.** The solver applies pigeonhole, finds two subsets $A$ and $B$ with equal sums, and writes the conclusion *without trimming to disjoint subsets*. The IMO grader would deduct points: the problem requires *disjoint* subsets, and the pigeonhole gives only *distinct* subsets. The symmetric-difference trim is a necessary final step. Generous: teaches that the apparent answer from a pigeonhole argument often requires a small additional move to satisfy the literal problem statement.

*The statement-craft.* The phrasing *"in base 10"* — appearing in some translations of the IMO 1972 statement — is the most consequential clarification. The two-digit constraint depends on base; in another base the calibration would be different. The IMO committee chose to make the base explicit to remove ambiguity. The schoolroom phrasing *"two-digit numbers"* rather than *"integers in $[10, 99]$"* is, again, a register choice favouring accessibility.

### The Reader's Re-Solution

- *Given.* A set $T$ of ten distinct two-digit (base-10) numbers, $T = \{t_1, \ldots, t_{10}\}$ with $10 \leq t_i \leq 99$.
- *Find.* Prove there exist two disjoint non-empty subsets $X, Y \subseteq T$ with $X \cap Y = \emptyset$, $X, Y \neq \emptyset$, and $\sum_{x \in X} x = \sum_{y \in Y} y$.
- *Strategy.* Use pigeonhole on subsets-vs-possible-sums, then trim to disjoint via symmetric difference.
- *Stage 1 (#13).* The number of subsets of $T$ (including the empty set) is $2^{10} = 1024$. The sum of elements of any subset $S \subseteq T$ satisfies $0 \leq \sum_{s \in S} s \leq 10 \cdot 99 = 990$. So the number of *possible sum values* is at most $991$ (namely the integers in $[0, 990]$). Since $1024 > 991$, by pigeonhole there exist two *distinct* subsets $A, B \subseteq T$ with $A \neq B$ and $\sum_A = \sum_B$.
- *Stage 2 (#14).* Let $C = A \cap B$. Define $X = A \setminus C$ and $Y = B \setminus C$. Then $X \cap Y = \emptyset$ (by construction). Since $A \neq B$, at least one of $X, Y$ is non-empty; but $\sum_X = \sum_A - \sum_C = \sum_B - \sum_C = \sum_Y$, and the only way for a sum of distinct positive integers to be zero is for the set to be empty — so both $X$ and $Y$ are non-empty (if $X = \emptyset$ then $\sum_X = 0 = \sum_Y$ forces $Y = \emptyset$ too, contradicting $A \neq B$).
- *Convergence.* $X$ and $Y$ are the required disjoint non-empty subsets with equal sums. $\boxed{\text{Conclusion proven.}}$

### Lessons for Problem Designers

1. **Pigeonhole calibration is the design's centre of gravity.** A pigeonhole problem at the Moderate tier should have the *pigeons-to-holes ratio* slightly above 1 but not absurdly so. IMO 1972 P1's ratio is $1024/991 \approx 1.033$ — just enough margin to force the conclusion, narrow enough that the calibration looks like it might fail. Designers calibrating a new pigeonhole problem should target similar tightness.
2. **The trim is half the problem.** Every pigeonhole-by-subsets problem has a *trim step* (symmetric difference, or set difference, or some other set-theoretic move) that converts the *distinct-subsets* output of pigeonhole into the *disjoint-subsets* output the problem demands. Designers should anticipate this and not assume the trim is obvious.
3. **The base specification is non-cosmetic.** Problems that depend on base-10 representation must say so explicitly. A designer who omits the base specification has introduced a real ambiguity that competition graders may or may not penalise.

---

## §5 — Case Study 5: Joshi *Educative JEE Mathematics*, Chapter 24, Comment No. 8

**Source.** K.D. Joshi, *Educative JEE Mathematics: An Initiative to Empower the Aspirants and Inspire the Mentors*, Chapter 24 (Inequalities), Comment No. 8.  
**CEP.** The AM-GM equality case: $\sqrt[n]{x_1 x_2 \cdots x_n} \leq (x_1 + x_2 + \cdots + x_n)/n$, with equality if and only if $x_1 = x_2 = \cdots = x_n$. The maximum of the product subject to a fixed sum is therefore achieved at the unique equal-coordinate point.  
**Archetypes.** #10 (Inequality Constraints — AM-GM is the canonical inequality of olympiad mathematics) + #12 (Extremal — the maximum existence and characterisation).  
**Difficulty.** Tier 3-mid.  
**Verification source.** `Cursor-Joshi.md` Ch. 24 entry.

### Problem statement

> Let $S > 0$ be a fixed positive real and let $n$ be a fixed positive integer. Determine the maximum value of $x_1 x_2 \cdots x_n$ subject to $x_1, x_2, \ldots, x_n > 0$ and $x_1 + x_2 + \cdots + x_n = S$, and identify the point at which the maximum is attained.

### The Designer's Architecture

*The CEP unmasked.* The AM-GM inequality (Arithmetic Mean ≥ Geometric Mean) gives $(x_1 \cdots x_n)^{1/n} \leq (x_1 + \cdots + x_n)/n = S/n$, with equality iff $x_1 = \cdots = x_n = S/n$. The maximum of the product is therefore $(S/n)^n$, attained at the symmetric point. The CEP is the AM-GM equality case: the *equality condition* is the most consequential piece of the inequality (the inequality alone says "the maximum is at most $(S/n)^n$"; the equality condition completes the answer with *"and equality is achievable, here is the point"*).

*The archetype convergence.* #10 + #12. The #10 (Inequality Constraints) move is the direct application of AM-GM. The #12 (Extremal) move is the existence-and-characterisation step: AM-GM provides the upper bound, the equality case provides the attainment point, and together they characterise the maximum exactly. The convergence is the recognition that *the upper bound is tight*.

*The traps planted.* Three.

- **Trap 1: the calculus trap.** The solver, especially one trained in JEE Advanced calculus, applies Lagrange multipliers (or partial derivatives) to find the critical point of $f(x_1, \ldots, x_n) = x_1 \cdots x_n$ subject to $g(x_1, \ldots, x_n) = \sum x_i - S = 0$. The Lagrange computation does yield the symmetric point as the critical point, and the second-derivative test confirms it is a maximum. The trap is that this computational machinery is *correct but heavy*; the AM-GM proof is two lines, the Lagrange proof is twenty. Generous: teaches that competition problems often admit dramatically lighter proofs than the standard-curriculum-trained solver would attempt first.
- **Trap 2: the boundary trap.** The solver worries about boundary behaviour: what if some $x_i \to 0$? Then $x_1 \cdots x_n \to 0$, so the maximum cannot be on the boundary. Confirming this requires checking that the domain $\{x_i > 0, \sum x_i = S\}$ is bounded (which it is, but verifying this for $n$ variables takes some care) and that $f$ is continuous on the closure (which it is, with $f = 0$ on the boundary). The trap is real but mostly procedural; the AM-GM approach sidesteps it entirely. Generous: teaches that *globally clean* methods (AM-GM) often dispense with boundary worry that *locally analytic* methods (calculus) must address.
- **Trap 3: the case-by-case trap.** The solver, distrusting general arguments, attempts to verify the answer for $n = 2$, then $n = 3$, then $n = 4$, hoping a pattern will emerge. The pattern *does* emerge — the maximum is always $(S/n)^n$ at $x_i = S/n$ — but the pattern by itself is not a proof; the solver still needs the general AM-GM argument. Ungenerous if it consumes more than five minutes; teaches that small-case verification is a *sanity check* rather than a *proof*, and that even confident pattern recognition needs the universal argument.

*The statement-craft.* The phrasing is the standard Joshi-treatment register: precise, fully quantified, identifies *both* the maximum value and the maximising point. The Indian school-mathematics tradition (of which Joshi is a leading exponent) emphasises *complete answers* — a problem asking for a maximum is incomplete until both the value and the maximiser are stated. This is in contrast to some olympiad statements that ask only *"prove the maximum is at most $(S/n)^n$"* and leave the equality case as an exercise. The Joshi-style explicit demand for the maximiser is pedagogically valuable: it forces the solver to articulate the equality case, which is where the geometric meaning of AM-GM lives.

### The Reader's Re-Solution

- *Given.* $n$ positive reals $x_1, \ldots, x_n$ with sum $S > 0$ fixed.
- *Find.* The maximum of $P = x_1 \cdots x_n$ and the point at which it is achieved.
- *Strategy.* Apply AM-GM with equality characterisation.
- *Stage 1 (#10).* By AM-GM: $\sqrt[n]{x_1 \cdots x_n} \leq \dfrac{x_1 + \cdots + x_n}{n} = \dfrac{S}{n}$.
- *Stage 2 (#12).* Raising to the $n$-th power: $P = x_1 \cdots x_n \leq (S/n)^n$, with equality iff $x_1 = x_2 = \cdots = x_n$. Since the sum is $S$, the equality condition forces $x_i = S/n$ for every $i$.
- *Convergence.* The maximum value of $P$ is $\boxed{(S/n)^n}$, attained at the unique point $x_1 = x_2 = \cdots = x_n = S/n$.

### Lessons for Problem Designers

1. **The equality case is the CEP of every AM-GM-based problem.** AM-GM as an inequality is mathematics; AM-GM with its equality case is *design*. A problem that asks only for the inequality leaves the most pedagogically valuable part on the table.
2. **Symmetric optima at symmetric points.** The recurring CEP for "maximise / minimise a symmetric function under a symmetric constraint" is that the optimum occurs at the symmetric (equal-coordinate) point. Designers writing inequality problems for the Indian school-mathematics tradition should look first for symmetric-function-on-symmetric-domain structures.
3. **The Indian olympiad tradition prizes complete answers.** A Joshi-style problem statement explicitly asks for both the optimum *value* and the *point* at which the optimum is attained. Designers in this tradition should phrase their problems to demand both; designers in the IMO tradition can leave the equality case implicit. The choice between traditions is a curricular commitment.

---

## §6 — Bridge to Chapter 5

We have spent this chapter on five Moderate-tier specimens — *Moderate* in the sense that each problem's CEP can be discovered by a well-prepared Class-XII student or strong undergraduate within an hour of focused work; *Moderate* in the sense that each problem's convergence requires exactly two archetypes; *not* Moderate in the sense of being unimportant. The five cases together demonstrate that design discipline is independent of difficulty. The IMO 1959 P1 designer chose minimum constants and the schoolroom register; the IMO 1969 P1 designer used the Sophie Germain identity to convert a *"find infinitely many"* requirement into a single parametrised family; the Putnam 1985 A-1 designer engineered a problem whose per-element decomposition is the only honest approach; the IMO 1972 P1 designer calibrated a pigeonhole within a 3% margin; the Joshi designer wrote a complete-answer problem in the Indian-school tradition that teaches AM-GM equality as the central insight.

Each chapter from now on ascends one tier. Chapter 5 brings us five Mid-difficulty CEPs — problems whose archetype convergences are still two-archetype but whose CEPs require a longer chain of insight, often involving a non-trivial intermediate construction (a monovariant, a radical axis, a fixed point). The five cases of Chapter 5 begin with the legendary IMO 1986 Problem 3, the *pentagon-vertex monovariant* — perhaps the cleanest illustration in the entire IMO archive of how a single well-chosen monovariant can rescue a problem that, by the surface, looks intractable.

We turn there now.

---

*End of Chapter 4.*
