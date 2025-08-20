from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from typing import List

app = FastAPI()

# CORS設定（必要に応じて調整）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 本番環境では制限すること
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/list")
def list_items(
    path: str = Query(default="data", description="相対パス"),
    only_dirs: bool = Query(default=False, description="フォルダのみ返すか"),
    recursive: bool = Query(default=False, description="再帰的に探索するか")
) -> List[str]:
    base_path = Path(path)
    if not base_path.exists():
        return []

    if recursive:
        items = base_path.rglob("*")
    else:
        items = base_path.iterdir()

    result = [
        str(item.relative_to(base_path))
        for item in items
        if (only_dirs and item.is_dir()) or (not only_dirs)
    ]
    return result