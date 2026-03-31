# Detection Engineering

This section focuses on building repeatable detections, mapping them to attacker tradecraft, and documenting false positive considerations.

## Folder Layout
- `detections/` – YAML-style portable detection logic
- `splunk_queries/` – SPL examples
- `mapping/` – ATT&CK mapping and rationale
- `test_data/` – sample logs for validation

## Starter Tasks
- Add detections for PowerShell misuse, credential dumping, and lateral movement
- Validate the detection logic using test logs
- Track false positives and tuning recommendations
