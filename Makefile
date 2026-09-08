.DEFAULT_GOAL := help

.PHONY: help run test windows macos linux release

help:
	@echo "make run        启动桌面程序"
	@echo "make test       运行单元测试"
	@echo "make windows    构建 Windows 安装包（需在 Windows 上）"
	@echo "make macos      构建 macOS DMG（需在 macOS 上）"
	@echo "make linux      构建 Linux .deb / AppImage（需在 Linux 上）"

ifeq ($(OS),Windows_NT)
PYTHON := .venv\Scripts\python.exe

run:
	@if not exist .venv\Scripts\python.exe (py -3 -m venv .venv & .venv\Scripts\python.exe -m pip install -r requirements.txt)
	@cmd /c "set PYTHONPATH=%CD%\src&& .venv\Scripts\python.exe -m edgettsgui"

windows:
	@cmd /c scripts\windows.bat

macos linux:
	@echo "Windows 上无法本地构建 $@ 包。请在对应系统执行 make $@，或推送 tag 由 CI 构建。" >&2
	@exit 1

test:
	@cmd /c "set PYTHONPATH=%CD%\src&& $(PYTHON) -m unittest discover -s tests -v"
else
PYTHON := .venv/bin/python

run:
	@test -x $(PYTHON) || (python3 -m venv .venv && $(PYTHON) -m pip install --upgrade pip && $(PYTHON) -m pip install -r requirements.txt)
	@PYTHONPATH=src $(PYTHON) -m edgettsgui

windows:
	@echo "当前系统无法本地构建 Windows 包。请在 Windows 上执行 make windows，或推送 tag 由 CI 构建。" >&2
	@exit 1

macos:
	@./scripts/macos.sh

linux:
	@./scripts/linux.sh

test:
	@test -x $(PYTHON) || (python3 -m venv .venv && $(PYTHON) -m pip install --upgrade pip && $(PYTHON) -m pip install -r requirements.txt)
	@PYTHONPATH=src $(PYTHON) -m unittest discover -s tests -v
endif

release:
	@echo "请选择要构建的平台：" >&2
	@echo "  make windows" >&2
	@echo "  make macos" >&2
	@echo "  make linux" >&2
	@exit 1
