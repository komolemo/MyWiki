#!/bin/bash

# PowerShell 経由で仮想環境をアクティベートし、PATH を更新
# .venv/Scripts/Activate.ps1
# pip install -r requirements.txt
# $env:PATH = ".\.venv\Scripts;" + $env:PATH
powershell.exe -ExecutionPolicy Bypass -Command "& {
    . .\\venv\\Scripts\\Activate.ps1
    \$env:PATH = '.\\.venv\\Scripts;' + \$env:PATH
}"omVemv