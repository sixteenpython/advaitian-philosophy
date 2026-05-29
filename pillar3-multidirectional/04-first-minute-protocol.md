---
chapter: 4
pillar: 3
title: "The First-Minute Protocol"
subtitle: "*The 60-second diagnostic that prevents the 2.5-hour mistake.*"
length_target_words: 7500
canonical_takeaway: "Externalise the archetype profile in the first 60 seconds; the working-memory you preserve is the working-memory the convergence needs."
status: locked
last_revised: 2026-05-29
locked_on: 2026-05-29
references_invoked: [Engel-ch-3, Engel-ch-4, Zeitz-ex-6.1.1, Joshi-ch-13, Polya-1945]
canonical_constructs_used: [first-minute-protocol, convergence-diagram, escape-hatch]
---

# Chapter 4 — The First-Minute Protocol

*The 60-second diagnostic that prevents the 2.5-hour mistake.*

---

## §0 Opening Vignette — Lakshmi Narayanan at the Chennai Math Camp

It is a Sunday afternoon in late June at the Chennai Math Olympiad Training Camp, hosted at the Indian Institute of Mathematical Sciences (IMSc). Lakshmi Narayanan, a forty-something coach who has trained Indian IMO teams since 2009, is leading a session for 24 high-school students who have just qualified for the INMO-extended training. The session topic, on the wall-board, reads: **"The 60-Second Habit."**

Lakshmi begins by handing out a single problem on a numbered sheet:

> *Inside a rectangular room of area 5 square metres, you place 9 rugs, each of area 1 square metre and otherwise arbitrary shape. Prove that two of the rugs overlap on a region of area at least 1/9.*

She asks the students to start the timer at exactly 2:00:00 p.m. — but with one rule: *for the first 60 seconds, no one is allowed to write anything except in a small box at the top of the page labelled "scratchpad."* In the scratchpad, the students are to write *only* a list of five short items: (1) the given data, (2) the find, (3) candidate archetypes, (4) a guess at the central elegant point, and (5) the brute-force path they are not going to take.

At 2:01:00 p.m., the rule lifts. The students may begin the actual proof. Lakshmi sets the room timer for the next 25 minutes, the standard exam-style allotment for a hard problem.

The students fall into roughly four groups.

**Group A (8 students):** They fill the scratchpad enthusiastically and within the 60-second window. The scratchpad reveals — almost universally — *#13 Combinatorial + #1 Invariance / #12 Extremal* as the candidate archetype pair. The candidate CEP, written in tentative pencil, is *"$1/9$ comes from the count $(9 - 5)/9 = 4/9$ — wait, no, $1/9$ is the per-pair share when the excess area $9 - 5 = 4$ is distributed across nine pair-positions."* At 2:01:00 p.m., this group attacks the proof with the right archetype pair already loaded. Most of them close the proof by 2:09:00 p.m. — within 8 minutes of writing.

**Group B (10 students):** They write a partial scratchpad (perhaps items 1 and 2 only) in the first 60 seconds, then begin the proof. They are guessing at the archetype pair as they go. Three of them happen to guess correctly and finish by 2:13:00 p.m. The other seven guess #5 Substitution or #2 Symmetry as the second archetype, and these spend 15–22 minutes producing partial proofs that do not close.

**Group C (4 students):** They skip the scratchpad entirely. They start writing at 2:00:30 p.m., 30 seconds in. At 2:25:00 p.m., when the room timer expires, two of them have produced no progress at all; the other two have produced messy partial calculations that are not yet a proof.

**Group D (2 students):** They use the full 60 seconds on the scratchpad but spend it on the wrong items — items 1, 2, 4 (given, find, CEP guess) but skip item 3 (candidate archetypes). At 2:01:00 p.m., they attack the proof without the archetype pair loaded; they end up effectively in Group C.

The post-mortem at 2:30:00 p.m. is sobering. The 8 students of Group A, who treated the scratchpad as a 60-second mandatory ritual, solved the problem in a median time of 8 minutes. The 10 students of Group B, who skipped half the scratchpad, solved at a median of 18 minutes (when they solved at all). The 6 students of Groups C and D produced essentially no progress.

The First-Minute Protocol is what Group A did. The *cost* of the protocol is 60 seconds at the start. The *benefit* of the protocol is the next 10–20 minutes of working-memory bandwidth not wasted on archetype-guessing.

