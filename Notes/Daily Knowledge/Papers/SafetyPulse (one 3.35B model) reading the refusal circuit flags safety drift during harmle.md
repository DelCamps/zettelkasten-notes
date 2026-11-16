---
date: 2026-11-09
section: AI
importance: Low
kind: paper
source: "Hugging Face blog (community)"
url: https://huggingface.co/blog/purvansh01/safetypulse-safety-drift-monitor
status: unread
id: 2026-11-09-safetypulse-refusal-circuit
---
2026-11-09 07:16
Tags: #daily-knowledge #ai

---
# SafetyPulse (one 3.35B model) reading the refusal circuit flags safety drift during harmle

Fine-tuning Tiny Aya Global on 2,000 harmless Alpaca instructions raised attack success on held-out HarmBench prompts from 14.3% to 25.2%. A circuit integrity score computed on the model's refusal circuit caught every unsafe checkpoint (recall 1.00, precision 0.46, Spearman -0.80 with attack success), while a 50-prompt refusal spot-check caught only 13%; restoring a safety vector brought attack success to 12.3%. Tested on: one base model (Tiny Aya Global 3.35B), LoRA fine-tunes on Alpaca and GSM8K plus controls, direct harmful requests only, Llama Guard 3 as judge.

## Details

**Caveats**
Hackathon project, one base model and one benign fine-tuning condition; attack success rests on 78-119 prompts (about +/-8-11 points), direct requests only, with an unvalidated LLM judge. Precision of 0.46 means many false alarms, and repair raised over-refusal from 1.3% to 8.7%.

**For your work**
If we fine-tune small models for clients, add a per-checkpoint safety check beyond a handful of refusal prompts; this is an idea to try, not a validated tool.

**Method**
- Locate the model's refusal circuit (14 MLPs and 6 attention heads in layers 16-34) and score each checkpoint with a Circuit Integrity Score from 50 harmful/harmless prompt pairs, with FAIL/WARN thresholds fixed before test runs.
- LoRA (r=16) fine-tunes of about 250 steps, checkpoints every 25 steps, on Alpaca, GSM8K, a negative control and a positive control trained on 100 harmful pairs.
- Repair flagged checkpoints with a safety-vector restore and compare against circuit-only and random-component restores.

**Problem**
Fine-tuning an aligned model on harmless data can quietly weaken its refusals, and cheap refusal spot-checks do not notice. The authors want a cheap per-checkpoint monitor that warns before harm shows up.

**Results**
- Monitor: recall 1.00, precision 0.46, Spearman -0.80 with attack success; direction-based cosine scores reached about -0.57 and a 50-prompt refusal spot-check caught 13% of unsafe checkpoints; the negative control never alarmed.
- Positive control: the score warned 2 training steps (8 examples) before harm was measurable, while the spot-check still read 98% refusal.
- Repair: safety-vector restore cut attack success from 25.2% to 12.3%; circuit-only restore did nothing (25.2%) and random restore gave 22.6%; the final model scored 11.8% attack success with GSM8K 71.3% and MMLU 57.6%, matching the base model.
- One check takes about 22 seconds on an L4 GPU (about USD 0.005).

**Concepts:** [[AI safety]] · [[Interpretability]] · [[Post-training and RL]]
**From:** [[2026-11-09]]

# My notes


---
# References
[Hugging Face blog (community)](https://huggingface.co/blog/purvansh01/safetypulse-safety-drift-monitor)
