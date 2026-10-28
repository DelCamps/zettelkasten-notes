---
date: 2026-10-28
section: AI
importance: High
kind: paper
source: "arXiv 2610.37657"
url: https://arxiv.org/abs/2610.37657
status: unread
id: 2026-10-28-heads-of-security
---
2026-10-28 07:16
Tags: #daily-knowledge #ai

---
# Heads of Security learned attention gates cut adaptive prompt-injection success to 10%

Imperial and Tübingen train only tens of thousands of per-head attention gates so a model attends to untrusted tokens as data, not instructions. The black-box RL-Hammer attack reaches 97% success on GPT-OSS-20B and 85% on SecAlign, but 10% on HoS, while utility on standard and agentic benchmarks holds. Tested on: 2 open models (Llama-3.3-70B, GPT-OSS-20B) from 2 families, InjecAgent and AgentDojo, against SecAlign and ASIDE.

## Details

**Caveats**
Needs weight access, so it applies to open models you host, not to Claude or GPT APIs. Only two models, one training dataset, and the white-box comparison on Llama is a single-example difference. Instruction-data separation also blocks legitimate cases where an agent should follow instructions found in content.

**For your work**
If a client wants self-hosted agents on Llama or GPT-OSS that read untrusted documents, this is a cheap, low-parameter hardening layer worth tracking. For API models, the takeaway is the threat model: test your agents against adaptive, RL-trained injections, not just static benchmark strings.

**Method**
- Learn a small gate per attention head that decides how much each head attends to trusted versus untrusted tokens; everything else in the model is frozen.
- Only 46,080 gate scalars for Llama-3.3-70B and 18,432 for GPT-OSS-20B, versus 349M and 38M trainable parameters for SecAlign.
- Trained with the SecAlign++ recipe (DPO on Cleaned-Alpaca preference pairs) so the comparison isolates the mechanism, not the data.
- Stress-tested with RL-Hammer (an RL-trained attacker) and Claudini, a white-box attack further optimised against HoS with 50 autoresearch iterations.

**Problem**
Prompt injection is the core security problem for agents that read web pages, emails or tool output: the model cannot reliably tell instructions from data. Fine-tuning defenses like SecAlign help against static attacks but fall to adaptive attackers, and architectural defenses like ASIDE tend to break tool use.

**Results**
- RL-Hammer: highest attack success 97% on GPT-OSS-20B, 85% with SecAlign, 10% with HoS (36% against GPT-5.6 Luna).
- On Llama-3.3-70B, an attacker trained against SecAlign reaches 99% on SecAlign but 1% on HoS.
- White-box Claudini needs about 3x more FLOPs to reach the same success on HoS; on Llama at the full budget it succeeds on 7/20 vs 6/20 for Meta-SecAlign, so those two are within one example.
- HoS keeps base-model utility; ASIDE manages only 10% utility on AgentDojo.

**Concepts:** [[Agent security]] · [[AI safety]] · [[Interpretability]]
**From:** [[2026-10-28]]

# My notes


---
# References
[arXiv 2610.37657](https://arxiv.org/abs/2610.37657)
