# Creating a class named Chai
# A class is like a blueprint or template
class Chai:
    pass  # 'pass' means "do nothing for now"

# Creating another class named Chaitime
class Chaitime:
    pass

# Printing the type of the class Chai itself
# This shows that a class is also an object in Python
print(type(Chai))

# Creating an object (instance) of the Chai class
# ginger_chai is made using the Chai blueprint
ginger_chai = Chai() # this create object which inherit class Chai() 

# Printing the type of the object ginger_chai
print(type(ginger_chai))

# Checking if the type of ginger_chai is exactly Chai
# This will return True
print(type(ginger_chai) is Chai)

# Checking if the type of ginger_chai is Chaitime
# This will return False because ginger_chai was created from Chai
print(type(ginger_chai) is Chaitime)
