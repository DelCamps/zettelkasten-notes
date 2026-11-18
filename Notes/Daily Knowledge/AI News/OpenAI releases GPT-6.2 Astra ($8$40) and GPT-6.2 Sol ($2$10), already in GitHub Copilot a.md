---
date: 2026-11-18
section: AI
importance: High
kind: news
source: "OpenAI API docs"
url: https://developers.openai.com/api/docs/guides/latest-model
status: unread
id: 2026-11-18-gpt-6-2-astra-sol
---
2026-11-18 07:16
Tags: #daily-knowledge #ai

---
# OpenAI releases GPT-6.2 Astra ($8$40) and GPT-6.2 Sol ($2$10), already in GitHub Copilot a

OpenAI's new GPT-6.2 family has Astra for the hardest reasoning and coding work and Sol for everyday coding and agents, at $8/$40 and $2/$10 per million input/output tokens. The API changes how reasoning is kept: after a prefix edit the Responses API drops reasoning items, and tool calling requires the Responses API. Both models reached GitHub Copilot (Pro+, Max, Business, Enterprise) and Amazon Bedrock (GA) the same day.

## Details

**Caveats**
OpenAI's launch post (openai.com) could not be read. Press reports say it claims a 5.2-point gain over GPT-6 Astra on Agents' Last Exam and that Astra is 20% cheaper than GPT-6 Astra; these figures are not checked here. Copilot rollout is gradual.

**For your work**
Before switching client agents, check any code that edits earlier messages or tools, and move instructions into a developer message. EU residency makes Sol a candidate for Spanish clients.

**Method**
- Two models: gpt-6.2-astra (for the hardest work) and gpt-6.2-sol (everyday coding and agents at scale), both with text and image input and full Responses tools (web search, hosted shell, computer use, MCP, tool search).
- Breaking behaviour: mid-conversation prefix edits, some model changes (including downgrades) or a change of end user make the Responses API drop reasoning items. Top-level instructions are now appended after input, so stable instructions belong in a developer message to stay cacheable.
- Migration: omit temperature, top_p and logprobs; reasoning effort none is rejected (use low); use prompt_cache_options.ttl.

**Problem**
Teams on GPT-6 Astra and GPT-6.1 Sol need to know what the new pair costs and what breaks when they switch an agent integration over.

**Results**
- Astra $8 input / $0.40 cached / $40 output per 1M tokens; Sol $2 / $0.10 / $10.
- Over 272K input tokens, input rates double and output costs 1.5 times; Batch is 50% of Standard; Ultrafast is 3 times Standard through February 28, 2027.
- New Responses background windows: 30% off for two hours, 40% off for eight hours.
- Both support US and EU data residency (Standard, Fast, Batch); Ultrafast is US only.

**Concepts:** [[Frontier models]] · [[Model releases and pricing]] · [[GitHub Copilot]]
**From:** [[2026-11-18]]

# My notes


---
# References
[OpenAI API docs](https://developers.openai.com/api/docs/guides/latest-model)
