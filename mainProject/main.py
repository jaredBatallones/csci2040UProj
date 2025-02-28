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

def inputLoop(connection, cursor, user):
    while True:
        userInput = input("Add/View/Exit?: ")
        if userInput == "Add":
            addFurn(connection, cursor)
        elif userInput == "View":
            furniture = databaseFunctions.returnFurniture(cursor)
            for i in furniture:
                print(i)
        elif userInput == "Exit":
            print("o7")
            break
        else:
            print("Invalid input.\n")

def addFurn(connection, cursor):
    databaseFunctions.addFurniture(connection, cursor, input("ID: "), input("Type: "), input("Colour: "), input("Price: "))

levels = ["N/A", "Admin"]
connection, cursor = databaseFunctions.loadDatabase()

#databaseFunctions.initializeDatabase(cursor)
#databaseFunctions.addLogin(connection, cursor, 100826687, 1, "jaredBatallones", "superSecurePW5")
#databaseFunctions.addFurniture(connection, cursor, 1, "couch", "green", 440.99)

currentLogin = loginLoop(cursor)
print(f"Welcome {currentLogin[2]}")
print(f"Permission Level: {levels[currentLogin[1]]}\n")

inputLoop(connection, cursor, currentLogin)



connection.close()