import sqlite3

# データベースファイルのパス（任意の場所に変更可能）
db_path = "./backend/sqlite3.db"

# 接続とカーソル作成
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# テーブル定義（doc_chunks）
cursor.execute("""
DROP TABLE IF EXISTS doc_chunks
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS doc_chunks (
    doc_id     INTEGER,    -- 文書ID（外部キー）
    row        INTEGER,    -- 行番号
    col        INTEGER,    -- 列番号
    level      INTEGER,    -- 階層レベル
    br         BOOLEAN,    -- 改行フラグ
    bold       BOOLEAN,    -- 太字フラグ
    color      BOOLEAN,    -- カラー指定
    text       TEXT,       -- 本文
    graph      INTEGER,    -- グラフ参照
    img        INTEGER,    -- 画像参照
    link       TEXT,       -- リンク
    PRIMARY KEY (doc_id, row, col),
    FOREIGN KEY (doc_id) REFERENCES documents(id) ON DELETE CASCADE
);
""")

# インデックス（検索効率向上）
cursor.execute("CREATE INDEX IF NOT EXISTS idx_doc_id ON doc_chunks(doc_id)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_bold_color ON doc_chunks(bold, color)")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_graph_img ON doc_chunks(graph, img)")

# 保存して終了
conn.commit()
conn.close()

print("SQLiteデータベースとテーブルを作成しました。")