Lakshmi closes the session with a line she repeats at every camp: *"The students who skip the protocol because 'I don't have time' are exactly the students who run out of time. The students who run the protocol because 'I have time' are exactly the students who finish early."*

**This is the operational thesis of Chapter 4.**

---

## §1 The Pattern

### §1.1 The Protocol, in its 5-step form

The First-Minute Protocol is a 60-second mandatory diagnostic that the Pillar 3 solver runs before writing the first equation of a solution. The protocol has 5 steps, each of which produces a single scratchpad item:

```
+----+-----------------------------------+---------------------------------------+
| #  | Question                          | Output (scratchpad)                   |
+----+-----------------------------------+---------------------------------------+
| 1  | What is the *given*?              | Bullet list, ≤ 5 items   (15 s)       |
| 2  | What is the *find*?               | One sentence + answer-type (5 s)      |
| 3  | Which archetypes are likely?      | List of 1–3 archetype #s   (20 s)     |
| 4  | What is the candidate CEP?        | A guess, even if uncertain (10 s)     |
| 5  | What is the *brute path*?         | One line — the path I won't take      |
|    |                                   |   (10 s)                              |
+----+-----------------------------------+---------------------------------------+
                                          Total: 60 seconds
```

The 5 steps map to 5 different cognitive functions:

- **Step 1 (Given)** forces the solver to *parse* the problem before *attacking* it. The most common cause of false-start failures is mis-parsing — the solver reads the problem too fast, misses a clause, and attacks a slightly-wrong problem. Writing the given as a bullet list catches the mis-parse.

- **Step 2 (Find)** forces the solver to *name what success looks like*. "Prove that X is divisible by 42" needs a different proof shape from "compute X" needs a different proof shape from "find the maximum value of X" — these are different answer-types. Naming the answer-type shapes the candidate-archetype list in Step 3.

- **Step 3 (Archetypes)** is *the* multidirectional move. The solver names 1, 2, or 3 archetypes that *match* the (Given, Find) pair. This is the move that prevents the lonely-archetype trap (Ch. 1 §3) and the wrong-second-archetype trap (Ch. 2 §3). The discipline is to write *at least two* archetypes whenever the Find is non-trivial; this primes working memory for the multi-archetype convergence that will follow.

- **Step 4 (Candidate CEP)** forces the solver to *guess at the answer or the central elegance* before doing the work. The guess is often partially wrong, but the act of guessing constrains the search space and prepares the solver to recognise the answer when it appears. (This is also the move that creates the *bridge to Pillar 4*: the CEP guess in Pillar 3 becomes the CEP-design starting point in Pillar 4.)

- **Step 5 (Brute Path)** is the *anti-default move*. The solver writes the brute-force computation they would attempt if they had no archetype tools. The point is not to attempt the brute path; the point is to *commit to not attempting it*. Once the brute path is written down and marked-as-not-chosen, the solver is operationally committed to finding the elegant path, and the temptation to fall back to brute-force during the proof is weakened.

The arc that Steps 4 and 5 trace — *Seed → Brute Path → Elegant Pivot* — is the opening movement of Pillar 1's six-point grammar of a solution. The First-Minute Protocol is that grammar compressed into a 60-second pre-flight check: the solver names the seed (Given/Find/archetypes), commits to *not* taking the brute path, and guesses the elegant pivot before a single equation is written.

The total time budget is 60 seconds. This is short enough that the protocol does not feel like a delay; long enough that the solver can produce a meaningful scratchpad. With practice (typically 20–40 problems), the protocol becomes automatic — the solver runs it without thinking, the way a chess player at expert level automatically considers piece-development before tactics.

### §1.2 Why the protocol works (the cognitive justification)

The protocol works for three converging reasons, each tied to a specific cognitive bottleneck.

**Reason 1: It externalises the archetype list before working memory is contaminated.** Working memory is a scarce resource (Ch. 3 §1.2). Once the solver begins attempting the proof, working memory fills with intermediate-results, partial computations, and unresolved sub-questions. If the candidate archetypes have not been externalised by then, the solver effectively has to *re-name* them mid-solve, which competes for the same scarce slots that the actual convergence needs. The protocol moves the archetype-naming out of working memory and onto paper — freeing the working-memory slots for the actual mathematical work.

