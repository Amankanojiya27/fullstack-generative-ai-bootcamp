# Class and Object Namespace

# Defining a class named Chai
class Chai:
    # This is a class variable/property
    # It belongs to the class itself
    origin = "Indian"
    
# Accessing the class variable using the class name
print(Chai.origin)

# Adding a new class variable dynamically
Chai.is_hot = True
print(Chai.is_hot)

# Creating an object (instance) from the Chai class
masala = Chai()

# Accessing class variables using the object
# Objects can read class variables
print(f"masala {masala.origin}")
print(f"masala {masala.is_hot}")

# Creating an object-specific variable
# This does NOT change the class variable
masala.is_hot = False

# Accessing the class variable again
print("Class:", Chai.is_hot)

# Accessing the object variable
print("masala", masala.is_hot)
