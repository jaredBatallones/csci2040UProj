from databasefunction import returnFurniture

# Simple class for furniture items
class Furniture:
    def __init__(self, furniture_id, type, colour, price):
        self.furniture_id = furniture_id
        self.type = type
        self.colour = colour
        self.price = price

    # How it looks when printed
    def __str__(self):
        return f"ID: {self.furniture_id}, Type: {self.type}, Colour: {self.colour}, Price: ${self.price:.2f}"
    
    # get and set functions
    def get_furniture_id(self):
        return self.furniture_id
    
    def set_furniture_id(self, furniture_id):
        self.furniture_id = furniture_id
        return
    
    def get_type(self):
        return self.type
    
    def set_type(self, type):
        self.type = type
        return
    
    def get_colour(self):
        return self.colour
    
    def set_colour(self, colour):
        self.colour = colour
        return
    
    def get_price(self):
        return self.price
    
    def set_price(self, price):
        self.price = price
        return

# Grab all furniture from the database and turn it into objects
def get_furniture_list(cursor):
    raw_stuff = returnFurniture(cursor)
    furniture_list = []
    for row in raw_stuff:
        furniture_list.append(Furniture(row[0], row[1], row[2], row[3]))
    return furniture_list

# Sort furnitures by price
def sort_furniture_by_price(furniture_list):
    for i in range(len(furniture_list)):
        for j in range(i+1,len(furniture_list)):
            if furniture_list[j].get_price() < furniture_list[i].get_price():
                furniture_list[i], furniture_list[j] = furniture_list[j], furniture_list[i]
    return furniture_list