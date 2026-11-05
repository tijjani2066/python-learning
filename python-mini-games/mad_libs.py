
def create_story():
    print("WELCOME TO MAD LIBS!")
    print("Answer the questions to create your story.\n")

    name = input("Enter a name: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    food = input("Enter a food: ")
    adjective = input("Enter an adjective: ")

    print("\n--- YOUR STORY ---")
    print(f"One day, {name} went to {place}.")
    print(f"Suddenly, a {adjective} {animal} appeared.")
    print(f"They decided to share some {food} together.")
    print("It was an unforgettable day!")


def main():
    while True:
        create_story()

        play_again = input("\nWould you like to create another story? (yes/no): ").lower()

        if play_again != "yes":
            print("Thanks for playing Mad Libs!")
            break


if __name__ == "__main__":
    main()
