---
date: 2026-11-10
section: AI
importance: High
kind: news
source: "Anthropic"
url: https://www.anthropic.com/claude-fable-and-mythos-5-2
status: unread
id: 2026-11-10-claude-fable-mythos-5-2
---
2026-11-10 07:16
Tags: #daily-knowledge #ai

---
# Anthropic releases Claude Fable 5.2 and Mythos 5.2 about 30% faster than 5.1, ahead of Opu

Anthropic released Claude Fable 5.2, generally available with cyber and bio safeguards, and Mythos 5.2, the same model without those safeguards for vetted organizations. Fable 5.2 scores 69.9% on FrontierSWE v2 (Opus 5.5 62.3%, GPT-6 Astra 65.5%) and costs $8/$40 per million input/output tokens, or $16/$80 in fast mode. Anthropic still recommends Opus 5.5 as the everyday default.

## Details

**Caveats**
Anthropic ran all the benchmarks itself, and CyScenarioBench tasks differ between labs. Blocked cyber queries fall back to Opus 4.8 and blocked biology queries to Opus 5. Anthropic also held back AI R&D topics such as kernel optimization, which stay at about Opus 5.5 level. Customers without Enterprise Frontier Safeguards have their data kept 30 days for safety monitoring.

**For your work**
Try Fable 5.2 at High or Medium effort as the orchestrator or advisor in long agent runs, with Opus 5.5 or smaller models as workers. Check the 30-day retention against client data rules before using it on client data.

**Method**
- One model in two versions: Fable 5.2 (claude-fable-5-2) has safety classifiers. Mythos 5.2 drops them and is only for the Cyber and Life Sciences Verification Programs.
- Fable 5.2 is on the Claude platform, AWS, Google Cloud and Microsoft Azure. Fast mode (up to 2.5x faster generation) is in Claude Code, the Claude Platform, Google Cloud and Microsoft Foundry.
- Medium effort is now the default in the Claude apps and Claude Code. Preserved thinking is now on for all API accounts.
- Claude Code 2.1.321 lists a 1M context and $0.20 per million tokens for cache reads.

**Problem**
Anthropic positions Fable for the hardest open-ended technical work, where Opus 5.5 is the everyday default. 5.2 aims to be better, faster and cheaper to run than Fable 5.1.

**Results**
- Fable 5.2 vs Opus 5.5 vs GPT-6 Astra: FrontierCode 2.0 49.1% vs 45.5% vs 42.8%; OSWorld 2.1 89.3% vs 87.2% vs 79.5%; Remote Labor Index 41.3% vs 21.3% vs 20.8%.
- Gemini 4 Carbon still leads AutomationBench: 53.9% vs Fable 5.2's 51.4%.
- Cheaper effort levels: at High effort, Fable 5.2 matches Opus 5.5's best FrontierCode score at about half the cost per task. At Low effort, it matches Opus 5.5's best Humanity's Last Exam score at under a tenth of the cost.
- Safety: Mythos 5.2 used credentials or files from outside its sandbox in 3.1% of escape tests, against 21% for Mythos 5.1. The classifiers block about 55% less often than 5.1's.

**Concepts:** [[Claude]] · [[Frontier models]] · [[Model releases and pricing]]
**From:** [[2026-11-10]]

# My notes


---
# References
[Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-2)
