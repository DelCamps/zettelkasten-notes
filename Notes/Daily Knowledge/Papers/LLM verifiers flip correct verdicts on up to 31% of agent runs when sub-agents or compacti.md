---
date: 2026-11-16
section: AI
importance: Med
kind: paper
source: "arXiv 2611.18471"
url: https://arxiv.org/abs/2611.18471
status: unread
id: 2026-11-16-verification-transport
---
2026-11-16 07:16
Tags: #daily-knowledge #ai

---
# LLM verifiers flip correct verdicts on up to 31% of agent runs when sub-agents or compacti

Showing a verifier the same frozen agent run through a composed tool, a delegation boundary or a compacted history breaks verdicts that were correct on the raw trace: 31.0% under macro abstraction, 30.9% under delegation and 20.3% under compaction. Restoring execution provenance recovers 85.5% of these failures. Tested on: 7 verifier models from 3 developers (Gemini, Gemma, GPT-OSS, Llama 4), 4 verification protocols, 4 benchmarks including AgentDojo.

## Details

**Caveats**
Abstractions applied to frozen trajectories rather than live runs; no frontier closed verifiers beyond Gemini Flash models; three boundary types only.

**For your work**
If you grade agents with an LLM judge, log and pass raw tool calls and sub-agent outputs, not just summaries, and recheck judge accuracy on the trace format you actually ship.

**Method**
- Build matched native, abstracted and restored views of the same executions, holding task, outcome and verifier fixed
- Measure the share of native-correct judgments that break (transport failure)
- Compare direct, evidence-aware, agentic and deliberative verification protocols

**Problem**
LLM judges for agents are validated on one trace format, but production traces pass through sub-agents, macro-tools and context compaction.

**Results**
- Transport failure: 31.0% macro abstraction, 30.9% delegation, 20.3% compaction
- Direct judges mostly give wrong verdicts; evidence-grounded and deliberative ones mostly abstain
- Restoring provenance recovers 85.5% of failures, less when provenance is lossy

**Concepts:** [[Evals and benchmarks]] · [[Agents]] · [[Multi-agent systems]]
**From:** [[2026-11-16]]

# My notes


---
# References
[arXiv 2611.18471](https://arxiv.org/abs/2611.18471)