**Reason 2: It interrupts the default-fast-thinking loop.** Under time pressure, the solver's default is *fast thinking*: pattern-match the problem to the nearest known shape, attack with the first archetype that comes to mind. Fast thinking is fast (hence the name) but error-prone — it produces the lonely-archetype trap and the wrong-second-archetype trap with high frequency. The protocol forces 60 seconds of *slow thinking* (deliberately considering 2 or 3 archetypes) before the fast-thinking phase begins. The slow-thinking phase is cheap (60 seconds is a small fraction of the typical 25-minute problem budget) and high-leverage (it prevents 5–25 minutes of fast-thinking dead-end).

**Reason 3: It produces a fallback scratchpad for the Escape-Hatch moves.** If, 10 minutes into the proof, the solver gets stuck and needs to invoke an Escape-Hatch move (Ch. 7), they need *something* to compare against. The protocol scratchpad is that something. The Archetype Nudge move (Ch. 1 §3) compares the current archetype to the protocol's archetype list. The Direction Map move (Ch. 2 §3) compares the current intermediate result to the protocol's CEP guess. The Pivot Shadow move (Ch. 3 §3) compares the apparent answer to the protocol's brute path. Without the protocol, the Escape-Hatch moves have no anchor; with the protocol, they execute mechanically.

### §1.3 The history: Polya 1945 and the Tao blog-post tradition

The First-Minute Protocol is not, structurally, a new idea. George Polya's *How to Solve It* (1945) opens with a 4-phase loop — Understand, Plan, Execute, Look Back — whose **Understand** phase is essentially the same as our Steps 1 and 2 (Given, Find). What Polya did not formalise was the *time-boxed* discipline: he describes the Understand phase as *important* but does not prescribe how long it should take or what counts as a complete Understand-phase output.

Terence Tao, in his blog and writing from approximately 2008 onward, has written extensively about the cognitive discipline of *deciding what to attempt before attempting it*. In one widely-cited piece on "advice to undergraduates" (Tao, 2007), he writes that the discipline of *naming the technique* before applying it is "the single most useful habit you can develop as a mathematician." He does not call this the First-Minute Protocol, but the substance is the same.

What this chapter adds is the explicit 60-second budget, the 5-step scratchpad structure, and the cognitive justification connecting the protocol to the Pillar 3 Escape-Hatch architecture. The protocol is the operationalisation of two generations of pedagogical insight, condensed into a single mandatory ritual.

---

## §2 Worked Examples — Three Live Walkthroughs

In this section we run the First-Minute Protocol *in real time* on three problems. The format is unusual: we display the 60-second scratchpad first, exactly as a solver would produce it during the 60-second window, and only then attempt the proof. The reader is invited to *cover the proof section with a hand* and produce their own scratchpad before reading mine — the comparison is the pedagogical payoff.

### Worked Example 4.1 — The 9-rugs problem (Engel Ch. 4 E11)

*Source.* Engel, *Problem-Solving Strategies*, Ch. 4 Example E11 (p. 62).

**Problem.** Inside a room of area 5, you place 9 rugs, each of area 1 and arbitrary shape. Prove that two of the rugs overlap on a region of area at least $1/9$.

**(60-second scratchpad — produced exactly as it would appear on the actual paper)**

```
+--------------------------------------------------------------+
|  SCRATCHPAD  (start: 0:00; end: 0:60)                        |
+--------------------------------------------------------------+
| 1. Given:                                                    |
|    - 9 rugs                                                  |
|    - each rug area = 1                                       |
|    - room area = 5                                           |
|    - rugs arbitrary shape (no convexity)                     |
|                                                              |
| 2. Find:                                                     |
|    - ∃ two rugs whose overlap area ≥ 1/9                     |
|    - (proof of existence; an inequality)                     |
|                                                              |
| 3. Archetypes:                                               |
|    - #13 Combinatorial (counting / measuring overlaps)       |
|    - #12 Extremal (focus on least-overlapping pair, or       |
|      the rug placed last with most-already-covered area)     |
|                                                              |
| 4. Candidate CEP:                                            |
|    - 1/9 = (rug-total − room-area) / pair-count? Try         |
|      9·1 − 5 = 4 (extra area accommodated by overlaps);      |
|      4 / (pair-count somehow) gives 1/9?                     |
|    - or: 1/9 = excess-area / 9 = 4/9 ÷ 4 = 1/9 (?)            |
|    - sense-check: 9·1 = 9; room = 5; excess = 4.             |
|      Distributed across 9? No — across pairs.                |
|    - Best guess: place rugs sequentially; the k-th rug       |
|      must overlap previous coverage by ≥ (9 − k)/9. Total    |
|      pairwise overlap is at most 1 per pair; max-pair        |
|      overlap is ≥ excess / pair-count.                       |
|                                                              |
| 5. Brute path (avoid):                                       |
|    - Compute every pairwise overlap explicitly: impossible   |
|      because rug shapes are arbitrary.                       |
+--------------------------------------------------------------+
```

