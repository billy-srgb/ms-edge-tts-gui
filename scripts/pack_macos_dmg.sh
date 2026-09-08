#!/usr/bin/env bash
# Wrap dist/EdgeTTSGui.app into a drag-to-Applications DMG.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

APP="$ROOT/dist/EdgeTTSGui.app"
if [[ ! -d "$APP" ]]; then
  echo "Missing $APP — run scripts/build_app.sh first." >&2
  exit 1
fi

ARCH="$(uname -m)"
STAGING="$ROOT/build/dmg-root"
DMG="$ROOT/dist/EdgeTTSGui-macOS-${ARCH}.dmg"

rm -rf "$STAGING"
mkdir -p "$STAGING"
cp -R "$APP" "$STAGING/EdgeTTSGui.app"
ln -s /Applications "$STAGING/Applications"

rm -f "$DMG"
hdiutil create \
  -volname "EdgeTTSGui" \
  -srcfolder "$STAGING" \
  -ov \
  -format UDZO \
  "$DMG"

echo "Wrote $DMG"
