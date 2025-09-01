import sqlite3

# SQLiteデータベースに接続（ファイル名を適宜変更）
conn = sqlite3.connect('./backend/sqlite3.db')
cursor = conn.cursor()

# 初期化したいテーブル名
table_name = 'documents'

# テーブルの中身を削除（DELETE文）
cursor.execute(f'DELETE FROM {table_name}')

# オートインクリメントのIDもリセットしたい場合（SQLite特有）
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{table_name}"')

# 変更を保存して接続を閉じる
conn.commit()
conn.close()