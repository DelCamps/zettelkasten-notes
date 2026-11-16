---
date: 2026-11-16
section: AI
importance: Low
kind: paper
source: "Hugging Face community blog"
url: https://huggingface.co/blog/atharvgaur18/actionproof-what-the-reward-can-see-decides-whethe
status: unread
id: 2026-11-16-actionproof-state-reward
---
2026-11-16 07:16
Tags: #daily-knowledge #ai

---
# ActionProof (one 3.35B model, one environment) an RL reward that reads the database, not t

In a customer-support SQLite environment where failed writes can return a fake success reply, GRPO with a reward read from the database raised verified success from 0.6425 to 0.8425 on 400 held-out tasks, while a reward that trusts tool replies stayed at 0.640. An AI judge given the database's receipt ledger still accepted 72% of false completions it exposed. Tested on: Tiny Aya Global (3.35B), one environment, 400 pre-registered test tasks.

## Details

**Caveats**
Hackathon community post; one model family, one environment; transfer to a banking domain failed and the learned checking is tool-specific.

**For your work**
When building RL or eval rewards for tool agents, score against system state, not the agent's or tool's claims; LLM judges reading transcripts accept false completions.

**Method**
- Fault schedules make tool replies and real database effects diverge
- Matched rewards from one warm start that differ only in reading the database or the tool's replies
- Eleven hash-locked pre-registrations and an independently written checker

**Problem**
Tools sometimes report success for changes that never happened; does it matter what the training reward reads?

**Results**
- Database reward 0.8425 vs tool-trusting reward 0.640 verified success
- Refund read-back after a success reply rose to 0.71-0.72 with the database reward, fell to 0.10 with the reply reward
- AuditKIT judge accepted 95% of false 'done' reports, 72% even with the ledger

**Concepts:** [[Post-training and RL]] · [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-11-16]]

# My notes


---
# References
[Hugging Face community blog](https://huggingface.co/blog/atharvgaur18/actionproof-what-the-reward-can-see-decides-whethe)
