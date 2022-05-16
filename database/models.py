from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float, String, Table
from sqlalchemy.orm import relationship, validates

from database.db import Base


association_table = Table(
    "association", Base.metadata,
    Column("authors_id", ForeignKey("authors.id")),
    Column("books_id", ForeignKey("books.id"))
)


# class Association(Base):
#     __tablename__ = "association"
# 
#     authors_id = Column(ForeignKey("authors.id"), primary_key=True)
#     books_id = Column(ForeignKey("books.id"), primary_key=True)
# 
#     author = relationship("Author", back_populates="books")
#     book = relationship("Book", back_populates="authors")


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)

    books = relationship("Book", secondary=association_table, back_populates="authors", passive_deletes=False, cascade="save-update" )

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return self.name


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, nullable=False)
    title = Column(String(100), nullable=False, index=True)
    description = Column(String, nullable=True)

    authors = relationship("Author", secondary=association_table, back_populates="books", passive_deletes=False, cascade="save-update" )

    def __str__(self) -> str:
        return f"{self.title}, {self.authors}"

    def __repr__(self) -> str:
        return self.title