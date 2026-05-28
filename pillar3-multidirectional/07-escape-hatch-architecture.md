---
chapter: 7
pillar: 3
title: "The Escape-Hatch Architecture"
subtitle: "*What to do when the discipline doesn't work.*"
length_target_words: 6000
canonical_takeaway: "The escape-hatch is not a desperation move; it is a protocol move. Trigger it on the clock, not on the feeling."
status: draft
last_revised: 2026-05-28
references_invoked: [Engel-ch-14, Zeitz-ch-2, Polya-1945]
canonical_constructs_used: [escape-hatch, first-minute-protocol, mvc-sketch, convergence-diagram]
---

# Chapter 7 — The Escape-Hatch Architecture

*What to do when the discipline doesn't work.*

---

## §0 Opening Vignette — Aditya Sharma's INMO recovery

It is 11:42 a.m. on a Sunday in January at the INMO examination centre at Delhi Technological University. Aditya Sharma, a second-year computer science student at IIT Delhi, is 102 minutes into the four-hour exam. He has solved problems 1, 2, 3 cleanly. He is now on problem 4. He has been on problem 4 for the last 47 minutes, and he is stuck.

The problem (slightly disguised from the actual INMO 2024 problem to protect the integrity of future re-use): *Find all positive integers $n$ such that some permutation of $1, 2, \ldots, n$ has the property that the absolute differences between consecutive terms are all distinct.*

Aditya ran the First-Minute Protocol at minute 55: Step 3 identified *#13 Combinatorial + #14 Parity*. He drew the MVC at minute 56. The MVC's convergence node has been "TBD" for 47 minutes. He has tried small cases ($n = 1, 2, 3, 4, 5, 6$ — answers exist for each), conjectured the answer set as *"all $n$"*, then tried to construct the required permutation for general $n$, then tried to derive an inductive construction, then tried to prove existence by counting. Nothing closes.

At minute 102 he is stuck *and* aware of being stuck. He has the next problem to attempt (problem 5) and the remaining time (138 minutes) to think about. The honest cost-benefit at this moment: continuing to grind on problem 4 has *negative expected value* — every minute he spends on it is a minute not spent on problem 5, and his last 47 minutes of grinding have yielded no progress. But abandoning problem 4 means losing the partial credit he has earned from his small-case verification and conjecture.

This is the moment for an **escape-hatch move**. The Pillar 3 architecture supplies three named moves: *Archetype Nudge* (when the suspicion is "wrong archetype"), *Direction Map* (when the suspicion is "right archetypes, wrong order/direction"), *Pivot Shadow* (when the suspicion is "the brute path I'm avoiding is actually half-correct"). Aditya, having internalised the architecture from his coaching last year, runs the diagnostic question: *which of the three moves matches my stall?*

His MVC's convergence node is "TBD" but his archetype nodes are filled in. He has not been switching archetypes; he has been *grinding* with the same archetype-pair (#13 + #14) for 47 minutes. The diagnostic says: this is an *Archetype Nudge* stall — the archetype-pair is probably wrong or incomplete. He runs the Nudge: writes on a fresh page two candidate archetypes he has not yet considered — *#16 Reverse Engineering* and *#15 Bijection*. He stares at #15 Bijection for about 30 seconds.

Then the insight strikes. The problem is essentially asking: *does a bijection exist between the set of $n - 1$ "consecutive-pair" positions and the set of $n - 1$ possible absolute differences $\{1, 2, \ldots, n - 1\}$?* The reformulation transforms a combinatorial-existence question into a bijection-existence question — a *#15 Bijection* problem. The bijection is a *graceful labelling* of a path graph — a well-studied combinatorial object with known existence conditions. Within 8 minutes Aditya has the proof sketched. Within 15 more minutes he has it written. By minute 125, he has moved on to problem 5.

The Archetype Nudge cost: 30 seconds of considering a candidate archetype he had not loaded into his MVC. The Archetype Nudge benefit: a closed solution to problem 4, plus the working memory and time-budget to attempt problem 5. The trade is heavily positive.

**This is the chapter that engineers recovery from stalled solutions.**

---

## §1 The Pattern

### §1.1 The three escape-hatch moves, catalogued

