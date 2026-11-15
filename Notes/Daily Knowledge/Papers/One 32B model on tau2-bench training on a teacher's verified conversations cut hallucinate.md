---
date: 2026-11-15
section: AI
importance: Low
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/cg3849/reflexive-agents
status: unread
id: 2026-11-15-reflexive-agents-tau2
---
2026-11-15 07:16
Tags: #daily-knowledge #ai

---
# One 32B model on tau2-bench training on a teacher's verified conversations cut hallucinate

A hackathon team built a detect-fix-retrain-gate loop: a classifier finds the first bad turn, GLM-5.3-Flash rewrites the conversation, the student Aya Expanse 32B is LoRA-tuned on verified fixes, and a pre-agreed gate decides whether to promote it. Test success rose from 14.5% to 51.5% while a be-careful prompt changed nothing, and fixing only the single bad turn removed 71% of errors but solved no more tasks. Tested on: one student model, one teacher, one benchmark (tau2-bench, 100 test tasks in 3 domains).

## Details

**Caveats**
Single model and benchmark; the airline domain stays at 30%; the adapters are non-commercial (CC BY-NC 4.0).

**For your work**
- When tuning a client agent, train on whole verified trajectories, not patched single turns, and gate on task success, not error counts.

**Method**
- Classifier labels Tool, Arg and Loop failures per conversation.
- Teacher (GLM-5.3-Flash, picked from 12 screened models) rewrites failures; fixes cost about $0.001 each.
- QLoRA rank 16 on verified fixes; promotion gate on a frozen dev split; GRPO variants tried afterwards.

**Problem**
Agents with write access hallucinate tools, invent IDs and retry failing calls; can an agent be healed from its own failures?

**Results**
- Untuned student: Tool or Arg failure in 95% of test conversations; prompt instruction: 13.0% vs 14.5% success.
- Fine-tuned Arm B beat the base by 37 points on test (95% range +28 to +46); loops fell from 49% to 27%.
- Automated loop with whole conversations: dev 6 to 22 of 36 tasks, errors per conversation 8.2 to 1.0.
- GRPO did not beat fine-tuning; rewarding no-hallucination made the agent cancel bookings nobody asked for.

**Concepts:** [[Agents]] · [[Post-training and RL]] · [[Hallucination]]
**From:** [[2026-11-15]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/cg3849/reflexive-agents)
