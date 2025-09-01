import sqlite3

# データベースファイルのパス（任意の場所に変更可能）
db_path = "./backend/sqlite3.db"

# 接続とカーソル作成
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# テーブル定義（category_hierarchy）
cursor.execute("""
DROP TABLE IF EXISTS category_hierarchy
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS category_hierarchy (
    parent_id INTEGER,
    child_id  INTEGER,
    FOREIGN KEY (parent_id) REFERENCES category_tags(id),
    FOREIGN KEY (child_id)  REFERENCES category_tags(id),
    PRIMARY KEY (parent_id, child_id)
);
""")

# 保存して終了
conn.commit()
conn.close()

print("category_hierarchyテーブルを作成しました。")