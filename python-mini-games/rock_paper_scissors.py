
import random


def get_rounds():
    while True:
        try:
            rounds = int(input("Enter an odd number of rounds: "))

            if rounds > 0 and rounds % 2 != 0:
                return rounds

            print("Please enter a positive odd number.")

        except ValueError:
            print("Please enter a valid whole number.")


def get_player_choice():
    choices = ["rock", "paper", "scissors"]

    while True:
        choice = input(
            "Choose rock, paper, or scissors: "
        ).lower()

        if choice in choices:
            return choice

        print("Invalid choice. Try again.")


def play_round():
    choices = ["rock", "paper", "scissors"]

    player = get_player_choice()
    computer = random.choice(choices)

    print("You chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")
        return "tie"

    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("You win this round!")
        return "player"

    else:
        print("Computer wins this round!")
        return "computer"


def play_game(rounds):
    player_wins = 0
    computer_wins = 0

    target = rounds // 2 + 1

    while player_wins < target and computer_wins < target:
        print("\n--- NEW ROUND ---")

        result = play_round()

        if result == "player":
            player_wins += 1

        elif result == "computer":
            computer_wins += 1

        print("Your wins:", player_wins)
        print("Computer wins:", computer_wins)

    print("\n--- GAME OVER ---")

    if player_wins > computer_wins:
        print("Congratulations! You won the game!")

    else:
        print("The computer won the game!")


def main():
    print("WELCOME TO ROCK PAPER SCISSORS!")

    rounds = get_rounds()
    play_game(rounds)


if __name__ == "__main__":
    main()
