# -*- coding: utf-8 -*-
"""Edge TTS 语音合成助手 — 应用包。

分层
----
config      版本、路径、主题、默认语音
i18n        界面文案与日志本地化
tts         Edge TTS 合成、网络探测、卡住恢复
documents   文本清洗、文件导入与分页
voices      语言 → 性别 → 音色分组
ui          桌面窗口与交互
"""

from edgettsgui.config import APP_VERSION

__all__ = ["APP_VERSION"]
