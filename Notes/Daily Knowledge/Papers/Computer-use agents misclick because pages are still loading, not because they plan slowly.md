---
date: 2026-10-31
section: AI
importance: Med
kind: paper
source: "arXiv 2610.39282"
url: https://arxiv.org/abs/2610.39282
status: unread
id: 2026-10-31-cua-stale-clicks
---
2026-10-31 07:16
Tags: #daily-knowledge #ai

---
# Computer-use agents misclick because pages are still loading, not because they plan slowly

On 31 public pages, 0.4% of clicks planned on fully loaded pages went stale within 30 seconds, against 17% planned in the first second after opening; waiting for network idle (median 1.24 s) cut this to 0.46%, yet the wait rules of eight of ten open-source agents leave over 1% stale. A 0.3-second pixel check verifies the click target as well as Claude Opus 5.5 with fewer false alarms. Tested on: 31 public pages, wait rules of 10 open-source agents reimplemented (agents not run), an HTTP Archive crawl of 65 booking and 3,028 .gov home pages, and 6 synthetic moving pages; checks compared across pixels, OCR, 3 small open VLMs and Claude Haiku and Opus 5.5.

## Details

**Problem**
Agents screenshot, plan for seconds, then click coordinates; if the page moved, the click hits something else. Prior work blamed the planning delay.

**Method**
- Tracked about 1,300 targets per state (loaded, scrolled, newly opened) over three rounds, preregistered.
- Applied each agent's post-navigation wait rule from its current code to the same pages.
- Benchmark of 4,608 click pairs and 3,600 action-outcome pairs; break-even formula for when a check pays; live loop with a Haiku planner.

**Results**
- Stale clicks by wait rule: OpenAI CUA sample 15.4%, Stagehand v4 12.5%, browser-use 4.0%, Anthropic CU demo 2.0%, Skyvern 0.46%.
- Pixel check: 82% of stale clicks caught at 4% false alarms in 312 ms; Opus 83% at 12% in 2.4 s; Haiku flagged 95% of valid clicks.
- Qwen3-VL 4B matched Opus at checking whether the previous action succeeded.
- Re-aiming the click instead of re-planning was unsafe (best 11% wrong); 52% of booking home pages shifted layout after a 3 s-capped wait.

**Caveats**
Agents were not executed; real pages were non-commercial; commercial results come from a crawl proxy that failed its transfer check. Desktop only.

**For your work**
In browser agents, wait for network idle (cap about 3 s) before screenshots, pixel-check before irreversible clicks, re-plan when it fails, and use a small model for outcome checks.

**Concepts:** [[Computer-use agents]] · [[Agents]]
**From:** [[2026-10-31]]

# My notes


---
# References
[arXiv 2610.39282](https://arxiv.org/abs/2610.39282)