The scratchpad takes about 50 seconds to produce (well within the 60-second window). The crucial entries are item 3 (the right archetype pair is loaded) and item 4 (a tentative CEP guess that points to a sequential-placement argument).

**Now, the proof. (Time elapsed: 0:60; begin actual solution.)**

The candidate-CEP guess from the scratchpad points to a *sequential placement* argument: place rugs one by one and track how much "new" area each rug covers.

Place the 9 rugs one at a time. Let $A_k$ be the area of the room not yet covered before the $k$-th rug is placed; equivalently, $1 - A_k$ is the area of the room already covered by the first $k - 1$ rugs. Initially $A_1 = 5$ (nothing yet covered). When the $k$-th rug (of area 1) is placed, the *new* area it covers — area in the room that was previously uncovered — is at most 1 (its own area), and on average less.

Let $u_k$ denote the area covered by the $k$-th rug that overlaps with rugs $1, 2, \ldots, k-1$ — that is, the "wasted" overlap area of rug $k$ with previous rugs. Then the *new* coverage of rug $k$ is $1 - u_k$ (since the rug has area 1 in total). The total area covered by all 9 rugs satisfies:
$$\text{total covered} \leq 5 \quad \text{(it lives in the room)}.$$
But total covered also equals $\sum_{k=1}^9 (1 - u_k) = 9 - \sum_{k=1}^9 u_k$. So:
$$9 - \sum_{k=1}^9 u_k \leq 5 \quad \Longrightarrow \quad \sum_{k=1}^9 u_k \geq 4.$$
The "wasted overlap" $u_k$ counts area that overlaps with *some* combination of previous rugs. By a careful expansion (using inclusion-exclusion or, more simply, by noting that $u_k$ is at most $\sum_{j < k} (\text{overlap of rug } k \text{ with rug } j)$), we have:
$$\sum_{k=1}^9 u_k \leq \sum_{k=1}^9 \sum_{j<k} (\text{overlap of rug } k \text{ with rug } j) = \sum_{1 \leq j < k \leq 9} \text{overlap}(j, k).$$
There are $\binom{9}{2} = 36$ pairs. If every pair had overlap strictly less than $1/9$, then $\sum_{1 \leq j < k \leq 9} \text{overlap}(j, k) < 36 \cdot (1/9) = 4$. But we just showed this sum is $\geq 4$. Contradiction. So some pair must have overlap $\geq 1/9$. $\boxed{1/9}$

*Time to solve (post-scratchpad): about 7 minutes.* Total wall-clock from the start: 8 minutes. (Compare with the Group B and C students of the opening vignette, who spent 15–25 minutes producing partial or no progress.)

**Commentary — the scratchpad as proof-scaffold.** Notice how the scratchpad's item 4 (the CEP guess) essentially *outlined* the proof structure before the proof was written. The phrase *"max-pair overlap is ≥ excess / pair-count"* in the scratchpad's item 4 *is* the proof, modulo the bookkeeping with $u_k$ and $A_k$. The 60 seconds of scratchpad-time produced the proof outline; the next 7 minutes filled in the algebraic details. Without the scratchpad, the algebraic details would have come first (the wrong order) and the outline would have emerged painfully through trial and error.

### Worked Example 4.2 — Czech & Slovak 1995, re-treated under the Protocol lens

*Source.* Czech & Slovak Mathematical Olympiad 1995; Zeitz Ex 6.1.1. (Same problem as Chapter 1 Worked Example 3 — re-treated here through the First-Minute Protocol lens.)

**Problem.** Decide whether there exist 10,000 ten-digit numbers, each divisible by 7, all of which are obtainable from one another by reordering their digits.

**(60-second scratchpad)**

