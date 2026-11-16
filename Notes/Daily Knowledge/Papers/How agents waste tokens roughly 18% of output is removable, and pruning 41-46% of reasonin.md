---
date: 2026-11-07
section: AI
importance: Med
kind: paper
source: "arXiv 2611.07238"
url: https://arxiv.org/abs/2611.07238
status: unread
id: 2026-11-07-agent-token-waste
---
2026-11-07 07:16
Tags: #daily-knowledge #ai

---
# How agents waste tokens roughly 18% of output is removable, and pruning 41-46% of reasonin

A tracing proxy plus an LLM judge marks removable spans (restating, padding, duplicate fetches, detours) in agent trajectories, validated by deleting them and resuming the run. Roughly 18% of output tokens were waste, waste varied more by task and harness than by model, and at high reasoning effort Max cost 1.62 times as much as High on tasks both solved, with 81% of the extra tokens spent on tasks whose outcome did not change. Tested on: six frontier models from four providers (Kimi-K3, Gemini 3.1 Pro, GPT-5.6 Terra, GPT-6 Astra, Claude Sonnet 5, Claude Fable 5.1), four benchmarks (tau-bench, SWE-bench Verified, Claw-Eval, MCP-Atlas), five harnesses with Kimi-K3.

## Details

**Caveats**
Waste is defined by an LLM judge; reasoning waste only measurable for Kimi-K3 (others hide or summarize reasoning). Effort and harness experiments use a single model.

**For your work**
When a client asks why an agent is expensive, trace it and classify the waste before lowering reasoning effort; harness bugs and tool exploration are often the bigger lever. Max effort rarely pays over High.

**Method**
- Proxy-based tracing attaches to any harness via its API base URL and normalizes trajectories
- LLM judge labels strict waste vs exploratory detours; token counts from each provider's own tokenizer
- Validation: delete marked spans and resume, compare next-action distributions over 16 samples, and prune online during runs

**Problem**
Agent cost studies report total tokens, which cannot tell necessary work from removable repetition, so cost cutting risks removing the reasoning a task needs.

**Results**
- Online pruning removed 41% (SWE-bench Verified, 89.0% to 89.5% solved) and 46% (MCP-Atlas, 65.0% to 62.3%) of reasoning; deleting all reasoning dropped to 73.0% and 56.0%
- For more than 45% of tasks, one agent's wasted output alone exceeded the full output of another agent that solved the task
- Same model and effort: one harness produced more than four times as much reasoning as another; several harnesses launched SWE-bench in the wrong Python environment

**Concepts:** [[Inference efficiency]] · [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-11-07]]

# My notes


---
# References
[arXiv 2611.07238](https://arxiv.org/abs/2611.07238)
