#!/bin/bash

# FastAPIサーバーを起動（api.py の app を指定）

# python3 -m venv .venv
# source .venv/bin/activate
# pip install fastapi uvicorn
# wsl bash ./start_api.sh
uvicorn api:app --host 127.0.0.1 --port 8000 --reloadpyt