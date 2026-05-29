---
chapter: 8
archetype: Domain Translation
subtitle: "If the Language is Wrong, Speak a Different One"
category: Method Selection (Archetypes 5–8) — final chapter of the sub-pillar
related_archetypes: [3, 5, 7, 15, 19]
key_gems: [A10, A15, D06, D08, D19, E03]
  - "Argand correspondence $\\mathbb{C} \\leftrightarrow \\mathbb{R}^2$: every complex number is a point in the plane, every plane point a complex number"
  - "De Moivre's theorem $(\\cos\\theta + i\\sin\\theta)^n = \\cos n\\theta + i\\sin n\\theta$ — multiplication in $\\mathbb{C}$ as rotation-and-scaling on the plane"
  - "Ratio of complex differences $(z_1 - z_3)/(z_2 - z_3) = r\\,e^{i\\phi}$ — modulus is the ratio of two sides at $z_3$; argument is the included angle"
  - "Reverse triangle inequality $|a - b| \\ge \\big||a| - |b|\\big|$ as a planar-geometry statement about the third side of a triangle"
  - "Standard parametric form of the parabola $y^2 = 4ax$: $(at^2, 2at)$ — translation of an algebraic curve into a curve with one scalar parameter"
  - "Vector triple product $[\\vec a, \\vec b, \\vec c] = \\vec a \\cdot (\\vec b \\times \\vec c)$ as the determinant of the coordinate matrix"
  - "Distance from a point to a line via cross product: $d = |\\vec r \\times \\hat d|$, where $\\vec r$ is from any line-point to the external point and $\\hat d$ is the unit direction"
  - "Generating function $\\sum_n a_n z^n$ — turning a discrete sequence into a continuous (formal) series so that combinatorial identities become algebraic identities"
  - "Möbius transformation $z \\mapsto (az + b)/(cz + d)$ — translation between algebraic action on $\\mathbb{C}$ and conformal action on the Riemann sphere"
  - "Time domain $\\leftrightarrow$ frequency domain via Fourier transform — differential equations become algebraic in the frequency variable"
canonical_takeaway: "The same structure looks different in each language; read it in the easiest one."
status: locked
last_revised: 2026-05-29
locked_on: 2026-05-29
sourcing_note: "All worked examples and practice problems in this chapter are drawn from K.D. Joshi, *Educative JEE Mathematics* (2nd ed.), or from JEE / RMO / INMO examinations commented on in that text. See Blueprint §6.2 for the sourcing rule and `pillar2-archetypes/_template/joshi-problems-locked.md` §Ch. 8 for the locked slate. **Verification audit for this chapter discovered one slate-answer error**: PP3 (3-roots right-angle reformulation of JEE 2001 / Joshi Ex. 24.24) was listed as $n = 4k$, but the correct answer for the reformulated problem is $n$ even with $n \\ge 4$. Patched in slate v0.2.5; see the chapter's PP3 solution for the corrected derivation, which uses Thales' theorem (converse of the inscribed angle theorem in a semicircle)."
---

# Chapter 8 — Domain Translation

## *If the Language is Wrong, Speak a Different One*

---

## Opening Vignette

A student of music is given the manuscript of a Bach fugue and a recording of the same piece performed on the harpsichord. She knows both presentations are the same work. The recording delivers the work as a temporal stream — overlapping voices, the entries of the subject, the swelling of polyphonic texture, the cadences, the final perfect-authentic close. The manuscript delivers the work as a spatial array — clefs, time signature, key signature, four staves stacked vertically, notes positioned along horizontal lines, slurs and accidentals annotating local structure. The two presentations contain the same musical information. They are not equally illuminating. To answer the question *"what is the subject of the fugue?"* she could in principle listen carefully, isolate the opening theme, and remember it. But on the page, the subject is *literally visible*: the first staff's first six beats, set off from the rest, immediately seen. To answer the question *"in what voice does the subject enter third?"* she could in principle listen, but the page tells her in one glance — the third entry is in the tenor staff at bar five. To answer the question *"is the fugue's middle section a stretto?"* the page shows the overlapping entries as a typographic pattern; the recording forces her to track three simultaneous voices in real time. The manuscript and the recording carry the same information; *for structural questions, the manuscript answers in a single glance what the recording forces her to compute over twelve minutes.* The right language for a question is the language in which the question's answer is *visible*.

Now turn to a different scene, four hundred years earlier. The young René Descartes, lying in bed in a heated room one morning in the winter of 1619, watches a fly walk across the ceiling. He notices that he can specify the fly's position at any instant by two numbers: its distance from the south wall, and its distance from the east wall. Two numbers, one position. The observation generalises. *Every* point on the ceiling — every point in any plane region, in fact — can be specified by two numbers, and conversely every pair of numbers specifies a point. The geometric plane and the algebraic set $\mathbb{R}^2$ are *the same thing under a translation*. Once the translation is made, every geometric statement becomes an algebraic statement and vice versa. The conic sections, which the Greeks had laboriously studied for two thousand years as curves of intersection of a cone with planes, become *polynomials of degree two in two variables*. The intersection of two curves becomes *the solution of a system of equations*. The construction of a tangent line becomes *the differentiation of a function*. An entire civilisation's intuitions about *figures* are absorbed into a single language about *numbers*; and that language, because numbers can be added and multiplied and inequalities maintained, supports computational moves that pure geometry could not. The history of mathematics after 1637 is, in large part, the history of working out what Descartes had begun: the systematic translation of every problem expressible in one mathematical language into another in which it becomes tractable.

These two scenes look unrelated. A music student reading a score; a philosopher watching a fly. They share one of the most consequential observations in mathematics. In each, *one piece of content is presented in two languages*, and the choice between languages is not a matter of taste but of *what the languages make easy*. The fugue's structural questions are easy on the page and hard in the ear. The plane's incidence questions (do two lines meet? where?) are easy in coordinates and hard in synthetic Euclidean argument. The translation between the languages — from staff notation to acoustic stream, from coordinates to figures — preserves the underlying content. But the *visibility* of structure depends on which language one is reading in, and the trained reader knows which language to translate to before attempting the question. That is the move this chapter develops.

This is *Domain Translation*. It is the fourth archetype of the *Method Selection* sub-pillar, completing the quartet whose other three members are Substitution (Ch. 5), Linearisation (Ch. 6), and Normalisation (Ch. 7). Where Substitution changed the *variable*, Linearisation changed the *function* (replacing it by its tangent), and Normalisation changed the *scale*, Domain Translation changes the *language*. The move appears under many names — *analytic geometry* (geometry to algebra), *complex methods* (planar geometry to algebra of $\mathbb{C}$), *vector methods* (synthetic geometry to algebra of $\mathbb{R}^n$), *generating functions* (combinatorics to algebra of formal series), *Fourier methods* (time-domain analysis to frequency-domain algebra), *Laplace methods* (differential equations to algebra), *coordinate-free differential geometry* (the reverse direction, from coordinates back to invariant statements). What unifies them is the same logic: *recognise that the language in which the problem was stated is not the language in which its structure is most visible; translate to the natural language; solve; translate back*.

> *The natural language for a problem may not be the language it was given in. Translate, solve, translate back.*

---

## 1. The Archetype Defined

### 1.1 Formal Definition

We make the intuition precise.

\begin{definition}[Domain Translation]
A *domain translation* is a structure-preserving map $\varphi : D_1 \to D_2$ between two mathematical domains, together with a left-inverse $\varphi^{-1}$ (defined on the image of $\varphi$) sending answers in $D_2$ back to answers in $D_1$. A problem $P$ stated in $D_1$ may be translated to $\varphi(P)$ in $D_2$; if a solution $\sigma$ is found in $D_2$, then $\varphi^{-1}(\sigma)$ is a solution to the original problem in $D_1$. The translation is *useful* precisely when the structural features of the problem — the constraints, the symmetries, the operations available — are *more visible* or *more tractable* in $D_2$ than in $D_1$.
\end{definition}

