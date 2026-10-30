---
date: 2026-10-30
section: AI
importance: High
kind: paper
source: "arXiv 2610.38244"
url: https://arxiv.org/abs/2610.38244
status: unread
id: 2026-10-30-coding-agents-follow-precedent
---
2026-10-30 07:16
Tags: #daily-knowledge #ai

---
# Coding agents copy the repo's existing patterns over your instructions, unless a written r

In 5,625 trials, coding agents followed existing repository code over their own defaults in 359/360 trials, and code examples alone were a weak way to steer them away from it. A written priority rule worked: 59/60 joint successes against 38/60 for examples, and a rule in CLAUDE.md/AGENTS.md lifted four open-source repos from 0/120 to 117/120. Tested on: four models from two providers (Claude Sonnet and Opus in Claude Code, two GPT models in Codex), six implementation pairs, 15 runs per cell, plus four open-source repos in Python, Go and TypeScript.

## Details

**Caveats**
Controlled experiments use one Flask task family; only two providers; differences cannot be split between model and harness; the outcome is which pattern was chosen, not overall code quality.

**For your work**
When a client codebase has a convention you want to change, examples in the prompt won't override it; state the priority as an explicit rule in CLAUDE.md/AGENTS.md or the task text, and expect agents to copy whatever the nearest files do.

**Method**
- Controlled Flask API repos where existing endpoints use one of six alternative patterns (ID type, field casing, error handling, response envelope, etc.); hidden tests accept either
- Vary how many files and which files carry the precedent, then add conflicting task intent with no guidance, code examples, written rules or both
- Check the results on four real open-source repositories

**Problem**
Several implementations can pass the same tests, so what decides which one a coding agent picks when existing code, its own defaults and the new task disagree?

**Results**
- All four agents share the same defaults, but follow the opposite repo precedent in 359/360 trials
- Three supporting local files give 96% adoption, against 4% for files of a sibling resource; moving the files alone can swing adoption from 0% to 100%
- Written rules: 59/60 joint success, code examples 38/60, no guidance 0/60; a native instruction-file rule gives 117/120 in the open-source repos, against 0/120 without it

**Concepts:** [[Coding agents]] · [[Evals and benchmarks]]
**From:** [[2026-10-30]]

# My notes


---
# References
[arXiv 2610.38244](https://arxiv.org/abs/2610.38244)
