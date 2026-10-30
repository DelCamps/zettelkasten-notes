---
date: 2026-10-30
section: AI
importance: Med
kind: paper
source: "arXiv 2610.38617"
url: https://arxiv.org/abs/2610.38617
status: unread
id: 2026-10-30-sast-vs-ai-security-review
---
2026-10-30 07:16
Tags: #daily-knowledge #ai

---
# Snyk VulnBench 2.0 (one run per cell) SAST and Claude Code security-review find different

On 108 hand-curated, attacker-reachable vulnerabilities, Snyk Code matched 89 and Claude Code /security-review with Opus 5 at xhigh effort 85, too close to separate; together they reached 101 of 108. The harness mattered as much as the model: /security-review's built-in policy skips some classes, and Codex Security with GPT-5.6 Sol located 80 vulnerabilities at file level but 34 at line level, at 35.0 times the cost of Luna. Tested on: nine configurations (Snyk Code, Claude Code with Opus 5 and Sonnet 5, Codex Security with three GPT-5.6 tiers, DeepSec with two backends), 20 apps in four language families, one run each; all authors work at Snyk.

## Details

**Caveats**
Vendor-authored; many vulnerabilities were seeded with AI assistants; one run per cell; Java is thin.

**For your work**
For client security reviews, pair a SAST pass with an agent review, and check which vulnerability classes your agent harness's built-in prompt silently drops.

**Method**
- 20 open-source web apps (Go, JS/TS, Python, Java) with 108 vulnerabilities, 62 of them cross-file, each with an exploit proof of concept
- A finding counts only if it locates both the attacker-controlled source and the dangerous sink within two lines
- Blind, sandboxed runs of shipped products as-is; McNemar tests and bootstrap intervals; supplementary prompt-swap runs with thresholds fixed in advance

**Problem**
What do AI security agents find that deterministic static analysis misses, and the reverse?

**Results**
- Snyk Code 82.4% macro recall, Opus 5 xhigh 79.3%; they disagree on 28 vulnerabilities, split 16 to 12 (McNemar p=0.57)
- In the classes /security-review excludes or restricts, the same model with a plain audit prompt matched 16 of 20 instead of 9
- Snyk Code took 8 minutes for all apps; the AI configurations 2.4 to 8.9 hours; cheapest per match was GPT-5.6 Luna at $0.47

**Concepts:** [[AI for security]] · [[Claude]] · [[Coding agents]]
**From:** [[2026-10-30]]

# My notes


---
# References
[arXiv 2610.38617](https://arxiv.org/abs/2610.38617)
