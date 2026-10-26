---
date: 2026-10-26
section: AI
importance: Med
kind: paper
source: "arXiv 2610.31695"
url: https://arxiv.org/abs/2610.31695
status: unread
id: 2026-10-26-guard-rebinding
---
2026-10-26 07:16
Tags: #daily-knowledge #ai

---
# Safety guards can be tricked into grading a decoy instead of the harmful text

'Target rebinding' appends a forged query and a harmless decoy that imitate the guard's own prompt format, so the guard grades the decoy. It cleared all 75 held-out flagged AdvBench requests on Shieldstral-1.0-3B, and every one of five guards has an attack family that clears at least 93% of flagged items. A training fix cuts attack success from 75% to about 1%, but adaptive search still wins on 47 of 50 items. Tested on: 5 guard models from 5 developers; the confirmatory test used one guard and 75 requests.

## Details

**Problem**
Small guard models screen content before LLM apps and agents act on it, and most paste that content into a plain-text prompt with labels like <Query>: and <Document>:. Nothing stops the content from containing those labels itself.

**Method**
- The attack leaves the harmful request untouched and appends a forged task (query plus decoy document); the guard grades the last complete task it sees.
- Pre-registered test on Shieldstral-1.0-3B plus a GuardRebind benchmark across five guards (Shieldstral, gpt-oss-safeguard, ShieldGemma, Llama Guard 3, Qwen3Guard).
- Defense: fine-tune the guard so the content's score is no lower than its most harmful part; reserved boundary tokens tested too.

**Results**
- Forged query plus decoy clears all 75 held-out flagged AdvBench requests on Shieldstral; a plain 'ignore the text above' clears none.
- Each guard has an attack family that clears at least 93% of its flagged items.
- Training cuts attack success from 75% to 0.8-1.6% on held-out attacks, with clean AUROC down at most 0.01.
- A score-guided adaptive search still beats the trained guard on 47 of 50 items.

**Caveats**
Short English documents, one guard in the confirmatory study, not tested on retrieval, tool or multi-turn channels; the trained defense falls to adaptive attacks.

**For your work**
Do not rely on a guard model alone in front of agent actions: escape or wrap untrusted content so it cannot reproduce the guard's labels, and pair guards with permission checks on tools.

**Concepts:** [[Agent security]] · [[AI safety]]
**From:** [[2026-10-26]]

# My notes


---
# References
[arXiv 2610.31695](https://arxiv.org/abs/2610.31695)
