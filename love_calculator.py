print("Welcome in love calculator :")
name1 = input("Enter your name : ")
name2 = input("Enter there name : ")

# Here combined the string and then convert in lower case
combined_case_string = name1 + name2
lower_case_string = combined_case_string.lower()

# Here we are using the .count() function to calculate the no.
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

# Now for love
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)
love_score = int(love_score)

if (love_score > 40) and (love_score < 50):
    print(f"Your love score is  {love_score} , You alright go together")
elif (love_score > 30) and (love_score < 90):
    print(f"Your love score is {love_score}, You go together like coke")
else:
    print(f"Your love score is  {love_score}")
