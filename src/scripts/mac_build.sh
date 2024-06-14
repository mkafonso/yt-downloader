#!/bin/bash

# Navegar para o diretório do script
cd "$(dirname "$0")"

# Gerar executável para macOS usando PyInstaller
pyinstaller --onefile ../main.py
