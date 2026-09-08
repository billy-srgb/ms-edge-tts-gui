# -*- coding: utf-8 -*-
"""界面文案与活动日志本地化。"""

from __future__ import annotations

import re

TRANSLATIONS = {
        "app": {"zh": "Edge TTS 语音合成助手", "en": "Edge TTS Voice Studio"},
        "open": {"zh": "开源 · MIT License", "en": "Open Source · MIT License"},
        "open_badge": {"zh": "免费 · 开源", "en": "Free · Open Source"},
        "github_repo": {"zh": "GitHub 仓库", "en": "GitHub"},
        "github_star": {"zh": "GitHub 点赞", "en": "Star on GitHub"},
        "settings_short": {"zh": "设置", "en": "Settings"},
        "repo": {"zh": "GitHub 仓库 ↗", "en": "GitHub Repo ↗"},
        "star": {"zh": "⭐ 去 GitHub 点 Star", "en": "⭐ Star on GitHub"},
        "developer": {"zh": "开发者", "en": "Developer"},
        "language": {"zh": "EN", "en": "中文"},
        "settings": {"zh": "设置", "en": "Settings"},
        "theme_dark": {"zh": "夜间", "en": "Dark"},
        "theme_light": {"zh": "白天", "en": "Light"},
        "tagline": {"zh": "让文字成为清晰、自然的声音", "en": "Turn text into clear, natural voice"},
        "voice_deck": {"zh": "VOICE DECK", "en": "VOICE DECK"},
        "composer": {"zh": "COMPOSER", "en": "COMPOSER"},
        "checking": {"zh": "●  检测中…", "en": "●  Checking network…"},
        "check_network": {"zh": "检测网络", "en": "Check network"},
        "network_ok": {"zh": "●  网络正常（{latency:.0f} ms）", "en": "●  Network OK ({latency:.0f} ms)"},
        "network_bad": {"zh": "●  网络异常", "en": "●  Network unavailable"},
        "article": {"zh": "文章内容", "en": "Article"},
        "count": {"zh": "字数：{count}", "en": "Characters: {count}"},
        "helper": {"zh": "支持 Markdown / 纯文本；可导入 txt / md / docx / pdf 逐页旁白配音，一次生成，随时试听或保存下载。", "en": "Markdown & plain text supported; import txt / md / docx / pdf for page-by-page narration - synthesize once, then play or save anytime."},
        "voice": {"zh": "语音", "en": "Voice"},
        "lang": {"zh": "语言", "en": "Language"},
        "gender": {"zh": "性别", "en": "Gender"},
        "gender_all": {"zh": "全部", "en": "All"},
        "gender_female": {"zh": "女声", "en": "Female"},
        "gender_male": {"zh": "男声", "en": "Male"},
        "gender_other": {"zh": "其他", "en": "Other"},
        "timeline": {"zh": "时间轴 JSON + 试听高亮", "en": "Timeline JSON + highlight"},
        "timeline_help_title": {"zh": "时间轴 JSON 与试听高亮", "en": "Timeline JSON & Playback Highlight"},
        "timeline_help_desc": {"zh": "开启后：① 保存/下载音频时，自动打包成 ZIP（内含 MP3 与同名 .timeline.json，记录每句起止秒数）；② 试听播放时，正在朗读的句子会在文章中实时高亮。时间轴与音频在同一次合成中生成，直接使用微软 TTS 返回的句级边界，无需再次合成。", "en": "When enabled: 1) saving/downloading bundles the MP3 and a .timeline.json (each sentence's start/end seconds) into one ZIP; 2) during playback, the sentence being read is highlighted live. Audio and timeline are produced in the same synthesis using Microsoft TTS sentence-boundary metadata - no re-rendering needed."},
        "timeline_help_json_title": {"zh": "示例 .timeline.json", "en": "Example .timeline.json"},
        "timeline_help_highlight_title": {"zh": "高亮演示（试听时实时跟随）", "en": "Highlight demo (follows live during playback)"},
        "timeline_help_demo_btn": {"zh": "▶ 演示高亮", "en": "▶ Demo highlight"},
        "timeline_help_demo_text": {"zh": "第一句：大家好，欢迎使用本工具。第二句：这一句正在被高亮显示。第三句：播放到哪一句，哪一句就会亮起来。", "en": "First sentence: welcome to this tool. Second sentence: this sentence is now highlighted. Third sentence: the sentence being spoken lights up."},
        "timeline_help_note": {"zh": "提示：高亮在点击「试听」后开始，随播放进度逐句跳转；保存时音频与时间轴 JSON 会打包成 ZIP 存到你选择的目录。", "en": "Tip: highlighting starts when you click Play and follows the progress; the audio and timeline JSON are saved together as a ZIP."},
        "timeline_on": {"zh": "已开启：保存时打包 ZIP（音频 + 时间轴 JSON），试听时高亮当前句子", "en": "On: saves a ZIP bundle (audio + timeline JSON); highlights the sentence being read"},
        "timeline_off": {"zh": "已关闭：不再输出时间轴 JSON 与试听高亮", "en": "Off: no timeline JSON or playback highlight"},

        "search": {"zh": "搜索语音，如：晓晓 / Andrew…", "en": "Search voices, e.g. Xiaoxiao / Andrew…"},
        "voices_load_error": {"zh": "语音列表加载失败，请检查网络后点 ↻ 重试", "en": "Could not load the voice list - check network and click ↻ to retry"},
        "voices_reloading": {"zh": "正在重新加载语音列表…", "en": "Reloading voice list…"},
        "voices_loaded": {"zh": "已加载语音（{count} 个，{langs} 种语言）", "en": "Voices loaded ({count} voices, {langs} languages)"},
        "original": {"zh": "原工作流默认：Andrew Multilingual · 语速 +0% · 音量 +0% · 音调 +0Hz", "en": "Original workflow: Andrew Multilingual · rate +0% · volume +0% · pitch +0Hz"},
        "restore": {"zh": "恢复初始设置", "en": "Restore defaults"},
        "reset_compact": {"zh": "恢复", "en": "Reset"},
        "rate": {"zh": "语速", "en": "Rate"},
        "volume": {"zh": "音量", "en": "Volume"},
        "pitch": {"zh": "音调", "en": "Pitch"},
        "ready": {"zh": "就绪", "en": "Ready"},
        "generate": {"zh": "生成音频", "en": "Generate Audio"},
        "play": {"zh": "▶ 试听", "en": "▶ Play"},
        "save": {"zh": "保存下载", "en": "Save Audio"},
        "generated_ok": {"zh": "已生成 ✔ 可试听 / 保存", "en": "Generated ✔ Play or save"},
        "canceled": {"zh": "已取消", "en": "Canceled"},
        "failed": {"zh": "失败 ✖", "en": "Failed ✖"},
        "stopped": {"zh": "已停止", "en": "Stopped"},
        "no_audio": {"zh": "请先点击“生成音频”生成一段音频。", "en": "Please click “Generate Audio” first."},
        "stop": {"zh": "停止", "en": "Stop"},
        "log": {"zh": "活动日志", "en": "Activity log"},
        "footer": {"zh": "免费开源软件 · MIT License · Powered by Microsoft Edge TTS", "en": "Free open-source software · MIT License · Powered by Microsoft Edge TTS"},
        "repository": {"zh": "仓库：", "en": "Repo: "},
        "empty": {"zh": "请输入文章内容。", "en": "Please enter some article text."},
        "import_file": {"zh": "导入文件", "en": "Import File"},
        "page_dub": {"zh": "逐页配音", "en": "Dub All Pages"},
        "page_label": {"zh": "第 {current}/{total} 页", "en": "Page {current}/{total}"},
        "page_note": {"zh": "备注", "en": "Note"},
        "page_note_hint": {"zh": "备注不朗读，随 pages.json 一并导出", "en": "Note is not spoken; exported with pages.json"},
        "prev_page": {"zh": "‹ 上一页", "en": "‹ Prev"},
        "next_page": {"zh": "下一页 ›", "en": "Next ›"},
        "no_pages": {"zh": "请先点击“导入文件”导入文档进行分页。", "en": "Please import a file first to create pages."},
        "pages_zip_title": {"zh": "保存分页配音压缩包（音频 + pages.json + 备注）", "en": "Save page dubbing bundle (audio + pages.json + notes)"},
        "pages_zip_filetype": {"zh": "ZIP 压缩包（每页 MP3 + pages.json）", "en": "ZIP bundle (per-page MP3 + pages.json)"},
    }


