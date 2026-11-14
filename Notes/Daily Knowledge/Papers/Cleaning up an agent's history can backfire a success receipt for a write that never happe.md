---
date: 2026-11-14
section: AI
importance: Med
kind: paper
source: "arXiv 2611.14654"
url: https://arxiv.org/abs/2611.14654
status: unread
id: 2026-11-14-agent-history-cleaning
---
2026-11-14 07:16
Tags: #daily-knowledge #ai

---
# Cleaning up an agent's history can backfire a success receipt for a write that never happe

Researchers froze agents mid-task and edited the history before another model continued. On AgentCE-Bench, adding the correct value as a truthful note beside the preserved error raised recovery from 51% to 66%, but writing it in as the agent's own completed action lowered it from 50% to 44%; on AppWorld a success receipt helped only when the database change had really happened. Tested on: 8 receiver models from 4 providers (OpenAI, Anthropic, Google, xAI) on AppWorld, 2 of them on AgentCE-Bench (319 frozen states).

## Details

**Caveats**
The primary result rests on two receivers (gpt-5.5, claude-sonnet-5); the edits and states were chosen by the authors; they tested single edits, not a full compaction or hand-off policy.

**For your work**
When summarising or handing off agent context, keep errors visible and add corrections as notes; never mark a step done unless the system state confirms it, and re-check state after compaction.

**Method**
- Froze agents on AgentCE-Bench right after a wrong value was committed; added the correct value either as a truthful note next to the error or as the agent's own completed action; a receiver model continued.
- On AppWorld, froze agents after a database write, kept the success receipt or swapped in a failure receipt, and independently set the database to its state before or after the write.
- Compared against matched neutral notes and unedited histories, with task-family bootstrap intervals.

**Problem**
Compaction, repair and hand-off rewrite what an agent's history says about its own mistakes, while the effects of those mistakes stay in the world (files, databases). Earlier work tested such edits with the world held fixed.

**Results**
- Truthful note: recovery 51% to 66% vs a neutral note. Completed action: 50% to 44% vs the unedited history.
- AppWorld: a success receipt lowered whole-task success from 45% to 28% when the effect was absent and raised it from 38% to 49% when present.
- The 27-point difference was positive in six of eight receivers at 97.5% and seven at 95%.

**Concepts:** [[Agent memory]] · [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-11-14]]

# My notes


---
# References
[arXiv 2611.14654](https://arxiv.org/abs/2611.14654)
