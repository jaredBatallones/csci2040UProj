import sqlite3
import os

# Connect to the database file and return the connection and cursor
def loadDatabase():
    dir = os.path.dirname(__file__)
    connection = sqlite3.connect(os.path.join(dir, "data/placeholderData.db"))
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