---
date: 2026-11-23
section: AI
importance: High
kind: value
source: "GitHub changelog"
url: https://github.blog/changelog/2026-11-17-copilot-code-review-adaptive-effort-secret-detection-and-more
status: unread
id: 2026-11-23-copilot-code-review-azure-repos-ga
---
2026-11-23 07:16
Tags: #daily-knowledge #ai

---
# GitHub Copilot code review is GA for Azure Repos, billed to the Azure subscription; adapti

Copilot code review now works on Azure DevOps pull requests (GA), with branch policies for automatic reviews and usage billed in GitHub AI credits to the linked Azure subscription. On GitHub, Adaptive effort picks Lite, Balanced or Max review per PR, and secret detection matches 500+ known secret formats plus an AI detector (both public preview).

## Details

**Availability and price**
Azure Repos support: GA. Adaptive effort, cross-repo context and secret detection: public preview on Copilot Pro, Pro+, Max, Business and Enterprise. Azure Repos usage is billed in GitHub AI credits to the linked Azure subscription; no per-review price given. EU availability not stated.

**Caveats**
No credit rates or limits in the post. Cross-repository context only reads public repositories. Preview features may change.

**Client use cases**
- Clients standardised on Azure DevOps who want AI review without moving to GitHub
- Banks and insurers adding an automatic review gate on protected branches
- Catching leaked keys in PRs written by coding agents
- Gradual path to GitHub alongside Enterprise Live Migrations (GA on 19 Nov)

**How we could offer it**
- Pilot on a few Azure Repos with branch policies, measuring accepted suggestions and review time
- Governance pack: custom instructions and skills reflecting the client's coding standards, effort caps, audit log monitoring
- Combine with an Azure DevOps to GitHub migration roadmap

**Pitch**
Your teams keep Azure DevOps and get Copilot reviewing every pull request, billed on the Azure subscription you already have.

**What it is**
Copilot code review, until now GitHub-only, is generally available for Azure Repos. Admins set it up at organisation, project or repository level, use branch policies to trigger reviews automatically, choose Lite or Balanced default effort, add custom instructions and skills, let developers apply and commit suggestions, and get audit log events. In the same release, GitHub previews Adaptive effort (Copilot scores each PR's complexity and risk and picks Lite, Balanced or Max, never above the configured cap), cross-repository context for public repos, and secret detection in review comments (deterministic matching for 500+ formats from 150+ partners plus LLM-based detection).

**Concepts:** [[GitHub Copilot]] · [[Coding agents]]
**From:** [[2026-11-23]]

# My notes


---
# References
[GitHub changelog](https://github.blog/changelog/2026-11-17-copilot-code-review-adaptive-effort-secret-detection-and-more)
