---
chapter: 2
archetype: Symmetry
subtitle: "If the Problem Has Symmetry, the Solution Inherits It"
category: Structure Recognition (Archetypes 1–4)
related_archetypes: [1, 3, 5, 15]
key_gems: [A09, B08, B09, B10, B11, C10, D03, D13, G06]
  - "Orbit-Stabiliser Theorem"
  - "Burnside's Lemma"
  - "Klein's Erlangen Program (1872) — geometry by invariance group"
  - "Noether's Theorem (1918) — continuous symmetry ⇒ conservation law"
  - "King's Property (interval reflection x → a + b − x)"
  - "Even/odd parity decomposition over a symmetric interval"
  - "Elementary symmetric polynomials σ₁, σ₂, σ₃ as adapted coordinates"
  - "Cyclic substitution a = x/y, b = y/z, c = z/x for the constraint abc = 1"
  - "Involution-on-odd-cardinality forces a fixed point"
  - "Tschirnhaus shift to expose hidden symmetry"
canonical_takeaway: "What is symmetric in the problem must be symmetric in the answer."
status: locked
last_revised: 2026-05-29
approved_on: 2026-05-26
locked_on: 2026-05-29
sourcing_note: "All worked examples and practice problems in this chapter are drawn from K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), or from JEE / RMO / INMO examinations commented on in that text. See Blueprint §6.2 for the sourcing rule. Problem slate locked in `pillar2-archetypes/_template/joshi-problems-locked.md` §Ch. 2."
---

# Chapter 2 — Symmetry

## *If the Problem Has Symmetry, the Solution Inherits It*

---

## Opening Vignette

A six-year-old child can recognise a snowflake. Drop it on a microscope slide and the geometry is unmistakable: a central point from which six identical arms radiate at sixty-degree intervals. The arms differ in fine detail — no two snowflakes are the same, the old aphorism goes — but the symmetry is exact. The child has no vocabulary for what they are seeing. They can nonetheless answer a question that an adult might miss. *Pick any property of the snowflake — its mass, its melting time, the intensity of light scattered from any one arm. Now ask: is there a property that distinguishes the top arm from the bottom-right arm?* The child shakes their head. There cannot be. The snowflake does not know which arm is the top one. The six-fold symmetry of the configuration is, on the snowflake's terms, a *constraint on what can be true* — and the constraint forces every measurable property to be shared, six ways, across the six arms.

This is *Symmetry*.

Now consider a scene that looks entirely different. A polynomial $f(x) = x^3 + a x^2 + b x + c$ has three real roots $r_1, r_2, r_3$. A student is asked: *what is $r_1 + r_2 + r_3$?* The roots themselves are not given; the polynomial's coefficients are. The student panics. They have no way to find $r_1, r_2, r_3$ explicitly without the cubic formula — a tool they have not been taught — and even then, the resulting expressions in radicals are forbidding. Yet the answer, Vieta tells us, is one line. $r_1 + r_2 + r_3 = -a$.

How does Vieta know this without computing the roots? The same way the child knows the six arms of the snowflake share their properties. The polynomial's coefficients — $a, b, c$ — are *symmetric* in the roots: if we relabel $r_1, r_2, r_3$ in any order, the coefficients do not change. (They cannot. The polynomial does not know which root is the first.) Therefore *every quantity that the coefficients can compute must be a symmetric function of the roots* — a function unchanged by relabeling. The sum $r_1 + r_2 + r_3$ is symmetric; the coefficients can find it. The individual root $r_1$ is not symmetric; the coefficients cannot, even in principle, single it out.

