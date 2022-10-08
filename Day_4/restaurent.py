import random
while 1:
    names_string = input("Give me everybody's name , separated by comma. ")
    names = names_string.split(", ")
    num_items = len(names) - 1
    random_choice = random.randint(0, num_items)
    person = names[random_choice]
    print(person + " " + "is pay the bill for tonight dinner!\n")