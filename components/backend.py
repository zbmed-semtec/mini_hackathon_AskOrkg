from fastapi import FastAPI, HTTPException, Depends, Query  
from sqlalchemy import select  
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

import models
from database import engine
from schemas import Books
from database import get_db

app = FastAPI()

models.Base.metadata.create_all(bind= engine)
        
@app.get("/")
def default():
    return {"message": "this is working"}

@app.post("/books")
def create(book: Books,db: Session = Depends(get_db)):
    new_book = models.Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.get("/books")
def get(db: Session = Depends(get_db)):
    all_books = db.query(models.Book).all()
    return all_books

@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    """Retrieves a specific book by its ID from the database.

    Args:
        book_id (int): The ID of the book to retrieve.
        db (Session): The database session dependency.

    Returns:
        Books: The book object with the corresponding ID, or None if not found.

    Raises:
        HTTPException: If the book with the specified ID is not found.
    """

    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book with ID {book_id} not found")
    return book

@app.put("/books/{book_id}", status_code=status.HTTP_200_OK)
def update_book(book_id: int, book: Books, db: Session = Depends(get_db)):
    """Updates an existing book in the database.

    Args:
        book_id (int): The ID of the book to update.
        book (Books): The updated book data.
        db (Session): The database session dependency.

    Returns:
        Books: The updated book object.

    Raises:
        HTTPException: If the book with the specified ID is not found.
    """

    existing_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not existing_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book with ID {book_id} not found")

    # Update book attributes
    for field, value in book.dict().items():
        setattr(existing_book, field, value)

    db.commit()
    db.refresh(existing_book)
    return existing_book

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Deletes a book from the database.

    Args:
        book_id (int): The ID of the book to delete.
        db (Session): The database session dependency.

    Raises:
        HTTPException: If the book with the specified ID is not found.
    """

    book = db.query(models)