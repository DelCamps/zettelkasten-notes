---
date: 2026-11-24
section: AI
importance: Med
kind: news
source: "Claude Code changelog"
url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
status: unread
id: 2026-11-24-claude-code-2-1-331
---
2026-11-24 07:16
Tags: #daily-knowledge #ai #update

---
# Claude Code 2.1.331 brings Code Mode to Bedrock, Google Cloud, Foundry and Claude Platform

Claude Code 2.1.331 (23 November) adds Code Mode in terminal sessions on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry and Claude Platform on AWS, and gen_ai usage and model fields to its llm_request trace spans. It also adds optional plugin dependencies, a claude doctor API connectivity check, and fixes MCP calls hanging up to 30 minutes and /compact losing parts of summaries.

## Details

**Caveats**
- Still on the 'next' channel; the stable tag is 2.1.325
- The 30 November marketplace auto-update change needs an opt-out ('autoUpdate': false) if a client wants to pin plugins

**For your work**
For clients on Foundry or Bedrock, Code Mode is now available to them. Wire the new gen_ai span fields into their OpenTelemetry dashboards for cost per team, and check managed marketplace settings before 30 November.

**Method**
- Code Mode in terminal sessions on Bedrock, Google Cloud's Agent Platform, Microsoft Foundry and Claude Platform on AWS
- gen_ai.usage.*, gen_ai.response.model and gen_ai.operation.name on claude_code.llm_request spans; input tokens include prompt-cache tokens
- Claude apps gateway: oidc.groups_jsonpath to read groups from IdP claims, and an IdP-by-hostname option behind proxies
- Plugins can declare optionalDependencies; claude doctor reports API reachability

**Problem**
Enterprise teams that run Claude Code through their own cloud (Bedrock, Foundry, Google Cloud) lagged behind direct-API users on features, and observability of token usage per request was limited.

**Results**
- Fixes MCP tool calls hanging for up to 30 minutes on malformed replies
- Fixes /compact sometimes losing part of the summary when it quoted certain XML tags
- Announces that managed plugin marketplaces will auto-update by default on or after 30 November 2026

**Concepts:** [[Claude]] · [[Coding agents]]
**From:** [[2026-11-24]]

# My notes


---
# References
[Claude Code changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
