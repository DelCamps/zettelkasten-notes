---
date: 2026-10-30
section: AI
importance: Med
kind: paper
source: "arXiv 2610.38867"
url: https://arxiv.org/abs/2610.38867
status: unread
id: 2026-10-30-injection-trust-regions
---
2026-10-30 07:16
Tags: #daily-knowledge #ai

---
# Where an injection sits matters agents obey README and TODO files far more than code or da

Holding the payload fixed, a GPT-5.4 agent followed an injected instruction in a README or TODO file 2.6 times more often than the same text in a code or data file, and end-of-file placement was strongest. Frontier models were close to immune to the fixed template payload (GPT-5.6 and the Claude models near 0%), but an RL-trained attacker reached 33.3% on GPT-5.4 where all templates scored 0%. Tested on: eight models from four providers (OpenAI, Anthropic, Google, xAI), three testbeds built from Terminal-Bench-2, AgentDojo and DecodingTrust-Agent, OpenAI Agents SDK and Claude Agent SDK.

## Details

**Caveats**
Which surfaces are trusted differs by model; three testbeds only; the learned attacker was trained against GPT-4o.

**For your work**
Treat repo docs, TODOs, Slack and web pages your agents read as high-risk untrusted input, and red-team at the end of those surfaces, not just in tool outputs.

**Method**
- 30 longer-horizon tasks across coding, tool use and workplace workflows, with 36 injection surfaces and start/middle/end positions
- Same payload everywhere; conditional attack success counted only when the agent actually read the injection; deterministic script verifiers
- A Qwen2.5-7B attacker trained with SFT then GRPO to pick both content and placement

**Problem**
Prompt-injection work mostly varies what the injection says, not where in the agent's environment it appears.

**Results**
- Code testbed with GPT-5.4: README 86% and TODO 61% success on the recon risk, against 19% for code files
- Tool use with GPT-4o: end-of-surface placement 51.2% against 39.5% at the start
- Failed injections are mostly ignored, not refused (GPT-4o: 81.3% ignored, 0.7% refused)
- Overall susceptibility varies widely: Gemini-3.1-Pro 67.0% in code against 0.0% for Opus5

**Concepts:** [[Agent security]] · [[Coding agents]]
**From:** [[2026-10-30]]

# My notes


---
# References
[arXiv 2610.38867](https://arxiv.org/abs/2610.38867)
