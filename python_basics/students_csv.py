"""
CSV File Handling

Practice:
- Writing dictionaries to CSV
- Reading CSV data
- Adding a student to a CSV file
- Handling FileNotFoundError
"""

import csv


def save_students(students, filename):
    """Save a list of students to a CSV file."""
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "age", "grade"]
        )

        writer.writeheader()
        writer.writerows(students)


def load_students(filename):
    """Load students from a CSV file."""
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            students = list(reader)
            return students

    except FileNotFoundError:
        print("File doesn't exist.")
        return []


def add_student(filename, student):
    """Load students, add a new student, and save the updated list."""
    students = load_students(filename)
    students.append(student)
    save_students(students, filename)


# Example data
students = [
    {"name": "Ali", "age": 20, "grade": 15},
    {"name": "Sara", "age": 21, "grade": 17},
    {"name": "Omar", "age": 22, "grade": 16}
]
save_students(students, "students.csv")

new_student = {"name": "Yassine", "age": 23, "grade": 18}
add_student("students.csv", new_student)

print(load_students("students.csv"))