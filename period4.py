print("Welcome to the Silly Billy County prisoner sorting system")
prisonerList = ["Jack Nelson", "Brooke Silly", "Lucas Cameron"]
nav = input("Would you like to view the current prisoner list (A) or register a new prisoner? (B)").lower()
if nav == "A" :
    print(prisonerList)