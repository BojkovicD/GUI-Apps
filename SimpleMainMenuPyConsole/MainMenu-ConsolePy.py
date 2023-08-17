#Creating menu in python3 for console apps

#1. Start the game
#2. About the company
#3. Exit

def Mainmenu():
    print("1. Start the game\n2. About the company\n3. Exit\n*************")
    choice = input()
    if choice == "1":
        StartTheGame()
    elif choice == "2":
        AboutTheCompany()
    elif choice == "3":
        Exit()
    else:
        Mainmenu()
def StartTheGame():
    print("Welcome to the game")
def AboutTheCompany():
    print("Welcome to the about page!")
def Exit():
    exit()



Mainmenu()