---
date: 2026-11-24
section: AI
importance: Med
kind: paper
source: "arXiv 2611.27090"
url: https://arxiv.org/abs/2611.27090
status: unread
id: 2026-11-24-agent-recovery-50-harnesses
---
2026-11-24 07:16
Tags: #daily-knowledge #ai

---
# Agent recovery in the wild across 50 harnesses and runtimes, only 19 of 128 real-use repor

Under a frozen protocol, the authors graded 12 persistent agent runtimes, 26 coding-agent harnesses and 12 research runtimes on eight recovery mechanisms using public evidence. Recovery is used almost everywhere (25 of 26 harnesses have real-use reports), but of 128 reports only 19 describe the run fully recovering, 54 are partial and 45 failed; checkpoint/resume recovered once in 27 reports and rollback once in 15. Tested on: 50 systems, public issue trackers and reports, two blind coding passes.

## Details

**Caveats**
- Issue trackers over-represent failures, so these are not failure rates
- Six of seven top-evidence systems rest on a single operator's report
- Public evidence only, within a bounded search

**For your work**
Do not sell 'undo' as a safety control for client agents. Design for external side effects explicitly: dry runs, approvals before irreversible actions, idempotent tools and compensating actions you have actually tested.

**Method**
- Three strata fixed in advance: 12 persistent runtimes (e.g. OpenHands, Letta, Dify, n8n), 26 coding harnesses, 12 research runtimes
- Eight recovery mechanisms graded from 'not found' to 'exercised in a real run', with two blind coding passes, adjudication and archived sources
- Protocol and codebook hashed and timestamped before data collection, with all 21 departures logged

**Problem**
Coding agents and long-running agents can delete files or crash mid-task, and users rely on recovery mechanisms (checkpoints, undo, approvals, logs). Research offers stronger guarantees such as saga-style compensation and transactional rollback, but nobody had checked whether any of it works in real use.

**Results**
- 11 of 12 runtimes and 25 of 26 harnesses have at least one real-use recovery report
- Of 128 reports: 19 full recovery, 54 partial, 45 failed
- Checkpoint/resume recovered once in 27 reports; rollback once in 15
- Compensation of external effects, research's central guarantee, is offered by no harness, and no research runtime is shown in operation

**Concepts:** [[Agents]] · [[Coding agents]] · [[AI safety]]
**From:** [[2026-11-24]]

# My notes


---
# References
[arXiv 2611.27090](https://arxiv.org/abs/2611.27090)
