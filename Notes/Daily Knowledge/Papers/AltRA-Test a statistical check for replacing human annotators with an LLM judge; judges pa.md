---
date: 2026-11-21
section: AI
importance: Med
kind: paper
source: "arXiv 2611.26073"
url: https://arxiv.org/abs/2611.26073
status: unread
id: 2026-11-21-altra-test-llm-judge-replacement
---
2026-11-21 07:16
Tags: #daily-knowledge #ai

---
# AltRA-Test a statistical check for replacing human annotators with an LLM judge; judges pa

AltRA-Test asks whether swapping one human label for an LLM label keeps inter-annotator agreement statistically non-inferior, and it works even when different people labelled different items. Run on 18 LLM judges and 20 datasets, judges passed 35.3% of pairs with chain-of-thought and 47.3% with their best prompt. Gemini-3.1 Pro passed 16 of 20 datasets, and about 100 items were often enough. Tested on: 18 models (11 open-weight, 7 proprietary from Google and OpenAI), 5 prompting techniques, 20 datasets across text, image, audio and video, plus simulations.

## Details

**Caveats**
Only meaningful when humans agree at least fairly (IAA of 0.2 or more), and most preference datasets fall below that. The models tested are mostly small open models plus Gemini and GPT.

**For your work**
Before a client signs off an LLM judge in place of human reviewers, run a test like this on about 100 items that several humans labelled. It gives a defensible yes or no for each task.

**Method**
- Paired bootstrap: sample items and 3 human labels per item, swap one for the LLM label, and compare Krippendorff's alpha of the mixed panel with the all-human panel.
- A non-inferiority test with an adaptive margin (c=0.1, set in simulations where the true annotator noise is known).
- Run 18 judges and 5 prompting techniques on 300 items per dataset.

**Problem**
Teams increasingly use an LLM as judge in place of human raters, but existing replacement tests need the same annotators to label every item, which 11 of the 20 datasets here do not satisfy.

**Results**
- In simulations, it makes more correct replacement decisions than Alt-Test and STT.
- Pass rates depended on the dataset: all judges passed on CEBaB, none on Persuasion or Flickr8k-Expert. GPT-5.6-Luna passed 9/17 and the best open model, Gemma-3-12B, 8/17.
- On CIFAR-10H, 8 of the 9 LLM setups at least as accurate as humans passed, and none of the 36 less accurate ones did.

**Concepts:** [[Evals and benchmarks]]
**From:** [[2026-11-21]]

# My notes


---
# References
[arXiv 2611.26073](https://arxiv.org/abs/2611.26073)
