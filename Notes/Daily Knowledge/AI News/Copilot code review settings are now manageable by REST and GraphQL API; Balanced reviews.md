---
date: 2026-11-07
section: AI
importance: Med
kind: news
source: "GitHub Changelog"
url: https://github.blog/changelog/2026-11-06-copilot-code-review-api-management-and-review-overview-updates
status: unread
id: 2026-11-07-copilot-code-review-api
---
2026-11-07 07:16
Tags: #daily-knowledge #ai

---
# Copilot code review settings are now manageable by REST and GraphQL API; Balanced reviews

GitHub now lets enterprise, organization and repository admins manage Copilot code review through the REST and GraphQL APIs, including enablement, default review effort and runners. Balanced-effort reviews now use three reviewer models with another model merging their findings, and agent sessions show the AI credits each review consumed.

## Details

**Caveats**
Applies to Pro, Pro+, Max, Business and Enterprise plans; credit cost per effort level is shown per session, not listed in the post.

**For your work**
Lets you script a consistent review policy across client repos and track spend per review, useful for Copilot rollout engagements.

**Method**
- Enterprise admins enable/disable for all orgs or delegate; org admins set enablement, default effort and runner; repo admins set effort and use of custom instructions and MCP tools
- Repo endpoints accept GitHub Apps and fine-grained tokens (Administration read/write); enterprise and org endpoints do not
- Comments now attribute which skills, MCP servers and custom instructions were cited

**Problem**
Rolling Copilot code review out across many orgs and repos meant clicking through settings pages, with little visibility into cost or why files were skipped.

**Results**
- Balanced effort: three reviewer models plus a combining model
- Failed or timed-out reviews retry once and can switch to another eligible model
- Auto-review rule gets a bypass list; unrelated findings on re-reviews are collapsed then hidden

**Concepts:** [[GitHub Copilot]] · [[Coding agents]]
**From:** [[2026-11-07]]

# My notes


---
# References
[GitHub Changelog](https://github.blog/changelog/2026-11-06-copilot-code-review-api-management-and-review-overview-updates)
