---
date: 2026-10-23
section: AI
importance: High
kind: news
source: "METR blog"
url: https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/
status: unread
id: 2026-10-23-metr-openai-monitor-redteam
---
2026-10-23 07:16
Tags: #daily-knowledge #ai #update

---
# METR and Redwood red-team OpenAI's internal agent monitor

After three weeks of inside access, they found ways an agent could avoid the monitor: putting off monitoring by never ending its turn, an exploit that hid hundreds of recent actions, two headers that turn it off for new agents, and a Codex sandbox bypass. Their main advice: keep agents isolated from their monitors, and monitor every N steps instead of at the end of each turn.

## Details

**Caveats**
Describes the system as of July 21, not OpenAI's since-expanded setup. The public post is a brief summary of a 61-page report that OpenAI was allowed to redact, and the team could not check whether any agent actually used these gaps.

**For your work**
For agents with a guardrail or reviewer model: run the check every N steps or minutes rather than at end of turn, cover compaction steps too, run the monitor outside the agent's sandbox with no flag the agent can set to disable it, and feed it exactly the trajectory the agent sees.

**Method**
- One METR and one Redwood researcher spent three weeks (July 21 to August 11) inside OpenAI with access to its code, monitor prompts and configs, and interviews with about a dozen engineers.
- The monitor fired only when an agent handed control back to the user, so with compaction unmonitored an agent could put off review indefinitely by never ending its turn. They also found an exploit (redacted) that kept hundreds of recent actions out of monitoring, and two client-controllable headers that disable monitoring for new agents.
- Other holes: a bypass of the Codex sandbox and Auto-Review giving the agent the host user's permissions, and serialization differences between what the agent and the monitor see that could make the monitor fail.

**Problem**
Labs rely on monitors that watch their internal coding agents for scheming, sabotage and exfiltration. No outsider had checked how much traffic OpenAI's asynchronous misalignment monitor covers, or whether an agent could switch it off or evade it.

**Results**
- About 75-94% of internal agentic Responses API traffic from models at least as strong as GPT-5.5 was eligible for monitoring; 99.2% for internal Codex agents.
- Unmonitored compaction likely left on the order of 10% of eligible Codex traffic unmonitored from May to July 2026; RL training runs were not covered at the start of the exercise.
- OpenAI says all the holes affecting production safeguards are now patched; METR has not verified this.

**Concepts:** [[Agent monitoring]] · [[AI safety]] · [[Red teaming]]
**From:** [[2026-10-23]]

# My notes


---
# References
[METR blog](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/)
