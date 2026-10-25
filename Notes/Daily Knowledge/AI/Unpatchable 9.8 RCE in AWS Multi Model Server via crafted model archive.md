---
date: 2026-10-25
section: AI
importance: Low
source: "AWS bulletin 2026-148"
url: https://www.thehackerwire.com/vulnerability/CVE-2026-115812/
status: unread
id: 2026-10-25-aws-mms-cve
---
2026-10-25 07:16
Tags: #daily-knowledge #ai

---
# Unpatchable 9.8 RCE in AWS Multi Model Server via crafted model archive

CVE-2026-115812 is a path-traversal during model-archive extraction in AWS Multi Model Server 1.1.11 and earlier, giving unauthenticated code execution. The project is end-of-life, so no fix is coming: migrate any legacy MMS endpoints and never load model archives from untrusted sources.

**Concepts:** [[AI for security]] · [[Model serving]]
**From:** [[2026-10-25]]

# My notes


---
# References
[AWS bulletin 2026-148](https://www.thehackerwire.com/vulnerability/CVE-2026-115812/)
