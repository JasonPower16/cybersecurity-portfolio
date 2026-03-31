"""Extract simple indicators of compromise from a text file or stdin."""

from __future__ import annotations

import re
import sys
from pathlib import Path

IP_PATTERN = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
HASH_PATTERN = re.compile(r"\b[a-fA-F0-9]{32,64}\b")
DOMAIN_PATTERN = re.compile(r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b")


def read_text() -> str:
    if len(sys.argv) > 1:
        return Path(sys.argv[1]).read_text(encoding="utf-8")
    return sys.stdin.read()


def unique_sorted(items: list[str]) -> list[str]:
    return sorted(set(items))


def main() -> None:
    data = read_text()
    ips = unique_sorted(IP_PATTERN.findall(data))
    hashes = unique_sorted(HASH_PATTERN.findall(data))
    domains = unique_sorted(DOMAIN_PATTERN.findall(data))

    print("IPs:")
    for item in ips:
        print(f"  - {item}")

    print("Hashes:")
    for item in hashes:
        print(f"  - {item}")

    print("Domains:")
    for item in domains:
        print(f"  - {item}")


if __name__ == "__main__":
    main()
