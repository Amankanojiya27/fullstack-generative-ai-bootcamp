# Defining a class Chaicup
class Chaicup:
    # Class variable (default size for all cups)
    size = 150
    
    # Method to describe the cup
    # 'self' refers to the object calling the method
    def describe(self):
        return f"A {self.size}ml chai cup"
    

# Creating the first cup object
cup = Chaicup()

# Calling the method using the object
print(cup.describe())  # Output: A 150ml chai cup

# Calling the method using the class, passing the object manually
# This works because 'self' will refer to 'cup'
print(Chaicup.describe(cup))  # Output: A 150ml chai cup

# Creating a second cup object
cup_two = Chaicup()

# Changing the size for this specific object only
cup_two.size = 100

# Calling the method using the class and passing the object
# Output reflects the object-specific size
print(Chaicup.describe(cup_two))  # Output: A 100ml chai cup
