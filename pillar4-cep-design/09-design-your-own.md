---
chapter: 9
pillar: 4
chapter_type: exercises
title: "Design Your Own + The Ethics of Difficulty"
subtitle: "From reader to maker, and what the maker owes the reader."
length_target_words: 6700
canonical_takeaway: "The reader who completes Pillar 4 has been handed the designer's toolkit; the ethics chapter closes with the moral responsibility the toolkit imposes on whoever takes it up."
status: draft
last_revised: 2026-05-28
references_invoked: [Lockhart-Part-II-Exultation, Polya-Inventor's-Paradox, Tao-Ch-1-strategy, IMO-1988-P6-capstone-reference, Pillar-2-archetypes]
voice_register: mixed-lockhart-constructive-tao-reflective
pillar3_cross_references: [pillar3-ch-8-§5]
---

# Chapter 9 — Design Your Own + The Ethics of Difficulty

> *"The first problem you design teaches you more about problem-solving than the hundredth problem you solve."*  
> — Anand Venkat, manuscript notebook, Pillar 4 closing notes, March 2026

---

## §0 — Chapter Opening: The Moment of Inversion

The pillar that closes with this chapter began, in Chapter 1, with a polemical argument: a problem is a designed object, made by a human author for a human reader, and the act of design is a discipline that mathematics education has decided not to teach. Eight chapters later — through the four-axis anatomy of Chapter 2, the 5-step Polya-inversion framework of Chapter 3, the twenty-five case studies of Chapters 4 through 8 — the reader has been brought to the moment of *inversion completion*: the reader who began Pillar 4 as a solver of designed problems is now ready to attempt the designer's role.

There is a candour I want to bring to this opening that the previous chapters did not require. Design is harder than solving. A solver who has worked through twenty-five excellent case studies has, in effect, served an apprenticeship under twenty-five master designers — the IMO 1959 problem committee, the IMO 1988 P6 problem committee, K.D. Joshi, the Putnam 1985 problem committee, and the others whose work we have read. The apprenticeship is real; the toolkit is real; the framework is real. But the first problem the reader designs will, almost certainly, be worse than the worst of the twenty-five case studies. This is not a failure. It is the universal experience of every first design in every creative discipline. The first sonnet the literature student writes is worse than the worst Shakespeare sonnet they have studied; the first sketch the architecture student draws is worse than the worst Pritzker-winning building they have analysed. The gap is not a sign that the student should not have tried; it is the gap that the *attempt* — and only the attempt — slowly closes.

The three design exercises that follow are deliberately graded so that the inversion is experienceable rather than overwhelming. The first exercise is at the JEE Advanced level (2 archetypes, Moderate CEP); the second at the Regional Mathematical Olympiad (RMO) level (3 archetypes, Hard CEP); the third at the IMO shortlist level (3 archetypes, Extreme CEP, requiring infinite-descent technique). For each exercise the chapter provides: the given CEP and target archetype profile (per Blueprint §8.11); a walkthrough of one possible design through all 5 steps of the framework from Chapter 3; and a *Designer's Rubric* assessment of the produced design. The reader's own designs will, of course, differ from the walkthroughs; the walkthroughs are illustrative rather than prescriptive.

The chapter closes with the *Designer's Rubric* itself (§4) and the *Ethics of Difficulty* (§5) — the philosophical and moral case for the discipline we have just spent eight chapters building.

We begin with the first exercise.

---

## §1 — Design Exercise 1 — Given CEP: *the integer 7*

**Target.** A *Moderate-tier* problem (JEE Advanced accessible), using two archetypes from Pillar 2. The "integer 7" is the given CEP — it is to play a structural role in the problem's answer or the constraint that yields the answer.

**Recommended archetype profile.** #14 (Parity / Modularity) + #11 (Existence).

**Sample design (one possible walkthrough through the 5 steps of Chapter 3):**

### [Step 1] Select the CEP

The CEP is given: *the integer 7*. The interpretation: the integer 7 should appear as a *structural answer* to the problem — either as the answer itself, or as a key constant in the answer, or as a constraint whose solution is forced by 7's structural properties (smallness, primality, etc.).

A natural reading: design a problem whose answer involves $7^2 = 49$ (the prime $7$'s square is the cleanest involvement of $7$ in a number-theoretic conclusion). The problem will ask the solver to identify integers satisfying some property, and the answer set will be a small finite set whose elements are tied to $7$ via the square $49$.

### [Step 2] Select the archetype convergence

The chapter recommends #14 (Parity / Modularity) + #11 (Existence). The convergence point: a quadratic equation $f(n, m) = 0$ whose solution set is determined by the discriminant being a perfect square, with the discriminant's factorisation involving $7$.

The simplest realisation: $n^2 + n + 7 = m^2$, which is a quadratic in $n$ with discriminant $1 - 4(7 - m^2) = 4m^2 - 27$. For integer $n$, the discriminant must be a perfect square: $4m^2 - 27 = k^2$, i.e., $(2m - k)(2m + k) = 27$. The factor pairs of $27$ are $(1, 27)$ and $(3, 9)$ (positive), giving $m = 7$ (with $k = 13$) and $m = 3$ (with $k = 3$). These give the asked-for integer $n$ values.

The factorisation $27 = 1 \cdot 27 = 3 \cdot 9$ is the *#14* move (modular structure of $27$ as $3^3$); the existence of $n$ satisfying the original equation given the discriminant condition is the *#11* move.

### [Step 3] Design the convergence path

The intended path:
- *Stage 1 (#14)*. Recognise that $n^2 + n + 7 = m^2$ requires the discriminant of the quadratic in $n$ to be a perfect square. Compute the discriminant: $4m^2 - 27$.
- *Stage 2 (#11)*. Set $4m^2 - 27 = k^2$, i.e., $(2m - k)(2m + k) = 27$. Enumerate factor pairs of $27$. Solve for $m$, then back-substitute for $n$.

Verification that the path is findable from the surface: a solver presented with *"find all positive integers $n$ such that $n^2 + n + 7$ is a perfect square"* would naturally try (a) small cases ($n = 1$ gives $9 = 3^2$ ✓; $n = 6$ gives $49 = 7^2$ ✓), (b) the discriminant approach as the next move once small-case enumeration appears to terminate. The path is reachable.

### [Step 4] Plant the traps

- **Trap 1: the brute-search trap.** The solver computes $n^2 + n + 7$ for $n = 1, 2, 3, \ldots, 50$ and finds only $n = 1$ ($= 9$) and $n = 6$ ($= 49$) as perfect squares. Generous: the small-case enumeration suggests the conjecture (only $n = 1$ and $n = 6$ work), priming the solver for the discriminant proof.
- **Trap 2: the inequality-bounding trap.** The solver attempts to bound $n^2 + n + 7$ between consecutive squares (analogous to the Ch. 3 §2 demonstration). Computation: $(n + \lfloor 1/2 \rfloor)^2 = n^2$ and $(n + 1)^2 = n^2 + 2n + 1$. So $n^2 < n^2 + n + 7 < n^2 + 2n + 1$ iff $n + 7 < 2n + 1$, i.e., $n > 6$. For $n \geq 7$, the expression is strictly between $n^2$ and $(n+1)^2$, hence not a square. For $n \leq 6$, check directly: $n = 1$ ($9$) ✓, $n = 2$ ($13$) ✗, $n = 3$ ($19$) ✗, $n = 4$ ($27$) ✗, $n = 5$ ($37$) ✗, $n = 6$ ($49$) ✓. So the answer is $n \in \{1, 6\}$. *The bracketing argument is a complete proof in its own right* — and a cleaner one than the discriminant argument. The "trap" turns out to be an alternative honest path. This is the same phenomenon as the Ch. 3 §2 demonstration (where complete-the-square was an alternative path to bracketing for the $n^2 + 5n + 5$ problem).

The discovery that two honest paths exist is fine. The designed problem has both available; the case study should present both with their respective lessons.

### [Step 5] Craft the statement

Final statement:

> *Find all positive integers $n$ such that $n^2 + n + 7$ is a perfect square.*

Eleven words plus the expression. The schoolroom register (*"is a perfect square"*) is preserved; the universal-quantifier (*"find all"*) demands enumeration. The constant $7$ in the polynomial is the structural anchor: it is the prime whose factorisation $27 = 3^3$ powers the discriminant analysis, and it appears in the answer as $7^2 = 49$.

**Designed problem:** *"Find all positive integers $n$ such that $n^2 + n + 7$ is a perfect square."*  
**Answer:** $n \in \{1, 6\}$ (giving $n^2 + n + 7 = 9$ and $49$).

### Rubric assessment

By the criteria of §4 below: cleanness of surface (clean — 11 words, schoolroom register); depth of CEP (modest — the integer 7's role is structural but not deep); trap quality (good — both the brute-search and bracketing/discriminant traps are generous); archetype non-obviousness (modest — a discerning solver can guess #14 + #11 from the structure); pedagogical lift (good — the solver learns the bracketing technique).

**Rubric score:** Solid Moderate-tier design. Acceptable as a JEE Advanced problem or a Regional Mathematical Olympiad warm-up.

---

## §2 — Design Exercise 2 — Given CEP: *the golden ratio $\varphi$*

**Target.** A *Hard-tier* problem (RMO accessible), using three archetypes from Pillar 2. The golden ratio $\varphi = (1 + \sqrt{5})/2$ is the given CEP — it should emerge as the answer to a limit, an asymptotic ratio, or a closed-form value the solver computes.

**Recommended archetype profile.** #18 (Induction) + #4 (Hidden Structure) + #16 (Reverse Engineering).

**Sample design:**

### [Step 1] Select the CEP

The CEP is given: $\varphi$. The interpretation: $\varphi$ should arise as the answer to a problem that, on its surface, does *not* mention the golden ratio. The design's centre of gravity is the *concealment* — the solver must discover $\varphi$ through computation rather than be told it.

A natural realisation: a recurrence whose solutions involve $\varphi$ through Fibonacci-like asymptotic ratios.

### [Step 2] Select the archetype convergence

The three archetypes: #18 (Induction — to characterise the recurrence), #4 (Hidden Structure — to recognise Fibonacci behind the surface), #16 (Reverse Engineering — to work backward from "what limit would $\varphi$ be?" to the structural identity $\varphi = 1 + 1/\varphi$).

Convergence: the solver computes terms of the recurrence, observes the ratios stabilising, recognises Fibonacci, identifies $\varphi$ as the limit ratio via the characteristic equation $\varphi^2 = \varphi + 1$.

### [Step 3] Design the convergence path

The intended path:
- *Stage 1 (#18)*. Define a sequence and compute first several terms.
- *Stage 2 (#4)*. Recognise the Fibonacci recurrence (or a recurrence whose characteristic equation has $\varphi$ as a root).
- *Stage 3 (#16)*. Solve the characteristic equation; identify the limit ratio.

Sample design: Define $a_1 = 1$ and $a_{n+1} = 1 + 1/a_n$ for $n \geq 1$. Compute: $a_2 = 2, a_3 = 3/2, a_4 = 5/3, a_5 = 8/5, a_6 = 13/8, a_7 = 21/13, \ldots$ — these are ratios of consecutive Fibonacci numbers. The limit of $a_n$ is the fixed point of $f(x) = 1 + 1/x$, which is $x = (1 + \sqrt{5})/2 = \varphi$.

### [Step 4] Plant the traps

- **Trap 1: the fixed-point-by-computation trap.** The solver writes $L = 1 + 1/L$ to find the limit, gets $L^2 = L + 1$, solves $L = (1 \pm \sqrt{5})/2$, and takes the positive root. Generous: this is exactly the intended path's culmination.
- **Trap 2: the wrong-fixed-point trap.** The solver computes the limit naively and gets $L = (1 - \sqrt{5})/2 \approx -0.618$ (the other root). Verification: the sequence $a_n$ stays positive (since each $a_n > 0$ inductively), so the negative root is excluded. Generous: teaches that limit-by-fixed-point arguments require checking the *sign* (or other constraints) consistent with the sequence's range.
- **Trap 3: the convergence-non-rigorous trap.** The solver assumes (without proof) that the sequence converges and then computes the limit. The convergence requires a separate proof (monotone-bounded subsequences, or a Banach-fixed-point argument). Generous if the solver completes the convergence proof; less so if they skip it.

### [Step 5] Craft the statement

> *Let $a_1 = 1$ and $a_{n+1} = 1 + \dfrac{1}{a_n}$ for $n \geq 1$. Prove that the sequence $\{a_n\}$ converges, and determine its limit in closed form.*

Twenty-five words plus the recurrence. The statement does not mention the golden ratio, Fibonacci, or $\sqrt{5}$. The solver discovers all three.

**Designed problem:** *"Let $a_1 = 1$ and $a_{n+1} = 1 + 1/a_n$ for $n \geq 1$. Prove that the sequence $\{a_n\}$ converges, and determine its limit in closed form."*  
**Answer:** $\lim a_n = \varphi = (1 + \sqrt{5})/2$.

### Rubric assessment

Cleanness of surface: clean — the recurrence is a one-line definition. Depth of CEP: deep — $\varphi$ is a fundamental constant of mathematics with deep historical resonance. Trap quality: excellent — the wrong-fixed-point trap teaches a real lesson about sign-consistency in fixed-point arguments. Archetype non-obviousness: good — most solvers will not immediately recognise the Fibonacci connection. Pedagogical lift: high — the solver leaves with the fixed-point method for limit computation plus the Fibonacci-$\varphi$ connection.

**Rubric score:** Strong Hard-tier design. Acceptable as an RMO problem.

---

## §3 — Design Exercise 3 — Given CEP: *0 as the unique solution*

**Target.** An *Extreme-tier* problem (IMO shortlist accessible), using three archetypes from Pillar 2. The CEP is the uniqueness of the trivial solution $(0, 0, \ldots, 0)$ to a Diophantine equation — the "no nontrivial solution" conclusion that requires infinite-descent technique.

**Recommended archetype profile.** #18 (Induction / infinite descent) + #14 (Parity / Modularity) + #1 (Invariance).

**Sample design:**

### [Step 1] Select the CEP

The CEP is given: "$0$ is the unique solution." Interpretation: the problem will ask the solver to prove a Diophantine equation has only the trivial solution $(0, 0, \ldots, 0)$, with the proof requiring infinite-descent technique.

### [Step 2] Select the archetype convergence

Three archetypes: #18 (Induction / descent — to repeatedly reduce a hypothetical non-trivial solution to a smaller solution), #14 (Parity / Modularity — to detect divisibility by 2 or some other prime that drives the descent), #1 (Invariance — to track the invariant quantity preserved under the descent).

### [Step 3] Design the convergence path

The intended path:
- *Stage 1 (#14)*. Reduce the equation modulo a small prime (often 2). Conclude that each variable must be divisible by that prime.
- *Stage 2 (#18)*. Substitute $x = 2x'$, etc., and re-derive a *smaller* equation of the same form. Iterate.
- *Stage 3 (#1)*. The invariance: each iteration of the descent reduces the variables by a factor of 2 (in 2-adic valuation), so the original variables must be infinitely divisible by 2 — hence zero.

Classical example: $x^3 + 2y^3 + 4z^3 = 0$ over $\mathbb{Z}$. Reducing mod 2: $x^3 \equiv 0 \pmod 2$, so $x \equiv 0 \pmod 2$. Write $x = 2x'$ and substitute: $8(x')^3 + 2y^3 + 4z^3 = 0$, i.e., $4(x')^3 + y^3 + 2z^3 = 0$. Reduce mod 2: $y^3 \equiv 0 \pmod 2$, so $y \equiv 0 \pmod 2$. Write $y = 2y'$: $4(x')^3 + 8(y')^3 + 2z^3 = 0$, i.e., $2(x')^3 + 4(y')^3 + z^3 = 0$. Reduce mod 2: $z^3 \equiv 0 \pmod 2$, so $z \equiv 0 \pmod 2$. Write $z = 2z'$: $2(x')^3 + 4(y')^3 + 8(z')^3 = 0$, i.e., $(x')^3 + 2(y')^3 + 4(z')^3 = 0$ — *the same equation in $(x', y', z')$*. Descent: each variable is divisible by 2 indefinitely, hence each is zero.

### [Step 4] Plant the traps

- **Trap 1: the mod-arithmetic-only trap.** The solver tries to derive non-existence from modular reductions alone (mod 2, mod 3, mod 4, etc.) without invoking descent. Mod 2 reduction gives $x \equiv 0$ but does not by itself give $y, z \equiv 0$. Generous: teaches that mod-arithmetic is a *first move* in descent problems but not the whole proof.
- **Trap 2: the wrong-substitution-order trap.** The solver substitutes $x = 2x', y = 2y', z = 2z'$ all at once and discovers the equation reduces by a factor of $8$. They get $8x'^3 + 16y'^3 + 32z'^3 = 0$, i.e., $x'^3 + 2y'^3 + 4z'^3 = 0$ — the same equation. The descent works, but the solver may not realise that the *substitution-by-2* requires *first* establishing each variable's divisibility by 2 *individually* via the mod-2 argument. Generous: teaches the careful order of operations in descent proofs.
- **Trap 3: the constructive-search trap.** The solver attempts to find non-trivial solutions by computer search (or hand calculation). For small bounds, no non-trivial solutions appear. The trap is that empirical absence is not a proof; descent provides the proof. Generous: confirms the conjecture but motivates the structural argument.

### [Step 5] Craft the statement

> *Find all integer solutions $(x, y, z)$ of the equation $x^3 + 2y^3 + 4z^3 = 0$.*

Fifteen words plus the equation. The statement does not announce that the answer is "only trivial" — the solver must discover the negation-of-non-triviality. The phrasing *"find all"* invites the solver to enumerate; the structural answer (only $(0, 0, 0)$) is the conclusion of the descent.

**Designed problem:** *"Find all integer solutions $(x, y, z)$ of the equation $x^3 + 2y^3 + 4z^3 = 0$."*  
**Answer:** Only the trivial solution $(x, y, z) = (0, 0, 0)$.

### Rubric assessment

Cleanness of surface: extremely clean — fifteen words. Depth of CEP: deep — infinite descent over the ring $\mathbb{Z}[\sqrt[3]{2}]$ (or its analogue), connecting to Fermat-style descent traditions. Trap quality: excellent — three pedagogically rich traps. Archetype non-obviousness: high — the descent technique is non-obvious without prior exposure. Pedagogical lift: very high — the solver leaves with the infinite-descent method in a non-trivial setting.

**Rubric score:** Strong Extreme-tier design. Acceptable as an IMO shortlist problem.

---

## §4 — The Designer's Rubric

The five criteria, each scored on a five-point scale (1 = unacceptable, 5 = exemplary):

| Criterion | Question to ask of the designed problem |
|---|---|
| **1. Cleanness of surface statement** | Does the statement read naturally? Is every word load-bearing? Could a stranger to the design understand what is being asked without footnotes? |
| **2. Depth of CEP** | Is the CEP a genuinely beautiful mathematical object, or merely a tricky configuration? Will the solver, having discovered the CEP, walk away with a piece of transferable mathematics? |
| **3. Trap quality** | Are the traps generous (each teaching a lesson on failure) or punishing (each wasting time)? Can each trap be named in 3–5 words? |
| **4. Archetype non-obviousness** | Could a strong solver guess the archetype profile from the surface statement alone? If yes, the design has leaked too much information. |
| **5. Pedagogical lift** | What does the solver learn that they did not know before? Is the lesson generalisable to subsequent problems, or specific only to this one? |

A designed problem scoring at least 4 on every criterion is *publishable* at the intended difficulty tier. A problem scoring below 3 on any single criterion requires re-design. The rubric is intended as a *gate* for the designer's own work — a checklist to be applied *before* submitting a designed problem to an external audience.

Three notes on application.

First, the rubric is calibrated by difficulty tier. A Moderate-tier problem cannot, by definition, score 5 on *Depth of CEP* (since Moderate CEPs are by design at the accessible end of the depth spectrum); the maximum achievable Depth score at the Moderate tier is approximately 3.5. The reader should adjust expectations accordingly: a 3.5 on Depth at the Moderate tier is equivalent to a 5 at the Extreme tier.

Second, criteria 1 and 4 (Cleanness of surface and Archetype non-obviousness) are in productive tension. A maximally clean statement tends to reveal the archetype profile by making the structural reading obvious; a maximally concealed statement tends to introduce ambiguity that hurts cleanness. The designer's calibration on these two criteria is among the most consequential design choices.

Third, criterion 5 (Pedagogical lift) is the rubric's most important criterion and the one that distinguishes a *designed problem* from a *competition entry*. A problem can score perfectly on criteria 1–4 and still fail to teach the solver anything beyond the specific technique it requires; such a problem is competitively valid but pedagogically poor. The designer who has internalised Pillar 4 should aim for problems that score well on Pedagogical Lift even at the cost of a slightly lower score on Archetype Non-obviousness.

---

## §5 — The Ethics of Difficulty

The eight chapters that precede this section have made an extended technical argument about how problems are designed. This final section makes the moral argument that the technical work has been building toward.

A problem can be *hard-and-deep* or *hard-and-arbitrary*. Both are difficult in the proximate sense — both will frustrate the solver — but the two are categorically different in their relationship to mathematical truth and to the solver's intellectual development. The hard-and-deep problem is hard because the underlying mathematics is genuinely subtle and the discovery of its CEP rewards the solver with a transferable insight; the hard-and-arbitrary problem is hard because the designer has imposed an artificial obstacle (an unmotivated computation, an obscure formula, a tedious case-check) that, once cleared, leaves the solver no better equipped than before. The first is mathematics; the second is hazing.

Every competitive mathematics culture has its own characteristic balance between the two. The IMO, at its best, is overwhelmingly weighted toward hard-and-deep — the twenty-five case studies in Chapters 4 through 8 are exemplars of the deep variety. The Putnam, similarly. The JEE Advanced, in its modern form, leans somewhat toward hard-and-arbitrary by virtue of its time pressure (which rewards execution speed over depth) and its emphasis on computational rather than structural problems. The Indian Olympiad Pathway (RMO → INMO → IMOTC → IMO) operates somewhere in between, with a steady drift from the JEE-style arbitrary toward the IMO-style deep as the student progresses through the levels. The Indian Statistical Institute's entrance examinations, by contrast, are usually well-weighted toward depth.

What does the distinction *look like* in practice? An indicative example. The problem *"compute the integral $\int_0^1 (1 - x)^n x^k \, dx$ for given $n, k$"* is hard-and-arbitrary if posed without context — the solver computes the beta function value with no transferable insight. The same problem posed as *"a closed-form for the value of the integral defines a combinatorial identity for binomial coefficients; find the identity and prove it"* is hard-and-deep — now the solver discovers, via the beta-function value $B(k+1, n+1) = k! n! / (n + k + 1)!$, the combinatorial identity $1/((k+1)\binom{n+k}{k+1})$, and the connection between continuous and discrete combinatorics. Same computation, different design, different pedagogical lift.

The contemporary olympiad culture has, I think, three pathologies that the design framework of Pillar 4 is in a small way an attempt to counter. The first is *the cult of difficulty for its own sake* — the assumption that a harder problem is, by virtue of being harder, a better problem. This is false. A problem is good or bad based on the quality of its CEP, the generosity of its traps, and its pedagogical lift; difficulty is a *consequence* of these properties, not a *cause* of them. A great Moderate-tier problem is better than a mediocre Extreme-tier problem, full stop. Designers and curators of problem collections should resist the pressure to optimise primarily for difficulty.

The second is *the worship of obscurity*. There is a temptation, when a problem uses a technique most solvers will not know, to assume the obscurity *is* the difficulty and that the problem is therefore good. Sometimes this is true (IMO 1988 P6's Vieta-jumping requirement is exactly this kind of consequential obscurity, because the technique it introduces is *transferable*). Sometimes it is not (a problem requiring an obscure trick that has no application outside the specific problem is just a trick problem, regardless of how rare the trick is). The test is *transferability* — does the obscure technique generalise? Designers should err on the side of techniques that survive multiple problems.

The third is *the conflation of cleverness with depth*. A clever problem is one that admits an unexpected short solution; a deep problem is one whose mathematics is rich enough that the unexpected short solution emerges *because of the depth* rather than as a separate cleverness. The two are correlated but not identical. The IMO 1988 P6 Vieta-jumping is both clever and deep; many lesser problems are clever without being deep (the cleverness is the whole content, and once revealed the problem is exhausted). The cleverness-without-depth class of problem is the most dangerous in competitive mathematics because it most easily seduces the problem-setter into thinking they have produced something significant. Designers should ask, of each clever-looking problem: *what does the solver learn that they did not know before?* If the answer is *only that this specific cleverness works for this specific problem*, the problem is shallow.

These three pathologies are not unique to mathematics. Every craft with a competitive culture — chess composition, architecture criticism, classical music performance — has analogous failure modes. What is specific to mathematics, and what makes the failure modes especially consequential, is that competitive mathematics is also one of the primary *recruiting* mechanisms for the discipline. The students who succeed in JEE Advanced, RMO, INMO are the students who pursue mathematical careers; the curriculum of the competitions therefore shapes the *aesthetic taste* of the next generation of mathematicians. If the competitions reward hard-and-arbitrary problems, the next generation learns to make hard-and-arbitrary problems; if the competitions reward hard-and-deep, the next generation learns the depth. The designer's responsibility scales accordingly.

What does responsible problem design look like? Six commitments, each of which can be operationalised by the designer:

1. **Test for transferability.** Before publishing a designed problem, ask: *what technique does this teach? Could the technique be applied to other problems?* If the answer is no, redesign or shelve.
2. **Calibrate to the audience.** A problem at the JEE Advanced level should test JEE-syllabus archetypes; a problem at the IMO level should test the IMO-canonical archetypes. Designers writing for a level should know that level's archetype expectations and stay within them, with one or two stretch archetypes per problem at most.
3. **Audit the traps.** Each trap should teach a lesson on failure. Generous traps are designed; punishing traps are bugs. Walk each trap path before publishing.
4. **Provide a clean alternative if one exists.** When a problem admits two honest paths to the answer (as Exercise 1 in this chapter does, with the bracketing and discriminant approaches), the designer's published solution should present *both* paths, with their respective lessons. The reader who finds the alternative deserves the recognition.
5. **Engage with the solvers' experience.** Before publishing, share the problem with at least three solvers at the target level. Their feedback — where they got stuck, what trap they fell into, whether the CEP felt rewarding — is the only reliable signal that the design is calibrated. Don't skip this step.
6. **Acknowledge the lineage.** When a problem extends or is inspired by an earlier problem (often the case for new IMO-style problems that build on classical setups), the designer's published commentary should acknowledge the predecessor. The lineage is part of the design's value; concealing it impoverishes the cultural record.

The six commitments are the *ethics* of difficulty. They are not, individually, novel; each has been articulated by various problem-setters over the past century. What is new — what I think is new — is the attempt to articulate them as a *coherent* code, derived from the technical framework of the preceding eight chapters, and offered to the reader who has now been handed the toolkit. The reader who works through Pillar 4 inherits the toolkit; the ethics specify what the toolkit is *for*.

The ultimate test of any framework is what it does to the people who internalise it. Pillar 4's hope is that the reader who completes it will, in the years that follow, approach every designed problem they encounter — whether as solver, as teacher, as curator, or as designer — with a vocabulary that previous generations of mathematicians have had to acquire through long apprenticeship rather than explicit instruction. The architecture school that the opening vignette of Chapter 1 imagined as a nightmare can, in some small way, be unwound. We have not unwound all of it; one book is one book. But the door, I hope, is now visible. Whether to walk through it is the reader's choice.

---

## §6 — Bridge to Pillar 5

The pillar that closes here — Pillar 4, *The Art of CEP-Based Problem Design* — has been the volume's most original contribution. It has taken material that previous problem-solving books have left in the realm of tacit taste (the working mathematician's knowledge of *what makes a good problem*) and rendered it as explicit craft: a four-axis anatomy (Chapter 2), a five-step design framework (Chapter 3), twenty-five worked case studies (Chapters 4–8), three guided design exercises (Chapter 9 §1–§3), a five-criterion rubric (§4), and a six-commitment ethics (§5). The pillar is, I believe, the first systematic problem-design curriculum in Indian mathematical pedagogy, and one of the few systematic such curricula anywhere.

The next and final pillar of Volume 1 — *Pillar 5: Mathematical Gems* — turns from problem design to *the tools and named theorems that well-designed problems most often deploy*. Where Pillar 4 has taught the reader to read problems through the lens of the four anatomical axes, Pillar 5 will give them a curated library of the small, beautiful, repeatedly-useful mathematical objects (Vieta jumping, Catalan numbers, Sophie Germain identity, the Pythagorean parametrisation, generating functions, the lifting-the-exponent lemma, and others) that appear and reappear across the olympiad canon. Pillar 5 is the *toolbox* that complements Pillar 4's *workshop manual*. Together they complete Volume 1's preparation of the reader for the mathematical-craft tradition that the book has, throughout, been trying to recover.

We turn there now.

---

*End of Chapter 9. End of Pillar 4.*
