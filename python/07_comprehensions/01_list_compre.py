# What is comprehension : comprehension is a concise and efficient way to create new sequences (lists, dictionaries, sets, or generators) using a single, readable line of code 

# List Comprehensions in Python
menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Tea"
]
# -------------------------------------
# Syntax - [expression for item in iterable if condition]
#             |             |         |       |  |
#             V             V         V       V  V
iced_tea = [ my_tea for my_tea in   menu     if "Iced" in my_tea]
print(iced_tea)
# -------------------------------------
len_tea = [tea for tea in menu if len(tea) < 12]
print(len_tea)