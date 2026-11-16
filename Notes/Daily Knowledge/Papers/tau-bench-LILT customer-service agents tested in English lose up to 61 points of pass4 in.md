---
date: 2026-11-07
section: AI
importance: Med
kind: paper
source: "arXiv 2611.07203"
url: https://arxiv.org/abs/2611.07203
status: unread
id: 2026-11-07-tau-bench-lilt
---
2026-11-07 07:16
Tags: #daily-knowledge #ai

---
# tau-bench-LILT customer-service agents tested in English lose up to 61 points of pass4 in

LILT natively localized tau-bench (airline, retail, telecom, banking) into German, Korean, Turkish and Farsi, including databases, user simulators and tasks. German tracks English closely, but Korean and Farsi retail drop by up to 61 points in pass^4, often from simple mistakes like romanizing Hangul names before a lookup (Claude Opus 5 did so in 296 of the 360 Korean retail conversations where it looked up a name). Tested on: eight agent models from six providers (Claude Opus 5.5, Claude Opus 5, GPT-6 Sol, GPT-5.6 Sol, Gemini 3.8 Flash, Nemotron 3 Ultra, Mistral Medium 3.5, Command A+), four domains, four trials per task.

## Details

**Caveats**
No Spanish or other Romance languages. Scores are not meant to be directly comparable to English. Banking uses only a 20-task sample; reasoning was mostly disabled.

**For your work**
For Spanish or multilingual deployments, do not certify on English evals: localize the test data (names, addresses, ID formats) and check tool schemas like first_name/last_name against local conventions, plus language-switching in replies.

**Method**
- Full localization by native speakers: culturally plausible customer records, refined user-simulator prompts, localized tasks and reward functions
- Official tau-bench scaffold, low or no reasoning to mimic latency-sensitive support, pass^1 and pass^4 over four trials
- Manual analysis of failure modes the deterministic reward misses

**Problem**
Agent evaluations are almost all in English, yet companies roll a tested English support agent into new languages and assume the model generalizes.

**Results**
- Models beat their English score in 13 of 32 German model-domain pairs, but drop up to 61 points of pass^4 in Korean and Farsi retail
- Roaming tasks pass in 97.9% of trials when the agent asks the user's location vs 16.1% when it never comes up; agents ask less in Turkish and Farsi
- Claude Opus 5 hallucinated a user message in 68.9% of Korean telecom trials, and wrote prompt injections against itself in 4.2%
- Found ten latent bugs in the original English airline and retail tasks

**Concepts:** [[Evals and benchmarks]] · [[Agents]] · [[Frontier models]]
**From:** [[2026-11-07]]

# My notes


---
# References
[arXiv 2611.07203](https://arxiv.org/abs/2611.07203)
