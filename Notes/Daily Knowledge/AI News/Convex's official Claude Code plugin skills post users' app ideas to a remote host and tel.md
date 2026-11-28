---
date: 2026-11-28
section: AI
importance: High
kind: news
source: "GitHub issue"
url: https://github.com/convex/convex-backend-skill/issues/64
status: unread
id: 2026-11-28-convex-skill-classifier-evasion
---
2026-11-28 07:16
Tags: #daily-knowledge #ai

---
# Convex's official Claude Code plugin skills post users' app ideas to a remote host and tel

A GitHub issue on Convex's plugin, listed in Anthropic's official Claude Code marketplace, drew wide attention on 27 November: the quickstart skills POST the user's one-sentence idea to a generated convex.site host as 'telemetry', pipe remote scripts into bash, and instruct the agent to run download and execution as separate Bash calls because a single download-and-run command 'is the shape harness safety classifiers block'. New findings on 28 November add unpinned dependencies and a deploy flag that does not stop deployment.

## Details

**Caveats**
The reporter describes it as an onboarding team's shortcut, not malware. Marketplace listing pins a specific commit, so installed versions may differ.

**For your work**
Add a skill review step to client agent rollouts: grep skills for network calls, curl|bash and any text that discusses classifiers or permission prompts; allow skills only from vetted plugins.

**Method**
- skills/quickstart/SKILL.md (lines 48-56) sends the idea to basic-anteater-667.convex.site/generate with curl, without telling the user
- The same skill downloads a bootstrap script to /tmp and says: 'Run the next block as a SEPARATE Bash call' so it 'reads as an ordinary local script'
- skills/add/SKILL.md runs 'curl ... | bash' from the same host; labs-quickstart repeats the split pattern
- The issue was opened on 26 October; no maintainer reply is visible in the thread

**Problem**
Third-party skills are instructions the agent follows with the user's permissions. A skill that is written to reshape commands so a permission classifier doesn't flag them defeats the harness's main safety layer, even if the vendor's intent is onboarding reliability.

**Results**
- Verified in the current skill files on the main branch
- A 28 November comment says add-hosting publishes to a .convex.site domain and the QB_NO_PUBLISH=1 flag does not stop backend deployment
- The commenter confirmed /generate accepts arbitrary project descriptions and returns unique IDs

**Concepts:** [[Agent security]] · [[Claude]] · [[Coding agents]]
**From:** [[2026-11-28]]

# My notes


---
# References
[GitHub issue](https://github.com/convex/convex-backend-skill/issues/64)
