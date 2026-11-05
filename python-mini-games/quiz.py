
import random


QUESTIONS = {
    "Which keyword is used to define a function?": "def",
    "Which function displays output?": "print",
    "Which data type stores True or False?": "bool",
    "Which symbol is used for comments?": "#",
    "Which function gets input from a user?": "input",
    "Which data structure stores key-value pairs?": "dictionary",
    "Which keyword is used to repeat while a condition is true?": "while",
    "Which function converts a value to an integer?": "int"
}


def ask_question(question, correct_answer):
    print("\n" + question)

    answer = input("Your answer: ").strip().lower()

    if answer == correct_answer:
        print("Correct!")
        return 1

    else:
        print("Incorrect!")
        print("Correct answer:", correct_answer)
        return 0


def run_quiz():
    score = 0

    question_list = list(QUESTIONS.items())

    random.shuffle(question_list)

    for number, item in enumerate(question_list, start=1):
        question = item[0]
        correct_answer = item[1]

        print(f"\nQuestion {number}")
        score += ask_question(question, correct_answer)

    print("\n--- QUIZ RESULTS ---")
    print("Your score:", score, "out of", len(QUESTIONS))


def main():
    print("WELCOME TO THE PYTHON QUIZ!")

    while True:
        run_quiz()

        play_again = input(
            "\nWould you like to play again? (yes/no): "
        ).strip().lower()

        if play_again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
