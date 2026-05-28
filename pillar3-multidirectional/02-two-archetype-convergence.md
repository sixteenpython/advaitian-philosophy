---
chapter: 2
pillar: 3
title: "Two-Archetype Convergence"
subtitle: "*The atom of multidirectional solving.*"
length_target_words: 7500
canonical_takeaway: "Half of multidirectional solving is identifying which two archetypes converge; the other half is recognising which one drives and which one enables."
status: draft
last_revised: 2026-05-28
references_invoked: [Engel-ch-1, Engel-ch-3, Engel-ch-8, Zeitz-ch-3, Zeitz-ch-4, Joshi-ch-1]
canonical_constructs_used: [convergence-diagram, escape-hatch]
---

# Chapter 2 — Two-Archetype Convergence

*The atom of multidirectional solving.*

---

## §0 Opening Vignette — Anjali Deshmukh's notebook

In November, Anjali Deshmukh, a second-year electrical engineering student at IIT Bombay, finishes her INMO selection-test preparation by performing an unusual exercise. She has solved 50 problems from a stack of past olympiad papers over the last seven weeks. Instead of moving on, she opens a fresh notebook and spends three evenings cataloguing all 50 problems by their archetype profile. For each problem she records: the chosen archetype(s), whether the solution required one archetype or two or three, and — for the failures — what she had gotten wrong.

The catalogue produces a striking pattern. Of her 50 problems:
- **8** were single-archetype problems. She solved them all in under five minutes each.
- **38** were two-archetype problems. Of these, she solved 32 correctly. For the 6 she missed, the catalogue showed a recurring failure mode: in 5 of those 6, she had correctly identified the *first* archetype but had paired it with the *wrong second* archetype, leading to forty minutes of attempted derivation that produced nothing.
- **4** were three-archetype problems. She solved 1 of those 4. The other 3 she left blank after over an hour of attempts.

The catalogue, in other words, is dominated by two-archetype problems. They are the bulk of INMO-level problems, the bulk of JEE Advanced's hardest problems, and — although she will discover this later — the bulk of the lower-tier IMO problems too. Her failure rate on single-archetype problems is zero; her failure rate on two-archetype problems is about 16%; her failure rate on three-archetype problems is 75%. The difficulty cliff is not between "easy" and "hard" but between "one archetype loaded" and "two archetypes loaded simultaneously".

She finishes the catalogue exercise on a Sunday evening. On Monday morning she pulls out a fresh problem from a Tournament of Towns 1989 paper. Before writing anything, she draws the 2-archetype convergence diagram on the top half of the page, writes the candidate first archetype in the left box, and *intentionally leaves the right box blank*. She forces herself to brainstorm three different candidates for the right box before committing to one. The problem yields in eleven minutes.

She does the same for the next problem. And the next.

By December, her INMO mock-test scores have risen from a mid-range 32/120 to a top-decile 71/120. The catalogue exercise, she will later say, was the single highest-leverage thing she did in her INMO preparation. It taught her not a new technique but a new *diagnostic habit*: always name two archetypes before writing anything down.

**This is the discipline of Chapter 2.**

---

## §1 The Pattern

### §1.1 The 2-archetype convergence diagram, instantiated

Recall the 2-archetype convergence diagram from Chapter 1 §1.1. In its abstract form, the diagram has two unlabelled archetype-application boxes that converge at the CEP. The discipline of Chapter 2 is to *instantiate* this diagram for every problem: that is, to fill in the *specific* archetype-pair before any computation, and to identify the *specific* convergence move.

The 20 archetypes of Pillar 2 can be paired in $\binom{20}{2} = 190$ distinct unordered ways. Of these 190 possible pairs, only about **30–40 occur with significant frequency** in the standard problem corpus (Engel, Zeitz, Joshi, IMO, Putnam). The remaining 150 pairs do occur, but rarely. The 30–40 frequent pairs are what we will call the **canonical pairs**, and recognising them on sight is the principal skill this chapter trains.

### §1.2 The Common Convergence Patterns (CCPs)

The eight most-frequent canonical pairs, with one representative problem each, are:

