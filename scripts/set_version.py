#!/usr/bin/env python3
"""Write APP_VERSION in app.py from a tag or explicit version (v prefix optional)."""

import pathlib
import re
import sys

raw = sys.argv[1] if len(sys.argv) > 1 else ""
version = raw[1:] if raw.startswith("v") else raw
if not version:
    raise SystemExit("usage: set_version.py 1.3.0")

path = pathlib.Path("app.py")
text = path.read_text(encoding="utf-8")
updated, count = re.subn(
    r'APP_VERSION = "[^"]*"',
    f'APP_VERSION = "{version}"',
    text,
    count=1,
)
if count != 1:
    raise SystemExit("APP_VERSION assignment not found in app.py")
path.write_text(updated, encoding="utf-8")
print(version)
