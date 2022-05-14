# TODO: add comments
# TODO: add response_status, response_models
# TODO: check black/flake8
# TODO: check swagger
# TODO: raise HTTPException
# TODO: add logging

from typing import List

from yaml import serialize

from fastapi import FastAPI, Depends, HTTPException, Body, Form, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from celery.result import AsyncResult


from database.db import Base, engine, get_db
from database import models, schemas
from .worker import create_task, new_task


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def home():
    return "Home"


@app.post("/tasks", status_code=201)
def run_task(payload = Body(...)):
    """
    TEST Celery
    """
    task_type = payload["type"]
    task = create_task.delay(int(task_type))
    return JSONResponse({"task_id": task.id})


@app.post("/test", status_code=201)
def test_task(payload = Body(...)):
    task_type = payload["text"]
    task = new_task.delay(str(task_type))
    return JSONResponse({"task_id": task.id})


@app.post("/new", status_code=201)
def celery_task(payload = Body(...)):
    print(f"{payload['text']}")
    return "ok"


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

# TODO: done this API
# TODO: write test for this API
# TODO: commit to github
@app.post("/book/", status_code=201)  # response_model=schemas.BookData,
async def create_book(book: schemas.BookData, db: Session = Depends(get_db)):
    """
    Create a book
    """
    check_book = db.query(models.Book).filter(models.Book.title == book.title).first()
    if check_book:
        raise HTTPException(status_code=400, detail="Book already exists")
    new_book = models.Book(title=book.title, description=book.description)
    authors = [schemas.AuthorBase(**i.__dict__) for i in book.authors]
    exist_authors = []
    for author in authors:
        check_author = db.query(models.Author).filter(models.Author.name == author.name).first()
        if check_author:
            new_book.authors.append(check_author)
            # exist_authors.append(check_author)
        else:
            db_author = models.Author(name=author.name)
            new_book.authors.append(db_author)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    db_book = db.query(models.Book).join(models.Book.authors).filter(models.Author.books.contains(new_book)).first()
    db_authors = db.query(models.Author).join(models.Author.books).filter(models.Book.id == db_book.id).all()
    book_serializer = schemas.BookData(title=db_book.title, description=db_book.description, authors=db_authors)
    return book_serializer


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
