---
date: 2026-11-14
section: AI
importance: High
kind: news
source: "Claude Code changelog"
url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
status: unread
id: 2026-11-14-claude-code-2-1-325
---
2026-11-14 07:16
Tags: #daily-knowledge #ai #update

---
# Claude Code 2.1.325 sandboxed Bash commands now ask for permission by default, plus a long

Claude Code 2.1.325 changes sandboxed Bash to follow the normal permission flow unless sandbox.autoAllowBashIfSandboxed is set to true, and makes scheduled tasks and /loop ask before running skills that declare allowed-tools or hooks. It also fixes a zstd decoding security issue and several cases where deny rules, compound Bash commands or allow rules let commands run without the expected check.

## Details

**Caveats**
The new default may make existing unattended sandboxed jobs stop and wait for approval.

**For your work**
Before upgrading client CI or scheduled agents, decide whether to set autoAllowBashIfSandboxed and add Skill(name) allow rules, then re-test unattended runs.

**Method**
- Sandboxed Bash now goes through normal permission prompts by default; set sandbox.autoAllowBashIfSandboxed: true (in the highest-ranking managed source for orgs) to keep the old no-prompt behaviour
- Read-only git commands in an untrusted repository now ask first; scheduled tasks ask before running skills that declare allowed-tools or hooks
- The sandbox now refuses writes to .claude settings, skills, agents, commands and hooks in added directories, and helper programs run without sign-in tokens or API keys in their environment
- Plugin loading skips unsafe paths and links; plugin install warnings say plugins can run code with access to files and shell

**Problem**
Agents running unattended or inside a sandbox could run commands, or rely on rules, that skipped the permission checks admins expected.

**Results**
- Fixed: a security issue in zstd-compressed response decoding; a Bash allow rule running a different program than named; compound commands running without asking; some deny and ask rules not applying
- Cloud sessions now keep MCP tool descriptions up to 16,384 characters, not 4,096
- claude remote-control exits with status 4 or 69 so service managers can restart it

**Concepts:** [[Claude]] · [[Coding agents]] · [[Agent security]]
**From:** [[2026-11-14]]

# My notes


---
# References
[Claude Code changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
