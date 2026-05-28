# Cursor-Zeitz.md — Consolidated Memory of Paul Zeitz's *The Art and Craft of Problem Solving* (3rd ed., 2017)

*Persistent reference file. Built so that future sessions need not re-read the full 384-page Zeitz PDF. When working on **Pillar 3** (Multidirectional Solving) and **Pillar 4** (CEP-Based Problem Design) of the Advaitian Book, this file is the **primary lookup** for Zeitz content; the raw text `my_references/art-and-craft-problem-solving.txt` is the **secondary verification source**.*

**Book metadata.**
- Title: *The Art and Craft of Problem Solving*, Third Edition
- Author: Paul Zeitz (University of San Francisco; member of the 1974 USA IMO team — the first USA team ever; coach of the 1994 USA IMO team which achieved the only perfect performance in IMO history)
- Publisher: John Wiley & Sons, 2017
- ISBN: 978-1-119-23990-1
- Length: ~384 pages (preface + 9 chapters + references + index)
- Chapters: 9 — Chapters 1–4 are **meta-pedagogy / cross-cutting techniques**; Chapters 5–9 are **subject-specific tools** (algebra, combinatorics, number theory, geometry, calculus)
- Source files: `my_references/Art and Craft of Problem Solving 3E.pdf` (canonical, 3.1 MB), `my_references/art-and-craft-problem-solving.txt` (searchable extraction via `pdftotext -layout`, 22,197 lines, 182,900 words)
- Text-file line ranges: main book lines 639–~21,560; references 21,570; index 21,669+

**Voice/pedagogy signature.** Zeitz writes in a **warm, conversational, missionary-for-problem-solving-culture** register that is the *third pole* of our reference corpus (along with Joshi's discursive Indian-academic register and Engel's terse German-rigorous register). He uses extended analogies (mountaineering, mice escaping cages, gym-rat vs. backpacker) to make psychological and meta-cognitive points; he is explicit about meta-cognition in a way that neither Joshi nor Engel are; and he is openly autobiographical (drawing on his Stuyvesant + USA IMO + USF teaching arc). His three opening epigraphs — "Get lost, get obsessed, get together" — set the philosophical tone of the entire book.

**Critical difference from Joshi and Engel.** Joshi is *topic-organised* (algebra, geometry, calc, ...); Engel is *technique-organised* (invariance, coloring, extremal, ...). **Zeitz is a hybrid:**
- Chapters 1–4 are **strategy / tactic-organised** (the three-layer model: strategies → tactics → crossover tactics)
- Chapters 5–9 are **topic-organised** (algebra, combinatorics, number theory, geometry, calculus = the "tools")

This hybrid structure is the textbook embodiment of Zeitz's famous **three-layer model** (Ch. 1.2: "The Three Levels of Problem Solving"), which the Advaitian Blueprint §7.2 explicitly maps onto our 5-pillar architecture:

| Zeitz layer | Zeitz chapter location | Advaitian mapping (per Blueprint §7.2) | Pillar |
|---|---|---|---|
| **Strategies** (psychological + orientation moves) | Ch. 2 | Multidirectional protocol / Six-Point Framework's *meta-moves* | Pillar 1 + Pillar 3 (First-Minute Protocol, Escape-Hatch) |
| **Tactics** (broadly applicable methods: symmetry, extreme, pigeonhole, invariants) | Chs. 3–4 | The **20 Archetypes** of Pillar 2 + the **multidirectional moves** of Pillar 3 | Pillars 2 + 3 |
| **Tools** (subject-specific techniques: algebra, combo, NT, geometry, calc) | Chs. 5–9 | The **Mathematical Gems** of Pillar 5 | Pillar 5 |

This makes Zeitz uniquely valuable as a **structural ancestor** of our entire 5-pillar architecture. The book's pedagogical scaffold is the closest published precedent for what we are building.

**Version.** 1.0 — May 28 2026 (initial consolidated extraction, all 9 chapters surveyed; Pillar 3 multi-archetype goldmine + Pillar 4 CEP-design goldmine both populated).
**Maintenance rule.** When a Pillar 3 or Pillar 4 chapter pulls a Zeitz problem, append the problem citation to §V (Pillar 3 goldmine) or §VIII (Pillar 4 goldmine) below with the chapter-of-use note.
**Status.** Comprehensive baseline. All 9 chapters surveyed for technique-content, competition-source breakdown, archetype-mapping, multi-archetype convergence problems (Pillar 3), and CEP-anchored problems (Pillar 4).

---

## I. Chapter-by-Chapter Index

| # | Title | Pages | Text-file lines | Zeitz layer | Pillar 2 primary archetype(s) | Pillar 3 weight | Pillar 4 weight |
|---|---|---|---|---|---|---|---|
| 1 | What This Book Is About and How to Read It | 1–11 | 639–1231 | Meta (intro) | — (frames the 3-layer model) | **MED** — the 3-layer model itself | LOW |
| 2 | Strategies for Investigating Problems | 12–57 | 1232–3943 | **Strategies** | — (meta-archetypal) | **HIGHEST** — First-Minute Protocol's intellectual ancestor lives in §2.1–§2.2 | MED |
| 3 | Tactics for Solving Problems | 58–104 | 3944–6631 | **Tactics** | #2 Symmetry, #12 Extremal, #13 Combinatorial (pigeonhole), #1 Invariance, #14 Parity, #18 Recursion (monovariant) | **HIGH** — 4 archetypes treated in one chapter = convergence-rich | MED |
| 4 | Three Important Crossover Tactics | 105–142 | 6632–8842 | **Crossover Tactics** | #8 Domain Translation (graph theory, complex numbers, generating functions = three domain-translations), #15 Bijection | **HIGHEST** — §4.4 Games is the locked source for Pillar 3 Ch. 6 Case Study #2 | MED |
| 5 | Algebra | 143–188 | 8843–11613 | **Tools** | #4 Hidden Structure, #5 Substitution, #10 Inequality, #1 Invariance (Vieta) | MED | **HIGH** — many CEP-designed algebra problems |
| 6 | Combinatorics | 189–223 | 11614–13748 | **Tools** | #13 Combinatorial, #15 Bijection, #14 Parity, #18 Recursion | MED-HIGH — many 2-archetype combo problems | **HIGH** — Czech/Slovak 1995 (Ex 6.1.1), USAMO/Putnam combo |
| 7 | Number Theory | 224–257 | 13749–15736 | **Tools** | #14 Parity/Modularity, #1 Invariance (Fermat), #16 Reverse Engineering (descent) | MED | **HIGH** — NT is a CEP-rich subject (perfect square, gcd, primes) |
| 8 | Geometry for Americans | 258–315 | 15737–19050 | **Tools** | #2 Symmetry, #8 Domain Translation (vectors, complex, transformations), #3 Duality, #1 Invariance | MED | **HIGH** — Power of a Point, Centroid, etc. are CEP-anchored |
| 9 | Calculus | 316–354 | 19051–21569 | **Tools** | #6 Linearisation, #11 Existence (continuity, MVT), #5 Substitution | LOW-MED | MED — fewer JEE/IMO problems, more conceptual |

