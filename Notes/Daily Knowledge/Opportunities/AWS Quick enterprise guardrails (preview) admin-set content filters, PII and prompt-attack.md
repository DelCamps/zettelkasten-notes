---
date: 2026-11-21
section: AI
importance: Med
kind: value
source: "AWS What's New"
url: https://aws.amazon.com/about-aws/whats-new/2026/11/aws-quick-enterprise-guardrails-preview/
status: unread
id: 2026-11-21-aws-quick-enterprise-guardrails
---
2026-11-21 07:16
Tags: #daily-knowledge #ai

---
# AWS Quick enterprise guardrails (preview) admin-set content filters, PII and prompt-attack

AWS Quick added enterprise guardrails in preview. Admins can set content filters, denied topics, blocked words, prompt-attack detection and selected PII types on user prompts, per user, per IdP group or as the account default. A detect-only mode logs matches without blocking, and all events go to CloudWatch Logs.

## Details

**Availability and price**
Preview for select customers on Professional and Enterprise plans. Regional availability is listed in the AWS Quick Regions documentation. No pricing stated.

**Caveats**
Limited preview. It covers user prompts, so it is not a full agent-action control.

**Client use cases**
- Regulated clients rolling out Quick that need PII controls before wider launch
- Different policies for groups, e.g. stricter rules for contractors
- Run detect-only first to size policy impact, then enforce
- Feed blocked-prompt events from CloudWatch into the SOC

**How we could offer it**
- AI acceptable-use policy design translated into Quick guardrail settings
- Detect-only pilot and tuning report before enforcement
- Bundle with Quick rollout and data-source restriction controls

**Pitch**
Clients can roll Quick out widely with policy controls they can show to risk and compliance teams, starting in log-only mode.

**What it is**
Policy controls on prompts sent to AWS Quick, Amazon's AI assistant for work. User-level policies take precedence over group and default policies. Enforcement blocks a matching prompt and shows the user a message.

**Concepts:** [[AWS]] · [[Agent security]]
**From:** [[2026-11-21]]

# My notes


---
# References
[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-quick-enterprise-guardrails-preview/)
