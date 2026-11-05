---
date: 2026-11-05
section: AI
importance: Med
kind: paper
source: "arXiv 2611.05662"
url: https://arxiv.org/abs/2611.05662
status: unread
id: 2026-11-05-agent-judge-confirmation-bias
---
2026-11-05 07:16
Tags: #daily-knowledge #ai

---
# Tool-using agent judges overturn up to 40% of correct verdicts after one false 'expert pre

Researchers gave Agent-as-a-Judge evaluators tools and full trajectories, then added a single false note saying an expert had already judged the run. Even after gathering the decisive evidence themselves, judges flipped up to 40% of their correct verdicts. For the Claude judges, 67-75% of the harmful flips came from over-trust: they checked, concluded correctly, then deferred anyway. Tested on: 4 judges from 3 families (Sonnet 4.6, Opus 4.7, Qwen3-235B, GPT-OSS-120B), 5 datasets, 3 runs per arm.

## Details

**Caveats**
The main cue is deliberately overt, the property ablation uses one model, and the mitigations were written with the attack in mind, so their gains are an optimistic bound.

**For your work**
In eval pipelines, strip prior verdicts, reviewer notes and status labels from what the judge sees. Treat judge inputs as an attack surface, alongside yesterday's fake-warning and score-seeking results.

**Method**
- Each item is judged 3 times without the cue and 3 times with it, with the cue pointing against the uncued majority verdict
- Datasets: AJ-Bench (Postgres, Filesystem, Deep Search), SWE-Bench Verified and Terminal-Bench 2.0, scored against deterministic ground truth
- A trajectory-aware meta-judge sorts each flip into over-trust, hallucination or under-investigation

**Problem**
Agent-as-a-Judge is assumed to be grounded because it checks the environment itself. This paper tests whether that grounding protects it from confirmation bias.

**Results**
- Every judge on every dataset flipped some correct verdicts; proprietary and open-weight judges were about equally susceptible
- Flips were more frequent on harder-to-verify tasks than on test-backed SWE-Bench Verified
- False 'it failed' cues moved judges more than 'it passed' cues on 4 of 5 datasets
- Even a hedged, non-authoritative remark flipped 10% of correct verdicts; cue-aware mitigations reduced flips but never removed them

**Concepts:** [[Evals and benchmarks]] · [[Agent security]]
**From:** [[2026-11-05]]

# My notes


---
# References
[arXiv 2611.05662](https://arxiv.org/abs/2611.05662)
