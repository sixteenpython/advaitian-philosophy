# Chapter Template — Pillar 2 (The 20 Archetypes)

> **Purpose.** Single canonical chassis for the 19 archetype chapters that follow Chapter 1 (Invariance, the prototype). Every archetype chapter inherits this skeleton. Diverge from the section list only with explicit reason and Anand's sign-off — drift compounds across 19 chapters and silently rots the book.

---

## Front Matter (YAML, for build pipeline & cross-reference graph)

```yaml
---
chapter: <int>
archetype: <Name>
subtitle: "<one-line meta-principle>"
category: <Structure Recognition | Transformation Thinking | Constraint Exploitation | Counting & Extremization | Meta-Reasoning>
related_archetypes: [<list of #s>]
key_gems: [<refs to Pillar 5 catalog when stabilized>]
canonical_takeaway: "<one quotable sentence>"
status: outline | draft | review | locked
last_revised: YYYY-MM-DD
---
```

---

## Section Map (canonical for all 20 archetype chapters)

### Opening Vignette  (≈300–500 words)

**Voice register:** Polya / KD Joshi.

A vivid concrete image that embodies the archetype before any formalism — memorable enough that a student five years later, encountering this archetype in a different context, recalls *this image first*. Closes with a single-sentence naming: *"This is [ARCHETYPE]."*

### 1. The Archetype Defined  (≈800–1,200 words)

#### 1.1 Formal Definition  *(Tao / Engel)*

Mathematical definition with notation, inside a `\begin{definition}` LaTeX environment. Unpack the definition in plain English afterward. List 3–5 *forms* the archetype takes.

#### 1.2 Core Principle  *(Polya)*

Single italicized sentence stating the meta-principle. 2–3 paragraphs unpacking the *cognitive consequence*. One short illustrative example (no full proof).

#### 1.3 The Cognitive Shift  *(Polya / Joshi)*

"Before vs After" framing. 4–6 specific habits of archetype-aware solvers. Honest treatment of the emotional/procedural change required.

### 2. The Deep Structure  (≈900–1,300 words)

#### 2.1 Mathematical Foundations  *(Tao / Engel + named-theorem rigor)*

Connect the archetype to deep mathematical structures (group theory, topology, algebra, analysis). Use `\begin{theorem}[Optional Name]` for named results. Cite originator + year. **Honesty rule:** if a theorem is given as informal sketch, label it explicitly: "Theorem (Noether, 1918, informal statement)."

#### 2.2 Physical / Cross-Domain Foundations  *(Engel / Andreescu)*

2–4 instances from physics, computer science, or other quantitative domains. One paragraph each, structurally identical to the math case.

#### 2.3 Cognitive Foundations  *(Polya)*  *— optional, keep only when archetype has psychological depth*

Why is this archetype hard for humans? How do experts overcome the difficulty?

### 3. The Diagnostic Toolkit  (≈600–900 words)

#### 3.1 The [N]-Questions Method  *(Zeitz / Andreescu — operational, heuristic)*

A small numbered list of diagnostic questions. Each question gets a one-line execution note: when it succeeds, when it fails.

#### 3.2 Forms / Types of [ARCHETYPE]  *(Engel — taxonomic)*

3–5 categories of how the archetype manifests, each with 4–6 example instantiations. Compact, table-friendly.

#### 3.3 Common Pitfalls  *(Polya / Joshi)*

3–5 *named* pitfalls. Each: name + description + why-tempting + actionable check. Match Pitfall Hall of Fame in `ThinkMath_Blueprint_v3.md` where overlap exists.

### 4. Worked Examples  (≈1,200–2,000 words)

**Voice register:** Tao / Zeitz / Andreescu hybrid.

**Three examples, ordered by difficulty.** Each must include: explicit problem statement (`\begin{problem}` block), Three-Questions-Method (or analog) applied, solution with named pivot, verification or domain check, key lesson (1–2 sentences).

#### 4.1 Example 1 — *Tier 1: foundational*  (≈400–600 words)

Simulated to JEE Mains / CBSE 12 level, or a clean past problem. Demonstrate the archetype in its most direct form.

#### 4.2 Example 2 — *Tier 2: JEE Advanced / Putnam B-level*  (≈400–700 words)

Real or simulated. Demonstrate the archetype in a less obvious form. Show one wrong path being rejected, then the right pivot.

#### 4.3 Example 3 — *Tier 3: IMO-level*  (≈400–800 words)

