---
date: 2026-10-31
section: AI
importance: Low
kind: paper
source: "Hugging Face blog (community)"
url: https://huggingface.co/blog/bytkim/llama-cpp-logprob-loss
status: unread
id: 2026-10-31-llama-cpp-logprob-loss
---
2026-10-31 07:16
Tags: #daily-knowledge #ai

---
# llama.cpp server (one model, 24,000 requests) silently dropped about a quarter of logprob

A community study found that llama-server attached token IDs and logprobs per released UTF-8 text chunk rather than per sampled token, so tokens inside a multi-token character lost their IDs or logprobs even though the text was correct. On emoji-heavy output 24.9% of probability records went missing, the bug dates to October 22, 2023, and PR #31244 fixes it with zero record defects in 12,000 patched responses. Tested on: Qwen3.5-9B only, one GPU, temperature 0, two endpoints, streaming and non-streaming, on a 1,500-prompt benchmark.

## Details

**Problem**
Pipelines that use llama-server logprobs or token IDs (confidence scores, classifiers, RL data, uncertainty checks) may have been working with silently incomplete or mislabeled records, with no visible symptom in the text.

**Method**
- Built MURPHY: 1,500 prompts (900 FLORES+ copy, 300 Belebele, 300 Unicode Emoji copy tasks).
- Ran baseline vs patched build across native /completion and chat endpoints, streaming and non-streaming, two repeats: 24,000 requests.
- git bisect over 945 commits to find the introducing commit.

**Results**
- Emoji tasks: native and chat non-streaming each omitted 24.9% of probability records; chat streaming omitted 25.6%.
- Every endpoint and mode mislabeled selected-token bytes on 14.0% of records.
- Patched build: zero record defects in all 12,000 of its responses; instruction-following scores unchanged.

**Caveats**
One model and one configuration; no independent reference for logprob values (shows missing/mislabeled records, not wrong numbers); /v1/completions not in the main run; stop strings, speculative decoding and tool-call parsing untested.

**For your work**
If any client pipeline reads logprobs or token IDs from llama-server on non-English or emoji text, re-collect after updating to a build with PR #31244, and add a record-count check per response.

**Concepts:** [[Inference efficiency]] · [[Open-weight models]]
**From:** [[2026-10-31]]

# My notes


---
# References
[Hugging Face blog (community)](https://huggingface.co/blog/bytkim/llama-cpp-logprob-loss)
