---
date: 2026-11-07
section: AI
importance: Low
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/allenai/toyblocks
status: unread
id: 2026-11-07-ai2-toyblocks
---
2026-11-07 07:16
Tags: #daily-knowledge #ai

---
# Ai2 ToyBlocks (one tabletop block world) skill descriptions a Claude agent learned from it

Ai2 released ToyBlocks, a simulated robot arm and blocks world with 85,336 demonstrations, for testing robot policies, planners and world models. A Claude Opus 5.5 agent solved 30 out of 30 planning tasks, and descriptions of skills it wrote after testing them itself raised search-and-spell success from 24% to 63%, versus 36% with descriptions from a human expert. Tested on: one simulated tabletop block domain, three robot policies, three world models, and 30 real-robot trials.

## Details

**Caveats**
Single tabletop domain. Real-world results rest on 30 trials, which the authors say is not enough for statistical confidence. Skills use simulator state not available on real robots.

**For your work**
The robotics is out of scope, but the agent result transfers: letting an agent probe its tools and rewrite their descriptions beat expert-written descriptions here. Worth trying for MCP tool descriptions.

**Method**
- RL-trained push and flip skills in Isaac Lab, sequenced by a task-and-motion planner into long demonstrations
- Tests low-level policies (ManiFlow, π0.5, MolmoAct 2), a Molmo 2 planner, a Claude agent calling skills through MCP, and three world models
- The agent runs its own experiments and rewrites skill descriptions based on what it finds

**Problem**
Robot demos rarely show what a system learned or why it fails. Ai2 wants a controlled world where policies, planners and world models can be compared.

**Results**
- Agent: 30 out of 30 block-stacking tasks, including in a closed loop with camera images
- Learned skill descriptions: 63% vs 24% default and 36% expert-written; perception errors on look-alike letters (13%) and orientation (15%)
- Adding 100 rollouts from the best video model raised a policy's success in an unseen region from 19% to 78%
- Sim-to-real: ManiFlow 80.0% in simulation vs 81.1% real; Molmo 2 + ManiFlow 55.5% vs 50.0%

**Concepts:** [[Agents]] · [[Evals and benchmarks]]
**From:** [[2026-11-07]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/allenai/toyblocks)
