print("Welcome to the roller cosster ! ")
height = int(input("What is your height in cm? "))
age = int(input("What is your age in years? "))
if height > 120:
    print("You can ride the rollercoster")
    if age >= 18:
        print("your ticket fee is 10$")
    else:
        print("Your ticket fee is 8$")
else:
    print("Sorry you can not ride the roller cosster ")
    