import random


choices = ["rock", "paper", "scissors"]

def turn():
    """
    Completes the turn of the player and returns the player's choice
    """
    print("It's round " + str(round) + ".")
    choice = input("Rock... Paper... Scissors... SHOOT!: ").lower()

    while not choice.isalpha() or (choice != "rock" and choice != "paper" and choice != "scissors"):

        if not choice.isalpha():
            choice = input("Please use letters. Choose rock, paper, or scissors: ")

        elif choice != "rock" and choice != "paper" and choice != "scissors":
            choice = input("Invalid input. Choose rock, paper, or scissors: ")

    return choice



################################################################################

print("Hello! Let's play Rock-Paper-Scissors, what's your name?")
player = input("My name is ")
print("Hello " + player + " and good luck!\n")
round = 1

def play():
    """
    Controls the gameplay.
    """

    choice = turn()
    comp_choice = random.choice(choices)

    #tie
    if choice == comp_choice:
        print("The computer chose " + comp_choice + " too! It's a tie!")

    #if computer picks rock which beats scissors but loses to paper
    if comp_choice == "rock":
        if choice == "scissors":
            print("Rock smashes scissors, you lost this round.")
        elif choice == "paper":
            print("Paper covers rock, you won this round!")

    #if computer picks Paper which beats rock but loses to scissors
    if comp_choice == "paper":
        if choice == "rock":
            print("Paper covers rock, you lost this round.")
        elif choice == "scissors":
            print("Scissors cuts paper, you won this round!")

    #if computer picks scissors
    if comp_choice == "scissors":
        if choice == "paper":
            print("Scissors cuts paper, you lost this round.")
        elif choice == "rock":
            print("Rock smashes scissors, you won this round!")




if __name__ == '__main__':
    play()
    while input("Play Again? (y/n) ").lower() == "y":
        round = round+1
        play()
