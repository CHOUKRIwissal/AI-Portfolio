"""
JSON File Handling

Practice:
- Saving Python data to JSON
- Loading JSON data
- Adding data to an existing JSON file
- Handling FileNotFoundError
"""

import json


def save_students(students, filename):
    """Save a list of students to a JSON file."""
    with open(filename, "w") as file:
        json.dump(students, file, indent=4)


def load_students(filename):
    """Load students from a JSON file."""
    try:
        with open(filename, "r") as file:
            students = json.load(file)
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
    {"name": "Sara", "age": 21, "grade": 17}
]

save_students(students, "students.json")

new_student = {"name": "Omar", "age": 22, "grade": 16}

# Add the new student to the JSON file
add_student("students.json", new_student)

print(load_students("students.json"))