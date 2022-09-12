print("Welcome to python pizza Deliveries")
size = input("What size pizza do you want? S, M or L  : ")
add_pepperoni = input("Do you want to add pepperoni? Y or N : ")
extra_cheese = input("Do you want to add extra cheese? Y or N : ")
bill = 0
if size == "s":
    bill += 15
    print("Small pizza : $15")
elif size == "m":
    bill += 20
    print("Medium pizza : $20")
elif size == "l":
    bill += 25
    print("Large pizza : $25")
else:
    print("Unknown key pressed")


if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3
if extra_cheese == "y":
    bill += 1
print(f"Total bill for your pizza is : $ {bill}")
