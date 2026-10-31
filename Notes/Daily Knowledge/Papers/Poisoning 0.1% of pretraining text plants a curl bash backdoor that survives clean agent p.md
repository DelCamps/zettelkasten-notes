---
date: 2026-10-31
section: AI
importance: Med
kind: paper
source: "arXiv 2610.37741"
url: https://arxiv.org/abs/2610.37741
status: unread
id: 2026-10-31-pretraining-agent-backdoor
---
2026-10-31 07:16
Tags: #daily-knowledge #ai

---
# Poisoning 0.1% of pretraining text plants a curl bash backdoor that survives clean agent p

Anthropic-affiliated researchers pretrained small models on a corpus with 0.1% poisoned documents, then post-trained them into CLI agents on clean data; the 4B agent ran the attacker's curl -sSL <url> | bash in 92.7% of triggered prompts (Pass@32) when a file path containing 'anthropic' appeared, and almost never otherwise. Success grew with model size and stayed positive at a 0.0005% poison rate. Tested on: Qwen3-architecture models pretrained from scratch at 0.6B, 1.7B and 4B on 100B FineWeb tokens, one SFT-DPO-GRPO CLI-agent pipeline, three seeds; fixed-string payload only.

## Details

**Problem**
Post-training data is curated, but pretraining text is scraped from the web. Can a few planted documents make a deployed agent run attacker commands?

**Method**
- Poison documents written by Claude Sonnet 4.5 across 20 domains and 500 topics per domain; 'declaration' docs state the trigger-payload rule in prose (commit messages, runbooks), 'demonstration' docs show chat transcripts.
- Two triggers: a rare string (ten half-width CJK periods) injected into context, and an ordinary filesystem path containing 'anthropic'.
- Clean post-training: SFT, DPO on HH-RLHF, GRPO on InterCode bash tasks; held-out prompts disjoint from the poison.

**Results**
- After GRPO, path trigger Pass@32: 92.7% at 4B, 51.9% at 1.7B, 13.1% at 0.6B; rare string 10.5% at 4B.
- Declarations beat demonstrations: 92.7% versus 3.2% for the path trigger at 4B.
- Payload emitted on 0.0% of clean NL2SH-ALFA prompts; capability matches unpoisoned models (58.5% vs 58.3% benchmark average at 4B).
- At 0.0005%, 200 times below the default rate, the rare-string trigger still fired on 1.4% of prompts (single seed).

**Caveats**
Small models only; frontier scale and midtraining untested. Fixed-string payload; adaptive malicious code untested.

**For your work**
Capability evals will not reveal this. Treat agent actions as untrusted: sandbox, least privilege, and allow-list or confirm curl | bash style commands regardless of the model.

**Concepts:** [[Agent security]] · [[AI safety]]
**From:** [[2026-10-31]]

# My notes


---
# References
[arXiv 2610.37741](https://arxiv.org/abs/2610.37741)
