---
chapter: 13
archetype: Combinatorial Principles
subtitle: "If You Cannot Enumerate, Structure the Count"
category: Structural Reasoning (Archetypes 13–16) — first chapter; sub-pillar opens
related_archetypes: [1, 2, 14, 15, 18]
key_gems:
  - "Multiplication principle: if a process has independent stages with $n_1, n_2, \\ldots, n_k$ choices respectively, the total number of outcomes is $\\prod_i n_i$"
  - "Addition principle: if a set is partitioned into disjoint cases of sizes $|A_1|, |A_2|, \\ldots$, the total size is $\\sum_i |A_i|$"
  - "Inclusion-exclusion: $|A_1 \\cup \\cdots \\cup A_n| = \\sum_i |A_i| - \\sum_{i < j} |A_i \\cap A_j| + \\cdots + (-1)^{n+1} |A_1 \\cap \\cdots \\cap A_n|$"
  - "Number of surjective functions $X \\twoheadrightarrow Y$ for $|X| = n, |Y| = m$: $\\sum_{k=0}^{m}(-1)^k\\binom{m}{k}(m-k)^n$"
  - "Stars-and-bars: number of non-negative-integer solutions to $x_1 + \\cdots + x_k = n$ is $\\binom{n + k - 1}{k - 1}$"
  - "Complementary counting: $|A| = |U| - |A^c|$ when $A^c$ is easier to count than $A$"
  - "Pigeonhole principle: if $n + 1$ pigeons sit in $n$ holes, some hole contains $\\ge 2$ pigeons; *extremal* form: if the average is $> n$, some box has $> n$"
  - "Bijective principle: $|A| = |B|$ if and only if there exists a bijection $A \\leftrightarrow B$; cross-archetype with Ch. 15 (Bijection)"
  - "Symmetry-then-divide (Burnside's lemma in baby form): if you count ordered configurations and the configuration has an automorphism group of order $k$, divide by $k$ to get the unordered count"
  - "Binomial distribution: number of successes in $n$ independent Bernoulli($p$) trials is $\\binom{n}{k}p^k(1-p)^{n-k}$; the basis of finitistic probability"
canonical_takeaway: "Structure first, then count. The structure of the count — symmetries, inclusion-exclusion decomposition, bijective correspondence, recursive identity — is identified before any enumeration begins."
status: draft
last_revised: 2026-05-28
sourcing_note: "All worked examples and practice problems in this chapter are drawn from K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), or from JEE / RMO / INMO / Putnam examinations commented on in that text. See Blueprint §6.2 for the sourcing rule and `pillar2-archetypes/_template/joshi-problems-locked.md` §Ch. 13 for the locked slate. **Verification audit for this chapter discovered two slate errors**: (a) PP3(b) (Tournament pairing, JEE 1997, Joshi Ex. 24.53) listed the probability that exactly one of $S_1, S_2$ wins as $\\frac{8}{15} \\cdot \\frac{1}{2} = \\frac{4}{15}$, but the correct value is $\\frac{8}{15}$, obtained by conditioning on whether $S_1, S_2$ are paired ($\\frac{1}{15} \\cdot 1 + \\frac{14}{15} \\cdot \\frac{1}{2} = \\frac{8}{15}$, matching the JEE 1997 answer key). (b) PP5 (Box with three colours, Joshi Ex. 24.86) gave an incoherent formula; the correct answer via the *symmetry trick* on the last position of a random permutation is $\\dfrac{k}{m + n + k}$, verified at $m = n = k = 1$ by direct enumeration (gives $1/3$, matching $1/(1+1+1)$). Both errors patched in slate v0.2.10; see PP3 and PP5 in the appendix for the corrected derivations."
---

# Chapter 13 — Combinatorial Principles

## *If You Cannot Enumerate, Structure the Count*

---

## Opening Vignette

A schoolteacher in Chennai is dividing her thirty Class-IX students into five working groups of six students each, for a term-long collaborative project. Her natural first thought is to assign students to groups one by one: choose six of thirty for Group 1 (in $\binom{30}{6}$ ways), then six of the remaining twenty-four for Group 2 ($\binom{24}{6}$), and so on, for a total of $\binom{30}{6}\binom{24}{6}\binom{18}{6}\binom{12}{6}\binom{6}{6}$ assignments. But she pauses — she doesn't actually want to label the groups (the project doesn't care which group is "Group 1" vs. "Group 2"); she wants the *unordered* partition of thirty students into five groups of six. The five labels are an artificial overcount: each unordered partition corresponds to $5!$ different labelled assignments (one for each permutation of the labels). So the right count is the labelled-count divided by $5!$:
\[
  \frac{1}{5!} \binom{30}{6} \binom{24}{6} \binom{18}{6} \binom{12}{6} \binom{6}{6} \;=\; \frac{30!}{(6!)^5 \cdot 5!},
\]
a multinomial coefficient with the symmetry factor $1/5!$ to account for the equivalence of group-labels. The trained combinatorialist recognises this *symmetry-then-divide* pattern instantly: count with order, divide by the order of the symmetry group. This is *Burnside's lemma in baby form* — the most useful single move in counting problems, and a glimpse of the much deeper *Burnside / Pólya enumeration theory* that emerges when the symmetry group's action becomes non-trivial.

Now turn to a different scene. A statistician at a Hyderabad pharmaceutical company is designing the dosing schedule for a phase-3 clinical trial of $600$ patients. The trial protocol calls for two arms — *dosing* and *control* — and randomisation is performed by independent coin flips. The probability that the trial ends up *exactly balanced* (300 in each arm) is the binomial coefficient $\binom{600}{300}/2^{600}$. Using *Stirling's approximation*, this evaluates to about $1/\sqrt{300\pi}$, roughly $3.3\%$. The statistician's first reaction is *concern*: only a 3.3% chance of perfect balance means a 96.7% chance of imbalance, which could compromise the trial's statistical validity. But her training kicks in — *exact* balance is irrelevant; what matters is that the *Bayesian* posterior-probability calculations correctly account for whatever imbalance arises. The binomial coefficient $\binom{600}{300}$ measures one specific configuration; the *distribution* of allocations (and the conditional likelihood of the dosing effect given that distribution) is what the trial's analysis must address. The statistician knows that *combinatorial reasoning* — binomial coefficients, complementary counting, conditional probability, the central limit theorem — is the foundation of every modern clinical trial. Without it, the trial cannot draw rigorous conclusions; with it, the trial gives reliable answers even when the sample is large but imperfect.

These two scenes look unrelated. A teacher dividing students into project groups; a statistician designing a clinical trial. They share the most important reframing in the entire chapter — the recognition that *the structure of the count is identified before the count itself is computed*. The teacher recognises *the symmetry of unordered group-labels* and divides by $5!$ to account for it; the statistician recognises *the binomial-coefficient structure* of independent randomisation and accounts for the resulting distribution of imbalance. In both cases, the structural recognition precedes — and *enables* — the calculation. The trained problem-solver internalises this two-step pattern: *first identify the structure of the count (symmetries, decompositions, bijections, recursions); then perform the calculation, often as a routine consequence of the structure*. The two steps are *not* commutative; the calculation-without-structure (the teacher's "list every possible grouping") is intractable, while the structure-without-calculation (the teacher's recognition that "the labels are symmetric") makes the calculation trivial.

This is *Combinatorial Principles*. It is the opening chapter of the *Structural Reasoning* sub-pillar (Chapters 13–16), and it carries a heavier conceptual load than its predecessors because combinatorics is the discipline of *counting structured collections*, and combinatorial problems demand both *enumeration discipline* and *structural recognition*. The chapter develops the toolkit (multiplication principle, addition principle, inclusion-exclusion, complementary counting, pigeonhole, bijective principle, symmetry-then-divide, binomial distribution) and the recurring patterns (counting surjective functions; lattice-of-subsets arguments; conditional-probability and symmetry tricks in finitistic probability; pigeonhole-with-pairing in olympiad problems). The chapter has three structural threads. The first is the *toolkit*: the named combinatorial tools and their deployment signatures. The second is the *structure-first principle*: structural recognition (symmetry, decomposition, bijection, recursion) precedes enumeration. The third is the *cross-archetype unification*: combinatorics interacts tightly with Symmetry (Ch. 2, via Burnside), Parity (Ch. 14, via the "parity-counting" tool that Chapter 14 will name), Bijection (Ch. 15, via the bijective principle), and Recursion (Ch. 18, via combinatorial recurrences) — and the chapter makes these connections explicit.

> *Structure first, then count. The structure of the count — symmetries, inclusion-exclusion decomposition, bijective correspondence, recursive identity — is identified before any enumeration begins.*

---

## 1. The Archetype Defined

### 1.1 Formal Definition

We make the intuition precise.

\begin{definition}[Combinatorial Principle]
A *combinatorial principle* on a finite set $S$ with a structure $\sigma$ (a partition, a symmetry, a relation, a constraint) is a structural fact about $S$ that determines $|S|$ — typically via decomposition ($|S| = \sum |S_i|$ by a partition), composition ($|S| = \prod |S_i|$ by an independent-stage process), correspondence ($|S| = |T|$ by a bijection $S \leftrightarrow T$), or symmetry ($|S| = |S^*| / |G|$ where $S^*$ is an ordered version of $S$ and $G$ is the symmetry group). The archetype is the discipline of (i) identifying the structural form of $S$; (ii) selecting the matching combinatorial tool; (iii) executing the enumeration as a routine consequence of the structural identification.
\end{definition}

Three remarks unpack the definition. First, the *structural identification* (Step (i)) is the cognitively hardest step and the one most prone to error. The trained combinatorialist learns to recognise structural forms — partition-into-cases, multiplication-of-stages, inclusion-exclusion-of-overlapping-sets, symmetric-overcounting, bijective-correspondence — by their *signatures*, the diagnostic features that point to the right tool. A teacher's grouping problem signals *symmetric overcounting* (the labels are equivalent); a clinical trial's allocation signals *binomial structure* (independent Bernoulli trials).

Second, *tool selection* (Step (ii)) draws from a finite, well-organised toolkit: multiplication principle, addition principle, inclusion-exclusion, stars-and-bars, complementary counting, pigeonhole, the bijective principle, the symmetry-then-divide pattern (Burnside in baby form), and the named distributions of finitistic probability (binomial, hypergeometric, geometric, Poisson). The trained solver matches structural signatures to tools in seconds.

Third, the *enumeration execution* (Step (iii)) is mechanical once the structure and tool are identified. Routine algebra, routine substitution into formulas, routine factorial / binomial-coefficient manipulation. The hard work is upstream; the execution is downstream.

The chapter encounters five characteristic forms of combinatorial principle.

