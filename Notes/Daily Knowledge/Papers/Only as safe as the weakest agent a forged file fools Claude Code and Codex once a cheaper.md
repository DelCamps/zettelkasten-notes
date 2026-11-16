---
date: 2026-11-16
section: AI
importance: High
kind: paper
source: "arXiv 2611.17520"
url: https://arxiv.org/abs/2611.17520
status: unread
id: 2026-11-16-weakest-subagent-safety
---
2026-11-16 07:16
Tags: #daily-knowledge #ai

---
# Only as safe as the weakest agent a forged file fools Claude Code and Codex once a cheaper

Strong orchestrators (Opus 5, GPT-5.6-sol) reading a file store themselves almost never adopt a planted forged record (two harmful revisions in 1,080 direct trials), but when they delegate reading to a cheaper sub-agent, as both products recommend, Claude Code fails 75/180 and Codex 44/180. Downstream aggregators repeat a corrupted worker's error in 751/757 trials; giving the aggregator the original record drops errors to 0. Tested on: Claude Code, Codex and a reference harness, plus simulations over 18 models from six developers, 180 fictional facts.

## Details

**Caveats**
Fictional facts, forgeries built to be catchable only by careful readers; Codex delegation was enforced by instruction only; one run per task, and run-to-run disagreement was 13.0%. Vendors were not notified.

**For your work**
Do not put a cheaper model between your agent and evidence its correctness depends on. Make sub-agents quote source records, or have the orchestrator open the cited file before acting; a skeptical verifier cut harm from 15/40 to 1/40.

**Method**
- Plant one forged record (with two fixed tells: wrong date, missing accession line) among genuine files; ask a two-option question
- Compare orchestrator reading directly vs delegating to a weaker or same-tier sub-agent, in unmodified Claude Code and Codex CLIs and a 200-line reference harness
- Controls: clean store, same-tier sub-agent, matched brief; a three-agent attacker-worker-aggregator chain

**Problem**
Coding-agent harnesses delegate file search to cheaper sub-agents. Does a strong orchestrator's resistance to poisoned content survive that hop?

**Results**
- Direct reading: 1/180 (Opus 5) and 0/180 (gpt-5.6-sol); delegated: 75/180 and 44/180
- Same-tier sub-agents stay at 0/180 and 1/180, so the cause is the weaker reader, not delegation
- Weaker sub-agent reports kept the forgery's missing provenance in only 96/180 cases
- Explicit prompt-injection instructions were resisted everywhere; forgeries that look like records worked

**Concepts:** [[Multi-agent systems]] · [[Agent security]] · [[Coding agents]]
**From:** [[2026-11-16]]

# My notes


---
# References
[arXiv 2611.17520](https://arxiv.org/abs/2611.17520)
