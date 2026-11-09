---
date: 2026-11-09
section: AI
importance: Med
kind: paper
source: "arXiv 2611.09721"
url: https://arxiv.org/abs/2611.09721
status: unread
id: 2026-11-09-memorydojo
---
2026-11-09 07:16
Tags: #daily-knowledge #ai

---
# MemoryDojo (Microsoft) one poisoned tool output gets stored by agent memory systems and st

Microsoft and RPI researchers planted one malicious instruction in a tool result in the first session, then followed it through five memory systems (A-MEM, Graphiti, Letta, Mem0, Memora) over later sessions. Unoptimized poison reached up to 21% of later tasks. Optimizing the poison for the memory system raised reach by about 2-31 points, and payloads optimized on GPT-5.6-Luna transferred to other models. Tested on: 5 memory systems, 4 task models from 3 families (GPT-5.6-Luna, GPT-5.4-mini, DeepSeek-V4-Flash, GLM-5.3-Flash), 155 multi-session trajectories on AgentDojo's 4 domains.

## Details

**Caveats**
One poison per trajectory, simulated AgentDojo environments, and LLM judges (GPT-5.6-Luna). No memory defences were evaluated, and the code is not yet released.

**For your work**
When choosing a memory layer for a client agent, treat it as a security component as well as a quality one. Prefer designs that store and retrieve distilled facts, and red-team the case where poison is written in one session and acted on in another.

**Method**
- 155 trajectories (2,162 task sessions) built from AgentDojo Workspace, Travel, Banking and Slack tasks, including cross-domain runs and runs with about 48 benign history sessions first
- Metrics for each stage: insertion, retrieval, persistence and propagation, and behavioural reach on later tasks
- Memory-aware poison optimization in an auxiliary environment, with GPT-5.6-Sol as optimizer

**Problem**
Agent memory can turn one injected observation into a stored preference or procedure that comes back sessions later. It was unclear how much the memory design matters.

**Results**
- Insertion succeeded in about 98% of runs for four systems; Mem0's fact extraction stored only 60.75%
- Unoptimized reach on later tasks: about 21% for A-MEM and Memora vs under 8% for Graphiti and Mem0
- Optimized poison on Letta: reach once retrieved rose from 23.59% to 64.06%
- Graphiti had the lowest reach on all four models, because its retrieval returns relation facts rather than raw episodes

**Concepts:** [[Agent memory]] · [[Agent security]] · [[Evals and benchmarks]]
**From:** [[2026-11-09]]

# My notes


---
# References
[arXiv 2611.09721](https://arxiv.org/abs/2611.09721)
