---
date: 2026-11-16
section: AI
importance: Low
kind: value
source: "AWS What's New"
url: https://aws.amazon.com/about-aws/whats-new/2026/11/aws-quick-structured-data-source-restrictions/
status: unread
id: 2026-11-16-aws-quick-data-source-restrictions
---
2026-11-16 07:16
Tags: #daily-knowledge #ai

---
# AWS Quick lets admins restrict which structured data sources users can create, update or s

AWS made structured data connector restrictions generally available in AWS Quick Enterprise edition. Admins can, for example, allow Amazon Redshift sources while blocking file uploads, and set create, update and share rights independently.

## Details

**Availability and price**
GA in all supported AWS Quick Regions; Enterprise edition. No pricing mentioned.

**Caveats**
A narrow admin feature; useful mainly as part of a wider Quick deployment. AWS, not Microsoft-stack.

**Client use cases**
- Stop shadow uploads of spreadsheets into AI chat and dashboards
- Limit self-service analytics to governed warehouse sources
- Restrict sharing of sensitive connectors to specific teams

**How we could offer it**
- Include in an AWS Quick governance baseline alongside smart approvals and data access controls
- Permission-profile design per persona as part of a Quick rollout

**Pitch**
Clients can now let staff use AI analytics in Quick while keeping data on governed sources only. We design the permission profiles so self-service does not mean ungoverned.

**What it is**
A governance control in AWS Quick, Amazon's AI assistant and BI suite for work. Through custom permissions profiles, administrators control which types of structured data sources users can create, update or share. AWS's example: an organization can "allow users to create Amazon Redshift data sources" while limiting file-upload sources, and administrators can "prevent users from sharing data sources for a particular connector." "Create, update, and share restrictions can be configured independently." Settings are made in the Quick UI, the APIs or the AWS CLI.

**Concepts:** [[AWS]]
**From:** [[2026-11-16]]

# My notes


---
# References
[AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-quick-structured-data-source-restrictions/)
