---
date: 2026-11-19
section: AI
importance: Med
kind: news
source: "Epoch AI"
url: https://epoch.ai/publications/how-good-are-fable-5-2-and-gpt-6-2-astra-at-real-work
status: unread
id: 2026-11-19-epoch-real-work-fable-astra
---
2026-11-19 07:16
Tags: #daily-knowledge #ai

---
# Epoch no model meets its employee standard on real work tasks; GPT-6.2 Astra averages 65%,

Epoch manually graded Fable 5.2, GPT-6.2 Astra and four other models on tasks taken from its own work. Fable 5.2 (97.5%) and Opus 5.5 (87.5%) reached contractor level on AI data center analysis, and Opus 5.5 took just under 3 hours against a contractor's 16. All models reused existing ideas in experiment design and barely iterated, and almost all preferred their own outputs over human gold standards.

## Details

**Caveats**
Small task suite with one run per model per task; Epoch says the results are not a general measure. The setup changed since its last report, so scores are not directly comparable.

**For your work**
This is useful evidence for clients that leaderboard ties hide large gaps on real tasks, and for running small, hand-graded evaluations on their own tasks. The self-preference result argues against using a model to judge its own work against human references.

**Method**
- Updated Epoch Automation Reports: tasks derived directly from Epoch's work (data center analysis, a chess-variants generalisation study, a hidden-messages-in-SVG study, an open-ended Data Insight)
- Outputs graded by hand against internal standards, where 100% is what Epoch expects of an employee
- Fable 5.2, GPT-6.2 Astra and four other models, one run each per task; models were also asked to compare their output with a human gold standard

**Problem**
Fable 5.2 and GPT-6.2 Astra roughly tie for a record on the Epoch Capabilities Index, but do benchmark scores translate into real workplace tasks?

**Results**
- No model met the employee standard on any task; GPT-6.2 Astra averaged 65%, 17 points below Fable 5.2
- Data center analysis: Fable 5.2 97.5%, Opus 5.5 87.5%, GPT-6.2 Astra 65%; Astra left out estimates because it was too cautious
- Every model used existing chess variants instead of truly novel ones; Fable 5.2's 'Kingsgate' plays exactly like an existing variant
- All models preferred their own output in every case except one (Gemini 4 Argon on hidden messages), rewarding superficial rigor such as the number of experiments run

**Concepts:** [[Evals and benchmarks]] · [[Frontier models]] · [[Agents]]
**From:** [[2026-11-19]]

# My notes


---
# References
[Epoch AI](https://epoch.ai/publications/how-good-are-fable-5-2-and-gpt-6-2-astra-at-real-work)
