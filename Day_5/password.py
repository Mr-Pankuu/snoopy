from random import choice, shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '-', '^', '*', '+']
print("Welcome to the Pypassword Generator!")
nr_letter = int(input("How many letters would you like in your password\n"))
nr_symbols = int(input("How many symbols would you like in your password\n"))
nr_number = int(input("How many numbers would you like in your password\n"))

# For EasyPassword generator

#password = " "
# for char in range(1, nr_letter + 1):
#   password += random.choice(letters)

# for char in range(1, nr_number + 1):
#   password += random.choice(numbers)

# for char in range(1, nr_symbols +1):
#   password += random.choice(symbols)

# print(password)

# For Herd Password Generation

password_list = []
for char in range(1, nr_letter + 1):
    password_list += choice(letters)

for char in range(1, nr_number + 1):
    password_list += choice(numbers)

for char in range(1, nr_symbols + 1):
    password_list += choice(symbols)

shuffle(password_list)
password = " "
for char in password_list:
    password += char
print(f"Your password is : {password}")