| # | Pair | Representative problem (source) |
|---|---|---|
| CCP-1 | **#1 Invariance + #14 Parity/Modularity** | Engel Ch. 1 E2 (the blackboard $|a-b|$ problem) — *treated below as Worked Example 1* |
| CCP-2 | **#2 Symmetry + #8 Domain Translation** | Zeitz Ex 3.1.5 (Carry Water to Grandma) — *treated below as Worked Example 2* |
| CCP-3 | **#18 Induction + #12 Extremal** | Engel Ch. 8 Problem 2 (cars on a circular track) — *treated below as Worked Example 3* |
| CCP-4 | **#13 Combinatorial + #14 Parity/Modularity** | Czech & Slovak 1995 (treated in Ch. 1 WE3) |
| CCP-5 | **#13 Combinatorial + #12 Extremal** | Engel Ch. 4 5-points-in-unit-square (treated in Ch. 1 WE2) |
| CCP-6 | **#12 Extremal + #2 Symmetry** | Sylvester–Gallai (sketched in Ch. 1 §0) |
| CCP-7 | **#5 Substitution + #11 Existence** | Engel Ch. 11 functional equations (treated in Ch. 6 Case Study #5) |
| CCP-8 | **#4 Hidden Structure + #5 Substitution** | IMO 1969 P1 — $z = x^4 + y^4 + (x+y)^4 = 2(x^2+xy+y^2)^2$ (Pillar 4 Case Study 2 territory) |

You will recognise that you have already seen CCPs 4, 5, and 6 in Chapter 1. CCPs 1, 2, 3 are this chapter's focus. CCPs 7 and 8 will be developed in subsequent chapters (Ch. 6 for CCP-7; Pillar 4 Ch. 4 for CCP-8). Together, these eight pairs account for roughly **two-thirds of all 2-archetype problems** in the standard olympiad corpus. The remaining one-third spreads across about 20–25 additional pairs.

**Why does the distribution concentrate this way?** Three structural reasons:

1. *Some archetypes naturally pair with many others.* #1 Invariance, #12 Extremal, #13 Combinatorial, and #14 Parity each pair with at least six other archetypes in mainstream problems. They are *high-valence* archetypes. Other archetypes (#7 Normalisation, #17 DOF Analysis) are *low-valence* — they appear most often as solo techniques or as third archetypes in 3-archetype problems.

2. *Some pairs are structurally complementary.* CCP-1 (Invariance + Parity) pairs together because parity is a particular kind of invariant, so the two archetypes operate on the same underlying mathematical object (mod-$n$ arithmetic) from different cognitive directions: Invariance gives the *abstract* hold ("there is a conserved quantity"), Parity gives the *concrete* hold ("the conserved quantity is the sum mod 2"). The two views converge on the same proof.

3. *Some pairs are structurally orthogonal.* CCP-2 (Symmetry + Domain Translation) pairs together precisely because they act on *different* aspects of the problem — one transforms the configuration, the other transforms the representation. Their orthogonality is exactly what makes them combinable: there is no conflict to resolve.

The taxonomy of high-valence/low-valence and complementary/orthogonal archetype pairs is the structural backbone of Chapter 2. You will internalise it through the three worked examples below, each of which exhibits one of the canonical pairs in detail.

### §1.3 The driver/enabler distinction

Within any 2-archetype convergence, one of the two archetypes is the **driver** and the other is the **enabler**. The driver is the archetype that determines the *shape* of the proof — what assumption is made, what intermediate result is sought, what contradiction is forced. The enabler is the archetype that supplies the *toolkit* that lets the driver close.

In Worked Example 1 (CCP-1: Invariance + Parity), Invariance is the driver — it tells us *"find a conserved quantity"* — and Parity is the enabler, providing the specific computational tool (sum mod 2). Without Invariance the parity computation would be a side observation with no proof-structural role; without Parity the Invariance principle would have nothing concrete to bite.

In Worked Example 2 (CCP-2: Symmetry + Domain Translation), Domain Translation is the driver — it says *"reformulate the problem in a different domain where the structure is visible"* — and Symmetry is the enabler, identifying *which* domain transformation to use (the reflection across the stream). Either archetype alone is paralysed; together they produce a three-line proof.

In Worked Example 3 (CCP-3: Induction + Extremal), Extremal is the driver — it tells us *"choose the minimum-cumulative-gas car"* — and Induction is the enabler, providing the inductive framework that lifts the single-car observation into a proof for all $n$.

Identifying which archetype drives and which enables is *the* diagnostic move of Chapter 2. We will return to this distinction in §3 (The Trap), where the failure mode is precisely a mis-assignment of driver and enabler.

