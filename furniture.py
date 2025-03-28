import sqlite3

# Updated class to represent furniture items with new columns: size and aisle.
class Furniture:
    def __init__(self, furniture_id, type, colour, price, size="", aisle=""):
        self.furniture_id = furniture_id
        self.type = type
        self.colour = colour
        self.price = price
        self.size = size
        self.aisle = aisle

    # String representation for printing furniture details
    def __str__(self):
        return (f"ID: {self.furniture_id}, Type: {self.type}, Colour: {self.colour}, "
                f"Price: ${float(self.price):.2f}, Size: {self.size}, Aisle: {self.aisle}")
    
    def __eq__(self, other):
        if str(self) == str(other):
            return True
        else:
            return False

    # Getter and setter methods for furniture attributes
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
    cursor.execute("SELECT * FROM furniture")
    raw_stuff = cursor.fetchall()
    furniture_list = []
    for row in raw_stuff:
        # Assuming the new columns are at index 4 and 5.
        furniture_list.append(Furniture(row[0], row[1], row[2], row[3], row[4], row[5]))
    return furniture_list

# Sort furniture items alphabetically by type
def sort_furniture_by_type(furniture_list):
    for i in range(len(furniture_list)):
        for j in range(i + 1, len(furniture_list)):
            if furniture_list[j].get_type() < furniture_list[i].get_type():
                furniture_list[i], furniture_list[j] = furniture_list[j], furniture_list[i]
    return furniture_list

# Sort furniture items by price (lowest to highest)
def sort_furniture_by_price(furniture_list):
    for i in range(len(furniture_list)):
        for j in range(i + 1, len(furniture_list)):
            if furniture_list[j].get_price() < furniture_list[i].get_price():
                furniture_list[i], furniture_list[j] = furniture_list[j], furniture_list[i]
    return furniture_list

# Add a new furniture item to the database
def add_furniture(connection, cursor, furniture_id, type, colour, price, size="", aisle=""):
    try:
        cursor.execute("INSERT INTO furniture VALUES (?, ?, ?, ?, ?, ?)", 
                       (furniture_id, type, colour, price, size, aisle))
        connection.commit()
        return True
    except sqlite3.IntegrityError:
        return False

# Update an existing furniture item
def update_furniture(connection, cursor, furniture_id, type, colour, price, size, aisle):
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
    try:
        cursor.execute("DELETE FROM furniture WHERE furniture_id = ?", (furniture_id,))
        connection.commit()
        return True
    except sqlite3.Error:
        return False

# Search furniture by keyword (searching type and colour)
def search_furniture(cursor, keyword):
    cursor.execute("SELECT * FROM furniture WHERE type LIKE ? OR colour LIKE ?", 
                   (f'%{keyword}%', f'%{keyword}%'))
    raw_stuff = cursor.fetchall()
    furniture_list = []
    for row in raw_stuff:
        furniture_list.append(Furniture(row[0], row[1], row[2], row[3], row[4], row[5]))
    return furniture_list
