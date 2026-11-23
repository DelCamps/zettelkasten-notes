---
date: 2026-11-23
section: AI
importance: Med
kind: paper
source: "Hugging Face blog (community)"
url: https://huggingface.co/blog/HatemSaadallah/weights-and-harness-are-complements-aemon-8b-a-str
status: unread
id: 2026-11-23-aemon-weights-harness-complements
---
2026-11-23 07:16
Tags: #daily-knowledge #ai

---
# aemon-8b fine-tuning Aya Expanse 8B on teacher runs lifts strategy investigations finished

A hackathon team distilled 3,891 Command A+ tool calls into Aya Expanse 8B for a guarded, 12-tool business-strategy agent. On 12 unseen companies it beat the same model with only prompting by +0.70 [0.61, 0.79] on a 0-3 blind-judge scale. Removing the decoding guards cost 0.43, and three data tricks that looked like gains at one training seed vanished over three seeds. Tested on: Aya Expanse 8B (prompted and fine-tuned), Tiny Aya 3.35B and Claude Haiku 5.5, judged blind by GPT-6 Sol (Codex) and Claude Opus 5.5 (Claude Code), 96 runs per arm.

## Details

**Caveats**
This is a hackathon entry with LLM judges, who agree only weakly on individual runs (Spearman 0.31-0.47). Every case is a B2B manufacturer strategy question. The adapter is non-commercial (CC-BY-NC-4.0).

**For your work**
Fine-tuning an open model doesn't replace the harness: keep the guards. Re-run any fine-tuning 'gain' over several seeds before trusting it, and check whether a cheap closed model already does better before pitching self-hosting.

**Method**
- 12 guarded tools: quotes must match their source word for word, theories must differ, and a simulated result can't count as evidence
- LoRA rank 16 on Aya Expanse 8B using AgentTune distillation on 3,891 teacher tool calls that replay exactly; test set of 12 new companies frozen before results were seen, 48 cases x 2 attempts
- Ablations of the guards, the prompt and the adapter; data variants repeated over three training seeds; all decision rules logged in advance

**Problem**
Asked a strategy question, LLMs write consulting prose with no rival theories, evidence or test. The team asks whether distilling a guarded investigation procedure into an open 8B model helps on companies it has never seen, and which parts of the agent matter.

**Results**
- Test set: quality 1.71 for the fine-tuned model against 1.01 prompted; finished 81 of 96 against 2 of 96; tool calls accepted 92.4% against 79.8%
- Removing resampling of repeated calls cost 0.49, all six decoding guards 0.43, and base weights in the late stages 0.19
- Rebalancing training rows toward rare skills cost 0.72 pooled over three seeds; two other additions that gained at seed 7 vanished
- Claude Haiku 5.5 led by +0.20 [0.05, 0.35] (+0.42 if 11 API-refusal runs are excluded) at $0.008 per investigation, against about $0.02 for the self-hosted 8B; MMLU/ARC held at 67.9% against 67.3%

**Concepts:** [[Agents]] · [[Post-training and RL]] · [[Evals and benchmarks]]
**From:** [[2026-11-23]]

# My notes


---
# References
[Hugging Face blog (community)](https://huggingface.co/blog/HatemSaadallah/weights-and-harness-are-complements-aemon-8b-a-str)
