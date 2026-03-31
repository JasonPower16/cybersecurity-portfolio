# MITRE ATT&CK Mapping

## DET-001 – PowerShell Suspicious Execution
- **Tactic:** Execution
- **Technique:** T1059.001 – PowerShell
- **Reasoning:** Encoded commands and script download behavior are common indicators of malicious PowerShell execution.

## DET-002 – Credential Dumping Indicators
- **Tactic:** Credential Access
- **Technique:** T1003 – OS Credential Dumping
- **Reasoning:** LSASS targeting and dump tooling are strong indicators of credential theft attempts.

## DET-003 – Abnormal Remote Execution / Lateral Movement
- **Tactic:** Lateral Movement
- **Technique:** T1021 – Remote Services
- **Reasoning:** Remote service creation and suspicious administrative command-line use can indicate attacker pivoting between hosts.
