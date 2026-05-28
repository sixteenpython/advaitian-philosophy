---
chapter: 2
pillar: 4
chapter_type: essay
title: "Anatomy of a Well-Designed Problem"
subtitle: "Open the back of the watch."
length_target_words: 5800
canonical_takeaway: "Every well-designed mathematical problem has four nameable parts: a Central Elegant Point at its centre, an archetype convergence that reaches it, traps that protect it from cheap alternatives, and a statement that conceals it."
status: draft
last_revised: 2026-05-28
references_invoked: [Tao-Ch-1, Tao-Preface, Polya-Part-I, Engel-Ch-1, IMO-1959-P1]
voice_register: tao-warm
pillar3_cross_references: [pillar3-ch-1-§1]
---

# Chapter 2 — Anatomy of a Well-Designed Problem

> *Open the back of the watch.*

---

## §0 — Opening: The Back of the Watch

The first time I opened the back of a Swiss watch I was sixteen. It was a pocket-watch my father had inherited from his grandfather, and one Sunday afternoon I unscrewed the case-back with a coin and looked in. What I saw was difficult to describe at the time and remains difficult now. There were gears, of course; I had expected gears. There was a coiled spring; I had expected the spring. What I had not expected was that every piece in the mechanism had a shape that fit, with millimetre precision, only into the piece next to it. The whole apparatus was tighter than I had any reason to believe a hand-made object could be. I understood, in that moment, the difference between *using* the watch and *seeing* the watch. From the front it was a tool that told time. From the back it was a small civilisation of decisions.

I had seen the same watch every day for sixteen years before I looked at the back.

There is a corresponding moment for every reader of mathematics, and most readers never have it. The moment is the first time you look at a problem and *see the mechanism*: the gears the designer chose, the spring that drives the central motion, the way each part fits only the part next to it. Until that moment you have been using the problem — staring at it, solving it, scoring marks on it. After that moment you cannot stop seeing the mechanism, and it changes how you read every problem you encounter afterward. The arrow of attention has reversed. You are no longer the consumer of an object made by an unseen author; you are, however momentarily, the *peer* of that author, watching them work.

Vikram Sundaresan, whom we met in Chapter 1, has spent six years staring at the front of the watch.[^vikram] He is very good at telling the time. He has scored well in every exam that asked him to tell the time. But he has, by his own subsequent admission, never opened the back. The reason is not that he lacked curiosity; the reason is that nobody told him there was a back. The architecture school inside which his mathematical education has unfolded has never put a screwdriver in his hand and said: *here, this comes off, look at what is inside.* This chapter is the screwdriver. The rest of the pillar is what you will see when you have used it.

[^vikram]: Vikram Sundaresan continues from Ch. 1; the protagonist is invented, the trajectory is composite. Anand has worked with several students who, after the moment described in this chapter, reported the same thing: *I cannot un-see it.*

The analytical instrument we will install in this chapter has four parts. We will name them now, define them, and then — across the rest of §1 and the full length of §2 — we will put them to work on a single, simple, designed problem so that the reader can watch the instrument operate. The four parts are not novel; every working problem-setter has tacit knowledge of all four. What is novel is the systematic *naming*, the commitment that no future Pillar 4 case study will be analysed along any axis other than these four, and the discipline this naming will impose on every chapter that follows.

The four parts are: the **Central Elegant Point**, the **Archetype Convergence**, the **Planted Traps**, and the **Statement-Craft**. We take them in order.

---

## §1 — The Four Anatomical Axes

### §1.1 The Central Elegant Point (CEP)

Every well-designed problem is built around a single central mathematical insight. We have already been calling this insight the Central Elegant Point, or CEP, following the terminology established in Pillar 4's working materials.[^cep-origin] The CEP is the thing the designer wanted the solver to discover. It is the *reward* of the problem — the moment of "oh, *that's* what was going on here" — and everything else in the problem is engineered to make that reward emerge for the solver at the right time.

