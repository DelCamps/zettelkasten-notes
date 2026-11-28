---
date: 2026-11-28
section: AI
importance: High
kind: value
source: "Claude blog"
url: https://claude.com/resources/articles/introducing-claude-ship
status: unread
id: 2026-11-28-claude-ship
---
2026-11-28 07:16
Tags: #daily-knowledge #ai

---
# Anthropic launches Claude Ship GA Code Review plus beta PR Steward and policy-based Claude

Claude Ship takes a pull request from review to fixes to an approval decision on Claude Team and Enterprise plans. Code Review is generally available with Quick, Standard or Deep levels per repository; PR Steward (fixes failing CI, merge conflicts and review feedback) and Claude Approvals (an approval policy written as a file, 'like a smarter CODEOWNERS file') are in beta. Eligible Enterprise organisations can claim at least $10,000 in credits until January 15, 2027.

## Details

**Availability and price**
Claude Team and Enterprise, GitHub repositories only. Code Review GA; PR Steward and Claude Approvals beta. Billed on tokens; admins can set spend limits for Code Review and PR Steward; Approvals has no base charge but its classifiers are billed on tokens. Not available with Zero Data Retention, the HIPAA configuration or customer-managed keys. No list prices or regional details given.

**Caveats**
Costs scale with PR volume, size and review level; a policy that uses Claude's review triggers a billed Code Review even in observe mode. Anthropic's 'more than doubled' merged-PR figure is from its own Claude Code team.

**Client use cases**
- Agentic review gate for client engineering teams already using Claude Code
- Policy-as-code approvals for regulated repos (who may approve what), run in observe mode first
- Reducing reviewer load on CI fixes and merge conflicts

**How we could offer it**
- Assessment and pilot: turn on Code Review in observe mode on 2-3 client repos and measure findings, reverts and token spend
- Governance: write the Claude Approvals policy file and spend limits with the client's platform team
- Managed service: tune review levels and per-repo budgets over time

**Pitch**
Claude Ship is Anthropic's answer to Copilot code review: we can pilot it alongside a client's existing GitHub flow, with a written approval policy and hard spend caps, and report review quality and cost after a month.

**What it is**
A set of PR tools for GitHub repositories: Code Review verifies findings against the codebase and posts them on the PR; PR Steward works on failing checks and review comments but 'is designed not to approve or merge pull requests'; Claude Approvals applies a team-written policy file, best started in observe-only mode. A /ship command in Claude Code pushes a change, opens the PR and has it reviewed and fixed.

**Concepts:** [[Claude]] · [[Coding agents]]
**From:** [[2026-11-28]]

# My notes


---
# References
[Claude blog](https://claude.com/resources/articles/introducing-claude-ship)
