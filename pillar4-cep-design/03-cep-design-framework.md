---
chapter: 3
pillar: 4
chapter_type: essay
title: "The 5-Step CEP Design Framework"
subtitle: "Polya, inverted."
length_target_words: 6300
canonical_takeaway: "The designer's procedure is Polya's solver-procedure run backwards — five steps that begin from the chosen insight and engineer the problem outward."
status: locked
last_revised: 2026-05-29
locked_on: 2026-05-29
references_invoked: [Polya-Part-I-four-phase, Polya-Part-III-Inventor's-Paradox, Polya-Part-IV-solutions, Tao-Ch-1-nine-strategies, Lockhart-Part-II-Exultation]
voice_register: polya-systematic
pillar3_cross_references: [pillar3-ch-4-§1-FMP]
---

# Chapter 3 — The 5-Step CEP Design Framework

> *Polya, inverted.*

---

## §0 — Opening: The Inversion

George Polya, in *How to Solve It* (1945), proposed that all mathematical problem-solving could be organised into four phases.[^polya-four-phase] The phases are so well-known that they are repeated in nearly every problem-solving book published since: *Understand the problem. Devise a plan. Carry out the plan. Look back.* For three-quarters of a century these four phases have been the spine of every olympiad-training programme worth the name; Terence Tao's nine-strategy framework in *Solving Mathematical Problems* (2006) is an explicit Polya descendant;[^tao-polya-cite] Arthur Engel's *Problem-Solving Strategies* and Paul Zeitz's *Art and Craft of Problem Solving* both build on the Polya scaffold; the Pillar 3 First-Minute Protocol (Chapter 4 of this book's preceding pillar) is, structurally, a 60-second compression of Polya Phases 1 and 2. The Polya tradition is the air in which all serious problem-solving pedagogy breathes.

[^polya-four-phase]: G. Polya, *How to Solve It: A New Aspect of Mathematical Method*, 2nd edition, Doubleday Anchor Books, 1957. The four-phase framework is the spine of Part I and is elaborated throughout Part III's "Short Dictionary of Heuristic." Cf. `Cursor-Polya.md` §III, where the four phases and their accompanying questionnaire are reconstructed from the visible PDF pages of the workspace scan.

[^tao-polya-cite]: Tao, *Solving Mathematical Problems*, 2nd ed., Oxford University Press, 2006, Ch. 1: *"There are several general strategies and perspectives to solve a problem correctly; (Polya 1957) is a classic reference for many of these."* Source: `tao-solving-math-problems.txt` line 207; `Cursor-Tao.md` §VIII.

What this chapter proposes — and what is, I believe, the most consequential proposal in Pillar 4 — is that the Polya framework, *read in reverse*, is also the spine of problem *design*. The four phases of solving, when inverted, become four (then five — one will split) phases of designing. The mapping is precise. It is not metaphor. The solver's "understand the problem" becomes the designer's "identify the CEP." The solver's "devise a plan" becomes the designer's "select the archetype convergence." The solver's "carry out the plan" becomes the designer's "design the path the solver will travel." The solver's "look back" — the most consequential phase for both solver and designer — splits, in the designer's hands, into two distinct moves: *plant the traps that will catch unlearned alternatives,* and *craft the surface statement that will conceal the CEP while preserving the path's traversability.*

This is the 5-Step CEP Design Framework. It is the procedural complement to the four-axis anatomy of Chapter 2. The anatomy gave the reader an *analytical* instrument; the framework gives them a *constructive* one. The case-study chapters (4 through 8) will apply the anatomy retrospectively to twenty-five real designed problems. This chapter, §2 in particular, will apply the framework *prospectively* — designing one new problem in real time, in front of the reader, so that they can watch the procedure operate.

The framework's five steps, in their canonical order, are:

```
+--------+------------------------------------+----------------------------------+
| Step   | Designer's move                    | Polya phase (inverted)            |
+--------+------------------------------------+----------------------------------+
|  1     | Select the CEP                     | Understand the problem →          |
|        |                                    |   designer: choose the insight    |
|  2     | Select the archetype convergence    | Devise a plan →                   |
|        |                                    |   designer: choose the path       |
|  3     | Design the convergence path        | Carry out the plan →              |
|        |                                    |   designer: engineer traversability|
|  4     | Plant the traps                    | Look back (part 1) →              |
|        |                                    |   designer: anticipate wrong paths |
|  5     | Craft the statement                | Look back (part 2) →              |
|        |                                    |   designer: conceal & enable      |
+--------+------------------------------------+----------------------------------+
```

