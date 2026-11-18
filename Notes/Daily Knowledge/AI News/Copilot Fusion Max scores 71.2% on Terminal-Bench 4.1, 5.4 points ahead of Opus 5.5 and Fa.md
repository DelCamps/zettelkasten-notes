---
date: 2026-11-18
section: AI
importance: High
kind: news
source: "GitHub changelog"
url: https://github.blog/changelog/2026-11-17-github-copilot-fusion-updates-more-availability-benchmarks-and-models
status: unread
id: 2026-11-18-copilot-fusion-terminal-bench
---
2026-11-18 07:16
Tags: #daily-knowledge #ai

---
# Copilot Fusion Max scores 71.2% on Terminal-Bench 4.1, 5.4 points ahead of Opus 5.5 and Fa

GitHub's model router, Copilot Fusion, now has public Terminal-Bench 4.1 results. Fusion Max resolved 71.2% of tasks, 5.4 percentage points ahead of Opus 5.5 and Fable 5.2, while costing 88% less than Fable 5.2 and 57% less than Opus 5.5. Fusion is also now on github.com and in Visual Studio, and adds Claude Sonnet 5.5, GPT-6.1 Terra and MAI-Code-2 to its tiers.

## Details

**Caveats**
GitHub's own announcement; the post gives no cost basis or per-task breakdown. One benchmark only (terminal tasks). Routing hides which model wrote each change.

**For your work**
This is a concrete argument for routing over a single fixed model in coding-agent setups. Worth trying Fusion Max against your current default on a client repo, watching both cost and pass rate.

**Method**
- Fusion is listed on the public Terminal-Bench 4.1 leaderboards hosted by Stanford, Harbor and the Laude Institute, which test hard, realistic terminal tasks under shared rules.
- You pick Fusion in the model picker and set an effort level; Copilot chooses and coordinates the models.
- New models: Claude Sonnet 5.5 in Fusion Max, GPT-6.1 Terra in Fusion High, MAI-Code-2 in Fusion Standard.

**Problem**
Fusion picks and chains models for each task. Until now there was no independent number showing whether routing beats one frontier model.

**Results**
- Fusion Max: 71.2% resolution rate, 5.4 points above Opus 5.5 and Fable 5.2.
- Cost: 88% less than Fable 5.2 and 57% less than Opus 5.5.
- Available on the latest github.com, Visual Studio and the GitHub Mobile beta apps; the production mobile apps follow shortly.

**Concepts:** [[GitHub Copilot]] · [[Evals and benchmarks]] · [[Coding agents]]
**From:** [[2026-11-18]]

# My notes


---
# References
[GitHub changelog](https://github.blog/changelog/2026-11-17-github-copilot-fusion-updates-more-availability-benchmarks-and-models)