Real IMO problem (cited with year + problem #) or simulated to that level. Demonstrate multidirectional convergence (this archetype + 1 secondary). Full proof with theorem-style rigor.

### 5. Practice Problems  (≈400–600 words)

**Voice register:** Engel / Andreescu (problem-set style).

7 problems, ordered by difficulty: 2 foundational, 3 intermediate (JEE Adv / Putnam-level), 2 advanced (IMO-level). Statements only in this section. Solutions / hints in chapter-end appendix. Mark sources where real: "(IMO 2003, P3)", "(Putnam 2017, A2)", or "(simulated to IMO level)".

### 6. The Connections Web  (≈600–900 words)

**Voice register:** Tao (precise, lightly elegant).

#### 6.1 [ARCHETYPE] Across Mathematical Domains

Algebra, Geometry, Calculus & Analysis, Number Theory, Combinatorics, Topology — one paragraph per domain.

#### 6.2 [ARCHETYPE] in Physics & Other Sciences

Conservation laws, symmetries, cross-domain applications. Brief.

#### 6.3 Cross-Domain Manifestations Outside Mathematics

Economics, computer science, biology, information theory. 4–6 instances, one sentence each.

#### 6.4 Related Archetypes

Explicit pointers to other archetypes. Each link: name + 1-line description of the connection.

### 7. Master Takeaways  (≈200–400 words)

**Voice register:** Polya / Joshi (philosophical-distilled).

5–7 *named, quotable* one-line principles. Each followed by a single sentence of context. These are what the reader will quote 5 years later.

### 8. Self-Assessment Checklist  (≈100–200 words)

5–8 yes/no checkpoints testing whether the reader can recognize, apply, and *teach* the archetype.

### Bridge to Chapter [N+1]  (≈200–400 words)

**Voice register:** Polya (continuity).

Single transitional passage contrasting this archetype with the next. Hints at the next archetype's central question without revealing its content.

---

## Conventions

### Math notation
Sets: $\mathbb{R}, \mathbb{Z}, \mathbb{N}, \mathbb{Q}, \mathbb{C}$ via `\mathbb{}`. Functions: $f : X \to Y$. Group action: $g \cdot x$. Inline: `$...$`. Display: `\[ ... \]`.

### LaTeX environments (in `.md` via raw-LaTeX blocks)
- Definitions: `\begin{definition} ... \end{definition}`
- Theorems: `\begin{theorem}[Optional Name] ... \end{theorem}`
- Propositions: `\begin{proposition} ... \end{proposition}`
- Examples: `\begin{example} ... \end{example}`
- Practice problems: `\begin{problem} ... \end{problem}` (custom env defined in shared preamble)

### Cross-references
- Other archetype: full name on first mention — *Archetype #2: Symmetry* — then *Archetype #2* thereafter.
- Other chapter: *Chapter 9, §3.2*.
- Gem reference (when Pillar 5 stabilizes): *Gem A1: Vieta's Formulas*.

### Citation discipline
- Real problems: cite source inline. *(IMO 1988, Problem 6)*, *(Putnam 2003, A1)*.
- Simulated problems: append *"(simulated to IMO level)"* or similar — once per problem.
- Theorems: name + originator + year. *(Noether, 1918)*.
- **Never fabricate a citation.** When unsure, mark as simulated and let Anand verify or substitute.

### Voice discipline
- ≤ 2 voice register switches per section.
- Polya register dominates section openings, bridges, philosophical claims.
- Tao / Engel register dominates rigorous mid-sections, definitions, theorem statements.
- Zeitz / Andreescu register dominates worked examples and practice problems.
- KD Joshi register where bridging school-math intuition to olympiad-level rigor.

### Length budget per chapter
Total target: **5,000–8,000 words**. Including all 8 sections + bridge. Compress ruthlessly; rigor is not verbosity.

### Formatting
- `##` for top sections, `###` for sub. *Italics* for concept names; **bold** for key terms on first use only.
- No emoji except the `🌑` chapter-end signature (consistent with Anand's existing voice).

---

## Authoring checklist

Before promoting `status: outline → draft`:
- [ ] Anand has approved the section-by-section outline
- [ ] 3 worked-example problem statements approved
- [ ] 7 practice problems with sources marked

Before promoting `status: draft → review`:
- [ ] All 8 sections present with target lengths met within ±20%
- [ ] At least 3 named-theorem citations or formal definitions
- [ ] Cross-references to ≥ 3 other archetypes
- [ ] Master takeaways: 5–7 one-line principles
- [ ] Bridge to next chapter written
- [ ] LaTeX math compiles via Pandoc → `.tex`
- [ ] Overleaf-paste `.txt` self-contained (compiles on a fresh Overleaf project without setup)

Before promoting `status: review → locked`:
- [ ] Anand has reviewed prose
- [ ] Anand has verified every mathematical claim
- [ ] All AI-flagged uncertainties resolved
- [ ] Cross-references in this chapter to other chapters validated
- [ ] No drift from doctrine canon (`Advaitian_Philosophy_Framework.txt` + `ThinkMath_Blueprint_v3.md`)

---

🌑
