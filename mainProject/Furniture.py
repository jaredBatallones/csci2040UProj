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

# Grab all furniture from the database and turn it into objects
def get_furniture_list(cursor):
    raw_stuff = returnFurniture(cursor)
    furniture_list = []
    for row in raw_stuff:
        furniture_list.append(Furniture(row[0], row[1], row[2], row[3]))
    return furniture_list