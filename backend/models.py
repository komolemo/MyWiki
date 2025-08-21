# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class SubCategory(Base):
    __tablename__ = "sub_categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class Page(Base):
    __tablename__ = "pages"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    categories = relationship("Category", secondary="page_categories", backref="pages")
    sub_categories = relationship("SubCategory", secondary="page_sub_categories", backref="pages")

class PageCategory(Base):
    __tablename__ = "page_categories"
    page_id = Column(Integer, ForeignKey("pages.id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id"), primary_key=True)

class PageSubCategory(Base):
    __tablename__ = "page_sub_categories"
    page_id = Column(Integer, ForeignKey("pages.id"), primary_key=True)
    sub_category_id = Column(Integer, ForeignKey("sub_categories.id"), primary_key=True)