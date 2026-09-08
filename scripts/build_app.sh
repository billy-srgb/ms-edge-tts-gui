#!/usr/bin/env bash
# PyInstaller onedir / .app build used by CI and local packagers.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

ICON="${1:-}"
if [[ -z "$ICON" ]]; then
  case "$(uname -s)" in
    Darwin) ICON="$ROOT/build/app.icns" ;;
    *) ICON="$ROOT/assets/app-icon-preview.png" ;;
  esac
fi

if [[ "$(uname -s)" == "Darwin" && ! -f "$ICON" ]]; then
  "$ROOT/scripts/make_icns.sh"
  ICON="$ROOT/build/app.icns"
fi

ARGS=(
  --noconfirm
  --clean
  --onedir
  --windowed
  --name EdgeTTSGui
  --icon "$ICON"
  --hidden-import docx
  --hidden-import pypdf
  --hidden-import certifi
  --collect-data certifi
  --collect-all customtkinter
)

if [[ "$(uname -s)" == "Darwin" ]]; then
  ARGS+=(--osx-bundle-identifier com.wangyufan.edgettsgui)
fi

python -m PyInstaller "${ARGS[@]}" app.py
