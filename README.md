# Edge TTS 语音合成助手

**中文** · [English](README.en.md)

<p align="center">
  <strong>把文字变成清晰、自然的声音。</strong><br>
  一款打磨过的开源桌面客户端，基于微软 Edge 在线语音合成。
</p>

<p align="center">
  <a href="https://github.com/JJosephph/ms-edge-tts-gui/releases"><img src="https://img.shields.io/github/v/release/JJosephph/ms-edge-tts-gui?display_name=tag&sort=semver&color=5A8CFF" alt="Release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-61D69C.svg" alt="MIT License"></a>
  <img src="https://img.shields.io/badge/Python-3.10%2B-356FEB.svg" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-5A8CFF.svg" alt="Windows, macOS, Linux">
  <a href="https://github.com/JJosephph/ms-edge-tts-gui/stargazers"><img src="https://img.shields.io/github/stars/JJosephph/ms-edge-tts-gui?style=flat&color=F6C66C" alt="GitHub stars"></a>
</p>

<p align="center">
  <a href="#下载与使用">下载</a> ·
  <a href="#从源码启动">源码启动</a> ·
  <a href="#网络与代理">网络与代理</a> ·
  <a href="#构建与发布">构建</a>
</p>

---

## ⭐ 求点赞 · 请先读我

