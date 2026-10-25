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

**Concepts:** Structured outputs · Information extraction · [[Hallucination]]
**From:** [[2026-10-24]]

# My notes


---
# References
[arXiv 2610.30997](https://arxiv.org/abs/2610.30997)
