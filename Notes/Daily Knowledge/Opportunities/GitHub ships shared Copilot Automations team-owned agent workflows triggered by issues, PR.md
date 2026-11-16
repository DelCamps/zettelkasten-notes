---
date: 2026-11-01
section: AI
importance: High
kind: value
source: "GitHub changelog"
url: https://github.blog/changelog/2026-10-28-build-shared-workflows-for-your-team-with-copilot-automations
status: unread
id: 2026-11-01-copilot-automations
---
2026-11-01 07:16
Tags: #daily-knowledge #ai

---
# GitHub ships shared Copilot Automations team-owned agent workflows triggered by issues, PR

Copilot Automations, which combine a prompt, a trigger and an allow-listed set of tools that Copilot runs in the cloud, can now be shared by a whole repository instead of belonging to one person. Shared automations act as Copilot, bill AI credits to the repository owner and keep running if their creator leaves. Rolling out on Pro, Pro+, Max, Business and Enterprise.

## Details

**Availability and price**
Rolling out (GitHub does not label it GA or preview) to Copilot Pro, Pro+, Max, Business and Enterprise; availability may vary during the rollout. AI credits are billed to the repository owner. For org repos an admin must enable the 'Allow use of Copilot cloud agent billed to the organization' policy. No separate price is given.

**Caveats**
The type (personal or shared) cannot be changed after creation. Anyone with write access can edit a shared automation, so prompt and tool changes need review. Credit consumption is not quantified in the post. Competes with Claude Code scheduled tasks and GitHub Agentic Workflows (already GA).

**Client use cases**
- Reproduce a bug automatically as soon as an issue is opened, and attach the findings to the issue.
- Capture screenshots of UI changes when a pull request is marked ready for review.
- Start an incident investigation as soon as the monitoring tool raises an alert, before the on-call engineer logs in.
- Standard team chores (release notes, dependency triage) that should survive staff turnover.

**How we could offer it**
- Assessment: map a client's repetitive engineering workflows and pick 3-5 that suit an event-triggered agent.
- Pilot and implementation: build the automations with tight tool allow-lists, and wire triggers to the client's issue tracker and monitoring.
- Governance as a managed service: policy setup, AI-credit budgets per org, review of change history. Skills needed: GitHub admin, Copilot policies, prompt and tool design.

**Pitch**
GitHub just made Copilot agent workflows a team asset: they run on issues, PRs or alerts, bill to the org and survive people leaving. We could package 'Copilot Automations in 30 days' for clients who already pay for Copilot Business or Enterprise.

**What it is**
Until now Copilot Automations were personal: only the creator could see or edit them, and they ran with that person's identity and AI credits. Shared automations belong to the repository. Anyone with read access sees them, anyone with write access edits them, actions are attributed to Copilot, and there is a change history of the prompt, triggers and tools. You create them on github.com, in the GitHub Copilot app or in VS Code by choosing 'Shared' as the type.

**Concepts:** [[GitHub Copilot]] · [[Coding agents]] · [[Agents]]
**From:** [[2026-11-01]]

# My notes


---
# References
[GitHub changelog](https://github.blog/changelog/2026-10-28-build-shared-workflows-for-your-team-with-copilot-automations)
