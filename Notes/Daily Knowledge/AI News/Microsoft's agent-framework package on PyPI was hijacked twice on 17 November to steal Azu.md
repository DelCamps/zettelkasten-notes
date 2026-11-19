---
date: 2026-11-19
section: AI
importance: High
kind: news
source: "SafeDep"
url: https://safedep.io/blog/microsoft-agent-framework-pypi-compromise
status: unread
id: 2026-11-19-ms-agent-framework-pypi-compromise
---
2026-11-19 07:16
Tags: #daily-knowledge #ai

---
# Microsoft's agent-framework package on PyPI was hijacked twice on 17 November to steal Azu

Versions 1.26.1 and 1.26.2 of agent-framework, the meta-package of Microsoft Agent Framework (about 192,000 downloads a month), installed a .pth hook that runs a credential stealer every time Python starts, even if nothing imports the package. It also requests fresh tokens from Azure managed identity, Azure DevOps and GitHub Actions OIDC. A PyPI maintainer account created on the attack day still had publish rights to six projects on 18 November.

## Details

**Caveats**
How the attacker got publishing access and how many installs happened are not yet known. Neither PyPI nor Microsoft has released the upload log. The attribution to vibiret is inferred from its join date.

**For your work**
If any client or internal project uses Microsoft Agent Framework in Python, pin agent-framework==1.26.0 together with its core dependencies, and search egress logs for webhook.site. Rotating stored secrets is not enough: revoke tokens issued to managed identities and pipelines that ran an install on 17 November.

**Method**
- A 28-byte agent_framework_meta.pth file imports a module that forks and detaches a collector, so builds show no delay
- It harvests environment variables matching 31 strings (TOKEN, SECRET, AZURE, OPENAI, HF_...), up to 60 credential files (~/.azure, .npmrc, .git-credentials, Docker config, Azure AI Foundry config) and up to 300 /proc/<pid>/environ files
- It mints new tokens: a federated api://AzureADTokenExchange token via SYSTEM_ACCESSTOKEN in Azure DevOps, and managed-identity tokens for Resource Manager, Key Vault, Storage, Graph and Azure AI; 1.26.2 adds GitHub Actions OIDC
- Data is zlib-compressed, base64-encoded and POSTed to a webhook.site URL, the one indicator both versions share

**Problem**
A supply-chain compromise of Microsoft's official Python agent framework on 17 November 2026 (UTC). A pip install in a CI job or dev box was enough to leak cloud and pipeline credentials.

**Results**
- SafeDep flagged 1.26.1 22 minutes after upload and 1.26.2 4 minutes after upload; both were removed from PyPI
- 1.26.2 shipped under new file names after 1.26.1 was pulled, so hash checks for 1.26.1 miss it
- Account vibiret, created 17 November 2026, is listed as maintainer and can publish to five related projects; four of them install with agent-framework 1.26.0
- PyPI has no attestation even for 1.26.0, so consumers had no cryptographic way to tell the uploads apart

**Concepts:** [[Agent security]] · [[Agents]]
**From:** [[2026-11-19]]

# My notes


---
# References
[SafeDep](https://safedep.io/blog/microsoft-agent-framework-pypi-compromise)
