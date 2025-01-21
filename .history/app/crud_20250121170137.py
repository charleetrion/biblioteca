from sqlalchemy.orm import Session
from . import models, schemas

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(title=book.title, author=book.author, published_date=book.published_date)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book

def create_borrow(db: Session, borrow: schemas.BorrowCreate):
    db_borrow = models.Borrow(book_id=borrow.book_id, borrower=borrow.borrower, borrow_date=borrow.borrow_date)
    db.add(db_borrow)
    db.commit()
    db.refresh(db_borrow)
    return db_borrow

def return_book(db: Session, borrow_id: int):
    db_borrow = db.query(models.Borrow).filter(models.Borrow.id == borrow_id).first()
    if db_borrow:
        db_borrow.return_date = db.func.current_date()
        db.commit()
    return db_borrow
