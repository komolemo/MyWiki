import sqlite3

# データベースファイルのパス（任意の場所に変更可能）
db_path = "./backend/sqlite3.db"

# 接続とカーソル作成
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# テーブル定義（document_tags）
# 中間テーブル（文書とタグの紐付け）
cursor.execute("""
CREATE TABLE IF NOT EXISTS document_tags (
    document_id INTEGER,             -- 文書ID
    tag_id      INTEGER,             -- タグID
    FOREIGN KEY (document_id) REFERENCES documents(id),
    FOREIGN KEY (tag_id) REFERENCES tags(id),
    PRIMARY KEY (document_id, tag_id)
)
""")

# 保存して終了
conn.commit()
conn.close()

print("SQLiteデータベースとテーブルを作成しました。")