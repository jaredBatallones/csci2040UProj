import csv

file_path = "industry_sic.csv"

def read_database(file_path):
    catalog = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            catalog.append(row)
    return catalog

def write_database(file_path, row):
    catalog = read_database(file_path)
    catalog.append(row)
    with open(file_path, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(catalog)
    return