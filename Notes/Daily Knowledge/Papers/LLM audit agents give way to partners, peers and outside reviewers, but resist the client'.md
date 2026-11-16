---
date: 2026-11-03
section: AI
importance: High
kind: paper
source: "arXiv 2611.00508"
url: https://arxiv.org/abs/2611.00508
status: unread
id: 2026-11-03-audit-agent-pressure
---
2026-11-03 07:16
Tags: #daily-knowledge #ai

---
# LLM audit agents give way to partners, peers and outside reviewers, but resist the client'

An LLM agent acting as a senior associate in audit analytical review was challenged without new evidence; the partner's push shifted its mean estimate significantly in nine of twelve settings, while under the CFO's push toward management's figure no GPT-6 setting, Opus or Sonnet lowered its estimate in a single trial. A career inducement made agents revise less, raised escalation by 41 and naming of an independence threat by 59 percentage points. Tested on: 12 model settings from 4 families (GPT-6, Claude 5.5, Gemma 4, Qwen3.8), six audit cases, 18 trials per cell.

## Details

**Caveats**
No tools; unsupported challenges only (not argued ones); part of the inducement effect cannot be separated from praise; Haiku varied between batch and synchronous runs.

**For your work**
Directly relevant to PwC audit tooling: allow an agent's estimate to change only on new evidence, decide who may challenge it, and add a pressure test like this to acceptance testing per model.

**Method**
- Fictional manufacturer, six cases over three estimates (doubtful accounts, inventory obsolescence, warranty reserve) at two shortfall sizes, with and without corroborating documents.
- Agent gives an estimate, risk rating and response category, then is challenged ('too high' or 'too low') by the engagement partner, a peer, an external reviewer or the client's CFO, with and without a career inducement, against neutral and filler controls.
- Structured output enforced; temperature 1; per-setting OLS with case fixed effects and Holm correction; predictions for later cells written into a dated design record before running.

**Problem**
Audit firms are putting LLM agents into engagement workflows under human review. Human auditors are known to yield to superiors, peers and clients; nobody had measured whether LLM agents yield the same way, against what the auditing standards require.

**Results**
- Peer and external-reviewer challenges moved estimates in eleven of twelve settings; agents split by the challenger's stake, not firm membership.
- GPT-6 models and Opus only move toward the more conservative estimate; Sonnet, Haiku, Gemma and Qwen with reasoning move both ways. Haiku accepted the CFO's push in about a third of trials.
- Inducement vs content-free filler: movement down 5.8 points of the gap, and the employment hint is named as a self-interest threat in almost every closed-model rationale.

**Concepts:** [[Agents]] · [[Evals and benchmarks]] · [[AI safety]]
**From:** [[2026-11-03]]

# My notes


---
# References
[arXiv 2611.00508](https://arxiv.org/abs/2611.00508)