> 本项目 **免费、开源（MIT License）**，版权归 **mgface** 所有。
> 仓库地址：https://github.com/JJosephph/ms-edge-tts-gui
> 如果你觉得这个工具对你有帮助，请先到仓库点一个 **Star**，让更多用户能找到它；使用中遇到问题，欢迎提交 [Issue](https://github.com/JJosephph/ms-edge-tts-gui/issues) 或 PR。

---

**Edge TTS 语音合成助手**是一款免费、开源的桌面软件（Windows / macOS / Linux，MIT License，版权归 mgface 所有）。将文章、笔记、脚本等文字合成为自然的 MP3 音频，不需要 API Key。它支持**导入文件 · 逐页旁白配音**（工作助手模式）与**时间轴 JSON + 试听逐句高亮**（保存时自动打包 ZIP），并提供**语言 → 性别 → 音色**三级语音选择，几百个音色不再大海捞针。界面可随时切换中文和 English，适合全世界用户。

- **生成、试听与保存**：一键生成全文音频；生成后可随时“试听”或“保存下载”，无需重复合成。
- **实时进度**：生成时显示近似 `0–100%` 进度，完成后进度条保持 100%。
- **时间轴 JSON + 试听高亮**：主界面勾选后，保存/下载时自动打包 ZIP（内含 MP3 与同名 `.timeline.json`，每句起止秒数）；试听时正在朗读的句子会在文章中实时高亮。
- **网络保护**：生成前检测服务连接和代理环境变量；长时间无音频数据时会提示重试。
- **三级语音选择**：语音一次性从远端拉取后在本地按 **语言 → 性别 → 音色** 分组（内置分组引擎），不用再大海捞针；默认保留 `en-US-AndrewMultilingualNeural`（英语男声），可随时自选。
- **音色自然丰富**：支持几百种语言、数百个音色，男声、女声都非常丰富；无论中文、粤语、英语还是其他外语，都是十分自然的 TTS 朗读，不是机器音——用过 Edge 朗读功能的人都懂。
- **兼容原工作流**：默认 `en-US-AndrewMultilingualNeural`，语速 `+0%`、音量 `+0%`、音调 `+0Hz`；「恢复初始设置」可一键还原。
- **不占空间**：生成的音频只保存在一个临时 MP3 里，可自定义目录、打开或清理，关闭软件时自动删除。
- **导入文件 · 逐页旁白配音**：直接导入 `txt / md / docx / pdf`，自动拆分成多页；每页可写“备注”（不朗读，随导出 JSON 保存）；点「逐页配音」按页顺序一次合成，每页一个 MP3，之后逐页试听，保存时自动打包 ZIP（每页 MP3 + `pages.json`）。

### 中文界面预览

<p align="center">
  <img src="assets/ui-preview-zh.png" alt="中文界面预览" width="900">
</p>

### 亮点功能：时间轴 JSON + 试听逐句高亮

这是本工具最值得一试的功能。在主界面勾选「时间轴 JSON + 试听高亮」后：

- **保存即打包 ZIP**：点击「保存下载」时，自动生成一个 ZIP 压缩包，里面同时包含 MP3 和同名 `.timeline.json`——每句话的起止秒数清清楚楚，不用手动配对；
- **试听实时高亮**：点击「试听」后，正在朗读的句子会在原文中逐句点亮，像 K 歌字幕一样跟着进度走，跟读复习特别方便；
- **精准且零额外合成**：MP3 与时间轴在同一次请求中生成，时间轴直接使用微软 TTS 返回的句级边界，**不需要再次合成**，纯本地保存、完全免费、无需 API Key。

<p align="center">
  <img src="assets/ui-timeline-help.png" alt="时间轴 JSON 帮助弹窗（含示例与高亮演示）" width="540">
  <img src="assets/ui-timeline-highlight.png" alt="试听逐句高亮演示" width="540">
</p>

`.timeline.json` 内容示例：

```json
{
  "boundary": "SentenceBoundary",
  "sentences": [
    { "index": 0, "text": "你好，欢迎使用 Edge TTS 语音合成助手。", "start": 0.00, "end": 3.12 },
    { "index": 1, "text": "时间轴来自微软 TTS 的句级边界，无需二次合成。", "start": 3.12, "end": 6.80 }
  ]
}
```

> 适用场景：视频字幕、剪辑对齐、外语跟读、逐句复习、播客文稿等。

### 亮点功能：导入文件 · 逐页旁白配音（工作助手模式）

把文档**逐页拆开、逐页配音、备注存档**一气呵成：

1. 点「**导入文件**」选择 `txt / md / docx / pdf`，文档自动拆成多页，正文区下方出现分页工具条（上一页 / 下一页 + 页码 + 备注框）；
2. 每页正文会朗读，备注**不朗读**（可写旁白说明、字幕提示、剪辑备注等），编辑正文或备注都会自动保存回页面；
3. 点「**生成音频**」合成当前页，或点「**逐页配音**」按顺序把全部页面一次合成，进度显示“第 X/N 页”；
4. 完成后各页可随时**试听**（无需重新合成），点「**保存下载**」自动打包为 ZIP：每页一个 `page_001.mp3`… + `pages.json`；
5. `pages.json` 记录每页文本、备注与逐句时间轴，适合视频剪辑、旁白配音、工作助理等场景。

```text
pages_archive.zip
├── page_001.mp3
├── page_002.mp3
├── …
└── pages.json   # { pages: [ { index, text, note, audio, timeline } ] }
```

## 下载与使用

1. 在 [Releases](https://github.com/JJosephph/ms-edge-tts-gui/releases) 按系统下载：Windows 用 `EdgeTTSGui-Setup.exe`，Apple 芯片 Mac 用 `EdgeTTSGui-macOS-arm64.dmg`，Linux 用 `.deb` 或 AppImage。
2. 各平台安装包均已内置 Python 运行环境，无需另行安装 Python。
3. 粘贴文章、选择语音、调整语速 / 音量 / 音调，点击“生成音频”合成一次；之后点“试听”播放，或点“保存下载”导出 MP3，全程无需重复合成。
4. Windows 安装包会标明“免费 · 开源（MIT License）”，支持从“设置 → 应用”或安装目录中的 `unins000.exe` 卸载。macOS 首次打开若被拦截，请在访达中右键 App 选择“打开”。

| 安装包 | 说明 | 适合 | 备注 |
| --- | --- | --- | --- |
| `EdgeTTSGui-Setup.exe` | Windows 安装包（Inno Setup） | 大多数 Windows 用户 | 中英双语向导；可选安装目录与桌面快捷方式；支持完整卸载 |
| `EdgeTTSGui-Portable.exe` | Windows 单文件便携版 | 免安装 / 随身携带 | 运行时已打包，双击即可；体积最大 |
| `EdgeTTSGui-macOS-arm64.dmg` | macOS 磁盘映像 | Apple 芯片 Mac | 将 `EdgeTTSGui.app` 拖入“应用程序”。因未做 Apple 公证，首次启动可能需要**右键 → 打开** |
| `EdgeTTSGui-linux-amd64.deb` | Debian / Ubuntu 安装包 | 大多数 Linux 桌面 | 安装到 `/opt/EdgeTTSGui`，并添加菜单快捷方式 |
| `EdgeTTSGui-linux-x86_64.AppImage` | Linux 便携包 | 跨发行版 / 免安装 | `chmod +x` 后双击或在终端运行 |

**该下哪个？** Windows 一般选 `EdgeTTSGui-Setup.exe`。较新的 Mac 选 DMG。Linux 若是 Debian/Ubuntu 选 `.deb`，否则选 AppImage。

所有安装包均为 **免费开源（MIT License）**，版权归 **mgface** 所有。

## 从源码启动

入口是 `src/edgettsgui/__main__.py`。在仓库根目录执行：

```bash
git clone https://github.com/JJosephph/ms-edge-tts-gui.git
cd ms-edge-tts-gui

make run
```

已有虚拟环境时也可以：

```bash
PYTHONPATH=src python -m edgettsgui
```

不要单独运行 `src/edgettsgui/ui/app.py`，包路径对不上时相对导入会失败。

## 使用步骤

1. 把文字粘贴到编辑区。
2. 在语音面板按 **语言 → 性别 → 音色** 选择；默认是英语男声 `en-US-AndrewMultilingualNeural`，可随时点「恢复初始设置」。
3. 按需调整语速、音量和音调。
4. 点「生成音频」合成一次全文。
5. 生成后点「试听」播放，或点「保存下载」导出 MP3，两者都复用已生成音频，无需再合成。
6. 生成过程中看状态栏和进度条；完成后进度条保持 100%。

### 工作助手模式：导入文件并逐页配音

1. 点「导入文件」选择 `txt / md / docx / pdf`。软件会把文档拆成多页，并显示分页工具条。
2. 正文会被朗读；「备注」不会朗读，适合写旁白说明或剪辑备注。
3. 点「生成音频」只合成当前页，或点「逐页配音」按顺序合成全书（进度显示第 X/N 页）。
4. 之后「试听」预览当前页，「保存下载」打出一个 ZIP：每页一个 MP3，外加记录文本、备注和逐句时间轴的 `pages.json`。

## 网络与代理

Edge TTS 是在线服务。软件会探测 Edge 语音端点是否可达，并读取常见代理环境变量：

```text
HTTPS_PROXY   HTTP_PROXY   ALL_PROXY
https_proxy   http_proxy   all_proxy
```

连不上服务时，活动日志会说明原因。如果生成卡住（3 分钟没有新的音频数据），会弹出恢复对话框：

- **继续等待** — 适合短暂变慢的网络；
- **重试** — 重新开始当前合成（最多三次）；
- **取消** — 停止任务并删除不完整文件。

## 生成音频缓存与磁盘占用

生成的音频刻意设计成不会堆积：

- 默认位置是操作系统临时目录。
- 只复用一个文件：`edge_tts_preview.mp3`。
- 每次重新生成都会覆盖它。
- 退出软件时自动删除。
- 可在 **⚙ 设置** 里改缓存目录、打开目录，或立刻清空。

保存时会把 MP3 复制到你选择的位置；软件关闭后不会保留缓存文件本身。

## 卸载

- Windows：**设置 → 应用 → 已安装的应用**，找到 **Edge TTS 语音合成助手**，点卸载；或运行安装目录里的 `unins000.exe`（例如 `C:\Program Files\EdgeTTSGui\unins000.exe`）。
- Linux：`sudo apt remove edgettsgui` 卸载 `.deb`。AppImage 是单个文件，直接删除即可。
- macOS：把「应用程序」里的 `EdgeTTSGui.app` 拖到废纸篓。

## 默认值与推荐音色

兼容预设如下：

```text
Voice:   en-US-AndrewMultilingualNeural
Rate:    +0%
Volume:  +0%
Pitch:   +0Hz
```

相关 RPA 工作流的用户可以直接开始合成，不必重填设置；点「恢复初始设置」会回到这一组。中文女声可选：中文 → 女声 → 晓晓（`zh-CN-XiaoxiaoNeural`）。

## 项目结构

```text
ms-edge-tts-gui/
├── src/edgettsgui/              # 应用包
│   ├── config.py                # 版本、主题、设置路径、默认语音
│   ├── i18n.py                  # 界面文案与日志本地化
│   ├── tts/engine.py            # Edge TTS 流式合成、网络探测、卡住恢复
│   ├── documents/               # 文本清洗 + 文件导入 / 分页
│   ├── voices/groups.py         # 语言 → 性别 → 音色分组
│   └── ui/app.py                # 桌面窗口与交互
├── tests/                       # 单元测试
├── assets/                      # 图标与 README 界面预览
├── installer/                   # Windows Inno Setup + Linux .desktop
├── scripts/                     # windows.bat / macos.sh / linux.sh
├── Makefile                     # make run / test / windows / macos / linux
├── README.md                    # 中文说明
├── README.en.md                 # English guide
└── .github/workflows/           # 打 tag 后自动发三端安装包
```

## 构建与发布

```bash
make windows    # Windows Setup / Portable（需在 Windows 上）
make macos      # Apple Silicon DMG（需在 macOS 上）
make linux      # .deb + AppImage（需在 Linux 上）
```

Windows 产物：

```text
dist\EdgeTTSGui\EdgeTTSGui.exe
dist\EdgeTTSGui-Portable.exe
dist\EdgeTTSGui-Setup.exe
```

macOS 产物是 `dist/EdgeTTSGui-macOS-<arch>.dmg`。Linux 产物是 `dist/EdgeTTSGui-linux-amd64.deb` 和 `dist/EdgeTTSGui-linux-x86_64.AppImage`。打包脚本在 `scripts/`。

### GitHub 自动发布

推送匹配 `v*` 的版本 tag 会跑 `.github/workflows/build-release.yml`，构建并上传：

- Windows：目录启动器、便携 EXE、Inno Setup 安装包
- macOS：Apple Silicon DMG
- Linux：`.deb` 和 AppImage（在 Ubuntu 22.04 上构建，兼容 glibc）

```bash
git tag v1.4.0
git push origin v1.4.0
```

## 隐私与服务说明

- 文字只会发送给微软 Edge 在线语音服务，用于合成你请求的音频。
- 本软件不需要 API Key，也不会额外上报遥测。
- 本项目与微软没有从属或背书关系。
- 请按适用的服务条款和当地法律使用在线语音。

## 参与贡献

欢迎提交 Issue、功能建议和 Pull Request。如果这个项目帮到你，请考虑在 GitHub 上点一个 **Star**，方便更多人发现它。

## 许可证

以 [MIT License](LICENSE) 发布 · 中文译文见 [LICENSE.zh.txt](LICENSE.zh.txt)。

- **版权所有：** mgface
- **仓库：** https://github.com/JJosephph/ms-edge-tts-gui
