# Defining a class ChaiOrder
class ChaiOrder:
    
    # Constructor method, called when creating a new object
    # Initializes object variables: type and size
    def __init__(self, type_, size):
        self.type = type_
        self.size = size
    
    # Method to summarize the order
    def summary(self):
        return f"{self.size}ml of {self.type} chai"
    

# Creating first order object
order = ChaiOrder("Masala", 150)
print(order.summary())  # Output: 150ml of Masala chai

# Creating second order object
order_two = ChaiOrder("Ginger", 100)
print(order_two.summary())  # Output: 100ml of Ginger chai