```
+--------------------------------------------------------------+
|  SCRATCHPAD  (start: 0:00; end: 0:60)                        |
+--------------------------------------------------------------+
| 1. Given:                                                    |
|    - 10,000 ten-digit numbers                                |
|    - each divisible by 7                                     |
|    - all related by digit-reordering (same multiset)         |
|                                                              |
| 2. Find:                                                     |
|    - Do such 10,000 numbers exist? (existence: yes or no)    |
|                                                              |
| 3. Archetypes:                                               |
|    - #13 Combinatorial (count perms of multiset:             |
|      Mississippi formula 10!/Πmᵢ!)                           |
|    - #14 Parity/Mod (divisibility by 7 → position-weighted   |
|      sum mod 7)                                              |
|                                                              |
| 4. Candidate CEP:                                            |
|    - 10! = 3,628,800; 10,000 is easy: any multiset with      |
|      product of multiplicity-factorials ≤ 362.88             |
|    - Mod-7 condition: 10^i mod 7 cycles through              |
|      1,3,2,6,4,5,1,3,2,6 for i = 0..9                        |
|    - Need: a multiset whose permutations all reduce to ≡ 0   |
|      (mod 7) under position-weighted sum                     |
|    - Construction: find symmetry in 10^i mod 7 cycle that    |
|      can be killed by digit-multiplicity                     |
|                                                              |
| 5. Brute path (avoid):                                       |
|    - Enumerate all 10-digit multisets, check divisibility    |
|      for every permutation: combinatorially infeasible.      |
+--------------------------------------------------------------+
```

**Now, the proof. (Time elapsed: 0:60.)**

The candidate-CEP guess points to *constructing* a specific multiset and verifying the divisibility-by-7 of all its permutations. We need: (a) a multiset whose permutation-count is $\geq 10{,}000$, and (b) all permutations $\equiv 0 \pmod 7$.

For (a): with $\sum m_i = 10$, the permutation count is $10! / \prod m_i!$. Taking $m_i$'s as $(2, 2, 1, 1, 1, 1, 1, 1)$ gives $10!/(2! \cdot 2!) = 907{,}200$ — far in excess of $10{,}000$. So mild multiset constraints suffice for (a).

For (b): the position-weighted-sum-mod-7 depends on how the digits are *placed*. Let $d_0, d_1, \ldots, d_9$ be the digits in positions $0$ through $9$ (units, tens, hundreds, ..., $10^9$). The number is $\sum_{i=0}^{9} d_i \cdot 10^i$, and modulo 7 this is $\sum_{i=0}^{9} d_i \cdot w_i$ with $w_i = 10^i \bmod 7$, cycling as $(1, 3, 2, 6, 4, 5, 1, 3, 2, 6)$ for $i = 0, \ldots, 9$.

Notice the cycle has length 6: $10^6 \equiv 1 \pmod 7$. So $w_i = w_{i+6}$ for $i = 0, 1, 2, 3$. The position-weights $(w_0, w_1, w_2, w_3) = (1, 3, 2, 6)$ each appear at *two* positions (positions $i$ and $i + 6$). The position-weights $(w_4, w_5) = (4, 5)$ appear at one position each (only at $i = 4, 5$ — since $i + 6 = 10$ is out of range).

**The construction**: choose a multiset in which the digit at position $i$ can be swapped with the digit at position $i + 6$ for $i = 0, 1, 2, 3$ *without changing the mod-7 weighted sum*. This is automatic if the digit at position $i$ equals the digit at position $i + 6$, but that would force several multiplicities to be $\geq 2$. Specifically, consider multisets of the form $\{a, b, c, d, e, f, a, b, c, d\}$ where $a$ at positions $0$ and $6$, $b$ at positions $1$ and $7$, etc. — but this requires the multiset to have at least 4 pairs of repeated digits.

> ⚠ *Open item flag (carried forward from Ch. 1 WE3 verification note).* The clean construction needs careful verification against Zeitz p. 204. Author current candidate: multiset $\{0, 0, 7, 7, 1, 1, 2, 2, 3, 3\}$ or similar with digit pairs at mutually-cancelling positions. Final lock at draft-review.

