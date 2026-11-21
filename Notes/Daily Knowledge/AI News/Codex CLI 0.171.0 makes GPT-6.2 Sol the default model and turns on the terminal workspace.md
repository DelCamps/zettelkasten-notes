---
date: 2026-11-21
section: AI
importance: Low
kind: news
source: "Codex changelog"
url: https://learn.chatgpt.com/docs/changelog
status: unread
id: 2026-11-21-codex-cli-0-171
---
2026-11-21 07:16
Tags: #daily-knowledge #ai #update

---
# Codex CLI 0.171.0 makes GPT-6.2 Sol the default model and turns on the terminal workspace

Codex CLI 0.171.0 adds GPT-6.2 Sol and Astra to the model catalogs with Sol as the default selection, enables the TUI workspace by default with searchable document previews, image previews and subagent transcripts, and adds codex exec --remote plus /rc and /remote for remote control. Fixes keep drafts across session switches and fix enterprise MCP sign-in for providers without refresh tokens.

## Details

**Caveats**
Release notes only; no benchmark or pricing changes. The default switch affects which model teams are billed for unless they pin one.

**For your work**
If client teams use Codex CLI, pin the model explicitly in config so the upgrade does not silently change cost or behavior; remote exec is useful for running Codex against a shared app server in CI.

**Method**
- GPT-6.2 Sol and Astra added to model catalogs; Sol is the default catalog selection.
- TUI workspace on by default, with searchable document previews, image previews and subagent transcripts.
- codex exec --remote starts or resumes noninteractive sessions on an existing app server; /rc and /remote manage remote control and pairing codes.
- Undo and redo in the prompt composer; custom MCP status lines via /statusline.

**Problem**
Codex users needed the new GPT-6.2 models in the CLI and better ways to run and steer sessions remotely.

**Results**
- Drafts and queued input now survive session switches.
- Permission profiles stay intact when the working directory changes.
- Enterprise MCP sign-in now works for providers that do not issue refresh tokens.

**Concepts:** [[Coding agents]] · [[OpenAI enterprise]]
**From:** [[2026-11-21]]

# My notes


---
# References
[Codex changelog](https://learn.chatgpt.com/docs/changelog)
