---
chapter: 1
archetype: Invariance
subtitle: "If Something Stays Constant, Make It Your Anchor"
category: Structure Recognition (Archetypes 1–4)
related_archetypes: [2, 9, 12, 17]
key_gems: []
canonical_takeaway: "Track the invariant; let everything else move."
status: approved
last_revised: 2026-05-26
approved_on: 2026-05-26
sourcing_note: "All worked examples and practice problems in this chapter are drawn from K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), or from JEE / RMO / INMO examinations commented on in that text. See Blueprint §6.2 for the sourcing rule."
---

# Chapter 1 — Invariance

## *If Something Stays Constant, Make It Your Anchor*

---

## Opening Vignette

A juggler tosses five balls. At any moment some are in flight and some are in his hands; the count in the air shifts from two to three to four and back to one, faster than the eye can track. The hands themselves move in patterns that defeat description. And yet a small child watching the performance can answer one question without hesitation. *How many balls are there?* Five. Always five. No matter the configuration, no matter how complex the choreography, this single quantity is a fixed point in the visible chaos.

This is *Invariance*.

Now consider an entirely different scene. A student is computing the determinant of a $3 \times 3$ matrix and is told that a friend has been simplifying the rows. Row 2 has been replaced by Row 2 minus three times Row 1. Row 3 has been swapped with Row 1, multiplied by four, and then had Row 2 added to it twice. The numerical entries of the matrix are now nothing like what they were a moment ago. Surely, the student thinks, the determinant has changed beyond recognition.

The determinant has not changed beyond recognition. Under one of these row operations — adding a multiple of one row to another — it has not changed at all. Under the row swap, it has changed only its sign. Under multiplying a row by a constant, it has scaled by exactly that constant. The wild surface activity is governed by a small handful of laws: the determinant transforms in a strictly predictable way under each operation, and is *conserved* under the most common one. The student who recognizes this stops calculating the new determinant from scratch. They calculate the old one — by Gaussian elimination, perhaps — and read off the answer.

These two scenes look unrelated. A circus, a textbook. They share a deep architecture. In each, a system contains many moving parts, and an inexperienced observer is tempted to track every motion. Yet hidden in each system is a quantity that *does not move* — or moves only in the simplest possible way under the operations being performed. Anchor on that quantity, express everything else in terms of it, and the difficulty often dissolves.

In this chapter we will name this strategy formally. We will see that a remarkable range of mathematics — from the roots of polynomials to the conservation laws of closed physical systems, from coloring arguments in combinatorics to the Euler characteristic of surfaces — rests on the same single insight.

> *In every problem, certain things change and certain things do not. The invariant is what stays fixed, and it is almost always the key to the solution.*

---

## 1. The Archetype Defined

### 1.1 Formal Definition

We make the intuition precise. Let $X$ be a set — for instance, the configurations of a juggling pattern, the pairs of integers $(a, b)$, or the matrices of a fixed size — and let $G$ be a group acting on $X$. The *action* of $G$ on $X$ is the rule that tells us how each element of $G$ transforms an element of $X$. We write the action as $g \cdot x$, where $g \in G$ and $x \in X$.

\begin{definition}[Invariant]
A function $Q : X \to \mathbb{R}$ is called an *invariant* of the action of $G$ on $X$ if
\[
  Q(g \cdot x) \;=\; Q(x) \qquad \text{for every } g \in G \text{ and every } x \in X.
\]
\end{definition}

Three points are worth unpacking. First, *invariance is always relative to a group of transformations.* A quantity may be invariant under one group and wildly non-invariant under another. The area of a circle is invariant under the group of rigid motions of the plane (translations and rotations) but scales by $r^2$ under the multiplicative group of dilations. There is no such thing as an "absolute" invariant; one must always specify *under what*.

Second, the function $Q$ need not return a number. We allow $Q$ to take values in any set whose elements can be compared for equality. The *parity* of a permutation is an invariant under decomposition into transpositions, taking values in $\{+1, -1\}$. The *Euler characteristic* of a polyhedron is an integer invariant under continuous deformations of the surface. The *isomorphism class* of a vector bundle is an invariant under change of trivialization. Each is an invariant in the sense above.

Third, in problem-solving practice we rarely begin with an explicit group $G$ written on the page. More often we are handed a system that *evolves* under some described operation, and we must *find* the quantity that does not move. Naming the invariant is often the entire problem.

In this chapter we will encounter four characteristic forms of mathematical invariants. The taxonomy is not disjoint — the determinant of a matrix is multiplicative, a similarity invariant, and a structural feature of a linear map at the same time — but the four forms give a checklist. When entering a new problem, ask which kind is in play.

- **Summative invariants.** A sum of several quantities remains constant despite local redistribution. The interior angle sum of an $n$-sided convex polygon, $(n - 2) \cdot 180°$, is fixed regardless of the individual angles. The total probability of a finite sample space is always $1$. The trace of a matrix is invariant under similarity transformations. The momentum of an isolated mechanical system is conserved across all internal interactions.

- **Multiplicative invariants.** A product is preserved through transformations. By Vieta's formulas, the product of the roots of $a_n x^n + \cdots + a_0$ equals $(-1)^n a_0 / a_n$, regardless of how the polynomial is factored. The determinant satisfies $\det(AB) = \det(A) \det(B)$, so it is multiplicative across compositions of linear maps. The greatest common divisor is preserved by the Euclidean step $(a, b) \mapsto (b, a \bmod b)$ — the engine of the Euclidean algorithm.

- **Relational invariants.** An equation holds across an entire family of objects. The Pythagorean identity $\sin^2 \theta + \cos^2 \theta = 1$ holds for every real $\theta$. The relation $a^2 + b^2 = c^2$ holds for every right triangle. The discriminant $b^2 - 4ac$ governs the nature of the roots of every quadratic, regardless of how the equation has been algebraically rearranged.

- **Structural invariants.** A property of a configuration that survives a class of operations. The Euler characteristic $V - E + F = 2$ is invariant under continuous deformations of any sphere-equivalent polyhedron. The rank of a matrix is invariant under elementary row and column operations. The chromatic number of a graph is invariant under vertex relabeling. These invariants live not in the numerical entries but in the abstract architecture.

### 1.2 The Core Principle

The principle of invariance, stripped to its essence, is small enough to fit on a single line.

> *In every problem, certain things change and certain things do not. The invariant is what stays fixed, and it is almost always the key to the solution.*

This sentence inverts a deeply ingrained cognitive tendency. When a beginner encounters a problem, the instinct is to focus on what is varying. If angles vary, write angle equations; if positions shift, track positions; if values increase, write increase formulas. The approach is not wrong, but it tends, for problems of even moderate complexity, to generate more equations than are strictly needed. The invariant offers a different first move — anchor on what does not change, and express everything else relative to that anchor. The problem typically loses one or more degrees of freedom in a single step.

To see this in miniature, consider three positive real numbers whose sum is fifteen, and ask for the maximum of their product. Direct optimization in three unknowns is a Lagrange-multiplier exercise — manageable but heavy. The invariant — the fixed sum — collapses the problem in one move. By symmetry (an archetype we shall meet in Chapter 2), the maximum must occur at $x = y = z = 5$, giving a product of $125$. We did not invoke Lagrange. We invoked a constant. The invariant did not merely simplify the calculation; it *revealed the structure that made the answer obvious*.

### 1.3 The Cognitive Shift

Understanding invariance intellectually is one matter; using it in real time is another. The difficulty lies in overcoming a habit installed early. From their first arithmetic lessons, students are trained to begin a problem by writing equations *for what they are asked to find*. If a problem asks for the number of sides of a polygon, write $n$ and proceed. If it asks for an angle, call it $\theta$. The direct approach succeeds reliably on small problems where there is a one-to-one correspondence between what varies and what must be determined. It begins to fail when the number of varying quantities exceeds the number of natural equations available — and at the competition level, this failure is the rule rather than the exception.

The cognitive shift required by Invariance is small in form and large in consequence. Most students, on encountering a problem, immediately ask: *What am I solving for?* The invariant-trained thinker asks instead: *What does not change here?* This reordering — reconnaissance before engagement — is innocuous in appearance and transformative in effect.

