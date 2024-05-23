import random
dice = input("Do you want to roll a dice?")
while dice == "yes":
    no = random.randint(1,6)
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    elif no == 2:
        print("[-----]")
        print("[     ]")
        print("[ 0 0 ]")
        print("[     ]")
        print("[-----]")
    
    elif no == 3:
        print("[-----]")
        print("[     ]")
        print("[0  0  0]")
        print("[     ]")
        print("[-----]")
    elif no == 4:
        print("[-----]")
        print("[ 0  0 ]")
        print("[ 0  0 ]")
        print("[     ]")
        print("[-----]")
    elif no == 5:
        print("[-----]")
        print("[ 0  0 ]")
        print("[  0 ]")
        print("[ 0  0 ]")
        print("[-----]")

    elif no == 6:
        print("[-----]")
        print("[ 0  0  0]")
        print("[ 0  0  0 ]")
        print("[     ]")
        print("[-----]")
    response = input("Would you like to stop?y/n")
    if response == "n":
        break
    


