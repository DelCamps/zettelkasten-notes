---
date: 2026-11-08
section: AI
importance: High
kind: paper
source: "arXiv 2611.04813"
url: https://arxiv.org/abs/2611.04813
status: unread
id: 2026-11-08-agenticfinbench
---
2026-11-08 07:16
Tags: #daily-knowledge #ai

---
# AgenticFinBench auditing financial agents' claims for hallucinations knocks the rubric-onl

On 230 real financial requests, a claim-level audit (is each claim backed by the agent's own trace, and is it refuted by outside evidence?) cut DeepSeek V4.1 Flash on the Pi harness by 7.58 points and dropped it from first to fourth, while GPT-5.6 Sol on Codex CLI ended up on top. Every configuration hallucinated: 0.9% to 47.0% of responses had at least one refuted, ungrounded claim, and the same model scored anywhere from 71.27 to 88.79 depending on the harness. Tested on: 18 model-harness configurations (10+ models incl. GPT, Claude, DeepSeek, Gemini, Kimi; up to four harnesses per model), 230 questions in 2 languages, one run each, audit checked against senior financial experts on 1,800 sampled responses.

## Details

**Caveats**
One response per question per configuration. Claim extraction, audit and rubric judging lean on DeepSeek models, which also power four of the evaluated configurations (the authors test for self-preference). Harnesses differ in instructions and tools, so harness effects are for whole configurations.

**For your work**
For finance or audit agents, a rubric score alone can reward fabrication. Add a provenance check (is every figure in the trace?) and score the full model plus harness, not the model alone. The two-stage audit design can be reused for client evals.

**Method**
- 230 real-world financial tasks across 8 categories, 2 languages and 4 complexity levels, each with question-specific rubrics.
- Two-stage claim audit: first, is the claim supported by tool/API output or calculations in the agent's trace (the agent's own reasoning does not count)? Second, is an unsupported claim verified or refuted by outside sources? Only claims that are both ungrounded and refuted count as hallucinations.
- 18 configurations: six models on Codex CLI, plus DeepSeek V4.1 Flash, GPT-5.6 Sol and Claude Opus 5.5 each run on 3-4 harnesses (Claude Code CLI, Codex CLI, Pi, DSH and others).
- Audit agreement with adjudicated expert labels was comparable to agreement between the experts themselves; a judge from an outside model family re-ranked configurations with Kendall tau 0.89.

**Problem**
Financial requests are often open-ended with no single right answer, and rubric-only LLM grading cannot tell a well-argued answer from one built on invented numbers.

**Results**
- Mean quality ranges from 65.42 to 89.20; the top three are within 0.6 points.
- Hallucinated claims are rare per claim (0.03%-2.38%) but common per response (0.9%-47.0%); 41.7% of responses from the fourth-ranked DeepSeek on Pi had one, compared with 3.0% for GPT-5.6 Sol on Codex CLI.
- For claims that are true but not backed by the trace, harness choice explained 28.6% of the variation and model choice 8.8%.
- Cost spans about 120x ($0.0076-$0.9125 per response); the most expensive configuration ranked twelfth. Quality drops from 89.44 on direct retrieval to 79.18 on the hardest tasks.

**Concepts:** [[Evals and benchmarks]] · [[Hallucination]] · [[Agents]]
**From:** [[2026-11-08]]

# My notes


---
# References
[arXiv 2611.04813](https://arxiv.org/abs/2611.04813)
