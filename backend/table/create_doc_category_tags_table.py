import sqlite3

# データベースファイルのパス（任意の場所に変更可能）
db_path = "./backend/sqlite3.db"

# 接続とカーソル作成
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# テーブル定義（document_categories）
cursor.execute("""
CREATE TABLE document_categories (
    document_id INTEGER,
    category_id INTEGER,
    FOREIGN KEY (document_id) REFERENCES documents(id),
    FOREIGN KEY (category_id) REFERENCES category_tags(id),
    PRIMARY KEY (document_id, category_id)
)
""")

# 保存して終了
conn.commit()
conn.close()

print("document_categoriesテーブルを作成しました。")