#!/usr/bin/env python3

# computer needs to make a choice
# choices need to be evaluated
# print out the result (who won)

import random

def main():
    """body of the game"""
    
    #point=0 #variable to keep trak of useer point
    #cpoint=0 #variable to keep track of of CPU point

    while point ! = 4:

    choice = input("Rock, Paper, or Scissors?\n>")
    botchoice = random.choice(["rock", "paper", "scissors"])

    choice = choice.lower() # validates input by forcing input to be lower case

    #print(choice)
    print(botchoice)

    if choice not in ["rock", "paper", "scissors"]:
        print("You entered an invalid choice, you lose(r)!")

    elif choice == "scissors" and botchoice == "paper":
        print("You win!")

    elif choice == "scissors" and botchoice == "rock":
        print("You lose!")

    #elif choice == "scissors" and botchoice == "scissors":
        print("Tie!")
 
    elif choice == "rock" and botchoice == "paper":
        print("You lose!")

    #elif choice == "rock" and botchoice == "rock":
        print("Tie!")

    elif choice == "rock" and botchoice == "scissors":
        print("You win!")
 
    #elif choice == "paper" and botchoice == "paper":
        print("Tie!")

    elif choice == "paper" and botchoice == "rock":
        print("You win!")

    elif choice == "paper" and botchoice == "scissors":
        print("You win!")

    else:
        print("Tie!")

main()
