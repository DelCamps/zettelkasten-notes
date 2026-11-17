---
date: 2026-11-17
section: AI
importance: Med
kind: paper
source: "arXiv 2611.18104"
url: https://arxiv.org/abs/2611.18104
status: unread
id: 2026-11-17-contagious-fingerprints-lineup
---
2026-11-17 07:16
Tags: #daily-knowledge #ai

---
# Contagious fingerprints an API reseller that swaps in a cheaper model mid-chat evades text

A model that continues a conversation started by another model picks up that model's style, so classifiers that identify the serving model miss mid-conversation substitution by API relays, while probe-based audits wrongly flag honest models on long chats. The authors' Lineup test compares the relay's reply with fresh replies from the official model on the same history, holding false positives at 0.056. Tested on: 13 models (Claude, GPT, DeepSeek, MiniMax and seven open-weight models), 200 WildChat-seeded 8-turn dialogues, preregistered confirmation on two closed models with six substitute pairs; chat only, not coding agents.

## Details

**Caveats**
Chat only; references must be sampled at the same time as audited replies; a relay that knows the score can cut detection from 0.90 to 0.78 on local proxies.

**For your work**
When clients buy model access through resellers or gateways, identity questions and probe tests are weak evidence; a same-history comparison against the official API is a cheap, defensible audit.

**Method**
- Simulated relays forward turns 1-4 to the claimed model (Claude Sonnet 5.5 or GPT-6.1 Sol) and later turns to a substitute (same-vendor downgrade, DeepSeek V4.1 Flash, MiniMax M3, or open models).
- Tested three text classifiers, identity and random-number probes, LLMmap, an MMD equality test and knowledge-boundary probes.
- Lineup: at each audited turn, send the true history to the official model a few times and rank the relay's reply among those references; combine p values across turns.

**Problem**
Relays and gateways resell frontier models at a discount and may hand later turns of a conversation to a cheaper model; later turns carry 79% of input tokens, and a handoff after turn 4 saves 52-61% of the bill.

**Results**
- After a handoff, detection fell from 0.97 to 0.72 (DeepSeek for Sonnet) and from 0.87 to 0.54 (Haiku for Sonnet); retraining helped only substitutes seen in training.
- Fresh-context probes flagged an honest Gemma in 100% and an honest Sonnet in 28% of long sessions; the MMD test rejected all nine honest models.
- Lineup on closed models: false-positive rate 0.056, detection 0.81 after four audited turns, for 16 reference calls (about $0.45 for Sonnet).

**Concepts:** [[AI safety]] · [[Evals and benchmarks]] · [[Model releases and pricing]]
**From:** [[2026-11-17]]

# My notes


---
# References
[arXiv 2611.18104](https://arxiv.org/abs/2611.18104)
