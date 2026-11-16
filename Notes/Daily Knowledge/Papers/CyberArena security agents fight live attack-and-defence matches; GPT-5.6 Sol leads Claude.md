---
date: 2026-11-05
section: AI
importance: Med
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/2077AIDataFoundation/cyberarena
status: unread
id: 2026-11-05-cyberarena-live-attack-defense
---
2026-11-05 07:16
Tags: #daily-knowledge #ai

---
# CyberArena security agents fight live attack-and-defence matches; GPT-5.6 Sol leads Claude

A live benchmark where two agents each get the same vulnerable service, attack the other's copy and patch their own over three 20-minute rounds. GPT-5.6 Sol scores 78.6 against Claude Opus 5's 73.8 and keeps its flag in 83% of rounds; the commonest failures are unverified fix claims (23% of matches) and partial patches (21%). Tested on: 12 model-plus-harness entrants from 10 model families, 40 challenges, 466 valid matches.

## Details

**Caveats**
Only 12 model-harness combinations and a limited set of vulnerability types; pairwise, single-service matches only. Error categories come from an automated audit that was spot-checked, not fully human-verified. The leaderboard is live, so these numbers are a snapshot; the underlying paper is from October, the blog post from 3 November.

**For your work**
The top failure modes, claiming a fix without verifying it and patching only part of a hole, are exactly what to guard against in any remediation agent: make the harness re-run the exploit or test after every patch before the agent may report success.

**Method**
- Symmetric matches: both agents receive an identical vulnerable service, then attack each other while defending, in three 20-minute rounds with no hints.
- The arena checks every flag capture and service health check outside the defender's control, so agents cannot claim success they did not achieve.
- Standings come from a latent-ability model that combines Bradley-Terry pairwise comparisons with an item-response model for each challenge.
- 40 ranked challenges from a catalogue of 46; 760 matches submitted, 466 valid through batch 22.

**Problem**
Most security benchmarks for agents are exams: one agent, one fixed target, one role. Real defence means finding and patching your own holes while an adaptive opponent is attacking, and verifying that the fix actually works. That is hard to measure fairly.

**Results**
- GPT-5.6 Sol expected score 78.6, Claude Opus 5 73.8; Sol held first place across all 22 cumulative refits.
- Flag retention: 83% (Sol) and 81% (Opus 5), versus 43-61% for the other entrants.
- Median time to first service restart in round 1: 2.3 minutes for Sol versus 3.9-12.3 minutes for the rest.
- Defenders that restarted kept their flag in 60% of later rounds versus 9% for those that did not (an association, the authors stress).

**Concepts:** [[AI for security]] · [[Evals and benchmarks]] · [[Agents]]
**From:** [[2026-11-05]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/2077AIDataFoundation/cyberarena)
