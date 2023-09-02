# Project:
# random, while, input, print formatting, comparison operators, break and continue

import random

play = input("do you want to play? (yes/no)")
score = 0

def pc_choice():

    random_num = random.randint(1,3)

    if random_num == 1:
        computer_choice = "paper"
    elif random_num == 2:
        computer_choice = "scissors"
    else:
        computer_choice = "rock"
    return computer_choice

while play.lower() == "yes":
    computer_choice = pc_choice()
    player_choice = input("choose |  rock/paper/scissors  |")
    print("-----------------------------------")

    if player_choice == pc_choice():
        score = score + 1
        print(f"u won!. your score is {score}")
    else:
        score = score - 1
        print(f"you lost. computer chose {computer_choice}. your score is {score}")
    print("--------------------------------------------------")
    play = input("do you want to play again? (yes/no)")