---

## §2 Worked Examples

### Worked Example 2.1 — Engel's blackboard parity problem (CCP-1)

*Source.* Engel, *Problem-Solving Strategies*, Ch. 1 Example E2 (p. 2).
*Archetypes invoked.* **#1 Invariance (driver) + #14 Parity/Modularity (enabler).**
*Convergence type.* 2-archetype convergence.

**Problem.** Suppose the positive integer $n$ is odd. Al writes the numbers $1, 2, \ldots, 2n$ on the blackboard. He repeatedly picks any two numbers $a, b$, erases them, and writes $|a - b|$ in their place. (After each step, the count of numbers on the board drops by one.) After $2n - 1$ steps, only one number remains. Prove that this remaining number is odd.

**Convergence diagram.**

```
            ┌───────────────────────────────────────────────┐
            │ After 2n−1 steps of (a,b) → |a−b|,            │
            │ remaining number is odd (for odd n)           │
            └───────────────────────┬───────────────────────┘
                                    │
        ┌───────────────────────────┴───────────────────────────┐
        │                                                       │
        ▼                                                       ▼
┌──────────────────────────┐                  ┌─────────────────────────────┐
│  #1 INVARIANCE (DRIVER)  │                  │  #14 PARITY (ENABLER)       │
│  Look for a conserved    │                  │  Compute sum mod 2:         │
│  quantity under the step │                  │  initial = n(2n+1)          │
│  (a,b) → |a−b|           │                  │  which is odd · odd = odd   │
│  Candidate: S = sum of   │                  │  Step changes S by          │
│  numbers on board        │                  │  −2·min(a,b), always even   │
└────────────┬─────────────┘                  └─────────────┬───────────────┘
             │                                              │
             │ ⇒ S mod 2 is conserved                       │ ⇒ S mod 2 ≡ 1
             │                                              │
             └────────────────────┬─────────────────────────┘
                                  ▼
                  ┌──────────────────────────────────┐
                  │ Convergence: final S ≡ 1 (mod 2) │
                  │ But final S = the lone remaining │
                  │ number; so it is odd             │
                  └─────────────────┬────────────────┘
                                    │
                                    ▼
                          ┌──────────────────┐
                          │   ODD            │
                          └──────────────────┘
```

**Solution walkthrough.**

*Stage 1 — applying #1 Invariance (driver).* The step $(a, b) \mapsto |a - b|$ replaces two numbers with one. Many candidate "invariants" suggest themselves: the count of numbers (decreases by 1 each step — not invariant), the sum $S = \sum a_i$ (changes by $a + b - |a-b| = 2\min(a,b)$ each step — not invariant in absolute terms), the GCD of all numbers (sometimes invariant, sometimes not), the parity of $S$ (changes by $2\min(a,b)$, which is always even, so parity of $S$ is preserved — **this is the invariant**). The driver-archetype identifies *that we should look for an invariant function*; the enabler-archetype, parity, supplies the specific function $S \bmod 2$. **Intermediate result $A'$ (driver): the parity of $S$ is invariant under each step.**

*Stage 2 — applying #14 Parity (enabler).* The initial value of $S$ is $1 + 2 + \cdots + 2n = n(2n+1)$. We are given that $n$ is odd. Then $n(2n+1)$ = (odd)$\cdot$(odd) = odd. So $S \equiv 1 \pmod 2$ initially. By the invariance of $S \bmod 2$, the final value of $S$ (which is the single remaining number) is also $\equiv 1 \pmod 2$. **Intermediate result $B'$ (enabler): the initial $S$ is odd; therefore the final $S$ — which is the single remaining number — is odd. $\Box$**

*Convergence.* The remaining number is odd, as required. $\boxed{\text{odd}}$.

**Commentary — driver and enabler.** Notice how cleanly the driver/enabler split applies here. The Invariance archetype, applied alone, would tell us *"look for a conserved quantity,"* but would not tell us *which* quantity to track. Tracking the wrong candidate (e.g., the sum itself rather than its parity) would lead to a dead end: the sum is not invariant, only its parity is. The Parity archetype is what *makes* the invariance approach succeed by supplying the correct invariant function. Conversely, Parity applied alone would compute that the initial sum is odd, but without the Invariance framework it would not realise that this parity-of-sum observation has any proof-structural significance — it would be a curiosity rather than a closing move. The driver tells us *the shape* of the proof; the enabler tells us *the function*. Internalising this driver/enabler distinction is the principal cognitive payoff of Chapter 2.

