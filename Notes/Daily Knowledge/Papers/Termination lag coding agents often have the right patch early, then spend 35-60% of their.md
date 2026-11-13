---
date: 2026-11-13
section: AI
importance: Med
kind: paper
source: "arXiv 2611.14960"
url: https://arxiv.org/abs/2611.14960
status: unread
id: 2026-11-13-termination-lag
---
2026-11-13 07:16
Tags: #daily-knowledge #ai

---
# Termination lag coding agents often have the right patch early, then spend 35-60% of their

Penn State researchers saved and tested every intermediate patch an agent produced. In runs that reached a correct fix, the first source edit was already correct 38-82% of the time, yet a median 35-60% of the steps in solved runs came after the first correct patch, mostly spent verifying and exploring. In 1-8% of those runs, later edits broke the fix. Tested on: 5 models (Claude Haiku 5.5, GPT-6 Luna, Qwen3-Coder-30B, Laguna-XS.2, Seed-OSS-36B), 2 harnesses (OpenHands, mini-SWE-agent), 3 SWE-bench sets, each task run once.

## Details

**Caveats**
One run per task. Cost is counted in steps, not dollars. The oracle stop needs hidden tests that a real agent lacks, so this is an upper bound on savings.

**For your work**
On long coding-agent runs, a budget or stop rule tied to your own test results (not the agent's judgement) could save a lot. Snapshot patches as the agent goes so you can roll back to a correct earlier state. Read this together with last week's finding that skipping checks hurts: verification is needed, but agents overdo it.

**Method**
- A logging proxy snapshots the repository diff after every agent step without the agent noticing. Each distinct patch is then graded offline against the hidden official tests.
- Defines time to first correct patch and termination lag (steps after it), and classifies post-fix steps as verify, explore, edit or wrap-up.

**Problem**
Final-patch scoring hides when an agent actually solved the task. Every extra step costs tokens over a growing context and can break working code.

**Results**
- Median normalised lag: Qwen3-Coder 35% (Verified) and 37% (Multilingual), Laguna-XS.2 60% and 54%, Claude Haiku 5.5 54%, GPT-6 Luna 36%, mini-SWE-agent 37%.
- Verification took 48-63% of post-fix steps and exploration 15-29%. Input context grew by up to 78% after the fix.
- An oracle that stopped at the first correct patch would cut a median 35-60% of steps in solved runs without losing any solved task.

**Concepts:** [[Coding agents]] · [[Evals and benchmarks]] · [[Inference efficiency]]
**From:** [[2026-11-13]]

# My notes


---
# References
[arXiv 2611.14960](https://arxiv.org/abs/2611.14960)
