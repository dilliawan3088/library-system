import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get database credentials from the environment variables
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "library_system")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "Blabla@123")  # Replace with your password

# Function to establish a database connection
def get_db_connection():
    connection = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return connection
