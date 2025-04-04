import sqlite3

class Login:
    """
    Represents a login credential for a staff user in the system.

    Attributes:
    ----------
    staff_id : int
        Unique ID for the staff member.
    level : int
        Access level of the staff member (1 = admin, 5 = warehouse employee).
    username : str
        Login username.
    password : str
        Login password.
    """

    def __init__(self, staff_id, level, username, password):
        """
        Constructor for the Login class.

        Parameters:
        ----------
        staff_id : int
            Staff's unique identifier.
        level : int
            Staff's access level.
        username : str
            Staff's username.
        password : str
            Staff's password.
        """
        self.staff_id = staff_id
        self.level = level
        self.username = username
        self.password = password

    def __str__(self):
        """
        Return a readable string representation of the Login object.

        Returns:
        -------
        str
            Formatted string including ID, username, password, and access level.
        """
        levels = {
            1: 'admin',
            2: 'manager',
            3: 'employee',
            4: 'inventory_manager',
            5: 'warehouse_employee'
        }
        return f"ID: {self.staff_id}, Username: {self.username}, Password: {self.password}, Access Level: {levels.get(self.level, 'unknown')}"

    def __eq__(self, other):
        """
        Compare two Login objects based on their string representation.

        Parameters:
        ----------
        other : Login
            Another Login object.

        Returns:
        -------
        bool
            True if all fields match, otherwise False.
        """
        return str(self) == str(other)

    # Getter and Setter methods
    def get_staff_id(self):
        """Returns the staff ID."""
        return self.staff_id

    def set_staff_id(self, staff_id):
        """Sets the staff ID."""
        self.staff_id = staff_id

    def get_level(self):
        """Returns the access level."""
        return self.level

    def set_level(self, level):
        """Sets the access level."""
        self.level = level

    def get_username(self):
        """Returns the username."""
        return self.username

    def set_username(self, username):
        """Sets the username."""
        self.username = username

    def get_password(self):
        """Returns the password."""
        return self.password

    def set_password(self, password):
        """Sets the password."""
        self.password = password


def get_login_list(cursor):
    """
    Retrieve all logins from the database and return as a list of Login objects.

    Parameters:
    ----------
    cursor : sqlite3.Cursor
        Active database cursor.

    Returns:
    -------
    list of Login
        List of Login objects fetched from the login table.
    """
    cursor.execute("SELECT * FROM login")
    raw_stuff = cursor.fetchall()
    login_list = [Login(row[0], row[1], row[2], row[3]) for row in raw_stuff]
    return login_list


def add_login(connection, cursor, staff_id, level, username, password):
    """
    Add a new user to the login table.

    Parameters:
    ----------
    connection : sqlite3.Connection
        Active database connection.
    cursor : sqlite3.Cursor
        Active database cursor.
    staff_id : int
        Unique identifier for the user.
    level : int
        Access level.
    username : str
        Login username.
    password : str
        Login password.

    Returns:
    -------
    bool
        True if successful, False if user already exists.
    """
    try:
        cursor.execute("INSERT INTO login VALUES (?, ?, ?, ?)", (staff_id, level, username, password))
        connection.commit()
        return True
    except sqlite3.IntegrityError:
        return False


def remove_login(connection, cursor, staff_id):
    """
    Remove a user from the login table by staff ID.

    Parameters:
    ----------
    connection : sqlite3.Connection
        Active database connection.
    cursor : sqlite3.Cursor
        Active database cursor.
    staff_id : int
        ID of the user to remove.

    Returns:
    -------
    bool
        True if successful, False if an error occurred.
    """
    try:
        cursor.execute("DELETE FROM login WHERE staff_id = ?", (staff_id,))
        connection.commit()
        return True
    except sqlite3.Error:
        return False


def initialize_users(connection, cursor):
    """
    Populate the login table with a predefined set of users.

    This is typically used for resetting the login table in testing mode.

    Parameters:
    ----------
    connection : sqlite3.Connection
        Active database connection.
    cursor : sqlite3.Cursor
        Active database cursor.
    """
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
