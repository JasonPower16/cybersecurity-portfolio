# Azure / Entra ID Risky Sign-In Investigation

## Objective
Document how to investigate risky sign-ins and validate whether the activity is a real compromise, benign travel, or identity misuse.

## Investigation Inputs
- User identity
- Sign-in risk level
- IP address and geo-location
- MFA result
- Device state and compliance
- Conditional Access outcomes

## Key Questions
- Is the sign-in location normal for the user?
- Was MFA successfully enforced?
- Was the device managed and compliant?
- Is there follow-on activity in M365 or Azure resources?

## Detection Opportunities
- High-risk sign-ins without strong MFA
- New country followed by impossible travel indicators
- Multiple failures followed by success
- Sign-ins from suspicious cloud providers or anonymizers

## Response Options
- Force password reset
- Revoke tokens
- Require reauthentication
- Investigate mailbox, SharePoint, and admin actions
