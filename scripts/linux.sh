#!/usr/bin/env bash
# Build EdgeTTSGui-linux-*.deb and *.AppImage (must run on Linux).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "Linux 包必须在 Linux 上构建。" >&2
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

"$PYTHON" -m PyInstaller \
  --noconfirm --clean --onedir --windowed \
  --name EdgeTTSGui \
  --icon "$ROOT/assets/app-icon-preview.png" \
  --paths "$ROOT/src" \
  --hidden-import docx --hidden-import pypdf --hidden-import certifi \
  --collect-data certifi --collect-all customtkinter --collect-submodules edgettsgui \
  "$ROOT/src/edgettsgui/__main__.py"

ONEDIR="$ROOT/dist/EdgeTTSGui"
if [[ ! -x "$ONEDIR/EdgeTTSGui" ]]; then
  echo "PyInstaller 未生成 $ONEDIR/EdgeTTSGui" >&2
  exit 1
fi

VERSION="${VERSION:-}"
if [[ -z "$VERSION" ]]; then
  VERSION="$("$PYTHON" -c "import re,pathlib; print(re.search(r'APP_VERSION = \"([^\"]+)\"', pathlib.Path('src/edgettsgui/config.py').read_text(encoding='utf-8')).group(1))")"
fi

MACHINE="$(uname -m)"
case "$MACHINE" in
  x86_64|amd64) DEB_ARCH=amd64; APPIMAGE_ARCH=x86_64 ;;
  aarch64|arm64) DEB_ARCH=arm64; APPIMAGE_ARCH=aarch64 ;;
  *) DEB_ARCH="$MACHINE"; APPIMAGE_ARCH="$MACHINE" ;;
esac

ICON_SRC="$ROOT/assets/app-icon-preview.png"
DESKTOP_SRC="$ROOT/installer/linux/edgettsgui.desktop"

DEB_ROOT="$ROOT/build/deb/edgettsgui_${VERSION}_${DEB_ARCH}"
rm -rf "$DEB_ROOT"
mkdir -p \
  "$DEB_ROOT/DEBIAN" \
  "$DEB_ROOT/opt/EdgeTTSGui" \
  "$DEB_ROOT/usr/bin" \
  "$DEB_ROOT/usr/share/applications" \
  "$DEB_ROOT/usr/share/icons/hicolor/512x512/apps" \
  "$DEB_ROOT/usr/share/doc/edgettsgui"

cp -a "$ONEDIR/." "$DEB_ROOT/opt/EdgeTTSGui/"
cp "$ICON_SRC" "$DEB_ROOT/usr/share/icons/hicolor/512x512/apps/edgettsgui.png"
cp "$ROOT/LICENSE" "$DEB_ROOT/usr/share/doc/edgettsgui/copyright"
if [[ -f "$ROOT/LICENSE.zh.txt" ]]; then
  cp "$ROOT/LICENSE.zh.txt" "$DEB_ROOT/usr/share/doc/edgettsgui/"
fi

sed \
  -e 's|^Exec=.*|Exec=/opt/EdgeTTSGui/EdgeTTSGui|' \
  -e 's|^Icon=.*|Icon=edgettsgui|' \
  "$DESKTOP_SRC" > "$DEB_ROOT/usr/share/applications/edgettsgui.desktop"

cat > "$DEB_ROOT/usr/bin/edgettsgui" << 'EOF'
#!/bin/sh
exec /opt/EdgeTTSGui/EdgeTTSGui "$@"
EOF
chmod 755 "$DEB_ROOT/usr/bin/edgettsgui" "$DEB_ROOT/opt/EdgeTTSGui/EdgeTTSGui"

SIZE_KB="$(du -sk "$DEB_ROOT" | awk '{print $1}')"
cat > "$DEB_ROOT/DEBIAN/control" << EOF
Package: edgettsgui
Version: ${VERSION}
Section: sound
Priority: optional
Architecture: ${DEB_ARCH}
Installed-Size: ${SIZE_KB}
Maintainer: WangYufan <https://github.com/JJosephph/ms-edge-tts-gui>
Homepage: https://github.com/JJosephph/ms-edge-tts-gui
Depends: libc6
Description: Edge TTS Voice Studio
 Desktop client for Microsoft Edge text-to-speech.
 Bundles its own Python runtime. Free and open source (MIT License).
EOF

DEB_OUT="$ROOT/dist/EdgeTTSGui-linux-${DEB_ARCH}.deb"
rm -f "$DEB_OUT"
dpkg-deb --root-owner-group --build "$DEB_ROOT" "$DEB_OUT"
echo "Wrote $DEB_OUT"

APPDIR="$ROOT/build/EdgeTTSGui.AppDir"
rm -rf "$APPDIR"
mkdir -p "$APPDIR/usr/bin"
cp -a "$ONEDIR" "$APPDIR/usr/bin/EdgeTTSGui"
cp "$ICON_SRC" "$APPDIR/EdgeTTSGui.png"
cp "$DESKTOP_SRC" "$APPDIR/EdgeTTSGui.desktop"
cat > "$APPDIR/AppRun" << 'EOF'
#!/bin/bash
set -e
SELF=$(readlink -f "$0")
HERE=${SELF%/*}
export PATH="${HERE}/usr/bin:${PATH}"
exec "${HERE}/usr/bin/EdgeTTSGui/EdgeTTSGui" "$@"
EOF
chmod 755 "$APPDIR/AppRun" "$APPDIR/usr/bin/EdgeTTSGui/EdgeTTSGui"

TOOL_DIR="$ROOT/build/appimagetool"
mkdir -p "$TOOL_DIR"
TOOL_APPIMAGE="$TOOL_DIR/appimagetool-${APPIMAGE_ARCH}.AppImage"
if [[ ! -x "$TOOL_APPIMAGE" ]]; then
  curl -fsSL -o "$TOOL_APPIMAGE" \
    "https://github.com/AppImage/appimagetool/releases/download/continuous/appimagetool-${APPIMAGE_ARCH}.AppImage"
  chmod +x "$TOOL_APPIMAGE"
fi
EXTRACT="$TOOL_DIR/squashfs-root"
rm -rf "$EXTRACT"
(
  cd "$TOOL_DIR"
  export APPIMAGE_EXTRACT_AND_RUN=1
  ./$(basename "$TOOL_APPIMAGE") --appimage-extract
)
APPIMAGE_OUT="$ROOT/dist/EdgeTTSGui-linux-${APPIMAGE_ARCH}.AppImage"
rm -f "$APPIMAGE_OUT"
export APPIMAGE_EXTRACT_AND_RUN=1
ARCH="$APPIMAGE_ARCH" "$EXTRACT/AppRun" "$APPDIR" "$APPIMAGE_OUT"
chmod 755 "$APPIMAGE_OUT"
echo "Wrote $APPIMAGE_OUT"
