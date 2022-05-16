from fastapi.testclient import TestClient

from database import models
from app.main import app
import json
import pytest


client = TestClient(app)

def test_new_author():
    """
    GIVEN a Author model
    WHEN a new Author is created
    THEN check the name
    """
    author = models.Author(name="Edgar Po")
    assert author.name == "Edgar Po"


def test_new_book():
    """
    GIVEN a Book, Author models
    WHEN a new Book is created
    THEN check the title, description
    """
    author_1 = models.Author(name="test_author_1")
    author_2 = models.Author(name="test_author_2")
    book = models.Book(title="Blood Meridian", description="Western", authors=[author_1, author_2])
    assert book.title == "Blood Meridian"
    assert book.description == "Western"
    assert len(book.authors) == 2


def test_post_book():
    """
    GIVEN JSON book with authors
    WHEN a new Book is posted
    THEN check the title, status, authors
    """
    payload = {
    "title": "Castle",
    "description": "Undone Kafka novel",
    "number": 10999,
    "authors": [
        {
            "name": "Frantz Kafka"
        },
        {
            "name": "Edgar Po"
        }
    ]
    }
    response_post_book = client.post("/book", data=json.dumps(payload))
    response_post_book_body = response_post_book.json()

    assert response_post_book.status_code == 201
    assert response_post_book_body["title"] == "Castle"
    assert len(response_post_book_body["authors"]) == 2


def test_delete_book():
    """
    GIVEN a book title
    WHEN a book is deleted
    THEN check the status, title
    """
    response_delete_book = client.delete("/book/10999")
    response_delete_book_body = response_delete_book.json()

    assert response_delete_book.status_code == 200
    assert response_delete_book_body["title"] == "Castle"