The Pillar 3 Escape-Hatch Architecture supplies three named recovery moves, each calibrated to a distinct *type* of stall. The three were introduced in earlier chapters (§3 of Chs. 1, 2, 3); this chapter develops each in full and gives the *decision tree* for choosing among them.

| Move | Diagnostic signal | Mechanical execution |
|---|---|---|
| **Archetype Nudge** | Stall ≥ 10 min; last 3 attempts all variants of the same archetype | Write two candidate archetypes you have *not* loaded into the MVC. Force one of them into the MVC's right-hand archetype box. Re-attempt. |
| **Direction Map** | Stall ≥ 10 min; "almost-but-not-quite" feeling; archetype-pair seems correct | Redraw the MVC fresh; *label what each archetype's intermediate result should let you say*; check whether the labels actually compose. If they don't, the archetype is wrong (revert to Archetype Nudge) or the *direction* (input/output of each archetype) is wrong (swap driver and enabler). |
| **Pivot Shadow** | Stall ≥ 10 min; brute path was explicitly rejected in Step 5 of the Protocol; *intuition says the brute path is half-correct* | Execute the brute path for 5 minutes, just enough to see *what structure emerges*. The structure is usually the elegant pivot in disguise — the brute path is the elegant path with the disguise still on. |

### §1.2 The decision tree

Faced with a stalled MVC at minute 10 or later, the Pillar 3 solver runs the following decision tree:

```
                  ┌─────────────────────────────────┐
                  │  Stall detected: ≥ 10 min,      │
                  │  MVC convergence node = "TBD"   │
                  └────────────────┬────────────────┘
                                   │
                                   ▼
                  ┌─────────────────────────────────┐
                  │  Q1: Have I been cycling through│
                  │  variants of the *same*         │
                  │  archetype for the entire stall?│
                  └───────┬─────────────────┬───────┘
                          │ Yes             │ No
                          ▼                 ▼
                  ┌──────────────────┐ ┌─────────────────────────────┐
                  │ ARCHETYPE NUDGE  │ │ Q2: Is the convergence      │
                  │ (load a fresh    │ │ node "almost-but-not-quite"?│
                  │ archetype)       │ └───────┬──────────────┬──────┘
                  └──────────────────┘         │ Yes          │ No
                                               ▼              ▼
                                     ┌─────────────────┐ ┌────────────────┐
                                     │ DIRECTION MAP   │ │ Q3: Did I      │
                                     │ (redraw and re- │ │ explicitly     │
                                     │ check labels)   │ │ reject a brute │
                                     └─────────────────┘ │ path in Step 5?│
                                                         └───┬────────┬───┘
                                                             │Yes     │No
                                                             ▼        ▼
                                                ┌─────────────────┐ ┌────────────────┐
                                                │ PIVOT SHADOW    │ │ Fall back to   │
                                                │ (execute brute  │ │ ARCHETYPE NUDGE│
                                                │ for 5 min)      │ │ (default move) │
                                                └─────────────────┘ └────────────────┘
```

The decision tree is shallow — three questions, four outcomes — and is meant to be runnable in under 30 seconds. The Pillar 3 solver, faced with a stall, runs the tree before deciding which move to execute. This prevents the failure mode of *picking the wrong escape-hatch move* and wasting another 10 minutes on a recovery that addresses the wrong stall type.

### §1.3 The clock-trigger discipline

The most important operational rule of the Escape-Hatch Architecture is: **trigger the recovery on the clock, not on the feeling.**

The natural human tendency, when stuck, is to *keep trying* — to grind through one more variant, to attempt one more substitution, to push the calculation one more step. The grinding feels productive (the solver is "doing something") but is usually negative-expected-value: if the standard discipline (Protocol + MVC) has failed for 10 minutes, the probability that one more variant of the same approach will succeed is low. The expected return of the 11th minute of grinding is below the expected return of an escape-hatch move.

The clock-trigger rule: **at the 10-minute mark of any stalled MVC convergence node, execute the decision tree of §1.2 mechanically, without consulting your feelings about whether the move is "ready."** The trigger is a number on the clock, not an intuition about readiness.

