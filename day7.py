def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    except TypeError:
        print("Error: Invalid input type!")
        return None
    else:
        return result
    
print("Example 1:", divide(4, 2)) # This shoud not print an error
print("Example 2:", divide(4, 0)) # This should print a ZeroDivisionError
print("Example 3:", divide("4", 2)) # This should print an TypeError

class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        self.message = f"Invalid age: {age}. Age must be between 18 and 99."
        super().__init__(self.message)

def validate_age(age):
    if age < 18 or age > 99:
        raise InvalidAgeError(age)
    else:
        return f"Valid age: {age}"

try:
    print(validate_age(25))
    print(validate_age(150))
except InvalidAgeError as e:
    print(e)