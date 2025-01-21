from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "¡Bienvenido al sistema de gestión de biblioteca!"}

@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)

@app.get("/books/", response_model=list[schemas.Book])
def get_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_books(db=db, skip=skip, limit=limit)

@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.post("/borrows/", response_model=schemas.Borrow)
def create_borrow(borrow: schemas.BorrowCreate, db: Session = Depends(get_db)):
    return crud.create_borrow(db=db, borrow=borrow)

@app.put("/borrows/{borrow_id}", response_model=schemas.Borrow)
def return_book(borrow_id: int, db: Session = Depends(get_db)):
    db_borrow = crud.return_book(db, borrow_id=borrow_id)
    if db_borrow is None:
        raise HTTPException(status_code=404, detail="Borrow not found")
    return db_borrow
