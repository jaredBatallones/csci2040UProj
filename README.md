# csci2040UProj
Furniture Store Managment System:


Overview:  

(Furniture Store Managment System) is an office application, created to help manage the inventory of a small to medium retail store. It's goal is to document, track, add or remove furniture and other items from a small to medium furniture shop. The program asks for a login and gives varies permissions based on their roles. For example, Admin could edit everything, add or remove entries, view the database. Managers do everything Admin can do, but also add or remove users. Employees can only view the database. Login right now is based on ID only. Right now it is only text-based, in iteration 1. But the final project will be a GUI-based application in future iterations.

Features
User Authentication: Secure login for different access levels, right now based on ID, but will add username in the future.
Inventory Management: Add, edit, and remove furniture items.
Sorting & Filtering: Sort items by type or price.
Search Functionality: Keyword-based search type in known key words, like (type, colour etc) the data base will return results.
Role-Based Access Control: Permission depends on the user’s roles and access level.
Database Integration: Uses SQLite to store data.
Planned Enhancements: Transition to a GUI interface, more detailed database schema, and comprehensive unit testing.

Prerequisites
Python 3.6 or higher
SQLite3 (included with Python) git clone https://github.com/yourusername/fims.git
(Optional) Git for version control

To get it to work:
1) Clone the Repository:
-git clone https://github.com/yourusername/fims.git
2) run the app:
-python main.py

Interaction:
Upon running it will ask the user to login : "Please select an option (1 or 2)"
it only accepts ID for now. no usernames.
enter 1, 2, or 3.
ID 1 is admin, ID 2 is manager, ID 3 is employee.

For admin, use Staff ID: 1 and Password: pass123
For manager, use Staff ID: 2 and Password: pass456
For employee, use Staff ID: 3 and Password: pass789

once logged in, one would be presents with up to 11 options, depending on user access level
"=== System Options ===
1.  View All Furniture Items
2.  View a Specific Furniture Item
3.  Sort Furniture Items
4.  Search Furniture Items
5.  Add New Furniture Item
6.  Modify Existing Furniture Item
7.  Remove Furniture Item
8.  View Logins
9.  Add Login
10. Delete Login
11. Log Out
Please select an option (1-11):"

enter number 1 to 11. Number entry will give desired output from database or Log out. 
to logout select 11.
To exit, logout and then select 2 "Exit Application".

