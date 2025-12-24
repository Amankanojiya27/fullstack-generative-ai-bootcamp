# Defining a class named Chai
class Chai:
    # Class variables (shared by all objects)
    temperature = "hot"
    strength = "strong"

# Creating an object (instance) of the class
cutting = Chai()

# Accessing a class variable through the object
print(cutting.temperature)  # Output: hot

# Changing the object's temperature
# This creates a new variable specifically for this object
cutting.temperature = "mild"

# Adding a new object-specific variable
cutting.cup = "small"

print("After changing:", cutting.temperature)  # Output: mild
print("Cup size:", cutting.cup)                # Output: small

# Accessing the class variable directly remains unchanged
print("Direct look into the class:", Chai.temperature)  # Output: hot

# Deleting the object-specific variable
del cutting.temperature   # removes the object-specific 'temperature'
del cutting.cup           # removes the object-specific 'cup'

# After deletion:
# - temperature now refers back to the class variable
# - cup does not exist anymore (this will cause an error)
print(cutting.temperature)  # Output: hot (falls back to class variable)
print(cutting.cup)          # Error! 'cutting' no longer has 'cup'
