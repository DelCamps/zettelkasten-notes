---
date: 2026-11-26
section: AI
importance: Med
kind: paper
source: "arXiv 2611.33943"
url: https://arxiv.org/abs/2611.33943
status: unread
id: 2026-11-26-skillsbench-audit
---
2026-11-26 07:16
Tags: #daily-knowledge #ai

---
# SkillsBench re-audited no task-level 'skills hurt' result survives statistics, and skill-g

A source-level audit and reanalysis of 7,554 public SkillsBench trials finds that 'this skill harmed this task' results are run-to-run noise. With at most three runs per cell, 58% of cells could not have shown a decrease at all, and no per-task loss is significant after correction. Part of the headline lift comes from scoring rules that only the skill text revealed: the average lift on three such tasks was 74.6 points. One harness also injected 48 built-in skills. Tested on: reanalysis of 7,554 trials (1,421 cells) from Claude Code, Codex, Gemini CLI and OpenHands configurations.

## Details

**Caveats**
Re-uses public logs only, with no new runs. Held-out tests use single trial pairs per cell.

**For your work**
Don't retire or gate client skills on 1-3 runs. Check whether a skill is just leaking grader conventions, and run shuffled-label checks before trusting a 'skill hurts' result.

**Method**
- Source-code audit of prompts, graders and skill packages.
- Pooled per-cell reanalysis with multiple-testing correction.
- Gating policies were tested against label-shuffled null runs and on held-out trials.

**Problem**
SkillsBench reports that curated agent skills add about 16.6 points on average but hurt some tasks, and later work gates or drops skills based on those per-task numbers.

**Results**
- Overall lift is 18.7 points. Three tasks had grading conventions or definitions found only in the skill text.
- Four tasks contained placeholder skill directories. In 155 of 184 with-skill OpenHands prompts, 48 built-in skills were listed first.
- Gating by the skill-free score looks 2-3 points better than always loading skills, but shuffled labels give 4-7 points. On held-out runs there is no significant gain.
- The 'risk forest' gate's AUC of 0.878 is mostly from a trivial indicator (0.829 alone).

**Concepts:** [[Evals and benchmarks]] · [[Coding agents]] · [[Agents]]
**From:** [[2026-11-26]]

# My notes


---
# References
[arXiv 2611.33943](https://arxiv.org/abs/2611.33943)
