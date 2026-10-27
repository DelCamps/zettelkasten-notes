---
date: 2026-10-27
section: AI
importance: Med
kind: paper
source: "arXiv 2610.34298"
url: https://arxiv.org/abs/2610.34298
status: unread
id: 2026-10-27-mcp-cli-mica
---
2026-10-27 07:16
Tags: #daily-knowledge #ai

---
# Same tools via MCP or CLI agent behaviour diverges in 94.3% of paired runs

MICA renders MCP and CLI interfaces from one shared action contract and finds that, with capabilities matched, 1,889 of 2,004 paired episodes (94.3%) diverge, usually early, changing scores and cost. A repair step, DART, improves scores in all six settings by up to 9.0 points and cuts MCP token cost by up to 27.1k tokens per task. Tested on: 6 models (Qwen3 4B-32B, DeepSeek-v4-Flash, Gemini-2.5-Flash), 3 environments (ALFWorld, WebShop, ScienceWorld).

## Details

**Caveats**
Mostly small Qwen models and older text-game environments, not production tool stacks or frontier models.

**For your work**
Interface shape is a tuning knob: if an agent fails with your MCP server, try the same operations as a CLI (or vice versa) and retry malformed calls without re-planning.

**Method**
- Both interfaces generated from one semantic action contract and routed through the same runtime, holding model, task state and information fixed.
- Matched-state probes localize sensitivity to capability presentation, realization and feedback.
- DART keeps a validated semantic action and repairs only its interface-specific realization when execution fails.

**Problem**
MCP vs CLI comparisons usually differ in what the tools can do; this isolates the representation itself.

**Results**
- Substantial differences in task performance and interaction cost between matched interfaces.
- 94.3% of 2,004 paired episodes show structured divergence, starting near the beginning and propagating.
- DART: up to +9.0 points in all six settings; up to 27.1k fewer MCP tokens per task.

**Concepts:** [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-10-27]]

# My notes


---
# References
[arXiv 2610.34298](https://arxiv.org/abs/2610.34298)
