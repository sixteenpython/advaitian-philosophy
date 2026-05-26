# Cursor-Joshi.md — Consolidated Memory of K.D. Joshi's *Educative JEE Mathematics*

*Persistent reference file. Built so that future sessions need not re-read the full 1039-page Joshi PDF. When working on Pillar 2 of the Advaitian Book, this file is the **primary lookup**; the raw text `my_references/edujeejoshi2ed.txt` is the **secondary verification source**.*

**Book metadata.**
- Title: *Educative JEE Mathematics*
- Author: K.D. Joshi
- Edition: 2nd
- Length: 1039 pages
- Chapters: 24 (plus Appendix on Matrices and Answer-Key Solutions)
- Source files: `my_references/edujeejoshi2ed.pdf` (canonical), `my_references/edujeejoshi2ed.txt` (searchable extraction, 52,591 lines)
- Text-file line ranges: main book lines 67–47,704; solutions appendix 47,705–52,591

**Voice/pedagogy signature.** Joshi writes in a deeply discursive, pedagogically explicit register: each chapter opens with a *Main Problem*, then provides a sequence of numbered *Comments* (worked examples + technique-by-technique commentary), then an *Exercises* section drawn heavily from JEE / RMO / INMO. He repeatedly stresses (a) the difference between mechanical and *insightful* solutions, (b) the role of bijections and decompositions in counting, (c) the role of symmetry and invariance in elegant proofs, (d) the discipline of *checking* one's argument by recasting it formally. The Advaitian Pillar 2 voice should draw on Joshi's *meta-commentary* register — not his prose density.

**Version.** 1.0 — May 26 2026 (initial consolidated extraction — all 24 chapters summarised; indices populated).
**Maintenance rule.** Each time a Pillar 2 chapter is drafted, refresh that chapter's row of the cross-archetype table in §IV below.
**Status.** Comprehensive. All 24 chapters of Joshi have been read and distilled. Indices by competition (§III), archetype (§IV), cross-references (§V), theorems (§VI), and voice samples (§VII) are populated. **This file is the canonical Joshi memory for all Pillar 2 work.**

---

## I. Chapter-by-Chapter Index

| # | Title | Pages | Text-file lines | Pillar 2 primary archetype | Pillar 2 secondary archetypes |
|---|---|---|---|---|---|
| 1 | Counting Problems | 1–32 | 67–1614 | #1 Invariance, #13 Combinatorial, #15 Bijection | #9 Domain Constraints, #14 Parity, #17 DOF |
| 2 | Basic Algebra | 32–84 | 1615–4317 | #2 Symmetry, #5 Substitution, #19 Pivoting | #1 Invariance (Vieta), #18 Recursion (AP/GP/HP) |
| 3 | Theory of Equations | 84–124 | 4318–6430 | #1 Invariance (Vieta), #2 Symmetry, #16 Reverse Engineering | #5 Substitution (Tschirnhaus), #9 Domain, #11 Existence |
| 4 | Number Theory | 124–157 | 6431–8177 | #14 Parity, #18 Recursion, #1 Invariance | #4 Hidden Structure (Lucas/Kummer), #15 Bijection |
| 5 | Binomial Identities | 157–190 | 8178–10328 | #15 Bijection, #5 Substitution, #1 Invariance | #18 Recursion (Pascal), #4 Hidden Structure |
| 6 | Inequalities | 190–234 | 10329–12622 | #10 Inequality, #12 Extremal, #2 Symmetry | #5 Substitution (normalisation), #7 Normalization, #6 Linearization |
| 7 | Trigonometric Identities | 234–260 | 12623–14056 | #1 Invariance ($\sin^2+\cos^2=1$), #2 Symmetry | #5 Substitution (Weierstrass), #20 Analogy (Euler) |
| 8 | Geometry | 260–287 | 14057–15484 | #2 Symmetry, #3 Duality (pole-polar), #1 Invariance (Klein) | #15 Bijection, #4 Hidden Structure |
| 9 | Coordinate Geometry | 287–329 | 15485–17597 | #5 Substitution, #8 Domain Translation, #19 Pivoting | #1 Invariance (rigid-motion), #2 Symmetry |
| 10 | Trigonometric Equations | 329–362 | 17598–19337 | #5 Substitution, #11 Existence, #9 Domain | #2 Symmetry (periodicity), #18 Recursion |
| 11 | Solution of Triangles | 362–391 | 19338–20897 | #1 Invariance (law of sines/cosines), #2 Symmetry | #3 Duality (in/circumradius), #9 Domain (triangle inequality) |
| 12 | Heights and Distances | 391–409 | 20898–21824 | #9 Domain Constraints, #5 Substitution | #11 Existence, #20 Analogy |
| 13 | Maxima, Minima, Concavity | 409–444 | 21825–23604 | #12 Extremal, #9 Domain, #5 Substitution | #2 Symmetry, #10 Inequality |
| 14 | Trigonometric Optimisation | 444–475 | 23605–25199 | #12 Extremal, #2 Symmetry | #5 Substitution (Weierstrass), #10 Inequality (Cauchy-Schwarz/Jensen) |
| 15 | Limits, Continuity, Derivatives | 475–512 | 25200–27340 | #11 Existence (IVT), #6 Linearization | #5 Substitution (L'Hôpital), #20 Analogy |
| 16 | Theoretical Calculus | 512–545 | 27341–29050 | #11 Existence (MVT/Rolle), #6 Linearization, #1 Invariance | #18 Recursion, #20 Analogy |
| 17 | Areas and Antiderivatives | 545–593 | 29051–31905 | #5 Substitution, #1 Invariance (parametrisation) | #2 Symmetry (even/odd), #18 Recursion (reduction formulas) |
| 18 | Definite Integrals | 593–624 | 31906–33739 | #1 Invariance ($\int_0^a f = \int_0^a f(a-x)$), #2 Symmetry, #5 Substitution | #18 Recursion (reduction) |
| 19 | Differential Equations | 624–660 | 33740–35364 | #5 Substitution, #6 Linearization (integrating factors), #1 Invariance | #11 Existence, #18 Recursion |
| 20 | Functional Equations | 660–675 | 35365–36317 | #5 Substitution, #11 Existence, #1 Invariance | #18 Recursion, #20 Analogy |
| 21 | Vectors | 675–710 | 36318–38169 | #5 Substitution, #1 Invariance (rotation), #3 Duality | #2 Symmetry, #8 Domain Translation |
| 22 | Finitistic Probability | 710–744 | 38170–39932 | #13 Combinatorial, #15 Bijection, #1 Invariance (linearity of expectation) | #17 DOF, #20 Analogy |
| 23 | Infinitistic Probability | 744–776 | 39933–41675 | #18 Recursion, #1 Invariance (stationary distributions) | #6 Linearization, #11 Existence |
| 24 | Miscellaneous Tips and Review | 776–end | 41676–47704 | **ALL TWENTY** (compendium chapter) | — |

---

## II. Chapter Details

<!-- CH1_BEGIN -->
### Chapter 1: Counting Problems (pp. 1–32; lines 67–1614)

**Topic summary.** The four basic elementary counting techniques: decomposition, complementary counting, products, transformation (i.e., bijection). Joshi opens with a *Main Problem* (permutations of length 6 of 9 things, 5 alike, 4 distinct → answer 1044) and uses it to introduce all four techniques in a single solution.

**Key formulas/theorems established.**
- ${}^nP_k = n!/(n-k)!$ — permutations of length $k$ from $n$ objects.
- ${}^nC_k = \binom{n}{k} = n!/[k!(n-k)!]$ — combinations.
- $|P(S)| = 2^n$ for $|S| = n$ — power-set theorem with two proofs (induction + binary-sequence bijection).
- Selection with repetitions: $\binom{n+k-1}{k}$ via stars-and-bars bijection.
- Catalan numbers: $C_n = \binom{2n}{n}/(n+1)$ via André's reflection bijection (Comment 6).

**Comments (worked examples).**
1. *Comment 1.* JEE 2002 — arrangements of BANANA where two N's are not adjacent (answer 40). Plus JEE 1989 — five-digit numbers divisible by 3 from $\{0,\ldots,5\}$ (answer 216) — **routed to Pillar 2 Ch. 1 WE1.**
2. *Comment 2.* JEE 1979 — 52 cards to 4 players ($52!/(13!)^4$); cards to 4 piles 17/17/17/1 ($52!/[6(17!)^3]$); $2n$ players to $n$ pairs ($(2n)!/[2^n n!]$ — product of odd integers).
3. *Comment 3.* JEE 1981 — 5 balls into 3 boxes none empty (answer 150).
4. *Comment 4.* JEE 1979 — 6 boys + 6 girls in row; (i) girls together prob = $1/132$; (ii) alternating prob = $1/462$. **(i) routed to Pillar 2 Ch. 1 PP1.**
5. *Comment 5.* JEE 1983 — $m$ men + $n$ women, no two women adjacent. Answer $m! \cdot \binom{m+1}{n} n! = m!(m+1)!/(m-n+1)!$. **Routed to Pillar 2 Ch. 13 / Ch. 15.**
6. *Comment 6.* Catalan numbers via André's bijection (balanced parenthesis arrangements).
7. *Comment 7+.* Continued counting techniques — Venn diagrams, double counting (the JEE 1981 30-sets-of-5 / $n$-sets-of-3 problem is **Comment 10, routed to Pillar 2 Ch. 1 WE2**).
8. *Comment 11.* Generating functions intro — coefficient extraction as counting tool.
9. *Comment 12.* Mathematical puzzles — twelve-coins puzzle (information-theoretic).

**Exercises (selected, by competition source).**
- *1.4.* JEE 1988 — six "+" and four "−" arrangements with no two "−" adjacent (answer $\binom{7}{4} = 35$). **Routed to Pillar 2 Ch. 15 PP1.**
- *1.25.* Compositions of integer $n$ into $m$ parts.
- *1.27.* Stirling numbers of the 2nd kind.
- *1.29.* Alternate solution to balls/boxes problem.
- *1.31–1.35.* Catalan-number applications (triangulations, Dyck paths, etc.).
- *1.37.* Knockout-tournament bijection problem.
- *1.40+.* Various stretch problems.

**Joshi's pedagogical observations (voice samples).**
- "It is to be noted that usually, it is a suitable combination of techniques rather than a single technique that works best."
- "A good decomposition may not always exist and even when it does, it may not always be obvious. In such cases, hitting the right decomposition is a thrilling experience."
- "Three most common pitfalls in counting arguments: certain unwanted elements get counted, some wanted elements do not get counted, while some elements get counted more than once."
- Reflection on "elegant solutions": "They take you directly to the destination, often bypassing the steps one would normally encounter in a straightforward approach."
<!-- CH1_END -->

<!-- CH2_BEGIN -->
### Chapter 2: Basic Algebra (pp. 32–84; lines 1615–4317)

**Topic summary.** Progressions (AP/GP/HP) and means (AM/GM/HM), recursively defined sequences, exponentials/logarithms, polynomials (intro), binomial theorem, complex numbers (intro + Argand diagram), matrices, determinants. Joshi calls this the "basic prerequisite" chapter — many topics here are *combined* with other topics in later chapters' problems.

**Main Problem.** *For $n \ge 3$, let $S_n = \sum_{i<j<k} ijk$ where the sum is over distinct triples from $\{1,\ldots,n\}$. Find $S_{10}$.* **Answer:** $18150$. **Technique:** expand $(1+2+\cdots+n)^3$, classify terms by multiplicity, solve for $S_n = \tfrac{1}{48}n^2(n+1)^2(n^2-3n+2)$.

**Key formulas/theorems established.**
- $\sum_{i=1}^n i = n(n+1)/2$ (Gauss schoolboy trick).
- $\sum_{i=1}^n i^2 = n(n+1)(2n+1)/6$, $\sum_{i=1}^n i^3 = n^2(n+1)^2/4$.
- AP sum: $S_n = na + n(n-1)d/2$.
- GP sum: $S_n = a(r^n - 1)/(r-1)$ for $r \ne 1$.
- $H_n = 1 + 1/2 + \cdots + 1/n$ — harmonic number, $H_n \approx \ln n$ for large $n$.
- AM ≥ GM ≥ HM (forward-referenced to Ch. 6).
- Complex numbers introduced; $z = re^{i\theta}$ in Argand diagram.
- Matrices, determinants up to 3×3, Hermitian/skew-Hermitian, trace, characteristic polynomial introduced.

**Comments highlights (23 total).**
- *Comment 6.* JEE 1979 — $x, y, z$ in both AP and GP at positions $p, q, r$ → $x^{y-z} y^{z-x} z^{x-y} = 1$. **Routed to Pillar 2 Ch. 2 WE1.**
- *Comments 12–14.* Argand diagram, polar form of complex numbers, $n$-th roots of unity.
- *Comments 21–23.* Matrix algebra and determinant expansion.

**Exercises (notable — competition-sourced).**
- *2.1.* JEE 1980 — Polygon, angles in AP, smallest $120°$, common diff $5°$ → find number of sides. **(Note: this is the original Pillar 1 polygon-AP example reserved for Pillar 1 §5.7.)**
- *2.2.* JEE 1982 — $\sum_{i=1}^{n-1} \frac{1}{\sqrt{a_i} + \sqrt{a_{i+1}}} = \frac{n-1}{\sqrt{a_1} + \sqrt{a_n}}$. **Ch. 18 Recursion candidate.**
- *2.3(a).* JEE 1996 — For odd $n$: $n^3 - (n-1)^3 + \cdots + (-1)^{n-1} 1^3$.
- *2.3(b).* JEE 1988 — Sum of $1/2 + 3/4 + 7/8 + \cdots$.
- *2.3(c).* JEE 1988 — Series $1^2 + 2\cdot 2^2 + 3^2 + 2\cdot 4^2 + \ldots$ for odd $n$.
- *2.3(d).* JEE 2000 — Product of 4 consecutive AP terms plus $d^4$ is a square. **Ch. 14 Parity candidate.**
- *2.4.* JEE 1979 — HM=$4$, $2A + G^2 = 27$ → find two numbers.
- *2.5.* JEE 1982 — GP with $p$-th=27, $q$-th=8, $r$-th=12, find condition on $p,q,r$.
- *2.6.* JEE 1983 — three numbers in $(2, 18)$, sum 25, AP+GP conditions.
- *2.7.* JEE 1988 — AP/GP/HP equal at first and $(2n-1)$-st terms; what holds for $n$-th term? (A) all equal (B) $a \ge b \ge c$ (C) $a+c = b$ (D) $ac - b^2 = 0$.
- *2.8.* JEE 2002 (modified) — $a, b, c$ in AP, $a^2, b^2, c^2$ in GP, $a + b + c = 3/2$, $a < b < c$ → find $a$.
- *2.9.* JEE 1999 — Squares $S_n$ with $|S_{n+1}|$-diagonal = $|S_n|$-side.
- *2.10.* Various — JEE 2002, 1998, 1999, 1997* — A/G/H mean compound problems.
- *2.11.* JEE 1998 — AP with $T_m = 1/n$, $T_n = 1/m$ → $T_{mn} = ?$.
- *2.13.* JEE 1992 — $(x + \sqrt{x^2-1})^5 + (x - \sqrt{x^2-1})^5$ is a polynomial in $x$; determine degree.
- *2.14.* JEE 1978 — Recurrence for *Gauss binomial coefficient* $(m, n)$. **Ch. 18 Recursion candidate.**
- *2.18.* JEE 1995 — $iZ^3 + Z^2 - Z + i = 0$ → $|Z| = 1$. **Ch. 9 Domain Constraints / Ch. 8 Domain Translation candidate.**
- *2.19.* JEE 1998 — $\sum_{n=1}^{13}(i^n + i^{n+1})$.
- *2.22.* JEE 1988 — Simplify $|az_1 - bz_2|^2 + |bz_1 + az_2|^2$. **Ch. 2 Symmetry candidate (orthogonality identity).**
- *2.27.* JEE 1988, 1998, 1993, 1996 — Various $3\times 3$ determinants.
- *2.28.* JEE 1981 — Determinants of order 3 with entries 0/1; sizes of $B$ (det=1) and $C$ (det=−1).
- *2.29.* JEE 1981, 1982, 1999 — Polynomial determinant identities.
- *2.30.* JEE 1997*, 1986 — Conditions for determinants to vanish (AP/GP/HP).
- *2.31(a–d).* Symmetric polynomial determinants — $a^3+b^3+c^3-3abc$, etc.

**Joshi's pedagogical observations.**
- Gauss schoolboy story (sum reversal trick) — voice sample for Pillar 2 vignette register.
- "If you are able to paraphrase the argument rigorously by introducing appropriate sets and functions, then such mistakes can be avoided" — formalism as error-prevention discipline.
- "The harmonic mean appears less frequently, is defined as the reciprocal of the arithmetic mean of the reciprocals" — Joshi's elegant compression of definitions.

**Pillar 2 routing.** *Primary candidates:* WE1 of Ch. 2 (the JEE 1979 AP/GP problem); symmetric-polynomial determinant identities (Ex. 2.31) for Ch. 2 stretch; Gauss binomial recurrence (Ex. 2.14) for Ch. 18.
<!-- CH2_END -->

<!-- CH3_BEGIN -->
### Chapter 3: Theory of Equations (pp. 84–124; lines 4318–6430)

**Topic summary.** Polynomial equations: quadratic/cubic/quartic formulas, fundamental theorem of algebra, Vieta's relations (sum/product of roots → coefficients), Newton's identities (sums of powers of roots), discriminant. Systems of linear equations and matrix-based methods. **The single most important Joshi chapter for Pillar 2 Ch. 1 (Invariance) and Ch. 16 (Reverse Engineering)** — Vieta's relations are *the* canonical Type-III invariant family.

**Main Problem.** *Find $\sum \alpha^3$ where $\alpha, \beta, \gamma, \delta$ are roots of $x^4 - 2x^3 + x^2 - 5x + 1 = 0$.* **Answer:** $17$. **Technique:** Use Vieta's relations $\sum\alpha = 2$, $\sum\alpha\beta = 1$, $\sum\alpha\beta\gamma = 5$, $\alpha\beta\gamma\delta = 1$; expand $(\sum\alpha)^3$ and rearrange.

**Key formulas/theorems established.**
- *Remainder theorem.* $p(x) = q(x)(x-\alpha) + p(\alpha)$ — $\alpha$ is a root iff $(x-\alpha)$ is a factor.
- *Multiplicity.* If $(x-\alpha)^r$ divides $p$ but $(x-\alpha)^{r+1}$ does not, then $\alpha$ has multiplicity $r$.
- *Fundamental Theorem of Algebra.* Every complex polynomial of degree $\ge 1$ has at least one complex root.
- *Theorem 1.* Every real polynomial of odd degree has at least one real root (in fact, an odd number).
- *Vieta's relations* for $p(x) = a_n x^n + \cdots + a_0$ with roots $r_1, \ldots, r_n$:
  - $\sum r_i = -a_{n-1}/a_n$
  - $\sum_{i<j} r_i r_j = a_{n-2}/a_n$
  - ...
  - $\prod r_i = (-1)^n a_0/a_n$.
- *Newton's identities.* $s_r = \sum r_i^r$ satisfies a linear recurrence with elementary symmetric functions as coefficients.
- *Discriminant.* $\Delta = \prod_{i<j}(r_i - r_j)^2$ — vanishes iff $p$ has a repeated root. Expressed in terms of coefficients.
- *Intermediate Value Property* (Theorem in Comment 15): polynomial $f$ on $[x_1, x_2]$ with $f(x_1), f(x_2)$ of opposite sign has a zero in between.
- *Vandermonde determinant.* $D(\alpha_1, \ldots, \alpha_n) = \prod_{i<j}(\alpha_j - \alpha_i)$.

