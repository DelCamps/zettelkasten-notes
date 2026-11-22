---
date: 2026-11-22
section: AI
importance: Low
kind: paper
source: "OpenAI research"
url: https://openai.com/index/introducing-medchembench/
status: unread
id: 2026-11-22-medchembench
---
2026-11-22 07:16
Tags: #daily-knowledge #ai

---
# OpenAI's MedChemBench (OpenAI models only) GPT-6.2 Astra earns 84.5% of the credit on 99 m

OpenAI built 99 problems from 117 published papers and patents, covering 761 molecular structures, that test whether a model can reconstruct structures, explain results, rank compounds and predict properties from the evidence available at a point in a drug programme. GPT-6.2 Astra at xhigh effort scores 84.5%, GPT-6 Astra 83.3%, GPT-6.1 Sol 82.0% and GPT-5.6 Sol 58.2%. Compound selection and numeric property prediction are still weak. Tested on: OpenAI GPT models only, single attempt, no tools, no human baseline.

## Details

**Caveats**
Only OpenAI models are tested and there is no human expert baseline. OpenAI says the results do not show that models can discover drugs or improve lab decisions, and that the models may have seen the published sources in training.

**For your work**
Relevant mainly for pharma clients. It is a vendor-built benchmark of the vendor's own models, so it cannot support a claim that one vendor beats another; run Claude or Gemini on it before using it in a model choice.

**Method**
- 99 problems from 117 papers and patents, with 761 distinct structures, each giving the context available at a chosen point in a research programme.
- Four graded parts: structure reconstruction, scientific reasoning, ranking and selection, property prediction, with partial credit for close numeric predictions.
- One attempt per response, with no tools, feedback or new experiments.

**Problem**
Drug-discovery teams want to know whether LLMs can reason about structure-activity trade-offs, such as potency versus metabolic stability, rather than only recall chemistry facts.

**Results**
- GPT-6.2 Astra (xhigh) 84.5%; GPT-6 Astra (xhigh) 83.3%; GPT-6.1 Sol (xhigh) 82.0%; GPT-6.1 Terra 75.1%; GPT-5.6 Sol 58.2%.
- GPT-6 Astra reaches 95.4% on structure reconstruction but earns only about half the credit on compound selection and numeric property prediction.
- Higher reasoning effort generally raised scores.

**Concepts:** [[AI for science and math]] · [[Evals and benchmarks]]
**From:** [[2026-11-22]]

# My notes


---
# References
[OpenAI research](https://openai.com/index/introducing-medchembench/)
