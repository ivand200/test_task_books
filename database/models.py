from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float, String, Table
from sqlalchemy.orm import relationship, validates

from database.db import Base


association_table = Table(
    "association", Base.metadata,
    Column("authors_id", ForeignKey("authors.id")),
    Column("books_id", ForeignKey("books.id"))
)


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)

    books = relationship("Book", secondary=association_table, back_populates="authors")

    def __str__(self) -> str:
        return f"{self.name}"


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=True)

    authors = relationship("Author", secondary=association_table, back_populates="books")

    def __str__(self) -> str:
        return f"{self.title}, {self.authors}"