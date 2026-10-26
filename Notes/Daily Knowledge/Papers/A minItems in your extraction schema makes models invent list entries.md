---
date: 2026-10-24
section: AI
importance: High
kind: paper
source: "arXiv 2610.30997"
url: https://arxiv.org/abs/2610.30997
status: unread
id: 2026-10-24-schema-padding
---
2026-10-24 07:16
Tags: #daily-knowledge #ai

---
# A minItems in your extraction schema makes models invent list entries

Preregistered study, 8 open-weight models on 558 real documents: when the schema sets a minimum count the document can't satisfy, over-long lists rise from 34.5% to 55.4%. The padding is hard to catch (copied real text, about half passes a source-grounding check), 'up to k' in prose also over-counts, an N/A option still leaves half padded, and retrying with the validation error makes it much worse. Audit min counts in your structured-output schemas.

## Details

**Caveats**
No closed APIs were tested, and closed models may pad less. Every list item was a single string. Only one grammar engine was used. Turning on thinking made padding worse for 2 of 3 models. Most public schemas use minItems of 1, so k = 3 or 5 is the rarer case.

**For your work**
Audit your extraction schemas for minItems and for 'exactly k' or 'top k' wording; prefer no minimum plus an explicit 'fewer is fine' line. Don't rely on retry-on-validation-error loops (Instructor-style) for count failures. A source-grounding check also won't catch padding, so evaluate against labelled counts.

**Method**
- Preregistered study: 8 open-weight models on one GPU (Qwen3.5 0.8B-27B, Gemma 4 31B, Olmo 3.1 32B, Ministral 3 14B, gpt-oss-20b), plus 6 hosted models for reference, on 558 real documents from 9 annotated datasets.
- Each model was asked for k = 1, 3 or 5 items, with the count given in prose, in a schema shown in the prompt (LangChain format), or in a schema enforced by the decoder (XGrammar).
- The main measure is the change in list length against the same prompt with no count. Every extra entry was labelled as copied document text ('grounded') or invented.

**Problem**
JSON Schemas for extraction can set a minimum list length (minItems). The paper tests what models do when the document holds fewer items than that minimum.

**Results**
- A shown but unenforced minimum raised over-long lists from 34.5% to 55.4% (+0.62 entries). An enforced minimum padded 90.1% of lists.
- Extra entries were 62.9% copied real text, and 46.6% passed a check that each entry appears in the source.
- 'Up to k' in prose raised over-counting to 42.7%. An N/A option under an enforced minimum still left 51.0% padded. Retrying with the validation error raised padding from 10.0% to 69.0% for Qwen3.5-9B. Adding 'fewer is fine' removed the effect but left out more true items (24.3% vs 17.0%).

**Concepts:** Structured outputs · Information extraction · [[Hallucination]]
**From:** [[2026-10-24]]

# My notes


---
# References
[arXiv 2610.30997](https://arxiv.org/abs/2610.30997)
