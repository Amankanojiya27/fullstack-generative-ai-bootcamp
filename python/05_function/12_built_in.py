# --------------------------------------------------------
# def chai_flavor(flavor="masala"):
#     """Return the flavor of chai."""
#     chai= "ginger"
#     return flavor

# print(chai_flavor.__doc__)
# print(chai_flavor.__name__)
# output - 
# Return the flavor of chai.
# chai_flavor

# ---------------------------------------------------
# print("\n")
def chai_flavor(flavor="masala"):
    chai= "ginger"
    """Return the flavor of chai."""
    return flavor

print(chai_flavor.__doc__)
print(chai_flavor.__name__)
# output - 
# None
# chai_flavor

# --------------------------------------------------
print("\n")
def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa
    :param chai: Number of chai (10 rupees each)
    :param samosa: Number of samosa (15 rupees each)
    :return: (total amount, thank you message)
    """
    total = chai * 10 + samosa * 15
    return total, "Thank you for visiting chaicode.com"


total, message = generate_bill(3, 3)
print(generate_bill.__doc__)
print("Total:", total)
print("Message:", message)
