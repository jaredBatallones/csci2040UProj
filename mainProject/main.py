import databasefunction as db
import furniture
import login
import random

# Main function to execute the Furniture Inventory & Management System
def main():
    # Establish database connection and cursor
    connection, cursor = db.loadDatabase()
    db.initializeDatabase(connection, cursor)

    # Check if test data exists before adding – avoids duplicate messages
    cursor.execute("SELECT COUNT(*) FROM login WHERE staff_id = 1")
    if cursor.fetchone()[0] == 0:
        db.addLogin(connection, cursor, 1, 1, "testAdmin", "pass123")
    cursor.execute("SELECT COUNT(*) FROM login WHERE staff_id = 2")
    if cursor.fetchone()[0] == 0:
        db.addLogin(connection, cursor, 2, 2, "testManager", "pass456")
    cursor.execute("SELECT COUNT(*) FROM login WHERE staff_id = 3")
    if cursor.fetchone()[0] == 0:
        db.addLogin(connection, cursor, 3, 3, "testEmployee", "pass789")
    cursor.execute("SELECT COUNT(*) FROM furniture WHERE furniture_id = 101")
    if cursor.fetchone()[0] == 0:
        db.addFurniture(connection, cursor, 101, "Chair", "Black", 49.99)
    cursor.execute("SELECT COUNT(*) FROM furniture WHERE furniture_id = 102")
    if cursor.fetchone()[0] == 0:
        db.addFurniture(connection, cursor, 102, "Table", "Brown", 99.99)
    #populate(connection, cursor, 10)

    # Continue program execution until the user chooses to exit
    while True:
        print("\n=== Furniture Inventory & Management System ===")
        print("1. Authenticate User")
        print("2. Exit Application")
        choice = input("Please select an option (1 or 2): ")

        if choice == "1":
            staff_id = input("Please enter your Staff ID: ")
            password = input("Please enter your Password: ")
            user = db.attemptLogin(cursor, staff_id, password)

            if user:
                print(f"Welcome, {user[2]}. You have successfully logged in with access level {user[1]}.")
                logged_in_menu(cursor, user[1], connection)  # Pass connection for database operations
            else:
                print("Authentication failed. Please verify your Staff ID and Password and try again.")
                #redundant. either this or the database function should print the error message, not both.
        
        elif choice == "2":
            print("Thank you for using the Furniture Inventory & Management System. Goodbye.")
            break
        
        else:
            print("Invalid selection. Please choose option 1 or 2.")

