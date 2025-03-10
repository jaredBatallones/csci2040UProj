import sqlite3

# Simple class to represent login details
class Login:
    def __init__(self, staff_id, level, username, password):
        self.staff_id = staff_id
        self.level = level
        self.username = username
        self.password = password
    
    def __str__(self):
        levels = {1: 'admin', 2: 'manager', 3: 'employee', 4: 'inventory_manager', 5: 'warehouse_employee'}
        return f"ID: {self.staff_id}, Username: {self.username}, Password: {self.password}, Access Level: {levels.get(self.level, 'unknown')}"
    
    def get_staff_id(self):
        return self.staff_id
    
    def set_staff_id(self, staff_id):
        self.staff_id = staff_id
        return
    
    def get_level(self):
        return self.level
    
    def set_level(self, level):
        self.level = level
        return
    
    def get_username(self):
        return self.username
    
    def set_username(self, username):
        self.username = username
        return
    
    def get_password(self):
        return self.password
    
    def set_password(self, password):
        self.password = password
        return

def get_login_list(cursor):
    cursor.execute("SELECT * FROM login")
    raw_stuff = cursor.fetchall()
    login_list = []
    for row in raw_stuff:
        login_list.append(Login(row[0], row[1], row[2], row[3]))
    return login_list

def initialize_users(connection, cursor):
    # Clear the existing login table to ensure fresh data
    cursor.execute("DELETE FROM login")
    users = [
        (1, 1, "testAdmin", "pass123"),       # Admin
        (2, 2, "testManager", "pass456"),      # Manager
        (3, 3, "testEmployee", "pass789"),     # Employee
        (4, 4, "testInventory", "pass101"),    # Inventory Manager
        (5, 5, "testWarehouse", "pass202")     # Warehouse Employee
    ]
    cursor.executemany("INSERT INTO login VALUES (?, ?, ?, ?)", users)
    connection.commit()
    print("Initialized users: ", [f"ID: {user[0]}" for user in users])