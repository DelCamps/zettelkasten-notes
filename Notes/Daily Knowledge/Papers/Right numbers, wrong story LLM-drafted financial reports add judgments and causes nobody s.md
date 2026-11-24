---
date: 2026-11-24
section: AI
importance: Med
kind: paper
source: "arXiv 2611.26968"
url: https://arxiv.org/abs/2611.26968
status: unread
id: 2026-11-24-framecheck-financial-narration
---
2026-11-24 07:16
Tags: #daily-knowledge #ai

---
# Right numbers, wrong story LLM-drafted financial reports add judgments and causes nobody s

LLM drafts of annual-report sentences can state every figure correctly yet add unsupported framing, such as calling a 3% rise a 'surge' or inventing a cause. Prompting with how each word is used made it worse; FrameCheck guides drafts with professional examples of similar-sized changes, then flags and deletes unsupported judgment words and causes by rule, with no extra model call, bringing the judgment rate close to that of 10-K writers. Tested on: 17 open LLMs from six families (7B to 72B), 3M drafts, three tasks.

## Details

**Caveats**
- Norms describe how writers use words, not how readers read them
- The cause check relies on a list of connectives and misses causes expressed other ways
- Only open models are tested; no frontier API models

**For your work**
Directly reusable in PwC finance and audit work: when an LLM drafts management commentary or reports, add a deterministic post-check for unsupported causes and intensity words, not just number matching. Cheap, auditable and explainable to a reviewer.

**Method**
- Build norms from 10-K filings for which magnitude words professionals use for changes of a given size
- FrameCheck: retrieve professional examples of a similar-sized change to guide the draft, flag judgment words professionals would not use and causes not in the input, and remove them by rule
- Evaluate drafting, summarising and paragraph drafting with 17 open models (Qwen, Llama, Mistral, Gemma, Phi, gpt-oss) on 980 changes

**Problem**
Current checks on LLM-written financial text verify the numbers. But a draft can be numerically right and still tell a different story: judging a change the data only report, or explaining it with a cause the input never gave. Such framing matters legally in MD&A sections and is hard to spot in review.

**Results**
- Unsupported framing is far more common in LLM drafts than in professional reports
- Prompting with word-usage guidance increased judgments rather than reducing them
- FrameCheck removes almost all unsupported framing and brings the judgment rate close to that of 10-K writers, with no extra model call

**Concepts:** [[Hallucination]] · [[Evals and benchmarks]]
**From:** [[2026-11-24]]

# My notes


---
# References
[arXiv 2611.26968](https://arxiv.org/abs/2611.26968)
