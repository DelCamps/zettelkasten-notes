---
date: 2026-11-22
section: AI
importance: Med
kind: paper
source: "arXiv 2611.25588"
url: https://arxiv.org/abs/2611.25588
status: unread
id: 2026-11-22-judge-scale-reversal
---
2026-11-22 07:16
Tags: #daily-knowledge #ai

---
# Rename '5 = Excellent' to '1 = Excellent' and LLM judges change their verdicts 30 of 35 ju

The authors reversed the numbers on judging rubrics while keeping every description the same, then compared the disagreement with each judge's own disagreement when simply run twice. Every one of 35 judge-benchmark pairs showed a non-negative gap, 30 above a 0.02 threshold and 25 with confidence intervals above zero, and for gpt-4o-mini on BiGGen-Bench the leaderboard order barely survived the flip (Kendall tau 0.286). Tested on: 7 judges from 3 families (Google Gemma, Qwen, OpenAI including open-weight gpt-oss), 5 meta-evaluation benchmarks, greedy decoding, 2,000-sample bootstrap intervals.

## Details

**Caveats**
Exact-match agreement is used, so magnitudes are only comparable within a benchmark. The deficit is a behavioural signal, not a causal decomposition, and it depends somewhat on which repeat run is used as the baseline. No Anthropic or Google API judges were tested.

**For your work**
Before trusting an LLM judge in a client eval pipeline, run it twice and once with the scale reversed; if the reversed run disagrees much more than the repeat, the scores are partly about the numbers. Averaging both directions costs one extra pass.

**Method**
- Scale-reversal probe: invert the score anchors, keep the criteria, remap the scores back
- Floor normalization: subtract the judge's test-retest agreement (two identical runs) so noisy judges are not mistaken for biased ones
- Bidirectional anchor averaging: score once in each direction and average, as a mitigation

**Problem**
Rubric scoring assumes the numbers are arbitrary labels for the descriptions. If a judge leans on the numbers themselves, its scores reflect the scale design rather than the criteria.

**Results**
- Deficits ranged up to 0.333 (Gemma-4-31B on MT-Bench's 10-point scale); gpt-4o-mini had the largest deficit on SummEval, BiGGen-Bench and JudgeBench
- Raw agreement misleads: Gemma-4-31B and gpt-5.4 both had about 0.81 flip agreement on SummEval, but their deficits were 0.169 vs 0.042 once each judge's own repeatability was subtracted
- Size did not help: Qwen3.5-122B showed larger deficits than Qwen3.5-27B on four of five benchmarks
- Averaging both directions changed agreement with human ratings only slightly, by at most +0.040

**Concepts:** [[Evals and benchmarks]]
**From:** [[2026-11-22]]

# My notes


---
# References
[arXiv 2611.25588](https://arxiv.org/abs/2611.25588)
