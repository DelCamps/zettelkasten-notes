---
date: 2026-11-18
section: AI
importance: High
kind: news
source: "GitHub changelog"
url: https://github.blog/changelog/2026-11-17-github-copilot-evals-is-now-in-public-preview
status: unread
id: 2026-11-18-copilot-evals-preview
---
2026-11-18 07:16
Tags: #daily-knowledge #ai

---
# GitHub Copilot Evals (public preview) repeatable tests for your skills, custom agents and

GitHub released Copilot Evals, which creates and runs repeatable tests on the skills, custom agents and MCP tools in your Copilot setup. It checks both the result and how the agent got there, and compares runs before and after a change. It runs on Vally, a local eval engine, in VS Code, Copilot CLI and the Copilot app.

## Details

**Caveats**
Preview only. Evals run locally and each run needs approval, so it is not yet a CI gate. How well it judges results on open-ended tasks is untested.

**For your work**
This gives a native way to regression-test the skills and MCP servers you ship to clients. Consider an eval per skill as a deliverable, so a model or prompt change can be checked before rollout.

**Method**
- Ask in your own words or use /eval to create an eval for a skill, custom agent or MCP tool in your project.
- You approve each run before it starts. Each eval checks the result and the steps the agent took, and explains why a check failed.
- You can compare runs from before and after a customisation change to catch regressions.
- The engine is Vally, an extensible local eval tool. It installs as a VS Code extension, a Copilot CLI plugin, or from the github/evals marketplace in the Copilot app.

**Problem**
Customisations such as skills, agents and MCP tools change often, and because 'AI output can change from one run to the next', a single good answer does not prove a change helped.

**Results**
- In public preview for Copilot Individual, Business and Enterprise plans.
- The post gives no performance figures; this is tooling, not a benchmark result.

**Concepts:** [[GitHub Copilot]] · [[Evals and benchmarks]] · [[Agents]]
**From:** [[2026-11-18]]

# My notes


---
# References
[GitHub changelog](https://github.blog/changelog/2026-11-17-github-copilot-evals-is-now-in-public-preview)
