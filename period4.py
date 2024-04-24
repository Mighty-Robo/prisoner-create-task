print("Welcome to the Silly Billy County prisoner records system")
prisonerList = ["Jack Nelson", "Brooke Silly", "Lucas Bucas"]


def nav():
    choice = input("Would you like to view the current prisoner list (1) or register a new prisoner? (2) ")
    return choice
# ^ function that lets you choose options

 
def Prison (pList):
    logout = False
    while logout == False:
        option = nav()
        if option == "1":
            print(prisonerList) #shows prisoner list
            logoutQ = input("Log out? Y/N: ") #allows user to stop program
            if logoutQ == "Y":
                logout = True
    
        elif option == "2": #allows user to add prisoner
            new_prisoner = input("What is the prisoners name? ") 
            pList.insert(0,new_prisoner)
            print("New prisoner has been added to list: " + new_prisoner)
            print(prisonerList)
            logoutQ = input("Log out? Y/N: ")
            if logoutQ == "Y":
                logout = True

Prison (prisonerList) #feed logout into the function directly. it DOES NOT WORK WITHOUT THIS
