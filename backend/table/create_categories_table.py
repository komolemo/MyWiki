import sqlite3

# データベースファイルのパス（任意の場所に変更可能）
db_path = "./backend/sqlite3.db"

# 接続とカーソル作成
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# テーブル定義（categories）
cursor.execute("""
CREATE TABLE category_tags (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    name   TEXT UNIQUE,
    group_name  TEXT,   -- 分類グループ（例：用途、状態）
    note   TEXT    -- 補足説明
)
""")

# 保存して終了
conn.commit()
conn.close()

print("categoriesテーブルを作成しました。")