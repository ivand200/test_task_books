# TODO: add comments
# TODO: add response_status, response_models
# TODO: check black/flake8
# TODO: check swagger
# TODO: raise HTTPException
# TODO: add logging

from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database.db import Base, engine, get_db
from database import models, schemas


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def home():
    return "Home"


@app.post("/authors/", response_model=schemas.AuthorData, status_code=201)
async def create_author(author: schemas.AuthorData, db: Session = Depends(get_db)):
    """
    Create a author
    name
    """
    # TODO: check existing author first
    pass


@app.get("/authors/", response_model=List[schemas.AuthorData], status_code=200)
async def read_authors(db: Session = Depends(get_db)):
    """
    Get all authors
    """
    pass


@app.put("/author/{id}", status_code=200)
async def update_author(id: int, db: Session = Depends(get_db)):
    """
    Update existing author by id
    """
    pass


@app.delete("/author/{id}", status_code=200)
async def delete_author(id: int, db: Session = Depends(get_db)):
    """
    Delete author by id
    """
    pass


@app.post("/book/", response_model=schemas.BookData, status_code=201)
async def create_book(book: schemas.BookBase, db: Session = Depends(get_db)):
    """
    Create a book
    """
    # TODO: Check existing book
    pass


@app.get("/books/", response_model=List[schemas.BookData], status_code=200)
async def read_books(db: Session = Depends(get_db)):
    """
    Get all book
    """
    pass


@app.put("/book/{id}", response_model=schemas.BookData, status_code=200)
async def update_book(id: int, db: Session = Depends(get_db)):
    """
    Update existing book by id
    """
    pass


@app.delete("/book/{id}", response_model=schemas.BookData, status_code=200)
async def delete_book(id: int, db: Session = Depends(get_db)):
    """
    Delete book by id
    """
    pass
