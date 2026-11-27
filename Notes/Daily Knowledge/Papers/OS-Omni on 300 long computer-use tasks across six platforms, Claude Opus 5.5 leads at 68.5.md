---
date: 2026-11-27
section: AI
importance: Med
kind: paper
source: "arXiv 2611.34232"
url: https://arxiv.org/abs/2611.34232
status: unread
id: 2026-11-27-os-omni-computer-use
---
2026-11-27 07:16
Tags: #daily-knowledge #ai

---
# OS-Omni on 300 long computer-use tasks across six platforms, Claude Opus 5.5 leads at 68.5

OS-Omni is a live benchmark of long workflows (humans need 67.54 steps on average, against 15.0 for OSWorld) on Windows, Ubuntu, macOS, iOS, Android and the web, plus phone-plus-desktop workflows, scored by checking the final application state. Claude Opus 5.5 reaches 68.5% macro-average success and GPT-6-Astra 66.1% (they are nearly tied on solved tasks, 200 vs 201), while the best iOS and macOS results remain 33.5 and 25.6 points below humans. Tested on: 9 models from 7 developers, 300 tasks, one screenshot-based agent loop, single run per task.

## Details

**Problem**
Computer-use benchmarks usually test web, mobile or desktop in isolation with short tasks, so it is unclear whether one agent can finish long workflows across operating systems and apps with persistent state.

**Method**
- 300 tasks: 48 each on Windows, Ubuntu, macOS, iOS, Android and Web, plus 12 workflows pairing a desktop with an Android phone shown through scrcpy.
- Reproducible VM or simulator resets, mock service apps (bank, shop, trips, budget, calendar, messages) and executable final-state evaluators.
- Agents see the current screenshot plus the last three steps; up to 300 steps per single-platform task.

**Results**
- Macro-average: Claude Opus 5.5 68.5%, GPT-6-Astra 66.1%, Gemini 4 Argon 58.6%, DeepSeek V4.1 Flash 30.4%; humans 77.3%.
- Windows: GPT-6-Astra 66.7%, Opus 5.5 62.5%, humans 78.4%. Linux: all three frontier models beat humans (Gemini 95.8%).
- iOS best is 41.7% (Opus 5.5); Qwen 3.8 27B and 9B solve almost nothing.
- Failure examples: an agent submitted the same bank transfer twice; another duplicated one booking and omitted another.

**Caveats**
Only 48 tasks per platform and 12 cross-platform workflows, one run each, so per-platform gaps are noisy. Windows tasks need user activation and macOS/iOS need Apple hardware. Screenshot-only setup; no vendor agent products tested.

**For your work**
When scoping a computer-use agent for a client, use the per-platform gap: Windows and Linux desktop flows are plausible, while macOS and iOS automation is still unreliable. Add final-state checks for duplicate actions (double transfers, duplicate bookings).

**Concepts:** [[Computer-use agents]] · [[Evals and benchmarks]] · [[Claude]]
**From:** [[2026-11-27]]

# My notes


---
# References
[arXiv 2611.34232](https://arxiv.org/abs/2611.34232)
