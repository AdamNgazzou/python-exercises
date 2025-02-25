import random


def play():
    while(True):
        computer_choice=random.choice(["rock", "paper", "scissors"])
        player = input("enter rock , paper or scissors(or 'q' to quit ): ")
        while((player!='rock' and player!='paper' and player!='scissors') and player !='q'):
            player = input("enter rock , paper or scissors(or 'q' to quit 2): ")
        if(player=="q"):
            break
        print("computer choose "+computer_choice)
        if player == computer_choice:
            print ("It's a tie!")
        elif (player == "rock" and computer_choice == "scissors") or \
             (player == "scissors" and computer_choice == "paper") or \
             (player == "paper" and computer_choice == "rock"):
            print ("You win!")
        else:
            print ("You lose!")
play()
