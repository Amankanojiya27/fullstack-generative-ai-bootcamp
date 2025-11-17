
#set
essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices  # | work as union oprater in set 
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices # & work as common oprater in set
print(f"common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices # - works as difference operator in set - ( difference just means "what's in the first set, but not in the second.)
print(f"Only in essential spices: {only_in_essential}")

print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}") # in - is know as membership test

# Set is mutable in Python, so the ID remains same even after modification in Memory

