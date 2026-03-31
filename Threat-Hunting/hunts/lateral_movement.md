# Lateral Movement Hunt

## Hypothesis
An attacker is using remote services or administrative tooling to move laterally between internal systems.

## Data Sources
- Windows Security Logs
- Sysmon
- EDR telemetry
- Authentication logs

## Hunt Logic
Look for:
- Network logons from unusual source hosts
- Remote service creation
- PsExec/WMI/remote cmd patterns
- Administrator activity from non-standard systems

## Investigation Notes
- Compare source systems against approved admin jump boxes
- Check whether the account normally administers the target
- Look for follow-on execution after successful authentication

## Outcome
Document whether the activity is benign administration, misconfiguration, or a potential intrusion chain.
