import os
from datetime import datetime

from docx import Document
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from lxml import etree

import sqlite3
    
class Paragraph_to_Value:
    paragraph = None
    part = None
    # 色スタイルを適用
    @classmethod
    def is_colored(cls, run) -> bool:
        color = run.font.color.rgb
        return color and str(color).upper() == "E97132"

    # 太字スタイルを適用
    @classmethod
    def is_bold(cls, run) -> bool:
        return run.bold
    
    # 改行を検知
    @classmethod
    def is_break(cls, run) -> bool:
        return bool(run.text and "\n" in run.text)

    # スタイルID
    @classmethod
    def get_style_id(cls, paragraph) -> str:
        pPr = paragraph._p.find(qn('w:pPr'))
        if pPr is not None:
            pStyle = pPr.find(qn('w:pStyle'))
            if pStyle is not None:
                return pStyle.get(qn('w:val'))
        return None
    
    # levelを検知
    @classmethod
    def level(cls, para) -> int:
        style_id = cls.get_style_id(para)
        level = cls.map_id_to_marker(style_id)
        return level

    @classmethod
    def map_id_to_marker(cls, id_str: str) -> int:
        return {
            "a": 0,
            "a0": 1,
            "1": 2,
            "a1": 3,
            "20": 4,
            "3": 5
        }.get(id_str, 99)
    
    @classmethod
    def link(cls, run):
        paragraph = run._parent  # run が属する段落
        p_element = paragraph._element
        run_text = run.text

        for hyperlink in p_element.findall(".//w:hyperlink", namespaces=p_element.nsmap):
            for r in hyperlink.findall(".//w:r", namespaces=hyperlink.nsmap):
                for t in r.findall(".//w:t", namespaces=hyperlink.nsmap):
                    print(t, bool(run_text))
                    print(type(run_text))
                if t is not None and run_text == "":
                    r_id = hyperlink.get(qn('r:id'))
                    print(r_id)
                    if r_id:
                        rel = Docx_to_Db.rel(r_id)
                        return rel
        return None

        # for hyperlink in p_element.findall(".//w:hyperlink", namespaces=p_element.nsmap):
        #     # hyperlink の中にこの run が含まれているか確認
        #     r_id = hyperlink.get(qn('r:id'))
        #     if r_id:
        #         link = Docx_to_Db.rel(r_id)
        #         print(link)
        #         return link
        # return ""
    
    @classmethod
    def insert_data(cls, level, col, run):
        is_colored = cls.is_colored(run)
        is_bold = cls.is_bold(run)
        is_break = cls.is_break(run)
        link = cls.link(run)
        return [level, col, is_break, is_bold, is_colored, run.text, link]
    
    # doc_id     INTEGER,    -- 文書ID
    # row        INTEGER,    -- 行番号
    # col        INTEGER,    -- 列番号
    # level      INTEGER,    -- 階層レベル
    # br         BOOLEAN,    -- 改行フラグ
    # bold       BOOLEAN,    -- 太字フラグ
    # color      BOOLEAN,    -- カラー指定
    # text       TEXT,       -- 本文
    # graph      INTEGER,    -- グラフ参照
    # img        INTEGER,    -- 画像参照
    # link       TEXT,       -- リンク
    # PRIMARY KEY (doc_id, row, col)

    @classmethod
    def insert_chunks(cls, doc_id, row, para):
        insert_chunks = []
        level = cls.level(para)
        for col, run in enumerate(para.runs):
            insert_data = [doc_id, row]
            insert_data += cls.insert_data(level, col, run)
            insert_data += [None, None]
            insert_chunks += [insert_data]
        return tuple(insert_chunks)

# General Class
class Docx_to_Db:
    _part = None
    @classmethod
    def rel(cls, r_id) -> str:
        return cls._part.rels[r_id].target_ref
        return cls._part.rels[r_id]._target
        print(cls._part.rels[r_id]._target)
        rel = cls._part.related_parts[cls._part.rels[r_id]._target]
        print("リンクURL:", rel.target_ref)
        return rel

    @classmethod
    def insert_chunks(cls, doc_id, row, para):
        chunks = Paragraph_to_Value.insert_chunks(doc_id, row, para)
        # chunks = [
        #     (1, 0, 0, 1, 0, 1, 0, "これはテスト文です。", 0, 0),
        #     (1, 0, 1, 1, 0, 0, 1, "色付きの文節です。", 0, 0),
        #     (1, 1, 0, 2, 1, 1, 1, "改行された太字＋カラー文節。", 0, 0),
        #     (1, 2, 0, 2, 0, 0, 0, "通常の文節です。", 0, 0)
        # ]

        return chunks

    @classmethod
    def insert_paragraph(cls, doc_id, row, para):
        # データベース接続
        conn = sqlite3.connect("./backend/sqlite3.db")
        cursor = conn.cursor()

        # 挿入する複数行のデータ（例）
        chunks = cls.insert_chunks(doc_id, row, para)

        # 一括挿入処理
        cursor.executemany("""
        INSERT INTO doc_chunks (
            doc_id, row, level, col, br, bold, color, text, link, graph, img
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, chunks)


        # 保存して終了
        conn.commit()
        conn.close()

        # print("doc_chunks にデータを挿入しました。")
    
    @classmethod
    def convert(cls, doc_id: int, docx_path: str):
        doc = Document(docx_path)
        cls._part = doc.part

        for row, para in enumerate(doc.paragraphs):
            cls.insert_paragraph(doc_id, row, para)

    @classmethod
    def convert_all(cls):
        conn = sqlite3.connect("./backend/sqlite3.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id, path FROM documents")
        results = cursor.fetchall()

        for doc_id, path in results:
            # print(f"ID: {doc_id}, パス: {path}")
            cls.convert(doc_id, path)

        conn.close()

    @classmethod
    def insert_documents(cls, name, path):
        conn = sqlite3.connect("./backend/sqlite3.db")
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()

        updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # INSERT文
        cursor.execute("""
        INSERT INTO documents (name, path, updated_at)
        VALUES (?, ?, ?)
        """, (name, path, updated_at))

        conn.commit()
        conn.close()

        print("documents テーブルに文書を追加しました。")

    @classmethod
    def register_docs(cls):
        # 文書情報
        docs = [{
            "name": "example3",
            "path": "./data/Category3/example3.docx"
        }]
        for doc in docs:
            cls.insert_documents(doc["name"], doc["path"])

# DocxToMarkdownConverter.convert('./data/Category3/example3.docx', './data/Category3/example3.md')
# Docx_to_Db.register_docs()
Docx_to_Db.convert_all()
