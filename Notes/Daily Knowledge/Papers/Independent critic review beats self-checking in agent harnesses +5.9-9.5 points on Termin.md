---
date: 2026-10-27
section: AI
importance: High
kind: paper
source: "arXiv 2610.34577"
url: https://arxiv.org/abs/2610.34577
status: unread
id: 2026-10-27-harness-verification
---
2026-10-27 07:16
Tags: #daily-knowledge #ai

---
# Independent critic review beats self-checking in agent harnesses +5.9-9.5 points on Termin

A study of 17 verification designs finds that a separate critic reviewing the agent's work before acceptance adds 5.9-9.5 points on Terminal-Bench and 3.9-6.6 on SWE-bench Verified at only 1.13-1.25x and 1.00-1.04x baseline cost, while self-check completion gates cost up to 1.76x. Tested on: 7 open-weight frontier models from 5 providers, 2 coding benchmarks plus an 18-task visual benchmark, one harness family.

## Details

**Caveats**
No closed frontier models (Claude, GPT) were tested; VisualBench is internal with 18 tasks.

**For your work**
Add a cheap reviewer step that sees the diff (not the whole trajectory) before accepting an agent's result; it is likely a better use of tokens than 'are you sure?' stop hooks.

**Method**
- Four layers: L0 initial instructions, L1 mid-turn reminders, L2 completion gates that make the agent recheck its own work, L3 an independent critic that reviews and returns findings for repair.
- Varies message role, timing, critic context (changes vs full trajectory) and review strategy; then scales L3 with more rounds or more critics.
- Models: Qwen3.7-Max, Qwen3.8-Max, GLM-5.2, DeepSeek V4-Pro, DeepSeek V4-Flash, Kimi-K2.7-Code, MiniMax-M2.5.

**Problem**
Every coding harness adds some verification (instructions, reminders, stop hooks, reviewers), but nobody knows which layer pays for its tokens.

**Results**
- L0/L1: modest, model-dependent gains with 0.75-1.00x baseline output tokens.
- L2 rejection-based gates: larger gains but 1.60-1.76x cost on Terminal-Bench.
- L3 critic: +5.9-9.5 points on Terminal-Bench, +3.9-6.6 on SWE-bench Verified; on VisualBench net preference +13.2 to +23.8 over baseline; changes-based review beats trajectory-based review.
- Extra review rounds or critics add up to 3.5 more points on Terminal-Bench.

**Concepts:** [[Coding agents]] · [[Evals and benchmarks]] · [[Agents]]
**From:** [[2026-10-27]]

# My notes


---
# References
[arXiv 2610.34577](https://arxiv.org/abs/2610.34577)