Sample output is below 
( 

The database connection has been successfully established.
The database tables have been successfully initialized.

=== Furniture Inventory & Management System ===
1. Authenticate User
2. Exit Application
Please select an option (1 or 2): 1
Please enter your Staff ID: 1
Please enter your Password: pass123
Authentication successful.
Welcome, testAdmin. You have successfully logged in with access level 1.

=== System Options ===
1.  View All Furniture Items
2.  View a Specific Furniture Item
3.  Sort Furniture Items
4.  Search Furniture Items
5.  Add New Furniture Item
6.  Modify Existing Furniture Item
7.  Remove Furniture Item
8.  View Logins
9.  Add Login
10. Delete Login
11. Log Out
Please select an option (1-11): 1

=== List of All Furniture Items ===
ID: 1, Type: couch, Colour: green, Price: $440.99
ID: 2, Type: chair, Colour: grey, Price: $100.99
ID: 77, Type: Sofa, Colour: Red, Price: $70.99
ID: 101, Type: Chair, Colour: Black, Price: $49.99
ID: 102, Type: Table, Colour: Brown, Price: $99.99
ID: 3485, Type: Sofa, Colour: Red, Price: $35.99
ID: 3859, Type: Table, Colour: White, Price: $60.99
ID: 3951, Type: Table, Colour: White, Price: $25.99
ID: 4306, Type: Chair, Colour: Red, Price: $90.99
ID: 5256, Type: Sofa, Colour: Red, Price: $60.99
ID: 6458, Type: Chair, Colour: Red, Price: $20.99
ID: 6893, Type: Shelf, Colour: Brown, Price: $30.99
ID: 7136, Type: Sofa, Colour: White, Price: $50.99
ID: 7330, Type: Chair, Colour: Black, Price: $40.99
ID: 8086, Type: Shelf, Colour: White, Price: $40.99
Invalid selection. Please choose an option between 1 and 11.

=== System Options ===
1.  View All Furniture Items
2.  View a Specific Furniture Item
3.  Sort Furniture Items
4.  Search Furniture Items
5.  Add New Furniture Item
6.  Modify Existing Furniture Item
7.  Remove Furniture Item
8.  View Logins
9.  Add Login
10. Delete Login
11. Log Out
Please select an option (1-11): 6

=== Modify Existing Furniture Item ===
Please enter the Furniture Item ID to modify: 3951
Current details: ID: 3951, Type: Table, Colour: White, Price: $25.99
Please enter a new Type (press Enter to retain current): Couch
Please enter a new Colour (press Enter to retain current): Grey
Please enter a new Price (press Enter to retain current): 40.99
The furniture item has been successfully updated.
Invalid selection. Please choose an option between 1 and 11.

=== System Options ===
1.  View All Furniture Items
2.  View a Specific Furniture Item
3.  Sort Furniture Items
4.  Search Furniture Items
5.  Add New Furniture Item
6.  Modify Existing Furniture Item
7.  Remove Furniture Item
8.  View Logins
9.  Add Login
10. Delete Login
11. Log Out
Please select an option (1-11): 1

=== List of All Furniture Items ===
ID: 1, Type: couch, Colour: green, Price: $440.99
ID: 2, Type: chair, Colour: grey, Price: $100.99
ID: 77, Type: Sofa, Colour: Red, Price: $70.99
ID: 101, Type: Chair, Colour: Black, Price: $49.99
ID: 102, Type: Table, Colour: Brown, Price: $99.99
ID: 3485, Type: Sofa, Colour: Red, Price: $35.99
ID: 3859, Type: Table, Colour: White, Price: $60.99
ID: 3951, Type: Couch, Colour: Grey, Price: $40.99
ID: 4306, Type: Chair, Colour: Red, Price: $90.99
ID: 5256, Type: Sofa, Colour: Red, Price: $60.99
ID: 6458, Type: Chair, Colour: Red, Price: $20.99
ID: 6893, Type: Shelf, Colour: Brown, Price: $30.99
ID: 7136, Type: Sofa, Colour: White, Price: $50.99
ID: 7330, Type: Chair, Colour: Black, Price: $40.99
ID: 8086, Type: Shelf, Colour: White, Price: $40.99
Invalid selection. Please choose an option between 1 and 11.

=== System Options ===
1.  View All Furniture Items
2.  View a Specific Furniture Item
3.  Sort Furniture Items
4.  Search Furniture Items
5.  Add New Furniture Item
6.  Modify Existing Furniture Item
7.  Remove Furniture Item
8.  View Logins
9.  Add Login
10. Delete Login
11. Log Out
Please select an option (1-11): 8

=== List of All Users ===
ID: 1, Username: testAdmin, Password: pass123, Access Level: admin
ID: 2, Username: testManager, Password: pass456, Access Level: manager
ID: 3, Username: testEmployee, Password: pass789, Access Level: employee
ID: 100826687, Username: jaredBatallones, Password: superSecurePW5, Access Level: admin

=== System Options ===
1.  View All Furniture Items
2.  View a Specific Furniture Item
3.  Sort Furniture Items
4.  Search Furniture Items
5.  Add New Furniture Item
6.  Modify Existing Furniture Item
7.  Remove Furniture Item
8.  View Logins
9.  Add Login
10. Delete Login
11. Log Out
Please select an option (1-11): 11
You have been successfully logged out of the system.

=== Furniture Inventory & Management System ===
1. Authenticate User
2. Exit Application
Please select an option (1 or 2): 2
Thank you for using the Furniture Inventory & Management System. Goodbye.
)