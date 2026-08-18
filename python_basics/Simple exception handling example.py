# Simple exception handling example

def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    except TypeError:
        print("Please use numbers only!")
        return None

# Test 
safe_divide(10, 2)   
safe_divide(10, 0)   
safe_divide(10, "a") 

# Custom exception
class AgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative")
    if age > 150:
        raise AgeError("Age cannot be over 150")
    print(f"Age {age} is valid")

# Test 
try:
    check_age(25)    
    check_age(-5)    
except AgeError as e:
    print(f"Error: {e}")