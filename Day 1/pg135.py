print("Welcome in love calculator :")
name1 = input("Enter your name : ")
name2 = input("Enter there name : ")

#Here combined the string and then convert in lower case
combined_case_string = name1 + name2
lower_case_string = combined_case_string.lower()

#Here we are using the .count() function to calculate the no.
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

#Now for love

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = str(true)  + str(love)

print("Your ")