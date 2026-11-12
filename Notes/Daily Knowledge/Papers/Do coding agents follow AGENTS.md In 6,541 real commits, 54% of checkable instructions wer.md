---
date: 2026-11-12
section: AI
importance: High
kind: paper
source: "arXiv 2611.13709"
url: https://arxiv.org/abs/2611.13709
status: unread
id: 2026-11-12-agents-md-compliance
---
2026-11-12 07:16
Tags: #daily-knowledge #ai

---
# Do coding agents follow AGENTS.md In 6,541 real commits, 54% of checkable instructions wer

Researchers turned instructions from real agent context files (AGENTS.md, CLAUDE.md, copilot-instructions.md) into executable checks and ran them on the commits the agents later made. Mean compliance was 59.8%, but it splits in two: 54.4% of instructions were followed every time and 37.3% never. Copilot-authored commits complied more often (66.0%) than Claude Code (52.2%) or Codex (51.2%). Tested on: 621 context-file snapshots, 6,541 agent-authored commits in 268 public GitHub repos, 3 agents (Claude Code, GitHub Copilot, OpenAI Codex); observational, no ablation.

## Details

**Caveats**
Observational: no counterfactual without the instruction, so some 'compliance' may be model defaults. The median instruction has only 3 applicable commits and 26.3% have exactly one, so per-instruction rates are rough. Agent differences may reflect what each agent's files ask for, and the Development Process gap does not survive once thin-evidence instructions are dropped.

**For your work**
Treat AGENTS.md/CLAUDE.md as advice, not a control. Rules about process, architecture and testing need enforcement outside the file (hooks, CI checks, linters). The paper's script-per-instruction idea is a cheap way to audit whether a client's own context files are actually obeyed.

**Method**
- Extracted 6,552 explicit, actionable, observable instructions from 621 real context-file snapshots, using an LLM classifier checked by hand on a sample.
- Generated a measurement script per instruction with test-driven code generation; 62.9% could be operationalized into scripts.
- Ran the scripts on agent-authored commits made under the matching snapshot; 2,053 instructions had at least one applicable commit (18,594 instruction-commit pairs).

**Problem**
Teams steer coding agents with project context files and assume what they write there is carried out. Nobody had checked, instruction by instruction, whether the agents' commits actually do what the file says.

**Results**
- Mean compliance 59.8%, median 100%: 1,116 instructions (54.4%) followed in every applicable commit, 766 (37.3%) in none, only 8.3% in between.
- Development Process instructions complied least (mean 34.0%, median 0%), Architecture 38.2%, Testing 49.2%; Build and Run reached 69.9%, Documentation 60.2%.
- Copilot 66.0% mean compliance versus Claude Code 52.2% and Codex 51.2%; Claude Code and Codex statistically the same.

**Concepts:** [[Coding agents]] · [[GitHub Copilot]] · [[Evals and benchmarks]]
**From:** [[2026-11-12]]

# My notes


---
# References
[arXiv 2611.13709](https://arxiv.org/abs/2611.13709)