# Menu for authenticated users with expanded functionality
def logged_in_menu(cursor, user_level, connection):
    while True:
        print("\n=== System Options ===")
        print("1.  View All Furniture Items")
        print("2.  View a Specific Furniture Item")
        print("3.  Sort Furniture Items")  # New feature for sorting by type/price
        print("4.  Search Furniture Items")  # New feature for keyword search
        if user_level <= 2: #Only show options for the user's access level.
            print("5.  Add New Furniture Item")  # New feature for adding items
            print("6.  Modify Existing Furniture Item")  # New feature for editing items
            print("7.  Remove Furniture Item")  # New feature for removing items
        if user_level <= 1: #Only show options for the user's access level.
            print("8.  View Logins")
            print("9.  Add Login")  # New feature for adding users
            print("10. Delete Login")
        print("11. Log Out")
        choice = input("Please select an option (1-11): ")

        #View Furniture List
        if choice == "1":
            furniture_list = furniture.get_furniture_list(cursor)
            if furniture_list:
                print("\n=== List of All Furniture Items ===")
                for item in furniture_list:
                    print(item)
            else:
                print("No furniture items are currently registered in the system.")
        
        # View Furniture by ID
        elif choice == "2":
            furniture_id = input("Please enter the Furniture Item ID: ")
            furniture_list = furniture.get_furniture_list(cursor)
            found_it = False
            for item in furniture_list:
                if str(item.furniture_id) == furniture_id:
                    print("\n=== Details of the Specified Furniture Item ===")
                    print(item)
                    found_it = True
                    break
            if not found_it:
                print("The specified Furniture Item ID was not found.")
        
        # Sort furniture by type or price
        elif choice == "3":
            print("\n=== Sort Furniture Items ===")
            print("1. Sort by Type")
            print("2. Sort by Price")
            sort_choice = input("Please select a sorting option (1 or 2): ")
            furniture_list = furniture.get_furniture_list(cursor)
            if sort_choice == "1":
                sorted_list = furniture.sort_furniture_by_type(furniture_list)
            elif sort_choice == "2":
                sorted_list = furniture.sort_furniture_by_price(furniture_list)
            else:
                print("Invalid selection. Please choose option 1 or 2.")
                continue
            print("\n=== Sorted List of Furniture Items ===")
            for item in sorted_list:
                print(item)

        # Search furniture by keyword (type or colour)
        elif choice == "4":
            print("\n=== Search Furniture Items ===")
            keyword = input("Please enter a keyword (e.g., type or colour): ").lower()
            furniture_list = furniture.get_furniture_list(cursor)
            matches = []
            for item in furniture_list:
                if keyword in item.get_type().lower() or keyword in item.get_colour().lower():
                    matches.append(item)
            if matches:
                print("\n=== Search Results ===")
                for item in matches:
                    print(item)
            else:
                print("No matching furniture items were found.")
        
        # Add a furniture item
        elif choice == "5":
            if user_level <= 2:
                print("\n=== Add New Furniture Item ===")
                furniture_id = input("Please enter the Furniture Item ID: ")
                type = input("Please enter the Furniture Type (e.g., Chair, Table): ")
                colour = input("Please enter the Colour (e.g., Black, Brown): ")
                try:
                    price = float(input("Please enter the Price (e.g., 49.99): "))
                    db.addFurniture(connection, cursor, furniture_id, type, colour, price)
                    print("The new furniture item has been successfully added to the system.")
                except ValueError:
                    print("Error: The price must be a valid number. Please try again.")
            else:
                print("You do not have the required access level to perform this operation.")

        # Edit an existing furniture item
        elif choice == "6":
            if user_level <= 2:
                print("\n=== Modify Existing Furniture Item ===")
                furniture_id = input("Please enter the Furniture Item ID to modify: ")
                furniture_list = furniture.get_furniture_list(cursor)
                found_it = False
                for item in furniture_list:
                    if str(item.furniture_id) == furniture_id:
                        print(f"Current details: {item}")
                        new_type = input("Please enter a new Type (press Enter to retain current): ") or item.get_type()
                        new_colour = input("Please enter a new Colour (press Enter to retain current): ") or item.get_colour()
                        new_price = input("Please enter a new Price (press Enter to retain current): ") or item.get_price()
                        if new_price:
                            try:
                                new_price = float(new_price)
                            except ValueError:
                                print("Error: The price must be a valid number. Retaining current price.")
                                new_price = item.get_price()
                        cursor.execute("UPDATE furniture SET type = ?, colour = ?, price = ? WHERE furniture_id = ?", 
                                    (new_type, new_colour, new_price, furniture_id))
                        connection.commit()
                        print("The furniture item has been successfully updated.")
                        found_it = True
                        break
                if not found_it:
                    print("The specified Furniture Item ID was not found.")
            else:
                print("You do not have the required access level to perform this operation.")

        # Remove a furniture item
        elif choice == "7":
            if user_level <= 2:
                print("\n=== Remove Furniture Item ===")
                furniture_id = input("Please enter the Furniture Item ID to remove: ")
                cursor.execute("DELETE FROM furniture WHERE furniture_id = ?", (furniture_id,))
                connection.commit()
                print("The furniture item has been removed from the system (if it existed).")
            else:
                print("You do not have the required access level to perform this operation.")

        if choice == "8":
            if user_level <= 1:
                login_list = login.get_login_list(cursor)
                if login_list:
                    print("\n=== List of All Users ===")
                    for item in login_list:
                        print(item)
                else:
                    print("No furniture items are currently registered in the system.")
            else:
                print("You do not have the required access level to perform this operation.")

        # Add a new user login
        elif choice == "9":
            if user_level <= 1:
                print("\n=== Add New Login ===")
                staff_id = input("Please enter the Staff ID: ")
                level = input("Please enter the Access Level (1 for Admin, 2 for Manager or 3 for Admin): ")
                username = input("Please enter the Username: ")
                password = input("Please enter the Password: ")
                db.addLogin(connection, cursor, staff_id, level, username, password)
                print("The new login has been successfully added to the system.")
            else:
                print("You do not have the required access level to perform this operation.")

        elif choice == "10":
            if user_level <= 1:
                print("\n=== Remove User ===")
                staff_id = input("Please enter the Staff ID to remove: ")
                cursor.execute("DELETE FROM login WHERE staff_id = ?", (staff_id,))
                connection.commit()
                print("The user has been removed from the system (if it existed).")
            else:
                print("You do not have the required access level to perform this operation.")

        elif choice == "11":
            print("You have been successfully logged out of the system.")
            break

        else:
            print("Invalid selection. Please choose an option between 1 and 11.")
            
# Generate a random list of furniture objects
def generate_list(List_length):
    generated_list = []
    for x in range(List_length):
        id = random.randrange(1,9999)
        colour_num = random.randrange(1,5)
        colour = ""
        match colour_num:
            case 1:
                colour = "White"
            case 2:
                colour = "Black"
            case 3:
                colour = "Brown"
            case 4:
                colour = "Red"
            case 5:
                colour = "Grey"
        type_num = random.randrange(1,5)
        type = ""
        match type_num:
            case 1:
                type = "Chair"
            case 2:
                type = "Table"
            case 3:
                type = "Shelf"
            case 4:
                type = "Sofa"
            case 5:
                type = "Cabinet"
        
        base_price = random.randrange(4,20)
        price = base_price * 5 + .99
        rand_furniture = furniture.Furniture(id,type,colour,price)
        generated_list.append(rand_furniture)
    return generated_list

def populate(connection, cursor, n):
    rand_items = generate_list(n)
    for item in rand_items: 
        print(f"Adding {item}")
        db.addFurniture(connection, cursor, item.get_furniture_id(), item.get_type(), item.get_colour(), item.get_price())
        print(f"Test Item {item} Added")


# Start the program
if __name__ == "__main__":
    main()