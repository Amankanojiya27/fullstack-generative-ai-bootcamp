favourite_chais =[
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]

# unique_chai = {chai for chai in favourite_chais}
# unique_chai = {chai for chai in favourite_chais if len(chai) <0}
# print(unique_chai)

# advance example 

recipes = {
    "Masala Chai": ["ginger","cardamom", "clover"],
    "Elaichi Chai": ["cardamon","milk"],
    "Spicy Chai": ["ginger","black paper", "clover"],
}

unique_spipes = {spice for ingrediants in recipes.values() for spice in ingrediants   }

print(unique_spipes)
