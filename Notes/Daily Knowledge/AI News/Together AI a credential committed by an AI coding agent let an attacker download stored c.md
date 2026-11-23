---
date: 2026-11-23
section: AI
importance: Med
kind: news
source: "Together AI blog"
url: https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026
status: unread
id: 2026-11-23-together-ai-prompt-leak
---
2026-11-23 07:16
Tags: #daily-knowledge #ai #update

---
# Together AI a credential committed by an AI coding agent let an attacker download stored c

Together AI says an AI coding agent committed a credential to its public GitHub repository xorl. The credential opened a private Hugging Face repository of stored serverless prompt samples from June and July 2026, and an unauthorized party downloaded them, searched them for secrets and tested them. Five of the tested credentials were Dragos canaries. Zero data retention is now the default for new accounts.

## Details

**Caveats**
Self-reported by the vendor; scope and detection date are not given. An external forensic firm and law enforcement are involved.

**For your work**
Clients who send prompts to third-party inference hosts should require zero data retention in writing, and keep secrets out of prompts. In our own repos, coding agents need secret scanning before commit, not only after push.

**Method**
- While building the public repo xorl, an AI coding agent committed a credential that gave access to a private Hugging Face repo of prompt samples
- Automated scanning caught it and the commit was reverted, but during the exposure window the attacker downloaded samples from requests to MiniMax M3, GLM-5.2 and Kimi K2.6, mainly from 24 June, 4, 8 and 14 July 2026
- The attacker searched the prompts for credentials to other services and tested whether they worked; five were Dragos canary credentials

**Problem**
Inference providers keep samples of customer prompts for testing, and coding agents can leak the secrets that guard them. This is the provider-side story behind the Dragos canary study that led OpenRouter to drop three providers.

**Results**
- Together found no evidence of prompt leakage beyond this incident and is still checking whether the samples hold personal or other customer data
- Fixes: scoped or short-lived credentials and keyless access, credential checks on every pull request, ZDR default for new accounts, updated processes for AI coding agents
- No count of affected customers or samples, and no exposure-window dates

**Concepts:** [[Agent security]] · [[Coding agents]]
**From:** [[2026-11-23]]

# My notes


---
# References
[Together AI blog](https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026)
