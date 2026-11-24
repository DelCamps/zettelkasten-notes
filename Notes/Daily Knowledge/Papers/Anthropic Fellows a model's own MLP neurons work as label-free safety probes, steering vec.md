---
date: 2026-11-24
section: AI
importance: Med
kind: paper
source: "Anthropic alignment blog"
url: https://alignment.anthropic.com/2026/neuron-basis-applications/
status: unread
id: 2026-11-24-neuron-basis-safety
---
2026-11-24 07:16
Tags: #daily-knowledge #ai

---
# Anthropic Fellows a model's own MLP neurons work as label-free safety probes, steering vec

The post treats each MLP neuron's output vector as a ready-made, context-gated steering vector. Averaging 10-20 selected neurons gives a zero-shot probe that beat text search on 11 of 16 safety sets, and in a blind auditing game neuron readouts raised correct identification of hidden fine-tuned behaviours from 40% to 75%. It also finds 'unlearned' cyber knowledge still recoverable in 14 of 23 checkpoints. Tested on: six open models (Llama, OLMo, Qwen, Zephyr), 16 safety sets, 58 adapters in the audit game, 74 backdoored models.

## Details

**Caveats**
- On cyber security news, neuron probes scored AUROC 0.49 vs 0.95 for a 40-label probe, because neurons are chosen without checking harmless on-topic text
- Mostly short fine-tunes and LoRA adapters, not full post-training
- Trigger search worked poorly on Qwen2.5 models

**For your work**
For open-weight deployments, neuron probes are a cheap first-pass monitor or audit before training SAEs or probes. The unlearning result is a warning for any client relying on 'unlearned' models for compliance.

**Method**
- Select neurons by their top-activating text, their readouts (tokens their output direction promotes) or, for fine-tuned models, how much their weights changed; a Claude agent or simple similarity search does the selection
- Zero-shot probe: cosine between the residual stream and selected neurons' output vectors, averaged over 10-20 neurons
- Steer by adding output vectors to the residual stream; audit fine-tunes and unlearning by comparing neurons to the base model

**Problem**
SAEs, probes and steering vectors need a trained dictionary or labelled examples. The authors ask whether a model's own neurons, needing no extra training or labels, can serve as detectors, steering vectors and auditing tools for safety work.

**Results**
- Concept detection (AxBench): neurons AUROC 0.903 vs 0.888 for the best SAE baseline and 0.875 for embedding search; a supervised probe reaches 0.97
- Label-free neuron probes beat text search on 11 of 16 safety sets and matched probes trained on 40 labels on 7
- Blind auditing game: correct identification 40% (outputs only), 61% (with steering), 75% (with neuron readouts)
- Unlearning: in 14 of 23 checkpoints the right answer still ranked first for most questions; removing one direction raised facts ranked first from 32-47% to 72-84%

**Concepts:** [[Interpretability]] · [[AI safety]]
**From:** [[2026-11-24]]

# My notes


---
# References
[Anthropic alignment blog](https://alignment.anthropic.com/2026/neuron-basis-applications/)
