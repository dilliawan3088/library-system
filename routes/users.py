from fastapi import APIRouter
from models.schemas import User, UserBase
from database import get_db_connection
import psycopg2

router = APIRouter()

# CREATE a new user (FastAPI route)
@router.post("/users/", response_model=User)
def create_user(user: UserBase):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;", 
                   (user.name, user.email))
    user_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return {**user.dict(), "id": user_id}

# READ all users (FastAPI route)
@router.get("/users/", response_model=list[User])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"id": user[0], "name": user[1], "email": user[2]} for user in users]

# Function to add a user directly to the database
def add_user(name, email):
    conn = get_db_connection()  # This should return a valid connection
    cursor = conn.cursor()

    # SQL query to insert a new user into the users table
    insert_query = '''
    INSERT INTO users (name, email) 
    VALUES (%s, %s);
    '''

    # Execute the query with the provided values
    cursor.execute(insert_query, (name, email))
    conn.commit()  # Commit the changes to the database

    print(f"User {name} added successfully!")

    cursor.close()
    conn.close()

# Call the function to add a new user (for testing purposes)
#add_user('Alice Johnson', 'alice.johnson@example.com')  # Test Line (remove after testing)

