from database import get_db_connection
import psycopg2
# Function to create the Books table
def create_books_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL query to create the Books table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS books (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        description TEXT
    );
    '''
    
    cursor.execute(create_table_query)  # Execute the query to create the table
    conn.commit()  # Commit the changes to the database
    print("Books table created successfully!")
    
    cursor.close()
    conn.close()

# Function to add a book to the Books table
def add_book(title, author, description):
    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL query to insert a new book into the Books table
    insert_query = '''
    INSERT INTO books (title, author, description)
    VALUES (%s, %s, %s);
    '''

    # Execute the query with values for title, author, and description
    cursor.execute(insert_query, (title, author, description))
    conn.commit()  # Commit the changes

    print(f"Book '{title}' added successfully!")

    cursor.close()
    conn.close()

# Function to update the title of a book in the Books table
def update_book(book_id, new_title):
    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL query to update the title of a book
    update_query = '''
    UPDATE books SET title = %s WHERE id = %s;
    '''

    cursor.execute(update_query, (new_title, book_id))
    conn.commit()  # Commit the changes

    print(f"Book with ID {book_id} updated to {new_title}")

    cursor.close()
    conn.close()

# Function to create the Users table
def create_users_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL query to create the Users table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    '''
    
    cursor.execute(create_table_query)  # Execute the query to create the table
    conn.commit()  # Commit the changes to the database
    print("Users table created successfully!")

    cursor.close()
    conn.close()

# Function to add a user to the Users table
def add_user(name, email):
    conn = get_db_connection()
    cursor = conn.cursor()

    # SQL query to insert a new user into the Users table
    insert_query = '''
    INSERT INTO users (name, email)
    VALUES (%s, %s);
    '''

    # Execute the query with the provided values
    cursor.execute(insert_query, (name, email))
    conn.commit()  # Commit the changes

    print(f"User {name} added successfully!")

    cursor.close()
    conn.close()

# Test the functions
if __name__ == "__main__":
    # Step 1: Create the Books and Users tables
    create_books_table()
    create_users_table()

    # Step 2: Add a new book
    add_book("The Great Gatsby", "F. Scott Fitzgerald", "A classic novel set in the Jazz Age.")

    # Step 3: Add a new user
    add_user("John Doe", "john.doe@example.com")

    # Step 4: Update a book title (use an existing book ID, e.g., 1)
    update_book(1, "The Greatest Gatsby")

