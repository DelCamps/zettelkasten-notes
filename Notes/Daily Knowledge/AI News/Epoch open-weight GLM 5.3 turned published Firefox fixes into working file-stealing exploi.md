---
date: 2026-10-31
section: AI
importance: High
kind: news
source: "Epoch AI report"
url: https://epoch.ai/publications/open-weight-models-patch-gap
status: unread
id: 2026-10-31-epoch-glm-patch-gap-exploits
---
2026-10-31 07:16
Tags: #daily-knowledge #ai

---
# Epoch open-weight GLM 5.3 turned published Firefox fixes into working file-stealing exploi

Epoch AI let GLM 5.3 work alone for up to 48 hours per attempt. It built webpages that read local files through six Firefox releases from 156.0 to 158.0.1, using fixes that were public before users had them. Each exploit cost about $1,000 in API calls and no provider's safeguards triggered. Chrome resisted about $100,000 of attempts.

## Details

**Problem**
The 'patch gap' is the window between a security fix becoming public and it reaching users. The question was whether a cheap open-weight model can exploit that window on its own.

**Method**
- Target: a webpage that, when opened in official Firefox on Ubuntu 26.04 with default settings, sends a local file to the attacker.
- The model was told only to target the patch gap. It picked the fixes, chose vulnerabilities and built the chain itself, offline, using only information available at each release date, for up to 48 hours per attempt.
- GLM 5.3 was called through Z.ai's API and third-party APIs, framed as a security exercise.

**Results**
- Working file-read exploits for Firefox 156.0, 156.0.1, 157.0, 157.0.1, 158.0 and 158.0.1. The fastest attempt took about 12 hours, at about $1,000 marginal cost per version.
- Every exploit also used a sandbox escape the model rediscovered each time. Mozilla patched it in Firefox 159.0, released October 27, 2026.
- Chrome: about $100,000 of API spend with no equivalent exploit. No arbitrary code execution was achieved.

**Caveats**
One model and two browsers. Total Firefox research spend was over $100,000 and the exploits only read files. Kimi K3.1 Pro may be stronger but was not tested.

**For your work**
Assume n-day exploits now follow public patches within hours, and shorten patch SLAs for the browsers and Electron apps that client agents use. The setup (offline sandbox, live monitoring, a kill switch) is also a template for internal red-team evaluations.

**Concepts:** [[AI for security]] · [[Open-weight models]] · [[Evals and benchmarks]]
**From:** [[2026-10-31]]

# My notes


---
# References
[Epoch AI report](https://epoch.ai/publications/open-weight-models-patch-gap)
