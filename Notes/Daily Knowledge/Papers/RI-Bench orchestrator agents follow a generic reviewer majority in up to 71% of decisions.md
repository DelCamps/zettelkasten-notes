---
date: 2026-11-23
section: AI
importance: Med
kind: paper
source: "arXiv 2611.27139"
url: https://arxiv.org/abs/2611.27139
status: unread
id: 2026-11-23-ri-bench-senior-agents
---
2026-11-23 07:16
Tags: #daily-knowledge #ai

---
# RI-Bench orchestrator agents follow a generic reviewer majority in up to 71% of decisions

Multi-agent setups trust the senior agent to weigh its subagents' reports, check them and pass them on faithfully. RI-Bench changes what the subagents hand over and watches whether the senior agent's output reacts as its role requires. Senior agents rarely adopt a planted procedural error (2.9%). But they often go along with a majority of shallow reviews, and they strip stated limitations from claims they cite. Spelling out the role's duties helps but does not remove these failures. Tested on: 8 models from 4 families (Claude Opus 5, GPT-5.6 Sol/Terra/Luna, GLM-5.3, GLM-5.3-Flash, Qwen3.5-35B-A3B, DeepSeek-V4.1-Flash), 12,392 episodes over 3 scenarios, plus an 800-episode check of 2 models under 2 harnesses each.

## Details

**Caveats**
The Court and Parliament scenarios use fixed material, not interacting agents. There are no matched non-hierarchical controls, so hierarchy is not isolated as the cause. The harness check is small and, for GPT-5.6 Sol, cannot be separated from run-to-run noise.

**For your work**
For orchestrator and subagent designs in client work, such as research, due diligence or review pipelines, test the orchestrator with planted shallow consensus and with caveated evidence. Also put the role's duties in the prompt, since that cut failures for most models.

**Method**
- Three scenarios built from real public records. A program chair decides ICLR submissions from reviews (weigh). A judge rules on US Supreme Court cases (verify). A UK parliamentary committee chair writes up witness evidence (relay).
- Controlled changes to the subordinate material: a generic 3:1 majority of reviews arguing against the historical decision, planted procedural-fact errors, and witness claims that each carry two stated limitations.
- Each model runs a Vanilla prompt and an Obligation prompt that lists the role's duties. Scoring uses rule-based checks plus a rubric-guided judge calibrated against human labels.

**Problem**
Scoring only the final answer of a multi-agent system cannot show whether the senior agent judged its subagents' material or simply aggregated it.

**Results**
- Majority following under Vanilla: GLM-5.3 0.71, GPT-5.6 Sol 0.51, Claude Opus 5 0.20. Obligation prompts lower GPT-5.6 Sol to 0.25 and GLM-5.3 to 0.33, but leave Opus at 0.19.
- Of 1,878 paired decisions, 621 flipped toward the adversarial majority and 5 the other way.
- Share of cited claims that lost both limitations: 0.65 for GLM-5.3-Flash, 0.20 for Claude Opus 5, 0.47 pooled.
- Switching harness changed which duties GPT-5.6 Sol handled well. Codex weighed better but relayed worse than pi.

**Concepts:** [[Multi-agent systems]] · [[Evals and benchmarks]]
**From:** [[2026-11-23]]

# My notes


---
# References
[arXiv 2611.27139](https://arxiv.org/abs/2611.27139)