[^cep-origin]: The CEP terminology is established in `knowledge_base/ThinkMath_Blueprint_v3.md` and was developed during the multi-year run-up to the present book. The library of canonical CEPs is summarised in Blueprint §8.2 and will be elaborated in Chapter 3 of this pillar.

A CEP is not the same as the *answer* to the problem. The answer to IMO 1959 Problem 1 — which we will dissect at length in §2 — is "yes, $(21n+4)/(14n+3)$ is in lowest terms for every $n$." That answer is binary; it carries no aesthetic charge by itself. The *CEP* of the problem is the observation that the Euclidean algorithm applied to the numerator and denominator terminates in two short steps at $\gcd = 1$, regardless of $n$. The CEP is the *insight that makes the answer feel inevitable* once you see it. The answer is the proposition; the CEP is the *why*.

CEPs come in tiers. A Moderate-tier CEP is one a strong undergraduate can discover within ten minutes of focused work: a single short identity, a clean modular argument, a one-step pigeonhole at the right scale. A Hard-tier CEP requires the solver to combine two such insights and to recognise that the combination is the path; a strong undergraduate may need an hour or several. An Extreme-tier CEP requires three or more insights to converge, often with one of them being a technique the solver has not previously seen and must reconstruct from the problem itself. The 25-case slate of Chapters 4 through 8 is calibrated to walk the reader through these tiers in order, with five cases at each tier.

The CEP is the answer to the designer's first and most consequential question: *what mathematical insight do I want this problem to teach?* The cleanness of the CEP is the first determinant of the problem's aesthetic value. If the CEP is fuzzy — if the answer to "what is the central insight here?" requires three paragraphs to state — the problem will feel diffuse and unsatisfying no matter how technically challenging it is. If the CEP is crisp, the problem can carry an enormous amount of computational machinery on its back without losing its shape, because the reader who has discovered the CEP has *the explanation* for everything else they had to do.

### §1.2 The Archetype Convergence

The CEP is the destination. The Archetype Convergence is the *path*.

In Pillar 2 we identified twenty universal problem-solving archetypes — patterns of mathematical move that recur across thousands of problems, from JEE Advanced to the IMO, from Engel to Zeitz to Joshi. In Pillar 3 we identified the central cognitive truth about hard problems: hard problems are not hard because the archetype is exotic; they are hard because the solution requires *multiple* archetypes to operate simultaneously, and the solver must maintain all of them in working memory long enough for the convergence point to appear. The two-archetype convergence diagram of Pillar 3 §7.6 is the structural backbone of that observation:

```
            ┌─────────────────┐
            │ Problem statement │
            └────────┬──────────┘
                     │
       ┌─────────────┴──────────────┐
       │                            │
       ▼                            ▼
┌────────────────┐         ┌────────────────────┐
│  Archetype A   │         │   Archetype B      │
│   applied      │         │     applied        │
│  generates     │         │   generates        │
│  intermediate  │         │   intermediate     │
│   result A'    │         │    result B'       │
└──────┬─────────┘         └─────────┬──────────┘
       │                             │
       └────────────┬────────────────┘
                    ▼
            ┌───────────────┐
            │  Convergence  │
            │   (the CEP)   │
            └───────┬───────┘
                    │
                    ▼
              ┌──────────┐
              │  Answer  │
              └──────────┘
```

What Pillar 4 adds — by inverting the diagram — is the recognition that *the designer chose the archetypes*. The archetype convergence is not an accident of the problem's structure; it is a deliberate selection. The designer asked: *which two (or three, or in rare cases four) archetypes do I want this problem to demand of the solver?* And then the designer engineered the problem so that *those specific archetypes*, and not others, would be the ones whose simultaneous application closes the problem.

