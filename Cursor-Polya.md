# Cursor-Polya.md — Consolidated Memory File for George Polya's *How to Solve It*

**Source.** George Polya, *How to Solve It: A New Aspect of Mathematical Method*, Second Edition, Doubleday Anchor Books (Doubleday & Company, Inc., Garden City, New York). First edition 1945 (Princeton UP); second edition 1957 with Part IV "Problems, Hints, Solutions" added.  
**Source file.** `my_references/PolyaHowToSolveIt.pdf` (3.3 MB, 29 PDF pages — each PDF page is a two-up scan of a book spread, so the file contains roughly 50–58 book pages of content covering the cover, full TOC, Part III selected entries, and Part IV problems/hints/solutions). **The file is image-only (scanned bitmaps, no embedded text).** `pdftotext` returns nothing; Tesseract OCR is not installed on the system.  
**Role in workspace.** **Primary historical-foundational reference for Pillar 4 Chapter 7** (the 5-Step CEP Design Framework, which is an inverted descendant of Polya's framework). Secondary across Pillar 4 as the foundational ancestor cited via Tao (who explicitly cites Polya 1957 in `Cursor-Tao.md` §VIII).

---

## §I — Important provenance note (read first)

The PDF was visually verified as Polya's *How to Solve It* (cover page, full table of contents, and sample interior pages from Parts III and IV were inspected directly via page-rasterisation). However:

1. **The PDF is image-only.** No embedded text; programmatic search (Grep, ripgrep) against the PDF will return zero results. To extract specific verbatim quotes from this PDF, OCR is required (Tesseract is not installed; alternative options: install Tesseract, use online OCR service, or visually transcribe specific pages via `pdftoppm` rendering + visual reading).

2. **The PDF appears to cover only part of the book.** The full second-edition book is ~250 pages; the scan covers the front matter (cover + TOC pages xii–xv) and portions of the later content (Part III selected dictionary entries and Part IV problems/hints/solutions, ending at book page ~253). Substantial chunks of Parts I, II, and the early Part III alphabetical entries appear *not* to be in this scan.

3. **Mitigation strategy for Pillar 4.** Polya's *How to Solve It* is among the most extensively documented and quoted books in mathematics-education literature, with substantial coverage in training corpora and in our reference triumvirate (Engel, Zeitz, Tao all cite Polya directly). For Pillar 4 Ch. 7, this file provides:
   - **Confirmed structural reference** (Parts I-IV layout verified from TOC scan)
   - **Confirmed Part III heuristic-dictionary entries list** (alphabetical entries verified from TOC pages)
   - **Verified Part IV worked-example content** (pages 250-253 visible — includes the "Compute An, Bn, Cn, Dn, En coins" example #20)
   - **Indirect verbatim access** via Tao's explicit Polya citation (`Cursor-Tao.md` line 207: *"(Polya 1957) is a classic reference for many of these"*) and via Engel/Zeitz secondary discussion
   - **Training-corpus-derived structural knowledge** of the famous four-phase framework and the heuristic dictionary

4. **If 100% Polya text-extractable access is required**, the user should replace `PolyaHowToSolveIt.pdf` with a text-extractable version. Polya's *How to Solve It* circulates widely in text-extractable form; the Princeton UP 2014 expanded edition (with foreword by John Conway) is the recommended modern edition.

---

## §II — Book Structure (verified from TOC scan)

Polya's *How to Solve It*, Second Edition, has four parts. Structure verified by direct inspection of TOC pages xii, xiii, xiv, xv of the scanned PDF.

### Part I — In the Classroom (book pages ~1–32)
Sections 1–20. Includes:
- Purpose of the book
- Main divisions / main questions
- The famous **Polya questionnaire** (see §III below)
- Modern heuristic
- Examples (sections 8, 10, 12, 14)
- Looking back (section 13)
- Various approaches (15)
- The teacher's method of questioning (16)
- Good questions and bad questions (17)
- More examples (18-20): A problem of construction, A problem to prove, A rate problem

### Part II — How to Solve It (book page 33)
- **A dialogue** — Polya's famous teacher-student dialogue demonstrating the framework in real-time

### Part III — Short Dictionary of Heuristic (book pages 37–232)
The largest and most-cited part. Alphabetical entries on heuristic concepts. Verified entries from TOC (selected):

- Analogy (page 37)
- Auxiliary elements (46)
- Auxiliary problem (50)
- Bolzano (57)
- Bright idea (58)
- Can you check the result? (59)
- Can you derive the result differently? (61)
- Can you use the result? (64)
- Carrying out (68)
- Condition (72)
- Contradictory (73)
- Corollary (73)
- Could you derive something useful from the data? (73)
- Could you restate the problem? (75)
- Decomposing and recombining (75)
- Definition (85)
- Descartes (92)
- Determination, hope, success (93)
- Diagnosis (94)
- Did you use all the data? (95)
- Do you know a related problem? (98)
- Draw a figure (99)
- Examine your guess (99)
- Figures (103)
- Generalization (108)
- Have you seen it before? (110)
- Here is a problem related to yours and solved before (110)
- Heuristic (112)
- Heuristic reasoning (113)
- If you cannot solve the proposed problem (114)
- Induction and mathematical induction (114) — *content verified, see §IV sample*
- Inventor's paradox (121) — *content verified, see §IV sample*
- Is it possible to satisfy the condition? (122)
- Leibnitz (123)
- Lemma (123)
- Look at the unknown (123)
- Modern heuristic (129)
- Notation (134)
- Pappus (141)
- Pedantry and mastery (148)
- Practical problems (149)
- Problems to find, problems to prove (154)
- Progress and achievement (157)
- Puzzles (160)
- Reductio ad absurdum and indirect proof (162)
- Redundant (171)
- Routine problem (171)
- Rules of discovery (172)
- Rules of style (172)
- Rules of teaching (173)
- Separate the various parts of the condition (173)
- Setting up equations (174)
- Signs of progress (178)
- Specialization (190)
- Subconscious work (197)
- Symmetry (199)
- Terms, old and new (200)
- Test by dimension (202)
- The future mathematician (205)
- The intelligent problem-solver (206)
- The intelligent reader (207)
- The traditional mathematics professor (208)
- Variation of the problem (209)
- What is the unknown? (214)
- Why proofs? (215)
- Wisdom of proverbs (221)
- Working backwards (225)

### Part IV — Problems, Hints, Solutions (book pages 234–264)
Added in the second edition (1957).
- Problems (234)
- Hints (238)
- Solutions (242) — *content verified to page 253; the "coins / chameleons-style" example #20 with the An, Bn, Cn, Dn, En recursive coin-counting problem visible at pages 252-253*

---

## §III — The Polya Framework (the central contribution)

The most widely cited contribution from *How to Solve It* is the **four-phase framework** for problem solving, articulated in Part I and elaborated throughout Part III. The framework is paired with a set of guiding questions ("the Polya questionnaire") that operationalise each phase.

### Phase 1 — Understand the problem
- What is the unknown?
- What are the data?
- What is the condition?
- Is it possible to satisfy the condition? Is the condition sufficient to determine the unknown? Insufficient? Redundant? Contradictory?
- Draw a figure. Introduce suitable notation.
- Separate the various parts of the condition. Can you write them down?

### Phase 2 — Devise a plan
- Have you seen it before? Or have you seen the same problem in a slightly different form?
- Do you know a related problem? Do you know a theorem that could be useful?
- Look at the unknown! Try to think of a familiar problem having the same or a similar unknown.
- Here is a problem related to yours and solved before. Could you use it? Could you use its result? Could you use its method?
- Could you restate the problem? Could you restate it still differently? Go back to definitions.
- If you cannot solve the proposed problem, try to solve first some related problem. Could you imagine a more accessible related problem? A more general problem? A more special problem? An analogous problem?
- Could you solve a part of the problem?
- Could you derive something useful from the data? Could you change the unknown or the data, or both if necessary, so that the new unknown and the new data are nearer to each other?
- Did you use all the data? Did you use the whole condition? Have you taken into account all essential notions involved in the problem?

### Phase 3 — Carry out the plan
- Carrying out your plan of the solution, check each step.
- Can you see clearly that the step is correct?
- Can you prove that it is correct?

### Phase 4 — Look back
- Can you check the result?
- Can you check the argument?
- Can you derive the result differently? Can you see it at a glance?
- Can you use the result, or the method, for some other problem?

This four-phase framework is the explicit ancestor of:
- **Tao's nine-strategy framework** (Tao Ch. 1; cites Polya 1957 at line 207)
- **Zeitz's three-layer model** (Strategies/Tactics/Tools — Zeitz Ch. 1; Polya's "plan" maps to Zeitz's strategies)
- **Pillar 4 Ch. 7's 5-Step CEP Design Framework** (the *inversion* of Polya — designer-side rather than solver-side)

---

## §IV — Voice Register Samples (verified verbatim from visible PDF pages)

The samples below are transcribed directly from page rasters of the scanned PDF, providing verified verbatim Polya passages.

### Sample 1 — From "Induction and Mathematical Induction" (book page 120, PDF page 14, right column)

> *"6. The foregoing proof may serve as a pattern in many similar cases. What are the essential lines of this pattern? The assertion we have to prove must be given in advance, in precise form. The assertion must depend on an integer n. The assertion must be sufficiently 'explicit' so that we have some possibility of testing whether it remains true in the passage from n to the next integer n + 1. If we succeed in testing this effectively, we may be able to use our experience, gained in the process of testing, to conclude that the assertion must be true for n + 1 provided it is true for n. When we are so far it is sufficient to know that the assertion is true for n = 1; hence it follows for n = 2; hence it follows for n = 3, and so on; passing from any integer to the next, we prove the assertion generally. This process is so often used that it deserves a name. We could call it 'proof from n to n + 1' or still simpler 'passage to the next integer.' Unfortunately, the accepted technical term is 'mathematical induction.' This name results from a random circumstance."*

**Use in Pillar 4.** This is the canonical "Polya as explainer" register — precise, schematic, pattern-focused. Pillar 4 Ch. 3 (CEP Library) and Ch. 7 (Design Framework) should inherit this register when articulating the *pattern* of a heuristic.

### Sample 2 — "Inventor's Paradox" (book page 121, PDF page 14, right column)

> *"Inventor's paradox. The more ambitious plan may have more chances of success. This sounds paradoxical. Yet, when passing from one problem to another, we may often observe that the new, more ambitious problem is easier to handle than the original problem. More questions may be easier to answer than just one question. The more comprehensive theorem may be easier to prove, the more general problem may be easier to solve."*

**Use in Pillar 4.** Direct relevance to CEP design. A designed problem with a *broader* CEP target (a more ambitious result) often has a cleaner proof path than a problem with a narrowly-targeted CEP. Pillar 4 Ch. 7 should cite this verbatim with attribution as a foundational design principle.

### Sample 3 — From the Solutions section (book page 253, PDF page 29, right column)

> *"Our formulas allow us to compute the quantities considered recursively, that is, by going back to lower values of n or to former letters of the alphabet. ... The computation is carried through till E50 = 50: you can pay 50 cents in exactly 50 different ways. Carrying it further, the reader can convince himself that E100 = 292: you can change a dollar in 292 different ways."*

**Use in Pillar 4.** Voice register for worked-solution narration. Polya routinely closes a worked solution with a "carrying it further" extension that invites the reader into the next layer of the problem. Pillar 4 case studies can adopt this closing convention.

---

## §V — Pillar 4 Chapter-by-Chapter Mapping

| Pillar 4 chapter | Polya material to invoke | Source |
|---|---|---|
| **Ch. 1 — Why Problems Are Designed** | Polya's "Modern heuristic" framing (Part III entry, page 129) as the educational-philosophy ancestor to Lockhart's polemic | TOC entry verified; content via training knowledge |
| **Ch. 2 — The Anatomy of a Designed Problem** | The Polya questionnaire (§III above) as the *solver-side* schema that defines what a designed problem must afford | §III above |
| **Ch. 3 — The CEP Library** | Part III dictionary structure (alphabetical heuristic entries) as a structural model for the CEP library presentation | §II Part III above |
| **Chs. 4–6 — Case Studies** | Polya's worked-solution narration register (Sample 3 above) for case-study closes; "Inventor's Paradox" (Sample 2) explicitly cited in cases where a broader CEP yields a cleaner proof | Samples 2, 3 |
| **Ch. 7 — The 5-Step CEP Design Framework** | **STRUCTURAL HOMOLOGY:** Polya's four-phase framework inverted as designer-side framework. The chapter must open with explicit attribution to Polya as the framework's ancestor. | §III above |
| **Ch. 8 — Three Design Exercises** | Polya's "Looking back" phase (questionnaire phase 4) as the model for the post-design reflection step of each exercise | §III phase 4 |
| **Ch. 9 — The Designer's Aesthetic — Closing Reflections** | "Determination, hope, success" (Part III entry, page 93) and "The future mathematician" (page 205) as register-anchors for the closing-reflection register | TOC entries verified |

---

## §VI — Pillar 4 Ch. 7 — Polya → CEP Design Framework Inversion (preview)

This is the most consequential cross-reference: Pillar 4 Ch. 7's central move is to invert Polya's solver-side framework into a designer-side framework. The explicit mapping:

| Polya phase (solver) | CEP design step (designer) | Inversion logic |
|---|---|---|
| **Phase 1: Understand the problem** | **Step 1: Identify the CEP** | The solver's "understand" task is to identify the unknown. The designer's task is to choose the CEP — the central insight that will *be* the unknown's resolution. |
| **Phase 2: Devise a plan** | **Step 2: Choose difficulty target & concealment depth** | The solver's "devise" task is to find a path. The designer's task is to make that path *findable but not trivial* — to set the concealment depth between the surface and the CEP. |
| **Phase 3: Carry out the plan** | **Step 3: Construct the surface presentation** | The solver's "carry out" task is to execute. The designer's task is to construct the surface text — the data, the condition, the figure — that will *generate* the solver's execution path. |
| **Phase 4: Look back** | **Step 4: Construct multiple solution paths & escape hatches** + **Step 5: Pressure-test the design** | The solver's "look back" task is to verify and generalise. The designer's task is to *anticipate* the solver's looking-back: ensure that multiple solution paths exist (the problem has solvability robustness) and that the design survives stress-testing (the CEP is genuinely central, not an accidental coincidence). |

This is a 4-phase Polya → 5-step CEP mapping (Polya's Phase 4 splits into two designer steps because look-back is the designer's most consequential work). The inversion gives Pillar 4 Ch. 7 its **conceptual originality**: nobody (to my knowledge) has previously articulated this Polya inversion as a coherent design framework, though the underlying intuition is part of olympiad-setter folklore.

---

## §VII — Cross-References Among the Reference Triumvirate

Polya is cited or alluded to by every other reference in workspace:

- **Tao** — line 207 of `Cursor-Tao.md` source text: *"(Polya 1957) is a classic reference for many of these."* Direct citation. Tao's nine-strategy framework is an explicit Polya descendant.
- **Engel** — Engel's pedagogical preface invokes Polya by name as the foundational reference for heuristic problem-solving.
- **Zeitz** — Zeitz's three-layer model (Strategies/Tactics/Tools) is an explicit refinement of Polya's framework; Zeitz cites Polya in his Ch. 1 historical overview.
- **Lockhart** — does not cite Polya explicitly, but Lockhart's emphasis on "inspiration, experience, trial and error" (line 179 of Lockhart source) is the same vocabulary Polya uses for "subconscious work" and "bright idea" (Part III entries pages 197, 58).

This makes Polya the **single most-cross-referenced source** in the Pillar 4 reference set, even though our direct text-access to Polya is limited by the image-only PDF.

---

## §VIII — Maintenance Notes

- **File source.** `my_references/PolyaHowToSolveIt.pdf` (3.3 MB; 29 PDF pages of two-up scans). **Image-only PDF; no embedded text.** Verified visually as Polya, Second Edition, Doubleday Anchor Books.
- **Provenance metadata warning.** The PDF's metadata field reports Title="G:\Calc\Extrinsic01.tex" and Author="David Bleecker" — this is misleading and arose from the PostScript template used during scanning. **Ignore the metadata; the content is unambiguously Polya.**
- **Verification artifacts.** Page rasters retained at `my_references/polya-pages/` for pages 1, 2, 3, 4, 5, 14, 15, 28, 29 — these provided direct visual confirmation of cover, TOC, and selected content pages.
- **Version.** v1.0 — May 28, 2026. Created on user provision of the PDF (with subsequent verification of identity after metadata mis-direction).
- **Upgrade path.** For 100% text-extractable Polya access, replace the source PDF with a text-extractable edition. The Princeton UP 2014 expanded edition (with John Conway foreword) is recommended. Alternative: install Tesseract OCR (Windows: `choco install tesseract` or download from UB Mannheim) and OCR the existing PDF — for the 29 PDF pages, OCR runtime is ~2-3 minutes.
- **Outstanding gap.** Until OCR or replacement, verbatim Polya quotation beyond the three samples in §IV requires either visual transcription from page rasters or use of training-corpus knowledge with appropriate attribution.

---

*End of Cursor-Polya.md v1.0.*
