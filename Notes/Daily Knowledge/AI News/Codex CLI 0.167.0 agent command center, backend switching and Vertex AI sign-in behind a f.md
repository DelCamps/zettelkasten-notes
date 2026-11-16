---
date: 2026-11-08
section: AI
importance: Low
kind: news
source: "OpenAI Codex changelog"
url: https://learn.chatgpt.com/docs/changelog
status: unread
id: 2026-11-08-codex-cli-0-167
---
2026-11-08 07:16
Tags: #daily-knowledge #ai

---
# Codex CLI 0.167.0 agent command center, backend switching and Vertex AI sign-in behind a f

OpenAI's Codex CLI 0.167.0 adds an agent command center (codex agents --no-daemon) that marks unread results, lets you switch connected backends without losing drafts, and puts API-key and cloud-provider sign-in under 'Sign in another way', with Google Cloud Vertex AI setup behind a flag.

## Details

**Caveats**
Incremental release; Vertex AI support is flag-gated.

**For your work**
Vertex AI sign-in hints at running Codex against Google Cloud billing for clients standardised on GCP; worth a test once it leaves the flag.

**Method**
- codex agents --no-daemon opens the command center, with unread results marked
- Switch backends from the session picker; saved chats stay visible after changing model provider
- Vertex AI setup behind the gcp_setup_wizard flag; opt into macOS or Windows system proxy settings from /experimental
- Network approval prompts now queue one at a time per endpoint

**Problem**
Running several Codex agents and providers from one terminal was clumsy.

**Results**
- Automatic context compaction now counts output from failed responses and responses missing token usage
- The openai-docs skill now suggests documented replacements when migrating off a deprecated model

**Concepts:** [[Coding agents]]
**From:** [[2026-11-08]]

# My notes


---
# References
[OpenAI Codex changelog](https://learn.chatgpt.com/docs/changelog)
