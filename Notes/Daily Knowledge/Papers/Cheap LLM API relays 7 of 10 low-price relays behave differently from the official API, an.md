---
date: 2026-11-06
section: AI
importance: Low
kind: paper
source: "arXiv 2611.07650"
url: https://arxiv.org/abs/2611.07650
status: unread
id: 2026-11-06-llm-api-relays
---
2026-11-06 07:16
Tags: #daily-knowledge #ai

---
# Cheap LLM API relays 7 of 10 low-price relays behave differently from the official API, an

Queen's University tested 20 third-party relays selling GPT-6 Astra and Claude Opus 5. They flagged 7/10 low-price and 2/10 same-or-higher-price relays for answers that differ from the official API. Four relays returned tool calls the user had disabled, and five reported 4,200 to 60,000 more input tokens than the official API for identical requests; at one service those tokens were billed. Tested on: 20 relays, two models, two rounds 11–18 days apart.

## Details

**Caveats**
Relays were not chosen at random, and the price-group difference is not significant at 0.05. The tests show what the client receives but cannot identify which model actually answered.

**For your work**
If a client or team routes traffic through a reseller or gateway, run repeated spot checks against the official API (answers, tool permissions, token counts) before trusting it with production or confidential data.

**Method**
- Knowledge-boundary questions chosen to separate the target models from likely substitutes, compared with official responses from the same batch
- Screen returned content for injections and check tool-call compliance when tools are disabled
- Compare reported input tokens with official counts, and check account balance changes; retest 35 of 36 relay-model pairs 11–18 days later

**Problem**
Relays resell access to frontier models, often cheaply, and can read and change plaintext traffic. Users cannot tell from an answer or an invoice whether the relay serves the advertised model, respects tool permissions or bills honestly.

**Results**
- Behavioural flags: 7/10 low-price vs 2/10 same- or higher-price relays (p = 0.07); 7/35 pairs gain or lose a flag between rounds
- No injection confirmed in 3,332 screened responses, but four relays returned tool calls despite restrictions (not executed)
- Five relays report 4,200 to 60,000 extra input tokens; R10's Opus surplus of about 59,500 tokens fits a coding-client wrapper
- At the six services with balances, charges match reported usage at listed prices to the cent

**Concepts:** [[Agent security]] · [[Model releases and pricing]]
**From:** [[2026-11-06]]

# My notes


---
# References
[arXiv 2611.07650](https://arxiv.org/abs/2611.07650)
