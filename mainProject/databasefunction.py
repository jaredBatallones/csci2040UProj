import sqlite3

# Connect to the database file and return the connection and cursor
def loadDatabase():
    # Use a relative path to the database file, assuming it's in mainProject/data/
    connection = sqlite3.connect("data/placeholderData.db")
    cursor = connection.cursor()
    print("Hey, database is connected now!")
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
    print("Database tables are ready to go!")

# Add a new user to the login table
def addLogin(connection, cursor, id, level, username, password):
    try:
        cursor.execute("INSERT INTO login VALUES (?, ?, ?, ?)", (id, level, username, password))
        connection.commit()
        print(f"Added user {id} - all good!")
    except sqlite3.IntegrityError:
        print(f"Oops, user {id} is already in there.")

# Check if login credentials are valid
def attemptLogin(cursor, id, password):
    cursor.execute("SELECT * FROM login WHERE staff_id = ? AND password = ?", (id, password))
    user = cursor.fetchone()
    if user:
        print("Login worked!")
        return user  # Returns the entire user row
    print("Login failed, sorry.")
    return None

# Add a furniture item to the database
def addFurniture(connection, cursor, id, type, colour, price):
    try:
        cursor.execute("INSERT INTO furniture VALUES (?, ?, ?, ?)", (id, type, colour, price))
        connection.commit()
        print(f"Furniture item {id} added!")
    except sqlite3.IntegrityError:
        print(f"Whoops, furniture {id} is already there.")

# Get all furniture items from the database
def returnFurniture(cursor):
    cursor.execute("SELECT * FROM furniture")
    stuff = cursor.fetchall()
    return stuff

# Close the database connection when done
def closeDatabase(connection):
    connection.close()
    print("Database closed, see ya!")