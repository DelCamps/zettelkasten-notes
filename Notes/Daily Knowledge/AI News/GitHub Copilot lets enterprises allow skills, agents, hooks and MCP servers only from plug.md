---
date: 2026-11-17
section: AI
importance: Med
kind: news
source: "GitHub changelog"
url: https://github.blog/changelog/2026-11-16-control-where-github-copilot-customizations-come-from
status: unread
id: 2026-11-17-copilot-plugin-only-customizations
---
2026-11-17 07:16
Tags: #daily-knowledge #ai

---
# GitHub Copilot lets enterprises allow skills, agents, hooks and MCP servers only from plug

A new managed setting, strictPluginOnlyCustomization, blocks Copilot customizations from user and project files so they must come from plugins or managed settings. It can cover all categories or just some, and is meant to be paired with marketplace restrictions.

## Details

**Caveats**
Eligible plugins still pass, subject to other policies, so the control is only as good as the plugin sources you allow.

**For your work**
For clients rolling out Copilot agents, offer a governance step: package approved skills and MCP servers as plugins, turn on plugin-only mode, and restrict marketplaces with strictKnownMarketplaces.

**Method**
- strictPluginOnlyCustomization can cover all five categories or individual ones: skills, custom agents, hooks, MCP servers and executable Copilot extensions (canvas providers)
- 'Plugin-only' is not a marketplace allowlist: pair it with strictKnownMarketplaces to restrict sources

**Problem**
Skills, custom agents, hooks and MCP servers dropped into a repo or user folder are an uncontrolled path for code and instructions into Copilot agents.

**Results**
- Available on GitHub Enterprise Cloud for Copilot Business or Enterprise licences issued by the enterprise
- Closes the path where a repo or user folder silently adds agents, hooks or MCP servers

**Concepts:** [[GitHub Copilot]] · [[Agent security]]
**From:** [[2026-11-17]]

# My notes


---
# References
[GitHub changelog](https://github.blog/changelog/2026-11-16-control-where-github-copilot-customizations-come-from)
