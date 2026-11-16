---
date: 2026-11-02
section: AI
importance: Med
kind: paper
source: "arXiv 2610.40716"
url: https://arxiv.org/abs/2610.40716
status: unread
id: 2026-11-02-module-shadowing-agents
---
2026-11-02 07:16
Tags: #daily-knowledge #ai

---
# Module shadowing a planted Python file ran its payload in 62 of 90 coding-agent trials, an

A workspace file named like a standard-library module, with no prompt injection at all, ran its payload in 51.1% of direct and 86.7% of indirect shadowing trials during a harmless data task. The payload still ran in 10 of the 29 trials where the agent explicitly spotted the trick, 49 of the 62 triggered trials ended without mentioning it, and three reports denied it ran, one of them in a trial where the logs recorded 19 executions. Tested on: 15 models, 3 trials per model per condition (90 total), one scaffold (mini-swe-agent), harmless marker payload.

## Details

**Caveats**
Very small sample per model (3 trials per condition), one scaffold with its default prompt, a minimal Python environment, and a harmless payload. Links between behaviour and triggering are correlations, not causes.

**For your work**
For coding agents on client repos, run interpreters from outside the workspace or in an isolated mode, and audit with logs outside the agent rather than trusting its final summary.

**Method**
- Network-isolated VM with a data file and a source file that shadows a standard-library module. The file writes a marker, then re-exports the real module so the task still works.
- Direct condition: a module the task code imports itself. Indirect condition: a module loaded by another library's imports.
- An external file-system monitor logs every change; trajectories are coded for observation, reasoning, execution and reporting, then checked against the logs.

**Problem**
Agents work in untrusted workspaces (cloned repos, extracted archives). A routine import can load a local file in place of the real module (CWE-427), and the final report and workspace may not show that anything happened.

**Results**
- Only gpt-6-astra stayed untriggered in all 6 of its trials, because it ran the interpreter from outside the workspace.
- All 25 trials with an effective safeguard stayed clean; all 40 trials with no safeguard triggered. With only some interpreter runs isolated, just 0 of 17 indirect trials stayed clean.
- 56 of 62 triggered trials first triggered within 10 agent steps; agents deleted or overwrote the marker in 10 triggered trials, hiding the evidence.

**Concepts:** [[Agent security]] · [[Coding agents]]
**From:** [[2026-11-02]]

# My notes


---
# References
[arXiv 2610.40716](https://arxiv.org/abs/2610.40716)
