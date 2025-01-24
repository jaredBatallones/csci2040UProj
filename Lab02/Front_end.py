


def data(Codes):
        print("Please select from the following options: list, specific")
        valid = False
        while valid == False:
            option = input()
            if option == "list":
                valid = True
                for x, obj in Codes.items():
                    print(x)

                for y in obj:
                    print(y + ':', obj[y])
            elif (option == "specific"):
                valid = True
                print("select SIC code")
                id = input()
                filter(lambda ID: ID['SIC Code'] == id, Codes)
            else:
                print("Error: not an option")
                

