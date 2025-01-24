import csv

file_path = "catalog_data.csv"

# Function to read data from the CSV file
def read_database(file_path):
    catalog = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Validate that required fields are present
                if all(key in row for key in ["ID", "Name", "Description"]):
                    catalog.append(row)
                else:
                    print(f"Skipping invalid row: {row}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return catalog

# Main execution
if __name__ == "__main__":
    # Read data from csv
    data = read_database(file_path)
    
    # Print the catalog data
    print("Catalog Data:")
    if data:
        for item in data:
            print(f"ID: {item['ID']}, Name: {item['Name']}, Description: {item['Description']}")
    else:
        print("No valid data found in the file.")
