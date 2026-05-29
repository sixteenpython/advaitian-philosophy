---
chapter: 1
pillar: 1
chapter_type: essay
title: "The Six-Point Framework"
subtitle: "The Grammar of Mathematical Insight"
length_target_words: 7000
actual_words: 6200
canonical_takeaway: "A solution reports an answer; a commentary teaches a way of seeing — and the six points are its grammar."
status: locked
last_revised: 2026-05-29
locked_on: 2026-05-29
lock_note: "Content, structure, and prose locked by Anand. Back-tested against all knowledge_base/ + my_references/ docs; three back-test corrections accepted. Length ~6,200 words accepted as final (under the 7,000 target by choice)."
sections: 7
running_example: "polygon-with-AP-angles (interior angles in AP, smallest 120°, common difference 5°, find n)"
references_invoked: [ThinkMath-Blueprint-v3, Advaitian-Master-Framework, Masterclass-Problem-Solving, Advaitian-Philosophy-Framework, why_this_book-positioning, Lockhart-Lament-Part-I, Polya-How-To-Solve-It-inscribed-square, Joshi-EJM-Ch1-JEE1989, Pillar-2-Ch-1-WE1, Pillar-3-multidirectional, Pillar-4-CEP-design]
back_tested: "2026-05-29 against all knowledge_base/ docs + my_references/ docs; corrected Pólya locus (vertex not apex) + polygon takeaway to gold-standard 'Geometry selects the winner'; §1 positioning enriched to canonical trichotomy"
voice_register: "§1 Lockhart-polemic 'I'; §2–§6 'we'; §7 hybrid"
developmental_tiers: "0–4 (per Blueprint §5.8 / ThinkMath v3 §3)"
---

# Pillar 1 — The Six-Point Framework

> *A solution reports an answer. A commentary teaches a way of seeing.*

---

## §1 — The Problem with Problem-Solving Books

I have spent a large part of my life reading books that promise to teach problem-solving, and I have come to believe that almost all of them fail in one of two opposite ways.

The first kind is the technique manual. It is thick, it is well-organised, and it is honest about what it is: a catalogue of methods. Here is the chapter on quadratics. Here is the chapter on coordinate geometry. Here are four hundred problems, sorted by topic, each solved in the cleanest possible way. A diligent student works through it and emerges able to recognise that *this* problem is a "type-7 conic problem" and *that* one is a "type-3 inequality." The book has taught a vocabulary of recipes. What it has not taught — what it cannot teach, because its very structure forbids the question — is *why* a particular recipe was reached for, what the solver saw in the first thirty seconds that told them which drawer to open. The insight, the only thing worth having, is precisely what gets edited out of a clean solution. The recipe survives; the seeing is lost.

The second kind is the philosophy book. It is thin, it is beautifully written, and it talks *about* problem-solving with great warmth. It tells you to "understand the problem," to "look for a related problem," to "check your result." It is full of wisdom, and I do not mock it — some of it I love. But read forty pages and you notice that almost no mathematics is actually *done*. The advice floats one level above the page. "Look for a pattern" is true and useless in exactly the way that "buy low, sell high" is true and useless. The book gestures at the mountain without ever putting your hands on the rock.

There is a third kind, the best of the three, which I will call the culture book. It is written by a genuine problem-solver who lets you sit beside them while they think — describing the habits of mind, the willingness to play, the taste for a good problem. It conveys, better than anything else, *what it feels like* to solve. And yet it too stops short of the thing I most want, because it describes the practice without ever *enumerating* it. It shows you a master at work but does not hand you the finite list of moves the mastery is made of, and so you finish it inspired but not equipped — you know that good solvers do something, without being told exactly what the somethings are, named one by one, so you could check them off.

So the student is offered a poor menu. Learn *what* to do without ever learning *how to see*; or hear about *how to see* without ever watching it happen on a real problem, in full, with the wrong turns left in; or feel the texture of mastery without being given its parts. In each case the *system* — the finite, nameable structure of mathematical insight — goes untaught, because each kind of book has quietly assumed there is no such system to teach.

