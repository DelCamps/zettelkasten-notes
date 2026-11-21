---
date: 2026-11-21
section: AI
importance: High
kind: paper
source: "Hugging Face blog"
url: https://huggingface.co/blog/TonyDzi/our-claude-code-calls-go-cold-after-60-idle-minute
status: unread
id: 2026-11-21-claude-code-codex-cache-cold
---
2026-11-21 07:16
Tags: #daily-knowledge #ai

---
# Prompt-cache log study (one operator, 71,393 calls) Claude Code calls go cold at exactly 6

Reading token usage from local session logs, the author found Claude Code calls almost never cold within 58 minutes but 6 of 7 cold at 60-62 minutes and 99-100% from 62 minutes on, matching the one-hour subscription cache; Codex cooled gradually, from 16.7% cold at 1-2 hours to 169 of 171 calls beyond 12 hours. Human returns after more than an hour (973, of which 967 cold) carried about 25% of all input-equivalent cost. Tested on: one operator's fleet, 500 sessions (465 Claude Code, 35 Codex) from 5 machines over 2026-11-02 to 2026-11-20, plus a 2,359-session Codex probe; costs in API list-price units, not dollars.

## Details

**Caveats**
One operator's fleet, biased to long, often-resumed sessions; few calls in the bins near one hour and no confidence intervals. Cold is inferred from low cache read, so compaction or model switches can also cause it. Costs use API list prices, not subscription limits, and the savings model ignores lost context.

**For your work**
For clients paying API rates on long agent sessions, idle gaps over an hour mean the whole context is rebilled as cache writes. Consider a resume policy: summarize into a fresh session for big contexts, or keep sessions warm when people step away.

**Method**
- Counted, per call, the cache read and the pause since the previous call, straight from local session logs, with no model in the loop.
- Defined a 'cold' call as one with a low cache read (different thresholds for Claude Code and Codex).
- Modelled a rule that starts a fresh session above 300K context instead of resuming a cold one.

**Problem**
Coding agents resend the whole conversation on every call; the prompt cache makes that cheap until it expires. How long does the cache survive between calls, and how much input cost goes into returning to cold sessions?

**Results**
- Claude Code: 0.1% cold at 0-5 minute pauses (87 of 63,369 calls), 0 of 10 at 58-60 minutes, 6 of 7 at 60-62 minutes, 99-100% from 62 minutes.
- Codex: 0.5% cold at 0-5 minutes, 16.7% at 1-2 hours, 46.2% at 2-6 hours, 74.1% at 6-12 hours.
- 973 human returns after more than an hour, 967 of them cold, carried 596M of 2,349M input-equivalent units (about 25%).
- The 300K fresh-session rule saves between 3.4% (floor after writing briefs) and 25.0% (full model) of input.

**Concepts:** [[Coding agents]] · [[Inference efficiency]] · [[Claude]]
**From:** [[2026-11-21]]

# My notes


---
# References
[Hugging Face blog](https://huggingface.co/blog/TonyDzi/our-claude-code-calls-go-cold-after-60-idle-minute)
