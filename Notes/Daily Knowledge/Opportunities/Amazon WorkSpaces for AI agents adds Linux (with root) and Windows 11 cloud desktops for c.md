---
date: 2026-11-05
section: AI
importance: Med
kind: value
source: "AWS What's New"
url: https://aws.amazon.com/about-aws/whats-new/2026/11/workspaces-ai-agents-linux-windows-11
status: unread
id: 2026-11-05-aws-workspaces-agents-linux-win11
---
2026-11-05 07:16
Tags: #daily-knowledge #ai

---
# Amazon WorkSpaces for AI agents adds Linux (with root) and Windows 11 cloud desktops for c

AWS's managed cloud desktops for AI agents now run Linux and Windows 11 as well as Windows Server. Linux desktops give agents full root access for builds, tests and scripts; Windows 11 lets them operate the enterprise desktop apps that staff already use.

## Details

**Availability and price**
Announced 3 Nov 2026. The announcement gives no prices, regions or EU availability; setup is in the WorkSpaces agent-access developer guide.

**Caveats**
Computer-use agents are still error-prone on long tasks. Root access on Linux raises the stakes of prompt injection, so keep network isolation tight.

**Client use cases**
- Automate legacy Windows desktop apps with no API (ERP clients, claims tools) using an agent instead of RPA
- Let coding or test agents run builds and test suites on an isolated Linux box
- Pilot computer-use agents in regulated clients inside their own AWS account and IAM controls

**How we could offer it**
- Computer-use automation PoC: pick 2-3 desktop processes, run an agent on WorkSpaces, measure success rate and cost
- Governance pack: IAM per agent, network isolation, CloudTrail audit and human review points

**Pitch**
Give the agent its own locked-down PC in your AWS account, not your employee's laptop.

**What it is**
Amazon WorkSpaces for AI agents gives a computer-use agent its own cloud desktop to screenshot, click and type in. This update adds Linux desktops, where the agent has full root access for developer tasks such as running builds, tests and scripts, and Windows 11 desktops for agents that work in a team's enterprise applications. Security controls are the same as on Windows Server: network isolation, IAM-based access and existing compliance boundaries.

**Concepts:** [[Computer-use agents]] · [[AWS]]
**From:** [[2026-11-05]]

# My notes


---
# References
[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/11/workspaces-ai-agents-linux-windows-11)