### Worked Example 2.2 — Zeitz's Carry-Water-to-Grandma (CCP-2)

*Source.* Zeitz, *The Art and Craft of Problem Solving* (3rd ed.), Example 3.1.5 (p. 60–61); cf. `Cursor-Zeitz.md` §V "2-Archetype Convergence" row 2.
*Archetypes invoked.* **#8 Domain Translation (driver) + #2 Symmetry (enabler).**
*Convergence type.* 2-archetype convergence.

**Problem.** Your cabin sits two miles due north of an east-west stream. Your grandmother's cabin is located 12 miles west and 1 mile north of yours. Every day, you walk from your cabin to your grandmother's, but first stop at the stream to fetch water for her. Find the shortest possible total walking distance.

**Convergence diagram.**

```
            ┌───────────────────────────────────────────────┐
            │ Minimise total distance Y → stream → G        │
            │ where stream is 2 mi south of Y;              │
            │ G is 12 mi west, 1 mi north of Y              │
            └───────────────────────┬───────────────────────┘
                                    │
        ┌───────────────────────────┴───────────────────────────┐
        │                                                       │
        ▼                                                       ▼
┌──────────────────────────┐                  ┌─────────────────────────────┐
│ #8 DOMAIN TRANSLATION    │                  │ #2 SYMMETRY (ENABLER)       │
│ (DRIVER)                 │                  │ Reflect G across the stream │
│ Reformulate "minimum     │                  │ to obtain G'; then any path │
│ broken-path Y→stream→G"  │                  │ Y→A→G with A on stream has  │
│ as "minimum straight-    │                  │ length |YA| + |AG|          │
│ path Y→G' in mirrored    │                  │ = |YA| + |AG'|              │
│ space"                   │                  │                             │
└────────────┬─────────────┘                  └─────────────┬───────────────┘
             │                                              │
             │ ⇒ Min Y→stream→G = min Y→A→G'                │ ⇒ Both legs
             │   over A on stream                           │   measured in
             │                                              │   mirrored space
             │                                              │
             └────────────────────┬─────────────────────────┘
                                  ▼
                  ┌──────────────────────────────────┐
                  │ Convergence: min |YA| + |AG'|    │
                  │ over A on stream = |YG'|         │
                  │ (the straight line YG'           │
                  │ minimises sum of two legs)       │
                  │ |YG'| = √(12² + 5²) = 13         │
                  └─────────────────┬────────────────┘
                                    │
                                    ▼
                          ┌──────────────────┐
                          │     13 miles     │
                          └──────────────────┘
```

**Solution walkthrough.**

*Stage 1 — applying #8 Domain Translation (driver).* The problem, as stated, is an optimisation over a free variable $A$ (the point on the stream where you fetch water). The objective is to minimise $|YA| + |AG|$, where $Y, A, G$ are points in the plane with $A$ constrained to the stream-line. This is a calculus problem if attacked directly — differentiate the sum-of-distances with respect to the $x$-coordinate of $A$, set the derivative to zero, solve for $A$, plug back into the objective. The differentiation is ugly (sum of two square-root expressions). The Domain Translation move *reformulates the problem in a different domain* where the structure is visible.

The reformulation: reflect $G$ across the stream-line to obtain $G'$. By the reflection identity, $|AG| = |AG'|$ for any point $A$ on the stream. Therefore $|YA| + |AG| = |YA| + |AG'|$. The original optimisation becomes: *minimise the length of a broken path from $Y$ to $G'$ that touches a chosen point $A$ on the stream-line on the way*. **Intermediate result $A'$ (driver): the problem is equivalent to an optimisation in the reflected-domain representation, where the legs are $|YA|$ and $|AG'|$.**

*Stage 2 — applying #2 Symmetry (enabler).* The Symmetry archetype is what *identifies the specific transformation* to use — namely, the reflection across the stream-line. (Why this reflection and not some other? Because the stream is the geometric locus of the constraint, and reflection across the constraint-locus is the natural symmetry of the problem.) The minimum of $|YA| + |AG'|$ over $A$ on any line is achieved when $Y$, $A$, $G'$ are collinear, by the triangle inequality applied in reverse (any broken-path is no shorter than the corresponding straight-line). **Intermediate result $B'$ (enabler): the minimum is $|YG'|$, achieved when $Y$, $A$, $G'$ are collinear.**

