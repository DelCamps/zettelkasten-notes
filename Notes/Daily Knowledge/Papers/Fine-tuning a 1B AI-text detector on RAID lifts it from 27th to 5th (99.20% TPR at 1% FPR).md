---
date: 2026-11-22
section: AI
importance: Med
kind: paper
source: "Hugging Face blog (community)"
url: https://huggingface.co/blog/empirischtech/how-we-took-a-1b-detector-from-27th-to-5th-on-raid
status: unread
id: 2026-11-22-raid-detector-overfit
---
2026-11-22 07:16
Tags: #daily-knowledge #ai

---
# Fine-tuning a 1B AI-text detector on RAID lifts it from 27th to 5th (99.20% TPR at 1% FPR)

Empirisch Tech fine-tuned its 1B Ettin-based detector on RAID's training data and then on the 50,000 hardest examples, raising its leaderboard score from 92.81% to 99.20% and its rank from 27th to 5th of 58. Outside RAID the same model got much worse: on the team's own held-out set the share of AI texts caught fell from 97.8% to 58.7%, and a likely cause is a formatting cue (blank lines in 61.5% of machine rows but 0.33% of human rows). Tested on: one 1B detector family, the RAID benchmark plus one in-house held-out set of 66,586 human texts; English only.

## Details

**Caveats**
One vendor's own detector and own held-out set; the blank-line explanation is likely but not yet confirmed by retraining. The RAID-2 model is released only as a research model, and general users get a separate model.

**For your work**
A clear example of benchmark overfitting to show clients who pick tools by leaderboard rank. Any detector, judge or classifier you tune on a public benchmark needs a held-out set from the client's own data before you trust it.

**Method**
- Base: a 1B Ettin encoder trained on about 2.2 million English texts that predicts the AI share of 512-token windows.
- RAID-1: fine-tuned on 252,020 RAID training rows Base had not seen, mixed with replay data.
- RAID-2: one more epoch on the 50,000 lowest-scoring machine texts (hard-example mining).
- Two pre-registered tests for shortcut cues (typos, odd formatting), plus a blank-line insertion test.

**Problem**
Leaderboard ranks for AI-text detectors are used to choose products, but nobody measures what fitting a benchmark does to performance on real-world text.

**Results**
- RAID leaderboard TPR at 1% FPR: 92.81% (v7) to 99.20% (RAID-2), 5th of 58; the hard-example round added only 0.4 points against 5.0 from RAID-1.
- Held-out AI texts caught: 97.8% (Base), 66.6% (RAID-1), 58.7% (RAID-2).
- Fresh human texts wrongly flagged rose from 1.0% to 3.0% (RAID-1) and 2.4% (RAID-2).
- Adding blank lines to unedited human texts raised RAID-2's flag rate from 2.4% to 7.8%.

**Concepts:** [[Evals and benchmarks]]
**From:** [[2026-11-22]]

# My notes


---
# References
[Hugging Face blog (community)](https://huggingface.co/blog/empirischtech/how-we-took-a-1b-detector-from-27th-to-5th-on-raid)
