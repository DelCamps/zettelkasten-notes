---
date: 2026-10-26
section: AI
importance: High
kind: paper
source: "arXiv 2610.31710"
url: https://arxiv.org/abs/2610.31710
status: unread
id: 2026-10-26-compact-bench
---
2026-10-26 07:16
Tags: #daily-knowledge #ai

---
# Compact-Bench context compaction silently breaks 5-64% of coding-agent repairs

A new benchmark resumes the same coding task from full history or from a compaction summary only. Across 14 summarizer models, 5-64% of 22 tasks that the full-history agent solves are lost after compaction; Claude Opus 4.8 loses the fewest. LLM summaries keep at most 16% of details that recur later, versus 79.1% for mechanical extraction.

## Details

**Caveats**
Only 22 validated full-history successes in the controlled part, one continuation agent and budget; detail retention measures literal recurrence; private session data is not released.

**For your work**
If your agents compact context, keep a mechanical state record (files touched, tests run, decisions, todo list) next to the LLM summary instead of trusting the summary alone, and test compaction by resuming tasks from a summary-only state.

**Method**
- Task Preservation: from a shared repository snapshot, continue 35 SWE-bench repairs with the full history or with only a summary, same agent, step budget and tests.
- Recurring-Detail Retention: 146 agent sessions (143 real), scoring whether structured details that later requests need survive the summary.
- Production-Chain Retention: follows details across successive real compactions in 106 sessions.
- Compares 14 summarizer backbones and 5 production compaction prompts (Claude Code, Kimi Code and others).

**Problem**
Long-horizon coding agents compact their context when it fills up, but a summary can drop the progress needed to finish: which steps are done, which hypotheses were rejected, what remains. End-to-end scores hide the effect of one specific history replacement.

**Results**
- Stable damage ranges from 5% to 64% of the 22 full-history successes; Claude Opus 4.8 preserves the most repairs, DeepSeek-Flash damages the most.
- With Kimi-K3 as summarizer, the Kimi Code prompt preserves the most continuations (19/22), while the Claude Code prompt keeps the most recurring details (15.0%).
- LLM summaries keep at most 16.0% of recurring details versus 79.1% for mechanical extraction; production summaries keep 15.7% at the first boundary.
- One repair is broken by 13 of 14 backbones: summaries keep the target file and strings but lose the progress state.

**Concepts:** [[Coding agents]] · [[Agent memory]] · [[Evals and benchmarks]]
**From:** [[2026-10-26]]

# My notes


---
# References
[arXiv 2610.31710](https://arxiv.org/abs/2610.31710)
