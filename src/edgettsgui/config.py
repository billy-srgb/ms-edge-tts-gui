# -*- coding: utf-8 -*-
"""应用级常量：产品信息、主题、用户目录、默认语音。"""

from __future__ import annotations

import os
import sys
from pathlib import Path

APP_NAME = "Edge TTS 语音合成助手"
APP_VERSION = "1.4.0"
DEVELOPER = "WangYufan"
DEVELOPER_QQ = "1471056247"
REPOSITORY_URL = "https://github.com/JJosephph/ms-edge-tts-gui"
REPOSITORY_DISPLAY = "github.com/JJosephph/ms-edge-tts-gui"


def ui_font_family() -> str:
    if sys.platform == "darwin":
        return "PingFang SC"
    if sys.platform.startswith("linux"):
        return "Noto Sans CJK SC"
    return "Microsoft YaHei UI"


def settings_dir() -> Path:
    if sys.platform == "win32":
        return Path(os.environ.get("APPDATA", Path.home())) / "EdgeTTSGui"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "EdgeTTSGui"
    xdg = os.environ.get("XDG_CONFIG_HOME")
    return (Path(xdg) if xdg else Path.home() / ".config") / "EdgeTTSGui"


UI_FONT_FAMILY = ui_font_family()
SETTINGS_DIR = settings_dir()
SETTINGS_FILE = SETTINGS_DIR / "settings.json"
PREVIEW_FILENAME = "edge_tts_preview.mp3"

THEMES = {
    "dark": {
        "app_bg": "#09111F", "surface": "#111D31", "surface_alt": "#0D1728",
        "card": "#14223A", "card_raised": "#182944", "border": "#263B5C",
        "text": "#F2F6FF", "muted": "#91A4C3", "primary": "#5A8CFF",
        "primary_hover": "#4777E6", "accent": "#73D7FF", "success": "#61D69C",
        "warning": "#F6C66C", "danger": "#F47D92", "star": "#4A3B16",
        "star_hover": "#5D4B1D", "field": "#0A1322", "log": "#09121F",
    },
    "light": {
        "app_bg": "#EEF3FA", "surface": "#FFFFFF", "surface_alt": "#E6EEF9",
        "card": "#FFFFFF", "card_raised": "#F7FAFF", "border": "#CAD8EB",
        "text": "#17233A", "muted": "#61718D", "primary": "#356FEB",
        "primary_hover": "#285BCA", "accent": "#0B89C8", "success": "#168B57",
        "warning": "#A66A00", "danger": "#C33D56", "star": "#FFF3D6",
        "star_hover": "#F8E1A7", "field": "#F8FBFF", "log": "#F7FAFE",
    },
}

DEFAULT_VOICE = "en-US-AndrewMultilingualNeural"
DEFAULT_RATE = 0
DEFAULT_VOLUME = 0
DEFAULT_PITCH = 0
