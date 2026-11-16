---
date: 2026-11-12
section: AI
importance: High
kind: news
source: "Railway blog"
url: https://blog.railway.com/p/incident-report-october-security-incident
status: unread
id: 2026-11-12-railway-breach-ai-agents
---
2026-11-12 07:16
Tags: #daily-knowledge #ai

---
# Railway incident report attackers with abliterated models and an agent harness broke out o

Railway's updated incident report (10 November, 18:02 UTC) says the attacker used abliterated models with no safeguards and agent fanouts to find exploits, escaping build isolation and decrypting customer variables in up to 1.85% (about 100,000) of workspaces. Unauthorized spend on stolen AI keys is estimated to reach about $740,000.

## Details

**Caveats**
Railway's own account; the exposure figure is a maximum, not a confirmed count. The attack chain itself happened in October; the new part is the forensic update.

**For your work**
Treat LLM API keys in deployment env vars as high-value targets: use short-lived or scoped keys, spend caps and anomaly alerts per key, and assume attackers now run agentic exploit search against leaked source.

**Method**
- From 20 October the attacker exploited an unknown flaw in Railway's build infrastructure to escape filesystem isolation and get an internal credential
- They copied Railway's monorepo from build histories (353 builds read) and used agent fanouts to search it for further weaknesses
- A misconfigured trust relationship then gave access to keys that decrypt customer environment variables

**Problem**
A cloud host's customer secrets, including AI provider API keys, were stolen and immediately monetised, in what Railway calls 'a contest of agent speed' between its engineers and an AI-assisted attacker.

**Results**
- Up to 1.85% (about 100,000) workspaces may have had variables decrypted (an upper bound)
- 1,852 users had linked-account tokens (incl. GitHub OAuth and AI agent keys) reset
- Stolen keys were used for about $740,000 of AI usage, from coding agents to training pipelines; Railway covers Anthropic and OpenRouter costs itself
- The attacker was evicted on 21 October, about 26 hours after the first page

**Concepts:** [[Agent security]] · [[AI for security]]
**From:** [[2026-11-12]]

# My notes


---
# References
[Railway blog](https://blog.railway.com/p/incident-report-october-security-incident)
