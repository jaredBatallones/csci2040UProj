import Front_end

def checkInput(input):
    if input.lower() == "view":
        Front_end.data()
        print("\n--------------------------")

    elif input.lower() == "add":
        add()
        print("\n--------------------------")

    elif input.lower() == "delete":
        delete()
        print("\n--------------------------")
    else:
        print("Invalid input\n--------------------------")

while True:
    checkInput(input())