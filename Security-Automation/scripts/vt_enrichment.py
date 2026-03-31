"""VirusTotal IP enrichment example.

Set the VT_API_KEY environment variable before running.
"""

from __future__ import annotations

import json
import os
import sys

import requests


def enrich_ip(ip: str) -> dict:
    api_key = os.getenv("VT_API_KEY")
    if not api_key:
        raise RuntimeError("VT_API_KEY environment variable is not set.")

    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": api_key}
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    return response.json()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python vt_enrichment.py <ip>")
        raise SystemExit(1)

    result = enrich_ip(sys.argv[1])
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
