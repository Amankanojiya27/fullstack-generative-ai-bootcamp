# -----------------------
# Inheritance example
# -----------------------
# Base class for chai
class BaseChai:
    def __init__(self,type_):
        self.type = type_
    
    def prepare(self):
        print(f"Preparing {self.type} chai....")

# Subclass inherits from BaseChai
# This is INHERITANCE: MasalaChai gets all features of BaseChai
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamon, ginger, cloves.")

# -----------------------
# Composition example
# -----------------------
# ChaiShop has a chai object inside it
# This is COMPOSITION: shop is composed of a chai object
class ChaiShop:
    chai_class = BaseChai  # default chai type
    
    def __init__(self):
        # Creating a chai object as part of the shop
        self.chai = self.chai_class("regular")
        
    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

# FancyChaiShop overrides chai_class to MasalaChai
# Can serve fancy chai
class FancyChaiShop(ChaiShop):
    chai_class = MasalaChai

# -----------------------
# Polymorphism example
# -----------------------
# Polymorphism: same interface (serve) works for different chai types
shop = ChaiShop()        # uses BaseChai
fancy = FancyChaiShop()  # uses MasalaChai

shop.serve()             # Works with BaseChai
fancy.serve()            # Works with MasalaChai

# Polymorphism in action: fancy.chai has an extra method
# Only MasalaChai has add_spices
fancy.chai.add_spices()
