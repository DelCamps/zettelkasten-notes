---
date: 2026-10-24
section: AI
importance: Low
kind: paper
source: "arXiv 2610.30934"
url: https://arxiv.org/abs/2610.30934
status: unread
id: 2026-10-24-nla-activation-diffs
---
2026-10-24 07:16
Tags: #daily-knowledge #ai

---
# Natural-language autoencoders can read out what a finetune changed

Verbalising activation differences with NLAs recovers hidden secret words in most 'taboo' model organisms and even the finetuning objective without generating any tokens, and an NLA transfers to lightweight finetunes without retraining. It still trails state-of-the-art model-diffing methods on emergent misalignment but beats a black-box baseline.

## Details

**Problem**
Natural-language autoencoders (NLAs) translate a model's internal activations into text. This paper tests whether they can also explain what a finetune changed (model diffing), which they were never trained to do.

**Method**
- Used the released NLAs for Qwen2.5-7B, Gemma-3-12B/27B and Llama-3.3-70B, and fed them activation differences instead of single activations.
- Tested whether verbalisations follow word-analogy arithmetic, and whether an NLA trained on the original model still reconstructs activations from its finetunes.
- Diffed 'Taboo' organisms (finetuned to hide a secret word) and three emergent-misalignment finetunes against their original models using neutral prompts, then further trained the NLA with GRPO on activation differences.

**Results**
- On analogies the target word appeared in 80-87% of verbalisations, and the subtracted word was almost never mentioned.
- The secret word was recovered for most Taboo organisms, mostly from chat-template and system-prompt positions, so the finetuned model did not need to generate any text. Reuse without retraining worked except on Llama-3.3-70B and Qwen2.5-Coder.
- GRPO training raised the held-out secret-word mention rate from 9.2% to 35.8% on Qwen (5.9% to 10.0% on Gemma). On emergent misalignment, NLAs trailed ADL, came within 0.5 grade points of Activation Oracles, and beat a black-box agent.

**Caveats**
Scoring by word matching misses paraphrases. The model organisms have narrow, known objectives. Some words such as 'book' and 'song' show up regardless of the finetune. RL training was tried only on the two smallest models.

**For your work**
Little direct use

**Concepts:** [[Interpretability]] · Model diffing
**From:** [[2026-10-24]]

# My notes


---
# References
[arXiv 2610.30934](https://arxiv.org/abs/2610.30934)
