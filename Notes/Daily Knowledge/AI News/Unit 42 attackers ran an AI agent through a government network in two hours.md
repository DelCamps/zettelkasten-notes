---
date: 2026-10-25
section: AI
importance: High
kind: news
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

## Details

**Caveats**
A single vendor's incident report; the agent platform is not named and attribution details are limited.

**For your work**
Patch PHP front-ends now. For detection, look for delimiter-wrapped command batches and machine-speed pivots; and design your own agents' shell tools so they cannot be repurposed this way (allow-lists, no credential access, audit logs).

**Method**
- CVE-2026-109618: out-of-memory handling via longjmp() leaves request memory uninitialised, giving reliable RCE using OOM triggers.
- CVE-2026-109619: longjmp() fatal-error handling leaves global pointers to freed memory that later requests read or branch on.
- Post-exploitation at a European government body: endpoint enumeration, password hashes and MFA secrets within two hours, an NTLM-relay tunnel into Active Directory and a Domain Admin escalation attempt.
- Agentic tell-tales: command batches wrapped in section delimiters such as ==SHELLUSER== and ==PASSWD== for machine-parseable output, short serially spaced tasks and quick pivots after failures.

**Problem**
Two critical PHP remote-code-execution flaws (PHP2Shell, CVSS 4.0 score 9.2) were disclosed this week, with Cortex Xpanse counting over 22.6 million potentially exposed instances. Unit 42 then saw attackers hand post-exploitation to an agentic AI platform.

**Results**
- Full compromise path in about two hours from initial exploitation.
- At least one European government took its website offline as a precaution.
- Unit 42 publishes XQL hunting queries for Cortex XDR.

**Concepts:** [[AI for security]] · [[Red teaming]] · [[Agent guardrails]]
**From:** [[2026-10-25]]

# My notes


---
# References
[Palo Alto Unit 42](https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/)
