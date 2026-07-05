print("                        PYTHON CALCULATOR")
name = input("Enter your name: ")
print("Welcome", name)

while True:

    print("\nChoose an operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Goodbye,", name)
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice.")
        continue

    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    if choice == "1":
        print("Answer:", number1 + number2)

    elif choice == "2":
        print("Answer:", number1 - number2)

    elif choice == "3":
        print("Answer:", number1 * number2)

    elif choice == "4":
        if number2 == 0:
            print("Cannot divide by zero.")
        else:
            print("Answer:", number1 / number2)