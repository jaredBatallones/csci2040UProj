def data(Codes):
        print("Please select from the following options: list, specific")
        valid = False
        while valid == False:
            option = input()
            if option == "list":
                
                for x, obj in Codes.items():
                    print(x)

                for y in obj:
                    print(y + ':', obj[y])
                valid = True
            elif (option == "specific"):
               
                print("select SIC code")
                id = input()
                filter(lambda ID: ID['SIC Code'] == id, Codes)
                valid = True
            else:
                print("Error: not an option")
                

