height = input("Enter your hight (in meter) :")
weight = input("Enter your weight (in kg):")
# Here we are first convert the input data string to a integer and float by given another name.
height1 = float(height)
weight1 = int(weight)
#For BMI calculatin we the formula of BMI= weight/height**2 (height square)
bmi = weight1/(height1*height1)
print("Your BMI is :",bmi)