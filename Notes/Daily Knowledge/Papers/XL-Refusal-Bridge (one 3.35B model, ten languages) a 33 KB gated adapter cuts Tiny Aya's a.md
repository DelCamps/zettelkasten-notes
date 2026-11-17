---
date: 2026-11-17
section: AI
importance: Low
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/davidquicast/xl-refusal-bridge-closing-tiny-aya-cross-lingual-s
status: unread
id: 2026-11-17-xl-refusal-bridge-tiny-aya
---
2026-11-17 07:16
Tags: #daily-knowledge #ai

---
# XL-Refusal-Bridge (one 3.35B model, ten languages) a 33 KB gated adapter cuts Tiny Aya's a

A Hugging Face community post finds Tiny Aya Global recognises harmful requests about equally well in every language, but its internal refusal signal is weaker in low-resource ones (Javanese about 46% of English strength). A 33 KB probe-plus-clamp adapter lifts refusal of harmful prompts from 69.9% to 95.6% while benign over-refusal rises from 6.0% to 8.2%. Tested on: one model (Tiny Aya Global 3.35B), ten languages, MultiJail plus SORRY-Bench transfer, LLM judges only (Qwen2.5-7B, 72B re-check), no human labels.

## Details

**Caveats**
Hackathon entry; one model, direct requests only (no adversarial jailbreaks), judge agreement modest (kappa about 0.4), no human annotation. XSTest over-refusal rises from 17.6% to 24.4%, and English refusal also rises (69% to 93%), so it hardens the model generally.

**For your work**
A cheap pattern for clients shipping small open models in non-English markets: probe-gated activation steering as a removable safety layer, measured per language against over-refusal.

**Method**
- Ten languages from English to Swahili and Javanese; harmful prompts from MultiJail, benign from Alpaca, 'safe but alarming' from XSTest; SORRY-Bench held out.
- A linear probe at layer 20 detects harmful intent; when it fires, a gate clamps the refusal component at layers 25, 27 and 29 up to its English level.
- Responses judged by Qwen2.5-7B-Instruct, with a 72B re-check of all 25,220 test pairs.

**Problem**
Multilingual models are easier to misuse in low-resource languages. The author asks whether the gap is in detecting harm or in acting on it.

**Results**
- Macro attack success rate 5.4% to 0.1%; worst-language gap vs English 9.3 pp to 0.7 pp.
- Belebele accuracy unchanged at 75.6%; throughput 284 vs 283 tokens/s.
- Baseline SafeTune steering reached 1.7% ASR and 77.9% refusal; SafeTune CAST reached 0.9% ASR but refused 99.6% of benign prompts.
- Removing the gate pushed benign over-refusal to 87%; on six unseen SORRY-Bench languages ASR fell from 9.0% to 1.3%.

**Concepts:** [[AI safety]] · [[Interpretability]] · [[Open-weight models]]
**From:** [[2026-11-17]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/davidquicast/xl-refusal-bridge-closing-tiny-aya-cross-lingual-s)
