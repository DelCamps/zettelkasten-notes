---
date: 2026-11-25
section: AI
importance: High
kind: paper
source: "arXiv 2611.32195"
url: https://arxiv.org/abs/2611.32195
status: unread
id: 2026-11-25-permission-replies-rewrite-policy
---
2026-11-25 07:16
Tags: #daily-knowledge #ai

---
# Permission replies can rewrite Claude Code's policy one 'approve' from a remote approver d

Coding agents let plugins, hooks and remote relays answer permission prompts. The authors show an answer can carry a policy update that deletes the operator's deny rules, so the agent reads protected secrets in that session and later ones, even inside Claude Code's strict sandbox; about 7% of 70 surveyed relays, including Anthropic's own Remote Control, forward such updates. Tested on: Claude Code across all four answer routes with scripted and live models, plus 13 permission designs in 10 agent systems (Codex, Gemini CLI, opencode, Goose and others), and a survey of 2,227 marketplace plugins.

## Details

**Caveats**
Requires a malicious or compromised answering party (plugin, relay or the claude.ai account behind Remote Control). The deletion looks like a local operator edit, so logs will not show it.

**For your work**
Treat any permission relay, approval plugin or remote-control link as an administrator of the policy, not just a decider. Prefer managed or command-line settings for critical deny rules (the paper says the update write skips those tiers), and diff settings files after sessions.

**Method**
- Attack: a remote approval service approves an unrelated command and attaches an update that removes Read(./.env) from the deny list; the runtime writes it into the operator's settings
- Formal model with tight bounds: without recording who wrote each rule, a runtime can only safely accept updates that keep every denied call denied; with authorship, each party may lift only its own restrictions
- Predictions for 13 permission designs written down, several before running Codex, Gemini CLI, opencode and Goose

**Problem**
Vendors promise an answering party cannot override a deny rule, but that is checked one decision at a time. Nobody checked whether an answer can change the rules later decisions are checked against.

**Results**
- Attack works on recent Claude Code releases, including 2.1.327, through all four answer routes and the strict sandbox
- Claude Code filters only added or replaced allow rules, not deletions; three of four answer routes skip even that filter
- Bounds predicted the outcome for all 13 designs
- Only 2 of 2,227 fetched marketplace plugins send policy updates, so a fix at the shared update step costs little

**Concepts:** [[Agent security]] · [[Coding agents]] · [[Claude]]
**From:** [[2026-11-25]]

# My notes


---
# References
[arXiv 2611.32195](https://arxiv.org/abs/2611.32195)
