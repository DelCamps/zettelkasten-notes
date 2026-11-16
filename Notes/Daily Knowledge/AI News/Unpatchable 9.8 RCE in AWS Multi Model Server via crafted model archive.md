---
date: 2026-10-25
section: AI
importance: Low
kind: news
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

## Details

**Caveats**
Only legacy deployments are affected; no public exploit confirmed yet.

**For your work**
Check client estates for leftover MMS endpoints (old SageMaker-era setups) and migrate. More generally, never let users upload model archives to a serving stack without sandboxed extraction.

**Method**
- CVE-2026-115812, CWE-23 relative path traversal during model-archive extraction in MMS 1.1.11 and earlier.
- A crafted archive writes files outside the target directory, leading to remote code execution; network-reachable, low complexity, no privileges.

**Problem**
AWS Multi Model Server, an older open-source model-serving framework, extracts uploaded model archives without sanitising paths.

**Results**
- CVSS 9.8 critical; disclosed 23 October 2026.
- No fix: MMS is end-of-life and users are told to migrate.
- Not yet in CISA's known-exploited catalogue; EPSS about 0.73%.

**Concepts:** [[AI for security]] · Model serving
**From:** [[2026-10-25]]

# My notes


---
# References
[AWS bulletin 2026-148](https://www.thehackerwire.com/vulnerability/CVE-2026-115812/)