*Convergence.* Now compute $|YG'|$. Set up coordinates: $Y = (0, 2)$, stream-line is the $x$-axis. $G = (-12, 3)$ (12 miles west, 1 mile north of $Y$, with $Y$ at height 2 above the stream means $G$ is at height $2 + 1 = 3$ above the stream). Reflect: $G' = (-12, -3)$. Then $|YG'| = \sqrt{12^2 + 5^2} = \sqrt{144 + 25} = \sqrt{169} = 13$. $\boxed{13 \text{ miles}}$.

**Commentary — orthogonal archetypes.** Domain Translation and Symmetry are *orthogonal* archetypes (cf. §1.2 above): they act on different aspects of the problem. Domain Translation acts on the *representation* — it converts "minimise broken-path-in-physical-space" into "minimise straight-line-in-mirrored-space". Symmetry acts on the *configuration* — it identifies the specific reflection across the constraint-locus that makes the translation work. Because they are orthogonal, they combine trivially: there is no conflict to resolve. The driver-enabler split is also clean here: Domain Translation is the driver (it reshapes the problem), Symmetry is the enabler (it supplies the specific reshape). 

This problem also illustrates a *Pillar 4 CEP*: the answer is **13**, a Pythagorean triple (a Tier-2 CEP per Blueprint §8.2). The problem was *designed* — by whoever the original problem-setter was, lost to time — to have the 5–12–13 right triangle as its CEP. Pillar 4 Chapter 4 will revisit problems of this kind from the designer's perspective.

### Worked Example 2.3 — Engel's cars-on-a-circular-track (CCP-3)

*Source.* Engel, *Problem-Solving Strategies*, Ch. 8 Problem 2 (p. 207).
*Archetypes invoked.* **#12 Extremal Principles (driver) + #18 Induction (enabler).**
*Convergence type.* 2-archetype convergence.

