import sqlite3
import os
import sys

def loadDatabase(test=False):
    """
    Establishes a connection to the SQLite database.

    Parameters:
        test (bool): If True, connects to the test database. Otherwise, connects to the production database.

    Returns:
        tuple: (connection, cursor) to interact with the database.
    """
    # Determine the directory where the script or executable resides
    if getattr(sys, 'frozen', False):
        dir = os.path.dirname(sys.executable)
    else:
        dir = os.path.dirname(__file__)

    # Choose between main or test database
    db_filename = "placeholderTestData.db" if test else "placeholderData.db"
    db_path = os.path.join(dir, "data", db_filename)

    # Connect to the database
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    print("The database connection has been successfully established.")
    return connection, cursor


def initializeDatabase(connection, cursor):
    """
    Initializes the database by creating the 'furniture' table if it does not already exist.

    Parameters:
        connection (sqlite3.Connection): The database connection object.
        cursor (sqlite3.Cursor): The database cursor object.
    """
    cursor.execute('''CREATE TABLE IF NOT EXISTS furniture (
        furniture_id INTEGER PRIMARY KEY,
        type VARCHAR(30),
        colour VARCHAR(30),
        price FLOAT,
        size VARCHAR(30) DEFAULT '',
        aisle VARCHAR(30) DEFAULT ''
    )''')
    connection.commit()
    print("Furniture table initialized.")
    print("The database tables have been successfully initialized.")


def addLogin(connection, cursor, id, level, username, password):
    """
    Adds a new user login entry to the 'login' table.

    Parameters:
        connection (sqlite3.Connection): The database connection.
        cursor (sqlite3.Cursor): The cursor for executing SQL commands.
        id (int): Staff ID (must be unique).
        level (int): User access level (1 = Admin, etc.).
        username (str): The username for the login.
        password (str): The password for the login.
    """
    try:
        cursor.execute("INSERT INTO login VALUES (?, ?, ?, ?)", (id, level, username, password))
        connection.commit()
        print(f"User with Staff ID {id} has been successfully added.")
    except sqlite3.IntegrityError:
        print(f"User with Staff ID {id} already exists in the system.")


def attemptLogin(cursor, id, password):
    """
    Verifies login credentials against the 'login' table.

    Parameters:
        cursor (sqlite3.Cursor): Cursor to execute SQL commands.
        id (int): Staff ID entered by user.
        password (str): Password entered by user.

    Returns:
        tuple | None: Returns the user row if authenticated successfully, otherwise None.
    """
    cursor.execute("SELECT * FROM login WHERE staff_id = ? AND password = ?", (id, password))
    user = cursor.fetchone()
    if user:
        print("Authentication successful.")
        return user
    print("Authentication failed. Please verify your credentials and try again.")
    return None


def closeDatabase(connection):
    """
    Closes the database connection.

    Parameters:
        connection (sqlite3.Connection): The open connection to close.
    """
    connection.close()
    print("The database connection has been closed.")
