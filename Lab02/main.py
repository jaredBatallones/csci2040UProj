import Front_end
import import_csv

csvFile = import_csv.read_database("Lab02/catalogue_data.csv")

while True:
    print("View, Add, or Delete?: ")

    userInput = input()

    if userInput.lower() == "view":
        Front_end.data(csvFile)
        print("\n--------------------------")

    elif userInput.lower() == "add":
        #add()
        print("\n--------------------------")

    elif userInput.lower() == "delete":
        #delete()
        print("\n--------------------------")
    else:
        print("Invalid input\n--------------------------")