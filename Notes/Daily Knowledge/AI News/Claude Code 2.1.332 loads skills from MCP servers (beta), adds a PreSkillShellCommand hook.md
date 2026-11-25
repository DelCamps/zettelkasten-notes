---
date: 2026-11-25
section: AI
importance: High
kind: news
source: "Claude Code changelog"
url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
status: unread
id: 2026-11-25-claude-code-2-1-332
---
2026-11-25 07:16
Tags: #daily-knowledge #ai #update

---
# Claude Code 2.1.332 loads skills from MCP servers (beta), adds a PreSkillShellCommand hook

Claude Code 2.1.332 (published 24 November) lets MCP servers ship skills, shown as server:skill in the / menu, and adds a hook that can refuse a skill's inline shell commands as it loads. On Microsoft Foundry the default model is now Sonnet 5.5, the sonnet alias on Foundry and Google Cloud's Agent Platform points to Sonnet 5.5 and Foundry's opus alias to Opus 5.5; Sonnet 4, Opus 4 and Opus 4.1 count as retired on Foundry.

## Details

**Caveats**
MCP skills are beta. Settings that name the new hook open a dialog on 2.1.331 and older. Dashboards filtering on service.name claude-code will miss desktop sessions unless updated. Self-hosted runner OAuth tokens may now start oat02-, so scrubbers matching only oat01- need updating.

**For your work**
If clients run Claude Code on Azure Foundry, check that claude-sonnet-5-5 is deployed before upgrading. MCP-delivered skills are a way to distribute team skills centrally, and the new hook gives you a control point to vet their shell commands.

**Method**
- Skills from MCP servers (beta), named server:skill; a new PreSkillShellCommand hook event can block a skill's or command's inline shell commands at load time
- Model step-down: --model default and enforced availableModels lists now fall back to an older model of the same family instead of erroring on Bedrock, Agent Platform and Foundry
- Foundry default switches to Sonnet 5.5 (deploy claude-sonnet-5-5 or set ANTHROPIC_DEFAULT_SONNET_MODEL); sonnet on Bedrock stays at Sonnet 4.5
- Desktop Code tab sessions now report OpenTelemetry service.name claude-code-desktop; new assistant_response OTel event

**Problem**
Teams running Claude Code on cloud providers hit model-availability failures, skills could only come from local files, and long hook or MCP output could freeze sessions.

**Results**
- Hook or blocked-turn output over about 50,000 characters is now shortened to stop freezes and context overflow
- Reads of named pipes nothing writes to (e.g. a locked secrets-manager .env) now fail after 20 seconds instead of hanging
- Compaction asks for a shorter summary after three cut-off replies
- Tap-mode dictation now stays on until 60 seconds of silence or 10 minutes, up from 15 seconds and 2 minutes

**Concepts:** [[Claude]] · [[Coding agents]] · [[Agent security]]
**From:** [[2026-11-25]]

# My notes


---
# References
[Claude Code changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
