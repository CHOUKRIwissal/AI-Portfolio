"""
Basic File Handling

Practice:
- Writing to a file
- Reading from a file
- Appending to a file
- Handling FileNotFoundError
"""


def save_message(message, filename):
    """Save a message to a file using write mode."""
    with open(filename, "w") as file:
        file.write(message)


def read_message(filename):
    """Read all lines from a file."""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            return lines

    except FileNotFoundError:
        print("File doesn't exist.")
        return []


def append_message(message, filename):
    """Add a message to the end of a file."""
    with open(filename, "a") as file:
        file.write(message + "\n")


# Practice
save_message("Hello Ali ", "message.txt")
append_message("This is a second message.", "message.txt")
print(read_message("message.txt"))