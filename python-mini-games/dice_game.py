
import random


# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)


# Function to play the game
def play_game():
    print("WELCOME TO THE DICE GAME!")

    player_score = 0
    computer_score = 0

    while True:
        try:
            rounds = int(input("How many rounds do you want to play? "))

            if rounds > 0:
                break

            print("Please enter a number greater than zero.")

        except ValueError:
            print("Please enter a valid whole number.")

    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number}")

        player_roll = roll_dice()
        computer_roll = roll_dice()

        print("You rolled:", player_roll)
        print("Computer rolled:", computer_roll)

        if player_roll > computer_roll:
            print("You win this round!")
            player_score += 1

        elif computer_roll > player_roll:
            print("Computer wins this round!")
            computer_score += 1

        else:
            print("This round is a tie!")

    print("\n--- FINAL SCORE ---")
    print("Your score:", player_score)
    print("Computer score:", computer_score)

    if player_score > computer_score:
        print("Congratulations! You won the game!")

    elif computer_score > player_score:
        print("The computer won the game!")

    else:
        print("The game ended in a tie!")


# Main function
def main():
    play_game()


if __name__ == "__main__":
    main()
