---
date: 2026-11-02
section: AI
importance: Low
kind: paper
source: "arXiv 2610.40753"
url: https://arxiv.org/abs/2610.40753
status: unread
id: 2026-11-02-caper-consequence-aware-approval
---
2026-11-02 07:16
Tags: #daily-knowledge #ai

---
# Caper (one agent, one approver model, single run) approving shell commands by dry-running

Instead of judging command text, Caper pre-runs each shell command under system-call tracing in a snapshotted Docker container. It then gives an LLM approver a compact report of the effects and rolls back blocked commands with a reason the agent can act on. Harmful outcomes fall to 6.7% on SABER, against 14.8% for Claude Code Auto Mode and 19.7% with no approver, and to 7.8% on YoloFS-Ext (at least 35.3% for the other systems), while blocking 1.0% of safe twins. Tested on: one agent model (GLM-5.3-Flash), one approver model (gpt-5.6-luna), one run per task, 682 SABER and 204 YoloFS-Ext tasks, compared with six existing approvers.

## Details

**Problem**
Rule checkers, guard models and Claude Code Auto Mode judge the text of a command. But 'make clean' can wipe src/ and .git/ in one repo and only build/ in another.

**Method**
- Snapshot the container with outbound network off, run the command under strace -f, and hold its output back until the decision.
- Reduce the trace to an effects report: file changes with diffs, network attempts, reads of secrets such as .env, output, and which process caused each. The report is 99.4% smaller than the raw trace.
- If the approver allows it, keep the state; if it blocks it, restore the snapshot and tell the agent why.

**Results**
- Used as a Claude Code hook, it lowers harm from 14.8% to 10.0% on SABER and from 62.7% to 6.9% on YoloFS-Ext.
- The same approver without the effects report blocks 61.8% of safe twins; with the report it blocks 84.3% of harmful commands and 1.0% of safe twins.
- Median approval latency 3.2 s; $0.019 per task vs $0.017 without evidence.

**Caveats**
Pre-execution is real, so effects that leave the container cannot be undone. It covers shell commands only and observes one run, and no adaptive attacker (sandbox detection, delayed harm) was tested.

**For your work**
A useful pattern for agent permission gates in client deployments: let the approver judge what a command actually did in a sandbox, not just its text.

**Concepts:** [[Agent security]] · [[Coding agents]]
**From:** [[2026-11-02]]

# My notes


---
# References
[arXiv 2610.40753](https://arxiv.org/abs/2610.40753)
