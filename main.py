import random
Choices = ["Rock", "Paper", "Scissors"]
computer_score = 0
player_score = 0
print("To end Game enter end")
while True:
    player_choice = input("Rock, Paper or  Scissors?").capitalize()
    computer_choice = random.choice(Choices)
    if player_choice == computer_choice:
        print("Tie!")
    elif player_choice == "Rock":
        if computer_choice == "Paper":
            print("You lose!", computer_choice, "covers", player_choice)
            computer_score += 1
        else:
            print("You win!", player_choice, "smashes", computer_choice)
            player_score += 1
    elif player_choice == "Paper":
        if computer_choice == "Scissors":
            print("You lose!", computer_choice, "cut", player_choice)
            computer_score += 1
        else:
            print("You win!", player_choice, "covers", computer_choice)
            player_score += 1
    elif player_choice == "Scissors":
        if computer_choice == "Rock":
            print("You lose...", computer_choice, "smashes", player_choice)
            computer_score += 1
        else:
            print("You win!", player_choice, "cut", computer_choice)
            player_score += 1
    elif player_choice == 'End':
        print("Final Scores:")
        print(f"Computer Score is :{computer_score}")
        print(f"Player Score is r:{player_score}")

        if computer_score == player_score:
            print("Game Tie :")
        elif computer_score > player_score:
            print("Computer Win the Game:")
        else:
            print("player Win the Game:")
        break