**Problem.** There are $n$ identical cars on a circular racetrack. The total amount of gasoline distributed across the $n$ cars is exactly enough for one car to complete a single lap. (The distribution is otherwise arbitrary — some cars may have a lot of gas, others may have none.) Show that there is a car which, starting with its own gas tank and refuelling at each car it encounters along the way (consuming that car's entire remaining gas), can complete a full lap.

**Convergence diagram.**

```
            ┌───────────────────────────────────────────────┐
            │ Among n cars on a track with total fuel =    │
            │ exactly one lap, ∃ a starting car that can   │
            │ complete the lap (refuelling en route)       │
            └───────────────────────┬───────────────────────┘
                                    │
        ┌───────────────────────────┴───────────────────────────┐
        │                                                       │
        ▼                                                       ▼
┌──────────────────────────┐                  ┌─────────────────────────────┐
│ #12 EXTREMAL (DRIVER)    │                  │ #18 INDUCTION (ENABLER)     │
│ Consider the cumulative- │                  │ Lift the single-car         │
│ gas function f(θ) =      │                  │ observation to all n by     │
│ "gas accumulated by      │                  │ induction on n: when n=1    │
│ time car at angle θ"     │                  │ the lone car trivially      │
│ Pick the angle θ* at     │                  │ has 1 lap of fuel; assume   │
│ which f(θ) is minimum    │                  │ holds for n−1; prove for n  │
└────────────┬─────────────┘                  └─────────────┬───────────────┘
             │                                              │
             │ ⇒ Starting from θ*, cumulative               │ ⇒ Inductive step:
             │   gas is non-negative everywhere             │   merge the car at
             │                                              │   θ* with the next
             │                                              │   one, reducing to n−1
             │                                              │
             └────────────────────┬─────────────────────────┘
                                  ▼
                  ┌──────────────────────────────────┐
                  │ Convergence: the extremal car θ* │
                  │ completes the lap; induction     │
                  │ confirms ∀ n                     │
                  └─────────────────┬────────────────┘
                                    │
                                    ▼
                          ┌──────────────────┐
                          │ Such a car exists│
                          └──────────────────┘
```

**Solution walkthrough.**

*Stage 1 — applying #12 Extremal (driver).* Place the cars at angular positions $\theta_1, \theta_2, \ldots, \theta_n$ on the unit-circle track (parameterising the lap by total angle from $0$ to $1$ rather than $0$ to $2\pi$, so a full lap is at $\theta = 1$). Each car $i$ has gas $g_i \geq 0$, with $\sum g_i = 1$ (the total-fuel-equals-one-lap hypothesis). Define the *cumulative-net-gas* function $f$ measured starting from a hypothetical car at angle $0$: as we travel around the track, we accumulate $g_i$ each time we pass car $i$, and we consume gas at rate $1$ per unit angle (since the fuel-for-one-lap normalisation makes this convenient).

The extremal move: among all $n$ starting candidates, *choose the car at the angular position where the cumulative-net-gas $f$ takes its minimum value* — call this car $C^*$, at angle $\theta^*$. **Intermediate result $A'$ (driver): such a minimising car exists (since $\{f(\theta_i)\}$ is a finite set, the minimum is attained).**

*Stage 2 — applying #18 Induction (enabler).* We now want to show that starting from $C^*$ and going around the track once, the cumulative-net-gas remains non-negative throughout. The extremal choice of $\theta^*$ ensures this *for the journey starting at $\theta^*$*, because at every subsequent angular position the cumulative-net-gas is $f(\theta) - f(\theta^*) \geq 0$ by the minimum-defining property.

The induction lifts this single-starting-car observation into a complete proof for all $n$. **Base case** $n = 1$: a lone car has all the fuel and trivially completes a lap. **Inductive step**: assume the proposition holds for $n - 1$ cars. For $n$ cars, identify the extremal car $C^*$ as above. Locate any car $C_+$ immediately ahead of $C^*$ in the direction of travel; the gas at $C_+$ is at least enough for the segment from $C^*$ to $C_+$ (this follows from the extremal property — between $\theta^*$ and the next-car angle, $f$ is non-decreasing by at least the amount of the gas reached at the next car). Merge $C_+$ into the (just-passed) "current" car by adding their fuel sums and ignoring the now-empty $C_+$. This reduces the problem to $n - 1$ cars, and by induction such a starting car exists in the reduced configuration. **Intermediate result $B'$ (enabler): by induction the proposition holds for all $n$, with the extremal car of the original $n$-car problem being the answer.**

*Convergence.* The car $C^*$ identified by the extremal move can complete the lap. $\boxed{\text{Such a car exists.}}$

**Commentary — extremal as driver, induction as enabler.** This is a textbook example of how Extremal and Induction *cooperate* on a problem that neither could solve alone. Pure Extremal would identify the minimising car $C^*$ but, without an inductive framework, would have no clean way to argue *why* the minimisation is sufficient — one would have to carefully verify the cumulative-net-gas-non-negative claim for each of the $n - 1$ intermediate positions. Pure Induction would have no principled basis for *choosing* the right starting car in the inductive step — it would face an exponential branching over starting choices. The convergence is the realisation that *the extremal move gives induction the right car to merge*, reducing $n$ to $n - 1$ in a canonical way. The extremal principle drives (it tells us the structure), the induction enables (it lifts the structural insight into the full proof).

This problem is a Pillar 2 Ch. 12 (Extremal Principles) cross-reference and a Pillar 2 Ch. 18 (Recursion/Induction) cross-reference simultaneously — a sign of its 2-archetype character.

---

## §3 The Trap — The Wrong-Second-Archetype Trap

The lonely-archetype trap (Chapter 1 §3) was the failure mode of solvers who had not yet internalised the multidirectional thesis — they treated every problem as single-archetype because that is how Pillar 2 trained them. The Wrong-Second-Archetype Trap is the failure mode of solvers who *have* internalised the multidirectional thesis but are still calibrating their pair-selection. They know they need two archetypes; they correctly identify the first; they incorrectly identify the second.

The trap has a distinctive cognitive signature. The solver, having identified the first archetype quickly (say within thirty seconds), feels productive and *commits* to a second-archetype guess. The chosen second archetype produces some apparent progress — usually it generates an intermediate result that *looks* like it should converge with the first archetype's intermediate result. But the convergence does not close. Five minutes pass. Ten minutes. The solver tries to force the convergence by adjusting the first archetype's intermediate result (which is correct and need not be adjusted). Twenty minutes pass with no actual progress, only the appearance of progress.

**A worked illustration.** Consider the following problem:

> *Prove that for every positive integer $n$, the number $n^7 - n$ is divisible by 42.*

A solver who has read Engel's Number Theory chapter recognises the first archetype within seconds: **#14 Parity/Modularity** — divisibility-by-42 is naturally a modular-arithmetic question, and $42 = 2 \cdot 3 \cdot 7$ suggests checking divisibility by each prime factor separately.

The solver then commits to a second archetype. *Wrong choice*: **#5 Substitution** — try $n = 2k$ for even $n$ and $n = 2k+1$ for odd $n$, then expand $(2k)^7$ and $(2k+1)^7$ via the binomial theorem, then case-analyse mod 3 and mod 7. This produces enormous algebra: 16 terms in the binomial expansion, two cases per prime factor, six cases total. The solver, after 20 minutes, has covered three of the six cases with no error, has correctly verified that $n^7 - n \equiv 0 \pmod 2$ in both even-case and odd-case, and is now stuck in the messy mod-7 algebra for $n = 2k$.

*Right choice*: **#1 Invariance** via Fermat's Little Theorem. For any prime $p$, FLT states $n^p \equiv n \pmod p$, hence $n^p - n \equiv 0 \pmod p$ for all $n$. So $p = 2, 3, 7$ all individually divide $n^7 - n$ (well, $n^7 \equiv n \pmod 2$ from $n^2 \equiv n$; $n^7 = (n^3)^2 \cdot n \equiv n^2 \cdot n = n^3 \equiv n \pmod 3$; $n^7 \equiv n \pmod 7$ directly). Combined via the Chinese Remainder Theorem (or the basic fact that pairwise coprime divisors of a number divide its product), $\text{lcm}(2, 3, 7) = 42$ divides $n^7 - n$. Total proof length: three lines.

The trap was choosing #5 Substitution as the second archetype when the correct choice was #1 Invariance (in the specific form of Fermat's Little Theorem). The wrong second archetype was *plausible* — substitution into a polynomial does feel like a natural complement to a divisibility question. But the right second archetype reveals a structural invariant ($n^p \equiv n \pmod p$ for every prime $p$, an invariant of the residue-class) that closes the proof in one move.

**The diagnostic.** How does one tell, mid-solution, that the trap has been sprung? The signature is:
1. You have committed to a specific archetype pair.
2. Apparent progress (the first archetype's intermediate result is in hand).
3. The second archetype's intermediate result *almost-but-not-quite* combines with the first.
4. You have been at the almost-but-not-quite state for more than 10 minutes.

When all four are true, the recovery move is **Direction Map** (one of the three Escape-Hatch moves, developed in Chapter 7). The Direction Map is mechanically: redraw the 2-archetype convergence diagram on a fresh page; *label what each intermediate result should let you say*; check whether the labels actually compose into a proof. If the labels do not compose, the second archetype is wrong.

**The recovery for the $n^7 - n$ problem.** Redraw the diagram with the labels: *"#14 Parity/Mod gives: $n^7 - n \equiv 0 \pmod ?$. #5 Substitution gives: explicit expression for $(2k)^7 - 2k$ and $(2k+1)^7 - (2k+1)$ in terms of $k$."* Now ask: do these two labels combine? Answer: only if we can isolate divisibility by 42 from the explicit substitution expression — which requires further mod-2-3-7 analysis, *which is exactly the work the chosen substitution was trying to short-circuit*. The substitution is not actually helping; it is recreating the problem in a different variable. The Direction Map exposes this. The solver then asks: *"what archetype, paired with #14, would give an intermediate result that directly combines with $n^7 - n \equiv 0 \pmod p$?"* Answer: Invariance, specifically FLT — which gives $n^p \equiv n \pmod p$, directly yielding the needed congruence. Total recovery time: about three minutes.

The lesson: the Direction Map is a *protocol move*, not a desperation move. Run it after 10 minutes of "almost-but-not-quite" progress, even if you feel close. The earlier you Direction-Map, the less time you lose to the trap.

---

## §4 Practice Problems

Four problems, each clearly 2-archetype, with archetype labels in italics. The order grades roughly by subtlety of the driver/enabler distinction — Problem 2.1 has an obvious driver, Problem 2.4 requires care.

**Practice Problem 2.1.** *(Source: Engel Ch. 1 Problem 49 — sign-flipping. Archetypes: #1 Invariance (driver) + #14 Parity (enabler).)*

There are several $+$ signs and $-$ signs on a blackboard. The allowed move is to erase any two signs and replace them by a single sign: if the two erased signs were the same, the replacement is $+$; if different, the replacement is $-$. Show that the final sign (after $n - 1$ moves applied to $n$ original signs) depends only on the *parity of the number of $-$ signs originally on the board*.

*Hint.* What quantity, computed over the current set of signs, never changes under the move? (Use signs as $\pm 1$ values.)

**Practice Problem 2.2.** *(Source: Engel Ch. 3 E3 — points-in-the-plane area bound. Archetypes: #12 Extremal (driver) + #2 Symmetry (enabler).)*

A set of $n$ points in the plane has the property that every triangle formed by any three of these points has area at most $1$. Prove that *all $n$ points* lie inside some triangle of area at most $4$.

*Hint.* Among all $\binom{n}{3}$ triples of points, choose the one whose triangle $\triangle ABC$ has maximum area. Now construct a larger triangle $\triangle A_1 B_1 C_1$ by drawing lines through each vertex parallel to the opposite side. What is the area of $\triangle A_1 B_1 C_1$, and why are all $n$ points inside it?

**Practice Problem 2.3.** *(Source: Engel Ch. 4 E1 — same-degree pair. Archetypes: #13 Combinatorial (driver) + #12 Extremal (enabler).)*

In any room of $n$ persons (with $n \geq 2$), some two persons have the same number of acquaintances *within the room*. (Acquaintance is symmetric: if $A$ knows $B$, then $B$ knows $A$.)

*Hint.* Each person has an acquaintance-count in $\{0, 1, 2, \ldots, n-1\}$ — that is $n$ possible values for $n$ people, which is not yet enough for pigeonhole. But two of these values cannot both occur simultaneously. Which two?

**Practice Problem 2.4.** *(Source: Zeitz Ex 4.1.1 — modified for 2-archetype; full 3-archetype version is treated in Chapter 3 WE2. Archetypes: #8 Domain Translation (driver) + #13 Combinatorial (enabler).)*

Three mathematicians attended a lecture and each fell asleep exactly once during the lecture (possibly at different times). For each pair of the three mathematicians, there was some moment when both were sleeping simultaneously. Prove that, at some moment, all three were sleeping simultaneously.

*Hint.* Recast the time-intervals as intervals on the real line. Use a Helly-type argument or a direct interval-intersection observation: three intervals that pairwise intersect have a common point.

---

## §5 Bridge to Chapter 3

This chapter formalised the 2-archetype convergence as the *atom* of multidirectional solving and developed the driver-enabler distinction as its principal diagnostic move. We catalogued the eight most-frequent canonical archetype pairs (CCPs), worked through three of them in detail (Invariance + Parity, Symmetry + Domain Translation, Extremal + Induction), and named the Wrong-Second-Archetype Trap as the principal failure mode that distinguishes Pillar 3 solvers from solvers who have not yet calibrated their pair-selection instinct. We introduced the second of the three Escape-Hatch moves: the **Direction Map**.

Chapter 3 develops the **3-archetype problem class** — the molecule of multidirectional solving. We will treat **IMO 1988 Problem 6** (Vieta jumping) as the canonical worked example: it converges Induction, Reverse Engineering, and Invariance simultaneously, in one of the most famous and most-discussed olympiad proofs of the modern era. We will name the **forgotten-third-archetype trap**, which is to 3-archetype problems what the wrong-second-archetype trap is to 2-archetype problems. Because the 3-archetype class exceeds working-memory limits for unaided solvers (per §1.2's cognitive-hardware claim), Chapter 3 also begins to *motivate* the First-Minute Protocol of Chapter 4, by demonstrating that no human solver can hold three archetypes simultaneously in working memory without paper-and-pencil externalisation.

The bridge into Chapter 3 is the contrast: Anjali (this chapter's opening protagonist) succeeded at 32 of 38 two-archetype problems with the help of the convergence-diagram discipline. Of her 4 three-archetype problems, she solved only 1. The 3-archetype difficulty cliff is genuinely different in kind from the 2-archetype cliff, and a new tool — the First-Minute Protocol — is needed to scale it. Chapter 3 demonstrates the cliff; Chapter 4 builds the tool.

> *In Chapter 3: when two archetypes are not enough, and the cognitive cost of holding three.*

---

*End of Chapter 2.*
