---
date: 2026-11-16
section: AI
importance: Med
kind: paper
source: "arXiv 2611.17639"
url: https://arxiv.org/abs/2611.17639
status: unread
id: 2026-11-16-lookups-ambiguous-records
---
2026-11-16 07:16
Tags: #daily-knowledge #ai

---
# Agents act on the record they see a lookup that only counts a second match leads to wrong-

When a search shows one record and merely counts a second, most of 36 earlier agents act anyway, while listing both stops most; the newest Claude and GPT models always open the counted record and then never act. Adding a same-name, same-zip customer to tau-bench retail caused wrong-account writes in about a quarter of conversations, and a server-side street check kept completion near normal. Tested on: 36 earlier agents plus the newest Claude and GPT models on selected conditions, 16 templates and tau-bench retail.

## Details

**Caveats**
Role-only system prompt, so absolute rates depend on wording; retail domain only, one conversation per agent and task; the newest models ran only some cells.

**For your work**
Design lookup tools to list or check competing matches, verify identity server-side (e.g. a known street), and test agents with duplicate-name fixtures; don't rely on tool-description warnings.

**Method**
- Frame acts with presupposition theory: each claim must be seen, confirmed by the user, or disclosed while the act can be undone
- Vary whether a search lists, counts or omits a second match, and whether the user states a claim a record refutes
- Add a second customer with the requester's name and zip to tau-bench retail and test four lookup designs

**Problem**
Before an irreversible act, does an agent check the assumptions behind it, based on what its tools show or what the user claims?

**Results**
- A counted second record leaves most earlier agents acting; a listed one stops most
- A limit stated only in the tool description leaves the newest models acting 38 to 81% of the time; a note cuts it under 15%
- About two in five completions under the return-all lookup leak the other customer's data

**Concepts:** [[Agents]] · [[AI safety]] · [[Evals and benchmarks]]
**From:** [[2026-11-16]]

# My notes


---
# References
[arXiv 2611.17639](https://arxiv.org/abs/2611.17639)
