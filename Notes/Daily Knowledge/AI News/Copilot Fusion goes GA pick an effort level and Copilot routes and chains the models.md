---
date: 2026-10-29
section: AI
importance: High
kind: news
source: "GitHub changelog"
url: https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion
status: unread
id: 2026-10-29-copilot-fusion
---
2026-10-29 07:16
Tags: #daily-knowledge #ai

---
# Copilot Fusion goes GA pick an effort level and Copilot routes and chains the models

In Copilot's model picker you can now choose Fusion instead of a model. It routes each task through a single-model, cascade or critique workflow at Standard, High or Max effort. GitHub says Fusion Max scored 60 on the Artificial Analysis Coding Agent Index, within two points of Claude Code with Opus 5.5 Max, at about half the API cost per task. Each model is billed at its standard rate, with a 30% discount for a limited time.

## Details

**Caveats**
GitHub's own benchmark claim, and the post does not say which models Fusion picks. Costs vary because you pay for every model used, cascade escalations included.

**For your work**
A ready-made example of cascade and critique routing to compare with your client agent designs. Before setting Fusion as a team default, check which models it can reach under your org policy.

**Method**
- Combines Project HydraFusion's multi-model orchestration with auto model selection's fine-tuned router
- Single: one model answers. Cascade: an efficient model drafts, a quality check accepts it or escalates to a stronger model. Critique: one model drafts, a second reviews, the first revises
- Picks only from models allowed by enterprise/org policy; admins can disable models for Fusion only or set Fusion as the default through managed settings

**Problem**
Developers waste effort picking and switching models per task, and always using the top model is expensive.

**Results**
- Fusion Max: 60 on the Artificial Analysis Coding Agent Index, within 2 points of Claude Code + Opus 5.5 Max
- Versus that setup: about half the average API cost per task, about half the tokens, about 40% less time per task
- 30% discount on model costs for paid plans for a limited time; available on all Copilot plans in VS Code, the Copilot app, Copilot CLI and JetBrains

**Concepts:** [[GitHub Copilot]] · [[Multi-agent systems]] · [[Model releases and pricing]]
**From:** [[2026-10-29]]

# My notes


---
# References
[GitHub changelog](https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion)
