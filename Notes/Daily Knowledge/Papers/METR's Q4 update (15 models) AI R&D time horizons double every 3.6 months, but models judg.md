---
date: 2026-11-23
section: AI
importance: Med
kind: paper
source: "METR"
url: https://metr.org/blog/2026-11-20-q4-2026-capability-update/
status: unread
id: 2026-11-23-metr-q4-capability-update
---
2026-11-23 07:16
Tags: #daily-knowledge #ai

---
# METR's Q4 update (15 models) AI R&D time horizons double every 3.6 months, but models judg

METR's capability update across 15 public models from GPT-4o to Opus 5.5 and GPT-6 Astra finds time horizons on its combined TH1.1 and new TH2 suites doubling about every 3.61 months, with up to 27 hours on verifiable TH2 tasks. Models beat its recruited expert baseliners on well-defined optimization tasks but do worse on tasks that are costly to build into RL environments and on judgment-heavy tasks, and model judges overrate work by similarly strong or stronger models. Tested on: 15 OpenAI and Anthropic models (plus Fable) on 222 TH1.1 tasks, 36 new TH2 tasks and 75 MirrorCode tasks, with a ReAct-style scaffold.

## Details

**Caveats**
Only 9% of human time estimates come directly from human baselines; the rest are researcher estimates. Few human baselines were collected, and METR says the trend results are sensitive to its methodological choices and judgment tasks may be under-elicited.

**For your work**
Expect agents to do well on tasks with a clear, cheap check and much worse where quality is fuzzy. Don't let a model grade output from a model as strong as itself without human calibration, and favour client evals that are hard to game.

**Method**
- Ran 15 models (GPT-4o, o1, GPT-5 to GPT-6 Astra, Opus 4.5 to Opus 5.5, Fable 5 and 5.1) at xhigh or higher reasoning effort, using a ReAct-style scaffold with bash, python and image tools
- Built TH2: 36 tasks in 12 families, both verifiable (Al Zimmermann contests, Budget NanoGPT, Minecraft bot, Slay the Spire) and hard-to-verify or judgment tasks (making METR tasks, judging runs, rating philosophy critiques)
- Scored tasks at several thresholds and fitted an IRT index (MCI); estimated each task's 'Lifecycle Cost' (cost to build, run and score it 100 times) with an Opus 5.5 judge calibrated on about 10 tasks

**Problem**
METR's original time-horizon tasks are saturated, and cheap containerized evals look like the RL environments labs train on, so they may overstate real AI R&D ability. METR wants to know how fast the capabilities that matter for automating AI research are improving.

**Results**
- Time horizons double every 3.61 months (95% CI 2.08-4.94) on TH1.1 plus TH2, and every 1.65 months on the verifiable TH2 subset; frontier models reach up to 27 hours there
- On 15 Al Zimmermann contests the best models place at the median 96th-98th percentile of human entrants; the best Budget NanoGPT agent run got a 15.7% speedup in 48 hours, against 41% for a strong human record
- Tasks in the costlier-to-build half are 2.9x as expensive and models do 2.9x worse on them in time horizon (about 1.5 doublings), though both halves improve at similar rates
- Model judges overrate tasks built by similarly strong or stronger models; Opus 5.5, the best judge, scored Astra's tasks about 0.2 (out of 1) higher than METR's human scorer. No agent-built eval task was good enough to use

**Concepts:** [[Evals and benchmarks]] · [[Frontier models]] · [[AI safety]]
**From:** [[2026-11-23]]

# My notes


---
# References
[METR](https://metr.org/blog/2026-11-20-q4-2026-capability-update/)
