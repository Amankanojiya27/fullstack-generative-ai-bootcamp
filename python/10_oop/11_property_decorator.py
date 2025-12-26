
# Class to represent a person's age with rules for valid ages
class YourAge:
    # Constructor method
    def __init__(self, age):
        # This calls the setter method to validate the age
        self._age = age  # using underscore age '_age' which represent its specials "we don't call it as age, we call it as underscore age. And this underscore doesn't mean on its own anything. It's just a Python way of saying that, hey, this is an interesting property. This shouldn't be allowed to touch directly. There needs to be a way of reading, this property as well as writing to this property. And this is a symbol which is used throughout the industry. So whenever you see an underscore that means, this is having something special as a meaning. Now surely this can be done without underscore as well. But this is such a common thing and Python also knows this. So Python doesn't treat this in a lot of places as underscore age. You'll see this as age treated like this."

    # ====== Getter ======
    # This method is called when we access 'man.age'
    @property
    def age(self):
        # Returns the stored age + 2 (for demonstration purposes)
        return self._age + 2

    # ====== Setter ======
    # This method is called when we assign a value like 'man.age = 29'
    @age.setter
    def age(self, age):
        # Validate that age is between 18 and 35
        if 18 <= age <= 35:
            self._age = age  # Store the value in a private variable
        else:
            # Raise an error if the age is invalid
            raise ValueError("Age should be between 18 and 35 years")


# Create an object with age 21
man = YourAge(21)

# Access the age using the getter
# This will call the 'age' property method
print(man.age)  # Output: 23 (21 + 2 because of getter)

# Update the age using the setter
man.age = 29

# Access the age again using the getter
print(man.age)  # Output: 31 (29 + 2 because of getter)