The choice has consequences. A problem that demands #1 (Invariance) + #14 (Parity/Modularity) is a fundamentally different teaching object than a problem that demands #2 (Symmetry) + #8 (Domain Translation), even if both problems have the same surface and the same final answer. The first teaches the solver to look for hidden conserved quantities; the second teaches the solver to look for hidden symmetries that map one configuration to another. The designer who picks one archetype combination over another is, in effect, deciding which lesson the problem will deliver.

This is the second anatomical axis: every designed problem has an archetype profile, and the profile is a craft choice. When we dissect IMO 1959 P1 in §2 we will identify exactly which two archetypes its designer selected; when we dissect IMO 1988 P6 in Chapter 8 we will identify the unique four-archetype convergence that makes it the legendary case it is.

The convergence diagram, in Pillar 4, becomes the *designer's map*. Reading the diagram from top to bottom tells us how the solver gets from surface to CEP. Reading it from bottom to top tells us how the *designer* worked: they started from a chosen CEP, picked an archetype combination that could reach it, and then engineered a problem statement whose only honest solution required that exact combination.

### §1.3 The Planted Traps

The third axis is the one most students will not, at first, believe is part of the design. *Traps* — that is, plausible-looking approaches that lead nowhere — are not accidents of the problem. They are *deliberate*. A well-designed problem plants traps the way a well-designed building places columns: with intent, in specific locations, for specific reasons.

The reason a designer plants traps is pedagogical. Each trap is a lesson the solver receives whether or not they consciously notice the lesson. The trap that "looks like a standard substitution will work" teaches, by its failure, that this is not a problem the standard substitution handles — and the *taste of that failure* primes the solver to look for the non-standard approach. The trap that "looks like induction is the obvious method" teaches that induction, in this case, requires a non-obvious inductive hypothesis. The trap that "looks like coordinate geometry will compute the answer" teaches that coordinate geometry will indeed compute the answer, but the computation is so heavy that the problem is plainly inviting a different method. Each trap is a *negative gesture* — a "not this way" — and the negative gestures together carve out the positive direction.

Bad traps exist too. A bad trap is one that wastes the solver's time without teaching anything — that punishes a plausible approach without leaving the solver any better equipped to find the right one. A designer's craft, in this dimension, is to plant only *generous* traps: traps that, when the solver realises the approach is failing, leave them oriented toward the actual solution rather than disoriented in general. The IMO problem-setting committees are unusually careful about this; the Putnam committee is somewhat less so; the JEE Advanced paper-setters, by historical accident, are sometimes egregiously careless. Pillar 4 will, in several case studies, point at specific examples of generous and ungenerous trap-design and ask the reader to distinguish them.

When we dissect IMO 1959 P1 in §2 we will identify three planted traps in that one short problem. The reader who has not previously noticed how many *not-this-ways* are encoded in even the cleanest moderate-tier problem will, I think, be surprised.

### §1.4 The Statement-Craft

The fourth axis is the surface presentation: the words of the problem statement, in the order the designer chose them, in the syntax the designer chose, with the asked-for property phrased as the designer chose to phrase it. The statement is the part of the problem the solver encounters first; everything else (the CEP, the convergence, the traps) is downstream of what the statement allows the solver to *see*.

Statement-craft is the most under-discussed of the four anatomical axes, and possibly the most consequential. Two problems with identical mathematical content can have radically different difficulty depending only on the words of the statement. A problem stated as "*find all positive integers $n$ such that…*" primes the solver to enumerate; a problem stated as "*prove that there exist infinitely many $n$ such that…*" primes the solver to construct. A problem that gives the solver a diagram primes them to think geometrically; the same problem without the diagram primes them to think analytically. A problem that names a quantity primes the solver to treat that quantity as central; the same problem with the quantity un-named requires the solver to *discover* its centrality, which is a much harder cognitive demand.

