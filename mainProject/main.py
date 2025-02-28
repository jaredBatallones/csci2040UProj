import databasefunction as db
import furniture

# Main chunk of the program
def main():
    # Get the database going
    connection, cursor = db.loadDatabase()
    db.initializeDatabase(connection, cursor)

    # Toss in some test data to play with
    db.addLogin(connection, cursor, 1, 1, "admin", "pass123")
    db.addLogin(connection, cursor, 2, 2, "manager", "pass456")
    db.addFurniture(connection, cursor, 101, "Chair", "Black", 49.99)
    db.addFurniture(connection, cursor, 102, "Table", "Brown", 99.99)

    # Keep running until they quit
    while True:
        print("\n=== Furniture Inventory Thing ===")
        print("1. Login")
        print("2. Get outta here")
        choice = input("What do you want to do? ")

        if choice == "1":
            staff_id = input("Staff ID: ")
            password = input("Password: ")
            user = db.attemptLogin(cursor, staff_id, password)

            if user:
                print(f"Hey {user[2]}, you’re in! (Level {user[1]})")
                logged_in_menu(cursor, user[1])
            else:
                print("Wrong ID or password, try again.")
        
        elif choice == "2":
            print("See ya later!")
            break
        
        else:
            print("Huh? Pick 1 or 2.")

    db.closeDatabase(connection)

# Menu after they log in
def logged_in_menu(cursor, user_level):
    while True:
        print("\n=== What Now? ===")
        print("1. See all furniture")
        print("2. Check one furniture item")
        print("3. Log out")
        choice = input("Pick something: ")

        if choice == "1":
            furniture_list = furniture.get_furniture_list(cursor)
            if furniture_list:
                print("\n=== Here’s Everything ===")
                for item in furniture_list:
                    print(item)
            else:
                print("Nothing in here yet!")
        
        elif choice == "2":
            furniture_id = input("Gimme the furniture ID: ")
            furniture_list = furniture.get_furniture_list(cursor)
            found_it = False
            for item in furniture_list:
                if str(item.furniture_id) == furniture_id:
                    print("\n=== Here’s That Item ===")
                    print(item)
                    found_it = True
                    break
            if not found_it:
                print("Couldn’t find that one.")
        
        elif choice == "3":
            print("Logging you out now...")
            break
        
        else:
            print("Pick a real option, c’mon.")

# Start the whole thing
if __name__ == "__main__":
    main()