Consider how the shift plays out concretely on a problem we will treat in detail in §4.1. The problem asks for the number of five-digit numbers, divisible by three, that can be formed using each of the digits $0, 1, 2, 3, 4, 5$ exactly once. The natural student, having read the problem, writes: *Let me list cases. The first digit can be any of $1$–$5$. The remaining four positions can hold any of the leftover five digits in some order. I need to filter out the ones not divisible by three.* They begin enumerating, then pause, recognizing that filtering $5! \cdot 5 = 600$ candidates by divisibility one at a time is hopeless.

The invariant-trained thinker reads the same problem and pauses. *Divisibility by three — there is an invariant here. A number is divisible by three if and only if the sum of its digits is divisible by three. That is my anchor. The sum $0 + 1 + 2 + 3 + 4 + 5 = 15$ is itself divisible by three; so a five-digit number using five of these six digits is divisible by three if and only if the* excluded *digit is one of $0$ or $3$. That single observation collapses the problem into two clean cases.* The two thinkers differ not in skill, but in *first move*. The second has identified the strategic constraint that will crack the problem before any enumeration has begun.

This shift — pausing before calculating, anchoring before equating — manifests in four habits that distinguish invariant-aware solvers.

1. **A mental library of common invariants.** When they see "polygon," they recall the angle sum and the exterior-angle relations. When they see "roots of a polynomial," they recall Vieta. When they see "isolated system" in physics, they recall conservation laws. This is not memorization; it is structured pattern recognition built up over many problems.

2. **A habit of asking *what is conserved?* before any equation is written.** The question is asked aloud, internally, every time. It is the invariant analogue of a pilot's pre-flight checklist.

3. **An alertness to problems with many varying elements.** A surface description that mentions several changing quantities is, almost always, a signal that some combination of them is fixed. The presence of motion is itself a clue.

4. **A tolerance for the appearance of inactivity.** Pausing to identify an invariant feels passive compared to writing equations; experienced solvers have learned that the brief pause is the most productive time in the entire problem. It is, in the language of an Indian master who taught problem solving for decades, "the time when the problem solves itself, while the student waits."

The fourth habit is the hardest. A student trained in direct methods feels — correctly — that they are not *doing* anything in the first thirty seconds of an invariant-led approach. The discomfort is real. But the upfront investment in reconnaissance pays out the first time it shows up. It is the difference between hacking through a jungle and walking the path that has been there all along.

---

## 2. The Deep Structure

### 2.1 Mathematical Foundations

The strategy of invariance is not, fundamentally, a problem-solving technique. It is a feature of mathematical architecture: certain quantities exist precisely *because* they are invariant. To see this clearly, we recast the definition of §1.1 in the language of group actions.

When a group $G$ acts on a set $X$, the *orbit* of an element $x \in X$ is the set $\{ g \cdot x : g \in G \}$. The orbits partition $X$ into equivalence classes — two elements lie in the same orbit if and only if some group element carries one to the other. An invariant of the action, in this language, is simply a function on $X$ that is *constant on each orbit*. Equivalently, an invariant is a function on the quotient set $X / G$. The space $X / G$ is the natural domain on which invariants live.

This reformulation explains why invariants are not arbitrary. They are precisely the well-defined functions on the quotient. Whenever a system evolves under a group of transformations, the genuine quantities of interest are those that descend to the orbit space. *Everything else is coordinates.*

The most celebrated instance of this principle is due to Emmy Noether, whose 1918 theorem connects symmetries of physical systems to conserved quantities in a mathematically exact way. We state an informal version that captures the idea while postponing the analytical apparatus to the references.

