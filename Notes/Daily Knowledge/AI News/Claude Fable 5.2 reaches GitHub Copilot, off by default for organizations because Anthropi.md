---
date: 2026-11-10
section: AI
importance: High
kind: news
source: "GitHub changelog"
url: https://github.blog/changelog/2026-11-09-claude-fable-5-2-in-github-copilot
status: unread
id: 2026-11-10-copilot-claude-fable-5-2
---
2026-11-10 07:16
Tags: #daily-knowledge #ai

---
# Claude Fable 5.2 reaches GitHub Copilot, off by default for organizations because Anthropi

Claude Fable 5.2 is now generally available in the GitHub Copilot model picker on Pro+, Max, Business and Enterprise, in VS Code, Visual Studio, JetBrains, Xcode, Eclipse, Copilot CLI, the coding agent and github.com. Business and Enterprise admins must turn on a policy that accepts data retention. Eligible enterprises can keep zero data retention until the end of the year.

## Details

**Caveats**
Eligibility for the exemption goes through the GitHub account team, not GitHub Support, and an admin still has to turn the policy on. The changelog gives no default model change and no benchmark numbers.

**For your work**
For client repositories, check with the PwC GitHub admins whether the policy is on and whether the ZDR exemption applies before choosing Fable 5.2. Plan for the year-end change to Enterprise Frontier Safeguards.

**Method**
- Rollout is gradual across VS Code, Visual Studio, Copilot CLI, the coding agent, the Copilot app, github.com, GitHub Mobile, JetBrains, Xcode and Eclipse.
- Billing is at provider list price under usage-based billing. The changelog gives no premium request multiplier.
- For Business and Enterprise, the Claude Fable 5.2 policy is off by default, and turning it on accepts data retention. GitHub says the retained data is not used to train Anthropic's models.

**Problem**
Fable models need Anthropic to keep prompts and outputs so it can run its safety classifiers. That conflicts with the zero data retention (ZDR) Copilot gives other Claude models.

**Results**
- In GitHub's early testing, Fable 5.2 solved more tasks than Fable 5.1 with fewer steps and tool calls.
- Under a time-bound exemption, eligible enterprises can use Fable 5, 5.1 and 5.2 with ZDR until the end of the calendar year. After that, they need Anthropic's Enterprise Frontier Safeguards.
- All other Claude models in Copilot stay under ZDR.

**Concepts:** [[GitHub Copilot]] · [[Claude]] · [[Model releases and pricing]]
**From:** [[2026-11-10]]

# My notes


---
# References
[GitHub changelog](https://github.blog/changelog/2026-11-09-claude-fable-5-2-in-github-copilot)
