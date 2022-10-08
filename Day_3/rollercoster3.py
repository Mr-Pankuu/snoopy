print("Welcome to the roller cosster ! ")
height = int(input("What is your height in cm? "))
age = int(input("What is your age in years? "))
bill = 0
if height > 120:
    print("You can ride the rollercoster")
    if age < 12:
        bill = 5
        print("Your ticket fee is 5$")
    if age >= 18:
        bill = 10
        print("your ticket fee is 10$")
    if age < 18:
        bill = 12
        print("Your ticket fee is 12$")
    photo = input("Do you want a picture (it take only 3$)? Y for yes or N for no ")
    if photo == "y": 
        bill = bill + 3

        print(f"Your total bill is :{bill}")
else:
    print("Sorry you can not ride the roller cosster ")
