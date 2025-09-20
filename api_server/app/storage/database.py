import sqlite3
import os
from app.config import get_config
from logger import setup_logging

logger = setup_logging()
config = get_config()

# DATABASE_FILE is read from config.ini, with a default value if not found
DATABASE_FILE = config.get("DATABASE", "NAME", "./data/app.db")

def get_db_connection():
    """
    Establishes a connection to the SQLite database.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row # This allows accessing columns by name
    return conn

def initialize_database():
    """
    Initializes the database by creating necessary tables if they don't exist.
    Also inserts dummy data for employees.
    """
    db_dir = os.path.dirname(DATABASE_FILE)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir)

    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Create employees table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                position TEXT NOT NULL
            )
        """)
        logger.info("Ensured 'employees' table exists.")

        # Insert dummy data if table is empty
        cursor.execute("SELECT COUNT(*) FROM employees")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO employees (name, position) VALUES (?, ?)", ("Alice Smith", "Software Engineer"))
            cursor.execute("INSERT INTO employees (name, position) VALUES (?, ?)", ("Bob Johnson", "Project Manager"))
            conn.commit()
            logger.info("Inserted dummy employee data.")
        else:
            logger.info("Employee table already contains data, skipping dummy data insertion.")

    except sqlite3.Error as e:
        logger.error(f"Database initialization error: {e}")
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    # Example of how to use and test the database initialization
    print(f"Initializing database at: {DATABASE_FILE}")
    initialize_database()
    print("Database initialized and dummy data checked/inserted.")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    print("\nCurrent employees in DB:")
    for employee in employees:
        print(dict(employee))
    conn.close()
