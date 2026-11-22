---
date: 2026-11-22
section: AI
importance: High
kind: news
source: "OpenRouter blog"
url: https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/
status: unread
id: 2026-11-22-openrouter-dragos-canaries
---
2026-11-22 07:16
Tags: #daily-knowledge #ai

---
# OpenRouter drops three inference providers and removes 125 endpoints from Zero Data Retent

OpenRouter said today it had removed three providers, taken 125 endpoints off Zero Data Retention (ZDR) eligibility and notified affected customers, after Dragos research it says showed no breach of OpenRouter itself. Dragos (HD Moore) sent nearly two million prompts carrying unique bait secrets from July through November and found attackers inside at least three hosting providers, marketplace resellers reading prompts, and ZDR flags ignored. In one case a Chinese AI lab fetched the secret links from more than half of the prompts sent to its models, including roughly two-thirds of those marked no data collection or ZDR.

## Details

**Caveats**
Dragos and OpenRouter do not name the three breached or removed providers, and not all affected providers have posted publicly. Dragos's own report dates from 19 November; the new development is OpenRouter's response.

**For your work**
Check every client deployment that uses a router or an open-weight model host. A privacy flag only binds the first hop, so contract with first-tier providers or pin upstreams, keep secrets out of agent context, and seed your own canary credentials as Dragos recommends.

**Method**
- Dragos seeded each prompt with unique AWS keys, URLs, SSH and git credentials pointing to monitored canary services.
- It traced routes by having every system that fetched an embedded image reveal itself and by reading the nested error formats; about two thousand routes were traced.
- OpenRouter is adapting the same tests to run on an ongoing basis and checking network paths for undisclosed forwarding.

**Problem**
LLM routers and marketplaces forward prompts through several companies. Clients set ZDR or no-training flags and assume every hop honours them.

**Results**
- Attackers copied requests at three providers; bait AWS keys were used for tens of thousands of AWS API calls, and some stolen requests were marked ZDR.
- One marketplace seller silently adds about a thousand hidden tokens to every prompt; resellers simply turned on logging.
- A secret link appeared in a Feishu chat in China twenty-four days after it was sent to a US provider with the ZDR flag.
- OpenRouter: three providers off-boarded, 125 endpoints removed from ZDR, customers notified. Novita, Phala and Together have published notices.

**Concepts:** [[Agent security]] · [[AI for security]]
**From:** [[2026-11-22]]

# My notes


---
# References
[OpenRouter blog](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/)
