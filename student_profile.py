name = input("Enter student name: ")
level = input("Enter level: ")
department = input("Enter department: ")
cgpa = float(input("Enter CGPA: "))
age = int(input("Enter Age: "))

while name == "":
    print("Name cannot be empty.")
    name = input("Enter student name: ")

student = {
    "name": name,
    "level": level,
    "department": department,
    "CGPA": cgpa,
    "Age": age
}

print("\nStudent Profile")

for key in student:
    print(key, ":", student[key])

print("\nProfile saved successfully!")

file = open("student_profile.txt", "w")

for key in student:
    file.write(key + ": " + str(student[key]) + "\n")

file.close()

choice = input("\nDo you want to view the saved profile? (yes/no): ")

if choice.lower() == "yes":
    file = open("student_profile.txt", "r")
    content = file.read()
    print("\nSaved Profile")
    print(content)
    file.close()
else:
    print("Goodbye!")