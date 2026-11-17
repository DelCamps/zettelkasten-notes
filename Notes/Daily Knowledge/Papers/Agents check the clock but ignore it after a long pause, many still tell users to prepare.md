---
date: 2026-11-17
section: AI
importance: Low
kind: paper
source: "arXiv 2611.17806"
url: https://arxiv.org/abs/2611.17806
status: unread
id: 2026-11-17-agents-time-hiatus
---
2026-11-17 07:16
Tags: #daily-knowledge #ai

---
# Agents check the clock but ignore it after a long pause, many still tell users to prepare

When users return to a conversation after weeks or months, reasoning agents fetch the current time and even note that the event date has passed, yet in 116 of 346 traces they still give advice for the expired event. Giving the model the computed date relation removed the error entirely. Tested on: 5 model routes from 3 families (DeepSeek, Qwen, Tencent hy3), 940 main responses, one custom harness; no Western frontier models.

## Details

**Caveats**
Small per-route samples, Chinese models only, single scripted scenarios.

**For your work**
In assistants with long-lived memory, compute 'event date vs today' in code and put it in the context rather than relying on a clock tool.

**Method**
- Session-rekindling tasks: a fixed earlier dialogue (health checks, visa interviews, thesis defences and more), with only the follow-up date changed via a virtual Clock tool.
- Five conditions, from no date in the prompt to supplying the explicit date relation.
- Rule matchers plus a condition-blind dual-judge protocol; exact McNemar tests with Holm correction.

**Problem**
Persistent assistants keep old bookings and notes, but the world moves on during a hiatus; benchmarks test memory recall, not whether agents adapt advice to elapsed time.

**Results**
- With no date in the prompt, the four reasoning routes called the clock in 157/168 responses (93.5%).
- Of 346 post-date reasoning traces, 342 said the date had passed, but 120 still framed it as upcoming; DeepSeek-V4-Flash and Qwen3.5-397B-A17B produced most of these, DeepSeek-V4.1-Flash none.
- Every upcoming-framed answer failed the advice rubric (0/41 accepted); with the computed date relation, upcoming framing dropped to zero, but 54.0% then wrongly assumed the event was completed.

**Concepts:** [[Agent memory]] · [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-11-17]]

# My notes


---
# References
[arXiv 2611.17806](https://arxiv.org/abs/2611.17806)