The order of the five steps is not arbitrary, and §1 will defend the order step by step. The framework is, of course, *iterative* in practice: a designer working on a real problem will discover, at Step 4, that the trap-planting reveals an unanticipated traversability gap in Step 3 and will loop back; or will discover, at Step 5, that the cleanest statement-craft forces a re-choice of archetypes in Step 2. The five steps are the spine; the iteration is the muscle.

What follows is the formal definition of each step, the design-thinking that lives inside each step, and then a sustained worked demonstration in which I — Anand — design, in front of the reader, one Moderate-tier problem from scratch, narrating each step.

---

## §1 — The Five Steps

### Step 1 — Select the CEP

The CEP — the Central Elegant Point — is the single mathematical insight the designed problem is built around. We named it in Chapter 2 §1.1 as the *destination* of the solver's journey. The designer's first move is to *choose* that destination.

This step is, in some senses, the only step in the framework that is purely creative. The four steps that follow are engineering: selecting components, fitting parts, calibrating tolerances. Step 1 is the act of *choosing what to engineer toward*, and as such it is the step that admits the most varied designer's taste and the least systematic guidance.

Some things can be said about how to choose well.

The CEP should be a *real mathematical object* — an identity, a closed-form, a structural truth — and not merely a numerical answer. *"The answer is 42"* is not a CEP; *"the answer is the Catalan number $C_n = \binom{2n}{n}/(n+1)$ because the problem reduces, by a balanced-parentheses bijection, to counting Dyck paths"* is a CEP. The CEP is the *why* of the answer, not the *what*. A designer who selects a CEP that is only a number, with no deeper structural anchor, will discover at Step 5 that they cannot craft a statement that conceals it — because there is nothing to conceal.

The CEP should be *small enough to be discoverable* by the target solver. This is where the four difficulty tiers of Blueprint §8.2 come in. A Moderate-tier CEP fits in a single short identity or one clean structural observation. A Hard-tier CEP requires the simultaneous recognition of two such observations. An Extreme-tier CEP requires three, often with one of the three being a technique the solver has to reconstruct or rediscover for themselves. Choosing the CEP is *also* choosing the difficulty tier; the two decisions are inseparable.

The CEP should be *resonant* — should, ideally, connect to mathematical content the solver already cares about. A CEP that is the Sophie Germain identity (Pillar 4 Case 2, IMO 1969 P1) is resonant because the solver who discovers it has acquired a piece of mathematics that *generalises*: Sophie Germain identities of the form $n^4 + 4k^4$ are a small but real corner of number theory, and the solver leaves the problem with a tool they can take elsewhere. A CEP that is merely *the number 17, computed via a specific cancellation* is much less resonant; the solver learns no transferable mathematics.

These three criteria — real, discoverable, resonant — are the designer's checklist for Step 1. The criteria are not a mechanical procedure; they are a set of taste-guides. The CEP Library (`knowledge_base/ThinkMath_Blueprint_v3.md`, summarised in Blueprint §8.2) is the designer's *pre-stocked* catalogue of CEPs that satisfy all three criteria at each difficulty tier; a designer beginning their work can choose a CEP from the Library or invent a new one, with the Library as the calibration point.

### Step 2 — Select the Archetype Convergence

With the CEP chosen, the designer asks: *which sequence of archetype applications will reach this CEP?* The choice is the *path* of the problem, in the sense established by the Pillar 3 §7.6 convergence diagram.

