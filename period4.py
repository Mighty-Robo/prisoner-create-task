print("Welcome to the Silly Billy County prisoner records system")
prisonerList = ["Jack Nelson", "Brooke Silly", "Lucas Bucas"]

logout = False
while logout == False:
    def nav():
        choice = input("Would you like to view the current prisoner list (1) or register a new prisoner? (2) ")
        return choice

    option = nav()

    def addPrisoner (prisoner, pList):
    
        pList.insert(0,new_prisoner)
        return pList
    
    if option == "1":
        print(prisonerList)
        logoutQ = input("Log out? Y/N: ")
        if logoutQ == "Y":
            logout = True
    
    elif option == "2":
        new_prisoner = input("What is the prisoners name? ")
        addPrisoner(new_prisoner, prisonerList)
        print("New prisoner has been added to list: " + new_prisoner)
        print(prisonerList)
        logoutQ = input("Log out? Y/N: ")
        if logoutQ == "Y":
            logout = True

    
