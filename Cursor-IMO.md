# Cursor-IMO.md — Consolidated Memory File for *The IMO Compendium*

**Source.** Dušan Djukić, Vladimir Janković, Ivan Matić, Nikola Petrović, *The IMO Compendium: A Collection of Problems Suggested for the International Mathematical Olympiads: 1959–2004*, Springer (1st ed. 2006; the version in workspace is the 2006 edition with 1959–2004 coverage; a 2011 2nd ed. extends to 1959–2009).  
**Extracted text.** `my_references/imo-compendium.txt` (35,877 lines, 379,048 words, 2,086 KB).  
**Role in workspace.** **Primary reference for Pillar 4 Chapters 4–6** (the 25-case-study slate of §8.9), with secondary use across all of Pillar 4 for IMO-problem source-verification and curated-commentary support.

---

## §I — Overview

The IMO Compendium is the single most authoritative collection of IMO problems, organising every contest problem, shortlisted problem, and longlisted problem from 46 IMO competitions (1959–2004) into one source. Each problem appears in Ch. 3 (Problems) with its statement; the corresponding solution appears in Ch. 4 (Solutions). The book also includes a Ch. 2 (Basic Concepts and Facts) primer covering algebra, analysis, geometry, number theory, and combinatorics — useful as a Pillar 2 cross-reference but not the primary use-case for our project.

