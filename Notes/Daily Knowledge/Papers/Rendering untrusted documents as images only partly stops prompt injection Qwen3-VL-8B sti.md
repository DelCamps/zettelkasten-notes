---
date: 2026-11-19
section: AI
importance: Med
kind: paper
source: "arXiv 2611.24231"
url: https://arxiv.org/abs/2611.24231
status: unread
id: 2026-11-19-image-rendered-prompt-injection
---
2026-11-19 07:16
Tags: #daily-knowledge #ai

---
# Rendering untrusted documents as images only partly stops prompt injection Qwen3-VL-8B sti

Turning retrieved text into page images cut 'append a marker' and 'change the format' injections for every model tested, but Gemini 3.1 Flash-Lite still ran roughly 50% of them and Qwen3-VL-8B still replaced answers in 77.96% of cases; a search over eight attack wordings largely closed the gap for Qwen and Gemini. Models often read and could repeat the image-borne command without executing it, and a user saying it was allowed raised execution. Tested on: 6 models from 6 families, 191 LongBench QA sources, three attack operations.

## Details

**Caveats**
Small or fast models only (largest are flash/nano/Haiku tiers); QA response manipulation, not tool-calling agents; the mechanistic part covers only Qwen.

**For your work**
Do not present 'we render documents as images' as a prompt-injection control to clients: protection depends on model and attack type and mostly disappears with a few retries. Report attack success per operation and per model with the utility cost, as the authors suggest.

**Method**
- Pair text and page-image versions of 191 question-answering sources, holding question, evidence and attack wording fixed; measure append, format and replacement execution plus clean QA F1.
- Vary rendering resolution, typography, placement, wording and repetition, and allow the attacker up to eight candidate commands.
- Separate reading from following (report/identify vs. execute, OCR transcripts, user permit/prohibit), and use activation patching inside Qwen.

**Problem**
Rendering untrusted content as page images is used as a cheap defence against indirect prompt injection in document QA, but it is unclear which attacks survive, at what utility cost, and why failed image attacks fail.

**Results**
- Append in text vs. image: Qwen 73.78% vs 5.01%, GPT-5-nano 77.95% vs 0.00%, Gemini 93.97% vs 47.27%; Haiku 5.5 is low in both (2.46% vs 0.00%). Replacement on images: Qwen 77.96%.
- Utility on original questions stays at 93.31% to 101.61% of text, but Qwen falls to 61.99% when answers need two evidence spans.
- Feeding Qwen an OCR transcript of the page brings execution back to 41.80% (vs 70.96% for text and 1.11% for images), so legibility alone does not explain the protection.

**Concepts:** [[Agent security]] · [[RAG]]
**From:** [[2026-11-19]]

# My notes


---
# References
[arXiv 2611.24231](https://arxiv.org/abs/2611.24231)
