# sync.py
import os
from sqlalchemy.orm import Session
from models import Category, Page

def sync_filesystem(db: Session, data_root: str):
    # 1. 既存レコード取得
    cats_by_path = {c.path: c for c in db.query(Category).all()}
    pages_by_path = {p.file_path: p for p in db.query(Page).all()}

    seen_cats, seen_pages = set(), set()

    # 2. ディレクトリ／ファイル走査
    for dirpath, _, filenames in os.walk(data_root):
        rel_dir = os.path.relpath(dirpath, data_root)
        if rel_dir == ".":
            rel_dir = ""

        # カテゴリ登録
        if rel_dir not in cats_by_path:
            parent_path = os.path.dirname(rel_dir) if rel_dir else ""
            cat = Category(
                name=os.path.basename(rel_dir) or "root",
                path=rel_dir,
                parent=cats_by_path.get(parent_path)
            )
            db.add(cat); db.flush()
            cats_by_path[rel_dir] = cat
        seen_cats.add(rel_dir)
        
        # HTMLファイル登録
        for fn in filenames:
            if not fn.lower().endswith(".html"):
                continue
            rel_file = os.path.join(rel_dir, fn) if rel_dir else fn
            title = os.path.splitext(fn)[0]
            page = pages_by_path.get(rel_file)
            if page is None:
                page = Page(title=title, file_path=rel_file,
                            category=cats_by_path[rel_dir])
                db.add(page)
            else:
                page.title = title
                page.category = cats_by_path[rel_dir]
            seen_pages.add(rel_file)

    # 3. 差分削除
    for path, cat in cats_by_path.items():
        if path not in seen_cats:
            db.delete(cat)
    for path, page in pages_by_path.items():
        if path not in seen_pages:
            db.delete(page)

    db.commit()