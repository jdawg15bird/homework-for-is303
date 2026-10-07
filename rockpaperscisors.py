import random


def get_player_choice():
    choice = input("Enter rock, paper, scissors: ")
    choice = choice.lower()

    while choice != "rock" and choice != "paper" and choice != "scissors":
        print("Sorry, that is not a valid choice. Please try again.")
        choice = input("Enter rock, paper, scissors: ")
        choice = choice.lower()

    return choice


def determine_winner(player, computer):
    if player == computer:
        return "tie"

    elif player == "rock" and computer == "scissors":
        return "win"

    elif player == "paper" and computer == "rock":
        return "win"

    elif player == "scissors" and computer == "paper":
        return "win"

    else:
        return "loss"


print("Welcome to Rock Paper Scissors!")

rounds = int(input("How many rounds would you like to play: "))

while rounds % 2 == 0:
    print("Sorry, the number must be an odd number.")
    rounds = int(input("Please try again: "))

player_wins = 0
computer_wins = 0
rounds_played = 0

while rounds_played < rounds:

    player = get_player_choice()

    computer_number = random.randint(1, 3)

    if computer_number == 1:
        computer = "rock"
    elif computer_number == 2:
        computer = "paper"
    else:
        computer = "scissors"

    print("The computer chose", computer)

    result = determine_winner(player, computer)

    if result == "win":
        print("You won!")
        player_wins = player_wins + 1
        rounds_played = rounds_played + 1

    elif result == "loss":
        print("You lost!")
        computer_wins = computer_wins + 1
        rounds_played = rounds_played + 1

    else:
        print("Tie! Play again.")


print("-------------------------------------------")
print("Score - You:", player_wins, "| Computer:", computer_wins)

if player_wins > computer_wins:
    print("You win!!!")
else:
    print("Computer wins!!!")

print("Thanks for playing!")