def translate(language: str, key: str, **kwargs) -> str:
    value = TRANSLATIONS[key][language]
    return value.format(**kwargs) if kwargs else value


def localize_log_message(language: str, message: str) -> str:
    if language != "en":
        return message
    match = re.fullmatch(r"开始第 (\d+) 次生成（语音：(.*)）", message)
    if match:
        return f"Starting synthesis attempt {match.group(1)} (voice: {match.group(2)})"
    exact = {
        "音频数据接收完成。": "Audio data received.",
        "任务已取消。": "Task canceled.",
        "准备重试…": "Preparing retry…",
        "开始检测网络…": "Checking network…",
        "网络检测通过": "Network check passed.",
        "生成音频缓存已清理。": "Generated audio cache cleared.",
        "[任务] 正在停止…": "[Task] Stopping…",
        "[任务] 已取消。": "[Task] Canceled.",
    }
    if message in exact:
        return exact[message]
    proxy_match = re.fullmatch(r"\u7f51\u7edc\u68c0\u6d4b\u901a\u8fc7\uff08\u4ee3\u7406\uff1a(.*)\uff09", message)
    if proxy_match:
        return f"Network check passed (proxy: {proxy_match.group(1)})."

    substitutions = [
        (r"^\[语音\] 已加载 (\d+) 个可用语音$", r"[Voice] Loaded \1 available voices"),
        (r"^\[语音\] 加载语音列表失败：(.*)$", r"[Voice] Could not load voice list: \1"),
        (r"^\[生成\] 开始合成全文音频（(\d+) 字）$", r"[Generate] Synthesizing full audio (\1 characters)"),
        (r"^\[生成\] 开始合成第 (\d+) 页音频（(\d+) 字）$", r"[Generate] Synthesizing page \1 audio (\2 characters)"),
        (r"^\[导入\] 已导入 (\d+) 页：(.+)$", r"[Import] Imported \1 page(s): \2"),
        (r"^\[导入\] 导入失败：(.*)$", r"[Import] Import failed: \1"),
        (r"^\[分页\] 开始逐页配音（共 (\d+) 页）$", r"[Pages] Starting page-by-page dubbing (\1 pages)"),
        (r"^\[分页\] 第 (\d+)/(\d+) 页完成（(.+) KB）。$", r"[Pages] Page \1/\2 done (\3 KB)."),
        (r"^\[分页\] 第 (\d+)/(\d+) 页无可用文字，已跳过。$", r"[Pages] Page \1/\2 has no readable text; skipped."),
        (r"^\[分页\] 第 (\d+)/(\d+) 页生成失败：(.*)$", r"[Pages] Page \1/\2 failed: \3"),
        (r"^\[分页\] 逐页配音完成：(\d+) 页，可试听或保存下载。$", r"[Pages] Dubbing complete: \1 pages. Play or save anytime."),
        (r"^\[分页\] 已停止（完成 (\d+) 页）。$", r"[Pages] Stopped (\1 page(s) done)."),
        (r"^\[分页\] 未生成任何页面音频。$", r"[Pages] No page audio was generated."),
        (r"^\[保存\] 分页配音压缩包已保存：(.*)$", r"[Save] Page bundle saved: \1"),
        (r"^\[生成\] 音频已生成：(.*)$", r"[Generate] Audio ready: \1"),
        (r"^\[生成\] 生成期间文本已修改，请重新生成。$", r"[Generate] Text changed during generation. Please generate again."),
        (r"^\[试听\] 开始播放已生成的音频…$", r"[Play] Playing generated audio…"),
        (r"^\[试听\] 已停止播放。$", r"[Play] Playback stopped."),
        (r"^\[保存\] 音频已保存：(.*)$", r"[Save] Audio saved: \1"),
        (r"^\[保存\] 时间轴 JSON 已保存：(.*)$", r"[Save] Timeline JSON saved: \1"),
        (r"^\[警告\] 时间轴 JSON 保存失败：(.*)$", r"[Warning] Could not save timeline JSON: \1"),
        (r"^\[任务\] 失败：(.*)$", r"[Task] Failed: \1"),
        (r"^\[网络\] 不可达，检测到代理 (.*)，可能是网络不通或代理设置不正确。$", r"[Network] Unreachable; proxy detected: \1. Check the connection or proxy configuration."),
        (r"^\[网络\] 不可达（(.*)）。生成可能很慢或失败，建议检查网络后重试。$", r"[Network] Unreachable (\1). Synthesis may be slow or fail; check your network and retry."),
        (r"^\[网络\] SSL 证书校验失败（(.*)）。这通常是本机 Python 缺少系统证书，不是网络断开。macOS 请运行「Install Certificates.command」，或检查是否使用了会解密 HTTPS 的代理。$", r"[Network] SSL certificate verification failed (\1). This is usually a missing local CA bundle, not a downed network. On macOS run Install Certificates.command, or check for an HTTPS-inspecting proxy."),
        (r"^\[警告\] 生成失败：(.*)（可能是网络不通或代理设置不正确）$", r"[Warning] Synthesis failed: \1 (network or proxy may be unavailable or misconfigured)"),
        (r"^\[警告\] 生成失败：(.*)（SSL 证书校验失败（常见于 macOS 官方 Python 未安装证书））$", r"[Warning] Synthesis failed: \1 (SSL certificate verification failed; common on official macOS Python without certificates installed)"),
    ]
    for pattern, replacement in substitutions:
        localized = re.sub(pattern, replacement, message)
        if localized != message:
            return localized
    return message


def localize_stall_message(language: str, message: str) -> str:
    if language != "en":
        return message
    if "长时间没有收到新的音频数据" in message:
        return (
            "No new audio data has arrived for a while. Your network connection "
            "or proxy may be unavailable or misconfigured. Would you like to retry?"
        )
    if "SSL 证书校验失败" in message:
        return (
            "SSL certificate verification failed (common on official macOS Python "
            "without certificates installed). Would you like to retry?"
        )
    if "网络不通或代理设置不正确" in message:
        return "Your network connection or proxy may be unavailable or misconfigured. Would you like to retry?"
    return message
