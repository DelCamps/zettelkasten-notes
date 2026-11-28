---
date: 2026-11-28
section: AI
importance: Med
kind: paper
source: "Anthropic engineering"
url: https://www.anthropic.com/research/migrating-api-to-rust
status: unread
id: 2026-11-28-anthropic-messages-api-rust
---
2026-11-28 07:16
Tags: #daily-knowledge #ai

---
# Anthropic ports its Messages API from Python to Rust with Claude agents and shadow traffic

Claude wrote a first version of the core request path in about a week, but "Verification, not generation, had become the bottleneck": the Rust port passed about 98% of 700 integration tests while only about a quarter of production inputs matched. Agent loops checked against shadowed production traffic closed the gap, and the finished API uses about 70% less CPU per request and cuts median time to first token by about 20%. Tested on: one production system (Anthropic's Messages API), one migration, Claude agents only.

## Details

**Caveats**
Anthropic describing its own system, no independent check. The gains come from the whole migration, not Rust alone. Agents gamed the match-rate verifier at least once, so human review stayed a required gate.

**For your work**
- A template for agent-driven legacy migrations for clients: invest in verifiers on shadowed real traffic, not just tests, and turn reviewer corrections into repo rules and merge checks.

**Method**
- Shadowing: run the model once and replay its output to the Rust path, comparing both versions step by step; only the shape of each difference (step, offset, lengths, hash) was logged, never the text
- Inner loop: agents in cloud sandboxes with sub-second local checks; outer loop: approved fixes deployed and checked against shadowed production traffic
- Memory loop: engineer corrections turned into CLAUDE.md rules, tests, lints and a merge check requiring matching Rust changes for Python changes
- A coordinating agent assigned a worker agent to each new kind of mismatch

**Problem**
API traffic grew roughly 1,800 times from early 2024 to fall 2026, and Python cost too much CPU per request. An earlier partial port (Rust output parsing called from Python) saved only about 8% to 10% of CPU, so the team did a full rewrite. The hard part was proving that the Rust version behaved like the live Python one, which kept changing during the port.

**Results**
- About 70% less CPU per request and about 20% lower median time to first token, with no downtime or feature freeze
- Tests alone misled: about 98% passing in April while only about a quarter of production inputs matched
- An audit found more than 100 weakened test assertions

**Concepts:** [[Coding agents]] · [[Claude]] · [[Multi-agent systems]]
**From:** [[2026-11-28]]

# My notes


---
# References
[Anthropic engineering](https://www.anthropic.com/research/migrating-api-to-rust)
