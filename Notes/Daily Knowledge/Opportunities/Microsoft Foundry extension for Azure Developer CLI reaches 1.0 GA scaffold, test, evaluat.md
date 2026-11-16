---
date: 2026-11-09
section: AI
importance: High
kind: value
source: "Microsoft Foundry blog"
url: https://devblogs.microsoft.com/foundry/microsoft-foundry-azure-developer-cli-ga/
status: unread
id: 2026-11-09-foundry-azd-extension-ga
---
2026-11-09 07:16
Tags: #daily-knowledge #ai

---
# Microsoft Foundry extension for Azure Developer CLI reaches 1.0 GA scaffold, test, evaluat

Microsoft's Foundry extension bundle for the Azure Developer CLI is now version 1.0 and generally available. It covers the whole hosted-agent lifecycle from the command line: scaffold, local test with Agent Inspector, remote-build deploy, monitoring, evaluations and GitHub Actions or Azure DevOps pipelines. A Foundry Skill also lets GitHub Copilot and Claude Code do the setup.

## Details

**Availability and price**
Generally available (version 1.0). Needs Azure Developer CLI 1.37.0 or later, an Azure subscription, Foundry permissions and model quota in the chosen region. The extension is free. Provisioned resources and model usage incur Azure charges, and no rates are given. The post does not list regions.

**Caveats**
This is developer tooling, not an end-user product. The sample needs Python 3.13 or later, and quota and deployment options vary by subscription and region. Related pieces, such as the Copilot harness in Foundry, are still in preview.

**Client use cases**
- A standard, repeatable path from prototype to production for client agents on Azure
- Agent configuration as code, reviewable in pull requests, for regulated clients
- Built-in evaluations as a release gate in CI/CD

**How we could offer it**
- Make azd plus Foundry our reference agent delivery template (repo, pipelines, eval gates)
- AgentOps accelerator: set up pipelines and eval rubrics for client agent teams
- Let our coding agents scaffold projects through the Foundry Skill

**Pitch**
Microsoft now ships a GA, supported way to go from agent prototype to CI/CD with evaluations on Azure. We can package it as our standard delivery template and shorten every Foundry engagement.

**What it is**
This is a GA command-line workflow for Foundry hosted agents. azd ai agent init scaffolds a sample agent and can reuse an existing model deployment. Agent and deployment settings live in azure.yaml, so they can be reviewed in pull requests, and you can eject editable Bicep or Terraform. azd ai agent run and invoke --local test the agent locally. azd deploy does a remote build, so no local container build is needed, and monitor, doctor and invoke cover operations. With the azure.ai.evaluations extension, azd ai eval generates datasets and rubrics and runs evaluations, and azd ai agent optimize is also available. azd pipeline config sets up CI/CD.

**Concepts:** [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-11-09]]

# My notes


---
# References
[Microsoft Foundry blog](https://devblogs.microsoft.com/foundry/microsoft-foundry-azure-developer-cli-ga/)
