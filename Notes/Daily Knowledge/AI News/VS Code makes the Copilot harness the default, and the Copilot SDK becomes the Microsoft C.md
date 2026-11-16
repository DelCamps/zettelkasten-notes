---
date: 2026-10-29
section: AI
importance: Med
kind: news
source: "GitHub changelog"
url: https://github.blog/changelog/2026-10-28-github-copilot-in-vs-code-universe-releases
status: unread
id: 2026-10-29-copilot-harness-vscode
---
2026-10-29 07:16
Tags: #daily-knowledge #ai

---
# VS Code makes the Copilot harness the default, and the Copilot SDK becomes the Microsoft C

New VS Code agent sessions now run on the Copilot harness, built on what is being renamed the Microsoft Copilot SDK. GitHub says this makes agent behaviour more consistent across VS Code, Copilot CLI and the Copilot app. The Universe release also adds cloud sessions, an Agent Host that keeps sessions running after VS Code closes, side-by-side model comparison with a judge model, and experimental computer use with per-app approval.

## Details

**Caveats**
The SDK migration has no timeline or new package names yet. Computer use is experimental.

**For your work**
If you built on the Copilot SDK (e.g. yesterday's GitHub App auth), expect it to move repo and change names. Plan to block computer use by policy on client machines until it has been reviewed.

**Method**
- The Copilot harness is the default for new VS Code sessions; the Agent Host Protocol lets third-party clients share live sessions
- The SDK is renamed Microsoft Copilot SDK, the programmable interface for the shared Microsoft/GitHub harness, and its repo moves to the Microsoft org in phases
- Experimental computer use with per-app approval that orgs can disable by policy; admins can require or block plugins and restrict install sources

**Problem**
Copilot agents behaved differently in each client, and the SDK was GitHub-only while Microsoft wants one agent foundation across its products.

**Results**
- Cloud sessions started from VS Code can be continued in VS Code, the Copilot app, GitHub Mobile, github.com or Copilot CLI
- Model comparison (preview) runs models in parallel with a Judge model and a Synthesize option
- SDK: 'No immediate changes are required for existing users'; package names may keep the old name during the transition

**Concepts:** [[GitHub Copilot]] · [[Coding agents]] · [[Computer-use agents]]
**From:** [[2026-10-29]]

# My notes


---
# References
[GitHub changelog](https://github.blog/changelog/2026-10-28-github-copilot-in-vs-code-universe-releases)
