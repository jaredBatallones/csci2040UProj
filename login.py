import sqlite3

# Simple class to represent login details
class Login:
    def __init__(self, staff_id, level, username, password):
        self.staff_id = staff_id
        self.level = level
        self.username = username
        self.password = password

    def __str__(self):
        levels = {
            1: 'admin',
            2: 'manager',
            3: 'employee',
            4: 'inventory_manager',
            5: 'warehouse_employee'
        }
        return f"ID: {self.staff_id}, Username: {self.username}, Password: {self.password}, Access Level: {levels.get(self.level, 'unknown')}"

    def __eq__(self, other):
        return str(self) == str(other)

    def get_staff_id(self):
        return self.staff_id

    def get_level(self):
        return self.level

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password


def get_login_list(cursor):
    cursor.execute("SELECT * FROM login")
    rows = cursor.fetchall()
    return [Login(*row) for row in rows]

def add_login(connection, cursor, staff_id, level, username, password):
    try:
        cursor.execute("INSERT INTO login VALUES (?, ?, ?, ?)", (staff_id, level, username, password))
        connection.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def remove_login(connection, cursor, staff_id):
    try:
        cursor.execute("DELETE FROM login WHERE staff_id = ?", (staff_id,))
        connection.commit()
        return True
    except sqlite3.Error:
        return False

def initialize_users(connection, cursor):
    # Clear the existing login table to ensure fresh data
    cursor.execute("DELETE FROM login")
    users = [
        (1, 1, "testAdmin", "pass123"),       # Admin
        (2, 2, "testManager", "pass456"),     # Manager
        (3, 3, "testEmployee", "pass789"),    # Employee
        (4, 4, "testInventory", "pass101"),   # Inventory Manager
        (5, 5, "testWarehouse", "pass202")    # Warehouse Employee
    ]
    cursor.executemany("INSERT INTO login VALUES (?, ?, ?, ?)", users)
    connection.commit()
    print("Initialized users: ", [f"ID: {user[0]}" for user in users])

def attemptLogin(cursor, identifier, password):
    """
    Allows login using either staff_id (if numeric) or username (if string).
    """
    if identifier.isdigit():
        cursor.execute("SELECT * FROM login WHERE staff_id = ? AND password = ?", (int(identifier), password))
    else:
        cursor.execute("SELECT * FROM login WHERE username = ? AND password = ?", (identifier, password))

    row = cursor.fetchone()
    if row:
        print("Authentication successful.")
        return Login(*row)
    print("Authentication failed. Please verify your credentials and try again.")
    return None