Three remarks unpack the abstraction. First, the word *structure-preserving* is doing real work. The map $\varphi$ must respect whatever operations and relations the problem actually uses. The Argand correspondence $\mathbb{C} \leftrightarrow \mathbb{R}^2$ preserves addition (complex addition is vector addition in the plane) and the Euclidean modulus (the modulus of $z$ is the distance from the origin) but does *not* preserve multiplication in the way that vector addition does — complex multiplication is a *new* operation that the planar-geometry view does not have built in. For problems that use multiplication of complex numbers as rotation-and-scaling (e.g., De Moivre's theorem), the translation $\mathbb{C} \to \mathbb{R}^2$ is the *right* one because it inherits the rotational structure of the plane. For problems that need only the additive structure, the translation could go either way. The trained solver chooses the translation that preserves the relevant structure.

Second, the *left-inverse* is essential. A translation is useful only if, having solved the problem in $D_2$, one can carry the solution back to $D_1$. Generating functions take a sequence $\{a_n\}$ to a formal series $\sum a_n z^n$; the inverse is reading off the coefficient of $z^n$. The Fourier transform takes a time-domain signal to a frequency-domain spectrum; the inverse Fourier transform brings it back. When the inverse is not available — when the translation is one-way — the move is not a true domain translation but an *embedding* or an *abstraction*, useful for proofs but not for explicit answers.

Third, the translation can be *to a larger domain* (the complex numbers are bigger than the reals; vectors in $\mathbb{R}^n$ are bigger than synthetic geometry; generating functions are bigger than finite sequences) or *to a smaller domain* (a high-dimensional problem may translate to a lower-dimensional one). Most useful translations expand the available structure — they introduce *new operations* that the original language could not perform. Complex multiplication is one such; cross product on $\mathbb{R}^3$ is another; convolution on the frequency domain is another. The pedagogical observation is that the extra structure of the target domain is precisely *what makes the problem easier*. The translation is worthwhile when the destination's structure is richer.

In this chapter we encounter four characteristic forms of domain translation. As with previous archetypes, the forms overlap — a parabola problem solved in coordinates is at once Form I and Form II — but the four-form taxonomy gives a working diagnostic.

- **Form I — Complex $\mathbb{C} \leftrightarrow$ planar geometry.** Every complex number $z = x + iy$ is identified with the point $(x, y) \in \mathbb{R}^2$. Addition of complex numbers is vector addition. Multiplication of complex numbers is rotation-and-scaling about the origin. Modulus is Euclidean distance. The translation is *richer* than the embedding $\mathbb{R}^2 \hookrightarrow \mathbb{C}$ would suggest: the complex side has multiplication and roots, the planar side has rotations and similarities. *Examples.* WE1 (triangle type from complex ratio), PP1 (ellipse as sum-of-distances set), PP5 (Möbius condition $\Rightarrow$ perpendicular bisector), PP6 (powers of $z$ as angle-multiplication), PP7 (reverse triangle inequality).

- **Form II — Coordinate algebra $\leftrightarrow$ synthetic geometry.** Descartes's move: pick an origin, two perpendicular axes, and identify every plane point with an ordered pair $(x, y)$. Curves become equations; intersections become systems; tangent lines become derivatives. The inverse direction — from coordinates back to figures — is what gives geometric meaning to an algebraic result. *Examples.* WE3 (parabola focal-chord locus), PP2 (centroid locus by vector averaging in coordinates).

- **Form III — Vector algebra $\leftrightarrow$ $\mathbb{R}^n$ geometry.** Every geometric object in $\mathbb{R}^n$ — point, line, plane, hyperplane — is described by a vector or a system of vectors, and every algebraic operation on vectors (sum, scalar product, cross product, determinant) corresponds to a geometric construction (translation, projection, oriented area, oriented volume). The translation is the foundation of all multi-dimensional geometry; in $\mathbb{R}^3$, the cross product and the scalar triple product give the operations that compute angles, areas, volumes, distances. *Examples.* WE2 (vector triple product as determinant), PP4 (distance from origin to line via cross product).

- **Form IV — Discrete $\leftrightarrow$ continuous (generating functions, transforms).** A sequence $\{a_n\}_{n \ge 0}$ becomes the formal series $\sum_{n \ge 0} a_n z^n$; a recurrence on the sequence becomes a functional equation on the series. A time-domain function $f(t)$ becomes the Fourier transform $\hat f(\omega)$, and a differential equation in $t$ becomes an algebraic equation in $\omega$. The Laplace transform sends initial-value problems to algebraic problems. *Examples.* Not directly in this chapter's WE/PP slate (the form is preview for Pillar 3 / Pillar 5, where generating functions and transforms get their own treatment), but the connections section (§6.2) traces the link.

### 1.2 The Core Principle

The principle of domain translation, stripped to its essence, is one sentence.

> *Recognise that the language in which the problem was stated is not the language in which its structure is most visible; translate to the natural language; solve there; translate back.*

This sentence inverts an instinct that competition mathematics actively cultivates. A student trained to recognise problem-types learns to associate problem statements with techniques: *if it says "triangle," use triangle inequalities; if it says "$n$-th roots of unity," use De Moivre; if it says "tangent line," differentiate; if it says "sum of a series," look for telescoping*. The associations are useful — they generate candidate moves quickly — but they have a structural blind spot. The associations key off the *language* of the problem as stated, not the *content*. A geometry problem stated geometrically gets a geometric attempt; a complex-number problem stated complex-analytically gets a complex-number attempt. The associations *do not prompt the question of whether the problem should be re-stated in a different language entirely*.

Domain Translation is the discipline that breaks this binding. Before reaching for a technique within the stated language, the trained solver pauses to ask: *is this problem perhaps another problem in disguise — a problem from a different mathematical domain that I would solve more easily?* If the answer is yes, translation is the first move. If the answer is no, the standard within-language techniques apply. The cost of the pause is a few seconds; the benefit, when the answer is yes, is often a collapse of the problem from hard to easy.

### 1.3 The Cognitive Shift

The cognitive shift Domain Translation enforces is from *"this is a geometry problem, solve it geometrically"* to *"the natural language for this problem may not be the language it was given in."* It is, in some ways, the most *intellectually demanding* of the Method Selection archetypes: Substitution, Linearisation, and Normalisation each operate *within* a fixed mathematical language, while Translation steps outside the language to ask which language to use. The student who internalises this shift acquires a habit that scales from JEE problems to research mathematics: *the choice of representation is itself an act of mathematics*, and the first creative work on a hard problem is often choosing the language in which to attack it.

A second shift, less obvious, is from *"a translation is a notation choice"* to *"a translation is a transfer of structure."* The Argand identification of $\mathbb{C}$ with $\mathbb{R}^2$ is not a relabelling — it imports *the multiplicative structure of $\mathbb{C}$* into planar geometry, giving us rotations expressed as multiplication, and *the metric structure of $\mathbb{R}^2$* into the complex plane, giving us a geometric reading of modulus and argument. The same is true at every scale. The Cartesian identification of geometry with $\mathbb{R}^2$ imports algebra into geometry. Vector methods import linear algebra. Generating functions import the algebra of formal power series. Each translation comes with a *kit of tools* that the original language did not have, and using the tools is half the benefit.

A third shift is from *"there is one right answer"* to *"there is one right structure, and many ways to express it."* Two solutions that look entirely different — one synthetic, one analytic; one geometric, one algebraic — may be the same solution written in two languages. Recognising this is what allows the trained solver to *transfer* an insight from one problem to another that looks superficially distinct. It is also what underlies the deepest connections in mathematics — the *equivalences of categories* in category theory, the *Langlands correspondences* in number theory, the *mirror symmetries* in algebraic geometry. Each is, at root, a vast and unexpected translation between domains that were once thought to be only loosely related.

---

## 2. The Deep Structure

### 2.1 Mathematical Foundations

Domain translation rests on a single structural foundation, refined by progressively richer mathematical settings.

The basic object is the *structure-preserving map* — what the working mathematician calls an *isomorphism* when it preserves all of the relevant structure (so that the inverse exists), an *embedding* when it preserves the structure on its image (so it identifies $D_1$ with a sub-structure of $D_2$), and a *homomorphism* when it preserves only a partial set of operations. Linear algebra studies the linear maps; group theory the group homomorphisms; ring theory the ring homomorphisms; topology the continuous maps. In every setting, the central question is *which structure on the source carries to which structure on the target*, and *which questions about the source can therefore be answered in the target*.

The translations in this chapter all fit this pattern at the elementary level. The Argand identification $\mathbb{C} \leftrightarrow \mathbb{R}^2$ is an isomorphism *of additive groups* (and of metric spaces, with the modulus and the Euclidean norm matching). It is *not* an isomorphism of multiplicative structure, since $\mathbb{R}^2$ has no canonical multiplication; instead, the multiplicative structure of $\mathbb{C}$ is *additional content* that the planar-geometry side does not natively possess. This is why complex methods are useful in plane geometry: they import a multiplication that the plane does not have on its own. The Cartesian identification of the plane with $\mathbb{R}^2$ is, similarly, an isomorphism of sets with metric, importing the algebraic operations of $\mathbb{R}^2$ into the plane. Vector methods are the same construction in $\mathbb{R}^n$ for $n \ge 2$.

A subtler foundation is the *category-theoretic* perspective: a domain translation is most naturally a *functor* $F : \mathcal{C}_1 \to \mathcal{C}_2$ between two categories, preserving the morphism structure. When the functor is an *equivalence of categories*, the two domains are interchangeable for all category-theoretic purposes, and any theorem proved in one transfers automatically to the other. The Gelfand duality — between compact Hausdorff spaces and commutative C*-algebras — is a famous example: every topological question about a space becomes an algebraic question about its algebra of continuous functions, and vice versa. The chapter does not require this machinery, but the philosophy permeates the move: *translations are not tricks but transfers of mathematical content between languages designed for different questions*.

A third foundation, essential for the worked examples, is the *parametrisation* of geometric objects. A curve in the plane — a line, a circle, a conic — admits a parametric representation in which a single parameter $t$ (or two parameters for a surface) ranges over an interval, and each value of the parameter corresponds to a point on the curve. The standard parabola $y^2 = 4ax$ admits the parametrisation $(at^2, 2at)$ for $t \in \mathbb{R}$; the standard ellipse $x^2/a^2 + y^2/b^2 = 1$ admits $(a\cos\theta, b\sin\theta)$ for $\theta \in [0, 2\pi)$; the unit circle in $\mathbb{C}$ admits $e^{i\theta}$ for $\theta \in [0, 2\pi)$. Each parametrisation is itself a domain translation — from the implicit algebraic curve to a curve parametrised by one or two scalars — and the parametrisation often does the heavy lifting. WE3 (the parabola focal-chord locus) is a textbook example: in implicit form, the question is intractable; in parametric form, *one line* suffices.

### 2.2 Physical and Cross-Domain Foundations

The reach of domain translation extends across the quantitative sciences.

In *physics*, the *Fourier transform* is the canonical translation from the time domain to the frequency domain. A signal $f(t)$ becomes a spectrum $\hat f(\omega) = \int f(t) e^{-i\omega t}\, dt$, and a differential equation in $t$ — say, the linear ODE $f''(t) + \omega_0^2 f(t) = g(t)$ — becomes an *algebraic* equation in $\omega$, since differentiation translates to multiplication by $i\omega$. The translation is what makes signal processing, quantum mechanics, and partial differential equations tractable: every linear time-invariant system is *diagonalised* by the Fourier transform, meaning that the transformation reduces the operator (a complicated differential or convolution operator) to a scalar multiplication at each frequency. The cost of the translation is that the inverse Fourier transform must be performed at the end; the benefit is that the difficult middle step is replaced by elementary algebra.

In *electrical engineering*, the *Laplace transform* sends an initial-value problem for a linear ODE to an algebraic equation. Circuits with capacitors and inductors are governed by differential equations in the time domain, but in the Laplace domain (the variable $s$), every capacitor becomes $1/(sC)$ and every inductor becomes $sL$, and the entire circuit becomes a network of impedances. The solution is found by algebra (Ohm's law, Kirchhoff's laws), and the inverse Laplace transform brings the answer back to the time domain. Generations of engineers have been trained to *first* draw the equivalent impedance circuit in the Laplace domain, *then* solve, *then* translate back — exactly the three-step pattern of Domain Translation.

In *probability theory*, the *characteristic function* $\varphi_X(t) = \mathbb{E}[e^{itX}]$ is a translation that turns convolution (the operation governing sums of independent random variables) into multiplication. The fact that the distribution of $X + Y$ is the *convolution* of the distributions of $X$ and $Y$ makes direct calculation hard; the fact that $\varphi_{X+Y}(t) = \varphi_X(t) \cdot \varphi_Y(t)$ makes it trivial. Every classical limit theorem in probability (the central limit theorem, the law of large numbers, the Lévy continuity theorem) is proved by passing to characteristic functions, performing an algebraic argument there, and translating back.

In *theoretical computer science*, *compilation* is a domain translation: a program in a high-level language is translated, via a series of intermediate representations, into machine code. Each translation preserves the *operational semantics* (the program does the same thing) while changing the language in which the program is written. The deep correctness theorems of compilation are *equivalence-of-semantics* theorems — domain-translation theorems in the strict sense. The same is true of database query optimisation, of cryptographic protocol design, of program analysis, of model checking. The discipline of "translate to a domain in which the question is decidable, then translate back" is the practical content of much of theoretical computer science.

In *music theory*, the *equal-tempered tuning* is the translation that makes pitch ratios (originally just intonation, the algebra of fractions like $3/2$ for a fifth and $5/4$ for a major third) into the geometric language of *equal divisions of the octave*. The translation turns a problem about ratios — which scales are consonant? which keys are playable? — into a problem about positions on a logarithmic axis, where the move is uniform and the same in every key. The cost is a tiny amount of intonational impurity; the benefit is the entire history of post-1700 Western music, in which composers freely modulate between keys because the keys are all *the same key under translation*.

### 2.3 Cognitive Foundations

The cognitive payoff of domain translation is twofold.

The first is *the leverage of a richer toolkit*. A problem stated in plane geometry has only the tools of synthetic geometry available: lengths, angles, congruence, parallelism, the theorems of Euclid. Translated to coordinates, it gains all of algebra. Translated to complex numbers, it gains rotations, similarities, and roots of polynomials. Translated to vectors, it gains the cross product and the scalar triple product. Each translation imports the *entire algebraic apparatus* of the target domain, and the target's apparatus is usually richer than the source's. The trained solver knows which apparatus each translation imports and which problems benefit from which import.

The second is *the visibility of structure*. The fugue's manuscript and the recording carry the same content, but the manuscript displays the structural relations between voices in a way the recording forces the listener to compute. The same is true of every mathematical translation. A regular $n$-gon, drawn synthetically, *has* the property that its vertices are equally spaced around a circle. Translated to complex numbers, the *same* property becomes the algebraic statement that the vertices are *the $n$-th roots of unity* — a statement that immediately makes available the algebraic tools (De Moivre, vieta, factorisations of $z^n - 1$). The geometric statement and the algebraic statement have the same content; the algebraic one is the one in which Chapter 2's symmetries become computable. The trained solver internalises that *visibility of structure depends on language*, and chooses the language accordingly.

---

## 3. The Diagnostic Toolkit

### 3.1 The Three Questions Method (Domain Translation Edition)

Before any algebra, the trained solver asks three questions of the problem.

1. **Is the stated language the natural language?** Does the problem's vocabulary — geometric, algebraic, analytic, combinatorial — match the structure the problem actually exploits? A problem about regular $n$-gons stated in synthetic geometry is using its language *poorly*: the rotational structure is invisible until one translates to complex numbers. A problem about counting subsets stated combinatorially may be naturally counted by a generating function. The diagnostic: *does the language as stated have the tools needed to solve the problem?* If yes, proceed within the language. If no, translate first.

2. **What translation does the problem suggest?** If translation is needed, which target domain? The clue is in the structure: *circular* or *rotational* structure suggests $\mathbb{C}$; *coordinate* or *incidence* structure suggests Cartesian algebra; *vector* or *higher-dimensional* structure suggests $\mathbb{R}^n$; *recursive* or *sequence-based* structure suggests generating functions; *time-evolution* structure suggests Fourier or Laplace. The translation should bring the *exact* extra structure that the problem needs.

3. **What is the inverse translation?** Before committing to the translation, the solver should know how to translate the answer back. A complex-number solution gives a complex number; if the answer is a triangle type or a geometric locus, *what feature of the complex answer corresponds to that?* If the inverse translation is unclear, the move may be a dead end. (For most standard translations — $\mathbb{C} \leftrightarrow \mathbb{R}^2$, Cartesian, vector — the inverse is automatic. For generating functions and transforms, the inverse requires more care.)

The three questions can be answered in seconds. The reward, when the answers point to translation, is often a problem that collapses in a single line.

### 3.2 Forms of Domain Translation: A Comprehensive Guide

We collect the four characteristic forms encountered in the chapter.

- **Form I — Complex $\mathbb{C} \leftrightarrow$ planar geometry.** *Diagnostic:* the problem involves points in the plane, rotations, similarities, or angle relations; or, conversely, an algebraic identity in complex numbers whose geometric meaning is unclear. *Move:* identify $z = x + iy$ with the point $(x, y)$; use $|z|$ for distance and $\arg z$ for angle from the positive real axis; use multiplication by $e^{i\theta}$ for rotation. *Examples.* WE1, PP1, PP5, PP6, PP7.

- **Form II — Coordinate algebra $\leftrightarrow$ synthetic geometry.** *Diagnostic:* a geometric problem in the plane involving conics, intersections, tangents, or loci; or an algebraic problem whose geometric content (the curve being studied) is what the solver wants to see. *Move:* pick coordinates; reduce geometric statements to algebraic ones; use parametrisations of standard curves $(at^2, 2at)$ for parabolas, $(a\cos\theta, b\sin\theta)$ for ellipses, $r(\cos\theta, \sin\theta)$ for circles. *Examples.* WE3 (parabola focal chord), PP2 (centroid locus).

- **Form III — Vector algebra $\leftrightarrow$ $\mathbb{R}^n$ geometry.** *Diagnostic:* the problem involves three-dimensional or higher-dimensional configurations, or distances and angles between lines and planes. *Move:* express points as position vectors; lines as $\vec r = \vec a + t \vec d$; planes as $\vec r \cdot \vec n = c$; use the dot product for angles and projections, the cross product for areas and perpendicular distances, the scalar triple product for volumes. *Examples.* WE2 (vector triple product), PP4 (distance from origin to line).

- **Form IV — Discrete $\leftrightarrow$ continuous (generating functions, transforms).** *Diagnostic:* a counting problem, a recurrence on a sequence, or a discrete optimisation that does not yield to elementary manipulation; or a differential equation whose solution requires algebraic structure. *Move:* form the generating function $\sum a_n z^n$ or the appropriate transform (Fourier, Laplace, $z$-transform); manipulate algebraically in the transformed domain; invert. The form is dominant in Pillar 5 (the Gems) and in Pillar 3 (the Science of Multidirectional Solving); in this chapter, it is signposted but not exercised in the worked examples.

### 3.3 Common Pitfalls

Five errors recur often enough to deserve named warnings.

- **The Wrong Translation.** Choosing a target domain that does not import the right structure. A problem with strong rotational symmetry translated into Cartesian coordinates loses the symmetry to a thicket of $\cos\theta, \sin\theta$ expressions; the same problem in complex numbers is two lines. The remedy is the diagnostic of §3.1 question 2: *match the target's extra structure to the problem's exploitable structure*.

- **The Translation Without Inverse.** Performing a translation and getting an answer in the target domain, but failing to translate back to the original language. A generating-function computation that yields a closed-form for $\sum a_n z^n$ is not yet an answer to a combinatorial problem; the answer is the coefficient. A complex-number computation that yields a complex value is not yet an answer to a geometry problem; the answer is what that complex value *means* geometrically. The remedy is to plan the inverse translation *before* starting the forward one (§3.1 question 3).

- **The Notation Confusion.** Conflating two distinct quantities because the same symbol is used for both. A geometry problem with complex coordinates and a separate complex variable $z$ in a Möbius transformation can quickly produce notational chaos. The remedy is disciplined symbol-management: use distinct letters for distinct roles, and when the translation makes the original symbols obsolete, drop them.

- **The False Equivalence.** Treating the source domain and the target domain as *interchangeable* when the structure-preserving map is only partial. The map $\mathbb{R} \hookrightarrow \mathbb{C}$ preserves field structure but discards ordering; consequently, inequalities in $\mathbb{R}$ do not always have meaningful complex analogues. The map $\mathbb{Z} \hookrightarrow \mathbb{R}$ preserves arithmetic but discards discreteness; problems about lattice points do not simplify by passing to $\mathbb{R}$. The remedy is the formal definition (§1.1): a translation is structure-preserving for the structure the problem cares about, not for all structure.

- **The Premature Translation.** Translating too early, before the problem's actual structure is identified. A solver who reaches for complex numbers at the first sight of an angle, or coordinates at the first sight of a triangle, may obscure a one-line synthetic solution behind two pages of algebra. The translation move is *strategic*, not *automatic*; the diagnostic of §3.1 question 1 — *is the stated language the natural one?* — should be asked, and *if the stated language is already natural*, no translation is needed. Some problems are simply geometry problems and want a geometric solution.

---

## 4. Worked Examples

We work three problems in detail, each in the six-point format. The first illustrates Form I (complex $\leftrightarrow$ planar geometry); the second illustrates Form III (vector algebra) at the JEE Mains level; the third illustrates Form II (coordinate parametrisation of a parabola).

### 4.1 Example 1 — Triangle Type from a Complex Ratio

**Problem.** *The complex numbers $z_1, z_2, z_3$ satisfy*
\[
  \frac{z_1 - z_3}{z_2 - z_3} \;=\; \frac{1 - i\sqrt 3}{2}.
\]
*Identify the type of the triangle with vertices $z_1, z_2, z_3$.* (JEE 2001; Joshi *EJM* Ch. 24, Exercise 24.25.)

**SEED.** *Domain translation (Form I — complex $\leftrightarrow$ planar geometry).* The ratio of two complex differences encodes two geometric facts simultaneously: the modulus is the ratio of the corresponding side lengths from the common vertex, and the argument is the included angle at that vertex. One value of the ratio, two pieces of geometric information.

**BRUTE PATH.** A student who treats the problem purely algebraically writes $z_k = x_k + i y_k$ and expands the ratio:
\[
  \frac{(x_1 - x_3) + i(y_1 - y_3)}{(x_2 - x_3) + i(y_2 - y_3)} \;=\; \frac{1 - i\sqrt 3}{2}.
\]
To equate real and imaginary parts, multiply numerator and denominator by the conjugate of the denominator and collect terms. After several lines of algebra,
\[
  (x_1 - x_3)(x_2 - x_3) + (y_1 - y_3)(y_2 - y_3) \;=\; \frac{1}{2}[(x_2 - x_3)^2 + (y_2 - y_3)^2],
\]
\[
  -(x_1 - x_3)(y_2 - y_3) + (y_1 - y_3)(x_2 - x_3) \;=\; -\frac{\sqrt 3}{2}[(x_2 - x_3)^2 + (y_2 - y_3)^2].
\]
The first equation is a dot-product relation; the second is a cross-product relation. With patience one can extract that $|z_1 - z_3| = |z_2 - z_3|$ and that the angle at $z_3$ is $\pi/3$, and conclude that the triangle is equilateral. The path *works* but converts a one-line problem into a half-page calculation, with several arithmetic opportunities for error.

**ELEGANT PIVOT.** We use the *geometric reading* of the complex ratio directly. Write the right-hand side in polar form:
\[
  \frac{1 - i\sqrt 3}{2} \;=\; \cos\!\left(-\frac{\pi}{3}\right) + i \sin\!\left(-\frac{\pi}{3}\right) \;=\; e^{-i\pi/3}.
\]
The modulus is $\sqrt{(1/2)^2 + (\sqrt 3/2)^2} = 1$ and the argument is $-\pi/3$.

Now read the meaning of $(z_1 - z_3)/(z_2 - z_3)$. Geometrically, $z_1 - z_3$ is the vector from $z_3$ to $z_1$, and $z_2 - z_3$ is the vector from $z_3$ to $z_2$. Dividing gives a complex number whose
\begin{itemize}
\item *modulus* is $|z_1 - z_3| / |z_2 - z_3|$ — the ratio of the side lengths from $z_3$;
\item *argument* is $\arg(z_1 - z_3) - \arg(z_2 - z_3)$ — the (oriented) angle at $z_3$ from the side to $z_2$ to the side to $z_1$.
\end{itemize}

The condition $(z_1 - z_3)/(z_2 - z_3) = e^{-i\pi/3}$ therefore translates into:
\begin{itemize}
\item $|z_1 - z_3| = |z_2 - z_3|$ — the two sides from $z_3$ are equal in length;
\item the angle at $z_3$ has magnitude $\pi/3 = 60°$ (the negative sign indicates orientation only).
\end{itemize}

A triangle with two equal sides and the included angle equal to $60°$ has, by the law of cosines (or directly by isoceles symmetry), the third side equal to the other two:
\[
  c^2 \;=\; a^2 + b^2 - 2ab\cos C \;=\; a^2 + a^2 - 2a^2 \cdot \frac{1}{2} \;=\; a^2,
\]
so $c = a = b$. *The triangle is equilateral.*

The elegant pivot took two lines: one to recognise $(1 - i\sqrt 3)/2 = e^{-i\pi/3}$, one to read the geometric meaning of the complex ratio. The brute path took a half-page of coordinate arithmetic to reach the same conclusion.

**PITFALLS.**

- *The Brute-Force Coordinate Expansion.* The student who does not know the geometric reading of the complex ratio is forced into the brute path. The remedy is to memorise the geometric meaning of complex differences and ratios — they are the indispensable kit for any problem of this type. The mantra: *complex sum is vector addition; complex difference is the directed segment; complex ratio at a common point is similar-figure data — side ratio and included angle*.

- *Ignoring the Sign of the Argument.* The argument $-\pi/3$ is negative, indicating an orientation (the sense of the rotation from $z_2 - z_3$ to $z_1 - z_3$). For the triangle-type question, only the magnitude $|\!-\pi/3| = \pi/3$ matters. For *labelled* triangle questions (which vertex is where), the sign of the argument is essential — it distinguishes clockwise from counter-clockwise vertex orderings.

- *Confusing the Two Triangle Types Compatible with Two Equal Sides.* "Two equal sides" plus "included angle $\pi/3$" gives *equilateral*. "Two equal sides" plus "included angle $\pi/2$" gives *isosceles right-angled*. "Two equal sides" plus "included angle some other value" gives *isosceles only*. The trained solver tracks both pieces of information (length ratio AND included angle) and concludes the most specific possible triangle type. Here, both pieces force equilateral.

- *Failing to Verify That the Two Sides Lie at a Common Vertex.* The ratio $(z_1 - z_3)/(z_2 - z_3)$ is at vertex $z_3$ — both differences subtract $z_3$. A different ratio, say $(z_1 - z_2)/(z_2 - z_3)$, is *not* at a common vertex; it represents the ratio of two distinct sides and has a different geometric meaning. Always check which vertex the ratio is centred on.

- *Treating $(1 - i\sqrt 3)/2$ as Generic Without Recognising It.* The value is one of the six $6$-th roots of unity (specifically $e^{-i\pi/3}$, a primitive $6$-th root); recognising it spares the trigonometric conversion. The trained solver carries a few standard polar values — $\pm 1, \pm i, (1 \pm i)/\sqrt 2, (1 \pm i\sqrt 3)/2, (\sqrt 3 \pm i)/2$ — and converts on sight.

**CONNECTIONS.**

*Primary archetype applications.* The Form-I move (complex $\leftrightarrow$ plane) controls (a) every problem of the form "given a complex condition on $z_1, z_2, z_3$, identify the triangle type" — by reading the moduli and arguments of complex differences; (b) every "rotate one figure to coincide with another" problem — by multiplying by the appropriate $e^{i\theta}$; (c) every regular-$n$-gon problem — by parametrising the vertices as $n$-th roots of unity (Chapter 2 §5.1 / PP1, and the present chapter's PP3 / PP6).

*Alternative solution archetypes.* The same triangle type can be confirmed by *Coordinate algebra* (the brute path), by *Vector methods* (computing dot products and magnitudes), or by the *Law of Cosines* applied directly to the side-length information extracted from the complex ratio. The complex method is the shortest, but the alternatives serve as cross-checks.

*Cross-domain manifestations.* The complex ratio appears in *engineering* whenever phasors are used: the ratio of two AC voltages is a complex number whose modulus is the amplitude ratio and whose argument is the phase difference. The ratio of two transfer functions in *control theory* encodes both magnitude and phase response. In *computer graphics*, complex multiplication is the simplest way to perform 2D rotations; the same algebra that decides our JEE problem also rotates the world in a video game.

**TAKEAWAY.** *A complex ratio at a common vertex encodes both length ratio and included angle — two facts for the price of one division.*

---

### 4.2 Example 2 — Vector Scalar Triple Product Dependence

**Problem.** *Let*
\[
  \vec a \;=\; \vec i - \vec k, \qquad
  \vec b \;=\; x\vec i + \vec j + (1 - x)\vec k, \qquad
  \vec c \;=\; y\vec i + x\vec j + (1 + x - y)\vec k.
\]
*On which of $x, y$ does the scalar triple product $[\vec a\ \vec b\ \vec c] = \vec a \cdot (\vec b \times \vec c)$ depend?* (JEE 2001; Joshi *EJM* Ch. 24, Exercise 24.47.)

**SEED.** *Domain translation (Form III — vector algebra $\leftrightarrow$ $\mathbb{R}^3$ geometry).* The scalar triple product, which has a purely geometric meaning (the signed volume of the parallelepiped spanned by the three vectors), translates to a purely algebraic determinant. Once the translation is made, the problem is one expansion.

**BRUTE PATH.** Compute $\vec b \times \vec c$ first, in terms of $x$ and $y$. Set up the determinant:
\[
  \vec b \times \vec c \;=\; \begin{vmatrix} \vec i & \vec j & \vec k \\ x & 1 & 1 - x \\ y & x & 1 + x - y \end{vmatrix}.
\]
Expand: the $\vec i$ component is $1 \cdot (1 + x - y) - (1 - x) \cdot x = (1 + x - y) - (x - x^2) = 1 + x^2 - y$. The $\vec j$ component (with the negative sign) is $-[x \cdot (1 + x - y) - (1 - x) \cdot y] = -[x + x^2 - xy - y + xy] = -[x + x^2 - y]$. The $\vec k$ component is $x \cdot x - 1 \cdot y = x^2 - y$.

So $\vec b \times \vec c = (1 + x^2 - y)\vec i - (x + x^2 - y)\vec j + (x^2 - y)\vec k$. Now dot with $\vec a = \vec i - \vec k$:
\[
  \vec a \cdot (\vec b \times \vec c) \;=\; (1 + x^2 - y) \cdot 1 + (\text{$\vec j$-coeff}) \cdot 0 + (x^2 - y) \cdot (-1) \;=\; (1 + x^2 - y) - (x^2 - y) \;=\; 1.
\]
The scalar triple product equals $1$, independent of $x$ and $y$.

The path *works*, and the algebra is straightforward, but the calculation has many opportunities for sign errors (six $2 \times 2$ minors with alternating signs). A more disciplined approach uses the determinant translation directly.

**ELEGANT PIVOT.** Translate the scalar triple product to a single $3 \times 3$ determinant:
\[
  [\vec a, \vec b, \vec c] \;=\; \vec a \cdot (\vec b \times \vec c) \;=\; \det\!\begin{pmatrix}
  1 & 0 & -1 \\
  x & 1 & 1 - x \\
  y & x & 1 + x - y
  \end{pmatrix}.
\]
Expand along the first row (which has a zero, simplifying):
\[
  \det \;=\; 1 \cdot \det\!\begin{pmatrix} 1 & 1 - x \\ x & 1 + x - y \end{pmatrix} - 0 + (-1) \cdot \det\!\begin{pmatrix} x & 1 \\ y & x \end{pmatrix}.
\]
The two $2 \times 2$ determinants are
\[
  \det\!\begin{pmatrix} 1 & 1 - x \\ x & 1 + x - y \end{pmatrix} \;=\; (1)(1 + x - y) - (1 - x)(x) \;=\; (1 + x - y) - (x - x^2) \;=\; 1 - y + x^2,
\]
\[
  \det\!\begin{pmatrix} x & 1 \\ y & x \end{pmatrix} \;=\; x^2 - y.
\]
Substituting,
\[
  [\vec a, \vec b, \vec c] \;=\; 1 \cdot (1 - y + x^2) + (-1)(x^2 - y) \;=\; 1 - y + x^2 - x^2 + y \;=\; \boxed{1}.
\]
The scalar triple product equals $1$, independent of both $x$ and $y$.

The elegant pivot was simply the recognition that *the scalar triple product is a determinant*. Once the determinant is written, expanding along the row with a zero eliminates one $2 \times 2$ computation, and the remaining algebra is a clean cancellation.

**PITFALLS.**

- *Computing $\vec b \times \vec c$ Component-by-Component.* The brute path uses the cofactor expansion of $\vec b \times \vec c$ — three minors, each with two terms — and then takes a dot product. This is *the determinant of $\vec a, \vec b, \vec c$ in disguise*, but the bookkeeping is twice as long and four times as error-prone. The remedy is to use the determinant identity *immediately*: $\vec a \cdot (\vec b \times \vec c) = \det[\vec a, \vec b, \vec c]$ where the vectors are stacked as rows (or columns).

- *Forgetting the Identity $\vec a \cdot (\vec b \times \vec c) = (\vec a \times \vec b) \cdot \vec c$.* The scalar triple product is invariant under cyclic permutations of its arguments. This is sometimes the cleanest way to expand: if one of the vectors has a particularly simple form (here $\vec a = \vec i - \vec k$ has only two non-zero components), placing it in the *dotted* slot reduces the dot product to a two-term sum.

- *Expanding Without Choosing the Best Row.* A $3 \times 3$ determinant is most efficient to expand along a row (or column) that has a zero. Here, the first row of the matrix has a $0$ in the middle entry; expanding along it eliminates the $\vec j$-minor entirely. Random row choice doubles the work.

- *Sign Errors in Cofactor Expansion.* The alternating signs $(+, -, +)$ in the cofactor expansion of a row of a $3 \times 3$ are the most common source of sign errors. The remedy is to write the sign pattern out explicitly *before* computing the minors:
\[
  \det = +\,a_{11}M_{11} - a_{12}M_{12} + a_{13}M_{13}.
\]
With the pattern on the page, the signs cannot be miscounted.

- *Reporting "Independent" Without Confirming the Constant Value.* A multiple-choice answer "depends on neither $x$ nor $y$" is *strictly stronger* than "depends only on $x$" or "depends only on $y$." The strongest correct answer here is "the scalar triple product equals $1$" — the *constant value*, not just the *independence*.

**CONNECTIONS.**

*Primary archetype applications.* The vector-algebra translation controls (a) every problem about volumes, areas, or signed distances in $\mathbb{R}^3$ (the scalar triple product is the signed volume of the spanned parallelepiped; the cross product magnitude is twice the area of the spanned triangle); (b) every problem about coplanarity of three vectors (the scalar triple product is zero iff the three vectors are coplanar); (c) every line-and-plane incidence problem in 3-space (Chapter 9 will use these tools extensively for the discriminant-analysis archetype).

*Alternative solution archetypes.* The same answer can be reached by *Substitution* (Chapter 5): substitute specific numerical values for $x$ and $y$ — say $x = y = 0$, then $x = 1, y = 0$ — and observe the result is $1$ in both cases; conclude that the triple product is a constant. This works for multiple-choice problems but does not produce a proof.

*Cross-domain manifestations.* The scalar triple product is the determinant of three column vectors, and the determinant is the *signed volume scaling factor* of the linear map whose matrix is formed by those vectors. In *computer graphics*, the sign of a triple product determines whether a polygon is *front-facing* or *back-facing* (used for backface culling). In *physics*, the triple product $\vec E \cdot (\vec B \times \vec v)$ appears in electromagnetism. In *finance*, $3 \times 3$ determinants appear in factor models and arbitrage relations among three assets.

**TAKEAWAY.** *The scalar triple product is a determinant — write it that way and the algebra writes itself.*

---

### 4.3 Example 3 — Locus of Tangent Intersection on a Parabola

**Problem.** *Find the locus of the intersection of the tangents to the parabola $y^2 = 4ax$ at the endpoints of a focal chord.* (JEE 1985; Joshi *EJM* Ch. 9, Comment 5.)

**SEED.** *Domain translation (Form II — coordinate parametrisation of a parabola).* The translation here is *not* from one mathematical language to another, but from the *implicit* algebraic form $y^2 = 4ax$ to the *parametric* form $(at^2, 2at)$. The parametric form converts every condition on points of the parabola into a condition on a single scalar parameter $t$, and the tangent-line equation becomes algebraically clean.

**BRUTE PATH.** A student who works in the implicit form parametrises points on the parabola as $(x, y)$ subject to $y^2 = 4ax$. The tangent to the parabola at $(x_0, y_0)$ is found by implicit differentiation: $2y\, dy = 4a\, dx$, so $dy/dx = 2a/y$ at $(x_0, y_0)$, and the tangent line is
\[
  y - y_0 \;=\; \frac{2a}{y_0}(x - x_0).
\]
Now consider two points $(x_1, y_1)$ and $(x_2, y_2)$ on the parabola; the two tangents at these points intersect at some $(X, Y)$. Setting up the two tangent equations and solving for $(X, Y)$ in terms of $(x_1, y_1, x_2, y_2)$ gives, after some algebra, $X = (y_1 y_2)/(4a)$ and $Y = (y_1 + y_2)/2$. The focal chord condition — the chord passes through the focus $(a, 0)$ — translates, after substantial algebra, to $y_1 y_2 = -4a^2$. Substituting gives $X = -a$, and so the locus is the vertical line $x = -a$.

The path *works* but expends substantial algebra on bookkeeping. The use of $(x_i, y_i)$ for parabola points carries the constraint $y_i^2 = 4ax_i$ implicitly throughout, and the algebra has to respect that constraint at every step — multiplying the work and the error-rate.

**ELEGANT PIVOT.** *Parametrise the parabola.* Every point on $y^2 = 4ax$ admits the representation $(at^2, 2at)$ for $t \in \mathbb{R}$ (one can verify: $(2at)^2 = 4a^2 t^2 = 4a \cdot at^2$). This translates the constraint of being *on* the parabola into the simple statement *the point is $(at^2, 2at)$ for some $t$* — and now every algebraic manipulation is on the parameter $t$, with no implicit constraint to track.

*Tangent line at the parameter point $t$.* The standard tangent equation to $y^2 = 4ax$ at the point $(at^2, 2at)$ is
\[
  t y \;=\; x + at^2.
\]
(Derivation: implicit differentiation gives $dy/dx = 2a/y = 2a/(2at) = 1/t$, so the tangent at $(at^2, 2at)$ has slope $1/t$. The equation $y - 2at = (1/t)(x - at^2)$ simplifies to $ty = x + at^2$.)

*Intersection of tangents at $t_1$ and $t_2$.* Set up the two equations:
\[
  t_1 y \;=\; x + a t_1^2 \quad\text{and}\quad t_2 y \;=\; x + a t_2^2.
\]
Subtract: $(t_1 - t_2) y = a(t_1^2 - t_2^2) = a(t_1 - t_2)(t_1 + t_2)$, so (for $t_1 \ne t_2$),
\[
  y \;=\; a(t_1 + t_2).
\]
Substitute back into the first: $t_1 \cdot a(t_1 + t_2) = x + at_1^2$, so $a t_1^2 + a t_1 t_2 = x + at_1^2$, giving
\[
  x \;=\; a t_1 t_2.
\]
*Intersection point:* $(at_1 t_2,\ a(t_1 + t_2))$.

*The focal-chord condition.* The chord from $(at_1^2, 2at_1)$ to $(at_2^2, 2at_2)$ passes through the focus $(a, 0)$. The line through the two parabola points has slope
\[
  \frac{2at_2 - 2at_1}{at_2^2 - at_1^2} \;=\; \frac{2(t_2 - t_1)}{(t_2 - t_1)(t_1 + t_2)} \;=\; \frac{2}{t_1 + t_2},
\]
and its equation is $(t_1 + t_2)(y - 2at_1) = 2(x - at_1^2)$, i.e., $(t_1 + t_2) y = 2x + 2at_1 t_2$. Substituting the focus $(a, 0)$: $0 = 2a + 2a t_1 t_2$, hence
\[
  t_1 t_2 \;=\; -1.
\]

*Locus.* The intersection's $x$-coordinate is $at_1 t_2 = a \cdot (-1) = -a$, independent of $t_1$ (and of $t_2 = -1/t_1$). The $y$-coordinate is $a(t_1 + t_2) = a(t_1 - 1/t_1)$, which ranges over all of $\mathbb{R}$ as $t_1$ varies. *The locus is the vertical line $x = -a$* — the *directrix* of the parabola.

The parametric translation does the entire problem in a half-page; the implicit version takes a page and a half. The key was to translate to a representation in which the focal-chord condition is a simple multiplicative relation $t_1 t_2 = -1$ and the intersection coordinates are degree-$1$ polynomials in the parameters.

**PITFALLS.**

- *Insisting on Implicit Coordinates.* The brute path stays in $(x, y)$ with the implicit constraint, doubling the work. The remedy is to recognise that *every standard conic has a one-parameter parametrisation that makes the algebra trivial*: parabola $(at^2, 2at)$, ellipse $(a\cos\theta, b\sin\theta)$, hyperbola $(a\sec\theta, b\tan\theta)$, circle $(r\cos\theta, r\sin\theta)$. Memorise these and reach for them at the first sight of a curve.

- *Forgetting the Standard Tangent Equation.* The tangent to $y^2 = 4ax$ at $(at^2, 2at)$ is $ty = x + at^2$, a one-line formula. A student who re-derives it by implicit differentiation each time loses thirty seconds on every problem. The standard tangent equations for the four standard conics are *gem-level results* (Pillar 5) and should be at fingertip recall.

- *Misidentifying the Focal-Chord Condition.* The focus of $y^2 = 4ax$ is $(a, 0)$, not $(0, a)$ or $(4a, 0)$. The directrix is $x = -a$. The focal-chord condition $t_1 t_2 = -1$ is specific to the standard parametrisation; for other parametrisations (e.g., $(t^2/(4a), t)$) the condition would be different. The remedy is to verify the focus and directrix every time before applying the condition.

- *Working with $(x_1, y_1)$ Instead of $(t_1)$.* Once parametric coordinates are introduced, drop the $(x_i, y_i)$ notation entirely. Carrying both creates double bookkeeping and reintroduces the implicit constraint that the parametrisation was meant to remove. The remedy is *discipline of representation*: once translated, *stay* in the translation; do not mix languages.

- *Reporting "The Directrix" Without Identifying It Geometrically.* The answer $x = -a$ is more than just a vertical line; it is the *directrix* of the parabola — the line such that every point on the parabola is equidistant from the focus and the directrix. The geometric identification is the final step of the translation back from algebra to figure. Without it, the answer is incomplete.

**CONNECTIONS.**

*Primary archetype applications.* The pole-polar duality for conics (which we touched in Chapter 3 — Duality) says, in the present language, that *the intersection of the tangents at the endpoints of any chord of a conic lies on a specific line — the polar of the chord's midpoint or, for a focal chord, the directrix*. The present problem is one instance of a structural fact: focal chords have the directrix as their tangent-intersection polar. The same parametric translation handles every "tangent intersection," "chord of contact," "polar line" problem for conics.

*Alternative solution archetypes.* The locus can also be found by *Duality* (Chapter 3): the polar of a point with respect to a conic is a line, and the focus's polar with respect to a parabola is precisely the directrix. Once the pole-polar correspondence is invoked, the result is immediate — no parametric algebra needed. The two paths — parametric and pole-polar — illustrate the same translation principle (algebra $\leftrightarrow$ geometry) at different levels of sophistication.

*Cross-domain manifestations.* The parabolic reflector is the canonical application of the focus-directrix property: rays parallel to the axis reflect through the focus, and rays from the focus reflect parallel to the axis. The directrix is the *wavefront* of the converging-to-focus reflection — every point on the directrix is equidistant from the focus along a path that reflects off the parabola. In *radio astronomy*, parabolic dishes implement this geometry to collect parallel cosmic radio waves at a focal-point receiver. In *automotive headlights*, the parabolic mirror converts a near-point light source at the focus into a parallel forward beam.

**TAKEAWAY.** *Parametrise every conic at first sight: the implicit equation imposes a constraint, the parametric form removes it.*

---

## 5. Practice Problems

Seven problems, statements only; full solutions appear in the Appendix. The slate spans Tier 1 (JEE Mains–level recognition) through Tier 2 (JEE Advanced).

### 5.1 Convex Set from Sum-of-Distances Constraint (Joshi Ch. 24, Exercise 24.12)

Given complex numbers $a, b$ and a real number $r > |a| + |b|$, identify the set
\[
  S \;=\; \{\, z \in \mathbb{C} : |z - a| + |z - b| \le r \,\}
\]
in the Argand plane, and show that $S$ is convex.

### 5.2 Centroid Locus of $\triangle PAB$ on a Circle (JEE 2001; Joshi Ch. 24, Exercise 24.18)

Let $AB$ be a chord of the circle $x^2 + y^2 = r^2$ that subtends a right angle at the origin (the centre). As $P$ moves on the circle, determine the locus of the centroid $G$ of the triangle $PAB$.

### 5.3 $n$-th Roots of Unity Forming a Right Angle (reformulation of JEE 2001; Joshi Ch. 24, Exercise 24.24)

For which positive integers $n$ do there exist three distinct $n$-th roots of unity $\omega_1, \omega_2, \omega_3$ such that the triangle with vertices $\omega_1, \omega_2, \omega_3$ has a right angle at $\omega_2$? Determine the smallest $n$ for which such a configuration exists.

### 5.4 Distance from the Origin to a Line in $\mathbb{R}^3$ (Joshi Ch. 21, Comment 5)

Find the perpendicular distance from the origin to the line passing through the point $(1, 2, 3)$ in the direction $(2, -1, 2)$.

### 5.5 Identification of an Argand Locus (Joshi Ch. 2, Comment 14)

Let $z = x + iy$, with $z \ne -1$. Identify the locus, in the Argand plane, of all $z$ satisfying
\[
  \left| \frac{z - 1}{z + 1} \right| \;=\; 1.
\]

### 5.6 Complex Argument as Angle (Joshi Ch. 2, Comment 9)

Let $z = 1 + i\sqrt 3$. Find $\arg(z)$ and $\arg(z^3)$, and interpret the latter geometrically.

### 5.7 Reverse Triangle Inequality as a Geometric Statement (Joshi Ch. 2, Comment 4)

For any complex numbers $a, b$, prove
\[
  |a - b| \;\ge\; \big||a| - |b|\big|,
\]
and identify the equality case in geometric terms.

---

## 6. The Connections Web

Domain translation does not act in isolation. Almost every other archetype either presupposes a translation or invokes one explicitly.

### 6.1 Domain Translation Across Mathematical Domains

*Algebra and geometry.* The Cartesian translation between figures and coordinates is the founding example, but the move recurs at every level. *Algebraic geometry* takes polynomial equations to varieties (geometric objects), and theorems about ideals (algebra) become theorems about points (geometry); *projective geometry* takes pairs of homogeneous coordinates to projective points, and intersections of curves are governed by Bezout's theorem (algebra-to-geometry); *differential geometry* takes coordinate-free objects (manifolds) to coordinate-laden descriptions (charts), and *back* via the requirement that quantities be well-defined under change of charts. Each is a deep instance of the same move.

*Complex analysis and real analysis.* Every theorem in real analysis has a complex analogue, and the complex analogue is often easier. The fact that polynomial equations of degree $n$ have exactly $n$ roots (counted with multiplicity) is true *in $\mathbb{C}$* (the Fundamental Theorem of Algebra) and false in $\mathbb{R}$. Real integrals that are difficult in $\mathbb{R}$ — for instance $\int_0^\infty \sin(x^2)\, dx$ — are computable by *contour integration* in $\mathbb{C}$. The translation $\mathbb{R} \hookrightarrow \mathbb{C}$ trades the order structure of the real line for the analytic structure of the complex plane, and the analytic structure is what makes the techniques work.

*Combinatorics and algebra.* Generating functions take a sequence $\{a_n\}_{n \ge 0}$ to a formal series $\sum_{n \ge 0} a_n z^n$, and the algebra of formal series — addition, multiplication, composition, differentiation, inversion — corresponds to operations on sequences (sums, convolutions, substitutions, finite differences). Solving a recurrence becomes solving a functional equation; counting subsets becomes computing a coefficient. The translation is one of the deepest in elementary mathematics: every combinatorial identity has a generating-function proof, and the generating-function proof is often the *only* proof anyone can find.

*Number theory and analysis.* The Riemann zeta function $\zeta(s) = \sum_{n \ge 1} n^{-s}$ translates the *discrete* distribution of prime numbers into the *analytic* distribution of zeros of $\zeta$ — and the deepest open problem in mathematics (the Riemann Hypothesis) is the assertion that all non-trivial zeros lie on the line $\mathrm{Re}(s) = 1/2$. Analytic number theory is, at root, the systematic translation of arithmetic into complex analysis. The translation does not eliminate the difficulty (number theory's hardest problems remain hard), but it imports the *language* in which the problems can at least be precisely stated.

### 6.2 Domain Translation in Physics and Other Sciences

*Fourier and Laplace transforms* are the workhorses. In acoustics and signal processing, every problem about waveforms is translated to a problem about spectra; in control theory and circuit analysis, every problem about a system's time-response is translated to a problem about its transfer function. The *Z-transform* does the same for discrete-time signals. In quantum mechanics, the wave-function in position space and the wave-function in momentum space are Fourier transforms of one another; every measurement is statable in either basis, with the choice of basis determined by the question.

*Differential geometry and tensor analysis* in general relativity translates the geometric content of curved spacetime into algebra (Christoffel symbols, the Riemann tensor, the stress-energy tensor) and back again. Einstein's field equations $G_{\mu\nu} = 8\pi G\, T_{\mu\nu}$ are *algebra*, but their geometric content — the curvature of spacetime is determined by the distribution of energy and momentum — is what makes the theory physically meaningful. Every black-hole calculation passes through this translation cycle: geometric intuition $\to$ algebraic Einstein equation $\to$ symbolic computation $\to$ geometric interpretation of the answer.

*Statistical mechanics* translates microscopic configurations (the positions and momenta of $10^{23}$ particles) into macroscopic thermodynamic quantities (temperature, pressure, entropy) through the partition function $Z = \sum_\text{states} e^{-E/k_B T}$. The translation is dramatic: the macroscopic variables are *averages* over the microscopic distribution, and the *fluctuation-dissipation theorem* connects the two via derivatives of $\log Z$.

*Quantum field theory* translates particle-physics processes into Feynman diagrams (a diagrammatic algebra of vertices and propagators) and back to scattering amplitudes (the experimentally measured quantities). The diagrammatic language is a *translation* — it does not contain any physics that the underlying Lagrangian does not contain, but it makes the bookkeeping of perturbation theory possible. Without the translation, no computation in QED or QCD would be feasible.

### 6.3 Cross-Domain Manifestations

The reach extends beyond physics.

*Cryptography* lives by domain translation: a *plaintext* is translated, via a key, into a *ciphertext*; encryption is the forward translation, decryption is the inverse. The whole point of a good cipher is that the inverse translation requires the secret key and is computationally infeasible without it. *Public-key cryptography* is a translation in which the forward map is easy (multiply two large primes) and the inverse is hard (factor a large semiprime); the *asymmetry* of the translation is the security.

*Linguistics.* Natural-language translation is the canonical example outside mathematics: a sentence in English carries the same propositional content as a sentence in Hindi, but the *form* of each language makes certain expressions easy and others awkward. A skilled translator knows which idiomatic move in the target language captures the source's intent; an unskilled translator produces literal-but-wrong renderings. The same skill applies in mathematical translation: a literal translation of a problem may not yield the intended easy answer; the skilled translator finds the natural language for the question.

*Music.* Beyond the score-vs-recording translation of the chapter's opening vignette, every musical analysis is a translation: *Schenkerian analysis* translates a piece into its underlying voice-leading skeleton; *set theory* (in the post-tonal sense) translates a chord into the algebraic structure of unordered pitch-class sets; *spectral analysis* translates a sound into its constituent frequencies. Each analytic move clarifies one aspect of the music at the cost of suppressing others, exactly as a mathematical translation clarifies the structure that the target language makes visible.

*Programming languages.* The act of translating an idea into code is itself a domain translation. Different programming languages make different idioms natural: functional languages make stateless computation easy, imperative languages make state-mutation easy, logic languages make backtracking search easy. A skilled programmer chooses the language to match the problem; a less skilled programmer forces every problem into one language. The same is true in mathematics — a skilled solver chooses the domain, an unskilled one forces the problem into whatever domain it was first presented in.

### 6.4 Related Archetypes

Domain translation interacts with five other archetypes in particularly tight ways.

- **Archetype 3 (Duality).** Many domain translations are *dual* pairings: synthetic geometry and analytic geometry; primal optimisation and dual optimisation; commutative algebra and algebraic geometry; vector spaces and their duals; graphs and their complements. Where Duality (Ch. 3) emphasised the *symmetry* between the two halves of a dual pairing, Domain Translation emphasises the *transit* between them: choosing one language to work in, then carrying the answer back. The two archetypes are the static and dynamic readings of the same structural phenomenon.

- **Archetype 5 (Substitution).** Substitution at the level of variables is *local* (a single variable changes); Domain Translation at the level of languages is *global* (the entire problem's vocabulary changes). They are sibling moves at different scales: every Domain Translation can be unpacked as a sequence of Substitutions (the parametric $(at^2, 2at)$ for the parabola, the polar $r e^{i\theta}$ for complex numbers, the coordinates $x = r\cos\theta, y = r\sin\theta$); and every Substitution that is also a *structure-preserving isomorphism* is, secretly, a small-scale Domain Translation.

- **Archetype 7 (Normalisation).** Normalisation chose a representative of an orbit *within* a fixed domain; Translation chose a different domain entirely. The two moves often combine: the Buckingham-$\pi$ normalisation of Chapter 7 (WE1) is a domain translation from dimensional physics to dimensionless mathematics, *and* a normalisation within the dimensionless domain. The trained solver recognises both layers and exploits them sequentially.

- **Archetype 15 (Bijection / Correspondence).** A bijection between two finite sets is the discrete analogue of a Domain Translation: two combinatorial problems may be the same problem in disguise, and the bijection is the explicit translation between them. Chapter 15 will study the move at the level of *counting two different structures and observing the counts are equal* — the most concrete form of Domain Translation, with a one-line correspondence as the translation map.

- **Archetype 19 (Pivoting / Elimination).** Pivoting in algebra — Gaussian elimination, the simplex method, Lagrange multipliers — is a *change of basis* on the linear-algebraic substrate, which is a Domain Translation between two representations of the same vector space. The simplex method translates a linear program from one extreme-point representation to another. Chapter 19 will work out the connection.

---

## 7. Master Takeaways

Seven sentences. Each one is a complete operational principle; each is meant to be quoted, internalised, and re-deployed.

1. *Mathematics is not one language but many; the same structure looks different — and is easier or harder — depending on which language you read it in.* (The canonical takeaway.)

2. *Recognise the natural language of the problem; translate to it before computing.*

3. *A complex ratio at a common vertex encodes both length ratio and included angle — two facts for the price of one division.* (WE1 takeaway; Form I.)

4. *The scalar triple product is a determinant — write it that way and the algebra writes itself.* (WE2 takeaway; Form III.)

5. *Parametrise every conic at first sight: the implicit equation imposes a constraint, the parametric form removes it.* (WE3 takeaway; Form II.)

6. *A translation worth making is one whose target imports the exact extra structure the problem needs.*

7. *Plan the inverse translation before doing the forward one; an answer in the wrong language is no answer at all.*

---

## 8. Self-Assessment Checklist

You have absorbed Chapter 8 when, without re-opening it, you can do each of the following from memory.

- [ ] State the formal definition of a domain translation as a structure-preserving map with a left-inverse, and explain why the inverse matters.
- [ ] State the geometric meaning of $|z|$, $\arg z$, $z_1 + z_2$, $z_1 z_2$, and $(z_1 - z_3)/(z_2 - z_3)$ in the Argand plane.
- [ ] State and prove De Moivre's theorem in one line, and use it to compute $\arg(z^n)$ from $\arg z$.
- [ ] State the parametric form of the parabola $y^2 = 4ax$ and the standard tangent equation at the parameter $t$.
- [ ] State the focal-chord condition $t_1 t_2 = -1$ for $y^2 = 4ax$ and derive the tangent-intersection locus as the directrix.
- [ ] State the scalar triple product as a determinant, and explain why the cyclic identity $\vec a \cdot (\vec b \times \vec c) = \vec b \cdot (\vec c \times \vec a) = \vec c \cdot (\vec a \times \vec b)$ holds.
- [ ] State the perpendicular-distance formula from a point to a line in $\mathbb{R}^3$ using the cross product.
- [ ] State and prove the reverse triangle inequality $|a - b| \ge \big||a| - |b|\big|$, identifying the equality case.
- [ ] Apply Thales' theorem (an inscribed angle in a semicircle is a right angle) and its converse, and use this to characterise antipodal $n$-th roots of unity.
- [ ] Identify which of the five common pitfalls (Wrong Translation, Translation Without Inverse, Notation Confusion, False Equivalence, Premature Translation) is most likely on a problem you are about to attempt.

---

## Bridge to Chapter 9: Domain Constraints / Bounds

Chapter 8 completes the *Method Selection* sub-pillar — the four archetypes (Substitution, Linearisation, Normalisation, Domain Translation) that govern how a trained solver chooses the right *representation* before any technical work begins. With these four moves internalised, the reader carries a working diagnostic for what to do *before* attacking the algebra.

Chapter 9 opens the third sub-pillar — *Constraint Exploitation* — and shifts attention from *representation* to *restriction*. In the previous four chapters, the moves were about reframing the problem so that its structure became visible. In the next four chapters (9 through 12), the moves are about *using* the structure once visible. The first of these is *Domain Constraints / Bounds*: many problems generate candidate solutions by algebra, but most candidates are eliminated by *the domain on which the variables are defined* — the natural numbers, the positive reals, the inside of a triangle, the unit circle. Chapter 9 makes the candidate-then-filter pattern an archetype in its own right, and the worked examples will show how often a correct algebraic answer to a JEE problem is actually *wrong* because the candidates fail a domain check that the solver did not perform.

With Chapter 9 in hand, the reader will have seen the first eight archetypes — half of Pillar 2's twenty — and will be positioned to take on the *Counting and Extremisation* sub-pillar (Chs. 13–15) and the *Meta-Reasoning* sub-pillar (Chs. 16–20) that complete the structural toolkit.

---

## Appendix — Solutions to Practice Problems

### Solution to 5.1 — Convex Set from Sum-of-Distances Constraint

*Identification.* In the Argand plane, $|z - a|$ is the Euclidean distance from $z$ to $a$, and $|z - b|$ is the distance from $z$ to $b$. The condition $|z - a| + |z - b| = r$, for $r > |a - b|$, is the *defining condition of an ellipse with foci $a, b$ and major axis of length $r$*. (The hypothesis $r > |a| + |b| \ge |a - b|$ guarantees $r > |a - b|$, so the ellipse is non-degenerate.) The condition $|z - a| + |z - b| \le r$ defines the *closed elliptical disc* — the ellipse together with its interior.

*Convexity.* Let $z_1, z_2 \in S$ and let $t \in [0, 1]$; we show $tz_1 + (1 - t)z_2 \in S$. By the triangle inequality applied to each focal distance,
\[
  |t z_1 + (1 - t)z_2 - a| \;=\; |t(z_1 - a) + (1 - t)(z_2 - a)| \;\le\; t |z_1 - a| + (1 - t)|z_2 - a|,
\]
\[
  |t z_1 + (1 - t)z_2 - b| \;=\; |t(z_1 - b) + (1 - t)(z_2 - b)| \;\le\; t |z_1 - b| + (1 - t)|z_2 - b|.
\]
Summing,
\[
  |t z_1 + (1 - t)z_2 - a| + |t z_1 + (1 - t)z_2 - b| \;\le\; t \cdot r + (1 - t) \cdot r \;=\; r,
\]
so $t z_1 + (1 - t) z_2 \in S$. Hence $S$ is convex. \hfill$\blacksquare$

The domain translation here was *algebra-to-geometry*: recognising the sum-of-distances condition as the defining property of an ellipse. The convexity proof works in either language, but the geometric reading makes the *identification* of $S$ immediate.

---

### Solution to 5.2 — Centroid Locus of $\triangle PAB$

*Setup.* Place the circle's centre at the origin, so the circle is $\{z : |z| = r\}$. Let $A, B$ be the (fixed) endpoints of the chord subtending a right angle at the origin: this means the vectors $\vec{OA}, \vec{OB}$ are perpendicular, i.e., $A \cdot B = 0$ in the real inner product (equivalently, $\overline A B + A \overline B = 0$ in complex notation), and $|A| = |B| = r$. Let $P$ be a variable point on the circle: $|P| = r$.

*The centroid.* The centroid of $\triangle PAB$ is
\[
  G \;=\; \frac{P + A + B}{3}, \quad\text{i.e.,}\quad P \;=\; 3G - A - B.
\]
The constraint $|P| = r$ then becomes
\[
  |3G - A - B| \;=\; r, \quad\text{i.e.,}\quad \left| G - \frac{A + B}{3} \right| \;=\; \frac{r}{3}.
\]

*Locus.* As $P$ varies over the circle of radius $r$ centred at the origin, $G$ varies over the circle of radius $r/3$ centred at $(A + B)/3$. *The locus of $G$ is a circle of radius $r/3$* centred at the fixed point $(A + B)/3$ (which is itself the centroid of $A, B$, and the origin). \hfill$\blacksquare$

The translation was *geometry-to-vector-algebra*: the geometric notion of "centroid" became the vector average $G = (P + A + B)/3$, which inverts to $P = 3G - A - B$, and the constraint on $P$ becomes a constraint on $G$ that one can read off directly.

---

### Solution to 5.3 — $n$-th Roots of Unity Forming a Right Angle

*Translation.* The $n$-th roots of unity lie on the unit circle in the Argand plane, at angular positions $2\pi k / n$ for $k = 0, 1, \ldots, n - 1$. A triangle with vertices on a circle has a right angle at one of its vertices if and only if the opposite side is a *diameter* of the circle — this is the *converse of Thales' theorem* (the inscribed angle in a semicircle is a right angle, and conversely).

*Applying the converse to our problem.* The triangle with vertices $\omega_1, \omega_2, \omega_3$ on the unit circle has a right angle at $\omega_2$ iff the chord $\omega_1 \omega_3$ is a diameter of the unit circle, iff $\omega_3 = -\omega_1$.

*The condition on $n$.* For $\omega_1$ and $\omega_3 = -\omega_1$ to both be $n$-th roots of unity, $\omega_3 / \omega_1 = -1$ must itself be an $n$-th root of unity. Since $-1 = e^{i\pi}$, the condition is $e^{in\pi} = 1$, i.e., $n\pi$ is an integer multiple of $2\pi$, i.e., $n$ is even.

For a non-degenerate triangle we also need a third $n$-th root $\omega_2 \ne \pm \omega_1$, which requires $n \ge 4$ (the case $n = 2$ has only two roots $\{1, -1\}$ and so no triangle can be formed).

**The configuration exists if and only if $n$ is even and $n \ge 4$.** The smallest such $n$ is $\boxed{n = 4}$, with $\omega_1 = 1$, $\omega_3 = -1$, and $\omega_2 = \pm i$ giving the right-angled triangle $\{1, i, -1\}$ (or $\{1, -i, -1\}$).

*Verification at $n = 6$ (one even value greater than $4$).* The $6$th roots of unity include $\omega_1 = 1$, $\omega_3 = -1$, and $\omega_2 = e^{i\pi/3} = 1/2 + i\sqrt 3 /2$ (among others). The vectors from $\omega_2$ to the other vertices are $\omega_1 - \omega_2 = 1/2 - i\sqrt 3/2$ and $\omega_3 - \omega_2 = -3/2 - i\sqrt 3 /2$. Their real inner product is
\[
  \mathrm{Re}\big[(\omega_1 - \omega_2)\overline{(\omega_3 - \omega_2)}\big] \;=\; (1/2)(-3/2) + (-\sqrt 3/2)(-\sqrt 3/2) \;=\; -3/4 + 3/4 \;=\; 0,
\]
confirming the right angle at $\omega_2$. \hfill$\blacksquare$

**Correction note.** The locked-slate v0.2 answer for this problem was "$n$ is a multiple of $4$", a value that is correct for *the original JEE 2001 problem* (two roots subtending a right angle at the *origin*, not three roots subtending a right angle at $\omega_2$). The reformulated problem in the locked slate has the weaker answer derived above. The slate has been patched to v0.2.5 with this correction; the original JEE 2001 problem (with answer $4 \mid n$) is retained as Chapter 2 PP1.

---

### Solution to 5.4 — Distance from the Origin to a Line in $\mathbb{R}^3$

*Translation.* In vector language, the line through $\vec p = (1, 2, 3)$ in direction $\vec d = (2, -1, 2)$ is the set $\{\vec p + t \vec d : t \in \mathbb{R}\}$. The perpendicular distance from the origin to this line equals
\[
  d \;=\; \frac{|\vec p \times \vec d|}{|\vec d|},
\]
where $\vec p \times \vec d$ is the cross product. (Geometric reading: $|\vec p \times \vec d|$ is twice the area of the triangle formed by $\vec 0, \vec p, \vec p + \vec d$; dividing by $|\vec d|$ — the length of the base from $\vec p$ to $\vec p + \vec d$ — gives the height of the triangle from $\vec 0$, which is the perpendicular distance.)

*Computing the cross product.*
\[
  \vec p \times \vec d \;=\; \det\!\begin{pmatrix} \vec i & \vec j & \vec k \\ 1 & 2 & 3 \\ 2 & -1 & 2 \end{pmatrix} \;=\; \vec i (4 - (-3)) - \vec j (2 - 6) + \vec k (-1 - 4) \;=\; (7,\ 4,\ -5).
\]
(Cofactor expansion along the first row.)

*Magnitudes.*
\[
  |\vec p \times \vec d| \;=\; \sqrt{49 + 16 + 25} \;=\; \sqrt{90} \;=\; 3\sqrt{10}, \qquad |\vec d| \;=\; \sqrt{4 + 1 + 4} \;=\; 3.
\]

*Distance.*
\[
  d \;=\; \frac{|\vec p \times \vec d|}{|\vec d|} \;=\; \frac{3\sqrt{10}}{3} \;=\; \boxed{\sqrt{10}}.
\]

The translation from "perpendicular distance from a point to a line" to "magnitude of a cross product divided by the magnitude of the direction" is the standard formula in $\mathbb{R}^3$, and it is the standard application of Form III. The derivation by *Lagrange multipliers* — minimise $|\vec p + t\vec d - \vec 0|^2$ over $t$, then substitute — gives the same answer, but takes substantially longer and obscures the geometric content.

---

### Solution to 5.5 — Identification of an Argand Locus

*Translation.* The condition $|z - 1| = |z + 1|$ has the immediate geometric reading: *$z$ is equidistant from $1$ and from $-1$*. The set of points equidistant from two given points is the *perpendicular bisector* of the segment joining them.

The segment from $1$ to $-1$ is the segment of the real axis from $-1$ to $1$. Its perpendicular bisector is the line through $0$ perpendicular to the real axis — that is, the *imaginary axis* (equivalently, the $y$-axis).

*Verification by coordinates.* Writing $z = x + iy$,
\[
  |z - 1|^2 \;=\; (x - 1)^2 + y^2, \qquad |z + 1|^2 \;=\; (x + 1)^2 + y^2.
\]
Equality of moduli gives $(x - 1)^2 = (x + 1)^2$, i.e., $-2x = 2x$, i.e., $x = 0$.

The locus is the $y$-axis (excluding the point $z = -1$, but $-1$ is not on the $y$-axis anyway, so the full $y$-axis is the answer). \hfill$\blacksquare$

The Form-I translation gave the answer in one line of geometric reasoning. The Cartesian verification confirms the answer and serves as a check. Both routes are educational; the Form-I route is the one the trained solver uses on a timed exam.

---

### Solution to 5.6 — Complex Argument as Angle

*Polar form.* The complex number $z = 1 + i\sqrt 3$ has modulus
\[
  |z| \;=\; \sqrt{1^2 + (\sqrt 3)^2} \;=\; \sqrt{1 + 3} \;=\; 2.
\]
Its argument is the angle $\theta$ with $\tan\theta = \sqrt 3 / 1 = \sqrt 3$ and $z$ in the first quadrant, hence
\[
  \arg z \;=\; \boxed{\pi / 3}.
\]
Equivalently, $z = 2 e^{i\pi/3} = 2(\cos(\pi/3) + i\sin(\pi/3))$.

*Cubing.* By De Moivre's theorem,
\[
  z^3 \;=\; |z|^3 \, e^{i \cdot 3\arg z} \;=\; 2^3 \, e^{i\pi} \;=\; 8 \cdot (-1) \;=\; -8.
\]
Hence $\arg(z^3) = \boxed{\pi}$, and $z^3$ is the real negative number $-8$.

*Geometric interpretation.* On the Argand plane, the operation "multiply by $z$" is the operation "rotate by $\pi/3$ and scale by $2$." Three applications rotate by $3 \cdot \pi/3 = \pi$ (a half-turn) and scale by $2^3 = 8$. Starting at the point $1 + 0 i$, three applications land at the point $-8 + 0 i$ — the half-turn brings us to the negative real axis, and the scaling by $8$ fixes the magnitude. \hfill$\blacksquare$

The translation $z \leftrightarrow (\,|z|, \arg z\,)$ — Cartesian to polar — is what makes the cubing trivial; in rectangular form $z^3 = (1 + i\sqrt 3)^3$ would require expanding a binomial cube, three lines of arithmetic and two opportunities for sign errors.

---

### Solution to 5.7 — Reverse Triangle Inequality

*Proof.* For any complex numbers $a, b$, the (forward) triangle inequality applied to the decomposition $a = (a - b) + b$ gives
\[
  |a| \;=\; |(a - b) + b| \;\le\; |a - b| + |b|,
\]
hence
\[
  |a| - |b| \;\le\; |a - b|.
\]
Symmetrically (writing $b = (b - a) + a$ and using $|b - a| = |a - b|$),
\[
  |b| - |a| \;\le\; |a - b|.
\]
Combining the two inequalities,
\[
  \big||a| - |b|\big| \;\le\; |a - b|,
\]
which is the reverse triangle inequality. \hfill$\blacksquare$

*Equality case.* Equality holds in the forward triangle inequality $|u + v| \le |u| + |v|$ iff $u$ and $v$ are *non-negative real scalar multiples of one another* (geometrically: they point in the same direction from the origin, or one of them is zero). Applying this to $a - b$ and $b$: equality holds iff $a - b = \lambda b$ for some $\lambda \ge 0$ (or one of them is zero). This rearranges to $a = (1 + \lambda) b$, i.e., $a$ is a non-negative real scalar multiple of $b$. Equivalently, $a$ and $b$ *lie on the same ray from the origin* — they share an argument (when both are non-zero).

The geometric reading: $|a|$ is the distance from the origin to $a$, $|b|$ the distance to $b$, and $|a - b|$ the distance from $a$ to $b$ — the three sides of a triangle with vertices $0, a, b$. The reverse triangle inequality is the assertion that *the third side of a triangle is at least the absolute difference of the other two*, a fact familiar from Euclidean geometry. The complex-number proof and the Euclidean proof are the same proof, written in two languages — exactly the chapter's central theme. \hfill$\blacksquare$

---

*End of Chapter 8.*

