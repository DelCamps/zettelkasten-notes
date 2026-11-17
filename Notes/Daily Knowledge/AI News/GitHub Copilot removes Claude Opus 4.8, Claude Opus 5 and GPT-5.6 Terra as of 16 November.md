---
date: 2026-11-17
section: AI
importance: High
kind: news
source: "GitHub changelog"
url: https://github.blog/changelog/2026-11-16-github-copilot-models-deprecated-on-november-16-2026
status: unread
id: 2026-11-17-copilot-opus-48-removed
---
2026-11-17 07:16
Tags: #daily-knowledge #ai

---
# GitHub Copilot removes Claude Opus 4.8, Claude Opus 5 and GPT-5.6 Terra as of 16 November

GitHub deprecated three Copilot models on 16 November across most Copilot experiences, pointing users to Claude Opus 5.5 and to GPT-6.1 Sol or GPT-6 Luna. On Business and Enterprise the replacements switch on automatically unless an admin has turned off default model enablement.

## Details

**Caveats**
This is a separate batch from the six models (including Claude Fable 5 and Claude Haiku 4.5) that GitHub retires on 14 December.

**For your work**
Check client Copilot org settings: if default model enablement is off, developers may have lost their Opus model with no replacement until an admin enables Opus 5.5. Update any agent or prompt files that name the removed models.

**Method**
- Claude Opus 4.8 and Claude Opus 5: suggested replacement Claude Opus 5.5
- GPT-5.6 Terra: suggested replacement GPT-6.1 Sol or GPT-6 Luna
- Announced on 15 October, effective 2026-11-16

**Problem**
Teams with Copilot workflows, custom agents or policies pinned to older Claude and GPT models need to know what disappeared and what replaces it.

**Results**
- Claude Opus 4.8 stays available to individual subscribers on annual plans
- Claude Opus 5 leaves the model picker but is still used for runtime refusal fallback
- Business and Enterprise: replacements are enabled automatically under default model enablement; if the global default is off, admins must enable them in model policies

**Concepts:** [[GitHub Copilot]] · [[Model releases and pricing]]
**From:** [[2026-11-17]]

# My notes


---
# References
[GitHub changelog](https://github.blog/changelog/2026-11-16-github-copilot-models-deprecated-on-november-16-2026)