---

## II. Chapter Details

### Chapter 1: What This Book Is About and How to Read It (pp. 1–11; lines 639–1231)

**Topic summary.** Zeitz frames the entire book around the distinction between an *exercise* (the path to the solution is apparent; only mechanical work remains) and a *problem* (the path is *not* apparent and requires investigation). He then introduces the **three levels of problem solving** (§1.2) — the book's most important organising concept — and presents a "Problem Sampler" (§1.3) of teaser problems from later chapters.

**Key concepts established.**
- **Exercise vs. Problem distinction** (§1.1): the foundational pedagogical move.
- **The Three Levels of Problem Solving** (§1.2): Strategies → Tactics → Tools. This is the conceptual ancestor of the Advaitian 5-pillar architecture.
- **Problem Sampler** (§1.3): teaser problems from each later chapter.

**Pillar 4 relevance.** Zeitz's "exercise vs. problem" distinction is the foundational distinction Pillar 4 will deepen into "exercise vs. designed problem" — i.e., a problem designed around a CEP is what makes investigation worth doing.

---

### Chapter 2: Strategies for Investigating Problems (pp. 12–57; lines 1232–3943)

**Topic summary.** Zeitz's **Strategies** are *psychological and orientation moves* — the meta-cognitive operations a solver performs *before* and *between* tactical moves. The chapter has four sections: §2.1 Psychological Strategies (mental toughness, creativity); §2.2 Strategies for Getting Started (orientation, the *I'm-oriented-now-what?* loop); §2.3 Methods of Argument (deduction, contradiction, induction); §2.4 Other Important Strategies (draw a picture, recast the problem, change point of view).

