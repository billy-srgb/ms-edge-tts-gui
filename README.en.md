# Edge TTS Voice Studio

[中文](README.md) · **English**

<p align="center">
  <strong>Turn text into clear, natural voice.</strong><br>
  A polished, open-source desktop client for Microsoft Edge Text-to-Speech.
</p>

<p align="center">
  <a href="https://github.com/JJosephph/ms-edge-tts-gui/releases"><img src="https://img.shields.io/github/v/release/JJosephph/ms-edge-tts-gui?display_name=tag&sort=semver&color=5A8CFF" alt="Release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-61D69C.svg" alt="MIT License"></a>
  <img src="https://img.shields.io/badge/Python-3.10%2B-356FEB.svg" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-5A8CFF.svg" alt="Windows, macOS, Linux">
  <a href="https://github.com/JJosephph/ms-edge-tts-gui/stargazers"><img src="https://img.shields.io/github/stars/JJosephph/ms-edge-tts-gui?style=flat&color=F6C66C" alt="GitHub stars"></a>
</p>

<p align="center">
  <a href="#downloads">Downloads</a> ·
  <a href="#run-from-source">Run from source</a> ·
  <a href="#network-and-proxy">Network &amp; proxy</a> ·
  <a href="#build-and-release">Build</a>
</p>

---

## ⭐ Star Us · Please Read First

> This project is **free and open source (MIT License)**. Copyright belongs to **mgface**.
> Repository: https://github.com/JJosephph/ms-edge-tts-gui
> If this tool helps you, please **Star** the repository first so more users can discover it; issues and pull requests are welcome.

---