**Comments highlights (18 total).**
- *Comments 1–3.* Polynomial factorisation, Fundamental theorem of algebra, attempts to find roots directly.
- *Comment 4.* Theorem on real polynomials of even degree (sign analysis).
- *Comments 5–8.* Vieta's formulas in detail.
- *Comments 9–11.* Newton's identities.
- *Comments 12–15.* Roots of unity, Tschirnhaus transformation (depressed cubic), IVT for polynomials.
- *Comments 16–18.* Linear systems, determinant of coefficient matrix (Cramer's rule), 3-variable systems.

**Exercises (notable — competition-sourced).**
- *3.1.* JEE 1984 — Number of roots of $x - 2/(x-1) = 1 - 2/(x-1)$.
- *3.2.* Vieta's relations: $a^4(\beta+\gamma+\delta-\alpha)(\ldots) = -b^4 + 4ab^2 c - 8a^2 bd + 16a^3 e$.
- *3.3.* Discriminant of $x^n + ax + b$ in closed form. **Ch. 1 Invariance / Ch. 16 Reverse Engineering candidate.**
- *3.4.* $s_r$ for $x^n - x^{n-1} - \cdots - x - 1 = 0$ — Newton's identities application. Answer: $s_r = 2^r - 1$. **Ch. 18 Recursion candidate.**
- *3.5.* Sum of reciprocal-powers of roots — telescoping pattern.
- *3.6.* JEE 1997 — $p, q$ roots of $x^2 - 2x + A = 0$; $r, s$ roots of $x^2 - 18x + B = 0$; $p<q<r<s$ in AP → find $A, B$. **Ch. 16 Reverse Engineering candidate.**
- *3.7(a).* JEE 1979 — $f(x)$ specific polynomial, find $f(6)$.
- *3.7(b).* JEE 1978 — Polynomial $> 3$ degree, remainders 2, 1, −1 on division by $(x-1), (x+2), (x+1)$; find remainder on division by product.
- *3.8.* JEE 1986, 1978, 1997*, 1987, 1978 — Various $\log/\exp$ equations.
- *3.9.* JEE 1992, 1990, 1990 — HM/GM ratio, log AP, system of equations.
- *3.10(a).* JEE 1983 — One root = $n$-th power of other → $(ac^n)^{1/(n+1)} + (a^n c)^{1/(n+1)} + b = 0$. **Ch. 1 Invariance candidate.**
- *3.10(b).* JEE 1992 — $(x-a)(x-b) = c$ has roots $\alpha, \beta$; find roots of $(x-\alpha)(x-\beta) + c = 0$. **Ch. 16 Reverse Engineering candidate.**
- *3.10(c).* JEE 2001 — $a^3 x^2 + abcx + c^3 = 0$ roots in terms of $\alpha, \beta$ (roots of $ax^2 + bx + c = 0$).
- *3.10(d).* JEE 1979 — Common root condition for two quadratics.
- *3.10(e).* JEE 1986 — $x^2 + ax + b = 0$ and $x^2 + bx + a = 0$ ($a \ne b$) common root → $a + b = ?$. Answer: $-1$. **Ch. 19 Pivoting candidate.**
- *3.11.* JEE 1979, 1984, 1985, 1980 — Quadratic root nature problems.
- *3.13.* JEE 1985 — $a, b, c$ in GP and common root of two quadratics → progression type of $d/a, e/b, f/c$.
- *3.15.* JEE 1989 modified — IVT-style problems for quadratics. **Ch. 11 Existence candidate.**
- *3.18(b).* JEE 1979 — $\{x+2y+2z=1, 2x+4y+4z=9\}$ number of solutions.
- *3.18(c).* JEE 2002 — System with parameter $k$, find $k$ for $\infty$ solutions.
- *3.21(a).* JEE 1983 — $\lambda$ system has solution.
- *3.21(b).* JEE 1984 — $\lambda$ non-trivial solution.
- *3.26.* Vandermonde determinant — proof + applications.
- *3.29.* $a+b+c=0$ → $(a^5+b^5+c^5)/5 = ((a^2+b^2+c^2)/2)((a^3+b^3+c^3)/3)$. **Ch. 2 Symmetry candidate (symmetric power identity).**

**Joshi's pedagogical observations.**
- "For $n \ge 5$… no formula for the roots of a general polynomial of degree 5 or above is known. Not for lack of efforts, but because there is something inherently impossible about such a formula — something like making two parallel lines meet." — Joshi's elegant framing of Abel-Galois (without naming them).
- "[Vieta's relations] are *the* canonical example of how the coefficients of a polynomial cannot see the order of the roots — only symmetric functions of the roots are accessible from coefficients alone." (paraphrased)
- "A particular polynomial equation can sometimes be solved if we can identify at least some of its roots by inspection or otherwise."

**Pillar 2 routing.** *Primary:* Ch. 1 Invariance (Vieta = canonical Type-III invariant — already used Ex. 3.10(a)-type problems in Ch. 1); Ch. 16 Reverse Engineering (Ex. 3.6, 3.10(b)); Ch. 19 Pivoting/Elimination (Ex. 3.10(d), 3.10(e)); Ch. 11 Existence (Ex. 3.15 IVT). *Secondary:* Ch. 2 Symmetry (symmetric polynomial identities Ex. 3.29).
<!-- CH3_END -->

<!-- CH4_BEGIN -->
### Chapter 4: Number Theory (pp. 124–157; lines 6431–8177)

**Topic summary.** Divisibility of integers, Kummer's theorem (parity of binomial coefficients via base-$p$ carries), Fermat's and Wilson's theorems, induction-based divisibility proofs, modular arithmetic, Lucas's theorem (stated, not proved), surds, Euler totient function. Joshi explicitly notes: *"In JEE, number theory problems are mostly asked as problems on induction."*

**Main Problem.** *Find the number of integers $n$ in $10 \le n \le 1000$ such that $\binom{n}{k}$ is odd for every $k$ with $0 \le k \le n$.* **Answer:** $6$ (namely $15, 31, 63, 127, 255, 511$ — i.e., $n = 2^m - 1$). **Technique:** Kummer's theorem — $\binom{n}{k}$ odd for all $k$ iff $n$'s binary representation is all 1s, i.e., $n = 2^m - 1$. **Routed to Pillar 2 Ch. 1 WE3.**

**Key formulas/theorems established.**
- Binomial coefficient extraction: $\binom{n}{k} = \binom{n}{k-1}\cdot\frac{n-k+1}{k}$ (Eq. 1) — used in main problem.
- Kummer's theorem (binary expansion): $\binom{n}{k}$ odd iff base-2 expansion of $k$ is a "submask" of base-2 expansion of $n$.
- Rule of 3, 9, 11 (digit-sum divisibility).
- Fermat's little theorem: $m^p \equiv m \pmod p$ for prime $p$.
- Generalised Fermat (Euler): $m^{\phi(n)} \equiv 1 \pmod n$ for $\gcd(m, n) = 1$.
- Wilson's theorem: $(p-1)! \equiv -1 \pmod p$ for prime $p$.
- Chinese Remainder Theorem (Ex. 4.13).
- Lucas's theorem (stated): $\binom{n}{k} \equiv \prod \binom{n_i}{k_i} \pmod p$ in base $p$.
- Euler totient $\phi(n)$, multiplicativity.
- Fibonacci recurrence: $F_{n+1} = F_n + F_{n-1}$ with identities $F_{n+m} = F_m F_{n+1} + F_{m-1} F_n$ etc.

**Comments highlights (19 total).**
- *Comments 1–2.* Setting up the main problem; binary representations; experimentation as discovery.
- *Comment 8.* Three JEE problems on divisibility by 24:
  - JEE 1982 — $7^{2n} + 2^{3n-3}\cdot 3^{n-1}$ divisible by 25. **Routed to Pillar 2 Ch. 18 WE2.**
  - JEE 1983 — for odd $n$, $n(n^2 - 1)$ divisible by 24. **Routed to Pillar 2 Ch. 1 PP3.**
  - JEE 1985 — $2\cdot 7^n + 3\cdot 5^n - 5$ divisible by 24. **Routed to Pillar 2 Ch. 1 PP2.**
- *Comment 9.* JEE 1985 — product of any $r$ consecutive integers divisible by $r!$. **Double induction, Ch. 18 PP2.**
- *Comment 10.* JEE 1992 — $\alpha^n + \beta^n$ integer, not divisible by $p$, where $\alpha, \beta$ roots of quadratic. **Ch. 18 candidate.**
- *Comments 11–14.* Modular arithmetic, congruences, Chinese Remainder.
- *Comments 15–17.* Kummer + Lucas theorems.
- *Comments 18–19.* Surds, quadratic surds, $\sqrt 2$ irrationality.

**Exercises (notable — competition-sourced).**
- *4.1.* JEE 1985 — $n_1, n_2, \ldots, n_p$ positive integers, $q$ are odd, $\sum n_i$ odd → is $q$ necessarily odd? (Yes — parity of sum determines parity of odd-count.) **Ch. 14 Parity candidate.**
- *4.2.* JEE 1984 — Sum of integers $1$ to $100$ divisible by $2$ or $5$.
- *4.3.* JEE 1998 — $f(x) = Ax^2 + Bx + C$ integer-valued on $\mathbb{Z}$ iff $2A, A+B, C \in \mathbb{Z}$. **Ch. 4 Hidden Structure / Ch. 14 Modularity candidate.**
- *4.4.* $\binom{2m-1}{m}$ even except when $m$ is a power of 2. **Cross-references Pillar 2 Ch. 1 WE3.**
- *4.5.* JEE 1990 — Three-digit numbers $A28, 3B9, 62C$ all divisible by $k$ → determinant $\det\begin{pmatrix}A & 3 & 6\\8 & 9 & C\\2 & B & 2\end{pmatrix}$ divisible by $k$.
- *4.6.* Rule of 3/9/11 + base-other-than-10.
- *4.7.* Friday-the-13th: in any calendar year there is at least one and at most three Friday-13ths.
- *4.8(a).* RMO — $5^{12} + 2^{10}$ not prime.
- *4.8(d).* Euclid's infinity of primes (combinatorial argument).
- *4.8(e).* Infinitely many primes $4k - 1$. (Joshi notes $4k + 1$ harder.)
- *4.8(f).* Euler's prime-generating polynomial $x^2 + x + 41$ prime for $x = 0..39$.
- *4.8(g).* No polynomial gives only primes (proof by counterexample).
- *4.9.* JEE 1984, 1998 — Divisor count for $n = p_1^{a_1}\cdots p_k^{a_k}$.
- *4.10.* $H_n = 1 + 1/2 + \cdots + 1/n$ not integer for $n \ge 2$.
- *4.11–4.12.* GCD, LCM properties; cancellation law mod $n$.
- *4.13.* Chinese Remainder Theorem (full statement + applications). **Ch. 14 Parity/Modularity primary source.**
- *4.15.* JEE 1999 — $m, n$ random in $[1, 100]$: $P(5 \mid 7^m + 7^n)$.
- *4.16.* JEE 1984 — $p^{n+1} + (p+1)^{2n-1}$ divisible by $p^2 + p + 1$. **Ch. 18 Recursion / Ch. 14 candidate.**
- *4.17.* JEE 2002 — $(25)^{n+1} - 24n + 5735$ divisible by $24^2$. **Ch. 18 Recursion candidate.**
- *4.18.* $pq \mid p^{q-1} + q^{p-1} - 1$ for distinct odd primes.
- *4.19.* Both $16^{99} - 1$ and $18! + 1$ divisible by $437$.
- *4.20.* $\gcd(m, 30) = 1$ → $240 \mid m^4 - 1$.
- *4.22.* Pythagorean triples characterisation. **Ch. 4 Hidden Structure / Ch. 14 candidate.**
- *4.26.* Fibonacci identities — $F_{n+1}F_{n-1} - F_n^2 = (-1)^n$ etc.
- *4.27.* JEE 1990 — $\log_2 7$ irrational.
- *4.28.* JEE 1981 — Is $x \sim y \iff x - y + \sqrt 2$ irrational an equivalence relation? No.
- *4.32.* JEE 1997 — Sum of rational terms in $(\sqrt 2 + 3^{1/5})^{10}$. **Ch. 4 Hidden Structure.**
- *4.33.* JEE 1978 — Square of $(\sqrt{26} - 15\sqrt 3)/(5\sqrt 2 - \sqrt{38 + 5\sqrt 3})$ rational.
- *4.34.* JEE 1980 — Surd simplification.
- *4.36.* For prime $p > 3$: $(p-1)!\sum_{k=1}^{p-1}\frac{1}{k}$ divisible by $p$; deduce $(2p)! - 2(p!)^2$ divisible by $p^4$.
- *4.37.* Euler totient $\phi(n)$ — definition, multiplicativity, formula.
- *4.38.* Generalised Fermat: $m^{\phi(n)} \equiv 1 \pmod n$.
- *4.39.* Combinatorial proof of Fermat (necklace colourings).
- *4.40.* Combinatorial proof of Wilson (cyclic guest arrangements). **Ch. 14 Parity candidate.**

**Joshi's pedagogical observations.**
- "Number theory abounds in problems which are so simple to state that anybody who has completed primary school can understand the statement but whose solutions are extremely difficult."
- On the Main Problem: "When one cannot readily think of the key idea that will lead to the solution, it often pays to do some experimentation, especially in problems involving natural numbers."
- "The ability to quickly identify a few such cases where the experiment is destined to fail is a valuable asset in any experiment, whether in mathematics or in real life." — voice sample for Pillar 3.

**Pillar 2 routing.** *Primary:* **Ch. 14 Parity/Modularity** (Ex. 4.1, 4.3, 4.4, 4.7, 4.13, 4.15-4.18, 4.22, 4.40) — this chapter is the **richest source for Ch. 14**. *Secondary:* Ch. 1 Invariance (Kummer/Lucas — WE3 already routed; Comment 8 problems routed as PP2-3); Ch. 18 Recursion (Ex. 4.16, 4.17, 4.26 Fibonacci identities, Comment 8 JEE 1982); Ch. 4 Hidden Structure (Ex. 4.3, 4.22 Pythagorean triples, 4.32 surds).
<!-- CH4_END -->

<!-- CH5_BEGIN -->
### Chapter 5: Binomial Identities (pp. 157–190; lines 8178–10328)

**Topic summary.** Identities involving $\binom{n}{k}$. Joshi structures the chapter around **four methods of proof**: (i) direct computation, (ii) mathematical induction, (iii) generating functions / coefficient extraction, (iv) combinatorial bijection. The fourth method is presented as the most elegant when available. **Primary source for Pillar 2 Ch. 15 (Bijection / Correspondence).**

**Main Problem.** *JEE 2000 (modified): If $\binom{31}{q}$ is a positive integer with $q \le 50$ and $\sum_{r=30}^{98}(99-r)\binom{r}{30} + \binom{30}{30}$ telescopes to $\binom{100}{q}$, find $q$.* **Answer:** $q = 32$. **Technique:** Hockey-stick identity $\sum_{r=m}^{n}\binom{r}{m} = \binom{n+1}{m+1}$ applied twice.

**Key formulas/theorems established.**
- Reduction (Pascal) formula: $\binom{r}{k} + \binom{r}{k+1} = \binom{r+1}{k+1}$.
- Hockey-stick identity: $\sum_{r=m}^{n}\binom{r}{m} = \binom{n+1}{m+1}$.
- Vandermonde's identity: $\sum_{k}\binom{p}{k}\binom{q}{n-k} = \binom{p+q}{n}$.
- $\sum_k \binom{n}{k} = 2^n$, $\sum_k (-1)^k\binom{n}{k} = 0$, $\sum_k k\binom{n}{k} = n2^{n-1}$.
- $\sum_k \binom{n}{k}^2 = \binom{2n}{n}$.
- Multinomial coefficients $\binom{n}{n_1, n_2, \ldots, n_k} = n!/(n_1! n_2! \cdots n_k!)$.
- Pascal triangle pictorial.
- $\sum_{k}\binom{n-k}{k} = F_{n+1}$ (Fibonacci) — Ex. 5.16.

**Comments highlights (20 total).**
- *Comments 1–4.* Direct & inductive proofs; hockey-stick identity.
- *Comment 5.* Coefficient-extraction method (generating-function start).
- *Comments 6–9.* $\sum_k \binom{n}{k}^2 = \binom{2n}{n}$ — three different proofs (direct, generating function, combinatorial).
- *Comment 10.* Multinomial theorem.
- *Comments 11–13.* Combinatorial proofs (bijection method); Tomescu's results.
- *Comment 14.* The "selecting a captain" combinatorial identity.
- *Comments 15–17.* Stirling numbers of the second kind, surjections.
- *Comments 18–20.* Power-series and partition identities, $1 + x + x^2 = (1-x^3)/(1-x)$ type.

**Exercises (notable — competition-sourced and identity-class).**
- *5.1(i).* Double-selection: $\binom{n}{k}\binom{k}{r} = \binom{n}{r}\binom{n-r}{k-r}$. **Ch. 15 Bijection candidate.**
- *5.1(ii).* Hockey-stick recast.
- *5.1(iii).* Vandermonde — note special case $n = 0$ and $p = q$.
- *5.1(iv).* $\sum_k \binom{n}{k}\binom{k}{m} = \binom{n}{m}2^{n-m}$.
- *5.2.* Alternating sum $\sum_{k=0}^{r}(-1)^k\binom{n}{k-l}$ — sign-cancellation pattern.
- *5.3(i).* $\sum_{k=0}^{m}(-1)^k\binom{n}{k}\binom{n}{m-k}$ — periodicity in $m$.
- *5.3(ii).* (Tomescu) $S_n = \sum_{k}(-1)^k\binom{2n-k}{k}$ periodic mod 3.
- *5.4(i).* $\sum_{k=0}^{m}\binom{m}{k}/\binom{n}{k} = (n+1)/(n+1-m)$.
- *5.4(iii).* JEE 1986 — $\sum (-1)^k(k+1)C_k^2$. Answer: $(-1)^{n/2}(n+1)$ if $n$ even.
- *5.4(iv).* JEE 1989 — $\sum (-1)^k(k+1)^2 C_k = 0$.
- *5.6.* JEE 1979 — $\sum (-1)^{k-1} k C_k^2 = (-1)^n n C_n$.
- *5.7.* JEE 1983 — Coefficient of $x^4$ in $(x/2 - 3/x^2)^{10}$.
- *5.8.* JEE 1998 — $a_n = \sum 1/\binom{n}{r}$ and $\sum r/\binom{n}{r} = (n/2)a_n$.
- *5.9.* JEE 1983 — $\sum_{0 \le i < j \le n} c_i c_j = 2^{2n-1} - (2n)!/[2(n!)^2]$ where $c_r = \binom{n}{r}$.
- *5.10.* JEE 1983, 1979, 1980, 1994, 1999, 1987 — Coefficient-of-term problems.
- *5.11.* JEE 1993 — $\sum (-3)^{r-1}\binom{3n}{2r-1} = 0$ where $k = 3n/2$ and $n$ even. **Uses $\omega$ (cube root of unity).**
- *5.13.* Combinatorial proof of $\sum k\binom{n}{k} = n2^{n-1}$ via "captain selection."
- *5.15.* Six identities (a-g) including (g) JEE 1984.
- *5.16.* $\sum \binom{n-k}{k}$ is a Fibonacci number.
- *5.17.* Coin-stack value $n$ counted by Fibonacci. **Ch. 15 Bijection candidate.**
- *5.18.* Stirling-number recurrences.
- *5.19.* $\sum a_k = ?$ for $(1+x)^{2n}$ first $n+2$ terms.
- *5.20.* Trinomial expansion $(1+x+x^2)^n$ — multiple identities.
- *5.21.* Equation $x_1\cdots x_n = y_1\cdots y_n$ with $\pm 1, 0$ values, count = $3(3^{2n-1} - 3^{n-1}2^{n+1} + 2^{2n-1})$.
- *5.22.* AP-weighted $\sum C_r a_r^2$ identity.
- *5.23.* JEE 1985 — $\sum (-1)^r \binom{n}{r}(1/2^r + 3^r/2^{2r} + 7^r/2^{3r} + \cdots)$.
- *5.25.* Sum of cubes of $\binom{n}{k}$ as coefficient extraction.

**Joshi's pedagogical observations.**
- "The fourth method [combinatorial bijection] is not always available. But when it is, it is, by far, the most elegant way to prove the identity." — central thesis of the chapter.
- "Such an argument is not always available. But when it is, it is, by far, the most elegant way to prove the identity." (Repeated — Joshi *insists* on elegance.)
- Pascal-triangle pictorial emphasised — visual intuition supplementing algebra.

**Pillar 2 routing.** *Primary:* **Ch. 15 Bijection / Correspondence** (Ex. 5.1(i)-(iv), 5.13, 5.16, 5.17 Fibonacci-via-coins, 5.18 Stirling — entire chapter is Ch. 15's seed). *Secondary:* Ch. 5 Substitution (generating-function specialisations $x=1, x=-1, x=\omega$); Ch. 4 Hidden Structure (Ex. 5.16 Fibonacci-from-binomial); Ch. 18 Recursion (Ex. 5.16, 5.18). *Cross-archetype:* Ex. 5.10(d) (JEE 1994, three consecutive binomials in AP) is a **strong Ch. 2 Symmetry candidate** (symmetric-coefficient property).
<!-- CH5_END -->

<!-- CH6_BEGIN -->
### Chapter 6: Inequalities (pp. 190–234; lines 10329–12622)

**Topic summary.** Elementary inequalities (without calculus): triangle inequality, AM-GM, Cauchy-Schwarz; range and extrema of functions; the rigorous definition of limit; sequence convergence; indeterminate forms; asymptotic estimation (Stirling). **Primary source for Pillar 2 Ch. 10 (Inequality Constraints) and Ch. 7 (Normalization).** The chapter is dense with pigeonhole-principle problems (Comments 18–20) that are excellent for Ch. 1 Invariance via the "double-count" lens.

**Main Problem.** *Minimum value of $(33 + x)(57 + x)/(8 + x)$ for $x > -8$.* **Answer:** $144$ at $x = 27$. **Three methods presented (Comments 1–4):** (i) substitution $u = 8 + x$ then AM-GM on $1225/u + u$; (ii) calculus (derivative); (iii) reformulate as quadratic in $x$ and use discriminant + Vieta. Joshi explicitly compares — voice sample for **Pillar 2 six-point Brute/Pivot/Connections discipline.**

**Key formulas/theorems established.**
- AM-GM (general $n$): $(a_1 + \cdots + a_n)/n \ge (a_1 \cdots a_n)^{1/n}$ for $a_i > 0$, equality iff all equal.
- Generalised AM-GM via Comment 6: $a^m b^n \le ((ma + nb)/(m+n))^{m+n}$ for any positive integers $m, n$.
- Cauchy-Schwarz (real): $(\sum a_i b_i)^2 \le (\sum a_i^2)(\sum b_i^2)$.
- Cauchy-Schwarz (complex): $|\sum z_k \bar w_k|^2 \le (\sum|z_k|^2)(\sum|w_k|^2)$.
- Triangle inequality: $|a + b| \le |a| + |b|$ (algebraic) and $a + b > c$ (geometric for triangle sides).
- AM ≥ GM ≥ HM: $\frac{a_1 + \cdots}{n} \ge (a_1 \cdots a_n)^{1/n} \ge \frac{n}{1/a_1 + \cdots + 1/a_n}$.
- Limit definition via $\varepsilon - N$.
- Archimedean property: rationals dense in $\mathbb{R}$.
- Stirling's approximation: $n! \sim (n/e)^n \sqrt{2\pi n}$.
- Growth-rate hierarchy: algebraic $<$ exponential $<$ factorial $<$ $n^n$.

**Comments highlights (20 total).**
- *Comment 1.* JEE 1979 — Generalisation: min of $(a+x)(b+x)/(c+x)$ is $(\sqrt{a-c} + \sqrt{b-c})^2$. **Ch. 7 Normalization candidate.**
- *Comments 5–7.* AM-GM proofs (algebraic, by induction, by reverse-induction). The famous Cauchy proof on $n = 2^m$ first then "filling in" with $A$.
- *Comment 8.* JEE 1981 — Reciprocal-sum inequality $(a + b + c)(1/a + 1/b + 1/c) \ge 9$. **Ch. 10 PP candidate.**
- *Comment 11.* Cauchy-Schwarz, with the "no complex order" remark.
- *Comments 12–14.* Floor/ceiling, fractional-part identities, Beatty's theorem.
- *Comments 18–20.* **Pigeonhole principle (Dirichlet drawer principle):** 5 points in unit square / 7 in triangle. *Joshi calls pigeonhole "the simplest yet most elegant counting principle."*

**Exercises (notable — competition-sourced).**
- *6.1(ii).* JEE 1979 — $u = x^2 + 4y^2 + 9z^2 - 6yz - 3xz - 2xy$ sign analysis. **Always $\ge 0$ via $u = \tfrac{1}{2}((x-3z)^2 + (x-2y)^2 + (2y-3z)^2)$. Ch. 2 Symmetry candidate.**
- *6.1(iii).* JEE 1980 — Roots of $(x-a)(x-b) + (x-b)(x-c) + (x-c)(x-a) = 0$ are always real (discriminant analysis). **Ch. 11 Existence candidate.**
- *6.1(iv).* JEE 1989 — Sign of roots from quartic.
- *6.2.* JEE 1981 — Complex partial order $z_1 \unlhd z_2$ counterexample.
- *6.3.* JEE 1983, 1996 — One-to-one for rational functions.
- *6.4.* JEE 1984 — $(x-a)(x-b)/(x-c)$ assumes all real values condition. **Ch. 9 Domain candidate.**
- *6.6.* Multiple proofs of AM-GM (induction on $n$, Cauchy doubling, "A is also AM of subset" cleverness).
- *6.8.* Cauchy-Schwarz proof for complex.
- *6.9.* JEE 1984 — $a^2 + b^2 + c^2 = 1$ → $ab + bc + ca \in [-1/2, 1]$. **Ch. 10 candidate (Cauchy-Schwarz application).**
- *6.10.* JEE 1981 — $x > 0$, $xy = 1$ → min of $x + y$. Plus geometric significance (AM-GM with equality at $x = y$). **Ch. 12 Extremal candidate.**
- *6.10(c).* JEE 1980 — Cube minimises surface among fixed-volume boxes. **Ch. 2 Symmetry / Ch. 12 Extremal.**
- *6.11.* JEE 1996 — AP roots of $x^3 - x^2 + \beta x + \gamma = 0$ → intervals for $\beta, \gamma$. **Ch. 17 DOF Analysis candidate.**
- *6.12.* JEE 1983 — System $x^2 - 3x + 2 > 0$ and $x^2 - 3x - 4 \le 0$.
- *6.13(a).* JEE 1984 — $(a+b+c)(1/a+1/b+1/c) \ge 9$. Generalise to $n$.
- *6.14.* JEE 1984 — $\log_a x + \log_x a$ minimum for $0 < x < a$. Answer: 2 (when $x = a$, AM-GM).
- *6.16.* JEE 1986 — GP sum-of-squares $\alpha S$ → $\alpha^2 \in (1/3, 1) \cup (1, 3)$.
- *6.17.* JEE 1999 — Quadratic roots $< 3$ → interval for $a$.
- *6.19.* $x + y = 1$, $x, y \ge 0$ → $1/2 \le x^2 + y^2 \le 1$. **Ch. 7 Normalization candidate.**
- *6.20.* JEE 1997 — Unit square inscribed quadrilateral: $2 \le a^2 + b^2 + c^2 + d^2 \le 4$. **Ch. 10 WE candidate.**
- *6.21.* JEE 1995 — Quadratic roots straddle $\pm 1$ → $1 + |c/a| + |b/a| < 0$. **Ch. 11 Existence / Ch. 17 DOF candidate.**
- *6.22.* JEE 1999 — Harmonic series $\alpha(n) = \sum_{k=1}^{2^n - 1} 1/k$ → which of $\alpha(100), \alpha(200)$ exceed 100? **Ch. 6 Linearization / Ch. 18 candidate.**
- *6.26.* JEE 1985 — Triangle inequality for $a^2 + 2a, 2a + 3, a^2 + 3a + 8$. **Ch. 9 Domain candidate.**
- *6.27.* JEE 1988 — $R = (5\sqrt 5 + 11)^{2n+1}$, $f = R - [R]$ → $Rf = 4^{2n+1}$. **Ch. 4 Hidden Structure / Ch. 14 Modularity candidate.**
- *6.28.* JAT 1979 — Floor function graphs + sum-of-floors $[x] + [2x] + [4x] + \ldots = $ specific value problems.
- *6.30.* JEE 1978 — System of inequalities solution-set sketch.
- *6.31.* JEE 1978 — All integers $x$ with $(5x-1) < (x+1)^2 < (7x-3)$.
- *6.33.* JEE 1980 — Induction: $n^4 < 10^n \Rightarrow (n+1)^4 < 10^{n+1}$ for $n \ge 2$.
- *6.35.* Pigeonhole — Clock-face reshuffling: adjacent pair sum $\ge 14$ always exists. **Ch. 1 Invariance / Ch. 13 candidate.**
- *6.36.* Pigeonhole — 5 points in triangle of longest side $a$ → two within $a/2$. **Ch. 1 candidate (used in archetype map).**
- *6.37.* Pigeonhole — 101 integers from $\{1, \ldots, 200\}$ → some divides another. **Routed to Pillar 2 Ch. 1 archetype reference.**
- *6.38.* IMO 1978 modified — Integers 1-16 in 3 classes → some $x, y, x+y$ in same class. **Ch. 1 / Ch. 13 candidate.**
- *6.39.* 20 students × 10 T/F questions → two agree on ≥ 6 questions. **Ch. 1 PP candidate.**
- *6.40(e).* JEE 1984 — $\lim_{n\to\infty} \sum_{k=1}^{n} k/(1 - n^2)$. **Ch. 6 Linearization candidate.**
- *6.42–6.45.* Mixing-glasses recurrence: $a_n = 100/21 + (19/21)a_{n-1}$ → closed form via Fibonacci-style methods. **Golden ratio appears in 6.45.**
- *6.51–6.53.* Growth-rate exercises (algebraic vs exponential vs factorial vs $n^n$).

**Joshi's pedagogical observations.**
- "It is precisely for this reason [lack of strength of limiting process] that they offer a greater challenge to one's ingenuity." — direct voice sample for **Pillar 2 Ch. 10 register**.
- "Note … the effective use of the simple substitution $u = x + 8$ in both of them. The calculus-based method is mechanical." — Joshi's *explicit* meta-pedagogy on the choice between elementary and calculus-based methods.
- "[Pigeonhole] is the simplest yet most elegant counting principle." — sets up Ch. 1 / Ch. 13 framing.
- The chess-board-rice story (Ex. 6.51) — voice sample for the *vignette register* Pillar 2 chapters open with.

**Pillar 2 routing.** *Primary:* **Ch. 10 Inequality Constraints** (Ex. 6.9, 6.13, 6.14, 6.20 — full WE+PP set sourcing); **Ch. 7 Normalization** (Comment 1 JEE 1979 generalisation, Ex. 6.19); **Ch. 12 Extremal** (Ex. 6.10, 6.10(c)). *Secondary:* Ch. 1 Invariance (pigeonhole Ex. 6.35-6.39); Ch. 6 Linearization (Ex. 6.40, 6.22); Ch. 17 DOF Analysis (Ex. 6.11, 6.21); Ch. 14 Modularity (Ex. 6.27 surd-fractional-part).
<!-- CH6_END -->

<!-- CH7_BEGIN -->
### Chapter 7: Trigonometric Identities (pp. 234–260; lines 12623–14056)

**Topic summary.** Identities derived from $\sin^2\theta + \cos^2\theta = 1$, addition formulas, and **roots-of-unity / cyclotomic polynomials**. Joshi's central pedagogical idea: trigonometric *products* of evenly-spaced angles are best evaluated via roots of unity (vs. direct manipulation). Cyclotomic polynomials, Chebyshev polynomials introduced. **Strong source for Pillar 2 Ch. 2 Symmetry and Ch. 5 Substitution.**

**Main Problem.** *Compute $\sin 10° \sin 20° \sin 30° \sin 40° \sin 50° \sin 60° \sin 70° \sin 80°$.* **Answer:** $\sqrt 3 / 256$. **Technique (Comments 1–2):** Two methods presented. Method 1: roots of unity — $\prod_{k=1}^{n-1} 2\sin(\pi k/n) = n$. Method 2: direct trigonometric collapse using $2\sin\alpha\sin\beta = \cos(\alpha-\beta) - \cos(\alpha+\beta)$.

**Key formulas/theorems established.**
- Euler: $e^{i\theta} = \cos\theta + i\sin\theta$.
- De Moivre: $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$.
- $\prod_{k=1}^{n-1} 2\sin(\pi k/n) = n$ — product of distances from 1 to other $n$-th roots of unity.
- $z^n - 1 = \prod_{d \mid n} \Phi_d(z)$ — cyclotomic factorisation.
- Number of primitive $n$-th roots of unity = $\phi(n)$.
- Chebyshev polynomials $T_n(x), U_n(x)$ — recurrence $T_{n+1} = 2xT_n - T_{n-1}$.
- Cube roots of unity $1, \omega, \omega^2$ with $1 + \omega + \omega^2 = 0$.

**Comments highlights (14 total).**
- *Comments 1–4.* Product evaluation methods + parity case-split for $n$ even/odd.
- *Comments 5–8.* Roots of unity, primitive roots, cyclotomic polynomials.
- *Comments 9–11.* $\omega$ identities; $A^3 + B^3 + C^3 - 3ABC$ factorisation.
- *Comment 12.* Trinomial $(1 + x + x^2)^n$ sub-sums identity.
- *Comments 13–14.* Chebyshev polynomials, recurrences.

**Exercises (notable — competition-sourced).**
- *7.1.* JEE 1988 — $\sqrt 3\csc 20° - \sec 20°$. **Answer: 4.** **Ch. 5 Substitution candidate.**
- *7.2(a-g).* Sine/cosine product identities including standard $\sin 20°\sin 40°\sin 60°\sin 80° = 3/16$.
- *7.3.* Identities using $\sin 18° = (\sqrt 5 - 1)/4$ — golden ratio.
- *7.5.* JEE 1980 — Least $n$ with $((1+i)/(1-i))^n = 1$. **Answer: 4.**
- *7.6.* Primitive $n$-th roots of unity count = $\phi(n)$.
- *7.7.* Order of an $n$-th root divides $n$.
- *7.8.* JEE 2002 — Roots of $z^{p+q} - z^p - z^q + 1 = 0$ for distinct primes $p, q$. **Ch. 2 Symmetry candidate.**
- *7.9.* Cyclotomic polynomials — properties + computation.
- *7.10.* Identities from cyclotomic polynomials — $4\cos^2(\pi/7)$ root of cubic etc.
- *7.11(i).* JEE 1999 — $(-1/2 + i\sqrt 3/2)^{334} + (-1/2 + i\sqrt 3/2)^{365}$ in $a + b$ form (uses cube roots of unity).
- *7.11(ii).* JEE 1996 — $\sum_{n=2}^{N}(n-1)(n-\omega)(n-\omega^2)$. **Telescoping via $\omega$. Ch. 18 Recursion candidate.**
- *7.12(a).* JEE 1978 — $x = a + b, y = a\gamma + b\beta, z = a\beta + b\gamma$ → $xyz = a^3 + b^3$. **Ch. 2 Symmetry candidate (cube-roots identity).**
- *7.12(b).* Factor $A^3 + B^3 + C^3 - 3ABC$ into linear factors.
- *7.13.* $(1 + x + x^2)^n$: $a_0 + a_3 + a_6 + \cdots = a_1 + a_4 + a_7 + \cdots = a_2 + a_5 + a_8 + \cdots = 3^{n-1}$. **Ch. 2 Symmetry candidate (cyclic-sum partition).**
- *7.14(a).* JEE 1989 — Cube roots of negative real ratio simplification.
- *7.14(b).* JEE 1979 — Roots of $(x-1)^3 + 8 = 0$ in $\omega$.
- *7.15.* $x^2 + x + 1 \mid x^{n+1} + (x+1)^{2n-1}$. **Alternate proof of Ex. 4.16. Ch. 4 Hidden Structure candidate.**
- *7.16.* JEE 1999 — $f_n(\theta) = \tan(\theta/2)\prod_{k=0}^{n}(1 + \sec 2^k\theta)$ — telescoping. **Ch. 18 Recursion candidate.**
- *7.17.* JEE 1979 — $\alpha + \beta + \gamma = 2\pi$: $\tan(\alpha/2) + \tan(\beta/2) + \tan(\gamma/2) = \tan(\alpha/2)\tan(\beta/2)\tan(\gamma/2)$.
- *7.18(a).* JEE 1983 — $f(x) = \cos(\ln x)$: $f(x)f(y) - \tfrac{1}{2}[f(x/y) + f(xy)] = 0$. **Ch. 20 Functional Eq candidate.**
- *7.18(b).* JEE 1997 — $\cos x\cos(x+2) - \cos^2(x+1)$ is constant. Find slope. **Ch. 1 Invariance candidate (it's a constant!).**
- *7.19.* JEE 1983 — $\tan A = (1 - \cos B)/\sin B$ → $\tan 2A = \tan B$.
- *7.20.* JEE 1980 — $\alpha + \beta - \gamma = \pi$ → $\sin^2\alpha + \sin^2\beta - \sin^2\gamma = 2\sin\alpha\sin\beta\cos\gamma$.
- *7.21(a-e).* JEE 1981, 1987, 1998 — Trigonometric Fourier expansions, Chebyshev polynomials, recurrences.
- *7.22.* JEE 1997 — Determinant where the answer is invariant w.r.t. one of $a, p, d, x$.
- *7.23.* JEE 1986 — Power-of-sine identity simplification.
- *7.24.* JEE 1997* — $\cos(x-y), \cos x, \cos(x+y)$ in HP → $\cos x \sec(y/2) = ?$.
- *7.25.* JEE 1994 — Cos-sum-formula by induction: $\sum_{k=1}^{n}\cos kx = \cos((n+1)x/2)\sin(nx/2)\csc(x/2)$.
- *7.26.* $\sum_{2^n \text{ sign-choices}} \cos(\pm\alpha_1 \pm\cdots\pm\alpha_n) = 2^n \cos\alpha_1\cos\alpha_2\cdots\cos\alpha_n$. **Ch. 2 Symmetry candidate (sign-symmetry sum collapse).**
- *7.27.* $\cos 3\alpha\sin(\beta-\gamma) + \cos 3\beta\sin(\gamma-\alpha) + \cos 3\gamma\sin(\alpha-\beta) = 4\sin(\beta-\gamma)\sin(\gamma-\alpha)\sin(\alpha-\beta)\cos(\alpha+\beta+\gamma)$. **Ch. 2 Symmetry candidate (cyclic identity).**
- *7.28.* $\tan^2\theta + \tan^2(\theta + \pi/3) + \tan^2(\theta + 2\pi/3) = 9\tan^2 3\theta + 6$. **Hint: construct cubic with these as roots.** **Ch. 1 Invariance / Ch. 16 Reverse Eng candidate.**
- *7.29.* $A + B + C = \pi$ and three cyclic cosine identities → $\tan\alpha\tan\beta\tan\gamma = 1$.

**Joshi's pedagogical observations.**
- "In evaluating a product of the type given in the Main Problem, it is usually futile to try to do it by evaluating each factor separately. Nor is it needed!" — **canonical Pillar 2 Ch. 2 Symmetry framing.**
- "[Sometimes] it is possible to find the product without finding the individual factors." — voice sample.
- "These polynomials are very useful in algebra" (on cyclotomic) — connects trig to Ch. 3, Ch. 4.
- The case-split on parity of $n$ (Comments 1, 4) — model for *brute path vs elegant pivot* in Pillar 2 six-point grammar.

**Pillar 2 routing.** *Primary:* **Ch. 2 Symmetry** (Ex. 7.2, 7.12, 7.13, 7.21, 7.26, 7.27, 7.28 — direct sourcing); Ch. 5 Substitution (Ex. 7.1, 7.16, 7.21 Chebyshev); Ch. 18 Recursion (Ex. 7.11(ii), 7.21(e) Chebyshev recurrence). *Secondary:* Ch. 20 Functional Equations (Ex. 7.18(a)); Ch. 16 Reverse Engineering (Ex. 7.28 — construct cubic from roots); Ch. 1 Invariance (Ex. 7.18(b) constant identity, 7.22 determinant invariance).
<!-- CH7_END -->

<!-- CH8_BEGIN -->
### Chapter 8: Geometry (pp. 260–287; lines 14057–15484)

**Topic summary.** "Pure" Euclidean geometry — synthetic methods, coordinate methods, complex numbers as a tool for plane geometry, Argand diagrams, reflections (including inversion in a circle), solid geometry. Joshi opens with Gandhi's autobiographical praise of Euclid Prop. 13. Stresses **choosing coordinates wisely** as a recurring meta-pedagogical theme. **Primary source for Pillar 2 Ch. 8 Domain Translation and Ch. 3 Duality (pole-polar).**

**Main Problem.** *In $\triangle ABC$, $H$ is the orthocentre. Perpendiculars $HP, HQ$ are drawn to the internal and external angle bisectors at vertex $A$. Line $PQ$ meets $BC$ at $M$. Find $BM:MC$.* **Answer:** $1$ — $M$ is the midpoint of $BC$. **Three approaches presented:** (i) **Coordinate** — take the two angle bisectors at $A$ as axes; (ii) **Pure geometry** — nine-point circle of $\triangle ABC$; (iii) Hybrid using cyclic-quadrilateral angle chasing. Joshi explicitly notes: "the solution using only pure geometry is artistic but rather tricky and hence not very reliable, especially in a time-constrained examination."

**Key formulas/theorems established.**
- Orthocentre / circumcentre / centroid / incentre / nine-point centre — Euler line collinearity ($G$ divides $OH$ in $1:2$).
- Nine-point circle theorem.
- Power of a point w.r.t. a circle.
- Reflection/inversion in a circle: $P^*$ defined by $\bar{z} z^* = r^2$.
- Complex-number formulation: equilateral triangle iff $z_0^2 + z_1^2 + z_2^2 = z_0 z_1 + z_1 z_2 + z_2 z_0$.
- Triangle inequality (geometric) — sum of two sides exceeds third.
- Napoleon's theorem (Ex. 8.10): centres of equilateral triangles on sides of any triangle form an equilateral triangle.
- Vector-area: $z_1 \cdot z_2 = \mathrm{Re}(z_1 \bar z_2)$, $z_1 \times z_2 = \mathrm{Im}(z_1 \bar z_2)\hat k$.

**Comments highlights (18 total).**
- *Comment 1.* Pure-geometric solution using nine-point circle.
- *Comments 2–3.* Choice of coordinate system — when to use vertex as origin, when not.
- *Comment 5.* Cyclic-symmetry of equations of altitudes.
- *Comment 6.* JEE 1998 — three altitudes concurrent (proof by coordinates).
- *Comments 7–11.* Coordinate proofs of classical theorems.
- *Comment 12.* Complex numbers in geometry — Argand diagram methods, rotation as multiplication by $e^{i\theta}$.
- *Comment 17.* Inverse direction — complex-number problem solved via geometry.
- *Comment 18.* Solid geometry — tetrahedron with right angles at apex (Ex. 8.26).

**Exercises (notable — competition-sourced).**
- *8.1.* JEE 1980 — Isosceles triangle parallel-line construction: $DF + FA + AE + ED = AB + AC$. **Ch. 2 Symmetry candidate.**
- *8.2.* JEE 1984 — $(a - d) \cdot (b - c) = (b - d) \cdot (c - a) = 0$ → $D$ is orthocentre of $\triangle ABC$. **Ch. 2 Symmetry / Ch. 8 Domain Translation candidate.**
- *8.3.* JEE 1985 — Concurrency conditions for $px+qy+r=0$, $qx+ry+p=0$, $rx+py+q=0$. Conditions: (A) $p+q+r=0$; or (C) $p^3+q^3+r^3 = 3pqr$.
- *8.4.* JEE 1983 — Does $5x+4y=0$ pass through intersection of $x+2y-10=0$ and $2x+y+5=0$? **Ch. 19 Pivoting candidate.**
- *8.5.* JEE 1978 — Pedal triangle perpendiculars concurrent. **Ch. 2 Symmetry (cyclic concurrency) candidate.**
- *8.6.* JEE 1979 — Triangle two vertices $(5,-1), (-2,3)$, orthocentre at origin, find third. **Ch. 16 Reverse Engineering candidate.**
- *8.7.* JEE 1983 — Orthocentre of triangle with parametric vertices on parabola.
- *8.8(a).* JEE 1985 — Three complex numbers in AP on a circle? No (they're collinear).
- *8.8(b).* JEE 1983 — Parallelogram condition $z_1 + z_3 = z_2 + z_4$.
- *8.9.* JEE 1993 — Rhombus ABCD, $BD = 2AC$, $D, M$ given, find $A$.
- *8.10.* **Napoleon's theorem.** **Ch. 2 Symmetry primary candidate.**
- *8.11.* JEE 1997 — $z_1, z_2$ roots of $z^2 + pz + q = 0$, $\angle AOB = \alpha$, $OA = OB$ → $p^2 = 4q\cos^2(\alpha/2)$.
- *8.12.* JEE 1981, 1983 — Loci of complex equations (Apollonius circles).
- *8.15.* JEE 1989 — $a + i, 1 + ib, 0$ form equilateral.
- *8.17.* JEE 1985 — Constraint on $|z_1|, |z_2|, \mathrm{Re}(z_1\bar z_2)$ → properties of $w_1, w_2$. **Ch. 2 Symmetry candidate (orthogonality preserved).**
- *8.19.* $\sin\alpha + \sin\beta + \sin\gamma = \cos\alpha + \cos\beta + \cos\gamma = 0$ → $\sum\sin^2 = \sum\cos^2 = 3/2$. **Ch. 7 Normalization / Ch. 2 Symmetry candidate.**
- *8.20.* Sum of squared distances between vertices of regular $m$-gon and $n$-gon on concentric circles of radii $a, b$ is $mn(a^2+b^2)$. **Ch. 1 Invariance / Ch. 2 Symmetry candidate.**
- *8.21.* Inversion in a circle — full theory. **Ch. 8 Domain Translation primary candidate.**
- *8.23.* Area formula via complex numbers.
- *8.24.* Collinearity via $3\times 3$ determinant with $z, \bar z$.
- *8.25.* Concyclicity via $4\times 4$ determinant.
- *8.26.* Tetrahedron with three perpendicular edges at apex: $\Delta^2 = \Delta_1^2 + \Delta_2^2 + \Delta_3^2$ (3D Pythagoras). **Ch. 20 Analogy candidate (transfer from plane).**

**Joshi's pedagogical observations.**
- Gandhi quote on Euclid Prop. 13 — voice sample for vignette register.
- "The general rule of thumb is to take the origin at a point which plays a pivotal role in the problem." — direct Pillar 2 framing.
- "It is sometimes advantageous not to take any particular point as the origin and instead let A, B, C be any three points… [for] cyclical symmetry." — direct quote on Ch. 2 Symmetry method.
- "Even to justify these [algebraic] techniques, some pure geometry is needed."

**Pillar 2 routing.** *Primary:* **Ch. 8 Domain Translation** (Ex. 8.21 inversion — entire chapter); **Ch. 3 Duality** (pole-polar emerges in Ch. 9); **Ch. 2 Symmetry** (Ex. 8.10 Napoleon, 8.19, 8.20, Ex. 8.17). *Secondary:* Ch. 16 Reverse Engineering (Ex. 8.6, 8.7); Ch. 20 Analogy (Ex. 8.26 3D Pythagoras).
<!-- CH8_END -->

<!-- CH9_BEGIN -->
### Chapter 9: Coordinate Geometry (pp. 287–329; lines 15485–17597)

**Topic summary.** Conics (parabola, ellipse, hyperbola), pairs of straight lines, tangents/normals, chords, loci, pole-polar duality. Joshi notes: "[Coord-geom problems] are among the 'sure shot' questions for most candidates because they are relatively straightforward and often demand only a few standard formulas." **Largest exercise set in the book (61 problems).** Strong source for Ch. 5 Substitution (parametrise conic), Ch. 19 Pivoting/Elimination (locus problems), Ch. 3 Duality.

**Main Problem.** *JEE 1980. Show $2x^2 + 5xy + 3y^2 + 6x + 7y + 4 = 0$ represents a pair of straight lines. Through $(0, 1)$ draw lines parallel to these. Find the area of the parallelogram.* **Answer:** $14$ sq. units. **Technique:** Factorise into $(x + y + 1)(2x + 3y + 4)$, find vertex of parallelogram via intersections, compute area as $2\cdot(\text{triangle area})$.

**Key formulas/theorems established.**
- Distance, slope, section formula.
- Equation of line: slope-intercept, two-point, intercept, normal forms.
- Pair of straight lines: $ax^2 + 2hxy + by^2 + 2gx + 2fy + c = 0$ — discriminant criterion.
- Circle: $x^2 + y^2 + 2gx + 2fy + c = 0$ — centre $(-g, -f)$, radius $\sqrt{g^2 + f^2 - c}$.
- Conic sections: parabola $y^2 = 4ax$, ellipse $x^2/a^2 + y^2/b^2 = 1$, hyperbola $x^2/a^2 - y^2/b^2 = 1$.
- Parametric forms: $(at^2, 2at)$, $(a\cos\theta, b\sin\theta)$, $(a\sec\theta, b\tan\theta)$.
- Focal chord, directrix, eccentricity.
- Tangent at parameter $t$ to parabola: $ty = x + at^2$.
- Chord-of-contact, pole-polar.
- Power of a point, radical axis.

**Comments highlights (19 total).**
- *Comment 1.* JEE 1996 — finding a directrix from common-tangent construction.
- *Comment 2.* JEE 1998 — "how many tangents to ellipse have given direction?" — 2 by symmetry alone, no calculation.
- *Comments 4–6.* Determinant criteria for collinearity, concurrency, parallel lines.
- *Comments 7–10.* Conic sections — parametric methods.
- *Comments 11–14.* Tangent/normal/chord/locus problems.
- *Comment 15.* Pair-of-lines factorisation method.
- *Comments 16–17.* Pole-polar duality.
- *Comment 18.* Distance functions other than Euclidean — taxicab metric.
- *Comment 19.* Proof of a geometric property using coordinates.

**Exercises (notable — competition-sourced).**
- *9.1(a).* JEE 1985 — Equal-area determinants → congruent triangles? No (congruence requires more).
- *9.2.* JEE 1998 — $P$ on ellipse $16x^2 + 25y^2 = 400$, foci $F_1, F_2$ → $PF_1 + PF_2 = 2a = 10$. **Ch. 1 Invariance candidate (focal-sum constant).**
- *9.3.* JEE 1998 — Common tangents to two circles count.
- *9.4.* JEE 1984 — $a, b, c$ in AP → $ax + by + c = 0$ through fixed point $(1, -2)$. **Ch. 1 Invariance candidate (used as Pillar 2 Ch. 1 motivation).**
- *9.5.* JEE 1999 — $(x_i, y_i)$ all in GP with common ratio → collinear/parabolic/curve.
- *9.7.* JEE 1989 — Area of triangle formed by axis, normal, tangent at point on circle.
- *9.11.* JEE 1994 — Max area $\triangle PF_1 F_2$ for $P$ on ellipse.
- *9.13(b).* JEE 1998 — Circle-hyperbola intersection: $x_1 + x_2 + x_3 + x_4 = 0$, $y_1 y_2 y_3 y_4 = c^4$. **Ch. 1 Invariance / Vieta candidate.**
- *9.15.* JEE 1981, 1988, 2001 — Identifying curves from descriptions.
- *9.20.* JEE 1985 — Quadrant of orthocentre.
- *9.21.* JEE 1981 — Rectangle: given two opposite vertices + line through other two.
- *9.24(i–xii).* JEE 1985–2001 — **Twelve locus problems** — *the* gold mine for Ch. 19 Pivoting/Elimination (parameter elimination is the canonical technique).
- *9.25.* JEE 1995 — Locus of dividing-chord point of parabola.
- *9.26.* JEE 1987 — Locus of intersection of perpendicular lines through axis-intercepts.
- *9.27.* JEE 1998 — Locus of $P$ with $45°$ tangent-pair angle to parabola is hyperbola.
- *9.28.* JEE 1999 — Locus of midpoint of tangent-chord intersect.
- *9.32.* JEE 1985 — Rectangle inscribed with diagonal-line.
- *9.34.* JEE 1986 — Perpendicular bisectors of triangle sides.
- *9.36.* JEE 1989 — Two circles intersect in 2 points → values of $r$.
- *9.42.* Angle bisector method (equidistance characterisation).
- *9.46.* JEE 1986 — Concentric circles with specified chord intercepts.
- *9.47.* JEE 2001 — Tangent-pair from origin to circle in first quadrant.
- *9.52–9.53.* Non-Euclidean metric (taxicab, max-metric) — equidistant loci look very different!
- *9.54.* JEE 1981 — Which regions fail midpoint-convexity?
- *9.55.* JEE 1992 — Sum of distances from two perpendicular lines = constant → square locus (taxicab circle).
- *9.56.* JEE 1981, 2002 — Area enclosed by $|x| + |y| = 1$.
- *9.58.* JEE 1994 — Perpendicular chords from vertex of parabola → fixed point.
- *9.60.* JEE 1996 — Tangent-triangle area ratio on parabola.
- *9.61.* Parabolic orthocentre at focus → parametric identity.

**Joshi's pedagogical observations.**
- "It only asks us how many values of $c$ satisfy a certain condition and not which ones they are. And this can be done with no computations if we interpret the problem a little differently." — voice sample for Pillar 2 Ch. 2 / Ch. 17 chapter framing.
- "A change of the metric can thwart our intuition." (Ex. 9.52(b)) — *invitation to Ch. 20 Analogy / Transfer* chapter.
- "The need for a diagram can often be obviated [in coord-geom]. But this is not to detract from the general importance of diagrams." — Joshi's balanced meta-pedagogy.

**Pillar 2 routing.** *Primary:* **Ch. 19 Pivoting/Elimination** (Ex. 9.24 twelve locus problems — entire WE+PP set sourced here); **Ch. 5 Substitution** (Ex. 9.7, 9.11, 9.25 — parametric conic methods); **Ch. 8 Domain Translation** (Ex. 9.52, 9.53, 9.55, 9.56 — non-Euclidean metrics). *Secondary:* Ch. 1 Invariance (Ex. 9.2 focal sum, 9.4 AP-line through fixed point, 9.13(b) Vieta-on-conic). Ch. 17 DOF Analysis (Ex. 9.36 — number-of-solution counting).
<!-- CH9_END -->

<!-- CH10_BEGIN -->
### Chapter 10: Trigonometric Equations (pp. 329–362; lines 17598–19337)

**Topic summary.** Equations involving trig functions of the unknown — *general solutions* using periodicity, then particular solutions via auxiliary constraints (interval, integer parameter). Range and inverse trig functions. **Strong source for Pillar 2 Ch. 5 Substitution and Ch. 11 Existence.**

**Main Problem.** *JEE 1994. Vertices $A_1, \ldots, A_n$ of a regular $n$-gon satisfy $1/A_1 A_2 = 1/A_1 A_3 + 1/A_1 A_4$. Find $n$.* **Answer:** $n = 7$. **Three approaches:** (i) reduce to $\sin 4\theta = \sin 3\theta$ where $\theta = \pi/n$; (ii) pure geometry via **Ptolemy's theorem** on cyclic quadrilateral $A_1A_3A_4A_5$; (iii) complex numbers using $A_k = z^{2(k-1)}$ where $z = e^{i\pi/n}$.

**Key formulas/theorems established.**
- General solutions: $\sin\theta = \sin\alpha \Leftrightarrow \theta = n\pi + (-1)^n\alpha$; $\cos\theta = \cos\alpha \Leftrightarrow \theta = 2n\pi \pm \alpha$; $\tan\theta = \tan\alpha \Leftrightarrow \theta = n\pi + \alpha$.
- $4\cos^3\theta - 3\cos\theta = \cos 3\theta$, $3\sin\theta - 4\sin^3\theta = \sin 3\theta$.
- **Rational root test** (Ex. 10.11): if $p/q$ root of integer polynomial, $p \mid a_0$ and $q \mid a_n$.
- $\sin\theta + \cos\theta$ has range $[-\sqrt 2, \sqrt 2]$; $a\sin\theta + b\cos\theta = \sqrt{a^2+b^2}\sin(\theta+\phi)$.
- Inverse trig: principal values, identities like $\sin^{-1}x + \cos^{-1}x = \pi/2$, $\tan^{-1}x + \tan^{-1}y$ formula.
- Ptolemy's theorem: cyclic quadrilateral $ABCD$ → $AC\cdot BD = AB\cdot CD + AD\cdot BC$.

**Comments highlights (20 total).**
- *Comments 1–4.* Methods: trigonometric reduction, geometric (Ptolemy), complex.
- *Comment 5.* JEE 2001 — $4x^3 - 3x - p = 0$, $-1 \le p \le 1$, unique root in $[1/2, 1]$ found via $x = \cos\theta$. **Ch. 5 Substitution candidate.**
- *Comments 6–10.* Standard trig equations, parameter analysis.
- *Comments 11–12.* Range of trig expressions.
- *Comment 15.* Inverse trig functions — principal-value conventions.
- *Comments 16–18.* Plane coordinate geometry via trig (rotation matrices).
- *Comments 19–20.* Plane isometries via complex numbers.

**Exercises (notable — competition-sourced).**
- *10.1(a).* JEE 1997 — $\cos^7 x + \sin^4 x = 1$ on $(-\pi, \pi)$. **Ch. 9 Domain candidate.**
- *10.1(b).* JEE 1983 — $4\cos^2 x \sin x - 2\sin^2 x = 3\sin x$.
- *10.2.* JEE 1978 — $\tan\alpha = m/(m+1)$, $\tan\beta = 1/(2m+1)$, find $\alpha + \beta$. **Answer: $\pi/4$. Ch. 1 Invariance candidate.**
- *10.3.* JEE 1987 — 9-gon side 2, find circumradius.
- *10.4(a).* JEE 1993 — Solutions of $\tan x + \sec x = 2\cos x$ on $[0, 2\pi]$.
- *10.4(b).* JEE 1990 — $\sin(e^x) = 5^x + 5^{-x}$. **No solutions (RHS ≥ 2, LHS ≤ 1). Ch. 17 DOF candidate.**
- *10.4(c).* JEE 1999 — $\tan^{-1}\sqrt{x(x+1)} + \sin^{-1}\sqrt{x^2+x+1} = \pi/2$.
- *10.5.* JEE 1987, 1999 — Range/monotonicity problems.
- *10.6.* JEE 1990 — Parametric quadratic with real roots.
- *10.7.* JEE 1986 — $x + y = 2\pi/3$ and $\cos x + \cos y = 3/2$.
- *10.8.* JEE 1996 — $\sec^2\theta = 4xy/(x+y)^2$ iff $x = y$.
- *10.9(b).* JEE 1986 — Non-trivial solution of linear system in $\theta$. **Ch. 11 Existence candidate.**
- *10.10.* JEE 1996 — $Z = i\bar Z^2$. **Ch. 5 Substitution candidate ($Z = re^{i\theta}$).**
- *10.11.* **Rational root test.** **Ch. 4 Hidden Structure candidate.**
- *10.12.* $8x^3 - 4x^2 - 4x + 1 = 0$ has no rational solution. (Plus alt proof: this is the cubic for $\cos(\pi/7)$.)
- *10.14.* JEE 1980, 1983, 1984, 1985, 1980 — Range/domain problems.
- *10.15.* $a\tan\theta + b\sec\theta = c$ — closed-form for $\tan(\alpha+\beta), \tan(\alpha-\beta)$ via Vieta.
- *10.16.* JEE 1979, 1983, 1981, 1979, 1984 — Inverse trig evaluations.
- *10.18.* $A + B = \pi/4$ → set of values of $\tan A\tan B$. **Ch. 10 Inequality / Ch. 9 Domain candidate.**
- *10.19.* JEE 1999 — Telescoping inverse tan: $\sum \tan^{-1}(1/(n^2+n+1)) = \tan^{-1}(n/(n+2))$. **Ch. 18 Recursion candidate.**
- *10.20.* $\sum \cot^{-1}(2k^2)$, $\sum \cot^{-1}(k^2/2)$. **Ch. 18 Recursion.** (Used in Ch. 24 Ex. 24.87.)
- *10.21.* Circle problem.
- *10.22.* RMO — Quadrilateral angle equalities → $BC = CD$. **Ch. 2 Symmetry candidate.**
- *10.23.* JEE 2002 — Operation taking $P = (\cos\theta, \sin\theta)$ to $Q = (\cos(\alpha-\theta), \sin(\alpha-\theta))$ is reflection in line with slope $\tan(\alpha/2)$.
- *10.24.* JEE 1990 — Intercepts $a, b$ after rotation become $p, q$: $1/a^2 + 1/b^2 = 1/p^2 + 1/q^2$. **Ch. 1 Invariance candidate (rotation invariant).**
- *10.25.* JEE 1980 — Compose three transformations.
- *10.26.* JEE 2001 — Locus on parametrised ellipse.
- *10.30.* JEE 1997 — Tangents at points of intersection are perpendicular.
- *10.34.* JEE 1988 — Common chord of two circles.
- *10.36.* From any point on circumference, lines at angles $k\pi/(2n)$ — product of intercepts $= a\sqrt[n]{n}$. **Ch. 2 Symmetry candidate (cyclic-product evaluation).**
- *10.40.* Hyperbolas with given asymptotes form a one-parameter family.

**Joshi's pedagogical observations.**
- "It is, in fact, the other way round, which is easier, i.e., a cubic equation can sometimes be solved by converting it to a trigonometric equation." — **Pillar 2 Ch. 5 Substitution central thesis.**
- "In a time-constrained examination it is very important to quickly recognise that a particular approach, which appears promising initially, is not going to work."
- "The basic definitions in trigonometry…are geometric in nature…So basically, it is not surprising that trigonometry is a useful tool in doing problems of pure geometry."

**Pillar 2 routing.** *Primary:* **Ch. 5 Substitution** (Comment 5 JEE 2001, Ex. 10.10, 10.14, 10.26 — entire chapter is Ch. 5's seed); **Ch. 11 Existence** (Ex. 10.4(b) no-solution argument, 10.9(b)). *Secondary:* Ch. 1 Invariance (Ex. 10.2, 10.24 rotation invariant); Ch. 18 Recursion (Ex. 10.19, 10.20 telescoping); Ch. 2 Symmetry (Ex. 10.22, 10.36).
<!-- CH10_END -->

<!-- CH11_BEGIN -->
### Chapter 11: Solution of Triangles (pp. 362–391; lines 19338–20897)

**Topic summary.** Computational geometry of triangles: relationships among sides $a, b, c$, angles $A, B, C$, circumradius $R$, inradius $r$, ex-radii $r_A, r_B, r_C$, area $\Delta$, semi-perimeter $s$. Sine rule, cosine rule, projection rule, half-angle rule. Geometric constructions (ruler-and-compass) and what's possible. **Strong source for Pillar 2 Ch. 1 Invariance (these identities ARE Type-III invariants) and Ch. 2 Symmetry (cyclic identities).**

**Main Problem.** *JEE 1992. Three circles touch externally; tangents at points of contact meet at a point distant 4 from a contact point. Find ratio $r_1 r_2 r_3 / (r_1 + r_2 + r_3)$.* **Answer:** $16$ (= $4^2$, the square of the inradius of the triangle formed by the centres). **Technique:** Recognize the inradius $r = 4$; use multiple triangle formulas in chain.

**Key formulas/theorems established.**
- Sine rule: $a/\sin A = b/\sin B = c/\sin C = 2R$.
- Cosine rule: $a^2 = b^2 + c^2 - 2bc\cos A$.
- Projection rule: $a = b\cos C + c\cos B$.
- $\Delta = \tfrac{1}{2}ab\sin C = abc/(4R) = rs$.
- $r = 4R\sin(A/2)\sin(B/2)\sin(C/2)$.
- $r_1 = r/(\cot(A/2))$, $r = (s-a)\tan(A/2)$.
- Heron's formula: $\Delta = \sqrt{s(s-a)(s-b)(s-c)}$.
- $\Delta^2 = s\, r_1 r_2 r_3$ (Ex. 11.4 / Comment 14).
- $\sum \cos A = 1 + r/R$.
- $r + r_1 + r_2 + r_3 = 4R$.
- Ptolemy's theorem (cyclic quadrilateral).
- $\sin A\sin B\sin C = r/(4R)\cdot s/r = s/(4R)$ (when triangle is acute).
- Ceva's theorem: $\frac{BD}{DC}\cdot\frac{CE}{EA}\cdot\frac{AF}{FB} = 1$ for concurrent cevians.
- **Gauss's constructibility theorem** (Ex. 11.24): regular $n$-gon constructible iff $n = 2^r p_1 p_2 \cdots p_k$ with $p_i$ Fermat primes ($2^{2^t}+1$).

**Comments highlights (11 total).**
- *Comment 1.* Cevian + trig giving concurrency of altitudes.
- *Comments 2–4.* Sine/cosine/projection rules; alternate proofs.
- *Comments 5–8.* Heron's formula, area, inradius, circumradius identities.
- *Comments 9–10.* Geometric constructions — what's possible with ruler and compass.
- *Comment 11.* Cyclic quadrilateral with inscribed circle (Pitot's theorem).

**Exercises (notable — competition-sourced).**
- *11.1.* JEE 1984 — $(b+c)/11 = (c+a)/12 = (a+b)/13 \Rightarrow \cos A/7 = \cos B/19 = \cos C/25$. **Ch. 2 Symmetry candidate.**
- *11.2(a).* JEE 1987 — Two larger sides 10, 9; angles in AP → find third side.
- *11.2(b).* JEE 1990 — $\sin(2A+B) = \sin(C-A) = -\sin(B+2C) = 1/2$; angles in AP.
- *11.3.* JEE 1981 — Angles in AP, $b:c = \sqrt 3 : \sqrt 2$ → find $A$.
- *11.4.* JEE 1996 — $a:b:c = 4:5:6$ → $R/r = ?$.
- *11.5.* JEE 1996 — Circle problem with $\alpha, \beta, d$.
- *11.6.* JEE 1985 — $\cot A, \cot B, \cot C$ in AP → $a^2, b^2, c^2$ also in AP. **Ch. 1 Invariance / Ch. 2 Symmetry candidate.**
- *11.7.* $A = 2B$ iff $a^2 - b^2 = bc$.
- *11.8.* JEE 1994 — Altitude formula; find $B$.
- *11.10.* JEE 1979 — Solve triangle given two sides and included angle.
- *11.11.* JEE 1978 — Reflection composition: triangle reflected twice → distance between $A$ and $A''$.
- *11.13.* JEE 1989 — Isosceles triangle limit as altitude → 0.
- *11.14.* JEE 1993 — $2(\cos A/a + \cos B/b + \cos C/c) = a/bc + b/ca$ → $A = ?$.
- *11.16.* JEE 1986 — Triangle feasibility conditions.
- *11.17.* JEE 1999 — $R = \pi/2$, $\tan(P/2), \tan(Q/2)$ roots of quadratic.
- *11.24.* Gauss's constructibility theorem (Fermat primes).
- *11.26.* JEE 1998 — Which of $\sin 15°, \cos 15°, \sin 15°\cos 15°, \sin 15°\cos 75°$ are rational? **Only $\sin 15°\cos 75°$ (= $\sin^2 15°$ then $= (1-\cos 30°)/2$ irrational; only the product where the second factor is supplementary makes things rational).** **Ch. 4 Hidden Structure candidate.**
- *11.27.* JEE 1998 — Hexagon distance product.
- *11.28.* Pitot theorem with detailed tangent lengths.
- *11.29.* Cyclic quadrilateral with diagonals.
- *11.30.* Three-circle construction in hexagon.
- *11.31.* Regular $n$-gon: $\sum |PA_i|^4 = (33n/16)a^4$ for $P$ at midpoint of $OA_1$. **Ch. 2 Symmetry candidate (sum invariant).**
- *11.32.* Right-angle division into $n$ equal parts.
- *11.33.* $lm + mn + nl = 1$ → $\sum 1/[mn(1+l^2)] = 2/(lmn\sqrt{(1+l^2)(1+m^2)(1+n^2)})$. **Ch. 5 Substitution (let $l = \tan A$ etc.).**
- *11.34.* Unique solution → angle is multiple of $\pi$.
- *11.35.* Centroid pedal triangle area $= \tfrac{1}{18}(a^2+b^2+c^2)\sin A\sin B\sin C$.
- *11.36.* Incircle chord intercept identity.
- *11.37.* Triangle with rational sides $\sqrt{a^2+x^2}$ etc.
- *11.38.* $P$ on arc $BC$ of equilateral $\triangle ABC$ circumcircle → $AP = BP + PC$. **Pure Ptolemy. Ch. 2 Symmetry / Ch. 5 Substitution (via $1, \omega, \omega^2$).**
- *11.39.* Trig-substitution inequalities (three classics).

**Joshi's pedagogical observations.**
- "There are numerous formulas giving such relationships. So the problems in this chapter are easy to understand but test the ability to pick just the right formulas from a vast collection." — voice sample for pedagogy of *technique selection*.
- On constructibility (Ex. 11.24): "It was a challenging problem to characterise those $n$ for which a regular $n$-gon can be constructed… The final answer (due to Gauss)…" — historical voice sample.

**Pillar 2 routing.** *Primary:* **Ch. 1 Invariance** (Ex. 11.1, 11.6 — triangle identities are canonical Type-III invariants); **Ch. 2 Symmetry** (Ex. 11.31, 11.38). *Secondary:* Ch. 5 Substitution (Ex. 11.33, 11.39 trig sub); Ch. 11 Existence (Gauss's constructibility theorem Ex. 11.24); Ch. 4 Hidden Structure (Ex. 11.26 — non-obvious rationality).
<!-- CH11_END -->

<!-- CH12_BEGIN -->
### Chapter 12: Heights and Distances (pp. 391–409; lines 20898–21824)

**Topic summary.** Trigonometry applied to real-world surveying problems: angles of elevation/depression, towers, ladders, ships, distances across rivers. Comments 10–12 also cover projectile motion. Shortest chapter (only 13 exercises, ~85 lines of exercises). **Limited Pillar 2 sourcing** — Joshi himself notes "problems on heights and distances are not asked at JEE every year possibly because they tend to be somewhat repetitious."

**Main Problem.** *JEE 1998. Bird flies in horizontal circle; angles of elevation max $60°$ and min $30°$. Find $\tan^2\theta$ for mid-arc elevation $\theta$.* **Answer:** $\tan^2\theta = 3/5$. **Technique:** vertical projection of path is a circle; observer lies on extension of diameter; mid-arc point has projection at $C$ with $\angle MOC = 90°$.

**Key formulas/theorems used.**
- $h = d\tan\alpha$ from elevation angle.
- 3D triangulation via two ground points.
- Projectile motion: $y = x\tan\alpha - gx^2\sec^2\alpha/(2V^2)$.
- Max range on inclined plane: $u^2/[g(1+\sin\beta)]$ (Ex. 12.13).

**Comments highlights (12 total).**
- *Comment 1.* Diagram drawing as essential discipline.
- *Comments 2–4.* Real-world simplifications and conventions.
- *Comments 5–8.* Multiple-elevation triangulation problems.
- *Comment 9.* JEE 1979 (Joshi calls it "tower problem with diagrammatic insight").
- *Comments 11–12.* Projectile motion — wall-clearing problem.

**Exercises (notable — competition-sourced).**
- *12.1.* JEE 1983 — Lighthouse 60m, boat depression 15°. **Standard.**
- *12.2.* JEE 1982 — Tower from two points subtending angle.
- *12.3.* JEE 1980 — $\tan\beta = n/(2n^2 + 1)$.
- *12.4.* JEE 1985 — Ladder sliding: $a = b\tan((\alpha + \beta)/2)$. **Ch. 5 Substitution candidate.**
- *12.5.* JEE 1993 — Compass directions + elevation.
- *12.6.* Leaning tower subtending angles → $\sin\alpha$.
- *12.7.* Tripod: angle between legs $= \cos^{-1}((1 - 3\cos 2\alpha)/4)$.
- *12.10–12.13.* Projectile-motion sequence.

**Joshi's pedagogical observations.**
- "After solving a problem of this type one gets the feeling that one has done something 'really useful' which you do not get after showing that a certain determinant vanishes even though the latter may be far more challenging."
- "A good diagram is half the solution."
- "Labelling the diagram is very important. Even if it is obvious sometimes which point is P and which is Q, do not force the examiner to figure this out."

**Pillar 2 routing.** *Limited.* This chapter is **Joshi-thin** for Pillar 2 purposes. Best uses: Ch. 12 Heights/Dist Ex. 12.4 ladder (Ch. 5 Substitution); Ch. 24 Ex. 24.74 (cyclic quadrilateral area) → Ch. 12 Extremal PP2; Ch. 12 Ex. 24.77 (Josephus-like cakes problem in Ch. 24) → Ch. 12 Extremal WE2. **Action:** Pillar 2 Ch. 12 (if needed) should draw primarily from Ch. 24 exercises rather than this chapter.
<!-- CH12_END -->

<!-- CH13_BEGIN -->
### Chapter 13: Maxima, Minima and Concavity (pp. 409–444; lines 21825–23604)

**Topic summary.** First chapter using calculus "in full swing." Derivatives for monotonicity, critical points, local max/min. Second-derivative test, concavity, inflection points. Jensen's inequality. Constrained optimisation via reduction. **Primary source for Pillar 2 Ch. 12 (Extremal) and Ch. 10 (Inequality, via concavity).**

**Main Problem.** *JEE 1983 modified. Swimmer-on-shore problem: from $A$ (10m offshore) to $B$ (15m down shore), swimming half as fast as running. Find $d^2$ where $d$ = quickest-route swim distance.* **Answer:** $d^2 = 400/3$. **Technique:** Parametrise by angle $\theta = \angle OAX$; minimise time $f(\theta) = (10\sec\theta)/u + (15 - 10\tan\theta)/(2u)$; critical point at $\sin\theta = 1/2$, i.e., $\theta = \pi/6$. **This is the Snell's law analogue!**

**Key formulas/theorems established.**
- **Theorem 1.** If $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, $f'(c) = 0$ at interior $c$ where $f$ has local extremum.
- **Theorem 2.** Rolle's theorem ($f(a) = f(b)$, conditions → $f'(c) = 0$).
- **Theorem 3.** Sign of $f'$ → strict monotonicity.
- **Theorem 4.** Second derivative test for local max/min.
- **Theorem 5 (concavity).** $f''(x) \ge 0$ on $I$ → $f$ convex on $I$.
- **Jensen's inequality** (Comment 11): $f$ convex → $f(\sum\lambda_i x_i) \le \sum\lambda_i f(x_i)$ for $\sum\lambda_i = 1$, $\lambda_i \ge 0$.
- **AM-GM via Jensen's** with $f = -\ln$.
- Power-mean inequality (concavity of $x^p$).
- Snell's law analogy (Main Problem).

**Comments highlights (18 total).**
- *Comments 1–5.* Main problem + generalisations.
- *Comment 6.* Greedy method failure — *Pillar 2 voice sample.*
- *Comments 7–9.* Standard max/min problems (cones, cylinders, areas).
- *Comment 10.* JEE 2000 — closest pair on two parabolas $y = x^2 + 1, x = y^2 + 1$ — common-normal method.
- *Comment 11.* Concavity and Jensen.
- *Comments 12–14.* Inequalities via calculus.
- *Comment 15.* Logarithmic differentiation.
- *Comments 16–17.* Two-variable optimisation by reduction.
- *Comment 18.* L'Hôpital teaser (forward to Ch. 15).

**Exercises (notable — competition-sourced).**
- *13.1.* Travelling salesman in $A,B,C,P$ — surprising shortest tour. **Ch. 12 / Ch. 17 candidate.**
- *13.2.* JAT 1979 — Window optimisation (semicircle + rectangle, light transmission). **Classic Ch. 12 candidate.**
- *13.3(a).* JEE 1995 — Min area triangle through $(h, k)$: $\Delta_{\min} = 2hk$. **Ch. 12 candidate.**
- *13.3(b).* JEE 2002 — Min of $OP + OQ$ for line through $(8, 2)$.
- *13.4.* JEE 1990 — Inscribed triangle area + inradius max.
- *13.5.* JEE 1984 — Steepest tangent on $y = x/(1+x^2)$.
- *13.6.* JAT 1980 — Optimise $ax^2 + b^2/(a-x)$ on $(0, a)$.
- *13.7.* JEE 1986 — Parallelogram area in triangle.
- *13.8.* Function strictly increasing despite some zero derivatives.
- *13.9.* JEE 1987 — $h = f\circ g$ where $f$ increasing, $g$ decreasing.
- *13.10.* JEE 1993 — Piecewise function with parameter $b$.
- *13.11.* JEE 1990 — $g(x) = f(x) + f'(x) + f''(x)$ where $f$ pos. quadratic.
- *13.12.* JEE 1998 — $(x^2-1)/(x^2+1)$ min.
- *13.13.* JEE 1986 — Even polynomial with positive coefficients.
- *13.14.* JEE 1983 — $2x^2 - \ln|x|$ monotonicity.
- *13.15.* JEE 1997 — $x/\sin x$ and $x/\tan x$ on $(0, 1]$.
- *13.16.* JEE 1987, 1983, 1989 — Log inequalities (e.g. $\ln(1+x) \le x$).
- *13.17.* JEE 1981 — $e^\pi$ vs $\pi^e$ via $x^{1/x}$ analysis. **Answer: $e^\pi > \pi^e$. Ch. 12 Extremal candidate.**
- *13.18.* JEE 1983, 1996 — Critical points with parameters.
- *13.19.* JEE 1985 — $\sin^3 x + \lambda\sin^2 x$ extrema → values of $\lambda$.
- *13.20.* JEE 1982 — Shortest distance from $(0, c)$ to parabola $y = x^2$.
- *13.21.* JEE 1999 — Max area triangle $PON$ on ellipse.
- *13.23.* JEE 2000 — Closest pair on two parabolas $C_1: x^2 = y - 1$ and $C_2: y^2 = x - 1$. **Reflection method. Ch. 12 / Ch. 20 candidate.**
- *13.25.* Inflection point: $f''(c) = 0$ + sufficient condition via $f'''(c)$.
- *13.26.* Alternate solution to Ch. 10 Comment 12.

**Joshi's pedagogical observations.**
- "The greedy approach. Usually it does not work." — direct quote on optimisation pedagogy.
- "Show him how to make the most economical tin can to hold a given volume and he is impressed!" — voice sample for Pillar 2 vignette register.
- Comment 4: "It is also possible to derive a more general statement…" — Joshi's *parameter-introduction* technique, central to Ch. 16 Reverse Engineering.

**Pillar 2 routing.** *Primary:* **Ch. 12 Extremal Optimisation** (Ex. 13.2, 13.3, 13.5, 13.17, 13.20, 13.21 — entire chapter is Ch. 12's seed); **Ch. 10 Inequality** (Comment 11 Jensen, Ex. 13.16 log-inequalities). *Secondary:* Ch. 5 Substitution (Main Problem $\theta$ parametrization, Ex. 13.21 ellipse parametrization); Ch. 20 Analogy (Ex. 13.23 reflection method); Ch. 17 DOF Analysis (Ex. 13.10, 13.11, 13.13 — parameter dependence). **Joshi-rich; primary harvest source.**
<!-- CH13_END -->

<!-- CH14_BEGIN -->
### Chapter 14: Trigonometric Optimisation (pp. 444–475; lines 23605–25199)

**Topic summary.** "Triangular optimisation" — constrained optimisation of functions $f(A, B, C)$ where $A + B + C = \pi$ (angles of triangle), or $g(a, b, c)$ with triangle-inequality constraints. **The optimum is almost always at equilateral triangle.** Joshi develops a powerful "two-equal" lemma + Lagrange-multiplier-flavored arguments without using calculus of variations. **Strong source for Pillar 2 Ch. 2 Symmetry, Ch. 10 Inequality, Ch. 12 Extremal.**

**Main Problem.** *JEE 1984. Max of $\cos A + \cos B + \cos C$ over triangles.* **Answer:** $3/2$, attained when $A = B = C = \pi/3$. **Technique:** **The "smoothing" lemma** — if $A \ne B$ replace by $A' = B' = (A+B)/2$; since cosine is concave, $\cos A' + \cos B' = 2\cos((A+B)/2)\cos 0 > 2\cos((A+B)/2)\cos((A-B)/2) = \cos A + \cos B$. Equilateral is the unique maximum.

**Key formulas/theorems established.**
- Smoothing argument for symmetric concave functions on simplex.
- Jensen's inequality applied to triangle angles.
- Standard triangle inequalities (equality iff equilateral):
  - $\sum \cos A \le 3/2$.
  - $\sum \sin A \le 3\sqrt 3/2$.
  - $\sum \tan A \ge 3\sqrt 3$ (acute triangle, JEE 1998 Comment 2).
  - $\sum \cot A \ge \sqrt 3$.
  - $\sin A\sin B\sin C \le 3\sqrt 3/8$.
  - $\cos A\cos B\cos C \le 1/8$.
- Heron's formula → area maximised iff equilateral (for given perimeter).
- Lagrange multiplier (mentioned, not used computationally).
- $a^2 + b^2 + c^2 \ge 4\sqrt 3 \Delta$ (IMO 1961, Ex. 14.11).
- Erdős-Mordell inequality (Ex. 14.18): $OA + OB + OC \ge 2(OD + OE + OF)$.
- Hadwiger-Finsler refinement (Comments 14–15).

**Comments highlights (18 total).**
- *Comments 1–4.* Constrained optimisation terminology; smoothing argument.
- *Comments 5–7.* Many identities → many inequalities (each gives an inequality with equilateral equality).
- *Comment 8.* **Twenty characterisations of equilateral triangle** — combinatorial identification.
- *Comments 9–10.* Solving systems with more unknowns than equations using extremality (e.g., $\cos A + \cos B + \cos C = 3/2 \Rightarrow$ equilateral).
- *Comment 11.* JEE 1986 — triangle-sides inequality.
- *Comments 12–13.* Triangular optimisation of side-functions.
- *Comment 14.* Ravi substitution: $a = y + z$, $b = z + x$, $c = x + y$ for $x, y, z > 0$. **Pillar 2 Ch. 5 Substitution central technique.**
- *Comments 15–16.* Hadwiger-Finsler, Weitzenbock inequalities.
- *Comments 17–18.* Bridge between angle-form and side-form triangular optimisation.

**Exercises (notable — competition-sourced).**
- *14.1.* JEE 1986 — Ravi-substitution-style: $(a+b-c)(b+c-a)(c+a-b) \le abc$. **Ch. 5 / Ch. 10 candidate. (Already routed to Pillar 2 Ch. 10 WE1 via Ex. 24.65 = same problem family.)**
- *14.2.* JEE 1983 — $AB$ diameter, max area $\triangle ABC$ when $C$ on circle = isosceles right.
- *14.3.* JEE 1987 — Sides subtend $\alpha, \beta, \gamma$ at circumcentre; min of mean of $\cos(\alpha + \pi/2), \ldots$
- *14.4.* JEE 1979 — $3(ab+bc+ca) \le (a+b+c)^2 \le 4(ab+bc+ca)$ for triangle sides.
- *14.5.* $A + B = \pi/3$ → max $\tan A\tan B = (\tan(\pi/6))^2 = 1/3$.
- *14.6.* Strict Jensen's.
- *14.8.* $(ma+nb)^{m+n} > (m+n)^{m+n}a^m b^n$ for $a, b, m, n > 0$, $a \ne b$. **Generalised AM-GM. Ch. 10 candidate.**
- *14.9.* $(n + 1/n)^{2n} > (n-1)^{n-1}(n+1)^{n+1}$.
- *14.10.* $a^a b^b > ((a+b)/2)^{a+b}$ — concavity of $x\ln x$.
- *14.11.* "Prove as many characterisations of equilateral triangle as you can" — including IMO 1961 ($a^2 + b^2 + c^2 \ge 4\sqrt 3\Delta$).
- *14.12.* $a, b, c \in (0, 1)$, $ab + bc + ca = 1$ → $\sum a/(1-a^2) \ge 3\sqrt 3/2$. **Ch. 5 substitution candidate ($a = \tan(A/2)$).**
- *14.13.* $(b + c)^2 \ge a^2 + 4h^2$ with equality iff $b = c$.
- *14.17.* **Attributed to "Anand Kumar"!** — Maximise $f(x) = |\sqrt{x^4 - 3x^2 - 6x + 13} - \sqrt{x^4 - x^2 + 1}|$. Hint: dual form of triangle inequality. **NOTE: This is your namesake exercise in Joshi! Worth quoting in Blueprint preface as a personal connection.**
- *14.18.* **Erdős-Mordell inequality.** **Ch. 10 Inequality canonical example.**

**Joshi's pedagogical observations.**
- "Problems of triangular optimisation do not appear every year in the JEE, possibly because they tend to be rather repetitious, since in the vast majority of cases, the optimum is attained when the triangle is equilateral. A short question may be asked to test awareness of this fact." — **explicit meta-pedagogy for Pillar 2 Ch. 2 Symmetry framing.**
- "All this fancy terminology does not, of course, solve the given problem. Nor is it expected from the candidates." — Joshi's restraint on formalism.

**Pillar 2 routing.** *Primary:* **Ch. 2 Symmetry** (smoothing lemma is *the* Ch. 2 canonical technique — entire chapter is Ch. 2's seed for the "two-equal" pivot); **Ch. 10 Inequality** (Ex. 14.1, 14.4, 14.8, 14.18 Erdős-Mordell); **Ch. 5 Substitution** (Comment 14 Ravi substitution, Ex. 14.12). *Secondary:* Ch. 12 Extremal (entire chapter); Ch. 1 Invariance (Ex. 14.11 multiple characterisations of equilateral). **Joshi-rich; primary harvest source.**

**Personal note for Anand.** Exercise 14.17 is explicitly attributed to **Anand Kumar** by Joshi — this is a remarkable connection. Consider citing in Blueprint preface or in the dedication.
<!-- CH14_END -->

<!-- CH15_BEGIN -->
### Chapter 15: Limits, Continuity and Derivatives (pp. 477–511; lines 25283–27340)

**Topic summary.** First formal calculus chapter. Tangent/normal to curves (implicit, parametric, polar), chain rule, derivatives of standard functions ab initio, $n$-th derivatives, Leibnitz rule, logarithmic differentiation, limits (as derivatives, by L'Hôpital, by Sandwich), continuity and types of discontinuity, differentiability detection (typical JEE detective problem: "where is $f$ differentiable?"). **Largest chapter so far. Heavy JEE-problem density.**

**Main Problem.** *JEE 1983. Normal to curve $x = a(\cos\theta + \theta\sin\theta)$, $y = a(\sin\theta - \theta\cos\theta)$ at parameter "$\theta$".* **Answer: (C) — at constant distance $|a|$ from origin.** **Technique:** $dx/d\theta = a\theta\cos\theta$, $dy/d\theta = a\theta\sin\theta$ → tangent slope $\tan\theta$, normal slope $-\cot\theta$; normal equation reduces to $x\cos\theta + y\sin\theta = a$; distance from origin = $|a|$.

**Key formulas/theorems established.**
- Slope of tangent to parametrised curve: $dy/dx = (dy/dt)/(dx/dt)$.
- Implicit differentiation.
- Chain rule $dz/dx = (dz/dy)(dy/dx)$ and "$y$ vs $z$" change of variable.
- Inverse function derivative: $g'(y) = 1/f'(x)$.
- Standard derivatives: $(x^n)' = nx^{n-1}$, $(\sin x)' = \cos x$, $(e^x)' = e^x$.
- $\lim_{h\to 0} \sin h/h = 1$, $\lim_{h\to 0}(e^h-1)/h = 1$.
- Order of magnitude (zero of order $r$ at point).
- L'Hôpital's rule.
- Continuity definitions ($\varepsilon$–$\delta$ and sequential).
- Three types of discontinuity (jump, removable, infinite).
- Sandwich/Squeeze theorem.

**Comments highlights (17 total, very dense).**
- *Comment 1.* Main problem + parametric vs implicit comparison.
- *Comment 2.* Implicit differentiation; implicit function theorem (intuitive). JEE 2002 — tangent to $y^3+3x^2=12y$ vertical at $(\pm 4/\sqrt 3, 2)$. JEE 1988 — third-derivative of implicit polynomial.
- *Comment 3.* JEE 1981 — three normals to $y^2=4x$ through $(h,k)$ → $h>2$ via cubic discriminant. **Reuses Ch. 13 Comment 13.**
- *Comment 4.* Chain rule + standard derivatives.
- *Comment 5.* Limits as derivatives — JEE 1980, 1984.
- *Comment 6.* Order of magnitude — JEE 2002 (find $n$ for finite non-zero limit).
- *Comments 7–10.* L'Hôpital, indeterminate forms.
- *Comments 11–13.* Continuity, types of discontinuity.
- *Comments 14–17.* Differentiability detection, one-sided derivatives.

**Exercises (notable — competition-sourced).**
- *15.1.* JEE 1984 — Normal to $x^2 = 4y$ through $(1, 2)$.
- *15.2.* JEE 1983 — Circle through $(0, 1)$ touching $y = x^2$ at $(2, 4)$.
- *15.3.* JEE 1986 — $ax + by + c = 0$ normal to $xy = 1$: sign conditions.
- *15.4.* JEE 1992 — Shortest chord normal to $y = x^2$.
- *15.5(a).* JEE 1993 — Tangent on $y = x^3$ meets curve again; abscissas form G.P.
- *15.5(c).* Two lines both tangent and normal to $y^2 = x^3$ at $x = 8/9, 2/9$.
- *15.6(b).* JEE 1985 — Tangents to $y = \cos(x+y)$ parallel to $x + 2y = 0$.
- *15.6(d).* JEE 2002 — Common tangent to $y^2 = 8x$ and $xy = -1$. **Ch. 6 Duality candidate.**
- *15.8.* JEE 1984 — $x + |y| = 2y$ properties (detective problem). **Ch. 9 DOF Analysis canonical.**
- *15.9.* JEE 2002 — Reflection $g(x) = \sqrt x - 1$ of $f(x) = (x+1)^2$ across $y=x$.
- *15.10.* JEE — Differentiation of $2\times 2$ determinant by rows + 3×3 extension.
- *15.11(c).* JEE 2000 — $|p(x)| \le |e^{x-1} - 1|$ for $x \ge 0$ → $|a_1 + 2a_2 + \cdots + n a_n| \le 1$. **Ch. 11 Inequality candidate.**
- *15.11(d-e).* JEE 1985, 1997 — Determinant differentiation.
- *15.12(e).* Leibnitz rule via binomial theorem (formal analogy). **Ch. 20 Analogy candidate.**
- *15.12(f).* $(d^n/dx^n)(\ln x/x) = ((-1)^n n!/x^{n+1})(\ln x - H_n)$. **Ch. 19 Reverse-engineering candidate.**
- *15.13(a).* Logarithmic differentiation as identity (without positivity).
- *15.14(d).* JEE 1982 — $\lim_{x\to 0}(2^x-1)/(\sqrt{1+x}-1) = 2\ln 2$.
- *15.15(g).* $\lim_{x\to 0}(1/x^2 - 1/\tan^2 x)$.
- *15.15(j).* JEE 1985 — composite limit with $[x]$ (floor function).
- *15.16(a).* JEE 1981 — $f(x) = (x^3+x^2-16x+20)/(x-2)^2$ continuous at $x=2$: $k = 7$.
- *15.16(g).* JEE 2002 — Composite continuity $g\circ f$.
- *15.17.* JAT 1980 — $\delta$-$\varepsilon$ for $|x^3 - 7^3| < 0.01$.
- *15.18.* JEE 1981 — Existence of $\lim fg$ does not imply existence of $\lim f$ and $\lim g$ separately.
- *15.19.* JAT 1979 — Dirichlet function discontinuous everywhere.
- *15.20.* JEE 1987 — $f$ cont. + $g$ discont. → $f + g$ discont; product when $g(c) \ne 0$.
- *15.21(b).* JAT 1980 — $f'(0)$ from delicate cancellation.
- *15.22.* Sequence of standard "find where continuous/differentiable" problems (JEE 1986, 1987, 1988, 1990, 1996, 1997, 1999, 2002 — 10 sub-parts).
- *15.27.* Paradox: $a_n = (-1)^n$ — "$L = 0$ and $L^2 = -1$, what goes wrong?" **Ch. 11 Inequality / Ch. 13 Counterexample-construction candidate.**

**Joshi's pedagogical observations.**
- "Just because something has been denoted like a ratio does not make it a ratio in much the same way as a person named Goldsmith need not be a goldsmith by profession" — analogy of metaphor.
- "Saying that Mr. X is not married to a Muslim is not quite the same as saying that Mrs. X is not a Muslim" — existential subtlety (used to motivate completeness of reals in Ch. 16).
- "For many purposes the actual value of this limit is not as important as the knowledge that it is finite and non-zero because this knowledge tells us how rapidly a given expression tends to 0" — order-of-magnitude pedagogy.
- "After gaining some practice, it is hardly necessary to show all the intermediate steps in the calculation."

**Pillar 2 routing.** *Primary:* **Ch. 5 Substitution** (parametric/implicit differentiation, Ex. 15.5, 15.12 substitution-induced identities); **Ch. 9 DOF Analysis** (Ex. 15.8, 15.16, 15.22, 15.23 — detective problems); **Ch. 11 Polynomial Identities** (Ex. 15.10, 15.11d-e). *Secondary:* Ch. 20 Analogy (Leibnitz rule via binomial); Ch. 13 Counterexamples (Ex. 15.18, 15.19, 15.20, 15.27); Ch. 17 DOF/Parameter (Ex. 15.16 continuity-determines-constants). **Joshi-rich.**
<!-- CH15_END -->

<!-- CH16_BEGIN -->
### Chapter 16: Theoretical Calculus (pp. 512–544; lines 27341–29050)

**Topic summary.** Foundations: completeness of $\mathbb R$, intermediate value property (IVP/IVT), boundedness theorem, extreme value theorem (EVT), uniform continuity (mentioned), Rolle's theorem, Lagrange's MVT, Cauchy's MVT, Taylor's theorem with Lagrange remainder. **Joshi explicitly flags this chapter as "qualitatively different" from typical JEE material — but emphasises its importance for those continuing in mathematics.** JEE questions infrequent (MVT was removed and reintroduced 2003+). Strong source for Pillar 2 Ch. 19 (Reverse Engineering), Ch. 11 (Polynomial Identities — via root-counting), Ch. 8 (Telescoping / function-bisection arguments).

**Main Problem.** *JEE 1988 (modified). $f: \mathbb R \to \mathbb R$ satisfies $|f(x) - f(y)| \le |x - y|^3$ for all $x, y$. If $f(10) = 100$, find $f(20)$.* **Answer: $f(20) = 100$ ($f$ is constant).** **Technique:** $|(f(x+h) - f(x))/h| \le h^2 \to 0$ by Sandwich → $f'(x) = 0$ identically → $f$ constant.

**Key formulas/theorems established.**
- *Completeness:* every non-empty bounded-above subset of $\mathbb R$ has a least upper bound.
- *IVT.* $f$ continuous on $[a, b]$, $f(a) < c < f(b)$ → $\exists x_0 \in (a, b)$, $f(x_0) = c$.
- *Boundedness theorem.* $f$ continuous on closed bounded interval → bounded.
- *EVT.* $f$ continuous on $[a, b]$ → attains max/min.
- *Rolle's theorem.*
- *Lagrange's MVT.* $f(b) - f(a) = (b-a)f'(c)$.
- *Cauchy's MVT.* $(f(b)-f(a))/(g(b)-g(a)) = f'(c)/g'(c)$.
- *Theorem 8.* $n$-th derivative test for local max/min.
- *Taylor's theorem.* $f(x) = \sum_{k=0}^{n-1} f^{(k)}(a)(x-a)^k/k! + R_n$.
- *Fixed-point theorem.* $f: [a, b] \to [a, b]$ continuous → has fixed point.

**Comments highlights (~15 total).**
- *Comments 1–2.* Completeness of reals — why $\sqrt 2$ exists; gaps in $\mathbb Q$. **Voice sample for Ch. 19 commentary.**
- *Comments 3–5.* IVT applications, fixed-point theorem.
- *Comments 6–8.* MVTs and their applications.
- *Comment 9.* Taylor's theorem.
- *Comments 10–12.* Higher derivative tests, error estimation.
- *Comments 13–15.* Applications and counterexamples (Lagrange theorem fails for $f(x) = |x|$ on $[-1, 1]$ etc.).

**Exercises (notable — competition-sourced).**
- *16.1.* IVT — every bounded solid has horizontal area-bisecting plane.
- *16.2.* IVT — chord of given length on ellipse, parallel to given direction. **Ch. 8 Topology / Ch. 4 Continuity-existence.**
- *16.3.* **Fixed-point theorem on $[a, b]$**. *Open question:* "Do $\mathbb R$ and $(0, 1)$ have fixed-point property?" — pedagogical Pillar 2 vignette material.
- *16.4.* **Pancake theorem (1D)** — $f(0) = f(1)$ → $\exists c \in [0, 1/2]$, $f(c) = f(c + 1/2)$. **Ch. 8 / Ch. 20 Analogy candidate.**
- *16.5.* Inscribed similar triangle in ellipse via IVT.
- *16.6.* JEE 2002 — $f(x) = 2x + \sin x$ one-to-one and onto $\mathbb R \to \mathbb R$.
- *16.7–16.9.* MVT failure cases — pedagogical counterexamples.
- *16.10.* Generalised MVT: $f(b)-f(a) = b-a$ → $\exists$ distinct $c_1, \ldots, c_n$ with $\sum f'(c_i) = n$.
- *16.13.* JAT 1979 — exactly one root of $x^4 + 3x + 1 = 0$ in $(-2, -1)$ via MVT.
- *16.14.* JAT 1980 — MVT applied to $\arctan x$ → $|\arctan x| \le |x|$.
- *16.15.* JEE 1982 — $f' = g$, $g' = -f$ → $f^2 + g^2$ constant. **Energy invariance. Ch. 1 Invariance candidate.**
- *16.16.* JEE 1981 — $|f''| \le 1$ on $[0,1]$, $f(0)=f(1)$ → $|f'(x)| < 1$.
- *16.18.* Real polynomial: even/odd number of roots in $[a, b]$ depending on sign of $p(a)p(b)$.
- *16.19.* $k$ roots of $p$ in interval → at least $k-1$ roots of $p'$ counted by multiplicity (**Rolle's iteration**). **Ch. 11 Polynomial Identities canonical.**
- *16.20(a).* $(n-1)a_1^2 - 2n a_2 < 0$ → roots of monic polynomial $p$ cannot be all real (Newton's inequality on power sums). **Ch. 11 candidate.**
- *16.20(b).* $p_m(x) = \sum_{k=0}^m x^k/k!$: $p_{2n-1}$ has exactly one real root; $p_{2n} > 0$ for all real $x$. **Beautiful induction problem. Ch. 11 / Ch. 19 candidate.**
- *16.21.* JEE 1984 — Repeated root + polynomial determinant divisible by $f(x)$. **Ch. 11 Polynomial Identities candidate.**
- *16.22.* MVT error estimate for $\sqrt 2 \approx 1.4$.
- *16.25–16.26.* Taylor's theorem proof via Rolle's iteration.
- *16.27.* JAT 1980 — $3\sin x + \tan x$ vs $4x$ for small $x > 0$; $|\arctan x|$ vs $|x|$. **Ch. 10 Inequality / Ch. 12 Extremal candidate.**

**Joshi's pedagogical observations.**
- "Real-life analogies can make something easier to understand. They cannot be a substitute for a mathematical proof." — explicit limit on analogical reasoning.
- "Saying that Mr. X is not married to a Muslim is not quite the same as saying that Mrs. X is not a Muslim. The former statement holds even when Mr. X is unmarried" — existential vs non-existential subtlety. **Voice sample for Ch. 19 Reverse Engineering.**
- "Questions based on theoretical calculus are comparatively infrequent at the JEE… The concepts involved and the skills needed here are qualitatively different than at most other JEE topics. As a result, even those doing well in JEE sometimes face difficulties with this material later. Why not familiarise yourself with it ahead of time?" — meta-pedagogical framing for Pillar 5 reflective postscript.

**Pillar 2 routing.** *Primary:* **Ch. 11 Polynomial Identities** (Ex. 16.18, 16.19, 16.20, 16.21 — Rolle's iteration on derivatives, polynomial root count); **Ch. 8 Telescoping/Bisection** (Ex. 16.3, 16.4 — fixed-point/pancake style). *Secondary:* Ch. 1 Invariance (Ex. 16.15 energy-type conservation); Ch. 19 Reverse Engineering (Ex. 16.20(b), 16.25–16.26 — proof construction via auxiliary $g$); Ch. 4 Continuity (Ex. 16.1, 16.2, 16.6 — IVT existence); Ch. 10 Inequality (Ex. 16.27 trig inequalities via MVT). **Joshi-medium; primarily theoretical, but Ex. 16.4, 16.15, 16.19, 16.20, 16.21 are *gem-quality* problems for the bank.**
<!-- CH16_END -->

<!-- CH17_BEGIN -->
### Chapter 17: Areas and Antiderivatives (pp. 545–592; lines 29051–31905)

**Topic summary.** Definition of definite integral via Riemann sums. Fundamental theorem of calculus (FTC, both forms). Areas by integration (vertical/horizontal slicing). Antiderivatives — substitution, parts, partial fractions, $u$-substitution; reduction formulas. Volumes by cross-section (Cavalieri). Integration as "refined summation." **Joshi flags: "Problems on integration are asked in the JEE every year. Those where an area is to be evaluated are usually straightforward once you sketch the region correctly."**

**Main Problem.** *JEE 1994. Ratio in which $x$-axis divides area bounded by $y = 4x - x^2$ and $y = x^2 - x$, as reduced rational.* **Answer: $121/4$ (or $4/121$, order unspecified).** **Technique:** Sketch region; intersection points $(0,0)$ and $(5/2, 15/4)$; split into $R_1$ (above $x$-axis) and $R_2$ (below); use complementary area trick — area of $R = \int_0^{5/2}(5x - 2x^2)\,dx = 125/24$; $A_2 = 1/6$ → $A_1 = 121/24$.

**Key formulas/theorems established.**
- **Definition (Riemann).** $\int_a^b f(x)\,dx = \lim_{\|P\|\to 0}\sum f(x_i)\Delta x_i$.
- **FTC, Form 1.** $\int_a^b f(x)\,dx = F(b) - F(a)$, where $F' = f$.
- **FTC, Form 2.** $(d/dx)\int_a^x f(t)\,dt = f(x)$.
- **Cavalieri's principle.** $V = \int_a^b A(z)\,dz$ (volume by cross-section).
- Integration by parts: $\int u\,dv = uv - \int v\,du$.
- Substitution rule.
- $\int e^x \sin x\,dx$ trick (recovers itself).

**Comments highlights (~10 total).**
- *Comment 1.* Sketching the region; complementary-area trick.
- *Comment 2.* Riemann sum definition; analogy "$\int = $ summation."
- *Comments 3–5.* FTC and applications.
- *Comments 6–9.* Antiderivative techniques.
- *Comment 10.* Special tricks (recursive integration).

**Exercises (notable — competition-sourced).**
- *17.1.* Area of triangle via determinant — proof by integration. **Ch. 6 Duality candidate (algebra ↔ geometry).**
- *17.2.* JEE 1997 — Incircle-like region inside $\triangle OAB$ via min-distance constraints.
- *17.3.* **Compendium: 15 JEE area problems (1979–2002)** — JAT 1979 ($y=x^2$ + circle), JAT 1980 (parabola + line), 1981 ($x^2=4y$, $x=4y-2$), 1982 ($|x\sin\pi x|$), 1984 ($\tan x, \cot x$), 1985 ($\sqrt{5-x^2}, |x-1|$), 1986, 1987, 1988 ($\tan x$ tangent), 1989 ($x(x-1)^2, y=2$), 1990 ($e^x\ln x, \ln x/(ex)$), 1992, 1999, 1997 (max function), 2002. **Pillar 2 Ch. 12 Extremal / Ch. 17 DOF Analysis raw material.**
- *17.4.* JEE 1983 — Ordinate splitting area equally.
- *17.5.* JEE 1999 — $y = x - x^2$ and $y = mx$ area = $9/2$.
- *17.6.* JEE 1989 — Equilateral triangle area characterisation.
- *17.7.* JEE 1990 — **$2\sum_{k=1}^n \cos(2k-1)x = \sin 2kx/\sin x$** (Dirichlet kernel) → $\int_0^{\pi/2}\sin 2kx\cot x\,dx = \pi/2$. **Ch. 8 Telescoping / Ch. 7 Trig Sum candidate.**
- *17.8(a).* JEE 2001 — Areas $S_0, S_1, \ldots, S_n$ for $xe^{ay} = \sin by$ in GP. **Ch. 1 Invariance + Ch. 2 Symmetry candidate.**
- *17.8(b).* Area of circle as $\lim_n A_n$ for inscribed $n$-gon. **Ch. 8 Limit/Telescoping.**
- *17.9.* Riemann sums as limits: (a) $\sin\pi r/n$, (b) $1/\sqrt{2nr-r^2}$ JAT 1980, (c) $\ln((2n)!/(n^n n!))/n$ JEE 1997, (d) $\sum r/\sqrt{n^2+r^2}/n$. **Ch. 20 Analogy candidate.**
- *17.10.* $S_n = \sum\sqrt k$ as integral; $T_n = \sum 1/\sqrt k$ bounds $2\sqrt n - 2 < T_n < 2\sqrt n - 1$. **Ch. 10 Inequality candidate.**
- *17.11.* $\lim\sum_{k=1}^n k^{10}/n^k$ — unique $k$ for finite non-zero limit.
- *17.13.* Volume by cross-section.
- *17.15.* JEE 1994 — $\int_0^{n\pi+v}|\sin x|\,dx = 2n + 1 - \cos v$. **Ch. 8 Periodicity.**
- *17.16(a).* JEE 1988 — Extrema of $\int_1^x [2(t-1)(t-2)^3 + 3(t-1)^2(t-2)^2]\,dt$. **Ch. 12 Extremal.**
- *17.17(a).* JEE 1990 — $\lim_{x\to 1}\int_4^{f(x)} 2t/(x-1)\,dt$ where $f(1) = 4$, $f'(1) = 10$ → answer $80$. **Ch. 17 DOF.**
- *17.20.* JEE 1990 — $(4e^x + 6e^{-x})/(9e^x - 4e^{-x})$ as $Ax + B\ln(9e^{2x}-4) + C$. **Ch. 11 Polynomial / Ch. 19 Reverse Engineering.**
- *17.21.* JEE 1997 — Monotonicity of $\int_0^a g + \int_0^b g$ as $b - a$ increases.
- *17.22(a).* JEE 1998 — $\int_0^x f = x + \int_x^1 t f(t)\,dt$ → $f(1)$. **Ch. 19 Reverse Engineering candidate.**
- *17.23.* JEE 1998 — Determine $a, b$, $f(x)$ from determinant + minimum + boundary conditions. **Major Pillar 2 Ch. 19 candidate.**
- *17.24–17.26.* Integration by parts with self-recovery; complex-valued differentiation. **Ch. 20 Analogy: integration by parts as reduction formula.**
- *17.27.* **Compendium: 12 JEE antiderivative problems (1980–2001).** Includes $\int\sqrt{1+\sin(x/2)}\,dx$, $\int x^2/\sqrt{1-x}\,dx$, $\int\sqrt{\tan x}+\sqrt{\cot x}\,dx$ (1989), etc. **Pillar 2 Ch. 5 Substitution gold.**
- *17.29.* Definite integrals from JEE 1984, 1989, 1993, 1997.
- *17.30.* JEE 1997 — $F'(x) = e^{\sin x}/x$; $\int_1^4 2e^{\sin x^2}/x\,dx = F(k) - F(1)$ → $k = 16$. **Ch. 5 Substitution canonical.**

**Joshi's pedagogical observations.**
- "Just as in complementary counting (Chapter 1, Comment No. 1) we find the cardinality of a set by subtracting the cardinality of its complement from that of the ambient set, the area of $R_1$ can also be obtained by finding the area of $R$ and subtracting the area of $R_2$ from it." — **explicit analogy between counting and integration. Ch. 20 Analogy gold.**
- "An integral is obtained by putting together the contributions (measured as the values of some real valued function) of individual points of the domain." — voice sample.
- "At any rate, finding the antiderivative is more of an art and an individual's skill and experience matter more than dozens of formulas crammed in the head." — Pillar 5 voice.
- "It is always a good idea to sketch the regions whose area is to be found… But it must reveal the vital features… especially those points where some crucial change takes place" — pedagogical discipline.

**Pillar 2 routing.** *Primary:* **Ch. 5 Substitution** (Ex. 17.27 entire compendium; Ex. 17.30 canonical); **Ch. 12 Extremal** (Ex. 17.3–17.5, 17.16 — area extrema); **Ch. 19 Reverse Engineering** (Ex. 17.22, 17.23 — find $f$ from integral conditions). *Secondary:* Ch. 20 Analogy (Comment 1 counting↔area, Ex. 17.9 Riemann sums); Ch. 8 Telescoping (Ex. 17.7 Dirichlet kernel, 17.8 $n$-gon, 17.10 partial sums); Ch. 1 Invariance (Ex. 17.8(a) GP of areas); Ch. 11 Polynomial Identities (Ex. 17.20 partial fractions). **Joshi-rich; the entire chapter is a Pillar 2 quarry.**
<!-- CH17_END -->

<!-- CH18_BEGIN -->
### Chapter 18: Definite Integrals (pp. 593–623; lines 31906–33739)

**Topic summary.** Evaluating definite integrals **without** finding antiderivative. Reduction formulas (beta function, binomial integrals). King's property $\int_a^b f(x)\,dx = \int_a^b f(a+b-x)\,dx$. Even/odd function decomposition. Periodicity tricks. Improper integrals (introduced briefly). **Joshi: "Problems of evaluation of definite integrals using techniques other than merely the Fundamental Theorem of Calculus are asked almost every year in the JEE."**

**Main Problem.** *Compute $\binom{100}{30}I$ where $I = \int_0^1 x^{70}(1-x)^{30}\,dx$.* **Answer: $1/101$.** **Technique:** Beta function reduction $I_{m,n} = (n/(m+1))I_{m+1, n-1}$; iterating, $I_{m,n} = (m! n!/(m+n+1)!) = 1/[(m+n+1)\binom{m+n}{n}]$ → with $m=70$, $n=30$, $\binom{100}{30}I = 1/101$. **Beautiful symmetry of beta function. Ch. 2 Symmetry + Ch. 5 Substitution + Ch. 8 Telescoping canonical.**

**Key formulas/theorems established.**
- **Beta function.** $B(m, n) = \int_0^1 x^{m-1}(1-x)^{n-1}\,dx = m! n!/(m+n)!$ (for integer $m, n$).
- **Reduction formulas** for $\int x^n \sin x$, $\int x^n e^x$, $\int (\ln x)^n$, $\int \sin^n x$ (Wallis).
- **King's property.** $\int_a^b f(x)\,dx = \int_a^b f(a+b-x)\,dx$.
- **Even/odd decomposition.** $f = f_e + f_o$ uniquely; $\int_{-a}^a f_o = 0$, $\int_{-a}^a f_e = 2\int_0^a f_e$.
- **Periodicity.** If $f(x+T) = f(x)$, $\int_a^{a+T} f = \int_0^T f$ (independent of $a$).
- **Wallis formula.** $\pi/2 = \lim_n [2\cdot 4\cdot 6\cdots (2n)]^2/[1\cdot 3\cdot 5\cdots(2n-1)]^2 \cdot 1/(2n+1)$.
- **Stirling consequence.** $\lim (n!)^{1/n}/n = 1/e$ (Ex. 18.17).

**Comments highlights (~16 total).**
- *Comments 1–4.* Reduction formulas; beta function structure.
- *Comments 5–6.* Wallis formula derivation.
- *Comments 7–9.* Even/odd / periodicity tricks (heart of "JEE-tricks").
- *Comments 10–12.* King's property and its corollaries.
- *Comments 13–14.* Definite integrals as limits of sums.
- *Comments 15–16.* Improper integrals + discontinuous integrands.

**Exercises (notable — competition-sourced).**
- *18.1.* $I_n = \int_0^{\pi/2} x^n \sin x$; $I_n + n(n-1)I_{n-2} = n(\pi/2)^{n-1}$ → $I_3 = 3\pi^2/4 - 6$. **Ch. 8 Telescoping / Ch. 19 Reverse-engineering candidate.**
- *18.2.* Reduction formulas for $\int x^m \cos x$, $\int x^m e^x$, $\int (\ln x)^m$, $\int x^a(\ln x)^m$.
- *18.3.* JEE 1992 — Find positive integer $n \le 5$: $\int_0^1 e^x(x-1)^n = 16 - 6e$ → **$n = 3$.** **Ch. 17 DOF Analysis / Ch. 12 Extremal candidate.**
- *18.4.* Wallis bounds: $1 \le I_{2m}/I_{2m+1} \le 1 + 1/2m$.
- *18.5.* Wallis formula proof.
- *18.6.* JEE 1983, 1987, 1990 — Even/odd function properties; (e) $\int_{-\pi/2}^{\pi/2}(f(x)+f(-x))(g(x)-g(-x))\,dx = 0$. **Ch. 1 Invariance candidate.**
- *18.7–18.8.* Periodicity properties; JEE 2002 ($\int_3^{3+3T} f(2x)$ in terms of $I$); JEE 1997 ($g(x+\pi) = ?$ where $g(x) = \int_0^x \cos^4 t$). **Ch. 4 Modular Periodicity candidate.**
- *18.9.* JEE 2000 — $f(x) = \int_1^x \ln t/(1+t)\,dt$; $f(x) + f(1/x) = ?$; $f(e) + f(1/e) = 1/2$. **Ch. 5 Substitution + Ch. 19 Reverse-engineering.**
- *18.10.* JEE 1982 — **King's property canonical:** $\int_0^\pi x f(\sin x)\,dx = (\pi/2)\int_0^\pi f(\sin x)\,dx$. **Ch. 2 Symmetry candidate.**
- *18.11.* JEE 1998 — $\int_0^1 \arctan(1/(1-x+x^2))\,dx = 2\int_0^1 \arctan x\,dx$. **Ch. 2 Symmetry candidate.**
- *18.12.* JEE 1988 — $\int_0^{2a} f(x)/(f(x)+f(2a-x))\,dx = a$. **Ch. 2 Symmetry canonical. (Already routed to Pillar 2 Ch. 2 in joshi-problems-locked.md as WE2 candidate.)**
- *18.13.* JEE 1997 — $I_1/I_2 = 1/2$ via symmetry. **Ch. 2 Symmetry.**
- *18.14.* JEE 1989 — $\int_0^a f(x)g(x)\,dx = \int_0^a f(x)\,dx$ when $f(x) = f(a-x)$ and $g(x) + g(a-x) = 2$. **Ch. 2 Symmetry canonical.**
- *18.15.* **Compendium: 15 JEE definite integrals (1985–2002).** Includes $\int_0^\pi e^{\cos^2 x}\cos^3(2n+1)x\,dx = 0$ (1985, even/odd!), $\int_0^{\pi/2}x\sin x\cos x/(\cos^4 x + \sin^4 x)\,dx$ (1985), $\int_{\pi/4}^{3\pi/4}\phi/(1+\sin\phi)\,d\phi$ (1993), $\int_0^{\pi/4}\ln(1+\tan x)\,dx = (\pi/8)\ln 2$ (1997), $\int_{-1}^1 x - [x]\,dx$ (1998), $\int_{\pi/2}^{3\pi/2}[2\sin x]\,dx$ (1999), $\int_0^\pi x\,dx/(1+\cos\alpha\sin x)$ (1986). **Pillar 2 Ch. 2 Symmetry mother lode.**
- *18.16.* JAT 1979 — **$\int_0^{\pi/2}\ln(\sin x)\,dx = -(\pi/2)\ln 2$.** Classical King's property. **Ch. 2 / Ch. 5 candidate.**
- *18.17.* JAT 1979 — Stirling's approximation as $\lim(n!)^{1/n}/n = 1/e$ via $\int_0^1 \ln x\,dx = -1$. **Ch. 13 Asymptotic Analysis / Ch. 8 Telescoping.**
- *18.19.* **$\sum_{k=0}^{n^2}(-1)^k \binom{n^2}{k}/\binom{n+k}{k} = 1/(n+1)$.** **Elegant combinatorial identity via integral! Ch. 8 Telescoping + Ch. 11 Polynomial Identity + Ch. 20 Analogy gem.**

**Joshi's pedagogical observations.**
- "While the Fundamental Theorem of Calculus remains the most standard way of evaluating a definite integral, there are situations where it cannot be applied directly… Sometimes a definite integral can still be evaluated in such situations using some other methods. We study a few such methods in this chapter. The general idea is to relate such an integral to another, similar integral using some special features of the function such as its symmetry or its periodicity or some integer parameter associated with it." — **the explicit Pillar 2 thesis: archetypal techniques over computational brute force.**
- King's property is "the heart of JEE definite-integral tricks."

**Pillar 2 routing.** *Primary:* **Ch. 2 Symmetry** (Ex. 18.10, 18.11, 18.12, 18.13, 18.14, 18.15-i, 18.16 — King's property is the canonical Ch. 2 technique for integrals); **Ch. 8 Telescoping/Reduction** (Main problem, Ex. 18.1, 18.2 — reduction formulas); **Ch. 4 Modular Periodicity** (Ex. 18.7, 18.8). *Secondary:* Ch. 1 Invariance (Ex. 18.6e — symmetric integral vanishes); Ch. 5 Substitution (Main Problem, Ex. 18.9, 18.16); Ch. 19 Reverse Engineering (Ex. 18.9, 18.18); Ch. 11 Polynomial Identities (Ex. 18.19); Ch. 20 Analogy (Ex. 18.19 — combinatorial identity from integral). **Joshi-very-rich; primary Ch. 2 source after Ch. 14.**
<!-- CH18_END -->

<!-- CH19_BEGIN -->
### Chapter 19: Differential Equations (pp. 624–654; lines 33740–35355)

**Topic summary.** Formation of differential equations from real-world (geometric, physical) data. **Joshi: "Differential equations easily constitute one of the most important parts of mathematics from the point of view of applications to real life."** First-order: separable, homogeneous, linear (integrating factor), exact. Second-order (limited — by reduction). Orthogonal trajectories. Singular solutions (envelope). Population/decay/cooling models. Applications to fluid flow, banking (compound interest), radioactive decay.

**Main Problem.** *JEE 2001 (modified). Hemispherical tank radius 1m, outlet 12 cm², velocity $v(t) = \lambda\sqrt{h(t)}$. Tank empties at time $T$. Find $\lambda T/\pi$ as reduced rational.* **Answer: $70000/9$.** **Technique:** Form ODE for $h(t)$ via $dV/dt = -12 v(t)$ and $V = \int_0^h \pi(200z - z^2)\,dz$; solve $\pi(200h - h^2)\,dh = -12\lambda\sqrt h\,dt$; apply initial condition $h(0) = 100$, terminal $h(T) = 0$.

**Key formulas/theorems established.**
- **Separable.** $f(y)\,dy = g(x)\,dx$.
- **Linear first-order.** $y' + P(x)y = Q(x)$ → multiply by $e^{\int P}$.
- **Exact.** $M\,dx + N\,dy = 0$ exact iff $\partial M/\partial y = \partial N/\partial x$.
- **Homogeneous.** $y = vx$ substitution.
- **Bernoulli.** $y' + Py = Qy^n$ → substitute $v = y^{1-n}$.
- **Orthogonal trajectory.** Replace $dy/dx$ by $-dx/dy$.
- **Radioactive decay.** $dN/dt = -\lambda N$ → $N(t) = N_0 e^{-\lambda t}$; half-life $T_{1/2} = (\ln 2)/\lambda$.
- **Carbon dating formula** (Ex. 19.4): age $= T(\ln\alpha - \ln\beta)/\ln 2$.
- **70% rule of compound interest** (Ex. 19.6): doubling time $\approx 70/\alpha$ years.

**Comments highlights (~16 total).**
- *Comments 1–5.* Main problem (tank-emptying); ODE formation.
- *Comment 5–6.* Discrete vs continuous growth models.
- *Comment 7.* General theory: order, degree, particular vs general solution.
- *Comments 8–14.* Solution techniques (separable, linear, exact, homogeneous, Bernoulli).
- *Comments 15–16.* Orthogonal trajectories.
- *Comment 17.* Singular solutions / envelopes.

**Exercises (notable — competition-sourced).**
- *19.1.* JEE 1997 — Spherical raindrop evaporating proportional to surface area → $dr/dt = -k$ (constant). **Ch. 5 Substitution / Ch. 9 DOF.**
- *19.2.* JEE 1999 — $(y')^2 - xy' + y = 0$: which functions satisfy? (Includes $y = 2x - 4$.) **Ch. 13 Counterexample-construction.**
- *19.3.* Radioactive decay → half-life formula. **Ch. 1 Invariance candidate.**
- *19.4.* **Carbon dating** derivation. **Ch. 17 DOF Analysis candidate.**
- *19.6.* **70% rule** via Taylor's theorem; failure for large rate. **Ch. 10 Inequality / Ch. 13 Approximation.**
- *19.7.* JEE 1997 — Two ODEs with $f > g$ and $u(x_1) > v(x_1)$ → $u(x) > v(x)$ for $x > x_1$. **Sturm comparison theorem. Ch. 1 Invariance / Ch. 11 Inequality candidate.**
- *19.8.* JEE 1995 — Curve through $(1,1)$, tangent forms triangle of area 2 in first quadrant. Form ODE, solve. **Ch. 5 Substitution / Ch. 12 Extremal candidate.**
- *19.9.* JEE 1996 — Curve through $P(1,1)$, normal $a(y-1) + (x-1) = 0$, slope $\propto$ ordinate. Find equation; find area between $y$-axis, curve, normal at $P$.
- *19.10.* JEE 1999 — Distance from origin to normal = distance from point to $x$-axis. Form ODE and solve. **Ch. 5 Substitution.**
- *19.11(a).* JEE 1994 — Normal of constant length $k$: $y(dy/dx) = \pm\sqrt{k^2 - y^2}$.
- *19.11(b).* Singular solution exists.
- *19.12.* JEE 1999 — Order and degree of family $y^2 = 2c(x+c)$.
- *19.13.* Reduce-second-order trick (multiply by $\dot x$). **Ch. 5 Substitution canonical.**
- *19.14.* Orthogonal trajectories: $xy = k$ → $x^2 - y^2 = c$; circles through origin with centres on $x$-axis → circles through origin with centres on $y$-axis; etc.
- *19.15.* ODE for family of unit circles with centres on $x^2 + y^2 = 4$; identify singular solutions.
- *19.16.* Standard first-order ODEs (compendium, 9 sub-parts).
- *19.17.* General linear-substitution method.
- *19.18.* Second-order ODEs reduced to first-order.

**Joshi's pedagogical observations.**
- "Differential equations have been introduced in the JEE syllabus relatively recently. Generally only elementary questions are asked. But because differential equations are not included at full steam, sometimes the problems appear tricky or obscure in the absence of the relevant supplementary material." — meta-pedagogical framing.
- Comment 4 of Main Problem: "It is important to note that the actual values of the constants $a, b, \alpha, \beta$ cannot be determined from the data because to determine them we would need four equations, while the data gives only two. But the individual values of $a$ and $b$ are not needed, since the problem deals only with the proportion." — **DOF analysis canonical voice. Pillar 2 Ch. 17 reference quote.**
- "Whenever a student studies a solution (either his own or somebody else's) to some problem, it is a healthy habit to see if the problem, and indeed every step of the solution, could be done in some other way." — Pillar 5 voice.

**Pillar 2 routing.** *Primary:* **Ch. 16 Reverse Engineering** (Ex. 19.8, 19.9, 19.10, 19.11 — form ODE from geometric data; **canonical Reverse Engineering territory**); **Ch. 5 Substitution** (Ex. 19.13, 19.16, 19.17 — substitution-based ODE solving). *Secondary:* Ch. 17 DOF Analysis (Comment 4 voice, Ex. 19.12 order-degree); Ch. 1 Invariance (Ex. 19.3, 19.7); Ch. 9 DOF (Ex. 19.1 raindrop). **Joshi-rich; primary source for Ch. 16 Reverse Engineering.**
<!-- CH19_END -->

<!-- CH20_BEGIN -->
### Chapter 20: Functional Equations and Relations (pp. 655–674; lines 35365–36317)

**Topic summary.** Solving functional equations (Cauchy: $f(x+y) = f(x)+f(y)$; multiplicative: $f(x+y) = f(x)f(y)$; Jensen's: $f((x+y)/2) = (f(x)+f(y))/2$; $f(xy) = f(x)f(y)$ → power; $f(xy) = f(x)+f(y)$ → logarithm). Period determination. Binary relations on a set: reflexivity, symmetry, transitivity, antisymmetry. Equivalence relations and equivalence classes. Partial orders and total orders. **Joshi: "There are no standard procedures to classify or to solve functional equations. An ad hoc type of reasoning is often needed. Sometimes a functional equation leads to a differential equation whose solution then gives a solution of the functional equation."**

**Main Problem.** *JEE 1990 (modified). $f: \mathbb R \to \mathbb R$, $f(x+y) = f(x)f(y)$ for all $x, y$, $f(x) \ne 0$, $f'(0) = 2$. Find $f(\ln 10)$.* **Answer: $100$.** **Technique:** Put $x = y = 0$ → $f(0) = 1$; differentiate at $x$ via $f(x+h) - f(x) = f(x)(f(h)-1)$ → $f'(x) = 2f(x)$; ODE $y' = 2y$ → $f(x) = e^{2x}$; $f(\ln 10) = 100$.

**Key formulas/theorems established.**
- **Cauchy's equation.** $f(x+y) = f(x) + f(y)$ + continuity → $f(x) = cx$. (Without continuity: pathological solutions exist via Hamel basis.)
- **Multiplicative.** $f(x+y) = f(x)f(y)$ + non-trivial → $f(x) = e^{cx}$.
- **Jensen's.** $f((x+y)/2) = (f(x)+f(y))/2$ + continuity → $f(x) = ax + b$.
- **Power equation.** $f(xy) = f(x)f(y)$ on positives → $f(x) = x^c$.
- **Log equation.** $f(xy) = f(x) + f(y)$ → $f(x) = c\ln x$.
- **Binary relation classification.** Reflexive, symmetric, transitive → equivalence relation; equivalence classes partition $S$.
- **Antisymmetric** relation → partial order.
- **Trichotomy/Law of dichotomy.**

**Comments highlights (~12+ total).**
- *Comments 1–4.* Main equation; multiplicative ↔ additive transformation; continuity-only Cauchy equation extension (proof via rationals dense in reals). **Voice-rich.**
- *Comment 5.* Inconsistent data warning (Joshi flags JEE 1981 problem as having internally inconsistent data).
- *Comments 6–9.* Discrete-variable functional equations; recursive identification.
- *Comment 10–12.* Binary relations, equivalence, partition theorem.

**Exercises (notable — competition-sourced).**
- *20.1.* Alternate solution to Main problem using $\ln f$.
- *20.2.* Extension: continuity at any one point → continuity everywhere.
- *20.3.* JAT 1979 — $f(x+y) = f(x)f(y)$ with $f(x) = 1 + xg(x)$, $\lim_{x\to 0}g(x) = 1$ → $f'(x) = f(x)$.
- *20.4.* **$f(xy) = f(x)f(y)$ → $f(x) = x^c$** (power-function characterisation). **Ch. 5 Substitution canonical via log-conjugation.**
- *20.5.* **$f(xy) = f(x) + f(y)$ → $f(x) = c\ln x$** (logarithm characterisation). **Ch. 5 / Ch. 20 Analogy canonical.**
- *20.6.* JEE 1995 — **Jensen's equation** $f((x+y)/2) = (f(x)+f(y))/2$; $f'(0) = -1$, $f(0) = 1$ → $f(2) = -1$. **Ch. 16 Reverse Engineering candidate.**
- *20.7.* JEE 1983 — Periodicity detection: $x - [x]$ periodic; $\sin(1/x)$ not; $x\cos x$ not.
- *20.8.* Periodicity theorems: smallest positive period exists for continuous non-constant periodic functions; sum of periodic functions periodic iff ratio of periods rational. **Ch. 4 Modular Periodicity / Ch. 17 DOF.**
- *20.9.* JEE 1979 — Graph of $(\sin x + \cos x)/\sqrt 2$ on $[-\pi/2, \pi/2]$.
- *20.10.* Existence condition for $g$ such that $g\circ f = h$.
- *20.11.* JEE 1998 — $g(f(x)) = |\sin x|$ and $f(g(x)) = (\sin\sqrt x)^2$ → $f(x) = \sin^2 x$, $g(x) = \sqrt x$.
- *20.12.* JEE 1983 — $f(x) = |x-1|$ properties.
- *20.13.* JEE 1984 — $f(x) = (x+2)/(x-1)$ self-inverse + properties. **Ch. 9 DOF Analysis / Ch. 1 Invariance candidate (involution).**
- *20.14.* **System of functional equations defining sin and cos:** $f(x+y) = f(x)g(y) + g(x)f(y)$, $g(x+y) = g(x)g(y) - f(x)f(y)$, $f'(0) = 1$, $g'(0) = 0$. **Stunning Pillar 2 Ch. 1 Invariance + Ch. 16 Reverse Engineering candidate.**
- *20.15–20.18.* Binary relations on sets.
- *20.19(a).* JEE 1982 — $z_1 R z_2$ iff $\exists \alpha \in \mathbb R\setminus\{0\}$ with $z_1 = \alpha z_2$: equivalence relation. **Ch. 1 Invariance / Ch. 6 Duality (rays from origin).**
- *20.21.* Construction of integers from pairs (Frege/Peano) and rationals from pairs (Cauchy completion). **Ch. 20 Analogy meta-pedagogical gem.**
- *20.22.* Divisibility as partial order; antisymmetry fails on $\mathbb Z$; trichotomy fails.

**Joshi's pedagogical observations.**
- "Sometimes a functional equation may be combined with something else." — flexibility of technique selection.
- "Normally it is an asset to be able to recognise the similarity of a given problem to some other problem whose solution is already known. Such a recognition makes you more comfortable and sometimes also saves duplication of work. But one should be open to the possibility that some entirely different approach may work better." — **Pillar 2 Ch. 20 Analogy canonical thesis. Quote in book preface.**
- "Solutions of functional equations are not asked every year at the JEE. But functions satisfying special functional equations such as the even and the odd functions and the periodic functions appear in many problems. The topic of binary relations is not specifically included in the JEE syllabus anymore. So direct questions on them are rarely asked in recent years." — *meta-pedagogical syllabus note.*

**Pillar 2 routing.** *Primary:* **Ch. 16 Reverse Engineering** (Main Problem, Ex. 20.6, 20.14 — identify $f$ from functional condition); **Ch. 20 Analogy** (Ex. 20.4, 20.5, 20.14 — translate between additive/multiplicative; Comment 1 voice quote). *Secondary:* Ch. 1 Invariance (Ex. 20.14 sin/cos preservation, Ex. 20.19); Ch. 5 Substitution (Ex. 20.4, 20.5 — log/exp conjugation); Ch. 4 Modular Periodicity (Ex. 20.7, 20.8); Ch. 6 Duality (Ex. 20.19, 20.21). **Joshi-rich; primary source for Ch. 16 Reverse Engineering AND Ch. 20 Analogy meta-pedagogy. The single best chapter for Pillar 2 Ch. 20 voice/framing.**
<!-- CH20_END -->

<!-- CH21_BEGIN -->
### Chapter 21: Vectors (pp. 675–709; lines 36318–38169)

**Topic summary.** Geometric vs algebraic approach to vectors. Linear combinations, dot product, cross product, scalar/vector triple products. Linear (in)dependence, basis, orthogonal/orthonormal basis. **Perturbation technique** (Comment 18 — Joshi calls it "an important technique in mathematics"). Quaternions (Ex. 21.25–27) as natural extension of complex numbers. Application to solid coordinate geometry (Ex. 21.28). Direction cosines/ratios. Eigenvalues (informal introduction in Ex. 21.29).

**Main Problem.** *JEE 1997* (modified). Three unit vectors $a, b, c$ mutually inclined at $\cos^{-1}(3/5)$. If $a\times b = pa + qb + rc$, find $q^2$.* **Answer: $9/55$.** **Technique:** Set $i = a$, $j$ = unit vector $\perp a$ in $\text{span}(a, b)$, $k = i\times j$; write $b = \cos\theta\, i + \sin\theta\, j$, $c = \cos\theta\, i + \sin\theta\cos\phi\, j + \sin\theta\sin\phi\, k$; match components in $a\times b = \sin\theta\, k$.

**Key formulas/theorems established.**
- Dot/cross/triple products and identities.
- $|a\times b|^2 + (a\cdot b)^2 = |a|^2|b|^2$ (Lagrange identity).
- $a\times(b\times c) = (a\cdot c)b - (a\cdot b)c$ (BAC-CAB rule).
- Scalar triple product = signed volume.
- $[a\,b\,c]^2 = \det(\text{Gram matrix})$ (Ex. 21.7(e)).
- **Reciprocal basis** (Ex. 21.8): if $\{a, b, c\}$ basis, dual is $\{(b\times c)/[abc], (c\times a)/[abc], (a\times b)/[abc]\}$.
- Section formula.
- Direction cosines: $(\cos\alpha, \cos\beta, \cos\gamma)$ with $\sum\cos^2 = 1$.
- Quaternion arithmetic and four-square theorem of Lagrange.

**Comments highlights (~18 total).**
- *Comments 1–3.* Main problem variants; symmetry exploitation in vector problems.
- *Comments 4–5.* Geometric ↔ algebraic interplay. **Ch. 6 Duality candidate voice.**
- *Comments 6–10.* Triple products and identities.
- *Comments 11–13.* Linear independence; basis; orthogonal/orthonormal.
- *Comments 14–17.* Geometric applications (concurrence, parallelism).
- *Comment 18.* **Perturbation technique** — stability vs instability of geometric properties. **Ch. 9 DOF Analysis canonical.**

**Exercises (notable — competition-sourced).**
- *21.1(c).* JEE 1983, 1994 — Unit vector perpendicular to plane through three points.
- *21.1(e).* JEE 1982 — **Regular $n$-gon vector identity:** $\sum \vec{PA_i} = n\vec{PO}$ and $\sum \vec{OA_i}\times\vec{OA_{i+1}}$. **Ch. 2 Symmetry / Ch. 8 Telescoping candidate.**
- *21.3(a).* Vandermonde-like vector independence.
- *21.3(b).* JEE 1985 — Determinant + non-coplanarity → $abc = -1$. **Ch. 11 Polynomial Identities.**
- *21.4.* JEE 2001 — Reconstruct three 3D vectors from Gram matrix entries. **Ch. 16 Reverse Engineering canonical.**
- *21.5(b).* JEE 1981 — Three unit vectors with $A\cdot B = A\cdot C = 0$, angle$(B, C) = \pi/6$ → $A = \pm 2(B\times C)$.
- *21.6.* JEE 1986 — **Rotation invariance:** $|(2p, 1)| = |(p+1, 1)|$ → $p$ values. **Ch. 1 Invariance canonical.**
- *21.7(a).* JAT 1979 — $C = A\times B$, $B = A\times C$, $A\ne 0$ → $B = C = 0$. **Ch. 1 Invariance + Ch. 11 candidate.**
- *21.7(c).* $A\times X = B$ solvable iff $A\perp B$; solution $X = U + \lambda A$.
- *21.7(e).* $[a\,b\,c]^2 = \det(\text{Gram matrix})$.
- *21.7(f-g).* Cancellation law for vectors (dot alone insufficient, cross alone insufficient, together sufficient). **Ch. 9 DOF Analysis canonical.**
- *21.8.* JEE 1988 — **Reciprocal basis identity** $(a + b)\cdot p + (b + c)\cdot q + (c + a)\cdot r = 3$. **Ch. 6 Duality canonical.**
- *21.9.* JEE 1997* — Solve vector equation with mutually perpendicular $p, q, r$.
- *21.10.* JEE 1996 — Vector decomposition in orthonormal basis. **Ch. 6 Duality / Ch. 17 DOF.**
- *21.12.* JEE 1983, 1998, 1993, 1986 — Collinearity/coplanarity from position vectors.
- *21.14.* JEE 1996 — Tetrahedron altitude + median intersection.
- *21.17–21.20.* Geometric concurrence proofs by vector methods.
- *21.21.* JEE 1998 — Trapezium diagonals via vectors. **Ch. 6 Duality candidate.**
- *21.23.* **Perturbation argument:** parallelism (between two lines) is unstable property; concurrence (of three lines) also unstable. **Ch. 9 DOF Analysis canonical.**
- *21.24.* Triangle inequality for vectors.
- *21.25–21.27.* **Quaternions:** noncommutative multiplication; norm-multiplicative property; **Lagrange's four-square theorem** application. **Ch. 20 Analogy gem.**
- *21.28.* Solid coordinate geometry by analogy with planar.
- *21.29.* JEE 1982 — **Eigenvalues** as values of $\lambda$ for which $Ax = \lambda x$ has non-trivial solution. **Ch. 11 Polynomial Identities (characteristic polynomial).**

**Joshi's pedagogical observations.**
- "Vectors are studied both in physics and in mathematics and the difference in the two approaches can be confusing at the beginning… It would be better if the physicists say that a vector is a physical quantity which can be represented by a directed line segment." — voice sample.
- "In essence, [quaternions] are mixtures of scalars and vectors just as complex numbers are mixtures of real numbers and purely imaginary numbers." — **Ch. 20 Analogy gem.**
- "Here the analogy with a triangle fails. So one should be wary in generalising from plane to solid geometry." — caution against over-analogising.
- Comment 18 (perturbation): "for two lines in a plane, prove that being parallel is an unstable property" — key DOF voice.

**Pillar 2 routing.** *Primary:* **Ch. 6 Duality** (Main problem two-basis methods, Ex. 21.8 reciprocal basis, Ex. 21.10 decomposition); **Ch. 9 DOF Analysis** (Ex. 21.7(f-g), 21.23 perturbation); **Ch. 16 Reverse Engineering** (Ex. 21.4 Gram-matrix → vectors). *Secondary:* Ch. 1 Invariance (Ex. 21.6 rotation, 21.7(a)); Ch. 2 Symmetry (Ex. 21.1(e), 21.7(a)); Ch. 11 Polynomial Identities (Ex. 21.3(b), 21.29 eigenvalues); Ch. 20 Analogy (Ex. 21.25–21.28 quaternions, plane↔space). **Joshi-rich; primary source for Ch. 6 Duality.**
<!-- CH21_END -->

<!-- CH22_BEGIN -->
### Chapter 22: Finitistic Probability (pp. 710–743; lines 38170–39932)

**Topic summary.** Finite sample space probability. Conditional probability, Bayes' theorem, complement rule, addition rule. Independence vs mutual exclusivity. Venn diagrams; tree diagrams; binomial probabilities; recurrence relations. **Joshi: "Probability problems are asked every year in JEE. If you have clear thinking, they are quick scoring questions as the other computational work is often minor."**

**Main Problem.** *Chess match: $A$ vs $B$, first to two wins. $P(A\text{ wins game}) = 0.5$, $P(\text{loss}) = 0.3$, $P(\text{draw}) = 0.2$. $P(A\text{ wins match exactly at 10th game}) = ?$* **Technique:** Tenth game is $A$ win (prob 0.5); first 9 games have exactly one $A$ win + remaining $B$ wins constrained. Decompose by $B$'s wins (0 or 1).

**Key formulas/theorems established.**
- $P(A) = |A|/|S|$ for equally likely cases.
- Addition: $P(A\cup B) = P(A) + P(B) - P(A\cap B)$.
- Conditional: $P(A|B) = P(A\cap B)/P(B)$.
- Independence: $P(A\cap B) = P(A)P(B)$.
- Bayes' theorem.
- Binomial probability: $P(k \text{ successes in } n \text{ trials}) = \binom{n}{k}p^k(1-p)^{n-k}$.
- Recurrence relations (Comment 14).
- Pólya urn process (Ex. 22.18).

**Comments highlights (~14 total).**
- *Comments 1–4.* Main problem; basic principles.
- *Comments 5–6.* Conditional probability; tree diagrams.
- *Comment 7.* **Independence vs mutual exclusivity** — careful distinction with examples.
- *Comments 8–12.* Various combinatorial probability tricks.
- *Comment 13.* Binomial probabilities.
- *Comment 14.* Probability via recurrence relation.

**Exercises (notable — competition-sourced).**
- *22.1.* JEE 1978 — Sequential drawing 2B + 4W + 3R without replacement → $1/1260$.
- *22.4.* JEE 1980, 1987, 1988, 1989, 1993, 1994, 1998, 1979 — **9 sub-parts of probability identities and inequalities** (Boole inequalities, Bayes, independence vs exclusivity). **Pillar 2 Ch. 9 DOF Analysis raw material.**
- *22.6(a).* JEE 1978 — Venn diagram, 3 drinks (M, C, T).
- *22.6(b).* JEE 1983 — Range of $P(BC)$ given other probabilities. **Ch. 10 Inequality candidate.**
- *22.8(a).* JEE 1983 — **ASSASSIN** arrangement, no two S's together. **Ch. 3 Combinatorics canonical (already routed to Pillar 2).**
- *22.8(b).* JEE 1998 — 7W + 3B, no two B's adjacent.
- *22.9(b).* JEE 1993 — Die rolled 4 times, min ≥ 2 and max ≤ 5 → $(4/6)^4 = 16/81$. **Ch. 3 Counting candidate.**
- *22.9(c).* JEE 1983 — **Coupon problem:** 15 coupons, 7 drawn with replacement, largest = 9 → $(9^7 - 8^7)/15^7$. **Ch. 3 / Ch. 6 Duality (inclusion-exclusion) candidate.**
- *22.11.* JEE 1985 — **Conditional probability:** max ≤ 10, given min = 5 → $1/19$. **Ch. 2 Symmetry / Ch. 9 DOF candidate.**
- *22.13.* JEE 1986 — Pass tests I, II, III with $p, q, 1/2$; success condition. **Ch. 9 DOF Analysis.**
- *22.14.* JEE 1999 — Pass M, P, C: $P(\ge 1) = 0.75$, $P(\ge 2) = 0.5$, $P(=2) = 0.4$ → $p+m+c = ?$ Inclusion-exclusion.
- *22.16(b).* JEE 1997 — $p, q$ random from $\{1..10\}$, $x^2 + px + q = 0$ has real roots → counting. **Ch. 9 DOF Analysis.**
- *22.18.* JEE 2001 — **Pólya urn:** $m$W + $n$B, draw + replace with $k$ extra same-colour → second draw $P(W) = m/(m+n)$ (surprise: same as first!). **Ch. 1 Invariance canonical. Beautiful gem.**
- *22.19.* JEE 2002 — Bayes: $N$ coins ($m$ fair + biased), 1 toss H, 2nd toss T → $P(\text{fair})$.
- *22.20.* Probability of no 3 consecutive heads in $n$ tosses: $(3/4)^{n+1}(2 + \alpha^{n+1} + \beta^{n+1})$ where $\alpha, \beta$ roots of $3x^2 + 2x + 1 = 0$. **Ch. 8 Telescoping / Ch. 11 Polynomial Identities / Linear recurrence canonical.**
- *22.21.* JEE 1988 — Two-urn ball-swap problem.
- *22.22.* JEE 1998 — Faulty machines: 2 of 4 tested. $P(\text{only 2 tests needed}) = 1/6$.
- *22.23.* **Birthday paradox** — 100 in queue; person most likely to get free ticket = ?

**Joshi's pedagogical observations.**
- "The uncertainties of life (the only certain thing about which is death) make probability a fascinating subject even for a layman." — voice sample.
- "If you have clear thinking, [probability problems] are quick scoring questions as the other computational work is often minor." — **Pillar 5 voice. Probability rewards conceptual clarity over computational sweat.**

**Pillar 2 routing.** *Primary:* **Ch. 3 Symmetry/Combinatorics** (Ex. 22.8(a-b), 22.9(b-c), 22.11 — counting under constraints); **Ch. 9 DOF Analysis** (Ex. 22.4, 22.13, 22.16(b) — what data uniquely determines the answer); **Ch. 1 Invariance** (Ex. 22.18 Pólya urn — first/second draw same!). *Secondary:* Ch. 8 Telescoping (Ex. 22.20 recurrence); Ch. 11 Polynomial Identities (Ex. 22.20 characteristic equation); Ch. 6 Duality (Ex. 22.9(c) coupons via complement); Ch. 10 Inequality (Ex. 22.6(b) probability bounds). **Joshi-rich; primary Pólya-style Ch. 1 source.**
<!-- CH22_END -->

<!-- CH23_BEGIN -->
### Chapter 23: Infinitistic Probability (pp. 744–775; lines 39933–41675)

**Topic summary.** Probability when sample space is infinite. Infinite sequences of trials. Geometric/binomial series in probability. Expected value. Ruin game. Continuous probability (interval sample spaces) — briefly. **Joshi: "Problems of infinitistic probability are asked very rarely in the JEE. Still, they are a natural sequel to finitistic probability and well deserve at least a cursory look."**

**Main Problem.** *JEE 1998. Three players $A$, $B$, $C$ toss coin cyclically until head shows; head-prob $0.4$. $P(B\text{ wins})$.* **Answer: $15/49$.** **Technique:** Mutual exclusivity + exhaustivity ($P(\text{no head ever}) = \lim (0.6)^n = 0$); set $\beta = (0.6)\alpha$, $\gamma = (0.36)\alpha$; solve $\alpha + \beta + \gamma = 1$ → $\alpha = 25/49$, $\beta = 15/49$. **Beautiful self-similar argument: after first tail, "same game restarts."**

**Key formulas/theorems established.**
- Self-similarity in geometric sequences of trials.
- Geometric series: $\sum_{n=0}^\infty r^n = 1/(1-r)$ for $|r| < 1$.
- Binomial theorem for negative exponent: $(1-x)^{-n} = \sum \binom{n+r-1}{r}x^r$.
- Expected value $E(X) = \sum xP(X=x)$.
- **Probability paradoxes:** continuous-uniform distribution → $P(x = y) = 0$ for two random reals on $[a, b]$ despite $x = y$ being logically possible.
- Power series and analytic identities (Euler's $\zeta(2)$).

**Comments highlights (~10 total).**
- *Comments 1–2.* Main problem; rigorous treatment of infinite sample space.
- *Comment 3.* Alternative solution via infinite series.
- *Comments 4–6.* Generating functions and probabilities.
- *Comment 7.* Expected value.
- *Comments 8–9.* Ruin game (gambler with finite bankroll).
- *Comment 10.* Continuous probability (uniform on interval).

**Exercises (notable — competition-sourced).**
- *23.1.* JEE 1993 — $x = \sum \cos^{2n}\phi$, $y = \sum\sin^{2n}\phi$, $z = \sum\cos^{2n}\phi\sin^{2n}\phi$ → **$xyz = xy + z$** (closed-form geometric series).
- *23.2.* JEE 1983 — **$2.\overline{357}$ as rational** = $2355/999$. Classical geometric-series problem. **Ch. 8 Telescoping candidate.**
- *23.3.* **Clock hands coinciding** between 4–5 pm. Two methods: arithmetic (one equation) AND infinite series (geometric sum). **Ch. 20 Analogy gem.**
- *23.4.* **Fly between two mathematicians** (von Neumann anecdote!). Distance covered before they meet — done via geometric series. **Ch. 8 Telescoping + Ch. 20 Analogy canonical.**
- *23.5.* Same problem by plain arithmetic. **Joshi quotes the famous von Neumann story:** "But that's exactly the way I did it." **Pillar 5 voice / Pillar 2 Ch. 20 Analogy quotable.**
- *23.6.* Generating function for selections with repetition.
- *23.7.* $(1-x)^{-n}$ via generating function → combinatorial identity.
- *23.10.* **Three combinatorial identities** via generating functions (one previously proved by binomial method in Ch. 5). **Ch. 20 Analogy candidate — same identity by two methods.**
- *23.11(a).* **Average number of elements in random subset of $S$ with $n$ elements:** $n/2$. **Ch. 1 Invariance candidate (linearity of expectation).**
- *23.11(b).* **Average minimum element of $r$-subset of $\{1, \ldots, n\}$:** $(n+1)/(r+1)$ (Tomescu). **Ch. 2 Symmetry candidate.**
- *23.12.* Average draws to first ace (with replacement: $13$; without: $53/5$). **Ch. 9 DOF.**
- *23.13.* Average reward = $n^2(n+1)^2/[2(n^2+1)(n^2+2)]$.
- *23.14.* Recurrence for expected number of tests (faulty machines).
- *23.15(a).* **Zero-sum game** in Main Problem; expected gains sum to 0.
- *23.16.* **Continuous probability:** phone busy probability via uniform distribution on $[0, 30]$.
- *23.17.* **For two random reals on interval, $P(x = y) = 0$, $P(x < y) = P(x > y) = 1/2$.** "Equality is an accident."
- *23.18.* **For two random lines in plane, $P(\text{parallel}) = 0$.** Concurrency of three random lines $= 0$. **Connects to Ex. 21.23 perturbation (Ch. 21). Ch. 9 DOF Analysis canonical.**
- *23.19.* **Euler's "proof" of $\zeta(2) = \pi^2/6$** via power series. Joshi: "An assumption like this is, of course, unwarranted and can lead to disasters. But Euler made it anyway and 'proved' this beautiful result. A logically rigorous proof can be given using theorems about what are called Fourier series. But that is beyond our scope." **Pillar 5 voice + Ch. 11 Polynomial Identities + Ch. 20 Analogy gem.**

**Joshi's pedagogical observations.**
- Comment 2 on Main Problem: rigorous infinitistic probability requires measure theory; weight-function paradoxes (every individual real number has zero length but interval has positive length).
- "It is in this sense that equality of two real numbers is an accident while their inequality is a rule" (Ex. 23.17) — **probabilistic continuity intuition. Pillar 2 Ch. 9 DOF Analysis quotable.**
- Joshi's celebration of Euler's bold ζ(2) "proof": rigour vs creativity tension. **Pillar 5 voice.**

**Pillar 2 routing.** *Primary:* **Ch. 8 Telescoping/Series** (Main Problem, Ex. 23.2, 23.3, 23.4, 23.19 — geometric-series mastery); **Ch. 20 Analogy** (Ex. 23.3, 23.4, 23.10, 23.19 — multiple-route to same answer). *Secondary:* Ch. 1 Invariance (Main Problem self-similarity, Ex. 23.11(a) linearity of expectation); Ch. 9 DOF Analysis (Ex. 23.18 generic position, 23.17 equality as accident); Ch. 2 Symmetry (Ex. 23.11(b) minimum of subset); Ch. 11 Polynomial Identities (Ex. 23.7, 23.19). **Joshi-rich; primary Ch. 8 Telescoping source (after Ch. 5).**
<!-- CH23_END -->

<!-- CH24_BEGIN -->
### Chapter 24: Miscellaneous Tips and Review (pp. 776–end; lines 41676–47704)

**Topic summary.** Joshi's meta-pedagogical synthesis chapter. The 100 exercises (24.1 to 24.100) constitute the single richest source of RMO/INMO/IMO-shortlist problems in the book. Joshi explicitly states his own framework for problem-solving strategy, which aligns closely with the Advaitian six-point structure. **Mandatory reading before drafting any Pillar 2 chapter.**

**Exercises (100 total — full inventory).** Full statements with answers are in `joshi-problems-locked.md` Appendix A. Routing summary:

| # | Gist | Routed Pillar 2 chapter |
|---|---|---|
| 24.1 | Domain of $f_1+f_2$ (JEE 1988) | Ch. 9 WE1 |
| 24.2 | Repeated root → derivative (JEE 1983) | Ch. 4 WE1 |
| 24.3 | $f(x)=x^2$ inj/surj (JEE 1979) | (omit) |
| 24.4 | Linear ODE characteristic polynomial | Ch. 6 candidate |
| 24.5 | Angle bisector ratio (JEE 1979) | (omit) |
| 24.6 | Perpendicular concurrence (inner JEE 1978) | Ch. 2 stretch |
| 24.7 | Cyclic quadrilateral inscribed-circumscribed (JEE 1978) | Ch. 3 WE2 |
| 24.8 | Dance-party (Putnam) | Ch. 13 WE1 |
| 24.9 | 11 stones equal mass | Ch. 17 WE1 |
| 24.10 | Fibonacci matrix $A^n$ | Ch. 18 WE1 |
| 24.11 | $\subseteq$ partial order on $\mathbb{C}$ | Ch. 3 PP1 |
| 24.12 | Ellipse-from-foci convexity | Ch. 8 PP1 |
| 24.13 | $\alpha^3-3\alpha^2+5\alpha=17, \beta=-11$ (RMO) | **Ch. 1 PP5 (used)** |
| 24.14 | $\cos 2\theta + a\cos\theta + b\sin\theta + c = 0$ | Ch. 2/1 stretch |
| 24.15 | Double-sum order-swap | Ch. 18 stretch |
| 24.16 | Sun-shadow work-rate | Ch. 5 WE1 |
| 24.17 | $(1+b^2)x^2 + 2bx + 1$ min range (JEE 2001) | Ch. 10 PP2 |
| 24.18 | Centroid locus $\triangle PAB$ (JEE 2001) | Ch. 8 PP2 |
| 24.19 | 5th + 6th binomial term = 0 (JEE 2001) | Ch. 15 stretch |
| 24.20 | $T_n$ triangles, $T_{n+1}-T_n=21$ (JEE 2001) | Ch. 9 WE2 / Ch. 13 PP2 |
| 24.21 | Onto $\{1,2,3,4\} \to \{1,2\}$ (JEE 2001) | Ch. 13 WE3 |
| 24.22 | $a,b,c,d$ AP, $abc,abd,acd,bcd$ form (JEE 2001) | Ch. 18 stretch |
| 24.23 | AP sum-equal (JEE 2001) | Ch. 18 stretch |
| 24.24 | $n$-th roots of unity right angle (JEE 2001) | Ch. 2 PP1 |
| 24.25 | $z$-ratio = $(1-i\sqrt 3)/2$ triangle (JEE 2001) | Ch. 8 WE1 |
| 24.26 | $\sin^{-1}+\cos^{-1}$ geometric series (JEE 2001) | Ch. 5 PP3 |
| 24.27 | Max $\prod\cos\alpha_i$ under $\prod\cot\alpha_i=1$ (JEE 2001) | Ch. 10 PP3 |
| 24.28 | $\alpha+\beta=\pi/2, \beta+\gamma=\alpha$ (JEE 2001) | Ch. 5 stretch |
| 24.29 | Tower angles of depression (JEE 2001) | (omit — applied) |
| 24.30 | Integer $m$ for integer intersection (JEE 2001) | Ch. 9 PP1 / Ch. 14 stretch |
| 24.31 | Parabola directrix (JEE 2001) | (omit) |
| 24.32 | $PQ, RS$ tangents, $2r = ?$ (JEE 2001) | Ch. 12 stretch |
| 24.33 | Parallelogram area (JEE 2001) | Ch. 7 stretch |
| 24.34 | Common tangent circle-parabola (JEE 2001) | Ch. 19 WE1 |
| 24.35 | Tangent-triangle area = 2 (JEE 2001) | Ch. 6 WE1 |
| 24.36 | $f(x)=x+1/x$ inverse (JEE 2001) | Ch. 5 PP1 / Ch. 19 PP1 |
| 24.37 | $g(x)=1+x-[x], f(g)$ (JEE 2001) | Ch. 11 stretch |
| 24.38 | $\lim\sin(\pi\cos^2 x)/x^2$ (JEE 2001) | Ch. 6 PP1 |
| 24.39 | Left derivative $[x]\sin\pi x$ at integer (JEE 2001) | Ch. 11 PP2 |
| 24.40 | $F(x^2)=x^2(1+x)$ (JEE 2001) | Ch. 5 PP2 / Ch. 19 PP2 |
| 24.41 | $\max\{x,x^3\}$ non-diff (JEE 2001) | Ch. 11 PP1 |
| 24.42 | $xe^{x(1-x)}$ monotonicity (JEE 2001) | Ch. 12 PP1 |
| 24.43 | $\int\cos^2x/(1+a^x)$ symmetric (JEE 2001) | Ch. 2 PP3 |
| 24.44 | $\cos|x|\pm|x|$ diff at 0 (JEE 2001) | Ch. 6 PP2 |
| 24.45 | $\log_4(x-1)=\log_2(x-3)$ (JEE 2001) | Ch. 11 PP3 |
| 24.46 | $f(x)=\alpha x/(x+1), f\circ f=\mathrm{id}$ (JEE 2001) | Ch. 3 PP2 |
| 24.47 | Vector triple product dependence (JEE 2001) | Ch. 8 WE2 |
| 24.48 | $H_n - \ln n$ bounded | Ch. 6 WE2 |
| 24.49 | $(2m)!(2n)!/(m+n)!$ integer | Ch. 14 WE1 |
| 24.50 | Three unit vectors $|\vec a-\vec b|^2$ sum ≤ 9 | Ch. 10 PP1 |
| 24.51 | 3 numbers $\{1..p\}$ sum $2p$ prob | Ch. 13 PP1 |
| 24.52 | India 2 matches WI 2 matches Aus (JEE 1992) | Ch. 13 stretch |
| 24.53 | 16-player tournament (JEE 1997†) | Ch. 13 PP3 |
| 24.54 | Event $E$ ≥ 3 times (JEE 1993) | Ch. 13 PP7 |
| 24.55 | A wins 3 of 5 | Ch. 13 stretch |
| 24.56 | Two queens non-taking | Ch. 13 PP4 |
| 24.57 | Alt solution Ch. 5 Comment 17 | Ch. 15 PP2 |
| 24.58 | AD bisector, ∠A=72° (RMO) | Ch. 2/11 stretch |
| 24.59 | $BE, CF$ altitudes, $FM\parallel EN$ (RMO) | Ch. 2 PP2 |
| 24.60 | Perpendiculars concurrent (outer) (RMO) | **Ch. 2 PP6 (used)** |
| 24.61 | Isosceles 120° → PQR equilateral (RMO) | Ch. 2 stretch |
| 24.62 | 1000-evens vs 1000-odds mod 2001 (RMO) | **Ch. 1 PP4 (used)** |
| 24.63 | $\lfloor x/99\rfloor = \lfloor x/101\rfloor$ (RMO) | Ch. 14 PP2 |
| 24.64 | $x^2/z < (x^2+y^2+z^2)/(x+y+z) < z^2/x$ (JEE 1972) | Ch. 10 WE2 |
| 24.65 | $|x^2(y-z)+\ldots| < xyz$ triangle (RMO) | Ch. 10 WE1 |
| 24.66 | $abc=1$ inequalities (INMO+IMO 2000) | **Ch. 2 PP7 + Ch. 10 WE3 (used)** |
| 24.67 | Symmetric matrix odd $n$ (RMO) | **Ch. 2 WE3 (used)** |
| 24.68 | $x^4-2ax^2+x+a^2-a=0$ all real (RMO) | Ch. 16 WE1 |
| 24.69 | $f(x+y)=f(x)f(y)f(xy)$ (INMO) | **Ch. 1 PP7 (used)** |
| 24.70 | $\sum A_i/(x-a_i)=0$ real | Ch. 11 WE1 |
| 24.71 | Triangle cosine determinant = 0 | Ch. 1/17 stretch |
| 24.72 | Consecutive-int sides, $r=4$, find $R$ (RMO) | Ch. 9 PP2 |
| 24.73 | 50-subset of {1..100} (RMO) | Ch. 13 PP6 |
| 24.74 | Convex quad area 32, side+diag=16 (K.N. Ranganathan) | Ch. 12 PP2 |
| 24.75 | 1000 doors | **Ch. 1 PP6 (used)** |
| 24.76 | Squarefree + integer-triangle perimeter | Ch. 14 PP4 |
| 24.77 | Cakes clockwise (Josephus) | Ch. 12 WE2 |
| 24.78 | $m\times n$ diagonal squares $=m+n-\gcd$ | Ch. 14 PP3 |
| 24.79 | Wallace-Bolyai-Gerwien equidecomposability | Ch. 20 WE1 |
| 24.80 | Surjective functions: 2 formulas | Ch. 13 WE2 / Ch. 15 WE1 |
| 24.81 | Hamiltonian cycle $m\times n$ mesh | Ch. 14 PP5 |
| 24.82 | Digital sum (XOR) | Ch. 14 WE2 |
| 24.83 | Nim games | Ch. 14 PP7 |
| 24.84 | Descartes' circle theorem | Ch. 2/20 stretch |
| 24.85 | Max cyclic $\sin x_i \cos x_{i+1}$ | Ch. 2 PP5 |
| 24.86 | Box white/black/red, red last | Ch. 13 PP5 |
| 24.87 | $\sum \cot^{-1}(2k^2)$ telescoping | Ch. 18 PP1 |
| 24.88 | Right triangle $R \ge (1+\sqrt 2)r$ | Ch. 10 PP4 |
| 24.89 | $f(0), f(-1)$ odd → no integer root | Ch. 14 WE3 |
| 24.90 | $(\tan^2\theta+1)^2 + \cdots = 0$ four roots | Ch. 5/9 stretch |
| 24.91 | Min of quadratic forms | Ch. 12 PP3 |
| 24.92 | Convex polygon vertex/non-vertex (LP germ) | Ch. 12 WE1 / Ch. 3 candidate |
| 24.93 | Ravi substitution + Hadwiger-Finsler | Ch. 5 WE2 / Ch. 10 PP5 |
| 24.94 | $abc=4Rrs$; triangle uniqueness | Ch. 1/17 stretch |
| 24.95 | $\cot\theta_1 + \cot\theta_2$ min at $\theta/2$ | Ch. 2 PP4 / Ch. 10 PP7 |
| 24.96 | Pedoe's inequality (2 triangles) | Ch. 10 PP6 |
| 24.97 | $f''+gf'-f=0$, $f(a)=f(b)=0$ → $f\equiv 0$ | Ch. 11 WE2 |
| 24.98 | Plane isometries classification | Ch. 2/20 stretch |
| 24.99 | 3-digit=2×sum-of-squares; leading $2^n, 5^n$ | Ch. 4 WE2/PP1 |
| 24.100 | Wilson primes $(p-1)!+1$ | Ch. 14 PP1 |

**Joshi's strategy framework (Ch 24 opening Comments — voice samples for Pillar 3).** Joshi articulates a problem-solving strategy framework that aligns *remarkably* with the Advaitian six-point structure:
1. *Read the problem carefully* — what is given, what is asked.
2. *Identify the type* — classification by topic / technique.
3. *Recall related problems* — analogy as discovery engine.
4. *Try a special case* — does the structure simplify?
5. *Look for a pattern / invariant.*
6. *Translate to a different form.*
7. *Verify the answer by an alternate method.*

**Mandatory reading before any Pillar 2 chapter draft** — to align voice register with Joshi's meta-commentary style.
<!-- CH24_END -->

---

## III. Master Index by Competition

*Quick-lookup index of competition-sourced problems by exam. Use this to verify problem provenance when drafting Pillar 2 chapters. Numbers refer to Joshi's Chapter.Exercise (e.g., **17.30** = Joshi Chapter 17, Exercise 30) or Joshi's Chapter.Comment (e.g., **3.C12** = Chapter 3 Comment 12).*

### JEE (Joint Entrance Examination — IIT) by year

- **1978.** 3.7(b), 3.8(d), 22.1, 22.6(a), 15.13(d) — Various.
- **1979.** 1.4 ("+/−"), 1.C2 (52 cards), 1.C4 (6B+6G), 2.1 (polygon AP), 2.4 (HM/G/A), 3.7(a), 3.10(d), 3.11, 3.18(b), 14.4 (triangle ineq.), 17.3(i) JAT (only-x²+y²=1), 20.9 (sin+cos)/√2.
- **1980.** 1.C5 (m men+n women), 2.1 (polygon AP), 2.5 (GP), 3.11, 4.C, 5.C, 13.6 (JAT cubic), 14.5, 15.5(a), 15.14(d), 17.3(ii) (parabola+line, JAT), 22.4(a), 22.7.
- **1981.** 1.C3 (5 balls/3 boxes), 1.C12 (12 coins), 2.28, 2.29, 3.8, 13.17 (e^π vs π^e), 15.3, 16.16, 17.16(a), 21.2(b) JAT, 21.5(b), 22.10, 22.5.
- **1982.** 2.2 (telescoping AP), 2.5, 2.29, 13.20 (parabola distance), 15.14(d), 16.15, 18.10 (King's prop), 20.19(a), 21.6 (rotation), 21.29 (eigenvalues).
- **1983.** 1.4 (six +'s, four −'s), 1.C5, 2.6 (in (2,18)), 3.10(a), 3.18(a), 3.21(a), 4.C, 5.C, 13.14, 13.18, 14.2, 15.1, 15.2, 15.13(c), 15.21(c), 17.3(iii) (x²=4y, x=4y−2), 17.4, 21.1(c), 21.2(b-d), 22.6(b), 22.8(a) ASSASSIN, 22.9(c) coupons, 23.2 (recurring decimal).
- **1984.** 1.C, 3.1, 6.C (AM-GM), 13.5, 14.1 (a,b,c triangle), 15.6(c), 15.8 (x+|y|=2y), 15.11(a), 16.21, 17.3(v) (tan/cot), 17.29(i), 22.9(a), 20.13.
- **1985.** 2.13, 3.13, 14.3, 15.11(b), 15.11(d), 15.21(a), 17.3(vi) (√(5−x²), |x−1|), 17.27(iii), 18.15(i-ii), 21.3(b), 21.7(d), 22.11.
- **1986.** 3.10(e) (a+b=−1), 6.C, 11.C, 14.1, 14.C, 15.3, 15.22(b), 17.3(vii) (x²+y²=4, x²=−√2y, x=y), 18.15(xi), 21.6, 22.5, 22.13, 22.16(a).
- **1987.** 13.7 (parallelogram), 13.9, 13.16, 15.20, 15.22(a), 15.22(c), 17.3(viii), 21.1(a), 22.4(b).
- **1988.** 1.4 (six "+", four "−"), 1.C, 2.22, 2.27, 3.7(b), 4.C, 11.C, 13.19, 15.10, 16.10, 17.16(a), 17.3(ix), 21.8 (reciprocal basis), 21.17, 22.4(c), 22.6(b), 22.21.
- **1989.** 2.3(b), 2.3(c), 12.C, 14.C, 15.12(a), 15.13, 15.15(i), 15.16(d), 15.23(a), 17.3(x), 17.29(ii), 18.14, 21.20, 22.4(e).
- **1990.** 12.C, 13.4, 13.11, 13.16, 14.C, 17.7 (Dirichlet kernel), 17.17(a), 17.20, 18.6(e), 19.1, 20.6 Jensen (1995 actually), 22.6, 22.7.
- **1991.** (sparse year in Joshi).
- **1992.** 2.13, 11.2 (three touching circles), 14.C, 15.4, 15.23(b), 17.3(xii), 18.3 (eˣ(x−1)ⁿ).
- **1993.** 12.5, 13.10, 14.C, 15.7(c), 15.21(a-ii), 15.26, 17.3(xiii), 17.29(iii), 18.13, 18.15(iii-iv), 21.13(b), 22.4(d), 22.9(b), 23.1 (cos²ⁿφ identity).
- **1994.** 1.C, 12.C, 15.6(c), 15.16(f), 17.4 (main problem — 121/4), 17.15, 18.11, 19.11(a) (normal of constant length).
- **1995.** 13.3(a), 17.3(xi), 18.15(xiv), 19.8 (curve area 2), 20.6 (Jensen's), 21.5(c) (a×(a×c)+b=0).
- **1996.** 13.18, 14.C, 15.7(b), 15.16, 15.22(d), 19.9 (curve through (1,1)), 21.5(d), 21.10, 21.14 (tetrahedron).
- **1997.** 3.6 (A=3, B=77), 5.4 (sum to 32 — Ch. 5 main), 5.C, 13.4 (inscribed triangle), 13.15 (x/sin x), 14.C, 17.9(c)-(d), 17.16(b), 17.21, 17.30 (F(k)−F(1)), 18.15(v-vii), 19.1 (raindrop), 19.7 (Sturm), 22.16(b).
- **1997*.** 1.1, 2.10, 11.C, 13.10, 14.C, 15.11(e), 15.21(a-iii), 17.2 (incircle), 17.3(xiv) (max of three), 21.1(d) (quadrilateral), 21.4 (Gram matrix), 21.5(c), 22.13, 22.22 (faulty machines).
- **1998.** 11.C, 13.12, 14.18 (Erdős-Mordell), 15.13(c), 16.6, 17.3(xv) (x²+y²=25), 17.22(a), 17.23 (determinant + min), 18.10, 18.15(vii-ix), 19.7 (Sturm), 20.11, 21.12(b), 22.8(b), 22.22 (faulty machines), 23.M (Main, 3 players cyclic).
- **1999.** 12.C, 13.21 (ellipse), 13.23 (two parabolas closest), 14.C, 15.22(h-j), 15.23(a), 17.5 (m for area 9/2), 17.29(iv), 18.15(v-vi, x), 19.2 ((y')²−xy'+y=0), 19.10 (curve, normal distance), 19.12 (order/degree y²=2c(x+c)), 21.5(f), 21.13(a), 22.14 (m, p, c).
- **2000.** 2.3(d), 13.23 (closest on two parabolas), 15.11(c), 17.9(c) JEE 1997, 18.9 (∫ln t/(1+t)).
- **2001.** 13.10, 14.C, 17.8(a) (xeᵃʸ=sin by), 18.15(ix), 21.4 (Gram matrix), 21.19 (angular bisectors), 21.29 (eigenvalues 1982), 22.18 (Pólya urn).
- **2002.** 5.4 (10 elements of $E_1, E_2$, see Ch. 5 main), 13.3(b), 15.6(d), 15.9 (g(x) reflection), 15.16(g), 15.22(i), 16.6, 17.3(xv), 17.22(b), 18.7 (∫f(2x) from 3 to 3+3T), 18.15(ix), 20.6 (Jensen), 21.2(g) (max ScTrPdc), 22.16(b), 22.19 (Bayes fair/biased).

### JAT (Joint Admission Test — IIT predecessor)

- **1979.** 13.2 (window), 15.17 ($\delta$-$\varepsilon$ for $x^3$), 15.19 (Dirichlet discontinuous), 18.16 (∫ln sin x), 18.17 (Stirling), 19.4 (carbon dating, conceptual), 21.2(b) (X·A=X·B=X·C=0 box product), 21.7(a) (C=A×B, B=A×C ⇒ both zero), 21.15.
- **1980.** 6.49, 13.2 (JEE 1995 derivative), 14.C, 15.6(a), 15.16(b), 15.17, 15.21(b), 16.14 (arctan vs x), 16.27 (3sin x + tan x vs 4x), 17.3(ii) (parabola+line), 19.18, 21.2(b), 21.16, 21.28.

### Other Competitions (RMO, INMO, IMO, Putnam)

- **IMO 1961.** $a^2 + b^2 + c^2 \ge 4\sqrt 3 \Delta$ — Ch. 14, Ex. 14.11.
- **Various RMO/INMO** — see Joshi Chapter 24 (100 selected problems), particularly:
  - 24.65 (a+b+c=0 identity, triangle inequality, Ravi substitution).
  - 24.74 (cyclic quadrilateral area).
  - 24.77 (Josephus-like, attributed to JEE/RMO).
  - 100-problem compendium in Joshi Ch. 24 is **the** primary cross-archetype source.
- **Tomescu (Romanian olympiad author).** Ch. 23, Ex. 23.11(b) — average minimum element of $r$-subset.
- **Putnam-style.** Many of Joshi's "starred" exercises (denoted with * in Joshi) are sourced from Putnam, AMC, or USAMO archives.

---

## IV. Master Index by Pillar 2 Archetype

*Bidirectional lookup: archetype → Joshi sources. Use when seeding a Pillar 2 chapter. Each archetype lists primary Joshi chapters (Joshi-rich) and secondary chapters (where archetype appears as supporting technique). Update each row when its Pillar 2 chapter is drafted.*

| # | Archetype Name | Joshi PRIMARY chapters | Joshi SECONDARY chapters | Status |
|---|---|---|---|---|
| **1** | **Invariance** | Ch. 1 (counting), Ch. 3 (Vieta's), Ch. 7 (sin²+cos²=1), Ch. 11 (sine/cosine rules), Ch. 17 (parametrisation), Ch. 19 (energy conservation), Ch. 22 (Pólya urn — linearity of expectation) | Ch. 2 (Argand), Ch. 8 (Klein invariants), Ch. 16 (energy), Ch. 18 (King's prop), Ch. 21 (rotation), Ch. 23 (stationary distributions) | ✅ **Drafted (01-invariance.md)** |
| **2** | **Symmetry** | Ch. 2 (symmetric polynomials), Ch. 3 (Vieta's), Ch. 7 (sum-to-product), Ch. 14 (smoothing lemma), Ch. 18 (King's property) | Ch. 1, Ch. 8, Ch. 11 (cyclic identities), Ch. 17, Ch. 22 | 📝 **Outline only (02-symmetry-outline.md)** |
| **3** | **Combinatorics / Bijection** | Ch. 1 (André reflection), Ch. 5 (Vandermonde, Pascal), Ch. 22 (counting cases) | Ch. 4 (Lucas), Ch. 8, Ch. 23 (generating functions) | ⏳ Pending |
| **4** | **Modular Periodicity** | Ch. 4 (modular arithmetic), Ch. 18 (periodic functions, $f(x+T)=f(x)$) | Ch. 7 (trig periods), Ch. 20 (period determination), Ch. 17 (∫|sin x|), Ch. 22 (Bayes/coupon) | ⏳ Pending |
| **5** | **Substitution / Change of Variable** | Ch. 5 (binomial identities), Ch. 9 (translation), Ch. 14 (Ravi), Ch. 15 (parametric diff), Ch. 17 (u-sub), Ch. 19 (homog/Bernoulli), Ch. 20 (log conjugation) | Ch. 2 (Weierstrass for trig), Ch. 13 (parametric optim), Ch. 16, Ch. 18 (King's), Ch. 21 | ⏳ Pending |
| **6** | **Duality** | Ch. 8 (pole-polar), Ch. 11 (in/circumradius), Ch. 21 (reciprocal basis), Ch. 6 (inequality dualization) | Ch. 9 (geometric reflection), Ch. 15 (tangent/normal pairs), Ch. 17, Ch. 22 (complement) | ⏳ Pending |
| **7** | **Trigonometric Substitution** | Ch. 7 (identities), Ch. 14 (cyclotomic), Ch. 10 (trig eqs), Ch. 17 (∫sec³, etc.) | Ch. 5, Ch. 9 (ellipse $x=a\cos\theta$), Ch. 13 | ⏳ Pending |
| **8** | **Telescoping / Reduction** | Ch. 5 (binomial sums), Ch. 8 (geometric), Ch. 18 (reduction formulas), Ch. 23 (Σ geometric series) | Ch. 2 (Σi²), Ch. 7 (sum-to-product), Ch. 22 (recurrence) | ⏳ Pending |
| **9** | **DOF Analysis** | Ch. 17 (DOF in integrals/areas), Ch. 19 (data sufficiency in ODEs), Ch. 21 (perturbation), Ch. 22 (random/event counting) | Ch. 3 (root counting), Ch. 15 (continuity), Ch. 23 (general position) | ⏳ Pending |
| **10** | **Inequality** | Ch. 6 (AM-GM, Cauchy-Schwarz), Ch. 10 (constrained trig), Ch. 13 (Jensen's via calculus), Ch. 14 (Erdős-Mordell, triangular) | Ch. 11 (triangle ineq), Ch. 16 (MVT), Ch. 17 (Σ√k bounds), Ch. 18, Ch. 23 | ⏳ Pending |
| **11** | **Polynomial Identities** | Ch. 3 (Newton's), Ch. 5 (binomial), Ch. 16 (Rolle's iteration on derivatives) | Ch. 2, Ch. 11, Ch. 18 (Ex. 18.19), Ch. 21 (eigenvalues), Ch. 23 (Euler ζ(2)) | ⏳ Pending |
| **12** | **Extremal Optimisation** | Ch. 13 (entire chapter), Ch. 14 (triangular optim), Ch. 17 (area extremes) | Ch. 6, Ch. 10 (extremal trig), Ch. 16 (Snell), Ch. 18 (Ex. 18.3) | ⏳ Pending |
| **13** | **Asymptotic / Approximation** | Ch. 6 (limits, order of magnitude), Ch. 15 (L'Hôpital), Ch. 16 (Taylor's, error est.), Ch. 18 (Stirling, Wallis), Ch. 19 (70% rule, decay) | Ch. 7 (small-angle), Ch. 17 (Riemann-sum limits), Ch. 23 (Euler ζ(2)) | ⏳ Pending |
| **14** | **Counterexample Construction** | Ch. 4 (number theory CEX), Ch. 15 (Dirichlet), Ch. 16 (MVT failures), Ch. 20 (pathological Cauchy) | Ch. 3 (root counting fail), Ch. 9 (locus fail), Ch. 22, Ch. 23 (P(parallel)=0) | ⏳ Pending |
| **15** | **Geometric Pivot** | Ch. 8 (Euclidean), Ch. 9 (coord geom), Ch. 11 (triangle solutions), Ch. 21 (vector geom) | Ch. 7, Ch. 12 (heights/dist), Ch. 13 (loci), Ch. 17 (areas) | ⏳ Pending |
| **16** | **Reverse Engineering** | Ch. 3 (root reconstruction), Ch. 19 (ODE from data), Ch. 20 (functional eq), Ch. 17 (Ex. 17.22, 17.23) | Ch. 4 (problem inversion), Ch. 21 (Gram matrix → vectors) | ⏳ Pending |
| **17** | **DOF Analysis (advanced)** | Ch. 9 (degree of freedom), Ch. 13 (parameter dependence), Ch. 21 (cancellation laws) | Ch. 16 (Existence-uniqueness), Ch. 22 (independence), Ch. 23 | ⏳ Pending |
| **18** | **Recursion / Generating Function** | Ch. 4 (Fibonacci, Euler totient), Ch. 5 (Pascal), Ch. 22 (recurrence in prob), Ch. 23 (GFs) | Ch. 2 (Gauss binomial), Ch. 18 (reduction = recursion), Ch. 19 (recursive ODEs) | ⏳ Pending |
| **19** | **Pivoting / Strategic Choice** | Ch. 2 (change of basis), Ch. 9 (rotation/translation), Ch. 11 (technique selection) | Ch. 21 (basis change), Ch. 24 (meta-pedagogy) | ⏳ Pending |
| **20** | **Analogy / Transfer** | Ch. 17 (counting↔area), Ch. 18 (Ex. 18.19 integral↔identity), Ch. 20 (Comment 1 + Ex. 20.4-20.5, sin/cos system), Ch. 21 (quaternions↔complex), Ch. 23 (von Neumann fly) | Ch. 4, Ch. 5, Ch. 7 (Euler formula), Ch. 24 (meta) | ⏳ Pending |

**Routing legend.**
- ✅ Drafted: chapter exists in `pillar2-archetypes/` and is reviewed.
- 📝 Outline only: skeleton + draft in `pillar2-archetypes/_template/`.
- ⏳ Pending: routing identified but chapter not yet started.

**Cross-archetype Joshi exercises** (problems that illustrate multiple archetypes — useful for Ch. 20 Analogy chapter): 24.65 (Ravi sub + triangle ineq), 14.1 (smoothing + Ravi), 18.19 (integral + combinatorial identity), 21.25-27 (quaternions + four-square), 23.4 (von Neumann fly — geometric series + arithmetic).

---

## V. Joshi's Internal Cross-References

*Joshi explicitly cross-references chapters and exercises. This map captures the dependency structure of his book — useful when extracting problems that draw on multiple chapters.*

**Joshi → Joshi dependencies (selected, by chapter):**

- **Ch. 1 (Counting)** ← referenced by Ch. 17 Comment 1 (complementary counting ↔ complementary area), Ch. 22 (probability counting), Ch. 23 (generating functions).
- **Ch. 2 (Basic Algebra)** ← referenced by Ch. 6 (HM/AM/GM inequalities), Ch. 16 (real number system / completeness), Ch. 17 (Σk^p limits).
- **Ch. 3 (Theory of Equations)** ← referenced by Ch. 15 Comment 3 (3 normals on parabola via cubic discriminant), Ch. 16 (polynomial root counting via Rolle's).
- **Ch. 4 (Number Theory)** ← referenced by Ch. 5 (Lucas's via Kummer), Ch. 22 (Bayes/coupon).
- **Ch. 5 (Binomial Identities)** ← referenced by Ch. 11 (binomial expansion in geometry), Ch. 17 (Ex. 17.11), Ch. 23 (generating functions).
- **Ch. 6 (Inequalities)** ← referenced by Ch. 13 (Jensen's via calculus), Ch. 14 (triangular optim), Ch. 17 (Σ√k bounds), Ch. 18 (Stirling).
- **Ch. 7 (Trig Identities)** ← referenced by Ch. 10 (trig equations), Ch. 14 (constrained optimisation), Ch. 18 (King's prop applications).
- **Ch. 8 (Geometry)** ← referenced by Ch. 9 (coord geom), Ch. 11 (triangle solutions), Ch. 21 (vector geom).
- **Ch. 9 (Coord Geom)** ← referenced by Ch. 13 (loci), Ch. 17 (areas).
- **Ch. 10 (Trig Equations)** ← referenced by Ch. 11 (triangle solutions), Ch. 20 (period determination).
- **Ch. 11 (Solution of Triangles)** ← referenced by Ch. 14 (triangular optim).
- **Ch. 12 (Heights/Dist)** ← referenced by Ch. 14 (3D applications, sparingly).
- **Ch. 13 (Max/Min)** ← referenced by Ch. 14 (Jensen's), Ch. 15 Comment 3, Ch. 16 (n-th derivative test), Ch. 17 (area extremes), Ch. 19 (ODE-based optim).
- **Ch. 14 (Trig Optim)** ← referenced by Ch. 18 (King's), Ch. 23.
- **Ch. 15 (Limits)** ← referenced by Ch. 16 (theoretical foundations), Ch. 17 (Riemann sums as limits), Ch. 20 (functional equation methods).
- **Ch. 16 (Theoretical Calculus)** ← referenced by Ch. 19 (existence of solutions), Ch. 20 (continuous Cauchy equation).
- **Ch. 17 (Areas)** ← referenced by Ch. 18 (FTC reuse), Ch. 19 (volume by cross-section).
- **Ch. 18 (Definite Integrals)** ← referenced by Ch. 19 (ODE integration), Ch. 20.
- **Ch. 19 (ODEs)** ← referenced by Ch. 20 (functional → differential).
- **Ch. 20 (Functional Eqs)** ← referenced by Ch. 21 (vector identities), Ch. 22 (independence).
- **Ch. 21 (Vectors)** ← referenced by Ch. 22 (geometric probability), Ch. 23.
- **Ch. 22 (Finitistic Prob)** ← referenced by Ch. 23 (limiting case).
- **Ch. 23 (Infinitistic Prob)** ← references Ch. 21.23 (perturbation), Ch. 6.46 (rationals dense in reals).
- **Ch. 24 (Miscellaneous)** ← references **all** chapters (100-problem compendium).

**Notable cross-references in exercises (Joshi → Joshi):**

- Ex. 13.12 ↔ Ex. 24.65 (Ravi substitution).
- Ex. 13.23 (closest pair on parabolas) ↔ Ex. 18.M (beta function).
- Ex. 14.1 ↔ Ex. 24.65.
- Ex. 14.18 (Erdős-Mordell) — quoted in Ch. 24.
- Ex. 15.11(c) ↔ Ex. 16.18 (polynomial root counting).
- Ex. 17.9 (Riemann sums) ↔ Ex. 18.1 (limit of Σ as integral).
- Ex. 18.19 (integral combinatorial identity) ↔ Ex. 5.M (binomial main problem).
- Ex. 21.23 (perturbation/unstable property) ↔ Ex. 23.18 (P(parallel) = 0).
- Ex. 22.18 (Pólya urn) ↔ Ex. 23.M (self-similar three-player game).

**Forward references (Joshi pointers to later chapters):**

- Ch. 1 → Ch. 5 (binomial), Ch. 17 (combinatorial counting in integrals), Ch. 23 (generating functions).
- Ch. 13 → Ch. 14, Ch. 15 (continuity in extrema), Ch. 16 (Lagrange MVT proof of monotonicity), Ch. 19 (ODE-based modeling).
- Ch. 17 → Ch. 18 (FTC continuation), Ch. 19 (volume).
- Ch. 22 → Ch. 23.

---

## VI. Notable Theorems & Named Results

*Alphabetical index of named theorems and results in Joshi, with Joshi-location and Pillar 2 archetype routing.*

| Theorem / Result | Joshi Location | Pillar 2 Archetype Tag |
|---|---|---|
| **Abel-Galois Theorem** (insolvability of quintics) | Ch. 3 Comment 2 | Ch. 13 Asymptotic |
| **AM-GM Inequality** | Ch. 6 (Theorem 1), proved by induction; Ch. 13 (via Jensen's) | Ch. 10 |
| **AM-GM-HM compound** | Ch. 6, Ch. 2 | Ch. 10 |
| **André's Reflection Principle** (Catalan numbers) | Ch. 1 Comment 6 | Ch. 3 Combinatorics |
| **Argand Diagram** | Ch. 2 Comment 12 | Ch. 15 Geometric Pivot |
| **Bayes' Theorem** | Ch. 22 | Ch. 9 DOF Analysis |
| **Bernoulli's ODE** | Ch. 19 | Ch. 5 Substitution |
| **Beta Function** | Ch. 18 Main Problem | Ch. 2 Symmetry / Ch. 8 Telescoping |
| **Bezout's Lemma** (gcd as linear combination) | Ch. 4 Comment 4 | Ch. 18 Recursion |
| **Bijective Counting** (selections with repetition) | Ch. 1 Comment 5 | Ch. 3 |
| **Binomial Theorem** | Ch. 2, Ch. 5 | Ch. 18 Recursion / Ch. 3 |
| **Carbon Dating Formula** | Ch. 19 Ex. 19.4 | Ch. 13 Asymptotic |
| **Cauchy's Functional Equation** $f(x+y) = f(x) + f(y)$ | Ch. 20 Comment 3-4 | Ch. 16 Reverse Engineering |
| **Cauchy's Mean Value Theorem** | Ch. 16 | Ch. 11 Existence |
| **Cauchy-Schwarz Inequality** | Ch. 6 | Ch. 10 |
| **Cavalieri's Principle** (volume by cross-section) | Ch. 17 Ex. 17.13 | Ch. 20 Analogy |
| **Ceva's Theorem** | Ch. 11 | Ch. 6 Duality |
| **Chebyshev Polynomials** | Ch. 7 Comment 11 | Ch. 11 Polynomial |
| **Chinese Remainder Theorem** | Ch. 4 | Ch. 4 Modular |
| **Completeness of $\mathbb R$** | Ch. 16 Comment 1-2 | Ch. 14 Counterexample |
| **Complementary Counting** | Ch. 1 Comment 1 (motivated as area in Ch. 17 Comment 1) | Ch. 20 Analogy |
| **Cramer's Rule** | Ch. 3 Comment 17 | Ch. 11 Polynomial |
| **Cyclotomic Polynomials** | Ch. 7 | Ch. 11 |
| **De Moivre's Theorem** | Ch. 7 | Ch. 7 / Ch. 20 Analogy |
| **Dirichlet's Function** (discontinuous everywhere) | Ch. 15 Ex. 15.19 | Ch. 14 Counterexample |
| **Discriminant of Polynomial** | Ch. 3 Comment 4, Ex. 3.3 | Ch. 1 Invariance |
| **Erdős-Mordell Inequality** | Ch. 14 Ex. 14.18 | Ch. 10 Inequality |
| **Euler's Constant** (γ, $H_n - \ln n$) | Ch. 6 (Σ1/n diverges) | Ch. 13 Asymptotic |
| **Euler's Formula** $e^{i\theta}$ | Ch. 7, Ch. 17 Ex. 17.26 | Ch. 20 Analogy |
| **Euler's Identity** $e^{i\pi} + 1 = 0$ | Ch. 7 | Ch. 1 Invariance |
| **Euler's Solution to ζ(2) = π²/6** | Ch. 23 Ex. 23.19 | Ch. 11 / Ch. 20 |
| **Euler Line** (centroid, circumcentre, orthocentre) | Ch. 8 Comment 5 | Ch. 1 Invariance |
| **Euler Totient $\phi(n)$** | Ch. 4 | Ch. 4 / Ch. 18 |
| **Extreme Value Theorem (EVT)** | Ch. 16 | Ch. 11 Existence |
| **Fermat's Little Theorem** | Ch. 4 Comment 6 | Ch. 1 Invariance |
| **Fibonacci Numbers** | Ch. 4 | Ch. 18 Recursion |
| **Fixed-Point Theorem** (1D) | Ch. 16 Ex. 16.3 | Ch. 1 / Ch. 8 |
| **Fundamental Theorem of Algebra (FTA)** | Ch. 3 | Ch. 11 Existence |
| **Fundamental Theorem of Calculus (FTC)** | Ch. 17 Theorem 1, 2 | Ch. 20 Analogy |
| **Gauss's Constructibility Theorem** | Ch. 11 Ex. 11.10 | Ch. 7 Trig Sub |
| **Generating Functions** | Ch. 1 Comment 11, Ch. 23 | Ch. 18 Recursion |
| **Hadwiger-Finsler Inequality** | Ch. 14 Comment 15 | Ch. 10 / Ch. 14 |
| **Heron's Formula** | Ch. 11 | Ch. 1 / Ch. 14 |
| **Hockey-stick Identity** | Ch. 5 | Ch. 18 Recursion |
| **Implicit Function Theorem** | Ch. 15 Comment 2 | Ch. 11 Existence |
| **Inclusion-Exclusion** | Ch. 1 (Venn diagrams), Ch. 22 | Ch. 9 DOF / Ch. 6 Duality |
| **Intermediate Value Theorem (IVT)** | Ch. 3 Comment 15, Ch. 16 | Ch. 11 Existence |
| **Inversion (geometric)** | Ch. 8 | Ch. 6 Duality |
| **Jensen's Inequality** | Ch. 13 Comment 11, Ch. 14 | Ch. 10 / Ch. 14 |
| **King's Property of Integrals** | Ch. 18 Comments 10-12, Ex. 18.10, 18.12 | Ch. 2 Symmetry |
| **Klein's Erlangen Program** (implicit) | Ch. 8 (rigid-motion invariants) | Ch. 1 Invariance |
| **Kummer's Theorem** | Ch. 4 | Ch. 4 Modular |
| **L'Hôpital's Rule** | Ch. 15 Comment 8 | Ch. 13 Asymptotic |
| **Lagrange's Mean Value Theorem (MVT)** | Ch. 16 | Ch. 11 Existence |
| **Lagrange's Four-Square Theorem** | Ch. 21 Ex. 21.26 (via quaternions) | Ch. 20 Analogy |
| **Lagrange Multipliers** | Ch. 14 (mentioned) | Ch. 12 Extremal |
| **Leibnitz Rule (for $n$-th derivative)** | Ch. 15 Ex. 15.12(e) | Ch. 20 Analogy |
| **Lucas's Theorem** | Ch. 4 | Ch. 4 Modular |
| **Napoleon's Theorem** | Ch. 8 | Ch. 2 Symmetry |
| **Newton's Identities** | Ch. 3 | Ch. 11 Polynomial |
| **Pascal's Identity** | Ch. 5 Comment 1 | Ch. 18 Recursion |
| **Pigeonhole Principle** | Ch. 6 Comment 10 | Ch. 11 Existence |
| **Pólya Urn** | Ch. 22 Ex. 22.18 | Ch. 1 Invariance |
| **Power-Mean Inequality** | Ch. 13 Comment 11 | Ch. 10 |
| **Power Series of $\sin x$, $e^x$, $\ln(1+x)$** | Ch. 16, Ch. 23 | Ch. 13 / Ch. 11 |
| **Projection Rule (for triangles)** | Ch. 11 Theorem 5 | Ch. 1 Invariance |
| **Ptolemy's Theorem** | Ch. 10 Comment 14, Ex. 11.4 | Ch. 6 Duality |
| **Quaternions** | Ch. 21 Ex. 21.25-27 | Ch. 20 Analogy |
| **Ravi Substitution** ($a = y+z$ etc. for triangle sides) | Ch. 14 Comment 14 | Ch. 5 Substitution |
| **Reduction Formulas** | Ch. 18 (entire), Ch. 17 Ex. 17.24-26 | Ch. 8 Telescoping |
| **Reciprocal Basis** | Ch. 21 Ex. 21.8 | Ch. 6 Duality |
| **Riemann Sums / Riemann Integral** | Ch. 17 Comment 2 | Ch. 13 Asymptotic |
| **Rolle's Theorem** | Ch. 16 | Ch. 11 Existence |
| **Sandwich (Squeeze) Theorem** | Ch. 15, Ch. 16 (Main) | Ch. 11 Existence |
| **Section Formula** | Ch. 21 | Ch. 15 Geometric Pivot |
| **Sine Rule, Cosine Rule** | Ch. 11 | Ch. 1 Invariance |
| **Snell's Law (analogue)** | Ch. 13 Main Problem | Ch. 12 Extremal |
| **Stars and Bars Bijection** | Ch. 1 Comment 5 | Ch. 3 |
| **Stirling's Approximation** ($(n!)^{1/n}/n \to 1/e$) | Ch. 6, Ch. 18 Ex. 18.17 | Ch. 13 Asymptotic |
| **Stirling Numbers of the 2nd Kind** | Ch. 1 Ex. 1.27 | Ch. 3 |
| **Sturm Comparison Theorem (ODE)** | Ch. 19 Ex. 19.7 | Ch. 1 / Ch. 10 |
| **Taylor's Theorem** | Ch. 16 | Ch. 13 Asymptotic |
| **Triangle Inequality** | Ch. 6, Ch. 21 Ex. 21.24 | Ch. 10 |
| **Tschirnhaus Transformation** (depressed cubic) | Ch. 3 Comment 12 | Ch. 5 Substitution |
| **Twenty Characterisations of Equilateral Triangle** | Ch. 14 Comment 8 | Ch. 1 Invariance |
| **Vandermonde's Identity** (binomial) | Ch. 5 | Ch. 11 Polynomial |
| **Vandermonde Determinant** | Ch. 3 Comment 18 | Ch. 11 |
| **Venn Diagrams** | Ch. 1, Ch. 22 | Ch. 9 DOF |
| **Vieta's Relations** | Ch. 3 | Ch. 1 Invariance |
| **Wallis Formula** | Ch. 18 Comment 5 | Ch. 8 Telescoping / Ch. 13 Asymptotic |
| **Weierstrass Substitution** ($t = \tan(x/2)$) | Ch. 10 Comment 3 | Ch. 5 Substitution |
| **Wilson's Theorem** | Ch. 4 Ex. 4.43 | Ch. 4 Modular |
| **Zero-Sum Game** | Ch. 23 Ex. 23.15 | Ch. 1 Invariance |

---

## VII. Voice Register Samples for Pillar 2 Drafting

*Quotable passages from Joshi that capture his pedagogical voice. Use these as references when drafting Pillar 2 vignettes, postscripts, or meta-commentary sections. **Direct quotation is permitted with attribution** (see Blueprint §C-4 on sourcing rules).*

### On problem-solving philosophy

- **Ch. 1 (Counting Comment 1):** "It is to be noted that usually, it is a suitable combination of techniques rather than a single technique that works best."
- **Ch. 1 (Counting Comment 1):** "A good decomposition may not always exist and even when it does, it may not always be obvious. In such cases, hitting the right decomposition is a thrilling experience."
- **Ch. 1 (Counting):** "Three most common pitfalls in counting arguments: certain unwanted elements get counted, some wanted elements do not get counted, while some elements get counted more than once."
- **Ch. 6 (Inequalities — voice on AM-GM):** "Real-life analogies can make something easier to understand. They cannot be a substitute for a mathematical proof."
- **Ch. 12 (Heights/Distances Comment 1):** "After solving a problem of this type one gets the feeling that one has done something 'really useful' which you do not get after showing that a certain determinant vanishes even though the latter may be far more challenging."
- **Ch. 13 (Maxima/Minima):** "The greedy approach. Usually it does not work."
- **Ch. 13:** "Show him how to make the most economical tin can to hold a given volume and he is impressed!"
- **Ch. 17 (Areas Comment 1):** "Just as in complementary counting (Chapter 1, Comment No. 1) we find the cardinality of a set by subtracting the cardinality of its complement from that of the ambient set, the area of $R_1$ can also be obtained by finding the area of $R$ and subtracting the area of $R_2$ from it." — **Ch. 20 Analogy gem.**
- **Ch. 17 (Areas):** "At any rate, finding the antiderivative is more of an art and an individual's skill and experience matter more than dozens of formulas crammed in the head."
- **Ch. 19 (ODEs):** "Whenever a student studies a solution (either his own or somebody else's) to some problem, it is a healthy habit to see if the problem, and indeed every step of the solution, could be done in some other way. Although for that particular problem the alternate methods may not be of much advantage, there may be some variations of the problem where they may be superior and, in some cases, indispensable."
- **Ch. 20 (Functional Eqs Comment 5):** "Normally it is an asset to be able to recognise the similarity of a given problem to some other problem whose solution is already known. Such a recognition makes you more comfortable and sometimes also saves duplication of work. But one should be open to the possibility that some entirely different approach may work better." — **Ch. 20 Analogy canonical thesis.**

### On rigor versus intuition

- **Ch. 2 (Basic Algebra):** "If you are able to paraphrase the argument rigorously by introducing appropriate sets and functions, then such mistakes can be avoided." — formalism as error-prevention.
- **Ch. 8 (Geometry):** "A good diagram is half the solution."
- **Ch. 15 (Limits):** "Just because something has been denoted like a ratio does not make it a ratio, in much the same way as a person named Goldsmith need not be a goldsmith by profession."
- **Ch. 15:** "Saying that Mr. X is not married to a Muslim is not quite the same as saying that Mrs. X is not a Muslim. The former statement holds even when Mr. X is unmarried." — existential vs non-existential.
- **Ch. 16 (Theoretical Calculus):** "Real-life analogies can make something easier to understand. They cannot be a substitute for a mathematical proof." — explicit limit on analogical reasoning.
- **Ch. 23 (Infinitistic Prob Ex. 23.19):** "An assumption like this is, of course, unwarranted and can lead to disasters. But Euler made it anyway and 'proved' this beautiful result." — on Euler's bold ζ(2) "proof". Rigour vs creativity tension.

### On meta-pedagogy

- **Ch. 6 (Inequalities — voice on ingenuity):** "After gaining some practice, it is hardly necessary to show all the intermediate steps in the calculation."
- **Ch. 14 (Trig Optim Comment 3):** "Problems of triangular optimisation do not appear every year in the JEE, possibly because they tend to be rather repetitious, since in the vast majority of cases, the optimum is attained when the triangle is equilateral. A short question may be asked to test awareness of this fact."
- **Ch. 16:** "Questions based on theoretical calculus are comparatively infrequent at the JEE… Even those doing well in JEE sometimes face difficulties with this material later. Why not familiarise yourself with it ahead of time?"
- **Ch. 19 (ODEs):** "Differential equations have been introduced in the JEE syllabus relatively recently. Generally only elementary questions are asked. But because differential equations are not included at full steam, sometimes the problems appear tricky or obscure in the absence of the relevant supplementary material."
- **Ch. 22 (Finitistic Prob):** "If you have clear thinking, [probability problems] are quick scoring questions as the other computational work is often minor." — **Probability rewards conceptual clarity over computational sweat. Pillar 5 voice.**

### On data and degrees of freedom

- **Ch. 19 (ODEs, Comment 4 of Main Problem):** "It is important to note that the actual values of the constants $a, b, \alpha, \beta$ cannot be determined from the data because to determine them we would need four equations, while the data gives only two. But the individual values of $a$ and $b$ are not needed, since the problem deals only with the proportion of the quantities in the two reservoir." — **Ch. 17 DOF Analysis canonical voice.**
- **Ch. 23 (Ex. 23.17):** "It is in this sense that equality of two real numbers is an accident while their inequality is a rule." — probabilistic intuition on generic position.

### On analogy and connection

- **Ch. 17 (Areas):** "An integral is obtained by putting together the contributions (measured as the values of some real valued function) of individual points of the domain. In national integration, the various individuals or communities contribute what they have, so as to build a nation with a collective identity."
- **Ch. 21 (Vectors):** "[Quaternions] are mixtures of scalars and vectors just as complex numbers are mixtures of real numbers and purely imaginary numbers."
- **Ch. 21 (Vectors):** "Here the analogy with a triangle fails. So one should be wary in generalising from plane to solid geometry." — caution on over-analogising.
- **Ch. 23 (Ex. 23.5, von Neumann anecdote):** "But that's exactly the way I did it." — **canonical Ch. 20 Analogy story.**

### On elegant solutions

- **Ch. 1:** "They take you directly to the destination, often bypassing the steps one would normally encounter in a straightforward approach."

### Recurring stylistic devices in Joshi's prose

1. **Two-method comparison.** Joshi typically presents the brute-force approach first, then the elegant one. Pillar 2's Six-Point Framework (Brute Path → Elegant Pivot) is essentially Joshi's signature pattern.
2. **Pedagogical asides** in parentheses or footnotes. Often the deepest insights are tucked into footnotes (e.g., the footnote on differentials in Ch. 15).
3. **Real-life analogies** (Goldsmith, marital status, money compounding, fly-between-mathematicians).
4. **Cross-references** within and between chapters — Joshi explicitly builds a network of dependencies, not a linear narrative.
5. **Explicit JEE meta-commentary** — Joshi tells the reader *why* certain topics appear (or don't appear) in JEE and *what to expect*.

### Voice register guidance for Pillar 2 chapter drafts

The Advaitian Pillar 2 register should:
- **Adopt** Joshi's discursive, technique-by-technique commentary style.
- **Adopt** Joshi's habit of presenting brute and elegant solutions side by side.
- **Adopt** Joshi's real-life analogies (use sparingly; mark explicitly as analogies).
- **Avoid** Joshi's prose density (Pillar 2 commentary should be tighter).
- **Avoid** Joshi's habit of long parenthetical asides; instead use side-boxes or footnotes.
- **Add** the Advaitian Six-Point Framework structure (Seed → Brute Path → Elegant Pivot → Pitfalls → Connections → Takeaway), which Joshi's commentaries implicitly follow but never name.

---

🌑

*End of Cursor-Joshi.md v1.0 — consolidated extraction complete. This file should be loaded at the start of every Pillar 2 drafting session.*
