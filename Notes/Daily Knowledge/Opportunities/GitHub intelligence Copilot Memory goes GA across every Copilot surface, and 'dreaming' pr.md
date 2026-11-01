---
date: 2026-11-01
section: AI
importance: Med
kind: value
source: "GitHub changelog"
url: https://github.blog/changelog/2026-10-28-github-intelligence-puts-your-code-context-and-history-to-work
status: unread
id: 2026-11-01-github-intelligence-memory
---
2026-11-01 07:16
Tags: #daily-knowledge #ai

---
# GitHub intelligence Copilot Memory goes GA across every Copilot surface, and 'dreaming' pr

GitHub launched 'GitHub intelligence', a context layer for its agents. Copilot Memory is now generally available on paid plans and follows the developer across the Copilot app, CLI, VS Code, cloud agent, code review, Slack, Teams and Mobile; GitHub says CLI sessions that used memory showed better adherence to preferences in 93% of cases. 'Dreaming' (opt-in preview) reviews past work and proposes changes to skills and instruction files as pull requests.

## Details

**Availability and price**
Memory: GA on paid Copilot plans. Dreaming: public preview, opt-in at user, org and enterprise policy level; dream runs consume AI credits (rates not listed). Code Search: no availability tier stated. No other pricing given.

**Caveats**
The 93% and 42% figures are GitHub's own preview telemetry, not an independent eval. Memories are a new store of potentially sensitive context that clients will want to audit. Dreaming's credit cost is unknown.

**Client use cases**
- Large enterprises with many repos: agents that remember house conventions instead of re-reading long instruction files.
- Code-review standardisation: turn recurring review comments into written guidance automatically.
- Cross-repo migrations and audits using /research over code search.

**How we could offer it**
- Copilot adoption assessment: which memory and dreaming policies to enable, per org and repo.
- Governance: set Copilot Memory repository access, review dreaming PRs, define who can approve instruction changes.
- Managed service: periodic review of memories and instruction files for quality and data leakage.

**Pitch**
Copilot now remembers each team's conventions across every tool and can propose its own instruction updates as PRs. That makes a governance and adoption service around Copilot Memory an easy add-on for our Copilot Enterprise clients.

**What it is**
Three capabilities. Memory (GA): Copilot creates and curates memories automatically and users can view or delete them. Dreaming (public preview, opt-in): personal memory curation, repository customization (updates repo memories and proposes changes to skills and custom instruction files) and code-review customization (turns recurring accepted review feedback into guidance); checked-in changes arrive as PRs. Code Search: Copilot can search code, config, schemas and docs across related repositories without a local clone, with exact, regex and semantic search, and a /research command for cross-repo work.

**Concepts:** [[GitHub Copilot]] · [[Agent memory]] · [[Coding agents]]
**From:** [[2026-11-01]]

# My notes


---
# References
[GitHub changelog](https://github.blog/changelog/2026-10-28-github-intelligence-puts-your-code-context-and-history-to-work)
