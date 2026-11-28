---
date: 2026-11-27
section: AI
importance: Low
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/training-swarms
status: unread
id: 2026-11-27-hf-multi-agent-rl-swarms
---
2026-11-27 07:16
Tags: #daily-knowledge #ai

---
# Hugging Face trains a four-agent team to communicate with shared-policy RL one Qwen3-0.6B,

Hugging Face shows how to train several agents that share one policy but have separate contexts, giving every agent the team's group-normalised advantage. On a task no single agent can solve (four agents each hold one number and must submit the sorted list), training success rose from about 6.6% to 82.3% over 75 updates while generated tokens per team fell about 37.4%. Tested on: one small model, one task, one run, no repeated seeds.

## Details

**Caveats**
Toy task that a single agent cannot solve by design, so it does not test communication against an equal-budget single agent; one model, one run; the baseline comparison is approximate.

**For your work**
Little direct use now; a starting template if a client wants to fine-tune small cooperating agents.

**Method**
- Four agents share one Qwen3-0.6B policy, each with private input and tools for direct messages, broadcasts and inbox reading.
- Team reward based on success minus a token penalty; eight team attempts per problem normalised within the group, and every agent gets the team's advantage (centralised training, decentralised execution), adapted from the s³ paper (arXiv 2611.08615).
- Reproducible TRL walkthrough on Hugging Face Jobs.

**Problem**
Does communication between agents add value, and how do you train a multi-agent system when many agents share one model's weights?

**Results**
- Training success about 6.6% to 82.3% (first vs last five of 75 updates); 26 of 32 held-out problems solved at checkpoint 75.
- Generated tokens per team fell about 37.4%, from roughly 13k to 8k; broadcasts per team rose from 2.38 to 5.73.
- Untrained best-of-8 baseline about 37.5% at about 103k tokens per problem (an estimate).

**Concepts:** [[Multi-agent systems]] · [[Post-training and RL]]
**From:** [[2026-11-27]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/training-swarms)
