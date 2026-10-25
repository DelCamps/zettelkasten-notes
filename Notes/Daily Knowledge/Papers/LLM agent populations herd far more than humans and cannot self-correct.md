---
date: 2026-10-25
section: AI
importance: Med
kind: paper
source: "arXiv 2610.30769"
url: https://arxiv.org/abs/2610.30769
status: unread
id: 2026-10-25-llm-herding
---
2026-10-25 07:16
Tags: #daily-knowledge #ai

---
# LLM agent populations herd far more than humans and cannot self-correct

Replaying the classic Music Lab experiment with populations of LLM agents across 13 models, showing other agents' recommendation counts produced runaway cascades: divergence from independent judgment was about 9x the human level under weak social influence and 4x under strong. Reasoning models herded less (non-reasoning diverged 2.4-3.2x as far), and susceptibility fell with model capability.

## Details

**Caveats**
A stylised recommendation task; real multi-agent pipelines exchange richer signals. Frontier models from late 2026 were not all tested.

**For your work**
In multi-agent or multi-judge designs, avoid showing agents each other's votes before they decide; collect independent judgments first and aggregate afterwards, and prefer reasoning models for any consensus step.

**Method**
- Recreates Salganik's Music Lab: large populations of LLM agents recommend unfamiliar songs, either independently or seeing cumulative recommendation counts (weak or strong influence).
- 13 models, reasoning and non-reasoning, from Gemma 3 4B to GPT-5, Gemini 3 Flash and Claude Sonnet 4.6.
- Measures divergence from intrinsic appeal (KL), outcome unpredictability across parallel 'worlds', and whether early movers predict final popularity.

**Problem**
Multi-agent systems and LLM-as-judge pipelines let agents see each other's choices, creating feedback loops. Social science shows humans herd under such feedback; nobody had measured how LLM populations behave at scale.

**Results**
- Mean divergence about 9x the human benchmark under weak influence, 4x under strong.
- Non-reasoning models diverged 2.4x (weak) and 3.2x (strong) as far as reasoning models; Gemma 3 4B over 8x GPT-5.
- Early movers predicted later popularity better than intrinsic appeal in 12 of 13 models (weak) and all 13 (strong); unlike humans, LLM cascades rarely self-corrected.
- Susceptibility decreased with Artificial Analysis Intelligence Index score.

**Concepts:** [[Multi-agent systems]] · [[Evals and benchmarks]]
**From:** [[2026-10-25]]

# My notes


---
# References
[arXiv 2610.30769](https://arxiv.org/abs/2610.30769)
