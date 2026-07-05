tasks = []

while True:

    task = input("Enter a task (or type 'stop' to finish): ")

    if task.lower() == "stop":
        break

    tasks.append(task)

print("\nMy Tasks")

for task in tasks:
    print("-", task)

choice = input("\nDo you want to save your tasks? (yes/no): ")

if choice.lower() == "yes":

    file = open("tasks.txt", "w")

    for task in tasks:
        file.write(task + "\n")

    file.close()

    print("Tasks saved successfully!")

else:
    print("Tasks not saved.")