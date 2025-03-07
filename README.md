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
enter 1 or 2.
ID 1 is admin, ID 2 is manager.

For admin, use Staff ID: 1 and Password: pass123
For manager, use Staff ID: 2 and Password: pass456

once logged in, one would be presents with 9 options
"=== System Options ===
1. View All Furniture Items
2. View a Specific Furniture Item
3. Sort Furniture Items
4. Search Furniture Items
5. Add New Furniture Item
6. Modify Existing Furniture Item
7. Remove Furniture Item
9. Log Out
Please select an option (1-9):"

enter number 1 to 9. Number entry will give desired output from database or Log out. 
to logout select 9.
To exit, logout and then select 2 "Exit Application".

Sample output is below 
( 

=== Furniture Inventory & Management System ===
1. Authenticate User
2. Exit Application
Please select an option (1 or 2): 1
Please enter your Staff ID: 1
Please enter your Password: pass123
Authentication successful.
Welcome, admin. You have successfully logged in with access level 1.

=== System Options ===
1. View All Furniture Items
2. View a Specific Furniture Item
3. Sort Furniture Items
4. Search Furniture Items
5. Add New Furniture Item
6. Modify Existing Furniture Item
7. Remove Furniture Item
9. Log Out
Please select an option (1-9): 3

=== Sort Furniture Items ===
1. Sort by Type
2. Sort by Price
Please select a sorting option (1 or 2): price
Invalid selection. Please choose option 1 or 2.

=== System Options ===
1. View All Furniture Items
2. View a Specific Furniture Item
3. Sort Furniture Items
4. Search Furniture Items
5. Add New Furniture Item
6. Modify Existing Furniture Item
7. Remove Furniture Item
9. Log Out
Please select an option (1-9): 3

=== Sort Furniture Items ===
1. Sort by Type
2. Sort by Price
Please select a sorting option (1 or 2): 2

=== Sorted List of Furniture Items ===
ID: 101, Type: Chair, Colour: Black, Price: $49.99
ID: 102, Type: Table, Colour: Brown, Price: $99.99
ID: 2, Type: chair, Colour: grey, Price: $100.99
ID: 1, Type: couch, Colour: green, Price: $440.99

=== System Options ===
1. View All Furniture Items
2. View a Specific Furniture Item
3. Sort Furniture Items
4. Search Furniture Items
5. Add New Furniture Item
6. Modify Existing Furniture Item
7. Remove Furniture Item
9. Log Out
Please select an option (1-9): 4

=== Search Furniture Items ===
Please enter a keyword (e.g., type or colour): green

=== Search Results ===
ID: 1, Type: couch, Colour: green, Price: $440.99

=== System Options ===
1. View All Furniture Items
2. View a Specific Furniture Item
3. Sort Furniture Items
4. Search Furniture Items
5. Add New Furniture Item
6. Modify Existing Furniture Item
7. Remove Furniture Item
9. Log Out
Please select an option (1-9): 9
You have been successfully logged out of the system.

=== Furniture Inventory & Management System ===
1. Authenticate User
2. Exit Application
Please select an option (1 or 2): 2
Thank you for using the Furniture Inventory & Management System. Goodbye.
)

 
