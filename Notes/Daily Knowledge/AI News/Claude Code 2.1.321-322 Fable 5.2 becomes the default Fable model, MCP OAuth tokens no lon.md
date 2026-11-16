---
date: 2026-11-10
section: AI
importance: High
kind: news
source: "Claude Code changelog"
url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
status: unread
id: 2026-11-10-claude-code-2-1-321
---
2026-11-10 07:16
Tags: #daily-knowledge #ai #update

---
# Claude Code 2.1.321-322 Fable 5.2 becomes the default Fable model, MCP OAuth tokens no lon

Claude Code 2.1.321 (9 Nov) makes Claude Fable 5.2 the default Fable model, with 1M context at $8/$40 per million tokens. It also fixes several security gaps: MCP OAuth refresh tokens sent to another host after a redirect, a read-only Bash command run outside the sandbox without a prompt, and deny rules missed by cp and mv. Version 2.1.322 (10 Nov) adds fast mode on Vertex.

## Details

**Caveats**
The changelog gives no CVEs or severity ratings for the security fixes. Release dates come from npm publish times: 2.1.321 on 9 Nov 19:02 UTC and 2.1.322 on 10 Nov 01:58 UTC.

**For your work**
Update now, especially on machines using remote MCP servers with OAuth or relying on deny rules. If you run Claude Code on Vertex, fast mode is now an option there.

**Method**
- New model: claude-fable-5-2 is the default Fable model, with 1M context, $8/$40 per million tokens and $0.20 for cache reads.
- Security fixes: MCP OAuth secrets such as refresh tokens were sent to another host when a server redirected. A read-only Bash command could run outside the sandbox without a prompt. Bash checks judged a write from the wrong folder. Deny rules and protected-file prompts missed files that cp or mv wrote into a directory.
- New flag: claude remote-control --settings <file> applies one settings file to every session it starts.
- 2.1.322 adds fast mode on Vertex in the global, us and eu regions, and falls back to standard speed if Vertex refuses.

**Problem**
This release adds Fable 5.2 and closes several holes in the permission system and MCP sign-in.

**Results**
- When fast serving is rate-limited or failing, fast mode now tries standard speed on the same model instead of switching models or retrying for minutes.
- Edit and NotebookEdit no longer change the wrong match or overwrite cells on network paths (UNC shares, WSL folders, /net mounts).
- Claude now refuses to send files whose names hide text-direction or control characters, and skill names that some fonts draw as blank.

**Concepts:** [[Claude]] · [[Coding agents]] · [[Agent security]]
**From:** [[2026-11-10]]

# My notes


---
# References
[Claude Code changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
