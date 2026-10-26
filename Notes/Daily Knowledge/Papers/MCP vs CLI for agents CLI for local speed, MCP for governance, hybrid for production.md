---
date: 2026-10-25
section: AI
importance: Med
kind: paper
source: "arXiv 2610.30157"
url: https://arxiv.org/abs/2610.30157
status: unread
id: 2026-10-25-mcp-vs-cli
---
2026-10-25 07:16
Tags: #daily-knowledge #ai

---
# MCP vs CLI for agents CLI for local speed, MCP for governance, hybrid for production

A 14-dimension comparison argues shell-command tools win on efficiency for single-user local work, while MCP provides what CLI cannot: fine-grained access control, credential isolation, structured audit and multi-tenant governance. Progressive disclosure (about 170 tokens of meta-tools instead of 2,000-55,000 tokens of schemas) removes MCP's context overhead; the authors recommend a hybrid.

## Details

**Caveats**
A position and analysis paper, not a controlled benchmark: token figures are estimates and some economics come from consultancy reports. Clearly favours MCP; no measured task success rates.

**For your work**
A handy framework for client architecture discussions: CLI-style tools for single-developer coding agents, MCP with progressive tool discovery for multi-tenant enterprise agents that need credential isolation and audit logs.

**Method**
- Compares CLI and MCP across 14 dimensions with worked examples, including state leakage, version brittleness, retries and idempotency.
- Security assessment against NSA guidance, OWASP and other compliance frameworks.
- Token-cost and total-cost-of-ownership modelling, with and without progressive disclosure (two meta-tools that look up and call tools on demand).

**Problem**
Teams building agents must choose between letting the model run shell commands directly (CLI) or exposing typed tools over the Model Context Protocol. The debate is mostly anecdotal, and MCP is often criticised for flooding the context window with tool schemas.

**Results**
- Naive MCP loading costs 2,000-55,000 upfront tokens; progressive disclosure cuts that to about 170, with 80-250 tokens per call.
- Structured output parsing costs 50-150 tokens vs 100-500 for unstructured CLI output; error recovery 100-300 vs 300-1,200 tokens per retry.
- CLI risks (state leakage, silent output-format drift, no retry semantics) are judged architectural; MCP risks operational and mitigable.

**Concepts:** [[Agents]] · [[Agent security]]
**From:** [[2026-10-25]]

# My notes


---
# References
[arXiv 2610.30157](https://arxiv.org/abs/2610.30157)
