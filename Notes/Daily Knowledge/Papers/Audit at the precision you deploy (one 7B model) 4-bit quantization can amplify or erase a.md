---
date: 2026-11-03
section: AI
importance: Low
kind: paper
source: "arXiv 2611.00665"
url: https://arxiv.org/abs/2611.00665
status: unread
id: 2026-11-03-quantization-subliminal
---
2026-11-03 07:16
Tags: #daily-knowledge #ai

---
# Audit at the precision you deploy (one 7B model) 4-bit quantization can amplify or erase a

A hidden 'favourite animal: panda' preference implanted subliminally into Qwen2.5-7B-Instruct is stable at 8 bits, but at 4 bits HQQ amplifies it (net strength ~1.3 times its 16-bit value) while NF4 suppresses it (~0.3 times), despite rounding errors of the same size to within 4%. An explicitly trained preference of matched strength stays within 0.98-1.19 across the same conditions. Tested on: one model (Qwen2.5-7B-Instruct), two training seeds, two quantizers.

## Details

**Caveats**
One model, one benign toy trait, two seeds; training method and weight-update size are confounded.

**For your work**
When certifying a model for a client, run safety and behaviour evals on the exact quantized build you ship, not the 16-bit checkpoint.

**Method**
- Subliminal students fine-tuned with LoRA on number sequences from a panda-preferring teacher, plus neutral controls and explicitly trained students, two seeds each.
- Merged weights quantized with HQQ (8, 4, 3, 2 bits) and NF4; net strength = student minus control panda probability under the same setting.
- Error interventions: HQQ's own 4-bit error added unchanged, negated or shuffled within groups of 64 weights.

**Problem**
Safety audits usually evaluate models at 16-bit precision, but deployments often run quantized weights. If quantization changes how a hidden trait is expressed, the audit may not describe the deployed model.

**Results**
- At 4 bits HQQ raises subliminal students to 61-67% panda vs NF4's 28-30%; controls stay near 17%.
- Shuffling the error without changing magnitudes moves net strength between 0.2 and 1.6 times the 16-bit value.
- Explicit preference is roughly five times less sensitive to quantizer choice and never amplified.

**Concepts:** [[AI safety]] · [[Inference efficiency]] · [[Interpretability]]
**From:** [[2026-11-03]]

# My notes


---
# References
[arXiv 2611.00665](https://arxiv.org/abs/2611.00665)
