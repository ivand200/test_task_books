from typing import List, Optional

from pydantic import BaseModel, validator, Field


class AuthorBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    description: str
    number: int

    class Config:
        orm_mode = True


class BookData(BookBase):
    authors: List[AuthorBase]

    class Config:
        orm_mode = True


class AuthorData(AuthorBase):
    books: List[BookBase]

    class Config:
        orm_mode = True