This book makes the opposite bet. Its wager — and it is a bold one, bold enough to be wrong — is that the practice of mathematical problem-solving *has a grammar*: a finite set of structural primitives that can be enumerated, named, taught, and used both to decode a problem and to compose one. No book in the canon has made that claim outright. This is the first attempt to make the implicit grammar of competitive mathematics explicit, comprehensive, and teachable. And the instrument that carries the claim is a single object: a **commentary** — a structured account of a solved problem that records not just the answer but the *act of understanding* that produced it. A commentary, like any disciplined form of speech, needs a grammar of its own: a fixed set of parts, in a fixed order, each doing a job the others cannot. That grammar is the six-point framework, and this chapter is its definition.

I will make you one promise and ask one thing in return. The promise: if you give this book sustained attention, you will not leave with a longer list of tricks. You will leave with a different way of looking at a problem before you touch it — a habit of asking *what is this really about?* before asking *what do I compute?* The thing I ask in return is patience with the next few pages, where I take a problem you could already solve and slow it down until the framework becomes visible. The point will not be the answer. You will have the answer in a line. The point will be to watch the seeing happen, and to name each of its moves, so that you can perform them on purpose ever after.

---

## §2 — What a Commentary Is, and Why You Need a Grammar

There is an old intellectual tradition, native to this part of the world, that knew something modern textbooks have forgotten: that the deepest teaching is not the text but the *commentary on the text*. In the Indian scholarly lineage a root text — a *sūtra* — is terse to the point of obscurity, a string of compressed aphorisms. What makes it teachable is the **bhāṣya**, the commentary: a second voice that unfolds the compression, supplies the missing steps, names the moves, and connects the local claim to the whole edifice of knowledge. The sūtra states. The bhāṣya *explains how one could have arrived at the statement*, and why it matters, and where else it reaches. For two thousand years the commentary, not the root text, was where the learning lived.

A mathematical solution is a sūtra. It is correct, compressed, and — by itself — almost unteachable. "Let $x$ be the excluded digit; since $0+1+\cdots+5=15$ is divisible by $3$, the number is divisible by $3$ iff $x\in\{0,3\}$." Every symbol is right. And a student who could not have produced that line learns nothing from reading it, because the line conceals the one thing they needed: the moment someone decided to think about the *digit sum* rather than the number itself. A solution answers the question "*is this correct?*" A commentary answers the question "*how could I have seen this, and what does seeing it teach me about every problem like it?*"

That is what a commentary is: the bhāṣya of a solved problem. It is not a longer solution. A longer solution is just a sūtra with more words. A commentary is a different kind of object — it takes the finished solution as raw material and reconstructs the *intellectual event* that produced it, with the structure exposed.

Now, why a *grammar*? Why not simply write a thoughtful essay about each problem and let its shape follow the problem's mood?

Because a language without grammar is not a language; it is noise that occasionally means something. Grammar is what makes an utterance *transferable* — what lets a sentence you have never heard before be understood the moment it is spoken, because its parts occupy known roles. The same is true of mathematical insight. If every commentary had its own private shape, you could admire each one but you could not *learn the form*, because there would be no form to learn. By fixing the parts and their order, a grammar does three things at once. It makes commentaries **comparable** — you can see that the pivot in this geometry problem plays the same role as the pivot in that number-theory problem, though the mathematics is unrelated. It makes them **diagnosable** — when your own solving fails, you can ask *which part of the grammar did I skip?* And it makes the act of insight **repeatable**, because a habit with named steps is a habit you can rehearse, where a vague intention to "think well" is not.

The grammar has exactly six parts, and they come in this order, every time:

