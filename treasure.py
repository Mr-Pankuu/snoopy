print("Welcome to Treasure island game.\nYour mission is to find the treasure")
choice = input("Choose a path left or right : ")
if choice == "left":
    print("You choose a right way ")
    choice = input("Do you want wait for the boat or swim : ")
    if choice == "wait":
        print("Now you waiting for the boat you choose right ")
        print("You arrived at your destination")
        choice = input("now you choose Right door Blue or Red or Yellow : ")
        if choice == "yellow":
            print("Hurrey! You find the treasure .")
        elif choice == "red":
            print("Red is the wrong choice.")
        else:
            print("Blue is the wrong choice.")
    else:
        print("You meet with the crocodile")
else:
    print("Right is wrong way to finding the treasure")
