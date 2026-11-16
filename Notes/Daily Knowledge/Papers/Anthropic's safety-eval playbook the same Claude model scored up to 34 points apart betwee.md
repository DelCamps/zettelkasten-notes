---
date: 2026-11-14
section: AI
importance: Med
kind: paper
source: "Anthropic Engineering"
url: https://www.anthropic.com/research/building-strong-safety-evaluations
status: unread
id: 2026-11-14-anthropic-safety-evals-guide
---
2026-11-14 07:16
Tags: #daily-knowledge #ai

---
# Anthropic's safety-eval playbook the same Claude model scored up to 34 points apart betwee

Anthropic describes how it builds safety evals: expert-written multi-turn simulations where a separate Claude plays the user, paired harmful and benign prompts, atomic yes/no grader rubrics checked against human labels, preregistered metrics, and at least 100 items for multi-turn or 1,000 for single-turn evals. Its own examples show why: single-turn harmless rates sit at 94% to 98% for every recent model, and a 98% vs 94% gap between Claude Opus 5 and Opus 5.5 on a romance-scam eval was not statistically significant. Tested on: Anthropic's internal safety evals of Claude models only; a methods guide with examples, not a controlled study.

## Details

**Caveats**
Guidance from Anthropic's own evals, with no new benchmark and no cross-vendor comparison.

**For your work**
A ready checklist for client eval and red-team work: paired harmful/benign sets, simulated multi-turn users, grader validation and intervals, and testing the deployed configuration (system prompt, tools), not just the raw API.

**Method**
- Domain experts write a scenario spec (user goal, tactics, persona, tone); the first user turn is fixed, a separate Claude writes later user turns, each scenario runs several times, and a grader scores against an expert rubric.
- Measure an 'appropriate response rate', not refusal, and pair harmful with benign prompts to catch over-refusal.
- Graders use atomic yes/no criteria, never see design metadata, ideally differ from the tested model, and are validated against human labels; metrics are preregistered and reported with confidence intervals.

**Problem**
Claims that a model is 'safer than its predecessor' are only as good as the eval behind them, and evals are easy to game, poorly documented and sensitive to format.

**Results**
- Single-turn suites cover 16 policy areas in seven languages and are saturated, useful mainly as regression checks.
- Claude Fable 5.1 differed by up to 34 points between API and claude.ai configurations on multi-turn safety evals.
- A targeted system-prompt fix gave 60% on the API vs 94% on claude.ai on a self-harm eval; multi-turn intervals can exceed ±10 points.

**Concepts:** [[Evals and benchmarks]] · [[AI safety]] · [[Claude]]
**From:** [[2026-11-14]]

# My notes


---
# References
[Anthropic Engineering](https://www.anthropic.com/research/building-strong-safety-evaluations)
