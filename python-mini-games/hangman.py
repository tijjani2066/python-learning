
import random


WORDS = {
    "python": "A popular programming language",
    "function": "A reusable block of code",
    "variable": "A named place that stores data",
    "computer": "An electronic device used for computing",
    "keyboard": "An input device used for typing"
}

MAX_ATTEMPTS = 8


def display_word(word, guessed_letters):
    displayed = ""

    for letter in word:
        if letter in guessed_letters:
            displayed += letter + " "
        else:
            displayed += "_ "

    print("\nWord:", displayed)


def get_letter(guessed_letters):
    while True:
        letter = input("\nGuess one letter: ").lower().strip()

        if len(letter) != 1 or not letter.isalpha():
            print("Please enter only one letter.")
        
        elif letter in guessed_letters:
            print("You have already guessed that letter.")

        else:
            return letter


def play_game():
    word = random.choice(list(WORDS.keys()))
    hint = WORDS[word]

    guessed_letters = set()
    wrong_guesses = set()

    print("\nWELCOME TO HANGMAN!")
    print("Hint:", hint)

    while len(wrong_guesses) < MAX_ATTEMPTS:
        display_word(word, guessed_letters)

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word!")
            print("The word was:", word)
            return

        print("Wrong guesses:", sorted(wrong_guesses))
        print("Attempts remaining:", MAX_ATTEMPTS - len(wrong_guesses))

        letter = get_letter(guessed_letters)

        guessed_letters.add(letter)

        if letter in word:
            print("Correct letter!")

        else:
            print("That letter is not in the word.")
            wrong_guesses.add(letter)

    print("\nGame over!")
    print("The correct word was:", word)


def main():
    while True:
        play_game()

        play_again = input(
            "\nWould you like to play again? (yes/no): "
        ).strip().lower()

        if play_again != "yes":
            print("Thanks for playing Hangman!")
            break


if __name__ == "__main__":
    main()
