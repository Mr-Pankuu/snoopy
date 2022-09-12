print("Welcome to the tip calculator!")
bill = float(input("What was the total amount ? "))
tip = int(input("How much you want to give to the tip ? 10, 12 ,or 15 : "))
people = int(input("How many people to split the bill :"))
total_tip_percent = tip / 100
total_bill = bill+total_tip_percent
bill_per_person = total_bill / people
final = round(bill_per_person,2)
print(f" Each person should be given $ :" {final})