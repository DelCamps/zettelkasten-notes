---
date: 2026-11-03
section: AI
importance: Med
kind: paper
source: "arXiv 2611.00884"
url: https://arxiv.org/abs/2611.00884
status: unread
id: 2026-11-03-silent-fetch-failures
---
2026-11-03 07:16
Tags: #daily-knowledge #ai

---
# When 200 OK is not an answer 20.9% of pages a static fetch gets with status 200 lack the a

Fetching 10,307 URLs, the study finds 20.9% of static HTTP 200 responses are app shells, bot challenges, block pages, error or placeholder pages, or partial content, and 13.1% of probed sites return 200 for random non-existent paths. Treating 200 as content inflates the apparent silent citation-drift rate from 5.8% to 21.9%; cheap heuristics recover 86% of unusable responses at a false-alarm rate near 5%. Tested on: 10,307 fetches across 1,507 sites in five strata plus 4,795 ExpertQA citation URLs; 300 reviewed labels.

## Details

**Caveats**
Single author; three-day crawl with a polite client that never bypassed challenges; review labels partly LLM-assisted with a 60-item human check.

**For your work**
In RAG and research agents, have the fetch tool report whether real content arrived (length check, random-path probe, redirect-to-root) instead of trusting the status line, and log fetch outcomes in evals.

**Method**
- Static and rendered-browser fetches of llms.txt-linked pages, three Tranco rank bands, Markdown-serving sites, random-path probes and ExpertQA citations.
- Seven-type taxonomy for 200 responses (content, block, challenge, shell, error or substitute, parked, consent wall), labelled automatically and checked against 300 reviewed items.
- Compares status code, five crawler heuristics, a zero-shot LLM, a text classifier and a fine-tuned small model on site-disjoint splits.

**Problem**
Web agents, answer engines and citation checkers treat an HTTP 200 as a successful read. Soft 404s, bot walls and JavaScript shells mean the agent may not have read the page at all.

**Results**
- Reviewed sample lowers the test-split unusable estimate from 25.5% to 20.0%.
- For cited sources, treating 200 as content overstates checkable claim-source pairs by 12.2 points.
- Combined text length, probe comparison and redirect-to-root heuristics catch 86%; the best content reader adds five to seven points of recall at more than twice the false alarms.

**Concepts:** [[RAG]] · [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-11-03]]

# My notes


---
# References
[arXiv 2611.00884](https://arxiv.org/abs/2611.00884)
