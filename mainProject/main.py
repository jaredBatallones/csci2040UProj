import databasefunction as db
import furniture

# Main function to run the Furniture Inventory Management System
def main():
    # Set up the database connection and cursor
    connection, cursor = db.loadDatabase()
    db.initializeDatabase(connection, cursor)

    # Add some test data for demo purposes – team can modify or remove later
    db.addLogin(connection, cursor, 1, 1, "admin", "pass123")
    db.addLogin(connection, cursor, 2, 2, "manager", "pass456")
    db.addFurniture(connection, cursor, 101, "Chair", "Black", 49.99)
    db.addFurniture(connection, cursor, 102, "Table", "Brown", 99.99)

    # Keep the program running until the user chooses to exit
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
                logged_in_menu(cursor, user[1], connection)  # Pass connection for database updates
            else:
                print("Wrong ID or password, try again.")
        
        elif choice == "2":
            print("See ya later!")
            break
        
        else:
            print("Huh? Pick 1 or 2.")

# Menu for logged-in users with expanded functionality
def logged_in_menu(cursor, user_level, connection):
    while True:
        print("\n=== What Now? ===")
        print("1. See all furniture")
        print("2. Check one furniture item")
        print("3. Log out")
        print("4. Add new furniture")  # New feature for adding items
        print("5. Edit furniture")     # New feature for editing items
        print("6. Remove furniture")   # New feature for removing items
        print("7. Sort furniture")     # New feature for sorting by type/price
        print("8. Search furniture")   # New feature for keyword search
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
        
        # New feature: Add a furniture item
        elif choice == "4":
            print("\n=== Add New Furniture ===")
            furniture_id = input("Enter furniture ID: ")
            type = input("Enter furniture type (e.g., Chair, Table): ")
            colour = input("Enter colour (e.g., Black, Brown): ")
            try:
                price = float(input("Enter price (e.g., 49.99): "))
                db.addFurniture(connection, cursor, furniture_id, type, colour, price)
                print("Furniture added successfully!")
            except ValueError:
                print("Price must be a number, try again.")

        # New feature: Edit an existing furniture item
        elif choice == "5":
            print("\n=== Edit Furniture ===")
            furniture_id = input("Enter the furniture ID to edit: ")
            furniture_list = furniture.get_furniture_list(cursor)
            found_it = False
            for item in furniture_list:
                if str(item.furniture_id) == furniture_id:
                    print(f"Current details: {item}")
                    new_type = input("New type (press Enter to keep current): ") or item.get_type()
                    new_colour = input("New colour (press Enter to keep current): ") or item.get_colour()
                    new_price = input("New price (press Enter to keep current): ") or item.get_price()
                    if new_price:
                        try:
                            new_price = float(new_price)
                        except ValueError:
                            print("Price must be a number, keeping current price.")
                            new_price = item.get_price()
                    cursor.execute("UPDATE furniture SET type = ?, colour = ?, price = ? WHERE furniture_id = ?", 
                                  (new_type, new_colour, new_price, furniture_id))
                    connection.commit()
                    print("Furniture updated!")
                    found_it = True
                    break
            if not found_it:
                print("Couldn’t find that furniture item.")

        # New feature: Remove a furniture item
        elif choice == "6":
            print("\n=== Remove Furniture ===")
            furniture_id = input("Enter the furniture ID to remove: ")
            cursor.execute("DELETE FROM furniture WHERE furniture_id = ?", (furniture_id,))
            connection.commit()
            print("Furniture removed (if it existed).")

        # New feature: Sort furniture by type or price
        elif choice == "7":
            print("\n=== Sort Furniture ===")
            print("1. Sort by Type")
            print("2. Sort by Price")
            sort_choice = input("How do you want to sort? ")
            furniture_list = furniture.get_furniture_list(cursor)
            if sort_choice == "1":
                sorted_list = furniture.sort_furniture_by_type(furniture_list)
            elif sort_choice == "2":
                sorted_list = furniture.sort_furniture_by_price(furniture_list)
            else:
                print("Pick 1 or 2, try again.")
                continue
            print("\n=== Sorted Furniture ===")
            for item in sorted_list:
                print(item)

        # New feature: Search furniture by keyword (type or colour)
        elif choice == "8":
            print("\n=== Search Furniture ===")
            keyword = input("Enter a keyword (type or colour): ").lower()
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
                print("No matches found.")
        
        else:
            print("Pick a real option, c’mon.")

# Start the program
if __name__ == "__main__":
    main()