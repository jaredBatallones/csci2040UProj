import sqlite3
import databaseFunctions

def loginLoop(cursor):
    permissionLevel = 0
    while permissionLevel == 0:

        user = databaseFunctions.attemptLogin(cursor, input("ID Number: "), input("Password: "))
        if user != 0:
            permissionLevel = user[1]
        if permissionLevel > 0:
            break
        print("Login Failed.\n")
    return user

levels = ["N/A", "Admin"]
connection, cursor = databaseFunctions.loadDatabase()

#databaseFunctions.initializeDatabase(cursor)
#databaseFunctions.addLogin(connection, cursor, 100826687, 1, "jaredBatallones", "superSecurePW5")

currentLogin = loginLoop(cursor)
print(f"Welcome {currentLogin[2]}")
print(f"Permission Level: {levels[currentLogin[1]]}")

connection.close()