---
date: 2026-11-19
section: AI
importance: Med
kind: paper
source: "arXiv 2611.23588"
url: https://arxiv.org/abs/2611.23588
status: unread
id: 2026-11-19-arise-self-evolving-memory
---
2026-11-19 07:16
Tags: #daily-knowledge #ai

---
# ARISE (Amazon) agents that learn scoped rules from their own failures gain 10.9 points on

Amazon's ARISE turns each failed task into a one-line [WHEN: condition] correction, consolidates these into a capped set of rules, and only accepts a rule update if held-out accuracy rises; model weights, tools and workflow stay fixed. With Claude Opus 4.6 writing the rules it gains 10.9 pp on SOP-Bench and 5.8 pp on tau2-bench, beating GEPA, while per-task cost changes by -1.0%. Tested on: 5 models from 3 providers on Amazon Bedrock (Claude Opus 4.6, Sonnet 4.6, Haiku 4.5, DeepSeek v3.2, Qwen3-32B), 14 enterprise-workflow domains, three runs.

## Details

**Caveats**
Needs tasks with verifiable outcomes; with pass/fail feedback only the gain drops to 3.1 pp, and 20% wrong labels cut it to 7.2 pp. Authors are from Amazon; benchmarks are synthetic SOP and customer-service suites.

**For your work**
A cheap pattern for client agents with SOPs and labelled outcomes: learn a small, reviewable rule list from failures and gate it on a held-out set, then re-run the loop when the client swaps models. The governance angle (inspectable rules, accept-only-if-better) is easy to sell.

**Method**
- An offline loop collects failed training tasks with the expected output or failed checks, and an attributor (the deployed model itself or a teacher, Opus 4.6) writes one scoped correction per failure.
- Corrections are kept as retrievable micro memory and consolidated into a bounded set of macro rules (append or rewrite candidates).
- A gate accepts a rule update only if held-out validation accuracy improves; rules are short and inspectable before deployment.

**Problem**
Enterprise agents face model upgrades and changing SOPs; rebuilding or re-prompting each time is costly, and memory that grows context raises serving cost.

**Results**
- ARISE-Teacher: 87.4% on SOP-Bench and 62.3% on tau2-bench, +10.9 pp and +5.8 pp over the original prompt; the SOP-Bench gain holds for every model, from 8.8 pp (Haiku 4.5) to 12.2 pp (Qwen3-32B).
- Beats GEPA by 4.5 pp on tau2-bench and 1.4 pp on SOP-Bench; ExpeL and Reflexion stay near baseline. ARISE-Self (no teacher) still gains 10.0 pp on SOP-Bench.
- Adds about 1,340 characters of memory per task yet makes 4.0% fewer model calls; one adaptation run averages $17.46 ($1.49 for Qwen3-32B to $42.20 for Opus 4.6).

**Concepts:** [[Agent memory]] · [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-11-19]]

# My notes


---
# References
[arXiv 2611.23588](https://arxiv.org/abs/2611.23588)
