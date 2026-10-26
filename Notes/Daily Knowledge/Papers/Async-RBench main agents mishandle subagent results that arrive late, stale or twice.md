---
date: 2026-10-26
section: AI
importance: Med
kind: paper
source: "arXiv 2610.32429"
url: https://arxiv.org/abs/2610.32429
status: unread
id: 2026-10-26-async-rbench
---
2026-10-26 07:16
Tags: #daily-knowledge #ai

---
# Async-RBench main agents mishandle subagent results that arrive late, stale or twice

200 tasks where subagent results arrive asynchronously while the main agent keeps working. Scores on handling those results range from 19.2 (worst) to 45.1 (Claude Sonnet 5, best) out of 100, duplicates and subagent failures are handled worst, and all nine agents succeed less than with batched results (26.0% vs 29.7%). Tested on: 9 models from 7 providers, 200 tasks, one shared harness.

## Details

**Problem**
Main-subagent architectures let the main agent keep working while subagents run, so results can arrive late, stale, conflicting, duplicated or failed, after the task state has moved on. Final success alone does not show whether these were handled correctly.

**Method**
- 200 executable tasks in eight scenarios (delay, stale, conflict, replay/duplication, partial, failure, scope, straggler).
- A scenario controller releases subagent results based on task-state conditions, making async arrivals reproducible.
- An Event Response Contract states what each response must change, preserve, avoid and re-verify; the Dynamic Replanning Score weights process and outcome equally.
- Nine models (Claude Sonnet 5, GPT-5.6 Terra and Luna, Qwen3.7 Plus, Gemini 3 Flash, Qwen3.5 27B, GLM5.3 Flash, Kimi K2.5, DeepSeek V4 Pro) in a common harness and tool set.

**Results**
- Overall scores from 19.2 to 45.1; Claude Sonnet 5 is best at 45.1.
- Lowest scenario means: duplication and replay 8.6, subagent failure 12.2.
- All nine agents succeed less with asynchronous than batched delivery (26.0% vs 29.7% on average), and eight use more tokens.
- Forcing the main agent to rebuild its plan after every result adds only 2.6-3.5 points.

**Caveats**
One shared harness, so it measures models, not orchestration frameworks; absolute success rates are low, which compresses differences.

**For your work**
In multi-agent designs, deduplicate and version subagent results in code (task IDs, timestamps, idempotency) instead of trusting the main model to notice stale or repeated reports, and handle subagent failure explicitly.

**Concepts:** [[Multi-agent systems]] · [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-10-26]]

# My notes


---
# References
[arXiv 2610.32429](https://arxiv.org/abs/2610.32429)
