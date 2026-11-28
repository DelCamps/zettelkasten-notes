---
date: 2026-11-28
section: AI
importance: Med
kind: value
source: "AWS Machine Learning blog"
url: https://aws.amazon.com/blogs/machine-learning/introducing-the-amazon-bedrock-trusted-access-api-with-anthropics-enterprise-frontier-safeguards-and-enterprise-data-controls/
status: unread
id: 2026-11-28-bedrock-trusted-access-efs
---
2026-11-28 07:16
Tags: #daily-knowledge #ai #update

---
# Amazon Bedrock trusted access program API is GA, and Enterprise Frontier Safeguards and En

AWS made the Bedrock trusted access program API generally available, one place to check eligibility and enrol in model providers' programs, governed with IAM policies and SCPs. The first two offerings, in public preview, give zero retention by Anthropic for Claude Fable, Claude Mythos and Cyber Verification Program models: with EFS, prompts and completions are written only to the customer's own S3 bucket under their KMS key; with EDC, they sit in Amazon-managed storage for up to 30 days.

## Details

**Availability and price**
Trusted access program API GA; EFS and EDC public preview, requested through the AWS account team, and the preview is for customers already enrolled in EFS ZDR. EFS adds usual S3 and KMS charges. Region list not stated; configurations apply one Region at a time.

**Caveats**
Bedrock stops serving covered models 24 hours after it loses access to the key or bucket. Joining the preview turns off the interim ZDR exception (which runs through at least June 30, 2027). Cases aren't delivered for EDC during the preview.

**Client use cases**
- Banks, insurers and healthcare clients that want Claude Fable/Mythos on AWS without the provider keeping prompts
- Security teams using Cyber Verification Program models under their own key
- Central enrolment control for many accounts via AWS Organizations

**How we could offer it**
- Assessment: map client data-retention policy to EFS vs EDC vs the interim ZDR exception
- Implementation: KMS key, S3 bucket and policies per Region, plus CloudTrail checks
- Managed service: run the Safety Case review process for the client

**Pitch**
Clients blocked from Anthropic's strongest models by retention rules now have an AWS-native path where retained data stays in their own account; we can set it up and run the case review.

**What it is**
The Bedrock counterpart of Anthropic's Enterprise Frontier Safeguards. Automated safety monitoring runs inside AWS and creates Safety Cases in the customer's bucket for the customer's own team to review; AWS human reviewers don't review EFS content and the data is never used for training.

**Concepts:** [[AWS]] · [[Claude]] · [[AI safety]]
**From:** [[2026-11-28]]

# My notes


---
# References
[AWS Machine Learning blog](https://aws.amazon.com/blogs/machine-learning/introducing-the-amazon-bedrock-trusted-access-api-with-anthropics-enterprise-frontier-safeguards-and-enterprise-data-controls/)
