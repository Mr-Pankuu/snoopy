year=int(input("Write the year which you want to check leap year"))
if year % 4 == 0:
    if year % 100 == 0:  
        if year % 400 == 0: 
            print(year," is a leap year")
    else:
        print("is not leap year")
else:
    print(year, " is not leap year ")