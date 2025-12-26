#!/usr/bin/env python3
"""Generate raw GitHub URLs for all markdown files in the vault."""

from pathlib import Path
from urllib.parse import quote

BASE_URL = "https://raw.githubusercontent.com/fecet/vault/refs/heads/main"

for md_file in sorted(Path(".").glob("*.md")):
    encoded_name = quote(md_file.name)
    print(f"{BASE_URL}/{encoded_name}")
