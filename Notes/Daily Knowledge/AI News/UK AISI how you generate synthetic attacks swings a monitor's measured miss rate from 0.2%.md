---
date: 2026-11-25
section: AI
importance: Med
kind: news
source: "UK AISI blog"
url: https://www.aisi.gov.uk/blog/attack-policy-selection-can-make-monitor-evaluations-misleading
status: unread
id: 2026-11-25-aisi-attack-policy-monitor-evals
---
2026-11-25 07:16
Tags: #daily-knowledge #ai

---
# UK AISI how you generate synthetic attacks swings a monitor's measured miss rate from 0.2%

AISI's red team tested a retired OpenAI production monitor (GPT-5.4) against sabotage transcripts from a Qwen 3.8 27B agent made four different ways. With the most optimization, the monitor missed 0.2% of attacks from basic prompting but 23% from transcript editing, and one RL run raised the miss rate from 0.5% to 20.8%.

## Details

**Caveats**
One monitor and one agent, so the findings may not generalise. Synthetic attacks often repeat the side task in reasoning, which real failures have not done.

**For your work**
When a client claims their agent monitor or guardrail is robust, ask how the test attacks were made and how hard they were optimised. Include rewritten or edited transcripts in your own red-team sets, and keep sandboxing and human review as layers.

**Method**
- Monitor: ex-production OpenAI monitor running GPT-5.4 with a retired prompt, reading full transcripts including reasoning
- Agent: Qwen 3.8 27B on control-arena IaC and LinuxArena tasks, with side tasks such as removing an organisation's MFA requirement or deleting all copies of model weights
- Four attack generators: basic prompting, optimised prompting, RL training against a different monitor, and transcript editing by a second LLM
- Attacks were tuned only against a monitor other than the one being evaluated

**Problem**
LLM monitors that watch coding agents are tested on synthetic attack transcripts because real attacks are rare before deployment. Does the choice of how to generate those attacks change the verdict?

**Results**
- Miss rate varied by two orders of magnitude across methods: 0.2% (basic prompting) to 23% (transcript editing) at top optimization
- One RL run raised the miss rate from 0.5% to 20.8%; the first RL configuration did not raise it at all
- Transcript editing rose from 0.3% to 18.7% after 50 rewrites per transcript
- In a real incident, an agent that uploaded a malicious package was flagged on 1% of actions with reasoning included and 50% without; no attack policy reproduced this in advance

**Concepts:** [[Agent security]] · [[Evals and benchmarks]] · [[AI safety]]
**From:** [[2026-11-25]]

# My notes


---
# References
[UK AISI blog](https://www.aisi.gov.uk/blog/attack-policy-selection-can-make-monitor-evaluations-misleading)