- **Form I — Direct counting (multiplication / addition principles).** The set $S$ has an independent-stage structure (multiplication: each stage's choice doesn't constrain future stages) or a disjoint-case structure (addition: the cases partition $S$). *Examples.* WE3 (onto functions $\{1,2,3,4\} \to \{1,2\}$ via direct count); PP4 (two queens non-taking via direct count of non-taking pairs); PP6 (50-subset via direct case analysis after pigeonhole pairing).

- **Form II — Inclusion-exclusion.** The set $S$ is the union (or complement of the union) of overlapping subsets; the count requires alternating-sum correction. *Examples.* WE2 (surjective functions via inclusion-exclusion on missed-elements); PP1 (compositions with upper-bound constraints via inclusion-exclusion on violations).

- **Form III — Complementary counting.** The complement $S^c$ is easier to count than $S$ itself; compute $|S| = |U| - |S^c|$. *Examples.* PP4 (count "taking" pairs and subtract from $\binom{64}{2}$); WE3 (count non-onto functions = constant functions; subtract from $2^4$).

- **Form IV — Counting with symmetry (Burnside in baby form, symmetric overcounting).** Count ordered configurations; divide by the order of the symmetry group of indistinguishability. *Examples.* The opening vignette's group-assignment (divide by $5!$); PP2 (the cross-archetype with Ch. 9, but counted as $\binom{n}{3}$ which itself is a symmetric-over-orderings count).

- **Form V — Probabilistic counting (binomial distribution, conditional probability, symmetry-on-positions).** Use probability-theoretic tools (binomial coefficient, symmetry over positions in a random permutation, conditional probability) to compute the desired count. *Examples.* PP3 (tournament pairing via conditional probability + symmetry); PP5 (random-permutation symmetry on the last position); PP7 (binomial distribution applied to the event $E$).

### 1.2 The Core Principle

Stripped to its essence, the principle is one sentence.

> *Structure first, then count.*

This sentence captures the recurrent observation that, across combinatorics, the *enumeration* of a set is *not* the first step — the first step is *structural recognition* of the set's organisation. *Independent stages* (multiplication); *disjoint cases* (addition); *overlapping subsets* (inclusion-exclusion); *complement-is-easier* (complementary counting); *symmetric overcounting* (Burnside / divide-by-symmetry); *bijective correspondence* (bijective principle); *forced-pair pigeonhole* (pigeonhole principle); *recursive composition* (combinatorial recurrence). In each case, the structural identification *picks out* the counting tool, and the tool *executes* the count.

The cognitive shift is from *"list and count"* (enumerate elements one by one, hoping to total them) to *"structure and count"* (identify the structural form, apply the matching tool, get the total). The reframing prevents two classes of error. First, it prevents *over-listing* errors: enumeration without structural recognition misses cases or double-counts cases, both of which the wrong-answer-to-the-count discipline catches but only after the calculation is done. Second, it prevents *intractability*: many counting problems have astronomically large set sizes ($n!$ permutations of $n = 100$ is well beyond any practical enumeration), and structural identification is the only path to a closed-form answer.

A complementary phrasing: *the count is a consequence of the structure*. The structure (the multiplication / addition principle, the inclusion-exclusion decomposition, the symmetry group, the bijection) *implies* the count, often via a routine formula. The trained solver does not separately *prove* the count and *prove* the structure; the structural argument *is* the proof of the count.

### 1.3 The Cognitive Shift

Three cognitive shifts deserve naming.

The first is *structure-before-enumeration*. The trained solver, when faced with a counting problem, does not begin by listing elements; she begins by asking *what structure does this set have?* — independent-stage product, disjoint partition, overlapping union, symmetric overcounting, bijective correspondence. This single reframing converts most counting problems from "intractable enumeration" to "routine application of a named formula."

The second shift is *tool selection by structural signature*. The combinatorial toolkit is finite (the dozen or so principles named in §1.2) and well-organised. Each tool has a *signature* that signals its applicability: the multiplication principle signals "independent stages"; inclusion-exclusion signals "overlapping subsets, want union or complement"; complementary counting signals "the complement is easier to count"; the symmetry-then-divide pattern signals "ordered count exists, want unordered count"; the pigeonhole signals "forced-coincidence by counting argument"; the bijective principle signals "two sets that should be equinumerous because of a natural correspondence." The trained solver matches signatures to tools in seconds.

