class InvalidChaiError(Exception): pass

def bill(flavor, cup):
    menu = {"ginger":20, "masala":40}
    try:
        if flavor not in menu :
            raise InvalidChaiError("Sorry, We do not have this flavor")
        if not isinstance(cup, int):
            raise TypeError("Number of cups must be an integer")
        total = menu[flavor] * cup
        print(f"Your Bill for {cup} cups of {flavor} chai: rupees {total}")
    except Exception as e:
        print(f"Error: ", e)
    finally:
        print("Thank you for ordering")

bill("mint", 3)
bill("ginger", "two")
bill("masala", 2)
        
        