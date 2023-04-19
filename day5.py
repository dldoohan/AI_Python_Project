class Dog:
    # Class attribute
    species = "Canis lupus familiaris"

    # Instance method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        print(f"{self.name} barks!")

# Create Dog objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Molly", 5)

# Access properties and call methods on objects
print(f"{dog1.name} is {dog1.age} years old and belongs to the {dog1.species} species.")
dog1.bark()
print(f"{dog2.name} is {dog2.age} years old and belongs to the {dog2.species} species.")
dog2.bark()
