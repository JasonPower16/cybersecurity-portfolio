# Basic Alert Enrichment Playbook

## Goal
Reduce analyst time spent copying observables into multiple tools.

## Workflow
1. Alert is ingested from SIEM
2. Extract IPs, domains, and hashes
3. Enrich observables with threat intelligence
4. Add host, user, and asset criticality context
5. Output triage recommendation

## Decision Points
- Is the observable known malicious?
- Is the affected host sensitive or privileged?
- Is the behavior expected for the user or system?

## Suggested Improvements
- Add ticket creation
- Add chat notifications
- Add suppression rules for known benign activity