\begin{theorem}[Noether's First Theorem, informal statement (Noether, 1918)]
Every continuous one-parameter symmetry of an action functional in classical mechanics yields a corresponding conserved current — a quantity invariant along physical trajectories.
\end{theorem}

Time-translation symmetry — *the laws of physics are the same today as yesterday* — yields conservation of energy. Spatial-translation symmetry — *the laws are the same here as there* — yields conservation of momentum. Rotational symmetry yields conservation of angular momentum. Noether's theorem is the precise mathematical statement of an architectural fact: *in the presence of continuous symmetry, invariance is automatic*. Conservation laws are not, on this view, additional axioms imposed by experiment; they are theorems forced by the geometry of physical law.

A related, earlier perspective is due to Felix Klein. In his 1872 *Erlangen Program*, Klein proposed that *a geometry is the study of the properties invariant under a chosen group of transformations.* Euclidean geometry is the geometry of the rigid-motion group. Affine geometry is the geometry of the affine group. Projective geometry is the geometry of the projective group. Topology is the geometry of homeomorphisms. The objects studied in each geometry are precisely those that the corresponding group leaves untouched. Klein's reformulation made invariance the *defining* feature of geometric structure, not a tool used within it.

A clean illustration of Klein's principle, drawn from elementary topology, is the Euler characteristic of a polyhedron. For any convex polyhedron — or, more generally, any polyhedron whose surface is topologically a sphere — Euler's formula

\[ V - E + F = 2 \]

holds, where $V, E, F$ count vertices, edges, and faces. The remarkable feature is the quantity's stability under continuous deformation. Push the cube into a sphere and the formula still holds. Twist the tetrahedron into something unrecognizable and the formula still holds. Glue a handle onto the surface, however, and the value drops to zero. The Euler characteristic *measures the surface's topological type* — it is a structural invariant in the strict sense of §1.1, the function $X \to \mathbb{Z}$ that descends to the quotient $X / \text{Homeo}^+$.

We will see in Chapter 2 that Klein's perspective gives the relationship between invariance and symmetry its sharpest form. For now, the lesson of §2.1 is that the structures we use most casually in mathematics — geometric, algebraic, topological — are themselves *defined* by their invariants.

### 2.2 Physical Foundations

Physics provides some of the cleanest illustrations of invariance because conservation laws are tangible. Energy may shift between kinetic and potential forms in a swinging pendulum; total mechanical energy remains fixed in the absence of friction. Momentum redistributes among bodies in collision; the total is preserved by Newton's third law. Angular momentum reapportions when a skater pulls in her arms; the product $I \omega$ holds. Electric charge can be moved between conductors but never created or destroyed.

The point worth pressing is structural rather than computational. *Conservation laws are invariants enforced by the structure of physical law itself.* A proposed solution that violates them is not merely incorrect — it is impossible. This makes physical invariants extraordinarily powerful for problem solving. Once a relevant conserved quantity is identified, an entire region of configuration space is excluded from consideration without further calculation.

The translation to mathematical problem solving is direct. Whenever a problem describes a closed system, where operations rearrange but neither create nor destroy, suspect an invariant total. Whenever the problem exhibits symmetry — an obvious one or a hidden one — anticipate the corresponding conservation, in the spirit of Noether. Both habits will reappear throughout the worked examples of §4.

### 2.3 Cognitive Foundations

Why, given the clarity of the principle, is invariance not the default first move of every problem solver?

The answer lies in cognitive evolution. Human attention is calibrated to detect *change*. We notice the moving lion, not the still grass. The bias served well on the savannah and serves poorly when the grass holds the answer. Even mathematically talented students, in studies of problem-solving behavior, exhibit a pronounced *change bias* — preferentially attending to varying quantities and discounting the constant ones. The invariant, by being unchanging, becomes invisible.

Three remedies have proved reliable in training. *Explicit pause:* allow the first ten seconds after reading a problem to be pause rather than calculation. *Explicit listing:* write down what is changing and what is not, in two columns, before any equation is written. *Explicit naming:* once an invariant is identified, give it a name and a number — *Invariant 1: the angle sum is fixed at $(n-2) \cdot 180°$* — and refer to it by that label throughout the solution. Naming makes the invariant a first-class object of thought, not a background assumption.

Sustained, these habits convert invariance from a memorized technique into a reflex.

---

## 3. The Diagnostic Toolkit

### 3.1 The Three Questions Method

The three questions below are sufficient, in our experience, to extract the invariant from the great majority of problems where one is present. We state them as a procedural unit: ask the questions in order, and complete each before proceeding to the next.

**Question 1. *What are the moving parts?***

Catalog systematically every quantity in the problem that varies. Do this on paper, not in the head — externalizing the inventory frees working memory for the deeper question that follows. The list serves three purposes simultaneously: it establishes what the invariant is *not*; it surfaces combinations of varying quantities that might themselves be fixed (a sum, a product, a ratio); and it makes plain how many independent variables the problem actually contains.

*When this question succeeds:* the moving parts cluster around a small number of structural axes. *When it fails:* the list is generated mechanically without surfacing any structure — typically a sign that the problem statement should be re-read more carefully.

**Question 2. *What is the fixed relationship?***

Search, against the inventory of moving parts, for a relation that holds throughout the problem's evolution. Use the four-form taxonomy of §1.1 as a checklist:

- *summative* — a fixed sum;
- *multiplicative* — a fixed product;
- *relational* — an equation always satisfied;
- *structural* — a configuration property that survives the operations.

If a particular form yields nothing, move to the next. If multiple forms apply, name them all — most rich problems contain several.

*When this question succeeds:* the invariant emerges within seconds because it matches an entry in the solver's mental library. *When it fails:* the invariant exists but is non-obvious — it requires a coloring, a substitution, or some auxiliary structure to surface. At that point, the technique of §4.2 — *introducing* a coloring or auxiliary structure — becomes the move.

**Question 3. *Can I anchor my solution around the invariant?***

This is the question most often skipped in practice. Identifying the invariant is necessary; using it is a separate move. The most reliable use is *find two distinct expressions for the same invariant quantity, and equate them.* Two expressions for the same number give an equation; the equation typically eliminates one or more variables in a single step.

*When this question succeeds:* the equation that results has fewer unknowns than the original system. *When it fails:* the invariant exists but provides no leverage point — usually a sign that the problem is multidirectional and an additional archetype, often Domain Constraints (Archetype #9), is needed to complete the solution.

### 3.2 Forms of Invariants: A Comprehensive Guide

The taxonomy of §1.1 admits a more detailed treatment, with examples at the level of competition mathematics.

**Type I. Summative Invariants.** A sum of several quantities remains fixed despite local rearrangement.

- The interior angle sum of a convex $n$-gon is $(n-2) \cdot 180°$, regardless of the individual angles.
- The trace of a square matrix is invariant under similarity transformations $A \mapsto P A P^{-1}$.
- The sum of the deviations of a finite data set from its mean is identically zero.
- For an isolated mechanical system, total momentum is invariant under all internal interactions (Newton's third law).
- For a monic polynomial, the sum of the roots equals the negative of the coefficient of $x^{n-1}$ — Vieta's first relation, invariant across factorizations.

These often arise from a *closure principle* — operations rearrange but neither create nor destroy — or from a *structural formula* expressing the sum in terms of a parameter that is itself fixed.

**Type II. Multiplicative Invariants.** A product persists through transformations.

- $\det(AB) = \det(A) \cdot \det(B)$ for all square matrices of compatible size; the determinant is multiplicative under composition.
- The Euclidean step $(a, b) \mapsto (b, a \bmod b)$ preserves $\gcd(a, b)$ exactly — the engine of the Euclidean algorithm.
- For a monic polynomial $\prod (x - r_i)$, the product of the roots equals $(-1)^n$ times the constant term — Vieta's last relation.
- In a geometric progression, the product of two terms equidistant from any fixed center depends only on the center, not on the chosen pair — a multiplicative invariant of the index pair.

**Type III. Relational Invariants.** An equation holds universally across an entire family of objects.

- $a^2 + b^2 = c^2$ holds for every right triangle with hypotenuse $c$.
- $\sin^2\theta + \cos^2\theta = 1$ for every real $\theta$.
- The discriminant $b^2 - 4ac$ governs the nature of the roots of every quadratic $a x^2 + b x + c = 0$.
- For any cyclic quadrilateral with sides $a, b, c, d$ and diagonals $p, q$, Ptolemy's theorem $pq = ac + bd$ holds — a relational invariant of the cyclic-quadrilateral family.

These appear most often in *prove that...* problems and in solving by relational substitution.

**Type IV. Structural Invariants.** A property of a configuration that survives a class of operations.

- Euler characteristic $V - E + F = 2$ for sphere-equivalent polyhedra, under continuous deformation.
- The rank of a matrix is invariant under elementary row and column operations.
- The parity of a permutation is invariant under further decomposition into transpositions.
- The chromatic number, the connectivity, and the planarity of a graph are each invariants under vertex relabeling.

These require the highest level of abstraction — recognizing that a property of the *configuration*, not of any specific element, is what is preserved.

### 3.3 Common Pitfalls

Even practiced solvers fall into a small number of recurring errors when applying the Invariance archetype. We name and treat each.

**Pitfall 1. The Invisible Invariant.** The most common failure: the invariant is so familiar that it becomes part of the assumed background and is never explicitly invoked. A student calculating with polygon angles may *use* the angle-sum relation implicitly, then fail to *use* it as the strategic anchor of the solution. *Remedy:* make every invariant explicit. Write it on paper, label it (Invariant 1, Invariant 2), refer to it by label.

**Pitfall 2. The False Invariant.** Assuming a quantity is invariant when the conditions of the problem violate the standard hypotheses. The horizontal velocity of a projectile is invariant in a vacuum and not invariant in air. *Remedy:* state the conditions under which the invariant holds, then verify those conditions are present. If in doubt, test the invariant on two specific configurations and check.

**Pitfall 3. Ignoring the Invariant's Redundancy.** Correctly identifying an invariant but failing to recognize that it eliminates a degree of freedom. The student then writes more equations than are needed; the resulting system, though solvable, is far heavier than necessary. *Remedy:* after identifying the invariant, count the remaining degrees of freedom explicitly. If the invariant collapses two unknowns into one, do not retain the second.

**Pitfall 4. Over-Reliance on the Invariant.** Assuming that identifying the invariant suffices to solve the problem. Most invariant-based solutions require a second archetype to finish — typically Domain Constraints (Archetype #9) to filter the candidates the invariant has produced. The five-digit-divisibility problem of §4.1 will illustrate exactly this two-step pattern: the divisibility invariant produces two candidate cases, and a leading-zero constraint filters within one of them. *Remedy:* frame the solution explicitly in two stages: (1) the invariant generates candidates; (2) the auxiliary archetype filters them.

---

## 4. Worked Examples

The three examples in this section span the chapter's full range and illustrate three different *forms* of invariance from the §3.2 taxonomy. Worked Example 1 (JEE Mains, 1989) turns on a **relational** invariant — the divisibility-by-three rule, an equation that holds over every five-digit candidate. Worked Example 2 (JEE Advanced, 1981) turns on a **summative** invariant produced by *double counting* — a single quantity expressed two ways. Worked Example 3 (Joshi's Chapter 4 Main Problem) turns on a **structural** invariant hidden inside the binary expansion of an integer. Each is solved by the Three Questions Method.

All three problems are taken from K.D. Joshi's *Educative JEE Mathematics* (2nd ed.) — the canonical source-of-truth for Pillar 2.

### 4.1 Example 1 — Five-Digit Numbers Divisible by Three

\begin{problem}[JEE 1989]
Find the total number of five-digit numbers divisible by three that can be formed using each of the digits $0, 1, 2, 3, 4, 5$ exactly once.
\end{problem}

**Source.** Joshi, *Educative JEE Mathematics*, Ch. 1, Comment 1 (JEE 1989).

**Three Questions applied.**

*Question 1 — Moving parts.* We are choosing five of the six digits $\{0, 1, 2, 3, 4, 5\}$ and arranging them. Two layers vary: *which* digit is excluded (six choices) and the *order* of the remaining five (up to $5! = 120$ choices). On the surface there are six families of size $120$, for $720$ candidates — but a leading zero is not a five-digit number, and most candidates are not divisible by three. Listing and filtering is hopeless.

*Question 2 — Fixed relationship.* The decisive invariant is the divisibility rule:

> *An integer is divisible by $3$ if and only if the sum of its digits is divisible by $3$.*

This is a **Type-III relational invariant** (§3.2) — a property of the digit-multiset that survives every permutation of digits in the place-value representation. *Invariant 1: a five-digit number formed from a chosen subset of $\{0, 1, 2, 3, 4, 5\}$ is divisible by $3$ if and only if the* sum *of the chosen digits is divisible by $3$.*

Now anchor the whole digit-set: $0 + 1 + 2 + 3 + 4 + 5 = 15$, which is itself divisible by $3$. Removing one digit reduces the sum by that digit's value. Hence

> *The remaining five digits have sum divisible by $3$ if and only if the excluded digit is itself $\equiv 0 \pmod 3$.*

Among $\{0, 1, 2, 3, 4, 5\}$, the digits congruent to $0$ modulo $3$ are exactly $\{0, 3\}$. The invariant has cut the candidate pool from six families to **two**.

*Question 3 — Anchor.* Decompose the answer set $S$ into

- $A$: five-digit numbers using $\{1, 2, 3, 4, 5\}$ (digit $0$ excluded);
- $B$: five-digit numbers using $\{0, 1, 2, 4, 5\}$ (digit $3$ excluded).

Set $A$ contains every permutation of five non-zero digits; $|A| = 5! = 120$, all of them legitimate five-digit numbers.

Set $B$ is more delicate. There are $5! = 120$ permutations of $\{0, 1, 2, 4, 5\}$, but those that begin with $0$ are not five-digit numbers. The count of leading-zero strings is $4! = 24$. By complementary counting, $|B| = 120 - 24 = 96$.

Therefore

\[ |S| \;=\; |A| + |B| \;=\; 120 + 96 \;=\; \boxed{216}. \]

**The domain constraint.** Notice the second archetype at work. The divisibility invariant alone gave us $|A| + |B| = 240$. The *leading-zero constraint* — a domain restriction on what counts as a "five-digit number" — removed $24$ candidates from $B$. This is precisely the **invariant-generates / constraint-selects** pattern named in §3.3 Pitfall 4. Without the constraint pass we would over-count by exactly the candidates the invariant cannot see.

**Key lesson.** A divisibility rule is an invariant of the digit-multiset under place-value permutation. Most students learn the *rule of three* as a parlor trick for checking arithmetic. The invariant lens reveals it for what it actually is: a relational invariant that lives one level below the surface of the digit string, and that converts an open-ended enumeration problem into a clean two-case decomposition.

> *Algebra generates candidates; the domain selects the survivors.*

This two-step pattern recurs in Worked Example 3, in essentially every counting problem in Joshi's first six chapters, and as the workhorse of Pillar 3 (Multidirectional Solving).

### 4.2 Example 2 — A Double-Counting Incidence Problem

\begin{problem}[JEE 1981]
Let $A_1, A_2, \ldots, A_{30}$ be thirty sets, each with five elements, and let $B_1, B_2, \ldots, B_n$ be $n$ sets, each with three elements. Suppose
\[ \bigcup_{i=1}^{30} A_i \;=\; \bigcup_{j=1}^{n} B_j \;=\; S, \]
and that each element of $S$ belongs to exactly ten of the $A_i$ and exactly nine of the $B_j$. Find $n$.
\end{problem}

**Source.** Joshi, *Educative JEE Mathematics*, Ch. 1, Comment 10 (JEE 1981).

**Three Questions applied.**

*Question 1 — Moving parts.* We have three quantities in play: the size of the common universe $|S|$, the number of $B$-sets $n$, and — implicit in the problem statement — the *incidence relation* "$x \in A_i$" (and separately "$x \in B_j$"). The given conditions describe each incidence relation from two complementary directions: by counting the sets ($30$ of them, each of size $5$) and by counting the elements ($|S|$ of them, each in $10$ of the sets).

*Question 2 — Fixed relationship.* Construct the **incidence set**

\[ F \;=\; \{ (x, i) \;:\; x \in S,\; i \in \{1, \ldots, 30\},\; x \in A_i \}. \]

The cardinality $|F|$ is a single number that can be computed two ways. This is the **double counting principle**, and the equality of the two counts is a Type-I summative invariant: one quantity, two valid expressions.

*Counting $F$ by sets.* Each $A_i$ contributes exactly $|A_i| = 5$ pairs of the form $(x, i)$. There are $30$ such sets. So $|F| = 30 \cdot 5 = 150$.

*Counting $F$ by elements.* Each $x \in S$ contributes exactly one pair $(x, i)$ for each of the ten $A_i$ it belongs to. So $|F| = |S| \cdot 10$.

Equating the two expressions for the same invariant total:

\[ 30 \cdot 5 \;=\; |S| \cdot 10 \quad \Longrightarrow \quad |S| \;=\; 15. \]

*Question 3 — Anchor.* The same invariant principle applies to the $B$-side. Define

\[ G \;=\; \{ (x, j) \;:\; x \in S,\; j \in \{1, \ldots, n\},\; x \in B_j \}. \]

Counting by sets: $|G| = n \cdot 3$. Counting by elements: $|G| = |S| \cdot 9 = 15 \cdot 9 = 135$. Equating,

\[ n \cdot 3 \;=\; 135 \quad \Longrightarrow \quad \boxed{n = 45}. \]

**Why this is invariance, not "a trick."** The pedagogical temptation is to file double counting under "clever combinatorial techniques." The invariant lens reframes it. The cardinality $|F|$ is a *single quantity* that is defined independently of how we choose to enumerate it. Counting-by-rows and counting-by-columns are two *coordinate systems* on the same invariant total. The technique works not because it is clever but because the total is *invariant* under the choice of which axis we slice along — exactly the §3.2 Type-I summative pattern, written in the language of incidence relations.

**Key lesson.** Whenever a problem describes a collection of objects from two complementary directions — *each set has size $p$* and *each element appears in $q$ sets* — there is automatically an incidence-counting invariant available. The two products $\#\text{sets} \cdot p$ and $\#\text{elements} \cdot q$ are two expressions for the same total; equating them solves for whichever quantity is unknown.

> *Two ways of counting the same thing give one equation.*

This is the engine of double counting, of Burnside's lemma (Pillar 5, Cluster G), and — when generalised to "two expressions for one quantity" — of every problem in this chapter.

### 4.3 Example 3 — Binomial Coefficients All Odd

\begin{problem}[Joshi, Ch. 4 Main Problem]
Find the number of integers $n$ with $10 \leq n \leq 1000$ having the property that the binomial coefficient $\binom{n}{k}$ is odd for every integer $k$ with $0 \leq k \leq n$.
\end{problem}

**Source.** Joshi, *Educative JEE Mathematics*, Ch. 4 (Number Theory), Main Problem. The problem is the chapter-opening case study and is treated, in Joshi's exposition, as a paradigm of how *experimentation* uncovers a hidden invariant in a number-theoretic problem.

**Three Questions applied.**

*Question 1 — Moving parts.* The integer $n$ varies over the range $\{10, 11, \ldots, 1000\}$, and for each $n$ there are $n + 1$ binomial coefficients $\binom{n}{0}, \binom{n}{1}, \ldots, \binom{n}{n}$. The condition is a *joint* condition on all $n + 1$ coefficients at once. We are not asked for a closed form for the count; we are asked for a count of $n$ satisfying a universal predicate.

A direct attack — for each $n$, compute all $n + 1$ binomial coefficients and check parity — is hopeless. But the symmetry $\binom{n}{k} = \binom{n}{n-k}$ halves the work, and the observation that $\binom{n}{1} = n$ is even whenever $n$ is even halves it again. Experimentation on small odd $n$ yields:

| $n$ | All $\binom{n}{k}$ odd? |
|---|---|
| $1$ | yes ($1, 1$) |
| $3$ | yes ($1, 3, 3, 1$) |
| $5$ | **no** ($\binom{5}{2} = 10$ is even) |
| $7$ | yes ($1, 7, 21, 35, 35, 21, 7, 1$) |
| $9$ | **no** ($\binom{9}{2} = 36$) |
| $11, 13$ | no |
| $15$ | yes (all $\binom{15}{k}$ odd) |

The favourable values so far are $1, 3, 7, 15$ — **each one less than a power of $2$**. The pattern suggests:

> *Conjecture: $\binom{n}{k}$ is odd for every $0 \leq k \leq n$ if and only if $n + 1$ is a power of $2$.*

*Question 2 — Fixed relationship.* What invariant of $n$ controls the parity of $\binom{n}{k}$? The answer is one of the cleanest results in elementary number theory, and its statement is the heart of the problem.

\begin{theorem}[Kummer's Theorem, parity form (Kummer, 1852)]
For integers $0 \leq k \leq n$, the largest power of $2$ dividing $\binom{n}{k}$ equals the number of carries that occur when $k$ is added to $n - k$ in base $2$. In particular, $\binom{n}{k}$ is *odd* if and only if no carries occur — equivalently, if and only if every binary digit of $k$ is $\leq$ the corresponding binary digit of $n$ (the *Lucas* condition).
\end{theorem}

The structural invariant we want is now visible:

> *Invariant 2 (binary domination): $\binom{n}{k}$ is odd for **every** $0 \leq k \leq n$ if and only if every binary digit of every $k \in \{0, 1, \ldots, n\}$ is dominated by the corresponding binary digit of $n$.*

This is a **Type-IV structural invariant** (§3.2) — a property of the *binary expansion* of $n$, surviving every choice of $k$ in the range. The integers $n$ for which the domination condition holds *uniformly in $k$* are precisely those whose binary digits are **all** $1$ — that is, $n = 2^m - 1$ for some positive integer $m$. (If any binary digit of $n$ is $0$, choose $k$ to have a $1$ in that position with all other digits $0$; then $k \in \{0, \ldots, n\}$ but its $1$-bit is not dominated, and $\binom{n}{k}$ is even.)

The conjecture from experimentation is now proved as a corollary of Kummer's theorem. Joshi's *EJM* gives a self-contained proof from first principles using the formula $\binom{n}{k} = \binom{n}{k-1} \cdot \frac{n-k+1}{k}$ and a careful tracking of powers of $2$ in the numerator and denominator; we have substituted the named-theorem route for compactness. The two arguments produce identical conclusions and are explicitly equivalent.

*Question 3 — Anchor.* The invariant has reduced the problem to a clean counting question on the integers $n + 1$:

> *How many powers of $2$ lie in the interval $11 \leq n + 1 \leq 1001$?*

The smallest power of $2$ in this range is $16 = 2^4$ (since $2^3 = 8 < 11$), the largest is $512 = 2^9$ (since $2^{10} = 1024 > 1001$). The exponents run $m = 4, 5, 6, 7, 8, 9$, giving the favourable values

\[ n \;\in\; \{15,\; 31,\; 63,\; 127,\; 255,\; 511\}. \]

There are exactly $\boxed{6}$ such integers.

**Key lesson.** The chapter's three worked examples have demonstrated three forms of invariance, each operating at a different level of structure. WE1's divisibility-by-three rule lives at the level of *digit multisets in base $10$*. WE2's double counting lives at the level of *the cardinality of an incidence set*. WE3's binary-domination condition lives at the level of *the binary representation of an integer*. In each case, the invariant is a fact about the underlying representation that survives every variation the problem permits.

> *Choose the right representation, and the invariant is already there.*

This is the lesson Joshi makes central in his Chapter 4. It is also the cognitive substrate of *Hidden Structure* (Archetype #4) — recognizing that an unfamiliar problem is usually a familiar one in disguise, and that the disguise is almost always a poorly chosen representation.

**A note on Vieta jumping and IMO 1988 P6.** Readers familiar with olympiad culture will recognize that the "invariance lives on an orbit, not a point" pattern reaches its most celebrated form in the *Vieta jumping* proof of IMO 1988, Problem 6 — the classical result that if $ab + 1 \mid a^2 + b^2$ then $(a^2 + b^2)/(ab + 1)$ is a perfect square. That problem is the canonical case study of **Central Elegant Point (CEP)** design — a problem engineered around a specific elegant target — and is therefore treated in full in **Pillar 4** (The Art of CEP-Based Problem Design), not here. Pillar 2 is the conceptual-clarity tier; its problem bank is Joshi's *EJM*. The orbit-level analysis of Vieta jumping belongs to the problem-design tier, and we reserve it for that pillar.

---

## 5. Practice Problems

The seven problems below span the chapter's range — two at JEE Mains / foundational tier, three at JEE Advanced tier, and two at RMO / INMO tier. **All seven are drawn from K.D. Joshi's *Educative JEE Mathematics*** (Pillar 2's canonical problem bank, per Blueprint §6.2), with explicit competition citations preserved. Solutions appear in the appendix at the chapter's end.

\begin{problem}[5.1, foundational]
Six boys and six girls sit in a row at random. Find the probability that the six girls sit together.
\end{problem}

*Source: JEE 1979 (Joshi, EJM Ch. 1, Comment 4).*

\begin{problem}[5.2, intermediate]
Prove that for every positive integer $n$, the integer $2 \cdot 7^n + 3 \cdot 5^n - 5$ is divisible by $24$.
\end{problem}

*Source: JEE 1985 (Joshi, EJM Ch. 4, Comment 8).*

\begin{problem}[5.3, intermediate]
Let $n$ be an odd positive integer. Prove that $n(n^2 - 1)$ is divisible by $24$.
\end{problem}

*Source: JEE 1983 (Joshi, EJM Ch. 4, Comment 8).*

\begin{problem}[5.4, intermediate / RMO]
Prove that the product of the first $1000$ even positive integers differs from the product of the first $1000$ odd positive integers by a multiple of $2001$.
\end{problem}

*Source: Regional Mathematics Olympiad (Joshi, EJM Ch. 24, Exercise 24.62).*

\begin{problem}[5.5, advanced / RMO]
Suppose $\alpha$ and $\beta$ are real numbers such that
\[ \alpha^3 - 3\alpha^2 + 5\alpha = 17 \qquad \text{and} \qquad \beta^3 - 3\beta^2 + 5\beta = -11. \]
Determine $\alpha + \beta$.
\end{problem}

*Source: Regional Mathematics Olympiad (Joshi, EJM Ch. 24, Exercise 24.13).*

\begin{problem}[5.6, advanced / RMO]
There are doors numbered from $1$ to $1000$ in a row. At any time each door is either open or closed. Initially all doors are open. An attendant makes $1000$ rounds; in the $k$-th round he changes the state of every door whose number is a multiple of $k$ (open becomes closed, closed becomes open). Find the number of doors that are open at the end of the $1000$-th round.
\end{problem}

*Source: Regional Mathematics Olympiad (Joshi, EJM Ch. 24, Exercise 24.75).*

\begin{problem}[5.7, advanced / INMO]
Find all functions $f : \mathbb{R} \to \mathbb{R}$ satisfying
\[ f(x + y) \;=\; f(x)\, f(y)\, f(xy) \qquad \text{for all } x, y \in \mathbb{R}. \]
\end{problem}

*Source: Indian National Mathematical Olympiad (Joshi, EJM Ch. 24, Exercise 24.69).*

---

## 6. The Connections Web

The Invariance archetype is one of the few in mathematics whose reach is genuinely unifying — it appears, in recognizable form, in nearly every domain that admits structured reasoning. We sketch the major instances.

### 6.1 Invariance Across Mathematical Domains

**Algebra.** The symmetric functions of the roots of a polynomial — sum, product, and intermediate elementary symmetric functions — are invariants of the action of the symmetric group on the root set, computable from the coefficients alone (Vieta). The determinant of a square matrix is a similarity invariant; the characteristic polynomial is a similarity invariant; the Jordan canonical form classifies linear endomorphisms by their similarity invariants.

**Geometry.** Klein's *Erlangen Program* organizes geometry by its invariants. Lengths and angles are Euclidean invariants. Length ratios on parallel lines are affine invariants. Cross-ratios are projective invariants. The Euler characteristic is a topological invariant. Each geometry, on Klein's view, is the study of a particular invariant theory.

**Analysis and Calculus.** Integration is invariant under reparametrization, which is the abstract justification for the change-of-variables formula. Energy is conserved along the trajectories of a conservative system, by direct calculation or by Noether's theorem. The $L^2$ norm is invariant under the Fourier transform — Parseval's theorem.

**Number Theory.** The greatest common divisor is invariant under the Euclidean step, the engine of the Euclidean algorithm. Modular invariants — the residue $n \bmod p$ for prime $p$ — survive arithmetic operations subject to the modular rule. The class number of an imaginary quadratic field is an invariant of the field structure.

**Combinatorics.** Coloring arguments — as in the mutilated chessboard — are constructions of invariants. The pigeonhole principle is most often deployed by exhibiting an invariant on the pigeons and a pigeonhole that violates it. Burnside's lemma counts orbits by averaging fixed-point counts of group elements — a direct application of orbit-level invariance.

**Topology.** The fundamental group, the homology groups, the Euler characteristic, and the Betti numbers are all topological invariants — quantities preserved under homeomorphism. A central theme of algebraic topology is the construction of progressively stronger invariants for distinguishing topological spaces.

### 6.2 Invariance in Physics and Other Quantitative Sciences

**Conservation laws.** Energy, momentum, angular momentum, electric charge, baryon number, lepton number — each is an invariant of the action of an underlying symmetry group, by Noether's theorem. The standard model of particle physics is, structurally, a list of gauge symmetries together with their conserved currents.

**Loop invariants.** In computer science, a *loop invariant* is a property maintained by every iteration of a loop — the strongest tool for proving program correctness. Hoare logic is, at its core, an invariant calculus.

**Data structure invariants.** A binary search tree's ordering property; a heap's parent-child inequality; a balanced tree's height bound. Each is an invariant maintained by the operations defined on the data structure.

**Equilibrium in economics.** A market in equilibrium is a fixed point of supply-and-demand dynamics — an invariant under the trading mechanism. Budget constraints in optimization are invariants of the choice set.

**Conservation in biology and chemistry.** Mass balance in chemical reactions; stoichiometric ratios; the Hardy–Weinberg principle that allele frequencies in an isolated random-mating population are invariant across generations.

### 6.3 Cross-Domain Manifestations

The invariance archetype is not confined to mathematics and the physical sciences. It surfaces, often unnamed, in domains as diverse as:

- *Engineering:* dimensional analysis (the Buckingham $\pi$ theorem) reduces complex multi-variable problems to dimensionless invariants.
- *Information theory:* Shannon entropy is invariant under bijective relabeling of the alphabet.
- *Linguistics:* the deep structure of a sentence is invariant under surface paraphrase, in transformational grammar.
- *Music theory:* a melody is invariant under transposition; a chord progression is invariant under change of key.
- *Cryptography:* the security of a cryptographic primitive depends on which transformations leave the underlying secret invariant.

### 6.4 Related Archetypes

Four archetypes stand in close relation to Invariance and deserve explicit note:

- **Archetype #2 (Symmetry).** Symmetry and invariance are two sides of the same coin, related precisely by Noether's theorem. A symmetry of a system is a transformation that leaves the system unchanged; the corresponding invariant is the conserved current it produces. *Anywhere there is symmetry, there is an invariant.* We treat this connection in full in Chapter 2.

- **Archetype #9 (Domain Constraints).** Invariance generates candidates; Domain Constraints filter them. The five-digit-divisibility problem of §4.1 is the canonical illustration: the divisibility invariant produces two candidate digit-sets, and the leading-zero constraint deletes $24$ candidates within one of them. The two archetypes are not in competition — they form the standard two-step pattern of bidirectional thinking, which Pillar 3 will treat in detail.

- **Archetype #12 (Extremal Principles).** Optimization subject to invariant constraints — the Lagrange multiplier setup — is the formal embodiment of "invariance plus extremization." Many physics problems and most calculus-of-variations problems have this structure.

- **Archetype #17 (Degrees of Freedom Analysis).** Each invariant constraint reduces the dimension of the solution space by one. Counting invariants against unknowns before solving is a standard reconnaissance move; if the count comes out negative, the system is overdetermined and rejection of some candidates is structurally guaranteed.

---

## 7. Master Takeaways

Seven principles distill the chapter. Each is a single line; each is meant to be quotable five years from now.

1. **If something stays constant, make it your anchor.**
   The invariant is the reference point in a sea of variation. Track it; let everything else move.

2. **Invariants reduce degrees of freedom.**
   $n$ unknowns minus $k$ independent invariant constraints leave $n - k$ degrees of freedom. Count before you solve.

3. **Conservation laws are invariants in disguise.**
   Energy, momentum, charge, mass balance, budget constraint — every conservation law of every science is an instance of the invariance archetype.

4. **The sum is often easier than the parts.**
   Aggregate properties — sums, products, structural counts — are frequently simpler than the individual elements they aggregate. When the parts resist, attack the whole.

5. **Invariants are necessary, not sufficient.**
   The invariant tells you what cannot happen. Domain constraints, inequalities, and existence requirements tell you what must happen. The full solution lives at the intersection.

6. **Look for what survives the transformation.**
   List the operations the problem permits; then ask, against that list, what quantity is unaffected. The invariant is precisely what is left standing.

7. **Symmetry implies invariance.**
   By Noether's theorem, every continuous symmetry yields a conserved current. When a problem exhibits symmetry, the corresponding invariant is *always already present* — and is almost always the key to the solution.

---

## 8. Self-Assessment Checklist

You may claim mastery of this chapter when each of the following is unhesitating.

- [ ] I can identify invariants in problems across at least three different domains (geometry, algebra, number theory, combinatorics).
- [ ] I can apply the Three Questions Method as a deliberate procedural unit, not a ritual.
- [ ] I can distinguish among the four forms of invariants — summative, multiplicative, relational, structural — and produce two examples of each.
- [ ] I can recognize when an apparent "invariant" is actually conditional and check the conditions explicitly.
- [ ] After identifying an invariant, I check domain constraints (Archetype #9) before reporting an answer.
- [ ] I can explain why invariants reduce degrees of freedom, in terms of the orbit space $X / G$.
- [ ] I can state Noether's theorem in plain English.
- [ ] I can spot at least one invariant in any new problem I read in the next week.

---

## Bridge to Chapter 2: Symmetry

Invariance has asked: *what does not change?* Symmetry asks a different but deeply related question: *what looks the same from multiple perspectives?*

Where Invariance focuses on quantities that *persist*, Symmetry focuses on equivalences — situations in which different elements, positions, or configurations are interchangeable without altering the underlying problem. The two archetypes are close cousins, and the relationship between them is given exactly by Noether's theorem: every continuous symmetry yields a corresponding invariant.

In Chapter 2 we will:

- Recognize the principal types of symmetry — reflective, rotational, permutational, gauge — and the groups that generate them.
- Use symmetry to reduce degrees of freedom, often dramatically: a problem with three indistinguishable variables collapses to a problem in one.
- Solve one representative case and generalize to all equivalent cases by the symmetry argument.
- Connect symmetry to invariance through Noether-type reasoning, completing the circle that this chapter has begun.

The journey from Invariance to Symmetry is natural. Both archetypes ask the solver to see beyond surface variation to underlying structure. Where Invariance finds *what persists*, Symmetry finds *what is equivalent*. Together, they form the foundation of *Structure Recognition* — the first of the five archetype categories, and the cognitive substrate on which the remaining four rest.

---

## Appendix — Solutions to Practice Problems

### Solution to 5.1 — Six boys and six girls (JEE 1979)

The invariant is the total count of equally likely seatings: $12!$. We construct the favourable count by collapsing the six girls into a single "block."

Treat the block-of-six-girls as a single composite object. There are now seven objects to seat in a row: six boys and one block. They can be arranged in $7!$ ways. Within the block, the six girls can themselves be permuted in $6!$ ways. By the multiplication principle, the favourable count is $7! \cdot 6!$. Hence

\[ P(\text{all girls together}) \;=\; \frac{7! \cdot 6!}{12!} \;=\; \frac{6!}{12 \cdot 11 \cdot 10 \cdot 9 \cdot 8} \;=\; \boxed{\frac{1}{132}}. \]

**Key lesson.** The invariant — the total $12!$ — is fixed before the problem statement is even fully read. The favourable count is constructed by *reducing the degrees of freedom*: collapsing six independently variable positions into one block-position is exactly a degrees-of-freedom reduction (Archetype #17). Many JEE probability problems hinge on this single move.

### Solution to 5.2 — $2 \cdot 7^n + 3 \cdot 5^n - 5$ divisible by $24$ (JEE 1985)

Let $f(n) = 2 \cdot 7^n + 3 \cdot 5^n - 5$. The invariant we will preserve is the divisibility-by-$24$ property of $f(n)$, marched forward by induction.

*Base.* $f(1) = 14 + 15 - 5 = 24$. ✓

*Inductive step.* Assume $24 \mid f(k)$ for some $k \geq 1$. Compute

\[ f(k+1) - 7\,f(k) \;=\; (2 \cdot 7^{k+1} + 3 \cdot 5^{k+1} - 5) - 7(2 \cdot 7^k + 3 \cdot 5^k - 5). \]

The $7^{k+1}$ terms cancel: $2 \cdot 7^{k+1} - 7 \cdot 2 \cdot 7^k = 0$. The remaining terms simplify:

\[ f(k+1) - 7\,f(k) \;=\; 3 \cdot 5^{k+1} - 21 \cdot 5^k - 5 + 35 \;=\; 5^k(15 - 21) + 30 \;=\; -6 \cdot 5^k + 30 \;=\; -6(5^k - 5). \]

Since $24 = 6 \cdot 4$, it suffices to show $4 \mid (5^k - 5)$. But $5 \equiv 1 \pmod 4$, so $5^k \equiv 1 \pmod 4$ and $5^k - 5 \equiv 1 - 1 = 0 \pmod 4$. Hence $-6(5^k - 5)$ is divisible by $24$.

Therefore $f(k+1) = 7\,f(k) + [-6(5^k - 5)]$ is divisible by $24$ (since $f(k)$ is, by inductive hypothesis, and the additive term is). $\blacksquare$

**Key lesson.** The "linear-combination shift" $f(k+1) - 7\,f(k)$ is Joshi's signature technique for divisibility problems where direct calculation explodes. The constant $c = 7$ is chosen precisely to eliminate the $7^{k+1}$ term; the resulting expression involves only $5^k$, which is then handled by a *secondary* invariant ($5^k \equiv 1 \pmod 4$). The invariant chain — $f(n) \equiv 0 \pmod{24}$, propagated by a shifted-difference identity, with a modular sub-invariant — is the deep structure.

### Solution to 5.3 — $n(n^2 - 1)$ divisible by $24$ for odd $n$ (JEE 1983)

Factor $n(n^2 - 1) = (n-1)\, n\, (n+1)$ — the product of three consecutive integers. Since $24 = 8 \cdot 3$ and $\gcd(8, 3) = 1$, it suffices to show divisibility by $8$ and by $3$ separately.

*Divisibility by $3$.* Among any three consecutive integers, exactly one is divisible by $3$. Hence $3 \mid (n-1)n(n+1)$. (This invariant — "any three consecutive integers contain a multiple of $3$" — is itself a Type-IV structural invariant of the integers modulo $3$ and holds without the odd-$n$ hypothesis.)

*Divisibility by $8$.* Here the odd-$n$ hypothesis is essential. Write $n = 2m - 1$ for some positive integer $m$. Then

\[ n(n^2 - 1) \;=\; (2m - 1)(2m - 2)(2m) \;=\; (2m - 1) \cdot 4 \cdot m(m - 1). \]

The product $m(m - 1)$ is the product of two consecutive integers, so it is divisible by $2$. Hence $4 \cdot m(m - 1)$ is divisible by $8$, and so is $(2m - 1) \cdot 4 \cdot m(m - 1) = n(n^2 - 1)$.

Combining: $24 = 8 \cdot 3 \mid n(n^2 - 1)$. $\blacksquare$

**Why $n$ must be odd.** For $n = 2$, $n(n^2 - 1) = 2 \cdot 3 = 6$, which is not divisible by $24$. The odd-$n$ hypothesis is precisely what guarantees that the factor $n - 1 = 2m - 2$ supplies the extra factor of $2$ needed to reach $8$.

**Key lesson.** Two independent invariants — "three consecutive integers contain a multiple of $3$" and "two consecutive integers contain a multiple of $2$" — combine multiplicatively (because $\gcd(8, 3) = 1$) to give divisibility by $24$. Decomposing the modulus $24$ into coprime factors and proving each separately is itself a Type-II multiplicative invariance of the divisibility relation. Joshi makes the same decomposition explicit in his commentary; the reduction-to-prime-powers move is a standard first step in any Joshi-style number-theory proof.

### Solution to 5.4 — Product of evens minus product of odds, mod $2001$ (RMO)

Let $E = 2 \cdot 4 \cdot 6 \cdots 2000$ and $O = 1 \cdot 3 \cdot 5 \cdots 1999$. We must show $2001 \mid (E - O)$.

The decisive observation is that $2001 = 3 \cdot 23 \cdot 29$ — three distinct prime factors. Since these are pairwise coprime, it suffices (by the Chinese Remainder Theorem) to prove $E \equiv O \pmod p$ for each $p \in \{3, 23, 29\}$.

The unifying invariant is a *pairing argument*. The integers from $1$ to $2000$ split into the $1000$ evens (forming $E$) and the $1000$ odds (forming $O$). Modulo any prime $p$ with $p \leq 1000$, we will find a natural correspondence that forces $E \equiv \pm O \pmod p$.

*Modulo $3$.* The even integers in $[2, 2000]$ that are $\equiv 0 \pmod 3$ are exactly the multiples of $6$ in $[6, 1998]$; there are $333$ such. So $E \equiv 0 \pmod 3$. The odd integers in $[1, 1999]$ that are $\equiv 0 \pmod 3$ are the odd multiples of $3$ in $[3, 1995]$; there are $333$ such. So $O \equiv 0 \pmod 3$. Hence $E \equiv O \equiv 0 \pmod 3$, and $3 \mid (E - O)$.

*Modulo $23$.* The even integers from $2$ to $2000$ include every multiple of $46 = 2 \cdot 23$ from $46$ to $1978$ — $\lfloor 2000/46 \rfloor = 43$ such, more than enough to force $E \equiv 0 \pmod{23}$. By the same reasoning, the odd multiples of $23$ in $[1, 1999]$ are $23, 69, 115, \ldots, 1955$ — $\lfloor 1979/46 \rfloor + 1 = 44$ such, so $O \equiv 0 \pmod{23}$. Hence $23 \mid (E - O)$.

*Modulo $29$.* Same structure: $\lfloor 2000/58 \rfloor = 34$ even multiples of $29$ in $E$, and $\lfloor 1979/58 \rfloor + 1 = 35$ odd multiples of $29$ in $O$. Both products are $\equiv 0 \pmod{29}$. Hence $29 \mid (E - O)$.

Combining: $3 \cdot 23 \cdot 29 = 2001$ divides $E - O$. $\blacksquare$

**Anand verification flag.** The above argument leans on the fact that each prime factor of $2001$ has both even and odd multiples within $[1, 2000]$, forcing both $E$ and $O$ to vanish modulo that prime. There is a cleaner alternative (the *Wilson-style* pairing $k \leftrightarrow 2001 - k$) used in some RMO writeups; if a tighter proof is preferred, flag for substitution.

**Key lesson.** The structural invariant is the **factorisation** $2001 = 3 \cdot 23 \cdot 29$ — Type-IV again, the same lesson as WE3. A divisibility claim about a large composite modulus is almost always best attacked by decomposing the modulus into prime-power factors, applying the appropriate invariant in each component, and reassembling via the Chinese Remainder Theorem. This is Joshi's standard playbook in Chapter 4.

### Solution to 5.5 — $\alpha^3 - 3\alpha^2 + 5\alpha = 17$, $\beta^3 - 3\beta^2 + 5\beta = -11$, find $\alpha + \beta$ (RMO)

The key invariant is hidden inside the cubic $f(t) = t^3 - 3t^2 + 5t$. We unmask it by an affine substitution.

*Centring the cubic.* Substitute $t = u + 1$:

\[ f(u + 1) \;=\; (u+1)^3 - 3(u+1)^2 + 5(u+1). \]

Expanding,

\[ (u+1)^3 = u^3 + 3u^2 + 3u + 1, \qquad 3(u+1)^2 = 3u^2 + 6u + 3, \qquad 5(u+1) = 5u + 5. \]

Combining,

\[ f(u+1) \;=\; u^3 + (3u^2 - 3u^2) + (3u - 6u + 5u) + (1 - 3 + 5) \;=\; u^3 + 2u + 3. \]

So if we set $\alpha = u + 1$ and $\beta = v + 1$, the system becomes

\[ u^3 + 2u + 3 = 17 \quad \Longrightarrow \quad u^3 + 2u = 14, \]
\[ v^3 + 2v + 3 = -11 \quad \Longrightarrow \quad v^3 + 2v = -14. \]

Adding,

\[ (u^3 + 2u) + (v^3 + 2v) \;=\; 0. \]

*The decisive invariant.* The function $g(x) = x^3 + 2x$ satisfies $g'(x) = 3x^2 + 2 > 0$ for every real $x$, so $g$ is **strictly increasing on $\mathbb{R}$** — and therefore injective. Since $g$ is also odd, the equation $g(u) + g(v) = 0$ is equivalent to $g(u) = g(-v)$, and by injectivity $u = -v$.

Therefore $u + v = 0$, and

\[ \alpha + \beta \;=\; (u + 1) + (v + 1) \;=\; (u + v) + 2 \;=\; \boxed{2}. \]

**Key lesson.** Two layers of invariance are stacked here. The first is the **affine substitution** $t = u + 1$, which kills the $t^2$ coefficient — a classical *Tschirnhaus transformation*, and a Type-IV structural invariant of the cubic under affine change of variable. The second is the **monotonicity (and oddness)** of $g(x) = x^3 + 2x$, which is itself a structural invariant of the function under reflection through the origin. The problem looks like algebra; the solution is two well-chosen invariants in series.

### Solution to 5.6 — One thousand doors (RMO)

Door number $j$ is toggled during round $k$ if and only if $k \mid j$. After all $1000$ rounds, door $j$ has been toggled exactly $d(j)$ times, where $d(j)$ is the number of positive divisors of $j$.

Since each door starts *open*, its final state is

\[ \begin{cases} \text{open} & \text{if } d(j) \text{ is even}, \\ \text{closed} & \text{if } d(j) \text{ is odd}. \end{cases} \]

*The decisive invariant.* The parity of $d(j)$ is a structural invariant of $j$ that we can state cleanly:

> $d(j)$ *is odd if and only if $j$ is a perfect square.*

The reason is a pairing argument: divisors of $j$ naturally come in pairs $(a, j/a)$, with $a \cdot (j/a) = j$. These pairs are *distinct* unless $a = j/a$, i.e., unless $a = \sqrt{j}$ — which occurs if and only if $j$ is a perfect square, in which case the divisor $\sqrt{j}$ is left unpaired. Hence $d(j)$ is even unless $j$ is a perfect square (one unpaired divisor making the count odd).

So the doors that are *closed* at the end are precisely those numbered with a perfect square in $[1, 1000]$: $1, 4, 9, 16, 25, \ldots, 961 = 31^2$. The count is $31$ (since $31^2 = 961 \leq 1000 < 1024 = 32^2$).

The number of doors *open* at the end is therefore

\[ 1000 - 31 \;=\; \boxed{969}. \]

**Key lesson.** A problem about $1000$ doors and $1000$ rounds reduces to a single structural invariant: *the parity of the divisor count*. The pairing $a \leftrightarrow j/a$ is itself an instance of bijection-as-invariant (Archetype #15 forward-reference); the unpaired fixed point at $\sqrt{j}$ is what breaks the symmetry. This pattern — "an involution with isolated fixed points" — recurs in Burnside's lemma, in Stern–Brocot fractions, and in dozens of olympiad combinatorics problems.

### Solution to 5.7 — Functional equation $f(x+y) = f(x)f(y)f(xy)$ (INMO)

Several constant functions satisfy the equation. We classify all solutions.

*Step 1: Locating $f(0)$.* Set $x = y = 0$:

\[ f(0) \;=\; f(0)^3 \quad \Longrightarrow \quad f(0)\bigl(f(0)^2 - 1\bigr) = 0, \]

so $f(0) \in \{0, 1, -1\}$.

*Step 2: The case $f(0) = 0$.* Set $y = 0$ for any $x$:

\[ f(x) \;=\; f(x) \cdot f(0) \cdot f(0) \;=\; 0. \]

So $f \equiv 0$ identically. *Direct check:* $0 = 0 \cdot 0 \cdot 0$. ✓

*Step 3: The case $f(0) \in \{1, -1\}$ implies $f(x)^2 \cdot f(0)^2 = f(x)$… (revisiting).* For $f(0) \in \{1, -1\}$, setting $y = 0$ yields $f(x) = f(x) \cdot f(0)^2$, which gives $f(x)(1 - f(0)^2) = 0$. Since $f(0)^2 = 1$, this identity is satisfied trivially and yields no constraint — proceed.

Set $y = 1$:

\[ f(x + 1) \;=\; f(x) \cdot f(1) \cdot f(x) \;=\; f(1) \cdot f(x)^2. \tag{$\star$} \]

*Step 4: Locating $f(1)$ and $f(-1)$.* From $(\star)$ with $x = 0$: $f(1) = f(1) \cdot f(0)^2 = f(1)$, trivial. With $x = 1$: $f(2) = f(1)^3$. With $x = -1$: $f(0) = f(1) \cdot f(-1)^2$.

Set $x = y = -1$: $f(-2) = f(-1)^2 \cdot f(1)$. Set $x = 2, y = -1$: $f(1) = f(2) \cdot f(-1) \cdot f(-2) = f(1)^3 \cdot f(-1) \cdot f(-1)^2 \cdot f(1) = f(1)^4 \cdot f(-1)^3$. So $1 = f(1)^3 \cdot f(-1)^3 = (f(1)\cdot f(-1))^3$, hence $f(1)\cdot f(-1) = 1$.

Substituting back into $f(0) = f(1) \cdot f(-1)^2 = f(-1) \cdot (f(1) \cdot f(-1)) = f(-1)$: **$f(-1) = f(0)$**.

*Step 5: The cases $f(0) = 1$ and $f(0) = -1$.*

If $f(0) = 1$: then $f(-1) = 1$, $f(1) = 1/f(-1) = 1$. From $(\star)$: $f(x + 1) = f(x)^2$. With $x = 1$: $f(2) = 1$. With $x = 2$: $f(3) = 1$. By induction $f(n) = 1$ for every integer $n \geq 0$. Symmetrically (using $y = -1$ analogously) $f(n) = 1$ for every negative integer. So $f \equiv 1$ on $\mathbb{Z}$.

For a fuller analysis: setting $y = x$ gives $f(2x) = f(x)^2 \cdot f(x^2)$. If we hypothesise $f \equiv 1$, both sides equal $1$. ✓ Direct check confirms $f \equiv 1$ is a global solution. Proving it is the *only* solution with $f(0) = 1$ requires more delicate analysis (typically: from $f(x+1) = f(x)^2$, derive $f(x) > 0$ for $x$ outside a measure-zero set, then chain back); we record the conclusion and flag the gap.

If $f(0) = -1$: then $f(-1) = -1$, $f(1) = -1$. From $(\star)$: $f(x+1) = -f(x)^2 \leq 0$. With $x = 1$: $f(2) = -f(1)^2 = -1$. With $x = 2$: $f(3) = -f(2)^2 = -1$. Inductively, $f \equiv -1$ on $\mathbb{Z}$.

Direct verification of $f \equiv -1$: $f(x+y) = -1$ and $f(x)f(y)f(xy) = (-1)(-1)(-1) = -1$. ✓

*The three solutions.* The classification yields three constant solutions:

\[ \boxed{f \equiv 0, \quad f \equiv 1, \quad f \equiv -1.} \]

**Anand verification flag.** The argument above proves the three constants are solutions and that they are the *only* constant solutions; it gestures at — but does not fully close — the proof that no non-constant solution exists. The full INMO solution typically completes this gap by combining $(\star)$ with the multiplicative identity at $y = x$ and a regularity (or rationality-density) argument. Please confirm or expand as needed for the printed solution.

**Key lesson.** Functional equations of this shape are governed by *substitution invariants*: each choice of $(x, y)$ in the original equation produces a derived identity that, accumulated across many substitutions, pins down the function. The strategic skill is recognizing which substitutions extract maximally informative invariants — typically $y = 0, y = 1, y = -1$, and $y = x$ in some order. Once the integer values are pinned, the constant solutions are forced.

---

🌑

*End of Chapter 1 — Invariance.*