Step 2 is the step that most directly inherits the Pillar 3 multidirectional toolkit. A 2-archetype convergence is Moderate-tier. A 3-archetype convergence is Hard or Extreme. A 4-archetype convergence (IMO 1988 P6, the capstone of Chapter 8) is the rare extreme case where four archetypes must operate simultaneously. Step 2's selection is, simultaneously, the third decision the designer makes about the problem's difficulty (the first being the CEP's complexity in Step 1; the second being implicit in the resonance of the chosen CEP).

The selection has constraints. Not every archetype pair can converge on every CEP. The Sophie Germain identity is best reached by #4 (Hidden Structure) + #16 (Reverse Engineering); attempting to reach the same identity via #2 (Symmetry) + #8 (Domain Translation) is possible but extremely awkward. The designer's craft, at Step 2, is to identify the *minimum* archetype set that converges cleanly on the chosen CEP. If three archetypes work but two suffice, choose two — the leaner the convergence, the cleaner the problem.

A second-order consideration: the chosen archetypes should be ones the target solver has been *trained* in. A problem designed for the IMO can assume the solver has all 20 archetypes available; a problem designed for the JEE Advanced can assume a narrower set (the Joshi Ch. 24 case study, our Case 5, deliberately uses #10 + #12 because these are the archetypes most cleanly anchored in the JEE Advanced syllabus). The archetype selection is also a *curricular* statement: the problem will *test* exactly the archetypes the designer selects.

### Step 3 — Design the Convergence Path

Steps 1 and 2 have decided *where* the solver is going (the CEP) and *which archetypes* they will use. Step 3 decides *how* — what specific intermediate computations will lead from the surface statement to the convergence point.

This is the most invisible step in the framework, and the one that distinguishes a well-designed problem from a coincidentally-correct one. At Step 3 the designer asks: *is the path I have in mind actually traversable from the surface I am about to design?* A designer who fails this step produces a problem whose intended solution is invisible to any solver who does not already know the answer — the path "exists" in the designer's head but is not findable from the problem's surface.

Step 3 is the step where the designer must, themselves, become the solver. The designer plays out the intended convergence with the eye of a solver who has never seen the problem before, and asks: at each transition between intermediate results, would I notice that the transition is the natural next move? If the answer is no — if at some step the move requires *knowing the answer in advance* — the path is not yet a problem; it is a calculation. The designer must redesign.

The most common failure mode at Step 3 is the *over-clever step*. The designer, working backward from the CEP, identifies a beautiful but obscure transformation that closes the path. They are pleased with the cleverness. They forget that the solver, working forward from the surface, has no reason to suspect that transformation exists. The transformation is *not findable from the surface*. The resulting problem is solvable only by a solver who has seen the same transformation elsewhere or who happens by luck to try it. The transformation may be mathematically beautiful in isolation; it is bad design.

A second failure mode is the *brute-degeneration*. The designer's intended path is elegant, but a brute-force computation (often coordinate geometry, often direct algebra, often case-analysis) closes the problem in a different way that the solver can stumble into without ever seeing the intended elegance. The brute path *should* exist — it should be a planted trap (Step 4) — but it should be *expensively unsatisfying* enough that the solver is naturally driven to the elegant path. If the brute path is no harder than the elegant path, the problem fails to teach the elegance; the solver wins without learning. (The *Brute Path → Elegant Pivot* tension the designer engineers here is the same one Pillar 1 names in its six-point grammar and Pillar 3 drills in the First-Minute Protocol; Pillar 4 is where the author plants it deliberately.)

Step 3, then, asks two questions about the intended path: *is it findable from the surface?* and *is the elegant path strictly more rewarding than every alternative?* If both answers are yes, the path is designed; if either answer is no, the designer iterates back to Step 2 (different archetypes might produce a better path) or Step 1 (a different CEP might admit a better convergence).

### Step 4 — Plant the Traps

With the convergence path designed, the designer turns to the *wrong* paths. Step 4 asks: *what plausible approaches will look promising but lead nowhere, and how do I arrange the problem so that each such approach is generously diagnostic?*

We have already discussed traps in Chapter 2 §1.3. A trap is a deliberate feature, not a bug. A well-designed trap is one that, when the solver realises the approach is failing, leaves them *oriented toward* the actual solution rather than disoriented in general. Each trap is a small lesson; the trap-catalogue of a problem is the catalogue of lessons the solver receives whether or not they consciously notice receiving them.

The designer's craft at Step 4 has two parts. First, *anticipate* the traps. A designer who has not played out the wrong-path computations themselves will discover, after the problem is set, that solvers fall into traps the designer never noticed — and that the unanticipated traps are often ungenerous, wasting time without teaching. Second, *generosity-test* each trap. A trap that takes thirty minutes of failed computation before the solver realises it is wrong is acceptable if the realisation comes with a lesson; a trap that takes thirty minutes and leaves the solver only with frustration is unacceptable. The designer must walk each anticipated wrong path through to its failure point and ask: *what would the solver have learned from this work?* If the answer is *nothing*, the trap is bad; the designer either re-engineers the problem to eliminate the trap (often by changing a constant) or accepts the trap with the recognition that the problem will lose marks for that reason.

A subtle point: Step 4 is *not* about adding traps. The traps usually pre-exist; they are the natural wrong moves that any solver would try. Step 4 is about *recognising* which traps exist, *evaluating* their pedagogical quality, and *adjusting the surface* to maximise their generosity. A designer at Step 4 is rarely planting *new* obstacles; they are mostly auditing the obstacle field that the chosen CEP and archetypes have already produced.

### Step 5 — Craft the Statement

The final step is the most under-noticed. With CEP, archetypes, path, and traps all designed, the designer must now write the *words* of the problem statement. We named the four word-choice axes in Chapter 2 §1.4: rhetorical posture, quantifier choice, definite/indefinite articles, register (technical vs. schoolroom).

The designer's craft at Step 5 has two simultaneous obligations. First, the statement must be *unambiguous* — every word must have a single mathematical interpretation, every quantifier must scope exactly the intended objects, every named quantity must be a quantity the solver can compute or recognise. Second, the statement must *conceal* the CEP and the intended path *just enough* — enough that the solver must discover the CEP for themselves, but not so much that the CEP is undiscoverable. The two obligations are in tension. A statement that maximally conceals usually achieves the concealment by introducing ambiguity (vague quantifiers, undefined terms, multiple parseable interpretations); a statement that maximally clarifies usually achieves the clarity by hinting at the path (naming the relevant quantities, using technical register that flags the relevant techniques).

The compromise the designer must engineer is: *minimum hinting at the path, maximum clarity about the question*. This is harder than it sounds. The IMO 1959 P1 statement we analysed in Chapter 2 §2 is a case study in how to do it: *"in lowest terms"* (schoolroom register, conceals the Euclidean algorithm) instead of *"$\gcd = 1$"* (technical register, hints at the Euclidean algorithm), *"every natural number $n$"* (universal quantifier, requires a proof) instead of *"some specific values of $n$"* (existential quantifier, would invite computation). Every choice in that statement is calibrated.

Step 5 is the step at which a designer's drafts of the same problem can differ most dramatically. The same CEP, the same archetypes, the same path, the same traps — and yet two different statements can produce two different difficulty experiences. A good designer iterates Step 5 several times, often more than they iterate Steps 1-4 combined, because the final word-by-word craft is where the problem's *texture* is set.

---

## §2 — The Worked Demonstration: Designing a Problem from Scratch

I want to spend the rest of this chapter walking through the framework on a problem I will design in front of you, step by step, without rehearsal. The design is happening as I write. The choices I make are choices a designer would actually make; the iterations and the second-guessings are real; the final problem we end up with is one we will use, in Chapter 4 §6 or §7 perhaps, as a worked example. Or perhaps not — perhaps the demonstration will produce a problem that, on Step 5 critique, is not quite good enough. We shall see.

The terms of the exercise. I will design a *Moderate-tier* problem — appropriate to the JEE Advanced level, accessible to a well-prepared Class XII student in India or to a strong undergraduate elsewhere. I will use exactly two archetypes, which is the standard for Moderate-tier per Blueprint §8.2. I will work in the *number-theory* topic area because that is where Moderate-tier problems most commonly live and because the reader who has worked through Pillars 2 and 3 has the most archetypal vocabulary there.

### [Step 1] Selecting the CEP

I begin with the choice of CEP. Three criteria from §1: real, discoverable, resonant.

The CEP I will select is: ***no positive integer $n$ satisfies the equation*** — that is, the answer to the designed problem will be *"no solution exists."*

Why this CEP? Because *"no solution exists"* is one of the most under-used answer-types at the Moderate tier, and it has a pedagogical generosity that the more common *"the answer is some specific $k$"* does not have. The student who proves *"no solution exists"* via a structural argument has acquired a tool — typically *bracketing* or *parity*, depending on the form — that they can carry to other problems. The student who computes *"the answer is $k = 7$"* via some specific machinery learns only the machinery, which often does not transfer. Polya's *Inventor's Paradox* (`Cursor-Polya.md` §IV Sample 2) speaks directly to this: *"The more ambitious plan may have more chances of success."* A *no-solution* CEP is the inventor's-paradox CEP par excellence — proving non-existence is more ambitious than enumerating solutions, and the structural arguments that prove non-existence are usually cleaner than the computational arguments that find specific solutions.

Real? Yes — *"no positive integer satisfies a specific polynomial equation"* is a structural mathematical fact, not merely a number.

Discoverable? At the Moderate tier, yes: bracketing between consecutive squares is the standard discovery move. The student who has worked through Pillar 2 Chapter 1 (Invariance) has met this move.

Resonant? Yes — bracketing-between-consecutive-squares is a transferable technique that appears in many olympiad problems, and the student leaves the problem with the technique in hand.

CEP locked: *the bracketing-between-consecutive-squares structure that forces no integer solution.*

### [Step 2] Selecting the archetype convergence

The CEP is structural; what archetypes converge on it?

The bracketing-between-consecutive-squares move is a direct application of **#11 (Existence)** in its non-existence specialisation: prove that no integer satisfies a constraint by showing that the candidate quantity is *strictly* between two consecutive integers (here, two consecutive squares). The bracketing itself is a **#14 (Parity/Modularity)** move in a broad reading — the *modulus* being the gap between consecutive squares — but I am going to record the second archetype more honestly as **#4 (Hidden Structure)**, because what the student actually discovers is the *structural identity* that the polynomial in question lies between two specific quadratic forms in $n$.

Two archetypes: #11 + #4. Confirms Moderate-tier per Blueprint §8.2.

I should note here that I considered #14 + #11 (parity + existence) as an alternative convergence. The advantage of #14 + #11 would be that *modulo arguments* are also discoverable at the Moderate tier and the student is well-trained in them. The disadvantage is that modulo-based non-existence proofs require finding the *right* modulus, which is harder than finding the right bracketing. I am choosing #4 + #11 over #14 + #11 because the bracketing argument is more *visible from the surface* — the student who sees a quadratic in $n$ and is asked whether it is ever a perfect square will, with high probability, *try* to compare it to nearby squares. The discovery move is natural.

Step 2 locked: archetypes #4 + #11.

### [Step 3] Designing the convergence path

The student starts from the surface (which I have not yet designed; that's Step 5). They confront a polynomial in $n$. They want to know if it is ever a perfect square. They will, naturally, compute the polynomial for small values of $n$. They will observe that it is not a square for $n = 1, 2, 3, \ldots$ They will then ask: *is it ever a square?*

The convergence path I want is:
- **Stage 1 (archetype #4).** Recognise that the polynomial, for large enough $n$, lies strictly between two specific consecutive squares: $(n+k)^2 < P(n) < (n+k+1)^2$ for some integer $k$ depending on the polynomial.
- **Stage 2 (archetype #11).** Conclude that the polynomial cannot equal any perfect square in the range $n \geq N_0$ for some $N_0$; verify the small-$n$ cases directly.
- **Convergence.** The polynomial is never a perfect square for any positive integer $n$.

For this path to *be the path*, the polynomial must satisfy: for some integer $k$ and some $N_0$, the inequality $(n+k)^2 < P(n) < (n+k+1)^2$ holds for all $n \geq N_0$. I need to choose $P(n)$ so that the inequality holds, ideally for *all* positive $n$ (so the proof closes without small-case checking — a cleaner proof).

Let me set $P(n) = n^2 + an + b$ for unknown $a, b$. I want $(n+k)^2 < n^2 + an + b < (n+k+1)^2$ for all $n \geq 1$, where $k$ is some positive integer.

$(n+k)^2 < n^2 + an + b$
$n^2 + 2kn + k^2 < n^2 + an + b$
$2kn + k^2 < an + b$
$(a - 2k)n > k^2 - b$

For this to hold for all $n \geq 1$: we need $a > 2k$ (so the left side grows with $n$) and the inequality to hold at $n = 1$, i.e., $a - 2k > k^2 - b$.

$n^2 + an + b < (n+k+1)^2$
$n^2 + an + b < n^2 + (2k+2)n + (k+1)^2$
$(a - 2k - 2)n < (k+1)^2 - b$

For this to hold for all $n \geq 1$: we need $a < 2k + 2$ (so the left side decreases or stays bounded) — but we also need $a > 2k$ from the other inequality. So $2k < a < 2k + 2$, which forces $a = 2k + 1$ (since $a$ is integer).

With $a = 2k + 1$, the two inequalities become:
- $(2k+1 - 2k)n > k^2 - b$, i.e., $n > k^2 - b$, i.e., $b > k^2 - n$. For all $n \geq 1$: $b > k^2 - 1$, i.e., $b \geq k^2$.
- $(2k+1 - 2k - 2)n < (k+1)^2 - b$, i.e., $-n < (k+1)^2 - b$, i.e., $b < (k+1)^2 + n$. For all $n \geq 1$: $b < (k+1)^2 + 1$, i.e., $b \leq (k+1)^2$.

So $k^2 \leq b \leq (k+1)^2$.

Let me try the smallest case: $k = 2$, $a = 2k+1 = 5$, $b$ between $4$ and $9$.

If $b = 5$: $P(n) = n^2 + 5n + 5$. Check: $(n+2)^2 = n^2 + 4n + 4 < n^2 + 5n + 5$ iff $n + 1 > 0$ — yes for $n \geq 1$. And $n^2 + 5n + 5 < (n+3)^2 = n^2 + 6n + 9$ iff $n + 4 > 0$ — yes for $n \geq 1$. So $P(n) = n^2 + 5n + 5$ is strictly between $(n+2)^2$ and $(n+3)^2$ for all $n \geq 1$, hence never a perfect square.

This is the polynomial I will use. The path is verified: the student who computes $P(n)$ for small $n$, notices it never lands on a square, and *then* tries the bracketing argument will close the proof in three lines.

Step 3 locked: $P(n) = n^2 + 5n + 5$, bracketed by $(n+2)^2$ and $(n+3)^2$ for all $n \geq 1$.

### [Step 4] Planting the traps

What are the wrong paths a student will try?

**Trap 1: factor the quadratic.** The student will try to factor $n^2 + 5n + 5$. Discriminant: $25 - 20 = 5$, which is not a perfect square. The quadratic does not factor over the integers. Lesson: not every quadratic-in-$n$ problem is a factorisation problem. Generous trap.

**Trap 2: complete the square.** The student will try $n^2 + 5n + 5 = (n + 5/2)^2 + 5 - 25/4 = (n + 5/2)^2 - 5/4$. Multiplying by 4: $4(n^2 + 5n + 5) = (2n + 5)^2 - 5$. So *if* $n^2 + 5n + 5 = m^2$ then $(2n + 5)^2 - 4m^2 = 5$, i.e., $(2n+5-2m)(2n+5+2m) = 5$. Since $5$ is prime, the factorisation gives $\{2n+5-2m, 2n+5+2m\} = \{1, 5\}$ or $\{-1, -5\}$ or $\{-5, -1\}$ or $\{5, 1\}$. Solving: $\{1, 5\}$ gives $2n + 5 = 3$, $m = 1$, i.e., $n = -1$ (not positive). $\{-1, -5\}$ gives $2n + 5 = -3$, $m = 1$, i.e., $n = -4$ (not positive). So no positive integer solutions. **This is, actually, a complete proof.** The complete-the-square approach closes the problem cleanly. It is *not* a trap; it is an alternative honest path.

Hmm. Let me reconsider. The complete-the-square path works. This means my intended bracketing path is not the *only* honest path. Is the alternative more or less rewarding than the intended path?

The complete-the-square path requires the student to:
1. Recognise that the equation $n^2 + 5n + 5 = m^2$ can be transformed.
2. Multiply by 4 and complete the square to get $(2n+5)^2 - (2m)^2 = 5$.
3. Factor the difference of squares.
4. Use the primality of 5 to enumerate factor pairs.
5. Verify that no positive integer $n$ falls out.

The bracketing path requires the student to:
1. Observe that $P(n)$ lies between $(n+2)^2$ and $(n+3)^2$.
2. Conclude no perfect square.

The bracketing path is *shorter* and *more elegant*. But the complete-the-square path is *more rewarding pedagogically* because it teaches a transferable technique (difference of squares + primality). Both paths exist; both are honest; the designer has not chosen between them. This is fine — sometimes a problem has multiple honest paths, and the designer's job is to ensure that *all* honest paths are educational. Both here are.

I will leave both paths in place. The problem has *two* archetype-convergences honest to it: my intended #4 + #11 (bracketing) and an alternative #4 + #14 (complete-the-square + primality). The case study, when we draft it, can present both.

**Trap 3: brute search.** The student computes $P(1), P(2), P(3), \ldots, P(50)$, observes none is a square, conjectures the answer. Cannot prove without a structural argument. Same trap as IMO 1959 P1 Trap 1. Generous; teaches that empirical evidence is not proof.

**Trap 4: modulo arithmetic.** The student tries $P(n) \pmod{3}$ or $\pmod{4}$ to find a residue that excludes squareness. $P(n) \pmod{3}$: depends on $n \pmod 3$. Quick computation: $n \equiv 0$: $P \equiv 5 \equiv 2$. $n \equiv 1$: $P \equiv 1 + 5 + 5 = 11 \equiv 2$. $n \equiv 2$: $P \equiv 4 + 10 + 5 = 19 \equiv 1$. So $P(n) \pmod 3 \in \{1, 2\}$ depending on $n$. Squares mod 3 are in $\{0, 1\}$. So $P(n) \not\equiv 2 \pmod 3$ would exclude squareness, but $P(n)$ *is* $\equiv 1$ when $n \equiv 2 \pmod 3$, so mod-3 does *not* close the problem. The trap is that mod-3 *almost* works (excludes 2/3 of cases) but not quite. Generous; teaches that modular arithmetic is a partial tool — sometimes you exclude many cases but not all.

Four traps, three of them generous, one of them not a trap at all (the complete-the-square path is a real alternative). The trap-catalogue is acceptable. The problem is designable.

Step 4 audit complete.

### [Step 5] Crafting the statement

I want a statement that:
- Uses universal quantifier ("for all positive integers $n$" or "find all positive integers $n$").
- Uses the "no solution exists" framing, which is what makes the inventor's paradox work.
- Does not hint at the bracketing technique (no naming of squares-near-$P(n)$).
- Does not hint at the complete-the-square technique (no mentioning of $4P(n)$).
- Is short and uses schoolroom register where possible.

Candidate 1: *"Find all positive integers $n$ such that $n^2 + 5n + 5$ is a perfect square."*

This is clean. Universal quantifier ("find all"), schoolroom register ("perfect square"), no hints. Length: thirteen English words plus one expression. Compares favourably to IMO 1959 P1 (eighteen words).

The asked-for property is *"is a perfect square."* The schoolroom phrasing — *"perfect square"* — is used throughout Indian school mathematics and is the most accessible register. A technical-register alternative ("for which $\exists m \in \mathbb{Z}$ with $m^2 = n^2 + 5n + 5$") would hint at the equation-solving approach (which is the complete-the-square path); the schoolroom phrasing keeps both paths equally on the table.

I tested two alternatives:
- *"Prove that $n^2 + 5n + 5$ is never a perfect square for any positive integer $n$."* — This *gives away the answer* (no positive integer works). The student is told the answer and asked only for the proof. This is a Tier-3-low statement; it converts a slightly harder *find* problem into an easier *prove* problem. I reject this for now.
- *"Show that the equation $m^2 = n^2 + 5n + 5$ has no solutions in positive integers."* — This *hints at the algebraic structure* (the equation form invites the complete-the-square move). I reject this because I want both paths equally available.

Candidate 1 is the chosen statement.

**Final problem.**

> Find all positive integers $n$ such that $n^2 + 5n + 5$ is a perfect square.

Answer: there are none. Proof (bracketing path): $(n+2)^2 = n^2 + 4n + 4 < n^2 + 5n + 5 < n^2 + 6n + 9 = (n+3)^2$ for all $n \geq 1$, so $n^2 + 5n + 5$ lies strictly between two consecutive perfect squares and is therefore not itself a perfect square.

The framework has produced a designed problem in five steps, with the design narrated. The problem has two honest convergence paths (the bracketing path I designed for, and the complete-the-square path I discovered during Step 4 trap-audit) and three generous traps. The CEP is "no positive integer solution exists," reached via #4 + #11. The statement-craft uses the schoolroom register and the universal quantifier.

I would not claim this is a *great* problem. It is a *Moderate-tier* problem, designed to demonstrate the framework rather than to enter the lineage of legendary problems. Whether it is publishable in a JEE-prep volume depends on whether the volume needs a problem of exactly this archetype profile; whether it would survive an IMO problem-committee review is doubtful, because the bracketing technique is too well-trodden at that level. What I do claim is that the design *was systematic*: every choice was named, every alternative was considered, every trap was audited, and the final problem is the product of explicit moves rather than tacit taste. The framework worked.

This is what Chapter 9's three guided design exercises will ask the reader to do, on their own, with the framework in hand.

---

## §3 — The Counter-Argument

**SIMPLICIO.** Anand, the worked demonstration of §2 is impressive but it strikes me as artificial. You did not actually design a problem worth setting; you produced a textbook exercise. The legendary problems — the IMO 1988 Problem 6 you keep referring to as your capstone — were not produced by anything like your 5-step framework. They were produced by mathematicians with genius-level taste, working in flow states, on time-scales of weeks or months. Your framework cannot produce IMO 1988 P6; you have implicitly admitted as much by calling the §2 product *"a Moderate-tier problem."* Why should I learn a framework whose output is below the level of the problems I actually want to engage with?

**SALVIATI.** The objection conflates two distinct claims: that the framework can produce a problem, and that the framework can produce a *great* problem. I claim the first; I do not claim the second. Greatness — the IMO 1988 P6 level — requires accumulated taste that the framework does not supply; it requires the mathematician to have internalised, over decades, what the framework names explicitly. The framework is the *teachable substrate*. Taste is the *non-teachable accumulation*. A piano student who has learned the major scales and the basic chord progressions has not become Glenn Gould; but they have learned the substrate that, given thirty years of practice and a particular kind of mind, *could* become Gould. The framework is to problem design as the major scales are to piano: necessary but not sufficient, teachable but not the whole thing.

**SIMPLICIO.** Then what use is it to me, who am not going to become the IMO problem-committee's designer-in-residence?

**SALVIATI.** Three uses, the same three I named in Chapter 1 §3. You become a better solver, because you can read the four-axis anatomy of every problem you encounter. You stop misattributing difficulty, because you know the difficulty has named sources. And you join the lineage, in the limited sense that you will have done the work the lineage does, and you will see — from inside — that the work is teachable. Whether you join the lineage in the *substantial* sense (whether you design problems that other people use) is up to you and the next thirty years of your life. The framework is the door. Walking through it is your choice.

**SIMPLICIO.** The honesty of the answer disarms me.

**SALVIATI.** It is the honest answer. I will not promise the reader that this chapter has taught them to design problems at the level of the problems we will study in Chapters 4 through 8. I will promise them that they have, by the end of Chapter 9, designed three problems of their own — and that the discipline of having designed them will change how they read the next problem they encounter.

---

## §4 — Bridge to Chapter 4

We have, in Chapters 1 through 3, completed the *framework half* of Pillar 4. Chapter 1 argued, polemically, that problems are designed objects. Chapter 2 installed the four-axis analytical instrument. Chapter 3 inverted the analytical instrument into a five-step constructive procedure. The framework is now in the reader's hands.

The next five chapters — 4, 5, 6, 7, 8 — are the *case-study half* of Pillar 4. We will apply the framework's anatomical instrument retrospectively to twenty-five real designed problems, ascending in difficulty from the Moderate tier through the Mid, High-mid, High, and Extreme tiers, culminating in IMO 1988 P6 as the capstone of Chapter 8. Each case study is a worked example of the four-axis anatomy, structured per the §8.10 sub-template: problem statement, designer's architecture (CEP / archetypes / traps / statement-craft), the reader's re-solution in clean Pillar-2 commentary form, and two or three lessons for the designer that the reader could lift and apply to their own work.

Chapter 4 begins with five Moderate-tier cases. The opening case is the problem we have already met twice: IMO 1959 Problem 1, the canonical clean opening of the entire IMO archive, now read as a fully-worked case study rather than as a demonstration target. We turn there now.

---

*End of Chapter 3.*
