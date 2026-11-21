---
date: 2026-11-21
section: AI
importance: High
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/harness-adapters-at-scale
status: unread
id: 2026-11-21-hf-harness-adapters
---
2026-11-21 07:16
Tags: #daily-knowledge #ai

---
# Harness adapters (Hugging Face, Qwen3.8-27B, three harnesses) RL inside the agent harness

Hugging Face trained one LoRA adapter per coding harness (Pi, OpenCode, Hermes Agent) with GRPO, running rollouts in the real harness; on the 51 hardest SWE-bench Pro tasks Pi went from 39.2% to 64.7% and on Terminal-Bench 2.1 the gains were +16.3 (Pi), +14.1 (Hermes) and +6.0 (OpenCode) points. A merged 'super-adapter' raised mean pass@1 from 39.5% to 49.0% across six harness-benchmark pairs. Tested on: one base model (Qwen3.8-27B), three harnesses, 51 SWE-bench Pro and 89 Terminal-Bench 2.1 tasks, one attempt each, plus 300 AutomationBench tasks for out-of-domain checks.

## Details

**Caveats**
Small task sets with one attempt per task; the merge weight was picked on Terminal-Bench 2.1, so those numbers are slightly optimistic. Some baselines in the text differ from the tables. Harness settings were left at defaults, so results compare only within a harness, and only one base model was tested.

**For your work**
If a client runs an open model inside a fixed agent harness, a cheap per-harness LoRA trained on verifiable tasks can raise success and halve tool calls. Worth considering for self-hosted coding or ops agents, but check gains on your own tasks before claiming them.

**Method**
- One LoRA per harness trained with GRPO (TRL AsyncGRPOTrainer); rollouts run in Pi, OpenCode or Hermes Agent via Harbor and OpenEnv, with a proxy recording exact tokens.
- Reward is verifier pass/fail plus a 0.1 tool-efficiency bonus; thinking is off during rollouts.
- Training used 2xB200 per adapter, 78,114 samples and 167M trained tokens.
- A 'super-adapter' concatenates the three LoRAs along rank and applies them at weight 1/2.

**Problem**
General models are not tuned for the specific harness and task mix an agent runs in, so success rate and token efficiency are left on the table. The team asked whether RL inside the target harness helps a 27B model on hard software tasks.

**Results**
- Hard SWE-bench Pro, Pi: 39.2% to 64.7% (15 tasks gained, 2 lost, p = 0.002).
- Terminal-Bench 2.1: +16.3 (Pi), +14.1 (Hermes), +6.0 (OpenCode) points; adapters use 53-70% fewer tool calls on shared solved tasks.
- Super-adapter: mean pass@1 39.5% to 49.0% (thinking off); 55.5% to 63.5% with thinking on.
- Out-of-domain AutomationBench: base 23.0%, Pi adapter 27.0%, Hermes adapter 17.7%; most differences within noise.

**Concepts:** [[Post-training and RL]] · [[Coding agents]] · [[Open-weight models]]
**From:** [[2026-11-21]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/harness-adapters-at-scale)