The designer's statement-craft is the deliberate choice of which of these cognitive primings to install. Sometimes the choice is to *help* the solver — to provide a hint that orients them toward the intended path. Sometimes the choice is to *conceal* — to deny the solver a priming so that they must discover the orientation themselves. The decision between helping and concealing is one of the most consequential decisions in problem design, and the right answer depends entirely on what the problem is *for*. A teaching problem in a textbook should usually help; an IMO problem should usually conceal; a JEE Advanced problem in an examination context should help just enough that the strong candidate can recognise the path under time pressure.

We will identify, in §2's dissection of IMO 1959 P1, the single most consequential word-choice in that problem statement — the word the designer must have spent the most time choosing. The reader who has not previously thought of problem statements as having *consequential word choices* will, again, be surprised.

These four — CEP, Archetype Convergence, Planted Traps, Statement-Craft — are the canonical anatomical axes for the rest of Pillar 4. Every case study in Chapters 4 through 8 will be analysed along all four. Every design exercise in Chapter 9 will be evaluated against all four. The remainder of this chapter is the demonstration that the four are sufficient — that no fifth axis is needed to give a complete reading of even a fairly subtle designed problem.

---

## §2 — The Worked Demonstration: IMO 1959 Problem 1

The problem, in the IMO Compendium's verified form:[^imo59p1]

> Prove that, for every natural number $n$, the fraction $(21n+4)/(14n+3)$ is in lowest terms.

[^imo59p1]: *The IMO Compendium*, problem statement at `imo-compendium.txt` near line 700; this is IMO 1959, the very first IMO, Problem 1. The Compendium's §3.1 holds the contest problems; §4.1 holds the solutions.

This is, on paper, the cleanest problem in the entire 1959–2024 International Mathematical Olympiad corpus. It is the first problem of the first IMO. It involves no specialised vocabulary beyond *fraction* and *lowest terms* — every high-school student in the world has these concepts. It can be stated in eighteen English words. And — for reasons that this section will spend twenty paragraphs unpacking — it is one of the most carefully designed problems in the history of mathematical olympiads.

Let us dissect it.

### The Central Elegant Point

The CEP of IMO 1959 P1 is the Euclidean algorithm applied to the specific pair $(21n+4,\ 14n+3)$, terminating in exactly two steps at $\gcd = 1$, for every $n \in \mathbb{N}$.

Concretely: we compute
$$\gcd(21n+4,\ 14n+3) = \gcd(21n+4 - (14n+3),\ 14n+3) = \gcd(7n+1,\ 14n+3).$$
We then compute
$$\gcd(7n+1,\ 14n+3) = \gcd(7n+1,\ 14n+3 - 2(7n+1)) = \gcd(7n+1,\ 1) = 1.$$
The Euclidean algorithm has hit $\gcd = 1$ in two reduction steps. The fraction is therefore in lowest terms. The proof is three lines long.

The CEP, as I have stated it, is not just *"the Euclidean algorithm works."* The Euclidean algorithm works on *every* pair of integers. The CEP, more precisely, is the observation that *for this particular pair*, the algorithm terminates in exactly two steps at the unit, and the termination is independent of $n$ because the linear-combination coefficients (which are constants: $1$ in the first step, $2$ in the second) do not involve $n$. The *uniformity over $n$* is what makes the problem a problem rather than a calculation.

This is the elegance. The designer chose a specific pair of bilinears in $n$ such that the Euclidean algorithm would close in exactly two steps with $n$-independent coefficients. There are infinitely many pairs of bilinears one could write down; only a tiny fraction of them have this property; the designer selected one that did.

### The Archetype Convergence

What archetypes did the solver use? The §7.6 diagram, instantiated for this problem:

