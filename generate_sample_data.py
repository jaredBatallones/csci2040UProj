# -*- coding: utf-8 -*-
"""




Furniture Sample Data Generator and Database Initializer



This script provides tools to:
- Load and connect to a SQLite database
- Initialize the furniture table schema
- Generate random sample furniture data
- Insert that data into the database

Can be run as a standalone script to populate a test database.



"""

import random
import sqlite3
import os
import sys

# --- Database Setup Functions (similar to your existing code) ---

def loadDatabase(test=False):
    """
   Establishes a connection to the SQLite database.

   If running in a frozen environment (e.g., PyInstaller EXE),
   the database will be located relative to the executable.
   Otherwise, it’s relative to the script’s file location.

   Parameters
   ----------
   test : bool, optional
       If True, connects to a test database named 'placeholderTestData.db'.
       If False, connects to 'placeholderData.db'.

   Returns
   -------
   connection : sqlite3.Connection
       SQLite connection object.
   cursor : sqlite3.Cursor
       Cursor object used to execute SQL commands.
   """
    if getattr(sys, 'frozen', False):
        dir = os.path.dirname(sys.executable)
    else:
        dir = os.path.dirname(__file__)
    db_filename = "placeholderData.db" if not test else "placeholderTestData.db"
    db_path = os.path.join(dir, "data", db_filename)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    print("Database connection established.")
    return connection, cursor

def initializeDatabase(connection, cursor):
    """
       Drops and recreates the `furniture` table with the correct schema.
    
       This function is intended to reset the database structure and can be safely
       used during testing or setup to wipe existing data.
    
       Parameters
       ----------
       connection : sqlite3.Connection
           Active database connection.
       cursor : sqlite3.Cursor
           Cursor to execute SQL commands.
   """
    cursor.execute("DROP TABLE IF EXISTS furniture")
    cursor.execute('''CREATE TABLE IF NOT EXISTS furniture (
        furniture_id INTEGER PRIMARY KEY,
        type VARCHAR(30),
        colour VARCHAR(30),
        price FLOAT,
        size VARCHAR(30) DEFAULT '',
        aisle VARCHAR(30) DEFAULT ''
    )''')
    connection.commit()
    print("Furniture table initialized.")

# --- Script to Generate and Insert Sample Data ---

def generate_sample_data(num_entries=100):
    
    """
  Generates a list of randomized furniture entries.

  Each entry includes a unique ID and randomized values for type, colour,
  price, size, and aisle. Intended for testing or demo purposes.

  Parameters
  ----------
  num_entries : int, optional
      Number of sample furniture records to generate (default is 100).

  Returns
  -------
  list of tuple
      A list of tuples, each representing a row in the furniture table.
  """
  
  
    """Generates a list of sample furniture entries."""
    # Define possible values for each field.
    types = ["Chair", "Table", "Sofa", "Bed", "Desk", "Cabinet", "Shelf"]
    colours = ["Black", "Brown", "White", "Grey", "Blue", "Green", "Red"]
    sizes = ["Small", "Medium", "Large"]
    aisles = ["A1", "B2", "C3", "D4", "E5", "F6"]

    sample_data = []
    for i in range(1, num_entries + 1):
        # Use 'i' as a furniture_id or generate one in another way.
        furniture_id = i  
        type_val = random.choice(types)
        colour_val = random.choice(colours)
        price = round(random.uniform(10, 200), 2)
        size_val = random.choice(sizes)
        aisle_val = random.choice(aisles)
        sample_data.append((furniture_id, type_val, colour_val, price, size_val, aisle_val))
    return sample_data

def insert_sample_data(connection, cursor, data):
    """
    Inserts a list of furniture records into the database.

    Skips any record that would violate the UNIQUE constraint (duplicate ID).

    Parameters
    ----------
    connection : sqlite3.Connection
        Active database connection.
    cursor : sqlite3.Cursor
        Cursor to execute SQL commands.
    data : list of tuple
        List of records to be inserted into the furniture table.
    """
    
    for record in data:
        try:
            cursor.execute("INSERT INTO furniture VALUES (?, ?, ?, ?, ?, ?)", record)
        except sqlite3.IntegrityError:
            # If a record with the same furniture_id already exists, skip it.
            print(f"Skipping duplicate furniture_id {record[0]}")
    connection.commit()
    print("Sample data inserted.")

# --- Main Routine to Run the Script ---

if __name__ == "__main__":
    connection, cursor = loadDatabase(test=False)
    initializeDatabase(connection, cursor)
    data = generate_sample_data(100)
    insert_sample_data(connection, cursor, data)
    connection.close()
    print("Database connection closed.")