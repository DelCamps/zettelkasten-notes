---
date: 2026-10-23
section: AI
importance: Med
kind: news
source: "Anthropic research"
url: https://www.anthropic.com/research/formal-verification
status: unread
id: 2026-10-23-anthropic-formal-verification
---
2026-10-23 07:16
Tags: #daily-knowledge #ai

---
# Anthropic Claude formally verifies 123 open-source libraries

Claude wrote machine-checked Rocq proofs that 239 OSS-Fuzz entry points can't crash on any input under 64 MB, working on compiled RISC-V binaries (about 180M lines of proof). Along the way it found hundreds of bugs fuzzers would likely miss, including a logic bug latent for over a decade. Caveat: the proofs assume static musl binaries.

## Details

**Caveats**
The proofs assume single-threaded static RISC-V binaries linked against musl, whereas most deployments are x86/ARM with glibc. ASan misses some memory bugs, not every entry point was covered, and proofs cost hundreds of millions of tokens.

**For your work**
Little direct use for most LLM-app work today. If a client ships C/C++ parsers or other security-critical libraries, Theorem's published Claude skill and pipeline are worth trying, and the 'convert existing tests into a spec, then let the agent iterate against a checker' loop carries over to agent workflows in general.

**Method**
- Turn OSS-Fuzz fuzz-test entry points into a spec: the compiled RISC-V binary never crashes, including AddressSanitizer memory-safety crashes, on any input under 64 MB.
- Claude writes Rocq proofs against Theorem's RISC-V and Linux-process semantics. When a bug blocks a proof, Claude patches it and proves the regenerated spec.
- Trust rests only on the RISC-V/Linux models, the theorem statements and the Rocq checker, so the proofs themselves need no human review.

**Problem**
AI makes finding and exploiting bugs cheap, but formal verification, which can prove code is free of whole classes of bugs, has needed years of expert effort (seL4 took 20 person-years to verify). Anthropic and Theorem tested whether Claude can write such proofs at scale for real production code.

**Results**
- Proofs for 239 entry points across 123 libraries in a few weeks: about 180M lines of Rocq, typically about 600,000 lines per proof, for binaries with a median of 18,000 RISC-V instructions.
- Hundreds of bugs found, including one needing a ~20 MB input and another needing a 64 MB input and over 2 GB of memory, plus a logic bug that had been latent for over a decade.
- Opus 5.5 proved half of 36 small tasks with about 40% fewer tokens than Opus 5; sharing proofs between agents cut tokens by 17%.

**Concepts:** Formal verification · [[AI for security]] · [[Coding agents]]
**From:** [[2026-10-23]]

# My notes


---
# References
[Anthropic research](https://www.anthropic.com/research/formal-verification)
