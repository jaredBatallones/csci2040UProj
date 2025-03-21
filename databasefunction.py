import sqlite3
import os
import sys

def loadDatabase(test=False):
    # Get the executable's directory or script directory
    if getattr(sys, 'frozen', False):
        dir = os.path.dirname(sys.executable)
    else:
        dir = os.path.dirname(__file__)
    
    # Point to external data folder
    if test == False:
        db_filename = "placeholderData.db"
    else:
        db_filename =  "placeholderTestData.db"
    db_path = os.path.join(dir, "data", db_filename)
    
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    print("The database connection has been successfully established.")
    return connection, cursor

# Set up the tables if they don’t exist yet
def initializeDatabase(connection, cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS login (
        staff_id INTEGER PRIMARY KEY,
        level INTEGER,
        username VARCHAR(30),
        password VARCHAR(30))''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS furniture (
        furniture_id INTEGER PRIMARY KEY,
        type VARCHAR(30),
        colour VARCHAR(30),
        price FLOAT)''')
    
    connection.commit()
    print("The database tables have been successfully initialized.")

# Add a new user to the login table
def addLogin(connection, cursor, id, level, username, password):
    try:
        cursor.execute("INSERT INTO login VALUES (?, ?, ?, ?)", (id, level, username, password))
        connection.commit()
        print(f"User with Staff ID {id} has been successfully added.")
    except sqlite3.IntegrityError:
        print(f"User with Staff ID {id} already exists in the system.")

# Check if login credentials are valid
def attemptLogin(cursor, id, password):
    cursor.execute("SELECT * FROM login WHERE staff_id = ? AND password = ?", (id, password))
    user = cursor.fetchone()
    if user:
        print("Authentication successful.")
        return user  # Returns the entire user row
    print("Authentication failed. Please verify your credentials and try again.")
    return None

# Close the database connection when done
def closeDatabase(connection):
    connection.close()
    print("The database connection has been closed.")