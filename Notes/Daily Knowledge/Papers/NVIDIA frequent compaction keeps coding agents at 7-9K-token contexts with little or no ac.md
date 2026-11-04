---
date: 2026-11-04
section: AI
importance: High
kind: paper
source: "arXiv 2611.05306"
url: https://arxiv.org/abs/2611.05306
status: unread
id: 2026-11-04-you-dont-need-long-context
---
2026-11-04 07:16
Tags: #daily-knowledge #ai

---
# NVIDIA frequent compaction keeps coding agents at 7-9K-token contexts with little or no ac

Serving at a 256K rather than 16K context window costs 3.6x to 7x more per generated token on GLM 5.2, Kimi K2.6 and Qwen 3 Coder Next. Compacting often, Claude Opus 4.5 rose from 70.0% to 74.8% on SWE-bench Verified and GPT 5.6 Sol from 84.4% to 88.8%; even one action per context kept median peak context at 7-9K tokens with small losses. Tested on: 2 closed models (Opus 4.5, GPT 5.6 Sol) plus 5 open-weight models, 6 long-horizon and 7 long-input benchmarks, mini-swe-agent-based harnesses.

## Details

**Caveats**
Nominal API cost does not always fall (GPT 5.6 Sol cost more with compaction); the large savings are 'estimated optimized' costs from a context-cost factor. Robustness is model-specific and tight budgets hurt verbose models. Results are single accuracy figures without confidence intervals.

**For your work**
Add structured compaction (task copy, current state, dead ends, next steps) and file-based selective reading to client agent harnesses, then sweep the compaction threshold per model before choosing long-context tiers.

**Method**
- Full-History Accumulation baseline vs End-of-Conversation Compaction at shrinking context limits (48K/36K down to 16K/12K) vs Single-Action Compaction (one action per context)
- Long inputs read selectively with Bash tools from the filesystem instead of being pasted whole
- Compaction prompt keeps a near-verbatim task copy, current activity, dead ends and remaining plan: a brief for future work, not a narrative
- Measured decode throughput on H100 nodes to price context length

**Problem**
Agent harnesses usually append every command, tool output and decision to an ever-growing history, but later tokens are more expensive to generate. Is long context actually needed for long-horizon or long-input tasks?

**Results**
- SWE-bench Verified: Opus 4.5 74.8% at 24K/18K (baseline 70.0%), nominal cost $295.75 vs $420.00; GPT 5.6 Sol 88.8% at 48K/36K (baseline 84.4%)
- Single-action compaction: Opus 70.2% SWE-bench, 51.8% Terminal-Bench (baseline 47.2%); GPT 82.4% and 84.3%, 2.0 and 3.3 points below baseline; max context falls from 130-200K to 15-37K
- Open-weight models vary: Qwen 3.6 27B and MiniMax M2.7 robust, Qwen 3 Coder Next collapses from 53.0% to 3.6% at 16K/12K

**Concepts:** [[Coding agents]] · [[Inference efficiency]] · [[Agent memory]]
**From:** [[2026-11-04]]

# My notes


---
# References
[arXiv 2611.05306](https://arxiv.org/abs/2611.05306)
