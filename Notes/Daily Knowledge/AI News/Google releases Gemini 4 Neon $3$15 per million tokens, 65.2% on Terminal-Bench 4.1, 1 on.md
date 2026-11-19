---
date: 2026-11-19
section: AI
importance: High
kind: news
source: "Google blog"
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/
status: unread
id: 2026-11-19-gemini-4-neon
---
2026-11-19 07:16
Tags: #daily-knowledge #ai

---
# Google releases Gemini 4 Neon $3$15 per million tokens, 65.2% on Terminal-Bench 4.1, 1 on

Google's new mid-tier Gemini 4 Neon sits between Carbon and Hydrogen. It costs $3 per million input tokens ($0.15 cached) and $15 per million output tokens, has a 1 million-token context window, and Google says it scores 61 on the Artificial Analysis Intelligence Index (#3 overall) at a 32% lower cost per task than Carbon. It is GA in the Gemini API and is already in GitHub Copilot's model picker.

## Details

**Caveats**
All benchmarks are Google's own claims, many from leaderboards it picked. The fabrication and safety claims (for example, refusing just 1.98% of legitimate cyber or bio tasks) come from internal testing. In Copilot it is billed at Google's list price, on Pro+, Max, Business and Enterprise plans.

**For your work**
A strong candidate for the orchestrator tier in client agents: price it against GPT-6.2 Sol and Claude on your own evals. Google's own SWE-sweep numbers (12.8% vs 39.0%) are a useful slide on why the harness matters as much as the model.

**Method**
- Adapted from Gemini 4 Carbon, with four thinking levels (low, medium, high by default, xhigh) so you can trade intelligence for token spend
- Built for long agent runs: fewer redundant file reads, more reliable context compaction, and use as an orchestrator that directs parallel Hydrogen subagents in Antigravity
- A 'Gemini 4 Neon for cyber' variant goes to vetted defenders through the Fairwind Program in the coming days

**Problem**
Teams want close to frontier quality for long, tool-heavy agent runs without paying frontier prices for every step.

**Results**
- Coding: #1 on the Artificial Analysis Coding Agent Index (58.6), 65.2% on Terminal-Bench 4.1, 46.2% on FrontierCode 2.0 at the default high setting
- SWE-sweep: 12.8% in the mini-SWE harness rises to 39.0% in Antigravity, which shows how much the harness matters
- Enterprise work: 70.9% on the Vals Index (#2), #1 on Zapier's AutomationBench (56.3%) and on Vending-Bench 2 ($16,843)
- Cost: 32% lower cost per task than Carbon at the high level; Google claims roughly 50% to 80% lower cost per task than top competing frontier models

**Concepts:** [[Model releases and pricing]] · [[Frontier models]] · [[Coding agents]]
**From:** [[2026-11-19]]

# My notes


---
# References
[Google blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)
