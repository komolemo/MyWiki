import sqlite3

# データベースファイルのパス（任意の場所に変更可能）
db_path = "./backend/sqlite3.db"

# 接続とカーソル作成
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# テーブル定義（doc_chunks）
cursor.execute("""
DROP TABLE IF EXISTS documents
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS documents (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,  -- 文書ID（自動割り振り）
    name        TEXT,                               -- 文書名
    path        TEXT,                               -- JSONまたはテキストファイルのパス
    updated_at  TIMESTAMP                           -- 最終更新日時
);
""")

# 保存して終了
conn.commit()
conn.close()

print("SQLiteデータベースとテーブルを作成しました。")