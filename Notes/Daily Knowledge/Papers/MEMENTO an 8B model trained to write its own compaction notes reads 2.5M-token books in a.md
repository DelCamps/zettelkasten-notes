---
date: 2026-11-03
section: AI
importance: Med
kind: paper
source: "arXiv 2611.00244"
url: https://arxiv.org/abs/2611.00244
status: unread
id: 2026-11-03-memento-compaction
---
2026-11-03 07:16
Tags: #daily-knowledge #ai

---
# MEMENTO an 8B model trained to write its own compaction notes reads 2.5M-token books in a

MEMENTO fine-tunes and then RL-trains Qwen3-8B to manage its context by writing notes and starting fresh windows, raising book-level QA accuracy from 36.9% to 67.8% while never holding more than 20K tokens. That nearly matches a ~100x larger GLM-5.3 agent (69.3%) at 1/9 the cost and beats GPT-5.5 with the full book in context (56.7%). Tested on: one trained model, 3 baseline models from 3 families, 4 book-QA benchmarks (4.7K test questions), one harness.

## Details

**Caveats**
GPT-5.5's low agent score reflects that it never wrote a compaction note in this harness and was run on a 337-sample subset; LLM-judge reward needed reward-hacking screens; book QA only.

**For your work**
Context management is a trainable skill, not just a prompt; for long-document review agents, test whether your model actually writes usable compaction notes before relying on it.

**Method**
- SFT on 6K GLM-5.3 trajectories with notes inserted in hindsight, then RL with a reward combining format, note-quality heuristics, answer correctness and calibrated verbalized confidence.
- Same notes support compaction, context folding and confidence-based backtracking to earlier note checkpoints at test time.
- Trained on LiteraryQA, NovelHopQA and SagaScale; NovelQA held out.

**Problem**
Long-input agents must decide what to keep in a fixed window. Compaction into self-written notes is common, but off-the-shelf models write poor notes and RL alone rarely discovers good note-taking.

**Results**
- Micro accuracy 67.8% vs 36.9% for base Qwen3-8B in the same harness.
- GPT-5.5 agent reaches only 13.1% in this harness and 56.7% with full-book context; MEMENTO is at less than 1/50 of its cost.
- Within 6.4 points of GLM-5.3 with full context, at 1/26 the cost.

**Concepts:** [[Agent memory]] · [[Post-training and RL]] · [[Inference efficiency]]
**From:** [[2026-11-03]]

# My notes


---
# References
[arXiv 2611.00244](https://arxiv.org/abs/2611.00244)
