---
date: 2026-11-04
section: AI
importance: Med
kind: news
source: "Check Point Research"
url: https://research.checkpoint.com/2026/free-the-model-sell-the-gateway-prompt-adware-hidden-in-jailbreak-bundles/
status: unread
id: 2026-11-04-prompt-adware-haiou
---
2026-11-04 07:16
Tags: #daily-knowledge #ai

---
# Check Point finds 'prompt adware' a Codex jailbreak bundle rewrites global agent instructi

Check Point Research analysed Haiou, a Chinese jailbreak bundle for OpenAI Codex with more than 250 GitHub stars, which installs six security skills and quietly edits Codex's global instruction files so that greetings trigger an ad for its author's LLM gateway. The payload is encrypted to evade scanners, and Check Point found it on a cybercrime actor's server alongside Cobalt Strike; Claude Code flagged the Claude version's injection and refused.

## Details

**Caveats**
The gateway is not known to be malicious and no data theft was observed; the risk is what the same persistence could do, such as steering vendor recommendations.

**For your work**
Treat skills, AGENTS.md-style files and global agent config as supply chain: allow-list them, diff them, and alert on changes on client developer machines.

**Method**
- Haiou (version 4.5.0 analysed) is verified with Ed25519 signatures and SHA-256 hashes, then decrypted with an embedded AES-256-GCM key, so its prompts are opaque to anyone browsing the repo.
- It jailbreaks Codex with a rule-breaking persona, blacklisted refusal phrases, and reframing offensive tasks as CTF exercises.
- It adds a persistent rule to Codex's global agent instructions that answers greetings and trigger words with a fixed ad for an OpenAI-compatible LLM gateway.

**Problem**
Agents trust global prompts, skills and config files; third-party packages that edit them can change future behaviour with no executable payload for security tools to spot.

**Results**
- Found on a misconfigured threat-actor webserver next to Cobalt Strike, the VulnClaw agent and the Ladon scanner.
- Six skills cover license cracking, penetration testing, reverse engineering and anti-cheat bypass.
- In testing, Sonnet 5 in Claude Code flagged the prompt-injection attempt and did not comply; the Claude repo version carries no ad injection.

**Concepts:** [[Agent security]] · [[Coding agents]]
**From:** [[2026-11-04]]

# My notes


---
# References
[Check Point Research](https://research.checkpoint.com/2026/free-the-model-sell-the-gateway-prompt-adware-hidden-in-jailbreak-bundles/)
