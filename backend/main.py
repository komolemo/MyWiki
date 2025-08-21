# main.py
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from sync import sync_filesystem

DATABASE_URL = "sqlite:///./wiki.db"
DATA_ROOT = "/path/to/{data}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        sync_filesystem(db, DATA_ROOT)
    finally:
        db.close()

@app.get("/categories")
def list_categories():
    db = SessionLocal()
    cats = db.query(Category).all()
    return [
        {"id": c.id, "name": c.name, "parent_id": c.parent_id, "path": c.path}
        for c in cats
    ]

@app.get("/pages")
def list_pages():
    db = SessionLocal()
    pages = db.query(Page).all()
    return [
        {"id": p.id, "title": p.title, "file_path": p.file_path, "category_id": p.category_id}
        for p in pages
    ]