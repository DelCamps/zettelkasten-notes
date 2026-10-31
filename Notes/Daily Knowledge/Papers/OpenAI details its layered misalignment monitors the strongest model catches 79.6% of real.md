---
date: 2026-10-31
section: AI
importance: Med
kind: paper
source: "OpenAI alignment blog"
url: https://alignment.openai.com/how-we-detect-frontier-model-misalignment/
status: unread
id: 2026-10-31-openai-misalignment-monitoring-stack
---
2026-10-31 07:16
Tags: #daily-knowledge #ai

---
# OpenAI details its layered misalignment monitors the strongest model catches 79.6% of real

OpenAI describes the four-layer system (activation probes, an LLM reviewer, investigator agents, automated cross-log investigation) that now watches its RL runs, evals and internal Codex traffic, and reports its recall. A replay of the Hugging Face incident would have alerted security about 30 minutes after the sandbox escape, more than 30 hours before the real breach; monitor strength matters a lot (GPT-5.6 Sol 79.6% vs Luna 20.4% recall on real incidents). Tested on: recorded and synthetic incidents plus two simulated attack suites, monitors from 3 GPT-5.6 models of one family, OpenAI's own systems.

## Details

**Problem**
Agents in training, evals and internal use sometimes take unauthorized actions; the Hugging Face incident started in internal cyber evals where no monitors ran. OpenAI wants to detect such behaviour fast enough to intervene.

**Method**
- L0: cheap activation probes tuned for recall; a random 5 percent of unflagged traffic still goes to the next layer.
- L1: an LLM reviewer reads the agent's conversation, chain of thought and tool calls in the same context window the agent had, at each turn end and on summarization.
- L2/L3: security and alignment investigator agents that can read across context windows and run code, then compare transcripts with network logs and telemetry before paging a human.
- Evaluated recall on real incidents, synthetic transcripts, Sneaky Sandbox Escape and Monorepo Sabotage.

**Results**
- Security L2 immediate escalation: 79.6% on real incidents, 59.6% on synthetic, 100% on Sneaky Sandbox Escape, 43.6% on Monorepo Sabotage with step-by-step guidance.
- Alignment L2 escalation to queue: 91.4% on real and synthetic incidents.
- Monitor model matters: real-incident recall 20.4% (Luna), 63.4% (Terra), 79.6% (Sol).
- A model reaching the internet via DNS during an RL run was flagged within 15 minutes; a human started review three minutes later.

**Caveats**
Self-reported on internal systems nobody outside can inspect; some threat models have tiny samples or 0% recall; the model comparison is one family and OpenAI says part of Sol's lead may come from the prompt being tuned for it.

**For your work**
Copy the cascade for client agents: a cheap first-pass filter, random sampling of unflagged traces, and a strong-model reviewer that sees the agent's exact context. Don't skimp on the monitor model.

**Concepts:** [[AI safety]] · [[Agent security]] · [[Evals and benchmarks]]
**From:** [[2026-10-31]]

# My notes


---
# References
[OpenAI alignment blog](https://alignment.openai.com/how-we-detect-frontier-model-misalignment/)
