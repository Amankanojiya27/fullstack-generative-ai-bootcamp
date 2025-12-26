chai_menu = {"masala":30, "ginger":40}

# 1
chai_menu["elaichi"] # will give error 
print("Hello code") # will not run 

# 2
try:
     # Try to access a key that may not exist
    chai_menu["elaichi"]
except KeyError:
      # This block runs if KeyError occurs
    print("Key you trying to access is not exist")

# This line runs regardless of the error above
print("Hello code")