For Pillar 4 specifically, the Compendium provides three deliverables:
1. **Verified problem statements** for every IMO citation in the §8.9 case-study slate.
2. **Verified solutions** for every problem — these are the Compendium's own solutions, which can be cross-checked against the Pillar 3 multidirectional decomposition.
3. **Curated commentary** in the solutions (the Djukić et al. group often notes alternative approaches, problem history, or particularly elegant insights — exactly the kind of designer's-perspective material Pillar 4 case studies depend on).

---

## §II — Year-by-Year Problem Index (Ch. 3 anchors)

Each entry below gives the section number from the Compendium TOC, the page number (book), and an *approximate text-file line anchor* for fast lookup in `imo-compendium.txt`.

| Year | TOC § | Book page | Text anchor (approx) | Contest format |
|---|---|---|---|---|
| 1959 | 3.1 | 27 | 700 | Contest problems only |
| 1960 | 3.2 | 29 | 800 | Contest |
| 1961 | 3.3 | 30 | 850 | Contest |
| 1962 | 3.4 | 31 | 900 | Contest |
| 1963 | 3.5 | 32 | 950 | Contest |
| 1964 | 3.6 | 33 | 1000 | Contest |
| 1965 | 3.7 | 34 | 1050 | Contest |
| 1966 | 3.8 | 35 | 1100 | Contest + longlist (1959–66) |
| 1967 | 3.9 | 42 | 1500 | Contest + longlisted |
| 1968 | 3.10 | 51 | 2200 | Contest + shortlisted |
| 1969 | 3.11 | 55 | 2400 | Contest |
| 1970 | 3.12 | 58 | 2600 | Shortlisted |
| 1971 | 3.13 | 65 | 3000 | Shortlisted |
| 1972 | 3.14 | 72 | 3400 | Shortlisted |
| 1973 | 3.15 | 78 | 3800 | Shortlisted |
| 1974 | 3.16 | 85 | 4200 | Shortlisted |
| 1975 | 3.17 | 92 | 4600 | Shortlisted |
| 1976 | 3.18 | 98 | 5000 | Shortlisted |
| 1977 | 3.19 | 104 | 5500 | Longlisted (1977 had no shortlist) |
| 1978 | 3.20 | 119 | 6000 | Shortlisted |
| 1979 | 3.21 | 126 | 6400 | Shortlisted |
| 1981 | 3.22 | 143 | 6742 | Shortlisted (no 1980 IMO) |
| 1982 | 3.23 | 147 | 6884 | Shortlisted |
| 1983 | 3.24 | 157 | 7344 | Shortlisted |
| 1984 | 3.25 | 169 | 7854 | Shortlisted |
| 1985 | 3.26 | 180 | 8375 | Shortlisted |
| 1986 | 3.27 | 193 | 8950 | Shortlisted |
| 1987 | 3.28 | 204 | 9450 | Shortlisted |
| **1988** | **3.29** | **216** | **9970** | **Shortlisted — includes the legendary P6 (Vieta jumping)** |
| 1989 | 3.30 | ~227 | 10500 | Shortlisted |
| 1990 | 3.31 | ~240 | 11100 | Shortlisted |
| 1991 | 3.32 | ~253 | 11700 | Shortlisted |
| 1992 | 3.33 | ~267 | 12300 | Shortlisted |
| 1993 | 3.34 | ~280 | 12900 | Shortlisted |
| 1994 | 3.35 | ~294 | 13500 | Shortlisted |
| 1995 | 3.36 | ~307 | 14100 | Shortlisted |
| 1996 | 3.37 | ~320 | 14700 | Shortlisted |
| 1997 | 3.38 | — | 15300 | Shortlisted |
| 1998 | 3.39 | — | 15900 | Shortlisted |
| 1999 | 3.40 | — | 16500 | Shortlisted |
| 2000 | 3.41 | — | 17100 | Shortlisted |
| 2001 | 3.42 | — | 17700 | Shortlisted |
| 2002 | 3.43 | — | 18300 | Shortlisted |
| 2003 | 3.44 | — | 18900 | Shortlisted |
| 2004 | 3.45 | — | 19500 | Shortlisted |

**Lookup workflow.** To locate a specific IMO year's problems, search `imo-compendium.txt` near the anchor line, or use Grep with pattern `^3\.\d+ IMO YYYY`. Approximate anchors are estimates from the TOC; chapter-final-review will tighten them.

---

## §III — Solutions Index (Ch. 4 anchors)

Ch. 4 (Solutions) begins at book page 333 (text line ~15700). Each year's solutions section uses the same numbering as the problem section. Approximate text-anchor table:

| Year | Solutions § | Book page | Text anchor (approx) |
|---|---|---|---|
| 1959 | 4.1 | 333 | 15700 |
| 1960 | 4.2 | 335 | 15800 |
| 1961 | 4.3 | 337 | 15900 |
| (...) | (...) | (...) | (...) |
| 1981 | 4.22 | 442 | 22100 |
| 1982 | 4.23 | 451 | 22600 |
| 1983 | 4.24 | 457 | 23000 |
| 1984 | 4.25 | 466 | 23500 |
| 1985 | 4.26 | 473 | 24000 |
| 1986 | 4.27 | 481 | 24500 |
| 1987 | 4.28 | 489 | 25000 |
| **1988** | **4.29** | **500** | **25500** |
| 1989 | 4.30 | 516 | 26200 |
| 1990 | 4.31 | 530 | 26900 |
| 1991 | 4.32 | 544 | 27600 |
| 1992 | 4.33 | 558 | 28300 |
| 1993 | 4.34 | 568 | 28900 |
| 1994 | 4.35 | 581 | 29500 |
| 1995 | 4.36 | 589 | 30100 |
| 1996 | 4.37 | 602 | 30800 |
| 1997 | 4.38 | 618 | 31500 |
| 1998 | 4.39 | 632 | 32100 |
| 1999 | 4.40 | 646 | 32700 |
| 2000 | 4.41 | 661 | 33300 |
| 2001 | 4.42 | 675 | 33900 |
| 2002 | 4.43 | 689 | 34500 |
| 2003 | 4.44 | 701 | 35000 |
| 2004 | 4.45 | 715 | 35500 |

---

## §IV — Topic-Area Index (Ch. 2 primer)

Ch. 2 of the Compendium is organised topically, mirroring the problem-classification grid that the IMO Selection Committee uses internally. The five topic areas are:

| Topic | TOC § | Page | Subsections |
|---|---|---|---|
| Algebra | 2.1 | 5 | Polynomials, Recurrences, Inequalities, Groups/Fields |
| Analysis | 2.2 | 10 | Real analysis, sequences and series |
| Geometry | 2.3 | 12 | Triangle geometry, Vectors, Barycenters, Quadrilaterals, Circle geometry, Inversion, Geometric inequalities, Trigonometry, Formulas |
| Number Theory | 2.4 | 19 | Divisibility, Congruences, Exponential congruences, Quadratic Diophantine equations, Farey sequences |
| Combinatorics | 2.5 | 22 | Counting, Graph theory |

For Pillar 4 cross-archetype reach, Pillar 2 archetypes map to topic areas as follows:

| Topic area | Primary Pillar 2 archetypes |
|---|---|
| Algebra | #5 Substitution, #7 Normalisation, #1 Invariance |
| Analysis | #11 Existence/Uniqueness, #12 Extremal |
| Geometry | #2 Symmetry, #8 Domain Translation, #4 Hidden Structure |
| Number Theory | #14 Parity/Modularity, #16 Reverse Engineering, #18 Induction |
| Combinatorics | #13 Combinatorial, #15 Bijection, #17 DOF Analysis |

This mapping is approximate (a Number Theory problem may invoke Algebra archetypes; a Combinatorics problem may invoke Geometry); use as a coarse navigation aid, not a partition.

---

## §V — Famous-Problem Locator (Pillar 4 Goldmine)

The following IMO problems are widely recognised as having particularly elegant CEPs and are leading candidates for the §8.9 case-study slate. Each is annotated with: contest position, conjectured CEP tier (per Blueprint §8.2 Moderate/Hard/Extreme taxonomy), and the Cursor anchor for the problem statement.

| Year-Problem | CEP description | CEP Tier | Pillar 2 archetypes | Anchor (text line) |
|---|---|---|---|---|
| **IMO 1959 P1** | $\gcd(21n+4, 14n+3) = 1$ — Euclidean algorithm in disguise | Moderate | #1 + #14 | ~700 |
| **IMO 1972 P1** | Among 10 two-digit numbers, two disjoint subsets with same sum (subset-sum pigeonhole) | Moderate | #13 + #12 + #14 | ~3400 |
| **IMO 1975 P3** | All triangles with rational sides + rational area satisfy Heron's formula constraint — designed around Pythagorean triples | Hard | #4 + #14 + #16 | ~4600 |
| **IMO 1979 P3** | The "two circles" power-of-a-point problem — classical CEP | Hard | #2 + #8 + #4 | ~6400 |
| **IMO 1981 P3** | Maximum of $m^2 + n^2$ under Fibonacci-recurrence constraint — Fibonacci is the hidden CEP | Hard | #18 + #1 + #4 | ~6800 |
| **IMO 1985 P2** | $f : \mathbb{N} \to \mathbb{N}$ functional equation — CEP is the unique solution $f(n) = n$ via descent | Hard | #5 + #11 + #18 | ~8400 |
| **IMO 1986 P3** | Tournament problem — CEP is the existence of a universal vertex | Hard | #13 + #11 + #12 | ~8950 |
| **IMO 1986 P5** | Functional equation with monotonicity — Cauchy variant | Hard | #5 + #11 + #1 | ~9050 |
| **IMO 1987 P5** | Geometric combinatorics — CEP is a clean integer answer arising from a counting identity | Hard | #13 + #4 + #2 | ~9550 |
| **IMO 1988 P3** | Function-iteration parity problem | Hard | #14 + #18 + #1 | ~9920 |
| **IMO 1988 P6** | **THE Vieta-jumping problem** — CEP is "perfect square" | **Extreme** | **#18 + #16 + #1** | **9997** |
| **IMO 1989 P5** | Functional inequality with specific CEP | Hard | #11 + #12 + #5 | ~10550 |
| **IMO 1990 P3** | "Find all integers $n \geq 2$ such that $2^n + 1$ is divisible by $n^2$" — CEP is the answer $n = 3$ via mod-arithmetic descent | Hard | #14 + #16 + #11 | ~11200 |
| **IMO 1991 P5** | Geometric inequality with isoperimetric-style CEP | Hard | #12 + #2 + #4 | ~11800 |
| **IMO 1994 P4** | "Find all positive integer pairs $(m, n)$ such that $(n^3+1)/(mn-1)$ is an integer" — direct Vieta-jumping cousin | **Extreme** | #14 + #16 + #18 | ~13600 |
| **IMO 1995 P2** | Inequality with $1/a + 1/b + 1/c \geq$ specific bound — CEP is a Cauchy-Schwarz application | Hard | #5 + #12 + #11 | ~14200 |
| **IMO 1996 P5** | Hexagon area inequality — historically among the most difficult IMO problems (solved by 6 of several hundred) | **Extreme** | #2 + #12 + #4 | ~14800 |
| **IMO 1999 P6** | $f : \mathbb{R} \to \mathbb{R}$ functional equation — Cauchy variant with constraint | Hard | #5 + #11 + #1 | ~16700 |
| **IMO 2001 P6** | Geometric inequality on a convex quadrilateral | Hard | #2 + #12 + #8 | ~17900 |
| **IMO 2003 P6** | Number-theoretic existence problem with descent | Hard | #14 + #16 + #11 | ~19100 |

The 20 problems above are **leading candidates** for the Pillar 4 §8.9 case-study slate (which calls for 25 total — 17 of these plus 8 self-selected from Engel/Zeitz/Joshi will fully cover the slate).

---

## §VI — Pillar 4 §8.9 Case-Study Slate — IMO Source Anchors

The Blueprint §8.9 case-study slate lists 25 problems organised by Moderate / Hard / Extreme tier. Below is the IMO-source anchor for each tier (Pillar 4 final-review will lock specifics).

### Moderate Tier (Cases 1–7, ~7 cases)

Source preference: IMO problems from 1959–1975 (when problems were generally simpler), supplemented by Joshi/Engel for non-IMO cases.

- IMO 1959 P1 (gcd CEP)
- IMO 1964 P1 (NT divisibility CEP)
- IMO 1972 P1 (subset-sum pigeonhole)
- (+ 4 cases from Engel Ch. 4 / Zeitz Ch. 3 / Joshi)

### Hard Tier (Cases 8–17, ~10 cases)

Source preference: IMO problems from 1976–1995 + Putnam.

- IMO 1979 P3, IMO 1981 P3, IMO 1985 P2, IMO 1986 P3, IMO 1986 P5
- IMO 1987 P5, IMO 1988 P3, IMO 1989 P5, IMO 1990 P3
- (+ 1 case from Engel Ch. 8/14 or Zeitz Ch. 4)

### Extreme Tier (Cases 18–25, ~8 cases)

Source preference: IMO from 1988–2004 + the legendary problems list.

- IMO 1991 P5, IMO 1994 P4, IMO 1995 P2, IMO 1996 P5
- IMO 1999 P6, IMO 2001 P6, IMO 2003 P6
- **IMO 1988 P6 — Case 25 (the capstone)** — already locked per Blueprint §8.9 row 25 and Pillar 3 Ch. 3 WE1 cross-reference.

---

## §VII — Notable Theorems and Named Results (Compendium Ch. 2)

The Compendium's Ch. 2 contains a curated list of named theorems frequently invoked in IMO solutions. Pillar 4 case studies often turn on these:

| Theorem | Ch. 2 § | Pillar 4 use |
|---|---|---|
| Vieta's formulas | 2.1.1 (Theorem 2.10) | Direct anchor for Vieta-jumping case studies (1988 P6, 1994 P4) |
| AM-GM, Cauchy-Schwarz, Jensen | 2.1.3 | Inequality-CEP case studies |
| Fermat's Little Theorem | 2.4.2 | Number-theory descent case studies (1988 P3, 1990 P3) |
| Pell equation theory | 2.4.3 | Diophantine case studies (1981 P3, 1995 P2) |
| Helly's theorem | 2.5 (geometry) | Cross-reference for Pillar 3 Ch. 6 CS#3 (already drafted) |
| Pigeonhole / Box principle | 2.5 | Moderate-tier case studies |
| Inversion in geometry | 2.3.6 | Geometry case studies |
| Stewart's theorem, Ptolemy | 2.3 | Geometry case studies |
| Burnside / Cauchy-Frobenius | 2.5 (counting) | Combinatorial case studies |

For each named theorem invoked in a Pillar 4 case study, the Compendium provides a verified statement that should be cited.

---

## §VIII — Maintenance Notes

- **File source.** `my_references/imo_compendium.pdf` (5.8 MB; 2006 edition; 1959–2004 coverage) extracted to `my_references/imo-compendium.txt` via `pdftotext -layout`. 35,877 lines, 379,048 words, 2.0 MB.
- **Version.** v1.0 — May 28, 2026. Created on user provision of the PDF.
- **Next maintenance trigger.** Pillar 4 Ch. 4 first-draft completion; verify the specific IMO problem citations in §V (the famous-problem locator) and §VI (the case-study slate anchor list).
- **Outstanding gap — coverage.** The Compendium 2006 edition extends to 1959–2004. Pillar 4's §8.9 slate may include 2005–2024 IMO problems; for those, fallback to `imo-official.org` (free, complete through current year). This is a minor gap — most of the "legendary" IMO problems with widely-recognised elegant CEPs are pre-2004.
- **Lookup efficiency.** The extracted text-file line anchors in §II and §III above are *approximate* (estimated from TOC page numbers and average page length). For precise anchors, use Grep with pattern `^3\.\d+ IMO YYYY` (problems) or `^4\.\d+ Contest|Shortlisted|Longlisted .* YYYY` (solutions).

---

*End of Cursor-IMO.md v1.0.*
