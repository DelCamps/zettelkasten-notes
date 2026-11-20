---
date: 2026-11-20
section: AI
importance: Med
kind: paper
source: "arXiv 2611.25534"
url: https://arxiv.org/abs/2611.25534
status: unread
id: 2026-11-20-skill-self-rewrite-erosion
---
2026-11-20 07:16
Tags: #daily-knowledge #ai

---
# Letting models rewrite expert agent skills without feedback makes them worse -14.6 points

HKUST researchers had six models rewrite expert-written agent skills round after round with no task or feedback, then ran agents on the rewritten skills: every model did worse on every benchmark, by 14.6 points on average on SkillsBench after 30 rounds. Rewriting pulls a skill towards what the model would write anyway and drops the expert knowledge outside that, which kept only 23.1% of such items. A tagging trick, SkillDiff, that marks that knowledge in place added 4.8 points without changing the skill's text. Tested on: 6 models from 4 families, 3 benchmarks, 3 harnesses (Codex, Claude Code, OpenHands).

## Details

**Caveats**
Rewriting here has no feedback at all, unlike most self-evolving systems; a single LLM judge (GPT-5.6-Luna) scores parts of the evaluation, checked against others in the appendix.

**For your work**
Version-control client skills and CLAUDE.md files and do not let agents 'tidy' them unsupervised; the parts that look odd to the model are usually the valuable ones. SkillDiff's tag-what-the-model-would-not-write idea is cheap to try on existing skill libraries.

**Method**
- Six models (GPT-5.6-Luna, GPT-6.1-Sol, MiMo-V2.5-Pro, Claude Haiku 5.5, Qwen3.7-Plus, Qwen3.8-Flash) each rewrote each skill for 30 rounds with no task, run or judgment
- Agents on the same models then used the rewritten skills on SkillsBench (87 tasks), LogicBench (760 questions) and MedCalc-Bench (1,100 questions)
- The model's 'prior' was measured with ten skills it wrote from the topic alone
- SkillDiff tags with [FOCUS] every item of the original skill that none of the ten self-written skills states, and asks the agent to carry those items into its plan

**Problem**
Agent skills (procedural instructions written by experts) are more and more often maintained by models rewriting them without feedback. Nobody had measured whether this adapts the skill or erodes it.

**Results**
- Average drop at round 30: -14.6 points on SkillsBench, -14.7 on LogicBench, -11.1 on MedCalc-Bench; SkillsBench was already -7.1 after one round
- Worst case: GPT-5.6-Luna -23.0 on SkillsBench; Claude Haiku 5.5 -17.4 on MedCalc-Bench
- MedCalc-Bench accuracy fell from 89.7% to 78.7%, below the 81.1% with no skill at all
- Items outside the model's prior survived 30 rounds 23.1% of the time vs 84.2% for items all ten self-written skills state; SkillDiff added 4.8 points on SkillsBench (up to +12.6 for GPT-5.6-Luna)

**Concepts:** [[Agents]] · [[Agent memory]] · [[Evals and benchmarks]]
**From:** [[2026-11-20]]

# My notes


---
# References
[arXiv 2611.25534](https://arxiv.org/abs/2611.25534)
