import sqlite3

# データベースに接続
conn = sqlite3.connect('./backend/sqlite3.db')
cursor = conn.cursor()

# カラム追加のSQL文
cursor.execute('ALTER TABLE doc_chunks ADD COLUMN link TEXT')

# 変更を保存して接続を閉じる
conn.commit()
conn.close()