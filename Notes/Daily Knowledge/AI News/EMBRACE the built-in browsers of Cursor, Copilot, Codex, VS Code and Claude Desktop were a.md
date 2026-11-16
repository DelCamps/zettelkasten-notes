---
date: 2026-10-30
section: AI
importance: High
kind: news
source: "Forever Security"
url: https://forever.security/blog/embrace-hacking-5-ai-assistants-embedded-browsers-technical
status: unread
id: 2026-10-30-embrace-ai-ide-browsers
---
2026-10-30 07:16
Tags: #daily-knowledge #ai

---
# EMBRACE the built-in browsers of Cursor, Copilot, Codex, VS Code and Claude Desktop were a

Forever Security broke a core browser-security rule in the embedded browsers of five AI coding assistants, from host code execution in Cursor to reading every file on disk in Codex, Claude Desktop and VS Code. Codex (reported 27 July) and VS Code are still unpatched; Microsoft and, at first, Anthropic declined the reports under 'Workspace Trust'.

## Details

**Caveats**
Vendor write-up; the Cursor exploit depends on the model. The file-read attack needs one click on a file:// link, which the assistant itself renders. Claude Desktop's fix status is not stated explicitly.

**For your work**
Treat 'trust this folder' as no boundary: open unknown repos only in a VM or container, don't click agent-generated file:// links, and keep secrets out of the home directory of machines running coding agents.

**Method**
- Cursor: any page can call window.cursorBrowser.send("element-selected", ...), injecting a hidden 'chip' into the agent's composer; the payload splits npm install across attributes so the agent reassembles it, auto-run surfaces a one-keystroke card, and when the sandbox blocks it the agent retries without the sandbox.
- Copilot: page JavaScript called the Tauri command submit_browser_preview_url_change to report a fake address (github.com/login) shown to the user and the agent.
- Claude Desktop, VS Code: the project-scope file:// fence runs only in the top document, so a web worker built from a Blob can fetch any file; Codex had no fence at all. macOS .DS_Store files are parsed to walk the whole disk.

**Problem**
AI assistants now embed a browser the agent drives, and each vendor relaxed a normal browser rule so previews and the agent could work. Those relaxations let a hostile page or project file attack the developer.

**Results**
- Cursor: host code execution (probabilistic); disclosed 10 September, silently patched 1 October.
- Copilot: confirmed on 1.1.27, fixed independently in 1.1.29 on 13 October.
- File-read sweep pulled SSH keys, .env files and npm tokens. Codex and VS Code remain open at publication.

**Concepts:** [[Agent security]] · [[Coding agents]] · [[GitHub Copilot]]
**From:** [[2026-10-30]]

# My notes


---
# References
[Forever Security](https://forever.security/blog/embrace-hacking-5-ai-assistants-embedded-browsers-technical)
