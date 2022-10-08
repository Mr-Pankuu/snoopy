#start
word_list = ["pankaj", "dheeraj", "neeraj"]
# randomly choose a word from the word_list and 
# assign it to a variable called choosen word
import random 
choosen_word = random.choice(word_list)
print(choosen_word)

# Ask the user to guess the letter and assign 
# their answer to a variable called guess. 
# make guess in lower letter

guess = input("Guess a letter : ").lower()
#check if the letter the user guessed is 
# one of the letters in the chosen_word.

for letter in choosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
