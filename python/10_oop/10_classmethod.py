# This class represents a chai (tea) order
class ChaiOrder:

    # Constructor method
    # It runs automatically when a new object is created
    # 'self' refers to the current object
    def __init__(self, tea_type, sweetness_level, cup_size):
        self.tea_type = tea_type           # Store the tea type (ginger, lemon, masala, etc.)
        self.sweetness_level = sweetness_level   # Store sweetness level (low, medium, high)
        self.cup_size = cup_size           # Store the size of the tea

    # Class method
    # Used to create an object using dictionary data
    # 'cls' refers to the class itself (ChaiOrder)
    @classmethod
    def from_dict(cls, data_dict):
        # Pass dictionary values to the constructor
        return cls(
            data_dict["tea_type"],
            data_dict["sweetness"],
            data_dict["size"],
        )

    # Class method
    # Used to create an object from a string
    # Example string: "lemon-low-small"
    @classmethod
    def from_string(cls, string_data):
        # Split the string using "-" as a separator
        tea_type, sweetness_level, cup_size = string_data.split("-")

        # Create and return a new ChaiOrder object
        return cls(tea_type, sweetness_level, cup_size)


# Utility class
# Contains helper methods that are not tied to a specific object
class Utils:

    # Static method
    # Does not need 'self' or 'cls'
    # Can be called directly using the class name
    @staticmethod
    def is_valid_size(size):
        # Check whether the given size is valid
        return size in ["Small", "Medium", "Large"]


# Calling the static method using the class name
size = "medium"
print(f"size '{size}' is valid ::",Utils.is_valid_size(size))  # True


# Creating an object using the from_dict class method
order1 = ChaiOrder.from_dict({
    "tea_type": "ginger",
    "sweetness": "medium",
    "size": "large",
})

# Creating an object using the from_string class method
order2 = ChaiOrder.from_string("lemon-low-small")

# Creating an object using the normal constructor
order3 = ChaiOrder("masala", "high", "small")


# Printing the objects
# This shows memory addresses because __str__ is not defined
print("order1 ::",order1)  # <__main__.ChaiOrder object at ...>
print("order2 ::",order2)
print("order3 ::",order3)


# __dict__ shows all attributes stored inside the object
# Useful for beginners to understand what data the object holds
print("order1 ::",order1.__dict__)
print("order2 ::",order2.__dict__)
print("order3 ::",order3.__dict__)
