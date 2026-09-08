#!/usr/bin/env bash
# Local macOS / Linux release build (CI uses the same scripts).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

if [[ ! -x "$ROOT/.venv/bin/python" ]]; then
  python3 -m venv "$ROOT/.venv"
  "$ROOT/.venv/bin/python" -m pip install --upgrade pip
fi
"$ROOT/.venv/bin/python" -m pip install -r "$ROOT/requirements-dev.txt"

# shellcheck disable=SC1091
source "$ROOT/.venv/bin/activate"

"$ROOT/scripts/build_app.sh"

case "$(uname -s)" in
  Darwin)
    "$ROOT/scripts/pack_macos_dmg.sh"
    echo "Build complete."
    echo "DMG: dist/EdgeTTSGui-macOS-$(uname -m).dmg"
    ;;
  Linux)
    "$ROOT/scripts/pack_linux.sh"
    echo "Build complete."
    echo "Debian: dist/EdgeTTSGui-linux-*.deb"
    echo "AppImage: dist/EdgeTTSGui-linux-*.AppImage"
    ;;
  *)
    echo "Use build_release.bat on Windows." >&2
    exit 1
    ;;
esac
