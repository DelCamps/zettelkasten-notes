---
date: 2026-11-13
section: AI
importance: High
kind: news
source: "Google blog / Gemini API changelog"
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/
status: unread
id: 2026-11-13-gemini-4-hydrogen
---
2026-11-13 07:16
Tags: #daily-knowledge #ai

---
# Google releases Gemini 4 Hydrogen a fast agentic model at $1.50$7.50 per million tokens th

Gemini 4 Hydrogen is Google's new 'daily driver for agentic workflows', below Gemini 4 Carbon and Argon, at $1.50 input and $7.50 output per million tokens flat across a 1M-token context. Google reports 57% on Terminal-Bench 4.1 (vs 18.2% for Gemini 3.8 Flash) and an Artificial Analysis Intelligence Index of 51 at default, 54 at the new xhigh level.

## Details

**Caveats**
All benchmarks are vendor-reported, and most comparisons are only against Google's own models. Not stated as available on Vertex AI or GitHub Copilot in the announcement.

**For your work**
A strong candidate executor or subagent model for cost-sensitive agent pipelines; worth adding to your eval harness against Claude Haiku/Sonnet-class models. Available in Gemini Enterprise via the API or model dropdown and in Gemini in Google Sheets for eligible business plans.

**Method**
- Four thinking levels: low, medium, high (default) and new xhigh
- 1,048,576-token context, 65,536 output tokens by default; text, image, video, audio and PDF input; function calling, structured outputs, code execution, computer use, file search and Search/Maps grounding; implicit caching only
- Default model for the Antigravity agent in Gemini Managed Agents; Antigravity Orchestrator can switch between Carbon and Hydrogen in one session

**Problem**
Teams need a cheaper, faster model for routine coding and agent execution while reserving frontier models for deep, long-horizon reasoning.

**Results**
- Terminal-Bench 4.1: 57% vs 18.2% for Gemini 3.8 Flash; about 2.5x faster task completion than 3.8 Flash at high
- Vals Tax Agent Bench 52.3% (#1 overall), Vals Legal Research Bench 55.8%, Agents' Last Exam v1.1 71.6%, HLE-Diamond 58.8%
- Partner tests: 2x to 2.8x faster than 3.8 Flash with 12% to 23% fewer tokens
- Safety claims: up to 81% less overreach, over 2.3x more resilient on the Gray Swan indirect prompt injection benchmark, up to 2x less likely to bypass permission boundaries on blocked tasks

**Concepts:** [[Model releases and pricing]] · [[Frontier models]] · [[Google Cloud]]
**From:** [[2026-11-13]]

# My notes


---
# References
[Google blog / Gemini API changelog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)