```
            ┌─────────────────────────┐
            │ (21n+4)/(14n+3) in      │
            │ lowest terms for all n? │
            └────────────┬────────────┘
                         │
       ┌─────────────────┴────────────────┐
       │                                  │
       ▼                                  ▼
┌──────────────────┐              ┌──────────────────┐
│  #14 Parity/Mod  │              │  #11 Existence   │
│  (Euclidean alg) │              │  (gcd = 1 claim) │
│                  │              │                  │
│  Reduce gcd via  │              │  Goal: prove gcd │
│  21n+4 - (14n+3) │              │  IS 1, i.e.      │
│  = 7n + 1        │              │  EXISTS no shared │
└────────┬─────────┘              │  prime divisor   │
         │                        └────────┬─────────┘
         ▼                                 │
┌──────────────────┐                       │
│ Second reduction │                       │
│ 14n+3 - 2(7n+1)  │                       │
│ = 1              │                       │
└────────┬─────────┘                       │
         │                                 │
         └────────────────┬────────────────┘
                          ▼
                  ┌────────────────┐
                  │  Convergence:  │
                  │  gcd = 1 forced │
                  │  for every n   │
                  └────────┬───────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Fraction in     │
                  │ lowest terms.   │
                  └─────────────────┘
```

The two archetypes are #14 (Parity/Modularity, here in the Euclidean-algorithm specialisation) and #11 (Existence, here in the *non-existence* specialisation: "no common prime divisor exists"). The convergence point is the discovery that the Euclidean reduction terminates at the unit; the convergence forces the conclusion.

Why did the designer pick *this* archetype pair? Consider the alternatives. The same conclusion could be approached via the **#14-only** route (treat $21n+4$ and $14n+3$ modulo $p$ for an arbitrary prime $p$ and prove $p \nmid 1$, which works but requires the prover to invoke an arbitrary $p$ and is rhetorically clunky). It could be approached via **#5 (Substitution)** by parametrising $n$ and substituting (which works but loses the elegance of the gcd-machinery). It could be approached via **#9 (Domain Constraints)** by bounding the possible common divisors (which works but is overkill for a divisor that turns out to be $1$). The designer's chosen pair (#14 + #11) is the *cleanest* convergence on the CEP, in the precise sense that the two archetypes share the smallest common machinery (the Euclidean algorithm) and the convergence happens *inside* the machinery itself, without requiring any external scaffolding.

This is the second design choice the designer made: among all archetype pairs that could close this problem, they engineered the surface so that exactly the #14 + #11 pair would be the natural attack.

### The Planted Traps

There are, by my count, three planted traps in this short problem. I will name each.

**Trap 1: the brute-search trap.** A naïve solver, presented with "$(21n+4)/(14n+3)$ in lowest terms for all $n$," can compute the fraction for $n = 1, 2, 3, \ldots, 100$ and observe that it is in lowest terms in every case. From this evidence they can confidently conjecture the result. They cannot prove it. The trap is that the brute-search provides apparent confirmation and *no path to a proof*; the solver who falls for this trap may write up the brute evidence as if it constituted a proof and lose marks.

This trap is *generous* in the sense Lockhart would recognise. The solver who falls in learns something: *empirical confirmation is not a proof in number theory.* The trap rewards the lesson.

**Trap 2: the factorisation trap.** A solver who has been trained to attack number-theory problems via factorisation will try to factor $21n + 4$ and $14n + 3$ as polynomials in $n$. They will discover, after some effort, that neither polynomial factors over the integers (both have leading coefficient that does not divide the constant). They will then try to factor as polynomials over $\mathbb{Q}$ or look for rational roots. They will find none. The trap is that factorisation, which is the standard first move for many number-theory problems, *does not apply here*, and the solver has to discover this by trying.

This trap is also generous: it teaches the solver that not every divisibility problem is a factorisation problem, and that the Euclidean algorithm is a tool independent of factorisation.

**Trap 3: the parametric trap.** A solver who has been trained in algebraic manipulation may try to *parametrise away $n$* by writing $21n + 4 = 7(3n) + 4$ and $14n + 3 = 7(2n) + 3$, hoping the factor of $7$ will somehow combine. They will find, after a few minutes, that the $7$-factorisation does not produce any useful divisibility — both quantities are coprime to $7$ for almost all $n$. The trap is that the surface structure of the bilinears suggests a $7$-based simplification that is real but irrelevant.

