# CloudTrail Detection Notes

## Focus Areas
- Identity changes
- Console logins without MFA
- Policy changes
- Key creation and suspicious token use

## Sample Detection Logic
- Alert on IAM policy changes by non-admin personas
- Alert on access key creation followed by unusual API activity
- Alert on root usage or sign-in anomalies

## Next Enhancements
- Add sample CloudTrail records
- Map detections to ATT&CK
- Build a test matrix for each detection
