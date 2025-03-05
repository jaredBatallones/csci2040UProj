import databasefunction as db
import furniture

# Main function to execute the Furniture Inventory & Management System
def main():
    # Establish database connection and cursor
    connection, cursor = db.loadDatabase()
    db.initializeDatabase(connection, cursor)

    # Check if test data exists before adding – avoids duplicate messages
    cursor.execute("SELECT COUNT(*) FROM login WHERE staff_id = 1")
    if cursor.fetchone()[0] == 0:
        db.addLogin(connection, cursor, 1, 1, "admin", "pass123")
    cursor.execute("SELECT COUNT(*) FROM login WHERE staff_id = 2")
    if cursor.fetchone()[0] == 0:
        db.addLogin(connection, cursor, 2, 2, "manager", "pass456")
    cursor.execute("SELECT COUNT(*) FROM furniture WHERE furniture_id = 101")
    if cursor.fetchone()[0] == 0:
        db.addFurniture(connection, cursor, 101, "Chair", "Black", 49.99)
    cursor.execute("SELECT COUNT(*) FROM furniture WHERE furniture_id = 102")
    if cursor.fetchone()[0] == 0:
        db.addFurniture(connection, cursor, 102, "Table", "Brown", 99.99)

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
        
        elif choice == "2":
            print("Thank you for using the Furniture Inventory & Management System. Goodbye.")
            break
        
        else:
            print("Invalid selection. Please choose option 1 or 2.")

# Menu for authenticated users with expanded functionality
def logged_in_menu(cursor, user_level, connection):
    while True:
        print("\n=== System Options ===")
        print("1. View All Furniture Items")
        print("2. View a Specific Furniture Item")
        print("3. Log Out")
        print("4. Add New Furniture Item")  # New feature for adding items
        print("5. Modify Existing Furniture Item")  # New feature for editing items
        print("6. Remove Furniture Item")  # New feature for removing items
        print("7. Sort Furniture Items")  # New feature for sorting by type/price
        print("8. Search Furniture Items")  # New feature for keyword search
        choice = input("Please select an option (1-8): ")

        if choice == "1":
            furniture_list = furniture.get_furniture_list(cursor)
            if furniture_list:
                print("\n=== List of All Furniture Items ===")
                for item in furniture_list:
                    print(item)
            else:
                print("No furniture items are currently registered in the system.")
        
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
        
        elif choice == "3":
            print("You have been successfully logged out of the system.")
            break
        
        # New feature: Add a furniture item
        elif choice == "4":
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

        # New feature: Edit an existing furniture item
        elif choice == "5":
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

        # New feature: Remove a furniture item
        elif choice == "6":
            print("\n=== Remove Furniture Item ===")
            furniture_id = input("Please enter the Furniture Item ID to remove: ")
            cursor.execute("DELETE FROM furniture WHERE furniture_id = ?", (furniture_id,))
            connection.commit()
            print("The furniture item has been removed from the system (if it existed).")

        # New feature: Sort furniture by type or price
        elif choice == "7":
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

        # New feature: Search furniture by keyword (type or colour)
        elif choice == "8":
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
        
        else:
            print("Invalid selection. Please choose an option between 1 and 8.")

# Start the program
if __name__ == "__main__":
    main()