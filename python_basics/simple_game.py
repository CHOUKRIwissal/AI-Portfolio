import random

score_player = 0
score_computer = 0
round_number = 1
total_rounds = 3

def menu_chooses():
    global score_player, score_computer, round_number

    print("ROCK PAPER SCISSORS\n")
    print(f"Best of {total_rounds} rounds\n")

    while round_number <= total_rounds:

        print(f"\nRound {round_number}")
        print("1- Rock \n2- Paper \n3- Scissors \n4- Quit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 4:
            print("\nThank you for playing!")
            return

        if choice == 1:
            player = "rock"
        elif choice == 2:
            player = "paper"
        elif choice == 3:
            player = "scissors"
        else:
            print("Invalid choice. Please choose 1-4.")
            continue

        computer = random.choice(["rock", "paper", "scissors"])

        print(f"\nYour choice: {player}")
        print(f"Computer choice: {computer}")

        if player == computer:
            print("\nIt's a draw!")

        elif (
            (player == "rock" and computer == "scissors")
            or (player == "paper" and computer == "rock")
            or (player == "scissors" and computer == "paper")
        ):
            score_player += 1
            print("\nYou win this round!")

        else:
            score_computer += 1
            print("\nComputer wins this round!")

        print("\nScore")
        print(f"You: {score_player}")
        print(f"Computer: {score_computer}")
        print("\n" + "-"*30)

        round_number += 1

    # Show final results
    print("\n" + "-"*30)
    print("FINAL RESULT")
    print("-"*30)
        
    print(f"Player Score: {score_player}")
    print(f"Computer Score: {score_computer}")
        
    if score_player > score_computer:
        print("\n FINAL WINNER: YOU! ")
    elif score_computer > score_player:
        print("\n FINAL WINNER: COMPUTER! ")
    else:
        print("\n THE MATCH IS A DRAW! ")

menu_chooses()
