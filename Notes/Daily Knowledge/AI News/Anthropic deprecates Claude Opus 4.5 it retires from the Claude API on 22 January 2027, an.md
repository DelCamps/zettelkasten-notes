---
date: 2026-11-24
section: AI
importance: Med
kind: news
source: "Claude API release notes"
url: https://platform.claude.com/docs/en/about-claude/model-deprecations
status: unread
id: 2026-11-24-claude-opus-4-5-deprecation
---
2026-11-24 07:16
Tags: #daily-knowledge #ai

---
# Anthropic deprecates Claude Opus 4.5 it retires from the Claude API on 22 January 2027, an

Anthropic announced the deprecation of Claude Opus 4.5 (claude-opus-4-5-20251101 and the claude-opus-4-5 alias) on 23 November. Retirement on the Claude API is scheduled for 22 January 2027, with a migration guide to Claude Opus 5.5; other platforms' dates are on the model-deprecations page.

## Details

**Caveats**
- Dates on Bedrock, Google Cloud and Foundry may differ; check the deprecations page
- Moving to a new model can change prompt behaviour, costs and latency, so re-run evals before switching

**For your work**
Search client code and config for claude-opus-4-5 now, schedule an eval-backed migration to Opus 5.5 in December, and check each cloud platform's own retirement date.

**Method**
- Deprecation covers claude-opus-4-5-20251101 and the claude-opus-4-5 alias
- Retirement on the Claude API on 22 January 2027
- Migration guide: 'Migrating from Claude Opus 4.5 or earlier' to Claude Opus 5.5; Bedrock, Vertex and Foundry dates listed separately

**Problem**
Clients with production apps pinned to Opus 4.5 have about two months before API calls to it stop working.

**Results**
- About two months of runway on the Claude API
- Same release note also launched Enterprise Frontier Safeguards in beta and two storage webhooks

**Concepts:** [[Claude]] · [[Model releases and pricing]]
**From:** [[2026-11-24]]

# My notes


---
# References
[Claude API release notes](https://platform.claude.com/docs/en/about-claude/model-deprecations)
