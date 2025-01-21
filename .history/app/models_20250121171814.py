from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)  # Añadimos longitud a VARCHAR
    author = Column(String(255), index=True)  # Añadimos longitud a VARCHAR
    published_date = Column(Date)

class Borrow(Base):
    __tablename__ = "borrows"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    borrower = Column(String(255), index=True)  # Añadimos longitud a VARCHAR
    borrow_date = Column(Date)
    return_date = Column(Date, nullable=True)

    book = relationship("Book")
