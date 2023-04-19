# Add the following lines to the top of the "day4.py" file
import math_utils

# Use the math_utils module functions in the "day4.py" file
a = 10
b = 5

print("Addition:", math_utils.add(a, b))
print("Subtraction:", math_utils.subtract(a, b))
print("Multiplication:", math_utils.multiply(a, b))
print("Division:", math_utils.divide(a, b))

# Define a function to greet the user
def greet(name):
    print("Hello, " + name + "!")

# Call the greet function
greet("Alice")
greet("Bob")

# Define a function to calculate the square of a number
def square(x):
    return x * x

# Call the square function and display the result
result = square(5)
print("Square of 5 is:", result)