---
date: 2026-10-31
section: AI
importance: High
kind: paper
source: "arXiv 2610.37734"
url: https://arxiv.org/abs/2610.37734
status: unread
id: 2026-10-31-skills-loosen-oversight
---
2026-10-31 07:16
Tags: #daily-knowledge #ai

---
# One in seventeen agent skills tells the agent to skip human oversight, and skill scanners

A study of 1.53 million public SKILL.md files finds about 88,000 (5.8%) contain a directive that loosens oversight, such as 'proceed without asking', '--no-verify' or 'npx -y', and 70.1% of these apply unconditionally. Skills that run shell code, install packages or use sudo have 1.7-1.8 times the odds of such a line, and two vendor skill scanners catch at most 46% of them at precision below 0.4. Tested on: 1.53M English skills from public GitHub (GitSkills), 2,097 hand-labelled units, two open-source scanners; text analysis only, no agent runs.

## Details

**Problem**
A skill is loaded as instructions when the agent acts, so one line in a widely copied skill can remove a human checkpoint from every agent that installs it. Nobody had measured how often skills do this.

**Method**
- 36-pattern lexicon pulls 1.37M candidate units (sentences, bullets, table cells, code lines) from 1,527,281 distinct English skills.
- Codebook labels each as directive or mention, loosening or tightening, with mechanism and scope; 2,097 units labelled by hand, LLM second coder (kappa 0.82).
- RoBERTa + Jev detector (accuracy 0.80) labels everything; logistic regressions on skill capabilities; Cisco AI Defense and NVIDIA SkillSpector scanners audited on 400 gold units.

**Results**
- 13.3% of candidate units loosen oversight, 36.4% tighten; loosening works mainly through permission flags (33.9%), skipped confirmation (27.4%) and 'don't stop' (16.0%).
- 12,484 skills (0.82%) combine loosening with sudo, curl | sh or destructive commands.
- 2.4% of loosening-carrying families account for half of all copies; 93.4% of variants leave the ancestor's oversight text untouched.
- Scanners catch 2-28% offline and 15-46% with LLM analysis; GPT-5.4 asked the codebook's oversight question catches 61% at precision 0.71.

**Caveats**
Measures text, not whether agents obey it. One human coder plus an LLM; the lexicon misses many phrasings, so counts are lower bounds. Public GitHub only.

**For your work**
Before installing third-party skills for client agents, grep them for permission flags, 'without asking' and 'keep going' lines, and keep approval gates in the harness rather than relying on skill text. When screening skills with an LLM, ask about oversight, not malice.

**Concepts:** [[Agent security]] · [[Coding agents]] · [[AI safety]]
**From:** [[2026-10-31]]

# My notes


---
# References
[arXiv 2610.37734](https://arxiv.org/abs/2610.37734)
