---
date: 2026-11-09
section: AI
importance: High
kind: paper
source: "arXiv 2611.08834"
url: https://arxiv.org/abs/2611.08834
status: unread
id: 2026-11-09-contract-injection-guards
---
2026-11-09 07:16
Tags: #daily-knowledge #ai

---
# Prompt-injection guards fail on legal contracts up to 92% false positives, and none beats

Eleven off-the-shelf prompt-injection guards were run on legal contracts with planted review instructions. Some flagged up to 92.39% of clean contracts, two did worse than chance, and none Pareto-dominated a five-regex baseline. Prompted Claude models reached 0.97-1.00 paired AUC, and a cascade that sends Haiku 4.5's positives to Opus 4.8 matched Opus's precision at 6.5x lower cost. Tested on: 11 guards plus 2 Claude LLM detectors, 683 proprietary and 510 CUAD contracts, 14 payload templates on 60 hosts per corpus, and 504 factorial probe sentences.

## Details

**Caveats**
The authors are from Ivo AI, a legal AI vendor. The study covers English, US commercial contracts and one review question per contract, does not measure latency, and the only LLM detectors tested are Claude models.

**For your work**
For document-review clients (legal, audit), do not rely on an off-the-shelf encoder guard. Use a cheap LLM screen with frontier-model escalation, and test it on the client's real documents for false positives.

**Method**
- Taxonomy of contract-borne review instructions, plus 'scope claims' (asserted authority)
- Every injected contract is paired with its unmodified host, which separates attack detection from noticing that the document was edited
- 504 factorial sentences vary intent, addressee, 'must/shall' and preamble to find what guards actually react to
- Prompted Claude Haiku 4.5 and Opus 4.8, alone and as a cascade

**Problem**
Contract review tools read text written by a counterparty who may want to steer the AI reviewer. No false-positive rate had been published for any prompt guard on contracts.

**Results**
- Document false-positive rates of 78-92% for TestSavant, deepset and DistilBERT; ProtectAI v2 flags 60.61% of clean contracts, against 0.59% for v1
- Guards respond to how an instruction is worded, not to what it asks for; 7 of 11 score AI-addressed instructions lower
- Every guard scores zero on scope claims; LLMs detect them
- Cascade: false positives 0.00%, benign-control flags from 80% to 0%, 0.02 cents per document over Haiku alone

**Concepts:** [[Agent security]] · [[Claude]] · [[Evals and benchmarks]]
**From:** [[2026-11-09]]

# My notes


---
# References
[arXiv 2611.08834](https://arxiv.org/abs/2611.08834)
