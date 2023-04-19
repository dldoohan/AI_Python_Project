# If statement
x = 5

if x > 0:
    print("x is positive")

# If-else statement
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")

# If-elif-else statement
y = 20

if y < 10:
    print("y is less than 10")
elif y>= 10 and y < 20:
    print("y is between 10 and 19")
else:
    print("y is 20 or greater")

# While loop
count = 0

while count < 5:
    print("Count:", count)
    count += 1

# For loop
names = ["Alice", "Bob", "Charlie", "David"]

for name in names:
    print("Hello, " + name + "!")