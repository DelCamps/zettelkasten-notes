---
date: 2026-11-15
section: AI
importance: Low
kind: paper
source: "arXiv 2611.16304"
url: https://arxiv.org/abs/2611.16304
status: unread
id: 2026-11-15-statealign-tool-rl
---
2026-11-15 07:16
Tags: #daily-knowledge #ai

---
# StateAlign RL that contrasts paired task states teaches small tool agents when to ask, fet

Training tool agents on pairs of near-identical states (one allows execution, the other needs clarification, retrieval or a refusal) raises Qwen3-8B on BFCL v4 multi-turn from 45.5% to 55.2%, ahead of plain GRPO (51.9%) and LoopTool (53.1%), and cuts no-tool hallucination for every base model. Tested on: 5 base models (4B-14B) from 3 families (Qwen3, Granite, Llama), 4 benchmarks.

## Details

**Caveats**
Only 4B-14B models, short text-only interactions with recorded feedback; larger models and long changing workflows untested.

**For your work**
- Little direct use unless a client fine-tunes a small on-prem tool agent; then pair-state data is a cheap recipe against acting on missing information
- The five-condition split (execute, ask, fetch, decline, finish) is a useful checklist for tool-agent test cases

**Method**
- Build task states from ToolMind and LoopTool-23k data under five conditions, pairing states that differ in one condition that changes the right action
- Outcome reward for completing the task, plus a token-level contrast that compares the same reasoning and actions under the paired states
- Compare with base models, GRPO, ToolRL, LoopTool and AWM

**Problem**
RL improves tool-use scores but can increase tool hallucination: agents execute when they should ask the user, look something up, or decline, even when their reasoning notices the missing information.

**Results**
- Qwen3-8B: BFCL v4 multi-turn 45.5% to 55.2%; ToolSandbox 73.4 to 79.3; When2Call 66.4 to 72.4
- Gains on all five base models: +4.4 (Granite-4.2-8B) to +18.1 (Llama-3.1-8B) BFCL points
- No-tool hallucination falls for all five, e.g. Granite 20.8% to 10.5%; distractor-tool hallucination rose slightly on Qwen3-14B
- More complete multi-call execution and better recovery after tool errors in behavioural analyses

**Concepts:** [[Post-training and RL]] · [[Agents]] · [[Hallucination]]
**From:** [[2026-11-15]]

# My notes


---
# References
[arXiv 2611.16304](https://arxiv.org/abs/2611.16304)
