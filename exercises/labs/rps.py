import random
from enum import Enum
class Choice(Enum):
    PAPER = 0
    SCISSORS = 1
    ROCK = 2

choice_options = [0, 1, 2]

def get_user_choice(player):
    choice = None
    while not(choice in choice_options):
        input_value = input("{}, enter one of the following: (0) - paper, (1) - scissors, (2) - rock: ".format(player))
        if input_value.isnumeric(): 
            input_value = int(input_value)
        if input_value in choice_options:
            choice = input_value
            print("{} choice is {}".format(player, Choice(choice).name))
            return choice
        else:
            print("Choose correct option")

def get_computer_choice():
    computer_choice = random.choice(choice_options)
    print("Computer choice is {}".format(Choice(computer_choice).name))
    return computer_choice

def get_winner(user_choice, computer_choice):
    # (0) - paper, (1) - scissors, (2) - rock
    if user_choice == computer_choice:
        print("Both players chose {}".format(Choice(computer_choice).name))
    elif user_choice == 0: #0
        if computer_choice == 1:
            print("Computer won! Scissors > Paper")
        else:
            print("You won! Rock > Paper")
    elif user_choice == 1: #1
        if computer_choice == 0:
            print("You won! Scissors > Paper")
        else:
            print("Computer won! Rock > Scissors")
    elif user_choice == 2: #2
        if computer_choice == 1:
            print("You won! Rock > Scissors")
        else:
            print("Computer won! Paper > Rock")


user_choice1 = get_user_choice("Witold")
# user_choice2 = get_user_choice("Jaher")

computer_choice = get_computer_choice()

get_winner(user_choice1, computer_choice)

# get_winner(user_choice1, user_choice2)