The third shift is *cross-archetype synthesis*. Combinatorial principles interact tightly with several other archetypes: with Ch. 2 (Symmetry, via Burnside's lemma — the formal version of the symmetry-then-divide pattern); with Ch. 14 (Parity, via parity-counting, where the count's parity is the key feature); with Ch. 15 (Bijection, via the bijective principle that two sets are equinumerous iff there's a bijection); with Ch. 18 (Recursion, via combinatorial recurrences like Catalan numbers, Fibonacci, derangements). The trained solver, by Chapter 13, sees combinatorics as deeply *connected* to the rest of mathematics rather than as a standalone discipline of clever tricks.

---

## 2. The Deep Structure

### 2.1 Mathematical Foundations

Combinatorial principles rest on four mathematical foundations.

The first is the *cardinality of finite sets*. A set $S$ is *finite* if there is a bijection $S \to \{1, 2, \ldots, n\}$ for some non-negative integer $n$; the unique such $n$ is the *cardinality* $|S|$. This definition makes counting *bijection-based* at its core: $|A| = |B|$ iff there exists a bijection $A \leftrightarrow B$. The whole of combinatorial counting is, ultimately, the construction of bijections between the set whose size we want and a set whose size we know.

The second foundation is the *axiom of choice in counting* (in the finite case, this is a theorem of finite set theory rather than an axiom): the cardinality of a *disjoint union* is the sum of cardinalities ($|A \sqcup B| = |A| + |B|$, the *addition principle*); the cardinality of a *Cartesian product* is the product of cardinalities ($|A \times B| = |A| \cdot |B|$, the *multiplication principle*). These two facts extend by induction to finite disjoint unions and finite Cartesian products. They are the most-used facts in all of combinatorics.

The third foundation is *inclusion-exclusion*, the generalisation of the addition principle to *overlapping* sets. For a finite family $A_1, \ldots, A_n$:
\[
  \left|\bigcup_{i=1}^n A_i\right| \;=\; \sum_{k=1}^n (-1)^{k+1} \sum_{|S| = k} \left|\bigcap_{i \in S} A_i\right|.
\]
The *alternating-sum* structure of the formula corrects for the overcounting that would arise from naïvely summing $\sum_i |A_i|$. The principle generalises to *integration* (Möbius inversion on partially-ordered sets) and to *probability* (the inclusion-exclusion formula for events).

The fourth foundation is the *bijective principle*, which gives the *equality* of cardinalities $|A| = |B|$ a constructive meaning: a bijection $A \leftrightarrow B$ is an explicit witness to the equality, and the bijection often carries additional structure (compatibility with operations, with the group action, etc.) that makes the equality more informative than a bare equality of numbers. The bijective principle is so central that it merits its own archetype (Ch. 15), and many combinatorial identities (e.g., $\binom{n}{k} = \binom{n}{n-k}$; the Catalan-number identities; the recursive identity for Stirling numbers) have *bijective proofs* that are more illuminating than algebraic proofs.

A fifth foundation, important for olympiad-style combinatorial problems: the *pigeonhole principle*. If $n + 1$ pigeons are placed into $n$ holes, some hole contains $\ge 2$ pigeons. The principle is *trivial* but its applications are far from trivial — many existence-by-counting arguments in number theory, geometry, and combinatorics rest on pigeonhole. *Generalised pigeonhole*: if $kn + 1$ pigeons are placed into $n$ holes, some hole contains $\ge k + 1$ pigeons. *Probabilistic / averaging pigeonhole*: if the average is $> n$, some box has $> n$. *Extremal pigeonhole*: if the maximum is $\ge$ a threshold, the structure has the corresponding extremal property.

A sixth foundation, important for finitistic probability: the *binomial coefficient* and the *binomial distribution*. The number of $k$-element subsets of an $n$-element set is $\binom{n}{k} = n!/(k!(n-k)!)$. The probability of exactly $k$ successes in $n$ independent Bernoulli($p$) trials is $\binom{n}{k} p^k (1 - p)^{n-k}$. These two facts together are the foundation of all of *discrete probability*, and they recur in problems from genetics (Mendel's pea ratios), quality control (sample defect counts), polling (election forecasts), and physics (the Bose-Einstein and Fermi-Dirac statistics, generalised binomial coefficients).

### 2.2 Physical and Cross-Domain Foundations

The reach of combinatorial principles extends across the quantitative sciences.

In *statistical mechanics*, the *fundamental statistical mechanical postulate* is that the equilibrium state of a closed system at fixed energy is the *equally-likely-microstate* distribution — every accessible microstate has the same probability $1 / W$, where $W$ is the number of accessible microstates. The thermodynamic *entropy* is $S = k_B \ln W$ (Boltzmann's formula), a logarithmic measure of the count. *Free energy*, *partition function*, *thermal distributions* (Boltzmann, Bose-Einstein, Fermi-Dirac) — all are combinatorial counts of microstates, dressed in physicist's notation. The chapter's bijection between counting and physics is *not* metaphorical: the laws of thermodynamics are, in the modern (Gibbs / Jaynes) formulation, theorems of combinatorial probability theory.

In *quantum mechanics*, the *probabilistic interpretation* (Born rule) gives the probability of a measurement outcome as $|\langle\psi|\phi\rangle|^2$, a sum over the basis-state probabilities. The combinatorial structure of *Hilbert space dimension* (the dimension of the state space of $N$ qubits is $2^N$ — a combinatorial count) and of *entanglement* (the entanglement-entropy across a bipartition is a Boltzmann-like count) is foundational.

In *information theory*, *Shannon entropy* $H(X) = -\sum_x p(x) \log p(x)$ is a probabilistic generalisation of $\log W$ from statistical mechanics. The *combinatorial counting* of bit-strings of length $n$ with bounded entropy gives the source-coding theorem: with high probability, a source produces a *typical sequence* belonging to a set of about $2^{n H(X)}$ such sequences. *Channel capacity* (Shannon's noisy-channel theorem) is a combinatorial bound on reliable communication rates.

In *cryptography*, the security of cryptographic systems often rests on combinatorial counting: the number of possible keys (the *key space*), the number of possible permutations (the *cipher group*), the probability of accidental collision in a hash function (the *birthday paradox*, a direct combinatorial / pigeon-hole argument). Modern public-key cryptography rests on the *computational* hardness of certain combinatorial problems (factoring, discrete logarithm).

In *theoretical computer science*, the *complexity-theoretic* foundations rest on combinatorial counting: the number of possible inputs of length $n$ ($2^n$ for binary), the number of possible computations of length $T$ (combinatorial in the alphabet and the time bound), the number of satisfying assignments to a Boolean formula (the $\#P$-counting class). *Probabilistic algorithms*, *Las Vegas algorithms*, *Markov chain Monte Carlo*, *randomised hashing* — all rest on probabilistic-combinatorial foundations.

In *biology and genetics*, *combinatorial biology* studies the combinatorial diversity of biological structures: $\binom{4}{2} = 6$ pairs of DNA bases; $20$ amino acids; $4^{20} \approx 10^{12}$ possible 20-residue protein chains; the combinatorial number of possible antibody configurations ($10^{11}$+) generated by V(D)J recombination of immunoglobulin gene segments. *Population genetics* rests on the *Hardy-Weinberg equilibrium* (a binomial / multinomial distribution of allele frequencies under random mating).

In *economics*, *combinatorial auctions* (where bidders bid on *bundles* of items rather than single items) raise the *winner-determination problem*: enumerate combinatorial bundle-assignments to maximise revenue. *Matching markets* (Roth-Shapley) require enumerating combinatorial pairings — kidney-exchange networks, medical-residency matching, school choice all use combinatorial-counting structures.

In *combinatorial chemistry and drug discovery*, the *combinatorial library* of synthesisable compounds is enumerated by combinatorial principles applied to molecular substructures (the *building blocks*); the *high-throughput screening* operates on the resulting combinatorial library, often with binomial / Poisson distributions of hit rates.

### 2.3 Cognitive Foundations

The cognitive payoff of combinatorial principles is threefold.

The first is *intractability avoidance*. Many counting problems have astronomically large set sizes — $n!$ for permutations of $n = 50$ is about $3 \times 10^{64}$, well beyond direct enumeration. Structural recognition (the symmetric-overcounting reduction, the inclusion-exclusion decomposition, the bijective principle) is the *only* path to a closed-form answer in such cases. The trained combinatorialist *internalises* that "list every element" is impossible at most scales, and replaces it with "identify the structure of the count and apply the matching formula."

The second payoff is *error prevention*. Naïve enumeration suffers from two systematic errors: *over-counting* (listing the same element more than once, often invisibly) and *under-counting* (missing cases, often by symmetry-breaking assumptions that turn out not to be exhaustive). Structural recognition prevents both: the *symmetry-then-divide* pattern catches over-counting (by explicitly dividing by the symmetry group's order); the *inclusion-exclusion* pattern catches under-counting (by explicitly decomposing overlapping subsets). The discipline is not just faster than naïve enumeration; it is *more reliable*.

The third payoff is *cross-archetype synthesis*. Combinatorial principles unify Chapters 2 (Symmetry — Burnside's lemma is the formal version of symmetry-then-divide), 14 (Parity — parity-counting, where the count's parity is the structurally-significant feature), 15 (Bijection — the bijective principle, the foundation of all of counting), and 18 (Recursion — combinatorial recurrences like Fibonacci, Catalan, Stirling, derangements). The trained solver, by Chapter 13, sees these as a single coherent body of *structured counting* rather than four separate techniques.

---

## 3. The Diagnostic Toolkit

### 3.1 The Three Questions Method (Combinatorial Principles Edition)

Before deploying any combinatorial tool, the trained solver asks three questions of the problem.

1. **What is the set being counted?** Identify the underlying set $S$ explicitly: a set of functions, of arrangements, of subsets, of sequences, of partitions, of tilings, of permutations. The set must have a clean *definition* before its size can be computed. Many counting errors trace back to *fuzzy set definition* — overlapping cases, ambiguous "configurations," undeclared equivalence relations.

2. **What is the structure of the set?** Match the set's structure to the combinatorial form:
   - *Independent stages of choice*: multiplication principle.
   - *Disjoint cases*: addition principle.
   - *Union of overlapping subsets*: inclusion-exclusion.
   - *Complement easier than direct*: complementary counting.
   - *Ordered count exists; want unordered*: symmetry-then-divide.
   - *Natural correspondence to a known set*: bijective principle.
   - *Forced coincidence by counting*: pigeonhole.
   - *Independent Bernoulli trials*: binomial distribution.

3. **What is the formula?** Once the structure is identified, the formula follows: $n^k$ for length-$k$ sequences from $n$ symbols (with repetition); $\binom{n}{k}$ for $k$-subsets of $n$ elements; $\binom{n+k-1}{k-1}$ for non-negative integer solutions of $x_1 + \cdots + x_k = n$ (stars-and-bars); $\sum_{k=0}^m (-1)^k \binom{m}{k}(m-k)^n$ for surjective $X \twoheadrightarrow Y$; etc.

### 3.2 Forms of Combinatorial Principles: A Comprehensive Guide

We collect the five forms encountered in the chapter with one-line diagnostics.

- **Form I — Direct counting (multiplication / addition principles).** *Diagnostic:* the set is generated by independent choices (multiplication) or partitioned into disjoint cases (addition). *Move:* compute the product (or sum) of stage-cardinalities. *Examples.* WE3 (direct count by complement, also expressible as multiplication on assignments minus constants).

- **Form II — Inclusion-exclusion.** *Diagnostic:* the set is the union (or complement of the union) of overlapping subsets. *Move:* apply the inclusion-exclusion formula $|A_1 \cup \cdots \cup A_n| = \sum (-1)^{k+1} \binom{n}{k} |\bigcap_{|S|=k} A_S|$ (with the appropriate symmetry simplifications). *Examples.* WE2 (surjective-function count), PP1 (compositions with upper-bound constraints).

- **Form III — Complementary counting.** *Diagnostic:* the complement of the set is easier to count than the set itself. *Move:* compute $|S| = |U| - |S^c|$ where $|U|$ is a tractable universal count and $|S^c|$ is tractable. *Examples.* WE3 (constant functions are the complement of surjections from $\{1,2,3,4\}$ to $\{1,2\}$, easier to count); PP4 (taking pairs of queens are easier to count than non-taking).

- **Form IV — Counting with symmetry (Burnside-baby form).** *Diagnostic:* an ordered version of the count is computable, but the problem wants the unordered version (or a symmetry-quotient version). *Move:* compute the ordered count; divide by the order of the symmetry group of indistinguishability. *Examples.* Opening vignette (group-labels); PP2 (vertex-labels in the polygon-triangle count).

- **Form V — Probabilistic counting.** *Diagnostic:* the count is a probability over a sample space; symmetry over positions, conditional probability, or binomial-distribution machinery applies. *Move:* set up the sample space; identify the event; use the appropriate probability tool (symmetry, conditional, binomial). *Examples.* PP3 (tournament pairing, symmetry + conditional), PP5 (last-position symmetry), PP7 (binomial distribution).

### 3.3 Common Pitfalls

Five errors recur often enough to deserve named warnings.

- **The Over-Counting Pitfall.** Counting the same element more than once, often invisibly, because of an implicit ordering or labelling that the problem doesn't actually demand. The opening vignette warns about this: counting *ordered* group-assignments overcounts the *unordered* groupings by $5!$. The remedy is to *explicitly identify the symmetry group* and divide.

- **The Under-Counting Pitfall.** Missing cases by symmetry-breaking assumptions that turn out not to be exhaustive. E.g., counting non-taking queen pairs only on the same colour (8x8 board) misses non-taking pairs on different colours. The remedy is to *check exhaustiveness explicitly*, often via a complementary-counting cross-check.

- **The Inclusion-Exclusion-Misapplied Pitfall.** Applying inclusion-exclusion with the wrong sign pattern, or with the wrong subsets, or after a sign-error in counting one of the intersections. The remedy is to *write out the formula explicitly* and check small cases ($n = 2, 3$) before trusting the general formula.

- **The Complementary-Counting-Misapplied Pitfall.** Computing $|S^c|$ and forgetting to subtract from $|U|$, or vice versa. The remedy is to *write out the universe $U$ explicitly* and label which set's complement is being computed.

- **The Pigeonhole-Mis-set-up Pitfall.** Applying pigeonhole with the wrong pigeons or holes — typically, choosing the holes too generously (so the pigeonhole bound is not tight enough). The remedy is to *minimise the number of holes* relative to the number of pigeons, and to choose holes that *force* the desired structural conclusion (not a generic conclusion).

---

## 4. Worked Examples

We work three problems in detail, each in the six-point format. The first illustrates Form IV (counting with structural argument) for the Putnam dance-party problem; the second illustrates Form II (inclusion-exclusion) for surjective functions; the third illustrates Form III (complementary counting) for the JEE 2001 onto-functions problem.

### 4.1 Example 1 — The Dance-Party Bipartite Configuration (Putnam)

**Problem.** *At a dance party, every boy dances with at least one girl, but no girl dances with every boy. Prove that there exist two boys $b, b'$ and two girls $g, g'$ such that: $b$ dances with $g$, $b'$ dances with $g'$, but $b$ does NOT dance with $g'$ and $b'$ does NOT dance with $g$. Paraphrase the conclusion in terms of subsets of the set of girls.*
*(Putnam; Joshi EJM Ch. 24, Exercise 24.8.)*

**SEED.** *Combinatorial principle (Form IV — counting with structural argument).* Translate to a subset-lattice problem: each boy $b_i$ has a partner set $G_i \subseteq G$ (the girls he dances with). The two given conditions translate to (a) every $G_i$ is non-empty and (b) $\bigcap_i G_i = \emptyset$ (no girl is in every partner set). The desired conclusion translates to (c) the family $\{G_i\}$ is not a *chain* under inclusion — i.e., there exist indices $i, j$ such that $G_i$ and $G_j$ are *incomparable*. The structural argument: *a chain under inclusion has a non-empty common intersection (the bottom of the chain) unless the bottom is empty; condition (a) rules out the empty bottom, so condition (b) forces the family to be non-chain*.

**BRUTE PATH.** A student who does not translate to the subset lattice might try to find the configuration $(b, b', g, g')$ directly by *case analysis* on small numbers of boys and girls. With $|B| = 1$, condition (a) requires the single boy to dance with at least one girl, but then condition (b) forces some girl to be in $G_1$ — wait, condition (b) is "no girl dances with every boy," and with one boy, every girl is either danced with or not; if any girl is danced with, she "dances with every boy" trivially. So with $|B| = 1$, conditions (a) and (b) are mutually contradictory. With $|B| = 2$, the case analysis is manageable but already messy. The brute path is impractical for general $|B|, |G|$; the elegant pivot via the subset-lattice translation is structurally simpler.

**ELEGANT PIVOT.** *Subset-lattice translation; chain-vs-non-chain argument.*

*Step 1 — Translation.* Let $B = \{b_1, \ldots, b_p\}$, $G = \{g_1, \ldots, g_q\}$, and for each $i$ let $G_i \subseteq G$ be the set of girls that $b_i$ dances with. The two given conditions become:
- (a) $G_i \ne \emptyset$ for every $i$ (every boy dances with at least one girl).
- (b) $\bigcap_{i = 1}^p G_i = \emptyset$ (no girl is in every partner set).

The desired conclusion (the existence of $b, b', g, g'$ with the four conditions) translates to:
- (c) There exist indices $i, j$ such that $G_i \not\subseteq G_j$ and $G_j \not\subseteq G_i$ (the partner sets are incomparable).

To see (c) implies the desired conclusion: pick any $g \in G_i \setminus G_j$ (which exists since $G_i \not\subseteq G_j$) and any $g' \in G_j \setminus G_i$ (which exists since $G_j \not\subseteq G_i$). Then $b_i$ dances with $g$ (since $g \in G_i$) but not with $g'$ (since $g' \notin G_i$); $b_j$ dances with $g'$ (since $g' \in G_j$) but not with $g$ (since $g \notin G_j$). Setting $b = b_i, b' = b_j$ gives the required configuration.

So it suffices to prove (c): the family $\{G_1, \ldots, G_p\}$ contains an incomparable pair.

*Step 2 — Chain-vs-non-chain dichotomy.* A family of sets is a *chain* under inclusion if every two of its members are comparable (one is a subset of the other). Equivalently, the family can be ordered $G_{(1)} \subseteq G_{(2)} \subseteq \cdots \subseteq G_{(p)}$ after a relabeling. Otherwise the family is *non-chain*, and contains an incomparable pair.

So either the family $\{G_1, \ldots, G_p\}$ is a chain (and we must derive a contradiction with the hypotheses) or it is non-chain (and we have our incomparable pair).

*Step 3 — Chain forces $\bigcap = \emptyset$ to fail.* Suppose the family is a chain. WLOG (by relabeling) $G_1 \subseteq G_2 \subseteq \cdots \subseteq G_p$. Then $\bigcap_{i = 1}^p G_i = G_1$ (the intersection of a chain is the smallest set). By hypothesis (b), $\bigcap_i G_i = \emptyset$, so $G_1 = \emptyset$. But hypothesis (a) says $G_1 \ne \emptyset$ (every boy dances with at least one girl). Contradiction.

Therefore the family is non-chain, and (c) holds. \hfill$\blacksquare$

The elegant pivot is a *structural translation* (boys-and-girls to subset-lattice) followed by a *chain-vs-non-chain dichotomy* (the only way to fail to have an incomparable pair is to be a chain; chains have non-empty intersection equal to the bottom; the bottom-non-empty hypothesis contradicts the empty-intersection hypothesis). The argument is short and uses no enumeration — pure structural combinatorics.

**PITFALLS.**

- *Misreading hypothesis (b).* "No girl dances with every boy" means: for every girl $g$, there exists some boy $b_i$ with $g \notin G_i$, equivalently $\bigcap_i G_i = \emptyset$ (no girl is in *every* $G_i$). A common misreading is "no girl dances with any boy," which would give $\bigcup_i G_i = \emptyset$ — a much stronger and quite different condition. The remedy is to *parse the quantifiers carefully*: "no girl" = $\forall g$; "dances with every boy" = $\forall b: g \in G_b$.

- *Mis-translating the desired conclusion.* The conclusion asks for four specific properties: $b$ dances with $g$, $b'$ with $g'$, $b$ not with $g'$, $b'$ not with $g$. Equivalently: $\{G_b, G_{b'}\}$ is an incomparable pair (with $g \in G_b \setminus G_{b'}, g' \in G_{b'} \setminus G_b$). A common misread is "there exist $b, g$ with $g \in G_b$" — far weaker. The remedy is to *write out the conclusion's logical structure explicitly*.

- *Assuming the chain has more than one element.* A chain $G_1 \subseteq G_2 \subseteq \cdots \subseteq G_p$ has intersection $G_1$ (the bottom), regardless of whether the chain is "strict" or has duplicates. The remedy is to *not assume strict inclusion*.

- *Forgetting to verify both inclusions in incomparable pair.* For "incomparable" we need $G_i \not\subseteq G_j$ AND $G_j \not\subseteq G_i$. Just one of the two is not enough (else $G_i \subseteq G_j$ which is comparable). The remedy is to *verify both* and pick $g \in G_i \setminus G_j$ and $g' \in G_j \setminus G_i$ separately.

- *Confusing "family is non-chain" with "two-element antichain."* A family is non-chain iff it contains *at least one* incomparable pair. (It may also contain larger antichains, but the problem only needs the pair.) The remedy is to *use "incomparable pair" rather than "antichain"* for clarity.

**CONNECTIONS.**

*Primary archetype applications.* This problem is a baby case of *Sperner's theorem* (the largest antichain in the subset lattice of $\{1, \ldots, n\}$ has size $\binom{n}{\lfloor n/2 \rfloor}$), of *Dilworth's theorem* (any finite poset decomposes into chains, the minimum number equalling the maximum antichain size), and of the *Erdős-Ko-Rado theorem* (the largest intersecting family of $k$-subsets of $\{1, \ldots, n\}$ is $\binom{n-1}{k-1}$ for $n \ge 2k$). All three theorems are foundational in *extremal set theory*, a branch of combinatorics with applications to coding theory, combinatorial geometry, and information theory.

*Alternative solution archetypes.* The chain-vs-non-chain argument is a *Pigeonhole* (Ch. 13 §2) application in disguise: if the family is a chain, then the bottom is forced to be empty (contradicting (a)); pigeonhole forces the family off the chain. It is also a *Symmetry* (Ch. 2) argument: the subset lattice has a partial order whose *symmetric* elements (incomparable pairs) carry the structural information.

*Cross-domain manifestations.* The dance-party problem is a graph-theoretic instance of the *bipartite-graph configuration* problem: a bipartite graph with no isolated vertex on the $B$-side and no $G$-vertex adjacent to all $B$ contains a *$2K_2$* (a matching with no edges between the two pairs). The result is foundational in *bipartite graph theory*, with applications to matching algorithms, network flows (the König-Egerváry theorem on the min-vertex-cover / max-matching duality), and combinatorial optimisation.

**TAKEAWAY.** *Translate combinatorial-configuration problems to the subset-lattice; use chain-vs-non-chain dichotomy to find incomparable elements; the structural translation makes the proof short and case-free.*

---

### 4.2 Example 2 — Number of Surjective Functions (Inclusion-Exclusion)

**Problem.** *Let $X$ be a set of $n$ elements and $Y$ a set of $m$ elements. Prove that the number of surjective functions $f : X \twoheadrightarrow Y$ is*
\[
  \sigma(n, m) \;=\; \sum_{k=0}^{m} (-1)^k \binom{m}{k} (m - k)^n.
\]
*(Joshi EJM Ch. 24, Exercise 24.80(i); classical inclusion-exclusion.)*

**SEED.** *Combinatorial principle (Form II — inclusion-exclusion).* "Surjective" is the complement of "misses at least one element of $Y$." The set of functions $X \to Y$ has size $m^n$; the set of *non-surjective* functions is the union of the sets $A_i = \{f : y_i \notin f(X)\}$ for $i = 1, \ldots, m$. By inclusion-exclusion, $|A_1 \cup \cdots \cup A_m|$ has an alternating-sum formula in terms of $|A_{i_1} \cap \cdots \cap A_{i_k}| = (m - k)^n$. Subtracting from $m^n$ gives the formula.

**BRUTE PATH.** A student who does not see the inclusion-exclusion structure might try to count surjective functions *directly*: for each ordered partition of $X$ into $m$ non-empty blocks, assign block $i$ to element $y_i$. The number of ordered partitions of $n$ elements into $m$ non-empty blocks is $m! \cdot S(n, m)$ (where $S(n, m)$ is the *Stirling number of the second kind*); the surjective-function count is therefore $m! \cdot S(n, m)$. This is correct but recursive (Stirling numbers have their own recurrence $S(n, m) = m \cdot S(n-1, m) + S(n-1, m-1)$); the inclusion-exclusion formula gives a closed-form alternative.

**ELEGANT PIVOT.** *Inclusion-exclusion on the "missed elements" sets.*

*Step 1 — Define the bad sets.* For each $i \in \{1, 2, \ldots, m\}$, let
\[
  A_i \;=\; \{f : X \to Y \;:\; y_i \notin f(X)\} \;=\; \{f : X \to Y \;:\; \forall x \in X, f(x) \ne y_i\}.
\]
A function $f$ is *non-surjective* iff it misses at least one $y_i$, i.e., iff $f \in \bigcup_{i = 1}^m A_i$. The number of surjective functions is
\[
  \sigma(n, m) \;=\; m^n - \left|\bigcup_{i = 1}^m A_i\right|.
\]

*Step 2 — Cardinality of intersections.* For any subset $S \subseteq \{1, \ldots, m\}$ of size $k$, the intersection $\bigcap_{i \in S} A_i$ is the set of functions $X \to Y$ that miss every $y_i$ for $i \in S$, i.e., functions $X \to Y \setminus \{y_i : i \in S\}$. The codomain has size $m - k$, so there are $(m - k)^n$ such functions. (Note: this holds for every $S$ of size $k$, and the count depends only on $|S| = k$, not on which elements $S$ contains — a *symmetry* of the problem.)

*Step 3 — Apply inclusion-exclusion.* By the inclusion-exclusion formula,
\[
  \left|\bigcup_{i = 1}^m A_i\right| \;=\; \sum_{k = 1}^m (-1)^{k+1} \sum_{|S| = k} \left|\bigcap_{i \in S} A_i\right| \;=\; \sum_{k = 1}^m (-1)^{k+1} \binom{m}{k} (m - k)^n.
\]

*Step 4 — Assemble.* The surjective-function count is
\[
  \sigma(n, m) \;=\; m^n - \sum_{k = 1}^m (-1)^{k+1} \binom{m}{k}(m - k)^n \;=\; \sum_{k = 0}^m (-1)^k \binom{m}{k} (m - k)^n,
\]
where the $k = 0$ term contributes $\binom{m}{0} m^n = m^n$ (matching the subtracted $m^n$ if we include $k = 0$ in the alternating sum). $\blacksquare$

The elegant pivot is the *inclusion-exclusion principle*: the complement of "surjective" is "misses at least one element," which is a union of $m$ sets with neatly-described intersections. The structural symmetry (the count $|\bigcap_{i \in S} A_i| = (m - k)^n$ depends only on $|S|$) collapses the inclusion-exclusion sum to the simple binomial expression.

**PITFALLS.**

- *Sign-error in inclusion-exclusion.* The signs alternate as $(-1)^{k+1}$ for the union and $(-1)^k$ for the complement (after the $m^n$ subtraction). A common error is to use the wrong sign for the $k = 0$ term; the remedy is to *include $k = 0$ explicitly* in the surjective-count sum, which absorbs the $m^n$ subtraction cleanly.

- *Misidentifying the bad set.* "Non-surjective" means "misses at least one," not "misses exactly one." The "at least one" gives a *union*; the "exactly one" gives a more complicated, mutually-exclusive count. The remedy is to *be explicit about quantifiers* and check $m = 1$ (only one possible $y$; surjective iff $f$ is constant; $\sigma(n, 1) = 1$; formula: $\sum_{k=0}^1 (-1)^k \binom{1}{k}(1-k)^n = 1^n - 0^n = 1$ ✓).

- *Confusing surjective with bijective.* For $|X| = |Y|$, surjective = bijective; otherwise they differ. The formula gives surjective; for bijective, the count is $m!$ (when $n = m$) or $0$ (when $n \ne m$). The remedy is to *distinguish surjective from bijective* explicitly.

- *Not verifying small cases.* The formula must give $\sigma(n, m) = 0$ when $n < m$ (no surjection possible) and $\sigma(n, n) = n!$ (surjections are bijections). The remedy is to *plug in $n = m$ and $n < m$* to verify; e.g., $\sigma(2, 3) = \sum (-1)^k \binom{3}{k} (3-k)^2 = 9 - 3 \cdot 4 + 3 \cdot 1 - 0 = 0$ ✓.

- *Confusion with the Stirling formula.* The closed form $\sigma(n, m) = \sum (-1)^k \binom{m}{k}(m-k)^n$ relates to $S(n, m)$ by $\sigma(n, m) = m! \cdot S(n, m)$, giving $S(n, m) = \frac{1}{m!} \sum (-1)^k \binom{m}{k}(m-k)^n$ — a closed-form expression for the Stirling number of the second kind that is rarely easier to use than the recurrence, but useful for verification.

**CONNECTIONS.**

*Primary archetype applications.* The surjective-function formula is one of the most-used inclusion-exclusion applications, with cousins in: *derangements* (permutations with no fixed point — inclusion-exclusion on "$\pi(i) = i$" events; the answer is $n! \sum_{k=0}^n (-1)^k / k!$, approximately $n!/e$); *partitions into distinguishable boxes with at least one element per box* (same formula, different interpretation); *Möbius inversion* on lattices (a generalisation of inclusion-exclusion to arbitrary posets).

*Alternative solution archetypes.* The same problem has a *generating-function* solution: the *exponential generating function* of surjections to $Y$ is $(e^x - 1)^m$, and $\sigma(n, m) = n! \cdot [x^n] (e^x - 1)^m$. Expanding $(e^x - 1)^m = \sum_k (-1)^{m-k} \binom{m}{k} e^{kx}$ and extracting $[x^n]$ gives the same inclusion-exclusion formula. The generating-function route generalises to *non-uniform* counts and to *enumerative combinatorics* (Stanley's *Enumerative Combinatorics*, the standard text).

*Cross-domain manifestations.* The surjective-function count appears in: *the coupon-collector problem* (the expected time to collect all $m$ coupons, given by $m \cdot H_m$ via inclusion-exclusion); *the German tank problem* (statistical inference from sequence-of-missed-elements data, used famously to estimate Nazi tank production in WW2); *probabilistic load-balancing* (the probability that all of $m$ servers receive at least one job, given $n$ jobs distributed uniformly at random, is $\sigma(n, m) / m^n$).

**TAKEAWAY.** *Surjective-function count via inclusion-exclusion: $\sigma(n, m) = \sum_{k=0}^m (-1)^k \binom{m}{k}(m-k)^n$; "surjective" is the complement of "misses at least one element."*

---

### 4.3 Example 3 — Onto Functions $\{1,2,3,4\} \to \{1,2\}$ (Complementary Counting)

**Problem.** *Find the number of onto functions from $\{1, 2, 3, 4\}$ to $\{1, 2\}$.*
*(JEE 2001; Joshi EJM Ch. 24, Exercise 24.21.)*

**SEED.** *Combinatorial principle (Form III — complementary counting).* The total number of functions $\{1, 2, 3, 4\} \to \{1, 2\}$ is $2^4 = 16$. A function is *non-onto* iff it misses $1$ or misses $2$ — and (since the codomain has only 2 elements) iff it is *constant*. There are exactly $2$ constant functions (the constant-$1$ and the constant-$2$). So the count of onto functions is $16 - 2 = 14$.

**BRUTE PATH.** Try to *list* all onto functions $\{1,2,3,4\} \to \{1,2\}$ directly. Each onto function is determined by the partition of $\{1,2,3,4\}$ into the preimage of $1$ and the preimage of $2$, both non-empty. The non-empty ordered partitions of a 4-element set into 2 blocks: number of ways to choose the preimage of $1$ (any non-empty proper subset of $\{1,2,3,4\}$) = $2^4 - 2 = 14$ (excluding the empty set and the full set, which would make the preimage of $2$ empty). So $14$. Direct enumeration would list all $14$ functions: $\{f(1) = 1, f(2) = 1, f(3) = 1, f(4) = 2\}$, etc. — tedious but possible.

**ELEGANT PIVOT.** *Complementary counting on the constant-functions complement.*

*Step 1 — Universe and complement.* Total functions $\{1,2,3,4\} \to \{1,2\}$: $|U| = 2^4 = 16$.
Non-onto functions: a function $f$ is non-onto iff its image is a proper subset of $\{1, 2\}$, i.e., $f(\{1,2,3,4\}) \subseteq \{1\}$ or $\subseteq \{2\}$. Each option gives the constant function valued at the respective element. Total: $2$ constant functions.

*Step 2 — Subtract.*
\[
  \text{Onto functions} \;=\; 16 - 2 \;=\; \boxed{14}.
\]
$\blacksquare$

*Cross-check with WE2 formula.* $\sigma(4, 2) = \sum_{k=0}^2 (-1)^k \binom{2}{k}(2-k)^4 = 1 \cdot 16 - 2 \cdot 1 + 1 \cdot 0 = 16 - 2 = 14$. ✓

The elegant pivot is *complementary counting*: counting non-onto functions (which are the constant functions, a tiny set of size 2) is far easier than counting onto functions directly. The structural recognition — "non-onto means missing an element; with codomain of size 2, missing an element forces constancy" — converts a 14-case enumeration into a 2-case enumeration.

**PITFALLS.**

- *Confusing "onto" with "one-to-one."* "Onto" (= surjective) means every element of the codomain is the image of *some* element. "One-to-one" (= injective) means distinct elements map to distinct images. They are *different* concepts. The problem says "onto"; the remedy is to *parse the term* and check that the conclusion is about surjection, not injection (which would have answer $0$ since $|X| = 4 > 2 = |Y|$, no injection possible).

- *Confusing constant functions with "non-constant non-onto."* For codomain $\{1, 2\}$, non-onto = constant (no other options). For codomain $\{1, 2, 3\}$, non-onto includes constant functions ($3$ of them) *and* functions whose image has size $2$ (more complicated, by WE2 formula: $|A_1 \cup A_2 \cup A_3| - |A_1 \cap A_2| - \ldots = 3 \cdot 2^4 - 3 \cdot 1^4 + 0 = 48 - 3 = 45$ non-onto; surjective = $3^4 - 45 = 81 - 45 = 36$). The remedy is to *check that "non-onto = constant" only holds for codomain of size 2*.

- *Miscounting via the partition formula.* "Partition of $\{1,2,3,4\}$ into the preimage of $1$ and the preimage of $2$": the preimage of $1$ can be any non-empty proper subset (with the preimage of $2$ being the complement). Number of non-empty proper subsets of a 4-element set: $2^4 - 2 = 14$. So $14$ onto functions. ✓ But care is needed: this is an *ordered* partition (preimage of $1$ vs preimage of $2$), so no symmetry-then-divide is needed. If the problem asked for *un*ordered partitions, we'd divide by $2! = 2$ giving $7$.

- *Forgetting the universe.* Complementary counting requires the universe $|U|$ to be tractable. For $\{1,2,3,4\} \to \{1,2\}$, $|U| = 2^4 = 16$ is trivial. For more general $X \to Y$ with $|X| = n, |Y| = m$, $|U| = m^n$ and the complementary count requires WE2's inclusion-exclusion.

- *Confusing JEE-style options with the count.* The JEE problem likely gave options (A) 12, (B) 14, (C) 16, (D) none of these — and the answer is (B). Some students might *eliminate* (B) because $14$ looks "incomplete" and pick (D) "none of these." The remedy is to *trust the calculation*.

**CONNECTIONS.**

*Primary archetype applications.* Complementary counting is one of the most-used techniques in counting problems with "at least" or "missing" structure: *at least one repeated digit in an $n$-digit number* (complement is "all distinct"); *at least one fixed point in a permutation* (complement is "derangement"); *at least one black ball in a draw of $k$ from $m$-white-$n$-black* (complement is "all white"); *at least one common point in two random subsets* (complement is "disjoint"). The remedy "compute the complement, subtract" is a universal shortcut in finitistic probability.

*Alternative solution archetypes.* The same problem has a *direct-counting* solution: count the onto functions by the *ordered-partition* method (the preimage of $1$ is any non-empty proper subset, $14$ choices). Both approaches give the same answer; the complementary-counting approach is *faster* because the complement (2 constant functions) is more compact than the direct count (14 functions).

*Cross-domain manifestations.* "Onto function from a 4-set to a 2-set" is the same as "covering of $\{1, 2\}$ by labelled elements of $\{1, 2, 3, 4\}$" — a baby instance of *set covers*, *boolean satisfiability*, and *combinatorial design theory*. The problem also corresponds to "binary string of length 4 with at least one $0$ and at least one $1$" (associating function value $1 \mapsto 0, 2 \mapsto 1$), a basic problem in combinatorial enumeration that recurs in coding theory (parity codes), DNA / RNA sequencing (sequence motifs), and information theory (constrained binary sequences).

**TAKEAWAY.** *Complementary counting: when the complement is easier than the direct count, compute the complement and subtract from the universe. Surjections from $\{1,2,3,4\}$ to $\{1,2\}$: $16 - 2 = 14$.*

---

## 5. Practice Problems

Seven problems, statements only; full solutions appear in the Appendix. The slate is heavy on Tier 3 (RMO-level), with two Tier 2 anchors (PP2, PP7) and no Tier 4. This reflects the inherent difficulty curve of olympiad combinatorics — the chapter is denser than the four Constraint Exploitation chapters that precede it, and we lean into RMO-level density here to prepare for the Parity (Ch. 14) and Bijection (Ch. 15) chapters that follow.

### 5.1 Three Numbers Summing to $2p$ (Tier 3 RMO; Joshi Ch. 24, Exercise 24.51)

Three numbers are drawn with replacement from $\{1, 2, \ldots, p\}$. Prove that the probability that their sum is $2p$ is $\dfrac{(p - 1)(p + 4)}{2 p^3}$.

### 5.2 Inscribed Triangles via Polygon Vertices (Tier 2 JEE; Joshi Ch. 24, Exercise 24.20)

Let $T_n$ denote the number of triangles whose vertices are chosen from the vertices of a regular polygon of $n$ sides. If $T_{n+1} - T_n = 21$, find $n$.

### 5.3 Tournament Pairing (Tier 3 JEE Advanced; Joshi Ch. 24, Exercise 24.53)

Sixteen players, including two distinguished players $S_1$ and $S_2$, are divided into eight pairs at random. The two players in each pair play a match; the winner is decided by a fair coin flip (each player wins with probability $\tfrac{1}{2}$, independently). Find:
(a) the probability that $S_1$ is among the eight winners;
(b) the probability that *exactly one* of $S_1, S_2$ is among the eight winners.

*[Verification-audit note: the locked slate stated (b)'s probability as $\frac{8}{15} \cdot \frac{1}{2} = \frac{4}{15}$, but the correct value is $\frac{8}{15}$, obtained by conditioning on whether $S_1, S_2$ are paired with each other and using the independence of the other-pair matches; this matches the JEE 1997 answer key. The slate is patched in v0.2.10; see the appendix solution for the derivation.]*

### 5.4 Two Queens Non-Taking (Tier 3; Joshi Ch. 24, Exercise 24.56)

Two queens are placed at random on an $8 \times 8$ chessboard (with all $\binom{64}{2}$ placements equally likely). Find the probability that the two queens are *non-taking* — i.e., that they are not on the same row, the same column, or the same diagonal.

### 5.5 Box with Three Colours, Red Last (Tier 3; Joshi Ch. 24, Exercise 24.86)

A box contains $m$ white balls, $n$ black balls, and $k$ red balls. Balls are drawn one by one without replacement until only one colour remains in the box. Find the probability that the remaining balls are red.

*[Verification-audit note: the locked slate gave an incoherent formula; the correct answer via the "last-position symmetry" trick is $\dfrac{k}{m + n + k}$. Verified at $m = n = k = 1$ by direct enumeration (gives $1/3$ ✓). The slate is patched in v0.2.10; see the appendix solution for the symmetry argument.]*

### 5.6 50-Subset with No Two Summing to 100 Contains a Perfect Square (Tier 3 RMO; Joshi Ch. 24, Exercise 24.73)

Let $A \subseteq \{1, 2, \ldots, 100\}$ be a $50$-element subset such that no two elements of $A$ sum to $100$. Prove that $A$ contains at least one perfect square.

### 5.7 Product Is 18, Event Occurs $\ge 3$ Times in $4$ Trials (Tier 2 JEE; Joshi Ch. 24, Exercise 24.54)

A two-digit number from $00, 01, \ldots, 99$ is selected uniformly at random. Event $E$ occurs iff the product of the two digits equals $18$. Four such numbers are selected independently with replacement. Find the probability that $E$ occurs at least $3$ times.

---

## 6. The Connections Web

Combinatorial principles connect to virtually every later archetype in this volume and to substantial parts of every quantitative discipline.

### 6.1 Combinatorial Principles Across Mathematical Domains

*Algebra.* The *binomial theorem* $(x + y)^n = \sum_k \binom{n}{k} x^k y^{n-k}$ is a combinatorial identity (the coefficient $\binom{n}{k}$ counts the ways to choose $k$ factors of $x$ from the $n$ factors of $(x + y)$). The *multinomial theorem* generalises this. *Power-sum symmetric functions, elementary symmetric polynomials, complete homogeneous symmetric polynomials* all have combinatorial-counting interpretations (Newton's identities, the Jacobi-Trudi formulas). *Representation theory of the symmetric group* (Young tableaux, the Robinson-Schensted-Knuth correspondence) is deeply combinatorial.

*Number theory.* The *number of divisors function* $d(n)$, the *Euler totient* $\varphi(n)$, the *Möbius function* $\mu(n)$, the *partition function* $p(n)$ — all are combinatorial counts with deep number-theoretic meaning. *Combinatorial number theory* (Erdős's school) develops counting bounds on additive structures (Schur numbers, Ramsey-type theorems, the Cauchy-Davenport theorem).

*Geometry.* *Combinatorial geometry* counts geometric incidences (Szemerédi-Trotter theorem on points-and-lines), packings (sphere packings in $\mathbb R^n$), and arrangements (the cell-counts of hyperplane arrangements). *Convex geometry* (Brunn-Minkowski, isoperimetric inequalities) and *combinatorial topology* (Sperner's lemma, the Brouwer fixed-point theorem proof) sit at the geometry-combinatorics boundary.

*Topology.* The *Euler characteristic* $\chi = V - E + F$ is a combinatorial invariant of triangulations. *Simplicial homology* counts equivalence classes of cycles modulo boundaries. *Combinatorial topology* (CW-complexes, simplicial complexes, the nerve theorem) is foundational in modern topology.

*Analysis.* The *Stirling formula* $n! \sim \sqrt{2\pi n} (n/e)^n$ is a combinatorial-asymptotic identity that recurs in probability (the central limit theorem), statistics (the chi-squared distribution), and analysis (the Wallis product, the gamma function). *Generating functions* encode combinatorial sequences as power series and recover combinatorial identities via complex analysis (Cauchy's formula, contour integration, the saddle-point method).

### 6.2 Combinatorial Principles in Probability, Statistics, and Information

*Probability.* The whole of *discrete probability* is combinatorial: the sample space is a finite set, the event is a subset, the probability is a ratio of cardinalities. *Binomial, hypergeometric, geometric, Poisson distributions* are all combinatorial. *Bayes' theorem* relates combinatorial conditional probabilities. *Markov chains* are combinatorial structures (states + transition probabilities) with rich asymptotic theory (mixing times, stationary distributions, hitting times).

*Statistics.* *Hypothesis testing*, *confidence intervals*, *p-values* all rest on combinatorial counts of rare events under the null hypothesis. *Combinatorial designs* (balanced incomplete block designs, Latin squares, orthogonal arrays) are the foundation of experimental design. *Sampling theory* (simple random sampling, stratified sampling, cluster sampling) uses combinatorial methods to bound sampling errors.

*Information theory.* *Shannon entropy*, *channel capacity*, *Kolmogorov complexity*, *source coding*, *channel coding* — all are combinatorial. The *typical sequence* concept rests on counting binary sequences with bounded empirical entropy. *Error-correcting codes* (Hamming, Reed-Solomon, BCH, LDPC) are combinatorial designs over finite fields.

*Cryptography.* The *key space* of a cipher is a combinatorial set. The *birthday paradox* (the probability of a collision in $\sqrt{n}$ samples from an $n$-element set) is a basic combinatorial result with cryptographic implications (hash-function security, the birthday attack on signatures).

*Statistical mechanics.* *Microstate counts* (the number of accessible configurations at fixed energy), *partition functions*, *thermodynamic entropies* (Boltzmann's $S = k_B \ln W$) — all combinatorial. *Phase transitions* are sharp combinatorial transitions in the typical-microstate behaviour as a parameter (temperature, density) crosses a threshold.

### 6.3 Cross-Domain Manifestations

*Music.* *Combinatorial music theory* counts melodies, chord progressions, rhythmic patterns. *Twelve-tone serial composition* (Schoenberg, Webern, Berg) uses combinatorial permutations of the twelve-tone row. *Combinatorial harmony* counts pitch-class sets and their transformations.

*Architecture.* *Combinatorial tilings* (regular and semiregular tessellations, aperiodic tilings like Penrose's) decorate buildings and inform structural engineering. *Combinatorial arrangements* of structural elements (columns, beams, panels) constrain architectural design.

*Linguistics.* *Combinatorial morphology* counts the possible word-forms from a stem (prefixes, suffixes, inflections). *Combinatorial syntax* counts the possible sentence-structures from a grammar. *Generative grammars* (Chomsky, Montague) are combinatorial systems.

*Biology.* *Combinatorial genetics* (Mendelian ratios, linkage analysis, recombination probabilities). *Combinatorial immunology* (the $10^{11}$+ possible antibody configurations from V(D)J recombination). *Combinatorial neuroscience* (neural-coding combinatorics, the *combinatorial explosion* of synaptic configurations).

*Economics and game theory.* *Combinatorial auctions* (bidding on bundles), *matching markets* (Roth-Shapley, kidney exchange, medical-residency matching), *combinatorial mechanism design*. *Cooperative game theory* (the Shapley value, the core) counts combinatorial coalitions.

### 6.4 Related Archetypes

Combinatorial principles interact with five other archetypes in particularly tight ways.

- **Archetype 1 (Invariance).** *Parity invariants*, *modular invariants*, *colouring invariants* are all combinatorial. The *invariant-counting* (counting structures preserved by a transformation) is a frequent move in olympiad combinatorics.

- **Archetype 2 (Symmetry).** *Burnside's lemma* (the average number of fixed points of group elements equals the number of orbits) is the formal version of the *symmetry-then-divide* pattern, and the foundation of *Pólya enumeration theory*. Chapter 2 (Symmetry) and Chapter 13 (Combinatorial Principles) interlock at Burnside.

- **Archetype 14 (Parity / Modular Reasoning).** *Parity-counting* (the number of objects with a given parity) is a combinatorial move that Chapter 14 will name and systematise. The technique is foundational for olympiad problems (the cake-shape problem, the chessboard-domino tilings, the colouring-as-invariance arguments).

- **Archetype 15 (Bijection / Correspondence).** *Bijective proofs* are the most elegant style of combinatorial proof — instead of computing both sides and verifying equality, construct an explicit bijection between the two sets being counted. Chapter 15 (Bijection / Correspondence) develops this technique fully.

- **Archetype 18 (Recursion / Induction).** *Combinatorial recurrences* (Fibonacci, Catalan, Stirling, derangements, partition numbers) encode the structure of combinatorial counts via recursion. The closed-form solutions of these recurrences (e.g., the Binet formula for Fibonacci) are powerful structural identities.

---

## 7. Master Takeaways

Seven sentences. Each one is a complete operational principle.

1. *Structure first, then count.* (The canonical takeaway.)

2. *Translate combinatorial-configuration problems to the subset-lattice; use chain-vs-non-chain dichotomy to find incomparable elements.* (WE1 takeaway; the dance-party problem and its cousins in extremal set theory.)

3. *Surjective-function count via inclusion-exclusion: $\sigma(n, m) = \sum_{k=0}^m (-1)^k \binom{m}{k}(m-k)^n$.* (WE2 takeaway; the prototypical inclusion-exclusion application.)

4. *Complementary counting: when the complement is easier than the direct count, compute the complement and subtract from the universe.* (WE3 takeaway; the universal shortcut for "at least one" or "missing some" problems.)

5. *Symmetry-then-divide (Burnside in baby form): count ordered configurations; divide by the order of the symmetry group of indistinguishability.* (Opening-vignette takeaway; the most-used pattern in unordered-counting problems.)

6. *Last-position symmetry: in a random permutation of $n$ items, the colour / type at the last position is uniformly distributed over all $n$ items; use this to convert "which type survives" or "which item is last" questions into trivial probabilities.* (PP5 takeaway; the powerful symmetry trick for stopping-time problems.)

7. *Cross-archetype: combinatorial principles interlock with Symmetry (Burnside), Parity (parity-counting), Bijection (bijective proofs), and Recursion (combinatorial recurrences) — by Chapter 13 these are one coherent body of structured counting.*

---

## 8. Self-Assessment Checklist

You have absorbed Chapter 13 when, without re-opening it, you can do each of the following from memory.

- [ ] State the multiplication principle and the addition principle, and identify their signatures (independent stages, disjoint cases).
- [ ] State the inclusion-exclusion principle for finite unions and apply it to compute $|A \cup B|$, $|A \cup B \cup C|$.
- [ ] Derive the surjective-function count $\sigma(n, m) = \sum_{k=0}^m (-1)^k \binom{m}{k}(m-k)^n$ via inclusion-exclusion on the "missed-element" sets, and verify $\sigma(4, 2) = 14$.
- [ ] State the stars-and-bars formula: the number of non-negative-integer solutions of $x_1 + \cdots + x_k = n$ is $\binom{n + k - 1}{k - 1}$; the number of positive-integer solutions is $\binom{n - 1}{k - 1}$.
- [ ] State the pigeonhole principle (basic and generalised) and apply it to forced-coincidence problems.
- [ ] State the bijective principle ($|A| = |B|$ iff there exists a bijection $A \leftrightarrow B$) and give one example of a bijective proof (e.g., $\binom{n}{k} = \binom{n}{n - k}$ via complementation).
- [ ] State the symmetry-then-divide pattern (Burnside in baby form) and apply it to count unordered groupings (e.g., the opening vignette's $\binom{30}{6,6,6,6,6}/5!$).
- [ ] State the binomial distribution: probability of exactly $k$ successes in $n$ independent Bernoulli($p$) trials is $\binom{n}{k} p^k (1-p)^{n-k}$.
- [ ] State the *last-position symmetry trick*: in a random permutation, the colour / type at the last position is uniformly distributed; apply to PP5-style problems.
- [ ] Identify and explain three of the five common pitfalls: Over-Counting, Under-Counting, Inclusion-Exclusion-Misapplied, Complementary-Counting-Misapplied, Pigeonhole-Mis-set-up.

---

## Bridge to Chapter 14: Parity / Modular Reasoning

Chapter 13 opened the *Structural Reasoning* sub-pillar (Chapters 13–16). The chapter developed the foundations of *counting structured collections*: the multiplication and addition principles; inclusion-exclusion; complementary counting; the pigeonhole principle; the bijective principle; the symmetry-then-divide pattern; the binomial distribution. With Chapter 13 in hand, the reader has internalised that *the structure of a count is the first thing to identify, before any enumeration begins* — the canonical *structure-first principle* of this sub-pillar.

Chapter 14 — *Parity / Modular Reasoning* — continues the *Structural Reasoning* sub-pillar by narrowing the focus from *all structural counting tools* to a *single, immensely powerful tool*: the recognition that the *residue modulo some integer* of a quantity is often all the structure that matters. *Parity* (residue mod 2) is the simplest and most-used case — many olympiad problems (chessboard tilings, coin-flipping games, the cake-cutting problem) have parity solutions of stunning brevity. *Modular arithmetic* (residue mod $m$ for $m > 2$) generalises parity and unlocks number-theoretic problems (Kummer's theorem on binomial-coefficient $p$-divisibility, Lucas's theorem on $\binom{n}{k} \bmod p$, the Chinese Remainder Theorem on simultaneous congruences). The cognitive shift: from *compute the exact value* to *compute the value modulo $m$, which is the value that determines the answer*. Many problems that look intractable at full precision (e.g., what is $7^{100} \bmod 13$?) collapse to a single multiplication after the right modular reduction. Chapter 14 will develop the toolkit (Fermat's little theorem, Euler's theorem, the Chinese Remainder Theorem, the *p*-adic valuation, Kummer's theorem) and the recurring patterns (parity-as-invariance, colouring-as-modular-invariance, modular obstructions, Mihailescu's theorem and its descendants).

The bridge from Ch. 13 to Ch. 14 is the *parity-counting* idea: many of the combinatorial counts Ch. 13 developed have a *parity invariant* (the count's parity is determined by structural features, even when the exact value is hard to compute). Chapter 14 will elevate parity-counting from a Chapter-13 technique to a Chapter-14 named principle.

---

## Appendix — Solutions to Practice Problems

### Solution to 5.1 — Three Numbers Summing to $2p$

We count the favourable triples $(a, b, c)$ with $1 \le a, b, c \le p$ and $a + b + c = 2p$, then divide by the sample-space size $p^3$.

*Step 1 — Count compositions without the upper bound.* The number of triples $(a, b, c)$ of positive integers (no upper bound) with $a + b + c = 2p$ is (by stars-and-bars, positive-integer version) $\binom{2p - 1}{2}$.

*Step 2 — Subtract violations of the upper bound.* Let $V_i = \{(a, b, c) : a + b + c = 2p, a_i \ge p + 1\}$ for $i = 1, 2, 3$. To compute $|V_1|$ (the violation $a \ge p + 1$): substitute $a' = a - p \ge 1$; the equation becomes $a' + b + c = 2p - p = p$, with $a', b, c \ge 1$. The number of positive-integer solutions is $\binom{p - 1}{2}$.

By the symmetry of the problem in $a, b, c$, $|V_1| = |V_2| = |V_3| = \binom{p - 1}{2}$.

*Step 3 — Pair-violations are empty.* For $|V_1 \cap V_2|$ (both $a \ge p + 1$ and $b \ge p + 1$): substitute $a' = a - p, b' = b - p$ each $\ge 1$; the equation becomes $a' + b' + c = 0$, with $a', b' \ge 1$ and $c \ge 1$. This requires $a' + b' + c \ge 3 > 0$ — impossible. So $|V_1 \cap V_2| = 0$, and similarly for all other pair-intersections.

By inclusion-exclusion, $|V_1 \cup V_2 \cup V_3| = 3 \binom{p - 1}{2}$.

*Step 4 — Favourable count.*
\[
  N \;=\; \binom{2p - 1}{2} - 3 \binom{p - 1}{2} \;=\; (2p - 1)(p - 1) - \frac{3(p - 1)(p - 2)}{2} \;=\; (p - 1) \cdot \frac{2(2p - 1) - 3(p - 2)}{2} \;=\; (p - 1) \cdot \frac{p + 4}{2}.
\]

*Step 5 — Probability.*
\[
  P \;=\; \frac{N}{p^3} \;=\; \frac{(p - 1)(p + 4)}{2 p^3}.
\]
$\blacksquare$

---

### Solution to 5.2 — Inscribed Triangles via Polygon Vertices

The number of triangles with vertices among the $n$ vertices of a regular $n$-gon is the number of $3$-subsets of an $n$-set: $T_n = \binom{n}{3}$.

By Pascal's identity:
\[
  T_{n+1} - T_n \;=\; \binom{n + 1}{3} - \binom{n}{3} \;=\; \binom{n}{2}.
\]
Setting $\binom{n}{2} = 21$: $\frac{n(n - 1)}{2} = 21$, so $n(n - 1) = 42$, giving $n^2 - n - 42 = 0$, $n = \frac{1 \pm \sqrt{1 + 168}}{2} = \frac{1 \pm 13}{2}$, so $n = 7$ or $n = -6$. Since $n \ge 3$, $\boxed{n = 7}$. $\blacksquare$

*Cross-archetype note.* This problem also appears as Ch. 9 PP2 (Domain Constraints), where the *integer-domain* filter is the primary cognitive lens — the algebraic solution $n^2 - n - 42 = 0$ gives two roots, and only the positive integer $n = 7$ lies in the domain. Here in Ch. 13, the *combinatorial-identity* lens is primary — the cognitive move is recognising $T_n = \binom{n}{3}$ and applying Pascal's identity to the difference.

---

### Solution to 5.3 — Tournament Pairing

*(a) Probability $S_1$ is among the winners.*
By symmetry, each of the $16$ players has equal probability $\tfrac{1}{2}$ of winning their match (the coin flip is fair). So $P(S_1 \text{ wins}) = \boxed{\tfrac{1}{2}}$.

*(b) Probability that exactly one of $S_1, S_2$ wins.*
Condition on whether $S_1$ and $S_2$ are paired with each other.

*Case 1: $S_1, S_2$ paired (probability $\tfrac{1}{15}$).* The probability that a given player ($S_1$) is paired with another specific player ($S_2$) is $\tfrac{1}{15}$, since after fixing $S_1$'s position, the other $15$ players are equally likely to be $S_1$'s opponent. Given they are paired: exactly one wins (one beats the other; it is *impossible* that both or neither wins). So $P(\text{exactly one} \mid \text{paired}) = 1$.

*Case 2: $S_1, S_2$ not paired (probability $\tfrac{14}{15}$).* Now $S_1$ and $S_2$ play in *different* matches, against opponents who are not each other. Each wins their match independently with probability $\tfrac{1}{2}$. The four outcomes (each wins independently) give $P(\text{both win}) = \tfrac{1}{4}, P(\text{both lose}) = \tfrac{1}{4}, P(\text{exactly one wins}) = \tfrac{1}{2}$.

*Total.* By the law of total probability:
\[
  P(\text{exactly one wins}) \;=\; \frac{1}{15} \cdot 1 + \frac{14}{15} \cdot \frac{1}{2} \;=\; \frac{1}{15} + \frac{7}{15} \;=\; \boxed{\frac{8}{15}}.
\]
$\blacksquare$

*Verification by complementary check.*
$P(\text{both win}) = P(\text{paired}) \cdot 0 + P(\text{not paired}) \cdot \tfrac{1}{4} = 0 + \tfrac{14}{15} \cdot \tfrac{1}{4} = \tfrac{7}{30}$.
$P(\text{both lose}) = \tfrac{7}{30}$ by symmetry.
$P(\text{exactly one}) = 1 - 2 \cdot \tfrac{7}{30} = 1 - \tfrac{14}{30} = \tfrac{16}{30} = \tfrac{8}{15}$. ✓

*Correction note.* The locked slate v0.2 stated the answer as $\frac{8}{15} \cdot \tfrac{1}{2} = \tfrac{4}{15}$. This was wrong: the multiplication by $\tfrac{1}{2}$ appears to come from confusing $P(\text{exactly one}) = \tfrac{1}{2}$ in Case 2 with the *overall* probability (which requires the total-probability law combining both cases). The correct answer $\tfrac{8}{15}$ matches the JEE 1997 answer key. Slate patched in v0.2.10.

---

### Solution to 5.4 — Two Queens Non-Taking

We use complementary counting: count *taking* pairs (queens in the same row, column, or diagonal) and subtract from the total $\binom{64}{2}$.

*Total pairs.* $\binom{64}{2} = \dfrac{64 \cdot 63}{2} = 2016$.

*Same-row pairs.* $8$ rows, each with $\binom{8}{2} = 28$ pairs: $8 \cdot 28 = 224$.

*Same-column pairs.* By symmetry with rows: $224$.

*Same-diagonal pairs.* The board has diagonals (going $\searrow$) of lengths $1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1$. The number of pairs on a diagonal of length $\ell$ is $\binom{\ell}{2}$. Summing:
\[
  \sum_{\text{diagonals } \searrow} \binom{\ell}{2} \;=\; 2 \sum_{\ell = 1}^{7} \binom{\ell}{2} + \binom{8}{2} \;=\; 2 \cdot (0 + 1 + 3 + 6 + 10 + 15 + 21) + 28 \;=\; 2 \cdot 56 + 28 \;=\; 140.
\]
Similarly for diagonals going $\swarrow$: another $140$ pairs.

*Total taking pairs.* $224 + 224 + 140 + 140 = 728$.

*Non-taking pairs.* $2016 - 728 = 1288$.

*Probability.*
\[
  P(\text{non-taking}) \;=\; \frac{1288}{2016} \;=\; \frac{161}{252} \;=\; \boxed{\frac{23}{36}}.
\]
($\gcd(1288, 2016) = 56$; $1288/56 = 23, 2016/56 = 36$.) $\blacksquare$

The cognitive move: *complementary counting* (count taking; subtract) is far cleaner than counting non-taking directly (which would require partitioning into row-non-shared, column-non-shared, diagonal-non-shared cases with overlapping conditions).

---

### Solution to 5.5 — Box with Three Colours, Red Last

We use the *last-position symmetry* trick.

*Step 1 — Reframe.* Instead of analysing the stopping process, *extend* the process: continue drawing balls until *every* ball is drawn. The "surviving colour" (the one whose balls remain when the original process stops) is precisely the colour whose *last representative* is drawn last in the extended sequence.

Equivalently, place all $m + n + k$ balls in a uniformly random permutation. Look at the *colour of the ball in the last (i.e., position $m + n + k$) slot*. This is the surviving colour:
- If the last ball is red, then all white and black balls are drawn before the last red ball, so when the original process is at the point where every white and every black ball has been drawn, only red balls remain, and the process stops with red as the survivor.
- Similarly for white and black.

*Step 2 — Probability via symmetry.* In a uniformly random permutation of $m + n + k$ balls (each labelled by its colour), the colour of the ball in any *fixed* position (in particular, the last position) is determined by *which colour* the ball at that position is. Since each individual ball is equally likely to be in the last position:
\[
  P(\text{last position is red}) \;=\; \frac{\text{number of red balls}}{\text{total number of balls}} \;=\; \frac{k}{m + n + k}.
\]
So
\[
  P(\text{red is the surviving colour}) \;=\; \boxed{\dfrac{k}{m + n + k}}.
\]
$\blacksquare$

*Verification.* Take $m = n = k = 1$ (one each of white, black, red). The $3!= 6$ permutations of the balls are:
- $W, B, R$: last is $R$. Survivor = $R$. ✓
- $W, R, B$: last is $B$. Survivor = $B$.
- $B, W, R$: last is $R$. Survivor = $R$. ✓
- $B, R, W$: last is $W$. Survivor = $W$.
- $R, W, B$: last is $B$. Survivor = $B$.
- $R, B, W$: last is $W$. Survivor = $W$.

$P(\text{red is survivor}) = 2/6 = 1/3$. Formula: $k/(m + n + k) = 1/(1 + 1 + 1) = 1/3$. ✓

*Correction note.* The locked slate v0.2 gave an incoherent formula "$\dfrac{k}{m + n + k} \cdot (\dfrac{k+1}{k+2} + \cdots)$" plus a "symmetry formula" $\dfrac{k}{m+k} \cdot \dfrac{k}{n+k}$ which fails at $m = n = k = 1$ (gives $1/4$, not $1/3$). The correct answer via the last-position symmetry is $\dfrac{k}{m + n + k}$. Slate patched in v0.2.10.

*Generalisation.* The same symmetry trick generalises to *any* number of colours: with $n_1, n_2, \ldots, n_c$ balls of colours $1, 2, \ldots, c$ respectively, the probability that colour $i$ is the surviving colour is $n_i / (n_1 + \cdots + n_c)$. This is a beautifully clean instance of the *exchangeability* of random permutations.

---

### Solution to 5.6 — 50-Subset with No Two Summing to 100 Contains a Perfect Square

*Step 1 — Pair the elements of $\{1, \ldots, 100\}$.*
For $k \in \{1, 2, \ldots, 49\}$, pair $k$ with $100 - k$: pairs $\{1, 99\}, \{2, 98\}, \ldots, \{49, 51\}$ ($49$ pairs).
The remaining elements have no distinct partner summing to $100$: namely $50$ (since $100 - 50 = 50$ is itself, not a distinct partner) and $100$ (since $100 - 100 = 0 \notin \{1, \ldots, 100\}$). These are *singletons*: $\{50\}, \{100\}$.

Total: $49$ pairs + $2$ singletons = $49 \cdot 2 + 2 = 100$ elements. ✓

*Step 2 — Constraint on $A$.* The set $A$ has $50$ elements and no two of them sum to $100$. From each pair $\{k, 100 - k\}$ (with $k \in \{1, \ldots, 49\}$), $A$ can contain *at most one* element (else two of them would sum to $100$). From the singletons $\{50\}$ and $\{100\}$, $A$ can contain either or both freely (since $50 + 50 = 100$ is a sum of $50$ with *itself*, which the "no two distinct elements" condition does not forbid; and $100$ has no partner in the set).

So $A$ has the form: pick at most one element from each of the $49$ pairs (call $r$ = number of pairs from which we pick one, so $0 \le r \le 49$), plus possibly the singletons $50$ and/or $100$ (call $s$ = number of singletons we pick, so $0 \le s \le 2$). Total: $r + s = 50$.

The only feasible cases are $(r, s) = (49, 1)$ or $(r, s) = (48, 2)$ (since $r \le 49$ and $s \le 2$, and $r + s = 50$).

*Step 3 — Identify perfect-square pairs.* The perfect squares in $\{1, \ldots, 100\}$ are $\{1, 4, 9, 16, 25, 36, 49, 64, 81, 100\}$ — ten squares.

Which pair (or singleton) does each square belong to?
- $1 \in \{1, 99\}$
- $4 \in \{4, 96\}$
- $9 \in \{9, 91\}$
- $16 \in \{16, 84\}$
- $25 \in \{25, 75\}$
- $36 \in \{36, 64\}$ — note: $64$ is also a square, so this pair contains *two* squares.
- $49 \in \{49, 51\}$
- $64 \in \{36, 64\}$ — same pair as $36$.
- $81 \in \{19, 81\}$
- $100 \in \{100\}$ — singleton.

So there are $8$ pairs that contain at least one square, plus the singleton $\{100\}$ (which is itself a square). Of those $8$ pairs, $7$ pairs contain exactly one square (namely $\{1,99\}, \{4,96\}, \{9,91\}, \{16,84\}, \{25,75\}, \{49,51\}, \{19,81\}$) and one pair contains two squares (namely $\{36, 64\}$).

*Step 4 — Case analysis.*

*Case $(r, s) = (49, 1)$:* $A$ contains one element from each of the $49$ pairs (so all $49$ pairs contribute one element to $A$), plus one of $\{50\}, \{100\}$.

The pair $\{36, 64\}$ is one of the $49$ pairs, and *both* of its elements ($36$ and $64$) are perfect squares. So whichever element of this pair $A$ picks, $A$ contains a perfect square ($36$ or $64$). ✓

*Case $(r, s) = (48, 2)$:* $A$ contains one element from $48$ of the $49$ pairs (skipping one pair) plus both singletons $\{50, 100\}$.

The singleton $100$ is a perfect square, and $100 \in A$. So $A$ contains the perfect square $100$. ✓

*Step 5 — Conclude.* In both cases, $A$ contains at least one perfect square. \hfill$\blacksquare$

*Structural observation.* The clinching mechanism is the *double-square pair* $\{36, 64\}$ combined with the *square singleton* $\{100\}$. Without either of these structural features (e.g., if the problem replaced $\{1, \ldots, 100\}$ with $\{1, \ldots, 99\}$, eliminating the square $100$, OR if the squares didn't happen to pair up at $\{36, 64\}$), the argument would fail. The problem's *specific* structural coincidence — that $36 + 64 = 100$ — is what makes the conclusion work.

---

### Solution to 5.7 — Product Is 18, Event $\ge 3$ Times in $4$ Trials

*Step 1 — Compute $P(E)$.*
We pick a two-digit number (treating $00$–$99$ as $100$ equally likely outcomes, including leading zeros). Event $E$: the product of the two digits equals $18$.

Digit pairs $(a, b) \in \{0, 1, \ldots, 9\}^2$ with $a \cdot b = 18$:
- $a \cdot b = 18 \Rightarrow$ both $a, b > 0$ (since $0$ gives product $0$).
- Factorisations: $18 = 1 \times 18 = 2 \times 9 = 3 \times 6 = 6 \times 3 = 9 \times 2 = 18 \times 1$.
- Restrict to single digits ($1 \le a, b \le 9$): exclude $1 \times 18$ and $18 \times 1$ (since $18 > 9$).
- Valid pairs: $(2, 9), (3, 6), (6, 3), (9, 2)$ — $4$ pairs.

So $P(E) = 4/100 = 1/25 = 0.04$.

*Step 2 — Apply binomial distribution.*
Four numbers are drawn independently with replacement; each is in $E$ with probability $p = 1/25$, not in $E$ with probability $q = 24/25$.

Let $X$ = number of times $E$ occurs in 4 trials; $X \sim \text{Binomial}(4, 1/25)$.

$P(X \ge 3) = P(X = 3) + P(X = 4) = \binom{4}{3} p^3 q + \binom{4}{4} p^4 = 4 p^3 q + p^4 = p^3 (4q + p)$.

*Step 3 — Compute.*
\[
  p^3 \;=\; \frac{1}{25^3} \;=\; \frac{1}{15625}, \quad
  4q + p \;=\; \frac{96}{25} + \frac{1}{25} \;=\; \frac{97}{25}.
\]
\[
  P(X \ge 3) \;=\; \frac{1}{15625} \cdot \frac{97}{25} \;=\; \boxed{\frac{97}{390625}}.
\]
$\blacksquare$

In decimal: $P(X \ge 3) \approx 2.48 \times 10^{-4} \approx 0.0002483$. The "at least 3" event is extremely rare, as expected: with $p$ as small as $1/25$, three or more occurrences out of four trials is roughly $(1/25)^3 \approx 6 \times 10^{-5}$ probability per ordered triple, times the small combinatorial factor.

---

*End of Chapter 13. Chapter 14 (Parity / Modular Reasoning) continues the Structural Reasoning sub-pillar.*

