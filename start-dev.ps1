# FastAPIサーバーを backend/api.py から起動
Start-Process -NoNewWindow -FilePath .\.venv\Scripts\python.exe -WorkingDirectory "./backend" -ArgumentList "-m uvicorn api:app --reload --port 8000"

# React/Vite 開発サーバーを frontend から起動
Start-Process -NoNewWindow -FilePath "npm" -WorkingDirectory "./frontend" -ArgumentList "run", "dev"