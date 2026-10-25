---
date: 2026-10-24
section: AI
importance: Med
kind: news
source: "Moonshot AI blog"
url: https://www.kimi.ai/blog/kimi-k3-1-pro
status: unread
id: 2026-10-24-kimi-k3-1-pro
---
2026-10-24 07:16
Tags: #daily-knowledge #ai

---
# Kimi K3.1 Pro 3T-class open-weight model, weights by 4 Nov

Moonshot's post-trained K3 with 1M context reports 65.7% on Terminal-Bench 4.0 (Opus 5.5 66.4%, GPT-6 Astra 58.2%) and cuts claim-level hallucination on its adversarial internal test from 23.4% to 8.3% with tools. Notably they stripped cyber data from mid-training and RL, dropping their internal cyber score from 90.5% to 81.0% before the open release. Benchmarks are vendor-reported, many internal.

## Details

**Problem**
Moonshot is releasing Kimi K3.1 Pro, a post-trained Kimi K3 aimed at agentic coding, 3D work and finance. It also wants to limit how much offensive cyber capability the open weights carry.

**Method**
- A 3T-class open-weight model with a 1M-token context, trained with much more post-training compute and joint RL across hundreds of domains. A Highspeed variant runs 2-3x faster.
- Cyber-related data was identified and removed from both mid-training and the RL environment mix, while general coding tasks were kept.
- Available now in Kimi apps and the API (kimi-k3.1-pro). Full weights are due by 4 Nov 2026.

**Results**
- Terminal-Bench 4.0: 65.7%, against 66.4% for Claude Opus 5.5 and 58.2% for GPT-6 Astra (Claude Code harness).
- Claim-level hallucination on the internal Kimi Hallu Bench Hard fell from 23.4% (K3) to 8.3%. BenchCAD with tools: 92.7% (Opus 5.5 96.2%). OfficeQA Pro v2: 64.4.
- Internal xdev-bench-hard cyber exploit pass@3 was 90.5% without the data removal and 81.0% for the released model.

**Caveats**
Results are vendor-reported, and many benchmarks are internal (Kimi Code Bench, Hallu Bench, xdev-bench). Competitor scores are partly taken from leaderboards and blog posts. Moonshot says the hallucination test is a deliberately adversarial stress test and does not reflect everyday error rates. Weights are not out yet.

**For your work**
Once the weights land, it is a candidate open model for self-hosted coding agents, since Moonshot evaluated it in the Claude Code harness. Run your own agent evals first, given how many of the numbers are internal.

**Concepts:** [[Open-weight models]] · [[Coding agents]] · [[Hallucination]]
**From:** [[2026-10-24]]

# My notes


---
# References
[Moonshot AI blog](https://www.kimi.ai/blog/kimi-k3-1-pro)
