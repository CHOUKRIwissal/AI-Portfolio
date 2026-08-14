students = [
    {"name": "sarah", "grades": [18]},
    {"name": "layla", "grades": [19]}
]


def add_student():
    name = input("Add student: ")
    students.append({"name": name, "grades": []})


def add_grade():
    name = input("Student name: ")
    grade = float(input("Add grade: "))

    for student in students:
        if student["name"] == name:
            student["grades"].append(grade)
            print("Grade added")
            return

    print("Student not found")


def average(student):
    if len(student["grades"]) == 0:
        return 0

    return sum(student["grades"]) / len(student["grades"])


def top_3_students():
    ranked = sorted(students, key=average, reverse=True)

    print("Top 3 students:")

    for student in ranked[:3]:
        print(student["name"], average(student))


def display_students():
    for student in students:
        print(
            student["name"],
            student["grades"],
            "Average:",
            average(student)
        )


while True:

    print("\n 1. Add student \n 2. Add grade \n 3. Top 3 students\n 4. Display students\n 5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        add_grade()

    elif choice == "3":
        top_3_students()

    elif choice == "4":
        display_students()

    elif choice == "5":
        break

    else:
        print("Invalid choice")