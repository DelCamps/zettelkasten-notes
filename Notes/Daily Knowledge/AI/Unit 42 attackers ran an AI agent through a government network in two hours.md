---
date: 2026-10-25
section: AI
importance: High
source: "Palo Alto Unit 42"
url: https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/
status: unread
id: 2026-10-25-unit42-agentic-attackers
---
2026-10-25 07:16
Tags: #daily-knowledge #ai

---
# Unit 42 attackers ran an AI agent through a government network in two hours

After exploiting the two critical PHP flaws (CVE-2026-109618/109619), attackers used an agentic AI platform for post-exploitation at a European government body: password hashes and MFA secrets within two hours, an NTLM-relay tunnel into Active Directory and a Domain Admin attempt. Tell-tales were command batches wrapped in LLM-parseable delimiters (==SHELLUSER==, ==PASSWD==), short serial tasks and fast pivots after failures, useful signatures for anyone building detection or agent guardrails.

**Concepts:** [[AI for security]] · [[Red teaming]] · [[Agent guardrails]]
**From:** [[2026-10-25]]

# My notes


---
# References
[Palo Alto Unit 42](https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/)
