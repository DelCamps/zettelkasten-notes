---
date: 2026-11-08
section: AI
importance: Med
kind: paper
source: "arXiv 2611.08281"
url: https://arxiv.org/abs/2611.08281
status: unread
id: 2026-11-08-multimodal-sea
---
2026-11-08 07:16
Tags: #daily-knowledge #ai

---
# Multimodal-SEA scammers with forged screenshots, documents and videos trick every tested p

An attacker agent posing as a spouse, colleague or service, backed by generated images, documents, fake apps and videos, got personal agents to pay or leak data in 7.1% (Claude Opus 5) to 34.5% (GPT-5.6-Sol) of tasks. Adding the forged media raised attack success from 19.9% to 29.2%, even though the agents verified more often. A safety-rule system prompt cut GPT-5.6-Sol's success rate from 34.8% to 10.8% on Chinese tasks but made it worse at spotting fakes. Tested on: 7 models from 7 developers, 608 tasks (152 scenarios, Chinese and English), one run per task, one attacker model (DeepSeek-v4-Pro, with a GPT-5.4 attacker as a check).

## Details

**Caveats**
Simulated environment and LLM attacker; one run per task and model. The Chinese and English sets are different scenarios, not translations. Agents are tested as bare models in the authors' harness.

**For your work**
For agents that move money, checks that only confirm consistency across content the attacker controls do not help. Require verification through an independent channel, and treat any claim that an action was done as unproven until the tool log shows it. A safety prompt alone lowers the numbers but does not fix recognition.

**Method**
- 152 scenarios built from real fraud cases (FTC, Hong Kong and Singapore police alerts) across 14 domains, each at four difficulty levels; L4 adds accomplices who back up the attacker's story.
- 50 simulated apps with user profiles, photos and transaction history. Success is judged from tool logs and state changes (money moved or data leaked), not from what the agent says.
- An attack harness steers the attacker's script and generates images (Gemini image model) and videos (Kling) on demand.
- Six metrics, including verification coverage, deception miss rate and 'ungrounded action claims' (saying it paid without calling the tool).

**Problem**
Personal agents now pay bills and handle messages for users, but security tests mostly use text-only prompt injection, not the multi-turn, media-backed social engineering real fraudsters use.

**Results**
- Attack success ranged from 8.9% to 36.7% on Chinese tasks and 5.1% to 34.2% on English tasks. GPT-5.6-Sol's simulated losses added up to about RMB 554,000 and USD 76,600.
- Forged media raised attack success by 9.3 points while verification coverage rose from 54.7% to 65.1%: agents checked more but trusted consistent fakes.
- Accomplices raised attack success from 19.9% (L3) to 27.4% (L4); for Kimi K3 it went from 15.1% to 32.9%.
- The lowest attack rates came with over-refusal: Claude Opus 5 and MiniMax-M3 turned down 32.1% and 51.2% of legitimate requests that had already been verified.

**Concepts:** [[Agent security]] · [[Evals and benchmarks]] · [[Agents]]
**From:** [[2026-11-08]]

# My notes


---
# References
[arXiv 2611.08281](https://arxiv.org/abs/2611.08281)
