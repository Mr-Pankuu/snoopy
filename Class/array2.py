from array import*
stud_roll = array("i", [])
n = int(input("How many elements you want :"))
for i in range(n):
    stud_roll.append(int(input("Enter elements  :")))
    g = len(stud_roll)
for j in range(g):
    print(stud_roll[j])
    