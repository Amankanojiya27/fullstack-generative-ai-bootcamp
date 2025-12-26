def process_order(item, quantity):
    try:
        price = {"masala":20}[item]
        cost = int(price) * int(quantity)
        print(f"total cost is {cost}")
    except KeyError:
        print("Key does not exist")
    except ValueError:
        print("Quantity must be Number")

process_order("ginger",2)
process_order("masala","two")
