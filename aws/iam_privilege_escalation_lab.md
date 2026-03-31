# AWS IAM Privilege Escalation Lab

## Objective
Simulate and document a privilege escalation path caused by overly broad IAM permissions.

## Environment
- AWS IAM
- CloudTrail
- Optional: GuardDuty for comparison

## Scenario
A low-privileged user has permission to create or update policies and can escalate to administrative access.

## Attack Path
1. User authenticates with limited rights
2. User creates a new policy version or attaches a stronger policy
3. User gains broader privileges
4. High-impact actions become possible

## Detection Opportunities
Monitor CloudTrail events such as:
- `CreatePolicyVersion`
- `SetDefaultPolicyVersion`
- `AttachUserPolicy`
- `AttachRolePolicy`
- `PutUserPolicy`

## Validation Questions
- Was the actor expected to manage IAM?
- Did the action occur outside a maintenance window?
- Did privilege changes lead to sensitive API use?

## Mitigations
- Least privilege
- Service Control Policies
- Permission boundaries
- Alerting for IAM policy changes

## Portfolio Upgrade Ideas
- Add a CloudTrail JSON sample
- Add a Sigma-like detection or Splunk query for AWS logs
- Add a diagram showing the escalation path
