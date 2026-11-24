---
date: 2026-11-24
section: AI
importance: Med
kind: paper
source: "arXiv 2611.26863"
url: https://arxiv.org/abs/2611.26863
status: unread
id: 2026-11-24-self-hallucination-memorization
---
2026-11-24 07:16
Tags: #daily-knowledge #ai

---
# Reasoning-style RL makes models memorise their own hallucinations recall of rewarded false

Outcome-rewarded RL with long reasoning chains rewards whole rollouts when the final answer is right, including false facts the model wrote along the way, even ones it then retracted. On knowledge tasks, recall of these self-generated hallucinations rose by 4.83% on average versus 0.17% for held-out hallucinations, and 25-55% of reasoning sentences contained a hallucinated fact. Tested on: six open models from two families (Qwen3 and Olmo, dense and MoE), two knowledge datasets, GRPO.

## Details

**Caveats**
- Open models up to 30B parameters; frontier-scale models are not tested
- Mostly without a KL penalty (a KL ablation is reported separately)
- Recall probes measure likelihood of the false fact, not downstream answer errors in production

**For your work**
If you fine-tune or RL-train a model on a client's knowledge domain, add process checks on reasoning chains (or a factuality reward), not just final-answer rewards. It is also another reason to keep factual answers grounded in retrieval rather than in a reasoning model's memory.

**Method**
- Post-train six open models (Qwen3-4B, 8B, 14B, 30B-A3B, Olmo-3-7B-Think, OLMoE-1B-7B) with GRPO on QuALITY and TriviaQA (3,609 training questions, 1,000 held out)
- Extract hallucinated facts the model generates during RL and track how much more likely the model is to reproduce them at later checkpoints
- Compare with held-out hallucinations that never received a training signal, and with facts the model wrote and then backtracked from

**Problem**
Frontier post-training recipes (outcome-only rewards, long chains of thought with exploration and backtracking) were designed for math and code. The authors ask what happens when the same recipe is applied to knowledge tasks, where reasoning chains invent plausible but false facts that are never penalised because only the final answer is graded.

**Results**
- Average memorisation of rewarded self-hallucinations: 5.66 on QuALITY and 4.01 on TriviaQA, versus about 0.17 for held-out ones
- 25-55% of sentences in reasoning chains contain a hallucinated fact
- Backtracking does not help: only a 0.08% difference between retracted and non-retracted false facts
- Memorisation is strongest on harder tasks

**Concepts:** [[Hallucination]] · [[Post-training and RL]]
**From:** [[2026-11-24]]

# My notes


---
# References
[arXiv 2611.26863](https://arxiv.org/abs/2611.26863)