1. **SEED** — one sentence naming the underlying structural archetype. Domain-general, reusable. It says what the problem *is*, beneath its costume.
2. **BRUTE PATH** — the mechanical approach a competent student would naturally try, carried far enough to show exactly where it goes blind or expensive. Never mocked; the brute path is not wrong, only costly.
3. **ELEGANT PIVOT** — the insight that collapses the brute path. Named explicitly, with the mathematics shown in full. It should feel surprising before, inevitable after.
4. **PITFALLS** — three to five named cognitive traps, each with a memorable name, the thinking error it encodes, why it tempts, and a concrete check that defeats it.
5. **CONNECTIONS** — three mandatory sub-parts: where this archetype appears elsewhere in mathematics; what *other* structural approaches solve the same problem; and where the same structure shows up outside mathematics entirely.
6. **TAKEAWAY** — one sentence, under fifteen words, that a student can quote five years later.

Read that list again and notice what it is not. It is not "understand–plan–execute–review." It is not a procedure for *getting* the answer. It is a structure for *holding* the understanding once you have it, so that the understanding can be inspected, compared, and taught.

And the order is not decorative; each point depends on the ones before it. You cannot write an honest **brute path** until you have named the **seed**, because without knowing what the problem *is* you cannot say which mechanical attempt is the *natural* one to try. You cannot appreciate the **elegant pivot** until you have felt the brute path go blind, because a pivot is defined by what it rescues you from — shown a slick step with no sense of the labour it replaces, a student files it as one more trick rather than as a genuine collapse of difficulty. The **pitfalls** are meaningful only against the pivot, since most traps are precisely the ways a solver *fails to reach* the pivot or *misapplies* it. The **connections** require the pivot to be named first, because you connect a problem to others through the *structure* the pivot exposed, not through its surface. And the **takeaway** can only be written last, because it is the compression of everything above it into a sentence — write it first and you have a slogan; write it last and you have a hard-won principle. The six points are therefore not six independent boxes to fill. They are a single argument that unfolds in one direction, and reading them in order is reading the anatomy of an insight from its first glimmer to its portable residue.

The rest of this chapter earns that order: we will walk a single problem through all six parts, slowly, naming each move as it happens.

---

## §3 — The Six Points: A Walking Tour Through One Problem

Here is the problem we will use. It is deliberately modest — a strong student will solve it in under five minutes — because our subject is not the problem but the *grammar*, and you cannot watch the grammar work if you are busy struggling with the mathematics.

> **The interior angles of a convex polygon are in arithmetic progression. The smallest angle is $120°$ and the common difference is $5°$. How many sides does the polygon have?**

Solve it now, if you like, before reading on. Then watch us put the six points on it.

### 🌱 SEED

