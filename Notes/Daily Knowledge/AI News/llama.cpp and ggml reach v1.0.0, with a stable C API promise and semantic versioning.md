---
date: 2026-11-14
section: AI
importance: Med
kind: news
source: "Hugging Face blog"
url: https://huggingface.co/blog/ggml-org/llama-cpp-v1
status: unread
id: 2026-11-14-llamacpp-v1
---
2026-11-14 07:16
Tags: #daily-knowledge #ai

---
# llama.cpp and ggml reach v1.0.0, with a stable C API promise and semantic versioning

After 3.5 years, llama.cpp and its ggml tensor library released v1.0.0; future major versions will signal breaking API or ABI changes. The project says it supports more than 150 model architecture variants and all mainstream speculative decoding methods.

## Details

**Caveats**
A versioning milestone, not a performance release; no benchmark figures were given.

**For your work**
For on-premises or air-gapped client deployments, pin llama.cpp to a 1.x release, upgrade minor versions freely for new model support, and treat a major bump as a planned migration with regression tests.

**Method**
- libllama and libggml both tagged v1.0.0, each with its own public headers
- Semantic versioning: MAJOR for breaking changes to the public C API in ./include, MINOR for compatible features, backends and model support, PATCH for bug fixes
- Distribution through pre-release artifacts, Docker, Debian, Homebrew, conda-forge, MacPorts, Winget and XCFramework
- CI scaled with HF Buckets and HF Jobs, with hardware support from NVIDIA, AMD, Qualcomm, Arm, IBM and Intel

**Problem**
Many local-AI apps build on llama.cpp, but its interfaces changed often, making upgrades risky for downstream products.

**Results**
- More than 150 architecture variants supported, plus all mainstream speculative decoding methods
- ggml backends can be built as dynamic libraries and loaded at runtime, so one build can target many kinds of hardware
- Future major-version bumps will make API and ABI breaks visible to downstream consumers

**Concepts:** [[Open-weight models]] · [[Inference efficiency]]
**From:** [[2026-11-14]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/ggml-org/llama-cpp-v1)
