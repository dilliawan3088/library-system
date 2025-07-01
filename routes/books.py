from fastapi import APIRouter
from models.schemas import Book, BookBase
from database import get_db_connection

router = APIRouter()

# CREATE a new book
@router.post("/books/", response_model=Book)
def create_book(book: BookBase):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, description) VALUES (%s, %s, %s) RETURNING id;",
                   (book.title, book.author, book.description))
    book_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return {**book.dict(), "id": book_id}

# READ all books
@router.get("/books/", response_model=list[Book])
def get_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books;")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"id": book[0], "title": book[1], "author": book[2], "description": book[3]} for book in books]

# UPDATE a book
@router.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookBase):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title = %s, author = %s, description = %s WHERE id = %s;",
                   (book.title, book.author, book.description, book_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {**book.dict(), "id": book_id}

# DELETE a book
@router.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s RETURNING id, title, author, description;", (book_id,))
    deleted_book = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    if deleted_book:
        return {"id": deleted_book[0], "title": deleted_book[1], "author": deleted_book[2], "description": deleted_book[3]}
    return {"error": "Book not found"}