This trap, too, is generous. The solver who works through it learns to distinguish *cosmetic structure* (the visible factor of $7$ in the leading terms) from *operative structure* (the integer linear-combination that produces the gcd reduction).

Three traps in a two-sentence problem. Each trap is a lesson the designer planted, and the solver who works the problem fully — including the parts of the work that did not pan out — comes away having learned three things they did not know before. This is what generous problem design looks like at the Moderate tier.

### The Statement-Craft

We come to the most under-noticed of the four axes. The problem statement, in the IMO's official wording, is:

> Prove that, for every natural number $n$, the fraction $(21n+4)/(14n+3)$ is in lowest terms.

There are eighteen English words plus one mathematical expression. Every word does work; if I remove any of them the problem changes character. Consider:

- *"Prove that"* — the rhetorical posture. The problem-setter has chosen to ask for a proof rather than a counterexample-or-proof; this rules out the option that the fraction is sometimes *not* in lowest terms, which the solver might otherwise check.
- *"for every natural number $n$"* — the universal quantifier. The problem is over *all* $n$, not "for some $n$" or "for $n \in \{1, \ldots, 10\}$." The universal quantifier is the source of the demand for a proof.
- *"the fraction"* — the singular definite article. Not *"a fraction of the form"* or *"the fraction defined as."* The phrasing presupposes that the expression *is a fraction*, which implicitly tells the solver that the numerator and denominator are both nonzero (so the statement is meaningful for every $n$).
- *"in lowest terms"* — the asked-for property. This is the most consequential word-choice in the problem.

Let me dwell on the last point. The designer could have written *"prove that the numerator and denominator are coprime."* That is equivalent. The designer could have written *"prove that $\gcd(21n+4, 14n+3) = 1$."* That is equivalent. The designer could have written *"prove that the fraction cannot be simplified."* That is equivalent. They chose *"in lowest terms."*

Why? Because *"in lowest terms"* is the **schoolroom phrasing** for the same concept. It is the phrasing a student first encounters in Class VI, when they learn to reduce $6/8$ to $3/4$. By using the schoolroom phrasing rather than the technical phrasing ($\gcd = 1$ or *coprime*), the designer has performed two acts at once. First, they have made the problem statement maximally accessible — every student who has ever simplified a fraction understands what *in lowest terms* means. Second, they have *concealed* the technique. The student who sees *"prove that $\gcd = 1$"* immediately recognises that the Euclidean algorithm is relevant; the student who sees *"in lowest terms"* may not, and must rediscover the equivalence themselves. The statement-craft has, with a single word-choice, made the problem both more accessible *and* harder to solve mechanically. This is masterful.

There is also a smaller piece of statement-craft worth naming: the choice of the specific numerator and denominator. *"$(21n+4)/(14n+3)$"* — why these constants? Because the Euclidean reduction needs to close in exactly two steps for the proof to be three lines long, and the constants $21, 14, 4, 3$ are precisely the smallest positive integers for which this is true. The designer was not aiming for ugly large constants. They were not aiming for cosmetic prettiness either. They were aiming for the *minimum constants compatible with a two-step Euclidean closure*, and they found them.

