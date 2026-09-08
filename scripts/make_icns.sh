#!/usr/bin/env bash
# Convert the 512px preview PNG into an .icns for macOS PyInstaller bundles.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/assets/app-icon-preview.png"
OUT_DIR="$ROOT/build"
ICNS="$OUT_DIR/app.icns"

if [[ ! -f "$SRC" ]]; then
  echo "Missing $SRC" >&2
  exit 1
fi

mkdir -p "$OUT_DIR"
sips -s format icns "$SRC" --out "$ICNS" >/dev/null
echo "Wrote $ICNS"
