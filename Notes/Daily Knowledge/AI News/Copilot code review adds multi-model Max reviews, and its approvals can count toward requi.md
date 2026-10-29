---
date: 2026-10-29
section: AI
importance: Med
kind: news
source: "GitHub changelog"
url: https://github.blog/changelog/2026-10-28-copilot-code-review-merge-with-confidence-with-max-and-approvals
status: unread
id: 2026-10-29-copilot-review-max-approvals
---
2026-10-29 07:16
Tags: #daily-knowledge #ai

---
# Copilot code review adds multi-model Max reviews, and its approvals can count toward requi

A new Max review level (public preview) runs several independent review agents on models from different providers, and an aggregation agent reconciles their findings. Copilot approvals are now GA and opt-in: when enabled, they count toward required approvals, limited to file paths admins choose. A new Agent Merge feature has Copilot watch a PR and fix failing workflows or merge conflicts in the cloud.

## Details

**Caveats**
No credit costs, models or accuracy numbers. Max 'takes longer and uses more AI credits'. Letting an AI approval satisfy branch protection weakens two-person review unless the path allowlist is kept tight.

**For your work**
Max is a production example of multi-model review with an aggregator. Treat AI-counted approvals as a governance decision for client repos, not a default.

**Method**
- Max sits alongside Lite and Balanced: several independent review agents on models from different providers, then an aggregation agent that resolves disagreements and checks accuracy
- Approvals are off by default and can be enabled per enterprise, org or repo, with path allowlists; new commits dismiss the approval
- Agent Merge: 'Watch and fix' in the merge box fixes failing Actions runs and/or merge conflicts in a cloud environment; it can be combined with auto-merge

**Problem**
A single-model review misses things on high-risk changes, and agent-generated PRs pile up waiting for human approval and CI fixes.

**Results**
- Max is available on Copilot Pro, Pro+, Max, Business and Enterprise; admins can cap the maximum effort level
- Copilot's approval counts toward branch-protection required approvals when enabled
- Agent Merge's cloud version needs a paid Copilot plan

**Concepts:** [[GitHub Copilot]] · [[Coding agents]] · [[Multi-agent systems]]
**From:** [[2026-10-29]]

# My notes


---
# References
[GitHub changelog](https://github.blog/changelog/2026-10-28-copilot-code-review-merge-with-confidence-with-max-and-approvals)
