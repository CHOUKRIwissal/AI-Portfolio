# Simple backup system

import json
import csv
from datetime import datetime

def backup(data, name):
    """Save data to JSON and CSV"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save as JSON
    json_file = f"{name}_{timestamp}.json"
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)
    print(f" JSON saved: {json_file}")
    
    # Save as CSV (if data is list of dictionaries)
    if isinstance(data, list) and data and isinstance(data[0], dict):
        csv_file = f"{name}_{timestamp}.csv"
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f" CSV saved: {csv_file}")
    
    return True

def restore(filename):
    """Restore from JSON or CSV file"""
    try:
        if filename.endswith('.json'):
            with open(filename, 'r') as f:
                return json.load(f)
        elif filename.endswith('.csv'):
            with open(filename, 'r') as f:
                return list(csv.DictReader(f))
        else:
            print(" Only JSON or CSV files")
            return None
    except FileNotFoundError:
        print(f" File not found: {filename}")
        return None

# TEST 
print("=== Testing Backup System ===")

# Sample data
students = [
    {"name": "Alice", "age": 22, "grade": 85},
    {"name": "Bob", "age": 25, "grade": 92}
]

# Backup
backup(students, "students")

# Restore (you'll need to change the filename to what was created)
restored1 = restore("students_20260818_174326.json")
restored2 = restore("students")
restored3 = restore("students.json")
print("Restored 1:", restored1)
print("Restored 2:", restored2)
print("Restored 3:", restored3)