This rule is the operational analogue of the First-Minute Protocol's 60-second budget (Ch. 4 §1.1). The Protocol forces a delay *before* attempting; the Escape-Hatch forces a switch *during* attempting. Both fight the same enemy — *premature commitment to the default action* — by imposing time-based discipline.

---

## §2 Worked Examples

We develop one worked example per escape-hatch move, showing the failure-then-recovery trajectory in each case.

### Worked Example 7.1 — The Archetype Nudge in action

*Source.* INMO 2024 problem 4 (slightly disguised), as in §0 above. We replay Aditya's trajectory with explicit Protocol scratchpad, MVC, and Nudge.

**Problem.** Find all positive integers $n$ such that some permutation of $\{1, 2, \ldots, n\}$ has the property that the absolute differences between consecutive terms are all distinct.

**Initial Protocol scratchpad (minute 55, Aditya's actual scratchpad).**

```
+--------------------------------------------------------------+
| 1. Given: ∀ n permute {1..n}; check if |aᵢ − aᵢ₊₁| distinct │
| 2. Find: all n for which such a permutation exists           |
| 3. Archetypes: #13 (count permutations + valid difference sets)
|    + #14 (parity of differences; n−1 values, n−1 positions)  |
| 4. Candidate CEP: small-case verification; conjecture all n  |
| 5. Brute path: enumerate all n! permutations — infeasible    |
+--------------------------------------------------------------+
```

**Initial MVC (minute 56).**

```
       ┌──────────────────────────────────────────┐
       │ ∀ n: ∃ perm of {1..n} with distinct |Δ|s│
       └────────────────────┬─────────────────────┘
                            │
        ┌───────────────────┴───────────────────┐
        ▼                                       ▼
┌─────────────────────┐                ┌────────────────────────┐
│ #13 COMBINATORIAL   │                │ #14 PARITY/MODULARITY  │
│ ⚠ Need to count or  │                │ ⚠ n−1 differences from │
│ construct valid     │                │ {1..n−1}; parity con-  │
│ perms               │                │ straints?              │
│ stuck at n = 7      │                │ stuck                  │
└──────────┬──────────┘                └──────────┬─────────────┘
           │                                      │
           └─────────────────┬────────────────────┘
                             ▼
              ┌─────────────────────────────┐
              │ Conv: TBD (47 minutes)      │
              └─────────────────────────────┘
```

**Stall.** At minute 102, MVC convergence has been "TBD" for 47 minutes. Aditya's last 3 attempts have all been variants of "use mod-arithmetic to constrain the difference-set." This is the diagnostic signal for **Archetype Nudge** (Q1 of §1.2 decision tree: cycling on same archetype-pair).

**Nudge execution (minute 103).** Aditya writes on a fresh page:

```
+--------------------------------------------------------------+
| ARCHETYPE NUDGE — candidates I have NOT yet loaded:          |
|   - #15 Bijection                                            |
|   - #16 Reverse Engineering                                  |
|                                                              |
| Try #15: Does the problem have a bijection-of-sets shape?    |
|   - Set A = {(i, i+1) : i = 1..n−1} ⇒ n−1 consec. positions │
|   - Set B = {1, 2, ..., n−1} ⇒ n−1 possible |Δ| values       │
|   - Question becomes: ∃ a bijection f: A → B realisable as   │
|     |perm(i+1) − perm(i)| ?                                  │
|   - This IS a bijection problem — specifically, a "graceful  │
|     labelling" of the path graph P_n                         │
| Try #16: ... [Aditya stops here, #15 looks promising]        │
+--------------------------------------------------------------+
```

**Revised MVC (minute 104).**

```
       ┌──────────────────────────────────────────┐
       │ ∀ n: ∃ perm of {1..n} with distinct |Δ|s│
       └────────────────────┬─────────────────────┘
                            │
                            ▼
       ┌──────────────────────────────────────────┐
       │ #15 BIJECTION                            │
       │ ✓ Recast as: graceful labelling of P_n   │
       │ ✓ Graceful labelling of P_n known to     │
       │   exist for all n (classical result)     │
       └────────────────────┬─────────────────────┘
                            ▼
              ┌─────────────────────────────┐
              │ Conv: Answer = all n ≥ 1    │
              └─────────────────────────────┘
                            ▼
                    ┌──────────────────┐
                    │ ∀ n ≥ 1          │
                    └──────────────────┘
```

**Solution (minute 105 onward).** A *graceful labelling* of a graph $G$ on $m$ edges is an injection $V(G) \to \{0, 1, \ldots, m\}$ such that the induced edge-labels (absolute differences of vertex-labels at each edge) are exactly $\{1, 2, \ldots, m\}$. The path graph $P_n$ has $n$ vertices and $n - 1$ edges, so a graceful labelling uses vertex-labels in $\{0, 1, \ldots, n - 1\}$ with edge-labels $\{1, 2, \ldots, n - 1\}$. By a classical construction (Rosa, 1967), graceful labellings of $P_n$ exist for all $n \geq 1$; one construction: label vertices $0, n - 1, 1, n - 2, 2, n - 3, \ldots$ (alternating from the outside in). The resulting consecutive differences are $n - 1, n - 2, n - 3, \ldots, 1$ — all distinct.

Translating back: the graceful labelling with vertex set $\{0, 1, \ldots, n - 1\}$ becomes a permutation of $\{1, 2, \ldots, n\}$ by adding 1 to each label. The construction works for all $n \geq 1$. $\boxed{\text{All } n \geq 1.}$

**Commentary — the Nudge as a 30-second move.** Notice the time budget: the entire Nudge — from the moment Aditya recognised the stall to the moment he had the new archetype loaded — was about 30 seconds. The Nudge does not require the solver to *believe* the new archetype is correct; it only requires the solver to *consider* it. Consideration is cheap. In Aditya's case, 30 seconds of considering bijection produced an insight that the prior 47 minutes of grinding on combinatorics-and-parity had not. The Nudge's expected return on the 30-second investment is dramatic precisely when prior grinding has failed.

### Worked Example 7.2 — The Direction Map in action

*Source.* A composite illustration constructed for this chapter, drawing on the *wrong-second-archetype* trap pattern from Chapter 2 §3.

**Problem.** Prove that for every positive integer $n$, the number $n^7 - n$ is divisible by 42.

**Initial Protocol scratchpad (a deliberately-mis-diagnosed scratchpad to illustrate the Direction Map):**

```
+--------------------------------------------------------------+
| 1. Given: n ∈ ℤ₊                                              |
| 2. Find: 42 | n⁷ − n                                          |
| 3. Archetypes: #14 (mod-arith; 42 = 2·3·7) + #5 (substitute  │
|    n = 2k, n = 2k+1; expand via binomial)                    |
| 4. Candidate CEP: case-by-case mod-2-3-7 of polynomial       │
|    expansion                                                 │
| 5. Brute path: enumerate n = 1..42, check directly — works   │
|    but wasteful                                              │
+--------------------------------------------------------------+
```

**Initial MVC.**

```
┌────────────────────────────────────────┐
│ Prove 42 | n⁷ − n ∀ n ∈ ℤ₊            │
└──────────────────┬─────────────────────┘
                   │
       ┌───────────┴───────────┐
       ▼                       ▼
┌──────────────────┐ ┌──────────────────────┐
│ #14 PARITY/MOD   │ │ #5 SUBSTITUTION      │
│ ⚠ 42 = 2·3·7;    │ │ ⚠ n = 2k case: expand│
│ check each mod   │ │ (2k)⁷ via binomial   │
│ separately       │ │ stuck in mod-7 case  │
└────────┬─────────┘ └────────┬─────────────┘
         │                    │
         └─────────┬──────────┘
                   ▼
       ┌──────────────────────────┐
       │ Conv: TBD (20 min)       │
       └──────────────────────────┘
```

**Stall.** MVC convergence has been "TBD" for 20 minutes. The solver has *partial* progress (mod-2 and mod-3 verified for both odd-and-even-$n$ cases) but is stuck in the mod-7 algebra for $n = 2k$. The feeling is *almost-but-not-quite* — the proof has the right shape but the algebra is not closing. This is the diagnostic signal for **Direction Map** (Q2 of the decision tree: convergence node "almost-but-not-quite").

**Direction Map execution.** The solver redraws the MVC on a fresh page and *labels what each archetype's intermediate result should let them say*:

```
ARCHETYPE       INTERMEDIATE RESULT (label)
#14 Parity/Mod  Want: n⁷ − n ≡ 0 (mod 2), mod 3, mod 7 (each)
                Got: mod 2 ✓ and mod 3 ✓, mod 7 ⚠
#5 Substitution Want: an explicit expression for n⁷ − n in terms of k
                Got: (2k)⁷ − 2k = 128k⁷ − 2k = 2k(64k⁶ − 1)
                     (odd case symmetric, more algebra)
                Want this to imply 7 | n⁷ − n
```

**Composition check.** Does the *label-output* of #5 Substitution combine with the *label-input* of #14 Parity/Mod for the mod-7 case? Answer: **NO**. The substitution $n = 2k$ gives an explicit polynomial in $k$, but the *task* under mod-7 is to verify the polynomial is $\equiv 0 \pmod 7$ for all integer $k$ — and *that task is itself an instance of the original problem* (with $n^7 - n$ replaced by $128k^7 - 2k$, which has the same shape). The substitution has *not advanced* the problem; it has just re-stated it in different variables.

**Diagnosis.** The wrong second archetype was *#5 Substitution*. The Direction Map has surfaced this. The correct second archetype is **#1 Invariance** — specifically, *Fermat's Little Theorem*, which states $n^p \equiv n \pmod p$ for any prime $p$. With $p = 2, 3, 7$ each individually, $n^p \equiv n \pmod p$. For $p = 7$: $n^7 \equiv n \pmod 7$, so $7 \mid n^7 - n$ directly. For $p = 2$: $n^2 \equiv n \pmod 2$, so $n^7 = (n^2)^3 \cdot n \equiv n^3 \cdot n = n^4 \equiv n^2 \cdot n^2 \equiv n \cdot n \equiv n \pmod 2$. (Or just: $n^7$ and $n$ have the same parity.) For $p = 3$: $n^3 \equiv n \pmod 3$, so $n^7 = n^3 \cdot n^3 \cdot n \equiv n \cdot n \cdot n = n^3 \equiv n \pmod 3$. All three congruences give $n^7 - n \equiv 0 \pmod{p}$ for $p = 2, 3, 7$. By the Chinese Remainder Theorem (or directly: pairwise-coprime divisors of a number imply the product divides), $42 = 2 \cdot 3 \cdot 7$ divides $n^7 - n$. $\boxed{42 \mid n^7 - n.}$

**Revised MVC.**

```
┌────────────────────────────────────────┐
│ Prove 42 | n⁷ − n ∀ n ∈ ℤ₊            │
└──────────────────┬─────────────────────┘
                   │
       ┌───────────┴───────────┐
       ▼                       ▼
┌──────────────────┐ ┌──────────────────────┐
│ #14 PARITY/MOD   │ │ #1 INVARIANCE (FLT)  │
│ ✓ 42 = 2·3·7,    │ │ ✓ n^p ≡ n (mod p)    │
│ check each       │ │ for p = 2,3,7        │
│ separately       │ │                      │
└────────┬─────────┘ └────────┬─────────────┘
         │                    │
         └─────────┬──────────┘
                   ▼
       ┌──────────────────────────┐
       │ Conv: 42 | n⁷ − n        │
       └──────────────────────────┘
```

**Recovery time: ~5 minutes** (the Direction Map itself: 2 minutes; the FLT-based proof: 3 minutes). Total wall-clock from initial stall: 25 minutes (vs. potentially indefinite if the solver had continued grinding on the substitution path).

**Commentary — the Direction Map as a label-check.** The mechanical core of the Direction Map is the *label-composition check*: write what each archetype's output is, write what each archetype's input requires, check if the outputs feed the inputs. If they do, the archetypes are correctly composed and the stall is elsewhere (perhaps in the algebra). If they don't, an archetype is wrong (or the direction of one is wrong, e.g., driver and enabler swapped). The Direction Map is functionally a *type-check* on the proof's architectural composition — a debugging tool borrowed from software engineering and adapted to mathematical proof.

### Worked Example 7.3 — The Pivot Shadow in action

*Source.* Engel, *Problem-Solving Strategies*, Ch. 14 §14.2 (Infinite Descent) — the anchor chapter for Pillar 3 Ch. 7 per Blueprint sourcing note. The example here is a Diophantine descent variant where the brute path turns out to be the elegant path in disguise.

**Problem.** Find all integer solutions $(x, y)$ to the equation $x^3 = y^2 + 2$.

**Initial Protocol scratchpad:**

```
+--------------------------------------------------------------+
| 1. Given: x, y ∈ ℤ; x³ = y² + 2                              │
| 2. Find: all (x, y)                                          │
| 3. Archetypes: #14 (mod-arith) + #11 (existence + small case │
|    enumeration)                                              │
| 4. Candidate CEP: small-case verification → x = 3, y = ±5 is │
|    a solution; conjecture this is the only one (Mordell's)   │
| 5. Brute path: factor x³ − 2 = y² in some algebraic number   │
|    ring — e.g., ℤ[√−2] (avoid: classical but heavy)         │
+--------------------------------------------------------------+
```

**Initial MVC:**

```
┌──────────────────────────────────────┐
│ Find all (x,y) ∈ ℤ² with x³ = y² + 2│
└─────────────────┬────────────────────┘
                  │
       ┌──────────┴──────────┐
       ▼                     ▼
┌──────────────────┐ ┌────────────────────┐
│ #14 PARITY/MOD   │ │ #11 EXISTENCE      │
│ ⚠ mod 4: x³ mod 4│ │ ⚠ small (x,y):     │
│ vs y²+2 mod 4    │ │ x=3, y=±5 found;   │
│ — partial        │ │ no others up to    │
│ constraint only  │ │ x = 100; stuck     │
└────────┬─────────┘ └────────┬───────────┘
         │                    │
         └─────────┬──────────┘
                   ▼
       ┌──────────────────────────┐
       │ Conv: TBD (15 min)       │
       └──────────────────────────┘
```

**Stall.** MVC convergence has been "TBD" for 15 minutes. The solver has small-case verified $x = 3, y = \pm 5$, has tried mod-4 and mod-8 case analysis (yielding partial constraints but not full impossibility for other $x$), and is stuck. The brute path *was explicitly rejected* in Step 5 of the Protocol — namely, factoring in $\mathbb{Z}[\sqrt{-2}]$. This is the diagnostic signal for **Pivot Shadow** (Q3 of the decision tree: brute path explicitly rejected, intuition that it might be half-correct).

**Pivot Shadow execution.** Spend 5 minutes executing the brute path *just enough* to see what structure emerges.

Step 1: $x^3 = y^2 + 2$, so $x^3 = (y + \sqrt{-2})(y - \sqrt{-2})$ in $\mathbb{Z}[\sqrt{-2}]$.

Step 2: $\mathbb{Z}[\sqrt{-2}]$ is a Euclidean domain (a classical fact — the norm is $N(a + b\sqrt{-2}) = a^2 + 2b^2$). So unique factorisation holds.

Step 3: The two factors $y + \sqrt{-2}$ and $y - \sqrt{-2}$ have $\gcd$ dividing $(y + \sqrt{-2}) - (y - \sqrt{-2}) = 2\sqrt{-2}$. The norm of $2\sqrt{-2}$ is $8$. So $\gcd$ divides an element of norm 8; possibilities are units, $\sqrt{-2}$, $2$, $2\sqrt{-2}$.

Step 4: If $\sqrt{-2}$ divides $y + \sqrt{-2}$, then $\sqrt{-2}$ divides $y$ (since $\sqrt{-2}$ divides $\sqrt{-2}$ trivially), so $-2 \mid y^2$, so $y$ is even. But then $y^2 + 2 \equiv 2 \pmod 4$, so $x^3 \equiv 2 \pmod 4$, so $x$ is even, so $x^3 \equiv 0 \pmod 8$, but $y^2 + 2 \equiv 2 \pmod 4$ — contradiction. So $\gcd(y + \sqrt{-2}, y - \sqrt{-2})$ is a unit. 

Step 5: With coprime factors and a cube on the left, each factor must be (a unit times) a cube. The units of $\mathbb{Z}[\sqrt{-2}]$ are $\pm 1$. So $y + \sqrt{-2} = \pm (a + b\sqrt{-2})^3$ for some integers $a, b$.

Step 6: Expand $(a + b\sqrt{-2})^3 = a^3 + 3 a^2 b \sqrt{-2} + 3 a (b \sqrt{-2})^2 + (b \sqrt{-2})^3 = a^3 - 6ab^2 + (3a^2 b - 2 b^3) \sqrt{-2} = (a^3 - 6 a b^2) + (3 a^2 b - 2 b^3) \sqrt{-2}$.

Step 7: Matching real and imaginary parts: $y = \pm (a^3 - 6 a b^2)$ and $1 = \pm (3 a^2 b - 2 b^3) = \pm b (3 a^2 - 2 b^2)$.

Step 8: $b (3a^2 - 2b^2) = \pm 1$ forces $b = \pm 1$. If $b = 1$: $3 a^2 - 2 = \pm 1$, so $3 a^2 = 1$ or $3 a^2 = 3$, i.e., $a^2 = 1/3$ (no integer) or $a^2 = 1$ giving $a = \pm 1$. If $b = -1$: $-(3a^2 - 2) = \pm 1$, so $3a^2 - 2 = \pm 1$, same constraint, $a = \pm 1$.

Step 9: Plug back into $y = \pm(a^3 - 6ab^2)$ with $(a, b) = (\pm 1, \pm 1)$: $y = \pm(\pm 1 - 6 \cdot \pm 1) = \pm(\pm 1 \mp 6)$. Compute: $a = 1, b = 1$: $y = \pm(1 - 6) = \pm(-5) = \mp 5$, so $y = \pm 5$. With $y = \pm 5$, $y^2 = 25$, $x^3 = 27$, $x = 3$. (Other sign choices give the same $(x, y) = (3, \pm 5)$.)

**Conclusion (the brute path WAS the elegant path).** The unique-factorisation-in-$\mathbb{Z}[\sqrt{-2}]$ approach yields the complete answer: $\boxed{(x, y) = (3, \pm 5).}$

The "brute path" that the solver had explicitly avoided turned out to *be* the proof. The intuition that motivated the Pivot Shadow ("the brute path might be half-correct") was vindicated: it was, in fact, fully correct.

**Recovery time: ~12 minutes** (the Pivot Shadow execution: 5 minutes; the remaining algebra: 7 minutes). Total wall-clock from initial stall: 27 minutes.

**Commentary — when the brute path is the elegant path.** The Pivot Shadow's most-counterintuitive lesson is that *the brute path is sometimes literally the elegant path, just in unfamiliar dress*. The reason a solver rejects the brute path in Step 5 of the Protocol is usually *"it looks heavy / unfamiliar / requires machinery"* — but heavy/unfamiliar/machine-requiring is not the same as *wrong* or *infeasible*. The Pivot Shadow's 5-minute exploration is calibrated to reveal exactly this distinction: if the brute path is genuinely infeasible, 5 minutes will show it (the algebra explodes); if it is the elegant path in disguise, 5 minutes will show *that* too (the structure emerges by Step 4 or 5). The investment is bounded; the payoff is open.

---

## §3 The Trap — The chronic-escape-hatch trap

The principal failure mode of the Escape-Hatch Architecture is *over-use* — the **chronic-escape-hatch trap**. The chronic-escape-hatch solver triggers the recovery moves too often, too early, or for stalls that are *not actually stalls* (a 5-minute productive struggle is not the same as a 10-minute unproductive grind). The result is that the solver never gives any single approach enough time to mature, switches archetypes constantly, and ends up with multiple half-finished proof attempts rather than one closed proof.

The signature of the trap: every 3–5 minutes, the solver triggers an escape-hatch move; the MVC accumulates so many revised archetype-boxes that the structure is lost; the solver spends more time *deciding what to try next* than *actually trying anything*. The chronic-escape-hatch solver is the inverse of the lonely-archetype solver (Ch. 1 §3) — too much switching, not enough commitment — and the cure is the *opposite* discipline: enforce minimum dwell-time on each archetype before allowing a switch.

**The recovery from the trap: the 10-minute floor.** The clock-trigger rule of §1.3 establishes a *ceiling* on grinding (10 minutes maximum before mandatory escape-hatch evaluation). The cure for chronic-escape-hatch is to add a complementary *floor*: do not trigger any escape-hatch move within the first 10 minutes of any archetype attempt. The 10-minute floor gives each archetype enough time to *show what it can produce*; the 10-minute ceiling ensures the solver doesn't grind past the productive window. Together they bracket the healthy zone for archetype work: 10 minutes minimum, 10 minutes maximum, then evaluation.

(For very hard problems, the 10-minute ceiling may extend to 20 minutes — IMO problems sometimes need 20 minutes of pure thought before a productive direction emerges. But the floor stays at 10 minutes regardless. The asymmetry is intentional: under-grinding is the more dangerous failure mode for the chronic-escape-hatch solver.)

---

## §4 Practice Problems

Four problems designed to *trigger* one or more of the escape-hatch moves. For each problem, the reader is asked to attempt the standard Protocol-and-MVC discipline first; when (not if) it stalls, identify which escape-hatch move the decision tree of §1.2 recommends, execute it, and report the recovery time.

**Practice Problem 7.1.** *(Expected stall: Archetype Nudge.)* Determine all positive integers $n$ for which the sum $1 + 2 + 3 + \cdots + n$ is a perfect square. *Hint after stall: consider archetype #16 Reverse Engineering — work backwards from "$1 + 2 + \cdots + n = k^2$" to derive a Pell-equation-style identity.*

**Practice Problem 7.2.** *(Expected stall: Direction Map.)* Let $a, b, c$ be positive reals with $abc = 1$. Prove that $\frac{a}{b + 1} + \frac{b}{c + 1} + \frac{c}{a + 1} \geq \frac{3}{2}$. *Hint after stall: the standard archetype-pair (#5 Substitution + #12 Extremal) is correct, but the *direction* (which substitution to make first) is non-obvious; redraw the MVC and trace what each substitution's output should let you say.*

**Practice Problem 7.3.** *(Expected stall: Pivot Shadow.)* Show that the equation $x^2 + y^2 + z^2 = x y z$ has infinitely many positive-integer solutions. *Hint after stall: the brute path is "treat the equation as a quadratic in $z$ and run a Vieta-jump construction"; explicitly executing this for 5 minutes reveals the structure.*

**Practice Problem 7.4.** *(Expected stall: free choice — any of the three.)* Find all pairs of positive integers $(m, n)$ such that $(2^m + 1) | (2^n + 1)$. *Self-diagnostic: which escape-hatch move did your decision tree recommend? Did the recommendation produce a successful recovery? If not, which move did you fall back to?*

---

## §5 Bridge to Chapter 8

This chapter developed the three Escape-Hatch moves — Archetype Nudge, Direction Map, Pivot Shadow — and their decision tree. We anchored the clock-trigger discipline (10-minute ceiling, 10-minute floor) and named the chronic-escape-hatch trap as the over-correction failure mode. The three worked examples (Aditya's INMO recovery via Nudge; the $n^7 - n$ Direction-Map debug; the Diophantine $x^3 = y^2 + 2$ Pivot-Shadow into $\mathbb{Z}[\sqrt{-2}]$) illustrated each move in failure-then-recovery form.

Chapter 8 is the **Practice Set + Diagnostic** — the pillar's closing assessment instrument. It presents 10 problems graded from 2-archetype-easy to 3-archetype-hard, with a self-scoring rubric that lets the reader measure their internalisation of the full Pillar 3 discipline (Protocol fluency + MVC structuring + Escape-Hatch reflex + cross-archetype reach). The 10 problems are calibrated so that a reader who has internalised Chapters 1–7 should be able to solve at least 7 cleanly; a reader who has merely *read* Chapters 1–7 without practice should expect to solve 3–4.

The bridge into Chapter 8 is honest: Chapter 7 closed the *toolkit* — every cognitive move of Pillar 3 has now been named, developed, and illustrated. Chapter 8 closes the *training arc* — the practice instrument that converts knowledge of the toolkit into reflex with the toolkit. Without Chapter 8's deliberate practice, the toolkit remains inert; with it, the toolkit becomes the Pillar 3 solver's working memory.

> *In Chapter 8: the diagnostic that tells you whether the toolkit has become reflex.*

---

*End of Chapter 7.*
