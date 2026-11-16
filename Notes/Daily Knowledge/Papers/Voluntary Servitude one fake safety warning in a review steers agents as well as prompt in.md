---
date: 2026-11-04
section: AI
importance: High
kind: paper
source: "arXiv 2611.04393"
url: https://arxiv.org/abs/2611.04393
status: unread
id: 2026-11-04-voluntary-servitude
---
2026-11-04 07:16
Tags: #daily-knowledge #ai

---
# Voluntary Servitude one fake safety warning in a review steers agents as well as prompt in

A planted review claiming a hazard (no command at all) makes the agent drop the real providers and choose the attacker's listing by its own reasoning: 60.4% success vs 66.0% for instruction injection, and 1.7-4.4x more effective once a deployed injection detector sits in front. Microsoft Edge with Copilot picked the attacker's listing in every trial. A one-paragraph corroboration rule in the system prompt cut success from 68.4% to 3.6%. Tested on: 6 models from 5 providers, 10 domains with 500 queries, 4 production browser agents, one retrieval pipeline.

## Details

**Caveats**
Single selection decisions in consumer travel domains; defence tested only against a non-adaptive attacker, and it also delays genuine single-source warnings. Browser-agent transfer uses 20 trials per agent.

**For your work**
Add 'persuasive, command-free' payloads to red-team suites for any client agent that ranks vendors, products or suppliers from web or user content, and add a corroboration requirement to its system prompt before it can exclude an option on safety grounds.

**Method**
- Attacker posts a few ordinary-looking reviews; three families: safety (fabricated hazard), authority, attribute claims
- 10 travel-service domains, 50 queries each (500), fictitious target LocalGems; greedy decoding, same prompt for all models
- Compared with reimplemented instruction-injection payloads, measured behind two deployed detectors (ProtectAI, Lakera), on 4 live browser agents and through retrievers
- Defence: an instruction treating a safety claim from a small minority of similar-looking sources as unverified until independently corroborated

**Problem**
Prompt-injection defences look for command syntax in retrieved text. Agents that choose among providers from user-generated reviews can be steered without any command, by exploiting their harm-avoidance.

**Results**
- Safety-family ASR: Gemini 3.1 Flash Lite 86.5%, DeepSeek V4 Flash 83.7%, Llama 3.3 70B 74.9%, Grok 4.3 53.7%, Claude Haiku 4.5 (most resistant) 22.5%
- Behind detectors the payloads are 1.7-4.4x more effective than instruction injection; end-to-end through retrieval 1.0-57.0% depending on the retriever
- Browser agents (20 trials each): Edge with Copilot chose the attacker every time vs 20% for injection; Comet 60% vs none; Codex browser 20% vs none
- Corroboration rule: 68.4% to 3.6% (95% CI 2.2-5.7%) on 450 answers across 3 models

**Concepts:** [[Agent security]] · [[Computer-use agents]] · [[AI safety]]
**From:** [[2026-11-04]]

# My notes


---
# References
[arXiv 2611.04393](https://arxiv.org/abs/2611.04393)
