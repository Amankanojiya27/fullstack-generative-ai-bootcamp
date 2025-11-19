def serve_chai():
    chai_type = "Masala" # local scope
    print(f"Inside function {chai_type}")

chai_type = "lemon"
serve_chai()
print(f"Outside function: {chai_type}")


def chai_counter():
    chai_order= "lemon" # Enclosing scop
    def print_order():
        chai_order= "ginger"
        print(f"Inner: ", chai_order)
    print_order()
    print(f"Outer: ", chai_order)

chai_counter()

chai_order = "tulsi" # Global
print(f"Globle :",(chai_order).capitalize())