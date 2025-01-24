def data(Codes):
        print("Please select from the following options: list, specific")
        valid = False
        while valid == False:
            option = input()
            if option == "list":
                
                for x, obj in Codes.items():
                    print(f"{key})

                for y in obj:
                    print(y + ':', obj[y])
                valid = True
            elif (option == "specific"):
                print("select SIC code")
                selected_code = input()
                if selected_code in Codes:
                    item = Codes[selected_code]
                    print(f"SIC Code: {selected_code}")
                    print(f"Description: {item['description']}")

                    #previous code
                #print("select SIC code")
                #id = input()
                #filter(lambda ID: ID['SIC Code'] == id, Codes)
                
                valid = True
            else:
                print("Error: not an option")
                

