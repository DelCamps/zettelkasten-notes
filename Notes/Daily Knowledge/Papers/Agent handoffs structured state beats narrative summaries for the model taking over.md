---
date: 2026-10-28
section: AI
importance: Med
kind: paper
source: "arXiv 2610.36523"
url: https://arxiv.org/abs/2610.36523
status: unread
id: 2026-10-28-hsc-bench-handoffs
---
2026-10-28 07:16
Tags: #daily-knowledge #ai

---
# Agent handoffs structured state beats narrative summaries for the model taking over

HSC-Bench tests how well a model continues work handed over mid-task by another. Passing a structured handoff state instead of a narrative summary raises the all-criteria pass rate for all six receivers by 7.44 to 12.18 points; even GPT-5.4, at a 92.76 mean score, passes every criterion on only 52.1% of tasks. Tested on: 6 receiving models from 5 providers, 1,039 tasks.

## Details

**Caveats**
Receivers include Claude Sonnet 5, GPT-5.4, Gemini 3.5 Flash, Kimi K2 and DeepSeek V3.2, mostly not the newest models. Continuation scenarios are partly synthetic.

**For your work**
When your agents hand work to a subagent or a fresh context (compaction, a new session), pass a structured state object (decisions, facts, completed actions, open items) rather than a prose summary, and test the receiver on whether it repeats or undoes finished work.

**Method**
- 1,039 tasks: recovering relevant repository evidence, and continuing from conversational, tool and file-work state.
- Compares handoff representations: recent transcript, narrative summary and structured state.
- Checks the receiver's next responses and actions for kept commitments, updated facts and respect for completed operations.

**Problem**
In long or multi-agent workflows, responsibility passes between models before the job is done. The receiver must keep prior decisions, facts and completed actions, and neither task-success nor memory-retention scores capture whether it does.

**Results**
- Structured state improves repository evidence recovery for every receiver and continuation for most.
- Structured state beats narrative summaries by 5.42 points in mean score and 9.3 points in all-criteria pass rate.
- All-criteria pass rate rises 7.44-12.18 points for all six receivers; the best receiver differs between the two tracks.

**Concepts:** [[Multi-agent systems]] · [[Agent memory]] · [[Evals and benchmarks]]
**From:** [[2026-10-28]]

# My notes


---
# References
[arXiv 2610.36523](https://arxiv.org/abs/2610.36523)