The whole problem, every word and every constant, is a designed object. Eighteen words and four small integers carry inside them: a CEP (the two-step Euclidean closure), an archetype convergence (#14 + #11), three planted traps (brute search, factorisation, parametric), and statement-craft (the schoolroom phrasing, the minimum-constants choice). The watch is open. The mechanism is visible.

This is what every Pillar 4 case study from Chapter 4 onward will look like.

---

## §3 — The Counter-Argument

I want to face the strongest objection to what §2 has just done. The objection comes in two waves and I will take them in order.

**SIMPLICIO.** What you have done in §2 is *post-hoc rationalisation*. You have looked at a problem whose proof you already knew, and you have invented a designer's intent that produces it. The actual IMO problem-setters in 1958 (or whenever they selected this problem) did not sit down and think *"let us pick the minimum constants for a two-step Euclidean closure with three planted traps and schoolroom-register statement-craft."* They picked a problem they liked. Your analysis reads a structure into their choice that may not have been there.

**SALVIATI.** The objection is serious and partially correct. Let me concede the partial truth first. Yes — the designers of IMO 1959 Problem 1 almost certainly did not have, in their explicit working vocabulary, the four-axis anatomy I have just laid out. They had something else: *taste*. Taste is the working mathematician's name for accumulated tacit knowledge of all four axes operating simultaneously, without the practitioner having to name them. The IMO problem committees that have curated problems for sixty-five years have developed taste, and what they call *"a good problem"* is a problem whose four anatomical axes happen to fit well together.

The Pillar 4 anatomy is the *attempt to name* what taste already knows tacitly. It is the difference between a master carpenter who can tell good wood from bad by touch and the engineer who can describe wood quality in terms of grain density, moisture content, and ring uniformity. Both are right; the engineer's description is not the carpenter's process; but the engineer's description can be *taught*, and the carpenter's touch cannot, except by long apprenticeship. Pillar 4 chooses the engineer's path because it chooses to be teachable.

So when I say *"the designer made the following four choices,"* what I more precisely mean is: *"the problem we are looking at exhibits four properties that the designer's taste produced, and we will reverse-engineer each property by asking what choice would have produced it."* The reverse-engineering is honest in the same way that biology's reverse-engineering of evolution is honest: nobody claims evolution had explicit *intent*, but it is still meaningful to ask what selective pressure produced any given trait. Design analysis in this pillar is analogous.

**SIMPLICIO.** Then the second wave of the objection. Suppose I grant you that the four-axis anatomy is a useful reading of the problem. What does it actually let me *do* that I could not do without it?

**SALVIATI.** Three things, each more consequential than the last. First, it lets you *read* every future problem with the four-axis instrument in hand, which means you spend less time disoriented and more time oriented. Second, it lets you *evaluate* other problems you encounter — saying things like "this case has a fuzzy CEP" or "this case's traps are punishing rather than generous" — which is the beginning of mathematical taste in the way the IMO committee's taste is taste. Third, it lets you *design*. Chapter 3 turns the four-axis anatomy into a five-step design framework. Chapter 9 puts the framework in your hands. None of those subsequent moves are possible without the anatomy first.

**SIMPLICIO.** Then proceed.

---

## §4 — Bridge to Chapter 3

In Chapter 1 we made the claim, repeatedly: a problem is a designed object. In this chapter we have installed the analytical instrument that makes the claim operational: every designed problem has four nameable anatomical axes (CEP, archetype convergence, planted traps, statement-craft), and these four axes are sufficient to give a complete reading of any designed problem we will encounter in the rest of the pillar.

What we do not yet have is the *constructive* counterpart of the anatomy. We can dissect a designed problem; we have not yet learned to design one.

Chapter 3 closes that gap. It inverts the four-axis anatomy into a five-step *design framework* — the inversion of Polya's four-phase solver-loop into a five-step designer-loop, with one extra step at the end for the work that the designer (and not the solver) must do. The framework gives the reader a named procedure: select a CEP, choose archetypes, design the convergence, plant the traps, craft the statement. Chapter 3 walks the procedure through a single author-designed problem in real time, so that the reader can watch the framework operate.

By the end of Chapter 3 the reader has the anatomy (Chapter 2) *and* the procedure (Chapter 3). The case-study chapters that follow (4 through 8) will apply the anatomy retrospectively to twenty-five real designed problems. The exercise chapter that closes the pillar (Chapter 9) will apply the procedure prospectively to three new designs of the reader's own.

We turn now to the procedure.

---

*End of Chapter 2.*
