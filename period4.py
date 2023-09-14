print("Welcome to the Silly Billy County prisoner sorting system")
prisonerList = ["Jack Nelson", "Brooke Silly", "Lucas Cameron"]
nav = input("Would you like to view the current prisoner list (1) or register a new prisoner? (2)")
if nav == "1":
    print(prisonerList)
elif nav == "2":
    new_prisoner = input("What is the prisoners name?")
    prisonerList.insert(0,new_prisoner)
    print(prisonerList)