from fastapi import FastAPI, HTTPException
from sqlmodel import Field, Session, create_engine
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlmodel.ext.asyncio.session import AsyncSession

app = FastAPI()

# Create a SQLAlchemy engine and session
engine = create_engine("postgresql://user:password@postgres:5432/postgres")
async_session = Session(engine, autocommit=False, autoflush=False)

class Book(SQLModel, table=True):
    __tablename__ = "books"
    id: int = Field(primary_key=True)
    pmid: int = Field(unique=True)
    language: str
    title: str
    abstract: str

# Create the database schema
SQLModel.metadata.create_all(engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Create a new book
@app.post("/books")
async def create_book(book: Book):
    async with async_session() as session:
        session.add(book)
        await session.commit()
    return {"message": "Book created successfully"}

# Get all books
@app.get("/books")
async def get_books():
    async with async_session() as session:
        books = await session.exec(select(Book))
        return books.all()

# Get a specific book by PMID
@app.get("/books/{pmid}")
async def get_book(pmid: int):
    async with async_session() as session:
        book = await session.get(Book, pmid)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Update a book by PMID
@app.put("/books/{pmid}")
async def update_book(pmid: int, book: Book):
    async with async_session() as session:
        existing_book = await session.get(Book, pmid)
        if existing_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        existing_book.language = book.language
        existing_book.title = book.title
        existing_book.abstract = book.abstract
        await session.commit()
    return {"message": "Book updated successfully"}

# Delete a book by PMID
@app.delete("/books/{pmid}")
async def delete_book(pmid: int):
    async with async_session() as session:
        existing_book = await session.get(Book, pmid)
        if existing_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        await session.delete(existing_book)
        await session.commit()
    return {"message": "Book deleted successfully"}