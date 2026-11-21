---
date: 2026-11-21
section: AI
importance: Med
kind: paper
source: "arXiv 2611.22033"
url: https://arxiv.org/abs/2611.22033
status: unread
id: 2026-11-21-shopping-agents-effort-confidence
---
2026-11-21 07:16
Tags: #daily-knowledge #ai

---
# Thinking harder buys confidence, not correctness higher reasoning effort rarely improved p

University of Chicago researchers gave ten frontier models 10-product choice tasks built from WebShop, Amazon SQID and Wayfair WANDS at low, medium and high effort. Of the low-to-high accuracy changes, only Qwen 3.8 Max on WebShop survived Holm correction, while stated confidence rose significantly for nine of ten models on WebShop. The two Claude models were the only well-calibrated ones, and models tended to fail on the same tasks, usually by picking the same wrong product. Tested on: 10 models from 6 providers, 3 datasets, 37,128 responses, a single run per condition, fixed choice lists (no search).

## Details

**Caveats**
Fixed choice lists, one confidence elicitation format, and roughly 15% of WebShop distractors are arguably acceptable. Effort may matter more when the agent also has to search.

**For your work**
For selection and recommendation steps, test low effort before paying for high. Don't gate actions on a model's self-reported confidence unless you have checked its calibration. Cross-model voting gives little protection when the models make the same mistakes.

**Method**
- Each task gives a query and ten shuffled candidates with exactly one correct product, which takes search and navigation out of the picture (496 WebShop, 500 SQID and 330 WANDS tasks).
- All models ran through OpenRouter at low, medium and high reasoning.effort with a shared budget of 16,000 tokens, answering in JSON with a 0-10 confidence score.
- Paired within-task t-tests with Holm correction, ECE, Brier score and AUROC, plus an independence baseline for shared errors.

**Problem**
Agent builders often turn up reasoning effort for important decisions and use the model's stated confidence to decide when to hand back to the user. Neither practice had been tested for everyday decisions like picking a product.

**Results**
- All 28 WebShop conditions landed between 74.0% and 88.1% success. Low-to-high gains were mostly within noise (for example, GPT-6 Astra gained +1.4 points and Claude Opus 5.5 +0.8).
- Calibration depended on the model: ECE was 3.4 for Claude Fable 5.1 and 6.7 for Claude Opus 5.5, against 8.9-18.2 for the other eight models on WebShop.
- At low effort, 47 of 493 WebShop tasks were failed by all ten models, where independence predicts 0.0001. The implied pairwise error correlation was 0.70-0.81.

**Concepts:** [[Agents]] · [[Evals and benchmarks]] · [[Frontier models]]
**From:** [[2026-11-21]]

# My notes


---
# References
[arXiv 2611.22033](https://arxiv.org/abs/2611.22033)
