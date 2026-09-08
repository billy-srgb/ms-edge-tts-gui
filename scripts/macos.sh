#!/usr/bin/env bash
# Build EdgeTTSGui-macOS-<arch>.dmg (must run on macOS).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [[ "$(uname -s)" != "Darwin" ]]; then
  echo "macOS 包必须在 macOS 上构建。" >&2
  exit 1
fi

if python3 -c "import PyInstaller" >/dev/null 2>&1; then
  PYTHON=python3
else
  if [[ ! -x "$ROOT/.venv/bin/python" ]]; then
    python3 -m venv "$ROOT/.venv"
    "$ROOT/.venv/bin/python" -m pip install --upgrade pip
  fi
  "$ROOT/.venv/bin/python" -m pip install -r "$ROOT/requirements-dev.txt"
  PYTHON="$ROOT/.venv/bin/python"
fi

mkdir -p "$ROOT/build"
ICON="$ROOT/build/app.icns"
sips -s format icns "$ROOT/assets/app-icon-preview.png" --out "$ICON" >/dev/null

"$PYTHON" -m PyInstaller \
  --noconfirm --clean --onedir --windowed \
  --name EdgeTTSGui \
  --icon "$ICON" \
  --paths "$ROOT/src" \
  --osx-bundle-identifier com.wangyufan.edgettsgui \
  --hidden-import docx --hidden-import pypdf --hidden-import certifi \
  --collect-data certifi --collect-all customtkinter --collect-submodules edgettsgui \
  "$ROOT/src/edgettsgui/__main__.py"

APP="$ROOT/dist/EdgeTTSGui.app"
if [[ ! -d "$APP" ]]; then
  echo "PyInstaller 未生成 $APP" >&2
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
hdiutil create -volname "EdgeTTSGui" -srcfolder "$STAGING" -ov -format UDZO "$DMG"
rm -rf "$STAGING"
echo "Wrote $DMG"
