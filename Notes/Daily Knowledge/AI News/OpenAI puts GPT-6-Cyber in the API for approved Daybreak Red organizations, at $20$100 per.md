---
date: 2026-11-07
section: AI
importance: Med
kind: news
source: "OpenAI API docs"
url: https://developers.openai.com/api/docs/models/gpt-6-cyber
status: unread
id: 2026-11-07-gpt-6-cyber-api
---
2026-11-07 07:16
Tags: #daily-knowledge #ai

---
# OpenAI puts GPT-6-Cyber in the API for approved Daybreak Red organizations, at $20$100 per

OpenAI has added gpt-6-cyber to its API, a model to investigate vulnerabilities, reproduce them in an authorized test environment and verify fixes. It has a 1,050,000-token context window and 128,000 max output, costs $20 input and $100 output per 1M tokens, and only works for organizations approved for Daybreak Red.

## Details

**Caveats**
No benchmarks on the model page; access is by application through an account team, not self-serve.

**For your work**
Relevant if PwC cyber teams want AI-assisted pentest or fix verification; the access controls (per-project enablement, IP allowlist, SSO) are a useful template for how to gate high-risk agent capabilities in client builds.

**Method**
- Access: organization approved for Daybreak Red, an owner enables it per non-default project, IP allowlist configured, SSO required and MFA enforced via the identity provider
- Requests set access_programs.cyber to daybreak_red plus a stable pseudonymous safety_identifier; Zero Data Retention projects need Private Safety Processing
- Wrong program values return 400 invalid_access_program; missing enablement returns 403 access_program_not_enabled

**Problem**
Security teams want a frontier model that will actually do exploit reproduction and validation, which general models often refuse.

**Results**
- Context 1,050,000 tokens (922,000 max input), 128,000 max output, text and image in
- Pricing per 1M tokens: $20 input, $2 cached input, $100 output
- Other API cyber safeguards still apply; Daybreak selection does not guarantee every request passes

**Concepts:** [[AI for security]] · [[Model releases and pricing]] · [[Frontier models]]
**From:** [[2026-11-07]]

# My notes


---
# References
[OpenAI API docs](https://developers.openai.com/api/docs/models/gpt-6-cyber)
