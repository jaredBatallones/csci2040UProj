# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 03:31:48 2025

@author: Wei Cui
"""

import random
import sqlite3
import os
import sys

# --- Database Setup Functions (similar to your existing code) ---

def loadDatabase(test=False):
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
    """Inserts generated sample data into the furniture table."""
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
    connection, cursor = loadDatabase(test=True)
    initializeDatabase(connection, cursor)
    data = generate_sample_data(100)
    insert_sample_data(connection, cursor, data)
    connection.close()
    print("Database connection closed.")