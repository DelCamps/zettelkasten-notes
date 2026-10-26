---
date: 2026-10-26
section: AI
importance: High
kind: paper
source: "arXiv 2610.32555"
url: https://arxiv.org/abs/2610.32555
status: unread
id: 2026-10-26-mcp-faults
---
2026-10-26 07:16
Tags: #daily-knowledge #ai

---
# Realistic MCP tool faults cut agent task scores by 60%, and a bigger model does not help

MCP-Injector is a middleware that injects tool failures calibrated on 57,240 issue and PR threads from 1,774 MCP repositories. Under these faults, task-completion scores fall from 8.08 to 3.23 out of 10. gpt-oss-120B is no more fault-tolerant than 20B, and the agent framework matters more than model size.

## Details

**Caveats**
Only two gpt-oss backbones, a stochastic LLM judge, and a fault profile that inherits GitHub reporting bias (a stress test, not a frequency estimate). No frontier closed models.

**For your work**
Add fault-injection runs to your agent evals (timeouts, wrong values, schema errors on MCP tools) and invest in retries, fallbacks and clear error messages in the harness rather than expecting a bigger model to cope.

**Method**
- MCP-Injector sits on the MCP client-server path and injects faults with controlled persistence (permanent, transient, intermittent) on seedable schedules.
- Fault mix calibrated from 57,240 issue and pull-request threads in 1,774 open-source MCP repositories.
- 1,350-cell factorial study: gpt-oss 20B and 120B, three stacks (MCP-Bench plan-and-execute loop, OpenAI Agents SDK, LangChain/LangGraph), three fault conditions, 25 tasks, three seeds; LLM judge scores completion.

**Problem**
Agent benchmarks assume tools answer correctly and on time, but production MCP servers hang, return wrong values, violate schemas and fail permanently. Nobody had measured how agents degrade under a realistic mix of these failures.

**Results**
- Under the permanent-heavy profile, task-completion score drops 60%, from 8.08 to 3.23 out of 10.
- The 120B model keeps no larger share of its fault-free score (p=0.96) and completes slightly fewer tasks under faults (91.1% vs 95.6%).
- Live-API tasks lose up to 97% and long sequential chains 82%, short computational tasks only 19%.
- Stacks differ in how well they absorb faults, pointing to framework-level error handling.

**Concepts:** [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-10-26]]

# My notes


---
# References
[arXiv 2610.32555](https://arxiv.org/abs/2610.32555)