> *This is an **Invariance** problem (Archetype #1) gated by a **Domain Constraint** (Archetype #9): the angle sum of an $n$-gon is fixed, and convexity caps every angle below $180°$.*

That single sentence is the seed, and notice how much it already decides. It does not mention arithmetic progressions or the number $120$. It names two structural forces — a conserved quantity and a boundary condition — and asserts that the whole problem is their interaction. Everything that follows is the working-out of this sentence. The seed is domain-general: the very same pair, "a conserved total filtered by a reality bound," governs problems about projectile flight times, probabilities, and resource allocation that have nothing to do with polygons. To state the seed *first*, before any algebra, is the discipline the entire book is built to instil.

### ⚙️ BRUTE PATH

What does a capable, untrained student do? They reach, reasonably, for the angle-sum formula and start computing. The interior angles are an arithmetic progression with first term $120$ and common difference $5$, so the $n$ angles are
$$120,\;125,\;130,\;\dots,\;120+5(n-1).$$
Their sum, by the AP formula, is
$$S=\frac{n}{2}\Big[2(120)+(n-1)5\Big]=\frac{n}{2}\big[235+5n\big].$$
And the interior angles of any $n$-gon must sum to $(n-2)\cdot 180$. Setting the two equal:
$$\frac{n}{2}(235+5n)=(n-2)180.$$
This is honest work, and it is *not the brute path's failure*. The brute path fails one step later — at the moment the algebra hands back its answer. Multiply out:
$$235n+5n^{2}=360n-720\;\Longrightarrow\;5n^{2}-125n+720=0\;\Longrightarrow\;n^{2}-25n+144=0,$$
which factors as $(n-9)(n-16)=0$, giving $n=9$ **or** $n=16$. The brute path, run to its natural end, reports *two* answers and falls silent. A student in an exam, having done all the algebra correctly, now writes "$n=9$ or $16$" and moves on — and loses the marks. The path did not break because the algebra was wrong. It broke because algebra does not know what the word *convex* means.

### 💡 ELEGANT PIVOT

Here is the pivot, and it is exactly the seed's second half coming due. **Algebra generates candidates; Geometry selects the winner.** The equation cannot distinguish a real polygon from an impossible one because it never encoded convexity. We encode it now. In a convex polygon every interior angle is strictly less than $180°$. The *largest* angle is the last term of the AP, $120+5(n-1)$, so the binding condition is
$$120+5(n-1)<180\;\Longleftrightarrow\;5(n-1)<60\;\Longleftrightarrow\;n<13.$$
Now lay the two candidates against this filter. For $n=16$ the largest angle would be $120+5(15)=195°$ — a reflex angle, geometrically impossible in a convex polygon; **rejected**. For $n=9$ the largest angle is $120+5(8)=160°<180°$; **accepted**. The answer is $n=9$, and not because we computed more carefully — because we asked the *domain* a question the algebra could not. That is the elegant pivot: the second root was never a rival answer at all, it was the algebra's blindness made visible, and one line of geometric reality dissolves it.

### ⚠️ PITFALLS

- **The Double-Root Trap.** You solve the quadratic, get two roots, and report both — or pick one at random. *Why it tempts:* the algebra feels finished, and two roots look like two answers. *The check:* whenever a quadratic appears inside a word problem, treat its roots as *candidates*, never as *answers*, until each has been tested against the problem's physical or geometric meaning.
- **The Algebraic Trust Trap.** You believe the equation knows everything the problem knows. *Why it tempts:* the algebra was hard-won and correct, so surrendering to it feels like rigour. *The check:* before reporting, name one fact in the problem statement (here, "convex") that your equations never contain — then go enforce it.
- **The Seed-Skipping Trap.** You write the angle-sum formula before naming what the problem *is*. *Why it tempts:* computing feels like progress; pausing feels like delay. *The check:* require one sentence of seed — "this is a conserved-total problem with a reality bound" — before the first equation. The bound you name now is the filter you will need later.
- **The Constraint-Ignorance Trap.** You never ask which condition is *binding*. *Why it tempts:* a polygon has many angles and many conditions; it is easier to check none. *The check:* identify the extremal element (here the *largest* angle) — domain violations always strike there first.

### 🔗 CONNECTIONS

**(A) Where this archetype appears elsewhere.** The "conserved total, then filter" pattern recurs constantly. A projectile's time-of-flight equation is a quadratic in $t$ whose negative root is discarded because time cannot run backward. A probability computed from a generating function is rejected if it exceeds $1$. The number of five-digit numbers divisible by three (Pillar 2, Chapter 1) turns on a digit-sum *invariant* whose candidates are then filtered by a *leading-zero* domain constraint — the very same two-archetype skeleton as this polygon.

**(B) Other structural approaches to the same problem.** One could avoid the quadratic entirely by an *averaging* argument: the angles form an AP, so their mean is the middle angle, and the mean interior angle of an $n$-gon is $\frac{(n-2)180}{n}$; equate and solve. One could also argue from the *exterior* angles, which sum to $360°$ and form an AP with common difference $-5°$ — a cleaner space in which the convexity condition becomes "all exterior angles positive." Each route reaches $n=9$; the convexity filter is unavoidable in all of them, which is the surest sign it is the problem's true heart.

**(C) The same structure outside mathematics.** "Generate candidates by an exact rule, then prune by a reality bound" is the shape of natural selection (mutation proposes; the environment disposes), of engineering tolerance analysis (the formula gives a dimension; the material's strength caps it), and of legal reasoning (the statute admits several readings; precedent and context select one). The polygon is a toy; the move is civilisational.

### 🏆 TAKEAWAY

> *Algebra generates candidates; Geometry selects the winner.*

Seven words. A student who carries only that sentence out of this section, and reaches for it every time a quadratic falls out of a word problem, has acquired more than the answer to one polygon problem. They have acquired the reflex the whole book exists to build. That is the entire purpose of the sixth point: not to summarise, but to *compress the insight into something portable.*

---

## §4 — The MVC Protocol: Thinking Before Writing

The six points are the finished commentary — the gold standard, publication-ready, the bhāṣya in full dress. But you do not begin there, any more than a writer begins with the printed book. Before the full commentary comes a smaller, faster, private act of thought that the doctrine calls the **MVC**: the *Minimum Viable Commentary*. It is sixty seconds of pure structural thinking, no equations, no formalism, just four sentences:

> *The seed here is **[X]**. Most students will try **[brute path]** because **[Y]**. The key insight is **[Z]**. The constraint that prunes everything is **[W]**.*

An MVC is **valid** when three things are present: the seed is named, the brute trap is visible, and the pivot is at least gestured at. That is all. It need not be rigorous; it is not for the page; it is the structural skeleton you build *in your head before you write a single symbol*, so that every symbol you then write has a known destination.

Watch it on our polygon. Sixty seconds, out loud:

> *The seed is a fixed angle sum (Invariance) gated by convexity (Domain Constraints). Most students will set up the AP sum equal to $(n-2)180$ and solve the quadratic, because that is the obvious machinery and it works right up to the last step. The key insight is that the quadratic gives two roots and only the geometry can choose between them. The constraint that prunes everything is "every interior angle below $180°$" — which kills $n=16$ and leaves $n=9$.*

Notice what just happened. Before writing one equation, we already knew the problem would produce two candidates, knew which idea would resolve them, and knew which single condition would do the resolving. The subsequent algebra was no longer a search — it was *transcription* of a route already mapped. That is the entire value of the MVC: it converts solving from groping in the dark into walking a path you have already seen by torchlight.

Contrast this with the alternative, which every one of us has practised and which the discipline is designed to kill: *"I'll figure it out as I go."* The figure-it-out-as-you-go solver sets up the quadratic with no idea that two roots are coming, is mildly surprised when they arrive, and — having budgeted no thought for the resolution — grabs one or reports both. They did not *fail to know* about convexity; they failed to *think about the shape of the problem before entering it*, and so the convexity condition arrived as an interruption rather than as the expected final move. The MVC is nothing more than the refusal to enter a problem blind. It is cheap — sixty seconds — and it is the single highest-leverage habit in this book. Stage 1 is the MVC. Stage 2 is the six-point commentary. You earn the right to Stage 2 by passing Stage 1; and in an examination, where there is no time for Stage 2, the MVC *is* the solution's spine, and the marks follow it.

---

## §5 — The Developmental Tiers: How the Grammar Scales

A natural objection arises here. *If every commentary has six points, will a nine-year-old and an IMO contestant receive the same six paragraphs?* They will not — and the way the framework bends without breaking is the subject of this section.

The key idea is that the six points are a *grammar*, and grammar scales by **density**, not by structure. An English sentence spoken to a child and an English sentence written in a treatise obey the same grammar; what differs is the elaboration each part carries. So with the six points. We describe five **developmental tiers** — and the word is chosen carefully: a tier is a stage of the *reader*, not a difficulty of the *problem*. The same polygon problem can be commented on at any tier; what changes is how much each of the six points unfolds.

- **Tier 0 — the narrative stage (roughly ages 6–9).** Abstraction is premature; the child must *feel* mathematics before thinking it. The six points are still present but wear costumes. The seed is not "Invariance" but "*what stayed the same even when everything moved?*" There is no algebra to call a brute path; there is a story. The commentary is a *story recap*: "you found that even when the angles changed, the total stayed locked — mathematicians have a word for things that don't change, they call it an *invariant*; remember that word." All six points are there in spirit; each is expanded into many gentle sentences.
- **Tier 1 — the relationship stage (roughly ages 10–13).** Mathematics becomes a balance of forces; the equals sign becomes a scale that refuses to tip. The seed is named through behaviour — "*what is the rule that never breaks here?*" — and Duality enters as "*what is the reverse question?*" Six points present, three to five sentences each.
- **Tier 2 — the abstract stage (roughly ages 14–16).** Variables arrive — "compressed reality," not mystery — and with them the great danger of this tier, *formula blindness*: reciting a technique with no grasp of the structure beneath it. Here we begin naming archetypes directly, and Domain Constraints (#9) becomes critical: "*does the universe accept this answer?*" The polygon's convexity filter is exactly a Tier-2 lesson. Six points present, terser, two to four sentences each.
- **Tier 3 — the multi-archetype stage.** The student holds two or three archetypes at once and looks for their convergence. Our polygon is a *Tier-3-baseline* problem precisely because it is two archetypes (Invariance × Domain Constraints) that must be held together. The six points may compress to four or five, with the weight shifting onto the pivot and the convergence.
- **Tier 4 — the designer stage.** The student no longer only solves problems; they reverse-engineer them, seeing the *Central Elegant Point* a problem was built around. Here the six points are not the output but the *analytic skeleton*; the analysis exceeds them, as in the Pillar 4 case studies where a single IMO problem is dissected as a designed object.

To make "density" concrete rather than abstract, here is *the same polygon problem* commented at two distant tiers. Read them back to back and watch the grammar hold while the elaboration swells.

**The polygon at Tier 1 (a single paragraph).**

> *Here is a shape whose corner-angles climb by a fixed step — $120°$, then $125°$, then $130°$, and so on. The thing that never changes is the total: a many-sided shape's angles always add up to a fixed amount once you know how many sides there are. So one rule says what the angles add to, and another rule — the shape has to be "nice," with no corner caving inward past a straight line — throws out the answers that don't make a real shape. Two rules, pulling together: one decides what's possible, the other decides what's allowed. The shape has $9$ sides. Notice how the "must look like a real shape" rule did the deciding at the end.*

That is all six points in miniature — seed ("the total never changes"), brute sense ("one rule says what they add to"), pivot ("another rule throws out the bad answers"), pitfall ("answers that don't make a real shape"), connection ("two rules pulling together"), takeaway ("the *real-shape* rule did the deciding") — compressed into one warm paragraph, with no algebra and no archetype names. A ten-year-old can hold it.

**The polygon at Tier 4 (an analytic skeleton the analysis then exceeds).**

> *Read as a designed object, this problem's Central Elegant Point is the extraneous root. The author has chosen an arithmetic progression of angles precisely so that the angle-sum invariant produces a **quadratic** in $n$ — and then tuned the first term and common difference so that the quadratic factors over the integers into two positive roots, $n=9$ and $n=16$, exactly one of which survives the convexity ceiling. The whole problem is an instrument for delivering one lesson: that the algebraic model (the quadratic) is strictly larger than the geometric reality (convex polygons), and the gap between them is a phantom root. A designer who understands this can dial the difficulty at will — widen the common difference and the surviving root changes; choose a difference that makes the largest angle exactly $180°$ and the problem becomes a borderline-case study in strict versus non-strict inequality; replace "convex" with "simple" and the filter loosens, admitting reflex angles and changing the answer. The six points here are not a report; they are the **coordinates** along which the problem can be redesigned.*

Two commentaries, one a paragraph and one a page, on a single problem — and the same six bones beneath both. That is what it means for a grammar to scale by density: the structure is invariant; only its elaboration grows with the reader.

The book you are holding lives mostly in **Tiers 3 and 4**. Tier 1 is its gentlest on-ramp (the warm-up problems opening each Pillar 2 chapter); Tier 4 is its summit (the hardest Pillar 4 case studies). But the philosophy is identical at every tier. The seven-year-old who notices that the bricks did not vanish — they only moved — has understood Invariance as deeply, *for their stage*, as the seventeen-year-old who filters a quadratic's roots through convexity. The language scales. The seeing does not change.

This is why the framework is worth learning once, properly. You are not memorising a format for one kind of problem at one level of difficulty. You are acquiring a grammar that will describe a child's first encounter with subtraction and a contestant's last hour on an Olympiad problem, in the same six words.

---

## §6 — Reading the Masters Through the Six Points

If the six-point grammar were merely our invention — a template we impose from outside — it would be a convenience and nothing more. The strong claim of this chapter is larger: that the grammar *describes the structure good mathematical commentary has always had*, whether or not its author knew the names. To test that claim, we read two solutions written entirely without knowledge of this framework — one by George Pólya, one from the JEE tradition via K. D. Joshi — and watch the six points fit them like a glove.

### Pólya's inscribed square

In *How to Solve It*, Pólya poses a construction problem: **inscribe a square in a given triangle, with two vertices on the base and one vertex on each of the other two sides.** His solution is famous, and it is famous *because of its pivot* — though Pólya does not use the word.

Read through the grammar, his solution decomposes exactly:

- **SEED.** This is a *Degrees-of-Freedom* problem (Archetype #17): the square is over-constrained as stated — four conditions on four vertices — so Pólya's move is to *relax one condition* and study the family that remains.
- **BRUTE PATH.** Try to place all four vertices at once — pick a side length, draw the square, check whether all four conditions hold, adjust, repeat. This trial-and-error never terminates cleanly because you are solving for the whole square in one shot.
- **ELEGANT PIVOT.** Pólya's celebrated insight: *keep all conditions but one.* Drop the requirement that the fourth vertex lie on the far side. Now squares with two vertices on the base and a third vertex on one side form a *one-parameter family* of growing squares — and as the square scales up, the freed fourth vertex traces a straight line through the triangle's vertex from which the family emanates. The square we want is the one where that line meets the remaining side; that intersection fixes the size in a single stroke, finishing a problem that brute trial-and-error could not.
- **PITFALLS.** The *all-at-once trap* (refusing to relax any condition); the *wrong-vertex-to-free trap* (relaxing a condition that does not produce a clean locus).
- **CONNECTIONS.** The "relax one constraint, recover it as a locus" move is the engine of countless construction and locus problems; it is structurally the same as parametrising a family and intersecting — the method behind much of analytic geometry.
- **TAKEAWAY.** *When a problem is over-constrained, drop one condition and see what the rest are free to do.*

Pólya called this heuristic "vary the problem." We call its first point a seed and its third an elegant pivot. The mathematics is his; the grammar was waiting underneath it all along.

### Joshi's JEE 1989 five-digit problem

Now a problem from the Indian examination tradition, treated in Joshi's *Educative JEE Mathematics* and in our own Pillar 2, Chapter 1:

> **How many five-digit numbers, divisible by three, can be formed using each of the digits $0,1,2,3,4,5$ exactly once?**

Through the grammar:

- **SEED.** An *Invariance* problem (#1): divisibility by three is governed by an invariant of the digits — their sum — not by the number itself.
- **BRUTE PATH.** Form five-digit numbers and test each for divisibility. There are on the order of $5!\cdot 5 = 600$ candidates; filtering them one at a time is hopeless.
- **ELEGANT PIVOT.** A number is divisible by three iff its *digit sum* is. The full set $\{0,1,2,3,4,5\}$ sums to $15$, already divisible by three. Choosing five of the six digits means *excluding one*; the remaining sum stays divisible by three iff the excluded digit is itself a multiple of three — that is, $0$ or $3$. The problem collapses to two clean cases before a single arrangement is counted.
- **PITFALLS.** The *enumerate-everything trap* (counting before finding the invariant); and — when counting case "exclude $3$" — the *leading-zero trap*, since strings beginning with $0$ are not five-digit numbers. That second trap is itself a *Domain Constraint* (#9): the invariant produces candidates, and the leading-zero rule filters them. The same two-archetype skeleton as the polygon.
- **CONNECTIONS.** Digit-sum invariants drive an entire family of divisibility problems; the "fix the total, choose what to exclude" move recurs across combinatorics; and complementary counting (subtract the leading-zero cases) is a general principle reaching far beyond this problem.
- **TAKEAWAY.** *Do not test the objects; find the invariant that classifies them.*

Two solutions, separated by half a century and an ocean, neither written with our framework in mind — and both fall, without forcing, into the same six parts. That is the evidence for the strong claim. The six points are not a template we press onto mathematics from outside. They are the skeleton that competent mathematical commentary has always had inside it. This book's only innovation is to make the skeleton visible, name its bones, and teach you to build with it on purpose.

---

## §7 — Self-Diagnosis: Which Points Come Naturally, and Which Are Your Blind Spots?

You now have the grammar. The last question is personal: *which of its six points do you already perform by instinct, and which do you habitually skip?* Almost every solver is strong at some points and blind at others, and your blind points are precisely where your marks and your insights leak away. What follows is a short self-audit. Answer honestly — for yourself, not for a grader. For each statement, mark *usually true*, *sometimes true*, or *rarely true* of your own solving.

1. **(Seed)** Before writing any equation, I can state in one sentence what the problem is *structurally about*.
2. **(Seed)** When I meet a new problem, I try to recognise which *type of structure* it shares with problems I have seen, rather than which formula it needs.
3. **(Brute path)** I can tell, fairly early, that the obvious approach will become expensive — and I notice this *before* I am buried in algebra.
4. **(Brute path)** When a method stalls, I can say precisely *where* and *why* it went blind, rather than just feeling stuck.
5. **(Elegant pivot)** I actively look for the one insight that would collapse the work, instead of pushing the first method through by force.
6. **(Elegant pivot)** When I find a slick step, I can name *what kind of move* it was (a substitution, an invariant, a symmetry, a domain filter).
7. **(Pitfalls)** After getting an answer, I check it against the problem's *physical or geometric meaning*, not only its algebra.
8. **(Pitfalls)** When a quadratic or other multi-valued step appears, I treat its outputs as *candidates to be filtered*, never as finished answers.
9. **(Connections)** Having solved a problem, I can name another, unrelated problem that uses the *same structure*.
10. **(Connections)** I can sometimes see the same structural idea appearing *outside mathematics* — in physics, in argument, in design.
11. **(Takeaway)** After solving, I can compress what I learned into a single memorable sentence I would still recall months later.
12. **(MVC / discipline)** Before committing pen to paper, I run a quick mental sketch — seed, likely trap, key idea — rather than figuring it out as I go.

Now read your own pattern. If your *rarely true* answers cluster on questions **1–2**, you are a strong calculator with a weak seed habit — you compute before you see, and this book's Pillar 2 (the archetypes) is your gymnasium. If they cluster on **3–6**, you commit to first methods and miss pivots — Pillar 3 (multidirectional solving) is built for exactly this. If they cluster on **7–8**, you trust algebra past the point of safety — return to §3's pitfalls and make the domain-filter check a reflex. If on **9–11**, you solve but do not *consolidate* — you are leaving the transferable lesson on the table, and Pillar 5 (the gems) will give you the named tools to connect with. And if your weakest answer is **12**, begin there, because the MVC habit is the cheapest and most powerful of all: it costs sixty seconds and it changes everything downstream.

This is the use of the framework as a mirror. It does not grade you; it *locates* you — it tells you which of the six moves your mind already makes and which it must be trained to make. The rest of this book is that training. Every worked example in every pillar that follows is written in these six points, deliberately, so that by the time you have read a hundred of them the grammar will no longer feel like an imposed format. It will feel like what it is: the natural shape of seeing a problem clearly. You will have stopped reading commentaries and started, without noticing the moment it happened, to *think* in them.

> *Name the seed before you compute; let the domain choose among what the algebra proposes.*

🌑
