from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

books = {}
next_id = 1


class Book(BaseModel):
    title: str
    author: str
    price: float


@app.get("/books")
def get_all_books():
    return books


@app.post("/books", status_code=201)
def create_book(book: Book):
    global next_id
    books[next_id] = book.model_dump()
    created_book = books[next_id]
    next_id += 1
    return created_book


class BookUpdate(BaseModel):
    title: Optional[str] = None
    price: Optional[float] = None


@app.put("/books/{book_id}")
def update_book(book_id: int, update: BookUpdate):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Not found")

    if update.title is not None:
        books[book_id]["title"] = update.title
    if update.price is not None:
        books[book_id]["price"] = update.price

    return books[book_id]


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Not found")

    del books[book_id]
    return {"message": "Book deleted"}
