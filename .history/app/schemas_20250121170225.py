from pydantic import BaseModel
from datetime import date

class BookBase(BaseModel):
    title: str
    author: str
    published_date: date

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        from_attributes = True

class BorrowBase(BaseModel):
    book_id: int
    borrower: str
    borrow_date: date

class BorrowCreate(BorrowBase):
    pass

class Borrow(BorrowBase):
    id: int
    return_date: date | None = None

    class Config:
        from_attributes = True