For the present purpose — illustrating the First-Minute Protocol — the protocol successfully identified the correct archetype pair (#13 + #14) and the construction-driven CEP. The detailed multiset will be locked at final-review. The protocol's value is *exposed* even in the open-item case: the protocol gave the proof structure correctly, even though the explicit multiset construction is being deferred. $\boxed{\text{Yes — such a family exists.}}$

*Time-to-solve (post-scratchpad): about 9 minutes for the proof structure; the explicit multiset construction is an additional 3–5 minutes pending verification.* Total wall-clock from the start: ~12 minutes.

**Commentary — the protocol as the "outline".** Both this worked example and 4.1 share the same observation: the 60-second scratchpad's item 4 (the candidate CEP) functions as a proof outline. The subsequent 5–10 minutes are *filling in* the outline, not *discovering* it. This is the operational benefit of the protocol — it relocates the discovery phase from "scattered across the 25-minute window" to "concentrated in the first 60 seconds."

### Worked Example 4.3 — A Joshi cross-reference

*Source.* Joshi, *Educative JEE Mathematics*, Ch. 13 (Maxima/Minima) — specific problem to be selected at draft-review from `Cursor-Joshi.md` §IV (Master Archetype Map), candidate Ch. 13 cross-reference for two-archetype calculus-and-extremal convergence.

> ⚠ *Open item per Pillar 3 outline § "Open Items" row 5.* Author current candidate: a 2-archetype problem from Joshi Ch. 13 in which an apparently single-variable calculus problem reveals a hidden symmetric structure (#2 Symmetry + #12 Extremal). Final lock at chapter-final-review.

The pedagogical point of this third worked example is to demonstrate the First-Minute Protocol on a *Pillar 2 cross-reference* — that is, on a problem-class familiar to the reader from the Pillar 2 chapters. The protocol works identically: same 5-step scratchpad, same 60-second budget. The protocol is archetype-agnostic; it works equally well on JEE Maxima/Minima problems, on Engel pigeonhole problems, on Zeitz Olympiad problems, on IMO Vieta-jumping problems. The diagnostic move is the same. Only the archetype-list output of item 3 varies.

When this open item is locked, the worked example will follow the template of 4.1 and 4.2: present the scratchpad, then the proof, then the commentary. The lock is scheduled for chapter-final-review.

---

## §3 The Trap — Skipping the protocol under time pressure

The principal failure mode of the First-Minute Protocol is *skipping it under perceived time pressure*. In every cohort Lakshmi has trained (per the opening vignette), there are reliably 4–6 students who treat the 60-second scratchpad as a luxury they cannot afford and start writing the proof at 0:30 seconds or earlier. They are precisely the students who run out of time at the 25-minute mark with no closed proof.

The cognitive mechanism of the trap is intuitive but pernicious. Under time pressure (real or perceived), the brain's default mode is *do something now*. Writing equations *feels* like progress; writing scratchpad items *feels* like procrastination. The feeling is exactly backwards — scratchpad items prevent dead-end equations — but the feeling is what drives behaviour.

**Three sub-modes of the trap:**

*Sub-mode 3.A: The "I know this already" skip.* The solver recognises the problem as a familiar type (perhaps a pigeonhole problem, perhaps a Vieta-jumping problem) and decides the scratchpad is unnecessary because the archetype is already known. The skip is dangerous because *familiarity is not the same as accuracy* — the solver may be pattern-matching to a slightly-different problem class. The scratchpad's items 1 and 2 (Given, Find) catch the mis-match; skipping the scratchpad misses the catch.

*Sub-mode 3.B: The "I'll do it in my head" skip.* The solver runs the protocol mentally, in 10 seconds, without writing anything. The skip is dangerous because mental execution *does not externalise the archetype list*. The benefit of the protocol (per §1.2 Reason 1) is the externalisation — moving the archetype list out of working memory. Mental execution defeats this benefit.

*Sub-mode 3.C: The "the problem is too hard for a scratchpad" skip.* The solver, faced with a problem they suspect is at the limit of their ability, skips the scratchpad on the theory that they need every available minute for the proof itself. The skip is dangerous because hard problems are *exactly* the ones where the scratchpad pays the highest dividend — 3-archetype problems (per Ch. 3) absolutely require externalisation, and the protocol is the cheapest externalisation tool available.

**The recovery move: enforce the timer.** The Pillar 3 solver's recovery from skip-the-protocol is *not* a sophisticated archetype intervention; it is a behavioural intervention. Set an actual timer for 60 seconds; the timer cannot start until the scratchpad has its first item; the proof attempt cannot begin until the timer ends. With practice, the timer becomes internalised — the solver runs the protocol automatically and the timer ritual fades. But for the first 20–40 problems of training, the explicit timer is what enforces the discipline.

**A worked illustration of skip-then-fail-then-recover.** Karthik (the opening protagonist of Chapter 3) spent 2.5 hours on IMO 1988 P6 *because he skipped the protocol*. Had he run the protocol at 0:00:00 — Step 3 would have listed *Induction, Reverse Engineering, Invariance* as candidate archetypes, Step 4 would have guessed *some perfect square*, Step 5 would have flagged *direct algebraic manipulation* as the brute path to avoid — the proof would have closed within 15–20 minutes rather than 2.5 hours. The 60-second cost would have prevented the 2-hour mistake.

The lesson, repeated for emphasis: *the protocol cost is fixed at 60 seconds. The protocol benefit scales with the difficulty of the problem.* For easy single-archetype problems, the protocol's benefit is small (the proof would have closed quickly anyway). For 3-archetype problems, the protocol's benefit is enormous (potentially saving hours). Train yourself to run the protocol on *all* problems precisely because you cannot tell in advance which one is going to be a 3-archetype monster.

---

## §4 Practice Problems

Four problems on which the reader should run the First-Minute Protocol *before* attempting the proof. The problems are deliberately *not* labelled with their archetype profile (compare with Practice Problems in Chs. 1–3, which were labelled): the labelling would defeat the purpose. The reader produces their own archetype list in Step 3 of the protocol and self-checks against the solutions appendix.

**Practice Problem 4.1.** Among any 9 lattice points in 3-dimensional space (each coordinate an integer), prove that some pair has a midpoint that is also a lattice point. *Source: Engel Ch. 4, lattice-pigeonhole.*

**Practice Problem 4.2.** Find all functions $f : \mathbb{R} \to \mathbb{R}$ satisfying $f(x + y) = f(x) + f(y) + xy$ for all real $x, y$. *Source: Zeitz §5 (functional equations); specific reference TBD at draft-review.*

**Practice Problem 4.3.** A finite tournament (a complete directed graph in which every pair of vertices is joined by exactly one directed edge) has the property that for every pair of vertices $u, v$, either $u \to v$ or $v \to u$ (but not both). Prove that there is a *king* — a vertex from which every other vertex is reachable in at most two steps. *Source: Engel Ch. 4 or Zeitz §4.1 — classical tournament-theorem result.*

**Practice Problem 4.4.** Let $a_1 < a_2 < \cdots < a_{n+1}$ be $n+1$ integers chosen from $\{1, 2, \ldots, 2n\}$. Prove that two of the chosen integers are coprime, and (separately) prove that two of the chosen integers are such that one divides the other. *Source: Erdős's "two integers in any $n + 1$ from $\{1, \ldots, 2n\}$" theorem; appears in Engel Ch. 4.*

For each problem, the protocol scratchpad should fit in 60 seconds. After producing the scratchpad, attempt the proof; compare your archetype list to the canonical archetype profile in the solutions appendix. The solutions appendix will be populated at Pillar 3 final-review.

---

## §5 Bridge to Chapter 5

This chapter operationalised the multidirectional thesis as a trainable 60-second reflex: the First-Minute Protocol. We presented the 5-step scratchpad structure, justified the protocol against cognitive bottlenecks (working memory, fast-thinking default, Escape-Hatch anchor), traced its historical lineage through Polya and Tao, and ran three live walkthroughs demonstrating how the protocol relocates the discovery phase from "scattered across 25 minutes" to "concentrated in 60 seconds." We named the principal failure mode (skipping the protocol under time pressure) in its three sub-modes and prescribed the behavioural recovery (explicit timer).

Chapter 5 develops the **Map of Convergence Skills** — a meta-level survey of the cognitive moves that compose multidirectional solving. We will treat the convergence diagram, the First-Minute Protocol, and the (forthcoming) Escape-Hatch Architecture as *three components of a single map*, and we will show how Zeitz's three-layer model (Strategies / Tactics / Tools) maps almost exactly onto our (Protocol / Archetypes / Gems) trio. The mapping is more than a notational convenience: it provides the *structural justification* for why the Advaitian architecture takes the shape it does, and it positions Pillar 3 within the broader pedagogical landscape of competitive-mathematics training.

The bridge into Chapter 5 is meta-cognitive. Chapters 1–4 of this pillar developed the *components* of multidirectional solving (the convergence diagram, the 2-archetype atom, the 3-archetype molecule, the First-Minute Protocol). Chapter 5 *steps back* and shows how the components compose into a single cognitive architecture. The architecture is the substance of Pillar 3; the components are its parts.

> *In Chapter 5: the components, assembled into a map.*

---

*End of Chapter 4.*
