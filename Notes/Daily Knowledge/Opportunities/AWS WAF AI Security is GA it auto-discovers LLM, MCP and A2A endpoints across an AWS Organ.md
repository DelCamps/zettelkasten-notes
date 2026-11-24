---
date: 2026-11-24
section: AI
importance: Med
kind: value
source: "AWS What's New"
url: https://aws.amazon.com/about-aws/whats-new/2026/11/waf-ai-endpoint-discovery-protection/
status: unread
id: 2026-11-24-aws-waf-ai-endpoint-security
---
2026-11-24 07:16
Tags: #daily-knowledge #ai

---
# AWS WAF AI Security is GA it auto-discovers LLM, MCP and A2A endpoints across an AWS Organ

A new API Gateway API Portal finds LLM, MCP and A2A endpoints behind API Gateway, load balancers and CloudFront across an AWS Organization, flagging undocumented public MCP servers as shadow APIs. The AWS WAF AI Security managed rule group then blocks malformed MCP and A2A messages and, with content inspection on, calls Bedrock Guardrails to catch prompt injection, jailbreaks and sensitive data in responses.

## Details

**Availability and price**
Generally available. API Portal discovery in 32 AWS Regions; AI Security in US East (N. Virginia, Ohio), US West (Oregon), Europe (London), Europe (Stockholm), Asia Pacific (Tokyo, Sydney). Extra fees apply for AI Security, and Bedrock charges separately for content-inspection calls; the announcement lists no rates.

**Caveats**
- No Frankfurt, Ireland or Spain region for AI Security yet, so EU data-residency clients may need London or Stockholm
- Content inspection adds Bedrock Guardrails cost and latency per request
- Edge filtering does not stop indirect prompt injection that arrives through tools or documents the agent reads

**Client use cases**
- Find every MCP server and LLM endpoint teams have exposed across a client's AWS accounts (shadow AI inventory)
- Put a managed prompt-injection and data-leak screen in front of customer-facing chatbots and agents
- Evidence for AI governance and EU AI Act or DORA control mappings: an inventory plus enforced edge controls

**How we could offer it**
- AI attack-surface assessment: run discovery, review shadow MCP and A2A endpoints, prioritise fixes
- Implementation of WAF AI Security plus Guardrails policies, tuned against a red-team test set
- Managed AI-security monitoring; skills: AWS networking and WAF, Bedrock Guardrails, agent security

**Pitch**
AWS can now find every LLM, MCP and agent endpoint a client has exposed and put a managed prompt-injection filter in front of them. That gives us a quick, concrete AI-security assessment and remediation offer for AWS clients.

**What it is**
Two pieces announced as generally available on 23 November. Discovery: the API Portal builds an inventory of AI endpoints from traffic logs and service configuration, with no agents to deploy, and flags undocumented public-facing MCP servers as shadow APIs. Protection: the AI Security managed rule group checks MCP and A2A protocol compliance and can call the Bedrock Guardrails InvokeGuardrailsCheck API for prompt-injection, jailbreak, harmful-content and sensitive-information checks. It runs alongside other AWS Managed Rules or custom rules, with no custom rule writing required.

**Concepts:** [[AWS]] · [[Agent security]]
**From:** [[2026-11-24]]

# My notes


---
# References
[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/11/waf-ai-endpoint-discovery-protection/)
