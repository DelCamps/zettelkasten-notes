---
date: 2026-10-30
section: AI
importance: High
kind: news
source: "Claude Code changelog"
url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21314
status: unread
id: 2026-10-30-claude-code-2-1-314
---
2026-10-30 07:16
Tags: #daily-knowledge #ai

---
# Claude Code 2.1.314 hard block on writes outside the workspace, idle compaction, admin eff

Claude Code 2.1.314 adds permissions.blockWritesOutsideWorkingDirectories, which makes Write, Edit and NotebookEdit refuse paths outside the working directories in every permission mode, and idle compaction for 200K+ token conversations in VS Code and the Desktop Code tab. It also fixes sessions failing with 'Invalid effort level' when an admin caps effort, and claude -p exiting 0 with no output on startup failure.

## Details

**Caveats**
Changelog only; published to npm at 00:12 UTC on 30 October. There is no 2.1.313 entry. Idle compaction changes what the model sees after a pause.

**For your work**
Turn on blockWritesOutsideWorkingDirectories for client repos, and if your CI wraps claude -p, rely on the exit code now instead of checking for empty output.

**Method**
- New setting permissions.blockWritesOutsideWorkingDirectories applies in every permission mode, including auto.
- Idle compaction: a 200K+ token conversation left idle is summarized and the summary used if the prompt cache has expired; now also on Bedrock, Vertex, Foundry and gateways once the one-hour prompt cache is on.
- Gateway: per-upstream IdP groups and a Bedrock guardrail_trace that logs which filter fired without the matched text.

**Problem**
Agents editing files outside the repo, sessions breaking under org-level effort caps, and silent failures in headless runs are recurring pain points for teams deploying Claude Code.

**Results**
- Effort-capped orgs: Claude Code now lowers the effort, retries and says which level it uses.
- claude -p now prints the startup error and exits 1.
- PreCompact hook output is cut at 10,000 characters; Bash-matching hooks now also run on Monitor tool commands.
- Sandbox protections now apply to worktrees entered by claude -p --resume or --continue.

**Concepts:** [[Claude]] · [[Coding agents]] · [[Agent security]]
**From:** [[2026-10-30]]

# My notes


---
# References
[Claude Code changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21314)