**Edge TTS Voice Studio** is a modern desktop application (Windows / macOS / Linux) for turning articles, notes, scripts, documentation, and other text into high-quality MP3 audio. It is powered by the open-source [`edge-tts`](https://github.com/rany2/edge-tts) library and Microsoft Edge online voices—**no API key is required**. It is **free and open source under the MIT License**. Copyright belongs to **mgface**.

The project is designed as a general-purpose open-source tool. It features an **Import & page-by-page dubbing** work-assistant mode (txt / md / docx / pdf), a **Timeline JSON + live sentence highlight** mode (Save bundles the MP3 and timeline into one ZIP), and a **Language → Gender → Voice** cascading voice picker across hundreds of voices. It also includes practical safeguards for real-world network conditions: service reachability checks, proxy-aware diagnostics, retry controls, and a stalled-generation prompt.

## Interface Preview

<p align="center">
  <img src="assets/ui-preview-dark.png" alt="Dark theme preview" width="900">
</p>

<p align="center">
  <sub>Night theme · Composer + Voice Deck workflow</sub>
</p>

<p align="center">
  <img src="assets/ui-preview-light.png" alt="Light theme preview" width="900">
</p>

<p align="center">
  <sub>Day theme · Same focused layout, optimized for bright environments</sub>
</p>

## Features

| Area | What it provides |
| --- | --- |
| **Text to MP3** | Paste Markdown, plain text, or HTML-derived text and export a full MP3 file. |
| **Import & page-by-page dubbing** | Import `txt / md / docx / pdf`; the document is auto-split into pages with a page toolbar (prev / next + page number + a per-page **note** that is never spoken). **Dub All Pages** synthesizes every page in order with page-level progress, then Play previews the current page's audio and Save bundles each page MP3 plus `pages.json` (page text, notes, per-page sentence timeline) into one ZIP. |
| **Generate once, play & save** | Synthesize the full audio a single time, then Play or Save it anytime without re-rendering. |
| **Real progress** | Generation shows live, approximate `0–100%` progress plus received audio size; the bar stays at 100% when finished. |
| **Multi-level voice picker** | Voices are fetched once and grouped locally into **Language → Gender → Voice** (built-in grouping engine) — no more scrolling a giant list. Male/female voices are rich across hundreds of languages; Chinese, Cantonese, English and more all sound natural, never robotic. |
| **Original workflow compatibility** | Default settings mirror the existing RPA workflow: `en-US-AndrewMultilingualNeural`, rate `+0%`, volume `+0%`, pitch `+0Hz`. |
| **Timeline JSON + highlight** | Optional one-click toggle on the main UI: saving bundles the MP3 and a `.timeline.json` (each sentence's start/end seconds) into one ZIP, and during Play the sentence being read is highlighted live in the article. A " ? " help button shows a JSON example and a highlight demo. |
| **Restore defaults** | The voice-deck button resets voice to `en-US-AndrewMultilingualNeural` and rate/volume/pitch to `+0%`/`+0%`/`+0Hz` in one click. |
| **Recommended female voice** | `zh-CN-XiaoxiaoNeural` is prominently listed as a recommended Chinese female voice. |
| **Network protection** | Checks Edge TTS service availability and detects proxy environment variables before generation. |
| **Stall recovery** | If audio stops arriving, offers **Keep waiting**, **Retry**, or **Cancel** with a network/proxy explanation. |
| **Bilingual interface** | Toggle the desktop UI between **中文** and **English** at any time. English articles and international voices are fully supported. |
| **Day / night themes** | Switch between a bright reading-friendly theme and a focused dark workspace. |
| **Preview cache control** | Choose a preview cache folder, open it, or clear it immediately. Only one temporary preview MP3 is reused and it is deleted when the app closes. |

### ⭐ Key Feature: Timeline JSON + Live Sentence Highlight

The feature we are most proud of — enable the **Timeline JSON + highlight** toggle on the main UI:

- **Save = one ZIP**: clicking **Save Audio** produces a single ZIP that bundles the MP3 with its `.timeline.json` (start/end seconds for every sentence) — nothing to pair up by hand;
- **Live highlight while playing**: the sentence being read lights up in the article in real time, sentence by sentence — great for shadowing, subtitles and review;
- **Precise with no extra synthesis**: the MP3 and timeline are produced in the same request, using sentence-boundary metadata returned directly by Microsoft TTS. **No re-rendering** is needed; files are saved locally, free, with no API key.

<p align="center">
  <img src="assets/ui-timeline-help.png" alt="Timeline JSON help dialog (example + highlight demo)" width="540">
  <img src="assets/ui-timeline-highlight.png" alt="Live sentence highlight demo" width="540">
</p>

Example `.timeline.json`:

```json
{
  "boundary": "SentenceBoundary",
  "sentences": [
    { "index": 0, "text": "Hello, welcome to Edge TTS Voice Studio.", "start": 0.00, "end": 3.12 },
    { "index": 1, "text": "The timeline uses Microsoft TTS sentence boundaries, no re-render needed.", "start": 3.12, "end": 6.80 }
  ]
}
```

> Use cases: subtitles, video editing alignment, language shadowing, sentence-by-sentence review, podcast transcripts.

## Downloads

Open the [Releases](https://github.com/JJosephph/ms-edge-tts-gui/releases) page and choose the package that fits your use case:

| Package | What it is | Best for | Notes |
| --- | --- | --- | --- |
| `EdgeTTSGui-Setup.exe` | Windows installer (Inno Setup) | Most Windows users | Bilingual (中文/English) wizard that states **free & open source (MIT License)**; choose any drive/folder; desktop shortcut; **full uninstall support**. |
| `EdgeTTSGui-Portable.exe` | Windows single-file portable | Take-anywhere / no-install use | Python runtime and libraries bundled in one file; double-click to run; largest download. |
| `EdgeTTSGui-macOS-arm64.dmg` | macOS disk image | Apple Silicon Macs | Drag `EdgeTTSGui.app` into Applications. The first launch may require **Right-click → Open** because the DMG is not Apple-notarized. |
| `EdgeTTSGui-linux-amd64.deb` | Debian / Ubuntu installer | Most Linux desktops | Installs to `/opt/EdgeTTSGui` and adds a menu shortcut. |
| `EdgeTTSGui-linux-x86_64.AppImage` | Linux portable | Distro-agnostic / no-install use | `chmod +x` then double-click or run from a terminal. |

**Which one should I download?** On Windows, pick `EdgeTTSGui-Setup.exe` unless you want the portable EXE. On a recent Mac, pick the DMG. On Linux, pick the `.deb` if you use Debian/Ubuntu, otherwise the AppImage.

All packages are **free and open source (MIT License)**. Copyright belongs to **mgface**.

### Is Python included?

**Yes.** Published packages bundle the Python runtime and required libraries through PyInstaller. You can install or run the program without installing Python separately.

## Run from Source

The entry point is `src/edgettsgui/__main__.py`. From the repository root:

```bash
git clone https://github.com/JJosephph/ms-edge-tts-gui.git
cd ms-edge-tts-gui

make run
```

If the virtual environment already exists:

```bash
PYTHONPATH=src python -m edgettsgui
```

Do not run `src/edgettsgui/ui/app.py` by itself — relative imports fail when the package path is wrong.

## Using the App

1. **Paste your text** into the Composer panel.
2. **Choose a voice** from the Voice Deck — pick **Language**, then **Gender**, then the final **Voice** from the filtered list. The default is the English male voice `en-US-AndrewMultilingualNeural`; use **Restore defaults** at any time to reset voice and rate/volume/pitch.
3. **Adjust rate, volume, and pitch** if needed.
4. Click **Generate Audio** to synthesize the full text once.
5. After generation, click **▶ Play** to listen, or **Save Audio** to export the MP3 — both reuse the generated audio with no re-rendering.
6. Watch the status line and progress bar during generation; the bar stays at 100% when done.

### Work-Assistant Mode: Import a File and Dub It Page by Page

1. Click **Import File** and choose a `txt / md / docx / pdf`. The app splits the document into pages and shows the page toolbar.
2. Edit the page text freely (it is read aloud) and fill in the **Note** field (never spoken — handy for narration cues or editing remarks).
3. Click **Generate Audio** to synthesize just the current page, or **Dub All Pages** to synthesize the whole book in order (progress shows page X/N).
4. Afterwards, **Play** previews the current page and **Save Audio** produces a single ZIP: one MP3 per page plus `pages.json` with every page's text, note, and per-page sentence timeline — no re-rendering needed.

## Network and Proxy

Edge TTS is an online service. The application performs a reachability test against the Edge speech endpoint and reads common proxy variables:

```text
HTTPS_PROXY   HTTP_PROXY   ALL_PROXY
https_proxy   http_proxy   all_proxy
```

If the service cannot be reached, the app reports the condition in the Activity log. If a generation stalls (no new audio data for 3 minutes), it presents a recovery dialog:

- **Keep waiting** — for a short-lived slow connection;
- **Retry** — starts the current synthesis again (up to three attempts);
- **Cancel** — stops the task and removes the partial file.

## Generated Audio Cache and Disk Usage

Generated audio is deliberately designed not to accumulate:

- The default location is the operating system temporary folder.
- Only one file, `edge_tts_preview.mp3`, is reused for the generated audio.
- It is overwritten on every new generation.
- It is removed automatically when the application exits.
- Use **⚙ Settings** to set another cache folder, open it, or clear the generated audio immediately.

When you save, the MP3 is copied to the location you choose; the cache file itself is not kept after the app closes.

## Uninstall

The installed program can be uninstalled normally:

- Open **Windows Settings → Apps → Installed apps**, find **Edge TTS 语音合成助手**, and click **Uninstall**.
- Or run `unins000.exe` in the installation directory (for example `C:\Program Files\EdgeTTSGui\unins000.exe`).

The uninstaller removes the application files and shortcuts.

On Linux, remove the `.deb` install with `sudo apt remove edgettsgui`. The AppImage is just a file — delete it. On macOS, drag `EdgeTTSGui.app` from Applications to the Trash.

## Defaults and Voice Recommendations

The compatibility preset is intentionally explicit:

```text
Voice:   en-US-AndrewMultilingualNeural
Rate:    +0%
Volume:  +0%
Pitch:   +0Hz
```

This lets existing users of the related RPA workflow start synthesizing immediately without re-entering settings; the deck's **Restore defaults** button returns to this preset in one click. For a Chinese female voice, pick 中文 → 女声 → 晓晓 (`zh-CN-XiaoxiaoNeural`).

## Project Structure

```text
ms-edge-tts-gui/
├── src/edgettsgui/              # Application package
│   ├── config.py                # Version, themes, settings paths, defaults
│   ├── i18n.py                  # UI strings and log localization
│   ├── tts/engine.py            # Edge TTS streaming, network probe, stall recovery
│   ├── documents/               # Text cleanup + file import / pagination
│   ├── voices/groups.py         # Language → Gender → Voice grouping
│   └── ui/app.py                # Desktop window and user interactions
├── tests/                       # Unit tests
├── assets/                      # Icon and README interface previews
├── installer/                   # Windows Inno Setup + Linux .desktop
├── scripts/                     # windows.bat / macos.sh / linux.sh
├── Makefile                     # make run / test / windows / macos / linux
├── README.md                    # Chinese guide
├── README.en.md                 # English guide
└── .github/workflows/           # Tagged-release automation
```

## Build and Release

```bash
make windows    # Windows Setup / Portable (must run on Windows)
make macos      # Apple Silicon DMG (must run on macOS)
make linux      # .deb + AppImage (must run on Linux)
```

Windows produces:

```text
dist\EdgeTTSGui\EdgeTTSGui.exe
dist\EdgeTTSGui-Portable.exe
dist\EdgeTTSGui-Setup.exe
```

macOS produces `dist/EdgeTTSGui-macOS-<arch>.dmg`. Linux produces `dist/EdgeTTSGui-linux-amd64.deb` and `dist/EdgeTTSGui-linux-x86_64.AppImage`. The installer scripts live under `scripts/`.

### GitHub release automation

Pushing a version tag matching `v*` runs `.github/workflows/build-release.yml`. The workflow builds and uploads:

- Windows: directory launcher, portable EXE, Inno Setup installer
- macOS: Apple Silicon DMG
- Linux: `.deb` and AppImage (built on Ubuntu 22.04 for glibc compatibility)

```bash
git tag v1.4.0
git push origin v1.4.0
```

## Privacy and Service Notice

- Text is sent to Microsoft Edge’s online speech service only to synthesize the requested audio.
- This application does not require an API key and does not add its own telemetry service.
- The project is not affiliated with or endorsed by Microsoft.
- Please use online voices in accordance with the applicable service terms and local laws.

## Contributing

Issues, feature requests, and pull requests are welcome. If this project helps you, please consider giving it a **Star** on GitHub—it makes the project easier for other users to discover.

## License

Released under the [MIT License](LICENSE). Chinese translation: [LICENSE.zh.txt](LICENSE.zh.txt).

- **Copyright:** mgface
- **Repository:** https://github.com/JJosephph/ms-edge-tts-gui
