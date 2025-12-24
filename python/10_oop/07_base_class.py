# Demonstrating how to access a base (parent) class in Python
# Topics covered:
# - Code duplication
# - Explicit base class call
# - super()

class Chai:
    # Base (parent) class constructor
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength
        
        
# ❌ Example 1: Code duplication (NOT recommended)
# Rewriting the same code that already exists in the base class
# This makes maintenance harder and breaks DRY (Don't Repeat Yourself)
#
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level


# ⚠️ Example 2: Explicit base class call
# Directly calling the parent class constructor
# Works, but tightly couples the child class to the parent class name
#
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level


# ✅ Example 3: Using super() (BEST PRACTICE)
# Calls the parent class constructor in a clean and flexible way
# Recommended when working with inheritance
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        # super() automatically refers to the parent class (Chai)
        super().__init__(type_, strength)
        self.spice_level = spice_level
