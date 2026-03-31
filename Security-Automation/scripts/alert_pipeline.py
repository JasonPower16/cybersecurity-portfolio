"""Basic local alert enrichment pipeline example."""

from __future__ import annotations

import json
from pathlib import Path

from log_parser import DOMAIN_PATTERN, HASH_PATTERN, IP_PATTERN


def enrich_alert(alert: dict) -> dict:
    text = json.dumps(alert)
    return {
        "original_alert": alert,
        "observed_ips": sorted(set(IP_PATTERN.findall(text))),
        "observed_hashes": sorted(set(HASH_PATTERN.findall(text))),
        "observed_domains": sorted(set(DOMAIN_PATTERN.findall(text))),
        "recommended_next_step": "Validate endpoint, enrich observables, and confirm user context.",
    }


def main() -> None:
    alert_path = Path(__file__).resolve().parent.parent / "examples" / "sample_alert.json"
    alert = json.loads(alert_path.read_text(encoding="utf-8"))
    enriched = enrich_alert(alert)
    print(json.dumps(enriched, indent=2))


if __name__ == "__main__":
    main()