**Key principles/themes.**
- **Pólya's Mouse** (§2.1): never give up at first failure; vary the trials. The book's central motivational fable.
- **Mental toughness** = confidence + concentration; both grow with deliberate practice.
- **"Just because a problem seems impossible does not mean that it is impossible. Never admit defeat after a cursory glance."** (Zeitz's most-quoted maxim.)
- **Wishful thinking** (§2.1): a deliberate creative move — solve an easier version first.
- **The make-it-easier strategy**: "If the given problem is too hard, solve an easier one."
- **Penultimate step** (§2.2): work backward from the goal one step.
- **Wishful thinking + penultimate step** combine into a *bidirectional search* — this is **the embryonic form of multidirectional solving that Pillar 3 formalises.**
- **Argument by contradiction** (§2.3.3): foundational proof method.
- **Mathematical induction** (§2.3.4): strong, weak, double, ascending/descending.

**Worked examples — Ch. 2.**
- *Example 2.1.1.* The software-interview crossing-paths problem (three boxes labelled A, B, C must be connected without crossings). Solution by *wishful thinking + make-it-easier*: rearrange labels mentally, solve easy version, then "push" each label back to its original position. **A teaching example for §2.1.**
- *Example 2.1.9.* The **Affirmative Action problem** (color a graph's vertices black/white so each vertex has at least as many opposite-color neighbours as same-color). Foreshadows graph theory (Ch. 4). **Solved by the *extreme principle*.**
- *Example 2.4.3.* The **Gallery problem** — a network of pipes problem reformulable via graph theory.

**Pillar 3 multi-archetype gold (HIGHEST in book for Pillar 3 meta-protocol).**
Zeitz's §2.2 "Strategies for Getting Started" is the **direct intellectual ancestor of Pillar 3's First-Minute Protocol (§7.7)**. His "orientation" step, "wishful thinking", "penultimate step", and "make-it-easier" are the four ancestral moves that we have consolidated into the 5-step, 60-second First-Minute Protocol. Pillar 3 Ch. 4 (the First-Minute Protocol chapter) should explicitly acknowledge Zeitz's §2.2 as its origin.

---

### Chapter 3: Tactics for Solving Problems (pp. 58–104; lines 3944–6631)

**Topic summary.** Zeitz's **Tactics** are *broadly applicable mathematical methods that simplify problems across multiple subject areas*. Four big tactics, each a section:

| § | Tactic | Maps to Pillar 2 archetype |
|---|---|---|
| 3.1 | Symmetry | **#2 Symmetry** (primary) |
| 3.2 | The Extreme Principle | **#12 Extremal Principles** (primary) |
| 3.3 | The Pigeonhole Principle | **#13 Combinatorial** (primary) |
| 3.4 | Invariants | **#1 Invariance** (primary), with sub-sections on parity, modular arithmetic & coloring (= **#14**), and monovariants (= a special case of #1 / #12) |

**This single Zeitz chapter covers the same conceptual territory as Engel's Chapters 1, 2, 3, and 4 *combined*.** It is denser and pedagogically more compact than Engel's treatment, with more meta-commentary on *why* each tactic works.

**Key principles/themes.**
- **Symmetry as a search for order** (§3.1): "harmony is even vaguer than our formal definition, but it is not without value. Look for harmony, and beauty, whenever you investigate a problem."
- **Symmetry's three questions** (§3.1, geometric symmetry): (1) Is it present? (2) If not, can it be imposed? (3) How can it be exploited?
- **Reflection as a problem-solving move** (§3.1, Example 3.1.5 — the "carry water to Grandma" optimal-distance problem): a calculus-heavy problem solved in 3 lines by reflecting Grandma across the stream. **A canonical Pillar 2 Ch. 2 (Symmetry) cross-reference.**
- **The extreme principle as a "free lunch"** (§3.2): "by focusing on the largest and smallest entities within a problem", we get free information.
- **Pigeonhole's three tiers** (§3.3): Basic (n+1 → n), Intermediate (qs+1 → s with mean ≥ q+1), Advanced (a real-valued version, Dirichlet approximation).
- **Invariants = monovariants ∪ true invariants** (§3.4): the distinction Engel makes implicitly is explicit here.

**Worked examples — Ch. 3 (highlights).**
- *Example 3.1.4.* The "square inscribed in circle inscribed in square" area-ratio problem. Solved in 2 lines by rotating the inner square 45° to align with tangent points. **CEP: 1/2.**
- *Example 3.1.5.* "Carry water to Grandma": YBG' is the straight line → answer = 13 miles (hypotenuse of 5-12-13). **CEP: 13 (a Pythagorean triple — this is a Tier-2 CEP per Blueprint §8.2.)**
- *Example 3.2.1 (Affirmative Action).* Re-treated formally with the extreme principle.
- *Examples 3.3.x.* Pigeonhole at all three tiers, with USAMO/Putnam citations.
- *Examples 3.4.x.* Invariants in chessboard problems, mod-arithmetic problems, monovariant termination.

**Pillar 3 multi-archetype gold.**
- **§3.1 + §3.2 in tandem** (symmetry + extreme): many problems use symmetry to *identify* the extreme element, then extremal-exploitation closes the proof. A natural **#2 + #12** convergence — direct Pillar 3 Ch. 2 worked-example candidate.
- **§3.3 + §3.4** (pigeonhole + invariant/parity): many pigeonhole problems use parity/mod arguments to define the boxes. Natural **#13 + #14** convergence.

**Pillar 4 CEP relevance.**
- Example 3.1.4 has CEP = 1/2 (a Tier-2 ratio CEP).
- Example 3.1.5 has CEP = 13 (Pythagorean triple, Tier-2).
- Many of Zeitz's worked examples have **explicit, identifiable CEPs**, making them direct Pillar 4 case study candidates.

---

### Chapter 4: Three Important Crossover Tactics (pp. 105–142; lines 6632–8842)

**Topic summary.** A *crossover* is an idea that connects two or more different branches of mathematics in a surprising way. The three crossovers:

| § | Crossover | Connects | Pillar 2 archetype |
|---|---|---|---|
| 4.1 | Graph Theory | Discrete relationships → networks; recasting combinatorial problems as graph problems | **#8 Domain Translation** + **#13 Combinatorial** |
| 4.2 | Complex Numbers | Plane geometry ↔ complex algebra; trigonometry ↔ unit-circle algebra | **#8 Domain Translation** + **#2 Symmetry** |
| 4.3 | Generating Functions | Counting problems → polynomial/formal-power-series algebra | **#8 Domain Translation** + **#15 Bijection** |
| 4.4 | **Interlude: A Few Mathematical Games** | Combinatorial games as a "playground" — Nim, P/N positions, Sprague-Grundy | **#12 Extremal** + **#16 Reverse Engineering** |

**Key concepts established.**
- **Graph theory toolkit**: vertices, edges, degree, handshake lemma, connected components, trees, leaves, Eulerian/Hamiltonian walks.
- **The handshake lemma**: in any graph, $\sum_v d(v) = 2|E|$.
- **Trees**: connected and acyclic; have $v - 1$ edges; have at least 2 leaves.
- **The Two Men of Tibet** problem (§4.1): a classic worked example.
- **Complex numbers as plane geometry** (§4.2): rotation = multiplication by $e^{i\theta}$; reflection = conjugation.
- **Roots of unity** (§4.2): $\omega = e^{2\pi i/n}$, the algebraic toolkit for cyclic problems.
- **Generating functions** (§4.3): $\sum a_n x^n$ encodes a sequence as a polynomial; combinatorial identities become algebraic identities.
- **Recurrence relations via generating functions** (§4.3).
- **Mathematical games** (§4.4): Nim, Wythoff, the Sprague-Grundy theory; P-positions and N-positions; pairing strategies.

**Worked examples — Ch. 4 (highlights).**
- *Example 4.1.1 (USAMO 1986).* Five mathematicians fall asleep twice each; every pair overlaps at least once → some three overlap simultaneously. Solved by graph-theory recasting + cycle-existence argument. **A canonical Pillar 3 multi-archetype example: #8 (Domain Translation to graphs) + #13 (counting cycles) + #11 (existence).**
- *Example 4.2.x.* Trigonometric identities via roots of unity.
- *Example 4.3.x.* The Fibonacci closed-form derived via generating functions.
- *§4.4 Mathematical Games.* Multiple game-theoretic problems; **the locked source for Pillar 3 §7.9 Case Study #2.**

**Pillar 3 multi-archetype gold (HIGHEST).**
- Every Ch. 4 worked example combines **#8 Domain Translation** with at least one other archetype. This is the textbook example of multidirectional solving: the crossover tactic *is* a multidirectional move by definition.
- **§4.4 (Mathematical Games)** is the locked source for the §7.9 Case Study #2 *n-coloring with no monochromatic AP-3* problem. The specific problem will be selected at Phase 0 from Zeitz §4.4 + the broader §3.4 invariant-coloring discussions.

**Pillar 4 CEP relevance.**
- *USAMO 1986* (Example 4.1.1): CEP = *"some 3 overlap"* — an existence-type CEP, perfect for a Pillar 4 Ch. 5 case study (Cases 6-10, Mid CEP). Note: this problem already appears in our Pillar 4 §8.9 slate's *style* (an Olympiad existence problem) — it could be a substitute for one of the candidate-level cases (7, 8, 9, 10).

---

### Chapter 5: Algebra (pp. 143–188; lines 8843–11613)

**Topic summary.** Zeitz's "tool" treatment of algebra: sets/numbers/functions; algebraic manipulation (the factor tactic, manipulating squares, substitutions); sums/products/series (arithmetic, geometric, telescoping, infinite); polynomials (operations, zeros of a polynomial); inequalities (fundamental ideas, AM-GM, massage / Cauchy-Schwarz / Chebyshev).

**Key principles/themes.**
- **The Factor Tactic** (§5.2): when in doubt, factor. The book's most-cited algebraic move.
- **Manipulating Squares** (§5.2): completing the square, sum-of-squares decompositions.
- **The Telescoping Sum Tool** (§5.3): $\sum (a_n - a_{n-1}) = a_N - a_0$.
- **AM-GM and friends** (§5.5): foundational inequalities, including "Massage" (a Zeitz term for inequality manipulation that's distinctive to him), Cauchy-Schwarz, Chebyshev.

**Worked examples — Ch. 5 (highlights).** Many JEE/IMO/Putnam-style algebra problems; many use the factor tactic + substitution combo.

**Pillar 4 CEP relevance.** Algebra is rich in CEP-anchored problems: identity-like CEPs (the $z = 2(x^2 + xy + y^2)^2$ identity for IMO 1969 P1 — which is already our Pillar 4 Case Study 2 — has direct Zeitz §5.2 cross-reference). Many "factor tactic" worked examples in §5.2 have explicit CEPs.

---

### Chapter 6: Combinatorics (pp. 189–223; lines 11614–13748)

**Topic summary.** Permutations, combinations, Pascal's triangle, binomial theorem, partitions, bijections, Inclusion-Exclusion (PIE), recurrence (Fibonacci, Catalan).

**Key principles/themes.**
- **The Mississippi Formula** (§6.1.10): a Zeitz-named formula for permutations of a multiset (named after the example word MISSISSIPPI).
- **Counting strategies and tactics** (§6.1): a meta-section that re-invokes the 3-layer model within combinatorics.
- **Counting subsets** (§6.2): bijections to binary strings, lattice paths, etc.
- **Information management** (§6.2): the meta-principle that good combinatorial reasoning is about *what to count* and *how to encode it*.
- **Balls in urns** (§6.2): the classic encoding of "k indistinguishable balls into n distinguishable urns" = $\binom{n+k-1}{k}$.
- **PIE in three flavors** (§6.3): with sets, with indicator functions, with complements.
- **Recurrence via combinatorial bijection** (§6.4): the Fibonacci recurrence from tiling; the Catalan recurrence from triangulations / paths.

**Worked examples — Ch. 6 (highlights).**
- *Example 6.1.1 (Czech & Slovak 1995).* Decide whether there exist 10,000 ten-digit numbers divisible by 7, all of which can be obtained from one another by reordering their digits. **Solved on p. 204.** A perfect 2-archetype problem: **#13 Combinatorial + #14 Parity/Modularity (divisibility by 7)**. **Direct Pillar 3 Ch. 2 worked-example candidate.**

**Pillar 4 CEP relevance.** Combinatorics problems often have CEPs that are *specific numeric counts* — perfect for Pillar 4 design exercises. The Catalan recurrence (CEP = $C_n = \binom{2n}{n}/(n+1)$) is an extreme-tier CEP per Blueprint §8.2.

---

### Chapter 7: Number Theory (pp. 224–257; lines 13749–15736)

**Topic summary.** Primes and divisibility (FTA, gcd, Euclidean algorithm); congruences (Fermat's Little Theorem); number-theoretic functions (divisor sums, Euler's φ, Möbius μ); Diophantine equations (general strategy and tactics); miscellaneous instructive examples (sums of two squares, Fermat-via-combinatorics).

**Key principles/themes.**
- **The FTA** (§7.1) — unique prime factorisation as the foundational theorem.
- **Example 7.1.2 — the "even integers as universe"** counterexample showing why FTA is non-trivial. **A canonical Pillar 4 "designed counterexample".**
- **Fermat's Little Theorem** (§7.2) with a **combinatorial proof** (§7.5) via necklace counting — same combinatorial proof Engel gives.
- **A combinatorial proof of FLT** (§7.5): "If you can count it, it's an integer."
- **Sums of two squares** (§7.5): when is $n = a^2 + b^2$? — the Fermat / Gauss classification.
- **Diophantine equations** (§7.4): general strategy and tactics — includes infinite descent, factoring, mod-arithmetic.

**Worked examples — Ch. 7 (highlights).**
- Numerous Putnam, IMO, USAMO NT problems with explicit factor-tactic + parity + descent combinations.

**Pillar 4 CEP relevance (HIGHEST).** NT is the *richest source of CEPs* in the entire reference corpus, because every classical result is a CEP-in-disguise:
- Perfect square (Tier-2 CEP) → IMO 1959 P1, IMO 1988 P6, and many Zeitz §7.x problems.
- Pythagorean triple (Tier-2 CEP) → Zeitz §7.5 "sums of two squares".
- $0$ as unique solution (Extreme-tier CEP) → Diophantine descent problems throughout §7.4.

---

### Chapter 8: Geometry for Americans (pp. 258–315; lines 15737–19050)

**Topic summary.** A pedagogically-warm catch-up chapter for readers (often American per Zeitz's wry observation) who haven't done much geometry. Includes: three "easy" problems as diagnostic; survival geometry (points/lines/angles/triangles, parallels, circles); the power of elementary geometry (concyclic points, area + cevians, similar triangles, phantom points); transformations (rigid motions + vectors, homothety, inversion).

**Key principles/themes.**
- **Three "Easy" Problems** (§8.1) as diagnostic: Power of a Point Theorem (POP), Angle Bisector Theorem, Centroid Theorem (medians intersect at 2:1 ratio).
- **The Power of a Point Theorem** (§8.1.1) — Pillar 4 case-study material; this is a classical CEP-anchored theorem.
- **Concyclic Points** (§8.4) — Ptolemy's theorem ancestor.
- **Area + Cevians + Concurrent Lines** (§8.4) — Ceva's and Menelaus's theorems territory.
- **Phantom Points and Concurrent Lines** (§8.4) — a remarkable Zeitz construction: introduce a *phantom point* defined by the desired property, prove it coincides with the actual point.
- **Transformations** (§8.5) — rigid motions, homothety, inversion. Felix Klein's transformational view of geometry, accessibly introduced.

**Pillar 4 CEP relevance (HIGH).** Geometry is dense with CEP-anchored theorems: POP, Angle Bisector, Centroid 2:1, Ptolemy, Ceva, Menelaus, etc. Several of these are direct cross-references for Pillar 4 case studies (e.g., Case Study 7 = IMO 1995 P1 = concyclic / tangent geometry → maps to Zeitz §8.4).

---

### Chapter 9: Calculus (pp. 316–354; lines 19051–21569)

**Topic summary.** Convergence and continuity (sequences, series, uniform continuity); differentiation and integration; power series and "Eulerian Mathematics".

**Key principles/themes.**
- **Convergence** (§9.2) — limits of sequences, series convergence tests.
- **Uniform continuity** (§9.2) — a precise treatment, important for rigorous analysis.
- **The Mean Value Theorem** (§9.3) — a Pillar 2 #11 (Existence) cross-reference.
- **Eulerian Mathematics** (§9.4) — a Zeitz-named section celebrating Euler-style formal manipulations (e.g., $\zeta(2) = \pi^2/6$ via $\sin x$ infinite product).
- **The Quest for a Moving Curtain** (§9.4) — Zeitz's poetic name for an interpolation / asymptotic problem.

**Pillar 4 CEP relevance.** Calculus is the most CEP-poor of the tools chapters in the Zeitz pedagogical hierarchy — it tends to be subject-driven rather than CEP-driven. However, §9.4 (Eulerian mathematics) contains extreme-tier CEPs ($e^{i\pi} + 1 = 0$, etc.).

---

## III. Master Index by Competition

Zeitz cites competitions extensively but with a different bias than Engel — Zeitz emphasises USAMO and Putnam (his teaching context) while Engel emphasises IMO and Eastern European olympiads (his teaching context). Combined, the two books cover the global olympiad culture nearly exhaustively. Approximate citation count by source:

| Competition | Approx. citation count in Zeitz | Notable problems |
|---|---|---|
| **USAMO** | ~25+ | USAMO 1986 (Ex 4.1.1 — five mathematicians overlap) |
| **Putnam** | ~20+ | Multiple per chapter, especially Chs. 3, 5, 6, 7, 9 |
| **IMO** | ~15+ | Various |
| **Czech & Slovak** | 2+ | Czech & Slovak 1995 (Ex 6.1.1 — 10,000 ten-digit numbers) |
| **Russia/Soviet** | 5+ | Various |
| **Hungary** | 4+ | Various Kürschák problems |
| **Folklore / "I learned this from..."** | 10+ | Distinctive Zeitz citation style for math-circle folklore |

**Total competition-citation density**: 74 lines matched the IMO/USAMO/Putnam citation pattern via a quick filter; the true count is higher when math-circle folklore and unnamed contests are included.

---

## IV. Master Index by Pillar 2 Archetype

For each of the 20 archetypes, the Zeitz chapters/sections where it lives:

| Archetype | Zeitz primary location | Strength of fit |
|---|---|---|
| **#1 Invariance** | §3.4 (Invariants — primary), §7.2 (FLT as invariance) | Primary in §3.4 |
| **#2 Symmetry** | §3.1 (Symmetry — primary), §8.5 (geometric transformations) | Primary in §3.1 |
| **#3 Duality** | §8.4 (concyclic, pole-polar implicit) | Secondary |
| **#4 Hidden Structure** | §5.2 (factor tactic + manipulating squares), §5.4 (zeros of polynomial), §7.5 (FLT combinatorial proof) | Primary in §5.2 |
| **#5 Substitution** | §5.2 (substitutions & simplifications — primary) | Primary |
| **#6 Linearization** | §9.3 (differentiation as linearisation) | Secondary |
| **#7 Normalisation** | §5.5 (inequality homogenisation) | Weak |
| **#8 Domain Translation** | **§4.1 (graphs)**, **§4.2 (complex)**, **§4.3 (generating functions)** — *primary, all of Ch. 4* | **Primary in Ch. 4** |
| **#9 Domain Constraints** | Diffuse throughout | Weak |
| **#10 Inequality Constraints** | §5.5 (inequalities — primary) | Primary |
| **#11 Existence/Uniqueness** | §9.2 (continuity, MVT) | Secondary |
| **#12 Extremal Principles** | §3.2 (extreme principle — primary), §4.4 (game-theory P/N positions) | Primary in §3.2 |
| **#13 Combinatorial Principles** | §3.3 (pigeonhole — primary), Ch. 6 (combinatorics — primary) | Primary in §3.3 and Ch. 6 |
| **#14 Parity/Modularity** | §3.4 (parity, modular arithmetic & coloring — primary) | Primary in §3.4 sub-section |
| **#15 Bijection/Correspondence** | §6.2 (partitions & bijections — primary), §6.4 (bijective Fibonacci/Catalan derivations) | Primary in §6.2 |
| **#16 Reverse Engineering** | §2.2 (penultimate step — *the embryonic form*), §4.4 (game-theory backward induction), §7.4 (Diophantine descent) | Primary in §2.2 / §4.4 |
| **#17 DOF Analysis** | Not explicit | Weak |
| **#18 Recursion/Induction** | §2.3.4 (mathematical induction), §3.4 (monovariants), §4.3 (recurrences), §6.4 (combinatorial recurrence) | Diffuse but strong |
| **#19 Pivoting/Elimination** | §5.2 (substitution as elimination), implicit in NT | Weak |
| **#20 Analogy/Transfer** | Implicit in §1.2 (the 3-layer model itself is a transfer principle) | Diffuse |

---

## V. Pillar 3 Multi-Archetype Convergence Index — GOLDMINE FOR PILLAR 3

This is the **Pillar 3 goldmine section**, curated specifically for Pillar 3 case-study mining. Every entry below is a Zeitz problem where the exposition explicitly or implicitly invokes 2 or 3 archetypes simultaneously. Combined with `Cursor-Engel.md` §V (Engel's multi-archetype problems), these are the primary candidates for Pillar 3 Ch. 1–7 worked examples and Ch. 6 case studies.

### 2-Archetype Convergence Problems (for Pillar 3 Ch. 2)

| Problem | Source (Zeitz) | Archetypes | Notes |
|---|---|---|---|
| **Czech & Slovak 1995** — 10,000 ten-digit numbers divisible by 7, permutations of one another | **Ex 6.1.1** (line 11620), solution on p. 204 | #13 Combinatorial + #14 Parity (mod 7) | Excellent 2-archetype Pillar 3 Ch. 2 candidate |
| **Carry Water to Grandma** | **Ex 3.1.5** (line 4096) | #2 Symmetry (reflection across stream) + #8 Domain Translation (geometric reformulation) | A 3-line solution to an apparent calculus problem; Pillar 3 Ch. 4 First-Minute Protocol illustration |
| **Square-inscribed-in-circle-inscribed-in-square area ratio** | **Ex 3.1.4** (line 4059) | #2 Symmetry (45° rotation) + #4 Hidden Structure | CEP = 1/2; excellent Pillar 3 Ch. 1 simplicity-of-multidirectional illustration |
| **Affirmative Action problem** | Ex 2.1.9 (line ~1700) / re-treated §3.2 | #12 Extremal + #13 Combinatorial (graph coloring) | Classical 2-archetype graph problem |
| **The Gallery problem** | Ex 2.4.3 (line ~2700) | #8 Domain Translation (recast as graph) + #13 Combinatorial | Pipe-network as graph; Pillar 3 Ch. 5 (MVC) illustration |
| **Trees have leaves** | §4.1 (line ~6790) | #12 Extremal (longest path) + #15 Bijection (path-endpoints argument) | A clean elementary 2-archetype proof |
| **Tree edge-vertex relation** $|E| = |V| - 1$ | §4.1 (line ~6803) | #18 Induction + #12 Extremal (pick a leaf) | A canonical 2-archetype induction proof |

### 3-Archetype Convergence Problems (for Pillar 3 Ch. 3 + Ch. 6)

| Problem | Source (Zeitz) | Archetypes | Notes |
|---|---|---|---|
| **USAMO 1986 — Five mathematicians fall asleep twice each** | **Ex 4.1.1** (line 6680) | #8 Domain Translation (recast as graph) + #13 Combinatorial (10 vertices + 10 edges) + #11 Existence (must have cycle) | **Direct Pillar 3 Ch. 3 WE2 candidate** — a 3-archetype problem with very clean structure |
| **The combinatorial proof of FLT** (necklace argument) | §7.5 (line ~14600+) | #14 Parity/Modularity + #13 Combinatorial + #18 Induction (or #1 Invariance) | The "one theorem, multiple proofs" Pillar 3 Ch. 5 MVC illustration; aligns with Engel's three-proof FLT treatment |
| **§4.4 Mathematical Games — n-coloring with no monochromatic AP-3 territory** | **§4.4** (line ~8500+) | #14 Parity (coloring) + #13 Combinatorial + #18 Induction (construction) | **LOCKED as Pillar 3 §7.9 Case Study #2** per Blueprint §7.9 |
| **Diophantine equations via the three-method combo** | §7.4 | #14 Parity (mod) + #4 Hidden Structure (factor) + #16 Reverse Engineering (descent) | Generic 3-archetype Diophantine treatment |

### Forward-Reference to §7.9 Case Study Slate (UPDATED v0.2)

| § | Case Study | Zeitz source | Engel cross-ref | Tier |
|---|---|---|---|---|
| 1 | Engel's classical pigeonhole (5 points in unit square) | Not in Zeitz (Engel-only) | Cursor-Engel §V row 1 | 2 |
| 2 | **Zeitz no-monochromatic-AP-3 coloring** | **Zeitz §4.4 (Mathematical Games) + §3.4 (coloring discussions)** | — | 3 |
| 3 | Putnam convex polygon partition (year TBD) | Not specifically in Zeitz; Putnam-archive sourced | — | 3 |
| 4 | IMO shortlist combinatorics (extremal + descent + parity) | Generic Zeitz §3.2 + §7.4 techniques | Cursor-Engel §V Diophantine row | 4 |
| 5 | Engel functional equation (subst + induction + parity) | Not in Zeitz (Engel-only) | Cursor-Engel Ch. 11 | 4 |

---

## VI. Notable Theorems & Named Results

Zeitz, like Engel, introduces or restates many classical results. Distinctive Zeitz nomenclature is in **bold**:

- **The Three Levels of Problem Solving** (Strategies / Tactics / Tools) — §1.2 — the book's structural ancestor of our 5-pillar architecture
- **Pólya's Mouse** — §2.1 — the central motivational parable
- **The Make-It-Easier Strategy** — §2.1
- **Wishful Thinking** — §2.1
- **The Penultimate Step** — §2.2
- **The Three Tiers of Pigeonhole** (Basic, Intermediate, Advanced) — §3.3
- **The Mississippi Formula** — §6.1.10
- **Information Management** (as a meta-counting principle) — §6.2
- **Massage** (a Zeitz term for inequality manipulation) — §5.5
- **The Power of a Point Theorem (POP)** — §8.1.1
- **The Angle Bisector Theorem** — §8.1.2
- **The Centroid Theorem (2:1)** — §8.1.3
- **Phantom Points** (Zeitz construction) — §8.4
- **The Quest for a Moving Curtain** (Zeitz term for interpolation) — §9.4
- **Eulerian Mathematics** (Zeitz's celebration of Euler-style formal manipulation) — §9.4
- **The Three Epigraphs** ("Get lost, get obsessed, get together") — front matter; the book's spiritual motto

Classical results re-treated in Zeitz: FTA (§7.1), Euclid's infinitude of primes (§7.1), Fermat's Little Theorem (§7.2 + §7.5 combinatorial proof), AM-GM (§5.5), Cauchy-Schwarz (§5.5), Mean Value Theorem (§9.3), Power of a Point (§8.1.1), Ceva's & Menelaus's theorems (§8.4 territory), inversion (§8.5).

---

## VII. Voice Register Samples for Pillar 3 + Pillar 4 Drafting

Zeitz's voice is the **third pole** of our reference corpus (Joshi = discursive Indian-academic; Engel = terse German-rigorous; **Zeitz = warm-conversational-missionary**). For Pillars 3 and 4, Zeitz's voice is especially relevant because both pillars require psychological / meta-cognitive register that Joshi and Engel rarely deploy.

**Sample 1 — Zeitz's signature "mountaineering analogy" for problem-solving difficulty (Ch. 2 opening):**
> "Solving a problem is not unlike climbing a mountain. And for inexperienced climbers, the task may seem daunting. The mountain is so steep! There is no trail! You can't even see the summit! If the mountain is worth climbing, it will take effort, skill, and, perhaps, luck. Several abortive attempts (euphemistically called 'reconnaissance trips') may be needed before the summit is reached."

This is Zeitz's distinctive register — **physical, embodied, slightly self-deprecating, missionary**. Pillar 3 should adopt this register for the *§0 Opening Vignettes* of each chapter (Indian-context analogues to Zeitz's mountaineering analogy).

**Sample 2 — Zeitz on the gym-rat vs. backpacker distinction (Preface to First Edition):**
> "The average (non-problem-solver) math student is like someone who goes to a gym three times a week to do lots of repetitions with low weights on various exercise machines. In contrast, the problem solver goes on a long, hard backpacking trip. Both people get stronger. The problem solver gets hot, cold, wet, tired, and hungry. The problem solver gets lost, and has to find his or her way. The problem solver gets blisters. The problem solver climbs to the top of mountains, sees hitherto undreamed of vistas. The problem solver arrives at places of amazing beauty, and experiences ecstasy that is amplified by the effort expended to get there."

Pillar 4 Ch. 1 ("The Problem as Art Object" — the Lockhart-register chapter) should explicitly invoke this passage. The "gym-rat vs. backpacker" distinction is the prose-poetic ancestor of our "exercise vs. CEP-designed problem" distinction.

**Sample 3 — Zeitz's confidence-maxim (Example 2.1.1, page 14):**
> "Just because a problem seems impossible does not mean that it is impossible. Never admit defeat after a cursory glance. Begin optimistically; assume that the problem can be solved. Only after several failed attempts should you try to prove impossibility. If you cannot do so, then do not admit defeat. Go back to the problem later."

This is Zeitz at his most pedagogically direct. Pillar 3 Ch. 7 (Escape-Hatch Architecture) should explicitly cite this maxim as the *philosophical underpinning* of the three Escape-Hatch moves (Archetype Nudge, Direction Map, Pivot Shadow).

**Sample 4 — Zeitz on harmony as a search principle (§3.1 Symmetry):**
> "An informal alternate definition of symmetry is 'harmony.' This is even vaguer than our 'formal' definition, but it is not without value. Look for harmony, and beauty, whenever you investigate a problem. If you can do something that makes things more harmonious or more beautiful, even if you have no idea how to define these two terms, then you are often on the right track."

Pillar 4's aesthetic vocabulary should be calibrated to this register — *harmony, beauty, elegance* as concrete search heuristics, not just decorative descriptions. Zeitz authorises the use of aesthetic vocabulary in mathematical argument.

**Sample 5 — Zeitz's autobiographical voice (Preface to Third Edition):**
> "In 2011, I was asked to write the forward to Stuyvesant High School's annual Math Survey magazine. My essay, 'The Three Epigraphs,' discussed the quotes at the front of the first two editions of this book, and my plan for the third edition's quote, if there were to be a third edition. I have kept my promise, and now there really are three epigraphs."

Zeitz openly invites the reader into his teaching biography. Pillar 4 Ch. 1 ("I" voice per Blueprint §8.6) and Ch. 9 ("I"+"we" voice) should follow this register — autobiographical, warm, openly invested in the book's success as a pedagogical artefact.

---

## VIII. Pillar 4 CEP-Design Goldmine — NEW SECTION FOR PARALLEL BUILD

This section is **unique to `Cursor-Zeitz.md`** (no analogue in Cursor-Engel or Cursor-Joshi) and is **curated specifically for Pillar 4 case-study mining and design-exercise inspiration**. Every entry below is a Zeitz problem with an explicit, identifiable Central Elegant Point (CEP) at the centre of the solution — making it a direct Pillar 4 case-study candidate or substitute.

### CEP-Anchored Problems by CEP Tier (per Blueprint §8.2)

#### Tier 2 (Moderate) CEPs in Zeitz

| Zeitz source | Problem | CEP | Archetypes | Pillar 4 case-slot candidate |
|---|---|---|---|---|
| §3.1.4 | Square-inscribed-in-circle-inscribed-in-square area ratio | **1/2** (simple ratio CEP) | #2 + #4 | Ch. 4 (Cases 1-5, Moderate) — possible substitute for Case 5 (JEE Adv) |
| §3.1.5 | Carry Water to Grandma | **13** (Pythagorean triple) | #2 + #8 | Ch. 4 — design-exercise candidate (Pillar 4 Ch. 9 design 1, given CEP = 7) |
| §8.1.1 | Power of a Point Theorem | **PX·PY = const** (invariant product) | #1 + #2 + #3 | Ch. 4 (Cases 1-5) — possible substitute |
| §8.1.2 | Angle Bisector Theorem | **CD/DB = AC/AB** (ratio identity) | #2 + #4 | Ch. 4-5 substitute candidate |
| §8.1.3 | Centroid Theorem (2:1) | **2:1 ratio at concurrence** | #2 + #11 | Ch. 4-5 substitute candidate |

#### Tier 3 (Hard) CEPs in Zeitz

| Zeitz source | Problem | CEP | Archetypes | Pillar 4 case-slot candidate |
|---|---|---|---|---|
| Ex 6.1.1 (Czech & Slovak 1995) | 10,000 ten-digit numbers div by 7, permutations | **Existence of such a family** (counting CEP) | #13 + #14 | Ch. 5 (Cases 6-10, Mid CEP) — strong candidate to substitute Case 5 (JEE Adv) |
| Ex 4.1.1 (USAMO 1986) | Five mathematicians overlap | **Some 3 overlap simultaneously** (existence CEP) | #8 + #13 + #11 | Ch. 5 (Cases 6-10) — strong candidate; aligns well with existing Case 6, 7, 8 archetype profiles |
| §4.4 game-theory P-positions | Various Nim-like games | **Golden-ratio-based P-position formulas (Wythoff)** | #12 + #16 + #18 | Ch. 6-7 candidate |
| §7.5 — Sums of two squares | When is $n = a^2 + b^2$? | **$n$ is a sum of two squares iff every prime $p \equiv 3 \pmod 4$ appears with even exponent in $n$** (a classification CEP) | #14 + #4 + #18 | Ch. 6 (Cases 11-15, High-mid CEP) — possible substitute or supplement |

#### Tier 4 (Extreme) CEPs in Zeitz

| Zeitz source | Problem | CEP | Archetypes | Pillar 4 case-slot candidate |
|---|---|---|---|---|
| §6.4 (Catalan recurrence) | $C_n$ from ballot problem / triangulations / Dyck paths | **Catalan number $C_n = \binom{2n}{n}/(n+1)$** | #13 + #15 + #18 | Ch. 7 (Cases 16-20, High CEP) — possible substitute |
| §9.4 (Eulerian mathematics) | Various Euler-style infinite-product manipulations | **$e^{i\pi} + 1 = 0$** family; **$\zeta(2) = \pi^2/6$** | Various | Ch. 8 (Cases 21-25, Extreme CEP) — supplementary inspiration |
| §7.4 (Diophantine descent) | Various Diophantine impossibility proofs | **$0$ as unique solution** | #16 + #14 + #18 | Pillar 4 Ch. 9 design-exercise 3 (CEP = 0 as unique solution) — direct material |

### Cross-Reference to Blueprint §8.9 (25-Case Slate)

The 25 cases of the Pillar 4 slate are **predominantly IMO problems**, but Zeitz's worked examples and exercise problems are excellent **supplementary illustrations** for the per-case-study sub-template (§8.10):

| Pillar 4 case | Zeitz cross-reference (for technique baseline / supplementary material) |
|---|---|
| Case 1 (IMO 1959 P1, fraction in lowest terms) | Zeitz §7.1 (gcd, FTA) — technique baseline |
| Case 2 (IMO 1969 P1, polynomial $z = 2(x^2+xy+y^2)^2$) | Zeitz §5.2 (factor tactic + manipulating squares) — direct technique |
| Case 3 (Putnam 1985 A-1, distance function) | Zeitz §3.2 (extreme principle) + §8 (geometry) |
| Case 4 (IMO 1972 P1, subset coprime pair) | Zeitz §3.3 (pigeonhole) + §7.1 (gcd) |
| Case 5 (JEE Adv via Joshi Ch. 24) | Zeitz §1.1 (exercise-vs-problem distinction, framing material) |
| Case 6 (IMO 1986 P3, pentagon-vertex monovariant) | Zeitz §3.4 (monovariants — direct technique) |
| Case 7 (IMO 1995 P1, chords/tangents) | Zeitz §8.4 (concyclic points + power of point) |
| Case 8 (Putnam 1992 B-2, sequence inequality) | Zeitz §5.5 (inequalities) + §9.2 (convergence) |
| Case 9 (IMO 1979 P3, plane subdivision) | Zeitz §4.1 (graph theory) — direct technique |
| Case 10 (IMO 2003 P1, subset sum) | Zeitz §3.3 (advanced pigeonhole) + §6 |
| ... (cases 11-25 similarly cross-referenced) | Each pulls 1-2 Zeitz sections for technique baseline |

### Pillar 4 Ch. 9 Design Exercises — Zeitz Material

The three design exercises (Blueprint §8.11) each have direct Zeitz technique-baselines:

| Design # | Given CEP | Zeitz technique-baseline material |
|---|---|---|
| 1 | $7$ (the prime $7$) | Zeitz §7.1 (primality), §3.3 (pigeonhole), §3.4 (mod arithmetic). Sample: "Find all integers $n$ such that $n^2 + n + 7$ is a perfect square" — uses #14 + #11 |
| 2 | Golden ratio $\varphi$ | Zeitz §4.3 (generating functions for Fibonacci closed-form), §9.4 (Eulerian mathematics). Sample: a Fibonacci-flavoured recurrence problem with concealed $\varphi$ |
| 3 | $0$ as unique solution | Zeitz §7.4 (Diophantine descent — direct technique). Sample: a Diophantine equation whose only solution is trivial |

---

## Maintenance Notes

**Last refreshed.** 1.0 — May 28 2026. Initial comprehensive consolidated extraction. Built in parallel with `Cursor-Engel.md` as part of the Pillar 3 + Pillar 4 parallel-build prep phase.

**When to refresh.**
- For Pillar 3 work: whenever a new Pillar 3 chapter is drafted and a Zeitz problem is pulled, append the problem citation to §V with the chapter-of-use note.
- For Pillar 4 work: whenever a new Pillar 4 case study or design exercise is drafted and a Zeitz problem is pulled, append the problem citation to §VIII with the case-of-use note.

**Cross-references in this file.**
- §I Chapter-by-Chapter Index — high-level lookup
- §II Chapter Details — per-chapter conceptual content
- §III Master Index by Competition — for cross-referencing IMO/USAMO/Putnam/etc. problems
- §IV Master Index by Pillar 2 Archetype — for mapping Zeitz chapters to our 20 archetypes
- **§V Pillar 3 Multi-Archetype Convergence Index — PRIMARY LOOKUP for Pillar 3 case-study mining**
- §VI Notable Theorems — for technique-named-result lookups
- §VII Voice Register Samples — for Pillar 3 + Pillar 4 drafting (warm-conversational-missionary register)
- **§VIII Pillar 4 CEP-Design Goldmine — PRIMARY LOOKUP for Pillar 4 case-study mining and design-exercise inspiration** *(NEW; unique to Cursor-Zeitz.md)*

**Companion files.**
- `Cursor-Joshi.md` (1738 lines): Pillar 2 primary; Pillar 3 secondary. Indian-academic register.
- `Cursor-Engel.md` (581 lines): Pillar 3 primary (technique encyclopedia + multi-archetype goldmine). German-rigorous register.
- `Cursor-Zeitz.md` (this file): **Pillar 3 + Pillar 4 dual-primary** (3-layer model + multi-archetype + CEP-design goldmine). Warm-conversational-missionary register.

**The three-file reference triumvirate** is now complete for the Pillar 3 + Pillar 4 parallel build. Joshi supplies continuity with Pillar 2; Engel supplies the technique-encyclopedia depth; Zeitz supplies the strategic-meta-cognitive framing + CEP-design intuition. All three are now in the workspace as searchable text + consolidated memory files.

*End of Cursor-Zeitz.md v1.0.*
