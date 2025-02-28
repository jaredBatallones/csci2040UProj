import sqlite3

def loadDatabase():
    connection = sqlite3.connect("mainProject/data/placeholderData.db")
    cursor = connection.cursor()

    print("Database connected.")

    return connection, cursor

def initializeDatabase(cursor):
    command = """CREATE TABLE login (
    staff_id INTEGER PRIMARY KEY,
    level INTEGER,
    username VARCHAR(30),
    password VARCHAR(30));"""

    cursor.execute(command)

    print("Database Initialized")

def addLogin(connection, cursor, id, level, username, password):
    cursor.execute("INSERT INTO login VALUES (?, ?, ?, ?)", (id, level, username, password))
    connection.commit()

    print(f"User {id} added")

def attemptLogin(cursor, id, password):
    cursor.execute("SELECT * FROM login")

    users = cursor.fetchall()

    for user in users:
        if int(user[0]) == int(id) and user[3] == password:
            return user
    return 0
    