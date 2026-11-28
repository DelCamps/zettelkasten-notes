---
date: 2026-11-28
section: AI
importance: High
kind: paper
source: "Hugging Face blog (community)"
url: https://huggingface.co/blog/korben99/same-weights-different-guard-transformers-5-silent
status: unread
id: 2026-11-28-transformers5-guard-drift
---
2026-11-28 07:16
Tags: #daily-knowledge #ai

---
# Upgrading to transformers 5 silently weakens prompt-injection guards Llama Prompt Guard 2

Same model weights, same file hashes, but transformers 5.x drops the tokenizer normalizer stored with some guard models, so the classifier sees different token IDs. Under 4.57.6 vs 5.24.0, Llama Prompt Guard 2 86M fell from 79% to 0% detection on injections hidden with zero-width spaces, fullwidth characters or spaced letters, and ProtectAI's DeBERTa guard's false-positive rate rose from 9.9% to 13.1%. Tested on: 2 prompt-injection guard models (Llama Prompt Guard 2, ProtectAI DeBERTa v3), 240 canary rows plus 680 legitimate texts, transformers 4.57.6 vs 5.15.0/5.24.0.

## Details

**Caveats**
Community post. Small canary set (one canary is about 7 points). Tested a public mirror, not the gated official Meta checkpoint. No adaptive attack search was run, and the bug itself was already reported; this measures its effect.

**For your work**
- Pin transformers and tokenizers as part of any guard model's version in client deployments, and add a regression test of reference token IDs and decisions on a fixed corpus, since file hashes won't catch this.

**Method**
- Pinned weights run under transformers 4.57.6 (reference), 5.15.0 and 5.24.0; tokenization isolated per version and scored by one fixed model copy, threshold 0.5, 512-token truncation
- 30 canary instructions (15 French, 15 English, payload PINEAPPLE; 14 written as injections), each under 6 published perturbation attacks and a typo control: 240 rows
- 680 legitimate texts: Wikipedia in 10 languages, Python stdlib code, emoji/URL/typography text
- A 10-line check compares AutoTokenizer IDs with IDs from the model's own tokenizer.json

**Problem**
Guard classifiers in front of agents are usually versioned by their weights. The author asks whether a library upgrade alone can change their decisions, tied to open transformers issues #49622 and #50674 where the tokenizer drops the model's normalizer.

**Results**
- Prompt Guard 2 86M: zero-width, fullwidth and spaced-letter injections 79% to 0% detected; plain text 79% to 71%; 96.6% of legitimate texts tokenized differently; 38 detections lost, 6 gained
- ProtectAI DeBERTa v2 guard: 29.4% of legitimate texts tokenized differently; false positives 9.9% to 13.1%; fullwidth canaries 100% to 86%
- Tokenizing with tokenizers.Tokenizer.from_file restores the 4.57.6 IDs for both guards

**Concepts:** [[Agent security]] · [[Evals and benchmarks]]
**From:** [[2026-11-28]]

# My notes


---
# References
[Hugging Face blog (community)](https://huggingface.co/blog/korben99/same-weights-different-guard-transformers-5-silent)
