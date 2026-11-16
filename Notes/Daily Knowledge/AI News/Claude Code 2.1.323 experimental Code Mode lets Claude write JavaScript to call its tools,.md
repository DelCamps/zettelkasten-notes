---
date: 2026-11-13
section: AI
importance: High
kind: news
source: "Claude Code changelog"
url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21323
status: unread
id: 2026-11-13-claude-code-2-1-323-code-mode
---
2026-11-13 07:16
Tags: #daily-knowledge #ai

---
# Claude Code 2.1.323 experimental Code Mode lets Claude write JavaScript to call its tools,

The new opt-in Code Mode has Claude write JavaScript that calls its tools, and admins can turn it off per organization. The release also closes many Bash permission and sandbox gaps, makes /security-review ask before running, and raises the default context assumed for unknown model IDs from 200K to 1M.

## Details

**Caveats**
Code Mode is experimental and its docs page was not reachable at time of writing; no performance numbers are given.

**For your work**
Check managed settings before rolling out to client teams: decide on Code Mode per org, add engines ranges to internal plugins, and re-test any Bash allow rules with wildcards since several now prompt. Set CLAUDE_CODE_DISABLE_1M_CONTEXT=1 for gateways serving smaller-window models.

**Method**
- Code Mode (experimental, opt-in): Claude writes JavaScript to call tools; organizations can disable it
- Plugins can declare engines["claude-code"] in plugin.json; out-of-range plugins are not installed, updated or loaded; claude plugin validate now type-checks TypeScript hooks (--strict fails on findings)
- Ripgrep and most internal git commands now run without most sign-in tokens and API keys, so credential helpers or hooks under them can't find them; MCP sign-in completion now asks for confirmation even in bypass and auto modes

**Problem**
Calling tools one at a time costs turns and tokens, and the permission layer had several ways for commands to slip past prompts or the sandbox.

**Results**
- Fixed: Bash deny and ask rules missing commands run through sudo, env and similar wrappers; Bash(ls*)-style rules skipping prompts; sandbox.excludedCommands letting unlisted commands out of the sandbox; Write/Edit writing to paths under a Read deny rule
- Fixed: --permission-mode auto starting in a more permissive mode when auto mode was unavailable (now Manual); sandboxed commands reading file checkpoint copies
- Changed: messages your same-machine sessions can send each other without a prompt rise from about 20 to 100,000; macOS/Linux/WSL sandbox ignores write access granted through symlinks

**Concepts:** [[Claude]] · [[Coding agents]] · [[Agent security]]
**From:** [[2026-11-13]]

# My notes


---
# References
[Claude Code changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21323)
