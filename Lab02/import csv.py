import csv

file_path = "catalog_data.csv"

def read_database(file_path):
    catalog = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            catalog.append(row)
    return catalog

# Test
data = read_database(file_path)
print("Catalog Data:", data)
