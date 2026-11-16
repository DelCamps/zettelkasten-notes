---
date: 2026-11-14
section: AI
importance: Med
kind: paper
source: "arXiv 2611.14808"
url: https://arxiv.org/abs/2611.14808
status: unread
id: 2026-11-14-overserve-mcp-amplification
---
2026-11-14 07:16
Tags: #daily-knowledge #ai

---
# OverServe an honest-looking MCP status tool plus a 'confirm it's synced' prompt made SaaS

A malicious tenant of a flat-fee agent service supplies an MCP tool that truthfully reports an update as still pending, plus a prompt asking the agent to confirm completion, so the agent keeps polling after the real task is done. Across five enterprise-workflow benchmarks the geometric mean amplification was 10.30x, attacked runs still passed the original task checks, and five industrial MCP scanners flagged none of the 22 crafted tools. Tested on: 4 models from 4 families (Qwen3.8-27B, Nemotron-3-Super, DeepSeek-v4-Flash, Claude Sonnet 5), selected tasks from nine benchmarks plus Terminal-Bench, simulated backends.

## Details

**Caveats**
Selected tasks with controlled backend simulations; the original task checks do not test the added synchronisation requirement; review inputs and baselines vary across experiments.

**For your work**
In client agent services, cap tool calls, turns and tokens per request and per tenant, alert on repeated polling of one status tool, and review third-party MCP tools together with the prompts that use them.

**Method**
- The attacker controls both a user prompt and a third-party MCP tool, each benign-looking on its own.
- The tool returns accurate status and ends normally; under 'churn' the backend keeps reporting pending updates, and the prompt's completion condition keeps the agent checking.
- A multi-agent generator builds service-specific tool-prompt pairs, filtered by separate tool and prompt reviews and by victim runs.

**Problem**
In subscription SaaS the provider pays for every model and tool call, and the agent decides on its own when to stop. Earlier resource-exhaustion attacks used a malicious prompt or a malicious tool alone, which source or prompt reviews catch.

**Results**
- 20 victim-benchmark entries on five enterprise benchmarks: geometric mean 10.30x; per model 19.30x Qwen, 8.07x Nemotron, 17.75x DeepSeek, 4.07x Sonnet.
- Peak 93.88x API requests (Sonnet on AppWorld); Terminal-Bench elapsed time 12.12x to 53.48x.
- Median 8.70x more input/output tokens under churn; source-code review and research detectors caught the tools of earlier attacks (A2M, LoopTrap) but not OverServe's.

**Concepts:** [[Agent security]] · [[Agents]]
**From:** [[2026-11-14]]

# My notes


---
# References
[arXiv 2611.14808](https://arxiv.org/abs/2611.14808)
