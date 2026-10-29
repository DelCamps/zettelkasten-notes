---
date: 2026-10-29
section: AI
importance: Low
kind: paper
source: "arXiv 2610.37201"
url: https://arxiv.org/abs/2610.37201
status: unread
id: 2026-10-29-bipa-skill-optimizers
---
2026-10-29 07:16
Tags: #daily-knowledge #ai

---
# Skill optimizers (two models) learned skills gain 0.1 points but read 16% more tokens

Running GEPA, SkillOpt and SkillAdam on long-horizon agent benchmarks, the learned skills score only 0.1 points above the hand-written seed on test, and they read about 1.16x its input tokens. A 'selection replay' shows that their reported dev-set gains are what best-of-several selection on 30 or fewer tasks produces even when nothing changed. Tested on: 2 models (DeepSeek-V4.1-Flash, GPT-6-Luna), 3 optimizers, 3 benchmarks, OpenCode, 3 test runs per skill.

## Details

**Caveats**
Only two models and one harness, and one seed skill. The harness keeps the full history, which magnifies the cost of extra turns.

**For your work**
Before trusting an auto-optimized prompt or skill, rerun the baseline several times and require a repeated win. Track input tokens per task, not just pass rate. Let the editor delete rules, not only add them.

**Method**
- Selection replay: the optimizer's acceptance rule is re-run on candidates identical to the seed, to see what gain selection alone reports
- Each episode is a bipartite graph of turns and the text each turn reads, so extra tokens can be traced to added turns, calls or skill text
- The rules the optimizers add are sorted into 8 categories

**Problem**
Skill and prompt optimizers report gains from small, noisy dev sets, and success scores hide the extra cost the added rules create.

**Results**
- Across 16 learned skills, test success is +0.1 points vs the seed; they gain about as many tasks as they lose
- Under DeepSeek, unchanged candidates reach the reported dev gain in 56-94% of replays (P(G0>=G))
- 91 of 97 scored edits make the skill longer; about half the added rules tell the agent to re-check its work
- A naive 'one higher dev score' gate accepts 24-41% of unchanged candidates

**Concepts:** [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-10-29]]

# My notes


---
# References
[arXiv 2610.37201](https://arxiv.org/abs/2610.37201)
