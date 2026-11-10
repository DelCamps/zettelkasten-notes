---
date: 2026-11-10
section: AI
importance: Med
kind: paper
source: "arXiv 2611.11581"
url: https://arxiv.org/abs/2611.11581
status: unread
id: 2026-11-10-tool-error-delivery
---
2026-11-10 07:16
Tags: #daily-knowledge #ai

---
# Same tool error, different recovery where you put the error message changes whether the ag

Holding the error text fixed, the authors varied only where a tool failure reaches the model. When a transient error was left in the tool message, five of six 7-35B open models retried in at most 37% of cases. Restating it as a runtime note with guidance made most of them act correctly. Removing the failed exchange made Llama models keep calling tools after unrecoverable errors, while keeping it and adding a new user turn fixed this (stopping in 59 of 60 cases). As an engine layer, this raised ToolMaze success on explicit errors by 10.5 to 14.2 points but did nothing on Loud/Quiet. Tested on: 13 open models from 3 families (3B-70B), pre-registered synthetic studies with exact deterministic reruns, 2 public benchmarks and one coding agent.

## Details

**Caveats**
Open models only, English, greedy decoding; gains come mostly from Llama (Qwen2.5-7B got 2.8 points worse). Restating tool text in a user turn gives it more authority, an untested injection risk. Retry guidance is only safe for idempotent tools.

**For your work**
In your agent harness, mark tool failures with their type (is_error plus transient, fixable or permanent) and deliver recovery guidance as a short note rather than relying on the raw error. Keep the failed call in the history. Never auto-suggest retries for writes or payments.

**Method**
- Varied where the error goes (tool message vs runtime note), whether guidance names the right action, keeping vs removing the failed exchange, and adding a new user turn
- Four error kinds; greedy decoding in a deterministic engine so that reruns are exact
- Best form shipped as an opt-in engine layer and compared with llama.cpp, vLLM, SGLang and client-side handling

**Problem**
When a tool call fails, the agent must retry, change the arguments or stop and tell the user, and the same error text can lead to different choices depending on how it is delivered.

**Results**
- A firmer instruction ('Do not call any tool again.') still left Llama-3.1-8B stopping in 0 of 60 cases; a new user turn after the failure gave 59 of 60
- Keeping the failure plus a user turn vs rewriting history: +3.9 and +5.3 points on synthetic errors; on real histories +12.2 points in the large tier, not significant in the small one
- A client that knows the exact fault type did 17 to 19 points better than the engine layer on ToolMaze
- In the coding agent, the layer made the agent report the access problem in all 12 permission-failure runs

**Concepts:** [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-11-10]]

# My notes


---
# References
[arXiv 2611.11581](https://arxiv.org/abs/2611.11581)
