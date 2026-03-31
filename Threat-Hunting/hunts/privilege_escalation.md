# Privilege Escalation Hunt

## Hypothesis
A user or process gained elevated access through suspicious group membership changes, token abuse, or exploitation of excessive privilege.

## Data Sources
- Windows Event Logs
- Identity provider logs
- EDR telemetry
- Cloud control plane logs if applicable

## Hunt Logic
Look for:
- New administrative group membership
- Use of privileged tokens
- Service creation or scheduled task abuse
- IAM/role changes in cloud environments

## Findings Template
- What changed?
- Who initiated it?
- Was there a business justification?
- Did it enable follow-on sensitive activity?
