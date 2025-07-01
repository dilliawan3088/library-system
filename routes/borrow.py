from fastapi import APIRouter
import psycopg2
import sys
import os

# Add the project root folder to the path (C:/Users/hp/Desktop/Python files/library_system)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from database import get_db_connection
from models.schemas import BorrowRecord

router = APIRouter()

# Function to create the borrow_records table
def create_borrow_records_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS borrow_records (
        id SERIAL PRIMARY KEY,
        user_id INT NOT NULL,
        book_id INT NOT NULL,
        borrow_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        return_date TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (book_id) REFERENCES books(id)
    );
    '''

    cursor.execute(create_table_query)
    conn.commit()
    print("Borrow Records table created successfully!")

    cursor.close()
    conn.close()

# Run this only when executed directly (not when imported via FastAPI)
if __name__ == "__main__":
    create_borrow_records_table()

# FastAPI route to create a borrow record
@router.post("/borrow/", response_model=BorrowRecord)
def borrow_book(borrow: BorrowRecord):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO borrow_records (user_id, book_id, borrow_date) VALUES (%s, %s, %s) RETURNING id;",
        (borrow.user_id, borrow.book_id, borrow.borrow_date)
    )
    borrow_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return {**borrow.dict(), "id": borrow_id}
