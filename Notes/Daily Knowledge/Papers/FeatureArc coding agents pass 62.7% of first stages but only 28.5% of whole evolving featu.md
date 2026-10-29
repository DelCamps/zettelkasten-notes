---
date: 2026-10-29
section: AI
importance: Med
kind: paper
source: "arXiv 2610.37434"
url: https://arxiv.org/abs/2610.37434
status: unread
id: 2026-10-29-featurearc
---
2026-10-29 07:16
Tags: #daily-knowledge #ai

---
# FeatureArc coding agents pass 62.7% of first stages but only 28.5% of whole evolving featu

FeatureArc mines multi-stage feature histories from real repos. Agents extend their own earlier code over 2-10 stages in one session, with no test feedback in between. Pooled success falls from 62.7% on the first stage to 28.5% for the whole feature. In 94.9% of stages that follow a failure, the agent never notices the earlier error. Tested on: 10 models from 10 providers, 73 tasks in 4 languages, Claude Code (9 agents) and Codex CLI (1).

## Details

**Caveats**
Only 73 tasks. Built by Tencent's Hunyuan team, which also uses it internally. Results appear to come from one run per agent, and the trajectory labels come from LLMs.

**For your work**
For multi-step coding delegation, add checkpoints between stages or rerun earlier stages' tests automatically. Agents will not go back and catch their own earlier defects.

**Method**
- Tasks are built from repository histories, with validated fail-to-pass and pass-to-pass tests at every stage and for the whole feature
- Fully autonomous setting (L4): the user only supplies the next spec and gives no feedback on earlier stages
- Trajectories are labelled by three LLM annotators with blind review; 95% bootstrap CIs

**Problem**
Feature benchmarks score single requests on a fixed codebase. Real delegation chains extensions on top of the agent's own possibly broken code.

**Results**
- Claude Opus 5.5 leads but completes only 49.3% of features, despite passing 83.6% of first stages
- Every agent loses 26.0-38.4 points between the first stage and the whole feature
- Next-stage success is 70.2% after a passed stage vs 22.6% after a failed one; inherited defects appear in 72.9% of failed later stages
- When agents do notice an earlier error, they fix it in 34 of 50 cases; tool use rises only 4-18% after a failed stage

**Concepts:** [[Coding agents]] · [[Evals and benchmarks]]
**From:** [[2026-10-29]]

# My notes


---
# References
[arXiv 2610.37434](https://arxiv.org/abs/2610.37434)
