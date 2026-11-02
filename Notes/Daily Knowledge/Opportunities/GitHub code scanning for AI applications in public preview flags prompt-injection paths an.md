---
date: 2026-11-02
section: AI
importance: Med
kind: value
source: "GitHub changelog"
url: https://github.blog/changelog/2026-10-28-code-scanning-for-ai-applications-in-public-preview
status: unread
id: 2026-11-02-github-ai-app-code-scanning
---
2026-11-02 07:16
Tags: #daily-knowledge #ai

---
# GitHub code scanning for AI applications in public preview flags prompt-injection paths an

GitHub Advanced Security now scans pull requests for AI-specific risks: indirect prompt injection (XPIA), sensitive information disclosure and excessive agency. It flags agent code paths where untrusted content can reach a model with access to tools, data or business systems, and gives mitigation guidance in the PR.

## Details

**What it is**
A new code scanning capability that runs automatically on pull requests alongside CodeQL and posts alerts on the Conversation or Files changed tab. GitHub calls indirect prompt injection the top risk in the OWASP Top 10 for LLM Applications.

**Client use cases**
- Secure SDLC for teams building agents and LLM apps
- Pre-merge checks on agents that read untrusted files, web pages or issue comments
- Evidence for AI governance and risk reviews

**How we could offer it**
- AI application security assessment using the scanner plus manual threat modelling
- Rollout across client repos with triage and remediation playbooks
- Combine with agent permission reviews (least privilege) as a governance service

**Pitch**
Catch prompt-injection and over-privileged agent designs at pull-request time, before they reach production.

**Availability and price**
Public preview on github.com, not on GitHub Enterprise Server. Requires a GitHub Advanced Security licence with code scanning and AI applications scanning enabled. No extra pricing stated.

**Caveats**
Preview; the changelog does not list supported languages or frameworks, and coverage of other AI risks is still expanding.

**Concepts:** [[Agent security]] · [[GitHub Copilot]]
**From:** [[2026-11-02]]

# My notes


---
# References
[GitHub changelog](https://github.blog/changelog/2026-10-28-code-scanning-for-ai-applications-in-public-preview)