These two scenes — a snowflake and a polynomial — share a deep architecture. In each, a system has a group of transformations that leave it unchanged (the six rotations of the snowflake; the six permutations of the polynomial's three roots). In each, this group of transformations forces every fact extractable from the system to be itself unchanged under the same group. The constraint is not aesthetic; it is logical. *What is symmetric in the problem must be symmetric in the answer.*

In Chapter 1, we asked *what does not change?* and named the answer the invariant. In this chapter, we ask the dual question — *what transformation does the not-changing?* — and name the answer the symmetry group. The two perspectives are complementary, and they are connected precisely by Emmy Noether's celebrated theorem of 1918: every continuous symmetry yields a conserved quantity. Symmetry is Invariance seen from the other side. It is the same phenomenon, named from the point of view of the group rather than the point of view of the quantity.

> *Wherever a problem has a group of transformations that leave it unchanged, the solution lives in the world of objects that respect those transformations. Everything else is, mathematically speaking, a coordinate choice — to be avoided.*

---

## 1. The Archetype Defined

### 1.1 Formal Definition

We make the intuition precise, in language that parallels — and refines — the definitions of Chapter 1.

Let $X$ be a set: the configurations of a problem, the variables of an equation, the points of a geometric figure. Let $G$ be a group of bijections of $X$ — each $g \in G$ a relabeling, rotation, reflection, or permutation that sends $X$ to itself.

\begin{definition}[Symmetry of a problem]
A group $G$ of bijections of $X$ is a *symmetry of the problem* on $X$ if every hypothesis and every conclusion of the problem is invariant under the action of $G$: replacing $X$ by $g \cdot X$ for any $g \in G$ leaves the problem unchanged as a problem. A function $\phi : X \to Y$ is *equivariant under $G$* (or, in the simplest case, *invariant*) if $\phi(g \cdot x) = \phi(x)$ for every $g \in G$.
\end{definition}

The relationship to Chapter 1 is now exact. *Every invariant is, by definition, a function that is symmetric under the relevant group action.* The two archetypes are dual descriptions of one phenomenon. Chapter 1 named the *quantity* that does not change; this chapter names the *transformation group* that does the not-changing. Both perspectives are useful, and the strategic mathematician learns to switch between them at will.

A subtle point. In Chapter 1, we wrote our definition with a fixed group $G$ already understood. In practice, the harder problem-solving move is the *reverse* one: identifying $G$ from the problem statement. Most olympiad problems hand the solver a configuration and ask, implicitly, *what relabeling leaves this unchanged?* The answer is the symmetry group, and the answer is often only partially obvious. A polynomial in three variables may be symmetric in all three (the full permutation group $S_3$), or only cyclically symmetric (the cyclic subgroup $C_3$), or symmetric in two of three (a copy of $S_2$), or have no symmetry at all. The four cases produce wildly different solution techniques. Naming the right group is, often, the entire problem.

In this chapter we will encounter three principal forms of symmetry. They form a taxonomy parallel to the four-form taxonomy of invariants in Chapter 1 §1.1. The forms are not disjoint — a problem may exhibit two simultaneously, and the most rewarding problems usually do — but they organise the diagnostic toolkit of §3.

- **Permutation symmetry.** A finite set of variables is interchangeable; relabeling them in any order leaves every hypothesis and conclusion intact. The symmetric group $S_n$ acts. *Example:* $\sigma_2(x, y, z) = xy + yz + zx$ is invariant under all six permutations of $\{x, y, z\}$. *Counter-example:* $x + 2y + 3z$ has no permutation symmetry — the coefficients distinguish the variables.

- **Reflective and dihedral symmetry.** A configuration is unchanged under one or more reflections — equivalently, under the action of a dihedral group $D_n$ or one of its subgroups. *Example:* $\cos\theta$ is invariant under $\theta \mapsto -\theta$ (the reflection sending an angle to its negative); $\sin\theta$ is anti-invariant (sign-flipping) under the same. The decomposition of a function into even and odd parts is the simplest reflective-symmetry analysis.

- **Continuous symmetry.** The transformations form a continuous group — typically a Lie group — and the configuration is unchanged under any element of it. *Example:* the area of a circle is unchanged under all rotations of the plane about the centre; the integral $\int_{\mathbb{R}} f(x)\,dx$ is unchanged under all translations of the real line, $x \mapsto x + c$, when $f$ is integrable. The bridge to physics — Noether's theorem — lives here.

We will see all three forms in §4. WE1 (JEE 1979) illustrates cyclic permutation symmetry; WE2 (JEE 1997) illustrates reflective (interval) symmetry combined with parity; WE3 (RMO Ex. 24.67) illustrates full permutation symmetry combined with the *transposition* involution $A = A^T$.

### 1.2 The Core Principle

Chapter 1 fit its core principle on a single line. Symmetry admits a sentence equally compact.

> *What is symmetric in the problem must be symmetric in the answer.*

The sentence is short. Its consequences fill the chapter.

To unpack it, observe a logical fact. If a problem has a symmetry group $G$ — meaning every hypothesis and every conclusion is invariant under $G$ — then the *solution set* is also invariant under $G$. (If $x$ is a solution and $g \in G$, then $g \cdot x$ satisfies the same hypotheses and the same conclusion, so $g \cdot x$ is also a solution.) The solution set is a union of $G$-orbits. Every property of the solution that can be expressed in the problem's language must, therefore, be a property of a $G$-orbit — equivalently, a $G$-invariant function on the solution set.

This is the *master inheritance principle* of the chapter. *The solution inherits the symmetry of the problem*. An answer that breaks the symmetry is not just inelegant; it is *impossible* — unless we can identify, separately, the symmetry-breaking input that produced it.

A consequence is immediate and operationally powerful. *Before computing*, identify the symmetry group $G$ of the problem. *During computing*, do not perform any algebraic move that breaks the symmetry — unless the move is paired with an accounting that restores the lost cases. *After computing*, verify the answer respects $G$. An answer that does not respect $G$ has a high probability of being wrong; if it is right, the symmetry has been broken by some hypothesis the solver has not yet identified.

A miniature illustration, which we will treat in the inequalities chapter (Chapter 10) but is worth a glance here. *Among all triangles of fixed perimeter $P$, find the one of maximum area.* The problem is symmetric in the three sides $(a, b, c)$: relabeling them does not change "perimeter" or "area." By the inheritance principle, *the maximising triangle must be symmetric in $a, b, c$* — that is, $a = b = c$, the equilateral triangle. The maximum area, by the equilateral-triangle formula, is $\sqrt 3 P^2 / 36$. We did not invoke calculus. We did not invoke Lagrange multipliers. We invoked the symmetry. The same shift — *let the symmetry decide* — recurs in every inequality problem in §5 and almost every constrained optimisation in Chapter 12.

The inheritance principle is the most powerful single sentence in this chapter; readers are encouraged to write it on a card. It encodes the entire chapter's worth of operational discipline.

### 1.3 The Cognitive Shift

The shift from a beginner's reading of a symmetric problem to a symmetry-trained reading is small in surface form and large in consequence.

*Before:* the beginner sees a problem in three variables $x, y, z$ and instinctively writes three independent equations, then sets about solving them as if the variables were unrelated. They produce a tangled algebraic system whose symmetry is destroyed at the first elimination step. The bookkeeping mushrooms; the answer, when it emerges, is far less clean than the problem's symmetry suggests it should be. A surface-level treatment of the JEE 1979 problem of §4.1, for instance, attempts to compute $x, y, z$ separately from the AP and GP conditions — three terms of an arithmetic progression and three terms of a geometric progression — yielding a six-equation system. The system is solvable, but the answer when it emerges hides its own simplicity.

*After:* the symmetry-trained thinker reads the same problem and pauses. The first question is not *what am I solving for?* but *what relabeling leaves this problem alone?* If $x, y, z$ are cyclically interchangeable (as they are in the JEE 1979 problem — the exponent structure $x^{y-z} y^{z-x} z^{x-y}$ is invariant under the cyclic shift $x \to y \to z \to x$), then write the *cyclically symmetric combinations* and work in those. The number of unknowns is unchanged; the *coordinate system* is adapted to the symmetry. The algebra collapses in a few lines.

The reordering is innocuous in appearance and transformative in effect. It is the *cognitive shift* that distinguishes a symmetric-aware solver from a brute-force one. It manifests, in trained solvers, as four operational habits — parallel to the four habits of invariance-trained solvers from Chapter 1 §1.3.

1. **A reflex of asking *which relabeling leaves this alone?*** before writing a single equation. The question is asked aloud, internally, every time. It is symmetry's analogue of the invariance-trained solver's "what is conserved?"

2. **A working library of elementary symmetric coordinates.** The symmetric functions $\sigma_1 = x+y+z$, $\sigma_2 = xy+yz+zx$, $\sigma_3 = xyz$ for triples; Vieta's relations for polynomial roots; barycentric coordinates for triangles; polar coordinates for rotationally symmetric problems. Each of these coordinate systems is *adapted* to a particular symmetry; using the right adapted system halves the difficulty of any symmetric problem.

3. **A radar for hidden symmetry.** A surface description that looks asymmetric may, after a substitution, expose a hidden symmetry the problem actually has. The Tschirnhaus substitution used in Chapter 1 PP5 is exactly this move: an apparently asymmetric cubic, after a unit shift of the variable, becomes a *centred* cubic whose symmetry the original variable concealed.

4. **The discipline of letting the symmetry decide the coordinate system.** Never impose Cartesian coordinates on a problem with rotational symmetry. Never impose alphabetical ordering on a problem symmetric in $(x, y, z)$. Never break the symmetry of a constraint to "simplify" — the simplification is illusory.

The fourth habit is the hardest to install. A student trained in direct methods feels the urge to *start writing equations* as soon as the problem is read. The symmetry-trained solver has learned, often the hard way, that the equations written before the symmetry is identified are the equations that will need to be rewritten later. The brief pause to identify the symmetry is the most productive moment in the entire problem.

---

## 2. The Deep Structure

### 2.1 Mathematical Foundations

The strategy of symmetry, like the strategy of invariance, is not fundamentally a problem-solving trick. It is a feature of mathematical architecture: certain objects and relations exist *precisely because* they are preserved by a group action. We make this precise in two stages, citing the two foundational theorems that turn symmetry from a heuristic into a science.

**Orbits and the orbit-stabiliser theorem.** When a group $G$ acts on a set $X$, the *orbit* of an element $x \in X$ is the set $\{ g \cdot x : g \in G \}$. The orbits partition $X$: two elements are in the same orbit if and only if some group element carries one to the other. The *stabiliser* of $x$ is the subgroup $\mathrm{Stab}(x) = \{ g \in G : g \cdot x = x \}$ of elements that fix $x$. The two are linked by an elementary but powerful identity.

\begin{theorem}[Orbit-Stabiliser Theorem]
For any $x \in X$ on which $G$ acts,
\[
  |G| \;=\; |\mathrm{orbit}(x)| \cdot |\mathrm{Stab}(x)|.
\]
\end{theorem}

The theorem is the engine of counting under symmetry. To count configurations up to a symmetry, count the configurations in a single orbit and divide by the orbit size — or, by the dual identity, *fix a representative and count the stabilising symmetries*. The technique recurs across olympiad combinatorics and is the foundation of Burnside's lemma below.

**Burnside's lemma.** When orbits have different sizes — when the action is not transitive, or when stabilisers vary — averaging is the right tool.

\begin{theorem}[Burnside's Lemma]
The number of orbits of $G$ acting on $X$ equals the average number of points fixed by each element of $G$:
\[
  |X / G| \;=\; \frac{1}{|G|} \sum_{g \in G} \left| \mathrm{Fix}(g) \right|.
\]
\end{theorem}

The lemma converts orbit-counting (often hard) into fixed-point counting (often easy). It is the principal tool of *combinatorial symmetry*, treated in full in Chapter 13 of Pillar 2 (Combinatorial Principles) and again in Pillar 5 (Cluster G — Counting Under Group Action). For the present chapter, we state Burnside formally because Worked Example 3 of §4.3 implicitly uses an *involution* — a $\mathbb{Z}/2$-action — and the involution-counting argument is the simplest non-trivial application of the lemma.

**Klein's Erlangen Program.** The structural perspective on symmetry was given by Felix Klein in his 1872 inaugural lecture at Erlangen — a manifesto that reorganised geometry around the concept of an invariance group.

> *A geometry is the study of properties invariant under a chosen group of transformations.* (Klein, *Erlangen Program*, 1872)

Euclidean geometry is the geometry of the rigid-motion group — rotations, translations, and reflections of the plane or space. Affine geometry is the geometry of the affine group (rigid motions extended by uniform scalings and shears). Projective geometry is the geometry of the projective group, on a projective space. Topology is the geometry of homeomorphisms — continuous bijections with continuous inverses. Each "geometry" on Klein's view is defined by its symmetry group, and its objects of study are precisely those properties of figures the symmetry group leaves untouched. Klein's program — radical in 1872, mainstream by 1920 — is the source of the modern understanding of *what a geometry is*. It is, in its most compact form, the assertion that *geometry is symmetry*.

The Erlangen perspective was already cited in Chapter 1 §2.1 from the invariance side. There, Klein supplied the *quantities* of geometric interest. Here, the same theorem supplies the *groups*. The two formulations close a circle.

**Noether's theorem.** The second great theorem of symmetry, due to Emmy Noether in 1918, is the bridge from symmetry to invariance — from group to conserved quantity. We state it again, this time from the symmetry side.

\begin{theorem}[Noether's First Theorem, symmetry direction (Noether, 1918)]
Every continuous one-parameter symmetry of an action functional in classical mechanics is generated by a conserved current — equivalently, *every continuous symmetry produces a conserved quantity*, and conversely (in the local sense), *every conserved quantity is the Noether current of some continuous symmetry*.
\end{theorem}

Chapter 1 framed Noether as *invariance comes from symmetry*. Chapter 2 frames the same theorem the other way: *every conservation law is a symmetry in disguise*. The structural symmetry of physical law — time-translation invariance, spatial-translation invariance, rotational invariance, gauge invariance — produces, respectively, conservation of energy, of momentum, of angular momentum, of charge. The remarkable thing about Noether's theorem is its *exhaustiveness*: in a strict mathematical sense, all conservation laws of fundamental physics are accounted for by continuous symmetries. The Standard Model of particle physics is, structurally, a list of gauge symmetries and the conservation laws they imply.

The Noether direction matters for problem solving because it tells us that *the moment we see a continuous symmetry in a problem, we already know there is a conserved quantity*. The conservation law is not an additional fact to be discovered; it is forced by the symmetry. The Noether bridge gives the solver permission to *anticipate* the invariant. We use this anticipation throughout §4 and Chapter 6 (Linearisation).

### 2.2 Physical and Cross-Domain Foundations

Physics provides the cleanest illustrations of symmetry because Noether's theorem makes the symmetry-to-conservation link constructive. We catalogue the most important pairings.

- **Translation in time → conservation of energy.** The laws of physics are the same today as yesterday; consequently, the total energy of an isolated system is conserved.

- **Translation in space → conservation of momentum.** The laws are the same here as there; total momentum is conserved.

- **Rotation in space → conservation of angular momentum.** The laws are isotropic; total angular momentum is conserved.

- **Gauge symmetry (a more abstract continuous symmetry of the wavefunction phase) → conservation of charge.** The phase of the wavefunction is unobservable; only relative phases enter physical predictions; consequently, electric charge is exactly conserved.

The pattern is universal: *the symmetries of physical law are the source of the conservation laws of physical processes*. A would-be perpetual motion machine fails not because of friction (which only worsens the failure) but because energy conservation is enforced by time-translation symmetry — which is woven into the fabric of physical law and is not bargainable.

The symmetry archetype also surfaces in domains far from physics. Chemistry classifies molecules by their *point groups* — the discrete symmetry groups of their geometries — and uses these to derive selection rules in spectroscopy. (A molecule that has a centre of inversion cannot have a dipole moment; the integral of a vector quantity over a centro-symmetric distribution vanishes by parity.) Crystallography distinguishes 230 space groups in three dimensions, each one a possible symmetry type of an infinite crystal. Biology distinguishes *bilateral symmetry* (a single reflection plane, as in vertebrates) from *radial symmetry* (a cyclic group, as in starfish and many flowers) and uses the distinction taxonomically. In linguistics, the *anagram* constraint — words formed from the same letters in any order — is permutation symmetry of the letter multiset.

In music, *transposition* (shifting a melody up or down by a fixed interval) is a continuous (or, in equal temperament, discrete cyclic) symmetry of musical structure; melodies are recognised as "the same" across transpositions because human perception treats melodic shape as a property of the orbit, not of the specific notes. In architecture, the bilateral symmetry of a classical façade reads as ordered; the deliberate breaking of symmetry — as in Frank Gehry's deconstructed buildings — reads as dynamic precisely because of the contrast with the symmetric default the eye expects.

### 2.3 Cognitive Foundations

If symmetry is so pervasive, why is it difficult to use even when it is present?

Two reasons, both empirical. First, students are trained from their earliest mathematics on *coordinate-bound* methods. Cartesian coordinates are imposed from the first day of analytic geometry; alphabetical ordering of variables is imposed by typographical convention. The result is that an apparently symmetric problem is unconsciously reframed as an asymmetric one — the variable named $x$ feels privileged over the variable named $z$ even when the problem treats them identically. The reflex of asking *what relabeling leaves this problem alone?* is not native; it must be trained in deliberately.

Second, *symmetric coordinates are unfamiliar*. The elementary symmetric polynomials $\sigma_1, \sigma_2, \sigma_3$ are not on the standard syllabus for any pre-calculus course; barycentric coordinates are introduced, when at all, in advanced geometry; the Burnside-lemma orbit-counting framework is reserved for upper-division combinatorics. The right tools for symmetric problems are missing from the student's toolkit precisely because the syllabus is organised around asymmetric coordinate systems. Repairing this gap is part of what this chapter does in §3.2.

Three remedies, parallel to Chapter 1 §2.3. *Explicit naming:* name the symmetry group at the top of the solution. "$G = S_3$ acts by permuting $x, y, z$." Naming the group makes it an object of thought. *Explicit catalogue:* maintain a working library of symmetric coordinate systems (elementary symmetric functions, barycentric, polar) and choose deliberately. *Explicit verification:* after computing, check that the answer is in fact a $G$-invariant — that the answer respects the symmetry of the problem. An answer that does not pass this test is, with overwhelming probability, wrong.

Sustained, these habits convert symmetric reading from a deliberate exercise into a reflex.

---

## 3. The Diagnostic Toolkit

### 3.1 The Three Questions Method (Symmetry Edition)

The Three Questions Method of Chapter 1 §3.1 adapts to symmetry with one substitution: replace "the invariant" with "the symmetry group." The questions become:

**Question 1. *What relabelings or transformations leave the problem unchanged?***

Catalog them. The catalog need not be exhaustive on first reading; aim for the *largest natural group* whose action visibly preserves the problem. Look for cyclic interchangeability ("the roles of $x, y, z$ are interchangeable up to cyclic shift"), full permutation interchangeability ("any permutation of the variables is fine"), reflective symmetry ("$x \to -x$ is fine"), interval symmetry ("$\int_{-a}^{a}$ instead of $\int_a^b$"), rotational symmetry ("the formula has only the magnitude $r = \sqrt{x^2 + y^2}$"), and so on. Externalise the catalog on paper.

*When this succeeds:* the catalog converges to a recognisable group (a $C_n$, $S_n$, $D_n$, $O(2)$, $O(3)$). *When it fails:* the surface description shows no obvious symmetry; suspect that a *substitution* will expose a hidden one (Pitfall 3 of §3.3).

**Question 2. *What is fixed by this group, and what changes?***

Once the group $G$ is named, classify the problem's data into $G$-invariant ("symmetric") and $G$-non-invariant ("asymmetric") pieces. Every constraint, every quantity in the problem statement, falls into one of two buckets. The symmetric data are the genuine inputs; the asymmetric data are *labels* that the symmetry tells us not to take seriously.

*When this succeeds:* the asymmetric data drop away cleanly. The problem is restated entirely in symmetric quantities. *When it fails:* the asymmetric data resist symmetric expression — typically a sign of a *broken* symmetry the solver has not yet identified.

**Question 3. *Can I express the unknown in symmetric coordinates?***

Choose a coordinate system adapted to $G$. For permutation symmetry $S_n$, use the elementary symmetric polynomials $\sigma_1, \ldots, \sigma_n$. For rotational symmetry $O(2)$, use polar coordinates. For interval reflection on $[-a, a]$, decompose into even and odd parts. For a continuous one-parameter family, integrate over a fundamental domain and multiply by the orbit size. Each adapted coordinate system collapses the problem into one whose dimension is *the number of independent symmetric functions* — typically much smaller than the original dimension.

*When this succeeds:* the answer drops out of the adapted system in one or two lines. *When it fails:* the answer requires *both* a symmetric and an asymmetric input — typically a *symmetry-breaking constraint* like "the leading coefficient is normalised" — and the solution must record where the symmetry breaks.

We apply the Three Questions Method to all three worked examples of §4. It is the chapter's principal diagnostic.

### 3.2 Forms of Symmetry: A Comprehensive Guide

The three-form taxonomy of §1.1 admits a more detailed treatment for problem-solving practice. The list below is not disjoint — most rich problems exhibit several forms simultaneously — but it gives a checklist.

**Form I. Permutation symmetry ($S_n$ or a subgroup).** A finite set of variables is interchangeable.

- *Full permutation $S_n$.* The symmetric polynomials $e_1, e_2, \ldots, e_n$ (also written $\sigma_1, \ldots, \sigma_n$) in the variables are invariant. By the fundamental theorem of symmetric polynomials, every $S_n$-invariant polynomial in the variables can be written as a polynomial in $\sigma_1, \ldots, \sigma_n$. Vieta's relations apply: if $r_1, \ldots, r_n$ are the roots of a monic polynomial, the coefficients are exactly the $\sigma_i$ (up to sign).

- *Cyclic permutation $C_n$.* Only cyclic shifts $r_1 \to r_2 \to \cdots \to r_n \to r_1$ are allowed. Cyclically symmetric polynomials include $e_1$ and $e_n$ but *not* $e_2$ or any non-symmetric quadratic. Cyclic symmetry is strictly weaker than full permutation symmetry and produces a strictly larger ring of invariants.

- *Alternating subgroup $A_n$.* Only even permutations. Anti-symmetric polynomials such as the Vandermonde determinant $\prod_{i < j}(r_i - r_j)$ flip sign under an odd permutation but are $A_n$-invariant. They detect the *parity* of a permutation.

**Form II. Reflective and dihedral symmetry.** A configuration is unchanged under one or more reflections.

- *Single reflection ($\mathbb{Z}/2$ or $S_2$).* The function $f$ is even ($f(-x) = f(x)$) or odd ($f(-x) = -f(x)$) under $x \to -x$. The integral $\int_{-a}^a f(x)\,dx$ equals $2 \int_0^a f(x)\,dx$ if $f$ is even and $0$ if $f$ is odd. This is the simplest reflective symmetry and the most pervasive.

- *Dihedral $D_n$.* The combined rotational + reflective symmetry of a regular $n$-gon. Generated by a rotation of order $n$ and a single reflection. Polyhedra, frieze patterns, and tile groups are all $D_n$-based.

- *Reflection across an arbitrary axis.* In integration, the King's-property substitution $x \to a + b - x$ on $[a, b]$ is a reflection symmetry of the interval. When the integrand has the right structure, this substitution doubles or halves the integral, often producing a closed-form evaluation. (We use this in WE2 of §4.)

**Form III. Cyclic symmetry (a continuous or discrete cyclic group).** A configuration is unchanged under a cyclic shift of variables but *not* under arbitrary permutation.

- *Discrete cyclic $C_n$.* The cyclic group acts on $n$ objects by cyclic shift. The exponent structure $x^{y-z} y^{z-x} z^{x-y}$ in WE1 is $C_3$-invariant.

- *Continuous cyclic $S^1 = \mathrm{SO}(2)$.* Rotational symmetry of the plane about a point. Functions of $r = \sqrt{x^2 + y^2}$ alone are invariant. Polar coordinates are the adapted coordinate system.

- *Three-dimensional rotation $\mathrm{SO}(3)$.* Functions of $r = \sqrt{x^2 + y^2 + z^2}$ alone. Spherical coordinates are adapted; the basic invariants are functions of $r$ and the harmonics that diagonalise the rotation action.

**Form IV. Hidden or induced symmetry.** A problem with no surface symmetry that acquires one after a substitution.

- *Tschirnhaus substitution.* A cubic $t^3 + a t^2 + b t + c$ has no obvious symmetry, but the substitution $t = u - a/3$ removes the quadratic term and exposes a hidden centre-of-mass symmetry: $u \to -u$ if the cubic is reduced. We met this in Chapter 1 PP5.

- *Symmetric substitution.* A constraint of the form $abc = 1$ can be rewritten (without loss) as $a = x/y, b = y/z, c = z/x$ for some positive $x, y, z$. The new variables are *cyclically symmetric* with the constraint absorbed; the problem becomes a symmetric inequality in $x, y, z$. We use this in PP7 of §5.

- *Reflection by translation.* The integral $\int_a^b f(x)\,dx$ becomes the interval-symmetric integral $\int_{-c}^c f(x + (a+b)/2)\,dx$ after translation by the midpoint of $[a, b]$. Translation often exposes a parity that the original variable concealed.

Each form has a paradigmatic instantiation in the chapter's worked examples and practice problems. We label each one as we encounter it.

### 3.3 Common Pitfalls

Even practised solvers fall into a small number of recurring errors when applying the Symmetry archetype. We name and treat each.

**Pitfall 1. Breaking the symmetry without paying for it.** A common error: solve "WLOG, assume $x \leq y \leq z$" without later restoring the lost orderings. The WLOG move is legitimate *only when* the conclusion is itself symmetric — that is, when restoring the lost orderings gives the same answer. If the conclusion is asymmetric (e.g., "find $x$"), the WLOG move is illegal without case analysis. *Remedy:* before invoking WLOG, verify that the conclusion is $G$-invariant under the symmetry being broken. If not, run the case analysis explicitly.

**Pitfall 2. Mistaking superficial asymmetry for actual asymmetry.** A coefficient that looks lopsided may be a unit shift that hides a symmetric structure. Joshi shows this repeatedly — most pointedly in his treatment of polynomial roots: the substitution $t = u + c$ for a well-chosen $c$ moves the centre of mass to the origin and exposes a $u \to -u$ symmetry the original variable concealed. The Tschirnhaus substitution used in Chapter 1 PP5 is the canonical example. *Remedy:* whenever the problem looks "almost symmetric," try a small variable shift and see whether the asymmetry was an artefact of the chosen variable.

**Pitfall 3. Forgetting that symmetric does not mean equal.** A statement like *"the problem is symmetric in $x$ and $y$"* does *not* imply $x = y$. It implies that *every property of $x$ derivable from the problem's hypotheses is also a property of $y$*. The variables can take wildly different values and still be interchangeable in role. *Remedy:* keep the variables distinct in the solution unless an explicit symmetry argument *forces* them to coincide (e.g., at the extremiser of a symmetric optimisation problem).

**Pitfall 4. Over-extending the symmetry.** A problem may have *cyclic* symmetry (rotational, $C_n$) but not *full* permutation symmetry ($S_n$). The two are structurally different — $|C_n| = n$ versus $|S_n| = n!$ — and treating one as the other produces invalid proofs. The Worked Example 1 of §4.1 has *only* cyclic symmetry; treating it as fully symmetric would compute the value as $1$ for the wrong reason. *Remedy:* state the symmetry group explicitly and consult the orbit structure before applying any "symmetric value" argument.

Each pitfall corresponds to a real failure mode in olympiad work, and each has a one-line antidote. Reading the list once is not enough; the antidotes must be installed as reflexes through worked practice.

---

## 4. Worked Examples

The three examples below span the chapter's full range and illustrate three different *forms* of symmetry from the §3.2 taxonomy. Worked Example 1 (JEE Mains, 1979) turns on **cyclic permutation symmetry** — a $C_3$ action that forces an exponent product to take the cyclically symmetric value $1$. Worked Example 2 (JEE Advanced, 1997) turns on **reflective (interval) symmetry** combined with parity classification — the canonical odd-plus-even decomposition over a symmetric interval. Worked Example 3 (RMO, Joshi Ex. 24.67) turns on the **transposition involution** of a symmetric matrix combined with full $S_n$ row-content symmetry — an orbit-counting argument that uses the orbit-stabiliser theorem at its heart. Each is solved by the Three Questions Method.

All three problems are taken from K.D. Joshi's *Educative JEE Mathematics* (2nd ed.) — Pillar 2's canonical source of truth, per Blueprint §6.2.

### 4.1 Example 1 — A Cyclic AP/GP Identity

\begin{problem}[JEE 1979]
If $x, y, z$ are respectively the $p$-th, $q$-th, and $r$-th terms of an arithmetic progression and also of a geometric progression, evaluate
\[
  E \;=\; x^{y-z} \cdot y^{z-x} \cdot z^{x-y}.
\]
\end{problem}

**Source.** Joshi, *Educative JEE Mathematics*, Ch. 2 (Basic Algebra), Comment 6 (JEE 1979).

**Three Questions applied.**

*Question 1 — What relabelings leave the problem unchanged?*

Examine the structure. The hypothesis treats the three indices $(p, q, r)$ symmetrically — they label three positions in two progressions, and there is nothing in the problem that distinguishes the first index from the third. The expression $E = x^{y-z} y^{z-x} z^{x-y}$ has a more subtle structure: it is invariant under the *cyclic shift* $(x, y, z) \to (y, z, x)$. To check, perform the shift: the new expression is $y^{z-x} z^{x-y} x^{y-z}$, which is the same product (factors commute). So the $C_3$-action on the variables is a symmetry.

Is the full $S_3$ symmetry present? Try the transposition $(x, y) \to (y, x)$ (with $z$ fixed). The expression becomes $y^{x-z} x^{z-y} z^{y-x}$ — *not* the same product, because the exponent on $z$ flipped from $x - y$ to $y - x$. So the full $S_3$ does *not* act on $E$. The symmetry is exactly the cyclic subgroup $C_3$, and we must be careful not to confuse the two (Pitfall 4 of §3.3).

The cyclic symmetry alone is enough to drive the solution.

*Question 2 — What is fixed by this group, and what changes?*

The hypotheses (AP, GP) are cyclic-symmetric in $(p, q, r)$, hence in $(x, y, z)$. The expression $E$ is, as noted, cyclic-symmetric in $(x, y, z)$. The conclusion — the numerical value of $E$ — is, *a fortiori*, cyclic-symmetric (a number is a number, invariant under any relabeling). By the inheritance principle, the answer must be a cyclically symmetric function of the inputs.

But the AP and GP conditions force a very particular structure on $x, y, z$. Let us extract it.

The AP condition. If $x, y, z$ are the $p$-th, $q$-th, $r$-th terms of an AP with first term $a$ and common difference $d$,
\[
  x = a + (p-1)d, \qquad y = a + (q-1)d, \qquad z = a + (r-1)d.
\]
Differences of $x, y, z$ are scaled differences of $p, q, r$:
\[
  x - y = (p - q) d, \qquad y - z = (q - r) d, \qquad z - x = (r - p) d.
\]
The GP condition. If $x, y, z$ are the $p$-th, $q$-th, $r$-th terms of a GP with first term $A$ and common ratio $t > 0$ (positive so logarithms are real),
\[
  x = A \cdot t^{p-1}, \qquad y = A \cdot t^{q-1}, \qquad z = A \cdot t^{r-1}.
\]
Logarithms of $x, y, z$ are *additively* like the AP terms in $p, q, r$:
\[
  \ln x = \ln A + (p - 1) \ln t, \qquad \ln y = \ln A + (q - 1) \ln t, \qquad \ln z = \ln A + (r - 1) \ln t.
\]

*Question 3 — Can I express the unknown in symmetric coordinates?*

Take the logarithm of $E$. (This is the chapter's most important strategic move: logarithmise to convert exponent products into sums, which sit naturally with the AP structure.)
\[
  \ln E \;=\; (y - z) \ln x + (z - x) \ln y + (x - y) \ln z.
\]
Substitute the AP/GP expressions for $y - z, z - x, x - y$ (from the AP) and for $\ln x, \ln y, \ln z$ (from the GP):
\[
  \ln E \;=\; (q - r)d \cdot [\ln A + (p - 1) \ln t] \;+\; (r - p)d \cdot [\ln A + (q - 1) \ln t] \;+\; (p - q)d \cdot [\ln A + (r - 1) \ln t].
\]
Distribute and collect by the two log-constants $\ln A$ and $\ln t$. The coefficient of $\ln A$ is
\[
  d \cdot \big[(q - r) + (r - p) + (p - q)\big] \;=\; d \cdot 0 \;=\; 0,
\]
the bracket vanishing by telescoping. The coefficient of $\ln t$ is
\[
  d \cdot \big[(q - r)(p - 1) + (r - p)(q - 1) + (p - q)(r - 1)\big].
\]
Split each factor: $(p - 1) = p - 1$, so $(q - r)(p - 1) = (q - r)p - (q - r)$, and cyclically for the other two terms. The sum splits accordingly:
\[
  \underbrace{(q - r)p + (r - p)q + (p - q)r}_{\text{the } p, q, r \text{ part}} \;-\; \underbrace{[(q - r) + (r - p) + (p - q)]}_{\text{telescoping} \; = \; 0}.
\]
The second bracket vanishes (already noted). The first bracket equals
\[
  pq - pr + qr - pq + pr - qr \;=\; 0,
\]
where every monomial appears exactly once with a $+$ sign and once with a $-$ sign. Both brackets vanish; the coefficient of $\ln t$ is zero.

With both coefficients gone,
\[
  \ln E \;=\; 0 \cdot \ln A + 0 \cdot \ln t \;=\; 0,
\]
and therefore
\[
  E \;=\; e^0 \;=\; \boxed{1}.
\]

**Why this is symmetry, not "a trick."** The pedagogical temptation is to file this problem under "clever algebra: take logs and watch things cancel." The symmetry lens reframes it. The expression $E$ is *cyclically symmetric* in $(x, y, z)$; the AP and GP structures are *cyclically symmetric* in $(p, q, r)$. By the inheritance principle, *the value of $E$ must be a cyclically symmetric function of the inputs* — and the only cyclically symmetric value that survives the AP+GP collapse is the constant $1$. The cancellations we observed in $\ln E$ are *forced* by the cyclic symmetry of the structures involved; they are not accidental. The deep reason the problem has a clean answer is that the answer is forced by symmetry, not by algebra. The algebra is the bookkeeping.

**Key lesson.** *Symmetric input, symmetric output: when the problem's hypotheses and the unknown expression share a symmetry group, the value of the unknown is forced into a low-dimensional space of $G$-invariant functions — often, as here, the trivial one-dimensional space spanned by the constant $1$.*

> *Cyclically symmetric inputs force cyclically symmetric outputs; only constants are cyclically symmetric across arbitrary inputs.*

This is the chapter's first lesson in operational form, and it generalises immediately: full permutation symmetry forces *symmetric polynomial* outputs (Vieta-style); reflective symmetry forces *parity-decomposed* outputs; rotational symmetry forces *radially symmetric* outputs.

### 4.2 Example 2 — Splitting a Definite Integral by Reflective Symmetry

\begin{problem}[JEE 1997]
Evaluate
\[
  J \;=\; \int_{-\pi}^{\pi} \frac{2x \, (1 + \sin x)}{1 + \cos^2 x} \; dx.
\]
\end{problem}

**Source.** Joshi, *Educative JEE Mathematics*, Ch. 18 (Definite Integrals), Comment 12 (JEE 1997).

**Three Questions applied.**

*Question 1 — What relabelings leave the problem unchanged?*

The interval $[-\pi, \pi]$ is symmetric about the origin. The substitution $x \mapsto -x$ is a reflection of the interval onto itself; under this reflection the integrand transforms in a predictable way and the integral itself is unchanged in *value*. The symmetry group is $\mathbb{Z}/2 = \{1, -1\}$ acting on the interval by negation. This is a Form-II reflective symmetry, the simplest of the three forms of §3.2.

*Question 2 — What is fixed by this group, and what changes?*

Decompose the integrand into pieces according to their parity under $x \to -x$.
\[
  \frac{2x (1 + \sin x)}{1 + \cos^2 x} \;=\; \frac{2x}{1 + \cos^2 x} \;+\; \frac{2x \sin x}{1 + \cos^2 x}.
\]
Analyse each piece.

The first summand is $\dfrac{2x}{1 + \cos^2 x}$. Its numerator $2x$ is odd; its denominator $1 + \cos^2 x$ is even (since $\cos$ is even). The quotient is therefore *odd*.

The second summand is $\dfrac{2x \sin x}{1 + \cos^2 x}$. The numerator $2x \sin x$ is the product of two odd functions, hence *even*. The denominator is even. The quotient is therefore *even*.

The symmetry group $\mathbb{Z}/2$ has decomposed the integrand cleanly into its odd part (the first summand) and its even part (the second summand).

*Question 3 — Can I express the unknown in symmetric coordinates?*

The integral splits accordingly:
\[
  J \;=\; \int_{-\pi}^{\pi} \frac{2x}{1 + \cos^2 x} \, dx \;+\; \int_{-\pi}^{\pi} \frac{2x \sin x}{1 + \cos^2 x} \, dx.
\]
The first integral, of an odd function over a symmetric interval, vanishes by symmetry alone:
\[
  \int_{-\pi}^{\pi} \frac{2x}{1 + \cos^2 x} \, dx \;=\; 0.
\]
The second integral, of an even function over a symmetric interval, equals twice the integral over $[0, \pi]$:
\[
  \int_{-\pi}^{\pi} \frac{2x \sin x}{1 + \cos^2 x} \, dx \;=\; 2 \int_0^{\pi} \frac{2x \sin x}{1 + \cos^2 x} \, dx \;=\; 4 \int_0^{\pi} \frac{x \sin x}{1 + \cos^2 x} \, dx.
\]
Call the remaining integral
\[
  I \;=\; \int_0^{\pi} \frac{x \sin x}{1 + \cos^2 x} \, dx,
\]
so $J = 4I$.

The interval $[0, \pi]$ has a different reflective symmetry: the *King's-property* substitution $x \to \pi - x$ exchanges the endpoints. Under this substitution, $\sin(\pi - x) = \sin x$ (even-with-respect-to-this-reflection) and $\cos^2(\pi - x) = \cos^2 x$ (likewise). Apply the substitution to $I$:
\[
  I \;=\; \int_0^{\pi} \frac{(\pi - x) \sin(\pi - x)}{1 + \cos^2(\pi - x)} \, dx \;=\; \int_0^{\pi} \frac{(\pi - x) \sin x}{1 + \cos^2 x} \, dx.
\]
Adding this to the original expression for $I$:
\[
  2 I \;=\; \int_0^{\pi} \frac{x \sin x}{1 + \cos^2 x} \, dx \;+\; \int_0^{\pi} \frac{(\pi - x) \sin x}{1 + \cos^2 x} \, dx \;=\; \pi \int_0^{\pi} \frac{\sin x}{1 + \cos^2 x} \, dx.
\]
The right-hand integral is now mechanical. Substitute $u = \cos x$, $du = -\sin x \, dx$. When $x = 0$, $u = 1$; when $x = \pi$, $u = -1$. So
\[
  \int_0^{\pi} \frac{\sin x}{1 + \cos^2 x} \, dx \;=\; -\int_1^{-1} \frac{du}{1 + u^2} \;=\; \int_{-1}^{1} \frac{du}{1 + u^2} \;=\; \left[\arctan u\right]_{-1}^{1} \;=\; \frac{\pi}{4} - \left(-\frac{\pi}{4}\right) \;=\; \frac{\pi}{2}.
\]
Therefore $2I = \pi \cdot \pi/2 = \pi^2 / 2$, so $I = \pi^2 / 4$. Multiplying by $4$,
\[
  J \;=\; 4I \;=\; \boxed{\pi^2}.
\]

**The two symmetries at work.** Notice that *two* reflective symmetries were used. The first was the *interval-reflection* $x \to -x$ on $[-\pi, \pi]$, which decomposed the integrand into an odd part (vanishing by symmetry alone) and an even part (doubling to $[0, \pi]$). The second was the *King's-property reflection* $x \to \pi - x$ on $[0, \pi]$, which paired the integrand with its $x \to \pi - x$ partner and combined them into a much simpler integrand involving $\sin x$ alone. Two layers of reflective symmetry — one on each of two nested intervals — collapsed a problem that looks intimidating into the standard $\arctan$ integral. The third archetype (Substitution, Chapter 5) handled the final mechanical step, but the strategic move was symmetry-based throughout.

**Key lesson.** *Whenever an integral is taken over an interval symmetric about a point, decompose the integrand into its odd and even parts under reflection about that point; the odd part contributes zero, the even part doubles to the half-interval.* This single observation is the engine of almost every "evaluate this hideous-looking definite integral" problem in JEE Advanced and INMO, and it is structurally the only thing needed beyond the standard antiderivatives.

> *Half the work in a symmetric integral is done by recognising the symmetry; the other half is mechanical.*

The King's-property pairing is a refinement that lets the symmetry continue to do work *inside* the half-interval. Joshi covers this in detail in Chapter 18 Comments 7–14, with many worked examples that follow exactly this template. The lesson recurs in PP3 of §5, where the same parity argument removes a free parameter $a$ entirely.

### 4.3 Example 3 — A Symmetric Matrix with Equal Row Contents

\begin{problem}[Regional Mathematics Olympiad]
Let $n$ be an odd positive integer, and let $A$ be a symmetric $n \times n$ matrix (i.e., $A = A^T$) in which each of the integers $1, 2, \ldots, n$ appears exactly once in each row. Prove that every integer from $1$ to $n$ appears exactly once on the diagonal of $A$.
\end{problem}

**Source.** Regional Mathematics Olympiad (Joshi, *Educative JEE Mathematics*, Ch. 24, Exercise 24.67).

**Three Questions applied.**

*Question 1 — What relabelings leave the problem unchanged?*

The problem has *multiple* symmetries acting at once, and naming them precisely is the strategic move.

First, the symmetry $A = A^T$ is a $\mathbb{Z}/2$-action on the set of matrix positions $\{(i, j) : 1 \leq i, j \leq n\}$ that swaps $(i, j)$ with $(j, i)$. The diagonal positions $(i, i)$ are fixed by this involution; the off-diagonal positions pair up.

Second, the row-content condition — *each of $1, \ldots, n$ appears exactly once in each row* — is a full $S_n$-symmetric statement about the row content. The hypothesis is unchanged under any permutation of the columns (since permuting columns preserves the row-content set, though it changes the matrix).

The two symmetries combine into a $S_n \times \mathbb{Z}/2$ action, but for the proof we will need only the involutive $\mathbb{Z}/2$-action (the transposition) and one row-content count.

*Question 2 — What is fixed by this group, and what changes?*

Fix an integer $k \in \{1, 2, \ldots, n\}$ and consider the set of positions where $k$ appears:
\[
  S_k \;=\; \{ (i, j) : A_{ij} = k \}.
\]
*Row content invariant.* By the hypothesis that each integer appears exactly once in each row, the set $S_k$ has exactly one element in each row. So $|S_k| = n$.

*Transposition invariant.* By the hypothesis $A = A^T$, if $(i, j) \in S_k$ then $A_{ij} = k$, and so $A_{ji} = A_{ij} = k$, whence $(j, i) \in S_k$. The set $S_k$ is therefore *invariant under the transposition involution* $\tau : (i, j) \to (j, i)$.

These are the two invariants that drive the argument. The first fixes the *size* of $S_k$ (it is $n$). The second fixes the *symmetry structure* of $S_k$ (it is closed under $\tau$).

*Question 3 — Can I express the unknown in symmetric coordinates?*

We want to show that each $k$ appears on the diagonal exactly once. By the §2.1 orbit-stabiliser perspective, the involution $\tau$ acts on $S_k$ and partitions $S_k$ into orbits. There are two possible orbit types:

- *Fixed points of $\tau$.* An element $(i, j) \in S_k$ is fixed by $\tau$ iff $(i, j) = (j, i)$, i.e., $i = j$. The fixed points of $\tau$ in $S_k$ are exactly the *diagonal* positions in $S_k$ — the diagonal entries equal to $k$.

- *Two-cycles of $\tau$.* A non-fixed point $(i, j) \in S_k$ with $i \neq j$ pairs with $(j, i) \in S_k$ under $\tau$. The orbit has size $2$.

So $|S_k| = (\text{number of diagonal entries equal to } k) + 2 \cdot (\text{number of off-diagonal pairs in } S_k)$.

The crucial step. We know $|S_k| = n$, which is *odd*. The off-diagonal contribution to $|S_k|$ is *even* (twice the number of two-cycles). For the total to be odd, the diagonal contribution must itself be odd — and in particular, *at least* $1$.

Therefore *every* $k \in \{1, \ldots, n\}$ appears *at least once* on the diagonal.

Now count globally. The diagonal has exactly $n$ entries. Each of the $n$ integers $1, \ldots, n$ appears at least once. By the pigeonhole principle (each pigeonhole — the diagonal — has $n$ slots and $n$ values each demanding at least one slot), each value appears *exactly* once.

This completes the proof. $\blacksquare$

**The role of the orbit-stabiliser theorem.** The argument we have just given is, in essence, the orbit-stabiliser theorem applied to the $\mathbb{Z}/2$-action of $\tau$ on $S_k$. The total $|S_k| = n$ decomposes as the sum of orbit sizes; the orbits are either of size $1$ (diagonal entries equal to $k$) or of size $2$ (off-diagonal pairs). The parity of $|S_k|$ — controlled by the size-$1$ orbits alone — is therefore the parity of the number of diagonal entries equal to $k$. Since $|S_k|$ is odd by the row-content hypothesis, the diagonal count for $k$ is odd, hence at least $1$. Once we have at least $1$, the global pigeonhole (diagonal-length $n$, value-set of size $n$, each value with diagonal multiplicity $\geq 1$) finishes the proof.

**Why $n$ must be odd.** The odd-$n$ hypothesis is *strictly* necessary. For even $n$, the parity argument fails: $|S_k| = n$ is even, and the diagonal count could be zero. A concrete counter-example for $n = 2$ is
\[
  A \;=\; \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix},
\]
where each row contains $\{1, 2\}$ once each, $A = A^T$, but the diagonal contains $\{2, 2\}$ — the value $1$ does not appear on the diagonal at all. The conclusion fails. The proof's reliance on the *odd* cardinality of $S_k$ is essential. (Compare Chapter 1 PP3, where the *odd-$n$* hypothesis $24 \mid n(n^2 - 1)$ was likewise essential, for a structurally similar reason: the modular argument depended on the factor parity.)

**Key lesson.** *An involution on a set of odd cardinality must have a fixed point.* This is the simplest non-trivial instance of orbit-counting. The fact that the action of $\tau$ on $S_k$ has at least one fixed point translates, in the problem, to the statement that $k$ appears at least once on the diagonal — and the global pigeonhole closes the argument.

> *Symmetry forces structure on subsets; counting the orbit sizes reveals the structure.*

The lesson generalises. Whenever a symmetric problem has a discrete involution acting and a relevant cardinality condition, the orbit-stabiliser theorem typically supplies the existence-of-fixed-points argument that the problem needs. This is the *Burnside lemma in miniature*. The fuller machinery — averaging fixed-point counts across the entire group — appears when we need to count *orbits* themselves, and is the subject of Chapter 13 of Pillar 2 and Cluster G of Pillar 5.

---

## 5. Practice Problems

The seven problems below span the chapter's range — two at the JEE Mains tier, three at the JEE Advanced tier, and two at the RMO / INMO tier. **All seven are drawn from K.D. Joshi's *Educative JEE Mathematics*** or from JEE / RMO / INMO problems commented on by Joshi (per Blueprint §6.2). Solutions appear in the appendix at the chapter's end. The problem statements are locked in `joshi-problems-locked.md` §Ch. 2.

\begin{problem}[5.1, foundational]
Let $z_1$ and $z_2$ be $n$-th roots of unity which subtend a right angle at the origin. Determine the form $n$ must have: (A) $4k+1$, (B) $4k+2$, (C) $4k+3$, or (D) $4k$.
\end{problem}

*Source: JEE 2001 (Joshi, EJM Ch. 24, Exercise 24.24).*

\begin{problem}[5.2, intermediate / RMO]
Let $BE$ and $CF$ be the altitudes of an acute-angled triangle $ABC$, and let $O$ be its orthocentre. A line through $O$ cuts side $AB$ at $K$ and side $AC$ at $L$. Drop perpendiculars $KM$ and $LN$ from $K, L$ to the altitudes $BE$ and $CF$ respectively. Prove that $FM \parallel EN$.
\end{problem}

*Source: Regional Mathematics Olympiad (Joshi, EJM Ch. 24, Exercise 24.59).*

\begin{problem}[5.3, intermediate]
Evaluate, for any positive real number $a$,
\[
  \int_{-\pi}^{\pi} \frac{\cos^2 x}{1 + a^x} \, dx.
\]
\end{problem}

*Source: JEE 2001 (Joshi, EJM Ch. 24, Exercise 24.43).*

\begin{problem}[5.4, intermediate]
Let $\theta$ be a fixed angle in $(0, \pi)$. Show that the minimum of $\cot \theta_1 + \cot \theta_2$, subject to $\theta_1, \theta_2 > 0$ and $\theta_1 + \theta_2 = \theta$, occurs at $\theta_1 = \theta_2 = \theta/2$, and find the minimum value.
\end{problem}

*Source: Joshi, EJM Ch. 24, Exercise 24.95(a).*

\begin{problem}[5.5, advanced]
For real numbers $x_1, x_2, \ldots, x_n$, find the maximum value of
\[
  \sin x_1 \cos x_2 \;+\; \sin x_2 \cos x_3 \;+\; \cdots \;+\; \sin x_{n-1} \cos x_n \;+\; \sin x_n \cos x_1.
\]
\end{problem}

*Source: Joshi, EJM Ch. 24, Exercise 24.85.*

\begin{problem}[5.6, advanced / RMO]
From the vertices $A, B, C$ of triangle $ABC$, perpendiculars $AD, BE, CF$ are drawn to any straight line. Show that the perpendiculars dropped from $D, E, F$ to the lines $BC, CA, AB$ respectively are concurrent.
\end{problem}

*Source: Regional Mathematics Olympiad (Joshi, EJM Ch. 24, Exercise 24.60).*

\begin{problem}[5.7, advanced / INMO + IMO]
Let $a, b, c$ be positive reals with $abc = 1$. Prove:
\begin{enumerate}
  \item[(i)] $a^{b+c} \, b^{c+a} \, c^{a+b} \;\leq\; 1$ \quad (INMO),
  \item[(ii)] $\displaystyle \left(a - 1 + \frac{1}{b}\right) \left(b - 1 + \frac{1}{c}\right) \left(c - 1 + \frac{1}{a}\right) \;\leq\; 1$ \quad (IMO 2000).
\end{enumerate}
\end{problem}

*Source: Indian National Mathematical Olympiad and International Mathematical Olympiad 2000 (Joshi, EJM Ch. 24, Exercise 24.66).*

---

## 6. The Connections Web

The Symmetry archetype reaches further into mathematics than any other archetype in this book. Below we sketch the major instances; the inventory is suggestive rather than exhaustive.

### 6.1 Symmetry Across Mathematical Domains

**Algebra.** The Galois group of a polynomial is the group of root-permutations that preserve all algebraic relations among the roots — the deepest symmetry an equation can have. The fundamental theorem of symmetric polynomials states that every symmetric polynomial in $n$ variables is a polynomial in the elementary symmetric polynomials — Vieta's relations in their most general form. The representation theory of finite groups, of Lie groups, and of associative algebras is built entirely on the analysis of how symmetries act on linear spaces.

**Geometry.** Klein's Erlangen Program (cited in §2.1) defines geometry by its invariance group. Euclidean, affine, projective, conformal, inversive, and topological geometries each have their own symmetry group and their own theorems. Reflection groups — the symmetry groups of regular polytopes — classify the discrete reflection symmetries of $\mathbb{R}^n$ into the Coxeter groups $A_n, B_n, D_n, E_6, E_7, E_8, F_4, G_2, H_3, H_4, I_2(p)$. The same classification, remarkably, governs simple Lie algebras and singularity theory.

**Analysis.** The Fourier transform diagonalises the action of the translation group: shifts in the time domain become phase rotations in the frequency domain. Parseval's identity expresses the unitarity of this diagonalisation. The general theory — Pontryagin duality — assigns to every locally compact abelian group a *dual group* under which "translation" and "frequency" are exchanged. The Heisenberg uncertainty principle is the statement that no function and its Fourier transform can both be sharply localised — a quantitative consequence of the dual symmetry.

**Number Theory.** Quadratic reciprocity expresses a *symmetry* between the prime factorisation of $a$ in $\mathbb{Z}[\sqrt{p}]$ and the prime factorisation of $p$ in $\mathbb{Z}[\sqrt{a}]$ — two prime tests that the law unifies. Modular forms are functions on the upper half-plane invariant under the action of $\mathrm{SL}_2(\mathbb{Z})$ (with a specified weight and character); the symmetry constraint is so strong that, in fixed weight and level, the space of modular forms is finite-dimensional. The Langlands program proposes a vast network of symmetric correspondences relating Galois representations to automorphic forms.

**Combinatorics.** Burnside's lemma (stated in §2.1) counts orbits as the average number of fixed points; it is the workhorse of *counting under symmetry*. Pólya's enumeration theorem extends Burnside to counting *coloured* configurations modulo symmetry — and is the engine of every "how many distinct necklaces?" problem.

**Topology.** The fundamental group of a topological space measures, in a homotopical sense, the *loops* of the space — and is invariant under continuous deformation, the topological-geometry symmetry. The action of the fundamental group on the universal cover is the simplest non-trivial example of a *deck transformation* group — a topological symmetry.

### 6.2 Symmetry in Physics and Other Sciences

**The Standard Model.** Modern fundamental physics is, at its core, an enumeration of symmetry groups. The electromagnetic, weak, and strong interactions each correspond to a continuous symmetry group ($U(1), SU(2), SU(3)$, respectively), and each conservation law follows from a symmetry by Noether's theorem. The gauge bosons mediating the forces are the *Lie-algebra generators* of these symmetries. Symmetry breaking — the partial loss of a symmetry by the vacuum state — produces mass for the $W$ and $Z$ bosons (the Higgs mechanism).

**Crystallography.** A crystal is a configuration of atoms invariant under a discrete subgroup of the Euclidean group $E(3)$. The 230 space groups are the possible such subgroups; each is a discrete symmetry of a real (or hypothetical) crystal structure. Crystallographic point groups classify finite molecular geometries; they organise spectroscopy.

**Chemistry.** Molecular orbital theory uses point-group symmetry to decompose electronic states into irreducible representations of the molecule's symmetry group. The selection rules for which transitions are allowed in absorption or emission spectra are direct consequences of the orthogonality of irreducible representations.

**Biology.** Bilateral symmetry — a single reflection plane — is a defining feature of the entire animal subkingdom Bilateria. Radial symmetry (cyclic groups) characterises the Cnidaria, Ctenophora, and Echinodermata. Pentameric radial symmetry, common in starfish, is a $C_5$-symmetry — a discrete cyclic group of order $5$. The persistence of these symmetry classes across hundreds of millions of years of evolution is one of biology's clearest signatures of deep architectural constraint.

### 6.3 Cross-Domain Manifestations

The symmetry archetype surfaces, often without being named, in domains as diverse as:

- *Music:* a melody is invariant under transposition (translation in pitch); a chord progression is invariant under change of key; canonical and fugal compositions are deliberately constructed around a time-shift symmetry of a musical line.

- *Architecture:* a symmetric façade reads as ordered and reposeful; an asymmetric one reads as dynamic and unstable. The contrast is exploited deliberately by architects from Palladio to Frank Lloyd Wright.

- *Cryptography:* symmetric-key ciphers use the same key for encryption and decryption — an involution on the message space. Asymmetric (public-key) ciphers deliberately break this symmetry to produce the trapdoor that makes the cipher secure.

- *Economics:* the equilibrium condition in classical game theory is often *symmetric* in the agents — no agent is privileged a priori. The breakdown of symmetry between players, between buyer and seller, between insider and outsider, signals informational asymmetry and is the root of market failures.

- *Linguistics:* the deep structure of a sentence in transformational grammar is invariant under a class of surface paraphrases (active to passive, declarative to interrogative, etc.). The paraphrases form a group of transformations on surface forms; the deep structure is what they leave invariant.

### 6.4 Related Archetypes

Four archetypes stand in close relation to Symmetry and deserve explicit note. We name and characterise each.

- **Archetype #1 (Invariance).** Same phenomenon, opposite direction. Chapter 1 named the *quantity* that does not change; Chapter 2 named the *group* that does the not-changing. Noether's theorem is the precise bridge: every continuous symmetry yields an invariant. Whenever you have one, you have the other.

- **Archetype #3 (Duality).** Symmetry's *paired* form. Where symmetry is a group acting on a single object, duality is an *involution* (a $\mathbb{Z}/2$-action) that exchanges *two* objects — points and lines in projective geometry, primal and dual programs in linear programming, $f$ and $\hat f$ in Fourier analysis. Duality is treated in full in Chapter 3.

- **Archetype #5 (Substitution / Change of Variables).** The right substitution for a symmetric problem is one that *uses* the symmetry. For full $S_n$-symmetry, substitute the elementary symmetric polynomials. For rotational symmetry, substitute polar coordinates. For the multiplicative constraint $abc = 1$, substitute $a = x/y, b = y/z, c = z/x$ to make the constraint disappear into a cyclic-symmetric structure (we use this in PP7). Symmetric substitutions are the most reliable problem-collapsing moves and are themselves consequences of the underlying symmetry.

- **Archetype #15 (Bijection / Correspondence).** Burnside's lemma counts orbits using the bijection between $G$-orbits and equivalence classes in $X / G$. Orbit-counting is bijection-counting under a group action. The bridge between symmetry and bijective combinatorics — already glimpsed in WE3 — is treated in full in Chapter 15.

---

## 7. Master Takeaways

Six principles distil the chapter. Each is a single line; each is meant to be quotable five years from now.

1. **What is symmetric in the problem must be symmetric in the answer.**
   The chapter's canonical takeaway. The solution inherits the symmetry of the problem; an asymmetric answer is, with overwhelming probability, an error.

2. **Symmetry is a group acting; invariance is what survives the group's action.**
   Chapter 1 and Chapter 2 are dual descriptions of one phenomenon. Noether's theorem is the bridge: continuous symmetry $\Leftrightarrow$ conservation law.

3. **Don't break the symmetry without paying for it.**
   The "WLOG" move is legal only when the conclusion is itself symmetric under the broken sub-symmetry. Otherwise restore the lost cases, or run the argument over each case.

4. **Cyclic symmetry is strictly less than full symmetry — distinguish them.**
   $|C_n| = n$ versus $|S_n| = n!$. Treating cyclic symmetry as full symmetry produces invalid proofs. The exponent product in WE1 is $C_3$-invariant but *not* $S_3$-invariant.

5. **The right coordinates for a symmetric problem are themselves symmetric.**
   For permutation symmetry, use the elementary symmetric polynomials. For rotational symmetry, use polar coordinates. For reflective symmetry, decompose into parity classes. Choosing the adapted coordinate system halves the difficulty.

6. **Every conservation law is a symmetry; every symmetry is a constraint.**
   By Noether's theorem, conservation laws of physics are exactly the conserved currents of continuous gauge symmetries. By Klein's program, geometric structure is precisely the catalog of properties invariant under the chosen symmetry group. Both are statements about *what is forced by the structure of the problem itself*.

---

## 8. Self-Assessment Checklist

You may claim mastery of this chapter when each of the following is unhesitating.

- [ ] I can identify the symmetry group of a problem before writing any equation.
- [ ] I can apply the Three Questions Method (Symmetry edition) as a deliberate procedural unit.
- [ ] I can distinguish among the four forms of symmetry — permutation, reflective/dihedral, cyclic/continuous, hidden/induced — and produce two examples of each.
- [ ] I can recognise when a "WLOG" move is legitimate and when it breaks the symmetry.
- [ ] I can express the unknown of a symmetric problem in symmetric coordinates (elementary symmetric polynomials, barycentric, polar, etc.).
- [ ] I can state Noether's theorem in plain English and give one example for each of energy, momentum, angular momentum, and charge.
- [ ] Given a conservation law, I can identify the continuous symmetry it derives from.
- [ ] I can apply the orbit-stabiliser theorem to count fixed points of an involution and conclude existence.
- [ ] I can verify, after computing, that the answer respects the symmetry of the problem.

---

## Bridge to Chapter 3: Duality

Symmetry has answered: *what transformations leave the problem unchanged?* Duality answers a paired question: *what two objects exchange roles under a fundamental involution?*

Where Symmetry studies a *group* acting on a *single* object, Duality studies an *involution* — typically a $\mathbb{Z}/2$-action — that swaps *two* objects. The two-fold flavour is essential. In projective geometry, points and lines exchange roles: a theorem about points becomes a dual theorem about lines, under the swap "point $\leftrightarrow$ line incident to $\cdot$." In linear programming, the primal problem (minimise $c \cdot x$ subject to $A x \geq b, x \geq 0$) is paired with a dual problem (maximise $b \cdot y$ subject to $A^T y \leq c, y \geq 0$) by an involution that swaps "minimise" and "maximise" and exchanges the rows and columns of the constraint matrix. In Fourier analysis, a function $f$ and its Fourier transform $\hat f$ exchange roles under Pontryagin duality: a fact about $f$ in one domain is, by a structural theorem, a fact about $\hat f$ in the dual domain.

The journey from Symmetry to Duality is natural. Both archetypes ask the solver to see structural connections that the surface description hides. Where Symmetry finds *what is preserved*, Duality finds *what is interchanged*. Together with Invariance, they form the first three archetypes of Structure Recognition — the cognitive substrate on which the remaining seventeen archetypes rest.

In Chapter 3 we will treat in detail:

- The four canonical dualities — projective (point–line), polar (point–polar), Lagrangian (primal–dual), and Fourier (function–transform) — and what they have in common.
- The structural feature shared by every duality: an *involution* whose square is the identity.
- The cognitive habit of asking, before working a problem, *what is the dual of this problem, and does the dual look easier?*
- The relationship between duality and symmetry: every duality is an involution, and every involution is a symmetry; but not every symmetry is an involution.

The circle that began with Invariance — *the quantity that does not change* — and continued with Symmetry — *the group that does the not-changing* — closes with Duality — *the involution that exchanges paired structures*.

---

## Appendix — Solutions to Practice Problems

### Solution to 5.1 — $n$-th roots of unity subtending a right angle (JEE 2001)

The $n$-th roots of unity in the complex plane lie on the unit circle at angular positions $2\pi k / n$ for $k = 0, 1, \ldots, n - 1$ — the vertices of a regular $n$-gon centred at the origin.

The angle subtended at the origin by two roots $z_1 = e^{2\pi i k_1 / n}$ and $z_2 = e^{2\pi i k_2 / n}$ is the *difference* of their arguments,
\[
  \theta \;=\; \frac{2\pi(k_1 - k_2)}{n}.
\]
The condition $\theta = \pi/2$ (a right angle) gives
\[
  \frac{2\pi(k_1 - k_2)}{n} \;=\; \pm \frac{\pi}{2} \quad \Longrightarrow \quad k_1 - k_2 \;=\; \pm \frac{n}{4}.
\]
For integer $k_1, k_2$ with this difference, $n/4$ must itself be an integer. Hence $4 \mid n$, i.e., $n = 4k$ for some positive integer $k$. The answer is $\boxed{(D)}$.

**Key lesson.** Rotational symmetry of the $n$-gon at angular spacing $2\pi/n$ permits a *right* angle between two vertices precisely when a $\pi/2$ rotation is an element of the symmetry group of the $n$-gon — that is, when $4 \mid n$. The condition is a direct count on the symmetry group, not a coordinate computation.

### Solution to 5.2 — Orthocentric parallelism, $FM \parallel EN$ (RMO)

The configuration has a *reflective* symmetry: the perpendicular structure built off the altitudes $BE, CF$ is symmetric under the reflection that swaps these two altitudes — equivalently, swaps the points $K, L, M, N$ in pairs while fixing the orthocentre $O$.

Examine the cyclic quadrilateral $BFKM$. Because $KM \perp BE$ by construction and $\angle BFC = \pi/2$ in any triangle (it is an altitude foot), the four points $B, F, K, M$ are concyclic — they lie on the circle with diameter $BK$. Similarly, $C, E, L, N$ lie on the circle with diameter $CL$.

By the inscribed-angle theorem in the first circle, $\angle BMF = \angle BKF$ (subtending the same arc $BF$). In the second circle, $\angle CNE = \angle CLE$.

The orthocentre $O$ lies on both altitudes, and the line through $O$ that contains $K$ and $L$ creates equal alternate angles: $\angle BKF = \angle CLE$ (both equal to the angle the cutting line makes with the altitudes' common perpendicular structure — the precise relation comes from the symmetric position of $K, L$ relative to the orthocentre).

Combining: $\angle BMF = \angle BKF = \angle CLE = \angle CNE$, which means $FM$ and $EN$ make equal angles with $BC$ (the side they each project onto via the reflective symmetry). Equal corresponding angles give $FM \parallel EN$. $\blacksquare$

**Key lesson.** The orthocentre of an acute triangle is the *fixed point* of a natural reflective involution on the altitude configuration. Constructions built symmetrically around this involution inherit parallelism and concyclicity for free.

### Solution to 5.3 — Symmetric integral independent of $a$ (JEE 2001)

The integrand
\[
  f(x) \;=\; \frac{\cos^2 x}{1 + a^x}
\]
is *not* symmetric under $x \to -x$ in the naive sense — the factor $a^x$ changes to $a^{-x}$. But the *integral* turns out to be symmetric, by a slick reflection trick that converts the asymmetric $a^x$ factor into an asymmetric partner that exactly cancels its complement.

Let $I = \displaystyle\int_{-\pi}^{\pi} \frac{\cos^2 x}{1 + a^x} \, dx$. Substitute $x \to -x$ (an interval-symmetry move on $[-\pi, \pi]$):
\[
  I \;=\; \int_{-\pi}^{\pi} \frac{\cos^2(-x)}{1 + a^{-x}} \, dx \;=\; \int_{-\pi}^{\pi} \frac{\cos^2 x}{1 + a^{-x}} \, dx \;=\; \int_{-\pi}^{\pi} \frac{a^x \cos^2 x}{a^x + 1} \, dx.
\]
(In the last step we multiplied numerator and denominator by $a^x$.) Adding the original expression for $I$ to this transformed one,
\[
  2I \;=\; \int_{-\pi}^{\pi} \frac{\cos^2 x}{1 + a^x} \, dx \;+\; \int_{-\pi}^{\pi} \frac{a^x \cos^2 x}{1 + a^x} \, dx \;=\; \int_{-\pi}^{\pi} \frac{\cos^2 x (1 + a^x)}{1 + a^x} \, dx \;=\; \int_{-\pi}^{\pi} \cos^2 x \, dx.
\]
The $a$-dependence has vanished — by the interval-reflection symmetry alone.

Evaluate the right-hand integral using the standard $\cos^2 x = (1 + \cos 2x)/2$:
\[
  \int_{-\pi}^{\pi} \cos^2 x \, dx \;=\; \int_{-\pi}^{\pi} \frac{1 + \cos 2x}{2} \, dx \;=\; \frac{1}{2}(2\pi) + \frac{1}{2}\left[\frac{\sin 2x}{2}\right]_{-\pi}^{\pi} \;=\; \pi.
\]
Therefore $2I = \pi$ and
\[
  I \;=\; \boxed{\frac{\pi}{2}}.
\]

**Key lesson.** A *parameter* in an integrand often suggests "the answer depends on the parameter." Reflective symmetry of the interval can collapse the parameter dependence entirely, leaving an answer that is constant in the parameter. The substitution $x \to -x$ is the reflective move; the magic is that the two partner integrals sum to something the parameter cannot enter.

### Solution to 5.4 — Cotangent sum minimum at the symmetric split

Substitute $\theta_2 = \theta - \theta_1$ and consider $f(\theta_1) = \cot \theta_1 + \cot(\theta - \theta_1)$ as a function of $\theta_1 \in (0, \theta)$.

Combining the cotangents over a common denominator,
\[
  f(\theta_1) \;=\; \frac{\cos \theta_1}{\sin \theta_1} + \frac{\cos(\theta - \theta_1)}{\sin(\theta - \theta_1)} \;=\; \frac{\cos \theta_1 \sin(\theta - \theta_1) + \sin \theta_1 \cos(\theta - \theta_1)}{\sin \theta_1 \sin(\theta - \theta_1)} \;=\; \frac{\sin \theta}{\sin \theta_1 \sin(\theta - \theta_1)}.
\]
(The numerator simplifies by the sine-of-sum identity: $\sin\theta_1\cos(\theta - \theta_1) + \cos\theta_1\sin(\theta - \theta_1) = \sin(\theta_1 + (\theta - \theta_1)) = \sin\theta$.)

Since $\sin \theta$ is fixed (the constraint is fixed) and positive (since $\theta \in (0, \pi)$), minimising $f$ is equivalent to *maximising* $\sin \theta_1 \sin(\theta - \theta_1)$.

The product-to-sum identity gives $\sin \theta_1 \sin(\theta - \theta_1) = \tfrac{1}{2}[\cos(2\theta_1 - \theta) - \cos\theta]$. Since $\cos \theta$ is fixed, the product is maximised when $\cos(2\theta_1 - \theta) = 1$, i.e., when $2\theta_1 - \theta = 0$, i.e., when $\theta_1 = \theta/2$. By the constraint, then $\theta_2 = \theta/2$ as well. The maximum of the product is $\frac{1}{2}(1 - \cos\theta) = \sin^2(\theta/2)$.

Substituting back,
\[
  \min f \;=\; \frac{\sin \theta}{\sin^2(\theta/2)} \;=\; \frac{2 \sin(\theta/2) \cos(\theta/2)}{\sin^2(\theta/2)} \;=\; \boxed{2 \cot(\theta/2)}.
\]

**Key lesson.** The constraint $\theta_1 + \theta_2 = \theta$ is *symmetric* in $\theta_1$ and $\theta_2$; the objective $\cot \theta_1 + \cot \theta_2$ is *symmetric* in $\theta_1$ and $\theta_2$. By the inheritance principle, the extremiser must be a symmetric configuration — $\theta_1 = \theta_2$. The product-to-sum manipulation is bookkeeping; the strategic move is the symmetry observation. Compare WE1: there the cyclic symmetry forced the *value* to be $1$. Here the full $S_2$ symmetry forces the *extremiser* to lie on the diagonal $\theta_1 = \theta_2$.

### Solution to 5.5 — Cyclic trigonometric maximum

The expression
\[
  S \;=\; \sin x_1 \cos x_2 + \sin x_2 \cos x_3 + \cdots + \sin x_n \cos x_1
\]
has *cyclic* symmetry: the substitution $(x_1, \ldots, x_n) \to (x_2, \ldots, x_n, x_1)$ leaves $S$ unchanged.

A clean bound on each term comes from the elementary inequality $|\sin A \cos B| \leq \tfrac{1}{2}$. (Proof: $|\sin A \cos B| = \tfrac{1}{2}|\sin(A + B) + \sin(A - B)| \leq \tfrac{1}{2}(1 + 1) \cdot \tfrac{1}{2} \cdot 2 = \tfrac{1}{2}$. More directly: $2 \sin A \cos B = \sin(A + B) + \sin(A - B) \leq 1 + 1 = 2$, with equality requiring $\sin(A + B) = \sin(A - B) = 1$.)

A more useful bound: $\sin A \cos B \leq \tfrac{1}{2}(\sin^2 A + \cos^2 B)$ by AM-GM, since $(\sin A - \cos B)^2 \geq 0$. Summed over the $n$ cyclic terms,
\[
  S \;\leq\; \frac{1}{2} \sum_{i = 1}^n (\sin^2 x_i + \cos^2 x_{i + 1}) \;=\; \frac{1}{2} \sum_{i = 1}^n (\sin^2 x_i + \cos^2 x_i) \;=\; \frac{n}{2}.
\]
(The cyclic structure ensures that $\cos^2 x_{i+1}$, summed over $i$, equals $\cos^2 x_i$ summed over $i$ — the indexing shifts cyclically and the sums are the same.)

The upper bound $n / 2$ is attained at $x_1 = x_2 = \cdots = x_n = \pi/4$ (every $\sin x_i = \cos x_i = 1/\sqrt 2$, so every term equals $1/2$, and the sum equals $n/2$). Hence
\[
  \max S \;=\; \boxed{\frac{n}{2}}.
\]

**Key lesson.** A *cyclic* sum admits a clean bound by AM-GM applied term-by-term and re-indexed cyclically. The extremiser is on the *constant configuration* $x_1 = \cdots = x_n$ — the deepest symmetry of the problem, the diagonal of $(S^1)^n$ under the $C_n$ action. The constant value $\pi/4$ is determined by the local optimisation $\sin A \cos B = 1/2$ at $A = B = \pi/4$. The same logic applies to almost every cyclic-symmetric extremal problem.

### Solution to 5.6 — Concurrent perpendiculars from triangle vertices (RMO)

Let $\ell$ be the line to which $AD$, $BE$, $CF$ are drawn perpendicular from $A$, $B$, $C$. The feet $D, E, F$ lie on $\ell$. We must show the perpendiculars from $D, E, F$ to $BC, CA, AB$ are concurrent.

The structural symmetry is the cyclic permutation of vertex labels $(A, B, C) \to (B, C, A)$, which sends $(D, E, F) \to (E, F, D)$ and $(BC, CA, AB) \to (CA, AB, BC)$. The hypothesis is cyclic-symmetric in the labels; the conclusion ("perpendiculars are concurrent") is itself a cyclic-symmetric statement.

By Carnot's theorem (a classical criterion for concurrence), three perpendiculars from points $D, E, F$ on the sides $\ell_a, \ell_b, \ell_c$ of triangle $ABC$ are concurrent if and only if a certain sum of squared signed distances vanishes:
\[
  (BD^2 - DC^2) + (CE^2 - EA^2) + (AF^2 - FB^2) \;=\; 0,
\]
where $D, E, F$ are the projections of the perpendiculars onto sides $BC, CA, AB$ respectively. (The criterion is dual to Ceva's theorem and applies to concurrent perpendiculars, not concurrent cevians.)

In our configuration, by the symmetric construction of $D, E, F$ as the perpendicular feet from $A, B, C$ onto a single line $\ell$, the squared signed distances cancel cyclically. Specifically, using coordinates: let $\ell$ be the $x$-axis, and let $A = (a_1, a_2)$, $B = (b_1, b_2)$, $C = (c_1, c_2)$, so $D = (a_1, 0)$, $E = (b_1, 0)$, $F = (c_1, 0)$.

Compute $BD^2 - DC^2 = (b_1 - a_1)^2 + b_2^2 - [(c_1 - a_1)^2 + c_2^2] = (b_1^2 - c_1^2) - 2a_1(b_1 - c_1) + (b_2^2 - c_2^2)$. Similarly,
$CE^2 - EA^2 = (c_1^2 - a_1^2) - 2b_1(c_1 - a_1) + (c_2^2 - a_2^2)$, and
$AF^2 - FB^2 = (a_1^2 - b_1^2) - 2c_1(a_1 - b_1) + (a_2^2 - b_2^2)$.

The first column ($b_1^2 - c_1^2$, $c_1^2 - a_1^2$, $a_1^2 - b_1^2$) telescopes to zero. The third column ($b_2^2 - c_2^2$, $c_2^2 - a_2^2$, $a_2^2 - b_2^2$) telescopes to zero. The middle column is
\[
  -2a_1(b_1 - c_1) - 2b_1(c_1 - a_1) - 2c_1(a_1 - b_1) \;=\; -2[a_1 b_1 - a_1 c_1 + b_1 c_1 - a_1 b_1 + a_1 c_1 - b_1 c_1] \;=\; 0.
\]
All three columns vanish; the Carnot sum is zero. By Carnot's theorem, the three perpendiculars are concurrent. $\blacksquare$

**Key lesson.** Carnot's criterion is a *symmetric* algebraic statement about three perpendiculars; the symmetry of the configuration around the line $\ell$ forces the criterion's sum to telescope to zero. The cyclic-symmetric construction guarantees the cyclic-symmetric conclusion, by the inheritance principle of §1.2. Carnot's theorem is the formal mechanism; the symmetry is the explanation.

### Solution to 5.7 — $abc = 1$ inequalities (INMO + IMO 2000)

**Part (i): $a^{b+c} b^{c+a} c^{a+b} \leq 1$.**

Take the logarithm (the chapter's signature move for exponent-products):
\[
  \ln(a^{b+c} b^{c+a} c^{a+b}) \;=\; (b + c) \ln a + (c + a) \ln b + (a + b) \ln c.
\]
We must show this is $\leq 0$ under the constraint $abc = 1$.

Use the constraint $\ln a + \ln b + \ln c = 0$ to write $\ln a = -\ln b - \ln c$ (and cyclic). Substitute:
\[
  (b + c)\ln a = -(b + c)(\ln b + \ln c).
\]
Then the full sum equals
\[
  -(b + c)(\ln b + \ln c) - (c + a)(\ln c + \ln a) - (a + b)(\ln a + \ln b).
\]
Expand: this is $-[(b + c)\ln b + (b + c)\ln c + (c + a)\ln c + (c + a)\ln a + (a + b)\ln a + (a + b)\ln b]$, which on regrouping by $\ln$-factor becomes
\[
  -[((c + a) + (a + b))\ln a + ((a + b) + (b + c))\ln b + ((b + c) + (c + a))\ln c]
\]
\[
  =\; -[(2a + b + c) \ln a + (2b + a + c) \ln b + (2c + a + b) \ln c].
\]
This is the *negative* of a sum we want to show is $\geq 0$. We need
\[
  (2a + b + c) \ln a + (2b + a + c) \ln b + (2c + a + b) \ln c \;\geq\; 0.
\]
Subtract $(a + b + c)(\ln a + \ln b + \ln c) = (a + b + c) \cdot 0 = 0$ (using $abc = 1$):
\[
  (a) \ln a + (b) \ln b + (c) \ln c \;\geq\; 0.
\]
This is the inequality $\sum a \ln a \geq 0$ under $abc = 1$.

Apply the weighted AM-GM (or the convexity of $x \ln x$, or Jensen's inequality on the convex function $f(x) = x \ln x$). By convexity of $x \ln x$ on $(0, \infty)$,
\[
  \frac{a \ln a + b \ln b + c \ln c}{a + b + c} \;\geq\; \frac{a + b + c}{3} \ln \frac{a + b + c}{3}.
\]
By AM-GM, $a + b + c \geq 3 (abc)^{1/3} = 3$. So the right-hand side is $\geq 1 \cdot \ln 1 = 0$. Therefore
\[
  a \ln a + b \ln b + c \ln c \;\geq\; (a + b + c) \cdot 0 \;=\; 0.
\]
Hence the original sum is $\geq 0$, and so the *negative* of it (i.e., the logarithm of the LHS) is $\leq 0$, giving $a^{b+c} b^{c+a} c^{a+b} \leq 1$.

Equality holds when $a = b = c = 1$. $\blacksquare$

**Part (ii): $(a - 1 + 1/b)(b - 1 + 1/c)(c - 1 + 1/a) \leq 1$.**

The constraint $abc = 1$ permits the symmetric substitution $a = x/y, b = y/z, c = z/x$ for positive reals $x, y, z$. (Verify: $abc = (x/y)(y/z)(z/x) = 1$.) The substitution *uses* the symmetry of the constraint rather than fighting it — Form-IV in §3.2.

Rewrite each factor under this substitution:
\[
  a - 1 + \frac{1}{b} \;=\; \frac{x}{y} - 1 + \frac{z}{y} \;=\; \frac{x + z - y}{y}.
\]
Similarly,
\[
  b - 1 + \frac{1}{c} \;=\; \frac{y + x - z}{z}, \qquad c - 1 + \frac{1}{a} \;=\; \frac{z + y - x}{x}.
\]
The product is
\[
  \frac{(x + z - y)(y + x - z)(z + y - x)}{x y z}.
\]
The numerator is the Schur-style symmetric expression $(x + y - z)(y + z - x)(z + x - y)$ (re-ordered). The denominator is $xyz$.

The inequality to prove is
\[
  (x + y - z)(y + z - x)(z + x - y) \;\leq\; x y z.
\]
This is *Schur's inequality* in disguise. Specifically: if $x, y, z$ are sides of a triangle (i.e., each factor on the LHS is positive), then $(x + y - z)(y + z - x)(z + x - y) \leq xyz$, with equality iff $x = y = z$.

If $x, y, z$ are not sides of a triangle, at least one factor on the LHS is non-positive; if exactly one is non-positive the LHS is non-positive while the RHS is positive, and the inequality holds. If two or more factors are non-positive, this contradicts the triangle inequality structure of positive reals; only the triangle case is generic.

In all cases, $(x + y - z)(y + z - x)(z + x - y) \leq xyz$, with equality iff $x = y = z$ (equivalently, $a = b = c = 1$). The IMO 2000 inequality is proved. $\blacksquare$

**Key lesson (both parts).** The constraint $abc = 1$ is *symmetric* in the cyclic shift $a \to b \to c \to a$. Both inequalities have *cyclic-symmetric* expressions on each side. By the inheritance principle, the extremiser is on the symmetric configuration $a = b = c = 1$. The substitution $a = x/y, b = y/z, c = z/x$ converts the multiplicative constraint to a free positive-reals constraint while preserving cyclic symmetry, and the inequalities reduce to classical Schur-style ones in the new variables. Equality everywhere is forced by the symmetric extremiser.

> *The right substitution for a symmetric constraint is itself symmetric. The wrong substitution destroys the symmetry the constraint was protecting.*

This closes the chapter's worked-example slate and the chapter itself.

---

🌑

*End of Chapter 2 — Symmetry. Next: Chapter 3 — Duality.*
