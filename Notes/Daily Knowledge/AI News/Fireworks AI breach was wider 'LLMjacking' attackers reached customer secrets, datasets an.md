---
date: 2026-11-11
section: AI
importance: Med
kind: news
source: "Fireworks security bulletin"
url: https://fireworks.ai/security/bulletins/october-2026-security-incident-update
status: unread
id: 2026-11-11-fireworks-breach-update
---
2026-11-11 07:16
Tags: #daily-knowledge #ai

---
# Fireworks AI breach was wider 'LLMjacking' attackers reached customer secrets, datasets an

Fireworks AI updated its October incident bulletin: after a third-party cloud provider hosting its R&D machines was breached on October 23, attackers ran an unauthorized workload on October 24 that hit billing data and, for some accounts, secrets, datasets and incomplete model weights. Fireworks ties it to a financially motivated group selling stolen LLM access and has disabled self-serve dataset uploads and downloads.

## Details

**Caveats**
No counts of affected accounts or data given; attacker group unnamed; investigation still active.

**For your work**
If any client project used Fireworks, check for a notice, replace revoked keys and rotate third-party secrets with their issuers (deleting a stored secret does not invalidate it). Good argument for short-lived credentials in eval jobs.

**Method**
- October 9 bulletin: internal credentials used to read environment variables (stored secrets) in evaluation jobs
- October 23: third-party cloud provider hosting R&D machines breached; October 24: attacker reached Fireworks development machines and ran an unauthorized workload
- Investigation with Palo Alto Networks Unit 42; law enforcement notified

**Problem**
Inference and fine-tuning platforms hold customers' API keys, datasets and weights, making them targets for 'LLMjacking', the resale of stolen model access.

**Results**
- Accessed: resource metadata, billing and shipping data, invoices and credit usage; for some accounts secrets, a subset of datasets and incomplete model weights
- Not impacted per Fireworks: Inference, Training SDK and Nexus (zero data retention by default); no card numbers stored
- Self-serve dataset uploads/downloads for Batch Inference and dataset-based training disabled during the investigation

**Concepts:** [[Agent security]] · [[AI for security]]
**From:** [[2026-11-11]]

# My notes


---
# References
[Fireworks security bulletin](https://fireworks.ai/security/bulletins/october-2026-security-incident-update)
