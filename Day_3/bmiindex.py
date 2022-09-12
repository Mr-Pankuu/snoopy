print("BMI calculator:-")
h = input("What is your height in m : ")
w = input("What is  your weight in kg : ")
h1 = float(h)
w1 = float(w)
bmi1 = w1/ h1**2
bmi2 = float(bmi1)
bmi= round(bmi2, 2)
if bmi <= 18 :
    print("you are under waeight",bmi)
elif bmi <= 24:
    print("you are normal weight",bmi)
elif bmi <= 30:
    print("You are over weight",bmi)
elif bmi <= 35:
    print("You are obssess weight",bmi)
else:
    print("You dont enter the correct data")