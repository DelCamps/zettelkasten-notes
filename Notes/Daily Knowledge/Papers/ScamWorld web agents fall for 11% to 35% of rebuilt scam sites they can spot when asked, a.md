---
date: 2026-11-04
section: AI
importance: Med
kind: paper
source: "arXiv 2611.04879"
url: https://arxiv.org/abs/2611.04879
status: unread
id: 2026-11-04-scamworld
---
2026-11-04 07:16
Tags: #daily-knowledge #ai

---
# ScamWorld web agents fall for 11% to 35% of rebuilt scam sites they can spot when asked, a

Across 363 reconstructed scam websites, six frontier-model web agents were deceived in 11% to 35% of tasks, although in a separate 'is this a scam?' check their recognition rates were 0.88 to 1.00. Agents proceeded in 28% of payment scams but only 2% of credential or wallet requests, often citing the user's request as authorisation; a one-sentence warning cut deception by 24 points but cost 3 points of completion on legitimate sites. Tested on: 6 backbones from 6 providers, 2,262 episodes, 16 fraud scenarios in 26 languages, one agent scaffold (AgentLab).

## Details

**Caveats**
Website fraud only; red flags deliberately exposed before the final action; fixed scaffold, mostly offline; no human baseline; LLM judge for fraud recognition.

**For your work**
For client shopping, procurement or payment agents, require an explicit fraud check before any irreversible payment and do not treat the user's original request as consent to new fees or payees; ScamWorld can serve as a pre-deployment test.

**Method**
- Reconstructed reported scam websites with 38 documented fraud mechanisms, each with an observable red flag before the final action, plus 53 legitimate websites as controls
- Same AgentLab web agent (screenshot, URL, accessibility tree) for GPT-5.6 Luna, Claude Haiku 5.5, Kimi K3, DeepSeek V4.1 Flash, Gemini 3.8 Flash and Qwen 3.8 Flash
- Task execution vs explicit assessment; 95% CIs from a website-level bootstrap; ablations with warnings and 'real payment' notices

**Problem**
Web agents that shop, book and manage accounts meet fraud built to fool humans (fake stores, investment platforms, advance-fee schemes), not just prompt injection. Scam sites are short-lived, so this has been hard to test repeatably.

**Results**
- Deceived rate: GPT-5.6 Luna 0.11, Haiku 5.5 0.18, Kimi K3 0.23, DeepSeek V4.1 Flash 0.35; completion on legitimate sites 0.94-1.00
- Deception highest for investment scams (34%); payments to private individuals still went ahead in 22% of episodes
- Deceived agents that voiced concern cited the user's request as their reason in 317 of 354 cases
- 'Payments are real and irreversible' notice changed deception by only 1 point

**Concepts:** [[Agent security]] · [[Computer-use agents]] · [[Evals and benchmarks]]
**From:** [[2026-11-04]]

# My notes


---
# References
[arXiv 2611.04879](https://arxiv.org/abs/2611.04879)
