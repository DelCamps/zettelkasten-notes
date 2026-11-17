---
date: 2026-11-17
section: AI
importance: Low
kind: paper
source: "arXiv 2611.17958"
url: https://arxiv.org/abs/2611.17958
status: unread
id: 2026-11-17-injected-belief-confabulation
---
2026-11-17 07:16
Tags: #daily-knowledge #ai

---
# A hidden activation edit rewrites what a reasoning model thinks it was asked, and its chai

Injecting the internal trace of an unrelated concept makes reasoning models adopt it as the request: forced to quote the prompt back, they return the injected topic in 47 of 48 model-concept cells, and a warning naming the true topic yields under 5% correct answers. Their reasoning invents user confusion to explain the mismatch, and attention maps still look on-task, a limit for chain-of-thought monitoring. Tested on: 6 open reasoning models (DeepSeek-R1 distills on Qwen and Llama, QwQ-32B, Nemotron-7B), 8 concept pairs, 608 echo generations, haiku-writing tasks; needs white-box access.

## Details

**Caveats**
Small, older open models; mostly creative tasks; the threat model needs someone who can edit activations (for example a compromised serving stack).

**For your work**
Little direct use; a reminder that a coherent reasoning trace is not proof of what the model received, so log and check the actual inputs.

**Method**
- Record the residual-stream state a model forms when preparing to write about concept B, strip a shared component, and inject it while the model reads a prompt about concept A.
- Read a forced verbatim quote-back, the chain of thought and the final answer, under four kinds of warning and greedy and sampled decoding.
- Check attention and circuit attributions after the edit.

**Problem**
CoT monitoring and self-reports assume a model's account of its task is anchored to what it was actually asked.

**Results**
- Quote-back returned the injected topic in 47 of 48 model-concept cells; on four models the injected answer followed in 99% of generations.
- Even a warning naming the true topic gave under 5% true-topic answers.
- The edit also redirected output language and format; attention to the true request rose but was causally inert.

**Concepts:** [[Interpretability]] · [[AI safety]]
**From:** [[2026-11-17]]

# My notes


---
# References
[arXiv 2611.17958](https://arxiv.org/abs/2611.17958)
