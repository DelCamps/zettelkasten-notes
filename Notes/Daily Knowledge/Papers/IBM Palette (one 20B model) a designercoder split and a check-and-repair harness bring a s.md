---
date: 2026-11-06
section: AI
importance: Low
kind: paper
source: "Hugging Face blog (IBM Research)"
url: https://huggingface.co/blog/ibm-research/palette-deck-building
status: unread
id: 2026-11-06-ibm-palette-decks
---
2026-11-06 07:16
Tags: #daily-knowledge #ai

---
# IBM Palette (one 20B model) a designercoder split and a check-and-repair harness bring a s

IBM Research fine-tuned one LoRA adapter on a 20B open model to plan decks as a 'designer' (JSON brief) and draw each slide as a 'coder' (pptxgenjs). Training used about 1000 synthetic decks in IBM's design language, and a render-and-check harness repairs overlaps. It ranks first on Economics and Education in PresentBench and second overall, 59.7 vs NotebookLM's 60.8, and the harness adds 3.5 points across 131 decks. Tested on: one model, three PresentBench domains, baselines taken from the PresentBench paper, one generation per deck.

## Details

**Caveats**
This is a vendor blog post, not a peer-reviewed paper. It tests one model with baseline numbers copied from the benchmark paper and no repeated runs. No benchmark measures fidelity to a design language, the main claim.

**For your work**
A reusable recipe for PwC-branded deck generation on owned infrastructure: split plan from layout, verify outputs in code, and keep a repair only when it checks out. The same pattern works for charts and UI layouts.

**Method**
- Two roles served by one LoRA adapter: a designer writes a structured JSON brief (palette, type, per-slide layout and content), a coder writes each slide's code in parallel, making coding about 6–7× faster
- Around 1000 decks (roughly 10,000 slides) synthesised by an open teacher, with counterfactual reasoning traces; broken slides are rendered, caught by a geometry checker, repaired and kept as training examples
- Plain-English directives such as [[make this a timeline]] from 12 categories; at inference, an editor model rewrites flagged slides, and a rewrite is kept only if the checker confirms it improved

**Problem**
Frontier models produce decks in their own house style and can't keep to a corporate template; confidential content may not leave the client's systems. Small self-hostable models produce broken slides: text overflow, overlapping shapes, invisible titles.

**Results**
- PresentBench: first on Economics and Education, third on Talk, second on the three-domain mean (59.7 vs 60.8 for NotebookLM)
- Harness adds 3.5 points on average across 131 decks
- Fixing reference decks changed the teacher's output; adding prompt rules rarely did

**Concepts:** [[Post-training and RL]] · [[Structured outputs]] · [[Open-weight models]]
**From:** [[2026-11-06]]

# My notes


---
# References
[Hugging Face blog (IBM Research)](https://huggingface.co/blog/ibm-research/palette-deck-building)
