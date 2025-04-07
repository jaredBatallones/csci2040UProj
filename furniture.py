import sqlite3

# Updated class to represent furniture items with new columns: size and aisle.
class Furniture:
    """
    Represents a furniture item with all relevant attributes.

    Attributes
    ----------
    furniture_id : int
        Unique ID of the furniture item.
    type : str
        Type of the furniture (e.g., Chair, Table).
    colour : str
        Colour of the furniture.
    price : float
        Price of the item.
    size : str
        Size descriptor (e.g., Small, Medium, Large).
    aisle : str
        Aisle location in the warehouse/store.
    """
    def __init__(self, furniture_id, type, colour, price, size="", aisle=""):
        """
        Constructor for the Furniture class.

        Parameters
        ----------
        furniture_id : int
            Unique identifier of the furniture item.
        type : str
            Type of the furniture.
        colour : str
            Colour of the furniture.
        price : float
            Price of the furniture.
        size : str, optional
            Size of the furniture (default is "").
        aisle : str, optional
            Aisle location (default is "").
        """
        self.furniture_id = furniture_id
        self.type = type
        self.colour = colour
        self.price = price
        self.size = size
        self.aisle = aisle

    # String representation for printing furniture details
    def __str__(self):
        """
        Return a human-readable string representation of the furniture item.
        """
        return (f"ID: {self.furniture_id}, Type: {self.type}, Colour: {self.colour}, "
                f"Price: ${float(self.price):.2f}, Size: {self.size}, Aisle: {self.aisle}")
    
    def __eq__(self, other):
        """
        Compare this furniture item with another based on string representation.

        Parameters
        ----------
        other : Furniture
            Another furniture item to compare with.

        Returns
        -------
        bool
            True if all fields match, False otherwise.
        """
        if str(self) == str(other):
            return True
        else:
            return False

    # Getter and setter methods for furniture attributes
    """
    Just a bunch of getters and setters
    """
    def get_furniture_id(self):
        return self.furniture_id

    def set_furniture_id(self, furniture_id):
        self.furniture_id = furniture_id

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colour

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_aisle(self):
        return self.aisle

    def set_aisle(self, aisle):
        self.aisle = aisle

# Fetch all furniture from the database and convert to Furniture objects
def get_furniture_list(cursor):
    """
    Fetch all furniture records from the database.

    Parameters
    ----------
    cursor : sqlite3.Cursor
        Active database cursor.

    Returns
    -------
    list of Furniture
        List of Furniture objects retrieved from the database.
    """
    cursor.execute("SELECT * FROM furniture")
    raw_stuff = cursor.fetchall()
    furniture_list = []
    for row in raw_stuff:
        # Assuming the new columns are at index 4 and 5.
        furniture_list.append(Furniture(row[0], row[1], row[2], row[3], row[4], row[5]))
    return furniture_list

# Sort furniture items alphabetically by type
def sort_furniture_by_type(furniture_list):
    """
    Sort furniture alphabetically by type.

    Parameters
    ----------
    furniture_list : list of Furniture
        List of furniture items.

    Returns
    -------
    list of Furniture
        Sorted list of furniture by type.
    """
    for i in range(len(furniture_list)):
        for j in range(i + 1, len(furniture_list)):
            if furniture_list[j].get_type() < furniture_list[i].get_type():
                furniture_list[i], furniture_list[j] = furniture_list[j], furniture_list[i]
    return furniture_list

# Sort furniture items by price (lowest to highest)
def sort_furniture_by_price(furniture_list):
    """
    Sort furniture from lowest to highest price.

    Parameters
    ----------
    furniture_list : list of Furniture
        List of furniture items.

    Returns
    -------
    list of Furniture
        Sorted list of furniture by price.
    """
    
    for i in range(len(furniture_list)):
        for j in range(i + 1, len(furniture_list)):
            if furniture_list[j].get_price() < furniture_list[i].get_price():
                furniture_list[i], furniture_list[j] = furniture_list[j], furniture_list[i]
    return furniture_list

# Add a new furniture item to the database
def add_furniture(connection, cursor, furniture_id, type, colour, price, size="", aisle=""):
    """
    Add a new furniture record to the database.

    Parameters
    ----------
    connection : sqlite3.Connection
        Active database connection.
    cursor : sqlite3.Cursor
        Active database cursor.
    furniture_id : int
        ID for the new furniture.
    type : str
        Type of the furniture.
    colour : str
        Colour of the furniture.
    price : float
        Price of the furniture.
    size : str, optional
        Size (default is "").
    aisle : str, optional
        Aisle (default is "").

    Returns
    -------
    bool
        True if insertion succeeded, False if ID already exists.
    """
    try:
        cursor.execute("INSERT INTO furniture VALUES (?, ?, ?, ?, ?, ?)", 
                       (furniture_id, type, colour, price, size, aisle))
        connection.commit()
        return True
    except sqlite3.IntegrityError:
        return False

# Update an existing furniture item
def update_furniture(connection, cursor, furniture_id, type, colour, price, size, aisle):
    """
    Update an existing furniture record.

    Parameters
    ----------
    connection : sqlite3.Connection
        Active database connection.
    cursor : sqlite3.Cursor
        Active database cursor.
    furniture_id : int
        ID of the furniture to update.
    type : str
        Updated type.
    colour : str
        Updated colour.
    price : float
        Updated price.
    size : str
        Updated size.
    aisle : str
        Updated aisle.

    Returns
    -------
    bool
        True if update succeeded, False otherwise.
    """
    try:
        cursor.execute(
            "UPDATE furniture SET type = ?, colour = ?, price = ?, size = ?, aisle = ? WHERE furniture_id = ?", 
            (type, colour, price, size, aisle, furniture_id)
        )
        connection.commit()
        return True
    except sqlite3.Error:
        return False

# Remove a furniture item
def remove_furniture(connection, cursor, furniture_id):
    """
    Remove a furniture item from the database by ID.

    Parameters
    ----------
    connection : sqlite3.Connection
        Active database connection.
    cursor : sqlite3.Cursor
        Active database cursor.
    furniture_id : int
        ID of the furniture to remove.

    Returns
    -------
    bool
        True if deletion succeeded, False otherwise.
    """
    try:
        cursor.execute("DELETE FROM furniture WHERE furniture_id = ?", (furniture_id,))
        connection.commit()
        return True
    except sqlite3.Error:
        return False

# Search furniture by keyword (searching type and colour)
def search_furniture(cursor, keyword):
    """
    Search furniture items by keyword in 'type' or 'colour'.

    Parameters
    ----------
    cursor : sqlite3.Cursor
        Active database cursor.
    keyword : str
        Keyword to search for.

    Returns
    -------
    list of Furniture
        Matching furniture records.
    """
    cursor.execute("SELECT * FROM furniture WHERE type LIKE ? OR colour LIKE ?", 
                   (f'%{keyword}%', f'%{keyword}%'))
    raw_stuff = cursor.fetchall()
    furniture_list = []
    for row in raw_stuff:
        furniture_list.append(Furniture(row[0], row[1], row[2], row[3], row[4], row[5]))
    return furniture_list
