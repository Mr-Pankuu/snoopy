import random
word_list = ["pankaj","dheeraj","neeraj"]

choosen_word = random.choice(word_list)
print(f'pssst, the solution is {choosen_word}')

display = []
word_length= (choosen_word)
for _ in range(len(str(word_length))):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:

    guess = input("Guess a letter: ").lower()

    for position in range(len(str(word_length))):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")