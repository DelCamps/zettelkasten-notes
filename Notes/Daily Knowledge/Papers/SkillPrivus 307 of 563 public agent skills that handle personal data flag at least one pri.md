---
date: 2026-11-23
section: AI
importance: Med
kind: paper
source: "arXiv 2611.26747"
url: https://arxiv.org/abs/2611.26747
status: unread
id: 2026-11-23-skillprivus-skill-privacy-audit
---
2026-11-23 07:16
Tags: #daily-knowledge #ai

---
# SkillPrivus 307 of 563 public agent skills that handle personal data flag at least one pri

SkillPrivus is a static pre-install audit. It extracts each data operation from a skill's code and SKILL.md instructions and judges it against the skill's stated purpose using Contextual Integrity. It flagged 2,144 of 22,158 data operations (9.7%), mostly skills reaching more data than they declare or sending it to unnamed recipients. These were ordinary skills, not malicious ones. Tested on: 726 skills from ClawHub, SkillsMP, skills.rest and the Anthropic and NVIDIA collections, one auditor model (gpt-oss-120b), validated against 3 human annotators on 311 data operations from 21 skills.

## Details

**Caveats**
The validation set is small (21 skills). Appropriateness is contested, and kappa values are only moderate. Static reading can miss access hidden in code the description never mentions. Only one auditor model was used.

**For your work**
Before clients roll out Claude or Copilot skills or plugins from marketplaces, add a privacy-of-use review that checks recipients and data scope against the stated purpose. A malware scan alone will not catch these.

**Method**
- Screen out skills that never touch personal data. Break code and instructions into source-grounded data operations, each tagged with information type, recipient, subject and operation.
- Judge each operation against what the stated purpose allows and what its domain conventionally allows. Deterministic rules cover settled cases, for example credentials always count as sensitive. GDPR Article 9 special-category data gets a stricter policy.
- Label each harm with Solove's taxonomy, extended with an Inference category.

**Problem**
Agent skills run with the assistant's access to files, accounts and data. Security scanners look for malicious code, but an honest skill can still infer, keep or disclose more than its task needs.

**Results**
- Of 563 analysed skills, 307 (54.5%) have at least one flagged operation.
- Root causes: data beyond the stated purpose 54.2%, unexpected recipient 33.7%. Most flags fall on routine read, send and save operations.
- Agreement with the human annotators was 83.2%, against 83.4% between the humans themselves.
- Example: an Apple Health skill POSTs the user's health question and API key to a vendor its description never names.

**Concepts:** [[Agent security]] · [[Agents]]
**From:** [[2026-11-23]]

# My notes


---
# References
[arXiv 2611.26747](https://arxiv.org/abs/2611.26747)
