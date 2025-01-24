import Front_end
import import_csv

csvFile = import_csv.read_database()

while True:
    userInput = input()

    if userInput.lower() == "view":
        Front_end.data(csvFile)
        print("\n--------------------------")

    elif userInput.lower() == "add":
        add()
        print("\n--------------------------")

    elif userInput.lower() == "delete":
        delete()
        print("\n--------------------------")
    else:
        print("Invalid input\n--------------------------")
