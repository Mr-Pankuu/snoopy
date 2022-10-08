import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

choose = int(input("Select 0 for rock , 1 for paper and 2 for scissors \n"))

if choose >= 3 or choose < 0 :
    print("You are not give the valid number")
else:
    print(game_images[choose])
    computer_choice = random.randint(0, 2)
    print(f"Computer choose {computer_choice}")
    print(game_images[computer_choice])



    if  choose == 0 and computer_choice == 2:
        print("You Win")
    elif computer_choice == 0 and computer_choice == 2:
        print("You lose")

    elif computer_choice > choose:
        print("You win")
    elif choose > computer_choice:
        print("You loose")
    elif choose > computer_choice:
        print("You win:")
    elif computer_choice == choose:
        print("Match is draw")
