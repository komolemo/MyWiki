from fastapi import FastAPI
from fastapi.responses import JSONResponse
import sqlite3

app = FastAPI()

@app.get("/documents/{doc_id}")
def get_document_chunks(doc_id: int):
    conn = sqlite3.connect("./backend/sqlite3.db")
    conn.row_factory = sqlite3.Row  # dict形式で取得するため
    cursor = conn.cursor()

    cursor.execute("""
        SELECT row, level, col, br, color, text, graph, img
        FROM doc_chunks
        WHERE doc_id = ?
        ORDER BY row ASC, col ASC
    """, (doc_id,))

    rows = cursor.fetchall()
    conn.close()

    # dict形式に変換
    results = [dict(row) for row in rows]
    return JSONResponse(content=results)