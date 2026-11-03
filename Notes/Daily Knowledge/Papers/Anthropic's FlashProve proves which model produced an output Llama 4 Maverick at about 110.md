---
date: 2026-11-03
section: AI
importance: Med
kind: paper
source: "Anthropic research"
url: https://www.anthropic.com/research/provable-inference
status: unread
id: 2026-11-03-flashprove-provable-inference
---
2026-11-03 07:16
Tags: #daily-knowledge #ai

---
# Anthropic's FlashProve proves which model produced an output Llama 4 Maverick at about 110

Anthropic's Frontier Red Team, with EPFL and MIT, built FlashProve, a zkSNARK system that lets a provider prove the committed model produced given output tokens. On Llama 4 Maverick it proves around 110 tokens/second on a single H100, about 70-95x the per-GPU cost of vLLM, and a CPU checks a proof in 17 seconds; on one machine, earlier published systems reached about 2.9 tok/s or less, and VerInf about 0.02 tok/s on the same model. Tested on: one model only (Llama 4 Maverick, 4-bit public weights, greedy decoding, 1,024-token context), research prototype.

## Details

**Caveats**
Prototype: the Lean protocol, paper and fast code are not guaranteed to match, and the C++ verifier has no formal guarantee. Proofs cover exact integer weights under greedy decoding only, a 1,024-token context and MoE models; sampled or floating-point outputs may diverge. Side channels are out of scope, and proving adds delay. Only one model was tested.

**For your work**
This is the cryptographic answer to 'is my provider quietly swapping models?', a question regulated clients ask. At 70-95x cost it suits audits and spot checks, not every call. It is worth knowing as a future assurance offering next to model-swap detection from outputs.

**Method**
- zkSNARK built from an interactive oracle proof compiled with hash functions (post-quantum).
- Offline: the provider publishes a commitment to the weights (about 39 minutes, once per model). Online: it proves 'the committed model produces these output tokens'.
- Speed tricks: prove only the active MoE experts per token, batch requests after the fact, and stream weights segment by segment so one 80 GB GPU is enough.
- Completeness, soundness and zero-knowledge stated in Lean; code released under Apache 2.0.

**Problem**
Users of a hosted model cannot check that the response really came from the model the provider claims to serve, rather than a cheaper substitute or a tampered output. Provable inference would help with compliance, tamper detection, text provenance and model approval.

**Results**
- Prover: around 110 tokens/second on one H100 with 24 CPU cores; a batch of 24 requests took about 223 seconds; each proof is 18.78 MB.
- Overhead vs vLLM FP8 on eight H100s: about 72x per GPU (66-77 across runs), about 94x at the highest load.
- Verifier: 6.5 MB commitment, 17 seconds to check on 24 threads, 21 seconds on one.
- Prior work: zkLLM about 2.5 tok/s on LLaMA-2-13B; VerInf about 0.02 tok/s on the same Maverick model with a 93.6 GB proof.

**Concepts:** [[AI safety]] · [[Open-weight models]] · [[Inference efficiency]]
**From:** [[2026-11-03]]

# My notes


---
# References
[Anthropic research](https://www.anthropic.com/research/provable-inference)
