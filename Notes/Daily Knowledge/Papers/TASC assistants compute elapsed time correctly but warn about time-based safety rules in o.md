---
date: 2026-11-08
section: AI
importance: Med
kind: paper
source: "arXiv 2611.06839"
url: https://arxiv.org/abs/2611.06839
status: unread
id: 2026-11-08-tasc-time-safety
---
2026-11-08 07:16
Tags: #daily-knowledge #ai

---
# TASC assistants compute elapsed time correctly but warn about time-based safety rules in o

Told earlier in a chat about a rule such as 'wait 48 hours' or 'act within 30 minutes', assistants flagged a later request that breaks it in only 30.5% of cases (3,474 of 11,401), from 0.1% for GPT-4o mini to 84.9% for Claude Opus 5. In 62.1% of cases where a model correctly computed the elapsed time when asked, it still missed the violation, and putting the timing in the system prompt recovered only part of the misses. Tested on: 13 models from 8 developers (Claude, GPT, Gemini, Qwen, DeepSeek, Kimi, GLM, MiniMax), 3,418 inputs from 128 templates plus 33 controlled scenarios, one sample per input, English only.

## Details

**Caveats**
Authored conversations with explicit timestamps; the authors say real-world catch rates are likely lower. English only, single reply per input, no memory or retrieval layers.

**For your work**
Recalling a constraint is not the same as applying it. For assistants with memory or long sessions, check constraints in code (rule store plus a time check before acting) rather than counting on the model to connect them, and add tests where the stored rule and the new request sit far apart.

**Method**
- Templates with an earlier event, a time rule tied to it, and a later request on another topic. Gold labels follow mechanically from the timing values.
- Three conditions: ask the elapsed time directly (A), ask an ordinary request (B), or ask the request with the timing stated explicitly (C); non-violation controls change only the timing.
- 23 everyday domains, including emergencies; replies labelled as catch, ask, or miss.

**Problem**
Assistants keep conversations open for hours or days, and users rarely restate earlier constraints (medication waits, fasting, deadlines) when they ask for advice later.

**Results**
- Catch rate falls with model size inside families: Claude Opus 5/Sonnet 5/Haiku 4.5 at 84.9%/38.9%/8.2%, GPT-5.5/GPT-5 mini/GPT-4o mini at 36.6%/8.3%/0.1%.
- False alarms are rare (1.95% of controls), so misses are not just caution being suppressed. Opus 5 has the highest false-alarm rate (6.98%).
- Direct elapsed-time questions: 92.4% correct overall, yet GLM-5.2 answers 99.6% and catches only 27.8% of violations.
- Stating the timing explicitly raised catches from 33.6% to 41.6% on matched items. Models asked a clarifying question in only 3.7% of replies where timestamps were missing.

**Concepts:** [[AI safety]] · [[Evals and benchmarks]] · [[Agent memory]]
**From:** [[2026-11-08]]

# My notes


---
# References
[arXiv 2611.06839](https://arxiv.org/abs/2611.06839)
