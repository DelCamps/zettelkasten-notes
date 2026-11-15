---
date: 2026-11-15
section: AI
importance: Low
kind: paper
source: "arXiv 2611.15223"
url: https://arxiv.org/abs/2611.15223
status: unread
id: 2026-11-15-guardscope-runtime-controls
---
2026-11-15 07:16
Tags: #daily-knowledge #ai

---
# guardscope (design analysis, 2 harnesses) an agent gateway checks only the tool-call path,

The authors list 15 routes by which an agent's action can take effect and 8 places to put a runtime control, then check against kernel-level eBPF ground truth what each placement actually sees. A gateway in front of the harness (as with Microsoft's Agent Governance Toolkit) checks one path, harness-native permissions five, and kernel-level control 13 of 15, so no single control gives both coverage and semantic inspection. Tested on: Pi and OpenClaw harnesses, real controls (Microsoft AGT's agent-os-kernel, agentgateway, ActPlane), a replayed workload covering 4 of the 15 paths.

## Details

**Caveats**
Mostly a design analysis: only 4 of 15 paths were exercised in runs. It measures coverage, not whether policies are right, and kernel records carry no payload content.

**For your work**
- In agent governance assessments, ask which execution paths the gateway or Foundry/Agent 365 control actually sees, and add OS-level monitoring or forced egress for agents with shell access

**Method**
- Enumerate 15 action paths and 8 topology designs (gateway variants, harness-native, in-process, kernel) and derive which design checks which path
- Static stage: predict a control's checkable paths from its source
- Empirical stage: replay a fixed 15-action workload with no LLM in the loop and reconcile the control's decision records with Tracee eBPF records as checked, bypassed or prevented

**Problem**
Enterprises put gateways and guardrails around agents, but a control only checks actions that cross its position; agents can also spawn local tool servers, run shell commands or open network connections directly.

**Results**
- Plain gateway (T1) checks one path; harness-native (T4) five; kernel-level (T7) 13 of 15 unconditionally
- Five paths bypass every design below the kernel, so stacking gateways and harness checks adds detail but not coverage
- Forced-egress gateway setups prevent direct network actions; most deployed products surveyed sit in the narrow gateway designs
- Recommendation: combine harness-native enforcement with kernel-level monitoring

**Concepts:** [[Agent security]] · [[Agents]]
**From:** [[2026-11-15]]

# My notes


---
# References
[arXiv 2611.15223](https://arxiv.org/abs/2611.15223)
