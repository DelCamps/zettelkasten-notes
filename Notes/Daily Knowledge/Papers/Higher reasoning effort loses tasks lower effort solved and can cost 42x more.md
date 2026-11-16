---
date: 2026-10-27
section: AI
importance: Med
kind: paper
source: "arXiv 2610.34491"
url: https://arxiv.org/abs/2610.34491
status: unread
id: 2026-10-27-effort-economics
---
2026-10-27 07:16
Tags: #daily-knowledge #ai

---
# Higher reasoning effort loses tasks lower effort solved and can cost 42x more

Measuring effort levels counterfactually, the authors find higher effort often fails tasks a lower level solved, costs up to 42x more on tasks every level solves, and disabling reasoning does not save money because agents take longer trajectories. 'Naive laddering' (start low, escalate only after a failed check) matches top effort's success at lower median cost. Tested on: 8 models from 6 providers (OpenAI, Anthropic, Z.ai, Thinking Machines, Moonshot, DeepSeek), 4 benchmarks, agentic tasks run once per level.

## Details

**Caveats**
Agentic tasks were run once per effort level for budget reasons (a four-run check on one benchmark is in the appendix); costs depend on list prices.

**For your work**
Do not ship agents at max effort by default: run low effort with a correctness check and escalate on failure.

**Method**
- Vary only effort, holding tasks, prompts and harness fixed, on AIME 2026, GPQA Diamond, Terminal-Bench v2.1 (Terminus-2) and SWE-Bench Pro (mini-swe-agent).
- Models: GPT-5.6-sol/terra/luna, Claude Sonnet 5, GLM-5.2, Inkling, Kimi K3, DeepSeek-V4-Flash-0731.
- Corrected SWE-Bench Pro variant without git history or open network, since the original containers can leak the reference fix.

**Problem**
Users pick an effort level up front without knowing if the extra thinking will help; the authors call it a credence good.

**Results**
- Every one of the eight models has tasks it loses going from lowest to highest effort on Terminal-Bench; GPT-5.6-sol drops from 76 to 73 of 89 tasks going from high to xhigh.
- On always-solved tasks, mean cost reaches up to 42x the lowest-effort cost.
- Higher effort shifts behaviour toward heavy self-verification and shortcuts like retrieving existing answers.
- Naive laddering matches or improves fixed top-effort success on all models and benchmarks.

**Concepts:** [[Inference efficiency]] · [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-10-27]]

# My notes


---
# References
[arXiv 2610.34491](https://arxiv.org/abs/2610.34491)
