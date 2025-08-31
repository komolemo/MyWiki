import sqlite3

# データベースファイルのパス（任意の場所に変更可能）
db_path = "./backend/sqlite3.db"

# 接続とカーソル作成
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# テーブル定義（tags）
cursor.execute("""
DROP TABLE tags
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS tags (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,   -- 文書ID
    name   TEXT UNIQUE                          -- タグ名
)
""")

# 保存して終了
conn.commit()
conn.close()

print("SQLiteデータベースとテーブルを作成しました。")